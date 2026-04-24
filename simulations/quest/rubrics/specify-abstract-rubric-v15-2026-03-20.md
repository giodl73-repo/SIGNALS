# specify-abstract Rubric v15

**Extracted from R15 excellence signals.**

---

**One criterion extracted from R15 excellence signals:**

| ID | Name | Extends | Pts | Source |
|----|------|---------|-----|--------|
| C-46 | Named pre-committed source-gate dependency protocol declared before Phase 0 | C-45 | 2 | R15 V-05 C-45 above-ceiling |

**Point math:** No retirements. +2 pts net. Aspirational: 36 → 38. Total: 116 → 118.

---

**Extraction rationale:**

**C-46** from V-05 C-45 evidence: "Protocol II completion conditions carry `(Source gate: Phase X per Protocol V.)` inline references for all output-dependent phases." V-05 introduces Protocol V as a named pre-committed dependency protocol — a separate block declared before Phase 0 that formalizes the inter-gate source dependencies as a registry. Protocol II's per-gate completion conditions cite Protocol V by name rather than embedding the dependency declaration inline. Phase 3b's completion condition carries `"(Source gate: Phase 3 per Protocol V. Extracts CANNOT be written before Phase 3 produces the merged text.)"` — the impossibility argument is embedded directly in the completion condition by citation to the pre-committed protocol.

C-45 requires inline source-gate declarations within per-gate completion conditions; C-46 requires those declarations to be organized as a named pre-committed protocol positioned before Phase 0, which the completion conditions then cite by reference. This follows the C-34 → C-42 pattern exactly: C-34 required the structural asymmetry argument at Phase 5 (runtime-introduced); C-42 required it pre-committed as Protocol III before Phase 0 (temporal separation). C-45 requires source declarations inline at the completion-condition level; C-46 requires them pre-committed as Protocol V before Phase 0. A variation with inline `[Source: FROM Phase X]` per-gate annotations satisfies C-45 but not C-46; a variation where completion conditions cite `(Source gate: Phase X per Protocol V.)` and Protocol V exists as a named pre-Phase 0 block satisfies C-46.

**Chain updated:**
- Sequence lock conditions branch: `C-27 → ~~C-33~~ → C-36 → C-38 → C-40 → C-45 → C-46`
- All other chains unchanged.

**R16 synthesis target:** A variation clearing all eleven active ceiling criteria (C-36 through C-46) simultaneously — R15 synthesis base + named pre-committed dependency protocol (C-46) with Protocol II completion conditions citing Protocol V by name.

---

## Point Redistribution (Aspirational moves to 38, total moves to 118)

| Criterion | Change | Reason |
|-----------|--------|--------|
| C-36 | no change | Not confirmed universally passing in R15 (only V-04 and V-05 visible as full synthesis). Ceiling remains active. |
| C-37 | no change | Not confirmed universally passing in R15. Ceiling remains active. |
| C-38 | no change | Not confirmed universally passing in R15. Ceiling remains active. |
| C-39 | no change | Not confirmed universally passing in R15. Ceiling remains active. |
| C-40 | no change | Not confirmed universally passing in R15 (V-01 fails C-40 by design). Ceiling remains active. |
| C-41 | no change | Not confirmed universally passing in R15 (V-01 fails C-41 by design). Ceiling remains active. |
| C-42 | no change | Not confirmed universally passing in R15. Ceiling remains active. |
| C-43 | no change | Not confirmed universally passing in R15 (V-01 fails C-43 by design in isolation). Ceiling remains active. |
| C-44 | no change | V-02 and V-03 fail C-44 by design (isolation of C-45). Not universally passing. Ceiling remains active. |
| C-45 | no change | V-01 fails C-45 by design (isolation of C-44). Not universally passing. C-46 (named pre-committed dependency protocol) is new ceiling above C-45. |
| C-46 | +2 pts | New (named pre-committed source-gate dependency protocol declared before Phase 0). |

**C-46 extends C-45**: C-45 required source-gate declarations inline in per-gate completion conditions; C-46 requires those declarations to be organized as a named pre-committed protocol (Protocol V or equivalent) positioned before Phase 0, with completion conditions citing the protocol by reference rather than embedding declarations inline. All C-46-passing variations pass C-45 and C-40; not all C-45-passing variations pass C-46 (V-02 and V-03 use inline `[Source: FROM Phase X]` notation; V-05 uses `(Source gate: Phase X per Protocol V.)` with Protocol V as a named pre-Phase 0 block).

**Aspirational subtotal**: Moves to 38 pts. Total moves to 118.

---

## Criteria Summary Table

