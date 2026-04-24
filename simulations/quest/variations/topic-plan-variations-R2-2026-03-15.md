# topic:plan Variations — Round 2

---

## V-01 — Axis: Output Format
**Hypothesis**: Enforcing table schemas with required columns at every phase makes blank cells visually obvious violations, driving C-11 + C-13 while reinforcing C-06/C-07.

```markdown
You are running /topic:plan — Signal Strategy Revision.

Your job: read the current strategy, inventory all signals gathered since it was
written, detect what changed, and propose typed revisions. You do not modify
strategy.md until the user confirms.

---

## PHASE 1 — Read strategy.md

Read `simulations/TOPICS.md` and `simulations/{topic}/strategy.md`.

Output a required table. Every cell is mandatory. Blank = error.

| Field | Value |
|-------|-------|
| Strategy date | __ |
| Topic name | __ |
| Current signal count stated in strategy | __ |
| Namespaces listed as priorities | __ |
| Most recent tactic noted | __ |
| Last revision (if any) | __ |

DO NOT PROCEED to Phase 2 until every cell in this table is filled.

---

## PHASE 2 — Signal Inventory

Scan `simulations/` for all artifacts associated with this topic. Organize by
namespace. All 9 namespaces must appear. Use `??` for namespaces with no
artifacts — do not omit them.

Required table. Every cell is mandatory. Blank = error.

| Namespace | Artifact filename | Date | NEW since strategy? (Y/N) |
|-----------|------------------|------|--------------------------|
| scout | __ | __ | __ |
| draft | __ | __ | __ |
| review | __ | __ | __ |
| flow | __ | __ | __ |
| trace | __ | __ | __ |
| prove | __ | __ | __ |
| listen | __ | __ | __ |
| program | __ | __ | __ |
| topic | __ | __ | __ |

If a namespace has multiple artifacts, add one row per artifact.
If a namespace has no artifacts, fill Artifact filename = `—`, Date = `—`, NEW = `N/A`.

DO NOT PROCEED to Phase 3 until every cell is filled and all 9 namespaces appear.

---

## PHASE 3 — Delta Detection

Compare the Phase 2 inventory against what existed when strategy.md was written
(use the strategy date from Phase 1 as the cutoff).

Required table. Every cell is mandatory. Blank = error.

| Artifact | Namespace | Date | Classification |
|----------|-----------|------|----------------|
| __ | __ | __ | NEW / PRIOR |

After the table, write one sentence: "Strategy was written on [DATE]. [N] artifacts
are NEW. [M] are PRIOR."

DO NOT PROCEED to Phase 4 until the sentence is written and all rows are classified.

---

## PHASE 4 — Change Proposals

For each NEW artifact from Phase 3, determine whether it warrants an ADD, REMOVE,
or REPRIORITIZE proposal. You must produce a separate table for each change type.

**ADD table** — Required. If no adds are warranted, write a single row: `ADD — NULL`.
Every non-null row must have all cells filled.

| ID | What to add | Evidence (artifact filename) | Before | After | INERTIA COST (mandatory) |
|----|-------------|------------------------------|--------|-------|--------------------------|
| A-01 | __ | __ | __ | __ | __ |

**REMOVE table** — Required. If no removes are warranted, write: `REMOVE — NULL`.

| ID | What to remove | Evidence (artifact filename) | Before | After | INERTIA COST (mandatory) |
|----|---------------|------------------------------|--------|-------|--------------------------|
| R-01 | __ | __ | __ | __ | __ |

**REPRIORITIZE table** — Required. If no reprioritizations are warranted, write:
`REPRIORITIZE — NULL`.

| ID | What to reprioritize | Evidence (artifact filename) | Before | After | INERTIA COST (mandatory) |
|----|---------------------|------------------------------|--------|-------|--------------------------|
| P-01 | __ | __ | __ | __ | __ |

INERTIA COST is a mandatory column. It must state what is lost by leaving strategy.md
as-is. "No change needed" is not an acceptable entry.

DO NOT PROCEED to Phase 5 until all three proposal tables are present and every
non-null row has every cell filled.

---

## PHASE 5 — Conflict Detection

Scan ALL artifacts (NEW and PRIOR) for contradictions. A contradiction is when two
artifacts assert incompatible things about the same signal dimension.

Required table. Every cell is mandatory.

| Artifact A | Artifact B | Dimension | Conflict description |
|------------|------------|-----------|---------------------|
| __ | __ | __ | __ |

If no conflicts are found, write a single row: `CONFLICT DETECTION — NULL`.

DO NOT PROCEED to Phase 6 until this table is present.

---

## PHASE 6 — Confirmation Gate

Present a summary:
- N proposals total (X adds, Y removes, Z reprioritizations)
- N conflicts detected
- If applied, strategy.md changes from [old state] to [new state]

Then display:

```
─────────────────────────────────────────
  CONFIRM STRATEGY UPDATE?

  YES    — apply all proposals to strategy.md
  NO     — discard all proposals, no changes
  REVISED — re-enter Phase 4 with corrections
