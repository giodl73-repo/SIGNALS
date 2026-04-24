# topic-plan Skill Variations — Round 9 (2026-03-15)

Rubric: v9 (C-01–C-34, max 100)
New criteria this round: C-31 (Named phase lifecycle template), C-32 (Artifact-to-register
calibration column), C-33 (Inverted artifact sequence with upfront calibration), C-34 (Compound
audit structure — spine + lifecycle)

---

## Round 9 Design Notes

The previous round surfaced four structural patterns across variations that have now been
promoted into rubric criteria:

1. **C-31 from prior V-02** — V-02's `ENTRY / JOB / EXIT` slots made the stop gate a named
   structural position (EXIT) rather than a trailing sentence. C-31 formalizes: each phase
   must declare three named slots; EXIT is the architectural home for the in-phase stop gate;
   a stop gate in running text outside an EXIT slot does not satisfy this criterion.

2. **C-32 from prior V-05** — V-05's calibration column made defense-register-row binding a
   table-fill operation rather than a discretionary inline citation. C-32 formalizes: the
   inventory table must have a dedicated "Cal" column mapping each artifact row to specific
   defense register row numbers; an inline parenthetical in prose does not satisfy this.

3. **C-33 from prior V-05** — V-05 sorted NEW artifacts before PRIOR in the inventory and
   completed calibration before opening proposals. C-33 formalizes: the ordering creates a
   hard architectural dependency — calibration is causally upstream of proposals, not
   retroactively filled after proposal rows are opened.

4. **C-34 from prior V-04** — V-04's hybrid structure yielded two independent audit paths:
   scan the write-surface register headers (spine), scan the EXIT slots (lifecycle). C-34
   formalizes: both structures must be present; one audit path is not redundant with the other.

**Previous round gap analysis:**

| Gap | Description | R9 fix |
|-----|-------------|--------|
| C-31 partial | Stop gates present in phases but not in named EXIT slots; a stop gate in running text drifts on revision | All five R9 designs use ENTRY/JOB/EXIT in every phase with EXIT as structural home |
| C-32 partial | Defense register row citations appeared as inline prose or parentheticals, not as a dedicated named column | All five R9 designs declare a named calibration column (Cal or equivalent) in the inventory table schema |
| C-33 partial | Calibration could be filled retroactively after proposals were written | All five R9 designs state an explicit ordering constraint: ALL NEW-artifact Cal cells must be filled before any proposal row opens |
| C-34 missing | Skills had either a write-surface register OR per-phase lifecycle slots, but not both declared as distinct audit paths | All five R9 designs declare both audit paths explicitly; C-34 requires each to be present as named structure |

**Round 9 single-axis and combined choices:**

| Variation | Axis | Primary mechanism |
|-----------|------|-------------------|
| V-01 | Lifecycle emphasis | ENTRY/JOB/EXIT as bold named sub-sections; EXIT is load-bearing structural position for stop gate |
| V-02 | Output format | Each phase prefaced by a three-row phase-spec table; all table schemas declared upfront |
| V-03 | Inertia framing | Defense register as document spine; calibration column = "Defenses Implicated"; all language frames change as defense-defeat |
| V-04 | Combined (lifecycle + role sequence) | Phase lifecycle template declared upfront as reusable pattern; calibration protocol is its own inter-phase section; explicit role sequence constraints |
| V-05 | Combined (all axes) | Compound audit structure declared upfront with two named audit paths; calibration-first ordering named as architectural constraint with violation condition |

---

## V-01: Lifecycle Emphasis — ENTRY/JOB/EXIT as Named Structural Positions

**Variation axis**: Lifecycle emphasis — each phase explicitly declares three named sub-sections:
`ENTRY` (preconditions), `JOB` (work instructions), `EXIT` (completion gate). The EXIT slot is
the architectural home for the in-phase stop gate required by C-12. The phase lifecycle template
is declared once at the top and every phase instantiates it. Stop gates in running text outside
an EXIT slot do not satisfy the template.

**Hypothesis**: When ENTRY/JOB/EXIT are first-class sub-section labels in every phase, the stop
gate becomes architecturally positioned — a reviewer can audit stop gate completeness by scanning
EXIT sections alone. A stop gate that drifts into JOB prose is visually absent from EXIT, making
omission structurally obvious rather than only detectable by reading.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

The default outcome is NO CHANGE to strategy.md. Every proposal carries the burden of proof
against the null: the current strategy is correct until signal evidence proves otherwise.

═══════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
═══════════════════════════════════════════════════════════

This skill is auditable via two independent structural paths. Neither path is redundant.

  AUDIT PATH 1 (Write-Surface Spine): Scan section headers for WS-1, WS-2, WS-3.
    Three write-surface blocks declared in the register below; three section headers must
    appear in execution. Completeness is verifiable without reading phase content.

  AUDIT PATH 2 (Lifecycle Slots): Scan each phase for EXIT slots.
    Every phase contains ENTRY / JOB / EXIT sub-sections. Each EXIT slot houses the in-phase
    stop gate. Completeness is verifiable by scanning EXIT sections without reading JOB content.

═══════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
═══════════════════════════════════════════════════════════

Positioned before Phase 0. Declares all three write-surface enforcement blocks. Audit
completeness by counting WS-N section headers — three rows declared, three headers must appear.

| Row | ID   | Surface Type              | Trigger Condition                                      |
|-----|------|---------------------------|--------------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact is opened    |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before any proposal column is filled   |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each typed null declaration write     |

═══════════════════════════════════════════════════════════
VOCABULARY CONTRACT
═══════════════════════════════════════════════════════════

Two sentinel tokens are in force in all cells, columns, and free-text fields:

| Token | Meaning                               |
|-------|---------------------------------------|
| ??    | Open obligation — unknown or unfilled |
| --    | Closed decision — deliberately absent |

Violation conditions — any of the following is a vocabulary violation:
- Blank cell where ?? is required: vocabulary violation
- ?? token where -- is the correct token: vocabulary violation
- Any banned form in any free-text cell: vocabulary violation
- Non-integer count in the delta summary sentence: integer-enforcement gate failure

BANNED FORMS — disqualified by verbatim match in any justification, inertia, reason, or
null-declaration cell. Writing any of the following is a gate failure:

  "no change needed"    "nothing to add"     "clearly warranted"
  "seems sufficient"    "a few artifacts"    "several artifacts"
  "some signals"        "not necessary"      any non-integer count

Check every free-text cell against this list before writing it.
This check applies to null declaration reason cells equally — null declarations do not
receive a scope exemption from the banned forms constraint.

Integer-enforcement gate: writing "a few", "several", "some", or any non-integer value
in any count field is a gate failure, not a quality concern.

═══════════════════════════════════════════════════════════
PHASE LIFECYCLE TEMPLATE (applied to every phase below)
═══════════════════════════════════════════════════════════

Every phase uses exactly three named sub-sections:

  ENTRY: [Preconditions that must be true before this phase begins]
  JOB:   [Work instructions for this phase]
  EXIT:  [Completion gate — "Do not advance to Phase N+1 without passing this gate."]

The EXIT slot is the structural home for all stop gate language in this phase.
Stop gate language appearing in ENTRY or JOB prose does not satisfy C-12.
An EXIT slot that omits the stop gate instruction is visually absent and auditable by scan.

═══════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
═══════════════════════════════════════════════════════════

ENTRY:
  Topic is known. No signal artifacts have been read. strategy.md has not been opened.

JOB:
  Open strategy.md. Read its full content and extract the last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]
  Record all strategy dimensions, priorities, namespace coverage decisions, and gaps.

  Build the DEFENSE REGISTER table. One row per potential change dimension. For each
  dimension, document the current strategy's active position and its defense argument.
  This table is committed before any signal artifact is read.

  DEFENSE REGISTER (required-cell schema — blank cells are violations):
  | Row | Dimension             | Current Strategy Position      | Defense Argument                          |
  |-----|-----------------------|--------------------------------|-------------------------------------------|
  |  1  | [dimension]           | [current position in strategy] | [why NO CHANGE is the correct outcome]    |
  |  2  | ...                   | ...                            | ...                                       |
  | ... | ...                   | ...                            | ...                                       |

  Every potential change dimension must have a row. Use ?? for cells whose value is
  unknown. Use -- only for dimensions confirmed not applicable to this topic.

