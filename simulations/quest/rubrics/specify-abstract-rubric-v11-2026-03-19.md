**v11 written** to `simulations/quest/rubrics/specify-abstract-rubric-v11-2026-03-19.md`.

---

**Two criteria extracted from R11 scorecard and promoted to aspirational ceilings:**

| ID | Name | Extends | Pts | Source |
|----|------|---------|-----|--------|
| C-36 | Sub-phase canonical naming in phase sequence lock | C-33 | 2 | R11 V-01 |
| C-37 | Weakness-specific per-row reasoning in per-excluded-category verification | C-35 | 2 | R11 V-02 |

**Two criteria retired** (universally passing R11): C-33, C-35.

**Point math**: −4 (retirements) + 4 (additions) = 0. Aspirational stays at 20. Total stays at 100.

**Chain updates:**
- Inertia: C-27 -> ~~C-33~~ -> **C-36** (sequence lock now requires sub-phase gate rationale naming the Phase 3 -> Phase 3b dependency as the basis for C-26/C-29)
- Self-diagnosis exclusion: C-24 -> ~~C-35~~ -> **C-37** (per-category rows now require weakness-specific sentences, closing the "confirmed" template shortcut)
- Self-diagnosis search: C-24 -> **C-34** (no new ceiling in v11)

**V-07 synthesis target**: V-01 passes C-36, fails C-37. V-02 passes C-37, fails C-36. The R12 synthesis variation combines both.
 synthesis variation for R12 would combine sub-phase canonical naming (C-36) with weakness-specific per-row reasoning (C-37) while retaining the asymmetry argument (C-34).

---

**C-36 -- Sub-phase canonical naming in phase sequence lock** (2 pts, format)
C-27 is the "per-path confirmation" floor; C-33 is the "phase sequence lock" mid (retired in v11 -- universally passing all R11 variations); C-36 is the new ceiling ("sub-phase canonical naming with structural rationale block"). C-33 required the gate closure to enumerate the full phase sequence and declare it locked; C-36 requires that Phase 3 (merge) and Phase 3b (integration verification) be named as individually gated sub-phases with an explicit structural rationale block ("Why sub-phase canonical naming matters" or structurally equivalent) explaining the gate dependency. The rationale names the causal mechanism: Phase 3b (bridge integration verification) requires the merged paragraph as input; Phase 3b cannot be executed before Phase 3 completes; a model that treats Phase 3 and Phase 3b as a combined or unlabeled step retains the shortcut of filling the Phase 3b integration column before the merge has been executed -- the same pre-fill window that C-26 (quoted evidence) and C-29 (CAN/CANNOT asymmetry) were designed to close at the verification stage. Sub-phase canonical naming at the sequence lock stage closes this window at the commitment level: the model commits before Phase 0 that Phase 3b is a named sub-phase gate requiring Phase 3 output, making the pre-fill shortcut structurally blocked from the start rather than only detectable post-hoc. A sequence lock that lists Phase 3 and Phase 3b in order without sub-phase rationale satisfies the retired C-33 but not C-36. Source: R11 V-01, C-36 excellence pattern.

**C-37 -- Weakness-specific per-row reasoning in per-excluded-category verification** (2 pts, depth)
C-24 is the "diagnosis targets weakest element" floor; C-35 is the "per-excluded-category verification" mid (retired in v11 -- universally passing all R11 variations); C-37 is the new ceiling ("weakness-specific per-row reasoning"). C-35 required four rows with per-row reasoning explaining why the diagnosed weakness falls outside each fixed category; C-37 requires that each row's reasoning name the actual diagnosed weakness and state specifically why that weakness is not an instance of the category -- not a template parenthetical describing the category boundary with "[confirmed / explain if uncertain]". The distinction: a C-35-compliant row can be written as "Gap sharpening: N -- [the named weakness does not target the Gap sentence's specificity: confirmed]" using the category-description template; a C-37-compliant row requires "Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]" where the sentence is self-contained and weakness-grounded. A reader auditing a C-37-compliant row can verify the exclusion from the row alone, without cross-referencing the category label or trusting a template confirmation. The "confirmed" shortcut path closes the per-row form requirement (C-35) without actually reasoning about the specific weakness; C-37 closes this shortcut by requiring the weakness to be named and the per-row reason to be stated as a distinct sentence. A model that writes four N entries with template parenthetical plus "confirmed" satisfies the retired C-35 but not C-37. Source: R11 V-02, C-37 excellence pattern.

