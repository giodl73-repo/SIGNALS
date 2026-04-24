Variations written to `simulations/quest/variations/quest-golden-variations-R2-2026-03-14.md`.

---

## R2 Summary

Five complete variations generated. Key design choices:

**Single-axis (3):**
- **V-01 — Inertia framing**: Champion named at round start; new variations must explicitly beat it on specific criteria. No C-11 language — tests whether adversarial pressure alone drives spread without the causal explanation from R1 E-1.
- **V-02 — Rubric-first**: Adds a Step 0 rubric audit before generation. Operator predicts which criteria will diverge, then designs variations to stress-test those targets. Includes spread rationale + C-11 language.
- **V-03 — Compact/dense**: All four phases, score matrix, and both gates expressed in ~200 words of dense prose. No RANK row, no structural headers, no C-11 language. The null hypothesis: elaborate formatting is decorative.

**Combination (2):**
- **V-04 — Pre-printed slots + inertia framing**: V-05 R1 fill-in-blank gate slots (hardest C-03 enforcement) combined with champion-defense framing (spread pressure). Both C-11 and C-09 covered.
- **V-05 — Imperative + spread rationale (V-03 R1 repaired)**: R1 V-03 verbatim plus one spread-design rule at Step 1 and one all-pass warning at Step 3. Minimal surgery; tests whether a single sentence is sufficient to repair both C-09 and C-11 in an imperative-register prompt.

**Expected spread**: V-01 (~97) and V-03 (~90-97) fail C-11; V-03 may also fail C-09. V-02/V-04/V-05 should score 100. This gives score separation that satisfies C-09 and produces at least one new excellence pattern for R2.

**Key R2 question**: Does inertia framing (V-01) produce C-09 spread without C-11 language? If yes, E-1 scope narrows. If no, competitive framing and causal explanation are non-substitutes.
bric with at least one essential criterion. Write
  it to disk before proceeding.

CURRENT CHAMPION
  At the start of each round, identify the champion: the highest-scoring variation from
  the previous round. If this is Round 1, the champion is "none."
  State:
    Champion: [variation name, or "none (Round 1)"]
    Champion score: [composite, or "N/A"]
    Champion weaknesses: [criteria where champion scored FAIL or PARTIAL, or criteria
                          where champion scored lower than at least one other variation]

PER-ROUND EXECUTION

--- PHASE 1: GENERATE ---

Generate 5 complete, runnable skill body prompt variations labeled V-01 through V-05.
Each variation is a full prompt body -- not a diff, not a summary of changes.

For each variation provide:
  V-NN
  Axis: [the design dimension this variation tests]
  Hypothesis: [predicted effect on scoring vs. the current champion]
  Champion relation: [beats champion on: C-NN | ties champion | matches champion approach]
  Body: [full prompt text]

Round 1: single-axis only.
Round 2+: combine axes that produced signal. At least two variations must directly target
one of the champion's weaknesses. At least one variation must match the champion approach
(as a stability baseline). At least one variation must try a structural approach the
champion has not used.

--- PHASE 2: SCORE ---

Score every variation against every criterion in the current rubric.

Score matrix:

| Criterion            | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------------|----|------|------|------|------|------|
| C-01: [short text]   | E  |      |      |      |      |      |
| C-02: ...            | E  |      |      |      |      |      |
...
| COMPOSITE            |    |      |      |      |      |      |
| RANK (1=best)        |    |      |      |      |      |      |

Wt: E=essential, R=recommended, A=aspirational.
Results: PASS | PARTIAL | FAIL only.

For every FAIL or PARTIAL, add an evidence note below the matrix:
  [V-NN / C-NN]: [the specific property absent or present that drove this result]

--- PHASE 3: IDENTIFY ---

Examine the score matrix for criteria where at least one variation outperforms another.

For each signal:
  Pattern: [name the structural property that caused the difference as a reusable
            principle -- not "V-03 won" but the design choice V-03 made that others did not]
  Scope: skill-specific | transferable
  Evidence: [criterion, score spread, champion delta]

If no variation outperforms any other on any criterion: state "No score spread this round.
No patterns extracted."

Failure patterns: list any criterion where all variations FAIL.
  Diagnosis: rubric-gap | skill-gap

