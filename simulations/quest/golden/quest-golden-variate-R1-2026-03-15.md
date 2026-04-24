# quest-golden Variate — Round 1

**Date:** 2026-03-15
**Skill:** quest-golden
**Rubric:** v1 (C-01 through C-10; essential C-01–C-05)
**Round:** R1 — single-axis pass (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 1 Variation Map

| Variation | Axis | What Changed | Hypothesis |
|-----------|------|--------------|------------|
| V-01 | role-sequence | Rubric-Curator + Prompt-Geneticist role declaration precedes all steps | Priming the operator with the curator/geneticist identity before mechanical steps improves C-06 (named pattern mechanism) and C-07 (5-field criterion) because the abstracting job is framed before the executing job |
| V-02 | output-format | Per-variation scorecard blocks replace cross-variation matrix | Completing one variation's full criterion trace before starting the next reduces partial-scoring; C-02 evidence quality improves because no partial cell is left when moving to the next variation |
| V-03 | lifecycle-emphasis | Convergence gate section expanded to equal the generation steps; Steps 1-2 compressed | C-03 (independent gate declarations) and C-08 (named rounds) improve because the gate mechanics receive equivalent instructional surface to generation mechanics, not a compressed postscript |
| V-04 | phrasing-register + lifecycle-emphasis | Fully imperative DO-NOT register combined with expanded convergence gate section | Imperative register creates hard stopping points at each phase boundary; expanded gate section makes two-gate independence structurally visible — targets C-01, C-02, C-03, C-08 simultaneously |
| V-05 | inertia-framing + output-format | Champion-challenger framing with champion column in score matrix | Naming a concrete champion forces spread-design by requiring each challenger to argue against a specific target; champion column makes regression visible at a glance — targets C-09 and C-03 |

---

## V-01 — Role Sequence: Rubric-Curator-First

**axis:** role-sequence
**hypothesis:** Declaring the operator's dual role (Rubric Curator + Prompt Geneticist) before any step instructions will improve C-06 (pattern stated as reusable principle with mechanism) and C-07 (proposed criterion has all 5 fields) because the operator is primed for the abstracting/archiving job before executing mechanical steps. The hypothesis is falsifiable: if C-06 and C-07 pass rates do not improve over baseline, the role declaration adds no protective value.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

ROLE: RUBRIC CURATOR + PROMPT GENETICIST

You are running a controlled experiment whose goal is to find the minimal prompt body that
reliably produces high-quality skill outputs, and to accumulate the rubric that defines
"high quality" as a durable artifact.

You hold two responsibilities simultaneously:
  Prompt Geneticist: produce variations, score them, extract what works.
  Rubric Curator: name the principles that caused improvement and propose them as criteria
    so future rounds can detect regression from those principles.

The loop runs until DUAL CONVERGENCE:
  TRIAL CONVERGED: all variations in a round pass every essential rubric criterion.
  QUEST PLATEAUED: this round AND the immediately preceding round found zero new excellence
    patterns.
Both gates must be satisfied simultaneously. Neither alone is sufficient.

---

EACH ROUND: EXECUTE ALL FOUR PHASES

PHASE 1 — GENERATE VARIATIONS

Write {N} complete, runnable skill body variations.

Round 1: vary exactly one axis per variation (single-axis pass).
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design (Prompt Geneticist role): before writing each variation, state which
axis it changes and predict which rubric criterion is most likely to shift as a result.
If all {N} variations are likely to produce identical composite scores, redesign for
divergence before writing.

Spread-design causal constraint: if all {N} variations produce identical composite scores,
this round generates no new excellence patterns and does not advance plateau detection —
because identical scores produce no cross-variation spread, and spread is the necessary
condition for pattern identification.

Axes to vary: role-sequence | output-format | lifecycle-emphasis |
              phrasing-register | inertia-framing | scoring-granularity

Each variation must be a complete, standalone skill body. Not a diff. Not a summary.
Every step. Every instruction. Every output contract.

Label:
  ## V-NN — [Axis Name]
  axis: [name]
  hypothesis: [which criterion changes and in which direction]
  [full prompt body]

DO NOT proceed to Phase 2 until all {N} variation bodies are written in full.

PHASE 2 — SCORE EACH VARIATION

Score every variation against every rubric criterion. Per-criterion scoring is mandatory.

For each variation, for each criterion:
  Result: PASS | FAIL
  Evidence: [quote or note from variation body confirming or denying the criterion]

Then produce the score matrix:

| Criterion | Weight | V-01 | V-02 | V-03 | ... |
|-----------|--------|------|------|------|-----|
| C-01      | E      |      |      |      |     |
| ...       |        |      |      |      |     |
| COMPOSITE |        |      |      |      |     |
| RANK      |        |      |      |      |     |

Composite formula: (essential_pass/N_essential * 60) + (recommended_pass/N_recommended * 30)
                   + (aspirational_pass/N_aspirational * 10)

DO NOT proceed to Phase 3 until per-criterion evidence is recorded for every variation.

PHASE 3 — IDENTIFY EXCELLENCE PATTERNS (Rubric Curator role)

For each criterion where at least one variation scores higher than another:
  Pattern name: [short label]
  Mechanism: the structural property present in passing variations and absent from failing ones
  Principle: stated as a reusable, transferable rule — not "V-02 scored higher" but what
             design choice caused the difference
  Scope: skill-specific | transferable

If no variation outperforms any other on any criterion:
  State: "No score spread found. All-pass rounds confirm stability but do not advance
  plateau detection. Redesign variations for divergence in the next round."

List any criterion all variations fail:
  Diagnosis: rubric-gap (criterion is poorly defined) | skill-gap (all variations share the flaw)

DO NOT proceed to Phase 4 until all patterns are named with mechanism stated.

PHASE 4 — PROPOSE RUBRIC CRITERIA (Rubric Curator role)

For each excellence pattern from Phase 3, propose a criterion with all five required fields:
  ID:             C-[NN] (next sequential ID after current rubric's highest)
  Text:           [what the criterion measures, one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence that makes pass/fail determinable]

---

CONVERGENCE CHECK (run after Phase 4 every round)

GATE 1 — TRIAL CONVERGENCE
Question: Do all {N} variations in this round pass every essential criterion?
State: TRIAL CONVERGED or TRIAL NOT CONVERGED
Evidence: [list which essential criteria failed and in which variations, or confirm all pass]

GATE 2 — PLATEAU DETECTION
Question: Did Phase 3 in this round AND in the immediately preceding round both find
zero new excellence patterns?
Requirement: cite both rounds by explicit name (e.g., "Round 2 and Round 3: no new
patterns found"). Do not write "the last two rounds."
State: QUEST PLATEAUED or QUEST NOT PLATEAUED
Evidence: [patterns found this round; patterns found last round]

DO NOT declare golden unless TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (on dual convergence only)

1. Select the highest-composite variation from this round.
   If tied, select the variation with minimal structure (fewest operator constraints).

2. Write the complete prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: the full, verbatim prompt text. Not a summary. Not a description.
   The complete skill body must be usable as a skill without modification.

3. Write the accumulated rubric (all criteria across all rounds) to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   Include all criteria with all five fields. Note which round added each criterion.

4. State both file paths.

---

## V-02 — Output Format: Per-Variation Scorecard

**axis:** output-format
**hypothesis:** Replacing the cross-variation score matrix (criteria × variations grid) with per-variation scorecard blocks — completing each variation's full criterion trace before starting the next — will improve C-02 evidence quality because partial-scoring failures happen when operators move to a new variation before completing the current one. Per-variation completion discipline removes this opportunity.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the full variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE DEFINITION
  TRIAL CONVERGED: all variations in a round pass every essential rubric criterion.
  QUEST PLATEAUED: this round AND the immediately preceding round found zero new excellence
    patterns.
Both gates must be satisfied simultaneously in the same round.

---

STEP 1 — GENERATE VARIATIONS

Write {N} complete, runnable skill body variations.

Round 1: vary exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing the first variation, assign one axis per variation.
Ensure at least two variations target different rubric criteria. Variations likely to
produce identical composite scores must be redesigned before writing.

Causal note: rounds where all {N} variations produce identical composite scores cannot
contribute to plateau detection — identical scores produce no excellence patterns, and
plateau detection requires zero new patterns in two consecutive rounds. Rounds with no
patterns do not count toward the two required.

Axes: role-sequence | output-format | lifecycle-emphasis |
      phrasing-register | inertia-framing | scoring-granularity

Each variation is a COMPLETE, STANDALONE skill body. Not a diff. Not a reference to
another variation.

Label each variation:
  ## V-NN — [Axis Name]
  axis: [name]
  hypothesis: [criterion expected to change + predicted direction]
  [full body — every instruction, every step, every output contract]

Do not proceed to Step 2 until all {N} bodies are written.

---

STEP 2 — SCORE EACH VARIATION (per-variation scorecards)

Score every variation using a per-variation scorecard. Complete each variation's full
scorecard before starting the next. This is a completeness discipline: do not start V-02's
scorecard until V-01's is finished with evidence in every row.

Format for each variation:

### SCORECARD: V-NN

| Criterion | Weight | Result    | Evidence                             |
|-----------|--------|-----------|--------------------------------------|
| C-01      | E      | PASS/FAIL | [text or note from the variation]    |
| C-02      | E      | PASS/FAIL | [text or note from the variation]    |
| C-03      | E      | PASS/FAIL | [text or note from the variation]    |
| C-04      | E      | PASS/FAIL | [text or note from the variation]    |
| C-05      | E      | PASS/FAIL | [text or note from the variation]    |
| C-06      | R      | PASS/FAIL | [text or note from the variation]    |
| C-07      | R      | PASS/FAIL | [text or note from the variation]    |
| C-08      | R      | PASS/FAIL | [text or note from the variation]    |
| C-09      | A      | PASS/FAIL | [text or note from the variation]    |
| C-10      | A      | PASS/FAIL | [text or note from the variation]    |
| **COMPOSITE** | —  | [score]   |                                      |

Repeat for all {N} variations in order (V-01, V-02, ..., V-{N}).

After all scorecards are complete, produce the summary matrix:

| V    | COMPOSITE | RANK | Essential failures |
|------|-----------|------|--------------------|
| V-01 |           |      |                    |
| ...  |           |      |                    |

Do not proceed to Step 3 until all {N} scorecards are complete with evidence in every row.

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scored higher than another:
  Pattern name: [label]
  Structural property: [what design choice in passing variations is absent in failing ones]
  Reusable principle: [transferable rule, not a variation comparison]
  Scope: skill-specific | transferable

If no variation outperforms any other on any criterion:
  State: "No score spread found. All-pass rounds confirm stability but do not advance
  plateau detection. Redesign variations for divergence."

List any criterion all variations fail:
  Diagnosis: rubric-gap | skill-gap

Do not proceed to Step 4 until all patterns are named with structural property stated.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five fields:
  ID:             C-[NN]
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable, one sentence]

---

CONVERGENCE CHECK

GATE 1 — TRIAL
Do all {N} variations pass every essential criterion?
State: TRIAL CONVERGED or TRIAL NOT CONVERGED
Evidence: [essential failures, or "all essential criteria pass across all variations"]

GATE 2 — PLATEAU
Did Step 3 find zero new excellence patterns in this round AND in the immediately preceding round?
Name both rounds explicitly (e.g., "Round 3 and Round 4: no new patterns found").
State: QUEST PLATEAUED or QUEST NOT PLATEAUED
Evidence: [patterns found this round; patterns found in previous round by name]

Declare golden only if both gates are satisfied in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write the full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body must be the complete, verbatim, runnable skill prompt — not a summary.
3. Write the accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   List all criteria from all rounds with all five fields per criterion.
4. State both artifact paths.

---

## V-03 — Lifecycle Emphasis: Convergence-Gate-Heavy

**axis:** lifecycle-emphasis
**hypothesis:** Operators most commonly fail C-03 (independent gate declarations) and C-08 (named rounds in plateau declaration) because the convergence section is always the shortest section of the prompt — a compressed postscript after four expanded steps. Giving the convergence gate section equal instructional surface to Steps 1-2 will improve C-03 and C-08 pass rates because the gate mechanics receive explicit procedural guidance rather than one-line instructions.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the variation-score-extract-propose loop until dual convergence. Each round has four
steps plus a convergence check. Execute all five before starting the next round.

STEP 1 — GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. Each varies exactly one axis in
Round 1; combine axes in Round 2+. Before writing, assign axes and verify variations will
diverge on at least one criterion — rounds where all variations produce identical composite
scores do not advance plateau detection.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each: axis, hypothesis (criterion + direction), full body. Do not proceed until
all {N} bodies are written.

STEP 2 — SCORE VARIATIONS

Score every criterion for every variation. Show per-criterion pass/fail before computing composite.

| Criterion | Weight | V-01 | V-02 | ... |
|-----------|--------|------|------|-----|
| ...       |        |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

Do not proceed until all per-criterion scores are shown.

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation outperforms another, name the pattern as a
reusable principle (mechanism, not comparison). State scope (skill-specific | transferable).
If no spread: state it and note this round will not advance plateau detection.

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose: ID, text, weight, category, pass condition (all five fields required).

---

CONVERGENCE CHECK — TWO INDEPENDENT GATES

This section is as important as Steps 1-4. Execute both gates fully, in order, with
explicit evidence for each. Do not merge them. Do not abbreviate one to reach the other.

---

GATE 1: TRIAL CONVERGENCE

Objective: determine whether the current round's variations are sufficient to stop
generating new variations.

Procedure:
  a. List every essential criterion (marked E in the rubric).
  b. For each variation, state whether it passes every essential criterion.
  c. If any essential criterion fails in any variation: TRIAL NOT CONVERGED.
     Name every (variation, criterion) pair that failed.
  d. If all essential criteria pass in all variations: TRIAL CONVERGED.

State exactly one of:
  TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
  TRIAL NOT CONVERGED: [V-NN fails C-NN], [V-NN fails C-NN], ...

Do not conflate TRIAL CONVERGED with QUEST PLATEAUED. They are independent gates asking
different questions. TRIAL CONVERGED does not mean the quest is done.

---

GATE 2: PLATEAU DETECTION

Objective: determine whether the rubric has stopped learning — the signal that the
excellence frontier has been found.

Definition: a round has "no new excellence patterns" when Step 3 found zero patterns worth
proposing — either all patterns were already in the rubric, or no score spread existed.
Identical composite scores across all variations means no spread, which means no new patterns.

The plateau gate requires TWO CONSECUTIVE ROUNDS with no new patterns. One round alone is
insufficient — the plateau is confirmed by repetition, not by a single no-pattern round.

Procedure:
  a. State what Step 3 found in the CURRENT ROUND: [pattern names] OR "no new patterns."
  b. State what Step 3 found in the IMMEDIATELY PRECEDING ROUND: [pattern names] OR "no new patterns."
  c. Name both rounds explicitly by label — e.g., "Round 3" and "Round 4."
     Do not write "the last two rounds" or "the previous two rounds."
  d. If both named rounds show zero new patterns: QUEST PLATEAUED.
  e. If either named round found new patterns: QUEST NOT PLATEAUED. Continue.

State exactly one of:
  QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
  QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
    not yet achieved.

---

DUAL CONVERGENCE RULE

Declare golden ONLY when TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

If TRIAL NOT CONVERGED: generate new variations targeting the failing essential criteria.
If TRIAL CONVERGED but QUEST NOT PLATEAUED: generate new variations to uncover remaining patterns.
If QUEST PLATEAUED but TRIAL NOT CONVERGED: audit whether the newest essential criteria are
  achievable by the current prompt structure.

Do not write golden artifacts until both gates are satisfied simultaneously.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: complete, runnable, verbatim. Not a summary. Not a description.
3. Write accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria from all rounds, all five fields per criterion, round-of-addition noted.
4. State both file paths.

---

## V-04 — Combined: Phrasing Register (Imperative) + Lifecycle Emphasis (Convergence-Gate-Heavy)

**axis:** phrasing-register + lifecycle-emphasis (combined)
**hypothesis:** Fully imperative DO-NOT register combined with an expanded convergence gate section targets C-01 (loop completeness), C-02 (per-criterion evidence), C-03 (independent gates), and C-08 (named rounds) simultaneously. The imperative register creates hard stopping points at each phase boundary, preventing step-skipping. The expanded gate section makes the two-gate independence structurally undeniable. Combined, these axes close the two most common failure modes: skipping a phase and conflating the two convergence gates.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run this loop until dual convergence. Execute every step. Do not skip.

---

STEP 1 — GENERATE VARIATIONS

Write {N} complete skill body variations. These are complete, runnable prompts — not diffs,
not summaries, not references to other variations. Every step. Every instruction. Every output contract.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in prior rounds.

Before writing any body: assign one axis per variation. Confirm at least two variations
target different rubric criteria and will diverge on at least one criterion.

Why divergence is mandatory: if all {N} variations produce identical composite scores, this
round cannot advance plateau detection. Identical scores mean no score spread. No spread
means no excellence patterns. No new patterns means the round does not count toward the
two consecutive zero-pattern rounds required for plateau. Design divergence before writing.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each variation:
  ## V-NN — [Axis]
  axis: [name]
  hypothesis: [criterion expected to change + direction]
  [full body — every instruction, every step, every output contract]

DO NOT proceed to Step 2 until every variation body is written in full. No placeholders.
No "see V-01 for X section." Write everything.

---

STEP 2 — SCORE EVERY VARIATION

Score every criterion for every variation. Per-criterion results come before composite — no exceptions.
A composite score without individual criterion results does not satisfy C-02.

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01      | E      |      |      |      |      |      |
| C-02      | E      |      |      |      |      |      |
| C-03      | E      |      |      |      |      |      |
| C-04      | E      |      |      |      |      |      |
| C-05      | E      |      |      |      |      |      |
| C-06      | R      |      |      |      |      |      |
| C-07      | R      |      |      |      |      |      |
| C-08      | R      |      |      |      |      |      |
| C-09      | A      |      |      |      |      |      |
| C-10      | A      |      |      |      |      |      |
| COMPOSITE |        |      |      |      |      |      |
| RANK      |        |      |      |      |      |      |

DO NOT proceed to Step 3 until every cell contains a result with evidence.

---

STEP 3 — NAME EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another:
  Pattern name: [label]
  Mechanism: [structural property present in passing variations, absent in failing ones]
  Principle: [reusable rule — not "V-02 scored higher" but what design choice caused it]
  Scope: skill-specific | transferable

If no criterion shows spread, write exactly:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
  detection. Redesign variations for divergence in the next round."

DO NOT proceed to Step 4 until every pattern has a mechanism stated.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, write a criterion with all five fields. No field may be blank.
  ID:             C-[NN]
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable, one sentence, no interpretation required]

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

Execute both gates separately. A single paragraph covering both is not acceptable.

GATE 1 — TRIAL CONVERGENCE

Ask: do all {N} variations pass every essential criterion?
List every essential criterion. Check each variation against each.

State ONE of:
  TRIAL CONVERGED: all variations pass all essential criteria this round.
  TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

DO NOT declare TRIAL CONVERGED unless you have verified every (essential criterion, variation) pair.

GATE 2 — PLATEAU DETECTION

Ask: did Step 3 in this round AND in the immediately preceding round both find zero new patterns?

Name the current round by label.
Name the immediately preceding round by label.
State what Step 3 found in each — by round name, not "the last two rounds."

State ONE of:
  QUEST PLATEAUED: [Round X] and [Round Y]: no new excellence patterns in either round.
  QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
    not yet achieved.

DO NOT declare QUEST PLATEAUED unless both named rounds have zero new patterns and both are
explicitly cited.

DUAL CONVERGENCE RULE: declare golden ONLY when TRIAL CONVERGED AND QUEST PLATEAUED appear
in the same round. Neither gate alone is sufficient.

---

WRITE GOLDEN ARTIFACTS — DUAL CONVERGENCE ONLY

DO NOT write golden artifacts unless both gates are satisfied in the same round.

1. Select the highest-composite variation. Ties: pick the variation with minimal structure.

2. Write the full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter required: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: the complete, verbatim, runnable prompt text. Not a summary. Not a description.
   The body must be copyable and usable as a skill without any modification.

3. Write the final accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   Include every criterion active at convergence, from every round, with all five fields.
   Note which round added each criterion.

4. State both file paths explicitly.

---

## V-05 — Combined: Inertia Framing (Champion-Challenger) + Output Format (Champion Column)

**axis:** inertia-framing + output-format (combined)
**hypothesis:** Naming a concrete champion (previous golden, or defined naive implementation) activates competitive spread-design: operators write variations that argue against a specific target rather than varying abstractly. Adding a champion column to the score matrix makes regression visible at a glance. Combined, these axes improve C-09 (active spread-design instruction in generation phase) because the champion gives the spread-design instruction a concrete referent, and C-03 (independent gate declarations) because the champion column makes the gap between "trial converged" and "plateau" structurally visible.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

THE CHAMPION

If a previous golden prompt exists for this skill, it is the champion.

If this is Round 1 and no previous golden exists, define the champion as the naive
implementation: a prompt that lists the four phases (generate, score, extract, propose)
and a convergence check — but contains no spread-design instruction, no causal explanation
for why identical-score rounds stall plateau detection, and no explicit separation between
the TRIAL and PLATEAU gates.

The champion is the cost of doing nothing. Every variation must argue it improves on the
champion on at least one criterion without regressing on any criterion the champion passes.

---

EACH ROUND: FOUR STEPS + CONVERGENCE

STEP 1 — GENERATE CHALLENGERS

Generate {N} challenger variations. A challenger is a complete, runnable skill body that
changes exactly one axis from the champion (Round 1) or combines axes that produced
improvement in earlier rounds (Round 2+).

Before writing each challenger:
  a. State which axis it changes from the champion.
  b. State what the champion currently does on that axis.
  c. State what this challenger does differently.
  d. State which rubric criterion it targets and how the champion currently fails it.

A challenger hypothesis must argue against the champion. "This variation will differ" is
not a valid challenger hypothesis. The challenger must name the champion's weakness and
claim to address it.

Active spread-design: before writing any challenger, survey all {N} planned challengers.
Confirm they target different rubric criteria. If all challengers are likely to produce
the same composite score as the champion, the round will generate no excellence patterns
and will not advance plateau detection — redesign before writing.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each challenger:
  ## V-NN — [Axis: Challenger Stance vs Champion Stance]
  axis: [name]
  champion-stance: [what the champion does on this axis]
  challenger-stance: [what this variation does differently]
  hypothesis: [criterion targeted, champion weakness exploited, predicted improvement]
  [FULL SKILL BODY — standalone, complete, not a diff]

Do not proceed to Step 2 until all {N} challengers are written in full.

STEP 2 — SCORE CHAMPION AND CHALLENGERS

Score the champion AND all {N} challengers against every rubric criterion. Per-criterion
results required before composite.

| Criterion | Weight | Champion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|----------|------|------|------|------|------|
| C-01      | E      |          |      |      |      |      |      |
| C-02      | E      |          |      |      |      |      |      |
| C-03      | E      |          |      |      |      |      |      |
| C-04      | E      |          |      |      |      |      |      |
| C-05      | E      |          |      |      |      |      |      |
| C-06      | R      |          |      |      |      |      |      |
| C-07      | R      |          |      |      |      |      |      |
| C-08      | R      |          |      |      |      |      |      |
| C-09      | A      |          |      |      |      |      |      |
| C-10      | A      |          |      |      |      |      |      |
| COMPOSITE |        |          |      |      |      |      |      |
| RANK      |        |          |      |      |      |      |      |

After scoring, for each challenger: state HYPOTHESIS CONFIRMED or HYPOTHESIS NOT CONFIRMED
based on whether the challenger outscored the champion on its targeted criterion.

Do not proceed to Step 3 until all per-criterion scores are recorded.

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one challenger scores higher than the champion (or higher
than another challenger):
  Pattern name: [label]
  Mechanism: [structural property present in better-scoring versions, absent from worse-scoring ones]
  Principle: [reusable rule, not a comparison]
  Scope: skill-specific | transferable

If no challenger outperforms the champion on any criterion:
  State: "No score spread found. Challengers did not improve on the champion. Redesign
  challengers to target different axes or different criteria. All-pass rounds do not
  advance plateau detection."

Do not proceed to Step 4 until patterns are named.

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five fields:
  ID:             C-[NN]
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable, one sentence]

