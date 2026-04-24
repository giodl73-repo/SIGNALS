# draft-proposal Variate — Round 11

Rubric version: v11 · Formula: /26 · New criteria: C-32 (Phase 9b dual-domain citation-site
enumeration), C-33 (Phase 2 RISK explicit prohibition instruction)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Role sequence (Architect-first, no register linkage) — designed fail: C-23 cascade → C-26, C-31, C-32, C-33
- **V-02**: Output format (compact tables, PM-first) — designed fail: C-22 (C-32 + C-33 PASS in this variation)
- **V-03**: Lifecycle emphasis (stale trigger count) — designed fail: C-24 + C-32 + C-33
- **V-04**: Phrasing register (conversational) + C-33 isolation — designed fail: C-25 + C-33 (C-32 PASS)
- **V-05**: Inertia framing + C-32 isolation — designed fail: C-32 alone (C-31 + C-33 PASS)

Predicted scores: V-01 → 98.08 · V-02 → 99.62 · V-03 → 98.85 · V-04 → 99.23 · V-05 → 99.62

---

## V-01 — Architect-First | Axis: Role Sequence | Designed fail: C-23 cascade → C-26, C-31, C-32, C-33

**Hypothesis**: An Architect-led variation that assesses risk inline per option using P×I
notation, without a separate register-linkage phase, will fail C-23 (no R-NN in RISK fields).
Because no R-NN usage exists anywhere in the document, no Phase 9b is authored (C-26 fail),
no forward-reference placeholder pattern is possible (C-31 fail by cascade), no Phase 9b
exists to enumerate citation sites (C-32 fail by cascade), and no Phase 2 template has
placeholder syntax adjacent to a prohibition instruction (C-33 fail by cascade). Five triggers
open at finalization: T-23, T-26, T-31, T-32, T-33. Each finding carries "Finding N: T-NN"
ordinal label (C-30 PASS). PHASE column present (C-29 PASS). Trigger count 33 (C-24 PASS).
CLOSED BY column present (C-22 PASS). Numbered 4-step finalization (C-25 PASS).

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

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-33 — one per v11 rubric criterion. Each row must carry a
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
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-33.
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

Trigger rules T-01..T-33 — exactly 33 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
PHASE column: populated for every row. Examples:
  T-01 PHASE = PRE-DOCUMENT
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage)
  T-24 PHASE = FINALIZATION  (fires if amendment table row count != 33)
  T-26 PHASE = FINALIZATION  (fires if no dedicated risk-propagation phase present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name
                               option RISK fields by option label AND comparison matrix
                               risk column as two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                               P×I" prohibition instruction adjacent to placeholder directive)

At document completion, update STATUS for any trigger that fired.
```

---

## V-02 — PM-First, Compact Tables | Axis: Output Format | Designed fail: C-22

**Hypothesis**: A compact-table variation with PM leading will omit the CLOSED BY column from
the coverage table (treating it as metadata overhead in a compact format), failing C-22.
All register-linkage, propagation, prohibition, and dual-domain enumeration behavior is
intact: C-33 PASS ("Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to
reserve the slot."), C-32 PASS (Phase 9b names both structural domains explicitly: "Domain 1
— option RISK fields by option label" and "Domain 2 — comparison matrix risk column"),
C-31 PASS (placeholder at Phase 2, back-filled in Phase 9b). One open trigger: T-22 (CLOSED
BY column absent). Finding carries "Finding 1: T-22" label (C-30 PASS). Trigger count 33
(C-24 PASS). Numbered 4-step finalization (C-25 PASS).

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
Populate T-01..T-33. Assign each trigger a PHASE value. All STATUS = PENDING at init.

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
        the slot. Note risk category only: "adoption barrier" / "schedule risk" /
        "technical coupling" / etc.
        PM notes business risk category. Architect notes technical risk category.
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
    [OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [OPTION-B label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [do-nothing option label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [R-NN IDs inserted per option column]

Confirm P×I formula applied at each named domain site.

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-33.
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

T-01..T-33, exactly 33 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 33)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name option RISK fields
                             by option label AND comparison matrix risk column as two named
                             structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
```

---

## V-03 — Lifecycle-Heavy | Axis: Lifecycle Emphasis | Designed fail: C-24 + C-32 + C-33

**Hypothesis**: A variation emphasizing explicit lifecycle gate checks at every phase
transition will build its amendment table from the v10 rubric criteria list (C-01..C-31,
producing 31 rows) rather than the updated v11 count of 33. T-24 is assigned PHASE =
PRE-DOCUMENT, so the count mismatch fires immediately at the opening gate — it is the first
trigger checked. One open trigger at finalization: T-24. Finding carries "Finding 1: T-24"
(C-30 PASS). CLOSED BY column present (C-22 PASS). R-NN placeholder at Phase 2 (C-31 PASS).
Phase 9b present (C-26 PASS). However, Phase 9b enumerates "each citation site visited by
option label" without naming the comparison matrix risk column as a structural domain (C-32
FAIL — single-domain enumeration). Phase 2 RISK carries "[R-NN pending] — placeholder for
register linkage, resolved in Phase 9b" with no adjacent prohibition instruction (C-33 FAIL
— placeholder present, prohibition absent). T-32 and T-33 do not exist in the 31-row table,
so they cannot fire; C-32 and C-33 fail the rubric behavioral evaluation independently.
Numbered 4-step finalization (C-25 PASS).

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

