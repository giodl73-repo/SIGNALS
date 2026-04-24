Reading the scorecard for V-05 excellence signals — the differentiating mechanisms that pushed beyond what C-26 and C-27 already capture:

1. **C-28 signal**: V-05 adds `[C-26: BELT]` and `[C-27: BELT]` anchors in the COMPLIANCE CONTRACT, making spine self-verification properties *contractually obligated* rather than structurally incidental. The obligation chain (`CONTRACT → SOLE GATE DECLARATION → spine row`) is explicitly traceable.

2. **C-29 signal**: V-05 stacks all three C-26 mechanisms simultaneously (pre-check block + inline Required condition imperative + CONTRACT anchor), eliminating every single point of self-referential failure.

---

```markdown
# listen-support Quest Rubric — v9

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

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×21) | 5 | 2 | 0 |

**Max composite:** 195 pts  
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

### C-05 — Minimum ticket count enforced with structural gate
A TABLE CHECK block appears after the planning table and before ticket generation. The block verifies that declared phase or layer minimums sum to ≥7. An explicit halt instruction names the next step and blocks progression until the check passes (e.g., "Do not proceed to STEP 4 until this check shows YES"). The minimum must be declared structurally, not as an advisory instruction.

**PASS:** TABLE CHECK block present with halt instruction naming the blocked step; minimums sum to ≥7; gate is structural not advisory.  
**PARTIAL:** TABLE CHECK or halt instruction present but minimum is < 7, or enforcement is advisory language without a named gate.  
**FAIL:** No TABLE CHECK, no halt instruction, or no minimum declared.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — Severity calibration grounded in phase
A Phase Map Table or equivalent structure grounds severity assignment to phase. The normative severity range per phase is declared as an inference rule before ticket generation begins — not as a post-hoc description.

**PASS:** Phase Map Table present with expected severity range per phase; declared before ticket inventory; cards comply.  
**PARTIAL:** Severity grounded to phase but declared after ticket generation, or compliance is inconsistent.  
**FAIL:** No phase-to-severity grounding; severity assigned ad hoc.

---

### C-07 — Volume differentiated by ceiling constraint
A CONSTRAINT MANIFEST or equivalent structure caps high-volume tickets (e.g., ≤ 50% of total). The Phase Map Table characterizes volume per phase. Volume field values vary across cards.

**PASS:** High-volume ceiling declared and enforced; Phase Map Table shows volume character per phase; card volume values vary.  
**PARTIAL:** Ceiling declared but not enforced, or volume undifferentiated across all phases.  
**FAIL:** No volume constraint; all cards carry same volume or field is absent.

---

### C-08 — Persona-authentic body register
The VOCABULARY MANIFEST or equivalent structure declares role-specific register descriptions per phase. A PERFORMANCE MODE DECLARATION provides per-role backstory or voice anchor. Card bodies reflect role and phase register — an SRE in Phase 1 writes differently from a PM in Phase 3.

**PASS:** Register descriptions declared per role and phase; PERFORMANCE MODE DECLARATION present; card bodies reflect differentiated register.  
**PARTIAL:** Register described but not differentiated by role or phase; or PERFORMANCE MODE DECLARATION absent.  
**FAIL:** No register guidance; all bodies share undifferentiated voice.

---

## Aspirational Criteria (5 pts each, max 105)

### C-09 — Theme-first generation
A theme declaration step precedes ticket inventory generation. A cross-ticket pattern table appears after ticket generation, surfacing recurring themes across the set.

**PASS:** Theme declaration in prompt precedes STEP generating inventory; cross-ticket pattern table present post-generation.  
**PARTIAL:** Theme mentioned but not structurally declared before inventory, or cross-ticket table absent.  
**FAIL:** No theme-first structure; tickets generated without declared theme.

---

### C-10 — Resolution paths for high-severity tickets
A resolution paths table appears after ticket generation covering all high-volume or P0/P1 tickets. Each entry maps a ticket to a concrete resolution path.

**PASS:** Resolution paths table present; all high-volume or P0/P1 tickets have a mapped resolution path.  
**PARTIAL:** Table present but coverage is incomplete; some qualifying tickets lack a resolution path.  
**FAIL:** No resolution paths table.

---

### C-11 — Phase as named card field
Every ticket card includes a discrete `Phase:` field with value of the form `Phase N (day X–Y)`. Phase embedded only in a heading does not satisfy this criterion.

**PASS:** Every card has a `Phase:` field with day-range value.  
**PARTIAL:** Phase present on some cards, or day range absent, or phase embedded in heading only.  
**FAIL:** No `Phase:` field on any card.

---

### C-12 — Fallback-grounded severity
A Role-Phase Cross-Matrix or equivalent structure provides a normative severity per role-phase intersection. Cards reference or comply with this matrix as a fallback when context is ambiguous.

**PASS:** Cross-matrix present; card severities traceable to matrix values; matrix precedes ticket generation.  
**PARTIAL:** Matrix present but cards deviate without stated justification.  
**FAIL:** No cross-matrix; severity assigned without role-phase grounding.

---

### C-13 — Mid-output verification block
At least one verification block appears between major generation steps (e.g., between planning table and ticket generation). The block is structural — a named gate with checkable conditions — not an advisory reminder.

**PASS:** At least one structural verification block between generation steps; conditions are checkable.  
**PARTIAL:** Verification present but advisory only; or placed after all generation with no mid-output gate.  
**FAIL:** No mid-output verification block.

---

### C-14 — Phase-differentiated body register in vocabulary
The VOCABULARY MANIFEST or equivalent structure explicitly differentiates register by phase (e.g., P1 = acute crisis language, P2 = adaptation language, P3 = steady-state language). The CONSTRAINT MANIFEST or equivalent checks per-phase register compliance.

**PASS:** Vocabulary rows differentiated by phase register; constraint manifest includes per-phase register compliance check.  
**PARTIAL:** Register differentiated by phase in vocabulary but not verified in constraint manifest.  
**FAIL:** No phase-differentiated register; single register for all phases.

---

### C-15 — Temporal adoption window mapped to severity
The Phase Map Table explicitly maps each phase to a temporal adoption window (e.g., day 0–30, day 31–60, day 61–90) and declares the severity range for that window. The mapping appears as an explicit column, not implied from phase names.

**PASS:** Phase Map Table has a temporal window column and a severity range column; both present for each phase.  
**PARTIAL:** Window or severity range present but not both as explicit columns.  
**FAIL:** No temporal window-to-severity mapping.

---

### C-16 — Prior-tool coverage in verification
The VOCABULARY MANIFEST includes a migration-surprise register covering prior-tool expectations (e.g., `VM-Cxx-P1`). The VERIFICATION MANIFEST checks that migration-surprise tickets trace to this register.

**PASS:** Migration-surprise register present in VOCABULARY MANIFEST; VERIFICATION MANIFEST includes traceability check for prior-tool coverage.  
**PARTIAL:** Register present but VERIFICATION MANIFEST does not check traceability, or traceability is declared but not enforced.  
**FAIL:** No migration-surprise register; prior-tool coverage unverified.

---

### C-17 — Phase-as-severity-key declaration
A Phase Map Table with an "Expected severity range" column appears before the ticket inventory step. The table is framed as an inference rule: given phase, derive severity. This is a forward declaration, not a retrospective summary.

**PASS:** Phase Map Table with severity range column precedes ticket inventory; framed as an inference rule.  
**PARTIAL:** Table present but placed after inventory, or severity range column absent.  
**FAIL:** No Phase Map Table with severity inference rule.

---

### C-18 — Gate minimum correct at ≥7
The declared minimums in the structural gate (TABLE CHECK or equivalent) sum to ≥7 when all role or phase minimums are added together.

**PASS:** Declared minimums sum to ≥7; arithmetic is correct.  
**PARTIAL:** Minimums declared but sum to < 7; or arithmetic error results in incorrect total.  
**FAIL:** No declared minimums; gate minimum absent or uncalculated.

---

### C-19 — TABLE CHECK halt instruction names the blocked step
The TABLE CHECK halt instruction names the next step by identifier (e.g., "Do not proceed to STEP 6 until this check shows YES"). An instruction that names only an action ("revise before continuing") without naming the blocked step does not satisfy this criterion.

**PASS:** Halt instruction names the blocked step by number or identifier.  
**PARTIAL:** Halt instruction names the blocked action but not the step number; or a step number is present but no "do not proceed" language.  
**FAIL:** No halt instruction; TABLE CHECK is advisory only.

---

### C-20 — VM Row ID annotation in ## headline
The COMPLIANCE CONTRACT or equivalent structure prohibits VM Row ID annotation on any subline. The `*(VM: VM-xxx-P#)*` annotation appears inline on the `##` headline only. The VERIFICATION MANIFEST checks headline annotation counts.

**PASS:** CONTRACT prohibition on subline annotation present; VERIFICATION MANIFEST checks ## headline annotation count; cards comply.  
**PARTIAL:** Annotation present on headlines but CONTRACT prohibition absent; or VERIFICATION MANIFEST check absent.  
**FAIL:** Annotation on sublines; or no annotation at all; or prohibition and verification both absent.

---

### C-21 — Five-item gate with item (e) inter-role register check
The VOCABULARY PRE-FLIGHT GATE contains exactly five items (a)–(e). Item (e) requires inter-role register differentiation with a VM-Row-ID citation demonstrating that at least two roles have distinct register descriptions.

**PASS:** Gate has items (a)–(e); item (e) requires inter-role differentiation with VM-Row-ID citation; gate is structural.  
**PARTIAL:** Five items present but item (e) absent or does not require VM-Row-ID citation; or gate has fewer than five items.  
**FAIL:** No five-item gate; or gate has no inter-role register check.

---

### C-22 — Prohibited sentinel language on consequence fields
The COMPLIANCE CONTRACT or equivalent structure explicitly prohibits generic sentinel language (e.g., "this may cause issues", "could be a problem") in consequence fields such as adoption cost and operational gap entries. Structural forms require non-generic content by design.

**PASS:** CONTRACT prohibition on sentinel language present and names the prohibited forms; structural fields require specificity by form.  
**PARTIAL:** Prohibition present but does not name specific prohibited forms; or structural forms allow generic content.  
**FAIL:** No prohibition; sentinel language appears unchecked.

---

### C-23 — Belt-and-suspenders criterion satisfaction
At least two independent locations in the prompt each independently cite the governing criterion or contract for a given structural requirement. If either citation is removed, the other still enforces the requirement.

**PASS:** At least two independent citations (e.g., in STEP 3B, STEP 4, and VERIFICATION MANIFEST) each reference the governing criterion by ID or contract name; both citations are independently sufficient.  
**PARTIAL:** Multiple mentions present but one is a forward reference that depends on the other; or only one independent citation.  
**FAIL:** Single citation; no belt-and-suspenders coverage.

---

### C-24 — Materialized-view traceability instruction
The prompt establishes a three-level traceability chain: source vocabulary (VOCABULARY MANIFEST) → commitment table → verification (VERIFICATION MANIFEST). The gate checks traceability in both directions: source-to-commitment and commitment-to-card.

**PASS:** Three-level chain explicit; gate items check both directions (source → commitment and commitment → card).  
**PARTIAL:** Three-level chain present but gate checks only one direction.  
**FAIL:** No three-level traceability chain; or chain present but not verified in gate.

---

### C-25 — Criterion-ID-named final verification spine
The final verification block is a table or structured list with one row per criterion, each row named by criterion ID (C-NN). The spine covers all aspirational and recommended criteria that apply to this prompt. Required/Actual/Pass? columns or equivalent are present for each row.

**PASS:** Final verification block is a per-criterion spine named by C-ID; Required/Actual/Pass? columns present; all applicable criteria covered.  
**PARTIAL:** Spine present but missing criterion IDs on some rows; or coverage is incomplete.  
**FAIL:** No per-criterion spine; final verification is a checklist or prose only.

---

### C-26 — Self-referential criterion enforcement
The verification spine contains a row for C-26 itself. The row's Required condition forces self-grading to occur only after all other rows are complete — either via a SPINE COMPLETENESS PRE-CHECK block that enumerates all C-IDs before filling begins, or via an inline imperative in the Required condition column that directs the model to count rows before writing the Actual value.

**PASS:** C-26 row present in spine; Required condition contains an explicit self-grading instruction (pre-check block or inline imperative) that prevents premature completion.  
**PARTIAL:** C-26 row present but no self-grading instruction in Required condition; row is structurally present but not functionally self-referential.  
**FAIL:** C-26 row absent from spine.

---

### C-27 — Spine-as-sole-suspenders declaration
A SOLE GATE DECLARATION block appears before the verification spine. The block must establish all four properties: (1) any PRE-SPINE PROPERTY TRACE or equivalent precursor block is explicitly demoted to a non-gate trace; (2) the spine governs in case of disagreement with any other verification block; (3) no other check substitutes for the spine verdict; (4) the declaration names the spine as the exclusive gate.

**PASS:** SOLE GATE DECLARATION block present before spine; all four properties (demotion, governance, non-substitution, exclusive naming) explicitly stated.  
**PARTIAL:** Declaration block present but one or more of the four properties absent or implied rather than stated.  
**FAIL:** No SOLE GATE DECLARATION block; spine present but not declared sole gate.

---

### C-28 — Compliance Contract spine-criterion anchoring
The COMPLIANCE CONTRACT or equivalent governing structure contains explicit named anchors for the spine's self-verification criteria — specifically for C-26 (self-referential enforcement) and C-27 (sole-gate declaration), named by criterion ID (e.g., `[C-26: BELT]`, `[C-27: BELT]`). These anchors make the spine's verification properties contractually obligated: a model that satisfies the CONTRACT cannot bypass the spine's self-verification mechanisms. The obligation chain — CONTRACT anchor → declaration/instruction → spine row — must be explicitly traceable.

**PASS:** COMPLIANCE CONTRACT contains named anchors for both C-26 and C-27 by criterion ID; obligation chain from CONTRACT to spine row is traceable for each.  
**PARTIAL:** One anchor present but not both; or anchors present but do not name criteria by ID; or anchor present but obligation chain is not traceable to the spine row.  
**FAIL:** No CONTRACT anchors for spine self-verification criteria.

---

### C-29 — Triple self-referential mechanism stack
All three C-26 satisfaction mechanisms are present simultaneously, with no single point of self-referential failure: (1) a SPINE COMPLETENESS PRE-CHECK block that enumerates all C-IDs and directs C-26 to be filled last; (2) an inline imperative in the Required condition column of C-26's spine row that directs the model to count rows before writing the Actual value; (3) a COMPLIANCE CONTRACT anchor (`[C-26: BELT]` or equivalent) that makes the self-referential enforcement contractually obligated. If any single mechanism is removed, the other two independently enforce self-referential grading.

**PASS:** All three mechanisms present: SPINE COMPLETENESS PRE-CHECK block + inline Required condition imperative + CONTRACT anchor. Each is independently sufficient.  
**PARTIAL:** Exactly two of the three mechanisms present.  
**FAIL:** Fewer than two mechanisms present; single-mechanism coverage only.
```
