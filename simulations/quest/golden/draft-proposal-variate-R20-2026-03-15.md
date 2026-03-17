# draft-proposal Variate — Round 20

Rubric version: v20 · Formula: (E/4×60) + (R/3×30) + (A/42×10) · New criteria: C-48
(T-46 CONDITION carries inline exemplar of Part-1-only T-42 CONDITION state — the V-03
R19 class), C-49 (T-47 CONDITION carries inline exemplar of T-42-exemplar-without-
explanation state — the V-02 R19 class)

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

Axes explored:
- **V-01**: T-46 CONDITION abstract (phrasing register — spec gives T-46 a category-only
  description: "fires if T-42 CONDITION lacks correct-format prescription"; no exemplar of
  the Part-1-only T-42 state; LLM mirrors abstract form) — designed fail: C-48 FAIL
  (independent: C-45 PASS, C-46 PASS, C-47 PASS; T-47 golden → C-49 PASS; 1 fail)
- **V-02**: T-47 CONDITION abstract (output format — spec gives T-47 a category-only
  description: "fires if T-42 CONDITION exemplar lacks explanation of abstractness"; no
  exemplar of the exemplar-without-explanation T-42 state; LLM mirrors abstract form) —
  designed fail: C-49 FAIL (independent: C-47 FAIL fires T-47; T-46 golden → C-48 PASS;
  1 fail)
- **V-03**: Both T-46 and T-47 CONDITION abstract (lifecycle emphasis — spec gives both
  T-46 and T-47 category-only descriptions; neither carries an exemplar directive; LLM
  mirrors both as category statements) — designed fail: C-48 FAIL + C-49 FAIL (both
  independent; 2 fails)
- **V-04**: Stale 47-row count + T-47 abstract (role sequence + inertia framing — T-24
  carries v19 count 47 not 49; spec covers T-01..T-47 only; T-47 abstract; T-48 and T-49
  absent) — designed fail: C-24 FAIL (table has 47 rows, rubric requires 49) + C-49 FAIL
  (T-47 CONDITION abstract); 2 fails
- **V-05**: T-42 CONDITION abstract, cascade root (phrasing register + lifecycle emphasis —
  spec gives T-42 a category-only description; no Part 1, no Part 2; LLM mirrors abstract
  form; C-45 FAIL cascades to C-46, C-47, C-48, C-49) — designed fail: C-45 FAIL →
  C-46+C-47+C-48+C-49 cascade; T-40 fully specified (C-42+C-43+C-44 PASS); 5 fails

Predicted scores under v20:
- V-01 → 41/42 → **99.76**
- V-02 → 41/42 → **99.76**
- V-03 → 40/42 → **99.52**
- V-04 → 40/42 → **99.52**
- V-05 → 37/42 → **98.81**

Cascade note: V-03 R19 scored 39/40 (99.75) under v19. Under v20, V-03 R19's C-46 FAIL
(independent, 1 fail) is joined by two new independent fails: C-48 FAIL (T-46 CONDITION
abstract in V-03 R19) and C-49 FAIL (T-47 CONDITION abstract in V-03 R19) → 39/42 →
99.29. The new V-01 here targets C-48 only (T-47 golden, C-49 PASS); the new V-02 targets
C-49 only (T-46 golden, C-48 PASS). R20 establishes V-03 R19's T-46 and T-47 as the live
demonstrations of the C-48 and C-49 independent-fail states.

---