---

CONVERGENCE CHECK

GATE 1 — TRIAL CONVERGENCE
Do all {N} challengers pass every essential criterion?
State: TRIAL CONVERGED or TRIAL NOT CONVERGED
Evidence: [essential failures named, or confirm all pass]

GATE 2 — PLATEAU DETECTION
Did Step 3 in this round AND in the immediately preceding round find zero new excellence patterns?
Name both rounds explicitly by label.
State: QUEST PLATEAUED or QUEST NOT PLATEAUED
Evidence: [patterns found this round; patterns found last round, named]

Declare golden only if TRIAL CONVERGED AND QUEST PLATEAUED simultaneously in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite challenger. Ties: prefer minimal structure.
   If the champion still outscores all challengers on composite: the champion is golden
   (it already represents dual convergence from a prior run).

2. Write the complete prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: complete, verbatim, runnable. Not a summary.

3. Write the accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria from all rounds, all five fields, with round-of-addition noted.

4. State both artifact paths.

---

## STEP 2 — SCORE EACH VARIATION

Rubric version: v1 (C-01 through C-10).
Essential tier: C-01–C-05. Recommended: C-06–C-08. Aspirational: C-09–C-10.
PARTIAL = 0 for essential/recommended; PARTIAL = 0.5 for aspirational.

