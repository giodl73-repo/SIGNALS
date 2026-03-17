Written to `simulations/quest/golden/flow-throttle-variate-R13-2026-03-16.md`.

---

## R13 Summary

| Variation | Axes | C-35 | C-36 | Predicted |
|-----------|------|------|------|-----------|
| V-01 | Role sequence — V-04 single-role baseline carry | FAIL | FAIL | 220/230 |
| V-02 | Lifecycle emphasis — FORMAT CONTRACT COMPLETE at phase boundary, merged consequence | PASS | FAIL | 225/230 |
| V-03 | Role sequence — Domain Expert + Consequence Analyst with count-declared activation conditions, no format-phase role | FAIL | PASS | 225/230 |
| V-04 | Combined — three-role pipeline, FORMAT CONTRACT COMPLETE + count-declared activation conditions | PASS | PASS | 230/230 |
| V-05 | Combined + phrasing register — V-04 structure in imperative/terse register | PASS | PASS | 230/230 |

**Single-axis questions:**
- **Q1** (V-01 vs V-02): Does FORMAT CONTRACT COMPLETE at a named phase boundary satisfy C-35 independent of C-36?
- **Q2** (V-01 vs V-03): Do count declarations at a consequence-role activation boundary satisfy C-36 independent of C-35?
- **Q3** (V-04 vs V-05): Is C-35/C-36 compliance register-independent (confirming structural vs. instructional distinction is orthogonal to phrasing)?

**Key architectural distinction C-35/C-36 add over C-33/C-34:** C-33 and C-34 require the *content* of counts to appear at specific positions (annotation header, path label). C-35 and C-36 require the *mechanism* of enforcement to be architectural — a handoff violation vs. a rubric-scan failure (C-35), a role-activation failure vs. an audit-format gap (C-36). V-04 and V-05 both achieve 230/230; V-01 confirms the baseline drop is real and not an artifact of other criteria changing.
