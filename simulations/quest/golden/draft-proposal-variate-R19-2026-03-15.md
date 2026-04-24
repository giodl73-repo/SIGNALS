# draft-proposal Variate — Round 19

Rubric version: v19 · Formula: (E/4×60) + (R/3×30) + (A/40×10) · New criteria: C-46
(T-42 CONDITION includes correct-format prescription — Part 2 showing what a passing
T-40 CONDITION entry looks like), C-47 (T-42 CONDITION exemplar includes explanation of
why the quoted deficient T-40 CONDITION form is abstract — Part 1 triple-layer standard)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: T-42 CONDITION abstract (lifecycle emphasis — AMENDMENT TABLE SPECIFICATION
  gives T-42 a category-only description; no exemplar, no explanation, no prescription;
  LLM mirrors abstract form) — designed fail: C-45 FAIL → C-46 FAIL + C-47 FAIL (cascade
  from no exemplar; 3 fails)
- **V-02**: T-42 CONDITION exemplar-only (output format — spec directs "quote the
  deficient T-40 form" but provides no explanation-of-abstractness directive and no
  prescription directive; LLM quotes exemplar and stops) — designed fail: C-47 FAIL
  (independent: exemplar present, explanation absent) + C-46 FAIL (independent: prescription
  absent); C-45 PASS; 2 fails
- **V-03**: T-42 CONDITION Part 1 explicit+labeled, Part 2 absent (phrasing register —
  spec carries an explicit "Part 1 — Failure exemplar with explanation" label with full
  content but no "Part 2" label; LLM reproduces Part 1 faithfully and stops) — designed
  fail: C-46 FAIL only (independent; C-45 PASS, C-47 PASS; 1 fail)
- **V-04**: Stale row count (45 not 47) + T-42 exemplar-only (output format + role
  sequence — v18-era T-24 check carried forward without increment; T-42 gets exemplar
  direction only) — designed fail: C-24 FAIL (43 rows present, T-24 checks 45 → wait,
  the table has 47 rows but T-24 says 45, so T-24 fires) + C-47 FAIL + C-46 FAIL; 3 fails
- **V-05**: C-23 cascade root + T-42 abstract (inertia framing + lifecycle emphasis —
  Phase 2 RISK template instructs inline P×I computation instead of [R-NN pending];
  T-42 CONDITION abstract) — designed fail: C-23 FAIL → C-26+C-31..C-43 cascade;
  C-42 FAIL → C-44 cascade; C-45 FAIL → C-46+C-47 cascade; 19 total fails

Predicted scores:
- V-01 → 37/40 → **99.25**
- V-02 → 38/40 → **99.50**
- V-03 → 39/40 → **99.75**
- V-04 → 37/40 → **99.25**
- V-05 → 21/40 → **95.25**

Cascade note: V-03 from R18 scored 37/38 (99.74) under v18. Under v19, V-03 R18's
C-45 FAIL cascades to C-46 FAIL + C-47 FAIL → 37/40 → 99.25. The new V-03 here is
designed to pass C-45 and C-47, failing C-46 only → 39/40 → 99.75.

---