---

## Point Redistribution (Aspirational stays at 20, total stays at 100)

| Criterion | Change | Reason |
|-----------|--------|--------|
| C-33 | retired | Universally passing in all R11 variations. C-36 is the new sub-phase-canonical-naming ceiling; C-33 as "phase sequence lock" is expectation, not achievement. |
| C-35 | retired | Universally passing in all R11 variations. C-37 is the new weakness-specific-per-row ceiling; C-35 as "per-excluded-category verification" is expectation, not achievement. |
| C-36 | +2 pts | New (sub-phase canonical naming in phase sequence lock). |
| C-37 | +2 pts | New (weakness-specific per-row reasoning in per-excluded-category verification). |

**C-36 extends C-33**: C-33 required the gate closure to enumerate Phase 0 through Phase 5 in order and declare the sequence locked; C-36 requires Phase 3 and Phase 3b to be individually named as sub-phase gates with a structural rationale block explaining the Phase 3 -> Phase 3b dependency as the basis for C-26/C-29. All C-36-passing variations pass C-33 (retired); not all C-33-passing variations pass C-36 (V-05 R10 / V-02 R11 enumerate the phase sequence without sub-phase rationale).

**C-37 extends C-35**: C-35 required one row per fixed category with per-row reasoning stating why the diagnosed weakness falls outside that category; C-37 requires that reasoning to name the actual diagnosed weakness in a self-contained sentence rather than a template category-description with "[confirmed]". All C-37-passing variations pass C-35 (retired); not all C-35-passing variations pass C-37 (V-05 R10 / V-01 R11 use template parenthetical form satisfying C-35 without naming the weakness per-row).

**Aspirational subtotal**: Remains 20 pts. Total remains 100.

---

## Criteria Summary Table

| ID   | Name                                                                                        | Weight       | Category    | Points |
|------|---------------------------------------------------------------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present                                                                  | essential    | correctness | 10     |
| C-02 | Word count within target                                                                    | essential    | correctness | 10     |
| C-03 | Artifact written to correct path                                                            | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal                                                                 | essential    | correctness | 10     |
| C-05 | Signal acquisition executed                                                                 | essential    | behavior    | 10     |
| C-06 | Result section is quantified                                                                | recommended  | depth       | 10     |
| C-07 | Amendment pass produces three distinct                                                      | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly                                                           | recommended  | correctness | 10     |
| C-10 | Abstract reads as a single coherent paragraph                                               | aspirational | format      | 1      |
| C-13 | Amendment non-triviality guard applied                                                      | aspirational | depth       | 1      |
| C-19 | Paper type governs all six section registers                                                | aspirational | depth       | 1      |
| C-20 | Semantic bridge type constrained vocabulary                                                 | aspirational | format      | 1      |
| C-21 | Section coupling verified before bridge                                                     | aspirational | depth       | 1      |
| C-22 | Coupling revision uses structured directive format                                          | aspirational | depth       | 1      |
| C-23 | Bridge integration verified post-merge                                                      | aspirational | format      | 1      |
| C-24 | Self-diagnosis amendment targets weakest element                                            | aspirational | depth       | 1      |
| C-26 | Bridge integration column cites actual merged prose                                         | aspirational | format      | 2      |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0                              | aspirational | format      | 2      |
| C-29 | Bridge integration format change accompanied by structural rationale                        | aspirational | format      | 2      |
| C-34 | Positive search space block contains structural asymmetry argument                          | aspirational | depth       | 2      |
| C-36 | Sub-phase canonical naming in phase sequence lock                                           | aspirational | format      | 2      |
| C-37 | Weakness-specific per-row reasoning in per-excluded-category verification                   | aspirational | depth       | 2      |

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
- **Source**: R2 excellence signal. Reduced 4->2 pts in v6; reduced 2->1 pt in v7 -- C-26 (quoted bridge evidence) and C-25 (categorical self-diagnosis, retired v10) structurally enforce what C-10 measured editorially. C-10 is the coherence floor.
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
- **Source**: R5 excellence signal V-03. Reduced 2->1 pt in v7 -- universally passing R6; C-25 (categorical novelty, retired v10) was the mid in v7-v9; C-35 (per-excluded-category verification, retired v11) was the mid in v10; C-37 (weakness-specific per-row reasoning) is now the ceiling above C-24.
- **Text**: A self-diagnosis amendment is added to Phase 5. The model reads the post-amendment abstract and identifies the single weakest remaining element. The diagnosed weakness must differ from all prior amendment targets (Gap, Result, Implication, prose coherence) and be stated as a specific claim. A generic self-compliment fails.
- **Pass condition**: Phase 5 includes a self-diagnosis slot. The output names a specific remaining weakness as a one-sentence claim that differs from the prior fixed targets. Before/After shows a substantive change traceable to the diagnosed weakness.

