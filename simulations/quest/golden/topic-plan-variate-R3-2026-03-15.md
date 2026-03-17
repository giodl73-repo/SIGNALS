# topic-plan Skill Variations — Round 3 (2026-03-15)

Rubric: v3 (C-14 Explicit placeholder tokens `??`; C-15 Counted-total delta summary
sentence with exact counts; C-16 Hedge-phrase disqualification — named and banned.)

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04, V-05).

---

## V-01: Output Format — Sentinel `??` Tokens Baked Into Pre-Committed Table Schemas

**Variation axis**: Output format — all table schemas are pre-committed with `??` as
the required placeholder for every unfilled cell; absent artifacts use `??` explicitly
rather than a blank cell. Single axis.

**Hypothesis**: C-14 requires that absent artifact filenames and dates carry a `??`
sentinel rather than a blank. Blanks look like empty cells; `??` is a machine-scannable
gap marker. Prior variations pre-committed table schemas but used blank cells as the
placeholder, which allowed a model to leave a gap indistinguishable from a deliberately
omitted row. Pre-printing `??` in every data cell of the schema — so the model must
replace `??` with a real value or leave the sentinel — makes gaps visible at parse time
without requiring a human to notice missing content. This also targets C-15: the delta
summary block includes a templated sentence with `??` slots for the exact counts, forcing
the model to fill in real integers rather than produce a vague "some artifacts are new"
statement.

