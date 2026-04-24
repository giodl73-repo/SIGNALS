# draft-proposal Variate — Round 16

Rubric version: v16 · Formula: (E/4×60) + (R/3×30) + (A/36×10) · New criteria: C-42 (Domain 2
bracket column-axis designator: `[Option-X column: R-NN IDs]` form required inside each bracket
entry), C-43 (Domain 2 row-label compound form: `Risk row:` pairing matrix dimension with
position type, not bare `row:` prefix alone)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Domain 2 bracket axis-designator (lifecycle emphasis — `column:` keyword absent from
  each bracket entry, `Risk row:` prefix intact) — designed fail: C-42 only (C-37 PASS — per-column
  enumeration present; C-40 PASS — `Risk row:` prefix present; C-43 PASS — compound form intact;
  C-41 PASS — compound after-state present)
- **V-02**: Domain 2 row-label compound form (phrasing register — bare `row:` prefix used instead
  of compound `Risk row:`, `column:` designators intact in brackets) — designed fail: C-43 only
  (C-40 PASS — row-label prefix present; C-42 PASS — `column:` designators in brackets; C-37 PASS)
- **V-03**: After-state compound form re-isolation under v16 (output format — P×I-only after-state
  in Domain 1, full `Risk row: [Option-A column: R-NN IDs]` form in Domain 2) — designed fail:
  C-41 only (C-40 PASS; C-42 PASS; C-43 PASS; C-36 PASS — P×I present in after-state)
- **V-04**: C-42 + C-43 combined isolation (lifecycle emphasis + phrasing register — bare `row:`
  prefix AND no `column:` designator) — designed fail: C-42 + C-43 (C-40 PASS — row-label prefix
  present; C-37 PASS; C-41 PASS — compound after-state intact; two-criterion isolation, no cascade
  between them)
- **V-05**: Role sequence cascade from C-23 root — designed fail: C-23 cascade → C-23, C-26,
  C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-42, C-43 (15 fails — extends
  R15 V-05 cascade from 13 to 15 via C-42 and C-43)

Predicted scores:
- V-01 → 35/36 → **99.72**
- V-02 → 35/36 → **99.72**
- V-03 → 35/36 → **99.72**
- V-04 → 34/36 → **99.44**
- V-05 → 21/36 → **95.83**

---

## V-01 — C-42 Targeted | Axis: Lifecycle Emphasis (Domain 2 Bracket Axis-Designator) | Designed fail: C-42 only

**Hypothesis**: A variation that produces Domain 2 per-column bracket entries without the
`column:` axis-designator inside each bracket will pass C-37 (per-column R-NN enumeration present),
C-40 (`Risk row:` row-label prefix anchoring the enumeration), and C-43 (compound `Risk row:` form
with dimension identifier intact) but fail C-42 because the bracket entries `[Option-A: R-NN IDs]`
do not label each option as a column-axis position within the matrix — the dimensional role of each
bracket entry is implicit rather than declared. Domain 1 after-state uses the full compound form
`[applicable R-NN entries, P×I scores]` (C-41 PASS). Composite site identifier `[OPTION label]
RISK field:` present (C-38 PASS). Before-state `[R-NN pending]` placeholder intact (C-39 PASS).
CLOSED BY column present (C-22 PASS). Trigger count 43 (C-24 PASS). One open trigger: T-42.
Score: 35/36 → 99.72.

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

Populate trigger rules T-01..T-43 — one per v16 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires (PRE-DOCUMENT,
PRE-OPTION, FINALIZATION, or a named phase). Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-43.
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
    Risk row: [Option-A: R-NN IDs] | [Option-B: R-NN IDs] | [do-nothing: R-NN IDs]

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

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
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
                             `column:` axis-designator — [Option-X: R-NN IDs] form without
                             `column:` keyword fires T-42)
