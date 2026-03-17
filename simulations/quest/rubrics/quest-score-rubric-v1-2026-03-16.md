---
skill: quest-rubric
skill_target: quest-score
date: 2026-03-16
version: 1
---

# Scoring Rubric -- quest-score

`quest-score` takes N skill outputs and a rubric, then produces: per-criterion verdicts
with evidence, composite scores, a ranked leaderboard, excellence signals, failure
patterns, and (when prior-round data exists) regression signals.

This rubric evaluates whether a `quest-score` output fulfills that contract.

Lessons incorporated from the 2026-03-15 rubric cycle (v1 through v10):
- Evidence grounding (C-02) is the highest-frequency failure mode; PARTIAL is not evidence.
- Failure patterns (C-05) is the primary diagnostic value of batch scoring; omission cannot be excused.
- Regression signals (C-08) must carry an explicit N/A note in round 1 -- PARTIAL, not FAIL.
- Score formula fidelity (C-03) must require explicit calculation, not just the final number.
- Load verification (C-01a) is a prerequisite correctness check, not a formality.

---

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PARTIAL counts as 0.5 toward pass count.
FAIL counts as 0.
Golden threshold: all essential PASS + composite >= 80.

N_essential = 5, N_recommended = 3, N_aspirational = 2.

---

## Criteria

### ESSENTIAL -- must all pass

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Rubric load verification** -- the output confirms the rubric was read; lists all criteria IDs and tiers, states the formula, and names the golden threshold before scoring begins | correctness | A load summary block exists (table, list, or prose) that names: (a) all criteria IDs with their tier labels, (b) the exact composite formula text, (c) the golden threshold condition, and (d) the count or list of outputs being scored. PARTIAL if any one of the four is missing. FAIL if the rubric is not referenced at all. |
| C-02 | **Per-criterion verdict matrix** -- every rubric criterion has a PASS/PARTIAL/FAIL verdict for every scored output | correctness | A table, prose block set, or equivalent structure exists where each criterion-output pair has an explicit verdict. No criterion-output cell is blank, merged-without-explanation, or implied. PARTIAL if verdicts exist for all criteria but one or more outputs are absent. FAIL if any criterion row is missing entirely. |
| C-03 | **Evidence for every verdict** -- every PASS/PARTIAL/FAIL verdict is backed by a direct quote, paraphrase, or specific structural reference to the scored output | correctness | No verdict stands alone as a label. Each criterion-output verdict is accompanied by text that references the output specifically -- either a quoted passage, a named section or line, or a structural observation about the output's format or content. PARTIAL if evidence exists for most verdicts but one or more are bare labels without reference. FAIL if a majority of verdicts lack evidence, or if evidence is present but consistently restates the criterion rather than quoting or referencing the output. |
| C-04 | **Composite score per output** -- each scored output has a numeric composite score computed from its verdict counts, shown with explicit calculation | correctness | A score is present for every output. The score is derived from a weighted formula (essential/recommended/aspirational tier counts). The calculation is shown explicitly -- e.g., "V-XX: E=X/5, R=X/2, A=X/1 -> composite = YY" -- not just the final number. PARTIAL if scores are present but calculations are omitted or partial. FAIL if scores are absent for any output. |
| C-05 | **Failure patterns section** -- criteria that receive zero PASS across all scored outputs are identified as failure patterns, or their absence is explicitly stated | coverage | A section labeled "Failure Patterns" (or equivalent) exists. Any criterion receiving no PASS across all N outputs is named. If no such criterion exists, the output states that explicitly (e.g., "No failure patterns -- all criteria passed in at least one output"). FAIL if the section is omitted entirely or if a criterion that failed across all outputs is not surfaced. |

### RECOMMENDED -- output is better with these

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Ranked leaderboard** -- all scored outputs are listed in descending composite score order; ties are noted explicitly | format | A leaderboard or ranking section exists. All N outputs appear, ordered from highest to lowest composite score. Ties are broken (with stated rule) or explicitly noted as tied. PARTIAL if the leaderboard exists but some outputs are absent or the order cannot be verified from stated scores. FAIL if the section is absent or ordering is implicit ("see scores above"). |
| C-07 | **Excellence signals** -- outputs scoring unusually high on a specific criterion are identified; any criterion where one output clearly leads the field is named with the structural feature that produced the outlier | depth | An "excellence signals" section exists. At least one specific output-criterion pair is highlighted with an explanation of what structural feature in that output produced the higher score. Generic comments ("V-05 scored highest overall") do not satisfy this criterion -- the signal must name the criterion and the mechanism. If no outlier pair exists, that is stated explicitly. |
| C-08 | **Per-output synthesis notes** -- each scored output has a brief narrative note explaining its key score drivers: what it did structurally that raised or lowered its score relative to other outputs | depth | A narrative note exists for each output beyond its verdict table or prose blocks. Each note explains at least one structural feature of the output that differentiates its score -- not a restatement of the verdict counts. PARTIAL if notes exist for most but not all outputs, or if notes only list counts without explaining mechanism. |

