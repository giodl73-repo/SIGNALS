# /quest:variate — org-build Round 3

## Variation Map

| ID | Axis (Primary) | Axis (Secondary) | Hypothesis |
|----|---------------|-----------------|------------|
| V-01 | Inertia framing | — | Centering every phase on the IA verdict makes C-08/C-11/C-13/C-15/C-17 impossible to skip — no phase completes without the verdict present |
| V-02 | Lifecycle emphasis | — | Formal named typed I/O contracts at every gate boundary make C-14 natural and scaffold C-11/C-15 because downstream phases must declare what they consume |
| V-03 | Output format | — | Declaring every table schema before writing content forces C-05/C-07/C-10 because the agent cannot omit a column it has already contracted |
| V-04 | Phrasing register | Lifecycle emphasis | FORBIDDEN/MUST throughout paired with explicit phase gates converts all correctness criteria into hard parse failures, not judgment calls |
| V-05 | Role sequence | Inertia framing | Sequencing structural verdict → IA role → all other roles chains C-08 into C-11/C-17, making verbatim scope application the natural path |

---

## V-01 — Single-axis: Inertia Framing

**Axis:** The IA assessment is produced first and every downstream section either prepares for or derives from the structural verdict.

**Hypothesis:** Centering every phase on the IA verdict makes C-08, C-11, C-13, C-15, and C-17 impossible to skip — no phase completes without the verdict present.

---

```
You are running /org-build. Generate a complete organizational structure for this
codebase or team. Every section of your output is anchored to a single structural
verdict you produce in Phase 1. Do not proceed past any phase until that phase's
output is written.

---

## Phase 1 — Structural Verdict (ANCHOR)

Examine the scan results or repository. Rate the flat-case pressure and issue a
structural verdict. Both outputs are recorded now and referenced in every later phase.

**FLAT-CASE-PRESSURE** — choose exactly one:
- LOW:    Scale pressures dominate. Flat operation is visibly strained.
- MEDIUM: Mixed signals. Flat is workable but accumulating friction.
- HIGH:   Flat case is strong. Adding structure requires active justification.

**Structural verdict** — choose exactly one:
- CAN-OPERATE-FLAT:    The team can execute without a hierarchy layer.
- STRUCTURE-WARRANTED: Scale, coordination cost, or accountability gaps require hierarchy.

Write this block in org-chart.md now:

```
FLAT-CASE-PRESSURE: {value}
{verdict}

Only one verdict is valid. Both is an error. Neither is an error.
```

Immediately after the verdict, write the category exclusion contract:

```
IF CAN-OPERATE-FLAT    → FORBIDDEN in Anti-Pattern Watch: cat-1, cat-4
IF STRUCTURE-WARRANTED → FORBIDDEN in Anti-Pattern Watch: cat-2, cat-3
```

---

## Phase 2 — Inertia-Advocate Role

Input: FLAT-CASE-PRESSURE from Phase 1.

Select the scope template for the rated pressure level. Apply it verbatim to the
scope field — no paraphrase, no adaptation, no summarization. The template text exactly.

**Scope templates:**

FLAT-CASE-PRESSURE = LOW:
  scope: >
    Track adoption signals. Flag resistance patterns in the first sprint.
    Escalate when resistance exceeds 15% of affected stakeholders.

FLAT-CASE-PRESSURE = MEDIUM:
  scope: >
    Lead structured objection sessions before each structural decision gate.
    Maintain a written objection registry with owner and resolution date.
    Escalate unresolved blockers within 5 business days.

FLAT-CASE-PRESSURE = HIGH:
  scope: >
    Own the flat-case rebuttal track. Produce stakeholder impact map, objection
    registry, and resolution playbook before any structural decision proceeds.
    Escalate to steering committee if a structural decision moves forward without
    documented IA sign-off.

Create .roles/governance/inertia-advocate.md:

```yaml
orientation: [role orientation]
lens:        [role lens]
expertise:   [role expertise]
scope:       [verbatim template text — do not modify]
collaborates_with:
  - [role]