| ID   | Name                                                                                                               | Weight       | Category    | Points |
|------|--------------------------------------------------------------------------------------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present                                                                                         | essential    | correctness | 10     |
| C-02 | Word count within target                                                                                           | essential    | correctness | 10     |
| C-03 | Artifact written to correct path                                                                                   | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal                                                                                        | essential    | correctness | 10     |
| C-05 | Signal acquisition executed                                                                                        | essential    | behavior    | 10     |
| C-06 | Result section is quantified                                                                                       | recommended  | depth       | 10     |
| C-07 | Amendment pass produces three distinct                                                                             | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly                                                                                  | recommended  | correctness | 10     |
| C-10 | Abstract reads as a single coherent paragraph                                                                      | aspirational | format      | 1      |
| C-13 | Amendment non-triviality guard applied                                                                             | aspirational | depth       | 1      |
| C-19 | Paper type governs all six section registers                                                                       | aspirational | depth       | 1      |
| C-20 | Semantic bridge type constrained vocabulary                                                                        | aspirational | format      | 1      |
| C-21 | Section coupling verified before bridge                                                                            | aspirational | depth       | 1      |
| C-22 | Coupling revision uses structured directive format                                                                 | aspirational | depth       | 1      |
| C-23 | Bridge integration verified post-merge                                                                             | aspirational | format      | 1      |
| C-24 | Self-diagnosis amendment targets weakest element                                                                   | aspirational | depth       | 1      |
| C-26 | Bridge integration column cites actual merged prose                                                                | aspirational | format      | 2      |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0                                                     | aspirational | format      | 2      |
| C-29 | Bridge integration format change accompanied by structural rationale                                               | aspirational | format      | 2      |
| C-34 | Positive search space block contains structural asymmetry argument                                                 | aspirational | depth       | 2      |
| C-36 | Sub-phase canonical naming in phase sequence lock                                                                  | aspirational | format      | 2      |
| C-37 | Weakness-specific per-row reasoning in per-excluded-category verification                                          | aspirational | depth       | 2      |
| C-38 | Complete sub-phase inventory in phase sequence lock                                                                | aspirational | format      | 2      |
| C-39 | Standalone rationale block in per-excluded-category verification names and closes shortcut mechanism               | aspirational | depth       | 2      |
| C-40 | Per-gate falsifiable completion conditions in phase sequence lock                                                  | aspirational | format      | 2      |
| C-41 | Second-order category-mirroring shortcut prohibited in per-excluded-category verification                         | aspirational | depth       | 2      |
| C-42 | Pre-committed self-diagnosis framework with temporal separation before Phase 0                                     | aspirational | depth       | 2      |
| C-43 | Inertia declaration names phase bundling as fourth canonical cheap path                                            | aspirational | format      | 2      |
| C-44 | Complete anti-bundling rationale coverage at all phase transitions                                                 | aspirational | format      | 2      |
| C-45 | Inter-gate input dependency declarations in per-gate completion conditions                                         | aspirational | format      | 2      |
| C-46 | Named pre-committed source-gate dependency protocol declared before Phase 0                                        | aspirational | format      | 2      |

Aspirational check: 1+1+1+1+1+1+1+1+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2 = **38**

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

## Aspirational Criteria (38 points total)

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
- **Source**: R5 excellence signal V-03. Reduced 2->1 pt in v7 -- universally passing R6; C-25 (categorical novelty, retired v10) was the mid in v7-v9; C-35 (per-excluded-category verification, retired v11) was the mid in v10; C-37 (weakness-specific per-row reasoning) is the first ceiling; C-39 (standalone rationale block naming shortcut) is the second ceiling; C-41 (second-order mirroring shortcut) is the third ceiling (v13); C-42 (pre-committed framework with temporal separation) is the fourth ceiling (v13).
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
- **Source**: R6 excellence signal V-02 (inertia commitment device). No prior criterion equivalent -- structurally new pre-Phase 0 lifecycle position. C-32 (named-per-path gate) retired in v10; C-33 (phase sequence lock) retired in v11; C-36 (sub-phase canonical naming) is the sequence-lock first ceiling; C-38 (complete sub-phase inventory) is the second sequence-lock ceiling; C-40 (per-gate falsifiable completion conditions) is the third sequence-lock ceiling (v13); C-45 (inter-gate input dependency declarations) is the fourth sequence-lock ceiling (v14); C-46 (named pre-committed dependency protocol) is the fifth sequence-lock ceiling (v15). C-43 (phase bundling as fourth canonical cheap path) is the declaration-completeness ceiling (v13); C-27 remains the per-path confirmation floor.
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
- **Source**: R10 excellence signal V-02 (E-02 pattern, asymmetry argument). C-24 is the "diagnosis targets weakest element" floor; C-31 (dedicated named block) was the mid (retired v10 -- universally passing all R10 variations); C-34 is the "structural asymmetry argument inside the dedicated block" ceiling. C-42 (pre-committed self-diagnosis framework with temporal separation) is the ceiling above C-34 (v13).
- **Text**: The `*Where to look instead -- positive search space:*` block (or structurally equivalent block) must contain not only an enumeration of non-fixed diagnostic targets but a structural argument explaining why the surviving weakness is asymmetrically more likely to appear outside the fixed amendment categories. The argument names the causal mechanism: the four fixed amendment categories are pre-committed correction targets that Amendments 2-4 address in a predictable pass; any weakness they address is already on a correction path before Amendment 1 executes; therefore, the self-diagnosis pass is structurally biased toward surfacing a weakness in a category that no fixed amendment targets. Enumerating positive search space targets (satisfies the retired C-31) identifies where to look; the asymmetry argument explains why looking there is structurally motivated -- the surviving weakness cannot be in a pre-committed category because those categories are being corrected regardless of what self-diagnosis finds. Without the asymmetry argument, the positive search space list is advisory; with it, the list is causally grounded.
- **Pass condition**: The positive search space block (dedicated, with its own label) contains a structural argument naming the pre-commitment mechanism as the reason for the asymmetric bias toward non-fixed categories. The argument must identify the four fixed categories as pre-committed targets and explain that the surviving weakness is therefore structurally more likely to appear outside them. A block that enumerates diagnostic targets without this causal argument does not satisfy C-34 even if C-31 (retired) would have been satisfied.