Regression signals (Round 2+): list any variation that passed a criterion last round but
fails now.

--- PHASE 4: PROPOSE ---

For each excellence pattern from Phase 3, propose a rubric criterion:
  ID:             C-[NN]
  Text:           [criterion text]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence -- a reviewer can determine PASS or FAIL]

State: "Awaiting approval to add C-[NN] to rubric."
On approval: write the updated rubric to disk and state the new version path.

CONVERGENCE GATES

GATE 1 -- TRIAL CONVERGENCE
  Do all variations in this round pass every essential criterion?
  State: TRIAL CONVERGED | TRIAL NOT CONVERGED

GATE 2 -- QUEST PLATEAU
  Did Phase 3 of this round AND Phase 3 of the immediately preceding round both produce
  zero new patterns? Name both rounds explicitly.
  State: QUEST PLATEAUED (Round X and Round Y: no new patterns) | QUEST NOT PLATEAUED

Dual convergence requires both gates satisfied. If only Gate 1: run another round. If
only Gate 2: run another round.

GOLDEN OUTPUT (dual convergence only)

  1. Select the highest-composite variation from this round.
  2. Write its full prompt body verbatim to:
       simulations/quest/golden/{skill}-golden-{date}.md
     Frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN
     Body: the complete, runnable prompt text. Not a summary. Not a pointer.
  3. Write the accumulated final rubric to:
       simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md
     Include all criteria from all rounds.
  Confirm both files written. State paths.
```

---

## V-02

**Variation axis**: Rubric-first role sequence
**Hypothesis**: Reading the rubric criteria and predicting which will diverge across variations before generating any variation produces more targeted spread than generating first and extracting patterns after. The generation step becomes a response to the rubric audit rather than a blank-slate exercise.

```
You are running quest-golden for {skill}.

LOAD INPUTS
  Skill spec: signal.skills.yaml (description field) or simulations/draft/specs/
  Rubric: simulations/quest/rubrics/{skill}-rubric-*.md (latest version)
  If no rubric exists: write a v1 rubric with at least one essential criterion before
  continuing. Record the rubric version at the start of each round.

PER-ROUND EXECUTION

--- STEP 0: RUBRIC AUDIT ---

Before generating any variation, read every rubric criterion and answer:

  For each criterion:
    C-[NN]: [short criterion text]
    Divergence prediction: HIGH | MEDIUM | LOW
    Reason: [why some variation designs satisfy this and others do not]

List the top 2-3 criteria by divergence prediction. These are the stress-test targets
for variation generation this round.

--- STEP 1: GENERATE VARIATIONS ---

Generate 5 complete, runnable skill body prompt variations (V-01 through V-05).
Each is a full prompt body -- not a diff.

Per variation:
  V-NN
  Axis: [the design dimension this variation tests]
  Hypothesis: [which stress-test target from Step 0 this variation is designed to
               satisfy or fail, and why]
  Body: [full prompt text]

Design rule: at least 3 variations must be specifically designed to diverge on the
Step 0 stress-test targets. At least one variation must represent a minimal/baseline
approach (to expose what's strictly required vs. what's incidental).

Rounds where all variations converge to the same composite score produce no new
excellence patterns and do not advance plateau detection -- design for divergence.

--- STEP 2: SCORE EACH VARIATION ---

Score every variation against every criterion in the current rubric.

Score matrix:

| ID   | Criterion (short)       | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------------------|----|------|------|------|------|------|
| C-01 | [text]                  | E  |      |      |      |      |      |
| C-02 | [text]                  | E  |      |      |      |      |      |
...
| --   | COMPOSITE               |    |      |      |      |      |      |
| --   | RANK (1=highest)        |    |      |      |      |      |      |

Results: PASS | PARTIAL | FAIL only.
For every FAIL or PARTIAL, write one evidence note immediately below the matrix:
  [V-NN / C-NN]: [the specific property absent or present]

--- STEP 3: IDENTIFY EXCELLENCE PATTERNS ---

Review the score matrix for criteria with score spread.

