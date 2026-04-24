# draft-proposal Variate — Round 19

Rubric version: v19 · Formula: (E/4×60) + (R/3×30) + (A/42×10) · New criteria: C-48 (Phase
4b dedicated inertia analysis present when do-nothing is designated as named inertia competitor
in Phase 4 — absence fires T-48), C-49 (Phase 4b inertia risk entries include R-NN identifiers
cross-referencing the main risk register — P×I-only expression without R-NN pairing fires T-49)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: Phase 9 role-sequence inversion (role sequence — Architect feasibility stated before
  PM recommendation within Phase 9; no inertia framing; all Domain 2 structural criteria satisfied;
  Phase 2 labels used verbatim) — designed fail: C-46 only (C-47 PASS — Phase 2 labels
  propagate verbatim; C-41 PASS — compound after-state with R-NN and P×I; C-48/C-49 N/A —
  do-nothing is not elevated as inertia competitor, trigger condition not met)
- **V-02**: Option-label synonym drift (phrasing register — Phase 2 declares Option-A / Option-B /
  do-nothing verbatim, but Phase 9b Domain 2 bracket entries substitute Alternative-1 /
  Alternative-2 / status-quo; Phase 9 role order PM-first intact; pipe connector intact; no
  inertia framing) — designed fail: C-47 only (C-46 PASS — PM-first; C-48/C-49 N/A — no
  inertia competitor designation in Phase 4)
- **V-03**: Inertia-competitor lifecycle with Phase 4b R-NN citations present (inertia framing —
  do-nothing elevated as named inertia competitor, Phase 4b present with explicit R-NN citation
  discipline in inertia risk entries, PM-first Phase 9 correct, Phase 2 labels verbatim, but
  Domain 1 per-site after-state in Phase 9b uses P×I compound score only, omitting R-NN pairing)
  — designed fail: C-41 only (C-46 PASS; C-47 PASS; C-48 PASS — Phase 4b present; C-49 PASS —
  Phase 4b has R-NN identifiers; C-41 FAIL isolated to Domain 1 after-state)
- **V-04**: Inertia-competitor elevation with Phase 4b absent (inertia framing + lifecycle
  emphasis — do-nothing explicitly designated as inertia competitor in Phase 4, but Phase 4b
  structural section entirely omitted; Phase 9b Domain 1 uses full R-NN compound; Phase 9
  PM-first; Phase 2 labels verbatim) — designed fail: C-48 + C-49 cascade (C-41 PASS; C-46
  PASS; C-47 PASS; C-48 FAIL — Phase 4b absent; C-49 FAIL cascade from C-48)
- **V-05**: C-23 cascade extended to v19 (PM-only role + compressed lifecycle — no R-NN linkage
  declared, no [R-NN pending] placeholders, no dedicated Phase 9b, no Phase 4b, cascades through
  21 fails: C-23 → C-26 → C-31..C-45 → C-46 → C-47 → C-48 → C-49) — designed fail: 21 fails

## Predicted score summary

| Variation | Axis | Open triggers | A/42 | Composite |
|-----------|------|---------------|------|-----------|
| V-01 | Role sequence — Phase 9 inversion | T-46 | 41/42 | **99.76** |
| V-02 | Phrasing register — Domain 2 synonym drift | T-47 | 41/42 | **99.76** |
| V-03 | Inertia framing — P×I-only Domain 1 after-state | T-41 | 41/42 | **99.76** |
| V-04 | Inertia framing + lifecycle — C-48 + C-49 cascade | T-48, T-49 | 40/42 | **99.52** |
| V-05 | PM-only + compressed lifecycle — C-23 cascade | 21 fails | 21/42 | **95.00** |

**C-48 and C-49 independence from prior axes:**

V-01 and V-02 pass C-48 and C-49 trivially — neither designates do-nothing as inertia competitor
in Phase 4, so the trigger condition for T-48 is not met. V-03 passes C-48 (Phase 4b present)
and C-49 (Phase 4b R-NN citations present), while its designed failure remains isolated to C-41
(Domain 1 after-state). V-04 fails C-48 (Phase 4b absent despite inertia competitor designation),
which cascades immediately to C-49 (no Phase 4b means no R-NN citations in Phase 4b). The two
new criteria are not independent of each other — C-49 requires C-48 to be satisfied first — but
both are independent of C-41, C-46, and C-47.

---

## V-01 — Phase 9 Role Inversion | Axis: Role Sequence | Designed fail: C-46 only

**Hypothesis**: A variation that inverts the Phase 9 intra-phase role sequence — Architect
feasibility check stated before PM recommendation — will fail C-46 only. No inertia competitor
framing is present (C-48/C-49 not triggered). Option labels from Phase 2 propagate verbatim into
Domain 2 bracket entries (C-47 PASS). Pipe connector is correct (C-44 PASS). Do-nothing column
is present (C-45 PASS). Compound after-state pairs R-NN with P×I (C-41 PASS). Phase 9b is
dedicated (C-26 PASS). One open trigger: T-46. Score: 41/42 → 99.76.