EXIT (Gate-0):
  Defense register is complete. Every cell is filled (no blanks; ?? or -- as required).
  Gate-0: No signal artifact may be read until this gate passes.
  Do not advance to Phase 1 without passing Gate-0.
  Stop. Verify every defense register cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

This block fires at Phase 0 EXIT, after Gate-0 passes, before any signal artifact opens.
Confirm:
  1. Gate-0 has passed — defense register table is complete and every cell is filled.
  2. WS-1 MILESTONE has been written in the output.

Writing WS-1 MILESTONE constitutes a declaration that Gate-0 has passed.
Do not open any signal artifact before writing WS-1 MILESTONE.
Halt here if Gate-0 has not passed.

═══════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
═══════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. Defense register complete and all cells filled. WS-1 MILESTONE written.

JOB:
  Locate all signal artifact files for this topic across all 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  SORT ORDER: List all NEW artifacts (date > STRATEGY DATE) above all PRIOR artifacts.
  This ordering is mandatory. The calibration column for all NEW-artifact rows must be
  filled before any proposal row in Phase 4 is opened. This ordering creates a hard
  architectural dependency: calibration precedes proposals, not vice versa.

  INVENTORY TABLE (required-cell schema — blank cells are violations):
  | Artifact Filename     | Date         | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  |-----------------------|--------------|-------------|------------------------------------------|
  | [filename]            | [YYYY-MM-DD] | NEW or PRIOR | [row numbers, e.g., 1,3 or ?? or --]   |
  | ...                   | ...          | ...         | ...                                      |

  CALIBRATION RULES:
  - "Defense Register Rows (Cal)" is MANDATORY. A blank cell is a violation.
  - NEW artifacts: list every defense register row number this artifact potentially
    implicates. Use ?? if the implication is unknown. Use -- if no rows are implicated.
  - PRIOR artifacts: fill Cal or enter -- if no rows are implicated.
  - Do not open a proposal row in Phase 4 until ALL NEW-artifact Cal cells are filled.

  After completing the table, write the mandatory delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Any non-integer form is an integer-enforcement gate failure.

EXIT:
  Inventory table is complete. NEW artifacts appear above PRIOR artifacts.
  All NEW-artifact Cal cells are filled (no blanks; ?? or -- as required).
  Delta summary sentence written with integer values for N and M.
  Do not advance to Phase 2 without passing this gate.
  Stop. Verify all NEW-artifact Cal cells are filled. Halt here.

═══════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
═══════════════════════════════════════════════════════════

ENTRY:
  Phase 1 exit passed. All NEW-artifact Cal cells filled. No proposals open.

JOB:
  Read the full content of every artifact classified NEW in the inventory table.
  Do not read PRIOR artifacts.

EXIT:
  All NEW artifacts read in full.
  Do not advance to Phase 3 without passing this gate.
  Stop. Confirm every NEW artifact has been read. Halt here.

═══════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
═══════════════════════════════════════════════════════════

ENTRY:
  Phase 2 exit passed. All NEW artifacts read. Defense register and strategy content
  known from Phase 0.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts, check two conditions:
    Condition 1: present in at least one NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md content?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations may not support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Check all NEW artifacts for cross-artifact contradictions.
  If contradictions found: document in a CONFLICT REGISTER table.
  If none found, write the typed null form:
    "CONFLICT DETECTION — NULL: No cross-artifact contradictions found.
    NO CHANGE to conflict resolution wins because: [specific artifact reference]."

EXIT:
  Delta detections documented. Conflict audit complete with typed result.
  Delta summary counts are integers (verified in Phase 1 delta summary sentence).
  Do not advance to Phase 4 without passing this gate.
  Stop. Verify conflict audit has a typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

This block fires at Phase 4 ENTRY, before any proposal column is filled.
Before opening the proposals table, confirm all three:
  1. Phase 3 exit passed and conflict audit has a typed result.
  2. All NEW-artifact Cal cells in the inventory table are filled (Phase 1 complete).
  3. The Inertia Justification column is labeled [MANDATORY] in the proposals schema.

Writing WS-2 MILESTONE constitutes a declaration that all three confirmations pass.
Do not fill any proposal column before writing WS-2 MILESTONE. Halt here if any
confirmation fails.

═══════════════════════════════════════════════════════════
Phase 4 — Proposals
═══════════════════════════════════════════════════════════

ENTRY:
  Phase 3 exit passed. WS-2 MILESTONE written. Defense register and Cal column populated.
  All NEW-artifact Cal cells are filled. No proposal row has been opened before this phase.