### C-26 -- Bridge Integration Column Cites Actual Merged Prose
- **Weight**: aspirational
- **Category**: format
- **Source**: R6 excellence signal V-03 (unified card rote-fill risk). C-23 is the "Y/N integration status" floor; C-26 is the "quoted evidence" ceiling.
- **Text**: The Phase 3b bridge integration table elevates its integration column from Y/N status to evidence: each row contains a verbatim extract (3-10 words) from the merged paragraph, in quotation marks, showing the bridge phrase or its recognizable variant as it actually appears in the merged prose. A Y checkbox without quoted text cannot confirm Phase 3 was completed before the table was filled in. Completing all columns in a single pre-merge pass is structurally prevented when the integration column requires post-merge text that cannot exist before the merge.
- **Pass condition**: The Phase 3b table integration column contains quoted text from the merged paragraph for at least four of the five boundaries. Each quoted extract is in quotation marks and visibly differs from the planned bridge phrase column (reflecting actual merged wording). A Y/N column without quoted extracts does not satisfy C-26 even if C-23 is satisfied.

### C-27 -- Inertia Declaration Names Canonical Cheap Paths Before Phase 0
- **Weight**: aspirational
- **Category**: format
- **Source**: R6 excellence signal V-02 (inertia commitment device). No prior criterion equivalent -- structurally new pre-Phase 0 lifecycle position. C-32 (named-per-path gate) retired in v10; C-33 (phase sequence lock) retired in v11; C-36 (sub-phase canonical naming) is the new ceiling; C-27 remains the per-path confirmation floor.
- **Text**: A pre-Phase 0 inertia declaration block names at least two of the three canonical cheap paths and requires explicit model confirmation before proceeding to Phase 0: (1) signal-skip -- running without executing the Phase 1 glob; (2) nominal gap framing -- writing a research goal instead of a field-state gap; (3) non-trivial gaming -- using cosmetic Before/After edits that pass the guard format without substantive improvement. The block must appear before Phase 0 and must require a per-path confirmation for each named path. C-05/C-04/C-13 are the execution-point scoring floors; C-27 is the pre-execution commitment device above those floors.
- **Pass condition**: Output includes a pre-Phase 0 block that explicitly names at least two canonical cheap paths (signal-skip, nominal gap framing, non-trivial gaming) with a per-path confirmation for each named path. A general statement ("I will execute all phases diligently") does not satisfy C-27. The block must be positioned before any Phase 0 content.

