**v8 written** to `simulations/quest/rubrics/specify-abstract-rubric-v8-2026-03-19.md`.

---

## What changed from v7

**Three new criteria (6 pts added):**

| ID | Name | Source |
|----|------|--------|
| C-28 | Self-diagnosis exclusion constraint enumerated with positive search space | R7 E-04 — V-02/V-04/V-05: "must be OUTSIDE" constraint + *Why* block naming where to look |
| C-29 | Bridge integration format change accompanied by structural rationale | R7 E-03 — V-01/V-04: quoted-extract instruction + pre-fill impossibility argument |
| C-30 | Inertia checklist closes with explicit aggregation gate | R7 E-02 — V-05: per-path confirmations + "All three paths closed. Proceed." |

**Six criteria retired (6 pts freed):**

C-11, C-12, C-14, C-15, C-17, C-18 — all universally passing in R7, each absorbed by a newer structural criterion. Retirement pattern is consistent with v7 (C-09, C-16): expectation, not achievement.

**Chain structure preserved:**
- Self-diagnosis: C-24 floor → C-25 ceiling → **C-28 ceiling+**
- Bridge lifecycle: C-23 floor → C-26 ceiling → **C-29 ceiling+**
- Inertia lifecycle: C-27 floor → **C-30 ceiling**

**No current R7 variation satisfies all three new criteria.** V-05 satisfies C-28 and C-30; V-01/V-04 satisfy C-29. V-06 synthesis is the target.
onale"). The instruction to use verbatim quoted text rather than Y/N in the Pass 3 integration column must be accompanied by an explicit explanation of the structural asymmetry: a Y/N column can be prefilled in the same cognitive pass as Pass 1 and Pass 2, before the merge has been executed; a verbatim extract from merged prose cannot exist before the merge does. The rationale need not be lengthy -- one sentence stating the pre-fill impossibility argument is sufficient. A format instruction without a structural rationale can be satisfied by mechanical compliance; a rationale instruction enforces understanding of why the format change closes the pre-fill window. Source: R7 V-01/V-04 signal, E-03 excellence pattern.

**C-30 -- Inertia checklist closes with explicit aggregation gate** (2 pts, format)
C-27 is the floor ("canonical terms + per-path confirmations"); C-30 is the ceiling ("per-path confirmations + named aggregation gate"). After the three per-path canonical-term confirmation lines (Signal-skip confirmed / Nominal gap framing confirmed / Non-trivial gaming confirmed), the block must close with an explicit aggregation line that converts the three individual acknowledgments into a single named gate event -- "All three paths closed. Proceed." or a structurally equivalent formulation. The aggregation line is not redundant: three separate acknowledgments without a gate event allow the model to proceed implicitly after the last confirmation; a named aggregation gate requires an active closure signal. The gate phrase must be its own line or sentence, distinct from the third per-path confirmation. Source: R7 V-05 signal, E-02 excellence pattern.

---

## Point Redistribution (Aspirational stays at 20, total stays at 100)

| Criterion | Change      | Reason |
|-----------|-------------|--------|
| C-11      | retired     | *Why:* blocks are universal across all R7 variations -- R7 scorecard: "Multiple *Why:* blocks throughout Phase 2" in all five. C-28 is the new positive-search-space ceiling; C-11 as "at least two constraints with rationale" is expectation, not achievement. |
| C-12      | retired     | Bridge planning fully absorbed by C-20 (constrained vocabulary) and C-21 (coupling verified before bridge). C-12 has no remaining independent scoring function. |
| C-14      | retired     | Gap-first ordering universally passing since R4 and now baseline. C-04 (essential) covers the structural constraint; C-14 ordering preference is expectation. |
| C-15      | retired     | "Do not self-correct as you write" is a universal baseline implementation detail in all R7 variations. Coverage-only draft discipline is no longer a distinguishing behavior. |
| C-17      | retired     | All six Phase 2 sections carry *Why:* rationale in all R7 variations. With C-11 also retired and C-28 as the new ceiling, C-17 has no remaining independent scoring function. |
| C-18      | retired     | Phase 0 paper-type declaration present in all five R7 variations. C-19 is the structurally sufficient ceiling; C-18 as the declaration floor is expectation. |
| C-28      | +2 pts      | New (self-diagnosis exclusion constraint enumerated with positive search space). |
| C-29      | +2 pts      | New (bridge integration format change accompanied by structural rationale). |
| C-30      | +2 pts      | New (inertia checklist closes with explicit aggregation gate). |

