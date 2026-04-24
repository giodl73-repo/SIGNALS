Here are the five complete variations for Round 9:

---

## Summary

| Variation | Axis | C-26 carrier | C-27 carrier | C-28 carrier |
|-----------|------|-------------|-------------|-------------|
| **V-01** | Lifecycle emphasis | "Read this entire table before executing Phase 1" on PIPELINE OVERVIEW table | F-01–F-05 + COV-01–COV-03 cited at Phase 6 exit AND Phase 7 exit | Two separate checkboxes: row count + column completeness |
| **V-02** | Output format (list-based schemas) | "Read this entire index before executing Step 1" on numbered PIPELINE INDEX | Same F-NN/COV-NN IDs cited at Step 6 AND Step 7 exits | Two separate items in Step 1 exit |
| **V-03** | Phrasing register (imperative command) | Bold "STOP. READ THIS PIPELINE BEFORE YOU START" header | "CHECK:" items citing F-NN/COV-NN at Phase 6 AND "STOP when done. Check again:" at Phase 7 | "STOP. Check these two items independently: (1)... (2)..." as separately enumerated |
| **V-04** | Lifecycle + Inertia framing | "Read the full overview before starting — cost of skipping visible at every row" | F-01–F-05 + COV-01–COV-03 at Phase 6 AND Phase 7 | Two labeled items: "row-count condition" and "column-completeness condition" |
| **V-05** | Output format + Role sequence + Inertia | "Read this entire table before executing Phase 1" on PIPELINE OVERVIEW | F-01–F-05 + COV-01–COV-03 at Phase 6 AND Phase 7 | Two separate checkboxes, plus Phase 1 header prompts technical-first role sequence |

### Key design decisions for R9

**V-02** tests whether list-based schemas (`F-01:` as a heading, not a table row) preserve the mechanical coupling that C-23/C-27 require. If it scores lower on C-27, the finding is that table-row IDs are harder to skip past than list-item labels.

**V-03** tests whether imperative phrasing makes C-28 harder to violate — "STOP. Check these two items **independently**" is a stronger sequencing signal than a passive checklist item.

**V-04** adds a "Without this step" consequence statement at every phase header. This tests C-14 (pervasive consequence framing) — the status-quo competitor is named at each phase, not only in the schemas.

**V-05** combines three axes simultaneously. The priority-leading column order (`Priority | Namespace | Skill...`) makes C-04/C-05 violations visible at the leftmost column, and the "What This Supersedes" section in Phase 3 creates a named contrast point for the commit gate in Phase 8.

Written to `simulations/quest/rubrics/topic-new-rubric-v8-variations-R9-2026-03-14.md`.