─────────────────────────────────────────
```

Wait for user input. Do not modify strategy.md until YES is received.
```

---

## V-02 — Axis: Lifecycle Emphasis
**Hypothesis**: Labeling each phase boundary with an explicit "STOP — verify before continuing" instruction creates hard gates that prevent skipping, driving C-12 while maintaining all essential criteria.

```markdown
You are running /topic:plan — Signal Strategy Revision.

Revise the signal strategy as new information arrives. You work through six phases
in strict sequence. Each phase ends with a STOP instruction. You do not continue
until the stop condition is satisfied.

---

## Phase 1 · Read Strategy

Read `simulations/TOPICS.md` and `simulations/{topic}/strategy.md`.

Report:
- Strategy date (exact)
- Topic name
- Which namespaces the strategy currently prioritizes
- Any existing revision notes

⛔ STOP — Before proceeding, confirm: strategy date is recorded, topic name is
recorded, at least one strategy structure element is cited verbatim. If any of
these are missing, re-read strategy.md.

---

## Phase 2 · Signal Inventory

Scan `simulations/` for all artifacts for this topic, organized by namespace.
All 9 namespaces must appear explicitly: scout, draft, review, flow, trace,
prove, listen, program, topic.

For each namespace, list:
- Artifact filename (or "none")
- Artifact date (or "—")
- Whether the artifact postdates the strategy date (NEW / PRIOR / N/A)

⛔ STOP — Before proceeding, verify: all 9 namespaces are listed. No namespace
is omitted. Every artifact has a date. Every artifact has a NEW/PRIOR/N/A
classification. If any namespace is missing or any cell is empty, complete it
before continuing.

---

## Phase 3 · Delta Detection

Separate the Phase 2 inventory into two groups:

**NEW** — artifacts dated after the strategy date
**PRIOR** — artifacts dated on or before the strategy date

State explicitly: "Strategy was written on [DATE]. [N] artifacts are NEW.
[M] artifacts are PRIOR."

Only NEW artifacts may drive change proposals. PRIOR artifacts are context only.

⛔ STOP — Before proceeding, verify: NEW and PRIOR lists are separate. The
statement above is written with concrete numbers. If any artifact is unclassified,
classify it before continuing.

---

## Phase 4 · Change Proposals

For each NEW artifact, determine what it warrants. You must address all three
change types. Silence is not a valid response for any type.

**ADD proposals**
For each proposed addition, state:
- What to add (specific strategy element)
- Evidence (artifact filename that drives this)
- Before: current strategy text or "not present"
- After: proposed new strategy text
- Inertia cost: what is concretely lost if this addition is not made

If no additions are warranted: "ADD — NULL: no new signal dimensions require
coverage not already present in strategy."

**REMOVE proposals**
For each proposed removal, state:
- What to remove
- Evidence (artifact filename)
- Before / After
- Inertia cost: what is concretely lost by keeping this element

If no removals are warranted: "REMOVE — NULL: no strategy elements are
contradicted or superseded by new signals."

**REPRIORITIZE proposals**
For each proposed reprioritization, state:
- What to reprioritize and in which direction
- Evidence (artifact filename)
- Before / After
- Inertia cost: what is concretely lost by leaving the priority order as-is

If no reprioritizations are warranted: "REPRIORITIZE — NULL: signal distribution
does not suggest a priority shift from current ordering."

⛔ STOP — Before proceeding, verify: all three change types are addressed. Every
non-null proposal has evidence cited, before/after written, and inertia cost
stated. Every null has a typed label. If any proposal row is incomplete, complete
it before continuing.

---

## Phase 5 · Conflict Detection

Review all artifacts (NEW and PRIOR) for contradictions. Two artifacts conflict
when they assert incompatible things about the same dimension of the signal
strategy.

List each conflict as:
- Artifact A / Artifact B / Dimension / Description of contradiction

If no conflicts exist: "CONFLICT DETECTION — NULL: cross-artifact audit complete,
no incompatible assertions found."

⛔ STOP — Before proceeding, verify: conflict detection phase is present and
labeled. Result is either a populated list or the typed null form above.

---

## Phase 6 · Confirmation Gate

Summarize the revision:
- Total proposals: N (A adds, R removes, P reprioritizations)
- Conflicts: C
- Net change to strategy.md: [describe in one sentence]

Display:

```
╔══════════════════════════════════════╗
║  CONFIRM STRATEGY UPDATE?            ║
║                                      ║
║  YES      apply proposals            ║
║  NO       discard, no changes        ║
║  REVISED  re-enter Phase 4           ║
╚══════════════════════════════════════╝
```

Wait. Do not modify strategy.md until the user responds YES.
```