## V-01 — C-48 FAIL (independent) | Axis: Phrasing Register | T-46 CONDITION abstract | Designed fail: C-48 only

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides T-46 CONDITION as a
category-only statement — "fires if T-42 CONDITION lacks correct-format prescription
showing what a passing T-40 CONDITION entry looks like" — with no exemplar of the
Part-1-only T-42 CONDITION state that T-46 fires for, the LLM mirrors that abstract form.
T-46 CONDITION will read as a category label with no inline exemplar. C-48 FAIL fires.
T-47 carries the full golden exemplar of the T-42-exemplar-without-explanation state
(identical to V-03 R19's golden T-46/T-47 pair, but with T-47 upgraded), so C-49 PASS.
C-45 PASS (T-42 carries Part 1 exemplar), C-46 PASS (T-42 carries Part 2 prescription),
C-47 PASS (T-42 Part 1 carries explanation-of-abstractness). All other 41 A-tier criteria
PASS. Score: 41/42 → **99.76**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-49 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 49)
All other triggers T-01..T-49 have PHASE = FINALIZATION.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
                             Part 1 — Failure exemplar with explanation: A deficient T-40
                             CONDITION entry reads: 'fires if Phase 9b Domain 2 per-column
                             enumeration lacks "Risk row:" anchor prefix before the column
                             list' — this is abstract because it names the Domain 2 format
                             requirement as a category without quoting or paraphrasing any
                             T-38 CONDITION entry that omits the required identifier; a
                             reviewer assessing T-38 cannot determine what a deficient T-38
                             CONDITION entry looks like from this category description alone.
                             Part 2 — Correct-format prescription: A passing T-40 CONDITION
                             entry must include a quoted or paraphrased deficient T-38 form
                             with explanation of its abstractness, e.g., 'T-38 CONDITION:
                             "fires if Phase 9b per-site entries do not use composite site
                             identifier form" — abstract because it names the required
                             identifier format without quoting a T-38 entry that omits it;
                             correct: quote the specific abstract T-38 CONDITION form'.)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form — exemplar must quote or
                             paraphrase an abstract-only T-40 CONDITION entry, e.g.,
                             'fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix' — this is abstract because it
                             names the Domain 2 format requirement without quoting a
                             deficient T-38 form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like —
                             Part 2: a quoted or paraphrased exemplar of an abstract-only
                             T-38 CONDITION form that would fire T-40, demonstrating the
                             minimum content a passing T-40 CONDITION must carry)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract — Part 1
                             must include both the quoted T-40 form AND an explanation of
                             what property makes it abstract.
                             Inline exemplar of the exemplar-without-explanation T-42
                             CONDITION state that fires T-47: 'fires if T-40 CONDITION lacks
                             inline failure exemplar — example of deficient T-40: "fires if
                             Phase 9b Domain 2 per-column enumeration lacks Risk row:
                             prefix"' — this T-42 CONDITION has a quoted deficient T-40 form
                             (C-45 PASS) but no explanation of why that T-40 form is abstract;
                             no language stating it names the Domain 2 format requirement
                             without showing what a deficient T-38 CONDITION looks like.)
T-48 PHASE = FINALIZATION  (fires if T-46 CONDITION lacks inline exemplar of the
                             Part-1-only T-42 CONDITION state that T-46 fires for — a T-46
                             CONDITION that states only "fires if T-42 CONDITION lacks
                             correct-format prescription showing what a passing T-40
                             CONDITION entry looks like" names the trigger condition without
                             exemplifying the specific Part-1-present-Part-2-absent T-42
                             state; T-46 CONDITION must quote or closely paraphrase a T-42
                             CONDITION with Part 1 labeled and present but no Part 2 label
                             and no Part 2 content)
T-49 PHASE = FINALIZATION  (fires if T-47 CONDITION lacks inline exemplar of the
                             T-42-exemplar-without-explanation state that T-47 fires for —
                             a T-47 CONDITION that states only "fires if T-42 CONDITION
                             exemplar lacks explanation of why the quoted T-40 form is
                             abstract" names the trigger condition without exemplifying
                             the specific exemplar-present-explanation-absent T-42 state;
                             T-47 CONDITION must quote or closely paraphrase a T-42
                             CONDITION that has a quoted deficient T-40 form but no
                             explanation of why that T-40 form is abstract)
