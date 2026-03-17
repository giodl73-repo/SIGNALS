# topic-new — Round 14 Variations (V-01 through V-05)
# Rubric target: v13 (36 aspirational criteria, denominator 36)
# Date: 2026-03-15

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Role sequence | Front-loading stakeholder discovery as the structural root — every downstream phase derives from Phase 1 rows — produces stronger role differentiation than pipelines where roles arrive as late checklist items |
| V-02 | Output format | Prose-first rationale (as a required fill-in document before any tabulation) forces the model to articulate the decision context before committing to signal rows, producing richer C-07 and reducing vocabulary drift |
| V-03 | Lifecycle emphasis | Explicit ENTRY GATE + EXIT GATE labels at every phase boundary, with ceremonial phase-transition checkpoints, eliminates silent skips more reliably than any single pre-write gate |
| V-04 | Role sequence + Inertia framing | Opening the entire prompt with the INERTIA REGISTER and linking each stakeholder row to the IR-NN they are most vulnerable to creates the strongest mechanical coupling between inertia defaults and role discovery |
| V-05 | Phrasing register + Output format | Formal specification language (Definition, Constraint, Invariant, Precondition, Postcondition) with explicit fill-in form templates eliminates interpretive freedom and produces the most consistent structural compliance across diverse topic inputs |

---

---

## V-01 — Role Sequence Axis

**Axis**: Role sequence
**Hypothesis**: Front-loading stakeholder discovery as the structural root — every downstream phase derives from Phase 1 rows — produces stronger role differentiation than pipelines where roles arrive as late checklist items.
**Key Structural Difference**: Phase 1 is the most architecturally significant phase; every signal row must cite an S-NN source and the Consumer in F-05 must appear verbatim in the Phase 1 table; roles emerge from the model's first output, not from a late enforcement column.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Read before the overview table. These are the default behaviors
> this pipeline is designed to override. Each ID is stable; all phase directives
> cite these entries by ID.

| ID    | Default Behavior                                                                                  | Override Active In |
|-------|---------------------------------------------------------------------------------------------------|--------------------|
| IR-01 | Skip stakeholder mapping; author signal rows from intuition with no role grounding                | Phase 1            |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context                         | Phase 2            |
| IR-03 | Collapse commit gate into the signal plan section with no structural separation                   | Phase 3            |
| IR-04 | Omit artifact naming; use freeform item names                                                     | Phase 4            |
| IR-05 | Assign all signals to a single generic owner role                                                 | Phase 2            |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row.

| Phase | Purpose                   | Handoff Artifact            | Exit Gate (summary)                                            | If I Skip This Phase, I Will…                                             | Team Default (→ IR-NN)     | Recovery Cost If Caught Late                                       |
|-------|---------------------------|-----------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------|--------------------------------------------------------------------|
| 1     | Stakeholder Map           | S-table (≥3 rows, 4 cols)  | ≥3 rows AND all 4 columns filled, checked independently         | author orphan signal rows with no role ground truth                        | → IR-01, IR-05             | Re-run Phase 1, re-derive all Owner Role and Consumer values in Phase 2, re-run Phase 3, re-write strategy.md |
| 2     | Signal Plan               | Signal table rows           | F-01–F-06, COV-01–COV-04 pass; Consumer in F-05 traces to S-table | produce malformed strategy unusable as commit gate                       | → IR-02, IR-05             | Re-run Phase 2, re-run Phase 3, re-write strategy.md              |
| 3     | Commit Gate               | Gate definition block       | Gate names ≥1 essential signal explicitly; structurally isolated | ship feature with no enforced readiness condition                         | → IR-03                    | Re-run Phase 3, re-write strategy.md commit gate section          |
| 4     | Artifact Write            | TOPICS.md row + strategy.md | Both files at correct paths; item names follow naming convention | topic unregistered; strategy unreachable by downstream skills             | → IR-04                    | Re-write both artifacts; re-run path verification                  |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01**: "Skip stakeholder mapping; author signal rows from
> intuition with no role grounding." And IR-05: "Assign all signals to a single
> generic owner role."
>
> Every signal row in Phase 2 must trace its Owner Role and Consumer to a specific
> row in this table. Role differentiation emerges here — not from a late checklist.

**Entry gate**: INERTIA REGISTER confirmed read. [ ]

Fill in the following table. Every column is required.

| Row ID | Decision-Maker Role | Risk Exposure (what breaks for them if topic is skipped) | What Decision This Topic Informs For Them |
|--------|---------------------|----------------------------------------------------------|-------------------------------------------|
| S-01   |                     |                                                          |                                           |
| S-02   |                     |                                                          |                                           |
| S-03   |                     |                                                          |                                           |
| S-NN   | (add rows)          |                                                          |                                           |

> **Check these two conditions INDEPENDENTLY. Do not advance until both are
> checked separately. Checking them sequentially produces this specific failure:
> "3 rows present, columns empty" passes as compliant — this is wrong.**

- [ ] Row count ≥ 3 (minimum stakeholder breadth enforced)
- [ ] All four columns populated in every filled row

> Do not advance until both items are checked independently, not sequentially.

**Exit gate — IR-01 text reproduced verbatim at enforcement point**:
"Skip stakeholder mapping; author signal rows from intuition with no role grounding."
This phase overrides that default. Phase 1 is complete only when both independent
conditions above are satisfied.

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary from
> project-management context." And IR-05: "Assign all signals to a single generic
> owner role."

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

Write ≥ 2 sentences explaining why this topic needs investigation and what decision
it informs. This section is a required fill-in step, not optional prose.

> [Model fills here — minimum 2 sentences before proceeding to schema]

### FIELD SCHEMA

> Column order = row order. F-01 is the leftmost column. Fill left to right.

| ID   | Field             | Constraint                                                   | Consumer Decision Anchor                                      | Immediate Failure                                    | Downstream Effect                                                      |
|------|-------------------|--------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------|
| F-01 | Priority          | Must be exactly: essential / recommended / optional          | essential=decision blocked; recommended=quality risk accepted; optional=consumer decides unaffected | Row fails schema; strategy malformed         | Strategy unusable as commit gate; downstream parsers emit wrong signals |
| F-02 | Namespace         | One of: scout draft review flow trace prove listen program topic | —                                                         | Row invalid; namespace routing fails                 | Signal routed to wrong executor at runtime                             |
| F-03 | Skill             | Named skill under stated namespace                           | —                                                             | Row references non-existent skill                    | Signal uncollectable; evidence gap invisible                           |
| F-04 | Item Name         | `{topic}-{signal}-{date}.md` or parameterized template       | —                                                             | Format check fails; artifact path unresolvable        | Strategy unreachable by path-based tools                               |
| F-05 | Producer → Consumer | `{owner-role} → {decision-maker-role}` pair; Consumer must appear verbatim in Phase 1 S-table | —                          | Orphan consumer; traceability broken                 | Ownership undefined; signals accumulate without decision accountability |
| F-06 | Stakeholder Ref   | Must cite specific S-NN row from Phase 1                     | —                                                             | Orphan signal; no stakeholder basis                  | Signal disconnected from risk motivation; pruning has no ground truth  |

### COVERAGE SCHEMA