## V-01 — C-45+C-46+C-47 Cascade | Axis: Lifecycle Emphasis (T-42 CONDITION Abstract) | Designed fail: C-45 → C-46+C-47 cascade

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides an abstract CONDITION
description for T-42 — naming the deficiency category without quoting any exemplar of a
deficient T-40 CONDITION form — the LLM mirrors that abstract form in its output. T-42
CONDITION will read "fires if T-40 CONDITION lacks inline failure exemplar showing what an
abstract-only T-38 CONDITION entry looks like" — a category statement with no quoted T-40
form. C-45 FAIL fires. C-46 FAIL and C-47 FAIL cascade deterministically from C-45 FAIL
(no exemplar → no prescription possible; no exemplar → no explanation-of-abstractness
possible). T-40 CONDITION is fully specified with triple-layer content (exemplar +
explanation + prescription), so C-42, C-43, C-44 PASS. All other 37 A-tier criteria PASS.
Score: 37/40 → **99.25**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 47)
All other triggers T-01..T-47 have PHASE = FINALIZATION.
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

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

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

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending]
placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

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
                             "Risk row:" anchor prefix before the column list.
                             Part 1 — Failure exemplar with explanation: A deficient T-38
                             CONDITION entry reads: 'fires if Phase 9b per-site entries
                             do not use composite site identifier "[OPTION label] RISK
                             field:" form' — this is abstract because it names the required
                             format category without quoting any T-38 CONDITION entry that
                             omits the composite identifier; the reader cannot verify what
                             the deficient form looks like without constructing it from
                             the description alone.
                             Part 2 — Correct-format prescription: A passing T-38
                             CONDITION entry must show an inline quoted example of an
                             abstract-only form, such as 'fires if Phase 9b per-site
                             entries omit option-label prefix' — sufficient to show what
                             a deficient T-38 CONDITION entry actually looks like, making
                             the deficiency concrete and independently verifiable.)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like —
                             Part 2: a quoted or paraphrased exemplar of an abstract-only
                             T-38 CONDITION form that would fire T-40, demonstrating the
                             minimum content a passing T-40 CONDITION must carry)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract — Part 1
                             must include both the quoted T-40 form AND an explanation of
                             what property makes it abstract: i.e., that it names the
                             deficiency category without quoting a T-38 form)
```

---

## V-02 — C-47+C-46 Independent | Axis: Output Format (T-42 Exemplar-Only, No Explanation, No Prescription) | Designed fail: C-47 (independent), C-46 (independent)

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides a "quote the deficient
T-40 form" directive for T-42 CONDITION but no "explain why it is abstract" directive and
no "show correct-format" directive, the LLM quotes the deficient T-40 form (C-45 PASS) and
stops. T-42 CONDITION reads: "fires if T-40 CONDITION lacks inline failure exemplar —
example: 'fires if Phase 9b Domain 2 per-column enumeration lacks Risk row: anchor prefix
before the column list'" — the exemplar is present, but no explanation of why that T-40
form is abstract appears alongside it. C-47 FAIL (independent: C-45 PASS does not
guarantee C-47 PASS). Without a prescription directive, T-42 CONDITION also lacks the
correct-format guidance — C-46 FAIL (independent). Two independent fails, no cascade.
T-40 CONDITION is fully specified (triple-layer), so C-42, C-43, C-44 PASS. Score:
38/40 → **99.50**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 47)
All other triggers T-01..T-47 have PHASE = FINALIZATION.
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

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

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

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending]
placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

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
                             "Risk row:" anchor prefix before the column list.
                             Part 1 — Failure exemplar with explanation: A deficient T-38
                             CONDITION entry reads: 'fires if Phase 9b per-site entries
                             do not use composite site identifier "[OPTION label] RISK
                             field:" form' — this is abstract because it names the required
                             format category without quoting any T-38 CONDITION entry that
                             omits the composite identifier; the reader cannot verify what
                             the deficient form looks like without constructing it from
                             the description alone.
                             Part 2 — Correct-format prescription: A passing T-38
                             CONDITION entry must show an inline quoted example of an
                             abstract-only form, such as 'fires if Phase 9b per-site
                             entries omit option-label prefix' — sufficient to show what
                             a deficient T-38 CONDITION entry actually looks like, making
                             the deficiency concrete and independently verifiable.)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like.
                             CONDITION must quote a deficient T-40 CONDITION form verbatim
                             — example: "fires if Phase 9b Domain 2 per-column enumeration
                             lacks 'Risk row:' anchor prefix before the column list")
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like —
                             Part 2: a quoted or paraphrased exemplar of an abstract-only
                             T-38 CONDITION form that would fire T-40, demonstrating the
                             minimum content a passing T-40 CONDITION must carry)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract — Part 1
                             must include both the quoted T-40 form AND an explanation of
                             what property makes it abstract: i.e., that it names the
                             deficiency category without quoting a T-38 form)
```

---

