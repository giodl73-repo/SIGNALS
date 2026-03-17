# draft-proposal Variate — Round 17

Rubric version: v17 · Formula: (E/4×60) + (R/3×30) + (A/36×10) · New criteria: C-42
(T-40 CONDITION carries inline failure exemplar of deficient T-38 CONDITION), C-43
(T-40 CONDITION carries correct-format prescription showing passing T-38 CONDITION)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: T-40 CONDITION abstract (lifecycle emphasis — trigger description present, no
  CONDITION content guidance; LLM writes abstract T-40 CONDITION) — designed fail: C-42 → C-43
  cascade (C-42 FAIL because T-40 CONDITION names the deficiency category without quoting a
  deficient T-38 CONDITION form; C-43 cascades per cascade invariant)
- **V-02**: T-40 CONDITION exemplar-only (output format — AMENDMENT TABLE SPECIFICATION
  provides exemplar guidance for T-40 CONDITION but no prescription guidance) — designed fail:
  C-43 only (C-42 PASS — exemplar present; C-43 FAIL — prescription absent)
- **V-03**: T-40 fully documented, Domain 1 P×I-only (phrasing register — T-40 CONDITION
  carries both exemplar and prescription, Domain 1 back-fill uses P×I compound scores only
  without R-NN identifiers) — designed fail: C-41 only (C-42 PASS; C-43 PASS; C-41 FAIL —
  Domain 1 after-state P×I-only fires T-41)
- **V-04**: T-40 minimal + Phase 9 role inversion (lifecycle emphasis + role sequence — T-40
  row in spec lists PHASE only, no CONDITION; Phase 9 Architect leads before PM) — designed
  fail: C-42, C-43, C-46 (three independent fails: cascade pair + role-sequence fail)
- **V-05**: C-23 cascade root (role sequence + cascade propagation — amendment table absent
  from Phase 0; C-23 FAIL → C-26, C-31..C-43) — maximum cascade path including new C-42/C-43

Predicted scores:
- V-01 → 34/36 → **99.44**
- V-02 → 35/36 → **99.72**
- V-03 → 35/36 → **99.72**
- V-04 → 33/36 → **99.17**
- V-05 → 21/36 → **95.83**

---

## V-01 — C-42+C-43 Cascade | Axis: Lifecycle Emphasis (T-40 CONDITION Abstract) | Designed fail: C-42 → C-43

**Hypothesis**: Without explicit CONDITION content guidance in the AMENDMENT TABLE
SPECIFICATION, an LLM will write T-40 CONDITION as a restatement of the trigger text —
"fires if Domain 2 per-column enumeration lacks 'Risk row:' anchor" — naming the deficiency
category without quoting a deficient T-38 CONDITION form. T-42 fires at FINALIZATION (C-42
FAIL). C-43 cascades per cascade invariant (C-42 FAIL → C-43 FAIL). All other 34 A-tier
criteria PASS. T-42 and T-43 in the spec correctly describe what they watch, so the LLM
recognizes the open triggers in Phase 10 Step 1 but cannot retroactively satisfy C-42 by
description alone. Score: 34/36 → **99.44**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-43 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 43)
All other triggers T-01..T-43 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

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
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix — it is the incumbent state that wins by default; active
options must demonstrate sufficient advantage over the inertia competitor to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Structure each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations in canonical bracket form, phases appear in declared sequence. Reference each
option by its Phase 2 label verbatim.

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
    [Option-A] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [Option-B] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [do-nothing] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
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

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
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
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix before the column list)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION omits inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION omits correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-02 — C-43 Isolated | Axis: Output Format (T-40 CONDITION Exemplar-Only) | Designed fail: C-43 only

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides explicit guidance to quote a
deficient T-38 CONDITION form in T-40 CONDITION, an LLM will produce the exemplar (C-42
PASS). Without a parallel instruction to also show a correct-format T-38 CONDITION, the LLM
stops at the exemplar and omits the prescription — T-43 fires (C-43 FAIL). C-42 PASS does
not guarantee C-43 PASS. One A-tier fail. Score: 35/36 → **99.72**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-43 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 43)
All other triggers T-01..T-43 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

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
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix — it is the incumbent state that wins by default; active
options must demonstrate sufficient advantage over the inertia competitor to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Structure each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations in canonical bracket form, phases appear in declared sequence. Reference each
option by its Phase 2 label verbatim.

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
    [Option-A] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [Option-B] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [do-nothing] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
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

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
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
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix; T-40 CONDITION must quote a
                             deficient T-38 CONDITION form — e.g., a T-38 CONDITION that
                             reads "fires if per-site entries lack composite identifier"
                             is abstract-only: it names the category but does not quote
                             a deficient per-site entry, and this abstract form fires T-40)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION omits inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like — see
                             T-40 CONDITION above for the required form)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION omits correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like —
                             exemplar alone is insufficient; C-43 requires the prescription
                             independently)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-03 — C-41 Isolated | Axis: Phrasing Register (T-40 Fully Documented, Domain 1 P×I-Only) | Designed fail: C-41 only

