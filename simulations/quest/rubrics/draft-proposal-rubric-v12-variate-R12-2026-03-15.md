# draft-proposal Variate — Round 12

Rubric version: v12 · Formula: /28 · New criteria: C-34 (Phase 9b domain-indexed labels),
C-35 (Phase 9b back-fill arrow notation)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Role sequence (Architect-first, no register linkage) — designed fail: C-23 cascade
  → C-26, C-31, C-32, C-33, C-34, C-35 (seven fails)
- **V-02**: Output format (compact tables, PM-first) — designed fail: C-22
  (C-34 + C-35 PASS in this variation)
- **V-03**: Lifecycle emphasis (stale trigger count: 31 rows) — designed fail: C-24 + C-32
  + C-33 + C-34 + C-35
- **V-04**: Phrasing register (conversational) + C-35 isolation — designed fail: C-25 + C-33
  + C-35 (C-34 PASS via ordinal "(1)"/"(2)" prefix form)
- **V-05**: Inertia framing + aggregate Phase 9b — designed fail: C-32 + C-34 + C-35
  (C-33 PASS)

Predicted scores: V-02 → 99.64 · V-04 → 98.93 · V-05 → 98.93 · V-03 → 98.21 · V-01 → 97.50

---

## V-01 — Architect-First | Axis: Role Sequence | Designed fail: C-23 cascade → C-26, C-31, C-32, C-33, C-34, C-35 (seven fails)

**Hypothesis**: An Architect-led variation that assesses risk inline per option using P×I
notation, without a separate register-linkage phase, will fail C-23 (no R-NN in RISK fields).
Because no R-NN usage exists anywhere in the document, no Phase 9b is authored (C-26 fail),
no forward-reference placeholder pattern is possible (C-31 fail by cascade), no Phase 9b
exists to enumerate citation sites (C-32 fail by cascade), no domain-index labels are
possible (C-34 fail by cascade), no per-site arrow notation is possible (C-35 fail by
cascade), and no Phase 2 template has placeholder syntax adjacent to a prohibition instruction
(C-33 fail by cascade). Seven triggers open at finalization: T-23, T-26, T-31, T-32, T-33,
T-34, T-35. Each finding carries "Finding N: T-NN" ordinal label (C-30 PASS). PHASE column
present (C-29 PASS). Trigger count 35 (C-24 PASS). CLOSED BY column present (C-22 PASS).
Numbered 4-step finalization (C-25 PASS). Score: 21/28 → 97.50.

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

Populate trigger rules T-01..T-35 — one per v12 rubric criterion. Each row must carry a
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-35.
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

Trigger rules T-01..T-35 — exactly 35 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
PHASE column: populated for every row. Examples:
  T-01 PHASE = PRE-DOCUMENT
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 35)
  T-26 PHASE = FINALIZATION  (fires if no dedicated risk-propagation phase present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name
                               option RISK fields by option label AND comparison matrix
                               risk column as two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                               P×I" prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix on each domain entry — "Domain N —" or equivalent
                               ordinal-indexed form required)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                               [R-NN pending] → [R-NN entries] transition notation per site)

At document completion, update STATUS for any trigger that fired.
```

---

## V-02 — PM-First, Compact Tables | Axis: Output Format | Designed fail: C-22

**Hypothesis**: A compact-table variation with PM leading will omit the CLOSED BY column from
the coverage table (treating it as metadata overhead in a compact format), failing C-22. All
register-linkage, propagation, prohibition, dual-domain enumeration, domain-index labeling,
and per-site arrow notation behavior is intact: C-33 PASS ("Do not compute P×I in Phase 2
RISK fields. Declare [R-NN pending] to reserve the slot."), C-32 PASS (Phase 9b names both
structural domains explicitly), C-34 PASS (Phase 9b uses "Domain 1 —" and "Domain 2 —"
numeric index prefixes), C-35 PASS (Phase 9b shows "[R-NN pending] → [applicable R-NN
entries, P×I scores]" arrow notation per citation site), C-31 PASS (placeholder at Phase 2,
back-filled in Phase 9b). One open trigger: T-22 (CLOSED BY column absent). Finding carries
"Finding 1: T-22" label (C-30 PASS). Trigger count 35 (C-24 PASS). Numbered 4-step
finalization (C-25 PASS). Score: 27/28 → 99.64.

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
Populate T-01..T-35. Assign each trigger a PHASE value. All STATUS = PENDING at init.

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-35.
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

T-01..T-35, exactly 35 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 35)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name option RISK fields
                             by option label AND comparison matrix risk column as two named
                             structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix on each domain entry — "Domain N —" or equivalent
                             ordinal-indexed form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                             [R-NN pending] → [R-NN entries] transition notation per site)
```

