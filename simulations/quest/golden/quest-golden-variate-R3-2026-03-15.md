# quest-golden Variate -- Round 3

**Date:** 2026-03-15
**Skill:** quest-golden
**Rubric:** v2 (C-01 through C-13; essential C-01-C-05; aspirational C-09-C-13)
**Round:** R3 -- combination pass (R2 signals combined + new feedback loop)

---

## SPREAD-DESIGN PHASE

Rubric state entering R3: v2, C-01..C-13. Aspirational pool: C-09, C-10, C-11, C-12, C-13 (5 criteria).

R2 signals that became v2 additions:
- V-03 (lifecycle-emphasis / PHASE 0): spread-design as dedicated labeled phase -> C-11
- V-01 (scoring-granularity): PARTIAL as meaningful intermediate state -> C-12
- V-04 (scoring-granularity + phrasing-register): causal "why" annotation per step -> C-13

R3 axis assignment plan:

| Plan | Axis | Target Criterion | Predicted Composite |
|------|------|-----------------|---------------------|
| V-01 | role-sequence + scoring-granularity | C-02, C-03, C-09, C-10 (strong R2 baseline) | 95 |
| V-02 | lifecycle-emphasis (SPREAD-DESIGN as named phase) | C-11 | 96 |
| V-03 | scoring-granularity (PARTIAL-as-amplifier) | C-12 | 97 |
| V-04 | phrasing-register (causal-layer annotation) | C-13 | 97 |
| V-05 | role-sequence + lifecycle-emphasis + scoring-granularity + phrasing-register + feedback loop | C-11 + C-12 + C-13 + new | 100 |

Divergence check: 95 / 96 / 97 / 97 / 100. At least two target different criteria. PROCEED.

---

## Round 3 Variation Map

| V | Axes | What Changed | Primary Target |
|---|------|--------------|----------------|
| V-01 | role-sequence + scoring-granularity | Constitution-first + PASS/PARTIAL/FAIL + verbatim quotes | C-02, C-03, C-09, C-10 |
| V-02 | lifecycle-emphasis | Dedicated labeled SPREAD-DESIGN PHASE with table + DO NOT PROCEED gate | C-11 |
| V-03 | scoring-granularity | PARTIAL AMPLIFIER table + forward-signal instruction for next round | C-12 |
| V-04 | phrasing-register | Causal-layer annotation (structural / behavioral / pedagogical) on every pattern | C-13 |
| V-05 | all four + feedback loop | Constitution-first + dedicated SPREAD-DESIGN PHASE + PARTIAL amplifier + causal-layer + PARTIAL-Causal feedback for Round 2+ axis assignment | C-11 + C-12 + C-13 + C-14 |

---

## V-01 -- Role-Sequence + Scoring-Granularity (Constitution-First with PARTIAL)

**axis:** role-sequence + scoring-granularity (R2 combination)
**hypothesis:** Leading with the dual-convergence constitution (R2-V-02 signal) combined with
PASS/PARTIAL/FAIL scoring and mandatory verbatim evidence quotes (R2-V-01 signal) will pass
all essential and recommended criteria and C-09/C-10, but will score PARTIAL on C-11
(spread-design is in the generation step, not a dedicated named phase) and FAIL C-12 and C-13
(no PARTIAL-as-amplifier instruction, no causal-layer annotation). This establishes the
round's baseline. Falsifiable: if this variation passes C-11 without a dedicated phase heading,
then C-11's pass condition is too lenient.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE -- READ THIS FIRST

This loop runs until BOTH gates are satisfied SIMULTANEOUSLY in the same round:

GATE 1 -- TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy an essential criterion. Only PASS counts.

GATE 2 -- QUEST PLATEAUED
Step 3 in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND both found zero new
excellence patterns. One zero-pattern round is not enough. Two consecutive zero-pattern
rounds are required. Both rounds must be cited by explicit name -- not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations. Every step. Every instruction.
Every output contract.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria. A round where all {N}
variations produce identical composite scores generates no excellence patterns and does not
advance plateau detection.

Causal constraint: identical composite scores -> no score spread -> no excellence patterns ->
round does not count toward the two consecutive zero-pattern rounds required for GATE 2.

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

Score every variation against every rubric criterion using PASS / PARTIAL / FAIL.

