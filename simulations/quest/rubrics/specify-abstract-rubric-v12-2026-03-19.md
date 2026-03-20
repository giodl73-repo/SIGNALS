**v12 written** to `simulations/quest/rubrics/specify-abstract-rubric-v12-2026-03-19.md`.

---

**Two new criteria extracted from R12:**

| ID | Name | Extends | Pts | Source |
|----|------|---------|-----|--------|
| C-38 | Complete sub-phase inventory in phase sequence lock | C-36 | 2 | R12 V-01 |
| C-39 | Standalone rationale block in per-excluded-category verification names and closes shortcut mechanism | C-37 | 2 | R12 V-02 |

**Evidence basis:**
- **C-38** from V-01's C-36 pass: "Nine individually named sub-phases." C-36 requires Phase 3/3b specifically; V-01 names all nine. The new ceiling closes the bundling shortcut at ALL phases, not just the merge pair.
- **C-39** from V-02's C-37 pass: "[confirmed] shortcut explicitly closed; '*Why specific per-row sentences matter:*' rationale present." C-37 requires weakness-specific sentences; V-02 also includes a standalone block that names the `[confirmed]` template form and prohibits it by instruction. The new ceiling closes the compliance-by-default path — a model can accidentally produce weakness-specific sentences without the instruction explicitly prohibiting the shortcut.

**Point math:** No retirements (C-36 fails in V-02, C-37 fails in V-01). +4 pts net. Aspirational: 20 → 24. Total: 100 → 104.

**Chain updates:**
- Inertia: `C-27 -> ~~C-33~~ -> C-36 -> C-38`
- Self-diagnosis exclusion: `C-24 -> ~~C-35~~ -> C-37 -> C-39`

**V-08 synthesis target for R13:** Combine C-38 (complete sub-phase inventory) + C-39 (named-shortcut rationale block) while passing C-36, C-37, and C-34.
se sequence lock** (2 pts, format)
C-36 is the "sub-phase canonical naming with structural rationale block" floor (Phase 3/3b individually named with rationale); C-38 is the new ceiling ("complete sub-phase inventory"). C-36 requires Phase 3 (merge) and Phase 3b (integration verification) to be named as individually gated sub-phases with a structural rationale block explaining the gate dependency; C-38 requires ALL phases in the sequence lock to be individually named as sub-phase gates -- not just the Phase 3/3b pair. A sequence lock that names every phase as an individually gated unit provides a structural inventory that makes any coarse-grain bundling visible: a reader can verify at a glance that no two phases have been silently combined or aggregated under a shared label. The distinction: a C-36-compliant lock names Phase 3 and Phase 3b individually and may aggregate other phases (e.g., "Phase 0 through Phase 2" as a block) without per-phase enumeration; a C-38-compliant lock names every phase as a separately gated unit so that the full commitment inventory is explicit at Phase 0. Complete sub-phase inventory closes the remaining bundling shortcut at phases other than 3/3b: a model that aggregates Phase 1 and Phase 2 retains the same coarse-grain structure that C-36 closes for Phase 3/3b, applied elsewhere in the sequence. A sequence lock that names Phase 3 and Phase 3b individually but bundles other phases satisfies C-36 but not C-38. Source: R12 V-01, C-38 excellence signal ("Nine individually named sub-phases").

**C-39 -- Standalone rationale block in per-excluded-category verification names and closes shortcut mechanism** (2 pts, depth)
C-37 is the "weakness-specific per-row reasoning" floor; C-39 is the new ceiling ("standalone rationale block naming and closing shortcut mechanism"). C-37 requires each row to contain a self-contained sentence naming the diagnosed weakness and stating why it falls outside that category; C-39 requires a dedicated standalone rationale block ("*Why specific per-row sentences matter:*" or structurally equivalent) that (a) explicitly names the template shortcut path ("[confirmed / explain if uncertain]" or equivalent form), (b) explains why template confirmation fails the verification requirement, and (c) declares the weakness-specific sentence as the required form. The distinction: a C-37-compliant variation can satisfy the per-row sentence requirement without ever explicitly naming or prohibiting the template form -- a reader auditing per-row entries can verify they are weakness-specific, but the variation itself may not have closed the shortcut by name; a C-39-compliant variation includes a standalone block that names the shortcut and explains why it is structurally insufficient, so that a model following the instruction knows the shortcut is prohibited, not merely absent. C-39 closes the compliance-by-default path: a model can accidentally produce weakness-specific sentences without understanding why the template form fails; the standalone rationale ensures the prohibition is instructed rather than implicit. A variation that has weakness-specific per-row sentences without a standalone named-shortcut rationale block satisfies C-37 but not C-39. Source: R12 V-02, C-39 excellence signal ("[confirmed] shortcut explicitly closed; '*Why specific per-row sentences matter:*' rationale present").

