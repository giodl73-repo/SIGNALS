Written to `simulations/quest/rubrics/prove-websearch-rubric-v2-2026-03-14.md`.

---

**15 criteria across 3 tiers — max 110 pts:**

| ID | Text (short) | Weight | Pts | Source |
|----|-------------|--------|-----|--------|
| C-01 | URL-grounded claims | essential | 12 | v1 |
| C-02 | Direct quote with attribution | essential | 12 | v1 |
| C-03 | Structured search record | essential | 12 | v1 |
| C-04 | Hypothesis relevance stated | essential | 12 | v1 |
| C-05 | Evidence strength rated | essential | 12 | v1 |
| C-06 | Multi-query coverage | recommended | 10 | v1 |
| C-07 | Balanced evidence set | recommended | 10 | v1 |
| C-08 | Source credibility assessment | recommended | 10 | v1 |
| C-09 | Cross-source synthesis | aspirational | 5 | v1 |
| C-10 | Query refinement trail | aspirational | 5 | v1 |
| **C-11** | **Phase-gate enforcement** | aspirational | 2 | R1 `phase-gate-vs-step` |
| **C-12** | **Live-phase trail placement** | aspirational | 2 | R1 `live-trail-placement` |
| **C-13** | **Named-target gate framing** | aspirational | 2 | R1 `gate-framing-names-target` |
| **C-14** | **Structured synthesis sub-fields** | aspirational | 2 | R1 excellence signal |
| **C-15** | **Rule-first constraint ordering** | aspirational | 2 | R1 excellence signal |

**Key design decisions:**
- Max score expands to 110 (not renormalized) so R1 variations retain their scores — V-05 would score ~106/110 retroactively.
- Golden threshold stays at "all 5 essential + composite >= 80," unchanged.
- C-11-C-15 are aspirational, not recommended — they reward structural sophistication that goes beyond correctness guarantees. A prompt can be golden (80+) without any of them.
- Each new criterion includes a `Derived from:` line linking it back to the R1 pattern so the lineage is traceable.
h quote is attributed to its source URL. Paraphrases, if used at all, are clearly
  labelled as such and the source URL is still provided.
- **Pass condition**: At least one direct quote (verbatim text in quotation marks) per
  source cited. No unattributed paraphrase presented as evidence.

---

### C-03 -- Structured Search Record
- **Category**: format
- **Weight**: essential
- **Text**: For each search performed, the output records: (a) the exact query string used,
  (b) the list of sources found, and (c) the evidence extracted from each source.
- **Pass condition**: Each search block contains all three fields -- query, sources, and
  extracted evidence. Missing any field in any search block fails this criterion.

---

### C-04 -- Hypothesis Relevance Stated
- **Category**: coverage
- **Weight**: essential
- **Text**: For each piece of evidence, the output explicitly states how the evidence
  relates to the hypothesis being investigated (supports, refutes, or is neutral/mixed).
- **Pass condition**: Every evidence item includes an explicit relevance label or sentence
  linking it to the hypothesis. Generic evidence with no stated connection fails.

---

### C-05 -- Evidence Strength Rated
- **Category**: correctness
- **Weight**: essential
- **Text**: Each source or evidence block is rated for strength using the prescribed
  vocabulary: strong / weak / mixed. The rating is justified with at least one sentence.
- **Pass condition**: Every source has a strength rating from {strong, weak, mixed} with
  a one-sentence justification. Missing or unjustified ratings fail this criterion.

---

## Recommended Criteria (weight: 30 pts total, 10 pts each)

### C-06 -- Multi-Query Coverage
- **Category**: depth
- **Weight**: recommended
- **Text**: The investigation uses more than one query to explore the hypothesis from
  different angles (e.g., pro framing, con framing, domain-specific terms). Single-query
  outputs are less thorough and may miss contrarian evidence.
- **Pass condition**: At least two distinct query strings are present in the output, with
  queries visibly different in framing or terminology.

