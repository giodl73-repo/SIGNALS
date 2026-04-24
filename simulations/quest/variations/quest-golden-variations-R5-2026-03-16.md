Now I have full context. Round 5 is the **confirmation round** — R4 found zero new patterns (first zero-pattern round). R5 must also find zero to declare QUEST PLATEAUED. The variations should push into unexplored territory to maximize the chance of surfacing any remaining hidden patterns.

---

# quest-golden — Round 5 Variations

**Skill:** quest-golden
**Rubric:** v4 (18 criteria)
**Round:** 5 (confirmation round — plateau requires R5 zero patterns to match R4 zero patterns)
**Champion entering this round:** R4 V-05 at 100/100

---

## SPREAD-DESIGN

Entering R5 with all prior axes (C-15 through C-18) already codified. New axes target unexplored territory.

| Variation | Axis | Hypothesis | Criteria primarily targeted | Distinct from others? |
|-----------|------|-----------|----------------------------|----------------------|
| V-01 | Lifecycle emphasis — expanded convergence gate | The convergence check is the most consequential decision in the loop yet currently the most compressed phase. Giving it 6 explicit sub-steps with named failure modes and anti-patterns makes compliance harder to shortcut and GATE 2 harder to satisfice. If a new pattern exists, it lives here. | C-01, C-11, C-16 | YES |
| V-02 | Phrasing register — conversational imperative | All prior rounds used PHASE/STEP formal headers. Replacing them with numbered plain-English imperatives + "because" rationales tests whether all 18 mechanisms are truly structural (survives format change) or partly format-dependent. | All 18, stress test | YES |
| V-03 | Inertia framing — V-00 as permanent scored competitor | Prior variations reference inertia in the delta field but never score it explicitly. Making V-00 a column in every scoring table (named, scored, always present) tests whether naming the baseline sharpens contrast enforcement and discovery identification. | C-12, C-14, C-07 | YES |
| V-04 | V-01 + V-02 + V-03 combined | Tests interaction effects among expanded convergence gate, conversational register, and V-00 scoring. Some axes may be synergistic; others may conflict. | All | YES |
| V-05 | Full synthesis: R4 champion + R5 V-01 + R5 V-03 | R4 V-05 champion body integrated with expanded convergence gate and V-00 baseline scoring. Conversational register (V-02) held out because formal headers are more auditable; V-02 integration covered by V-04. | All 18 | YES |

**Spread gate:** No two variations share the same primary axis. V-05 synthesizes V-01 and V-03 (two strongest structural additions). V-04 covers all three for interaction testing. V-02 is a pure format probe — if it scores 100/100 with a different register, that confirms format independence of the criteria.

**Prior round PARTIAL near-misses:** None from R4 (all variations scored PASS or FAIL with no PARTIAL). No trajectory carry-forward needed.

---

## V-01 — Lifecycle Emphasis: Expanded Convergence Gate

**Axis:** Lifecycle emphasis — convergence gate expansion
**Hypothesis:** The convergence check is currently the most consequential phase in the loop yet occupies proportionally the least structural space. Expanding it to 6 sub-steps with explicit failure modes, anti-pattern inventory, and a fill-in-the-blank citation template forces the executor to show their work at the exit point, making GATE 2 harder to satisfice through vague language.

---