| ID     | Constraint                             | Minimum | Immediate Failure                                      | Downstream Effect                                                  |
|--------|----------------------------------------|---------|--------------------------------------------------------|--------------------------------------------------------------------|
| COV-01 | Signals marked essential               | ≥ 1     | No commit gate exists                                  | Feature ships without evidence gate; design commit is ungated      |
| COV-02 | Distinct namespaces                    | ≥ 2     | Single-namespace plan; structural blind spot           | Namespace gap analysis cannot detect coverage holes                |
| COV-03 | Distinct owner roles (via F-05)        | ≥ 2     | Single-owner strategy; collapses on personnel change   | Cross-functional gaps invisible; strategy is untrustworthy         |
| COV-04 | Narrative rationale (prose section)    | ≥ 2 sentences | Rationale absent                                  | Topic context lost; reviewers cannot evaluate signal relevance     |

### PRE-WRITE GATE

> Cite schema IDs directly. Do not restate rules in prose.

- [ ] F-01: Priority values are essential / recommended / optional only
- [ ] F-02: All namespace values from valid list
- [ ] F-03: All skill values are named skills under their namespace
- [ ] F-04: All item names follow `{topic}-{signal}-{date}.md` pattern
- [ ] F-05: All Producer→Consumer pairs; Consumer value appears verbatim in Phase 1 S-table (C-40 enforcement)
- [ ] F-06: All Stakeholder Ref values cite S-NN rows
- [ ] COV-01: ≥ 1 essential signal present
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct owner roles (verifiable via F-05 column)
- [ ] COV-04: Narrative rationale written above

### SIGNAL TABLE

> Priority is the leftmost column. Fill left to right. Reaching namespace/skill
> before setting priority induces "high/medium/low" vocabulary substitution — IR-02.

| Priority | Namespace | Skill | Item Name | Producer → Consumer | Stakeholder Ref |
|----------|-----------|-------|-----------|---------------------|-----------------|
|          |           |       |           |                     |                 |

**Exit gate**: All pre-write checkboxes above are cleared, citing F-01–F-06 and
COV-01–COV-04. Signal table contains ≥ 1 row.

**Exit gate — IR-02 text reproduced verbatim**: "Use 'high/medium/low' priority
vocabulary from project-management context." This phase overrides that default.
Every Priority cell must contain exactly one of: essential / recommended / optional.

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03**: "Collapse commit gate into the signal plan
> section with no structural separation."

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

The commit gate defines the minimal signal set required before design commit. It is
a separate phase because an inline gate is not enforced — it is aspirational.

Fill in the following block:

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name from essential row]
  2. [additional essential rows if any]

PERMITTED AFTER COMMIT (recommended/optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above exist
as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named explicitly.
Gate expressed as a condition, not as a list of aspirations.

**Exit gate — IR-03 text reproduced verbatim**: "Collapse commit gate into the
signal plan section with no structural separation." This phase overrides that
default. Phase 3 is complete only when the commit gate occupies this standalone
phase with its own named conditions.

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04**: "Omit artifact naming; use freeform item names."

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff artifact present. [ ]

### Write 1: simulations/TOPICS.md

Append a row:

```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |
```

### Write 2: simulations/{TOPIC}/strategy.md

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste 2+ sentence rationale from Phase 2]

## Stakeholder Map
[paste Phase 1 fill-in table]

## Inertia Register (Active Overrides)
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see pre-pipeline INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths. All item names in strategy.md
follow `{topic}-{signal}-{date}.md`.

