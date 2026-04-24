Here are the 5 complete variations.

---

## V-01 — Single Axis: Inertia Framing
**Hypothesis:** Making inertia the lead character (not a clause) causes the model to treat zero-change as the primary track and forces each proposal to explicitly defeat the null outcome before it can appear in the output.

---

```markdown
---
name: topic-plan
description: Signal strategy revision. Inertia is the primary outcome. Change requires evidence.
allowed-tools: [Read, Write, Glob]
---

## THE NULL PATH

You are running the null path. The null path ends with strategy.md unchanged.
That is not a fallback — it is the primary outcome of this skill. Every step
below is a test of whether any NEW signal artifact provides evidence strong
enough to defeat the null path for a specific strategy dimension.

The burden of proof rests entirely on change. A run that produces zero
proposals is a complete, successful execution.

You are running /topic:plan for the topic named in the user's message.

---

## INERTIA DEFENSE PROTOCOL

Before reading any artifact, register the inertia defense for each current
strategy dimension. These defenses represent what must be defeated by signal
evidence for any proposal to appear in the output.

| Defense ID | Strategy dimension | Best argument for keeping it | What would defeat this defense |
|------------|-------------------|------------------------------|-------------------------------|

---

## SIGNAL INVENTORY

Read `simulations/TOPICS.md` to locate strategy.md. Extract the STRATEGY DATE
(last-modified date). This is the cutoff for NEW vs PRIOR classification.

List every artifact in `simulations/` matching the topic slug.

| Artifact filename | Date | NEW / PRIOR | Namespace |

All 9 namespaces must be assessed explicitly:
scout / draft / review / flow / trace / prove / listen / program / topic.

Null: "SIGNAL INVENTORY: null -- no artifacts found for topic [name].
Null path complete. strategy.md unchanged."

**SIGNAL READ-LOCK**: After writing the table above, signal files may not
be re-read. All subsequent steps use this written inventory only.

---

## EVIDENCE AGAINST INERTIA

For each NEW artifact, state whether it provides evidence defeating any
inertia defense from the Defense Protocol above.

Classify each piece of evidence into one category:

**CONFIRMED** -- NEW artifact confirms a strategy assumption.
| Finding ID | Defense ID | Source artifact | What the signal confirms |

Null: "CONFIRMED: none"

**EXPANDED** -- NEW artifact reveals the dimension is larger than assumed.
| Finding ID | Defense ID | Source artifact | Prior understanding | Expanded understanding |

Null: "EXPANDED: none"

**UNEXPECTED** -- NEW artifact reveals a dimension the strategy did not cover.
| Finding ID | Strategy gap | Source artifact | What was revealed |

Null: "UNEXPECTED: none"

**CHALLENGED** -- NEW artifact directly contests a current strategy element.
| Finding ID | Defense ID | Source artifact | What is challenged | Challenge strength: Strong / Moderate / Weak |

Null: "CHALLENGED: none"

---

## DEFEAT ASSESSMENT

For each entry in CHALLENGED or UNEXPECTED above, assess whether the evidence
is strong enough to defeat the inertia defense for that dimension.

Defeat requires: a named NEW artifact + a stated consequence of NOT changing.

| # | Dimension | Defeats defense? | Evidence | Consequence of no change |
|---|-----------|-----------------|----------|--------------------------|

Entries that do not defeat their inertia defense do not become proposals.
They are listed here as "INERTIA HOLDS" and drop from the proposal table.

---

## PROPOSAL TABLE

Only dimensions where inertia was defeated appear in this table.
Action must be one of: ADD / REMOVE / REPRIORITIZE.

If no inertia defenses were defeated:
"PROPOSALS: null -- no NEW artifacts defeated inertia for any strategy dimension.
Null path complete."

| # | Action | Dimension | Before | After | Evidence artifact | Consequence of no change |
|---|--------|-----------|--------|-------|-------------------|--------------------------|

---

## CONFIRMATION GATE

Display the Defeat Assessment table and the Proposal Table above.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Null path is active unless you confirm changes below.

Proposed changes: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply all | NO to keep null path complete | REVISED + edited
table to apply a subset | WITHDRAW [#] to remove a proposal first
---

Stop here. Do not write anything further until the user replies.

---

## APPLY

Triggered only by YES or REVISED.

Write exactly the confirmed changes to strategy.md. No changes to
dimensions not listed in confirmed proposals.

Confirm: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations. Null path did not complete."
```

