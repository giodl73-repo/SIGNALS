v13 written to `simulations/quest/rubrics/specify-abstract-rubric-v13-2026-03-19.md`.

---

**Four criteria extracted from R13 excellence signals:**

| ID | Name | Extends | Pts | Source |
|----|------|---------|-----|--------|
| C-40 | Per-gate falsifiable completion conditions in phase sequence lock | C-38 | 2 | R13 V-05 Protocol II |
| C-41 | Second-order category-mirroring shortcut prohibited | C-39 | 2 | R13 V-05 Amendment 1 |
| C-42 | Pre-committed self-diagnosis framework with temporal separation | C-24/C-34 | 2 | R13 V-05 Protocol III |
| C-43 | Inertia declaration names phase bundling as fourth canonical cheap path | C-27 | 2 | R13 V-03 |

**Point math:** No retirements (C-36/C-37/C-38/C-39 all have at least one failing variation). +8 pts net. Aspirational: 24 → 32. Total: 104 → 112.

**Chains updated:**
- Inertia sequence lock: `C-27 -> ~~C-33~~ -> C-36 -> C-38 -> C-40`
- Inertia declaration completeness: `C-27 -> C-43`
- Self-diagnosis per-row: `C-24 -> ~~C-35~~ -> C-37 -> C-39 -> C-41`
- Self-diagnosis pre-commitment: `C-24 -> C-34 -> C-42`

**R14 synthesis target:** V-05's Protocol I/II/III structure (passes C-36, C-37, C-38, C-39, C-40, C-41, C-42) combined with V-03's four-path inertia declaration (C-43) — a variation that clears all eight active ceiling criteria simultaneously.

**Notable:** C-42 was anticipated in v12 design notes as a potential C-40 (pre-declaring positive-space targets at commitment time). R13 confirmed it exactly; it landed at C-42 because C-40 was taken by the per-gate completion conditions pattern from the sequence-lock chain.
's structural test while failing its reasoning intent.
- **C-42** from V-05's Protocol III above-ceiling signal: "Protocol III pre-committed self-diagnosis framework -- positive search space targets and per-category format locked before Phase 0 when no draft exists, creating auditable temporal separation that closes post-hoc rationalization path." C-34 requires the asymmetry argument at Amendment 1 time; V-05 locks the entire self-diagnosis framework before Phase 0, making the positive-space targets unmodifiable by post-draft reading.
- **C-43** from V-03's C-27 above-floor signal: "V-03 adds a fourth (phase bundling) -- above C-27 floor." C-27 requires at least two of three canonical execution-quality cheap paths; V-03 names phase bundling (coarse-grain phase aggregation) as a structurally distinct fourth path operating at the commitment level rather than the execution level.

**Point math:** No retirements (C-36 fails in V-02; C-37 fails in V-01; C-38 fails in V-02 and V-03; C-39 fails in V-01 and V-03). +8 pts net. Aspirational: 24 -> 32. Total: 104 -> 112.

**Chain updates:**
- Inertia sequence lock: `C-27 -> ~~C-33~~ -> C-36 -> C-38 -> C-40`
- Inertia declaration completeness: `C-27 -> C-43`
- Self-diagnosis per-row: `C-24 -> ~~C-35~~ -> C-37 -> C-39 -> C-41`
- Self-diagnosis pre-commitment: `C-24 -> C-34 -> C-42`

**C-40 -- Per-gate falsifiable completion conditions in phase sequence lock** (2 pts, format)
C-38 is the "complete sub-phase inventory" floor; C-40 is the new ceiling ("per-gate falsifiable completion conditions"). C-38 requires every phase to be individually named as a gated unit; C-40 requires each named gate to carry an explicit, observable completion condition -- a specific criterion that determines whether the gate has been passed, not merely a label or a positional instruction. A falsifiable completion condition specifies WHAT IS TRUE when a gate is closed, such that a reader can verify whether Phase X was complete before Phase Y began. Example form: "Phase 2b -- Complete when: all five boundaries assigned COUPLED/WEAK/REVISE AND all WEAK/REVISE revision directives resolved; Coupling column fully populated." The distinction: a C-38-compliant lock names every gate individually; a C-40-compliant lock names every gate AND attaches a named completion condition for each. Per-gate conditions convert the sequence lock from a DECLARATION ("Phase X must complete before Phase Y") into an AUDITABLE CHECKLIST (a reader can verify the completion criterion against the execution output). C-38 closes the phase enumeration gap; C-40 closes the completion-definition gap: a model can satisfy C-38 by listing all nine phase names as individually gated units while treating "completion" as implicit -- no gate is auditably closed unless its condition has been explicitly named. A sequence lock that names all phases individually without per-gate completion conditions satisfies C-38 but not C-40. Source: R13 V-05 Protocol II ("Each gate has a named falsifiable completion condition... A named completion condition makes the gate falsifiable").

