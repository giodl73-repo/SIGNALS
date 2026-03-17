# draft-proposal Variate — Round 13

Rubric version: v13 · Formula: /30 · New criteria: C-36 (Phase 9b Domain 1 P×I compound
scores in back-fill transition), C-37 (Phase 9b Domain 2 per-option-column R-NN attribution)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Role sequence (Architect-first) — designed fail: C-36 only
  (C-34 PASS, C-35 PASS, C-37 PASS: R-NN IDs in Domain 1 transitions but no P×I scores)
- **V-02**: Output format (compact tables, PM-first) — designed fail: C-37 only
  (C-36 PASS: P×I in Domain 1; Domain 2 row-level only, no per-column attribution)
- **V-03**: Lifecycle emphasis (stale trigger count: 35 rows, not 37) — designed fails: C-24 + C-36 + C-37
  (T-36 and T-37 absent from table; C-35 PASS but Domain 1 no P×I, Domain 2 row-level only)
- **V-04**: Phrasing register (conversational) — designed fails: C-25 + C-33
  (C-36 PASS + C-37 PASS: both new criteria pass in conversational register)
- **V-05**: Inertia framing + C-36+C-37 dual fail — designed fails: C-36 + C-37
  (C-33 PASS, C-34 PASS, C-35 PASS: Phase 9b fully structured but no P×I and no per-column)

Predicted scores: V-01 → 99.67 · V-02 → 99.67 · V-04 → 99.33 · V-05 → 99.33 · V-03 → 99.00

---

## V-01 — Architect-First | Axis: Role Sequence | Designed fail: C-36

**Hypothesis**: An Architect-led variation with complete Phase 9b structural compliance —
dual-domain enumeration (C-32 PASS), domain-index prefixes (C-34 PASS), per-site arrow
notation (C-35 PASS), and Domain 2 per-option-column attribution (C-37 PASS) — but omitting
P×I compound scores from Domain 1 transition targets will isolate C-36. The back-fill notation
shows `[R-NN pending] → [R-03, R-07]` at each Domain 1 site: transition notation is present
(C-35 PASS) but the target carries only R-NN IDs without the compound scores (C-36 FAIL).
Domain 2 carries explicit per-column attribution: "Risk row: [OPTION-A column: R-03, R-07 |
OPTION-B column: R-01 | do-nothing column: R-02]" (C-37 PASS). Trigger count 37 (C-24 PASS).
CLOSED BY column present (C-22 PASS). Prohibition adjacent to placeholder (C-33 PASS).
Numbered 4-step finalization (C-25 PASS). One open trigger: T-36.
Finding 1: T-36. Score: 29/30 → 99.67.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Owns option framing, technical risk assessment, register construction, Phase 9b
  back-fill, gate audit, and feasibility validation.
- PM: Owns business trade-off commentary, adoption risk factors, and recommendation rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) as a typed header at the top of the
output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-37 — one per v13 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires (PRE-DOCUMENT,
PRE-OPTION, FINALIZATION, or a named phase). Leave STATUS = PENDING for all rows at init.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

Architect: State the shared problem being decided. This PROBLEM field is shared by all options
and must appear verbatim in every option entry.

PM: Confirm the problem statement captures business context and urgency.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Compose at least 3 options. One must be a do-nothing or status-quo option. For each option,
produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot for Phase 9b back-fill. Note risk category only (adoption barrier /
        schedule risk / technical coupling). PM notes business risk category; Architect
        notes technical risk category.
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build the risk register:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 technical risk entries. P and I on a 1-5 scale. Compute P×I per entry.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs from the register into each option RISK field, replacing [R-NN pending].
Update the comparison matrix risk column.

Enumerate citation sites by structural domain:

  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [R-NN IDs applicable to this option]
    [OPTION-B label] RISK field: [R-NN pending] → [R-NN IDs applicable to this option]
    [do-nothing label] RISK field: [R-NN pending] → [R-NN IDs applicable to this option]

  Domain 2 — Comparison matrix risk column:
    Risk row: [OPTION-A column: R-NN IDs | OPTION-B column: R-NN IDs |
               do-nothing column: R-NN IDs]

