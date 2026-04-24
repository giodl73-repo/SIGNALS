---
skill: quest-variate
skill_target: quest-golden
round: 1
date: 2026-03-16
rubric: simulations/quest/rubrics/quest-golden-rubric-v1-2026-03-16.md
rubric_version: v1
---

# quest-golden — Round 1 Variations (V-01 through V-05)

Generated against rubric v1 (10 criteria, C-01..C-10).
Single-axis variations for V-01 through V-04. Combination for V-05.

**Axes covered:**
- V-01: role-sequence — 6 named roles in fixed execution order per round
- V-02: output-format — tables throughout (scoreboard, round log, criterion proposals)
- V-03: lifecycle-emphasis — 4 hard phase gates with explicit ENTRY/PROCEDURE/EXIT per round
- V-04: phrasing-register — conversational/intent-first; describes WHY each step matters
- V-05: combination — inertia-framing (named baseline competitor) + lifecycle-emphasis (phase gates)

---

## V-01 — Role Sequence

**axis:** role-sequence
**hypothesis:** Assigning each loop phase to a named role (RUBRIC KEEPER, VARIATOR, SCORER,
ANALYST, CRITERION AUTHOR, CONVERGENCE JUDGE) with strict execution order structurally
enforces C-04 (QU2 precedes QU3) — the ANALYST role must complete before CRITERION AUTHOR
runs, making QU2-before-QU3 a sequencing property rather than a compliance instruction. Also
strengthens C-05 by making RUBRIC KEEPER the first role that executes. Risk: naming roles may
produce role-blending in practice; the hypothesis is falsifiable if ANALYST and CRITERION AUTHOR
sections merge in outputs.

---

Find the golden prompt for a target skill through systematic variation and scoring.

The loop has six roles. Each role executes in strict sequence per round. Do not merge or skip a role.

### RUBRIC KEEPER

Runs once at loop start and again after any approved criterion.

At start: load the rubric for the target skill from `simulations/quest/rubrics/`. If no rubric
exists, invoke quest-rubric to create one. Confirm: rubric file path and criteria count recorded
before proceeding.

