# topic-plan Skill Variations — Round 8 (Commitment-Phase Track) (2026-03-15)

Rubric: v8 (C-01–C-29, max composite 111)
New criteria this round: C-28 (Enforcement note as labeled template field), C-29 (Gate sub-requirements use identifier labels)

---

## Round 8 Design Notes

Round 7 of this rubric track surfaced two new structural requirements, both extracted
from V-01:

1. **C-28 — Enforcement note as labeled template field**: C-23 required the enforcement
   note to exist; C-28 requires it to appear as a named, labeled field
   (`Enforcement note: ...`) parallel to `Source dimension:` in the VERBATIM BLOCK
   template. An unlabeled trailing sentence passes C-23 but fails C-28. Without the
   label, Gate 1 Check [2] sub-requirement [2c] has no field name to target.

2. **C-29 — Gate sub-requirements use identifier labels**: C-25 required the enforcement
   note to be named as a sub-requirement of Check [2]; C-29 requires each sub-condition
   of Check [2] to carry its own alphanumeric identifier ([2a], [2b], [2c]). Prose
   enumeration passes C-25 but fails C-29. Labels enable partial-failure attribution —
   a gate result can report `[2b] failed` rather than failing the whole check.

**Round 8 strategy**: All five variations satisfy C-28 (labeled `Enforcement note:` field
in VERBATIM BLOCK template) and C-29 ([2a][2b][2c] labeled sub-conditions in Gate 1
Check [2]) as baseline requirements. The primary discriminating axes are:

| Variation | Axis | C-28/C-29 presentation approach |
|-----------|------|---------------------------------|
| V-01 | Lifecycle emphasis | Gate 1 is a standalone phase; each [2x] sub-check produces its own output line |
| V-02 | Output format | VERBATIM BLOCK pre-declared as named schema template with labeled field slots |
| V-03 | Phrasing register | Conversational-imperative; inline "Gate will check [2c]" motivation for labeled fields |
| V-04 | Inertia framing + role sequence | Defense register before signals; inertia in every proposal gate; labeled contract declaration |
| V-05 | Full combination | Upfront structural contract + pre-declared schemas + lifecycle gates + defense register |

---

## V-01: Lifecycle Emphasis — Gate 1 as Dedicated Phase

**Variation axis**: Lifecycle emphasis — the skill runs in named phases; Gate 1 is its
own dedicated phase (not a checklist embedded in the commitment phase). Each of the three
Check [2] sub-conditions ([2a], [2b], [2c]) produces an explicit output line before the
gate result is declared.

**Hypothesis**: Treating Gate 1 as a named standalone phase forces the model to visit each
[2a][2b][2c] check as a separate step before emitting the gate result. A model cannot
emit `GATE 1: PASS` without first producing all three sub-condition lines. This makes
C-29 compliance a structural consequence of the phase layout rather than an instruction
to remember. The VERBATIM BLOCK template with its labeled `Enforcement note:` field is
introduced in Phase 2 before the model fills it, making C-28 compliance a slot-filling
operation.

