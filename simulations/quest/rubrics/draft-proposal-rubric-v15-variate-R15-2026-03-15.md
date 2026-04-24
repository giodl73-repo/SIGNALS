# draft-proposal Variate — Round 15

Rubric version: v15 · Formula: /32 · New criterion: C-39 (amendment table T-37 trigger entry
includes correct-format prescription alongside the inline failure exemplar — two-part T-37
CONDITION structure: Part 1 quotes the failure construct that fires T-37; Part 2 prescribes the
correct per-column attribution format that satisfies C-37)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Role sequence (Architect-first) — designed fail: C-39 only
  (C-37 PASS: Domain 2 per-column attribution present; C-38 PASS: T-37 CONDITION carries Part 1
  inline failure exemplar; C-39 FAIL: Part 2 correct-format prescription absent — isolates C-39
  against a fully-compliant Phase 9b and a C-38-passing T-37 CONDITION entry)
- **V-02**: Output format (compact tables, PM-first) — designed fail: C-37 only
  (C-38 PASS and C-39 PASS: T-37 CONDITION carries the full two-part structure; C-37 FAIL:
  Domain 2 row-level only — reference exemplar for C-38+C-39 double-pass when T-37 fires)
- **V-03**: Lifecycle emphasis (stale trigger count: 38 rows, v14 table carried forward) —
  designed fails: C-24 + C-38 independent fail + C-39 cascade
  (T-39 absent from stale table; T-37 CONDITION abstract — no exemplar, no prescription; C-38
  fails independently; C-39 fails by cascade; named findings: T-24, T-38)
- **V-04**: Phrasing register (conversational) + Role sequence combination —
  designed fails: C-25 + C-33; C-38 PASS and C-39 PASS via two-part T-37 CONDITION in
  conversational style
  (C-36 PASS, C-37 PASS: both depth criteria satisfied in conversational register; 39-row table;
  T-25 and T-33 fire; T-38 and T-39 silent)
- **V-05**: Inertia framing + C-36 + C-37 + C-38 + C-39 quad fail —
  designed fails: C-36 + C-37 + C-38 + C-39; all four depth/exemplar criteria fail
  simultaneously
  (C-24 PASS: 39-row table; T-37 CONDITION abstract; Domain 1 no P*I compound scores; Domain 2
  row-level only; four open triggers: T-36, T-37, T-38, T-39)

Predicted scores: V-01 -> 99.69 · V-02 -> 99.69 · V-03 -> 99.06 · V-04 -> 99.38 · V-05 -> 98.75

---

## V-01 -- Architect-First | Axis: Role Sequence | Designed fail: C-39

**Hypothesis**: An Architect-led variation with complete Phase 9b structural compliance --
dual-domain enumeration (C-32 PASS), domain-index prefixes (C-34 PASS), per-site arrow notation
(C-35 PASS), P*I compound scores in Domain 1 transitions (C-36 PASS), and per-option-column
Domain 2 attribution (C-37 PASS) -- and the T-37 CONDITION entry carrying the inline failure
exemplar (Part 1, C-38 PASS) but stopping there, omitting the correct-format prescription
(Part 2). C-39 FAIL. T-39 fires at FINALIZATION. T-38 is silent (exemplar present). One open
trigger: T-39. Finding 1: T-39. 39-row amendment table (C-24 PASS). CLOSED BY column present
(C-22 PASS). Prohibition adjacent to placeholder (C-33 PASS). Numbered 4-step finalization
(C-25 PASS). Score: 31/32 -> 99.69.

