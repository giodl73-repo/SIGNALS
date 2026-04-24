---
skill: quest-variate
skill_target: corps-build
round: 2
date: 2026-03-17
rubric_version: 1
r1_file: corps-build-variate-R1-2026-03-17.md
---

# Variate R2 — corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 2. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R1 covered: role sequence, output format (table-first), phrasing register,
inertia framing (resistance profile phase), lifecycle emphasis (phase gates).

R2 targets three axes not yet tested:
- Scaffold-first: write org-chart.md skeleton before any role files
- Coverage audit loop: explicit self-audit after all files written, before org-chart
- Schema-as-contract: define role file schema upfront by field ID, reference IDs throughout

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Scaffold-first (org-chart skeleton committed before role files) | V-01, V-04, V-05 |
| Coverage audit loop (self-audit after write, before org-chart) | V-02, V-04, V-05 |
| Schema-as-contract (field IDs F-1..F-5 defined once, referenced throughout) | V-03, V-05 |
| Resistance profile (from R1 V-04) | V-05 |

---

## V-01 — Scaffold-First: Commit Structure Before Writing

**Axis**: Scaffold-first
**Hypothesis**: Writing org-chart.md as a structural skeleton (with placeholder headcounts
and the full ASCII hierarchy) before writing any role files forces the model to commit to
the exact directory structure implied by org.yaml. Because the skeleton is derived directly
from org.yaml and written before any files exist, structural drift (C-04) is caught at the
draft stage rather than the review stage. The skeleton's team list also serves as a checklist:
every team in the diagram must receive role files before the skeleton can be updated to final
form. Strongest on C-02, C-04, and C-10 (cross-reference integrity).

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

**STEP 1 — PARSE**

Read `org.yaml`. Emit a parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [e.g., Division > Team, or Division > Group > Sub-team]
  teams: [list all team names with full parent path]
  standard roles per team: [role names by team]
  specialized roles per team: [role names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE org-chart.md SKELETON**

Write `org-chart.md` now, before any role files exist. This is the structural commitment.

Write two sections:

**Section A — ASCII Hierarchy**

Draw the full org tree from `org.yaml`. Use `+--` and `|`. All names verbatim from
`org.yaml`. At least two nesting levels must be visible.

Example:
```
[Org Name]
+-- [Division A]
|   +-- [Team 1]
|   +-- [Team 2]
+-- [Division B]
    +-- [Team 3]
```

**Section B — Pending Headcount Table (placeholder)**

Insert a table with one row per area and a PENDING marker in every count cell.
This table will be updated in Step 4.

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area from org.yaml] | PENDING | PENDING | PENDING | PENDING | [levels or "not declared"] |
| **Total** | PENDING | PENDING | PENDING | PENDING | |

Add a note: `(headcount table will be updated once role files are written — Step 4)`

The skeleton is now the contract. The directory structure of `.roles/` must mirror
this skeleton exactly. Any area in the diagram must exist as a subdirectory; any area not
in the diagram must not exist.

**STEP 3 — WRITE ROLE FILES**

For each team listed in the skeleton (Section A, in order top to bottom), write all role
files before moving to the next team.

Per team, write in this sequence:
1. All standard roles
2. All specialized roles
3. Inertia Advocate (mandatory — one per team, no exceptions)

Path: `.roles/{area-slug}/{role-slug}.md`

Frontmatter required for each file:
```yaml
role-type: [standard | specialized | inertia-advocate]
area: [area-slug matching the skeleton]
```

Five required fields — every file, every field, non-empty:

- **orientation**: what this role is oriented toward within this specific team's declared
  responsibilities. Must be grounded in this team's domain, not a generic job description.
- **lens**: the specific domain, system, or practice through which this role evaluates
  proposals. Name the system. "Technical" is not a lens.
- **expertise**: what makes this person's opinion credible — systems built, decisions owned,
  failures survived in this team's domain. No generic labels.
- **scope**: what this role can approve, block, recommend, or escalate within this team.
- **collaboration-pattern**: how this role works with the other roles on this same team.

The Inertia Advocate's `lens` and `expertise` must be drawn from this specific team's
declared domain. An Inertia Advocate who could belong to any team has failed this field.

After all teams: write shared-group roles to `.roles/shared/` and exec-office roles
to `.roles/exec-office/` with `role-type: shared-group` and `role-type: exec-office`
respectively. Skip if not declared in `org.yaml`.

