---
skill: quest-variate
skill_target: corps-build
round: 2
date: 2026-03-16
rubric_version: 2
---

# Variate R2 — corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v2 adds C-11 through C-14. No single R1 variation hit all four — R2 targets that gap.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Lifecycle emphasis: VALIDATE as hard pre-write gate (C-11) | V-01 |
| Output format: table-as-build-contract + mandatory prose (C-13, C-14) | V-02 |
| Phrasing register: output-forward / descriptive (C-14, C-09) | V-03 |
| Resistance profiles + table contract + IA-first ordering (C-09, C-12, C-13) | V-04 |
| All four new aspirational criteria in one integration variation (C-11, C-12, C-13, C-14) | V-05 |

---

## R1 Gap Analysis (rubric v2 lens)

| New Criterion | Best R1 Coverage | Gap |
|---------------|-----------------|-----|
| C-11 pre-write VALIDATE gate | V-03 only | V-01, V-02, V-04, V-05 had no VALIDATE phase |
| C-12 IA-first write ordering | V-01, V-04 | V-02, V-03, V-05 wrote IA last |
| C-13 headcount table as build contract | V-02 only | V-01, V-03, V-04, V-05 built chart after roles |
| C-14 org analytic narrative prose | V-05 only | V-01, V-02, V-03, V-04 had no prose after tables |

No single R1 variation satisfied all four. R2 V-05 is the first to target all four explicitly.

---

## V-01 — Lifecycle Emphasis: VALIDATE as Hard Pre-write Gate

**Axis**: Lifecycle emphasis
**Hypothesis**: Elevating validation to an explicit named phase with 5 typed checks, positioned
as a hard gate — no file can be written until VALIDATE-PASS appears in the output — makes C-11
structurally impossible to elide under compression pressure. The model knows the rule: write
VALIDATE-PASS or halt. This is the cleanest single-criterion implementation of C-11. Secondary
benefit: the IA-first ordering inside the WRITE phase also satisfies C-12.

---

You are running `corps-build`. Read org.yaml — auto-detect in the current directory or use the
path provided.

**Phase sequence**: PARSE → VALIDATE → WRITE → VERIFY. Do not begin a phase until the gate for
the previous phase appears in your output.

---

### PHASE 1 — PARSE

Read org.yaml. Emit:

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
  teams:
    [team name] (group: [parent]) — standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  nesting depth: [n]
  total role slots: [n]
```

Halt on failure: `PARSE-FAIL: [error description]. Provide a valid org.yaml.`

On success: `PARSE-PASS: [n] teams, [n] role slots.`

---

### PHASE 2 — VALIDATE

**Entry condition**: PARSE-PASS in output.
**No files are written during this phase.** Validation must complete and emit VALIDATE-PASS
before any file is written — including org-chart.md.

Run 5 checks. Emit PASS or FAIL for each:

```
VALIDATE:
  [V-1] every team has >= 1 role declared
        PASS  /  FAIL — teams with no roles: [list]

  [V-2] no role name appears in both standard and specialized for the same team
        PASS  /  FAIL — collisions: [team.role list]

  [V-3] no duplicate team names across all groups
        PASS  /  FAIL — duplicates: [list with parent groups]

  [V-4] all level labels use a single vocabulary convention
        (not mixing "L5" with "Senior Engineer" for the same level)
        PASS  /  FAIL — inconsistent pairs: [list]

  [V-5] exec office roles (if declared) are not also assigned to a specific team
        PASS  /  FAIL — [role] appears under both exec-office and [team name]