**Exit gate — IR-04 text reproduced verbatim**: "Omit artifact naming; use freeform
item names." This phase overrides that default. Phase 4 is complete only when both
artifacts exist at declared paths with correctly formatted item names.
```

---

---

## V-02 — Output Format Axis

**Axis**: Output format
**Hypothesis**: A mandatory prose-first rationale phase (fill-in document, not table) between stakeholder discovery and signal tabulation forces articulation of the decision context before signal rows are committed, producing richer C-07 coverage and reducing the namespace/skill framing that induces priority vocabulary drift.
**Key Structural Difference**: Phase 1.5 is a dedicated prose rationale document phase with its own entry and exit gates; signals are expressed in a list format with labeled fields before the table is assembled; the FIELD SCHEMA drives column order but signals are also expressible as structured field blocks.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Read before the overview table. Stable IDs; all phase directives
> cite these by ID.

| ID    | Default Behavior                                                                                  | Override Active In |
|-------|---------------------------------------------------------------------------------------------------|--------------------|
| IR-01 | Skip stakeholder mapping; write signal rows from intuition                                        | Phase 1            |
| IR-02 | Use "high/medium/low" priority vocabulary                                                         | Phase 2b           |
| IR-03 | Collapse commit gate into signal plan; no structural isolation                                    | Phase 3            |
| IR-04 | Omit artifact naming convention; use freeform names                                               | Phase 4            |
| IR-05 | Write rationale after signals are defined, anchoring justification to rows already written         | Phase 1.5          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have processed every row of this table.

| Phase | Purpose                       | Handoff Artifact                    | Exit Gate (summary)                                          | If I Skip This Phase, I Will…                                                 | Team Default (→ IR-NN) | Recovery Cost If Caught Late                                              |
|-------|-------------------------------|-------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------|
| 1     | Stakeholder Map               | S-table (≥3 rows, 4 cols)           | ≥3 rows AND all 4 columns filled, checked independently      | produce signals with no stakeholder ground truth                                | → IR-01                | Re-run Phase 1, re-run 1.5, re-run 2b, re-write strategy.md             |
| 1.5   | Prose Rationale Document      | Rationale prose block (≥2 sentences)| Prose confirms topic decision and ≥2 sentences written       | anchor rationale to rows already defined — IR-05 drift                          | → IR-05                | Re-run Phase 1.5, re-run Phase 2b (may add/remove rows), re-write file   |
| 2a    | Schema Declaration            | FIELD SCHEMA + COVERAGE SCHEMA      | All F-NN and COV-NN rows present with consequence columns    | fill signal table with no schema enforcement frame                               | → IR-02                | Re-run 2a, re-run 2b, re-run Phase 3, re-write strategy.md               |
| 2b    | Signal Plan (tabulation)      | Signal table rows                   | F-01–F-06, COV-01–COV-04 pass; Consumer traces to S-table   | produce malformed strategy unusable as commit gate                               | → IR-02, IR-01         | Re-run 2b, re-run Phase 3, re-write strategy.md                          |
| 3     | Commit Gate                   | Gate definition block               | Gate names ≥1 essential signal; structurally isolated        | ship feature with no enforced readiness condition                                | → IR-03                | Re-run Phase 3, re-write strategy.md commit gate section                 |
| 4     | Artifact Write                | TOPICS.md row + strategy.md         | Both files at correct paths; item names follow convention    | topic unregistered; strategy unreachable by downstream skills                    | → IR-04                | Re-write both artifacts; re-run path verification                         |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01**: "Skip stakeholder mapping; write signal rows from intuition."

**Entry gate**: INERTIA REGISTER confirmed read. [ ]

| Row ID | Decision-Maker Role | Risk Exposure | What Decision This Topic Informs |
|--------|---------------------|---------------|----------------------------------|
| S-01   |                     |               |                                  |
| S-02   |                     |               |                                  |
| S-03   |                     |               |                                  |
| S-NN   | (add rows)          |               |                                  |

> **Check these two conditions INDEPENDENTLY. Do not advance until both are checked
> separately. Sequential checking produces this failure: "3 rows present, cells
> empty" passes as compliant — this is wrong.**

- [ ] Row count ≥ 3
- [ ] All four columns populated in every row

> Do not advance until both items are checked independently, not sequentially.

**Exit gate — IR-01 text reproduced verbatim**: "Skip stakeholder mapping; write
signal rows from intuition." This phase overrides that default.

---

## PHASE 1.5 — PROSE RATIONALE DOCUMENT

> **This phase overrides IR-05**: "Write rationale after signals are defined,
> anchoring justification to rows already written."
>
> Rationale must be written BEFORE signal rows are committed. This is the critical
> difference from IR-05: rationale shapes the signal plan, not the other way around.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

Write a rationale prose block answering both of:
1. Why does `{TOPIC}` need investigation right now? What is unknown?
2. What design or build decision does this topic directly inform?

```
RATIONALE FOR {TOPIC}
=====================
[2+ sentences — model fills here]
```

**Exit gate**: Rationale block present. ≥ 2 sentences written. Decision it informs
is named explicitly.

**Exit gate — IR-05 text reproduced verbatim**: "Write rationale after signals are
defined, anchoring justification to rows already written." This phase overrides that
default. Phase 1.5 is complete only when the rationale is written before Phase 2b.

---

## PHASE 2a — SCHEMA DECLARATION

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary."

**Entry gate**: Phase 1.5 exit gate cleared AND rationale handoff artifact present. [ ]

### FIELD SCHEMA

> Row order defines column order. F-01 = Priority = leftmost column.

| ID   | Field              | Constraint                                                   | Decision-State Anchor (all 3 tiers)                                          | Immediate Failure                             | Downstream Effect                                                    |
|------|--------------------|--------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority           | essential / recommended / optional only                      | essential=decision blocked; recommended=quality risk accepted; optional=consumer decides unaffected | Schema violation; strategy malformed | Strategy unusable as commit gate; parsers emit wrong signals        |
| F-02 | Namespace          | scout draft review flow trace prove listen program topic     | —                                                                            | Namespace invalid; routing fails              | Signal routed to wrong executor                                     |
| F-03 | Skill              | Named skill under stated namespace                           | —                                                                            | Skill non-existent; execution fails           | Signal uncollectable; evidence gap invisible                        |
| F-04 | Item Name          | `{topic}-{signal}-{date}.md` or parameterized template       | —                                                                            | Format invalid; path unresolvable             | Strategy unreachable by path-based tools                            |
| F-05 | Producer → Consumer | `{owner-role} → {decision-maker-role}`; Consumer verbatim in S-table | —                                                                   | Orphan consumer; traceability broken          | Ownership undefined; signals lack decision accountability           |
| F-06 | Stakeholder Ref    | S-NN row from Phase 1                                        | —                                                                            | Orphan signal; no stakeholder basis           | Signal disconnected from risk motivation                            |

### COVERAGE SCHEMA

| ID     | Constraint                    | Minimum  | Immediate Failure                            | Downstream Effect                                              |
|--------|-------------------------------|----------|----------------------------------------------|----------------------------------------------------------------|
| COV-01 | Essential signals              | ≥ 1      | No commit gate exists                         | Feature ships ungated                                          |
| COV-02 | Distinct namespaces            | ≥ 2      | Single-namespace plan                         | Blind spots undetectable by gap analysis                       |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2      | All signals owned by one party                | Cross-functional gaps invisible                                |
| COV-04 | Rationale document             | ≥ 2 sent | Rationale absent                              | Context lost; signal relevance unverifiable                    |

**Exit gate**: All F-NN and COV-NN rows present with consequence columns filled.

---

## PHASE 2b — SIGNAL PLAN

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary."
> And IR-01: "Skip stakeholder mapping; write signal rows from intuition."

**Entry gate**: Phase 2a exit gate cleared AND schema handoff artifacts present. [ ]

### PRE-WRITE GATE

> Cite schema IDs directly. Do not restate rules in prose.

- [ ] F-01: Priority vocabulary confirmed (essential / recommended / optional only)
- [ ] F-02: All namespaces from valid list
- [ ] F-03: All skills named under their namespace
- [ ] F-04: All item names follow `{topic}-{signal}-{date}.md`
- [ ] F-05: Consumer value appears verbatim in Phase 1 S-table (C-40 check)
- [ ] F-06: All Stakeholder Ref values cite S-NN rows
- [ ] COV-01: ≥ 1 essential signal
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct Producer roles
- [ ] COV-04: Rationale document present (from Phase 1.5)

### SIGNAL TABLE

> Priority column is first (F-01 = leftmost). Fill left to right.

| Priority | Namespace | Skill | Item Name | Producer → Consumer | Stakeholder Ref |
|----------|-----------|-------|-----------|---------------------|-----------------|
|          |           |       |           |                     |                 |

**Exit gate**: All pre-write checkboxes cleared (F-01–F-06, COV-01–COV-04 cited).
Signal table contains ≥ 1 row with ≥ 1 essential.

**Exit gate — IR-02 text reproduced verbatim**: "Use 'high/medium/low' priority
vocabulary." This phase overrides that default. Every Priority cell must contain
exactly one of: essential / recommended / optional.

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03**: "Collapse commit gate into signal plan; no structural isolation."

**Entry gate**: Phase 2b exit gate cleared AND signal table handoff artifact present. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when present in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name]

PERMITTED AFTER COMMIT:
  - [recommended/optional items]

Enforcement: no design commit until REQUIRED items exist at declared paths.
```

**Exit gate**: Block written. ≥ 1 essential signal named. Gate is a condition,
not an aspiration.

**Exit gate — IR-03 text reproduced verbatim**: "Collapse commit gate into signal
plan; no structural isolation." This phase overrides that default.

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04**: "Omit artifact naming convention; use freeform names."

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff present. [ ]

Write `simulations/TOPICS.md` row and `simulations/{TOPIC}/strategy.md` with sections:
Rationale / Stakeholder Map / Inertia Register / Signal Plan / Commit Gate.

**Exit gate**: Both files at correct paths. All item names follow naming convention.

