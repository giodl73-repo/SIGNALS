Written to `simulations/quest/rubrics/quest-score-rubric-v12-variations-R12-2026-03-15.md`.

---

## quest-score R12 Variations — Summary

**Single-axis variations (3) + combination (1):**

| V-ID | Axis | Predicted verdicts | Expected composite |
|------|------|-------------------|-------------------|
| V-01 | Baseline — R12 full stack | All PASS | 100.00 |
| V-02 | C-31 PARTIAL ablation — independent cascade entries, no "per cascade" grouping | C-31 PARTIAL | ~99.80 |
| V-03 | C-32 PARTIAL ablation — design-time note present, specific template element ("column 4") absent | C-32 PARTIAL | ~99.80 |
| V-04 | C-30 FAIL ablation — no shared baseline evidence table instruction in Phase 2 | C-30 FAIL | ~99.60 |
| V-05 | Combination — V-02 + V-03 (independent entries AND element-unnamed design-time note) | C-31 PARTIAL + C-32 PARTIAL | ~99.60 |

**Key R12 structural changes in V-01 baseline:**
- N_aspirational: 22 → 25 (10/25 = 0.40 pt each; PARTIAL = 0.20 pt degradation)
- Criterion roster: 29 → 32 rows
- C-11 required declarations: 8 → 10 (added C-31, C-32)
- C-07 cascade block: now instructs the grouped form `"C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade"` + design-time note naming `"Variation in causal position, column 4"`
- C-25 inventory: 6 → 9 entries (added C-30 for C-02, C-31 for C-11, C-32 for C-28)
- Phase 2: shared-evidence consolidation instruction for multi-variation runs
- Worked example updated to C-31 axis (cascade grouping in quest-score.md PHASE 1 SETUP)

**Evidence ladders:**
- C-30: V-04 FAIL ← [gap] → V-01/V-02/V-03/V-05 PASS
- C-31: V-02 PARTIAL ← V-05 PARTIAL ← [gap] → V-01/V-03/V-04 PASS
- C-32: V-03 PARTIAL ← V-05 PARTIAL ← [gap] → V-01/V-02/V-04 PASS
