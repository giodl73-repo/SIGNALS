Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v17-2026-03-15.md`.

---

## What changed v16 -> v17

Three new criteria extracted from R16 excellence signals. Formula `/42` -> `/45`. Golden threshold 9.0 now requires **41/45** aspirational.

---

### C-51 — CHAIN STATUS Per-Direction Violation Check (`depth`, C-51->C-50)

C-50 built a static DIRECTION INVENTORY (PRESENT/ABSENT + section cite). C-51 activates it: each PRESENT direction carries an explicit **violation check** — a named string-comparison condition stating what inconsistency would reopen the gate. CHAIN STATUS stays CLOSED only when all direction-level checks evaluate to no-conflict. Sourced from V-05's explicit C-48 consistency violation check in CHAIN STATUS (V-01–V-04 have the inventory but no falsifiability conditions).

---

### C-52 — Phase Gate Contract Summary Return-and-Annotate Instruction (`format`, C-52->C-48)

C-48 required the `Phase Refs:` annotation at the destination (INCUMBENT BASELINE rows). C-52 requires the **trigger-site instruction** at the source: PHASE GATE CONTRACT SUMMARY must carry a named cross-section authoring instruction directing the author to return and back-annotate INCUMBENT BASELINE upon completing all PHASE ENTRY CONTRACT blocks. V-04 passed C-48 (destination annotation exists) but has no such instruction in PHASE GATE CONTRACT SUMMARY — C-52 is a fail regardless of annotation correctness.

---

### C-53 — EX Block Hint Architecture Back-Reference (`format`, C-53->C-49)

C-49 placed the EXCEPTION BLOCK ARCHITECTURE declaration in the preamble. C-53 closes the loop: the `IM Ref:` hint in each EX block template must carry an **explicit inline back-reference** to that declaration by name (e.g., "see EXCEPTION BLOCK ARCHITECTURE above"). V-02 passed C-49 (preamble declaration present) but the per-block hints carry no such anchor — C-53 is a fail. Only V-05, which added "(see architecture above)" to the `IM Ref:` hint, passes.

---

### R16 Retrospective under v17

| Variation | C-48 | C-49 | C-50 | C-51 | C-52 | C-53 | Aspirational | Score |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:------------:|-------|
| V-01 | FAIL | FAIL | [?] | FAIL | FAIL | FAIL | 39/45† | 8.667† |
| V-02 | FAIL | PASS | [?] | FAIL | FAIL | FAIL | 40/45† | 8.889† |
| V-03 | FAIL | FAIL | [?] | FAIL | FAIL | FAIL | 39/45† | 8.667† |
| V-04 | PASS | FAIL | [?] | FAIL | FAIL | FAIL | 40/45† | 8.889† |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | 45/45 | **10.000** |

† C-50 data was cut off in the provided scorecard; shown as FAIL (conservative). Add 1/0.222 per variation if C-50 passed.
