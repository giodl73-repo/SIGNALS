Written to `simulations/quest/golden/mock-all-variate-R19-2026-03-16.md`.

---

**R19 summary:**

**C-38 axis** (new criterion): stage-local compliance architecture. A multi-stage template fails C-38 when the inertia instruction lives in the ROLE 2 preamble as a cross-stage statement rather than independently within each stage body.

**Five variations:**

| | C-38 | R-03 | Composite |
|---|---|---|---|
| V-01 | FAIL | FAIL | 88.0 |
| V-02 | FAIL | PASS | 99.0 |
| V-03 | PASS | PASS | 99.33 |
| V-04 | PASS + C-36 | PASS | 99.67 |
| V-05 | PASS + C-36 + C-37 | PASS | 100.0 |

**Key finding exposed by the v19 formula:** R-03 (Recommended, 10 pts) dominates C-38 (Aspirational, 0.33 pts) by 30:1. The V-01→V-02 step is the highest-discrimination move in the ladder, driven entirely by gate completeness, not by the new architectural criterion. V-02 through V-05 compress into a 1.0-point band.

**Single-axis chain:** V-02→V-03 (C-38), V-03→V-04 (C-36), V-04→V-05 (C-37). V-05 is R18 V-05 retroactively C-38 PASS — no new ceiling variation is needed.
