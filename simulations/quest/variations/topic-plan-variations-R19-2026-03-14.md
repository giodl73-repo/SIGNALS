# topic:plan — Variations V-01 through V-05

**Round**: 19
**Skill**: `topic:plan`
**Base rubric**: v18
**Single-axis variations**: V-01 (Inertia framing), V-02 (Output format/slot architecture), V-03 (Narrative Format Contract)
**Combined**: V-04 (Inertia + Output format), V-05 (All three axes)

---

## V-01 — Single Axis: Inertia Framing

**Variation axis**: Inertia framing
**Hypothesis**: Declaring a named `[INERTIA-GATE]` verbatim block in the preamble and reproducing it at every decision gate forces the model to evaluate the status-quo option structurally rather than dismissing it under proposal-generation momentum. A recalled sentence can be compressed; a reproduced named block cannot be silently omitted.

---

```
# topic:plan — Revise Signal Strategy

You are revising the signal strategy for {{topic}}.

---

## PREAMBLE — INERTIA BLOCK

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision, ask: does the evidence actually require this change,
> or is the existing strategy sufficient to cover what matters?
> Mark every proposal with an explicit inertia disposition.
> A prompt that produces only proposals without inertia verdicts has failed this gate.

This block is reproduced verbatim at Steps 3, 4b, 6, and 7. Its presence is required at each site.

---

## Step 1 — Read Strategy

Read `simulations/{{topic}}/strategy.md`.

Extract and output:
- Strategy date
- Coverage intent (which namespaces the strategy targets and why)
- Stated priorities (ordered list)
- Open questions the strategy flagged as unresolved

---

## Step 2 — Survey Gathered Signals

List all signal files found under `simulations/{{topic}}/` across all namespaces:
`scout/`, `draft/`, `review/`, `flow/`, `trace/`, `prove/`, `listen/`, `program/`

For each signal file produce one row:

| Signal File | Namespace | Date | Key Finding (one sentence) |
|---|---|---|---|

---

## Step 3 — Identify Delta

Compare what the strategy anticipated against what the signals revealed.

For each signal that diverges from strategy intent:

| Signal File | Dimension Revealed | Change Type | Evidence Quote |
|---|---|---|---|
| | | [ADDITION] / [REMOVAL] / [REPRIORITIZATION] | |

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision, ask: does the evidence actually require this change,
> or is the existing strategy sufficient to cover what matters?
> Mark every proposal with an explicit inertia disposition.
> A prompt that produces only proposals without inertia verdicts has failed this gate.

For each delta item add an inertia column:

| Signal File | Dimension | Change Type | Inertia Verdict |
|---|---|---|---|
| | | | [CHANGE REQUIRED — evidence demands it] / [INERTIA HOLDS — strategy sufficient] |

---

## Step 4a — Proposals: Additions

New coverage areas not in current strategy, where inertia was rejected.

| # | Proposed Addition | Source Signal | Evidence | Inertia Rejected Because |
|---|---|---|---|---|

If no additions: write `ADDITIONS: none — inertia holds for all candidate additions.`

---

## Step 4b — Proposals: Removals and Reprioritizations

**REMOVALS** — coverage made obsolete by signals

| # | Proposed Removal | Source Signal | Reason Obsolete | Inertia Rejected Because |
|---|---|---|---|---|

If no removals: write `REMOVALS: none — inertia holds.`

**REPRIORITIZATIONS** — coverage that should move up or down

| # | Coverage Item | Current Priority | Proposed Priority | Source Signal | Inertia Rejected Because |
|---|---|---|---|---|---|

If no reprioritizations: write `REPRIORITIZATIONS: none — inertia holds.`

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision, ask: does the evidence actually require this change,
> or is the existing strategy sufficient to cover what matters?
> Mark every proposal with an explicit inertia disposition.
> A prompt that produces only proposals without inertia verdicts has failed this gate.

---

## Step 5 — Calibration Check

State overall calibration:

- SIGNIFICANT REVISION — 3+ proposals across multiple change types; strategy substantially updated
- MINOR REFINEMENT — 1–2 proposals; strategy adjusted at the margin
- INERTIA HOLDS — evidence does not require revision; strategy is current

State which applies and cite the evidence that determined it.

---

## Step 6 — Confirm Gate

Present the revision summary to the user. Do not write `strategy.md` until confirmed.

Output:
- Calibration verdict
- Proposals grouped by type (Steps 4a–4b)
- Net count: N additions, N removals, N reprioritizations

Ask: `Confirm revisions? (yes / adjust / reject)`

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision, ask: does the evidence actually require this change,
> or is the existing strategy sufficient to cover what matters?
> Mark every proposal with an explicit inertia disposition.
> A prompt that produces only proposals without inertia verdicts has failed this gate.

If the user says "reject" or selects inertia: acknowledge, do not write, close cleanly.

---

## Step 7 — Update strategy.md

On confirmed "yes" only.

Rewrite `simulations/{{topic}}/strategy.md` with:
- Updated date
- Revised coverage intent
- Updated priorities (in order)
- Resolution notes for open questions addressed by signals
- New open questions surfaced by signals

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision, ask: does the evidence actually require this change,
> or is the existing strategy sufficient to cover what matters?
> Mark every proposal with an explicit inertia disposition.
> A prompt that produces only proposals without inertia verdicts has failed this gate.

Final check before writing: are all changes confirmed? Write only confirmed changes. Unconfirmed items remain in the old strategy or are excluded.
```