```
You are running /topic:plan for the topic named in the user's message.

This skill runs in named phases. Each phase has an exit condition. You may not
advance to the next phase until the current phase exit condition is satisfied and
its result is written to the output.

The default outcome is NO CHANGE to strategy.md. The burden of proof rests on
change, not on stability.

---

## Phase 1 — Read strategy.md and build commitment registry

Read simulations/TOPICS.md to locate the strategy file path for this topic.
Read strategy.md. Record its last-modified date:

  STRATEGY DATE: [YYYY-MM-DD]

List all named strategy dimensions in order, assigning each a D-N label:

  D-1: [dimension name] — [one-line summary of current strategy position]
  D-2: [dimension name] — [one-line summary of current strategy position]
  ...

This is Schema A. Every D-N row must be filled before proceeding. Schema A is the
locked representation of what the strategy currently says. Every proposal's Before
value must come from Schema A — not from a subsequent re-read of strategy.md.

Phase 1 exit gate:
  [PHASE 1 GATE: PASS — STRATEGY DATE recorded, N dimensions in Schema A]
  [PHASE 1 GATE: STOP — describe gap]

---

## Phase 2 — Verbatim quotation with labeled fields

Select the strategy sentence that most directly captures the topic's scope or
sequencing commitment. Copy it verbatim (exact characters). Write it in the
VERBATIM BLOCK using this template exactly — do not rename or merge any field:

=== VERBATIM BLOCK ===
"[exact quoted sentence]"
Source dimension: D-N
Enforcement note: A Source dimension field that does not match a D-N label fails this block.
=== END VERBATIM BLOCK ===

The Source dimension field must use a D-N label from Schema A (Phase 1).
The Enforcement note field must appear as a named, labeled field — not as an
inline parenthetical or trailing sentence within the Source dimension field.

Phase 2 exit gate:
  [PHASE 2 GATE: PASS — VERBATIM BLOCK present, Source dimension in D-N format,
   Enforcement note as labeled field]
  [PHASE 2 GATE: STOP — describe gap]

---

## Phase 3 — Seal the commitment

Write the SEALED BLOCK immediately after the VERBATIM BLOCK:

=== SEALED BLOCK ===
Committed dimensions: D-1 through D-N ([count] total)
Verbatim anchor: [first 10 words of quoted sentence]
Re-read prohibition: strategy.md may not be re-opened or re-read until the user
  applies confirmed changes.
SEAL violation: A Before value in any proposal containing text not present in Schema A
  at seal time is a SEAL violation and must be dropped.
=== END SEALED BLOCK ===

After writing the SEALED BLOCK, write this attestation sentence:
  Commitment table complete. No signal artifacts read yet.

Phase 3 exit gate:
  [PHASE 3 GATE: PASS — SEALED BLOCK complete, temporal attestation written]
  [PHASE 3 GATE: STOP — describe gap]

---

## Phase 4 — Gate 1 (commitment-phase compound verification)

Verify all three commitment-phase artifacts. Write each check result before
declaring the gate outcome.

  Check [1] Schema A: all D-N dimension rows filled?
    [1]: PASS — [N] rows present / FAIL — [describe gap]

  Check [2] VERBATIM BLOCK:
    [2a] Delimiters (=== VERBATIM BLOCK === and === END VERBATIM BLOCK ===) present?
         [2a]: PASS / FAIL
    [2b] Source dimension field present and in D-N format matching a D-N label in Schema A?
         [2b]: PASS — Source dimension D-[N] matches Schema A row [N] / FAIL — [describe mismatch]
    [2c] Enforcement note present as a named, labeled sub-field?
         [2c]: PASS / FAIL

  Check [3] SEALED BLOCK: all required fields present (committed dimensions, verbatim
    anchor, re-read prohibition, SEAL violation definition)?
    [3]: PASS — [N] fields present / FAIL — [describe gap]

  [GATE 1: PASS — all checks passed, proceed to Phase 5]
  [GATE 1: STOP — return to failing phase, fix gap, re-run Gate 1]

Do not proceed to Phase 5 until Gate 1 shows PASS.

---

## Phase 5 — Signal inventory

List every signal artifact in simulations/ whose filename contains the topic slug.
For each artifact, one row:

  [artifact-filename] | [artifact-date] | NEW (date > STRATEGY DATE) or PRIOR | [namespace]

Assess all 9 namespaces. Every namespace must appear. Report 0 total | 0 new for
namespaces with no artifacts:

  scout:   [total] total | [new] new
  draft:   [total] total | [new] new
  review:  [total] total | [new] new
  flow:    [total] total | [new] new
  trace:   [total] total | [new] new
  prove:   [total] total | [new] new
  listen:  [total] total | [new] new
  program: [total] total | [new] new
  topic:   [total] total | [new] new

HIGH-PRESSURE namespaces (new count > 0): [list all HIGH-PRESSURE namespaces]

Phase 5 exit gate:
  [PHASE 5 GATE: PASS — 9 namespace rows present with total|new counts,
   HIGH-PRESSURE list written]
  [PHASE 5 GATE: STOP — describe gap]

---

## Phase 6 — Read NEW artifacts

Read every artifact classified NEW in Phase 5. PRIOR artifacts are already incorporated
in strategy.md — skip them.

Phase 6 exit gate:
  [PHASE 6 GATE: PASS — [N] NEW artifacts read]
  [PHASE 6 GATE: STOP — describe gap]

---

## Phase 7 — Delta detection

For each finding from the NEW artifacts, apply the two-condition novelty gate:
  Condition 1: present in at least one artifact dated after STRATEGY DATE?
  Condition 2: absent from strategy.md (not covered by any D-N row in Schema A)?

CONFIRMED NEW = both conditions true.
PRIOR-ONLY = condition 1 true, condition 2 false.
  Annotate: "PRIOR-ONLY — not a delta." A PRIOR-ONLY finding may not drive an ADD proposal.

Phase 7 exit gate:
  [PHASE 7 GATE: PASS — delta detection complete for all NEW artifact findings]
  [PHASE 7 GATE: STOP]

---

## Phase 8 — Proposals

Write the PROPOSAL SCOPE block at the start of this phase:

PROPOSAL SCOPE:
  HIGH-pressure namespaces: [list from Phase 5]
  Proposals restricted to: HIGH-pressure namespaces only.
  A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.

Scope gate:
  Check: PROPOSAL SCOPE violation condition present as named output category?
  [SCOPE GATE: PASS — violation condition present / STOP — add violation condition line]

Build the proposals table. Only NEW artifacts (from Phase 5) may appear in the Evidence
column. Each Before value must come from Schema A (Phase 1) — not from a re-read of
strategy.md.

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [N] | ADD / REMOVE / REPRIORITIZE | [D-N dimension name] | [NEW filename] | [from Schema A] | [proposed] | [specific consequence of not changing] |

Typed null declarations (required — one per change type, not collectively):
  ADDITIONS: none — [specific reason inertia holds] / [N proposals listed above]
  REMOVALS: none — [specific reason inertia holds] / [N proposals listed above]
  REPRIORITIZATIONS: none — [specific reason inertia holds] / [N proposals listed above]

Before/after diff (required when proposals exist):

| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| [fill]    | [from Schema A] | [fill] | ADD-N / REMOVE-N / REPRIORITIZE-N |

Phase 8 exit gate:
  [PHASE 8 GATE: PASS — all three action types declared, all evidence from NEW list,
   all Before values from Schema A]
  [PHASE 8 GATE: STOP — describe gap]

---

## Phase 9 — Confirmation gate

Display Phase 5 (inventory), Phase 7 (delta), Phase 8 (proposals), and before/after diff.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop here. Write nothing further until the user replies.

---

## Phase 10 — Apply (triggered by YES or REVISED only)

Write exactly the confirmed changes to strategy.md. Source Before values from Schema A —
do not re-read strategy.md.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Output Format — Pre-Declared Block Schemas with Labeled Field Slots

**Variation axis**: Output format — all structural blocks (Schema A, VERBATIM BLOCK,
SEALED BLOCK, Gate 1, namespace audit, proposals table) are pre-declared as named
templates before any file is read. The VERBATIM BLOCK template pre-prints
`Source dimension:` and `Enforcement note:` as labeled field slots. The model fills
slots, making omission visible as a gap rather than a silent skip.

**Hypothesis**: Pre-printing the VERBATIM BLOCK template with `Enforcement note:` as a
labeled slot (C-28) means the model fills an existing labeled field rather than
constructing the enforcement note from memory. Similarly, pre-printing Gate 1 with
[2a]/[2b]/[2c] labels (C-29) means the sub-condition identifiers exist before the
check runs — the model cannot emit a prose enumeration when the output slots require
individually labeled lines. Schema-first design converts structural requirements into
slot-filling operations.

```
You are running /topic:plan for the topic named in the user's message.

The default outcome is NO CHANGE to strategy.md.

Commit to this output schema before reading any file. Fill every block in
the order shown. Do not replace any labeled field with prose. Do not merge blocks.

---

## Pre-committed output schema

**Schema A — Strategy dimensions (commitment registry)**
| Label | Dimension name | Current strategy position |
|-------|---------------|--------------------------|
| D-1   | [fill]        | [fill]                   |
| D-2   | [fill]        | [fill]                   |
| ...   | ...           | ...                      |
(add one row per strategy dimension found)

**VERBATIM BLOCK (fill after reading strategy.md)**
=== VERBATIM BLOCK ===
"[exact quoted sentence from strategy.md — verbatim, character for character]"
Source dimension: D-N
Enforcement note: A Source dimension field that does not match a D-N label fails this block.
=== END VERBATIM BLOCK ===