- PASS: criterion is fully satisfied. Evidence quote confirms.
- PARTIAL: criterion is partially satisfied. A required element is present but incomplete.
- FAIL: criterion is absent or contradicted.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | PARTIAL | FAIL
Quote: "[verbatim text from the variation body that supports the result, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | ... |
|-----------|--------|------|------|-----|
| C-01      | E      |      |      |     |
| C-02      | E      |      |      |     |
| C-03      | E      |      |      |     |
| C-04      | E      |      |      |     |
| C-05      | E      |      |      |     |
| C-06      | R      |      |      |     |
| C-07      | R      |      |      |     |
| C-08      | R      |      |      |     |
| C-09      | A      |      |      |     |
| C-10      | A      |      |      |     |
| C-11      | A      |      |      |     |
| C-12      | A      |      |      |     |
| C-13      | A      |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)
PARTIAL counts as 0.5 for composite purposes only. Essential criteria require PASS for
TRIAL CONVERGENCE -- PARTIAL does not satisfy an essential criterion.

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another (including PASS vs
PARTIAL, or PARTIAL vs FAIL):
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
PARTIAL is not PASS for trial convergence.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN] with [result]. ...

GATE 2 -- PLATEAU DETECTION

State what Step 3 found in the CURRENT ROUND: [pattern names] OR "no new patterns."
State what Step 3 found in the IMMEDIATELY PRECEDING ROUND by name: [patterns] OR "no new patterns."
Name both rounds explicitly (e.g., "Round 2 and Round 3").

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. PARTIAL cells count as 0.5 for ranking.
   Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score,
   status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## V-02 -- Lifecycle-Emphasis: Dedicated SPREAD-DESIGN PHASE (targeting C-11)

**axis:** lifecycle-emphasis
**hypothesis:** Elevating spread-design to a dedicated labeled phase ("SPREAD-DESIGN PHASE")
that precedes STEP 1 with its own heading, axis-assignment table, and DO NOT PROCEED gate
will cause C-11 to PASS (vs V-01's PARTIAL) because the phase is architecturally unskippable.
V-01's inline note can be glossed over under pressure; a named gate cannot.
Falsifiable: if C-11 pass rate is identical to V-01, the dedicated heading adds no protective
value over the inline instruction.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE -- READ THIS FIRST

This loop runs until BOTH gates are satisfied SIMULTANEOUSLY in the same round:

GATE 1 -- TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy an essential criterion. Only PASS counts.

GATE 2 -- QUEST PLATEAUED
Step 3 in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND both found zero new
excellence patterns. One zero-pattern round is not enough. Two consecutive zero-pattern
rounds are required. Both rounds must be cited by explicit name -- not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

SPREAD-DESIGN PHASE

Run this phase before writing any variation body. This is a mandatory procedural step --
not a note.

1. List the {N} variations you plan to write. For each, assign exactly one axis.

2. For each planned variation, state:
   a. Which axis it changes.
   b. Which rubric criterion it is most likely to affect.
   c. Your predicted composite score (numeric).

3. Confirm at least two variations target different rubric criteria.

4. If all {N} predicted composite scores are identical, STOP. Redesign before proceeding.
   Identical predicted composites mean the round will produce no score spread.
   No spread -> no excellence patterns -> round does not count toward GATE 2 plateau detection.

Complete the SPREAD-DESIGN PHASE output as a table:

| Plan # | Axis | Target Criterion | Predicted Composite |
|--------|------|-----------------|---------------------|
| 1      |      |                  |                     |
| ...    |      |                  |                     |

DO NOT proceed to STEP 1 until this table is complete and predicted composites diverge.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations. Every step. Every instruction.
Every output contract.

Round 1: change exactly one axis per variation (per SPREAD-DESIGN PHASE plan).
Round 2+: combine axes that produced signal in earlier rounds.

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

| Criterion | Weight | V-01 | V-02 | ... |
|-----------|--------|------|------|-----|
| C-01      | E      |      |      |     |
| C-02      | E      |      |      |     |
| C-03      | E      |      |      |     |
| C-04      | E      |      |      |     |
| C-05      | E      |      |      |     |
| C-06      | R      |      |      |     |
| C-07      | R      |      |      |     |
| C-08      | R      |      |      |     |
| C-09      | A      |      |      |     |
| C-10      | A      |      |      |     |
| C-11      | A      |      |      |     |
| C-12      | A      |      |      |     |
| C-13      | A      |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)

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
Diagnosis: rubric-gap | skill-gap
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
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score,
   status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## V-03 -- Scoring-Granularity: PARTIAL-as-Amplifier (targeting C-12)

