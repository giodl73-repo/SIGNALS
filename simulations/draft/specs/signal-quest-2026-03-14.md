# Quest Specification

**Topic**: signal
**Namespace**: /quest:
**Skills**: 4
**Default mode**: Full
**Audience**: Skill builders -- anyone authoring, improving, or validating a Signal skill body.
The quest namespace is meta-tooling: it makes the other 48 skills better.

---

## Purpose

The other 9 namespaces produce signals. Quest makes the skills themselves better.

Every skill has a golden prompt: the formulation that produces consistently excellent output
across all scenarios. Finding it is not intuition -- it is systematic variation, scoring against
a rubric, extraction of excellence patterns, and iteration until the rubric stabilizes.

Quest answers: "Is this the best this skill can be?"

---

## The Quest Loop

```
rubric           <- define what "good output" looks like (criteria with pass conditions)
variate          <- generate N prompt variations of the skill body
score            <- run each variation against scenarios, score against rubric
extract          <- identify excellence signals (what made the top output better?)
evolve           <- propose rubric update from excellence pattern, apply it
iterate          <- repeat variate -> score -> extract until dual convergence:
                     (1) all scenarios pass -- trial converged
                     (2) no new excellence patterns -- quest plateaued
golden           <- the prompt variation that achieves dual convergence
```

Dual convergence is the signal that you have found the golden prompt. The rubric at that
point defines what "golden" means for this skill.

---

## Skills

### /quest:rubric

**What**: Define the objective function for a skill. Given a skill spec and sample outputs,
produce a scoring rubric with ranked criteria.
**Input**: Skill spec (the methodology doc), optional sample outputs for calibration
**Output**: Rubric file at `simulations/quest/rubrics/{skill}-rubric-{date}.md`
**Rubric structure**:
- Criteria list: C-01, C-02... each with text, weight (essential/recommended/aspirational),
  category (correctness, depth, format, coverage, behavior), and pass condition
- Starting criteria (3-5): the non-negotiable behaviors the skill must always exhibit
- Rubric version: starts at v1, bumps when /quest:golden adds a criterion
**Lifecycle**:
- Setup: read the skill spec. Identify what the skill promises (what outputs it claims to produce,
  what roles it uses, what the lifecycle phases produce). These become correctness criteria.
- Execute: generate initial criteria. For each phase of the skill lifecycle, ask: what does
  passing look like? What does failure look like? Produce C-01 through C-05 minimum.
- Findings: the rubric document. Criteria ranked: essential (must pass) first, then recommended,
  then aspirational (raise the bar once essential criteria are stable).
- Amend: user can add, remove, reweight, or reword criteria. Rubric is a living document --
  it grows as /quest:golden discovers excellence patterns.
**Example** (rubric for scout-competitors):
```
C-01 [essential]: Matrix includes "none / status quo" as explicit competitor row
C-02 [essential]: Whitespace identified (space with no existing solution)
C-03 [essential]: Table stakes listed (features product must have to compete)
C-04 [recommended]: Threat level assessed per competitor (HIGH/MEDIUM/LOW)
C-05 [recommended]: Inertia framed as the primary competition risk
C-06 [aspirational]: GTM difficulty quantified per competitor
```

---

### /quest:variate

**What**: Generate N distinct prompt variations of a skill body. Each variation is a complete,
runnable skill body -- not a diff. Variations test different design choices independently.
**Input**: Skill spec, variation axes to explore, N (default 5)
**Output**: N skill body variations, each labeled V-01 through V-0N with its variation axis
**Variation axes** (each is a dimension of choice in skill body design):
- Role sequence: which roles run first, what order, which roles are included/excluded
- Output format: table vs. prose vs. list, level of detail per section, scoring scale
- Lifecycle emphasis: how much space each phase gets, how explicit the phase boundaries are
- Phrasing register: formal/technical vs. conversational, imperative vs. descriptive
- Stock role selection: PM+Strategy+Architect vs. PM+GTM vs. all 4 vs. Architect-only
- Scoring granularity: 1-5 scale vs. 1-10 scale vs. traffic light vs. qualitative only
**Lifecycle**:
- Setup: read the skill spec. Identify 3 variation axes most likely to affect output quality
  for this skill. For each axis, define 2 poles.
- Execute: generate V-01 through V-0N. Each variation holds all axes constant except one --
  single-axis variation isolates the effect. V-05+ can be combinations.
- Findings: variation table (axis x variation, what changed). Each variation annotated with
  its hypothesis ("V-02 tests whether removing the GTM role improves focus on technical moat").
- Amend: user can add variation axes, fix N, or specify a combination to test.
**Example** (variations for scout-competitors):
```
V-01: Baseline -- PM, Strategy, Architect, GTM in that order
V-02: Role sequence reversed -- GTM first, Architect last
V-03: PM + Strategy only (remove technical roles)
V-04: Add explicit "none / status quo" instruction at role level (not just setup)
V-05: Scoring scale changed from 1-10 to HIGH/MEDIUM/LOW per dimension
```

---

### /quest:score