```

---

## Phase 3 — org-chart.md (Remaining Sections)

The verdict block from Phase 1 is already written. Complete these sections in order:

**ASCII Hierarchy**
Box-and-line diagram with minimum 2 organizational levels.
A flat list of names without visual hierarchy fails.

**Headcount by Area**

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

All five columns required. Omitting Decides or Escalates fails.

**Anti-Pattern Watch**

Constraint: do not select any category named in the Phase 1 exclusion contract.

| Pattern | Why It Applies Here | Mitigation |
|---------|---------------------|------------|

- "Why It Applies Here": every cell opens with `[element name] (cat-N) —` then explanation
- "Mitigation": specific remediation action (not format guidance, not column instructions)

Category selection must be consistent with the Phase 1 verdict:
- CAN-OPERATE-FLAT    → cat-2, cat-3 only
- STRUCTURE-WARRANTED → cat-1, cat-4 only

**Org Evolution Roadmap**

| Trigger | Type | Structural Response |
|---------|------|---------------------|

Minimum 2 rows. Row 1: headcount threshold trigger. Row 2: a different trigger
category (not headcount).

**Operating Rhythm**

Table with minimum 3 distinct cadences: ROB, shiproom, and governance.

Charter per governance meeting — all six fields required:

| Field        | Value  |
|--------------|--------|
| Name         |        |
| Frequency    |        |
| Owner        |        |
| Participants |        |
| Quorum       | N of M |
| Decisions    |        |

Quorum must be expressed as a fraction (e.g., 3 of 5). "Majority" or "consensus" fails.

---

## Phase 4 — Remaining Role Files

Input: structural verdict and pressure level from Phase 1.

Generate all role files except inertia-advocate (already written in Phase 2).

Depth targets:
- Standard:          20-30 roles total including IA
- --depth deep:      50+ roles total including IA

Organize under .roles/{area}/ with minimum 2 area subdirectories.

Every .roles/{area}/{role}.md requires exactly these five fields:

```yaml
orientation: ...
lens:        ...
expertise:   ...
scope:       ...
collaborates_with:
  - ...
```

A file missing any field fails. Do not rewrite the inertia-advocate scope.
```

---

## V-02 — Single-axis: Lifecycle Emphasis

**Axis:** Every phase is a formal gate with named typed input variables and named typed output variables. A phase does not begin until its input contract is satisfied.

**Hypothesis:** Explicit named typed variables at gate boundaries make C-14 natural and scaffold C-11/C-15 because the data contract forces the verdict to be named before it can be consumed downstream.

---

```
You are running /org-build. Execute in four phases. Each phase declares an input
contract and produces named typed output variables. A phase does not begin until
all variables in its input contract are available.

---

## Phase 1 — Structural Assessment

Input contract: scan results or repository contents.

Examine team size, coordination overhead, and accountability clarity. Assign:

**T1-PRESSURE** (one of: LOW | MEDIUM | HIGH)
- LOW:    Scale pressures dominate; flat operation is visibly strained
- MEDIUM: Mixed signals; flat is workable with accumulating friction
- HIGH:   Flat case is strong; hierarchy requires active justification

**T1-VERDICT** (one of: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED)
- CAN-OPERATE-FLAT:    team can execute without a hierarchy layer
- STRUCTURE-WARRANTED: scale, coordination cost, or accountability gaps require hierarchy

**T1-EXCLUSIONS** (derived from T1-VERDICT):
- T1-VERDICT = CAN-OPERATE-FLAT    → T1-EXCLUSIONS = {cat-1, cat-4}
- T1-VERDICT = STRUCTURE-WARRANTED → T1-EXCLUSIONS = {cat-2, cat-3}

**Guard:** T1-VERDICT accepts exactly one value. Both assigned is an error.
Neither assigned is an error.

Write in org-chart.md:
```
FLAT-CASE-PRESSURE: {T1-PRESSURE}
{T1-VERDICT}

Only one verdict is valid. Both is an error. Neither is an error.

