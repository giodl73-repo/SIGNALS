Written to `simulations/quest/rubrics/listen-support-rubric-v16-2026-03-15.md`.

**What changed v15 -> v16:**

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-47 | Phase-2 No-Exception Triple-Clause | C-44 | V-01, V-04, V-05 |
| C-48 | Post-Generation Phase Distribution Re-Verify | C-45 | V-02, V-04, V-05 |
| C-49 | Switching-Friction Count Floor >= 3 with Phase-2 Barrier Constraint | C-46 | V-03, V-05 |

Aspirational tier: 190 -> 205 pts. Total ceiling: **280 -> 295**.

**R16 scores under v16:**

| Variation | Score | Fails |
|-----------|-------|-------|
| V-05 | 295/295 | -- |
| V-04 | 290/295 | C-49 FAIL |
| V-01 | 285/295 | C-48 FAIL, C-49 FAIL |
| V-02 | 285/295 | C-47 FAIL, C-49 FAIL |
| V-03 | 285/295 | C-47 FAIL, C-48 FAIL |
