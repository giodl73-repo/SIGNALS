Written to `simulations/quest/variations/quest-golden-variations-R1-2026-03-14.md`.

---

## R1 Variations — quest-golden

Five complete, runnable skill body prompts across three single-axis and two combination variations:

| ID | Axis | Hypothesis | Primary targets |
|----|------|-----------|----------------|
| **V-01** | Lifecycle emphasis | Explicit `PHASE 1/2/3/4` labels in every round prevent phase-skipping (QG-06) | C-01, C-03 |
| **V-02** | Output format (table-heavy) | Mandatory score matrix with one row per criterion per variation makes C-02 trivially auditable; eliminates QG-02 by construction | C-02, C-09 |
| **V-03** | Phrasing register (imperative + hard stops) | `DO NOT proceed to Step N until...` gates eliminate soft ambiguity about what is required vs. optional | C-01, C-03, C-04 |
| **V-04** | V-01 + V-02 combination | Outer phase labels (can't skip a phase) + inner score matrix (can't elide a criterion) — two independent structural guarantees | C-01, C-02, C-03 |
| **V-05** | V-02 + V-03 + pre-printed convergence slots | Gate blocks have pre-printed fill-in-the-blank slots for both conditions — the model must state "Essential criteria failing: ___, Variations failing: ___" before it can proceed | C-02, C-03, C-04, C-05 |

**Key design decision in V-05**: the convergence gates are printed as templates the model fills in, not instructions it follows. This targets the most common failure mode (QG-01 — declaring golden after trial convergence without checking plateau) by forcing the plateau evidence to be stated before the action decision appears.

**Expected score spread**: V-01 and V-03 likely split on C-02 (V-01 omits the matrix format; V-03 omits it too but uses hard stops). V-02 likely passes C-02 but may be weaker on C-03 (convergence gate separation). V-05 should score highest on C-03 due to the pre-printed gate structure.
posite. Every criterion must appear for every variation.
Compute the composite score per the rubric formula. Rank variations by composite.

--- PHASE 3: IDENTIFY ---
Look across all variation scores. Identify:
1. Excellence signals -- criteria where at least one variation clearly outperforms others.
   For each signal, state the structural property that caused the difference as a reusable
   principle (not which variation won). Tag each pattern:
   scope: skill-specific | transferable
2. Failure patterns -- criteria that no variation passes. Note whether this is a rubric gap
   or a skill design issue.
3. Regression signals (Round 2+) -- variations that passed a criterion in the previous
   round but fail now.

--- PHASE 4: PROPOSE ---
For each excellence signal identified in Phase 3, propose a new rubric criterion with all
five required fields:
  ID:             [next available C-NN]
  Text:           [one-sentence description of what the criterion tests]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [precise, auditable statement of what PASS looks like]

Ask for approval before adding the criterion to the rubric. On approval, write the updated
rubric to disk.

CONVERGENCE GATES

After each round, check both gates independently:

GATE 1 -- TRIAL CONVERGENCE
  All variations in this round: do all pass all essential criteria?
  State: TRIAL CONVERGED | TRIAL NOT CONVERGED

GATE 2 -- QUEST PLATEAU
  Have the last two consecutive rounds produced zero new excellence patterns in Phase 3?
  Name the rounds explicitly (e.g., "Round 3 and Round 4: no new patterns found").
  State: QUEST PLATEAUED | QUEST NOT PLATEAUED

Dual convergence requires BOTH gates to be CONVERGED/PLATEAUED simultaneously.
Declaring golden when only TRIAL CONVERGED is a hard stop -- continue to the next round.

GOLDEN PROMPT

When dual convergence is reached:
1. Select the highest-scoring variation from the final round.
2. Write it verbatim as the prompt body to:
   simulations/quest/golden/{skill}-golden-{date}.md

   Frontmatter fields: skill, target_skill, date, rounds, rubric, score, status: GOLDEN

3. Write the final rubric (all criteria accumulated across all rounds) to:
   simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md

Do not summarize the golden prompt. Write it in full.
```

---

## V-02

**Variation axis**: Output format (table-heavy scoring)
**Hypothesis**: Structuring the per-criterion score output as a mandatory matrix (one row
per criterion per variation) makes C-02 trivially auditable and forces score spread to be
visible at a glance -- eliminating QG-02 by construction. Targets C-02 and C-09.

```
You are running quest-golden for the skill named in the invocation.

