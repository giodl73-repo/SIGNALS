Here is the complete v4 rubric.

---

**Two new criteria from R3 signals:**

**C-17 — All-section constraint coverage** (2 pts, depth)
V-02 is the only R3 variation to earn C-11 full PASS (4/4) — by putting *Why:* on all six sections, not two. C-11 remains as the "at least two" floor. C-17 is the ceiling: when every rule is explained, the model self-corrects edge cases not covered by examples.

**C-18 — Paper type declared before Claim** (2 pts, format)
V-02 is the only R3 variation to earn C-09 full PASS (2/2) — via a forced "Paper type: empirical / theoretical" declaration before writing Claim. All other variations state the tense rule but provide no forcing function, making it advisory. The declaration is the mechanism.

**Point redistribution (aspirational stays at 20, total stays at 100):**

| Criterion | Change | Reason |
|-----------|--------|--------|
| C-11 | 4→2 pts | C-17 captures the ceiling; C-11 remains the floor |
| C-15 | 2→1 pt | Universally passing R3 — becoming baseline |
| C-16 | 2→1 pt | Universally passing R3 — becoming baseline |
| C-17 | +2 pts | New (all-section coverage) |
| C-18 | +2 pts | New (paper-type declaration) |

**R4 candidate noted on C-12**: V-03's bridge table with all five labeled section-boundary pairs is the natural C-12 excellence mechanism — candidate C-19 for v5 if a variation demonstrates it cleanly at R4.
ive section-boundary pairs labeled and purposeful (non-stock) connectors. A "bridge table with labeled boundaries" criterion is the natural C-12 excellence ceiling. Candidate for C-19 in v5 if a variation demonstrates it cleanly at R4.

**Aspirational subtotal**: Remains 20 pts. Total remains 100.

---

## Criteria Summary Table

| ID   | Name                                    | Weight       | Category    | Points |
|------|-----------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present              | essential    | correctness | 10     |
| C-02 | Word count within target                | essential    | correctness | 10     |
| C-03 | Artifact written to correct path        | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal             | essential    | correctness | 10     |
| C-05 | Signal acquisition executed             | essential    | behavior    | 10     |
| C-06 | Result section is quantified            | recommended  | depth       | 10     |
| C-07 | Amendment pass produces three distinct  | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly       | recommended  | correctness | 10     |
| C-09 | Claim uses correct tense convention     | aspirational | depth       | 2      |
| C-10 | Abstract reads as a single coherent paragraph | aspirational | format | 4      |
| C-11 | Constraint reasoning stated             | aspirational | depth       | 2      |
| C-12 | Connective bridges planned before merge | aspirational | format      | 2      |
| C-13 | Amendment non-triviality guard applied  | aspirational | depth       | 2      |
| C-14 | Gap drafted first to ground background  | aspirational | format      | 2      |
| C-15 | Draft phase targets coverage only       | aspirational | format      | 1      |
| C-16 | Prose coherence is a named amendment    | aspirational | depth       | 1      |
| C-17 | All-section constraint coverage         | aspirational | depth       | 2      |
| C-18 | Paper type declared before Claim        | aspirational | format      | 2      |

---

**Two new aspirational criteria added from R3 signals:**

**C-17** (2 pts) — Every section (all six) carries a *Why:* rationale. Exceeds C-11's "at least two" floor. Source: R3 Signal 1 `all-section-constraint-coverage`. Mechanistically enables a model to self-correct edge cases not covered by examples.

**C-18** (2 pts) — An explicit "Paper type: empirical / theoretical" declaration is made before writing the Claim section. The declaration forces tense convention rather than advising it. Source: R3 Signal 2 `paper-type-forced-declaration`. Mechanistically enables C-09 full PASS.

**Point redistribution**: C-11 reduced 4→2 (C-17 is the excellence ceiling; C-11 remains as the floor). C-15 reduced 2→1 (universally passing R3 — now baseline). C-16 reduced 2→1 (universally passing R3 — now baseline). Two new criteria at 2 pts each. Aspirational subtotal remains 20. Total remains 100.

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
- **Source**: R2 scoring: only V-02 achieves this via explicit tense check in Pass B. Reduced 4→2 pts in v3. C-18 (v4) captures the forcing mechanism.
- **Text**: The Claim section follows academic tense convention: past tense for empirical results, present tense for theoretical contributions. The distinction reflects timeless logical truths (present) vs. historical experimental events (past).
- **Pass condition**: Claim tense matches the paper contribution type. Empirical paper uses past tense; theory/argument paper uses present tense. Mixed papers use past for findings, present for implications.