### SCORECARD: V-01 (Role Sequence: Rubric-Curator-First)

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | "PHASE 1 — GENERATE VARIATIONS / PHASE 2 — SCORE / PHASE 3 — IDENTIFY EXCELLENCE PATTERNS / PHASE 4 — PROPOSE RUBRIC CRITERIA" — all four labeled phases with substantive content |
| C-02 | E | PASS | Score matrix with criterion rows, PASS/FAIL column per variation, Evidence column — composite appears only after all rows. "Per-criterion scoring is mandatory." |
| C-03 | E | PASS | "GATE 1 — TRIAL CONVERGENCE" and "GATE 2 — PLATEAU DETECTION" as separate named sections. Each requires a distinct state declaration. |
| C-04 | E | PASS | "Body: the full, verbatim prompt text. Not a summary. Not a description. The complete skill body must be usable as a skill without modification." |
| C-05 | E | PASS | "Write the accumulated rubric (all criteria across all rounds) to: … Include all criteria with all five fields. Note which round added each criterion." |
| C-06 | R | PASS | Phase 3: "Mechanism: the structural property present in passing variations and absent from failing ones / Principle: stated as a reusable, transferable rule — not 'V-02 scored higher' but what design choice caused the difference" |
| C-07 | R | PASS | Phase 4 lists all five fields: ID, Text, Weight, Category, Pass condition — individually labeled. |
| C-08 | R | PASS | Gate 2: "cite both rounds by explicit name (e.g., 'Round 2 and Round 3: no new patterns found'). Do not write 'the last two rounds.'" |
| C-09 | A | PASS | Phase 1: "Round 1: vary exactly one axis per variation. Round 2+: combine axes that produced signal in earlier rounds." Round-progression rule present before any body instruction. |
| C-10 | A | PASS | Phase 1: "…because identical scores produce no cross-variation spread, and spread is the necessary condition for pattern identification." Full chain: identical scores → no spread → no patterns → no plateau advance. |
| **COMPOSITE** | — | **100** | 5/5 essential + 3/3 recommended + 2/2 aspirational |

