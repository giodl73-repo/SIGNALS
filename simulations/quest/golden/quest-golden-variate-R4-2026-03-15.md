# quest-golden Variate -- Round 4

**Date:** 2026-03-15
**Skill:** quest-golden
**Rubric:** v3 (C-01 through C-16; essential C-01..C-05; recommended C-06..C-08; aspirational C-09..C-16)
**Round:** R4 -- combination pass (R3 signals applied: C-14 gate, C-15 trajectory table, C-16 provenance)

---

## SPREAD-DESIGN PHASE

Rubric state entering R4: v3, C-01..C-16. Aspirational pool: 8 criteria (C-09..C-16).
Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)

R3 signals that became v3 additions:
- Phase bleeding: V-01/V-03/V-04 PARTIAL on C-11 -- labeled heading present but no declarative
  phase-end gate -> C-14 (phase-end gate as operator checkpoint)
- PARTIAL as table artifact: V-03 passes C-12 with prose; V-05 with PARTIAL AMPLIFIER table ->
  C-15 (PARTIAL trajectory table with first/repeated occurrence distinction)
- Excellence pattern provenance: no variation carried V-XX/R-N citation -> C-16

R3 leading variation: V-05 (composite 100 on rubric v2). V-05 had: dedicated SPREAD-DESIGN PHASE
with "DO NOT proceed to STEP 1 until..." gate + PARTIAL AMPLIFIER table (Variation/Criterion/
What's Present/What's Missing) + Layer annotation on patterns.

Against rubric v3, V-05 R3 would score:
- C-14: FAIL (ends phase with prohibitive gate, not declarative "COMPLETE" marker)
- C-15: PARTIAL (PARTIAL AMPLIFIER table present but lacks Round and Occurrence-type columns)
- C-16: FAIL (no provenance citation on patterns)

Axis assignment for R4 (ROUND 2+ protocol -- axes derived from R3 PARTIAL/FAIL signals):

Step A -- PARTIAL record from R3:
- V-05 R3, C-14: PARTIAL -- labeled heading present, declarative exit gate absent
- V-05 R3, C-15: PARTIAL -- PARTIAL table present, first/repeated distinction absent
(Note: C-16 was FAIL across all R3 variations -- treated as seed for single-axis probe)

Step B -- Causal-layer review from R3:
- Phase bleeding pattern (Layer: structural) -- prompt architecture must enforce phase exit,
  not just phase entry
- PARTIAL-as-table-artifact pattern (Layer: behavioral) -- table structure changes operator
  action at evidence-population time
- Provenance pattern (Layer: correctness) -- citation field in pattern contract

Step C -- Axis assignment:

| Plan | Axis | Source | Target Criterion | Predicted Composite |
|------|------|--------|-----------------|---------------------|
| V-01 | phase-end gate (declarative COMPLETE marker) | C-14 PARTIAL R3; structural layer | C-14 | 98.1 |
| V-02 | trajectory table (Round/Axis/Occurrence/Action columns) | C-15 PARTIAL R3; behavioral layer | C-15 | 97.5 |
| V-03 | pattern provenance (V-XX, R-N citation per pattern) | C-16 FAIL all R3; correctness layer | C-16 | 98.1 |
| V-04 | gate + provenance | C-14 + C-16 combination | C-14, C-16 | 99.4 |
| V-05 | gate + trajectory + provenance | all three new R3 signals | C-14, C-15, C-16 | 100 |

Divergence check: 97.5 / 98.1 / 98.1 / 99.4 / 100. At least two target different criteria.

SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence
before proceeding to STEP 1.

---

## STEP 1 -- GENERATE 5 VARIATIONS

---

## V-01 -- Phase-End Gate: Declarative COMPLETE Marker

**axis:** phase-end gate
**hypothesis:** V-05 R3 passes C-11 with a dedicated SPREAD-DESIGN PHASE but ends it with "DO NOT
proceed to STEP 1 until..." -- a prohibitive gate that places compliance burden on the operator.
Replacing this with "SPREAD-DESIGN COMPLETE -- confirm axis assignments before proceeding" creates
a declarative phase-end artifact the operator must generate, passing C-14. C-15 remains PARTIAL
(inherited PARTIAL AMPLIFIER lacks Round/Occurrence columns). C-16 remains FAIL (no provenance).
Falsifiable: if the prohibitive gate in V-05 R3 already passes C-14, this variation and V-05 R3
will score identically, collapsing spread.

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
| 1      |      |                 |                     |
| ...    |      |                 |                     |

ROUND 2+ -- PARTIAL-Causal feedback spread design:
Before planning this round's variations, examine the immediately preceding round's output:

Step A -- PARTIAL record review:
List every PARTIAL result from the preceding round's PARTIAL AMPLIFIER table.
For each PARTIAL: which criterion? What element is present but incomplete?

Step B -- Causal-layer review:
List every causal-layer annotation from the preceding round's Step 3 patterns.
For each: what layer (structural / behavioral / pedagogical)? What design dimension does it suggest?

Step C -- Axis assignment from signals:
Assign this round's variation axes by combining:
- Axes that produced PARTIAL passes (incomplete signal worth amplifying)
- Axes whose causal-layer is structural (prompt architecture changes, not just wording)
Do not assign axes that produced only FAIL results with no PARTIAL -- they are dead ends, not seeds.

Output as a table with a Source column:

| Plan # | Axis | Source (PARTIAL/causal-layer citation) | Target Criterion | Predicted Composite |
|--------|------|----------------------------------------|-----------------|---------------------|
| 1      |      |                                        |                 |                     |
| ...    |      |                                        |                 |                     |

SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence
before proceeding to STEP 1.

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
| ...       |        |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
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
- pedagogical: the prompt teaches the scorer why the behavior matters, not just that it is required

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
If Step 3 found zero new patterns, write: "No new criteria proposed this round."

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
Name both rounds explicitly (e.g., "Round 3 and Round 4").

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

## V-02 -- Trajectory Table: Round/Axis/Occurrence/Action Columns

**axis:** trajectory table
**hypothesis:** V-05 R3's PARTIAL AMPLIFIER table (Variation | Criterion | What's Present |
What's Missing) enables C-12 PASS but fails C-15 because it lacks Round and Occurrence-type
columns. Adding a named PARTIAL TRAJECTORY TABLE with columns (Round | Axis | Criterion |
Occurrence | Recommended Action) enables "first-occurrence" vs "repeated-occurrence" diagnosis
and passes C-15. The gate remains "DO NOT proceed until..." (prohibitive), so C-14 FAILS.
C-16 absent, so FAIL.
Falsifiable: if the four-column table PARTIAL scores C-15 as PARTIAL (not PASS), the pass
condition requires additional structure not captured by the column set alone.

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
3. Predict each variation's composite score. If all {N} are identical, redesign before proceeding.

Output as a table:

| Plan # | Axis | Target Criterion | Predicted Composite |
|--------|------|-----------------|---------------------|
| 1      |      |                 |                     |
| ...    |      |                 |                     |

ROUND 2+ -- PARTIAL-Causal feedback spread design:
Before planning this round's variations, examine the immediately preceding round's output:

Step A -- PARTIAL record review:
List every PARTIAL result from the preceding round's PARTIAL TRAJECTORY TABLE.
For each PARTIAL: which criterion? What element is present but incomplete?

Step B -- Causal-layer review:
List every causal-layer annotation from the preceding round's Step 3 patterns.
For each: what layer (structural / behavioral / pedagogical)? What design dimension does it suggest?

Step C -- Axis assignment from signals:
Assign this round's variation axes by combining:
- Axes that produced PARTIAL passes (incomplete signal worth amplifying)
- Axes whose causal-layer is structural (prompt architecture changes, not just wording)
Do not assign axes that produced only FAIL results with no PARTIAL -- they are dead ends, not seeds.

Output as a table with a Source column:

| Plan # | Axis | Source (PARTIAL/causal-layer citation) | Target Criterion | Predicted Composite |
|--------|------|----------------------------------------|-----------------|---------------------|
| 1      |      |                                        |                 |                     |
| ...    |      |                                        |                 |                     |

DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites diverge.

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
| ...       |        |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
PARTIAL counts as 0.5 for composite. Essential criteria require full PASS for TRIAL CONVERGENCE.

PARTIAL TRAJECTORY TABLE -- run after scoring all variations.
Extract PARTIAL results as a persistent cross-round record. Add a row for each PARTIAL:

| Round | Axis | Criterion | Occurrence | Recommended Action |
|-------|------|-----------|------------|-------------------|
|       |      |           | First / Repeated | Amplify (next axis targets this) / Diagnose (structural constraint -- try different mechanism) |

Occurrence rules:
- First: this axis/criterion pair has not appeared in prior rounds' trajectory tables.
- Repeated: this axis/criterion pair appeared in a prior round's trajectory table.

If no PARTIALs this round, write: "No PARTIAL trajectory entries this round."

Reference this table at the top of SPREAD-DESIGN PHASE in the following round.

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation AND
the PARTIAL TRAJECTORY TABLE is updated.

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
- pedagogical: the prompt teaches the scorer why the behavior matters, not just that it is required

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
If Step 3 found zero new patterns, write: "No new criteria proposed this round."

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
Name both rounds explicitly (e.g., "Round 3 and Round 4").

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

## V-03 -- Pattern Provenance: V-XX, R-N Citation

**axis:** pattern provenance
**hypothesis:** No R3 variation carried provenance on excellence patterns. Adding "(V-XX, R-N)" as
a required field in the Step 3 pattern output contract -- identifying which variation and which
round first exhibited the pattern -- passes C-16 because patterns become reproducible and
cross-referenceable. Gate remains prohibitive (C-14 FAIL). Trajectory table not upgraded (C-15
inherits PARTIAL AMPLIFIER without Occurrence column, C-15 PARTIAL).
Falsifiable: if a provenance tag is "V-XX, R-N" with filled-in variation and round but the rubric
requires a specific format beyond these two fields, C-16 will score PARTIAL rather than PASS.

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
3. Predict each variation's composite score. If all {N} are identical, redesign before proceeding.

Output as a table:

| Plan # | Axis | Target Criterion | Predicted Composite |
|--------|------|-----------------|---------------------|
| 1      |      |                 |                     |
| ...    |      |                 |                     |

ROUND 2+ -- PARTIAL-Causal feedback spread design:
Before planning this round's variations, examine the immediately preceding round's output:

Step A -- PARTIAL record review:
List every PARTIAL result from the preceding round's PARTIAL AMPLIFIER table.
For each PARTIAL: which criterion? What element is present but incomplete?

Step B -- Causal-layer review:
List every causal-layer annotation from the preceding round's Step 3 patterns.
For each: what layer (structural / behavioral / pedagogical)? What design dimension does it suggest?