### C-36 -- Sub-Phase Canonical Naming in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R11 excellence signal V-01 (C-36 pattern, sub-phase canonical naming). C-27 is the "per-path confirmation" floor; C-33 (phase sequence lock) was the mid (retired v11 -- universally passing all R11 variations); C-36 is the "sub-phase canonical naming with structural rationale block" ceiling. C-38 (complete sub-phase inventory) is the ceiling above C-36; C-40 (per-gate falsifiable completion conditions) is above C-38 in the conditions branch; C-45 (inter-gate input dependency declarations) is the ceiling above C-40 (v14); C-46 (named pre-committed dependency protocol) is the ceiling above C-45 (v15). C-44 (complete anti-bundling rationale coverage at all phase transitions) is the ceiling above C-38 in the rationale branch (v14).
- **Text**: The phase sequence lock (at the aggregation gate closure) must enumerate Phase 3 (merge) and Phase 3b (integration verification) as individually named sub-phase gates and include a structural rationale block ("*Why sub-phase canonical naming matters*" or structurally equivalent) explaining the Phase 3 -> Phase 3b gate dependency. The rationale names the causal mechanism: Phase 3b requires the merged paragraph as input; a model that treats Phase 3 and Phase 3b as a combined or unlabeled step retains the pre-fill shortcut of filling the Phase 3b integration column before the merge has been executed -- the same pre-fill window that C-26 and C-29 were designed to close at the verification stage. Sub-phase canonical naming at the sequence lock stage closes this window at the commitment level: the model commits before Phase 0 that Phase 3b is a named sub-phase gate requiring Phase 3 output, making the pre-fill shortcut structurally blocked from the start rather than only detectable post-hoc. A sequence lock that lists all phases including Phase 3 and Phase 3b without a sub-phase rationale block satisfies the retired C-33 but not C-36.
- **Pass condition**: The phase sequence lock includes Phase 3 and Phase 3b named as individually gated sub-phases AND a structural rationale block explaining the Phase 3 -> Phase 3b gate dependency in terms of the pre-fill window that C-26/C-29 close at the verification stage. The rationale must identify the causal mechanism (Phase 3b requires post-merge text as input) and state why sub-phase naming at the commitment stage closes the shortcut earlier than verification-stage guards alone. A sequence lock that enumerates the phases without this rationale block does not satisfy C-36 even if C-33 (retired) would have been satisfied.

### C-37 -- Weakness-Specific Per-Row Reasoning in Per-Excluded-Category Verification
- **Weight**: aspirational
- **Category**: depth
- **Source**: R11 excellence signal V-02 (C-37 pattern, weakness-specific per-row reasoning). C-24 is the "diagnosis targets weakest element" floor; C-35 (per-excluded-category verification) was the mid (retired v11 -- universally passing all R11 variations); C-37 is the "weakness-specific per-row reasoning" ceiling. C-39 (standalone rationale block naming and closing shortcut mechanism) is the ceiling above C-37; C-41 (second-order category-mirroring shortcut) is the ceiling above C-39 (v13).
- **Text**: The per-excluded-category verification table must contain, in each row, a sentence that names the actual diagnosed weakness and states specifically why that weakness is not an instance of the category -- not a template parenthetical describing the category boundary with "[confirmed / explain if uncertain]". The distinction: a C-35-compliant row can be written as "Gap sharpening: N -- [the named weakness does not target the Gap sentence's specificity: confirmed]" using the category-description template; a C-37-compliant row requires "Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]" where the sentence is self-contained and weakness-grounded. A reader auditing a C-37-compliant row can verify the exclusion from the row alone, without cross-referencing the category label or trusting a template confirmation. The "confirmed" shortcut path closes the per-row form requirement (C-35) without reasoning about the specific weakness; C-37 closes this shortcut by requiring the weakness to be named and the per-row reason to be stated as a distinct sentence referencing the actual weakness.
- **Pass condition**: The per-excluded-category verification table includes one row per fixed category (Gap sharpening, Result quantification, Implication tightening, Prose coherence), each row containing an N and a self-contained sentence that names the diagnosed weakness and states why it falls outside that specific category. A row using a template category-description parenthetical with "confirmed" does not satisfy C-37 even if C-35 (retired) would have been satisfied. At least three of the four rows must contain weakness-specific sentences; a row that restates the category boundary without naming the weakness fails.

