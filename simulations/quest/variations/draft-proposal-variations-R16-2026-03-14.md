The existing variate R16 file belongs to a later rubric epoch (C-42/C-43, /36 denominator — that's a different run). The current task targets rubric v16 (C-40/C-41, /34 denominator). I'll output the variations as Markdown per the task instruction.

---

# draft-proposal Variate — Round 16

**Rubric**: v16 · **Formula**: `(E/4×60) + (R/3×30) + (A/34×10)` · **New criteria**: C-40 (T-38 CONDITION must carry inline exemplar of abstract-only T-37 CONDITION form) and C-41 (T-38 CONDITION must additionally carry correct-format prescription showing what a passing T-37 CONDITION looks like). Amendment table row count: **41**. Denominator: **/34**.

Single-axis variations first (V-01..V-03), then combinations (V-04..V-05).

**Axes explored:**
- **V-01**: Role sequence (Architect-first for analysis phases; Phase 9 PM-first enforced) — designed fail: **C-39 only** (T-37 CONDITION carries Part 1 inline exemplar but omits Part 2 correct-format prescription; T-38 CONDITION complete → C-40/C-41 PASS)
- **V-02**: Inertia framing (maximum prominence throughout; T-37 CONDITION complete; T-38 CONDITION abstract-only) — designed fail: **C-40 cascade → C-41** (T-38 CONDITION names condition category without quoting a deficient T-37 form)
- **V-03**: Phrasing register (conversational/descriptive "the PM should" rather than imperative "PM:"; T-37 and T-38 CONDITION both complete) — designed fail: **none** — tests whether register variation affects rubric outcomes
- **V-04**: Role sequence + Output format (Architect-first + table-heavy option anatomy; T-37 CONDITION complete → C-38/C-39 PASS; T-38 CONDITION carries Part 1 only) — designed fail: **C-41 only** (C-40 PASS since Part 1 present; C-40 PASS does not guarantee C-41 PASS)
- **V-05**: Lifecycle emphasis + Inertia framing (Phase 4b elevated to dedicated lifecycle position with boundary markers; maximum lifecycle explicitness; T-37 CONDITION abstract-only; T-38 CONDITION abstract-only) — designed fail: **C-38→C-39 cascade + C-40→C-41 cascade** (four simultaneous fails from two independent abstract-CONDITION authoring shortcuts)

**Predicted scores under v16:**
| Variation | Designed fails | A-tier pass | Composite |
|-----------|---------------|-------------|-----------|
| V-01 | C-39 | 33/34 | **99.71** |
| V-02 | C-40, C-41 | 32/34 | **99.41** |
| V-03 | none | 34/34 | **100.00** |
| V-04 | C-41 | 33/34 | **99.71** |
| V-05 | C-38, C-39, C-40, C-41 | 30/34 | **98.82** |

**Cascade invariants:**
- C-40 FAIL → C-41 FAIL (abstract T-38 CONDITION contains neither Part 1 nor Part 2)
- C-38 FAIL → C-39 FAIL (abstract T-37 CONDITION contains neither Part 1 nor Part 2)
- C-40 PASS does **not** guarantee C-41 PASS (Part 1 present, Part 2 absent = C-41 FAIL independently)
- C-38 PASS does **not** guarantee C-39 PASS (same logic for T-37)

---

## V-01 — Axis: Role Sequence (Architect-First) | Designed fail: C-39 only

**Hypothesis**: An Architect-first role sequence (Architect leads analysis phases, PM confirms business framing) passes all structural criteria. The T-37 CONDITION carries Part 1 (inline failure exemplar, C-38 PASS) but not Part 2 (correct-format prescription, C-39 FAIL). T-38 CONDITION is complete (both parts present, C-40 PASS, C-41 PASS). Role sequence is confirmed orthogonal to amendment table criteria — only C-39 fires. Score: 33/34 → 99.71.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the inertia competitor — the implicit default that wins if no action is taken.

ROLE SEQUENCE: Architect → PM (Phase 9 exception: PM issues recommendation first,
then Architect confirms feasibility)

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) and the Phase 9 exception as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-41 — one per v16 rubric criterion (C-01..C-41). Each
row must carry a populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
All other triggers T-01..T-41 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger CONDITION requirements.

PM: Confirm amendment table initialized before proceeding.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

Architect: State the technical problem space and constraints. One paragraph.

PM: Add the business gap, forcing function, and what the inertia competitor costs the
team if it wins by default. One paragraph.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Architect: Compose at least 3 options. The third option must be the inertia competitor,
labeled `do-nothing`. For each option produce:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — copy verbatim from Phase 1]
  RISK: [R-NN pending] — Do not compute P×I in Phase 2 RISK fields. Declare risk
        category only: Architect notes technical risk; PM notes adoption risk.
        Example: "[R-NN pending] — integration complexity with existing pipeline
        (Architect); adoption friction if workflow changes required (PM)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