Step C -- Axis assignment from signals:
Assign this round's variation axes by combining:
- Axes that produced PARTIAL passes (incomplete signal worth amplifying)
- Axes whose causal-layer is structural (prompt architecture changes, not just wording)
Do not assign axes that produced only FAIL results with no PARTIAL -- they are dead ends, not seeds.

Output as a table with a Source column:

| Plan # | Axis | Source (PARTIAL/causal-layer citation) | Target Criterion | Predicted Composite |
|--------|------|----------------------------------------|-----------------|---------------------|
| 1      |      |                                        |                 |                     |
| ...    |      |                                        |                 |                     |

DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites diverge.

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
| ...       |        |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
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
Provenance: [V-XX, R-N] (the variation and round that first exhibited this property)
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
Layer: structural | behavioral | pedagogical
Scope: skill-specific | transferable
```

The Provenance field is mandatory. If the pattern is new to this round, cite the current round
and the variation that scores highest. If the pattern appeared in a prior round, cite the
original source: "first exhibited [V-XX, R-N]."

Causal layer definitions:
- structural: the prompt architecture itself enforces the behavior (a missing section makes
  the behavior impossible)
- behavioral: the operator action sequence changes (a step is added, reordered, or gated)
- pedagogical: the prompt teaches the scorer why the behavior matters, not just that it is required

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until all patterns are named with mechanism, Layer, AND Provenance stated.

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
If Step 3 found zero new patterns, write: "No new criteria proposed this round."

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
Name both rounds explicitly (e.g., "Round 3 and Round 4").

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

## V-04 -- Gate + Provenance (C-14 + C-16)

**axis:** phase-end gate + pattern provenance
**hypothesis:** Combining the declarative COMPLETE gate (V-01 axis) and the Provenance field in
the pattern output contract (V-03 axis) should PASS both C-14 and C-16. C-15 remains PARTIAL
because the trajectory table is the inherited PARTIAL AMPLIFIER without Occurrence-type column.
The combination tests whether C-14 and C-16 are independent (no structural interference) or
whether adding provenance forces a gate change.
Falsifiable: if the COMPLETE gate changes C-16 scoring in any direction, the axes interact.

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
3. Predict each variation's composite score. If all {N} are identical, redesign before proceeding.

Output as a table:

| Plan # | Axis | Target Criterion | Predicted Composite |
|--------|------|-----------------|---------------------|
| 1      |      |                 |                     |
| ...    |      |                 |                     |

ROUND 2+ -- PARTIAL-Causal feedback spread design:
Before planning this round's variations, examine the immediately preceding round's output:

Step A -- PARTIAL record review:
List every PARTIAL result from the preceding round's PARTIAL AMPLIFIER table.
For each PARTIAL: which criterion? What element is present but incomplete?

Step B -- Causal-layer review:
List every causal-layer annotation from the preceding round's Step 3 patterns.
For each: what layer (structural / behavioral / pedagogical)? What design dimension does it suggest?

Step C -- Axis assignment from signals:
Assign this round's variation axes by combining:
- Axes that produced PARTIAL passes (incomplete signal worth amplifying)
- Axes whose causal-layer is structural (prompt architecture changes, not just wording)
Do not assign axes that produced only FAIL results with no PARTIAL -- they are dead ends, not seeds.

Output as a table with a Source column:

| Plan # | Axis | Source (PARTIAL/causal-layer citation) | Target Criterion | Predicted Composite |
|--------|------|----------------------------------------|-----------------|---------------------|
| 1      |      |                                        |                 |                     |
| ...    |      |                                        |                 |                     |

SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence
before proceeding to STEP 1.

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
| ...       |        |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
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
Provenance: [V-XX, R-N] (the variation and round that first exhibited this property)
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
Layer: structural | behavioral | pedagogical
Scope: skill-specific | transferable
```

The Provenance field is mandatory. If the pattern is new to this round, cite the current round
and the highest-scoring variation. If the pattern appeared in a prior round, cite the
original source: "first exhibited [V-XX, R-N]."

Causal layer definitions:
- structural: the prompt architecture itself enforces the behavior (a missing section makes
  the behavior impossible)
- behavioral: the operator action sequence changes (a step is added, reordered, or gated)
- pedagogical: the prompt teaches the scorer why the behavior matters, not just that it is required

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until all patterns are named with mechanism, Layer, AND Provenance stated.

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
If Step 3 found zero new patterns, write: "No new criteria proposed this round."

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
Name both rounds explicitly (e.g., "Round 3 and Round 4").

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

## V-05 -- All Three: Gate + Trajectory + Provenance (C-14 + C-15 + C-16)

**axis:** phase-end gate + trajectory table + pattern provenance
**hypothesis:** Combining all three R3 signals should PASS C-14 (declarative COMPLETE gate),
C-15 (trajectory table with Round/Axis/Occurrence/Action columns), and C-16 (Provenance field
per pattern), achieving composite 100 on rubric v3. The combination test: does adding all
three create any new structural property not captured by the individual criteria? If not,
Step 3 will find zero new patterns (confirmed mechanisms only), making R4 the first potential
zero-pattern round.

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
3. Predict each variation's composite score. If all {N} are identical, redesign before proceeding.

Output as a table:

| Plan # | Axis | Target Criterion | Predicted Composite |
|--------|------|-----------------|---------------------|
| 1      |      |                 |                     |
| ...    |      |                 |                     |

ROUND 2+ -- PARTIAL-Causal feedback spread design:
Reference the PARTIAL TRAJECTORY TABLE from the preceding round before assigning axes.

