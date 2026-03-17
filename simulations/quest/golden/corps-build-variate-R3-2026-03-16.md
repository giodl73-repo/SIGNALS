---
skill: quest-variate
skill_target: corps-build
round: 3
date: 2026-03-16
rubric_version: 3
---

# Variate R3 -- corps-build

5 complete prompt body variations for the `corps-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v3 adds C-15 and C-16. R2 V-03 and V-04 showed early forms of both; R3 targets them directly.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Inertia framing: person-portrait quality bar + transplant self-check (C-15) | V-01 |
| Lifecycle emphasis: resistance profile as hard-gated extraction phase (C-16) | V-02 |
| Phrasing register: output-forward derivation chain with annotated examples (C-15, C-16) | V-03 |
| Inertia framing + Lifecycle: profile-to-portrait pipeline with explicit field derivation (C-15, C-16) | V-04 |
| Full integration: all eight aspirational criteria (C-09 through C-16) | V-05 |

---

## R2 Gap Analysis (rubric v3 lens)

| New Criterion | Best R2 Coverage | Gap |
|---------------|-----------------|-----|
| C-15 IA file as person-portrait | V-03 partial -- showed strong/weak lens example; portrait standard not enforced structurally | No R2 variation required self-check or transplant test; quality depended on model inference |
| C-16 Resistance profile before IA write | V-04 closest -- had credibility source + failure mode fields; lens phrase was part of profile | V-04 profile fields did not match C-16's three required elements exactly: defended-artifact, change-pressure, derived lens-phrase; trace-back requirement not explicit |

Both C-15 and C-16 appeared in R2 but as approximations -- the rubric sharpened the bar. R3 targets the precise mechanisms.

---

## V-01 -- Inertia Framing: Person-Portrait Standard with Transplant Test

**Axis**: Inertia framing
**Hypothesis**: Embedding a "portrait standard" directly in the IA writing instructions --
with strong/weak examples and a per-file transplant-test self-check annotation -- makes
generic lens language visible and correctable inline without adding a new phase. The transplant
test ("if you pasted this lens into a different team's file unchanged, would it still apply?")
creates a binary gate the model evaluates per file rather than abstractly. This is the minimal
structural addition for C-15: one paragraph of standard + one annotation per IA write.

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or use the
provided path.

**Phase sequence**: PARSE -> VALIDATE -> WRITE -> CROSS-REF. Do not begin a phase until its
gate appears in output.

---

### PHASE 1 -- PARSE

Read org.yaml. Emit:

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
  teams:
    [team name] (group: [parent]) -- standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  nesting depth: [n]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] role slots.`
or `PARSE-FAIL: [error]. Halt.`

---

### PHASE 2 -- VALIDATE

**Entry condition**: PARSE-PASS.
**No files written during this phase.**

Run 4 checks:

```
VALIDATE:
  [V-1] every team has >= 1 role declared
        PASS / FAIL -- teams with no roles: [list]

  [V-2] no role name in both standard and specialized for the same team
        PASS / FAIL -- collisions: [team.role list]

  [V-3] no duplicate team names across groups
        PASS / FAIL -- duplicates: [list with parent groups]

  [V-4] level vocabulary uses one consistent label convention
        PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. Proceeding to WRITE.`
or `VALIDATE-FAIL: [n] error(s): [details]. No files written. Halt.`

---

### PHASE 3 -- WRITE

**Entry condition**: VALIDATE-PASS.

Write outputs in this sequence: IA files (all teams) -> org-chart.md -> standard/specialized role files.

---

**3a -- Inertia Advocate files**

Write the IA file for every team before writing any standard or specialized roles.
Path: `.craft/roles/{area-slug}/inertia-advocate.md`

**Portrait standard -- apply to every IA file:**

An Inertia Advocate file describes the specific kind of person who would occupy this role
on *this team*. It is not a template filled with domain-adjacent words. The lens field
opens with a phrase anchored to a concrete domain artifact this team owns or operates.
The expertise field names a real thing this person has built, run, or maintained.

Apply this test before emitting each IA file: if you pasted the `lens` field into a
different team's IA file, would it still apply? If yes, rewrite it. A lens that passes
the transplant test fails this standard.

Strong lens (team: API Gateway):
> "Schema contract enforcement at the ingress boundary -- this advocate tracks breaking
> change candidates against the 23 published client SDKs and monitors the three consumers
> that have not migrated off v1. Any endpoint deprecation notice triggers a review from
> this role before the timeline is announced."

Weak lens (any team, fails transplant test):
> "Operational stability and institutional knowledge about existing systems and processes."

Strong expertise (team: Data Ingestion):
> "Authored the three-stage validation pipeline that catches schema drift before records
> land in the warehouse; maintains the dead-letter queue retry policy and the monitoring
> dashboard tracking late-arrival SLA compliance."

Weak expertise (any team):
> "Deep knowledge of data systems and experience with change management and data quality."

Five fields, populated from the team's declared responsibilities in org.yaml:

- **orientation**: rational perspective of a senior team member defending the current
  arrangement; names the specific practice, system, or decision defended -- not a generic
  stance toward stability
- **lens**: opens with a phrase anchored to this team's domain; describes the specific
  slice of the system this advocate monitors; no generic "stability" or "institutional
  knowledge" phrases; passes transplant test