---

### C-07 -- Balanced Evidence Set
- **Category**: coverage
- **Weight**: recommended
- **Text**: The output includes evidence on both sides of the hypothesis -- both supporting
  and refuting sources -- or explicitly documents that only one-sided evidence was found
  after attempting balanced queries.
- **Pass condition**: At least one supporting and one refuting (or mixed) evidence item
  is present, OR the output contains a documented note that refuting/supporting evidence
  could not be found despite targeted queries.

---

### C-08 -- Source Credibility Assessment
- **Category**: depth
- **Weight**: recommended
- **Text**: For each source, the output notes the credibility or authority of the source
  (e.g., peer-reviewed, industry report, news outlet, blog, forum). This helps the reader
  calibrate confidence in the evidence.
- **Pass condition**: At least half of cited sources have a credibility note (one phrase
  or label is sufficient). Outputs with zero credibility notes fail.

---

## Aspirational Criteria (weight: 20 pts total)

### C-09 -- Cross-Source Synthesis (5 pts)
- **Category**: depth
- **Weight**: aspirational
- **Text**: After presenting individual evidence items, the output provides a synthesis
  section that identifies where sources converge, where they conflict, and what the
  aggregate evidence says about the hypothesis. This is beyond per-source analysis.
- **Pass condition**: A synthesis paragraph or section is present that references at least
  two sources by name and draws a cross-source conclusion about the hypothesis.

---

### C-10 -- Query Refinement Trail (5 pts)
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The output shows iterative search behavior -- initial queries, results that
  prompted refinement, and the refined queries that followed. This demonstrates active
  epistemic hygiene rather than a single-pass search.
- **Pass condition**: At least one instance of documented query refinement is present,
  showing the original query, what gap it revealed, and the follow-up query used.

---

### C-11 -- Phase-Gate Enforcement (2 pts)
- **Category**: structure
- **Weight**: aspirational
- **Derived from**: R1 pattern `phase-gate-vs-step`
- **Text**: Multi-query and balance requirements are enforced via explicit "GATE: do not
  proceed" checkpoints rather than numbered steps. Gates are structurally harder to skip
  under output pressure because they require a binary verdict before the next phase can
  begin. Numbered steps allow the model to proceed regardless of whether the step's
  condition was met.
- **Pass condition**: At least C-06 and C-07 requirements are enforced by named GATE
  blocks (not numbered steps) that contain an explicit "do not proceed" or equivalent
  stop condition.

---

### C-12 -- Live-Phase Trail Placement (2 pts)
- **Category**: behavior
- **Weight**: aspirational
- **Derived from**: R1 pattern `live-trail-placement`
- **Text**: The query refinement trail (C-10) is placed in the search/collection phase,
  not in the synthesis phase. Placement during the live search captures observed behavior
  at the moment of observation. Placement in the synthesis phase forces retrospective
  reconstruction from memory, which is less accurate and loses the causal link between
  gap-discovery and query adjustment.
- **Pass condition**: The query refinement trail field appears inside the search record
  (alongside query, sources, evidence) rather than in a post-synthesis section.

---

### C-13 -- Named-Target Gate Framing (2 pts)
- **Category**: correctness
- **Weight**: aspirational
- **Derived from**: R1 pattern `gate-framing-names-target`
- **Text**: The gate condition for multi-query coverage names the specific epistemic target
  of Q2 (e.g., "Q2 must explicitly target the refutation side"), not just "distinct framing
  or terminology." Naming the target closes the semantic loophole where two slightly
  different pro-hypothesis queries satisfy the letter of "2 distinct queries" while failing
  the spirit of adversarial coverage.
- **Pass condition**: The GATE or instruction for multi-query coverage explicitly identifies
  what Q2 must attack (refutation, null hypothesis, opposing mechanism). A gate that only
  requires "distinct framing" without naming the target does not pass.

---

