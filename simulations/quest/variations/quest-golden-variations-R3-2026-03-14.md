Variations written to `simulations/quest/variations/quest-golden-variations-R3-2026-03-14.md`.

---

## R3 Variations — quest-golden

Five complete, runnable variations across three single-axis and two combination designs:

| ID | Axis | Hypothesis | Expected |
|----|------|-----------|---------|
| **V-01** | Competitive/inertia framing only — no causal statement | Passes C-12 (mechanism b), fails C-11 and C-13. Boundary test for R2-P2 under v3. | 96 |
| **V-02** | Explicit dual-mechanism — both competitive and causal labeled in Phase 1 | All 13 pass. Tests whether naming both mechanisms explicitly is more robust than single-causal. | 100 |
| **V-03** | Compact plateau gate — no round-naming template | Fails C-08 alone (compact gate language doesn't instruct round-naming). All aspirational including C-11/C-12/C-13 pass. | 90 |
| **V-04** | DO NOT gates + rubric-audit Step 0 + dual mechanism + pre-printed gate slots | All 13 pass. Maximum structural coverage of C-08, C-11, C-12, C-13 simultaneously. | 100 |
| **V-05** | Stability baseline — R2-V-05 verbatim | R2-V-05 passes C-12 (divergence instruction, mechanism a) and C-13 (causal statement). Scores 100 under v3. | 100 |

**Designed score spread**: V-03=90, V-01=96, V-02/V-04/V-05=100. Spread isolates two already-captured failure modes (C-08 and C-11/C-13) — confirming no new structural weaknesses in the champions under v3.

**R3 expected finding**: Zero new excellence patterns. The score spread is fully explained by existing criteria. This is the quest's first zero-pattern round. For plateau detection, R4 must also produce zero new patterns.

**Convergence projection after R3**:
- GATE 1 (TRIAL): CONVERGED — all 5 pass essential criteria
- GATE 2 (PLATEAU): NOT PLATEAUED — R2 had 2 new patterns; R3 has 0. Need two consecutive zero-pattern rounds.
- Action: **RUN ANOTHER ROUND** (R4)

**Leading candidates entering R4**: V-02, V-04, V-05 (all tied at 100). Structural differentiators to probe in R4:
- V-04 has the rubric-audit Step 0 — not captured by any criterion; could yield C-14 if it produces measurable divergence improvement
- V-02 has labeled dual-mechanism — most explicit C-12/C-13 coverage
- V-05 has the most minimal structure among 100-scorers — baseline robustness
ive + DO NOT) | V-03 | V-05 (repaired) | V-05 (stability) |
| Combination (lifecycle + tables) | V-04 | -- | -- |
| Pre-printed convergence slots | V-05 | V-04 | V-04 |
| Inertia framing only | -- | V-01 | V-01 (confirm) |
| Rubric-first role sequence | -- | V-02 | V-04 (combined) |
| Compact lifecycle / gate | -- | V-03 | V-03 (gate variant) |
| Dual-mechanism (competitive + causal) | -- | -- | V-02 (new) |
| Rubric-audit + DO NOT + dual mechanism | -- | -- | V-04 (new combination) |

---

## V-01

**Variation axis**: Competitive/inertia framing only in generation phase -- no causal statement
**Hypothesis**: Passes C-12 via competitive framing (mechanism b of C-12 pass condition).
Fails C-11 and C-13 because the causal explanation that identical-composite rounds do not
advance plateau detection is absent. Confirms R2-P2 holds under v3: competitive framing
and causal explanation are non-substitutes for C-11, regardless of C-12 satisfaction.
**Champion relation**: structural alternative -- deliberately omits causal mechanism to
stress-test the C-11/C-13 boundary