Step A -- PARTIAL trajectory review:
List every entry in the preceding round's PARTIAL TRAJECTORY TABLE.
For each entry: Round, Axis, Criterion, Occurrence (First/Repeated), Recommended Action.
Entries marked Repeated require a different mechanism than amplification -- do not repeat
the same axis without changing the structural approach.

Step B -- Provenance review:
List every pattern from the preceding round's Step 3 with its Provenance field.
For each: was this pattern first exhibited in a prior round? Has it appeared more than once?
Patterns that first appeared 2+ rounds ago and still generate spread indicate a structural
constraint the current rubric may not fully capture.

Step C -- Axis assignment from signals:
Assign this round's variation axes by combining:
- Axes from PARTIAL TRAJECTORY entries marked First (amplify the seed)
- Axes whose patterns carry a structural Layer annotation (prompt architecture must change)
Do not assign axes that produced only FAIL with no PARTIAL -- they are dead ends, not seeds.

Output as a table with a Source column:

| Plan # | Axis | Source (Trajectory/Provenance citation) | Target Criterion | Predicted Composite |
|--------|------|-----------------------------------------|-----------------|---------------------|
| 1      |      |                                         |                 |                     |
| ...    |      |                                         |                 |                     |

SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence
before proceeding to STEP 1.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations. Every step. Every instruction.
Every output contract.

Round 1: change exactly one axis per variation (per SPREAD-DESIGN PHASE plan).
Round 2+: combine axes from the SPREAD-DESIGN PHASE plan -- specifically axes from First-
occurrence trajectory entries or structural-layer patterns in the preceding round.

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
| ...       |        |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
PARTIAL counts as 0.5 for composite. Essential criteria require full PASS for TRIAL CONVERGENCE.

PARTIAL TRAJECTORY TABLE -- run after scoring all variations.
Add a row for each PARTIAL result. Carry forward prior-round entries:

| Round | Axis | Criterion | Occurrence | Recommended Action |
|-------|------|-----------|------------|-------------------|
|       |      |           | First / Repeated | Amplify next round / Diagnose structural constraint |

Occurrence rules:
- First: axis/criterion pair not in any prior round's table.
- Repeated: axis/criterion pair present in a prior round's table.

Reference this table at the top of the following round's SPREAD-DESIGN PHASE.

If no PARTIALs this round, write: "No PARTIAL trajectory entries this round."

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation AND
the PARTIAL TRAJECTORY TABLE is updated.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another (including PASS vs
PARTIAL, or PARTIAL vs FAIL):
```
Pattern name: [short label]
Provenance: [V-XX, R-N] (the variation and round that first exhibited this property)
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule -- not "V-02 scored higher" but the design choice that caused the difference]
Layer: structural | behavioral | pedagogical
Scope: skill-specific | transferable
```

The Provenance field is mandatory. If the pattern is new to this round, cite the current round
and the variation that scores highest. If the pattern appeared in a prior round, cite the
original source: "first exhibited [V-XX, R-N]."

Causal layer definitions:
- structural: the prompt architecture itself enforces the behavior (a missing section makes
  the behavior impossible)
- behavioral: the operator action sequence changes (a step is added, reordered, or gated)
- pedagogical: the prompt teaches the scorer why the behavior matters, not just that it is required

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until all patterns are named with mechanism, Layer, AND Provenance stated.

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
If Step 3 found zero new patterns, write: "No new criteria proposed this round."

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
Name both rounds explicitly (e.g., "Round 3 and Round 4").

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

## STEP 2 -- SCORE EACH VARIATION (Against Rubric v3: C-01..C-16)

Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
PARTIAL = 0.5 for composite; essential criteria require full PASS for TRIAL CONVERGENCE.

---

### V-01 -- Phase-End Gate

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE {N} VARIATIONS [...] STEP 2 -- SCORE EACH VARIATION [...] STEP 3 -- IDENTIFY EXCELLENCE PATTERNS [...] STEP 4 -- PROPOSE RUBRIC CRITERIA" |
| C-02 | PASS | "For each variation, for each criterion: Criterion: C-NN / Result: PASS/PARTIAL/FAIL / Quote: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGED [...] GATE 2 -- QUEST PLATEAUED [...] Name both rounds explicitly. State ONE of: TRIAL CONVERGED / TRIAL NOT CONVERGED. State ONE of: QUEST PLATEAUED / QUEST NOT PLATEAUED." |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields. Note which round added each criterion." |
| C-06 | PASS | "Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]" |
| C-07 | PASS | "ID: C-[NN] / Text: [...] / Weight: [...] / Category: [...] / Pass condition: [...] DO NOT proceed to the convergence check until every proposed criterion has all five fields." |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 3 and Round 4'). State ONE of: QUEST PLATEAUED: [Round X] and [Round Y]..." |
| C-09 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. [...] ROUND 2+ -- PARTIAL-Causal feedback spread design: [...] Assign this round's variation axes by combining: Axes that produced PARTIAL passes..." |
| C-10 | PASS | "Causal constraint: identical composite scores -> no score spread -> no excellence patterns -> round does not count toward the two consecutive zero-pattern rounds required for GATE 2." (inherited from STEP 2 matrix constraint) |
| C-11 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note inside the generation step. [...] SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence before proceeding to STEP 1." -- dedicated labeled heading precedes STEP 1; COMPLETE gate marks exit. |
| C-12 | PASS | "PARTIAL AMPLIFIER -- run after scoring all variations: [...] | Variation | Criterion | What's Present | What's Missing | [...] If the table is empty (no PARTIALs), note: 'No PARTIAL amplifier signals this round.'" |
| C-13 | PASS | "Layer: structural / behavioral / pedagogical [...] Causal layer definitions: - structural: [...] - behavioral: [...] - pedagogical: [...] DO NOT proceed to Step 4 until all patterns are named with mechanism and Layer both stated." |
| C-14 | PASS | "SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence before proceeding to STEP 1." -- explicit declarative phase-end marker naming the phase, requiring confirmation before proceeding. |
| C-15 | PARTIAL | PARTIAL AMPLIFIER table present (Variation/Criterion/What's Present/What's Missing) but lacks Round and Occurrence-type (First/Repeated) columns required for cross-round trajectory tracking. |
| C-16 | FAIL | absent -- Step 3 pattern output contract has Pattern name / Mechanism / Principle / Layer / Scope but no Provenance field. |

essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 6.5 (C-09/C-10/C-11/C-12/C-13/C-14 PASS=1 each; C-15 PARTIAL=0.5; C-16 FAIL=0)
composite = (5/5 * 60) + (3/3 * 30) + (6.5/8 * 10) = 60 + 30 + 8.125 = **98.125**

---

### V-02 -- Trajectory Table

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE [...] STEP 2 -- SCORE [...] STEP 3 -- IDENTIFY EXCELLENCE PATTERNS [...] STEP 4 -- PROPOSE RUBRIC CRITERIA" |
| C-02 | PASS | "For each variation, for each criterion: Criterion: C-NN / Result: PASS/PARTIAL/FAIL / Quote: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...] Name both rounds explicitly. State ONE of: TRIAL CONVERGED / TRIAL NOT CONVERGED. State ONE of: QUEST PLATEAUED / QUEST NOT PLATEAUED." |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields. Note which round added each criterion." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule...]" |
| C-07 | PASS | "ID: C-[NN] / Text / Weight / Category / Pass condition -- all five fields. DO NOT proceed to the convergence check until every proposed criterion has all five fields." |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 3 and Round 4')." |
| C-09 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. [...] ROUND 2+ -- PARTIAL-Causal feedback spread design: [...] Step A -- PARTIAL record review: List every PARTIAL result from the preceding round's PARTIAL TRAJECTORY TABLE." |
| C-10 | PASS | Composite matrix constraint and causal note: "Identical predicted composites mean the round will produce no score spread -- no spread -> no excellence patterns -> round does not count toward GATE 2." |
| C-11 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note inside the generation step. [...] DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites diverge." -- dedicated labeled heading precedes STEP 1. |
| C-12 | PASS | "PARTIAL TRAJECTORY TABLE -- run after scoring all variations. [...] | Round | Axis | Criterion | Occurrence | Recommended Action | [...] Reference this table at the top of SPREAD-DESIGN PHASE in the following round." |
| C-13 | PASS | "Layer: structural / behavioral / pedagogical [...] DO NOT proceed to Step 4 until all patterns are named with mechanism and Layer both stated." |
| C-14 | FAIL | absent -- phase ends with "DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites diverge." This is a prohibitive gate; no declarative "COMPLETE" phase-end marker. |
| C-15 | PASS | "PARTIAL TRAJECTORY TABLE -- run after scoring all variations. Add a row for each PARTIAL result. [...] | Round | Axis | Criterion | Occurrence | Recommended Action | [...] Occurrence rules: First: this axis/criterion pair has not appeared in prior rounds' trajectory tables. Repeated: this axis/criterion pair appeared in a prior round's trajectory table." -- all four required columns present; first/repeated distinction explicit; referenced in SPREAD-DESIGN PHASE for following round. |
| C-16 | FAIL | absent -- Step 3 pattern output contract has Pattern name / Mechanism / Principle / Layer / Scope but no Provenance field. |

essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 6 (C-09..C-13/C-15 PASS; C-14/C-16 FAIL)
composite = (5/5 * 60) + (3/3 * 30) + (6/8 * 10) = 60 + 30 + 7.5 = **97.5**

---

### V-03 -- Pattern Provenance

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE [...] STEP 2 -- SCORE [...] STEP 3 -- IDENTIFY EXCELLENCE PATTERNS [...] STEP 4 -- PROPOSE RUBRIC CRITERIA" |
| C-02 | PASS | "For each variation, for each criterion: Criterion: C-NN / Result: PASS/PARTIAL/FAIL / Quote: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...] Name both rounds explicitly. State ONE of: TRIAL CONVERGED / State ONE of: QUEST PLATEAUED." |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields. Note which round added each criterion." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice that caused the difference]" |
| C-07 | PASS | "ID: C-[NN] / Text / Weight / Category / Pass condition -- DO NOT proceed to the convergence check until every proposed criterion has all five fields." |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 3 and Round 4')." |
| C-09 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. [...] ROUND 2+ -- PARTIAL-Causal feedback spread design: [...] Assign this round's variation axes by combining: Axes that produced PARTIAL passes..." |
| C-10 | PASS | Causal constraint note embedded in spread-design: "A round where all {N} variations produce identical composite scores generates no excellence patterns and does not advance plateau detection." |
| C-11 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note inside the generation step. [...] DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites diverge." |
| C-12 | PASS | "PARTIAL AMPLIFIER -- run after scoring all variations: [...] | Variation | Criterion | What's Present | What's Missing | [...] If the table is empty, note: 'No PARTIAL amplifier signals this round.'" |
| C-13 | PASS | "Pattern name: [...] / Provenance: [...] / Mechanism: [...] / Principle: [...] / Layer: structural / behavioral / pedagogical / Scope: [...] / DO NOT proceed to Step 4 until all patterns are named with mechanism, Layer, AND Provenance stated." |
| C-14 | FAIL | absent -- phase ends with "DO NOT proceed to STEP 1 until the spread-design table is complete and predicted composites diverge." Prohibitive gate; no declarative COMPLETE marker. |
| C-15 | PARTIAL | PARTIAL AMPLIFIER table present (Variation/Criterion/What's Present/What's Missing) but lacks Round and Occurrence-type columns for cross-round trajectory tracking. |
| C-16 | PASS | "Provenance: [V-XX, R-N] (the variation and round that first exhibited this property) [...] The Provenance field is mandatory. If the pattern is new to this round, cite the current round and the highest-scoring variation. If the pattern appeared in a prior round, cite the original source: 'first exhibited [V-XX, R-N].'" -- required field in Step 3 pattern output contract; provenance citation required per pattern. |

essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 6.5 (C-09..C-13/C-16 PASS; C-14 FAIL; C-15 PARTIAL=0.5)
composite = (5/5 * 60) + (3/3 * 30) + (6.5/8 * 10) = 60 + 30 + 8.125 = **98.125**

---

### V-04 -- Gate + Provenance

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE [...] STEP 2 -- SCORE [...] STEP 3 -- IDENTIFY EXCELLENCE PATTERNS [...] STEP 4 -- PROPOSE RUBRIC CRITERIA" |
| C-02 | PASS | "For each variation, for each criterion: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...] State ONE of: TRIAL CONVERGED / TRIAL NOT CONVERGED. State ONE of: QUEST PLATEAUED / QUEST NOT PLATEAUED." |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields. Note which round added each criterion." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule...]" |
| C-07 | PASS | "ID: C-[NN] / Text / Weight / Category / Pass condition -- all five fields required." |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 3 and Round 4')." |
| C-09 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. [...] ROUND 2+ spread design: Step C -- Axis assignment from signals: Assign this round's variation axes by combining: Axes that produced PARTIAL passes..." |
| C-10 | PASS | Causal constraint embedded in spread design instructions. |
| C-11 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note inside the generation step. [...] SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence before proceeding to STEP 1." |
| C-12 | PASS | "PARTIAL AMPLIFIER -- run after scoring all variations: [...] | Variation | Criterion | What's Present | What's Missing |" |
| C-13 | PASS | "Pattern name: [...] / Provenance: [...] / Mechanism: [...] / Principle: [...] / Layer: structural / behavioral / pedagogical [...] DO NOT proceed to Step 4 until all patterns are named with mechanism, Layer, AND Provenance stated." |
| C-14 | PASS | "SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence before proceeding to STEP 1." -- explicit declarative phase-end marker. |
| C-15 | PARTIAL | PARTIAL AMPLIFIER table present (Variation/Criterion/What's Present/What's Missing) but lacks Round and Occurrence-type columns. |
| C-16 | PASS | "Provenance: [V-XX, R-N] (the variation and round that first exhibited this property) [...] The Provenance field is mandatory. If the pattern appeared in a prior round, cite the original source: 'first exhibited [V-XX, R-N].'" |

essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 7.5 (C-09..C-14/C-16 PASS; C-15 PARTIAL=0.5)
composite = (5/5 * 60) + (3/3 * 30) + (7.5/8 * 10) = 60 + 30 + 9.375 = **99.375**

---

### V-05 -- Gate + Trajectory + Provenance