---

## V-02 — Single Axis: Output Format / Pre-printed Slot Architecture

**Variation axis**: Output format
**Hypothesis**: Pre-printing `[ ] A / [ ] B` selection slots at every binary decision site — not just calibration — eliminates conditional branch composition risk throughout execution. A slot forces the model to make a discrete, visible choice; conditional prose allows paraphrase, partial emission, or hybrid output.

---

```
# topic:plan — Revise Signal Strategy

You are revising the signal strategy for {{topic}}.

---

## OUTPUT SCHEMA (read before opening any files)

Your output has five named sections produced in this order:

1. `STRATEGY SNAPSHOT` — current strategy before any revision
2. `SIGNAL SURVEY` — all signals gathered across namespaces
3. `DELTA ANALYSIS` — what signals revealed that the strategy did not anticipate
4. `REVISION PROPOSAL` — additions, removals, reprioritizations with null-case declarations
5. `CALIBRATION + CONFIRM` — calibration verdict and user gate

Do not produce narrative description of steps. Produce the five sections.

---

## SCHEMA COMMITMENT

Select exactly one and write it as output before proceeding:

[ ] SCHEMA-A — I will produce all five sections in order, with null-case declarations for empty
    proposal types, and pre-printed slots at all binary decision sites as specified below.

[ ] SCHEMA-B — I will adapt the schema to what seems appropriate for this topic.

---

## SECTION 1: STRATEGY SNAPSHOT

Read `simulations/{{topic}}/strategy.md`.

Produce:

```
Strategy Date: ___
Coverage Intent: ___
Priorities:
  1. ___
  2. ___
  3. ___
Open Questions:
  - ___
