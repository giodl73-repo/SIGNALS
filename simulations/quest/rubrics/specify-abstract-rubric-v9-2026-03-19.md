**v9 written** to `simulations/quest/rubrics/specify-abstract-rubric-v9-2026-03-19.md`.

---

## What changed

**Two new criteria extracted from R8:**

| ID | Name | Source | Pts |
|----|------|--------|-----|
| C-31 | Self-diagnosis positive search space given as a dedicated named block | R8 V-02 -- separate `*Where to look instead -- positive search space:*` block, structurally distinct from the Why block | +2 |
| C-32 | Inertia aggregation gate names each canonical path at the closure event | R8 V-03 -- "Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed." embeds canonical terms at the gate itself | +2 |

**Two criteria retired (-4 pts):**
- **C-28** retired — universally passing in all R8 variations; C-31 is the new ceiling (dedicated block vs embedded)
- **C-30** retired — universally passing in all R8 variations; C-32 is the new ceiling (named-per-path vs anonymous gate)

**One criterion tightened:**
- **C-29** pass condition now requires *both sides* of the asymmetry — CAN-side (Y/N can be prefilled before merge) and CANNOT-side (verbatim text cannot exist before merge). R8 V-02/V-03 revealed that CANNOT-only form was a subthreshold compliance path that v8's written condition didn't explicitly exclude.

**Chain structure:** C-24 -> C-25 -> **C-31** (self-diagnosis) | C-27 -> **C-32** (inertia) | C-23 -> C-26 -> C-29 (bridge, unchanged)

**V-04 synthesis target**: No R8 variation satisfies all three ceilings. V-01 passes C-29, fails C-31/C-32. V-02 passes C-31, fails C-29/C-32. V-03 passes C-32, fails C-29/C-31.
erated, embedded"); C-31 is the ceiling ("dedicated labeled block for the positive search space"). The Amendment 1 positive search space instruction must appear as a separately labeled block -- distinct from the Why block that accompanies the exclusion constraint. A block with its own header such as `*Where to look instead -- positive search space:*` separates the two cognitive tasks: the Why block explains why fixed categories are excluded; the positive-space block names where to look instead. Embedding the positive targets inside the Why block satisfies C-28; a dedicated block satisfies C-31 by making the diagnostic target list structurally independent of the constraint rationale. Without separation, a reader can satisfy both tasks in a single pass; with separation, the positive search space becomes an independently auditable component. Source: R8 V-02 signal, E-01 excellence pattern.

**C-32 -- Inertia aggregation gate names each canonical path at the closure event** (2 pts, format)
C-30 is the floor ("per-path confirmations + named aggregation gate"); C-32 is the ceiling ("named-per-path gate"). The aggregation gate line must name all three canonical cheap paths at the closure event itself -- "Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. All three canonical paths confirmed and closed. Proceed to Phase 0." or a structurally equivalent formulation. An anonymous gate ("All three paths closed. Proceed.") satisfies C-30 by generating an active closure signal; a named-per-path gate satisfies C-32 by embedding the canonical terms at the gate event, not only at the per-path confirmation lines. When the canonical names appear at closure, the gate itself serves as a checklist summary: a reader auditing the gate can confirm which paths were checked without scanning back through the per-path lines. Source: R8 V-03 signal, E-02 excellence pattern.

---

## Point Redistribution (Aspirational stays at 20, total stays at 100)

| Criterion | Change | Reason |
|-----------|--------|--------|
| C-28 | retired | Universally passing in all three R8 variations (V-01, V-02, V-03). C-31 is the new dedicated-block ceiling; C-28 as "exclusion constraint + enumerated positive search space (embedded)" is expectation, not achievement. |
| C-30 | retired | Universally passing in all three R8 variations. C-32 is the new named-per-path ceiling; C-30 as "per-path confirmations + anonymous aggregation gate" is expectation, not achievement. |
| C-31 | +2 pts | New (self-diagnosis positive search space given as a dedicated named block). |
| C-32 | +2 pts | New (inertia aggregation gate names each canonical path at the closure event). |

