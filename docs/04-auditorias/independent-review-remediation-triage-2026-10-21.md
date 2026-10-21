# Independent review remediation — triage and ratification boundary

**Date:** 2026-10-21  
**Status:** CANDIDATE / NON-NORMATIVE · HOLD / NO-GO  
**Base:** master at `0015cd33243827a0eb99c533107c8480055ebd0f`  
**Source:** Independent technical review supplied by the project owner (REV-01..REV-20). Its ZIP-based findings are **claims to verify**, not automatically accepted facts. This document does not alter ADRs, approve G2.1/G2.2, authorize code, or close gaps.

## Actionable classification

| Findings | Treatment | Acceptance evidence |
|---|---|---|
| REV-02, REV-04 | Verify prerequisites for G2.2 and exclusion of original E-10 from F-01..F-10 execution | Exact references in staged protocol, comparative contract and original E-10 contract; no implicit exception |
| REV-07, REV-08 | Compare executive-summary recommendations and restore original meanings of F/E/R IDs | Side-by-side literal definitions with source section and explicit aliases for any *new* variant |
| REV-09, REV-17 | Restore second-domain transfer, extensibility, serialization and profile versioning as comparison requirements | Domain-neutral fixtures and at least two declared profiles before any comparative run |
| REV-10, REV-12, REV-14 | Namespace colliding IDs; treat authenticity as fixture input rather than claimed crypto verification; make boundary tests non-vacuous | Namespace map, positive/negative controls and independent observer definition |
| REV-11, REV-18 | Correct security verification coverage and avoid exactly-once claims | Trace TH-016 to SEC-REQ-015; separate designed vs executed; document unknown remote outcomes |
| REV-19, REV-20 | Separate laboratory interchange format from durable persistence; fix current editorial inconsistencies | Explicit format proposal and no claim of approved dependencies |
| REV-01, REV-03, REV-05, REV-06, REV-15, REV-16 | **Owner ratification required** | Signed decision record; no unilateral gate/authority/license/independence claims |
| REV-13 | **Experiment required** | Explicit registration order and injected-time hypothesis; not a verified clock guarantee |

**Original E-10 remains BLOCKED.** A logical in-memory hiding exercise, if ever approved, must receive a distinct ID and must not be represented as physical deletion or legal compliance.

## Owner ratification sheet (PROPOSALS, not decisions)

1. **Scope (DEC-01):** choose offline synthetic epistemic comparison only; no production, real data, network, persistence, or gateway.
2. **Representation (DEC-02):** authorize *comparison only* of R1/R2/hybrid C/domain-specific D; no winner before evidence; include a second domain.
3. **Pure core (DEC-03):** propose explicit injected clocks, ordering and immutable rules as input; deterministic behavior is a hypothesis.
4. **Privacy (DEC-04):** exclude original E-10 from the first run; keep BLOCKED; any logical simulation separate and explicitly authorized.
5. **Oracles (DEC-05):** include negative cases, justified abstention and versioned rules; preserve original F/E/L/R meanings.
6. **Storage (DEC-06):** defer persistent storage, but approve an independently specified *synthetic laboratory interchange* format before G2.2.
7. **License (DEC-07):** decide license/ownership and visibility before distribution or outside contributions; do not assume MIT/Apache is approved.
8. **Authorization (DEC-08):** retain HOLD/NO-GO. Distinguish disposable laboratory code from production code **before** any G2.2 permission.
9. **Gates / GAP-010:** select one authoritative G0..G5 definition, resolve contradictory historical definitions, define documentary precedence, reviewer independence, recorded signatures and revocation. Merge is not ratification.
10. **G3:** distinguish permission to start product code from permission to merge it; document scoped exceptions and their expiration before approval.

## Implementation boundary

No Rust, Cargo, executable harness, CI, security experiment, accepted ADR, GO, or merge is authorized by this PR. G2.1 remains pending and G2.2 blocked.

## Next action

