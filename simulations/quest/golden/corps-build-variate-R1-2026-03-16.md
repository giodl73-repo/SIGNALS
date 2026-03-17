---
skill: quest-variate
skill_target: corps-build
round: 1
date: 2026-03-16
rubric_version: 1
---

# Variate R1 — corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (Inertia Advocate generated first per team) | V-01, V-04 |
| Output format (table-first org-chart.md vs prose-section hybrid) | V-02, V-05 |
| Lifecycle emphasis (explicit phase gates with entry conditions) | V-03, V-05 |
| Inertia framing (resistance profiles before any file writing) | V-04 |
| Phrasing register (imperative/structured vs descriptive/narrative) | V-02 |

---

## V-01 — Role Sequence: Inertia Advocate First

**Axis**: Role sequence
**Hypothesis**: Generating the Inertia Advocate role file before any standard or specialized
role for each team eliminates the most common C-03 failure: IA files added as an afterthought
and silently omitted from one or more teams. Because IA is the first file written per team by
construction, every team that exists in org.yaml will have an IA file. The IA is also written
while the team's context is freshest in the model's attention, improving C-09 contextualization.
Standard and specialized roles follow per team. This variation is strongest on C-03 and C-09.

---

You are running `corps-build`. Read the org.yaml at the path provided, or auto-detect `org.yaml`
in the working directory if no path is given.

**STEP 1 — PARSE ORG.YAML**

Read org.yaml. Extract and echo:

```
ORG-PARSED:
  org name: [name]
  nesting depth: [n levels]
  groups: [list all Division/Group names]
  teams: [list all Team names with parent group]
  roles per team:
    [team name]: standard=[list names x count], specialized=[list names x count]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "none"]
  total role slots: [n]
```

If org.yaml is missing or malformed, halt: `PARSE ERROR: [describe problem]. Correct org.yaml
before running corps-build.`

**STEP 2 — PER-TEAM: INERTIA ADVOCATE FIRST**

For each team in org.yaml, in declaration order, run sub-steps 2a then 2b then 2c before
moving to the next team.

**2a. Write the Inertia Advocate file first.**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five required fields — populate from the team's declared context in org.yaml:

- **orientation**: Why a senior member of this team would rationally defend the existing
  arrangement. Draw from the team's declared responsibilities. Name the specific concern.
- **lens**: The domain-specific status quo this advocate protects. Must reference at least one
  term drawn from the team's name or declared responsibilities. No generic "stability" language.
- **expertise**: What makes this person's skepticism technically credible. Name the specific
  systems, processes, or decisions they have built or run.
- **scope**: `standard — present in all teams`
- **collaboration pattern**: How this role surfaces resistance — which forums (design review,
  sprint planning, architecture board), on what cadence, and which counterpart role they engage
  most directly.

No copy-paste across teams. The `lens` and `expertise` fields must differ between teams because
they are drawn from different team contexts. Two teams with identical `lens` text is a build error.

After writing: `IA-WRITTEN: [team name] — lens: "[one phrase from team context used]"`

**2b. Write standard role files for this team.**

Standard roles are shared across all teams (the same role name appears in multiple teams).

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Required fields for each:
- **orientation**: Perspective this role brings to the team's work
- **lens**: Domain focus — what aspect of the system or product this role attends to
- **expertise**: What this role knows that others do not
- **scope**: `standard — present in all teams`
- **collaboration pattern**: Key counterpart roles and interaction mode

**2c. Write specialized role files for this team.**

Specialized roles are unique to this team.

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Same five fields. Scope must read: `specialized — [team name]`.

After all files for a team: `TEAM-COMPLETE: [team name] — [n] files written (1 IA + [n] standard
+ [n] specialized)`

**STEP 3 — SHARED GROUP ROLES**

If org.yaml declares roles at the group or division level (not assigned to any specific team):

Path: `.craft/roles/{group-slug}/{role-slug}.md` (no team subdirectory)

Scope: `shared — group: [group name]`

**STEP 4 — EXEC OFFICE ROLES**

If org.yaml declares exec office roles:

Path: `.craft/roles/exec-office/{role-slug}.md`

Scope: `exec office`

**STEP 5 — WRITE ORG-CHART.MD**

After all role files are written, generate `org-chart.md`. Sections in this order:

**5a. ASCII Org Diagram**

Draw hierarchy after the table — minimum two levels. Use box-drawing characters (`+--`, `|`).
Each leaf node (team) shows headcount in parentheses. Group names must match org.yaml
character-for-character. Do not introduce nodes not present in org.yaml.

**5b. Headcount by Group/Area**

```markdown
## Headcount by Group/Area

| Group/Area | Headcount | Key Roles |
|------------|-----------|-----------|
| [name]     | [n]       | [role names] |
| **Total**  | **[n]**   |           |
```

Headcount per area = sum of all role slots in that area. Total = sum of all area rows.

**5c. Level Distribution**

```markdown
## Level Distribution

| Level  | Count | % of Org |
|--------|-------|----------|
| [label]| [n]   | [n]%     |
| **Total** | **[n]** | 100% |
```

Level labels drawn directly from org.yaml `level:` fields. If no levels declared, infer `IC`
and `Management` from role names. Total must match headcount table total.

**STEP 6 — AMEND SECTION**

Append to org-chart.md:

```markdown
## AMEND

Run `corps-build --amend` with one of these options:

1. **Regenerate area**: `--area "[area name]"` — rewrites all .craft/roles/ files for the
   named area (including its IA file) and updates the corresponding org-chart.md rows.
   Available areas in this build: [list area names from org.yaml]

2. **Adjust level vocabulary**: `--levels "[old]:[new]"` — replaces level labels throughout
   org-chart.md Level Distribution and all role file scope fields.
   Levels currently in use: [list unique level values from org.yaml]

3. **Change group structure**: `--restructure "[team] > [new-parent]"` — moves a team to a
   new parent group, renames the .craft/roles/ subdirectory, and redraws the org diagram.
   Current structure: [list group > team nesting relationships from org.yaml]
```

**STEP 7 — VERIFY AND EMIT SUMMARY**

Count:
- Role slots declared in org.yaml
- .craft/roles/ files written (exclude README or index files)
- Teams in org.yaml
- IA files written

Emit:

```
BUILD-COMPLETE:
  org.yaml roles declared: [n]
  .craft/roles/ files written: [n]
  match: [YES / NO]
  if NO — missing: [list role names]
  teams with IA files: [n of n]
  org-chart.md: written
  AMEND section: written
```

If file count != declared count: `BUILD-WARNING: [n] discrepancies found. List: [names].`

Generated by: corps-build — {date}

---

## V-02 — Output Format: Table-Driven org-chart.md

**Axis**: Output format
**Hypothesis**: Building org-chart.md as a table-first document — headcount table before the ASCII
diagram — makes C-06 and C-10 mechanically auditable. The headcount table becomes the authoritative
source for the role count, and the ASCII diagram is derived from it rather than constructed
independently. The `TABLE-CLOSED` gate emits the authoritative total before any files are written,
so the model has a concrete target count to hit. Cross-reference integrity (C-10) becomes a
natural closing check rather than a post-hoc verification. Risk: the table-dominant format may
under-serve C-09 (IA contextualization) if the model writes IA files to fit the table schema
rather than using team context.

---

You are running `corps-build`. Read org.yaml (auto-detect or use path provided).

**1. PARSE**

Read org.yaml. Extract all groups, teams, roles (standard and specialized), shared group roles,
exec office roles, and level labels.

Internal summary (not emitted in final output):
```
INTERNAL:
  total role slots: [n]
  unique role types: [n]
  teams: [n]
  max nesting depth: [n]
```

Halt with parse error if org.yaml is missing or structurally invalid.

**2. BUILD HEADCOUNT TABLE — AUTHORITATIVE**

Before writing any files, produce the headcount table. This table is the authoritative source
for all subsequent sections. Any discrepancy between this table's total and the files written
is a build error.

```markdown
## Headcount by Group/Area

| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [role names]   | [names or —]      | [labels or —] |
| **Total**  | **[n]**   |                |                   |        |
```

Rules:
- One row per team/area node from org.yaml (not one row per individual role slot)
- Headcount = sum of all role slots declared for that area
- Standard Roles: role types shared across all teams — list names, deduplicated across teams
- Specialized Roles: roles unique to this team — list names
- Levels: all level labels present in this area's roles
- Total row = sum of all area headcounts