### SCORECARD: V-02 (Output Format: Per-Variation Scorecard)

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | "STEP 1 — GENERATE VARIATIONS / STEP 2 — SCORE EACH VARIATION (per-variation scorecards) / STEP 3 — IDENTIFY EXCELLENCE PATTERNS / STEP 4 — PROPOSE RUBRIC CRITERIA" — all four phases. |
| C-02 | E | PASS | Per-variation scorecard format with "Evidence" column per row. "Completeness discipline: do not start V-02's scorecard until V-01's is finished with evidence in every row." Composite appears only in summary matrix after all individual scorecards complete. |
| C-03 | E | PASS | "GATE 1 — TRIAL" and "GATE 2 — PLATEAU" as separate named sections, each requiring an explicit state declaration. |
| C-04 | E | PASS | "Body must be the complete, verbatim, runnable skill prompt — not a summary." |
| C-05 | E | PASS | "List all criteria from all rounds with all five fields per criterion." |
| C-06 | R | PASS | Step 3: "Structural property: [what design choice in passing variations is absent in failing ones] / Reusable principle: [transferable rule, not a variation comparison]" |
| C-07 | R | PASS | Step 4: all five fields listed: ID, Text, Weight, Category, Pass condition. |
| C-08 | R | PASS | Gate 2: "Name both rounds explicitly (e.g., 'Round 3 and Round 4: no new patterns found')." |
| C-09 | A | PASS | Step 1: "Active spread-design: before writing the first variation, assign one axis per variation… Round 1: vary exactly one axis per variation. Round 2+: combine axes that produced signal in earlier rounds." |
| C-10 | A | PASS | Step 1 causal note: "identical scores produce no excellence patterns, and plateau detection requires zero new patterns in two consecutive rounds. Rounds with no patterns do not count toward the two required." Full chain. |
| **COMPOSITE** | — | **100** | 5/5 essential + 3/3 recommended + 2/2 aspirational |

