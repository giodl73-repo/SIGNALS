Looking at the v12 rubric, I'll design 5 variations targeting different structural axes. Let me write them now.

---

# `topic:plan` — Skill Variations V-01 through V-05 (Round 12)

---

## V-01 — Lifecycle Emphasis

**Axis**: Lifecycle emphasis — every phase carries named ENTRY / JOB / EXIT slots, making phase boundaries architectural rather than narrative annotations.

**Hypothesis**: Naming ENTRY/JOB/EXIT slots makes stop gates the natural content of the EXIT slot, preventing gate language from appearing as trailing prose that can be skipped. Phase-skip becomes structurally detectable.

---

```
SKILL: topic:plan
PURPOSE: Revise the signal strategy as new information arrives.

Read the current strategy.md and all gathered signal artifacts.
Identify what has changed since the strategy was written.
Propose additions, removals, or re-prioritizations.
Stop and present proposals to the user before modifying strategy.md.
Apply confirmed changes only after explicit approval.

────────────────────────────────────────
VOCABULARY CONTRACT
────────────────────────────────────────

Sentinel tokens used throughout this skill:

  ??   Open obligation — unknown, not yet filled, requires resolution before advancing
  --   Closed decision — deliberately absent, not applicable to this row

Violation conditions (named, not implied):
  - Leaving a cell blank when ?? would be correct is a vocabulary violation
  - Leaving a cell blank when -- would be correct is a vocabulary violation
  - Using ?? for a row where inapplicability is already established is a vocabulary violation
  - Writing "a few", "several", "some", or any non-integer count is an integer-enforcement gate failure
  - Writing "no change needed", "clearly warranted", "minor adjustment", or "seems reasonable"
    in any justification cell is a banned-forms violation

────────────────────────────────────────
PHASE 1 — READ STRATEGY.MD
────────────────────────────────────────

ENTRY: No prior reads have occurred. strategy.md has not been read.

JOB:
  Read strategy.md.
  Extract and record:
    - Strategy file date (the date the strategy was last written or revised)
    - Active topics under coverage
    - Namespace priorities as stated in the strategy
    - Any explicit gaps, unknowns, or deferred decisions the strategy names

  Output a STRATEGY SUMMARY block with these four items populated.
  Use ?? for any item that cannot be determined from the file.
  Do not paraphrase the strategy date — cite it exactly as it appears.

EXIT — Gate 1:
  The STRATEGY SUMMARY block must be complete before proceeding.
  Every cell must contain either a value, ??, or --.
  A blank cell is a gate failure.
  Do not advance to Phase 2 without passing Gate 1.

────────────────────────────────────────
PHASE 2 — SIGNAL INVENTORY
────────────────────────────────────────

ENTRY: Strategy date is known. strategy.md has been read and summarized.

JOB:
  Scan all signal artifacts across all 9 namespaces:
    scout / draft / review / flow / trace / prove / listen / program / topic

  For each namespace produce one inventory row:

    | Namespace | Artifact Filenames | Artifact Dates | Classification |
    |-----------|-------------------|----------------|----------------|

  Classification column values:
    NEW   — artifact date is after the strategy file date
    PRIOR — artifact date is on or before the strategy file date
    ??    — date cannot be determined from available information

  Rules:
    - Every namespace must have a row. Absence of artifacts is not a reason to omit a row.
      A namespace with no artifacts gets: filenames = --, dates = --, classification = --
    - Artifact filenames must be the actual filenames, not descriptions.
      If a filename cannot be retrieved, use ?? in that cell.
    - Do not summarize multiple artifacts into one cell. Each artifact gets its own filename entry.

EXIT — Gate 2:
  All 9 namespace rows must be present.
  No cell may be blank — only values, ??, or --.
  The strategy date used for classification must match the date recorded in Phase 1.
  Do not advance to Phase 3 without passing Gate 2.

────────────────────────────────────────
PHASE 3 — DELTA CLASSIFICATION
────────────────────────────────────────

ENTRY: Signal inventory is complete. All 9 namespaces have been assessed.

JOB:
  From the Phase 2 table, extract two separate lists:

    NEW ARTIFACTS (date > strategy date):
      List each artifact filename and the namespace it belongs to.

    PRIOR ARTIFACTS (date ≤ strategy date):
      List each artifact filename. These do not drive proposals.

  Then produce a mandatory templated delta sentence:

    "Strategy was written on [EXACT DATE FROM PHASE 1].
     [N] artifacts are NEW.
     [M] artifacts are PRIOR."

  N and M must be exact integers.
  Writing "a few", "several", "some", or any non-integer value is a gate failure.

  Only NEW artifacts are eligible to drive change proposals in Phase 4.
  PRIOR artifacts are ineligible and must not appear in any proposal row as evidence.

EXIT — Gate 3:
  The delta sentence must be present with integer counts.
  The NEW list and PRIOR list must be non-overlapping and complete.
  Do not advance to Phase 4 without passing Gate 3.

────────────────────────────────────────
PHASE 4 — CHANGE PROPOSALS
────────────────────────────────────────

ENTRY: Delta classification is complete. NEW artifacts are identified.

JOB:
  For each NEW artifact, assess whether it warrants a change to strategy.md.
  Produce a proposal table:

    | Change Type | Proposal Description | Evidence Artifact | Before | After | Inertia Justification |
    |-------------|---------------------|-------------------|--------|-------|-----------------------|

  Change Type must be one of: ADD / REMOVE / REPRIORITIZE
  There is no "NO CHANGE" change type. Null change declarations are handled separately below.

  Evidence Artifact: the exact filename of the NEW artifact driving this proposal.
  Before: the current strategy.md text that this proposal affects (quoted or described).
  After: the proposed replacement text.
  Inertia Justification: the specific reason why the current strategy is insufficient given this
    new artifact. This column is mandatory.

  BANNED FORMS in Inertia Justification:
    Check each cell against this list before writing. Any match disqualifies the row:
      "no change needed"
      "already covered"
      "clearly warranted"
      "minor adjustment"
      "seems reasonable"
      "minor update"

  NULL DECLARATIONS (required if a change type is absent):
  If no ADD proposals exist: state "ADD — NULL. No new coverage dimension identified in NEW artifacts."
  If no REMOVE proposals exist: state "REMOVE — NULL. No obsolete coverage dimension identified."
  If no REPRIORITIZE proposals exist: state "REPRIORITIZE — NULL. No priority shift identified."

  Silence is not a null declaration. Each absent type must be explicitly declared.

EXIT — Gate 4:
  All three change types are either represented by at least one proposal row or have an
    explicit typed null declaration.
  Every non-null proposal row must have a value in every column (no blanks, no ??).
  Every inertia justification cell must be checked against the BANNED FORMS list.
  Do not advance to Phase 5 without passing Gate 4.

────────────────────────────────────────
PHASE 5 — CONFLICT DETECTION
────────────────────────────────────────

ENTRY: Change proposals are complete and gate-checked.

JOB:
  Review all proposal rows for cross-artifact contradictions:
    - Does any ADD proposal conflict with any REMOVE proposal?
    - Does any REPRIORITIZE proposal contradict the direction of another?
    - Does any proposal assume a fact that a different artifact contradicts?

  If conflicts are found: list each conflict as a named row with the two conflicting proposals
    identified by their proposal rows.

  If no conflicts are found: state "CONFLICT DETECTION — NULL. No cross-artifact contradictions
    identified across [N] proposals."

EXIT — Gate 5:
  Conflict detection must be explicitly resolved (either list or null declaration).
  Do not advance to Phase 6 without passing Gate 5.

────────────────────────────────────────
PHASE 6 — CONFIRMATION GATE
────────────────────────────────────────

ENTRY: Proposals are final. Conflicts are resolved.

JOB:
  Present the full proposal set to the user.
  Display the delta sentence, the proposal table, and all null declarations.

  Then display this gate exactly:

  ┌─────────────────────────────────────────────────────┐
  │  STRATEGY UPDATE GATE                               │
  │                                                     │
  │  strategy.md has NOT been modified.                 │
  │  Respond with one of:                               │
  │                                                     │
  │    YES     — apply all proposals as shown           │
  │    NO      — discard all proposals, no change       │
  │    REVISED — specify which proposals to change      │
  │                                                     │
  │  strategy.md will not be touched until you respond. │
  └─────────────────────────────────────────────────────┘

  Do not proceed to Phase 7. Wait for user response.

EXIT — Gate 6:
  This gate does not pass automatically.
  User must provide YES, NO, or REVISED.
  Proceeding without a response is a gate failure.

────────────────────────────────────────
PHASE 7 — APPLY UPDATES
────────────────────────────────────────

ENTRY: User has responded YES or REVISED to the confirmation gate.
  If NO: skip Phase 7. Report "No changes applied." End skill.

JOB:
  Apply the confirmed proposals to strategy.md.
  For REVISED responses: apply only the proposals the user confirmed.
  Write the updated strategy.md.
  Report: "strategy.md updated. [N] proposals applied."

EXIT:
  strategy.md is saved.
  Report the count of applied proposals.
  Skill complete.
```

