```markdown
# listen-support Quest Rubric — v10

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 8 essential/recommended criteria |
| v2 | Added C-11 (Phase as card field), C-12 (Fallback-grounded severity), C-13 (Mid-output verification block) from R1 excellence signals. Max: 115 pts |
| v3 | Added C-14 (Phase+Title coexistence), C-15 (Temporal adoption window severity), C-16 (Prior-tool coverage in verification) from R2 excellence signals. Max: 130 pts |
| v4 | Added C-17 (Phase-as-severity-key declaration), C-18 (Gate minimum correct at ≥7) from R3 excellence signals. Max: 140 pts |
| v5 | Added C-19 (TABLE CHECK halt instruction), C-20 (Gap analysis coverage verification block) from R4 excellence signals. Max: 150 pts |
| v6 | Added C-21 (Evidence-to-gap traceability with orphan-gap check), C-22 (Prohibited sentinel language on consequence fields) from R5 excellence signals. Max: 160 pts |
| v7 | Added C-23 (Belt-and-suspenders criterion satisfaction), C-24 (Materialized-view traceability instruction), C-25 (Criterion-ID-named final verification spine) from R6 excellence signals. Max: 175 pts |
| v8 | Added C-26 (Self-referential criterion enforcement), C-27 (Spine-as-sole-suspenders declaration) from R7 excellence signals. Max: 185 pts |
| v9 | Added C-28 (Compliance Contract spine-criterion anchoring), C-29 (Triple self-referential mechanism stack) from R8 excellence signals. Max: 195 pts |
| v10 | Added C-30 (Spine-row self-enforcement imperative), C-31 (Dual-load CONTRACT implementation), C-32 (Three-timing enforcement coverage) from R9 excellence signals. Max: 210 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×24) | 5 | 2 | 0 |

**Max composite:** 210 pts  
**Golden gate:** all_essential_pass = TRUE AND composite ≥ 80

PARTIAL on any Essential criterion = all_essential_pass FALSE (Golden blocked regardless of composite).

---

## Essential Criteria (12 pts each, max 60)

### C-01 — Title field on card
Each ticket card includes `Title: [descriptive subject line]` as a named field. A ticket ID (`Ticket T-NN`) does not satisfy this criterion — Title must be a human-readable subject line that summarizes the feedback. A heading of the form `## T-NN — {Title}` does not satisfy this criterion; the title must appear as a discrete named field in the card body.

**PASS:** Every card has a `Title:` field with a descriptive value.  
**PARTIAL:** Title absent on some cards, or ticket ID used in place of subject line, or title embedded in heading only.  
**FAIL:** No title field on any card.

---

### C-02 — Controlled vocabulary declared and enforced
Phase, Category, Volume, and Severity use controlled vocabularies declared in the planning table. The model enforces values — no free-form variants accepted in scored fields.

**PASS:** Vocabulary table present; all card values match declared options.  
**PARTIAL:** Vocabulary declared but not consistently enforced.  
**FAIL:** Free-form values used; no vocabulary declaration.

---

### C-03 — First-person voice throughout
All ticket bodies written in first person. No role titles in body text. The voice constraint is stated explicitly in the prompt (e.g., "Write as me — first person throughout. No role titles in body text.").

**PASS:** All bodies pass first-person check; constraint is stated in prompt.  
**PARTIAL:** Constraint stated but some bodies break first-person or include role titles.  
**FAIL:** Constraint absent or systematically violated.

---

### C-04 — Gap analysis with three named sections
A gap analysis step (distinct from ticket generation) produces three sections: Doc Gaps, Design Gaps, Operational Gaps. Each section must reference ≥1 named artifact.

**PASS:** All three sections present, each with ≥1 named artifact.  
**PARTIAL:** Sections present but one or more is empty or unnamed.  
**FAIL:** Gap analysis absent or fewer than three sections.

---

### C-05 — Ticket body actionable and feedback-grounded
Each ticket body contains a specific, actionable description traceable to a source feedback item. Body text is not a paraphrase of the title. No placeholder language (e.g., "TBD", "see above", "N/A") appears in a scored body field.

**PASS:** All ticket bodies are actionable, traceable to a feedback item, and free of placeholder language.  
**PARTIAL:** Most bodies meet the criterion; one or more contain placeholder language or are non-actionable paraphrases of the title.  
**FAIL:** Bodies systematically absent, placeholder-filled, or not traceable to feedback items.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — Severity classification grounded in impact
Severity values are assigned based on stated impact criteria, not guessed or applied uniformly. The prompt includes a severity rubric or the classification logic is derivable from the planning table.

