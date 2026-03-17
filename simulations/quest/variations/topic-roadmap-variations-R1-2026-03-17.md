Now I have the full picture. Writing the 5 variations.

---

# /quest:variate — topic-roadmap (topic-plan) — Round 1

**Skill:** Signal strategy revision as new information arrives.
**Rubric file:** `simulations/quest/rubrics/topic-roadmap-rubric-v1-2026-03-17.md`
**Variation axes selected for single-axis:** Inertia framing / Output format / Lifecycle emphasis
**Combination axes:** Phrasing register + Role sequence (V-04); Simplified gates + Embedded inertia (V-05)

---

## V-01

**Axis:** Inertia framing
**Hypothesis:** Front-loading inertia as a *named competitor to beat* — rather than a passive default — causes the model to produce proposals that explicitly answer "why does this beat NO CHANGE?" as first-class structure, improving C-01 and C-06 pass rates.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

## THE INERTIA COMPETITOR

Before this skill does anything else, register this constraint:

  NO CHANGE is the primary competitor. It is not a fallback or a default.
  It is an active, named option that wins unless a proposal can beat it.

  "Beating NO CHANGE" means:
    (a) A NEW signal artifact exists (date > strategy.md write date), AND
    (b) That artifact reveals something strategy.md did not account for, AND
    (c) The consequence of not acting is named and specific.

  A run that produces zero proposals has beaten NO CHANGE zero times.
  That is a complete, correct, valid execution of this skill.
  Do not treat zero proposals as failure.