INPUTS
- Skill spec: load from signal.skills.yaml or simulations/draft/specs/
- Rubric: load from simulations/quest/rubrics/{skill}-rubric-*.md (latest version)
  If no rubric exists, create a v1 rubric with at least one essential criterion now.

PER-ROUND OUTPUT FORMAT

Each round produces the following sections, in this order:

### Variations

Five complete, runnable skill body prompts labeled V-01 through V-05. Each labeled with:
  Axis: [variation axis name]
  Hypothesis: [one sentence predicting what this axis changes]

In Round 1: single-axis only. In later rounds: combine axes that showed signal.

### Score Matrix

One table covering all variations and all criteria. Format:

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| C-01      | E  | PASS | PASS | FAIL | PASS | PASS |
| C-02      | E  | ...  | ...  | ...  | ...  | ...  |
...
| Composite |    | 72   | 85   | 48   | 91   | 80   |

Wt legend: E=essential, R=recommended, A=aspirational
Results: PASS | PARTIAL | FAIL only. No other values.

Below the matrix, write one row per variation:
  V-NN: [composite score] -- [one-sentence rationale for rank]

### Excellence Signals

For each criterion where score spread exists (at least one FAIL or PARTIAL vs. at least
one PASS):
  - Pattern: [name the structural property as a reusable principle, not the winning variation]
  - Scope: skill-specific | transferable
  - Evidence: [which criterion, what scores diverged]

### Failure Patterns

List any criterion that no variation passes. For each:
  - Criterion: [ID and text]
  - Diagnosis: rubric-gap (criterion is unclear or unachievable) | skill-gap (skill design
    does not produce this output)

### Proposed Criteria

For each excellence signal, propose a rubric criterion with all five fields:

  ID:             [next C-NN]
  Text:           [criterion text]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [precise, auditable, one-sentence]

Await approval before adding to rubric.

### Convergence Check

TRIAL CONVERGENCE: [CONVERGED if all variations pass all essential criteria | NOT CONVERGED]
PLATEAU CHECK: [PLATEAUED if rounds RN-1 and RN both found zero new excellence signals |
                NOT PLATEAUED -- list which pattern was new in RN]

Both must read CONVERGED/PLATEAUED to declare golden. If only TRIAL CONVERGED: continue
to next round.

GOLDEN PROMPT OUTPUT

On dual convergence:
1. Write the highest-scoring variation verbatim to:
   simulations/quest/golden/{skill}-golden-{date}.md
   (Frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN)

2. Write accumulated rubric to:
   simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md

The prompt body in the golden artifact must be the complete, runnable prompt -- not a
summary or pointer. An artifact containing only metadata is a hard fail.
```

---

## V-03

**Variation axis**: Phrasing register (imperative with hard stops)
**Hypothesis**: Imperative "you will" phrasing with explicit "DO NOT proceed" gates at
phase boundaries eliminates soft ambiguity about what is required vs. optional, directly
addressing QG-01 (premature convergence declaration) and QG-06 (phase skipping).
Targets C-01, C-03, C-04.

```
You are running quest-golden for {skill}.

DO NOT proceed past any section until the section is complete.

LOAD INPUTS

1. Load the skill spec from signal.skills.yaml (description field) or the spec file.
2. Load the current rubric from simulations/quest/rubrics/{skill}-rubric-*.md.
   If no rubric file exists: create a v1 rubric with at least one essential criterion.
   Write it to disk before continuing.

FOR EACH ROUND, EXECUTE IN ORDER:

STEP 1 -- GENERATE VARIATIONS
Generate 5 complete, runnable prompt bodies labeled V-01 through V-05.
Each variation must be a full prompt -- not a diff, not a summary.
Each must include:
  - Label: V-NN
  - Axis: [the single dimension varied]
  - Hypothesis: [what this axis is predicted to change]
In Round 1: each variation must vary only one axis.
In Round 2+: you may combine axes that produced signal.

DO NOT proceed to Step 2 until all 5 variations are written in full.

