Written to `simulations/quest/rubrics/quest-variate-rubric-v16-2026-03-15.md`.

---

**v16 changes summary:**

**New criterion: C-40 -- Phase 1 axis breadth gate at planning-commit** (R16/V-02 confirmed)

The Phase 1 STOP CONDITION gains a 5th condition gating on at least 4 distinct axis values across all variation rows in the planning table -- before Phase 2 entry is permitted. V-02 cleanly ablated this ("R15/V-01 State Exactly"): Phase 1 reverts to 4 conditions (ending at C-39), while the set-level axis breadth checkpoint predicate (C-21) and all other R15 structures are retained.

**Design decision chain:** C-07 (axis coverage breadth, reviewer-enforced) + C-21 (axis breadth as checkpoint predicate, post-body enforcement) → C-40 (axis breadth as Phase 1 gate condition at planning-commit). Parallel enforcement chain to C-34/C-39 on the FROM/TO dimension. Together C-26 + C-39 + C-40 create a three-field Phase 1 gate: cross-variation citation, secondary-effect spatial grounding, and axis uniqueness must all be confirmed before any body is generated.

**Denominator: 32 → 33.**

**R16 tier structure under v16:**

| Rank | Variation | Score | Failures |
|------|-----------|-------|----------|
| 1 | V-01 full stack | 100.00 | -- |
| 2 | V-02 (C-40 ablation) | 99.70 | C-40 |
| 2 | V-03 (C-39 ablation) | 99.70 | C-39 |
| 2 | V-04 (C-38 ablation) | 99.70 | C-38 |
| 5 | V-05 (C-40+C-39 combo) | 99.39 | C-40, C-39 |

Three-way symmetry at Rank 2 again -- C-40, C-39, C-38 each fail independently at distinct structural boundaries. No R16→R17 candidate identified.