---

## V-02 — Inertia Framing

**Axis**: Inertia framing — the defense register is the load-bearing architectural element. The status quo is treated as an active competitor. Every proposal must name and defeat a pre-committed defense argument, with row-number citation.

**Hypothesis**: Front-loading defense arguments before any artifact read forces explicit acknowledgment of the status quo's strength, making inertia linkage evidence-based rather than post-hoc. Proposals that cannot defeat a named defense are rejected structurally, not stylistically.

---

```
SKILL: topic:plan
PURPOSE: Revise the signal strategy as new information arrives. The strategy
is presumed correct until a new signal defeats a specific defense argument.
This skill is structured around that adversarial model.

────────────────────────────────────────
VOCABULARY CONTRACT
────────────────────────────────────────

  ??   Open obligation (unknown, requires resolution)
  --   Closed decision (deliberately absent / not applicable)

Banned forms — these phrases are disqualified in all justification cells:
  "no change needed" | "already covered" | "clearly warranted"
  "minor adjustment" | "seems reasonable" | "minor update"

────────────────────────────────────────
PHASE 0 — PRE-SIGNAL DEFENSE REGISTER
────────────────────────────────────────

Before reading any artifact, commit a defense register.

The defense register captures the current strategy's best argument for why
each dimension does NOT need to change. This is the competitor. Every
subsequent proposal must name and defeat a row from this register.

STEP 0A — Read strategy.md.
  Extract: strategy date, active topics, namespace priorities, stated gaps.

STEP 0B — Commit the Defense Register table before reading any signal artifact:

  | Row | Dimension | Current Strategy Position | Defense Argument |
  |-----|-----------|--------------------------|-----------------|

  Populate one row per coverage dimension the strategy addresses.
  Defense Argument: the strongest case the strategy can make for no change.
    This is the strategy speaking in its own defense — write it as such.
    Use ?? if you cannot identify a defense argument for a dimension.
    Do not leave Defense Argument blank.

  BANNED FORMS in Defense Argument:
    "no information available" | "unclear" | "not addressed"
    If the strategy genuinely has no defense for a dimension, write:
    "No defense committed — this dimension is already acknowledged as a gap."

GATE 0 — Hard stop.
  The defense register table must be fully populated before proceeding.
  Every row must have a value in every column (no blank cells).
  No artifact reads may occur until Gate 0 passes.
  Do not advance to Phase 1 without passing Gate 0.

────────────────────────────────────────
PHASE 1 — SIGNAL INVENTORY
────────────────────────────────────────

Read all signal artifacts across the 9 namespaces:
  scout / draft / review / flow / trace / prove / listen / program / topic

Produce the inventory table. One row per artifact:

  | Namespace | Artifact Filename | Date | Classification | Defense Row Implicated |
  |-----------|------------------|------|----------------|------------------------|

  Classification: NEW (after strategy date) or PRIOR (on or before) or ??
  Defense Row Implicated: the row number(s) from the Phase 0 defense register
    that this artifact is relevant to. Use ?? if unknown. Use -- if the
    artifact touches no defended dimension.

  Sort order: NEW artifacts first, PRIOR artifacts second within each namespace.

GATE 1:
  All 9 namespaces must have at least a -- row (no namespace omitted).
  Defense Row Implicated column must be filled for all NEW artifacts.
  Do not advance to Phase 2 without passing Gate 1.

────────────────────────────────────────
PHASE 2 — DELTA QUANTIFICATION
────────────────────────────────────────

From Phase 1, produce:

  NEW artifact list: filenames, namespace, Defense Row Implicated
  PRIOR artifact list: filenames, namespace

Mandatory delta sentence (required, integer values only):
  "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  Writing "a few", "several", "some", or any non-integer is a gate failure.

GATE 2:
  Delta sentence must be present.
  N and M must be integers.
  Do not advance to Phase 3 without passing Gate 2.

────────────────────────────────────────
PHASE 3 — PROPOSAL TABLE WITH DEFENSE LINKAGE
────────────────────────────────────────

For each NEW artifact, assess whether it warrants a change to strategy.md.
Each proposal must name and defeat a specific defense register row.

Produce the proposal table:

  | # | Change Type | Proposal | Evidence Artifact | Before | After | Defense Defeated (Row #) | Defeat Argument |
  |---|-------------|----------|------------------|--------|-------|--------------------------|-----------------|

  Change Type: ADD / REMOVE / REPRIORITIZE
  Evidence Artifact: exact filename from the NEW artifact list.
  Defense Defeated (Row #): the row number from the Phase 0 defense register
    that this proposal defeats. This column is mandatory.
    A named defense without a row number does not satisfy this criterion.
    Use ?? if the defeated row cannot be identified — this flags a weak proposal.
  Defeat Argument: the specific claim from the NEW artifact that overrides the
    defense argument at that row. Quote or cite specifically.

  CELL-LEVEL CHECK: Before writing each Defeat Argument cell, check it against
    the BANNED FORMS list above. Any match disqualifies the row.

NULL DECLARATIONS (for absent change types):
  "ADD — NULL. No new coverage dimension identified. [Defense rows consulted: N, M, ...]"
  "REMOVE — NULL. No obsolete coverage dimension identified. [Defense rows consulted: N, M, ...]"
  "REPRIORITIZE — NULL. No priority shift identified. [Defense rows consulted: N, M, ...]"

  Null declarations must name which defense rows were evaluated and found undefeated.
  A null declaration without defense row citations is incomplete.

GATE 3:
  Every non-null proposal row must have an integer row number in Defense Defeated.
  Every null declaration must name at least one defense row.
  Defeat Argument cells must be checked against BANNED FORMS.
  Do not advance to Phase 4 without passing Gate 3.

────────────────────────────────────────
PHASE 4 — CONFLICT DETECTION
────────────────────────────────────────

Review all proposal rows for contradictions:
  - Conflicting ADD / REMOVE pairs
  - Contradictory priority directions
  - Proposals that assume facts other proposals deny

If conflicts found: name each conflict with the two proposal row numbers involved.
If no conflicts: "CONFLICT DETECTION — NULL. No contradictions across [N] proposals."

────────────────────────────────────────
PHASE 5 — CONFIRMATION GATE
────────────────────────────────────────

Present the complete defense register, delta sentence, proposal table,
null declarations, and conflict detection result.

Display this gate:

  ┌──────────────────────────────────────────────────────────────┐
  │  STRATEGY UPDATE GATE                                        │
  │                                                              │
  │  strategy.md has NOT been modified.                          │
  │                                                              │
  │  [N] proposals were generated.                               │
  │  [M] defense rows were defeated.                             │
  │  [K] defense rows were consulted and held (no change).       │
  │                                                              │
  │  Respond: YES / NO / REVISED                                 │
  │                                                              │
  │  strategy.md will not be touched until you respond.          │
  └──────────────────────────────────────────────────────────────┘

Wait for user response. Do not proceed without a response.

────────────────────────────────────────
PHASE 6 — APPLY UPDATES
────────────────────────────────────────

On YES or REVISED: apply confirmed proposals to strategy.md. Report count.
On NO: report "No changes applied." End skill.
```