**SEALED BLOCK (fill after VERBATIM BLOCK)**
=== SEALED BLOCK ===
Committed dimensions: D-1 through D-N ([count])
Verbatim anchor: [first 10 words of quoted sentence]
Re-read prohibition: strategy.md may not be re-opened until user applies confirmed changes.
SEAL violation: A Before value containing text not present in Schema A at seal time is a
  SEAL violation and must be dropped.
Temporal attestation: Commitment table complete. No signal artifacts read yet.
=== END SEALED BLOCK ===

**Gate 1 — commitment-phase compound verification (fill after SEALED BLOCK)**
  Check [1] Schema A: all D-N rows filled?
    [1]: PASS — [N] rows / FAIL — [describe gap]
  Check [2] VERBATIM BLOCK:
    [2a] Delimiters (=== VERBATIM BLOCK === / === END VERBATIM BLOCK ===) present?
         [2a]: PASS / FAIL
    [2b] Source dimension field present in D-N format matching a Schema A label?
         [2b]: PASS — D-[N] matches Schema A / FAIL — [describe mismatch]
    [2c] Enforcement note present as named, labeled sub-field?
         [2c]: PASS / FAIL
  Check [3] SEALED BLOCK: all required fields present?
    [3]: PASS — [N] fields / FAIL — [describe gap]
  Gate 1: PASS — proceed to Schema B / STOP — fix failing checks, re-run Gate 1

**Schema B — Signal inventory**
| Artifact filename | Artifact date | Classification | Namespace |
|-------------------|---------------|----------------|-----------|
| [fill]            | YYYY-MM-DD    | NEW (date > STRATEGY DATE) or PRIOR | [fill] |

**Schema C — Namespace audit (all 9 rows required)**
| Namespace | Total artifacts | New artifacts | Pressure |
|-----------|----------------|---------------|----------|
| scout     | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| draft     | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| review    | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| flow      | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| trace     | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| prove     | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| listen    | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| program   | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |
| topic     | [N]            | [M]           | HIGH-PRESSURE (M > 0) / INACTIVE |

HIGH-PRESSURE namespaces (new > 0): [list]

**PROPOSAL SCOPE (declare after Schema C; reproduce at Schema F)**
PROPOSAL SCOPE:
  HIGH-pressure namespaces: [list from Schema C]
  Proposals restricted to: HIGH-pressure namespaces only.
  A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.

**Gate 2 — scope check (fill before Schema F)**
  Check: PROPOSAL SCOPE violation condition present as named output category?
  Gate 2: PASS / STOP — add violation condition line before continuing

**Schema F — Proposals (PROPOSAL SCOPE reproduced at this enforcement point)**
PROPOSAL SCOPE (reproduced):
  HIGH-pressure namespaces: [reproduce from above]
  Proposals restricted to: HIGH-pressure namespaces only.
  A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [N] | ADD / REMOVE / REPRIORITIZE | [D-N name] | [NEW filename] | [from Schema A] | [fill] | [specific consequence] |

ADDITIONS: none — [reason] / [N proposals above]
REMOVALS: none — [reason] / [N proposals above]
REPRIORITIZATIONS: none — [reason] / [N proposals above]

**Schema G — Before/after diff (required when Schema F is non-empty)**
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| [fill]    | [from Schema A] | [fill] | ADD-N / REMOVE-N / REPRIORITIZE-N |

---

## Step 1 — Fill Schema A

Read simulations/TOPICS.md to locate the strategy file. Read strategy.md.
Record: STRATEGY DATE: [YYYY-MM-DD]
Fill Schema A with all named strategy dimensions. Assign D-N labels in sequence.
Quote at least one complete sentence from strategy.md to confirm you have read it —
this quote will become the VERBATIM BLOCK content in Step 2.

---

## Step 2 — Fill VERBATIM BLOCK

Copy the most scope-relevant sentence from strategy.md verbatim.
Fill the VERBATIM BLOCK template above exactly as shown.
The Source dimension field must use a D-N label from Schema A.
The Enforcement note field must appear exactly as labeled — not merged with Source dimension.

---

## Step 3 — Fill SEALED BLOCK

Fill the SEALED BLOCK template above. Write the temporal attestation sentence last.
After filling the SEALED BLOCK, do not re-read strategy.md. The commitment is sealed.

---

## Step 4 — Fill Gate 1

Evaluate Check [1], Check [2] with all three sub-conditions ([2a], [2b], [2c]), and
Check [3]. Write each result to the Gate 1 block above. If Gate 1 is STOP, return to
the failing step and fix the gap before proceeding.

---

## Step 5 — Fill Schema B and Schema C

Find every artifact in simulations/ whose filename contains the topic slug.
Fill Schema B (all artifacts, classified NEW or PRIOR).
Fill Schema C (all 9 namespace rows with total and new counts).
List HIGH-PRESSURE namespaces (those with new count > 0).

Gate: all 9 rows present AND HIGH-PRESSURE list written before proceeding.

---

## Step 6 — Read NEW artifacts

Read every artifact classified NEW in Schema B. PRIOR artifacts were available when
strategy.md was written — do not read them.

---

## Step 7 — Delta detection

For each finding from the NEW artifacts:
  Condition 1: artifact date > STRATEGY DATE?
  Condition 2: finding absent from Schema A dimensions?
CONFIRMED NEW = both conditions true.
PRIOR-ONLY = condition 1 true, condition 2 false. Annotate: "PRIOR-ONLY — not a delta."
PRIOR-ONLY may not drive ADD proposals.

---

## Step 8 — Fill PROPOSAL SCOPE and Gate 2

Write PROPOSAL SCOPE using HIGH-PRESSURE namespaces from Schema C.
Fill Gate 2. If STOP: add violation condition line to PROPOSAL SCOPE before continuing.

---

## Step 9 — Fill Schema F and Schema G

At the start of this step, reproduce PROPOSAL SCOPE exactly (the PROPOSAL SCOPE
reproduced line in Schema F).

Build Schema F: proposals restricted to HIGH-pressure namespaces.
Each Before value must come from Schema A — not from re-reading strategy.md.
Write typed null declarations for each of the three change types.
Build Schema G for each Schema F row.

---

## Step 10 — Confirmation gate