```
You are running quest-golden for {skill}.

LOAD INPUTS

1. Load the skill spec from signal.skills.yaml (description field) or the spec file.
2. Load the current rubric from simulations/quest/rubrics/{skill}-rubric-*.md.
   If no rubric file exists: write a v1 rubric with at least one essential criterion.
   Write it to disk before continuing. State the path and version.

CURRENT CHAMPION

State at the start of every round:
  Champion: [highest-scoring variation from last round, or "none -- Round 1"]
  Champion composite: [score, or "N/A"]
  Champion weak points: [criteria where champion scored FAIL, PARTIAL, or scored lowest
                         among passing variations; or "N/A -- Round 1"]

FOR EACH ROUND, EXECUTE STEPS 1-4 IN ORDER.

STEP 1 -- GENERATE VARIATIONS

Generate 5 complete, runnable prompt bodies labeled V-01 through V-05.
Each variation must be a full prompt -- not a diff, not a summary.
Each must include:
  - Label: V-NN
  - Axis: [the single design dimension this variation tests]
  - Hypothesis: [what this axis is predicted to change relative to the current champion]
  - Champion relation: [beats champion on C-NN | baseline -- matches champion approach |
                        structural alternative -- approach the champion has not tried]

Round 1: each variation must vary only one axis.
Round 2+: combine axes that produced signal. Design rules:
  - At least two variations must directly target one of the champion's weak points.
  - At least one variation must match the champion approach (stability baseline).
  - At least one variation must try a structural approach the champion has not used.

DO NOT proceed to Step 2 until all 5 variation bodies are written in full.

STEP 2 -- SCORE EACH VARIATION

Score every variation against every criterion in the current rubric.
For every criterion, write:
  Result: PASS | PARTIAL | FAIL
  Evidence: [specific text from variation, or property absent]

After all criteria, compute composite score per rubric formula. Produce summary matrix:

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| C-01      | E  |      |      |      |      |      |
...
| COMPOSITE |    |      |      |      |      |      |
| RANK      |    |      |      |      |      |      |

Results: PASS | PARTIAL | FAIL only.
For every FAIL or PARTIAL, write one evidence note:
  [V-NN / C-NN]: [specific structural property absent or present]

DO NOT proceed to Step 3 until criterion-by-criterion scores are complete for all 5.

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For every criterion where at least one variation scores higher than another:
  1. Name the structural property that caused the difference as a reusable principle --
     not "V-03 passed" but the design choice V-03 made that others did not.
  2. Tag: skill-specific | transferable
  3. Mechanism: the specific prompt property present in passing variations, absent
     from failing ones.

List any criterion where all variations fail:
  Diagnosis: rubric-gap | skill-gap

Round 2+: list any variation that passed a criterion last round but fails now.

If no variation outperforms any other on any criterion, state:
  "No score spread this round. No new patterns extracted."

DO NOT proceed to Step 4 until all patterns are named and scoped.

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each excellence pattern from Step 3, propose a new rubric criterion:
  ID:             C-[NN]
  Text:           [criterion text]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence]

State each proposal. Wait for approval before adding to rubric.
On approval: update rubric file, increment version, state new path.

CONVERGENCE -- CHECK BOTH GATES INDEPENDENTLY

GATE 1 (TRIAL): Do all variations pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED
  If NOT CONVERGED: list which variations failed which essential criteria.

GATE 2 (PLATEAU): Did Step 3 in this round AND in the immediately preceding round
  both produce zero new excellence patterns?
  Name both rounds explicitly.
  State: QUEST PLATEAUED (Round X and Round Y) or QUEST NOT PLATEAUED

DO NOT declare golden unless both gates are satisfied simultaneously.
If only Gate 1 is satisfied: run another round.
If only Gate 2 is satisfied: run another round.

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation from this round.
2. Write the full prompt body verbatim to:
     simulations/quest/golden/{skill}-golden-{date}.md
   Frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN
   Body: the complete, runnable prompt text. Not a summary. Not a pointer.
3. Write the final accumulated rubric to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
   Include all criteria from all rounds.

DO NOT write only a summary of the prompt. Write the complete prompt body.
DO NOT declare this task complete until both files are written to disk and paths stated.
```

---

## V-02

**Variation axis**: Explicit dual-mechanism spread design -- both competitive framing and
causal explanation named and labeled in the generation phase
**Hypothesis**: All 13 criteria pass. Explicitly naming and labeling both spread mechanisms
(a. competitive = force divergence through champion pressure; b. causal = explain why uniform
rounds stall plateau detection) produces a prompt unambiguous on C-12 and C-13 simultaneously.
A model following V-02 has two independently named reasons to design divergent variations.
**Champion relation**: beats champion on C-12/C-13 explicitness; tests whether explicit
dual-mechanism labeling is more robust than single-mechanism causal (V-05, V-04 R2)