**C-28 extends C-25**: C-25 requires the exclusion constraint; C-28 requires the constraint plus an enumerated positive search space. All C-28-passing variations pass C-25; not all C-25-passing variations will pass C-28 once variations separate on this axis.

**C-29 extends C-26**: C-26 requires quoted extract in the integration column; C-29 requires the format change plus an explicit structural rationale. The rationale converts format compliance into demonstrated understanding of the post-merge window problem.

**C-30 extends C-27**: C-27 requires canonical terms plus per-path confirmations; C-30 requires the full per-path checklist plus a named aggregation gate. V-03 passes C-27 without the gate; V-05 passes both.

**Aspirational subtotal**: Remains 20 pts. Total remains 100.

---

## Criteria Summary Table

| ID   | Name                                                                     | Weight       | Category    | Points |
|------|--------------------------------------------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present                                               | essential    | correctness | 10     |
| C-02 | Word count within target                                                 | essential    | correctness | 10     |
| C-03 | Artifact written to correct path                                         | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal                                              | essential    | correctness | 10     |
| C-05 | Signal acquisition executed                                              | essential    | behavior    | 10     |
| C-06 | Result section is quantified                                             | recommended  | depth       | 10     |
| C-07 | Amendment pass produces three distinct                                   | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly                                        | recommended  | correctness | 10     |
| C-10 | Abstract reads as a single coherent paragraph                            | aspirational | format      | 1      |
| C-13 | Amendment non-triviality guard applied                                   | aspirational | depth       | 1      |
| C-19 | Paper type governs all six section registers                             | aspirational | depth       | 1      |
| C-20 | Semantic bridge type constrained vocabulary                              | aspirational | format      | 1      |
| C-21 | Section coupling verified before bridge                                  | aspirational | depth       | 1      |
| C-22 | Coupling revision uses structured directive format                       | aspirational | depth       | 1      |
| C-23 | Bridge integration verified post-merge                                   | aspirational | format      | 1      |
| C-24 | Self-diagnosis amendment targets weakest element                         | aspirational | depth       | 1      |
| C-25 | Self-diagnosis names weakness outside fixed categories                   | aspirational | depth       | 2      |
| C-26 | Bridge integration column cites actual merged prose                      | aspirational | format      | 2      |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0           | aspirational | format      | 2      |
| C-28 | Self-diagnosis exclusion constraint enumerated with positive search space | aspirational | depth       | 2      |
| C-29 | Bridge integration format change accompanied by structural rationale     | aspirational | format      | 2      |
| C-30 | Inertia checklist closes with explicit aggregation gate                  | aspirational | format      | 2      |

Aspirational check: 1+1+1+1+1+1+1+1+2+2+2+2+2+2 = **20**

---

## Essential Criteria (50 points total)

### C-01 -- Six-Part Structure Present
- **Weight**: essential
- **Category**: correctness
- **Text**: The abstract contains all six named sections: Background, Gap, Claim, Method, Result, Implication. Each section is present and contains at least one sentence. The structure is non-negotiable: missing any section produces an incomplete abstract that cannot be evaluated on content criteria.
- **Pass condition**: All six section labels appear in the draft output, each followed by at least one substantive sentence.

### C-02 -- Word Count Within Target
- **Weight**: essential
- **Category**: correctness
- **Text**: The merged abstract falls within the target word count range (150-250 words by default, or the journal-specified limit if --for journal:<name> is provided). Abstracts outside range must include an explicit compression or expansion attempt with before/after counts.
- **Pass condition**: Word count is in range, or if over-range the output includes an explicit compression attempt with before/after counts.