```
You are running /topic:plan for the topic named in the user's message.

Commit to this output schema before reading any file. You will fill these tables
in order. Do not replace any table with prose. Do not merge tables.

Every unfilled cell in the schemas below contains `??`. You must replace each `??`
with a real value. A `??` that remains in the final output is a machine-detectable
gap. Do not leave `??` in any cell you could fill. If a value is genuinely absent
(e.g., no artifact exists for a namespace), write `--` (dash), not `??`. `??` means
"I have not yet filled this" and `--` means "nothing exists here."

---

## Pre-committed Output Schema

**Schema A -- Strategy anchor**
| Item | Value |
|------|-------|
| Strategy file path | ?? |
| STRATEGY DATE | ?? |
| Dimensions listed in strategy.md | ?? |

**Schema B -- Signal inventory**
(Add one row per artifact. If a column value cannot be determined, use `??`.)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| ?? | ?? | ?? | ?? |

**Schema C -- Namespace audit (all 9 rows required)**
| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | ?? | ?? | ?? |
| draft | ?? | ?? | ?? |
| review | ?? | ?? | ?? |
| flow | ?? | ?? | ?? |
| trace | ?? | ?? | ?? |
| prove | ?? | ?? | ?? |
| listen | ?? | ?? | ?? |
| program | ?? | ?? | ?? |
| topic | ?? | ?? | ?? |

**Schema D -- Delta partition**
| List | Artifacts |
|------|-----------|
| NEW (date > STRATEGY DATE) | ?? |
| PRIOR (date <= STRATEGY DATE) | ?? |

**Schema E -- Delta summary (mandatory templated sentence)**
  Strategy was written on ??. ?? artifacts are NEW. ?? are PRIOR.

**Schema F -- Change proposals**
| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| ?? | ?? | ?? | ?? | ?? | ?? | ?? |

**Schema G -- Before/after diff**
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| ?? | ?? | ?? | ?? |

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file path for this topic.
Read strategy.md. Fill Schema A. Quote at least one concrete sentence from
strategy.md to confirm you have read it.

---

## Step 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B. For each artifact: date from filename, NEW/PRIOR classification
(NEW = artifact date > STRATEGY DATE), namespace from filename prefix.

If an artifact's date cannot be determined from the filename, write `??` in the
Artifact date column -- do not omit the row.

Fill Schema C. Mark ABSENT namespaces with artifact count = 0 and NEW artifact
count = 0. Do not skip any of the 9 namespace rows.

---

## Step 3 -- Delta detection

Partition artifacts into Schema D (NEW list and PRIOR list).

Fill Schema E. Replace all `??` placeholders with exact counts:
  Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR.

[N] and [M] must be integers. Do not write "several", "a few", or any non-integer.

If no NEW artifacts exist:
  Write: "No new signals since STRATEGY DATE ([date]). Strategy is current."
  Stop. Do not proceed to Step 4.

---

## Step 4 -- Read NEW artifacts (only)

Read each NEW artifact. PRIOR artifacts are already incorporated in strategy.md --
re-citing them would re-litigate settled decisions.

Write a short freeform paragraph (no headings, no bullets) describing what the NEW
artifacts collectively reveal. Name at least two artifacts by filename.

---

## Step 5 -- Proposals

Only NEW artifacts (Schema D, NEW list) may drive proposals.

Fill Schema F. For every row:
- Action must be exactly ADD, REMOVE, or REPRIORITIZE
- Evidence artifact must be a filename from the NEW list in Schema D
- "vs. NO CHANGE" must state the specific consequence of NOT changing; a
  generic claim is not sufficient

Null declarations (required per change type, labeled separately):
- If no additions: "ADDITIONS: none -- [reason specific to this topic]"
- If no removals: "REMOVALS: none -- [reason specific to this topic]"
- If no reprioritizations: "REPRIORITIZATIONS: none -- [reason specific to this topic]"

If proposals exist, fill Schema G.

---

## Step 6 -- Confirmation gate

Display Schema B, Schema C, Schema D, Schema E, Schema F, and Schema G.

Scan the output for any remaining `??` tokens. If any `??` tokens remain in
Schemas A-G, resolve them before continuing.

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.

---

## Step 7 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Phrasing Register -- Conversational with Named Banned-Phrase Blacklist

**Variation axis**: Phrasing register -- conversational direct-address with an
explicit inline blacklist of hedge phrases prohibited in any justification column.
Single axis.

**Hypothesis**: C-16 requires that justification columns explicitly name and ban
hedge phrases. Prior variations stated that a "generic phrase" fails the requirement
but never enumerated the phrases. A model that doesn't know which phrases are banned
can satisfy the letter of C-16 by adding a single "no generic phrases" instruction
while still producing output containing those exact phrases. Naming the banned phrases
inline -- inside the proposal gate, not in a preamble clause -- closes this. A
conversational register makes the blacklist feel like a direct per-cell warning rather
than a policy note, which reduces the tendency to treat it as boilerplate. C-15 is
satisfied via a required templated sentence at the delta step.

```
You are running /topic:plan for the topic named in the user's message.

---

## Before you start

The goal here is not to find reasons to update strategy.md. The goal is to find
out whether new evidence is strong enough to justify changing a document that
represents prior considered decisions. Most of the time, the answer is no change.

---

## Step 1 -- Read strategy.md

Go to `simulations/TOPICS.md` and find the strategy file path for this topic.
Read strategy.md. Note the date it was last modified -- call it the STRATEGY DATE.

Write out:
- STRATEGY DATE: [YYYY-MM-DD]
- A direct quote (at least one full sentence) from strategy.md confirming you
  actually read it

---

## Step 2 -- Find all signal artifacts

Search `simulations/` for every file whose name contains the topic slug.
For each one, write a row:

| Artifact filename | Artifact date | NEW or PRIOR | Namespace |
|-------------------|---------------|--------------|-----------|

Classify each artifact:
- NEW = artifact date is after the STRATEGY DATE
- PRIOR = artifact date is the same as or before the STRATEGY DATE

Now go through all 9 namespaces and note what you found:
  scout, draft, review, flow, trace, prove, listen, program, topic

For each namespace: how many artifacts total, how many are NEW.
Write "0 artifacts -- ABSENT" for any namespace with nothing.

---

## Step 3 -- Delta summary

