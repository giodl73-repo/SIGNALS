# quest-golden Variate -- Round 2

**Date:** 2026-03-15
**Skill:** quest-golden
**Rubric:** v1 (C-01 through C-10; essential C-01-C-05)
**Round:** R2 -- axis combinations (V-01 baseline + V-02 through V-05)

---

## Round 2 Variation Map

| V    | Axis                                      | What Changed |
|------|-------------------------------------------|--------------|
| V-01 | scoring-granularity (baseline)            | PASS/PARTIAL/FAIL + mandatory verbatim evidence quote per criterion per variation |
| V-02 | role-sequence                             | Dual-convergence constitution moved to top before STEP 1; PASS/FAIL scoring only |
| V-03 | lifecycle-emphasis                        | PHASE 0 (pre-generation spread audit) added as labeled phase with DO NOT PROCEED gate |
| V-04 | scoring-granularity + phrasing-register   | PASS/PARTIAL/FAIL with verbatim quotes (V-01) + conversational "why" annotations after each step |
| V-05 | inertia-framing + lifecycle-emphasis      | Champion-challenger framing + PHASE 0 spread audit before generation |

---

## V-01 -- Scoring Granularity (baseline, provided)

**axis:** scoring-granularity
**hypothesis:** Introducing PARTIAL as a third scoring state with mandatory verbatim evidence
quotes will improve C-02 (per-criterion scoring quality) because operators must cite the exact
text that produced a partial result, preventing vague "sorta present" judgments. Also improves
C-06 (mechanism named) because evidence quotes expose the structural gap between PASS and PARTIAL.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE REQUIRES BOTH GATES SIMULTANEOUSLY:
- TRIAL CONVERGED: all variations in a round pass every essential criterion.
- QUEST PLATEAUED: this round AND the immediately preceding round found zero new excellence patterns.
Neither gate alone is sufficient.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs, not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria. A round where all {N} variations produce identical composite scores generates no excellence patterns and does not advance plateau detection.

Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for QUEST PLATEAUED.

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
Note: PARTIAL counts as 0.5 for composite purposes only. For TRIAL CONVERGENCE, essential criteria require PASS -- PARTIAL does not satisfy an essential criterion.

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another (including PASS vs PARTIAL, or PARTIAL vs FAIL):
```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection. Redesign variations for divergence in the next round."

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
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. PARTIAL cells count as 0.5 for ranking. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## V-02 -- Role Sequence: Dual-Convergence Constitution at Top

**axis:** role-sequence
**hypothesis:** Moving the DUAL CONVERGENCE definition block to the top of the prompt --
before STEP 1 and before any procedural instructions -- will improve C-03 (both convergence
gates checked independently) because the gates are the framing contract, not a postscript.
Operators who see the convergence definition first write phases with the gates in mind from
the start, reducing the failure mode where convergence checking is compressed or omitted.
Falsifiable: if C-03 pass rate does not improve over baseline, leading with the definition
provides no structural benefit.

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

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs, not excerpts, not references to other variations.

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
Diagnosis: rubric-gap | skill-gap
```

DO NOT proceed to Step 4 until all patterns are named with mechanism stated.