- **expertise**: names specific systems, code paths, schemas, or operational procedures
  this person has built or maintained; must differ from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart role

No two IA files may share identical `lens` or `expertise` text.

After each IA file:
```
IA-WRITTEN: [team name]
  lens-phrase: "[opening phrase of lens field]"
  transplant-test: PASS (phrase is team-specific) / FAIL (generic language -- [which phrase])
```

After all IA files: `IA-PHASE-COMPLETE: [n of n] teams covered.`

If any IA-WRITTEN shows transplant-test FAIL, rewrite that file before proceeding.

---

**3b -- org-chart.md** (after all IA files)

Sections in order:

1. ASCII hierarchy -- box-drawing characters, minimum two nesting levels. Group names match
   org.yaml exactly. Team leaf nodes show headcount in parentheses.

2. Headcount by Group/Area:
   ```markdown
   | Group/Area | Headcount | Key Roles |
   |------------|-----------|-----------|
   | [name]     | [n]       | [names]   |
   | **Total**  | **[n]**   |           |
   ```
   One row per area, Total row, counts sum correctly.

3. Level Distribution -- labels from org.yaml. Total matches headcount Total.
   If no levels declared, infer IC and Management from role names.

4. AMEND section:
   ```markdown
   ## AMEND
   1. --area "[area name]" -- regenerate one area (IA + all roles + chart row).
      Areas: [list from org.yaml]
   2. --levels "[old]:[new]" -- replace level vocabulary throughout.
      Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current structure: [parent > child pairs from org.yaml]
   ```

`CHART-WRITTEN.`

---

**3c -- Standard and specialized role files**

Paths:
- `.craft/roles/{area-slug}/{role-slug}.md` -- standard and specialized
- `.craft/roles/{group-slug}/{role-slug}.md` -- shared group roles
- `.craft/roles/exec-office/{role-slug}.md` -- exec office

All five fields, no placeholder text. Scope field must be explicit:
`standard`, `specialized -- [team name]`, `shared -- [group name]`, or `exec office`.

After each team: `TEAM-WRITTEN: [team name] -- [n] std + [n] spec.`

---

### PHASE 4 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n]
  files written:  [n]
  result: MATCH / MISMATCH
  if MISMATCH: missing: [list]

  IA check:  teams [n], IA files [n] -- MATCH / MISMATCH
  dir check: areas in org.yaml [list], dirs present [list] -- MATCH / MISMATCH
```

All MATCH: `CROSS-REF-PASS: build consistent.`
Any MISMATCH: `CROSS-REF-FAIL: [details].`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:      PASS (4/4 checks)
  IA coverage:   [n of n] teams -- all portrait-standard / [n] transplant-test rewrites applied
  org-chart.md:  written
  role files:    [n] written / [n] declared
  cross-ref:     PASS / FAIL
  status:        COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-02 -- Lifecycle Emphasis: Resistance Profile as Hard-Gated Extraction Phase

**Axis**: Lifecycle emphasis
**Hypothesis**: A named PROFILE PHASE with three required fields -- (1) specific system or
process defended, (2) specific change pressure threatening it, (3) a lens phrase derived
from those two -- gated before any IA file is written, makes C-16 pass by construction. The
gate is binary: no IA file may be written until PROFILE-COMPLETE appears in the output. This
is the minimal new phase: one step added between VALIDATE and WRITE that locks IA content
before any file is touched. Secondary: because the lens phrase is derived from
defended-artifact + change-pressure, generic phrases are mechanically excluded -- you cannot
derive a specific lens phrase from "data stability" and "rapid change."

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or use the
provided path.

**Phase sequence**: PARSE -> VALIDATE -> PROFILE -> WRITE -> CROSS-REF. Each gate must
appear in output before the next phase begins.

---

### PHASE 1 -- PARSE

```
PARSE:
  org name: [name]
  groups: [list]
  teams:
    [team name] (group: [parent]) -- standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS: [n] teams, [n] role slots.`
or `PARSE-ERROR: [description]. Halt.`

---

### PHASE 2 -- VALIDATE

**Entry**: PARSE-PASS. **No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role         PASS / FAIL -- teams with no roles: [list]
  [V-2] no std/spec role collision        PASS / FAIL -- collisions: [list]
  [V-3] no duplicate team names           PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary       PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks. Proceeding to PROFILE.`
or `VALIDATE-FAIL: [n] errors. No files written. Halt.`

---

### PHASE 3 -- PROFILE

**Entry**: VALIDATE-PASS.
**No files written during this phase.**
**No IA file may be written until PROFILE-COMPLETE appears in output.**

For every team declared in org.yaml, extract a resistance profile with exactly three fields:

```
PROFILE: [team name]
  defended-artifact:  [name the specific system, code path, schema, deployment pipeline,
                      SLA contract, or operational procedure this team owns and would
                      protect -- NOT "stability," "existing processes," or "data quality"
                      as unmodified generic categories]
  change-pressure:    [name the specific proposed change, migration, architectural shift,
                      or new initiative that threatens the defended artifact -- NOT "rapid
                      change," "new features," or "technical debt" without qualification]
  lens-phrase:        [a 5-10 word phrase derived from defended-artifact + change-pressure,
                      usable as the opening phrase of this team's IA lens field; must be
                      distinct from every other team's lens-phrase]
```