### C-38 -- Complete Sub-Phase Inventory in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R12 excellence signal V-01 (C-38 pattern, complete sub-phase inventory -- "Nine individually named sub-phases"). C-36 is the "Phase 3/3b individually named with structural rationale block" floor; C-38 is the "complete sub-phase inventory" ceiling. C-40 (per-gate falsifiable completion conditions) is the conditions-branch ceiling above C-38 (v13); C-45 (inter-gate input dependency declarations) is the ceiling above C-40 (v14); C-46 (named pre-committed dependency protocol) is the ceiling above C-45 (v15). C-44 (complete anti-bundling rationale coverage at all phase transitions) is the rationale-branch ceiling above C-38 (v14).
- **Text**: The phase sequence lock must enumerate ALL phases as individually named sub-phase gates -- not just the Phase 3/3b pair. A complete sub-phase inventory makes any coarse-grain bundling visible: a reader can verify at a glance that no two phases have been silently combined or aggregated under a shared label. The distinction: a C-36-compliant lock names Phase 3 and Phase 3b individually and may aggregate other phases (e.g., treating Phase 0 through Phase 2 as a pre-execution block) without per-phase enumeration; a C-38-compliant lock names every phase as a separately gated unit so that the full commitment inventory is explicit before Phase 0. Complete sub-phase inventory closes the bundling shortcut at phases other than 3/3b: a model that aggregates earlier phases retains the coarse-grain structure that C-36 closes for the merge pair, applied elsewhere. A sequence lock that names Phase 3 and Phase 3b individually but bundles other phases satisfies C-36 but not C-38.
- **Pass condition**: The phase sequence lock enumerates every phase in the skill's execution sequence as an individually named gate unit -- no two phases are bundled under a shared label or aggregated. The Phase 3/3b sub-phase structure required by C-36 must also be present. A lock that names Phase 3 and Phase 3b but aggregates other phases (e.g., "Phase 0 through Phase 2 -- pre-execution setup") does not satisfy C-38 even if C-36 is satisfied.

### C-39 -- Standalone Rationale Block in Per-Excluded-Category Verification Names and Closes Shortcut Mechanism
- **Weight**: aspirational
- **Category**: depth
- **Source**: R12 excellence signal V-02 (C-39 pattern -- "[confirmed] shortcut explicitly closed; '*Why specific per-row sentences matter:*' rationale present"). C-37 is the "weakness-specific per-row reasoning" floor; C-39 is the "standalone rationale block naming and closing shortcut mechanism" ceiling. C-41 (second-order category-mirroring shortcut) is the ceiling above C-39 (v13).
- **Text**: The per-excluded-category verification section must include a standalone rationale block ("*Why specific per-row sentences matter:*" or structurally equivalent) that (a) explicitly names the template shortcut path ("[confirmed / explain if uncertain]" or equivalent form), (b) explains why template confirmation fails the verification requirement -- specifically, that a template parenthetical describes the category boundary without referencing the diagnosed weakness, making it impossible to audit the exclusion from the row alone, and (c) declares the weakness-specific sentence as the required form. The distinction: a C-37-compliant variation can satisfy the per-row sentence requirement without ever explicitly naming or prohibiting the template form -- a reader auditing per-row entries can verify they are weakness-specific, but the variation itself may not have instructed the model that the shortcut is closed; a C-39-compliant variation includes a standalone block that names the shortcut and explains its structural insufficiency, ensuring the prohibition is instructed rather than incidentally absent. A variation that has weakness-specific per-row sentences without a standalone named-shortcut rationale block satisfies C-37 but not C-39.
- **Pass condition**: The per-excluded-category verification section includes a standalone rationale block that (1) names the "[confirmed / explain if uncertain]" template form (or equivalent) by name or close paraphrase, (2) explains why the template form is insufficient -- the category-description parenthetical does not reference the diagnosed weakness -- and (3) declares the self-contained weakness-specific sentence as the required per-row form. A variation that has weakness-specific rows without this standalone named-shortcut rationale block does not satisfy C-39 even if C-37 is satisfied.

### C-40 -- Per-Gate Falsifiable Completion Conditions in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R13 excellence signal V-05 Protocol II (C-38 above-ceiling -- "Per-gate conditions extend the C-38 commitment to falsifiable completion criteria"). C-38 is the "complete sub-phase inventory" floor; C-40 is the "per-gate falsifiable completion conditions" ceiling. C-45 (inter-gate input dependency declarations) is the ceiling above C-40 (v14); C-46 (named pre-committed dependency protocol) is the ceiling above C-45 (v15). C-40 extends C-38: all phases individually named is the prerequisite; per-gate conditions are the additional requirement.
- **Text**: The phase sequence lock must attach an explicit, observable completion condition to each individually named gate -- not merely a label or positional instruction. A falsifiable completion condition specifies WHAT IS TRUE when a gate is closed, such that a reader (or auditing pass) can verify whether Phase X was complete before Phase Y began. Example form for Phase 2b: "Complete when: all five boundaries assigned COUPLED/WEAK/REVISE AND all WEAK/REVISE revision directives resolved; Coupling column fully populated." The distinction: a C-38-compliant lock names every gate individually; a C-40-compliant lock names every gate AND attaches a named completion condition for each. Per-gate conditions convert the sequence lock from a DECLARATION ("Phase X must complete before Phase Y") into an AUDITABLE CHECKLIST (a reader can verify each completion criterion against the execution output). C-38 closes the phase enumeration gap; C-40 closes the completion-definition gap: a model can satisfy C-38 by listing all nine phase names as individually gated units while treating "completion" as implicit -- no gate is auditably closed unless its condition has been explicitly named. A sequence lock that names all phases individually without per-gate completion conditions satisfies C-38 but not C-40.
- **Pass condition**: The phase sequence lock attaches a named, observable completion condition to each individually gated phase. Each condition specifies what must be true for the gate to be considered closed -- output columns populated, required inputs present, specific structural requirements met, or equivalent falsifiable criterion. A lock that names gates but specifies conditions only implicitly (by gate label alone or generic "must complete before proceeding") does not satisfy C-40 even if C-38 is satisfied. The Phase 3/3b structure required by C-36/C-38 must also be present.

