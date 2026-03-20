Written to `simulations/quest/rubrics/specify-abstract-rubric-v2-2026-03-19.md`. Here is the complete rubric:

---

# specify-abstract -- Evaluation Rubric v2

**14 criteria across 3 tiers. Total: 100 points.**
**Golden threshold**: C-01 through C-05 all pass AND composite >= 80.

---

## Scoring Summary

| ID   | Criterion                               | Weight       | Category    | Points |
|------|-----------------------------------------|--------------|-------------|--------|
| C-01 | Six-part structure present              | essential    | correctness | 10     |
| C-02 | Word count within target                | essential    | correctness | 10     |
| C-03 | Artifact written to correct path        | essential    | behavior    | 10     |
| C-04 | Gap framed as gap, not goal             | essential    | correctness | 10     |
| C-05 | Signal acquisition executed             | essential    | behavior    | 10     |
| C-06 | Result section is quantified            | recommended  | depth       | 10     |
| C-07 | Amendment pass: 3 distinct changes      | recommended  | depth       | 10     |
| C-08 | Journal variant applied correctly       | recommended  | correctness | 10     |
| C-09 | Claim uses correct tense                | aspirational | depth       | 4      |
| C-10 | Abstract reads as coherent prose        | aspirational | format      | 4      |
| C-11 | Constraint reasoning stated             | aspirational | depth       | 4      |
| C-12 | Connective bridges planned before merge | aspirational | format      | 4      |
| C-13 | Amendment non-triviality guard applied  | aspirational | depth       | 2      |
| C-14 | Gap drafted first to ground background  | aspirational | format      | 2      |

---

**Four new aspirational criteria added from R1 signals:**

**C-11** (4 pts) — At least two key constraints include a one-sentence rationale explaining *why* the rule exists. Source: E-01 `explain-why-not-just-what`. Also back-ported into C-04, C-06, and C-07 text.

**C-12** (4 pts) — A 3-8 word connective phrase is composed after each section draft, before the merge step. Source: E-02 `connective-bridges-pre-merge`.

**C-13** (2 pts) — Phase 5 includes before/after text for at least 2 amendments and at least 2 produce visible textual change. Source: E-03 `anti-trivial-amendment-guard`. Also back-ported into C-07 text.

**C-14** (2 pts) — Gap is drafted before Background so Background scaffolds toward a known gap. Source: `gap-first-causal-scaffold`.

**Point redistribution**: Essential reduced 12→10 pts each (freeing 10 pts); aspirational expanded from 2 criteria (10 pts) to 6 criteria (20 pts). Total remains 100.
s in range, or if over-range the output includes an explicit compression attempt with before/after counts.

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
- **Source**: R1 excellence signal E-01 (explain-why-not-just-what)
- **Text**: For at least two of the key constraints (gap framing, result quantification, tense convention), the skill explains the reason the rule exists, not just the rule itself. An AI that understands the motivation can self-correct edge cases not covered by examples.
- **Pass condition**: At least two of C-04, C-06, or C-09 are accompanied by a one-sentence rationale explaining why the constraint exists (e.g., "goal framing implies the paper might have failed; gap framing states a fact about the field").

### C-12 -- Connective Bridges Planned Before Merge
- **Weight**: aspirational
- **Category**: format
- **Source**: R1 excellence signal E-02 (connective-bridges-pre-merge)
- **Text**: A 3-8 word connective phrase is composed after each section draft, before the merge step. These phrases become the logical glue in Phase 3, forcing narrative flow to be a first-class authoring concern rather than a post-hoc editorial fix.
- **Pass condition**: Output includes connective bridge phrases between section drafts (or the merged paragraph shows tight logical connectives at each section boundary). The Background-to-Gap and Result-to-Implication transitions are explicit, not implied.

### C-13 -- Amendment Non-Triviality Guard Applied
- **Weight**: aspirational
- **Category**: depth
- **Source**: R1 excellence signal E-03 (anti-trivial-amendment-guard)
- **Text**: Phase 5 explicitly guards against low-effort compliance by stating that a restatement of the prior sentence is not an amendment. Before/after comparison is shown for each amendment slot, making the change visible and verifiable.
- **Pass condition**: Phase 5 output includes before/after text for at least 2 of the 3 amendments. At least 2 of the 3 produce a visible textual change -- not a paraphrase of the same sentence.

### C-14 -- Gap Drafted First to Ground Background
- **Weight**: aspirational
- **Category**: format
- **Source**: R1 excellence signal (gap-first-causal-scaffold)
- **Text**: The Gap section is drafted before the Background section, so Background is written knowing precisely what gap it must scaffold toward. This produces tighter Background-to-Gap semantic flow at merge time: the Background ends where the Gap begins.
- **Pass condition**: Execution order shows Gap drafted first (or Phase 1 notes show gap extraction preceding background drafting). The Background sentence and Gap sentence read as cause and effect -- Background establishes the conditions; Gap names the open problem those conditions create.

---

## Tier Descriptions

| Tier         | Criteria      | Points | Interpretation                                                                  |
|--------------|---------------|--------|---------------------------------------------------------------------------------|
| Essential    | C-01 to C-05  | 50     | Hard fails. Any miss disqualifies the run for gold.                             |
| Recommended  | C-06 to C-08  | 30     | Expected in a competent implementation. Missing one is a warning.               |
| Aspirational | C-09 to C-14  | 20     | Separates good from excellent. Only V-05-class implementations reach ceiling.   |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v1

| Change               | Detail                                                                                               |
|----------------------|------------------------------------------------------------------------------------------------------|
| Point redistribution | Essential 12->10 pts each; aspirational split 6 criteria (4+4+4+4+2+2) to maintain 100 total        |
| C-04 text            | Added rationale sentence (goal framing implies failure) per E-01                                     |
| C-06 text            | Added motivational framing (uninformative, signals weak paper) per E-01                              |
| C-07 text            | Added anti-restatement guard (a restatement is not an amendment) per E-03                            |
| C-11 added           | Constraint reasoning stated -- from R1 E-01 (explain-why-not-just-what)                              |
| C-12 added           | Connective bridges planned before merge -- from R1 E-02 (connective-bridges-pre-merge)               |
| C-13 added           | Amendment non-triviality guard applied -- from R1 E-03 (anti-trivial-amendment-guard)                |
| C-14 added           | Gap drafted first to ground background -- from R1 (gap-first-causal-scaffold)                        |