| Criterion | Result | Quote |
|-----------|--------|-------|
| C-01 | PASS | "STEP 1 -- GENERATE [...] STEP 2 -- SCORE [...] STEP 3 -- IDENTIFY EXCELLENCE PATTERNS [...] STEP 4 -- PROPOSE RUBRIC CRITERIA" |
| C-02 | PASS | "For each variation, for each criterion: [...] Complete all criteria for one variation before moving to the next." |
| C-03 | PASS | "GATE 1 -- TRIAL CONVERGENCE [...] GATE 2 -- PLATEAU DETECTION [...] Name both rounds explicitly. State ONE of: TRIAL CONVERGED / State ONE of: QUEST PLATEAUED." |
| C-04 | PASS | "Body: the complete, verbatim, runnable prompt. Not a summary. Not a description." |
| C-05 | PASS | "Write the accumulated rubric (all criteria from all rounds) to: [...] All criteria with all five fields. Note which round added each criterion." |
| C-06 | PASS | "Mechanism: [...] / Principle: [reusable rule -- not 'V-02 scored higher' but the design choice...]" |
| C-07 | PASS | "ID: C-[NN] / Text / Weight / Category / Pass condition -- all five fields. DO NOT proceed to the convergence check until every proposed criterion has all five fields." |
| C-08 | PASS | "Name both rounds explicitly (e.g., 'Round 3 and Round 4')." |
| C-09 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. [...] ROUND 2+ -- PARTIAL-Causal feedback spread design: Reference the PARTIAL TRAJECTORY TABLE from the preceding round before assigning axes. Step A -- PARTIAL trajectory review: List every entry in the preceding round's PARTIAL TRAJECTORY TABLE. [...] Step C -- Axis assignment from signals: Assign this round's variation axes by combining: Axes from PARTIAL TRAJECTORY entries marked First (amplify the seed)..." |
| C-10 | PASS | Causal constraint embedded in spread-design: "A round where all {N} variations produce identical composite scores generates no excellence patterns and does not count toward GATE 2." |
| C-11 | PASS | "SPREAD-DESIGN PHASE / Run this phase before writing any variation body. This is a mandatory procedural step -- not a note inside the generation step. [...] SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence before proceeding to STEP 1." |
| C-12 | PASS | "PARTIAL TRAJECTORY TABLE -- run after scoring all variations. Add a row for each PARTIAL result. [...] | Round | Axis | Criterion | Occurrence | Recommended Action | [...] Reference this table at the top of the following round's SPREAD-DESIGN PHASE." |
| C-13 | PASS | "Pattern name: [...] / Provenance: [...] / Mechanism: [...] / Principle: [...] / Layer: structural / behavioral / pedagogical [...] DO NOT proceed to Step 4 until all patterns are named with mechanism, Layer, AND Provenance stated." |
| C-14 | PASS | "SPREAD-DESIGN COMPLETE -- confirm axis assignments and predicted composite divergence before proceeding to STEP 1." -- explicit declarative phase-end marker; gate is a distinct prompt instruction between spread-design and scoring phases. |
| C-15 | PASS | "PARTIAL TRAJECTORY TABLE -- run after scoring all variations. [...] | Round | Axis | Criterion | Occurrence | Recommended Action | [...] Occurrence rules: First: axis/criterion pair not in any prior round's table. Repeated: axis/criterion pair present in a prior round's table. Reference this table at the top of the following round's SPREAD-DESIGN PHASE." -- all four required columns; first/repeated distinction; explicit cross-round reference. |
| C-16 | PASS | "Provenance: [V-XX, R-N] (the variation and round that first exhibited this property) [...] The Provenance field is mandatory. If the pattern is new to this round, cite the current round and the variation that scores highest. If the pattern appeared in a prior round, cite the original source: 'first exhibited [V-XX, R-N].'" -- mandatory provenance field per pattern in Step 3 contract. |

essential_pass = 5 | recommended_pass = 3 | aspirational_pass = 8 (all C-09..C-16 PASS)
composite = (5/5 * 60) + (3/3 * 30) + (8/8 * 10) = 60 + 30 + 10 = **100**

---

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
| C-11 | A | PASS | PASS | PASS | PASS | PASS |
| C-12 | A | PASS | PASS | PASS | PASS | PASS |
| C-13 | A | PASS | PASS | PASS | PASS | PASS |
| C-14 | A | PASS | FAIL | FAIL | PASS | PASS |
| C-15 | A | PARTIAL | PASS | PARTIAL | PARTIAL | PASS |
| C-16 | A | FAIL | FAIL | PASS | PASS | PASS |
| **COMPOSITE** | | **98.1** | **97.5** | **98.1** | **99.4** | **100** |
| **RANK** | | **3** | **5** | **3** | **2** | **1** |

Composite calculations:
- V-01: (5/5*60) + (3/3*30) + (6.5/8*10) = 60 + 30 + 8.125 = 98.125
- V-02: (5/5*60) + (3/3*30) + (6.0/8*10) = 60 + 30 + 7.500 = 97.500
- V-03: (5/5*60) + (3/3*30) + (6.5/8*10) = 60 + 30 + 8.125 = 98.125
- V-04: (5/5*60) + (3/3*30) + (7.5/8*10) = 60 + 30 + 9.375 = 99.375
- V-05: (5/5*60) + (3/3*30) + (8.0/8*10) = 60 + 30 + 10.000 = 100.000

### PARTIAL AMPLIFIER

| Variation | Criterion | What's Present | What's Missing |
|-----------|-----------|----------------|----------------|
| V-01 | C-15 | PARTIAL AMPLIFIER table (Variation/Criterion/What's Present/What's Missing) | Round and Occurrence-type (First/Repeated) columns for cross-round trajectory tracking |
| V-02 | C-14 | Prohibitive phase gate ("DO NOT proceed until...") | Declarative phase-end marker ("SPREAD-DESIGN COMPLETE -- confirm before proceeding") |
| V-02 | C-16 | Pattern output contract with Name/Mechanism/Principle/Layer/Scope | Provenance field identifying originating variation and round |
| V-03 | C-14 | Prohibitive phase gate | Declarative phase-end marker |
| V-03 | C-15 | PARTIAL AMPLIFIER table | Round and Occurrence-type columns |
| V-04 | C-15 | PARTIAL AMPLIFIER table | Round and Occurrence-type columns |

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

### C-14 spread: V-01/V-04/V-05 PASS; V-02/V-03 FAIL

```
Pattern name: Declarative Closure vs Prohibitive Gate
Mechanism: V-01/V-04/V-05 end the SPREAD-DESIGN PHASE with "SPREAD-DESIGN COMPLETE -- confirm
axis assignments and predicted composite divergence before proceeding to STEP 1" -- a positive
artifact the operator must generate. V-02/V-03 end with "DO NOT proceed to STEP 1 until the
spread-design table is complete and predicted composites diverge" -- a negative constraint the
operator self-polices.
Principle: A declarative phase-end marker ("X COMPLETE") requires the operator to produce a
visible, confirmable artifact before the gate clears; a prohibitive gate ("DO NOT PROCEED until Y")
requires the operator to self-certify compliance with no positive evidence generated. The
declarative form is structurally stronger because non-compliance is detectable; the prohibitive
form allows silent drift.
Layer: structural
Scope: transferable
```