A reviewer must validate each cited REV finding against exact files in current master, correct only **verified** documentary contradictions in a separate change set, and return a concise owner ratification sheet. Do not silently rewrite historical documents or claim that unverified ZIP assertions were independently reproduced.

## Verified remediation log (current PR branch; 2026-10-21)

| REV | Source-level evidence | Status | Change |
|---|---|---|---|
| REV-02 | `staged-authorization-protocol-v1.md` G2.2 originally lacked the four mandatory prerequisites listed in `comparative-contract-v1.md` §1.2 | CONFIRMED / DOCUMENTARY FIX | G2.2 entry now includes normalized fixtures, versioned oracle, tolerances and output schema; authorization still required |
| REV-04 | `staged-authorization-protocol-v1.md` G2.3 originally said F-01..F-10 despite E-10 BLOCKED in `offline-experiment-contract-candidate-v0.md` §4 | CONFIRMED / DOCUMENTARY FIX | G2.3 defaults to F-01..F-09; additional cases need explicit approval |
| REV-07 | `executive-summary-v1.md` §§4–5 originally recommended both option I and option II | CONFIRMED / DOCUMENTARY FIX | Single conditional recommendation: fix contradictions before G2.1 deliberation |
| REV-08 (partial) | `precode-decision-protocol-v0.md` F-03/F-10 and `offline-experiment-contract-candidate-v0.md` E-03/E-10 differ from `traceability-matrix-v1.md` | CONFIRMED / PARTIAL FIX | Restored F-03 provenance-only and F-10 privacy/history meaning in matrix; remaining R mapping still requires review |
| REV-09 | `precode-decision-protocol-v0.md` comparative criteria included second domain, serialization/versioning and coupling absent from `comparative-contract-v1.md` §4.2 | CONFIRMED / DOCUMENTARY FIX | Added explicit cross-domain, lifecycle and coupling criteria; no experiments performed |
| REV-11 (partial) | `requirements.md` SEC-REQ-015..017 were pending; `verification-plan.md` stopped at SEC-014 | CONFIRMED / PROPOSED FIX | SEC-015..017 now proposed in verification plan with correct TH-016/019/012 mapping; other traceability docs still need review |
| REV-14 | `traceability-matrix-v1.md` F-12 previously required absence of gateway event although gateway is out of scope | CONFIRMED / DOCUMENTARY FIX | Boundary observer plus positive control specified in F-12; no test executed |

**Remaining findings:** REV-01, 03, 05, 06, 13, 15, 16, 17, 18, 19, 20 remain UNVERIFIED or OWNER_DECISION / EXPERIMENT as classified above. REV-08, 10 and 11 remain PARTIAL. REV-12 and REV-14 have documentary fixes only, not empirical verification.

## Further verified changes on this branch

| REV | Evidence and outcome | Status |
|---|---|---|
| REV-10 | Original `offline-experiment-contract-candidate-v0.md` §3 lists five errors; comparative v1 previously listed two. Comparative v1 now preserves all five; traceability v1 distinguishes `R-FALS` from `R-RISK` and separates provenance from epistemic result | PARTIAL FIX; other vocabulary collisions require owner review |
| REV-12 | Comparative v1 described R2 using a signature while the laboratory lacks key management and does not evaluate cryptographic authentication. Now verification is fixture-supplied for all representations; cryptography excluded from comparison | DOCUMENTARY FIX; no security proof |
| REV-14 | F-12 in traceability v1 required no event in an out-of-scope Action Gateway. Now specifies independent boundary observation and a positive control; without them outcome is NOT EVALUABLE | DOCUMENTARY FIX; F-12 still PROPOSED / NOT EXECUTED |

**Review warning:** This branch also changes gate prerequisites and test proposals; it must be independently reviewed against historical gate definitions and threat-to-requirement traceability before merge. No implicit G2.1 ratification.

## Review follow-up (2026-10-21)