T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                             form — bare `row:` prefix without dimension identifier fires T-43)
```

---

## V-02 — C-43 Targeted | Axis: Phrasing Register (Row-Label Vocabulary) | Designed fail: C-43 only

**Hypothesis**: A variation that uses a bare `row:` prefix for the Domain 2 per-column
enumeration will pass C-40 (a row-label prefix is present, anchoring the enumeration to a
named matrix row) and C-42 (`column:` axis-designator appears inside each bracket entry) but
fail C-43 because the prefix `row:` names only the structural position type, not the matrix
dimension — the reader knows which row position is being annotated but not which comparison
matrix the annotation belongs to. The form `row: [Option-A column: R-NN IDs]` is positionally
self-locating but not dimensionally self-locating, unlike `Risk row:` which names both. Domain 1
after-state uses the full compound form `[applicable R-NN entries, P×I scores]` (C-41 PASS).
Composite site identifier `[OPTION label] RISK field:` present (C-38 PASS). Before-state
`[R-NN pending]` placeholder intact (C-39 PASS). CLOSED BY column present (C-22 PASS).
Trigger count 43 (C-24 PASS). One open trigger: T-43. Score: 35/36 → 99.72.

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

Populate trigger rules T-01..T-43 — one per v16 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires. Leave STATUS
= PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
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
                               row-label prefix before listing columns — bare column list
                               without any row anchor fires T-40)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                               entries and P×I scores together in a single compound expression —
                               P×I-only or R-NN-only after-state fires T-41)
  T-42 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries do not
                               carry the `column:` axis-designator inside the bracket — form
                               [Option-X: R-NN IDs] without `column:` keyword fires T-42)
  T-43 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 row-label prefix is not the compound
                               `Risk row:` form — bare `row:` without dimension identifier fires
                               T-43 even when the row-label prefix is otherwise present)

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

Enumerate at least 3 technical risk entries. Assign P and I scores on a 1-5 scale.
Compute P×I compound score.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-43.
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
    row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

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
  Enumerate findings sequentially. One finding per trigger.

Step 2: Verify all E-tier criteria are satisfied. Update coverage table STATUS for any
  E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria are satisfied. Update coverage table STATUS for any
  R-tier criterion found incomplete.

Step 4: Confirm the coverage table is fully populated. Set COMPLETION STATUS of the
  amendment table to the final state.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name two
                             explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration lacks numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state omits P×I compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry lacks per-column
                             R-NN ID enumeration)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack composite site identifier
                             "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b before-state lacks [R-NN pending] placeholder)
T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration has no row-label prefix
                             at all — bare column list fires T-40)
T-41 PHASE = FINALIZATION  (fires if per-site after-state pairs P×I without R-NN IDs —
                             P×I-only compound expression fires T-41)
T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column brackets lack `column:` axis-designator
                             inside the bracket — [Option-X: R-NN IDs] form fires T-42)
T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is bare `row:` not compound
                             `Risk row:` — dimension identifier absent fires T-43)
```

---

## V-03 — C-41 Re-Isolation | Axis: Output Format (After-State Resolution Expression) | Designed fail: C-41 only

**Hypothesis**: Under the v16 rubric, re-isolating C-41 confirms that a P×I-only after-state in
Domain 1 per-site entries fails C-41 independently of the new criteria C-42 and C-43. When Domain
2 uses the full `Risk row: [Option-A column: R-NN IDs]` form, C-40, C-42, and C-43 all pass.
When Domain 1 per-site entries are written as `[OPTION-A label] RISK field: [R-NN pending] →
[P×I compound score for applicable risks]`, C-36 passes (P×I scores present) but C-41 fails (R-NN
identifiers that replaced the placeholder are absent from the after-state expression — the
transition is asserted without showing which register entries drove the scores). The variation uses
PM → Architect role sequence to distinguish it from V-01 and V-02. CLOSED BY column present
(C-22 PASS). Trigger count 43 (C-24 PASS). One open trigger: T-41. Score: 35/36 → 99.72.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

OUTPUT FORMAT: Narrative-first within each phase. Lead with prose context before tables.
Use standard table form for risk register and comparison matrix.

ROLE ASSIGNMENTS:
- PM: Leads business framing, problem statement, option business cases, and recommendation
  rationale. Owns adoption risk entries.
