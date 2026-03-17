Written to `simulations/quest/golden/program-plan-variate-R7-2026-03-16.md`.

---

## R7 Variate Summary

**Rubric**: v7 (27 criteria, 190 pts max). Three new axes: C-25 (Why: rationale), C-26 (criterion-tagged structural fields), C-27 (uniform dep syntax).

| Variation | Axis | Key mechanism | C-25 | C-26 | C-27 | Expected |
|-----------|------|---------------|------|------|------|----------|
| V-01 | Role sequence | Per-zone `Why:` rationale in comment-based FAIL/PASS pairs | PASS | FAIL | FAIL | ~145 |
| V-02 | Output format | `# WRONG C-04` inline on every `gate_fail:` structural field | FAIL | PASS | FAIL | ~150 |
| V-03 | Phrasing register | `# requires: X from Zone: Y (C-05)` uniformly at ALL positions | FAIL | FAIL | PASS | ~150 |
| V-04 | Lifecycle emphasis | Structural gate fields + `Why:` + `# WRONG C-04` at every field | PASS | PASS | FAIL | ~165 |
| V-05 | Golden | All three axes on R6 V-05 foundation | PASS | PASS | PASS | ~190 |

**Key design decisions:**
- **V-01** uses comment-based zones (R6 V-02 base) — isolates Why: without structural entanglement
- **V-02** has `gate_fail: "..." # WRONG C-04` inline — the criterion tag coincides with the wrong shape atomically
- **V-03** enforces `# requires: X from Zone: Y (C-05)` as a pure, separate comment — no preamble mixing breaks the uniform scan pattern
- **V-05** splits the dep reminder and correction-table reference onto separate lines at the `skills:` position, resolving the R6 V-05 uniformity failure where `# check correction table: skill names; requires: ...` mixed two concerns in one prefix
