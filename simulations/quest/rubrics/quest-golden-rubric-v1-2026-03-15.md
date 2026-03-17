---
skill: quest-rubric
skill_target: quest-golden
date: 2026-03-15
version: 1
---

# Rubric: quest-golden

Evaluates output of the `quest-golden` skill, which finds the golden prompt through
systematic variation and scoring. The skill must run a full variation-score-extract-propose
loop until dual convergence: all scenarios pass (trial converged) AND no new excellence
patterns for 2 consecutive rounds (quest plateaued).

---

## Scoring Formula

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
```

Golden threshold: **all 5 essential criteria pass AND composite >= 80.**

---

## Essential Criteria (must all pass)

| ID   | Category  | Text | Pass Condition |
|------|-----------|------|----------------|
| C-01 | behavior  | Full 4-phase loop executed in every round: generate variations, score each against rubric, identify excellence patterns, propose rubric criteria. | Output contains all four labeled phases (or equivalent headings) with substantive content in each, in every round reported. |
| C-02 | behavior  | Every variation is scored criterion-by-criterion; per-criterion pass/fail is shown for all variations before composite is computed. | A score matrix or equivalent table is present showing each criterion result for each variation; no variation has only a composite without individual scores. |
| C-03 | correctness | Both convergence gates are checked independently: TRIAL (all variations pass every essential criterion) and PLATEAU (no new excellence patterns in this round AND the immediately preceding round). | Output explicitly states TRIAL CONVERGED/NOT CONVERGED and QUEST PLATEAUED/NOT PLATEAUED as separate declarations with stated evidence for each. |
| C-04 | format    | On dual convergence, the golden prompt is written as a complete, runnable skill body — not a summary, description, or excerpt. | The golden artifact file contains the full prompt text that could be copied verbatim and used as a skill; it is not paraphrased or truncated. |
| C-05 | format    | On dual convergence, the final rubric is written as a Markdown document containing all criteria accumulated across all rounds. | A rubric artifact file is produced listing every criterion (ID, weight, category, text, pass condition) active at the time of convergence. |

---

## Recommended Criteria (output is better with these)

| ID   | Category    | Text | Pass Condition |
|------|-------------|------|----------------|
| C-06 | depth       | Each excellence pattern is named and stated as a reusable principle — not merely "V-02 scored higher than V-01" but the structural property that caused the difference. | At least one named pattern per round that produced spread; pattern statement identifies the mechanism (what prompt property is present in passing variations and absent from failing ones). |
| C-07 | correctness | Each rubric criterion proposed from an excellence pattern includes all five required fields: ID, text, weight, category, pass condition. | Every proposed criterion block contains all five fields; no field is missing or left blank. |
| C-08 | behavior    | When declaring QUEST PLATEAUED, both rounds are cited explicitly by name (e.g., "Round 3 and Round 4: no new patterns found"). | The plateau declaration includes two round identifiers by name, not "the last two rounds" or equivalent vague reference. |

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

| ID   | Category  | Text | Pass Condition |
|------|-----------|------|----------------|
| C-09 | structure | The generation step contains an active spread-design instruction that causes the operator to produce divergent variations before writing them — not a post-hoc RANK row that reveals spread after the fact. | The variation-generation phase includes explicit language instructing how to vary axes (e.g., "Round 1: vary only one axis; Round 2+: combine axes that produced signal") prior to any scoring step. |
| C-10 | depth     | The prompt explains *why* rounds where all variations produce identical composite scores stall plateau detection — the causal mechanism, not just that they do. | Output contains a sentence or annotation stating the causal link: identical scores produce no new excellence patterns, and no new patterns means the round does not count toward the two-round plateau gate. |

---

## Criterion Summary

| ID   | Weight       | Category    | Short Label |
|------|--------------|-------------|-------------|
| C-01 | essential    | behavior    | 4-phase loop present every round |
| C-02 | essential    | behavior    | Per-criterion scores for all variations |
| C-03 | essential    | correctness | Both convergence gates declared independently |
| C-04 | essential    | format      | Golden artifact = full runnable skill body |
| C-05 | essential    | format      | Final rubric artifact = all accumulated criteria |
| C-06 | recommended  | depth       | Pattern named as reusable principle with mechanism |
| C-07 | recommended  | correctness | Proposed criterion has all 5 fields |
| C-08 | recommended  | behavior    | Plateau declaration cites both rounds by name |
| C-09 | aspirational | structure   | Generation phase has active spread-design instruction |
| C-10 | aspirational | depth       | Causal explanation for why identical-score rounds stall plateau |