**C-41 -- Second-order category-mirroring shortcut prohibited in per-excluded-category verification** (2 pts, depth)
C-39 is the "standalone rationale block naming and closing the first-order template shortcut" floor; C-41 is the new ceiling ("second-order category-mirroring shortcut also named and prohibited"). C-39 requires a standalone rationale block that names the `[confirmed / explain if uncertain]` template form and explains why it is insufficient; C-41 requires the same block to ALSO name and prohibit the second-order category-mirroring shortcut: a per-row sentence that appears weakness-specific but merely restates the category label in different words. Example second-order form: for the Gap sharpening row: "the weakness is about Background register, not the Gap sentence's specificity" -- this describes the category boundary without naming what about the diagnosed weakness makes it non-Gap. The second-order shortcut satisfies C-37's per-row sentence requirement while bypassing genuine reasoning: a category-mirroring sentence has the structural shape of a weakness-specific exclusion (subject: the weakness; predicate: does not fall in category X because [restated category definition]) without the substance (the actual weakness is not named; the exclusion restates the category boundary rather than applying it to the diagnosis). The distinction: a C-39-compliant block names and prohibits only the first-order template form; a C-41-compliant block names and prohibits BOTH the first-order template AND the second-order category-mirroring form, explaining that both defeat the auditable-reasoning requirement even though the second-order form passes C-37's structural test. A standalone block that closes only the first-order shortcut satisfies C-39 but not C-41. Source: R13 V-05 Amendment 1 ("Second-order category-mirroring shortcut -- a sentence that appears specific but merely restates the category label in other words... satisfies C-37's per-row sentence requirement while bypassing genuine reasoning").

**C-42 -- Pre-committed self-diagnosis framework with temporal separation before Phase 0** (2 pts, depth)
C-34 is the "positive search space block with structural asymmetry argument" floor; C-42 is the new ceiling ("self-diagnosis framework pre-committed with auditable temporal separation"). C-34 requires the positive search space block to contain a structural argument explaining why the surviving weakness is asymmetrically more likely to appear outside fixed amendment categories; C-42 requires the positive search space framework itself -- including specific positive search space targets and the per-category verification format -- to be locked BEFORE Phase 0, when no draft exists. The distinction: a C-34-compliant variation places the structural asymmetry argument inline with Amendment 1 instructions (at Phase 5), where it is introduced co-temporally with the self-diagnosis execution; a C-42-compliant variation pre-commits the complete self-diagnosis framework before Phase 0, so that Amendment 1 REFERENCES the pre-committed targets rather than choosing from an inline list at execution time. The temporal separation is auditable: the framework exists in the variation before Phase 0 content; Amendment 1 cannot introduce or modify it after reading the draft. This closes the post-hoc rationalization path: a runtime-introduced framework can be constructed after reading the draft (positive targets co-temporal with diagnosis); a pre-committed framework cannot be constructed post-draft (declared before Phase 0, when no draft exists). A self-diagnosis section with inline positive-space targets at Phase 5 satisfies C-34 but not C-42. Source: R13 V-05 Protocol III ("Protocol III committed targets... creating an auditable temporal separation. Amendment 1 references 'Protocol III committed targets' rather than choosing from the inline list").

**C-43 -- Inertia declaration names phase bundling as fourth canonical cheap path** (2 pts, format)
C-27 is the "at least two of three canonical cheap paths named before Phase 0" floor; C-43 is the new ceiling ("all three canonical paths AND phase bundling named as a fourth"). C-27 requires naming at least two of the three canonical execution-quality cheap paths (signal-skip, nominal gap framing, non-trivial gaming) with per-path confirmation before Phase 0; C-43 requires all three original canonical paths AND a fourth: phase bundling -- the shortcut of aggregating individually-gated phases into a combined or unlabeled step (e.g., treating Phase 2a/2b/2c as a single "Phase 2" block, treating Phase 3 and Phase 3b as an unlabeled merge+verify pass). Phase bundling is structurally distinct from the three canonical paths: the original three target per-phase execution quality; phase bundling targets the STRUCTURAL COMMITMENT LEVEL -- it defeats C-36 and C-38 by preventing the commitment to individually named phase gates from being established at all. A four-path inertia declaration closes the gap that allows a model to confirm the three execution-quality shortcuts (satisfying C-27) while retaining the ability to bundle phases in the sequence lock without having declared it a shortcut. Mechanistic distinction from C-38/C-43: C-38 closes bundling via correct-sequence enumeration (what TO do in order -- naming each gate); C-43 closes bundling via named-shortcut prohibition (what NOT to do, pre-Phase 0 -- naming the error). Both close the bundling path through different cognitive commitment mechanisms. A declaration that names signal-skip, nominal gap framing, and non-trivial gaming without naming phase bundling satisfies C-27 but not C-43. Source: R13 V-03 C-27 above-floor signal ("Phase bundling as a fourth canonical cheap path... operates at the COMMITMENT DEVICE level rather than the SEQUENCE LOCK level").