### SCORECARD: V-03 (Lifecycle Emphasis: Convergence-Gate-Heavy)

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | "STEP 1 — GENERATE / STEP 2 — SCORE VARIATIONS / STEP 3 — IDENTIFY EXCELLENCE PATTERNS / STEP 4 — PROPOSE RUBRIC CRITERIA" — all four phases. |
| C-02 | E | PASS | Cross-variation matrix with all criteria, COMPOSITE, RANK rows. "Show per-criterion pass/fail before computing composite." |
| C-03 | E | PASS | "GATE 1: TRIAL CONVERGENCE" (procedure steps a–d, dedicated state declaration) and "GATE 2: PLATEAU DETECTION" (procedure steps a–e, dedicated state declaration). "Do not conflate TRIAL CONVERGED with QUEST PLATEAUED." Strongest separation of any variation. |
| C-04 | E | PASS | "Body: complete, runnable, verbatim. Not a summary. Not a description." |
| C-05 | E | PASS | "All criteria from all rounds, all five fields per criterion, round-of-addition noted." |
| C-06 | R | PASS | Step 3: "name the pattern as a reusable principle (mechanism, not comparison). State scope (skill-specific | transferable)." |
| C-07 | R | PASS | Step 4: "propose: ID, text, weight, category, pass condition (all five fields required)" |
| C-08 | R | PASS | Gate 2 procedure: "Name both rounds explicitly by label — e.g., 'Round 3' and 'Round 4.' Do not write 'the last two rounds' or 'the previous two rounds.'" |
| C-09 | A | PASS | Step 1: "Before writing, assign axes and verify variations will diverge on at least one criterion. Round 1: vary exactly one axis per variation; combine axes in Round 2+." Round-progression rule present. |
| C-10 | A | PASS | Gate 2 definition: "Identical composite scores across all variations means no spread, which means no new patterns." Step 1: "rounds where all variations produce identical composite scores do not advance plateau detection." Two-statement chain covers the full mechanism. |
| **COMPOSITE** | — | **100** | 5/5 essential + 3/3 recommended + 2/2 aspirational |

