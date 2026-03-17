# draft-proposal Variate — Round 17

Rubric version: v17 · Formula: (E/4×60) + (R/3×30) + (A/38×10) · New criteria: C-44 (Domain 2
inter-entry pipe connector: ` | ` with flanking spaces required between adjacent bracket entries —
comma, semicolon, or juxtaposition fires T-44), C-45 (do-nothing option must appear as a named
column bracket in Domain 2 per-column enumeration — alternatives-only list without do-nothing
column fires T-45)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Domain 2 inter-entry connector (lifecycle emphasis — comma separator used instead of
  pipe between bracket entries, `Risk row:` compound prefix intact, `column:` designators intact,
  do-nothing column present) — designed fail: C-44 only (C-37 PASS — per-column enumeration present;
  C-40 PASS — `Risk row:` prefix present; C-42 PASS — `column:` designators in brackets; C-43 PASS —
  compound form intact; C-45 PASS — do-nothing column bracket present; C-41 PASS — compound
  after-state present)
- **V-02**: Domain 2 column coverage (output format — do-nothing option absent from Domain 2
  per-column bracket enumeration, pipe connector present, all bracket-internal criteria intact) —
  designed fail: C-45 only (C-37 PASS — per-column enumeration present; C-40 PASS; C-42 PASS;
  C-43 PASS; C-44 PASS — pipe connector between named alternatives; C-41 PASS — compound after-state)
- **V-03**: After-state compound form re-isolation under v17 (inertia framing — P×I-only after-state
  in Domain 1, full `Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] |
  [do-nothing column: R-NN IDs]` form in Domain 2) — designed fail: C-41 only (C-40 PASS; C-42 PASS;
  C-43 PASS; C-44 PASS; C-45 PASS; C-36 PASS — P×I present in after-state)
- **V-04**: C-44 + C-45 combined isolation (role sequence + phrasing register — comma separator AND
  do-nothing absent from Domain 2) — designed fail: C-44 + C-45 (C-37 PASS — per-column enumeration
  present; C-40 PASS — `Risk row:` prefix; C-42 PASS — `column:` designators; C-43 PASS — compound
  form; C-41 PASS — compound after-state; two-criterion isolation, no cascade between C-44 and C-45)
- **V-05**: Role sequence cascade from C-23 root (PM-only role + compressed lifecycle) — designed
  fail: C-23 cascade → C-23, C-26, C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38, C-39, C-40,
  C-41, C-42, C-43, C-44, C-45 (17 fails — extends R16 V-05 cascade from 15 to 17 via C-44 and
  C-45, both cascading from C-37)

Predicted scores:
- V-01 → 37/38 → **99.74**
- V-02 → 37/38 → **99.74**
- V-03 → 37/38 → **99.74**
- V-04 → 36/38 → **99.47**
- V-05 → 21/38 → **95.53**

---

## V-01 — C-44 Targeted | Axis: Lifecycle Emphasis (Domain 2 Inter-Entry Connector) | Designed fail: C-44 only

**Hypothesis**: A variation that produces Domain 2 per-column bracket entries separated by commas
rather than ` | ` pipes will pass C-37 (per-column R-NN enumeration present), C-40 (`Risk row:`
row-label prefix anchoring the enumeration), C-42 (`column:` axis-designator inside each bracket),
C-43 (compound `Risk row:` form with dimension identifier intact), and C-45 (do-nothing column
bracket present) but fail C-44 because the comma separator between bracket entries leaves the
inter-entry connector ungoverned — the annotation `Risk row: [Option-A column: R-NN IDs],
[Option-B column: R-NN IDs], [do-nothing column: R-NN IDs]` is structurally correct at every
bracket-internal and prefix layer but uses a connector that is not the required pipe form. Domain 1
after-state uses the full compound form `[applicable R-NN entries, P×I scores]` (C-41 PASS).
Composite site identifier `[OPTION label] RISK field:` present (C-38 PASS). Before-state
`[R-NN pending]` placeholder intact (C-39 PASS). CLOSED BY column present (C-22 PASS).
Trigger count 45 (C-24 PASS). One open trigger: T-44. Score: 37/38 → 99.74.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Owns technical option framing, risk register construction, Phase 9b
  back-fill, gate audit, and feasibility confirmation.
- PM: Owns business trade-off commentary, adoption risk entries, and recommendation
  rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) as a typed header at the top of