```

On any FAIL: `VALIDATE-FAIL: [n] structural error(s) found: [list failed check IDs and details].
Correct org.yaml before proceeding. No files have been written.` — HALT.

On all PASS: `VALIDATE-PASS: 5 of 5 checks passed. No structural anomalies detected.
Proceeding to WRITE.`

---

### PHASE 3 — WRITE

**Entry condition**: VALIDATE-PASS in output.

Write all outputs in this sequence:

**3a — Inertia Advocate files (all teams, before any standard or specialized role)**

Write the IA file for every team before writing any standard or specialized roles.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

All five fields — populated from the team's declared responsibilities in org.yaml:
- **orientation**: rational perspective of a senior team member defending the current arrangement;
  names the specific practice, system, or decision defended
- **lens**: domain-specific status quo this advocate monitors; must use at least one term from
  the team's name or declared responsibilities; no generic "stability" language
- **expertise**: specific systems, processes, or decisions this person has built or run;
  must differ from every other team's IA expertise field
- **scope**: `standard — present in all teams`
- **collaboration pattern**: forums (design review, sprint planning, architecture board),
  cadence, and primary counterpart role

No two IA files may share identical `lens` or `expertise` text.

After each IA file: `IA-WRITTEN: [team name] — lens: "[key phrase used]"`
After all IA files: `IA-PHASE-COMPLETE: [n of n] teams covered.`

**3b — org-chart.md**

Write org-chart.md after all IA files, before standard/specialized role files.

Sections in this order:

1. ASCII hierarchy — box-drawing or dash/pipe characters, minimum two nesting levels.
   Group names match org.yaml exactly. Team leaf nodes show headcount in parentheses.

2. Headcount by Group/Area:
   ```markdown
   | Group/Area | Headcount | Key Roles |
   |------------|-----------|-----------|
   | [name]     | [n]       | [names]   |
   | **Total**  | **[n]**   |           |
   ```
   One row per area, Total row, counts sum correctly.

3. Level Distribution — labels from org.yaml, Total matches headcount table Total.
   If no levels declared, infer IC and Management from role names.

4. AMEND section:
   ```markdown
   ## AMEND
   1. --area "[area name]" — regenerate one area (IA + all roles + chart row).
      Areas: [list from org.yaml]
   2. --levels "[old]:[new]" — replace level vocabulary throughout.
      Levels in use: [list]
   3. --restructure "[team] > [new-parent]" — move team, rename directory, redraw diagram.
      Current structure: [parent > child pairs from org.yaml]
   ```

Emit: `CHART-WRITTEN: diagram, headcount table, level distribution, AMEND present.`

**3c — Standard and specialized role files**

Paths:
- `.craft/roles/{area-slug}/{role-slug}.md` — standard and specialized
- `.craft/roles/{group-slug}/{role-slug}.md` — shared group roles
- `.craft/roles/exec-office/{role-slug}.md` — exec office

All five fields, no placeholder text:
- **orientation**, **lens**, **expertise**
- **scope**: exactly one of `standard`, `specialized — [team name]`,
  `shared — [group name]`, `exec office`
- **collaboration pattern**

Standard vs. specialized distinction must be explicit in the `scope` field —
not derivable only from directory path.

After each team: `TEAM-WRITTEN: [team name] — [n] std + [n] spec. Running: [n total].`

WRITE-GATE:
```
WRITE-GATE:
  org.yaml slots: [n]
  files written: [n]
  match: [YES / NO]
  if NO — missing: [list]
  IA files: [n of n] teams
```

---

### PHASE 4 — VERIFY

**Entry condition**: WRITE-GATE YES in output.

Three cross-reference checks:

```
VERIFY:
  [C1] headcount table total == .craft/roles/ file count
       table: [n], files: [n] — MATCH / MISMATCH
       if MISMATCH: in table not in files: [list] / in files not in table: [list]

  [C2] IA file present for every team
       teams: [n], IA files: [n] — MATCH / MISMATCH
       if MISMATCH: teams without IA: [list]

  [C3] every area in headcount table has a .craft/roles/{area}/ directory
       table areas: [list], dirs present: [list] — MATCH / MISMATCH
       if MISMATCH: missing dirs: [list], extra dirs: [list]
```

All MATCH: `VERIFY-PASS: cross-reference consistent. Build complete.`
Any MISMATCH: `VERIFY-FAIL: [details]. Build is not consistent.`

---

**FINAL SUMMARY**

```
CORPS-BUILD — {date}
  validate:      PASS (5/5 checks)
  org-chart.md:  written
  role files:    [n] written / [n] declared
  IA coverage:   [n of n] teams
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build — {date}

---

## V-02 — Output Format: Table-first Build Contract + Narrative Prose

**Axis**: Output format
**Hypothesis**: Writing the headcount table as the literal first artifact produced by the skill —
before any resistance profiles, before any IA file, before any role write — satisfies C-13 by
construction. Any model that emits output in the stated order will produce the table before any
role file. Requiring 2-3 sentences of analytic prose immediately after each table satisfies C-14.
Both criteria are delivered purely through output-format sequencing with no additional lifecycle
phases. The table's TABLE-CLOSED gate establishes an authoritative file count that constrains
every subsequent write.

---

You are running `corps-build`. Read org.yaml — auto-detect in the current directory or use the
provided path.

---

**STEP 1 — PARSE**

Read org.yaml. Emit:

```
PARSE:
  org name: [name]
  groups: [list]
  teams: [n] — [list with parent group]
  total role slots: [n]
  levels declared: [list or "not declared"]
  nesting depth: [n]
```