### SCORECARD: V-04 (Phrasing Register + Lifecycle Emphasis)

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | "STEP 1 — GENERATE VARIATIONS / STEP 2 — SCORE EVERY VARIATION / STEP 3 — NAME EXCELLENCE PATTERNS / STEP 4 — PROPOSE RUBRIC CRITERIA" — all four phases with DO NOT gates. |
| C-02 | E | PASS | "A composite score without individual criterion results does not satisfy C-02." Explicit matrix with all criteria rows. "Per-criterion results come before composite — no exceptions." |
| C-03 | E | PASS | "GATE 1 — TRIAL CONVERGENCE" and "GATE 2 — PLATEAU DETECTION" as fully separate sections. "Execute both gates separately. A single paragraph covering both is not acceptable." Strongest gate-separation language of any variation. |
| C-04 | E | PASS | "Body: the complete, verbatim, runnable prompt text. Not a summary. Not a description. The body must be copyable and usable as a skill without any modification." |
| C-05 | E | PASS | "Include every criterion active at convergence, from every round, with all five fields. Note which round added each criterion." |
| C-06 | R | PASS | Step 3: "Mechanism: [structural property present in passing variations, absent in failing ones] / Principle: [reusable rule — not 'V-02 scored higher' but what design choice caused it]" |
| C-07 | R | PASS | Step 4: "No field may be blank." All five fields listed: ID, Text, Weight, Category, Pass condition. |
| C-08 | R | PASS | Gate 2: "Name the current round by label. Name the immediately preceding round by label. State what Step 3 found in each — by round name, not 'the last two rounds.'" |
| C-09 | A | PASS | Step 1: "Round 1: change exactly one axis per variation. Round 2+: combine axes that produced signal in prior rounds. Before writing any body: assign one axis per variation. Confirm at least two variations target different rubric criteria and will diverge on at least one criterion." |
| C-10 | A | PASS | Step 1: "Why divergence is mandatory: if all {N} variations produce identical composite scores, this round cannot advance plateau detection. Identical scores mean no score spread. No spread means no excellence patterns. No new patterns means the round does not count toward the two consecutive zero-pattern rounds required for plateau." Strongest C-10 formulation — four discrete causal sentences. |
| **COMPOSITE** | — | **100** | 5/5 essential + 3/3 recommended + 2/2 aspirational |

