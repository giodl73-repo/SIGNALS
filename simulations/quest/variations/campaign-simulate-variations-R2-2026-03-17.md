Written to `simulations/quest/golden/campaign-simulate-variate-R2-2026-03-17.md`.

---

## Round 2 Summary

Five variations targeting the three new v2 aspirational criteria:

| Variation | Axis | Primary Target | Key Mechanism |
|-----------|------|---------------|---------------|
| **V-01** | Role sequence (trace-first) | C-13 | Trace runs before flow; flow sub-skills receive a Trace Findings Brief; mandatory Trace Link column |
| **V-02** | Severity budgets | C-11 | Each trace sub-skill requires >= 1 CRITICAL/HIGH before advancing; budget gate halts the campaign if unmet |
| **V-03** | No-blank-cell table contract | C-12 | Table schema defined upfront; sentinel rule ("N/A -- reason" not blank); blank cell = failed finding |
| **V-04** | Trace-first + severity budgets | C-11 + C-13 | Budget gate before flow; Trace Findings Brief feeds flow; Trace Link column required on flow findings |
| **V-05** | All three axes combined | C-11 + C-12 + C-13 | Maximum structure: budgets + trace brief + 10-column no-blank table closes all three criteria by construction |

**Key structural bets for Round 2:**

- **C-11 closes by budget**: V-02/V-04/V-05 make a missing CRITICAL/HIGH on any trace sub-skill a named halting failure, not a silent omission.
- **C-13 closes by ordering + column**: V-01/V-04/V-05 force a Trace Link column per flow finding -- "none" is acceptable, blank is not. At least one non-"none" is required.
- **C-12 closes by sentinel rule**: V-03/V-05 replace blank-cell tolerance with an explicit failure definition; "no findings" rows still get fully populated with "None required -- reason".
- **C-09 closes by construction in V-04/V-05**: when all three trace budgets are met, >= 3 CRITICAL/HIGH findings exist as test scenario seeds before the baseline section is reached.