```
# quest-golden

Find the golden prompt for a skill through systematic variation, scoring, and
pattern extraction. The loop terminates at dual convergence: trial convergence
(all essential criteria pass) AND quest convergence (no new excellence signals
for two consecutive named rounds). The convergence check is the only exit point.

---

## LOOP ENTRY

### Load rubric

Read `simulations/quest/rubrics/{skill}-rubric-*.md`. Identify the latest
version. Record: rubric version, criterion count by tier, composite formula,
golden threshold.

If no rubric exists: call quest-rubric first. Do not proceed without a loaded
rubric.

---

## EACH ROUND

### SPREAD-DESIGN

Entry condition: rubric loaded.

Before writing any variation body, complete this table:

| Variation | Axis | Hypothesis (which criterion changes, predicted direction) | Criteria targeted |
|-----------|------|----------------------------------------------------------|-------------------|
| V-01      |      |                                                          |                   |
| V-02      |      |                                                          |                   |
| V-03      |      |                                                          |                   |
| V-04      |      |                                                          |                   |
| V-05      |      | synthesizes V-[X], V-[Y], V-[Z]                          |                   |

Check: do any two rows share the same axis? If yes, reassign before continuing.
V-05 must synthesize the three strongest single-axis hypotheses from V-01..V-04.

DO NOT write any variation body until the SPREAD-DESIGN table is complete
and confirmed.

### Step 1 — Generate variations

Write V-01 through V-05 as complete, runnable skill bodies. Each must be
self-contained — a full prompt, not a diff. Label each with its axis and
hypothesis.

### Step 2 — Score

**2a — Pre-commit evaluation structure (runs before scoring):**

Print this skeleton matrix before scoring any variation. This commits to the
evaluation structure for this round. Any criterion absent from this skeleton
cannot receive a valid score.

DO NOT score any variation until this skeleton is printed.

| Criterion | Tier | Pass condition (one sentence) |
|-----------|------|-------------------------------|
[one row per criterion in the active rubric]

**2b — Per-variation evidence:**

For each variation, for each criterion: PASS / PARTIAL / FAIL with one sentence
of justification.

**2c — Fill the pre-committed skeleton:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|

| Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|

### Step 3 — Round log entry

Append one row to the iteration history (do not replace prior rows):

| Round | Variation IDs | Top composite | Patterns found | PARTIAL near-misses | Criterion added |
|-------|--------------|---------------|----------------|---------------------|-----------------|

PARTIAL near-misses: list criteria where any variation scored PARTIAL. Mark
trajectory: up-arrow (improved from prior round), down-arrow (regressed), "new"
(first appearance this round).

Before designing next round's spread, consult the PARTIAL column. Near-miss
criteria are productive leads for targeted variation axes.

### Step 4 — Excellence extraction (QU2)

DO NOT proceed to Step 5 until extraction is complete for ALL signals this
round. This gate exists because criterion proposals derived without a named
structural gap are editorial guesses, not loop discoveries.

For the top variation vs the runner-up:

| Field                 | Value |
|-----------------------|-------|
| TOP HAD               | [structural element present in the top variation]           |
| SECOND LACKED         | [that element absent in runner-up — state absence, not quality judgment] |
| INERTIA LACKED        | [that element absent from inertia baseline — this is the discovery]      |
| Round first seen      | [round number, or "this round"]                             |

If no structural gap can be identified between top and runner-up: signal = none.

### Step 5 — Criterion proposal (QU3)

Gated: QU3 requires a named QU2 signal. If signal = none: write "QU3: no
criterion proposed this round." Proceed to Step 6.

If signal is named: propose a criterion with all five components:
- Criterion text (what the prompt must contain)
- Tier with rationale (essential = wrong without it; recommended = better with
  it; aspirational = excellent)
- LOCATION: where in the prompt body to look for this criterion
- OBSERVABLE: what to observe — the specific textual or structural evidence
- STANDARD: pass condition (one sentence) and fail condition (one sentence)

Present the proposal. Await QU4 approval. Do not apply to the rubric until
the user approves.

---

## CONVERGENCE CHECK

This phase runs after Step 5 in every round. It is the only place the loop
exits. Work through each sub-step in order.

### C1 — Identify current round

State: "Current round: R-[N]."

### C2 — Extract current round signal

Read Row R-[N] from the iteration history. State:
"Round R-[N]: patterns found = [names of patterns, or 'none']."

### C3 — Extract prior round signal

Read Row R-[N-1] from the iteration history. State:
"Round R-[N-1]: patterns found = [names of patterns, or 'none']."

If R-[N-1] does not exist in the log: write "R-[N-1] not in log. GATE 2 is
UNRESOLVABLE." GATE 2 = FAIL. Do not proceed to C5.

### C4 — Evaluate GATE 1: trial convergence

PASS if: all variations (V-01 through V-05) pass all essential criteria in
R-[N], AND all variations passed all essential criteria in R-[N-1].

Failure modes that invalidate GATE 1:
- Any essential criterion fails for any variation in either round
- R-[N-1] is not in the iteration log

State: "GATE 1 = [PASS / FAIL]. Reason: [one sentence]."

### C5 — Evaluate GATE 2: quest convergence (plateau)

PASS if: Round R-[N] patterns = none AND Round R-[N-1] patterns = none.

Anti-patterns that do NOT satisfy GATE 2 — these phrases cannot appear in a
valid convergence declaration:
- "Both recent rounds found zero patterns" (no round numbers)
- "The last two rounds showed no signals" (no round numbers)
- Citing only one round
- Citing rounds not present in the iteration history

Required citation format:
"Round R-[N]: patterns = [value]. Round R-[N-1]: patterns = [value]."

State: "GATE 2 = [PASS / FAIL]. Citation: Round R-[N] = [value]. Round
R-[N-1] = [value]."

### C6 — Termination decision

If GATE 1 = PASS AND GATE 2 = PASS:
  TRIAL CONVERGED AND QUEST PLATEAUED.
  Proceed to WRITE GOLDEN ARTIFACTS.

If either gate = FAIL or UNRESOLVABLE:
  Loop continues.
  Present round summary to user. Await instruction to proceed to next round.
  Do not exit on GATE 1 alone.
  Do not exit on a single round of none.
  Both gates. Both rounds. Named.

---

## WRITE GOLDEN ARTIFACTS (only at dual convergence)

**1. Golden prompt.**
Write the full verbatim skill body to:
  simulations/quest/golden/{skill}-golden-{date}.md
Not a summary. Not a description. Complete, copy-pastable text.

**2. Final rubric.**
Write the accumulated rubric to:
  simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
Contents: all converged criteria with text, tier, and three-part pass conditions;
composite formula with current denominator; golden threshold; version history.

**3. "What Made It Golden" section.**
Minimum 2 structural mechanisms. For each:
  (a) the round in which the mechanism was first discovered
  (b) the inertia gap it closed
  (c) the criterion it activated

**4. "Ablated criteria" section.**
List criteria with zero activations across all rounds, with a suggested targeted
probe per criterion. If none: write "No ablated criteria."

State: "Golden prompt written. Final rubric written. Quest complete."
```