FORBIDDEN in Anti-Pattern Watch for this org: {T1-EXCLUSIONS}
```

**Gate output — available to all downstream phases:**
- T1-PRESSURE:   {LOW | MEDIUM | HIGH}
- T1-VERDICT:    {CAN-OPERATE-FLAT | STRUCTURE-WARRANTED}
- T1-EXCLUSIONS: {cat set}

---

## Phase 2 — Inertia-Advocate Role File

Input contract: T1-PRESSURE (must be set by Phase 1).

Select the scope template keyed to T1-PRESSURE. The scope field receives the
verbatim template text. No paraphrase. No adaptation. The exact text.

Scope templates by T1-PRESSURE:

LOW:
  > Track adoption signals. Flag resistance patterns in the first sprint.
    Escalate when resistance exceeds 15% of affected stakeholders.

MEDIUM:
  > Lead structured objection sessions before each structural decision gate.
    Maintain a written objection registry with owner and resolution date.
    Escalate unresolved blockers within 5 business days.

HIGH:
  > Own the flat-case rebuttal track. Produce stakeholder impact map, objection
    registry, and resolution playbook before any structural decision proceeds.
    Escalate to steering committee if a structural decision moves forward without
    documented IA sign-off.

Create .roles/governance/inertia-advocate.md with fields:
orientation, lens, expertise, scope (verbatim template), collaborates_with.

**Gate output:**
- T2-IA-ROLE-PATH:     .roles/governance/inertia-advocate.md
- T2-IA-SCOPE-SOURCE:  {LOW | MEDIUM | HIGH}  (equals T1-PRESSURE)

---

## Phase 3 — org-chart.md (Remaining Sections)

Input contract: T1-PRESSURE, T1-VERDICT, T1-EXCLUSIONS (all from Phase 1).

The verdict block is already written. Complete these sections:

**ASCII Hierarchy:** Box-and-line diagram, minimum 2 levels.

**Headcount by Area:** Table with columns Area | Headcount | Key Roles | Decides | Escalates.

**Anti-Pattern Watch:**
Input contract: T1-EXCLUSIONS must be set. Do not select any category in T1-EXCLUSIONS.

Table with columns: Pattern | Why It Applies Here | Mitigation
- "Why It Applies Here": `[element name] (cat-N) —` + explanation
- "Mitigation": specific remediation action (not format guidance)

Permitted categories:
- T1-VERDICT = CAN-OPERATE-FLAT    → use cat-2, cat-3
- T1-VERDICT = STRUCTURE-WARRANTED → use cat-1, cat-4

**Org Evolution Roadmap:** Trigger | Type | Structural Response
- Row 1: headcount threshold trigger
- Row 2: different trigger category (not headcount)

**Operating Rhythm:**
Table with minimum 3 rows (ROB, shiproom, governance).
Charter per governance meeting: Name | Frequency | Owner | Participants | Quorum | Decisions
Quorum as N of M fraction.

**Gate output:**
- T3-CHART-COMPLETE:   true
- T3-CATEGORIES-USED:  {cat values appearing in Anti-Pattern Watch}

---

## Phase 4 — Role Files

Input contract: T1-VERDICT, T1-PRESSURE, T2-IA-ROLE-PATH (all must be set before
this phase begins).

Generate all remaining role files. Do not regenerate inertia-advocate (T2-IA-ROLE-PATH
is the canonical source).

Depth targets:
- Standard:     19-29 additional files (total 20-30 with IA)
- --depth deep: 49+ additional files (total 50+ with IA)

File location: .roles/{area}/{role}.md
Minimum 2 area subdirectories.

Every file requires exactly five fields: orientation, lens, expertise, scope,
collaborates_with. A file missing any field fails.

**Gate output:**
- T4-ROLE-COUNT:  {n}
- T4-AREA-DIRS:   {list of area directory names}
```

---

## V-03 — Single-axis: Output Format

**Axis:** All output schemas are declared as contracts before any content is generated. Every table is defined by its column contract first; content fills the schema second.

**Hypothesis:** Declaring column contracts before writing forces C-05, C-07, and C-10 because the agent cannot omit a column it has already contracted — the schema becomes an incomplete checklist until every field is populated.

---