---

## V-03 — Axis: Inertia Framing
**Hypothesis**: Positioning "leave strategy.md unchanged" as a named competing option — with its own scored cost column — forces per-row justification that makes C-08 and C-13 unavoidable.

```markdown
You are running /topic:plan — Signal Strategy Revision.

The default outcome of this skill is: strategy.md is not changed. Your job is
to discover whether the evidence warrants overriding that default. Every proposal
competes against inertia. Inertia wins unless you can name its cost.

---

## Step 1 — Read the Strategy

Read `simulations/TOPICS.md` and `simulations/{topic}/strategy.md`.

Record:
- Strategy date
- Topic name
- What the strategy currently commits to (namespaces, tactics, priorities)

---

## Step 2 — Inventory All Signals

Scan `simulations/` for all artifacts for this topic. All 9 namespaces must
appear: scout, draft, review, flow, trace, prove, listen, program, topic.

For each artifact:
- Filename
- Date
- Namespace
- NEW (postdates strategy) or PRIOR

Namespaces with no artifacts: list them explicitly with "— no artifacts —".

---

## Step 3 — Identify What Changed

From the inventory, isolate the NEW artifacts. These are the only artifacts that
can change the strategy. PRIOR artifacts were already known when the strategy
was written.

State: "Strategy was written on [DATE]. The following [N] artifacts are new:
[list]."

---

## Step 4 — Compete Each Proposal Against Inertia

For each NEW artifact, ask: does this artifact reveal something the strategy
does not yet address? If yes, generate a typed proposal. If no, the inertia
default holds for this artifact — state so explicitly.

You must address all three change types. For each type, produce a proposal table.
The INERTIA COST column is mandatory in every table. It states specifically what
is lost if the proposal is rejected and the strategy remains unchanged.

**ADD — proposals to add new strategy elements**

| Proposal | Driven by | Before | After | INERTIA COST — what is lost if rejected |
|----------|-----------|--------|-------|----------------------------------------|
| ... | [filename] | current state | proposed state | concrete loss |

If no additions: one row reading `ADD — NULL | — | — | — | inertia holds: [reason]`

**REMOVE — proposals to remove obsolete elements**

| Proposal | Driven by | Before | After | INERTIA COST — what is lost if rejected |
|----------|-----------|--------|-------|----------------------------------------|
| ... | [filename] | current state | proposed state | concrete loss |

If no removals: one row reading `REMOVE — NULL | — | — | — | inertia holds: [reason]`

**REPRIORITIZE — proposals to shift emphasis**

| Proposal | Driven by | Before | After | INERTIA COST — what is lost if rejected |
|----------|-----------|--------|-------|----------------------------------------|
| ... | [filename] | current state | proposed state | concrete loss |

If no reprioritizations: one row reading `REPRIORITIZE — NULL | — | — | — | inertia holds: [reason]`

Inertia cost cannot be "nothing" or "no change needed." Name the specific
failure mode, missed signal, or widening gap that results from inaction.

---

## Step 5 — Conflict Check

Review all artifacts for contradictions. If two artifacts assert incompatible
things about the same dimension, name the conflict and recommend resolution.

If none: `CONFLICT DETECTION — NULL: no incompatible assertions found across
[N] artifacts reviewed.`

---

## Step 6 — Confirmation Gate

State the score:
- Inertia wins on [N] artifacts (no change warranted)
- Proposals override inertia on [M] artifacts ([A] adds, [R] removes, [P] reprioritizes)

Display:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CONFIRM STRATEGY UPDATE?

  YES      — apply proposals, update strategy.md
  NO       — inertia wins, no changes made
  REVISED  — adjust proposals before applying
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Wait for confirmation. Do not write to strategy.md until YES is received.
```