After QU4 approval: write the updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md` with incremented version number.

### VARIATOR

Generate 5 complete, runnable prompt body variations for the target skill. Each variation is
the full prompt body text — not a diff, not a summary, not a label. Label each variation with:
- **Axis:** what single dimension is being varied (single axis first; combinations in later rounds)
- **Hypothesis:** what you expect this axis to improve

### SCORER

Load the current rubric. For each variation: evaluate every criterion (pass/fail with one-line
evidence). Compute composite score using the rubric formula. Produce a ranked leaderboard. State
the top variation and the score gap to second place.

### ANALYST (QU2)

Compare the top variation against the second-highest variation only. Name the specific observable
output difference: what did the top variation produce that the second lacked? The signal is a
contrast, not a property list. Name it: `SIGNAL-R{N}: {name}`. If no distinguishing difference
exists, name it `none`.

### CRITERION AUTHOR (QU3)

Execute only if ANALYST named a signal (not `none`). Propose a rubric criterion that captures
the excellence signal. The proposal must include:
- **Text:** one sentence stating what the criterion measures
- **Tier:** essential / recommended / aspirational
- **Pass condition:** LOCATION (where in the output) + OBSERVABLE (what to look for) +
  STANDARD (pass vs fail threshold)

Present to user for approval (QU4). If approved: invoke RUBRIC KEEPER to write the updated
rubric. If rejected: note the reason and continue.

### CONVERGENCE JUDGE

Check both convergence conditions simultaneously:
1. **Trial convergence:** every variation passes all essential criteria in the current rubric.
2. **Quest convergence:** this round's excellence signal was `none` AND the previous round's
   excellence signal was also `none`.

Both must be true. If both true: proceed to Golden Output. If either is false: return to
VARIATOR for the next round.

---

### Per-Round Record

Write one table row per round:

| Round | Variations | Top score | Excellence signal | Criterion added |
|-------|------------|-----------|-------------------|-----------------|
| R-01  | V-01..V-05 | NN        | SIGNAL-R01 or none | C-NN or none |

---

### Golden Output (at dual convergence only)

Write two artifacts:

**Golden prompt** — `simulations/quest/golden/{skill}-golden-{date}.md`
Full converged prompt body verbatim. Not a label. Not a summary. Immediately after the body,
include a "What Made It Golden" section: for each structural mechanism discovered, state the
round it was found and the output gap it closed.

**Final rubric** — `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`
All criteria, composite formula, denominator, golden threshold, version history. Standalone
file — not embedded in the golden file.

List any criteria with zero activations across all rounds as ablated, with a suggested probe
for each. If none, write "No ablated criteria."

---

## V-02 — Output Format (Tables Throughout)

**axis:** output-format
**hypothesis:** Fixed-column tables for round records, scoring, and criterion proposals map
directly to the four C-06 fields (variation IDs, top score, signal, criterion), making
dual convergence checkable by column inspection. This raises C-06, C-07 (contrast column
enforces isolation), and C-08 (proposal table enforces all three fields). Risk: prose
variations may still outscore on C-09 (mechanism narrative) where free-form text is richer.

---

Find the golden prompt for a target skill through systematic variation, tabular scoring, and
rubric evolution.

### Setup

Load the rubric for the target skill from `simulations/quest/rubrics/`. If no rubric exists,
invoke quest-rubric to create one. Record rubric path and version before proceeding.

### Loop — repeat until dual convergence

Each round produces three tables and one decision.

#### Table 1 — Variations

Generate 5 complete, runnable prompt body variations for the target skill. Each variation is
the full prompt body text — no diffs, no summaries. Single-axis first; combinations in later rounds.

| ID   | Axis | Hypothesis |
|------|------|------------|
| V-01 | ...  | ...        |
| V-02 | ...  | ...        |
| V-03 | ...  | ...        |
| V-04 | ...  | ...        |
| V-05 | ...  | ...        |

#### Table 2 — Scoreboard

Score each variation against every rubric criterion. One row per variation, one column per
criterion. Compute composite using the rubric formula. Rank 1 = highest composite.

| ID   | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Composite | Rank |
|------|------|------|------|------|------|------|------|------|------|------|-----------|------|
| V-01 | P/F  | P/F  | P/F  | P/F  | P/F  | P/F  | P/F  | P/F  | P/F  | P/F  | NN        | #N   |
| V-02 | ...  |      |      |      |      |      |      |      |      |      |           |      |
| V-03 | ...  |      |      |      |      |      |      |      |      |      |           |      |
| V-04 | ...  |      |      |      |      |      |      |      |      |      |           |      |
| V-05 | ...  |      |      |      |      |      |      |      |      |      |           |      |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)

#### Table 3 — Excellence Signal and Criterion (QU2 then QU3)

Compare rank-1 against rank-2. Name the observable output difference (QU2).

| Round | Rank-1 | Rank-2 | Gap | Signal (QU2) |
|-------|--------|--------|-----|--------------|
| R-NN  | V-XX   | V-YY   | +NN | SIGNAL-RNN: {name} or none |

If a signal was found, propose a criterion (QU3). Three fields required:

| Field             | Value |
|-------------------|-------|
| Criterion text    | ...   |
| Tier              | essential / recommended / aspirational |
| Pass: LOCATION    | ...   |
| Pass: OBSERVABLE  | ...   |
| Pass: STANDARD    | ...   |

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

#### Convergence Check

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

### Round Log

Append one row per round:

| Round | Variations | Top score | Signal | Criterion |
|-------|------------|-----------|--------|-----------|
| R-01  | V-01..V-05 | NN        | SIGNAL or none | C-NN or none |

### Golden Output (at dual convergence only)

**Golden prompt** — `simulations/quest/golden/{skill}-golden-{date}.md`
Full converged prompt body verbatim. Followed by "What Made It Golden": each structural
mechanism, the round it was discovered, and the output gap it closed.

**Final rubric** — `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`
All criteria, composite formula, denominator, golden threshold, version history. Standalone file.

**Ablation table:**

| Criterion | Activation count | Probe suggestion |
|-----------|-----------------|------------------|
| C-NN      | 0               | ...              |

Write "No ablated criteria" if all criteria activated at least once.

---

## V-03 — Lifecycle Emphasis (Hard Phase Gates)

**axis:** lifecycle-emphasis
**hypothesis:** Structuring each round as 4 explicit phases (INITIALIZATION, VARIATION,
SCORING, ANALYSIS) with ENTRY CONDITION, PROCEDURE, and EXIT CONDITION per phase prevents
premature convergence declaration (C-01) because you cannot enter ANALYSIS without completing
SCORING (artifact dependency), and you cannot declare dual convergence without completing
ANALYSIS. Also strengthens C-04 because QU2 and QU3 are sequenced steps within ANALYSIS
with named ordering. Risk: verbose phase gates may not improve C-07 or C-09 (depth criteria).

---

Find the golden prompt for a target skill through systematic variation and rubric-grounded
scoring. The loop runs until dual convergence: all essential criteria pass across all variations
AND no new excellence patterns emerge for two consecutive rounds.

---

### PHASE 0 — INITIALIZATION

**Entry condition:** skill name provided.

**Procedure:**
1. Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load the latest version.
2. If no rubric exists: invoke quest-rubric. Do not proceed until rubric is confirmed.
3. Record: rubric path, version, criteria count.

**Exit condition:** rubric artifact confirmed and criteria count > 0.

---

### PHASE 1 — VARIATION

**Entry condition:** Phase 0 complete (rubric loaded).

**Procedure:**
1. Generate 5 complete, runnable prompt body variations for the target skill.
2. Each variation = full prompt body text. No diffs. No summaries.
3. Label each: variation axis (single axis first) + hypothesis (what this axis is expected
   to improve).

**Exit condition:** 5 complete labeled prompt body variations ready for scoring.

---

### PHASE 2 — SCORING

**Entry condition:** Phase 1 complete (variations ready); current rubric loaded.

**Procedure:**
1. For each variation: evaluate every rubric criterion (pass/fail with one-line evidence).
2. Compute composite score per variation using the rubric formula.
3. Rank all variations. Identify: top variation and score gap to second place.

**Exit condition:** ranked leaderboard with per-criterion pass/fail for every variation.

---

### PHASE 3 — ANALYSIS

**Entry condition:** Phase 2 complete (ranked leaderboard available).

**Step QU2 — Excellence Signal Isolation:**

Compare the top variation against the second-highest variation only. Name the specific
observable output difference: what did the top variation contain that the second lacked?
The signal is the contrast, not a description of the winner. Name it: `SIGNAL-R{N}: {name}`.
If no distinguishing difference exists, name it `none`.

**Step QU3 — Criterion Proposal (only if QU2 signal is not `none`):**

Propose a rubric criterion that captures the excellence signal. Required fields:
- **Text:** one sentence stating what the criterion measures
- **Tier:** essential / recommended / aspirational
- **Pass condition:** LOCATION + OBSERVABLE + STANDARD

Present the proposal to the user for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`. If rejected: record reason and
proceed without rubric update.