- Architect: Validates technical constraints, owns risk register technical entries, Phase 9b
  back-fill, gate audit, and feasibility confirmation.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) as a typed header at the top of the output.
Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-43 — one per v16 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires. Leave STATUS
= PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
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
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state shows P×I scores but
                               omits the R-NN identifiers that resolved the placeholder —
                               P×I-only after-state fires T-41)
  T-42 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries do not
                               carry the `column:` axis-designator inside the bracket — form
                               [Option-X: R-NN IDs] without `column:` keyword fires T-42)
  T-43 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 row-label prefix is not the compound
                               `Risk row:` form pairing the matrix dimension identifier with the
                               structural position type — bare `row:` prefix fires T-43)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided, including business context and urgency.
This PROBLEM field is shared by all options and must appear before any option is composed.

Architect: Confirm the problem statement accurately represents the technical constraints.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if teams must retrain (PM); technical
        coupling risk if shared schema changes (Architect)"
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries. Assign P and I scores on a 1-5 scale.
Compute P×I compound score.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Architect: Build a comparison matrix with OPTIONS as column headers.
Matrix rows (dimensions): Effort, Risk (R-NN cited), Reversibility, Time-to-value.
PM: Add Adoption friction as a row. Score or characterize each cell consistently.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify all phase headers carry [GATE: X-NN] citations. List any missing and
update amendment table STATUS = OPEN for corresponding T-NN.

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, phases appear in declared sequence.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-43.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [OPTION-A label] RISK field: [R-NN pending] → [P×I compound score for applicable risks]
    [OPTION-B label] RISK field: [R-NN pending] → [P×I compound score for applicable risks]
    [do-nothing option label] RISK field: [R-NN pending] → [P×I compound score for applicable risks]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

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
  Enumerate findings sequentially. One finding per trigger.

Step 2: Verify all E-tier criteria are satisfied. Update coverage table STATUS for any
  E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria are satisfied. Update coverage table STATUS for any
  R-tier criterion found incomplete.

Step 4: Confirm the coverage table is fully populated. Set COMPLETION STATUS of the
  amendment table to the final state.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name two
                             explicitly named structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                             prohibition adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration lacks numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state omits P×I compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry lacks per-column
                             R-NN ID enumeration)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack composite site identifier
                             "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b before-state lacks [R-NN pending] placeholder)
T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration has no row-label prefix)
T-41 PHASE = FINALIZATION  (fires if per-site after-state is P×I-only — R-NN IDs absent from
                             the compound expression alongside P×I scores)
T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column brackets lack `column:` axis-designator
                             inside the bracket)
T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is bare `row:` not compound
                             `Risk row:` — dimension identifier absent fires T-43)
```

---

## V-04 — C-42 + C-43 Combined | Axis: Lifecycle Emphasis + Phrasing Register | Designed fail: C-42 + C-43

**Hypothesis**: Combining a bare `row:` prefix (fails C-43 — compound form absent) with bracket
entries that lack the `column:` axis-designator (fails C-42 — axis role of each bracket entry
implicit) will isolate both new v16 criteria simultaneously without triggering any cascade between
them. C-42 and C-43 test orthogonal sub-properties of the Domain 2 annotation: C-42 tests the
column-axis designator inside each bracket entry; C-43 tests whether the row-label prefix carries
the matrix dimension identifier. Neither fail cascades from the other — a `row:` prefix can coexist
with `column:`-labelled brackets, and a bare bracket can coexist with a `Risk row:` prefix. C-40
passes (row-label prefix is present — just not in compound form). C-37 passes (per-column R-NN
enumeration present). C-41 passes (Domain 1 after-state uses full compound form
`[applicable R-NN entries, P×I scores]`). CLOSED BY column present (C-22 PASS). Trigger count 43
(C-24 PASS). Two open triggers: T-42, T-43. Score: 34/36 → 99.44.

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

Populate trigger rules T-01..T-43 — one per v16 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires. Leave STATUS
= PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
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
  T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks any
                               row-label prefix — bare column list without anchor fires T-40)
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                               entries and P×I scores in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column bracket entries do not
                               carry the `column:` axis-designator inside the bracket — form
                               [Option-X: R-NN IDs] without `column:` keyword fires T-42)
  T-43 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 row-label prefix is not the compound
                               `Risk row:` form pairing the matrix dimension identifier with the
                               structural position type — bare `row:` prefix fires T-43)

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

Enumerate at least 3 technical risk entries. Assign P and I scores on a 1-5 scale.
Compute P×I compound score.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-43.
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
    row: [Option-A: R-NN IDs] | [Option-B: R-NN IDs] | [do-nothing: R-NN IDs]

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

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name two structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I" prohibition)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration lacks numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state omits P×I compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 lacks per-column R-NN enumeration)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack "[OPTION label] RISK field:"
                             composite site identifier form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b before-state lacks [R-NN pending] placeholder)
T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration has no row-label prefix at
                             all — bare column list without any anchor fires T-40)
T-41 PHASE = FINALIZATION  (fires if per-site after-state is P×I-only with R-NN IDs absent from
                             the compound expression)
T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column brackets lack `column:` axis-designator
                             inside the bracket — [Option-X: R-NN IDs] form fires T-42)
T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is bare `row:` not compound
                             `Risk row:` — dimension identifier absent fires T-43)
```