---

## V-03 — Output Format (Table-dominant with Phase -1 Schema Declaration)

**Axis**: Output format — all structured output is governed by pre-declared table schemas. Phase -1 defines every table the skill produces, with mandatory column labels, sentinel token usage, and typed violation taxonomy with category labels.

**Hypothesis**: Pre-declaring named table schemas (Schema A through Schema E) makes column omissions structurally detectable without reading phase content. A typed violation taxonomy enables class-level auditing of failure modes.

---

```
SKILL: topic:plan
PURPOSE: Revise the signal strategy as new information arrives. Read
strategy.md and all signal artifacts. Classify artifacts by age against the
strategy date. Propose typed changes. Confirm before writing.

────────────────────────────────────────
PHASE -1 — TABLE SCHEMAS
────────────────────────────────────────

ENTRY: No files have been read. No tables have been produced.

JOB: Declare all table schemas used by this skill. Every table this skill
produces is governed by one of the schemas below. Producing a table with
columns not matching the schema is a contract breach.

────────────────
Schema A — Strategy Summary
────────────────
Columns: [Item] | [Value]
Mandatory rows: Strategy Date, Active Topics, Namespace Priorities, Named Gaps
Sentinel usage: ?? for unknown items, -- not applicable here (all rows are required)
Breach conditions:
  - Schema A breach: any of the four mandatory rows is absent
  - Schema A breach: Value cell is blank (must use ?? if unknown)
  - Schema A breach: Strategy Date row contains a non-exact date (paraphrase not allowed)

────────────────
Schema B — Signal Inventory
────────────────
Columns: [Namespace] | [Artifact Filenames] | [Artifact Dates] | [Classification]
Mandatory rows: one row per namespace (9 rows minimum: scout, draft, review,
  flow, trace, prove, listen, program, topic)
Classification vocabulary: NEW | PRIOR | ??
Sentinel usage: -- in Artifact Filenames and Artifact Dates when no artifacts exist
  for a namespace; ?? when artifacts exist but dates cannot be determined
Breach conditions:
  - Schema B breach: fewer than 9 namespace rows
  - Schema B breach: Classification cell contains any value other than NEW, PRIOR, ??, or --
  - Schema B breach: Artifact Filenames cell contains a description rather than a filename
  - Schema B breach: blank cell (must use ??, --, or a value)

────────────────
Schema C — Proposal Table
────────────────
Columns: [#] | [Change Type] | [Proposal Description] | [Evidence Artifact]
         | [Before] | [After] | [Inertia Justification]
Change Type vocabulary: ADD | REMOVE | REPRIORITIZE
Evidence Artifact: exact filename from NEW artifacts only
Inertia Justification: mandatory column — reason why the current strategy is
  insufficient given this artifact; banned forms apply (see Vocabulary Contract)
Sentinel usage: ?? permitted only in Evidence Artifact if filename cannot be retrieved
Breach conditions:
  - Schema C breach: any column absent or renamed
  - Schema C breach: Change Type cell contains any value outside ADD/REMOVE/REPRIORITIZE
  - Schema C breach: Inertia Justification cell is blank or contains a banned form
  - Schema C breach: Evidence Artifact contains an artifact whose Classification
      is PRIOR (prior artifacts may not drive proposals)

────────────────
Schema D — Null Declaration Table
────────────────
Columns: [Change Type] | [Declaration] | [Reason]
Mandatory rows: one row per change type absent from Schema C (ADD, REMOVE, REPRIORITIZE)
Declaration vocabulary: [TYPE] — NULL
Reason: specific statement explaining why no [TYPE] proposals were warranted
Sentinel usage: -- not applicable (rows are only created when a type is absent)
Breach conditions:
  - Schema D breach: absent change type not represented (silence is not a null declaration)
  - Schema D breach: Reason cell is blank or contains a banned form
  - Schema D breach: Declaration cell value deviates from the [TYPE] — NULL pattern

────────────────
Schema E — Conflict Detection Table
────────────────
Columns: [Conflict ID] | [Proposal A Row #] | [Proposal B Row #] | [Conflict Description]
If no conflicts: produce null form "CONFLICT DETECTION — NULL. [N] proposals
  checked. No contradictions identified."
Breach conditions:
  - Schema E breach: conflict identified but not represented in table
  - Schema E breach: Conflict Description is vague ("might conflict") rather than specific

────────────────
VOCABULARY CONTRACT
────────────────

Sentinel tokens:
  ??   Open obligation — unknown or not yet resolved; requires resolution before gate
  --   Closed decision — deliberately absent; inapplicability has been established

Violation taxonomy (typed, categorized):

  VOCABULARY VIOLATIONS:
    V-1: Cell left blank when ?? is correct (obligation not acknowledged)
    V-2: Cell left blank when -- is correct (inapplicability not declared)
    V-3: ?? used for a row where inapplicability is already established (wrong token)

  INTEGER-ENFORCEMENT GATE FAILURES:
    I-1: Writing "a few", "several", "some", or any non-integer artifact count
    I-2: Writing "many", "multiple", "various" in place of an integer count

  SCHEMA CONTRACT BREACHES:
    S-1: Column added to any schema table not declared in Phase -1
    S-2: Column removed or renamed from a schema table
    S-3: Mandatory cell left blank in any schema table
    S-4: Invalid vocabulary in a controlled-vocabulary column

  BANNED FORMS VIOLATIONS:
    B-1: "no change needed" in any justification cell
    B-2: "already covered" in any justification cell
    B-3: "clearly warranted" in any justification cell
    B-4: "minor adjustment" | "seems reasonable" | "minor update" in any justification cell

EXIT — Gate -1 (Schema Gate):
  All five schemas must be declared above.
  Every schema must list its Breach Conditions block.
  The Vocabulary Contract must include the typed violation taxonomy.
  Do not advance to Phase 0 without passing Gate -1.

────────────────────────────────────────
PHASE 0 — READ STRATEGY.MD
────────────────────────────────────────

ENTRY: All schemas are declared. No artifacts have been read.

JOB:
  Read strategy.md.
  Produce Schema A (Strategy Summary table).

EXIT — Gate 0:
  Schema A must have all four mandatory rows.
  Strategy Date must be an exact date.
  No blank cells.
  Do not advance to Phase 1 without passing Gate 0.

────────────────────────────────────────
PHASE 1 — SIGNAL INVENTORY
────────────────────────────────────────

ENTRY: Schema A is complete. Strategy date is known.

JOB:
  Scan all 9 namespace directories.
  Produce Schema B (Signal Inventory table).
  Sort rows: NEW artifacts first within each namespace, then PRIOR.

EXIT — Gate 1:
  All 9 namespace rows present.
  No blank cells (use ?? or --).
  Classification column uses only valid vocabulary.
  Do not advance to Phase 2 without passing Gate 1.

────────────────────────────────────────
PHASE 2 — DELTA QUANTIFICATION
────────────────────────────────────────

ENTRY: Schema B is complete.

JOB:
  Count NEW artifacts and PRIOR artifacts from Schema B.
  Produce mandatory delta sentence:
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be exact integers. Writing non-integer values is violation I-1.

EXIT — Gate 2:
  Delta sentence present with integer counts.
  Do not advance to Phase 3 without passing Gate 2.

────────────────────────────────────────
PHASE 3 — CHANGE PROPOSALS
────────────────────────────────────────

ENTRY: Delta sentence complete. NEW artifacts identified.

JOB:
  For each NEW artifact, assess whether it warrants a change to strategy.md.
  Produce Schema C (Proposal Table) for proposals that exist.

  CELL-LEVEL CHECK (WS-2): Before writing each Inertia Justification cell,
    check the cell against BANNED FORMS violations B-1 through B-4.
    Any match disqualifies the row. Resolve before presenting.

  For each absent change type, produce Schema D (Null Declaration Table).

  CELL-LEVEL CHECK: Before writing each Null Declaration Reason cell,
    check the cell against BANNED FORMS violations B-1 through B-4.
    Banned forms apply to null declaration cells equally.

EXIT — Gate 3:
  All three change types either have proposal rows (Schema C) or null declarations (Schema D).
  All Inertia Justification cells have been checked against banned forms.
  No blank cells in Schema C or Schema D.
  Do not advance to Phase 4 without passing Gate 3.

────────────────────────────────────────
PHASE 4 — CONFLICT DETECTION
────────────────────────────────────────

ENTRY: Proposal and null declaration tables are complete.

JOB:
  Audit Schema C rows for cross-proposal contradictions.
  Produce Schema E (Conflict Detection Table) or null form.

EXIT — Gate 4:
  Conflict detection must be explicitly resolved.
  Do not advance to Phase 5 without passing Gate 4.

────────────────────────────────────────
PHASE 5 — CONFIRMATION GATE
────────────────────────────────────────

ENTRY: All tables complete. All gates passed.

JOB:
  Present Schema A through Schema E in sequence.
  Present the delta sentence.

  Display gate:

  ┌──────────────────────────────────────────────┐
  │  STRATEGY UPDATE GATE                        │
  │  strategy.md has NOT been modified.          │
  │  YES — apply all proposals                   │
  │  NO  — discard all proposals                 │
  │  REVISED — specify changes to proposals      │
  └──────────────────────────────────────────────┘

  Do not proceed without user response.

────────────────────────────────────────
PHASE 6 — APPLY UPDATES
────────────────────────────────────────

On YES or REVISED: write confirmed proposals to strategy.md. Report count.
On NO: "No changes applied." End skill.
```

