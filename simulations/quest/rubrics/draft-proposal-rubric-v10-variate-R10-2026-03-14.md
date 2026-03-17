# draft-proposal Variate — Round 10

Rubric version: v10 · Formula: /24 · New criteria: C-30 (finding ordinal labels), C-31 (forward-reference R-NN placeholder)

Single-axis variations first (V-01..V-04), then inertia-forward combination (V-05).

Axes explored:
- **V-01**: Role sequence (Architect-first, no register linkage) — designed fail: C-23 + C-26 → C-31
- **V-02**: Output format (compact tables, PM-first) — designed fail: C-22
- **V-03**: Lifecycle emphasis (explicit early-gate checks) — designed fail: C-24
- **V-04**: Phrasing register (conversational/narrative) — designed fail: C-25
- **V-05**: Inertia framing (status-quo first, direct register IDs) — designed fail: C-31

Predicted scores: V-01 → 98.75 · V-02..V-05 → 99.58

---

## V-01 — Architect-First | Axis: Role Sequence | Designed fail: C-23 + C-26 (→ C-31)

**Hypothesis**: An Architect-led variation that assesses risk inline per option using P×I notation,
without a separate register-linkage phase, will fail C-23 (no R-NN in RISK fields) and C-26
(no Phase 9b). Because no R-NN usage exists anywhere in the document, the forward-reference
placeholder pattern is also impossible — fails C-31 by cascade. Two triggers open at
finalization: T-23 (C-23: no R-NN in RISK fields) and T-26 (C-26: no Phase 9b). Both findings
carry ordinal labels (C-30 PASS). PHASE column present in amendment table (C-29 PASS).
Trigger count 31 (C-24 PASS).

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Owns option framing, technical risk assessment, register construction, gate
  audit, and feasibility validation.
- PM: Owns business trade-off commentary, adoption risk factors, and recommendation rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) as a typed header at the top of the
output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with the following columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-31 — one per v10 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires (PRE-DOCUMENT,
PRE-OPTION, FINALIZATION, or a named phase). Leave STATUS = PENDING for all rows at init.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

Architect: State the shared problem being decided. This PROBLEM field is shared by all
options and must appear before any option is composed.

PM: Confirm the problem statement captures the business context and urgency.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Compose at least 3 options. One must be a do-nothing or status-quo option. For each option,
produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat from Phase 1]
  RISK: [Architect assesses risk for this option using probability-impact notation.
         Format: "P:[n] × I:[n] = [score] — [risk driver description]."
         PM adds business and adoption risk factors inline.
         Example: "P:3 × I:4 = 12 (High) — integration coupling. PM: adoption friction if
         teams must retrain."]
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Assign P and I scores
on a 1-5 scale. Compute P×I compound score.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Architect: Build a comparison matrix with OPTIONS as column headers.
Matrix rows (dimensions): Effort, Technical risk score, Reversibility, Time-to-value.
PM: Add Adoption friction as a row. Score or characterize each cell consistently.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN] citation
referencing a real criterion ID. List any missing citations and mark them in the amendment
table (STATUS = OPEN for the corresponding T-NN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3 entries,
phases appear in declared sequence.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-31.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions for the recommendation.
Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry using this format:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."
  Enumerate findings sequentially (Finding 1, Finding 2, ...). Do not bundle two open
  triggers into a single finding entry.

Step 2: Verify all E-tier criteria are satisfied. Update coverage table STATUS for any
  E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria are satisfied. Update coverage table STATUS for any
  R-tier criterion found incomplete.

Step 4: Confirm the coverage table is fully populated. Set COMPLETION STATUS of the
  amendment table to the final state.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-31 — exactly 31 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
PHASE column: populated for every row. Examples:
  T-01 PHASE = PRE-DOCUMENT
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage)
  T-24 PHASE = FINALIZATION  (fires if amendment table row count != 31)
  T-26 PHASE = FINALIZATION  (fires if no dedicated risk-propagation phase present)
  T-30 PHASE = FINALIZATION  (fires if finding entries lack "Finding N: T-NN" header format)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no forward-reference placeholder)