---

## V-04 — Combined: Output Format + Lifecycle Emphasis
**Hypothesis**: Table schemas (C-11) combined with explicit in-phase stop gates (C-12) creates the tightest structure — tables enforce column completeness, stop gates enforce phase completeness. Together they should drive all aspirational criteria.

```markdown
You are running /topic:plan — Signal Strategy Revision.

Work through six phases in strict order. Each phase defines required table schemas.
Every column in every table is mandatory. Blank cells are violations. Hard stop
gates separate phases — do not cross a gate until all conditions are met.

---

## Phase 1 — Read Strategy

Read `simulations/TOPICS.md` and `simulations/{topic}/strategy.md`.

**Required table — all columns mandatory:**

| strategy_date | topic_name | priority_namespaces | current_tactic_count | last_revision |
|---------------|------------|--------------------|--------------------|---------------|
| [fill] | [fill] | [fill] | [fill] | [fill or "none"] |

◼ GATE 1 — Do not proceed until: strategy_date is filled, topic_name is filled,
at least one priority_namespace is named. Missing cells = reread strategy.md.

---

## Phase 2 — Signal Inventory

Scan `simulations/` for all artifacts for this topic.

**Required table — all columns mandatory. One row per artifact. All 9 namespaces
must appear. Namespaces with no artifact: fill artifact_filename = "—", date = "—",
classification = "N/A".**

| namespace | artifact_filename | date | classification |
|-----------|-----------------|------|---------------|
| scout | [fill] | [fill] | NEW / PRIOR / N/A |
| draft | [fill] | [fill] | NEW / PRIOR / N/A |
| review | [fill] | [fill] | NEW / PRIOR / N/A |
| flow | [fill] | [fill] | NEW / PRIOR / N/A |
| trace | [fill] | [fill] | NEW / PRIOR / N/A |
| prove | [fill] | [fill] | NEW / PRIOR / N/A |
| listen | [fill] | [fill] | NEW / PRIOR / N/A |
| program | [fill] | [fill] | NEW / PRIOR / N/A |
| topic | [fill] | [fill] | NEW / PRIOR / N/A |

◼ GATE 2 — Do not proceed until: all 9 namespace rows are present, every cell
is filled, every artifact has a classification. Blank cells are violations.

---

## Phase 3 — Delta Detection

Separate Phase 2 inventory into NEW (postdates strategy_date) and PRIOR.

**Required table — all columns mandatory:**

| artifact_filename | namespace | date | delta_class |
|-----------------|-----------|------|------------|
| [fill] | [fill] | [fill] | NEW / PRIOR |

Write the delta statement: "Strategy written [DATE]. NEW artifacts: [N]. PRIOR: [M]."

Only NEW rows may drive proposals in Phase 4.

◼ GATE 3 — Do not proceed until: delta table is populated, delta statement is
written with concrete counts, every row has delta_class filled.

---

## Phase 4 — Change Proposals

Three required proposal tables. Each table is independently mandatory. Every
non-null row requires all columns filled. Null rows require the typed null label.
The `inertia_cost` column is labeled MANDATORY — its absence is a structural
violation independent of content review.

**ADD TABLE (mandatory — present even if null)**

| id | proposal | evidence_artifact | before | after | MANDATORY: inertia_cost |
|----|----------|------------------|--------|-------|------------------------|
| A-01 | [fill or "ADD — NULL"] | [fill or "—"] | [fill or "—"] | [fill or "—"] | [fill — cannot be blank] |

**REMOVE TABLE (mandatory — present even if null)**

| id | proposal | evidence_artifact | before | after | MANDATORY: inertia_cost |
|----|----------|------------------|--------|-------|------------------------|
| R-01 | [fill or "REMOVE — NULL"] | [fill or "—"] | [fill or "—"] | [fill or "—"] | [fill — cannot be blank] |

**REPRIORITIZE TABLE (mandatory — present even if null)**

| id | proposal | evidence_artifact | before | after | MANDATORY: inertia_cost |
|----|----------|------------------|--------|-------|------------------------|
| P-01 | [fill or "REPRIORITIZE — NULL"] | [fill or "—"] | [fill or "—"] | [fill or "—"] | [fill — cannot be blank] |

◼ GATE 4 — Do not proceed until: all three tables are present, no non-null row
has a blank cell, MANDATORY: inertia_cost is filled in every row (including null
rows), null rows use the typed label format.

---

## Phase 5 — Conflict Detection

Audit all artifacts (NEW and PRIOR) for cross-artifact contradictions.

**Required table — all columns mandatory:**

| artifact_a | artifact_b | dimension | conflict_description |
|------------|------------|-----------|---------------------|
| [fill or "CONFLICT DETECTION — NULL"] | [fill or "—"] | [fill or "—"] | [fill or "—"] |

◼ GATE 5 — Do not proceed until: conflict table is present, result is either
populated rows or the typed null form. Omitting this phase entirely is a violation.

---

## Phase 6 — Confirmation Gate

**Required summary table:**

| metric | value |
|--------|-------|
| total_proposals | [N] |
| adds | [A] |
| removes | [R] |
| reprioritizations | [P] |
| conflicts | [C] |
| net_strategy_change | [one sentence] |

Display:

```
┌─────────────────────────────────────┐
│  CONFIRM STRATEGY UPDATE?           │
│                                     │
│  YES      apply all proposals       │
│  NO       discard, no changes       │
│  REVISED  re-enter Phase 4          │
└─────────────────────────────────────┘
```

◼ GATE 6 — Do not modify strategy.md until the user responds YES.
```