This competitor position governs every step below. Every proposal
row answers: "Why does this beat NO CHANGE?" If it cannot answer
that question with a named artifact, it is not a proposal -- it is
a preference. Preferences are not written to strategy.md.

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md`. Locate the strategy file path for the
named topic. Read strategy.md. Record the STRATEGY DATE (last-modified
date or date field in frontmatter).

Extract every planned signal dimension: coverage scope, sequencing,
completion criteria, success thresholds.

Build the assumption table. For each assumption, test: is this stated
explicitly, or is it implicit? Apply the column independence test --
can you populate the "Implicit evidence" cell without re-reading the
source? If not, the cell is invalid.

| Assumption | Implicit evidence | Signal adjudication | Delta-candidate |

Null declaration (required if empty):
"ASSUMPTIONS: none -- all strategy dimensions are explicitly stated."

---

## Step 2 -- Pre-read Defense Register

Before reading a single signal artifact, write the defense register.
This is the NO CHANGE competitor's strongest current position.

For each strategic decision in strategy.md, state:
- What is the strongest argument for keeping it exactly as written?
- What signal evidence would force a revision?

| Defense ID | Strategic decision | NO CHANGE argument | Would be overridden by |

This register is your baseline. Every proposal in Step 4 must name
a Defense ID it is overriding, or explain why no Defense ID applies.

---

## Step 3 -- Signal inventory

Glob `simulations/` for all artifacts matching the topic slug.
Classify each artifact:
- NEW: artifact date > STRATEGY DATE
- PRIOR: artifact date <= STRATEGY DATE

All 9 namespaces must be assessed: scout / draft / review / flow /
trace / prove / listen / program / topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: After writing this table, signal files may not
be re-read. All subsequent analysis uses only what is recorded here.

Null declaration (required if no artifacts found):
"SIGNAL INVENTORY: null -- no artifacts found for topic [name].
Cannot run /topic:plan without signal artifacts."

---

## Step 3b -- Delta findings

For each NEW artifact, classify its contribution. Use only what you
can derive from the filename, date, and namespace -- no re-reading.
If the signal content is not reconstructable from the inventory, mark
the finding as "Pending -- content not carried into inventory."

Write exactly four sub-sections. Do not merge them.

### 3b-1 -- CONFIRMED
NEW artifacts that validate what strategy.md already assumed.
| Finding ID | Strategy assumption confirmed | Source artifact | Understanding changed |

Null: "CONFIRMED: none -- no NEW artifacts confirm existing assumptions."

### 3b-2 -- EXPANDED
NEW artifacts that expand a known assumption to a broader scope.
| Finding ID | Existing assumption | Expanded to | Source artifact | Understanding changed |

Null: "EXPANDED: none -- no NEW artifacts expand existing assumptions."

### 3b-3 -- UNEXPECTED
NEW artifacts that surface dimensions strategy.md did not cover.
| Finding ID | Gap in strategy | What signal reveals | Source artifact | Understanding changed |

Null: "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."

### 3b-4 -- CHALLENGED
NEW artifacts that contradict or weaken a strategy assumption.
| Finding ID | Strategy assumed | Signal challenges | Source artifact | Understanding changed |

Null: "CHALLENGED: none -- no NEW artifacts challenge existing strategy."

---

## Step 4 -- Proposals (beat the competitor)

For each Delta-candidate finding, write a proposal row only if the
finding can beat NO CHANGE on all three tests:
  (a) Named NEW artifact exists
  (b) Artifact reveals something not in strategy.md
  (c) Consequence of not acting is specific and named

If a finding fails any test, it does not produce a proposal.
Record the failed test in the "NO CHANGE won because" column.

### 4a -- Additions

| # | Dimension | Delta finding | Evidence | Before | After | Confidence |
  If unchanged | Reversibility | NO CHANGE won because / Beaten by |

Null: "ADDITIONS: none -- NO CHANGE wins all addition candidates."

### 4b -- Removals and Reprioritizations

| # | Action | Dimension | Delta finding | Evidence | Before | After |
  Confidence | If unchanged | Reversibility | NO CHANGE won because / Beaten by |

Null declarations (separate, labeled):
"REMOVALS: none -- NO CHANGE wins all removal candidates."
"REPRIORITIZATIONS: none -- NO CHANGE wins all reprioritization candidates."

### 4c -- Challenger Table

For each proposal that beat NO CHANGE, construct the strongest
possible argument for reverting it. This is the NO CHANGE
competitor filing a protest.

| Defense ID | Proposal # | Decision defended | Counter-argument | Strength |

Calibration check: examine the Strength column distribution.
- All Weak: "Calibration: rubber-stamp risk."
- All Strong: "Calibration: over-zealous risk."
- Mixed: "Calibration: balanced."

---

## Step 5 -- Conflict audit

Identify any two NEW artifacts that contradict each other on the
same strategy dimension. A conflict means proposals built on
conflicting signals are unreliable.

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none -- no contradictions between NEW artifacts
on the same dimension."

---

## Step 6 -- Before/after diff

Show the net effect on strategy.md if all non-withdrawn proposals
are applied. Include evidence in After cells.

| Dimension | Before | After [evidence] | Proposal ref |

---

## Step 7 -- Confirmation gate

Display Steps 3b, 4a, 4b, 4c, 5, and 6 for review.

Individual proposals may be withdrawn before confirmation.
Reply YES applies only to non-withdrawn proposals.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table to apply custom version | WITHDRAW [#] to remove specific proposals
---

Stop here. Write nothing further until the user replies.

---

## Step 8 -- Apply (after YES or REVISED only)

Write exactly the confirmed (non-withdrawn) changes to strategy.md.
Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."

If the user replied NO: "strategy.md unchanged. NO CHANGE wins."
```

---

## V-02

**Axis:** Output format (proposal cards instead of wide tables)
**Hypothesis:** Wide multi-column proposal tables cause column-skipping failures (model fills some columns, leaves others blank). Replacing them with numbered per-proposal *cards* — each with a fixed set of labeled sub-fields — forces the model to populate each field inline, improving C-03 and C-06 pass rates.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

## INERTIA PRIOR

This skill executes under an inertia prior. strategy.md unchanged is
the default outcome. Proposals require evidence from NEW signal
artifacts. Volume of signals alone does not trigger change. A run
that produces zero proposals is a valid, complete execution.

---

## Step 1 -- Read and inventory

Read `simulations/TOPICS.md` to locate the strategy file.
Read strategy.md. Record STRATEGY DATE.

**Assumption inventory** (table format):
| Assumption | Implicit evidence | Delta-candidate |

Null: "ASSUMPTIONS: none -- all strategy dimensions explicitly stated."