- REV-11: `docs/02-diseno/security/traceability.md` now links TH-012/016/019 to SEC-REQ-017/015/016 and proposed SEC-017/015/016; none executed.
- REV-09: `comparative-contract-v1.md` now references the preexisting `A6/A7`, `HET-002` and `HET-003` second-domain cases, distinguishing conceptual expectations from unapproved machine-readable fixtures.
- REV-14: single current state is **DOCUMENTARY FIX / NOT EXECUTED**; the earlier OPEN label was stale and is corrected above.

**Still blocking review:** REV-01/03/05/06 gate and authority ratification, REV-08 original R criterion interpretation, REV-13 temporal backdating experiment, and remaining owner decisions. The documentary edits are not ratification.

## Historical audit errata / source-preserving interpretation (REV-08)

The historical `informe-auditoria-adversarial-2026.md` remains unchanged as an audit artifact. Its §4.2 explanations are **proposed interpretations**, not verbatim definitions of the Finch §5 criteria. The following precedence is documentary only; it does not approve a new oracle:

| Original Finch criterion | Exact historical meaning | Audit gloss to treat separately | Remaining proof obligation |
|---|---|---|---|
| R-01 | External identity merged solely on textual coincidence | Audit adds `UNVERIFIED` and `INSUFFICIENT` provenance judgments | F-11 must prove **no identity merge**, not merely unknown authenticity; add positive twin for authorized identity link |
| R-04 | Later knowledge backdated | Audit focuses on a mismatch between `valid_time` and `recorded_time` | Timestamp difference alone is not retroactive rewriting; require immutable registration order and explicit backdating attempt |
| R-05 | Historical evaluation/rule overwritten without trace | Audit focuses on rejecting direct mutation of a record | Include rule and assessment versions and a historical lookup after correction, not only input rejection |
| R-08 | Logical suppression presented as physical deletion | Audit focuses on whether E-10 is excluded or has a policy | Exclusion is correct governance, **not** falsation of a false physical-deletion claim; original E-10 stays BLOCKED |

Other Finch R-02/03/06/07 mappings remain hypotheses until source-specific acceptance oracles are approved. F-11 and F-12 are proposals only. The original Finch and historical audit documents are preserved.

## Temporal falsification proposal (REV-13; NOT AUTHORIZED / NOT EXECUTED)

A synthetic sequence with immutable registration ordinal `seq` distinct from caller-supplied `valid_time`, `recorded_time` and `assessed_time` is proposed: record assertion A at seq=1; submit correction B at seq=2 with earlier user-provided timestamps; query knowledge **as recorded at seq=1** and at seq=2. The expected invariant is that B never appears in the seq=1 view and A's historical assessment remains attributable to its original rule version. A negative control attempts to mutate A's seq=1 payload or evaluation and must be rejected or independently detected; a positive control adds a legitimate versioned correction. `seq` is a **hypothetical laboratory ordering witness**, not a demonstrated trusted clock, tamper-resistant ledger or storage design. Define an independent observer and machine-readable oracle before G2.2. No experiment or security guarantee is claimed.

## Governance residuals

- REV-01/03/05/06: `staged-authorization-protocol-v1.md` now identifies the unresolved historical gate precedence, G3 meaning, and lack of any current code/harness exception. Only the owner can ratify a resolution.
- REV-13: a negative and positive temporal oracle is proposed above, but no experimental result exists.
- REV-08: this errata preserves the historical audit rather than silently rewriting it; criteria and proposed oracle variants remain distinct.

## Public repository and licensing evidence (REV-15; verified 2026-10-21)

GitHub REST `GET /repos/hypenosys/the_machine` returned `visibility=public`, `private=false`, `license=null`. `docs/04-auditorias/gap-register.md` GAP-001 independently reports no root LICENSE file. Therefore statements suggesting publication is merely future-facing are outdated: the repository **is already publicly readable without a detected repository license**. This does not grant permission to reuse or redistribute, nor prove the legal status of each contributed document. Owner decision required: confirm visibility intent, provenance/third-party rights and licensing terms; do not autonomously alter settings or adopt a license. GAP-001 stays OPEN.