### C-03 -- Artifact Written to Correct Path
- **Weight**: essential
- **Category**: behavior
- **Text**: Output file is written to signals/specify/abstract/{topic}-abstract-{date}.md (or --output path/ if flag provided). Frontmatter includes: skill: specify-abstract, topic, date, word_count, and journal (if specified).
- **Pass condition**: File exists at the expected path and frontmatter contains all required fields.

### C-04 -- Gap Framed as Gap, Not Goal
- **Weight**: essential
- **Category**: correctness
- **Text**: The Gap section names what is unresolved or unknown (e.g. "X remains unresolved"), not a research goal (e.g. "we aimed to study X"). Goal framing implies the paper might have failed; gap framing states a fact about the state of the field.
- **Pass condition**: Gap sentence does not use goal-framing phrases ("we aimed", "we sought to", "this paper investigates"). It makes a claim about the state of the field.

### C-05 -- Signal Acquisition Executed
- **Weight**: essential
- **Category**: behavior
- **Text**: Phase 1 is executed: the skill globs signals/**/{topic}-* and reads available artifacts (paper draft, specify-spec, discover-hypothesis) before writing the abstract. The abstract reflects extracted signals, not generic filler.
- **Pass condition**: Output shows evidence of signal-informed content. Glob results are visible or the artifact content is clearly grounded in topic signals.

---

## Recommended Criteria (30 points total)

### C-06 -- Result Section Is Quantified
- **Weight**: recommended
- **Category**: depth
- **Text**: The Result section includes at least one quantified finding -- effect size, percentage, count, or qualitative strength descriptor -- not just "we found improvements."
- **Pass condition**: Result sentence contains a number, percentage, or explicit qualitative strength claim ("strong", "substantial", "no significant difference").

### C-07 -- Amendment Pass Produces Three Distinct Improvements
- **Weight**: recommended
- **Category**: depth
- **Text**: Phase 5 produces three labeled amendments: (1) Gap sharpened to name a specific unresolved question, (2) Result quantified if not already, (3) Implication tightened to one concrete enabling action. Each amendment is distinct and non-trivial. A restatement of the prior sentence is not an amendment.
- **Pass condition**: All three amendment slots are filled with substantive revisions. At least two of the three result in visible textual changes from the pre-amendment version.

### C-08 -- Journal Variant Applied Correctly
- **Weight**: recommended
- **Category**: correctness
- **Text**: If --for journal:<name> is specified, the abstract register matches the journal requirements (Nature/Science: broad significance lead + societal implication; PNAS: effect size in result; cognitive-science: theoretical advance in implication; arxiv: technical precision, 300-word limit).
- **Pass condition**: When a journal flag is present, the abstract text shows at least two structural adjustments matching the journal profile. Pass vacuously if no journal flag provided.

---

## Aspirational Criteria (20 points total)

### C-10 -- Abstract Reads as a Single Coherent Paragraph
- **Weight**: aspirational
- **Category**: format
- **Source**: R2 excellence signal. Reduced 4->2 pts in v6; reduced 2->1 pt in v7 -- C-26 (quoted bridge evidence) and C-25 (categorical self-diagnosis) now structurally enforce what C-10 measured editorially. C-10 is the coherence floor.
- **Text**: The merged abstract (Phase 3) reads as prose, not as six labeled sentences stapled together. Transitions are natural and the paragraph has narrative flow from context through finding to significance.
- **Pass condition**: No section labels appear in the merged paragraph. Adjacent sentences have logical connectives or implicit flow. The paragraph would not be rejected on stylistic grounds by a journal editor.

### C-13 -- Amendment Non-Triviality Guard Applied
- **Weight**: aspirational
- **Category**: depth
- **Source**: R1 excellence signal E-03 (anti-trivial-amendment-guard). Universally passing R3 and R4 -- reduced 2->1 pt in v5, now baseline.
- **Text**: Phase 5 explicitly guards against low-effort compliance by stating that a restatement of the prior sentence is not an amendment. Before/after comparison is shown for each amendment slot.
- **Pass condition**: Phase 5 output includes before/after text for at least 2 of the 3 amendments. At least 2 of the 3 produce a visible textual change -- not a paraphrase of the same sentence.

