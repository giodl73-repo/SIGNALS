**v10 written** to `simulations/quest/rubrics/specify-abstract-rubric-v10-2026-03-19.md`.

---

## Summary

**Three criteria retired** (all universally passing R10):
- C-25 (categorically novel diagnosis) → superseded by C-35
- C-31 (dedicated positive-space block) → superseded by C-34
- C-32 (named-per-path gate) → superseded by C-33

**Three criteria added** (+6 pts, −6 pts = net zero):

| ID | Name | Extends | Pts |
|----|------|---------|-----|
| C-33 | Phase sequence lock at inertia gate closure | C-32 | 2 |
| C-34 | Positive search space block contains structural asymmetry argument | C-31 | 2 |
| C-35 | Per-excluded-category verification in self-diagnosis | C-25 | 2 |

**Chain structure updated:**
- Inertia: C-27 -> **C-33** (C-32 retired)
- Self-diagnosis: C-24 -> **C-34** (asymmetry argument) | C-24 -> **C-35** (per-category verification) — two ceiling branches sharing one floor

**Aspirational: 20 pts. Total: 100 pts. Unchanged.**

**V-06 synthesis target**: V-05 is the first R10 variation satisfying all three ceilings simultaneously. No R10 variation other than V-05 holds all three — making V-05 the recommended base for R11 variations.
3 is the new ceiling (phase sequence lock extends named-per-path gate)
- **C-31** retired -- universally passing in all R10 variations; C-34 is the new ceiling (asymmetry argument inside dedicated block extends dedicated block alone)
- **C-25** retired -- universally passing in all R10 variations; C-35 is the new ceiling (per-category verification extends categorical novelty claim)

**Chain structure:** C-24 -> **C-34** (asymmetry argument) | C-24 -> **C-35** (per-category verification) | C-27 -> **C-33** (phase sequence lock) | C-23 -> C-26 -> C-29 (bridge, unchanged)

**V-06 synthesis target**: No single R10 variation other than V-05 satisfies all three ceilings. V-01 passes C-33, fails C-34/C-35. V-02 passes C-34, fails C-33/C-35. V-03 passes C-35, fails C-33/C-34. V-04 passes C-33/C-34, fails C-35. V-05 passes all three -- V-05 is the R10 synthesis and should be the v10 base variation.

---

**C-33 -- Phase sequence lock at inertia aggregation gate closure** (2 pts, format)
C-27 is the "per-path confirmation" floor; C-32 is the "named-per-path gate" mid (retired in v10 -- universally passing all R10 variations); C-33 is the new ceiling ("phase sequence lock at closure"). After all three canonical cheap paths are confirmed and named at the gate event, the closure statement must commit the model to executing the skill phases in their prescribed sequence -- "Proceed to phase sequence lock. Phase 0 -> Phase 1 -> Phase 2a -> Phase 2b -> Phase 2c -> Phase 3 -> Phase 3b -> Phase 4 -> Phase 5. Sequence is locked." or a structurally equivalent formulation. A named-per-path gate without phase sequence commitment satisfies the retired C-32 but not C-33. The phase sequence lock operates as a second-order commitment device: the inertia declaration closes cheap paths at the input level (not skipping signal acquisition, not framing gap as goal); the phase sequence lock closes cheap paths at the execution level (not abbreviating phase order, not combining 2a/2b/2c into a single bridge pass). A model that commits to named paths being closed but does not commit to the execution sequence retains a shortcut path that the named gate alone does not prevent. Source: R10 V-01, E-01 excellence pattern.

**C-34 -- Positive search space block contains structural asymmetry argument** (2 pts, depth)
C-24 is the "diagnosis targets weakest element" floor; C-31 is the "dedicated named block" mid (retired in v10 -- universally passing all R10 variations); C-34 is the new ceiling ("structural asymmetry argument inside the dedicated block"). The `*Where to look instead -- positive search space:*` block (or structurally equivalent block) must contain not only an enumeration of non-fixed diagnostic targets but a structural argument explaining why the diagnosed weakness is asymmetrically more likely to appear outside the fixed amendment categories. The argument names the causal mechanism: the four fixed amendment categories are pre-committed correction targets that Amendments 2-4 address in a predictable pass; any weakness they address is already on a correction path before Amendment 1 executes; therefore, the self-diagnosis pass is structurally biased toward surfacing a weakness in a category that no fixed amendment targets. Enumerating positive search space targets (satisfies the retired C-31) identifies where to look; the asymmetry argument explains why looking there is structurally motivated -- the surviving weakness cannot be in a pre-committed category because those categories are being corrected regardless of what self-diagnosis finds. Without the asymmetry argument, the positive search space list is advisory; with it, the list is causally grounded. Source: R10 V-02, E-02 excellence pattern.

