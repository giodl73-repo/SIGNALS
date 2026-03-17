## topic:plan — Skill Body Variations (Round 20, v20 rubric)

Five complete, runnable skill body prompts. V-01 through V-03 are single-axis. V-04 and V-05 combine axes. C-58 (Defense basis temporal audit — PRE-READ / POST-READ / POST-SIGNAL) is introduced as a structural column in V-02 and carried forward into V-05.

---

## V-01

**Variation axis:** Role sequence — signal inventory precedes strategy read
**Hypothesis:** Completing all 9 namespace inventories before opening strategy.md prevents the existing strategy from anchoring delta detection; unbiased impressions form before the prior frame is visible.

---

You are running `topic:plan` — strategy revision for a Signal topic.

**Your first action is the signal inventory. Do not read strategy.md until Phase 2.**

---

### Phase 1: Signal Inventory

Scan `simulations/` across all 9 namespaces in this order:
`scout` / `draft` / `review` / `flow` / `trace` / `prove` / `listen` / `program` / `topic`

For each namespace, produce a table:

| Filename | Date | Content summary |
|----------|------|-----------------|
| (full path) | (from filename) | (one line) |

Complete all 9 namespace tables before proceeding to Phase 2.

---

### Phase 2: Read strategy.md

Open `simulations/topic/[topic-name]/strategy.md`.

Record:
- Strategy creation date — name it explicitly
- Goal statement — verbatim or quoted paraphrase
- Every planned signal entry, listed by namespace

Cite at least one concrete reference to the strategy's structure in your output (e.g., a quoted section header, a planned signal entry, a goal line).

---

### Phase 3: Delta Detection

Compare the Phase 1 inventory against the Phase 2 strategy.

Label each artifact:
- **PRIOR** — the strategy explicitly references or planned for this artifact
- **NEW** — the strategy does not reference this artifact

For each NEW artifact, classify:
- **CONFIRMS** — validates an existing planned signal
- **EXPANDS** — reveals a dimension outside the strategy's current scope
- **CHALLENGES** — contradicts an assumption the strategy was built on

Only NEW artifacts drive proposals. Complete classification before writing any proposals.

---

### Phase 4: Typed Change Proposals

Produce a proposal table. Every namespace must have a row — silence is not a null declaration.

| Namespace | Proposal type | Evidence | Before | After | Defense |
|-----------|--------------|----------|--------|-------|---------|

Column rules:
- **Proposal type**: `ADD` / `REMOVE` / `REPRIORITIZE` / `NO CHANGE`
- **Evidence**: artifact filename — required for every non-null proposal row
- **Before**: current strategy language, or `(none)` for ADD
- **After**: proposed new language, or `(unchanged)` for NO CHANGE
- **Defense**: for `NO CHANGE` rows, a per-row reason why the existing strategy is sufficient given the new signals; `"no new signals"` is only valid if the namespace produced zero NEW artifacts in Phase 1

---

### Phase 5: Confirmation Gate

**STOP. Do not modify strategy.md.**

Present the complete proposal table.

> Confirm proposals? **YES / NO / REVISED**

Do not open strategy.md for writing until the user confirms YES.
If REVISED: incorporate user edits and re-present the full table for final confirmation.
If YES: apply changes and report the resulting diff.

---

## V-02

**Variation axis:** Output format — Defense basis temporal audit column (PRE-READ / POST-READ / POST-SIGNAL)
**Hypothesis:** Explicitly labeling when each inertia defense was constructed — relative to the signal-reading stages — creates an epistemic audit trail that distinguishes genuine prior justification from post-hoc rationalization; a NO CHANGE defense that only became articulable after the full signal pattern emerged is high-risk and must be flagged.

---

You are running `topic:plan` — strategy revision for a Signal topic.

---

### Step 1: Read strategy.md

Open `simulations/topic/[topic-name]/strategy.md`.

Note and cite:
- Strategy creation date
- Goal statement
- Every planned signal entry by namespace

---

### Step 2: Signal Inventory

Scan all 9 namespaces in `simulations/`:
`scout` / `draft` / `review` / `flow` / `trace` / `prove` / `listen` / `program` / `topic`

Produce a single inventory table:

| Namespace | Filename | Date | Status | Content summary |
|-----------|----------|------|--------|-----------------|

**Status**: `NEW` (not referenced in strategy) or `PRIOR` (strategy references it)

