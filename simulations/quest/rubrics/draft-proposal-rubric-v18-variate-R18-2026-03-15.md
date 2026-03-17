# draft-proposal Variate — Round 18

Rubric version: v18 · Formula: (E/4×60) + (R/3×30) + (A/40×10) · New criteria: C-46 (Phase 9
role-sequence order: PM recommendation precedes Architect feasibility check within Phase 9 —
Architect-before-PM fires T-46), C-47 (option-label register consistency across phases: Phase 2
label declarations must appear verbatim in Phase 4 column headers, Phase 6 option count, and
Phase 9b Domain 2 bracket entries — synonym substitution fires T-47)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Phase 9 role-sequence inversion (role sequence — Architect feasibility stated before
  PM recommendation within Phase 9, all other phases structurally correct, Domain 2 full
  per-column bracket enumeration with ` | ` connector and do-nothing column present, Phase 2
  labels used verbatim in Domain 2) — designed fail: C-46 only (C-47 PASS — Phase 2 labels
  propagate verbatim; C-44 PASS — pipe connector intact; C-45 PASS — do-nothing column present;
  C-41 PASS — compound after-state with R-NN and P×I; E-04 PASS — recommendation produced)
- **V-02**: Option-label synonym drift (phrasing register — Phase 2 declares Option-A / Option-B /
  do-nothing verbatim, but Phase 9b Domain 2 bracket entries substitute Alternative-1 /
  Alternative-2 / status-quo; Phase 9 role order PM-first intact; pipe connector intact; all
  Domain 2 structural criteria satisfied) — designed fail: C-47 only (C-46 PASS — PM-first in
  Phase 9; C-44 PASS — pipe connector; C-45 PASS — do-nothing-column bracket present under new
  label; C-42 PASS — `column:` designators present; C-43 PASS — compound `Risk row:` prefix)
- **V-03**: Inertia-competitor lifecycle (inertia framing — do-nothing elevated as named "inertia
  competitor" across all phases, Phase 9 PM-first correct, Phase 2 labels verbatim in Domain 2,
  pipe connector intact, but Domain 1 per-site after-state uses P×I compound score only, omitting
  R-NN pairing) — designed fail: C-41 only (C-46 PASS — PM before Architect; C-47 PASS — labels
  verbatim; C-44 PASS — pipe connector; C-45 PASS — do-nothing column)
- **V-04**: C-46 + C-47 combined isolation (role sequence + phrasing register — Architect
  feasibility before PM recommendation AND Phase 2 labels do not appear in Domain 2 bracket
  entries, comma connector between bracket entries also absent correct form) — designed fail:
  C-46 + C-47 (C-37 PASS — per-column enumeration present; C-40 PASS — `Risk row:` prefix;
  C-42 PASS — `column:` designators; C-43 PASS — compound form; C-44 PASS — pipe connector;
  C-45 PASS — do-nothing bracket present)
- **V-05**: C-23 cascade extended to v18 (PM-only role + compressed lifecycle — no R-NN linkage
  declared, no [R-NN pending] placeholders, no dedicated Phase 9b, cascades through 19 fails:
  C-23 → C-26 → C-31..C-45 → C-46 → C-47) — designed fail: 19 fails

## Predicted score summary

| Variation | Axis | Open triggers | A/40 | Composite |
|-----------|------|---------------|------|-----------|
| V-01 | Role sequence — Phase 9 inversion | T-46 | 39/40 | **99.75** |
| V-02 | Phrasing register — Domain 2 synonym drift | T-47 | 39/40 | **99.75** |
| V-03 | Inertia framing — P×I-only after-state | T-41 | 39/40 | **99.75** |
| V-04 | Role sequence + phrasing register — C-46 + C-47 | T-46, T-47 | 38/40 | **99.50** |
| V-05 | PM-only + compressed lifecycle — C-23 cascade | 19 fails | 21/40 | **95.25** |

**C-46 and C-47 independence evidence:**

V-01 passes C-47 (Phase 2 labels propagate verbatim into Domain 2) while failing C-46 (Architect
before PM). V-02 passes C-46 (PM first in Phase 9) while failing C-47 (synonym substitution in
Domain 2). V-04 fails both. Independence is confirmed: neither failure causes the other; C-46
governs Phase 9 role sequence, C-47 governs cross-phase label register. Two independent axes,
both cascade from criteria already in the V-05 failure chain (C-26 and C-37).

