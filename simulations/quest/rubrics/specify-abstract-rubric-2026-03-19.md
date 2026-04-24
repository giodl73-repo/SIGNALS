Rubric written to `simulations/quest/rubrics/specify-abstract-rubric-2026-03-19.md`.

**10 criteria across 3 tiers:**

**Essential (5) — hard fails if any miss:**
- C-01: All six sections present (Background/Gap/Claim/Method/Result/Implication)
- C-02: Word count 200-250 (300 for arxiv), with compression attempt if over
- C-03: Artifact at correct path with required frontmatter fields
- C-04: Gap framed as gap ("X remains unresolved"), not goal ("we aimed to...")
- C-05: Signal acquisition actually executed — content grounded in topic signals

**Recommended (3):**
- C-06: Result section quantified with a number or strength descriptor
- C-07: Phase 5 amendment produces 3 distinct non-trivial improvements
- C-08: Journal variant structurally applied when flag present (vacuous pass otherwise)

**Aspirational (2):**
- C-09: Claim tense matches paper type (past=empirical, present=theoretical)
- C-10: Merged paragraph reads as coherent prose, not labeled sentences
urnal:arxiv`). The artifact reports the word count and status (UNDER / ON TARGET / OVER). If OVER, a compression pass was attempted.
- **Pass condition**: Word count is in range, or if over-range the output includes explicit compression attempt with before/after counts.

### C-03 — Artifact Written to Correct Path
- **Weight**: essential
- **Category**: behavior
- **Text**: Output file is written to `signals/specify/abstract/{topic}-abstract-{date}.md` (or `--output <path>/` if flag provided). Frontmatter includes: `skill: specify-abstract`, `topic`, `date`, `word_count`, and `journal` (if specified).
- **Pass condition**: File exists at the expected path and frontmatter contains all required fields.

### C-04 — Gap Framed as Gap, Not Goal
- **Weight**: essential
- **Category**: correctness
- **Text**: The Gap section names what is unresolved or unknown ("X remains unresolved"), not a research goal ("we aimed to study X"). This is the inertia framing required by the skill spec.
- **Pass condition**: Gap sentence does not use goal-framing phrases ("we aimed", "we sought to", "this paper investigates"). It makes a claim about the state of the field.

### C-05 — Signal Acquisition Executed
- **Weight**: essential
- **Category**: behavior
- **Text**: Phase 1 is executed: the skill globs `signals/**/{topic}-*` and reads available artifacts (paper draft, specify-spec, discover-hypothesis) before writing the abstract. The abstract reflects extracted signals, not generic filler.
- **Pass condition**: Output shows evidence of signal-informed content (e.g., references the topic's actual claim or method, not lorem ipsum). Glob results are visible or the artifact content is clearly grounded in topic signals.

---

## Recommended Criteria (30 points total)

### C-06 — Result Section Is Quantified
- **Weight**: recommended
- **Category**: depth
- **Text**: The Result section includes at least one quantified finding — effect size, percentage, count, or qualitative strength descriptor — not just "we found improvements."
- **Pass condition**: Result sentence contains a number, percentage, or explicit qualitative strength claim ("strong", "substantial", "no significant difference").

### C-07 — Amendment Pass Produces Three Distinct Improvements
- **Weight**: recommended
- **Category**: depth
- **Text**: Phase 5 produces three labeled amendments: (1) Gap sharpened to name a specific unresolved question, (2) Result quantified if not already, (3) Implication tightened to one concrete enabling action. Each amendment is distinct and non-trivial.
- **Pass condition**: All three amendment slots are filled with substantive revisions, not restatements of the prior text. At least two of the three result in visible textual changes.

### C-08 — Journal Variant Applied Correctly
- **Weight**: recommended
- **Category**: correctness
- **Text**: If `--for journal:<name>` is specified, the abstract register matches the journal's requirements (e.g., Nature/Science: broad significance lead + societal implication; PNAS: effect size in result; cognitive-science: theoretical advance in implication; arxiv: technical precision, 300-word limit).
- **Pass condition**: When a journal flag is present, the abstract text shows at least two structural adjustments matching the journal profile. Pass vacuously if no journal flag provided.

---

## Aspirational Criteria (10 points total)

### C-09 — Claim Uses Correct Tense Convention
- **Weight**: aspirational
- **Category**: depth
- **Text**: The Claim section follows academic tense convention: past tense for empirical results ("we found that X increases Y by Z%"), present tense for theoretical contributions ("we show that X implies Y"). The distinction is correctly applied to the paper type.
- **Pass condition**: Claim tense matches the paper's contribution type. Empirical paper uses past tense; theory/argument paper uses present tense. Mixed papers use past for findings, present for implications.

### C-10 — Abstract Reads as a Single Coherent Paragraph
- **Weight**: aspirational
- **Category**: format
- **Text**: The merged abstract (Phase 3) reads as prose, not as six labeled sentences stapled together. Transitions are natural and the paragraph has narrative flow from context through finding to significance.
- **Pass condition**: No section labels appear in the merged paragraph. Adjacent sentences have logical connectives or implicit flow. The paragraph would not be rejected on stylistic grounds by a journal editor.

---

## Scoring Summary Table

| ID   | Criterion                          | Weight        | Category    | Points |
|------|------------------------------------|---------------|-------------|--------|
| C-01 | Six-part structure present         | essential     | correctness | 12     |
| C-02 | Word count within target           | essential     | correctness | 12     |
| C-03 | Artifact written to correct path   | essential     | behavior    | 12     |
| C-04 | Gap framed as gap, not goal        | essential     | correctness | 12     |
| C-05 | Signal acquisition executed        | essential     | behavior    | 12     |
| C-06 | Result section is quantified       | recommended   | depth       | 10     |
| C-07 | Amendment pass: 3 distinct changes | recommended   | depth       | 10     |
| C-08 | Journal variant applied correctly  | recommended   | correctness | 10     |
| C-09 | Claim uses correct tense           | aspirational  | depth       | 5      |
| C-10 | Abstract reads as coherent prose   | aspirational  | format      | 5      |

**Total**: 100 points
**Golden threshold**: C-01 through C-05 all pass AND composite >= 80