Emit after table: `TABLE-CLOSED: [n] area rows, [n] total headcount. This is the authoritative
count. Role file generation must produce exactly [n] .craft/roles/ files.`

**3. LEVEL DISTRIBUTION TABLE**

Immediately after the headcount table:

```markdown
## Level Distribution

| Level  | Headcount | % of Org |
|--------|-----------|----------|
| [label from org.yaml] | [n] | [n]% |
| **Total** | **[n]** | 100% |
```

Draw level labels directly from org.yaml. If no levels declared, infer from role names
(`IC` / `Management`). Total must match the headcount table Total row.

**4. ASCII ORG DIAGRAM**

Generate the ASCII hierarchy after the tables. Derive structure exclusively from the headcount
table — do not introduce any groups or teams not present in the table.

```
[Org Name]
+-- [Division/Group]
    +-- [Team] ([n])
    |   +-- [Sub-group] ([n])
    +-- [Team] ([n])
+-- [Division/Group]
    +-- [Team] ([n])
```

Each leaf node shows headcount in parentheses, pulled from the table. Group names must match
org.yaml character-for-character.

Emit after diagram: `DIAGRAM-DERIVED: all [n] nodes sourced from headcount table rows.`

**5. WRITE ROLE FILES**

Write all .craft/roles/ files. Process in headcount table row order — left to right, top to
bottom. For each area row:

a. Write standard role files: `.craft/roles/{area-slug}/{role-slug}.md`
b. Write specialized role files: `.craft/roles/{area-slug}/{role-slug}.md`
c. Write Inertia Advocate: `.craft/roles/{area-slug}/inertia-advocate.md`

Also write:
- Shared group roles: `.craft/roles/{group-slug}/{role-slug}.md`
- Exec office roles: `.craft/roles/exec-office/{role-slug}.md`

Every role file must contain all five fields. No placeholder text ("TBD", empty sections):
- **orientation**
- **lens**
- **expertise**
- **scope**: one of `standard`, `specialized — [team name]`, `shared — [group name]`, `exec office`
- **collaboration pattern**

Standard vs specialized distinction must be explicit in the `scope` field — not derivable only
from directory placement.

IA files: `lens` and `expertise` must reference at least one term from the team's context in
org.yaml. No identical `lens` or `expertise` text across two IA files.

After each area: `AREA-WRITTEN: [area name] — [n] files. Running total: [n of TABLE-CLOSED total].`

**6. CROSS-REFERENCE CHECK**

After all files are written:

- Count .craft/roles/ files generated (exclude README or index files)
- Compare to TABLE-CLOSED authoritative count

```
CROSS-REF:
  table declared: [n]
  files written: [n]
  match: [YES / MISMATCH]
  if MISMATCH: in table not found in files: [list]
               in files not found in table: [list]
```

If mismatch: `BUILD-ERROR: cross-reference mismatch. Build is not consistent.`
If match: `CROSS-REF PASS: [n] files match [n] declared. Build is consistent.`

**7. AMEND SECTION**

Append to org-chart.md:

```markdown
## AMEND

Run `corps-build --amend` with one of these options:

1. **Regenerate area**: `--area "[area name]"` — rewrites all .craft/roles/ files for the
   named area and updates its headcount table row in org-chart.md.
   Available areas: [list area names from headcount table]

2. **Adjust level vocabulary**: `--levels "[old]:[new]"` — replaces level labels in the
   Level Distribution table and all role file scope fields.
   Levels currently in use: [list from Level Distribution table]

3. **Change group structure**: `--restructure "[team] > [new-parent]"` — moves a team to
   a new parent group, renames the .craft/roles/ subdirectory, and redraws the ASCII diagram.
   Current structure: [list nesting relationships from headcount table]
```

Generated by: corps-build — {date}

---

## V-03 — Lifecycle Emphasis: Explicit Phase Gates

**Axis**: Lifecycle emphasis
**Hypothesis**: Structuring corps-build as five named phases — PARSE, VALIDATE, WRITE-CHART,
WRITE-ROLES, VERIFY — each with an explicit entry condition and a gate confirmation line,
catches structural failures before any files are written (VALIDATE), and prevents the model
from skipping output sections under compression pressure (each gate must appear before the
next phase can begin). The VALIDATE phase specifically rejects org.yaml structural problems
that would produce silent failures (phantom files, missing areas, role name collisions) in a
free-form approach. This variation is strongest on C-01 (no missing files) and C-04 (structural
fidelity). Risk: the phase structure adds verbosity; the model may abbreviate later phases to
stay within output limits.