the output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per v17 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires (PRE-DOCUMENT,
PRE-OPTION, FINALIZATION, or a named phase). Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column as
                               two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                               P×I" prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix — "Domain N —" or equivalent ordinal form required)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                               [R-NN pending] → [R-NN entries] transition notation)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site resolved state does not include
                               P×I compound scores in the after-state)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks a
                               row-label prefix naming the matrix row before listing columns —
                               bare per-column form without "Risk row:" anchor fires T-40)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                               entries and P×I scores together in a single compound expression —
                               P×I-only or R-NN-only after-state fires T-41)
  T-42 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries do not
                               carry the `column:` axis-designator inside the bracket — form
                               [Option-X: R-NN IDs] without `column:` keyword fires T-42)
  T-43 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 row-label prefix is not the compound
                               `Risk row:` form pairing the matrix dimension identifier with the
                               structural position type — bare `row:` prefix fires T-43)
  T-44 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries use a
                               separator other than ` | ` between adjacent bracket expressions —
                               comma, semicolon, newline, or juxtaposition fires T-44; only the
                               space-pipe-space form between bracket entries satisfies this rule)
  T-45 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket enumeration does
                               not include a named column entry for the do-nothing option — a
                               list covering only the named alternatives but omitting do-nothing
                               fires T-45 regardless of how many alternatives are present)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

Architect: State the shared problem being decided. This PROBLEM field is shared by all
options and must appear before any option is composed.

PM: Confirm the problem statement captures business context and urgency.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Architect notes technical risk category. PM notes adoption risk category.
        Example: "[R-NN pending] — technical coupling risk (Architect); adoption friction
        if teams must retrain (PM)"
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
Matrix rows (dimensions): Effort, Risk (R-NN cited), Reversibility, Time-to-value.
PM: Add Adoption friction as a row. Score or characterize each cell consistently.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation referencing a real criterion ID. List any missing citations and mark them in
the amendment table (STATUS = OPEN for the corresponding T-NN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, phases appear in declared sequence.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [OPTION-B label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [do-nothing option label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs], [Option-B column: R-NN IDs], [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

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
  Enumerate findings sequentially (Finding 1, Finding 2, ...). One finding per trigger.

Step 2: Verify all E-tier criteria are satisfied. Update coverage table STATUS for any
  E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria are satisfied. Update coverage table STATUS for any
  R-tier criterion found incomplete.

Step 4: Confirm the coverage table is fully populated. Set COMPLETION STATUS of the
  amendment table to the final state.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix on each domain entry — "Domain N —" form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                             [R-NN pending] → [R-NN entries] transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                             compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                             specify R-NN IDs per option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration lacks "Risk row:" anchor
                             prefix before the column list)
T-41 PHASE = FINALIZATION  (fires if per-site after-state does not pair R-NN entries and P×I
                             scores together in a single compound expression)
T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                             `column:` axis-designator — [Option-X: R-NN IDs] form fires T-42)
T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                             form — bare `row:` prefix without dimension identifier fires T-43)
T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                             newline, or juxtaposition as the inter-entry separator instead of
                             ` | ` — only space-pipe-space between bracket entries satisfies)
T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration omits the
                             do-nothing option as a named column bracket — alternatives-only
                             list without do-nothing column entry fires T-45)