List each applicable R-NN ID at each site. The register carries the full P×I scores; reference
the register for compound scores rather than repeating them in the transition notation.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Architect: Build a comparison matrix with OPTIONS as column headers.
Rows: Effort, Technical risk score (R-NN cited), Reversibility, Time-to-value.
PM: Add Adoption friction and Business value rows.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN] citation.
List any missing citations. Update amendment table for any T-NN that fires.

---

PHASE 6 — COVERAGE TABLE [GATE: C-22]

Build a coverage table:
  CRITERION | STATUS | CLOSED BY

Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-37.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing present, risk register >= 3 entries, Phase 9b complete,
assumption register >= 2 entries, both registers precede recommendation in document sequence.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide rationale referencing at least two comparison matrix
dimensions. State qualifying conditions (at least 2 circumstances under which the
recommendation changes).
Architect: Confirm technical feasibility.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."
  Enumerate sequentially (Finding 1, Finding 2, ...). One finding per trigger.

Step 2: Verify all E-tier criteria satisfied. Update coverage table for any failing criterion.

Step 3: Verify all R-tier criteria satisfied. Update coverage table for any failing criterion.

Step 4: Confirm coverage table is fully populated. Set COMPLETION STATUS of amendment table.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-37 — exactly 37 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
PHASE column populated for every row. Key triggers:
  T-01 PHASE = PRE-DOCUMENT
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 37)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column
                               as two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                               P×I" prohibition adjacent to [R-NN pending] placeholder)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] → [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P×I compound scores alongside R-NN IDs in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution)

At document completion, update STATUS for any trigger that fired.
```

---

## V-02 — PM-First, Compact Tables | Axis: Output Format | Designed fail: C-37

**Hypothesis**: A compact-table PM-first variation will include full Domain 1 P×I transitions
(C-36 PASS: each Domain 1 site shows `[R-NN pending] → [R-03 (P:n × I:n = n), R-07
(P:n × I:n = n)]`) but fail C-37 by confirming Domain 2 only at the row level: "Risk row:
R-NN IDs applied to risk row. Confirm applicable entries present." — no per-option-column
attribution. The compact-format rationale: cell real estate is minimized, per-column breakdown
treated as overhead. C-22 PASS (CLOSED BY column present — kept even in compact form for
traceability). Trigger count 37 (C-24 PASS). Prohibition adjacent to placeholder (C-33 PASS).
Numbered 4-step finalization (C-25 PASS). One open trigger: T-37.
Finding 1: T-37. Score: 29/30 → 99.67.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

OUTPUT FORMAT: Compact tables throughout. Minimize prose between tables.
Use concise cell values. Each phase produces a table or structured block, not paragraphs.

ROLE ASSIGNMENTS:
- PM: Leads business framing, option business cases, recommendation rationale, adoption risk.
- Architect: Validates technical constraints, owns risk register entries, confirms feasibility.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare role sequence (PM → Architect) as a typed header. Apply in every phase header.

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-37. Assign each trigger a PHASE value. All STATUS = PENDING at init.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: Compact problem block:
  PROBLEM: [shared problem for all options]
  DECISION REQUIRED: [what must be chosen]
  WHY NOW: [urgency or cost of inaction]

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

For each option (minimum 3, including do-nothing), produce a compact option block:

  OPTION: [label and brief description]
  PROBLEM: [shared problem — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Note risk category only: adoption barrier / schedule risk / technical
        coupling. PM notes business risk category; Architect notes technical risk category.
  RATIONALE: [one-sentence: why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Compact risk register table:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 entries. P and I on 1-5 scale. P×I computed.
PM: Add 1-2 adoption or schedule risk entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:

  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]
    [OPTION-B label] RISK field: [R-NN pending] → [R-01 (P:n × I:n = n), R-04 (P:n × I:n = n)]
    [do-nothing label] RISK field: [R-NN pending] → [R-02 (P:n × I:n = n)]

  Domain 2 — Comparison matrix risk column:
    Risk row: R-NN IDs applied to risk row. Confirm applicable register entries present.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Compact matrix — OPTIONS as column headers.
Rows: Effort | Risk (R-NN cited) | Time-to-value | Reversibility | Adoption friction
PM leads dimension selection; Architect validates technical dimensions.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Verify all phase headers carry [GATE: X-NN] citations. List any missing.
Update amendment table for any T-NN that fires.

---

PHASE 6 — COVERAGE TABLE [GATE: R-03]

Coverage table columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-37.
STATUS = PASS or FAIL. CLOSED BY = phase that satisfied the criterion.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Confirm: options >= 3, do-nothing present, risk register entries >= 3, Phase 9b complete,
registers precede recommendation.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option with business rationale citing two matrix dimensions.
State qualifying conditions.
Architect: Confirm technical feasibility.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute as explicitly numbered four-step list:

Step 1: Review amendment table for STATUS = OPEN triggers.
  For each open trigger T-NN, produce:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing]."
  Enumerate sequentially. One finding per trigger.

Step 2: Verify all E-tier criteria satisfied.
Step 3: Verify all R-tier criteria satisfied.
Step 4: Update coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-37, exactly 37 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 37)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name option RISK fields
                               by option label AND comparison matrix risk column as two named
                               structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] → [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P×I compound scores in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution — row-level confirmation
                               "R-NN IDs applied to risk row" fires T-37)
```