After classifying every artifact, write this sentence exactly (fill in the parts):

  Strategy was written on [STRATEGY DATE]. [N] artifacts are NEW. [M] are PRIOR.

[N] and [M] must be plain integers -- not "a few", "several", or any other
non-integer value.

If N is 0, write: "No new signals since [STRATEGY DATE]. Strategy is current."
Stop here -- no proposals are possible.

---

## Step 4 -- Read the NEW artifacts

Read only the NEW artifacts. The PRIOR ones were already available when
strategy.md was written -- they're not new information.

Write a short paragraph (no headers, no bullets) describing what the NEW
artifacts say taken together. Mention at least two artifact filenames.
Don't compare to strategy.md yet -- just describe what you found.

---

## Step 5 -- Proposals

Now compare what the NEW artifacts revealed to the current strategy.md.
For each change you'd propose, fill one row in this table:

| # | Action | Dimension | Evidence artifact | Before | After | Why this beats NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|--------------------------|

Rules for the "Why this beats NO CHANGE" column:

The following phrases are BANNED -- any row containing them will be removed
before applying:
- "compelling reason"
- "clearly warranted"
- "update is needed"
- "this should be updated"
- "obvious improvement"
- "no change needed"
- "as expected"
- "the strategy benefits from this"
- Any phrase that doesn't name a specific consequence of NOT changing

The "Why this beats NO CHANGE" cell must state what would go wrong -- or what
specific opportunity would be missed -- if the strategy were left exactly as-is.
A good answer names a risk, gap, or incorrect prediction the new artifact exposes.

For each change type you are NOT proposing, write one line:
- ADDITIONS: none -- [specific reason why no new dimensions emerged]
- REMOVALS: none -- [specific reason why existing dimensions still hold]
- REPRIORITIZATIONS: none -- [specific reason why order/weight is unchanged]

"No change needed" is not an acceptable reason in null declarations either.
State what the new evidence showed and why it didn't cross the bar.

If proposals exist, also write a before/after diff:
| Dimension | Before | After |
|-----------|--------|-------|

---

## Step 6 -- Confirmation gate

Show Step 2 (inventory + namespace audit), Step 3 (delta summary sentence),
and Step 5 (proposals + before/after diff).

Then write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Do not write anything else until the user replies.

---

## Step 7 -- Apply (triggered by YES or REVISED)

Apply exactly the confirmed changes to strategy.md. Don't reformat anything
you didn't change.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Lifecycle Emphasis -- Delta Summary as Standalone Mandatory Output Block

**Variation axis**: Lifecycle emphasis -- the delta detection step is expanded into
its own gated phase whose sole primary deliverable is the templated counted-total
sentence; the phase may not be exited until the sentence contains exact integers.
Single axis.

**Hypothesis**: C-15 requires a mandatory templated sentence with exact counts. In
prior variations the delta detection and classification happened within a larger
inventory step, and the sentence was one requirement among many. When a step has
many requirements, models tend to satisfy the easier ones and elide the harder
quantitative ones. Splitting delta detection into a standalone phase -- with a named
output block ("DELTA SUMMARY") that must contain exact integers before the phase
exits -- makes the templated sentence the only deliverable of that phase. The exit
gate cannot be passed by producing a filled table; it requires the sentence. This
tests whether isolated phase responsibility improves counted-total compliance
independently of other structural elements.