```

---

## V-02 — C-49 FAIL (independent) | Axis: Output Format | T-47 CONDITION abstract | Designed fail: C-49 only

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides T-47 CONDITION as a
category-only statement — "fires if T-42 CONDITION exemplar lacks explanation of why the
quoted deficient T-40 CONDITION form is abstract" — with no exemplar of the exemplar-
without-explanation T-42 state that T-47 fires for, the LLM mirrors that abstract form.
T-47 CONDITION will read as a category label with no inline exemplar. C-49 FAIL fires.
T-46 carries the full golden exemplar of the Part-1-only T-42 CONDITION state, so C-48
PASS. C-45 PASS (T-42 carries Part 1 exemplar), C-46 PASS (T-42 Part 2 present), C-47
PASS (T-42 Part 1 carries explanation-of-abstractness). All other 41 A-tier criteria
PASS. Score: 41/42 → **99.76**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-49 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 49)
All other triggers T-01..T-49 have PHASE = FINALIZATION.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
                             Part 1 — Failure exemplar with explanation: A deficient T-40
                             CONDITION entry reads: 'fires if Phase 9b Domain 2 per-column
                             enumeration lacks "Risk row:" anchor prefix before the column
                             list' — this is abstract because it names the Domain 2 format
                             requirement as a category without quoting or paraphrasing any
                             T-38 CONDITION entry that omits the required identifier; a
                             reviewer assessing T-38 cannot determine what a deficient T-38
                             CONDITION entry looks like from this category description alone.
                             Part 2 — Correct-format prescription: A passing T-40 CONDITION
                             entry must include a quoted or paraphrased deficient T-38 form
                             with explanation of its abstractness, e.g., 'T-38 CONDITION:
                             "fires if Phase 9b per-site entries do not use composite site
                             identifier form" — abstract because it names the required
                             identifier format without quoting a T-38 entry that omits it;
                             correct: quote the specific abstract T-38 CONDITION form'.)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form — exemplar must quote or
                             paraphrase an abstract-only T-40 CONDITION entry, e.g.,
                             'fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix' — this is abstract because it
                             names the Domain 2 format requirement without quoting a
                             deficient T-38 form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like.
                             Inline exemplar of the Part-1-only T-42 CONDITION state that
                             fires T-46: 'Part 1 — Failure exemplar with explanation: A
                             deficient T-40 CONDITION entry reads: "fires if Phase 9b Domain
                             2 per-column enumeration lacks Risk row: anchor prefix" —
                             abstract because it names the Domain 2 format requirement
                             without quoting a deficient T-38 form.' [END — no Part 2 label
                             and no Part 2 content present] — T-42 CONDITION with Part 1
                             labeled and fully present but no Part 2 label and no correct-
                             format prescription fires T-46.)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract — Part 1
                             must include both the quoted T-40 form AND an explanation of
                             what property makes it abstract: i.e., that it names the
                             deficiency category without quoting a T-38 form)
T-48 PHASE = FINALIZATION  (fires if T-46 CONDITION lacks inline exemplar of the
                             Part-1-only T-42 CONDITION state that T-46 fires for — a T-46
                             CONDITION that states only "fires if T-42 CONDITION lacks
                             correct-format prescription showing what a passing T-40
                             CONDITION entry looks like" names the trigger condition without
                             exemplifying the specific Part-1-present-Part-2-absent T-42
                             state; T-46 CONDITION must quote or closely paraphrase a T-42
                             CONDITION with Part 1 labeled and present but no Part 2 label
                             and no Part 2 content)
T-49 PHASE = FINALIZATION  (fires if T-47 CONDITION lacks inline exemplar of the
                             T-42-exemplar-without-explanation state that T-47 fires for —
                             a T-47 CONDITION that states only "fires if T-42 CONDITION
                             exemplar lacks explanation of why the quoted T-40 form is
                             abstract" names the trigger condition without exemplifying
                             the specific exemplar-present-explanation-absent T-42 state;
                             T-47 CONDITION must quote or closely paraphrase a T-42
                             CONDITION that has a quoted deficient T-40 form but no
                             explanation of why that T-40 form is abstract)
```

---