PM: Confirm the do-nothing option carries plausible business rationale, not a dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build the risk register with columns:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 technical risk entries (R-01, R-02, R-03...). Include at least one risk
applying ONLY to the do-nothing option. Assign P and I on 1-5 scale. Compute P×I.

PM: Add at least one adoption or schedule risk entry (R-NN row).

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build comparison matrix with OPTIONS as column headers using Phase 2 labels verbatim:
Option-A | Option-B | do-nothing. The do-nothing column is the active inertia competitor —
active options must demonstrate sufficient advantage over it to justify action.
Rows: Business value, Time-to-value, Reversibility, Risk (R-NN cited), Inertia cost.

Architect: Add Effort and Integration complexity rows.

---

PHASE 4b — INERTIA ANALYSIS

PM: Produce a dedicated inertia analysis section. For each risk specific to the
do-nothing option, cite its R-NN identifier using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only — R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify every phase header produced so far carries a [GATE: X-NN] citation.
Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing present as inertia competitor, risk register
>= 3 entries, Phase 4b present with R-NN citations in canonical bracket form, phases
in declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build coverage table with columns: CRITERION | STATUS | CLOSED BY
One row per criterion: E-01..E-04, R-01..R-03, C-01..C-41.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending]
placeholders.

Enumerate citation sites by structural domain:

  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores]

  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each Domain 1 citation site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide rationale referencing at least two comparison
matrix dimensions. State whether the recommendation beats the inertia competitor and
on what basis. Include at least two qualifying conditions naming circumstances under
which this recommendation would no longer be valid.

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

Trigger rules T-01..T-41 — exactly 41 rows (one per C-01..C-41).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name both
                             structural domains explicitly by label)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                             P×I" prohibition adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain headers lack numeric index prefix —
                             "Domain N —" or ordinal equivalent required)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation
                             [R-NN pending] → [R-NN entries])
T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 per-site after-state omits P×I
                             compound scores alongside R-NN IDs)

T-37 CONDITION: fires when Domain 2 enumeration shows row-level confirmation without
  per-column attribution.
  [C-38 Part 1] Inline exemplar of firing construct: "Risk row: R-NN IDs applied to
  risk row" fires T-37 (row-level only, no per-column label).
  [C-39 Part 2 — V-01 designed axis: correct-format prescription omitted here]

T-38 CONDITION: fires when T-37 CONDITION entry is abstract-only — naming the condition
  category without quoting a deficient T-37 form.
  [C-40 Part 1] Inline exemplar of deficient T-37 form: "T-37 CONDITION: fires if
  Phase 9b Domain 2 enumeration does not carry per-option-column R-NN attribution"
  (category statement only, no quoted failure construct) — this abstract form fires T-38.
  [C-41 Part 2] Correct-format prescription for passing T-37 CONDITION: T-37 CONDITION
  must quote the failure construct, e.g., "row-level confirmation 'R-NN IDs applied to
  risk row' fires T-37; per-column format required: [Option-A column: R-NN IDs] |
  [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]".

T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION carries Part 1 exemplar but omits
                             Part 2 correct-format prescription)
T-40 PHASE = FINALIZATION  (fires if T-38 CONDITION lacks inline exemplar of abstract
                             T-37 CONDITION form — C-40)
T-41 PHASE = FINALIZATION  (fires if T-38 CONDITION carries Part 1 but omits Part 2
                             correct-format prescription for passing T-37 CONDITION — C-41)
```

---

## V-02 — Axis: Inertia Framing (Maximum Prominence) | Designed fail: C-40 cascade → C-41

**Hypothesis**: Foregrounding the inertia competitor in every phase header and body paragraph passes all inertia-related structural criteria (Phase 4b present, R-NN citations, canonical bracket form) and passes C-37, C-38, C-39 (T-37 CONDITION complete). However T-38 CONDITION is abstract-only — naming the condition without quoting a deficient T-37 form — which fails C-40, and by cascade fails C-41 (abstract CONDITION contains neither Part 1 nor Part 2). Inertia framing axis is confirmed orthogonal to T-38 CONDITION quality. Score: 32/34 → 99.41.

```
INERTIA FRAMING CONVENTION: The do-nothing option is the inertia competitor. It is the
incumbent default state that wins automatically if no decision is made. Every phase in
this document explicitly names the inertia competitor and its ongoing cost. The inertia
competitor receives equal analytical weight — not a straw man.

ROLE SEQUENCE: PM → Architect

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output. The do-nothing inertia competitor must appear
by name in every phase that evaluates options.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-41 — one per v16 rubric criterion (C-01..C-41). Each
row must carry a populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
All other triggers T-01..T-41 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger CONDITION requirements.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap,
the forcing function, the cost of the inertia competitor winning by default, and the
explicit business risk of continued inaction. Name the inertia competitor (do-nothing)
as the incumbent state in the problem statement.