---

## V-02 — Phrasing Register: Conversational Imperative

**Axis:** Phrasing register — full conversational imperative (no PHASE/STEP headers)
**Hypothesis:** All prior rounds used formal PHASE/STEP labels. If the 18 criteria are truly structural (not format-dependent), they should survive a complete register change to numbered plain-English imperatives with inline "because" rationales. If a criterion drops under the register change, that signals format-dependence worth surfacing as a new pattern.

---

```
# quest-golden

Your job: find the golden prompt for a skill by running a systematic loop of
variation, scoring, and pattern extraction. You stop when two conditions are
both true: all essential criteria are passing, and no new excellence signals
have appeared for two consecutive named rounds.

Here is how to run the loop, step by step.

---

**Before each round, do this once at the start:**

**1. Load the rubric.**
Find `simulations/quest/rubrics/{skill}-rubric-*.md` and read the latest
version. Write down: rubric version, criterion count by tier, the composite
formula, and the golden threshold. No rubric means no scoring — run quest-rubric
first before proceeding.

**2. Design the spread before writing anything.**
You need five variations. Before writing a single word of variation text,
fill in this table. Each row is a commitment.

| Variation | Axis | Hypothesis: what changes and why | Criteria targeted |
|-----------|------|----------------------------------|-------------------|
| V-01      |      |                                  |                   |
| V-02      |      |                                  |                   |
| V-03      |      |                                  |                   |
| V-04      |      |                                  |                   |
| V-05 (synthesis) | | combines V-[X] + V-[Y] + V-[Z] |              |

Check every pair of rows: if two variations share the same axis, replace one.
V-05 must synthesize the three strongest single-axis results. Do not write any
variation body until every row is filled and the axes are distinct.

**3. Pre-commit the scoring criteria.**
Before writing any variation, print the full scoring matrix. This is a
commitment — once variation generation starts, nothing can be added.

| Criterion | Tier | Pass condition |
|-----------|------|----------------|
[one row per rubric criterion]

Do not score any variation before printing this.

**4. Write the five variations.**
V-01 through V-05 as complete, runnable skill bodies. Full text, not diffs.
Label each with its axis and hypothesis.

**5. Score each variation.**
Use the pre-committed matrix. For every variation x criterion: PASS, PARTIAL,
or FAIL with one sentence of evidence. Then fill in:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|

| Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|

**6. Log this round.**
Add one row to the iteration history:

| Round | Variation IDs | Top composite | Patterns found | PARTIAL near-misses | Criterion added |
|-------|--------------|---------------|----------------|---------------------|-----------------|

For PARTIAL near-misses: list any criterion where any variation scored PARTIAL.
Mark trajectory with an up-arrow (improved), down-arrow (regressed), or "new"
(first appearance). Before designing the next round's spread, check this column
first — partial-pass criteria are near-misses and productive leads.

**7. Extract the excellence signal. Do this before proposing any criterion.**
This step exists because a criterion proposal not grounded in an observed output
gap is an editorial guess, not a loop discovery.

Find the structural element that separates the top variation from the runner-up:

| TOP HAD          | [structural element present in the top variation]                |
| SECOND LACKED    | [that element absent in runner-up — state the absence]           |
| INERTIA LACKED   | [that element absent from the inertia baseline — the discovery]  |
| Round first seen | [round number, or "this round"]                                  |

If no structural element distinguishes top from runner-up: signal = none.
Do not proceed to step 8 until this block is complete.

**8. Propose a criterion only if step 7 found a new signal.**
Signal = none means "QU3: nothing to propose this round." Skip to step 9.

If you found a signal: write a criterion proposal with these five parts:
- What the prompt must contain (criterion text)
- Which tier it belongs to and why (essential = wrong without it; recommended =
  better with it; aspirational = excellent)
- LOCATION: where in the prompt to find the evidence
- OBSERVABLE: the specific textual or structural evidence to look for
- STANDARD: one-sentence pass condition, one-sentence fail condition

Wait for the user to approve before adding it to the rubric.

**9. Check convergence. This is the only way out of the loop.**
You need two independent conditions, both true, to exit.

First condition (trial convergence): all five variations passed all essential
criteria this round. Check your scoring table.

Second condition (quest convergence, plateau): no new patterns were found this
round AND no new patterns were found in the prior round. You must name both
rounds and state their signal values, traceable to the iteration history:

"Round R-[N]: patterns = [names or 'none']. Round R-[N-1]: patterns = [names
or 'none']."

Phrases that do NOT satisfy this condition:
- "Both recent rounds found zero patterns." (no round numbers)
- "The last two rounds were clean." (no round numbers)
- Citing only one round's evidence

If the prior round is not yet in the iteration log: second condition = not
resolvable. Keep running.

If both conditions are true: proceed to step 10.
If either is false or unresolvable: tell the user what happened this round and
wait for instructions to continue.

**10. Write the golden artifacts. Only when step 9 says both conditions are met.**

Write the golden prompt as a complete, deployable skill body to
`simulations/quest/golden/{skill}-golden-{date}.md`. Full text, verbatim —
someone should be able to paste this into SKILL.md and use it immediately.
No summaries. No descriptions.

Write the final rubric as a standalone file at
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`. Include all criteria
with text, tier, and pass conditions; the composite formula; the golden
threshold; and a version history table.