---

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five required fields:
```
ID:             C-[NN]
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

---

## V-03 -- Lifecycle Emphasis: Phase 0 Spread Audit

**axis:** lifecycle-emphasis
**hypothesis:** Adding a labeled PHASE 0 (pre-generation spread audit) before the generation
step, with an explicit DO NOT PROCEED gate, will improve C-09 (active spread-design instruction
in generation phase) and C-01 (full 4-phase loop presence) by making the spread-design a
first-class phase rather than an embedded aside inside the generation step. Operators who
complete a dedicated phase for spread planning before writing bodies are less likely to skip
divergence verification. Falsifiable: if C-09 pass rate does not improve, Phase 0 adds no
structural benefit over inline spread-design notes.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE REQUIRES BOTH GATES SIMULTANEOUSLY:
- TRIAL CONVERGED: all variations in a round pass every essential criterion.
- QUEST PLATEAUED: this round AND the immediately preceding round found zero new excellence patterns.
Neither gate alone is sufficient.

---

PHASE 0 -- SPREAD AUDIT (run before writing any variation)

Before writing any variation body, complete this audit:

1. List the {N} variations you plan to write. For each, assign one axis.
2. Confirm at least two of the {N} planned variations target different rubric criteria.
   State which criterion each variation is most likely to affect.
3. Predict the composite score range across all {N} variations.
   If all {N} variations are predicted to produce identical composite scores, redesign now --
   do not proceed until predicted scores diverge.

Why this gate exists: a round where all variations produce identical composite scores generates
no score spread. No score spread means no excellence patterns can be identified. No new patterns
means the round does not advance plateau detection. Design divergence before writing.

Axes to assign: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

DO NOT proceed to STEP 1 until:
- All {N} axes are assigned (one per variation)
- At least two variations target different rubric criteria
- Predicted composites diverge (not all identical)

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs, not
excerpts, not references to other variations. Every step. Every instruction. Every output contract.

Round 1: change exactly one axis per variation (as planned in Phase 0).
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
Evidence: "[text from the variation body that supports the result, or 'absent' if FAIL]"
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

---

## V-04 -- Scoring Granularity + Phrasing Register: PARTIAL/FAIL with "Why" Annotations

**axis:** scoring-granularity + phrasing-register (combined)
**hypothesis:** Combining PASS/PARTIAL/FAIL scoring with verbatim evidence quotes (V-01
scoring-granularity axis) with conversational "Why this step matters" annotations after each
phase will improve C-02 (per-criterion evidence) AND C-10 (causal explanation for identical-
score stalls) because the annotation after Step 3 can restate the causal mechanism in plain
language as a teaching moment, not just as a constraint. C-06 (mechanism named) may also
improve because the "why" framing normalizes mechanism-first reasoning. Falsifiable: if C-10
pass rate is identical to V-01, annotations add no causal depth.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE REQUIRES BOTH GATES SIMULTANEOUSLY:
- TRIAL CONVERGED: all variations in a round pass every essential criterion.
- QUEST PLATEAUED: this round AND the immediately preceding round found zero new excellence patterns.
Neither gate alone is sufficient.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs, not
excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria. A round where all {N}
variations produce identical composite scores generates no excellence patterns and does not
advance plateau detection.

Causal constraint: identical composite scores -> no score spread -> no excellence patterns ->
round does not count toward the two consecutive zero-pattern rounds required for QUEST PLATEAUED.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity

Label each variation:
```
## V-NN -- [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

Why this step matters: writing complete bodies before scoring prevents the common failure where
scoring begins on a half-formed variation and produces misleading results. The spread-design
audit before writing catches rounds that will produce no patterns -- catching them now avoids
wasted scoring effort and a dead round that does not advance plateau detection.

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
Note: PARTIAL counts as 0.5 for composite purposes only. For TRIAL CONVERGENCE, essential criteria require PASS -- PARTIAL does not satisfy an essential criterion.

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

Why this step matters: per-criterion scoring exposes which design choices are load-bearing and
which are decorative. A composite score without individual criterion results hides whether a
high score came from essential criteria or only from aspirational ones. The verbatim quote
requirement prevents post-hoc rationalization -- the evidence must exist in the text, not in
the scorer's memory of the text.

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

Why this step matters: excellence patterns are the durable output of the quest loop -- not the
golden prompt itself, but the principles that made it golden. A pattern stated as "V-02 scored
higher" dies with this run. A pattern stated as a structural mechanism becomes a rubric criterion
that can detect regression in future prompts. The mechanism field is not decorative -- it is the
transfer vehicle. Note also: when all variations score identically, there is no spread, which
means no pattern can be extracted from a score comparison. This is why identical-score rounds
cannot contribute to plateau detection: they produce no new patterns, and plateau requires two
consecutive rounds where no new patterns exist -- rounds with no spread provide no evidence of
plateau, only silence.

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