JOB:
  Produce the PROPOSALS TABLE (required-cell schema — blank cells are violations):

  | Type                  | Proposal    | Before       | After        | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  |-----------------------|-------------|--------------|--------------|-------------------|------------------------------------|--------------------------|
  | ADD/REMOVE/REPRIORITIZE | [description] | [current]  | [proposed]   | [artifact filename] | [specific reason this beats NO CHANGE] | Row [N]            |
  | ...                   | ...         | ...          | ...          | ...               | ...                                | ...                      |

  COLUMN RULES:
  - Evidence Artifact: artifact filename providing direct evidence. Use ?? if no specific
    artifact. A blank cell is a violation.
  - Inertia Justification [MANDATORY]: explain specifically why this beats NO CHANGE.
    Check this cell against the BANNED FORMS list before writing.
    "no change needed" is not an acceptable entry.
    "clearly warranted" is not an acceptable entry.
    Check this cell against the BANNED FORMS list before presenting; any match disqualifies the row.
  - Defense Defeated (Row #): cite the specific defense register row number this proposal
    defeated (e.g., Row 3). A named defense without a row number does not satisfy this column.
    A proposal row that references a defense by prose description only does not satisfy C-22.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

This block fires at each null declaration write in Phase 4 JOB.
Before writing any typed null declaration:
  1. Use the mandatory template:
     "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
  2. Check the reason cell against BANNED FORMS before writing.
     "no change needed" is not an acceptable entry.
     "nothing to add" is not an acceptable entry.
     "not necessary" is not an acceptable entry.
     Check this cell against the BANNED FORMS list before presenting; any match disqualifies.
  3. Reason must cite specific evidence or strategy content, not a generic assertion.

Required null declarations for each absent proposal type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

Writing WS-3 MILESTONE constitutes a declaration that all null declarations use this
template and have been checked against BANNED FORMS.

EXIT:
  Proposals table is complete. Every non-null row has all required cells filled.
  Every absent type has a typed null declaration (ADD — NULL / REMOVE — NULL /
  REPRIORITIZE — NULL). Inertia justification and null declaration reason cells have
  been checked against BANNED FORMS.
  Do not advance to Confirmation Gate without passing this gate.
  Stop. Verify every cell is filled and every null uses the typed template. Halt here.

═══════════════════════════════════════════════════════════
CONFIRMATION GATE
═══════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md are listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Do not modify any file. Halt here and wait for reply.

═══════════════════════════════════════════════════════════
APPLY PHASE (after YES or REVISED only)
═══════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
Do not add unrequested changes.
```

---

## V-02: Output Format — Three-Row Phase-Spec Tables with Upfront Schema Declarations

**Variation axis**: Output format — each phase is prefaced by a three-row phase-spec table
(`ENTRY | JOB | EXIT` as table rows) that declares the phase's preconditions, work, and
gate condition. All table schemas (defense register, inventory, proposals) are declared once
in a `TABLE SCHEMAS` section before Phase 0. The calibration column schema is specified there
and the inventory phase references it. Banned forms appear in their own `BANLIST TABLE`.

**Hypothesis**: When the lifecycle is a table rather than sub-sections, blank cells in the phase-spec
table are visually obvious violations. An auditor checking EXIT slot completeness across phases
scans the bottom row of each phase-spec table — the structural check is mechanical rather than
requiring prose reading. Upfront schema declarations create a single authoritative reference,
reducing the chance that a column is omitted when the phase is executed.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. A proposal earns its place by defeating the null.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE
════════════════════════════════════════════════════════════

Two independent audit paths. Both must be present.

PATH 1 (Spine): Count WS-1, WS-2, WS-3 section headers. Register declares 3 rows.
PATH 2 (Lifecycle): Scan phase-spec tables for EXIT row stop gate text in every phase.
Neither path is redundant. A skill with only one structural layer fails C-34.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface             | Trigger                                         |
|-----|------|---------------------|-------------------------------------------------|
|  1  | WS-1 | Pre-read barrier    | Phase 0 EXIT row — before any signal artifact   |
|  2  | WS-2 | Schema boundary     | Phase 4 ENTRY row — before proposal column fill |
|  3  | WS-3 | Null decl template  | Phase 4 JOB — at each null declaration write    |

Three rows declared. Three WS-N headers must appear. Verify by counting section headers.

════════════════════════════════════════════════════════════
TABLE SCHEMAS
════════════════════════════════════════════════════════════

All required-cell tables are declared here. Blank cells in any required column are violations.
Use ?? for open obligations (unknown/unfilled). Use -- for closed decisions (not applicable).

SCHEMA A — DEFENSE REGISTER
| Row | Dimension | Current Strategy Position | Defense Argument |
Required columns: Row (integer), Dimension, Current Strategy Position, Defense Argument.
All cells required. ?? permitted. -- permitted for not-applicable rows only.

SCHEMA B — SIGNAL INVENTORY
| Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
Sort order: NEW artifacts above PRIOR artifacts (mandatory).
Required columns: all four. Cal column is MANDATORY — blank is a violation.
NEW-artifact Cal cells must be filled before any Phase 4 proposal row opens.

SCHEMA C — PROPOSALS TABLE
| Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
Required columns: all seven. Blank cells are violations.
Defense Defeated (Row #): must cite row number from defense register, not prose description.
Inertia Justification: must pass BANLIST check before writing.

SCHEMA D — PHASE-SPEC TABLE (applied to each phase)
| Slot  | Content                                                  |
|-------|----------------------------------------------------------|
| ENTRY | [Preconditions true before this phase begins]            |
| JOB   | [Work instructions]                                      |
| EXIT  | [Stop gate: "Do not advance to Phase N+1 without this."] |
EXIT row is the structural home for the stop gate. Missing EXIT = missing stop gate.

════════════════════════════════════════════════════════════
VOCABULARY CONTRACT + BANLIST
════════════════════════════════════════════════════════════

Sentinel tokens (two-tier, in force everywhere):
| Token | Meaning |
|-------|---------|
| ??    | Open obligation — unknown or unfilled |
| --    | Closed decision — deliberately absent |

Violation conditions:
- Blank cell where ?? is required: vocabulary violation
- ?? where -- is correct: vocabulary violation
- Any banned form in any free-text cell: vocabulary violation
- Non-integer count: integer-enforcement gate failure

BANLIST TABLE (verbatim — match triggers disqualification):
| Banned Form           | Context where banned              | Violation type             |
|-----------------------|-----------------------------------|----------------------------|
| "no change needed"    | Any justification or null reason  | Vocabulary violation       |
| "nothing to add"      | Any justification or null reason  | Vocabulary violation       |
| "clearly warranted"   | Any justification or null reason  | Vocabulary violation       |
| "seems sufficient"    | Any justification or null reason  | Vocabulary violation       |
| "a few artifacts"     | Any count context                 | Integer-enforcement failure |
| "several artifacts"   | Any count context                 | Integer-enforcement failure |
| "some signals"        | Any count context                 | Integer-enforcement failure |
| any non-integer count | Delta summary or count cell       | Integer-enforcement failure |

Check every free-text cell against the BANLIST TABLE before writing.
Null declaration reason cells are not exempt — banned forms are banned everywhere.

Integer-enforcement gate: writing "a few", "several", "some", or any non-integer value
is a gate failure. Fuzziness is a named failure condition.

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                |
|-------|------------------------------------------------------------------------|
| ENTRY | Topic known. No signal artifacts read. strategy.md not yet opened.     |
| JOB   | Open strategy.md. Read full content. Extract date. Build SCHEMA A table.|
| EXIT  | Gate-0: Defense register complete, all cells filled. Do not advance to Phase 1 without passing Gate-0. Stop. Verify defense register. Halt here. |

Execute JOB:
  Open strategy.md. Read full content and extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]
  Record all strategy dimensions, priorities, namespace coverage decisions.

  Build SCHEMA A — DEFENSE REGISTER:
  | Row | Dimension | Current Strategy Position | Defense Argument |
  (One row per potential change dimension. All cells required. ?? or -- as appropriate.)

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT. Before opening any signal artifact:
  Confirm: Gate-0 passed (defense register complete, all cells filled).
  Write WS-1 MILESTONE as declaration that Gate-0 has passed.
  Do not read any signal artifact before this milestone is written.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                          |
|-------|----------------------------------------------------------------------------------|
| ENTRY | Gate-0 passed. WS-1 MILESTONE written. Defense register complete.                |
| JOB   | Locate all signal artifacts (9 namespaces). Build SCHEMA B table. Write delta sentence. |
| EXIT  | Gate-1: Inventory complete. NEW artifacts above PRIOR. All NEW-artifact Cal cells filled. Delta sentence with integer counts. Do not advance to Phase 2. Stop. Verify Cal cells. Halt here. |

Execute JOB:
  Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (NEW artifacts above PRIOR — mandatory sort):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  (All NEW-artifact Cal cells must be filled before any Phase 4 proposal row opens.)

  Write mandatory delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Any non-integer form is a gate failure.

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
  Read full content of every artifact classified NEW in the inventory table.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                        |
|-------|--------------------------------------------------------------------------------|
| ENTRY | Gate-2 passed. All NEW artifacts read. Defense register known from Phase 0.    |
| JOB   | Delta detection (two-condition gate). Conflict audit. Typed results for both.  |
| EXIT  | Gate-3: Delta detections documented. Conflict audit has typed result (table or typed NULL). Integer counts verified. Do not advance to Phase 4. Stop. Halt here. |

Execute JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: in a NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations may not support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Check for cross-artifact contradictions among NEW artifacts.
  If contradictions: CONFLICT REGISTER table.
  If none: typed null form:
    "CONFLICT DETECTION — NULL: No cross-artifact contradictions found.
    NO CHANGE wins because: [specific reference to artifact content]."

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before filling any proposal column:
  Confirm: (1) Gate-3 passed. (2) All NEW-artifact Cal cells filled. (3) Schema C
  Inertia Justification column labeled [MANDATORY].
Write WS-2 MILESTONE as declaration that all three confirmations pass.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

Phase-spec (Schema D):
| Slot  | Content                                                                        |
|-------|--------------------------------------------------------------------------------|
| ENTRY | Gate-3 passed. WS-2 MILESTONE written. Cal column filled. No prior proposal rows. |
| JOB   | Build SCHEMA C proposals table. Typed null declarations. WS-3 at each null.    |
| EXIT  | Gate-4 (Confirmation): Proposals table complete. All null types declared. All cells filled. Inertia and null reason cells checked against BANLIST. Stop. Do not touch strategy.md. Halt here. |

Execute JOB:
  Build SCHEMA C — PROPOSALS TABLE:
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |

  For each absent proposal type, use WS-3 template (below).

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB. Use mandatory template:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."

Before writing the reason cell: check against BANLIST TABLE.
  "no change needed" is not an acceptable entry — check this cell before presenting.
  "nothing to add" is not an acceptable entry — check this cell before presenting.
  Any banned form in the reason cell disqualifies the null declaration.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations. NO CHANGE wins because: [specific reason].

Reason cells must cite specific artifact or strategy evidence, not generic assertions.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not modify strategy.md or any file. Halt here and wait for user reply.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
```

---

## V-03: Inertia Framing — Defense Register as Document Spine

**Variation axis**: Inertia framing — the defense register is the document's primary structural
element. All downstream phases are framed in terms of defeating or upholding the defense. The
calibration column is labeled "Defenses Implicated" to make the threat assessment the primary
purpose of classification. Proposal type language frames change as defense-defeat: a proposal
"defeats Defense Row N" rather than "proposes an addition." The vocabulary contract frames banned
forms as inadmissible rebuttals rather than quality concerns.

**Hypothesis**: When inertia pervades every level — defense register as spine, calibration as
threat assessment, proposals as indictments, banned forms as inadmissible rebuttals — the burden
of proof is institutionalized in the language rather than declared as a policy. The model cannot
write a proposal without naming the specific defense it defeats, making evidence-linked inertia
structurally mandatory rather than aspirational.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

THE PREMISE: The current strategy is correct. It will remain correct unless signal evidence
defeats a specific defense. A proposal is an indictment: it claims that a specific defense
argument in the defense register is wrong. The burden of proof is on the indictment.
If no defense is defeated, the outcome is NO CHANGE to strategy.md.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan for WS-1, WS-2, WS-3 section headers.
  Three write-surface enforcement blocks declared below; three headers must appear.

AUDIT PATH 2 (Lifecycle Slots): Scan every phase for ENTRY / JOB / EXIT sub-sections.
  EXIT is the structural home for each phase's stop gate. Scan EXIT sections to audit
  stop gate coverage without reading JOB content.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface              | Trigger                                          |
|-----|------|----------------------|--------------------------------------------------|
|  1  | WS-1 | Pre-read barrier     | Phase 0 EXIT — before any signal artifact opened |
|  2  | WS-2 | Schema boundary      | Phase 4 ENTRY — before proposal column fill      |
|  3  | WS-3 | Null decl template   | Phase 4 JOB — at each null declaration write     |

════════════════════════════════════════════════════════════
VOCABULARY CONTRACT — ADMISSIBILITY RULES
════════════════════════════════════════════════════════════

Two sentinel tokens:
  ??  — open obligation (implication unknown; the defense has not yet been assessed)
  --  — closed decision (defense confirmed not implicated by this artifact)

Violation conditions:
  - Blank cell where ?? is required: admissibility violation
  - ?? where -- is correct: admissibility violation
  - Any inadmissible rebuttal form in any free-text cell: disqualified
  - Non-integer count in any count cell: integer-enforcement gate failure

INADMISSIBLE REBUTTALS — the following forms are inadmissible in any justification,
defense argument, inertia justification, or null declaration reason cell. The defense
must cite specific evidence. Generic rebuttals are not accepted:

  "no change needed"    "nothing to add"     "clearly warranted"
  "seems sufficient"    "a few artifacts"    "several artifacts"
  "some signals"        "not necessary"      any non-integer count

These strings are banned by verbatim match. Check every free-text cell against this
list before writing. Null declaration reason cells are not exempt — inadmissible
rebuttals are disqualified everywhere, including null declarations.

Integer-enforcement gate: writing "a few", "several", "some", or any non-integer value
is a gate failure. The count must be an integer.

Violation enumeration:
  - Blank cell where ?? required: admissibility violation
  - ?? where -- correct: admissibility violation
  - Inadmissible rebuttal in any free-text cell: admissibility violation
  - Non-integer count: integer-enforcement gate failure

════════════════════════════════════════════════════════════
Phase 0 — ARM THE DEFENSE REGISTER
════════════════════════════════════════════════════════════

ENTRY:
  No signal artifacts have been read. The defense has not been articulated.
  This phase arms the defense register before any signal evidence is examined.

JOB:
  Open strategy.md. Read its full content and extract the last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build the DEFENSE REGISTER. Each row is a dimension the current strategy actively
  defends. The defense argument is why NO CHANGE is the correct outcome for this
  dimension. This register is committed before any signal artifact is read.

  DEFENSE REGISTER:
  | Row | Dimension         | Current Strategy Position      | Defense Argument (why NO CHANGE)          |
  |-----|-------------------|--------------------------------|-------------------------------------------|
  |  1  | [dimension]       | [current position]             | [specific reason status quo is correct]   |
  |  2  | ...               | ...                            | ...                                       |

  All cells required. ?? for unknown cells. -- only for confirmed not-applicable rows.
  Check defense argument cells against INADMISSIBLE REBUTTALS before writing each one.
  "no change needed" is not an acceptable defense argument — check before writing.

EXIT (Gate-0):
  Defense register is complete. All cells filled (no blanks; ?? or -- as required).
  Defense argument cells checked against inadmissible rebuttals.
  Gate-0: The defense is armed. No signal artifact may be examined until Gate-0 passes.
  Do not advance to Phase 1 without passing Gate-0.
  Stop. Verify every defense register cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

This block fires at Phase 0 EXIT. The defense has been armed. Before examining any
signal evidence, confirm Gate-0 has passed (defense register complete, all cells filled).
Write WS-1 MILESTONE. This constitutes a declaration that Gate-0 has passed.
Do not open any signal artifact before writing WS-1 MILESTONE. The signal evidence
is not examined until the defense is ready to receive it.

════════════════════════════════════════════════════════════
Phase 1 — EXAMINE THE EVIDENCE (Signal Inventory with Calibration)
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. Defense armed. WS-1 MILESTONE written. No proposals open.
  Every NEW artifact will be assessed against the defense before proposals are written.

JOB:
  Locate all signal artifact files for this topic across all 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  THREAT ASSESSMENT PROTOCOL:
  - NEW artifacts (date > STRATEGY DATE) are the potential challengers to the defense.
  - Sort: NEW artifacts appear above PRIOR artifacts in the inventory table.
    The challengers are examined before the defense is re-articulated in proposals.
  - For each NEW artifact, assess: which defense register rows does this artifact
    potentially implicate? This is the calibration step. It must be complete before
    any proposal row opens.
  - Writing a proposal row before ALL NEW-artifact calibration cells are filled is a
    sequence violation — it allows proposals to shape calibration rather than the reverse.

  SIGNAL INVENTORY TABLE (required-cell schema — blank cells are violations):
  | Artifact Filename      | Date         | NEW / PRIOR | Defenses Implicated (Cal) [MANDATORY] |
  |------------------------|--------------|-------------|----------------------------------------|
  | [filename]             | [YYYY-MM-DD] | NEW or PRIOR| [defense register row #s, ?? or --]   |
  | ...                    | ...          | ...         | ...                                    |

  Cal column is MANDATORY. A blank cell is a violation regardless of other content.
  After the table, write the delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Non-integer form is a gate failure.

EXIT:
  Inventory complete. NEW artifacts appear above PRIOR artifacts.
  ALL NEW-artifact Cal cells filled (no blanks; ?? or -- as required).
  Delta summary sentence written with integer values.
  Do not advance to Phase 2 without passing this gate.
  Stop. Verify all NEW-artifact Cal cells are filled. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read the Challengers
════════════════════════════════════════════════════════════

ENTRY:
  Phase 1 exit passed. All NEW-artifact Cal cells filled. Defense register armed.
  The calibrated threat assessment precedes the detailed reading.

JOB:
  Read the full content of every artifact classified NEW in the inventory table.
  Do not read PRIOR artifacts. The challengers are read; the defense awaits the verdict.

EXIT:
  All NEW artifacts read in full.
  Do not advance to Phase 3 without passing this gate.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Contradiction Audit
════════════════════════════════════════════════════════════

ENTRY:
  Phase 2 exit passed. Challengers read. Defense register and strategy content known.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in a NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES — this observation potentially defeats a defense.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY may not support ADD or REPRIORITIZE proposals. The defense holds.

  CONTRADICTION AUDIT — Check all NEW artifacts for cross-artifact contradictions.
  If contradictions found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions among challengers.
    NO CHANGE wins because: [specific artifact reference]."

EXIT:
  Delta detections documented. Contradiction audit complete with typed result.
  Do not advance to Phase 4 without passing this gate.
  Stop. Verify conflict audit has a typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. The defense verdict is about to be rendered in the proposals
table. Before any proposal column is filled, confirm:
  1. Phase 3 exit passed. Delta detections and conflict audit documented.
  2. ALL NEW-artifact Cal cells in the inventory are filled (Phase 1 complete).
  3. Inertia Justification column is labeled [MANDATORY] in the proposals schema.
Write WS-2 MILESTONE. This constitutes a declaration that all three confirmations pass.
Do not fill any proposal column before WS-2 MILESTONE is written.

════════════════════════════════════════════════════════════
Phase 4 — RENDER THE VERDICT (Proposals)
════════════════════════════════════════════════════════════

ENTRY:
  Phase 3 exit passed. WS-2 MILESTONE written. Defense register armed.
  Cal column filled. No proposal row has been opened before this phase.

JOB:
  Each proposal row is an indictment: it claims that the current strategy is wrong
  about a specific dimension and that a specific signal defeated the defense.

  PROPOSALS TABLE (required-cell schema — blank cells are violations):
  | Type         | Proposal    | Before       | After        | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  |--------------|-------------|--------------|--------------|-------------------|------------------------------------|--------------------------|
  | ADD / REMOVE / REPRIORITIZE | [description] | [current] | [proposed] | [artifact filename] | [specific reason this defeats NO CHANGE] | Row [N] |

  Defense Defeated (Row #): cite the specific row number from the defense register that
  this proposal defeats. A prose description without a row number is inadmissible.
  Inertia Justification: cite specific evidence. Check against inadmissible rebuttals
  before writing. "no change needed" is not an acceptable entry. Check this cell against
  the INADMISSIBLE REBUTTALS list before presenting; any match disqualifies the row.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

When no indictment is possible for a proposal type, render the acquittal:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."

The reason must cite specific evidence. Generic acquittals are inadmissible:
  "no change needed" is inadmissible — check before writing.
  "nothing to add" is inadmissible — check before writing.
Check this cell against the INADMISSIBLE REBUTTALS list before presenting; any match
disqualifies the null declaration.

Required acquittals for each absent type:
  ADD — NULL: No indictments for addition. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No indictments for removal. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No indictments for reprioritization. NO CHANGE wins because: [specific reason].

EXIT:
  Proposals table complete. Every non-null row has all required cells filled.
  Every absent type acquitted with a typed null declaration.
  All justification and reason cells checked against inadmissible rebuttals.
  Do not advance to Confirmation Gate without passing this gate.
  Stop. Verify every cell filled and every absent type acquitted. Halt here.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table (the verdict). Write:
"The verdict on the strategy is above. The default is NO CHANGE — the defense holds
unless a proposal is confirmed. Apply these changes? Reply YES, NO, or REVISED."

Stop. Do not write to strategy.md. Do not modify any file. Halt here and await reply.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply confirmed proposals. Write exactly what was approved. The defense is overturned
only for approved rows. All other dimensions retain NO CHANGE status.
```

---

## V-04: Combined (Lifecycle Emphasis + Role Sequence) — Phase Template with Calibration Protocol as Inter-Phase Section

**Variation axes combined**: Lifecycle emphasis (PHASE LIFECYCLE TEMPLATE declared as a named
reusable pattern) + Role sequence (explicit precedes/follows constraints; Calibration Protocol
is its own named section between Phase 1 and Phase 2, not embedded in a phase)

**Hypothesis**: Declaring the phase lifecycle template as a standalone section that phases
reference — rather than repeating ENTRY/JOB/EXIT as content within phases — creates a single
authoritative lifecycle contract. When the Calibration Protocol is an inter-phase section
(not a sub-element of inventory), it becomes a named architectural boundary: Phase 1 produces
the inventory, Calibration Protocol binds artifacts to defenses, Phase 2 reads the bound
artifacts. A reviewer scanning section headers sees the calibration obligation explicitly,
independent of reading the inventory phase content.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

The default outcome is NO CHANGE to strategy.md. Evidence changes the strategy.
Absence of evidence sustains it. The burden is on the change.

════════════════════════════════════════════════════════════
EXECUTION ARCHITECTURE
════════════════════════════════════════════════════════════

This section declares the full execution contract before any phase runs.

COMPOUND AUDIT STRUCTURE — two independent audit paths:
  PATH 1 (Spine): Scan section headers for WS-1, WS-2, WS-3.
    Write-surface register below declares 3 rows; 3 headers must appear.
  PATH 2 (Lifecycle): Scan every phase for EXIT slot stop gates.
    PHASE LIFECYCLE TEMPLATE below declares the EXIT slot as structural home.
    Neither path is redundant with the other.

PHASE SEQUENCE (role order — each phase follows the one named):
  Phase 0: Strategy Read + Defense Register    → Precedes Phase 1
  Phase 1: Signal Inventory                    → Follows Phase 0; Precedes Calibration Protocol
  [CALIBRATION PROTOCOL]                       → Follows Phase 1; Precedes Phase 2
  Phase 2: Read NEW Artifacts                  → Follows Calibration Protocol; Precedes Phase 3
  Phase 3: Delta Detection + Conflict Audit    → Follows Phase 2; Precedes Phase 4
  Phase 4: Proposals                           → Follows Phase 3; Precedes Confirmation Gate

CALIBRATION ARCHITECTURAL CONSTRAINT:
  Calibration Protocol is a named inter-phase section, not a sub-task of inventory.
  All NEW-artifact rows in the inventory table must have Cal cells filled during
  Calibration Protocol before Phase 2 begins. Opening a proposal row before the
  Calibration Protocol section completes is a sequence violation.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface             | Trigger                                         |
|-----|------|---------------------|-------------------------------------------------|
|  1  | WS-1 | Pre-read barrier    | Phase 0 EXIT — before any signal artifact reads |
|  2  | WS-2 | Schema boundary     | Phase 4 ENTRY — before proposal column fill     |
|  3  | WS-3 | Null decl template  | Phase 4 JOB — at each null declaration write    |

Three rows declared. Three WS-N section headers must appear below.

════════════════════════════════════════════════════════════
PHASE LIFECYCLE TEMPLATE
════════════════════════════════════════════════════════════

Every phase instantiates this pattern:

  ENTRY: [Preconditions — what must be true before this phase begins]
  JOB:   [Work instructions — what this phase produces]
  EXIT:  [Stop gate — "Do not advance to [next phase] without passing this gate." +
          completion criteria all cells filled per required-cell schema]

The EXIT slot is the load-bearing structural position for the stop gate.
Stop gate language in ENTRY prose or JOB prose does not satisfy this template.
A phase whose EXIT slot omits the stop gate instruction is visually defective.

════════════════════════════════════════════════════════════
VOCABULARY CONTRACT
════════════════════════════════════════════════════════════

Two sentinel tokens — in force everywhere:
  ??  Open obligation (unknown or not yet assessed)
  --  Closed decision (confirmed not applicable)

Violation enumeration:
  - Blank where ?? required: vocabulary violation
  - ?? where -- correct: vocabulary violation
  - Banned form in any free-text cell: vocabulary violation
  - Non-integer count: integer-enforcement gate failure

BANNED FORMS (verbatim — disqualified by exact match):
  "no change needed"    "nothing to add"     "clearly warranted"
  "seems sufficient"    "a few artifacts"    "several artifacts"
  "some signals"        "not necessary"      any non-integer count

Check every free-text cell against this list before writing.
Null declaration reason cells are not exempt — banned forms are banned everywhere.

Integer-enforcement gate: "a few", "several", "some", or any non-integer form in any
count cell is a gate failure, not a style concern.

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

(instantiates PHASE LIFECYCLE TEMPLATE)

ENTRY:
  Topic known. No signal artifacts read. strategy.md not yet opened.

JOB:
  Open strategy.md. Read full content. Extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build the DEFENSE REGISTER (required-cell schema):
  | Row | Dimension | Current Strategy Position | Defense Argument |

  One row per potential change dimension. All cells required. ?? permitted.
  -- permitted only for confirmed not-applicable dimensions.

EXIT (Gate-0):
  Defense register complete. All cells filled (no blanks; ?? or -- as required).
  Do not advance to Phase 1 without passing Gate-0.
  Gate-0: No signal artifact may be read until this gate passes.
  Stop. Verify every defense register cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT, after Gate-0. Before any signal artifact is opened:
  Confirm Gate-0 passed (defense register complete, all cells filled).
Write WS-1 MILESTONE as declaration that Gate-0 has passed.
Do not read any signal artifact before this milestone is written.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory
════════════════════════════════════════════════════════════

(instantiates PHASE LIFECYCLE TEMPLATE)

ENTRY:
  Gate-0 passed. WS-1 MILESTONE written. Defense register complete.

JOB:
  Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  SIGNAL INVENTORY TABLE (required-cell schema — blank cells are violations):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |

  SORT ORDER: NEW artifacts (date > STRATEGY DATE) above PRIOR artifacts. Mandatory.
  Cal column is MANDATORY. Leave Cal cells with ?? for NEW artifacts that will be
  assessed in the Calibration Protocol section (next). Do not fill Cal cells yet —
  the Calibration Protocol fills them.

  After the table, write the delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Any non-integer form is a gate failure.

EXIT:
  Inventory table complete. NEW artifacts appear above PRIOR artifacts.
  Delta summary sentence written with integer values.
  Do not advance to Calibration Protocol without passing this gate.
  Stop. Verify the inventory table is complete and sort order is correct. Halt here.

════════════════════════════════════════════════════════════
CALIBRATION PROTOCOL
════════════════════════════════════════════════════════════

This is a named inter-phase section, not a sub-task of Phase 1 or Phase 2.
It executes between Phase 1 and Phase 2 and must complete before Phase 2 begins.

PURPOSE: Map every NEW-artifact row in the inventory to the specific defense register
row numbers it potentially implicates. This binding is the input to Phase 2 reading
and the evidence base for Phase 4 proposals. Calibration before reading prevents
proposals from shaping calibration retroactively.

For each NEW artifact in the inventory table, fill its Cal cell:
  - List every defense register row number this artifact potentially implicates
    (e.g., 1, 3 or 2 or 4,7).
  - Use ?? if the implication is unknown pending reading (unusual — usually assessable
    from filename and date alone).
  - Use -- if this artifact clearly implicates no defense register rows.

For PRIOR artifacts: fill Cal cells or enter -- if no rows are implicated.

CALIBRATION COMPLETION GATE:
  All NEW-artifact Cal cells must be filled before Phase 2 begins.
  A blank Cal cell in a NEW-artifact row is a calibration protocol violation.
  Do not advance to Phase 2 until all NEW-artifact Cal cells are filled.
  Stop. Verify all NEW-artifact Cal cells. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

(instantiates PHASE LIFECYCLE TEMPLATE)

ENTRY:
  Calibration Protocol complete. All NEW-artifact Cal cells filled.
  No proposals open. Phase 1 and Calibration Protocol both passed.

JOB:
  Read full content of every artifact classified NEW in the inventory table.
  Do not read PRIOR artifacts.

EXIT:
  All NEW artifacts read in full.
  Do not advance to Phase 3 without passing this gate.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

(instantiates PHASE LIFECYCLE TEMPLATE)

ENTRY:
  Phase 2 exit passed. All NEW artifacts read. Defense register and strategy known.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: in a NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY may not support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Check NEW artifacts for cross-artifact contradictions.
  If contradictions: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found.
    NO CHANGE wins because: [specific artifact reference]."

EXIT:
  Delta detections documented. Conflict audit typed result present.
  Do not advance to Phase 4 without passing this gate.
  Stop. Verify conflict audit has a typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before any proposal column is filled:
  1. Phase 3 exit passed.
  2. All NEW-artifact Cal cells filled (Calibration Protocol complete).
  3. Inertia Justification column is labeled [MANDATORY] in the schema.
Write WS-2 MILESTONE as declaration all three confirmations pass.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

(instantiates PHASE LIFECYCLE TEMPLATE)

ENTRY:
  Phase 3 exit passed. WS-2 MILESTONE written. Calibration Protocol complete.
  No proposal row has been opened before this phase.

JOB:
  PROPOSALS TABLE (required-cell schema — blank cells are violations):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |

  Defense Defeated (Row #): cite specific row number from defense register (e.g., Row 3).
  Prose description without row number does not satisfy this column.
  Inertia Justification [MANDATORY]: check against banned forms before writing.
  "no change needed" is not acceptable — check this cell before presenting.

  For each absent proposal type, write a typed null declaration using WS-3 template.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Mandatory template for each absent proposal type:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."

Before writing the reason cell: check against banned forms.
  "no change needed" is not an acceptable entry — check this cell before presenting.
  "nothing to add" is not an acceptable entry — check this cell before presenting.
Any banned form in the reason cell disqualifies the null declaration.

Required declarations for each absent type:
  ADD — NULL: No additions. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations. NO CHANGE wins because: [specific reason].

EXIT:
  Proposals table complete. All cells filled. Every absent type has a typed null
  declaration. Inertia and null reason cells checked against banned forms.
  Do not advance to Confirmation Gate without passing this gate.
  Stop. Verify every cell filled and all absent types declared. Halt here.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md above. Default is NO CHANGE.
Apply? Reply YES, NO, or REVISED with modifications."

Stop. Do not modify strategy.md or any file. Halt here.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply confirmed proposals to strategy.md. Write exactly what was approved.
```

---

## V-05: Combined (All Axes) — Compound Audit Structure with Calibration-First Architectural Constraint

**Variation axes combined**: Output format (upfront ARCHITECTURE DECLARATION naming both audit
paths) + Lifecycle emphasis (ENTRY/JOB/EXIT in compact inline form) + Inertia framing
(defense register as spine, all language frames change as evidence-based) + Role sequence
(calibration-first ordering named as an architectural constraint with a named violation condition)

**Hypothesis**: Declaring BOTH audit paths in an upfront ARCHITECTURE DECLARATION block — not
just registering write surfaces but explicitly naming ENTRY/JOB/EXIT as Audit Path 2 — makes
C-34 self-verifying. An auditor reads the architecture declaration and knows exactly what two
structural patterns to check. Naming the calibration-first ordering as an "ARCHITECTURAL
CONSTRAINT" (not a sequencing instruction) with a named violation condition ("SEQUENCE VIOLATION")
makes the constraint enforceable: the model can detect its own violation and halt.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

The default outcome is NO CHANGE to strategy.md. Every proposal is a claim that the current
strategy is wrong about something. Claims require evidence. The burden is on the change.

════════════════════════════════════════════════════════════
ARCHITECTURE DECLARATION
════════════════════════════════════════════════════════════

This block declares the full structural contract. The model may audit its execution against
this block at any point. All gates, write surfaces, lifecycle slots, and constraints are
declared here before any phase runs.

COMPOUND AUDIT STRUCTURE — two independent audit paths:

  AUDIT PATH 1 — Write-Surface Spine:
    Three write-surface enforcement blocks are declared in the WRITE SURFACE REGISTER below.
    Each block appears as a first-class section header (WS-1, WS-2, WS-3).
    Completeness is auditable by scanning section headers alone — no phase content required.
    Three rows declared; three headers must appear.

  AUDIT PATH 2 — Lifecycle Slots:
    Every phase uses ENTRY / JOB / EXIT slots. EXIT is the structural home for the stop gate.
    Completeness is auditable by scanning EXIT slots alone — no JOB content required.
    A stop gate in JOB prose or ENTRY prose does not satisfy this path.

  Neither path is redundant with the other. A skill with only Path 1 or only Path 2
  does not satisfy C-34. Both paths must be present and independently auditable.

CALIBRATION-FIRST ARCHITECTURAL CONSTRAINT:
  The inventory table contains a "Defense Register Rows (Cal)" column [MANDATORY].
  NEW artifacts are sorted above PRIOR artifacts in the inventory table.
  ALL NEW-artifact Cal cells must be filled before any Phase 4 proposal row is opened.
  SEQUENCE VIOLATION: opening a proposal row before all NEW-artifact Cal cells are filled
  is a named architectural violation. This constraint makes calibration causally upstream
  of proposals, preventing retroactive row-number assignment.

GATE ARTIFACT CONTRACT:
  Gate-0 artifact: defense register table (Phase 0 EXIT — before any signal artifact).
  Gate-1 artifact: inventory table with filled Cal cells (Phase 1 EXIT).
  Gate-2 artifact: all NEW artifacts read (Phase 2 EXIT).
  Gate-3 artifact: delta detections + conflict audit (Phase 3 EXIT).
  Gate-4 artifact: proposals table + typed null declarations (Phase 4 EXIT).
  Gate-5 artifact: user confirmation (Confirmation Gate).
  strategy.md may not be modified until Gate-5 materializes.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

Positioned before Phase 0. Audit completeness by counting WS-N headers — three rows
declared, three headers must appear below.

| Row | ID   | Surface Type              | Trigger Condition                                   |
|-----|------|---------------------------|-----------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — blocks all signal artifact reads     |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — blocks all proposal column fills    |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — fires at each null declaration write  |

════════════════════════════════════════════════════════════
VOCABULARY CONTRACT
════════════════════════════════════════════════════════════

Two sentinel tokens — two-tier, both required:
| Token | Meaning                               | Violation if misused                      |
|-------|---------------------------------------|-------------------------------------------|
| ??    | Open obligation — unknown or unfilled | Leaving blank where ?? correct: violation |
| --    | Closed decision — deliberately absent | Using ?? where -- correct: violation      |

PROHIBITED VOCABULARY REGISTER — banned by verbatim match in any free-text cell:
| Prohibited Form       | Scope                   | Violation Classification            |
|-----------------------|-------------------------|-------------------------------------|
| "no change needed"    | All free-text cells     | Vocabulary violation                |
| "nothing to add"      | All free-text cells     | Vocabulary violation                |
| "clearly warranted"   | All free-text cells     | Vocabulary violation                |
| "seems sufficient"    | All free-text cells     | Vocabulary violation                |
| "a few artifacts"     | All count fields        | Integer-enforcement gate failure    |
| "several artifacts"   | All count fields        | Integer-enforcement gate failure    |
| "some signals"        | All count fields        | Integer-enforcement gate failure    |
| any non-integer count | Delta summary, any count | Integer-enforcement gate failure   |

Scope: all free-text cells including null declaration reason cells.
Null declarations do not receive a scope exemption — prohibited forms are banned everywhere.

Integer-enforcement gate: writing "a few", "several", "some", or any non-integer value
is a named gate failure. Fuzziness is a named failure condition, not a quality concern.

Violation enumeration:
- Blank cell where ?? required: vocabulary violation
- ?? where -- correct: vocabulary violation
- Any prohibited form in any free-text cell: vocabulary violation
- Non-integer count: integer-enforcement gate failure

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

ENTRY: Topic known. No signal artifacts read. strategy.md not yet opened.

JOB: Open strategy.md. Read full content. Extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]
  Build DEFENSE REGISTER (required-cell schema — blank cells are violations):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  All cells required. ?? permitted. -- for confirmed not-applicable rows only.
  Check defense argument cells against PROHIBITED VOCABULARY REGISTER before writing.

EXIT (Gate-0): Defense register complete. All cells filled. No blanks (use ?? or --).
  Gate-0: No signal artifact may be read until this gate passes.
  Do not advance to Phase 1 without passing Gate-0.
  Stop. Verify every defense register cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT. After Gate-0: confirm defense register complete, all cells filled.
Write WS-1 MILESTONE as declaration that Gate-0 has passed.
Do not read any signal artifact before WS-1 MILESTONE is written. If Gate-0 has not
passed, this milestone must not be written. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

ENTRY: Gate-0 passed. WS-1 MILESTONE written. Defense register complete. No proposals open.

JOB: Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  INVENTORY TABLE — NEW artifacts above PRIOR artifacts (mandatory sort order):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  (blank Cal cells are violations; ?? for unknown; -- for not applicable)

  CALIBRATION-FIRST ENFORCEMENT: Fill Cal cells for ALL NEW-artifact rows now.
  Opening any Phase 4 proposal row before all NEW-artifact Cal cells are filled is a
  SEQUENCE VIOLATION. Cal cells for PRIOR artifacts may be filled here or set to --.

  Write delta summary sentence (mandatory):
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Non-integer form is an integer-enforcement gate failure.

EXIT (Gate-1): Inventory table complete. NEW artifacts above PRIOR artifacts.
  All NEW-artifact Cal cells filled (no blanks; ?? or -- as required).
  Delta summary sentence written with integer values.
  Do not advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells filled and sort order correct. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

ENTRY: Gate-1 passed. All NEW-artifact Cal cells filled. No proposals open.

JOB: Read full content of every NEW artifact. Do not read PRIOR artifacts.

EXIT (Gate-2): All NEW artifacts read.
  Do not advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

ENTRY: Gate-2 passed. All NEW artifacts read. Strategy content known from Phase 0.

JOB:
  DELTA DETECTION:
    For each observation from NEW artifacts:
      Condition 1: in a NEW artifact (date > STRATEGY DATE)?
      Condition 2: absent from strategy.md?
    CONFIRMED DELTA = both YES.
    PRIOR-ONLY = Cond 1 YES, Cond 2 NO. Annotate: "PRIOR-ONLY — not a delta."
    PRIOR-ONLY may not support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION:
    Check NEW artifacts for cross-artifact contradictions.
    If found: CONFLICT REGISTER table.
    If none: "CONFLICT DETECTION — NULL: No contradictions found.
      NO CHANGE wins because: [specific artifact content reference]."

EXIT (Gate-3): Delta detections documented. Conflict audit complete with typed result.
  Do not advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has a typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before any proposal column is filled, confirm all three:
  1. Gate-3 passed — delta and conflict audit typed results present.
  2. All NEW-artifact Cal cells filled (no SEQUENCE VIOLATION occurred).
  3. Inertia Justification column labeled [MANDATORY] in proposals schema.
Write WS-2 MILESTONE as declaration all three pass. Do not fill any proposal column
before WS-2 MILESTONE is written. Halt here if any confirmation fails.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

ENTRY: Gate-3 passed. WS-2 MILESTONE written. Cal column fully populated.
  No proposal row has been opened before this phase (SEQUENCE VIOLATION would have
  halted execution earlier).

JOB:
  PROPOSALS TABLE (required-cell schema — blank cells are violations):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |

  Defense Defeated (Row #): cite specific defense register row number (e.g., Row 3).
  A prose description without a row number does not satisfy this column.
  Inertia Justification [MANDATORY]: check against PROHIBITED VOCABULARY REGISTER before writing.
    "no change needed" is not an acceptable entry — check this cell before presenting;
    any match disqualifies the row.

  For each absent proposal type, apply WS-3 template below:

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Mandatory template for each absent proposal type:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."

Before writing the reason cell, check against PROHIBITED VOCABULARY REGISTER:
  "no change needed" is not an acceptable entry — check this cell before presenting.
  "nothing to add" is not an acceptable entry — check this cell before presenting.
  "clearly warranted" is not an acceptable entry — check this cell before presenting.
Any prohibited form in the reason cell disqualifies the null declaration.
Null declarations are not exempt from the prohibited vocabulary scope.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations. NO CHANGE wins because: [specific reason].

EXIT (Gate-4): Proposals table complete. All non-null rows have all cells filled.
  Every absent type has a typed null declaration.
  All justification and reason cells have been checked against PROHIBITED VOCABULARY REGISTER.
  Do not advance to Confirmation Gate without passing Gate-4.
  Stop. Verify every cell filled, all null types declared, all cells checked. Halt here.

════════════════════════════════════════════════════════════
CONFIRMATION GATE
════════════════════════════════════════════════════════════

Present the proposals table. Write:
"Proposed revisions to strategy.md are listed above. The default is NO CHANGE.
Apply these changes? Reply YES to proceed, NO to cancel, or REVISED with modifications."

Stop. Do not write to strategy.md. Do not modify any file. Halt here and await reply.

════════════════════════════════════════════════════════════
APPLY PHASE (YES or REVISED only)
════════════════════════════════════════════════════════════

Apply approved proposals to strategy.md. Write exactly what was confirmed.
Do not add unrequested changes.
```

---

## Round 9 Predicted Scoring

### New Criteria Coverage by Variation

**C-31 — Named Phase Lifecycle Template (ENTRY/JOB/EXIT)**

| Variation | ENTRY/JOB/EXIT presence | EXIT as structural stop gate home | Mechanism |
|-----------|------------------------|-----------------------------------|-----------|
| V-01 | Bold sub-sections in every phase | "EXIT (Gate-N): ... Do not advance to Phase N+1 ..." | PHASE LIFECYCLE TEMPLATE declared upfront; every phase instantiates it |
| V-02 | Three-row phase-spec tables (ENTRY/JOB/EXIT rows) | EXIT row in each phase-spec table contains stop gate | Schema D declared in TABLE SCHEMAS section |
| V-03 | Bold sub-sections in every phase | EXIT slot with "Do not advance to Phase N+1" | Same lifecycle template as V-01 |
| V-04 | Compact ENTRY/JOB/EXIT sub-sections; phases reference "instantiates PHASE LIFECYCLE TEMPLATE" | EXIT in every phase | PHASE LIFECYCLE TEMPLATE as standalone section referenced by each phase |
| V-05 | Inline ENTRY/JOB/EXIT labels per phase | EXIT (Gate-N) in every phase | Declared in ARCHITECTURE DECLARATION as Audit Path 2 |

All five predicted: **PASS C-31**

**C-32 — Artifact-to-Register Calibration Column**

| Variation | Column name | Column declared as | Enforcement |
|-----------|-------------|-------------------|-------------|
| V-01 | "Defense Register Rows (Cal) [MANDATORY]" | Part of inventory table schema in Phase 1 JOB | "MANDATORY — blank cell is violation" |
| V-02 | "Defense Register Rows (Cal) [MANDATORY]" | Schema B in TABLE SCHEMAS section (upfront) | All table schemas declared once; mandatory marker |
| V-03 | "Defenses Implicated (Cal) [MANDATORY]" | Part of Signal Inventory TABLE schema | "MANDATORY — blank is violation" |
| V-04 | "Defense Register Rows (Cal) [MANDATORY]" | In Phase 1 inventory table schema | Calibration Protocol is its own inter-phase section |
| V-05 | "Defense Register Rows (Cal) [MANDATORY]" | In Phase 1 inventory table | Declared in ARCHITECTURE DECLARATION as calibration-first constraint |

All five predicted: **PASS C-32**

**C-33 — Inverted Artifact Sequence with Upfront Calibration**

| Variation | Sort order stated | Calibration before proposals | Enforcement mechanism |
|-----------|------------------|-----------------------------|-----------------------|
| V-01 | "SORT ORDER: NEW above PRIOR — mandatory" | "Do not open proposal row until ALL NEW Cal cells filled" | Exit gate in Phase 1 verifies before Phase 2 |
| V-02 | "Sort order: NEW artifacts above PRIOR artifacts (mandatory)" | "NEW-artifact Cal cells must be filled before any Phase 4 proposal row opens" | Phase-spec table EXIT row enforces |
| V-03 | "Sort: NEW artifacts above PRIOR" + "challengers examined before defense re-articulated" | "Writing a proposal row before ALL NEW-artifact Cal cells filled is a sequence violation" | THREAT ASSESSMENT PROTOCOL |
| V-04 | "SORT ORDER: NEW above PRIOR — Mandatory" | Calibration Protocol as inter-phase section between Phase 1 and Phase 2 | Calibration Completion Gate before Phase 2 |
| V-05 | "NEW artifacts above PRIOR artifacts (mandatory sort order)" | "SEQUENCE VIOLATION: opening proposal row before all NEW-artifact Cal cells filled is a named architectural violation" | Named violation condition in ARCHITECTURE DECLARATION |

All five predicted: **PASS C-33**

**C-34 — Compound Audit Structure (Spine + Lifecycle)**

| Variation | Write-surface spine | Per-phase lifecycle slots | Two paths declared | Both independently auditable |
|-----------|--------------------|--------------------------|--------------------|------------------------------|
| V-01 | WRITE SURFACE REGISTER + WS-1/WS-2/WS-3 headers | ENTRY/JOB/EXIT sub-sections | "COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS" section | PATH 1 = scan WS headers; PATH 2 = scan EXIT sections |
| V-02 | WRITE SURFACE REGISTER + WS-1/WS-2/WS-3 headers | Phase-spec tables (Schema D) | "COMPOUND AUDIT STRUCTURE" section | PATH 1 = count WS headers; PATH 2 = scan EXIT rows in phase-spec tables |
| V-03 | WRITE SURFACE REGISTER + WS-1/WS-2/WS-3 headers | ENTRY/JOB/EXIT sub-sections | "COMPOUND AUDIT STRUCTURE — TWO PATHS" section | PATH 1 = scan WS headers; PATH 2 = scan EXIT slots |
| V-04 | WRITE SURFACE REGISTER + WS-1/WS-2/WS-3 headers | ENTRY/JOB/EXIT sub-sections; PHASE LIFECYCLE TEMPLATE as standalone section | "COMPOUND AUDIT STRUCTURE" in EXECUTION ARCHITECTURE | Both paths in EXECUTION ARCHITECTURE declaration |
| V-05 | WRITE SURFACE REGISTER + WS-1/WS-2/WS-3 headers | ENTRY/JOB/EXIT slots | "COMPOUND AUDIT STRUCTURE — two independent audit paths" in ARCHITECTURE DECLARATION | "Neither path is redundant with the other" explicitly stated |

All five predicted: **PASS C-34**

### Predicted Composite Scores

All five variations are designed to pass all 5 essential criteria, all 3 recommended criteria,
and all 26 aspirational criteria.

| Variation | Essential (5/5) | Recommended (3/3) | Aspirational (26/26) | Predicted Score |
|-----------|-----------------|-------------------|----------------------|-----------------|
| V-01      | 60              | 30                | 10                   | 100             |
| V-02      | 60              | 30                | 10                   | 100             |
| V-03      | 60              | 30                | 10                   | 100             |
| V-04      | 60              | 30                | 10                   | 100             |
| V-05      | 60              | 30                | 10                   | 100             |

### Discriminating Axes for Round 10

If all five reach ceiling, the following structural distinctions will generate new criteria:

1. **Calibration violation naming precision (C-33 refinement)**: V-05 names the violation
   condition ("SEQUENCE VIOLATION") as a first-class label in the architecture declaration.
   V-04's "Calibration Completion Gate" names the gate but not the violation. V-01/V-02/V-03
   state the constraint as an instruction without naming the violation. A criterion requiring
   a named, labeled violation condition would distinguish V-05 from V-01/V-02/V-03.

2. **Audit path independence declaration (C-34 refinement)**: V-05 explicitly states "Neither
   path is redundant with the other." V-01 states both paths with descriptions. V-02/V-03/V-04
   declare both paths without the independence assertion. A criterion requiring an explicit
   independence statement ("neither path is redundant") would distinguish V-05.

3. **Calibration column placement (C-32 refinement)**: V-02 declares Schema B (inventory
   table with calibration column) in a TABLE SCHEMAS section before Phase 0 — the column
   is contractually committed before inventory begins. V-01/V-03/V-05 declare the column
   within the inventory phase. V-04's inter-phase Calibration Protocol separates the column
   declaration from the filling. A criterion requiring the calibration column schema to be
   declared before Phase 0 (upfront commitment) would distinguish V-02.

4. **Lifecycle template independence (C-31 refinement)**: V-04 declares the PHASE LIFECYCLE
   TEMPLATE as a standalone section and has each phase say "instantiates PHASE LIFECYCLE
   TEMPLATE" — making the template a named contractual reference. V-01/V-02/V-03 embed
   ENTRY/JOB/EXIT as content within phases without a standalone template declaration. A
   criterion requiring phases to cite the template they instantiate would distinguish V-04.

```json
{
  "round": 9,
  "rubric_version": "v9",
  "max_score": 100,
  "new_criteria": ["C-31", "C-32", "C-33", "C-34"],
  "predicted_top_score": 100,
  "predicted_all_essential_pass": true,
  "predicted_all_recommended_pass": true,
  "predicted_all_aspirational_pass": true,
  "predicted_discriminators_round_10": [
    "Calibration violation naming: named violation condition ('SEQUENCE VIOLATION') vs constraint as instruction",
    "Audit path independence declaration: explicit 'neither path is redundant' statement vs implicit",
    "Calibration column placement: declared in TABLE SCHEMAS before Phase 0 vs declared within inventory phase",
    "Lifecycle template independence: phases cite 'instantiates PHASE LIFECYCLE TEMPLATE' vs inline ENTRY/JOB/EXIT"
  ]
}
```
