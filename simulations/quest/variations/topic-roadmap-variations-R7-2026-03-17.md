I now have everything. Let me write the 5 complete variations:

---

## /quest:variate — topic-roadmap (Round 7)

**Skill:** topic-plan (signal strategy revision)
**Rubric:** v7 (C-01–C-18; C-17 bias labels, C-18 WITHDRAW now formalized)
**Prior round best:** V-02 scored 100 (table-first), V-01 scored 99 (inertia framing, missed C-16)

**Variation axis assignments:**

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | Inertia framing | Positioning inertia as explicit competitor throughout every phase improves C-01 reliability and creates coherent epistemic posture |
| V-02 | Output format (table-first) | Committing to table schema before execution makes classification errors structurally harder to commit than prose-mixed output |
| V-03 | Phrasing register (descriptive) | "What this phase does" framing reduces brittleness vs imperative commands while preserving structural requirements |
| V-04 | V-01 + V-02 | Inertia-as-competitor framing + table-first are synergistic: tables make the competition visible at every decision cell |
| V-05 | All axes + lifecycle emphasis | Explicit phase entry/exit conditions + bias labels at every guard = maximum structural resistance to all six identified failure modes |

---

## V-01 — Inertia Framing Prominent

**Axis:** Inertia framing
**Hypothesis:** Positioning inertia as the primary competitor — not a process rule but the entity that wins by default — creates a fundamentally different epistemic posture. Every section becomes a "case against inertia" rather than a "list of changes." This eliminates the cognitive default toward action that degrades C-01.

```
You are running /topic:plan.

Default outcome: strategy.md unchanged.
Inertia is not a fallback — it is the primary outcome and the entity
that must be defeated. A zero-proposal run is a complete, valid execution.

---

## INERTIA COMPETITOR DECLARATION

Before this skill opens any file, commit to the following:

Inertia represents the position that strategy.md is correct as written.
Inertia wins unless a NEW signal artifact provides evidence that a
specific dimension is wrong, incomplete, or stale. Inertia does not
lose to intuition, volume of signals, or elapsed time.

The burden of proof rests on change. This declaration governs every
section below. It is not overridden by any step.

---

## Phase 1 — Pre-Signal Defense Register
Bias blocked: anchor bias — defenses written before signals are read
cannot be contaminated by signal vocabulary. A defense written after
reading signals rationalizes evidence rather than declares prior belief.

Read `simulations/TOPICS.md`. Identify the topic's active strategy
dimensions. Do NOT read strategy.md or any signal file yet.

For each dimension, state the best argument for keeping it unchanged
and what evidence would defeat that argument:

| Dimension | Best reason to keep unchanged | What would defeat this defense |
|-----------|------------------------------|--------------------------------|

Null (if no dimensions identifiable from TOPICS.md entry alone):
"DEFENSE REGISTER: null — no active dimensions identifiable pre-read.
Inertia register empty."

---

## Phase 2 — Signal Inventory
Bias blocked: post-hoc rationalization — cataloguing evidence before
the strategy frame is open produces a vocabulary-independent record.
Once strategy.md is read, every artifact gets unconsciously evaluated
against its language.

Glob `simulations/` for all artifacts matching the topic slug. Do NOT
read strategy.md yet.

| Artifact filename | Date | Namespace | Summary (1 line) |
|------------------|------|-----------|------------------|

All 9 namespaces must appear in the table:
scout / draft / review / flow / trace / prove / listen / program / topic
A namespace with zero artifacts: emit one null row for it.

**SIGNAL READ-LOCK**: After this table is written, signal files may not
be re-read. The inventory above is the fixed evidence record.
Bias blocked by this lock: confirmation bias — post-lock re-reading
selects details that fit what strategy.md says.

---

## Phase 3 — Read Strategy
Bias blocked: vocabulary contamination — reading strategy last means
the inventory is classified against dates and content, not strategy
vocabulary. The evidence record is already fixed.

Read strategy.md. Record:
- Strategy date (required for NEW/PRIOR split — name it explicitly)
- Goal statement (verbatim)
- Every planned signal entry by namespace

---

## Phase 4 — Delta Classification

NEW = artifact date > strategy date.
PRIOR = artifact date <= strategy date.
Only NEW artifacts are eligible to advance proposals.

For each NEW artifact, classify its relationship to the strategy:
- CONFIRMED: validates an existing assumption
- EXPANDED: extends an existing assumption to broader scope
- UNEXPECTED: reveals a dimension the strategy did not address
- CHALLENGED: contradicts an existing assumption

| Finding ID | NEW artifact | Delta category | What understanding changed |
|------------|-------------|---------------|---------------------------|

All four category null declarations are required (type-labeled):
"CONFIRMED: none — no NEW artifacts confirm existing assumptions."
"EXPANDED: none — no NEW artifacts expand existing assumptions."
"UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."
"CHALLENGED: none — no NEW artifacts challenge existing strategy."

---

## Phase 5 — Defeat Assessment

This is the inertia-defeat checkpoint. Each Phase 1 defense meets the
delta evidence here. Inertia can only be defeated at this step —
a proposal for a HOLDS dimension is structurally invalid.

For each Phase 1 dimension, evaluate against NEW delta findings:

| Dimension | Phase 1 defense | Defeating signal | Verdict | Consequence if unchanged |
|-----------|----------------|-----------------|---------|------------------------|

Verdict: DEFEATED (signal overcomes pre-registered defense) or
HOLDS (defense survives; no proposal generated for this dimension).

Null: "DEFEAT ASSESSMENT: null — all defenses hold. Inertia wins."

If all verdicts are HOLDS:
Emit: "NULL_DELTA: inertia holds for all dimensions.
strategy.md unchanged. Null path complete."
Stop. Do not open Phase 6.

---

## Phase 6 — Change Proposals

[INERTIA-GATE: This phase runs only for DEFEATED dimensions.
Inertia wins for all HOLDS dimensions and their rows get NO CHANGE.]

All 9 namespaces must have a row — silence is not a null declaration.
DEFEATED dimensions: ADD / REMOVE / REPRIORITIZE with full columns.
HOLDS dimensions: NO CHANGE; Defense column explains sufficiency.

Additions:
| # | Dimension | Before | After | Evidence | Confidence | Consequence if unchanged | Bias blocked by guard |
|---|-----------|--------|-------|----------|------------|--------------------------|----------------------|

Removals and Reprioritizations:
| # | Action | Dimension | Before | After | Evidence | Confidence | Consequence if unchanged | Bias blocked by guard |
|---|--------|-----------|--------|-------|----------|------------|--------------------------|----------------------|

Confidence: HIGH (two+ independent NEW artifacts) / MEDIUM (one NEW
artifact) / LOW (inference from delta finding).

"Bias blocked by guard": name the Phase 1 or Phase 2 guard that
protected this dimension's row from spurious revision.

Null per type (all three required, type-labeled):
"ADDITIONS: none — inertia holds for all candidate additions."
"REMOVALS: none — inertia holds."
"REPRIORITIZATIONS: none — inertia holds."

---

## Phase 7 — Confirmation Gate

STOP. Do not modify strategy.md.
Present the complete Phase 6 tables.

---
AWAITING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply options:
YES — apply all proposals
NO — keep strategy.md unchanged
REVISED + edited table — apply custom version; re-present for final YES/NO
WITHDRAW [#] — row-level removal: named proposals are dropped;
  remaining proposals apply on YES. WITHDRAW is NOT NO (which rejects
  all) and NOT REVISED (which requires a re-submitted table).
  WITHDRAW [2, 4] removes rows 2 and 4; remaining rows apply.
---

Stop. Write nothing further until the user replies.

---

## Phase 8 — Apply (triggered by YES, WITHDRAW-then-YES, or REVISED-then-YES)

Write exactly the confirmed (non-withdrawn) changes to strategy.md.
No re-evaluation. No changes outside the confirmed set.

Diff summary:
| Proposal # | Applied | Change summary |
|------------|---------|----------------|

On YES or WITHDRAW-then-YES:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
Null path did not complete — changes applied."

On NO:
Emit: | — | NO | strategy.md unchanged |
"strategy.md unchanged. Null path complete."
```

