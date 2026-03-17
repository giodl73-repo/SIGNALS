# topic-plan Skill Variations — Round 11 (2026-03-15)

Rubric: v11 (C-01–C-39, max 100)
New criteria this round: C-36 through C-39

- C-36: TABLE SCHEMAS section elevated to a full named phase (Phase -1) with explicit ENTRY/JOB/EXIT lifecycle slots
- C-37: Each schema block includes inline BREACH CONDITIONS enumerating violation conditions
- C-38: Sequential gate chain includes Gate-S for the schema phase, positioned before Gate-0
- C-39: Modal obligation language (SHALL/SHALL NOT, MUST/MUST NOT) at 4+ critical constraint sites

---

## Round 11 Design Notes

R10 introduced C-35 (upfront TABLE SCHEMAS section as a pre-phase declared contract with named
schema identifiers). R11 extends this with four new criteria that deepen the structural weight
of the schema phase and formalize its obligation language.

**C-36** requires TABLE SCHEMAS to be elevated from a section to a full named phase — Phase -1 —
with ENTRY, JOB, and EXIT lifecycle slots in Schema D format. In R10, V-02 already had this
structure. All R11 variations must include it.

**C-37** requires each schema block to carry inline BREACH CONDITIONS — an enumeration of the
specific violation conditions that make compliance fail for that schema. R10's V-04 had per-schema
breach conditions. R11 generalizes this requirement across all variations.

**C-38** requires Gate-S (the schema gate) to appear in the sequential gate chain before Gate-0.
The chain SHALL read: Gate-S -> Gate-0 -> Gate-1 -> Gate-2 -> Gate-3 -> Gate-4. Gate-S is the
named enforcement point that Phase 0 cannot begin until schema declarations are complete.

**C-39** requires modal obligation language (SHALL/SHALL NOT, MUST/MUST NOT) at 4 or more
distinct critical constraint sites. Informal language ("do not", "stop", "halt") may co-exist but
cannot substitute for the modal requirement count.

**Previous round gap analysis:**

| Gap | Description | R11 fix |
|-----|-------------|---------|
| C-36 missing | TABLE SCHEMAS is a section, not a phase; no ENTRY/JOB/EXIT slots | All five R11 designs elevate TABLE SCHEMAS to Phase -1 with full Schema D lifecycle slots |
| C-37 missing | Schema blocks state mandatory columns and sentinel rules but do not enumerate inline BREACH CONDITIONS per schema | All five R11 designs add BREACH CONDITIONS block at the end of each schema declaration |
| C-38 partial | Gate-S mentioned in lifecycle text but not explicitly named in the sequential gate chain before Gate-0 | All five R11 designs include Gate-S explicitly in the chain: Gate-S -> Gate-0 -> ... -> Gate-4 |
| C-39 absent or low count | Modal SHALL language present in some phases but fewer than 4 distinct critical sites | All five R11 designs audit for 4+ distinct SHALL/SHALL NOT constraint sites |

**Round 11 single-axis and combined choices:**

| Variation | Axis | Primary mechanism |
|-----------|------|-------------------|
| V-01 | Lifecycle emphasis | Phase -1 has maximal ENTRY/JOB/EXIT explicitness; every phase has hard boundary language at ENTRY and EXIT; breach conditions use lifecycle-phase framing |
| V-02 | Phrasing register (formal modal) | SHALL/SHALL NOT/MUST/MUST NOT saturates all obligation positions throughout all phases and gate statements; breach conditions use SHALL language |
| V-03 | Inertia framing | Defense register is the central organizing structure; schemas carry inertia equal to strategy; breach conditions framed as inertia violations; all proposals must defeat a named defense row |
| V-04 | Lifecycle + Inertia combined | Detailed lifecycle slots with explicit phase boundary text + defense register as primary spine; breach conditions cross-reference both lifecycle and inertia violations |
| V-05 | Modal + Table Schemas combined | Formal modal language throughout + comprehensive Phase -1 schema declarations with BREACH CONDITIONS as first-class structural elements; schema breaches treated as SHALL NOT violations |

---

## V-01: Lifecycle Emphasis — Maximally Explicit Phase Boundaries with Hard ENTRY/JOB/EXIT

**Variation axis**: Lifecycle emphasis — every phase has maximally explicit ENTRY/JOB/EXIT slots.
Phase -1 (TABLE SCHEMAS) is a first-class lifecycle phase: its ENTRY declares pre-conditions
(nothing opened, nothing read, no structures built), its JOB declares all schema work, and its
EXIT is Gate-S. Each schema block carries BREACH CONDITIONS framed in terms of lifecycle boundary
violations: "This schema is considered breached when a phase begins without the schema having
been declared in Phase -1." The sequential gate chain (Gate-S -> Gate-0 -> Gate-1 -> Gate-2 ->
Gate-3 -> Gate-4) is the structural spine the reviewer scans to verify phase integrity.

**Hypothesis**: When every phase has hard ENTRY/JOB/EXIT boundaries and Phase -1 is a genuine
lifecycle phase (not a section), schema completeness is an ENTRY precondition for Phase 0 — not
a recommendation. The ENTRY slot forces a binary check: Gate-S passed or not. A reviewer auditing
phases does not have to read JOB content to know if a phase started legally — they check the
ENTRY slot for its precondition and the corresponding EXIT of the prior phase for its gate.
This separates structural compliance from content quality.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. Every proposal must defeat the null.

Sequential gate chain (audit this chain for completeness):
  Gate-S -> Gate-0 -> Gate-1 -> Gate-2 -> Gate-3 -> Gate-4

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan section headers for WS-1, WS-2, WS-3.
  Write-surface register below declares 3 rows; 3 section headers must appear.
  Completeness verifiable by header count.

AUDIT PATH 2 (Lifecycle Slots): Scan each phase (Phase -1 through Phase 4) for ENTRY / JOB / EXIT.
  EXIT is the structural home for each in-phase stop gate.
  Gate-S lives in Phase -1 EXIT. Gate-0 lives in Phase 0 EXIT. And so on.
  A missing EXIT slot or a missing gate inside EXIT is a visible lifecycle breach.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface Type              | Trigger                                             |
|-----|------|---------------------------|-----------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact opened    |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before any proposal column filled   |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each typed null declaration write  |

════════════════════════════════════════════════════════════
Phase -1 — TABLE SCHEMAS (Schema Declarations)
════════════════════════════════════════════════════════════

ENTRY:
  Nothing has been opened. No strategy file read. No signal artifacts located.
  No structures exist. This phase is the first act of execution.
  Precondition: execution has just begun and no prior phase output exists.
  If any file has been opened before Phase -1 begins, that is a lifecycle boundary violation.