---

### Step 3: Delta Detection

For every NEW artifact:
- Classify as `CONFIRMS` / `EXPANDS` / `CHALLENGES`
- Name the strategy date; only NEW artifacts drive proposals

Complete classification before producing proposals.

---

### Step 4: Proposals with Temporal Defense Audit

Produce a proposal table with the following columns:

| Namespace | Proposal type | Evidence | Before | After | Defense basis | Defense timing |
|-----------|--------------|----------|--------|-------|---------------|----------------|

Column rules:
- **Proposal type**: `ADD` / `REMOVE` / `REPRIORITIZE` / `NO CHANGE`; every namespace needs a row
- **Evidence**: artifact filename — required for every non-null proposal
- **Before**: current strategy entry verbatim, or `(none)` for ADD
- **After**: proposed new entry, or `(unchanged)` for NO CHANGE
- **Defense basis**: reason for the proposal or for inertia
- **Defense timing**: temporal label — one of `PRE-READ` / `POST-READ` / `POST-SIGNAL`

**Temporal legend:**

| Label | Meaning |
|-------|---------|
| `PRE-READ` | You could have stated this defense before reading any signal artifacts today |
| `POST-READ` | You formed this defense while reading artifacts, before the signal pattern became clear |
| `POST-SIGNAL` | You formed this defense only after the full pattern of signals made the conclusion visible |

**Flag rule:** Any `NO CHANGE` row with `POST-SIGNAL` defense timing is high-risk rationalization. Mark these rows explicitly: `⚠ POST-SIGNAL NO CHANGE`.

---

### Step 5: Confirmation Gate

**STOP. Do not modify strategy.md.**

Present the complete proposal table, including Defense timing column and any flagged rows.

> Confirm proposals? **YES / NO / REVISED**

Await user response before making any file changes.

---

## V-03

**Variation axis:** Lifecycle emphasis — numbered phases with Gate-0 completeness check before proposals
**Hypothesis:** A named Gate-0 that requires every namespace schema and the pre-proposal evaluation step to be populated before any proposal is written prevents premature proposal generation; the numbered gate makes the completeness requirement independently scannable and enforceable.

---

You are running `topic:plan` — strategy revision for a Signal topic.

---

## Phase −1: Schema Declaration

Before executing, declare the schemas you will populate:

```
§1   Signal inventory — scout namespace
§2   Signal inventory — draft namespace
§3   Signal inventory — review namespace
§4   Signal inventory — flow namespace
§5   Signal inventory — trace namespace
§6   Signal inventory — prove namespace
§7   Signal inventory — listen namespace
§8   Signal inventory — program namespace
§9   Signal inventory — topic namespace
§10  Strategy read (date, goal, planned signals)
§11  Pre-proposal delta classification
```

---

### Gate-0: Schema Completeness

Gate-0 passes when all 11 confirmed:

> **namespace schemas [§1][§2][§3][§4][§5][§6][§7][§8][§9] all populated + strategy read [§10] complete + delta classification [§11] complete**
>
> Reading this condition line enumerates all 11 items required; no item may be inferred by range.

**GATE-0 PASS THRESHOLD:** passes when all 11 confirmed (9 declared namespace schemas + 2 procedural schemas = 11 items total); blocked by any single STOP result.

Do not begin Phase 1 until you have confirmed you will populate all 11 schemas.

---

## Phase 1: Read strategy.md (§10)

Open `simulations/topic/[topic-name]/strategy.md`.

Record and cite:
- Strategy creation date (name it explicitly)
- Goal statement
- Every planned signal entry by namespace

---

## Phase 2: Signal Inventory (§1–§9)

For each of the 9 namespaces, scan `simulations/{namespace}/` and list every artifact:

| Namespace | Filename | Date | Status | Content summary |
|-----------|----------|------|--------|-----------------|

**Status**: `NEW` (no strategy reference) or `PRIOR` (strategy references it)

Complete all 9 namespace tables (§1–§9 all populated) before advancing.

---

## Phase 3: Pre-Proposal Delta Classification (§11)

For each NEW artifact, classify before writing any proposals:
- **CONFIRMS** — validates a planned signal
- **EXPANDS** — reveals a dimension outside strategy scope
- **CHALLENGES** — contradicts a strategy assumption

Gate-0 fires here: confirm all 11 schemas are populated before proceeding to Phase 4.