**axis:** scoring-granularity
**hypothesis:** Adding explicit "PARTIAL AMPLIFIER" instructions in Step 2 -- instructing the
operator to record all PARTIAL results in a separate named table and use them as candidate
axes for the next round's spread-design -- will cause C-12 to PASS (vs V-01's FAIL) because
the mechanism is explicitly built into the scoring step, not implied. PARTIAL results become
forward signals, not just diagnostic records. Falsifiable: if C-12 pass rate is identical
to V-01, the PARTIAL-amplifier instruction adds no structural value.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE -- READ THIS FIRST

This loop runs until BOTH gates are satisfied SIMULTANEOUSLY in the same round:

GATE 1 -- TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy an essential criterion. Only PASS counts.

GATE 2 -- QUEST PLATEAUED
Step 3 in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND both found zero new
excellence patterns. One zero-pattern round is not enough. Two consecutive zero-pattern
rounds are required. Both rounds must be cited by explicit name -- not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations. Every step. Every instruction.
Every output contract.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria. A round where all {N}
variations produce identical composite scores generates no excellence patterns and does not
advance plateau detection.

Causal constraint: identical composite scores -> no score spread -> no excellence patterns ->
round does not count toward the two consecutive zero-pattern rounds required for GATE 2.

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

Score every variation against every rubric criterion using PASS / PARTIAL / FAIL.

- PASS: criterion is fully satisfied. Evidence quote confirms.
- PARTIAL: criterion is partially satisfied. A required element is present but incomplete.
- FAIL: criterion is absent or contradicted.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | PARTIAL | FAIL
Quote: "[verbatim text from the variation body that supports the result, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | ... |
|-----------|--------|------|------|-----|
| C-01      | E      |      |      |     |
| C-02      | E      |      |      |     |
| C-03      | E      |      |      |     |
| C-04      | E      |      |      |     |
| C-05      | E      |      |      |     |
| C-06      | R      |      |      |     |
| C-07      | R      |      |      |     |
| C-08      | R      |      |      |     |
| C-09      | A      |      |      |     |
| C-10      | A      |      |      |     |
| C-11      | A      |      |      |     |
| C-12      | A      |      |      |     |
| C-13      | A      |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)
PARTIAL counts as 0.5 for composite. Essential criteria require full PASS for TRIAL CONVERGENCE.

PARTIAL AMPLIFIER -- run after scoring all variations:
After recording all per-criterion results, extract any PARTIAL results into a dedicated table:

| Variation | Criterion | What's Present | What's Missing |
|-----------|-----------|----------------|----------------|
|           |           |                |                |

This table is the input to the next round's spread-design. A PARTIAL on C-NN means the
criterion's mechanism exists in seed form -- the next round's variation on that axis should
amplify the missing element to full PASS.

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation AND
the PARTIAL AMPLIFIER table is populated (or explicitly noted as empty).

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another (including PASS vs
PARTIAL, or PARTIAL vs FAIL):
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
PARTIAL is not PASS for trial convergence.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN] with [result]. ...

GATE 2 -- PLATEAU DETECTION

State what Step 3 found in the CURRENT ROUND: [pattern names] OR "no new patterns."
State what Step 3 found in the IMMEDIATELY PRECEDING ROUND by name: [patterns] OR "no new patterns."
Name both rounds explicitly (e.g., "Round 2 and Round 3").

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. PARTIAL cells count as 0.5 for ranking.
   Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score,
   status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## V-04 -- Phrasing-Register: Causal-Layer Annotation (targeting C-13)

**axis:** phrasing-register
**hypothesis:** Requiring each excellence pattern in Step 3 to carry an explicit causal-layer
label -- Layer: structural | behavioral | pedagogical -- will cause C-13 to PASS (vs V-01's
FAIL) because the label is a mandatory field in the pattern output contract, not an optional
annotation. Future authors reading the rubric will know not just that a mechanism exists,
but at which architectural layer to apply it. Falsifiable: if C-13 pass rate is identical
to V-01, the causal-layer label adds no transferable value.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE -- READ THIS FIRST

This loop runs until BOTH gates are satisfied SIMULTANEOUSLY in the same round:

GATE 1 -- TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy an essential criterion. Only PASS counts.

GATE 2 -- QUEST PLATEAUED
Step 3 in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND both found zero new
excellence patterns. One zero-pattern round is not enough. Two consecutive zero-pattern
rounds are required. Both rounds must be cited by explicit name -- not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations. Every step. Every instruction.
Every output contract.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria. A round where all {N}
variations produce identical composite scores generates no excellence patterns and does not
advance plateau detection.

