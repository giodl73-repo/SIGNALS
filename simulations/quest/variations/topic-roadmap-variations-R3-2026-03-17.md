Now I have the full T3 body and rubric context. Generating the 5 variations:

---

# quest-variate — topic-plan (Round 3)

**Skill:** topic-plan (topic-roadmap signal strategy revision)
**Rubric version:** v3
**N variations:** 5 (3 single-axis + 2 combinations)

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Inertia framing | Protagonist framing ("defeat NO CHANGE") improves C-01 compliance |
| V-02 | Output format (table-heavy) | All-table structure improves verifiability and C-02/C-03 precision |
| V-03 | Phrasing register (conversational) | Plain imperative language reduces instruction-following errors |
| V-04 | Role sequence + lifecycle emphasis | Named roles with explicit phase budgets reduce phase-bleed |
| V-05 | Inertia framing + prose delta | Status-quo protagonist + narrative delta improves unexpected-finding depth |

---

## V-01 — Inertia Protagonist Framing

**Axis:** Inertia framing
**Hypothesis:** Casting NO CHANGE as the explicit first-class output — not a fallback — sharpens the evidence bar for every proposal and improves C-01 pass rates.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---

## YOUR DEFAULT OUTPUT IS: NO CHANGES TO STRATEGY.MD

This is not a hedging disclaimer. It is the starting state.
Every step below is an attempt to defeat that default with evidence.
If no evidence defeats it, the run ends with: "Inertia holds. strategy.md unchanged."
That is a successful, complete execution of this skill.

You are running /topic:plan for the topic named in the user's message.

---

## WHAT DEFEATS THE DEFAULT

One thing defeats NO CHANGE: a NEW signal artifact (dated after strategy.md)
that reveals a dimension the strategy did not account for, got wrong,
or covered at the wrong priority. Volume of signals is not evidence.
Agreement between signals is not evidence. Only a named artifact
with a named delta defeats the default.

---

## GATE DECLARATION

Before Step 1: commit to three named gates.

Gate 1 -- READ-TO-ANALYSIS: you will emit exactly
  GATE CHECK PASSED -- READ-TO-ANALYSIS
before delta analysis opens. You are committing to this now.

Gate 2 -- ANALYSIS-TO-CONFIRMATION: you will emit exactly
  GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION
before the proposal table is shown. You are committing to this now.

Gate 3 -- CONFIRMATION-TO-APPLY: you will emit exactly
  GATE CHECK PASSED -- CONFIRMATION-TO-APPLY
after the user replies YES or REVISED. You are committing to this now.

Emit now:

| Gate | Token | Status |
|------|-------|--------|
| GC-1 READ-TO-ANALYSIS | GATE CHECK PASSED -- READ-TO-ANALYSIS | committed |
| GC-2 ANALYSIS-TO-CONFIRMATION | GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION | committed |
| GC-3 CONFIRMATION-TO-APPLY | GATE CHECK PASSED -- CONFIRMATION-TO-APPLY | committed |

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md` for the strategy file path. Read strategy.md.
Record: STRATEGY DATE (last-modified date). This date is the cutoff for NEW vs PRIOR.

Extract every stated strategy dimension. For each dimension, ask:
"What assumption is this dimension making that a signal could challenge?"

| Assumption | Strategy dimension it underlies | What would invalidate it |
|------------|--------------------------------|--------------------------|

If no implicit assumptions found:
"ASSUMPTIONS: none -- all strategy elements are explicitly stated."

---

## Step 2 -- Pre-Signal Defense Register

Before reading any artifact: record why each strategy dimension might deserve to stay.
This is the status quo's opening argument.

| Defense ID | Strategy dimension | Best argument for keeping it | What signal finding would defeat this |

---

## Step 3 -- Signal inventory

Glob `simulations/` for artifacts matching the topic slug.
Classify each: NEW (date > STRATEGY DATE) or PRIOR.
All 9 namespaces assessed: scout / draft / review / flow / trace / prove / listen / program / topic.

| Artifact filename | Date | NEW / PRIOR | Namespace |

If no artifacts: "SIGNAL INVENTORY: null -- no artifacts found for topic [name]. Cannot run /topic:plan."

SIGNAL READ-LOCK: signal files may not be re-read after this step.

---

## NO-CHANGE CHECKPOINT

After the inventory: how many NEW artifacts exist?

- Zero NEW artifacts: emit "INERTIA HOLDS -- no new signals since strategy date.
  strategy.md unchanged. Run complete." Stop here.
- One or more NEW artifacts: continue to delta analysis.

---

GATE CHECK PASSED -- READ-TO-ANALYSIS

---

## Step 3b -- Delta findings

For each NEW artifact, classify its findings. Four categories. Do not merge.
Every entry requires a two-part citation:
  [Source: {filename}] Understanding changed: {prior} -> {now}
An entry without both parts is structurally incomplete.

### CONFIRMED -- strategy assumptions the new signal backs up
| Finding ID | Assumption confirmed | Source artifact | Citation | Defeats NO CHANGE? |

If none: "CONFIRMED: none -- no NEW artifacts confirm existing assumptions."

### EXPANDED -- strategy dimensions the new signal reveals are wider than assumed
| Finding ID | Assumption | Expanded to | Source artifact | Citation | Defeats NO CHANGE? |

If none: "EXPANDED: none -- no NEW artifacts expand existing assumptions."

### UNEXPECTED -- dimensions the strategy did not cover that new signals revealed
| Finding ID | Gap (what was missing) | What signal revealed | Source artifact | Citation | Defeats NO CHANGE? |

If none: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### CHALLENGED -- strategy assumptions the new signal directly contradicts
| Finding ID | Strategy assumed | Signal challenges | Source artifact | Citation | Defeats NO CHANGE? |

If none: "CHALLENGED: none -- no NEW artifacts challenge existing strategy."

---

## NO-CHANGE RE-CHECK

Scan the "Defeats NO CHANGE?" column above.
If every entry is NO: emit "INERTIA HOLDS -- all findings confirm or expand
  but none defeat the keep-unchanged option. strategy.md unchanged. Run complete."
  Stop here.

If any entry is YES: continue to proposals.

---

GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION

---

## Step 4 -- Proposals

  +------------------------------------------------------------------+
  | DEFAULT REMAINS: NO CHANGE                                       |
  | Each row below is an attempt to defeat that default.             |
  | A row without a named artifact and a concrete consequence        |
  | of deferral does not defeat the default. Remove it.             |
  +------------------------------------------------------------------+

### Additions
Only findings where "Defeats NO CHANGE?" = YES enter this table.

| # | Dimension | Finding ID | Evidence artifact | Before (absent) | After (proposed) | Confidence | If deferred | Reversibility | Why NO CHANGE loses |

If none: "ADDITIONS: none -- inertia holds."

### Removals and Reprioritizations
Same evidence bar as additions.

| # | Action | Dimension | Finding ID | Evidence artifact | Before | After | Confidence | If deferred | Reversibility | Why NO CHANGE loses |

If none for removals: "REMOVALS: none -- inertia holds."
If none for reprioritizations: "REPRIORITIZATIONS: none -- inertia holds."

### Defense Check
For every proposal row: has the Defense Register argument been addressed?

| Proposal # | Defense ID challenged | Was it addressed? | If not: proposal withdrawn |

### Conflict Check
Do any NEW artifacts contradict each other on the same dimension?

| Conflict ID | Signal A | Signal B | Nature | Resolution |

If none: "CONFLICT AUDIT: none."

---

## Step 5 -- Diff

Show only dimensions with accepted proposals.

  +------------------------------------------------------------------+
  | DEFAULT REMAINS: NO CHANGE until user confirms.                  |
  +------------------------------------------------------------------+

| Dimension | Before | After [evidence] | Proposal # |

---

## Step 6 -- Confirmation gate

Display: delta findings / proposals / diff.

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

The default outcome is still: no changes.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove proposals before confirming
---

Stop. Write nothing until the user replies.

---

After YES or REVISED:

GATE CHECK PASSED -- CONFIRMATION-TO-APPLY

## Step 7 -- Apply

Write exactly the confirmed changes. No reformatting of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02 — Table-Heavy Output Format

**Axis:** Output format
**Hypothesis:** Maximizing structural table coverage at every phase — including assumption extraction, delta categories, and gate compliance — produces outputs that are more parseable, verifiable, and consistently pass C-02 and C-03.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---

## INERTIA PRIOR

strategy.md unchanged is the default outcome.
The burden of proof rests on change.
A run producing zero proposals is valid and complete.

You are running /topic:plan for the topic named in the user's message.

---

## GATE MANIFEST TABLE

Emit this table now. It is a required pre-execution artifact.

| Gate ID | Name | Token string | When emitted |
|---------|------|-------------|--------------|
| GC-1 | READ-TO-ANALYSIS | GATE CHECK PASSED -- READ-TO-ANALYSIS | After Step 3 inventory, before Step 3b |
| GC-2 | ANALYSIS-TO-CONFIRMATION | GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION | After Step 3b, before Step 4 |
| GC-3 | CONFIRMATION-TO-APPLY | GATE CHECK PASSED -- CONFIRMATION-TO-APPLY | After user YES/REVISED, before Step 7 |

Token strings are fixed. A token that differs from the table above is a structural error.

---

## PRE-EXECUTION SCHEMA COMMITMENT

I commit to the following table structures. Columns are fixed. No prose substitutes.
No table merges. No column renames.

| Table | Step | Mandatory columns |
|-------|------|-------------------|
| Assumption table | 1 | Assumption / Source dimension / Implicit evidence / Delta-candidate |
| Pre-defense register | 2 | Defense ID / Dimension / Keep argument / Invalidation condition |
| Signal inventory | 3 | Filename / Date / NEW\|PRIOR / Namespace |
| CONFIRMED findings | 3b-1 | Finding ID / Assumption confirmed / Source artifact / Citation / Delta-candidate |
| EXPANDED findings | 3b-2 | Finding ID / Assumption / Expanded to / Source artifact / Citation / Delta-candidate |
| UNEXPECTED findings | 3b-3 | Finding ID / Strategy gap / Revealed / Source artifact / Citation / Delta-candidate |
| CHALLENGED findings | 3b-4 | Finding ID / Strategy assumed / Challenged by / Source artifact / Citation / Delta-candidate |
| Additions | 4a | # / Dimension / Finding ID / Evidence / Before / After / Confidence / If deferred / Reversibility / Inertia Rejected Because |
| Removals+Repri | 4b | # / Action / Dimension / Finding ID / Evidence / Before / After / Confidence / If deferred / Reversibility / Inertia Rejected Because |
| Defender challenge | 4c | Defense ID / Proposal # / Decision defended / Defense argument / Strength |
| Conflict audit | 5 | Conflict ID / Signal A / Signal B / Nature / Resolution |
| Diff | 6 | Dimension / Before / After [evidence] / Proposal |

---

## Step 1 -- Assumption extraction

Read `simulations/TOPICS.md` for strategy file path. Read strategy.md.
Record STRATEGY DATE as the last-modified date.

| Assumption | Source dimension | Implicit evidence | Delta-candidate |
|------------|-----------------|-------------------|-----------------|

Null row: "ASSUMPTIONS: none -- all dimensions explicitly stated."
(Delta-candidate values: Yes / No / Pending signal)

---

## Step 2 -- Pre-Signal Defense Register

Before reading any artifact. Populate from strategy.md only.

| Defense ID | Strategy dimension | Keep argument | Invalidation condition |
|------------|--------------------|--------------|----------------------|

---

## Step 3 -- Signal inventory

Glob `simulations/` for topic-slug artifacts. Classify vs STRATEGY DATE.
Every namespace must appear in the table; use explicit null rows for absent namespaces.

| Artifact filename | Date | NEW / PRIOR | Namespace |
|-------------------|------|-------------|-----------|
| (none) | — | — | scout: no artifacts |
| (none) | — | — | draft: no artifacts |
| ... | | | |

SIGNAL READ-LOCK active after this step.

| Namespace | Artifact count NEW | Artifact count PRIOR |
|-----------|-------------------|----------------------|
| scout | | |
| draft | | |
| review | | |
| flow | | |
| trace | | |
| prove | | |
| listen | | |
| program | | |
| topic | | |
| **TOTAL** | | |

---

GATE CHECK PASSED -- READ-TO-ANALYSIS

---

## Step 3b -- Delta findings

Citation format required for every row:
  [Source: {filename}] Understanding changed: {prior} -> {now}

### 3b-1 CONFIRMED

| Finding ID | Assumption confirmed | Source artifact | Citation | Delta-candidate |
|------------|---------------------|-----------------|----------|-----------------|

Null: "CONFIRMED: none."

### 3b-2 EXPANDED

| Finding ID | Assumption | Expanded to | Source artifact | Citation | Delta-candidate |
|------------|------------|-------------|-----------------|----------|-----------------|

Null: "EXPANDED: none."

### 3b-3 UNEXPECTED

| Finding ID | Strategy gap | Revealed | Source artifact | Citation | Delta-candidate |
|------------|-------------|---------|-----------------|----------|-----------------|

Null: "UNEXPECTED: none."

### 3b-4 CHALLENGED

| Finding ID | Strategy assumed | Challenged by | Source artifact | Citation | Delta-candidate |
|------------|-----------------|---------------|-----------------|----------|-----------------|

Null: "CHALLENGED: none."

### Delta summary table

| Category | Finding count | Delta-candidate: Yes | Delta-candidate: No |
|----------|--------------|---------------------|---------------------|
| CONFIRMED | | | |
| EXPANDED | | | |
| UNEXPECTED | | | |
| CHALLENGED | | | |

---

GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION

---

## Step 4 -- Change proposals

Proposals limited to rows where Delta-candidate = Yes in Step 3b.
A proposal without a named consequence of deferral is structurally invalid.

### 4a -- Additions

| # | Dimension | Finding ID | Evidence | Before | After | Confidence | If deferred | Reversibility | Inertia Rejected Because |
|---|-----------|-----------|----------|--------|-------|-----------|-------------|---------------|--------------------------|

Null: "ADDITIONS: none -- inertia holds."
(Reversibility values: Reversible at same cost / Gets harder / Becomes impossible)

### 4b -- Removals and Reprioritizations

| # | Action | Dimension | Finding ID | Evidence | Before | After | Confidence | If deferred | Reversibility | Inertia Rejected Because |
|---|--------|-----------|-----------|----------|--------|-------|-----------|-------------|---------------|--------------------------|

Null rows:
"REMOVALS: none -- inertia holds."
"REPRIORITIZATIONS: none -- inertia holds."
(Action values: REMOVE / REPRIORITIZE)

### 4c -- Defender Challenge Table

| Defense ID | Proposal # | Decision defended | Defense argument | Strength |
|------------|-----------|------------------|-----------------|----------|

Calibration: count Weak / Moderate / Strong.
"All Weak -> calibration: rubber-stamp risk."
"All Strong -> calibration: over-zealous risk."
Otherwise: "Calibration: balanced."

---

## Step 5 -- Conflict audit

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |
|-------------|---------|---------|-------------------|------------|

Null: "CONFLICT AUDIT: none."

---

## Step 6 -- Diff

| Dimension | Before | After [evidence bracket] | Proposal |
|-----------|--------|--------------------------|---------|

---

## Step 7 -- Confirmation gate

Display: Steps 3b / 4a / 4b / 4c / 6.

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES | NO | REVISED + edited table | WITHDRAW [#]
---

Stop. Write nothing until the user replies.

---

After YES or REVISED:

GATE CHECK PASSED -- CONFIRMATION-TO-APPLY

## Step 8 -- Apply

Write exactly the confirmed changes. No reformatting of unchanged sections.

| Applied | Count |
|---------|-------|
| Additions | |
| Removals | |
| Reprioritizations | |

"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03 — Conversational/Imperative Register

**Axis:** Phrasing register
**Hypothesis:** Plain second-person imperative instructions ("Read this. Do that. If nothing changed, say so.") reduce abstraction-layer errors and improve gate compliance without the cognitive load of formal schema language.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---

You are running /topic:plan. Here is exactly what you will do.

**Your default outcome is: do nothing.** You only change strategy.md if you
find a new signal artifact that proves the strategy missed something, got
something wrong, or is covering the right thing at the wrong priority.
If you don't find that, say "inertia holds" and stop. That is a successful run.

---

## Before you start: three checkpoints

You will hit three checkpoints during this run. At each one you say a specific
phrase. No variations. If you skip one, the run is broken.

Checkpoint 1 — after you finish reading: say `GATE CHECK PASSED -- READ-TO-ANALYSIS`
Checkpoint 2 — after you finish your analysis: say `GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION`
Checkpoint 3 — after the user says YES: say `GATE CHECK PASSED -- CONFIRMATION-TO-APPLY`

Say this now to confirm you're committing:

> I commit to emitting exactly:
> - GATE CHECK PASSED -- READ-TO-ANALYSIS at Checkpoint 1
> - GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION at Checkpoint 2
> - GATE CHECK PASSED -- CONFIRMATION-TO-APPLY at Checkpoint 3

---

## Step 1 -- Read the strategy

Open `simulations/TOPICS.md`. Find where the strategy file is for this topic.
Open strategy.md. Write down:
- The date it was last modified (call this the STRATEGY DATE)
- Every coverage dimension it describes (what it plans to gather, in what order, and how it knows it's done)

For each dimension, ask: what assumption is baked into this? Write a row:

| Assumption | Which dimension it's in | What would prove it wrong |

If no hidden assumptions: write "ASSUMPTIONS: none."

---

## Step 2 -- Write the defense before you read anything

Before looking at any signal file: for each strategy dimension, write down
the best argument for keeping it exactly as-is.

| ID | Dimension | Best reason to keep it | What would change my mind |

This is the strategy's opening argument. You're going to test it in Step 3b.

---

## Step 3 -- Take inventory of signals

Find every signal file in `simulations/` that matches this topic. For each one:
- Is its date newer than STRATEGY DATE? If yes: mark NEW. If no: mark PRIOR.

| File | Date | NEW or PRIOR | Namespace |

Check all 9 namespaces: scout / draft / review / flow / trace / prove / listen / program / topic.
If a namespace has nothing, say so explicitly.

After you write this table: stop reading signal files. Don't go back to them.
Everything you need is in the table.

If there are zero NEW files: write "Inertia holds -- no signals since strategy date.
strategy.md unchanged." and stop.

---

GATE CHECK PASSED -- READ-TO-ANALYSIS

---

## Step 3b -- What did the new signals change?

For every NEW file in your inventory: what did it tell you that changed your
understanding of the strategy? Put each finding in one of four buckets.
For every finding, say: what did you think before, and what do you know now?

Format: [Source: {filename}] Understanding changed: {what you assumed} -> {what you now know}

### Confirmed
Things you already expected that the new signal backs up.

| ID | What was confirmed | File | Citation |

If nothing: "CONFIRMED: none."

### Expanded
Things the strategy was roughly right about, but the new signal shows are
bigger, more complex, or cover more ground than assumed.

| ID | Original assumption | What it expanded to | File | Citation |

If nothing: "EXPANDED: none."

### Unexpected
Things the strategy simply didn't address that the new signal surfaced.

| ID | What was missing | What the signal revealed | File | Citation |

If nothing: "UNEXPECTED: none."

### Challenged
Things the strategy got wrong, or assumed that the new signal contradicts.

| ID | What the strategy assumed | What the signal says instead | File | Citation |

If nothing: "CHALLENGED: none."

---

After filling in all four buckets: look at what you have.
Do any findings actually argue for changing the strategy?
If no: write "Inertia holds -- findings confirm or expand but do not require change." Stop.

---

GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION

---

## Step 4 -- Propose changes

Only for findings that genuinely argue for change. For each one:
- Say what you want to do: ADD / REMOVE / REPRIORITIZE
- Say what the strategy looked like before
- Say what it should look like after
- Name the file that proved the change is needed
- Say what happens if you don't make this change
- Say why "leave it alone" is not the right call here

### Additions

| # | What to add | Why (finding) | Evidence file | Before (nothing) | After (proposed) | Confidence | If skipped | Gets harder to reverse? | Why not leave it alone |

If nothing: "ADDITIONS: none -- inertia holds."

### Removals and Reprioritizations

| # | ADD/REMOVE/REPRIORITIZE | What changes | Why (finding) | Evidence file | Before | After | Confidence | If skipped | Gets harder to reverse? | Why not leave it alone |

If nothing to remove: "REMOVALS: none -- inertia holds."
If nothing to reprioritize: "REPRIORITIZATIONS: none -- inertia holds."

---

## Step 4b -- Challenge your own proposals

Go back to Step 2. Does the defense hold against each proposal?
Rate each challenge: Strong / Moderate / Weak.

| Defense ID | Proposal # | Is the defense answered? | Challenge strength |

Count the ratings. If they're all Weak: say "Warning: all defenses rated Weak --
rubber-stamp risk." If all Strong: say "Warning: all Strong -- may be over-defending."

---

## Step 5 -- Do any new signals contradict each other?

If two new signals say opposite things about the same dimension:

| Conflict ID | Signal A | Signal B | What they disagree on | How to resolve |

If none: "CONFLICT AUDIT: none."

---

## Step 6 -- Show the diff

For each strategy dimension that would change, show before and after.

| Dimension | Before | After [cite the evidence] | Proposal # |

---

## Step 7 -- Ask before touching anything

Show the user: your delta findings, your proposals, the diff.

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to leave strategy.md alone | REVISED + edited table | WITHDRAW [#]
---

Do not write anything else. Wait.

---

After user replies YES or REVISED:

GATE CHECK PASSED -- CONFIRMATION-TO-APPLY

## Step 8 -- Write the changes

Apply only what the user confirmed. Don't reformat sections you didn't change.

Say: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04 — Role Sequence + Lifecycle Emphasis

**Axis combination:** Role sequence + lifecycle emphasis
**Hypothesis:** Assigning named roles with explicit phase budgets and hard enter/exit conditions produces better separation of analysis from proposal-making, reducing the most common failure mode (proposals before delta).

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---

## INERTIA PRIOR

strategy.md unchanged is the default outcome. This prior governs all four
phases. Evidence from NEW artifacts defeats it; volume and agreement do not.

You are running /topic:plan for the topic named in the user's message.

---

## EXECUTION MODEL: FOUR-PHASE LIFECYCLE

This skill runs four named phases. Each phase has:
- An owner role
- An entry condition (what must be true before the phase opens)
- An exit token (emitted when the phase is complete and the next may open)
- An exit condition (what output must exist before the token is emitted)

| Phase | Role | Entry condition | Exit token | Exit condition |
|-------|------|----------------|------------|----------------|
| P1: READ | Signal Reader | None | GATE CHECK PASSED -- READ-TO-ANALYSIS | strategy.md read; assumption table written; signal inventory written; SIGNAL READ-LOCK in effect |
| P2: ANALYZE | Delta Analyst | P1 exit token emitted | GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION | All four delta categories written; defender challenge table initialized |
| P3: PROPOSE | Change Architect | P2 exit token emitted | (user reply YES/REVISED) | Proposals written; diff shown; confirmation prompt emitted; execution halted |
| P4: APPLY | Change Architect | P3 exit (user YES/REVISED) | GATE CHECK PASSED -- CONFIRMATION-TO-APPLY | Changes written to strategy.md; confirmation message emitted |

You commit to this lifecycle now, before P1 opens. A phase that opens without
its entry condition being met is a structural violation.

---

## P1: READ -- Signal Reader

**Entry condition:** none
**Owner:** Signal Reader
**Budget:** complete before any delta classification begins

### P1-a: Read strategy.md

Read `simulations/TOPICS.md`. Locate strategy file path. Read strategy.md.
Record: STRATEGY DATE (last-modified date of strategy.md).

Extract every stated strategy dimension. For each, identify the implicit
assumption -- the belief that would have to be false for this dimension
to need changing.

| Assumption | Underlying dimension | Implicit evidence | Delta-candidate |

Null: "ASSUMPTIONS: none -- all elements explicitly stated."
(Delta-candidate: Yes / No / Pending signal)

### P1-b: Pre-Signal Defense Register

Before any artifact is read: what are the strongest arguments for keeping
each strategy dimension unchanged?

| Defense ID | Dimension | Keep argument | Falsification condition |

### P1-c: Signal inventory

Glob `simulations/` for the topic slug. Every artifact gets a row.
Classify vs STRATEGY DATE. All 9 namespaces explicitly represented.

| Filename | Date | NEW / PRIOR | Namespace |

Namespace null rows required: "scout: 0 artifacts" etc.

SIGNAL READ-LOCK: no signal files may be re-read after this table is written.

If zero NEW artifacts: emit "INERTIA HOLDS -- no new signals since strategy date.
strategy.md unchanged. P1 complete. Run ends." Stop.

---

GATE CHECK PASSED -- READ-TO-ANALYSIS

*P1 closed. P2 now open.*

---

## P2: ANALYZE -- Delta Analyst

**Entry condition:** P1 exit token emitted; SIGNAL READ-LOCK active
**Owner:** Delta Analyst
**Constraint:** Delta Analyst reads only the P1 inventory table, not the
  original signal files. SIGNAL READ-LOCK is in effect.
**Budget:** four delta categories, then defender pre-challenge

### P2-a: Delta findings

For every NEW artifact in the inventory: classify each finding.
Citation required for every entry:
  [Source: {filename}] Understanding changed: {prior} -> {now}

#### CONFIRMED
| Finding ID | Assumption confirmed | Source | Citation | Delta-candidate |

Null: "CONFIRMED: none -- no NEW artifacts confirm existing assumptions."

#### EXPANDED
| Finding ID | Original assumption | Expanded to | Source | Citation | Delta-candidate |

Null: "EXPANDED: none."

#### UNEXPECTED
| Finding ID | Strategy gap | Signal revealed | Source | Citation | Delta-candidate |

Null: "UNEXPECTED: none."

#### CHALLENGED
| Finding ID | Strategy assumed | Signal challenges | Source | Citation | Delta-candidate |

Null: "CHALLENGED: none."

### P2-b: Delta Analyst verdict

After all four categories: how many findings have Delta-candidate = Yes?

If zero: "DELTA ANALYST VERDICT: no findings defeat the keep-unchanged option.
Inertia holds. P2 complete. Run ends."  Stop.

If one or more: "DELTA ANALYST VERDICT: [N] findings are candidates for
strategy change. Passing to Change Architect."

---

GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION

*P2 closed. P3 now open.*

---

## P3: PROPOSE -- Change Architect

**Entry condition:** P2 exit token emitted; P2 delta findings in output
**Owner:** Change Architect
**Constraint:** Change Architect may only propose changes backed by
  Delta-candidate = Yes findings from P2. A proposal with no P2 finding
  reference is structurally invalid.

### P3-a: Additions

| # | Dimension | P2 Finding | Evidence | Before | After | Confidence | If deferred | Reversibility | Inertia Rejected Because |

Null: "ADDITIONS: none -- inertia holds."
(Reversibility: Reversible at same cost / Gets harder / Becomes impossible)

### P3-b: Removals and Reprioritizations

| # | Action | Dimension | P2 Finding | Evidence | Before | After | Confidence | If deferred | Reversibility | Inertia Rejected Because |

Null rows:
"REMOVALS: none -- inertia holds."
"REPRIORITIZATIONS: none -- inertia holds."

### P3-c: Defender Challenge

Revisit the P1-b Defense Register. For each proposal, does it address the
defense? Rate: Strong / Moderate / Weak.

| Defense ID | Proposal # | Defense argument | Addressed? | Strength |

Calibration: "All Weak = rubber-stamp risk / All Strong = over-zealous risk /
Mixed = balanced."

### P3-d: Conflict audit

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none."

### P3-e: Diff

| Dimension | Before | After [evidence] | Proposal # |

### P3-f: Confirmation prompt

Display: P2 delta findings / P3-a / P3-b / P3-c (with calibration) / P3-e.

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals
---

*P3 suspended. Execution halted. Write nothing until user replies.*

---

## P4: APPLY -- Change Architect

**Entry condition:** User replied YES or REVISED
**Owner:** Change Architect

GATE CHECK PASSED -- CONFIRMATION-TO-APPLY

Write exactly the confirmed (non-withdrawn) changes.
No additional formatting of unchanged sections.

"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."

*P4 closed. Run complete.*
```

