---
skill: quest-golden
skill_target: draft-proposal
date: 2026-03-14
rounds: 20
rubric_final: draft-proposal-rubric-v21-2026-03-14.md
score: 99.76
status: GOLDEN
---

# draft-proposal — Golden Prompt

**Source:** QU5 simplified (20% reduction from R20 complete golden · PASS)
**Rubric:** v21 · Denominator /44 · Criteria C-01..C-51 · Triggers T-01..T-51
**Scores under v21:** Golden (fully passing) = 100.00 · Nearest miss (V-01, C-48+C-50) = 99.55

---

## Golden Prompt Body

```
INERTIA FRAMING CONVENTION: the do-nothing option is the inertia competitor.

---

PHASE 0 — PRE-DOCUMENT [GATE: E-01]

PM: Declare the role sequence (PM → Architect) and the inertia framing convention as a
typed header at the top of the output.

Initialize the amendment tracking table with columns:
  ID | TRIGGER | CONDITION | STATUS | PHASE

Populate trigger rules T-01..T-51 — one per rubric criterion. Each row must carry a
populated PHASE value. Leave STATUS = PENDING for all rows at init.

T-24 PHASE = PRE-DOCUMENT (fires if amendment table row count != 51)
All other triggers T-01..T-51 have PHASE = FINALIZATION.

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
risk that applies ONLY to the do-nothing option. Assign P and I scores on the defined
scale. Compute P×I. PM: Add at least one adoption or schedule risk entry.

---

PHASE 4 — COMPARISON MATRIX [GATE: E-03]

PM: Build a comparison matrix with OPTIONS as column headers. Use Phase 2 option labels
verbatim: Option-A | Option-B | do-nothing. Designate the do-nothing column as the active
inertia competitor in the matrix.
Matrix rows (dimensions): Business value, Time-to-value, Reversibility, Risk (R-NN cited),
Inertia cost.
Architect: Add Effort and Integration complexity as rows.

---

PHASE 4b — INERTIA ANALYSIS [GATE: C-06]

PM: Produce a dedicated inertia analysis section. For each risk that specifically affects
the do-nothing option, cite its R-NN identifier from the Phase 3 risk register. Structure
each inertia risk entry using the canonical bracket form:
  [R-NN] — [inertia risk name, P×I compound score]: [inertia impact description]

---

PHASE 5 — GATE AUDIT [GATE: C-21]

Architect: Verify that every phase header produced so far carries a [GATE: X-NN]
citation. Mark any missing citations in the amendment table (STATUS = OPEN).

---

PHASE 6 — PREREQUISITES CHECK [GATE: R-02]

Verify: option count >= 3, do-nothing option present as inertia competitor, risk register
has at least 3 entries including one inertia risk, assumption register has at least 2 A-NN
entries, phases appear in declared sequence. Reference each option by its Phase 2 label
verbatim.

---

PHASE 7 — COVERAGE TABLE [GATE: C-22]

Build a coverage table with columns: CRITERION | STATUS | CLOSED BY
Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-51.
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
under which the recommendation would change.

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

Trigger rules T-01..T-51 — exactly 51 rows.
Columns: ID | TRIGGER | CONDITION | STATUS | PHASE
T-24 PHASE = PRE-DOCUMENT  (fires if amendment table row count != 51)
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
                             omits the composite identifier.
                             Part 2 — Correct-format prescription: A passing T-38
                             CONDITION entry must show an inline quoted example of an
                             abstract-only form, such as 'fires if Phase 9b per-site
                             entries omit option-label prefix'.)
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
                             T-38 CONDITION entry that omits the required identifier.
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
                             a deficient T-40 CONDITION form)
T-46 PHASE = FINALIZATION  (fires if T-42 CONDITION lacks correct-format prescription
                             showing what a passing T-40 CONDITION entry looks like.
                             Inline exemplar of the Part-1-only T-42 CONDITION state that
                             fires T-46: 'Part 1 — Failure exemplar with explanation: A
                             deficient T-40 CONDITION entry reads: "fires if Phase 9b Domain
                             2 per-column enumeration lacks Risk row: anchor prefix" —
                             abstract because it names the Domain 2 format requirement
                             without quoting a deficient T-38 form.' [END — no Part 2 label
                             and no Part 2 content present])
T-47 PHASE = FINALIZATION  (fires if T-42 CONDITION exemplar lacks explanation of why
                             the quoted T-40 form is abstract.
                             Inline exemplar of the exemplar-without-explanation T-42
                             CONDITION state that fires T-47: 'fires if T-40 CONDITION lacks
                             inline failure exemplar — example of deficient T-40: "fires if
                             Phase 9b Domain 2 per-column enumeration lacks Risk row:
                             prefix"' — this T-42 CONDITION has a quoted deficient T-40 form
                             (C-45 PASS) but no explanation of why that T-40 form is abstract.)
T-48 PHASE = FINALIZATION  (fires if T-46 CONDITION lacks inline exemplar of the
                             Part-1-only T-42 CONDITION state that T-46 fires for)
T-49 PHASE = FINALIZATION  (fires if T-47 CONDITION lacks inline exemplar of the
                             T-42-exemplar-without-explanation state that T-47 fires for)
T-50 PHASE = FINALIZATION  (fires if T-46 CONDITION exemplar lacks the terminal marker
                             [END — no Part 2 label and no Part 2 content present])
T-51 PHASE = FINALIZATION  (fires if T-47 CONDITION exemplar lacks the (C-45 PASS)
                             pass-state annotation)
```