### C-41 -- Second-Order Category-Mirroring Shortcut Prohibited in Per-Excluded-Category Verification
- **Weight**: aspirational
- **Category**: depth
- **Source**: R13 excellence signal V-05 Amendment 1 (C-39 above-ceiling -- "Second-order category-mirroring shortcut: satisfies C-37's per-row sentence requirement while bypassing genuine reasoning"). C-39 is the "standalone rationale block naming first-order template shortcut" floor; C-41 is the "second-order category-mirroring shortcut also named and prohibited" ceiling. C-41 extends C-39: the first-order shortcut closure is the prerequisite; the second-order shortcut closure is the additional requirement.
- **Text**: The per-excluded-category verification standalone rationale block must name and prohibit TWO shortcuts: (1) the first-order `[confirmed / explain if uncertain]` template shortcut (C-39 floor), AND (2) the second-order category-mirroring shortcut -- a per-row sentence that appears weakness-specific but merely restates the category label in different words. A category-mirroring sentence has the structural shape of a weakness-specific exclusion (subject: the weakness; predicate: does not fall in category X because [restated category definition]) without the substance (the actual weakness is not named; the exclusion restates the category boundary rather than applying it to the diagnosis). Example second-order form for the Gap sharpening row: "the weakness is about Background register, not the Gap sentence's specificity" -- this describes the category boundary without naming what about the diagnosed weakness makes it non-Gap. The second-order shortcut satisfies C-37's structural requirement while bypassing its reasoning intent: a reader auditing such a row cannot distinguish the category boundary from the weakness-specific reasoning. The distinction: a C-39-compliant block names and prohibits only the first-order template form; a C-41-compliant block names and prohibits BOTH forms, explaining that the second-order form passes C-37's shape test while failing its auditable-reasoning requirement. A standalone block that closes only the first-order shortcut satisfies C-39 but not C-41.
- **Pass condition**: The per-excluded-category verification standalone rationale block explicitly names and prohibits the second-order category-mirroring shortcut (in addition to the first-order template shortcut required by C-39). The description of the second-order shortcut must be specific enough that a reader can identify a category-mirroring sentence by comparison -- e.g., it names the form ("a sentence that restates the category boundary without naming what about the diagnosed weakness makes it non-qualifying") and explains why that form fails auditable reasoning. A standalone block naming only the first-order `[confirmed]` shortcut does not satisfy C-41 even if C-39 is satisfied.

### C-42 -- Pre-Committed Self-Diagnosis Framework with Temporal Separation Before Phase 0
- **Weight**: aspirational
- **Category**: depth
- **Source**: R13 excellence signal V-05 Protocol III (C-24/C-34 above-ceiling -- "Protocol III pre-committed self-diagnosis framework -- positive search space targets and per-category format locked before Phase 0 when no draft exists, creating auditable temporal separation that closes post-hoc rationalization path"). C-34 is the "positive search space block with structural asymmetry argument" floor; C-42 is the "pre-committed self-diagnosis framework with auditable temporal separation" ceiling. C-42 extends C-34: the structural asymmetry argument is the prerequisite; temporal pre-commitment is the additional requirement.
- **Text**: The positive search space framework -- including specific positive search space targets and the per-category verification format for Amendment 1 -- must be declared BEFORE Phase 0, when no draft exists. Amendment 1 instructions must reference the pre-committed framework by name rather than defining targets inline at Phase 5. The temporal separation is auditable: the framework exists in the variation before any Phase 0 content; Amendment 1 cannot introduce or modify the framework after reading the draft. This closes the post-hoc rationalization path: a runtime-introduced positive search space framework (inline at Phase 5) can be constructed after reading the draft, making positive targets co-temporal with diagnosis; a pre-committed framework cannot be constructed post-draft, creating a verifiable temporal constraint. The distinction: a C-34-compliant variation includes the structural asymmetry argument at Amendment 1 time (Phase 5), where the framework is introduced as the self-diagnosis executes; a C-42-compliant variation locks the complete framework before Phase 0, so that when Amendment 1 executes it is referencing a fixed pre-committed document rather than selecting from an inline list. A self-diagnosis section with inline positive-space targets at Phase 5 satisfies C-34 but not C-42.
- **Pass condition**: The variation declares a named self-diagnosis framework (protocol, committed targets, or structurally equivalent) positioned before Phase 0 content, specifying: (a) the positive search space targets, and (b) the per-category verification format for Amendment 1. Amendment 1 instructions reference the pre-committed framework rather than defining or choosing targets inline at Phase 5. The pre-commitment must be positioned before any Phase 0 content, making the temporal separation verifiable. A self-diagnosis section embedded in Phase 5 with inline positive-space targets does not satisfy C-42 even if C-34 is satisfied.