Use this criteria list for trigger construction: C-01 through C-31.
Each criterion in the list generates one trigger row (T-01..T-31). Total: 31 rows.

PHASE column: T-24 PHASE = PRE-DOCUMENT (trigger fires early if row count mismatches).

PRE-DOCUMENT GATE CHECK — run immediately after table initialization:
  Check T-24: Does the amendment table row count equal the expected v11 criterion count?
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

Build from criteria list C-01..C-31. Total rows: 31 (T-01..T-31).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != expected count)
  Note: Expected count for v11 = 33; this table has 31 rows → T-24 fires at PRE-DOCUMENT.
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
```

---

## V-04 — Conversational Register + C-33 Isolation | Axis: Phrasing Register | Designed fail: C-25 + C-33

**Hypothesis**: A conversational-register variation will perform finalization verification as a
continuous prose narrative ("walk through" framing), explicitly avoiding numbered steps (C-25
FAIL). Phase 9b enumerates citation sites using explicit structural domain labels — "(1) option
RISK fields by option label" and "(2) comparison matrix risk column" — satisfying C-32 (C-32
PASS). Phase 2 RISK carries "[R-NN pending] — Placeholder for risk register linkage; will be
resolved in Phase 9b" with no "Do not compute P×I" prohibition adjacent (C-33 FAIL —
placeholder present, prohibition absent). This variation isolates C-33: the only difference
from a C-33 PASS document is the absence of the prohibition instruction in the Phase 2
template. Finding ordinal labels are still produced in "Finding N: T-NN" format within the
narrative (C-30 PASS). Two open triggers at finalization: T-25 and T-33. Trigger count 33
(C-24 PASS). CLOSED BY column present (C-22 PASS). Score: 24/26 → 99.23.

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
Populate T-01..T-33 (33 trigger rules, one per v11 criterion). Assign PHASE for each.

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

Architect: Walk through each option's RISK field and replace the [R-NN pending] placeholder
with the applicable R-NN identifiers from the register. Then update the comparison matrix
risk column.

Enumerate citation sites by structural domain:
  (1) Option RISK fields (by option label) — for each option, state the option label and
      the R-NN IDs applied to its RISK field.
  (2) Comparison matrix risk column — confirm R-NN IDs are present in the risk row.

Confirm P×I formula applied at each domain site.

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-33.

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
absent or incomplete. Each open trigger gets its own separately labeled finding entry. Do not
bundle two open triggers into a single finding.

Then discuss E-tier criterion satisfaction — briefly confirm or flag each essential criterion.
Next, discuss R-tier satisfaction in the same way. Finally, note the overall completeness
of the document and whether any follow-up is warranted.

Update the coverage table to final state.

---

AMENDMENT TABLE SPECIFICATION

T-01..T-33, exactly 33 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 33)
T-25 PHASE = FINALIZATION  (fires if finalization verification is not a numbered 4-step list)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
```

---

## V-05 — Inertia-Forward + C-32 Isolation | Axis: Inertia Framing | Designed fail: C-32 alone

**Hypothesis**: A variation that foregrounds the status-quo option and uses back-fill mode
(C-31 PASS: placeholder at Phase 2 with prohibition instruction adjacent — C-33 PASS) will
fail C-32 alone when Phase 9b enumerates citation sites generically ("all [R-NN pending]
placeholders resolved; back-fill complete") without naming individual option RISK fields by
label or the comparison matrix risk column as a named structural domain. The document passes
C-26 (Phase 9b present, citation-site inventory present — "back-fill complete" is an inventory
statement), passes C-31 (placeholder present at Phase 2, resolved in Phase 9b), and passes
C-33 (prohibition instruction present adjacent to placeholder directive). It fails C-32
because the citation-site inventory is a one-line aggregate confirmation rather than a
structural-domain enumeration with option labels and matrix column named explicitly. One open
trigger: T-32. Finding carries "Finding 1: T-32" (C-30 PASS). CLOSED BY column present
(C-22 PASS). Trigger count 33 (C-24 PASS). Numbered 4-step finalization (C-25 PASS).
Score: 25/26 → 99.62.

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
Populate T-01..T-33. Assign PHASE for each trigger. All STATUS = PENDING at init.

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
for Option A. P and I on a 1-5 scale.
PM: Add adoption risk entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs from the register into all option RISK field placeholders, replacing
[R-NN pending] with the applicable register entries.

After back-filling, confirm the comparison matrix risk column is updated with R-NN IDs.

Citation-site enumeration: all [R-NN pending] placeholders resolved; R-NN IDs back-filled
from register; comparison matrix risk column updated. Back-fill complete.

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-33.

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

T-01..T-33, exactly 33 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 33)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains — aggregate confirmation
                             "back-fill complete" without named domains fires T-32)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
