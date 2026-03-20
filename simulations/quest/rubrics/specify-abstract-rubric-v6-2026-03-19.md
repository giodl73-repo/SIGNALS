Written to `simulations/quest/rubrics/specify-abstract-rubric-v6-2026-03-19.md`.

---

**Three new criteria from R5 signals:**

**C-22 -- Coupling revision uses structured directive format** (2 pts, depth)
C-21 is the floor ("coupling verified"); C-22 is the ceiling ("revision is auditable"). When Phase 2c finds WEAK or REVISE, the directive must follow six fields: Boundary / Deficient-section / Deficiency / Before / After / Re-verify — parallel to Phase 5 amendment format. Open-ended notes ("revise for alignment") cannot be scored; structured directives can. Pass vacuously if all boundaries are COUPLED. Source: R5 V-01 signal, `C-21 enforcement depth`.

**C-23 -- Bridge integration verified post-merge** (2 pts, format)
Phase 3b table positioned after merge, before journal variant. Five rows — one per boundary — each with the planned Phase 2b bridge phrase and Y / N integration status. Any N (bridge dropped or replaced with a stock connector: "however", "additionally") triggers paragraph revision. Stock connectors convey no semantic relationship; they are not bridges. C-10 is the coherence floor; C-23 is the lifecycle verification ceiling. Source: R5 V-02 signal, `bridge integration as named phase`.

**C-24 -- Self-diagnosis amendment targets weakest element** (2 pts, depth)
Amendment 5 in Phase 5: model reads the post-amendment abstract and names the single weakest remaining element as a specific one-sentence claim. Must differ from all prior amendment targets (Gap / Result / Implication / prose coherence). Generic self-assessment fails. Tests calibrated quality perception beyond fixed-slot coverage. Source: R5 V-03 signal, `5th self-diagnosis amendment`.

**Point redistribution:**

| Criterion | Change   | Reason |
|-----------|----------|--------|
| C-10 | 4 -> 2 pt | C-23 + C-24 structurally enforce what C-10 measured editorially |
| C-17 | 2 -> 1 pt | Universally passing R5 |
| C-19 | 2 -> 1 pt | Universally passing R5 |
| C-20 | 2 -> 1 pt | C-23 is new ceiling; C-20 becomes planning floor |
| C-21 | 2 -> 1 pt | C-22 is new ceiling; C-21 becomes coupling floor |
| C-22/23/24 | +2 each | New criteria |

Aspirational subtotal: 1+2+1+1+1+1+1+1+1+1+1+1+1+2+2+2 = **20**. Total: **100**.
amendment) is a named-target precedent; C-24 is the unconstrained self-diagnosis ceiling. Source: R5 V-03 signal, `5th self-diagnosis amendment`.

---

## Point Redistribution (Aspirational stays at 20, total stays at 100)

| Criterion | Change   | Reason |
|-----------|----------|--------|
| C-10      | 4 -> 2 pt | C-23 (bridge integration) and C-24 (self-diagnosis) structurally enforce what C-10 measured editorially; C-10 becomes the coherence floor |
| C-17      | 2 -> 1 pt | Universally passing R5 -- becoming baseline expectation |
| C-19      | 2 -> 1 pt | Universally passing R5 -- becoming baseline expectation |
| C-20      | 2 -> 1 pt | C-23 captures the post-merge bridge integration ceiling; C-20 remains the type-planning floor |
| C-21      | 2 -> 1 pt | C-22 captures the structured-directive ceiling; C-21 remains the coupling-verified floor |
| C-22      | +2 pts   | New (coupling revision uses structured directive format) |
| C-23      | +2 pts   | New (bridge integration verified post-merge) |
| C-24      | +2 pts   | New (self-diagnosis amendment targets weakest element) |

**V-05 R5 is the synthesis base.** C-22 extends C-21; C-23 extends the C-12/C-20 bridge chain; C-24 extends C-07. All three are independent and non-redundant.

**Aspirational subtotal**: Remains 20 pts. Total remains 100.

---

## Criteria Summary Table