Causal constraint: identical composite scores -> no score spread -> no excellence patterns ->
round does not count toward the two consecutive zero-pattern rounds required for GATE 2.

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

Score every variation against every rubric criterion using PASS / PARTIAL / FAIL.

- PASS: criterion is fully satisfied. Evidence quote confirms.
- PARTIAL: criterion is partially satisfied. A required element is present but incomplete.
- FAIL: criterion is absent or contradicted.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | PARTIAL | FAIL
Quote: "[verbatim text from the variation body that supports the result, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | ... |
|-----------|--------|------|------|-----|
| C-01      | E      |      |      |     |
| C-02      | E      |      |      |     |
| C-03      | E      |      |      |     |
| C-04      | E      |      |      |     |
| C-05      | E      |      |      |     |
| C-06      | R      |      |      |     |
| C-07      | R      |      |      |     |
| C-08      | R      |      |      |     |
| C-09      | A      |      |      |     |
| C-10      | A      |      |      |     |
| C-11      | A      |      |      |     |
| C-12      | A      |      |      |     |
| C-13      | A      |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)
PARTIAL counts as 0.5 for composite. Essential criteria require full PASS for TRIAL CONVERGENCE.

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another (including PASS vs
PARTIAL, or PARTIAL vs FAIL):
```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
Layer: structural | behavioral | pedagogical
Scope: skill-specific | transferable
```

Causal layer definitions:
- structural: the prompt architecture itself enforces the behavior (a missing section makes
  the behavior impossible)
- behavioral: the operator action sequence changes (a step is added, reordered, or gated)
- pedagogical: the prompt teaches the scorer why the behavior matters, not just that it is
  required

DO NOT proceed to Step 4 until all patterns are named with mechanism and Layer both stated.

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
PARTIAL is not PASS for trial convergence.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN] with [result]. ...

GATE 2 -- PLATEAU DETECTION

State what Step 3 found in the CURRENT ROUND: [pattern names] OR "no new patterns."
State what Step 3 found in the IMMEDIATELY PRECEDING ROUND by name: [patterns] OR "no new patterns."
Name both rounds explicitly (e.g., "Round 2 and Round 3").

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. PARTIAL cells count as 0.5 for ranking.
   Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score,
   status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## V-05 -- Full Integration: PARTIAL-Causal Feedback Loop (all four axes combined)

**axis:** role-sequence + lifecycle-emphasis + scoring-granularity + phrasing-register
**hypothesis:** Combining constitution-first placement, a dedicated SPREAD-DESIGN PHASE with
PARTIAL-Causal feedback from the prior round, PARTIAL-as-amplifier table, and causal-layer
annotation on patterns will pass C-11, C-12, and C-13 simultaneously and reveal a new
structural property: the PARTIAL-Causal Feedback Loop, where PARTIAL records and causal-layer
labels from round N are explicitly consumed by the SPREAD-DESIGN PHASE for round N+1. This
feedback loop is not captured by C-11, C-12, or C-13 individually.
Falsifiable: if no new pattern emerges beyond what C-11/C-12/C-13 already capture, V-05
adds no structural property beyond the union of its components.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE -- READ THIS FIRST

This loop runs until BOTH gates are satisfied SIMULTANEOUSLY in the same round:

GATE 1 -- TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy an essential criterion. Only PASS counts.

GATE 2 -- QUEST PLATEAUED
Step 3 in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND both found zero new
excellence patterns. One zero-pattern round is not enough. Two consecutive zero-pattern
rounds are required. Both rounds must be cited by explicit name -- not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

SPREAD-DESIGN PHASE

Run this phase before writing any variation body. This is a mandatory procedural step --
not a note inside the generation step.

ROUND 1 -- First-time spread design:
1. List {N} planned variations with one axis each.
2. Confirm at least two variations target different rubric criteria.
3. Predict each variation's composite score. If all {N} are identical, redesign before
   proceeding.

Output as a table:

| Plan # | Axis | Target Criterion | Predicted Composite |
|--------|------|-----------------|---------------------|
| 1      |      |                  |                     |
| ...    |      |                  |                     |

ROUND 2+ -- PARTIAL-Causal feedback spread design:
Before planning this round's variations, examine the immediately preceding round's output:

Step A -- PARTIAL record review:
List every PARTIAL result from the preceding round's PARTIAL AMPLIFIER table.
For each PARTIAL: which criterion? What element is present but incomplete?

Step B -- Causal-layer review:
List every causal-layer annotation from the preceding round's Step 3 patterns.
For each: what layer (structural / behavioral / pedagogical)? What design dimension does
it suggest?