On failure: `PARSE-ERROR: [description]. Halt.`

---

**STEP 2 — HEADCOUNT TABLE (first artifact, before any files)**

Before writing org-chart.md or any .craft/roles/ file, emit the headcount table.
This table is the **build contract** — the Total row is the authoritative target file count.

```markdown
## Headcount by Group/Area

| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or —]      | [labels or —] |
| **Total**  | **[n]**   |                |                   |        |
```

Rules:
- One row per area/team declared in org.yaml
- Headcount = sum of all role slots declared for that area
- Standard Roles = role types shared across teams (deduplicated list of names)
- Specialized Roles = role types unique to this area
- Levels = all level labels present in this area's roles
- Total row = sum of all area rows

Emit after table:
`TABLE-CLOSED: [n] area rows, [n] total headcount. This is the authoritative file count.
The .craft/roles/ write phase must produce exactly [n] files.`

Then write **2-3 sentences of analytic prose** immediately after TABLE-CLOSED:
- Name the largest area by headcount and state it as a percentage of total
- Note any area that accounts for more than 30% of total headcount
- Call out any area with no declared level vocabulary, or note if level vocabulary is consistent
  across all areas

---

**STEP 3 — LEVEL DISTRIBUTION TABLE**

```markdown
## Level Distribution

| Level  | Count | % of Org |
|--------|-------|----------|
| [label]| [n]   | [n]%     |
| **Total** | **[n]** | 100% |
```

Labels from org.yaml `level:` fields. Total must match TABLE-CLOSED headcount.
If no levels declared, infer IC and Management from role names.

After table, write **one sentence on seniority profile**: what the distribution suggests about
the org's hiring stage or career-level composition.

---

**STEP 4 — ASCII ORG DIAGRAM**

Draw after the tables. Derive structure exclusively from the headcount table rows —
no groups or teams not present in the table.

```
[Org Name]
+-- [Group]
    +-- [Team] ([n])
    |   +-- [Sub-group] ([n])
    +-- [Team] ([n])
```

Each leaf node shows headcount pulled from the table. Group names must match org.yaml exactly.

Emit: `DIAGRAM-DERIVED: all [n] nodes sourced from headcount table rows.`

---

**STEP 5 — AMEND SECTION**

```markdown
## AMEND

Run `corps-build --amend` with one of:

1. **Regenerate area**: `--area "[area name]"` — rewrites all .craft/roles/ files for the
   named area and updates its headcount table row in org-chart.md.
   Available areas: [list from headcount table]

2. **Adjust level vocabulary**: `--levels "[old]:[new]"` — replaces level labels in the
   Level Distribution table and all role file scope fields.
   Levels currently in use: [list from Level Distribution table]

3. **Change group structure**: `--restructure "[team] > [new-parent]"` — moves a team to
   a new parent group, renames the .craft/roles/ path, and redraws the ASCII diagram.
   Current nesting: [list parent > child relationships from headcount table]
```

---

**STEP 6 — WRITE ROLE FILES (derived from table rows)**

Write .craft/roles/ files using the headcount table as the work list — process rows top to
bottom. For each area row:

**Order within each area**: Inertia Advocate first, then standard roles, then specialized.

Paths:
- `.craft/roles/{area-slug}/inertia-advocate.md` — IA
- `.craft/roles/{area-slug}/{role-slug}.md` — standard and specialized
- `.craft/roles/{group-slug}/{role-slug}.md` — shared group
- `.craft/roles/exec-office/{role-slug}.md` — exec office

All five fields, no placeholder text in any file:
- **orientation**
- **lens**: for IA files, must reference at least one term from this team's context in org.yaml
- **expertise**: for IA files, names specific systems, processes, or decisions; no two IA files
  share identical `expertise` text
- **scope**: exactly one of `standard`, `specialized — [team]`, `shared — [group]`, `exec office`
- **collaboration pattern**

Standard vs. specialized: explicit in `scope` field — not inferred from directory placement.
No two IA files may share identical `lens` or `expertise` text.

After each area: `AREA-WRITTEN: [area name] — [n] files. Running total: [n of TABLE-CLOSED [n]].`

---

**STEP 7 — CROSS-REFERENCE**

After all files written:

```
CROSS-REF:
  TABLE-CLOSED declared: [n]
  .craft/roles/ written: [n]
  result: MATCH / MISMATCH
  if MISMATCH: in table not in files: [list]
               in files not in table: [list]

  IA check:   teams [n], IA files [n] — MATCH / MISMATCH
  dir check:  areas in table [list], dirs present [list] — MATCH / MISMATCH
```