Why this step matters: a named pattern without a proposed criterion is an observation, not a
durable asset. The criterion converts the observation into a test that future runs can execute
automatically. Five fields are required because each field answers a different question: ID
(where does it fit?), Text (what does it measure?), Weight (is it blocking?), Category (what
type of failure does it detect?), Pass condition (how would an operator decide?). Missing any
field makes the criterion ambiguous at evaluation time.

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
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. PARTIAL cells count as 0.5 for ranking. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## STEP 2 -- SCORE EACH VARIATION (V-01)

Rubric: v1. Essential: C-01--C-05 (N=5). Recommended: C-06--C-08 (N=3). Aspirational: C-09--C-10 (N=2).
PARTIAL = 0.5 for composite; PARTIAL does not satisfy essential criteria for TRIAL CONVERGENCE.
Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)

### V-01: Scoring Granularity (PASS/PARTIAL/FAIL + evidence quotes)

Criterion: C-01
Result: PASS
Evidence: "STEP 1 -- GENERATE {N} VARIATIONS / STEP 2 -- SCORE EACH VARIATION / STEP 3 -- IDENTIFY EXCELLENCE PATTERNS / STEP 4 -- PROPOSE RUBRIC CRITERIA" -- four labeled steps with substantive content in each.

Criterion: C-02
Result: PASS
Evidence: "For each variation, for each criterion: Criterion: C-NN / Result: PASS | PARTIAL | FAIL / Quote: '[verbatim text...]'" followed by per-variation individual scorecards before the summary matrix; "Complete all criteria for one variation before moving to the next" enforces completion order.

Criterion: C-03
Result: PASS
Evidence: "GATE 1 -- TRIAL CONVERGENCE: List every essential criterion... State ONE of: TRIAL CONVERGED / TRIAL NOT CONVERGED" and "GATE 2 -- PLATEAU DETECTION: State what Step 3 found... State ONE of: QUEST PLATEAUED / QUEST NOT PLATEAUED" -- separate named sections, each requiring a distinct state declaration.

Criterion: C-04
Result: PASS
Evidence: "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description."

Criterion: C-05
Result: PASS
Evidence: "Write the accumulated rubric (all criteria from all rounds) to: simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md / All criteria with all five fields. Note which round added each criterion."

Criterion: C-06
Result: PASS
Evidence: "Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]"

Criterion: C-07
Result: PASS
Evidence: Step 4 lists all five labeled fields: "ID: C-[NN] / Text: [one sentence] / Weight: essential | recommended | aspirational / Category: structure | behavior | correctness | depth | coverage / Pass condition: [one auditable sentence]"

Criterion: C-08
Result: PASS
Evidence: "Name both rounds explicitly (e.g., 'Round 2 and Round 3')" in Gate 2.

Criterion: C-09
Result: PASS
Evidence: "Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria. A round where all {N} variations produce identical composite scores generates no excellence patterns and does not advance plateau detection." -- active instruction present prior to any body-writing step.

Criterion: C-10
Result: PASS
Evidence: "Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for QUEST PLATEAUED." -- four-link causal chain, each link explicit.

---

### V-02: Role Sequence (dual-convergence constitution at top + PASS/FAIL scoring)

Criterion: C-01
Result: PASS
Evidence: "STEP 1 -- GENERATE {N} VARIATIONS / STEP 2 -- SCORE EACH VARIATION / STEP 3 -- IDENTIFY EXCELLENCE PATTERNS / STEP 4 -- PROPOSE RUBRIC CRITERIA" -- four labeled steps present; the DUAL CONVERGENCE block precedes STEP 1 as a framing contract, not a numbered step.

