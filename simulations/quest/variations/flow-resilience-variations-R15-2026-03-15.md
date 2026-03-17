V-02 correctly carries C-43 PASS from its R13 V-02 baseline (two independent Gate 1 CLOSE checkboxes) while adding C-42 PASS (two independent Gate 2b CLOSE checkboxes). Both V-01 and V-02 land at C-42+C-43 PASS, C-44 FAIL — tied under v14, separated by construction path only.

Written to `simulations/quest/golden/flow-resilience-variate-R15-2026-03-15.md` (2697 lines).

---

**R15 variation summary:**

| Variation | Axis | C-42 | C-43 | C-44 | C-45 (cand.) | Expected |
|-----------|------|------|------|------|--------------|---------|
| V-01 | Gate 1 CLOSE split (C-43) added to R13 V-01 baseline | PASS | **PASS** | FAIL | FAIL | 70/72 |
| V-02 | Gate 2b CLOSE split (C-42) added to R13 V-02 baseline | **PASS** | PASS | FAIL | FAIL | 70/72 |
| V-03 | C-42+C-43 both added to R13 V-03 baseline (C-44 preserved) | **PASS** | **PASS** | PASS | FAIL | 72/72 |
| V-04 | C-44 formal registry added to R13 V-04 baseline (C-42+C-43 preserved) | PASS | PASS | **PASS** | FAIL | 72/72 |
| V-05 | Full integration + Recovery Stage VS Cross-Reference Registry (C-45 candidate) | PASS | PASS | PASS | **PASS** | 72/72 + |

**Structural distinctions:**
- V-01/V-02: tied under v14 (both C-42+C-43 PASS, no C-44). Open for R16: C-44 for both.
- V-03/V-04: both reach 72/72 from opposite construction paths. Ties under v14; separated by v15 if C-45 (VS Registry) is extracted from V-05.
- V-05: introduces Recovery Stage VS Cross-Reference Registry as Act 1 Terminal — each recovery stage VS registered with VS ID / Stage Context / Observation Assertion. Orthogonal to C-35 (presence check at row level); registry makes VS independently assertion-ready at terminal level. Candidate C-45.