---

## V-02 — Output Format Table-First

**Axis:** Output format (table-first structural enforcement)
**Hypothesis:** Committing to the complete table schema before opening any file makes every classification decision auditable. Prose allows errors to hide in narrative; a table enforces that every artifact gets an explicit Status cell. This closes the "prose-burial" failure mode for C-02 and C-13.

```
You are running /topic:plan — signal strategy revision.

strategy.md unchanged is the default outcome. Change requires defeating
inertia with evidence from NEW signal artifacts. A zero-proposal run is
a complete, valid execution.

---

## Output Schema Commitment

Commit to the following table structures before reading any file.
No prose substitutes. No table merges. Column names are fixed.

Table T-1: Defense Register
| Dimension | Best reason to keep unchanged | What would defeat this |

Table T-2: Signal Inventory
| Filename | Date | Namespace | Summary (1 line) | Status |

Table T-3: Strategy Extract
| Field | Value |

Table T-4: Delta Classification (four subtables — one per category)
| Finding ID | Artifact | Category | What understanding changed |

Table T-5: Defeat Assessment
| Dimension | T-1 defense | Defeating signal | Verdict | Consequence if unchanged |

Table T-6: Proposals
| # | Action | Dimension | Before | After | Evidence |
    Confidence | Consequence if unchanged | Bias blocked |

Table T-7: Diff Output (on apply)
| Proposal # | Applied | Change summary |

Schema is fixed. Proceed.

---

## Step 1 — Defense Register
Bias blocked: anchor bias.

Read TOPICS.md. Identify topic dimensions. Do NOT read strategy.md.
Populate T-1. One row per active dimension.
Null: "T-1: null — no dimensions identifiable from TOPICS.md entry alone."

---

## Step 2 — Signal Inventory
Bias blocked: post-hoc rationalization.

Glob simulations/ for topic artifacts. Do NOT read strategy.md yet.
Populate T-2 columns: Filename, Date, Namespace, Summary. Leave Status blank.
All 9 namespaces required (scout / draft / review / flow / trace /
prove / listen / program / topic). Null row for empty namespaces.

**SIGNAL READ-LOCK: After T-2 is written, signal files may not be re-read.**
Bias blocked by lock: confirmation bias.

---

## Step 3 — Read Strategy

Read strategy.md. Populate T-3:
| Field | Value |
| Strategy date | [required — drives NEW/PRIOR split in Step 4] |
| Goal | [verbatim] |
| Planned signals | [by namespace] |

---

## Step 4 — Delta Classification

NEW = Filename date > strategy date. PRIOR = date <= strategy date.
Fill T-2 Status column.
Populate four subtables of T-4:

T-4a CONFIRMED: NEW artifact validates existing assumption.
T-4b EXPANDED: NEW artifact extends existing assumption.
T-4c UNEXPECTED: NEW artifact reveals uncovered dimension.
T-4d CHALLENGED: NEW artifact contradicts existing assumption.

All four category nulls required (type-labeled):
"CONFIRMED: none." / "EXPANDED: none." / "UNEXPECTED: none." /
"CHALLENGED: none."

---

## Step 5 — Defeat Assessment
Bias blocked: motivated reasoning.

For each T-1 dimension, test against T-4 findings.
Populate T-5.
DEFEATED: dimension advances to T-6.
HOLDS: emit NO CHANGE row in T-6 with defense explanation.

NULL_DELTA stop condition:
If all T-5 verdicts are HOLDS: emit structured block below and stop.

+------------------------------------------------------------------+
| NULL_DELTA                                                       |
| Type: NULL_DELTA                                                 |
| All defenses hold. Inertia wins.                                 |
| strategy.md unchanged. Null path complete.                       |
+------------------------------------------------------------------+

Do not proceed to Step 6.

---

## Step 6 — Change Proposals

Populate T-6. All 9 namespaces must appear — silence is not a null
declaration. A namespace with no DEFEATED dimensions gets NO CHANGE.

Action values: ADD / REMOVE / REPRIORITIZE / NO CHANGE
Confidence: HIGH / MEDIUM / LOW
"Bias blocked" column: name the guard (T-1 pre-registration or
T-2 read-lock) that protected this dimension from spurious revision.

NO CHANGE row Defense: explain why existing strategy is sufficient
given the NEW signals for that namespace.
"No new signals" is only valid if the namespace had zero NEW artifacts.

Null per type (type-labeled, all three required):
"ADDITIONS: none — inertia holds."
"REMOVALS: none — inertia holds."
"REPRIORITIZATIONS: none — inertia holds."

---

## Step 7 — Confirmation Gate

STOP. Present T-6.

---
AWAITING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

YES — apply all; populate T-7; emit count.
NO — emit T-7: | — | NO | strategy.md unchanged |
     emit "Null path complete."
REVISED + edited T-6 — incorporate edits; re-present T-6 for YES/NO.
WITHDRAW [#] — row-level removal. Names specific proposal rows to drop.
  Remaining rows apply on YES. WITHDRAW [1,3] removes rows 1 and 3.
  Distinct from NO (rejects all) — WITHDRAW preserves the remainder.
  Distinct from REVISED (requires re-submitted table) — WITHDRAW needs
  no re-submission; re-present trimmed T-6, then YES applies remainder.
---

Do not write anything further until the user replies.

---

## Step 8 — Apply (YES / WITHDRAW-then-YES / REVISED-then-YES)

Write exactly the confirmed changes to strategy.md.
Populate T-7.
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
Null path did not complete — changes applied."

On NO: T-7 row | — | NO | strategy.md unchanged |
"strategy.md unchanged. Null path complete."
```