## V-03 — C-48+C-49 FAIL | Axis: Lifecycle Emphasis | Both T-46 and T-47 CONDITION abstract | Designed fail: C-48 + C-49 (both independent)

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides both T-46 and T-47
CONDITION as category-only statements — T-46: "fires if T-42 CONDITION lacks correct-format
prescription"; T-47: "fires if T-42 CONDITION exemplar lacks explanation of abstractness" —
with no inline exemplar directives in either row, the LLM mirrors both forms abstractly.
T-46 CONDITION and T-47 CONDITION each read as category labels. C-48 FAIL and C-49 FAIL
both fire independently. T-42 is fully specified (Part 1 + explanation + Part 2), so C-45
PASS, C-46 PASS, C-47 PASS. C-48 and C-49 are mutually independent fails: neither cascades
from the other. This is the R20 proof that the C-48/C-49 independent-fail states exist and
are distinguishable from each other and from the C-46/C-47 chain. Score: 40/42 → **99.52**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-49 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 49)
All other triggers T-01..T-49 have PHASE = FINALIZATION.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
                             Part 1 — Failure exemplar with explanation: A deficient T-40
                             CONDITION entry reads: 'fires if Phase 9b Domain 2 per-column
                             enumeration lacks "Risk row:" anchor prefix before the column
                             list' — this is abstract because it names the Domain 2 format
                             requirement as a category without quoting or paraphrasing any
                             T-38 CONDITION entry that omits the required identifier; a
                             reviewer assessing T-38 cannot determine what a deficient T-38
                             CONDITION entry looks like from this category description alone.
                             Part 2 — Correct-format prescription: A passing T-40 CONDITION
                             entry must include a quoted or paraphrased deficient T-38 form
                             with explanation of its abstractness, e.g., 'T-38 CONDITION:
                             "fires if Phase 9b per-site entries do not use composite site
                             identifier form" — abstract because it names the required
                             identifier format without quoting a T-38 entry that omits it;
                             correct: quote the specific abstract T-38 CONDITION form'.)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form — exemplar must quote or
                             paraphrase an abstract-only T-40 CONDITION entry, e.g.,
                             'fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix' — this is abstract because it
                             names the Domain 2 format requirement without quoting a
                             deficient T-38 form)
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
T-48 PHASE = FINALIZATION  (fires if T-46 CONDITION lacks inline exemplar of the
                             Part-1-only T-42 CONDITION state that T-46 fires for — a T-46
                             CONDITION that states only "fires if T-42 CONDITION lacks
                             correct-format prescription showing what a passing T-40
                             CONDITION entry looks like" names the trigger condition without
                             exemplifying the specific Part-1-present-Part-2-absent T-42
                             state; T-46 CONDITION must quote or closely paraphrase a T-42
                             CONDITION with Part 1 labeled and present but no Part 2 label
                             and no Part 2 content)
T-49 PHASE = FINALIZATION  (fires if T-47 CONDITION lacks inline exemplar of the
                             T-42-exemplar-without-explanation state that T-47 fires for —
                             a T-47 CONDITION that states only "fires if T-42 CONDITION
                             exemplar lacks explanation of why the quoted T-40 form is
                             abstract" names the trigger condition without exemplifying
                             the specific exemplar-present-explanation-absent T-42 state;
                             T-47 CONDITION must quote or closely paraphrase a T-42
                             CONDITION that has a quoted deficient T-40 form but no
                             explanation of why that T-40 form is abstract)
```

---

## V-04 — C-24+C-49 FAIL | Combination: Role Sequence + Stale Count | 47-row table (v19) + T-47 abstract | Designed fail: C-24 + C-49

**Hypothesis**: When the spec carries a stale v19-era row count declaration ("T-01..T-47 —
exactly 47 rows") with T-24 checking 47, the LLM generates a 47-row amendment table.
C-24 fires at PRE-DOCUMENT: rubric requires 49 rows, table has 47 (T-48 and T-49 absent).
T-47 CONDITION is additionally abstract in the spec (category-only: "fires if T-42 CONDITION
exemplar lacks explanation of abstractness"), so C-49 FAIL fires independently — the T-47
abstract form is mirrored regardless of the row-count failure. T-46 carries the golden
exemplar directive for the Part-1-only T-42 state. C-48 evaluates independently against
T-46's CONDITION cell: since T-46 is golden, C-48 PASS. C-45 PASS (T-42 carries Part 1),
C-46 PASS (T-42 Part 2 present), C-47 PASS (explanation-of-abstractness present in Part 1).
C-24 FAIL + C-49 FAIL = 2 fails. Score: 40/42 → **99.52**.

Note: C-24 FAIL (stale 47-row count) and C-49 FAIL (T-47 abstract) are independent: the
stale count prevents T-48 and T-49 rows from existing, but C-49 fires for T-47's CONDITION
content independently, and C-48 is about T-46's CONDITION content (T-46 exists in the
47-row table and carries golden content → C-48 PASS independent of row count).

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
                             Part 1 — Failure exemplar with explanation: A deficient T-40
                             CONDITION entry reads: 'fires if Phase 9b Domain 2 per-column
                             enumeration lacks "Risk row:" anchor prefix before the column
                             list' — this is abstract because it names the Domain 2 format
                             requirement as a category without quoting or paraphrasing any
                             T-38 CONDITION entry that omits the required identifier; a
                             reviewer assessing T-38 cannot determine what a deficient T-38
                             CONDITION entry looks like from this category description alone.
                             Part 2 — Correct-format prescription: A passing T-40 CONDITION
                             entry must include a quoted or paraphrased deficient T-38 form
                             with explanation of its abstractness, e.g., 'T-38 CONDITION:
                             "fires if Phase 9b per-site entries do not use composite site
                             identifier form" — abstract because it names the required
                             identifier format without quoting a T-38 entry that omits it;
                             correct: quote the specific abstract T-38 CONDITION form'.)
T-43 PHASE = FINALIZATION  (fires if T-40 CONDITION lacks correct-format prescription
                             showing what a passing T-38 CONDITION entry looks like)
T-44 PHASE = FINALIZATION  (fires if T-40 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-38 form is abstract)
T-45 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks inline failure exemplar of
                             a deficient T-40 CONDITION form — exemplar must quote or
                             paraphrase an abstract-only T-40 CONDITION entry, e.g.,
                             'fires if Phase 9b Domain 2 per-column enumeration lacks
                             "Risk row:" anchor prefix' — this is abstract because it
                             names the Domain 2 format requirement without quoting a
                             deficient T-38 form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like.
                             Inline exemplar of the Part-1-only T-42 CONDITION state that
                             fires T-46: 'Part 1 — Failure exemplar with explanation: A
                             deficient T-40 CONDITION entry reads: "fires if Phase 9b Domain
                             2 per-column enumeration lacks Risk row: anchor prefix" —
                             abstract because it names the Domain 2 format requirement
                             without quoting a deficient T-38 form.' [END — no Part 2 label
                             and no Part 2 content present] — T-42 CONDITION with Part 1
                             labeled and fully present but no Part 2 label and no correct-
                             format prescription fires T-46.)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract — Part 1
                             must include both the quoted T-40 form AND an explanation of
                             what property makes it abstract: i.e., that it names the
                             deficiency category without quoting a T-38 form)
```