---

## V-03 — Lifecycle-Heavy | Axis: Lifecycle Emphasis | Designed fails: C-24 + C-36 + C-37

**Hypothesis**: A lifecycle-gate-heavy variation that builds its amendment table from the v12
rubric criteria list (T-01..T-35, 35 rows) triggers C-24 at PRE-DOCUMENT (35 != 37). Because
T-36 and T-37 are absent from the stale table, Phase 9b's register-linkage depth failures
cannot be captured as named trigger findings; C-36 and C-37 fail behaviorally but produce no
ordinal findings at finalization (no T-36 / T-37 rows exist to fire). Phase 9b uses per-site
arrow notation (C-35 PASS: `[R-NN pending] → [R-NN IDs]` form present at each Domain 1 site)
but Domain 1 transitions list only R-NN IDs without P×I scores (C-36 FAIL), and Domain 2
confirms "R-NN IDs confirmed in risk row" without per-column breakdown (C-37 FAIL). One named
finding at finalization: Finding 1: T-24. CLOSED BY column present (C-22 PASS). Prohibition
adjacent to placeholder (C-33 PASS). Numbered 4-step finalization (C-25 PASS).
Three fails: C-24 + C-36 + C-37. Score: 27/30 → 99.00.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

LIFECYCLE DESIGN: Every phase transition includes an explicit gate check before proceeding.
PRE-DOCUMENT checks run before any content is authored. Failures detected early are recorded
in the amendment table (STATUS = OPEN) and reported in finalization findings.

ROLE ASSIGNMENTS:
- Architect: Owns phase gate checks, register construction, technical options, and audit.
- PM: Owns business options, adoption trade-offs, and recommendation rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare role sequence (Architect → PM) as a typed header.

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Build trigger rules from the current rubric criteria. Assign each trigger a PHASE value.

Use this criteria list for trigger construction: C-01 through C-35.
Each criterion in the list generates one trigger row (T-01..T-35). Total: 35 rows.

PHASE column required for every row:
  T-24 PHASE = PRE-DOCUMENT  (fires if row count mismatches expected count)
  T-31 PHASE = FINALIZATION
  T-35 PHASE = FINALIZATION

PRE-DOCUMENT GATE CHECK — run immediately after initialization:
  Check T-24: Does the amendment table row count equal the expected criterion count?
  If count != expected, set T-24 STATUS = OPEN.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PRE-PHASE CHECK: Confirm role sequence declared (T-01). Confirm amendment table initialized.
If either fails, record in amendment table before proceeding.

Architect: State the shared problem.
PM: Confirm business context and urgency.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PRE-OPTION CHECK: Confirm problem statement complete. Confirm amendment table initialized.