```
You are running /org-build. Before generating any content, this prompt declares
the complete output schema for every artifact. You then fill each section in
declared order. A section is not complete until every field in its schema is populated.

---

## Output Schema Declaration

### Artifact A: org-chart.md

Section A1 — ASCII Hierarchy
  Required: box-and-line diagram with minimum 2 organizational levels
  Failure: flat list of names without a visual hierarchy

Section A2 — Headcount by Area
  Required columns: Area | Headcount | Key Roles | Decides | Escalates
  Failure: missing Decides column; missing Escalates column

Section A3 — Structural Verdict Block
  Required fields:
    - FLAT-CASE-PRESSURE label and rated value
    - verdict value (exactly one of CAN-OPERATE-FLAT | STRUCTURE-WARRANTED)
    - single-verdict guard statement (verbatim: "Only one verdict is valid.
      Both is an error. Neither is an error.")
    - category exclusion declaration (states FORBIDDEN categories per verdict path)
  Failure: missing guard; missing exclusion; multiple verdict values

Section A4 — Anti-Pattern Watch
  Required columns: Pattern | Why It Applies Here | Mitigation
  "Why It Applies Here" schema: `[element name] (cat-N) —` followed by explanation
  "Mitigation" schema: specific remediation action (imperative verb phrase)
  Failure: "Why It Applies Here" lacks cat-N prefix; Mitigation contains format
    guidance or column descriptions instead of a remediation action

Section A5 — Org Evolution Roadmap
  Required columns: Trigger | Type | Structural Response
  Row 1 schema: headcount threshold trigger
  Row 2 schema: non-headcount trigger category
  Failure: all rows are headcount thresholds

Section A6 — Operating Rhythm
  Required rows: ROB, shiproom, governance (minimum 3 distinct cadences)
  Charter schema per governance meeting:
    Name | Frequency | Owner | Participants | Quorum | Decisions
  Quorum schema: N of M fraction (example: 3 of 5)
  Failure: Quorum expressed as qualitative term; missing charter field

### Artifact B: .roles/{area}/{role}.md

File schema (required in every file):
  orientation:       string
  lens:              string
  expertise:         string
  scope:             string
  collaborates_with: list

Count schema:
  Standard:          20-30 files
  --depth deep:      50+ files

Layout schema:
  Minimum 2 area subdirectories under .roles/

Inertia-advocate scope schema (override):
  The scope field contains verbatim text from the pressure-level template.
  No paraphrase. No adaptation. Verbatim.

---

## Step 1 — Structural Verdict

Fill Section A3 now.

Rate FLAT-CASE-PRESSURE (one of: LOW | MEDIUM | HIGH):
- LOW:    scale pressures dominate; flat operation is strained
- MEDIUM: flat is workable with accumulating friction
- HIGH:   flat case is strong; hierarchy needs justification

Issue structural verdict (one of: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED).

Write in org-chart.md:

```
FLAT-CASE-PRESSURE: {value}
{verdict}

Only one verdict is valid. Both is an error. Neither is an error.