JOB:
  Declare all table schemas that will be used in this skill execution.
  Every table produced in this output must conform to a schema declared here.
  Producing a table with columns not declared here is a schema violation.
  Declaring a schema here that is never used is permitted; it does not constitute a violation.

  SCHEMA A — DEFENSE REGISTER
  | Row | Dimension | Current Strategy Position | Defense Argument |
  Required columns: Row (integer), Dimension, Current Strategy Position, Defense Argument.
  All four columns are mandatory. Blank cell is a violation regardless of context.
  Sentinel rules: ?? for unknown or unfilled. -- for confirmed not-applicable only.
  Phase used: Phase 0.

  BREACH CONDITIONS — Schema A is considered breached when:
  (a) any of the four columns is absent, renamed, or reordered in the produced table;
  (b) any cell is blank where ?? is the required sentinel;
  (c) any Defense Argument cell contains an inadmissible rebuttal form;
  (d) Phase 0 begins execution of Schema A before Phase -1 EXIT (Gate-S) has passed.

  SCHEMA B — SIGNAL INVENTORY
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  Required columns: all four. Cal column is mandatory — blank Cal cell is a violation.
  Sort order: NEW artifacts above PRIOR artifacts. This is a mandatory ordering constraint.
  Sentinel rules for Cal: ?? if defensive implication unknown. -- if no rows implicated.
  Architectural constraint: ALL NEW-artifact Cal cells must be filled before any Schema C
  proposal row is opened. Cal completion is causally upstream of proposals.
  Phase used: Phase 1.

  BREACH CONDITIONS — Schema B is considered breached when:
  (a) Cal column is absent, renamed, or merged with another column;
  (b) any NEW-artifact Cal cell is blank (sentinel ?? is required if implication unknown);
  (c) PRIOR artifacts appear above any NEW artifact in the produced table;
  (d) any Schema C row is opened before ALL NEW-artifact Cal cells are filled —
      this is a cross-schema lifecycle breach: Phase 4 began before Phase 1's constraint
      was fully satisfied.

  SCHEMA C — PROPOSALS TABLE
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Required columns: all seven. Blank cell is a violation.
  Type values: ADD, REMOVE, REPRIORITIZE only. Any other type value is a violation.
  Defense Defeated (Row #): must cite a Schema A row number. Prose description alone fails.
  Inertia Justification [MANDATORY]: must be checked against BANNED FORMS before writing.
  Phase used: Phase 4.

  BREACH CONDITIONS — Schema C is considered breached when:
  (a) any of the seven columns is absent or renamed;
  (b) Defense Defeated contains prose without a Schema A row number;
  (c) Inertia Justification contains a banned form;
  (d) any absent change type (ADD, REMOVE, REPRIORITIZE) has no typed null declaration;
  (e) a proposal row is opened before WS-2 MILESTONE was written in Phase 4 ENTRY.

  SCHEMA D — PHASE-SPEC TABLE (instantiated in every phase including this one)
  | Slot  | Content                                                     |
  |-------|-------------------------------------------------------------|
  | ENTRY | [Preconditions that must be true before this phase begins]  |
  | JOB   | [Work instructions for this phase]                          |
  | EXIT  | [Gate — named stop condition before advancing]              |
  All three slots are required in every phase.
  EXIT is the structural home for stop gates. Stop gate language in ENTRY or JOB does not
  satisfy Schema D: EXIT is the declared structural position for gate content.
  Phase used: every phase.

  BREACH CONDITIONS — Schema D is considered breached when:
  (a) any phase omits ENTRY, JOB, or EXIT slots;
  (b) stop gate language appears only in JOB or ENTRY with no EXIT slot;
  (c) EXIT exists but does not contain a named gate or halt instruction.

  VOCABULARY CONTRACT:
  Sentinel tokens (in force in all cells and free-text fields):
    ??  — open obligation (unknown or unfilled)
    --  — closed decision (confirmed not-applicable)
  BANNED FORMS — verbatim match disqualifies any justification or null-declaration cell:
    "no change needed"    "nothing to add"      "clearly warranted"
    "seems sufficient"    "a few artifacts"     "several artifacts"
    "some signals"        "not necessary"       any non-integer count
  Check every free-text cell against this list before writing.
  Null declaration reason cells are NOT exempt.
  Integer-enforcement: "a few", "several", "some", or any non-integer in any count field
  is a gate failure, not a quality concern.

EXIT (Gate-S):
  All four schemas declared with full column definitions.
  All four schemas carry inline BREACH CONDITIONS.
  Vocabulary contract declared. Banned forms listed.
  Sequential gate chain confirmed: Gate-S -> Gate-0 -> Gate-1 -> Gate-2 -> Gate-3 -> Gate-4.
  Gate-S: Phase 0 ENTRY precondition requires Gate-S passed.
  Do not advance to Phase 0 without passing Gate-S.
  Stop. Verify all four schema declarations are complete, each with BREACH CONDITIONS. Halt here.

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

ENTRY:
  Gate-S passed. All schemas declared. All schemas carry BREACH CONDITIONS.
  Topic known. strategy.md not yet opened. No signal artifacts located.
  Precondition: Phase -1 EXIT (Gate-S) has passed.
  If Gate-S has not passed, Phase 0 must not begin.

JOB:
  Open strategy.md. Read full content and extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER (conform to Schema A declaration in Phase -1):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension.
  Check Defense Argument cells against BANNED FORMS before writing.
  All four columns required. ?? or -- per Schema A rules. No blank cells.

EXIT (Gate-0):
  Schema A complete. All cells filled (no blanks; ?? or -- per Schema A rules).
  Defense Argument cells checked against BANNED FORMS.
  Gate-0: No signal artifact may be opened until Gate-0 passes.
  Do not advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT, after Gate-0 passes, before any signal artifact is opened.
  ENTRY precondition check: Gate-0 has passed. Schema A is complete.
  Write WS-1 MILESTONE as declaration that Gate-0 has passed.
  Do not open any signal artifact before writing WS-1 MILESTONE.
  Lifecycle boundary: any artifact opened before WS-1 MILESTONE is a Phase 0 EXIT breach. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. WS-1 MILESTONE written. Schema A complete.
  Precondition: Phase 0 EXIT (Gate-0) has passed and WS-1 MILESTONE exists.
  If WS-1 MILESTONE has not been written, Phase 1 must not begin.

JOB:
  Locate all signal artifact files across all 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (NEW artifacts above PRIOR — mandatory per Schema B):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  All NEW-artifact Cal cells must be filled before any Schema C proposal row opens.
  This is the Schema B architectural constraint declared in Phase -1.

  Write mandatory delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. Non-integer form is an integer-enforcement gate failure.

EXIT (Gate-1):
  Schema B complete. NEW artifacts appear above PRIOR artifacts.
  All NEW-artifact Cal cells filled (no blanks; ?? or -- per Schema B rules).
  Delta sentence written with integer values for N and M.
  Gate-1: Phase 2 ENTRY precondition requires Gate-1 passed.
  Do not advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells are filled. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

ENTRY:
  Gate-1 passed. All NEW-artifact Cal cells filled. No proposals open.
  Precondition: Phase 1 EXIT (Gate-1) has passed.
  If Gate-1 has not passed, Phase 2 must not begin.

JOB:
  Read full content of every artifact classified NEW in Schema B inventory.
  Do not read PRIOR artifacts. Reading PRIOR artifacts in this phase is a lifecycle boundary violation.

EXIT (Gate-2):
  All NEW artifacts read in full.
  Gate-2: Phase 3 ENTRY precondition requires Gate-2 passed.
  Do not advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

ENTRY:
  Gate-2 passed. All NEW artifacts read. Schema A (Defense Register) known from Phase 0.
  Precondition: Phase 2 EXIT (Gate-2) has passed.
  If Gate-2 has not passed, Phase 3 must not begin.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in at least one NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md content?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations may not support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Audit NEW artifacts for cross-artifact contradictions.
  If found: document in a CONFLICT REGISTER table.
  If none: write typed null form:
    "CONFLICT DETECTION — NULL: No cross-artifact contradictions found.
    NO CHANGE wins because: [specific artifact reference]."

EXIT (Gate-3):
  Delta detections documented.
  Conflict audit has a typed result (CONFLICT REGISTER table or typed NULL).
  Gate-3: Phase 4 ENTRY precondition requires Gate-3 passed.
  Do not advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before filling any Schema C proposal column:
  ENTRY precondition check: (1) Gate-3 passed. (2) All NEW Cal cells in Schema B filled.
  (3) Schema C Inertia Justification column is labeled [MANDATORY] per Phase -1 declaration.
  Write WS-2 MILESTONE as declaration that all three confirmations pass.
  Do not fill any proposal column before writing WS-2 MILESTONE.
  Lifecycle boundary: any proposal column filled before WS-2 MILESTONE is a Phase 4 ENTRY breach. Halt here.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 passed. WS-2 MILESTONE written. All NEW Cal cells filled. No proposal rows open.
  Precondition: Phase 3 EXIT (Gate-3) has passed and WS-2 MILESTONE exists.
  If WS-2 MILESTONE has not been written, Phase 4 must not begin.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C declaration in Phase -1):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Check Inertia Justification cells against BANNED FORMS before writing each cell.
  Defense Defeated must cite a Schema A row number. Prose description alone fails Schema C.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB.
Mandatory template: "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Before writing reason cell: check against BANNED FORMS.
  "no change needed" — banned. "nothing to add" — banned.
  Any match disqualifies. Reason must cite specific artifact or strategy content.

Required for each absent proposal type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C complete per Phase -1 declaration. All cells filled.
  All absent types have typed null declarations with WS-3 template.
  Inertia and null reason cells checked against BANNED FORMS.
  Do not modify strategy.md. Do not advance to Apply Phase without user confirmation.
  Gate-4: Apply Phase ENTRY precondition requires Gate-4 passed and user confirmation received.
  Stop. Verify every cell filled and every null uses typed template. Halt here.

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

## V-02: Phrasing Register (Formal Modal) — SHALL/SHALL NOT Throughout

