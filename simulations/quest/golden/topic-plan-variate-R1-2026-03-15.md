# topic-plan Skill Variations — Round 1 (2026-03-15)

Rubric: v1 (C-01 Read strategy.md, C-02 Signal inventory 9-namespace, C-03 Delta
detection by strategy date, C-04 Typed proposals with explicit null, C-05 Confirmation
gate; C-06 Evidence citation, C-07 Before/after diff, C-08 Inertia justification,
C-09 Type-labeled nulls, C-10 Conflict detection)

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04, V-05).

---

## V-01: Output Format — Pre-Committed Table Schemas

**Variation axis**: Output format — declare all required table schemas before reading
any file; model fills slots, cannot substitute prose.

**Hypothesis**: C-02 requires all 9 namespaces assessed and C-04 requires typed
proposals with explicit nulls. Both are easy to omit when the model chooses its own
structure. Pre-printing table headers with a Namespace column and an Action column that
accepts only ADD/REMOVE/REPRIORITIZE makes omission a visible blank, not a silent skip.
The 9-namespace checklist as a required row forces assessment even for absent namespaces.

```
You are running /topic:plan for the topic named in the user's message.

Commit to this output schema before reading any file. You will fill these tables
in order. Do not replace any table with prose. Do not merge tables.

---

## Output Schema (pre-committed)

**Table A — Strategy anchor**
| Item | Value |
|------|-------|
| Strategy file path | [fill] |
| Strategy last-modified date | YYYY-MM-DD |
| Dimensions in strategy.md | [comma-separated list] |

**Table B — Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| [fill]            | YYYY-MM-DD    | [fill]      | [fill]    |

**Table C — Namespace coverage (all 9 namespaces required)**
| Namespace | Artifacts found | Any NEW? | Status |
|-----------|-----------------|----------|--------|
| scout     | [N]             | YES / NO | COVERED / ABSENT |
| draft     | [N]             | YES / NO | COVERED / ABSENT |
| review    | [N]             | YES / NO | COVERED / ABSENT |
| flow      | [N]             | YES / NO | COVERED / ABSENT |
| trace     | [N]             | YES / NO | COVERED / ABSENT |
| prove     | [N]             | YES / NO | COVERED / ABSENT |
| listen    | [N]             | YES / NO | COVERED / ABSENT |
| program   | [N]             | YES / NO | COVERED / ABSENT |
| topic     | [N]             | YES / NO | COVERED / ABSENT |

**Table D — Change proposals**
| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [filename] | [fill] | [fill] | [fill] |

**Table E — Before/after diff**
| Dimension | Before | After | Source proposal |
|-----------|--------|-------|-----------------|
| [fill]    | [fill] | [fill]| ADD-N / REMOVE-N / REPRIORITIZE-N |

---

## Step 1 — Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file path for this topic.
Read strategy.md. Record its last-modified date as the STRATEGY DATE.
Fill Table A now.

---

## Step 2 — Signal inventory

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Table B. Classify each artifact: NEW if artifact date > STRATEGY DATE, else PRIOR.
Then fill Table C, counting artifacts per namespace. Mark ABSENT for namespaces with
no artifacts. Do not skip any of the 9 namespace rows.

---

## Step 3 — Proposals

Only NEW artifacts (date > STRATEGY DATE) may drive change proposals.

Fill Table D. For each proposed change:
- Action must be exactly ADD, REMOVE, or REPRIORITIZE — no other values
- Evidence artifact must be a filename from the NEW list in Table B
- "vs. NO CHANGE" cell must explain why this specific change beats leaving
  strategy.md unchanged — "compelling reason" is not sufficient

If no changes are warranted, write exactly:
  "ADDITIONS: none — no NEW artifacts warrant additions."
  "REMOVALS: none — no NEW artifacts warrant removals."
  "REPRIORITIZATIONS: none — no NEW artifacts warrant reprioritizations."

Then fill Table E for each row in Table D (skip if Table D is empty).

---

## Step 4 — Confirmation gate

Display Table B, Table C, Table D, and Table E.

Then write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop here. Write nothing further until the user replies.

---

## Step 5 — Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
After writing, confirm: "strategy.md updated: [N] additions, [N] removals,
[N] reprioritizations."
```