---

## V-05 — C-45+C-46+C-47+C-48+C-49 cascade | Combination: Phrasing Register + Lifecycle Emphasis | T-42 CONDITION abstract | Designed fail: C-45 cascade root → C-46+C-47+C-48+C-49

**Hypothesis**: When the AMENDMENT TABLE SPECIFICATION provides T-42 CONDITION as a
category-only statement — "fires if T-40 CONDITION lacks inline failure exemplar showing
what an abstract-only T-38 CONDITION entry looks like" — with no Part 1 exemplar, no
explanation-of-abstractness directive, and no Part 2 prescription directive, the LLM
mirrors that abstract form. T-42 CONDITION will read as a category label with no exemplar.
C-45 FAIL fires. C-45 FAIL cascades deterministically to C-46 FAIL (no exemplar → no
prescription target), C-47 FAIL (no exemplar → no explanation-of-abstractness target),
C-48 FAIL (C-45 FAIL → the Part-1-present-Part-2-absent T-42 state required for T-46's
exemplar cannot be constructed from a fully abstract T-42), and C-49 FAIL (C-45 FAIL →
the exemplar-present-explanation-absent T-42 state required for T-47's exemplar cannot be
constructed from a fully abstract T-42). T-40 is fully specified (Part 1 + explanation +
Part 2), so C-42 PASS, C-43 PASS, C-44 PASS. All other 37 A-tier criteria PASS. T-46 and
T-47 CONDITION cells are also abstract (no exemplar directives provided for either), which
is consistent with the cascade: even if T-46 carried a golden directive, C-48 FAIL would
cascade from C-45 regardless — the cascade fires from T-42's abstractness, not T-46's.
5 fails total. Score: 37/42 → **98.81**.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the "inertia competitor" — the implicit default that will win if no action is taken.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-49 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 49)
All other triggers T-01..T-49 have PHASE = FINALIZATION.
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
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-49.
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

Trigger rules T-01..T-49 — exactly 49 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 49)
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
                             showing what a passing T-40 CONDITION entry looks like)
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted deficient T-40 CONDITION form is abstract)
T-48 PHASE = FINALIZATION  (fires if T-46 CONDITION lacks inline exemplar of the
                             Part-1-only T-42 CONDITION state that T-46 fires for)
T-49 PHASE = FINALIZATION  (fires if T-47 CONDITION lacks inline exemplar of the
                             T-42-exemplar-without-explanation state that T-47 fires for)
```