## V-03 — C-46 Independent | Axis: Phrasing Register (T-42 Part 1 Explicit+Labeled, Part 2 Absent) | Designed fail: C-46 only

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides T-42 CONDITION with an
explicit "Part 1 — Failure exemplar with explanation" label — giving both the quoted
deficient T-40 form and an explanation of why that form is abstract — but provides no
"Part 2" label and no prescription content, the LLM reproduces Part 1 faithfully (C-45
PASS: exemplar present; C-47 PASS: explanation-of-abstractness present) but generates no
Part 2 content because the spec carries no Part 2 label or directive. C-46 FAIL is the
only failure: the LLM mirrors the spec's register — explicit labeled parts reproduce
labeled parts; absent Part 2 label produces absent Part 2 output. C-46 is independently
testable (C-45 PASS and C-47 PASS do not guarantee C-46 PASS). Score: 39/40 → **99.75**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 47)
All other triggers T-01..T-47 have PHASE = FINALIZATION.
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

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

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

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending]
placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

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
                             "Risk row:" anchor prefix before the column list.
                             Part 1 — Failure exemplar with explanation: A deficient T-38
                             CONDITION entry reads: 'fires if Phase 9b per-site entries
                             do not use composite site identifier "[OPTION label] RISK
                             field:" form' — this is abstract because it names the required
                             format category without quoting any T-38 CONDITION entry that
                             omits the composite identifier; the reader cannot verify what
                             the deficient form looks like without constructing it from
                             the description alone.
                             Part 2 — Correct-format prescription: A passing T-38
                             CONDITION entry must show an inline quoted example of an
                             abstract-only form, such as 'fires if Phase 9b per-site
                             entries omit option-label prefix' — sufficient to show what
                             a deficient T-38 CONDITION entry actually looks like, making
                             the deficiency concrete and independently verifiable.)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like.
                             Part 1 — Failure exemplar with explanation: Quote the deficient
                             T-40 CONDITION form verbatim, then explain why it is abstract
                             — e.g., 'fires if Phase 9b Domain 2 per-column enumeration
                             lacks "Risk row:" anchor prefix before the column list' names
                             the deficiency as a missing prefix category but carries no
                             quoted T-38 CONDITION form showing how the abstract-only form
                             appears; it is abstract because it states what is required
                             without showing a concrete example of the deficient T-38 text,
                             leaving the reader to construct the deficient form mentally)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like —
                             Part 2: a quoted or paraphrased exemplar of an abstract-only
                             T-38 CONDITION form that would fire T-40, demonstrating the
                             minimum content a passing T-40 CONDITION must carry)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract — Part 1
                             must include both the quoted T-40 form AND an explanation of
                             what property makes it abstract: i.e., that it names the
                             deficiency category without quoting a T-38 form)
```

---

## V-04 — C-24+C-47+C-46 | Axis: Output Format + Role Sequence (Stale Row Count + T-42 Exemplar-Only) | Designed fail: C-24, C-47 (independent), C-46 (independent)

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION carries a stale row-count check
(T-24 fires if "!= 45" rather than "!= 47") and provides exemplar-only direction for T-42
CONDITION — quoting the deficient T-40 form but supplying no explanation-of-abstractness
and no prescription directive — C-24 fires (the output table has 47 rows because the spec
instructs T-01..T-47, but T-24 checks for 45, so T-24 fires immediately at PRE-DOCUMENT
phase); C-47 fires (exemplar present in T-42, explanation absent); C-46 fires (prescription
absent in T-42). Three independent fails across two independently triggered paths: C-24
fires from stale count comparison, C-47 and C-46 fire from absent T-42 content directives.
Score: 37/40 → **99.25**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 45)
All other triggers T-01..T-47 have PHASE = FINALIZATION.
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

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

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

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending]
placeholders.

Enumerate citation sites by structural domain:
  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [Option-B] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
    [do-nothing] RISK field: [R-NN pending] → [R-NN IDs (P:N × I:N = P×I), ...]
  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

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
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 45)
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
                             "Risk row:" anchor prefix before the column list.
                             Part 1 — Failure exemplar with explanation: A deficient T-38
                             CONDITION entry reads: 'fires if Phase 9b per-site entries
                             do not use composite site identifier "[OPTION label] RISK
                             field:" form' — this is abstract because it names the required
                             format category without quoting any T-38 CONDITION entry that
                             omits the composite identifier; the reader cannot verify what
                             the deficient form looks like without constructing it from
                             the description alone.
                             Part 2 — Correct-format prescription: A passing T-38
                             CONDITION entry must show an inline quoted example of an
                             abstract-only form, such as 'fires if Phase 9b per-site
                             entries omit option-label prefix' — sufficient to show what
                             a deficient T-38 CONDITION entry actually looks like, making
                             the deficiency concrete and independently verifiable.)
T-41 PHASE = FINALIZATION  (fires if Phase 9b per-site after-state does not pair R-NN
                             entries and P×I scores together in a single compound expression
                             — P×I-only or R-NN-only after-state fires T-41)
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like.
                             CONDITION must quote a deficient T-40 CONDITION form verbatim
                             — example: "fires if Phase 9b Domain 2 per-column enumeration
                             lacks 'Risk row:' anchor prefix before the column list")
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like —
                             Part 2: a quoted or paraphrased exemplar of an abstract-only
                             T-38 CONDITION form that would fire T-40, demonstrating the
                             minimum content a passing T-40 CONDITION must carry)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract — Part 1
                             must include both the quoted T-40 form AND an explanation of
                             what property makes it abstract: i.e., that it names the
                             deficiency category without quoting a T-38 form)
```