Write a "What Made It Golden" section naming at least two structural mechanisms
the loop discovered. For each mechanism: the round it was found, the inertia
gap it closed, and the criterion it activated.

Write an "Ablated criteria" section. List any criteria that never activated
across any round, with a targeted probe suggestion per criterion. If all
criteria activated: write "No ablated criteria."

Tell the user: "Golden prompt written. Final rubric written. Quest complete."
```

---

## V-03 — Inertia Framing: V-00 as Permanent Scored Competitor

**Axis:** Inertia framing — V-00 explicitly scored as a permanent column in every round
**Hypothesis:** Prior variations reference inertia in the delta field (C-14) and contrast field (C-12) but never score the inertia baseline against the rubric as a live competitor. Scoring V-00 explicitly in every round's table tests whether making the baseline concrete and scored sharpens contrast enforcement — and may surface a new pattern around "baseline-anchored discovery gate" that requires the inertia gap to be shown numerically, not just structurally.

---

```
# quest-golden

Find the golden prompt for a skill through systematic variation, scoring, and
pattern extraction. The loop terminates only at dual convergence: trial
convergence (all essential criteria pass) AND quest convergence (no new
excellence signals for two consecutive named rounds).

The inertia baseline — the skill body as it existed before this optimization
loop started — is scored as V-00 in every round. Every variation is evaluated
relative to V-00. A pattern is only a loop discovery if the top variation has
it and V-00 does not.

---

## LOOP ENTRY

### Load rubric and baseline

**Load the rubric.** Read `simulations/quest/rubrics/{skill}-rubric-*.md`.
Record: version, criterion count by tier, formula, golden threshold.
If no rubric exists: call quest-rubric first.

**Load V-00.** Read the current skill body (the prompt before optimization
started). Score V-00 against all rubric criteria using the same scoring method
as variations. Record:
- V-00 composite score
- Criteria V-00 fails (list all)
- Criteria V-00 partially satisfies (list all)

State: "V-00 (Inertia) baseline: [composite score]. Fails: [list].
PARTIAL: [list]."

This baseline is fixed for all rounds. V-00 does not change.

---

## EACH ROUND

### SPREAD-DESIGN

Entry condition: rubric loaded, V-00 scored.

Before writing any variation body, commit to five hypotheses. Each hypothesis
must address at least one criterion that V-00 fails or partially satisfies.

| Variation | Axis | Hypothesis | Criteria targeted | V-00 failure addressed |
|-----------|------|-----------|-------------------|-----------------------|
| V-01      |      |           |                   |                       |
| V-02      |      |           |                   |                       |
| V-03      |      |           |                   |                       |
| V-04      |      |           |                   |                       |
| V-05 (synthesis) | | synthesizes V-[X] + V-[Y] + V-[Z] | |         |

Gate: if a hypothesis targets only criteria V-00 already fully passes, replace
it. V-05 synthesizes the three strongest single-axis hypotheses.

DO NOT write any variation body until this table is complete and all hypotheses
target V-00 failures.

### Pre-committed scoring matrix

Before generating any variation, print the evaluation commitment for this round:

| Criterion | Tier | Pass condition |
|-----------|------|----------------|
[all rubric criteria — one row each]

Nothing can be added to this matrix after generation begins.

### Generate variations

Write V-01 through V-05 as complete, self-contained skill bodies. Not diffs.
Label each: axis, hypothesis, V-00 failure being addressed.

### Score all variations including V-00

Score all six variations (V-00 through V-05) against every criterion in the
pre-committed matrix:

| Criterion | V-00 | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|

Delta table:

| Variation | Criteria gained vs V-00 | Score delta vs V-00 | Golden? |
|-----------|------------------------|---------------------|---------|

### Round log

| Round | Top | Score | V-00 score | Delta vs V-00 | Patterns found | PARTIAL near-misses | Trajectory |
|-------|-----|-------|-----------|---------------|----------------|---------------------|------------|

Trajectory: up-arrow (improved from prior round), down-arrow (regressed),
"new" (first appearance this round). Before designing next round's spread,
consult PARTIAL near-misses — they are productive leads.

### Excellence extraction (QU2) — before QU3