**What**: Score a set of skill outputs against a rubric. Rank outputs. Identify excellence signals.
**Input**: N skill outputs (V-01 through V-0N results), rubric file
**Output**: Scorecard at `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`
**Scoring protocol**:
- For each output x each criterion: PASS / PARTIAL / FAIL with evidence quote from output
- Composite score per output: sum of (criterion weight x pass score) / total possible
- Ranked leaderboard: outputs sorted by composite score, highest first
- Excellence signals: outputs that score unusually high on a specific criterion (score > mean + 1 sigma)
- Failure patterns: criteria that fail across ALL outputs -- signal that rubric criterion is
  unclear OR that all variations share the same gap (skill design issue, not variation issue)
- Regression signals: outputs that passed in round N-1 but fail in round N (raised bar regression)
**Lifecycle** (always single-pass -- scoring is objective once rubric is defined):
- Read each output, apply each criterion, record evidence. Compute scores. Rank. Extract signals.
**Artifact**: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

### /quest:golden

**What**: Full quest loop to find the golden prompt. Orchestrates rubric, variate, score,
extract, evolve, and repeat until dual convergence.
**Input**: Skill spec, test scenarios (from trace-skill runs), optional existing rubric
**Output**: Golden prompt body + converged rubric + convergence report
**The dual convergence condition**:
- Trial convergence: all test scenarios pass all essential rubric criteria
- Quest plateau: 2 consecutive rounds produce no new excellence patterns (rubric is stable)
- Both required. Trial convergence without quest plateau = rubric still growing = not golden yet.
  Quest plateau without trial convergence = rubric stabilized but skill still failing = redesign.
**Lifecycle**:

Round 0 -- Setup:
- Load or create rubric via /quest:rubric
- Load test scenarios from trace-skill runs (the hand-compiled expected outputs are the ground truth)
- Generate V-01 through V-05 via /quest:variate

Round N -- Execute:
- Run each variation against all test scenarios
- Score via /quest:score -- produce scorecard
- Check trial convergence: do all essential criteria pass?
- Identify excellence signals: which output scored highest on which criterion?
- Extract pattern: what did the excellent output do that others didn't? (QU2)
- Propose rubric update: new criterion C-NN from the pattern (QU3)
- User reviews proposed criterion: approve / reject / reword
- If approved: apply to rubric (version bump), add to subsequent scoring
- Check quest plateau: was a new criterion added? If yes, not plateaued. If no for 2 rounds: plateaued.
- Check dual convergence. If yes: GOLDEN. If no: generate next round variations targeting the gaps.

Findings phase -- Convergence report:
- Round history: what changed each round, what criteria were added, which variations were eliminated
- The golden prompt: the variation body that achieved dual convergence
- The final rubric: criteria C-01 through C-NN, all with evidence from the golden output
- "What made it golden": the key patterns that distinguish the golden prompt from the runner-up

Amend phase:
- User can reject a proposed excellence pattern (keeps rubric lean)
- User can force an additional round even after plateau (test robustness)
- User can add a new test scenario and re-run from the scoring step only

**Artifact**: `simulations/quest/golden/{skill}-golden-{date}.md` (the golden prompt body)
**Artifact**: `simulations/quest/rubrics/{skill}-rubric-final-{date}.md` (the converged rubric)
**Artifact**: `simulations/quest/reports/{skill}-convergence-{date}.md` (the round history)

---

## Roles

Quest has no stock roles in the simulation sense. The "roles" in quest are the rubric criteria --
each criterion is a lens through which output quality is evaluated. The rubric IS the role system.

Custom rubric criteria play the role of custom domain experts: a criterion that asks "does the
output quantify risk per competitor with confidence intervals?" is a domain expert encoded as
a scoring rule.

---

## Artifacts

```
simulations/quest/
  rubrics/
    {skill}-rubric-{date}.md          <- initial rubric (v1)
    {skill}-rubric-final-{date}.md    <- converged rubric (vN)
  scorecards/
    {skill}-scorecard-R{round}-{date}.md
  golden/
    {skill}-golden-{date}.md          <- the golden prompt body
  reports/
    {skill}-convergence-{date}.md     <- round history + what made it golden
```

---

## Cross-Namespace Integration

- **trace-skill -> quest:golden**: trace-skill produces the test scenarios (hand-compiled
  expected outputs). These are the ground truth for quest scoring. A skill that cannot be
  hand-compiled via trace-skill cannot be evaluated by quest.
- **quest:golden -> program.yaml**: the golden prompt body goes into the `description` field
  of the corresponding command in `program.yaml`. `craft generate` bakes it into the SKILL.md.
- **quest:golden -> all namespaces**: every skill in every namespace has a golden prompt
  waiting to be found. Quest is the meta-skill that improves all 48.
- **quest:rubric -> review:design**: a well-designed rubric is itself a design artifact that
  can be reviewed via /review:design. The rubric defines the standard; the review validates
  the standard is correct.

---

## Technique Heritage

Quest is the Signal implementation of the Trial + Quest system from craftworks (Spec 92).

| Craftworks concept | Quest skill |
|-------------------|-------------|
| Trial mode | quest:golden (full loop) |
| Rubric / scoring criteria | quest:rubric |
| Variation generation | quest:variate |
| QU1 (score outputs) | quest:score |
| QU2 (extract pattern) | built into quest:golden |
| QU3 (propose criterion) | built into quest:golden |
| QU4 (apply criterion) | built into quest:golden |
| Dual convergence | convergence condition in quest:golden |

The key difference: craftworks trial mode requires the compiler pipeline. Quest is a Signal
skill -- anyone can run it with zero setup beyond the trace-skill scenarios and a rubric.