```
You are running quest-golden for {skill}.

LOAD INPUTS
  Skill spec: signal.skills.yaml or simulations/draft/specs/
  Rubric: simulations/quest/rubrics/{skill}-rubric-*.md (latest version)
  If no rubric exists: write a v1 rubric with at least one essential criterion before
  continuing. Record the rubric version and round number at the start of each round.

PER-ROUND EXECUTION

--- PHASE 1: GENERATE ---

Generate 5 complete, runnable skill body prompt variations labeled V-01 through V-05.
Each is a full prompt body -- not a diff, not a summary.

Per variation:
  V-NN
  Axis: [the design dimension this variation tests]
  Hypothesis: [predicted score effect relative to the current champion]
  Champion relation: [beats champion on C-NN | baseline | structural alternative]
  Body: [full prompt text]

Round 1: single-axis only.
Round 2+: combine axes that produced signal. Design rules:
  - Name the current champion (highest scorer from last round).
  - At least two variations must target a criterion where the champion scored below
    its theoretical maximum.
  - At least one must match the champion approach (stability baseline).
  - At least one must try a structural approach the champion has not used.

Spread-design (BOTH mechanisms required; label each explicitly):

  a. Competitive mechanism: at least two variations must be explicitly designed to
     beat the champion on one or more of its named weak-point criteria. State which
     criteria each variation targets.

  b. Causal mechanism: rounds where all variations produce identical composite scores
     generate no new excellence patterns and do not advance plateau detection. Design
     variations that are structurally distinct enough to score differently on at least
     one criterion.

Both mechanisms reinforce each other and address different failure modes. Neither alone
is sufficient when the other is absent.

--- PHASE 2: SCORE ---

Score every variation against every criterion in the current rubric.

Score matrix:

| ID   | Criterion (short)       | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------------------|----|------|------|------|------|------|
| C-01 | [text]                  | E  |      |      |      |      |      |
| C-02 | [text]                  | E  |      |      |      |      |      |
...
| --   | COMPOSITE               |    |      |      |      |      |      |
| --   | RANK (1=best)           |    |      |      |      |      |      |

Results: PASS | PARTIAL | FAIL only.
For every FAIL or PARTIAL, add one evidence note:
  [V-NN / C-NN]: [the specific structural property absent or present]

--- PHASE 3: IDENTIFY ---

For each criterion with score spread (at least one variation outperforms another):
  Pattern: [the design principle that caused the difference -- as a reusable rule,
            not a variation name]
  Scope: skill-specific | transferable
  Trigger: C-[NN] -- spread: [V-01=X, V-02=X, ...]
  Mechanism: [structural property present in passing variations, absent from failing ones]

If no variation outperforms any other on any criterion:
  State: "No score spread this round. No patterns extracted.
  Redesign variations for divergence in the next round."

Failure patterns (all fail a criterion):
  Criterion: [ID]
  Diagnosis: rubric-gap | skill-gap

Round 2+: list any regression (passed last round, fails now).

--- PHASE 4: PROPOSE ---

For each excellence pattern, propose a rubric criterion with all five fields:
  ID:             C-[NN]
  Text:           [criterion text]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence]

State: "Awaiting approval to add C-[NN] to rubric."
On approval: update rubric file, increment version, state new path.

CONVERGENCE GATES

GATE 1 -- TRIAL CONVERGENCE
  Essential criteria failing this round: [list C-NN IDs, or "none"]
  Variations failing at least one essential: [list V-NN IDs, or "none"]
  GATE 1 RESULT: TRIAL CONVERGED | TRIAL NOT CONVERGED

GATE 2 -- QUEST PLATEAU
  This round (Round [N]) new patterns: [count and names, or "none"]
  Previous round (Round [N-1]) new patterns: [count and names, or "N/A -- first round"]
  GATE 2 RESULT: QUEST PLATEAUED -- Round [N-1] and Round [N] both found zero new patterns |
                 QUEST NOT PLATEAUED -- [which round found a new pattern and what it was]

Dual convergence = Gate 1 CONVERGED AND Gate 2 PLATEAUED.
If only Gate 1: run another round.
If only Gate 2: run another round.

GOLDEN OUTPUT (dual convergence only)

  1. Select the highest-composite variation from this round.
  2. Write its full prompt body verbatim to:
       simulations/quest/golden/{skill}-golden-{date}.md
     Frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN
     Body: the complete runnable prompt. Not a summary.
  3. Write the accumulated rubric to:
       simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md
     Include all criteria across all rounds.
  Confirm both files written. State paths.
```