For the top variation vs the runner-up:

| Field            | Value |
|------------------|-------|
| TOP HAD          | [structural element present in the top variation]             |
| SECOND LACKED    | [that element absent in runner-up — state the absence]        |
| V-00 LACKED      | [that element absent from inertia baseline — the discovery]   |
| Round first seen | [round number, or "this round"]                               |
| New signal?      | YES / NO                                                      |

Signal = none unless the element is: (a) present in the top variation, (b)
absent in the runner-up, AND (c) absent from V-00. If V-00 already has the
element, it is not a loop discovery — it was always there.

DO NOT proceed to QU3 until this block is complete.

### Criterion proposal (QU3)

Gated on QU2 signal not being none.

If signal = none: "QU3: nothing to propose this round."

If signal is named: propose with — criterion text / tier with rationale /
LOCATION / OBSERVABLE / STANDARD.

Include contrast evidence: "V-[top] passes because [mechanism]. V-00 fails
because [absence of mechanism]. Runner-up fails because [absence]."

Await QU4 approval. Do not apply until approved.

---

## CONVERGENCE CHECK

Dedicated phase. The only exit from the loop. Runs after QU3.

**GATE 1 — Trial convergence:**
PASS if all variations (V-01 through V-05) pass all essential criteria this
round.

State: "GATE 1 = [PASS / FAIL]."

**GATE 2 — Quest convergence (plateau):**
Cite both rounds explicitly:
"Round R-[N]: patterns = [names or 'none']. Round R-[N-1]: patterns = [names
or 'none']."

PASS if both = none.
FAIL if either names a pattern, or if R-[N-1] is not in the log.

Do not use "the last two rounds" or "both recent rounds" — name the round
numbers and show their values.

State: "GATE 2 = [PASS / FAIL]."

**Termination:**
GATE 1 = PASS AND GATE 2 = PASS → proceed to WRITE GOLDEN ARTIFACTS.
Else: loop continues. Report round summary. Await user instruction.

Do not exit on GATE 1 alone. Both gates. Both rounds. Named values.

---

## WRITE GOLDEN ARTIFACTS (dual convergence only)

**Golden prompt:** full verbatim skill body to
`simulations/quest/golden/{skill}-golden-{date}.md`. Copy-pastable into
SKILL.md. Not a summary.

**Final rubric:** standalone file at
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`. All criteria,
formula, denominator, threshold, version history.

**"What Made It Golden":** minimum two structural mechanisms. For each:
(a) round first discovered, (b) inertia gap closed — show "V-00 failed
[criterion] because [absence]; golden prompt passes because [mechanism]",
(c) criterion activated.

**"Ablated criteria":** criteria with zero activations across all rounds, with
a probe per criterion. If none: "No ablated criteria."

State: "Golden prompt written. Final rubric written. Quest complete."
```

---

## V-04 — V-01 + V-02 + V-03 Combined

**Axis:** Lifecycle emphasis (expanded gate) + Phrasing register (conversational imperative) + Inertia framing (V-00 scored)
**Hypothesis:** Interaction testing — if all three axes together produce a score different from any single axis, the delta identifies an interaction effect not visible in single-axis tests. Also the most aggressive probe for any format-dependence in the 18 criteria.

---