```

---

## V-02 — C-45 Targeted | Axis: Output Format (Domain 2 Column Coverage) | Designed fail: C-45 only

**Hypothesis**: A variation that produces Domain 2 per-column bracket entries covering only
the named alternatives (Option-A, Option-B) with the correct ` | ` pipe separator and
`column:` axis-designators but no do-nothing column bracket will pass C-37 (per-column
enumeration present), C-40 (`Risk row:` prefix anchoring), C-42 (`column:` inside each
bracket), C-43 (compound `Risk row:` form), and C-44 (pipe connector between entries) but
fail C-45 because the do-nothing option's per-column R-NN assignment is absent from the matrix
annotation layer. The annotation `Risk row: [Option-A column: R-NN IDs] | [Option-B column:
R-NN IDs]` is structurally correct at every governed layer (C-40 through C-44) but omits the
column bracket that covers the do-nothing option's risk exposure in the comparison matrix.
Domain 1 after-state uses the full compound form `[applicable R-NN entries, P×I scores]`
(C-41 PASS). Composite site identifier `[OPTION label] RISK field:` present (C-38 PASS).
Before-state `[R-NN pending]` placeholder intact (C-39 PASS). CLOSED BY column present
(C-22 PASS). Trigger count 45 (C-24 PASS). One open trigger: T-45. Score: 37/38 → 99.74.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Owns technical option framing, risk register construction, Phase 9b
  back-fill, gate audit, and feasibility confirmation.
- PM: Owns business trade-off commentary, adoption risk entries, and recommendation
  rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) as a typed header at the top of
the output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per v17 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires. Leave STATUS
= PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column as
                               two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                               P×I" prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix — "Domain N —" or equivalent ordinal form required)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                               [R-NN pending] → [R-NN entries] transition notation)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site resolved state does not include
                               P×I compound scores in the after-state)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks a
                               row-label prefix naming the matrix row before listing columns)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                               entries and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries do not
                               carry the `column:` axis-designator inside the bracket)
  T-43 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 row-label prefix is not the compound
                               `Risk row:` form — bare `row:` prefix without dimension
                               identifier fires T-43)
  T-44 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries use a
                               separator other than ` | ` between adjacent bracket expressions)
  T-45 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket enumeration does
                               not include a named column entry for the do-nothing option —
                               alternatives-only list omitting do-nothing fires T-45)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

Architect: State the shared problem being decided. This PROBLEM field is shared by all
options and must appear before any option is composed.

PM: Confirm the problem statement captures business context and urgency.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Architect notes technical risk category. PM notes adoption risk category.
        Example: "[R-NN pending] — technical coupling risk (Architect); adoption friction
        if teams must retrain (PM)"
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
Matrix rows (dimensions): Effort, Risk (R-NN cited), Reversibility, Time-to-value.
PM: Add Adoption friction as a row. Score or characterize each cell consistently.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation referencing a real criterion ID. List any missing citations and mark them in
the amendment table (STATUS = OPEN for the corresponding T-NN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, phases appear in declared sequence.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [OPTION-B label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [do-nothing option label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

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
  Enumerate findings sequentially (Finding 1, Finding 2, ...). One finding per trigger.

Step 2: Verify all E-tier criteria are satisfied. Update coverage table STATUS for any
  E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria are satisfied. Update coverage table STATUS for any
  R-tier criterion found incomplete.

Step 4: Confirm the coverage table is fully populated. Set COMPLETION STATUS of the
  amendment table to the final state.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                             RISK fields by option label AND comparison matrix risk column as
                             two explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition instruction adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                             index prefix on each domain entry — "Domain N —" form required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                             [R-NN pending] → [R-NN entries] transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                             compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                             specify R-NN IDs per option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration lacks "Risk row:" anchor
                             prefix before the column list)
T-41 PHASE = FINALIZATION  (fires if per-site after-state does not pair R-NN entries and P×I
                             scores together in a single compound expression)
T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                             `column:` axis-designator — [Option-X: R-NN IDs] form fires T-42)
T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                             form — bare `row:` prefix without dimension identifier fires T-43)
T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                             newline, or juxtaposition as the inter-entry separator instead of
                             ` | ` — only space-pipe-space between bracket entries satisfies)
T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration omits the
                             do-nothing option as a named column bracket — alternatives-only
                             list without do-nothing column entry fires T-45)
```

---

## V-03 — C-41 Targeted | Axis: Inertia Framing (After-State Compound Form) | Designed fail: C-41 only

**Hypothesis**: A variation that produces Domain 1 per-site after-states containing P×I scores
only (no R-NN entries named in the compound expression) will pass C-36 (P×I present in
after-state), C-38 (composite site identifier present), C-39 (`[R-NN pending]` before-state
present), C-40 (`Risk row:` prefix), C-42 (`column:` axis-designator), C-43 (compound `Risk
row:` form), C-44 (pipe connector between entries), and C-45 (do-nothing column present) but
fail C-41 because the after-state `[P4×I3 = 12]` names the computed product without identifying
which R-NN entries produced it — the compound resolution form requires both the applicable R-NN
entries AND P×I scores within a single bracketed expression. The do-nothing option is framed
prominently in Phase 2 as the current-state default and analyzed first; its risk exposure is
covered in Domain 1 and Domain 2. Domain 2 uses the full five-criterion form (C-44 and C-45
PASS). One open trigger: T-41. Score: 37/38 → 99.74.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Owns technical option framing, risk register construction, Phase 9b
  back-fill, gate audit, and feasibility confirmation.
- PM: Owns business trade-off commentary, adoption risk entries, and recommendation
  rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) as a typed header at the top of