For each diverging criterion:
  Pattern: [the structural design principle that caused the difference -- not the
            variation name but the reusable property]
  Scope: skill-specific | transferable
  Trigger: C-[NN] -- spread: [V-01=X, V-02=X, ...]
  Mechanism: [the specific thing passing variations do that failing ones omit]

Review divergence predictions from Step 0: were they accurate? Note any surprises.

Failure patterns: criteria no variation passes.
  Criterion: [ID]
  Diagnosis: rubric-gap | skill-gap

Regression signals (Round 2+): criteria a variation passed last round but fails now.

--- STEP 4: PROPOSE RUBRIC CRITERIA ---

For each excellence pattern, propose a rubric criterion with all five fields:
  ID:             C-[NN]
  Text:           [criterion text]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [precise auditable condition -- a reviewer can apply it unambiguously]

State: "Awaiting approval to add C-[NN] to rubric."
On approval: update the rubric file on disk and state the new version path.

CONVERGENCE GATES

GATE 1 -- TRIAL CONVERGENCE
  Predicate: all variations pass every essential criterion.
  Essential criteria failing this round: [list, or "none"]
  Variations failing at least one essential: [list, or "none"]
  GATE 1 RESULT: TRIAL CONVERGED | TRIAL NOT CONVERGED

GATE 2 -- QUEST PLATEAU
  Predicate: Step 3 of this round and Step 3 of the previous round both produced zero
  new excellence patterns.
  This round new patterns: [count and names, or "none"]
  Previous round new patterns: [count and names, or "N/A -- first round"]
  GATE 2 RESULT: QUEST PLATEAUED -- Round [N-1] and Round [N] both zero | NOT PLATEAUED

Dual convergence = Gate 1 CONVERGED AND Gate 2 PLATEAUED. Both required simultaneously.
Declaring golden on Gate 1 alone is a hard stop.

GOLDEN OUTPUT (on dual convergence only)

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

**Variation axis**: Compact/dense lifecycle (minimal structural overhead)
**Hypothesis**: A prompt that states all four phases, the score matrix, and both convergence gates in dense prose with no elaborate section formatting achieves identical convergence behavior to phased approaches at substantially lower token cost. The structural overhead in V-04 and V-05 R1 is decorative, not functional.

```
You are running quest-golden for {skill}.

Load: skill spec from signal.skills.yaml or specs file; rubric from
simulations/quest/rubrics/{skill}-rubric-*.md. If no rubric exists, write a v1 rubric
with at least one essential criterion before starting.

Each round runs four steps in order.

Step 1 -- Generate. Write 5 complete, runnable skill body prompts (V-01 to V-05). Each
is a full prompt text with a label, axis (the design dimension it tests), and a one-line
hypothesis. Round 1: single-axis only. Round 2+: combine axes that produced signal.

Step 2 -- Score. Score every variation against every rubric criterion. Produce a score
matrix with one row per criterion and one column per variation plus COMPOSITE and RANK
rows. Use PASS | PARTIAL | FAIL only. For every FAIL or PARTIAL write one evidence note.

Step 3 -- Extract. Find criteria where at least one variation outperforms another. For
each: name the structural property that drove the difference as a reusable principle
(not the variation name), and tag it as skill-specific or transferable. List any criterion
all variations fail (rubric-gap or skill-gap). In Round 2+, list any regression.

Step 4 -- Propose. For each excellence pattern, propose a rubric criterion with five
fields: ID, Text, Weight (essential | recommended | aspirational), Category (structure |
behavior | correctness | depth | coverage), Pass condition. Await approval before adding.
On approval update the rubric file and state the new path.

Convergence: after Step 4, check two independent gates.
  Gate 1 -- TRIAL: do all variations pass every essential criterion?
    State TRIAL CONVERGED or TRIAL NOT CONVERGED.
  Gate 2 -- PLATEAU: did Step 3 this round and Step 3 the previous round both find zero
    new patterns? Name both rounds. State QUEST PLATEAUED or QUEST NOT PLATEAUED.
  Both gates must be satisfied to declare golden. One gate is not enough.

On dual convergence: (1) write the highest-scoring variation verbatim to
simulations/quest/golden/{skill}-golden-{date}.md with frontmatter (skill, target_skill,
date, rounds, rubric, score, status: GOLDEN) and the full prompt body -- not a summary;
(2) write the accumulated rubric to simulations/quest/rubrics/{skill}-rubric-v{final}-
{date}.md including all criteria from all rounds. Confirm both paths written.
```