**Variation axis**: Phrasing register — SHALL/SHALL NOT/MUST/MUST NOT saturates all obligation
positions throughout the skill. Every phase JOB uses SHALL for positive obligations and
SHALL NOT for prohibitions. Every gate EXIT uses "Phase N SHALL NOT advance to Phase N+1
without passing this gate." Every schema breach condition uses SHALL. The VOCABULARY CONTRACT
enumerates sentinel usage as SHALL obligations. The result is a skill where every evaluable
constraint is formally stated in modal language, making compliance binary-checkable.

**Hypothesis**: When modal language (SHALL/SHALL NOT) appears at 4+ distinct critical sites,
each obligation becomes binary-evaluable without interpretive judgment. A reviewer checking
"was the SHALL satisfied?" needs only to verify presence or absence of the declared output.
Informal language ("stop", "halt", "do not") is aspirational — it describes desired behavior
but does not create a structurally named obligation. SHALL creates a named obligation. The
accumulation of SHALL obligations across the skill creates an obligation registry that can be
audited independently of content quality.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. All proposals SHALL defeat the null.

Sequential gate chain: Gate-S -> Gate-0 -> Gate-1 -> Gate-2 -> Gate-3 -> Gate-4.
Each gate is a SHALL NOT advance condition. All six gates SHALL appear in output.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Count WS-1, WS-2, WS-3 section headers.
  Write-surface register declares 3 rows. 3 section headers SHALL appear.
AUDIT PATH 2 (Lifecycle Slots): Scan each phase for ENTRY / JOB / EXIT sub-sections.
  EXIT SHALL house the in-phase stop gate.
  Gate-S SHALL appear in Phase -1 EXIT. Gate-0 SHALL appear in Phase 0 EXIT.
  A phase without EXIT is a structural violation.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface Type              | Trigger                                            |
|-----|------|---------------------------|----------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact opened   |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before any proposal column filled  |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each null declaration write       |

════════════════════════════════════════════════════════════
Phase -1 — TABLE SCHEMAS (Schema Declarations)
════════════════════════════════════════════════════════════

ENTRY:
  No file SHALL have been opened. No artifact SHALL have been read. No structure SHALL exist.
  This phase SHALL be the first act of execution without exception.

JOB:
  All table schemas used in this skill execution SHALL be declared in this phase.
  Every table produced in this output SHALL conform to a schema declared here.
  Producing a table with columns not declared in this phase is PROHIBITED.

  SCHEMA A — DEFENSE REGISTER
  | Row | Dimension | Current Strategy Position | Defense Argument |
  All four columns SHALL be present. Sentinel: ?? (unknown), -- (not applicable).
  Defense Argument cells SHALL be checked against BANNED FORMS before writing.
  Blank cell is PROHIBITED regardless of context.
  Phase used: Phase 0.

  BREACH CONDITIONS — Schema A SHALL be considered breached when:
  (a) any column is absent, renamed, or reordered in the produced table;
  (b) any cell is blank where ?? is the required sentinel;
  (c) any Defense Argument cell contains a banned form;
  (d) the produced Schema A table deviates from the column declaration above.

  SCHEMA B — SIGNAL INVENTORY
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  All four columns SHALL be present. Cal column SHALL NOT be omitted or renamed.
  Sort order: NEW artifacts SHALL appear above PRIOR artifacts. Inversion is PROHIBITED.
  Sentinel for Cal: ?? (implication unknown), -- (no rows implicated). Blank is PROHIBITED.
  Architectural constraint: ALL NEW-artifact Cal cells SHALL be filled before any Schema C
  row is opened. Opening a Schema C row before Cal completion is PROHIBITED.
  Phase used: Phase 1.

  BREACH CONDITIONS — Schema B SHALL be considered breached when:
  (a) Cal column is absent or renamed;
  (b) any NEW-artifact Cal cell is blank;
  (c) PRIOR artifacts appear above any NEW artifact;
  (d) any Schema C row is opened before ALL NEW-artifact Cal cells are filled —
      this is PROHIBITED as a cross-schema ordering violation.

  SCHEMA C — PROPOSALS TABLE
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  All seven columns SHALL be present. Type values SHALL be ADD, REMOVE, or REPRIORITIZE only.
  Defense Defeated (Row #) SHALL cite a Schema A row number. Prose alone is PROHIBITED.
  Inertia Justification SHALL be checked against BANNED FORMS before writing.
  Phase used: Phase 4.

  BREACH CONDITIONS — Schema C SHALL be considered breached when:
  (a) any mandatory column is absent;
  (b) Defense Defeated contains prose without a Schema A row number;
  (c) Inertia Justification contains a banned form;
  (d) any absent change type has no typed null declaration.

  SCHEMA D — PHASE-SPEC TABLE (applied in every phase including this one)
  | Slot  | Content                                            |
  |-------|----------------------------------------------------|
  | ENTRY | [Preconditions that must be true before phase begins] |
  | JOB   | [Work instructions for this phase]                 |
  | EXIT  | [Gate — SHALL NOT advance without passing]         |
  All three slots SHALL be present in every phase.
  EXIT SHALL be the structural home for stop gate language.
  Stop gate language in ENTRY or JOB SHALL NOT satisfy the EXIT requirement.
  Phase used: every phase.

  BREACH CONDITIONS — Schema D SHALL be considered breached when:
  (a) any phase omits ENTRY, JOB, or EXIT;
  (b) stop gate language appears only in JOB or ENTRY, with EXIT absent or empty;
  (c) EXIT does not contain a named gate and an explicit halt instruction.

  VOCABULARY CONTRACT:
  Sentinel tokens SHALL be used as follows:
    ?? — SHALL be used for unknown or unfilled values. SHALL NOT be left blank.
    -- — SHALL be used only for confirmed not-applicable entries.
  BANNED FORMS — verbatim match in any free-text cell is PROHIBITED:
    "no change needed"    "nothing to add"      "clearly warranted"
    "seems sufficient"    "a few artifacts"     "several artifacts"
    "some signals"        "not necessary"       any non-integer count
  Every free-text cell SHALL be checked against this list before it is written.
  Null declaration reason cells SHALL NOT receive a scope exemption.
  Integer-enforcement: "a few", "several", "some", or any non-integer in any count field
  is PROHIBITED and SHALL be treated as a gate failure.

EXIT (Gate-S):
  All four schemas SHALL be declared with full column definitions and sentinel rules.
  All four schemas SHALL carry inline BREACH CONDITIONS.
  Vocabulary contract SHALL be declared.
  Phase 0 SHALL NOT begin until Gate-S passes.
  Stop. Verify all four schema declarations are complete with BREACH CONDITIONS. Halt here.

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

ENTRY:
  Gate-S SHALL have passed. All schemas declared with BREACH CONDITIONS.
  Topic known. strategy.md not yet opened. No signal artifacts read.

JOB:
  Open strategy.md. Read full content. Extract last-modified date.
  STRATEGY DATE SHALL be recorded as: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER (conform to Schema A declared in Phase -1):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension. Defense Argument cells SHALL be checked
  against BANNED FORMS before writing. No blank cells SHALL appear.

EXIT (Gate-0):
  Schema A SHALL be complete. All cells SHALL be filled (no blanks; ?? or -- per Schema A).
  Defense Argument cells SHALL have been checked against BANNED FORMS.
  Phase 0 SHALL NOT advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

SHALL fire at Phase 0 EXIT, after Gate-0 passes, before any signal artifact is opened.
  Gate-0 SHALL have passed (Schema A complete, all cells filled).
  WS-1 MILESTONE SHALL be written as declaration that Gate-0 passed.
  Opening any signal artifact before WS-1 MILESTONE is written is PROHIBITED. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 SHALL have passed. WS-1 MILESTONE SHALL have been written. Schema A complete.

JOB:
  Locate all signal artifact files across all 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (conform to Schema B declared in Phase -1):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  NEW artifacts SHALL appear above PRIOR artifacts.
  All NEW-artifact Cal cells SHALL be filled before any Schema C row is opened.

  Delta summary sentence SHALL state exactly:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M SHALL be integers. Non-integer form is PROHIBITED.

EXIT (Gate-1):
  Schema B SHALL be complete. NEW SHALL appear above PRIOR.
  All NEW-artifact Cal cells SHALL be filled.
  Delta sentence SHALL contain integer values.
  Phase 1 SHALL NOT advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

ENTRY:
  Gate-1 SHALL have passed. All NEW-artifact Cal cells filled. No proposals open.

JOB:
  Read full content of every artifact classified NEW in Schema B.
  PRIOR artifacts SHALL NOT be read in this phase.

EXIT (Gate-2):
  All NEW artifacts SHALL have been read.
  Phase 2 SHALL NOT advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

ENTRY:
  Gate-2 SHALL have passed. All NEW artifacts read. Schema A defense arguments known.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in at least one NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations SHALL NOT support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Audit NEW artifacts for contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found. NO CHANGE wins because:
  [specific artifact reference]."

EXIT (Gate-3):
  Delta detections SHALL be documented.
  Conflict audit SHALL have a typed result (table or typed NULL).
  Phase 3 SHALL NOT advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

SHALL fire at Phase 4 ENTRY. SHALL fire before any Schema C column is filled.
  Gate-3 SHALL have passed. All NEW Cal cells in Schema B SHALL be filled.
  Schema C Inertia Justification SHALL be labeled [MANDATORY] per Phase -1 declaration.
  WS-2 MILESTONE SHALL be written.
  Opening a proposal row before WS-2 MILESTONE is written is PROHIBITED. Halt here.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 SHALL have passed. WS-2 MILESTONE SHALL have been written.
  All NEW Cal cells filled. No proposal rows open.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C declared in Phase -1):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Inertia Justification cells SHALL be checked against BANNED FORMS before writing.
  Defense Defeated SHALL cite a Schema A row number. Prose alone is PROHIBITED.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

