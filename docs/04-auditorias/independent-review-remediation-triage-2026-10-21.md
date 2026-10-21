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
| REV-14 | `traceability-matrix-v1.md` F-12 requires absence of gateway event but gateway is out of scope | CONFIRMED / OPEN | Add independent boundary observer and positive control; not yet applied |

**Remaining findings:** REV-01, 03, 05, 06, 10, 12, 13, 15, 16, 17, 18, 19, 20 remain UNVERIFIED or OWNER_DECISION / EXPERIMENT as classified above. No claim of exhaustive remediation.

## Further verified changes on this branch

| REV | Evidence and outcome | Status |
|---|---|---|
| REV-10 | Original `offline-experiment-contract-candidate-v0.md` §3 lists five errors; comparative v1 previously listed two. Comparative v1 now preserves all five; traceability v1 distinguishes `R-FALS` from `R-RISK` and separates provenance from epistemic result | PARTIAL FIX; other vocabulary collisions require owner review |
| REV-12 | Comparative v1 described R2 using a signature while the laboratory lacks key management and does not evaluate cryptographic authentication. Now verification is fixture-supplied for all representations; cryptography excluded from comparison | DOCUMENTARY FIX; no security proof |
| REV-14 | F-12 in traceability v1 required no event in an out-of-scope Action Gateway. Now specifies independent boundary observation and a positive control; without them outcome is NOT EVALUABLE | DOCUMENTARY FIX; F-12 still PROPOSED / NOT EXECUTED |

**Review warning:** This branch also changes gate prerequisites and test proposals; it must be independently reviewed against historical gate definitions and threat-to-requirement traceability before merge. No implicit G2.1 ratification.