```
You are running /topic:plan for the topic named in the user's message.

This skill runs in named phases. Each phase has a single primary deliverable and an
exit gate. You may not advance to the next phase until the current phase exit gate
is satisfied.

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file path for this topic.
Read strategy.md.

**Phase 1 deliverable**:

  STRATEGY FILE: [path]
  STRATEGY DATE: [YYYY-MM-DD]
  DIMENSIONS: [comma-separated list of dimensions named in strategy.md]

Quote at least one complete sentence from strategy.md (scope, priority, or
completion criterion).

**Phase 1 exit gate**: STRATEGY DATE is recorded as YYYY-MM-DD AND at least one
direct quote from strategy.md is present. If either is missing, re-read and retry.
Do not advance to Phase 2 without passing this gate.

---

## Phase 2 -- Signal inventory

List every artifact in `simulations/` whose filename contains the topic slug.

**Phase 2 deliverable -- Inventory table**:

| Artifact filename | Artifact date | Namespace |
|-------------------|---------------|-----------|
| [fill] | YYYY-MM-DD | [fill] |

Then assess all 9 namespaces:

| Namespace | Artifact count | Assessment |
|-----------|---------------|------------|
| scout | [N] | COVERED / ABSENT |
| draft | [N] | COVERED / ABSENT |
| review | [N] | COVERED / ABSENT |
| flow | [N] | COVERED / ABSENT |
| trace | [N] | COVERED / ABSENT |
| prove | [N] | COVERED / ABSENT |
| listen | [N] | COVERED / ABSENT |
| program | [N] | COVERED / ABSENT |
| topic | [N] | COVERED / ABSENT |

**Phase 2 exit gate**: All 9 namespace rows are present with counts. Blank rows
or missing namespaces are a gate failure. Do not advance to Phase 3 without
passing this gate.

---

## Phase 3 -- Delta detection: DELTA SUMMARY BLOCK

Classify every artifact from Phase 2:
- NEW: artifact date > STRATEGY DATE
- PRIOR: artifact date <= STRATEGY DATE

**Phase 3 primary deliverable -- DELTA SUMMARY BLOCK**:

This block is the sole required output of Phase 3. It must appear with exact
integers substituted for the bracketed placeholders:

  DELTA SUMMARY
  Strategy was written on [STRATEGY DATE]. [N] artifacts are NEW. [M] are PRIOR.
  NEW artifacts: [comma-separated filenames, or "none"]
  PRIOR artifacts: [comma-separated filenames, or "none"]

[N] and [M] must be integers. Writing "a few", "several", "some", or any
non-integer value in place of [N] or [M] is a gate failure.

**Phase 3 exit gate**: The DELTA SUMMARY BLOCK is present, [N] and [M] are
integers, and NEW and PRIOR artifact lists are filled. If N = 0:
  Write: "STRATEGY IS CURRENT -- 0 artifacts are NEW since [STRATEGY DATE].
  No update warranted."
  Stop. Do not proceed to Phase 4.
Do not advance to Phase 4 without passing this gate.

---

## Phase 4 -- Read NEW artifacts

Read each artifact listed in the NEW artifacts line of the DELTA SUMMARY BLOCK.
PRIOR artifacts may not be read for proposal purposes -- they are already
reflected in strategy.md.

**Phase 4 deliverable**: A short paragraph (no headings, no bullets) describing
what the NEW artifacts collectively reveal. Must name at least two artifact
filenames.

**Phase 4 exit gate**: Paragraph exists and at least two NEW artifact filenames
appear in it.

---

## Phase 5 -- Proposals

Compare NEW artifact findings to each STRATEGY dimension from Phase 1.

**Phase 5 deliverable -- Proposal table**:

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [NEW filename only] | [fill] | [fill] | [specific consequence of NOT changing] |

Only filenames from the NEW artifacts line of the DELTA SUMMARY BLOCK may
appear in the Evidence artifact column. A PRIOR filename in this column is a
gate failure.

Null declarations (required per change type):
- "ADDITIONS: none -- [specific to this topic]"
- "REMOVALS: none -- [specific to this topic]"
- "REPRIORITIZATIONS: none -- [specific to this topic]"

If proposals exist, also produce a before/after diff:
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|

**Phase 5 exit gate**: Every evidence artifact in the proposal table appears
in the DELTA SUMMARY NEW artifacts list.

---

## Phase 6 -- Confirmation gate

Display: Phase 2 inventory table, Phase 2 namespace audit, Phase 3 DELTA SUMMARY
BLOCK, Phase 5 proposal table, Phase 5 before/after diff (if present).

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.

---

## Phase 7 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Role Sequence + Output Format -- Defense Register with Sentinel Tokens

**Variation axis**: Role sequence (defense register before reading NEW artifacts,
committing to what strategy.md would argue on its own behalf) combined with output
format (sentinel `??` tokens in all table schemas so gaps are machine-scannable).
Combined.

**Hypothesis**: Defense-first role sequence (from R1 V-04 lineage) creates a
fair-fight framing: the model commits to what it would defend before reading the
challengers, preventing opportunistic proposals from artifacts that happen to match
available dimensions. Combining this with sentinel `??` tokens (C-14) targets the
gap that a defense register without sentinels still allows silent omissions in the
inventory table. With `??` pre-printed in every data cell, a model that skips a row
must actively remove the sentinel -- making skipping a visible act rather than a
silent one. C-15 is satisfied by a required templated sentence at the delta step.
C-16 is satisfied by a named banned-phrase rule in the proposal gate that names
the defense argument the "vs. NO CHANGE" cell must reference.

```
You are running /topic:plan for the topic named in the user's message.