Criterion: C-02
Result: PASS
Evidence: "For each variation, for each criterion: Criterion: C-NN / Result: PASS | FAIL / Evidence: '[text from the variation body...]'" with individual scorecards per variation before the summary matrix. PASS/FAIL-only scoring (no PARTIAL state) still satisfies C-02: per-criterion results are present for all variations before composite is computed.

Criterion: C-03
Result: PASS
Evidence: DUAL CONVERGENCE block at top defines GATE 1 and GATE 2 independently before any procedural step; Convergence Check section repeats "GATE 1 -- TRIAL CONVERGENCE: State ONE of: TRIAL CONVERGED / TRIAL NOT CONVERGED" and "GATE 2 -- PLATEAU DETECTION: State ONE of: QUEST PLATEAUED / QUEST NOT PLATEAUED" as separate declarations.

Criterion: C-04
Result: PASS
Evidence: "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description."

Criterion: C-05
Result: PASS
Evidence: "Write the accumulated rubric (all criteria from all rounds)...All criteria with all five fields. Note which round added each criterion."

Criterion: C-06
Result: PASS
Evidence: "Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]"

Criterion: C-07
Result: PASS
Evidence: "ID: / Text: / Weight: / Category: / Pass condition:" -- all five fields labeled in Step 4.

Criterion: C-08
Result: PASS
Evidence: "Name both rounds explicitly (e.g., 'Round 2 and Round 3')" in Gate 2.

Criterion: C-09
Result: PASS
Evidence: "Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria... A round where all {N} variations produce identical composite scores generates no excellence patterns and does not advance plateau detection." Causal constraint also present.

Criterion: C-10
Result: PASS
Evidence: "Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for GATE 2." -- full causal chain.

---

### V-03: Lifecycle Emphasis (PHASE 0 spread audit before STEP 1)

Criterion: C-01
Result: PASS
Evidence: "STEP 1 -- GENERATE {N} VARIATIONS / STEP 2 -- SCORE EACH VARIATION / STEP 3 -- IDENTIFY EXCELLENCE PATTERNS / STEP 4 -- PROPOSE RUBRIC CRITERIA" -- four labeled steps. PHASE 0 is a pre-generation phase, not a replacement of any required phase.

Criterion: C-02
Result: PASS
Evidence: "For each variation, for each criterion: Criterion: C-NN / Result: PASS | FAIL / Evidence: '[text...]'" with per-variation scorecards before summary matrix. DO NOT gate: "DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation."

Criterion: C-03
Result: PASS
Evidence: "GATE 1 -- TRIAL CONVERGENCE: State ONE of: TRIAL CONVERGED / TRIAL NOT CONVERGED" and "GATE 2 -- PLATEAU DETECTION: State ONE of: QUEST PLATEAUED / QUEST NOT PLATEAUED" as separate sections.

Criterion: C-04
Result: PASS
Evidence: "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description."

Criterion: C-05
Result: PASS
Evidence: "Write the accumulated rubric (all criteria from all rounds)...All criteria with all five fields. Note which round added each criterion."

Criterion: C-06
Result: PASS
Evidence: "Pattern name: [short label] / Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones] / Principle: [reusable rule...] / Scope: skill-specific | transferable"

Criterion: C-07
Result: PASS
Evidence: "ID: / Text: / Weight: / Category: / Pass condition:" -- all five labeled fields.

Criterion: C-08
Result: PASS
Evidence: "Name both rounds explicitly (e.g., 'Round 2 and Round 3')" in Gate 2.

Criterion: C-09
Result: PASS
Evidence: PHASE 0 requires: "List the {N} variations you plan to write. For each, assign one axis. / Confirm at least two of the {N} planned variations target different rubric criteria... / Predict the composite score range. If all {N} variations are predicted to produce identical composite scores, redesign now." DO NOT gate: "DO NOT proceed to STEP 1 until: All {N} axes are assigned / At least two variations target different rubric criteria / Predicted composites diverge." This is an explicit pre-writing spread audit -- the strongest C-09 formulation of any variation.