---

## V-03 — Lifecycle-Heavy | Axis: Lifecycle Emphasis | Designed fail: C-24 + C-32 + C-33 + C-34 + C-35

**Hypothesis**: A variation emphasizing explicit lifecycle gate checks at every phase
transition will build its amendment table from the v10 rubric criteria list (C-01..C-31,
producing 31 rows) rather than the current v12 count of 35. T-24 fires immediately at
PRE-DOCUMENT (31 != 35). Phase 9b enumerates "each citation site visited by option label"
without naming the comparison matrix risk column as a second structural domain, and without
domain-index prefixes or per-site arrow notation (C-32 FAIL — single-domain enumeration,
C-34 FAIL — no index prefix on any domain entry, C-35 FAIL — no transition notation at
citation sites). Phase 2 RISK carries "[R-NN pending] — placeholder for register linkage,
resolved in Phase 9b" with no adjacent prohibition instruction (C-33 FAIL — placeholder
present, prohibition absent). T-32 through T-35 do not exist in the 31-row table, so they
cannot fire as named triggers; C-32, C-33, C-34, C-35 fail the rubric behavioral evaluation
independently. One T-NN finding produced at finalization (Finding 1: T-24). CLOSED BY column
present (C-22 PASS). R-NN placeholder at Phase 2 (C-31 PASS). Numbered 4-step finalization
(C-25 PASS). Score: 23/28 → 98.21.

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

Use this criteria list for trigger construction: C-01 through C-31.
Each criterion in the list generates one trigger row (T-01..T-31). Total: 31 rows.

PHASE column: T-24 PHASE = PRE-DOCUMENT (trigger fires early if row count mismatches).

PRE-DOCUMENT GATE CHECK — run immediately after table initialization:
  Check T-24: Does the amendment table row count equal the expected v12 criterion count?
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

Build from criteria list C-01..C-31. Total rows: 31 (T-01..T-31).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != expected count)
  Note: Expected count for v12 = 35; this table has 31 rows → T-24 fires at PRE-DOCUMENT.
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
```

---

## V-04 — Conversational Register + C-35 Isolation | Axis: Phrasing Register | Designed fail: C-25 + C-33 + C-35

**Hypothesis**: A conversational-register variation will perform finalization verification as a
continuous prose narrative ("walk through" framing), explicitly avoiding numbered steps
(C-25 FAIL). Phase 9b enumerates citation sites using explicit structural domain labels with
ordinal numeric prefixes — "(1) Option RISK fields by option label" and "(2) Comparison matrix
risk column" — satisfying C-32 (both domains named) and C-34 (the "(1)"/"(2)" ordinal form is
an accepted numeric-indexed form for C-34). Phase 9b states only the outcome at each option
site ("the R-NN IDs applied to its RISK field") without showing the [R-NN pending] → [R-NN
IDs] state transition (C-35 FAIL — per-site transition notation absent). Phase 2 RISK carries
"[R-NN pending] — Placeholder for risk register linkage; will be resolved in Phase 9b" with
no "Do not compute P×I" prohibition adjacent (C-33 FAIL — placeholder present, prohibition
absent). This variation isolates C-35: domain-indexed "(1)"/"(2)" prefixes satisfy C-34, but
the per-site before/after notation is absent. Three open triggers at finalization: T-25, T-33,
T-35. Finding ordinal labels produced in "Finding N: T-NN" format within the narrative
(C-30 PASS). Trigger count 35 (C-24 PASS). CLOSED BY column present (C-22 PASS).
Score: 25/28 → 98.93.

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
Populate T-01..T-35 (35 trigger rules, one per v12 criterion). Assign PHASE for each.

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-35.

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

T-01..T-35, exactly 35 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 35)
T-25 PHASE = FINALIZATION  (fires if finalization verification is not a numbered 4-step list)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-30 PHASE = FINALIZATION  (fires if findings lack "Finding N: T-NN" header format)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix on each domain entry — "Domain N —" or equivalent
                             ordinal-indexed form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                             [R-NN pending] → [R-NN entries] transition notation per site)
```