---

## V-03

**Variation axis**: Compact plateau gate -- lifecycle on brevity, no round-naming template
in the convergence gate language
**Hypothesis**: Fails C-08. The compact Gate 2 instruction ("State PLATEAUED or NOT")
directs the operator to declare the result without instructing them to name both rounds.
All other 12 criteria pass -- notably C-11/C-12/C-13 all pass because the causal statement
is in Step 1. This isolates C-08 as a single-criterion failure, not a compound weakness.
**Champion relation**: structural alternative -- tests how much gate verbosity is required
for C-08 compliance vs. how compact convergence language can be

```
You are running quest-golden for {skill}.

LOAD INPUTS

Load the skill spec (signal.skills.yaml description field or spec file) and the current
rubric (simulations/quest/rubrics/{skill}-rubric-*.md latest version). If no rubric
exists, write a v1 with at least one essential criterion before continuing.

FOR EACH ROUND:

STEP 1 -- GENERATE VARIATIONS

Write 5 complete, runnable prompt bodies labeled V-01 through V-05. Each is a full text
-- not a diff. Include label, axis (design dimension tested), and hypothesis (predicted
effect vs. a generic approach).

Round 1: single-axis only.
Round 2+: combine axes that produced signal in earlier rounds.

Spread-design rule: rounds where all variations produce identical composite scores
generate no new excellence patterns and do not advance plateau detection. Design
variations to diverge on at least one criterion.

STEP 2 -- SCORE

Score every variation against every rubric criterion. Produce a score matrix with
one row per criterion (ID, short text, weight) and one column per variation, plus
COMPOSITE and RANK rows. Use PASS | PARTIAL | FAIL. Add one evidence note for
every FAIL or PARTIAL:
  [V-NN / C-NN]: [specific property absent or present]

STEP 3 -- PATTERNS

For each criterion with spread, name the structural property that caused the difference
as a reusable principle (not a variation name). Tag as skill-specific or transferable.
State the mechanism: the property present in passing variations, absent from failing.
List any criterion all variations fail (rubric-gap or skill-gap). In Round 2+, list
regressions. If no spread: state "No patterns this round."

STEP 4 -- PROPOSE

For each pattern, propose a rubric criterion with all five fields: ID, Text, Weight,
Category, Pass condition. Await approval before adding. On approval update the file.

CONVERGENCE

Gate 1: do all variations pass every essential criterion?
  State TRIAL CONVERGED or TRIAL NOT CONVERGED.

Gate 2: did Step 3 this round and Step 3 last round both find zero patterns?
  State QUEST PLATEAUED or QUEST NOT PLATEAUED.
  Both gates must be satisfied for dual convergence.

If only one gate satisfied: run another round. Do not declare golden.

ON DUAL CONVERGENCE

Write the highest-scoring variation's full prompt body (not a summary) to:
  simulations/quest/golden/{skill}-golden-{date}.md
with frontmatter (skill, target_skill, date, rounds, rubric, score, status: GOLDEN).
Write the accumulated rubric to:
  simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md
Confirm both files written. State paths.
```

---

## V-04

**Variation axes**: DO NOT gates + rubric-audit step (Step 0) + explicit dual mechanism
(both competitive and causal labeled) + pre-printed convergence slots with round-naming fields
**Hypothesis**: All 13 criteria pass. Combines the strongest structural elements from R1
and R2: V-05 (R1/R2) enforcement gates, V-02 (R2) rubric audit, and the explicit dual
spread-design labeling introduced in V-02 (R3). Maximum structural coverage of C-08
(pre-printed round-naming slots), C-11/C-13 (causal statement in Step 1), and C-12
(both competitive and causal mechanisms active and labeled).
**Champion relation**: beats champion on C-08 structural enforcement and C-12/C-13
completeness; tests whether rubric-audit as Step 0 adds value not captured by current criteria