**Exit gate — IR-04 text reproduced verbatim**: "Omit artifact naming convention;
use freeform names." This phase overrides that default.
```

---

---

## V-03 — Lifecycle Emphasis Axis

**Axis**: Lifecycle emphasis
**Hypothesis**: Explicit ENTRY GATE and EXIT GATE labels at every phase boundary — with both a "before writing" entry check and an "after writing" exit check — eliminates silent phase skips more reliably than any single pre-write gate or linear-only exit gate chain. Every phase boundary is a ceremony, not a transition.
**Key Structural Difference**: Each phase opens with a named ENTRY GATE block and closes with a named EXIT GATE block. The ENTRY GATE is a precondition list; the EXIT GATE is a postcondition list. The phase body is sandwiched between them. Skipping either block is structurally visible.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IDs. All phase ENTRY and EXIT gates cite these by ID.

| ID    | Default Behavior                                                              | Override Active In  |
|-------|-------------------------------------------------------------------------------|---------------------|
| IR-01 | Skip stakeholder mapping; author signals from intuition                       | Phase 1 ENTRY       |
| IR-02 | Use "high/medium/low" priority vocabulary                                     | Phase 2 ENTRY + EXIT|
| IR-03 | Collapse commit gate into signal plan section                                 | Phase 3 ENTRY       |
| IR-04 | Omit artifact naming convention                                               | Phase 4 EXIT        |
| IR-05 | Treat phase transitions as implicit; no gate ceremony required                | Every boundary      |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1. All entry gates, exit gates,
> handoff artifacts, and skip costs are declared here. Do not begin Phase 1 until
> you have processed every row.**

| Phase | Purpose          | Handoff Artifact              | Entry Gate               | Exit Gate                                              | If I Skip This Phase, I Will…                              | Team Default (→ IR-NN) | Recovery Cost If Caught Late                                    |
|-------|------------------|-------------------------------|--------------------------|--------------------------------------------------------|------------------------------------------------------------|------------------------|-----------------------------------------------------------------|
| 1     | Stakeholder Map  | S-table (≥3 rows, 4 cols)    | IR register confirmed    | ≥3 rows AND 4 cols filled, checked independently        | author signals with no stakeholder ground truth            | → IR-01, IR-05         | Re-run Phase 1, re-derive F-05 in Phase 2, re-run 3, re-write files |
| 2     | Signal Plan      | Signal table + schemas        | S-table present          | F-01–F-06 + COV-01–COV-04 pass; Consumer traces S-table | produce strategy unusable as commit gate                   | → IR-02, IR-05         | Re-run Phase 2, re-run Phase 3, re-write strategy.md           |
| 3     | Commit Gate      | Gate definition block         | Signal table present     | Gate names ≥1 essential; structurally isolated          | ship without enforced readiness condition                   | → IR-03, IR-05         | Re-run Phase 3, re-write commit gate section                    |
| 4     | Artifact Write   | TOPICS.md row + strategy.md   | Gate block present       | Both files correct path; item names follow convention   | topic unregistered; strategy unreachable                    | → IR-04, IR-05         | Re-write both artifacts; re-run path verification               |

---

## PHASE 1 — STAKEHOLDER MAP

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTRY GATE — Phase 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> **This phase overrides IR-01**: "Skip stakeholder mapping; author signals from intuition."
> And IR-05: "Treat phase transitions as implicit; no gate ceremony required."

Before beginning Phase 1:
- [ ] INERTIA REGISTER has been read in full
- [ ] IR-01 override acknowledged: stakeholder table must be filled before any signal rows are written
- [ ] IR-05 override acknowledged: this ENTRY GATE is a required ceremony, not optional

Do not begin Phase 1 body until all ENTRY GATE items are checked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 BODY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Fill the stakeholder map. Every column is required.

| Row ID | Decision-Maker Role | Risk Exposure                                    | What Decision This Topic Informs |
|--------|---------------------|--------------------------------------------------|----------------------------------|
| S-01   |                     |                                                  |                                  |
| S-02   |                     |                                                  |                                  |
| S-03   |                     |                                                  |                                  |
| S-NN   | (add rows)          |                                                  |                                  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXIT GATE — Phase 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> **Check these two conditions INDEPENDENTLY. Do not advance until both are
> checked separately. Sequential checking produces this specific failure:
> "3 rows present, columns empty" passes as compliant — this is wrong.**

- [ ] Row count ≥ 3 (minimum breadth enforced)
- [ ] All four columns populated in every filled row (completeness enforced)

> Do not advance until both items are checked independently, not sequentially.

**IR-01 text reproduced verbatim at exit enforcement point**:
"Skip stakeholder mapping; author signals from intuition."
This phase overrides that default. EXIT GATE is complete only when both
conditions above are independently satisfied.

Do not proceed to Phase 2 until this EXIT GATE is complete.

---

## PHASE 2 — SIGNAL PLAN

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTRY GATE — Phase 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary."
> And IR-05: "Treat phase transitions as implicit."

Before beginning Phase 2:
- [ ] Phase 1 EXIT GATE confirmed complete
- [ ] S-table handoff artifact present (≥3 rows, all 4 columns filled)
- [ ] IR-02 override acknowledged: priority values must be essential / recommended / optional only

Do not begin Phase 2 body until all ENTRY GATE items are checked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 BODY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Narrative Rationale** (≥ 2 sentences before schema):
> [Model fills — minimum 2 sentences. What is unknown? What decision does this inform?]

### FIELD SCHEMA

> Row order = column order. F-01 is the leftmost column in the signal table.

| ID   | Field              | Constraint                                               | Decision-State Anchor                                                         | Immediate Failure                          | Downstream Effect                                               |
|------|--------------------|----------------------------------------------------------|-------------------------------------------------------------------------------|--------------------------------------------|---------------------------------------------------------------|
| F-01 | Priority           | essential / recommended / optional only                  | essential=decision blocked; recommended=quality risk accepted; optional=consumer decides unaffected | Schema violation; strategy malformed | Strategy unusable as commit gate                            |
| F-02 | Namespace          | scout draft review flow trace prove listen program topic | —                                                                             | Invalid namespace; routing fails           | Signal routed to wrong executor                                |
| F-03 | Skill              | Named skill under stated namespace                       | —                                                                             | Non-existent skill; execution fails        | Signal uncollectable                                           |
| F-04 | Item Name          | `{topic}-{signal}-{date}.md` or parameterized template   | —                                                                             | Format invalid; path unresolvable          | Strategy unreachable by path tools                             |
| F-05 | Producer → Consumer | `{role} → {decision-maker-role}`; Consumer verbatim in S-table | —                                                                      | Orphan consumer; traceability broken       | Signals lack decision accountability                           |
| F-06 | Stakeholder Ref    | S-NN row from Phase 1                                    | —                                                                             | Orphan signal; no stakeholder basis        | Signal disconnected from risk motivation                       |

### COVERAGE SCHEMA

| ID     | Constraint                  | Minimum | Immediate Failure                        | Downstream Effect                              |
|--------|-----------------------------|---------|------------------------------------------|------------------------------------------------|
| COV-01 | Essential signals            | ≥ 1     | No commit gate exists                     | Feature ships ungated                          |
| COV-02 | Distinct namespaces          | ≥ 2     | Single-namespace plan                     | Blind spots undetectable                       |
| COV-03 | Distinct Producer roles      | ≥ 2     | Single-owner collapse                     | Cross-functional gaps invisible                |
| COV-04 | Narrative rationale written  | ≥ 2 s   | Context absent                            | Signal relevance unverifiable                  |

**Pre-write gate** (cite F-NN and COV-NN IDs):
- [ ] F-01: Priority vocabulary valid
- [ ] F-02: Namespaces valid
- [ ] F-03: Skills named
- [ ] F-04: Item names follow convention
- [ ] F-05: Consumer appears verbatim in S-table
- [ ] F-06: Stakeholder Refs cite S-NN rows
- [ ] COV-01: ≥ 1 essential
- [ ] COV-02: ≥ 2 namespaces
- [ ] COV-03: ≥ 2 roles
- [ ] COV-04: Rationale written

### SIGNAL TABLE (Priority first — F-01 leftmost)

| Priority | Namespace | Skill | Item Name | Producer → Consumer | Stakeholder Ref |
|----------|-----------|-------|-----------|---------------------|-----------------|
|          |           |       |           |                     |                 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXIT GATE — Phase 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [ ] All pre-write gate checkboxes above cleared (F-01–F-06, COV-01–COV-04)
- [ ] Signal table has ≥ 1 row
- [ ] ≥ 1 essential signal present (COV-01 enforcement)
- [ ] F-05 Consumer value checked verbatim against Phase 1 S-table

**IR-02 text reproduced verbatim at exit enforcement point**:
"Use 'high/medium/low' priority vocabulary."
This phase overrides that default. Every Priority cell must contain exactly one
of: essential / recommended / optional. EXIT GATE is complete only when all four
conditions above are satisfied.

Do not proceed to Phase 3 until this EXIT GATE is complete.

---

## PHASE 3 — COMMIT GATE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTRY GATE — Phase 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> **This phase overrides IR-03**: "Collapse commit gate into signal plan section."
> And IR-05: "Treat phase transitions as implicit."

Before beginning Phase 3:
- [ ] Phase 2 EXIT GATE confirmed complete
- [ ] Signal table handoff artifact present
- [ ] IR-03 override acknowledged: commit gate occupies its own phase

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 BODY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when ALL REQUIRED items present in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name]

PERMITTED AFTER COMMIT:
  - [recommended/optional items]

Enforcement: no design commit until REQUIRED items exist at declared paths.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXIT GATE — Phase 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [ ] Commit gate block written as a standalone section
- [ ] ≥ 1 essential signal named explicitly in REQUIRED list
- [ ] Gate is a condition, not a list of aspirations

**IR-03 text reproduced verbatim**: "Collapse commit gate into signal plan section."
This phase overrides that default. EXIT GATE complete only when block is structurally
isolated and conditions above are satisfied.

---

## PHASE 4 — ARTIFACT WRITE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENTRY GATE — Phase 4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [ ] Phase 3 EXIT GATE confirmed complete
- [ ] Commit gate block handoff present

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 BODY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write `simulations/TOPICS.md` row and `simulations/{TOPIC}/strategy.md`
with sections: Rationale / Stakeholder Map / INERTIA REGISTER / Signal Plan / Commit Gate.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXIT GATE — Phase 4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [ ] `simulations/TOPICS.md` contains row for {TOPIC}
- [ ] `simulations/{TOPIC}/strategy.md` exists at correct path
- [ ] All item names follow `{topic}-{signal}-{date}.md` convention
- [ ] All five strategy.md sections present

**IR-04 text reproduced verbatim**: "Omit artifact naming convention." This phase
overrides that default. EXIT GATE complete only when all four conditions satisfied.
```

