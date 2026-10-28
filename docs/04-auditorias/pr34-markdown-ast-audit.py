#!/usr/bin/env python3
"""Read-only external Markdown corpus audit; never imports or executes project code."""
from __future__ import annotations

import hashlib
from collections import Counter
import html.parser
import json
import os
import posixpath
import re
import subprocess
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt, __version__ as MARKDOWN_IT_VERSION
import linkify_it
import mdurl
import uc_micro

SOURCE_COMMIT = "80db1db1b3a93c880e8cedbc70c556725f6da368"
PARSER_VERSION = "4.2.0"
PARSER_CONFIG = "MarkdownIt('default', html=True, linkify=True, typographer=False)"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], stderr=subprocess.DEVNULL)


def slugify(text: str) -> str:
    # Candidate GitHub-style slug only. Anchor results remain UNVERIFIED.
    text = unicodedata.normalize("NFC", text).lower()
    text = re.sub(r"\s", "-", text)
    return "".join(ch for ch in text if ch == "-" or ch == "_" or ch.isalnum())


class HTMLCollector(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k.lower(): v for k, v in attrs}
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if tag.lower() == "a" and values.get("name"):
            self.ids.append(values["name"] or "")
        if values.get("href") is not None:
            self.links.append(("html_href", values["href"] or ""))
        if values.get("src") is not None:
            self.links.append(("html_src", values["src"] or ""))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: pr34-markdown-ast-audit.py OUTPUT.json")
    expected_dependencies = {"markdown-it-py": "4.2.0", "linkify-it-py": "2.0.3", "mdurl": "0.1.2", "uc-micro-py": "2.0.0"}
    actual_dependencies = {"markdown-it-py": MARKDOWN_IT_VERSION, "linkify-it-py": linkify_it.__version__,
                           "mdurl": mdurl.__version__, "uc-micro-py": uc_micro.__version__}
    if actual_dependencies != expected_dependencies:
        raise SystemExit(f"dependency versions differ: {actual_dependencies}")
    output_path = sys.argv[1]
    root = git("rev-parse", "--show-toplevel").decode().strip()
    os.chdir(root)
    tree = git("ls-tree", "-r", "-z", SOURCE_COMMIT)
    files: list[dict[str, str]] = []
    tracked_paths: set[str] = set()
    for record in tree.split(b"\0"):
        if not record:
            continue
        meta, path_bytes = record.split(b"\t", 1)
        mode, kind, oid = meta.decode().split()
        path = path_bytes.decode("utf-8", "surrogateescape")
        if kind == "blob":
            tracked_paths.add(path)
        if kind == "blob" and path.endswith(".md"):
            files.append({"path": path, "blob_sha": oid})
    files.sort(key=lambda item: item["path"])
    file_set = tracked_paths
    dir_set = set()
    for tracked_path in tracked_paths:
        parts = tracked_path.split("/")[:-1]
        for i in range(1, len(parts) + 1):
            dir_set.add("/".join(parts[:i]))
    md = MarkdownIt("default", {"html": True, "linkify": True, "typographer": False})
    entries: list[dict] = []
    diagnostics: list[dict] = []
    totals = {"link": 0, "image": 0, "html_href": 0, "html_src": 0}

    anchor_cache: dict[str, tuple[list[str], set[str]]] = {}

    def anchors(target_path: str) -> tuple[list[str], set[str]]:
        if target_path in anchor_cache:
            return anchor_cache[target_path]
        if target_path not in {item["path"] for item in files}:
            return [], set()
        target_source = git("show", f"{SOURCE_COMMIT}:{target_path}").decode("utf-8", "replace")
        parsed_tokens = md.parse(target_source)
        headings: list[str] = []
        explicit_ids: set[str] = set()
        duplicate_counts: dict[str, int] = {}
        for i, token in enumerate(parsed_tokens):
            if token.type == "heading_open" and i + 1 < len(parsed_tokens) and parsed_tokens[i + 1].type == "inline":
                inline = parsed_tokens[i + 1]
                title = "".join(child.content for child in (inline.children or [])
                               if child.type in {"text", "code_inline", "html_inline"})
                base = slugify(title)
                count = duplicate_counts.get(base, 0)
                duplicate_counts[base] = count + 1
                headings.append(base if count == 0 else f"{base}-{count}")
            if token.type == "inline":
                for child in token.children or []:
                    if child.type in {"html_inline", "html_block"}:
                        collector = HTMLCollector()
                        collector.feed(child.content)
                        explicit_ids.update(collector.ids)
            elif token.type == "html_block":
                collector = HTMLCollector()
                collector.feed(token.content)
                explicit_ids.update(collector.ids)

        anchor_cache[target_path] = (headings, explicit_ids)
        return headings, explicit_ids

    for file in files:
        path, blob = file["path"], file["blob_sha"]
        source = git("show", f"{SOURCE_COMMIT}:{path}").decode("utf-8", "replace")
        tokens = md.parse(source)
        def add(kind: str, target: str, token, occurrence: int) -> None:
            totals[kind] += 1
            line_map = token.map
            source_start = line_map[0] + 1 if line_map else None
            source_end = line_map[1] if line_map else None  # one-based inclusive end
            lines = source.splitlines()
            snippet = "\n".join(lines[line_map[0]:line_map[1]]) if line_map else ""
            raw_target_status = "TEXT_MATCH_IN_BLOCK_POSITION_UNPROVEN" if target and target in snippet else "NOT_EXPOSED_OR_NOT_FOUND"
            raw_target = target if raw_target_status == "TEXT_MATCH_IN_BLOCK_POSITION_UNPROVEN" else None
            parsed = urlsplit(target)
            scheme = parsed.scheme.lower()
            local_status = "NOT_APPLICABLE"
            resolved_path = None
            fragment_status = "NOT_APPLICABLE"
            if scheme or target.startswith("//"):
                local_status = "EXTERNAL_SCHEME"
            else:
                raw_path = unquote(parsed.path, errors="replace")
                if re.search(r"%(?![0-9A-Fa-f]{2})", parsed.path):
                    local_status = "INVALID_PERCENT_ENCODING"
                else:
                    joined = posixpath.normpath(posixpath.join(posixpath.dirname(path), raw_path)) if raw_path else path
                    if joined == ".." or joined.startswith("../") or joined.startswith("/"):
                        local_status = "OUTSIDE_REPOSITORY"
                    else:
                        resolved_path = joined
                        if joined in file_set:
                            local_status = "EXISTS_FILE"
                        elif joined in dir_set:
                            local_status = "EXISTS_DIRECTORY"
                        elif raw_path == "" and joined == path:
                            local_status = "EXISTS_FILE"
                        else:
                            local_status = "MISSING_PATH"
                if parsed.fragment and resolved_path is not None:
                    headings, explicit_ids = anchors(resolved_path)
                    fragment = unquote(parsed.fragment, errors="replace")
                    if fragment in explicit_ids:
                        fragment_status = "EXISTS_EXPLICIT_ID"
                    elif fragment in headings:
                        fragment_status = "CANDIDATE_HEADING_MATCH_UNVERIFIED"
                    else:
                        fragment_status = "UNVERIFIED"
            entries.append({
                "source_path": path, "source_blob_sha": blob,
                "source_line_start": source_start, "source_line_end": source_end,
                "position_precision": "BLOCK_RANGE_ONLY" if line_map else "POSITION_UNAVAILABLE",
                "syntax_kind": kind, "occurrence_in_source_order": occurrence,
                "raw_target": raw_target, "raw_target_status": raw_target_status,
                "parsed_target": target, "normalized_path": resolved_path,
                "query": parsed.query or None, "fragment": parsed.fragment or None,
                "local_target_status": local_status, "fragment_status": fragment_status,
                "parser": "markdown-it-py", "parser_version": PARSER_VERSION,
            })

        occurrence = 0
        for token in tokens:
            if token.type == "html_block":
                collector = HTMLCollector()
                collector.feed(token.content)
                for kind, target in collector.links:
                    occurrence += 1
                    add(kind, target, token, occurrence)
            elif token.type == "inline":
                for child in token.children or []:
                    if child.type == "link_open":
                        occurrence += 1
                        add("link", child.attrGet("href") or "", token, occurrence)
                    elif child.type == "image":
                        occurrence += 1
                        add("image", child.attrGet("src") or "", token, occurrence)
                    elif child.type == "html_inline":
                        collector = HTMLCollector()
                        collector.feed(child.content)
                        for kind, target in collector.links:
                            occurrence += 1
                            add(kind, target, token, occurrence)

    entries.sort(key=lambda e: (e["source_path"], e["source_line_start"] or 0,
                                e["syntax_kind"], e["parsed_target"], e["occurrence_in_source_order"]))

    # Compare the historical regex observations only where the exact source blob is unchanged.
    historical_rows: list[tuple[str, str, str]] = []
    row_pattern = re.compile(r"^\| `([^`]+)` \| `([0-9a-f]{40})` \| `([0-9]+)` \| `([^`]+)` \| `(.*)` \|$")
    for batch_number in range(1, 10):
        batch_path = f"docs/04-auditorias/pr33-reference-manifest-regex-batch-{batch_number:02d}-2026-10-23.md"
        batch_text = git("show", f"{SOURCE_COMMIT}:{batch_path}").decode("utf-8", "replace")
        for line in batch_text.splitlines():
            match = row_pattern.match(line)
            if match:
                historical_rows.append((match.group(1), match.group(2), match.group(5).replace(r"\|", "|")))
    current_blobs = {item["path"]: item["blob_sha"] for item in files}
    rendered_targets = Counter((item["source_path"], item["source_blob_sha"], item["parsed_target"])
                               for item in entries if item["syntax_kind"] == "link")
    comparable_rows = [row for row in historical_rows if current_blobs.get(row[0]) == row[1]]
    changed_blob_rows = [row for row in historical_rows if current_blobs.get(row[0]) != row[1]]
    matched_comparable = []
    unmatched_comparable = []
    for row in comparable_rows:
        if rendered_targets[row] > 0:
            matched_comparable.append(row)
            rendered_targets[row] -= 1
        else:
            unmatched_comparable.append(row)
    historical_comparison = {
        "historical_source_commit": "3ff2f14fbc96c3f73768f1e870491155f36144b6",
        "historical_markdown_denominator": 103,
        "historical_regex_observations": len(historical_rows),
        "historical_files_with_observations": len({row[0] for row in historical_rows}),
        "same_blob_observations_compared": len(comparable_rows),
        "same_blob_observations_found_as_rendered_links": len(matched_comparable),
        "same_blob_observations_unmatched": len(unmatched_comparable),
        "observations_on_changed_or_absent_blobs_not_comparable": len(changed_blob_rows),
        "unmatched_comparable_observations": [{"path": row[0], "blob_sha": row[1], "target": row[2]}
                                               for row in unmatched_comparable],
        "interpretation": "Positive-only historical regex evidence; does not measure regex false negatives. Different blobs are not compared as if they were the same input.",
    }
    status_counts: dict[str, int] = {}
    for item in entries:
        status_counts[item["local_target_status"]] = status_counts.get(item["local_target_status"], 0) + 1
        if item["local_target_status"] in {"MISSING_PATH", "OUTSIDE_REPOSITORY", "INVALID_PERCENT_ENCODING"}:
            diagnostics.append({k: item[k] for k in (
                "source_path", "source_blob_sha", "source_line_start", "syntax_kind",
                "parsed_target", "normalized_path", "local_target_status")})
    manifest = {
        "schema": "the-machine-markdown-ast-audit-v1",
        "source_commit": SOURCE_COMMIT,
        "audit_utility_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        "source_tree_sha": git("rev-parse", f"{SOURCE_COMMIT}^{{tree}}").decode().strip(),
        "parser": "markdown-it-py", "parser_version": PARSER_VERSION,
        "dependencies": actual_dependencies,
        "python_version": sys.version.split()[0], "configuration": PARSER_CONFIG,
        "profile_notes": [
            "CommonMark-based markdown-it-py default preset with GFM-like tables/strikethrough and linkify enabled.",
            "Not GitHub's renderer: HTML tag filtering, GitHub-specific heading slugs and rendering equivalence are not certified.",
            "HTML href/src extracted from rendered HTML AST tokens; raw source lexemes may be unavailable.",
            "Child-token source coordinates are not provided by parser; reported positions are containing block ranges only.",
            "Local path existence is checked against tracked blobs/directories at the frozen Git tree; external URLs are not fetched.",
            "Anchor checks are candidate-only; no anchor is certified against GitHub rendering."
        ],
        "inventory_count": len(files), "inventory": files,
        "link_counts_by_kind": totals, "local_status_counts": status_counts,
        "historical_regex_comparison": historical_comparison,
        "diagnostics": diagnostics, "entries": entries,
    }
    encoded = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with open(output_path, "wb") as stream:
        stream.write(encoded)
    print(f"{output_path}: sha256={hashlib.sha256(encoded).hexdigest()} files={len(files)} entries={len(entries)} diagnostics={len(diagnostics)}")


if __name__ == "__main__":
    main()