```
# quest-golden

Your job: find the golden prompt for a skill using inertia-anchored scoring,
conversational-imperative structure, and a rigorous six-step convergence gate.
You stop only at dual convergence: all essential criteria passing AND no new
excellence signals for two consecutive named rounds. The convergence check is
the only exit.

The inertia baseline (V-00, the current skill body before optimization) is
scored in every round. Every variation's value is measured against V-00.

---

**Before the first round:**

**1. Load the rubric.** Find `simulations/quest/rubrics/{skill}-rubric-*.md`.
Record version, criteria by tier, formula, and threshold. No rubric = run
quest-rubric first.

**2. Score V-00.** Read the current skill body. Score it against all rubric
criteria. Record its composite, failures, and PARTIAL hits. This baseline does
not change.

---

**Each round, in this order:**

**Step 1. Design the spread.** Before writing anything, fill in this table.
Each hypothesis must address a criterion V-00 fails or partially satisfies.

| Variation | Axis | Hypothesis | Criteria targeted | V-00 failure addressed |
|-----------|------|-----------|-------------------|-----------------------|
| V-01      |      |           |                   |                       |
| V-02      |      |           |                   |                       |
| V-03      |      |           |                   |                       |
| V-04      |      |           |                   |                       |
| V-05 (synthesis) | | synthesizes V-[X] + V-[Y] + V-[Z] | |         |

No two rows can share the same axis. V-05 synthesizes the three strongest
single-axis results. Do not write any variation body until this table is
complete and all hypotheses target V-00 failures.

**Step 2. Pre-commit the scoring criteria.** Print this before generating
any variation. Nothing can be added afterward.

| Criterion | Tier | Pass condition |
|-----------|------|----------------|
[all rubric criteria]

**Step 3. Write the variations.** V-01 through V-05 as complete, runnable
skill bodies. Full text, not diffs. Label each with axis and hypothesis.

**Step 4. Score all six (V-00 through V-05).** Use the pre-committed matrix.

| Criterion | V-00 | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|

| Variation | Essential | Recommended | Aspirational | Composite | vs V-00 delta | Golden? |
|-----------|-----------|-------------|--------------|-----------|--------------|---------|

**Step 5. Log this round.** Append to the iteration history:

| Round | Top | Score | V-00 | Delta | Patterns found | PARTIAL near-misses | Trajectory |
|-------|-----|-------|------|-------|----------------|---------------------|------------|

Trajectory: up-arrow (improved), down-arrow (regressed), "new" (first
appearance). Consult PARTIAL near-misses before designing next round's spread.

**Step 6. Extract the excellence signal.** Do this before proposing any
criterion — because a criterion proposal not grounded in an observed output gap
is a guess, not a discovery.

| TOP HAD          | [structural element in the top variation]                     |
| SECOND LACKED    | [that element absent in runner-up — state the absence]        |
| V-00 LACKED      | [that element absent from V-00 — this is the discovery]       |
| Round first seen | [round number, or "this round"]                               |

Signal = none unless: present in top AND absent in runner-up AND absent in V-00.
Do not continue to step 7 until this block is filled.

**Step 7. Propose a criterion only if step 6 found a signal.**
No signal = "QU3: nothing to propose this round." Move to step 8.

If signal found: propose with — criterion text / tier + rationale / LOCATION /
OBSERVABLE / STANDARD. Contrast: "V-[top] passes because [X]. V-00 fails
because [absence of X]." Wait for approval before applying.

**Step 8. Check convergence. The only exit from the loop.**

Work through each sub-step in order. Do not skip or combine them.

C1. State the current round: "Current round: R-[N]."

C2. Read R-[N] from the iteration log:
    "Round R-[N]: patterns = [names or 'none']."

C3. Read R-[N-1] from the iteration log:
    "Round R-[N-1]: patterns = [names or 'none']."
    If R-[N-1] not in log: GATE 2 is unresolvable. Mark FAIL and skip to C6.

C4. Evaluate GATE 1 (trial convergence):
    PASS if all V-01..V-05 pass all essential criteria this round.
    Failure modes: any essential criterion fails for any variation.
    "GATE 1 = [PASS / FAIL]. Reason: [one sentence]."

C5. Evaluate GATE 2 (quest convergence / plateau):
    PASS if Round R-[N] = none AND Round R-[N-1] = none.
    Required citation format:
      "Round R-[N]: patterns = [value]. Round R-[N-1]: patterns = [value]."
    These do NOT satisfy GATE 2: "both recent rounds," "the last two rounds,"
    citing one round, citing rounds absent from the log.
    "GATE 2 = [PASS / FAIL]. Citation: R-[N] = [value], R-[N-1] = [value]."

C6. Termination:
    GATE 1 = PASS AND GATE 2 = PASS -> proceed to step 9.
    Either FAIL or UNRESOLVABLE -> loop continues. Report to user and wait.
    Do not exit on GATE 1 alone. Both gates. Both rounds. Named values.

**Step 9. Write the golden artifacts.** Only when step 8 exits.

Golden prompt: complete verbatim skill body to
`simulations/quest/golden/{skill}-golden-{date}.md`. Copy-pastable, no summary.

Final rubric: standalone file at
`simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`. All criteria,
formula, denominator, threshold, version history.

"What Made It Golden": two or more structural mechanisms. For each: round
discovered, inertia gap closed — "V-00 failed [criterion] because [absence];
golden prompt passes because [mechanism]" — criterion activated.

"Ablated criteria": list never-activated criteria with probes. If none: "No
ablated criteria."

State: "Golden prompt written. Final rubric written. Quest complete."
```

---

## V-05 — Full Synthesis: R4 Champion + V-01 (Expanded Gate) + V-03 (V-00 Baseline)

**Axis:** Full synthesis — R4 V-05 champion body integrated with Round 5 axes V-01 (expanded convergence gate) and V-03 (V-00 as scored baseline); formal PHASE/STEP headers preserved from R4 champion
**Hypothesis:** The R4 champion scored 100/100. Integrating the two strongest structural additions from R5 (V-01's 6-step convergence gate, V-03's V-00 scoring) into the R4 body creates the strongest possible candidate while preserving format stability. V-02's register change is covered by V-04; V-05 confirms whether the R5 structural additions are synergistic with or neutral to the R4 champion body.

---