---

---

## V-04 — Role Sequence + Inertia Framing (Combined)

**Axes**: Role sequence + Inertia framing
**Hypothesis**: Opening the entire prompt with the INERTIA REGISTER (as the first thing read, before pipeline overview) and structurally linking each stakeholder row to the specific IR-NN they are most vulnerable to creates the strongest mechanical coupling between inertia defaults and role discovery. The signal plan becomes a plan to defeat inertia defaults on behalf of named stakeholders.
**Key Structural Difference**: INERTIA REGISTER is the document opener — before any context. Phase 1 stakeholder table has a "Most Vulnerable To IR-NN" column. Phase 2 signal rows cite both an S-NN and an IR-NN — each signal is a stake in the ground against a specific inertia default for a specific stakeholder. The framing of the entire prompt is: "inertia is the competitor; stakeholders are at risk; signals are the countermoves."

---

```
# topic-new — Register Topic and Plan Signals

---

## INERTIA REGISTER

> **Read this first. Before anything else.**
>
> These are the behaviors your team will default to if this pipeline is not
> actively executed. Each IR-NN is a failure mode with a named stakeholder victim.
> The pipeline exists to override these defaults on behalf of named stakeholders.

| ID    | Default Behavior (what happens without active intervention)                                      | Stakeholder Harmed By This Default            | Override Phase |
|-------|--------------------------------------------------------------------------------------------------|-----------------------------------------------|----------------|
| IR-01 | Skip stakeholder mapping; write signal rows from intuition with no role grounding                | All roles — no one's risk is represented       | Phase 1        |
| IR-02 | Use "high/medium/low" priority vocabulary; strategy is unenforceable as a commit gate            | PM / Program Manager — cannot gate design commit | Phase 2      |
| IR-03 | Collapse commit gate into signal plan; gate is implicit and unenforced                           | Tech Lead / Engineering Manager — ships blind  | Phase 3        |
| IR-04 | Omit artifact naming; strategy paths are unresolvable by downstream tools                        | Developer / Toolchain — cannot locate signals  | Phase 4        |
| IR-05 | Assign all signals to a single generic owner; strategy collapses on personnel change             | All roles — no cross-functional accountability | Phase 2        |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1. All exit gate conditions,
> handoff artifacts, and skip costs are declared here. Do not begin Phase 1 until
> you have processed every row of this table.**

| Phase | Purpose          | Handoff Artifact             | Exit Gate (summary)                                         | If I Skip This Phase, I Will…                                       | Team Default (→ IR-NN) | Recovery Cost If Caught Late                                       |
|-------|------------------|------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------|------------------------|--------------------------------------------------------------------|
| 1     | Stakeholder Map  | S-table (≥3 rows, 5 cols)   | ≥3 rows AND all 5 cols filled, checked independently         | produce signals with no stakeholder-inertia coupling                | → IR-01, IR-05         | Re-run Phase 1, re-run Phase 2 entirely, re-run Phase 3, re-write files |
| 2     | Signal Plan      | Signal table rows            | F-01–F-07, COV-01–COV-04 pass; Consumer traces to S-table   | produce strategy unusable as commit gate; inertia unaddressed        | → IR-02, IR-05         | Re-run Phase 2, re-run Phase 3, re-write strategy.md              |
| 3     | Commit Gate      | Gate definition block        | Gate names ≥1 essential signal; structurally isolated        | ship feature with no enforced readiness condition                    | → IR-03                | Re-run Phase 3, re-write commit gate section                       |
| 4     | Artifact Write   | TOPICS.md row + strategy.md  | Both files at correct paths; item names follow convention    | topic unregistered; strategy unreachable                             | → IR-04                | Re-write both artifacts; re-run path verification                  |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01**: "Skip stakeholder mapping; write signal rows
> from intuition with no role grounding." Every row in this table represents an
> active defense against IR-01 on behalf of a named stakeholder.
>
> Also overrides IR-05: "Assign all signals to a single generic owner." The
> "Most Vulnerable To IR-NN" column forces you to identify which inertia default
> most endangers each stakeholder — this is the structural mechanism that prevents
> single-owner collapse.

**Entry gate**: INERTIA REGISTER read in full. [ ]

Fill in the stakeholder map. The fifth column links each stakeholder to the
inertia default that most threatens them if this topic is not investigated.

| Row ID | Decision-Maker Role | Risk Exposure                          | What Decision This Topic Informs | Most Vulnerable To IR-NN |
|--------|---------------------|----------------------------------------|----------------------------------|--------------------------|
| S-01   |                     |                                        |                                  |                          |
| S-02   |                     |                                        |                                  |                          |
| S-03   |                     |                                        |                                  |                          |
| S-NN   | (add rows)          |                                        |                                  |                          |

> **Check these two conditions INDEPENDENTLY. Do not advance until both are checked
> separately. Sequential checking produces this specific failure: "3 rows present,
> column 5 empty" passes as compliant — this is wrong.**

- [ ] Row count ≥ 3 (minimum breadth enforced)
- [ ] All five columns populated in every filled row

> Do not advance until both items are checked independently, not sequentially.

**Exit gate — IR-01 text reproduced verbatim**: "Skip stakeholder mapping; write
signal rows from intuition with no role grounding." This phase overrides that
default. Phase 1 complete only when both conditions above are independently satisfied.

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary."
> And IR-05: "Assign all signals to a single generic owner."
>
> Each signal row is a countermove against a specific inertia default on behalf
> of a specific stakeholder. The IR-NN Override column makes this explicit.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

**Narrative Rationale** (≥ 2 sentences — write before filling any signal rows):
> [Model fills — minimum 2 sentences.]

### FIELD SCHEMA

> Row order defines column order. F-01 = Priority = leftmost column.

| ID   | Field              | Constraint                                                   | Decision-State Anchor                                                         | Immediate Failure                          | Downstream Effect                                              |
|------|--------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------|--------------------------------------------|----------------------------------------------------------------|
| F-01 | Priority           | essential / recommended / optional only                      | essential=decision blocked; recommended=quality risk accepted; optional=consumer decides unaffected | Schema violation; strategy malformed | Strategy unusable as commit gate                             |
| F-02 | Namespace          | scout draft review flow trace prove listen program topic     | —                                                                             | Invalid namespace; routing fails           | Signal routed to wrong executor                               |
| F-03 | Skill              | Named skill under stated namespace                           | —                                                                             | Non-existent skill                         | Signal uncollectable; gap invisible                           |
| F-04 | Item Name          | `{topic}-{signal}-{date}.md` or parameterized template       | —                                                                             | Format invalid; path unresolvable          | Strategy unreachable                                          |
| F-05 | Producer → Consumer | `{role} → {decision-maker-role}`; Consumer verbatim in S-table | —                                                                         | Orphan consumer; traceability broken       | Signals lack decision accountability                          |
| F-06 | Stakeholder Ref    | S-NN row from Phase 1                                        | —                                                                             | Orphan signal; no stakeholder basis        | Signal disconnected from risk motivation                      |
| F-07 | IR-NN Override     | IR-NN from INERTIA REGISTER; this signal defeats that default | —                                                                            | Orphan signal; inertia not addressed       | Inertia default survives for this stakeholder silently        |

### COVERAGE SCHEMA

| ID     | Constraint                   | Minimum | Immediate Failure                        | Downstream Effect                              |
|--------|------------------------------|---------|------------------------------------------|------------------------------------------------|
| COV-01 | Essential signals             | ≥ 1     | No commit gate exists                     | Feature ships ungated                          |
| COV-02 | Distinct namespaces           | ≥ 2     | Single-namespace plan                     | Blind spots undetectable                       |
| COV-03 | Distinct Producer roles (F-05)| ≥ 2     | Single-owner collapse                     | Cross-functional gaps invisible                |
| COV-04 | Narrative rationale           | ≥ 2 s   | Context absent                            | Signal relevance unverifiable                  |

**Pre-write gate** (cite F-NN and COV-NN IDs):
- [ ] F-01: Priority vocabulary valid (essential / recommended / optional only)
- [ ] F-02: All namespaces from valid list
- [ ] F-03: All skills named under their namespace
- [ ] F-04: All item names follow `{topic}-{signal}-{date}.md`
- [ ] F-05: Consumer appears verbatim in Phase 1 S-table
- [ ] F-06: All rows cite S-NN
- [ ] F-07: All rows cite IR-NN from INERTIA REGISTER
- [ ] COV-01: ≥ 1 essential
- [ ] COV-02: ≥ 2 namespaces
- [ ] COV-03: ≥ 2 distinct roles
- [ ] COV-04: Rationale written

### SIGNAL TABLE

> Priority is leftmost (F-01). Fill left to right. IR-NN Override column makes
> each signal's inertia countermove explicit.

| Priority | Namespace | Skill | Item Name | Producer → Consumer | Stakeholder Ref | IR-NN Override |
|----------|-----------|-------|-----------|---------------------|-----------------|----------------|
|          |           |       |           |                     |                 |                |

**Exit gate**: All pre-write checkboxes cleared (F-01–F-07, COV-01–COV-04).
Signal table ≥ 1 row. ≥ 1 essential signal. Consumer verified verbatim in S-table.

**Exit gate — IR-02 text reproduced verbatim**: "Use 'high/medium/low' priority
vocabulary; strategy is unenforceable as a commit gate." This phase overrides
that default. Every Priority cell must contain exactly one of: essential /
recommended / optional.

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03**: "Collapse commit gate into signal plan section."

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff present. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when ALL REQUIRED items present in simulations/{TOPIC}/:

REQUIRED (essential — these defeat the remaining inertia defaults):
  1. [item name] — defeats IR-NN for S-NN

PERMITTED AFTER COMMIT:
  - [recommended/optional items]

Enforcement: no design commit until REQUIRED items exist at declared paths.
```

