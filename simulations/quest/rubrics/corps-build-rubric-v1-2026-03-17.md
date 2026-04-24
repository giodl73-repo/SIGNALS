---
skill: quest-rubric
skill_target: corps-build
date: 2026-03-17
version: 1
---

# Scoring Rubric: corps-build

Read a confirmed org.yaml and generate the full org. Outputs: org-chart.md with ASCII
box diagram, headcount by group/area, level distribution; .roles/{area}/{role}.md
typed files for every role. Supports arbitrary nesting: Division > Team > Sub-group.
Inertia-advocate always in every team. AMEND section with three actionable options.

---

## Essential Criteria (60 points total -- all must pass)

### C-01 -- Role file completeness
**Weight**: essential
**Category**: correctness
**Text**: Without complete role file generation, the artifact fails because downstream
skills (org-review, org-committee) reference .roles/ paths that do not exist. Not
partial generation with most roles present, but complete generation where every declared
role has a corresponding file.
**Pass condition**:
- LOCATION: .roles/ directory tree
- OBSERVABLE: count of role files (excluding index or README files)
- STANDARD: equals total roles declared in org.yaml; zero missing, zero phantom

---

### C-02 -- org-chart.md with ASCII hierarchy
**Weight**: essential
**Category**: format
**Text**: Without org-chart.md containing an ASCII hierarchy, the artifact fails because
consumers cannot visually verify the organizational structure without parsing the file tree
manually. Not a prose description of teams, but an ASCII diagram showing declared nesting.
**Pass condition**:
- LOCATION: org-chart.md
- OBSERVABLE: ASCII tree using box-drawing or dash/pipe characters
- STANDARD: all areas from org.yaml appear in the diagram; at least 2 hierarchy levels
  visible; group names in the diagram match org.yaml group names character-for-character

---

### C-03 -- Inertia Advocate present in every team
**Weight**: essential
**Category**: correctness
**Text**: Without an Inertia Advocate role file in every team, the artifact fails because
the mandatory change-resistance perspective is absent from teams where it is most needed.
Not one global Inertia Advocate, but one per team declared in org.yaml.
**Pass condition**:
- LOCATION: .roles/{area}/ subdirectories
- OBSERVABLE: inertia-advocate.md (or canonical equivalent) per team node
- STANDARD: count of Inertia Advocate files equals count of team nodes in org.yaml

---

### C-04 -- org.yaml structural fidelity
**Weight**: essential
**Category**: correctness
**Text**: Without structural fidelity to org.yaml nesting, the artifact fails because the
directory tree misrepresents the organization and breaks area-specific amendment operations.
Not a flattened all-roles directory, but a nested structure that mirrors the declared
Division > Team > Sub-group hierarchy.
**Pass condition**:
- LOCATION: .roles/ directory structure
- OBSERVABLE: area subdirectory names
- STANDARD: one-to-one map to org.yaml area names; no area added, no area missing

---

### C-05 -- Role file typed fields present
**Weight**: essential
**Category**: coverage
**Text**: Without all five typed fields populated in every role file, the artifact fails
because role files cannot be used in org-review without complete orientation, lens,
expertise, scope, and collaboration pattern. Not files with section headings and empty
bodies, but files with substantive content in every required field.
**Pass condition**:
- LOCATION: each .roles/{area}/{role}.md
- OBSERVABLE: five required headings (orientation, lens, expertise, scope, collaboration
  pattern) each with non-empty body text
- STANDARD: all five present per file; "TBD" or empty body fails this criterion

---

## Recommended Criteria (30 points total -- output is better with these)

### C-06 -- Headcount by group table with level distribution
**Weight**: recommended
**Category**: depth
**Dimension**: precision
**Text**: Without a headcount-by-group table in org-chart.md, the artifact fails because
program planning cannot confirm resourcing at a glance. Not ad-hoc counting from the file
tree, but an explicit table with per-area rows, a Total row, and level distribution visible.
**Pass condition**:
- LOCATION: org-chart.md headcount section
- OBSERVABLE: table with one row per area/group and a Total row
- STANDARD: per-area counts sum to Total; level distribution (IC vs management, or explicit
  level labels from org.yaml) visible in the same table or a companion section

