#!/usr/bin/env python3
"""Synthetic, isolated Git fixture for the external Markdown auditor; no product code runs."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

AUDITOR = Path(__file__).with_name('pr34-markdown-ast-audit.py')
SOURCE_COMMIT = '80db1db1b3a93c880e8cedbc70c556725f6da368'

with tempfile.TemporaryDirectory(prefix='pr34-fixture-') as temp:
    root = Path(temp)
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=root).decode().strip()
    git('init', '-q')
    git('config', 'user.name', 'Fixture')
    git('config', 'user.email', 'fixture@example.invalid')
    source = '''# Source heading

[x](b.md#source-heading) [y](b.md#target-heading) [z](b.md#explicit) [asset](assets/logo.png) [dir](assets/)

[inline](b.md) [reference][ref] ![image](assets/logo.png) [only](unique.md)

[ref]: b.md

`[literal](no.md)`

```md
[fenced](no.md)
```

<a href="b.md">html inline</a>

<div>
<img src="assets/logo.png">
</div>

[escape](space%20name.md) [traversal](../outside.md) [bad](broken%ZZ.md)
'''
    files = {'a.md': source, 'b.md': '# Target heading\n\n<a id="explicit"></a>\n',
             'space name.md': '# Space\n', 'unique.md': '# Unique\n', 'assets/logo.png': 'png'}
    for name, content in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
    source_blob = git('hash-object', 'a.md')
    row = f'| `a.md` | `{source_blob}` | `1` | `link` | `unique.md` |\n'
    for number in range(1, 10):
        path = root / f'docs/04-auditorias/pr33-reference-manifest-regex-batch-{number:02d}-2026-10-23.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        changed = f'| `a.md` | `{"0" * 40}` | `1` | `link` | `unique.md` |\n'
        path.write_text(row * 2 + changed if number == 1 else '', encoding='utf-8')
    git('add', '.')
    git('commit', '-qm', 'synthetic fixture')
    commit = git('rev-parse', 'HEAD')
    original = AUDITOR.read_text(encoding='utf-8')
    assert original.count(SOURCE_COMMIT) == 1
    adapted = root / 'audit.py'
    adapted.write_text(original.replace(SOURCE_COMMIT, commit), encoding='utf-8')
    outputs = [root / 'one.json', root / 'two.json']
    for output in outputs:
        subprocess.run([sys.executable, str(adapted), str(output)], cwd=root, check=True)
    assert outputs[0].read_bytes() == outputs[1].read_bytes(), 'serialization differs'
    manifest = json.loads(outputs[0].read_text(encoding='utf-8'))
    rows = [e for e in manifest['entries'] if e['source_path'] == 'a.md']
    def entry(kind, target):
        matches = [e for e in rows if e['syntax_kind'] == kind and e['parsed_target'] == target]
        assert matches, (kind, target)
        return matches[0]
    assert entry('link', 'b.md#source-heading')['fragment_status'] == 'UNVERIFIED'
    assert entry('link', 'b.md#target-heading')['fragment_status'] == 'CANDIDATE_HEADING_MATCH_UNVERIFIED'
    assert entry('link', 'b.md#explicit')['fragment_status'] == 'EXISTS_EXPLICIT_ID'
    assert entry('link', 'assets/logo.png')['local_target_status'] == 'EXISTS_FILE'
    assert entry('link', 'assets/')['local_target_status'] == 'EXISTS_DIRECTORY'
    assert entry('image', 'assets/logo.png')['local_target_status'] == 'EXISTS_FILE'
    assert entry('html_href', 'b.md')['local_target_status'] == 'EXISTS_FILE'
    assert entry('html_src', 'assets/logo.png')['local_target_status'] == 'EXISTS_FILE'
    assert entry('link', 'space%20name.md')['local_target_status'] == 'EXISTS_FILE'
    assert entry('link', '../outside.md')['local_target_status'] == 'OUTSIDE_REPOSITORY'
    assert entry('link', 'broken%25ZZ.md')['local_target_status'] == 'MISSING_PATH'
    assert all(e['parsed_target'] != 'no.md' for e in rows), 'literal code extracted'
    assert len([e for e in rows if e['syntax_kind'] == 'link' and e['parsed_target'] == 'b.md']) == 2
    assert entry('html_src', 'assets/logo.png')['occurrence_in_source_order'] < entry('link', 'space%20name.md')['occurrence_in_source_order']
    comparison = manifest['historical_regex_comparison']
    assert comparison['same_blob_observations_compared'] == 2
    assert comparison['same_blob_observations_found_as_rendered_links'] == 1
    assert comparison['same_blob_observations_unmatched'] == 1
    assert comparison['observations_on_changed_or_absent_blobs_not_comparable'] == 1
    print('PASS: paths, target anchors, literal code, references, images, HTML, order, encoding, traversal, multiplicity and determinism')
