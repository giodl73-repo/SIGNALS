Now I have the full golden prompt structure. Let me write 5 complete single-axis (and combined) variations for Round 1.

---

# quest-golden Variate — Round 1

**Date:** 2026-03-15
**Skill:** quest-golden
**Rubric:** v1 (C-01 through C-10; essential C-01–C-05)
**Round:** R1 — single-axis first (V-01, V-02, V-03), then 2 combinations (V-04, V-05)

---

## Variation Map

| V | Axis | Hypothesis focus |
|---|------|-----------------|
| V-01 | role-sequence | Target-declaration first improves C-03 |
| V-02 | output-format | Table-native scoring improves C-05 |
| V-03 | lifecycle-emphasis | Named PHASE gates improve C-01 |
| V-04 | phrasing-register + inertia-framing | Champion-challenger register improves C-06 |
| V-05 | role-sequence + output-format | Combined V-01 + V-02 targets C-03 and C-05 simultaneously |

---

## V-01 — Role Sequence

**axis:** role-sequence
**hypothesis:** Declaring the golden artifact output contract (what will be written upon convergence) at the TOP, before the loop begins, will improve C-03 (golden prompt body written as self-contained skill artifact) because the operator has the output spec in working memory during generation — preventing the common failure of producing a description of the prompt instead of the prompt itself. Predicted improvement: C-03 PASS rate up; no regression on C-01, C-02, C-04, C-05.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

TARGET DECLARATION — READ THIS FIRST

When this loop converges, you will write exactly two artifacts:

ARTIFACT 1 — Golden prompt body:
  Path: simulations/quest/golden/{skill-name}-golden-{date}.md
  Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
  Body: the complete, verbatim, runnable prompt — not a summary, not a description, not bullet points.
  A reader must be able to copy the body and use it as the operative skill prompt without modification.

ARTIFACT 2 — Converged rubric:
  Path: simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
  All criteria with all five fields (ID, Text, Weight, Category, Pass condition).
  Includes every criterion added during the loop via QU3/QU4. Note which round added each.

Hold these output contracts in working memory throughout the loop.
Every variation you write is a candidate body for ARTIFACT 1.

---

DUAL CONVERGENCE — THE LOOP EXITS ONLY WHEN BOTH GATES PASS IN THE SAME ROUND

GATE 1 — TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy. Only PASS counts.

GATE 2 — QUEST PLATEAUED
Step 3 in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND both found zero new excellence patterns.
One zero-pattern round is not enough. Two consecutive zero-pattern rounds are required.
Both rounds must be cited by name — not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

STEP 1 — GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations.
Every variation is a full prompt — not a diff, not an excerpt, not a reference to another variation.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria. A round where all {N} variations produce identical composite scores generates no excellence patterns and does not advance plateau detection.

Causal constraint: identical composite scores → no score spread → no excellence patterns → round does not count toward the two consecutive zero-pattern rounds required for GATE 2.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity

Label each variation:

```
## V-NN — [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body — every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 — SCORE EACH VARIATION

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

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another:

```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule — not "V-02 scored higher" but the design choice that caused the difference]
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

STEP 4 — PROPOSE RUBRIC CRITERIA

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

GATE 1 — TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 — PLATEAU DETECTION

State what Step 3 found in the CURRENT ROUND: [pattern names] OR "no new patterns."
State what Step 3 found in the IMMEDIATELY PRECEDING ROUND by name: [patterns] OR "no new patterns."
Name both rounds explicitly (e.g., "Round 2 and Round 3").

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

Write ARTIFACT 1 and ARTIFACT 2 as declared in the TARGET DECLARATION at the top of this prompt.

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write the full prompt body verbatim to ARTIFACT 1 path.
3. Write the accumulated rubric to ARTIFACT 2 path.
4. State both file paths.

---

## V-02 — Output Format

**axis:** output-format
**hypothesis:** Replacing code-block per-criterion scoring with inline table rows will improve C-05 (numeric composite tracked per round per variation) because the composite calculation is embedded directly in the scoring table rather than as a post-hoc computation. Predicted improvement: C-05 PASS rate up (composite always computed); possible improvement on C-06 (patterns emerge from adjacent table rows). No predicted regression.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE — READ THIS FIRST

This loop runs until BOTH of the following gates are satisfied SIMULTANEOUSLY in the same round:

GATE 1 — TRIAL CONVERGED
Every variation in the current round passes every essential rubric criterion.
PARTIAL does not satisfy an essential criterion. Only PASS counts.

GATE 2 — QUEST PLATEAUED
Step 3 (excellence patterns) in the CURRENT ROUND and in the IMMEDIATELY PRECEDING ROUND both found zero new excellence patterns.
One zero-pattern round is not enough. Two consecutive zero-pattern rounds are required.
Both rounds must be cited by explicit name — not "the last two rounds."

Declare golden ONLY when GATE 1 and GATE 2 are both satisfied in the same round.

---

STEP 1 — GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts — not diffs, not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and confirm at least two variations target different rubric criteria. A round where all {N} variations produce identical composite scores generates no excellence patterns and does not advance plateau detection.

Causal constraint: identical composite scores → no score spread → no excellence patterns → round does not count toward the two consecutive zero-pattern rounds required for GATE 2.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity

Label each variation:

```
## V-NN — [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body — every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 — SCORE EACH VARIATION

For each variation, score every criterion in a single inline table. Compute the composite immediately after each variation — do not defer.

Per-variation scoring table format:

**V-NN — [axis name]**

| C  | Weight | Result | Evidence (quote or "absent") |
|----|--------|--------|------------------------------|
| C-01 | E | PASS/FAIL | "[quote]" |
| C-02 | E | PASS/FAIL | "[quote]" |
| C-03 | E | PASS/FAIL | "[quote]" |
| C-04 | E | PASS/FAIL | "[quote]" |
| C-05 | E | PASS/FAIL | "[quote]" |
| C-06 | R | PASS/FAIL | "[quote]" |
| C-07 | R | PASS/FAIL | "[quote]" |
| C-08 | R | PASS/FAIL | "[quote]" |
| C-09 | A | PASS/FAIL | "[quote]" |
| C-10 | A | PASS/FAIL | "[quote]" |

Essential pass: N/5 → E-pts = N/5 × 60 = ___
Recommended pass: N/3 → R-pts = N/3 × 30 = ___
Aspirational pass: N/2 → A-pts = N/2 × 10 = ___
**COMPOSITE: ___**

Repeat this table for every variation before proceeding.

After all per-variation tables are complete, produce the summary matrix:

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

DO NOT proceed to Step 3 until every composite is computed and entered in the summary matrix.

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another:

| Pattern | Mechanism | Principle | Scope |
|---------|-----------|-----------|-------|
| [short label] | [structural property in better-scoring variation] | [reusable design rule] | skill-specific / transferable |

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection. Redesign variations for divergence in the next round."

List criteria where all variations fail:

| Criterion | Diagnosis |
|-----------|-----------|
| C-NN | rubric-gap / skill-gap |

DO NOT proceed to Step 4 until all patterns are in the table.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion:

| Field | Value |
|-------|-------|
| ID | C-[NN] |
| Text | [one sentence] |
| Weight | essential / recommended / aspirational |
| Category | structure / behavior / correctness / depth / coverage |
| Pass condition | [one auditable sentence] |

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

GATE 1 — TRIAL CONVERGENCE

| Variation | All essential pass? | Failing criteria |
|-----------|---------------------|-----------------|
| V-01 | YES/NO | — |
| V-02 | YES/NO | — |
| ... | | |

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [list V-NN / C-NN failures]

GATE 2 — PLATEAU DETECTION

| Round | New patterns found |
|-------|--------------------|
| [Current round name] | [pattern names] / none |
| [Prior round name] | [pattern names] / none |

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

## V-03 — Lifecycle Emphasis

**axis:** lifecycle-emphasis
**hypothesis:** Adding explicit PHASE labels (PHASE 0 through PHASE 5) with hard DO NOT PROCEED gates and a round-start checklist will improve C-01 (full loop with 2+ rounds of named variations and scores) because incomplete executions typically abort between phases; named gates create a visible checklist that makes early stopping an explicit decision rather than an accidental omission. Predicted improvement: C-01 PASS rate up; possible improvement on C-07 (QU3/QU4 trace) because PHASE 4 is explicitly labeled as the criterion-proposal phase.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

DUAL CONVERGENCE — READ THIS FIRST

This loop runs until BOTH gates are satisfied SIMULTANEOUSLY in the same round.

GATE 1 — TRIAL CONVERGED: every variation in the current round passes every essential criterion. PARTIAL does not count.
GATE 2 — QUEST PLATEAUED: the current round AND the immediately preceding round (cited by name) both found zero new excellence patterns.

Declare golden ONLY when both gates pass together.

---

ROUND STRUCTURE

Every round runs exactly these phases in order. Do not skip. Do not merge.

```
PHASE 0 — SPREAD AUDIT         (before writing any variation)
PHASE 1 — GENERATION           (write all variation bodies)
PHASE 2 — SCORING              (score all variations, compute composites)
PHASE 3 — PATTERN EXTRACTION   (name excellence patterns with mechanism)
PHASE 4 — CRITERION PROPOSAL   (QU3 proposals + QU4 application)
PHASE 5 — CONVERGENCE CHECK    (both gates, golden declaration if met)
```

---

PHASE 0 — SPREAD AUDIT

Before writing any variation body, complete this audit:

```
Round: [R-NN]
Axes assigned:
  V-01: [axis]
  V-02: [axis]
  ...