**Hypothesis**: With T-40 CONDITION fully specified in the AMENDMENT TABLE SPECIFICATION
(both inline failure exemplar and correct-format prescription), C-42 and C-43 both PASS.
The designed fail is the classic C-41 isolation: Domain 1 back-fill instructions explicitly
call for P×I compound scores only, omitting R-NN identifiers. T-41 fires (per-site after-state
lacks R-NN+P×I compound pairing). One A-tier fail, verifying C-42/C-43 can coexist with the
prior-round C-41 isolation under v17. Score: 35/36 → **99.72**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-43 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 43)
All other triggers T-01..T-43 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

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
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix — it is the incumbent state that wins by default; active
options must demonstrate sufficient advantage over the inertia competitor to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Structure each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations in canonical bracket form, phases appear in declared sequence. Reference each
option by its Phase 2 label verbatim.

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
    Back-fill P×I compound scores only into Domain 1 RISK fields — do not include R-NN
    identifiers in Domain 1 back-fill entries:
    [Option-A] RISK field: [R-NN pending] → P×I compound score
    [Option-B] RISK field: [R-NN pending] → P×I compound score
    [do-nothing] RISK field: [R-NN pending] → P×I compound score
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

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
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
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix; T-40 CONDITION carries both:
                             (a) inline failure exemplar — "fires if Phase 9b per-site
                                 entries lack composite identifier '[OPTION label] RISK
                                 field:' form" — abstract category only, no quoted
                                 deficient per-site entry shown in T-38 CONDITION
                             (b) correct-format prescription — "a passing T-38 CONDITION
                                 reads: 'fires if [Option-A] RISK field back-fill omits
                                 [Option-A] RISK field: label prefix — e.g., entry reads
                                 [R-NN pending] → P×I without option-label prefix fires T-38'")
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — Domain 1 P×I-only back-fill per Phase 9b instructions above
                             fires T-41; this is the designed single open trigger)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION omits inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like — T-40
                             CONDITION above satisfies C-42)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION omits correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like — T-40
                             CONDITION above satisfies C-43)
T-46 PHASE = FINALIZATION  (fires if Phase 9 Architect output precedes PM output)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-04 — C-42+C-43+C-46 | Combined: Lifecycle Emphasis + Role Sequence | Designed fails: C-42, C-43, C-46

**Axes**: Lifecycle emphasis (T-40 row in spec lists PHASE only — no trigger description, no
CONDITION guidance) + Role sequence (Phase 9 Architect precedes PM — C-46 designed fail).

**Hypothesis**: T-40 listed as `T-40 PHASE = FINALIZATION` with no accompanying text gives
the LLM no signal about T-40 CONDITION content. LLM produces a blank or one-word CONDITION
field. T-42 fires (C-42 FAIL) → T-43 cascades (C-43 FAIL). Separately, Phase 9 instructs
Architect to lead before PM — T-46 fires (C-46 FAIL). Three independent fails: the C-42/C-43
cascade pair and C-46 do not interact. Score: 33/36 → **99.17**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-43 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 43)
All other triggers T-01..T-43 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger conditions.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

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
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix — it is the incumbent state that wins by default; active
options must demonstrate sufficient advantage over the inertia competitor to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Structure each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations in canonical bracket form, phases appear in declared sequence. Reference each
option by its Phase 2 label verbatim.

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
    [Option-A] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [Option-B] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [do-nothing] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each Domain 2 column entry.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