IF CAN-OPERATE-FLAT    → FORBIDDEN in Anti-Pattern Watch: cat-1, cat-4
IF STRUCTURE-WARRANTED → FORBIDDEN in Anti-Pattern Watch: cat-2, cat-3
```

Section A3 is now complete.

---

## Step 2 — IA Scope Template Selection

This step prepares the verbatim scope text before writing the role file.
Record the selected template text; it will be pasted unchanged in Step 3.

Pressure-level templates:

LOW:
  Track adoption signals. Flag resistance patterns in the first sprint.
  Escalate when resistance exceeds 15% of affected stakeholders.

MEDIUM:
  Lead structured objection sessions before each structural decision gate.
  Maintain a written objection registry with owner and resolution date.
  Escalate unresolved blockers within 5 business days.

HIGH:
  Own the flat-case rebuttal track. Produce stakeholder impact map, objection
  registry, and resolution playbook before any structural decision proceeds.
  Escalate to steering committee if a structural decision moves forward without
  documented IA sign-off.

Selected template (record): {text of applicable template}

---

## Step 3 — ASCII Hierarchy

Fill Section A1. Draw box-and-line diagram. Minimum 2 levels.
Section A1 is complete when the diagram is present with visible hierarchy.

---

## Step 4 — Headcount by Area

Fill Section A2. All five columns required.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

Section A2 is complete when all five columns are populated for every area.

---

## Step 5 — Anti-Pattern Watch

Fill Section A4. Respect the FORBIDDEN category set from Step 1.

| Pattern | Why It Applies Here | Mitigation |
|---------|---------------------|------------|

Schema compliance check before writing each row:
- Does "Why It Applies Here" open with `[element name] (cat-N) —`? If not, rewrite.
- Does "Mitigation" contain a specific action verb phrase? If not, rewrite.
- Is the cat-N value excluded by the Step 1 contract? If so, replace.

Section A4 is complete when all rows pass schema compliance.

---

## Step 6 — Org Evolution Roadmap

Fill Section A5.

| Trigger | Type | Structural Response |
|---------|------|---------------------|

Schema compliance: Row 1 is headcount threshold. Row 2 is a different type.
Section A5 is complete when minimum 2 rows are present and row types are distinct.

---

## Step 7 — Operating Rhythm

Fill Section A6.

Rhythm table (minimum 3 rows: ROB, shiproom, governance).

Charter table per governance meeting (all six fields required):

| Field        | Value  |
|--------------|--------|
| Name         |        |
| Frequency    |        |
| Owner        |        |
| Participants |        |
| Quorum       | N of M |
| Decisions    |        |

Section A6 is complete when all charters have all six fields and Quorum is a fraction.

---

## Step 8 — Inertia-Advocate Role File

Fill Artifact B schema for inertia-advocate.

Location: .roles/governance/inertia-advocate.md

scope: {paste template selected in Step 2 — verbatim, unchanged}

All five fields required. Section complete when all five fields are present and scope
matches the Step 2 template exactly.

---

## Step 9 — Remaining Role Files

Fill Artifact B schema for all other roles.

- Do not regenerate inertia-advocate (Step 8 is canonical)
- Standard: 19-29 additional files (total 20-30)
- Deep (--depth deep): 49+ additional files (total 50+)
- Minimum 2 area subdirectories
- All five fields required per file

Schema compliance check: after generating, count files and list area subdirs.
If count is below lower bound, add roles. If area dirs < 2, reorganize.
```

---

## V-04 — Combined: Phrasing Register × Lifecycle Emphasis

**Axes:** FORBIDDEN/MUST imperative language throughout + explicit named typed output variables at every phase gate.

**Hypothesis:** Pairing hard-stop imperative language with formal typed gate contracts eliminates the two most common failure modes: constraint ambiguity (solved by FORBIDDEN/MUST) and implicit data flow (solved by named typed variables). Together they should close C-02, C-03, C-10, C-13, C-14, C-15, C-16, C-17.

---

```
You are running /org-build. All constraints in this prompt are imperative.
FORBIDDEN means the output is invalid. MUST means the output is incomplete without it.
Execute in four phases. Each phase records named typed output variables consumed
by downstream phases. A phase MUST NOT begin without its declared inputs.

---

## Phase 1 — Structural Assessment

Input contract: scan results or repository contents.

MUST: assign exactly one value to T1-PRESSURE (LOW | MEDIUM | HIGH).
FORBIDDEN: assigning multiple values to T1-PRESSURE.

MUST: issue exactly one structural verdict (CAN-OPERATE-FLAT | STRUCTURE-WARRANTED).
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED.

MUST: derive T1-EXCLUSIONS from T1-VERDICT:
  T1-VERDICT = CAN-OPERATE-FLAT    → T1-EXCLUSIONS = {cat-1, cat-4}
  T1-VERDICT = STRUCTURE-WARRANTED → T1-EXCLUSIONS = {cat-2, cat-3}

MUST: write this block in org-chart.md:
```
FLAT-CASE-PRESSURE: {T1-PRESSURE}
{T1-VERDICT}

Only one verdict is valid. Both is an error. Neither is an error.