### C-29 -- Bridge Integration Format Change Accompanied by Structural Rationale
- **Weight**: aspirational
- **Category**: format
- **Source**: R7 excellence signal V-01/V-04 (E-03 pattern, pre-fill impossibility argument). C-26 is the "quoted extract required" floor; C-29 is the "format change + structural rationale" ceiling. Pass condition tightened in v9: both CAN-side and CANNOT-side of the asymmetry must be stated (R8 V-02/V-03 revealed that CANNOT-only form is a subthreshold compliance path).
- **Text**: The instruction to use verbatim quoted text rather than Y/N in the Pass 3 integration column must be accompanied by a structural rationale block explaining why the format change closes the pre-fill window. The core argument requires both sides of the asymmetry: the CAN-side (a Y/N status can be assigned in the same cognitive pass as Pass 1 and Pass 2, before the merge has been executed -- filling in Y does not require the merged paragraph to exist) and the CANNOT-side (a verbatim extract from merged prose cannot be written before the merge is executed -- the text does not yet exist). A rationale that states only the CANNOT-side omits the contrast that makes the asymmetry structurally explicit; a reader who sees only the prohibition may comply mechanically without understanding the pre-fill window the format closes.
- **Pass condition**: The Pass 3 table instruction for quoted extracts includes the pre-fill impossibility argument with both sides of the asymmetry stated: (1) a Y/N status CAN be prefilled before the merge is executed, and (2) verbatim text from merged prose CANNOT be written before the merge exists. A rationale that states only one side does not satisfy C-29 even if C-26 is satisfied.

### C-34 -- Positive Search Space Block Contains Structural Asymmetry Argument
- **Weight**: aspirational
- **Category**: depth
- **Source**: R10 excellence signal V-02 (E-02 pattern, asymmetry argument). C-24 is the "diagnosis targets weakest element" floor; C-31 (dedicated named block) was the mid (retired v10 -- universally passing all R10 variations); C-34 is the ceiling ("structural asymmetry argument inside the dedicated block"). C-34 extends C-31: the dedicated block exists AND contains the causal argument. No new ceiling added in v11 -- C-34 remains the aspirational ceiling for the positive-search-space branch.
- **Text**: The `*Where to look instead -- positive search space:*` block (or structurally equivalent block) must contain not only an enumeration of non-fixed diagnostic targets but a structural argument explaining why the surviving weakness is asymmetrically more likely to appear outside the fixed amendment categories. The argument names the causal mechanism: the four fixed amendment categories are pre-committed correction targets that Amendments 2-4 address in a predictable pass; any weakness they address is already on a correction path before Amendment 1 executes; therefore, the self-diagnosis pass is structurally biased toward surfacing a weakness in a category that no fixed amendment targets. Enumerating positive search space targets (satisfies the retired C-31) identifies where to look; the asymmetry argument explains why looking there is structurally motivated -- the surviving weakness cannot be in a pre-committed category because those categories are being corrected regardless of what self-diagnosis finds. Without the asymmetry argument, the positive search space list is advisory; with it, the list is causally grounded.
- **Pass condition**: The positive search space block (dedicated, with its own label) contains a structural argument naming the pre-commitment mechanism as the reason for the asymmetric bias toward non-fixed categories. The argument must identify the four fixed categories as pre-committed targets and explain that the surviving weakness is therefore structurally more likely to appear outside them. A block that enumerates diagnostic targets without this causal argument does not satisfy C-34 even if C-31 (retired) would have been satisfied.