---

## Opening premise

The default outcome is NO CHANGE. Strategy documents represent prior considered
decisions. New evidence must earn a proposal by defeating a specific strategy
position -- not by matching a dimension the model noticed opportunistically.

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file path. Read strategy.md.

Record:
  STRATEGY FILE: ??
  STRATEGY DATE: ??

Replace `??` with real values before continuing.

List every dimension named in strategy.md. Number them. You will defend each
one in Step 2.

  1. ??
  2. ??
  (continue for all dimensions)

Quote at least one complete sentence from strategy.md.

---

## Step 2 -- Pre-signal defense register

Before reading any signal artifact, fill this table. Record the strongest
argument for keeping each strategy dimension as-is. Replace every `??` with
a real value -- a `??` remaining in any cell indicates the defense was skipped.

| Dimension | Defense argument (keep-unchanged) | What evidence would override this |
|-----------|----------------------------------|-----------------------------------|
| ?? | ?? | ?? |
(one row per dimension from Step 1)

Complete this table in full before reading any signal artifact. This register
is the baseline against which NEW artifacts will be measured.

---

## Step 3 -- Signal inventory

List every artifact in `simulations/` whose filename contains the topic slug.
Fill this table. Replace each `??` with a real value. If a value genuinely cannot
be determined, write `??` and note why -- do not silently skip the row.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| ?? | ?? | ?? | ?? |

Assess all 9 namespaces. Replace `??` in every cell:

| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | ?? | ?? | ?? |
| draft | ?? | ?? | ?? |
| review | ?? | ?? | ?? |
| flow | ?? | ?? | ?? |
| trace | ?? | ?? | ?? |
| prove | ?? | ?? | ?? |
| listen | ?? | ?? | ?? |
| program | ?? | ?? | ?? |
| topic | ?? | ?? | ?? |

Classify: NEW = artifact date > STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

---

## Step 4 -- Delta summary

After classification, write this sentence exactly (replace bracketed parts
with exact integers):

  Strategy was written on [STRATEGY DATE]. [N] artifacts are NEW. [M] are PRIOR.

[N] and [M] must be integers. Do not write "several", "a few", or any
non-integer value.

If N = 0: write "No new signals since [STRATEGY DATE]. Strategy is current."
Stop here.

---

## Step 5 -- Read NEW artifacts and challenge defense register

Read only the NEW artifacts. For each NEW artifact, write one row matching
it to the Step 2 defense register. Replace every `??`:

| NEW Artifact | Dimension challenged | Defense argument tested | Assessment |
|--------------|---------------------|------------------------|------------|
| ?? | ?? | ?? | VALIDATES / WEAKENS / INVALIDATES |

If a NEW artifact raises a dimension absent from the Step 2 register, add:
| ?? | [NEW DIMENSION] | none registered | CANDIDATE ADDITION |