---

## V-05 — C-23 Cascade Root + C-45+C-46+C-47 | Axis: Inertia Framing + Lifecycle Emphasis | Designed fail: C-23 cascade (19 fails total)

**Hypothesis**: When the Phase 2 RISK template instructs inline P×I computation (removing
the [R-NN pending] placeholder directive) and T-42 CONDITION is abstract (category-only,
no exemplar content guidance), C-23 FAIL fires the maximum cascade path under v19. C-23
FAIL (RISK fields have inline P×I without R-NN linkage from Phase 3) → C-26 FAIL (no
Phase 9b propagation phase present, because no placeholders need backfilling) → C-31
through C-43 FAIL (13 Phase 9b structural criteria all fail: no Phase 9b phase means no
domain enumeration, no per-site entries, no transition notation, no after-state, no
compound expressions, no Risk row: anchor). C-42 FAIL (from cascade) → C-44 FAIL
(cascade: no exemplar means no explanation possible). T-42 CONDITION abstract → C-45 FAIL
(no exemplar) → C-46 FAIL + C-47 FAIL (both cascade from C-45). Count: C-23 (1) + C-26
(1) + C-31..C-43 (13) + C-44 (1) + C-45 (1) + C-46 (1) + C-47 (1) = 19 fails →
21/40 → **95.25**.

Note: the do-nothing option is less prominently featured in Phase 2 (no [R-NN pending]
placeholder means no explicit inertia risk reservation), compounding the inertia framing
axis: the inertia competitor's risk column in Phase 2 carries a premature P×I score rather
than a reserved slot, undermining the inertia analysis chain from Phase 2 → Phase 4b.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-47 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 47)
All other triggers T-01..T-47 have PHASE = FINALIZATION.
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
  RISK: Compute the P×I score for this option's primary risk now. PM notes adoption risk
        with P and I values. Architect notes technical risk with P and I values.
        Example: "Adoption friction if workflow changes required (PM, P:2 × I:3 = 6);
        integration complexity with existing pipeline (Architect, P:3 × I:4 = 12)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness. Confirm the do-nothing option
carries plausible technical rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build a risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Define project-specific scoring anchors before any entry: what P=1, P=3, P=5 mean for
this project's probability scale; what I=1, I=3, I=5 mean for this project's impact scale.