Rules:
- `defended-artifact` must name a specific thing -- not a category
- `change-pressure` must name a specific initiative or shift -- not a generic force
- `lens-phrase` is derived: it combines a signal from defended-artifact with a signal from
  change-pressure; it cannot be written without both
- A profile where all three fields could apply to a different team fails and must be revised

After all profiles:

```
PROFILE-COMPLETE: [n of n] teams profiled.
  Lens phrases:
    [team name]: "[lens-phrase]"
    [team name]: "[lens-phrase]"
    ...
```

Scan for collisions: `LENS-COLLISION: [team A] and [team B] share "[phrase]". Revise one
before proceeding.` -- if collision found, revise and reprint the corrected profile before
emitting PROFILE-COMPLETE.

---

### PHASE 4 -- WRITE

**Entry**: PROFILE-COMPLETE.

**4a -- Inertia Advocate files (all teams, before any other role)**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields, populated using the team's resistance profile from Phase 3:

- **orientation**: from `defended-artifact` -- the rational perspective of the person
  who built or runs that artifact; names the specific concern, not a generic caution
- **lens**: opens with the `lens-phrase` from Phase 3, then expands in 2-3 sentences
  describing the specific slice of the system this advocate monitors; body text must
  reference at least one term from `defended-artifact`
- **expertise**: from `defended-artifact` -- names the specific systems, processes, or
  decisions this person has built or maintained; must differ from every other team's IA
  expertise entry
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: surfaces resistance in design reviews and architecture
  discussions; primary counterpart is the role most likely to propose structural change
  on this team; escalates when velocity pressure overrides quality threshold

No two IA files may share identical `lens` or `expertise` text.

After each file:
```
IA-WRITTEN: [team name]
  profile lens-phrase used: "[phrase from Phase 3]"
  lens opening matches profile: YES / NO
```

If `lens opening matches profile: NO`, rewrite the lens before proceeding.

After all IA files: `IA-PHASE-COMPLETE: [n of n] teams. All IA files written before
standard or specialized roles.`

---

**4b -- org-chart.md**

Sections in order:

1. ASCII hierarchy -- minimum two nesting levels. Group names match org.yaml exactly.
   Team leaf nodes show headcount in parentheses.

2. Headcount table:
   ```markdown
   | Group/Area | Headcount | Key Roles |
   |------------|-----------|-----------|
   | [name]     | [n]       | [names]   |
   | **Total**  | **[n]**   |           |
   ```

3. Level Distribution -- labels from org.yaml. Total matches headcount Total.
   If no levels declared, infer IC and Management from role names.

4. AMEND section:
   ```markdown
   ## AMEND
   1. --area "[area name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Areas: [list]
   2. --levels "[old]:[new]" -- replace level labels. Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current structure: [parent > child pairs]
   ```

`CHART-WRITTEN.`

---

**4c -- Standard and specialized role files**

Paths per scope type. All five fields, no placeholder text. Scope field explicit.

After each team: `TEAM-WRITTEN: [team name] -- [n] std + [n] spec.`

---

### PHASE 5 -- CROSS-REF

```
CROSS-REF:
  org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH
  if MISMATCH: missing: [list]

  IA files:    teams [n], IA files [n] -- MATCH / MISMATCH
  Profile use: every IA lens traces to a Phase 3 profile -- YES / NO
```

All pass: `CROSS-REF-PASS: build consistent. All IA lenses derived from profiles.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:          PASS (4/4)
  resistance profiles: [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA phase:          [n of n] teams written from profiles, before standard/specialized
  org-chart.md:      written
  role files:        [n] written / [n] declared
  cross-ref:         PASS / FAIL
  status:            COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-03 -- Phrasing Register: Derivation Chain in Output-Forward Language

**Axis**: Phrasing register
**Hypothesis**: An output-forward prompt that describes what a well-formed resistance
profile produces -- showing the derivation chain (defended-artifact + change-pressure ->
lens-phrase -> IA lens field -> IA expertise field) with annotated strong/weak examples at
each stage -- produces better C-15 and C-16 compliance than imperative step instructions.
When the model sees the full chain of inference rather than a list of checks, it is more
likely to produce the whole chain rather than the first step alone. The derivation annotation
("this lens phrase comes from combining X with Y") is the key mechanism that R2 V-03 lacked.

---

You are running `corps-build`. Read org.yaml in the working directory, or use the path provided.

`corps-build` produces two outputs: **org-chart.md** and **typed role files** under
`.craft/roles/`. What follows describes what good output looks like at each stage.

---

### Before writing: parse and validate

Read org.yaml. Confirm: every team has at least one role declared; no role name appears in
both standard and specialized for the same team; no two teams share a name; level vocabulary
is consistent. If any problem is found, list it in a `VALIDATE:` block and halt. If none,
emit `VALIDATE: no structural anomalies. Proceeding.`

---

### Resistance profiles: what they look like and how they feed the IA files

Before writing any Inertia Advocate file, identify the resistance profile for each team.
A resistance profile has three components, and each component feeds the IA file directly:

**Component 1 -- the defended artifact** becomes the `expertise` field anchor and the
opening orientation of the IA file. It names a specific thing this team owns and would
defend: a schema, a deployment pipeline, an SLA contract, a test suite, an operational
procedure -- not a category.

**Component 2 -- the change pressure** frames the orientation field. It names the specific
proposed change or initiative that threatens the defended artifact -- not a generic force.

**Component 3 -- the lens phrase** is derived by combining signals from components 1 and 2.
It opens the `lens` field. It cannot be written without the other two, because it is a
compression of both.

**Derivation chain (read this as the template):**

```
defended-artifact:  the nightly data reconciliation job that runs at 02:00 UTC
change-pressure:    proposed migration from batch ingestion to streaming pipeline
lens-phrase:        "Reconciliation job integrity under streaming migration pressure"
IA lens field:      "Reconciliation job integrity under streaming migration pressure --
                    this advocate monitors the batch window SLAs, the 14 downstream
                    consumers that depend on the 06:00 snapshot, and any proposed
                    pipeline change that shortens or eliminates the reconciliation window."