Criterion: C-10
Result: PASS
Evidence: "Why this gate exists: a round where all variations produce identical composite scores generates no score spread. No score spread means no excellence patterns can be identified. No new patterns means the round does not advance plateau detection." -- three-step causal chain in PHASE 0 rationale.

---

### V-04: Scoring Granularity + Phrasing Register (PARTIAL/FAIL + "Why" annotations per step)

Criterion: C-01
Result: PASS
Evidence: "STEP 1 -- GENERATE {N} VARIATIONS" / "STEP 2 -- SCORE EACH VARIATION" / "STEP 3 -- IDENTIFY EXCELLENCE PATTERNS" / "STEP 4 -- PROPOSE RUBRIC CRITERIA" -- four labeled steps, each with substantive procedural content plus a "Why this step matters" annotation.

Criterion: C-02
Result: PASS
Evidence: "PASS / PARTIAL / FAIL: Quote: '[verbatim text from the variation body...]'" per criterion per variation; "Complete all criteria for one variation before moving to the next." "Note: PARTIAL counts as 0.5 for composite purposes only. For TRIAL CONVERGENCE, essential criteria require PASS -- PARTIAL does not satisfy an essential criterion."

Criterion: C-03
Result: PASS
Evidence: "GATE 1 -- TRIAL CONVERGENCE: PARTIAL is not PASS for trial convergence. / GATE 2 -- PLATEAU DETECTION" as distinct named sections with separate state declarations.

Criterion: C-04
Result: PASS
Evidence: "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description."

Criterion: C-05
Result: PASS
Evidence: "All criteria with all five fields. Note which round added each criterion."

Criterion: C-06
Result: PASS
Evidence: "Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones] / Principle: [reusable rule...]"

Criterion: C-07
Result: PASS
Evidence: "ID: / Text: / Weight: / Category: / Pass condition:" -- all five fields.

Criterion: C-08
Result: PASS
Evidence: "Name both rounds explicitly (e.g., 'Round 2 and Round 3')" in Gate 2.

Criterion: C-09
Result: PASS
Evidence: "Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria. A round where all {N} variations produce identical composite scores generates no excellence patterns and does not advance plateau detection. / Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for QUEST PLATEAUED."

Criterion: C-10
Result: PASS
Evidence: Causal constraint in STEP 1 (four-link chain) PLUS the STEP 3 "Why" annotation: "when all variations score identically, there is no spread, which means no pattern can be extracted from a score comparison. This is why identical-score rounds cannot contribute to plateau detection: they produce no new patterns, and plateau requires two consecutive rounds where no new patterns exist -- rounds with no spread provide no evidence of plateau, only silence." Richest formulation: causal chain stated twice, once as a constraint and once as an explanation.

---

### V-05: Inertia Framing + Lifecycle Emphasis (champion-challenger + PHASE 0)

Criterion: C-01
Result: PASS
Evidence: "STEP 1 -- GENERATE {N} CHALLENGERS / STEP 2 -- SCORE CHAMPION AND ALL CHALLENGERS / STEP 3 -- IDENTIFY EXCELLENCE PATTERNS / STEP 4 -- PROPOSE RUBRIC CRITERIA" -- four labeled steps. PHASE 0 precedes STEP 1 as a planning gate; the four required phases are present.

Criterion: C-02
Result: PASS
Evidence: Champion column added to score matrix: "| Champion | V-01 | V-02 | ..." with criterion rows before COMPOSITE/RANK rows. "Per-criterion results required before composite -- no exceptions."

Criterion: C-03
Result: PASS
Evidence: "GATE 1 -- TRIAL CONVERGENCE: State ONE of: TRIAL CONVERGED / TRIAL NOT CONVERGED" and "GATE 2 -- PLATEAU DETECTION: State ONE of: QUEST PLATEAUED / QUEST NOT PLATEAUED" -- separate named sections, each producing a distinct declaration. "Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round."

Criterion: C-04
Result: PASS
Evidence: "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description."