Then glob `simulations/` for all topic artifacts. Classify each:

**Signal inventory** (table format):
| Artifact | Date | NEW / PRIOR | Namespace |

Coverage check: note which of the 9 namespaces (scout / draft / review /
flow / trace / prove / listen / program / topic) have zero artifacts.

Null: "SIGNAL INVENTORY: null -- no artifacts found. Cannot proceed."

SIGNAL READ-LOCK: after writing the signal inventory, signal files
may not be re-read. All analysis uses only what is in this table.

---

## Step 2 -- Delta analysis

For each NEW artifact, classify its finding into one of four categories.
Write each finding as a prose bullet. Do not merge categories.

**CONFIRMED** -- NEW artifact validates an existing assumption:
- [Finding ID] [Source artifact]: Prior understanding: [X]. Now confirmed by: [Y].
- (or) CONFIRMED: none.

**EXPANDED** -- NEW artifact extends an assumption to broader scope:
- [Finding ID] [Source artifact]: Prior understanding: [X]. Expanded to: [Y].
- (or) EXPANDED: none.

**UNEXPECTED** -- NEW artifact reveals a gap not in strategy.md:
- [Finding ID] [Source artifact]: Strategy did not cover: [X]. Signal reveals: [Y].
- (or) UNEXPECTED: none.

**CHALLENGED** -- NEW artifact contradicts an existing assumption:
- [Finding ID] [Source artifact]: Strategy assumed: [X]. Signal challenges: [Y].
- (or) CHALLENGED: none.

Each finding marked with Delta-candidate: YES / NO / Pending.

---

GATE CHECK: All four delta categories above are complete before
any proposal card is written. If any category is absent, stop and
complete it. Do not write Step 3 until this gate is passed.

---

## Step 3 -- Proposal cards

For each Delta-candidate: YES finding, write one proposal card.
If no findings have Delta-candidate: YES, write the null block and skip to Step 4.

Null block: "ADDITIONS: none -- inertia holds."
             "REMOVALS: none -- inertia holds."
             "REPRIORITIZATIONS: none -- inertia holds."
Write each absent change type as its own labeled null.

For each proposal, use this exact card format:

---
PROPOSAL [number] -- [ADD / REMOVE / REPRIORITIZE]
Dimension:        [which strategy dimension this targets]
Delta finding:    Strategy assumed [X] / Signal revealed [Y]
Evidence:         [artifact filename that drives this proposal]
Before:           [current state in strategy.md]
After:            [proposed new state]
Confidence:       [High / Medium / Low]
If unchanged:     [specific consequence of deferring this change]
Reversibility:    [Reversible at same cost / Gets harder / Becomes impossible]
Inertia beaten:   [one sentence naming the specific evidence that defeats keep-unchanged]
---

A card that does not answer "Inertia beaten" with a named artifact
is incomplete and may not proceed to confirmation.

---

## Step 4 -- Challenger review

For each proposal card, write a challenger response:

---
CHALLENGE [number] -- responds to PROPOSAL [number]
Defends:          [strategic decision being challenged]
Counter-argument: [strongest reason NOT to make this change]
Strength:         [Strong / Moderate / Weak]
---

After all challenges: "Calibration: [rubber-stamp risk / balanced / over-zealous risk]."

---

## Step 5 -- Conflict check

If two NEW artifacts contradict each other on the same dimension,
surface the conflict before confirming any proposal that references either.

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none."

---

## Step 6 -- Diff summary

For each proposal card that has not been withdrawn, show:

| Dimension | Before | After [evidence] | Proposal # |

---

## Step 7 -- Confirmation gate

Present all proposal cards, all challenge cards, the conflict check,
and the diff summary. Do not touch strategy.md.