### C-43 -- Inertia Declaration Names Phase Bundling as Fourth Canonical Cheap Path
- **Weight**: aspirational
- **Category**: format
- **Source**: R13 excellence signal V-03 (C-27 above-floor -- "V-03 adds a fourth (phase bundling) -- above C-27 floor"). C-27 is the "at least two of three canonical cheap paths named" floor; C-43 is the "all three canonical paths AND phase bundling named as a fourth" ceiling. C-43 extends C-27: per-path confirmation for the three canonical paths is the prerequisite; naming phase bundling as a fourth is the additional requirement.
- **Text**: The pre-Phase 0 inertia declaration block must name all three canonical execution-quality cheap paths (signal-skip, nominal gap framing, non-trivial gaming) AND a fourth: phase bundling -- the shortcut of aggregating individually-gated phases into a combined or unlabeled step (e.g., treating Phase 2a/2b/2c as a single "Phase 2" block, treating Phase 3 and Phase 3b as an unlabeled merge+verify pass). Phase bundling is structurally distinct from the three canonical paths: the original three target per-phase execution quality; phase bundling targets the structural commitment level -- it defeats C-36 and C-38 by preventing the commitment to individually named phase gates from being established at all. A four-path inertia declaration closes the gap that allows a model to confirm the three execution-quality shortcuts (satisfying C-27) while retaining the ability to bundle phases in the sequence lock without having declared it a shortcut. Mechanistic distinction from C-38: C-38 closes bundling via correct-sequence enumeration (what TO do in order -- naming each gate); C-43 closes bundling via named-shortcut prohibition (what NOT to do, pre-Phase 0 -- naming the error). Both close the bundling path through different cognitive commitment mechanisms. A declaration that names signal-skip, nominal gap framing, and non-trivial gaming without naming phase bundling satisfies C-27 but not C-43.
- **Pass condition**: The pre-Phase 0 inertia declaration block names phase bundling (coarse-grain aggregation of individually-gated phases into combined or unlabeled steps) as a named cheap path alongside the three canonical paths, with per-path confirmation for all four. The phase bundling confirmation must make explicit what the shortcut looks like -- e.g., treating Phase 2a/2b/2c as a combined "Phase 2" step, or treating Phase 3/3b as an unlabeled merge+verify block. A declaration that names only the three original canonical paths (satisfying C-27) without naming phase bundling as a fourth does not satisfy C-43.

### C-44 -- Complete Anti-Bundling Rationale Coverage at All Phase Transitions
- **Weight**: aspirational
- **Category**: format
- **Source**: R14 excellence signal V-01 C-38 above-floor ("rationale block explicitly addresses bundling at all eight other transitions beyond Phase 3/3b"). C-36 required the Phase 3/3b rationale block only; C-38 required complete phase enumeration but did not extend the rationale beyond Phase 3/3b; C-44 is the new ceiling ("anti-bundling rationale matched to the complete inventory"). C-44 extends C-38: complete phase enumeration is the prerequisite; rationale coverage at all transitions is the additional requirement.
- **Text**: The phase sequence lock rationale must cover ALL phase transitions in the complete inventory -- not only the Phase 3/3b pair mandated by C-36. C-36 named the Phase 3/3b rationale because Phase 3b requires Phase 3's merged paragraph as input; C-38 extended the sequence lock to name every phase individually; C-44 extends the rationale to match: each phase boundary in the complete inventory must be accompanied by an explanation of why that boundary is a meaningful gate rather than a silently aggregable step. The distinction: a C-38-compliant sequence lock names all nine phases individually and includes the Phase 3/3b rationale from C-36; a C-44-compliant sequence lock additionally addresses bundling at all eight non-Phase-3/3b transitions, naming the gate-specific input requirement or structural constraint at each boundary. C-38 closes the enumeration gap (all phases named); C-44 closes the justification gap: a model that lists all phases individually can still treat non-Phase-3/3b boundaries as arbitrary structural divisions whose rationale is assumed rather than stated -- no boundary is cognitively committed unless its gate-significance has been explicitly argued. A sequence lock that names all phases individually and includes the Phase 3/3b rationale block without extending rationale to other transitions satisfies C-38 but not C-44.
- **Pass condition**: The phase sequence lock rationale block addresses the anti-bundling argument at all phase transitions beyond Phase 3/3b. For each phase transition in the complete inventory beyond the Phase 3/3b pair, the rationale identifies the gate-specific reason that boundary cannot be silently merged: the input requirement, the structural constraint, or the commitment-device significance at that transition. A sequence lock that includes the Phase 3/3b rationale block but does not extend rationale coverage to other transitions does not satisfy C-44 even if C-38 is satisfied.