---

You are running `corps-build`. Read org.yaml — auto-detect in current directory, or use the
provided path. Work through phases in order. Do not begin a phase until its entry condition is
confirmed and its gate line is emitted.

---

### PHASE 1 — PARSE

**Entry condition**: org.yaml is accessible.

Read org.yaml. Emit a structured parse output:

```
PARSE RESULT:
  org name: [name]
  nesting depth: [n levels]
  groups: [list Division/Group names]
  teams:
    [team name] (parent: [group]) — standard: [roles], specialized: [roles]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "none declared"]
  total role slots: [n]
```

**PHASE 1 GATE**:
- org.yaml not found: `PARSE GATE FAIL: org.yaml not found at [path]. Provide a valid path.` — HALT.
- no team nodes: `PARSE GATE FAIL: no team nodes found. org.yaml must declare at least one team.` — HALT.
- no roles: `PARSE GATE FAIL: no roles found. Each team must declare at least one role.` — HALT.
- otherwise: `PARSE GATE PASS: [n] teams, [n] total role slots, [n] nesting levels. Proceeding to VALIDATE.`

---

### PHASE 2 — VALIDATE

**Entry condition**: PARSE GATE PASS present in output.

Run these five checks. Emit PASS or FAIL for each:

```
VALIDATE CHECKS:
  V-1  every team has at least one role
       [PASS / FAIL: [team name] has no roles]

  V-2  no role name appears in both standard and specialized for the same team
       [PASS / FAIL: [role name] in [team] is both standard and specialized]

  V-3  no duplicate team names across the org
       [PASS / FAIL: [name] appears [n] times]

  V-4  all level labels use consistent vocabulary (not mix of "L5" and "Senior Engineer")
       [PASS / FAIL: inconsistent labels: [list]]

  V-5  exec office roles (if declared) are not also assigned to a team node
       [PASS / FAIL: [role] appears under both exec-office and [team name]]
```

**PHASE 2 GATE**:
- any FAIL: `VALIDATE GATE FAIL: [n] errors. Correct org.yaml before proceeding.` — HALT.
- all pass: `VALIDATE GATE PASS: all 5 checks pass. Proceeding to WRITE-CHART.`

---

### PHASE 3 — WRITE-CHART

**Entry condition**: VALIDATE GATE PASS present in output.

Write `org-chart.md`. Sections in this exact order within the file:

**3a. ASCII Org Diagram**

Draw the full hierarchy. Minimum two levels. Use dash/pipe or box-drawing characters. Each
leaf team node shows headcount in parentheses. Group names must match org.yaml exactly.

Emit after diagram: `DIAGRAM-WRITTEN: [n] team nodes, [n] group nodes, max depth [n].`

**3b. Headcount by Group/Area**

```markdown
## Headcount by Group/Area

| Group/Area | Headcount | Key Roles |
|------------|-----------|-----------|
| [name]     | [n]       | [role names] |
| **Total**  | **[n]**   |           |
```

Headcount per area = sum of role slots. Total = sum of all areas.

**3c. Level Distribution**

```markdown
## Level Distribution

| Level  | Count | % |
|--------|-------|---|
| [label]| [n]   | [n]% |
| **Total** | **[n]** | 100% |
```

Labels from org.yaml. Total must match headcount table Total.

**3d. AMEND Section**

```markdown
## AMEND

Run `corps-build --amend` with one of these options:

1. **Regenerate area**: `--area "[name]"` — rewrites all .craft/roles/ files for one area
   and updates its org-chart.md headcount row.
   Target areas: [list area names from org.yaml]

2. **Adjust level vocabulary**: `--levels "[old]:[new]"` — replaces level labels throughout
   org-chart.md and all role files.
   Current levels: [list level values from org.yaml]

3. **Change group structure**: `--restructure "[team] > [new-parent]"` — moves a team node,
   renames its .craft/roles/ subdirectory, and redraws the ASCII diagram.
   Current nesting: [describe parent-child relationships from org.yaml]
```