### C-19 -- Paper Type Governs All Six Section Registers
- **Weight**: aspirational
- **Category**: depth
- **Source**: R4 excellence signal E-01 (paper-type-as-planning-parameter). C-18 (declaration floor) retired in v8; C-19 is now the sufficient criterion for paper-type compliance. Reduced 2->1 pt in v6 -- universally passing all R5 variations, now baseline.
- **Text**: The paper type declared at Phase 0 propagates into all six section registers: Background epistemic register, Gap framing language, Method scope, Implication form (empirical: "these findings enable"; theoretical: "this framework predicts"). C-19 captures whether the declaration actually governs the draft.
- **Pass condition**: At least four of the six sections show register differentiation traceable to the declared paper type. Mixed registers without intentional justification fail.

### C-20 -- Semantic Bridge Type Constrained Vocabulary
- **Weight**: aspirational
- **Category**: format
- **Source**: R4 excellence signal E-02. C-12 (bridges planned floor) retired in v8; C-20 was the type-first ceiling. Reduced 2->1 pt in v6 -- C-23 creates a new ceiling; C-20 remains the type-planning floor.
- **Text**: Bridge composition uses a five-term constrained vocabulary (contrast / causation / resolution / escalation / application) as a Type column. The type is assigned before the bridge phrase is composed. A consecutive-type constraint (no more than two consecutive boundaries of the same type) prevents formulaic labeling.
- **Pass condition**: Bridge table includes a Type column with values from the five-term vocabulary. At least two distinct types appear across the five boundaries. Bridge phrases appear after the type assignment, not before.

### C-21 -- Section Coupling Verified Before Bridge Composition
- **Weight**: aspirational
- **Category**: depth
- **Source**: R4 excellence signal E-03. Reduced 2->1 pt in v6 -- C-22 captures the structured-directive ceiling; C-21 remains the "coupling verified" floor.
- **Text**: After all six sections are drafted and before bridge composition begins, Phase 2c assigns a COUPLED / WEAK / REVISE status at each of the five section boundaries. Any WEAK or REVISE triggers a section-level revision before proceeding.
- **Pass condition**: Output includes evidence of a boundary-status pass at each of the five boundaries positioned after drafting and before bridge composition. At least one boundary is WEAK or REVISE and addressed, OR all five are COUPLED with brief rationale. A table with no rationale does not pass.

### C-22 -- Coupling Revision Uses Structured Directive Format
- **Weight**: aspirational
- **Category**: depth
- **Source**: R5 excellence signal V-01. C-21 is the "coupling verified" floor; C-22 is the "structured and auditable" ceiling. Reduced 2->1 pt in v7 -- universally passing R6; pre-implemented by V-05 R5 synthesis base.
- **Text**: When Phase 2c identifies a WEAK or REVISE boundary, the revision directive follows a structured format: Boundary / Deficient-section / Deficiency / Before / After / Re-verify -- parallel to Phase 5 amendment format. Open-ended notes ("revise for alignment") cannot be audited; structured directives can.
- **Pass condition**: When at least one WEAK or REVISE is found, the output includes a structured directive for each flagged boundary with all six fields populated. Pass vacuously if all boundaries are COUPLED.

### C-23 -- Bridge Integration Verified Post-Merge
- **Weight**: aspirational
- **Category**: format
- **Source**: R5 excellence signal V-02. Reduced 2->1 pt in v7 -- universally passing R6; C-26 (quoted evidence) is the new ceiling; C-23 remains the integration-status floor.
- **Text**: A Phase 3b verification step is positioned after merge and before journal variant. It produces a five-row table confirming each Phase 2b bridge phrase appears in the merged prose. Any N triggers paragraph revision. Stock connectors ("however", "additionally", "furthermore", "moreover", "therefore") are not bridges; they convey no semantic relationship.
- **Pass condition**: Output includes a Phase 3b table with one row per boundary, each containing the planned bridge phrase and a Y / N integration status. At least one N must trigger visible paragraph revision, OR all five Y with bridge phrase quoted from merged prose.