**Exit gate**: Block written. ≥ 1 essential signal named. Inertia connection stated.

**Exit gate — IR-03 text reproduced verbatim**: "Collapse commit gate into signal
plan section; gate is implicit and unenforced." This phase overrides that default.

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04**: "Omit artifact naming; strategy paths are
> unresolvable by downstream tools."

**Entry gate**: Phase 3 exit gate cleared. [ ]

Write `simulations/TOPICS.md` row and `simulations/{TOPIC}/strategy.md`
with sections: Rationale / Stakeholder Map / INERTIA REGISTER / Signal Plan / Commit Gate.

**Exit gate**: Both files at correct paths. All item names follow `{topic}-{signal}-{date}.md`.

**Exit gate — IR-04 text reproduced verbatim**: "Omit artifact naming; strategy
paths are unresolvable by downstream tools." This phase overrides that default.
```

---

---

## V-05 — Phrasing Register + Output Format (Combined)

**Axes**: Phrasing register + Output format
**Hypothesis**: Formal specification language — using Definition, Constraint, Invariant, Precondition, Postcondition, and Violation: clauses throughout — with fill-in forms that have typed field slots eliminates interpretive freedom and produces the most structurally consistent output across diverse topic inputs. Conversational language is a source of behavioral variance; formal language eliminates that variance.
**Key Structural Difference**: All instructions use formal spec language. Every structural element is introduced by a keyword (DEFINITION, CONSTRAINT, INVARIANT, etc.). Output templates are explicit numbered forms with typed slots. Schema tables use formal column labels. No natural-language preambles.

---

```
# topic-new — Specification for Registering a Topic and Planning Its Signals

SKILL: topic-new
OUTPUT-1: simulations/TOPICS.md (append row)
OUTPUT-2: simulations/{TOPIC}/strategy.md (write file)

---

## INERTIA REGISTER

DEFINITION: The INERTIA REGISTER is a pre-pipeline declaration of the team's
default behaviors in the absence of active execution of this pipeline. Each entry
carries a stable identifier (IR-NN) and is referenced by ID from all phase
directives. No inline restatement of defaults is permitted elsewhere in this prompt.

| ID    | Default Behavior (Formal Statement)                                                        | Override Constraint                                                            |
|-------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| IR-01 | AGENT produces signal rows without prior stakeholder grounding                             | PRECONDITION Phase 2: Phase 1 S-table ≥ 3 rows with 4 columns complete         |
| IR-02 | AGENT uses priority vocabulary { "high", "medium", "low" }                                 | INVARIANT: Priority ∈ { "essential", "recommended", "optional" } at all times  |
| IR-03 | AGENT produces commit gate as inline prose within signal plan section                      | CONSTRAINT: Commit Gate must occupy Phase 3, a phase structurally distinct from Phase 2 |
| IR-04 | AGENT produces item names without adherence to naming convention                           | INVARIANT: item_name matches regex `{topic}-{signal}-{date}\.md`               |
| IR-05 | AGENT assigns identical Owner Role to all signal rows                                      | CONSTRAINT: COV-03 requires ≥ 2 distinct Owner Roles across signal table       |

---

## PIPELINE SPECIFICATION

INVARIANT: Read this entire table before executing Phase 1.
INVARIANT: All preconditions, postconditions, and violation consequences are declared here before any phase body.
VIOLATION: Executing Phase 1 before reading this table produces incorrect gate-condition framing for all subsequent phases.