---

## V-04

**Variation axes**: Pre-printed convergence slots + inertia framing (combination)
**Hypothesis**: V-05 R1 proved that pre-printed fill-in-blank gate slots are the strongest enforcement mechanism for C-03. Adding champion-defense inertia framing to the generation phase amplifies spread incentive by making each variation compete against a named target, not a generic quality bar. The combination removes both premature-golden risk (via gate slots) and uniform-variation risk (via champion pressure).

```
You are running quest-golden for {skill}.

Load inputs before starting:
  Skill spec: signal.skills.yaml or simulations/draft/specs/
  Rubric: simulations/quest/rubrics/{skill}-rubric-*.md (latest version)
  If no rubric exists: write a v1 rubric now with at least one essential criterion.
  Record the rubric version and round number.

CURRENT CHAMPION
  State at the start of every round:
    Champion: [highest-scoring variation from last round, or "none -- Round 1"]
    Champion composite: [score, or "N/A"]
    Champion weak points: [criteria where champion scored FAIL, PARTIAL, or lowest
                           among passing variations; or "N/A -- Round 1"]

ROUND LOOP -- repeat until dual convergence.

---

### A. GENERATE VARIATIONS

Write 5 complete, runnable skill body prompts (V-01 through V-05).
Each must be a full prompt body -- not a diff, not a reference to another variation.

Per variation:
  V-NN
  Axis: [design dimension being tested]
  Hypothesis: [predicted effect relative to the current champion]
  Champion relation: [beats champion on C-NN | baseline -- matches champion approach |
                      structural alternative -- approach champion has not tried]
  Body:
  [full prompt text]

Round 1: single-axis only.
Round 2+: combine axes that showed spread. Design rules:
  - At least two variations target one of the champion's weak points.
  - At least one variation attempts a structural approach the champion has not used.
  - At least one variation matches the champion approach as a stability baseline.
  - Rounds where all variations produce identical composite scores generate no new
    excellence patterns and do not advance plateau detection. Design for divergence.

---

### B. SCORE MATRIX

Produce one score matrix per round. Every criterion. Every variation.

| ID   | Criterion (short)       | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------------------|----|------|------|------|------|------|
| C-01 | [text]                  | E  |      |      |      |      |      |
| C-02 | [text]                  | E  |      |      |      |      |      |
...
| --   | COMPOSITE               |    |      |      |      |      |      |
| --   | RANK (1=best)           |    |      |      |      |      |      |

Results: PASS | PARTIAL | FAIL only.
Evidence block for every FAIL or PARTIAL:
  [V-NN / C-NN]: [specific structural property absent or present]

---

### C. EXCELLENCE PATTERNS

Review the score matrix. For each criterion with spread (at least one variation
outperforms another):

  Pattern-[NN]:
    Name:      [a reusable design principle -- stated as a rule, not a variation name]
    Scope:     skill-specific | transferable
    Trigger:   C-[NN] -- spread: [scores by variation]
    Mechanism: [the structural property in passing variations absent from failing ones]
    Champion delta: [does this change the leading candidate?]

If all variations produce identical composite scores: state "No new patterns this round.
Uniform scores confirm stability but do not advance plateau detection -- design variations
for divergence in the next round."

Failure patterns (all variations fail a criterion):
  Criterion: [ID]
  Diagnosis: rubric-gap | skill-gap

Regression signals (Round 2+): criteria a variation passed last round but fails now.

---

### D. PROPOSED CRITERIA

For each pattern from C, propose a rubric criterion. All five fields required -- incomplete
proposals will not be added.

  ID:             C-[NN]
  Text:           [what the criterion tests]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable -- a reviewer applying this reaches the same PASS/FAIL]

State the proposal. Await approval. On approval: update the rubric file on disk, increment
the version number, state the new path.

---

### E. CONVERGENCE GATES

Complete both fill-in slots before taking any action.

GATE 1 -- TRIAL CONVERGENCE
  Essential criteria failing this round: [list C-NN IDs, or "none"]
  Variations failing at least one essential: [list V-NN IDs, or "none"]
  GATE 1 RESULT: [ TRIAL CONVERGED | TRIAL NOT CONVERGED ]

GATE 2 -- QUEST PLATEAU
  This round (Round [N]) new patterns: [count and names, or "none"]
  Previous round (Round [N-1]) new patterns: [count and names, or "N/A -- first round"]
  GATE 2 RESULT: [ QUEST PLATEAUED -- Round [N-1] and Round [N] both found zero new
                   patterns | QUEST NOT PLATEAUED -- [which round found a new pattern] ]

DUAL CONVERGENCE:
  Gate 1: [ CONVERGED | NOT CONVERGED ]
  Gate 2: [ PLATEAUED | NOT PLATEAUED ]
  Action: [ WRITE GOLDEN -- proceed to F | RUN ANOTHER ROUND ]

If only Gate 1 is satisfied: run another round. Do not declare golden.
If only Gate 2 is satisfied: run another round. Do not declare golden.

---

### F. GOLDEN ARTIFACTS (execute only when E declares WRITE GOLDEN)

  1. Identify: highest-composite variation from this round.

  2. Write full prompt body verbatim to:
       simulations/quest/golden/{skill}-golden-{date}.md
     Frontmatter (YAML):
       skill: quest-golden
       target_skill: {skill}
       date: {date}
       rounds: {N}
       rubric: simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md
       score: {composite}
       status: GOLDEN
     Body: the complete prompt text. Not a summary. Not a pointer. The full text.

  3. Write accumulated final rubric to:
       simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md
     Include all criteria added across all rounds with current weight assignments.

  Confirm both files written. State paths.
```

