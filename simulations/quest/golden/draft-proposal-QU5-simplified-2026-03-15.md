# draft-proposal — QU5 Simplified Golden
**Date:** 2026-03-15
**Source:** draft-proposal-variate-R20-2026-03-15.md (V-02 base + V-01 golden T-47)
**Rubric:** v21 · Denominator /44 · Criteria C-01..C-51 · Triggers T-01..T-51

---

## Simplification Report

**Original word count (complete golden, pre-simplification):** ~1903
**Simplified word count:** ~1521
**Reduction:** ~382 words (~20%)
**All essential criteria preserved:** YES (44/44 under v21)

### What was removed and why

| # | Removed element | Words | Criterion impact |
|---|----------------|-------|-----------------|
| 1 | INERTIA FRAMING CONVENTION — verbose definition shortened | 17 | None — concept restated inline throughout phases |
| 2 | PHASE 0 — "See AMENDMENT TABLE SPECIFICATION below for key trigger conditions." | 9 | None — navigational hint, not specification |
| 3 | PHASE 3 — "(inertia risk: technical debt accumulation, opportunity cost, competitive erosion)" | 9 | None — example categories only; no criterion tests them |
| 4 | PHASE 4 — "it is the incumbent state that wins by default; active options must demonstrate sufficient advantage over the inertia competitor to justify action." | 28 | None — restates the inertia convention; no criterion tests this Phase 4 phrasing |
| 5 | PHASE 4b — "Do not express inertia risks as P×I scores only — the R-NN pairing and canonical bracket structure are both required." | 20 | None — no criterion tests this prohibition; canonical form already shown in template |
| 6 | PHASE 6 — "Phase 4b present with R-NN citations in canonical bracket form" prerequisite check | 9 | None — absent from R-02 and C-20 pass conditions |
| 7 | PHASE 9 — "State explicitly whether the recommendation beats the inertia competitor and on what basis." | 16 | None — no criterion (E-04 or C-XX) tests for this comparison language |
| 8 | T-40 Part 1 — "; the reader cannot verify what the deficient form looks like without constructing it from the description alone." | 17 | None — duplicate justification; C-44 satisfied by preceding "this is abstract because…" |
| 9 | T-40 Part 2 — "— sufficient to show what a deficient T-38 CONDITION entry actually looks like, making the deficiency concrete and independently verifiable." | 21 | None — annotation on the example; C-43 satisfied by the example itself |
| 10 | T-42 Part 1 — "; a reviewer assessing T-38 cannot determine what a deficient T-38 CONDITION entry looks like from this category description alone." | 19 | None — duplicate justification; C-47 satisfied by preceding "abstract because it names the Domain 2 format requirement as a category…" |
| 11 | T-45 — full example directive ("exemplar must quote or paraphrase…e.g., '...' — this is abstract because…") | 42 | None — no criterion tests T-45's own CONDITION content; C-45 tests T-42's CONDITION |
| 12 | T-46 — trailing sentence "— T-42 CONDITION with Part 1 labeled and fully present but no Part 2 label and no correct-format prescription fires T-46." | 22 | None — explanatory summary; C-48/C-50 test T-46's exemplar content, not this trailing restatement |
| 13 | T-47 — "Part 1 must include both the quoted T-40 form AND an explanation of what property makes it abstract." clause before exemplar | 20 | None — intent already in trigger condition phrase; exemplar that follows demonstrates the standard |
| 14 | T-47 — trailing "no language stating it names the Domain 2 format requirement without showing what a deficient T-38 CONDITION looks like." | 20 | None — duplicate of "no explanation of why that T-40 form is abstract"; C-49/C-51 test exemplar presence and (C-45 PASS) annotation |
| 15 | T-48 — elaboration block (abstract T-46 example + "T-46 CONDITION must quote or closely paraphrase…") | 58 | None — no criterion tests T-48's own CONDITION; C-48 tests T-46's CONDITION; T-48 need only exist (C-24) with PHASE value (C-29) |
| 16 | T-49 — elaboration block (abstract T-47 example + "T-47 CONDITION must quote or closely paraphrase…") | 55 | None — same logic as T-48; C-49 tests T-47's CONDITION |

