Written to `simulations/quest/golden/quest-score-variate-R1-2026-03-16.md`.

---

## Summary

**Rubric context**: v1-2026-03-16. N_essential=5, N_recommended=3, N_aspirational=2. Formula denominator changed from v1-2026-03-15 (was E/5·60 + R/2·30 + A/1·10; now E/5·60 + R/3·30 + A/2·10).

**Axis selection rationale**: The new rubric's two hardest-to-satisfy requirements are C-01's four-sub-element load block and C-04's explicit E/R/A calculation form — both likely to produce PARTIALs in R1. Axis C targets these directly with inline worked examples. Axis B (phase gates) targets the synthesis-omission failure pattern that cost C-05/C-07/C-08/C-09 in the prior cycle. Axis A (numbered blocks) targets both through slot-level templating.

| Variation | Axis | Primary target |
|-----------|------|----------------|
| V-01 | A — numbered criterion blocks | C-01 PARTIAL (missing sub-elements), C-04 PARTIAL (bare number) |
| V-02 | B — hard phase gates with STOP tokens | C-05/C-07/C-08/C-09 omission under context pressure |
| V-03 | C — worked examples inline | C-01 and C-04 compliance via positive anchor |
| V-04 | A+B — blocks + gates | Quality floor + presence gate; tests additivity |
| V-05 | A+B+C — all three | Full stack; tests whether C's anchor is redundant when A+B already enforce slot precision |

**Key regression guard**: All five variations include the C-09 N/A handling (PARTIAL, not FAIL in round 1) because the new rubric moved regression signals to Aspirational and the N/A rule changed denominator position accordingly.