---

## V-03 — Phrasing Register: Descriptive

**Axis:** Phrasing register (conversational / descriptive)
**Hypothesis:** Describing what each phase "is doing" and why — rather than issuing imperative commands — reduces brittleness in instruction-following while preserving structural requirements. The model is more likely to internalize a constraint explained than one merely commanded.

```
You are running /topic:plan.

This skill examines whether new signal evidence justifies revising a
Signal topic's strategy document. The default answer is no. The skill
does not revise strategy.md to demonstrate activity — it revises only
when specific evidence defeats a pre-registered inertia defense.

The skill works in seven phases. Each phase has one job and one output.
Phases run in order. No phase opens until the previous one is complete.

---

## The Inertia Prior

strategy.md unchanged is the correct and complete outcome of a run that
produces no defeated defenses. A zero-proposal run is not a failure —
it is inertia winning, which is the right result when evidence is
insufficient.

The burden of proof rests on change. This applies to every phase below
and is not overridden by signal volume, elapsed time, or intuition.

---

## Phase 1 — Defense Registration

What this phase does: It records the skill's prior beliefs before any
evidence is examined. Each active strategy dimension gets a pre-signal
defense — the best argument for keeping it unchanged — and a defeat
criterion that states in advance what evidence would overturn it.

Why this phase runs first: Defenses written after signals are read
rationalize observations. Pre-registration makes the defeat assessment
falsifiable rather than retrospective. This blocks anchor bias.

Read simulations/TOPICS.md to identify the topic's active strategy
dimensions. Do not read strategy.md or any signal file at this step.

| Dimension | Best reason to keep unchanged | What would defeat this defense |
|-----------|------------------------------|--------------------------------|

If no dimensions are identifiable from the TOPICS.md entry alone:
"DEFENSE REGISTER: null — no active dimensions identifiable pre-read.
Inertia register empty."

---

## Phase 2 — Signal Inventory

What this phase does: It builds the complete evidence record before
the strategy frame is opened. Artifacts catalogued before reading
strategy.md are classified against dates and content — not against
strategy vocabulary.

Why this phase runs before Phase 3: Once strategy.md is open, its
language unconsciously shapes how artifacts are perceived. The
inventory must be vocabulary-independent. Post-lock re-reading would
introduce confirmation bias, so after this phase's output is written,
signal files may not be re-read.

Glob simulations/ for all artifacts matching the topic slug. Do not
read strategy.md at this step.

| Artifact filename | Date | Namespace | Summary (1 line) |
|------------------|------|-----------|------------------|

All 9 namespaces must appear in the table (scout / draft / review /
flow / trace / prove / listen / program / topic). A namespace with
zero artifacts gets a null row.

SIGNAL READ-LOCK: This table is now the fixed evidence record. Signal
files may not be re-read in any subsequent phase.

---

## Phase 3 — Strategy Read

What this phase does: It opens the strategy frame. The evidence record
is now fixed and vocabulary-independent, so reading strategy.md at
this point cannot contaminate the inventory classification.

Read strategy.md. Record the following:
- Strategy date (explicit — drives the NEW/PRIOR determination)
- Goal statement (verbatim)
- Every planned signal entry, organized by namespace

---

## Phase 4 — Delta Classification

What this phase does: It labels each inventory artifact as NEW
(eligible to drive proposals) or PRIOR (background; cannot drive
proposals alone). NEW artifacts are then classified by how they relate
to the strategy.

NEW = artifact date is later than the strategy date.
PRIOR = artifact date is at or before the strategy date.

For each NEW artifact, classify its relationship to the strategy using
one of four categories:
- CONFIRMED: it validates an existing strategy assumption
- EXPANDED: it extends an existing assumption to broader scope
- UNEXPECTED: it reveals a dimension the strategy did not address
- CHALLENGED: it contradicts an existing strategy assumption

| Finding ID | NEW artifact | Delta category | What understanding changed |
|------------|-------------|---------------|---------------------------|

All four category null declarations are required. They are not optional
even when empty, because their absence would be ambiguous:
"CONFIRMED: none — no NEW artifacts confirm existing assumptions."
"EXPANDED: none — no NEW artifacts expand existing assumptions."
"UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."
"CHALLENGED: none — no NEW artifacts challenge existing strategy."

---

## Phase 5 — Defeat Assessment

What this phase does: It is the inertia-defeat checkpoint. Each Phase
1 defense is evaluated against Phase 4 delta findings. This is the
only place where inertia can be officially defeated — proposals that
bypass this step are not valid.

Why a separate phase: Jumping directly from inventory to proposals
allows motivated reasoning — any signal can be dressed up as evidence.
The intermediate defeat assessment requires naming the specific defense
and the specific signal that overcomes it.

For each Phase 1 dimension, evaluate against Phase 4 NEW findings:

| Dimension | Phase 1 defense | Defeating signal | Verdict | Consequence if unchanged |
|-----------|----------------|-----------------|---------|------------------------|

Verdict is DEFEATED when a NEW signal from Phase 4 provides evidence
that overcomes the pre-registered defense. Verdict is HOLDS when the
defense survives — no proposal is generated for a HOLDS dimension.

When all verdicts are HOLDS: this is the null path. The skill outputs
the null declaration below and terminates. Phase 6 does not open.

"NULL_DELTA: inertia holds for all dimensions. strategy.md unchanged.
Null path complete."

---

## Phase 6 — Change Proposals

What this phase does: It translates DEFEATED defeat assessment entries
into structured proposals. HOLDS dimensions get NO CHANGE rows — they
are not silently omitted.

All 9 namespaces must have a row in the proposal table. Silence is not
a null declaration.

| # | Action | Dimension | Before | After | Evidence |
    Confidence | Consequence if unchanged | Bias blocked by guard |
|---|--------|-----------|--------|-------|----------|
    ------------|--------------------------|----------------------|

Action: ADD / REMOVE / REPRIORITIZE (for DEFEATED) / NO CHANGE (for HOLDS).
Confidence: HIGH (two or more independent NEW artifacts) / MEDIUM (one
NEW artifact) / LOW (inference from delta finding).
"Bias blocked by guard": the Phase 1 pre-registration or Phase 2
read-lock guard that protected this dimension's row from spurious
revision. Name the specific guard and the bias it blocked.

NO CHANGE row — Defense column: explain why the existing strategy is
sufficient given the NEW signals for that namespace. The explanation
"no new signals" is only valid if the namespace produced zero NEW
artifacts.

Null per type (all three required, type-labeled):
"ADDITIONS: none — inertia holds for all candidate additions."
"REMOVALS: none — inertia holds."
"REPRIORITIZATIONS: none — inertia holds."

---

## Phase 7 — Confirmation Gate

What this phase does: It presents the complete proposal table to the
user and stops. strategy.md is not modified at any earlier point and
is not modified now without an explicit YES response. The absence of a
NO is not a YES.

STOP. Present the complete Phase 6 table.

---
AWAITING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

The following reply modes are available:

YES — apply all proposals as shown and produce a diff summary.

NO — keep strategy.md unchanged. Output: "strategy.md unchanged.
Null path complete."

REVISED + edited table — incorporate the edits provided and re-present
the full proposal table for a final YES or NO. Apply only after the
second YES confirmation.

WITHDRAW [#] — remove the specified proposal rows from the table and
apply the remainder. WITHDRAW is a row-level operation: it drops named
rows and applies the rest without requiring a full table re-submission.
WITHDRAW [2, 5] removes rows 2 and 5; all other rows apply on YES.
WITHDRAW is distinct from NO, which rejects all proposals. WITHDRAW
is distinct from REVISED, which requires submitting a re-edited table.
---

Do not write anything further until the user replies.

---

## Phase 8 — Apply

What this phase does: It writes exactly the confirmed changes to
strategy.md. Nothing else changes. No re-evaluation occurs. No
dimension outside the confirmed proposal set is touched.

Apply step executes after YES, WITHDRAW-then-YES, or REVISED-then-YES.

Diff summary (structured):
| Proposal # | Applied | Change summary |
|------------|---------|----------------|

"strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations. Null path did not complete — changes applied."

On NO:
Emit: | — | NO | strategy.md unchanged |
"strategy.md unchanged. Null path complete."
```