Emit: `CHART-GATE PASS: org-chart.md written with diagram, headcount table, level distribution,
and AMEND section. Proceeding to WRITE-ROLES.`

---

### PHASE 4 — WRITE-ROLES

**Entry condition**: CHART-GATE PASS present in output.

Write all .craft/roles/ files. Process in this order:
1. Exec office roles (if declared)
2. Shared group roles (if declared)
3. Per-team: standard roles → specialized roles → Inertia Advocate (for each team)

**File path conventions**:
- Standard/specialized: `.craft/roles/{area-slug}/{role-slug}.md`
- Shared group: `.craft/roles/{group-slug}/{role-slug}.md`
- Exec office: `.craft/roles/exec-office/{role-slug}.md`
- Inertia Advocate: `.craft/roles/{area-slug}/inertia-advocate.md`

**Required fields for every role file** — no placeholder text allowed:
- **orientation**: perspective this role brings to the team's work
- **lens**: specific domain focus
- **expertise**: what this role uniquely knows
- **scope**: exactly one of `standard`, `specialized — [team name]`, `shared — [group name]`,
  or `exec office`
- **collaboration pattern**: counterpart roles and interaction mode

**Standard vs specialized**: must be explicit in the `scope` field — not derivable only from
directory placement.

**Inertia Advocate per team**: `lens` must reference at least one domain-specific term from
the team's context in org.yaml. `expertise` must name specific systems or decisions this
advocate has institutional knowledge of. No two IA files may share identical `lens` or
`expertise` body text.

After each team: `TEAM-WRITTEN: [team name] — [n] files (1 IA + [n] std + [n] spec).
Running count: [n of total].`

**PHASE 4 GATE**:

```
ROLES-GATE:
  declared in org.yaml: [n]
  .craft/roles/ files written: [n]
  match: [YES / NO]
  if NO — missing: [list role names not written]
```

If not match: `ROLES-GATE FAIL: [n] files missing. Build incomplete.`
If match: `ROLES-GATE PASS: [n] files written, [n] declared. All present. Proceeding to VERIFY.`

---

### PHASE 5 — VERIFY

**Entry condition**: ROLES-GATE PASS present in output.

Verify AMEND section written in Phase 3 references actual org.yaml elements:

- Option 1 names at least one actual area name: [check and list]
- Option 2 names at least one actual level value: [check and list]
- Option 3 names at least one actual group nesting relationship: [check and list]

Emit: `AMEND-VERIFIED: 3 options present with concrete references. [list area, level, and
structure references used]`

If generic: `AMEND-WARNING: options are too generic. Rewrite to reference actual org.yaml
elements.`

---

**FINAL SUMMARY**

```
BUILD SUMMARY — corps-build — {date}
  org.yaml:       parsed and validated (all 5 checks pass)
  org-chart.md:   written
  .craft/roles/:  [n] files / [n] declared
  IA coverage:    [n of n] teams
  AMEND section:  verified
  status:         COMPLETE / INCOMPLETE
```

Generated by: corps-build — {date}

---

## V-04 — Role Sequence + Inertia Framing (Combination)

**Axes**: Role sequence (IA first) + Inertia framing (resistance profiles before any file writing)
**Hypothesis**: Running a per-team resistance profiling step before writing any files produces
Inertia Advocate files that are genuinely contextualized (C-09) rather than structurally
correct but boilerplate. The resistance profile names what each team's IA will defend — drawn
from org.yaml context — and this profile is referenced directly when writing the IA file.
Combining IA-first role ordering (V-01) with pre-writing resistance profiling produces the
strongest C-03 + C-09 combination: no team is missing an IA, and no two IA files share a lens.
Risk: the profiling step adds output length before any files are written; under token pressure,
later teams may receive less thorough profiling.

---

You are running `corps-build`. Read org.yaml — auto-detect or use path provided.

**STEP 1 — PARSE**

Read org.yaml. Identify all teams and their declared responsibilities/roles. Emit:

```
PARSED:
  org name: [name]
  teams: [list: team name — parent group]
  total role slots: [n]
  levels declared: [list or "none"]
```

Halt on parse error with specific message.

**STEP 2 — RESISTANCE PROFILES**