Step C -- Axis assignment from signals:
Assign this round's variation axes by combining:
- Axes that produced PARTIAL passes (incomplete signal worth amplifying)
- Axes whose causal-layer is structural (prompt architecture changes, not just wording)
Do not assign axes that produced only FAIL results with no PARTIAL -- they are dead ends,
not seeds.

Output as a table with a Source column:

| Plan # | Axis | Source (PARTIAL/causal-layer citation) | Target Criterion | Predicted Composite |
|--------|------|----------------------------------------|-----------------|---------------------|
| 1      |      |                                        |                  |                     |
| ...    |      |                                        |                  |                     |

DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites
diverge.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations. Every step. Every instruction.
Every output contract.

Round 1: change exactly one axis per variation (per SPREAD-DESIGN PHASE plan).
Round 2+: combine axes from the SPREAD-DESIGN PHASE plan -- specifically axes that produced
PARTIAL passes or structural-layer patterns in the preceding round.

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

Score every variation against every rubric criterion using PASS / PARTIAL / FAIL.

- PASS: criterion is fully satisfied. Evidence quote confirms.
- PARTIAL: criterion is partially satisfied. A required element is present but incomplete.
- FAIL: criterion is absent or contradicted.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | PARTIAL | FAIL
Quote: "[verbatim text from the variation body that supports the result, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | ... |
|-----------|--------|------|------|-----|
| C-01      | E      |      |      |     |
| C-02      | E      |      |      |     |
| C-03      | E      |      |      |     |
| C-04      | E      |      |      |     |
| C-05      | E      |      |      |     |
| C-06      | R      |      |      |     |
| C-07      | R      |      |      |     |
| C-08      | R      |      |      |     |
| C-09      | A      |      |      |     |
| C-10      | A      |      |      |     |
| C-11      | A      |      |      |     |
| C-12      | A      |      |      |     |
| C-13      | A      |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)
PARTIAL counts as 0.5 for composite. Essential criteria require full PASS for TRIAL CONVERGENCE.

PARTIAL AMPLIFIER -- run after scoring all variations:
Extract any PARTIAL results into a dedicated table for the next round's SPREAD-DESIGN PHASE:

| Variation | Criterion | What's Present | What's Missing |
|-----------|-----------|----------------|----------------|
|           |           |                |                |

If the table is empty (no PARTIALs), note: "No PARTIAL amplifier signals this round."

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation AND
the PARTIAL AMPLIFIER table is populated or explicitly empty.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another (including PASS vs
PARTIAL, or PARTIAL vs FAIL):
```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
Layer: structural | behavioral | pedagogical
Scope: skill-specific | transferable
```

Causal layer definitions:
- structural: the prompt architecture itself enforces the behavior (a missing section makes
  the behavior impossible)
- behavioral: the operator action sequence changes (a step is added, reordered, or gated)
- pedagogical: the prompt teaches the scorer why the behavior matters, not just that it is
  required

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until all patterns are named with mechanism and Layer both stated.

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
PARTIAL is not PASS for trial convergence.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN] with [result]. ...

GATE 2 -- PLATEAU DETECTION

State what Step 3 found in the CURRENT ROUND: [pattern names] OR "no new patterns."
State what Step 3 found in the IMMEDIATELY PRECEDING ROUND by name: [patterns] OR "no new patterns."
Name both rounds explicitly (e.g., "Round 2 and Round 3").

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. PARTIAL cells count as 0.5 for ranking.
   Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score,
   status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## STEP 2 -- SCORE EACH VARIATION (Summary Matrix)

### Per-Criterion Evidence

#### V-01

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE {N} VARIATIONS [...] STEP 2 -- SCORE EACH VARIATION [...] STEP 3 -- IDENTIFY EXCELLENCE PATTERNS [...] STEP 4 -- PROPOSE RUBRIC CRITERIA" |
| C-02 | PASS | "For each variation, for each criterion: [...] Complete all criteria for one variation before moving to the next. After all variations are scored individually, produce the summary matrix" |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGED [...] GATE 2 -- QUEST PLATEAUED [...] State ONE of: - TRIAL CONVERGED [...] State ONE of: - QUEST PLATEAUED" |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields." |
| C-06 | PASS | "Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]" |
| C-07 | PASS | "ID: C-[NN] [...] Text: [...] Weight: [...] Category: [...] Pass condition: [...] DO NOT proceed to the convergence check until every proposed criterion has all five fields." |
| C-08 | PASS | "State what Step 3 found in the IMMEDIATELY PRECEDING ROUND by name. Name both rounds explicitly (e.g., 'Round 2 and Round 3')." |
| C-09 | PASS | "Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria." |
| C-10 | PASS | "Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for GATE 2." |
| C-11 | PARTIAL | "Active spread-design: before writing any variation body..." -- instruction is inline within STEP 1, not a dedicated labeled phase with its own heading preceding STEP 1. |
| C-12 | FAIL | absent -- no PARTIAL AMPLIFIER table or forward-signal instruction. |
| C-13 | FAIL | absent -- pattern output has Pattern name / Mechanism / Principle / Scope but no Layer field. |