```
ROLE SEQUENCE: Architect → PM (Phase 9 only; all other phases PM → Architect)

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, comparison matrix, and recommendation.
  Runs first in every phase except Phase 9, where Architect leads.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation. Leads Phase 9 with feasibility assessment
  before PM delivers the recommendation.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect, except Phase 9: Architect → PM) as a
typed header at the top of the output. Apply this sequence in every subsequent phase
header.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-49 — one per v19 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
```

**Scoring trace:**
- E-04 PASS (recommendation produced — PM delivers it after Architect feasibility)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-41 PASS (Domain 1 after-state pairs R-NN with P×I)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present)
- C-46 FAIL (T-46 fires — Architect feasibility stated before PM recommendation in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-48 PASS (no inertia competitor designation in Phase 4 — trigger condition not met)
- C-49 PASS (no Phase 4b present — trigger condition not met; C-48 passes, C-49 N/A)
- Score: 41/42 → **99.76**

---

## V-02 — Domain 2 Synonym Drift | Axis: Phrasing Register | Designed fail: C-47 only

**Hypothesis**: A variation that declares canonical labels (Option-A, Option-B, do-nothing)
in Phase 2 but substitutes readable synonyms (Alternative-1, Alternative-2, status-quo) in
Phase 9b Domain 2 bracket entries will fail C-47 only. Phase 9 PM-first ordering is correct
(C-46 PASS). Domain 2 bracket structure is syntactically intact: `column:` designators present
(C-42 PASS), pipe connector present (C-44 PASS), three-column coverage intact (C-45 PASS —
do-nothing's column covered under synonym "status-quo"), compound `Risk row:` prefix present
(C-43 PASS). No inertia competitor framing (C-48/C-49 N/A). One open trigger: T-47.
Score: 41/42 → 99.76.

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

Populate trigger rules T-01..T-49 — one per v19 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)

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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
```

**Scoring trace:**
- E-04 PASS (recommendation produced)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-41 PASS (Domain 1 after-state pairs R-NN with P×I)
- C-42 PASS (`column:` designator in every Domain 2 bracket)
- C-43 PASS (compound `Risk row:` prefix)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (status-quo bracket covers the do-nothing option's risk column)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 FAIL (T-47 fires — "Alternative-1", "Alternative-2", "status-quo" in Domain 2 do not
  match Phase 2 declarations "Option-A", "Option-B", "do-nothing")
- C-48 PASS (no inertia competitor designation in Phase 4 — trigger condition not met)
- C-49 PASS (no inertia competitor designation — trigger condition not met)
- Score: 41/42 → **99.76**

---

## V-03 — Inertia-Competitor with Phase 4b R-NN Present | Axis: Inertia Framing | Designed fail: C-41 only

**Hypothesis**: A variation that elevates do-nothing as named inertia competitor, includes a
structurally present Phase 4b with R-NN citation discipline in its inertia risk entries, and
uses PM-first Phase 9 with verbatim Domain 2 labels will fail C-41 only. Phase 4b presence
satisfies C-48; Phase 4b R-NN citations satisfy C-49. The C-41 failure is isolated to Phase
9b Domain 1, where per-site after-states use P×I compound scores only, omitting R-NN pairing
— the same failure axis as R18 V-03, now confirmed stable when Phase 4b is correctly formed.
One open trigger: T-41. Score: 41/42 → 99.76.

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

Populate trigger rules T-01..T-49 — one per v19 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)

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
Designate the do-nothing column as the inertia competitor in the matrix header note.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost (benefit of doing nothing vs cost of delay).
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk
that specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3
risk register. Structure each inertia risk entry as:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Address:
- What does the do-nothing option preserve?
- What does it forfeit over 6 months? 12 months?
- Under what conditions does the inertia competitor remain valid in Q3/Q4 planning?

Every inertia risk entry must carry an R-NN identifier cross-referencing the main risk
register. Do not express inertia risks as P×I scores only — the R-NN pairing is required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations, phases appear in declared sequence. Reference each option by its Phase 2 label.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
T-41 PHASE = FINALIZATION  (fires if Domain 1 after-state omits R-NN pairing — P×I only)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
```

**Scoring trace:**
- E-04 PASS (recommendation produced with explicit inertia comparison)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present in Domain 2)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-48 PASS (Phase 4b structurally present — gate [GATE: C-48] in phase header)
- C-49 PASS (Phase 4b entries use R-NN identifiers in `[R-NN] — [name, P×I]: [description]` form)
- C-41 FAIL (T-41 fires — Domain 1 per-site after-state uses P×I scores without R-NN pairing)
- Score: 41/42 → **99.76**