---

## V-01 — Phase 9 Role Inversion | Axis: Role Sequence | Designed fail: C-46 only

**Hypothesis**: A variation that inverts the Phase 9 intra-phase role sequence — Architect
feasibility check stated before PM recommendation — will fail C-46 only. All other criteria
pass: option labels from Phase 2 propagate verbatim into Domain 2 bracket entries (C-47 PASS);
pipe connector is correct (C-44 PASS); do-nothing column is present (C-45 PASS); compound
after-state pairs R-NN with P×I (C-41 PASS); Phase 9b is dedicated (C-26 PASS). One open
trigger: T-46. Score: 39/40 → 99.75.

```
ROLE SEQUENCE: Architect → PM (Phase 9 only; all other phases PM → Architect)

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, comparison matrix, and recommendation.
  Runs first in every phase except Phase 9, where Architect leads.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate audit,
  and feasibility confirmation. Leads Phase 9 with feasibility assessment before PM
  delivers the recommendation.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect, except Phase 9: Architect → PM) as a typed
header at the top of the output. Apply this sequence in every subsequent phase header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per v18 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
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
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator — [Option-X: R-NN IDs] form fires T-42)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form — bare `row:` prefix fires T-43)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9 — PM output must appear first)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context and
the forcing function making this decision necessary now.

Architect: Confirm the problem statement is technically grounded and scope is bounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: the labels declared here (e.g., Option-A, Option-B, do-nothing)
are the canonical labels for this document. Use them unchanged in all downstream phases.

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

PM: Build a comparison matrix with OPTIONS as column headers. Use the option labels
declared in Phase 2 verbatim as column headers.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited).
Architect: Add Effort and Integration complexity as rows.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, phases appear in declared sequence. Reference options by their Phase 2 labels.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

Architect: Confirm technical feasibility of each option. State which options are
technically viable given the risk register findings.

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions for the recommendation.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-47 — exactly 47 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
```