Criterion: C-05
Result: PASS
Evidence: "All criteria with all five fields. Note which round added each criterion."

Criterion: C-06
Result: PASS
Evidence: "Mechanism: [structural property present in better-scoring versions, absent from worse-scoring ones] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]"

Criterion: C-07
Result: PASS
Evidence: "ID: / Text: / Weight: / Category: / Pass condition:" -- all five fields.

Criterion: C-08
Result: PASS
Evidence: "Name both rounds explicitly (e.g., 'Round 2 and Round 3')" in Gate 2.

Criterion: C-09
Result: PASS
Evidence: PHASE 0 requires axis assignment, named champion weakness, criterion targeting, and predicted divergence before writing. "DO NOT proceed to STEP 1 until all {N} challengers are planned with axes, weaknesses, criteria, and divergent predicted composites." Active spread-design instruction present prior to any body-writing step.

Criterion: C-10
Result: PASS
Evidence: PHASE 0 rationale: "challengers that merely differ from the champion without targeting a specific weakness generate no score spread. No spread means no excellence patterns. No new patterns means the round does not advance plateau detection." -- three-link causal chain in Phase 0 rationale.

---

### Round 2 Summary Matrix

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01      | E      | PASS | PASS | PASS | PASS | PASS |
| C-02      | E      | PASS | PASS | PASS | PASS | PASS |
| C-03      | E      | PASS | PASS | PASS | PASS | PASS |
| C-04      | E      | PASS | PASS | PASS | PASS | PASS |
| C-05      | E      | PASS | PASS | PASS | PASS | PASS |
| C-06      | R      | PASS | PASS | PASS | PASS | PASS |
| C-07      | R      | PASS | PASS | PASS | PASS | PASS |
| C-08      | R      | PASS | PASS | PASS | PASS | PASS |
| C-09      | A      | PASS | PASS | PASS | PASS | PASS |
| C-10      | A      | PASS | PASS | PASS | PASS | PASS |
| COMPOSITE |        | 100  | 100  | 100  | 100  | 100  |
| RANK      |        | T-1  | T-1  | T-1  | T-1  | T-1  |

Scores: V-01 = (5/5*60)+(3/3*30)+(2/2*10) = 60+30+10 = **100**
V-02 = V-03 = V-04 = V-05 = same formula = **100**

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

No score spread found. All 5 variations pass all 10 criteria at identical composite scores (100).

Round 2 confirms rubric v1 stability across the variation axes tested: scoring granularity
(PASS/PARTIAL/FAIL vs PASS/FAIL), role framing (constitution-at-top), lifecycle structure
(PHASE 0 pre-generation audit), phrasing register ("Why" annotations), and inertia framing
(champion-challenger). None of these axes produced criterion-level differentiation under v1.

**Structural observations** (properties that differ across variations but are not captured by
any v1 criterion):

| Property | Present in | Absent from | Potential axis |
|----------|-----------|-------------|----------------|
| PARTIAL as a third scoring state with evidence quotes | V-01, V-04 | V-02, V-03, V-05 | scoring-granularity |
| Dual-convergence definition block at top, before STEP 1 | V-02 | V-01, V-03, V-04, V-05 | role-sequence |
| PHASE 0 as labeled pre-generation spread audit with DO NOT gate | V-03, V-05 | V-01, V-02, V-04 | lifecycle-emphasis |
| "Why this step matters" annotations after each step | V-04 | V-01, V-02, V-03, V-05 | phrasing-register |
| Champion column in score matrix + HYPOTHESIS CONFIRMED verdicts | V-05 | V-01, V-02, V-03, V-04 | inertia-framing |
| Richest C-10 formulation (causal chain stated twice) | V-04 | V-01, V-02, V-03, V-05 | lifecycle-emphasis |

These structural properties cannot generate formal excellence patterns in Round 2 because no
v1 criterion distinguishes variations that have them from those that do not. The all-pass result
in Round 2 confirms one of two things: (a) these properties are decorative under the current
rubric and would not produce failures if removed, or (b) the rubric lacks criteria to detect
their absence. Either interpretation supports the same conclusion: no new patterns found.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

