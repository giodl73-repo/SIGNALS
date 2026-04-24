Written to `simulations/quest/golden/quest-score-variate-R7-2026-03-16.md`.

---

## R7 Summary

**Rubric**: v7 (22 criteria, N_aspirational=14)
**New criteria targeted**: C-21 (Phase 1 exit criterion-coverage assertion) and C-22 (Axis non-additivity identification)

### Axes

| Code | Axis | Mechanism | C-22 path |
|------|------|-----------|-----------|
| R | NON-ADDITIVITY ANALYSIS BLOCK | Schema-bound section in SYNTHESIS: three required fields (redundant axis / criterion / subsuming mechanism) | Structural — PASS predicted |
| S | COMPOSITE INCREMENT TABLE | Leaderboard delta column; zero-delta rows require "explain why" note | Numeric — PARTIAL predicted |
| T | AXIS ARCHITECTURE AUDIT | Phase 3 per-axis table with ZERO row annotations | Systematic — PARTIAL predicted |

### Variations

| Var | Axes | Key prediction |
|-----|------|---------------|
| V-01 | R | C-22 PASS (schema forces three elements); C-21 FAIL (no COVERAGE ASSERTION) |
| V-02 | S | C-22 PARTIAL (delta present, mechanism-subsuming absent); C-21 FAIL |
| V-03 | T | C-22 PARTIAL (per-axis verdict present, mechanism-subsuming absent); C-21 FAIL |
| V-04 | P+Q+R | All four post-v5 criteria PASS simultaneously; composite 99.64 |
| V-05 | P+Q+R+S | Predicted tie with V-04 at 99.64 — S non-additive given R |

### The R7 non-additivity hypothesis

If V-04 == V-05, the finding mirrors R6's: **S is subsumed by R**. R's three-field schema forces the structural reasoning (axis / criterion / subsuming mechanism) that C-22 requires; S's delta table surfaces the same information numerically but cannot advance C-22 above PASS. The minimal sufficient combination for v7 is P+Q+R.