At document completion, update STATUS for any trigger that fired.
```

---

## V-02 — PM-First, Compact Tables | Axis: Output Format | Designed fail: C-22

**Hypothesis**: A compact-table variation with PM leading will omit the CLOSED BY column from
the coverage table (treating it as metadata overhead in a compact format), failing C-22.
All register-linkage and propagation behavior is intact: R-NN placeholder at Phase 2,
Phase 9b back-fill, ordinal finding labels. One open trigger: T-22 (CLOSED BY column absent).
Finding carries "Finding 1: T-22" label (C-30 PASS). Trigger count 31 (C-24 PASS).

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

OUTPUT FORMAT: Compact tables throughout. Minimize prose between tables.
Use concise cell values. Each phase produces a table or structured block, not paragraphs.

ROLE ASSIGNMENTS:
- PM: Leads business framing, option business cases, recommendation rationale, and
  adoption risk.
- Architect: Validates technical constraints, owns risk register entries, and confirms
  technical feasibility.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare role sequence (PM → Architect) as a typed header. Apply in every phase header.

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-31. Assign each trigger a PHASE value. All STATUS = PENDING at init.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: One-sentence problem statement. Compact block:
  PROBLEM: [shared problem for all options]
  DECISION REQUIRED: [what must be chosen]
  WHY NOW: [urgency or cost of inaction]

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

For each option (minimum 3, including do-nothing), produce a compact option block:

  OPTION: [label and brief description]
  PROBLEM: [shared problem — repeat verbatim from Phase 1]
  RISK: [R-NN pending] — back-filled after risk register. Note risk category:
        "adoption barrier" / "schedule risk" / "technical coupling" / etc.
        PM adds business risk label. Architect adds technical risk label.
  RATIONALE: [one-sentence: why this option is a candidate]

Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve the slot.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Compact risk register table:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 entries. P and I on 1-5 scale. P×I computed.
PM: Add 1-2 adoption or schedule risk entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

For each option, state which R-NN entries apply:
  Option A RISK: [R-NN pending] → R-01, R-03 (P×I: 12, 8)
  Option B RISK: [R-NN pending] → R-02, R-04 (P×I: 6, 10)
  Option C (do-nothing) RISK: [R-NN pending] → R-05 (P×I: 15)

Enumerate citation sites visited: option RISK fields (by option label),
comparison matrix risk column (by column label).
Confirm R-NN formula applied at each site.

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

Compact coverage table — columns: CRITERION | STATUS
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-31.
STATUS = PASS or FAIL. Keep the table minimal — status only.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Confirm: options >= 3, do-nothing present, risk register entries >= 3, Phase 9b complete.

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

T-01..T-31, exactly 31 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 31)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
```

---

## V-03 — Lifecycle-Heavy | Axis: Lifecycle Emphasis | Designed fail: C-24

**Hypothesis**: A variation emphasizing explicit lifecycle gate checks at every phase transition
will build its amendment table from the v9 rubric criteria list (C-01..C-29, producing 29
rows) rather than the updated v10 count of 31. T-24 is assigned PHASE = PRE-DOCUMENT, so
the count mismatch fires immediately at the opening gate — it is the first trigger checked.
One open trigger at finalization: T-24. Finding carries "Finding 1: T-24" (C-30 PASS). CLOSED
BY column present (C-22 PASS). R-NN placeholder at Phase 2 (C-31 PASS). Phase 9b present
(C-26 PASS).

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

LIFECYCLE DESIGN: Every phase transition includes an explicit gate check before proceeding.
PRE-DOCUMENT checks run before any content is authored. Failures detected early are recorded
as OPEN triggers in the amendment table and reported in finalization.

ROLE ASSIGNMENTS:
- Architect: Owns phase gate checks, register construction, technical options, and audit steps.
- PM: Owns business options, adoption trade-offs, and recommendation rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare role sequence (Architect → PM) as a typed header.

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Build trigger rules from the current rubric criteria. Assign each trigger a PHASE value.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