### C-36 -- Sub-Phase Canonical Naming in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R11 excellence signal V-01 (C-36 pattern, sub-phase canonical naming). C-27 is the "per-path confirmation" floor; C-33 (phase sequence lock) was the mid (retired v11 -- universally passing all R11 variations); C-36 is the new ceiling ("sub-phase canonical naming with structural rationale block"). C-36 extends C-33: the sequence lock enumerates sub-phases individually AND names Phase 3/Phase 3b as separately gated with explicit structural rationale.
- **Text**: The phase sequence lock (at the aggregation gate closure) must enumerate Phase 3 (merge) and Phase 3b (integration verification) as individually named sub-phase gates and include a structural rationale block ("*Why sub-phase canonical naming matters*" or structurally equivalent) explaining the Phase 3 -> Phase 3b gate dependency. The rationale names the causal mechanism: Phase 3b requires the merged paragraph as input; a model that treats Phase 3 and Phase 3b as a combined or unlabeled step retains the pre-fill shortcut of filling the Phase 3b integration column before the merge has been executed -- the same pre-fill window that C-26 and C-29 were designed to close at the verification stage. Sub-phase canonical naming at the sequence lock stage closes this window at the commitment level: the model commits before Phase 0 that Phase 3b is a named sub-phase gate requiring Phase 3 output, making the pre-fill shortcut structurally blocked from the start rather than only detectable post-hoc. A sequence lock that lists all phases including Phase 3 and Phase 3b without a sub-phase rationale block satisfies the retired C-33 but not C-36.
- **Pass condition**: The phase sequence lock includes Phase 3 and Phase 3b named as individually gated sub-phases AND a structural rationale block explaining the Phase 3 -> Phase 3b gate dependency in terms of the pre-fill window that C-26/C-29 close at the verification stage. The rationale must identify the causal mechanism (Phase 3b requires post-merge text as input) and state why sub-phase naming at the commitment stage closes the shortcut earlier than verification-stage guards alone. A sequence lock that enumerates the phases without this rationale block does not satisfy C-36 even if C-33 (retired) would have been satisfied.

### C-37 -- Weakness-Specific Per-Row Reasoning in Per-Excluded-Category Verification
- **Weight**: aspirational
- **Category**: depth
- **Source**: R11 excellence signal V-02 (C-37 pattern, weakness-specific per-row reasoning). C-24 is the "diagnosis targets weakest element" floor; C-35 (per-excluded-category verification) was the mid (retired v11 -- universally passing all R11 variations); C-37 is the new ceiling ("weakness-specific per-row reasoning"). C-37 extends C-35: the per-category rows exist AND each row names the actual diagnosed weakness in a self-contained sentence.
- **Text**: The per-excluded-category verification table must contain, in each row, a sentence that names the actual diagnosed weakness and states specifically why that weakness is not an instance of the category -- not a template parenthetical describing the category boundary with "[confirmed / explain if uncertain]". The distinction: a C-35-compliant row can be written as "Gap sharpening: N -- [the named weakness does not target the Gap sentence's specificity: confirmed]" using the category-description template; a C-37-compliant row requires "Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]" where the sentence is self-contained and weakness-grounded. A reader auditing a C-37-compliant row can verify the exclusion from the row alone, without cross-referencing the category label or trusting a template confirmation. The "confirmed" shortcut path closes the per-row form requirement (C-35) without reasoning about the specific weakness; C-37 closes this shortcut by requiring the weakness to be named and the per-row reason to be stated as a distinct sentence referencing the actual weakness. When self-diagnosis runs in Amendment 1 position (diagnosis-first), the four rows confirm the weakness could not have been caught by fixed passes yet to run; when in Amendment 5 position (standard), the four rows confirm four targeted passes left the weakness unaddressed. In both positions the criterion fires identically.
- **Pass condition**: The per-excluded-category verification table includes one row per fixed category (Gap sharpening, Result quantification, Implication tightening, Prose coherence), each row containing an N and a self-contained sentence that names the diagnosed weakness and states why it falls outside that specific category. A row using a template category-description parenthetical with "confirmed" does not satisfy C-37 even if C-35 (retired) would have been satisfied. At least three of the four rows must contain weakness-specific sentences; a row that restates the category boundary without naming the weakness fails.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                               |
|--------------|-----------------|--------|----------------------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                                          |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                            |
| Aspirational | C-10 to C-37    | 20     | Separates good from excellent. C-26, C-27, C-29, C-34, C-36, C-37 are the ceiling layer.    |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v10