**PASS:** Severity on all tickets traceable to an impact criterion; classification logic declared.  
**PARTIAL:** Severity assigned but classification logic absent or inconsistently applied.  
**FAIL:** Severity uniform, absent, or arbitrary.

---

### C-07 — Category accuracy across ticket set
Each ticket is assigned to a category from the controlled vocabulary that correctly classifies the feedback type. Miscategorized tickets are absent.

**PASS:** All ticket categories match feedback type; no miscategorization detectable.  
**PARTIAL:** Most tickets correctly categorized; isolated exceptions present.  
**FAIL:** Category field absent, free-form, or systematically wrong.

---

### C-08 — Planning table present before ticket generation
A planning table (or equivalent structured output) declaring the controlled vocabulary and ticket plan appears before any ticket card is generated. The table is not post-hoc.

**PASS:** Planning table present; appears before first ticket card; vocabulary in table matches card values.  
**PARTIAL:** Planning table present but appears after ticket generation, or vocabulary in table does not match card values.  
**FAIL:** No planning table; ticket generation begins without a declared plan.

---

## Aspirational Criteria (5 pts each, max 120)

### C-09 — Artifact naming in gap analysis
Each gap named in the gap analysis references a specific artifact (document name, section, or deliverable) rather than a general category. Vague references (e.g., "the documentation", "existing tooling") do not satisfy this criterion.

**PASS:** Every gap cites a named artifact.  
**PARTIAL:** Most gaps cite named artifacts; one or more cite categories only.  
**FAIL:** Gap analysis present but no artifacts named.

---

### C-10 — No required field left blank
Every scored field (Title, Phase, Category, Volume, Severity) contains a non-null, non-placeholder value on every ticket card. The prompt does not leave resolution of required fields to the reader.

**PASS:** All required fields populated on all cards.  
**PARTIAL:** One or more required fields blank or placeholder on some cards.  
**FAIL:** Required fields systematically unpopulated.

---

### C-11 — Phase as named card field
Each ticket card includes `Phase: [value]` as a discrete named field in the card body. A phase reference embedded only in a heading or table row does not satisfy this criterion.

**PASS:** Every card has a `Phase:` field with a value from the controlled vocabulary.  
**PARTIAL:** Phase present on some cards but absent on others, or embedded in heading only.  
**FAIL:** Phase field absent from all cards.

---

### C-12 — Fallback-grounded severity assignment
When a feedback item lacks explicit severity cues, the prompt specifies a fallback rule (e.g., "default to Medium when impact is unquantified"). Severity is never left to unconstrained model judgment.

**PASS:** Fallback severity rule declared; every ticket severity traceable to either an explicit cue or the fallback rule.  
**PARTIAL:** Fallback rule present but not applied consistently; some tickets have unexplained severity values.  
**FAIL:** No fallback rule; severity assigned without declared logic when cues are absent.

---

### C-13 — Mid-output verification block
The prompt includes an explicit verification step after ticket generation and before final output. The verification block names the fields to check and declares the halt condition (e.g., "stop and fix before continuing if any required field is blank").

**PASS:** Verification block present; names fields; declares halt condition.  
**PARTIAL:** Verification mentioned but field list or halt condition absent.  
**FAIL:** No verification block in prompt.

---

### C-14 — Phase and Title coexistence on every card
Both `Phase:` and `Title:` fields are present on the same card. Neither field's presence substitutes for the other.

**PASS:** Every card has both Phase and Title as discrete named fields.  
**PARTIAL:** Both fields declared in vocabulary but one is absent on some cards.  
**FAIL:** One or both fields absent on all cards, or one field substitutes for the other.

---

### C-15 — Severity scoped to adoption-window temporality
For feedback items describing adoption barriers, severity reflects the time-sensitivity of the adoption window (e.g., High severity for blockers present during the active rollout window). Severity is not assessed as if the feature were in steady-state.

**PASS:** Adoption-window temporality declared in severity rubric or planning table; High-severity adoption blockers correctly scoped to window.  
**PARTIAL:** Temporality referenced but not operationalized in severity values.  
**FAIL:** Severity assessed without adoption-window scoping.

---

### C-16 — Prior-tool coverage in verification block
The verification block explicitly checks whether any ticket covers behavior that existed in the prior tool and is now missing or degraded. "Prior tool coverage" is named as a check item.

**PASS:** Verification block includes a prior-tool coverage check by name.  
**PARTIAL:** Verification block present but prior-tool coverage check absent.  
**FAIL:** No verification block, or prior-tool coverage not mentioned anywhere.

---