**C-31 extends C-28**: C-28 requires the exclusion constraint plus enumerated positive targets; C-31 requires those targets in a separately labeled block. All C-31-passing variations pass C-28; not all C-28-passing variations will pass C-31 (V-01 embeds targets in the Why block and fails C-31).

**C-32 extends C-30**: C-30 requires per-path confirmations plus a named aggregation gate; C-32 requires the gate to name each path at the closure event. All C-32-passing variations pass C-30; not all C-30-passing variations will pass C-32 (V-01/V-02 use an anonymous gate and fail C-32).

**Aspirational subtotal**: Remains 20 pts. Total remains 100.

---

## Criteria Summary Table

| ID   | Name                                                                         | Weight       | Category    | Points |
|------|------------------------------------------------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present                                                   | essential    | correctness | 10     |
| C-02 | Word count within target                                                     | essential    | correctness | 10     |
| C-03 | Artifact written to correct path                                             | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal                                                  | essential    | correctness | 10     |
| C-05 | Signal acquisition executed                                                  | essential    | behavior    | 10     |
| C-06 | Result section is quantified                                                 | recommended  | depth       | 10     |
| C-07 | Amendment pass produces three distinct                                       | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly                                            | recommended  | correctness | 10     |
| C-10 | Abstract reads as a single coherent paragraph                                | aspirational | format      | 1      |
| C-13 | Amendment non-triviality guard applied                                       | aspirational | depth       | 1      |
| C-19 | Paper type governs all six section registers                                 | aspirational | depth       | 1      |
| C-20 | Semantic bridge type constrained vocabulary                                  | aspirational | format      | 1      |
| C-21 | Section coupling verified before bridge                                      | aspirational | depth       | 1      |
| C-22 | Coupling revision uses structured directive format                           | aspirational | depth       | 1      |
| C-23 | Bridge integration verified post-merge                                       | aspirational | format      | 1      |
| C-24 | Self-diagnosis amendment targets weakest element                             | aspirational | depth       | 1      |
| C-25 | Self-diagnosis names weakness outside fixed categories                       | aspirational | depth       | 2      |
| C-26 | Bridge integration column cites actual merged prose                          | aspirational | format      | 2      |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0               | aspirational | format      | 2      |
| C-29 | Bridge integration format change accompanied by structural rationale         | aspirational | format      | 2      |
| C-31 | Self-diagnosis positive search space given as a dedicated named block        | aspirational | depth       | 2      |
| C-32 | Inertia aggregation gate names each canonical path at the closure event      | aspirational | format      | 2      |

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
- **Source**: R6 excellence signal V-02 (inertia commitment device). No prior criterion equivalent -- structurally new pre-Phase 0 lifecycle position. C-30 (anonymous aggregation gate) retired in v9; C-32 (named-per-path gate) is the new ceiling; C-27 remains the per-path confirmation floor.
- **Text**: A pre-Phase 0 inertia declaration block names at least two of the three canonical cheap paths and requires explicit model confirmation before proceeding to Phase 0: (1) signal-skip -- running without executing the Phase 1 glob; (2) nominal gap framing -- writing a research goal instead of a field-state gap; (3) non-trivial gaming -- using cosmetic Before/After edits that pass the guard format without substantive improvement. The block must appear before Phase 0 and must require a per-path confirmation for each named path. C-05/C-04/C-13 are the execution-point scoring floors; C-27 is the pre-execution commitment device above those floors.
- **Pass condition**: Output includes a pre-Phase 0 block that explicitly names at least two canonical cheap paths (signal-skip, nominal gap framing, non-trivial gaming) with a per-path confirmation for each named path. A general statement ("I will execute all phases diligently") does not satisfy C-27. The block must be positioned before any Phase 0 content.

