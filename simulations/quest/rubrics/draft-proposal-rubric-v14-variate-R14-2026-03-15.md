# draft-proposal Variate — Round 14

Rubric version: v14 · Formula: /31 · New criterion: C-38 (amendment table T-37 trigger entry
includes inline failure-condition exemplar in CONDITION field)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Role sequence (Architect-first) — designed fail: C-38 only
  (C-37 PASS: Domain 2 per-column attribution present; T-37 CONDITION abstract, no inline
  exemplar — isolates C-38 against a fully-compliant Phase 9b)
- **V-02**: Output format (compact tables, PM-first) — designed fail: C-37 only
  (C-38 PASS: T-37 CONDITION carries inline exemplar; C-37 FAIL: Domain 2 row-level only —
  reference exemplar for C-38 PASS when T-37 fires)
- **V-03**: Lifecycle emphasis (stale trigger count: 37 rows, v13 table carried forward) —
  designed fails: C-24 + C-38 independent fail
  (T-37 exists in stale table but carries abstract condition; C-38 fails independently, not
  by cascade; T-38 absent from stale table; one named finding: T-24)
- **V-04**: Phrasing register (conversational) + Role sequence combination —
  designed fails: C-25 + C-33; C-38 PASS via inline exemplar in conversational style
  (C-36 PASS, C-37 PASS: both depth criteria satisfied in conversational register; 38-row
  table; T-38 silent)
- **V-05**: Inertia framing + C-36 + C-37 + C-38 triple fail —
  designed fails: C-36 + C-37 + C-38; all three depth/exemplar criteria fail simultaneously
  (C-24 PASS: 38-row table; T-37 CONDITION abstract; Domain 1 no P×I; Domain 2 row-level only;
  three open triggers: T-36, T-37, T-38)

Predicted scores: V-01 → 99.68 · V-02 → 99.68 · V-03 → 99.35 · V-04 → 99.35 · V-05 → 99.03

---

## V-01 — Architect-First | Axis: Role Sequence | Designed fail: C-38

**Hypothesis**: An Architect-led variation with complete Phase 9b structural compliance — dual-
domain enumeration (C-32 PASS), domain-index prefixes (C-34 PASS), per-site arrow notation
(C-35 PASS), P×I compound scores in Domain 1 transitions (C-36 PASS), and per-option-column
Domain 2 attribution (C-37 PASS) — but with the T-37 CONDITION entry in the amendment table
using abstract condition text ("fires if per-column attribution absent from Domain 2") without
an inline quoted exemplar of what row-level Domain 2 confirmation looks like. C-18 PASS (trigger
rules front-loaded), C-29 PASS (PHASE column populated), C-38 FAIL (no inline exemplar in T-37
CONDITION). T-38 fires at FINALIZATION. One open trigger: T-38. Finding 1: T-38.
38-row amendment table (C-24 PASS). CLOSED BY column present (C-22 PASS). Prohibition adjacent
to placeholder (C-33 PASS). Numbered 4-step finalization (C-25 PASS). Score: 30/31 → 99.68.

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

Populate trigger rules T-01..T-38 -- one per v14 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires (PRE-DOCUMENT,
PRE-OPTION, FINALIZATION, or a named phase). Leave STATUS = PENDING for all rows at init.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

Architect: State the shared problem being decided. This PROBLEM field is shared by all options
and must appear verbatim in every option entry.

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

Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-38.
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

Trigger rules T-01..T-38 -- exactly 38 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 38)
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
                               per-option-column R-NN attribution)
  T-38 PHASE = FINALIZATION  (fires if T-37 CONDITION entry lacks an inline exemplar quoting
                               the exact document construct that fires T-37)
```

---

## V-02 -- PM-First, Compact Tables | Axis: Output Format | Designed fail: C-37 only; C-38 PASS

**Hypothesis**: A compact PM-first variation will include full Domain 1 P*I transitions (C-36
PASS: each Domain 1 site shows `[R-NN pending] -> [R-03 (P:n * I:n = n), R-07 (P:n * I:n = n)]`)
but fail C-37 by confirming Domain 2 only at the row level: "Risk row: R-NN IDs applied to risk
row" -- no per-option-column attribution. The T-37 CONDITION entry in the amendment table spec
carries an explicit inline exemplar quoting the exact firing construct: "row-level confirmation
'R-NN IDs applied to risk row' fires T-37". C-38 PASS. T-38 is silent (C-38 passes). CLOSED BY
column present (C-22 PASS). 38-row amendment table (C-24 PASS). Prohibition adjacent to
placeholder (C-33 PASS). Numbered 4-step finalization (C-25 PASS). One open trigger: T-37.
Finding 1: T-37. Score: 30/31 -> 99.68.

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
Populate T-01..T-38. Assign each trigger a PHASE value. All STATUS = PENDING at init.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PM: Compact problem block:
  PROBLEM: [shared problem for all options]
  DECISION REQUIRED: [what must be chosen]
  WHY NOW: [urgency or cost of inaction]

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-38.
STATUS = PASS or FAIL. CLOSED BY = phase that satisfied the criterion.

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

Execute as explicitly numbered four-step list:

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

T-01..T-38, exactly 38 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 38)
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
```