Use this criteria list for trigger construction: C-01 through C-29.
Each criterion in the list generates one trigger row (T-01..T-29). Total: 29 rows.

PHASE column: T-24 PHASE = PRE-DOCUMENT (trigger fires early if row count mismatches).

PRE-DOCUMENT GATE CHECK — run immediately after table initialization:
  Check T-24: Does the amendment table row count equal the expected v10 criterion count?
  If count != expected, set T-24 STATUS = OPEN.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PRE-PHASE CHECK: Confirm role sequence is declared (T-01). Confirm amendment table is
initialized (T-18). If either fails, record in amendment table before proceeding.

Architect: State the shared problem.
PM: Confirm business context.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PRE-OPTION CHECK: Confirm problem statement complete. Confirm amendment table initialized.

For each option (minimum 3, including do-nothing), produce:

  OPTION: [label and description]
  PROBLEM: [shared problem — verbatim from Phase 1]
  RISK: [R-NN pending] — placeholder for register linkage, resolved in Phase 9b.
        Architect notes risk category and vectors. PM notes adoption risk.
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

POST-OPTION CHECK: Verify option count >= 3, do-nothing present.

Architect: Risk register:
  R-NN | RISK | P | I | P×I | MITIGATION
At least 3 entries. 1-5 scale.
PM: Add adoption and schedule risks.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields from [R-NN pending] placeholders.
Enumerate each citation site visited by option label.
Confirm R-NN formula applied at comparison matrix risk column.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

POST-REGISTER CHECK: Confirm risk register >= 3 entries.

Comparison matrix — OPTIONS as column headers.
Rows: Effort | Risk (R-NN cited) | Time-to-value | Reversibility | PM adoption risk.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Audit all phase headers for [GATE: X-NN] citations. Record missing citations in
amendment table.

---

PHASE 6 — COVERAGE TABLE [GATE: C-22]

Coverage table columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-31.
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

Build from criteria list C-01..C-29. Total rows: 29 (T-01..T-29).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != expected count)
  Note: Expected count for v10 = 31; this table has 29 rows → T-24 fires at PRE-DOCUMENT.
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
```

---

## V-04 — Conversational Register | Axis: Phrasing Register | Designed fail: C-25

**Hypothesis**: A conversational-register variation will perform finalization verification as a
continuous prose narrative ("walk through" framing), explicitly avoiding numbered steps.
Finding ordinal labels are still produced in "Finding N: T-NN" format — the labels appear as
inline identifiers within the narrative, satisfying C-30. One open trigger at finalization:
T-25 (C-25: prose finalization without numbered steps). Trigger count 31 (C-24 PASS). Phase
9b present (C-26 PASS). R-NN placeholder at Phase 2 (C-31 PASS). CLOSED BY column present
(C-22 PASS).

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
Populate T-01..T-31 (31 trigger rules, one per v10 criterion). Assign PHASE for each.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: Open with a brief framing paragraph that explains the problem, why it matters now,
and what decision needs to be made. Then state the PROBLEM field explicitly:

  PROBLEM: [concise problem statement shared by all options]

Architect: Add a sentence on any technical constraints that shape the decision space.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Present each option (minimum 3, including do-nothing) in a narrative block. For each option,
include all four anatomy fields in conversational form:

  OPTION: [label and description — PM introduces the option's value proposition]
  PROBLEM: [repeat the shared problem statement]
  RISK: [R-NN pending] — Placeholder for risk register linkage; will be resolved in Phase 9b.
        For now, PM names the key adoption concern; Architect names the key technical concern.
        Example: "[R-NN pending] — PM: high switching cost for teams. Architect: requires
        async coordination across two services."
  RATIONALE: [PM explains why this option belongs in the shortlist]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Construct the risk register as a table:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 entries. Use a 1-5 scale for P and I. Compute P×I.
PM: Add 1-2 adoption risk entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Walk through each option's RISK field and replace [R-NN pending] with the
applicable R-NN identifiers from the register. Then update the comparison matrix risk column.

Enumerate each citation site visited: state option label, updated RISK field, and R-NN IDs
applied. Confirm the comparison matrix risk column references R-NN IDs.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Present a comparison matrix with OPTIONS as column headers.
Dimensions: Effort, Risk (R-NN cited), Time-to-value, Reversibility, PM adoption risk.
PM leads dimension selection; Architect validates scoring.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify phase headers carry [GATE: X-NN] citations. Note any missing in the
amendment table.

---

PHASE 6 — COVERAGE TABLE [GATE: C-22]

Build a coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-31.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Verify phase ordering: options before registers, registers before recommendation.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: State the recommended option and explain the reasoning in narrative form, citing at
least two comparison matrix dimensions. Include qualifying conditions.
Architect: Confirm the recommendation is technically viable.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Walk through coverage verification as a narrative discussion. You are reviewing the document
for completeness and surfacing any gaps.

Begin by checking the amendment table for any trigger rules that remain open. For each open
trigger T-NN, produce a named finding inline in the narrative using the label format
"Finding N: T-NN": state the criterion ID and name, what the trigger expected, and what is
absent or incomplete. Each open trigger gets its own separately labeled finding entry.

Then discuss E-tier criterion satisfaction — briefly confirm or flag each essential criterion.
Next, discuss R-tier satisfaction in the same way. Finally, note the overall completeness
of the document and whether any follow-up is warranted.

Update the coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-31, exactly 31 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 31)
T-25 PHASE = FINALIZATION  (fires if finalization verification is not a numbered 4-step list)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
```