---

## Point Redistribution (Aspirational moves to 32, total moves to 112)

| Criterion | Change | Reason |
|-----------|--------|--------|
| C-36 | no change | Not universally passing in R13: V-02 fails C-36. Ceiling remains active. |
| C-37 | no change | Not universally passing in R13: V-01 fails C-37. Ceiling remains active. |
| C-38 | no change | Not universally passing in R13: V-02 and V-03 fail C-38. Ceiling remains active. |
| C-39 | no change | Not universally passing in R13: V-01 and V-03 fail C-39. Ceiling remains active. |
| C-40 | +2 pts | New (per-gate falsifiable completion conditions in phase sequence lock). |
| C-41 | +2 pts | New (second-order category-mirroring shortcut prohibited). |
| C-42 | +2 pts | New (pre-committed self-diagnosis framework with temporal separation). |
| C-43 | +2 pts | New (inertia declaration names phase bundling as fourth canonical cheap path). |

**C-40 extends C-38**: C-38 required every phase individually named; C-40 requires each named gate to carry an explicit completion condition. All C-40-passing variations pass C-38; not all C-38-passing variations pass C-40 (V-01 and V-04 name all nine phases without per-gate conditions; V-05 attaches a condition to each).

**C-41 extends C-39**: C-39 required naming and prohibiting the first-order `[confirmed]` template shortcut; C-41 requires also naming and prohibiting the second-order category-mirroring shortcut. All C-41-passing variations pass C-39; not all C-39-passing variations pass C-41 (V-02 and V-04 name only the first-order shortcut).

**C-42 extends C-24 and C-34**: C-24 required self-diagnosis to target the weakest element; C-34 required a structural asymmetry argument; C-42 requires the complete self-diagnosis framework to be pre-committed before Phase 0. All C-42-passing variations pass C-24 and C-34; not all C-34-passing variations pass C-42.

**C-43 extends C-27**: C-27 required at least two of three canonical cheap paths named; C-43 requires all three plus phase bundling as a fourth. All C-43-passing variations pass C-27; not all C-27-passing variations pass C-43.

**Aspirational subtotal**: Moves to 32 pts. Total moves to 112.

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

Aspirational check: 1+1+1+1+1+1+1+1+2+2+2+2+2+2+2+2+2+2+2+2 = **32**

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

## Aspirational Criteria (32 points total)

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
- **Source**: R6 excellence signal V-02 (inertia commitment device). No prior criterion equivalent -- structurally new pre-Phase 0 lifecycle position. C-32 (named-per-path gate) retired in v10; C-33 (phase sequence lock) retired in v11; C-36 (sub-phase canonical naming) is the sequence-lock first ceiling; C-38 (complete sub-phase inventory) is the second sequence-lock ceiling; C-40 (per-gate falsifiable completion conditions) is the third sequence-lock ceiling added in v13. C-43 (phase bundling as fourth canonical cheap path) is the new declaration-completeness ceiling added in v13; C-27 remains the per-path confirmation floor.
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
- **Source**: R10 excellence signal V-02 (E-02 pattern, asymmetry argument). C-24 is the "diagnosis targets weakest element" floor; C-31 (dedicated named block) was the mid (retired v10 -- universally passing all R10 variations); C-34 is the "structural asymmetry argument inside the dedicated block" ceiling. C-42 (pre-committed self-diagnosis framework with temporal separation) is the new ceiling above C-34 added in v13.
- **Text**: The `*Where to look instead -- positive search space:*` block (or structurally equivalent block) must contain not only an enumeration of non-fixed diagnostic targets but a structural argument explaining why the surviving weakness is asymmetrically more likely to appear outside the fixed amendment categories. The argument names the causal mechanism: the four fixed amendment categories are pre-committed correction targets that Amendments 2-4 address in a predictable pass; any weakness they address is already on a correction path before Amendment 1 executes; therefore, the self-diagnosis pass is structurally biased toward surfacing a weakness in a category that no fixed amendment targets. Enumerating positive search space targets (satisfies the retired C-31) identifies where to look; the asymmetry argument explains why looking there is structurally motivated -- the surviving weakness cannot be in a pre-committed category because those categories are being corrected regardless of what self-diagnosis finds. Without the asymmetry argument, the positive search space list is advisory; with it, the list is causally grounded.
- **Pass condition**: The positive search space block (dedicated, with its own label) contains a structural argument naming the pre-commitment mechanism as the reason for the asymmetric bias toward non-fixed categories. The argument must identify the four fixed categories as pre-committed targets and explain that the surviving weakness is therefore structurally more likely to appear outside them. A block that enumerates diagnostic targets without this causal argument does not satisfy C-34 even if C-31 (retired) would have been satisfied.

