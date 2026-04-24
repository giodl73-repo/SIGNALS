# topic-new — Round 10 Variations (v9 rubric)

Five complete, runnable skill body prompts. Each is a standalone prompt body — not a diff against
a prior round. C-29/C-30/C-31 are structurally satisfied in all five; the variation axes determine
*how* each new criterion is satisfied, not *whether* it is.

---

## Variation Legend

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | C-29 consequence column as first-person failure narration | — | First-person "If I skip..." framing makes phase-level consequences personally salient rather than abstractly descriptive |
| V-02 | C-30 four-layer independence instruction with sequential-treatment consequence | — | Adding a consequence-of-sequential-treatment statement closes the last rationalization gap two-layer independence leaves open |
| V-03 | C-31 schema-row-order mirrors signal-table-column-order | — | F-01=Priority (schema-first) pre-conditions the model to place Priority first in the signal table before the template is reached |
| V-04 | C-29 status-quo-default column + C-30 named isolation-check + C-31 schema+table mirroring | Inertia framing | All three new criteria satisfied via shared behavioral-prediction architecture; consequence column names what teams default to, not just what breaks |
| V-05 | Imperative register (STOP/CHECK) targeted at all three new criteria enforcement points | Phrasing register | All-caps command markers at C-29/C-30/C-31 checkpoints make non-compliance register-visible; violation requires overriding an explicit command, not just ignoring a description |

---

## V-01 — C-29: First-Person Consequence Column