---

## V-02 — Single Axis: Compact Output Format
**Hypothesis:** Reducing column counts in proposal tables (from 10 to 5-6) while preserving all essential criteria reduces parsing overhead and makes the inertia-rejection signal more visible, not less.

---

```markdown
---
name: topic-plan
description: Signal strategy revision with compact table format.
allowed-tools: [Read, Write, Glob]
---

## INERTIA PRIOR

strategy.md unchanged is the default outcome. Change requires specific evidence
from NEW artifacts (date > strategy date). Volume of signals does not trigger
change. A run with zero proposals is complete and valid.

You are running /topic:plan for the topic named in the user's message.

---

## STEP 1 -- READ

Read `simulations/TOPICS.md`. Locate strategy.md. Record STRATEGY DATE.
Read strategy.md. List the active strategy dimensions.

| Dimension | What the strategy assumes |
|-----------|--------------------------|

---

## STEP 2 -- PRE-SIGNAL DEFENSE

Before reading any signal artifact, record the defense for each dimension.

| Dimension | Best reason to keep it unchanged | What would defeat this |
|-----------|----------------------------------|------------------------|

---

## STEP 3 -- SIGNAL INVENTORY

Glob `simulations/` for artifacts matching the topic slug. Classify each as
NEW (date > STRATEGY DATE) or PRIOR. Assess all 9 namespaces.

| Filename | Date | NEW/PRIOR | Namespace |
|----------|------|-----------|-----------|

Null: "SIGNAL INVENTORY: null -- no artifacts found for topic [name]."

**READ-LOCK**: Signal files may not be re-read after this step.

---

## STEP 4 -- DELTA ANALYSIS

For each NEW artifact, classify the finding. Four categories. Do not merge.

**CONFIRMED** (signal validates existing assumption)
| Source | What it confirms |

**EXPANDED** (signal shows dimension is larger)
| Source | Prior scope | Expanded scope |

**UNEXPECTED** (signal reveals uncovered dimension)
| Source | What was missing | What it revealed |

**CHALLENGED** (signal contests existing strategy element)
| Source | What is challenged | Challenge strength: Strong / Moderate / Weak |

Use verbatim null declarations for empty categories:
- "CONFIRMED: none -- inertia holds."
- "EXPANDED: none -- inertia holds."
- "UNEXPECTED: none -- inertia holds."
- "CHALLENGED: none -- inertia holds."

---

## STEP 5 -- PROPOSALS

Each proposal requires: action type (ADD / REMOVE / REPRIORITIZE) + a named
NEW artifact as evidence + why keeping it unchanged has a concrete consequence.
Proposals without all three are structurally invalid.

**ADDITIONS**
| # | What to add | Evidence artifact | If not added |
|---|------------|-------------------|--------------|
Null: "ADDITIONS: none -- inertia holds."

**REMOVALS / REPRIORITIZATIONS**
| # | Action | What to change | Evidence artifact | If not changed |
|---|--------|----------------|-------------------|----------------|
Null: "REMOVALS: none -- inertia holds."
     "REPRIORITIZATIONS: none -- inertia holds."

**DEFENDER CHALLENGES**
For each proposal, record the strongest defense of the current position.
| Proposal # | Defense argument | Challenge strength: Strong / Moderate / Weak |
After completing: note if all challenges are Weak (rubber-stamp risk) or all
Strong (over-rejection risk).

---

## STEP 6 -- BEFORE/AFTER DIFF

Show only dimensions that have proposals.

| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|

---

## STEP 7 -- CONFIRMATION GATE

Show Steps 4, 5, 6. Then write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep unchanged | REVISED + edited table |
WITHDRAW [#] to remove a proposal before confirming
---

Stop here. Write nothing further until the user replies.

---

## STEP 8 -- APPLY (triggered by YES or REVISED only)

Apply confirmed proposals. Write:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03 — Single Axis: Conversational Register
**Hypothesis:** Shifting from imperative "you will" declarations to descriptive "here's what you're doing and why" framing makes the inertia prior more intuitive and reduces mechanical compliance in favor of genuine application.

---

```markdown
---
name: topic-plan
description: Signal strategy revision — conversational guide format.
allowed-tools: [Read, Write, Glob]
---