---

## V-04 — Combined: Inertia Framing + Table-First

**Axes:** V-01 (inertia framing) + V-02 (table-first)
**Hypothesis:** Inertia-as-competitor framing and table-first schema enforcement are synergistic: the tables make the inertia competition visible at every decision cell. A "Status" column in the signal table doesn't just classify artifacts — it makes inertia's position explicit at every row. The combination closes both the action-bias failure mode (V-01) and the prose-burial failure mode (V-02) simultaneously.

```
You are running /topic:plan.

Default outcome: strategy.md unchanged. Inertia is the primary
competitor — not a process rule but the entity that must be defeated.
A zero-proposal run is a complete, valid execution.

---

## Upfront Commitments

Before opening any file, commit to the following:

1. Output schema is fixed (tables below). No prose substitutes for
   any table. No table merges.
2. Phase boundaries are hard: Phase N+1 does not open until Phase N
   output is written.
3. Inertia wins for every dimension where the pre-registered defense
   is not defeated by a specific named NEW artifact.
4. WITHDRAW [#] is a row-level removal operator: it drops named
   proposals and applies the rest. It is distinct from NO (rejects
   all) and REVISED (requires re-submitted table).
5. A run that reaches Phase 8 with zero proposals is not a failed run.

---

## Fixed Output Schema

T-1 Defense Register (Phase 1 — before any file is read)
| Dimension | Inertia defense | What would defeat this | Bias this guard blocks |

T-2 Signal Inventory (Phase 2 — before strategy.md is read)
| Filename | Date | Namespace | Summary (1 line) | Status |

T-3 Strategy Extract (Phase 3)
| Field | Value |

T-4 Delta Findings (Phase 4 — four subtables)
T-4a CONFIRMED | T-4b EXPANDED | T-4c UNEXPECTED | T-4d CHALLENGED
Each: | Finding ID | Artifact | What understanding changed |

T-5 Defeat Assessment (Phase 5 — inertia-defeat checkpoint)
| Dimension | T-1 defense | Defeating signal | Verdict | Consequence if unchanged |

T-6 Change Proposals (Phase 6)
| # | Action | Dimension | Before | After | Evidence |
    Confidence | Consequence if unchanged | Bias blocked |

T-7 Diff Output (Phase 8)
| Proposal # | Applied | Change summary |

---

## Phase 1 — Pre-Signal Defense Registration

Bias blocked: anchor bias.
Entry: no files read. Exit: T-1 written.

Read TOPICS.md only. Extract active strategy dimensions. Do NOT read
strategy.md or any signal file.

Populate T-1. "Bias this guard blocks" column: write "anchor bias"
for all rows — this guard is pre-signal precisely to prevent
post-signal rationalization.

T-1 null: "T-1: null — no active dimensions identifiable from TOPICS.md
entry. Inertia register empty."

---

## Phase 2 — Signal Inventory

Bias blocked: post-hoc rationalization.
Entry: T-1 written. Exit: T-2 written; SIGNAL READ-LOCK active.

Glob simulations/ for topic artifacts. Do NOT read strategy.md yet.

Populate T-2 columns: Filename, Date, Namespace, Summary. Leave Status
column blank — filled in Phase 4 after strategy date is known.

All 9 namespaces required: scout / draft / review / flow / trace /
prove / listen / program / topic. Null row for empty namespaces.

SIGNAL READ-LOCK: T-2 is the fixed evidence record. Signal files may
not be re-read. Bias blocked by lock: confirmation bias.

---

## Phase 3 — Read Strategy

Bias blocked: vocabulary contamination.
Entry: T-2 written, SIGNAL READ-LOCK active. Exit: T-3 written.

Read strategy.md. Populate T-3:
| Field        | Value          |
| Strategy date | [explicit date] |
| Goal          | [verbatim]      |
| Planned signals | [by namespace] |

---

## Phase 4 — Delta Classification

Entry: T-3 written. Exit: T-2 Status column filled; T-4 subtables written.

NEW = artifact date > strategy date. PRIOR = artifact date <= strategy date.
Fill T-2 Status column. Only NEW artifacts advance to T-5.

Populate four T-4 subtables:
T-4a CONFIRMED: validates existing assumption.
T-4b EXPANDED: extends existing assumption.
T-4c UNEXPECTED: reveals uncovered dimension.
T-4d CHALLENGED: contradicts existing assumption.

All four category nulls required (type-labeled):
"CONFIRMED: none." / "EXPANDED: none." / "UNEXPECTED: none." /
"CHALLENGED: none."

---

## Phase 5 — Defeat Assessment

Entry: T-4 complete. Exit: T-5 written; NULL_DELTA decision made.
Bias blocked: motivated reasoning — inertia is defeated at a formal
checkpoint with a named signal, not at proposal-generation time.

For each T-1 dimension, test against T-4 NEW findings. Populate T-5.

Verdict DEFEATED: dimension advances; generates T-6 rows.
Verdict HOLDS: dimension gets NO CHANGE row in T-6 with defense.

NULL_DELTA stop — if all verdicts are HOLDS:

+------------------------------------------------------------------+
| NULL_DELTA                                                       |
| Type: NULL_DELTA                                                 |
| All pre-registered defenses hold. Inertia wins.                  |
| strategy.md unchanged. Null path complete.                       |
+------------------------------------------------------------------+

Stop. Phase 6 does not open.

---

## Phase 6 — Change Proposals

Entry: at least one DEFEATED verdict in T-5.
Exit: T-6 written; all 9 namespaces covered.

Populate T-6. All 9 namespaces must have a row — silence is not a null
declaration.

DEFEATED dimensions: ADD / REMOVE / REPRIORITIZE with all columns.
HOLDS dimensions: NO CHANGE; Defense: explain sufficiency given NEW
signals. "No new signals" is valid only if that namespace had zero
NEW artifacts.

Confidence: HIGH (2+ independent NEW artifacts) / MEDIUM (1 NEW
artifact) / LOW (inference from delta finding).

"Bias blocked" column: name the T-1 or T-2 guard and the bias it
blocked for this dimension's row.

Null per type (all three required, type-labeled):
"ADDITIONS: none — inertia holds."
"REMOVALS: none — inertia holds."
"REPRIORITIZATIONS: none — inertia holds."

---

## Phase 7 — Confirmation Gate

Entry: T-6 written. Exit: user replies with one of four modes.

STOP. Present T-6.

---
AWAITING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

YES — apply all T-6 proposals; populate T-7.
  "strategy.md updated: [N] additions, [N] removals, [N]
  reprioritizations. Null path did not complete — changes applied."

NO — emit T-7: | — | NO | strategy.md unchanged |
  "strategy.md unchanged. Null path complete."

REVISED + edited T-6 — incorporate edits; re-present full T-6 for
  final YES/NO. Do not apply until second YES.

WITHDRAW [#] — row-level removal operator. WITHDRAW [2, 4] removes
  rows 2 and 4; remaining rows apply on YES. Re-present trimmed T-6
  before applying. WITHDRAW is NOT NO (rejects all). WITHDRAW is NOT
  REVISED (requires table re-submission). WITHDRAW needs no table
  re-submission — just YES on the trimmed presentation.
---

Stop. Write nothing further until the user replies.

---

## Phase 8 — Apply (YES / WITHDRAW-then-YES / REVISED-then-YES)

Write exactly the confirmed (non-withdrawn) changes. No re-evaluation.
No changes outside the confirmed proposal set.

Populate T-7. Emit count.
```