**STEP 4 — FINALIZE org-chart.md**

Return to `org-chart.md` and replace all PENDING cells with actual counts derived from
the role files just written.

Updated headcount table format:

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | n | n | 1 | n | [labels from org.yaml or "not declared"] |
| exec-office | — | — | — | n | — |
| shared | — | — | — | n | — |
| **Total** | n | n | n | **[sum]** | |

Verify: the Total in this table must equal the count of files written in Step 3. If they
do not match, identify the discrepancy before writing the AMEND section.

Add a coverage notes section: one line per area confirming which role categories were
generated and noting any absent by declaration.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — rewrite all role files for that area;
   update org-chart.md headcount table.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: move [team name] from [current parent] to [new parent group];
   update skeleton and role file paths.
```

---

## V-02 — Coverage Audit Loop: Self-Audit After Write, Before org-chart

**Axis**: Coverage audit loop
**Hypothesis**: An explicit self-audit pass after all role files are written — but before
org-chart.md is started — forces the model to verify every essential criterion programmatically
before producing the chart. Because the audit names the specific failure modes (missing files,
empty fields, missing IA per team, directory mismatch), it catches gaps that would otherwise
propagate silently into the headcount table. The audit output is visible to the reader,
creating an accountability checkpoint. Strongest on C-01, C-03, C-04, and C-05.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

**PARSE**

Read `org.yaml`. Emit a parse manifest before writing any files:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth description]
  teams: [list with parent path]
  standard roles per team: [role names by team]
  specialized roles per team: [role names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

Per team, in sequence:
1. Standard roles
2. Specialized roles
3. Inertia Advocate (one per team — mandatory, no exceptions)

Path: `.roles/{area-slug}/{role-slug}.md`

Every file requires frontmatter with `role-type` and `area`, plus five required fields
with substantive (non-empty, non-"TBD") body text:

```
orientation: [team-specific perspective — grounded in this team's declared responsibilities]
lens:         [specific domain, system, or practice — named, not generic]
expertise:    [concrete systems, decisions, or past work owned in this domain]
scope:        [approval/block/escalation reach within this team]
collaboration-pattern: [how this role interacts with other roles on this team]
```

For the Inertia Advocate, `lens` and `expertise` must reference terminology specific to
this team's declared domain. Identical IA content across two teams is a defect.

After all teams: write shared-group roles (`.roles/shared/`) and exec-office roles
(`.roles/exec-office/`) if declared in `org.yaml`.

**COVERAGE AUDIT**

Before writing org-chart.md, run this audit. Emit all results. Do not skip any check.

```
COVERAGE-AUDIT:

  [A] Role file count
      Expected: [total declared role slots from parse]
      Actual:   [count of .roles/ files written, excluding index/README]
      Status:   [PASS | FAIL — list missing or phantom files]

  [B] Inertia Advocate per team
      For each team:
        [team name]: [PRESENT at .roles/{area}/inertia-advocate.md | MISSING]
      Status:   [PASS | FAIL]

  [C] Directory fidelity
      For each area in org.yaml:
        [area name]: [directory exists as .roles/{area-slug}/ | MISSING]
      Extra directories not in org.yaml: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Required field completeness
      Spot-check: verify five required fields are non-empty in:
        - first file written
        - last file written
        - one Inertia Advocate file (any team)
      Status:   [PASS | FAIL — name any file with empty or TBD fields]

  AUDIT RESULT: [PASS | FAIL]
  Failures to resolve before writing org-chart.md: [list or "none"]
```

If any audit check is FAIL, resolve the gap before proceeding. Do not write org-chart.md
until AUDIT RESULT is PASS.

**WRITE org-chart.md**

Write `org-chart.md` after the audit passes. Three sections:

**Section 1 — ASCII Hierarchy**

Use `+--` and `|`. All names verbatim from `org.yaml`. At least two nesting levels visible.

**Section 2 — Headcount Table**

| Area | Headcount | Standard | Specialized | Inertia-Adv | Levels |
|------|-----------|----------|-------------|-------------|--------|
| [area] | [n] | [n] | [n] | [n] | [labels or "not declared"] |
| **Total** | [sum] | | | | |

Total must match audit check [A] Actual count.

**Section 3 — Coverage Notes**

One line per area: which role categories were generated; which were absent by declaration.

**AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — rerun write + audit for that area only.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: move [team name] under [new parent group]; update paths and chart.
```

---

## V-03 — Schema-as-Contract: Field IDs as Reference Contract

**Axis**: Schema-as-contract
**Hypothesis**: Defining the role file schema once at the top of the prompt as a numbered
field contract (F-1 through F-5) and then referencing those IDs in every subsequent
instruction reduces the cognitive distance between the schema definition and its application.
When the instruction says "populate F-1 through F-5" rather than restating all five field
names in full each time, the model has a single authoritative source for field requirements.
This should reduce partial-field omissions (C-05 failures) by making the complete field
set a first-class reference object rather than an inline list that may be skimmed. Strongest
on C-05 and C-07.

---

You are running `corps-build`. Read `org.yaml` from the path provided or auto-detect it.

==== ROLE FILE SCHEMA (reference contract) ====

Every `.roles/` file must contain all five schema fields. Reference them as F-1..F-5.

| ID  | Field name            | Content requirement |
|-----|-----------------------|---------------------|
| F-1 | orientation           | Team-specific perspective grounded in this team's declared responsibilities. Not a job title. A statement of what this person is oriented toward in this specific context. |
| F-2 | lens                  | The domain, system, or practice through which this role evaluates proposals. Must name the specific thing. "Technical perspective" fails this field. "Schema migration cost at >10M rows" passes. |
| F-3 | expertise             | Concrete systems built, decisions owned, or failures survived in this domain. No generic labels like "deep expertise in engineering." Name the actual systems or decisions. |
| F-4 | scope                 | The reach of this role's authority: what they approve, block, recommend, or escalate, and where that authority ends. |
| F-5 | collaboration-pattern | How this role works with other roles on this team: who they lean on, who they push back on, what productive friction looks like here. |

Frontmatter required on every file:
- `role-type`: one of `standard | specialized | inertia-advocate | shared-group | exec-office`
- `area`: the area slug matching org.yaml

"TBD", empty bodies, or placeholder text fails the schema contract on any field.

==== END SCHEMA ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth]
  teams: [list with parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE STANDARD ROLES**

For each team in declaration order, write all standard roles.
Path: `.roles/{area-slug}/{role-slug}.md`
Frontmatter: `role-type: standard`, `area: {area-slug}`

Populate F-1 through F-5 (schema above). Every field must satisfy its content requirement.

**STEP 3 — WRITE SPECIALIZED ROLES**

For each team in declaration order, write all specialized roles.
Path: `.roles/{area-slug}/{role-slug}.md`
Frontmatter: `role-type: specialized`, `area: {area-slug}`

Populate F-1 through F-5. For specialized roles, F-2 (lens) and F-3 (expertise) must
name domain-specific systems or practices that distinguish this role from the standard
roles on the same team. Generic F-2 content that could apply to any role on any team
fails the specialized designation.

**STEP 4 — WRITE INERTIA ADVOCATES**

For each team in declaration order, write the Inertia Advocate file.
Path: `.roles/{area-slug}/inertia-advocate.md`
Frontmatter: `role-type: inertia-advocate`, `area: {area-slug}`

Populate F-1 through F-5 with this additional constraint: this role represents principled
resistance to the proposed change. The content must be grounded in this specific team's
declared domain.

- F-1 must express why a senior member of this team would rationally resist.
- F-2 must name the status-quo system or practice this advocate is protecting, using
  terminology from this team's declared responsibilities.
- F-3 must identify what makes their skepticism credible in this specific domain.

No two Inertia Advocate files across different teams may share identical F-2 or F-3 body
text. If reuse is detected, differentiate before proceeding.

**STEP 5 — WRITE SHARED-GROUP AND EXEC-OFFICE ROLES**

Write shared-group roles to `.roles/shared/` with `role-type: shared-group`.
Write exec-office roles to `.roles/exec-office/` with `role-type: exec-office`.
Populate F-1 through F-5 for all. Scope (F-4) must reference cross-team or cross-division
authority, not a single team's domain. Skip if not declared in `org.yaml`.

**STEP 6 — WRITE org-chart.md**

Write `org-chart.md` with three sections:

**Section A — ASCII Hierarchy**
Use `+--` and `|`. All names verbatim from `org.yaml`. Minimum two nesting levels.

**Section B — Headcount Table**

| Area | Headcount | Standard | Specialized | Inertia-Adv | Levels |
|------|-----------|----------|-------------|-------------|--------|
| [area] | [n] | [n] | [n] | 1 per team | [from org.yaml or "not declared"] |
| **Total** | [sum] | [sum] | [sum] | [n teams] | |

Count from actual files written, not from org.yaml declaration.

**Section C — Coverage Notes**
One line per area: role categories generated, any absent by declaration.

**STEP 7 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — re-run steps 2-4 for that area; all
   regenerated files must satisfy F-1..F-5 schema.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: restructure [team name] from [current parent] to [new parent].
```

---

## V-04 — Combination: Scaffold-First + Coverage Audit Loop

**Axis**: Scaffold-first + Coverage audit loop
**Hypothesis**: The scaffold commits the expected directory structure before any file is
written; the audit verifies the actual file set matches that structure after writing.
Together they close the loop: the scaffold is the contract, the audit is the enforcement.
Without the scaffold, the audit catches drift after the fact. Without the audit, the
scaffold commitment may not be checked. Together, they should produce the highest structural
fidelity (C-04, C-10) while also catching field-level omissions (C-01, C-05). The audit
runs against the scaffold's team list as its checklist, making the two steps mutually
reinforcing. Expected to be the strongest variation on the structural criteria cluster.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

**STEP 1 — PARSE**

Read `org.yaml`. Emit a parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth — e.g., Division > Team]
  teams: [list all team names with full parent path]
  standard roles per team: [role names by team]
  specialized roles per team: [role names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE org-chart.md SKELETON (structural commitment)**

Write the skeleton of `org-chart.md` now. This is the structural contract for Step 3.

**Skeleton Section 1 — ASCII Hierarchy**

Draw the complete org tree from `org.yaml`. Use `+--` and `|`. All names verbatim.
Minimum two nesting levels. Every team declared in `org.yaml` must appear here.

**Skeleton Section 2 — Team Checklist**

Add a checklist derived from the ASCII hierarchy. This will be checked in Step 4.

```
TEAM CHECKLIST (to be verified in coverage audit):
[ ] [team name] — [n] role files expected at .roles/{area-slug}/
[ ] [team name] — [n] role files expected at .roles/{area-slug}/
...
TOTAL EXPECTED: [n] files (sum of all role slots from parse manifest)
```

**Skeleton Section 3 — Pending Headcount Table**

Insert a table with PENDING cells to be filled in Step 5:

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | PENDING | PENDING | 1 | PENDING | [levels or "not declared"] |
| **Total** | PENDING | PENDING | PENDING | PENDING | |

Note: `Inertia-Adv` column prefilled with 1 per team as a constraint, not an estimate.

**STEP 3 — WRITE ROLE FILES**

Using the team checklist from the skeleton as the iteration order, write role files for
each team before moving to the next.

Per team sequence:
1. Standard roles (path: `.roles/{area-slug}/{role-slug}.md`, `role-type: standard`)
2. Specialized roles (same path pattern, `role-type: specialized`)
3. Inertia Advocate (`role-type: inertia-advocate`) — mandatory, one per team

Every file must contain five required fields with non-empty, non-"TBD" body text:

- **orientation**: team-specific perspective grounded in this team's declared responsibilities
- **lens**: specific domain, system, or practice — named, not generic
- **expertise**: concrete systems, decisions, or work owned in this domain
- **scope**: approval, block, recommendation, or escalation reach within this team
- **collaboration-pattern**: how this role interacts with other roles on this team

The Inertia Advocate's `lens` and `expertise` must reference this specific team's domain
vocabulary. No cross-team boilerplate.

After all teams: shared-group roles to `.roles/shared/`, exec-office to
`.roles/exec-office/`. Skip if not declared.

Mark each team's checklist entry as completed once files are written:
`[x] [team name] — [n] files written at .roles/{area-slug}/`

**STEP 4 — COVERAGE AUDIT**

Run this audit against the skeleton's team checklist. Emit all results:

```
COVERAGE-AUDIT:

  [A] File count
      Skeleton expected: [total from Step 2 checklist]
      Actual written:    [count of .roles/ files, excluding index/README]
      Status:   [PASS | FAIL — list any team with wrong count]

  [B] Inertia Advocate per team
      [team name]: [PRESENT | MISSING] — .roles/{area}/inertia-advocate.md
      (repeat for each team in skeleton checklist)
      Status:   [PASS | FAIL]

  [C] Directory-to-skeleton fidelity
      For each area in skeleton:
        [area slug]: [EXISTS | MISSING as .roles/{area-slug}/]
      Directories present but not in skeleton: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Five-field spot-check
      Verify F-1..F-5 all non-empty in:
        - first file written per area (one area)
        - one Inertia Advocate file (any team)
      Status:   [PASS | FAIL — name any file with gap]

  AUDIT RESULT: [PASS | FAIL]
  Unresolved gaps: [list or "none"]
```

Resolve all gaps before Step 5.

**STEP 5 — FINALIZE org-chart.md**

Return to `org-chart.md`. Replace PENDING cells with actual counts from the audit:

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [n] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n] | **[= audit [A] actual]** | |

Add a coverage notes section: one line per area confirming role categories generated and
any absent by declaration.

Verify: Total in updated table equals audit [A] Actual. If they differ, identify the
discrepancy before writing the AMEND section.

**STEP 6 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — rewrite role files for that area;
   re-run audit checks [A]-[D] for that area; update headcount table.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: move [team name] from [current parent] to [new parent group];
   update skeleton, role file paths, and headcount table.
```

---

## V-05 — Combination: Schema-as-Contract + Scaffold-First + Coverage Audit + Resistance Profile

**Axis**: Schema-as-contract + Scaffold-first + Coverage audit loop + Inertia framing
**Hypothesis**: All four axes together create the most defensible prompt in this round.
The schema contract eliminates field ambiguity (C-05). The scaffold commits structure before
any writing begins (C-04, C-02). The resistance profile anchors IA differentiation before
any file is written (C-09). The coverage audit verifies all three invariants after writing
and before finalizing the chart (C-01, C-03, C-10). Each axis addresses a distinct failure
mode; combining them should produce a prompt that passes all 5 essential criteria and at
least 2 recommended criteria by construction. Tests whether accumulated structure produces
a reliable, if verbose, golden candidate — or whether the overhead creates new failure modes
from prompt length alone.

---

You are running `corps-build`. Read `org.yaml` from the path provided or auto-detect it.

==== ROLE FILE SCHEMA (reference contract) ====

| ID  | Field              | Content requirement |
|-----|--------------------|---------------------|
| F-1 | orientation        | Team-specific perspective grounded in this team's declared responsibilities. States what this person is oriented toward in this specific context. |
| F-2 | lens               | The specific domain, system, or practice through which this role evaluates proposals. Must name the thing. Generic frames ("technical perspective") fail. |
| F-3 | expertise          | Concrete systems built, decisions owned, or failures survived in this domain. No generic labels. Name actual systems or decisions. |
| F-4 | scope              | What this role approves, blocks, recommends, or escalates, and where authority ends. |
| F-5 | collaboration-pattern | How this role works with other roles on the same team: who they lean on, who they push back on, what productive friction looks like. |

Frontmatter required: `role-type` (standard | specialized | inertia-advocate | shared-group | exec-office), `area` (area slug from org.yaml).
"TBD" or empty body on any F-1..F-5 fails the schema contract.

==== END SCHEMA ====

==============================================================================
PHASE 0 — PARSE
Exit condition: parse manifest emitted, total role slots calculated.
==============================================================================

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth — e.g., Division > Team]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