---

## V-02: Inertia Framing — NO CHANGE as the Default Verdict

**Variation axis**: Inertia framing — the opening premise names NO CHANGE as the
default outcome; every proposal must earn its inclusion by explicitly defeating the
null; the preamble repeats at the proposal gate.

**Hypothesis**: C-08 (inertia justification) is the recommended criterion most likely
to be satisfied by annotation rather than structure. Leading with "NO CHANGE is the
default verdict" and repeating it at the proposal gate makes the justification a
precondition for inclusion, not an optional column. A model that omits the "vs. NO
CHANGE" column cannot claim to have followed the instructions.

```
You are running /topic:plan for the topic named in the user's message.

---

## Opening premise

The default outcome of this skill is NO CHANGE to strategy.md. Strategy documents
represent considered decisions. They have inertia for good reason. New signals must
earn their way into a change proposal. Your role is to determine whether any new
signal provides sufficient evidence to depart from the status quo — not to find
reasons to update the strategy.

---

## Step 1 — Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file path. Read strategy.md.
Record its last-modified date as the STRATEGY DATE.

Quote at least two concrete facts from strategy.md (dimensions, priorities, completion
criteria, or scope). These quotes confirm you have read it.

---

## Step 2 — Signal inventory

List every signal artifact in `simulations/` whose filename contains the topic slug.
For each artifact output one row:

  [artifact filename] | [artifact date] | NEW / PRIOR | [namespace]

Then assess all 9 namespaces explicitly:

  scout: [N artifacts] — NEW: [Y/N]
  draft: [N artifacts] — NEW: [Y/N]
  review: [N artifacts] — NEW: [Y/N]
  flow: [N artifacts] — NEW: [Y/N]
  trace: [N artifacts] — NEW: [Y/N]
  prove: [N artifacts] — NEW: [Y/N]
  listen: [N artifacts] — NEW: [Y/N]
  program: [N artifacts] — NEW: [Y/N]
  topic: [N artifacts] — NEW: [Y/N]

Classify: NEW if artifact date > STRATEGY DATE. PRIOR otherwise.
State the STRATEGY DATE here before classifying.

---

## Step 3 — Read NEW artifacts only

Read only the NEW artifacts. PRIOR artifacts are already incorporated in strategy.md —
using them as evidence would be re-litigating settled decisions.

Write a short paragraph (no structure, no headings) describing what the NEW artifacts
reveal. Name at least two artifacts by filename. Do not compare to strategy.md yet.

---

## Step 4 — Map NEW signals against strategy dimensions

For each dimension in strategy.md, write one line:

  [Dimension] — VALIDATED / CHALLENGED / NOT COVERED — [1 sentence] — [source artifact]

For each dimension in NEW artifacts that is absent from strategy.md, write one line:

  [Dimension] [NEW] — CANDIDATE ADDITION — [source artifact]

---

## Step 5 — Proposal gate

Reminder: NO CHANGE is the default verdict. A proposal is only included if it
clearly beats leaving strategy.md as-is.

For each potential change, ask: does this beat NO CHANGE?
- YES → include it in the proposal table below
- NO or UNCERTAIN → exclude it; write one line explaining why NO CHANGE wins

Proposal table:

| # | Action | Dimension | Evidence artifact | Before | After | Why this beats NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|--------------------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [filename] | [fill] | [fill] | [fill — specific, not generic] |

"Why this beats NO CHANGE" must name the specific consequence of NOT changing. A
generic phrase such as "compelling argument exists" or "clearly warranted" fails this
requirement.

If the proposal table is empty after the gate:
  Write: "NO CHANGE — new signals validate the existing strategy without warranting
  updates."

Before/after diff (produce only if proposals exist):

| Dimension | Before | After |
|-----------|--------|-------|
| [fill]    | [fill] | [fill]|

---

## Step 6 — Confirmation gate

Display Step 4, Step 5, and the before/after diff.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop here. Write nothing further until the user replies.

---

## Step 7 — Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. No additional edits.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Lifecycle Emphasis — Named Phases with Binary Exit Gates

**Variation axis**: Lifecycle emphasis — each phase has an explicit exit condition that
must be satisfied before the model may advance; the 9-namespace audit and delta
detection are isolated phases with stop conditions.

**Hypothesis**: C-02 (9-namespace coverage) and C-03 (delta detection with named
strategy date) are both candidates for silent truncation under a flat step structure.
Wrapping them in named phases with binary "PASS / STOP" exit gates makes truncation a
visible structural failure rather than an invisible omission. The model cannot arrive
at the proposal phase without passing the namespace audit and the delta detection gates.

```
You are running /topic:plan for the topic named in the user's message.

