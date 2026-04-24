Written to `simulations/quest/variations/quest-golden-variations-R4-2026-03-14.md`.

---

## R4 Variations — quest-golden

**Research question**: Do any structural differences among the three R3 co-champions (V-02, V-04, V-05) produce criterion-captured improvement not yet in v3? Or does R4 confirm plateau?

| ID | Axis | Hypothesis | Expected |
|----|------|-----------|---------|
| **V-01** | Stability baseline — R3-V-05 verbatim (minimal structure) | Scores 100. Minimal champion stable. | 100 |
| **V-02** | Stability baseline — R3-V-02 verbatim (PHASE headers + explicit a/b dual-mechanism labels) | Scores 100. Dual-mechanism champion stable. | 100 |
| **V-03** | V-04 with Step 0 rubric-audit **ablated** (steps renumbered 1–4) | Scores 100 same as V-04. If equal, Step 0 is not criterion-captured under v3 → no new pattern. | 100 |
| **V-04** | Stability baseline — R3-V-04 verbatim (Step 0 + full structure) | Scores 100. Comparison point for V-03 ablation. | 100 |
| **V-05** | Novel probe — explicit **round-state header block** per round (round#, champion, cumulative pattern count, Gate trajectory) | Scores 100. Tests whether state tracking exposes any rubric gap. | 100 |

---

**Designed spread**: None expected — all five should score 100. This is a confirmation round. The key structural probes are:

- **V-03 vs V-04** (ablation): isolates whether Step 0 rubric-audit produces any criterion separation. If both score 100, Step 0 is structurally neutral under v3.
- **V-05** (novelty): tests whether explicit round-state tracking exposes a blind spot in v3. If it scores 100, v3 has no gap on meta-loop state management.

**Convergence projection**: If R4 yields 0 new patterns (expected), Gate 2 is PLATEAUED (R3 + R4 both zero). Gate 1 already CONVERGED. → Dual convergence → write golden.

**Golden candidate**: V-01 (R3-V-05) — minimal structure, all 13 criteria met, fewest operator constraints. V-04 adds Step 0 work not required by any criterion. V-02 adds PHASE headers without criterion benefit.
ed spread analysis**: No spread expected — all five should score 100. This is the confirmation round. If any variation fails a criterion, a new pattern exists and v3 is incomplete. If all pass, the rubric is saturated.

**Convergence projection after R4**:
- GATE 1 (TRIAL): Expected CONVERGED (all 5 pass essential)
- GATE 2 (PLATEAU): Expected PLATEAUED — R3: 0 new patterns; R4: 0 new patterns. Two consecutive zero-pattern rounds.
- Action (if expected): **WRITE GOLDEN**

---

## V-01

**Variation axis**: Stability baseline — R3-V-05 verbatim (minimal structure, DO NOT gates, single causal statement)
**Hypothesis**: Scores 100 under v3. The minimal structure passes all 13 criteria: DO NOT gates cover C-03, causal statement in Step 1 covers C-11/C-13, divergence instruction covers C-12, round-naming template in Gate 2 covers C-08. Baseline for structural comparison with ablation and novel probes.
**Champion relation**: matches champion approach — stability check for R4

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

## V-02

**Variation axis**: Stability baseline — R3-V-02 verbatim (PHASE headers + explicitly labeled dual-mechanism spread design)
**Hypothesis**: Scores 100 under v3. The explicit a/b mechanism labeling ("a. Competitive mechanism" and "b. Causal mechanism") passes C-12 via both mechanism routes and C-13 via the causal statement. PHASE headers do not affect any criterion. Score expected equal to V-01 and V-04 — no differentiation from dual-mechanism labeling alone.
**Champion relation**: matches champion approach — stability check for R4

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

**Variation axis**: R3-V-04 with Step 0 rubric-audit ablated — steps renumbered 1–4
**Hypothesis**: Scores 100 under v3 — same composite as V-04. If identical score, Step 0 is not captured by any v3 criterion: rubric-audit does not produce measurable criterion improvement under the current rubric. No new pattern from ablation. This is the isolation test: V-03 (V-04 minus Step 0) vs V-04 (full structure) should produce zero criterion separation.
**Champion relation**: structural alternative — ablated version of V-04 champion; tests whether Step 0 produces any criterion-captured contribution

```
You are running quest-golden for {skill}.

DO NOT proceed past any section until it is complete.

LOAD INPUTS

1. Load the skill spec from signal.skills.yaml (description field) or the spec file.
2. Load the current rubric from simulations/quest/rubrics/{skill}-rubric-*.md.
   If no rubric file exists: write a v1 rubric with at least one essential criterion.
   Write it to disk before continuing. State the path and version.

FOR EACH ROUND, EXECUTE STEPS 1-4 IN ORDER.

State at the start of every round:
  Champion: [highest-scoring variation from last round, or "none -- Round 1"]
  Champion composite: [score, or "N/A"]
  Champion weak points: [criteria where champion scored FAIL, PARTIAL, or lowest among
                         passing variations; or "N/A -- Round 1"]

STEP 1 -- GENERATE VARIATIONS

Generate 5 complete, runnable prompt bodies labeled V-01 through V-05.
Each is a full prompt body -- not a diff, not a summary.
Each must include: Label (V-NN), Axis, Hypothesis, Champion relation, Body.

Round 1: single-axis only.
Round 2+: combine axes that produced signal. Design rules:
  - At least two variations must target the champion's weak-point criteria.
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

## V-04

**Variation axis**: Stability baseline — R3-V-04 verbatim (Step 0 rubric-audit + DO NOT gates + pre-printed dual-convergence slots + labeled dual mechanism)
**Hypothesis**: Scores 100 under v3. Maximum-structure champion remains stable. Comparison point for V-03 ablation — if V-03 and V-04 score identically, Step 0 is structurally neutral under v3 and produces no new pattern.
**Champion relation**: matches champion approach — stability check for R4

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

**Variation axis**: Novel probe — explicit round-state header block at the start of each round (round number, current champion name+score, cumulative pattern count, convergence trajectory)
**Hypothesis**: Scores 100 under v3. Round-state tracking is an organizational structural property — it improves operator orientation but does not affect any of the 13 criterion behaviors. Expected: same 100 score as V-01/V-02/V-04. If so, round-state tracking is not a criterion gap and no new pattern is yielded. This is the structural novelty probe: tests whether v3 has any blind spots on meta-loop state management.
**Champion relation**: structural alternative — novel property not tried in any prior round; tests whether state tracking exposes a rubric gap

```
You are running quest-golden for {skill}.

DO NOT proceed past any section until the section is complete.

LOAD INPUTS

1. Load the skill spec from signal.skills.yaml (description field) or the spec file.
2. Load the current rubric from simulations/quest/rubrics/{skill}-rubric-*.md.
   If no rubric file exists: write a v1 rubric with at least one essential criterion.
   Write it to disk before continuing. State the path and version.

FOR EACH ROUND, EXECUTE STEPS 1-4 IN ORDER.

ROUND STATE (fill in before Step 1)

  Round: [N]
  Champion: [highest-scoring variation from last round, or "none -- Round 1"]
  Champion composite: [score, or "N/A"]
  Patterns found to date: [cumulative count across all prior rounds]
  Consecutive zero-pattern rounds: [count; 0 if last round had any new patterns]
  Gate 1 status from last round: [CONVERGED | NOT CONVERGED | N/A -- Round 1]
  Gate 2 trajectory: [N rounds needed; M consecutive zero-pattern rounds so far]

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

## R4 Design Notes

**Single-axis design (for reference)**:

| Axis | R1 | R2 | R3 | R4 |
|------|----|----|----|-----|
| DO NOT enforcement gates | V-05 | V-05 (repaired) | V-04, V-05 | V-01, V-03, V-04 (carry-forward) |
| Competitive/inertia framing only | -- | V-01 | V-01 (confirm) | -- |
| Rubric-first role sequence | -- | V-02 | V-04 (combined) | -- |
| Compact lifecycle / gate | -- | V-03 | V-03 (gate variant) | -- |
| Dual-mechanism (competitive + causal) | -- | -- | V-02 (new) | V-02 (stability) |
| Rubric-audit + DO NOT + dual mechanism | -- | -- | V-04 (new combination) | V-04 (stability) |
| Rubric-audit ablation | -- | -- | -- | V-03 (new) |
| Round-state header | -- | -- | -- | V-05 (new) |

**R4 ablation logic (V-03 vs V-04)**:

Both V-03 and V-04 have:
- DO NOT gates
- Labeled dual spread-design (a/b)
- Pre-printed convergence slots with Gate 1/Gate 2/Action fields
- Champion state at round start
- All 13 v3 criteria satisfied

V-04 additionally has: Step 0 rubric-audit with per-criterion divergence prediction.

If V-03 = V-04 = 100: Step 0 adds no v3-criterion-captured value. No C-14 from Step 0.
If V-03 < V-04: Step 0 exposes a criterion gap → C-14 proposed → rubric v4 → R5 needed.

**R4 novelty logic (V-05)**:

V-05 adds ROUND STATE block (round#, champion+score, cumulative pattern count, consecutive zero-pattern count, Gate 1 status, Gate 2 trajectory). This tracks convergence state explicitly. All 13 v3 criteria are still satisfied by the underlying structure.

If V-05 = 100 (same as V-01): round-state tracking is not a criterion gap. No C-14 from state tracking.
If V-05 < 100: the state-tracking block introduced a structural violation → new pattern.

**Expected R4 finding**: All 5 score 100. Zero new patterns. Combined with R3 (zero patterns), Gate 2 is PLATEAUED. Gate 1 CONVERGED. Dual convergence achieved. Write golden.

**Golden candidate**: All three stability baselines (V-01, V-02, V-04) are equivalent under v3. Tiebreak: V-05 (R3) = V-01 here — minimal structure, all criteria met, fewest constraints for operators. V-04 (Step 0) adds operator work not required by any criterion. V-02 adds PHASE header style. Recommendation pending R4 scoring: V-01 (V-05 from R3) as golden — minimal, robust, fully passing.