Before writing any files, generate a resistance profile for each team. A resistance profile
answers: *What does a senior member of this team, with 3+ years of history here, defend as
non-negotiable?* It names the specific practice, system, or decision they believe the org
structure must preserve.

For each team, write a structured profile:

```
RESISTANCE PROFILES:

[Team Name]
  Status quo defended: [specific practice, system, or decision — not generic "stability"]
  Credibility source: [what this person has built or run that grounds their skepticism]
  Failure mode seen: [the specific bad outcome that shaped their caution]
  IA lens phrase: [one phrase, ≤8 words, that will anchor this team's IA lens field]
```

Rules:
- Do not use "they value stability," "institutional knowledge," or equivalent placeholders.
  Name the specific system, code path, or operational process.
- The `IA lens phrase` must differ across all teams — it becomes the distinguishing text in
  the IA file and is the primary C-09 signal.

Emit after all profiles: `RESISTANCE-COMPLETE: [n] teams profiled. IA lens phrases: [list one
per team].`

**STEP 3 — WRITE INERTIA ADVOCATE FILES (all teams, before any other role)**

For each team, in declaration order, write the IA file using the resistance profile from Step 2.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Required fields — populated from the resistance profile:
- **orientation**: Drawn from "Status quo defended." Describes the rational, experienced
  perspective this advocate holds — not a cartoon of change-resistance.
- **lens**: Opens with the `IA lens phrase` from Step 2. Expands it in 2-3 sentences naming
  the domain-specific status quo: which system, decision pattern, or operational practice this
  advocate monitors for signs of degradation.
- **expertise**: Drawn from "Credibility source." Names the specific systems, code, or
  processes this person has run. Must be distinct from every other team's IA expertise entry.
- **scope**: `standard — present in all teams`
- **collaboration pattern**: Surfaces resistance in design reviews, sprint planning, and
  architecture discussions. Primary counterpart: [the standard role most likely to propose
  changes in this team]. Escalates to group lead when velocity pressure overrides quality threshold.

Verification: no two IA files may share identical `lens` or `expertise` text.

Emit after each: `IA-WRITTEN: [team name] — lens phrase: "[phrase from Step 2]"`

Emit after all IA files: `IA-PHASE-COMPLETE: [n] IA files written. All [n] teams covered.`

**STEP 4 — WRITE REMAINING ROLE FILES (per team)**

For each team, after its IA file is already written:

**4a. Standard role files** (roles shared across all teams):

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Five fields required:
- **orientation**, **lens**, **expertise**: role-specific content
- **scope**: `standard — present in all teams`
- **collaboration pattern**: key counterparts and interaction mode

**4b. Specialized role files** (roles unique to this team):

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Same five fields. Scope: `specialized — [team name]`

Emit after a team is complete: `TEAM-COMPLETE: [team name] — [n] files (1 IA + [n] std + [n] spec)`

**4c. Shared group roles** (if declared in org.yaml at group level):

Path: `.craft/roles/{group-slug}/{role-slug}.md`
Scope: `shared — group: [group name]`

**4d. Exec office roles** (if declared):

Path: `.craft/roles/exec-office/{role-slug}.md`
Scope: `exec office`

**STEP 5 — WRITE ORG-CHART.MD**

After all role files are written, generate `org-chart.md`. Sections:

**5a. ASCII Org Diagram**

Hierarchy showing all nesting levels from org.yaml. Minimum two levels. Box-drawing or dash/pipe.
Each team node shows headcount. Group names must match org.yaml exactly.

**5b. Headcount by Group/Area**

```markdown
| Group/Area | Headcount | Standard Roles | Specialized Roles |
|------------|-----------|----------------|-------------------|
| [name]     | [n]       | [names]        | [names or —]      |
| **Total**  | **[n]**   |                |                   |
```

**5c. Level Distribution**

```markdown
| Level  | Count | % of Org |
|--------|-------|----------|
| [label]| [n]   | [n]%     |
| **Total** | **[n]** | 100% |
```

**5d. Resistance Summary** (appended below Level Distribution)

One-line per team showing the IA lens phrase from Step 2. This section confirms that IA files
are contextualized and demonstrates C-09 compliance:

```markdown
## Inertia Advocate Lens Summary

| Team | IA Lens Phrase |
|------|----------------|
| [team name] | [lens phrase from resistance profile] |
```