### ASPIRATIONAL -- raise the bar once essential/recommended are stable

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Regression signals** -- if a prior-round scorecard is provided, any criterion-output pair that degraded from PASS (or PARTIAL) to a lower verdict since the prior round is flagged | behavior | A regression section exists. If prior-round data was provided, any PASS->FAIL or PASS->PARTIAL degradation is named with the criterion ID, output ID, and prior verdict. If no regressions occurred, that is stated. If no prior-round file was provided or available, the output writes "No prior round data -- regression analysis cannot be performed" and the criterion receives PARTIAL (not FAIL). |
| C-10 | **Score arithmetic verification** -- the composite scores in the output are arithmetically correct given the stated verdict counts and formula | correctness | At least one composite score in the output can be independently verified from the stated PASS/PARTIAL/FAIL counts and formula. Arithmetic errors are absent or flagged. PARTIAL if scores are stated without enough detail to verify. FAIL if a score is demonstrably wrong given the stated counts. |

---

## Weight Summary

| Tier | Criteria | N | Weight |
|------|----------|---|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 |
| Recommended | C-06, C-07, C-08 | 3 | 30 |
| Aspirational | C-09, C-10 | 2 | 10 |

**Formula (explicit):**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

Score at all essential + all recommended + all aspirational: 100.
Score at all essential + all recommended + no aspirational: 90.
Score at all essential + no recommended + no aspirational: 60.
Golden threshold: all 5 essentials PASS AND composite >= 80.

---

## Scoring Notes

**C-01 (load verification):** The load summary can appear anywhere before the first output
is scored -- preamble, header block, or first phase. What matters is that it precedes scoring,
not that it appears in a specific format.

**C-02 (verdict matrix):** Formats vary -- table cells, prose blocks labeled by output, or
grouped criterion blocks -- as long as every criterion-output combination has a stated verdict.
Implied verdicts ("all PASS") count only when the N is small and the claim is unambiguous.

**C-03 (evidence):** Evidence that restates the criterion ("the output has a leaderboard")
does not satisfy C-03. Evidence must refer to the output's specific content: a quoted phrase,
a section title, a structural observation about the output's layout, or a line-level reference.
The test: could you find the referenced feature in the output using only the evidence text?

**C-04 (composite score):** "Explicit calculation" means the tier counts are stated before the
final score is given (e.g., "E=4/5, R=2/3, A=1/2"). A final number alone is PARTIAL.

**C-05 (failure patterns):** The section is required even when empty. The correct empty-section
text is: "No failure patterns -- all criteria passed in at least one output." Omitting the
section entirely is FAIL even when the scoring otherwise looks complete.

**C-06 (leaderboard):** A table that happens to be sorted by score satisfies C-06 only if the
sort order is unambiguous. "See scores above" or a pointer to the composite score table does
not satisfy C-06 -- the ranking must be restated as a ranked list or explicitly sorted table.

**C-07 (excellence signals):** "V-05 scored highest overall" is not an excellence signal. An
excellence signal requires a specific output-criterion pairing with a structural explanation.
Example: "V-03 leads on C-02 because it names the line number of the evidence quote in each
cell, making every verdict independently verifiable without re-reading the output."

**C-08 (per-output notes):** Notes that only list "PASS x4, PARTIAL x1" do not satisfy C-08.
The note must explain what the output did structurally that drove its result.

**C-09 (regression):** Round 1 N/A rule: if no prior-round file exists, writing the prescribed
N/A statement earns PARTIAL. Omitting the section entirely earns FAIL.

**C-10 (arithmetic):** Score this criterion by picking one output and verifying its composite
from the stated counts and formula. PARTIAL if counts are absent (cannot verify). FAIL only
if a demonstrable arithmetic error exists.

---

## Design Notes

**Why C-01 (load verification) is Essential, not Recommended:**
The prior cycle showed that scorers who skip or abbreviate the load step produce verdict
matrices with incorrect criterion counts, missing N/A rules, and wrong formula denominators.
A missing load summary is a leading indicator of downstream errors in C-02 through C-04.
Making it Essential surfaces this class of error early.

**Why C-03 (evidence) requires explicit output reference, not restatement:**
The highest-frequency failure mode in the prior cycle (observed across Rounds 1-6) was
scorers writing evidence that restates the criterion name instead of quoting the output.
"The output provides evidence for each verdict" is not evidence; it is circular. The pass
condition is written to force a specific reference because generic observations consistently
produced scorecards that could not drive rubric evolution -- they had no diagnostic content.

**Why C-05 (failure patterns) is Essential:**
Failure patterns are the primary value of batch scoring over single-output scoring. A score
report that does not surface criteria failing across all outputs cannot tell you whether the
rubric has a gap or the skill has a design issue. Without this section, the scoring exercise
cannot produce actionable output. Demoting it to Recommended would allow outputs to pass
golden threshold while omitting the analysis that makes batch scoring useful.

**Why C-06 (leaderboard) is Recommended, not Essential:**
The leaderboard is a navigation aid, not a primary output. The composite scores in C-04
contain the same information; the leaderboard reorganizes them for readability. A scoring
output missing only the leaderboard is still useful for rubric evolution -- it is degraded,
not broken.