All match: `CROSS-REF-PASS: [n] files consistent with table contract.`
Any mismatch: `CROSS-REF-FAIL: [details].`

---

**FINAL SUMMARY**

```
CORPS-BUILD — {date}
  headcount table:   [n] areas, [n] total (contract established)
  ASCII diagram:     written
  narrative prose:   written after headcount table and level distribution
  role files:        [n] written / [n] (TABLE-CLOSED)
  IA coverage:       [n of n] teams
  cross-reference:   PASS / FAIL
  status:            COMPLETE / INCOMPLETE
```

Generated by: corps-build — {date}

---

## V-03 — Phrasing Register: Output-forward / Reviewer Perspective

**Axis**: Phrasing register
**Hypothesis**: An output-forward prompt — describing what `corps-build` produces rather than
issuing step-by-step instructions — reduces mechanical step-following behavior and improves
content quality. For C-14 (narrative prose), showing an example of expected prose is more
effective than instructing "write 2-3 sentences." For C-09 (IA contextualization), showing what
a strong IA lens reads like — with a named counterexample to avoid — is more effective than
prohibiting "no generic text." For C-11, the validation section describes what a good parse
output looks like and what problems halt the build, rather than listing checks as imperatives.

---

You are running `corps-build`. Read org.yaml in the working directory, or use the path provided.

`corps-build` produces two outputs: **org-chart.md** and **typed role files** under
`.craft/roles/`. What follows describes what good output looks like for each.

---

### What org-chart.md contains

A well-formed org-chart.md has four sections, in this order:

**Section 1 — Introductory sentence + ASCII hierarchy**

One sentence opens the file: "[Org Name] organizes [n] teams across [n] groups at [n] nesting
levels." The ASCII tree follows, using `+--` and `|` characters. Group names appear exactly
as they appear in org.yaml — not abbreviated, not reformatted. Every team leaf node shows its
headcount in parentheses pulled from org.yaml.

**Section 2 — Headcount by Group/Area table + analytic prose**

The table has one row per area, a Total row, and columns for headcount, key roles, and level
labels. After the table, 2-3 sentences interpret the numbers. These sentences are specific:
they name an actual area, cite an actual count, and make an observation the table rows alone
do not convey.

Strong analytic prose (produce this):
> "Platform Engineering carries 9 of 22 total headcount — the largest area by nearly 2:1 over
> the next area. All five Platform teams declare IC levels, but no management level vocabulary
> appears in org.yaml, suggesting the org is pre-leveling its management layer."

Weak analytic prose (do not produce this):
> "The org has several teams with different headcount. Level distribution is shown below."

**Section 3 — Level Distribution table + seniority sentence**

A table with level labels, headcount per level, and percentage of total. Labels drawn directly
from org.yaml `level:` fields; if none declared, infer IC and Management from role names.
After the table, one sentence characterizes the seniority profile — what the distribution implies
about the org's hiring stage or career-level composition.

**Section 4 — AMEND options**

Three options the user can invoke with `corps-build --amend`:

1. `--area "[name]"` — regenerate all role files for one area and update its chart rows.
   The list of available areas is named here, drawn from the headcount table.
2. `--levels "[old]:[new]"` — replace level labels throughout chart and role files.
   The current levels in use are listed.
3. `--restructure "[team] > [new-parent]"` — move a team to a new parent, rename its
   `.craft/roles/` subdirectory, redraw the diagram.
   The current parent-child relationships are listed.

---

### What .craft/roles/ files contain

Each file has exactly five typed fields. No field is empty, contains "TBD," or contains generic
boilerplate that would read identically in a different team's file.

- **orientation** — the perspective this role holds when arriving at any decision: what problem
  they are always solving for, stated from their point of view

- **lens** — the specific slice of the system or product this role attends to; for Inertia
  Advocate files, this field must include at least one term drawn from this team's declared
  responsibilities in org.yaml

- **expertise** — what this role knows that others at the table do not; for Inertia Advocate
  files, this names specific systems, code paths, or operational processes they have run or
  authored

- **scope** — exactly one of: `standard` (role present in all teams), `specialized — [team name]`
  (role unique to this team), `shared — [group name]` (group-level role), `exec office`;
  this field must distinguish standard from specialized explicitly — not by directory path alone

- **collaboration pattern** — who this role works with most directly, in what forums, and on what
  triggers

---

### The Inertia Advocate role

Every team has an Inertia Advocate file. No team is exempt.

