Written to `simulations/quest/golden/campaign-simulate-variate-R8-2026-03-16.md`.

---

## Round 8 Variations — Summary

**Base**: R7 V-05 (96.5/100 under v7; ~96.6/100 under v8 with partial C-26/C-27 coverage)

**Closing gap**: 4 criteria remain unmet — C-26 (systematic), C-27 (all blocks), C-09, C-15

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | C-26 single-axis | Every enforcement rule names its failure mode as a structural violation — in axis rows, finding schema annotations (`STRUCTURAL VIOLATION:` replaces `FAILURE:`), and OBSERVATIONAL DISCIPLINE enforcement statements |
| **V-02** | C-27 single-axis | Every aggregation block (CANDIDATE OBS, T-1 ANNEX, EXECUTION LOG, RANKED FINDINGS, Step 3) carries a self-characterization statement; compliance checklist adds a verification row |
| **V-03** | C-09 + C-15 single-axis | Severity (`critical/high/medium/low`) and Lifecycle (`new/confirmed/amended/closed`) added as required standalone fields; scales declared in OBSERVATIONAL DISCIPLINE before execution; FINDINGS TABLE adds two columns |
| **V-04** | C-26 + C-27 combined | V-01 + V-02 on R7 V-05 base; no C-09/C-15 |
| **V-05** | Full integration | V-04 + C-09 + C-15; all four persistent gaps closed simultaneously |

**Score ceiling under v8 if hypotheses hold**: V-05 → 118/118 = 100/100.

**Key structural signal in V-05 vs V-04**: V-05 adds the self-characterization rule to OBSERVATIONAL DISCIPLINE as a named structural commitment (with all five blocks listed), and the compliance checklist gains two new rows (Severity/Lifecycle + Aggregation self-characterization). The T-1 ANNEX in V-05 names the structural violation inline: `STRUCTURAL VIOLATION: a withheld-T1 observation named in this ANNEX that is absent from any per-scope Disposition column is a structural violation.` — making C-26 and C-27 mutually reinforcing in the same block.