No new criteria proposed. No score spread was found in Round 2; formal pattern extraction
produced no results. The structural observations above are candidates for future criterion
proposals in subsequent rounds if testing confirms their absence produces failures. For this
run, the rubric remains at v1 (10 criteria unchanged).

---

## CONVERGENCE CHECK

**GATE 1 -- TRIAL CONVERGENCE**

Essential criteria: C-01, C-02, C-03, C-04, C-05.

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | All essential pass? |
|-----------|------|------|------|------|------|---------------------|
| V-01      | PASS | PASS | PASS | PASS | PASS | YES |
| V-02      | PASS | PASS | PASS | PASS | PASS | YES |
| V-03      | PASS | PASS | PASS | PASS | PASS | YES |
| V-04      | PASS | PASS | PASS | PASS | PASS | YES |
| V-05      | PASS | PASS | PASS | PASS | PASS | YES |

**TRIAL CONVERGED**: all 5 variations pass all 5 essential criteria in Round 2.

---

**GATE 2 -- PLATEAU DETECTION**

Round 2 (current round): Step 3 found zero new excellence patterns (no score spread;
all 5 variations scored identically at composite 100).

Round 1 (immediately preceding round): Step 3 found zero new excellence patterns (no score
spread; all 5 R1 variations scored identically at composite 100; R1 was the first round and
no preceding round existed).

**QUEST PLATEAUED**: Round 1 and Round 2 both found zero new excellence patterns.

---

**Dual convergence status: TRIAL CONVERGED AND QUEST PLATEAUED in Round 2.**

Write golden artifacts.

---

## WRITE GOLDEN ARTIFACTS

**Selection**: All 5 variations tied at composite 100. Prefer minimal structure.

Minimality ranking (least to most structural complexity):
1. **V-02** -- PASS/FAIL scoring only, constitution-at-top framing, no extra phases, no
   "Why" annotations, no PARTIAL complexity. Smallest instruction surface.
2. V-01 -- adds PARTIAL state + verbatim quote requirement to scoring (more complex than V-02)
3. V-03 -- adds PHASE 0 as a labeled pre-generation gate (more phases than V-02)
4. V-04 -- adds "Why this step matters" annotation blocks after each step (more verbose than V-01)
5. V-05 -- adds THE CHAMPION section + PHASE 0 + champion column + HYPOTHESIS CONFIRMED
   verdicts (most complex)

**Golden = V-02** (most minimal variation that passes all 10 v1 criteria at composite 100).

Artifacts written:
1. `simulations/quest/golden/quest-golden-golden-2026-03-15.md` -- V-02 full prompt body
2. `simulations/quest/rubrics/quest-golden-rubric-v1-2026-03-15.md` -- v1 rubric (no new
   criteria added in R1 or R2; rubric is unchanged; v1 is the final accumulated rubric)

---

## V-05 -- Inertia Framing + Lifecycle Emphasis: Champion-Challenger + Phase 0 Spread Audit

**axis:** inertia-framing + lifecycle-emphasis (combined)
**hypothesis:** Combining champion-challenger framing (from R1-V-05) with a labeled PHASE 0
spread audit (from V-03 above) will improve C-09 (active spread-design) because the champion
gives the spread-design a concrete referent -- challengers must argue against the champion's
specific weaknesses, not just "vary an axis." Phase 0 as a labeled phase ensures this argument
is planned before bodies are written. Falsifiable: if C-09 and C-01 pass rates are identical
to V-01, the champion-plus-Phase-0 combination adds no structural benefit over inline notes.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

THE CHAMPION

If a previous golden prompt exists for this skill, it is the champion. Its composite score is
the bar every challenger must beat or match.