An Inertia Advocate file reads like a portrait of a specific person, not a generic role. The
`lens` field opens with a phrase that anchors this advocate to this team's domain. The
`expertise` field names specific systems, deployment pipelines, schema decisions, or operational
procedures this person has authored or maintained. Two IA files for different teams should read
as two different people defending two different things.

Strong Inertia Advocate `lens`:
> "Query optimizer regression detection — this advocate monitors execution plan changes that
> reduce throughput on the five core customer queries, the ones rewritten during the v3 schema
> migration."

Weak Inertia Advocate `lens` (do not produce this):
> "Operational stability and institutional knowledge about existing systems."

---

### Before writing: structural checks

Before writing any file, check org.yaml for structural problems and report them:

- Teams with no declared roles
- Duplicate team names across groups
- Role names that appear in both standard and specialized for the same team
- Level vocabulary that mixes numeric and string labels for the same level concept

If any problem is found, list each in a `VALIDATE:` block and halt — do not write files.
If none are found, emit `VALIDATE: no structural anomalies. Proceeding.`

---

### After writing: build verification

```
CORPS-BUILD — {date}
  parse:      org name [name], [n] teams, [n] role slots
  validate:   [anomalies found: list / "none — PASS"]
  org-chart:  written (diagram + headcount table + prose + level dist + AMEND)
  role files: [n] written / [n] declared — MATCH / MISMATCH
              if MISMATCH: missing: [list]
  IA files:   [n of n] teams
  scope dist: [n] standard, [n] specialized, [n] shared, [n] exec-office
  cross-ref:  headcount table total [n] == file count [n] — MATCH / MISMATCH
  status:     COMPLETE / INCOMPLETE
```

Generated by: corps-build — {date}

---

## V-04 — Resistance Profiles + Table Contract + IA-first Ordering

**Axes**: Inertia framing (resistance profiles before any write) + Output format
(table as build contract) + Role sequence (IA-first phase)
**Hypothesis**: The headcount table and resistance profiles are sequenced compatibly in this
order: build the table first (establishing file count contract, C-13), then generate resistance
profiles (locking IA content plan before any file write, C-09), then write all IA files in a
dedicated phase before standard/specialized roles (C-12). This sequence satisfies three new
aspirational criteria in a single linear flow while preserving R1-V-04's strongest mechanism
for IA contextualization. The table gives the build contract; the profiles give the IA content
plan; the IA-first phase makes omission impossible by construction.

---

You are running `corps-build`. Read org.yaml — auto-detect in the current directory or use the
provided path.

Execute these steps in order. Each gate must appear in the output before the next step begins.

---

**STEP 1 — PARSE**

```
PARSE:
  org name: [name]
  groups: [list]
  teams:
    [team name] (group: [parent]) — standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS.` or `PARSE-ERROR: [description]. Halt.`

---

**STEP 2 — HEADCOUNT TABLE (build contract, first artifact)**

**Before writing any files or resistance profiles**, emit the headcount table.
This table is the build contract for this run — the Total row establishes the authoritative
.craft/roles/ file count.

```markdown
## Headcount by Group/Area

| Area/Group | Headcount | Standard Roles | Specialized Roles |
|------------|-----------|----------------|-------------------|
| [name]     | [n]       | [role names]   | [names or —]      |
| **Total**  | **[n]**   |                |                   |
```

Rules: one row per area, headcount = sum of role slots for that area, Total = sum of area rows.

Emit: `TABLE-CLOSED: [n] areas, [n] total headcount. Build contract established.
Role file generation must produce exactly [n] .craft/roles/ files.`

After TABLE-CLOSED, write **2-3 sentences of analytic prose**:
- Name the largest area and its share of total headcount
- Note any concentration or imbalance visible in the table
- Flag any area with no declared level vocabulary

---

**STEP 3 — RESISTANCE PROFILES**

After the table is closed and before writing any files, generate a resistance profile for each
team. A resistance profile names the specific practice, system, or decision a senior member of
this team would rationally defend.

```
RESISTANCE PROFILES:

[Team Name]
  Status quo defended: [specific system, code path, or operational process — not "stability"]
  Credibility source: [what this person has built or maintained here]
  Failure mode seen: [the specific bad outcome that shaped their caution]
  IA lens phrase: [one phrase, 5-8 words, anchoring this team's IA lens field]
```

Rules:
- Every team from the headcount table gets a profile
- "IA lens phrase" must be distinct across all teams and draw on the team's declared
  responsibilities in org.yaml; no generic "they value stability" or equivalent phrases
- Name the specific system or decision