For each option (minimum 3, including do-nothing), produce:

  OPTION: [label and description]
  PROBLEM: [shared problem — verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Risk register is built in Phase 3; R-NN IDs will be back-filled in Phase 9b.
        Architect notes technical risk category and vectors. PM notes adoption risk.
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

POST-OPTION CHECK: Verify option count >= 3, do-nothing present.

Architect: Risk register:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 entries. P and I on 1-5 scale. Compute P×I.
PM: Add adoption and schedule risks.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields from [R-NN pending] placeholders.

Domain 1 — Option RISK fields (by option label):
  [OPTION-A label] RISK field: [R-NN pending] → [R-NN IDs applicable to this option]
  [OPTION-B label] RISK field: [R-NN pending] → [R-NN IDs applicable to this option]
  [do-nothing label] RISK field: [R-NN pending] → [R-NN IDs applicable to this option]

Domain 2 — Comparison matrix risk column:
  R-NN IDs confirmed in risk row. Confirm applicable register entries are referenced.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

POST-REGISTER CHECK: Confirm risk register >= 3 entries.

Comparison matrix — OPTIONS as column headers.
Rows: Effort | Risk (R-NN cited) | Time-to-value | Reversibility | PM adoption friction.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Audit all phase headers for [GATE: X-NN] citations. Record missing in amendment
table.

---

PHASE 6 — COVERAGE TABLE [GATE: C-22]

Coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-35.
CLOSED BY must name the phase or step that satisfied each criterion.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Verify: registers precede recommendation, phases in declared sequence.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Recommended option with rationale referencing two matrix dimensions.
Qualifying conditions required.
Architect: Technical feasibility confirmation.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute as an explicitly numbered four-step list:

Step 1: Review amendment table for STATUS = OPEN triggers (including T-24 if it fired at
  PRE-DOCUMENT). For each open trigger T-NN, produce:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing]."
  One finding per trigger. Enumerate sequentially.

Step 2: Verify all E-tier criteria satisfied.
Step 3: Verify all R-tier criteria satisfied.
Step 4: Update coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

Build from criteria list C-01..C-35. Total rows: 35 (T-01..T-35).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != expected count;
    expected count for v13 = 37; this table has 35 rows → T-24 fires at PRE-DOCUMENT)
  T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" label format)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] → [R-NN entries] transition notation per site)
```

---

## V-04 — Conversational Register | Axis: Phrasing Register | Designed fails: C-25 + C-33; C-36 + C-37 both PASS

**Hypothesis**: A conversational-register variation will perform finalization as a prose
narrative (C-25 FAIL: "walk through" framing without numbered steps) and omit the "Do not
compute P×I" prohibition from the Phase 2 RISK template (C-33 FAIL: placeholder present,
prohibition absent). However, Phase 9b will demonstrate both C-36 and C-37 passing in a
natural language register: Domain 1 transitions include full P×I compound scores embedded in
arrow notation (`[R-NN pending] → [R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]`), and Domain
2 carries explicit per-option-column attribution ("Risk row: [OPTION-A column: R-03, R-07 |
OPTION-B column: R-01 | do-nothing column: R-02]"). This variation confirms C-36 and C-37 are
achievable in a conversational style. Two open triggers: T-25, T-33. Finding ordinal labels
appear inline in narrative (C-30 PASS). Trigger count 37 (C-24 PASS). CLOSED BY column present
(C-22 PASS). Score: 28/30 → 99.33.

```
ROLE SEQUENCE: PM → Architect

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

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Begin by declaring: "This proposal follows a PM → Architect role sequence." Repeat this
attribution in each subsequent phase header to satisfy E-01.

Initialize the amendment table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-37 (37 trigger rules, one per v13 criterion). Assign PHASE for each.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: Open with a brief framing paragraph that explains the problem, why it matters now, and
what decision needs to be made. Then state the PROBLEM field explicitly:

  PROBLEM: [concise problem statement shared by all options]