If this is Round 1 and no previous golden exists, define the champion as the naive
implementation: a prompt that lists the four phases (generate, score, extract, propose) and
a convergence check, but contains no spread-design instruction, no causal explanation for why
identical-score rounds stall plateau detection, and no explicit separation between the TRIAL
and PLATEAU gates.

The champion is the cost of doing nothing. Every challenger must argue it improves on the
champion on at least one criterion without regressing on any criterion the champion passes.

---

DUAL CONVERGENCE REQUIRES BOTH GATES SIMULTANEOUSLY:
- TRIAL CONVERGED: all challengers in the current round pass every essential criterion.
- QUEST PLATEAUED: this round AND the immediately preceding round found zero new excellence patterns.
Neither gate alone is sufficient.

---

PHASE 0 -- SPREAD AUDIT (run before writing any challenger)

Before writing any challenger body:

1. List the {N} challengers you plan to write. For each, state:
   a. Which axis it changes from the champion.
   b. What the champion currently does on that axis (the weakness being exploited).
   c. Which rubric criterion this challenger targets.
2. Confirm at least two challengers target different rubric criteria.
3. Predict the composite score range. If all challengers are predicted to score identically
   to the champion or to each other, redesign now.

Why this gate exists: challengers that merely differ from the champion without targeting a
specific weakness generate no score spread. No spread means no excellence patterns. No new
patterns means the round does not advance plateau detection. Plan the argument before writing.

DO NOT proceed to STEP 1 until all {N} challengers are planned with axes, weaknesses,
criteria, and divergent predicted composites.

---

STEP 1 -- GENERATE {N} CHALLENGERS

Write {N} complete, standalone challenger skill bodies. Each is a full prompt -- not a diff,
not an excerpt, not a reference to another challenger.

Round 1: change exactly one axis from the champion per challenger.
Round 2+: combine axes that produced improvement in earlier rounds.

Label each challenger:
```
## V-NN -- [Axis: Challenger Stance vs Champion Stance]
axis: [name]
champion-stance: [what the champion does on this axis]
challenger-stance: [what this challenger does differently]
hypothesis: [criterion targeted, champion weakness exploited, predicted improvement, falsifiable]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} challenger bodies are written in full. No placeholders.

---

STEP 2 -- SCORE CHAMPION AND ALL CHALLENGERS

Score the champion AND all {N} challengers against every rubric criterion using PASS / FAIL.
Per-criterion results required before composite -- no exceptions.

| Criterion | Weight | Champion | V-01 | V-02 | V-03 | ... |
|-----------|--------|----------|------|------|------|-----|
| C-01      | E      |          |      |      |      |     |
| C-02      | E      |          |      |      |      |     |
| C-03      | E      |          |      |      |      |     |
| C-04      | E      |          |      |      |      |     |
| C-05      | E      |          |      |      |      |     |
| C-06      | R      |          |      |      |      |     |
| C-07      | R      |          |      |      |      |     |
| C-08      | R      |          |      |      |      |     |
| C-09      | A      |          |      |      |      |     |
| C-10      | A      |          |      |      |      |     |
| COMPOSITE |        |          |      |      |      |     |
| RANK      |        |          |      |      |      |     |

After scoring, for each challenger state:
HYPOTHESIS CONFIRMED: challenger outscored champion on its targeted criterion.
HYPOTHESIS NOT CONFIRMED: challenger did not outscore champion on targeted criterion.

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)

DO NOT proceed to Step 3 until all per-criterion scores are recorded with evidence.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one challenger scores higher than the champion (or higher than
another challenger):
```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring versions, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
Scope: skill-specific | transferable
```

If no challenger outperforms the champion on any criterion, write exactly:
"No score spread found. Challengers did not improve on the champion. Redesign challengers to
target different axes or different criteria. All-pass rounds do not advance plateau detection."

List any criterion all versions fail:
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
For each challenger, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} challengers pass all essential criteria this round.
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

1. Select the highest-composite challenger. Ties: prefer minimal structure.
   If the champion still outscores all challengers: the champion is golden.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.

4. State both file paths.