| ID   | Name                                               | Weight       | Category    | Points |
|------|----------------------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present                         | essential    | correctness | 10     |
| C-02 | Word count within target                           | essential    | correctness | 10     |
| C-03 | Artifact written to correct path                   | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal                        | essential    | correctness | 10     |
| C-05 | Signal acquisition executed                        | essential    | behavior    | 10     |
| C-06 | Result section is quantified                       | recommended  | depth       | 10     |
| C-07 | Amendment pass produces three distinct             | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly                  | recommended  | correctness | 10     |
| C-09 | Claim uses correct tense convention                | aspirational | depth       | 1      |
| C-10 | Abstract reads as a single coherent paragraph      | aspirational | format      | 2      |
| C-11 | Constraint reasoning stated                        | aspirational | depth       | 1      |
| C-12 | Connective bridges planned before merge            | aspirational | format      | 1      |
| C-13 | Amendment non-triviality guard applied             | aspirational | depth       | 1      |
| C-14 | Gap drafted first to ground background             | aspirational | format      | 1      |
| C-15 | Draft phase targets coverage only                  | aspirational | format      | 1      |
| C-16 | Prose coherence is a named amendment               | aspirational | depth       | 1      |
| C-17 | All-section constraint coverage                    | aspirational | depth       | 1      |
| C-18 | Paper type declared before Claim                   | aspirational | format      | 1      |
| C-19 | Paper type governs all six section registers       | aspirational | depth       | 1      |
| C-20 | Semantic bridge type constrained vocabulary        | aspirational | format      | 1      |
| C-21 | Section coupling verified before bridge            | aspirational | depth       | 1      |
| C-22 | Coupling revision uses structured directive format | aspirational | depth       | 2      |
| C-23 | Bridge integration verified post-merge             | aspirational | format      | 2      |
| C-24 | Self-diagnosis amendment targets weakest element   | aspirational | depth       | 2      |

Aspirational check: 1+2+1+1+1+1+1+1+1+1+1+1+1+2+2+2 = 20

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
- **Text**: The merged abstract falls within the target word count range (150-250 words by default, or the journal-specified limit if --for journal:<name> is provided). Abstracts outside range are not rejected outright but must include an explicit compression or expansion attempt with before/after counts.
- **Pass condition**: Word count is in range, or if over-range the output includes an explicit compression attempt with before/after counts.

### C-03 -- Artifact Written to Correct Path
- **Weight**: essential
- **Category**: behavior
- **Text**: Output file is written to signals/specify/abstract/{topic}-abstract-{date}.md (or --output path/ if flag provided). Frontmatter includes: skill: specify-abstract, topic, date, word_count, and journal (if specified).
- **Pass condition**: File exists at the expected path and frontmatter contains all required fields.

### C-04 -- Gap Framed as Gap, Not Goal
- **Weight**: essential
- **Category**: correctness
- **Text**: The Gap section names what is unresolved or unknown (e.g. "X remains unresolved"), not a research goal (e.g. "we aimed to study X"). The distinction matters: goal framing implies the paper might have failed; gap framing states a fact about the state of the field.
- **Pass condition**: Gap sentence does not use goal-framing phrases ("we aimed", "we sought to", "this paper investigates"). It makes a claim about the state of the field.

### C-05 -- Signal Acquisition Executed
- **Weight**: essential
- **Category**: behavior
- **Text**: Phase 1 is executed: the skill globs signals/**/{topic}-* and reads available artifacts (paper draft, specify-spec, discover-hypothesis) before writing the abstract. The abstract reflects extracted signals, not generic filler.
- **Pass condition**: Output shows evidence of signal-informed content (references the topic actual claim or method, not lorem ipsum). Glob results are visible or the artifact content is clearly grounded in topic signals.

---

## Recommended Criteria (30 points total)

### C-06 -- Result Section Is Quantified
- **Weight**: recommended
- **Category**: depth
- **Text**: The Result section includes at least one quantified finding -- effect size, percentage, count, or qualitative strength descriptor -- not just "we found improvements." Abstracts that say only "we found improvements" are uninformative and signal a weak paper.
- **Pass condition**: Result sentence contains a number, percentage, or explicit qualitative strength claim ("strong", "substantial", "no significant difference").

### C-07 -- Amendment Pass Produces Three Distinct Improvements
- **Weight**: recommended
- **Category**: depth
- **Text**: Phase 5 produces three labeled amendments: (1) Gap sharpened to name a specific unresolved question, (2) Result quantified if not already, (3) Implication tightened to one concrete enabling action. Each amendment is distinct and non-trivial. A restatement of the prior sentence is not an amendment.
- **Pass condition**: All three amendment slots are filled with substantive revisions. At least two of the three result in visible textual changes from the pre-amendment version.