---

## V-05

**Variation axes**: Phrasing register (imperative + hard stops) + spread-design rationale (R1 V-03 repaired)
**Hypothesis**: R1 V-03 scored 95/100, failing C-09 and (under the v2 rubric) C-11, because imperative DO NOT gates enforce completeness but give the model no reason to design variations that diverge. Adding one explicit sentence explaining why all-pass rounds stall plateau detection repairs both failures without changing the imperative register that makes V-03 strong on C-01/C-03/C-04.

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

## R2 Design Notes

**Expected score spread under rubric v2 (11 criteria, 3 aspirational):**

| Variation | C-09 | C-10 | C-11 | Expected composite |
|-----------|------|------|------|--------------------|
| V-01 | PASS (inertia drives spread) | PASS | FAIL (no explicit language) | ~97 |
| V-02 | PASS (rubric-audit drives spread) | PASS | PASS | 100 |
| V-03 | FAIL or PASS (compact, no spread-design) | PASS | FAIL (no explicit language) | ~90-97 |
| V-04 | PASS (champion-defense + spread warning) | PASS | PASS | 100 |
| V-05 | PASS (spread rule in Step 1) | PASS | PASS (Step 3 all-pass warning) | 100 |

**Designed divergence**: V-01 and V-03 are expected to fail C-11 (no explicit
uninformative-round explanation). V-03 may also fail C-09 (compact form, no spread-design
rationale, no RANK row). This gives R2 a spread of at least 3 points on the aspirational
band -- satisfying C-09 -- while keeping all essential criteria passing (TRIAL CONVERGED
in R1 holds).

**R2 novel test**: If inertia framing alone (V-01) passes C-09 without explicit C-11
language, it suggests competitive framing is a structurally sufficient substitute for
causal explanation. If it fails C-09, the E-1 finding from R1 generalizes: spread-design
requires either explanation or structural visibility, and competitive framing alone is
insufficient.

**Axis coverage across R1+R2:**

| Axis | R1 variation | R2 variation |
|------|-------------|-------------|
| Lifecycle emphasis (phase labels) | V-01 | -- |
| Output format (table-heavy) | V-02 | -- |
| Phrasing register (imperative) | V-03 | V-05 (repaired) |
| Lifecycle + tables (combination) | V-04 | -- |
| Pre-printed convergence slots | V-05 | V-04 (combined) |
| Inertia framing | -- | V-01 (new) |
| Rubric-first role sequence | -- | V-02 (new) |
| Compact/dense lifecycle | -- | V-03 (new) |