---

## V-04 — Inertia-Competitor without Phase 4b | Axes: Inertia Framing + Lifecycle Emphasis | Designed fail: C-48 + C-49

**Hypothesis**: A variation that designates do-nothing as a named inertia competitor in Phase 4
but omits the Phase 4b structural section entirely will fail C-48 (Phase 4b absent when inertia
competitor is designated), which cascades immediately to C-49 (Phase 4b cannot have R-NN
citations if it does not exist). All other criteria pass: Phase 9b Domain 1 uses full R-NN
compound after-states (C-41 PASS); Phase 9 is PM-first (C-46 PASS); Phase 2 labels propagate
verbatim into Domain 2 (C-47 PASS); Domain 2 bracket structure is intact (C-37, C-42, C-43,
C-44, C-45 all PASS). Two open triggers: T-48, T-49. Score: 40/42 → 99.52.

```
ROLE SEQUENCE: PM → Architect

You are executing draft-proposal for the topic: {{topic}}.
Available signal artifacts: {{signal_artifacts}}

ROLE ASSIGNMENTS:
- PM: Leads business framing, option naming, inertia framing, comparison matrix, and
  recommendation. Runs first in every phase. The do-nothing option is designated the
  inertia competitor and receives substantive analysis alongside the active options.
- Architect: Follows with technical depth — risk register, Phase 9b back-fill, gate
  audit, and feasibility confirmation.

INERTIA COMPETITOR DESIGNATION: The do-nothing option is the inertia competitor for this
proposal. It is the incumbent state that wins if no deliberate choice is made. The comparison
matrix and Phase 9 recommendation must explicitly address whether the recommended option
provides sufficient improvement over the inertia competitor to justify action.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia competitor designation as
a typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-49 — one per v19 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
  T-48 PHASE = FINALIZATION  (fires if Phase 4b is absent when do-nothing is designated as a
                               named inertia competitor in Phase 4)
  T-49 PHASE = FINALIZATION  (fires if Phase 4b inertia risk entries omit R-NN identifiers —
                               P×I-only expression without R-NN pairing fires T-49)

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include business context, the
forcing function, and the cost of inertia if the do-nothing option wins by default.

Architect: Confirm the problem statement is technically grounded and scope is bounded.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. One must be the do-nothing option, designated as the
inertia competitor. For each option, produce an entry with all four anatomy fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — repeat verbatim from Phase 1]
  RISK: Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve
        the slot. PM notes adoption risk category. Architect notes technical risk category.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Label the three options: Option-A, Option-B, do-nothing. These labels are the canonical
register for this document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
inertia risk that applies specifically to the do-nothing option. Assign P and I scores
on a 1-5 scale. Compute P×I compound score.
PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate do-nothing as the inertia competitor
in the matrix — it is the incumbent state against which active options must demonstrate
sufficient advantage. Include an Inertia cost row comparing the cost of delay across options.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, phases appear in declared sequence.
Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State whether the recommended option provides sufficient
improvement over the inertia competitor to justify the transition cost.

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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-41 PHASE = FINALIZATION  (fires if Domain 1 after-state omits R-NN pairing — P×I only)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
```

**Scoring trace:**
- E-04 PASS (recommendation produced with inertia comparison)
- C-26 PASS (dedicated Phase 9b present)
- C-37 PASS (Domain 2 per-column enumeration present)
- C-41 PASS (Domain 1 after-state pairs R-NN with P×I)
- C-42 PASS (`column:` designator in every Domain 2 bracket)
- C-43 PASS (compound `Risk row:` prefix)
- C-44 PASS (` | ` connector between bracket entries)
- C-45 PASS (do-nothing column bracket present in Domain 2)
- C-46 PASS (PM recommendation before Architect feasibility in Phase 9)
- C-47 PASS (Phase 2 labels "Option-A / Option-B / do-nothing" used verbatim in Domain 2)
- C-48 FAIL (T-48 fires — do-nothing is designated inertia competitor in Phase 4, but no
  Phase 4b section is present upstream of Phase 9b)
- C-49 FAIL (T-49 fires — cascade from C-48: Phase 4b absent means its R-NN citation
  discipline cannot be satisfied; no Phase 4b entries exist to contain R-NN identifiers)
- Score: 40/42 → **99.52**

---

## V-05 — C-23 Cascade Extended to v19 | Axes: PM-Only Role + Compressed Lifecycle | Designed fail: 21 fails