==============================================================================
PHASE 1 — SCAFFOLD (structural commitment)
Exit condition: org-chart.md skeleton written with hierarchy, checklist, and pending table.
==============================================================================

Write `org-chart.md` now as a skeleton. This is the contract the rest of the run must match.

**Skeleton A — ASCII Hierarchy**

Use `+--` and `|`. All names verbatim from `org.yaml`. Minimum two nesting levels.
Every team from the parse manifest must appear.

**Skeleton B — Team Checklist**

```
TEAM CHECKLIST:
[ ] [team name] — [n] files expected at .roles/{area-slug}/
[ ] ...
TOTAL EXPECTED: [n] (= total declared role slots from Phase 0)
```

**Skeleton C — Pending Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | PENDING | PENDING | 1 | PENDING | [levels or "not declared"] |
| **Total** | PENDING | PENDING | [n teams] | PENDING | |

==============================================================================
PHASE 2 — RESISTANCE PROFILES (thinking step, visible output)
Exit condition: one profile per team, all domain vocabulary sets distinct.
==============================================================================

Before writing any role files, derive a resistance profile for each team.

For each team in checklist order:

```
RESISTANCE PROFILE: [team name]
  Core domain:          [what this team owns per org.yaml]
  Status-quo investment:[specific system, process, or past decision at risk if change proceeds]
  Rational objection:   [most technically credible reason to resist — concrete, not generic]
  Domain vocabulary:    [4-6 terms from this team's area that will anchor IA F-2 and F-3]
```