SHALL fire at each null declaration write in Phase 4 JOB.
Null declarations SHALL use mandatory template:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Reason cells SHALL be checked against BANNED FORMS before writing.
  "no change needed" is PROHIBITED. "nothing to add" is PROHIBITED.
  Any banned form SHALL disqualify the null declaration.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C SHALL be complete. All cells SHALL be filled.
  All absent types SHALL have typed null declarations using WS-3 template.
  All Inertia and null reason cells SHALL have been checked against BANNED FORMS.
  strategy.md SHALL NOT be modified before user confirmation is received.
  Phase 4 SHALL NOT advance to Apply Phase without passing Gate-4.
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

---

## V-03: Inertia Framing — Defense Register as Central Organizing Structure

**Variation axis**: Inertia framing — the defense register is the central organizing structure.
All proposals are indictments: a proposal claims that a specific defense argument is wrong.
The TABLE SCHEMAS section introduces both kinds of inertia operating simultaneously —
STRATEGY INERTIA (the strategy is correct until evidence defeats a named defense) and
SCHEMA INERTIA (the declared schemas are immutable output contracts; column drift is a
contract breach equal to using a banned form). Phase -1 is the phase that arms both kinds
of inertia before any evidence is examined. Gate-S is the point at which both inertia
contracts become operative.

**Hypothesis**: When table schemas share the inertia framing with strategy content, column
additions, removals, or renames cannot be treated as innocent formatting choices. A schema
change is structurally equivalent to an unauthorized strategy change — it requires defeating
a declared contract. The defense register's row numbers serve as the cross-schema link:
Schema B's Cal column maps artifacts to defense rows; Schema C's Defense Defeated column
cites those rows. A proposal without a row number cannot be an indictment — it is a
preference. The inertia framing institutionalizes this traceability chain as the primary
structural spine, making every proposal either a named indictment or inadmissible.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

THE PREMISE: This skill manages two kinds of inertia simultaneously.

STRATEGY INERTIA: The current strategy is correct until signal evidence defeats a specific
defense row. A proposal is an indictment of a defense row. If no defense row is defeated,
the outcome is NO CHANGE to strategy.md.

SCHEMA INERTIA: The declared table schemas are immutable output contracts. Every table
produced must conform exactly to a schema declared in Phase -1 below. Column additions,
removals, or renames are contract breaches equal to using a banned form in an inertia cell.
Schema drift is an unauthorized change to a declared contract, not a formatting choice.

Both kinds of inertia are armed in Phase -1. Gate-S is the point at which both contracts
become operative. No evidence may be examined before both contracts are in force.

Sequential gate chain: Gate-S -> Gate-0 -> Gate-1 -> Gate-2 -> Gate-3 -> Gate-4.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan for WS-1, WS-2, WS-3 section headers.
AUDIT PATH 2 (Lifecycle Slots): Scan each phase for ENTRY / JOB / EXIT sub-sections.
  EXIT is the structural home for each stop gate.
  Inertia contract violations surface here: a phase without EXIT has no named gate = unguarded inertia breach.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface                   | Trigger                                            |
|-----|------|---------------------------|----------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact opened   |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before any proposal column filled  |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each null declaration write       |

════════════════════════════════════════════════════════════
Phase -1 — TABLE SCHEMAS (Arming Both Inertia Contracts)
════════════════════════════════════════════════════════════

ENTRY:
  Nothing opened. Nothing read. No structures built.
  Both inertia contracts are about to be declared.
  STRATEGY INERTIA will be armed when Schema A (Defense Register) is declared.
  SCHEMA INERTIA is armed the moment Phase -1 declares a schema.
  This phase has no predecessors. It begins with a clean execution state.