---

## V-05 — Inertia-Forward + Aggregate Phase 9b | Axis: Inertia Framing | Designed fail: C-32 + C-34 + C-35

**Hypothesis**: A variation that foregrounds the status-quo option and uses back-fill mode
(C-31 PASS: placeholder at Phase 2; C-33 PASS: prohibition instruction adjacent to
placeholder directive) will fail C-32, C-34, and C-35 when Phase 9b confirms back-fill with
an aggregate statement ("all [R-NN pending] placeholders resolved; back-fill complete") rather
than a structural-domain enumeration. The aggregate form names neither option RISK fields by
label nor the comparison matrix risk column as a named structural domain (C-32 FAIL). Because
no domains are enumerated, no domain-index prefixes can be present (C-34 FAIL by necessity —
no domains to index). Because the aggregate form has no per-site entries, no site can show the
[R-NN pending] → [R-NN IDs] transition notation (C-35 FAIL). Three fails: C-32, C-34, C-35.
Three open triggers: T-32, T-34, T-35. CLOSED BY column present (C-22 PASS). Trigger count 35
(C-24 PASS). Numbered 4-step finalization (C-25 PASS). Score: 25/28 → 98.93.

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
Populate T-01..T-35. Assign PHASE for each trigger. All STATUS = PENDING at init.

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
[R-NN pending] with the applicable register entries. Confirm the comparison matrix risk
column is also updated with applicable R-NN IDs.

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-35.

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

T-01..T-35, exactly 35 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = FINALIZATION  (fires if amendment table row count != 35)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains — aggregate confirmation
                             "back-fill complete" without named structural domains fires T-32)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix on each domain entry — aggregate form with no
                             enumerated domains fires T-34)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show
                             [R-NN pending] → [R-NN entries] transition notation per site —
                             aggregate "back-fill complete" without per-site notation fires T-35)