### C-24 -- Self-Diagnosis Amendment Targets Weakest Element
- **Weight**: aspirational
- **Category**: depth
- **Source**: R5 excellence signal V-03. Reduced 2->1 pt in v7 -- universally passing R6; C-25 (categorical novelty) is the new ceiling; C-24 remains the "differs from prior targets" floor.
- **Text**: A self-diagnosis amendment is added to Phase 5. The model reads the post-amendment abstract and identifies the single weakest remaining element. The diagnosed weakness must differ from all prior amendment targets (Gap, Result, Implication, prose coherence) and be stated as a specific claim. A generic self-compliment fails.
- **Pass condition**: Phase 5 includes a self-diagnosis slot. The output names a specific remaining weakness as a one-sentence claim that differs from the prior fixed targets. Before/After shows a substantive change traceable to the diagnosed weakness.

### C-25 -- Self-Diagnosis Names Weakness Outside Fixed Amendment Categories
- **Weight**: aspirational
- **Category**: depth
- **Source**: R6 excellence signal V-01 (diagnosis-first audit trail). C-24 is the "differs from prior targets" floor; C-25 is the "categorically novel diagnosis" ceiling.
- **Text**: The self-diagnosis amendment identifies a weakness whose category is entirely outside the four fixed amendment slots (Gap sharpening, Result quantification, Implication tightening, prose coherence). The diagnosed weakness must name a specific element type not covered by any of the four named categories. When self-diagnosis runs in Amendment 1 position (diagnosis-first variant), the model reads the unimproved post-merge abstract with all weaknesses present; naming a non-standard weakness before targeted fixes narrow attention is causally significant. When in Amendment 5 position (standard variant), it identifies what survives four targeted passes. In both positions the criterion fires identically.
- **Pass condition**: The self-diagnosis amendment names a weakness whose category is distinct from Gap, Result, Implication, and prose coherence. The named weakness is traceable to a specific sentence or element type not addressed by the other four amendment targets. A diagnosis that names "the Gap is still vague" (Gap category) after a Gap amendment fails; a diagnosis that names "the Background uses observational language inconsistent with the theoretical register" (Background register category) passes.

### C-26 -- Bridge Integration Column Cites Actual Merged Prose
- **Weight**: aspirational
- **Category**: format
- **Source**: R6 excellence signal V-03 (unified card rote-fill risk). C-23 is the "Y/N integration status" floor; C-26 is the "quoted evidence" ceiling.
- **Text**: The Phase 3b bridge integration table elevates its integration column from Y/N status to evidence: each row contains a verbatim extract (3-10 words) from the merged paragraph, in quotation marks, showing the bridge phrase or its recognizable variant as it actually appears in the merged prose. A Y checkbox without quoted text cannot confirm Phase 3 was completed before the table was filled in. Completing all columns in a single pre-merge pass is structurally prevented when the integration column requires post-merge text that cannot exist before the merge.
- **Pass condition**: The Phase 3b table integration column contains quoted text from the merged paragraph for at least four of the five boundaries. Each quoted extract is in quotation marks and visibly differs from the planned bridge phrase column (reflecting actual merged wording). A Y/N column without quoted extracts does not satisfy C-26 even if C-23 is satisfied.

### C-27 -- Inertia Declaration Names Canonical Cheap Paths Before Phase 0
- **Weight**: aspirational
- **Category**: format
- **Source**: R6 excellence signal V-02 (inertia commitment device). No prior criterion equivalent -- structurally new pre-Phase 0 lifecycle position.
- **Text**: A pre-Phase 0 inertia declaration block names at least two of the three canonical cheap paths and requires explicit model confirmation before proceeding to Phase 0: (1) signal-skip -- running without executing the Phase 1 glob; (2) nominal gap framing -- writing a research goal instead of a field-state gap; (3) non-trivial gaming -- using cosmetic Before/After edits that pass the guard format without substantive improvement. The block must appear before Phase 0 and must require a per-path confirmation for each named path. C-05/C-04/C-13 are the execution-point scoring floors; C-27 is the pre-execution commitment device above those floors.
- **Pass condition**: Output includes a pre-Phase 0 block that explicitly names at least two canonical cheap paths (signal-skip, nominal gap framing, non-trivial gaming) with a per-path confirmation for each named path. A general statement ("I will execute all phases diligently") does not satisfy C-27. The block must be positioned before any Phase 0 content.