STEP 2 -- SCORE EACH VARIATION
For every variation, score every criterion in the current rubric.
You must produce a criterion-by-criterion breakdown -- not just a composite.
For every criterion in the rubric, write:
  Result: PASS | PARTIAL | FAIL
  Evidence: [quote the specific variation text that justifies the result, or note its absence]

After all criteria, compute and state the composite score using the rubric formula.

DO NOT proceed to Step 3 until you have criterion-by-criterion scores for all 5 variations.

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS
Look at the score spread across all variations.
For every criterion where at least one variation scores higher than another:
  1. Name the structural property that caused the difference.
     Write it as a reusable principle -- not "V-03 passed" but "what V-03 did that others
     did not, as a property a future skill designer could apply."
  2. Tag its scope: skill-specific | transferable
If no variation outperforms any other on any criterion, state: "No score spread found --
no patterns extracted this round."

DO NOT proceed to Step 4 until all patterns are named and scoped.

STEP 4 -- PROPOSE RUBRIC CRITERIA
For each excellence pattern from Step 3, propose a new rubric criterion.
Every criterion proposal must include all five fields:
  ID:             C-[NN]
  Text:           [criterion description]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one sentence, auditable -- a reviewer can determine PASS or FAIL]

State each proposal explicitly. Wait for approval before adding to the rubric.
On approval, update the rubric file on disk.

CONVERGENCE -- CHECK BOTH GATES INDEPENDENTLY

GATE 1 (TRIAL): Do all variations in this round pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED

GATE 2 (PLATEAU): Did Step 3 in this round AND Step 3 in the previous round both find
  zero new excellence patterns?
  Name both rounds explicitly.
  State: QUEST PLATEAUED (Round X and Round Y: no new patterns) or QUEST NOT PLATEAUED

DO NOT declare golden unless both gates are satisfied simultaneously.
If only Gate 1 is satisfied: run another round.
If only Gate 2 is satisfied: run another round.

WRITE GOLDEN ARTIFACTS (on dual convergence only)

1. Select the highest-composite-scoring variation from this round.
2. Write it verbatim -- the full prompt body -- to:
     simulations/quest/golden/{skill}-golden-{date}.md
   Include frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN
3. Write the final accumulated rubric to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md

DO NOT write only a summary of the prompt. Write the complete prompt body.
DO NOT declare this task complete until both files are written to disk.
```

---

## V-04

**Variation axis**: Lifecycle emphasis + Output format (combination)
**Hypothesis**: Combining phase-labeled sections (V-01) with a mandatory score matrix
(V-02) creates structural enforcement at two levels -- the outer round structure (phases
cannot be skipped) and the inner scoring output (criteria cannot be elided). This
combination targets C-01, C-02, and C-03 simultaneously.

```
You are running quest-golden for the skill named in the invocation.

INPUTS
- Skill spec: signal.skills.yaml description field or spec file
- Current rubric: simulations/quest/rubrics/{skill}-rubric-*.md (latest version)
  If absent: create a v1 rubric with at least one essential criterion before proceeding.

ROUND STRUCTURE -- four labeled phases, in order, every round.

====================================================================
PHASE 1: GENERATE
====================================================================
Produce 5 complete, runnable skill body prompt variations.
Label each: V-01 through V-05.
Each variation includes:
  - Axis: [the single design dimension varied from the others]
  - Hypothesis: [one sentence predicting the effect of this axis]
  - Body: [the full prompt text -- not a diff, not a summary]

Round 1 constraint: single-axis variations only.
Round 2+: combine axes that produced signal in earlier rounds.

====================================================================
PHASE 2: SCORE
====================================================================
Score every variation against the current rubric using the score matrix format.

SCORE MATRIX -- one table per round covering all variations:

| Criterion | Cat | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|----|------|------|------|------|------|
| C-01: [text] | [cat] | E | PASS | FAIL | ... | ... | ... |
| C-02: [text] | [cat] | E | ...  | ...  | ... | ... | ... |
...

Results: PASS | PARTIAL | FAIL. No other values.
Add a COMPOSITE row at the bottom using the rubric formula.
Add a RANK row below that (1 = highest scoring).

Evidence for every FAIL or PARTIAL:
Below the matrix, list each FAIL/PARTIAL with a one-line evidence note:
  [V-NN / C-NN]: [why this failed -- quote or absence observation]