---

## V-05 — Full Combination: All Axes

**Axes:** Inertia framing + table-first + explicit lifecycle entry/exit conditions + bias labels at every guard + WITHDRAW semantics fully specified
**Hypothesis:** Combining all five axes closes the maximum number of failure modes simultaneously. Explicit phase entry/exit conditions create hard structural dependencies that prevent phase-skipping. Bias labeling at every guard transforms procedural compliance into epistemic commitment. The combination targets all 18 rubric criteria in one prompt body.

```
You are running /topic:plan.

INERTIA PRIOR: strategy.md unchanged is the default and correct
outcome absent defeating evidence. Inertia is the entity that wins
when evidence is insufficient. Every phase below is an instrument for
testing whether inertia holds for each active strategy dimension.

---

## Upfront Commitments (commit before reading any file)

1. Output schema is fixed (tables below). No prose substitutes any
   table. All column names are fixed.
2. Phase boundaries are hard entry/exit conditions: Phase N+1 does
   not open until Phase N's exit condition is met.
3. Inertia wins for any dimension whose pre-registered defense is not
   defeated by a named NEW artifact at the defeat assessment.
4. WITHDRAW [#] is a row-level removal operator distinct from YES
   (apply all), NO (reject all), and REVISED (table re-submission).
   WITHDRAW drops named rows and applies the remainder on YES.
5. Zero proposals is a complete, valid run — not a failure state.
6. The confirmation gate does not close without an explicit reply.
   The absence of NO is not YES.

---

## Fixed Output Schema

T-1 Defense Register
| Dimension | Best inertia defense | What would defeat this | Temporal marker | Bias blocked |

T-2 Signal Inventory
| Filename | Date | Namespace | Summary (1 line) | Status (NEW / PRIOR) |

T-3 Strategy Extract
| Field | Value |

T-4a CONFIRMED — T-4b EXPANDED — T-4c UNEXPECTED — T-4d CHALLENGED
Each subtable: | Finding ID | Artifact | What understanding changed |

T-5 Defeat Assessment
| Dimension | T-1 defense | Defeating signal | Verdict (DEFEATED / HOLDS) | Consequence if unchanged |

T-6 Change Proposals
| # | Action | Dimension | Before | After | Evidence |
    Confidence | Consequence if unchanged | Bias blocked by guard |

T-7 Diff Output
| Proposal # | Applied | Change summary |

---

## Phase 1 — Pre-Signal Defense Registration
Entry condition: no files read.
Exit condition: T-1 written; one row per active strategy dimension.
Bias blocked: anchor bias — defenses registered before signals are
seen cannot be contaminated by signal vocabulary. A defense written
after reading signals rationalizes evidence rather than declares prior
belief. "Temporal marker" column: write PRE-READ for all rows.

Read TOPICS.md only. Extract active strategy dimensions.
Do NOT read strategy.md or any signal file.

Populate T-1. "Temporal marker" is PRE-READ for every row (enforces
that this defense was not informed by any downstream file).

Null: "T-1: null — no dimensions identifiable from TOPICS.md alone.
Inertia register empty. Proceed to Phase 2."

---

## Phase 2 — Signal Inventory
Entry condition: T-1 written.
Exit condition: T-2 written; SIGNAL READ-LOCK active.
Bias blocked: post-hoc rationalization — evidence catalogued before
the strategy frame is open is vocabulary-independent. The inventory
becomes the fixed evidence record against which delta is measured.

Glob simulations/ for all artifacts matching the topic slug.
Do NOT read strategy.md yet.

Populate T-2: Filename, Date, Namespace, Summary (1 line).
Leave Status column blank — filled in Phase 4 after strategy date is known.
All 9 namespaces required: scout / draft / review / flow / trace /
prove / listen / program / topic. Null row for empty namespaces.

SIGNAL READ-LOCK: T-2 is now the fixed evidence record.
Signal files may not be re-read in any subsequent phase.
Bias blocked by lock: confirmation bias — post-strategy-open re-reading
selects details that confirm what the strategy already says.

---

## Phase 3 — Read Strategy
Entry condition: T-2 written; SIGNAL READ-LOCK active.
Exit condition: T-3 written; strategy date recorded.
Bias blocked: vocabulary contamination — reading strategy only after
the inventory is fixed means artifact classification cannot be
anchored to strategy vocabulary.

Read strategy.md. Populate T-3:
| Field            | Value              |
| Strategy date    | [required — drives NEW/PRIOR split] |
| Goal statement   | [verbatim]         |
| Planned signals  | [by namespace]     |

---

## Phase 4 — Delta Classification
Entry condition: T-3 written.
Exit condition: T-2 Status column filled; T-4a–T-4d written.

NEW = artifact date > strategy date. Only NEW artifacts are eligible
to advance to the defeat assessment.
PRIOR = artifact date <= strategy date.

Classify each NEW artifact into one of four categories:
- CONFIRMED: validates an existing strategy assumption
- EXPANDED: extends an existing assumption to broader scope
- UNEXPECTED: reveals a dimension the strategy did not address
- CHALLENGED: contradicts an existing strategy assumption

Populate T-2 Status column. Populate T-4a–T-4d.

All four category nulls required (type-labeled):
"CONFIRMED: none — no NEW artifacts confirm existing assumptions."
"EXPANDED: none — no NEW artifacts expand existing assumptions."
"UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."
"CHALLENGED: none — no NEW artifacts challenge existing strategy."

---

## Phase 5 — Defeat Assessment
Entry condition: T-4a–T-4d written.
Exit condition: T-5 written; NULL_DELTA decision made.
Bias blocked: motivated reasoning — inertia can only be defeated at
a formal checkpoint with a named signal. Proposals that bypass this
step are structurally invalid.

For each T-1 dimension, evaluate against T-4 NEW findings.
Populate T-5.

Verdict DEFEATED: the NEW signal overcomes the pre-registered defense.
Dimension advances to T-6 with full proposal row.

Verdict HOLDS: the defense survives. Dimension gets a NO CHANGE row
in T-6 with a defense explanation.

NULL_DELTA stop condition — if all T-5 verdicts are HOLDS:

+------------------------------------------------------------------+
| NULL_DELTA                                                       |
| Type: NULL_DELTA                                                 |
| All pre-registered defenses hold. Inertia wins.                  |
| strategy.md unchanged. Null path complete.                       |
+------------------------------------------------------------------+

Stop. Phase 6 does not open. Execution is complete.

---

## Phase 6 — Change Proposals
Entry condition: at least one DEFEATED verdict in T-5.
Exit condition: T-6 written; all 9 namespaces covered.
Bias blocked: availability bias — requiring a row for every namespace
prevents silent omission of weak-signal namespaces (which would be
invisible to the user at decision time).

Populate T-6. All 9 namespaces must have a row — silence is not a
null declaration.

DEFEATED dimensions: ADD / REMOVE / REPRIORITIZE with all columns.
HOLDS dimensions: NO CHANGE; Defense: explain why existing strategy
is sufficient given the NEW signals for that namespace. "No new
signals" is valid only if that namespace produced zero NEW artifacts.

Confidence: HIGH (two or more independent NEW artifacts) /
MEDIUM (one NEW artifact) / LOW (inference from delta finding only).

"Bias blocked by guard" column: name the Phase 1 or Phase 2 guard
and the specific bias it blocked for this dimension's row.

Null per type (all three required, type-labeled):
"ADDITIONS: none — inertia holds for all candidate additions."
"REMOVALS: none — inertia holds."
"REPRIORITIZATIONS: none — inertia holds."

---

## Phase 7 — Confirmation Gate
Entry condition: T-6 written.
Exit condition: user replies with one of four valid modes.
Bias blocked: action bias — the hard stop prevents the skill from
applying changes on behalf of the user without explicit confirmation.

STOP. Present T-6. Do not open strategy.md for writing.

---
AWAITING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Four reply modes (all are valid outcomes):

YES — apply all T-6 proposals.
  Populates T-7. "strategy.md updated: [N] additions, [N] removals,
  [N] reprioritizations. Null path did not complete — changes applied."

NO — keep strategy.md unchanged.
  Emits T-7: | — | NO | strategy.md unchanged |
  "strategy.md unchanged. Null path complete."

REVISED + edited T-6 — incorporate user edits into T-6 and re-present
  the full table. Do not apply until the user confirms YES a second
  time. REVISED is the correct mode when the user wants to change which
  proposals are included or edit their content before applying.

WITHDRAW [#] — row-level removal operator. WITHDRAW [2, 4] removes
  rows 2 and 4 from T-6; remaining rows apply on YES. Re-present the
  trimmed T-6 and ask for YES/NO before applying. WITHDRAW is NOT NO:
  it preserves the non-withdrawn rows. WITHDRAW is NOT REVISED: it
  does not require a user-submitted edited table. WITHDRAW [2, 4] then
  YES applies all rows except 2 and 4.
---

Stop. Write nothing further until the user replies.

---

## Phase 8 — Apply
Entry condition: YES (direct), WITHDRAW-then-YES, or REVISED-then-YES.
Exit condition: strategy.md written; T-7 populated; count confirmed.

Write exactly the confirmed (non-withdrawn) changes to strategy.md.
No re-evaluation. No dimensions touched outside the confirmed set.

Populate T-7. Emit count:
"strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations. Null path did not complete — changes applied."

On NO:
Emit T-7: | — | NO | strategy.md unchanged |
"strategy.md unchanged. Null path complete."
```