### C-08 -- Journal Variant Applied Correctly
- **Weight**: recommended
- **Category**: correctness
- **Text**: If --for journal:<name> is specified, the abstract register matches the journal requirements (e.g., Nature/Science: broad significance lead + societal implication; PNAS: effect size in result; cognitive-science: theoretical advance in implication; arxiv: technical precision, 300-word limit).
- **Pass condition**: When a journal flag is present, the abstract text shows at least two structural adjustments matching the journal profile. Pass vacuously if no journal flag provided.

---

## Aspirational Criteria (20 points total)

### C-09 -- Claim Uses Correct Tense Convention
- **Weight**: aspirational
- **Category**: depth
- **Source**: R2 scoring: only V-02 achieves this via explicit tense check in Pass B. Reduced 4->2 pts in v3. C-18 (v4) captures the declaration mechanism; C-19 (v5) captures section-register propagation. Reduced 2->1 pt in v5 -- tense rule alone is now baseline.
- **Text**: The Claim section follows academic tense convention: past tense for empirical results, present tense for theoretical contributions. The distinction reflects timeless logical truths (present) vs. historical experimental events (past).
- **Pass condition**: Claim tense matches the paper contribution type. Empirical paper uses past tense; theory/argument paper uses present tense. Mixed papers use past for findings, present for implications.

### C-10 -- Abstract Reads as a Single Coherent Paragraph
- **Weight**: aspirational
- **Category**: format
- **Source**: R2 excellence signal. Reduced 4->2 pts in v6 -- C-23 (bridge integration post-merge) and C-24 (self-diagnosis amendment) now structurally enforce what C-10 measured editorially. C-10 is the coherence floor; C-23 and C-24 are the structural ceiling.
- **Text**: The merged abstract (Phase 3) reads as prose, not as six labeled sentences stapled together. Transitions are natural and the paragraph has narrative flow from context through finding to significance.
- **Pass condition**: No section labels appear in the merged paragraph. Adjacent sentences have logical connectives or implicit flow. The paragraph would not be rejected on stylistic grounds by a journal editor.

### C-11 -- Constraint Reasoning Is Stated
- **Weight**: aspirational
- **Category**: depth
- **Source**: R1 excellence signal E-01 (explain-why-not-just-what). Reduced 4->2 pts in v4; C-17 is the all-section ceiling. Reduced 2->1 pt in v5 -- universally passing R4, now baseline.
- **Text**: For at least two of the key constraints (gap framing, result quantification, tense convention), the skill explains the reason the rule exists, not just the rule itself. An AI that understands the motivation can self-correct edge cases not covered by examples.
- **Pass condition**: At least two of C-04, C-06, or C-09 are accompanied by a one-sentence rationale explaining why the constraint exists (e.g., "goal framing implies the paper might have failed; gap framing states a fact about the field").

### C-12 -- Connective Bridges Planned Before Merge
- **Weight**: aspirational
- **Category**: format
- **Source**: R1 excellence signal E-02 (connective-bridges-pre-merge). Reduced 4->2 pts in v3; reduced 2->1 pt in v5 as C-20 captures the semantic type ceiling. C-12 remains the "bridges planned" floor.
- **Text**: A 3-8 word connective phrase is composed after each section draft, before the merge step. These phrases become the logical glue in Phase 3, forcing narrative flow to be a first-class authoring concern rather than a post-hoc editorial fix.
- **Pass condition**: Output includes connective bridge phrases between section drafts (or the merged paragraph shows tight logical connectives at each section boundary). The Background-to-Gap and Result-to-Implication transitions are explicit, not implied.

### C-13 -- Amendment Non-Triviality Guard Applied
- **Weight**: aspirational
- **Category**: depth
- **Source**: R1 excellence signal E-03 (anti-trivial-amendment-guard). Universally passing R3 and R4 -- reduced 2->1 pt in v5, now baseline.
- **Text**: Phase 5 explicitly guards against low-effort compliance by stating that a restatement of the prior sentence is not an amendment. Before/after comparison is shown for each amendment slot, making the change visible and verifiable.
- **Pass condition**: Phase 5 output includes before/after text for at least 2 of the 3 amendments. At least 2 of the 3 produce a visible textual change -- not a paraphrase of the same sentence.