```

---

## Predicted Scoring

| Variation | Axis | Designed Fail | C-22 | C-23 | C-24 | C-25 | C-26 | C-31 | C-32 | C-33 | A score | Composite |
|-----------|------|---------------|------|------|------|------|------|------|------|------|---------|-----------|
| V-01 | Role sequence | C-23 cascade | PASS | FAIL | PASS | PASS | FAIL | FAIL | FAIL | FAIL | 21/26 | **98.08** |
| V-02 | Output format | C-22 | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 25/26 | **99.62** |
| V-03 | Lifecycle emphasis | C-24 + C-32 + C-33 | PASS | PASS | FAIL | PASS | PASS | PASS | FAIL | FAIL | 23/26 | **98.85** |
| V-04 | Phrasing register | C-25 + C-33 | PASS | PASS | PASS | FAIL | PASS | PASS | PASS | FAIL | 24/26 | **99.23** |
| V-05 | Inertia + C-32 isolation | C-32 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | 25/26 | **99.62** |

**V-01 cascade path**: No R-NN usage (C-23 fail) → no Phase 9b (C-26 fail) → no placeholder
syntax (C-31 fail by cascade) → no Phase 9b to enumerate domains (C-32 fail by cascade) →
no placeholder pattern so no prohibition co-location possible (C-33 fail by cascade).
Five open triggers: T-23, T-26, T-31, T-32, T-33. Five ordinal-labeled findings. 21/26.

**V-02 as C-32+C-33 exemplar**: Phase 2 template embeds "Do not compute P×I in Phase 2 RISK
fields. Declare [R-NN pending] to reserve the slot." (C-33 PASS). Phase 9b enumerates by
"Domain 1 — Option RISK fields (by option label)" and "Domain 2 — Comparison matrix risk
column" (C-32 PASS). One open trigger: T-22 (CLOSED BY absent). 25/26.

**V-03 stale table**: Amendment table uses C-01..C-31 (31 rows, v10 count). T-32 and T-33
do not exist in the table. T-24 fires at PRE-DOCUMENT (31 != 33). Phase 9b uses single-domain
enumeration ("by option label" only, with matrix column as a confirmation not a named domain)
→ C-32 FAIL. No prohibition adjacent to placeholder → C-33 FAIL. Three criteria fail; one
T-NN finding (T-24). 23/26.

**V-04 C-33 isolation**: Phase 9b names both structural domains explicitly (C-32 PASS). Phase
2 RISK placeholder present (C-31 PASS) but no prohibition instruction (C-33 FAIL). Prose
finalization produces ordinal-labeled findings inline (C-30 PASS) but not as a numbered 4-step
list (C-25 FAIL). Two open triggers: T-25 and T-33. New composite tier: 24/26 → 99.23.

**V-05 C-32 isolation**: Phase 2 template carries prohibition + placeholder (C-31 PASS,
C-33 PASS). Phase 9b back-fills placeholders. Citation-site enumeration is a single-line
aggregate ("all [R-NN pending] placeholders resolved; back-fill complete") — no option labels
named, no matrix column named as a domain (C-32 FAIL). One open trigger: T-32. 25/26.
The C-32 failure mode here is distinct from V-03: V-03 is a verification pass that names
option labels but omits the matrix column; V-05 is a back-fill pass that names neither domain.

**New composite tier introduced**: V-04 scores 24/26 → aspirational 9.23 → composite 99.23.
This tier sits between 23/26 (98.85, three aspratational fails) and 25/26 (99.62, one
aspirational fail). R11 is the first round to populate this tier.

**C-32 isolation coverage**: V-05 demonstrates C-32 can fail while C-26, C-31, C-33 all pass
(back-fill mode, prohibition present, Phase 9b present, but enumeration generic). Combined
with V-02 (C-32 PASS exemplar), the rubric has isolation evidence in both directions for C-32.

**C-33 isolation coverage**: V-04 demonstrates C-33 can fail while C-32 passes (dual-domain
Phase 9b present, but Phase 2 template omits prohibition). Combined with V-02 (C-33 PASS
exemplar), the rubric has isolation evidence in both directions for C-33.