Architect: Confirm the problem statement is technically grounded. Identify any technical
debt or capability decay that the inertia competitor accelerates.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor, labeled
`do-nothing`. The inertia competitor is an active option requiring the same analytical
rigor as Option-A and Option-B. For each option produce:

  OPTION: [label and description — do-nothing: explicit status-quo description]
  PROBLEM: [shared problem statement — copy verbatim from Phase 1]
  RISK: [R-NN pending] — Do not compute P×I in Phase 2 RISK fields. PM notes adoption
        and inertia risk category; Architect notes technical risk category.
        Example: "[R-NN pending] — ongoing technical debt accumulation under do-nothing
        (Architect); adoption window closing if action delayed beyond quarter (PM)"
  RATIONALE: [why this option is a candidate — do-nothing: conditions under which
              inaction remains a legitimate choice]

Option label register: Option-A, Option-B, do-nothing. Fixed for this document.

Architect: Confirm each active option's technical feasibility. Confirm the do-nothing
option's rationale names specific conditions rather than defaulting to inaction.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build the risk register:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 technical risk entries. Include at least one inertia risk applying ONLY to
the do-nothing option (technical debt accumulation, opportunity cost, competitive
erosion). Label inertia-specific risks with "(inertia risk)" in the RISK column.
Assign P and I on 1-5 scale. Compute P×I.

PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build comparison matrix. Column headers use Phase 2 labels verbatim:
Option-A | Option-B | do-nothing. The do-nothing column is the active inertia
competitor — designate it explicitly in the matrix header. Active options must
demonstrate sufficient advantage over the inertia competitor to justify action.
Rows: Business value, Time-to-value, Reversibility, Risk (R-NN cited), Inertia cost,
Inertia risk exposure (unique dimension for do-nothing column comparison).

Architect: Add Effort and Integration complexity rows. Score the do-nothing column
against the same rubric as active options.

---

PHASE 4b — INERTIA ANALYSIS

PM: Produce a dedicated inertia analysis section. Enumerate every risk from Phase 3
that specifically affects the do-nothing option. For each inertia risk, cite its R-NN
identifier using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Address: (1) compounding nature of inertia risks over time, (2) threshold conditions
under which the inertia competitor ceases to be viable, (3) earliest point at which
inertia cost exceeds the cost of any active option.

Do not express inertia risks as P×I scores only — R-NN pairing and canonical bracket
structure are both required.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify every phase header carries a [GATE: X-NN] citation. Mark missing
citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing present as labeled inertia competitor, risk
register >= 3 entries including at least one inertia risk, Phase 4b present with R-NN
citations in canonical bracket form, phases in declared sequence. Reference each
option by Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build coverage table with columns: CRITERION | STATUS | CLOSED BY
One row per criterion: E-01..E-04, R-01..R-03, C-01..C-41.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending]
placeholders.

Enumerate citation sites by structural domain:

  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores,
      including all inertia-specific risks]

  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each Domain 1 citation site.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide rationale referencing at least two comparison
matrix dimensions. State explicitly whether the recommendation beats the inertia
competitor and on what basis. Name at least two qualifying conditions under which this
recommendation would no longer be valid — conditions under which the inertia competitor
would re-emerge as the preferred path.

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

Trigger rules T-01..T-41 — exactly 41 rows (one per C-01..C-41).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name both
                             structural domains explicitly by label)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                             P×I" prohibition adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain headers lack numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 per-site after-state omits P×I
                             compound scores alongside R-NN IDs)

T-37 CONDITION: fires when Domain 2 enumeration shows row-level confirmation without
  per-column attribution.
  [C-38 Part 1] Inline exemplar: "Risk row: R-NN IDs applied to risk row" fires T-37.
  [C-39 Part 2] Correct-format prescription: per-column format required:
  "[Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]".

T-38 CONDITION: fires if T-37 CONDITION lacks an inline failure exemplar.
  [V-02 designed axis — C-40 Part 1 exemplar of deficient T-37 form absent; T-38
   CONDITION carries only the abstract category statement; C-40 FAIL → C-41 FAIL]

T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION carries Part 1 exemplar but omits
                             Part 2 correct-format prescription)
T-40 PHASE = FINALIZATION  (fires if T-38 CONDITION lacks inline exemplar of abstract
                             T-37 CONDITION form — C-40)
T-41 PHASE = FINALIZATION  (fires if T-38 CONDITION carries Part 1 but omits Part 2
                             correct-format prescription for passing T-37 CONDITION — C-41)