This skill runs in named phases. Each phase has an exit condition. You may not
advance to the next phase until the current phase's exit condition is satisfied.

---

## Phase 1 — Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file path. Read strategy.md.
Note its last-modified date.

Record:
  STRATEGY FILE: [path]
  STRATEGY DATE: [YYYY-MM-DD]

Quote at least one complete sentence from strategy.md (scope, completion criteria,
or sequencing) to confirm you have read it.

**Exit gate**: STRATEGY DATE is recorded AND at least one direct quote from
strategy.md appears in output. PASS → proceed to Phase 2. FAIL → re-read and retry.

---

## Phase 2 — Signal inventory and 9-namespace audit

List every artifact in `simulations/` whose filename contains the topic slug:

| Artifact filename | Artifact date | Namespace |
|-------------------|---------------|-----------|
| [fill]            | YYYY-MM-DD    | [fill]    |

Then assess all 9 namespaces. Every namespace must appear — ABSENT is a valid status:

| Namespace | Count | Any artifact date > STRATEGY DATE? |
|-----------|-------|-------------------------------------|
| scout     | [N]   | YES / NO                            |
| draft     | [N]   | YES / NO                            |
| review    | [N]   | YES / NO                            |
| flow      | [N]   | YES / NO                            |
| trace     | [N]   | YES / NO                            |
| prove     | [N]   | YES / NO                            |
| listen    | [N]   | YES / NO                            |
| program   | [N]   | YES / NO                            |
| topic     | [N]   | YES / NO                            |

**Exit gate**: All 9 namespace rows are present AND each row has a count and a
YES/NO for new artifacts. PASS → proceed to Phase 3. FAIL → re-fill the table.

---

## Phase 3 — Delta detection

Partition the inventory from Phase 2:

  NEW (artifact date > STRATEGY DATE):
  - [filename] | [date]

  PRIOR (artifact date <= STRATEGY DATE):
  - [filename] | [date]

PRIOR artifacts are already baked into strategy.md. They may not drive proposals.

**Exit gate**: At least one NEW artifact exists. If all artifacts are PRIOR, write:
"No new signals since STRATEGY DATE ([date]). Strategy is current. No update needed."
and stop here.

---

## Phase 4 — Read and synthesize NEW artifacts

Read each NEW artifact. Write a short freeform paragraph about what these NEW
artifacts collectively reveal. No headings. No bullet points. Name at least two
artifacts by filename. Do not compare to strategy.md yet.

**Exit gate**: Paragraph exists and references at least two artifact filenames.

---

## Phase 5 — Comparison and proposals

Compare NEW artifact findings to strategy.md. For each strategy dimension, assess
whether new signals validate, challenge, or do not touch it.

Then produce the proposal table:

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [NEW artifact filename] | [fill] | [fill] | [specific reason] |

Only NEW artifacts (Phase 3) may appear in the Evidence column.

If no proposals are warranted:
  "ADDITIONS: none — inertia holds."
  "REMOVALS: none — inertia holds."
  "REPRIORITIZATIONS: none — inertia holds."