Enumerate at least 3 technical risk entries (R-01, R-02, R-03...). Include at least one
risk that applies ONLY to the do-nothing option (inertia risk: technical debt accumulation,
opportunity cost, competitive erosion). Assign P and I scores on the defined scale. Compute
P×I. PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix — it is the incumbent state that wins by default; active
options must demonstrate sufficient advantage over the inertia competitor to justify action.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (P×I cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, Phase 4b present with R-NN citations in
canonical bracket form, assumption register has at least 2 A-NN entries, phases appear in
declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-47.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 8 — ASSUMPTION REGISTER [GATE: C-08]

PM: Build an assumption register with at least 2 A-NN entries. Columns:
  A-NN | ASSUMPTION | VALIDATION PLAN

Entries must be distinct from risk register entries.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide explicit rationale referencing at least two
comparison matrix dimensions. State qualifying conditions: at least 2 specific circumstances
under which the recommendation would change. State explicitly whether the recommendation
beats the inertia competitor and on what basis.

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
T-42 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks inline failure exemplar showing
                             what an abstract-only T-38 CONDITION entry looks like)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract)
```

---

## Variation Diff Summary

| Section | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Phase 2 RISK template | [R-NN pending] | [R-NN pending] | [R-NN pending] | [R-NN pending] | Inline P×I (C-23 cascade) |
| Phase 9b present | YES | YES | YES | YES | ABSENT (no placeholder to backfill) |
| T-24 check value | 47 | 47 | 47 | **45** (stale) | 47 |
| T-40 CONDITION | Triple-layer (exemplar+explain+prescribe) | Triple-layer | Triple-layer | Triple-layer | Abstract only |
| T-42 CONDITION | Abstract only | Exemplar-only | Part 1 (exemplar+explanation), no Part 2 | Exemplar-only | Abstract only |
| T-46/T-47 CONDITION | Fully specified | Fully specified | Fully specified | Fully specified | Abstract only |
| Coverage table range | C-01..C-47 | C-01..C-47 | C-01..C-47 | C-01..C-47 | C-01..C-47 |
| Designed fails | C-45, C-46, C-47 | C-47, C-46 | C-46 | C-24, C-47, C-46 | C-23+cascade (19) |
| Fails count | 3 | 2 | 1 | 3 | 19 |
| A-tier score | 37/40 | 38/40 | 39/40 | 37/40 | 21/40 |
| Composite | **99.25** | **99.50** | **99.75** | **99.25** | **95.25** |

## Cascade Paths Under v19

**C-45 → C-46 + C-47**: Both cascade from C-45 FAIL (no exemplar means no
prescription is possible and no explanation-of-abstractness is possible). C-46 and
C-47 are mutually independent: C-46 PASS does not guarantee C-47 PASS and vice versa.
V-01 and V-04 and V-05 all reach C-45 FAIL and therefore trigger both cascades.

**C-42 → C-43 + C-44**: Both cascade from C-42 FAIL (T-38 abstract means no T-38
exemplar to cite in T-40 means no explanation of T-38 abstractness). V-05 reaches
C-42 FAIL via the C-23 cascade.

**C-23 → C-26 + C-31..C-43**: The maximum cascade path. V-05 is the only variation
designed to trigger this path. Inline P×I in Phase 2 → no placeholder → no Phase 9b
phase → no domain enumeration → 13 Phase 9b structural criteria fail deterministically.

## Discriminator Isolation Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | What it isolates |
|-----------|------|------|------|------|------|-----------------|
| C-45 | FAIL | PASS | PASS | PASS | FAIL | Exemplar present in T-42 CONDITION |
| C-46 | FAIL* | FAIL | FAIL | FAIL | FAIL* | Part 2 prescription present in T-42 |
| C-47 | FAIL* | FAIL | PASS | FAIL | FAIL* | Explanation-of-abstractness in T-42 |
| C-24 | PASS | PASS | PASS | FAIL | PASS | Amendment table row count = 47 |
| C-23 | PASS | PASS | PASS | PASS | FAIL | No inline P×I in Phase 2 RISK |

*cascade from C-45 FAIL

V-02 vs V-03: isolates C-47 (V-02 fails C-47; V-03 passes C-47 by supplying
  explanation-of-abstractness directive in Part 1).
V-03 vs V-01: isolates C-45 (V-03 has exemplar+explanation in spec; V-01 is abstract).
V-04 vs V-02: isolates C-24 (V-04 has stale T-24 check; V-02 does not).
V-05 vs V-01: isolates C-23 cascade (V-05 forces C-23 FAIL via P×I in Phase 2).