```
# quest-golden

Find the golden prompt for a skill through systematic variation, scoring, and
pattern extraction. The loop terminates only at dual convergence: trial
convergence (all essential criteria pass) AND quest convergence (no new
excellence signals for two consecutive named rounds).

The inertia baseline — the skill body before optimization — is scored as V-00
in every round. Every pattern is only a discovery if the top variation has it
and V-00 does not.

---

## LOOP ENTRY

### Load rubric and V-00

**Load the rubric.** Read `simulations/quest/rubrics/{skill}-rubric-*.md`.
Identify the latest version. Record: rubric version, criterion count by tier,
composite formula, golden threshold. If no rubric exists: call quest-rubric
first. Do not proceed without a loaded rubric.

**Load V-00 (inertia baseline).** Read the current skill body. Score it
against all rubric criteria. Record: V-00 composite score, criteria V-00 fails,
criteria V-00 partially satisfies. This baseline is fixed for all rounds.

State: "V-00 baseline: [composite]. Fails: [list]. PARTIAL: [list]."

---

## EACH ROUND

### SPREAD-DESIGN

Entry condition: rubric loaded, V-00 scored.

Before writing any variation body, complete this table:

| Variation | Axis | Hypothesis (which criterion changes, predicted direction) | Criteria targeted | V-00 failure addressed |
|-----------|------|----------------------------------------------------------|-------------------|-----------------------|
| V-01      |      |                                                          |                   |                       |
| V-02      |      |                                                          |                   |                       |
| V-03      |      |                                                          |                   |                       |
| V-04      |      |                                                          |                   |                       |
| V-05      |      | synthesizes V-[X], V-[Y], V-[Z]                          |                   |                       |

Check: (a) no two rows share the same axis; (b) each hypothesis addresses a
criterion V-00 fails or partially satisfies; (c) V-05 synthesizes the three
strongest single-axis hypotheses. Replace non-compliant rows before proceeding.

DO NOT write any variation body until the SPREAD-DESIGN table is complete and
all checks pass. This gate exists because variations generated without committed
hypotheses produce redundant coverage; the spread table forces distinct
territory.

Round 2+: before filling the spread table, consult the PARTIAL near-misses
column in the iteration history. Near-miss criteria from prior rounds are
productive leads for new hypotheses.

### Step 1 — Generate variations

Write V-01 through V-05 as complete, runnable skill bodies. Each is
self-contained — full text, not a diff. Label each with its axis and hypothesis.

### Step 2 — Score

**2a — Pre-commit evaluation structure (executes before scoring):**

Print this skeleton matrix before generating or scoring any variation. This
commits to the evaluation structure for this round. Any criterion not in this
table cannot receive a valid score.

DO NOT score any variation until this skeleton is printed.

| Criterion | Tier | Pass condition (one sentence) |
|-----------|------|-------------------------------|
[one row per criterion in the active rubric]

**2b — Per-variation evidence:**

For each variation, for each criterion: PASS / PARTIAL / FAIL with one sentence
of evidence. Work through every row in the pre-committed skeleton.

**2c — Fill the skeleton:**

| Criterion | V-00 | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|

Composite table:

| Variation | Essential | Recommended | Aspirational | Composite | vs V-00 delta | Golden? |
|-----------|-----------|-------------|--------------|-----------|--------------|---------|

### Step 3 — Iteration history entry

Append one row:

| Round | Variation IDs | Top composite | Patterns found | PARTIAL near-misses | Criterion added |
|-------|--------------|---------------|----------------|---------------------|-----------------|

PARTIAL near-misses: list any criterion where any variation scored PARTIAL.
Track trajectory: up-arrow (improved from prior round), down-arrow (regressed),
"new" (first appearance). This column feeds the next round's spread-design.

### Step 4 — Excellence extraction (QU2)

DO NOT proceed to Step 5 until all patterns in this round are extracted and
named. This gate exists because proposals made before extraction completes can
target already-solved problems, wasting rubric space. Extract for ALL patterns,
not just the first one observed.

For the top variation vs the runner-up:

| Field            | Value |
|------------------|-------|
| TOP HAD          | [structural element present in the top variation]              |
| SECOND LACKED    | [that element absent in runner-up — state the absence]         |
| V-00 LACKED      | [that element absent from inertia baseline — the discovery]    |
| Round first seen | [round number, or "this round"]                                |

Signal = none if: (a) no structural gap between top and runner-up, OR (b) V-00
already has the element. Signal must be absent from V-00 to count as a
loop discovery.

### Step 5 — Criterion proposal (QU3)

Gated on Step 4 signal not being none. If signal = none: write "QU3: no
criterion proposed this round." Proceed to the CONVERGENCE CHECK.

If signal is named: propose a criterion with all five components:
- Criterion text (what the prompt must structurally contain)
- Tier with rationale (essential = wrong without it; recommended = better with
  it; aspirational = excellent)
- LOCATION: where in the prompt body to find the evidence
- OBSERVABLE: the specific textual or structural evidence
- STANDARD: pass condition (one sentence) and fail condition (one sentence)

Include contrast evidence: "V-[top] passes because [mechanism]. V-00 fails
because [absence of mechanism]. Runner-up fails because [absence]."

Present the proposal. Await QU4 approval. Do not apply until approved.

---

## CONVERGENCE CHECK

This phase runs after Step 5. It is the only exit point from the loop. Work
through each sub-step in order.

### C1 — Identify current round

State: "Current round: R-[N]."

### C2 — Extract current round signal from log

Read Row R-[N] from the iteration history. State:
"Round R-[N]: patterns = [names of patterns, or 'none']."

### C3 — Extract prior round signal from log

Read Row R-[N-1] from the iteration history. State:
"Round R-[N-1]: patterns = [names of patterns, or 'none']."

If R-[N-1] does not exist in the log: GATE 2 is UNRESOLVABLE. State this.
GATE 2 = FAIL. Proceed to C6 without evaluating C5.

### C4 — Evaluate GATE 1: trial convergence

PASS if: all variations (V-01 through V-05) pass all essential criteria in
R-[N]. (Prior-round essential pass is carried in the log — verify if needed.)

Failure modes: any essential criterion fails for any variation.

State: "GATE 1 = [PASS / FAIL]."

### C5 — Evaluate GATE 2: quest convergence (plateau)

PASS if: Round R-[N] patterns = none AND Round R-[N-1] patterns = none.

Required citation format (no substitutions allowed):
"Round R-[N]: patterns = [value]. Round R-[N-1]: patterns = [value]."

These phrases do NOT satisfy GATE 2:
- "Both recent rounds found zero patterns." (missing round numbers)
- "The last two rounds showed no signals." (missing round numbers)
- Citing only one round
- Citing rounds not present in the iteration history

State: "GATE 2 = [PASS / FAIL]. Round R-[N] = [value]. Round R-[N-1] = [value]."

### C6 — Termination decision

GATE 1 = PASS AND GATE 2 = PASS:
  TRIAL CONVERGED AND QUEST PLATEAUED.
  Proceed to WRITE GOLDEN ARTIFACTS.

Either gate = FAIL or UNRESOLVABLE:
  Loop continues.
  Present round summary. Await instruction to proceed to next round.
  Do not exit on GATE 1 alone.
  Do not exit on a single round of none.
  Two named rounds with traceable values are required.

---

## WRITE GOLDEN ARTIFACTS (only at dual convergence)

**1. Golden prompt.**
Write the full verbatim skill body to:
  simulations/quest/golden/{skill}-golden-{date}.md
Complete, copy-pastable. Not a summary. Not a description. Every line.

**2. Final rubric.**
Write the accumulated rubric to:
  simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
Contents: all converged criteria with text, tier, and three-part pass
conditions; composite formula with current denominator; golden threshold;
version history table noting which round added each criterion.

**3. "What Made It Golden".**
Minimum two structural mechanisms. For each:
  (a) the round it was first discovered
  (b) the inertia gap it closed: "V-00 failed [criterion] because [absence];
      the golden prompt passes because [mechanism]"
  (c) the criterion it activated

**4. "Ablated criteria".**
List criteria with zero activations across all rounds; suggested targeted probe
per criterion. If all criteria activated at least once: "No ablated criteria."

State: "Golden prompt written. Final rubric written. Quest complete."
```