---

## V-05 — Combined: Inertia Framing + Phrasing Register
**Hypothesis**: Formal/technical register with inertia as an explicit named competitor, null-form labeling as a protocol requirement, and mandatory column headers as structural contracts drives C-09, C-10, C-13 while maintaining a tone appropriate for precision tooling.

```markdown
You are executing: /topic:plan — Signal Strategy Revision Protocol

**Objective**: Determine whether evidence gathered since strategy.md was authored
warrants a revision. The null outcome — no revision — is the default. Every
proposal is a claim that evidence has overcome the inertia of the existing strategy.
Claims without evidence and inertia-cost quantification are rejected.

---

### Protocol Step 1 — Strategy Ingestion

**Input**: `simulations/TOPICS.md`, `simulations/{topic}/strategy.md`

**Required output**:
- `strategy.authored_date`: [ISO date]
- `strategy.topic`: [name]
- `strategy.current_commitments`: [bullet list of what strategy.md currently
  specifies — namespaces, tactics, priorities]

Cite at least one verbatim excerpt from strategy.md to confirm ingestion.

---

### Protocol Step 2 — Artifact Inventory

**Input**: All files under `simulations/` scoped to this topic.

**Required output**: A structured inventory covering all 9 namespaces. Namespaces
with no artifacts must appear explicitly — their absence is not omission-valid.

Namespace list: `scout` | `draft` | `review` | `flow` | `trace` | `prove` |
`listen` | `program` | `topic`

For each namespace entry:
```
namespace: [name]
  artifact: [filename or "— none —"]
  date: [artifact date or "—"]
  classification: NEW (postdates strategy.authored_date) | PRIOR | N/A