```
You are running quest-golden for {skill}.

DO NOT proceed past any section until it is complete.

LOAD INPUTS

1. Load the skill spec from signal.skills.yaml (description field) or the spec file.
2. Load the current rubric from simulations/quest/rubrics/{skill}-rubric-*.md.
   If no rubric file exists: write a v1 rubric with at least one essential criterion.
   Write it to disk before continuing. State the path and version.

FOR EACH ROUND, EXECUTE STEPS 0-4 IN ORDER.

STEP 0 -- RUBRIC AUDIT

Before generating any variation, read every criterion in the current rubric and state:
  C-[NN]: [short criterion text]
  Divergence prediction: HIGH | MEDIUM | LOW
  Reason: [why some variation designs satisfy this and others don't]

List the top 2-3 criteria by divergence prediction. These are the spread-targets for
this round.

Current champion:
  Champion: [highest-scoring variation from last round, or "none -- Round 1"]
  Champion composite: [score, or "N/A"]
  Champion weak points: [criteria where champion scored FAIL, PARTIAL, or lowest among
                         passing variations; or "N/A -- Round 1"]

DO NOT proceed to Step 1 until rubric audit and champion assessment are complete.

STEP 1 -- GENERATE VARIATIONS

Generate 5 complete, runnable prompt bodies labeled V-01 through V-05.
Each is a full prompt body -- not a diff, not a summary.
Each must include: Label (V-NN), Axis, Hypothesis, Champion relation, Body.

Round 1: single-axis only.
Round 2+: combine axes that produced signal. Design rules:
  - At least two variations must target the spread-target criteria from Step 0.
  - At least one must match the champion approach (stability baseline).
  - At least one must try a structural approach the champion has not used.

Spread-design (BOTH mechanisms required; label each):

  a. Competitive mechanism: at least two variations must explicitly target the champion's
     weak-point criteria -- the criteria where the champion scored lowest.

  b. Causal mechanism: rounds where all variations produce identical composite scores
     generate no new excellence patterns and do not advance plateau detection. Design
     variations that will diverge on at least one criterion.

DO NOT proceed to Step 2 until all 5 variation bodies are written in full.

STEP 2 -- SCORE EACH VARIATION

For every variation, score every criterion in the current rubric.
Per criterion:
  Result: PASS | PARTIAL | FAIL
  Evidence: [quote the text that justifies the result or note the absent property]

After all criteria, compute composite using the rubric formula. Produce summary matrix:

| ID   | Criterion (short)       | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------------------|----|------|------|------|------|------|
| C-01 | [text]                  | E  |      |      |      |      |      |
...
| --   | COMPOSITE               |    |      |      |      |      |      |
| --   | RANK (1=best)           |    |      |      |      |      |      |

Evidence block for every FAIL or PARTIAL:
  [V-NN / C-NN]: [specific structural property absent or present]

DO NOT proceed to Step 3 until criterion-by-criterion scores are complete for all 5.

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion with score spread (at least one variation outperforms another):
  Pattern-[NN]:
    Name: [reusable design principle -- not variation name but the design choice]
    Scope: skill-specific | transferable
    Trigger: C-[NN] -- spread: [V-01=X, V-02=X, ...]
    Mechanism: [structural property in passing variations absent from failing ones]
    Champion delta: [does this change the leading candidate?]

Failure patterns (all fail a criterion):
  Criterion: [ID]
  Diagnosis: rubric-gap | skill-gap

Round 2+: list any regression (passed last round, fails now).

If all variations produce identical composite scores: state "No patterns this round.
Uniform scores confirm stability but do not advance plateau detection. Redesign
variations for divergence in the next round."

DO NOT proceed to Step 4 until all patterns are named and scoped.

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a rubric criterion. All five fields required.
Incomplete proposals will not be added.

  ID:             C-[NN]
  Text:           [what the criterion tests]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable -- a reviewer applying this reaches the same PASS/FAIL]

State the proposal. Await approval. On approval: update rubric file on disk, increment
version, state new path.

CONVERGENCE -- EVALUATE BOTH GATES INDEPENDENTLY

Fill in both slots before taking any action.

GATE 1 -- TRIAL CONVERGENCE
  Essential criteria failing this round: [list C-NN IDs, or "none"]
  Variations failing at least one essential: [list V-NN IDs, or "none"]
  GATE 1 RESULT: [ TRIAL CONVERGED | TRIAL NOT CONVERGED ]

GATE 2 -- QUEST PLATEAU
  This round (Round [N]) new patterns: [count and names, or "none"]
  Previous round (Round [N-1]) new patterns: [count and names, or "N/A -- first round"]
  GATE 2 RESULT: [ QUEST PLATEAUED -- Round [N-1] and Round [N] both found zero new
                   patterns | QUEST NOT PLATEAUED -- [round and pattern names] ]

DUAL CONVERGENCE:
  Gate 1: [ CONVERGED | NOT CONVERGED ]
  Gate 2: [ PLATEAUED | NOT PLATEAUED ]
  Action: [ WRITE GOLDEN | RUN ANOTHER ROUND ]

DO NOT declare golden unless both gates show CONVERGED + PLATEAUED.
If only Gate 1 satisfied: run another round.
If only Gate 2 satisfied: run another round.

WRITE GOLDEN ARTIFACTS (execute only when Action = WRITE GOLDEN)

  1. Identify the highest-composite variation from this round.

  2. Write its full prompt body verbatim to:
       simulations/quest/golden/{skill}-golden-{date}.md
     Frontmatter (YAML): skill, target_skill, date, rounds, rubric, score, status: GOLDEN
     Body: the complete, runnable prompt text. Not a summary. Not a pointer.

  3. Write the accumulated final rubric to:
       simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md
     Include all criteria added across all rounds.

DO NOT write only a summary of the prompt. Write the complete prompt body.
DO NOT declare this task complete until both files are written to disk and paths stated.
Confirm both files written. State paths.
```