```

---

## SECTION 2: SIGNAL SURVEY

Read all signal files under `simulations/{{topic}}/` in all namespaces.

| Signal File | Namespace | Date | Key Finding |
|---|---|---|---|

**NULL-CASE DECLARATION — SIGNAL SURVEY**

Select exactly one and write it as output:

[ ] SIGNALS-FOUND — at least one signal file exists; table above is populated.
[ ] SIGNALS-EMPTY — no signal files found; revision cannot proceed without gathered signals.

If SIGNALS-EMPTY: stop here and output a message explaining what signals are needed before
`topic:plan` can run. Do not proceed to Section 3.

---

## SECTION 3: DELTA ANALYSIS

For each signal that reveals a gap, contradiction, or uncovered dimension in the current strategy:

| Signal File | Dimension Revealed | Change Type | Evidence Quote |
|---|---|---|---|
| | | [ADDITION] / [REMOVAL] / [REPRIORITIZATION] | |

**NULL-CASE DECLARATION — DELTA**

Select exactly one and write it as output:

[ ] DELTA-EXISTS — at least one signal diverges from strategy intent; table above is populated.
[ ] NULL-DELTA — no signal contradicts or extends the current strategy; inertia holds; skip
    Section 4 proposals and proceed to Section 5 calibration.

---

## SECTION 4: REVISION PROPOSAL

**Additions** — new coverage areas not in current strategy

| # | Proposed Addition | Source Signal | Evidence Quote |
|---|---|---|---|

Select exactly one and write it as output:

[ ] ADDITIONS-PRESENT — table above contains at least one addition.
[ ] ADDITIONS-EMPTY — no additions proposed; inertia holds for all candidate additions.

---

**Removals** — existing coverage made obsolete by signals

| # | Proposed Removal | Source Signal | Reason Obsolete |
|---|---|---|---|

Select exactly one and write it as output:

[ ] REMOVALS-PRESENT — table above contains at least one removal.
[ ] REMOVALS-EMPTY — no removals proposed; inertia holds for all existing coverage.

---

**Reprioritizations** — coverage that should move up or down

| # | Coverage Item | Current Priority | Proposed Priority | Source Signal |
|---|---|---|---|---|

Select exactly one and write it as output:

[ ] REPRIO-PRESENT — table above contains at least one reprioritization.
[ ] REPRIO-EMPTY — no reprioritizations proposed; current priority order holds.

---

**SCHEMA CHECKPOINT — SECTION 4**

Select exactly one and write it as output:

[ ] SECTION4-COMPLETE — all three proposal types declared; null-case slots selected for
    each empty type; no proposal type silently omitted.
[ ] SECTION4-INCOMPLETE — missing: ___

---

## SECTION 5: CALIBRATION + CONFIRM

**Calibration**

Select exactly one and write it as output:

[ ] CALIBRATION-SIGNIFICANT — 3 or more proposals across multiple change types; strategy
    substantially revised.
[ ] CALIBRATION-MINOR — 1–2 proposals; strategy adjusted at the margin.
[ ] CALIBRATION-INERTIA — evidence does not require revision; strategy is current.

**Confirm Gate**

Present Section 4 to the user alongside the calibration verdict.

Net count: ___ additions, ___ removals, ___ reprioritizations.

Ask: `Confirm revisions? (yes / adjust / reject)`

Do not write `strategy.md` until the user responds.

**POST-CONFIRM CHECKPOINT**

Select exactly one and write it as output after the user responds:

[ ] WRITE-CONFIRMED — user said "yes"; proceeding to update strategy.md with confirmed
    revisions only.
[ ] WRITE-ADJUSTED — user said "adjust"; returning to Section 4 with noted changes before
    writing.
[ ] WRITE-REJECTED — user said "reject" or chose inertia; no write performed; closing cleanly.

---

## WRITE STEP — Update strategy.md

Execute only on WRITE-CONFIRMED or WRITE-ADJUSTED (after adjustment confirmed).

Rewrite `simulations/{{topic}}/strategy.md` with:
- Updated date
- Revised coverage intent
- Updated priority order
- Resolution notes for open questions addressed by signals
- New open questions surfaced

**POST-WRITE CHECKPOINT**

Select exactly one and write it as output:

[ ] WRITE-COMPLETE — strategy.md rewritten with all confirmed revisions applied.
[ ] WRITE-PARTIAL — wrote only subset; reason: ___
[ ] WRITE-FAILED — error: ___
```

---

## V-03 — Single Axis: Narrative Format Contract (Phrasing Register)

