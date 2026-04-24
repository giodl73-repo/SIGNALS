Written to `simulations/quest/rubrics/quest-variate-rubric-v15-variations-R16-2026-03-15.md`.

---

## R16 Variations -- Design Summary

**C-40 candidate: Axis breadth gate at Phase 1 STOP CONDITION**

The structural gap in R15/V-01: axis breadth (≥4 distinct axes) is enforced only as a set-level checkpoint predicate in Phase 2 -- after bodies are being written. A planning table with 5 rows all using the same axis label passes all 4 Phase 1 STOP conditions and the violation only surfaces at a Phase 2 checkpoint, triggering a costly amendment cycle.

C-40 adds a **5th Phase 1 STOP condition**: "The planning table contains at least 4 distinct axis values across all 5 rows." This shifts enforcement from checkpoint-time detection to planning-commit time -- parallel to C-26 (V-ID citation gate) and C-39 (FROM/TO endpoint gate), creating a **triple Phase 1 gate** across three planning-table columns.

---

| V-ID | Axis | Key structural change | Expected score under v15 |
|------|------|----------------------|--------------------------|
| V-01 | R16 full stack + C-40 | Phase 1 STOP gains 5th condition: axis breadth gate | 100.00 |
| V-02 | C-40 ablation | Phase 1 STOP has 4 conditions only (C-39 retained); axis breadth checkpoint-only | 100.00 |
| V-03 | C-39 ablation + C-40 retained | Phase 1 STOP has 4 conditions: C-40 as condition 4, FROM/TO gate removed | 99.69 (C-39) |
| V-04 | C-38 ablation + C-40 retained | Phase 1 STOP 5 conditions intact; checkpoint failure routing unified (no type stratification) | 99.69 (C-38) |
| V-05 | C-40 + C-39 combination | Phase 1 STOP has 3 conditions only; both Phase 1 gates removed; C-38 retained | 99.69 (C-39) |

V-01 and V-02 score identically under v15 (C-40 not yet a criterion). Under future v16, V-02 would fail C-40 (99.70) while V-01 remains 100.00 -- that asymmetry is the confirmation test. V-05 tests superadditivity of two Phase 1 STOP gates operating on different columns at the same structural boundary.