---

## Rubric Coverage Prediction

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Inertia prior | 2 | 2 | 2 | 2 | 2 |
| C-02 Delta before proposals | 2 | 2 | 2 | 2 | 2 |
| C-03 Action-typed proposals | 2 | 2 | 2 | 2 | 2 |
| C-04 Confirmation gate | 2 | 2 | 2 | 2 | 2 |
| C-05 Write guard | 2 | 2 | 2 | 2 | 2 |
| C-06 Type-labeled null | 2 | 2 | 2 | 2 | 2 |
| C-07 Namespace column | 2 | 2 | 2 | 2 | 2 |
| C-08 Diff summary | 2 | 2 | 2 | 2 | 2 |
| C-09 All 4 delta categories | 2 | 2 | 2 | 2 | 2 |
| C-10 1-line summary | 2 | 2 | 2 | 2 | 2 |
| C-11 Stop on null delta | 2 | 2 | 2 | 2 | 2 |
| C-12 Before/After in proposals | 2 | 2 | 2 | 2 | 2 |
| C-13 Named artifact per proposal | 2 | 2 | 2 | 2 | 2 |
| C-14 Type label in structured block | 1 | 2 | 1 | 2 | 2 |
| C-15 Structured diff | 2 | 2 | 2 | 2 | 2 |
| C-16 Confidence levels | 2 | 2 | 2 | 2 | 2 |
| C-17 Bias labels per guard | 2 | 2 | 2 | 2 | 2 |
| C-18 WITHDRAW semantics | 2 | 2 | 2 | 2 | 2 |
| **Predicted composite** | **98** | **100** | **98** | **100** | **100** |

**Notes:**
- C-14 partial in V-01 and V-03: NULL_DELTA appears in prose rather than a fenced block — the `+----+` box in V-04/V-05 makes the type label structural
- C-17: all five variations include inline "Bias blocked" annotations — full pass expected
- C-18: all five variations define WITHDRAW with row-level semantics, distinguish it from NO and REVISED, and specify WITHDRAW [2,4] syntax

**Key structural difference from R6:** All five variations now include C-16 (confidence levels: HIGH/MEDIUM/LOW) which was the only gap in R6 V-01. The "Bias blocked by guard" column covers C-17 inline rather than in a separate section.