You're running `/topic:plan` for the topic the user named. Here's what this
skill does: it checks whether anything you've learned since the strategy was
written is strong enough to justify changing it. Most of the time, it won't
be — and that's fine. Leaving the strategy alone is a successful outcome.

Before getting into the steps, the most important thing to understand:

**The strategy is innocent until proven otherwise.**

Every step below is asking the question: "Does this signal give us a reason to
change the strategy?" If the answer is "not really" at every step, the skill
ends with strategy.md untouched. That's not a failed run — it's the expected
result most of the time.

---

### What you need from the files

Start by reading `simulations/TOPICS.md` to find where strategy.md lives.
Read strategy.md and note the date it was last modified — that's your cutoff
for deciding which signals are "new" (dated after that) versus "prior" (dated
before). Jot down what the strategy currently says it's trying to accomplish.

| Dimension | What the strategy currently assumes |
|-----------|-------------------------------------|

Next, take a moment — before you read any signal files — to think through
the best arguments for keeping the current strategy as-is. This is the
pre-signal defense register, and it matters: you want to know what "good"
looks like for the current strategy before you're influenced by what the
signals say.

| Dimension | Why the current approach is probably right | What kind of evidence could genuinely change this |
|-----------|-------------------------------------------|--------------------------------------------------|

---

### Building the signal inventory

Now look at what signals exist. Glob `simulations/` for files matching the
topic slug. For each file you find, note whether it's new (after the strategy
date) or prior (before it). Check all nine namespaces explicitly:
scout / draft / review / flow / trace / prove / listen / program / topic.

| Filename | Date | New or Prior? | Namespace |
|----------|------|--------------|-----------|

Once you've written this table, stop reading signal files. Everything from
here uses this written inventory — you're not going back to the files.

If there are no artifacts at all: "No signals found for this topic. The
strategy can't be evaluated yet — nothing to compare against."

---

### What did the new signals actually reveal?