---

## V-03 -- Stale Table (37 rows) | Axis: Lifecycle Emphasis | Designed fails: C-24 + C-38 independent

**Hypothesis**: A lifecycle-gate-heavy variation builds its amendment table from the v13 rubric
criteria list (T-01..T-37, 37 rows). T-24 fires at PRE-DOCUMENT (37 != 38 required by v14).
T-38 is absent from the stale table and cannot fire -- C-38 fails behaviorally but produces no
named T-38 finding. The T-37 CONDITION entry carries abstract text ("fires if per-option-column
attribution absent from Domain 2") without an inline exemplar -- C-38 fails independently even
though T-37 exists (the exemplar absence is detectable from T-37's CONDITION cell regardless of
T-38's existence). Phase 9b is fully compliant with the depth criteria: Domain 1 transitions
include P*I compound scores (C-36 PASS), Domain 2 carries explicit per-option-column attribution
(C-37 PASS). CLOSED BY column present (C-22 PASS). Prohibition adjacent to placeholder (C-33
PASS). Numbered 4-step finalization (C-25 PASS). One named finding: Finding 1: T-24.
Two fails: C-24 + C-38. Score: 29/31 -> 99.35.

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

Use this criteria list for trigger construction: C-01 through C-37.
Each criterion in the list generates one trigger row (T-01..T-37). Total: 37 rows.

PHASE column required for every row:
  T-24 PHASE = PRE-DOCUMENT  (fires if row count mismatches expected count)
  T-31 PHASE = FINALIZATION
  T-35 PHASE = FINALIZATION

PRE-DOCUMENT GATE CHECK -- run immediately after initialization:
  Check T-24: Does the amendment table row count equal the expected criterion count?
  If count != expected, set T-24 STATUS = OPEN.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PRE-PHASE CHECK: Confirm role sequence declared (T-01). Confirm amendment table initialized.
If either fails, record in amendment table before proceeding.

Architect: State the shared problem.
PM: Confirm business context and urgency.

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

PRE-OPTION CHECK: Confirm problem statement complete. Confirm amendment table initialized.

For each option (minimum 3, including do-nothing), produce:

  OPTION: [label and description]
  PROBLEM: [shared problem -- verbatim from Phase 1]
  RISK: Do not compute P*I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Risk register is built in Phase 3; R-NN IDs will be back-filled in Phase 9b.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-37.
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

Build from criteria list C-01..C-37. Total rows: 37 (T-01..T-37).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != expected count;
    expected count for v14 = 38; this table has 37 rows -> T-24 fires at PRE-DOCUMENT)
  T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" label format)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] -> [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transitions do not include P*I scores)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution)
```

---

## V-04 -- Conversational + 38-row | Axes: Phrasing Register + Role Sequence | Designed fails: C-25 + C-33; C-38 PASS

**Hypothesis**: A conversational-register PM-first variation will perform finalization as a prose
narrative (C-25 FAIL: "walk through" framing without numbered steps) and omit the "Do not compute
P*I" prohibition from the Phase 2 RISK template (C-33 FAIL: placeholder present, prohibition
absent). However, the 38-row amendment table (C-24 PASS) carries a T-37 CONDITION entry with an
inline exemplar in natural language: "confirming 'risk row updated' without naming per-column
R-NN IDs fires T-37". C-38 PASS. Phase 9b demonstrates the ceiling for both depth criteria in
conversational style: Domain 1 transitions include P*I compound scores (C-36 PASS), Domain 2
carries per-option-column attribution (C-37 PASS). T-38 is silent (C-38 passes). Two open
triggers: T-25, T-33. Finding 1: T-25, Finding 2: T-33. Score: 29/31 -> 99.35.

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
Populate T-01..T-38 (38 trigger rules, one per v14 criterion). Assign PHASE for each.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PM: Open with a brief framing paragraph that explains the problem, why it matters now, and
what decision needs to be made. Then state the PROBLEM field explicitly:

  PROBLEM: [concise problem statement shared by all options]

Architect: Add a sentence on any technical constraints that shape the decision space.

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

Present each option (minimum 3, including do-nothing) in a narrative block. For each option,
include all four anatomy fields:

  OPTION: [label and description -- PM introduces the option's value proposition]
  PROBLEM: [repeat the shared problem statement verbatim]
  RISK: [R-NN pending] -- Placeholder for risk register linkage; will be resolved in Phase 9b.
        For now, PM names the key adoption concern; Architect names the key technical concern.
        Example: "[R-NN pending] -- PM: high switching cost for teams. Architect: requires
        async coordination across two services."
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
      Risk row: [OPTION-A column: R-03, R-07 | OPTION-B column: R-01, R-04 |
                 do-nothing column: R-02]

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-38.

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

Then discuss E-tier criterion satisfaction -- briefly confirm or flag each essential criterion.
Next discuss R-tier satisfaction in the same way. Finally note overall completeness of the
document and whether any follow-up is warranted.

Update the coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-38, exactly 38 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 38)
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
```

---

## V-05 -- Inertia-Forward + C-36 + C-37 + C-38 Triple Fail | Axes: Inertia Framing + Combination

**Hypothesis**: An inertia-forward variation that foregrounds the status-quo option will maintain
complete Phase 9b structural compliance for all non-depth criteria -- dual-domain enumeration
(C-32 PASS), domain-index prefixes (C-34 PASS), per-site arrow notation (C-35 PASS), prohibition
adjacent to placeholder (C-33 PASS) -- but fail all three depth criteria simultaneously: (1)
Domain 1 transitions list R-NN IDs without P*I scores (`[R-NN pending] -> [R-03, R-07]` -- C-35
PASS, C-36 FAIL), (2) Domain 2 provides aggregate risk-row attribution without per-column
breakdown ("Risk row: R-NN IDs applied by option" -- C-32 PASS, C-37 FAIL), and (3) T-37
CONDITION entry in the 38-row amendment table carries abstract text ("fires if per-option-column
attribution absent") without an inline exemplar (C-38 FAIL independent -- T-37 entry exists but
exemplar absent). C-24 PASS (38 rows). Three open triggers: T-36, T-37, T-38.
Three findings at finalization. Score: 28/31 -> 99.03.

```
ROLE SEQUENCE: PM -> Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

INERTIA FRAMING: Open by foregrounding inaction as the default path. The do-nothing option
represents the current trajectory and must be evaluated first, before alternatives. Every
option is implicitly competing against the ongoing cost of not acting. The do-nothing option
appears as Option A in the option list and in the first column of the comparison matrix.

ROLE ASSIGNMENTS:
- PM: Leads business case framing, inertia cost analysis, and recommendation.
- Architect: Owns technical risk identification, register construction, and feasibility.

---

PHASE 0 -- PRE-DOCUMENT [GATE: E-01]

PM: Declare role sequence (PM -> Architect) as a typed header. Apply in every phase header.
State the inertia framing principle: "Option A (do-nothing) is evaluated first as the default
trajectory."

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-38. Assign PHASE for each trigger. All STATUS = PENDING at init.

---

PHASE 1 -- PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem. Include an inertia cost statement: what happens if no option
is selected and the current state continues.

  PROBLEM: [shared problem statement]
  INERTIA COST: [cost or consequence of maintaining the status quo per unit time]

---

PHASE 2 -- OPTION COMPOSITION [GATE: E-02]

Present options in this order: do-nothing first, then alternatives.

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
scores; the register is the authoritative source for compound scoring -- option anatomy carries
the register IDs for traceability.

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-38.

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

T-01..T-38, exactly 38 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 38)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column as
                               two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P*I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] -> [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P*I compound scores in the back-fill target -- R-NN IDs listed
                               without compound scores fire T-36)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution)
  T-38 PHASE = FINALIZATION  (fires if T-37 CONDITION entry lacks an inline exemplar quoting
                               the exact document construct that fires T-37)
```

---

## Predicted Scoring

| Variation | Axes | v14 Fails | A/31 | Composite |
|-----------|------|-----------|------|-----------|
| V-01 | Role sequence | C-38 | 30/31 | **99.68** |
| V-02 | Output format | C-37 | 30/31 | **99.68** |
| V-03 | Lifecycle emphasis | C-24 + C-38 | 29/31 | **99.35** |
| V-04 | Phrasing register + role | C-25 + C-33 | 29/31 | **99.35** |
| V-05 | Inertia + combination | C-36 + C-37 + C-38 | 28/31 | **99.03** |

**V-01 C-38 isolation (1 fail)**: Phase 9b fully compliant -- C-32 PASS, C-34 PASS, C-35 PASS,
C-36 PASS (P*I in Domain 1 transitions), C-37 PASS (per-column Domain 2 attribution). T-37
CONDITION carries abstract text; no inline exemplar. One open trigger: T-38. Finding 1: T-38.
30/31.

**V-02 C-37 isolation + C-38 PASS reference (1 fail)**: Domain 1 fully compliant -- per-site
arrows with P*I scores (C-35 PASS, C-36 PASS). Domain 2 row-level only: "Risk row: R-NN IDs
applied to risk row" -- confirms domain presence (C-32 PASS, C-34 PASS) but no per-column
attribution (C-37 FAIL). T-37 CONDITION carries inline exemplar: "row-level confirmation 'R-NN
IDs applied to risk row' fires T-37" -- C-38 PASS. T-38 silent. One open trigger: T-37.
Finding 1: T-37. 30/31.

**V-03 stale table + C-38 independent fail (2 fails)**: T-24 fires at PRE-DOCUMENT (37 rows !=
38 required by v14). T-38 absent from stale table. T-37 CONDITION abstract -- C-38 fails
behaviorally; no T-38 finding. C-36 PASS, C-37 PASS (Phase 9b depth fully compliant). One named
finding: Finding 1: T-24. Two fails: C-24 + C-38. 29/31.

**V-04 conversational + 38-row + C-38 PASS (2 fails on phrasing axes)**: Phase 9b demonstrates
ceiling behavior for C-36 (P*I in Domain 1) and C-37 (per-column Domain 2) in conversational
style. C-38 PASS -- T-37 CONDITION carries inline exemplar in natural language form. Fails are
orthogonal to the new criterion: prose finalization (C-25 FAIL), placeholder without prohibition
(C-33 FAIL). Two open triggers: T-25, T-33. 29/31.

**V-05 triple depth fail against compliant Phase 9b structure (3 fails)**: Phase 9b structurally
sound -- C-32 PASS, C-33 PASS, C-34 PASS, C-35 PASS. Fails isolated to all three depth/exemplar
criteria: Domain 1 transitions omit P*I (C-36 FAIL), Domain 2 aggregate without column labels
(C-37 FAIL), T-37 CONDITION abstract without exemplar (C-38 FAIL). Three open triggers:
T-36, T-37, T-38. 28/31.

**C-38 discrimination axes confirmed by R14:**
- V-01 provides cleanest C-38 isolation: C-37 PASS (T-37 never fires during run), T-38 fires
  because T-37 CONDITION lacks exemplar at initialization time. Confirms C-38 is independently
  testable from whether T-37 actually fires -- it is a structural property of the amendment
  table spec, not a runtime event.
- V-02 provides C-38 PASS reference when T-37 fires: T-37 fires (C-37 FAIL), but T-38 is
  silent because T-37 CONDITION carries the inline exemplar. Confirms C-38 and C-37 are
  independently testable -- a variation can fail C-37 while passing C-38.
- V-03 confirms C-38 independent fail from stale-table path: T-37 exists in the 37-row table
  but CONDITION is abstract. C-38 fails behaviorally even though T-38 is not present to fire.
- V-05 confirms C-38 independent fail alongside C-36 and C-37 fails: 38-row table (T-38
  present), T-37 CONDITION abstract. All three depth criteria fail; T-38 fires as a named
  trigger.

**New cascade evidence for v14:**
- C-38 is testable at initialization: a reviewer reads the T-37 CONDITION cell in the amendment
  table spec. No runtime Phase 9b execution required -- the exemplar either appears in the spec
  or it does not. V-01 and V-03 confirm this: C-37 PASS (no runtime T-37 event) is compatible
  with C-38 FAIL (exemplar absent from T-37 spec).
- C-38 does not cascade from C-37: failing C-37 does not cause C-38 to fail or pass. V-02
  confirms: C-37 FAIL + C-38 PASS is achievable. V-05 confirms: C-37 FAIL + C-38 FAIL is
  achievable independently (the combination is not forced).
- Stale-table C-38 determination: For a v13-era 37-row table, T-38 is absent but C-38 is
  still evaluable from T-37 CONDITION content. V-03 demonstrates the independent-fail path:
  C-24 FAIL (stale row count) does not automatically cascade to C-38 FAIL -- it depends on
  whether T-37 CONDITION carries the exemplar. A v13-era table with an exemplar-bearing T-37
  entry would pass C-38 while failing C-24.