**Axis**: Single — C-29 framing.
**Hypothesis**: Labeling the pipeline overview consequence column "If I Skip This Phase, I Will..." and
writing each cell in first-person produces higher consequence salience than third-person "If Skipped"
cells. A model reading the overview encounters each phase's skip-cost as a self-directed prediction
rather than a passive failure mode, making the architectural consequence visible as personal operational
impact before Phase 1 begins.
**C-29**: "If I Skip This Phase, I Will..." column with first-person consequence cells.
**C-30**: Standard two-layer independence instruction ("Check these two items independently" + "Do not
advance until both are checked separately").
**C-31**: Priority as leftmost column in signal table; explicit label at Phase 6 states the ordering
rationale.

---

You are executing the `topic-new` skill for Signal. Your task: register a new topic in
`simulations/TOPICS.md` and write a strategy file at `simulations/{topic}/strategy.md`
that plans the signals needed to reach design commit.

---

## PIPELINE OVERVIEW

Read this entire table before executing Phase 1. All exit gate conditions are declared here.
Do not begin Phase 1 until you have read every row.

| Phase | Purpose | Produces | Exit Gate | If I Skip This Phase, I Will... |
|-------|---------|----------|-----------|---------------------------------|
| 1 | Identify who bears the risk if this strategy is wrong | Stakeholder fill-in table (S-01..S-N) | >= 3 rows filled; all 4 columns populated (checked independently) | ...have no source of truth for Owner Role; every role assignment in Phase 6 will be invented, not derived |
| 2 | Register the topic | One new row in simulations/TOPICS.md | Row contains topic name, status=active, strategy path | ...produce an orphaned strategy.md with no canonical registry entry; the topic will not be discoverable |
| 3 | Write the narrative rationale | ## Rationale in strategy.md | >= 2 sentences; names the design decision | ...produce a signal list with no stated purpose; the commit gate will have no decision it can be evaluated against |
| 4 | Establish artifact naming | ## Artifact Naming Convention in strategy.md | Pattern present; >= 1 parameterized example | ...name signals by intuition; cross-signal traceability breaks when names diverge |
| 5 | Pre-write validation — no signal rows yet | Schema compliance checkpoint | F-01--F-05 and COV-01--COV-03 held in working memory | ...produce rows that violate constraints I have not reviewed; Phase 6 and Phase 7 gates will catch failures that should not have been introduced |
| 6 | Produce signal plan rows | ## Signal Plan table in strategy.md | F-01--F-05 pass; COV-01--COV-03 pass | ...have a signal list that may not satisfy the structural requirements of a valid commit gate |
| 7 | Post-write validation | Schema re-check against produced rows | F-01--F-05 and COV-01--COV-03 independently verified | ...carry Phase 6 violations into the commit gate phase without detection |
| 8 | Define the commit gate | ## Commit Gate in strategy.md | Every essential signal named by item name; condition explicit | ...deliver a strategy with no defined stopping condition; the team will not know which signals must exist before design commit |

---

## FIELD SCHEMA

Every signal row in the signal plan table must satisfy all five field constraints.

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | Priority | Must be exactly: essential / recommended / optional — no other values, no substitutions, not "high/medium/low" | Row cannot be validated as a gate condition | Strategy cannot be parsed as a commit gate; team commits without a defined stopping condition |
| F-02 | Namespace | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic | Signal cannot be routed to the correct skill | Investigation stalls; skill owner has no namespace to operate from |
| F-03 | Item Name | Must follow {topic}-{signal}-{date}.md; use a parameterized template if the date is not yet known | Artifact cannot be located after the skill runs | Cross-signal traceability breaks; team cannot confirm the signal was produced |
| F-04 | Owner Role | A role description referencing the stakeholder category from Phase 1 | Owner is unresolvable; no one is assigned to gather the signal | Signals accumulate without owners; none get actioned before design commit |
| F-05 | Stakeholder Ref | Must contain the S-N identifier from Phase 1 that traces this signal to a risk bearer | Signal cannot be traced to a stakeholder at row level | C-08 cannot be verified by inspection; reviewer must count distinct roles manually |

---

## COVERAGE SCHEMA

After all signal rows are written, the complete set must satisfy all three coverage constraints.

| ID | Constraint | Rule | Immediate Failure | Downstream Effect |
|----|-----------|------|-------------------|-------------------|
| COV-01 | Essential minimum | At least one signal is marked essential | Strategy has no commit gate threshold | Investigation continues indefinitely or stops arbitrarily |
| COV-02 | Namespace breadth | Signals span at least 2 distinct namespaces | Strategy investigates one facet only | Design commit happens without evidence from adjacent investigation dimensions |
| COV-03 | Role differentiation | At least 2 distinct owner roles appear, each tracing to a distinct S-N row | Signal ownership is concentrated in one role | Strategy represents one stakeholder's view; adjacent risk bearers contribute no signals |

---

## Phase 1 — Stakeholder Identification

WHO BEARS THE RISK if this topic's strategy is wrong?

Fill in this table before writing anything else. Identify every stakeholder role whose work,
decisions, or commitments would be affected if the signals in this strategy turn out to be wrong,
incomplete, or gathered too late.

| S-N | Role | What They Decide Using These Signals | Risk If Signals Are Wrong |
|-----|------|--------------------------------------|---------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

Add rows as needed. Owner Role values in Phase 6 must trace back to an S-N row in this table.

**Phase 1 Exit Gate — Check these two items independently**

- [ ] (1) >= 3 rows filled
- [ ] (2) All four columns populated in every filled row

Do not advance to Phase 2 until both items are checked separately. Satisfying (1) does not
imply (2); check them as independent pass/fail conditions.

---

## Phase 2 — TOPICS.md Registration

Append to `simulations/TOPICS.md`:

```
| {topic} | active | simulations/{topic}/strategy.md |
```

**Phase 2 Exit Gate**

- [ ] TOPICS.md contains a row for this topic
- [ ] Status = active
- [ ] Path = simulations/{topic}/strategy.md

---

## Phase 3 — Narrative Rationale

Write `## Rationale` in `simulations/{topic}/strategy.md`.

Requirements:
- >= 2 sentences
- Name the specific design decision these signals inform
- Name the assumption teams make when they skip this investigation (the status-quo default)

**Phase 3 Exit Gate**

- [ ] ## Rationale section present
- [ ] >= 2 sentences
- [ ] A specific design decision named
- [ ] The status-quo assumption named

---

## Phase 4 — Artifact Naming Convention

Write `## Artifact Naming Convention` in strategy.md.

Pattern: `{topic}-{signal}-{date}.md`

Include at least one parameterized example using the actual topic name.

**Phase 4 Exit Gate**

- [ ] ## Artifact Naming Convention section present
- [ ] Pattern uses {topic}-{signal}-{date}.md
- [ ] >= 1 parameterized example present

---

## Phase 5 — Pre-Write Validation

Before producing any signal rows, confirm compliance with FIELD SCHEMA and COVERAGE SCHEMA.
Review every constraint:
- F-01: Priority restricted to essential / recommended / optional
- F-02: Namespace from canonical list
- F-03: Item names follow {topic}-{signal}-{date}.md
- F-04: Owner Role traceable to Phase 1
- F-05: Stakeholder Ref contains S-N identifier
- COV-01: At least one essential signal required
- COV-02: At least 2 namespaces required
- COV-03: At least 2 distinct owner roles required

**Phase 5 Exit Gate**

- [ ] F-01 through F-05 held in working memory
- [ ] COV-01 through COV-03 held in working memory
- [ ] No signal rows written yet

---

## Phase 6 — Signal Plan Production

Write `## Signal Plan` in strategy.md.

Produce a table with the following columns in this exact order:

**Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role**

Priority is the leftmost column. This order is not optional. Priority must appear before Namespace
and Skill so that the field most likely to receive an invalid value (F-01) is filled before any
other field can establish contextual framing that induces vocabulary substitution.

Constraints:
- Priority: essential / recommended / optional only (F-01)
- Namespace: from canonical list (F-02)
- Item Name: {topic}-{signal}-{date}.md pattern (F-03)
- Owner Role: role description (F-04)
- Stakeholder Ref: S-N identifier from Phase 1 (F-05)

**Phase 6 Exit Gate** — cite F-01--F-05 and COV-01--COV-03

- [ ] F-01: all Priority cells contain essential / recommended / optional only
- [ ] F-02: all Namespace cells are from the canonical list
- [ ] F-03: all Item Name cells follow {topic}-{signal}-{date}.md
- [ ] F-04: all Owner Role cells are filled
- [ ] F-05: all Stakeholder Ref cells contain an S-N identifier
- [ ] COV-01: at least one signal marked essential
- [ ] COV-02: at least 2 distinct namespaces present
- [ ] COV-03: at least 2 distinct owner roles, each tracing to a distinct S-N row

---

## Phase 7 — Post-Write Validation

Do not add any new rows. Verify the completed signal plan against all schema constraints.

**Phase 7 Exit Gate** — F-01--F-05 and COV-01--COV-03 independently re-verified

- [ ] F-01: every Priority cell = essential / recommended / optional
- [ ] F-02: every Namespace cell is canonical
- [ ] F-03: every Item Name follows the pattern
- [ ] F-04: every Owner Role cell filled
- [ ] F-05: every Stakeholder Ref contains S-N identifier
- [ ] COV-01: at least one essential
- [ ] COV-02: at least 2 distinct namespaces
- [ ] COV-03: at least 2 distinct owner roles tracing to distinct S-N rows

---

## Phase 8 — Commit Gate (Dedicated Phase)

This phase is dedicated to the commit gate definition. It is separate from signal plan production.
Do not write new signal rows here.

Write `## Commit Gate` in strategy.md.

State which specific signals must exist before design commit. Name every essential signal by its
item name — not by count. Write the condition explicitly:

> "Design commit requires the following signals to be present: [list each essential signal by item name]."

**Phase 8 Exit Gate**

- [ ] ## Commit Gate section present and separate from ## Signal Plan
- [ ] Every essential signal named by item name
- [ ] Condition stated as an explicit design commit requirement
- [ ] No new signal rows present in this section

---

---

## V-02 — C-30: Four-Layer Independence Instruction

**Axis**: Single — C-30 depth.
**Hypothesis**: A four-layer independence instruction at the Phase 1 exit gate — (1) pre-label naming
the evaluation mode, (2) numbered conditions, (3) prohibition against sequential treatment, (4)
consequence statement describing the specific false-pass produced by sequential checking — closes the
rationalization gap that two-layer and three-layer instructions leave open. Two conditions that share
a checkbox list can be treated as a sequence even when labeled "independently"; naming the false-pass
(row count passes, columns empty, sequential checker advances) makes the evaluation-mode instruction
operationally specific rather than semantically general.
**C-29**: Standard "If Skipped" column with third-person failure-mode cells.
**C-30**: Four-layer independence instruction: mode-label + enumerated conditions + sequential-treatment
prohibition + consequence of sequential checking.
**C-31**: Priority as leftmost column in signal table; explicit label at Phase 6.

---

You are executing the `topic-new` skill for Signal. Your task: register a new topic in
`simulations/TOPICS.md` and write a strategy file at `simulations/{topic}/strategy.md`
that plans the signals needed to reach design commit.

---

## PIPELINE OVERVIEW

Read this entire table before executing Phase 1. All exit gate conditions are declared here.
Do not begin Phase 1 until you have read every row.

| Phase | Purpose | Produces | Exit Gate | If Skipped |
|-------|---------|----------|-----------|-----------:|
| 1 | Identify who bears the risk | Stakeholder fill-in table (S-01..S-N) | >= 3 rows filled; all 4 columns populated (checked independently) | No source of truth for Owner Role; all Phase 6 role assignments will be invented |
| 2 | Register the topic | One new row in simulations/TOPICS.md | Row has topic name, status=active, path | Strategy.md is an orphaned file; topic not in registry |
| 3 | Write narrative rationale | ## Rationale in strategy.md | >= 2 sentences; names the design decision | Signal list has no stated purpose; commit gate has no evaluable decision |
| 4 | Establish artifact naming | ## Artifact Naming Convention in strategy.md | Pattern and >= 1 example present | Signals named by intuition; traceability breaks |
| 5 | Pre-write validation | Schema compliance checkpoint | F-01--F-05 and COV-01--COV-03 reviewed | Constraint violations introduced before gates can catch them |
| 6 | Produce signal plan | ## Signal Plan table in strategy.md | F-01--F-05 pass; COV-01--COV-03 pass | Signal list may not satisfy commit gate structural requirements |
| 7 | Post-write validation | Schema re-check | F-01--F-05 and COV-01--COV-03 re-verified | Violations carry forward to commit gate phase undetected |
| 8 | Define commit gate | ## Commit Gate in strategy.md | Every essential signal named by item name; condition explicit | Strategy has no stopping condition; team cannot evaluate readiness |

---

## FIELD SCHEMA

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | Priority | Must be exactly: essential / recommended / optional — no substitutions | Row cannot be validated as a gate condition | Strategy cannot be parsed as a commit gate; team commits without a stopping condition |
| F-02 | Namespace | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic | Signal cannot be routed | Investigation stalls; skill owner has no namespace to operate from |
| F-03 | Item Name | Must follow {topic}-{signal}-{date}.md | Artifact cannot be located | Traceability breaks; team cannot confirm signal was produced |
| F-04 | Owner Role | A role description traceable to Phase 1 stakeholder categories | Owner unresolvable | Signals accumulate without owners; none actioned before commit |
| F-05 | Stakeholder Ref | S-N identifier from Phase 1 | Signal not traceable at row level | C-08 unverifiable by inspection |

---

## COVERAGE SCHEMA

| ID | Constraint | Rule | Immediate Failure | Downstream Effect |
|----|-----------|------|-------------------|-------------------|
| COV-01 | Essential minimum | At least one signal marked essential | No commit gate threshold | Investigation continues indefinitely |
| COV-02 | Namespace breadth | Signals span at least 2 distinct namespaces | One-dimensional investigation | Design commit without evidence from adjacent dimensions |
| COV-03 | Role differentiation | At least 2 distinct owner roles, each tracing to a distinct S-N row | Single-stakeholder view | Adjacent risk bearers contribute no signals |

---

## Phase 1 — Stakeholder Identification

WHO BEARS THE RISK if this topic's strategy is wrong?

Fill in this table before writing anything else.

| S-N | Role | What They Decide Using These Signals | Risk If Signals Are Wrong |
|-----|------|--------------------------------------|---------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

Add rows as needed. Owner Role values in Phase 6 must trace back to an S-N row here.

**Phase 1 Exit Gate — Evaluate these as independent conditions, not a sequence**

These two conditions must be checked as isolated pass/fail evaluations. Do not advance because
one condition passes; each condition must be independently satisfied before you proceed.

- [ ] (1) >= 3 rows filled
- [ ] (2) All four columns populated in every filled row

Do not advance to Phase 2 until both conditions are independently satisfied. Sequential treatment
produces a false pass: checking (1), finding it satisfied, and then moving to (2) in the same
scan is a sequential check — it allows a table with 3 rows but empty cells to pass because the
row-count check anchors the evaluation. Independent checking means: evaluate (1) to a result,
reset, then evaluate (2) to a result without reference to (1).

---

## Phase 2 — TOPICS.md Registration

Append to `simulations/TOPICS.md`:

```
| {topic} | active | simulations/{topic}/strategy.md |
```

**Phase 2 Exit Gate**

- [ ] TOPICS.md contains a row for this topic
- [ ] Status = active
- [ ] Path = simulations/{topic}/strategy.md

---

## Phase 3 — Narrative Rationale

Write `## Rationale` in strategy.md. Requirements: >= 2 sentences; name the specific design decision
these signals inform; name the status-quo assumption this investigation supersedes.

**Phase 3 Exit Gate**

- [ ] ## Rationale present; >= 2 sentences; design decision named; status-quo assumption named

---

## Phase 4 — Artifact Naming Convention

Write `## Artifact Naming Convention` in strategy.md. Pattern: `{topic}-{signal}-{date}.md`.
Include >= 1 parameterized example.

**Phase 4 Exit Gate**

- [ ] ## Artifact Naming Convention present; pattern correct; >= 1 example

---

## Phase 5 — Pre-Write Validation

Confirm every constraint before producing signal rows:
- F-01: Priority = essential / recommended / optional only
- F-02: Namespace from canonical list
- F-03: Item Name follows {topic}-{signal}-{date}.md
- F-04: Owner Role traceable to Phase 1
- F-05: Stakeholder Ref contains S-N identifier
- COV-01: At least one essential required
- COV-02: At least 2 namespaces required
- COV-03: At least 2 distinct owner roles required

**Phase 5 Exit Gate**

- [ ] F-01--F-05 and COV-01--COV-03 reviewed; no signal rows written yet

---

## Phase 6 — Signal Plan Production

Write `## Signal Plan` in strategy.md.

Produce a table with the following columns in this exact order:

**Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role**

Priority is the leftmost column. This order is structural, not stylistic: Priority must appear
before all other fields so that the field associated with the hardest failure mode (F-01 priority
vocabulary substitution) is filled before Namespace or Skill values can establish contextual
framing that might induce invalid vocabulary.

**Phase 6 Exit Gate** — cite F-01--F-05 and COV-01--COV-03

- [ ] F-01: all Priority cells contain essential / recommended / optional only
- [ ] F-02: all Namespace cells canonical
- [ ] F-03: all Item Name cells follow pattern
- [ ] F-04: all Owner Role cells filled
- [ ] F-05: all Stakeholder Ref cells contain S-N identifier
- [ ] COV-01: at least one essential
- [ ] COV-02: at least 2 distinct namespaces
- [ ] COV-03: at least 2 distinct owner roles tracing to distinct S-N rows

---

## Phase 7 — Post-Write Validation

Do not add rows. Re-verify against all schema constraints.

**Phase 7 Exit Gate** — F-01--F-05 and COV-01--COV-03 independently re-verified

- [ ] F-01 through F-05 and COV-01 through COV-03 verified against produced rows

---

## Phase 8 — Commit Gate (Dedicated Phase)

This phase is separate from signal plan production. Do not write new signal rows here.

Write `## Commit Gate` in strategy.md. Name every essential signal by item name. State the
condition explicitly: "Design commit requires the following signals to be present: [list]."

**Phase 8 Exit Gate**

- [ ] ## Commit Gate present and separate from ## Signal Plan
- [ ] Every essential signal named by item name
- [ ] Condition stated as explicit design commit requirement
- [ ] No new signal rows in this section

---

---

## V-03 — C-31: Schema-Row-Order Mirrors Signal-Table-Column-Order

**Axis**: Single — C-31 enforcement architecture.
**Hypothesis**: If FIELD SCHEMA lists F-01=Priority as its first row — and the schema row order
is the same as the signal table column order (F-01 Priority, F-02 Namespace, F-03 Skill, F-04
Item Name, F-05 Owner Role) — then a model reading the schema before reaching the signal table
template is pre-conditioned to place Priority first. The schema encounter pre-loads priority-first
as the canonical structure; when the table template appears, the column order is already established
in working memory rather than being encountered fresh at the point of potential substitution.
**C-29**: Standard "If Skipped" column in pipeline overview.
**C-30**: Standard two-layer independence instruction.
**C-31**: F-01=Priority in FIELD SCHEMA (schema row order = table column order); explicit note at
Phase 6 that schema row order is the signal for table column order.

---

You are executing the `topic-new` skill for Signal. Your task: register a new topic in
`simulations/TOPICS.md` and write a strategy file at `simulations/{topic}/strategy.md`
that plans the signals needed to reach design commit.

---

## PIPELINE OVERVIEW

Read this entire table before executing Phase 1. All exit gate conditions are declared here.
Do not begin Phase 1 until you have read every row.

| Phase | Purpose | Produces | Exit Gate | If Skipped |
|-------|---------|----------|-----------|-----------:|
| 1 | Identify stakeholders | Stakeholder fill-in table (S-01..S-N) | >= 3 rows filled; all 4 columns populated (checked independently) | No source of truth for Owner Role; role assignments will be invented |
| 2 | Register the topic | One new row in simulations/TOPICS.md | Row has topic name, status=active, path | Orphaned strategy.md; topic absent from registry |
| 3 | Write rationale | ## Rationale in strategy.md | >= 2 sentences; names design decision | Signal list has no purpose; commit gate has no evaluable decision |
| 4 | Establish artifact naming | ## Artifact Naming Convention in strategy.md | Pattern and >= 1 example present | Signals named by intuition; traceability breaks |
| 5 | Pre-write validation | Schema checkpoint | F-01--F-05 and COV-01--COV-03 reviewed | Violations introduced before gates can detect them |
| 6 | Produce signal plan | ## Signal Plan table in strategy.md | F-01--F-05 pass; COV-01--COV-03 pass | Signal list may not satisfy commit gate requirements |
| 7 | Post-write validation | Schema re-check | F-01--F-05 and COV-01--COV-03 re-verified | Violations carry forward undetected |
| 8 | Define commit gate | ## Commit Gate in strategy.md | Every essential signal named; condition explicit | Strategy has no stopping condition |

---

## FIELD SCHEMA

Schema row order defines signal table column order. The leftmost column in your signal plan
table corresponds to F-01; the second column to F-02; and so on. F-01 is Priority — it is
both the first schema constraint and the first column you will fill when populating a signal row.

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | **Priority** | Must be exactly: essential / recommended / optional — no substitutions, not "high/medium/low" | Row cannot be validated as a gate condition | Strategy cannot be parsed as a commit gate; team commits without a stopping condition |
| F-02 | Namespace | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic | Signal cannot be routed | Investigation stalls |
| F-03 | Skill | Identifies the specific skill within the namespace | Signal cannot be assigned | No execution path for the signal |
| F-04 | Item Name | Must follow {topic}-{signal}-{date}.md | Artifact cannot be located | Traceability breaks |
| F-05 | Owner Role | Role description traceable to Phase 1 stakeholder category | Owner unresolvable | Signal goes unactioned |

Note: A Stakeholder Ref column (S-N identifier) must also appear in the signal table. It does
not have a corresponding schema row because it is a traceability pointer, not a fill field.
Place it between Item Name and Owner Role: Priority | Namespace | Skill | Item Name |
Stakeholder Ref | Owner Role.

---

## COVERAGE SCHEMA

| ID | Constraint | Rule | Immediate Failure | Downstream Effect |
|----|-----------|------|-------------------|-------------------|
| COV-01 | Essential minimum | At least one signal marked essential | No commit gate threshold | Investigation continues indefinitely |
| COV-02 | Namespace breadth | Signals span at least 2 distinct namespaces | One-dimensional investigation | Commit without evidence from adjacent dimensions |
| COV-03 | Role differentiation | At least 2 distinct owner roles, each tracing to a distinct S-N row | Single-stakeholder view | Adjacent risk bearers contribute nothing |

---

## Phase 1 — Stakeholder Identification

WHO BEARS THE RISK if this topic's strategy is wrong?

Fill in this table before writing anything else.

| S-N | Role | What They Decide Using These Signals | Risk If Signals Are Wrong |
|-----|------|--------------------------------------|---------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

Add rows as needed. Owner Role values in Phase 6 must trace back to an S-N row here.

**Phase 1 Exit Gate — Check these two items independently**

- [ ] (1) >= 3 rows filled
- [ ] (2) All four columns populated in every filled row

Do not advance to Phase 2 until both items are checked separately.

---

## Phase 2 — TOPICS.md Registration

Append to `simulations/TOPICS.md`:

```
| {topic} | active | simulations/{topic}/strategy.md |
```

**Phase 2 Exit Gate**

- [ ] TOPICS.md contains row; status=active; path correct

---

## Phase 3 — Narrative Rationale

Write `## Rationale` in strategy.md. Requirements: >= 2 sentences; name the specific design
decision; name the status-quo assumption this investigation supersedes.

**Phase 3 Exit Gate**

- [ ] ## Rationale present; >= 2 sentences; design decision named; status-quo assumption named

---

## Phase 4 — Artifact Naming Convention

Write `## Artifact Naming Convention` in strategy.md. Pattern: `{topic}-{signal}-{date}.md`.
Include >= 1 parameterized example.

**Phase 4 Exit Gate**

- [ ] Section present; pattern correct; >= 1 example

---

## Phase 5 — Pre-Write Validation

Review all schema constraints before writing rows:
- F-01 (Priority): essential / recommended / optional only — this is the first field you will fill
- F-02 (Namespace): from canonical list
- F-03 (Skill): identifies the skill within the namespace
- F-04 (Item Name): {topic}-{signal}-{date}.md
- F-05 (Owner Role): traceable to Phase 1 S-N row
- COV-01: at least one essential required
- COV-02: at least 2 namespaces required
- COV-03: at least 2 distinct owner roles required

**Phase 5 Exit Gate**

- [ ] F-01--F-05 and COV-01--COV-03 reviewed; no signal rows written yet

---

## Phase 6 — Signal Plan Production

Write `## Signal Plan` in strategy.md.

Produce a table with columns in the following order — which matches the FIELD SCHEMA row order
(F-01 through F-05) with Stakeholder Ref inserted after Item Name:

**Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role**

F-01 (Priority) is the first schema row and the first table column. Fill Priority before filling
any other field. A model filling rows left to right encounters Priority as the first decision,
before Namespace or Skill values exist to anchor contextual framing.

**Phase 6 Exit Gate** — cite F-01--F-05 and COV-01--COV-03

- [ ] F-01: all Priority cells contain essential / recommended / optional only
- [ ] F-02: all Namespace cells canonical
- [ ] F-03: all Skill cells present
- [ ] F-04: all Item Name cells follow {topic}-{signal}-{date}.md
- [ ] F-05: all Owner Role cells filled and traceable
- [ ] Stakeholder Ref: all cells contain S-N identifier
- [ ] COV-01: at least one essential
- [ ] COV-02: at least 2 distinct namespaces
- [ ] COV-03: at least 2 distinct owner roles tracing to distinct S-N rows

---

## Phase 7 — Post-Write Validation

Do not add rows. Re-verify all constraints against produced rows.

**Phase 7 Exit Gate** — F-01--F-05 and COV-01--COV-03 independently re-verified

- [ ] All F-NN and COV-NN constraints satisfied by every row and the full set

---

## Phase 8 — Commit Gate (Dedicated Phase)

This phase is separate from signal plan production. Write `## Commit Gate` in strategy.md.
Name every essential signal by item name. State the condition explicitly:
"Design commit requires: [list essential signals by item name]."

**Phase 8 Exit Gate**

- [ ] ## Commit Gate present and separate from ## Signal Plan
- [ ] Every essential signal named by item name
- [ ] Condition stated as explicit design commit requirement

---

---

## V-04 — Combined: Status-Quo-Default Consequence Column + Named Isolation Check + Schema+Table Priority-First

**Axes**: C-29 via behavioral-prediction framing + C-30 via named isolation-check construct +
C-31 via schema-row mirroring + inertia framing.
**Hypothesis**: C-29 is strongest when the consequence column names the behavioral default teams
revert to when a phase is skipped (not just "what breaks" but "what teams do instead") — because
identifying the default substitution is actionable in a way that abstract failure descriptions
are not. Combined with C-30 implemented as a named formal construct ("ISOLATION CHECK") at the
Phase 1 gate and C-31 enforced at both the schema level (F-01=Priority) and the table level
(explicit column order label), all three new criteria share a common behavioral-prediction
architecture: each names the default behavior being superseded, not just the rule being enforced.
**C-29**: "Status-Quo Default (if phase skipped)" column — names what teams do when they skip
each phase, not just what breaks.
**C-30**: "ISOLATION CHECK" as a named formal construct preceding the two conditions; closing
statement: "Do not advance until both conditions pass an independent evaluation."
**C-31**: F-01=Priority in FIELD SCHEMA; signal table column order explicit at Phase 6 with
inertia note.

---

You are executing the `topic-new` skill for Signal. Your task: register a new topic in
`simulations/TOPICS.md` and write a strategy file at `simulations/{topic}/strategy.md`
that plans the signals needed to reach design commit.

---

## PIPELINE OVERVIEW

Read the full overview before starting. The cost of skipping each phase is visible in every row.
Do not begin Phase 1 until you have read every entry.

| Phase | Purpose | Produces | Exit Gate | Status-Quo Default (if phase skipped) |
|-------|---------|----------|-----------|-----------------------------------------|
| 1 | Identify who bears the risk | Stakeholder fill-in table (S-01..S-N) | >= 3 rows filled; all 4 columns populated (ISOLATION CHECK — see Phase 1) | Teams list generic roles ("PM", "eng") without tracing them to actual stakeholders; Owner Role column in Phase 6 is filled from intuition |
| 2 | Register the topic | One new row in simulations/TOPICS.md | Row has topic name, status=active, path | Topics are created ad-hoc without registry entries; strategy files are discovered by directory scan, not by canonical reference |
| 3 | Write rationale | ## Rationale in strategy.md | >= 2 sentences; names the design decision and the status-quo assumption | Strategy reads as a signal list with no stated decision; teams commit to building without knowing which signals were meant to inform that decision |
| 4 | Establish artifact naming | ## Artifact Naming Convention in strategy.md | Pattern and >= 1 example present | Signals are named by convention-of-the-moment; names diverge across runs; the team cannot tell whether a signal was produced or just named differently |
| 5 | Pre-write validation | Schema checkpoint | F-01--F-05 and COV-01--COV-03 reviewed | Teams write signal rows before reviewing constraints; F-01 violations (high/medium/low) are introduced in the first row and then repeated across the table before any gate fires |
| 6 | Produce signal plan | ## Signal Plan table in strategy.md | F-01--F-05 pass; COV-01--COV-03 pass | Signal list is produced without structural enforcement; team uses the strategy as-is; commit gate is evaluated by judgment, not by inspection |
| 7 | Post-write validation | Schema re-check | F-01--F-05 and COV-01--COV-03 re-verified | First-pass violations carry forward; team discovers them only when trying to evaluate the commit gate |
| 8 | Define commit gate | ## Commit Gate in strategy.md | Every essential signal named by item name; condition explicit | Commit gate is stated as a count ("we need 3 signals") rather than as named items; team cannot check off specific signals; "done" is undefined |

---

## FIELD SCHEMA

Schema row order defines signal table column order. F-01 is Priority — it is the first
constraint row and the first column in the signal table. Fill Priority before any other field.

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | **Priority** | Must be exactly: essential / recommended / optional — no substitutions. Teams default to "high/medium/low"; this is the most common F-01 failure. | Row cannot be validated as a gate condition | Strategy cannot be parsed as a commit gate; team uses judgment to decide when to stop, which means they never stop with confidence |
| F-02 | Namespace | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic | Signal cannot be routed | Skill owner has no namespace; investigation stalls at assignment |
| F-03 | Skill | Specific skill within the namespace | Signal cannot be assigned to a skill | No execution path; signal is aspirational but not actionable |
| F-04 | Item Name | Must follow {topic}-{signal}-{date}.md | Artifact unlocatable | Traceability breaks; team cannot confirm signal was produced |
| F-05 | Owner Role | Role description traceable to Phase 1 stakeholder category | Owner unresolvable | Signals accumulate; no one is responsible; none are actioned |

Note: A Stakeholder Ref column (S-N identifier from Phase 1) must appear in the signal table.
It is a traceability pointer, not a fill constraint. Position: after Item Name.
Signal table column order: **Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role**

---

## COVERAGE SCHEMA

| ID | Constraint | Rule | Immediate Failure | Downstream Effect |
|----|-----------|------|-------------------|-------------------|
| COV-01 | Essential minimum | At least one signal marked essential | No commit gate threshold | Teams default to treating all signals as optional; investigation continues until calendar pressure forces a stop |
| COV-02 | Namespace breadth | At least 2 distinct namespaces | Investigation is one-dimensional | Design commit without evidence from adjacent risk dimensions; undiscovered constraints surface post-commit |
| COV-03 | Role differentiation | At least 2 distinct owner roles, tracing to distinct S-N rows | Single-stakeholder ownership | Only one discipline contributes signals; team commits without cross-disciplinary evidence |

---

## Phase 1 — Stakeholder Identification

WHO BEARS THE RISK if this topic's strategy is wrong?

Fill in this table before writing anything else. Identify every stakeholder role whose work,
decisions, or commitments would be affected if the signals in this strategy are wrong, incomplete,
or gathered too late.

| S-N | Role | What They Decide Using These Signals | Risk If Signals Are Wrong |
|-----|------|--------------------------------------|---------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

Add rows as needed. Owner Role assignments in Phase 6 must trace back to an S-N row here.

**Phase 1 Exit Gate — ISOLATION CHECK**

Evaluate each condition independently. An independent evaluation means: reach a pass/fail result
for condition (1) before considering condition (2), and vice versa. Do not let the result of one
condition influence the evaluation of the other.

- [ ] (1) >= 3 rows filled
- [ ] (2) All four columns populated in every filled row

Do not advance to Phase 2 until both conditions pass an independent evaluation. A table with 3
rows but empty cells passes condition (1); it fails condition (2). Independent checking catches
this; sequential checking may not.

---

## Phase 2 — TOPICS.md Registration

Append to `simulations/TOPICS.md`:

```
| {topic} | active | simulations/{topic}/strategy.md |
```

**Phase 2 Exit Gate**

- [ ] Row present; status=active; path=simulations/{topic}/strategy.md

---

## Phase 3 — Narrative Rationale

Write `## Rationale` in strategy.md.

Requirements:
- >= 2 sentences
- Name the specific design decision these signals inform
- Name the status-quo assumption this investigation supersedes (what do teams currently assume
  when they skip this investigation?)

**Phase 3 Exit Gate**

- [ ] ## Rationale present; >= 2 sentences; design decision named; status-quo assumption named

---

## Phase 4 — Artifact Naming Convention

Write `## Artifact Naming Convention` in strategy.md. Pattern: `{topic}-{signal}-{date}.md`.
Include >= 1 parameterized example using the actual topic name.

**Phase 4 Exit Gate**

- [ ] Section present; pattern correct; >= 1 example

---

## Phase 5 — Pre-Write Validation

Review all constraints before writing signal rows. F-01 (Priority) is the first constraint and
the first column — the most common failure mode is here.

- F-01: essential / recommended / optional only (not "high/medium/low")
- F-02: namespace from canonical list
- F-03: skill within namespace
- F-04: item name follows {topic}-{signal}-{date}.md
- F-05: owner role traceable to Phase 1
- COV-01: at least one essential required
- COV-02: at least 2 namespaces required
- COV-03: at least 2 distinct owner roles required

**Phase 5 Exit Gate**

- [ ] F-01--F-05 and COV-01--COV-03 reviewed; no signal rows written yet

---

## Phase 6 — Signal Plan Production

Write `## Signal Plan` in strategy.md.

Column order — matching FIELD SCHEMA row order, with Stakeholder Ref after Item Name:

**Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role**

Priority goes first. Teams default to filling Namespace first, which anchors contextual
framing that makes "high/medium/low" feel natural before "essential/recommended/optional" is
considered. Priority-first eliminates that anchor. Fill Priority before any other field.

**Phase 6 Exit Gate** — F-01--F-05 and COV-01--COV-03

- [ ] F-01: all Priority = essential / recommended / optional
- [ ] F-02: all Namespace canonical
- [ ] F-03: all Skill cells present
- [ ] F-04: all Item Name cells follow pattern
- [ ] F-05: all Owner Role cells filled and traceable to Phase 1
- [ ] Stakeholder Ref: all cells contain S-N identifier
- [ ] COV-01: at least one essential
- [ ] COV-02: at least 2 distinct namespaces
- [ ] COV-03: at least 2 distinct owner roles tracing to distinct S-N rows

---

## Phase 7 — Post-Write Validation

Do not add rows. Re-verify all constraints against produced rows.

**Phase 7 Exit Gate** — F-01--F-05 and COV-01--COV-03 independently re-verified

- [ ] Every F-NN constraint satisfied by every row
- [ ] Every COV-NN constraint satisfied by the full signal set

---

## Phase 8 — Commit Gate (Dedicated Phase)

This phase is separate from signal plan production. Do not write new signal rows here.

Write `## Commit Gate` in strategy.md. Name every essential signal by item name — not by count.
The status-quo default is to state a count ("we need N signals"); naming specific items closes
that gap. Write: "Design commit requires: [list each essential signal by item name]."

**Phase 8 Exit Gate**

- [ ] ## Commit Gate present and separate from ## Signal Plan
- [ ] Every essential signal named by item name (not by count)
- [ ] Condition stated as an explicit design commit requirement
- [ ] No new signal rows in this section

---

---

## V-05 — Combined: Imperative Register Targeting All Three New Criteria Enforcement Points

**Axes**: Phrasing register (STOP/CHECK) + C-29 "SKIP COST" column + C-30 "INDEPENDENCE TEST"
gate label + C-31 "PRIORITY GOES FIRST" table preamble.
**Hypothesis**: Applying the imperative register specifically at the three new criteria enforcement
points — bold all-caps column header, gate label, and table preamble — creates register contrast
that makes non-compliance visible as a command override rather than a guideline violation. A model
that skips C-29 by omitting a consequence column must ignore a bold "SKIP COST" header; a model
that treats C-30 conditions sequentially must ignore "INDEPENDENCE TEST"; a model that puts
Namespace first in the signal table must ignore "PRIORITY GOES FIRST." Register contrast at the
enforcement point itself makes the cost of non-compliance structurally legible.
**C-29**: "SKIP COST" as bold column header in pipeline overview; terse all-caps failure mode per row.
**C-30**: "INDEPENDENCE TEST" as named gate label with STOP marker; explicit prohibition.
**C-31**: "PRIORITY GOES FIRST" as a bold preamble before the signal table column declaration.

---

You are executing the `topic-new` skill for Signal. Your task: register a new topic in
`simulations/TOPICS.md` and write a strategy file at `simulations/{topic}/strategy.md`
that plans the signals needed to reach design commit.

---

## PIPELINE OVERVIEW

**STOP. READ THIS PIPELINE BEFORE YOU START.**

Read every row below before executing Phase 1. Every exit gate condition and every skip cost for
every phase is declared in this table. Do not start Phase 1 until you have read all eight rows.

| Phase | What You Will Do | What You Will Produce | What You Must Check | **SKIP COST** |
|-------|-----------------|----------------------|---------------------|---------------|
| 1 | Identify stakeholders | Stakeholder fill-in table (S-01..S-N) | >= 3 rows filled; all 4 columns populated (INDEPENDENCE TEST) | **OWNER ROLE BECOMES FICTION** — no source of truth; all Phase 6 roles invented |
| 2 | Register the topic | One new row in simulations/TOPICS.md | Row has topic name, status=active, path | **STRATEGY IS ORPHANED** — not in registry; discovered only by directory scan |
| 3 | Write rationale | ## Rationale | >= 2 sentences; names the design decision | **COMMIT GATE HAS NO DECISION** — signal list exists; evaluable purpose does not |
| 4 | Establish artifact naming | ## Artifact Naming Convention | Pattern and >= 1 example | **NAMES DIVERGE** — convention-of-the-moment; traceability breaks |
| 5 | Pre-write validation | Schema checkpoint | F-01--F-05 and COV-01--COV-03 reviewed | **VIOLATIONS INTRODUCED BEFORE GATES FIRE** — F-01 failures baked in from row 1 |
| 6 | Produce signal plan | ## Signal Plan table | F-01--F-05 pass; COV-01--COV-03 pass | **COMMIT GATE IS UNEVALUABLE** — signal list without structural enforcement |
| 7 | Post-write validation | Schema re-check | F-01--F-05 and COV-01--COV-03 re-verified | **VIOLATIONS CARRY FORWARD** — discovered only at commit gate evaluation |
| 8 | Define commit gate | ## Commit Gate | Every essential signal named by item name; condition explicit | **NO STOPPING CONDITION** — team commits when calendar pressure peaks, not when evidence is complete |

---

## FIELD SCHEMA

| ID | Field | Rule | If Wrong Immediately | What That Causes Downstream |
|----|-------|------|---------------------|------------------------------|
| F-01 | Priority | Write exactly: essential OR recommended OR optional — nothing else. Not "high". Not "medium". Not "low". | Row cannot be validated as a gate condition | Team commits without knowing which signals must exist first; "done" is decided by pressure |
| F-02 | Namespace | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic | Signal cannot be routed | Skill owner has no namespace; investigation stalls at assignment |
| F-03 | Skill | Specific skill within namespace | No execution path for signal | Signal stays on the plan; never actioned |
| F-04 | Item Name | Must follow {topic}-{signal}-{date}.md | Artifact unlocatable | Team cannot confirm signal was produced; coverage unknown |
| F-05 | Owner Role | Role description traceable to Phase 1 S-N row | Owner unresolvable | Signal accumulates without an owner; never actioned before commit |

---

## COVERAGE SCHEMA

| ID | Constraint | Rule | If Wrong Immediately | What That Causes Downstream |
|----|-----------|------|---------------------|------------------------------|
| COV-01 | Essential minimum | At least one signal marked essential | No commit gate threshold | Investigation has no floor; continues until external pressure stops it |
| COV-02 | Namespace breadth | At least 2 distinct namespaces | One-dimensional investigation | Adjacent risks go unexamined; surface post-commit |
| COV-03 | Role differentiation | At least 2 distinct owner roles tracing to distinct S-N rows | Single point of ownership | One discipline's view; cross-disciplinary risks invisible |

---

## Phase 1 — Stakeholder Identification

ASK: WHO GETS HURT if this topic's strategy is wrong?

Fill in this table before writing anything else. Identify every stakeholder role whose work,
decisions, or commitments would be affected if the signals are wrong, incomplete, or late.

| S-N | Role | What They Decide Using These Signals | Risk If Signals Are Wrong |
|-----|------|--------------------------------------|---------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

Add rows as needed. These S-N identifiers are the source of truth for every Owner Role you
write in Phase 6. Do not invent roles; derive them from this table.

**INDEPENDENCE TEST — Phase 1 Exit Gate**

**STOP. Check these two items independently before Phase 2.**

- [ ] (1) >= 3 rows filled
- [ ] (2) All four columns filled in every row you wrote

Do not advance until both items are checked separately. These are not a sequence — do not
scan (1) and then scan (2) in the same pass. Evaluate (1) to a result. Evaluate (2) to a
result. Advance only when both results are PASS.

---

## Phase 2 — TOPICS.md Registration

Append to `simulations/TOPICS.md`:

```
| {topic} | active | simulations/{topic}/strategy.md |
```

**CHECK before Phase 3:**

- [ ] TOPICS.md contains the row
- [ ] Status = active
- [ ] Path = simulations/{topic}/strategy.md

---

## Phase 3 — Narrative Rationale

Write `## Rationale` in strategy.md.

Tell the reader:
- Why this topic matters
- Which specific design decision cannot be made without these signals
- What assumption teams currently make when they skip this investigation

**CHECK before Phase 4:**

- [ ] ## Rationale present
- [ ] >= 2 sentences
- [ ] A specific design decision is named
- [ ] The status-quo assumption is named

---

## Phase 4 — Artifact Naming Convention

Write `## Artifact Naming Convention` in strategy.md.

Pattern: `{topic}-{signal}-{date}.md`. Write at least one real parameterized example using
the actual topic name so the convention is concrete, not hypothetical.

**CHECK before Phase 5:**

- [ ] ## Artifact Naming Convention present
- [ ] Pattern is correct
- [ ] >= 1 real parameterized example

---

## Phase 5 — Pre-Write Validation

**STOP. Check everything before writing signal rows.**

Review each constraint:
- F-01 (Priority): essential / recommended / optional only — write exactly one of these three words
- F-02 (Namespace): from the canonical list
- F-03 (Skill): specific skill within namespace
- F-04 (Item Name): {topic}-{signal}-{date}.md
- F-05 (Owner Role): traceable to Phase 1 S-N row
- COV-01: at least one essential required
- COV-02: at least 2 namespaces required
- COV-03: at least 2 distinct owner roles required

**CHECK before Phase 6:**

- [ ] F-01--F-05 held in working memory
- [ ] COV-01--COV-03 held in working memory
- [ ] No signal rows written yet

---

## Phase 6 — Signal Plan Production

Write `## Signal Plan` in strategy.md.

**PRIORITY GOES FIRST.** The signal table column order is:

**Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role**

Priority is the leftmost column because it is the hardest failure mode to catch. A model that
fills Namespace first has already established contextual framing before reaching Priority; that
framing makes "high/medium/low" feel natural. Fill Priority before anything else. There is no
valid reason to place Priority in any other column position.

**CHECK before Phase 7** — cite F-01--F-05 and COV-01--COV-03:

- [ ] F-01: every Priority cell = essential / recommended / optional — nothing else
- [ ] F-02: every Namespace cell is from the canonical list
- [ ] F-03: every Skill cell is present
- [ ] F-04: every Item Name follows {topic}-{signal}-{date}.md
- [ ] F-05: every Owner Role traces to a Phase 1 S-N row
- [ ] Every Stakeholder Ref contains an S-N identifier
- [ ] COV-01: at least one essential
- [ ] COV-02: at least 2 distinct namespaces
- [ ] COV-03: at least 2 distinct owner roles tracing to distinct S-N rows

---

## Phase 7 — Post-Write Validation

**STOP when done. Check everything again before Phase 8.**

Do not add rows. Re-verify every constraint.

**CHECK before Phase 8** — F-01--F-05 and COV-01--COV-03 independently re-verified:

- [ ] Every F-NN constraint satisfied by every signal row
- [ ] Every COV-NN constraint satisfied by the full signal set

---

## Phase 8 — Commit Gate (Dedicated Phase)

**This phase is separate from signal production. Do not mix signal rows and commit gate text
in the same section.**

Write `## Commit Gate` in strategy.md.

Name every essential signal by its item name. Write the condition so a team member can check
it without re-reading the signal plan: "Design commit requires the following signals to be
present: [list]."

**CHECK when done:**

- [ ] ## Commit Gate is separate from ## Signal Plan
- [ ] Every essential signal named by item name
- [ ] Condition stated explicitly as a design commit requirement
- [ ] No new signal rows in this section