---

## V-05

**Variation axis**: Stability baseline -- R2-V-05 verbatim
**Hypothesis**: R2-V-05 scores 100 under rubric v3. The spread-design rule in Step 1
("rounds in which all variations produce identical composite scores generate no new
excellence patterns and do not advance plateau detection") satisfies C-11 and C-13
(causal statement present). The divergence instruction ("Design variations that are
structurally distinct enough to diverge on at least one criterion") satisfies C-12
(mechanism a: explicit instruction to diverge). DO NOT gates satisfy C-03. Round-naming
instruction in Gate 2 ("Name both rounds explicitly") satisfies C-08.
**Champion relation**: matches champion approach -- stability check under v3

```
You are running quest-golden for {skill}.

DO NOT proceed past any section until the section is complete.

LOAD INPUTS

1. Load the skill spec from signal.skills.yaml (description field) or the spec file.
2. Load the current rubric from simulations/quest/rubrics/{skill}-rubric-*.md.
   If no rubric file exists: write a v1 rubric with at least one essential criterion.
   Write it to disk before continuing. State the path and version.

FOR EACH ROUND, EXECUTE STEPS 1-4 IN ORDER.

STEP 1 -- GENERATE VARIATIONS

Generate 5 complete, runnable prompt bodies labeled V-01 through V-05.
Each variation must be a full prompt -- not a diff, not a summary.
Each must include:
  - Label: V-NN
  - Axis: [the single design dimension this variation tests]
  - Hypothesis: [what this axis is predicted to change relative to a generic approach]

Round 1: each variation must vary only one axis.
Round 2+: combine axes that produced signal in earlier rounds.

Spread-design rule: rounds in which all variations produce identical composite scores
generate no new excellence patterns and do not advance plateau detection. Design
variations that are structurally distinct enough to diverge on at least one criterion.

DO NOT proceed to Step 2 until all 5 variation bodies are written in full.

STEP 2 -- SCORE EACH VARIATION

For every variation, score every criterion in the current rubric.
You must produce a criterion-by-criterion breakdown -- not just a composite.
For every criterion in the rubric, write:
  Result: PASS | PARTIAL | FAIL
  Evidence: [quote the specific variation text that justifies the result, or note the
             absent property]

After all criteria, compute and state the composite score using the rubric formula.
Produce a summary score matrix after scoring all variations:

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| C-01      | E  |      |      |      |      |      |
...
| COMPOSITE |    |      |      |      |      |      |
| RANK      |    |      |      |      |      |      |

DO NOT proceed to Step 3 until you have criterion-by-criterion scores for all 5 variations.

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

Look at the score spread across all variations.
For every criterion where at least one variation scores higher than another:
  1. Name the structural property that caused the difference.
     Write it as a reusable principle -- not "V-03 passed" but the design choice V-03
     made that others did not, as a property a future skill designer could apply.
  2. Tag its scope: skill-specific | transferable
  3. State the mechanism: the specific prompt property present in passing variations
     and absent from failing ones.

List any criterion all variations fail:
  Diagnosis: rubric-gap (criterion unclear or unachievable) | skill-gap (skill design
  does not produce this behavior)

In Round 2+: list any variation that passed a criterion last round but fails now.

If no variation outperforms any other on any criterion, state:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
  detection. Redesign variations for divergence in the next round."

DO NOT proceed to Step 4 until all patterns are named and scoped.

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each excellence pattern from Step 3, propose a new rubric criterion.
Every criterion proposal must include all five fields:
  ID:             C-[NN]
  Text:           [criterion description, one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one sentence, auditable -- a reviewer can determine PASS or FAIL
                  without ambiguity]

State each proposal explicitly. Wait for approval before adding to the rubric.
On approval: update the rubric file on disk, increment the version number, state path.

CONVERGENCE -- CHECK BOTH GATES INDEPENDENTLY

GATE 1 (TRIAL): Do all variations in this round pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED
  If NOT CONVERGED: list which variations failed which essential criteria.

GATE 2 (PLATEAU): Did Step 3 in this round AND Step 3 in the immediately preceding
  round both find zero new excellence patterns?
  Name both rounds explicitly (e.g., "Round 3 and Round 4: no new patterns found").
  State: QUEST PLATEAUED (Round X and Round Y: no new patterns) or QUEST NOT PLATEAUED

DO NOT declare golden unless both gates are satisfied simultaneously.
If only Gate 1 is satisfied: run another round.
If only Gate 2 is satisfied: run another round.

WRITE GOLDEN ARTIFACTS (on dual convergence only)

1. Select the highest-composite-scoring variation from this round.
2. Write it verbatim -- the full prompt body -- to:
     simulations/quest/golden/{skill}-golden-{date}.md
   Frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN
   Body: the complete, runnable prompt text.
3. Write the final accumulated rubric (all criteria across all rounds) to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md

DO NOT write only a summary of the prompt. Write the complete prompt body.
DO NOT declare this task complete until both files are written to disk and paths stated.
```

---

## R3 Design Notes

**R3 research question**: Do any of the three co-champion variations (V-02, V-04, V-05 R2)
have structural weaknesses not yet exposed by the v2 rubric? Under v3 (adding C-12 and C-13),
do they still all score 100?

**Designed divergence under rubric v3 (13 criteria):**

- V-01: Tests the C-11/C-13 boundary. Competitive framing satisfies C-12 (mechanism b) but
  not C-11 or C-13. Confirms R2-P2 as a structural property of v3. Expected: 96.

- V-03: Tests C-08 isolation. Compact gate without round-naming template fails C-08 (R),
  even when all 5 aspirational criteria (C-09 through C-13) pass. Expected: 90.

- V-02, V-04, V-05: All should score 100, confirming the three R2 co-champions are robust
  under v3 and that v3's new criteria (C-12, C-13) add no new separation among them.

**If R3 produces zero new excellence patterns** (expected): Quest enters its first zero-pattern
round. For plateau detection: R2 produced 2 new patterns; R3 produces 0. Plateau requires
TWO consecutive zero-pattern rounds. Action after R3: RUN ANOTHER ROUND (need R4 also zero).

**Score spread summary:**

| Variation | C-08 | C-11 | C-12 | C-13 | Composite |
|-----------|------|------|------|------|-----------|
| V-01 | PASS | FAIL | PASS | FAIL | 96 |
| V-02 | PASS | PASS | PASS | PASS | 100 |
| V-03 | FAIL | PASS | PASS | PASS | 90 |
| V-04 | PASS | PASS | PASS | PASS | 100 |
| V-05 | PASS | PASS | PASS | PASS | 100 |