---

## Point Redistribution (Aspirational moves to 24, total moves to 104)

| Criterion | Change | Reason |
|-----------|--------|--------|
| C-36 | no change | Not universally passing in R12: V-02 fails C-36. Ceiling remains active. |
| C-37 | no change | Not universally passing in R12: V-01 fails C-37. Ceiling remains active. |
| C-38 | +2 pts | New (complete sub-phase inventory in phase sequence lock). |
| C-39 | +2 pts | New (standalone rationale block in per-excluded-category verification names and closes shortcut mechanism). |

**C-38 extends C-36**: C-36 required Phase 3 and Phase 3b to be individually named as sub-phase gates with a structural rationale block explaining the Phase 3 -> Phase 3b dependency; C-38 requires ALL phases in the sequence lock to be individually named. All C-38-passing variations pass C-36; not all C-36-passing variations pass C-38 (V-01 R12 names nine individual sub-phases; a variation that names only Phase 3/3b and aggregates the rest satisfies C-36 but not C-38).

**C-39 extends C-37**: C-37 required per-row sentences naming the actual diagnosed weakness; C-39 requires a dedicated standalone rationale block that explicitly names and prohibits the template shortcut. All C-39-passing variations pass C-37; not all C-37-passing variations pass C-39 (V-02 R12 includes the "*Why specific per-row sentences matter:*" block with explicit shortcut closure; a variation that has weakness-specific rows without this named-prohibition block satisfies C-37 but not C-39).

**Aspirational subtotal**: Moves to 24 pts. Total moves to 104.

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

Aspirational check: 1+1+1+1+1+1+1+1+2+2+2+2+2+2+2+2 = **24**

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

## Aspirational Criteria (24 points total)

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
- **Source**: R5 excellence signal V-03. Reduced 2->1 pt in v7 -- universally passing R6; C-25 (categorical novelty, retired v10) was the mid in v7-v9; C-35 (per-excluded-category verification, retired v11) was the mid in v10; C-37 (weakness-specific per-row reasoning) is the first ceiling above C-24; C-39 (standalone rationale block naming shortcut) is the new second ceiling above C-37 added in v12.
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
- **Source**: R6 excellence signal V-02 (inertia commitment device). No prior criterion equivalent -- structurally new pre-Phase 0 lifecycle position. C-32 (named-per-path gate) retired in v10; C-33 (phase sequence lock) retired in v11; C-36 (sub-phase canonical naming) is the current ceiling; C-38 (complete sub-phase inventory) is the new ceiling above C-36 added in v12; C-27 remains the per-path confirmation floor.
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
- **Source**: R10 excellence signal V-02 (E-02 pattern, asymmetry argument). C-24 is the "diagnosis targets weakest element" floor; C-31 (dedicated named block) was the mid (retired v10 -- universally passing all R10 variations); C-34 is the ceiling ("structural asymmetry argument inside the dedicated block"). C-34 extends C-31: the dedicated block exists AND contains the causal argument. No new ceiling added in v11 or v12 -- C-34 remains the aspirational ceiling for the positive-search-space branch.
- **Text**: The `*Where to look instead -- positive search space:*` block (or structurally equivalent block) must contain not only an enumeration of non-fixed diagnostic targets but a structural argument explaining why the surviving weakness is asymmetrically more likely to appear outside the fixed amendment categories. The argument names the causal mechanism: the four fixed amendment categories are pre-committed correction targets that Amendments 2-4 address in a predictable pass; any weakness they address is already on a correction path before Amendment 1 executes; therefore, the self-diagnosis pass is structurally biased toward surfacing a weakness in a category that no fixed amendment targets. Enumerating positive search space targets (satisfies the retired C-31) identifies where to look; the asymmetry argument explains why looking there is structurally motivated -- the surviving weakness cannot be in a pre-committed category because those categories are being corrected regardless of what self-diagnosis finds. Without the asymmetry argument, the positive search space list is advisory; with it, the list is causally grounded.
- **Pass condition**: The positive search space block (dedicated, with its own label) contains a structural argument naming the pre-commitment mechanism as the reason for the asymmetric bias toward non-fixed categories. The argument must identify the four fixed categories as pre-committed targets and explain that the surviving weakness is therefore structurally more likely to appear outside them. A block that enumerates diagnostic targets without this causal argument does not satisfy C-34 even if C-31 (retired) would have been satisfied.