IA expertise field: "Designed and operates the reconciliation job; authored the audit log
                    that tracks row-level diff counts; holds the runbook for the three
                    historical replay scenarios triggered by upstream schema changes."
```

The derivation is traceable: lens phrase appears verbatim in the lens field; defended
artifact drives the expertise field. This is what C-16 and C-15 together require.

**Weak derivation chain (do not produce this):**

```
defended-artifact:  data stability and process continuity
change-pressure:    rapid change and new technology adoption
lens-phrase:        "Stability and continuity focus"
IA lens field:      "Institutional knowledge about existing systems and processes."
```

The weak chain is not a derivation -- it is boilerplate substitution. The lens phrase
could be transplanted to any team's IA file unchanged.

Emit the resistance profiles before any IA file write:

```
RESISTANCE PROFILES:

[Team Name]
  defended-artifact: [specific]
  change-pressure:   [specific]
  lens-phrase:       "[derived, 5-10 words]"
```

`PROFILE-COMPLETE: [n] profiles. Lens phrases: [list, one per line].`

---

### What .craft/roles/inertia-advocate.md files contain

Each IA file is a portrait of the kind of person who would occupy this role on this specific
team. The `lens` field opens with the resistance profile's lens phrase. The `expertise` field
names the specific defended artifact, the systems around it, and the operational knowledge
this person holds. The file could not be transplanted to a different team's IA slot without
substantive rewrite -- because the lens and expertise are anchored to this team's context.

Five fields:

- **orientation**: the rational perspective of a senior person who built or runs the
  defended artifact; names the specific practice or decision defended; does not describe
  a generic resistance to change
- **lens**: opens with the lens phrase from the resistance profile; expands to describe
  the specific domain slice this advocate monitors; no "stability," "institutional
  knowledge," or similar generic phrases
- **expertise**: names the specific artifact from the resistance profile; lists related
  systems, schemas, or procedures this person has built or maintained; differs from every
  other team's IA expertise entry
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums, cadence, primary counterpart role (the role most
  likely to propose the change pressure on this team)

Write all IA files before any standard or specialized role files.
After all IA files: `IA-COMPLETE: [n of n] teams.`

---

### What org-chart.md contains

A well-formed org-chart.md has four sections, in this order:

**Section 1 -- ASCII hierarchy**

`+--` and `|` characters, minimum two nesting levels. Group names exactly as in org.yaml.
Every team leaf node shows its headcount in parentheses.

**Section 2 -- Headcount by Group/Area table + analytic prose**

Table: one row per area, headcount, key roles, level labels. Total row.

After the table, 2-3 sentences that interpret the numbers. These sentences are specific:
they name an actual area, cite an actual count, and make an observation the table rows
alone do not convey.

Strong analytic prose (produce this):
> "Platform Engineering carries 9 of 22 total headcount -- the largest area by nearly 2:1
> over the next-largest area. All five Platform teams declare IC levels, but no management
> level vocabulary appears in org.yaml, suggesting the org has not yet leveled its
> management layer."

Weak analytic prose (do not produce this):
> "The org has several teams with different headcount. Level distribution is shown below."

**Section 3 -- Level Distribution table + seniority sentence**

Labels from org.yaml. Total matches headcount Total. One sentence after the table on
seniority profile.

**Section 4 -- AMEND options**

Three options: `--area "[name]"`, `--levels "[old]:[new]"`, `--restructure "[team] > [new-parent]"`.
Each option names the available values for its argument.

---

### What standard and specialized role files contain

Each file has exactly five typed fields. No field is empty, "TBD," or generic boilerplate.

- **orientation** -- the perspective this role holds at any decision point
- **lens** -- the specific system slice this role attends to; for IA files, opens with the
  resistance profile's lens phrase
- **expertise** -- what this role knows others at the table do not; for IA files, names
  the defended artifact and associated systems
- **scope** -- exactly one of: `standard`, `specialized -- [team name]`, `shared -- [group]`,
  `exec office`; must distinguish standard from specialized explicitly
- **collaboration pattern** -- who, what forums, what cadence, what triggers

---

### After writing: build verification

```
CORPS-BUILD -- {date}
  parse:        [org name], [n] teams, [n] slots
  validate:     [anomalies / none -- PASS]
  profiles:     [n of n] teams -- defended-artifact, change-pressure, lens-phrase extracted
  IA files:     [n of n] teams -- all written from profiles, before standard/specialized
  org-chart:    written (diagram + table + prose + level dist + AMEND)
  role files:   [n] written / [n] declared -- MATCH / MISMATCH
                if MISMATCH: missing: [list]
  scope dist:   [n] standard, [n] specialized, [n] shared, [n] exec-office
  cross-ref:    table total [n] == file count [n] -- MATCH / MISMATCH
  status:       COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-04 -- Inertia Framing + Lifecycle: Profile-to-Portrait Pipeline

