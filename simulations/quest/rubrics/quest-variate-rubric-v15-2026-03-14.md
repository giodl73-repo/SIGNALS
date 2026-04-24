Written to `simulations/quest/rubrics/quest-variate-rubric-v15-2026-03-15.md`.

---

**v15 changes summary:**

**New criterion: C-39 -- Phase 1 FROM/TO endpoint gate at planning-commit** (R15/V-02 confirmed)

The Phase 1 STOP CONDITION gains a 4th condition gating on actual FROM/TO endpoint content in at least one secondary-effect planning-table cell — before Phase 2 entry is permitted. Distinct from C-34 (FROM/TO content as review-time quality criterion): C-39 shifts enforcement to planning-commit time. Distinct from C-26 (V-ID citation gate at Phase 1): both are Phase 1 gates but on different fields. Together they create a dual-field Phase 1 gate.

**Design decision chain:** C-34 (FROM/TO content quality) → C-39 (FROM/TO content as Phase 1 gate condition at planning-commit).

**Denominator: 31 → 32.**

**R15 tier structure under v15:**

| Rank | Variation | Score | Failures |
|------|-----------|-------|----------|
| 1 | V-01 full stack | 100.00 | — |
| 2 | V-02 (C-39 ablation) | 99.69 | C-39 |
| 2 | V-03 (C-38 ablation) | 99.69 | C-38 |
| 2 | V-04 (C-37 ablation) | 99.69 | C-37 |
| 5 | V-05 (C-39+C-38 combo) | 99.38 | C-39, C-38 |

Three-way symmetry at Rank 2 again — C-39 (Phase 1 gate), C-38 (checkpoint routing), C-37 (Phase 2 STOP destination) each fail independently at distinct structural boundaries. No R15→R16 candidate identified.