### C-14 -- Structured Synthesis Sub-Fields (2 pts)
- **Category**: format
- **Weight**: aspirational
- **Derived from**: R1 excellence signal (pre-printed synthesis sub-fields > prose instruction)
- **Text**: The synthesis section uses pre-printed sub-fields (e.g., Convergence:,
  Conflict:, Conclusion:) rather than a prose instruction to "write a paragraph naming
  two sources." Pre-printed fields require the model to produce three distinct sub-answers.
  A prose instruction can be satisfied by a single paragraph that addresses only one
  dimension, making C-09 easier to nominally pass without genuine multi-dimensional
  synthesis.
- **Pass condition**: The synthesis section contains at least two named sub-fields
  (labels followed by a required fill-in). A single undivided synthesis paragraph does
  not pass, even if it references multiple sources.

---

### C-15 -- Rule-First Constraint Ordering (2 pts)
- **Category**: structure
- **Weight**: aspirational
- **Derived from**: R1 excellence signal (rules enumerated before content fields)
- **Text**: The skill prompt enumerates hard constraints (no training-data evidence,
  verbatim quotes only, URL required per claim) in a numbered rules block before the
  Topic and Hypothesis fields. Rule-first ordering ensures constraints are parsed before
  content is seen, reducing the probability that rules are treated as trailing caveats
  and glossed over during output generation.
- **Pass condition**: A numbered or labeled rules block appears before the first content
  input field (Topic, Hypothesis, or equivalent). Rules that appear only inline within
  later sections, or only as footnotes, do not pass.

---

## Criterion Summary

| ID   | Text (short)                     | Weight       | Category    | Pts |
|------|----------------------------------|--------------|-------------|-----|
| C-01 | URL-grounded claims              | essential    | correctness | 12  |
| C-02 | Direct quote with attribution    | essential    | correctness | 12  |
| C-03 | Structured search record         | essential    | format      | 12  |
| C-04 | Hypothesis relevance stated      | essential    | coverage    | 12  |
| C-05 | Evidence strength rated          | essential    | correctness | 12  |
| C-06 | Multi-query coverage             | recommended  | depth       | 10  |
| C-07 | Balanced evidence set            | recommended  | coverage    | 10  |
| C-08 | Source credibility assessment    | recommended  | depth       | 10  |
| C-09 | Cross-source synthesis           | aspirational | depth       |  5  |
| C-10 | Query refinement trail           | aspirational | behavior    |  5  |
| C-11 | Phase-gate enforcement           | aspirational | structure   |  2  |
| C-12 | Live-phase trail placement       | aspirational | behavior    |  2  |
| C-13 | Named-target gate framing        | aspirational | correctness |  2  |
| C-14 | Structured synthesis sub-fields  | aspirational | format      |  2  |
| C-15 | Rule-first constraint ordering   | aspirational | structure   |  2  |

**Total max: 110 pts.**

---

## Scoring Examples

All 5 essential pass, 2 of 3 recommended pass, 0 aspirational:

```
score = 60 + (2/3 * 30) + 0
      = 60 + 20 + 0
      = 80  --> meets golden threshold (all essential + composite >= 80)
```

All 5 essential pass, 1 of 3 recommended pass, 0 aspirational:

```
score = 60 + (1/3 * 30) + 0
      = 60 + 10 + 0
      = 70  --> fails golden threshold (composite < 80)
```

All 5 essential pass, 3 of 3 recommended pass, all 7 aspirational pass:

```
score = 60 + 30 + (5+5+2+2+2+2+2)
      = 60 + 30 + 20
      = 110  --> perfect score
```

V-05 retroactive score under v2 (C-11 not addressed in R1, C-12/C-13/C-14 PASS,
C-15 not assessed in R1):

```
conservative: 100 + 0 + 2 + 2 + 2 + 0 = 106 / 110
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, max 100 pts |
| v2 | 2026-03-14 | +5 aspirational criteria (C-11-C-15) from R1 excellence signals; max 110 pts |