```
ROLE SEQUENCE: Architect -> PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Owns option framing, technical risk assessment, register construction, Phase 9b
  back-fill, gate audit, and feasibility validation.
- PM: Owns business trade-off commentary, adoption risk factors, and recommendation rationale.

---

PHASE 0 -- PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect -> PM) as a typed header at the top of the
output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-39 -- one per v15 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires (PRE-DOCUMENT,
PRE-OPTION, FINALIZATION, or a named phase). Leave STATUS = PENDING for all rows at init.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

Architect: State the shared problem being decided. This PROBLEM field is shared by all options
and must appear verbatim in every option entry.

Include:
  PROBLEM: [shared problem statement]
  TEMPORAL ANCHOR: [specific named date, sprint, or event by which a decision is required]
  INACTION CONSEQUENCE: [concrete named outcome if no option is selected by the anchor]

PM: Confirm the problem statement captures business context and urgency.

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

Compose at least 3 options. One must be a do-nothing or status-quo option, explicitly labeled
as such. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement -- repeat verbatim from Phase 1]
  RISK: Do not compute P*I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot for Phase 9b back-fill. Note risk category only (adoption barrier /
        schedule risk / technical coupling). PM notes business risk category; Architect
        notes technical risk category.
  RATIONALE: [why this option is a candidate]

---

PHASE 3 -- RISK REGISTER [GATE: R-01]

Architect: Build the risk register:
  R-NN | RISK | P | I | P*I | MITIGATION

At least 3 technical risk entries. P and I on a 1-5 scale. Compute P*I per entry.
PM: Add at least one adoption or schedule risk entry.

Include project-specific scoring anchors before any entries are scored:
  P=1: [what low probability means for this project context]
  P=3: [what medium probability means for this project context]
  P=5: [what near-certain probability means for this project context]
  I=1: [what low impact means for this project context]
  I=3: [what medium impact means for this project context]
  I=5: [what critical impact means for this project context]

---

PHASE 9b -- RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs from the register into each option RISK field, replacing [R-NN pending].
Update the comparison matrix risk column.

Enumerate citation sites by structural domain:

  Domain 1 -- Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] -> [R-03 (P:n * I:n = n), R-07 (P:n * I:n = n)]
    [OPTION-B label] RISK field: [R-NN pending] -> [R-01 (P:n * I:n = n), R-04 (P:n * I:n = n)]
    [do-nothing label] RISK field: [R-NN pending] -> [R-02 (P:n * I:n = n)]

  Domain 2 -- Comparison matrix risk column:
    Risk row: [OPTION-A column: R-NN IDs] | [OPTION-B column: R-NN IDs] |
              [do-nothing column: R-NN IDs]

Include P*I compound scores from the register in each Domain 1 transition target.
Attribute specific R-NN IDs to each option's column in Domain 2.

---

PHASE 4 -- COMPARISON MATRIX [GATE: E-03]

Architect: Build a comparison matrix with OPTIONS as column headers.
Rows: Effort, Technical risk score (R-NN cited), Reversibility, Time-to-value.
PM: Add Adoption friction and Business value rows.

---

PHASE 5 -- GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN] citation.
List any missing citations. Update amendment table for any T-NN that fires.

---

PHASE 6 -- COVERAGE TABLE [GATE: C-22]

Build a coverage table:
  CRITERION | STATUS | CLOSED BY

Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-39.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 7 -- PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing present, risk register >= 3 entries, Phase 9b complete,
assumption register >= 2 entries, both registers precede recommendation in document sequence.

---

PHASE 9 -- RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide rationale referencing at least two comparison matrix
dimensions. State qualifying conditions (at least 2 circumstances under which the
recommendation changes).
Architect: Confirm technical feasibility.

---

PHASE 10 -- FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN -- [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."
  Enumerate sequentially (Finding 1, Finding 2, ...). One finding per trigger.

Step 2: Verify all E-tier criteria satisfied. Update coverage table for any failing criterion.

Step 3: Verify all R-tier criteria satisfied. Update coverage table for any failing criterion.

Step 4: Confirm coverage table is fully populated. Set COMPLETION STATUS of amendment table.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-39 -- exactly 39 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 39)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name option RISK fields
                               by option label AND comparison matrix risk column as two named
                               structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P*I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] -> [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P*I compound scores alongside R-NN IDs in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution -- row-level confirmation
                               "R-NN IDs applied to risk row" fires T-37)
  T-38 PHASE = FINALIZATION  (fires if T-37 CONDITION entry lacks an inline exemplar quoting
                               the exact document construct that fires T-37)
  T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION entry carries the inline failure
                               exemplar (Part 1, C-38) but omits the correct-format
                               prescription stating the expected per-option-column attribution
                               structure (Part 2, C-39))
```

---