### SCORECARD: V-05 (Inertia Framing + Output Format)

| Criterion | Wt | Result | Evidence |
|-----------|----|--------|----------|
| C-01 | E | PASS | "STEP 1 — GENERATE CHALLENGERS / STEP 2 — SCORE CHAMPION AND CHALLENGERS / STEP 3 — IDENTIFY EXCELLENCE PATTERNS / STEP 4 — PROPOSE RUBRIC CRITERIA" — all four phases. |
| C-02 | E | PASS | Champion column added to cross-variation matrix. "Per-criterion results required before composite." |
| C-03 | E | PASS | "GATE 1 — TRIAL CONVERGENCE" and "GATE 2 — PLATEAU DETECTION" as separate sections. "Declare golden only if TRIAL CONVERGED AND QUEST PLATEAUED simultaneously in the same round." |
| C-04 | E | PASS | "Body: complete, verbatim, runnable. Not a summary." |
| C-05 | E | PASS | "All criteria from all rounds, all five fields, with round-of-addition noted." |
| C-06 | R | PASS | Step 3: "Mechanism: [structural property present in better-scoring versions, absent from worse-scoring ones] / Principle: [reusable rule, not a comparison]" |
| C-07 | R | PASS | Step 4: all five fields present: ID, Text, Weight, Category, Pass condition. |
| C-08 | R | PASS | Gate 2: "Name both rounds explicitly by label." |
| C-09 | A | PASS | Step 1: "A challenger is a complete, runnable skill body that changes exactly one axis from the champion (Round 1) or combines axes that produced improvement in earlier rounds (Round 2+)." Round-progression rule present. Active spread-design instruction: "survey all {N} planned challengers. Confirm they target different rubric criteria." |
| C-10 | A | PASS | Step 1: "If all challengers are likely to produce the same composite score as the champion, the round will generate no excellence patterns and will not advance plateau detection." Covers: identical scores → no excellence patterns → no plateau advance. |
| **COMPOSITE** | — | **100** | 5/5 essential + 3/3 recommended + 2/2 aspirational |