the output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per v17 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires. Leave STATUS
= PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column as
                               two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                               P×I" prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix — "Domain N —" or equivalent ordinal form required)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                               [R-NN pending] → [R-NN entries] transition notation)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site resolved state does not include
                               P×I compound scores in the after-state)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks a
                               row-label prefix naming the matrix row before listing columns)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                               entries and P×I scores together in a single compound expression —
                               P×I-only after-state `[PX×IY = Z]` without named R-NN entries
                               fires T-41; required form: `[R-NN entries, PX×IY = Z]`)
  T-42 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries do not
                               carry the `column:` axis-designator inside the bracket)
  T-43 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 row-label prefix is not the compound
                               `Risk row:` form — bare `row:` prefix fires T-43)
  T-44 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries use a
                               separator other than ` | ` between adjacent bracket expressions)
  T-45 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket enumeration does
                               not include a named column entry for the do-nothing option)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

Architect: State the shared problem being decided. This PROBLEM field is shared by all
options and must appear before any option is composed.

PM: Confirm the problem statement captures business context and urgency. Explicitly
state the cost of inaction — what the do-nothing option costs the business over time.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Inertia framing: analyze the do-nothing option first. It is the current-state default
and the baseline against which all alternatives are measured. All other options must
justify their cost relative to the do-nothing baseline.

Compose at least 3 options, starting with do-nothing. For each option, produce an entry
with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. Architect notes technical risk category. PM notes adoption risk category.
        Example: "[R-NN pending] — technical coupling risk (Architect); adoption friction
        if teams must retrain (PM)"
  RATIONALE: [why this option is a candidate]

Compose do-nothing first, then alternatives.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Assign P and I scores
on a 1-5 scale. Compute P×I compound score. Include at least one risk specific to the
do-nothing option (cost of status quo, accruing tech debt, or missed opportunity window).
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Architect: Build a comparison matrix with OPTIONS as column headers. do-nothing appears
as the rightmost column to serve as the inertia baseline.
Matrix rows (dimensions): Effort, Risk (R-NN cited), Reversibility, Time-to-value.
PM: Add Adoption friction as a row. Add Status-quo cost as a row characterizing what
    do-nothing accumulates over the decision horizon.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation referencing a real criterion ID. List any missing citations and mark them in