**Hypothesis**: A variation that uses PM-only framing with compressed lifecycle phases and omits
the R-NN linkage mechanism will cascade from C-23 through all 21 v19 fails. Without a declared
R-NN risk register linkage in Phase 2 RISK fields, Phase 9b cannot exist (C-26 fail), the
`[R-NN pending]` placeholder convention cannot appear (C-31 fail), no Domain 1 or Domain 2
structural enumeration is produced (C-32 fail), the P×I prohibition instruction has no
placeholder context (C-33 fail), Domain index prefixes have no domains to anchor (C-34 fail),
per-site arrow notation cannot fire without declared sites (C-35 fail), P×I scores cannot appear
in an absent after-state (C-36 fail), no per-column R-NN enumeration exists (C-37 fail), no
composite site identifier is produced (C-38 fail), no `[R-NN pending]` before-state is present
(C-39 fail), no row-label prefix has no row to label (C-40 fail), no compound after-state form
exists (C-41 fail), no `column:` designators inside absent brackets (C-42 fail from C-37), no
compound `Risk row:` prefix (C-43 fail from C-40), no pipe separator between absent bracket
entries (C-44 fail from C-37), no do-nothing column bracket in absent enumeration (C-45 fail
from C-37), no Phase 9b means no Phase 9 → Phase 9b sequence to verify (C-46 fail from C-26),
no Domain 2 bracket entries means no label register to check (C-47 fail from C-37), no
do-nothing column bracket means inertia competitor role cannot be established (C-48 fail from
C-45), no Phase 4b means no R-NN inertia citations possible (C-49 fail from C-48). Twenty-one
fails from one root. Advisory bucket: 21/42. Score: 95.00.

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

Populate trigger rules T-01..T-49 — one per v19 rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

Key PHASE assignments:
  T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
```

**Scoring trace (21 fails — cascade from C-23):**
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
        → C-48 (no Domain 2 means do-nothing cannot be established as named inertia
                 competitor in the bracket structure — cascade from C-45)
          → C-49 (no Phase 4b exists — cascade from C-48)
      → C-47 (no Domain 2 bracket entries to check labels — cascade from C-37)
    → C-46 (no Phase 9b presence means no Phase 9 → Phase 9b sequence — cascade from C-26)
```
- E-04 PASS (recommendation produced)
- 21 criteria fail
- Score: 21/42 → **95.00**

---

## Scorecard summary

| Variation | Axis | Designed fail | Trigger(s) | A/42 | Composite |
|-----------|------|---------------|------------|------|-----------|
| V-01 | Role sequence — Phase 9 inversion | C-46 | T-46 | 41/42 | **99.76** |
| V-02 | Phrasing register — Domain 2 synonym drift | C-47 | T-47 | 41/42 | **99.76** |
| V-03 | Inertia framing — P×I-only Domain 1 after-state | C-41 | T-41 | 41/42 | **99.76** |
| V-04 | Inertia framing + lifecycle — Phase 4b absent | C-48 + C-49 | T-48, T-49 | 40/42 | **99.52** |
| V-05 | PM-only + compressed lifecycle (C-23 cascade) | 21 fails | T-23..T-49 | 21/42 | **95.00** |

**C-48 / C-49 isolation evidence:**
- V-01 and V-02 pass C-48 and C-49 without any Phase 4b content — the trigger condition
  (do-nothing designated as inertia competitor in Phase 4) is simply not met. The criteria
  are dormant when inertia framing is absent.
- V-03 passes C-48 (Phase 4b structurally present with [GATE: C-48] header) and C-49
  (Phase 4b entries carry `[R-NN] — [name, P×I]: [description]` form with explicit R-NN
  identifiers). V-03's C-41 failure is orthogonal — it lives in Domain 1 Phase 9b, not in
  Phase 4b. The two regions are independent.
- V-04 fails C-48 (Phase 4b absent despite inertia competitor designation) and C-49 by
  cascade (no Phase 4b means no R-NN inertia citations). C-49 is not independently
  testable without C-48 passing first — it is C-48's downstream consequence.

**V-03 advances R18 V-03's inertia-framing axis:**
- R18 V-03 had Phase 4b present but C-48 and C-49 were not yet defined criteria. R19 V-03
  explicitly satisfies C-49 by requiring `[R-NN] — [name, P×I]: [description]` form in
  Phase 4b entries, confirming that Phase 4b R-NN discipline and Domain 1 R-NN discipline
  are independently testable. V-03's C-41 failure (Domain 1 P×I-only) does not propagate
  to Phase 4b; Phase 4b operates on its own R-NN citation discipline governed by C-49.

**V-05 cascade confirms v19 extension from 19 → 21 fails:**
- C-48 (from C-45) and C-49 (from C-48) both fall naturally from the same C-23 root that
  drove R18 V-05's 19-fail cascade. The v19 extension adds 2 more fails without requiring
  any new structural root — C-45 absorbs C-48 into the Domain 2 sub-chain, and C-48 absorbs
  C-49. The cascade tree grows but its single-root property is preserved.