**Exit condition:** excellence signal named (or `none`); rubric updated if criterion approved.

---

### PHASE 4 — CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

**Procedure:**
Check both conditions simultaneously:

| Condition | Met? |
|-----------|------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |

- If both YES: exit loop and proceed to GOLDEN OUTPUT.
- If either NO: record round log entry and return to PHASE 1.

**Exit condition:** dual convergence declared, or next round initiated.

---

### Round Log

Append one row after each Phase 4:

| Round | Variations | Top composite | QU2 signal | Criterion added |
|-------|------------|--------------|------------|-----------------|
| R-01  | V-01..V-05 | NN           | SIGNAL or none | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**File 1 — Golden prompt**
Path: `simulations/quest/golden/{skill}-golden-{date}.md`
Write the full converged prompt body verbatim. Immediately after the body, include "What Made
It Golden": each structural mechanism discovered, the round it was found, and the output gap
it closed (minimum 2 mechanisms required).

**File 2 — Final rubric**
Path: `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`
All converged criteria, composite formula, denominator, golden threshold, version history.
Standalone file, separate from the golden file.

**Ablated criteria check:** list any criteria with zero activations across all rounds with
a suggested probe for each. If none, write "No ablated criteria."

---

## V-04 — Phrasing Register (Conversational / Intent-First)