**Axes**: Inertia framing (C-15) + Lifecycle emphasis (C-16)
**Hypothesis**: A prompt that (1) extracts a resistance profile for each team as a gated
phase before any IA write, and (2) explicitly connects each profile field to a target IA
file field through a labeled derivation table, makes the profile-to-portrait transformation
mechanical rather than inferential. The derivation table is the key mechanism: "lens-phrase
from profile -> opening of IA lens field; defended-artifact -> IA expertise field anchor."
When the connection is explicit rather than implied, the model does not need to infer the
link -- it follows it. This satisfies C-16 (profile as pre-artifact) and C-15 (portrait
quality) together as a single construction mechanism rather than two independent checks.
The portrait self-check gate at the end of the IA phase catches regressions before moving on.

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or use
the provided path.

Execute steps in order. Each gate must appear in output before the next step begins.

---

**STEP 1 -- PARSE**

```
PARSE:
  org name: [name]
  groups: [list]
  teams:
    [team name] (group: [parent]) -- standard: [names], specialized: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels declared: [list or "not declared"]
  total role slots: [n]
```

`PARSE-PASS.` or `PARSE-ERROR: [description]. Halt.`

---

**STEP 2 -- VALIDATE**

**Entry**: PARSE-PASS. **No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role                  PASS / FAIL
  [V-2] no std/spec name collision per team        PASS / FAIL
  [V-3] no duplicate team names                    PASS / FAIL
  [V-4] consistent level vocabulary                PASS / FAIL