---

## V-05 — Cascade Root | Axis: Role Sequence (C-23 cascade → 15 fails) | Designed fail: C-23 + 14 cascades

**Hypothesis**: A variation that omits R-NN linkage from RISK fields in the final document will
fail C-23 (the root), which cascades through the entire Phase 9b structure to produce 15 total
fails. Under v16, the cascade path extends two steps further than R15 (which terminated at C-41):
C-37 failure (no per-column R-NN enumeration) now cascades to C-42 (no `column:` designators
possible if no R-NN enumeration exists); C-40 failure (no Domain 2 row-label prefix) now cascades
to C-43 (compound form certainly absent if no prefix at all). The cascade from one root generates
exactly 15 advisory criterion failures: C-23, C-26, C-31, C-32, C-33, C-34, C-35, C-36, C-37,
C-38, C-39, C-40, C-41, C-42, C-43. Advisory bucket: 21/36. Score: 21/36 → 95.83.

```
ROLE SEQUENCE: Architect → PM

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- Architect: Owns technical option framing, risk register construction, gate audit,
  and feasibility confirmation.
- PM: Owns business trade-off commentary, adoption risk entries, and recommendation
  rationale.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) as a typed header at the top of
the output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-43 — one per v16 rubric criterion. Each row must carry a
populated PHASE value naming the lifecycle gate at which the trigger fires. Leave STATUS
= PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
  T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
  T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
  T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation section present)
  T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
  T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name two
                               explicitly named structural domains)
  T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I"
                               prohibition adjacent to placeholder directive)
  T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration lacks numeric index prefix)
  T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
  T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state omits P×I compound scores)
  T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain entry lacks per-column
                               R-NN ID enumeration)
  T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack composite site identifier
                               "[OPTION label] RISK field:" form)
  T-39 PHASE = FINALIZATION  (fires if Phase 9b before-state lacks [R-NN pending] placeholder)
  T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration has no row-label prefix)
  T-41 PHASE = FINALIZATION  (fires if per-site after-state omits R-NN IDs from compound
                               expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column brackets lack `column:` axis-designator
                               inside the bracket)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not compound `Risk row:`
                               form — dimension identifier absent fires T-43)

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
  RISK: Describe qualitative risk for this option. Note technical risk category
        (Architect) and adoption risk category (PM).
  RATIONALE: [why this option is a candidate]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries. Assign P and I scores on a 1-5 scale.
Compute P×I compound score.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

Architect: Build a comparison matrix with OPTIONS as column headers.
Matrix rows (dimensions): Effort, Risk, Reversibility, Time-to-value.
PM: Add Adoption friction as a row. Score or characterize each cell consistently.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify all phase headers carry [GATE: X-NN] citations. List any missing and
update amendment table STATUS = OPEN for the corresponding T-NN.

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, phases appear in declared sequence.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-43.
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
  Enumerate findings sequentially (Finding 1, Finding 2, ...). One finding per trigger.

Step 2: Verify all E-tier criteria are satisfied. Update coverage table STATUS for any
  E-tier criterion found incomplete.

Step 3: Verify all R-tier criteria are satisfied. Update coverage table STATUS for any
  R-tier criterion found incomplete.

Step 4: Confirm the coverage table is fully populated. Set COMPLETION STATUS of the
  amendment table to the final state.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b enumeration does not name two structural domains)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits "Do not compute P×I" prohibition)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain enumeration lacks numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state omits P×I compound scores)
T-37 PHASE = FINALIZATION  (fires if Phase 9b comparison matrix domain lacks per-column R-NN IDs)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack "[OPTION label] RISK field:"
                             composite site identifier)
T-39 PHASE = FINALIZATION  (fires if Phase 9b before-state lacks [R-NN pending] placeholder)
T-40 PHASE = FINALIZATION  (fires if Domain 2 per-column enumeration has no row-label prefix)
T-41 PHASE = FINALIZATION  (fires if per-site after-state omits R-NN IDs from compound expression)
T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column brackets lack `column:` axis-designator)
T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix lacks `Risk` dimension identifier)
```