Display Schema B, Schema C, Schema F, and Schema G.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop here. Write nothing further until the user replies.

---

## Step 11 — Apply (triggered by YES or REVISED only)

Write exactly the confirmed changes to strategy.md. Source Before values from Schema A.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Phrasing Register — Conversational-Imperative with Inline Enforcement Motivation

**Variation axis**: Phrasing register — instructions are written in direct, conversational
language rather than formal specification style. The reason WHY each labeled field is
required is stated inline at the point where it is first introduced ("Gate 1 will check
[2c] — if the Enforcement note is not labeled, [2c] fails"). This motivation makes
compliance a logical consequence of understanding the gate contract, not an instruction
to memorize.

**Hypothesis**: Explaining the gate's sub-requirement identifier system in plain English
at the moment of field introduction motivates the model to produce the labeled structure
because it understands what a downstream check will look for. Conversational register
reduces the distance between instruction and compliance by removing the need to translate
from specification language to action.

```
You are running /topic:plan. Your goal is to revise the strategy for the topic named
in the user's message — but only if the evidence actually warrants a change.

Start from the default assumption: nothing needs to change. The strategy reflects
considered decisions that have inertia for good reason. Every proposed update must
earn its place by beating that default.

---

## What you will do

1. Read strategy.md and lock down what it currently says — before touching any signals.
2. Scan new signals and detect what is genuinely new versus what was already there
   when the strategy was written.
3. Propose only changes that new signals force — with evidence and a "vs. NO CHANGE"
   case for each.
4. Ask for confirmation before touching any file.

---

## Step 1 — Read strategy.md (do this first, before any signal files)

Find the strategy file: read simulations/TOPICS.md to get the path.
Read strategy.md. Record the STRATEGY DATE (last-modified date):

  STRATEGY DATE: [YYYY-MM-DD]

Now write out all the named dimensions in the strategy, giving each a D-N label:

  D-1: [name] — [one-line summary of what the strategy currently says about this]
  D-2: [name] — [one-line summary]
  ...

This is your commitment registry (Schema A). These are the positions the strategy
is currently committed to. Your proposals will compare against this — not against
whatever strategy.md says when you re-read it during the proposal phase.

---

## Step 2 — Lock in a verbatim quote

Pick one sentence from strategy.md that best captures the core commitment for this
topic. Copy it exactly — character for character.

Write it in this block. The labeled fields (`Source dimension:` and `Enforcement note:`)
must appear exactly as shown — they are not optional commentary:

=== VERBATIM BLOCK ===
"[exact sentence here — copy-paste, do not paraphrase]"
Source dimension: D-N
Enforcement note: A Source dimension field that does not match a D-N label fails this block.
=== END VERBATIM BLOCK ===

Why the labeled fields matter: Gate 1 will run three sub-checks on this block:
  [2a] Are the delimiters present?
  [2b] Is Source dimension in D-N format matching your Step 1 registry?
  [2c] Is the Enforcement note present as a named, labeled sub-field?

If you embed the enforcement note inside the Source dimension line rather than
giving it its own `Enforcement note:` label, sub-check [2c] will fail.
The Source dimension must use a D-N label from your Step 1 list — if it does not,
sub-check [2b] will fail and you can trace the mismatch to the specific registry row.

---

## Step 3 — Seal the commitment

Write this block to record that your reading of strategy.md is complete and locked.
After writing it, do not re-open strategy.md:

=== SEALED BLOCK ===
Committed dimensions: D-1 through D-[N] ([count] total)
Verbatim anchor: [first 10 words of your quoted sentence]
Re-read prohibition: strategy.md may not be re-opened until the user applies
  confirmed changes.
SEAL violation: A Before value in any proposal containing text not present in
  Schema A at seal time is a SEAL violation and must be dropped.
=== END SEALED BLOCK ===

Then write this sentence exactly:
  Commitment table complete. No signal artifacts read yet.

---

## Step 4 — Gate 1: check the commitment artifacts

Before moving to signals, verify the commitment artifacts are complete.
Write each result — the sub-check labels matter for traceability:

  Check [1] Schema A: are all D-N dimension rows written above?
    [1]: PASS / FAIL

  Check [2] VERBATIM BLOCK:
    [2a] Are the === VERBATIM BLOCK === and === END VERBATIM BLOCK === delimiters present?
         [2a]: PASS / FAIL
    [2b] Is the Source dimension field present and using a D-N label from your Step 1 list?
         [2b]: PASS — "Source dimension: D-[N]" matches Step 1 row [N] / FAIL — [describe mismatch]
    [2c] Is the Enforcement note present as its own named, labeled field (not merged into
         the Source dimension line)?
         [2c]: PASS / FAIL

  Check [3] SEALED BLOCK: does it contain all five required fields?
    [3]: PASS / FAIL

  Gate 1 result:
    PASS — all checks passed; proceed to Step 5
    STOP — return to the step where the failure occurred, fix it, then re-run Gate 1

---

## Step 5 — Inventory all signals

Now you can look at signals. List every artifact in simulations/ whose filename
contains the topic slug:

  [filename] | [artifact date] | NEW (date > STRATEGY DATE) or PRIOR | [namespace]

Count by namespace — include every namespace, even ones with zero artifacts:

  scout:   [total] total | [new] new
  draft:   [total] total | [new] new
  review:  [total] total | [new] new
  flow:    [total] total | [new] new
  trace:   [total] total | [new] new
  prove:   [total] total | [new] new
  listen:  [total] total | [new] new
  program: [total] total | [new] new
  topic:   [total] total | [new] new

HIGH-PRESSURE namespaces (new count > 0): [list them]

Only these namespaces can drive proposals — a namespace with no new artifacts carries
no change pressure regardless of how many prior artifacts it has.

---

## Step 6 — Read only NEW artifacts

Read every artifact classified NEW above. PRIOR artifacts were present when strategy.md
was written — they are already baked in. Using them as evidence would mean relitigating
settled decisions.

---

## Step 7 — Delta detection

For each finding from the NEW artifacts, ask two questions:

  1. Does this come from an artifact dated after STRATEGY DATE? (It must — you only
     read NEW artifacts, so yes by definition.)
  2. Is this absent from strategy.md? (Check against your D-N registry in Step 1.)

Both yes = CONFIRMED NEW — this finding can drive a proposal.
Only question 1 yes = PRIOR-ONLY — mark it "PRIOR-ONLY — not a delta" and exclude it
from ADD proposals.

---

## Step 8 — Build proposals (scoped to HIGH-pressure namespaces)

Before building proposals, write this scope block:

PROPOSAL SCOPE:
  HIGH-pressure namespaces: [list from Step 5]
  Proposals restricted to: HIGH-pressure namespaces only.
  A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.

Scope gate: does the PROPOSAL SCOPE block above include the violation condition statement?
  SCOPE GATE: PASS / STOP — add the violation condition line before continuing

Remember: you are not looking for reasons to change. You are checking whether the
evidence forces a change. If it does not, NO CHANGE wins.

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [N] | ADD / REMOVE / REPRIORITIZE | [D-N dimension name] | [NEW filename] | [from D-N row in Step 1] | [proposed] | [specific reason this beats doing nothing] |

Before values must come from your D-N registry in Step 1 — not from re-reading
strategy.md.

For each change type, write the result:
  ADDITIONS: none — [reason] / [N proposals above]
  REMOVALS: none — [reason] / [N proposals above]
  REPRIORITIZATIONS: none — [reason] / [N proposals above]

Before/after diff (include when proposals exist):

| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| [fill]    | [from Step 1] | [fill] | ADD-N / REMOVE-N / REPRIORITIZE-N |

---

## Step 9 — Confirmation gate

Show Step 5 (inventory), Step 7 (deltas), Step 8 (proposals), and the diff.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop. Do not touch any file until the user replies.

---

## Step 10 — Apply (only after YES or REVISED)

Write the confirmed changes to strategy.md. Use Before/After values from Step 8 —
not from a re-read.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Inertia Framing + Role Sequence — Defense Register Before Signals

**Variation axes combined**: Inertia framing (NO CHANGE as opening premise; defense
register for each D-N dimension before reading signals) + Role sequence (dimensions
extracted and defended before the verbatim quote is anchored; the defense register
establishes the D-N label set that both Schema A and the VERBATIM BLOCK Source field
must reference).

**Hypothesis**: A pre-signal defense register (recording the strongest keep-unchanged
argument for each D-N dimension before reading any signal) creates a fair adversarial
structure: each new signal must defeat a named defense position, not just be noticed
as interesting. When the defense register is produced before the verbatim quote is
anchored, the D-N label space is already fully defined — the Source dimension field in
the VERBATIM BLOCK must draw from a pre-confirmed registry, making [2b] failures
traceable to the register rather than requiring inference about what D-N means.
Inertia framing at every gate (proposal gate, confirmation gate) keeps the null
hypothesis active throughout.

```
You are running /topic:plan for the topic named in the user's message.

---

## Opening premise — the null hypothesis

The null hypothesis is: strategy.md is correct and should not change.
Every proposal you make is a specific claim that the null hypothesis is wrong
about something. Claims require evidence from NEW signals only.
The burden of proof rests on change, not on stability.
The default outcome is NO CHANGE to strategy.md.

---

## Step 1 — Read strategy.md and register all dimensions

Read simulations/TOPICS.md to locate the strategy file. Read strategy.md.
Record: STRATEGY DATE: [YYYY-MM-DD]

List all named strategy dimensions, assigning D-N labels:

  D-1: [dimension name] — [current strategy position]
  D-2: [dimension name] — [current strategy position]
  ...

This is Schema A — the locked representation of the strategy's current positions.

---

## Step 2 — Pre-signal defense register

Before reading any signal artifact, record the strongest argument for keeping each
D-N dimension unchanged. This is the null hypothesis arguing on its own behalf.

| Dimension (D-N label) | Current position (from Schema A) | Strongest keep-unchanged argument | What NEW signal evidence would invalidate this |
|-----------------------|----------------------------------|----------------------------------|-----------------------------------------------|
| [D-N name]            | [from Schema A]                  | [1-2 sentences]                  | [specific signal type or finding required]    |

Every D-N row from Schema A must appear. Complete this table before writing the
VERBATIM BLOCK or reading any signal file.

---

## Step 3 — Verbatim anchor with labeled fields

Select the strategy sentence that most directly captures the topic's core commitment.
Copy it verbatim. Write it in the VERBATIM BLOCK. The labeled fields are required:

=== VERBATIM BLOCK ===
"[exact quoted sentence from strategy.md]"
Source dimension: D-N
Enforcement note: A Source dimension field that does not match a D-N label fails this block.
=== END VERBATIM BLOCK ===

The Source dimension field must use a D-N label from Schema A (Step 1).
The Enforcement note must appear as a named, labeled field — not as inline commentary.
Both fields must be present for Gate 1 Check [2] to pass.

---

## Step 4 — Seal the commitment

=== SEALED BLOCK ===
Committed dimensions: D-1 through D-N ([count])
Verbatim anchor: [first 10 words of quoted sentence]
Re-read prohibition: strategy.md may not be re-opened until user applies confirmed changes.
SEAL violation: A Before value containing text not present in Schema A at seal time is a
  SEAL violation and must be dropped.
=== END SEALED BLOCK ===

Write: Commitment table complete. No signal artifacts read yet.

---

## Step 5 — Gate 1 (commitment-phase compound check)

  Check [1] Schema A: all D-N rows filled?
    [1]: PASS — [N] rows / FAIL — [describe gap]

  Check [2] VERBATIM BLOCK:
    [2a] Delimiters present?
         [2a]: PASS / FAIL
    [2b] Source dimension in D-N format matching a D-N label in Schema A (Step 1)?
         [2b]: PASS — D-[N] matches Step 1 row [N] / FAIL — [describe mismatch]
    [2c] Enforcement note present as named, labeled sub-field (not merged into Source line)?
         [2c]: PASS / FAIL

  Check [3] SEALED BLOCK: all required fields present?
    [3]: PASS — [N] fields / FAIL — [describe gap]

  [GATE 1: PASS — proceed to Step 6 / STOP — fix failing checks, re-run Gate 1]

---

## Step 6 — Signal inventory

List every artifact in simulations/ whose filename contains the topic slug:

  [artifact-filename] | [artifact-date] | NEW (date > STRATEGY DATE) or PRIOR | [namespace]

Assess all 9 namespaces — include every namespace, 0 total | 0 new for absent ones:

  scout:   [total] total | [new] new
  draft:   [total] total | [new] new
  review:  [total] total | [new] new
  flow:    [total] total | [new] new
  trace:   [total] total | [new] new
  prove:   [total] total | [new] new
  listen:  [total] total | [new] new
  program: [total] total | [new] new
  topic:   [total] total | [new] new

HIGH-PRESSURE namespaces (new count > 0): [list]

---

## Step 7 — Read NEW artifacts and challenge the defense register

Read every artifact classified NEW above. PRIOR artifacts do not constitute new evidence.

For each NEW artifact, identify which Step 2 defense position it challenges:

| NEW Artifact | D-N dimension challenged | Step 2 defense argument | Assessment |
|--------------|--------------------------|-------------------------|------------|
| [filename]   | [D-N label]              | [summary from Step 2]   | VALIDATES / WEAKENS / INVALIDATES |

If a NEW artifact introduces a dimension not in Schema A:
| [filename] | NEW DIMENSION | none registered | CANDIDATE ADDITION |

---

## Step 8 — Delta detection

For each Step 7 finding:
  Condition 1: from an artifact dated after STRATEGY DATE?
  Condition 2: absent from strategy.md (not in Schema A)?

CONFIRMED NEW = both conditions true.
PRIOR-ONLY = condition 1 true, condition 2 false. Annotate: "PRIOR-ONLY — not a delta."
PRIOR-ONLY may not drive ADD proposals.

---

## Step 9 — Proposals (the case for change)

Write the PROPOSAL SCOPE block:

PROPOSAL SCOPE:
  HIGH-pressure namespaces: [list from Step 6]
  Proposals restricted to: HIGH-pressure namespaces only.
  A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.

Scope gate:
  Check: PROPOSAL SCOPE violation condition present as named output category?
  [SCOPE GATE: PASS / STOP — add violation condition before continuing]

For Step 7 findings where Assessment is WEAKENS or INVALIDATES, propose a change.
For CANDIDATE ADDITIONS, evaluate whether the defense register is defeated.

Reminder: NO CHANGE is the default verdict. "vs. NO CHANGE" must name the specific
defense argument from Step 2 that this finding defeats.

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [N] | ADD / REMOVE / REPRIORITIZE | [D-N name] | [NEW filename] | [from Schema A] | [proposed] | [Step 2 defense argument defeated] |

Before values must come from Schema A — not from a re-read of strategy.md.

Typed null declarations:
  ADDITIONS: none — Step 2 defenses held for all ADD candidates / [N proposals above]
  REMOVALS: none — Step 2 defenses held for all REMOVE candidates / [N proposals above]
  REPRIORITIZATIONS: none — Step 2 defenses held for all REPRIORITIZE candidates / [N proposals above]

Before/after diff (required when proposals exist):

| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| [fill]    | [from Schema A] | [fill] | ADD-N / REMOVE-N / REPRIORITIZE-N |

---

## Step 10 — Confirmation gate

Display Step 6 (inventory), Step 7 (challenge assessment), Step 8 (delta), Step 9
(proposals), and before/after diff.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
The default outcome is NO CHANGE. The proposals above are the case against that default.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop. Write nothing until the user replies.

---

## Step 11 — Apply (triggered by YES or REVISED)

Write exactly the confirmed changes. Source Before values from Schema A.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Combined — Upfront Structural Contract + Pre-Declared Schemas + Lifecycle Gates + Defense Register

**Variation axes combined**: Output format (pre-declared schemas with labeled field
slots, V-02) + Lifecycle emphasis (named phases with explicit exit gates, V-01) +
Role sequence + Inertia framing (defense register + NO CHANGE as default, V-04) +
Upfront structural declaration naming all gates and contract elements before execution.

**Hypothesis**: Declaring the complete structural contract upfront — naming all gates,
labeling all block templates, and specifying all sub-condition identifiers before any
phase runs — gives the model an auditable reference it can verify its output against at
any point. Pre-declared schemas with labeled field slots (VERBATIM BLOCK, SEALED BLOCK)
convert C-28 compliance into slot-filling. Explicit phase exit gates with [2a][2b][2c]
labels in the gate structure convert C-29 compliance into a named check sequence.
The defense register (V-04 role sequence) makes inertia structural rather than
rhetorical. Together these mechanisms make every rubric criterion an observable output
structure rather than an implicit instruction.

```
You are running /topic:plan for the topic named in the user's message.

══════════════════════════════════════════════════════════════════════
SKILL EXECUTION CONTRACT
══════════════════════════════════════════════════════════════════════

This block declares the complete structural contract. All templates, gate conditions,
and scope constraints are specified here. The model may audit its execution against
this block at any point during execution.

DEFAULT OUTCOME: NO CHANGE to strategy.md. Every proposal is a specific claim against
this default. The burden of proof rests on change.

PHASE SEQUENCE:
  Phase 1: Commitment registry (Schema A + VERBATIM BLOCK + SEALED BLOCK)
  Phase 2: Pre-signal defense register
  Phase 3: Gate 1 (commitment-phase compound verification)
  Phase 4: Signal inventory (Schema B + Schema C + HIGH-PRESSURE list)
  Phase 5: Read NEW artifacts + challenge assessment
  Phase 6: Delta detection
  Phase 7: Proposals (PROPOSAL SCOPE + Gate 2 + Schema F + Schema G)
  Phase 8: Confirmation gate
  Phase 9: Apply (post-confirmation only)

GATE CONTRACTS:

  Gate 1 — commitment-phase compound gate (runs at end of Phase 1 / start of Phase 3):
    Check [1]: Schema A — all D-N rows filled
    Check [2]: VERBATIM BLOCK —
      [2a] Delimiters (=== VERBATIM BLOCK === / === END VERBATIM BLOCK ===) present
      [2b] Source dimension in D-N format matching a Schema A label
      [2c] Enforcement note present as named, labeled sub-field
    Check [3]: SEALED BLOCK — all required fields present
    Result: PASS (all checks pass) / STOP (any check fails — return to failing phase)

  Gate 2 — scope gate (runs at start of Phase 7 proposal step):
    Check: PROPOSAL SCOPE violation condition present as named output category
    Result: PASS / STOP — add violation condition line before continuing

BLOCK TEMPLATES (fill during Phase 1):

  VERBATIM BLOCK template:
  =================================
  === VERBATIM BLOCK ===
  "[exact quoted sentence]"
  Source dimension: D-N
  Enforcement note: A Source dimension field that does not match a D-N label fails this block.
  === END VERBATIM BLOCK ===
  =================================

  SEALED BLOCK template:
  =================================
  === SEALED BLOCK ===
  Committed dimensions: D-1 through D-N ([count])
  Verbatim anchor: [first 10 words]
  Re-read prohibition: strategy.md may not be re-opened until user applies confirmed changes.
  SEAL violation: A Before value containing text not present in Schema A at seal time is a
    SEAL violation and must be dropped.
  === END SEALED BLOCK ===
  Temporal attestation: Commitment table complete. No signal artifacts read yet.
  =================================

PROPOSAL SCOPE template (declare at Phase 7; reproduce at proposal sub-step):
  =================================
  PROPOSAL SCOPE:
    HIGH-pressure namespaces: [list namespaces from Schema C with new count > 0]
    Proposals restricted to: HIGH-pressure namespaces only.
    A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.
  =================================

PRE-SCAN COMMITMENT RULE: Schema A, VERBATIM BLOCK, and SEALED BLOCK must all be written
and Gate 1 must PASS before any signal artifact is read. A proposal's Before value must
come from Schema A — not from a re-read of strategy.md during or after the proposal phase.

══════════════════════════════════════════════════════════════════════
PHASE 1 — Commitment registry
══════════════════════════════════════════════════════════════════════

Read simulations/TOPICS.md to locate the strategy file. Read strategy.md.
Record: STRATEGY DATE: [YYYY-MM-DD]

**Schema A — Strategy dimensions**
| Label | Dimension name | Current strategy position |
|-------|---------------|--------------------------|
| D-1   | [fill]        | [fill]                   |
| D-2   | [fill]        | [fill]                   |
| ...   | ...           | ...                      |

Fill VERBATIM BLOCK (use template from Skill Execution Contract):
=== VERBATIM BLOCK ===
"[exact quoted sentence from strategy.md]"
Source dimension: D-N
Enforcement note: A Source dimension field that does not match a D-N label fails this block.
=== END VERBATIM BLOCK ===

Fill SEALED BLOCK (use template from Skill Execution Contract):
=== SEALED BLOCK ===
Committed dimensions: D-1 through D-N ([count])
Verbatim anchor: [first 10 words of quoted sentence]
Re-read prohibition: strategy.md may not be re-opened until user applies confirmed changes.
SEAL violation: A Before value containing text not present in Schema A at seal time is a
  SEAL violation and must be dropped.
=== END SEALED BLOCK ===
Temporal attestation: Commitment table complete. No signal artifacts read yet.

Phase 1 exit gate: Schema A has at least one D-N row, VERBATIM BLOCK filled, SEALED BLOCK filled,
  temporal attestation written.
  [PHASE 1 EXIT: PASS / STOP — describe gap]

══════════════════════════════════════════════════════════════════════
PHASE 2 — Pre-signal defense register
══════════════════════════════════════════════════════════════════════

Before reading any signal artifact, record the strongest argument for keeping each
D-N dimension unchanged. Every Schema A dimension must appear:

| D-N label | Current position | Strongest keep-unchanged argument | What NEW evidence would invalidate |
|-----------|-----------------|----------------------------------|-----------------------------------|
| [D-N name]| [from Schema A] | [1-2 sentences]                  | [specific signal type]            |

Phase 2 exit gate: all D-N dimensions in defense register.
  [PHASE 2 EXIT: PASS — N dimensions registered / STOP]

══════════════════════════════════════════════════════════════════════
PHASE 3 — Gate 1 (commitment-phase compound verification)
══════════════════════════════════════════════════════════════════════

Run Gate 1 per the Gate Contracts in the Skill Execution Contract:

  Check [1] Schema A: all D-N rows filled?
    [1]: PASS — [N] rows / FAIL — [describe gap]

  Check [2] VERBATIM BLOCK:
    [2a] Delimiters (=== VERBATIM BLOCK === / === END VERBATIM BLOCK ===) present?
         [2a]: PASS / FAIL
    [2b] Source dimension in D-N format matching a Schema A label?
         [2b]: PASS — D-[N] matches Schema A row [N] / FAIL — [describe mismatch]
    [2c] Enforcement note present as named, labeled sub-field?
         [2c]: PASS / FAIL

  Check [3] SEALED BLOCK: all required fields present?
    [3]: PASS — [N] fields / FAIL — [describe gap]

  [GATE 1: PASS — all checks passed, proceed to Phase 4]
  [GATE 1: STOP — return to Phase 1, fix failing checks, re-run Phase 3]

══════════════════════════════════════════════════════════════════════
PHASE 4 — Signal inventory
══════════════════════════════════════════════════════════════════════

**Schema B — Signal inventory**
| Artifact filename | Artifact date | Classification | Namespace |
|-------------------|---------------|----------------|-----------|
| [fill]            | YYYY-MM-DD    | NEW (date > STRATEGY DATE) or PRIOR | [fill] |

**Schema C — Namespace audit (all 9 rows required)**
| Namespace | Total artifacts | New artifacts | Pressure |
|-----------|----------------|---------------|----------|
| scout     | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| draft     | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| review    | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| flow      | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| trace     | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| prove     | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| listen    | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| program   | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |
| topic     | [N]            | [M]           | HIGH-PRESSURE / INACTIVE |

HIGH-PRESSURE namespaces (new > 0): [list]

Phase 4 exit gate: all 9 Schema C rows present, HIGH-PRESSURE list written.
  [PHASE 4 EXIT: PASS / STOP]

══════════════════════════════════════════════════════════════════════
PHASE 5 — Read NEW artifacts + challenge assessment
══════════════════════════════════════════════════════════════════════

Read every artifact classified NEW in Schema B. PRIOR artifacts are already incorporated.

For each NEW artifact, identify which Phase 2 defense position it challenges:

| NEW Artifact | D-N dimension | Phase 2 defense argument | Assessment |
|--------------|---------------|--------------------------|------------|
| [filename]   | [D-N label]   | [summary from Phase 2]   | VALIDATES / WEAKENS / INVALIDATES |

NEW dimensions not in Schema A:
| [filename] | NEW DIMENSION | none registered | CANDIDATE ADDITION |

Phase 5 exit gate: all NEW artifacts assessed against Phase 2 register.
  [PHASE 5 EXIT: PASS / STOP]

══════════════════════════════════════════════════════════════════════
PHASE 6 — Delta detection
══════════════════════════════════════════════════════════════════════

Apply the two-condition novelty gate to each Phase 5 finding:
  Condition 1: from an artifact dated after STRATEGY DATE?
  Condition 2: absent from strategy.md (not in Schema A)?

CONFIRMED NEW = both true. PRIOR-ONLY = only condition 1 true.
Annotate PRIOR-ONLY: "PRIOR-ONLY — not a delta." PRIOR-ONLY may not drive ADD proposals.

══════════════════════════════════════════════════════════════════════
PHASE 7 — Proposals
══════════════════════════════════════════════════════════════════════

Declare PROPOSAL SCOPE (use template from Skill Execution Contract):

PROPOSAL SCOPE:
  HIGH-pressure namespaces: [list from Schema C]
  Proposals restricted to: HIGH-pressure namespaces only.
  A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.

Run Gate 2:
  Check: PROPOSAL SCOPE violation condition present as named output category?
  [GATE 2: PASS / STOP — add violation condition line before continuing]

Reproduce PROPOSAL SCOPE at this enforcement point:

PROPOSAL SCOPE (reproduced at proposal step):
  HIGH-pressure namespaces: [reproduce from above]
  Proposals restricted to: HIGH-pressure namespaces only.
  A proposal row citing any excluded namespace is a SCOPE violation and must be dropped.

**Schema F — Proposals**
For Phase 5 findings where Assessment is WEAKENS or INVALIDATES, propose a change.
For CANDIDATE ADDITIONS, evaluate whether Phase 2 defense is defeated.
Default: NO CHANGE. "vs. NO CHANGE" must name the Phase 2 defense argument defeated.

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [N] | ADD / REMOVE / REPRIORITIZE | [D-N name] | [NEW filename] | [from Schema A] | [proposed] | [Phase 2 defense argument defeated] |

Before values must come from Schema A — not from re-reading strategy.md.

Typed null declarations (one per change type):
  ADDITIONS: none — Phase 2 defenses held for all ADD candidates / [N proposals above]
  REMOVALS: none — Phase 2 defenses held for all REMOVE candidates / [N proposals above]
  REPRIORITIZATIONS: none — Phase 2 defenses held for all REPRIORITIZE candidates / [N proposals above]

**Schema G — Before/after diff (required when Schema F non-empty)**
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| [fill]    | [from Schema A] | [fill] | ADD-N / REMOVE-N / REPRIORITIZE-N |

Phase 7 exit gate: all three action types declared, all evidence from Schema B NEW list,
  all Before values from Schema A, PROPOSAL SCOPE reproduced.
  [PHASE 7 EXIT: PASS / STOP]

══════════════════════════════════════════════════════════════════════
PHASE 8 — Confirmation gate
══════════════════════════════════════════════════════════════════════

Display Schema B, Schema C, Schema F, and Schema G.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
The default outcome is NO CHANGE. The proposals above are the case for change.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to apply
custom version
---

Stop. Write nothing further until the user replies.

══════════════════════════════════════════════════════════════════════
PHASE 9 — Apply (triggered by YES or REVISED only)
══════════════════════════════════════════════════════════════════════

Apply confirmed changes to strategy.md. Source Before values from Schema A.
Do not re-read strategy.md to populate Before values.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Round 8 Variation Summary

| Variation | Primary axis | C-28 mechanism | C-29 mechanism | Inertia mechanism |
|-----------|-------------|----------------|----------------|-------------------|
| V-01 | Lifecycle emphasis | VERBATIM BLOCK template introduced in Phase 2 with `Enforcement note:` labeled field | Gate 1 is dedicated Phase 4; each [2x] check produces its own output line | Phase 8 exit gate; typed null declarations |
| V-02 | Output format | VERBATIM BLOCK pre-declared as schema template; `Enforcement note:` is a pre-printed field slot | Gate 1 pre-declared with [2a][2b][2c] as named slot lines | Schema F includes typed null slots; confirmation gate |
| V-03 | Phrasing register | Inline explanation at Step 2 ("Gate will check [2c] — if not labeled, [2c] fails") | Step 4 shows sub-checks in natural language with [2x] labels and explanation | "Not looking for reasons to change" framing in Step 8 |
| V-04 | Inertia framing + role sequence | VERBATIM BLOCK introduced in Step 3 after defense register establishes D-N label space | Gate 1 in Step 5 with [2a][2b][2c] sub-conditions | Defense register in Step 2; "vs. NO CHANGE = defense defeated" per proposal |
| V-05 | Full combination | VERBATIM BLOCK template in Skill Execution Contract; Phase 1 fills pre-declared slots | Gate 1 contract declared upfront with [2a][2b][2c]; Phase 3 executes against declared contract | Defense register Phase 2; NO CHANGE framing in contract + confirmation gate |

**Predicted Round 8 discriminators for Round 9:**

1. **Gate 1 sub-condition failure reporting specificity** — When [2b] fails (Source dimension
   mismatch), does the output name the specific D-N label that was provided vs. the D-N label
   that would have matched? Precise failure reporting requires the commitment registry to be
   cross-referenced at check time, not just declared.

2. **Commitment registry completeness under sparse strategy.md** — When strategy.md has only
   one or two named dimensions, does Schema A capture the full implied scope or only the
   explicitly labeled sections? The D-N registry should cover both explicit dimension names
   and implied structural commitments (e.g., sequencing decisions not labeled as dimensions).

```json
{
  "round": 8,
  "track": "commitment-phase",
  "rubric_version": "v8",
  "max_composite": 111,
  "formula": "60 + (rec_passed * 10) + asp_passed",
  "new_criteria": ["C-28", "C-29"],
  "all_variations_satisfy_C28": true,
  "all_variations_satisfy_C29": true,
  "primary_discriminating_axis": "how C-28 and C-29 are enforced structurally vs instructionally",
  "predicted_round_9_discriminators": [
    "Gate 1 sub-condition failure reporting specificity: does [2b] failure name the specific D-N mismatch?",
    "Commitment registry completeness: does Schema A capture implied structural commitments, not only explicitly labeled dimensions?"
  ]
}
```
