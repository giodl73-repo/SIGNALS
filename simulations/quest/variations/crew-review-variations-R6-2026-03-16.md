Written to `simulations/quest/golden/crew-review-variate-R6-2026-03-16.md`.

---

## crew-review Variate R6 -- Summary

**R6 design target**: R5 achieved C-20+C-21 coexistence and the maximal stack. R6 explores structural alternatives that could make the full aspirational chain more reliably satisfied -- not by adding criteria, but by changing *how the mechanisms are expressed*.

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | Phrasing register -- declarative contract form | Replace imperative steps with typed output invariants. C-20/C-21 become properties the output must have, checked at output time rather than recalled during execution. |
| **V-02** | Lifecycle emphasis -- AMEND as pre-delivery phase | Five phases: LOAD, CHALLENGE, REVIEW, **VALIDATE** (new), AMEND. VALIDATE checks every row before the matrix is written. AMEND options are *derived from* this run's findings, not generic. |
| **V-03** | Role sequence -- numbered execution manifest | Before any role runs, declare a numbered manifest (slot 1 = challengers, slots 2-N = domain roles ranked by relevance). Execution order is a first-class artifact; cross-role synthesis references slot numbers. |
| **V-04** | Phrasing register + Inertia framing | Peer-voice challenger ("let's hear the strongest case for doing nothing") with state machine gate intact (OPEN/CLOSED, 5-condition closure, C-21 anti-pattern inside the rule). Tests register vs structure orthogonality. |
| **V-05** | Lifecycle + Output format + Role sequence (verification-first maximal) | Full stack (C-11--C-21) + **PHASE 4 VERIFY**: explicit criterion-check table before render. If any designed criterion scores NO, the relevant phase re-executes. Makes meta-verification visible in the output. |

**Key structural innovations vs R5:**
- V-01 inverts the architecture: contract-first, not step-first
- V-02 adds a VALIDATE phase that didn't exist in any prior round
- V-03 introduces the manifest as a pre-declared, lockable artifact
- V-04 tests that peer-voice register doesn't weaken C-20/C-21 structurally
- V-05 adds the criterion-check table as a visible verification checkpoint -- the first variation across all rounds where the model explicitly self-checks aspirational criteria before final output
