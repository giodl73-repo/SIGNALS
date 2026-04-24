Written to `simulations/quest/golden/file-issue-variate-R6-2026-03-17.md`.

---

## Round 6 Summary

**Context**: R5 V-04 achieved 12/12 (100.00) under v6. R5 V-05 failed only C-19 (headings said "severity-dispatched" without naming origin "A1"). Round 6 isolates C-18 and C-19 to understand their structural dependencies.

**5 variations:**

| Variation | Axis | Key structural difference | Predicted |
|-----------|------|--------------------------|-----------|
| **V-01** | Single -- C-19 (steps-based) | Steps not phases; headings say "(dispatched by severity in Step 1)" | 9/12 = 97.50 |
| **V-02** | Single -- C-18 (completion condition) | Macro-phase; A1 says "determines both" (not "simultaneously dispatches"); completion condition uses "dispatched by" | 9-10/12 = 97.50-98.33 |
| **V-03** | Combined C-18 + C-19 | Macro-phase; "determines both" in A1; provenance headings naming "in A1"; C-18 completion condition | 11-12/12 = 99.17-100.00 |
| **V-04** | Full synthesis + inertia framing | Identical to R5 V-04 structurally, adds opening paragraph naming cost of not filing | 12/12 = 100.00 |
| **V-05** | Minimal C-19 fix of R5 V-05 | Patch headings from "severity-dispatched X" to "X (dispatched by severity in A1)" only | 12/12 = 100.00 |

**Critical open questions for scoring:**
1. Does "in Step 1" (vs "in A1") satisfy C-19? (V-01)
2. Is C-18 achievable while C-17 fails -- i.e., can the completion condition verify dispatch without "simultaneously dispatches" in A1? (V-02)
3. Does "determines both" + C-18 + C-19 together satisfy C-17? (V-03 -- the most consequential test)