| Phase | Specification                | Handoff Artifact               | Precondition (Entry Gate)                           | Postcondition (Exit Gate)                                             | AGENT Violation Description                                              | Team Default (→ IR-NN) | Recovery Chain If Caught Late                                       |
|-------|------------------------------|--------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------|
| 1     | Stakeholder Map Production   | S-table(rows≥3, cols=4)       | IR register confirmed read                          | row_count ≥ 3 ∧ ∀row: all_4_columns_populated [checked independently] | AGENT produces signal rows with no stakeholder basis (IR-01)             | → IR-01, IR-05         | Phase 1 re-execute → Phase 2 re-execute → Phase 3 re-execute → re-write OUTPUT-2 |
| 2     | Signal Plan Production       | signal_table(rows≥1)          | S-table handoff present                              | ∀rows: F-01–F-06 pass ∧ COV-01–COV-04 pass ∧ Consumer ∈ S-table     | AGENT produces invalid priority vocabulary and orphaned consumer roles   | → IR-02, IR-05         | Phase 2 re-execute → Phase 3 re-execute → re-write OUTPUT-2        |
| 3     | Commit Gate Production       | commit_gate_block              | signal_table handoff present                         | gate_block isolates ≥ 1 essential signal in named REQUIRED list       | AGENT ships without enforced design commit gate (IR-03)                  | → IR-03                | Phase 3 re-execute → re-write OUTPUT-2 commit gate section         |
| 4     | Artifact Write               | OUTPUT-1, OUTPUT-2             | commit_gate_block handoff present                    | ∀paths: correct ∧ ∀item_names: regex_compliant                        | AGENT produces unregistered topic with unreachable strategy path (IR-04) | → IR-04                | Re-write OUTPUT-1 and OUTPUT-2; re-run path verification            |

---

## PHASE 1 — STAKEHOLDER MAP PRODUCTION

OVERRIDE: IR-01 ("AGENT produces signal rows without prior stakeholder grounding")
OVERRIDE: IR-05 ("AGENT assigns identical Owner Role to all signal rows")
PRECONDITION: INERTIA REGISTER has been read in full. [ ]
CONSTRAINT: No signal row in Phase 2 may reference an Owner Role or Consumer not
  present in this table.

FORM 1.A — STAKEHOLDER MAP

Instructions: Fill all slots. Row_ID format: S-{integer}.
Minimum row count: 3 (enforced at EXIT GATE below).

| Row_ID | Decision_Maker_Role: string | Risk_Exposure: string           | Informs_Decision: string |
|--------|-----------------------------|---------------------------------|--------------------------|
| S-01   |                             |                                 |                          |
| S-02   |                             |                                 |                          |
| S-03   |                             |                                 |                          |
| S-NN   | [add rows as needed]        |                                 |                          |

POSTCONDITION (Exit Gate):

INDEPENDENCE INSTRUCTION: Check these two conditions independently. Do not
  evaluate them as a compound statement. Sequential evaluation produces this
  specific failure mode: "row_count ≥ 3 ∧ cells empty" evaluates as true under
  sequential check — this is a specification violation.

- [ ] row_count ≥ 3
- [ ] ∀row ∈ S-table: all_4_columns_populated = true

INVARIANT: Do not advance to Phase 2 until both postconditions are independently satisfied.

VIOLATION CONSEQUENCE — IR-01 text verbatim at postcondition enforcement:
"AGENT produces signal rows without prior stakeholder grounding."
Phase 1 postcondition is satisfied only when both conditions above hold independently.

---

## PHASE 2 — SIGNAL PLAN PRODUCTION

OVERRIDE: IR-02 ("AGENT uses priority vocabulary { 'high', 'medium', 'low' }")
OVERRIDE: IR-05 ("AGENT assigns identical Owner Role to all signal rows")
PRECONDITION: Phase 1 postcondition satisfied ∧ S-table handoff present. [ ]

FORM 2.A — NARRATIVE RATIONALE

Constraint: Write before filling any signal rows. Minimum length: 2 sentences.

```
RATIONALE(topic="{TOPIC}"):
  why_investigation_needed: [string, min 2 sentences]
  decision_informed: [string, name the decision explicitly]
```

SPECIFICATION 2.B — FIELD SCHEMA

DEFINITION: FIELD SCHEMA defines the type constraints for each field in the signal
  table. Row order defines column order. F-01 occupies the leftmost column.
INVARIANT: ∀signal_row: all field constraints in FIELD SCHEMA must be satisfied.

| ID   | Field              | Type Constraint                                                  | Decision_State_Anchor                                                              | Immediate_Violation                          | Downstream_Effect                                              |
|------|--------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| F-01 | Priority           | Enum { essential, recommended, optional }                        | essential := consumer_cannot_decide; recommended := quality_risk_accepted; optional := consumer_decides_unaffected | Schema violation; strategy malformed | Strategy unusable as commit gate; parsers emit wrong signals  |
| F-02 | Namespace          | Enum { scout, draft, review, flow, trace, prove, listen, program, topic } | —                                                                         | Invalid value; routing_error                 | Signal routed to wrong executor at runtime                     |
| F-03 | Skill              | string; must name a skill defined under F-02 namespace           | —                                                                                  | Undefined skill; execution_failure           | Signal uncollectable; evidence gap invisible                   |
| F-04 | Item_Name          | Regex: `{topic}-{signal}-{date}\.md`                             | —                                                                                  | Format_violation; path_unresolvable          | Strategy unreachable by path-based tools                       |
| F-05 | Producer_Consumer  | Format: `{owner_role} → {decision_maker_role}`; Consumer ∈ S-table.Decision_Maker_Role | —                                                              | Orphan_consumer; traceability_broken         | Ownership undefined; signals lack decision accountability      |
| F-06 | Stakeholder_Ref    | Ref to S-NN ∈ S-table.Row_ID                                     | —                                                                                  | Orphan_signal; no_stakeholder_basis          | Signal disconnected from risk motivation                       |

SPECIFICATION 2.C — COVERAGE SCHEMA

DEFINITION: COVERAGE SCHEMA defines aggregate constraints over the complete set
  of signal rows. COV violations cannot be caught at the row level.

| ID     | Aggregate Constraint                                        | Min | Immediate_Violation                    | Downstream_Effect                              |
|--------|-------------------------------------------------------------|-----|----------------------------------------|------------------------------------------------|
| COV-01 | COUNT(row.Priority == essential) ≥ 1                        | 1   | Commit gate has no essential signals   | Feature ships ungated                          |
| COV-02 | CARDINALITY(row.Namespace) ≥ 2                              | 2   | Single-namespace plan                  | Coverage gaps structurally undetectable        |
| COV-03 | CARDINALITY(row.Producer in F-05) ≥ 2                       | 2   | Single-owner strategy                  | Cross-functional gaps invisible                |
| COV-04 | LENGTH(Form_2.A.why_investigation_needed) ≥ 2_sentences     | 2s  | Rationale absent                       | Signal relevance unverifiable by reviewers     |

PRE-WRITE GATE — Precondition for writing signal rows.
Cite F-NN and COV-NN identifiers directly:

- [ ] F-01: ∀rows: Priority ∈ {essential, recommended, optional}
- [ ] F-02: ∀rows: Namespace ∈ valid_enum
- [ ] F-03: ∀rows: Skill is a named skill under its Namespace
- [ ] F-04: ∀rows: Item_Name matches regex
- [ ] F-05: ∀rows: Consumer ∈ S-table.Decision_Maker_Role (verbatim)
- [ ] F-06: ∀rows: Stakeholder_Ref ∈ S-table.Row_ID
- [ ] COV-01: COUNT(essential) ≥ 1
- [ ] COV-02: CARDINALITY(Namespace) ≥ 2
- [ ] COV-03: CARDINALITY(Producer) ≥ 2
- [ ] COV-04: Form_2.A length ≥ 2 sentences

FORM 2.D — SIGNAL TABLE

Column order is defined by FIELD SCHEMA row order: F-01=Priority (leftmost).

| Priority | Namespace | Skill | Item_Name | Producer_Consumer | Stakeholder_Ref |
|----------|-----------|-------|-----------|-------------------|-----------------|
|          |           |       |           |                   |                 |

