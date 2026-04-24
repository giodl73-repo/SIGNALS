---
skill: quest-rubric
skill_target: quest-score
date: 2026-03-15
version: 1
---

# Scoring Rubric -- quest-score

`quest-score` takes N skill outputs and a rubric, then produces: per-criterion verdicts with
evidence, composite scores, a ranked leaderboard, excellence signals, failure patterns, and
(when prior-round data exists) regression signals.

This rubric evaluates whether a `quest-score` output fulfills that contract.

---

## Composite Score Formula

```
composite = (essential_pass/N_essential * 60)
          + (recommended_pass/N_recommended * 30)
          + (aspirational_pass/N_aspirational * 10)
```

PARTIAL counts as 0.5 toward pass count.
Golden threshold: all essential PASS + composite >= 80.

---

## Criteria

### ESSENTIAL -- must all pass

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Per-criterion verdict matrix** -- every rubric criterion has a PASS/PARTIAL/FAIL verdict for every scored output | correctness | A table or equivalent structure exists where each row is a criterion and each column is a scored output; no criterion-output cell is blank or missing |
| C-02 | **Evidence for every verdict** -- every PASS/PARTIAL/FAIL is backed by a direct quote or specific reference to the scored output | correctness | No verdict stands alone; each cell (or its accompanying note) includes a quote, paraphrase, or location reference from the actual output |
| C-03 | **Composite score per output** -- each scored output has a numeric composite score computed from the verdict counts | correctness | Score values are present for all N outputs; the formula (essential/recommended/aspirational weighted sum) is applied correctly or the score is derivable from the stated counts |
| C-04 | **Ranked leaderboard** -- all outputs are ranked by composite score, highest to lowest | format | A ranking list or section exists; outputs appear in descending score order; ties are broken or noted |
| C-05 | **Failure patterns called out** -- criteria that fail across ALL scored outputs are identified as failure patterns, or absence of failure patterns is explicitly noted | coverage | A "failure patterns" section (or equivalent) exists; any criterion with zero PASS across all N outputs is surfaced; if no such criterion exists, that absence is stated |

### RECOMMENDED -- output is better with these

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Excellence signals** -- outputs scoring unusually high on a specific criterion are identified; any criterion where one output clearly leads the field is named | depth | An "excellence signals" section (or equivalent) exists; at least one output-criterion pair is highlighted as an outlier high performer, with a brief explanation of why; if no outlier exists, that is stated |
| C-07 | **Per-output evidence notes** -- each scored output has a narrative section summarizing its axis wins, degradations, and key differentiators from other outputs | depth | A section per output exists beyond the verdict table; each section explains *why* the output scored the way it did, referencing at least one specific structural feature |

### ASPIRATIONAL -- raise the bar once essential/recommended are stable

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-08 | **Regression signals** -- if a prior-round score file is referenced or available, outputs that passed a criterion in round N-1 but fail in round N are flagged | behavior | A regression section exists and identifies any criterion-output pair that degraded from PASS (or PARTIAL) since the prior round; if no prior-round data is available or no regressions occurred, that is stated explicitly |

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 |
| Recommended | C-06, C-07 | 30 |
| Aspirational | C-08 | 10 |

---

## Scoring Notes

**C-01 (verdict matrix):** Formats vary -- table, indented list, or grouped blocks -- as long
as every criterion-output cell has a stated verdict. Implied verdicts ("all PASS" in a notes
column) count only if unambiguous.

**C-02 (evidence):** A shared Notes column covering all outputs for a criterion satisfies the
requirement if the note is specific enough to verify each output's verdict. Generic notes
("all use the correct form") satisfy C-02 only when the form is narrow and unambiguous.

**C-03 (composite score):** The score need not be labelled "composite" -- any
denominator-based or weighted score counts. "X/Y" fractions satisfy C-03 if the scoring
formula is documented elsewhere in the output.

**C-04 (leaderboard):** A final ranking list, a score table sorted by score, or a "Ranking"
section all satisfy C-04. The ranking must be explicit -- a table that happens to be sorted
satisfies this only if the ordering is unambiguous.

**C-05 (failure patterns):** A criterion failing in all outputs signals either a rubric gap or
a systematic skill design issue. Surfacing this is the primary diagnostic value of batch
scoring. A score report that omits this analysis cannot drive rubric evolution.

**C-06 (excellence signals):** An excellence signal requires a *specific* output-criterion
pairing, not a general comment that one output scored highest overall. The signal should name
what structural feature produced the outlier score.

**C-07 (per-output notes):** Notes that only list PASS/FAIL counts do not satisfy C-07.
The note must explain the mechanism behind the score: what the output did structurally
differently that drove its result.

**C-08 (regression):** N/A in round 1 (no prior data). Round-1 outputs should receive
PARTIAL rather than FAIL if they explicitly state "no prior round data available."

---

## Machine-Readable Footer

A conformant `quest-score` output ends with:

```json
{"top_score": <float>, "all_essential_pass": <bool>, "new_patterns": [<string>, ...]}
```

The rubric does not score for this footer, but scorers should note its presence as a signal
of output completeness and machine-parseability.