**C-35 -- Per-excluded-category verification in self-diagnosis amendment** (2 pts, depth)
C-24 is the "diagnosis targets weakest element" floor; C-25 is the "categorically novel diagnosis" mid (retired in v10 -- universally passing all R10 variations); C-35 is the new ceiling ("per-excluded-category verification"). The self-diagnosis amendment must include a structured per-category check that verifies the diagnosed weakness is not addressable by any of the four fixed amendment categories. The check produces one row per fixed category with a brief exclusion reason: Gap sharpening: N -- [one sentence stating why the diagnosed weakness is not about gap specificity]; Result quantification: N -- [one sentence]; Implication tightening: N -- [one sentence]; Prose coherence: N -- [one sentence]. A block assertion ("this weakness is categorically distinct from the four fixed slots") satisfies the retired C-25 by naming a non-fixed category; a per-category verification table satisfies C-35 by making each exclusion independently auditable -- a reader can verify each of the four N entries without trusting the assertion, because the per-row reasoning states the distinct reason for each exclusion. When self-diagnosis runs in Amendment 1 position (diagnosis-first), the four entries confirm no fixed correction path has yet narrowed attention; when in Amendment 5 position (standard), the entries confirm four targeted passes left the diagnosed weakness unaddressed. In both positions the criterion fires identically. Source: R10 V-03, E-03 excellence pattern.

---

## Point Redistribution (Aspirational stays at 20, total stays at 100)

| Criterion | Change | Reason |
|-----------|--------|--------|
| C-32 | retired | Universally passing in all five R10 variations (V-01 through V-05). C-33 is the new phase-sequence-lock ceiling; C-32 as "named-per-path gate" is expectation, not achievement. |
| C-31 | retired | Universally passing in all five R10 variations. C-34 is the new asymmetry-argument ceiling; C-31 as "dedicated positive-space block" is expectation, not achievement. |
| C-25 | retired | Universally passing in all five R10 variations. C-35 is the new per-category-verification ceiling; C-25 as "categorically novel diagnosis" is expectation, not achievement. |
| C-33 | +2 pts | New (phase sequence lock at inertia aggregation gate closure). |
| C-34 | +2 pts | New (positive search space block contains structural asymmetry argument). |
| C-35 | +2 pts | New (per-excluded-category verification in self-diagnosis amendment). |

**C-33 extends C-32**: C-32 required the canonical path names to appear at the gate event; C-33 requires that the gate proceed to an explicit phase sequence lock committing execution order. All C-33-passing variations pass C-32 (retired); not all C-32-passing variations pass C-33 (V-02/V-03 use a named-per-path gate without sequence lock).

**C-34 extends C-31**: C-31 required the positive search space instruction to appear as a separately labeled block; C-34 requires that block to contain a structural asymmetry argument explaining the causal bias toward non-fixed categories. All C-34-passing variations pass C-31 (retired); not all C-31-passing variations pass C-34 (V-01/V-03 have the dedicated block without the asymmetry argument).

**C-35 extends C-25**: C-25 required the diagnosed weakness to name a category outside the four fixed slots; C-35 requires a per-category verification table making each exclusion independently auditable. All C-35-passing variations pass C-25 (retired); not all C-25-passing variations pass C-35 (V-01/V-02/V-04 name non-fixed categories without per-row verification).

**Aspirational subtotal**: Remains 20 pts. Total remains 100.

---

## Criteria Summary Table