---

## What Made It Golden

Five patterns distinguish the golden from baseline V-01 (which fails C-48 + C-50):

**1. T-46 carries a complete inline exemplar with `[END —...]` terminal marker (C-48 + C-50)**
V-01's T-46 CONDITION is abstract — it names the Part-2-absent state as a category without
showing what a Part-1-only T-42 CONDITION entry actually looks like. The golden quotes the
exact deficient T-42 form, then appends `[END — no Part 2 label and no Part 2 content present]`
as an explicit delineation marker. The terminal marker makes Part 1's end and Part 2's
absence simultaneously unambiguous — a reviewer need not infer the boundary.

**2. T-47 carries the `(C-45 PASS)` pass-state annotation (C-49 + C-51)**
T-47's exemplar quotes a T-42 CONDITION that has an exemplar present but no
explanation-of-abstractness. Without the `(C-45 PASS)` annotation, a reviewer must
confirm the cascade prerequisite (C-45 satisfied) by reading the quoted T-42 form
independently. The annotation makes the prerequisite chain status inline and
self-documenting — the exemplar tells you which upstream criteria are PASS.

**3. 51-row table with T-48..T-51 (C-24)**
T-24 fires if row count != 51. The golden declares T-01..T-51 at PHASE 0, ensuring
T-48, T-49, T-50, and T-51 exist as rows testing the v21 criteria. A prompt carrying
forward the v20 49-row count generates a table that fails C-24 at PRE-DOCUMENT.

**4. Self-referential cascade chain (C-42..C-51)**
Each trigger from T-40 through T-51 tests the CONDITION cell quality of the immediately
preceding trigger: T-40 tests T-38, T-42 tests T-40, T-46 tests T-42, T-47 tests T-42,
T-48 tests T-46, T-49 tests T-47, T-50 tests T-46's exemplar content, T-51 tests T-47's
exemplar content. The chain is fully specified in the golden — every link is present,
exemplified, and explained. A LLM generating the amendment table must reproduce this
structure or specific criteria cascade.

