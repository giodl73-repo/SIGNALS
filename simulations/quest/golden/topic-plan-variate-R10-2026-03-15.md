# topic-plan Skill Variations — Round 10 (2026-03-15)

Rubric: v10 (C-01–C-35, max 100)
New criterion this round: C-35 (Upfront table schema register — dedicated TABLE SCHEMAS
section before Phase 0, naming all schemas with column structure, mandatory labels, and
sentinel usage as a pre-phase declared contract)

---

## Round 10 Design Notes

R9 surfaced one new structural pattern not yet captured in the rubric:

**C-35 from prior V-02 (R9)** — V-02's TABLE SCHEMAS section declared all schemas before
Phase 0, but the criterion formalizes a stricter requirement: a **dedicated TABLE SCHEMAS
section** with **named schema identifiers** (Schema A, Schema B, etc.) must appear before
Phase 0 and before any artifact read, committing:
- Column structure (full header row per schema)
- Mandatory column labels (which columns may not be omitted)
- Sentinel token usage rules per schema

A skill where table schemas are defined inline within phase descriptions fails C-35
even if every mandatory column is present and correctly labeled. Inline definition is
not a pre-phase declared contract — it is emergent schema definition, and it cannot be
audited for completeness before phase execution begins.

**Previous round gap analysis:**

| Gap | Description | R10 fix |
|-----|-------------|---------|
| C-35 missing | Table schemas defined inline within phase instructions rather than in a dedicated pre-Phase-0 TABLE SCHEMAS section; no named schema identifiers assigned | All five R10 designs declare a dedicated TABLE SCHEMAS section before Phase 0, assign Schema IDs (Schema A through Schema D), and declare mandatory columns and sentinel rules per schema |

**Round 10 single-axis and combined choices:**

| Variation | Axis | Primary mechanism |
|-----------|------|-------------------|
| V-01 | Output format | Two-level schema presentation: compact register table (Schema ID / Name / Phase Used / Mandatory Columns) + expanded schema blocks for execution; auditability by row count in register |
| V-02 | Lifecycle emphasis | TABLE SCHEMAS as Phase −1 with ENTRY/JOB/EXIT and Gate-S; schemas have phase-level standing; Gate-S blocks Phase 0 until schema declarations complete |
| V-03 | Inertia framing | Schemas as immutable output contracts parallel to strategy; column deviation = contract breach = gate failure; Cal column as "chain of custody" linking evidence to defense |
| V-04 | Combined (output format + phrasing register) | Schema Contract Board with per-schema BREACH CONDITIONs; SHALL/MUST throughout all phase obligations and gate statements; breach conditions named inline per schema |
| V-05 | Combined (all axes) | Three-path audit system: PATH 1 (schema spine), PATH 2 (WS-N headers), PATH 3 (EXIT slots); Schema B's Cal column as named architectural dependency of Schema C; schema IDs as cross-reference anchors across all phases |

---

## V-01: Output Format — Two-Level Schema Register

**Variation axis**: Output format — the TABLE SCHEMAS section is structured at two levels:
(1) a compact register table with one row per schema (Schema ID, Name, Phase Used, Mandatory
Columns), then (2) full expanded schema blocks with header rows and sentinel rules. The register
table makes completeness auditable by row count — a reviewer verifies all schemas are declared
before reading any schema block. The expanded blocks are the execution contracts phases
reference when producing output.

**Hypothesis**: A two-level structure separates the completeness concern (does a schema exist
for every table produced?) from the correctness concern (does the schema correctly define its
columns?). The register table answers completeness by scan; the expanded blocks answer
correctness by read. Having both means a reviewer cannot conflate "Schema B appears in the
register" with "Schema B's column definitions are verified" — they are distinct checks against
distinct structural layers.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. Every proposal must defeat the null.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan section headers for WS-1, WS-2, WS-3.
  Write-surface register below declares 3 rows; 3 section headers must appear.
  Completeness verifiable by header count without reading phase content.

AUDIT PATH 2 (Lifecycle Slots): Scan each phase for ENTRY / JOB / EXIT sub-sections.
  EXIT is the structural home for every in-phase stop gate.
  Completeness verifiable by scanning EXIT sections without reading JOB content.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface Type              | Trigger Condition                                      |
|-----|------|---------------------------|--------------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact is opened    |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before any proposal column is filled   |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each typed null declaration write     |

════════════════════════════════════════════════════════════
TABLE SCHEMAS
════════════════════════════════════════════════════════════

This section is the upfront table contract. It is positioned before Phase 0 and before
any artifact read. All tables produced by this skill must conform to the schema declared
here. Defining a table with different columns during phase execution is a schema violation.

SCHEMA REGISTER (one row per schema — verify completeness by row count = 4):