#### V-02

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE [...] STEP 2 -- SCORE [...] STEP 3 -- IDENTIFY [...] STEP 4 -- PROPOSE" |
| C-02 | PASS | "For each variation, for each criterion: [Criterion / Result / Evidence] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...] State ONE of: - TRIAL CONVERGED / State ONE of: - QUEST PLATEAUED" |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule...]" |
| C-07 | PASS | "ID: C-[NN] [...] Text: [...] Weight: [...] Category: [...] Pass condition: [...]" |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 2 and Round 3')." |
| C-09 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note. [...] DO NOT proceed to STEP 1 until this table is complete and predicted composites diverge." |
| C-10 | PASS | "Identical predicted composites mean the round will produce no score spread. No spread -> no excellence patterns -> round does not count toward GATE 2 plateau detection." |
| C-11 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note. [...] DO NOT proceed to STEP 1 until this table is complete and predicted composites diverge." -- dedicated labeled heading, DO NOT PROCEED gate, precedes STEP 1. |
| C-12 | FAIL | absent -- V-02 uses PASS/FAIL scoring, so PARTIAL state is unavailable. No PARTIAL AMPLIFIER table. |
| C-13 | FAIL | absent -- no Layer field in pattern output contract. |

#### V-03

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 [...] STEP 2 [...] STEP 3 [...] STEP 4" |
| C-02 | PASS | "Score every variation against every rubric criterion using PASS / PARTIAL / FAIL. [...] For each variation, for each criterion: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...]" |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]" |
| C-07 | PASS | "ID: [...] Text: [...] Weight: [...] Category: [...] Pass condition: [...]" |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 2 and Round 3')." |
| C-09 | PASS | "Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria." |
| C-10 | PASS | "Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for GATE 2." |
| C-11 | PARTIAL | "Active spread-design: before writing any variation body..." -- same as V-01: inline instruction within STEP 1, not a dedicated labeled phase. |
| C-12 | PASS | "PARTIAL AMPLIFIER -- run after scoring all variations: [...] This table is the input to the next round's spread-design. A PARTIAL on C-NN means the criterion's mechanism exists in seed form -- the next round's variation on that axis should amplify the missing element to full PASS." |
| C-13 | FAIL | absent -- no Layer field in Step 3 pattern output contract. |

#### V-04

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 [...] STEP 2 [...] STEP 3 [...] STEP 4" |
| C-02 | PASS | "Score every variation against every rubric criterion using PASS / PARTIAL / FAIL. [...] For each variation, for each criterion: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...]" |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule...]" |
| C-07 | PASS | "ID: [...] Text: [...] Weight: [...] Category: [...] Pass condition: [...]" |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 2 and Round 3')." |
| C-09 | PASS | "Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria." |
| C-10 | PASS | "Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for GATE 2." |
| C-11 | PARTIAL | "Active spread-design: before writing any variation body..." -- inline within STEP 1, not a dedicated labeled phase. |
| C-12 | FAIL | absent -- PARTIAL scoring present but no PARTIAL AMPLIFIER table or forward-signal instruction. |
| C-13 | PASS | "Layer: structural | behavioral | pedagogical [...] DO NOT proceed to Step 4 until all patterns are named with mechanism and Layer both stated. / Causal layer definitions: - structural: [...] - behavioral: [...] - pedagogical: [...]" |