### C-10 -- Abstract Reads as a Single Coherent Paragraph
- **Weight**: aspirational
- **Category**: format
- **Text**: The merged abstract (Phase 3) reads as prose, not as six labeled sentences stapled together. Transitions are natural and the paragraph has narrative flow from context through finding to significance.
- **Pass condition**: No section labels appear in the merged paragraph. Adjacent sentences have logical connectives or implicit flow. The paragraph would not be rejected on stylistic grounds by a journal editor.

### C-11 -- Constraint Reasoning Is Stated
- **Weight**: aspirational
- **Category**: depth
- **Source**: R1 excellence signal E-01 (explain-why-not-just-what). Reduced 4→2 pts in v4; C-17 is the all-section excellence ceiling.
- **Text**: For at least two of the key constraints (gap framing, result quantification, tense convention), the skill explains the reason the rule exists, not just the rule itself. An AI that understands the motivation can self-correct edge cases not covered by examples.
- **Pass condition**: At least two of C-04, C-06, or C-09 are accompanied by a one-sentence rationale explaining why the constraint exists (e.g., "goal framing implies the paper might have failed; gap framing states a fact about the field").

### C-12 -- Connective Bridges Planned Before Merge
- **Weight**: aspirational
- **Category**: format
- **Source**: R1 excellence signal E-02 (connective-bridges-pre-merge). R2 result: universal fail across all 5 variations. Reduced 4→2 pts in v3 to reflect structural debt status. R3 result: V-03 achieves full PASS via an explicit bridge table with all five section-boundary pairs labeled and purposeful (non-stock) connectors — the natural excellence mechanism. R4 candidate C-19: bridge table with labeled boundary pairs.
- **Text**: A 3-8 word connective phrase is composed after each section draft, before the merge step. These phrases become the logical glue in Phase 3, forcing narrative flow to be a first-class authoring concern rather than a post-hoc editorial fix.
- **Pass condition**: Output includes connective bridge phrases between section drafts (or the merged paragraph shows tight logical connectives at each section boundary). The Background-to-Gap and Result-to-Implication transitions are explicit, not implied.

### C-13 -- Amendment Non-Triviality Guard Applied
- **Weight**: aspirational
- **Category**: depth
- **Source**: R1 excellence signal E-03 (anti-trivial-amendment-guard). Universally passing in R3 — approaching baseline expectation.
- **Text**: Phase 5 explicitly guards against low-effort compliance by stating that a restatement of the prior sentence is not an amendment. Before/after comparison is shown for each amendment slot, making the change visible and verifiable.
- **Pass condition**: Phase 5 output includes before/after text for at least 2 of the 3 amendments. At least 2 of the 3 produce a visible textual change -- not a paraphrase of the same sentence.

### C-14 -- Gap Drafted First to Ground Background
- **Weight**: aspirational
- **Category**: format
- **Source**: R1 excellence signal (gap-first-causal-scaffold)
- **Text**: The Gap section is drafted before the Background section, so Background is written knowing precisely what gap it must scaffold toward. This produces tighter Background-to-Gap semantic flow at merge time: the Background ends where the Gap begins.
- **Pass condition**: Execution order shows Gap drafted first (or Phase 1 notes show gap extraction preceding background drafting). The Background sentence and Gap sentence read as cause and effect -- Background establishes the conditions; Gap names the open problem those conditions create.

### C-15 -- Draft Phase Targets Coverage Only
- **Weight**: aspirational
- **Category**: format
- **Source**: R2 excellence signal (amendment-over-draft-discipline). V-05 scored 88 -- highest in R2 -- by separating phase responsibilities. Universally passing in R3 -- reduced 2→1 pt in v4 as it becomes baseline expectation.
- **Text**: Phase 2 produces a complete six-section draft without inline self-correction or precision revision loops. The draft is expected to be imprecise; that is Phase 5's job. Mixing coverage and correctness in one pass increases overhead and reduces amendment depth because the model conflates completeness with quality.
- **Pass condition**: Phase 2 output shows no inline revision commentary or self-correction notes. Phase 5 carries the full precision load: Before/After evidence, non-triviality guard, and explicit amendment targets.

