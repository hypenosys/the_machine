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
