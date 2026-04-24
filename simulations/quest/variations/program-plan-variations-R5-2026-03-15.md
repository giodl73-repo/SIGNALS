Written to `simulations/quest/golden/program-plan-variate-R5-2026-03-16.md`.

---

## R5 Variate Summary

**Rubric v5 adds C-19, C-20, C-21.** The R4 retrospective showed three critical gaps:

| R4 Variation | C-19 | C-20 | C-21 |
|---|---|---|---|
| V-01 (criterion tags) | PASS (incidental — BAD block had `# WRONG C-05/C-06`) | FAIL | FAIL |
| V-02 (per-zone contrast) | FAIL | PARTIAL (headers, not skill-line) | FAIL |
| V-03 (correction table) | PASS (incidental — C-06 pairs) | FAIL | PARTIAL (missing skills bridges) |
| V-04/V-05 (golden) | PASS | PARTIAL | PARTIAL |

**Five variations, three single-axis then two combined:**

| | Axis | Key technique | C-19 | C-20 | C-21 |
|---|---|---|---|---|---|
| **V-01** | Inertia framing | BAD YAML tags cover C-05+C-06+C-07 alongside C-02/03/04 | PASS | FAIL | FAIL |
| **V-02** | Lifecycle emphasis | `PREREQUISITE:` reminders moved to `skills:` placeholder line, not just zone header | FAIL | PASS | FAIL |
| **V-03** | Output format | `# check correction table` bridges at all three field types (name, skills, gate) | PASS (incidental) | FAIL | PASS |
| **V-04** | Inertia + lifecycle | Cross-tier BAD block + skill-position prerequisites | PASS | PASS | FAIL |
| **V-05** | Golden synthesis | All three on best R4 foundation | PASS | PASS | PASS |

**Key design decisions:**
- **C-19** is achievable by adding recommended-criterion tags (`# WRONG C-05`, `# WRONG C-06`, `# WRONG C-07`) to the BAD PLAN block and C-06/C-07 rows to the correction table
- **C-20** requires moving the dependency note from the zone comment to the `skills:` line itself — `# requires: draft:spec from Design zone` at the `skills:` placeholder, not at the zone header
- **C-21** requires `# check correction table: skill names` / `# check correction table: gates` / `# check correction table: stage names` at every covered field type — the bidirectional coupling that R4 V-03 only partially achieved