| Change              | Detail |
|---------------------|--------|
| C-33 retired        | Universally passing in all R11 variations. C-36 (sub-phase canonical naming) is the new ceiling; C-33 as "phase sequence lock" is expectation, not achievement. |
| C-35 retired        | Universally passing in all R11 variations. C-37 (weakness-specific per-row reasoning) is the new ceiling; C-35 as "per-excluded-category verification" is expectation, not achievement. |
| C-27 updated        | Source note updated: C-33 (phase sequence lock) retired in v11; C-36 (sub-phase canonical naming) is the new ceiling; C-27 remains the per-path confirmation floor. |
| C-24 updated        | Source note updated: C-35 (per-excluded-category verification) retired v11; C-37 (weakness-specific per-row reasoning) is the new ceiling above C-24. |
| C-34 updated        | Source note updated: no new ceiling added in v11 for the positive-search-space branch -- C-34 remains the current aspirational ceiling for that branch. |
| C-36 added          | Sub-phase canonical naming in phase sequence lock -- from R11 V-01 signal. 2 pts. Sub-phase-rationale ceiling above the retired C-33 phase-sequence-lock floor. |
| C-37 added          | Weakness-specific per-row reasoning in per-excluded-category verification -- from R11 V-02 signal. 2 pts. Weakness-specific-sentence ceiling above the retired C-35 per-category-verification floor. |
| Tier description    | Updated to reflect C-10 to C-37 aspirational range (C-33, C-35 retired); ceiling layer is now C-26, C-27, C-29, C-34, C-36, C-37. |
| Aspirational subtotal | Remains 20 pts. Total remains 100. |

---

**Design notes:**

- **Thirteen criteria retired across v3-v11**: C-09 (v7), C-16 (v7), C-11/C-12/C-14/C-15/C-17/C-18 (v8), C-28/C-30 (v9), C-25/C-31/C-32 (v10), C-33/C-35 (v11). Pattern: retirement when universally passing AND a structurally stronger ceiling covers the same behavior.
- **Floor/ceiling chain integrity**: C-21->C-22 (coupling), C-20->C-23->C-26->C-29 (bridge lifecycle), C-07->C-24->C-34/C-37 (self-diagnosis), C-27->C-36 (inertia lifecycle). The self-diagnosis chain has two ceiling criteria sharing the C-24 floor: C-34 (structural motivation for where to look) and C-37 (weakness-specific exclusion reasoning per-row) capture distinct aspects of the Amendment 1 self-diagnosis pass.
- **C-36/C-37 structural logic**: Both share the v11 pattern -- a v10 criterion established a reasoning layer (phase sequence lock / per-category verification table); the v11 ceiling requires that layer to contain a further reasoning element that is self-contained and independently auditable without reference to external context. C-36: sequence lock lists phases AND provides sub-phase gate rationale (the pre-fill window argument motivating C-26/C-29 is now stated at commitment time). C-37: per-category rows exist AND each row is self-contained with weakness-specific reasoning (the exclusion can be audited from the row alone without trusting a template confirmation).
- **V-07 synthesis target**: No single R11 variation satisfies both new ceilings simultaneously. V-01 R11 passes C-36, fails C-37. V-02 R11 passes C-37, fails C-36. A next-generation synthesis variation for R12 would combine sub-phase canonical naming at the sequence lock (C-36) with weakness-specific per-row reasoning in the exclusion table (C-37), while retaining the positive-search-space asymmetry argument (C-34).
- **C-34 status**: The positive-search-space asymmetry argument branch (C-24 -> C-34) has no new R11 ceiling. All R11 variations inherit C-34 from V-05 R10 as base and pass it. If R11 generates a variation that extends the asymmetry argument further (e.g., pre-declaring positive-space targets at commitment time rather than at Amendment 1 execution time), a C-38 ceiling would be warranted in v12.
- **C-29 unchanged**: The two-sided CAN + CANNOT asymmetry requirement (tightened in v9) continues to differentiate in R11. All R11 variations carry both sides; no new ceiling is needed this round.