**STEP 6 — AMEND SECTION**

Append to org-chart.md:

```markdown
## AMEND

Run `corps-build --amend` with one of these options:

1. **Regenerate area**: `--area "[area name]"` — rewrites all .craft/roles/ files for the
   named area, including regenerating its resistance profile and IA file from current org.yaml
   context. Areas in this build: [list area names]

2. **Adjust level vocabulary**: `--levels "[old]:[new]"` — replaces level labels in
   org-chart.md and all role files. Levels in use: [list level values]

3. **Change group structure**: `--restructure "[team] > [new-parent]"` — moves a team to a
   new parent group, renames .craft/roles/ subdirectory, and redraws the diagram.
   Current nesting: [list nesting relationships]
```

**STEP 7 — BUILD SUMMARY**

```
BUILD-COMPLETE:
  resistance profiles:    [n of n teams]
  IA files written:       [n of n teams]
  standard role files:    [n]
  specialized role files: [n]
  shared group files:     [n]
  exec office files:      [n]
  total files written:    [n]
  org.yaml slots declared:[n]
  match:                  [YES / NO — if NO, list]
  org-chart.md:           written
  AMEND section:          written
```

Generated by: corps-build — {date}

---

## V-05 — Output Format + Lifecycle Emphasis (Combination)

**Axes**: Output format (prose-section org-chart with embedded tables) + lifecycle emphasis
(phase gates with entry conditions)
**Hypothesis**: Prose section headers create natural completion checkpoints in long outputs,
reducing the risk of a section being silently abbreviated or omitted under output pressure.
Phase gates add a second layer: each gate must appear before the next phase can begin, enforcing
completeness on C-01 (role file count verified at ROLES-GATE) and C-10 (cross-reference check
in its own dedicated phase). Prose headcount sections allow a richer level distribution
narrative (C-06) — a sentence after each table contextualizes the numbers — which pure table
format cannot carry. This combination is strongest on the essential criteria (C-01, C-02, C-03,
C-04) and on C-10. Risk: most verbose variation; the VALIDATE-CROSS-REF phase may be compressed
if the model is near output limits.

---

You are running `corps-build`. Read org.yaml — auto-detect in current directory, or use the
provided path. Work through phases in order. Do not begin a phase until its entry condition is
met and its gate line appears in the output.

---

### PHASE 1 — PARSE AND PLAN

**Entry condition**: org.yaml is accessible.

Read org.yaml. Emit:

```
ORG-PLAN:
  org name: [name]
  groups: [n]  ([list names])
  teams: [n]   ([list names with parent group])
  total role slots: [n]
  role breakdown:
    standard: [n unique types] — [names]
    specialized: [n total entries]
    shared group: [n]
    exec office: [n]
  levels: [list or "not declared"]
  nesting depth: [n]
```

Emit: `PARSE-GATE PASS: [n] role files will be written to .craft/roles/. Proceeding to PHASE 2.`

Halt on parse failure: `PARSE-GATE FAIL: [specific error]. Correct org.yaml and retry.`

---

### PHASE 2 — WRITE ORG-CHART.MD

**Entry condition**: PARSE-GATE PASS in output.

Write `org-chart.md` using prose sections with embedded tables.

**2a. Org Structure**

Open with one sentence describing the org: name, number of groups, number of teams, nesting
depth. Example: "The [org name] organization comprises [n] groups containing [n] teams across
[n] nesting levels."

Then the ASCII hierarchy:

```
[Org Name]
+-- [Group]
    +-- [Team] ([n])
    |   +-- [Sub-group] ([n])
    +-- [Team] ([n])
+-- [Group]
    +-- [Team] ([n])
```

Each team/sub-group shows headcount from org.yaml in parentheses. Group names must match
org.yaml character-for-character.

**2b. Headcount Narrative**

One sentence introducing the table: "The following table shows headcount by area with key
roles and level distribution."

```markdown
## Headcount by Group/Area

| Area       | Headcount | Key Roles            | Levels         |
|------------|-----------|----------------------|----------------|
| [name]     | [n]       | [role names]         | [level labels] |
| **Total**  | **[n]**   |                      |                |
```

After the table, write 2-3 sentences of narrative: name the largest area by headcount, note
any level concentration visible in the table (e.g., "80% of headcount is at L4-L5"), and call
out any team with no declared levels.