### C-17 — Phase declared as severity-key dimension
The planning table or severity rubric declares Phase as an input dimension to severity assignment (e.g., "Severity is higher during Rollout phase than Post-GA phase for equivalent friction"). Phase is not a decoration — it modulates severity.

**PASS:** Phase-as-severity-key rule present in planning table or severity rubric; at least one ticket demonstrates phase-modulated severity.  
**PARTIAL:** Phase-as-severity-key referenced in text but not operationalized in a table row or severity rubric.  
**FAIL:** Severity assigned independently of Phase.

---

### C-18 — Gate minimum: ≥7 tickets correct before proceeding
The prompt includes a gate instruction: a minimum of 7 tickets must pass all required-field checks before the output is accepted. The gate halts output if the threshold is not met.

**PASS:** Gate instruction present; threshold ≥7 stated; halt condition declared.  
**PARTIAL:** Gate present but threshold is below 7 or halt condition is advisory only.  
**FAIL:** No gate instruction.

---

### C-19 — TABLE CHECK halt instruction
The prompt includes a `TABLE CHECK` step (or equivalent named step) that explicitly halts ticket generation if the planning table is incomplete or invalid. The halt is mandatory, not advisory.

**PASS:** `TABLE CHECK` step named; halt condition stated; step appears before ticket generation.  
**PARTIAL:** Table check step present but not named as a halt; advisory language only.  
**FAIL:** No table check step.

---

### C-20 — Gap analysis coverage verification block
A verification step after gap analysis confirms that each of the three gap sections (Doc Gaps, Design Gaps, Operational Gaps) contains at least one named artifact. The step names the three sections explicitly and declares a halt if any section is empty.

**PASS:** Coverage verification block present; all three sections named; halt condition stated.  
**PARTIAL:** Coverage verification present but section list incomplete or halt condition absent.  
**FAIL:** No coverage verification after gap analysis.

---

### C-21 — Evidence-to-gap traceability with orphan-gap check
Each gap in the gap analysis is traceable to a specific evidence item from the feedback. An orphan-gap check verifies that no gap is asserted without a traceable evidence item.

**PASS:** Each gap cites evidence; orphan-gap check step present in prompt; zero orphan gaps in output.  
**PARTIAL:** Most gaps cite evidence; orphan-gap check present but one or more gaps are untraceable.  
**FAIL:** Gaps asserted without evidence; no orphan-gap check.

---

### C-22 — Prohibited sentinel language on consequence fields
The prompt explicitly prohibits sentinel values (e.g., "None", "N/A", "TBD") on consequence-bearing fields (Severity, Phase, Volume). Prohibition is stated as an instruction, not as a recommendation.

**PASS:** Prohibition stated for each named consequence field; no sentinel values appear in output.  
**PARTIAL:** Prohibition stated but not for all consequence fields, or sentinel values appear on some cards.  
**FAIL:** No prohibition on sentinel language; sentinel values present.

---

### C-23 — Belt-and-suspenders criterion satisfaction
For each essential criterion, the prompt implements two independent mechanisms to ensure satisfaction (belt + suspenders). No essential criterion relies on a single mechanism for enforcement.

**PASS:** Two distinct enforcement mechanisms traceable for each essential criterion.  
**PARTIAL:** Belt-and-suspenders pattern applied to some but not all essential criteria.  
**FAIL:** Essential criteria rely on single-mechanism enforcement throughout.

---

### C-24 — Materialized-view traceability instruction
The prompt includes an instruction to produce a traceability view (table or list) mapping each ticket to its source feedback item and gap. The view is a materialized artifact in the output, not an implicit claim.

**PASS:** Traceability view instruction present; output includes a table or list mapping tickets to sources.  
**PARTIAL:** Traceability instruction present but output contains only a partial mapping.  
**FAIL:** No traceability view instruction; mapping absent or implicit only.

---

### C-25 — Criterion-ID-named final verification spine
The final verification step uses a spine structure that names each criterion by ID (e.g., `C-01`, `C-02`) and records a PASS/PARTIAL/FAIL judgment per criterion. The spine covers all essential criteria at minimum.

**PASS:** Final verification spine present; criterion IDs named; PASS/PARTIAL/FAIL recorded for each essential criterion.  
**PARTIAL:** Spine present but criterion IDs absent, or some essential criteria not covered.  
**FAIL:** No criterion-ID-named spine in final verification.

---

### C-26 — Self-referential criterion enforcement
The spine includes a row that verifies the spine itself (i.e., the spine confirms its own completeness and correctness). The self-referential row is labeled and its PASS condition is stated.

**PASS:** Spine contains a self-referential row; row label present; PASS condition stated.  
**PARTIAL:** Self-referential concept mentioned but not implemented as a named row in the spine.  
**FAIL:** No self-referential row in spine.