## V-02 -- PM-First Compact | Axis: Output Format | Designed fail: C-37; C-38 PASS, C-39 PASS

**Hypothesis**: A compact PM-first variation will include full Domain 1 P*I transitions (C-36
PASS: each Domain 1 site shows `[R-NN pending] -> [R-03 (P:n * I:n = n), R-07 (P:n * I:n = n)]`)
but fail C-37 by confirming Domain 2 only at the row level: "Risk row: R-NN IDs applied to risk
row" -- no per-option-column attribution. The T-37 CONDITION entry in the amendment table spec
carries the full two-part structure: Part 1 quotes the exact firing construct ("row-level
confirmation 'R-NN IDs applied to risk row' fires T-37") and Part 2 prescribes the correct
replacement format ("per-column format required: [OPTION-A column: R-NN IDs] | [OPTION-B:
R-NN IDs]"). C-38 PASS, C-39 PASS. T-37 fires. T-38 and T-39 silent. One open trigger: T-37.
Finding 1: T-37. 39-row amendment table (C-24 PASS). CLOSED BY column present (C-22 PASS).
Prohibition adjacent to placeholder (C-33 PASS). Numbered 4-step finalization (C-25 PASS).
Score: 31/32 -> 99.69.

```
ROLE SEQUENCE: PM -> Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

OUTPUT FORMAT: Compact tables throughout. Minimize prose between tables.
Use concise cell values. Each phase produces a table or structured block, not paragraphs.

ROLE ASSIGNMENTS:
- PM: Leads business framing, option business cases, recommendation rationale, adoption risk.
- Architect: Validates technical constraints, owns risk register entries, confirms feasibility.

---

PHASE 0 -- PRE-DOCUMENT [GATE: E-01]

PM: Declare role sequence (PM -> Architect) as a typed header. Apply in every phase header.

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-39. Assign each trigger a PHASE value. All STATUS = PENDING at init.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PM: Compact problem block:
  PROBLEM: [shared problem for all options]
  DECISION REQUIRED: [what must be chosen]
  TEMPORAL ANCHOR: [specific named date, sprint, or event]
  INACTION CONSEQUENCE: [concrete named outcome of not deciding]

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

For each option (minimum 3, including do-nothing), produce a compact option block:

  OPTION: [label and brief description]
  PROBLEM: [shared problem -- repeat verbatim from Phase 1]
  RISK: Do not compute P*I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Note risk category only: adoption barrier / schedule risk / technical
        coupling. PM notes business risk category; Architect notes technical risk category.
  RATIONALE: [one-sentence: why this option is a candidate]

---

PHASE 3 -- RISK REGISTER [GATE: R-01]

Architect: Compact risk register table:
  R-NN | RISK | P | I | P*I | MITIGATION

At least 3 entries. P and I on 1-5 scale. P*I computed.
PM: Add 1-2 adoption or schedule risk entries.

---

PHASE 9b -- RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:

  Domain 1 -- Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] -> [R-03 (P:n * I:n = n), R-07 (P:n * I:n = n)]
    [OPTION-B label] RISK field: [R-NN pending] -> [R-01 (P:n * I:n = n), R-04 (P:n * I:n = n)]
    [do-nothing label] RISK field: [R-NN pending] -> [R-02 (P:n * I:n = n)]

  Domain 2 -- Comparison matrix risk column:
    Risk row: R-NN IDs applied to risk row. Confirm applicable register entries present.

---

PHASE 4 -- COMPARISON MATRIX [GATE: E-03]

Compact matrix -- OPTIONS as column headers.
Rows: Effort | Risk (R-NN cited) | Time-to-value | Reversibility | Adoption friction
PM leads dimension selection; Architect validates technical dimensions.

---

PHASE 5 -- GATE AUDIT [GATE: C-21]

Verify all phase headers carry [GATE: X-NN] citations. List any missing.
Update amendment table for any T-NN that fires.

---

PHASE 6 -- COVERAGE TABLE [GATE: C-22]

Coverage table columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-39.
STATUS = PASS or FAIL. CLOSED BY = phase that satisfied the criterion.
Include CLOSED BY column even in compact format for traceability.

---

PHASE 7 -- PREREQUISITES CHECK [GATE: R-02]

Confirm: options >= 3, do-nothing present, risk register entries >= 3, Phase 9b complete,
registers precede recommendation.

---

PHASE 9 -- RECOMMENDATION [GATE: E-04]

PM: Name the recommended option with business rationale citing two matrix dimensions.
State qualifying conditions.
Architect: Confirm technical feasibility.

---

PHASE 10 -- FINALIZATION [GATE: R-03]

Execute as an explicitly numbered four-step list:

Step 1: Review amendment table for STATUS = OPEN triggers.
  For each open trigger T-NN, produce:
    "Finding N: T-NN -- [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing]."
  Enumerate sequentially. One finding per trigger.

Step 2: Verify all E-tier criteria satisfied.
Step 3: Verify all R-tier criteria satisfied.
Step 4: Update coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-39, exactly 39 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 39)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name option RISK fields
                               by option label AND comparison matrix risk column as two named
                               structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P*I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] -> [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P*I compound scores in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution -- row-level confirmation
                               "R-NN IDs applied to risk row" fires T-37; per-column format
                               required: [OPTION-A column: R-NN IDs] | [OPTION-B: R-NN IDs])
  T-38 PHASE = FINALIZATION  (fires if T-37 CONDITION entry lacks an inline exemplar quoting
                               the exact document construct that fires T-37)
  T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION entry carries the inline failure
                               exemplar but omits the correct-format prescription stating the
                               expected per-option-column attribution structure)
```

---

## V-03 -- Stale Table (38 rows) | Axis: Lifecycle Emphasis | Designed fails: C-24 + C-38 independent + C-39 cascade

**Hypothesis**: A lifecycle-gate-heavy variation builds its amendment table from the v14 criterion
list (T-01..T-38, 38 rows). T-24 fires at PRE-DOCUMENT (38 != 39 required by v15). T-39 is
absent from the stale table and cannot fire as a named finding. The T-37 CONDITION entry carries
abstract text ("fires if Phase 9b Domain 2 does not carry per-option-column R-NN attribution")
without an inline failure exemplar -- C-38 fails independently (T-37 entry exists, exemplar
absent; independently testable from T-39's absence). C-39 fails by cascade from C-38 (abstract
entry contains neither Part 1 nor Part 2). Phase 9b is fully compliant with the depth criteria:
Domain 1 transitions include P*I compound scores (C-36 PASS), Domain 2 carries explicit
per-option-column attribution (C-37 PASS). CLOSED BY column present (C-22 PASS). Prohibition
adjacent to placeholder (C-33 PASS). Numbered 4-step finalization (C-25 PASS). Named findings:
Finding 1: T-24; Finding 2: T-38. Three fails: C-24, C-38, C-39. Score: 29/32 -> 99.06.

```
ROLE SEQUENCE: Architect -> PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

LIFECYCLE DESIGN: Every phase transition includes an explicit gate check before proceeding.
PRE-DOCUMENT checks run before any content is authored. Failures detected early are recorded
in the amendment table (STATUS = OPEN) and reported in finalization findings.

ROLE ASSIGNMENTS:
- Architect: Owns phase gate checks, register construction, technical options, and audit.
- PM: Owns business options, adoption trade-offs, and recommendation rationale.

---

PHASE 0 -- PRE-DOCUMENT [GATE: E-01]

Architect: Declare role sequence (Architect -> PM) as a typed header.

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Build trigger rules from the current rubric criteria. Assign each trigger a PHASE value.
Use the v14 criteria list for trigger construction: C-01 through C-38.
Each criterion generates one trigger row (T-01..T-38). Total: 38 rows.

PHASE column required for every row. Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != expected count)
  T-31 PHASE = FINALIZATION
  T-35 PHASE = FINALIZATION

PRE-DOCUMENT GATE CHECK -- run immediately after initialization:
  Check T-24: Does the amendment table row count equal the expected criterion count (38)?
  Count current rows. If count != 38, set T-24 STATUS = OPEN.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PRE-PHASE CHECK: Confirm role sequence declared. Confirm amendment table initialized.

Architect: State the shared problem.
  PROBLEM: [shared problem statement]
  TEMPORAL ANCHOR: [specific named date or sprint]
  INACTION CONSEQUENCE: [concrete named outcome of not deciding]

PM: Confirm business context and urgency.

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

PRE-OPTION CHECK: Confirm problem statement complete. Confirm amendment table initialized.

For each option (minimum 3, including do-nothing), produce:

  OPTION: [label and description]
  PROBLEM: [shared problem -- verbatim from Phase 1]
  RISK: Do not compute P*I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Risk register is built in Phase 3; R-NN IDs back-filled in Phase 9b.
        Architect notes technical risk category and vectors. PM notes adoption risk.
  RATIONALE: [why this option is a candidate]

---

PHASE 3 -- RISK REGISTER [GATE: R-01]

POST-OPTION CHECK: Verify option count >= 3, do-nothing present.

Architect: Risk register:
  R-NN | RISK | P | I | P*I | MITIGATION

At least 3 entries. P and I on 1-5 scale. Compute P*I.
PM: Add adoption and schedule risks.

---

PHASE 9b -- RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields from [R-NN pending] placeholders.

Enumerate citation sites by structural domain:

  Domain 1 -- Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] -> [R-03 (P:n * I:n = n), R-07 (P:n * I:n = n)]
    [OPTION-B label] RISK field: [R-NN pending] -> [R-01 (P:n * I:n = n), R-04 (P:n * I:n = n)]
    [do-nothing label] RISK field: [R-NN pending] -> [R-02 (P:n * I:n = n)]

  Domain 2 -- Comparison matrix risk column:
    Risk row: [OPTION-A column: R-NN IDs] | [OPTION-B column: R-NN IDs] |
              [do-nothing column: R-NN IDs]

Include P*I compound scores in Domain 1 transition targets.
Attribute R-NN IDs per option column in Domain 2.

---

PHASE 4 -- COMPARISON MATRIX [GATE: E-03]

POST-REGISTER CHECK: Confirm risk register >= 3 entries.

Comparison matrix -- OPTIONS as column headers.
Rows: Effort | Risk (R-NN cited) | Time-to-value | Reversibility | PM adoption friction.

---

PHASE 5 -- GATE AUDIT [GATE: C-21]

Architect: Audit all phase headers for [GATE: X-NN] citations. Record missing in amendment
table.

---

PHASE 6 -- COVERAGE TABLE [GATE: C-22]

Coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-38.
CLOSED BY must name the phase or step that satisfied each criterion.

---

PHASE 7 -- PREREQUISITES CHECK [GATE: R-02]

Verify: registers precede recommendation, phases in declared sequence.

---

PHASE 9 -- RECOMMENDATION [GATE: E-04]

PM: Recommended option with rationale referencing two matrix dimensions.
Qualifying conditions required.
Architect: Technical feasibility confirmation.

---

PHASE 10 -- FINALIZATION [GATE: R-03]

Execute as an explicitly numbered four-step list:

Step 1: Review amendment table for STATUS = OPEN triggers (including T-24 if it fired at
  PRE-DOCUMENT). For each open trigger T-NN, produce:
    "Finding N: T-NN -- [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing]."
  One finding per trigger. Enumerate sequentially.

Step 2: Verify all E-tier criteria satisfied.
Step 3: Verify all R-tier criteria satisfied.
Step 4: Update coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

Build from criteria list C-01..C-38. Total rows: 38 (T-01..T-38).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != expected count;
    expected count for v15 = 39; this table has 38 rows -- T-24 fires at PRE-DOCUMENT)
  T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" label format)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] -> [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transitions do not include P*I
                               compound scores alongside R-NN IDs in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution)
  T-38 PHASE = FINALIZATION  (fires if T-37 CONDITION entry lacks an inline exemplar quoting
                               the exact document construct that fires T-37)
```

---

## V-04 -- Conversational Register + PM-First | Axes: Phrasing Register + Role Sequence | Designed fails: C-25 + C-33

**Hypothesis**: A conversational-register PM-first variation with full Phase 9b structural
compliance -- including the full two-part T-37 CONDITION in natural language (C-38 PASS,
C-39 PASS) -- but fails C-25 (finalization described as a prose narrative walk-through, not a
numbered four-step list) and C-33 (Phase 2 RISK template contains the [R-NN pending] placeholder
but the "Do not compute P*I" prohibition adjacent to it is absent). C-36 PASS (Domain 1 P*I
transitions), C-37 PASS (Domain 2 per-column attribution). T-25 fires (no numbered steps),
T-33 fires (prohibition absent). T-38 and T-39 silent. Two open triggers. Finding 1: T-25;
Finding 2: T-33. 39-row table (C-24 PASS). Score: 30/32 -> 99.38.

```
ROLE SEQUENCE: PM -> Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

STYLE: Write in a conversational, explanatory register throughout. Explain rationale and
trade-offs in natural language. Use tables where structure adds clarity, but connect sections
with transitional prose. Phase summaries should read as coherent narrative, not isolated
bullet lists.

ROLE ASSIGNMENTS:
- PM: Leads narrative framing, business trade-offs, and recommendation.
- Architect: Provides technical constraints, risk assessment, and feasibility commentary.

---

PHASE 0 -- PRE-DOCUMENT [GATE: E-01]

Begin by declaring: "This proposal follows a PM -> Architect role sequence." Repeat this
attribution in each subsequent phase header to satisfy E-01.

Initialize the amendment table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-39 (39 trigger rules, one per v15 criterion). Assign PHASE for each.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PM: Open with a brief framing paragraph that explains the problem, why it matters now, and
what decision needs to be made. Then state the PROBLEM field explicitly:

  PROBLEM: [concise problem statement shared by all options]
  TEMPORAL ANCHOR: [specific sprint or date by which the decision must land]
  INACTION CONSEQUENCE: [named outcome if no option is chosen by the anchor]

Architect: Add a sentence on any technical constraints that shape the decision space.

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

Present each option (minimum 3, including do-nothing) in a narrative block. For each option,
include all four anatomy fields:

  OPTION: [label and description -- PM introduces the option's value proposition]
  PROBLEM: [repeat the shared problem statement verbatim]
  RISK: [R-NN pending] -- placeholder for risk register linkage; will be resolved in Phase 9b.
        PM names the key adoption concern; Architect names the key technical concern.
  RATIONALE: [PM explains why this option belongs in the shortlist]

---

PHASE 3 -- RISK REGISTER [GATE: R-01]

Architect: Construct the risk register:
  R-NN | RISK | P | I | P*I | MITIGATION

At least 3 entries. Use a 1-5 scale. Compute P*I.
PM: Add 1-2 adoption risk entries.

---

PHASE 9b -- RISK PROPAGATION [GATE: C-26]

Architect: Walk through each option's RISK field and replace the [R-NN pending] placeholder
with the applicable register entries. Include each register entry's P*I compound score in
the back-fill notation so that option anatomy is self-contained at review time. Then update
the comparison matrix risk column with per-option-column attribution.

Enumerate citation sites by structural domain:

  Domain 1 -- Option RISK fields (by option label) -- include P*I compound scores:
    [OPTION-A label] RISK field: [R-NN pending] -> [R-03 (P:n * I:n = n), R-07 (P:n * I:n = n)]
    [OPTION-B label] RISK field: [R-NN pending] -> [R-01 (P:n * I:n = n), R-04 (P:n * I:n = n)]
    [do-nothing label] RISK field: [R-NN pending] -> [R-02 (P:n * I:n = n)]

  Domain 2 -- Comparison matrix risk column -- attribute R-NN IDs per option column:
    Risk row: [OPTION-A column: R-NN IDs] | [OPTION-B column: R-NN IDs] |
              [do-nothing column: R-NN IDs]

---

PHASE 4 -- COMPARISON MATRIX [GATE: E-03]

Present a comparison matrix with OPTIONS as column headers.
Dimensions: Effort, Risk (R-NN cited), Time-to-value, Reversibility, PM adoption friction.
PM leads dimension selection; Architect validates scoring.

---

PHASE 5 -- GATE AUDIT [GATE: C-21]

Architect: Verify phase headers carry [GATE: X-NN] citations. Note any missing in the
amendment table.

---

PHASE 6 -- COVERAGE TABLE [GATE: C-22]

Build a coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-39.

---

PHASE 7 -- PREREQUISITES CHECK [GATE: R-02]

Verify phase ordering: options before registers, registers before recommendation.

---

PHASE 9 -- RECOMMENDATION [GATE: E-04]

PM: State the recommended option and explain the reasoning in narrative form, citing at least
two comparison matrix dimensions. Include qualifying conditions.
Architect: Confirm the recommendation is technically viable.

---

PHASE 10 -- FINALIZATION [GATE: R-03]

Walk through coverage verification as a narrative discussion. You are reviewing the document
for completeness and surfacing any gaps.

Begin by checking the amendment table for open trigger rules. For each open trigger T-NN,
produce a named finding inline in the narrative using the label format "Finding N: T-NN":
state the criterion ID and name, what the trigger expected, and what is absent or incomplete.
Each open trigger gets its own separately labeled finding entry. Do not bundle two open
triggers into a single finding.

Then confirm E-tier criterion satisfaction -- briefly note each essential criterion's status.
Next confirm R-tier satisfaction. Finally update the coverage table to reflect final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-39, exactly 39 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 39)
  T-25 PHASE = FINALIZATION  (fires if finalization verification is not a numbered 4-step list)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" label format)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column
                               as two named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P*I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] -> [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P*I compound scores in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry per-
                               option-column R-NN attribution -- confirming "risk row updated"
                               without naming per-column R-NN IDs fires T-37)
  T-38 PHASE = FINALIZATION  (fires if T-37 CONDITION entry lacks an inline exemplar quoting
                               the exact document construct that fires T-37)
  T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION entry carries the inline failure
                               exemplar (Part 1) but omits the correct-format prescription
                               (Part 2) -- two-part form required: Part 1 quotes the failure
                               construct AND Part 2 states "per-column format required:
                               [OPTION-A column: R-NN IDs] | [OPTION-B: R-NN IDs]")
```

---

## V-05 -- Inertia-Forward + Quad Fail | Axes: Inertia Framing + Lifecycle Combination | Designed fails: C-36 + C-37 + C-38 + C-39

**Hypothesis**: An inertia-forward variation that foregrounds the do-nothing option as the
default trajectory -- explicitly modeling the compounding cost of status quo, placing Option A
(do-nothing) first in all structures -- maintains structural compliance for non-depth criteria:
39-row amendment table (C-24 PASS), dual-domain Phase 9b naming (C-32 PASS), domain-index
prefixes (C-34 PASS), per-site arrow notation in Domain 1 (C-35 PASS), prohibition adjacent to
placeholder (C-33 PASS), numbered 4-step finalization (C-25 PASS). However, the variation fails
all four depth and exemplar criteria simultaneously: (1) Domain 1 transition targets list R-NN
IDs without P*I scores (`[R-NN pending] -> [R-03, R-07]` -- C-35 PASS, C-36 FAIL); (2) Domain 2
confirms only row-level risk presence ("Risk row: R-NN IDs applied by option" -- C-32 PASS,
C-37 FAIL); (3) T-37 CONDITION abstract, no failure exemplar (C-38 FAIL independent); (4) C-39
FAIL by cascade from C-38 (abstract entry contains neither Part 1 nor Part 2). Four open
triggers: T-36, T-37, T-38, T-39. Four findings. Score: 28/32 -> 98.75.

```
ROLE SEQUENCE: PM -> Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

INERTIA FRAMING: Open by foregrounding inaction as the default path. The do-nothing option
represents the current trajectory and must be evaluated first, before alternatives. Every
option is implicitly competing against the ongoing cost of not acting. The do-nothing option
appears as Option A in the option list and in the first column of the comparison matrix.
Model the inertia cost explicitly: what is the per-sprint or per-quarter cost of remaining
on the current trajectory?

ROLE ASSIGNMENTS:
- PM: Leads business case framing, inertia cost analysis, and recommendation.
- Architect: Owns technical risk identification, register construction, and feasibility.

---

PHASE 0 -- PRE-DOCUMENT [GATE: E-01]

PM: Declare role sequence (PM -> Architect) as a typed header. Apply in every phase header.
State the inertia framing principle: "Option A (do-nothing) is evaluated first as the default
trajectory. All alternatives are compared against the ongoing inertia cost."

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-39. Assign PHASE for each trigger. All STATUS = PENDING at init.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem. Lead with the inertia cost of not deciding.

  PROBLEM: [shared problem statement]
  INERTIA COST: [cost or consequence of maintaining status quo per sprint/quarter]
  TEMPORAL ANCHOR: [specific sprint or date by which the decision must be made]
  INACTION CONSEQUENCE: [concrete named outcome if no option is selected by the anchor]

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

Present options in this order: do-nothing first (Option A), then alternatives.

For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem -- verbatim from Phase 1]
  RISK: Do not compute P*I in Phase 2 RISK fields. Declare [R-NN pending] to reserve the
        slot. Risk register is built in Phase 3; R-NN IDs will be back-filled in Phase 9b.
        PM notes inertia or adoption risk category. Architect notes technical risk category.
  RATIONALE: [why this option is a candidate]

Option A must be the do-nothing (status-quo) option and must appear first.

---

PHASE 3 -- RISK REGISTER [GATE: R-01]

Architect: Build the risk register:
  R-NN | RISK | P | I | P*I | MITIGATION

At least 3 entries. Inertia-related risks (schedule drift, compounding technical debt) must
appear for Option A. P and I on a 1-5 scale. Compute P*I.
PM: Add adoption risk entries.

---

PHASE 9b -- RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs from the register into each option RISK field, replacing [R-NN pending].
Update the comparison matrix risk column with applicable register references.

Enumerate citation sites by structural domain:

  Domain 1 -- Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] -> [R-NN IDs applicable to Option A]
    [OPTION-B label] RISK field: [R-NN pending] -> [R-NN IDs applicable to Option B]
    [do-nothing label] RISK field: [R-NN pending] -> [R-NN IDs applicable to do-nothing]

  Domain 2 -- Comparison matrix risk column:
    Risk row: R-NN IDs applied by option. Applicable register entries referenced in risk row.

List each applicable R-NN ID at each Domain 1 site. The risk register carries the full P*I
scores; the register is the authoritative source for compound scoring.

---

PHASE 4 -- COMPARISON MATRIX [GATE: E-03]

Comparison matrix -- do-nothing (Option A) as first column.
Dimensions: Inertia cost, Implementation effort, Risk (R-NN cited), Time-to-value,
Reversibility, PM adoption friction.
Architect validates technical dimension scoring.

---

PHASE 5 -- GATE AUDIT [GATE: C-21]

Verify all phase headers carry [GATE: X-NN] citations. Record missing citations in amendment
table.

---

PHASE 6 -- COVERAGE TABLE [GATE: C-22]

Coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-39.

---

PHASE 7 -- PREREQUISITES CHECK [GATE: R-02]

Verify: Option A is do-nothing and appears first; registers complete; phases in sequence.

---

PHASE 9 -- RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Frame the recommendation against the inertia baseline
(Option A). Cite the sprint or time horizon at which the recommended option recovers its
implementation cost relative to Option A's ongoing inertia cost.
State qualifying conditions.
Architect: Confirm technical feasibility.

---

PHASE 10 -- FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review amendment table for STATUS = OPEN triggers.
  For each open trigger T-NN, produce:
    "Finding N: T-NN -- [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing]."
  One finding per trigger. Enumerate sequentially.

Step 2: Verify all E-tier criteria satisfied.
Step 3: Verify all R-tier criteria satisfied.
Step 4: Update coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-39, exactly 39 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 39)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name option RISK fields
                               by option label AND comparison matrix risk column as two named
                               structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P*I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] -> [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P*I compound scores alongside R-NN IDs in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry per-
                               option-column R-NN attribution)
  T-38 PHASE = FINALIZATION  (fires if T-37 CONDITION entry lacks an inline exemplar quoting
                               the exact document construct that fires T-37)
  T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION entry does not carry both Part 1
                               (inline failure exemplar) and Part 2 (correct-format
                               prescription for per-option-column attribution))
```