### C-14 -- Gap Drafted First to Ground Background
- **Weight**: aspirational
- **Category**: format
- **Source**: R1 excellence signal (gap-first-causal-scaffold). Universally passing R4 -- reduced 2->1 pt in v5, now baseline.
- **Text**: The Gap section is drafted before the Background section, so Background is written knowing precisely what gap it must scaffold toward. This produces tighter Background-to-Gap semantic flow at merge time: the Background ends where the Gap begins.
- **Pass condition**: Execution order shows Gap drafted first (or Phase 1 notes show gap extraction preceding background drafting). The Background sentence and Gap sentence read as cause and effect -- Background establishes the conditions; Gap names the open problem those conditions create.

### C-15 -- Draft Phase Targets Coverage Only
- **Weight**: aspirational
- **Category**: format
- **Source**: R2 excellence signal (amendment-over-draft-discipline). Universally passing R3 -- reduced 2->1 pt in v4 as baseline expectation.
- **Text**: Phase 2 produces a complete six-section draft without inline self-correction or precision revision loops. The draft is expected to be imprecise; that is Phase 5's job. Mixing coverage and correctness in one pass increases overhead and reduces amendment depth because the model conflates completeness with quality.
- **Pass condition**: Phase 2 output shows no inline revision commentary or self-correction notes. Phase 5 carries the full precision load: Before/After evidence, non-triviality guard, and explicit amendment targets.

### C-16 -- Prose Coherence Is a Named Amendment Target
- **Weight**: aspirational
- **Category**: depth
- **Source**: R2 excellence signal (prose-coherence-as-amendment-target). Universally passing R3 -- reduced 2->1 pt in v4 as baseline expectation.
- **Text**: Phase 5 includes a dedicated amendment slot whose explicit target is prose coherence -- sentence-level flow, transition quality, or readability. Prose coherence is a named, verifiable goal, not an emergent side effect of the merge step.
- **Pass condition**: Phase 5 amendment list includes one amendment explicitly labeled for prose coherence or readability. The amendment shows Before/After evidence of a prose-level change (not a content change). This amendment is the primary mechanism for earning C-10.

### C-17 -- All-Section Constraint Coverage
- **Weight**: aspirational
- **Category**: depth
- **Source**: R3 excellence signal (all-section-constraint-coverage). V-02 R3 is the only variation to earn C-11 full PASS by carrying Why: rationale on all six sections. C-11 remains as the "at least two" floor; C-17 was the ceiling. Reduced 2->1 pt in v6 -- universally passing R5, now baseline.
- **Text**: Every section instruction (all six: Background, Gap, Claim, Method, Result, Implication) carries an explicit Why: rationale explaining the criterion it enforces -- not just two. When every rule is explained, the model can self-correct edge cases not covered by examples.
- **Pass condition**: All six section drafting instructions include at least one Why: sentence explaining the reason the constraint exists. Partial credit (1 pt) if four or five sections carry rationale. Zero if three or fewer.

### C-18 -- Paper Type Declared Before Claim
- **Weight**: aspirational
- **Category**: format
- **Source**: R3 excellence signal (paper-type-forced-declaration). V-02 R3 is the only variation to earn C-09 full PASS via forced declaration. Reduced 2->1 pt in v5 -- C-19 captures the planning-parameter ceiling; C-18 remains the declaration floor.
- **Text**: Before writing the Claim section, the skill forces an explicit paper-type declaration ("Paper type: empirical / theoretical") that binds the tense convention for the Claim. A rule without a declaration is advisory; a forced declaration is a structural constraint.
- **Pass condition**: Phase 2 output includes an explicit paper-type classification step before or during Claim drafting. The classification ("empirical" or "theoretical") is stated, and the Claim tense matches it.

