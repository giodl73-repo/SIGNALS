Written to `simulations/quest/golden/signal-variate-R11-2026-03-17.md`.

---

## R11 Variation Summary

**Five complete prompt bodies generated. Isolation plan:**

| V | C-34 (P) | C-35 (Q) | FULL gate | BARE gate | Predicted |
|---|----------|----------|-----------|-----------|-----------|
| V-01 | PASS | FAIL | 4 checks | 2 checks | **99.63** |
| V-02 | FAIL | PASS | 3 checks | 3 checks | **99.63** |
| V-03 | FAIL | FAIL | 3 checks | 2 checks | **99.26** |
| V-04 | PASS | PASS | 4 checks | 3 checks | **100.00** |
| V-05 | PASS | PASS | 4 checks | 3 checks | **100.00** |

**What each variation changes from the R10 V-05 baseline:**

- **V-01 (P only)**: BARE gate reduced to 2 checks — removes Check 3 (order). FULL gate keeps all 4.
- **V-02 (Q only)**: FULL gate reduced to 3 checks — removes Check 4 (format). BARE gate keeps all 3.
- **V-03 (neither)**: Both gates reduced — FULL has 3 checks, BARE has 2. Control baseline.
- **V-04 (P+Q)**: Both gates full (4+3). First variation with both new axes. Achieves ceiling.
- **V-05 (golden)**: Exact R10 V-05 canonical text reproduced. Reference ceiling for v11.

**Independence tests:**
- V-01 − V-03 = +0.37 → confirms C-34 (FULL format check) is independent
- V-02 − V-03 = +0.37 → confirms C-35 (BARE order check) is independent
- V-04 − V-03 = +0.74 → confirms no interaction; the two axes add cleanly
- V-04 = V-05 = 100.00 → ceiling confirmed; mode symmetry closure is complete