---

## V-04 — Phrasing Register (Formal Modal Obligations)

**Axis**: Phrasing register — modal obligation language (SHALL / SHALL NOT / MUST / MUST NOT) at all constraint sites, making advisory vs. mandatory guidance lexically distinguishable at four distinct constraint categories: gate conditions, mandatory column declarations, cell-level check instructions, and null-declaration enforcement.

**Hypothesis**: Modal verb forms create a lexically distinguishable constraint tier. A constraint that uses "do not" is advisory-sounding; one that uses SHALL NOT is obligatory-sounding. This distinction survives paraphrase and enables automated compliance checking.

---

```
SKILL: topic:plan
PURPOSE: Revise the signal strategy as new information arrives. Read
strategy.md and all gathered signals. Identify what has changed.
Propose typed changes. Receive user confirmation. Apply updates.

────────────────────────────────────────
VOCABULARY CONTRACT
────────────────────────────────────────

Sentinel tokens:
  ??   Open obligation (unknown; MUST be resolved before gate passage)
  --   Closed decision (deliberately absent; inapplicability SHALL be established before use)

Banned forms — the following phrases SHALL NOT appear in any justification or
  reason cell in this skill:
    "no change needed" | "already covered" | "clearly warranted"
    "minor adjustment" | "seems reasonable" | "minor update"
  These forms MUST be checked at the point of production, not post-review.
  Any cell containing a banned form SHALL be treated as a gate failure.

Integer enforcement: artifact counts SHALL be exact integers.
  The following forms SHALL NOT be used in place of integer counts:
    "a few" | "several" | "some" | "many" | "multiple" | "various"
  Use of any of these forms in a count position SHALL be treated as a gate failure.

Null declaration rule: silence is NOT a null declaration. Each absent change
  type SHALL be explicitly declared using the typed form [TYPE] — NULL.
  A skill output that omits a null declaration for an absent type SHALL be
  treated as a behavioral violation.

────────────────────────────────────────
PHASE 1 — READ STRATEGY.MD
────────────────────────────────────────

The skill SHALL begin by reading strategy.md.

The following items SHALL be extracted and recorded:
  - Strategy file date (SHALL be cited exactly as it appears, not paraphrased)
  - Active topics under coverage
  - Namespace priorities as stated in the strategy
  - Named gaps, unknowns, or deferred decisions

Output format: a STRATEGY SUMMARY block with these four items.
  Any item that cannot be determined from the file SHALL be recorded as ??.
  Cells SHALL NOT be left blank.

GATE 1 (mandatory):
  The STRATEGY SUMMARY block MUST be complete before proceeding.
  All four items MUST be present with a value, ??, or --.
  The skill SHALL NOT advance to Phase 2 without passing Gate 1.

────────────────────────────────────────
PHASE 2 — SIGNAL INVENTORY
────────────────────────────────────────

The skill SHALL scan all signal artifacts across all 9 namespaces:
  scout / draft / review / flow / trace / prove / listen / program / topic

For each namespace, the skill SHALL produce one inventory row:

  | Namespace | Artifact Filenames | Artifact Dates | Classification |

Classification values: NEW (after strategy date) / PRIOR (on or before) / ??

The following rules SHALL apply:
  - Every namespace SHALL have a row. An absent namespace row is a gate failure.
  - A namespace with no artifacts SHALL receive: filenames = --, dates = --, classification = --
  - Artifact filenames SHALL be the actual filenames. Descriptions SHALL NOT
      appear in the filenames column.
  - Cells SHALL NOT be left blank. ?? or -- MUST be used for unknown or absent values.

Sort order: NEW artifacts SHALL appear before PRIOR artifacts within each namespace.

GATE 2 (mandatory):
  All 9 namespace rows MUST be present.
  Classification column MUST use only NEW, PRIOR, ??, or -- values.
  The skill SHALL NOT advance to Phase 3 without passing Gate 2.

────────────────────────────────────────
PHASE 3 — DELTA QUANTIFICATION
────────────────────────────────────────

The skill SHALL extract the NEW artifact list and PRIOR artifact list from Phase 2.

The following delta sentence SHALL be produced, with exact integer values:
  "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."

The following forms SHALL NOT appear in N or M positions:
  "a few" | "several" | "some" | "many" | "multiple" | "various"

Only NEW artifacts SHALL be used as evidence in Phase 4 proposals.
PRIOR artifacts SHALL NOT appear as evidence in any proposal row.

GATE 3 (mandatory):
  The delta sentence MUST be present.
  N and M MUST be exact integers.
  The skill SHALL NOT advance to Phase 4 without passing Gate 3.

────────────────────────────────────────
PHASE 4 — CHANGE PROPOSALS
────────────────────────────────────────

For each NEW artifact, the skill SHALL assess whether a change to strategy.md
is warranted.

The following proposal table SHALL be produced for non-null proposals:

  | Change Type | Proposal Description | Evidence Artifact | Before | After | Inertia Justification |

The following rules SHALL apply to the proposal table:
  - Change Type SHALL be one of: ADD / REMOVE / REPRIORITIZE
  - Evidence Artifact SHALL be the exact filename of the NEW artifact. It SHALL NOT
      be a description, summary, or paraphrase.
  - Inertia Justification is a mandatory column. It SHALL NOT be left blank.
  - Before and After SHALL both be present for every non-null proposal row.

CELL-LEVEL CHECK (mandatory, point-of-production):
  Before writing each Inertia Justification cell, the skill SHALL check the
    cell against the BANNED FORMS list in the Vocabulary Contract.
  Any cell matching a banned form SHALL NOT be written. The cell MUST be
    rewritten before the row is presented.
  This check SHALL apply to null declaration reason cells equally.

NULL DECLARATIONS (mandatory for each absent change type):
  If no ADD proposals exist, the skill SHALL produce:
    "ADD — NULL. [Reason why no new coverage dimension was identified.]"
  If no REMOVE proposals exist, the skill SHALL produce:
    "REMOVE — NULL. [Reason why no obsolete coverage dimension was identified.]"
  If no REPRIORITIZE proposals exist, the skill SHALL produce:
    "REPRIORITIZE — NULL. [Reason why no priority shift was identified.]"

  Silence SHALL NOT serve as a null declaration.
  Null declaration reason cells SHALL be subject to the same banned-forms check.

GATE 4 (mandatory):
  All three change types MUST be either represented by proposal rows or by
    explicit typed null declarations.
  All Inertia Justification cells MUST have passed the cell-level banned-forms check.
  The skill SHALL NOT advance to Phase 5 without passing Gate 4.

────────────────────────────────────────
PHASE 5 — CONFLICT DETECTION
────────────────────────────────────────

The skill SHALL audit all proposal rows for cross-artifact contradictions.

If conflicts are found: each conflict SHALL be named with the row numbers of
  the conflicting proposals.

If no conflicts are found: the skill SHALL produce:
  "CONFLICT DETECTION — NULL. No contradictions identified across [N] proposals."

The skill SHALL NOT present proposals to the user without completing conflict detection.

────────────────────────────────────────
PHASE 6 — CONFIRMATION GATE
────────────────────────────────────────

The skill SHALL present the full proposal set including the delta sentence,
proposal table, null declarations, and conflict detection result.

The following gate SHALL be displayed:

  ┌──────────────────────────────────────────────────────────┐
  │  STRATEGY UPDATE GATE                                    │
  │                                                          │
  │  strategy.md has NOT been modified.                      │
  │                                                          │
  │  This gate SHALL NOT pass without your explicit input.   │
  │  The skill SHALL NOT modify strategy.md until you        │
  │  provide one of the following responses:                 │
  │                                                          │
  │    YES     — apply all proposals as shown                │
  │    NO      — discard all proposals, no change            │
  │    REVISED — specify which proposals to modify           │
  └──────────────────────────────────────────────────────────┘

The skill SHALL NOT proceed past this gate.
strategy.md SHALL NOT be written until the user responds.
Proceeding without a response SHALL be treated as a gate failure.

────────────────────────────────────────
PHASE 7 — APPLY UPDATES
────────────────────────────────────────

On YES or REVISED: confirmed proposals SHALL be applied to strategy.md.
  The skill SHALL report: "strategy.md updated. [N] proposals applied."
  N SHALL be an exact integer.

On NO: the skill SHALL report: "No changes applied." Skill ends.

strategy.md SHALL NOT be written more than once.
```