### C-28 -- Self-Diagnosis Exclusion Constraint Enumerated with Positive Search Space
- **Weight**: aspirational
- **Category**: depth
- **Source**: R7 excellence signal V-02/V-04/V-05 (E-04 pattern, positive-search-space enumeration). C-25 is the "exclusion constraint present" floor; C-28 is the "constraint + enumerated positive search space" ceiling.
- **Text**: The Amendment 1 exclusion constraint must be accompanied by a *Why this constraint matters* block that names at least two specific non-fixed weakness categories the model should diagnose instead. The block converts a prohibition into a diagnostic target. Example non-fixed categories: Background epistemic register inconsistency, Claim scope or specificity gap, Method framing relative to claim strength, contribution incrementality framing. Any two distinct non-fixed category names satisfy the enumeration requirement. Without enumeration, a model that passes C-25 has been told where not to look; a model that passes C-28 has been told where to look.
- **Pass condition**: The Amendment 1 self-diagnosis instruction includes an explicit block or note naming at least two non-fixed weakness categories as positive diagnostic targets. The block must accompany the exclusion constraint, not appear in a different section. Zero or one named category does not satisfy C-28 even if the exclusion constraint is present.

### C-29 -- Bridge Integration Format Change Accompanied by Structural Rationale
- **Weight**: aspirational
- **Category**: format
- **Source**: R7 excellence signal V-01/V-04 (E-03 pattern, pre-fill impossibility argument). C-26 is the "quoted extract required" floor; C-29 is the "format change + structural rationale" ceiling.
- **Text**: The instruction to use verbatim quoted text rather than Y/N in the Pass 3 integration column must be accompanied by a structural rationale block explaining why the format change closes the pre-fill window. The core argument: a Y/N column can be prefilled in the same cognitive pass as Pass 1 and Pass 2, before the merge has been executed; a verbatim extract from merged prose cannot exist before the merge does. The rationale converts format compliance into demonstrated understanding of the structural problem the format solves. A format instruction without rationale can be satisfied by mechanical compliance; a rationale instruction enforces the cognitive model behind the constraint.
- **Pass condition**: The Pass 3 table instruction for quoted extracts includes at least one sentence stating the pre-fill impossibility argument -- that verbatim text from merged prose cannot be written before the merge is executed. The rationale must accompany the format instruction, not appear as a general comment elsewhere. A format instruction with no rationale fails C-29 even if C-26 is satisfied.

### C-30 -- Inertia Checklist Closes with Explicit Aggregation Gate
- **Weight**: aspirational
- **Category**: format
- **Source**: R7 excellence signal V-05 (E-02 pattern, aggregation gate). C-27 is the "canonical terms + per-path confirmations" floor; C-30 is the "per-path confirmations + named aggregation gate" ceiling.
- **Text**: After the three per-path canonical-term confirmation lines (one per cheap path: Signal-skip / Nominal gap framing / Non-trivial gaming), the pre-Phase 0 inertia block must close with an explicit aggregation gate line that names all three paths as jointly cleared -- "All three paths closed. Proceed." or a structurally equivalent formulation. The aggregation gate converts three individual acknowledgments into a single named gate event: the model cannot proceed silently after the last per-path confirmation; it must generate an active closure signal. The gate line must be its own sentence, distinct from the third per-path confirmation. A prompt whose per-path confirmations trail directly into Phase 0 without a gate line fails C-30 even if C-27 is satisfied.
- **Pass condition**: The pre-Phase 0 inertia block includes all three per-path confirmations followed by a distinct aggregation line naming all three paths as cleared before proceeding. The aggregation line is a separate sentence or line item, not a suffix to the third confirmation. A prompt without an aggregation gate does not satisfy C-30 even if all per-path confirmations are present.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                         |
|--------------|-----------------|--------|----------------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                                    |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                      |
| Aspirational | C-10 to C-30    | 20     | Separates good from excellent. C-25 through C-30 are the ceiling layer.               |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v7