### C-19 -- Paper Type Governs All Six Section Registers
- **Weight**: aspirational
- **Category**: depth
- **Source**: R4 excellence signal E-01 (paper-type-as-planning-parameter). V-01 R4 reference implementation. C-18 is the "before Claim" declaration floor; C-19 was the all-section propagation ceiling. Reduced 2->1 pt in v6 -- universally passing all R5 variations, now baseline.
- **Text**: The paper type declared at Phase 0 (before signal acquisition, before any drafting) propagates into all six section registers: Background uses the appropriate epistemic register (empirical: "prior studies show"; theoretical: "existing frameworks assume"), Gap framing language shifts (empirical: "it is unknown whether X"; theoretical: "no framework accounts for X"), Method scope is bounded accordingly, and Implication form varies (empirical: "these findings enable"; theoretical: "this framework predicts"). C-18 captures the moment of declaration; C-19 captures whether the declaration actually governs the draft.
- **Pass condition**: At least four of the six sections show register differentiation traceable to the declared paper type. Empirical sections use observational language; theoretical sections use logical or structural language. Mixed registers without intentional justification fail this criterion.

### C-20 -- Semantic Bridge Type Constrained Vocabulary
- **Weight**: aspirational
- **Category**: format
- **Source**: R4 excellence signal E-02 (semantic-bridge-type-constrained-vocabulary). V-02 R4 reference implementation. C-12 is the "bridges planned" floor; C-20 was the type-first ceiling. Reduced 2->1 pt in v6 -- C-23 (bridge integration post-merge) creates a new ceiling above the bridge-planning chain; C-20 remains the type-planning floor.
- **Text**: Bridge composition uses a five-term constrained vocabulary (contrast / causation / resolution / escalation / application) as a Type column in the bridge table. The type is assigned before the bridge phrase is composed, forcing relationship identification prior to phrasing. A consecutive-type constraint (no more than two consecutive boundaries of the same type) prevents formulaic all-causation labeling without requiring the scorer to judge label correctness.
- **Pass condition**: Bridge table includes a Type column with values drawn from the five-term vocabulary (contrast / causation / resolution / escalation / application). At least two distinct types appear across the five boundaries. Bridge phrases appear after the type assignment, not before.

### C-21 -- Section Coupling Verified Before Bridge Composition
- **Weight**: aspirational
- **Category**: depth
- **Source**: R4 excellence signal E-03 (section-coupling-verification-pre-bridge). V-03 R4 reference implementation. New lifecycle position with no prior criterion equivalent. Reduced 2->1 pt in v6 -- C-22 captures the structured-directive ceiling; C-21 remains the "coupling verified" floor.
- **Text**: After all six sections are drafted and before bridge composition begins, Phase 2c assigns a COUPLED / WEAK / REVISE status at each of the five section boundaries. Any WEAK or REVISE status triggers a section-level revision before proceeding. Gap-first order (C-14) prevents Background drift but cannot prevent downstream misalignment -- Method diverging from Claim, Implication naming a known insight rather than an enabled action. Amendment 4 (prose coherence) cannot fix cross-section semantic drift post-merge; Phase 2c catches it pre-merge.
- **Pass condition**: Output includes evidence of a boundary-status pass at each of the five section boundaries (Background-Gap, Gap-Claim, Claim-Method, Method-Result, Result-Implication) positioned after section drafting and before bridge composition. At least one boundary is evaluated as WEAK or REVISE and addressed, OR all five are confirmed COUPLED with brief rationale. A boundary-status table with no rationale does not pass.

### C-22 -- Coupling Revision Uses Structured Directive Format
- **Weight**: aspirational
- **Category**: depth
- **Source**: R5 excellence signal V-01 (C-21 enforcement depth). C-21 is the "coupling verified" floor; C-22 is the "revision is structured and auditable" ceiling.
- **Text**: When Phase 2c identifies a WEAK or REVISE boundary, the revision directive follows a structured format parallel to the Phase 5 amendment format: Boundary (which of the five) / Deficient-section (which section is misaligned) / Deficiency (what is wrong in one sentence) / Before (the deficient sentence verbatim) / After (the revised sentence) / Re-verify (COUPLED / WEAK / REVISE re-applied after the revision). Open-ended revision notes ("revise for alignment") cannot be audited; structured directives can. C-21 fires the check; C-22 governs the repair format.
- **Pass condition**: When at least one WEAK or REVISE is found in Phase 2c, the output includes a structured directive for each flagged boundary, with all six fields (Boundary, Deficient-section, Deficiency, Before, After, Re-verify) populated. A boundary-status table with a general note ("revised for alignment") does not satisfy this criterion. Pass vacuously if all boundaries are COUPLED.