```

---

## Predicted Scoring

| Variation | Axis | v12 Fails | A/28 | Composite |
|-----------|------|-----------|------|-----------|
| V-02 | Output format | C-22 | 27/28 | **99.64** |
| V-04 | Phrasing register | C-25 + C-33 + C-35 | 25/28 | **98.93** |
| V-05 | Inertia framing | C-32 + C-34 + C-35 | 25/28 | **98.93** |
| V-03 | Lifecycle emphasis | C-24 + C-32 + C-33 + C-34 + C-35 | 23/28 | **98.21** |
| V-01 | Role sequence | C-23 cascade: +C-26, C-31, C-32, C-33, C-34, C-35 | 21/28 | **97.50** |

**V-01 cascade path (7 fails)**: No R-NN usage (C-23 fail) → no Phase 9b authored (C-26
fail) → no placeholder syntax at Phase 2 (C-31 fail) → no Phase 9b to enumerate domains
(C-32 fail) → no domain-index prefixes possible with no Phase 9b present (C-34 fail) → no
per-site arrow notation possible with no back-fill present (C-35 fail) → no placeholder
pattern adjacent to prohibition (C-33 fail). Seven open triggers: T-23, T-26, T-31, T-32,
T-33, T-34, T-35. Seven ordinal-labeled findings (Finding 1: T-23 ... Finding 7: T-35).
21/28.

**V-02 as C-34+C-35 exemplar**: Phase 2 template: "Do not compute P×I in Phase 2 RISK
fields. Declare [R-NN pending] to reserve the slot." (C-33 PASS). Phase 9b uses "Domain 1 —
Option RISK fields (by option label)" and "Domain 2 — Comparison matrix risk column" as
numeric-indexed domain headers (C-34 PASS), and shows "[OPTION-A label] RISK field: [R-NN
pending] → [applicable R-NN entries, P×I scores]" arrow notation per citation site (C-35
PASS). Coverage table omits CLOSED BY column (C-22 FAIL). One open trigger: T-22. Finding
1: T-22. 27/28.

**V-03 stale table + five fails**: C-24 fail (31 rows, not 35) fires at PRE-DOCUMENT. Phase
9b: "Enumerate each citation site visited by option label. Confirm R-NN formula applied at
comparison matrix risk column." — no named structural domains (C-32 FAIL), no index prefixes
(C-34 FAIL), no per-site arrow notation (C-35 FAIL). Phase 2: "[R-NN pending] — placeholder
for register linkage, resolved in Phase 9b" with no prohibition (C-33 FAIL). T-32 through
T-35 absent from 31-row table; behavioral fails not captured as trigger findings. One finding:
Finding 1: T-24. 23/28.

**V-04 C-35 isolation**: Phase 9b uses "(1) Option RISK fields (by option label)" and
"(2) Comparison matrix risk column" — two named structural domains with ordinal-indexed
prefixes (C-32 PASS, C-34 PASS). But per-site output states only the outcome: "the R-NN IDs
applied to its RISK field" — no [R-NN pending] → [R-NN IDs] transition notation (C-35 FAIL).
Phase 2 placeholder present, prohibition absent (C-33 FAIL). Prose finalization (C-25 FAIL).
Three open triggers: T-25, T-33, T-35. Finding ordinal labels appear inline in narrative
(C-30 PASS). 25/28.

**V-05 C-32+C-34+C-35 cascade from aggregate Phase 9b**: Phase 2 carries prohibition +
placeholder (C-31 PASS, C-33 PASS). Phase 9b: "Citation-site enumeration: all [R-NN pending]
placeholders resolved; R-NN IDs back-filled from register; comparison matrix risk column
updated. Back-fill complete." — aggregate form, no structural domains named (C-32 FAIL), no
index prefixes (C-34 FAIL — no domains to prefix), no per-site transition notation (C-35
FAIL — aggregate has no per-site entries). Three open triggers: T-32, T-34, T-35. 25/28.

**New C-34+C-35 isolation coverage**: V-04 demonstrates C-34 PASS / C-35 FAIL (ordinal
"(1)"/"(2)" prefix satisfies C-34; outcome-only per-site output fails C-35). Combined with
V-02 (C-34 PASS / C-35 PASS exemplar), the rubric has isolation evidence: C-35 can fail
while C-34 passes when the domain-index structure is present but each site shows only the
final ID without the before/after state transition. V-05 demonstrates C-32 + C-34 + C-35 all
fail together from a single aggregate-confirmation shortcut — the same three-fail pattern
identified in the v12 rubric C-32 cascade path.

**C-34 failure modes documented in R12**:
- V-03: Phase 9b enumerates option labels only (C-32 FAIL) — no structural domain entries,
  so no index prefix possible. C-34 and C-32 co-fail.
- V-05: Phase 9b is aggregate with no enumerated domains — C-34 FAIL by absence of any
  domain entry to carry a prefix.
- V-04 provides the C-34 PASS / C-35 FAIL isolation: "(1)"/"(2)" ordinal form satisfies
  C-34 while the per-site outcome-only notation fails C-35.

**C-35 failure modes documented in R12**:
- V-01: No Phase 9b authored — C-35 fails by cascade from C-23.
- V-03: No Phase 9b arrow notation — fails as part of the stale-table aggregate.
- V-04: Domain-indexed Phase 9b present, but outcome-only notation ("applied to its RISK
  field") — the cleanest C-35 isolation: C-31 PASS, C-32 PASS, C-34 PASS, C-35 FAIL.
- V-05: Aggregate Phase 9b — C-35 fails because aggregate "back-fill complete" form has
  no per-site entries to carry transition notation.