**2c. Level Distribution**

```markdown
## Level Distribution

| Level  | Count | % of Org |
|--------|-------|----------|
| [label]| [n]   | [n]%     |
| **Total** | **[n]** | 100% |
```

After the table, one sentence on the seniority profile: what the distribution implies about
the org's career stage or hiring strategy.

**2d. AMEND Section**

```markdown
## AMEND

Run `corps-build --amend` with one of these options:

1. **Regenerate area**: `--area "[area name]"` — rewrites all .craft/roles/ files for the
   named area and updates its org-chart.md headcount row.
   Available areas: [list area names from org.yaml]

2. **Adjust level vocabulary**: `--levels "[old]:[new]"` — replaces level labels in
   org-chart.md Level Distribution and all role file scope fields.
   Levels currently in use: [list level values from org.yaml]

3. **Change group structure**: `--restructure "[team] > [new-parent]"` — moves a team to a
   new parent group, renames its .craft/roles/ path, and redraws the ASCII diagram.
   Current nesting: [describe the parent-child relationships from org.yaml, e.g.
   "Platform > Infrastructure, Platform > Reliability, Growth > Acquisition"]
```

Emit: `CHART-GATE PASS: org-chart.md written with diagram, headcount table (narrative),
level distribution (narrative), and AMEND section. Proceeding to PHASE 3.`

---

### PHASE 3 — WRITE ROLE FILES

**Entry condition**: CHART-GATE PASS in output.

Write role files in this sequence: exec office → shared group → per-team (standard →
specialized → Inertia Advocate).

**File path conventions**:
- Standard/specialized: `.craft/roles/{area-slug}/{role-slug}.md`
- Shared group: `.craft/roles/{group-slug}/{role-slug}.md`
- Exec office: `.craft/roles/exec-office/{role-slug}.md`
- Inertia Advocate: `.craft/roles/{area-slug}/inertia-advocate.md`

**Required fields for every role file** — no placeholder text:
- **orientation**
- **lens**
- **expertise**
- **scope**: exactly one of `standard`, `specialized — [team name]`, `shared — [group name]`,
  `exec office`
- **collaboration pattern**

**Standard vs specialized**: explicit in `scope` field — not derivable only from directory
placement.

**Inertia Advocate per team**:
- `lens` must reference at least one domain-specific term drawn from the team's declared
  context in org.yaml
- `expertise` must name specific systems, processes, or decisions this advocate has run
- No two IA files may share identical `lens` or `expertise` body text

After each team: `TEAM-WRITTEN: [team name] — [n] files (1 IA + [n] std + [n] spec).
Running count: [n].`

Emit: `ROLES-GATE PASS: [n] role files written. Proceeding to PHASE 4.`

---

### PHASE 4 — VALIDATE CROSS-REFERENCE

**Entry condition**: ROLES-GATE PASS in output.

This phase exists specifically to close C-10. Run three checks:

```
CROSS-REF CHECKS:

  C1 — headcount table total == .craft/roles/ file count
       table total (from CHART-GATE): [n]
       files written (from ROLES-GATE): [n]
       result: [MATCH / MISMATCH]
       if MISMATCH: in table not in files: [list]
                    in files not in table: [list]

  C2 — every team has an IA file
       teams in org diagram: [n]
       IA files found: [n]
       result: [MATCH / MISMATCH]
       if MISMATCH: teams missing IA: [list]

  C3 — every area in headcount table has a .craft/roles/{area-slug}/ directory
       table areas: [list]
       directories present: [list]
       result: [MATCH / MISMATCH]
       if MISMATCH: missing dirs: [list] / extra dirs: [list]
```

If all three MATCH: `CROSS-REF GATE PASS: all cross-reference checks pass. Build is consistent.`

If any MISMATCH: `CROSS-REF GATE FAIL: [describe which checks failed]. Build is inconsistent.
Do not treat as complete.`

---

**FINAL SUMMARY**

```
CORPS-BUILD COMPLETE — {date}
  org-chart.md:        written
  .craft/roles/ files: [n] written / [n] declared
  teams with IA:       [n of n]
  cross-reference:     [PASS / FAIL]
  AMEND section:       written with 3 concrete options
  build status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build — {date}