---

## V-05 — Combined (Inertia-first + Table-heavy + Modal + Three-path Audit)

**Axes combined**: Inertia framing + Output format + Phrasing register + Three-path audit declaration.

**Hypothesis**: Combining the defense register (inertia framing), pre-declared named schemas (table-heavy), modal obligation language, and an explicit three-path audit declaration creates a self-auditing skill structure where three independent completeness checks (Schema Spine, Write-Surface Spine, Lifecycle Slots) can confirm correctness without reading phase content.

---

```
SKILL: topic:plan
PURPOSE: Revise the signal strategy as new information arrives. The strategy
is presumed correct until a new artifact defeats a pre-committed defense.
This skill is a structured adversarial process: the defense register is
committed before any artifact is read; every proposal must defeat a named row.

────────────────────────────────────────
THREE-PATH AUDIT DECLARATION
────────────────────────────────────────

This skill is independently auditable by three paths. Each path is complete
without consulting the others:

  PATH 1 — SCHEMA SPINE
    Scan TABLE SCHEMAS section headers (Phase -1) to verify that all
    five named schemas (A through E) are declared with Breach Conditions.
    A missing schema header indicates an undeclared output structure.

  PATH 2 — WRITE-SURFACE SPINE
    Scan WS block section headers (WS-1, WS-2, WS-3) to verify that all
    three point-of-production enforcement blocks are present as standalone sections.
    A missing WS header indicates an unenforced write surface.

  PATH 3 — LIFECYCLE SLOTS
    Scan EXIT slots in each phase to verify that every phase has a named,
    numbered gate as its EXIT condition.
    An EXIT slot without a gate number indicates an unguarded phase boundary.

Audit commitment: a skill that satisfies all three paths is structurally complete.
A skill that satisfies any two paths is structurally incomplete.

────────────────────────────────────────
WRITE-SURFACE REGISTER
────────────────────────────────────────

(Positioned before Phase -1. This register SHALL be complete before any phase begins.)

  | WS ID | Surface Name           | Type              | Trigger Condition                          |
  |-------|------------------------|-------------------|--------------------------------------------|
  | WS-1  | Defense Register       | Read barrier      | Before any artifact read (Gate 0 precondition) |
  | WS-2  | Proposal justification | Cell-level check  | Before writing each Inertia Justification cell |
  | WS-3  | Null declaration reason| Cell-level check  | Before writing each Null Declaration Reason cell |

Each WS block SHALL appear as a standalone section header in the skill structure.
Having a WS block embedded as a bullet without a section header SHALL NOT satisfy
this register, even if the check instruction fires at the correct site.

────────────────────────────────────────
PHASE -1 — TABLE SCHEMAS
────────────────────────────────────────

ENTRY: No files have been read. No tables have been produced.
  The Write-Surface Register above MUST be complete before this phase begins.

JOB: Declare all table schemas. Every table produced by this skill SHALL conform
  to one of these named schemas. Producing a table with unlisted columns is a
  Schema Spine contract breach.

────────────────
Schema A — Strategy Summary
────────────────
Columns: [Item] | [Value]
Mandatory rows: Strategy Date, Active Topics, Namespace Priorities, Named Gaps
Sentinel: ?? for unknown; no -- (all rows are required)
BREACH CONDITIONS (Schema A):
  - Any mandatory row absent
  - Value cell blank (SHALL use ?? if unknown)
  - Strategy Date not an exact date

────────────────
Schema B — Defense Register
────────────────
Columns: [Row #] | [Dimension] | [Current Strategy Position] | [Defense Argument]
Mandatory: one row per coverage dimension addressed by the strategy
Sentinel: ?? only in Defense Argument if no argument can be identified
BREACH CONDITIONS (Schema B):
  - Any row missing a Row # (rows MUST be numbered sequentially for citation)
  - Defense Argument blank (SHALL use the acknowledged-gap form if truly absent)
  - Defense Argument containing a banned form

CROSS-SCHEMA DEPENDENCY (declared here, not at use site):
  Schema D (Proposal Table) references Schema B row numbers in the
  "Defense Defeated (Row #)" column. The Row # column in Schema B is the
  primary key for that cross-schema reference. Schema B rows MUST be numbered
  before Schema D can be opened. Schema D's dependency on Schema B Row #
  is declared here and SHALL be labeled "inherited from Phase -1 declaration,
  not invented here" at every Schema D use site.

────────────────
Schema C — Signal Inventory
────────────────
Columns: [Namespace] | [Artifact Filenames] | [Artifact Dates] | [Classification] | [Defense Row Implicated]
Mandatory rows: 9 (one per namespace: scout, draft, review, flow, trace, prove, listen, program, topic)
Classification vocabulary: NEW | PRIOR | ??
Defense Row Implicated: Schema B row number(s) this artifact implicates
Sort order: NEW rows MUST appear before PRIOR rows within each namespace
Sentinel: -- for namespaces with no artifacts; ?? when row implication is unknown
BREACH CONDITIONS (Schema C):
  - Fewer than 9 namespace rows
  - Classification value outside allowed vocabulary
  - Artifact filename is a description rather than a filename
  - Defense Row Implicated is blank for a NEW artifact
  - Sort order violation (PRIOR row before NEW row in same namespace)

CROSS-SCHEMA DEPENDENCY (inherited from Phase -1 declaration, not invented here):
  Defense Row Implicated references Schema B Row # column.

────────────────
Schema D — Proposal Table
────────────────
Columns: [#] | [Change Type] | [Proposal Description] | [Evidence Artifact]
         | [Before] | [After] | [Defense Defeated (Row #)] | [Defeat Argument]
Change Type vocabulary: ADD | REMOVE | REPRIORITIZE
Evidence Artifact: exact filename from NEW artifacts only (PRIOR filenames SHALL NOT appear)
Defense Defeated (Row #): mandatory column — Schema B row number defeated by this proposal
  (a named defense without a row number SHALL NOT satisfy this criterion)
Defeat Argument: the specific claim from the NEW artifact overriding the defense argument
Sentinel: ?? in Defense Defeated if row cannot be identified (flags a weak proposal)
BREACH CONDITIONS (Schema D):
  - Change Type outside allowed vocabulary
  - Evidence Artifact is a PRIOR artifact
  - Defense Defeated (Row #) blank or containing text rather than an integer row reference
  - Defeat Argument cell containing a banned form
  - Any column absent or renamed

CROSS-SCHEMA DEPENDENCY (inherited from Phase -1 declaration, not invented here):
  Defense Defeated (Row #) references Schema B Row # column.

────────────────
Schema E — Null Declaration Table
────────────────
Columns: [Change Type] | [Declaration] | [Reason] | [Defense Rows Consulted]
Mandatory rows: one row per change type absent from Schema D
Declaration vocabulary: [TYPE] — NULL
Defense Rows Consulted: comma-separated Schema B row numbers evaluated and found undefeated
BREACH CONDITIONS (Schema E):
  - Absent change type not represented (silence SHALL NOT serve as a null declaration)
  - Reason cell blank or containing a banned form
  - Defense Rows Consulted blank (null declarations MUST name the rows they evaluated)
  - Declaration value deviating from the [TYPE] — NULL pattern

CROSS-SCHEMA DEPENDENCY (inherited from Phase -1 declaration, not invented here):
  Defense Rows Consulted references Schema B Row # column.

────────────────
VOCABULARY CONTRACT
────────────────

Sentinel tokens:
  ??   Open obligation — unknown; MUST be resolved before gate passage
  --   Closed decision — deliberately absent; inapplicability SHALL be established before use

Violation taxonomy (typed, categorized):

  VOCABULARY VIOLATIONS:
    V-1: Cell left blank when ?? is correct (open obligation not acknowledged)
    V-2: Cell left blank when -- is correct (closed decision not declared)
    V-3: ?? used where inapplicability is already established (wrong token class)

  INTEGER-ENFORCEMENT GATE FAILURES:
    I-1: "a few" | "several" | "some" in any count position
    I-2: "many" | "multiple" | "various" in any count position
    (Any non-integer value in a count position SHALL be treated as type I-1)

  SCHEMA CONTRACT BREACHES:
    S-1: Column added to a schema table not declared in Phase -1
    S-2: Column removed or renamed from a declared schema
    S-3: Mandatory cell left blank in any schema table
    S-4: Invalid controlled-vocabulary value in a classification column
    S-5: PRIOR artifact cited as Evidence Artifact in Schema D

  BANNED FORMS VIOLATIONS:
    B-1: "no change needed" in any justification or reason cell
    B-2: "already covered" in any justification or reason cell
    B-3: "clearly warranted" in any justification or reason cell
    B-4: "minor adjustment" | "seems reasonable" | "minor update" in any cell
    (Banned forms SHALL apply to null declaration reason cells; null declarations
     are not exempt from this constraint)

EXIT — Gate -1 (Schema Gate, linked to Gate 0):
  All five schemas (A through E) MUST be declared with named Breach Conditions.
  The Vocabulary Contract MUST include the typed violation taxonomy with category labels.
  All cross-schema dependencies MUST be declared at Phase -1, not at use sites.
  The Write-Surface Register MUST be complete before this gate passes.
  The skill SHALL NOT advance to Phase 0 without passing Gate -1.
  Gate -1 MUST pass before Gate 0 can open. These gates are sequentially linked.

────────────────────────────────────────
WS-1 — READ BARRIER (Write-Surface 1, Register Row 1)
────────────────────────────────────────

WS-1 MILESTONE: The defense register (Schema B) SHALL be fully committed before
  any signal artifact is read. This is a hard read barrier.
  Reading any artifact before Schema B is complete and gate-checked is a
  WS-1 violation, regardless of whether the artifact is NEW or PRIOR.
  WS-1 fulfills Write-Surface Register Row 1.

────────────────────────────────────────
PHASE 0 — PRE-SIGNAL DEFENSE REGISTER
────────────────────────────────────────

ENTRY: Gate -1 has passed. No signal artifacts have been read. WS-1 is active.

JOB:
  Read strategy.md.
  Produce Schema A (Strategy Summary).
  Extract the strategy date for use as classification baseline.

  Commit Schema B (Defense Register) before reading any other file.
    One row per coverage dimension the strategy addresses.
    Defense Argument: the strongest case the current strategy makes for no change.
      Write it as the strategy speaking in its own defense.
      If no defense argument can be formed: "No defense committed — this dimension
        is already acknowledged as a gap in the strategy."
    Row numbers MUST be assigned sequentially (1, 2, 3...) — Schema D depends on them.

EXIT — Gate 0 (linked from Gate -1, links to Gate 1):
  Schema A MUST be complete (all four mandatory rows).
  Schema B MUST be complete (all rows numbered, no blank cells).
  The read barrier (WS-1) is lifted only after Gate 0 passes.
  The skill SHALL NOT advance to Phase 1 and SHALL NOT read any signal artifact
    until Gate 0 passes.
  Do not advance to Phase 1 without passing Gate 0.

────────────────────────────────────────
PHASE 1 — SIGNAL INVENTORY
────────────────────────────────────────

ENTRY: Gate 0 has passed. Read barrier lifted. Strategy date known. Schema B complete.

JOB:
  Scan all 9 namespace directories for signal artifacts.
  Produce Schema C (Signal Inventory).
    Sort: NEW rows before PRIOR rows within each namespace.
    Defense Row Implicated: cite Schema B row number(s). Blank is a Schema C breach.

  Produce mandatory delta sentence (integer values only — I-1/I-2 violations apply):
    "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."

EXIT — Gate 1 (links to Gate 2):
  Schema C MUST have all 9 namespace rows.
  Defense Row Implicated MUST be filled for all NEW artifact rows.
  Delta sentence MUST be present with integer N and M.
  Do not advance to Phase 2 without passing Gate 1.

────────────────────────────────────────
WS-2 — PROPOSAL CELL CHECK (Write-Surface 2, Register Row 2)
────────────────────────────────────────

WS-2 MILESTONE: Before writing each Inertia Justification cell in Schema D,
  the skill SHALL check the cell content against banned forms B-1 through B-4.
  Any match SHALL cause the cell to be rewritten before the row is presented.
  This check is a point-of-production obligation, not a post-review step.
  WS-2 fulfills Write-Surface Register Row 2.

────────────────────────────────────────
PHASE 2 — CHANGE PROPOSALS
────────────────────────────────────────

ENTRY: Gate 1 has passed. NEW artifacts identified. Schema C complete. WS-2 active.

JOB:
  For each NEW artifact, assess whether a change to strategy.md is warranted.
  Produce Schema D (Proposal Table) for non-null proposals.

  Defense Defeated (Row #): cite the Schema B row number defeated by this proposal.
    This column is mandatory. (Cross-schema dependency: inherited from Phase -1
    declaration, not invented here.)
    A named defense without a row number SHALL NOT satisfy this criterion.

  Defeat Argument: the specific claim from the NEW artifact overriding the
    defense argument. Quote or cite specifically.

  [WS-2 fires here: check each Inertia Justification cell before writing.]

EXIT — Gate 2 (links to Gate 3):
  Every non-null Schema D row MUST have an integer value in Defense Defeated (Row #).
  Every Inertia Justification cell MUST have passed WS-2.
  Do not advance to Phase 3 without passing Gate 2.

────────────────────────────────────────
WS-3 — NULL DECLARATION CELL CHECK (Write-Surface 3, Register Row 3)
────────────────────────────────────────

WS-3 MILESTONE: Before writing each Reason cell in Schema E (Null Declaration Table),
  the skill SHALL check the cell against banned forms B-1 through B-4.
  Null declarations are NOT exempt from banned forms constraints.
  Any match SHALL cause the cell to be rewritten before the row is presented.
  WS-3 fulfills Write-Surface Register Row 3.

────────────────────────────────────────
PHASE 3 — NULL DECLARATIONS
────────────────────────────────────────

ENTRY: Gate 2 has passed. Proposal table complete. WS-3 active.

JOB:
  For each change type absent from Schema D, produce a Schema E row.
  [WS-3 fires here: check each Reason cell before writing.]
  Defense Rows Consulted: name the Schema B rows evaluated and found undefeated.
    (Cross-schema dependency: inherited from Phase -1 declaration, not invented here.)

EXIT — Gate 3 (links to Gate 4):
  Every absent change type MUST have a Schema E row.
  Every Reason cell MUST have passed WS-3.
  Defense Rows Consulted MUST be populated for all Schema E rows.
  Do not advance to Phase 4 without passing Gate 3.

────────────────────────────────────────
PHASE 4 — CONFLICT DETECTION
────────────────────────────────────────

ENTRY: Gate 3 has passed. All proposals and null declarations complete.

JOB:
  Audit all Schema D rows for cross-proposal contradictions.
  If conflicts found: produce Schema-E-style conflict rows with proposal row numbers.
  If no conflicts: produce "CONFLICT DETECTION — NULL. [N] proposals checked."
  N MUST be an exact integer.

EXIT — Gate 4 (links to Gate 5):
  Conflict detection MUST be explicitly resolved (list or null form).
  Do not advance to Phase 5 without passing Gate 4.

────────────────────────────────────────
PHASE 5 — CONFIRMATION GATE
────────────────────────────────────────

ENTRY: Gate 4 has passed. All schemas complete.

JOB:
  Present schemas A through E in order with the delta sentence.

  ┌────────────────────────────────────────────────────────────────┐
  │  STRATEGY UPDATE GATE                                          │
  │                                                                │
  │  strategy.md has NOT been modified.                            │
  │                                                                │
  │  [N] proposals generated. [M] defense rows defeated.          │
  │  [K] defense rows consulted and held (no change warranted).   │
  │                                                                │
  │  This gate SHALL NOT pass without explicit user response.      │
  │  strategy.md SHALL NOT be written until you respond:           │
  │                                                                │
  │    YES     — apply all proposals as shown                      │
  │    NO      — discard all proposals                             │
  │    REVISED — specify which proposals to modify                 │
  └────────────────────────────────────────────────────────────────┘

  The skill SHALL NOT proceed. strategy.md SHALL NOT be written.
  Proceeding without a response SHALL be treated as a gate failure.

EXIT — Gate 5:
  This gate MUST NOT pass automatically.
  User MUST provide YES, NO, or REVISED.

────────────────────────────────────────
PHASE 6 — APPLY UPDATES
────────────────────────────────────────

ENTRY: User has responded YES or REVISED. Gate 5 has passed.

JOB:
  On YES: apply all Schema D proposals to strategy.md.
  On REVISED: apply only confirmed proposals.
  On NO: report "No changes applied." Skill ends.

  Report: "strategy.md updated. [N] proposals applied." N MUST be an exact integer.

EXIT:
  strategy.md is saved.
  Proposal count is reported.
  Skill complete.
```

---

## Variation Summary

| Variation | Primary Axis | Key Rubric Targets | Distinguishing Move |
|-----------|-------------|-------------------|---------------------|
| V-01 | Lifecycle emphasis | C-12, C-20, C-31 | ENTRY/JOB/EXIT per phase; gates as EXIT slot content |
| V-02 | Inertia framing | C-18, C-22, C-08 | Defense register as Phase 0; row# citations required in proposals |
| V-03 | Output format (table-dominant) | C-35, C-36, C-37, C-40 | Phase -1 with 5 named schemas + typed violation taxonomy with category labels |
| V-04 | Phrasing register (modal) | C-39, C-16, C-23, C-24 | SHALL/MUST/SHALL NOT at all constraint sites; 4+ distinct modal sites |
| V-05 | Combined (all four + three-path audit) | C-40, C-41, C-42, C-29, C-30 | Three-path audit declaration; cross-schema dependency at Phase -1; WS register with milestone linkage |