If proposals exist, also produce a before/after diff:

| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| [fill]    | [fill] | [fill]| ADD-N / REMOVE-N / REPRIORITIZE-N |

**Exit gate**: Every evidence artifact in the proposal table appears in the Phase 3
NEW list. Any PRIOR artifact cited is a gate failure — remove that row.

---

## Phase 6 — Confirmation gate

Display Phase 2 (inventory), Phase 3 (delta partition), Phase 5 (proposals), and
Phase 5 (before/after diff if present).

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop. Write nothing further until the user replies.

---

## Phase 7 — Apply (triggered by YES or REVISED)

Write exactly the confirmed changes. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Role Sequence + Inertia Framing — Defense-First Before Reading Signals

**Variation axis**: Role sequence (strategy defense registered before reading NEW
artifacts) + Inertia framing (NO CHANGE is explicitly named as the default at the
opening and at the proposal gate).

**Hypothesis**: In prior rounds, proposals tended to be opportunistic — the model
read signals and matched them against strategy without first asking what the strategy
gets right. A pre-signal defense register (Step 2) forces the model to commit to what
it would defend before it reads the challengers. This creates a fair fight between
each NEW artifact and the strategy position it threatens, rather than a one-sided
scan for update opportunities. Combined with front-loaded inertia framing, the burden
of proof on change is structural, not decorative.

```
You are running /topic:plan for the topic named in the user's message.

---

## Opening premise

The default outcome of this skill is NO CHANGE to strategy.md. New signals must
earn their way into a proposal by defeating the specific strategy position they
challenge. The burden of proof rests on change, not on stability.

---

## Step 1 — Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file path. Read strategy.md.
Record its last-modified date as the STRATEGY DATE.

Identify all strategy dimensions (scope, sequencing, priorities, completion criteria).
List them in a numbered register — you will defend each one explicitly in Step 2.

  STRATEGY DATE: [YYYY-MM-DD]
  Dimensions: 1. [name], 2. [name], 3. [name], ...

---

## Step 2 — Pre-signal defense register

Before reading any signal artifact, record the strongest argument for keeping each
strategy dimension as-is. This is not advocacy — it is a record of what the strategy
would argue on its own behalf.

| Dimension | Strongest keep-unchanged argument | What evidence would invalidate this |
|-----------|----------------------------------|--------------------------------------|
| [name]    | [1–2 sentences]                  | [specific signal type or finding]    |

Complete this table before reading any signal artifact.

---

## Step 3 — Signal inventory

List every artifact in `simulations/` whose filename contains the topic slug:

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| [fill]            | YYYY-MM-DD    | [fill]      | [fill]    |

Assess all 9 namespaces (even if absent):

  scout / draft / review / flow / trace / prove / listen / program / topic

For each: count of artifacts, count of NEW artifacts.

NEW = artifact date > STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

---

## Step 4 — Read NEW artifacts (only)

Read each NEW artifact. PRIOR artifacts were available when strategy.md was written;
they are not new evidence.

For each NEW artifact, write one row matching it to the Step 2 defense register:

| NEW Artifact | Dimension challenged | Defense argument it meets | Assessment |
|--------------|---------------------|--------------------------|------------|
| [filename]   | [dimension name]     | [defense argument summary]| VALIDATES / WEAKENS / INVALIDATES |

If a NEW artifact raises a dimension not in the Step 2 register, add a row:

| NEW Artifact | Dimension challenged | Defense argument it meets | Assessment |
|[filename]    | [NEW DIMENSION]      | none registered           | CANDIDATE ADDITION |

---

## Step 5 — Proposals

For each row in Step 4 where Assessment is WEAKENS or INVALIDATES, propose a change.
For each CANDIDATE ADDITION, evaluate whether it warrants an ADD proposal.

Reminder: NO CHANGE is the default verdict. Only propose a change if the NEW
artifact clearly defeats the defense argument in Step 2.

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [NEW filename] | [fill] | [fill] | [specific — name the defense argument defeated] |

Null declarations per change type:
- If no additions: "ADDITIONS: none — Step 2 defenses held against all NEW artifacts."
- If no removals: "REMOVALS: none — Step 2 defenses held against all NEW artifacts."
- If no reprioritizations: "REPRIORITIZATIONS: none — Step 2 defenses held against
  all NEW artifacts."

Before/after diff (if proposals exist):

| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| [fill]    | [fill] | [fill]| [ADD-N / REMOVE-N / REPRIORITIZE-N] |

---

## Step 6 — Confirmation gate

Display Step 3 (inventory), Step 4 (challenge assessment), Step 5 (proposals), and
the before/after diff.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
apply custom version
---

Stop. Write nothing further until the user replies.

---

## Step 7 — Apply (triggered by YES or REVISED)

Write exactly the confirmed changes. No additional edits.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Full Combination — Tables + Inertia + Lifecycle + Typed Null Declarations

**Variation axis**: Combined — Output format (pre-committed tables, V-01) + Inertia
framing (NO CHANGE as opening premise and per-proposal gate, V-02) + Lifecycle
emphasis (named phases with exit conditions, V-03) + Type-labeled null declarations
per change type (C-09 aspirational).

**Hypothesis**: The five essential criteria and all three recommended criteria require
structural enforcement, not prose reminders. V-01's pre-committed tables guarantee
column presence. V-02's inertia framing makes the "vs. NO CHANGE" column a
precondition for inclusion. V-03's phase gates prevent silent advancement past the
9-namespace audit and delta detection. Adding type-labeled null declarations per
change type (C-09) and a conflict audit (C-10) to the schema from the start targets
all five essential plus all three recommended in a single variation.

```
You are running /topic:plan for the topic named in the user's message.