Review all profiles. If any two teams share identical domain vocabulary terms, revise
until distinct. Do not proceed to Phase 3 until all vocabulary sets are unique.

==============================================================================
PHASE 3 — WRITE ROLE FILES
Exit condition: file count equals total declared role slots; checklist fully marked.
==============================================================================

For each team in checklist order, write all role files before moving to the next team.

**Category A — Standard roles**
Path: `.roles/{area-slug}/{role-slug}.md`
Frontmatter: `role-type: standard`, `area: {area-slug}`
Populate F-1 through F-5 (schema above). All fields substantive.

**Category B — Specialized roles**
Same path pattern. Frontmatter: `role-type: specialized`, `area: {area-slug}`
F-2 and F-3 must name domain-specific systems that distinguish this role from standard
roles on the same team.

**Category C — Inertia Advocate** (mandatory — one per team)
Path: `.roles/{area-slug}/inertia-advocate.md`
Frontmatter: `role-type: inertia-advocate`, `area: {area-slug}`

The IA's fields must be anchored to this team's Phase 2 resistance profile:
- F-1 must surface the `rational objection` from the profile
- F-2 must include at least one `domain vocabulary` term from the profile
- F-3 must reference the `status-quo investment` from the profile
- F-4 and F-5 may follow standard patterns