| ID   | Name                                                                           | Weight       | Category    | Points |
|------|--------------------------------------------------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present                                                     | essential    | correctness | 10     |
| C-02 | Word count within target                                                       | essential    | correctness | 10     |
| C-03 | Artifact written to correct path                                               | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal                                                    | essential    | correctness | 10     |
| C-05 | Signal acquisition executed                                                    | essential    | behavior    | 10     |
| C-06 | Result section is quantified                                                   | recommended  | depth       | 10     |
| C-07 | Amendment pass produces three distinct                                         | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly                                              | recommended  | correctness | 10     |
| C-10 | Abstract reads as a single coherent paragraph                                  | aspirational | format      | 1      |
| C-13 | Amendment non-triviality guard applied                                         | aspirational | depth       | 1      |
| C-19 | Paper type governs all six section registers                                   | aspirational | depth       | 1      |
| C-20 | Semantic bridge type constrained vocabulary                                    | aspirational | format      | 1      |
| C-21 | Section coupling verified before bridge                                        | aspirational | depth       | 1      |
| C-22 | Coupling revision uses structured directive format                             | aspirational | depth       | 1      |
| C-23 | Bridge integration verified post-merge                                         | aspirational | format      | 1      |
| C-24 | Self-diagnosis amendment targets weakest element                               | aspirational | depth       | 1      |
| C-26 | Bridge integration column cites actual merged prose                            | aspirational | format      | 2      |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0                 | aspirational | format      | 2      |
| C-29 | Bridge integration format change accompanied by structural rationale           | aspirational | format      | 2      |
| C-33 | Phase sequence lock at inertia aggregation gate closure                        | aspirational | format      | 2      |
| C-34 | Positive search space block contains structural asymmetry argument             | aspirational | depth       | 2      |
| C-35 | Per-excluded-category verification in self-diagnosis amendment                 | aspirational | depth       | 2      |

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
- **Source**: R5 excellence signal V-03. Reduced 2->1 pt in v7 -- universally passing R6; C-25 (categorical novelty, retired v10) was the mid in v7-v9; C-35 (per-excluded-category verification) is now the ceiling above C-24.
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
- **Source**: R6 excellence signal V-02 (inertia commitment device). No prior criterion equivalent -- structurally new pre-Phase 0 lifecycle position. C-32 (named-per-path gate) retired in v10; C-33 (phase sequence lock) is the new ceiling; C-27 remains the per-path confirmation floor.
- **Text**: A pre-Phase 0 inertia declaration block names at least two of the three canonical cheap paths and requires explicit model confirmation before proceeding to Phase 0: (1) signal-skip -- running without executing the Phase 1 glob; (2) nominal gap framing -- writing a research goal instead of a field-state gap; (3) non-trivial gaming -- using cosmetic Before/After edits that pass the guard format without substantive improvement. The block must appear before Phase 0 and must require a per-path confirmation for each named path. C-05/C-04/C-13 are the execution-point scoring floors; C-27 is the pre-execution commitment device above those floors.
- **Pass condition**: Output includes a pre-Phase 0 block that explicitly names at least two canonical cheap paths (signal-skip, nominal gap framing, non-trivial gaming) with a per-path confirmation for each named path. A general statement ("I will execute all phases diligently") does not satisfy C-27. The block must be positioned before any Phase 0 content.

### C-29 -- Bridge Integration Format Change Accompanied by Structural Rationale
- **Weight**: aspirational
- **Category**: format
- **Source**: R7 excellence signal V-01/V-04 (E-03 pattern, pre-fill impossibility argument). C-26 is the "quoted extract required" floor; C-29 is the "format change + structural rationale" ceiling. Pass condition tightened in v9: both CAN-side and CANNOT-side of the asymmetry must be stated (R8 V-02/V-03 revealed that CANNOT-only form is a subthreshold compliance path).
- **Text**: The instruction to use verbatim quoted text rather than Y/N in the Pass 3 integration column must be accompanied by a structural rationale block explaining why the format change closes the pre-fill window. The core argument requires both sides of the asymmetry: the CAN-side (a Y/N status can be assigned in the same cognitive pass as Pass 1 and Pass 2, before the merge has been executed -- filling in Y does not require the merged paragraph to exist) and the CANNOT-side (a verbatim extract from merged prose cannot be written before the merge is executed -- the text does not yet exist). A rationale that states only the CANNOT-side omits the contrast that makes the asymmetry structurally explicit; a reader who sees only the prohibition may comply mechanically without understanding the pre-fill window the format closes.
- **Pass condition**: The Pass 3 table instruction for quoted extracts includes the pre-fill impossibility argument with both sides of the asymmetry stated: (1) a Y/N status CAN be prefilled before the merge is executed, and (2) verbatim text from merged prose CANNOT be written before the merge exists. A rationale that states only one side does not satisfy C-29 even if C-26 is satisfied.