#### V-05

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE [...] STEP 2 -- SCORE [...] STEP 3 -- IDENTIFY EXCELLENCE PATTERNS [...] STEP 4 -- PROPOSE RUBRIC CRITERIA" |
| C-02 | PASS | "Score every variation against every rubric criterion using PASS / PARTIAL / FAIL. [...] For each variation, for each criterion: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...] State ONE of: - TRIAL CONVERGED [...] State ONE of: - QUEST PLATEAUED" |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]" |
| C-07 | PASS | "ID: [...] Text: [...] Weight: [...] Category: [...] Pass condition: [...] DO NOT proceed to the convergence check until every proposed criterion has all five fields." |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 2 and Round 3')." |
| C-09 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note inside the generation step. [...] ROUND 2+ -- PARTIAL-Causal feedback spread design: [...] Step C -- Axis assignment from signals: Assign this round's variation axes by combining: - Axes that produced PARTIAL passes..." |
| C-10 | PASS | "No spread -> no excellence patterns -> round does not count toward GATE 2 plateau detection. [...] If all {N} predicted composite scores are identical, STOP. Redesign before proceeding." |
| C-11 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note inside the generation step. [...] DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites diverge." |
| C-12 | PASS | "PARTIAL AMPLIFIER -- run after scoring all variations: Extract any PARTIAL results into a dedicated table for the next round's SPREAD-DESIGN PHASE: [...] If the table is empty (no PARTIALs), note: 'No PARTIAL amplifier signals this round.'" |
| C-13 | PASS | "Layer: structural | behavioral | pedagogical [...] DO NOT proceed to Step 4 until all patterns are named with mechanism and Layer both stated. / Causal layer definitions: [...]" |

### Summary Matrix

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | E | PASS | PASS | PASS | PASS | PASS |
| C-02 | E | PASS | PASS | PASS | PASS | PASS |
| C-03 | E | PASS | PASS | PASS | PASS | PASS |
| C-04 | E | PASS | PASS | PASS | PASS | PASS |
| C-05 | E | PASS | PASS | PASS | PASS | PASS |
| C-06 | R | PASS | PASS | PASS | PASS | PASS |
| C-07 | R | PASS | PASS | PASS | PASS | PASS |
| C-08 | R | PASS | PASS | PASS | PASS | PASS |
| C-09 | A | PASS | PASS | PASS | PASS | PASS |
| C-10 | A | PASS | PASS | PASS | PASS | PASS |
| C-11 | A | PARTIAL | PASS | PARTIAL | PARTIAL | PASS |
| C-12 | A | FAIL | FAIL | PASS | FAIL | PASS |
| C-13 | A | FAIL | FAIL | FAIL | PASS | PASS |
| **COMPOSITE** | | **95** | **96** | **97** | **97** | **100** |
| **RANK** | | **5** | **4** | **2** | **2** | **1** |

Composite calculations:
- V-01: (5/5 * 60) + (3/3 * 30) + (2.5/5 * 10) = 60 + 30 + 5 = 95
- V-02: (5/5 * 60) + (3/3 * 30) + (3.0/5 * 10) = 60 + 30 + 6 = 96
- V-03: (5/5 * 60) + (3/3 * 30) + (3.5/5 * 10) = 60 + 30 + 7 = 97
- V-04: (5/5 * 60) + (3/3 * 30) + (3.5/5 * 10) = 60 + 30 + 7 = 97
- V-05: (5/5 * 60) + (3/3 * 30) + (5.0/5 * 10) = 60 + 30 + 10 = 100

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

### C-11 spread: V-02 = PASS; V-01, V-03, V-04 = PARTIAL; V-05 = PASS

```
Pattern name: Phase Heading as Architectural Gate
Mechanism: V-02 and V-05 place spread-design under a dedicated labeled heading with a
DO NOT PROCEED gate before STEP 1. V-01, V-03, V-04 embed the same instruction as a
paragraph inside STEP 1. The heading creates a structural boundary; the inline paragraph
can be skipped without a gate forcing compliance.
Principle: A procedural step the operator can skip under pressure is not a gate -- it is
a suggestion. Only a dedicated labeled section with an explicit DO NOT PROCEED condition
creates an architecturally unskippable phase.
Layer: structural
Scope: transferable
```

Confirms C-11 mechanism. Not a new pattern.

### C-12 spread: V-03 = PASS; V-05 = PASS; V-01, V-02, V-04 = FAIL

```
Pattern name: PARTIAL-Forward Signal Connection
Mechanism: V-03 and V-05 provide a named PARTIAL AMPLIFIER table with explicit instructions
connecting each PARTIAL entry to the next round's spread-design. V-01 and V-04 use PARTIAL
scoring but treat results as diagnostic only. V-02 uses PASS/FAIL only.
Principle: Recording PARTIAL results is not the same as using them. The PARTIAL AMPLIFIER
table forces the operator to state what is present (seed) and what is missing (amplification
target), converting a diagnostic record into an axis assignment instruction for the next round.
Layer: behavioral
Scope: transferable
```