the amendment table (STATUS = OPEN for the corresponding T-NN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, do-nothing analyzed first in Phase 2, phases appear in declared sequence.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [P×I score]
    [OPTION-B label] RISK field: [R-NN pending] → [P×I score]
    [do-nothing option label] RISK field: [R-NN pending] → [P×I score]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. Explicitly compare against the do-nothing baseline.
State qualifying conditions for the recommendation.
Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry using this format:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria are satisfied.
Step 3: Verify all R-tier criteria are satisfied.
Step 4: Confirm the coverage table is fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
[Same key assignments as V-01 and V-02 — T-24 row count = 45, T-44 pipe connector,
T-45 do-nothing column, T-41 compound after-state R-NN + P×I form]
```

---

## V-04 — C-44 + C-45 Combined | Axes: Role Sequence + Phrasing Register | Designed fail: C-44 + C-45

**Hypothesis**: A variation that uses PM-first role sequence and conversational phrasing will
produce Domain 2 per-column bracket entries with comma separators AND omit the do-nothing
column bracket, failing both C-44 and C-45 while passing C-37 (per-column enumeration present),
C-40 (`Risk row:` prefix), C-42 (`column:` designators), C-43 (compound `Risk row:` form), and
C-41 (compound after-state with R-NN entries and P×I scores). C-44 and C-45 are mutually
independent: the presence or absence of the do-nothing column does not affect whether the
separator is a comma or pipe; a variation carrying both failures demonstrates that neither
criterion cascades from the other. Two open triggers: T-44, T-45. Score: 36/38 → 99.47.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, comparison matrix, and recommendation.
  Runs first in every phase.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) as a typed header at the top of the
output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per v17 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name option
                               RISK fields by option label AND comparison matrix risk column as
                               two explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                               prohibition instruction adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration does not carry numeric
                               index prefix — "Domain N —" form required)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b citation-site entries do not show per-site
                               [R-NN pending] → [R-NN entries] transition notation)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not include P×I
                               compound scores)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry does not
                               specify R-NN IDs per option column)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                               identifier "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                               [R-NN pending] placeholder literal)
  T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration lacks "Risk row:" anchor
                               prefix before the column list)
  T-41 PHASE = FINALIZATION  (fires if per-site after-state does not pair R-NN entries and P×I
                               scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator — [Option-X: R-NN IDs] form fires T-42)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form — bare `row:` prefix fires T-43)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration omits the
                               do-nothing option as a named column bracket)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. Keep it concise — one paragraph maximum.
    Focus on the business gap and the decision that is needed.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Name at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Architect: Review option framing for technical completeness.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Assign P and I scores
on a 1-5 scale. Compute P×I compound score.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited).
Architect: Add Effort and Integration complexity as rows.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, phases appear in declared sequence.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [OPTION-B label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
    [do-nothing option label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs], [Option-B column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions for the recommendation.
Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria. Step 3: Verify all R-tier criteria.
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
[Same key assignments as V-01 through V-03 — T-44 pipe connector, T-45 do-nothing column,
T-24 row count = 45]
```

---

## V-05 — C-23 Cascade | Axes: PM-Only Role + Compressed Lifecycle | Designed fail: 17 fails

**Hypothesis**: A variation that uses PM-only framing with compressed lifecycle phases and omits
the R-NN linkage mechanism will cascade from C-23 through 17 fails. Without a declared R-NN risk
register linkage in Phase 2 RISK fields, Phase 9b cannot exist (C-26 fail), the `[R-NN pending]`
placeholder convention cannot appear (C-31 fail), no Domain 1 or Domain 2 structural enumeration
is produced (C-32 fail), the P×I prohibition instruction has no placeholder context (C-33 fail),
Domain index prefixes have no domains to anchor (C-34 fail), per-site arrow notation cannot fire
without declared sites (C-35 fail), P×I scores cannot appear in an absent after-state (C-36 fail),
no per-column R-NN enumeration exists (C-37 fail), no composite site identifier is produced
(C-38 fail), no `[R-NN pending]` before-state placeholder is present (C-39 fail), no row-label
prefix has no row to label (C-40 fail), no compound after-state form exists (C-41 fail), no
`column:` designators inside absent brackets (C-42 fail from C-37), no compound `Risk row:` prefix
(C-43 fail from C-40), no pipe separator between absent bracket entries (C-44 fail from C-37), no
do-nothing column bracket in absent enumeration (C-45 fail from C-37). Seventeen fails from one
root. Advisory bucket: 21/38. Score: 95.53.

```
ROLE SEQUENCE: PM (single role)

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENT:
- PM: Owns all phases. Frames the business decision, enumerates options, builds the
  comparison matrix, and delivers the recommendation. Technical constraints are noted
  inline where relevant but no Architect role is active.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the PM-only role sequence at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-45 — one per v17 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context and
the forcing function making this decision necessary now.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce the following:

  OPTION: [label and description]
  PROS: [advantages of this option]
  CONS: [disadvantages of this option]
  RISK: [key risks, described in plain language]
  EFFORT: [rough estimate — S / M / L / XL]
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers.
Matrix rows: Business value, Time-to-value, Reversibility, Risk level, Effort.
Score or characterize each cell consistently across all options.

---

PHASE 4 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, phases appear in declared sequence.

---

PHASE 5 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-45.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 6 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions for the recommendation.

---

PHASE 7 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered three-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier and R-tier criteria are satisfied.
Step 3: Confirm the coverage table is fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-45 — exactly 45 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
```

---

## Predicted score summary

| Variation | Axis | Open triggers | A/38 | Composite |
|-----------|------|---------------|------|-----------|
| V-01 | Lifecycle emphasis — comma connector | T-44 | 37/38 | **99.74** |
| V-02 | Output format — do-nothing absent from Domain 2 | T-45 | 37/38 | **99.74** |
| V-03 | Inertia framing — P×I-only after-state | T-41 | 37/38 | **99.74** |
| V-04 | Role sequence + phrasing register — comma AND no do-nothing | T-44, T-45 | 36/38 | **99.47** |
| V-05 | PM-only + compressed lifecycle — C-23 cascade | 17 fails | 21/38 | **95.53** |

**C-44 and C-45 independence evidence:**
V-04 demonstrates that C-44 and C-45 are mutually independent: the comma separator failure (C-44)
and the do-nothing column absence (C-45) are combinable without cascade between them. Neither
criterion conditions on the other. Both cascade independently from C-37 (per-column enumeration
present), which V-04 satisfies. V-05 demonstrates the cascade path: when C-37 fails (no per-column
enumeration), C-44 and C-45 both fail as a consequence — the absence of brackets makes both the
inter-entry connector and the do-nothing column bracket structurally impossible.

**V-03 as v17 exemplar for C-44 + C-45 (both PASS):**
V-03 passes all five Domain 2 annotation criteria: `Risk row: [Option-A column: R-NN IDs] |
[Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]` — row-label prefix (C-40 PASS),
compound `Risk row:` form (C-43 PASS), `column:` designators (C-42 PASS), pipe connectors (C-44
PASS), do-nothing column present (C-45 PASS). Single open trigger: T-41 (P×I-only after-state
in Domain 1). 37/38 = 99.74.