**Scoring trace:**
- E-04 PASS (recommendation produced — PM delivers it, Architect confirmed feasibility)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present)
- C-46 FAIL (T-46 fires — Architect feasibility stated before PM recommendation in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- Score: 39/40 → **99.75**

---

## V-02 — Domain 2 Synonym Drift | Axis: Phrasing Register | Designed fail: C-47 only

**Hypothesis**: A variation that declares canonical labels (Option-A, Option-B, do-nothing) in
Phase 2 but substitutes readable synonyms (Alternative-1, Alternative-2, status-quo) in
Phase 9b Domain 2 bracket entries will fail C-47 only. Phase 9 PM-first ordering is correct
(C-46 PASS). Domain 2 bracket structure is syntactically intact: `column:` designators present
(C-42 PASS), pipe connector present (C-44 PASS), three-column coverage intact (C-45 PASS —
do-nothing's column is covered under the synonym "status-quo"), compound `Risk row:` prefix
present (C-43 PASS). One open trigger: T-47. Score: 39/40 → 99.75.

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

PM: Declare the role sequence (PM → Architect) as a typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per v18 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
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
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form — bare `row:` prefix fires T-43)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context and
the forcing function making this decision necessary now.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Use clear, reader-friendly option names. Three options: one that builds the feature
(Option-A), one that integrates an existing tool (Option-B), and one that keeps the
current approach (do-nothing). Label them naturally; their clear, descriptive summaries
will be rendered in the comparison matrix under these same names.

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

PM: Build a comparison matrix. Column headers are the option names from Phase 2.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited).
Architect: Add Effort and Integration complexity as rows. For readability in the matrix,
use friendly column labels that reflect each option's essence — the reader should grasp
each option at a glance from the column header alone.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present, risk register has at least 3
entries, phases appear in declared sequence. Name each option as it appeared in Phase 2.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
  Domain 2 — Comparison matrix risk column:
    For the matrix risk row, enumerate R-NN assignments per option using the column labels
    that appear in the comparison matrix. Use reader-friendly column names that match the
    matrix headers for navigability.
    Risk row: [Alternative-1 column: R-NN IDs] | [Alternative-2 column: R-NN IDs] | [status-quo column: R-NN IDs]

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

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-47 — exactly 47 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
```

**Scoring trace:**
- E-04 PASS (recommendation produced)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-42 PASS (`column:` designator in every Domain 2 bracket)
- C-43 PASS (compound `Risk row:` prefix)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (status-quo bracket covers the do-nothing option's risk column)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 FAIL (T-47 fires — "Alternative-1", "Alternative-2", "status-quo" in Domain 2 do not
  match Phase 2 declarations "Option-A", "Option-B", "do-nothing")
- Score: 39/40 → **99.75**

---

## V-03 — Inertia-Competitor Lifecycle | Axis: Inertia Framing | Designed fail: C-41 only

**Hypothesis**: A variation that frames the do-nothing option as a named "inertia competitor"
throughout — giving it equal analytical weight and a dedicated inertia section — will produce
rich do-nothing analysis while passing both new criteria (C-46 PM-first, C-47 label register)
but failing C-41 (compound after-state form) because Domain 1 per-site after-states are
expressed as P×I scores only, without pairing R-NN identifiers. C-46 PASS; C-47 PASS; C-44
PASS; C-45 PASS. One open trigger: T-41. Score: 39/40 → 99.75.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, inertia analysis, comparison matrix, and
  recommendation. Runs first in every phase. PM gives equal analytical weight to the
  do-nothing option as an inertia competitor — not a straw man.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation.

INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken. Every
analysis section must address why the inertia competitor is or is not adequate. The
recommendation must explicitly state whether it beats the inertia competitor and on which
dimensions.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per v18 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
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
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap,
the forcing function, and what the inertia competitor (do-nothing) would cost the team
if it wins by default.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor, labeled
`do-nothing`. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

  For the do-nothing option specifically, RATIONALE must articulate the inertia case:
  why is the status quo a legitimate choice? What conditions would make it the right answer?

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on a 1-5 scale. Compute P×I.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim as column headers: Option-A | Option-B | do-nothing.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost (benefit of doing nothing vs cost of delay).
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-21]

PM: Produce a dedicated inertia analysis section. Address:
- What specifically does the do-nothing option preserve?
- What does it forfeit over 6 months? 12 months?
- Under what conditions does the inertia competitor remain valid in Q3/Q4 planning?

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, phases appear in declared
sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → P×I scores for applicable risks
    [Option-B] RISK field: [R-NN pending] → P×I scores for applicable risks
    [do-nothing] RISK field: [R-NN pending] → P×I scores for applicable risks, including
                              inertia risks unique to this option
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each Domain 2 column entry.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State explicitly whether the recommendation beats the
inertia competitor and on what basis.

Architect: Confirm technical feasibility of the recommended option.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-47 — exactly 47 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
T-41 PHASE = FINALIZATION  (fires if Domain 1 after-state omits R-NN pairing — P×I only)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
```

**Scoring trace:**
- E-04 PASS (recommendation produced with explicit inertia comparison)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present in Domain 2)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-41 FAIL (T-41 fires — Domain 1 per-site after-state uses P×I scores without R-NN pairing)
- Score: 39/40 → **99.75**

---

## V-04 — C-46 + C-47 Combined | Axes: Role Sequence + Phrasing Register | Designed fail: C-46 + C-47

**Hypothesis**: A variation that uses PM-initial framing in the preamble but inverts Phase 9
to Architect-first AND substitutes synonym labels in Domain 2 will fail both C-46 and C-47
while passing all other criteria. C-37 PASS (per-column enumeration present); C-40 PASS
(`Risk row:` prefix); C-42 PASS (`column:` designators); C-43 PASS (compound form); C-44 PASS
(pipe connector); C-45 PASS (do-nothing bracket under synonym label); C-41 PASS (compound
after-state with R-NN and P×I). Two open triggers: T-46, T-47. Score: 38/40 → 99.50.