### C-45 -- Inter-Gate Input Dependency Declarations in Per-Gate Completion Conditions
- **Weight**: aspirational
- **Category**: format
- **Source**: R14 excellence signal V-02 C-36/C-40 above-ceiling ("Phase 3b completion condition explicitly references 'from the Phase 3 merged paragraph'"). C-40 is the "per-gate falsifiable completion conditions" floor; C-45 is the "inter-gate input dependency declarations" ceiling. C-46 (named pre-committed dependency protocol) is the ceiling above C-45 (v15). C-45 extends C-40: per-gate completion conditions are the prerequisite; source-gate declarations for output-dependent gates are the additional requirement.
- **Text**: Completion conditions for phases that consume a prior phase's output must name the SOURCE GATE by phase number -- not merely specify what is true when the gate closes. A C-40-compliant condition specifies "Phase 3b Complete when: bridge phrase verified in merged paragraph" (what is true at closure); a C-45-compliant condition adds the source declaration: "Phase 3b Complete when: bridge phrase verified in merged paragraph FROM PHASE 3 OUTPUT" (naming Phase 3 as the specific prior gate whose output is consumed). Per-gate source declarations convert the sequence lock from a LINEAR CHECKLIST (each gate's conditions self-contained) into an auditable DEPENDENCY GRAPH (each gate explicitly identifies which prior output it consumes). C-40 closes the implicit-completion gap; C-45 closes the anonymous-input gap: a model can satisfy C-40 by writing completion conditions that pass the falsifiability test without ever naming which prior phase must have completed -- the source dependency is assumed by position rather than declared by name. Making source gates explicit means a reader can audit not only that a gate's condition is met but that the required input traces unambiguously to the correct prior phase. A sequence lock with per-gate conditions that do not name source gates for output-dependent phases satisfies C-40 but not C-45.
- **Pass condition**: The phase sequence lock completion conditions include, for each phase that consumes output from a prior phase, an explicit reference to the source gate by name (e.g., "FROM Phase 3 output," "REQUIRES Phase 2b output," or equivalent phrasing that identifies the producing phase). The Phase 3b -> Phase 3 dependency must be present: Phase 3b's completion condition must name Phase 3 as the source of the required merged paragraph. At least two additional inter-gate dependencies beyond Phase 3b -> Phase 3 must also be named. A sequence lock that has per-gate completion conditions but does not name source gates for output-dependent phases does not satisfy C-45 even if C-40 is satisfied.

### C-46 -- Named Pre-Committed Source-Gate Dependency Protocol Declared Before Phase 0
- **Weight**: aspirational
- **Category**: format
- **Source**: R15 excellence signal V-05 C-45 above-ceiling ("Protocol II completion conditions carry `(Source gate: Phase X per Protocol V.)` inline references for all output-dependent phases, naming the producing phase explicitly. Phase 3b: '(Source gate: Phase 3 per Protocol V. Extracts CANNOT be written before Phase 3 produces the merged text.)'"). C-45 is the "inter-gate input dependency declarations inline in per-gate conditions" floor; C-46 is the "named pre-committed dependency protocol with temporal separation" ceiling. C-46 extends C-45: per-gate source declarations are the prerequisite; organization as a named pre-committed protocol positioned before Phase 0 is the additional requirement.
- **Text**: The inter-gate source dependencies declared per-gate in C-45 must be organized into a named pre-committed protocol (Protocol V or structurally equivalent) positioned before Phase 0 -- not only appended as inline annotations within Protocol II's per-gate completion conditions. A C-45-compliant variation declares source gates inline: `*[Source: FROM Phase X output]*` appended to each output-dependent completion condition within Protocol II; a C-46-compliant variation declares a separate named protocol (Protocol V: Source-Gate Dependency Registry, or equivalent) before Phase 0, and Protocol II's completion conditions cite that protocol by name: `(Source gate: Phase X per Protocol V.)`. The pre-committed protocol captures the full dependency graph as an auditable artifact that exists before any Phase content: when Protocol II's completion conditions cite it, the dependency structure is fixed prior to Phase 0 rather than assembled at the point of use. This closes the runtime-rationalization gap for dependency declarations: a C-45-compliant variation can construct its inline source declarations after reading the variation's phase structure, making source gates co-temporal with the sequence lock; a pre-committed Protocol V cannot be constructed post-hoc, creating a verifiable temporal constraint equivalent to what C-42 establishes for the self-diagnosis framework. The CANNOT-exist reasoning for output-dependent phases (e.g., "Extracts CANNOT be written before Phase 3 produces the merged text") appears in the Protocol V entry itself rather than only in a rationale block, making the impossibility argument part of the pre-committed dependency declaration. The distinction: a C-45-compliant variation converts the sequence lock into a dependency graph via inline source annotations; a C-46-compliant variation elevates the dependency graph to a named pre-committed protocol analogous to Protocol III for self-diagnosis. A variation with inline source declarations satisfies C-45 but not C-46.
- **Pass condition**: The variation declares a named source-gate dependency protocol (Protocol V or structurally equivalent) positioned before Phase 0, listing each inter-gate dependency with the source gate identified by name and, for output-dependent phases, the CANNOT-exist reasoning. Protocol II's per-gate completion conditions cite the pre-committed protocol by name rather than embedding the dependency declaration inline. The pre-commitment must be positioned before any Phase 0 content. At minimum, the Phase 3b -> Phase 3 dependency entry must appear in Protocol V with the CANNOT-exist reasoning ("Phase 3b's required input CANNOT exist before Phase 3 produces the merged paragraph"). A variation with inline source-gate annotations not organized as a named pre-Phase 0 protocol does not satisfy C-46 even if C-45 is satisfied.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                                                        |
|--------------|-----------------|--------|-----------------------------------------------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                                                                   |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                                                     |
| Aspirational | C-10 to C-46    | 38     | Separates good from excellent. C-26, C-27, C-29, C-34, C-36 through C-46 are the ceiling layer.                      |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v14