JOB:
  Declare all table schemas. Both inertia contracts become operative upon declaration.

  SCHEMA A — DEFENSE REGISTER (strategy inertia contract)
  | Row | Dimension | Current Strategy Position | Defense Argument |
  Columns: Row (integer), Dimension, Current Strategy Position, Defense Argument.
  All four mandatory. Sentinel: ?? (unknown), -- (confirmed not-applicable only).
  Defense Argument cells: check against BANNED FORMS before writing.
  The defense register is the indictment ledger. A proposal that cannot name the row it
  defeats is inadmissible — it is a preference, not an indictment.

  BREACH CONDITIONS — Schema A is considered breached when:
  (a) any column absent, renamed, or reordered — schema inertia violation;
  (b) any cell blank where ?? required — inadmissible rebuttal gap;
  (c) any Defense Argument contains a banned form — inadmissible defense;
  (d) a Phase 4 proposal row cites a defense dimension in prose without naming a row number —
      inadmissible indictment.

  SCHEMA B — SIGNAL INVENTORY (chain-of-custody contract)
  | Artifact Filename | Date | NEW / PRIOR | Defenses Implicated (Cal) [MANDATORY] |
  Columns: all four mandatory. Cal column mandatory — blank is a chain-of-custody violation.
  Sort: NEW artifacts above PRIOR. Mandatory ordering constraint.
  Sentinel for Cal: ?? (threat not assessed), -- (no defense threatened). Blank: violation.
  Chain-of-custody rule: the Cal column traces every NEW artifact to the specific defense
  row it threatens. Cal = ??: threat not yet assessed (must resolve before Phase 4).
  Cal = --: artifact threatens no defense row. Blank Cal: chain-of-custody breach.
  Architectural constraint: ALL NEW-artifact Cal cells must be filled before any Schema C
  row opens. Retroactive calibration after proposals are written is a chain-of-custody breach.

  BREACH CONDITIONS — Schema B is considered breached when:
  (a) Cal column absent or renamed — chain of custody severed;
  (b) any NEW-artifact Cal cell blank — chain-of-custody gap;
  (c) PRIOR artifacts appear above NEW — mandatory sort inverted;
  (d) any Schema C row opened before ALL NEW Cal cells filled — premature indictment.

  SCHEMA C — PROPOSALS TABLE (indictment contract)
  | Type | Proposal | Before | After | Evidence | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  All seven mandatory. Type: ADD, REMOVE, REPRIORITIZE only.
  Defense Defeated (Row #): must name Schema A row number. A proposal without a row number
  is inadmissible — it is a preference stating no specific defense was defeated.
  Inertia Justification [MANDATORY]: check against BANNED FORMS before writing.
  Every typed null declaration is an admission that a change type's inertia was not defeated.

  BREACH CONDITIONS — Schema C is considered breached when:
  (a) any mandatory column absent — indictment form incomplete;
  (b) Defense Defeated lacks row number — inadmissible indictment;
  (c) Inertia Justification contains a banned form — inadmissible rebuttal;
  (d) any absent change type has no typed null — undeclared inertia victory.

  SCHEMA D — PHASE-SPEC TABLE (lifecycle contract)
  | Slot  | Content                                            |
  ENTRY, JOB, EXIT required in every phase. EXIT is the home for stop gates.
  A phase without EXIT lacks its inertia enforcement point.

  BREACH CONDITIONS — Schema D is considered breached when:
  (a) any phase missing ENTRY, JOB, or EXIT;
  (b) stop gate language only in JOB — EXIT position unfilled;
  (c) EXIT exists but contains no named gate.

  VOCABULARY CONTRACT — INADMISSIBLE REBUTTALS:
  ?? (open obligation) | -- (closed decision). In force in all cells.
  INADMISSIBLE REBUTTALS (banned everywhere including null declarations):
    "no change needed"    "nothing to add"      "clearly warranted"
    "seems sufficient"    "a few artifacts"     "several artifacts"
    "some signals"        "not necessary"       any non-integer count
  Check every free-text cell before writing. Non-integer count: gate failure.

  Violation taxonomy:
  - Blank cell where ?? required: inadmissibility violation
  - ?? where -- correct: inadmissibility violation
  - Inadmissible rebuttal anywhere: inadmissibility violation
  - Non-integer count: integer-enforcement gate failure
  - Column added/removed/renamed from declared schema: contract breach

EXIT (Gate-S):
  Both inertia contracts are now declared.
  Schema A declared (strategy inertia armed). Schema B declared (chain of custody armed).
  Schema C declared (indictment form armed). Schema D declared (lifecycle contract armed).
  Vocabulary contract declared. INADMISSIBLE REBUTTALS listed.
  Gate-S: Phase 0 may not begin until Gate-S passes.
  Do not advance to Phase 0 without passing Gate-S.
  Stop. Verify all four schemas declared, each with BREACH CONDITIONS. Halt here.

════════════════════════════════════════════════════════════
Phase 0 — ARM THE DEFENSE REGISTER
════════════════════════════════════════════════════════════

ENTRY:
  Gate-S passed. Both inertia contracts declared. Topic known. No signal artifacts examined.

JOB:
  Open strategy.md. Read full content and extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER (conform to Schema A immutable contract):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension.
  Check Defense Argument cells against INADMISSIBLE REBUTTALS before writing.
  Generic arguments are inadmissible defenses. Each defense must be specific.

EXIT (Gate-0):
  Schema A complete. All cells filled per Schema A contract.
  Defense argument cells checked against INADMISSIBLE REBUTTALS.
  Gate-0: No signal artifact may be examined until Gate-0 passes.
  Do not advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT. The strategy inertia defense has been armed.
  Confirm Gate-0 passed (Schema A complete, all cells filled, defenses checked).
  Write WS-1 MILESTONE. Declaration that the defense is armed and Gate-0 passed.
  Do not open any signal artifact before writing WS-1 MILESTONE. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — ASSEMBLE THE EVIDENCE (Signal Inventory with Calibration)
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 passed. Defense armed. WS-1 MILESTONE written.
  Every NEW artifact will be calibrated against the defense register before proposals open.
  The Cal column maintains the chain of custody from evidence to indictment.

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
  Do not read PRIOR artifacts. Chain of custody runs only through NEW evidence.

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

  CONFLICT DETECTION — Audit NEW artifacts for contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found. NO CHANGE wins because:
  [specific artifact or strategy reference]."

EXIT (Gate-3):
  Delta detections documented. Conflict audit has typed result (table or typed NULL).
  Do not advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before opening any Schema C indictment row:
  Confirm: (1) Gate-3 passed. (2) ALL NEW-artifact Cal cells in Schema B filled
  (chain of custody unbroken). (3) Schema C Inertia Justification labeled [MANDATORY].
  Write WS-2 MILESTONE. Declaration that chain of custody is complete and proposals may open.
  Halt here if any confirmation fails.

════════════════════════════════════════════════════════════
Phase 4 — DELIVER THE INDICTMENT (Proposals)
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 passed. WS-2 MILESTONE written. Chain of custody verified. No proposal rows open.

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
A typed null is an admission that the inertia for this change type was not defeated.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C complete per immutable contract. All cells filled.
  All absent types have typed null declarations using WS-3 template.
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

## V-04: Lifecycle + Inertia Combined — Detailed Lifecycle Slots with Defense Register Spine

**Variation axes**: Lifecycle emphasis (detailed ENTRY/JOB/EXIT slots with explicit phase
boundary conditions) + inertia framing (defense register as primary spine; all proposals
must defeat a named defense row; schemas carry schema inertia in parallel with strategy
inertia). BREACH CONDITIONS cross-reference both lifecycle boundary violations and inertia
contract violations, making each schema's breach conditions a two-dimensional audit surface.

**Hypothesis**: The combination of lifecycle boundaries and inertia framing creates two
independent failure mode surfaces. A skill can fail on lifecycle grounds (wrong phase start
precondition) independently of inertia grounds (proposal without row number). The cross-
referenced BREACH CONDITIONS make this independence explicit: breach condition type (a) is
a lifecycle violation; breach condition type (b) is an inertia violation. A reviewer can
audit each dimension independently without conflating them.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

TWO SIMULTANEOUS INERTIA CONTRACTS:
  STRATEGY INERTIA: The current strategy is correct until evidence defeats a named defense row.
  SCHEMA INERTIA: Declared schemas are immutable output contracts. Column drift = contract breach.

Both contracts are armed in Phase -1 before any file is opened.

Sequential gate chain: Gate-S -> Gate-0 -> Gate-1 -> Gate-2 -> Gate-3 -> Gate-4.
All six gates SHALL appear. The chain SHALL be auditable without reading phase content.

════════════════════════════════════════════════════════════
COMPOUND AUDIT STRUCTURE — TWO INDEPENDENT AUDIT PATHS
════════════════════════════════════════════════════════════

AUDIT PATH 1 (Write-Surface Spine): Scan section headers for WS-1, WS-2, WS-3.
  3 rows declared in write-surface register. 3 section headers SHALL appear.

AUDIT PATH 2 (Lifecycle Slots): Scan each phase for ENTRY / JOB / EXIT.
  EXIT SHALL contain the named gate. Gate-S in Phase -1 EXIT. Gate-0 in Phase 0 EXIT.
  A phase without EXIT is an unguarded lifecycle boundary.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface                   | Trigger                                             |
|-----|------|---------------------------|-----------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact opened    |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before any proposal column filled   |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each null declaration write        |

════════════════════════════════════════════════════════════
Phase -1 — TABLE SCHEMAS (Arming Both Inertia Contracts)
════════════════════════════════════════════════════════════

ENTRY:
  Precondition: execution has just begun. No file opened. No artifact read. No structure built.
  Both inertia contracts are about to be established.
  If any file has been opened before this ENTRY condition is satisfied,
  that constitutes a lifecycle boundary violation of Phase -1.

JOB:
  Declare all four table schemas. Schema inertia is armed upon declaration of each schema.
  Strategy inertia will be armed in Phase 0 when Schema A is populated.

  SCHEMA A — DEFENSE REGISTER (strategy inertia contract)
  | Row | Dimension | Current Strategy Position | Defense Argument |
  All four columns mandatory. Blank cell is a lifecycle inertia violation.
  Sentinel: ?? (unknown), -- (confirmed not-applicable). Defense Argument: check BANNED FORMS.
  The defense register is the indictment ledger. Row numbers are the cross-schema links.

  BREACH CONDITIONS — Schema A:
  (a) LIFECYCLE VIOLATION: Phase 0 populates Schema A before Gate-S passes in Phase -1 EXIT.
  (b) INERTIA VIOLATION: any column absent, renamed, or reordered in the produced table.
  (c) INERTIA VIOLATION: any cell blank where ?? is the required sentinel.
  (d) INERTIA VIOLATION: any Defense Argument contains a banned form.

  SCHEMA B — SIGNAL INVENTORY (chain-of-custody contract)
  | Artifact Filename | Date | NEW / PRIOR | Defenses Implicated (Cal) [MANDATORY] |
  All four columns mandatory. Cal column: blank is a chain-of-custody violation.
  Sort: NEW above PRIOR. Mandatory ordering constraint (schema inertia term).
  Sentinel for Cal: ?? (not yet assessed), -- (no defense threatened). Blank: violation.
  Architectural constraint (cross-schema inertia term): ALL NEW-artifact Cal cells SHALL be
  filled before any Schema C row is opened. This constraint is inherited by Phase 4.

  BREACH CONDITIONS — Schema B:
  (a) LIFECYCLE VIOLATION: Phase 1 opens Cal cells after Phase 4 proposals have begun.
  (b) INERTIA VIOLATION: Cal column absent or renamed.
  (c) INERTIA VIOLATION: any NEW-artifact Cal cell blank.
  (d) INERTIA VIOLATION: PRIOR artifacts appear above NEW.
  (e) CROSS-SCHEMA VIOLATION: any Schema C row opened before ALL NEW Cal cells filled.

  SCHEMA C — PROPOSALS TABLE (indictment contract)
  | Type | Proposal | Before | After | Evidence | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  All seven columns mandatory. Type values: ADD, REMOVE, REPRIORITIZE only.
  Defense Defeated (Row #): must name Schema A row number.
  A proposal that cites no defense row is inadmissible — it is a preference, not an indictment.
  Inertia Justification [MANDATORY]: check BANNED FORMS before writing.

  BREACH CONDITIONS — Schema C:
  (a) LIFECYCLE VIOLATION: any proposal row opened before WS-2 MILESTONE written in Phase 4 ENTRY.
  (b) INERTIA VIOLATION: any mandatory column absent.
  (c) INERTIA VIOLATION: Defense Defeated lacks a Schema A row number.
  (d) INERTIA VIOLATION: Inertia Justification contains a banned form.
  (e) INERTIA VIOLATION: any absent change type has no typed null declaration.

  SCHEMA D — PHASE-SPEC TABLE (lifecycle contract — applied to all phases)
  | Slot  | Content                                             |
  |-------|-----------------------------------------------------|
  | ENTRY | [Preconditions before this phase begins]            |
  | JOB   | [Work instructions for this phase]                  |
  | EXIT  | [Gate — do not advance without this gate passing]   |
  All three slots mandatory in every phase.
  EXIT is the lifecycle home for stop gates. Stop gate only in JOB = lifecycle breach.

  BREACH CONDITIONS — Schema D:
  (a) LIFECYCLE VIOLATION: any phase omits ENTRY, JOB, or EXIT.
  (b) LIFECYCLE VIOLATION: stop gate language appears only in JOB with EXIT absent.
  (c) LIFECYCLE VIOLATION: EXIT exists but contains no named gate with halt instruction.

  VOCABULARY CONTRACT:
  ?? (open obligation) | -- (closed decision). Both in force in all cells.
  BANNED FORMS (inadmissible everywhere including null declaration cells):
    "no change needed"    "nothing to add"      "clearly warranted"
    "seems sufficient"    "a few artifacts"     "several artifacts"
    "some signals"        "not necessary"       any non-integer count
  Check every free-text cell before writing. Non-integer count = gate failure.

EXIT (Gate-S):
  SCHEMA INERTIA NOW IN FORCE: all four schemas declared.
  All four schemas carry two-dimensional BREACH CONDITIONS (lifecycle + inertia).
  Vocabulary contract declared. BANNED FORMS listed.
  Gate-S: Phase 0 SHALL NOT begin until Gate-S passes.
  Do not advance to Phase 0 without passing Gate-S.
  Stop. Verify all four schemas declared, each with BREACH CONDITIONS. Halt here.

════════════════════════════════════════════════════════════
Phase 0 — ARM THE DEFENSE REGISTER
════════════════════════════════════════════════════════════

ENTRY:
  Precondition: Gate-S passed. Both inertia contracts declared.
  Topic known. strategy.md not yet opened. No signal artifacts read.
  If Gate-S has not passed: Phase 0 ENTRY precondition not satisfied. Do not proceed.

JOB:
  Open strategy.md. Read full content and extract last-modified date.
  Record: STRATEGY DATE: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER (conform to Schema A immutable contract):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension.
  Check Defense Argument cells against BANNED FORMS before writing.
  No blank cells. All four columns required. ?? or -- per Schema A rules.

EXIT (Gate-0):
  Schema A SHALL be complete. All cells filled (no blanks; ?? or -- per Schema A contract).
  Defense argument cells SHALL have been checked against BANNED FORMS.
  Gate-0: Phase 1 ENTRY precondition requires Gate-0 passed.
  Phase 0 SHALL NOT advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

Fires at Phase 0 EXIT, after Gate-0 passes, before any signal artifact is opened.
  Lifecycle precondition: Gate-0 passed (Schema A complete, all cells filled).
  Inertia status: defense register armed. Strategy inertia now operative.
  Write WS-1 MILESTONE as declaration that Gate-0 passed and defense is armed.
  Phase 1 ENTRY requires WS-1 MILESTONE. Do not open signal artifacts before writing it. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — ASSEMBLE THE EVIDENCE (Signal Inventory with Calibration)
════════════════════════════════════════════════════════════

ENTRY:
  Precondition: Gate-0 passed. WS-1 MILESTONE written. Schema A complete.
  If WS-1 MILESTONE does not exist: Phase 1 ENTRY precondition not satisfied.

JOB:
  Locate all signal artifact files across 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (conform to Schema B immutable contract):
  | Artifact Filename | Date | NEW / PRIOR | Defenses Implicated (Cal) [MANDATORY] |
  NEW artifacts above PRIOR (mandatory per Schema B contract).
  Chain-of-custody enforcement: ALL NEW-artifact Cal cells SHALL be filled before
  any Schema C row opens. This is the Schema B cross-schema constraint inherited by Phase 4.

  Write mandatory delta summary sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M SHALL be integers. Non-integer form is PROHIBITED.

EXIT (Gate-1):
  Schema B SHALL be complete per contract. NEW above PRIOR. All NEW Cal cells filled.
  Delta sentence SHALL contain integer values.
  Gate-1: Phase 2 ENTRY precondition requires Gate-1 passed.
  Phase 1 SHALL NOT advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — READ THE CHALLENGERS (NEW Artifacts)
════════════════════════════════════════════════════════════

ENTRY:
  Precondition: Gate-1 passed. All NEW-artifact Cal cells filled. No proposals open.
  Chain of custody established from evidence through Cal to defense rows.

JOB:
  Read full content of every artifact classified NEW in Schema B.
  Do not read PRIOR artifacts. PRIOR artifacts are not challengers in this cycle.

EXIT (Gate-2):
  All NEW artifacts SHALL have been read in full.
  Gate-2: Phase 3 ENTRY precondition requires Gate-2 passed.
  Phase 2 SHALL NOT advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — ADJUDICATE DELTAS AND CONFLICTS
════════════════════════════════════════════════════════════

ENTRY:
  Precondition: Gate-2 passed. All NEW artifacts read. Schema A defense register known.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in at least one NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES. Potential indictment material for Phase 4.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations SHALL NOT support ADD or REPRIORITIZE indictments.

  CONFLICT DETECTION — Audit NEW artifacts for cross-artifact contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found. NO CHANGE wins because:
  [specific artifact or strategy reference]."

EXIT (Gate-3):
  Delta detections SHALL be documented.
  Conflict audit SHALL have a typed result (table or typed NULL).
  Gate-3: Phase 4 ENTRY precondition requires Gate-3 passed.
  Phase 3 SHALL NOT advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

Fires at Phase 4 ENTRY. Before opening any Schema C proposal row:
  Lifecycle check: Gate-3 passed.
  Chain-of-custody check: ALL NEW-artifact Cal cells in Schema B filled.
  Inertia check: Schema C Inertia Justification labeled [MANDATORY] per Phase -1 contract.
  Write WS-2 MILESTONE. Halt here if any check fails.
  A proposal row opened before WS-2 MILESTONE triggers Schema C BREACH CONDITION (a).

════════════════════════════════════════════════════════════
Phase 4 — DELIVER THE INDICTMENT (Proposals)
════════════════════════════════════════════════════════════

ENTRY:
  Precondition: Gate-3 passed. WS-2 MILESTONE written. All NEW Cal cells filled. No rows open.
  If WS-2 MILESTONE does not exist: Phase 4 ENTRY precondition not satisfied.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C immutable contract):
  | Type | Proposal | Before | After | Evidence | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Each row is an indictment of a specific Schema A defense register row.
  Defense Defeated (Row #): must name Schema A row number. No row number = inadmissible.
  Inertia Justification: check against BANNED FORMS before writing each cell.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

Fires at each null declaration write in Phase 4 JOB.
Mandatory template: "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Before writing reason: check against BANNED FORMS.
  "no change needed" — banned. "nothing to add" — banned.
  Any match disqualifies. Reason must cite specific evidence or strategy content.
A typed null is an inertia-victory declaration: the change type's defense was not defeated.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C SHALL be complete per immutable contract. All cells filled.
  All absent types SHALL have typed null declarations using WS-3 template.
  Inertia and null reason cells SHALL have been checked against BANNED FORMS.
  strategy.md SHALL NOT be modified before user confirmation is received.
  Gate-4: Apply Phase requires Gate-4 passed and user confirmation.
  Phase 4 SHALL NOT advance to Apply Phase without passing Gate-4.
  Stop. Verify every cell and every null uses typed template. Halt here.

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

---

## V-05: Modal + Table Schemas Combined — Formal Modal Language with Comprehensive Phase -1

**Variation axes**: Phrasing register (formal modal language — SHALL/SHALL NOT/MUST/MUST NOT
throughout all obligation positions) + TABLE SCHEMAS as Phase -1 with the most comprehensive
schema declarations, BREACH CONDITIONS as first-class structural elements using SHALL language,
and a three-path audit system. Schema B's Cal column is named explicitly as the architectural
dependency of Schema C (a cross-schema contract term stated in Phase -1, not in Phase 4).
The ordering constraint (Cal completion before proposals) is inherited by Phase 4 from the
Phase -1 declaration, making it structurally upstream rather than embedded in phase instructions.

**Hypothesis**: When modal language and comprehensive Phase -1 schema declarations combine,
two independent forcing functions operate simultaneously. Modal language makes every obligation
binary-checkable; Phase -1 with BREACH CONDITIONS makes schema compliance structurally visible
without reading phase content. The cross-schema Cal dependency declared in Phase -1 (not in
Phase 4) means Phase 4's obligation is inherited from a prior contract, not invented locally.
A reviewer can audit schema compliance from Phase -1 alone without reading Phase 1 or Phase 4.

---

```
You are executing the topic:plan skill — revise the signal strategy as new information arrives.

Default outcome: NO CHANGE to strategy.md. All proposals SHALL defeat the null.

Sequential gate chain (SHALL be complete as declared): Gate-S -> Gate-0 -> Gate-1 -> Gate-2 -> Gate-3 -> Gate-4.

════════════════════════════════════════════════════════════
THREE-PATH AUDIT SYSTEM
════════════════════════════════════════════════════════════

PATH 1 (Schema Spine): Count named schema sections in Phase -1.
  Four schemas SHALL be declared; four schema blocks SHALL appear.
  Completeness auditable by count without reading phase content.

PATH 2 (Write-Surface Spine): Count WS-1, WS-2, WS-3 section headers.
  Write-surface register declares 3 rows. 3 section headers SHALL appear.

PATH 3 (Lifecycle Slots): Scan EXIT slots across Gate-S through Gate-4.
  Every EXIT SHALL contain a named gate. A missing EXIT or empty gate is a PATH 3 failure.

════════════════════════════════════════════════════════════
WRITE SURFACE REGISTER
════════════════════════════════════════════════════════════

| Row | ID   | Surface Type              | Trigger                                            |
|-----|------|---------------------------|----------------------------------------------------|
|  1  | WS-1 | Pre-read barrier          | Phase 0 EXIT — before any signal artifact opened   |
|  2  | WS-2 | Schema boundary check     | Phase 4 ENTRY — before any proposal column filled  |
|  3  | WS-3 | Null declaration template | Phase 4 JOB — at each null declaration write       |

════════════════════════════════════════════════════════════
Phase -1 — TABLE SCHEMAS (Schema Contract Declarations)
════════════════════════════════════════════════════════════

ENTRY:
  No file SHALL have been opened. No artifact SHALL have been read.
  No structure SHALL exist. This phase SHALL be the first act of execution.
  Violation: any file opened before Phase -1 ENTRY is a structural ordering violation.

JOB:
  All table schemas used in this skill execution SHALL be declared in this phase.
  Every table produced in this output SHALL conform to a schema declared here.
  Producing a table with columns not declared in this phase is PROHIBITED.
  Each schema SHALL carry inline BREACH CONDITIONS.

  CROSS-SCHEMA DEPENDENCY (declared here as a Phase -1 contract term):
  Schema C SHALL NOT be opened until Schema B's Cal dependency is satisfied.
  This dependency is inherited by Phase 4 from this Phase -1 declaration.
  It is a cross-schema contract term, not a Phase 4 instruction.
  Retroactive Cal completion after Schema C rows are opened is PROHIBITED.

  SCHEMA A — DEFENSE REGISTER
  | Row | Dimension | Current Strategy Position | Defense Argument |
  All four columns SHALL be present in the produced table.
  Sentinel: ?? SHALL be used for unknown values. -- SHALL be used for confirmed not-applicable only.
  Blank cell is PROHIBITED regardless of context.
  Defense Argument cells SHALL be checked against BANNED FORMS before writing.
  Phase used: Phase 0.

  BREACH CONDITIONS — Schema A SHALL be considered breached when:
  (a) any column is absent, renamed, or reordered in the produced table;
  (b) any cell is blank where ?? is the required sentinel;
  (c) any Defense Argument cell contains a banned form;
  (d) Phase 0 begins without Gate-S having passed — this is a lifecycle ordering violation.

  SCHEMA B — SIGNAL INVENTORY
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  All four columns SHALL be present. Cal column SHALL NOT be omitted or renamed.
  Sort order: NEW artifacts SHALL appear above PRIOR artifacts. Inversion is PROHIBITED.
  Sentinel for Cal: ?? SHALL be used if implication is unknown.
              -- SHALL be used if no rows are implicated.
              Blank SHALL NOT be used — it is PROHIBITED.
  CAL DEPENDENCY (inherited from Phase -1 cross-schema term):
  ALL NEW-artifact Cal cells SHALL be filled before any Schema C row is opened.
  Opening a Schema C row before Cal completion is PROHIBITED as a cross-schema violation.
  Phase used: Phase 1.

  BREACH CONDITIONS — Schema B SHALL be considered breached when:
  (a) Cal column is absent or renamed;
  (b) any NEW-artifact Cal cell is blank;
  (c) PRIOR artifacts appear above any NEW artifact;
  (d) any Schema C row is opened before ALL NEW-artifact Cal cells are filled —
      this is PROHIBITED; it triggers the Phase -1 cross-schema dependency.

  SCHEMA C — PROPOSALS TABLE
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  All seven columns SHALL be present. Type values SHALL be ADD, REMOVE, or REPRIORITIZE only.
  Other Type values are PROHIBITED.
  Defense Defeated (Row #) SHALL cite a Schema A row number.
  Prose description alone is PROHIBITED as a substitute for a row number.
  Inertia Justification SHALL be checked against BANNED FORMS before writing.
  CROSS-SCHEMA DEPENDENCY (from Phase -1): Schema C SHALL NOT be opened before
  Schema B Cal dependency is satisfied. This is a contract term inherited from Phase -1.
  Phase used: Phase 4.

  BREACH CONDITIONS — Schema C SHALL be considered breached when:
  (a) any mandatory column is absent;
  (b) Defense Defeated lacks a Schema A row number;
  (c) Inertia Justification contains a banned form;
  (d) any absent change type has no typed null declaration;
  (e) any Schema C row is opened before WS-2 MILESTONE is written —
      this is PROHIBITED as a Phase 4 ENTRY lifecycle violation.

  SCHEMA D — PHASE-SPEC TABLE (applied in every phase including this one)
  | Slot  | Content                                                     |
  |-------|-------------------------------------------------------------|
  | ENTRY | [Preconditions that SHALL be true before this phase begins] |
  | JOB   | [Work instructions for this phase]                          |
  | EXIT  | [Gate — Phase N SHALL NOT advance without this gate]        |
  All three slots SHALL be present in every phase.
  EXIT SHALL be the structural home for stop gate language.
  Stop gate language appearing only in ENTRY or JOB SHALL NOT satisfy the EXIT requirement.
  Phase used: every phase (Path 3 audits EXIT slots for gate content).

  BREACH CONDITIONS — Schema D SHALL be considered breached when:
  (a) any phase omits ENTRY, JOB, or EXIT;
  (b) stop gate language appears only in JOB or ENTRY with EXIT absent or empty;
  (c) EXIT exists but does not contain a named gate and an explicit halt instruction.

  VOCABULARY CONTRACT:
  Sentinel tokens SHALL be applied as follows:
    ?? — SHALL be used for unknown or unfilled values. SHALL NOT be left blank.
    -- — SHALL be used only for confirmed not-applicable entries.
  BANNED FORMS — verbatim match in any free-text cell is PROHIBITED:
    "no change needed"    "nothing to add"      "clearly warranted"
    "seems sufficient"    "a few artifacts"     "several artifacts"
    "some signals"        "not necessary"       any non-integer count
  Every free-text cell SHALL be checked against this list before it is written.
  Null declaration reason cells SHALL NOT receive a scope exemption — banned forms are
  PROHIBITED in null declarations equally.
  Integer-enforcement: "a few", "several", "some", or any non-integer in any count field
  is PROHIBITED and SHALL be treated as a gate failure.

  Violation taxonomy:
  - Blank cell where ?? required: vocabulary violation
  - ?? where -- is correct: vocabulary violation
  - Any banned form in any free-text cell: vocabulary violation
  - Non-integer count in any count field: integer-enforcement gate failure
  - Column added/removed/renamed from declared schema: schema contract breach

EXIT (Gate-S):
  All four schemas SHALL be declared with full column definitions and sentinel rules.
  All four schemas SHALL carry inline BREACH CONDITIONS.
  Phase -1 cross-schema dependency SHALL be declared.
  Vocabulary contract SHALL be declared.
  Phase 0 SHALL NOT begin until Gate-S passes.
  Stop. Verify all four schema declarations are complete with BREACH CONDITIONS. Halt here.

════════════════════════════════════════════════════════════
Phase 0 — Strategy Read and Defense Register
════════════════════════════════════════════════════════════

ENTRY:
  Gate-S SHALL have passed. All schemas declared with BREACH CONDITIONS.
  Topic known. strategy.md not yet opened. No signal artifacts read.

JOB:
  Open strategy.md. Read full content. Extract last-modified date.
  STRATEGY DATE SHALL be recorded as: [YYYY-MM-DD]

  Build SCHEMA A — DEFENSE REGISTER (conform to Schema A declared in Phase -1):
  | Row | Dimension | Current Strategy Position | Defense Argument |
  One row per potential change dimension.
  Defense Argument cells SHALL be checked against BANNED FORMS before writing.
  No blank cells SHALL appear. All four columns are required.

EXIT (Gate-0):
  Schema A SHALL be complete. All cells SHALL be filled (no blanks; ?? or -- per Schema A).
  Defense Argument cells SHALL have been checked against BANNED FORMS.
  Phase 0 SHALL NOT advance to Phase 1 without passing Gate-0.
  Stop. Verify every Schema A cell is filled. Halt here.

## WS-1 — Pre-Read Barrier

> WS-1 MILESTONE — fulfills Register Row 1

SHALL fire at Phase 0 EXIT, after Gate-0 passes, before any signal artifact is opened.
  Gate-0 SHALL have passed (Schema A complete, all cells filled).
  WS-1 MILESTONE SHALL be written as declaration that Gate-0 passed.
  Opening any signal artifact before WS-1 MILESTONE is written is PROHIBITED. Halt here.

════════════════════════════════════════════════════════════
Phase 1 — Signal Inventory with Calibration
════════════════════════════════════════════════════════════

ENTRY:
  Gate-0 SHALL have passed. WS-1 MILESTONE SHALL have been written. Schema A complete.

JOB:
  Locate all signal artifact files across all 9 namespaces:
  scout, draft, review, flow, trace, prove, listen, program, topic.

  Build SCHEMA B — SIGNAL INVENTORY (conform to Schema B declared in Phase -1):
  | Artifact Filename | Date | NEW / PRIOR | Defense Register Rows (Cal) [MANDATORY] |
  NEW artifacts SHALL appear above PRIOR artifacts.
  ALL NEW-artifact Cal cells SHALL be filled before any Schema C row is opened
  (Phase -1 cross-schema dependency — inherited from Phase -1, not invented here).

  Delta summary sentence SHALL state exactly:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M SHALL be integers. Non-integer form is PROHIBITED.

EXIT (Gate-1):
  Schema B SHALL be complete. NEW SHALL appear above PRIOR.
  All NEW-artifact Cal cells SHALL be filled.
  Delta sentence SHALL contain integer values.
  Phase 1 SHALL NOT advance to Phase 2 without passing Gate-1.
  Stop. Verify all NEW-artifact Cal cells are filled. Halt here.

════════════════════════════════════════════════════════════
Phase 2 — Read NEW Artifacts
════════════════════════════════════════════════════════════

ENTRY:
  Gate-1 SHALL have passed. All NEW-artifact Cal cells filled. No proposals open.

JOB:
  Read full content of every artifact classified NEW in Schema B.
  PRIOR artifacts SHALL NOT be read in this phase.

EXIT (Gate-2):
  All NEW artifacts SHALL have been read.
  Phase 2 SHALL NOT advance to Phase 3 without passing Gate-2.
  Stop. Confirm every NEW artifact has been read. Halt here.

════════════════════════════════════════════════════════════
Phase 3 — Delta Detection and Conflict Audit
════════════════════════════════════════════════════════════

ENTRY:
  Gate-2 SHALL have passed. All NEW artifacts read. Schema A defense arguments available.

JOB:
  DELTA DETECTION — For each observation from NEW artifacts:
    Condition 1: present in at least one NEW artifact (date > STRATEGY DATE)?
    Condition 2: absent from strategy.md?
  CONFIRMED DELTA = both YES.
  PRIOR-ONLY = Condition 1 YES, Condition 2 NO. Annotate: "PRIOR-ONLY — not a delta."
  PRIOR-ONLY observations SHALL NOT support ADD or REPRIORITIZE proposals.

  CONFLICT DETECTION — Audit NEW artifacts for cross-artifact contradictions.
  If found: CONFLICT REGISTER table.
  If none: "CONFLICT DETECTION — NULL: No contradictions found. NO CHANGE wins because:
  [specific artifact reference]."

EXIT (Gate-3):
  Delta detections SHALL be documented.
  Conflict audit SHALL have a typed result (table or typed NULL).
  Phase 3 SHALL NOT advance to Phase 4 without passing Gate-3.
  Stop. Verify conflict audit has typed result. Halt here.

## WS-2 — Schema Boundary Check

> WS-2 MILESTONE — fulfills Register Row 2

SHALL fire at Phase 4 ENTRY. SHALL fire before any Schema C column is filled.
  Gate-3 SHALL have passed.
  ALL NEW-artifact Cal cells in Schema B SHALL be filled (Phase -1 cross-schema dependency).
  Schema C Inertia Justification SHALL be labeled [MANDATORY] per Phase -1 declaration.
  WS-2 MILESTONE SHALL be written.
  Opening a Schema C row before WS-2 MILESTONE is written is PROHIBITED. Halt here.

════════════════════════════════════════════════════════════
Phase 4 — Proposals
════════════════════════════════════════════════════════════

ENTRY:
  Gate-3 SHALL have passed. WS-2 MILESTONE SHALL have been written.
  All NEW Cal cells filled. No proposal rows open.

JOB:
  Build SCHEMA C — PROPOSALS TABLE (conform to Schema C declared in Phase -1):
  | Type | Proposal | Before | After | Evidence Artifact | Inertia Justification [MANDATORY] | Defense Defeated (Row #) |
  Inertia Justification cells SHALL be checked against BANNED FORMS before writing.
  Defense Defeated SHALL cite a Schema A row number. Prose alone is PROHIBITED.

## WS-3 — Null Declaration Template

> WS-3 MILESTONE — fulfills Register Row 3

SHALL fire at each null declaration write in Phase 4 JOB.
Null declarations SHALL use mandatory template:
  "[TYPE] — NULL: No proposals. NO CHANGE wins because: [specific reason]."
Reason cells SHALL be checked against BANNED FORMS before writing.
  "no change needed" is PROHIBITED. "nothing to add" is PROHIBITED.
  Any banned form SHALL disqualify the null declaration.

Required for each absent type:
  ADD — NULL: No additions proposed. NO CHANGE wins because: [specific reason].
  REMOVE — NULL: No removals proposed. NO CHANGE wins because: [specific reason].
  REPRIORITIZE — NULL: No reprioritizations proposed. NO CHANGE wins because: [specific reason].

EXIT (Gate-4):
  Schema C SHALL be complete. All cells SHALL be filled.
  All absent types SHALL have typed null declarations using WS-3 template.
  All Inertia and null reason cells SHALL have been checked against BANNED FORMS.
  strategy.md SHALL NOT be modified before user confirmation is received.
  Phase 4 SHALL NOT advance to Apply Phase without passing Gate-4.
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
