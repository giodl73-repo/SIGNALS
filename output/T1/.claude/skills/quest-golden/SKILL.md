---
name: quest-golden
description: "Find the golden prompt for any Signal skill in a single session. Runs the full quest loop: rubric -> variate -> score -> extract -> evolve -> converge. No external scripts needed. Works for customers."
allowed-tools: [Read, Write, Glob, Grep]
---

# /quest:golden -- Find the Golden Prompt

You are running the quest loop to find the golden prompt for a Signal skill.
The golden prompt is the skill body formulation that achieves DUAL CONVERGENCE:
all essential rubric criteria pass AND no new excellence patterns emerge for
2 consecutive rounds.

This entire loop runs in ONE session. You hold all state in context.
Do not ask for external tools or scripts. Reason through each step.

---

## Setup

Read the following (use Read tool):
1. `signal.skills.yaml` -- find the skill entry for the requested skill ID
2. Any trace artifact in `simulations/trace/skill/` matching the skill name
3. Any existing rubric in `simulations/quest/rubrics/` for this skill

If no trace artifact exists: derive ground truth from the skill description alone.
If no rubric exists: generate one now (see Round 0 below).

---

## Round 0: Generate Rubric (if none exists)

From the skill description and trace artifact, generate a scoring rubric:

**Essential criteria (3-5)**: What must ALWAYS be true for the output to be useful?
- Each criterion: ID (C-01...), text, pass condition (specific, not vague)
- Failure on any essential criterion = output is not useful

**Recommended criteria (2-3)**: What makes the output better?

**Aspirational criteria (1-2)**: What raises the bar after the essentials are stable?

**Composite score formula**:
(essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)

**Golden threshold**: all essential pass + composite >= 85

Write rubric to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

---

## Round N: Variate -> Score -> Check

### Step 1: Generate 5 Variations

Generate V-01 through V-05. Each is a COMPLETE, RUNNABLE skill body -- not a diff.
Single-axis variation: test one design choice at a time.

Axes to test (pick 3 for single-axis, combine later):
- **Inertia prominence**: How prominently is "none / status quo" featured?
- **Output structure**: Insight-first (narrative) vs evidence-first (matrix)?
- **Role sequence**: Which role runs first and sets the frame?
- **Phrasing register**: Directive ("Do X") vs descriptive ("The skill does X")?
- **WebSearch explicitness**: Is the instruction to use WebSearch explicit or implied?
- **Amend specificity**: Generic ("adjust scope") vs specific ("change X, see Y change")?

Label each variation: `V-01: [axis] -- [hypothesis about why this is better]`

### Step 2: Score All 5 Variations

For each variation (V-01 through V-05):
- Evaluate each criterion: PASS / PARTIAL / FAIL + one-line evidence
- Compute composite score
- Note what this variation does that others don't

Produce a ranked leaderboard.

### Step 3: Check Convergence

**Excellence signals**: Does any variation score unusually high on a specific criterion
that others miss? Name the pattern: what did it DO differently?

**Convergence check**:
- Trial converged? All essential criteria pass in the top variation? YES/NO
- Quest plateaued? Are there excellence signals worth adding to the rubric? YES/NO

**If BOTH are YES for 2 consecutive rounds**: DUAL CONVERGENCE. Go to Final Step.
**If trial not converged OR new signals exist**: evolve rubric, increment round, repeat.

### Step 4: Evolve Rubric (if new signals)

For each excellence signal: add a new aspirational criterion (C-NN).
Bump rubric version. The new criterion captures what made the excellent output excellent.
Write updated rubric.

---

## Final Step: Write the Golden Prompt

When dual convergence is achieved:

1. Identify the winning variation (highest score, all essential pass)
2. Write the golden prompt document to `simulations/quest/golden/{skill}-golden-{date}.md`:

```
---
skill: quest-golden
skill_target: {skill}
date: {date}
rounds: {N}
rubric_final: {rubric file}
score: {composite score}
status: GOLDEN
---

# Golden Prompt: {skill}

## The Prompt Body
[exact text of the winning variation -- this goes into signal.skills.yaml]

## What Made It Golden
[3-5 key patterns that distinguish it from V-01 baseline]

## Final Rubric Summary
[C-01 through C-NN with pass conditions]
```

3. Tell the user: "GOLDEN found in {N} rounds, score {X}. Update signal.skills.yaml
   description for {skill} with the prompt body above. Then run craft generate."

---

## Example Session Flow

```
User: /quest-golden scout-naming

> Reading signal.skills.yaml for scout-naming...
> Found trace: simulations/trace/skill/plugin-scout-naming-2026-03-14.md
> No existing rubric -- generating Round 0 rubric...

Round 0: Rubric generated (v1) -- 5 essential, 3 recommended, 2 aspirational.
Written: simulations/quest/rubrics/scout-naming-rubric-2026-03-14.md

Round 1: Generating 5 variations...
  V-01: Baseline (spec as written)
  V-02: --validate flag prominent in setup
  V-03: Collision check runs before scoring (not after)
  V-04: Strategy role removed (PM+Design+UX+GTM only)
  V-05: Insight-first: top pick announced before matrix

Scoring Round 1...
  V-05: 78 (top) -- C-06 PASS (top pick prominent), C-07 FAIL (no WebSearch)
  V-02: 72 -- C-08 PASS (--validate flag explicit)
  V-01: 60 -- baseline

Excellence signal ES-01: V-05 announces top pick before the matrix -- forces
  the narrative structure. Add C-09: "Top recommendation stated before matrix."

Round 1: not converged (C-07 fails all, new signal ES-01). Evolving rubric to v2.

Round 2: Generating 5 variations incorporating ES-01 + explicit WebSearch...
  V-06: V-05 + WebSearch explicit + C-09 criterion
  V-07: V-06 + --validate flag prominent

Scoring Round 2...
  V-06: 92 (top) -- all essential PASS, C-07 PASS, C-09 PASS
  V-07: 91

Excellence signals Round 2: none.
Round 2: TRIAL CONVERGED, QUEST PLATEAUED (count 1/2).

Round 3: Re-run to confirm plateau...
  V-06 variant: 93. No new signals. PLATEAU CONFIRMED (count 2/2).

DUAL CONVERGENCE in Round 3. Golden prompt = V-06 body.
Writing: simulations/quest/golden/scout-naming-golden-2026-03-14.md

GOLDEN found in 3 rounds, score 93.
Update signal.skills.yaml description for scout-naming with the prompt body above.
```