```
ROLE SEQUENCE: PM → Architect (reversed in Phase 9: Architect → PM)

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads option framing and business analysis in Phases 1-8. Delivers the final
  recommendation in Phase 9, but only after Architect technical assessment.
- Architect: Follows PM in Phases 1-8 with technical depth. Opens Phase 9 with a
  feasibility assessment to anchor the PM recommendation.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence at the top of the output. Note that Phase 9 inverts order:
Architect feasibility assessment precedes PM recommendation.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per v18 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
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
  T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN entries
                               and P×I scores together in a single compound expression)
  T-42 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries do not carry the
                               `column:` axis-designator)
  T-43 PHASE = FINALIZATION  (fires if Domain 2 row-label prefix is not the compound `Risk row:`
                               form)
  T-44 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket entries use comma, semicolon,
                               newline, or juxtaposition instead of ` | ` between entries)
  T-45 PHASE = FINALIZATION  (fires if Domain 2 per-column bracket enumeration does not include
                               a named column entry for the do-nothing option)
  T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect feasibility check precedes PM
                               recommendation within Phase 9)
  T-47 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 bracket label text does not match the
                               option label declared in Phase 2 verbatim)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context and
the forcing function making this decision necessary now.

Architect: Confirm the problem statement is technically grounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be a do-nothing or status-quo option. For each
option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Label the three options: Option-A, Option-B, do-nothing.

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

PM: Build a comparison matrix with OPTIONS as column headers. Write column headers that
read naturally to an executive audience — descriptive names that capture each option's
essence work better than technical identifiers in this context.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending] placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries, R-NN: P×I compound scores]
  Domain 2 — Comparison matrix risk column:
    Use the column labels that appear in the comparison matrix for navigability. Produce
    the per-column enumeration in the `Risk row:` bracket form with ` | ` separators.
    Risk row: [Build column: R-NN IDs] | [Integrate column: R-NN IDs] | [Defer column: R-NN IDs]

Confirm P×I formula applied at each named domain site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

Architect: Assess the technical feasibility of each option. State which options are viable
and flag any disqualifying technical risks before the PM delivers the recommendation.

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions for the recommendation.

---

PHASE 10 — FINALIZATION [GATE: R-03]

Execute coverage verification as an explicitly numbered four-step list:

Step 1: Review the amendment table for trigger rules with STATUS = OPEN.
  For each open trigger T-NN, produce a finding entry:
    "Finding N: T-NN — [criterion ID and full name].
     Expected: [what the trigger required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.

---

AMENDMENT TABLE SPECIFICATION

Trigger rules T-01..T-47 — exactly 47 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
```