```

---

## V-03 — Axis: Phrasing Register (Conversational/Descriptive) | Designed fail: none

**Hypothesis**: A descriptive, guidance-oriented register ("the PM should...", "the goal here is...", "consider...") satisfies all structural criteria equivalently to an imperative register. T-37 and T-38 CONDITION fields are both complete (two-part form). No designed fail. Tests whether phrasing register is a neutral axis under the v16 rubric. Expected: 34/34 → 100.00.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the inertia competitor — the implicit default that wins if no action is taken.

ROLE SEQUENCE: PM → Architect

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

The PM should open by declaring the role sequence (PM → Architect) and the inertia
framing convention as a typed header at the top of the output.

The goal in Phase 0 is to establish the amendment tracking table before any options or
analysis are written. The table should use columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Consider populating all 41 trigger rows T-01..T-41 at initialization — one per v16
rubric criterion (C-01..C-41). Each row needs a populated PHASE value. STATUS starts
as PENDING for all rows.

The one PRE-DOCUMENT trigger is T-24 (fires if row count is not exactly 41). All
other triggers fire at FINALIZATION. Specific CONDITION requirements for key triggers
are in the AMENDMENT TABLE SPECIFICATION below.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

The PM's role here is to frame the shared problem being decided. A single paragraph
works well — covering the business gap, what's forcing a decision now, and what it
would cost the team if the inertia competitor (do-nothing) wins by default.

The Architect should then confirm the problem statement is technically grounded and
flag any constraints the PM framing may have understated.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

The PM should compose at least 3 options. The third option needs to be the inertia
competitor, explicitly labeled `do-nothing`. Using this exact label matters — it's
the fixed register entry for all downstream phases.

For each option, the anatomy should include all four fields:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — copy verbatim from Phase 1, not paraphrased]
  RISK: [R-NN pending] — The goal is to avoid computing P×I at this stage. Do not
        compute P×I in Phase 2 RISK fields. Reserve the register-linkage slot with
        a placeholder and a brief risk category note:
        "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels should travel
verbatim through all downstream phases — the comparison matrix, Phase 9b, Phase 9.

The Architect should review the option framing for technical completeness and confirm
the do-nothing option carries plausible technical rationale rather than dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

The Architect should build the risk register. Columns:
  R-NN | RISK | P | I | P×I | MITIGATION

Three or more technical risk entries (R-01, R-02, R-03...) are the minimum. It's
worth including at least one risk that only applies to the do-nothing option — the
kind of risk that compounds when action is deferred (technical debt, opportunity cost).
Scores use a 1-5 scale for both P and I, with P×I computed per entry.

The PM should add at least one adoption or schedule risk entry as a named R-NN row.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

The PM builds the comparison matrix. Column headers should use Phase 2 labels verbatim:
Option-A | Option-B | do-nothing. The do-nothing column is the active inertia competitor
in this matrix — designating it explicitly in the matrix header is the goal (not just
implied by the column label). Active options need to show sufficient advantage over
the inertia competitor to justify action.
Suggested rows: Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.

The Architect should contribute Effort and Integration complexity rows.

---

PHASE 4b — INERTIA ANALYSIS

The PM should produce a dedicated inertia analysis section upstream of Phase 9b. For
each risk that specifically affects the do-nothing option, cite its R-NN identifier.
The canonical bracket form works best here:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Expressing inertia risks as P×I scores without R-NN pairing would omit the register
linkage that downstream phases need — so both elements should be present in each entry.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

The Architect should verify that every phase header produced so far carries a
[GATE: X-NN] citation referencing a real criterion ID. Any missing citations should
be recorded in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Before proceeding to the coverage table, verify: option count >= 3, do-nothing present
as the labeled inertia competitor, risk register >= 3 entries including at least one
inertia risk, Phase 4b present with R-NN citations in canonical bracket form, phases
in declared sequence. Reference each option by its Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
One row per criterion: E-01..E-04, R-01..R-03, C-01..C-41.
STATUS = PASS or FAIL. CLOSED BY = the phase or step that satisfied the criterion.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

The Architect should back-fill R-NN IDs into option RISK fields, replacing every
[R-NN pending] placeholder.

The enumeration should explicitly name two structural domains:

  Domain 1 — Option RISK fields (by option label):
    The goal is a per-site arrow notation showing the transition at each RISK field:
    [Option-A] RISK field: [R-NN pending] → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores]
    P×I compound scores should appear in the after-state, not just R-NN IDs alone.

  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

The PM should name the recommended option and provide rationale referencing at least
two comparison matrix dimensions. The recommendation should explicitly state whether
it beats the inertia competitor and on what basis. Including at least two qualifying
conditions — specific circumstances under which the recommendation would no longer be
valid — makes the sign-off durable.

The Architect should then confirm technical feasibility.

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

Trigger rules T-01..T-41 — exactly 41 rows (one per C-01..C-41).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name both
                             structural domains explicitly by label)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                             P×I" prohibition adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain headers lack numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 per-site after-state omits P×I
                             compound scores alongside R-NN IDs)

T-37 CONDITION: fires when Domain 2 enumeration shows row-level confirmation without
  per-column attribution.
  [C-38 Part 1] Inline exemplar of firing construct: "Risk row: R-NN IDs applied to
  risk row" fires T-37 (row-level only, no per-column labels present).
  [C-39 Part 2] Correct-format prescription: per-column format required:
  "[Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]".

T-38 CONDITION: fires when T-37 CONDITION entry is abstract-only — naming the condition
  category without quoting a deficient T-37 form.
  [C-40 Part 1] Inline exemplar of deficient T-37 form: "T-37 CONDITION: fires if
  Phase 9b Domain 2 enumeration does not carry per-option-column R-NN attribution"
  (category statement only, no quoted failure construct) — this abstract form fires T-38.
  [C-41 Part 2] Correct-format prescription for passing T-37 CONDITION: T-37 CONDITION
  must quote the exact failure construct, e.g., "row-level confirmation 'R-NN IDs
  applied to risk row' fires T-37; per-column format required: [Option-A column: R-NN IDs] |
  [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]".

T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION carries Part 1 exemplar but omits
                             Part 2 correct-format prescription)
T-40 PHASE = FINALIZATION  (fires if T-38 CONDITION lacks inline exemplar of abstract
                             T-37 CONDITION form — C-40)
T-41 PHASE = FINALIZATION  (fires if T-38 CONDITION carries Part 1 but omits Part 2
                             correct-format prescription for passing T-37 CONDITION — C-41)
```