FORBIDDEN in Anti-Pattern Watch for this org: {T1-EXCLUSIONS}
```

Gate outputs (MUST be recorded before Phase 2 begins):
  T1-PRESSURE:   {LOW | MEDIUM | HIGH}
  T1-VERDICT:    {CAN-OPERATE-FLAT | STRUCTURE-WARRANTED}
  T1-EXCLUSIONS: {cat set}

---

## Phase 2 — Inertia-Advocate Role File

Input contract: T1-PRESSURE (MUST be set by Phase 1).

MUST: select the scope template keyed to T1-PRESSURE.
FORBIDDEN: paraphrasing the scope template.
FORBIDDEN: adapting or summarizing the scope template.
MUST: copy the exact template text into the scope field — no modifications.

Scope templates:

T1-PRESSURE = LOW:
  > Track adoption signals. Flag resistance patterns in the first sprint.
    Escalate when resistance exceeds 15% of affected stakeholders.

T1-PRESSURE = MEDIUM:
  > Lead structured objection sessions before each structural decision gate.
    Maintain a written objection registry with owner and resolution date.
    Escalate unresolved blockers within 5 business days.

T1-PRESSURE = HIGH:
  > Own the flat-case rebuttal track. Produce stakeholder impact map, objection
    registry, and resolution playbook before any structural decision proceeds.
    Escalate to steering committee if a structural decision moves forward without
    documented IA sign-off.

MUST: create .roles/governance/inertia-advocate.md.
FORBIDDEN: omitting the inertia-advocate role.

MUST: include all five fields in inertia-advocate.md:
  orientation, lens, expertise, scope, collaborates_with.
FORBIDDEN: any field absent.

Gate outputs:
  T2-IA-ROLE-PATH:    .roles/governance/inertia-advocate.md
  T2-IA-SCOPE-SOURCE: {LOW | MEDIUM | HIGH}

---

## Phase 3 — org-chart.md (Remaining Sections)

Input contract: T1-PRESSURE, T1-VERDICT, T1-EXCLUSIONS (MUST all be set by Phase 1).

**ASCII Hierarchy:**
MUST: include a box-and-line diagram with minimum 2 organizational levels.
FORBIDDEN: a flat list of names without hierarchical visual structure.

**Headcount by Area:**
MUST: include table with columns Area, Headcount, Key Roles, Decides, Escalates.
FORBIDDEN: omitting the Decides column.
FORBIDDEN: omitting the Escalates column.

**Anti-Pattern Watch:**
Input contract: T1-EXCLUSIONS (MUST be set).

MUST: table has columns Pattern, Why It Applies Here, Mitigation.
MUST: every "Why It Applies Here" cell opens with `[element name] (cat-N) —`
FORBIDDEN: "Why It Applies Here" cells that lack the cat-N citation prefix.
FORBIDDEN: selecting any category in T1-EXCLUSIONS.
MUST: every Mitigation cell contains a specific remediation action.
FORBIDDEN: Mitigation cells that contain format guidance.
FORBIDDEN: Mitigation cells that describe column structure.

Anti-pattern category alignment (MUST apply):
  T1-VERDICT = CAN-OPERATE-FLAT    → MUST use cat-2, cat-3; FORBIDDEN: cat-1, cat-4
  T1-VERDICT = STRUCTURE-WARRANTED → MUST use cat-1, cat-4; FORBIDDEN: cat-2, cat-3

**Org Evolution Roadmap:**
MUST: table has columns Trigger, Type, Structural Response.
MUST: row 1 is a headcount threshold trigger.
MUST: row 2 is a different trigger type.
FORBIDDEN: all rows being headcount thresholds.

**Operating Rhythm:**
MUST: include minimum 3 cadences (ROB, shiproom, governance).
MUST: each governance cadence has a charter with fields
  Name, Frequency, Owner, Participants, Quorum, Decisions.
MUST: Quorum expressed as N of M fraction.
FORBIDDEN: Quorum expressed as "majority", "consensus", or any qualitative term.

Gate outputs:
  T3-CHART-COMPLETE:   true
  T3-CATEGORIES-USED:  {cat values in Anti-Pattern Watch}

---

## Phase 4 — Role Files

Input contract: T1-VERDICT, T1-PRESSURE, T2-IA-ROLE-PATH (MUST all be set).

MUST: generate role files for all roles except inertia-advocate (at T2-IA-ROLE-PATH).
FORBIDDEN: regenerating the inertia-advocate role in Phase 4.

MUST: every .roles/{area}/{role}.md contains all five fields:
  orientation, lens, expertise, scope, collaborates_with.
FORBIDDEN: any file missing any of the five fields.

MUST: standard depth produces 20-30 total roles (including IA from Phase 2).
FORBIDDEN: standard depth producing fewer than 20 total roles.
FORBIDDEN: standard depth producing more than 36 total roles.
MUST: --depth deep produces 50+ total roles.

MUST: roles organized under minimum 2 area subdirectories.
FORBIDDEN: all roles in a single flat directory under .roles/.

Gate outputs:
  T4-ROLE-COUNT: {n}
  T4-AREA-DIRS:  {list}
```