Architect: Add a sentence on any technical constraints that shape the decision space.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Present each option (minimum 3, including do-nothing) in a narrative block. For each option,
include all four anatomy fields:

  OPTION: [label and description — PM introduces the option's value proposition]
  PROBLEM: [repeat the shared problem statement verbatim]
  RISK: [R-NN pending] — Placeholder for risk register linkage; will be resolved in Phase 9b.
        For now, PM names the key adoption concern; Architect names the key technical concern.
        Example: "[R-NN pending] — PM: high switching cost for teams. Architect: requires
        async coordination across two services."
  RATIONALE: [PM explains why this option belongs in the shortlist]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Construct the risk register:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 entries. Use a 1-5 scale. Compute P×I.
PM: Add 1-2 adoption risk entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Walk through each option's RISK field and replace the [R-NN pending] placeholder
with the applicable register entries. Include each register entry's P×I compound score in
the back-fill notation so that option anatomy is self-contained at review time. Then update
the comparison matrix risk column with per-option-column attribution.

Enumerate citation sites by structural domain:

  Domain 1 — Option RISK fields (by option label) — show the full back-fill transition
      including P×I compound scores from the register:
      [OPTION-A label] RISK field: [R-NN pending] → [R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]
      [OPTION-B label] RISK field: [R-NN pending] → [R-01 (P:n × I:n = n), R-04 (P:n × I:n = n)]
      [do-nothing label] RISK field: [R-NN pending] → [R-02 (P:n × I:n = n)]

  Domain 2 — Comparison matrix risk column — attribute R-NN IDs to each option's column:
      Risk row: [OPTION-A column: R-03, R-07 | OPTION-B column: R-01, R-04 |
                 do-nothing column: R-02]

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Present a comparison matrix with OPTIONS as column headers.
Dimensions: Effort, Risk (R-NN cited), Time-to-value, Reversibility, PM adoption friction.
PM leads dimension selection; Architect validates scoring.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify phase headers carry [GATE: X-NN] citations. Note any missing in the
amendment table.

---

PHASE 6 — COVERAGE TABLE [GATE: C-22]

Build a coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-37.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Verify phase ordering: options before registers, registers before recommendation.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: State the recommended option and explain the reasoning in narrative form, citing at least
two comparison matrix dimensions. Include qualifying conditions.
Architect: Confirm the recommendation is technically viable.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Walk through coverage verification as a narrative discussion. You are reviewing the document
for completeness and surfacing any gaps.

Begin by checking the amendment table for open trigger rules. For each open trigger T-NN,
produce a named finding inline in the narrative using the label format "Finding N: T-NN":
state the criterion ID and name, what the trigger expected, and what is absent or incomplete.
Each open trigger gets its own separately labeled finding entry. Do not bundle two open
triggers into a single finding.

Then discuss E-tier criterion satisfaction — briefly confirm or flag each essential criterion.
Next discuss R-tier satisfaction in the same way. Finally note overall completeness of the
document and whether any follow-up is warranted.

Update the coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-37, exactly 37 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 37)
  T-25 PHASE = FINALIZATION  (fires if finalization verification is not a numbered 4-step list)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" label format)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column
                               as two named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] → [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P×I compound scores in the back-fill target)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution)
```

---

## V-05 — Inertia-Forward + C-36 + C-37 Dual Fail | Axis: Inertia Framing + Combination | Designed fails: C-36 + C-37

**Hypothesis**: An inertia-forward variation that foregrounds the status-quo option will
maintain complete Phase 9b structural compliance — dual-domain enumeration (C-32 PASS),
domain-index prefixes (C-34 PASS), per-site arrow notation (C-35 PASS), prohibition adjacent
to placeholder (C-33 PASS) — but fail both C-36 and C-37 by: (1) Domain 1 transitions list
R-NN IDs without P×I scores (`[R-NN pending] → [R-03, R-07]` — C-35 PASS, C-36 FAIL), and
(2) Domain 2 provides aggregate risk-row attribution without per-column breakdown ("Risk row:
R-NN IDs applied by option" — C-32 PASS, C-37 FAIL). This is the combination variant that
cleanly isolates C-36 and C-37 against a structurally-sound Phase 9b frame. C-22 PASS (CLOSED
BY present), C-24 PASS (37 rows), C-25 PASS (numbered finalization). Two open triggers:
T-36, T-37. Score: 28/30 → 99.33.

```
ROLE SEQUENCE: PM → Architect

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

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare role sequence (PM → Architect) as a typed header. Apply in every phase header.
State the inertia framing principle: "Option A (do-nothing) is evaluated first as the default
trajectory."

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-37. Assign PHASE for each trigger. All STATUS = PENDING at init.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem. Include an inertia cost statement: what happens if no option
is selected and the current state continues.

  PROBLEM: [shared problem statement]
  INERTIA COST: [cost or consequence of maintaining the status quo per unit time]

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Present options in this order: do-nothing first, then alternatives.