## Security-test identifier correction (REV-11; partial)

The historical adversarial audit assigned TH-012→SEC-015, TH-016→SEC-016 and TH-019→SEC-017, with TH-016's scenario testing corrupted-state load instead of actual backup restoration. The current proposed plan and traceability use TH-016→SEC-015/SEC-REQ-015 (backup restore), TH-019→SEC-016/SEC-REQ-016 (separation of duties), TH-012→SEC-017/SEC-REQ-017 (confused deputy). `uncertainty-register-v1.md` now records the **current candidate mapping** and notes the historical discrepancy. These identifiers remain proposed; no test was run and GAP-002 stays OPEN.

## Cross-document DEC-05/06/07 consistency pass (2026-10-21)

- `decision-package-v1.md` and `executive-summary-v1.md` no longer recommend adopting the blocked original F-10/E-10 in the initial experiment. Original E-10 stays BLOCKED; additional F-11/F-12 remain candidate-only.
- DEC-06 distinguishes synthetic laboratory interchange and versioned input/output from deferred durable database selection. No persistence technology or dependency is approved.
- DEC-07 and the executive summary now reflect the **already public** repository and absent detected repository license, rather than treating public availability as a future event.
- The executive summary no longer claims historical gate harmonization is complete. `security/security-gates.md` explicitly defines G3 as **before merging executable code**, while `staged-authorization-protocol-v1.md` frames G3 as **before writing Rust code**. Both remain unratified and unreconciled; do not silently pick either as binding.

**Residual:** REV-01/03/05/06/15/16/17/18/19/20 require remaining owner decisions or targeted verification. This pass is editorial/documentary only and does not change the HOLD status.

## Source-checked residual findings (REV-17 / REV-18 / REV-20)

- **REV-17 — PARTIAL DOCUMENTARY FIX:** `design-freeze-candidate-v0.md` restricts `evidence.v0`, integer `milli_degC`, illustrative 1000-unit tolerance and exact UTC instant to a candidate sensor profile; `comparative-contract-v1.md` now distinguishes this profile from optional generic times and epistemic verdicts. Adapter, normalization and oracle are **not ratified**.
- **REV-18 — OPEN / OWNER DECISION:** `docs/02-diseno/adr/0005-logging-recovery-and-data-lifecycle.md` (Proposed) says INV-017 “reiniciar no debe repetir efectos externos” and INV-018 “no declarar éxito sin recibo verificable”. Without a remote executor, durable idempotency keys, acknowledgement and recovery/reconciliation policy, neither an exactly-once effect nor a globally reliable receipt can be proven. Proposed future requirement: represent `PENDING | CONFIRMED | FAILED | UNKNOWN`, preserve idempotency identity, reconcile `UNKNOWN` before retry, and document external-system limitations. **No ADR edit, no runtime guarantee, no action gateway approval.**
- **REV-20 — CONFIRMED STALE TEXT:** `docs/03-preimplementacion/precode-review-checklist.md` says “Repositorio privado” under Publication, contradicted by GitHub API `visibility=public` (2026-10-21). Historical checklist remains intact; its publication row must not be used as current evidence. Editorial corrections to active v1 decision documents already describe the actual state. Other REV-20 issues (README determinism, audit index, dependency examples, OWASP pinning) still need source-by-source verification.

## Next owner decisions, not automatic changes

1. Decide whether the public repository is intentional and approve an explicit licensing/provenance path (DEC-07 / GAP-001).
2. Ratify documentary precedence and the exact G3 transition, and separately define any temporary experimental-code exception (GAP-010 / REV-01/03/05/06).
3. Decide whether remote-effect invariants are future requirements with `UNKNOWN` and reconciliation, or excluded from the offline experiment (REV-18).
4. Confirm the synthetic sensor profile version and its translation contract before experimental authorization (REV-17).

No owner approval, test execution, code change, merge, or GO is implied by this addendum.