| Change              | Detail |
|---------------------|--------|
| C-11 retired        | *Why:* blocks are universal across all R7 variations -- R7 scorecard: "Multiple *Why:* blocks throughout Phase 2" in all five. C-28 (enumerated positive search space) is the new Why-block ceiling. Expectation, not achievement. |
| C-12 retired        | Bridge planning absorbed by C-20 (constrained vocabulary) and C-21 (coupling verified before bridge). C-12 has no remaining independent scoring function. |
| C-14 retired        | Gap-first ordering universally passing since R4 and now baseline. C-04 (essential) covers the structural constraint; C-14 ordering preference is expectation. |
| C-15 retired        | "Do not self-correct as you write" is a universal baseline implementation detail in all R7 variations. Coverage-only draft discipline is no longer a distinguishing behavior. |
| C-17 retired        | All six Phase 2 sections carry *Why:* rationale in all R7 variations. With C-11 also retired and C-28 as the new ceiling, C-17 has no remaining independent scoring function. |
| C-18 retired        | Phase 0 paper-type declaration present in all five R7 variations. C-19 is the structurally sufficient ceiling; C-18 as the declaration floor is expectation. C-19 updated to note C-18 retirement. |
| C-19 updated        | Note added: C-18 (declaration floor) retired in v8; C-19 is now the sufficient criterion for paper-type compliance. |
| C-27 updated        | Text updated: per-path confirmation requirement made explicit (surfaced by C-30 design; V-03 vs V-05 distinction). C-30 is the aggregation-gate ceiling above C-27's per-path floor. |
| C-28 added          | Self-diagnosis exclusion constraint enumerated with positive search space -- from R7 V-02/V-04/V-05 signal (E-04). 2 pts. Positive-diagnostic-target ceiling above C-25 exclusion-constraint floor. |
| C-29 added          | Bridge integration format change accompanied by structural rationale -- from R7 V-01/V-04 signal (E-03). 2 pts. Pre-fill impossibility ceiling above C-26 quoted-extract floor. |
| C-30 added          | Inertia checklist closes with explicit aggregation gate -- from R7 V-05 signal (E-02). 2 pts. Named gate ceiling above C-27 per-path-confirmation floor. |
| Tier description    | Updated to reflect C-10 to C-30 aspirational range (C-11, C-12, C-14, C-15, C-17, C-18 retired). |
| Aspirational subtotal | Remains 20 pts. Total remains 100. |

---

**Design notes:**

- **Six criteria retired across v3-v8**: C-09 (v7), C-16 (v7), C-11/C-12/C-14/C-15/C-17/C-18 (v8). Pattern: retirement when universally passing for 2+ rounds AND a structurally stronger ceiling criterion covers the same behavior.
- **Floor/ceiling chain integrity**: C-21->C-22 (coupling), C-20->C-23->C-26->C-29 (bridge lifecycle), C-07->C-24->C-25->C-28 (self-diagnosis), C-27->C-30 (inertia lifecycle). Each chain has a 1-pt floor (universally passing) and a 2-pt ceiling (newly differentiating).
- **C-28/C-29/C-30 structural logic**: All three share the same v8 pattern -- a v7 criterion established the behavior (what to do); the v8 ceiling requires the model to also close or explain the behavior. C-28: constraint + enumerated positive space (where to look). C-29: format + structural rationale (why the format works). C-30: per-path confirmations + aggregation gate (active closure signal).
- **V-06 synthesis target**: A next-generation synthesis variation would combine all three: per-path canonical terms + aggregation gate (C-30), quoted extracts + pre-fill impossibility rationale (C-29), exclusion constraint + enumerated positive search space (C-28). V-05 R7 already satisfies C-28 and C-30; V-01/V-04 satisfy C-29. No single R7 variation satisfies all three.