### C-36 -- Sub-Phase Canonical Naming in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R11 excellence signal V-01 (C-36 pattern, sub-phase canonical naming). C-27 is the "per-path confirmation" floor; C-33 (phase sequence lock) was the mid (retired v11 -- universally passing all R11 variations); C-36 is the "sub-phase canonical naming with structural rationale block" ceiling. C-38 (complete sub-phase inventory) is the ceiling above C-36; C-40 (per-gate falsifiable completion conditions) is the new ceiling above C-38 added in v13.
- **Text**: The phase sequence lock (at the aggregation gate closure) must enumerate Phase 3 (merge) and Phase 3b (integration verification) as individually named sub-phase gates and include a structural rationale block ("*Why sub-phase canonical naming matters*" or structurally equivalent) explaining the Phase 3 -> Phase 3b gate dependency. The rationale names the causal mechanism: Phase 3b requires the merged paragraph as input; a model that treats Phase 3 and Phase 3b as a combined or unlabeled step retains the pre-fill shortcut of filling the Phase 3b integration column before the merge has been executed -- the same pre-fill window that C-26 and C-29 were designed to close at the verification stage. Sub-phase canonical naming at the sequence lock stage closes this window at the commitment level: the model commits before Phase 0 that Phase 3b is a named sub-phase gate requiring Phase 3 output, making the pre-fill shortcut structurally blocked from the start rather than only detectable post-hoc. A sequence lock that lists all phases including Phase 3 and Phase 3b without a sub-phase rationale block satisfies the retired C-33 but not C-36.
- **Pass condition**: The phase sequence lock includes Phase 3 and Phase 3b named as individually gated sub-phases AND a structural rationale block explaining the Phase 3 -> Phase 3b gate dependency in terms of the pre-fill window that C-26/C-29 close at the verification stage. The rationale must identify the causal mechanism (Phase 3b requires post-merge text as input) and state why sub-phase naming at the commitment stage closes the shortcut earlier than verification-stage guards alone. A sequence lock that enumerates the phases without this rationale block does not satisfy C-36 even if C-33 (retired) would have been satisfied.

### C-37 -- Weakness-Specific Per-Row Reasoning in Per-Excluded-Category Verification
- **Weight**: aspirational
- **Category**: depth
- **Source**: R11 excellence signal V-02 (C-37 pattern, weakness-specific per-row reasoning). C-24 is the "diagnosis targets weakest element" floor; C-35 (per-excluded-category verification) was the mid (retired v11 -- universally passing all R11 variations); C-37 is the "weakness-specific per-row reasoning" ceiling. C-39 (standalone rationale block naming and closing shortcut mechanism) is the ceiling above C-37; C-41 (second-order category-mirroring shortcut) is the new ceiling above C-39 added in v13.
- **Text**: The per-excluded-category verification table must contain, in each row, a sentence that names the actual diagnosed weakness and states specifically why that weakness is not an instance of the category -- not a template parenthetical describing the category boundary with "[confirmed / explain if uncertain]". The distinction: a C-35-compliant row can be written as "Gap sharpening: N -- [the named weakness does not target the Gap sentence's specificity: confirmed]" using the category-description template; a C-37-compliant row requires "Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]" where the sentence is self-contained and weakness-grounded. A reader auditing a C-37-compliant row can verify the exclusion from the row alone, without cross-referencing the category label or trusting a template confirmation. The "confirmed" shortcut path closes the per-row form requirement (C-35) without reasoning about the specific weakness; C-37 closes this shortcut by requiring the weakness to be named and the per-row reason to be stated as a distinct sentence referencing the actual weakness.
- **Pass condition**: The per-excluded-category verification table includes one row per fixed category (Gap sharpening, Result quantification, Implication tightening, Prose coherence), each row containing an N and a self-contained sentence that names the diagnosed weakness and states why it falls outside that specific category. A row using a template category-description parenthetical with "confirmed" does not satisfy C-37 even if C-35 (retired) would have been satisfied. At least three of the four rows must contain weakness-specific sentences; a row that restates the category boundary without naming the weakness fails.