---

## V-05 — Inertia-Forward | Axis: Inertia Framing + Direct Register IDs | Designed fail: C-31

**Hypothesis**: A variation that foregrounds the status-quo option and writes resolved R-NN
identifiers directly into Phase 2 RISK fields (rather than forward-reference placeholders)
will fail C-31. The document passes C-23 because final RISK fields do contain R-NN IDs; Phase
9b is present and confirms propagation sites (C-26 PASS); the two-phase
declaration-resolution process is bypassed because identifiers were already finalized at
composition time. T-31 fires at finalization. One open trigger: T-31. Finding carries
"Finding 1: T-31" (C-30 PASS). CLOSED BY column present (C-22 PASS). 31 trigger rows
(C-24 PASS). Numbered 4-step finalization (C-25 PASS).

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

INERTIA FRAMING: Open by foregrounding inaction as the default path. The do-nothing option
represents the current trajectory and must be evaluated first, before alternatives. Every
option is implicitly competing against the cost of not acting. The do-nothing option appears
as Option A in the option list and in the first column of the comparison matrix.

ROLE ASSIGNMENTS:
- PM: Leads business case framing, inertia cost analysis, and recommendation.
- Architect: Owns technical risk identification, register construction, and feasibility.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare role sequence (PM → Architect) as a typed header. Apply in every phase header.
State the inertia framing principle: "Option A (do-nothing) is evaluated first as the
default trajectory."

Initialize amendment tracking table:
  ID | TRIGGER | CONDITION | STATUS | PHASE
Populate T-01..T-31. Assign PHASE for each trigger.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem. Include an inertia cost statement: what happens if no option
is selected and the current state continues.

  PROBLEM: [shared problem statement]
  INERTIA COST: [cost or consequence of maintaining the status quo per unit time]

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Present options in this order: do-nothing first, then alternatives.

