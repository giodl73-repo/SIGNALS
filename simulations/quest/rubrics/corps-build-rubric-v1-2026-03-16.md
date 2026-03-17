---
skill: quest-rubric
skill_target: corps-build
date: 2026-03-16
version: 1
---

# Scoring Rubric: corps-build

Read a confirmed org.yaml and generate the full org. Outputs: org-chart.md with ASCII
box diagram, headcount by group/area, level distribution; .craft/roles/{area}/{role}.md
typed files for every role. Supports arbitrary nesting. Inertia-advocate always in every team.

---

## Essential Criteria (60 points total — all must pass)

### C-01 — Role file completeness
**Weight**: essential
**Category**: correctness
**Text**: Every role declared in org.yaml has a corresponding .craft/roles/{area}/{role}.md
file. No role in org.yaml is absent from the filesystem output.
**Pass condition**: Count of role files generated equals count of roles declared in org.yaml.
Zero missing role files. Zero phantom files (files with no matching org.yaml entry).

---

### C-02 — Org-chart.md produced with ASCII diagram
**Weight**: essential
**Category**: format
**Text**: org-chart.md is written and contains a readable ASCII box diagram that shows the
declared hierarchy at a minimum of two levels. Group names match org.yaml exactly.
**Pass condition**: File exists at the declared output path. Contains at least one ASCII
hierarchy block (box-drawing or dash/pipe characters forming a tree). Minimum two hierarchy
levels visible. Group names in the diagram match org.yaml group names character-for-character.

---

### C-03 — Inertia Advocate present in every team
**Weight**: essential
**Category**: correctness
**Text**: The Inertia Advocate role exists in every team node declared in org.yaml. No team
is exempt. The role file must be present, not merely referenced in org-chart.md.
**Pass condition**: For every team in org.yaml, a file named inertia-advocate.md (or
equivalent canonical name) exists under .craft/roles/{area}/. Count of teams in org.yaml
equals count of Inertia Advocate role files.

---

### C-04 — org.yaml structural fidelity
**Weight**: essential
**Category**: correctness
**Text**: The generated role file directory tree reflects every declared group nesting level
(Division > Team > Sub-group) and every role assignment from org.yaml. No structural
reshuffling or flattening that was not in the input.
**Pass condition**: Directory structure under .craft/roles/ maps 1-to-1 to the area/group
nesting in org.yaml. No area appears in .craft/roles/ that does not exist in org.yaml. No
area declared in org.yaml is absent from .craft/roles/.

---

### C-05 — Role file typed fields present
**Weight**: essential
**Category**: coverage
**Text**: Every .craft/roles/{area}/{role}.md file contains all five required typed fields:
orientation, lens, expertise, scope, and collaboration pattern. Placeholder text ("TBD",
empty section, omitted heading) is a fail.
**Pass condition**: Each role file contains all five headings with non-empty body text. A
file missing any single field fails this criterion for the full output.

---

## Recommended Criteria (30 points total — output is better with these)

### C-06 — Headcount by group/area table in org-chart.md
**Weight**: recommended
**Category**: depth
**Text**: org-chart.md includes a headcount table with one row per area/group showing
individual headcount plus a Total row. Level distribution (IC vs management, or explicit
level labels from org.yaml) is shown either in the same table or in a companion section.
**Pass condition**: Table present with at least two area rows and a Total row. Level
distribution visible as either a column, a sub-table, or a labeled distribution block.
Counts sum correctly to Total.

---

### C-07 — Standard vs specialized role distinction honored
**Weight**: recommended
**Category**: correctness
**Text**: Role files correctly reflect whether a role is standard (shared across all teams),
specialized (team-specific), shared group-level, or exec office. The distinction is visible
in the role file's scope field or a role-type annotation — not inferred only from directory
placement.
**Pass condition**: At least one role file for a standard role and at least one for a
specialized role each contain explicit scope or role-type language that differentiates them.
Exec office roles (if declared in org.yaml) are placed under an exec-office area, not
embedded inside a team area.

---

### C-08 — AMEND section with three actionable options
**Weight**: recommended
**Category**: behavior
**Text**: The output includes an AMEND section listing exactly three amendment options the
user can invoke: (1) regenerate a specific area, (2) adjust level vocabulary, (3) change
group structure. Each option is concrete and references the relevant org.yaml element.
**Pass condition**: AMEND section present. Three distinct options listed. Each option names
a specific mechanism (area name, level term, group node) rather than a generic description.

---

## Aspirational Criteria (10 points total — raise the bar)

### C-09 — Inertia Advocate role files are team-contextualized
**Weight**: aspirational
**Category**: depth
**Text**: Each Inertia Advocate role file is customized to the specific team context: the
lens and expertise fields reference that team's domain, not a generic "status quo" boilerplate
copied across all teams.
**Pass condition**: No two Inertia Advocate role files share identical lens or expertise
body text. Each references at least one domain-specific term drawn from the team's declared
responsibilities in org.yaml.

---

### C-10 — Cross-reference integrity between org-chart.md and .craft/roles/
**Weight**: aspirational
**Category**: correctness
**Text**: Every role path referenced or implied in org-chart.md resolves to an actual file
in .craft/roles/. The headcount total in the chart matches the count of generated role files.
**Pass condition**: Headcount total in org-chart.md equals the number of .craft/roles/ files
generated (excluding any index or README files). No role mentioned in the chart is absent
from .craft/roles/. No file in .craft/roles/ is unmentioned in org-chart.md.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

---

## Criterion Summary

| ID   | Text (short)                            | Weight        | Category    |
|------|-----------------------------------------|---------------|-------------|
| C-01 | Role file completeness                  | essential     | correctness |
| C-02 | org-chart.md with ASCII diagram         | essential     | format      |
| C-03 | Inertia Advocate in every team          | essential     | correctness |
| C-04 | org.yaml structural fidelity            | essential     | correctness |
| C-05 | Role file typed fields present          | essential     | coverage    |
| C-06 | Headcount by group table + levels       | recommended   | depth       |
| C-07 | Standard vs specialized distinction     | recommended   | correctness |
| C-08 | AMEND section with three options        | recommended   | behavior    |
| C-09 | Inertia Advocate team-contextualized    | aspirational  | depth       |
| C-10 | Cross-reference integrity chart/roles   | aspirational  | correctness |
