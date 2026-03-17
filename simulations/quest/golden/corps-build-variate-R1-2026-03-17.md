---
skill: quest-variate
skill_target: corps-build
round: 1
date: 2026-03-17
rubric_version: 1
---

# Variate R1 — corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (shared-group + exec-office placement in write order) | V-01, V-05 |
| Output format (table-first headcount before ASCII diagram) | V-02, V-05 |
| Phrasing register (descriptive/narrative vs imperative/structured) | V-03 |
| Inertia framing (resistance profile phase before any file writing) | V-04, V-05 |
| Lifecycle emphasis (explicit phase gates with entry/exit conditions) | V-05 |

---

## V-01 — Role Sequence: Categorical Write Order

**Axis**: Role sequence
**Hypothesis**: Writing roles in strict categorical order (standard roles first, then
specialized roles, then Inertia Advocate, then shared-group roles, then exec-office roles)
anchors C-07 (type distinction) by construction. Because the model writes standard vs.
specialized as separate passes, the `role-type` annotation is applied at write time rather
than as a post-hoc label. Exec-office roles written last, under a dedicated `exec-office`
directory, prevents accidental nesting inside team areas. Strongest on C-07 and C-04.

---

You are running `corps-build`. Read the `org.yaml` at the path provided, or auto-detect
`org.yaml` in the working directory if no path is given.

**STEP 1 — PARSE ORG.YAML**

Read `org.yaml`. Echo a parse manifest before writing any files:

```
ORG-PARSED:
  org name: [name]
  nesting: [Division > Group > Team depth]
  teams: [list all team names with parent path]
  standard roles per team: [role names]
  specialized roles per team: [role names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "none"]
  total role slots: [n]
```

Halt on malformed or missing `org.yaml`: `PARSE ERROR: [reason]. Fix org.yaml before
running corps-build.`

**STEP 2 — WRITE ROLES IN CATEGORICAL ORDER**

For each team in declaration order, run sub-steps 2a → 2b → 2c in sequence before
proceeding to the next team. Do not interleave teams.

**2a. Standard roles** — write all standard roles for this team.

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Each file must contain all five required fields with non-empty body text:

- `orientation`: The team context this role operates from. One to two sentences grounded
  in the team's declared responsibilities.
- `lens`: The specific evaluative frame this role applies. Name the domain or system.
- `expertise`: The concrete skills or systems this role commands. No generic labels.
- `scope`: What this role can approve, block, or recommend within this team.
- `collaboration-pattern`: How this role interacts with other roles on this team.

Add to each file's frontmatter:

```yaml
role-type: standard
area: {area-slug}
```

**2b. Specialized roles** — write all specialized roles for this team.

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Same five required fields. Frontmatter:

```yaml
role-type: specialized
area: {area-slug}
```

The lens and expertise fields must name domain-specific systems or practices that
distinguish this specialized role from the standard roles in the same team.

**2c. Inertia Advocate** — write the Inertia Advocate for this team.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Required fields, each grounded in this specific team's declared responsibilities:

- `orientation`: Why a senior team member would rationally resist the proposed change.
  Name the specific concern drawn from the team's declared domain.
- `lens`: The status-quo system or practice this advocate is protecting. Must reference
  a term from this team's area or declared responsibilities. No generic "stability" text.
- `expertise`: What makes this person's skepticism credible. Name the actual systems,
  decisions, or processes they have owned in this team's domain.
- `scope`: What this advocate can slow, block, or escalate within this team's domain.
- `collaboration-pattern`: How this advocate engages with standard and specialized roles
  on this team — where they align and where they push back.

Frontmatter:

```yaml
role-type: inertia-advocate
area: {area-slug}
```

**STEP 3 — SHARED GROUP ROLES**

After all teams are complete, write shared-group roles.

Path: `.craft/roles/shared/{role-slug}.md`

Frontmatter: `role-type: shared-group`. Five required fields as above, with scope
spanning the group or division (not a single team). If no shared-group roles are declared
in `org.yaml`, skip this step.

**STEP 4 — EXEC OFFICE ROLES**

Write exec-office roles last.

Path: `.craft/roles/exec-office/{role-slug}.md`

Frontmatter: `role-type: exec-office`. Five required fields. Scope must reference
cross-functional authority rather than a single team's domain. If no exec-office roles
are declared in `org.yaml`, skip this step.