Architect: Confirm technical feasibility of each option and provide a ranked assessment of
implementation risk across all three candidates.

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State explicitly whether the recommendation beats the
inertia competitor and on what basis.

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

Trigger rules T-01..T-43 — exactly 43 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 43)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
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
T-37 PHASE = FINALIZATION  (fires if Phase 9b Domain 2 does not specify R-NN IDs per
                             option column)
T-38 PHASE = FINALIZATION  (fires if Phase 9b per-site entries do not use composite site
                             identifier "[OPTION label] RISK field:" form)
T-39 PHASE = FINALIZATION  (fires if Phase 9b per-site before-state does not carry the
                             [R-NN pending] placeholder literal)
T-40 PHASE = FINALIZATION
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION omits inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION omits correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-46 PHASE = FINALIZATION  (fires if Phase 9 PM output precedes Architect output — Architect
                             must lead Phase 9 before PM provides recommendation)
T-47 PHASE = FINALIZATION  (fires if Domain 2 bracket labels differ from Phase 2 declarations)
T-48 PHASE = FINALIZATION  (fires if Phase 4b absent when do-nothing is inertia competitor)
T-49 PHASE = FINALIZATION  (fires if Phase 4b risk entries omit R-NN identifiers)
T-50 PHASE = FINALIZATION  (fires if Phase 4b entries have R-NN but non-canonical bracket form)
T-51 PHASE = FINALIZATION  (fires if Phase 4b present but Phase 4 used implicit-only framing)
```

---

## V-05 — C-23 Cascade Root | Combined: Role Sequence + Cascade Propagation | Designed fails: C-23, C-26, C-31..C-43

**Axes**: Role sequence (amendment table absent from Phase 0 — the initialization step that
creates the chain from which all downstream criteria depend) + cascade propagation (C-23 FAIL
triggers every amendment-table-dependent criterion, extending the prior-round cascade from 13
fails to 15 by including new C-42 and C-43).

**Hypothesis**: Phase 0 omits amendment table initialization. No T-01..T-43 rows are ever
produced. C-23 fires (amendment table absent). C-26 fires (no Phase 9b section to verify
against the table). C-31..C-43 all fire: every criterion dependent on amendment table
infrastructure fails, including the new C-42 and C-43 which require a T-40 CONDITION
field that never exists. 15 A-tier cascade fails. Score: 21/36 → **95.83**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap, the
forcing function, and what the inertia competitor (do-nothing) would cost the team if it
wins by default.

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
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix — it is the incumbent state that wins by default; active
options must demonstrate sufficient advantage over the inertia competitor to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-48]

PM: Produce a dedicated inertia analysis section upstream of Phase 9b. For each risk that
specifically affects the do-nothing option, cite its R-NN identifier from the Phase 3 risk
register. Structure each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations.

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as the inertia competitor, risk
register has at least 3 entries including one inertia risk, Phase 4b present with R-NN
citations in canonical bracket form, phases appear in declared sequence. Reference each
option by its Phase 2 label verbatim.

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
    [Option-A] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [Option-B] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
    [do-nothing] RISK field: [R-NN pending] → R-NN IDs and P×I compound scores
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

Step 1: Review the document for any criterion shortfalls.
  For each shortfall, produce a finding entry:
    "Finding N: [criterion ID and full name].
     Expected: [what the criterion required].
     Absent/incomplete: [what is missing from this document]."

Step 2: Verify all E-tier criteria (E-01..E-04).
Step 3: Verify all R-tier criteria (R-01..R-03).
Step 4: Confirm coverage table fully populated. Set COMPLETION STATUS.
```