For each signal dated after the strategy, think about what it told you and
whether that's surprising given what the strategy assumed. Sort your findings
into four buckets (it's fine if some buckets are empty — just say so):

**Things the signal confirmed** — the strategy assumed X, and the signal backs that up.
| Source file | What got confirmed |

Empty: "Nothing new confirmed existing assumptions."

**Things that turned out to be bigger than expected** — the strategy had the
right idea but the signal shows it's larger or more complex than assumed.
| Source file | What was assumed | What the signal shows instead |

Empty: "Nothing expanded beyond what the strategy assumed."

**Things the strategy didn't cover at all** — the signal surfaced a dimension
that wasn't in the strategy.
| Source file | What was missing | What was revealed |

Empty: "No unexpected dimensions surfaced."

**Things the signal pushed back on** — the signal gives a reason to doubt
something the strategy assumed.
| Source file | What's being questioned | How strong is the pushback: Strong / Moderate / Weak |

Empty: "No existing assumptions were challenged."

---

### Should anything change?

Now, given everything above, are there changes worth proposing? Remember: each
proposal needs three things to be valid: (a) a specific action (adding
something, removing something, or changing the priority of something), (b) a
specific new signal file as evidence, and (c) a concrete answer to "what
happens if we don't make this change?"

If something doesn't meet all three criteria, leave it out. It's a preference,
not a proposal.

**Things to add to the strategy:**
| # | What to add | Signal evidence | What we'd miss if we don't add it |
|---|------------|-----------------|-----------------------------------|

No additions? Write: "Nothing new enough to add. Strategy coverage holds."

**Things to remove or reprioritize:**
| # | What changes (remove or shift priority) | Signal evidence | What we'd miss if we don't change it |
|---|----------------------------------------|-----------------|--------------------------------------|

No changes? Write: "Nothing to remove or reprioritize. Strategy sequencing holds."

Before wrapping up proposals, go back to your pre-signal defenses and check:
did any proposal actually defeat a defense you registered? If a defense still
stands, the proposal probably shouldn't be there.

| Proposal # | Defense it needs to beat | Does it beat it? | Strength: Strong / Moderate / Weak |
|------------|--------------------------|-----------------|-------------------------------------|

Note if all challenges ended up Weak — that suggests the proposals might not
really be necessary.

---

### Show the diff

If there are any proposals, show what strategy.md would look like before and
after each one.

| Dimension | Current wording | Proposed wording | Which proposal |
|-----------|----------------|------------------|----------------|

---

### Ask before changing anything

Show everything above, then write exactly this:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Here's what's proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply all of them | NO to keep everything as-is | REVISED +
an edited table if you want a custom version | WITHDRAW [#] to pull a
specific proposal before confirming
---

Then stop. Don't write anything else until the user replies.

---

### Making the changes (only if confirmed)

If the user replies YES or REVISED, write the confirmed changes to
strategy.md. Don't touch dimensions that weren't in the confirmed proposals.

Finish with: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."
```

---

## V-04 — Combined: Phase-Boundary Emphasis + Defense-First Sequence
**Hypothesis:** Restructuring execution into explicit named phases (rather than numbered steps) and placing the pre-signal defense register before strategy.md is read forces the model to commit to inertia defenses before encountering confirming evidence — preventing post-hoc rationalization of inertia positions.

---

```markdown
---
name: topic-plan
description: Signal strategy revision. Four explicit phases. Defense registers before read.
allowed-tools: [Read, Write, Glob]
---

## INERTIA PRIOR

strategy.md unchanged is the default and co-equal outcome. Change requires
evidence. A run that produces zero proposals is complete. The burden of proof
rests on change.

You are running /topic:plan for the topic in the user's message.

---

## PHASE 0: ORIENTATION

Before reading any file, declare the topic slug and the expected strategy
file path based on `simulations/TOPICS.md`.

Then commit to this execution schema:
- Phase 1: Read strategy and inventory signals
- Phase 2: Analyze delta
- Phase 3: Propose changes (or declare inertia)
- Phase 4: Confirm and apply

You will not cross a phase boundary until the previous phase is complete
in the output. A phase boundary is marked by an explicit PHASE COMPLETE token.

---

## PHASE 1: READ

### 1a. Pre-Signal Defense Register

Output this table BEFORE reading strategy.md or any signal file.

List what you would predict the current strategy defends well, drawn only
from your prior knowledge of the topic (from the user's invocation context).

| Defense ID | Predicted dimension | Best keep-unchanged argument | What would defeat this defense |
|------------|---------------------|------------------------------|-------------------------------|

This register is sealed after this step. You may not add to it in Phase 2 or 3.

### 1b. Strategy Read

Read `simulations/TOPICS.md`. Locate strategy.md. Record STRATEGY DATE.

Read strategy.md. Extract:
- Active strategy dimensions
- Stated completion criteria
- Signal coverage plan

| Dimension | Strategy assumption | In pre-signal defense? Y/N |
|-----------|---------------------|---------------------------|

### 1c. Signal Inventory

Glob `simulations/` for artifacts matching the topic slug. Classify each:
NEW (date > STRATEGY DATE) or PRIOR. All 9 namespaces must be listed.

| Filename | Date | NEW/PRIOR | Namespace |

READ-LOCK: Signal files may not be re-read after Phase 1.

Null: "SIGNAL INVENTORY: null -- no artifacts found. Cannot run /topic:plan."

---

**PHASE 1 COMPLETE**

Conditions: strategy.md read, assumption table present, signal inventory
written, READ-LOCK in effect.

---

## PHASE 2: ANALYZE

For each NEW artifact, classify findings. Do not merge categories.
Required columns per entry: source artifact, what understanding changed.

Format: "[Source: {filename}] Prior understanding: {X} | Now: {Y}"

**CONFIRMED** -- NEW artifact validates existing strategy assumption
| Finding ID | Defense ID (if matched) | Citation |

Null: "CONFIRMED: none"

**EXPANDED** -- NEW artifact shows a dimension is larger than the strategy assumed
| Finding ID | Defense ID | Citation |

Null: "EXPANDED: none"

**UNEXPECTED** -- NEW artifact reveals a dimension absent from the strategy
| Finding ID | Strategy gap | Citation |

Null: "UNEXPECTED: none"

**CHALLENGED** -- NEW artifact contests a current strategy element
| Finding ID | Defense ID | Citation | Challenge strength: Strong / Moderate / Weak |

Null: "CHALLENGED: none"

---

**PHASE 2 COMPLETE**

Condition: all four delta categories present in output (null declarations
acceptable per category).

---

## PHASE 3: PROPOSE

INERTIA REMINDER: Proposals require evidence. Each proposal must name
(a) action type, (b) dimension, (c) NEW artifact, (d) consequence of no change.
Missing any element makes the proposal structurally invalid.

### 3a. Additions

| # | Dimension | Evidence artifact | Before | After | If unchanged | Why inertia fails here |
|---|-----------|------------------|--------|-------|--------------|----------------------|

Null: "ADDITIONS: none -- inertia holds."

### 3b. Removals and Reprioritizations

| # | Action | Dimension | Evidence artifact | Before | After | If unchanged | Why inertia fails here |
|---|--------|-----------|------------------|--------|-------|--------------|----------------------|

Null: "REMOVALS: none -- inertia holds."
     "REPRIORITIZATIONS: none -- inertia holds."

### 3c. Defense Audit

For each proposal, verify it defeats the corresponding pre-signal defense
registered in Phase 1. A proposal that does not defeat its registered defense
should be marked INERTIA HOLDS and removed from the proposal table.

| Proposal # | Defense ID | Defense argument | Defeated? Y/N | If N: mark INERTIA HOLDS |
|------------|------------|-----------------|--------------|--------------------------|

### 3d. Before/After Diff

Show only dimensions with surviving proposals.

| Dimension | Before | After | Proposal ref |

---

**PHASE 3 COMPLETE**

Condition: all three proposal tables present (null declarations acceptable),
defense audit complete, diff table present.

---

## PHASE 4: CONFIRM AND APPLY

Show Phase 2 delta findings and Phase 3 proposal tables.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep unchanged | REVISED + edited table |
WITHDRAW [#] to remove a proposal
---

Stop here. Write nothing further until the user replies.

---

**PHASE 4 GATE**: strategy.md is not modified without an explicit YES or
REVISED. Absence of a NO reply does not imply YES.

---

## APPLY (triggered by YES or REVISED)

Write confirmed changes to strategy.md.

PHASE 4 COMPLETE: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."
```

---

## V-05 — Combined: Formal/Technical Register + Compressed Steps + Explicit Null Track
**Hypothesis:** Providing a dedicated, labeled NULL TRACK template (as an alternative to the proposal track) makes it structurally easier to declare inertia than to propose changes — inverting the default cognitive path where producing output feels like progress.

---

```markdown
---
name: topic-plan
description: Signal strategy revision. Compressed steps. Explicit null track.
allowed-tools: [Read, Write, Glob]
---

## EXECUTION CONTRACT

This skill operates under an inertia prior. The null track (strategy.md
unchanged) and the proposal track (strategy.md modified) are co-equal
outcomes. The null track requires zero justification. The proposal track
requires artifact-backed evidence for every proposal row.

You are executing /topic:plan for the topic in the user's message.

---

## ENUMERATED CONSTRAINTS

These constraints apply to all tables and declarations in this execution:

**E-1. Action column**: ADD / REMOVE / REPRIORITIZE only. Prose invalid.
**E-2. Null declarations**: Each change type (additions, removals, reprioritizations)
      requires its own labeled null declaration. A single "no changes" covering
      multiple types violates E-2.
**E-3. Evidence citation format**: "[Source: {filename}] Changed: {prior} -> {now}"
      An entry lacking both parts is incomplete.
**E-4. Inertia rejection column**: Required in all proposal rows. One sentence naming
      the specific artifact evidence and stated consequence that defeats no-change.
      Generic ("compelling argument") is invalid.
**E-5. Gate compliance**: strategy.md is not modified before user confirmation.
      Absence of a NO reply does not constitute confirmation.

---

## STEP 1: READ AND INVENTORY

Read `simulations/TOPICS.md`. Locate strategy.md path. Record STRATEGY DATE.
Read strategy.md. Extract dimensions.

**Strategy assumption table:**
| Dimension | Stated assumption | Implicit assumption [requires independent evidence cell] |

**Signal inventory:**
Glob `simulations/` for topic slug artifacts. Classify NEW (> STRATEGY DATE)
or PRIOR. All nine namespaces must appear.

| Filename | Date | NEW/PRIOR | Namespace |

Null: "SIGNAL INVENTORY: null -- no artifacts found. Cannot proceed."

READ-LOCK: Signal files may not be re-read after Step 1.

---

## STEP 2: DELTA ANALYSIS

Classify all NEW artifacts into four categories. Each entry requires E-3
citation. Do not merge categories.

| Category | Finding ID | Source | Citation [E-3] | Proposal candidate: Yes / No / Pending |

Categories (labeled sections, not merged):
- CONFIRMED: strategy assumption validated by NEW artifact
- EXPANDED: strategy assumption shown to be narrower than reality
- UNEXPECTED: strategy gap revealed by NEW artifact
- CHALLENGED: strategy assumption contested by NEW artifact

Per-category null [E-2]:
- "CONFIRMED: none"
- "EXPANDED: none"
- "UNEXPECTED: none"
- "CHALLENGED: none"

---

## STEP 3: TRACK DETERMINATION

Based on Step 2, determine which track applies.

**NULL TRACK** -- select when no NEW artifacts produced UNEXPECTED or CHALLENGED
findings with proposal-candidate status "Yes".

```
NULL TRACK DECLARATION
======================
Topic: [topic name]
Strategy date: [date]
NEW artifacts reviewed: [N]
UNEXPECTED candidates: 0
CHALLENGED candidates: 0

Result: strategy.md unchanged. Inertia holds on all dimensions.
Execution complete.
```

If NULL TRACK applies: proceed to Step 5 (confirmation gate) with
"0 additions / 0 removals / 0 reprioritizations" as the proposal count.

**PROPOSAL TRACK** -- select when at least one finding carries
proposal-candidate status "Yes".

---

## STEP 4: PROPOSALS (Proposal Track only)

Pre-signal defense: For each proposal, state the strongest argument for
keeping the current strategy unchanged on that dimension, then state why
the evidence defeats it [E-4].

**Additions [E-1, E-4]:**
| # | Dimension | Evidence [E-3] | Before | After | If unchanged | Inertia rejected because [E-4] |

Null [E-2]: "ADDITIONS: none -- inertia holds."

**Removals and Reprioritizations [E-1, E-4]:**
| # | Action [E-1] | Dimension | Evidence [E-3] | Before | After | If unchanged | Inertia rejected because [E-4] |

Null [E-2, two declarations]:
"REMOVALS: none -- inertia holds."
"REPRIORITIZATIONS: none -- inertia holds."

**Defender challenge table:**
| Proposal # | Defense argument | Challenge strength: Strong / Moderate / Weak |
Calibration note: if all Weak, state "rubber-stamp risk"; if all Strong, state
"over-rejection risk"; otherwise "balanced".

**Conflict audit:**
Identify NEW artifacts contradicting each other on the same dimension.
| Conflict ID | Artifact A | Artifact B | Conflict | Resolution |
Null: "CONFLICT AUDIT: none"

**Before/after diff:**
| Dimension | Before | After [evidence] | Proposal ref |

---

## STEP 5: CONFIRMATION GATE [E-5]

Display Step 2 delta findings. Display Step 4 tables (or NULL TRACK
declaration if null track was selected).

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Track: [NULL / PROPOSAL]
Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep unchanged | REVISED + edited table |
WITHDRAW [#] to remove a specific proposal
---

Halt. Write nothing further until the user replies.

---

## STEP 6: APPLY (triggered by YES or REVISED only)

Write confirmed changes to strategy.md. Unchanged dimensions are not
reformatted.

Terminal declaration: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations. Track: [NULL completed / PROPOSAL applied]."
```

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|-----------|
| V-01 | Inertia framing | Inertia-as-lead-character forces explicit defeat before proposal can appear |
| V-02 | Output format (compact tables) | 5-6 column tables surface inertia-rejection signal more clearly than 10-column tables |
| V-03 | Phrasing register (conversational) | Descriptive "here's why" reduces mechanical compliance, improves genuine application |
| V-04 | Phase boundaries + defense-first sequence | Committing to defenses before reading prevents post-hoc rationalization of inertia positions |
| V-05 | Formal/compressed + explicit null track | A labeled NULL TRACK template makes declaring inertia structurally easier than proposing changes |