```

`VALIDATE-PASS: 4/4. Proceeding.`
or `VALIDATE-FAIL: [errors]. No files written. Halt.`

---

**STEP 3 -- RESISTANCE PROFILES**

**Entry**: VALIDATE-PASS.
**No files written during this step.**
**No IA file may be written before PROFILE-COMPLETE.**

For each team, extract three fields. The third is derived from the first two:

```
PROFILE: [team name]
  defended-artifact:  [the specific system, schema, pipeline, SLA, or procedure this
                      team owns -- not a category like "data quality" or "system stability"]
  change-pressure:    [the specific proposed change or initiative threatening the defended
                      artifact -- not a generic force like "rapid change" or "new tech"]
  lens-phrase:        [5-10 words derived by combining the core signal from defended-artifact
                      with the core threat from change-pressure; this phrase MUST appear
                      verbatim as the opening of this team's IA lens field]
```

Derivation requirement: the `lens-phrase` is not a label for "what this team cares about."
It is a compressed statement of the specific tension between what is defended and what
threatens it. A lens-phrase that could be written without knowing `defended-artifact` and
`change-pressure` is not derived.

Example (team: Schema Registry):
```
defended-artifact:  the versioned schema contract table (currently 340 registered schemas)
change-pressure:    GraphQL federation migration that would replace typed schema contracts
                    with resolver-level field resolution
lens-phrase:        "Schema contract table integrity through federation migration"
```

After all profiles:
```
PROFILE-COMPLETE: [n of n] teams profiled.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

Collision check: any two identical or near-identical lens phrases -> `LENS-COLLISION: [teams]. Revise.`

---

**STEP 4 -- DERIVATION TABLE**

Before writing any IA file, emit the derivation table. This table maps each profile field
to the target IA file field it populates. It is the build contract for the IA phase.

```markdown
| Team | defended-artifact -> expertise anchor | lens-phrase -> lens opening |
|------|---------------------------------------|------------------------------|
| [team name] | [one phrase from defended-artifact] | "[lens-phrase]" |
```

Rules:
- `expertise anchor` is the seed phrase for this team's IA `expertise` field
- `lens opening` is the verbatim opening phrase of this team's IA `lens` field
- Every row must be filled; no cell may be generic

`DERIVATION-TABLE-CLOSED: [n] rows. IA write phase may begin.`

---

**STEP 5 -- WRITE ALL IA FILES**

**Entry**: DERIVATION-TABLE-CLOSED.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields, populated by following the derivation table:

- **orientation**: from `defended-artifact` -- the rational perspective of someone who
  built or maintains that artifact; what specific concern drives their review attention
- **lens**: opens verbatim with the `lens-phrase` from Step 3; then expands in 2-3
  sentences naming the domain slice, the monitoring signals, and the failure mode this
  advocate watches for; no generic stability language
- **expertise**: anchored to the `expertise anchor` from the derivation table; names the
  specific system, schema, or procedure and the operational knowledge around it; differs
  from every other team's IA expertise entry
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums (design review, sprint planning, architecture board),
  cadence, primary counterpart -- the role most likely to propose the change-pressure
  initiative on this team

No two IA files may share identical `lens` or `expertise` text.

After each file:
```
IA-WRITTEN: [team]
  lens opens with lens-phrase: YES / NO
  expertise anchored to defended-artifact: YES / NO
```

Any NO -> rewrite the failing field before proceeding.

After all IA files:

**Portrait self-check** -- for each IA file, verify:
- [ ] lens contains no generic phrases ("stability," "institutional knowledge,"
      "resistance to change," "status quo advocate")
- [ ] expertise names a concrete artifact, not a domain category
- [ ] file could not be transplanted to a different team's IA slot unchanged

```
PORTRAIT-CHECK: [n of n] IA files pass all three self-checks.
  Failures (if any): [team name] -- [which check failed] -- [corrective rewrite applied]
```

`IA-PHASE-COMPLETE: [n of n] teams. Portrait self-check passed. Standard and specialized
roles may now be written.`

---

**STEP 6 -- WRITE REMAINING ROLE FILES**

For each team (org.yaml declaration order):

**6a. Standard role files**: `.craft/roles/{area-slug}/{role-slug}.md`, `scope: standard -- present in all teams`
**6b. Specialized role files**: `.craft/roles/{area-slug}/{role-slug}.md`, `scope: specialized -- [team name]`
**6c. Shared group roles** (if declared): `.craft/roles/{group-slug}/{role-slug}.md`, `scope: shared -- group: [name]`
**6d. Exec office roles** (if declared): `.craft/roles/exec-office/{role-slug}.md`, `scope: exec office`

All five fields, no placeholder text. Scope field explicit -- not derivable from directory alone.

After each team: `TEAM-COMPLETE: [team name] -- [n] std + [n] spec.`

---

**STEP 7 -- ORG-CHART.MD**

Sections in order:

1. ASCII hierarchy -- minimum two nesting levels, headcount at leaf nodes.
2. Headcount by Group/Area table with Total row.
3. Level Distribution table with Total row.
4. AMEND section (three options with specific values from org.yaml).

---

**STEP 8 -- BUILD SUMMARY**

```
BUILD-COMPLETE -- {date}
  validate:            PASS (4/4)
  resistance profiles: [n of n] teams (derived: defended-artifact + change-pressure -> lens-phrase)
  derivation table:    [n] rows written (explicit field mappings)
  IA files:            [n of n] -- written from profiles; portrait self-check [n of n] pass
  standard roles:      [n]
  specialized roles:   [n]
  shared group roles:  [n]
  exec office roles:   [n]
  total files:         [n] written / [n] declared -- MATCH / YES / NO
  org-chart.md:        written
  status:              COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## V-05 -- Full Integration: All Eight Aspirational Criteria

**Axes**: Inertia framing + Lifecycle emphasis + Output format + Role sequence
**Hypothesis**: A single variation can target all eight aspirational criteria (C-09 through
C-16) by mapping each criterion to the smallest mechanism that satisfies it and composing
them in a single linear phase sequence with no redundancy:
- C-09: IA lens/expertise references team domain terms (enforced via profile derivation)
- C-10: CROSS-REF phase checks chart total vs file count (inherited from R2 V-05)
- C-11: VALIDATE phase gates all writes (inherited from R2 V-01)
- C-12: IA-phase completes before any standard/specialized role write (inherited from R2)
- C-13: headcount table is Phase 3 output, first artifact before any file write (R2 V-02)
- C-14: mandatory analytic prose after each table (R2 V-02)
- C-15: portrait self-check gate after IA phase (R3 V-01)
- C-16: PROFILE phase with three required fields gated before IA write (R3 V-02)

The composition hypothesis: these mechanisms are compatible in linear sequence; none conflict.
The complexity cost is a longer prompt, but each step is a named gate, making omissions
visible. If any single mechanism degrades under length pressure, the gate catches it.

---

You are running `corps-build`. Read org.yaml -- auto-detect in the current directory or use
the provided path.

Eight phases. Each gate must appear in output before the next phase begins. No file is
written before Phase 5.

---

### PHASE 1 -- PARSE

```
PARSE:
  org name: [name]
  groups: [list all Division and Group names]
  teams:
    [team name] (group: [parent]) -- std: [names], spec: [names]
  shared group roles: [list or "none"]
  exec office roles: [list or "none"]
  levels: [list or "not declared"]
  depth: [n]
  total slots: [n]
```

`PARSE-PASS: [n] teams, [n] slots.`
or `PARSE-FAIL: [error]. Halt.`

---

### PHASE 2 -- VALIDATE

**Entry**: PARSE-PASS. **No files written.**

```
VALIDATE:
  [V-1] every team has >= 1 role declared     PASS / FAIL -- teams with no roles: [list]
  [V-2] no std/spec collision per team         PASS / FAIL -- [team.role collisions]
  [V-3] no duplicate team names                PASS / FAIL -- duplicates: [list]
  [V-4] consistent level vocabulary            PASS / FAIL -- inconsistent pairs: [list]
```

`VALIDATE-PASS: 4/4 checks pass. No structural anomalies. Proceeding to PHASE 3.`
or `VALIDATE-FAIL: [n] error(s): [details]. No files written. Halt.`

---

### PHASE 3 -- BUILD CONTRACT (headcount table + analytic prose)

**Entry**: VALIDATE-PASS.
**This phase produces the first artifact -- the headcount table -- before any .craft/roles/ file.**

```markdown
## Headcount by Group/Area

| Area/Group | Headcount | Standard Roles | Specialized Roles | Levels |
|------------|-----------|----------------|-------------------|--------|
| [name]     | [n]       | [names]        | [names or --]     | [labels or --] |
| **Total**  | **[n]**   |                |                   |        |
```

Rules: one row per area, headcount = sum of all role slots for that area, Total = sum of area rows.

`TABLE-CLOSED: [n] area rows, [n] total headcount. Build contract established.
File generation must produce exactly [n] .craft/roles/ files.`

**Analytic prose (mandatory, 2-3 sentences):**
- Sentence 1: name the largest area and its headcount as a percentage of total
- Sentence 2: name the dominant level label, or note that most teams have no declared levels
- Sentence 3: any structural observation the table rows alone do not convey

Then:

```markdown
## Level Distribution

| Level  | Count | % of Org |
|--------|-------|----------|
| [label]| [n]   | [n]%     |
| **Total** | **[n]** | 100% |
```

After Level Distribution table: one sentence on seniority profile.

`CONTRACT-GATE: headcount table + analytic prose + level distribution written. Proceeding to PHASE 4.`

---

### PHASE 4 -- RESISTANCE PROFILES

**Entry**: CONTRACT-GATE.
**No files written during this phase.**
**No IA file may be written before PROFILE-COMPLETE.**

For every team in the headcount table, extract three fields:

```
PROFILE: [team name]
  defended-artifact:  [specific system, schema, pipeline, SLA, procedure -- not a category]
  change-pressure:    [specific migration, initiative, or architectural shift threatening
                      the defended artifact -- not a generic force]
  lens-phrase:        [5-10 words derived from defended-artifact + change-pressure; opens
                      the IA lens field verbatim; cannot be generic; cannot be written
                      without knowing both other fields]
```

After all profiles:

```
PROFILE-COMPLETE: [n of n] teams profiled.
  Lens phrases:
    [team]: "[phrase]"
    ...
```

Collision check: `LENS-COLLISION: [teams] -- "[phrase]". Revise one.` -- halt until resolved.

`PROFILE-GATE: all profiles complete with distinct lens phrases. Proceeding to PHASE 5.`

---

### PHASE 5 -- WRITE ROLE FILES

**Entry**: PROFILE-GATE.

Write in this strict sequence within each pass:

**5a -- PASS 1: All Inertia Advocate files (all teams before any other role)**

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields, populated from the resistance profile:

- **orientation**: from `defended-artifact` -- the rational perspective of the person who
  built or maintains it; names the specific concern; no generic stance toward stability
- **lens**: opens verbatim with the `lens-phrase` from Phase 4; expands in 2-3 sentences
  naming the specific domain slice monitored; no "stability," "institutional knowledge,"
  or phrases applicable to any team
- **expertise**: anchored to `defended-artifact`; names the specific system, schema, or
  procedure and related operational knowledge; differs from every other team's IA expertise
- **scope**: `standard -- present in all teams`
- **collaboration pattern**: forums (design review, sprint planning, architecture board),
  cadence, primary counterpart (the role most likely to propose the change-pressure
  initiative on this team)

No two IA files share identical `lens` or `expertise` text.

After each file:
```
IA-WRITTEN: [team]
  profile lens-phrase used: "[phrase]"
  lens-phrase appears verbatim: YES / NO
  expertise anchored to defended-artifact: YES / NO
```

Any NO -> rewrite that field before proceeding.

After all IA files, portrait self-check:

For each IA file, confirm:
- [ ] lens opens with the Phase 4 lens-phrase verbatim
- [ ] expertise names a concrete artifact (not a domain category)
- [ ] no generic resistance phrases present ("stability," "institutional knowledge,"
      "status quo," "existing processes" as unqualified terms)
- [ ] file could not be transplanted to a different team unchanged

```
PORTRAIT-CHECK: [n of n] IA files pass all four checks.
  Failures (if any): [team] -- [failed check] -- [rewrite applied]
```

`IA-PHASE-COMPLETE: [n of n] teams. All portraits verified. Standard and specialized
roles may now be written.`

---

**5b -- PASS 2: Standard role files (all teams)**

Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, no placeholder text, `scope: standard -- present in all teams`.

**5c -- PASS 3: Specialized role files (all teams)**

Path: `.craft/roles/{area-slug}/{role-slug}.md`
Five fields, no placeholder text, `scope: specialized -- [team name]`.

**5d -- Shared group roles** (if declared)

Path: `.craft/roles/{group-slug}/{role-slug}.md`, `scope: shared -- group: [name]`

**5e -- Exec office roles** (if declared)

Path: `.craft/roles/exec-office/{role-slug}.md`, `scope: exec office`

Standard vs. specialized must be explicit in `scope` -- not derivable from directory alone.
No placeholder text in any field.

After each team: `TEAM-WRITTEN: [team] -- 1 IA + [n] std + [n] spec.`

`ROLES-GATE: [n] written / [n] declared (TABLE-CLOSED). MATCH / MISMATCH.`
If MISMATCH: `ROLES-GATE-FAIL: missing: [list]. Halt.`

---

### PHASE 6 -- WRITE ORG-CHART.MD

**Entry**: ROLES-GATE MATCH.

org-chart.md sections in this order:

1. **ASCII hierarchy** -- box-drawing characters, minimum two nesting levels. Group names
   exactly as in org.yaml. Team leaf nodes show headcount.

2. **Headcount table** from Phase 3 (transcribe verbatim)

3. **Analytic prose** from Phase 3 (transcribe verbatim -- same sentences)

4. **Level Distribution** from Phase 3 (transcribe verbatim)

5. **Seniority sentence** from Phase 3 (transcribe)

6. **AMEND section**:
   ```markdown
   ## AMEND
   1. --area "[name]" -- regenerate area (resistance profile + IA + all roles + chart row).
      Available areas: [list from headcount table]
   2. --levels "[old]:[new]" -- replace level labels. Levels in use: [list]
   3. --restructure "[team] > [new-parent]" -- move team, rename directory, redraw diagram.
      Current nesting: [parent > child pairs, e.g. "Platform > Infrastructure, Platform > Reliability"]
   ```

`CHART-GATE: org-chart.md written with all sections. Proceeding to PHASE 7.`

---

### PHASE 7 -- CROSS-REFERENCE

**Entry**: CHART-GATE.

```
CROSS-REF:
  C1 -- TABLE-CLOSED contract vs .craft/roles/ file count
        contract: [TABLE-CLOSED n], files written: [ROLES-GATE n]
        result: MATCH / MISMATCH
        if MISMATCH: in contract not in files: [list]
                     in files not in contract: [list]

  C2 -- every team has an IA file
        teams: [n], IA files: [n] -- MATCH / MISMATCH
        if MISMATCH: teams missing IA: [list]

  C3 -- every area in headcount table has a .craft/roles/{area}/ directory
        table areas: [list], directories present: [list] -- MATCH / MISMATCH
        if MISMATCH: missing dirs: [list] / extra dirs: [list]

  C4 -- every IA lens opens with its Phase 4 lens-phrase
        [n of n] IA files verified -- MATCH / MISMATCH
        if MISMATCH: files with lens mismatch: [list]
```

All MATCH: `CROSS-REF-PASS: build consistent. All IA files derived from resistance profiles.`
Any MISMATCH: `CROSS-REF-FAIL: [details]. Build is not consistent.`

---

**FINAL SUMMARY**

```
CORPS-BUILD -- {date}
  validate:            PASS (4/4) -- no files written before validation
  headcount table:     written pre-roles (contract: [n] files, analytic prose: included)
  resistance profiles: [n of n] teams (defended-artifact + change-pressure + lens-phrase)
  IA phase:            [n of n] teams -- written from profiles; portrait self-check [n/n] pass
  standard roles:      [n]
  specialized roles:   [n]
  shared group roles:  [n]
  exec office roles:   [n]
  total files:         [n] written / [n] declared -- MATCH / MISMATCH
  org-chart.md:        written (diagram + tables + prose + level dist + AMEND)
  cross-ref:           PASS / FAIL (IA lenses traced to profiles: YES / NO)
  status:              COMPLETE / INCOMPLETE
```

Generated by: corps-build -- {date}

---

## Variation Summary

| Var | Axis | Key Hypothesis | Criteria Targeted | R2 Predecessor |
|-----|------|----------------|-------------------|----------------|
| **V-01** | Inertia framing | Portrait standard + transplant-test annotation makes generic language visible inline | C-15 | Extends V-03(R2) example approach |
| **V-02** | Lifecycle emphasis | 3-field PROFILE phase (defended-artifact + change-pressure + derived lens-phrase) gated before IA write makes C-16 pass by construction | C-16 | Tightens V-04(R2) profile fields to match C-16 exactly |
| **V-03** | Phrasing register | Output-forward derivation chain (showing how profile fields flow to IA file fields, with annotated examples) produces better compliance than imperatives | C-15, C-16 | New axis extending V-03(R2) |
| **V-04** | Inertia + Lifecycle | Explicit derivation table (profile field -> IA file field) + portrait self-check gate makes C-15+C-16 one construction pipeline | C-15, C-16 | Combines V-03(R2) + V-02(R2) under R3 bar |
| **V-05** | All axes | All eight aspirational criteria in one linear phase sequence; each criterion mapped to minimal dedicated mechanism; no criterion requires another to be present | C-09 through C-16 | Synthesizes R2 V-05 + R3 V-01 + R3 V-02 |

**Single-axis axes used**: inertia framing (V-01), lifecycle emphasis (V-02), phrasing register (V-03).

**Combination axes**: V-04 = inertia framing + lifecycle; V-05 = inertia + lifecycle + output format + role sequence.

**Predicted rubric v3 sensitivity**:
- V-01 is the strongest single bet for C-15 (portrait standard is the structural centerpiece; transplant test is an inline gate)
- V-02 is the strongest single bet for C-16 (3-field profile with derivation requirement; PROFILE-COMPLETE gate before any IA write)
- V-03 may produce the highest C-15 quality by showing the derivation chain rather than requiring it (model sees the expected output, not just the rule)
- V-04 targets the C-15/C-16 pair as a single mechanism; derivation table makes the connection explicit; portrait self-check adds a batch verification at phase end
- V-05 is the only variation targeting C-09 through C-16 together -- highest ceiling for composite score; risk is that phase count (8) creates compression pressure on output quality in individual phases