---

## Step 6 -- Proposals

For each row in Step 5 where Assessment is WEAKENS or INVALIDATES, propose
a change. For each CANDIDATE ADDITION, evaluate whether it warrants an ADD.

Fill this table. Replace every `??`:

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| ?? | ?? | ?? | ?? | ?? | ?? | ?? |

BANNED phrases in the "vs. NO CHANGE" column -- any row containing these
phrases will be removed before applying:
- "no change needed"
- "compelling reason"
- "clearly warranted"
- "obviously beneficial"
- "update is warranted"

The "vs. NO CHANGE" cell must name the defense argument from Step 2 that the
NEW artifact defeated. A cell that does not reference a Step 2 defense argument
fails this requirement.

Null declarations (required per change type):
- If no additions: "ADDITIONS: none -- Step 2 defenses held against all NEW artifacts."
- If no removals: "REMOVALS: none -- Step 2 defenses held against all NEW artifacts."
- If no reprioritizations: "REPRIORITIZATIONS: none -- Step 2 defenses held against
  all NEW artifacts."

If proposals exist, produce a before/after diff:

| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| ?? | ?? | ?? | ?? |

---

## Step 7 -- Confirmation gate

Display Step 3 (inventory + namespace audit), Step 4 (delta summary), Step 5
(challenge assessment), Step 6 (proposals + before/after diff).

Scan all tables for remaining `??` tokens. Resolve any before displaying.

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.

---

## Step 8 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Full Combination -- Sentinel Tokens + Counted-Total Block + Banned Phrases + Phase Gates

**Variation axis**: Combined -- Output format (`??` sentinel tokens in all
pre-committed schemas, C-14) + Lifecycle emphasis (DELTA SUMMARY BLOCK as a
standalone gated phase with one required deliverable, C-15) + Phrasing register
(conversational with an explicit named banned-phrase blacklist, C-16) + Named phases
with binary exit gates (C-02, C-03 essential) + Inertia framing as opening premise
(C-08 recommended). Full combination.

**Hypothesis**: C-14, C-15, and C-16 are the three new criteria in v3. Each has a
failure mode that earlier rubric versions left open:
- C-14's gap: absent cells look the same as blank schema cells -- `??` sentinels close this
- C-15's gap: counted-total sentence gets elided when it shares a step with other
  deliverables -- a standalone gated phase with one required output closes this
- C-16's gap: "no generic phrases" is a policy clause, not a blacklist -- naming the
  banned phrases inline at the proposal gate closes this

Combining all three with the established phase-gate structure and inertia premise creates
a prompt where all five essential criteria, all three recommended criteria, and all three
new v3 aspirational criteria each have dedicated structural mechanisms rather than
prose reminders.