====================================================================
PHASE 3: IDENTIFY
====================================================================
Excellence signals (criteria with score spread):
For each criterion where at least one variation outperforms another:
  Pattern name:     [a reusable design principle -- not the variation name]
  Scope:            skill-specific | transferable
  Trigger:          [which criterion, what score difference]
  Structural cause: [the specific prompt property that drove the difference]

Failure patterns (criteria no variation passes):
  Criterion: [ID]
  Diagnosis: rubric-gap | skill-gap
  Note: [brief explanation]

Regression signals (Round 2+):
  List any variation that passed a criterion in round N-1 but fails now.

====================================================================
PHASE 4: PROPOSE
====================================================================
For each excellence signal from Phase 3:

  Proposed criterion:
    ID:             C-[NN]
    Text:           [criterion text]
    Weight:         essential | recommended | aspirational
    Category:       structure | behavior | correctness | depth | coverage
    Pass condition: [precise one-sentence auditable condition]

State: "Awaiting approval to add C-[NN] to rubric."
On approval: update the rubric file on disk and note the new version number.

====================================================================
CONVERGENCE GATES -- check after Phase 4 each round
====================================================================

GATE 1 -- TRIAL CONVERGENCE
Condition: all variations in this round pass all essential criteria.
Result: TRIAL CONVERGED | TRIAL NOT CONVERGED

GATE 2 -- QUEST PLATEAU
Condition: Phase 3 of this round AND Phase 3 of the previous round both produced zero
new excellence patterns. Name both rounds.
Result: QUEST PLATEAUED (Round [X] and Round [Y]: no new patterns) | QUEST NOT PLATEAUED

Dual convergence = Gate 1 CONVERGED AND Gate 2 PLATEAUED.
Both must be satisfied. A single gate passing does not end the quest.

====================================================================
GOLDEN PROMPT -- write only on dual convergence
====================================================================
1. Select: highest-ranking variation from this round.
2. Write verbatim prompt body to:
   simulations/quest/golden/{skill}-golden-{date}.md
   Frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN

3. Write accumulated final rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md

The golden artifact body is the full prompt. Metadata only is a hard fail.
```

---

## V-05

**Variation axis**: Output format + Phrasing register + Convergence gates pre-printed (combination)
**Hypothesis**: Combining the mandatory score matrix (V-02), imperative "must" phrasing
(V-03), and visually separate convergence gate blocks with pre-printed fill-in-the-blank
slots forces explicit evaluation of both convergence conditions before the model can
continue. Prevents QG-02 (unauditable scoring), QG-01 (premature golden declaration), and
QG-06 (loop not running) simultaneously. Targets C-02, C-03, C-04, C-05.

```
You are running quest-golden for {skill}.

Load inputs before starting:
  Skill spec: signal.skills.yaml or simulations/draft/specs/
  Rubric: simulations/quest/rubrics/{skill}-rubric-*.md (latest version)
  If no rubric exists: write a v1 rubric now with at least one essential criterion.
  Record rubric version in use at the start of each round.

ROUND LOOP -- repeat until dual convergence.

---

### A. GENERATE VARIATIONS

You must generate 5 complete, runnable skill body prompts (V-01 through V-05).
Each must be a full prompt body -- not a diff, not a reference to another variation.

Per variation:
  V-NN
  Axis: [name of the design dimension this variation tests]
  Hypothesis: [one sentence predicting what changes relative to the default]
  Body:
  [full prompt text]

Round 1: single-axis only.
Round 2+: you may combine axes that showed score spread in prior rounds.

---

### B. SCORE MATRIX

You must produce one score matrix per round. Every criterion. Every variation.

| ID   | Criterion (short)      | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------------------------|----|------|------|------|------|------|
| C-01 | [text excerpt]         | E  |      |      |      |      |      |
| C-02 | [text excerpt]         | E  |      |      |      |      |      |
...
| --   | COMPOSITE              |    |      |      |      |      |      |
| --   | RANK (1=best)          |    |      |      |      |      |      |

Fill every cell. Use PASS | PARTIAL | FAIL only.
Wt: E=essential, R=recommended, A=aspirational.

Evidence block (required for every FAIL or PARTIAL):
  V-NN / C-NN: [the specific structural property absent or present that drove this result]

---

