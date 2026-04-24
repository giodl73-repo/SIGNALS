---
skill: quest-golden
date: 2026-03-16
source_variation: V-01 (R4, inertia-framing, composite 100.00)
qu5_pass: true
original_word_count: 1140
simplified_word_count: 877
reduction_pct: 23.1
all_essential_still_pass: true
status: simplified-golden
---

# quest-golden -- QU5 Simplified Golden Prompt

## Simplified Prompt Body

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE -- READ THIS FIRST

This loop runs until BOTH of the following gates are satisfied SIMULTANEOUSLY in the same round:

GATE 1 -- TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy an essential criterion. Only PASS counts.

GATE 2 -- QUEST PLATEAUED
Step 3 (excellence patterns) in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND
both found zero new excellence patterns. Two consecutive zero-pattern rounds are required.
Both rounds must be cited by explicit name -- not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
inertia-framing | scoring-granularity

Label each variation:
```
## V-NN -- [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 -- SCORE EACH VARIATION

Score every variation against every rubric criterion using PASS / FAIL.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[text from the variation body that confirms or denies, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | V-03 | ... |
|-----------|--------|------|------|------|-----|
| C-01      | E      |      |      |      |     |
| C-02      | E      |      |      |      |     |
| C-03      | E      |      |      |      |     |
| C-04      | E      |      |      |      |     |
| C-05      | E      |      |      |      |     |
| C-06      | R      |      |      |      |     |
| C-07      | R      |      |      |      |     |
| C-08      | R      |      |      |      |     |
| C-09      | A      |      |      |      |     |
| C-10      | A      |      |      |      |     |
| C-11      | A      |      |      |      |     |
| C-12      | A      |      |      |      |     |
| C-13      | A      |      |      |      |     |
| C-14      | A      |      |      |      |     |
| COMPOSITE |        |      |      |      |     |
| RANK      |        |      |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/6 * 10)

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another, complete this
template in full:

```
Pattern name: [short label]
Structural property: [the design element present in better-scoring variations, absent from
                     worse-scoring ones -- must be a named structural feature, not a
                     variation ID or an outcome description]
Contrast: "V-NN had [structural property]; V-MM did not."
Mechanism: [how the structural property causes the criterion result difference]
Principle: [reusable design rule derived from the structural property]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until ALL patterns are named AND mechanism stated for each.
This gate requires completeness for ALL patterns in the current round -- not just the first
pattern encountered. Name every pattern found, state mechanism for each, before proceeding.

---

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five required fields:
```
ID:             C-[NN] (next sequential after current rubric's highest)
Text:           [what the criterion measures, one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence, no interpretation required]
```

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

GATE 1 -- TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 -- PLATEAU DETECTION

Iteration history (append one row per round executed):

| Round | Variation IDs scored | Top composite | Excellence signals found  | Criterion added  |
|-------|---------------------|---------------|---------------------------|-----------------|
| R-NN  | V-01..V-{N}         | [score]       | [signal names or "none"]  | [C-NN or "none"]|

Convergence state table (fill before declaring any result):

| Round   | Step 3 patterns    | New patterns? | Loop state          |
|---------|--------------------|---------------|---------------------|
| [R N-1] | [names or "none"]  | Y / N         | RUNNING / PLATEAUED |
| [R N]   | [names or "none"]  | Y / N         | RUNNING / PLATEAUED |

State definitions:
- RUNNING: fewer than two consecutive zero-pattern rounds recorded.
- PLATEAUED: current round AND immediately preceding round both show N. Entry condition:
  two consecutive rounds with zero new excellence patterns in Step 3.
- GOLDEN (terminal): PLATEAUED and TRIAL CONVERGED in the same round. Entry condition:
  both gates satisfied simultaneously.

Fill both tables before declaring any result. Name both rounds explicitly in the plateau check.

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden.
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write a "What Made It Golden" section immediately after the prompt body in the same file.
   Include at least two mechanism descriptions. Each must state:
   (a) the round in which the mechanism was first discovered, and
   (b) the output gap it closed.

4. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.
   Include an "Ablated criteria" section at the end: list every criterion that received zero
   activations across all rounds, with a suggested targeted probe approach for each. If no
   criteria were ablated across all rounds, write "No ablated criteria."

5. State both file paths.

---

## QU5 Simplification Report

### What was removed and why

| Removed block | Word count | Rubric work done | Reason for removal |
|---------------|-----------|------------------|--------------------|
| "WHAT THIS LOOP REPLACES" section (4 bullets + closing paragraph) | 136 | 0 of 14 criteria | Inertia-framing axis -- R4 scorecard confirmed zero criterion coverage. Context only. |
| Active spread-design second sentence ("A round where all {N} variations...") | 22 | 0 | Explanatory consequence already covered by GATE 2 definition in DUAL CONVERGENCE. |
| "Causal constraint: identical composite scores -> ..." block | 25 | 0 | Further elaboration of same causal chain; GATE 2 is the authoritative statement. |
| "Requirements for this template" block (2 bullets in STEP 3) | 55 | 0 | Restates constraints already embedded in the template field descriptions (Structural property field already says "not a variation ID"; Contrast field already shows "V-NN had X; V-MM did not"). |
| Example format line in artifact #3 | 13 | 0 | Illustrative only. The requirement is fully stated in (a) and (b) above it. |
| "Generic prose without round citations..." line in artifact #3 | 12 | 0 | Negative restatement of the positive requirement in (a). Adds no new constraint. |

**Total removed: 263 words**

### Essential criteria verification (post-simplification)

| Criterion | Pass? | Evidence in simplified prompt |
|-----------|-------|-------------------------------|
| C-01 -- Dual convergence gate declaration | PASS | GATE 1 + GATE 2 defined; "Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round" |
| C-02 -- Golden prompt written verbatim | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-03 -- Final rubric as standalone artifact | PASS | "Write the accumulated rubric...to: simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md" |
| C-04 -- QU2 (Step 3) precedes QU3 (Step 4) | PASS | STEP 3 appears before STEP 4 in step sequence |
| C-05 -- Rubric present at loop start | PASS | "Current rubric ({rubric-version}): {rubric-content}" in header |

All 5 essential: **PASS**

All 3 recommended also preserved:
- C-06: iteration history table with all 4 fields -- PASS
- C-07: labeled `Contrast:` field -- PASS
- C-08: five-field criterion template -- PASS

All 6 aspirational also preserved:
- C-09: "What Made It Golden" with (a) round + (b) gap citations -- PASS
- C-10: Ablated criteria section instruction -- PASS
- C-11: state table with RUNNING / PLATEAUED / GOLDEN + entry conditions -- PASS
- C-12: `Structural property:` labeled field in STEP 3 template -- PASS
- C-13: "DO NOT proceed to Step 4 until ALL patterns are named AND mechanism stated" -- PASS
- C-14: `Contrast:` as labeled named slot in template -- PASS

**All 14 criteria: PASS. Predicted composite: 100.00.**