### C-38 -- Complete Sub-Phase Inventory in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R12 excellence signal V-01 (C-38 pattern, complete sub-phase inventory -- "Nine individually named sub-phases"). C-36 is the "Phase 3/3b individually named with structural rationale block" floor; C-38 is the "complete sub-phase inventory" ceiling. C-40 (per-gate falsifiable completion conditions) is the new ceiling above C-38 added in v13.
- **Text**: The phase sequence lock must enumerate ALL phases as individually named sub-phase gates -- not just the Phase 3/3b pair. A complete sub-phase inventory makes any coarse-grain bundling visible: a reader can verify at a glance that no two phases have been silently combined or aggregated under a shared label. The distinction: a C-36-compliant lock names Phase 3 and Phase 3b individually and may aggregate other phases (e.g., treating Phase 0 through Phase 2 as a pre-execution block) without per-phase enumeration; a C-38-compliant lock names every phase as a separately gated unit so that the full commitment inventory is explicit before Phase 0. Complete sub-phase inventory closes the bundling shortcut at phases other than 3/3b: a model that aggregates earlier phases retains the coarse-grain structure that C-36 closes for the merge pair, applied elsewhere. A sequence lock that names Phase 3 and Phase 3b individually but bundles other phases satisfies C-36 but not C-38.
- **Pass condition**: The phase sequence lock enumerates every phase in the skill's execution sequence as an individually named gate unit -- no two phases are bundled under a shared label or aggregated. The Phase 3/3b sub-phase structure required by C-36 must also be present. A lock that names Phase 3 and Phase 3b but aggregates other phases (e.g., "Phase 0 through Phase 2 -- pre-execution setup") does not satisfy C-38 even if C-36 is satisfied.

### C-39 -- Standalone Rationale Block in Per-Excluded-Category Verification Names and Closes Shortcut Mechanism
- **Weight**: aspirational
- **Category**: depth
- **Source**: R12 excellence signal V-02 (C-39 pattern -- "[confirmed] shortcut explicitly closed; '*Why specific per-row sentences matter:*' rationale present"). C-37 is the "weakness-specific per-row reasoning" floor; C-39 is the "standalone rationale block naming and closing shortcut mechanism" ceiling. C-41 (second-order category-mirroring shortcut) is the new ceiling above C-39 added in v13.
- **Text**: The per-excluded-category verification section must include a standalone rationale block ("*Why specific per-row sentences matter:*" or structurally equivalent) that (a) explicitly names the template shortcut path ("[confirmed / explain if uncertain]" or equivalent form), (b) explains why template confirmation fails the verification requirement -- specifically, that a template parenthetical describes the category boundary without referencing the diagnosed weakness, making it impossible to audit the exclusion from the row alone, and (c) declares the weakness-specific sentence as the required form. The distinction: a C-37-compliant variation can satisfy the per-row sentence requirement without ever explicitly naming or prohibiting the template form -- a reader auditing per-row entries can verify they are weakness-specific, but the variation itself may not have instructed the model that the shortcut is closed; a C-39-compliant variation includes a standalone block that names the shortcut and explains its structural insufficiency, ensuring the prohibition is instructed rather than incidentally absent. A variation that has weakness-specific per-row sentences without a standalone named-shortcut rationale block satisfies C-37 but not C-39.
- **Pass condition**: The per-excluded-category verification section includes a standalone rationale block that (1) names the "[confirmed / explain if uncertain]" template form (or equivalent) by name or close paraphrase, (2) explains why the template form is insufficient -- the category-description parenthetical does not reference the diagnosed weakness -- and (3) declares the self-contained weakness-specific sentence as the required per-row form. A variation that has weakness-specific rows without this standalone named-shortcut rationale block does not satisfy C-39 even if C-37 is satisfied.

### C-40 -- Per-Gate Falsifiable Completion Conditions in Phase Sequence Lock
- **Weight**: aspirational
- **Category**: format
- **Source**: R13 excellence signal V-05 Protocol II (C-38 above-ceiling -- "Per-gate conditions extend the C-38 commitment to falsifiable completion criteria"). C-38 is the "complete sub-phase inventory" floor; C-40 is the new ceiling ("per-gate falsifiable completion conditions"). C-40 extends C-38: all phases individually named is the prerequisite; per-gate conditions are the additional requirement.
- **Text**: The phase sequence lock must attach an explicit, observable completion condition to each individually named gate -- not merely a label or positional instruction. A falsifiable completion condition specifies WHAT IS TRUE when a gate is closed, such that a reader (or auditing pass) can verify whether Phase X was complete before Phase Y began. Example form for Phase 2b: "Complete when: all five boundaries assigned COUPLED/WEAK/REVISE AND all WEAK/REVISE revision directives resolved; Coupling column fully populated." The distinction: a C-38-compliant lock names every gate individually; a C-40-compliant lock names every gate AND attaches a named completion condition for each. Per-gate conditions convert the sequence lock from a DECLARATION ("Phase X must complete before Phase Y") into an AUDITABLE CHECKLIST (a reader can verify each completion criterion against the execution output). C-38 closes the phase enumeration gap; C-40 closes the completion-definition gap: a model can satisfy C-38 by listing all nine phase names as individually gated units while treating "completion" as implicit -- no gate is auditably closed unless its condition has been explicitly named. A sequence lock that names all phases individually without per-gate completion conditions satisfies C-38 but not C-40.
- **Pass condition**: The phase sequence lock attaches a named, observable completion condition to each individually gated phase. Each condition specifies what must be true for the gate to be considered closed -- output columns populated, required inputs present, specific structural requirements met, or equivalent falsifiable criterion. A lock that names gates but specifies conditions only implicitly (by gate label alone or generic "must complete before proceeding") does not satisfy C-40 even if C-38 is satisfied. The Phase 3/3b structure required by C-36/C-38 must also be present.