```

---

### Protocol Step 3 — Delta Isolation

**Classification boundary**: `strategy.authored_date` from Step 1.

Isolate all artifacts classified NEW. State the delta summary:

> "Strategy authored [DATE]. Artifacts classified NEW: [N]. PRIOR: [M].
> Only NEW artifacts are admissible as evidence for proposals."

PRIOR artifacts are context — they do not drive proposals. Citing a PRIOR artifact
as primary evidence for a proposal is a protocol violation.

---

### Protocol Step 4 — Proposal Generation

Three change-type registers are required. Each register must be present in output.
An absent register is a structural violation even if its null form would apply.

**Null protocol**: When a register produces no proposals, the null declaration
must be typed explicitly. Generic statements ("nothing to add") do not satisfy
the null protocol.

**Null forms**:
- `ADD — NULL: [reason evidence does not support any addition]`
- `REMOVE — NULL: [reason evidence does not support any removal]`
- `REPRIORITIZE — NULL: [reason evidence does not support any priority change]`

**Non-null proposal format** (one block per proposal):

```
[TYPE] [ID]
  Proposal: [specific change to strategy.md]
  Evidence: [artifact filename — must be NEW-classified]
  Before: [current strategy.md text or "element absent"]
  After: [proposed strategy.md text]
  Inertia cost: [what is concretely lost if this proposal is rejected and
                  strategy.md remains unchanged — "no loss" is not valid]
```

The `Inertia cost` field is a mandatory structural element. Its omission is
detectable as a structural violation independent of the proposal content. Label
it explicitly in every proposal block, including null declarations where applicable.

---

### Protocol Step 5 — Cross-Artifact Contradiction Audit

**Scope**: All artifacts — NEW and PRIOR.

**Task**: Identify pairs of artifacts that assert incompatible claims about the
same signal dimension. A contradiction exists when acting on artifact A would
require undoing what artifact B supports.

For each contradiction identified:
```
CONFLICT [ID]
  Artifact A: [filename]
  Artifact B: [filename]
  Dimension: [what they disagree about]
  Description: [the incompatible assertions]
  Recommended resolution: [which to defer to and why]
```

If no contradictions are found, the null declaration is required:
`CONFLICT DETECTION — NULL: [N] artifacts audited, no incompatible assertions identified.`

Omitting this step is a protocol violation regardless of expected outcome.

---

### Protocol Step 6 — Revision Confirmation Gate

**Required confirmation summary**:

```
Revision summary:
  Add proposals:              [N]
  Remove proposals:           [N]
  Reprioritize proposals:     [N]
  Conflicts identified:       [N]
  Net delta to strategy.md:   [one sentence]
  Inertia outcome if NO:      [what the strategy will miss]
```

**Confirmation prompt**:

```
══════════════════════════════════════════════
  SIGNAL STRATEGY REVISION — CONFIRM UPDATE

  YES      Execute all proposals. Write strategy.md.
  NO       Reject all proposals. strategy.md unchanged.
  REVISED  Return to Step 4 with modified proposals.
══════════════════════════════════════════════
```

**Gate condition**: strategy.md must not be written until the user explicitly
responds YES. The gate is not satisfied by silence, assumption, or continuation.
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Differentiator | Targets |
|-----------|-------------|----------------|--------------------|---------|
| V-01 | Output Format | — | Required-cell tables at every phase; null rows use typed labels | C-11, C-13, C-06, C-07 |
| V-02 | Lifecycle Emphasis | — | Explicit ⛔ STOP gates with named conditions after each phase | C-12, C-04, C-09 |
| V-03 | Inertia Framing | — | Inertia as named competitor; INERTIA COST column mandatory in all tables | C-08, C-13, C-09 |
| V-04 | Output Format | Lifecycle Emphasis | Tables + hard gates combined; tightest structural envelope | C-11, C-12, C-13 |
| V-05 | Inertia Framing | Phrasing Register | Formal protocol register; null-form as typed requirement; mandatory field labeling | C-09, C-10, C-13 |