### C-36 -- Sub-Phase Canonical Naming in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R11 excellence signal V-01 (C-36 pattern, sub-phase canonical naming). C-27 is the "per-path confirmation" floor; C-33 (phase sequence lock) was the mid (retired v11 -- universally passing all R11 variations); C-36 is the "sub-phase canonical naming with structural rationale block" ceiling. C-38 (complete sub-phase inventory) is the new ceiling above C-36 added in v12.
- **Text**: The phase sequence lock (at the aggregation gate closure) must enumerate Phase 3 (merge) and Phase 3b (integration verification) as individually named sub-phase gates and include a structural rationale block ("*Why sub-phase canonical naming matters*" or structurally equivalent) explaining the Phase 3 -> Phase 3b gate dependency. The rationale names the causal mechanism: Phase 3b requires the merged paragraph as input; a model that treats Phase 3 and Phase 3b as a combined or unlabeled step retains the pre-fill shortcut of filling the Phase 3b integration column before the merge has been executed -- the same pre-fill window that C-26 and C-29 were designed to close at the verification stage. Sub-phase canonical naming at the sequence lock stage closes this window at the commitment level: the model commits before Phase 0 that Phase 3b is a named sub-phase gate requiring Phase 3 output, making the pre-fill shortcut structurally blocked from the start rather than only detectable post-hoc. A sequence lock that lists all phases including Phase 3 and Phase 3b without a sub-phase rationale block satisfies the retired C-33 but not C-36.
- **Pass condition**: The phase sequence lock includes Phase 3 and Phase 3b named as individually gated sub-phases AND a structural rationale block explaining the Phase 3 -> Phase 3b gate dependency in terms of the pre-fill window that C-26/C-29 close at the verification stage. The rationale must identify the causal mechanism (Phase 3b requires post-merge text as input) and state why sub-phase naming at the commitment stage closes the shortcut earlier than verification-stage guards alone. A sequence lock that enumerates the phases without this rationale block does not satisfy C-36 even if C-33 (retired) would have been satisfied.

### C-37 -- Weakness-Specific Per-Row Reasoning in Per-Excluded-Category Verification
- **Weight**: aspirational
- **Category**: depth
- **Source**: R11 excellence signal V-02 (C-37 pattern, weakness-specific per-row reasoning). C-24 is the "diagnosis targets weakest element" floor; C-35 (per-excluded-category verification) was the mid (retired v11 -- universally passing all R11 variations); C-37 is the "weakness-specific per-row reasoning" ceiling. C-39 (standalone rationale block naming and closing shortcut mechanism) is the new ceiling above C-37 added in v12.
- **Text**: The per-excluded-category verification table must contain, in each row, a sentence that names the actual diagnosed weakness and states specifically why that weakness is not an instance of the category -- not a template parenthetical describing the category boundary with "[confirmed / explain if uncertain]". The distinction: a C-35-compliant row can be written as "Gap sharpening: N -- [the named weakness does not target the Gap sentence's specificity: confirmed]" using the category-description template; a C-37-compliant row requires "Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]" where the sentence is self-contained and weakness-grounded. A reader auditing a C-37-compliant row can verify the exclusion from the row alone, without cross-referencing the category label or trusting a template confirmation. The "confirmed" shortcut path closes the per-row form requirement (C-35) without reasoning about the specific weakness; C-37 closes this shortcut by requiring the weakness to be named and the per-row reason to be stated as a distinct sentence referencing the actual weakness.
- **Pass condition**: The per-excluded-category verification table includes one row per fixed category (Gap sharpening, Result quantification, Implication tightening, Prose coherence), each row containing an N and a self-contained sentence that names the diagnosed weakness and states why it falls outside that specific category. A row using a template category-description parenthetical with "confirmed" does not satisfy C-37 even if C-35 (retired) would have been satisfied. At least three of the four rows must contain weakness-specific sentences; a row that restates the category boundary without naming the weakness fails.