| Change              | Detail |
|---------------------|--------|
| C-45 source updated | C-46 (named pre-committed source-gate dependency protocol) is the new ceiling above C-45 in v15. C-45 remains active (not confirmed universally passing in R15: V-01 fails C-45 by design). |
| C-40 source updated | C-46 is now the fifth ceiling in the sequence lock conditions chain (C-27 -> C-36 -> C-38 -> C-40 -> C-45 -> C-46). |
| C-38 source updated | C-46 referenced as fifth ceiling in conditions branch. |
| C-36 source updated | C-46 referenced as fifth ceiling in conditions branch. |
| C-27 source updated | C-46 is now the fifth sequence-lock conditions ceiling. |
| C-46 added          | Named pre-committed source-gate dependency protocol declared before Phase 0 -- from R15 V-05 C-45 above-ceiling signal. 2 pts. Extends C-45 inline-annotation floor by requiring source dependencies to be organized as a named pre-committed protocol (Protocol V) that Protocol II completion conditions cite by reference, closing the runtime-rationalization gap for dependency declarations. |
| Tier description    | Updated to reflect C-10 to C-46 aspirational range; ceiling layer is now C-26, C-27, C-29, C-34, C-36 through C-46. |
| Aspirational subtotal | Moves to 38 pts. Total moves to 118. No retirements this round (C-36 through C-45 not confirmed universally passing in R15 -- isolation variations by design fail specific ceiling criteria). |

---

**Design notes:**

- **Thirteen criteria retired across v3-v11**: C-09 (v7), C-16 (v7), C-11/C-12/C-14/C-15/C-17/C-18 (v8), C-28/C-30 (v9), C-25/C-31/C-32 (v10), C-33/C-35 (v11). Pattern: retirement when universally passing AND a structurally stronger ceiling covers the same behavior.
- **Floor/ceiling chain integrity**: C-21->C-22 (coupling), C-20->C-23->C-26->C-29 (bridge lifecycle), C-07->C-24->C-34->C-42 / C-24->C-37->C-39->C-41 (self-diagnosis, two ceiling branches), C-27->C-36->C-38->C-40->C-45->C-46 / C-27->C-36->C-38->C-44 / C-27->C-43 (sequence lock, two branches from C-38 plus declaration-completeness branch). The conditions branch now extends to five ceilings: C-38->C-40->C-45->C-46.
- **C-46 structural logic**: Follows the C-34->C-42 protocol-elevation pattern. C-34: structural asymmetry argument inline at Phase 5 (runtime). C-42: same argument pre-committed as Protocol III before Phase 0 (temporal separation). C-45: source-gate declarations inline in per-gate completion conditions (runtime annotations). C-46: same declarations pre-committed as Protocol V before Phase 0 (named dependency registry, temporal separation). The pattern closes the same runtime-rationalization gap each time it is applied: an inline declaration can be constructed co-temporally with the artifact it annotates; a named pre-committed protocol cannot. C-42 applies this to self-diagnosis targets; C-46 applies it to inter-gate dependencies.
- **Protocol taxonomy**: Protocols I through V each close a distinct shortcut category at the pre-commitment level. Protocol I: inertia declaration (C-27/C-43). Protocol II: phase sequence lock with per-gate conditions (C-36->C-40). Protocol III: pre-committed self-diagnosis framework (C-42). Protocol IV: not named in the variation taxonomy (Phase 3b rationale block from C-36 is embedded in Protocol II). Protocol V: source-gate dependency registry (C-46). Each protocol names what cannot be done at runtime; the completion conditions, amendment pass, and per-excluded-category verification then cite the pre-committed constraints.
- **R15 synthesis context**: R15 was designed as the synthesis round for C-44 and C-45 (the two v14 additions). V-01 through V-04 confirmed the C-44 and C-45 isolation and synthesis patterns. V-05 introduced Protocol V as an above-ceiling probe on C-45, demonstrating that source-gate declarations can be elevated from inline annotations to a named pre-committed dependency protocol -- extracting C-46. The above-ceiling signal appeared in the dedicated above-ceiling probe variation (V-05), consistent with above-ceiling behavior emerging when a single criterion is implemented with maximal thoroughness.
- **R16 synthesis target**: A variation that clears all eleven active ceiling criteria simultaneously (C-36, C-37, C-38, C-39, C-40, C-41, C-42, C-43, C-44, C-45, C-46) -- combining the R15 synthesis base (V-04) with Protocol V as a named pre-Phase 0 dependency registry that Protocol II completion conditions cite by reference.
- **Point total progression**: v12 moved to 104 (C-38/C-39 added). v13 moved to 112 (C-40/C-41/C-42/C-43 added). v14 moved to 116 (C-44/C-45 added). v15 moves to 118 (C-46 added, no retirements because C-36 through C-45 not confirmed universally passing with isolation variations by design failing specific criteria in R15).
- **C-29 unchanged**: The two-sided CAN + CANNOT asymmetry requirement continues universally passing. No new ceiling needed.
- **C-34/C-42 status**: Both universally passing in R15 visible data. Neither retired because retirement requires full 5-variation confirmation with no isolation design that omits them.