**STEP 5 — WRITE org-chart.md**

Write `org-chart.md` with three sections in order:

**5a. ASCII hierarchy** — an ASCII diagram showing the declared nesting from `org.yaml`.
Use `+--` and `|` box-drawing characters. All area names must match `org.yaml` exactly,
character for character. At least two hierarchy levels must be visible in the diagram.

Example structure (adapt to actual org):
```
[Org Name]
+-- [Division A]
|   +-- [Team 1]
|   +-- [Team 2]
+-- [Division B]
    +-- [Team 3]
```

**5b. Headcount table** — one row per area/group, a Total row, and a level-distribution
column. Counts must reflect the actual number of role files written, not the org.yaml
declaration.

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | n | n | 1 | n | [labels] |
| **Total** | n | n | n | n | |

**5c. Coverage notes** — one line per area noting any role types absent from that area
(e.g., "no specialized roles declared" is valid). No area may be omitted from coverage
notes.

**STEP 6 — AMEND**

Close with an AMEND section listing three specific options referencing actual names from
`org.yaml`:

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — re-run steps 2a–2c for that area only.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: move [team name] from [current parent] to [new parent group].
```

---

## V-02 — Output Format: Table-First org-chart.md

**Axis**: Output format
**Hypothesis**: Building the headcount table before the ASCII diagram forces the model to
commit to exact role counts before drawing the diagram. Because the table is constructed
from the file set that was just written (not from org.yaml), the Total row is verifiable
against the actual `.craft/roles/` file count, directly satisfying C-10. The ASCII diagram
is then drawn to match the table rather than the other way around, reducing count drift.
Strongest on C-06 and C-10.

---

You are running `corps-build`. Read `org.yaml` from the path provided or auto-detect it.

**PARSE**

Read `org.yaml` and emit a parse summary before writing files:

```
teams: [list]
standard roles per team: [counts]
specialized roles per team: [counts]
shared-group roles: [list or none]
exec-office roles: [list or none]
total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is absent or unreadable.

**WRITE ROLE FILES**

For each team declared in `org.yaml`, in declaration order, write all role files before
moving to the next team.

Per team, write in this order:
1. All standard roles
2. All specialized roles
3. The Inertia Advocate (mandatory — one per team, no exceptions)

Each role file path: `.craft/roles/{area-slug}/{role-slug}.md`

Every role file must contain five required fields with substantive (non-empty, non-"TBD")
body text:

```markdown
**orientation**: [team context this role operates from]
**lens**: [evaluative frame — name the specific domain or system]
**expertise**: [concrete skills or systems this role commands]
**scope**: [what this role can approve, block, or recommend on this team]
**collaboration-pattern**: [how this role works with other roles on this team]
```

Include `role-type` in frontmatter: `standard`, `specialized`, or `inertia-advocate`.

After all teams, write shared-group roles to `.craft/roles/shared/` and exec-office roles
to `.craft/roles/exec-office/`. Skip if none declared.

**WRITE org-chart.md — TABLE FIRST**

Write `org-chart.md` in this exact section order:

**Section 1 — Headcount Table (write this first)**

Count the role files just written. Do not estimate — count from the file set.

| Area | Headcount | Levels |
|------|-----------|--------|
| [area name from org.yaml] | [exact count of files written] | [level labels from org.yaml or "not declared"] |
| exec-office | [count or 0] | — |
| shared | [count or 0] | — |
| **Total** | [sum] | |

The Total must equal the exact number of `.craft/roles/` files written in this run
(excluding any index or README files).

**Section 2 — Level Distribution**

If `org.yaml` declares levels, add a secondary table showing IC vs. management (or
whatever level vocabulary is declared). If levels are not declared, write: "Level
distribution: not declared in org.yaml."

**Section 3 — ASCII Hierarchy Diagram**

Draw the org tree after the tables. All group and team names must match `org.yaml`
verbatim. Use box-drawing characters (`+--`, `|`). At least two nesting levels must
be visible.

**AMEND**

End with an AMEND section naming three concrete options referencing actual groups and
terms from `org.yaml`:

```
AMEND:
1. Regenerate area: [name one area] — rewrites all role files for that area.
2. Adjust level vocabulary: rename "[current level term]" across all files.
3. Change group structure: restructure [team or group name] as described.
```

---