---

## Score Summary

| Variation | Axis | Designed Fail | A/36 | Composite |
|-----------|------|---------------|------|-----------|
| V-01 | Lifecycle emphasis (bracket axis-designator) | C-42 | 35/36 | **99.72** |
| V-02 | Phrasing register (row-label vocabulary) | C-43 | 35/36 | **99.72** |
| V-03 | Output format (after-state resolution form) | C-41 | 35/36 | **99.72** |
| V-04 | Lifecycle emphasis + phrasing register combined | C-42 + C-43 | 34/36 | **99.44** |
| V-05 | Role sequence cascade (C-23 root) | 15 fails | 21/36 | **95.83** |

**Cascade path confirmation (V-05, 15 fails):**
C-23 (root: no R-NN linkage) →
  C-26 (no Phase 9b section) →
  C-31 (no `[R-NN pending]` placeholder) →
  C-32 (no two-domain enumeration) →
  C-33 (no "Do not compute P×I" prohibition) →
  C-34 (no numeric domain index prefix) →
  C-35 (no per-site arrow notation) →
  C-36 (no P×I scores in after-state) →
  C-37 (no per-column R-NN enumeration) →
  C-38 (no composite site identifier) →
  C-39 (no `[R-NN pending]` before-state) →
  C-40 (no Domain 2 row-label prefix) →
  C-41 (no compound after-state R-NN + P×I form) →
  C-42 (no `column:` bracket designators — cascade from C-37) →
  C-43 (no compound `Risk row:` prefix form — cascade from C-40).
Fifteen fails from one root. Advisory bucket: 21/36.

**V-01 vs V-04 key distinction:**
- V-01: `Risk row: [Option-A: R-NN IDs]` — compound prefix present (C-43 PASS), `column:` absent (C-42 FAIL)
- V-04: `row: [Option-A: R-NN IDs]` — bare prefix (C-43 FAIL), `column:` absent (C-42 FAIL)
Both have C-40 PASS (row-label prefix present in both forms). V-01 isolates C-42; V-04 isolates C-42 + C-43.

**V-02 vs V-04 key distinction:**
- V-02: `row: [Option-A column: R-NN IDs]` — bare prefix (C-43 FAIL), `column:` present (C-42 PASS)
- V-04: `row: [Option-A: R-NN IDs]` — bare prefix (C-43 FAIL), `column:` absent (C-42 FAIL)
V-02 isolates C-43; V-04 isolates C-42 + C-43.

**v16 exemplar (all four new criteria pass):**
`Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]`
→ C-40 PASS (row-label prefix present), C-43 PASS (compound `Risk row:` form), C-42 PASS (`column:`
designators in each bracket), C-37 PASS (per-column enumeration present).