---

### C-07 -- Standard vs specialized role type distinction
**Weight**: recommended
**Category**: correctness
**Dimension**: specificity
**Text**: Without explicit role type annotation in role files, the artifact fails because
org-review cannot distinguish team-universal roles from team-specific expertise using file
content alone. Not directory placement as the only distinguisher, but an explicit type
annotation in the scope or role-type field of every role file.
**Pass condition**:
- LOCATION: scope or role-type field in each .roles/ file
- OBSERVABLE: explicit type label (standard | specialized | exec-office | shared-group)
- STANDARD: at least one standard role and at least one specialized role each carry the
  label; exec-office roles (if declared) placed under exec-office area, not inside teams

---

### C-08 -- AMEND section with three actionable options
**Weight**: recommended
**Category**: behavior
**Dimension**: degree
**Text**: Without an AMEND section listing the three amendment options, the artifact fails
because users have no guided path to iterate on the generated org. Not a general edit
invitation, but three specific amendment verbs each referencing a concrete target.
**Pass condition**:
- LOCATION: AMEND section at end of primary output
- OBSERVABLE: three listed options
- STANDARD: option 1 = regenerate a specific area (names an area from org.yaml); option 2 =
  adjust level vocabulary (names a level term); option 3 = change group structure (names a
  group node); generic descriptions without named targets fail

---

## Aspirational Criteria (10 points total -- raise the bar)

### C-09 -- Inertia Advocate files are team-contextualized
**Weight**: aspirational
**Category**: depth
**Gap closed**: team-contextualization mechanism
**Text**: Without team-contextualized Inertia Advocate content, the artifact fails because
identical boilerplate across teams cannot be distinguished from lazy generation that ignored
team responsibilities. Not the same lens and expertise text reused across teams, but
domain-specific content per team drawn from that team's declared responsibilities.
**Pass condition**:
- LOCATION: lens and expertise fields in each inertia-advocate.md
- OBSERVABLE: domain-specific terms from the team's responsibilities in org.yaml
- STANDARD: no two Inertia Advocate files share identical lens or expertise body text; each
  file references at least one term tied to that team's declared domain

---

### C-10 -- Cross-reference integrity between org-chart.md and .roles/
**Weight**: aspirational
**Category**: correctness
**Gap closed**: cross-reference integrity mechanism
**Text**: Without cross-reference integrity, the artifact fails because a reader cannot
confirm from the chart alone that the generated file set is complete. Not independent counts
that happen to agree by coincidence, but a verifiable link between the org-chart.md headcount
total and the actual count of generated role files.
**Pass condition**:
- LOCATION: org-chart.md headcount Total row AND .roles/ file count
- OBSERVABLE: numeric equality between chart total and file count
- STANDARD: Total in org-chart.md = count of .roles/ files (excluding index/README);
  no role referenced in the chart is absent from .roles/

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

| Tier          | Weight | Count | Max   |
|---------------|--------|-------|-------|
| Essential     | 1.0    | 5     | 60    |
| Recommended   | 0.5    | 3     | 30    |
| Aspirational  | 0.25   | 2     | 10    |

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

**PARTIAL**: composite >= 60 with all 5 essential passing = PARTIAL PASS. Earn full PASS
by satisfying at least 2 of 3 recommended criteria.

---

## Criterion Summary

| ID   | Text (short)                            | Weight        | Category    |
|------|-----------------------------------------|---------------|-------------|
| C-01 | Role file completeness                  | essential     | correctness |
| C-02 | org-chart.md with ASCII hierarchy       | essential     | format      |
| C-03 | Inertia Advocate in every team          | essential     | correctness |
| C-04 | org.yaml structural fidelity            | essential     | correctness |
| C-05 | Role file typed fields present          | essential     | coverage    |
| C-06 | Headcount by group table + levels       | recommended   | depth       |
| C-07 | Standard vs specialized distinction     | recommended   | correctness |
| C-08 | AMEND section with three options        | recommended   | behavior    |
| C-09 | Inertia Advocate team-contextualized    | aspirational  | depth       |
| C-10 | Cross-reference integrity chart/roles   | aspirational  | correctness |