## V-03 — Phrasing Register: Descriptive/Narrative

**Axis**: Phrasing register
**Hypothesis**: Framing the skill as a descriptive account of what good output looks like
(rather than numbered imperative commands) may produce more natural, holistic output.
The model must infer the necessary steps from the description, which may improve consistency
of five-field population (C-05) and role-type annotation (C-07) by engaging richer internal
understanding rather than mechanical step-following. Tests whether register affects completeness
and quality of per-file content.

---

You are running `corps-build`.

Your job is to read an `org.yaml` file and generate a complete organizational artifact
from it — two outputs: a set of typed role files in `.craft/roles/` and an `org-chart.md`
that shows the structure at a glance.

Start by reading `org.yaml`. If it is not at the path given, look for it in the working
directory. If you cannot find it, stop and say: "org.yaml not found. Provide the path to
run corps-build."

From `org.yaml`, understand the full structure: how many teams there are, what nesting
depth looks like (Division > Group > Team or whatever the yaml declares), what roles each
team needs, whether there are any shared-group roles or an executive office, and what
level vocabulary the org uses.

**Generating role files**

For each team in the org, generate one file per role in `.craft/roles/{area-slug}/`.
Area names in the directory tree must match the area names in `org.yaml` exactly — no
renaming, no flattening.

Every file must have five fields written out in full:

*Orientation* — the perspective this role holds within this specific team. Not a generic
job description but a statement of what this person is oriented toward given what this
team actually does.

*Lens* — the specific domain, system, or practice through which this role evaluates ideas
and proposals. Name the thing. "Technical perspective" is not a lens. "Distributed cache
invalidation latency" is.

*Expertise* — what makes this person's opinion credible. The systems they have built or
run, the decisions they have owned, the failures they have survived in this domain.

*Scope* — the reach of this role's authority: what they can approve, what they can block,
what they escalate, and where their influence stops.

*Collaboration pattern* — how this role normally works with the other roles on the same
team. Who they lean on, who they push back on, and what kind of friction is productive.