For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem — verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve the
        slot. Risk register is built in Phase 3; R-NN IDs will be back-filled in Phase 9b.
        PM notes inertia or adoption risk category. Architect notes technical risk category.
  RATIONALE: [why this option is a candidate]

Option A must be the do-nothing (status-quo) option and must appear first.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build the risk register:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 entries. Inertia-related risks (schedule drift, compounding debt) must appear
for Option A. P and I on a 1-5 scale. Compute P×I.
PM: Add adoption risk entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs from the register into each option RISK field, replacing [R-NN pending].
Update the comparison matrix risk column with applicable register references.

Enumerate citation sites by structural domain:

  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [R-NN IDs applicable to Option A]
    [OPTION-B label] RISK field: [R-NN pending] → [R-NN IDs applicable to Option B]
    [do-nothing label] RISK field: [R-NN pending] → [R-NN IDs applicable to do-nothing]

  Domain 2 — Comparison matrix risk column:
    Risk row: R-NN IDs applied by option. Applicable register entries referenced in risk row.

List each applicable R-NN ID at each Domain 1 site. The risk register carries the full P×I
scores; the register is the authoritative source for compound scoring — option anatomy carries
the register IDs, not redundant score copies.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Comparison matrix — do-nothing (Option A) as first column.
Dimensions: Inertia cost, Implementation effort, Risk (R-NN cited), Time-to-value,
Reversibility, PM adoption friction.
Architect validates technical dimension scoring.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Verify all phase headers carry [GATE: X-NN] citations. Record missing citations in amendment
table.

---

PHASE 6 — COVERAGE TABLE [GATE: C-22]

Coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-37.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Verify: Option A is do-nothing and appears first; registers complete; phases in sequence.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Frame the recommendation against the inertia baseline
(Option A). Cite the sprint or time horizon at which the recommended option recovers its
implementation cost relative to Option A's ongoing inertia cost.
State qualifying conditions.
Architect: Confirm technical feasibility.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review amendment table for STATUS = OPEN triggers.
  For each open trigger T-NN, produce:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing]."
  One finding per trigger. Enumerate sequentially.

Step 2: Verify all E-tier criteria satisfied.
Step 3: Verify all R-tier criteria satisfied.
Step 4: Update coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-37, exactly 37 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 37)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column as
                               two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] → [R-NN entries] transition notation per site)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 transition entries do not include
                               P×I compound scores in the back-fill target — R-NN IDs listed
                               without compound scores fire T-36)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 enumeration does not carry
                               per-option-column R-NN attribution — "R-NN IDs applied by
                               option" without column-level breakdown fires T-37)