Emit after all profiles: `RESISTANCE-COMPLETE: [n] teams profiled.
IA lens phrases: [list one per team, one line each].`

Scan for duplicates: if any two phrases are identical, emit `LENS-COLLISION: [team A] and
[team B] share "[phrase]". Revise one before proceeding.`

---

**STEP 4 — WRITE ALL IA FILES (before any other role)**

For each team, write the Inertia Advocate file using its resistance profile from Step 3.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields, populated from the resistance profile:
- **orientation**: from "Status quo defended" — the rational perspective, not a cartoon
  of stubbornness; names the specific concern
- **lens**: opens with the IA lens phrase from Step 3, expanded in 2-3 sentences naming the
  domain-specific status quo this advocate monitors
- **expertise**: from "Credibility source" — names specific systems, schemas, or processes;
  must differ from every other team's IA expertise entry
- **scope**: `standard — present in all teams`
- **collaboration pattern**: surfaces resistance in design reviews, sprint planning, and
  architecture discussions; primary counterpart is the role most likely to propose structural
  changes in this team; escalates to group lead when velocity pressure overrides quality threshold

No two IA files may share identical `lens` or `expertise` text.

After each file: `IA-WRITTEN: [team name] — lens: "[lens phrase from Step 3]"`
After all files: `IA-PHASE-COMPLETE: [n of n] teams. All IA files written before standard
or specialized roles.`

---

**STEP 5 — WRITE REMAINING ROLE FILES**

For each team (in org.yaml declaration order), after its IA file is already written:

**5a. Standard role files** (shared across all teams):
Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, `scope: standard — present in all teams`

**5b. Specialized role files** (unique to this team):
Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, `scope: specialized — [team name]`

**5c. Shared group roles** (if declared at group level):
Path: `.craft/roles/{group-slug}/{role-slug}.md`
`scope: shared — group: [group name]`

**5d. Exec office roles** (if declared):
Path: `.craft/roles/exec-office/{role-slug}.md`
`scope: exec office`

Standard vs. specialized distinction must be explicit in the `scope` field — not derivable from
directory path alone. No placeholder text in any field.

After each team: `TEAM-COMPLETE: [team name] — [n] std + [n] spec.`

---

**STEP 6 — ORG-CHART.MD (write after all role files)**

Write org-chart.md. Sections in order:

1. **ASCII hierarchy** — box-drawing or dash/pipe, minimum two nesting levels. Group names
   match org.yaml exactly. Team leaf nodes show headcount.

2. **Headcount table** from Step 2 (transcribe here)

3. **Analytic prose** from Step 2 (transcribe here)

4. **Level Distribution table** — labels from org.yaml, Total matches headcount Total.
   Follow with one sentence on seniority profile.

5. **Inertia Advocate Lens Summary**:
   ```markdown
   | Team | IA Lens Phrase |
   |------|----------------|
   | [team name] | [lens phrase from Step 3] |
   ```

6. **AMEND section**:
   ```markdown
   ## AMEND
   1. --area "[name]" — regenerate role files + resistance profile + IA for this area.
      Areas: [list from headcount table]
   2. --levels "[old]:[new]" — replace level labels. Levels in use: [list]
   3. --restructure "[team] > [new-parent]" — move team, rename directory, redraw diagram.
      Current structure: [parent > child pairs]
   ```

---

**STEP 7 — BUILD SUMMARY**

```
BUILD-COMPLETE — {date}
  headcount table:        [n] areas, [n] total (contract established pre-write)
  resistance profiles:    [n of n] teams
  IA files:               [n of n] teams (written before standard/specialized)
  standard role files:    [n]
  specialized role files: [n]
  shared group files:     [n]
  exec office files:      [n]
  total files:            [n]
  org.yaml declared:      [n]
  match:                  [YES / NO — if NO: [list]]
  headcount contract:     table [n] == files [n] — [YES / NO]
  org-chart.md:           written
  status:                 COMPLETE / INCOMPLETE
```

Generated by: corps-build — {date}

---

## V-05 — Full Integration: All Four New Aspirational Criteria

**Axes**: Lifecycle emphasis (VALIDATE gate, C-11) + Output format (table contract, C-13;
narrative prose, C-14) + Role sequence (IA-first phase, C-12)
**Hypothesis**: A single variation can target all four new aspirational criteria without
exceeding reasonable output length if each criterion maps to the smallest possible dedicated
mechanism: (1) C-11 via a compact 4-check VALIDATE phase before any writes; (2) C-13 via
headcount table as the first phase output; (3) C-14 via a required 2-3 sentence prose block
immediately after each table; (4) C-12 via an explicit IA-PHASE that names and completes all
IA files before the standard-role phase begins. This is the integration variation — the only
R2 candidate targeting the full aspirational set (C-09 through C-14).

