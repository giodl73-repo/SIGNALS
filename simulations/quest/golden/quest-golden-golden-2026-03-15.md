---
skill: quest-golden
date: 2026-03-15
rounds_to_convergence: 2
rubric_version: v1
composite_score: 100
status: golden
selected_from: R2-V-02 (most minimal 100-scorer; 5/5 variations tied; minimal structure tiebreak)
---

# quest-golden — Golden Prompt

**Converged:** Round 2 (R1 zero new patterns + R2 zero new patterns = QUEST PLATEAUED;
all essential criteria PASS in R2 = TRIAL CONVERGED)

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
both found zero new excellence patterns.
One zero-pattern round is not enough. Two consecutive zero-pattern rounds are required.
Both rounds must be cited by explicit name -- not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria. A round where all {N}
variations produce identical composite scores generates no excellence patterns and does not
advance plateau detection.

Causal constraint: identical composite scores -> no score spread -> no excellence patterns ->
round does not count toward the two consecutive zero-pattern rounds required for GATE 2.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity

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
| COMPOSITE |        |      |      |      |     |
| RANK      |        |      |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another:
```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
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

DO NOT proceed to Step 4 until all patterns are named with mechanism stated.

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

State what Step 3 found in the CURRENT ROUND: [pattern names] OR "no new patterns."
State what Step 3 found in the IMMEDIATELY PRECEDING ROUND by name: [patterns] OR "no new patterns."
Name both rounds explicitly (e.g., "Round 2 and Round 3").

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.