| Schema ID | Schema Name       | Phase Used  | Required Columns                                                                                                       | Mandatory Column(s)                                            |
|-----------|-------------------|-------------|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Schema A  | Defense Register  | Phase 0     | Row, Dimension, Current Strategy Position, Defense Argument                                                           | All four                                                       |
| Schema B  | Signal Inventory  | Phase 1     | Artifact Filename, Date, NEW/PRIOR, Defense Register Rows (Cal)                                                        | Cal [MANDATORY]                                                |
| Schema C  | Proposals Table   | Phase 4     | Type, Proposal, Before, After, Evidence Artifact, Inertia Justification, Defense Defeated (Row #)                     | Inertia Justification [MANDATORY], Defense Defeated (Row #) [MANDATORY] |
| Schema D  | Phase-Spec Table  | Every phase | Slot (ENTRY/JOB/EXIT), Content                                                                                         | All three slots                                                |

SCHEMA A — DEFENSE REGISTER (full definition)
| Row | Dimension | Current Strategy Position | Defense Argument |
Sentinel rules: ?? for unknown cells. -- for confirmed not-applicable rows only.
All four columns required. Blank cell is a violation regardless of other content.

SCHEMA B — SIGNAL INVENTORY (full definition)
| Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
Sort order: NEW artifacts above PRIOR artifacts (mandatory ordering constraint).
Sentinel rules — Cal column: ?? if implication unknown. -- if no rows implicated.
Cal column is MANDATORY: blank cell is a schema violation.
Architectural constraint: ALL NEW-artifact Cal cells must be filled before any
Schema C proposal row is opened. Cal completion is causally upstream of proposals.

SCHEMA C — PROPOSALS TABLE (full definition)
| Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
Type values: ADD, REMOVE, REPRIORITIZE only.
Evidence Artifact: ?? if no specific artifact. Blank is a violation.
Defense Defeated (Row #): must cite Schema A row number. Prose description alone fails.
A named defense without a row number does not satisfy this column.
Inertia Justification [MANDATORY]: check against BANNED FORMS before writing.

SCHEMA D — PHASE-SPEC TABLE (full definition)
| Slot  | Content                                                   |
|-------|-----------------------------------------------------------|
| ENTRY | [Preconditions true before this phase begins]             |
| JOB   | [Work instructions for this phase]                        |
| EXIT  | [Gate — "Do not advance to Phase N+1 without this gate."] |
All three slots required in every phase. EXIT is the structural home for stop gates.
Stop gate language in ENTRY or JOB does not satisfy the EXIT structural requirement.

════════════════════════════════════════════════════════════
VOCABULARY CONTRACT
════════════════════════════════════════════════════════════

Two sentinel tokens, in force in all cells, columns, and free-text fields:

| Token | Meaning                                |
|-------|----------------------------------------|
| ??    | Open obligation — unknown or unfilled  |
| --    | Closed decision — deliberately absent  |

BANNED FORMS — verbatim match disqualifies any justification, inertia, reason,
or null-declaration cell. Writing any of the following is a gate failure:

  "no change needed"    "nothing to add"      "clearly warranted"
  "seems sufficient"    "a few artifacts"     "several artifacts"
  "some signals"        "not necessary"       any non-integer count

Check every free-text cell against this list before writing.
Null declaration reason cells are NOT exempt. Banned forms are banned everywhere.

Integer-enforcement gate: "a few", "several", "some", or any non-integer value in
any count field is a gate failure, not a quality concern.

Violation conditions:
- Blank cell where ?? required: vocabulary violation
- ?? where -- is correct: vocabulary violation
- Any banned form in any free-text cell: vocabulary violation
- Non-integer count in any count field: integer-enforcement gate failure

════════════════════════════════════════════════════════════
PHASE LIFECYCLE TEMPLATE (applied to every phase below)
════════════════════════════════════════════════════════════

Every phase uses Schema D as its structural container:
| Slot  | Content                                                    |
|-------|-----------------------------------------------------------|
| ENTRY | [Preconditions]                                           |
| JOB   | [Instructions]                                            |
| EXIT  | [Gate — "Do not advance to Phase N+1 without this gate."] |

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                                   |
|-------|-------------------------------------------------------------------------------------------|
| ENTRY | Topic known. No signal artifacts read. strategy.md not opened.                           |
| JOB   | Open strategy.md. Extract date. Build Schema A (Defense Register).                       |
| EXIT  | Gate-0: Schema A complete, all cells filled. Do not advance to Phase 1. Stop. Halt here. |

Execute JOB:
  Open strategy.md. Read full content and extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER:
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension. All cells required. ?? or -- per Schema A rules.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT, after Gate-0 passes, before any signal artifact opens.
  Confirm: Gate-0 has passed (Schema A complete, every cell filled).
  Write WS-1 MILESTONE as declaration that Gate-0 has passed.
  Do not open any signal artifact before writing WS-1 MILESTONE. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------|
| ENTRY | Gate-0 passed. WS-1 MILESTONE written. Schema A complete.                                                    |
| JOB   | Locate all signal artifacts (9 namespaces). Build Schema B. Write delta sentence.                            |
| EXIT  | Gate-1: Schema B complete. NEW above PRIOR. All NEW Cal cells filled. Integer delta sentence. Do not advance to Phase 2. Stop. Halt here. |

Execute JOB:
  Locate all signal artifact files across all 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (NEW artifacts above PRIOR — mandatory sort):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  All NEW-artifact Cal cells must be filled before any Schema C proposal row opens.

  Write mandatory delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Non-integer form is an integer-enforcement gate failure.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                              |
|-------|----------------------------------------------------------------------|
| ENTRY | Gate-1 passed. All NEW-artifact Cal cells filled. No proposals open. |
| JOB   | Read full content of every NEW artifact. Do not read PRIOR artifacts. |
| EXIT  | Gate-2: All NEW artifacts read. Do not advance to Phase 3. Stop. Halt here. |

Execute JOB:
  Read full content of every artifact classified NEW in Schema B inventory.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                               |
|-------|--------------------------------------------------------------------------------------|
| ENTRY | Gate-2 passed. All NEW artifacts read. Schema A (Defense Register) known.            |
| JOB   | Delta detection (two-condition gate). Conflict audit. Typed results for both.        |
| EXIT  | Gate-3: Delta detections documented. Conflict audit has typed result. Do not advance to Phase 4. Stop. Halt here. |

Execute JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in at least one NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md content?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations may not support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Audit cross-artifact contradictions among NEW artifacts.
  If found: document in a CONFLICT REGISTER table.
  If none: write typed null form:
    "CONFLICT DETECTION — NULL: No cross-artifact contradictions found.
    NO CHANGE wins because: [specific artifact reference]."

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before filling any Schema C proposal column:
  Confirm: (1) Gate-3 passed. (2) All NEW Cal cells in Schema B filled.
  (3) Schema C Inertia Justification column labeled [MANDATORY] per TABLE SCHEMAS section.
  Write WS-2 MILESTONE as declaration that all three confirmations pass.
  Do not fill any proposal column before writing WS-2 MILESTONE. Halt here.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                                     |
|-------|---------------------------------------------------------------------------------------------|
| ENTRY | Gate-3 passed. WS-2 MILESTONE written. All NEW Cal cells filled. No proposal rows open.   |
| JOB   | Build Schema C (Proposals Table). Typed null declarations per WS-3 for absent types.      |
| EXIT  | Gate-4: Schema C complete. All cells filled. All absent types have typed null declarations. Inertia and null reason cells checked against BANNED FORMS. Do not modify strategy.md. Stop. Halt here. |

Execute JOB:
  Build SCHEMA C — PROPOSALS TABLE:
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Check Inertia Justification cells against BANNED FORMS before writing.
  Defense Defeated must cite Schema A row number, not prose description.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB.
Mandatory template: "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Before writing reason cell: check against BANNED FORMS.
  "no change needed" — banned. Check this cell before presenting.
  "nothing to add" — banned. Check this cell before presenting.
  Any match disqualifies. Reason must cite specific artifact or strategy evidence.

Required for each absent proposal type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md are listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Do not modify any file. Halt here and wait for reply.

════════════════════════════════════════════════════════════
APPLY PHASE (after YES or REVISED only)
════════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
Do not add unrequested changes.
```

---

## V-02: Lifecycle Emphasis — TABLE SCHEMAS as Phase −1 with Gate-S

**Variation axis**: Lifecycle emphasis — the TABLE SCHEMAS section is formalized as Phase −1,
a numbered pre-phase with ENTRY/JOB/EXIT slots. A Gate-S (Schema Gate) explicitly blocks
Phase 0 from starting until all schema declarations are complete. The sequential gate chain
runs Gate-S → Gate-0 → Gate-1 → Gate-2 → Gate-3 → Gate-4, with schema completeness as the
first named gate.

**Hypothesis**: When TABLE SCHEMAS has phase-level standing (Phase −1 with its own named
gate), schema completeness acquires the same structural weight as defense register completeness
(Gate-0). A reviewer auditing gate coverage must find Gate-S in the chain — its absence is a
visible break at the start. The gate chain makes schema-before-data an architectural rule with
its own named enforcement point, not a recommendation embedded in the write-surface register.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. Every proposal must defeat the null.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan for WS-1, WS-2, WS-3 section headers.
  Three rows in write-surface register below; three section headers must appear.

AUDIT PATH 2 (Lifecycle Slots): Scan each phase (Phase −1 through Phase 4) for EXIT slots.
  Every EXIT slot houses the in-phase stop gate.
  Gate-S (Phase −1) → Gate-0 → Gate-1 → Gate-2 → Gate-3 → Gate-4.
  A missing gate is a visible break in the sequential chain.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface Type              | Trigger                                          |
|-----|------|---------------------------|--------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact opened |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before proposal column fill      |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each null declaration write     |

════════════════════════════════════════════════════════════
PHASE LIFECYCLE TEMPLATE
════════════════════════════════════════════════════════════

Every phase (Phase −1 through Phase 4) declares three named sub-sections:
  ENTRY: [Preconditions that must be true before this phase begins]
  JOB:   [Work instructions for this phase]
  EXIT:  [Gate — "Do not advance to Phase N+1 without passing this gate."]
EXIT is the structural home for stop gates. Stop gate in ENTRY or JOB does not satisfy C-12.

════════════════════════════════════════════════════════════
Phase −1 — TABLE SCHEMAS (Schema Declarations)
════════════════════════════════════════════════════════════

ENTRY:
  No strategy file opened. No signal artifacts read. No structures built.
  This is the first act. Schema completeness is established here before any data is examined.

JOB:
  Declare all table schemas used in this skill execution. Every table produced in
  this output must conform to a schema declared in this phase. Producing a table
  with columns not declared here, or omitting a declared mandatory column, is a
  schema violation.

  SCHEMA A — DEFENSE REGISTER
  | Row | Dimension | Current Strategy Position | Defense Argument |
  Required columns: Row (integer), Dimension, Current Strategy Position, Defense Argument.
  Sentinel rules: ?? for unknown. -- for confirmed not-applicable only.
  All four columns MANDATORY. Blank cell is a violation.

  SCHEMA B — SIGNAL INVENTORY
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  Required columns: all four. Cal column MANDATORY — blank is a violation.
  Sort order: NEW artifacts above PRIOR artifacts. Mandatory ordering.
  Sentinel rules for Cal: ?? if implication unknown. -- if no rows implicated.
  Architectural constraint: all NEW-artifact Cal cells must be filled before any
  Schema C row is opened. Calibration is causally upstream of proposals.

  SCHEMA C — PROPOSALS TABLE
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Required columns: all seven. Blank cell is a violation.
  Type values: ADD, REMOVE, REPRIORITIZE only.
  Defense Defeated (Row #): must cite Schema A row number. Prose alone fails this column.
  Inertia Justification: check against BANNED FORMS before writing.

  SCHEMA D — PHASE-SPEC TABLE (instantiated in every phase including this one)
  | Slot  | Content  |
  ENTRY, JOB, EXIT rows required. All three slots mandatory in every phase.

  VOCABULARY CONTRACT:
  Sentinel tokens: ?? (open obligation) | -- (closed decision). In force in all cells.
  BANNED FORMS — check every free-text cell before writing:
    "no change needed"   "nothing to add"    "clearly warranted"
    "seems sufficient"   "a few artifacts"   "several artifacts"
    "some signals"       "not necessary"     any non-integer count
  Null declaration cells are NOT exempt from banned forms.
  Integer-enforcement: "a few", "several", "some", or any non-integer is a gate failure.

EXIT (Gate-S):
  All four schemas declared with full column definitions and sentinel rules.
  Vocabulary contract declared. Banned forms listed.
  Gate-S: Phase 0 may not begin until Gate-S passes.
  Do not advance to Phase 0 without passing Gate-S.
  Stop. Verify all four schemas are declared. Halt here.

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

ENTRY:
  Gate-S passed. All schemas declared. Topic known. No signal artifacts read.

JOB:
  Open strategy.md. Read full content and extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER:
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension. Conform to Schema A declaration in Phase −1.

EXIT (Gate-0):
  Schema A complete. All cells filled (no blanks; ?? or -- per Schema A rules).
  Gate-0: No signal artifact may be read until Gate-0 passes.
  Do not advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT, after Gate-0 passes, before any signal artifact is opened.
  Confirm: Gate-0 passed (Schema A complete, all cells filled).
  Write WS-1 MILESTONE. Declaration that Gate-0 has passed.
  Do not open any signal artifact before writing WS-1 MILESTONE. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. WS-1 MILESTONE written. Schema A complete.
  All schemas declared (Gate-S passed in Phase −1).

JOB:
  Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (NEW above PRIOR — mandatory per Schema B):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  All NEW-artifact Cal cells must be filled before any Phase 4 row opens.

  Write mandatory delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Non-integer is an integer-enforcement gate failure.

EXIT (Gate-1):
  Schema B complete. NEW above PRIOR. All NEW-artifact Cal cells filled.
  Delta sentence written with integer values.
  Do not advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells are filled. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

ENTRY:
  Gate-1 passed. All NEW-artifact Cal cells filled. No proposals open.

JOB:
  Read full content of every artifact classified NEW in Schema B inventory.
  Do not read PRIOR artifacts.

EXIT (Gate-2):
  All NEW artifacts read in full.
  Do not advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

ENTRY:
  Gate-2 passed. All NEW artifacts read. Schema A (Defense Register) known from Phase 0.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in at least one NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."

  CONFLICT DETECTION — Audit NEW artifacts for cross-artifact contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found. NO CHANGE wins because:
  [specific artifact reference]."

EXIT (Gate-3):
  Delta detections documented. Conflict audit has typed result.
  Do not advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before opening any Schema C proposal row:
  Confirm: (1) Gate-3 passed. (2) All NEW Cal cells in Schema B filled.
  (3) Schema C Inertia Justification labeled [MANDATORY] per Phase −1 declaration.
  Write WS-2 MILESTONE. Halt here if any confirmation fails.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 passed. WS-2 MILESTONE written. All NEW Cal cells filled. No proposal rows open.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C declaration in Phase −1):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  For each absent proposal type, write a typed null declaration per WS-3 template below.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB.
Mandatory template: "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Before writing reason cell: check against BANNED FORMS.
  "no change needed" — banned. "nothing to add" — banned.
  Any match disqualifies. Reason must cite specific evidence or strategy content.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C complete. All cells filled. All absent types have typed null declarations.
  Inertia and null reason cells checked against BANNED FORMS.
  Do not modify strategy.md. Do not advance to Apply Phase without user confirmation.
  Stop. Verify every cell filled and every null uses typed template. Halt here.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md are listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for reply.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
```

---

## V-03: Inertia Framing — Schemas as Immutable Output Contracts

**Variation axis**: Inertia framing — the TABLE SCHEMAS section is introduced with the same
inertia framing that governs strategy content. Both the current strategy and the declared table
schemas carry inertia. A schema column is as stable as a strategy priority: deviating from a
declared schema is a contract violation, not a formatting choice. The calibration column is the
"chain of custody" column — it traces every NEW artifact to the defense it threatens. Breaking
that chain (omitting Cal, opening proposals before Cal is complete) is a chain-of-custody
violation with the same structural weight as a banned-form violation.

**Hypothesis**: When table schemas share the inertia framing with strategy content, column
additions, removals, or renames cannot be treated as innocent formatting adjustments. A schema
change is structurally equivalent to an unauthorized strategy change — it requires defeating a
declared position. This framing institutionalizes schema stability at the same level as strategy
stability, closing the gap where a model might produce "mostly-compliant" tables with quietly
altered columns. The chain-of-custody metaphor for Cal makes its omission a named violation
type, not an oversight.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

THE PREMISE: This skill manages two kinds of inertia simultaneously.

STRATEGY INERTIA: The current strategy is correct until signal evidence defeats a specific
defense. A proposal is an indictment: it claims a specific defense argument is wrong. If no
defense is defeated, the outcome is NO CHANGE to strategy.md.

SCHEMA INERTIA: The declared table schemas are immutable output contracts. Every table
produced in this execution must conform exactly to a schema declared in TABLE SCHEMAS below.
Adding, removing, or renaming a column is a contract violation equal to using a banned form.
Schema drift is not a formatting choice — it is an unauthorized change to a declared contract.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan for WS-1, WS-2, WS-3 section headers.
AUDIT PATH 2 (Lifecycle Slots): Scan each phase for ENTRY / JOB / EXIT sub-sections.
  EXIT is the structural home for each phase's stop gate.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface               | Trigger                                          |
|-----|------|-----------------------|--------------------------------------------------|
|  1  | WS-1 | Pre-read barrier      | Phase 0 EXIT — before any signal artifact opened |
|  2  | WS-2 | Schema boundary check | Phase 4 ENTRY — before proposal column fill      |
|  3  | WS-3 | Null declaration      | Phase 4 JOB — at each null declaration write     |

════════════════════════════════════════════════════════════
TABLE SCHEMAS — IMMUTABLE OUTPUT CONTRACTS
════════════════════════════════════════════════════════════

These schemas are declared before Phase 0 and before any artifact read.
They are immutable output contracts. Schema inertia is in effect from this point.
Column additions, removals, or renames during execution are contract breaches,
not formatting adjustments. They require the same evidentiary standard as strategy changes.

SCHEMA A — DEFENSE REGISTER (immutable contract)
Columns: Row | Dimension | Current Strategy Position | Defense Argument
Mandatory: all four. Sentinel: ?? for unknown. -- for confirmed not-applicable only.
Contract violation: any column renamed, added, or dropped; any cell blank where ?? required;
any defense argument using an inadmissible rebuttal form.

SCHEMA B — SIGNAL INVENTORY (immutable contract)
Columns: Artifact Filename | Date | NEW / PRIOR | Defenses Implicated (Cal) [MANDATORY]
Mandatory: all four. Sort order: NEW above PRIOR. Mandatory ordering constraint.
Sentinel for Cal: ?? (threat not yet assessed). -- (no defense threatened). Blank: violation.
Chain-of-custody rule: the Cal column traces every NEW artifact to the specific defense
it threatens. Cal = ??: threat not yet assessed (acceptable during Phase 1, must be resolved
before Phase 4). Cal = --: no defense threatened. Blank Cal cell: chain-of-custody violation.
Architectural constraint: ALL NEW-artifact Cal cells must be filled before any Schema C
row opens. Retroactive calibration after proposals are written is a chain-of-custody breach.

SCHEMA C — PROPOSALS TABLE (immutable contract)
Columns: Type | Proposal | Before | After | Evidence | Inertia Justification [MANDATORY] | Defense Defeated (Row #)
Mandatory: all seven. Type values: ADD, REMOVE, REPRIORITIZE only.
Defense Defeated (Row #): must cite Schema A row number. A proposal that cannot name the
specific defense row it defeated is inadmissible — it is a preference, not an indictment.
Inertia Justification: must pass inadmissible rebuttals check before writing.
Contract violation: any mandatory column omitted; Defense Defeated contains prose without
row number; Inertia Justification contains a banned form; any absent type has no typed null.

SCHEMA D — PHASE-SPEC TABLE (immutable contract — applied to every phase)
Columns: Slot | Content (ENTRY row, JOB row, EXIT row)
Mandatory: all three slots. Violation: any phase missing ENTRY, JOB, or EXIT.
EXIT slot is the structural home for stop gates. Stop gate in JOB prose does not satisfy
Schema D compliance — EXIT is the declared position for that content.

VOCABULARY CONTRACT — INADMISSIBLE REBUTTALS
Sentinel tokens: ?? (open obligation) | -- (closed decision). In force in all cells.

INADMISSIBLE REBUTTALS — banned by verbatim match everywhere including null declarations:
  "no change needed"    "nothing to add"      "clearly warranted"
  "seems sufficient"    "a few artifacts"     "several artifacts"
  "some signals"        "not necessary"       any non-integer count

Check every free-text cell against this list before writing.
Non-integer count in any count field: integer-enforcement gate failure.
Null declaration reason cells are NOT exempt — inadmissible rebuttals are banned everywhere.

Violation taxonomy:
- Blank cell where ?? required: inadmissibility violation
- ?? where -- correct: inadmissibility violation
- Inadmissible rebuttal in any free-text cell: inadmissibility violation
- Non-integer count: integer-enforcement gate failure
- Column added/removed/renamed from declared schema: contract breach

════════════════════════════════════════════════════════════
PHASE LIFECYCLE TEMPLATE
════════════════════════════════════════════════════════════

Every phase uses Schema D: ENTRY, JOB, EXIT sub-sections. EXIT houses each stop gate.

════════════════════════════════════════════════════════════
Phase 0 — ARM THE DEFENSE REGISTER
════════════════════════════════════════════════════════════

ENTRY:
  Schema contracts declared. No signal artifacts read. strategy.md not opened.
  This phase arms the defense before any signal evidence is examined.

JOB:
  Open strategy.md. Read full content and extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER (conform to Schema A immutable contract):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension. Check Defense Argument cells against
  INADMISSIBLE REBUTTALS before writing — generic rebuttals are inadmissible.

EXIT (Gate-0):
  Schema A complete. All cells filled (no blanks; ?? or -- per Schema A contract).
  Defense argument cells checked against inadmissible rebuttals.
  Gate-0: No signal artifact may be examined until Gate-0 passes.
  Do not advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT. The defense has been armed.
Confirm Gate-0 passed (Schema A complete, all cells filled, defense argument cells
checked against inadmissible rebuttals).
Write WS-1 MILESTONE. Declaration that Gate-0 has passed and the defense is armed.
Do not open any signal artifact before writing WS-1 MILESTONE. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — ASSEMBLE THE EVIDENCE (Signal Inventory with Calibration)
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. Defense armed. WS-1 MILESTONE written.
  Every NEW artifact will be calibrated against the defense before proposals open.

JOB:
  Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (conform to Schema B immutable contract):
  | Artifact Filename | Date | NEW / PRIOR | Defenses Implicated (Cal) [MANDATORY] |
  NEW artifacts above PRIOR (mandatory sort per Schema B contract).
  Chain-of-custody enforcement: ALL NEW-artifact Cal cells must be filled before any
  Schema C row opens. Blank Cal = chain-of-custody violation.

  Write mandatory delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Non-integer form is a gate failure.

EXIT (Gate-1):
  Schema B complete per contract. NEW above PRIOR. All NEW-artifact Cal cells filled.
  Delta sentence written with integer values.
  Do not advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — READ THE CHALLENGERS (NEW Artifacts)
════════════════════════════════════════════════════════════

ENTRY:
  Gate-1 passed. Chain of custody established. No proposals open.

JOB:
  Read full content of every artifact classified NEW in Schema B.
  Do not read PRIOR artifacts.

EXIT (Gate-2):
  All NEW artifacts read.
  Do not advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — ADJUDICATE DELTAS AND CONFLICTS
════════════════════════════════════════════════════════════

ENTRY:
  Gate-2 passed. All NEW artifacts read. Schema A defense arguments known.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in a NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES. Potential indictment material.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations may not support ADD or REPRIORITIZE indictments.

  CONFLICT DETECTION — Audit NEW artifacts for cross-artifact contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found. NO CHANGE wins because:
  [specific artifact or strategy reference]."

EXIT (Gate-3):
  Delta detections documented. Conflict audit has typed result (table or typed NULL).
  Do not advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before opening any Schema C row:
  Confirm: (1) Gate-3 passed. (2) All NEW-artifact Cal cells in Schema B filled
  (chain of custody unbroken). (3) Schema C Inertia Justification labeled [MANDATORY].
  Write WS-2 MILESTONE. Halt here if any confirmation fails.

════════════════════════════════════════════════════════════
Phase 4 — DELIVER THE INDICTMENT (Proposals)
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 passed. WS-2 MILESTONE written. Chain of custody verified. No rows open.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C immutable contract):
  | Type | Proposal | Before | After | Evidence | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Each proposal row is an indictment of a specific defense register row.
  Defense Defeated (Row #): must name Schema A row number. No row number = inadmissible.
  Inertia Justification: check against INADMISSIBLE REBUTTALS before writing.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB.
Mandatory template: "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Before writing reason: check against INADMISSIBLE REBUTTALS.
  "no change needed" — inadmissible. "nothing to add" — inadmissible.
  Any match disqualifies. Reason must cite specific evidence or strategy content.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C complete per immutable contract. All cells filled. All absent types have typed nulls.
  Inertia and null reason cells checked against INADMISSIBLE REBUTTALS.
  Do not modify strategy.md. Halt here pending user confirmation.
  Stop. Verify every cell and every null uses typed template. Halt here.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md are listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Halt here and wait for reply.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
```

---

## V-04: Combined (Output Format + Phrasing Register) — Schema Contract Board with Breach Conditions

**Variation axes**: Output format (Schema Contract Board — formal named register with per-schema
BREACH CONDITION) + phrasing register (SHALL/MUST/PROHIBITED throughout all phase obligations
and gate statements).

Each schema in the TABLE SCHEMAS section carries an explicit named BREACH CONDITION — the exact
violation form that makes compliance fail. The skill uses SHALL in all obligation positions and
PROHIBITED for all disqualification positions. Gate statements use SHALL form ("Phase N SHALL
NOT advance until..."), making gate violations formally evaluable rather than aspirational.

**Hypothesis**: When every schema carries a named breach condition, schema non-conformance is
a detectable violation with a name, not an unclassified gap. Combined with formal register
(SHALL), every obligation in the skill is binary-evaluable: either the SHALL condition was met
or it was violated. A reviewer needs no interpretive judgment — they check whether the SHALL
was satisfied and whether any named BREACH CONDITION was triggered.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. All proposals SHALL defeat the null.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan section headers for WS-1, WS-2, WS-3.
  Write-surface register declares 3 rows. 3 section headers SHALL appear.
AUDIT PATH 2 (Lifecycle Slots): Scan each phase for ENTRY / JOB / EXIT sub-sections.
  EXIT SHALL house the in-phase stop gate. A phase without EXIT is a structural violation.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface               | Trigger                                          |
|-----|------|-----------------------|--------------------------------------------------|
|  1  | WS-1 | Pre-read barrier      | Phase 0 EXIT — before any signal artifact opened |
|  2  | WS-2 | Schema boundary check | Phase 4 ENTRY — before proposal column fill      |
|  3  | WS-3 | Null declaration      | Phase 4 JOB — at each null declaration write     |

════════════════════════════════════════════════════════════
TABLE SCHEMAS — SCHEMA CONTRACT BOARD
════════════════════════════════════════════════════════════

This section SHALL be positioned before Phase 0 and before any artifact read.
All tables produced by this skill SHALL conform to a schema declared here.
Each schema declares column structure, mandatory labels, sentinel rules, and BREACH CONDITION.
A BREACH CONDITION is a named violation that makes schema compliance fail. Producing a
table that triggers a BREACH CONDITION is a structural violation, not a quality concern.

SCHEMA A — DEFENSE REGISTER
Columns: Row | Dimension | Current Strategy Position | Defense Argument
Mandatory: all four columns. Sentinel: ?? (unknown), -- (not applicable).
BREACH CONDITION: Schema A SHALL be considered breached when: (a) any column is omitted,
renamed, or reordered; (b) any cell is left blank where ?? is the required sentinel;
(c) any defense argument contains an inadmissible rebuttal form.

SCHEMA B — SIGNAL INVENTORY
Columns: Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY]
Mandatory: all four. Sort order: NEW above PRIOR (mandatory). Sentinel for Cal:
?? (implication unknown), -- (no defense implicated). Blank Cal cell is PROHIBITED.
BREACH CONDITION: Schema B SHALL be considered breached when: (a) Cal column is absent
or renamed; (b) any NEW-artifact Cal cell is blank; (c) NEW artifacts appear below PRIOR;
(d) any Schema C proposal row is opened before ALL NEW-artifact Cal cells are filled.
The ordering constraint (NEW first; Cal filled before proposals) is a Schema B contract term.

SCHEMA C — PROPOSALS TABLE
Columns: Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #)
Mandatory: all seven. Type values: ADD, REMOVE, REPRIORITIZE. Other values PROHIBITED.
Defense Defeated (Row #): SHALL cite Schema A row number. Prose description alone is PROHIBITED.
Inertia Justification: SHALL be checked against BANNED FORMS before any cell is written.
BREACH CONDITION: Schema C SHALL be considered breached when: (a) any mandatory column is
omitted; (b) Defense Defeated lacks a row number; (c) Inertia Justification contains a banned
form; (d) any absent change type has no typed null declaration.

SCHEMA D — PHASE-SPEC TABLE
Columns: Slot | Content (three rows: ENTRY, JOB, EXIT)
Mandatory: all three slots SHALL be present in every phase.
EXIT SHALL house the stop gate. Stop gate language appearing only in JOB or ENTRY is PROHIBITED
as a substitute for the EXIT position.
BREACH CONDITION: Schema D SHALL be considered breached when: (a) any phase omits ENTRY, JOB,
or EXIT; (b) stop gate language appears only in JOB or ENTRY; (c) EXIT does not reference
the next phase by number.

════════════════════════════════════════════════════════════
VOCABULARY CONTRACT
════════════════════════════════════════════════════════════

Sentinel tokens:
  ??  — open obligation. SHALL be used for unknown or unfilled values.
  --  — closed decision. SHALL be used only for confirmed not-applicable entries.

BANNED FORMS — verbatim match in any free-text cell is PROHIBITED:
  "no change needed"    "nothing to add"      "clearly warranted"
  "seems sufficient"    "a few artifacts"     "several artifacts"
  "some signals"        "not necessary"       any non-integer count

Every free-text cell SHALL be checked against this list before it is written.
Null declaration reason cells SHALL NOT receive a scope exemption. Banned forms
are PROHIBITED in null declarations equally.
Integer-enforcement: "a few", "several", "some", or any non-integer in any count field
is PROHIBITED. Non-integer count SHALL be treated as a gate failure.

Violation conditions:
- Blank cell where ?? required: vocabulary violation
- ?? where -- is correct: vocabulary violation
- Any banned form anywhere: vocabulary violation
- Non-integer count: integer-enforcement gate failure

════════════════════════════════════════════════════════════
PHASE LIFECYCLE TEMPLATE
════════════════════════════════════════════════════════════

Every phase SHALL use Schema D: ENTRY, JOB, EXIT sub-sections.
EXIT SHALL be the structural home for the stop gate. EXIT SHALL reference the next phase:
"Phase N SHALL NOT advance to Phase N+1 without passing this gate."

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

ENTRY:
  Schema Contract Board declared. Topic known. No signal artifacts read.

JOB:
  Open strategy.md. Read full content. Extract last-modified date.
  STRATEGY DATE: [YYYY-MM-DD]
  Build SCHEMA A — DEFENSE REGISTER. Conform to Schema A contract.
  | Row | Dimension | Current Strategy Position | Defense Argument |
  Defense Argument cells SHALL be checked against BANNED FORMS before writing.

EXIT (Gate-0):
  Schema A SHALL be complete. All cells filled (no blanks; ?? or -- per Schema A).
  Phase 0 SHALL NOT advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT. SHALL fire before any signal artifact is opened.
  Confirm Gate-0 passed (Schema A complete, all cells filled).
  Write WS-1 MILESTONE. This SHALL constitute declaration Gate-0 passed.
  Opening any signal artifact before WS-1 MILESTONE is written is PROHIBITED. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. WS-1 MILESTONE written. Schema A complete.

JOB:
  Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (conform to Schema B contract):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  NEW artifacts SHALL appear above PRIOR artifacts. All NEW-artifact Cal cells SHALL be
  filled before any Schema C row opens. Opening a proposal row before Cal is complete
  is a Schema B breach.

  Delta summary sentence SHALL state:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M SHALL be integers. Non-integer form is PROHIBITED.

EXIT (Gate-1):
  Schema B SHALL be complete. NEW above PRIOR. All NEW-artifact Cal cells filled.
  Delta sentence SHALL be written with integer values.
  Phase 1 SHALL NOT advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

ENTRY:
  Gate-1 passed. All NEW-artifact Cal cells filled. No proposals open.

JOB:
  Read full content of every NEW artifact in Schema B. PRIOR artifacts SHALL NOT be read.

EXIT (Gate-2):
  All NEW artifacts SHALL have been read.
  Phase 2 SHALL NOT advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

ENTRY:
  Gate-2 passed. All NEW artifacts read. Schema A defense arguments available.

JOB:
  DELTA DETECTION — For each NEW-artifact observation:
    Condition 1: present in a NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA: both YES. PRIOR-ONLY: Condition 2 NO — annotate "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations SHALL NOT support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Audit NEW artifacts for contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found. NO CHANGE wins because:
  [specific artifact reference]."

EXIT (Gate-3):
  Delta detections SHALL be documented. Conflict audit SHALL have a typed result.
  Phase 3 SHALL NOT advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. SHALL fire before any Schema C column is filled.
  Confirm: (1) Gate-3 passed. (2) All NEW Cal cells in Schema B filled.
  (3) Schema C Inertia Justification labeled [MANDATORY] per Schema Contract Board.
  Write WS-2 MILESTONE. Opening a proposal row before WS-2 MILESTONE is PROHIBITED.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 passed. WS-2 MILESTONE written. All NEW Cal cells filled. No proposal rows open.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C contract):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Inertia Justification cells SHALL be checked against BANNED FORMS before writing.
  Defense Defeated SHALL cite Schema A row number. Prose alone is PROHIBITED.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB.
Null declarations SHALL use mandatory template:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Reason cells SHALL be checked against BANNED FORMS before writing.
  "no change needed" is PROHIBITED. "nothing to add" is PROHIBITED.
  Any banned form in reason cell SHALL disqualify the null declaration.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C SHALL be complete. All cells filled. All absent types SHALL have typed nulls.
  All Inertia and null reason cells SHALL have been checked against BANNED FORMS.
  strategy.md SHALL NOT be modified before user confirmation.
  Phase 4 SHALL NOT advance without passing Gate-4.
  Stop. Verify every cell filled and every null uses typed template. Halt here.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md are listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. strategy.md SHALL NOT be written before user reply. Halt here.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
```

---

## V-05: Combined (All Axes) — Three-Path Audit with Schema Spine

**Variation axes**: All four — output format (schema register as PATH 1 spine), lifecycle
emphasis (Phase −1 for schemas with Gate-S in gate chain), inertia framing (schema inertia
+ defense inertia as twin contracts; Cal as chain of custody), phrasing register (SHALL/MUST
throughout).

Three independent audit paths declared upfront before any skill content:
- PATH 1 (Schema Spine): Count named schema sections in TABLE SCHEMAS.
- PATH 2 (Write-Surface Spine): Count WS-N section headers.
- PATH 3 (Lifecycle Slots): Scan EXIT slots across Gate-S through Gate-4.

Schema B's Cal column is named explicitly as the architectural dependency of Schema C:
Schema C SHALL NOT be opened until Schema B's Cal dependency is satisfied. This dependency
is a cross-schema contract term, not a phase instruction, making the ordering constraint
structurally upstream of Phase 4 rather than embedded in it.

**Hypothesis**: Three audit paths create three independent failure modes. A skill satisfying
PATH 2 and PATH 3 but failing PATH 1 has an incomplete schema contract — table columns can
drift without being visible as structural violations. The schema spine is the only audit path
that makes C-35 compliance verifiable by structure rather than by reading phase content. When
Schema B's Cal dependency is a contract term, it is inherited by Schema C and cannot be
satisfied retroactively: the constraint fires at the schema level, not only at phase execution.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. All proposals SHALL defeat the null.

════════════════════════════════════════════════════════════
THREE-PATH AUDIT SYSTEM
════════════════════════════════════════════════════════════

This skill is auditable via three independent structural paths. No path is redundant.

PATH 1 (Schema Spine): Count named schema sections in TABLE SCHEMAS register below.
  Four schemas declared; four schema blocks SHALL appear. Completeness by count.
  Failure: a skill that produces tables with undeclared columns has no PATH 1 violation
  visible without reading phase content. PATH 1 makes that failure structurally detectable.

PATH 2 (Write-Surface Spine): Count WS-1, WS-2, WS-3 section headers.
  Three write-surface blocks declared in register below; three headers SHALL appear.

PATH 3 (Lifecycle Slots): Scan each phase (Phase −1 through Phase 4) for EXIT slots.
  Every EXIT slot SHALL house the in-phase stop gate.
  Gate-S → Gate-0 → Gate-1 → Gate-2 → Gate-3 → Gate-4 form a linked chain.
  A missing gate is a visible break in the chain without reading phase content.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface               | Trigger                                          |
|-----|------|-----------------------|--------------------------------------------------|
|  1  | WS-1 | Pre-read barrier      | Phase 0 EXIT — before any signal artifact opened |
|  2  | WS-2 | Schema boundary check | Phase 4 ENTRY — before proposal column fill      |
|  3  | WS-3 | Null declaration      | Phase 4 JOB — at each null declaration write     |

Three rows declared. Three WS-N section headers SHALL appear. PATH 2 audit complete
when three headers found.

════════════════════════════════════════════════════════════
TABLE SCHEMAS — SCHEMA SPINE (PATH 1 ANCHOR)
════════════════════════════════════════════════════════════

This section is the PATH 1 anchor. It SHALL be positioned before Phase −1 begins.
Four schemas SHALL be declared. PATH 1 audit counts named schema sections: count = 4.
Both strategy content and table schemas carry inertia. A schema column is as stable as
a strategy priority. Column deviation is a contract breach requiring the same evidentiary
standard as a strategy change — not a formatting choice.

Each schema declares column structure, mandatory labels, sentinel rules, and BREACH CONDITION.

SCHEMA A — DEFENSE REGISTER
Columns: Row | Dimension | Current Strategy Position | Defense Argument
Mandatory: all four. Sentinel: ?? (unknown), -- (not applicable).
Defense Argument cells SHALL cite specific strategy content. Generic assertions are
PROHIBITED — see VOCABULARY CONTRACT.
BREACH CONDITION: (1) any column omitted, renamed, or reordered; (2) any cell blank
where ?? required; (3) any defense argument uses a banned form.

SCHEMA B — SIGNAL INVENTORY
Columns: Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY]
Mandatory: all four. Sort: NEW above PRIOR (mandatory ordering).
Sentinel for Cal: ?? (threat not assessed), -- (no defense implicated). Blank: PROHIBITED.
Chain-of-custody rule: Cal traces every NEW artifact to the defense it threatens.
Cross-schema dependency: Schema C rows SHALL NOT be opened until ALL NEW-artifact Cal
cells in Schema B are filled. This dependency is a Schema B contract term — it is
structurally upstream of Phase 4, not merely a phase instruction.
BREACH CONDITION: (1) Cal column absent or renamed; (2) any NEW-artifact Cal cell blank;
(3) NEW artifacts below PRIOR; (4) any Schema C row opened before Schema B Cal dependency
is satisfied — both Schema B and Schema C are simultaneously breached.

SCHEMA C — PROPOSALS TABLE
Columns: Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #)
Mandatory: all seven. Type values: ADD, REMOVE, REPRIORITIZE only.
Defense Defeated (Row #): SHALL cite Schema A row number. Prose alone is PROHIBITED.
Inertia Justification: SHALL be checked against BANNED FORMS before any cell is written.
Schema C inherits Schema B's Cal dependency as a cross-schema contract term.
BREACH CONDITION: (1) any mandatory column omitted; (2) Defense Defeated lacks row number;
(3) Inertia Justification contains a banned form; (4) any absent change type has no
typed null declaration; (5) any row opened before Schema B Cal dependency satisfied.

SCHEMA D — PHASE-SPEC TABLE
Columns: Slot | Content (three mandatory rows: ENTRY, JOB, EXIT)
Mandatory: all three slots in every phase (Phase −1 through Phase 4).
EXIT SHALL house the stop gate. Stop gate language in JOB or ENTRY is PROHIBITED as
EXIT substitute. EXIT SHALL reference the next phase by number.
BREACH CONDITION: (1) any slot absent from any phase; (2) stop gate appears only in
JOB or ENTRY; (3) EXIT does not reference next phase number.

════════════════════════════════════════════════════════════
VOCABULARY CONTRACT
════════════════════════════════════════════════════════════

Sentinel tokens (in force in all cells, all schemas, all phases):
  ?? — open obligation — SHALL be used for unknown or unfilled values
  -- — closed decision — SHALL be used only for confirmed not-applicable entries

BANNED FORMS — verbatim match in any free-text cell is PROHIBITED:
  "no change needed"    "nothing to add"      "clearly warranted"
  "seems sufficient"    "a few artifacts"     "several artifacts"
  "some signals"        "not necessary"       any non-integer count

Every free-text cell SHALL be checked against this list before writing.
Null declaration reason cells SHALL NOT receive a scope exemption.
Integer-enforcement: "a few", "several", "some", or non-integer in any count is PROHIBITED.

Violation taxonomy:
| Type | Condition |
|------|-----------|
| Schema breach | Column added, removed, or renamed from declared schema |
| Cal dependency breach | Schema C row opened before all NEW-artifact Cal cells filled |
| Vocabulary violation | Blank where ?? required, or ?? where -- is correct |
| Banned form | Any BANNED FORM in any free-text cell including null declarations |
| Integer gate failure | Any non-integer count in any count field |

════════════════════════════════════════════════════════════
PHASE LIFECYCLE TEMPLATE
════════════════════════════════════════════════════════════

Every phase (Phase −1 through Phase 4) SHALL use Schema D: ENTRY, JOB, EXIT.
EXIT SHALL house the stop gate. EXIT SHALL state:
"Phase N SHALL NOT advance to Phase N+1 without passing this gate."
Gate references the next phase by number.

════════════════════════════════════════════════════════════
Phase −1 — DECLARE SCHEMAS (Schema Spine — PATH 1 source)
════════════════════════════════════════════════════════════

ENTRY:
  No strategy file opened. No signal artifacts read. No structures built.
  This is the first act. PATH 1 completeness is established here.

JOB:
  The TABLE SCHEMAS section above declares all four schemas.
  Confirm: Schema A through Schema D are present in TABLE SCHEMAS. Count = 4.
  PATH 1 audit: four schema names present and each has column definitions and
  breach condition. Count = 4.

EXIT (Gate-S):
  All four schemas SHALL be declared with column definitions, sentinel rules,
  and breach conditions. Vocabulary contract SHALL be declared.
  Phase −1 SHALL NOT advance to Phase 0 without passing Gate-S.
  Stop. Verify all four schemas present. Halt here.

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

ENTRY:
  Gate-S passed. All schemas declared. Topic known. No signal artifacts read.

JOB:
  Open strategy.md. Read full content. Extract last-modified date.
  STRATEGY DATE: [YYYY-MM-DD]
  Build SCHEMA A — DEFENSE REGISTER (conform to Schema A — breach conditions in force):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  Defense Argument cells SHALL be checked against BANNED FORMS before writing.

EXIT (Gate-0):
  Schema A SHALL be complete. All cells filled per Schema A contract.
  Phase 0 SHALL NOT advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT. SHALL fire before any signal artifact is opened.
  Confirm Gate-0 passed (Schema A complete, all cells filled).
  Write WS-1 MILESTONE. This SHALL constitute declaration Gate-0 passed.
  Opening any signal artifact before WS-1 MILESTONE is written is PROHIBITED. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. WS-1 MILESTONE written. Schema A complete.

JOB:
  Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (conform to Schema B — breach conditions in force):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  NEW artifacts SHALL appear above PRIOR artifacts (mandatory sort per Schema B).
  Schema B's Cal dependency on Schema C is active: no Schema C row SHALL be opened
  until ALL NEW-artifact Cal cells are filled.

  Delta summary sentence SHALL state:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M SHALL be integers. Non-integer is PROHIBITED.

EXIT (Gate-1):
  Schema B SHALL be complete per contract. NEW above PRIOR. All NEW-artifact Cal cells filled.
  Delta sentence written with integer values for N and M.
  Phase 1 SHALL NOT advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

ENTRY:
  Gate-1 passed. All NEW-artifact Cal cells filled. Schema B Cal dependency satisfied.

JOB:
  Read full content of every artifact classified NEW in Schema B.
  PRIOR artifacts SHALL NOT be read in this phase.

EXIT (Gate-2):
  All NEW artifacts SHALL have been read.
  Phase 2 SHALL NOT advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

ENTRY:
  Gate-2 passed. All NEW artifacts read. Schema A defense arguments available.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in a NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA: both YES.
  PRIOR-ONLY: Condition 2 NO — annotate "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations SHALL NOT support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Audit NEW artifacts for cross-artifact contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found.
  NO CHANGE wins because: [specific artifact reference]."

EXIT (Gate-3):
  Delta detections SHALL be documented. Conflict audit SHALL have a typed result.
  Phase 3 SHALL NOT advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. SHALL fire before any Schema C column is filled.
  Confirm: (1) Gate-3 passed. (2) All NEW-artifact Cal cells in Schema B filled
  (Schema B Cal dependency satisfied). (3) Schema C Inertia Justification labeled
  [MANDATORY] per TABLE SCHEMAS section.
  Write WS-2 MILESTONE. Opening any Schema C row before WS-2 MILESTONE is PROHIBITED.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 passed. WS-2 MILESTONE written. Schema B Cal dependency satisfied.
  No Schema C rows have been opened.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C — breach conditions in force):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Inertia Justification cells SHALL be checked against BANNED FORMS before writing.
  Defense Defeated SHALL cite Schema A row number. Prose alone is PROHIBITED.
  For each absent proposal type, write a typed null declaration per WS-3 below.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB.
Null declarations SHALL use mandatory template:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Reason cells SHALL be checked against BANNED FORMS before writing.
  "no change needed" is PROHIBITED. "nothing to add" is PROHIBITED.
  Any banned form SHALL disqualify the null declaration.
  Null declaration reason cells SHALL NOT receive a scope exemption.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C SHALL be complete per contract. All cells filled. All absent types have typed nulls.
  All Inertia and null reason cells SHALL have been checked against BANNED FORMS.
  strategy.md SHALL NOT be modified before user confirmation is received.
  Phase 4 SHALL NOT advance without passing Gate-4.
  Stop. Verify every cell filled and every null uses typed template. Halt here.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md are listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. strategy.md SHALL NOT be written before user reply. Halt here.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
Do not add unrequested changes.
```