```

---

## Predicted Scoring

| Variation | Axis | v13 Fails | A/30 | Composite |
|-----------|------|-----------|------|-----------|
| V-01 | Role sequence | C-36 | 29/30 | **99.67** |
| V-02 | Output format | C-37 | 29/30 | **99.67** |
| V-04 | Phrasing register | C-25 + C-33 | 28/30 | **99.33** |
| V-05 | Inertia framing | C-36 + C-37 | 28/30 | **99.33** |
| V-03 | Lifecycle emphasis | C-24 + C-36 + C-37 | 27/30 | **99.00** |

**V-01 C-36 isolation (1 fail)**: Phase 9b fully structured — C-32 PASS, C-34 PASS, C-35 PASS
(per-site arrows present), C-37 PASS (per-column Domain 2 attribution). Domain 1 transitions
show `[R-NN pending] → [R-03, R-07]` — R-NN IDs present (C-35 PASS) but P×I compound scores
absent from transition target (C-36 FAIL). One open trigger: T-36. Finding 1: T-36. 29/30.

**V-02 C-37 isolation (1 fail)**: Domain 1 fully compliant — per-site arrows with P×I scores
`[R-NN pending] → [R-03 (P:n × I:n = n)]` (C-35 PASS, C-36 PASS). Domain 2 row-level only:
"Risk row: R-NN IDs applied to risk row" — confirms domain presence (C-32 PASS, C-34 PASS)
but provides no per-column attribution (C-37 FAIL). One open trigger: T-37. Finding 1: T-37.
29/30.

**V-04 C-36 + C-37 exemplar in conversational register (2 fails on phrasing axes)**: Phase 9b
demonstrates the ceiling behavior for C-36 and C-37 in conversational style: Domain 1
transitions carry P×I scores (C-36 PASS), Domain 2 carries per-column attribution (C-37 PASS).
Fails are orthogonal to the new criteria: prose finalization (C-25 FAIL) and placeholder
without prohibition (C-33 FAIL). Two open triggers: T-25, T-33. 28/30.

**V-05 C-36 + C-37 dual fail against compliant Phase 9b structure (2 fails on new axes)**:
Phase 9b is structurally sound — C-32 PASS, C-33 PASS, C-34 PASS, C-35 PASS. Fails isolated
to depth criteria: Domain 1 transitions omit P×I (C-36 FAIL), Domain 2 is aggregate without
column labels (C-37 FAIL). Two open triggers: T-36, T-37. 28/30.

**V-03 stale table + three fails**: T-24 fires at PRE-DOCUMENT (35 rows, not 37) — C-24 FAIL.
T-36 and T-37 absent from the 35-row stale table; C-36 and C-37 fail behaviorally (Domain 1
no P×I, Domain 2 row-level only) but produce no named trigger findings. One ordinal finding:
Finding 1: T-24. Three total fails: C-24 + C-36 + C-37. 27/30.

**C-36 discrimination axis confirmed by V-01 and V-05**:
- V-01 provides the cleanest C-36 isolation: C-31 PASS (placeholder), C-32 PASS (both domains),
  C-34 PASS (index prefixes), C-35 PASS (arrow notation), C-37 PASS (per-column Domain 2),
  C-36 FAIL (no P×I in transition target). Single open trigger.
- V-05 provides C-36 fail alongside C-37 fail against a compliant Phase 9b structure.
- Combined evidence: C-36 is independently testable from C-35 — transition notation can be
  present without P×I scores; P×I can be absent from the arrow target even when R-NN IDs
  appear correctly.

**C-37 discrimination axis confirmed by V-02 and V-05**:
- V-02 provides the cleanest C-37 isolation: C-36 PASS (P×I in Domain 1), C-32 PASS, C-34
  PASS, C-35 PASS, C-37 FAIL (Domain 2 row-level only). Single open trigger.
- V-05 provides C-37 fail alongside C-36 fail.
- Combined evidence: C-37 is independently testable from C-32 and C-34 — a variation can
  name Domain 2 (C-32 PASS) and prefix it (C-34 PASS) while providing only aggregate row-level
  confirmation (C-37 FAIL). Per-column attribution is independently required.

**New cascade evidence for R13**:
- C-36 cascade invariant: C-36 requires P×I scores in Domain 1 transition entries. Any
  variation failing C-35 (no arrow notation) also fails C-36 — P×I cannot appear inside
  notation that was never authored. The cascade is deterministic: C-35 FAIL → C-36 FAIL. V-03
  provides the non-cascade case: C-35 PASS, C-36 FAIL (arrows present but no P×I) — confirms
  C-36 can fail independently when C-35 passes.
- C-37 independent fail: V-02 confirms C-37 fails independently of C-32 and C-34. Domain 2
  named and indexed (C-32 PASS, C-34 PASS); confirmation is row-level only (C-37 FAIL). The
  independent fail axis from V-04 R12 (which introduced this pattern) is now reinforced by
  V-02 R13 with the added dimension that C-36 can pass simultaneously.