**Scoring trace:**
- E-04 PASS (recommendation produced)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-42 PASS (`column:` designator in every Domain 2 bracket)
- C-43 PASS (compound `Risk row:` prefix)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS ("Defer column" bracket covers do-nothing's risk column)
- C-41 PASS (Domain 1 after-state pairs R-NN with P×I)
- C-46 FAIL (T-46 fires — Architect feasibility in Phase 9 precedes PM recommendation)
- C-47 FAIL (T-47 fires — "Build", "Integrate", "Defer" in Domain 2 do not match Phase 2
  declarations "Option-A", "Option-B", "do-nothing")
- Score: 38/40 → **99.50**

---

## V-05 — C-23 Cascade Extended to v18 | Axes: PM-Only Role + Compressed Lifecycle | Designed fail: 19 fails

**Hypothesis**: A variation that uses PM-only framing with compressed lifecycle phases and omits
the R-NN linkage mechanism will cascade from C-23 through all 19 v18 fails. Without a declared
R-NN risk register linkage in Phase 2 RISK fields, Phase 9b cannot exist (C-26 fail), the
`[R-NN pending]` placeholder convention cannot appear (C-31 fail), no Domain 1 or Domain 2
structural enumeration is produced (C-32 fail), the P×I prohibition instruction has no
placeholder context (C-33 fail), Domain index prefixes have no domains to anchor (C-34 fail),
per-site arrow notation cannot fire without declared sites (C-35 fail), P×I scores cannot appear
in an absent after-state (C-36 fail), no per-column R-NN enumeration exists (C-37 fail), no
composite site identifier is produced (C-38 fail), no `[R-NN pending]` before-state placeholder
is present (C-39 fail), no row-label prefix has no row to label (C-40 fail), no compound
after-state form exists (C-41 fail), no `column:` designators inside absent brackets (C-42 fail
from C-37), no compound `Risk row:` prefix (C-43 fail from C-40), no pipe separator between
absent bracket entries (C-44 fail from C-37), no do-nothing column bracket in absent enumeration
(C-45 fail from C-37), no Phase 9b means no PM-before-Architect sequence to verify in the
Phase 9 → Phase 9b context (C-46 fail from C-26), no Domain 2 bracket entries means no label
register to check (C-47 fail from C-37). Nineteen fails from one root. Advisory bucket: 21/40.
Score: 95.25.

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

Populate trigger rules T-01..T-47 — one per v18 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
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
  RISK: [key risks, described in plain language — note any technical dependencies inline]
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
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

Trigger rules T-01..T-47 — exactly 47 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 47)
```

**Scoring trace (19 fails — cascade from C-23):**
```
C-23 (R-NN linkage absent from Phase 2 RISK fields)
  → C-26 (no dedicated Phase 9b — cannot exist without R-NN mechanism)
    → C-31 (no [R-NN pending] placeholder — no Phase 9b to require it)
    → C-32 (no domain enumeration — no citation sites declared)
    → C-33 (no P×I prohibition instruction — no placeholder to guard)
    → C-34 (no domain numeric index — no domains to index)
    → C-35 (no per-site arrow notation — no sites to transition)
    → C-36 (no per-site P×I after-state — no after-state produced)
    → C-37 (no per-column R-NN enumeration — no Domain 2 produced)
      → C-38 (no composite site identifier — no sites in Domain 1)
      → C-39 (no [R-NN pending] before-state — no placeholder used)
      → C-40 (no `Risk row:` prefix — no risk row present)
        → C-41 (no compound after-state — no after-state at all)
        → C-43 (no compound `Risk row:` form — no risk row at all)
      → C-42 (no `column:` designators — cascade from C-37)
      → C-44 (no ` | ` pipe connector — cascade from C-37)
      → C-45 (no do-nothing column bracket — cascade from C-37)
      → C-47 (no Domain 2 bracket entries to check labels — cascade from C-37)
    → C-46 (no Phase 9b presence means no Phase 9→9b sequence to verify — cascade from C-26)
```
- E-04 PASS (recommendation produced)
- 19 criteria fail
- Score: 21/40 → **95.25**

---

## Scorecard summary

| Variation | Axis | Designed fail | Trigger(s) | A/40 | Composite |
|-----------|------|---------------|------------|------|-----------|
| V-01 | Role sequence — Phase 9 inversion | C-46 | T-46 | 39/40 | **99.75** |
| V-02 | Phrasing register — Domain 2 synonym drift | C-47 | T-47 | 39/40 | **99.75** |
| V-03 | Inertia framing — P×I-only after-state | C-41 | T-41 | 39/40 | **99.75** |
| V-04 | Role sequence + phrasing register | C-46 + C-47 | T-46, T-47 | 38/40 | **99.50** |
| V-05 | PM-only + compressed lifecycle (C-23 cascade) | 19 fails | T-23..T-47 | 21/40 | **95.25** |

**C-46 / C-47 independence confirmed:**
- V-01 passes C-47 while failing C-46: Phase 9 role inversion does not disturb Domain 2 label
  register. The two criteria govern orthogonal structural locations.
- V-02 passes C-46 while failing C-47: PM-first ordering in Phase 9 is compatible with synonym
  drift in Domain 2. Neither failure causes the other.
- V-04 combines both failures: they co-exist without interaction, each satisfying its independent
  trigger condition.

**V-03 isolation confirms existing criteria are stable under inertia framing:**
- Elevated do-nothing analysis does not disturb C-46 or C-47; inertia framing is an orthogonal
  document dimension. The C-41 failure (P×I-only after-state) is the unique axis under test.

**V-05 cascade confirms v18 extension from 17 → 19 fails:**
- C-46 (from C-26) and C-47 (from C-37) both fall naturally from the same C-23 root that
  drove R17 V-05's 17-fail cascade. The v18 extension adds 2 more fails without requiring
  a new root; the cascade is structurally deeper, not structurally wider.