**Variation axis**: Phrasing register + Narrative Format Contract declared upfront
**Hypothesis**: Declaring the required output register ("conclusion before evidence") and its degenerate form ("step-description narrative — FAIL") as a named block before Step 1 anchors the model's register commitment before any execution context pressure accumulates. A mid-execution gate row names the constraint but encounters it under context load; a preamble contract establishes the constraint before any step runs.

---

```
# topic:plan — Revise Signal Strategy

You are revising the signal strategy for {{topic}}.

---

## NARRATIVE FORMAT CONTRACT

**Required register**: Conclusion before evidence.
Every analytical output leads with the conclusion. Evidence follows in subordinate position.

**Required form** — state the finding, then cite what produced it:
> "Scout signals establish two uncovered dimensions (market timing, regulatory lag) — scout-market-2026-03-10 found timing sensitivity; scout-compliance-2026-03-11 found pending regulation."

**Degenerate register — FAIL** — step-description narrative: describing what you are doing
rather than stating what you found.
> FAIL: "I will now examine the scout signals to determine whether they reveal any gaps in
> the current strategy."
> FAIL: "Next, I read strategy.md and extracted the following information."

This contract applies at every analytical step in this skill. Degenerate register at any
step constitutes a rubric failure. Produce findings, not descriptions of finding.

---

## Step 1 — Read Strategy

Read `simulations/{{topic}}/strategy.md`.

Output (conclusion-first):

The strategy [is current / shows N gaps against gathered signals]. Written on [date], it
targets [coverage intent in one sentence]. Its stated priorities are [list]. Its open
questions are [list].

---

## Step 2 — Survey Gathered Signals

Read all signal files under `simulations/{{topic}}/` across all namespaces.

Output (conclusion-first):

[N] signals exist. [N] diverge from strategy intent. The highest-signal finding is
[one sentence from the most significant signal file].

Full signal list:

| Signal File | Namespace | Key Finding | Diverges from Strategy? |
|---|---|---|---|

---

## Step 3 — Delta: What Changed

For each signal that diverges from strategy intent, output one conclusion-first statement:

> [Signal file] establishes [dimension] as [uncovered / deprioritized / contradicted] in
> the current strategy — [one-sentence evidence]. Change type: [ADDITION / REMOVAL /
> REPRIORITIZATION].

Do not produce tables for this step. Do not describe what you are comparing. State what
you found, then cite the signal.

---

## Step 4 — Inertia Assessment

Before listing proposals, assess the status-quo option. Output (conclusion-first):

The inertia option [is viable / is not viable]. [Evidence in one sentence.] [N] candidate
revisions clear the evidence threshold; [N] do not and are excluded.

**[INERTIA-GATE]**
> Inertia is a co-equal option. Signal evidence must clear a threshold before revision is
> warranted. Marginal or ambiguous signals default to inertia. Do not propose changes that
> the evidence does not require.

Items that did not clear the threshold: [list, or "none — all candidates clear threshold."]

---

## Step 5 — Propose Revisions

Produce three sections. Each entry is a conclusion-first statement, not a table row.

**ADDITIONS** (new coverage dimensions established by signals)

For each addition (conclusion-first):
> [Signal file] establishes [dimension] as a required coverage area — [evidence in one
> sentence].

If no additions: "No additions — inertia holds for all candidate additions."

---

**REMOVALS** (existing coverage made obsolete by signals)

For each removal (conclusion-first):
> [Signal file] makes [existing coverage item] obsolete — [evidence in one sentence].

If no removals: "No removals — all existing coverage remains valid."

---

**REPRIORITIZATIONS** (coverage that should move in the priority order)

For each reprioritization (conclusion-first):
> [Signal file] elevates / demotes [coverage item] from priority [N] to [N] — [evidence].

If no reprioritizations: "No reprioritizations — current priority order holds."

**[INERTIA-GATE]**
> Inertia is a co-equal option. Signal evidence must clear a threshold before revision is
> warranted. Marginal or ambiguous signals default to inertia. Do not propose changes that
> the evidence does not require.

---

## Step 6 — Calibration Check

Output (conclusion-first):

This revision is [significant / minor / inertia holds]. Evidence: [one sentence].

---

## Step 7 — Confirm Gate

Present the revision summary to the user. Do not write `strategy.md` until confirmed.

Output format:
- Calibration verdict (from Step 6)
- Proposals from Step 5, grouped by type
- Net count: N additions, N removals, N reprioritizations

Ask: `Confirm revisions? (yes / adjust / reject)`

**[INERTIA-GATE]**
> Inertia is a co-equal option. Signal evidence must clear a threshold before revision is
> warranted. Marginal or ambiguous signals default to inertia. Do not propose changes that
> the evidence does not require.

If "reject": acknowledge that inertia was selected, confirm no write will occur, close cleanly.

---

## PHASE 3 EXIT GATE

Before writing strategy.md, verify each item:

- [ ] Every step produced conclusion-first output — no step-description narrative
- [ ] Step 3 used prose, not tables — findings stated, not described
- [ ] Inertia assessed at Steps 4, 5, and 7 — items excluded for insufficient evidence listed
- [ ] Calibration stated conclusion first with evidence
- [ ] User confirmed before reaching this step

If any item is not checked: return to the failing step and correct the register before writing.

---

## Step 8 — Update strategy.md

On confirmation only.

Rewrite `simulations/{{topic}}/strategy.md` with confirmed revisions. Lead the document with
the revision date and a one-sentence conclusion: what changed and why.
```