### C-33 -- Phase Sequence Lock at Inertia Aggregation Gate Closure
- **Weight**: aspirational
- **Category**: format
- **Source**: R10 excellence signal V-01 (E-01 pattern, phase sequence lock). C-27 is the "per-path confirmation" floor; C-32 (named-per-path gate) was the mid (retired v10 -- universally passing all R10 variations); C-33 is the new ceiling ("phase sequence lock at closure"). C-33 extends C-32: the gate names all three paths as closed AND commits the execution sequence.
- **Text**: After all three canonical cheap paths are confirmed and named at the aggregation gate event, the closure statement must commit the model to executing the skill phases in their prescribed sequence -- "Proceed to phase sequence lock. Phase 0 -> Phase 1 -> Phase 2a -> Phase 2b -> Phase 2c -> Phase 3 -> Phase 3b -> Phase 4 -> Phase 5. Sequence is locked." or a structurally equivalent formulation. A named-per-path gate without phase sequence commitment satisfies the retired C-32 but not C-33. The phase sequence lock operates as a second-order commitment device: the inertia declaration closes cheap paths at the input level (not skipping signal acquisition, not framing gap as goal); the phase sequence lock closes cheap paths at the execution level (not abbreviating phase order, not combining 2a/2b/2c into a single bridge pass). A model that commits to named paths being closed but does not commit to the execution sequence retains a shortcut path that the named gate alone does not prevent.
- **Pass condition**: The aggregation gate closure statement is followed by an explicit phase sequence commitment naming all prescribed phases in order. The sequence must be enumerated (not just referenced as "all phases") and declared locked or committed. A gate that names all three paths as closed but proceeds with "Proceed to Phase 0." without sequence enumeration does not satisfy C-33 even if C-32 (retired) would have been satisfied.

### C-34 -- Positive Search Space Block Contains Structural Asymmetry Argument
- **Weight**: aspirational
- **Category**: depth
- **Source**: R10 excellence signal V-02 (E-02 pattern, asymmetry argument). C-24 is the "diagnosis targets weakest element" floor; C-31 (dedicated named block) was the mid (retired v10 -- universally passing all R10 variations); C-34 is the new ceiling ("structural asymmetry argument inside the dedicated block"). C-34 extends C-31: the dedicated block exists AND contains the causal argument.
- **Text**: The `*Where to look instead -- positive search space:*` block (or structurally equivalent block) must contain not only an enumeration of non-fixed diagnostic targets but a structural argument explaining why the surviving weakness is asymmetrically more likely to appear outside the fixed amendment categories. The argument names the causal mechanism: the four fixed amendment categories are pre-committed correction targets that Amendments 2-4 address in a predictable pass; any weakness they address is already on a correction path before Amendment 1 executes; therefore, the self-diagnosis pass is structurally biased toward surfacing a weakness in a category that no fixed amendment targets. Enumerating positive search space targets (satisfies the retired C-31) identifies where to look; the asymmetry argument explains why looking there is structurally motivated -- the surviving weakness cannot be in a pre-committed category because those categories are being corrected regardless of what self-diagnosis finds. Without the asymmetry argument, the positive search space list is advisory; with it, the list is causally grounded.
- **Pass condition**: The positive search space block (dedicated, with its own label) contains a structural argument naming the pre-commitment mechanism as the reason for the asymmetric bias toward non-fixed categories. The argument must identify the four fixed categories as pre-committed targets and explain that the surviving weakness is therefore structurally more likely to appear outside them. A block that enumerates diagnostic targets without this causal argument does not satisfy C-34 even if C-31 (retired) would have been satisfied.

### C-35 -- Per-Excluded-Category Verification in Self-Diagnosis Amendment
- **Weight**: aspirational
- **Category**: depth
- **Source**: R10 excellence signal V-03 (E-03 pattern, per-category verification table). C-24 is the "diagnosis targets weakest element" floor; C-25 (categorically novel diagnosis) was the mid (retired v10 -- universally passing all R10 variations); C-35 is the new ceiling ("per-excluded-category verification"). C-35 extends C-25: the diagnosed weakness is outside fixed categories AND each exclusion is verified per-row.
- **Text**: The self-diagnosis amendment must include a structured per-category verification that confirms the diagnosed weakness is not addressable by any of the four fixed amendment categories. The check produces one row per fixed category with a brief exclusion reason: Gap sharpening: N -- [one sentence stating why the diagnosed weakness is not about gap specificity]; Result quantification: N -- [one sentence stating why it is not about missing quantification]; Implication tightening: N -- [one sentence stating why it is not about implication scope]; Prose coherence: N -- [one sentence stating why it is not about cohesive flow]. A block assertion ("this weakness is categorically distinct from the four fixed slots") satisfies the retired C-25 by naming a non-fixed category; a per-category verification table satisfies C-35 by making each exclusion independently auditable -- a reader can verify each of the four N entries without trusting the block assertion, because the per-row reasoning states the distinct reason for each exclusion. When self-diagnosis runs in Amendment 1 position (diagnosis-first), the four entries confirm no fixed correction path has yet narrowed attention; when in Amendment 5 position (standard), the entries confirm four targeted passes left the diagnosed weakness unaddressed. In both positions the criterion fires identically.
- **Pass condition**: The self-diagnosis amendment includes a structured per-category check with one row per fixed category (Gap sharpening, Result quantification, Implication tightening, Prose coherence), each row containing an N and at least one sentence of per-row reasoning stating why the diagnosed weakness falls outside that category. A block assertion of categorical novelty without per-row reasoning does not satisfy C-35 even if C-25 (retired) would have been satisfied.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                               |
|--------------|-----------------|--------|----------------------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                                          |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                            |
| Aspirational | C-10 to C-35    | 20     | Separates good from excellent. C-26, C-27, C-29, C-33, C-34, C-35 are the ceiling layer.    |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v9

