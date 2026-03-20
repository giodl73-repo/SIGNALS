Done. Here's what changed in v3:

**Two new criteria from R2 signals:**

- **C-15 — Draft phase targets coverage only** (2 pts, format): Phase 2 is permissive — no inline self-correction, no precision revision loops. Phase 5 carries the full correctness load. Source: V-05's 88-point performance showed that separating "coverage" from "correctness" into distinct phases beats trying to do both in the draft pass.

- **C-16 — Prose coherence is a named amendment target** (2 pts, depth): Phase 5 must include a dedicated amendment slot explicitly targeting prose coherence with Before/After evidence. This is the mechanism that makes C-10 achievable — V-05 was the only R2 variation to earn C-10 PASS, via exactly this mechanism. All other variations hoped coherence would emerge from merge.

**Point redistribution (keeps total at 100):**

- C-09: 4→2 pts (only V-02 achieves it; requires explicit tense-check mechanism)
- C-12: 4→2 pts (universal fail across all R2 variations; the R3 candidate note confirms it needs a structural Phase step, not a criterion retrofit)

**R3 signal preserved in C-12 note**: the connective bridges criterion remains but is flagged as structural debt — it needs a phase change to become achievable.
  | 4      |
| C-11 | Constraint reasoning stated             | aspirational | depth       | 4      |
| C-12 | Connective bridges planned before merge | aspirational | format      | 2      |
| C-13 | Amendment non-triviality guard applied  | aspirational | depth       | 2      |
| C-14 | Gap drafted first to ground background  | aspirational | format      | 2      |
| C-15 | Draft phase targets coverage only       | aspirational | format      | 2      |
| C-16 | Prose coherence is a named amendment    | aspirational | depth       | 2      |

---

**Two new aspirational criteria added from R2 signals:**

**C-15** (2 pts) — Phase 2 is permissive (coverage only); Phase 5 carries the full correctness load. No self-correction overhead in the draft pass. Source: R2 Signal 1 `amendment-over-draft-discipline`.

**C-16** (2 pts) — Phase 5 includes a dedicated amendment slot whose explicit target is prose coherence. Coherence is a named goal, not emergent from merge. Source: R2 Signal 2 `prose-coherence-as-amendment-target`. Mechanistically enables C-10.

**Point redistribution**: C-09 reduced 4->2 (only V-02 achieves it; requires explicit tense-check mechanism absent by default). C-12 reduced 4->2 (universal fail across all R2 variations; requires structural Phase step -- criterion retrofit insufficient). Two new criteria at 2 pts each. Aspirational subtotal remains 20. Total remains 100.

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
- **Source**: R2 scoring: only V-02 achieves this via explicit tense check in Pass B. Reduced 4->2 pts.
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
- **Source**: R1 excellence signal E-02 (connective-bridges-pre-merge). R2 result: universal fail across all 5 variations. Requires an explicit Phase step, not a criterion retrofit. Reduced 4->2 pts to reflect structural debt status.
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

### C-15 -- Draft Phase Targets Coverage Only
- **Weight**: aspirational
- **Category**: format
- **Source**: R2 excellence signal (amendment-over-draft-discipline). V-05 scored 88 -- highest in R2 -- by separating phase responsibilities: Phase 2 for coverage, Phase 5 for correctness.
- **Text**: Phase 2 produces a complete six-section draft without inline self-correction or precision revision loops. The draft is expected to be imprecise; that is Phase 5's job. Mixing coverage and correctness in one pass increases overhead and reduces amendment depth because the model conflates completeness with quality.
- **Pass condition**: Phase 2 output shows no inline revision commentary or self-correction notes. Phase 5 carries the full precision load: Before/After evidence, non-triviality guard, and explicit amendment targets.

### C-16 -- Prose Coherence Is a Named Amendment Target
- **Weight**: aspirational
- **Category**: depth
- **Source**: R2 excellence signal (prose-coherence-as-amendment-target). V-05 is the only R2 variation to earn C-10 PASS -- via a 4th amendment slot explicitly targeting prose coherence. All other variations relied on coherence emerging from merge.
- **Text**: Phase 5 includes a dedicated amendment slot whose explicit target is prose coherence -- sentence-level flow, transition quality, or readability. Prose coherence is a named, verifiable goal, not an emergent side effect of the merge step.
- **Pass condition**: Phase 5 amendment list includes one amendment explicitly labeled for prose coherence or readability. The amendment shows Before/After evidence of a prose-level change (not a content change). This amendment is the primary mechanism for earning C-10.

---

## Tier Descriptions

| Tier         | Criteria      | Points | Interpretation                                                                  |
|--------------|---------------|--------|---------------------------------------------------------------------------------|
| Essential    | C-01 to C-05  | 50     | Hard fails. Any miss disqualifies the run for gold.                             |
| Recommended  | C-06 to C-08  | 30     | Expected in a competent implementation. Missing one is a warning.               |
| Aspirational | C-09 to C-16  | 20     | Separates good from excellent. Only V-05-class implementations reach ceiling.   |

**Golden threshold**: all essential pass AND composite >= 80.

---

## Changelog from v2

| Change               | Detail                                                                                                          |
|----------------------|-----------------------------------------------------------------------------------------------------------------|
| C-09 reduced         | 4->2 pts. Only V-02 achieves it; requires explicit tense-check mechanism absent from all other variations.      |
| C-12 reduced         | 4->2 pts. Universal fail across all R2 variations. Structural Phase step required -- criterion retrofit is not enough. |
| C-15 added           | Draft phase targets coverage only -- from R2 Signal 1 (amendment-over-draft-discipline). 2 pts.                 |
| C-16 added           | Prose coherence is a named amendment target -- from R2 Signal 2 (prose-coherence-as-amendment-target). 2 pts.   |
| C-16 note            | Primary mechanism for earning C-10. Explicit 4th amendment slot vs. hoped-for emergent quality.                 |
| R3 candidate noted   | V-03 (gap-first + constraint reasoning) + V-01 (hardened Before/After) combination predicted ~90 pts.           |
| Aspirational subtotal| Remains 20 pts. Total remains 100.                                                                              |