---

## V-04 — Axes: Role Sequence + Output Format (Architect-First + Table-Heavy) | Designed fail: C-41 only

**Hypothesis**: An Architect-first role sequence combined with table-heavy option anatomy (OPTION / PROBLEM / RISK / RATIONALE as a table, Phase 9b Domain 1 as a transition table) passes all structural criteria at the same rate as prose format. T-37 CONDITION is complete (Part 1 + Part 2, C-38/C-39 PASS). T-38 CONDITION carries Part 1 only (the abstract-T-37 exemplar is present, **C-40 PASS**) but omits Part 2 (no prescription for what a passing T-37 CONDITION looks like, **C-41 FAIL**). The C-40 PASS / C-41 FAIL combination confirms the cascade is one-directional. Score: 33/34 → 99.71.

```
INERTIA FRAMING CONVENTION: Throughout this document the do-nothing option is treated as
the inertia competitor — the implicit default that wins if no action is taken.

ROLE SEQUENCE: Architect → PM (Phase 9 exception: PM recommends first, Architect confirms)

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

Architect: Declare the role sequence (Architect → PM) and the Phase 9 exception as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-41 — one per v16 rubric criterion (C-01..C-41). Each
row must carry a populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
All other triggers T-01..T-41 have PHASE = FINALIZATION.
See AMENDMENT TABLE SPECIFICATION below for key trigger CONDITION requirements.

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

Architect: State the technical problem space and constraints. One paragraph.

PM: Add the business gap, forcing function, and cost of inertia. One paragraph.

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

Architect: Compose at least 3 options as a structured table. The third option must be
the inertia competitor, labeled `do-nothing`. Use the four-column option table:

| OPTION | PROBLEM | RISK | RATIONALE |
|--------|---------|------|-----------|
| Option-A: [description] | [shared problem — verbatim from Phase 1] | [R-NN pending] — Do not compute P×I in Phase 2 RISK fields. Technical risk category (Architect); adoption risk category (PM). | [candidate rationale] |
| Option-B: [description] | [verbatim] | [R-NN pending] — [category note] | [rationale] |
| do-nothing: [status-quo description] | [verbatim] | [R-NN pending] — [inertia risk category note] | [conditions for inaction] |

Option label register: Option-A, Option-B, do-nothing. Fixed for this document.

PM: Confirm do-nothing carries plausible business rationale, not dismissal.

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build the risk register as a table:

| R-NN | RISK | P | I | P×I | MITIGATION |
|------|------|---|---|-----|------------|

At least 3 technical risk entries (R-01, R-02, R-03...). Include at least one risk
applying ONLY to the do-nothing option. P and I on 1-5 scale. Compute P×I.

PM: Add at least one adoption or schedule risk row to the table.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build comparison matrix. Column headers use Phase 2 labels verbatim:
Option-A | Option-B | do-nothing. The do-nothing column is the active inertia
competitor — designate it explicitly in the matrix header.

| DIMENSION | Option-A | Option-B | do-nothing (inertia competitor) |
|-----------|----------|----------|---------------------------------|
| Business value | ... | ... | ... |
| Time-to-value | ... | ... | ... |
| Reversibility | ... | ... | ... |
| Risk (R-NN cited) | ... | ... | ... |
| Inertia cost | ... | ... | ... |

Architect: Add Effort and Integration complexity rows to the matrix table.

---

PHASE 4b — INERTIA ANALYSIS

PM: Produce a dedicated inertia analysis section. For each risk specific to the
do-nothing option, cite its R-NN identifier using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Do not express inertia risks as P×I scores only.

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify every phase header carries a [GATE: X-NN] citation. Record missing
citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing present as inertia competitor, risk register
>= 3 entries, Phase 4b present with R-NN citations in canonical bracket form, phases
in declared sequence. Reference each option by Phase 2 label verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build coverage table as a table:

| CRITERION | STATUS | CLOSED BY |
|-----------|--------|-----------|

One row per criterion: E-01..E-04, R-01..R-03, C-01..C-41.
STATUS = PASS or FAIL. CLOSED BY = phase or step.

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields. Use a structured table for
Domain 1 and explicit enumeration for Domain 2.

  Domain 1 — Option RISK fields:

  | OPTION RISK FIELD | BEFORE | AFTER |
  |-------------------|--------|-------|
  | [Option-A] RISK field | [R-NN pending] | → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)] |
  | [Option-B] RISK field | [R-NN pending] | → [applicable R-NN entries with P×I scores] |
  | [do-nothing] RISK field | [R-NN pending] | → [applicable R-NN entries with P×I scores] |

  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each Domain 1 row.

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide rationale referencing at least two comparison
matrix dimensions. State whether the recommendation beats the inertia competitor and
on what basis. Include at least two qualifying conditions naming when this recommendation
would no longer be valid.

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

Trigger rules T-01..T-41 — exactly 41 rows (one per C-01..C-41).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name both
                             structural domains explicitly by label)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                             P×I" prohibition adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain headers lack numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 per-site after-state omits P×I
                             compound scores alongside R-NN IDs)

T-37 CONDITION: fires when Domain 2 enumeration shows row-level confirmation without
  per-column attribution.
  [C-38 Part 1] Inline exemplar: "Risk row: R-NN IDs applied to risk row" fires T-37.
  [C-39 Part 2] Correct-format prescription: per-column format required:
  "[Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]".

T-38 CONDITION: fires when T-37 CONDITION entry is abstract-only — naming the condition
  category without quoting a deficient T-37 form.
  [C-40 Part 1] Inline exemplar of deficient T-37 form: "T-37 CONDITION: fires if
  Phase 9b Domain 2 enumeration does not carry per-option-column R-NN attribution"
  (category statement only, no quoted failure construct) — this abstract form fires T-38.
  [V-04 designed axis — C-41 Part 2 omitted: no correct-format prescription for what
   a passing T-37 CONDITION looks like; C-40 PASS, C-41 FAIL]

T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION carries Part 1 exemplar but omits
                             Part 2 correct-format prescription)
T-40 PHASE = FINALIZATION  (fires if T-38 CONDITION lacks inline exemplar of abstract
                             T-37 CONDITION form — C-40)
T-41 PHASE = FINALIZATION  (fires if T-38 CONDITION carries Part 1 but omits Part 2
                             correct-format prescription for passing T-37 CONDITION — C-41)
```