---

## Opening premise

The default outcome of this skill is NO CHANGE to strategy.md. Inertia is a
co-equal option, not a fallback. The burden of proof rests on change, not on
stability. This premise is not ceremonial — it governs every proposal gate below.

---

## Pre-committed output schema

Declare before reading any file. All tables below will be filled exactly as shown.
No table may be replaced by prose. No table may be omitted.

**Schema A — Strategy anchor**
| Item | Value |
|------|-------|
| Strategy file | [path] |
| STRATEGY DATE | YYYY-MM-DD |
| Dimensions | [list] |

**Schema B — Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C — Namespace audit (all 9 rows required)**
| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | | | COVERED / ABSENT |
| draft | | | COVERED / ABSENT |
| review | | | COVERED / ABSENT |
| flow | | | COVERED / ABSENT |
| trace | | | COVERED / ABSENT |
| prove | | | COVERED / ABSENT |
| listen | | | COVERED / ABSENT |
| program | | | COVERED / ABSENT |
| topic | | | COVERED / ABSENT |

**Schema D — Additions proposals**
| # | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|-----------|-------------------|--------|-------|---------------|

**Schema E — Removals / Reprioritizations proposals**
| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|

**Schema F — Before/after diff**
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|

**Schema G — Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature | Resolution |
|-------------|----------|----------|-----------|--------|------------|

---

## Phase 1 — Read strategy.md (exit gate required)

Read `simulations/TOPICS.md` to locate the strategy file. Read strategy.md.
Fill Schema A. Quote at least one concrete sentence from strategy.md.

**Phase 1 exit gate**: STRATEGY DATE is recorded AND at least one direct quote
from strategy.md appears. Do not advance to Phase 2 without passing this gate.

---

## Phase 2 — Signal inventory and namespace audit (exit gate required)

Find every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 namespace rows).

Classify: NEW = artifact date > STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

**Phase 2 exit gate**: All 9 rows of Schema C are present. Do not advance to
Phase 3 without passing this gate.

---

## Phase 3 — Delta detection (exit gate required)

Partition Schema B:

  NEW (date > STRATEGY DATE): [list]
  PRIOR (date <= STRATEGY DATE): [list]