### C-23 -- Bridge Integration Verified Post-Merge
- **Weight**: aspirational
- **Category**: format
- **Source**: R5 excellence signal V-02 (bridge integration as named phase). C-12 is the "bridges planned" floor; C-20 is the type-first ceiling; C-23 is the post-merge integration verification ceiling. C-10 (coherent paragraph) is the closest prior criterion; C-23 adds lifecycle structure that editorial review cannot provide.
- **Text**: A Phase 3b verification step is positioned after merge (Phase 3) and before journal variant (Phase 4). It produces a five-row table -- one row per section boundary -- confirming each of the five Phase 2b bridge phrases (by their exact wording or recognizable variant) appears in the merged prose. Any N (bridge absent or replaced by a stock connector: "however", "additionally", "furthermore", "moreover", "therefore") triggers paragraph revision that restores the intended bridge phrase. Stock connectors are not bridges; they convey no semantic relationship. Phase 2b bridge planning is wasted if stock connectors overwrite it at merge time.
- **Pass condition**: Output includes a Phase 3b verification table with one row per section boundary (Background-Gap, Gap-Claim, Claim-Method, Method-Result, Result-Implication), each row containing the planned bridge phrase and a Y / N integration status. At least one N row must trigger a visible paragraph revision, OR all five Y with the bridge phrase quoted from the merged prose. A Phase 3b table with no bridge phrase evidence does not pass.

### C-24 -- Self-Diagnosis Amendment Targets Weakest Element
- **Weight**: aspirational
- **Category**: depth
- **Source**: R5 excellence signal V-03 (5th self-diagnosis amendment). C-07 requires three fixed amendment slots; C-16 requires a named prose-coherence amendment. C-24 is the unconstrained self-diagnosis ceiling: the model identifies its own weakest point without being told which category to examine.
- **Text**: After all prior amendments are applied (including the prose coherence amendment), a final Amendment 5 is added to Phase 5. The model reads the post-amendment abstract and identifies the single weakest remaining element -- the one sentence or transition most likely to draw editorial rejection or reviewer confusion. The diagnosed weakness must differ from all prior amendment targets (Gap, Result, Implication, prose coherence) and must be stated as a specific claim ("the Method sentence understates scope" or "the Implication overpromises relative to the Result"). A generic self-compliment ("the abstract is now strong") fails this criterion. This tests whether the model has calibrated quality perception beyond fixed-category instruction.
- **Pass condition**: Phase 5 includes an Amendment 5 slot. The output names a specific remaining weakness as a one-sentence claim. The weakness differs from the prior four amendment targets. A Before/After revision is applied. The Before/After pair shows a substantive change traceable to the diagnosed weakness.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                    |
|--------------|-----------------|--------|-----------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                               |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.                 |
| Aspirational | C-09 to C-24    | 20     | Separates good from excellent. Only V-05-class-and-above implementations ceiling. |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v5

| Change              | Detail                                                                                                                                          |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| C-10 reduced        | 4->2 pts. C-23 (bridge integration post-merge) and C-24 (self-diagnosis amendment) structurally enforce what C-10 measured editorially. C-10 is now the coherence floor. |
| C-17 reduced        | 2->1 pt. Universally passing all R5 variations -- becoming baseline expectation.                                                                |
| C-19 reduced        | 2->1 pt. Universally passing all R5 variations -- becoming baseline expectation.                                                                |
| C-20 reduced        | 2->1 pt. C-23 captures the post-merge bridge integration ceiling; C-20 remains the type-planning floor.                                        |
| C-21 reduced        | 2->1 pt. C-22 captures the structured-directive ceiling; C-21 remains the coupling-verified floor.                                             |
| C-22 added          | Coupling revision uses structured directive format -- from R5 V-01 signal. 2 pts. Structured-directive ceiling above C-21 floor.               |
| C-23 added          | Bridge integration verified post-merge -- from R5 V-02 signal. 2 pts. Phase 3b lifecycle position; new ceiling above C-12/C-20 planning chain. |
| C-24 added          | Self-diagnosis amendment targets weakest element -- from R5 V-03 signal. 2 pts. Unconstrained Amendment 5 ceiling above C-07 fixed slots.      |
| Tier description    | Updated to reflect C-09 to C-24 aspirational range.                                                                                            |
| Aspirational subtotal | Remains 20 pts. Total remains 100.                                                                                                          |