---

## V-05 — Axes: Lifecycle Emphasis + Inertia Framing | Designed fail: C-38→C-39 + C-40→C-41 (4 fails)

**Hypothesis**: Maximum lifecycle boundary explicitness (full phase manifest in Phase 0, explicit `[BOUNDARY]` markers at every phase transition, Phase 4b elevated to a named position in the lifecycle manifest) combined with maximum inertia prominence passes all inertia-structural criteria. However both T-37 and T-38 CONDITION fields are abstract-only — naming condition categories without quoting exemplars. This fires two independent cascades: (1) C-38 FAIL → C-39 FAIL (abstract T-37 CONDITION), (2) C-40 FAIL → C-41 FAIL (abstract T-38 CONDITION). Four simultaneous advisory fails from two authoring shortcuts isolated in the AMENDMENT TABLE SPECIFICATION. Score: 30/34 → 98.82.

```
INERTIA FRAMING CONVENTION: The do-nothing option is the inertia competitor — the
incumbent default that wins automatically if no decision is made. Every phase of this
document explicitly names the inertia competitor and its ongoing cost. The inertia
competitor receives equal analytical weight as any active option.

ROLE SEQUENCE: PM → Architect

LIFECYCLE BOUNDARY MANIFEST:
  Phase 0  [GATE: E-01]  — PRE-DOCUMENT: Amendment table initialization
  Phase 1  [GATE: E-02]  — Problem statement
  Phase 2  [GATE: E-02]  — Option composition (no P×I permitted at this stage)
  Phase 3  [GATE: R-01]  — Risk register (first P×I computation appears here)
  Phase 4  [GATE: E-03]  — Comparison matrix
  Phase 4b              — Inertia analysis (dedicated lifecycle position)
  Phase 5  [GATE: C-21]  — Gate audit
  Phase 6  [GATE: R-02]  — Prerequisites check
  Phase 7  [GATE: C-22]  — Coverage table
  Phase 9b [GATE: C-26]  — Risk propagation (back-fill only — no new content)
  Phase 9  [GATE: E-04]  — Recommendation (PM leads, Architect confirms)
  Phase 10 [GATE: R-03]  — Finalization (4-step structured closure)

Lifecycle invariant: no phase may execute content belonging to a later phase. Phase 9b
may only back-fill; it may not introduce new options or risks. Phase 9 may not modify
the risk register.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect), the inertia framing convention, and
the lifecycle boundary manifest as a typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-41 — one per v16 rubric criterion (C-01..C-41). Each
row must carry a populated PHASE value aligned to the lifecycle boundary manifest.
Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
All other triggers (T-01..T-23, T-25..T-41) PHASE = FINALIZATION unless a more
specific phase applies per their criterion scope.
See AMENDMENT TABLE SPECIFICATION below for individual CONDITION requirements.

[BOUNDARY: Phase 0 complete. Phase 1 begins.]

---

PHASE 1 — PROBLEM STATEMENT [GATE: E-02]

PM: State the shared problem being decided. One paragraph. Include: the business gap,
the forcing function, the cost of the inertia competitor winning by default. Name the
inertia competitor explicitly as the incumbent state in the problem statement.

Architect: Confirm the problem statement is technically grounded.

[BOUNDARY: Phase 1 complete. No options before Phase 2.]

---

PHASE 2 — OPTION COMPOSITION [GATE: E-02]

PM: Compose at least 3 options. The third option must be the inertia competitor,
labeled `do-nothing`. For each option produce:

  OPTION: [label and description]
  PROBLEM: [shared problem statement — copy verbatim from Phase 1]
  RISK: [R-NN pending] — Do not compute P×I in Phase 2 RISK fields. Declare risk
        category only. PM notes adoption/inertia risk; Architect notes technical risk.
        Example: "[R-NN pending] — adoption friction if workflow changes required (PM);
        integration complexity with existing pipeline (Architect)"
  RATIONALE: [why this option is a candidate]

Option label register: Option-A, Option-B, do-nothing. These labels are fixed for this
document and must appear verbatim in all downstream phases.

Architect: Review option framing for technical completeness.

[BOUNDARY: Phase 2 complete. No P×I computation before Phase 3.]

---

PHASE 3 — RISK REGISTER [GATE: R-01]

Architect: Build the risk register:
  R-NN | RISK | P | I | P×I | MITIGATION

At least 3 technical risk entries (R-01, R-02, R-03...). Include at least one inertia
risk applying ONLY to the do-nothing option. Assign P and I on 1-5 scale. Compute P×I.

PM: Add at least one adoption or schedule risk entry.

[BOUNDARY: Phase 3 complete. No comparison matrix before Phase 4.]

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build comparison matrix with OPTIONS as column headers using Phase 2 labels
verbatim: Option-A | Option-B | do-nothing. The do-nothing column is the active
inertia competitor — designate it explicitly in the matrix header. Active options
must demonstrate sufficient advantage over the inertia competitor to justify action.
Rows: Business value, Time-to-value, Reversibility, Risk (R-NN cited), Inertia cost.

Architect: Add Effort and Integration complexity rows.

[BOUNDARY: Phase 4 complete. Inertia analysis is a separate lifecycle position.]

---

PHASE 4b — INERTIA ANALYSIS

PM: Produce a dedicated inertia analysis section. This phase occupies its own position
in the lifecycle manifest between Phase 4 and Phase 5. For each risk specific to the
do-nothing option, cite its R-NN identifier using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

Address: (1) which inertia risks compound over time, (2) threshold conditions under
which do-nothing ceases to be viable, (3) decision timeline implied by inertia cost
accumulation.

Do not express inertia risks as P×I scores only — R-NN pairing and canonical bracket
structure are both required.

[BOUNDARY: Phase 4b complete. Gate audit begins Phase 5.]

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify every phase header carries a [GATE: X-NN] citation. Mark missing
citations in the amendment table (STATUS = OPEN).

[BOUNDARY: Phase 5 complete. Prerequisites check begins Phase 6.]

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing present as inertia competitor, risk register
>= 3 entries including at least one inertia risk, Phase 4b present with R-NN citations
in canonical bracket form, phases appearing in declared lifecycle sequence. Reference
each option by Phase 2 label verbatim.

[BOUNDARY: Phase 6 complete. Coverage table begins Phase 7.]

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build coverage table with columns: CRITERION | STATUS | CLOSED BY
One row per criterion: E-01..E-04, R-01..R-03, C-01..C-41.
STATUS = PASS or FAIL. CLOSED BY = phase or step that satisfied the criterion.

[BOUNDARY: Phase 7 complete. Risk propagation begins Phase 9b.]

---

PHASE 9b — RISK PROPAGATION [GATE: C-26]

Architect: Back-fill R-NN IDs into option RISK fields, replacing [R-NN pending]
placeholders. This phase is exclusively for back-fill — no new options or risks.

Enumerate citation sites by structural domain:

  Domain 1 — Option RISK fields (by option label):
    [Option-A] RISK field: [R-NN pending] → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)]
    [Option-B] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores]
    [do-nothing] RISK field: [R-NN pending] → [applicable R-NN entries with P×I scores]

  Domain 2 — Comparison matrix risk column:
    Risk row: [Option-A column: R-NN IDs] | [Option-B column: R-NN IDs] | [do-nothing column: R-NN IDs]

Confirm P×I formula applied at each Domain 1 citation site.

[BOUNDARY: Phase 9b complete. Recommendation begins Phase 9.]

---

PHASE 9 — RECOMMENDATION [GATE: E-04]

PM: Name the recommended option. Provide rationale referencing at least two comparison
matrix dimensions. State explicitly whether the recommendation beats the inertia
competitor and on what basis. Include at least two qualifying conditions naming
circumstances under which this recommendation would no longer be valid.

Architect: Confirm technical feasibility of the recommended option.

[BOUNDARY: Phase 9 complete. Finalization begins Phase 10.]

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

Trigger rules T-01..T-41 — exactly 41 rows (one per C-01..C-41).
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE

T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 41)
T-22 PHASE = FINALIZATION  (fires if coverage table omits CLOSED BY column)
T-23 PHASE = FINALIZATION  (fires if RISK fields contain no R-NN linkage in final output)
T-26 PHASE = FINALIZATION  (fires if no dedicated Phase 9b risk-propagation phase present)
T-31 PHASE = FINALIZATION  (fires if Phase 2 RISK fields used no [R-NN pending] placeholder)
T-32 PHASE = FINALIZATION  (fires if Phase 9b citation-site enumeration does not name both
                             structural domains explicitly by label)
T-33 PHASE = FINALIZATION  (fires if Phase 2 RISK template omits explicit "Do not compute
                             P×I" prohibition adjacent to placeholder directive)
T-34 PHASE = FINALIZATION  (fires if Phase 9b domain headers lack numeric index prefix)
T-35 PHASE = FINALIZATION  (fires if Phase 9b per-site entries lack arrow transition notation)
T-36 PHASE = FINALIZATION  (fires if Phase 9b Domain 1 per-site after-state omits P×I
                             compound scores alongside R-NN IDs)

T-37 CONDITION: fires if Phase 9b Domain 2 lacks per-option-column R-NN attribution.
  [V-05 designed axis — C-38 Part 1 inline exemplar absent; T-37 CONDITION is abstract-
   only (names condition, quotes no failure construct); C-38 FAIL → C-39 FAIL by cascade]

T-38 CONDITION: fires if T-37 CONDITION lacks an inline failure exemplar.
  [V-05 designed axis — C-40 Part 1 exemplar of deficient T-37 form absent; T-38
   CONDITION is abstract-only; C-40 FAIL → C-41 FAIL by cascade]

T-39 PHASE = FINALIZATION  (fires if T-37 CONDITION carries Part 1 exemplar but omits
                             Part 2 correct-format prescription)
T-40 PHASE = FINALIZATION  (fires if T-38 CONDITION lacks inline exemplar of abstract
                             T-37 CONDITION form — C-40)
T-41 PHASE = FINALIZATION  (fires if T-38 CONDITION carries Part 1 but omits Part 2
                             correct-format prescription for passing T-37 CONDITION — C-41)
```