### C-38 -- Complete Sub-Phase Inventory in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R12 excellence signal V-01 (C-38 pattern, complete sub-phase inventory -- "Nine individually named sub-phases"). C-36 is the "Phase 3/3b individually named with structural rationale block" floor; C-38 is the new ceiling ("complete sub-phase inventory"). C-38 extends C-36: the sequence lock names Phase 3 and Phase 3b AND names every other phase individually.
- **Text**: The phase sequence lock must enumerate ALL phases as individually named sub-phase gates -- not just the Phase 3/3b pair. A complete sub-phase inventory makes any coarse-grain bundling visible: a reader can verify at a glance that no two phases have been silently combined or aggregated under a shared label. The distinction: a C-36-compliant lock names Phase 3 and Phase 3b individually and may aggregate other phases (e.g., treating Phase 0 through Phase 2 as a pre-execution block) without per-phase enumeration; a C-38-compliant lock names every phase as a separately gated unit so that the full commitment inventory is explicit before Phase 0. Complete sub-phase inventory closes the bundling shortcut at phases other than 3/3b: a model that aggregates earlier phases retains the coarse-grain structure that C-36 closes for the merge pair, applied elsewhere. A sequence lock that names Phase 3 and Phase 3b individually but bundles other phases satisfies C-36 but not C-38.
- **Pass condition**: The phase sequence lock enumerates every phase in the skill's execution sequence as an individually named gate unit -- no two phases are bundled under a shared label or aggregated. The Phase 3/3b sub-phase structure required by C-36 must also be present. A lock that names Phase 3 and Phase 3b but aggregates other phases (e.g., "Phase 0 through Phase 2 -- pre-execution setup") does not satisfy C-38 even if C-36 is satisfied.

### C-39 -- Standalone Rationale Block in Per-Excluded-Category Verification Names and Closes Shortcut Mechanism
- **Weight**: aspirational
- **Category**: depth
- **Source**: R12 excellence signal V-02 (C-39 pattern -- "[confirmed] shortcut explicitly closed; '*Why specific per-row sentences matter:*' rationale present"). C-37 is the "weakness-specific per-row reasoning" floor; C-39 is the new ceiling ("standalone rationale block naming and closing shortcut mechanism"). C-39 extends C-37: the per-row sentences are weakness-specific AND a dedicated rationale block explicitly names and prohibits the template shortcut.
- **Text**: The per-excluded-category verification section must include a standalone rationale block ("*Why specific per-row sentences matter:*" or structurally equivalent) that (a) explicitly names the template shortcut path ("[confirmed / explain if uncertain]" or equivalent form), (b) explains why template confirmation fails the verification requirement -- specifically, that a template parenthetical describes the category boundary without referencing the diagnosed weakness, making it impossible to audit the exclusion from the row alone, and (c) declares the weakness-specific sentence as the required form. The distinction: a C-37-compliant variation can satisfy the per-row sentence requirement without ever explicitly naming or prohibiting the template form -- a reader auditing per-row entries can verify they are weakness-specific, but the variation itself may not have instructed the model that the shortcut is closed; a C-39-compliant variation includes a standalone block that names the shortcut and explains its structural insufficiency, ensuring the prohibition is instructed rather than incidentally absent. A variation that has weakness-specific per-row sentences without a standalone named-shortcut rationale block satisfies C-37 but not C-39.
- **Pass condition**: The per-excluded-category verification section includes a standalone rationale block that (1) names the "[confirmed / explain if uncertain]" template form (or equivalent) by name or close paraphrase, (2) explains why the template form is insufficient -- the category-description parenthetical does not reference the diagnosed weakness -- and (3) declares the self-contained weakness-specific sentence as the required per-row form. A variation that has weakness-specific rows without this standalone named-shortcut rationale block does not satisfy C-39 even if C-37 is satisfied.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                                                        |
|--------------|-----------------|--------|-----------------------------------------------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                                                                   |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                                                     |
| Aspirational | C-10 to C-39    | 24     | Separates good from excellent. C-26, C-27, C-29, C-34, C-36, C-37, C-38, C-39 are the ceiling layer.                |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v11

