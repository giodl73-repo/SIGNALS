Written to `simulations/quest/golden/signal-variate-R9-2026-03-17.md`.

---

**R9 Summary**

Three new axes discovered from structural analysis of R8 V-05:

| Axis | Mechanism | Gap closed |
|------|-----------|------------|
| M | FULL MODE Check 4 (format) | FULL was the only mode without a format check in its compliance gate |
| N | BARE MODE Check 3 (order) | BARE had end-anchors (C-21) but no interior-order gate check |
| O | PARSE MODE disambiguation examples | "FULL otherwise" branch had no worked example for sub-skill-name arguments |

**Structural theme for R9**: *complete the gate symmetry* -- each primary compliance gate gains the check dimension that peer gates already have. M brings FULL in line with FILTER (format check). N brings BARE in line with FULL (order check). O closes the parse-mode inference gap the same way C-16 and C-30 closed prior inference gaps: rule + worked example beats rule alone.

**Predicted spread-design:**

| V | C-31 | C-32 | C-33 | Predicted |
|---|------|------|------|-----------|
| V-01 | PASS | FAIL | FAIL | 100.00 under v9; C-31 extracted |
| V-02 | FAIL | PASS | FAIL | 100.00 under v9; C-32 extracted |
| V-03 | FAIL | FAIL | PASS | 100.00 under v9; C-33 extracted |
| V-04 | PASS | PASS | FAIL | 100.00 under v9; C-31+C-32 extracted |
| **V-05** | PASS | PASS | PASS | **100.00 under v10** |