**axis:** phrasing-register
**hypothesis:** Describing the intent and reasoning behind each step ("here's what you're
looking for") rather than issuing imperatives produces more reliable QU2/QU3 separation (C-04),
because the model reasons about the goal of the step rather than pattern-matching to instruction
labels. The intent behind "QU2 before QU3" is that criteria must be grounded in observed output
gaps — stating that reasoning directly may embed C-04 compliance rather than requiring it.
Also predicted to improve C-09 (mechanism narrative) because the style invites explanation.
Risk: may weaken C-01 and C-05 where gate precision requires literal conditions.

---

You're here to find the best possible prompt body for a given skill — not just a good one, but
the one where further variation stops improving things. The process is iterative: generate
candidates, score them against a rubric, extract what made the winner better, tighten the rubric
to capture that insight, and repeat until the loop has nothing new to teach you. That stopping
point — where every candidate passes the essential bar and two consecutive rounds produce no new
discoveries — is dual convergence. The converged prompt body is the golden prompt.

**Before the first round**, find the rubric for the target skill at `simulations/quest/rubrics/`.
If one doesn't exist yet, create it by running quest-rubric before doing anything else. The
rubric is the objective function — you can't score without it, and you can't discover excellence
without scoring.

**Each round has four steps:**

*Generate variations.* Write 5 complete, runnable prompt bodies for the skill. Complete means
the full text — not a diff, not a summary, not "like V-03 but with X." Early rounds should vary
one thing at a time (a single axis per variation) with a hypothesis about what that axis might
improve. Later rounds can combine axes. Label each variation with its axis and hypothesis so
the contrast step is grounded.

*Score them.* Apply the current rubric to each variation. For every criterion, mark pass or
fail with a brief note on what you observed. Compute the composite score for each variation
using the rubric formula and rank them. What matters most is who's at the top and how far ahead
they are — that gap is where the signal lives.

*Identify the excellence signal (QU2).* Compare the top variation to the second-place variation
only. What did the winner have that the runner-up didn't? This is a contrast question, not a
description question — you're looking for the observable difference that separated them, not a
list of everything the winner did well. Name it: `SIGNAL-R{N}: {description}`. If you can't
find a meaningful difference beyond scoring noise, name it `none`. The signal must come before
any criterion proposal — a criterion not grounded in an observed output gap is guesswork, not
discovery.

*Propose a criterion (QU3), if you found a signal.* Translate the excellence signal into a
rubric criterion. Every proposal needs three things: what the criterion measures (the text),
how much it should count (tier: essential, recommended, or aspirational), and what a passing
output looks like (location in the output, what to look for, and what distinguishes pass from
fail). Present the proposal for approval (QU4). If approved, write the updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md` with an incremented version number.
If rejected, note why and continue.

**Check for dual convergence after each round.** Two conditions, both required:
- Every variation passes every essential criterion in the current rubric (trial convergence).
- This round's signal was `none` and so was the previous round's (quest convergence).

If both are met, you're done. If either is missing, run another round.

**Keep a round log** throughout. After each round, record: which variations were scored, the
top composite score, what the excellence signal was (or `none`), and what criterion was added
(or `none`). This log is the audit trail for the convergence claim.

**At dual convergence**, write two things:

The golden prompt file at `simulations/quest/golden/{skill}-golden-{date}.md`. This is the full
verbatim text of the converged prompt body — not a summary, not a label, the complete runnable
text. Include a "What Made It Golden" section immediately after: for each structural mechanism
the loop discovered, say which round found it and what output gap it closed.

The final rubric at `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`. This is a
standalone artifact with all converged criteria, the composite formula, the denominator, the
golden threshold, and the version history. Keep it separate from the golden file — it's the
theory of excellence, and the golden prompt is the evidence.

One last thing: check for ablated criteria — any criterion that was proposed but never activated
across all rounds. List each with a suggested probe for how to activate it. If none exist, say
so explicitly.

---

## V-05 — Combination: Inertia Framing + Lifecycle Emphasis

**axis:** inertia-framing + lifecycle-emphasis (combination)
**hypothesis:** Naming the unconstrained baseline ("what a capable model produces without this
loop") as INERTIA and using it as the primary comparator for QU2 produces sharper excellence
signal extraction (C-07) — the contrast reveals what the loop adds, not just what one variation
does better. Adding explicit phase gates (ENTRY/PROCEDURE/EXIT) anchors the inertia comparison
within PHASE 3 so it cannot be absorbed into generic scoring prose. Combined, these should also
improve C-09 (mechanism narrative) because "what made it golden" naturally becomes "what
inertia missed." Risk: two axes may suppress single-axis signal isolation in subsequent rounds.

---

Find the golden prompt for a target skill by systematically outcompeting inertia — the
unconstrained baseline a capable model produces without variation, rubric, or iteration. The
goal is dual convergence: all essential criteria passing across all variations AND no new
improvements over inertia discoverable for two consecutive rounds. The converged prompt body
is the golden prompt.

---

### PHASE 0 — SETUP

**Entry condition:** skill name provided.

**Procedure:**
1. **Name the inertia prompt.** Write a brief (one paragraph) description of the prompt body
   a capable model would produce for this skill without any quest-golden loop: no rubric, no
   variation axis, no convergence logic. This is your primary competitor. It sets the floor all
   variations must beat.
2. **Load the rubric.** Glob `simulations/quest/rubrics/{skill}-rubric-*.md`. Load the latest
   version. If none exists: invoke quest-rubric before proceeding. The rubric defines what
   "beating inertia" means in measurable terms.
3. Record: inertia baseline summary, rubric path, version, criteria count.

**Exit condition:** inertia baseline documented and rubric loaded.

---

### PHASE 1 — VARIATION

**Entry condition:** Phase 0 complete.

**Procedure:**
Generate 5 complete, runnable prompt body variations for the target skill. Each variation =
full prompt body text. No diffs. No summaries. Single-axis first; combinations in later rounds.

Label each:
- **Axis:** what single dimension is being varied
- **Hypothesis:** how this axis is expected to outperform inertia
- **Inertia delta:** in one phrase, what this variation adds or changes vs the inertia baseline

**Exit condition:** 5 labeled, complete prompt body variations ready.

---

### PHASE 2 — SCORING

**Entry condition:** Phase 1 complete; current rubric loaded.

**Procedure:**
Score each variation against every rubric criterion (pass/fail with evidence). Compute
composite scores using the rubric formula. Add the inertia baseline as a pseudo-variation
scored against the same rubric.

| Rank | ID      | Composite | vs Inertia | Notes |
|------|---------|-----------|------------|-------|
| 1    | V-XX    | NN        | +NN        | ...   |
| ...  | ...     | ...       | ...        | ...   |
| —    | INERTIA | NN        | baseline   | unconstrained |

**Exit condition:** ranked leaderboard with inertia baseline anchoring the comparison.

---

### PHASE 3 — ANALYSIS (QU2 then QU3)

**Entry condition:** Phase 2 complete (leaderboard available, including inertia row).

**Step QU2 — Excellence Signal Isolation:**

Compare the top variation against two references:
1. The second-ranked variation (within-field contrast)
2. The inertia baseline (inertia contrast)

Name what the top variation had that neither the runner-up NOR the inertia baseline had. This
is the pure excellence signal — something the loop discovered that unconstrained generation
misses. Name it: `SIGNAL-R{N}: {name}`.

The inertia contrast is the more important of the two. A variation that beats the runner-up but
matches inertia on the new dimension is not producing a genuine discovery. If no such difference
exists, name it `none`.

**Step QU3 — Criterion Proposal (only if QU2 signal is not `none`):**

Propose a rubric criterion that captures the excellence signal. Required fields:
- **Text:** what the criterion measures
- **Tier:** essential / recommended / aspirational
- **Pass condition:** LOCATION + OBSERVABLE + STANDARD

Present for approval (QU4). If approved: write updated rubric to
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`.

**Exit condition:** excellence signal named with inertia contrast; rubric updated if approved.

---

### PHASE 4 — CONVERGENCE CHECK

**Entry condition:** Phase 3 complete.

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES / NO |
| Quest convergence: this round signal = none AND previous round signal = none | YES / NO |
| **Dual convergence** | **YES (exit) / NO (next round)** |

---

### Round Log

| Round | Top | vs Inertia | QU2 signal | Criterion |
|-------|-----|------------|------------|-----------|
| R-01  | V-XX | +NN       | SIGNAL or none | C-NN or none |

---

### GOLDEN OUTPUT (Phase 4 dual convergence only)

**Golden prompt** — `simulations/quest/golden/{skill}-golden-{date}.md`
Full converged prompt body verbatim. Followed by "What Made It Golden": each structural
mechanism, the round it was discovered, and the specific inertia gap it closed.

**Final rubric** — `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`
All criteria, composite formula, denominator, golden threshold, version history. Standalone file.

**Ablated criteria:** list any criteria with zero activations across all rounds with a suggested
probe. If none, write "No ablated criteria."