---

## Phase 4: Typed Change Proposals

Only NEW artifacts drive proposals. Every namespace needs a row.

| Namespace | Proposal type | Evidence | Before | After | Defense |
|-----------|--------------|----------|--------|-------|---------|

- **Proposal type**: `ADD` / `REMOVE` / `REPRIORITIZE` / `NO CHANGE`
- **Evidence**: artifact filename — required for all non-null proposals
- **Before/After**: strategy language — required for every row
- **Defense**: for NO CHANGE rows, per-row reason why status quo is sufficient; must be grounded in Phase 3 classification results

---

### Gate-1: Confirmation Gate

**STOP. Do not modify strategy.md.**

Present the complete proposal table.

> Confirm proposals? **YES / NO / REVISED**

Apply changes only after YES confirmation.

---

## V-04

**Variation axis:** Phrasing register — analytical/descriptive rather than imperative commands
**Hypothesis:** Framing the task as a structured reasoning exercise rather than a command sequence produces more thorough inertia justification and richer delta detection, because the model attends to the underlying reasoning rather than mechanical compliance.

---

You are performing a strategic revision analysis for a Signal topic.

Your goal is to determine whether the current strategy for this topic still reflects what the signals have revealed, and to produce specific, evidence-backed revision proposals that account for every namespace.

---

### What you are analyzing

A Signal topic strategy (`strategy.md`) names which namespaces to gather signals from, in what order, and toward what decision outcome. Over time, signals arrive that were not anticipated when the strategy was written. The task is to surface the gap between what the strategy expected and what the signals have actually revealed — and to propose changes only where that gap is meaningful.

---

### How to approach this

**Reading the strategy.** Open `simulations/topic/[topic-name]/strategy.md` and understand its structure: when it was written, what it expected to learn, what signals it planned to gather. Your output should cite at least one concrete reference to the strategy's structure — a quoted section header, a planned signal entry, or the goal statement — so it is clear you read the document rather than operating from inference.

**Inventorying the signals.** For each of the 9 namespaces — `scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic` — examine what artifact files actually exist in `simulations/{namespace}/`. For each artifact, record its filename, date, and a one-line content summary. Label each artifact as `NEW` (appeared after the strategy was written and not referenced in it) or `PRIOR` (the strategy already accounts for it). The inventory is a factual enumeration; do not make proposals yet.

**Analyzing the delta.** Only NEW artifacts carry information the strategy did not anticipate. For each NEW artifact, reason about what it tells you: does it confirm what the strategy expected, expand into territory the strategy did not anticipate, or challenge an assumption the strategy was built on? Completing this classification before writing proposals prevents the proposals from shaping the analysis.

---

### What to produce

A proposal table that addresses every namespace. Silence is not a null declaration — a namespace with no proposed changes still needs a row explaining why the current strategy is sufficient.

| Namespace | Proposal type | Evidence | Before | After | Inertia defense |
|-----------|--------------|----------|--------|-------|-----------------|

**Proposal type** must be one of `ADD`, `REMOVE`, `REPRIORITIZE`, or `NO CHANGE`. For every non-null proposal, the Evidence column must name the artifact filename that grounds it. The Before and After columns should carry the actual strategy language — verbatim where possible — so the proposed change is legible without opening strategy.md. For NO CHANGE rows, the Inertia defense column must contain a per-row reason why the current strategy is sufficient despite the new signal context; `"no change warranted"` is not sufficient — the reason must be grounded in the delta analysis.

---

### Before you modify anything

After producing the proposal table, present it to the user with this question:

> "Confirm proposals? YES / NO / REVISED"

Do not open `strategy.md` for writing until the user responds YES. If the user responds REVISED, incorporate their adjustments and re-present the table for a final confirmation pass. If YES, apply changes and report what changed.

---

## V-05

**Variation axis:** Combined — signals-first role sequence (V-01) + temporal defense audit (V-02) + numbered Gate-0 (V-03)
**Hypothesis:** The three axes address three distinct failure modes simultaneously: anchored detection (signals-first eliminates strategy priming), post-hoc rationalization (temporal audit makes construction timing visible), and incomplete inventory (Gate-0 enforces all 11 schemas before proposals); the combination is strictly more diagnostic than any single axis.

---

You are running `topic:plan` — strategy revision for a Signal topic.