POSTCONDITION (Exit Gate):
- [ ] PRE-WRITE GATE (F-01–F-06, COV-01–COV-04) all satisfied
- [ ] FORM 2.D row_count ≥ 1
- [ ] COV-01 satisfied: ≥ 1 essential row confirmed
- [ ] F-05 postcondition: Consumer value appears verbatim in FORM 1.A

VIOLATION CONSEQUENCE — IR-02 text verbatim at postcondition enforcement:
"AGENT uses priority vocabulary { 'high', 'medium', 'low' }."
Phase 2 postcondition satisfied only when all four conditions above hold.

---

## PHASE 3 — COMMIT GATE PRODUCTION

OVERRIDE: IR-03 ("AGENT produces commit gate as inline prose within signal plan section")
PRECONDITION: Phase 2 postcondition satisfied ∧ signal_table handoff present. [ ]

FORM 3.A — COMMIT GATE BLOCK

```
COMMIT_GATE(topic="{TOPIC}"):
  authorized_when:
    required_signals:                # essential only
      - item_name: [string]
        path: simulations/{TOPIC}/[item_name]
    permitted_after_commit:          # recommended + optional
      - [item_name]
  enforcement: "no design commit until required_signals exist at declared paths"
```

POSTCONDITION (Exit Gate):
- [ ] FORM 3.A written as standalone section (not inline in Phase 2)
- [ ] required_signals list contains ≥ 1 entry
- [ ] enforcement field is a condition, not an aspiration

VIOLATION CONSEQUENCE — IR-03 text verbatim: "AGENT produces commit gate as inline
prose within signal plan section." Phase 3 postcondition satisfied only when block
is structurally isolated and all conditions hold.

---

## PHASE 4 — ARTIFACT WRITE

OVERRIDE: IR-04 ("AGENT produces item names without adherence to naming convention")
PRECONDITION: Phase 3 postcondition satisfied ∧ commit_gate_block handoff present. [ ]

WRITE simulations/TOPICS.md:
  Append row: | {TOPIC} | active | simulations/{TOPIC}/strategy.md | {description} |

WRITE simulations/{TOPIC}/strategy.md:
  Required sections: Rationale | Stakeholder Map | INERTIA REGISTER | Signal Plan | Commit Gate
  INVARIANT: ∀item_name in Signal Plan: matches regex `{topic}-{signal}-{date}\.md`

POSTCONDITION (Exit Gate):
- [ ] OUTPUT-1: simulations/TOPICS.md contains row for {TOPIC}
- [ ] OUTPUT-2: simulations/{TOPIC}/strategy.md exists at correct path
- [ ] ∀item_names in OUTPUT-2: regex_compliant = true
- [ ] All 5 required sections present in OUTPUT-2

VIOLATION CONSEQUENCE — IR-04 text verbatim: "AGENT produces item names without
adherence to naming convention." Phase 4 postcondition satisfied only when all
four conditions above are verified.
```

---

---

## Variation Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 | Y | Y | Y | Y | Y | TOPICS.md write in all |
| C-02 | Y | Y | Y | Y | Y | strategy.md at correct path |
| C-03 | Y | Y | Y | Y | Y | All 5 fields in signal table |
| C-04 | Y | Y | Y | Y | Y | essential/recommended/optional enforced |
| C-05 | Y | Y | Y | Y | Y | COV-01 in all |
| C-06 | Y | Y | Y | Y | Y | COV-02: ≥ 2 namespaces |
| C-07 | Y | Y | Y | Y | Y | Narrative rationale phase/section |
| C-08 | Y | Y | Y | Y | Y | COV-03 + F-05 in all |
| C-09 | Y | Y | Y | Y | Y | Commit Gate phase in all |
| C-10 | Y | Y | Y | Y | Y | Naming convention in F-04 |
| C-11 | Y | Y | Y | Y | Y | Pre-write gate checkboxes |
| C-12 | Y | Y | Y | Y | Y | Consequence framing on F-01 |
| C-13 | Y | Y | Y | Y | Y | Commit Gate as dedicated section |
| C-14 | Y | Y | Y | Y | Y | All constraints carry failure modes |
| C-15 | Y | Y | Y | Y | Y | Phase 1 stakeholder table is opener |
| C-16 | Y | Y | Y | Y | Y | All criteria enforced structurally |
| C-17 | Y | Y | Y | Y | Y | Phase 1 fill-in table, not static |
| C-18 | Y | Y | Y | Y | Y | FIELD SCHEMA + COVERAGE SCHEMA |
| C-19 | Y | Y | Y | Y | Y | F-06 Stakeholder Ref column |
| C-20 | Y | Y | Y | Y | Y | Immediate + Downstream columns |
| C-21 | Y | Y | Y | Y | Y | Per-phase exit gates throughout |
| C-22 | Y | Y | Y | Y | Y | ≥3 row count enforced at exit gate |
| C-23 | Y | Y | Y | Y | Y | F-NN and COV-NN IDs in schemas |
| C-24 | Y | Y | Y | Y | Y | Pipeline overview table |
| C-25 | Y | Y | Y | Y | Y | Commit Gate = Phase 3 |
| C-26 | Y | Y | Y | Y | Y | "Read before executing" directive |
| C-27 | Y | Y | Y | Y | Y | F-NN/COV-NN cited at multiple gates |
| C-28 | Y | Y | Y | Y | Y | Row count AND column completeness separate |
| C-29 | Y | Y | Y | Y | Y | Consequence column in pipeline table |
| C-30 | Y | Y | Y | Y | Y | Independence instruction explicit |
| C-31 | Y | Y | Y | Y | Y | Priority column leftmost |
| C-32 | Y | Y | Y | Y | Y | First-person consequence framing |
| C-33 | Y | Y | Y | Y | Y | Sequential-treatment failure named |
| C-34 | Y | Y | Y | Y | Y | Schema row order → column order stated |
| C-35 | Y | Y | Y | Y | Y | Consumer-decision anchor in F-01 |
| C-36 | Y | Y | Y | Y | Y | Producer→Consumer in F-05 |
| C-37 | Y | Y | Y | Y | Y | Handoff Artifact column in overview |
| C-38 | Y | Y | Y | Y | Y | Team Default column in overview |
| C-39 | Y | Y | Y | Y | Y | All 3 priority tiers anchored in F-01 |
| C-40 | Y | Y | Y | Y | Y | F-05 Consumer verbatim check in Phase 2 exit |
| C-41 | Y | Y | Y | Y | Y | Recovery Cost column in overview |
| C-42 | Y | Y | Y | Y | Y | Named INERTIA REGISTER block with IR-NN IDs |
| C-43 | Y | Y | Y | Y | Y | "This phase overrides IR-NN" per phase |
| C-44 | Y | Y | Y | Y | Y | Full IR-NN text reproduced at exit gates |

**Predicted aspirational score**: 36/36 = 10.0 (all 5 variations target full coverage)

**Axis differentiation** (primary testable difference per variation):

| Variation | What Changes | What to Watch For |
|-----------|-------------|-------------------|
| V-01 | Role sequence: S-table is structural root; every element traces back | Consumer traceability quality; role diversity in complex topics |
| V-02 | Prose-first rationale: rationale before signals, not after | Rationale depth; does pre-signal prose improve C-07 quality? |
| V-03 | Lifecycle emphasis: ENTRY + EXIT labeled at every boundary | Gate skip rate; does dual-boundary labeling reduce silent advances? |
| V-04 | Inertia framing: each row in S-table maps to IR-NN; signals defeat inertia | IR-NN coverage per signal row; inertia-stakeholder coupling quality |
| V-05 | Formal register: specification language, typed forms, no prose | Structural compliance consistency across diverse topic inputs |