```
You are running /topic:plan for the topic named in the user's message.

---

## Opening premise

The default outcome of this skill is NO CHANGE to strategy.md. Inertia is a
co-equal option, not a fallback. New signals must earn their way into a proposal
by defeating a specific strategy position. The burden of proof rests on change,
not on stability. This premise governs every proposal gate below.

---

## Pre-committed output schema

Declare before reading any file. Every table below will be filled exactly as shown.
No table may be replaced by prose. No table may be omitted.

Every data cell in the schemas below is pre-filled with `??`. Rules:
- Replace `??` with a real value as you fill each table.
- If a value is genuinely absent (no artifact exists), write `--` (dash).
- A `??` remaining in any final output cell is a machine-detectable gap.
- Do not leave `??` in any cell you could fill.

**Schema A -- Strategy anchor**
| Item | Value |
|------|-------|
| Strategy file path | ?? |
| STRATEGY DATE | ?? |
| Dimensions in strategy.md | ?? |

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| ?? | ?? | ?? | ?? |

**Schema C -- Namespace audit (all 9 rows required)**
| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | ?? | ?? | ?? |
| draft | ?? | ?? | ?? |
| review | ?? | ?? | ?? |
| flow | ?? | ?? | ?? |
| trace | ?? | ?? | ?? |
| prove | ?? | ?? | ?? |
| listen | ?? | ?? | ?? |
| program | ?? | ?? | ?? |
| topic | ?? | ?? | ?? |

**Schema D -- DELTA SUMMARY BLOCK** (sole deliverable of Phase 3)
  DELTA SUMMARY
  Strategy was written on ??. ?? artifacts are NEW. ?? are PRIOR.
  NEW artifacts: ??
  PRIOR artifacts: ??

**Schema E -- Change proposals -- ADDITIONS**
| # | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|-----------|-------------------|--------|-------|---------------|
| ?? | ?? | ?? | ?? | ?? | ?? |

**Schema F -- Change proposals -- REMOVALS / REPRIORITIZATIONS**
| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| ?? | ?? | ?? | ?? | ?? | ?? | ?? |

**Schema G -- Before/after diff**
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| ?? | ?? | ?? | ?? |

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature | Resolution |
|-------------|----------|----------|-----------|--------|------------|
| ?? | ?? | ?? | ?? | ?? | ?? |

---

## Phase 1 -- Read strategy.md (exit gate required)

Read `simulations/TOPICS.md` to find the strategy file path for this topic.
Read strategy.md. Fill Schema A (replace all `??`).
Quote at least one complete sentence from strategy.md.

**Phase 1 exit gate**: STRATEGY DATE is recorded as YYYY-MM-DD AND a direct quote
from strategy.md appears. If either missing, re-read and retry.
Do not advance to Phase 2 without passing this gate.

---

## Phase 2 -- Signal inventory and namespace audit (exit gate required)

Find every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (replace all `??`; use `--` for genuinely absent values).
Fill Schema C (replace all `??`; all 9 rows required).
Classify: NEW = artifact date > STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

**Phase 2 exit gate**: All 9 rows of Schema C are present with integer counts.
Any missing namespace row is a gate failure. Do not advance to Phase 3 without
passing this gate.

---

## Phase 3 -- Delta detection: DELTA SUMMARY BLOCK (exit gate required)

Fill Schema D. Replace every `??` with exact values:
- "Strategy was written on [STRATEGY DATE]." -- exact date from Schema A
- "[N] artifacts are NEW." -- exact integer count of NEW artifacts from Schema B
- "[M] are PRIOR." -- exact integer count of PRIOR artifacts from Schema B
- "NEW artifacts:" -- comma-separated filenames from Schema B, or "none"
- "PRIOR artifacts:" -- comma-separated filenames from Schema B, or "none"

[N] and [M] must be integers. Writing "several", "a few", "some", or any
non-integer value in place of [N] or [M] is a gate failure.

**Phase 3 exit gate**: Schema D is filled with exact integers for NEW and PRIOR
counts. If N = 0:
  Write: "STRATEGY IS CURRENT -- 0 artifacts are NEW since [STRATEGY DATE].
  No update warranted."
  Stop. Do not proceed to Phase 4.
Do not advance to Phase 4 without passing this gate.

---

## Phase 4 -- Read NEW artifacts

Read each artifact listed in the NEW artifacts line of Schema D.
PRIOR artifacts are already reflected in strategy.md. Reading them for proposal
purposes would re-litigate settled decisions.

Write a short paragraph (no headings, no bullets) describing what the NEW
artifacts collectively reveal. Name at least two artifact filenames.

---

## Phase 5 -- Comparison

Map each NEW artifact finding to a dimension in Schema A. Write one row per
dimension:

| Dimension | In strategy? | NEW signal | Assessment |
|-----------|-------------|-----------|------------|
| ?? | YES / NO | [summary] | VALIDATED / CHALLENGED / NOT COVERED / NEW |

---

## Phase 6 -- Proposals (exit gate required)

Reminder: NO CHANGE is the default verdict.

Fill Schema E (Additions). Fill Schema F (Removals / Reprioritizations).

**BANNED phrases in the "vs. NO CHANGE" column**:
Any row whose "vs. NO CHANGE" cell contains one of these phrases will be
removed from the proposal before applying:
- "no change needed"
- "compelling reason"
- "clearly warranted"
- "obviously beneficial"
- "update is warranted"
- "the strategy benefits from this"
- "as expected"

The "vs. NO CHANGE" cell must state what would go wrong -- or what specific
opportunity would be missed -- if the strategy were left exactly as-is.
Naming a risk, gap, or incorrect prediction is sufficient. A phrase that could
apply to any topic regardless of its content is not sufficient.

Null declarations (required per change type, labeled separately):
- If no additions: "ADDITIONS: none -- [specific reason this topic's NEW artifacts
  do not warrant new dimensions]"
- If no removals: "REMOVALS: none -- [specific reason existing dimensions still hold]"
- If no reprioritizations: "REPRIORITIZATIONS: none -- [specific reason order/weight
  is unchanged]"

Note: "No change needed" is not acceptable as a null reason. State what the new
evidence showed and why it didn't cross the bar for a proposal.

Fill Schema G (before/after diff) for each row in Schema E and Schema F.

Fill Schema H (conflict audit). Identify any two NEW artifacts that contradict
each other on the same strategy dimension. If none:
  "CONFLICT AUDIT: none -- no contradictions detected between NEW artifacts."

Evidence artifacts in Schema E and Schema F must appear in Schema D NEW list.
A PRIOR filename in the Evidence column is a gate failure -- remove that row.

**Phase 6 exit gate**: Every evidence artifact in Schema E and Schema F appears
in Schema D NEW artifacts list. No banned phrases remain in any "vs. NO CHANGE"
cell. Null declarations for all three change types are present.

---

## Phase 7 -- Confirmation gate

Display Schema B, Schema C, Schema D (DELTA SUMMARY BLOCK), Schema E, Schema F,
Schema G, and Schema H.

Scan all schemas for remaining `??` tokens. Resolve any before displaying.

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.

---

## Phase 8 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Round 3 Variation Summary

| Variation | Primary axis | New criteria targeted | Key mechanism | Hypothesis |
|-----------|--------------|-----------------------|---------------|------------|
| V-01 | Output format | C-14 (`??` sentinels), C-15 (integer slots) | Pre-print `??` in all schema cells; delta sentence with `??` slots | Sentinel tokens make gaps machine-scannable without requiring human diff-reading |
| V-02 | Phrasing register | C-16 (named banned-phrase blacklist) | Conversational direct-address; inline banned-phrase list at proposal gate | Named phrases close the escape hatch that "no generic phrases" leaves open |
| V-03 | Lifecycle emphasis | C-15 (standalone DELTA SUMMARY BLOCK) | DELTA SUMMARY BLOCK as sole deliverable of its own gated phase | Isolated phase with one integer-required output improves counted-total compliance |
| V-04 | Role sequence + Output format | C-14, C-15, C-16 | Defense register before reading artifacts + `??` sentinels in all tables | Fair-fight framing prevents opportunistic proposals; sentinels close silent-omission gap |
| V-05 | Full combination | C-14, C-15, C-16 + all essential + recommended | `??` sentinels + standalone DELTA SUMMARY BLOCK phase + named banned-phrase blacklist + phase gates + inertia premise | All three new v3 criteria have dedicated structural mechanisms rather than prose reminders |

**Structural risk ranking** (lowest risk first): V-05 > V-03 > V-04 > V-01 > V-02

V-05 encodes C-14, C-15, and C-16 each as dedicated mechanisms inside named phases
with exit gates. V-02 relies most on the conversational tone carrying the banned-phrase
rule to the proposal gate; under long context, the blacklist may be treated as a
preamble note rather than a per-cell constraint.