**5. Simplification without criterion loss (20% reduction)**
382 words were removed — all from trigger CONDITION text whose content is tested by no
rubric criterion. The structurally-tested cells (T-40, T-42, T-46, T-47) retain every
required element. The result is the minimal prompt form that passes 44/44 under v21,
demonstrating that the excess text was explanatory scaffolding for the prompt author,
not specification content for the LLM.

---

## Final Rubric Criteria Summary (v21 · /44)

### Scoring formula
`(E/4 × 60) + (R/3 × 30) + (A/44 × 10)`
- E-tier (4 criteria): 60 points — correctness gate
- R-tier (3 criteria): 30 points — reliability gate
- A-tier (44 criteria): 10 points — aspirational ceiling

### E-tier (essential, 60 pts)

| ID | Criterion |
|----|-----------|
| E-01 | Role sequence (PM → Architect) declared as typed header at document open; applied to all phase headers |
| E-02 | 3+ options, one labeled `do-nothing`; every option has OPTION / PROBLEM / RISK / RATIONALE fields |
| E-03 | Comparison matrix with option-label column headers; 4+ dimensions; PM + Architect each contribute ≥1 row |
| E-04 | Recommendation names option, cites 2+ matrix dimensions, states 2+ qualifying conditions |

### R-tier (reliability, 30 pts)

| ID | Criterion |
|----|-----------|
| R-01 | Risk register with P/I/P×I and project-specific scoring anchors; 3+ entries; ≥1 do-nothing-only risk |
| R-02 | Prerequisites check phase verifying all structural prerequisites before recommendation |
| R-03 | Phase 10 finalization as explicit 4-step numbered list |

### A-tier (aspirational, 10 pts · /44)

**Structural mandatory (C-01..C-07):** amendment table present, phase lifecycle complete,
dual-role declared, gate citations present, inertia competitor labeled in matrix, inertia
analysis section present, coverage table present.

**Key aspirational criteria:**

| Range | What they test |
|-------|----------------|
| C-08 | Assumption register (≥2 A-NN entries, distinct from risk register) |
| C-16 | Project-specific P/I scoring anchors defined before risk entries |
| C-21..C-26 | Gate audit, coverage CLOSED BY column, R-NN back-fill in RISK fields, coverage table columns, Phase 10 numbered list, dedicated Phase 9b |
| C-29..C-37 | Amendment table PHASE column, finding format, [R-NN pending] placeholder, dual-domain enumeration, "Do not compute P×I" prohibition, Domain N— labels, transition notation, P×I in back-fill, per-column R-NN attribution |
| C-38..C-41 | T-37/T-38 CONDITION cells carry inline exemplars and correct-format prescriptions |
| C-42..C-44 | T-40 CONDITION: exemplar (C-42), prescription (C-43), explanation-of-abstractness (C-44) |
| C-45..C-47 | T-42 CONDITION: exemplar (C-45), prescription (C-46), explanation-of-abstractness (C-47) |
| C-48 | T-46 CONDITION: inline exemplar of Part-1-only T-42 state |
| C-49 | T-47 CONDITION: inline exemplar of exemplar-without-explanation T-42 state |
| C-50 | T-46 exemplar includes `[END — no Part 2 label and no Part 2 content present]` terminal marker |
| C-51 | T-47 exemplar includes `(C-45 PASS)` pass-state annotation |

### Cascade invariants (v21)

| Root | Cascades to |
|------|-------------|
| C-42 FAIL | C-44 FAIL |
| C-45 FAIL | C-46, C-47, C-48, C-49, C-50, C-51 FAIL |
| C-48 FAIL | C-50 FAIL |
| C-49 FAIL | C-51 FAIL |
| C-48 PASS | does not guarantee C-50 PASS |
| C-49 PASS | does not guarantee C-51 PASS |
| C-50 ⊥ C-51 | mutually independent |

**Live demonstrations from R20:** V-01 = C-50 FAIL + C-51 PASS; V-02 = C-50 PASS + C-51 FAIL.
Both asymmetric independence cases confirmed in a single round.