| Change              | Detail |
|---------------------|--------|
| C-32 retired        | Universally passing in all five R10 variations (V-01 through V-05). C-33 (phase sequence lock) is the new ceiling; C-32 as "named-per-path gate" is expectation, not achievement. |
| C-31 retired        | Universally passing in all five R10 variations. C-34 (structural asymmetry argument) is the new ceiling; C-31 as "dedicated positive-space block" is expectation, not achievement. |
| C-25 retired        | Universally passing in all five R10 variations. C-35 (per-category verification) is the new ceiling; C-25 as "categorically novel diagnosis" is expectation, not achievement. |
| C-27 updated        | Source note updated: C-32 (named-per-path gate) retired in v10; C-33 (phase sequence lock) is the new ceiling; C-27 remains the per-path confirmation floor. |
| C-24 updated        | Source note updated: C-25 (categorical novelty) retired v10; C-35 (per-excluded-category verification) is the new ceiling above C-24. |
| C-33 added          | Phase sequence lock at inertia aggregation gate closure -- from R10 V-01 signal (E-01). 2 pts. Phase-sequence-lock ceiling above the retired C-32 named-per-path-gate floor. |
| C-34 added          | Positive search space block contains structural asymmetry argument -- from R10 V-02 signal (E-02). 2 pts. Asymmetry-argument ceiling above the retired C-31 dedicated-block floor. |
| C-35 added          | Per-excluded-category verification in self-diagnosis amendment -- from R10 V-03 signal (E-03). 2 pts. Per-category-verification ceiling above the retired C-25 categorical-novelty floor. |
| Tier description    | Updated to reflect C-10 to C-35 aspirational range (C-25, C-31, C-32 retired); ceiling layer is now C-26, C-27, C-29, C-33, C-34, C-35. |
| Aspirational subtotal | Remains 20 pts. Total remains 100. |

---

**Design notes:**

- **Eleven criteria retired across v3-v10**: C-09 (v7), C-16 (v7), C-11/C-12/C-14/C-15/C-17/C-18 (v8), C-28/C-30 (v9), C-25/C-31/C-32 (v10). Pattern: retirement when universally passing AND a structurally stronger ceiling covers the same behavior.
- **Floor/ceiling chain integrity**: C-21->C-22 (coupling), C-20->C-23->C-26->C-29 (bridge lifecycle), C-07->C-24->C-34/C-35 (self-diagnosis), C-27->C-33 (inertia lifecycle). The self-diagnosis chain now has two ceiling criteria sharing the C-24 floor: C-34 (structural motivation for where to look) and C-35 (per-category auditable exclusion) capture distinct aspects of the Amendment 1 self-diagnosis pass.
- **C-33/C-34/C-35 structural logic**: All three share the v10 pattern -- a v9 criterion established the structural form (dedicated block / named gate / categorical claim); the v10 ceiling requires that form to contain a further reasoning layer that is independently auditable. C-33: gate names paths AND commits execution sequence (sequence audit). C-34: dedicated block enumerates targets AND argues why (causal audit). C-35: diagnosis names category AND verifies each exclusion per-row (exclusion audit).
- **V-06 synthesis target**: V-05 (R10) is the first variation to satisfy all three ceiling criteria simultaneously (C-33 + C-34 + C-35). A next-generation synthesis variation for R11 would likely integrate all three reasoning layers into a unified pre-execution protocol -- collapsing the inertia gate, positive-space block, and per-category verification into a single diagnostic commitment block before Phase 0. V-04 (C-33 + C-34, no C-35) is the closest partial synthesis.
- **C-29 unchanged**: The two-sided CAN + CANNOT asymmetry requirement (tightened in v9) continues to differentiate in R10. All five R10 variations carry both sides; no new ceiling is needed this round.