**Your first action is the namespace inventory. Do not read strategy.md until Phase 2.**

---

## Phase −1: Schema Declaration

Declare schemas before reading any files:

```
§1   Signal inventory — scout namespace
§2   Signal inventory — draft namespace
§3   Signal inventory — review namespace
§4   Signal inventory — flow namespace
§5   Signal inventory — trace namespace
§6   Signal inventory — prove namespace
§7   Signal inventory — listen namespace
§8   Signal inventory — program namespace
§9   Signal inventory — topic namespace
§10  Strategy read (date, goal, planned signals)
§11  Pre-proposal delta classification
```

---

### Gate-0: Schema Completeness

Gate-0 passes when all 11 confirmed:

> **namespace schemas [§1][§2][§3][§4][§5][§6][§7][§8][§9] all populated + strategy read [§10] complete + delta classification [§11] complete**
>
> Reading this condition line enumerates all 11 items required; no item may be inferred by range.

**GATE-0 PASS THRESHOLD:** passes when all 11 confirmed (9 declared namespace schemas + 2 procedural schemas = 11 items total); blocked by any single STOP result.

---

## Phase 1: Signal Inventory (§1–§9) — before reading strategy.md

Scan all 9 namespaces in `simulations/`. **Do not open strategy.md yet.**

For each namespace, produce:

| Namespace | Filename | Date | Content summary |
|-----------|----------|------|-----------------|

Complete all 9 tables. Record the time impression label for each artifact as you read it:
- `PRE-READ` — impression formed before you have read strategy.md
- (all Phase 1 artifacts are necessarily PRE-READ)

---

## Phase 2: Read strategy.md (§10)

Now open `simulations/topic/[topic-name]/strategy.md`.

Record and cite:
- Strategy creation date (name it explicitly)
- Goal statement
- Every planned signal entry by namespace

---

## Phase 3: Delta Classification (§11)

Compare Phase 1 inventory against Phase 2 strategy.

Label each artifact:
- **PRIOR** — strategy references or planned for this artifact
- **NEW** — strategy does not reference this artifact

For each NEW artifact, classify:
- **CONFIRMS** / **EXPANDS** / **CHALLENGES**

Also record whether your classification impression formed as PRE-READ, POST-READ, or POST-SIGNAL (see legend below).

Gate-0: confirm all 11 schemas populated before proceeding.

---

## Phase 4: Typed Change Proposals with Temporal Defense Audit

Every namespace must have a row. Silence is not a null declaration.

| Namespace | Proposal type | Evidence | Before | After | Defense basis | Defense timing |
|-----------|--------------|----------|--------|-------|---------------|----------------|

Column rules:
- **Proposal type**: `ADD` / `REMOVE` / `REPRIORITIZE` / `NO CHANGE`
- **Evidence**: artifact filename — required for all non-null proposals
- **Before/After**: strategy language verbatim — required for every row
- **Defense basis**: reason for proposal or for inertia
- **Defense timing**: `PRE-READ` / `POST-READ` / `POST-SIGNAL`

**Temporal legend:**

| Label | When defense was articulable |
|-------|------------------------------|
| `PRE-READ` | Before reading any signal artifacts today |
| `POST-READ` | After reading artifacts, before the pattern became clear |
| `POST-SIGNAL` | Only after the full signal pattern was visible |

**Flag rule:** Any `NO CHANGE` row with `POST-SIGNAL` defense timing is high-risk rationalization. Mark explicitly: `⚠ POST-SIGNAL NO CHANGE`.

---

### Gate-1: Confirmation Gate

**STOP. Do not modify strategy.md.**

Present the complete proposal table — including Defense timing column and any flagged rows.

> Confirm proposals? **YES / NO / REVISED**

Apply changes only after YES confirmation.

---

## Variation Summary

| Variation | Axis | Key structural difference | C-58 coverage |
|-----------|------|--------------------------|---------------|
| V-01 | Role sequence | Signals-first: namespace inventory before strategy read | none |
| V-02 | Output format | Defense timing column with PRE-READ/POST-READ/POST-SIGNAL legend | **primary** |
| V-03 | Lifecycle emphasis | Numbered Gate-0 with 11-item schema declaration | none |
| V-04 | Phrasing register | Analytical/descriptive framing throughout | none |
| V-05 | Combined (V-01+V-02+V-03) | Signals-first + temporal audit + Gate-0 | **primary** |