C-14 confirms the mechanism from which C-14 was derived. Not a new pattern.

### C-15 spread: V-02/V-05 PASS; V-01/V-03/V-04 PARTIAL

```
Pattern name: Trajectory Columns as Diagnostic Differentiators
Mechanism: V-02/V-05 include Occurrence (First/Repeated) and Recommended Action columns in the
PARTIAL trajectory table, making the "first vs. repeated" diagnosis explicit and the recommended
intervention machine-readable. V-01/V-03/V-04 include a PARTIAL AMPLIFIER table with
What's Present/What's Missing columns, which records what is incomplete but does not distinguish
whether the incompleteness is a new signal (amplify) or a recurring constraint (diagnose).
Principle: A PARTIAL table that records presence/absence but not occurrence history cannot
distinguish "this axis generated a seed for the first time" from "this axis has been seeding
without converting for two rounds." The occurrence column changes the recommended action,
not just the record.
Layer: behavioral
Scope: transferable
```

C-15 confirms the mechanism from which C-15 was derived. Not a new pattern.

### C-16 spread: V-03/V-04/V-05 PASS; V-01/V-02 FAIL

```
Pattern name: Provenance as Reproducibility Contract
Mechanism: V-03/V-04/V-05 include a mandatory Provenance field in the Step 3 pattern output
contract, citing the originating variation and round (e.g., "V-03, R-2"). V-01/V-02 omit
the Provenance field, listing patterns as undifferentiated discoveries without origin.
Principle: A pattern without a provenance citation is an observation, not a reproducible
finding. Citing origin variation and round makes the pattern re-testable (run the variation
again in a later round -- does the pattern re-emerge?) and trend-detectable (has the same
variation-type generated this pattern across multiple rounds?).
Layer: correctness
Scope: transferable
```

C-16 confirms the mechanism from which C-16 was derived. Not a new pattern.

### V-05 unique behavior

V-05 is the only variation that explicitly connects the PARTIAL TRAJECTORY TABLE and the
Provenance review in the SPREAD-DESIGN PHASE for Round 2+. The ROUND 2+ spread-design
instructions in V-05 contain "Step B -- Provenance review: List every pattern from the
preceding round's Step 3 with its Provenance field. For each: was this pattern first exhibited
in a prior round? Has it appeared more than once? Patterns that first appeared 2+ rounds ago
and still generate spread indicate a structural constraint the current rubric may not fully
capture."

This cross-artifact review (trajectory + provenance) checks whether recurring PARTIAL signals
and recurring spread patterns are correlated -- a signal that the rubric may have a gap rather
than an axis insufficiency. However, this behavior is already partially covered by C-12
(PARTIAL as amplifier) and C-16 (provenance). The specific structural mechanism -- referencing
provenance data during spread design -- is a behavioral combination, not a structural property
absent from all other variations.

Assessment: no new criterion warranted. The "use provenance data during spread design" behavior
is a downstream effect of having both C-15 trajectory data and C-16 provenance data available.
It is implementation detail, not an architectural property that a new rubric criterion would
isolate. A criterion for this would be: "the spread-design phase explicitly instructs the
operator to check provenance annotations when assigning axes." This is narrower than any
existing criterion but too implementation-specific to be a stable rubric criterion.

**Ruling: no new excellence pattern in Round 4.**

All patterns in this round confirm existing criteria (C-14, C-15, C-16). No pattern exhibits
a structural property absent from all existing criteria.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

No new criteria proposed this round. Step 3 found zero new excellence patterns. All spread
was explained by the mechanisms already captured in C-14, C-15, and C-16.

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

Round 4 found: no new excellence patterns. All spread confirmed existing criteria C-14, C-15, C-16.

Round 3 found: Phase bleeding (-> C-14), PARTIAL as table artifact (-> C-15), Excellence
pattern provenance (-> C-16). Three new patterns.

QUEST NOT PLATEAUED: Round 3 found three new excellence patterns (C-14, C-15, C-16). Two
consecutive zero-pattern rounds not yet achieved. Round 4 is the first zero-pattern round.
Round 5 must also find zero new patterns to satisfy GATE 2.

---

Dual convergence not reached. TRIAL CONVERGED but QUEST NOT PLATEAUED.

Next round: R5. Rubric remains at v3 (no new criteria proposed in R4).
V-05 is the leading variation at composite 100.

For R5 to satisfy GATE 2: Step 3 must find zero new excellence patterns (as in Round 4).
If R5 also finds zero new patterns, the GATE 2 declaration becomes:
"Round 4 and Round 5 both found zero new excellence patterns. QUEST PLATEAUED."
Combined with TRIAL CONVERGED, dual convergence is achieved and the golden is declared.

**Status:** TRIAL CONVERGED (R1-R4). QUEST tracking: R1 found N patterns, R2 found 3
patterns, R3 found 3 patterns, R4 found 0 patterns. First zero-pattern round: R4.
Plateau requires R5 also finding zero patterns.

R5 variation design note: to maximize the chance of detecting any remaining patterns,
R5 should probe the boundary conditions of C-14/C-15/C-16 -- specifically:
- Does the Provenance field change scoring behavior when the same pattern is re-exhibited
  in a later round (cite original vs. current round)?
- Does the trajectory table's Occurrence column correctly trigger "Diagnose structural
  constraint" vs "Amplify" recommendations when it fires in practice?
- Does the COMPLETE gate prevent phase-bleed in adversarial conditions (long axes tables,
  many variations)?
If these boundary probes generate no new spread, plateau is confirmed.