### Round 1 Summary Matrix

| V    | COMPOSITE | RANK | Essential failures |
|------|-----------|------|--------------------|
| V-01 | 100       | T-1  | none               |
| V-02 | 100       | T-1  | none               |
| V-03 | 100       | T-1  | none               |
| V-04 | 100       | T-1  | none               |
| V-05 | 100       | T-1  | none               |

---

## STEP 3 — IDENTIFY EXCELLENCE PATTERNS

No score spread found on any criterion. All 5 variations pass all 10 criteria at identical composite scores (100).

All-pass rounds confirm rubric v1 stability on these variation axes, but do not advance plateau detection. No cross-variation score difference exists from which to extract a structural property.

**Structural observations (not formal patterns — no score spread):**

Although scores are identical, structural properties differ across variations in ways not yet captured by v1 rubric criteria:

| Property | Present in | Absent from | Potential future axis |
|----------|-----------|-------------|----------------------|
| Evidence cells per criterion row (text quote/note) | V-01, V-02 | V-03, V-04, V-05 | scoring-granularity |
| Per-variation scorecard completeness discipline (one scorecard complete before starting next) | V-02 | V-01, V-03, V-04, V-05 | output-format |
| Dual role declaration (Rubric Curator + Prompt Geneticist) | V-01 | V-02–V-05 | role-sequence |
| Four-sentence explicit causal chain on C-10 | V-04 | V-01–V-03, V-05 | lifecycle-emphasis |
| Gate constraint meta-language ("single paragraph not acceptable") | V-04 | V-01–V-03, V-05 | phrasing-register |
| Champion-challenger framing with champion column | V-05 | V-01–V-04 | inertia-framing |
| HYPOTHESIS CONFIRMED/NOT CONFIRMED verdict per challenger | V-05 | V-01–V-04 | inertia-framing |

These observations cannot generate formal patterns this round because no rubric criterion distinguishes between variations that have these properties and those that do not. To produce spread, Round 2 must either: (a) add criteria targeting these properties and re-score, or (b) design degraded variations that deliberately omit properties that all current variations share — testing whether their removal causes essential failures.

---

## STEP 4 — PROPOSE RUBRIC CRITERIA

No new criteria proposed this round. No score spread was found; formal pattern extraction produced no results. The structural observations above are candidates for future criterion proposals after Round 2 testing confirms which properties are discriminating.

---

## CONVERGENCE CHECK

**GATE 1 — TRIAL CONVERGENCE**

Essential criteria: C-01, C-02, C-03, C-04, C-05.

| | C-01 | C-02 | C-03 | C-04 | C-05 |
|-|------|------|------|------|------|
| V-01 | PASS | PASS | PASS | PASS | PASS |
| V-02 | PASS | PASS | PASS | PASS | PASS |
| V-03 | PASS | PASS | PASS | PASS | PASS |
| V-04 | PASS | PASS | PASS | PASS | PASS |
| V-05 | PASS | PASS | PASS | PASS | PASS |

**TRIAL CONVERGED:** all 5 variations pass all 5 essential criteria in Round 1.

---

**GATE 2 — PLATEAU DETECTION**

Round 1: Step 3 found zero new excellence patterns (no score spread; all-pass round).
Immediately preceding round: Round 1 is the first round — no preceding round exists.

**QUEST NOT PLATEAUED:** Round 1 is the first of two consecutive zero-pattern rounds required for plateau. Round 2 must also find zero new excellence patterns before QUEST PLATEAUED can be declared.

---

**Dual convergence status:** TRIAL CONVERGED but QUEST NOT PLATEAUED. Do not write golden artifacts. Proceed to Round 2.

**Round 2 design directive:** All v1 criteria are stable. The structural observations in Step 3 above are the highest-value axes for Round 2. To generate score spread, Round 2 must introduce variations that test whether properties absent from some v1 variations would — if elevated to rubric criteria — produce failures. Recommended axes:

1. **Degraded causal chain (C-10 weakening)** — vary how explicitly the causal chain is stated: full 4-sentence chain (V-04 style) vs. single-sentence conclusion ("identical scores don't advance plateau") vs. omitted.
2. **Evidence cells absent** — vary whether per-criterion scoring requires text evidence quotes or just PASS/FAIL marks.
3. **Gate meta-constraint absent** — test whether removing "a single paragraph covering both gates is not acceptable" affects C-03.

If Round 2 also finds zero new patterns: QUEST PLATEAUED. Combined with TRIAL CONVERGED, golden artifacts can be written.