---

## Round 5 Predicted Scores (v4 rubric preview)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Dual convergence | PASS | PASS | PASS | PASS | PASS |
| C-02 Golden prompt artifact | PASS | PASS | PASS | PASS | PASS |
| C-03 Final rubric artifact | PASS | PASS | PASS | PASS | PASS |
| C-04 QU2 before QU3 | PASS | PASS | PASS | PASS | PASS |
| C-05 Rubric at loop start | PASS | PASS | PASS | PASS | PASS |
| C-06 Round log | PASS | PASS | PASS | PASS | PASS |
| C-07 Signal isolation | PASS | PASS | PASS | PASS | PASS |
| C-08 Criterion proposal | PASS | PASS | PASS | PASS | PASS |
| C-09 What made it golden | PASS | PASS | PASS | PASS | PASS |
| C-10 Ablated criteria | PASS | PASS | PASS | PASS | PASS |
| C-11 Termination isolation | PASS | PASS | PASS | PASS | PASS |
| C-12 Contrast-enforced signal | PASS | PASS | PASS | PASS | PASS |
| C-13 Rationale-grounded sequencing | PASS | PASS | PASS | PASS | PASS |
| C-14 Inertia-anchored delta | PASS | PASS | PASS | PASS | PASS |
| C-15 Spread-design phase | PASS | PASS | PASS | PASS | PASS |
| C-16 Named-round citation | PASS | PASS | PASS | PASS | PASS |
| C-17 PARTIAL trajectory | PASS | PASS | PASS | PASS | PASS |
| C-18 Pre-committed matrix | PASS | PASS | PASS | PASS | PASS |
| **Composite** | **100** | **100** | **100** | **100** | **100** |

**Predicted outcome:** All five variations at 100/100. No new excellence signals across any axis. If confirmed by scoring, then: Round R-5 patterns = none AND Round R-4 patterns = none → GATE 2 = PASS. Combined with GATE 1 = PASS → **TRIAL CONVERGED AND QUEST PLATEAUED. Golden prompt = V-05 body.**