Confirms C-12 mechanism. Not a new pattern.

### C-13 spread: V-04 = PASS; V-05 = PASS; V-01, V-02, V-03 = FAIL

```
Pattern name: Layer as Transfer Vector
Mechanism: V-04 and V-05 include a mandatory Layer field (structural | behavioral |
pedagogical) in the pattern output contract for Step 3, with causal layer definitions.
V-01, V-02, V-03 include Mechanism and Principle but no Layer field.
Principle: A named mechanism tells you what is happening. A causal-layer label tells you
where to intervene. Without the layer, a pattern is an observation with no address.
Layer: pedagogical
Scope: transferable
```

Confirms C-13 mechanism. Not a new pattern.

### V-05 unique spread: composite 100 vs V-03/V-04 at 97 (V-05 passes C-11 + C-12 + C-13 simultaneously)

V-05's SPREAD-DESIGN PHASE for Round 2+ names two prior-round outputs as required inputs
to axis assignment: (a) the PARTIAL AMPLIFIER table from Step 2 and (b) the Layer annotations
from Step 3. This explicit cross-phase consumption creates a feedback loop that is not
captured by C-11 (which requires a dedicated spread-design phase), C-12 (which requires
PARTIAL-as-amplifier), or C-13 (which requires causal-layer annotation) individually.
Removing any one of the three breaks the feedback loop.

```
Pattern name: PARTIAL-Causal Feedback Loop
Mechanism: V-05's SPREAD-DESIGN PHASE for Round 2+ explicitly names the PARTIAL AMPLIFIER
table (Step 2 output) and the Layer annotations (Step 3 output) as required inputs to axis
assignment. V-01 through V-04 may record PARTIAL results and may annotate causal layers,
but none instructs the spread-design phase to consume those outputs by name as inputs to
axis selection.
Principle: A feedback loop across phases is only created when a downstream phase explicitly
names upstream phase outputs as required inputs. Recording PARTIAL results in Step 2 and
labeling causal layers in Step 3 produces no feedback if the SPREAD-DESIGN PHASE for the
next round does not name them as inputs. The connection must be explicit and bidirectional.
Layer: structural
Scope: transferable
```

NEW pattern. C-11 + C-12 + C-13 exist in rubric v2 but none captures the cross-phase
consumption of PARTIAL records and causal-layer labels as named inputs to the spread-design
phase.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

```
ID:             C-14
Text:           The spread-design phase for rounds after Round 1 explicitly names the PARTIAL
                AMPLIFIER table and the causal-layer annotations from the preceding round as
                required inputs to axis assignment, creating a feedback loop rather than
                independent per-round axis selection.
Weight:         aspirational
Category:       structure
Pass condition: The SPREAD-DESIGN PHASE (or equivalent) for rounds > 1 contains explicit
                instructions referencing both (a) PARTIAL results from the preceding round
                and (b) causal-layer labels from the preceding round as named inputs to axis
                assignment; prompts that instruct round-2+ axis selection without naming
                these prior-round outputs as inputs do not pass.
```

All five fields present.

---

## CONVERGENCE CHECK

### GATE 1 -- TRIAL CONVERGENCE

| Essential | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |

TRIAL CONVERGED: all 5 variations pass all essential criteria this round.

### GATE 2 -- PLATEAU DETECTION

Round 3 found: PARTIAL-Causal Feedback Loop (proposed as C-14). One new pattern.

Round 2 found: Spread-Design as Dedicated Phase (C-11), PARTIAL State as Evidence Amplifier
(C-12), Causal Annotation as Teaching Layer (C-13). Three new patterns.

QUEST NOT PLATEAUED: Round 3 found the PARTIAL-Causal Feedback Loop pattern. Two consecutive
zero-pattern rounds not yet achieved.

---

Dual convergence not reached. TRIAL CONVERGED but QUEST NOT PLATEAUED.

Next round: R4. Rubric advances to v3 (adding C-14). V-05 is the leading variation at 100
composite. R4 should score against rubric v3 (C-01..C-14, aspirational pool now 6 criteria).
For R4 to contribute to plateau detection, all variations must pass essentials AND Step 3
must find zero new patterns. If R4 also finds zero new patterns, R4+R5 would satisfy the
plateau gate (both rounds named as producing no new patterns).

**Status:** TRIAL CONVERGED (R3). QUEST tracking: R1 found 2 patterns, R2 found 3 patterns,
R3 found 1 pattern. First zero-pattern round not yet reached.