---

You are running `corps-build`. Read org.yaml — auto-detect in the current directory or use the
provided path.

Six phases. Do not begin a phase until its gate appears in the output.

---

### PHASE 1 — PARSE

Read org.yaml. Emit:

```
PARSE:
  org name: [name]
  groups: [list]
  teams:
    [team] (group: [parent]) — std: [names], spec: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels: [list or "not declared"]
  depth: [n]
  total slots: [n]
```

`PARSE-PASS: [n] teams, [n] slots.`
or `PARSE-FAIL: [error]. Halt.`

---

### PHASE 2 — VALIDATE

**Entry**: PARSE-PASS.
**No files written during this phase.**

Run 4 checks:

```
VALIDATE:
  [V-1] every team has >= 1 role           PASS / FAIL — teams with no roles: [list]
  [V-2] no standard/specialized collision  PASS / FAIL — [team.role collisions]
  [V-3] no duplicate team names            PASS / FAIL — duplicates: [list]
  [V-4] level vocabulary is consistent     PASS / FAIL — inconsistent label pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. No structural anomalies. Proceeding to PHASE 3.`
or `VALIDATE-FAIL: [n] error(s): [details]. No files written. Halt.`

---

### PHASE 3 — BUILD CONTRACT (headcount table + prose)

**Entry**: VALIDATE-PASS.

The headcount table is the first artifact produced. It is the build contract —
the Total row is the authoritative .craft/roles/ file count for this run.

```markdown
## Headcount by Group/Area

| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or —]      | [labels or —] |
| **Total**  | **[n]**   |                |                   |        |
```

Emit: `TABLE-CLOSED: [n] total headcount. File generation must produce exactly [n]
.craft/roles/ files.`

Then write **2-3 sentences of analytic prose** (mandatory):
- Sentence 1: name the largest area and its headcount as a percentage of total
- Sentence 2: name the dominant level label, or note that most teams have no declared levels
- Sentence 3: any structural observation the table numbers alone do not convey

`CONTRACT-GATE: headcount table written with analytic prose. Proceeding to PHASE 4.`

---

### PHASE 4 — WRITE ROLE FILES

**Entry**: CONTRACT-GATE.

Write all .craft/roles/ files in this sequence:

**4a — Inertia Advocate phase (all teams, before any other role)**

Write the IA file for every team before writing any standard or specialized role.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields:
- **orientation**: rational perspective of a senior team member defending the current
  arrangement; names the specific practice, system, or decision defended — not a generic
  stance toward stability
- **lens**: opens with a domain-specific phrase tied to this team's responsibilities in
  org.yaml; must differ from every other team's IA lens; no "stability" or "institutional
  knowledge" boilerplate
- **expertise**: names specific systems, processes, or decisions this person has run;
  must differ from every other team's IA expertise field
- **scope**: `standard — present in all teams`
- **collaboration pattern**: forums (design review, sprint planning, architecture board),
  cadence, primary counterpart role

No two IA files may share identical `lens` or `expertise` text.

After each file: `IA-WRITTEN: [team] — lens: "[opening phrase]"`
After all IA files: `IA-PHASE-COMPLETE: [n of n] teams. All IA files written.
Standard and specialized role files may now be written.`

**4b — Standard role files (all teams)**

Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, no placeholder text, `scope: standard — present in all teams`.

**4c — Specialized role files (all teams)**

Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, no placeholder text, `scope: specialized — [team name]`.

**4d — Shared group roles** (if declared)

Path: `.craft/roles/{group-slug}/{role-slug}.md`, `scope: shared — group: [name]`

**4e — Exec office roles** (if declared)

Path: `.craft/roles/exec-office/{role-slug}.md`, `scope: exec office`

Standard vs. specialized must be explicit in `scope` field — not derivable from
directory path alone. No placeholder text in any field.

After each team: `TEAM-WRITTEN: [team] — 1 IA + [n] std + [n] spec.`

`ROLES-GATE: [n] written / [n] declared (TABLE-CLOSED). MATCH / MISMATCH.`
If MISMATCH: `ROLES-GATE-FAIL: missing: [list]. Build incomplete.` — Halt.

---

### PHASE 5 — WRITE ORG-CHART.MD

**Entry**: ROLES-GATE MATCH.

org-chart.md sections in this order:

1. **ASCII hierarchy** — prepend before the headcount table. Box-drawing characters,
   minimum two levels. Group names exactly as in org.yaml. Team leaf nodes show headcount.

2. **Headcount table** from Phase 3 (transcribe)

3. **Analytic prose** from Phase 3 (transcribe — same sentences)

4. **Level Distribution**:
   ```markdown
   ## Level Distribution
   | Level | Count | % of Org |
   |-------|-------|----------|
   | [label] | [n] | [n]% |
   | **Total** | **[n]** | 100% |
   ```
   After table: one sentence on seniority profile.

5. **AMEND section**:
   ```markdown
   ## AMEND
   1. --area "[name]" — regenerate area (all roles + IA). Areas: [list from headcount table]
   2. --levels "[old]:[new]" — replace levels. Levels in use: [list]
   3. --restructure "[team] > [new-parent]" — move team. Current nesting:
      [parent > child pairs, e.g. "Platform > Infrastructure, Platform > Reliability"]
   ```

`CHART-GATE: org-chart.md written with all sections. Proceeding to PHASE 6.`

---

### PHASE 6 — CROSS-REFERENCE

**Entry**: CHART-GATE.

```
CROSS-REF:
  C1 — TABLE-CLOSED contract vs .craft/roles/ file count
       contract: [TABLE-CLOSED n], files written: [ROLES-GATE n]
       result: MATCH / MISMATCH
       if MISMATCH: in contract not in files: [list]
                    in files not in contract: [list]

  C2 — every team has an IA file
       teams: [n], IA files: [n] — MATCH / MISMATCH
       if MISMATCH: teams missing IA: [list]

  C3 — every area in headcount table has a .craft/roles/{area}/ directory
       table areas: [list], directories present: [list] — MATCH / MISMATCH
       if MISMATCH: missing dirs: [list] / extra dirs: [list]
```

All MATCH: `CROSS-REF-PASS: build consistent with contract.`
Any MISMATCH: `CROSS-REF-FAIL: [details]. Build is not consistent.`

---

**FINAL SUMMARY**

```
CORPS-BUILD — {date}
  validate:        PASS (4/4 checks) — no files written before validation
  headcount table: written pre-roles (contract: [n] files)
  narrative prose: written after headcount + level distribution tables
  IA phase:        [n of n] teams — completed before standard/specialized roles
  role files:      [n] written / [n] declared — MATCH / MISMATCH
  cross-ref:       PASS / FAIL
  status:          COMPLETE / INCOMPLETE
```

Generated by: corps-build — {date}

---

## Variation Summary

| Variation | Axis | Key Hypothesis | New Criteria Targeted | R1 Predecessor |
|-----------|------|----------------|----------------------|----------------|
| **V-01** | Lifecycle: VALIDATE as hard pre-write gate | VALIDATE-PASS as gate means C-11 cannot be elided; IA-first inside WRITE catches C-12 | C-11, C-12 | Strengthens V-03(R1) |
| **V-02** | Output format: table-contract + prose | Table as first artifact = C-13 by construction; prose after each table = C-14 | C-13, C-14 | Strengthens V-02(R1) |
| **V-03** | Phrasing register: output-forward | Showing expected output (with good/weak examples) guides C-14 prose quality and C-09 IA depth | C-14, C-09 | New axis — no R1 precedent |
| **V-04** | Resistance profiles + table contract + IA-first | Table locks count, profiles lock IA content, IA-phase locks ordering — three criteria in one linear sequence | C-09, C-12, C-13, C-14 | Combines V-04(R1) + V-02(R1) |
| **V-05** | Full integration — all four new criteria | Minimal mechanisms for each: VALIDATE(C-11) + table-first(C-13) + prose(C-14) + IA-phase(C-12) | C-11, C-12, C-13, C-14 | Synthesizes all R1 patterns |

**Single-axis axes used**: lifecycle emphasis (V-01), output format (V-02), phrasing register (V-03).

**Combination axes**: V-04 = inertia framing + output format + role sequence; V-05 = lifecycle + output format + role sequence.

**Predicted rubric v2 sensitivity**:
- V-01 is the strongest single bet for C-11 (VALIDATE is the structural centerpiece, not an afterthought)
- V-02 is the strongest single bet for C-13 (table literally first) and C-14 (prose required by format)
- V-03 is the only variation that shows example prose, which may produce the best C-14 quality
- V-04 is strongest on C-09 (resistance profiles) + C-12 (IA-first) + C-13 (table contract) simultaneously
- V-05 is the only variation targeting C-11 + C-12 + C-13 + C-14 together — highest ceiling, highest verbosity risk