Add a `role-type` field to each file's frontmatter. The valid values are: `standard`
(applies to every team generically), `specialized` (unique to this team's domain), and
`inertia-advocate` (always present — one per team, representing principled resistance to
change). Shared-group and exec-office roles use `shared-group` and `exec-office`.

Every team must have at least one Inertia Advocate. The Inertia Advocate's orientation,
lens, and expertise must be drawn from the team's specific domain. An Inertia Advocate
who sounds the same as the Inertia Advocate in a different team is not acceptable — they
must feel like they belong to this team and this domain.

If `org.yaml` declares shared-group roles, write them in `.craft/roles/shared/`. If it
declares exec-office roles, write them in `.craft/roles/exec-office/` — not inside any
team's area directory.

**Generating org-chart.md**

`org-chart.md` is a single document that gives a reader the full picture of the org at a
glance. It should contain:

An ASCII diagram of the org hierarchy, using box-drawing characters, showing every area
from `org.yaml` in the correct nesting relationship. All names in the diagram must match
`org.yaml` verbatim.

A headcount section with a table showing each area, its total number of role files, and
the level distribution if levels are declared in `org.yaml`. Include a Total row. The
totals in this table must reflect the actual files written — they are not estimates.

Coverage notes — a line per area confirming what role categories were generated and noting
any that were absent by declaration (not by omission).

**Offering amendments**

After generating all outputs, offer three specific amendments that the user can request,
using actual names from `org.yaml`:

1. Regenerate a specific area — name one area and offer to rerun just that area's files.
2. Adjust the level vocabulary — name a level term from `org.yaml` and offer to relabel it.
3. Change the group structure — name a specific team and offer to move or restructure it.

---

## V-04 — Inertia Framing: Resistance Profile Phase Before File Writing

**Axis**: Inertia framing (prominently foregrounded) + Role sequence
**Hypothesis**: Running an explicit "resistance profiling" phase before writing any role
files forces the model to derive domain-specific skepticism content for each team
before committing it to disk. The resistance profile is a named thinking step — not an
output — that anchors all subsequent Inertia Advocate files with team-specific content.
This should eliminate the C-09 failure mode (identical boilerplate IA files across teams)
by making domain differentiation an explicit pre-condition. Strongest on C-03 and C-09.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory. Halt with `PARSE ERROR: [reason]` if not found or malformed.

**STEP 1 — PARSE**

Read `org.yaml`. Emit a parse manifest:

```
ORG-PARSED:
  org name: [name]
  depth: [n levels]
  teams: [list with parent path]
  standard roles per team: [list per team]
  specialized roles per team: [list per team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total role slots: [n]
```

**STEP 2 — RESISTANCE PROFILES (thinking step — no files written)**

Before writing any files, derive a resistance profile for each team. This is an internal
reasoning step. Do not skip it.

For each team, write one paragraph (in the output, visible to the reader) covering:

```
RESISTANCE PROFILE: [team name]
  Core domain: [what this team owns — drawn from org.yaml responsibilities]
  Status-quo investment: [the specific system, process, or decision the team has built
    and would lose if the proposal succeeds]
  Rational objection: [the most technically credible reason to resist — not "change is
    hard" but a concrete risk from this team's domain perspective]
  Vocabulary: [3-5 domain terms from this team's area that will anchor the IA's lens
    and expertise fields]
```

These profiles are reference material for Step 3. If any two teams share the same
`vocabulary` terms, revise until they are distinct.

**STEP 3 — WRITE ROLE FILES**

For each team, write role files in this order: standard roles, specialized roles, then
Inertia Advocate.

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Required fields in every file: `orientation`, `lens`, `expertise`, `scope`,
`collaboration-pattern`. No empty bodies. No "TBD".

Frontmatter must include `role-type` with one of: `standard`, `specialized`,
`inertia-advocate`, `shared-group`, `exec-office`.

**Inertia Advocate files must use the resistance profile from Step 2:**

- `lens` must include at least one of the vocabulary terms from that team's profile.
- `expertise` must reference the `status-quo investment` identified in the profile.
- `orientation` must surface the `rational objection` from the profile.

No two Inertia Advocate files may share identical `lens` or `expertise` body text. If
you find yourself reusing text, return to the resistance profile and differentiate.

After all teams, write shared-group roles to `.craft/roles/shared/` and exec-office
roles to `.craft/roles/exec-office/` (only if declared in `org.yaml`).

**STEP 4 — WRITE org-chart.md**

Write `org-chart.md` with three sections:

**ASCII hierarchy** — use `+--` and `|`. All names verbatim from `org.yaml`. Minimum
two nesting levels.

**Headcount table** — one row per area, a Total row, and level distribution column.

| Area | Headcount | Levels |
|------|-----------|--------|
| [area] | [n] | [labels or "not declared"] |
| **Total** | [sum] | |

**Coverage notes** — one line per area confirming role types generated. Note absences
by declaration, not omission.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — re-derive resistance profile and
   rewrite all role files for that area.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: move [team name] under [new parent group name].
```

---

## V-05 — Combination: Phase Gates + Table-First + Resistance Profile

**Axis**: Lifecycle emphasis (explicit phase gates) + Output format (table-first) + Inertia framing
**Hypothesis**: Combining three axes creates a skill body with the strongest possible
structural guarantees. Phase gates with entry/exit conditions prevent the model from
writing outputs before preconditions are met. Table-first org-chart forces count
commitment before drawing. Resistance profiling ensures IA differentiation. This
combination should be the hardest to break — if it fails, the failure is in a single
accountable gate. Expected to be the strongest overall variation, with the highest
composite score, but also the longest prompt. Tests whether structure overhead costs
more than it earns in accuracy.

---

You are running `corps-build`.

==============================================================================
PHASE 0 — PARSE
Entry condition: `org.yaml` exists and is readable.
Exit condition: parse manifest emitted with no unresolved gaps.
==============================================================================

Read `org.yaml` from the path provided, or auto-detect in the working directory.

Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting depth: [n levels — e.g., Division > Team]
  teams: [list all team names with full parent path]
  standard roles per team: [role names by team]
  specialized roles per team: [role names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

If `org.yaml` is missing or malformed: `PARSE ERROR: [reason]. Correct org.yaml before
running corps-build.` Do not proceed.

==============================================================================
PHASE 1 — RESISTANCE PROFILES
Entry condition: PHASE 0 complete.
Exit condition: one profile per team, all vocabulary sets distinct.
==============================================================================

For each team in declaration order, derive a resistance profile. Emit it in the output
(this is visible reasoning, not a hidden step):

```
RESISTANCE PROFILE: [team name]
  Core domain: [what this team owns per org.yaml]
  Status-quo investment: [specific system, process, or past decision at risk]
  Rational objection: [the most technically credible reason to resist — concrete, not generic]
  Domain vocabulary: [4-6 terms from this team's area that will anchor IA lens and expertise]
```

Review all profiles. If any two teams share identical domain vocabulary terms, revise
until distinct. Do not proceed to Phase 2 until all profiles have unique vocabulary.

==============================================================================
PHASE 2 — WRITE ROLE FILES
Entry condition: PHASE 1 complete with all resistance profiles distinct.
Exit condition: file count equals total declared role slots from PHASE 0.
==============================================================================

For each team, in declaration order, write role files in categorical sequence:

**Category A — Standard roles**
Path: `.craft/roles/{area-slug}/{role-slug}.md`
Frontmatter: `role-type: standard`, `area: {area-slug}`
Five required fields (non-empty, non-"TBD"):
- `orientation`: team-grounded perspective
- `lens`: specific domain or system named
- `expertise`: concrete skills, systems, or past decisions
- `scope`: approval/block/escalation reach
- `collaboration-pattern`: interaction with other team roles

**Category B — Specialized roles**
Same path pattern, same five fields.
Frontmatter: `role-type: specialized`, `area: {area-slug}`
`lens` and `expertise` must name domain-specific systems distinguishing this from
standard roles on the same team.

**Category C — Inertia Advocate** (mandatory — one per team, no exceptions)
Path: `.craft/roles/{area-slug}/inertia-advocate.md`
Frontmatter: `role-type: inertia-advocate`, `area: {area-slug}`

The Inertia Advocate's five fields must be anchored to Phase 1 resistance profile:
- `orientation` must surface the `rational objection` from the profile
- `lens` must include at least one `domain vocabulary` term from the profile
- `expertise` must reference the `status-quo investment` from the profile
- `scope` and `collaboration-pattern` may be standard

No two Inertia Advocate files may share identical `lens` or `expertise` body text.
If duplication is detected, return to Phase 1 and differentiate before continuing.

After all teams:
- Write shared-group roles to `.craft/roles/shared/` with `role-type: shared-group`
- Write exec-office roles to `.craft/roles/exec-office/` with `role-type: exec-office`
- Skip categories not declared in `org.yaml`

**Phase 2 exit check**: count files written. Must equal `total declared role slots`
from PHASE 0. If the count does not match, identify the gap before proceeding.

==============================================================================
PHASE 3 — WRITE org-chart.md (TABLE FIRST)
Entry condition: PHASE 2 complete, file count verified.
Exit condition: org-chart.md written with all three sections, Total = Phase 2 file count.
==============================================================================

Write `org-chart.md` in this section order:

**Section 1 — Headcount Table**

Compute from the Phase 2 file count (not from org.yaml). One row per area. Include
exec-office and shared rows if files were written there.

| Area | Standard | Specialized | Inertia-Adv | Shared/Exec | Total | Levels |
|------|----------|-------------|-------------|-------------|-------|--------|
| [area] | n | n | 1 | — | n | [labels] |
| exec-office | — | — | — | n | n | — |
| shared | — | — | — | n | n | — |
| **Total** | n | n | n | n | **[must = Phase 2 file count]** | |

**Section 2 — Level Distribution**

If levels are declared in `org.yaml`, show a breakdown by level label across the org.
If not declared: "Level distribution: not declared in org.yaml."

**Section 3 — ASCII Hierarchy**

Draw after the tables. Use `+--` and `|`. All names verbatim from `org.yaml`. Minimum
two nesting levels visible. Every team in org.yaml must appear in the diagram.

**Phase 3 exit check**: confirm that `Total` in Section 1 equals the file count from
Phase 2. If they differ, identify which area is miscounted before adding the AMEND section.

==============================================================================
PHASE 4 — AMEND
Entry condition: PHASE 3 complete, cross-reference verified.
==============================================================================

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — re-derive resistance profile (Phase 1)
   and rewrite all role files for that area (Phase 2). Update headcount table.
2. Adjust level vocabulary: replace "[current level term from org.yaml]" with a new label
   across all role files.
3. Change group structure: move [team name] from [current parent] to [new parent group],
   update directory paths and org-chart.md accordingly.
```