### C. EXCELLENCE PATTERNS

Review the score matrix for columns that diverge. For each diverging criterion:

Pattern-[NN]:
  Name:      [a transferable or skill-specific design principle, stated as a rule]
  Scope:     skill-specific | transferable
  Trigger:   C-[ID] -- score spread: [e.g., V-01=PASS, V-02=FAIL, V-03=PASS]
  Mechanism: [the structural property in the passing variations that the failing ones lack]

If no criterion shows spread (all PASS or all FAIL): state "No patterns this round."
Note: all-pass rounds confirm stability but contribute nothing to plateau detection.

Failure pattern check:
For any criterion where all variations FAIL:
  Diagnosis: rubric-gap (criterion not achievable by any variation) | skill-gap (skill
  design does not produce this behavior)

---

### D. PROPOSED CRITERIA

For each pattern named in C above, propose a rubric criterion.
Each proposal must include all five fields -- incomplete proposals will not be added.

  ID:             C-[NN]
  Text:           [what the criterion tests, one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable -- a reviewer applying this criterion reaches the same
                  PASS/FAIL without ambiguity]

State the proposal. Await approval. On approval: update the rubric file on disk, increment
the rubric version number, and state the new path.

---

### E. CONVERGENCE GATES

Complete both gates before starting the next round.

GATE 1 -- TRIAL CONVERGENCE
  Predicate: every variation in this round passes every essential criterion.
  Essential criteria failing this round: [list C-NN IDs, or "none"]
  Variations failing at least one essential: [list V-NN IDs, or "none"]
  GATE 1 RESULT: [ TRIAL CONVERGED | TRIAL NOT CONVERGED ]

GATE 2 -- QUEST PLATEAU
  Predicate: Section C of this round and Section C of the immediately preceding round both
  found zero new excellence patterns.
  This round (Round [N]) new patterns: [count and names, or "none"]
  Previous round (Round [N-1]) new patterns: [count and names, or "none"]
  GATE 2 RESULT: [ QUEST PLATEAUED -- Round [N-1] and Round [N] both found zero new
                    patterns | QUEST NOT PLATEAUED -- [which round found a new pattern] ]

DUAL CONVERGENCE CHECK:
  Gate 1: [CONVERGED | NOT CONVERGED]
  Gate 2: [PLATEAUED | NOT PLATEAUED]
  Action: [ WRITE GOLDEN -- proceed to F | RUN ANOTHER ROUND ]

If only Gate 1 is satisfied: run another round. Do not declare golden.
If only Gate 2 is satisfied: run another round. Do not declare golden.

---

### F. GOLDEN ARTIFACTS (execute only when E declares WRITE GOLDEN)

1. Identify the highest-composite-scoring variation from this round.

2. Write the full prompt body verbatim to:
   simulations/quest/golden/{skill}-golden-{date}.md

   Frontmatter (YAML block):
     skill: quest-golden
     target_skill: {skill}
     date: {date}
     rounds: {N}
     rubric: simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md
     score: {composite}
     status: GOLDEN

   Body: the complete prompt text of the winning variation.
   Do not substitute a summary, a prose description, or a pointer. Write the full text.

3. Write the accumulated rubric to:
   simulations/quest/rubrics/{skill}-rubric-v{final}-{date}.md

   Include all criteria added across all rounds, with current weight assignments.

Confirm both files written. State paths.
```

---

## Variation Summary

| ID   | Axis                                          | Hypothesis (short)                                        | Primary targets |
|------|-----------------------------------------------|-----------------------------------------------------------|-----------------|
| V-01 | Lifecycle emphasis                            | Explicit phase labels prevent loop skipping               | C-01, C-03      |
| V-02 | Output format (table-heavy scoring)           | Score matrix makes per-criterion audit trivial            | C-02, C-09      |
| V-03 | Phrasing register (imperative + hard stops)   | DO NOT gates eliminate soft ambiguity                     | C-01, C-03, C-04|
| V-04 | V-01 + V-02 (lifecycle + tables)              | Outer phase enforcement + inner criterion enforcement     | C-01, C-02, C-03|
| V-05 | V-02 + V-03 + pre-printed convergence slots   | Fill-in-the-blank gates force both conditions checked     | C-02, C-03, C-04, C-05 |
