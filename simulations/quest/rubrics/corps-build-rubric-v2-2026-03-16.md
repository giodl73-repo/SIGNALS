Done. Here's what changed:

**4 new aspirational criteria added (C-11 through C-14):**

| ID | Pattern | Source |
|----|---------|--------|
| C-11 | Pre-write structural validation gate | V-03 on C-04 — VALIDATE phase before any writes; halts on duplicate names or role collisions |
| C-12 | IA-first write ordering | V-01/V-04 on C-03 — IA files written before standard/specialized roles; omission impossible by construction |
| C-13 | Headcount table as build contract | V-02 on C-06 — table built first, file writes derived from table rows |
| C-14 | Org analytic narrative prose | V-05 on C-06 — 2-3 sentences naming largest area, level concentration, seniority profile |

**Score formula updated:** `aspirational_pass / 6 * 10` (was `/2`). The 10-point aspirational pool is unchanged; it now spreads across 6 criteria instead of 2.

**What was left out:** The V-04 "fields populated by construction from resistance profile" pattern — this is a mechanism distinction (how fields get populated) rather than an output distinction, and output quality is already evaluated by C-05 (no placeholders) and C-09 (team-contextualized). Not useful as a rubric criterion.
atch org.yaml exactly.
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

### C-11 — Pre-write structural validation gate
**Weight**: aspirational
**Category**: correctness
**Source**: R1 excellence signal — V-03 on C-04
**Text**: A dedicated VALIDATE phase runs before any role files or org-chart.md are written.
It checks: no duplicate team names, no role-name collision within a team, no area declared
in org.yaml with no roles. The build halts and reports failures before touching the
filesystem if any check fails.
**Pass condition**: The output narrative or step log shows an explicit validation phase
preceding the first file write. At minimum two structural checks are named (e.g.,
duplicate-name check, role-collision check). If validation fails, no files are written and
the failure names the specific node or role at fault.

---

### C-12 — Inertia Advocate files written before standard and specialized roles
**Weight**: aspirational
**Category**: correctness
**Source**: R1 excellence signal — V-01/V-04 on C-03
**Text**: All Inertia Advocate role files are generated either as the first file per team
or in a dedicated IA phase that completes before any standard or specialized roles are
written. This ordering makes IA omission structurally impossible — an unstarted IA file
means the team is not yet begun, not silently skipped.
**Pass condition**: The output step sequence places every IA write before the first
standard or specialized role write for its team. Alternatively, a dedicated IA phase is
named and all IA files are confirmed complete before the standard-role phase begins. A
BUILD-COMPLETE or phase-gate block explicitly confirms IA coverage ("X of X teams
covered") at the end of the IA phase.

---

### C-13 — Headcount table constructed as build contract before role files
**Weight**: aspirational
**Category**: depth
**Source**: R1 excellence signal — V-02 on C-06
**Text**: The headcount table in org-chart.md is the first artifact produced, before any
.craft/roles/ files are written. The file-writing phase derives its work items from the
table — each row becomes a write target. This makes the table a contract between the
declared org structure and the generated file set rather than a post-hoc summary.
**Pass condition**: The output step log or narrative shows the headcount table written
prior to the first role file. The role-file writing phase references the table (or its
row count) as the source of its work list. Final totals in the table match the number
of role files produced.

---

### C-14 — Org analytic narrative prose alongside headcount tables
**Weight**: aspirational
**Category**: depth
**Source**: R1 excellence signal — V-05 on C-06
**Text**: The headcount section of org-chart.md includes 2-3 sentences of analytic prose
that interpret the numbers — identifying the largest area by headcount, naming any
concentration in level distribution, flagging teams with no declared levels, and providing
a one-sentence seniority profile. The narrative adds interpretive value that the table rows
alone do not convey.
**Pass condition**: org-chart.md contains at least two prose sentences adjacent to (not
inside) the headcount tables. At least one sentence names a specific area or level finding
(e.g., "Platform Engineering accounts for 40% of total headcount"). Sentences are not
generic templates — they reference actual values from the generated org.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

---

## Criterion Summary

| ID   | Text (short)                              | Weight       | Category    |
|------|-------------------------------------------|--------------|-------------|
| C-01 | Role file completeness                    | essential    | correctness |
| C-02 | org-chart.md with ASCII diagram           | essential    | format      |
| C-03 | Inertia Advocate in every team            | essential    | correctness |
| C-04 | org.yaml structural fidelity              | essential    | correctness |
| C-05 | Role file typed fields present            | essential    | coverage    |
| C-06 | Headcount by group table + levels         | recommended  | depth       |
| C-07 | Standard vs specialized distinction       | recommended  | correctness |
| C-08 | AMEND section with three options          | recommended  | behavior    |
| C-09 | Inertia Advocate team-contextualized      | aspirational | depth       |
| C-10 | Cross-reference integrity chart/roles     | aspirational | correctness |
| C-11 | Pre-write structural validation gate      | aspirational | correctness |
| C-12 | IA-first write ordering                   | aspirational | correctness |
| C-13 | Headcount table as build contract         | aspirational | depth       |
| C-14 | Org analytic narrative prose              | aspirational | depth       |