---

## V-04 — Combined: Inertia Framing + Pre-printed Slot Architecture

**Variation axes**: Inertia framing + Output format
**Hypothesis**: INERTIA-GATE verbatim blocks prevent inertia omission; pre-printed slots eliminate composition risk at binary decision sites. Together they address two independent failure modes: the model silently skipping the status-quo competitor, and the model producing conditional prose where discrete choices were required. Neither constraint implies the other; combining them closes both gaps without redundancy.

---

```
# topic:plan — Revise Signal Strategy

You are revising the signal strategy for {{topic}}.

---

## PREAMBLE — INERTIA BLOCK

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

This block is reproduced verbatim at Steps 3, 5, 7, and 8. Its presence is required at
each site. Absence of the block at any gate site is a visible failure.

---

## OUTPUT SCHEMA (read before opening any files)

Five sections in order: STRATEGY SNAPSHOT → SIGNAL SURVEY → DELTA ANALYSIS →
REVISION PROPOSAL → CALIBRATION + CONFIRM.

**SCHEMA COMMITMENT**

Select exactly one and write it as output:

[ ] SCHEMA-A — I will produce all five sections with null-case slots and pre-printed
    decision slots as specified.
[ ] SCHEMA-B — I will adapt the schema.

---

## SECTION 1: STRATEGY SNAPSHOT

Read `simulations/{{topic}}/strategy.md`.

```
Strategy Date: ___
Coverage Intent: ___
Priorities:
  1. ___
  2. ___
  3. ___
Open Questions:
  - ___