### C-41 -- Second-Order Category-Mirroring Shortcut Prohibited in Per-Excluded-Category Verification
- **Weight**: aspirational
- **Category**: depth
- **Source**: R13 excellence signal V-05 Amendment 1 (C-39 above-ceiling -- "Second-order category-mirroring shortcut: satisfies C-37's per-row sentence requirement while bypassing genuine reasoning"). C-39 is the "standalone rationale block naming first-order template shortcut" floor; C-41 is the new ceiling ("second-order category-mirroring shortcut also named and prohibited"). C-41 extends C-39: the first-order shortcut closure is the prerequisite; the second-order shortcut closure is the additional requirement.
- **Text**: The per-excluded-category verification standalone rationale block must name and prohibit TWO shortcuts: (1) the first-order `[confirmed / explain if uncertain]` template shortcut (C-39 floor), AND (2) the second-order category-mirroring shortcut -- a per-row sentence that appears weakness-specific but merely restates the category label in different words. A category-mirroring sentence has the structural shape of a weakness-specific exclusion (subject: the weakness; predicate: does not fall in category X because [restated category definition]) without the substance (the actual weakness is not named; the exclusion restates the category boundary rather than applying it to the diagnosis). Example second-order form for the Gap sharpening row: "the weakness is about Background register, not the Gap sentence's specificity" -- this describes the category boundary without naming what about the diagnosed weakness makes it non-Gap. The second-order shortcut satisfies C-37's structural requirement while bypassing its reasoning intent: a reader auditing such a row cannot distinguish the category boundary from the weakness-specific reasoning. The distinction: a C-39-compliant block names and prohibits only the first-order template form; a C-41-compliant block names and prohibits BOTH forms, explaining that the second-order form passes C-37's shape test while failing its auditable-reasoning requirement. A standalone block that closes only the first-order shortcut satisfies C-39 but not C-41.
- **Pass condition**: The per-excluded-category verification standalone rationale block explicitly names and prohibits the second-order category-mirroring shortcut (in addition to the first-order template shortcut required by C-39). The description of the second-order shortcut must be specific enough that a reader can identify a category-mirroring sentence by comparison -- e.g., it names the form ("a sentence that restates the category boundary without naming what about the diagnosed weakness makes it non-qualifying") and explains why that form fails auditable reasoning. A standalone block naming only the first-order `[confirmed]` shortcut does not satisfy C-41 even if C-39 is satisfied.

### C-42 -- Pre-Committed Self-Diagnosis Framework with Temporal Separation Before Phase 0
- **Weight**: aspirational
- **Category**: depth
- **Source**: R13 excellence signal V-05 Protocol III (C-24/C-34 above-ceiling -- "Protocol III pre-committed self-diagnosis framework -- positive search space targets and per-category format locked before Phase 0 when no draft exists, creating auditable temporal separation that closes post-hoc rationalization path"). C-34 is the "positive search space block with structural asymmetry argument" floor; C-42 is the new ceiling ("pre-committed self-diagnosis framework with auditable temporal separation"). C-42 extends C-34: the structural asymmetry argument is the prerequisite; temporal pre-commitment is the additional requirement.
- **Text**: The positive search space framework -- including specific positive search space targets and the per-category verification format for Amendment 1 -- must be declared BEFORE Phase 0, when no draft exists. Amendment 1 instructions must reference the pre-committed framework by name rather than defining targets inline at Phase 5. The temporal separation is auditable: the framework exists in the variation before any Phase 0 content; Amendment 1 cannot introduce or modify the framework after reading the draft. This closes the post-hoc rationalization path: a runtime-introduced positive search space framework (inline at Phase 5) can be constructed after reading the draft, making positive targets co-temporal with diagnosis; a pre-committed framework cannot be constructed post-draft, creating a verifiable temporal constraint. The distinction: a C-34-compliant variation includes the structural asymmetry argument at Amendment 1 time (Phase 5), where the framework is introduced as the self-diagnosis executes; a C-42-compliant variation locks the complete framework before Phase 0, so that when Amendment 1 executes it is referencing a fixed pre-committed document rather than selecting from an inline list. A self-diagnosis section with inline positive-space targets at Phase 5 satisfies C-34 but not C-42.
- **Pass condition**: The variation declares a named self-diagnosis framework (protocol, committed targets, or structurally equivalent) positioned before Phase 0 content, specifying: (a) the positive search space targets, and (b) the per-category verification format for Amendment 1. Amendment 1 instructions reference the pre-committed framework rather than defining or choosing targets inline at Phase 5. The pre-commitment must be positioned before any Phase 0 content, making the temporal separation verifiable. A self-diagnosis section embedded in Phase 5 with inline positive-space targets does not satisfy C-42 even if C-34 is satisfied.