---

## V-05 — Combined: Role Sequence × Inertia Framing

**Axes:** Role sequence (verdict before all roles; IA role before all other roles) + inertia framing (IA verdict is the explicit dependency that gates the IA scope template selection).

**Hypothesis:** Sequencing structural verdict → IA role → all other roles chains C-08 into C-11/C-17 because the IA scope template cannot be selected until T1-PRESSURE is known, making verbatim copy the natural path. Generating IA before other roles prevents scope drift because the template decision is isolated before the workload expands.

---

```
You are running /org-build. The execution sequence below is strict. The structural
verdict gates all role generation. The inertia-advocate role is generated second —
after the verdict and before every other role — because its scope field is derived
from the verdict. All other roles come last.

---

## Execution Sequence

```
[A] Structural Verdict
      ↓ T1-PRESSURE, T1-VERDICT available
[B] Inertia-Advocate Role
      ↓ T2-IA-SCOPE-APPLIED = true
[C] org-chart.md (remaining sections)
      ↓ T3-CHART-COMPLETE = true
[D] All Remaining Role Files
```

Sequence is enforced: B does not begin without A complete. D does not begin without B complete.

---

## [A] Structural Verdict

Examine the scan results or repository. Assign exactly one value to each output:

**T1-PRESSURE** (LOW | MEDIUM | HIGH):
- LOW:    scale pressures dominate; flat operation visibly strained
- MEDIUM: flat workable with accumulating friction
- HIGH:   flat case is strong; hierarchy requires justification

**T1-VERDICT** (CAN-OPERATE-FLAT | STRUCTURE-WARRANTED):
- CAN-OPERATE-FLAT:    team can execute without a hierarchy layer
- STRUCTURE-WARRANTED: scale, coordination cost, or accountability gaps require hierarchy

Guard: Only one verdict. Both is an error. Neither is an error.

Write in org-chart.md:
```
FLAT-CASE-PRESSURE: {T1-PRESSURE}
{T1-VERDICT}

Only one verdict is valid. Both is an error. Neither is an error.

IF CAN-OPERATE-FLAT    → FORBIDDEN in Anti-Pattern Watch: cat-1, cat-4
IF STRUCTURE-WARRANTED → FORBIDDEN in Anti-Pattern Watch: cat-2, cat-3
```

Record: A complete. T1-PRESSURE={value}. T1-VERDICT={value}.

---

## [B] Inertia-Advocate Role

This step runs before any other role file is created.

Input: T1-PRESSURE from [A].

Locate the scope template for the T1-PRESSURE level. The scope field receives the
template text exactly — not adapted, not summarized, not paraphrased. The template text.

Scope templates:

T1-PRESSURE = LOW:
  > Track adoption signals. Flag resistance patterns in the first sprint.
    Escalate when resistance exceeds 15% of affected stakeholders.

T1-PRESSURE = MEDIUM:
  > Lead structured objection sessions before each structural decision gate.
    Maintain a written objection registry with owner and resolution date.
    Escalate unresolved blockers within 5 business days.

T1-PRESSURE = HIGH:
  > Own the flat-case rebuttal track. Produce stakeholder impact map, objection
    registry, and resolution playbook before any structural decision proceeds.
    Escalate to steering committee if a structural decision moves forward without
    documented IA sign-off.

Create .roles/governance/inertia-advocate.md now, before any other role file:

```yaml
orientation:       [role orientation]
lens:              [role lens]
expertise:         [role expertise]
scope:             [exact template text for T1-PRESSURE — no changes]
collaborates_with:
  - [role]