No two IA files may share identical F-2 or F-3 body text. If duplication detected,
return to Phase 2 and differentiate before continuing.

After all teams:
- Shared-group roles: `.roles/shared/`, `role-type: shared-group`, populate F-1..F-5
- Exec-office roles: `.roles/exec-office/`, `role-type: exec-office`, populate F-1..F-5
- Skip if not declared in `org.yaml`

Mark each team's checklist entry: `[x] [team name] — [n] files written`

==============================================================================
PHASE 4 — COVERAGE AUDIT
Exit condition: AUDIT RESULT PASS on all checks.
==============================================================================

```
COVERAGE-AUDIT:

  [A] File count
      Checklist expected: [Phase 1 total]
      Actual written:     [count of .roles/ files, excluding index/README]
      Status:   [PASS | FAIL]

  [B] Inertia Advocate per team
      [team name]: [PRESENT | MISSING]
      Status:   [PASS | FAIL]

  [C] Directory-to-scaffold fidelity
      For each area in scaffold:
        [area slug]: [EXISTS | MISSING]
      Extra directories not in scaffold: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Schema compliance spot-check
      Check F-1..F-5 non-empty in:
        - one standard role (any team)
        - one specialized role (any team, if any exist)
        - one inertia-advocate.md (any team)
      Status:   [PASS | FAIL — name any file with schema gap]

  [E] IA domain-vocabulary check
      Verify that each IA F-2 contains at least one term from its Phase 2 vocabulary set.
      Status:   [PASS | FAIL — name any IA file missing profile vocabulary]

  AUDIT RESULT: [PASS | FAIL]
  Unresolved gaps: [list or "none"]
```