### C-43 -- Inertia Declaration Names Phase Bundling as Fourth Canonical Cheap Path
- **Weight**: aspirational
- **Category**: format
- **Source**: R13 excellence signal V-03 (C-27 above-floor -- "V-03 adds a fourth (phase bundling) -- above C-27 floor"). C-27 is the "at least two of three canonical cheap paths named" floor; C-43 is the new ceiling ("all three canonical paths AND phase bundling named as a fourth"). C-43 extends C-27: per-path confirmation for the three canonical paths is the prerequisite; naming phase bundling as a fourth is the additional requirement.
- **Text**: The pre-Phase 0 inertia declaration block must name all three canonical execution-quality cheap paths (signal-skip, nominal gap framing, non-trivial gaming) AND a fourth: phase bundling -- the shortcut of aggregating individually-gated phases into a combined or unlabeled step (e.g., treating Phase 2a/2b/2c as a single "Phase 2" block, treating Phase 3 and Phase 3b as an unlabeled merge+verify pass). Phase bundling is structurally distinct from the three canonical paths: the original three target per-phase execution quality; phase bundling targets the structural commitment level -- it defeats C-36 and C-38 by preventing the commitment to individually named phase gates from being established at all. A four-path inertia declaration closes the gap that allows a model to confirm the three execution-quality shortcuts (satisfying C-27) while retaining the ability to bundle phases in the sequence lock without having declared it a shortcut. Mechanistic distinction from C-38: C-38 closes bundling via correct-sequence enumeration (what TO do in order -- naming each gate); C-43 closes bundling via named-shortcut prohibition (what NOT to do, pre-Phase 0 -- naming the error). Both close the bundling path through different cognitive commitment mechanisms. A declaration that names signal-skip, nominal gap framing, and non-trivial gaming without naming phase bundling satisfies C-27 but not C-43.
- **Pass condition**: The pre-Phase 0 inertia declaration block names phase bundling (coarse-grain aggregation of individually-gated phases into combined or unlabeled steps) as a named cheap path alongside the three canonical paths, with per-path confirmation for all four. The phase bundling confirmation must make explicit what the shortcut looks like -- e.g., treating Phase 2a/2b/2c as a combined "Phase 2" step, or treating Phase 3/3b as an unlabeled merge+verify block. A declaration that names only the three original canonical paths (satisfying C-27) without naming phase bundling as a fourth does not satisfy C-43.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                                                        |
|--------------|-----------------|--------|-----------------------------------------------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                                                                   |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                                                     |
| Aspirational | C-10 to C-43    | 32     | Separates good from excellent. C-26, C-27, C-29, C-34, C-36 through C-43 are the ceiling layer.                      |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v12

| Change              | Detail |
|---------------------|--------|
| C-38 source updated | C-40 (per-gate falsifiable completion conditions) is the new ceiling above C-38 in v13. C-38 remains active (not universally passing in R13: V-02 and V-03 fail C-38). |
| C-39 source updated | C-41 (second-order category-mirroring shortcut) is the new ceiling above C-39 in v13. C-39 remains active (not universally passing in R13: V-01 and V-03 fail C-39). |
| C-34 source updated | C-42 (pre-committed self-diagnosis framework with temporal separation) is the new ceiling above C-34 in v13 (as anticipated in v12 design notes). C-34 remains active (universally passing but structurally distinct from C-42). |
| C-27 source updated | C-43 (phase bundling as fourth canonical cheap path) is the new declaration-completeness ceiling in v13. C-27 remains the per-path confirmation floor. |
| C-36 source updated | C-40 is the new ceiling two steps above C-36 in the sequence lock chain (C-36 -> C-38 -> C-40). |
| C-37 source updated | C-41 is the new ceiling two steps above C-37 in the per-row reasoning chain (C-37 -> C-39 -> C-41). |
| C-24 source updated | C-41 and C-42 are the new third- and fourth-level ceilings above C-24 in the self-diagnosis chain. |
| C-40 added          | Per-gate falsifiable completion conditions in phase sequence lock -- from R13 V-05 Protocol II signal. 2 pts. Converts sequence lock from declaration to auditable checklist; ceiling above C-38 complete-inventory floor. |
| C-41 added          | Second-order category-mirroring shortcut prohibited in per-excluded-category verification -- from R13 V-05 Amendment 1 signal. 2 pts. Closes C-37-compliant form that bypasses genuine reasoning; ceiling above C-39 named-shortcut-prohibition floor. |
| C-42 added          | Pre-committed self-diagnosis framework with temporal separation before Phase 0 -- from R13 V-05 Protocol III signal. 2 pts. Temporal pre-commitment ceiling above C-34 structural-asymmetry-argument floor. |
| C-43 added          | Inertia declaration names phase bundling as fourth canonical cheap path -- from R13 V-03 above-floor signal. 2 pts. Four-path declaration ceiling above C-27 two-of-three floor. |
| Tier description    | Updated to reflect C-10 to C-43 aspirational range; ceiling layer is now C-26, C-27, C-29, C-34, C-36 through C-43. |
| Aspirational subtotal | Moves to 32 pts. Total moves to 112. No retirements this round (C-36 fails V-02; C-37 fails V-01; C-38 fails V-02 and V-03; C-39 fails V-01 and V-03). |