For each option, produce an entry with all four anatomy fields. In the RISK field, cite
the applicable R-NN identifiers directly — the risk register is built in Phase 3, but the
identifiers for this topic area are well-known; cite them now for each option's risk profile:

  OPTION A — Do-nothing (status quo):
    OPTION: [description of the current trajectory]
    PROBLEM: [shared problem — verbatim from Phase 1]
    RISK: R-01, R-03 (inertia accumulation, P:3 × I:5 = 15; schedule drift, P:4 × I:3 = 12)
          PM: each sprint without action compounds switching costs.
          Architect: technical debt accumulates in current approach.
    RATIONALE: The default path — no implementation cost, but carries ongoing inertia cost.

  OPTION B — [alternative 1]:
    OPTION: [description]
    PROBLEM: [shared problem]
    RISK: R-02, R-04 (integration coupling, P:2 × I:4 = 8; team ramp-up, P:3 × I:3 = 9)
          PM: one-time adoption friction. Architect: two-service coordination required.
    RATIONALE: [why this option is a candidate]

  OPTION C — [alternative 2]:
    OPTION: [description]
    PROBLEM: [shared problem]
    RISK: R-01, R-05 (inertia baseline, P:2 × I:3 = 6; migration cost, P:2 × I:4 = 8)
          PM: lower adoption barrier. Architect: lower technical risk.
    RATIONALE: [why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Formalize the risk register, confirming the R-NN entries cited in Phase 2:
  R-NN | RISK | P | I | P×I | MITIGATION

Entries must include R-01 through R-05 (or however many were cited in Phase 2 RISK fields).
PM: Add any additional adoption risk entries not yet captured.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Verify that each option RISK field cites the correct R-NN entries from the
register. Confirm the comparison matrix risk column references R-NN IDs.

Enumerate citation sites visited:
  Option A RISK: cites R-01, R-03 — confirmed
  Option B RISK: cites R-02, R-04 — confirmed
  Option C RISK: cites R-01, R-05 — confirmed
  Comparison matrix risk column: R-NN cited by column — confirmed

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Comparison matrix — do-nothing (Option A) as first column.
Dimensions: Inertia cost, Implementation effort, Risk (R-NN cited), Time-to-value,
Reversibility, PM adoption friction.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Verify all phase headers carry [GATE: X-NN] citations. Record missing citations in amendment
table.

---

PHASE 6 — COVERAGE TABLE [GATE: C-22]

Coverage table: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-31.

---

PHASE 7 — PREREQUISITES CHECK [GATE: R-02]

Verify: registers complete, phases in sequence, do-nothing option is Option A.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Frame the recommendation against the inertia baseline
(Option A). Cite the sprint or time horizon at which Option B or C recovers its
implementation cost relative to the inertia cost of Option A.
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

T-01..T-31, exactly 31 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 31)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder
                             — direct R-NN IDs at Phase 2 without a placeholder stage fires T-31)
```

---

## Predicted Scoring

| Variation | Axis | Designed Fail | C-23 | C-26 | C-31 | Other fails | A score | Composite |
|-----------|------|---------------|------|------|------|-------------|---------|-----------|
| V-01 | Role sequence | C-23 + C-26 → C-31 | FAIL | FAIL | FAIL | — | 21/24 | **98.75** |
| V-02 | Output format | C-22 | PASS | PASS | PASS | C-22 | 23/24 | **99.58** |
| V-03 | Lifecycle emphasis | C-24 | PASS | PASS | PASS | C-24 | 23/24 | **99.58** |
| V-04 | Phrasing register | C-25 | PASS | PASS | PASS | C-25 | 23/24 | **99.58** |
| V-05 | Inertia framing | C-31 | PASS | PASS | FAIL | — | 23/24 | **99.58** |

**V-01 cascade path**: No R-NN usage at all (C-23 fail) → no Phase 9b (C-26 fail) → no
placeholder syntax and no back-fill phase (C-31 fail). Two open triggers at finalization:
T-23 and T-26. Both carry ordinal labels (C-30 PASS).

**V-05 distinction from V-01**: V-05 has Phase 9b and R-NN IDs in final RISK fields (both
C-23 and C-26 pass); fails only C-31 because R-NN IDs were written directly at Phase 2 rather
than as forward-reference placeholders resolved in Phase 9b.

**New C-30/C-31 coverage**: C-30 is exercised positively in all five variations. C-31 is
exercised negatively in V-01 (cascade) and V-05 (direct-ID pattern). A future variation
designed to fail C-30 (findings enumerated without ordinal header labels) and a variation
designed to fail C-30 + C-31 simultaneously would extend coverage.