### C-16 -- Prose Coherence Is a Named Amendment Target
- **Weight**: aspirational
- **Category**: depth
- **Source**: R2 excellence signal (prose-coherence-as-amendment-target). V-05 is the only R2 variation to earn C-10 PASS via this mechanism. Universally passing in R3 -- reduced 2→1 pt in v4 as it becomes baseline expectation.
- **Text**: Phase 5 includes a dedicated amendment slot whose explicit target is prose coherence -- sentence-level flow, transition quality, or readability. Prose coherence is a named, verifiable goal, not an emergent side effect of the merge step.
- **Pass condition**: Phase 5 amendment list includes one amendment explicitly labeled for prose coherence or readability. The amendment shows Before/After evidence of a prose-level change (not a content change). This amendment is the primary mechanism for earning C-10.

### C-17 -- All-Section Constraint Coverage
- **Weight**: aspirational
- **Category**: depth
- **Source**: R3 excellence signal (all-section-constraint-coverage). V-02 R3 is the only variation to earn C-11 full PASS (4/4) by carrying *Why:* rationale on all six sections. C-11 remains as the "at least two" floor; C-17 is the ceiling.
- **Text**: Every section instruction (all six: Background, Gap, Claim, Method, Result, Implication) carries an explicit *Why:* rationale explaining the criterion it enforces -- not just two. When every rule is explained, the model can self-correct edge cases not covered by examples. An implementation that explains all six sections shows it has internalized the abstract's structural logic, not memorized rules.
- **Pass condition**: All six section drafting instructions include at least one *Why:* sentence explaining the reason the constraint exists. Partial credit (1 pt) if four or five sections carry rationale. Zero if three or fewer.

### C-18 -- Paper Type Declared Before Claim
- **Weight**: aspirational
- **Category**: format
- **Source**: R3 excellence signal (paper-type-forced-declaration). V-02 R3 is the only variation to earn C-09 full PASS (2/2) via an explicit forced declaration. All other R3 variations state the tense rule but provide no forcing function -- making tense convention advisory, not constrained.
- **Text**: Before writing the Claim section, the skill forces an explicit paper-type declaration ("Paper type: empirical / theoretical") that binds the tense convention for the Claim. A rule without a declaration is advisory; a forced declaration is a structural constraint. The declaration is the mechanism that makes C-09 reliably achievable -- without it, models apply the tense rule inconsistently.
- **Pass condition**: Phase 2 output includes an explicit paper-type classification step before or during Claim drafting. The classification ("empirical" or "theoretical") is stated, and the Claim tense matches it.

---

## Tier Descriptions

| Tier         | Criteria        | Points | Interpretation                                                                  |
|--------------|-----------------|--------|---------------------------------------------------------------------------------|
| Essential    | C-01 to C-05    | 50     | Hard fails. Any miss disqualifies the run for gold.                             |
| Recommended  | C-06 to C-08    | 30     | Expected in a competent implementation. Missing one is a warning.               |
| Aspirational | C-09 to C-18    | 20     | Separates good from excellent. Only V-02-class implementations reach ceiling.   |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v3

| Change              | Detail                                                                                                                         |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|
| C-11 reduced        | 4→2 pts. C-17 captures the all-section excellence ceiling; C-11 remains as "at least two" floor.                              |
| C-15 reduced        | 2→1 pt. Universally passing in R3 — becoming baseline expectation, no longer a differentiator.                                |
| C-16 reduced        | 2→1 pt. Universally passing in R3 — becoming baseline expectation, no longer a differentiator.                                |
| C-17 added          | All-section constraint coverage -- from R3 Signal 1 (all-section-constraint-coverage). 2 pts. V-02 R3 reference implementation.|
| C-18 added          | Paper type declared before Claim -- from R3 Signal 2 (paper-type-forced-declaration). 2 pts. V-02 R3 reference implementation. |
| C-12 note updated   | V-03 R3 achieves C-12 PASS via bridge table with labeled boundary pairs. Candidate C-19 noted for v5.                         |
| Aspirational subtotal | Remains 20 pts. Total remains 100.                                                                                           |