```

---

## SECTION 2: SIGNAL SURVEY

Read all signal files under `simulations/{{topic}}/`.

| Signal File | Namespace | Date | Key Finding |
|---|---|---|---|

**NULL-CASE DECLARATION**

Select exactly one and write it as output:

[ ] SIGNALS-FOUND — signal files exist; table populated.
[ ] SIGNALS-EMPTY — no signals found; plan cannot run; output what signals are needed.

---

## SECTION 3: DELTA ANALYSIS

For each signal that diverges from strategy intent:

| Signal File | Dimension Revealed | Change Type | Evidence Quote | Inertia Verdict |
|---|---|---|---|---|
| | | [ADDITION]/[REMOVAL]/[REPRIO] | | [CHANGE REQUIRED] / [INERTIA HOLDS] |

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

**NULL-CASE DECLARATION — DELTA**

Select exactly one and write it as output:

[ ] DELTA-EXISTS — at least one signal diverges; table populated; proceed to Section 4.
[ ] NULL-DELTA — no signal diverges; inertia holds across all signals; skip to Section 5.

---

## SECTION 4: REVISION PROPOSAL

Include only items where inertia was explicitly rejected in Section 3.

**Additions**

| # | Proposed Addition | Source Signal | Evidence | Inertia Rejected Because |
|---|---|---|---|---|

Select exactly one and write it as output:

[ ] ADDITIONS-PRESENT — table populated.
[ ] ADDITIONS-EMPTY — inertia holds for all addition candidates.

---

**Removals**

| # | Proposed Removal | Source Signal | Reason | Inertia Rejected Because |
|---|---|---|---|---|

Select exactly one and write it as output:

[ ] REMOVALS-PRESENT — table populated.
[ ] REMOVALS-EMPTY — inertia holds for all removal candidates.

---

**Reprioritizations**

| # | Item | Current | Proposed | Source Signal | Inertia Rejected Because |
|---|---|---|---|---|---|

Select exactly one and write it as output:

[ ] REPRIO-PRESENT — table populated.
[ ] REPRIO-EMPTY — current priority order holds.

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

**SECTION 4 CHECKPOINT**

Select exactly one and write it as output:

[ ] SECTION4-COMPLETE — all three types declared; slots selected for empty types;
    inertia verdicts present on all proposals.
[ ] SECTION4-INCOMPLETE — missing: ___

---

## SECTION 5: CALIBRATION + CONFIRM

**Calibration**

Select exactly one and write it as output:

[ ] CALIBRATION-SIGNIFICANT — 3+ proposals across multiple types.
[ ] CALIBRATION-MINOR — 1–2 proposals.
[ ] CALIBRATION-INERTIA — evidence does not require revision.

**Present to user**: Section 4 proposals + calibration verdict.
Net count: ___ additions, ___ removals, ___ reprioritizations.

Ask: `Confirm revisions? (yes / adjust / reject)`

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

**POST-CONFIRM SLOT**

Select exactly one and write it as output:

[ ] WRITE-CONFIRMED — "yes" received; writing strategy.md with confirmed revisions.
[ ] WRITE-ADJUSTED — "adjust" received; returning to Section 4.
[ ] WRITE-REJECTED — "reject" received; inertia selected; no write; closing cleanly.

---

## WRITE STEP — Update strategy.md

Execute only on WRITE-CONFIRMED or WRITE-ADJUSTED (after adjusted confirmation).

Rewrite `simulations/{{topic}}/strategy.md`:
- Updated date
- Revised coverage intent
- Updated priority order
- Open question resolutions and new open questions

**POST-WRITE SLOT**

Select exactly one and write it as output:

[ ] WRITE-COMPLETE — strategy.md rewritten with confirmed revisions.
[ ] WRITE-FAILED — error: ___
```

---

## V-05 — Combined: Inertia Framing + Slot Architecture + Narrative Format Contract

**Variation axes**: All three — Inertia framing + Output format (slots) + Narrative Format Contract
**Hypothesis**: Each axis closes a distinct failure mode: INERTIA-GATE blocks prevent status-quo omission; pre-printed slots eliminate composition risk at binary decisions; Narrative Format Contract upfront eliminates step-description drift before any execution pressure accumulates. All three can be active simultaneously without interference. Maximum constraint density at all three sites produces the highest-fidelity execution.

---