| Change              | Detail |
|---------------------|--------|
| C-36 source updated | C-38 (complete sub-phase inventory) is the new ceiling above C-36 in v12. C-36 remains active (not universally passing in R12: V-02 fails C-36). |
| C-37 source updated | C-39 (standalone rationale block naming shortcut) is the new ceiling above C-37 in v12. C-37 remains active (not universally passing in R12: V-01 fails C-37). |
| C-27 source updated | C-38 (complete sub-phase inventory) is the new ceiling in the inertia chain; C-27 remains the per-path confirmation floor. |
| C-24 source updated | C-39 (standalone rationale block naming shortcut) is the new second ceiling above C-37 in the self-diagnosis exclusion chain; C-24 remains the floor. |
| C-34 source updated | No new ceiling added in v12 for the positive-search-space branch -- C-34 remains the aspirational ceiling for that branch. |
| C-38 added          | Complete sub-phase inventory in phase sequence lock -- from R12 V-01 signal. 2 pts. Full-inventory ceiling above the C-36 Phase 3/3b-minimum floor. |
| C-39 added          | Standalone rationale block in per-excluded-category verification names and closes shortcut mechanism -- from R12 V-02 signal. 2 pts. Named-shortcut-prohibition ceiling above the C-37 weakness-specific-sentences floor. |
| Tier description    | Updated to reflect C-10 to C-39 aspirational range; ceiling layer is now C-26, C-27, C-29, C-34, C-36, C-37, C-38, C-39. |
| Aspirational subtotal | Moves to 24 pts. Total moves to 104. No retirements this round (C-36 and C-37 are not universally passing in R12). |

---

**Design notes:**

- **Thirteen criteria retired across v3-v11**: C-09 (v7), C-16 (v7), C-11/C-12/C-14/C-15/C-17/C-18 (v8), C-28/C-30 (v9), C-25/C-31/C-32 (v10), C-33/C-35 (v11). Pattern: retirement when universally passing AND a structurally stronger ceiling covers the same behavior.
- **Floor/ceiling chain integrity**: C-21->C-22 (coupling), C-20->C-23->C-26->C-29 (bridge lifecycle), C-07->C-24->C-34/C-37->C-39 (self-diagnosis), C-27->C-36->C-38 (inertia lifecycle). The self-diagnosis chain has two ceiling branches sharing the C-24 floor: the positive-search-space branch (C-24->C-34) and the per-excluded-category branch (C-24->C-37->C-39). The inertia chain now has two active ceilings: C-36 (Phase 3/3b sub-phase naming with rationale) and C-38 (complete inventory of all phases).
- **C-38/C-39 structural logic**: Both follow the v12 pattern -- a v11 criterion established a reasoning layer requiring a specific form (sub-phase naming for Phase 3/3b / weakness-specific sentences per row); the v12 ceiling requires that the same layer also include an explicit standalone rationale block that names the shortcut it closes. C-38: sequence lock names Phase 3/3b AND names all other phases individually (no bundling anywhere). C-39: per-category rows are weakness-specific AND a dedicated rationale block names the "[confirmed]" template form and prohibits it explicitly (named-shortcut closure, not merely-absent shortcut).
- **V-08 synthesis target**: No single R12 variation satisfies both new ceilings simultaneously. V-01 R12 passes C-36 and C-38, fails C-37 and C-39. V-02 R12 passes C-37 and C-39, fails C-36 and C-38. A next-generation synthesis variation for R13 would combine complete sub-phase inventory (C-38) with weakness-specific per-row reasoning plus standalone named-shortcut rationale (C-39), while retaining the positive-search-space asymmetry argument (C-34).
- **C-34 status**: The positive-search-space asymmetry argument branch (C-24 -> C-34) has no new R12 ceiling. All R12 variations pass C-34. If R13 generates a variation that extends the asymmetry argument further (e.g., pre-declaring positive-space targets at commitment time rather than at Amendment 1 execution time), a C-40 ceiling would be warranted in v13.
- **Point total above 100**: v12 is the first version where the total exceeds 100 (104 pts). This reflects two rounds of additions with different net effects: v11 retired C-33/C-35 and added C-36/C-37 (net 0); v12 adds C-38/C-39 with no retirements because C-36 and C-37 are not yet universally passing (net +4). If R13 produces C-36 and C-37 as universally passing, retiring them (-4) while adding R13 ceiling criteria (+4) would restore balance.
- **C-29 unchanged**: The two-sided CAN + CANNOT asymmetry requirement (tightened in v9) continues to differentiate in R12. All R12 variations carry both sides; no new ceiling is needed this round.