### C-29 -- Bridge Integration Format Change Accompanied by Structural Rationale
- **Weight**: aspirational
- **Category**: format
- **Source**: R7 excellence signal V-01/V-04 (E-03 pattern, pre-fill impossibility argument). C-26 is the "quoted extract required" floor; C-29 is the "format change + structural rationale" ceiling. Pass condition tightened in v9: both CAN-side and CANNOT-side of the asymmetry must be stated (R8 V-02/V-03 revealed that CANNOT-only form is a subthreshold compliance path).
- **Text**: The instruction to use verbatim quoted text rather than Y/N in the Pass 3 integration column must be accompanied by a structural rationale block explaining why the format change closes the pre-fill window. The core argument requires both sides of the asymmetry: the CAN-side (a Y/N status can be assigned in the same cognitive pass as Pass 1 and Pass 2, before the merge has been executed -- filling in Y does not require the merged paragraph to exist) and the CANNOT-side (a verbatim extract from merged prose cannot be written before the merge is executed -- the text does not yet exist). A rationale that states only the CANNOT-side omits the contrast that makes the asymmetry structurally explicit; a reader who sees only the prohibition may comply mechanically without understanding the pre-fill window the format closes.
- **Pass condition**: The Pass 3 table instruction for quoted extracts includes the pre-fill impossibility argument with both sides of the asymmetry stated: (1) a Y/N status CAN be prefilled before the merge is executed, and (2) verbatim text from merged prose CANNOT be written before the merge exists. A rationale that states only one side does not satisfy C-29 even if C-26 is satisfied.

### C-31 -- Self-Diagnosis Positive Search Space Given as a Dedicated Named Block
- **Weight**: aspirational
- **Category**: depth
- **Source**: R8 excellence signal V-02 (E-01 pattern, dedicated positive-search-space block). C-25 is the "categorically novel diagnosis" floor; C-31 is the "dedicated labeled block" ceiling. C-28 (embedded positive search space) retired in v9; C-31 is the new ceiling above C-25.
- **Text**: The Amendment 1 positive search space instruction must appear as a separately labeled block -- distinct from the Why block that accompanies the exclusion constraint. A dedicated block such as `*Where to look instead -- positive search space:*` separates the two cognitive tasks: the Why block explains why the fixed amendment categories are excluded as diagnostic targets; the positive-space block names where to look instead. Embedding the positive search space targets inside the Why block satisfies the retired C-28; a dedicated block satisfies C-31 by making the diagnostic target list structurally independent of the constraint rationale. Without separation, both tasks can be satisfied in a single reading pass; with a dedicated block, the positive search space becomes an independently auditable component with its own label and scope.
- **Pass condition**: The Amendment 1 self-diagnosis instruction includes a separately labeled block for the positive search space that is visually and structurally distinct from the Why constraint block. The positive-space block must carry its own label (e.g., "Where to look instead", "Positive search space", or structurally equivalent) and appear as a distinct block -- not as inline content within the Why block. A Why block that mentions positive targets inline does not satisfy C-31 even if two or more non-fixed category names appear in it.

### C-32 -- Inertia Aggregation Gate Names Each Canonical Path at the Closure Event
- **Weight**: aspirational
- **Category**: format
- **Source**: R8 excellence signal V-03 (E-02 pattern, named-per-path gate). C-27 is the "per-path confirmation" floor; C-32 is the "named-per-path gate" ceiling. C-30 (anonymous aggregation gate) retired in v9; C-32 is the new ceiling.
- **Text**: The aggregation gate must name all three canonical cheap paths at the closure event itself -- "Signal-skip: closed. Nominal gap framing: closed. Non-trivial gaming: closed. All three canonical paths confirmed and closed. Proceed to Phase 0." or a structurally equivalent formulation that names each path at the gate. An anonymous gate ("All three paths closed. Proceed.") satisfies the retired C-30 by generating an active closure signal; a named-per-path gate satisfies C-32 by embedding the canonical path names at the gate event, not only at the per-path confirmation lines. When canonical names appear at closure, the gate itself serves as a checklist summary: a reader auditing the gate can confirm which paths were checked without scanning back through the per-path confirmation lines. The gate line must be its own sentence or structured block, distinct from the third per-path confirmation.
- **Pass condition**: The aggregation gate line names all three canonical cheap paths (signal-skip, nominal gap framing, non-trivial gaming) at the gate event itself, with each path individually named and declared closed before the proceed statement. A gate that says "All three paths closed. Proceed." without naming the individual paths does not satisfy C-32 even if C-30 would have been satisfied.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                         |
|--------------|-----------------|--------|----------------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                                    |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                      |
| Aspirational | C-10 to C-32    | 20     | Separates good from excellent. C-25, C-26, C-27, C-29, C-31, C-32 are the ceiling layer. |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v8