```

All five fields required. Scope is the template. Nothing else.

Record: B complete. T2-IA-SCOPE-APPLIED=true. Template level: {T1-PRESSURE}.

---

## [C] org-chart.md (Remaining Sections)

The verdict block from [A] is already written. Complete these sections:

**ASCII Hierarchy**
Box-and-line diagram. Minimum 2 organizational levels. No flat name lists.

**Headcount by Area**
Table: Area | Headcount | Key Roles | Decides | Escalates
All five columns required.

**Anti-Pattern Watch**
Input: T1-VERDICT exclusion from [A]. Do not select excluded categories.

Table: Pattern | Why It Applies Here | Mitigation
- "Why It Applies Here": `[element name] (cat-N) —` then explanation
- "Mitigation": specific remediation action (not format guidance)

Category alignment with T1-VERDICT:
- CAN-OPERATE-FLAT    → cat-2, cat-3 permitted; cat-1, cat-4 FORBIDDEN
- STRUCTURE-WARRANTED → cat-1, cat-4 permitted; cat-2, cat-3 FORBIDDEN

**Org Evolution Roadmap**
Table: Trigger | Type | Structural Response
Row 1: headcount threshold trigger. Row 2: different trigger type.

**Operating Rhythm**
Table with minimum 3 cadences: ROB, shiproom, governance.
Charter per governance meeting — all six fields required:

| Field        | Required Format |
|--------------|-----------------|
| Name         | string          |
| Frequency    | string          |
| Owner        | role name       |
| Participants | role list       |
| Quorum       | N of M fraction |
| Decisions    | string list     |

Record: C complete. T3-CHART-COMPLETE=true.

---

## [D] All Remaining Role Files

Input: [A] and [B] must be recorded complete before this step begins.

Generate all roles except inertia-advocate (already written in [B]).

Role generation order (recommended):
1. Leadership / executive layer roles
2. Core delivery area roles (aligned to org structure in [C])
3. Cross-cutting / platform roles
4. Specialist / embedded roles

Depth targets:
- Standard:     19-29 additional files (total 20-30 including IA)
- --depth deep: 49+ additional files (total 50+ including IA)

File location: .roles/{area}/{role}.md
Minimum 2 area subdirectories.

Every file — five fields required:
  orientation, lens, expertise, scope, collaborates_with

Do not reference or rewrite the inertia-advocate scope. [B] is canonical.

Record: D complete. T4-ROLE-COUNT={n}. T4-AREA-DIRS={list}.
```

---

## Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 ASCII hierarchy | explicit | explicit | schema declared | MUST | explicit |
| C-02 five role fields | Phase 4 | Phase 4 | schema declared | MUST/FORBIDDEN | [D] |
| C-03 IA always present | Phase 2 | Phase 2 | Step 8 | MUST/FORBIDDEN | [B] |
| C-04 role count | Phase 4 | Phase 4 | schema declared | MUST/FORBIDDEN | [D] |
| C-05 headcount table | Phase 3 schema | Phase 3 schema | schema declared | MUST/FORBIDDEN | [C] |
| C-06 area subdirs | Phase 4 | Phase 4 | schema declared | MUST/FORBIDDEN | [D] |
| C-07 rhythm + charters | Phase 3 | Phase 3 | Section A6 schema | MUST | [C] |
| C-08 verdict + pressure | Phase 1 anchor | T1 gate | Step 1 | MUST | [A] anchor |
| C-09 roadmap typed triggers | Phase 3 | Phase 3 | Section A5 schema | MUST | [C] |
| C-10 cat-N citations | Phase 3 | Phase 3 | Section A4 schema | MUST/FORBIDDEN | [C] |
| C-11 IA scope from pressure | Phase 2 template | T2 gate | Step 2 template | MUST | [B] template |
| C-12 categories from verdict | Phase 3 exclusion | T1-EXCLUSIONS | Step 5 | MUST | [C] |
| C-13 single-verdict guard | Phase 1 verbatim | Phase 1 verbatim | Step 1 verbatim | MUST | [A] verbatim |
| C-14 named typed outputs | implicit | explicit gates | implicit | explicit gates | typed records |
| C-15 bidirectional guard | Phase 1 "neither" | Phase 1 "neither" | Step 1 "neither" | FORBIDDEN both + neither | [A] "neither" |
| C-16 mitigation = actions | Phase 3 note | Phase 3 note | schema contract | FORBIDDEN | [C] note |
| C-17 scope verbatim | Phase 2 "no paraphrase" | Phase 2 "exact text" | schema override | FORBIDDEN paraphrase | [B] "no changes" |
| C-18 exclusion FORBIDDEN sets | Phase 1 IF→FORBIDDEN | T1-EXCLUSIONS | Step 1 FORBIDDEN | FORBIDDEN per path | [A] FORBIDDEN |
