Rubric written to `simulations/quest/rubrics/prove-websearch-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (5) | URL-grounded claims, direct quotes with attribution, structured search record, hypothesis relevance stated, evidence strength rated | 60 |
| Recommended (3) | Multi-query coverage, balanced evidence set, source credibility assessment | 30 |
| Aspirational (2) | Cross-source synthesis, query refinement trail | 10 |

The essential criteria enforce the three hardest constraints from the skill spec: no training-data claims (C-01), verbatim quotes not paraphrases (C-02), and the required per-search structure of query + sources + evidence (C-03). C-04/C-05 enforce the hypothesis relevance and strength rating fields that must appear on every evidence item.

Golden threshold requires all 5 essential to pass plus composite >= 80 — meaning at least 2 of 3 recommended criteria must also pass.
tly disclaimed.

---

### C-02 -- Direct Quotation with Attribution
- **Category**: correctness
- **Weight**: essential
- **Text**: Evidence is presented as direct quotes from source material, not paraphrases.
  Each quote is attributed to its source URL. Paraphrases, if used at all, are clearly
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

## Recommended Criteria (weight: 30 pts total)

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

## Aspirational Criteria (weight: 10 pts total)

### C-09 -- Cross-Source Synthesis
- **Category**: depth
- **Weight**: aspirational
- **Text**: After presenting individual evidence items, the output provides a synthesis
  section that identifies where sources converge, where they conflict, and what the
  aggregate evidence says about the hypothesis. This is beyond per-source analysis.
- **Pass condition**: A synthesis paragraph or section is present that references at least
  two sources by name and draws a cross-source conclusion about the hypothesis.

---

### C-10 -- Query Refinement Trail
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The output shows iterative search behavior -- initial queries, results that
  prompted refinement, and the refined queries that followed. This demonstrates active
  epistemic hygiene rather than a single-pass search.
- **Pass condition**: At least one instance of documented query refinement is present,
  showing the original query, what gap it revealed, and the follow-up query used.

---

## Criterion Summary

| ID   | Text (short)                  | Weight       | Category    |
|------|-------------------------------|--------------|-------------|
| C-01 | URL-grounded claims           | essential    | correctness |
| C-02 | Direct quote with attribution | essential    | correctness |
| C-03 | Structured search record      | essential    | format      |
| C-04 | Hypothesis relevance stated   | essential    | coverage    |
| C-05 | Evidence strength rated       | essential    | correctness |
| C-06 | Multi-query coverage          | recommended  | depth       |
| C-07 | Balanced evidence set         | recommended  | coverage    |
| C-08 | Source credibility assessment | recommended  | depth       |
| C-09 | Cross-source synthesis        | aspirational | depth       |
| C-10 | Query refinement trail        | aspirational | behavior    |

---

## Scoring Example

All 5 essential pass, 2 of 3 recommended pass, 0 of 2 aspirational pass:

```
score = (5/5 * 60) + (2/3 * 30) + (0/2 * 10)
      = 60 + 20 + 0
      = 80  --> meets golden threshold (all essential + composite >= 80)
```

All 5 essential pass, 1 of 3 recommended pass, 0 aspirational:

```
score = (5/5 * 60) + (1/3 * 30) + (0/2 * 10)
      = 60 + 10 + 0
      = 70  --> fails golden threshold (all essential pass but composite < 80)
```