```
# topic:plan — Revise Signal Strategy

You are revising the signal strategy for {{topic}}.

---

## NARRATIVE FORMAT CONTRACT

**Required register**: Conclusion before evidence.
Lead every analytical output with the conclusion. Evidence follows.

**Required form**:
> "[Signal file] establishes [dimension] as uncovered — [evidence in one sentence]."

**Degenerate register — FAIL**: Step-description narrative.
> FAIL: "I will now read strategy.md and extract the current priorities."
> FAIL: "Next, I examined the signals to determine what has changed."

This contract applies at every analytical step. Degenerate register at any step is a
rubric failure. The contract is active before Step 1 runs.

---

## PREAMBLE — INERTIA BLOCK

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

This block is reproduced verbatim at Steps 3, 5, 7, and 8. Its presence is required at
each site. Absence is visible and constitutes a failure.

---

## OUTPUT SCHEMA

Five sections in order:
STRATEGY SNAPSHOT → SIGNAL SURVEY → DELTA ANALYSIS → REVISION PROPOSAL → CALIBRATION + CONFIRM.

**SCHEMA COMMITMENT**

Select exactly one and write it as output before reading any files:

[ ] SCHEMA-A — all five sections; conclusion-first register throughout; null-case slots
    for empty proposal types; pre-printed decision slots at all binary sites;
    INERTIA-GATE reproduced at all four required sites.
[ ] SCHEMA-B — adapted schema.

---

## SECTION 1: STRATEGY SNAPSHOT

Read `simulations/{{topic}}/strategy.md`.

Output (conclusion-first):

The strategy [is current / has N gaps against gathered signals], written on [date].
Coverage intent: [one sentence]. Priorities: [list]. Open questions: [list].

Do not describe reading the file. State what the file contains.

---

## SECTION 2: SIGNAL SURVEY

Read all signal files under `simulations/{{topic}}/`.

Output (conclusion-first):

[N] signals exist across [N] namespaces. The highest-signal finding is [one sentence].
[N] signals diverge from strategy intent.

Full list:

| Signal File | Namespace | Date | Key Finding | Diverges? |
|---|---|---|---|---|

**NULL-CASE SLOT**

Select exactly one and write it as output:

[ ] SIGNALS-FOUND — signals exist; survey populated; proceed.
[ ] SIGNALS-EMPTY — no signals found; output what signals are needed; do not proceed.

---

## SECTION 3: DELTA ANALYSIS

For each divergent signal, output one conclusion-first sentence, then the table row:

> "[Signal file] reveals [dimension] as [uncovered / deprioritized / contradicted] —
> [evidence]. Change type: [ADDITION / REMOVAL / REPRIORITIZATION]. Inertia verdict:
> [CHANGE REQUIRED / INERTIA HOLDS]."

| Signal File | Dimension | Type | Evidence | Inertia Verdict |
|---|---|---|---|---|
| | | [ADDITION]/[REMOVAL]/[REPRIO] | | [CHANGE REQUIRED]/[INERTIA HOLDS] |

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

**NULL-CASE SLOT — DELTA**

Select exactly one and write it as output:

[ ] DELTA-EXISTS — at least one signal diverges; proceed to Section 4.
[ ] NULL-DELTA — no divergence found; inertia holds universally; skip to Section 5.

---

## SECTION 4: REVISION PROPOSAL

Include only items where inertia was rejected in Section 3.

Output (conclusion-first for each entry, then table):

**Additions**

> "[Signal] establishes [dimension] — [evidence]. Inertia rejected because [reason]."

| # | Proposed Addition | Source | Evidence | Inertia Rejected Because |
|---|---|---|---|---|

Select exactly one and write it as output:

[ ] ADDITIONS-PRESENT — table populated; conclusion-first statements above each row.
[ ] ADDITIONS-EMPTY — inertia holds; no additions warranted.

---

**Removals**

| # | Proposed Removal | Source | Reason | Inertia Rejected Because |
|---|---|---|---|---|

Select exactly one and write it as output:

[ ] REMOVALS-PRESENT — table populated.
[ ] REMOVALS-EMPTY — inertia holds; no removals warranted.

---

**Reprioritizations**

| # | Item | Current | Proposed | Source | Inertia Rejected Because |
|---|---|---|---|---|---|

Select exactly one and write it as output:

[ ] REPRIO-PRESENT — table populated.
[ ] REPRIO-EMPTY — priority order holds.

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

**SECTION 4 CHECKPOINT**

Select exactly one and write it as output:

[ ] SECTION4-COMPLETE — all three types declared; empty types slotted; conclusion-first
    statements present; inertia verdicts on all proposals.
[ ] SECTION4-INCOMPLETE — missing: ___

---

## SECTION 5: CALIBRATION + CONFIRM

**Calibration** (conclusion-first):

This revision is [significant / minor / inertia holds]. Evidence: [one sentence].

Select exactly one and write it as output:

[ ] CALIBRATION-SIGNIFICANT — 3+ proposals across multiple change types.
[ ] CALIBRATION-MINOR — 1–2 proposals.
[ ] CALIBRATION-INERTIA — evidence does not require revision.

**Present to user**: Section 4 + calibration verdict.
Net count: ___ additions, ___ removals, ___ reprioritizations.

Ask: `Confirm revisions? (yes / adjust / reject)`

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

**POST-CONFIRM SLOT**

Select exactly one and write it as output:

[ ] WRITE-CONFIRMED — "yes"; writing strategy.md.
[ ] WRITE-ADJUSTED — "adjust"; returning to Section 4 with changes.
[ ] WRITE-REJECTED — "reject"; inertia chosen; no write; close cleanly.

---

## WRITE STEP — Update strategy.md

Execute only on WRITE-CONFIRMED or WRITE-ADJUSTED (after new confirmation).

Rewrite `simulations/{{topic}}/strategy.md`. Lead the document with a conclusion-first
revision note: "[N] revisions applied — [one sentence summary]. Date: [today]."

Then: updated coverage intent, priorities, open question resolutions, new open questions.

**[INERTIA-GATE]**
> Inertia is a co-equal option at every decision point in this skill.
> "No change" is a valid and often correct outcome.
> Before proposing any revision: does the evidence require this change, or is the
> existing strategy sufficient? Mark every proposal with an explicit inertia verdict.
> A response that produces proposals without inertia verdicts has failed this gate.

**POST-WRITE SLOT**

Select exactly one and write it as output:

[ ] WRITE-COMPLETE — strategy.md rewritten with confirmed revisions.
[ ] WRITE-FAILED — error: ___

---

## PHASE 3 EXIT GATE

Before any write, verify:

- [ ] Narrative Format Contract honored at every step — no degenerate register produced
- [ ] INERTIA-GATE block reproduced verbatim at Steps 3, 5, 7, and 8
- [ ] Pre-printed slots selected (not left blank) at all binary decision sites
- [ ] Section 4 contains only items where inertia was explicitly rejected in Section 3
- [ ] User confirmed before reaching write step

If any item unchecked: return to failing step and correct before writing.
```

---

## Variation Axis Summary

| Variation | Axis | Discriminating Test |
|---|---|---|
| V-01 | Inertia framing | INERTIA-GATE block defined once in preamble; reproduced at 4 sites; absent block is visible failure |
| V-02 | Output format / slot architecture | Pre-printed `[ ] A / [ ] B` slots at every binary decision site — schema commitment, null cases, type rows, checkpoint verdicts, post-confirm, post-write |
| V-03 | Phrasing register + Narrative Format Contract | Named contract block before Step 1; requires conclusion-first at all steps; names degenerate register explicitly; Phase 3 Exit Gate checks register compliance |
| V-04 | Inertia + Output format | Both failure modes addressed: inertia omission (GATE blocks) + composition drift (slots); neither implies the other |
| V-05 | All three axes | Maximum constraint density: GATE blocks + slots + upfront register contract; Phase 3 Exit Gate verifies all three simultaneously |