---

## Design Notes

**V-01 isolation (role sequence vs amendment table)**: Role sequence is orthogonal to amendment table criteria. V-01 confirms that Architect-first ordering does not interfere with T-37/T-38 CONDITION quality — only the explicitly designed T-37 Part 2 omission generates a finding (T-39 fires, Finding 1). T-38 CONDITION is complete, so C-40 and C-41 pass independently.

**V-02 isolation (inertia framing vs T-38 CONDITION)**: Maximum inertia prominence passes all Phase 4b structural criteria (Phase 4b present, canonical bracket form, R-NN citations) and passes C-37..C-39 entirely. The T-38 CONDITION abstract-only designation is the sole source of failures (T-40 fires → C-40 FAIL, T-41 fires → C-41 FAIL by cascade). Confirms inertia framing axis does not interact with T-38 CONDITION quality.

**V-03 register parity test**: Conversational register preserves all structural invariants. Both T-37 and T-38 CONDITION fields carry complete two-part specifications in the descriptive register. Expected 100.00 establishes phrasing register as a rubric-neutral axis. If V-03 scores below 34/34, the register variation is interacting with structural production — that interaction is the new finding.

**V-04 table format + C-40 PASS / C-41 FAIL precision test**: Table-heavy format (option anatomy as table, Phase 9b Domain 1 as transition table) does not affect amendment table criteria. T-38 CONDITION Part 1 is present (abstract-T-37-form exemplar → C-40 PASS), Part 2 absent (no prescription for passing T-37 CONDITION → C-41 FAIL). This is the cleanest C-41 isolation achievable: C-40 PASS is the necessary precondition and C-41 FAIL is independently verifiable. Confirms the one-directional cascade asymmetry stated in the rubric.

**V-05 dual-cascade path**: Two independent abstract CONDITION entries (T-37 and T-38 both abstract-only) produce four simultaneous advisory fails: C-38 → C-39 (from abstract T-37 CONDITION) and C-40 → C-41 (from abstract T-38 CONDITION). The lifecycle emphasis axis contributes zero fails of its own — all four fails trace exclusively to the two AMENDMENT TABLE SPECIFICATION authoring shortcuts. This confirms the cascades are additive and independent, and that `[BOUNDARY]` marker density and Phase 4b promotion have no interaction with T-37/T-38 CONDITION quality.