| Change              | Detail |
|---------------------|--------|
| C-28 retired        | Universally passing in all three R8 variations (V-01, V-02, V-03). C-31 (dedicated positive-space block) is the new ceiling; C-28 as "exclusion constraint + enumerated positive search space (embedded)" is expectation, not achievement. |
| C-30 retired        | Universally passing in all three R8 variations. C-32 (named-per-path gate) is the new ceiling; C-30 as "per-path confirmations + anonymous aggregation gate" is expectation, not achievement. |
| C-27 updated        | Source note updated: C-30 (anonymous aggregation gate) retired in v9; C-32 (named-per-path gate) is the new ceiling; C-27 remains the per-path confirmation floor. |
| C-29 updated        | Pass condition tightened: both CAN-side and CANNOT-side of the asymmetry must be stated. R8 V-02/V-03 reveal that CANNOT-only form is a subthreshold compliance path. Prior v8 pass condition did not make the two-sided requirement explicit; this update aligns the written condition with the R7 evidence base (V-01/V-04 always cited both sides). |
| C-31 added          | Self-diagnosis positive search space given as a dedicated named block -- from R8 V-02 signal (E-01). 2 pts. Dedicated-block ceiling above the retired C-28 embedded-positive-space floor. |
| C-32 added          | Inertia aggregation gate names each canonical path at the closure event -- from R8 V-03 signal (E-02). 2 pts. Named-per-path ceiling above the retired C-30 anonymous-gate floor. |
| Tier description    | Updated to reflect C-10 to C-32 aspirational range (C-28, C-30 retired). |
| Aspirational subtotal | Remains 20 pts. Total remains 100. |

---

**Design notes:**

- **Eight criteria retired across v3-v9**: C-09 (v7), C-16 (v7), C-11/C-12/C-14/C-15/C-17/C-18 (v8), C-28/C-30 (v9). Pattern: retirement when universally passing AND a structurally stronger ceiling covers the same behavior.
- **Floor/ceiling chain integrity**: C-21->C-22 (coupling), C-20->C-23->C-26->C-29 (bridge lifecycle), C-07->C-24->C-25->C-31 (self-diagnosis), C-27->C-32 (inertia lifecycle). Each chain has a 1-pt floor (universally passing) and a 2-pt ceiling (newly differentiating).
- **C-31/C-32 structural logic**: Both share the same v9 pattern -- a v8 criterion established the behavior (what to do: enumerate targets / generate gate); the v9 ceiling requires that behavior to be structurally independent and auditable. C-31: dedicated block separates where-to-look from why-not-there (two independently auditable components). C-32: named-per-path gate embeds canonical terms at the closure event so the gate itself confirms what was checked (single auditable event replaces back-scan).
- **C-29 pass condition tightened**: R8 V-02/V-03 revealed that CANNOT-only form is the minimal compliance path. The two-sided requirement (CAN + CANNOT) is now explicit. This is a clarification, not a new criterion -- the R7 evidence always cited both sides (V-01/V-04); the written condition now matches the evidence.
- **V-04 synthesis target**: A next-generation synthesis variation would combine all three ceiling criteria: CAN + CANNOT sides in Pass 3 rationale (C-29), dedicated positive-space block in Amendment 1 (C-31), and named-per-path aggregation gate in the inertia block (C-32). V-01 satisfies C-29 but not C-31 or C-32. V-02 satisfies C-31 but not C-29 or C-32. V-03 satisfies C-32 but not C-29 or C-31. No single R8 variation satisfies all three.