PRIOR artifacts may not drive change proposals. They were available when strategy.md
was written.

**Phase 3 exit gate**: At least one NEW artifact exists. If no NEW artifacts:
  Write: "STRATEGY IS CURRENT — no new signals since STRATEGY DATE ([date]).
  No update warranted."
  Stop. Do not proceed to Phase 4.

---

## Phase 4 — Read NEW artifacts

Read each NEW artifact. Write a short freeform paragraph (no structure, no headings)
about what the NEW artifacts collectively reveal. Name at least two artifacts by
filename. Do not compare to strategy.md yet.

---

## Phase 5 — Comparison

Map each NEW artifact finding to a strategy dimension. Write one row per dimension:

| Dimension | In strategy? | NEW signal coverage | Assessment |
|-----------|-------------|---------------------|------------|
| [fill] | YES / NO | [summary] | VALIDATED / CHALLENGED / NOT COVERED / [NEW] |

---

## Phase 6 — Proposals

Reminder: NO CHANGE is the default verdict.

Fill Schema D (Additions). Fill Schema E (Removals / Reprioritizations).

For each proposal row:
- Evidence artifact must appear in the Phase 3 NEW list
- "vs. NO CHANGE" must name the specific consequence of NOT changing — not
  a generic phrase

Null declarations (required — labeled per change type, not collectively):

  If no additions: "ADDITIONS: none — inertia holds for all candidate additions."
  If no removals: "REMOVALS: none — inertia holds."
  If no reprioritizations: "REPRIORITIZATIONS: none — inertia holds."

A single unlabeled "no changes proposed" covering multiple change types does not
satisfy this requirement.

Fill Schema F (before/after diff) for each row in Schema D and Schema E.

Fill Schema G (conflict audit). Identify any two NEW artifacts that contradict
each other on the same strategy dimension. If none:
  "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts."

---

## Phase 7 — Confirmation gate

Display Schema B, Schema C, Schema D, Schema E, Schema F, and Schema G.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
apply custom version
---

Stop. Write nothing further until the user replies.

---

## Phase 8 — Apply (triggered by YES or REVISED)

Write exactly the confirmed changes. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Round 1 Variation Summary

| Variation | Primary axis | Key hypothesis | C-02 mechanism | C-03 mechanism | C-08 mechanism |
|-----------|-------------|----------------|----------------|----------------|----------------|
| V-01 | Output format | Pre-committed table slots prevent silent omission | Schema C with 9 required namespace rows | NEW/PRIOR column in Schema B; STRATEGY DATE slot | "vs. NO CHANGE" column in Table D |
| V-02 | Inertia framing | Opening premise + per-proposal gate makes inertia structural | 9-namespace list in Step 2 assessment | STRATEGY DATE recorded in Step 2; NEW/PRIOR classification | "Why this beats NO CHANGE" column; gate in Step 5 |
| V-03 | Lifecycle emphasis | Named phases with binary exit gates prevent silent advance | Phase 2 has 9-namespace table with exit gate | Phase 3 delta detection is its own gated phase | "vs. NO CHANGE" column in Phase 5 proposal table |
| V-04 | Role sequence + inertia | Pre-signal defense register forces fair challenge framing | 9-namespace audit in Step 3 | STRATEGY DATE in Step 1; NEW/PRIOR classification | "vs. NO CHANGE" names specific defense argument defeated |
| V-05 | Full combination | All 5 essential + all 3 recommended covered structurally | Schema C (9 rows required, phase gate) | Phase 3 gated delta detection; NEW list locked before proposals | "vs. NO CHANGE" per proposal row; type-labeled null per change type |

**Structural risk ranking** (lowest risk first): V-05 > V-03 > V-01 > V-04 > V-02

V-05 encodes all essential criteria as named phases with exit gates AND pre-commits
all table schemas — failure to satisfy any essential criterion creates a visible
structural gap. V-02 relies most heavily on the opening premise being carried through
to the proposal gate; under long context, this framing is most susceptible to drift.