---

## V-05 — Inertia Protagonist + Prose Delta Narrative

**Axis combination:** Inertia framing + output format (prose delta)
**Hypothesis:** Casting inertia as the protagonist AND writing delta analysis as a narrative paragraph per finding (vs table rows) produces richer unexpected-dimension capture (C-09/C-10 aspirational) — because narrative form forces the writer to articulate the "before understanding" that table cells often skip.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
param_set: lean
---

## THIS SKILL HAS A DEFAULT OUTCOME

The default outcome of this skill is:
  **No changes to strategy.md.**

Every step is a structured challenge against that default.
The default wins unless a named NEW artifact names a concrete
dimension the strategy missed, got wrong, or prioritized incorrectly.

You are running /topic:plan for the topic named in the user's message.

---

## GATE COMMITMENT

Before Step 1 executes: commit to three gate tokens.

I will emit exactly:
  GATE CHECK PASSED -- READ-TO-ANALYSIS   after Step 3, before Step 3b
  GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION   after Step 3b, before Step 4
  GATE CHECK PASSED -- CONFIRMATION-TO-APPLY   after user YES/REVISED, before Step 7

Tokens are fixed strings. I will not vary them.

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md`. Locate strategy file. Read strategy.md.
Record STRATEGY DATE (last-modified date).

For each strategy dimension: write a one-sentence implicit assumption test.
"This dimension assumes ___ is true. If a signal shows ___ is false, this
dimension needs to change."

| Assumption | Dimension | Falsification test |

Null: "ASSUMPTIONS: none."

---

## Step 2 -- Pre-read defense

Before reading any signal file: for each strategy dimension, write the
strongest argument for leaving it exactly as it is.

| Defense ID | Dimension | Strongest keep-it argument |

---

## Step 3 -- Signal inventory

Glob `simulations/` for topic-slug artifacts. All 9 namespaces assessed.
Classify vs STRATEGY DATE.

| Filename | Date | NEW / PRIOR | Namespace |

SIGNAL READ-LOCK active. No re-reads after this table.

If no NEW artifacts: "INERTIA HOLDS -- no new signals.
strategy.md unchanged. Run complete." Stop.

---

GATE CHECK PASSED -- READ-TO-ANALYSIS

---

## Step 3b -- Delta narrative

For each NEW artifact in the inventory: write a narrative paragraph that answers:
  "Before this signal, the strategy assumed ___. This artifact showed ___.
  The gap between those two things is ___."

If the gap is zero (signal confirms the strategy): label the paragraph CONFIRMED.
If the gap reveals the strategy was roughly right but smaller than reality: label EXPANDED.
If the gap reveals a dimension the strategy never addressed: label UNEXPECTED.
If the gap reveals the strategy was wrong: label CHALLENGED.

Each paragraph must name the source artifact and state what understanding changed.
A paragraph without these two elements is structurally incomplete.

After all paragraphs: collect findings into a summary table.

| Finding ID | Label | Source artifact | Prior understanding | Current understanding | Delta-candidate |

Null declarations required per category:
  "CONFIRMED: none." / "EXPANDED: none." / "UNEXPECTED: none." / "CHALLENGED: none."
(Delta-candidate: Yes / No / Pending signal)

---

## NO-CHANGE ASSESSMENT

Scan Delta-candidate column.
All No: "INERTIA HOLDS -- all findings confirm or expand without defeating
keep-unchanged. strategy.md unchanged. Run complete." Stop.
Any Yes: continue.

---

GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION

---

## Step 4 -- Proposals

The default is still: no change. Each row below must name the finding that
defeats it, the specific consequence of deferral, and why "leave it alone"
is not acceptable.

### Additions

| # | Dimension | Finding ID | Evidence | Before | After | Confidence | If deferred | Reversibility | Why inertia loses |

Null: "ADDITIONS: none -- inertia holds."

### Removals and Reprioritizations

| # | Action | Dimension | Finding ID | Evidence | Before | After | Confidence | If deferred | Reversibility | Why inertia loses |

Null rows:
"REMOVALS: none -- inertia holds."
"REPRIORITIZATIONS: none -- inertia holds."

---

## Step 4b -- Defense challenge

| Defense ID | Proposal # | Defense argument | Proposal response | Challenge strength |

Calibration note after table. All Weak = rubber-stamp risk; all Strong = over-zealous.

---

## Step 5 -- Conflict audit

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none."

---

## Step 6 -- Diff

The default is still: no change. This table shows what changes if YES is given.

| Dimension | Before | After [evidence] | Proposal # |

---

## Step 7 -- Confirmation gate

Display: delta narrative (Step 3b) / proposals / diff.

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.
The default outcome remains: no changes.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals
---

Stop. Write nothing until user replies.

---

After YES or REVISED:

GATE CHECK PASSED -- CONFIRMATION-TO-APPLY

## Step 8 -- Apply

Write exactly the confirmed changes. No reformatting of unchanged sections.

"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Variation Summary

| Variation | Key differentiator | Expected C-01 | Expected C-02 | Expected C-03 | Expected C-04 | Risk |
|-----------|-------------------|---------------|---------------|---------------|---------------|------|
| V-01 | NO CHANGE as protagonist; mid-stream inertia checkpoints that can halt early | High — two early-halt checkpoints | High — halt before proposals if no delta | High | High | May halt too aggressively on sparse signal sets |
| V-02 | All-table format including delta summary and namespace coverage tables | Moderate — inertia in prose preamble only | Very high — structured table forces ordering | Very high — column contract forces all fields | High | Schema weight may crowd out aspirational depth (C-09/C-10) |
| V-03 | Plain imperative language; "you" voice throughout | High — plain language = harder to skip | High — explicit ordering in plain steps | Moderate — less formal column contract | High | Reduced column enforcement may weaken C-03/C-05 |
| V-04 | Named roles with lifecycle phase budgets and entry/exit conditions | High — phase contract enforces ordering | Very high — P1/P2 phase boundary is hard gate | High | Very high — P3 halts with hard confirmation prompt | Phase overhead may add verbosity without quality gain |
| V-05 | Inertia protagonist + narrative delta paragraphs | High — two NO CHANGE assessments | High — narrative before proposals | Moderate — finding IDs referenced in proposal rows | High | Narrative format may produce richer unexpected findings (C-09) but weaker citation traceability (C-06) |