**Cascade safety check:** All 16 removals are from trigger CONDITION text whose content is tested by no rubric criterion. The structurally-tested cells — T-40 CONDITION (C-42, C-43, C-44), T-42 CONDITION (C-45, C-46, C-47), T-46 CONDITION (C-48, C-50), T-47 CONDITION (C-49, C-51) — retain all content required by their respective criteria.

---

## Simplified Prompt Body

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

## Criteria Preservation Verification

| Criterion | Satisfied by | Status |
|-----------|-------------|--------|
| E-01 | PHASE 0 role sequence declaration | PASS |
| E-02 | PHASE 1 + PHASE 2 options with 4 anatomy fields | PASS |
| E-03 | PHASE 4 comparison matrix with 7 dimensions (5 PM + 2 Architect) | PASS |
| E-04 | PHASE 9 recommendation with rationale + qualifying conditions | PASS |
| R-01 | PHASE 3 risk register with P, I, P×I, project-specific anchors | PASS |
| R-02 | PHASE 6 prerequisites check | PASS |
| R-03 | PHASE 10 four-step finalization | PASS |
| C-01..C-07 | Mandatory C-tier: all phase lifecycle, dual-role, scout ref, amendment table | PASS |
| C-08 | PHASE 8 assumption register | PASS |
| C-16 | PHASE 3 project-specific scoring anchors | PASS |
| C-22 | PHASE 7 CLOSED BY column directive | PASS |
| C-23 | T-23 trigger + PHASE 9b back-fill | PASS |
| C-24 | T-24 PRE-DOCUMENT fires if row count != 51; PHASE 0 declares T-01..T-51 | PASS |
| C-25 | PHASE 10 numbered 4-step list | PASS |
| C-26 | PHASE 9b dedicated phase + T-26 trigger | PASS |
| C-29 | All T-XX rows carry PHASE value | PASS |
| C-31 | PHASE 2 [R-NN pending] placeholder directive + T-31 | PASS |
| C-32 | PHASE 9b dual-domain enumeration (Domain 1 + Domain 2) + T-32 | PASS |
| C-33 | PHASE 2 "Do not compute P×I" prohibition + T-33 | PASS |
| C-34 | PHASE 9b "Domain 1 —" / "Domain 2 —" labels + T-34 | PASS |
| C-35 | PHASE 9b transition notation [R-NN pending] → [...] + T-35 | PASS |
| C-36 | PHASE 9b P×I in back-fill + T-36 | PASS |
| C-37 | PHASE 9b per-column R-NN attribution + T-37 | PASS |
| C-38 | T-40 CONDITION Part 1 carries inline exemplar of deficient T-38 form | PASS |
| C-39 | T-40 CONDITION Part 2 carries correct-format prescription | PASS |
| C-40 | T-42 CONDITION Part 1 carries inline exemplar of deficient T-40 form | PASS |
| C-41 | T-42 CONDITION Part 2 carries correct-format prescription | PASS |
| C-42 | T-40 CONDITION carries inline exemplar (Part 1) | PASS |
| C-43 | T-40 CONDITION carries correct-format prescription (Part 2) | PASS |
| C-44 | T-40 CONDITION Part 1 includes explanation-of-abstractness | PASS |
| C-45 | T-42 CONDITION carries inline exemplar (Part 1) | PASS |
| C-46 | T-42 CONDITION carries correct-format prescription (Part 2) | PASS |
| C-47 | T-42 CONDITION Part 1 includes explanation-of-abstractness | PASS |
| C-48 | T-46 CONDITION carries inline exemplar of Part-1-only T-42 state | PASS |
| C-49 | T-47 CONDITION carries inline exemplar of exemplar-without-explanation T-42 state | PASS |
| C-50 | T-46 CONDITION exemplar includes `[END — no Part 2 label and no Part 2 content present]` terminal marker | PASS |
| C-51 | T-47 CONDITION exemplar includes `(C-45 PASS)` pass-state annotation | PASS |