Criteria targeted (at least 2 must differ):
  V-01 targets: [C-NN]
  V-02 targets: [C-NN]
  ...
Spread confirmed: YES (at least 2 different target criteria) | NO (re-assign axes)
```

If spread is NO: reassign axes until at least two variations target different rubric criteria.

DO NOT PROCEED TO PHASE 1 until spread is confirmed YES.

---

PHASE 1 — GENERATION

Write {N} complete, standalone skill body variations. These are full prompts — not diffs, not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity

Label each variation:

```
## V-NN — [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body — every step, every instruction, every output contract]
```

DO NOT PROCEED TO PHASE 2 until all {N} variation bodies are written in full. No placeholders.

---

PHASE 2 — SCORING

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

DO NOT PROCEED TO PHASE 3 until per-criterion evidence is recorded for every variation and all composites are computed.

---

PHASE 3 — PATTERN EXTRACTION

For each criterion where at least one variation scores higher than another:

```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule — not "V-02 scored higher" but the design choice that caused the difference]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection. Redesign variations for divergence in the next round."

List any criterion all variations fail:

```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT PROCEED TO PHASE 4 until all patterns are named with mechanism stated.

---

PHASE 4 — CRITERION PROPOSAL (QU3 + QU4)

For each pattern from Phase 3, propose a criterion (QU3):

```
ID:             C-[NN] (next sequential after current rubric's highest)
Text:           [what the criterion measures, one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence, no interpretation required]
```

For each QU3 proposal, state the approval decision: APPROVED | REJECTED | DEFERRED.

For each APPROVED proposal, execute QU4: add the criterion to the working rubric and note:

```
QU4 applied: C-[NN] added to rubric. Now scoring against [N+1] criteria starting next round.
```

DO NOT PROCEED TO PHASE 5 until every proposed criterion has all five fields and an approval decision.

---

PHASE 5 — CONVERGENCE CHECK

GATE 1 — TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 — PLATEAU DETECTION

State what Phase 3 found in the CURRENT ROUND by round name: [pattern names] OR "no new patterns."
State what Phase 3 found in the IMMEDIATELY PRECEDING ROUND by round name: [pattern names] OR "no new patterns."

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

If not converged: begin the next round at PHASE 0.

---

WRITE GOLDEN ARTIFACTS (dual convergence only — after Phase 5 declares both gates met)

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

## V-04 — Phrasing Register + Inertia Framing

**axis:** phrasing-register + inertia-framing
**hypothesis:** Conversational imperative register (short sentences, direct commands) combined with explicit champion framing (V-00 as the current skill body baseline scored alongside variations) will improve C-06 (excellence pattern named with structural cause) because operators must explicitly articulate why a variation beats V-00, forcing mechanism identification rather than score-differential description. Predicted: C-06 PASS rate up, C-09 PASS rate up (champion anchor makes element mapping natural). Possible risk: C-03 FAIL if champion framing distracts from golden prompt writing.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

The goal: find the best possible version of this skill's prompt body. You do that by writing variations, scoring them, extracting what makes the best ones work, and iterating until the loop stabilizes.

The loop exits when two things are true at once:
(a) every variation in the current round passes every essential criterion — trial converged
(b) the current round AND the prior round both produced zero new excellence patterns — quest plateaued

Neither condition alone is enough. Cite both by name when you declare convergence.

---

STEP 1 — SET THE CHAMPION

Before writing any variations, score the CURRENT skill body (V-00) against the rubric.

V-00 is the baseline. Every variation must beat V-00 on at least one criterion to be worth keeping. If V-00 already scores 100, note that and proceed — the loop still runs for plateau detection.

Score V-00 using the same format as Step 2.

---

STEP 2 — WRITE VARIATIONS

Write {N} complete skill body variations. Full prompts — not diffs, not summaries.

Before writing, assign axes:

```
V-01 axis: [name]  targets: [C-NN]
V-02 axis: [name]  targets: [C-NN]
...
```

At least two variations must target different criteria. If all {N} variations would target the same criterion, reassign before writing.

Round 1: one axis per variation.
Round 2+: combine axes that produced signal against V-00 or prior rounds.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity

Label each:

```
## V-NN — [Axis Name]
axis: [name]
hypothesis: [what changes vs V-00, which criterion improves, falsifiable]
[complete prompt body]
```

Do not proceed to Step 3 until all variation bodies are written in full.

---

STEP 3 — SCORE ALL VARIATIONS (INCLUDING V-00)

Score V-00 and every variation against every criterion.

For each variation (starting with V-00), for each criterion:

```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[quote from the body or 'absent']"
```

Then compute:

```
V-NN composite: (E-pass/5 × 60) + (R-pass/3 × 30) + (A-pass/2 × 10) = [value]
```

After all variations: produce the summary matrix including V-00.

| Criterion | Weight | V-00 | V-01 | V-02 | ... |
|-----------|--------|------|------|------|-----|
| ...       |        |      |      |      |     |
| COMPOSITE |        |      |      |      |     |
| DELTA vs V-00 |    | —    |      |      |     |

Do not proceed to Step 4 until composites are computed and deltas vs V-00 are filled in.

---

STEP 4 — EXTRACT PATTERNS

For each criterion where at least one variation outperforms V-00:

```
Pattern name: [short label]
What V-00 lacks: [structural property missing from V-00]
What the better variation has: [structural property present]
Mechanism: [why this property causes the criterion score to change]
Principle: [reusable design rule]
Scope: skill-specific | transferable
```

If no variation outperforms V-00 on any criterion:
"No improvement over champion. V-00 is locally optimal. Redesign variation axes."

If some variations underperform V-00, list the regression and its cause:

```
Regressed criterion: C-NN  in V-NN
Cause: [structural property in V-NN that broke what V-00 had]
```

Do not proceed to Step 5 until all patterns are named with mechanism stated.

---

STEP 5 — PROPOSE CRITERIA

For each pattern, propose a rubric criterion (QU3):

```
ID:             C-[NN]
Text:           [one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence]
Approval:       APPROVED | REJECTED | DEFERRED
```

For each APPROVED criterion, execute QU4 immediately:

```
QU4: C-[NN] added to working rubric. Apply from next round.
```

Do not proceed to the convergence check until all proposed criteria have an approval decision.

---

CONVERGENCE CHECK

GATE 1 — TRIAL CONVERGED?

For each variation (not including V-00): does it pass every essential criterion?

State:
- TRIAL CONVERGED: all {N} variations pass all essential criteria.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. ...

GATE 2 — QUEST PLATEAUED?

Current round ([Round name]): [pattern names] | no new patterns
Prior round ([Round name]): [pattern names] | no new patterns

State:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: ...

Declare golden ONLY if both gates pass. Otherwise: advance V-00 to the new champion (highest-composite variation this round) and begin the next round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write the accumulated rubric to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria. Note which round added each.

4. State both file paths.

---

## V-05 — Role Sequence + Output Format

**axis:** role-sequence + output-format
**hypothesis:** Combining target-declaration-first (V-01 axis) with table-native scoring (V-02 axis) will achieve 100 composite by targeting C-03 and C-05 simultaneously: the output contract at the top prevents description-instead-of-body failures; the inline table composites prevent deferred calculation failures. Predicted: both C-03 and C-05 PASS, no regression on other essentials.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

TARGET DECLARATION — READ BEFORE RUNNING THE LOOP

When this loop converges, write exactly two artifacts:

ARTIFACT 1:
  File: simulations/quest/golden/{skill-name}-golden-{date}.md
  Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
  Body: the complete, verbatim, runnable prompt — not a description, not a summary, not bullets.
  Copy-paste ready. A reader must be able to use it without modification.

ARTIFACT 2:
  File: simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
  All criteria from all rounds, each with five fields (ID, Text, Weight, Category, Pass condition).
  Label which round added each criterion.

---

DUAL CONVERGENCE — THE LOOP EXITS ONLY WHEN BOTH GATES PASS IN THE SAME ROUND

GATE 1 — TRIAL CONVERGED: every variation in the current round passes every essential criterion.
GATE 2 — QUEST PLATEAUED: the current round AND the immediately preceding round (cited by name) both found zero new excellence patterns.

Neither gate alone is sufficient. Declare golden only when both pass together.

---

STEP 1 — GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. Full prompts — not diffs, not excerpts.

Spread-design first: assign axes and confirm at least two variations target different criteria before writing bodies.

```
V-01 axis: [name]  targets: [C-NN]
V-02 axis: [name]  targets: [C-NN]
...spread confirmed: YES / NO
```

Round 1: one axis per variation.
Round 2+: combine axes that produced signal.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity

Format each:

```
## V-NN — [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[complete prompt body]
```

DO NOT proceed to Step 2 until all variation bodies are complete.

---

STEP 2 — SCORE ALL VARIATIONS

Score every variation in a per-variation inline table. Compute composite immediately after each.

Format for each variation:

**V-NN — [axis name]**

| C | Weight | Result | Evidence |
|---|--------|--------|----------|
| C-01 | E | PASS/FAIL | "[quote or 'absent']" |
| C-02 | E | PASS/FAIL | "[quote or 'absent']" |
| C-03 | E | PASS/FAIL | "[quote or 'absent']" |
| C-04 | E | PASS/FAIL | "[quote or 'absent']" |
| C-05 | E | PASS/FAIL | "[quote or 'absent']" |
| C-06 | R | PASS/FAIL | "[quote or 'absent']" |
| C-07 | R | PASS/FAIL | "[quote or 'absent']" |
| C-08 | R | PASS/FAIL | "[quote or 'absent']" |
| C-09 | A | PASS/FAIL | "[quote or 'absent']" |
| C-10 | A | PASS/FAIL | "[quote or 'absent']" |

E-pass: _/5 → E-pts = _/5 × 60 = __
R-pass: _/3 → R-pts = _/3 × 30 = __
A-pass: _/2 → A-pts = _/2 × 10 = __
**COMPOSITE: __**

Repeat for every variation. Then produce the summary matrix:

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

DO NOT proceed to Step 3 until all composites are computed and filled into the summary matrix.

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another:

```
Pattern name: [short label]
Mechanism: [structural property present in better-scoring variations, absent from worse-scoring ones]
Principle: [reusable rule — the design choice, not the score delta]
Scope: skill-specific | transferable
```

If no score spread:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection. Redesign variations for divergence in the next round."

Criteria where all variations fail:

```
Criterion: C-NN
Diagnosis: rubric-gap | skill-gap
```

DO NOT proceed to Step 4 until all patterns include mechanism.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern, propose a criterion (QU3):

```
ID:             C-[NN]
Text:           [one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence]
Approval:       APPROVED | REJECTED | DEFERRED
```

For each APPROVED criterion, execute QU4:

```
QU4: C-[NN] added to working rubric. Applies from next round.
```

DO NOT proceed to the convergence check until all proposals have approval decisions.

---

CONVERGENCE CHECK

GATE 1 — TRIAL CONVERGENCE

| Variation | All essential PASS? | Failing (if any) |
|-----------|---------------------|-----------------|
| V-01      | YES/NO              |                 |
| V-02      | YES/NO              |                 |
| ...       |                     |                 |

TRIAL CONVERGED / TRIAL NOT CONVERGED: [details]

GATE 2 — PLATEAU DETECTION

| Round | New patterns |
|-------|-------------|
| [Current round] | [names or "none"] |
| [Prior round]   | [names or "none"] |

QUEST PLATEAUED / QUEST NOT PLATEAUED: [cite both round names]

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

Write ARTIFACT 1 and ARTIFACT 2 as declared in the TARGET DECLARATION above.

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write ARTIFACT 1: the full verbatim prompt body.
3. Write ARTIFACT 2: the accumulated rubric with all criteria.
4. State both file paths.

---

*Round 1 variations complete. Ready for scoring.*