---

**Design notes:**

- **Thirteen criteria retired across v3-v11**: C-09 (v7), C-16 (v7), C-11/C-12/C-14/C-15/C-17/C-18 (v8), C-28/C-30 (v9), C-25/C-31/C-32 (v10), C-33/C-35 (v11). Pattern: retirement when universally passing AND a structurally stronger ceiling covers the same behavior.
- **Floor/ceiling chain integrity**: C-21->C-22 (coupling), C-20->C-23->C-26->C-29 (bridge lifecycle), C-07->C-24->C-34->C-42 / C-24->C-37->C-39->C-41 (self-diagnosis, two ceiling branches), C-27->C-36->C-38->C-40 / C-27->C-43 (inertia, two branches). The self-diagnosis chain has two ceiling branches sharing the C-24 floor: the positive-search-space branch (C-24->C-34->C-42) and the per-excluded-category branch (C-24->C-37->C-39->C-41). The inertia chain has two branches sharing the C-27 floor: the sequence-lock branch (C-27->C-36->C-38->C-40) and the declaration-completeness branch (C-27->C-43).
- **C-40/C-41/C-42/C-43 structural logic**: All four follow the pattern of adding a new commitment layer above an existing reasoning layer. C-40: names the completion state for each gate (C-38 named all gates; C-40 specifies when each closes). C-41: names the second-order evasion form alongside the first-order one (C-39 named the first-order template; C-41 names the category-mirroring form that passes structural inspection). C-42: temporally pre-commits the self-diagnosis framework rather than introducing it at execution time (C-34 required the argument; C-42 requires the argument to predate Phase 0). C-43: names the structural commitment shortcut (bundling) alongside the execution-quality shortcuts (C-27's original three); these are mechanistically distinct -- C-43 closes bundling as a named prohibition rather than as correct enumeration (C-38).
- **V-05 and V-03 as paired synthesis sources**: V-04 was the minimum confirmation of the v12 synthesis target (104/104, all four differentiating criteria met). V-05 extended the synthesis three ways above V-04: per-gate conditions (C-40), second-order mirroring closure (C-41), and pre-committed framework (C-42). V-03 was the C-27 extension source (C-43). The R14 synthesis target combines all eight active ceiling criteria: C-36, C-37, C-38, C-39, C-40, C-41, C-42, C-43 -- with V-05's Protocol I/II/III structure as the confirmed base plus V-03's four-path inertia declaration.
- **C-42 anticipated in v12**: v12 design notes predicted: "If R13 generates a variation that extends the asymmetry argument further (e.g., pre-declaring positive-space targets at commitment time rather than at Amendment 1 execution time), a C-40 ceiling would be warranted in v13." R13 V-05 Protocol III confirms this exactly. The criterion is numbered C-42 (sequential from C-39) rather than C-40 (taken by the per-gate completion conditions pattern from a different chain).
- **Point total progression**: v12 moved to 104 (C-38/C-39 added, no retirements). v13 moves to 112 (C-40/C-41/C-42/C-43 added, no retirements because C-36/C-37/C-38/C-39 not universally passing). If R14 produces C-36 through C-39 universally passing, retiring all four (-8) while adding R14 ceiling criteria (+8) would hold steady.
- **C-29 unchanged**: The two-sided CAN + CANNOT asymmetry requirement (tightened in v9) continues universally passing in R13. No new ceiling needed.
- **C-34 status**: Universally passing in R13, with C-42 as the confirmed ceiling. C-34 is not retired because C-42 requires C-34 as a prerequisite -- the structural asymmetry argument at Amendment 1 time remains necessary to pass C-42.