---

### C-27 — Spine-as-sole-suspenders declaration
The prompt includes an explicit declaration that the final verification spine is the sole gate — no other section's claim of completeness substitutes for the spine's verdict. The declaration is stated as a constraint, not as a recommendation.

**PASS:** SOLE GATE declaration present; explicitly names the spine as the sole gate; no other completeness claim substitutes.  
**PARTIAL:** Sole-gate concept present but stated as advisory, or not explicitly naming the spine as the exclusive gate.  
**FAIL:** No sole-gate declaration; completeness claims scattered across sections.

---

### C-28 — Compliance Contract spine-criterion anchoring
The prompt includes a COMPLIANCE CONTRACT section that explicitly anchors `[C-26: BELT]` and `[C-27: BELT]` (or their named equivalents), making spine self-verification and sole-gate properties contractually obligated rather than structurally incidental. The obligation chain is traceable: CONTRACT → SOLE GATE DECLARATION → spine row.

**PASS:** COMPLIANCE CONTRACT section present; anchors `[C-26: BELT]` and `[C-27: BELT]` by name; obligation chain CONTRACT → SOLE GATE DECLARATION → spine row is traceable.  
**PARTIAL:** COMPLIANCE CONTRACT present but BELT anchors absent, or obligation chain breaks at one step.  
**FAIL:** No COMPLIANCE CONTRACT section; spine properties are structurally incidental rather than contractually obligated.

---

### C-29 — Triple self-referential mechanism stack
All three self-referential mechanisms are present simultaneously: (1) a pre-check block before any body is generated, (2) an inline `Required:` condition imperative inside the spine row instruction, and (3) a CONTRACT anchor (`[C-26: BELT]` / `[C-27: BELT]`). No single mechanism alone satisfies this criterion.

**PASS:** All three mechanisms present: pre-check block (before body generation) + inline `Required:` in spine row instruction + CONTRACT anchor. Each mechanism independently verifiable.  
**PARTIAL:** Two of three mechanisms present. One gap in the triple stack.  
**FAIL:** Fewer than two mechanisms present.

---

### C-30 — Spine-row self-enforcement imperative
The spine row instruction contains an inline `Required:` condition imperative (or equivalent named obligation) that makes criterion compliance visible and verifiable at the point of definition. The spine row is self-contained with respect to its obligation: a scorer reading only the spine row can identify the enforcement requirement without consulting any external section (CONTRACT, DECLARATION, or otherwise).

**PASS:** Spine row instruction contains an inline named imperative (e.g., `Required: [condition]`) identifying the obligation. Row is self-enforcing — no external lookup required to understand the compliance requirement at the scoring step.  
**PARTIAL:** Spine row references an obligation but does not name it inline — resolution requires consulting another section to identify what is required.  
**FAIL:** Spine row contains no self-enforcement mechanism; obligation traceable only through external CONTRACT or DECLARATION sections.

---

### C-31 — Dual-load CONTRACT implementation
The COMPLIANCE CONTRACT anchor implementation is structurally load-bearing for both C-28 (contractual obligation of spine properties) and C-29 mechanism 3 (CONTRACT anchor in the triple stack) simultaneously. No independent, separate implementation step is required to satisfy both criteria — the CONTRACT section is shared infrastructure for both.

**PASS:** CONTRACT section satisfies C-28 and simultaneously supplies C-29 mechanism 3 from the same implementation. Both criteria traceable to the same CONTRACT anchor. No redundant or separate implementation needed.  
**PARTIAL:** CONTRACT anchor satisfies one criterion but requires an independent implementation step to satisfy the other. The two criteria are not composited onto shared infrastructure.  
**FAIL:** CONTRACT anchor is not load-bearing for both criteria; implementation is duplicated, absent, or addresses only one criterion.

---

### C-32 — Three-timing enforcement coverage
The enforcement mechanisms cover all three distinct timings in the output pipeline: (1) design time via CONTRACT anchor, (2) pre-generation time via pre-check block before body generation, and (3) scoring time via inline `Required:` imperative in the spine row instruction. All three timings are covered simultaneously by distinct named mechanisms, closing every gap in the pipeline.

**PASS:** All three enforcement timings covered: CONTRACT anchor (design) + pre-check block (pre-generation) + inline `Required:` (scoring). Each timing is traceable to a distinct named mechanism in the prompt.  
**PARTIAL:** Two of three enforcement timings covered. One phase of the output pipeline has no enforcement mechanism.  
**FAIL:** Fewer than two enforcement timings covered; enforcement is concentrated in a single phase of the output pipeline.
```