Individual proposals may be withdrawn: "WITHDRAW [number]."

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
cards to apply custom version | WITHDRAW [#] to remove specific proposals
---

Stop here. Write nothing until the user replies.

---

## Step 8 -- Apply

Triggered only after YES or REVISED.

Apply exactly the confirmed (non-withdrawn) cards to strategy.md.
Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."

If NO: "strategy.md unchanged."
```

---

## V-03

**Axis:** Lifecycle emphasis (compressed 4-phase structure)
**Hypothesis:** A 4-phase (Read / Analyze / Propose / Confirm+Apply) structure with minimal ceremony reduces cognitive overhead. The model can pass C-01 through C-05 more reliably when the structure is simple and each phase has a single clear exit condition, even if C-09 and C-10 depth is reduced.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

INERTIA PRIOR: strategy.md unchanged is the default. Zero proposals
is a valid, complete run. Change requires NEW artifacts with named
consequences of inaction.

---

## Phase 1 -- READ

Read `simulations/TOPICS.md`. Find and read strategy.md. Record:
- STRATEGY DATE (last-modified or frontmatter date)
- All planned coverage dimensions

Glob `simulations/` for topic artifacts. For each:
- Classify NEW (date > STRATEGY DATE) or PRIOR
- Record namespace (scout / draft / review / flow / trace /
  prove / listen / program / topic)

| Artifact | Date | NEW / PRIOR | Namespace |

If no NEW artifacts exist: output "No NEW artifacts -- inertia holds.
strategy.md unchanged." Stop here.

PHASE 1 COMPLETE. Do not enter Phase 2 until this table is written.

---

## Phase 2 -- ANALYZE

For each NEW artifact, classify its contribution to strategy revision.
Each finding needs: source artifact + what changed in your understanding.

CONFIRMED -- validates existing strategy:
[list or "CONFIRMED: none"]

EXPANDED -- extends an existing assumption to broader scope:
[list or "EXPANDED: none"]

UNEXPECTED -- surfaces a gap strategy.md did not cover:
[list or "UNEXPECTED: none"]

CHALLENGED -- contradicts an existing strategy assumption:
[list or "CHALLENGED: none"]

Each finding: mark Delta-candidate YES / NO / Pending.
A finding is a Delta-candidate YES only if it can name: (a) a NEW
artifact, (b) what the artifact revealed, (c) the consequence of
not updating strategy.md.

PHASE 2 COMPLETE. Do not enter Phase 3 until all four categories
are written and Delta-candidate fields are populated.

---

## Phase 3 -- PROPOSE

For each Delta-candidate YES finding, propose a change.

Action types: ADD / REMOVE / REPRIORITIZE (choose one per row).

Required columns per proposal:
| # | Action | Dimension | Delta finding (Strategy assumed X / Signal revealed Y) |
  Evidence | Before | After | Confidence | If unchanged | Inertia beaten |

"Inertia beaten": one sentence naming the specific artifact that
defeats keep-unchanged. Generic statements ("strong evidence exists")
are not valid -- name the file.

Null declarations (per change type, individually labeled):
"ADDITIONS: none -- inertia holds."
"REMOVALS: none -- inertia holds."
"REPRIORITIZATIONS: none -- inertia holds."

Challenger check: for each proposal, write one line of counter-argument
and rate its strength (Strong / Moderate / Weak). After all proposals:
state calibration (balanced / rubber-stamp risk / over-zealous risk).

Diff table: | Dimension | Before | After [evidence] | Proposal # |

PHASE 3 COMPLETE. Do not enter Phase 4 until proposals and diff are written.

---

## Phase 4 -- CONFIRM AND APPLY

Present Phase 2 (delta), Phase 3 (proposals + diff).

strategy.md is NOT modified until the user replies.

Proposals may be individually withdrawn: WITHDRAW [#].

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table | WITHDRAW [#] to remove specific proposals before confirming
---

STOP. Write nothing further until the user replies.

After YES or REVISED: apply exactly the confirmed (non-withdrawn) changes.
Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."

After NO: "strategy.md unchanged."
```

---

## V-04

**Axis:** Phrasing register (conversational) + Role sequence (Analyst → Advocate → Skeptic)
**Hypothesis:** Assigning three named roles in explicit sequence — Analyst (reads signals without bias), Advocate (builds the case for change), Skeptic (challenges each proposal) — will produce more calibrated Defender Challenge Tables (C-09) because the Skeptic role has a mandate to push back, not rubber-stamp. Conversational register reduces formula-following failure.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

You'll work through this in three roles, in order. Don't skip ahead.
The roles are sequential: Analyst finishes before Advocate starts.
Advocate finishes before Skeptic starts.

Before any role runs, state this once:

  Default outcome: strategy.md is unchanged.
  Change requires evidence. A run with zero proposals is fine.

---

## Role 1 -- Analyst

Your job: read what exists without forming any opinion about what
should change. Just inventory the facts.

First, read `simulations/TOPICS.md` to find the strategy file path.
Read strategy.md. Note the date it was written (STRATEGY DATE).
List every coverage dimension it plans.

Then, glob `simulations/` for all artifacts matching this topic.
For each artifact, note: filename, date, whether it's newer than
STRATEGY DATE (NEW) or not (PRIOR), and which namespace it's from.

Write the signal table:
| Artifact | Date | NEW / PRIOR | Namespace |

Check all 9 namespaces: scout / draft / review / flow / trace / prove
/ listen / program / topic. Note which have no coverage at all.

If there are no NEW artifacts: write "No NEW artifacts -- Analyst
finds nothing to review. Default outcome: strategy.md unchanged."
Stop here.

Now, for each NEW artifact, write what it says about the existing
strategy -- without advocating for any change yet. Use four buckets:

**Confirmed**: this NEW artifact agrees with what strategy.md assumed.
Format each entry: [artifact] confirms that [strategy assumption].

**Expanded**: this NEW artifact suggests an assumption covers more
ground than strategy.md stated.
Format: [artifact] expands [assumption] to include [broader scope].

**Unexpected**: this NEW artifact reveals something strategy.md
didn't plan for at all.
Format: [artifact] reveals [gap] that strategy.md doesn't address.

**Challenged**: this NEW artifact contradicts something strategy.md
assumed.
Format: [artifact] contradicts [assumption] by showing [finding].

For buckets with no entries, write: "[Bucket name]: none found."

Write these findings out now. Analyst's job is done when all four
buckets are written. Hand off to Advocate.

---

## Role 2 -- Advocate

Your job: look at the Analyst's findings and build the case for any
changes that are genuinely warranted. You're making proposals, not
just listing options. Each proposal needs to answer: "Why does this
beat doing nothing?"

For each finding the Analyst marked (or you assess as significant),
decide: does it warrant an addition, a removal, or a reprioritization?
If it doesn't warrant any change, say so and move on.

For each proposal, write:

**PROPOSAL [#] -- [ADD / REMOVE / REPRIORITIZE]**
- What dimension this touches: [dimension name from strategy.md]
- What the Analyst found: Strategy assumed [X] / Signal revealed [Y]
- The specific artifact driving this: [filename]
- Current state in strategy.md: [before]
- Proposed new state: [after]
- How confident you are: [High / Medium / Low]
- What happens if we don't do this: [specific consequence, not generic]
- Why this beats doing nothing: [one sentence naming the artifact evidence]

For change types with no proposals, write:
"ADDITIONS: none -- nothing in the Analyst's findings warrants adding coverage."
"REMOVALS: none -- nothing warrants removing coverage."
"REPRIORITIZATIONS: none -- nothing warrants changing priority."

Write each absent type as its own sentence. Don't combine them.

Finally, write a diff table showing what strategy.md would look
like after all your proposals:
| Dimension | Before | After [source] | Proposal # |

Advocate's job is done. Hand off to Skeptic.

---

## Role 3 -- Skeptic

Your job: challenge every proposal the Advocate made. You are not
trying to be destructive -- you're trying to make sure the
Advocate's case is actually strong enough to beat doing nothing.

For each Advocate proposal, write:

**CHALLENGE [#] -- responds to PROPOSAL [#]**
- What you're defending: [the decision to keep strategy.md as-is]
- Strongest counter-argument: [why this proposal might be premature or wrong]
- How strong this challenge is: [Strong / Moderate / Weak]

After all challenges, assess the distribution:
- If all Weak: "Calibration: rubber-stamp -- the Advocate's case was unchallenged."
- If all Strong: "Calibration: over-zealous -- the Skeptic may be blocking sound proposals."
- Otherwise: "Calibration: balanced -- challenge strength varied appropriately."

Also check: do any two NEW artifacts say contradictory things about
the same dimension? If yes, write a conflict note before confirming
any proposal that references either artifact.
| Conflict | Artifact A | Artifact B | Nature | How to resolve |
If none: "No conflicts detected between NEW artifacts."

Skeptic's job is done.

---

## Confirmation gate

You've heard from all three roles. Now present the Advocate's
proposals and the Skeptic's challenges to the user.

strategy.md has NOT been touched yet, and won't be until the
user explicitly says YES.

The user can:
- Reply YES to apply all non-withdrawn proposals
- Reply NO to leave strategy.md unchanged
- Reply REVISED + edited proposals to apply a modified version
- Reply WITHDRAW [#] to remove specific proposals before confirming

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
proposals | WITHDRAW [#] to drop specific proposals before confirming
---

Stop here. Do not write anything else until the user replies.

---

## Apply

Only runs after YES or REVISED from the user.

Write the confirmed changes to strategy.md. Don't reformat
sections that weren't changed.

Tell the user: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."

If the user said NO: "strategy.md unchanged."
```

---

## V-05

**Axis:** Simplified gates + Embedded inertia per step
**Hypothesis:** Replacing the 3-gate token machinery (GC-1/GC-2/GC-3, manifest, cross-source consistency) with simple inline STOP blocks, and embedding an explicit inertia checkpoint as the *first line* of each proposal step, will improve C-04 reliability (the confirmation gate can't be accidentally skipped when it's a visually distinct STOP block) and C-01 reliability (inertia is checked at the point of action, not just as a preamble). Reduces ceremony without losing the essential behavioral guarantees.

```markdown
---
name: topic-plan
description: Signal strategy revision as new information arrives with user confirmation.
allowed-tools: [Read, Write, Glob]
---

You are running /topic:plan for the topic named in the user's message.

---

## INERTIA PRIOR

strategy.md unchanged is the default outcome. The burden of proof
rests on change, not on keeping the strategy intact.

A proposal is only valid if it names:
  1. A NEW signal artifact (date > STRATEGY DATE)
  2. What that artifact revealed that strategy.md did not account for
  3. The specific consequence of not updating strategy.md

A run that produces zero proposals has correctly found that inertia
wins. That is not failure. That is the correct result when the
evidence does not justify change.

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md`. Find the strategy file for the named topic.
Read strategy.md. Record STRATEGY DATE.

List every planned signal dimension. For each, extract whether the
assumption is explicit or implicit.

| Assumption | Explicit or implicit | Delta-candidate |

Null: "ASSUMPTIONS: none -- all dimensions explicitly stated."

---

## Step 2 -- Signal inventory

Glob `simulations/` for all artifacts matching the topic slug.

| Artifact filename | Date | NEW / PRIOR | Namespace |

NEW = date > STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

Check all 9 namespaces: scout / draft / review / flow / trace /
prove / listen / program / topic.

SIGNAL READ-LOCK: after writing this table, signal files
are closed. All subsequent steps use only the written inventory.

Null: "SIGNAL INVENTORY: null -- no artifacts found for topic [name].
Cannot run /topic:plan."

[INERTIA CHECK] If no NEW artifacts exist: inertia holds by default.
Output "No NEW artifacts -- strategy.md unchanged." Stop here.

---

## Step 3 -- Delta analysis

For each NEW artifact, classify its finding. Write all four
categories. Each entry: source filename + what understanding changed.

### CONFIRMED
NEW artifact validates an existing assumption.
Format: "[source] confirms [assumption]. Understanding: [prior] -> [now]."
Null: "CONFIRMED: none."

### EXPANDED
NEW artifact extends an assumption to broader scope.
Format: "[source] expands [assumption] to [scope]. Understanding: [prior] -> [now]."
Null: "EXPANDED: none."

### UNEXPECTED
NEW artifact reveals a gap strategy.md did not cover.
Format: "[source] reveals [gap]. Understanding: [prior] -> [now]."
Null: "UNEXPECTED: none."

### CHALLENGED
NEW artifact contradicts an existing assumption.
Format: "[source] challenges [assumption]. Understanding: [prior] -> [now]."
Null: "CHALLENGED: none."

Mark each finding: Delta-candidate YES / NO / Pending.

--- STEP 3 COMPLETE ---
Do not write Step 4 until all four categories are written above.

---

## Step 4a -- Additions

[INERTIA CHECK] Before writing any row, confirm: does this finding
name a NEW artifact + reveal a gap + name a consequence of inaction?
If not, it is not a valid addition. Do not write the row.

| # | Dimension | Strategy assumed / Signal revealed | Evidence |
  Before | After | Confidence | If unchanged | Reversibility |
  Why this beats NO CHANGE |

"Why this beats NO CHANGE": one sentence naming the specific
artifact and what would be missed without this addition.
Generic statements ("strong evidence") do not satisfy this column.

Null: "ADDITIONS: none -- inertia holds for all candidate additions."

---

## Step 4b -- Removals and Reprioritizations

[INERTIA CHECK] Same check as Step 4a applies to every row here.

| # | Action | Dimension | Strategy assumed / Signal revealed | Evidence |
  Before | After | Confidence | If unchanged | Reversibility |
  Why this beats NO CHANGE |

Null declarations (separate, labeled):
"REMOVALS: none -- inertia holds."
"REPRIORITIZATIONS: none -- inertia holds."

---

## Step 4c -- Challenger table

For each proposal, write the strongest argument against making the
change. Rate challenge strength: Strong / Moderate / Weak.

| Proposal # | Decision defended | Counter-argument | Strength |

Calibration: after the table, write one line:
"Calibration: [balanced / rubber-stamp risk / over-zealous risk]."

---

## Step 5 -- Conflict check

Do any two NEW artifacts contradict each other on the same dimension?
If so, surface the conflict before any proposal referencing either
artifact proceeds to confirmation.

| Conflict ID | Signal A | Signal B | Nature | Resolution |

Null: "CONFLICT AUDIT: none -- no NEW artifact contradictions detected."

---

## Step 6 -- Diff table

Show the net change to strategy.md if all non-withdrawn proposals apply.

| Dimension | Before | After [evidence] | Proposal # |

---

## *** STOP -- CONFIRMATION REQUIRED ***

strategy.md has NOT been modified. It will not be modified until
you reply.

Present Steps 3, 4a, 4b, 4c, 5, and 6 above.

Proposals may be individually withdrawn: WITHDRAW [#].

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited
table to apply custom version | WITHDRAW [#] to remove specific proposals
---

Do not write anything further until the user replies.

## *** END STOP ***

---

## Step 7 -- Apply (after YES or REVISED only)

[INERTIA CHECK] Applying only confirmed (non-withdrawn) proposals.
Proposals the user did not confirm are not written to strategy.md.

Write the confirmed changes. Do not reformat unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."

If NO: "strategy.md unchanged -- inertia holds."
```

---

## Variation Summary

| ID | Axis | Hypothesis | Key distinguishing mechanism |
|----|------|-----------|------------------------------|
| V-01 | Inertia framing | "NO CHANGE competitor" framing improves C-01 and C-06 | `NO CHANGE won because / Beaten by` column; Defense Register as "competitor position" |
| V-02 | Output format | Per-proposal cards prevent column-skipping, improve C-03 and C-06 | Numbered cards with labeled sub-fields replace wide proposal tables |
| V-03 | Lifecycle emphasis | 4-phase compression reduces ceremony, improves essential-criteria pass rate | Single-phase exit conditions, challenger check inlined into Phase 3 |
| V-04 | Phrasing register + Role sequence | Analyst→Advocate→Skeptic roles improve C-09 calibration; conversational reduces formula-following failure | Three named sequential roles with handed-off output |
| V-05 | Simplified gates + Embedded inertia | STOP blocks more reliable than token strings; per-step inertia check strengthens C-01 at the point of action | `[INERTIA CHECK]` at each proposal step; `*** STOP ***` block replaces GC-1/GC-2/GC-3 machinery |