Resolve all gaps before Phase 5.

==============================================================================
PHASE 5 — FINALIZE org-chart.md (TABLE FIRST)
Exit condition: org-chart.md complete with all PENDING replaced; Total = Phase 4 [A] actual.
==============================================================================

Replace all PENDING cells in the skeleton with actual counts from the audit:

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [n] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= Phase 4 [A] actual]** | |

Add level distribution section: if levels declared, show breakdown. If not: "Level
distribution: not declared in org.yaml."

The ASCII hierarchy from Phase 1 skeleton is already correct — do not redraw it unless
group structure changed. Confirm hierarchy is still accurate.

Add coverage notes: one line per area confirming role categories generated and any absent
by declaration.

Phase 5 exit check: Total in table must equal Phase 4 [A] actual. If different, identify
the discrepancy before writing Phase 6.

==============================================================================
PHASE 6 — AMEND
==============================================================================

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — re-derive resistance profile (Phase 2),
   rewrite role files for that area (Phase 3), re-run audit checks [A]-[E] for that area,
   update headcount table (Phase 5).
2. Adjust level vocabulary: replace "[current level term from org.yaml]" with a new label
   across all role files and the headcount table.
3. Change group structure: move [team name] from [current parent] to [new parent group];
   update scaffold hierarchy, role file paths, and headcount table accordingly.
```
