# topic-new — Round 15 Variations (V-01 through V-05)
# Rubric target: v13 (36 aspirational criteria, denominator 36)
# Date: 2026-03-15

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Schema-as-sole-truth | When phases contain zero inline prose constraints — every rule lives exclusively in named schema rows, phases reference only schema IDs — structural drift between prose instruction and schema definition is architecturally impossible; C-16 reaches its logical endpoint when the structural mechanism IS the schema |
| V-02 | Inertia vulnerability linkage | Adding a "Stakeholder Most Harmed" column to INERTIA REGISTER — naming who suffers if each default is not overridden — and reproducing that role at every per-phase override directive and exit gate verbatim reproduction produces stronger C-43/C-44 compliance because human consequence is visible at every enforcement point, not only the abstract behavioral default |
| V-03 | Failure cascade registry | Moving all execution-time failure consequences from the pipeline overview table into a dedicated pre-pipeline FAILURE CASCADE REGISTRY (FC-NN IDs, mirroring INERTIA REGISTER pattern) makes failure modes consultable by ID throughout execution — the same architectural improvement C-42 made to team inertia defaults, applied to model-execution failures |
| V-04 | Inertia vulnerability + Commitment block gate | V-02's vulnerable-role INERTIA REGISTER combined with COMMITMENT BLOCK gate topology (fill-in structured templates instead of checkbox lists) creates the strongest phase-boundary enforcement: vulnerable roles make inertia consequences human-specific, and active authorship of commitment blocks produces stronger commitment than passive checkbox ticking |
| V-05 | Failure cascade registry + Schema-as-sole-truth | Maximum structural compression: INERTIA REGISTER + FAILURE CASCADE REGISTRY as the two pre-pipeline registries with zero prose in phases (schema citations only); all constraint text lives in named registries; all references are by ID; no inline prose can drift; tests whether maximum ID-citation density produces the most consistent structural compliance |

---

---

## V-01 — Schema-as-Sole-Truth Axis

**Axis**: Schema-as-sole-truth
**Hypothesis**: When phases contain zero inline prose constraints — every rule lives exclusively in FIELD SCHEMA, COVERAGE SCHEMA, or PHASE SCHEMA rows, and phases reference only schema IDs — structural drift between prose instruction and schema definition is architecturally impossible. C-16 (every criterion enforced by structural mechanism) reaches its logical endpoint when the structural mechanism IS the schema lookup itself. No prose can drift because no prose exists outside schema rows.
**Key Structural Difference**: Phase 1 has a STAKEHOLDER SCHEMA (SK-01–SK-04) defining each column constraint. Phase 2 has no prose rules — only FIELD SCHEMA + COVERAGE SCHEMA citations. Gate checkboxes cite schema IDs only; constraint text is retrieved by ID lookup. This creates a single source of truth for every enforced constraint.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IDs. Phase directives and exit gates cite these by ID.
> Read this register before reading the pipeline overview.

| ID    | Default Behavior                                                              | Override Active In |
|-------|-------------------------------------------------------------------------------|--------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition               | Phase 1            |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context     | Phase 2            |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation    | Phase 3            |
| IR-04 | Omit artifact naming convention; use freeform item names                      | Phase 4            |
| IR-05 | Assign all signals to a single generic owner role                             | Phase 2            |

---

## STAKEHOLDER SCHEMA

> Phase 1 table constraint registry. SK-NN row order = column order in Phase 1 table.
> These rows are the sole source of column constraints for Phase 1.
> Do not write Phase 1 column constraints in prose anywhere outside this schema.

| ID    | Column Name             | Constraint                                                                | Immediate Failure                            | Downstream Effect                                             |
|-------|-------------------------|---------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------------------|
| SK-01 | Row ID                  | Must be S-NN (S-01, S-02, ... S-NN)                                       | Row unaddressable by downstream F-05/F-06    | Consumer traceability in Phase 2 fails at lookup time         |
| SK-02 | Decision-Maker Role     | Named role accountable for a real decision; not "stakeholder" or "user"   | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for the signal |
| SK-03 | Risk Exposure           | What breaks for this role if the topic is skipped — specific harm         | Empty risk = no motivation for signal        | Pruning has no ground truth; coverage gaps invisible          |
| SK-04 | What Decision Informed  | The concrete decision this topic provides evidence for                    | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance to any decision |

---

## FIELD SCHEMA

> Phase 2 signal table constraint registry. F-NN row order = column order in signal table.
> F-01 is the leftmost column. Fill left to right.
> These rows are the sole source of column constraints for the signal table.
> Do not restate column constraints in prose anywhere outside this schema.

| ID   | Field               | Constraint                                                          | Decision-State Anchor                                                                                    | Immediate Failure                                  | Downstream Effect                                               |
|------|---------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                 | essential=consumer cannot decide without this (decision blocked); recommended=consumer decides with increased exposure (quality risk accepted); optional=consumer decides unaffected (supplementary enrichment only) | Schema violation; row malformed | Strategy unusable as commit gate; downstream parsers emit wrong signals |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic    | —                                                                                                        | Invalid namespace; routing fails                   | Signal routed to wrong executor at runtime                       |
| F-03 | Skill               | Named skill existing under stated namespace                         | —                                                                                                        | Non-existent skill reference                       | Signal uncollectable; evidence gap invisible                     |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form | —                                                                                                        | Format check fails; artifact path unresolvable     | Strategy unreachable by path-based tools                         |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer value must appear verbatim as SK-02 in Phase 1 table | —                                                                                       | Orphan consumer; traceability broken               | Ownership undefined; signals accumulate without decision accountability |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 table                                      | —                                                                                                        | Orphan signal; no stakeholder basis                | Signal disconnected from risk motivation; pruning ungrounded    |

---

## COVERAGE SCHEMA

> Phase 2 coverage constraint registry. COV-NN rows are the sole source of
> coverage constraints. Do not restate coverage constraints in prose outside this schema.

| ID     | Constraint                          | Minimum      | Immediate Failure                               | Downstream Effect                                         |
|--------|-------------------------------------|--------------|-------------------------------------------------|-----------------------------------------------------------|
| COV-01 | Signals marked essential            | ≥ 1          | No commit gate definable                        | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces                 | ≥ 2          | Single-namespace plan; structural blind spot    | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (via F-05)  | ≥ 2          | Single-owner strategy; collapses on change      | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale written         | ≥ 2 sentences| Decision context absent                         | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose          | Handoff Artifact              | Exit Gate (summary)                              | If I Skip This Phase, I Will…                         | Team Default (→ IR-NN) | Recovery Cost If Caught Late                              |
|-------|------------------|-------------------------------|--------------------------------------------------|-------------------------------------------------------|------------------------|-----------------------------------------------------------|
| 1     | Stakeholder Map  | S-table (≥3 rows)            | SK-01–SK-04 compliant; row count + col completeness independently | author orphan signal rows with no role ground truth | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05 and F-06 in Phase 2; re-run Phase 3; re-write strategy.md |
| 2     | Signal Plan      | Signal table rows             | F-01–F-06 + COV-01–COV-04 pass; Consumer traces S-table | produce malformed strategy unusable as commit gate | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md      |
| 3     | Commit Gate      | Gate definition block         | Gate names ≥1 essential signal; structurally isolated | ship feature with no enforced readiness condition  | → IR-03                | Re-run Phase 3; re-write strategy.md commit gate section  |
| 4     | Artifact Write   | TOPICS.md row + strategy.md   | Both files at correct paths; item names follow F-04 | topic unregistered; strategy unreachable            | → IR-04                | Re-write both artifacts; re-run path verification          |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01**: "Skip stakeholder mapping; author signals from feature intuition."
> And IR-05: "Assign all signals to a single generic owner role."
>
> All column constraints are in STAKEHOLDER SCHEMA rows SK-01–SK-04.
> No additional column instructions apply.

**Entry gate**: INERTIA REGISTER confirmed read. STAKEHOLDER SCHEMA rows SK-01–SK-04 confirmed read. [ ]

Fill in the following table. Consult SK-NN for each column's constraint.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: What Decision Informed |
|---------------|---------------------------|----------------------|-------------------------------|
| S-01          |                           |                      |                               |
| S-02          |                           |                      |                               |
| S-03          |                           |                      |                               |
| S-NN          | (add rows)                |                      |                               |

**Exit gate** — check INDEPENDENTLY:

> Check these two conditions INDEPENDENTLY. Do not advance until both are
> checked separately. Sequential checking produces this specific failure:
> "3 rows present, columns empty" passes as compliant — this is wrong.

- [ ] SK-01 through SK-04: Row count ≥ 3
- [ ] SK-01 through SK-04: All four columns populated in every filled row

> Do not advance until both items are checked independently, not sequentially.

**IR-01 text reproduced verbatim at exit enforcement point**:
"Skip stakeholder mapping; author signals from feature intuition."
This phase overrides that default. Phase 1 is complete only when both
independent conditions above are satisfied.

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary from project-management context."
> And IR-05: "Assign all signals to a single generic owner role."
>
> All field constraints are in FIELD SCHEMA rows F-01–F-06.
> All coverage constraints are in COVERAGE SCHEMA rows COV-01–COV-04.
> No additional constraint instructions apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE (COV-04)

> Required fill-in step. Constraint: COV-04 (≥ 2 sentences).
> Failure modes: see COV-04 row in COVERAGE SCHEMA.

> [Model fills here — minimum 2 sentences before proceeding to signal table]

### PRE-WRITE GATE

> Cite schema IDs only. Constraint text is in the schema rows above.

- [ ] F-01: Priority vocabulary valid (see F-01)
- [ ] F-02: All namespace values valid (see F-02)
- [ ] F-03: All skill values valid (see F-03)
- [ ] F-04: All item names valid (see F-04)
- [ ] F-05: All Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: All Stakeholder Ref values cite S-NN rows (see F-06)
- [ ] COV-01: ≥ 1 essential signal (see COV-01)
- [ ] COV-02: ≥ 2 distinct namespaces (see COV-02)
- [ ] COV-03: ≥ 2 distinct Producer roles (see COV-03)
- [ ] COV-04: Narrative rationale written above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost.
> Fill left to right. Constraint for each column: see F-NN row.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|
|                 |                  |              |                  |                           |                        |

**Exit gate**: All pre-write gate items above cleared. Signal table contains ≥ 1 row. F-05 Consumer values verified against Phase 1 SK-02 column.

**IR-02 text reproduced verbatim at exit enforcement point**:
"Use 'high/medium/low' priority vocabulary from project-management context."
This phase overrides that default. Every Priority cell must contain exactly
one of: essential / recommended / optional.

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03**: "Collapse commit gate into signal plan section with no structural isolation."

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

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

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named explicitly.
Gate expressed as a condition, not as a list of aspirations.

**IR-03 text reproduced verbatim at exit enforcement point**:
"Collapse commit gate into signal plan section with no structural isolation."
This phase overrides that default. Phase 3 is complete only when the commit
gate occupies this standalone phase with its own named conditions.

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04**: "Omit artifact naming convention; use freeform item names."

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
[paste COV-04 narrative from Phase 2]

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
follow constraint F-04: `{topic}-{signal}-{date}.md`.

**IR-04 text reproduced verbatim at exit enforcement point**:
"Omit artifact naming convention; use freeform item names."
This phase overrides that default. Phase 4 is complete only when both
artifacts exist at declared paths with item names satisfying F-04.
```

---

---

## V-02 — Inertia Vulnerability Linkage Axis

**Axis**: Inertia vulnerability linkage
**Hypothesis**: Adding a "Stakeholder Most Harmed" column to INERTIA REGISTER — naming the role category that suffers most when each default is not overridden — and propagating that role name into per-phase override directives and exit gate verbatim reproductions produces stronger C-43/C-44 compliance because human consequence is visible at every enforcement point. An abstract behavioral default ("skip stakeholder mapping") is easier to rationalize past than a named-role consequence ("Product Manager owns commitment scope; this default removes their ground truth").
**Key Structural Difference**: INERTIA REGISTER has a fourth column "Stakeholder Most Harmed"; per-phase "This phase overrides IR-NN" directive includes the vulnerable role; exit gate verbatim reproduction includes the full register row text (default + harmed role).

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IDs. Read this entire register before the pipeline overview.
> All phase directives and exit gates cite these rows by ID.
> The Stakeholder Most Harmed column names who suffers when the default is not overridden.

| ID    | Default Behavior                                                              | Override Active In | Stakeholder Most Harmed                                            |
|-------|-------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition               | Phase 1            | Product Manager — loses commit scope ground truth                  |
| IR-02 | Use "high/medium/low" priority vocabulary                                     | Phase 2            | Design Lead — cannot gate design commit on unparseable priority    |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation    | Phase 3            | Engineering Lead — no enforced readiness condition at commit time  |
| IR-04 | Omit artifact naming convention; use freeform item names                      | Phase 4            | All downstream consumers — strategy unreachable by path-based tools |
| IR-05 | Assign all signals to a single generic owner role                             | Phase 2            | Cross-functional team — gaps invisible when all ownership collapses |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose          | Handoff Artifact              | Exit Gate (summary)                              | If I Skip This Phase, I Will…                            | Team Default (→ IR-NN) | Recovery Cost If Caught Late                                |
|-------|------------------|-------------------------------|--------------------------------------------------|----------------------------------------------------------|------------------------|--------------------------------------------------------------|
| 1     | Stakeholder Map  | S-table (≥3 rows, 4 cols)    | ≥3 rows AND 4 cols filled, independently checked | author orphan signal rows with no role ground truth      | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05 and F-06; re-run Phases 2–3; re-write files |
| 2     | Signal Plan      | Signal table rows             | F-01–F-06 + COV-01–COV-04; Consumer traces S-table | produce malformed strategy unusable as commit gate     | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md        |
| 3     | Commit Gate      | Gate definition block         | Gate names ≥1 essential; structurally isolated   | ship feature with no enforced readiness condition        | → IR-03                | Re-run Phase 3; re-write commit gate section                 |
| 4     | Artifact Write   | TOPICS.md row + strategy.md   | Both files correct path; item names follow convention | topic unregistered; strategy unreachable             | → IR-04                | Re-write both artifacts; re-run path verification            |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01**: "Skip stakeholder mapping; author signals from feature intuition."
> IR-01 Stakeholder Most Harmed: **Product Manager — loses commit scope ground truth.**
>
> And IR-05: "Assign all signals to a single generic owner role."
> IR-05 Stakeholder Most Harmed: **Cross-functional team — gaps invisible when all ownership collapses.**
>
> Every signal row in Phase 2 must trace its Owner Role and Consumer to a specific
> row in this table. Role differentiation emerges here — not from a late checklist.

**Entry gate**: INERTIA REGISTER confirmed read, including Stakeholder Most Harmed column. [ ]

Fill in the following table. Every column is required.

| Row ID | Decision-Maker Role | Risk Exposure (what breaks for them if topic is skipped) | What Decision This Topic Informs For Them |
|--------|---------------------|----------------------------------------------------------|-------------------------------------------|
| S-01   |                     |                                                          |                                           |
| S-02   |                     |                                                          |                                           |
| S-03   |                     |                                                          |                                           |
| S-NN   | (add rows)          |                                                          |                                           |

> **Check these two conditions INDEPENDENTLY. Do not advance until both are
> checked separately. Sequential checking produces this specific failure:
> "3 rows present, columns empty" passes as compliant — this is wrong.**

- [ ] Row count ≥ 3 (minimum stakeholder breadth enforced)
- [ ] All four columns populated in every filled row (completeness enforced)

> Do not advance until both items are checked independently, not sequentially.

**IR-01 text reproduced verbatim at exit enforcement point** (full register row):
Default: "Skip stakeholder mapping; author signals from feature intuition."
Stakeholder Most Harmed: "Product Manager — loses commit scope ground truth."
This phase overrides that default. Phase 1 is complete only when both
independent conditions above are satisfied.

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary."
> IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
>
> And IR-05: "Assign all signals to a single generic owner role."
> IR-05 Stakeholder Most Harmed: **Cross-functional team — gaps invisible when all ownership collapses.**

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

Write ≥ 2 sentences explaining why this topic needs investigation and what decision
it informs. Required fill-in step — not optional prose.

> [Model fills here — minimum 2 sentences before proceeding to schema]

### FIELD SCHEMA

> Column order = row order. F-01 is the leftmost column. Fill left to right.

| ID   | Field               | Constraint                                                          | Decision-State Anchor                                                                                      | Immediate Failure                                  | Downstream Effect                                               |
|------|---------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                 | essential=consumer cannot decide without this (decision blocked); recommended=consumer decides with increased exposure (quality risk accepted); optional=consumer decides unaffected (supplementary enrichment only) | Schema violation; strategy malformed | Strategy unusable as commit gate; Design Lead cannot gate commit |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic    | —                                                                                                          | Invalid namespace; routing fails                   | Signal routed to wrong executor at runtime                       |
| F-03 | Skill               | Named skill under stated namespace                                  | —                                                                                                          | Non-existent skill reference                       | Signal uncollectable; evidence gap invisible                     |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template              | —                                                                                                          | Format fails; path unresolvable                    | Strategy unreachable by path-based tools                         |
| F-05 | Producer → Consumer | `{role} → {decision-maker-role}`; Consumer verbatim in Phase 1 S-table | —                                                                                                     | Orphan consumer; traceability broken               | Ownership undefined; signals accumulate without accountability   |
| F-06 | Stakeholder Ref     | S-NN row from Phase 1                                               | —                                                                                                          | Orphan signal; no stakeholder basis                | Signal disconnected from risk motivation; pruning ungrounded     |

### COVERAGE SCHEMA

| ID     | Constraint                  | Minimum      | Immediate Failure                            | Downstream Effect                                       |
|--------|-----------------------------|--------------|----------------------------------------------|---------------------------------------------------------|
| COV-01 | Signals marked essential    | ≥ 1          | No commit gate exists                        | Feature ships ungated; Engineering Lead has no gate     |
| COV-02 | Distinct namespaces         | ≥ 2          | Single-namespace plan; blind spot            | Gap analysis cannot detect coverage holes               |
| COV-03 | Distinct Producer roles     | ≥ 2          | Single-owner collapse                        | Cross-functional gaps invisible; IR-05 harm materializes|
| COV-04 | Narrative rationale written | ≥ 2 sentences| Context absent                               | Signal relevance unverifiable for all stakeholders      |

### PRE-WRITE GATE

- [ ] F-01: Priority vocabulary valid (essential / recommended / optional only)
- [ ] F-02: Namespace values valid
- [ ] F-03: Skill values valid (named skills under their namespace)
- [ ] F-04: Item names follow `{topic}-{signal}-{date}.md`
- [ ] F-05: Consumer values appear verbatim in Phase 1 S-table
- [ ] F-06: Stakeholder Refs cite S-NN rows
- [ ] COV-01: ≥ 1 essential signal present
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct Producer roles
- [ ] COV-04: Narrative rationale written above

### SIGNAL TABLE

> Priority is the leftmost column. Fill left to right.

| Priority | Namespace | Skill | Item Name | Producer → Consumer | Stakeholder Ref |
|----------|-----------|-------|-----------|---------------------|-----------------|
|          |           |       |           |                     |                 |

**Exit gate**: All pre-write checkboxes cleared. Signal table ≥ 1 row. F-05 Consumer
verified verbatim against Phase 1 S-table.

**IR-02 text reproduced verbatim at exit enforcement point** (full register row):
Default: "Use 'high/medium/low' priority vocabulary."
Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."
This phase overrides that default. Every Priority cell must contain exactly one
of: essential / recommended / optional.

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03**: "Collapse commit gate into signal plan section with no structural isolation."
> IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

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

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named explicitly.
Gate expressed as a condition, not as a list of aspirations.

**IR-03 text reproduced verbatim at exit enforcement point** (full register row):
Default: "Collapse commit gate into signal plan section with no structural isolation."
Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."
This phase overrides that default. Phase 3 is complete only when the commit gate
occupies this standalone phase with its own named conditions.

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04**: "Omit artifact naming convention; use freeform item names."
> IR-04 Stakeholder Most Harmed: **All downstream consumers — strategy unreachable by path-based tools.**

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

**Exit gate**: Both files written at correct paths. All item names follow
`{topic}-{signal}-{date}.md`.

**IR-04 text reproduced verbatim at exit enforcement point** (full register row):
Default: "Omit artifact naming convention; use freeform item names."
Stakeholder Most Harmed: "All downstream consumers — strategy unreachable by path-based tools."
This phase overrides that default. Phase 4 is complete only when both artifacts
exist at declared paths with correctly formatted item names.
```

---

---

## V-03 — Failure Cascade Registry Axis

**Axis**: Failure cascade registry
**Hypothesis**: Moving all execution-time failure consequences from the pipeline overview table into a dedicated pre-pipeline FAILURE CASCADE REGISTRY (FC-NN IDs, mirroring the INERTIA REGISTER pattern) and having pipeline rows cite FC-NN makes failure modes consultable by ID throughout execution — the same architectural improvement C-42 made to team inertia defaults, applied to model-execution failures. A model executing Phase 3 can look up FC-05 to see the full cascade of consequences for commit gate collapse without decoding pipeline table cells.
**Key Structural Difference**: FAILURE CASCADE REGISTRY block (FC-01 through FC-06) precedes the pipeline overview. Pipeline consequence column carries FC-NN citations. Per-phase consequence warnings reproduce FC-NN text verbatim analogous to IR-NN reproduction in C-44.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IDs. Read before pipeline overview.

| ID    | Default Behavior                                                              | Override Active In |
|-------|-------------------------------------------------------------------------------|--------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition               | Phase 1            |
| IR-02 | Use "high/medium/low" priority vocabulary                                     | Phase 2            |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation    | Phase 3            |
| IR-04 | Omit artifact naming convention; use freeform item names                      | Phase 4            |
| IR-05 | Assign all signals to a single generic owner role                             | Phase 2            |

---

## FAILURE CASCADE REGISTRY

> Pre-pipeline. Stable IDs. Execution-time failure modes — distinct from team inertia
> defaults. These are model-execution failures (what breaks when the model skips or
> misexecutes a constraint), not team behavioral defaults.
> Pipeline consequence column cites FC-NN. Phase exit gates reproduce FC-NN text verbatim.

| ID    | Failure Mode                                     | Phase Detectable | Immediate Consequence                            | Downstream Effect                                      | Recovery Steps                                              |
|-------|--------------------------------------------------|------------------|-------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------|
| FC-01 | Priority vocabulary substitution (high/med/low)  | Phase 2 pre-write| Schema validation fails; row malformed          | Strategy unusable as commit gate                       | Re-fill signal table; re-run Phase 3                        |
| FC-02 | Orphaned Consumer (F-05 value not in S-table)    | Phase 2 exit     | Consumer traceability broken                    | Signal ownership undefined; accountability gap          | Re-run Phase 1; re-derive F-05; re-run Phase 2 exit         |
| FC-03 | Silent stakeholder table (rows empty, count met) | Phase 1 exit     | Column completeness check fails                 | Phase 2 role differentiation has no ground truth       | Re-fill Phase 1 table; re-run Phase 2 role columns          |
| FC-04 | Commit gate collapsed into signal plan section   | Phase 3 exit     | No structurally isolated gate exists            | Engineering has no enforceable readiness condition      | Re-run Phase 3 as dedicated phase; re-write strategy.md     |
| FC-05 | Freeform item names (no artifact convention)     | Phase 4 exit     | Path format check fails                         | Strategy unreachable by path-based tools                | Re-fill item name column; re-write strategy.md              |
| FC-06 | Single-role strategy (all signals same owner)    | Phase 2 pre-write| COV-03 fails; cross-functional gap undetectable | Strategy survives review but masks role coverage gaps   | Re-derive Producer roles from Phase 1 S-table; re-run check |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose          | Handoff Artifact            | Exit Gate (summary)                                         | If I Skip This Phase, I Will… | Team Default (→ IR-NN) | Recovery Cost (→ FC-NN)              |
|-------|------------------|-----------------------------|-------------------------------------------------------------|-------------------------------|------------------------|--------------------------------------|
| 1     | Stakeholder Map  | S-table (≥3 rows, 4 cols)  | ≥3 rows AND all 4 columns filled, checked independently     | author orphan signal rows     | → IR-01, IR-05         | → FC-03 (silent table); → FC-02 chain|
| 2     | Signal Plan      | Signal table rows           | F-01–F-06 + COV-01–COV-04; Consumer traces S-table          | produce malformed strategy    | → IR-02, IR-05         | → FC-01 (vocab); → FC-02; → FC-06   |
| 3     | Commit Gate      | Gate definition block       | Gate names ≥1 essential signal; structurally isolated       | ship without readiness gate   | → IR-03                | → FC-04 (gate collapse)              |
| 4     | Artifact Write   | TOPICS.md row + strategy.md | Both files correct path; item names follow convention       | topic unregistered            | → IR-04                | → FC-05 (freeform names)             |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01**: "Skip stakeholder mapping; author signals from feature intuition."
> And IR-05: "Assign all signals to a single generic owner role."

**Entry gate**: INERTIA REGISTER and FAILURE CASCADE REGISTRY confirmed read. [ ]

Fill in the following table. Every column is required.

| Row ID | Decision-Maker Role | Risk Exposure (what breaks for them if topic is skipped) | What Decision This Topic Informs For Them |
|--------|---------------------|----------------------------------------------------------|-------------------------------------------|
| S-01   |                     |                                                          |                                           |
| S-02   |                     |                                                          |                                           |
| S-03   |                     |                                                          |                                           |
| S-NN   | (add rows)          |                                                          |                                           |

> **Check these two conditions INDEPENDENTLY. Do not advance until both are
> checked separately. Sequential checking produces this specific failure:
> "3 rows present, columns empty" passes as compliant — this is wrong.**

- [ ] Row count ≥ 3 (minimum stakeholder breadth enforced)
- [ ] All four columns populated in every filled row (completeness enforced independently of row count)

> Do not advance until both items are checked independently, not sequentially.

**IR-01 text reproduced verbatim at exit enforcement point**:
"Skip stakeholder mapping; author signals from feature intuition."
This phase overrides that default. Phase 1 is complete only when both
independent conditions above are satisfied.

**FC-03 text reproduced verbatim at exit enforcement point** (failure cascade risk):
Failure Mode: "Silent stakeholder table (rows empty, count met)."
Immediate: "Column completeness check fails."
Downstream: "Phase 2 role differentiation has no ground truth."

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary."
> And IR-05: "Assign all signals to a single generic owner role."

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

Write ≥ 2 sentences explaining why this topic needs investigation and what decision
it informs. Required fill-in step.

> [Model fills here — minimum 2 sentences before proceeding to schema]

### FIELD SCHEMA

> Column order = row order. F-01 is the leftmost column. Fill left to right.

| ID   | Field               | Constraint                                                          | Decision-State Anchor                                                                                      | Immediate Failure                                  | Downstream Effect                                              |
|------|---------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                 | essential=consumer cannot decide without this (decision blocked); recommended=consumer decides with increased exposure (quality risk accepted); optional=consumer decides unaffected (supplementary enrichment only) | Schema violation; strategy malformed → FC-01 | Strategy unusable as commit gate |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic    | —                                                                                                          | Invalid namespace; routing fails                   | Signal routed to wrong executor at runtime                     |
| F-03 | Skill               | Named skill under stated namespace                                  | —                                                                                                          | Non-existent skill reference                       | Signal uncollectable; evidence gap invisible                   |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template              | —                                                                                                          | Format fails; path unresolvable → FC-05            | Strategy unreachable by path-based tools                       |
| F-05 | Producer → Consumer | `{role} → {decision-maker-role}`; Consumer verbatim in Phase 1 S-table | —                                                                                                     | Orphan consumer; traceability broken → FC-02       | Ownership undefined; accountability gap                        |
| F-06 | Stakeholder Ref     | S-NN row from Phase 1                                               | —                                                                                                          | Orphan signal; no stakeholder basis                | Signal disconnected from risk motivation                       |

### COVERAGE SCHEMA

| ID     | Constraint                  | Minimum      | Immediate Failure                            | Downstream Effect                             |
|--------|-----------------------------|--------------|----------------------------------------------|-----------------------------------------------|
| COV-01 | Signals marked essential    | ≥ 1          | No commit gate definable                     | Feature ships ungated → FC-04 risk            |
| COV-02 | Distinct namespaces         | ≥ 2          | Single-namespace plan; blind spot            | Gap analysis cannot detect coverage holes     |
| COV-03 | Distinct Producer roles     | ≥ 2          | Single-owner strategy → FC-06                | Cross-functional gaps invisible               |
| COV-04 | Narrative rationale written | ≥ 2 sentences| Context absent                               | Signal relevance unverifiable                 |

### PRE-WRITE GATE

- [ ] F-01: Priority valid — essential / recommended / optional only (FC-01 risk if failed)
- [ ] F-02: Namespaces valid
- [ ] F-03: Skills valid
- [ ] F-04: Item names follow convention (FC-05 risk if failed)
- [ ] F-05: Consumer values appear verbatim in Phase 1 S-table (FC-02 risk if failed)
- [ ] F-06: Stakeholder Refs cite S-NN rows
- [ ] COV-01: ≥ 1 essential signal
- [ ] COV-02: ≥ 2 namespaces
- [ ] COV-03: ≥ 2 Producer roles (FC-06 risk if failed)
- [ ] COV-04: Narrative rationale written

### SIGNAL TABLE

> Priority is the leftmost column. Fill left to right.

| Priority | Namespace | Skill | Item Name | Producer → Consumer | Stakeholder Ref |
|----------|-----------|-------|-----------|---------------------|-----------------|
|          |           |       |           |                     |                 |

**Exit gate**: All pre-write checkboxes cleared. Signal table ≥ 1 row. F-05 Consumer
verified verbatim in Phase 1 S-table.

**IR-02 text reproduced verbatim at exit enforcement point**:
"Use 'high/medium/low' priority vocabulary."
This phase overrides that default. Every Priority cell must contain exactly
one of: essential / recommended / optional.

**FC-01 text reproduced verbatim at exit enforcement point** (failure cascade risk):
Failure Mode: "Priority vocabulary substitution (high/med/low)."
Immediate: "Schema validation fails; row malformed."
Downstream: "Strategy unusable as commit gate."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03**: "Collapse commit gate into signal plan section with no structural isolation."

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

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

Enforcement: no design commit proceeds until REQUIRED signals exist at declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named explicitly.
Gate expressed as a condition, not as a list of aspirations.

**IR-03 text reproduced verbatim at exit enforcement point**:
"Collapse commit gate into signal plan section with no structural isolation."
This phase overrides that default. Phase 3 is complete only when the gate
occupies this standalone phase with its own named conditions.

**FC-04 text reproduced verbatim at exit enforcement point** (failure cascade risk):
Failure Mode: "Commit gate collapsed into signal plan section."
Immediate: "No structurally isolated gate exists."
Downstream: "Engineering has no enforceable readiness condition."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04**: "Omit artifact naming convention; use freeform item names."

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff artifact present. [ ]

### Write 1: simulations/TOPICS.md

Append row:

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

**Exit gate**: Both files written at correct paths. All item names follow
`{topic}-{signal}-{date}.md`.

**IR-04 text reproduced verbatim at exit enforcement point**:
"Omit artifact naming convention; use freeform item names."
This phase overrides that default. Phase 4 is complete only when both
artifacts exist at declared paths with correctly formatted item names.

**FC-05 text reproduced verbatim at exit enforcement point** (failure cascade risk):
Failure Mode: "Freeform item names (no artifact convention)."
Immediate: "Path format check fails."
Downstream: "Strategy unreachable by path-based tools."
```

---

---

## V-04 — Inertia Vulnerability + Commitment Block Gate (Combined)

**Axis**: Inertia vulnerability linkage + Gate topology (commitment block format)
**Hypothesis**: Combining V-02's vulnerable-role INERTIA REGISTER with COMMITMENT BLOCK gate topology (structured fill-in templates instead of checkbox lists) creates the strongest phase-boundary enforcement because: (a) vulnerable roles make inertia consequences human-specific at every enforcement point, and (b) commitment blocks require the model to actively author each gate field value — to declare the current status, the stakeholder at risk, and the phase decision — rather than passively ticking a box; active authorship produces demonstrably stronger commitment than passive selection.
**Key Structural Difference**: INERTIA REGISTER has a "Stakeholder Most Harmed" column. Every phase gate is a COMMITMENT BLOCK — a structured fill-in template with labeled fields: Override, Vulnerable Role, conditions with status values, and explicit ADVANCE/STOP decision.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IDs. Read this entire register before the pipeline overview.
> Stakeholder Most Harmed column: who suffers if this default is not overridden.

| ID    | Default Behavior                                                              | Override Active In | Stakeholder Most Harmed                                               |
|-------|-------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition               | Phase 1            | Product Manager — loses commit scope ground truth                     |
| IR-02 | Use "high/medium/low" priority vocabulary                                     | Phase 2            | Design Lead — cannot gate commit on unparseable priority              |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation    | Phase 3            | Engineering Lead — no enforced readiness condition at commit time     |
| IR-04 | Omit artifact naming convention; use freeform item names                      | Phase 4            | All downstream consumers — strategy unreachable by path-based tools   |
| IR-05 | Assign all signals to a single generic owner role                             | Phase 2            | Cross-functional team — gaps invisible when all ownership collapses   |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose          | Handoff Artifact            | Exit Gate (summary)                                          | If I Skip This Phase, I Will…                       | Team Default (→ IR-NN) | Recovery Cost If Caught Late                               |
|-------|------------------|-----------------------------|--------------------------------------------------------------|-----------------------------------------------------|------------------------|------------------------------------------------------------|
| 1     | Stakeholder Map  | S-table (≥3 rows, 4 cols)  | COMMITMENT BLOCK 1 cleared: row count + col completeness independently | author orphan signal rows with no role ground truth | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05/F-06; re-run Phases 2–3; re-write files |
| 2     | Signal Plan      | Signal table rows           | COMMITMENT BLOCK 2 cleared: F-01–F-06 + COV-01–COV-04; Consumer traces | produce malformed strategy unusable as commit gate | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md       |
| 3     | Commit Gate      | Gate definition block       | COMMITMENT BLOCK 3 cleared: gate names ≥1 essential; isolated | ship feature with no enforced readiness condition  | → IR-03                | Re-run Phase 3; re-write strategy.md commit gate section   |
| 4     | Artifact Write   | TOPICS.md row + strategy.md | COMMITMENT BLOCK 4 cleared: both files; item names valid     | topic unregistered; strategy unreachable            | → IR-04                | Re-write both artifacts; re-run path verification          |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01**: "Skip stakeholder mapping; author signals from feature intuition."
> IR-01 Stakeholder Most Harmed: **Product Manager — loses commit scope ground truth.**
>
> And IR-05: "Assign all signals to a single generic owner role."
> IR-05 Stakeholder Most Harmed: **Cross-functional team — gaps invisible when all ownership collapses.**

**Entry**: INERTIA REGISTER confirmed read, including Stakeholder Most Harmed column.

Fill in the following table. Every column is required.

| Row ID | Decision-Maker Role | Risk Exposure (what breaks for them if topic is skipped) | What Decision This Topic Informs For Them |
|--------|---------------------|----------------------------------------------------------|-------------------------------------------|
| S-01   |                     |                                                          |                                           |
| S-02   |                     |                                                          |                                           |
| S-03   |                     |                                                          |                                           |
| S-NN   | (add rows)          |                                                          |                                           |

```
╔═══════════════════════════════════════════════════════════════╗
║  COMMITMENT BLOCK 1 — Phase 1 Exit Gate                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Override: IR-01 ("Skip stakeholder mapping...") +           ║
║             IR-05 ("Assign all signals to single role...")    ║
║                                                               ║
║  Vulnerable if not overridden:                                ║
║    IR-01: Product Manager — loses commit scope ground truth   ║
║    IR-05: Cross-functional team — ownership gaps invisible    ║
║                                                               ║
║  Condition A — Row count ≥ 3:                                 ║
║    Status: [ PASS | FAIL ]   Actual count: ______             ║
║                                                               ║
║  Condition B — All four columns populated (every filled row): ║
║    Status: [ PASS | FAIL ]                                    ║
║                                                               ║
║  ⚠ CHECK A AND B INDEPENDENTLY. Sequential treatment yields  ║
║    this failure: "3 rows present, columns empty" → PASS.     ║
║    That result is WRONG. Each condition must clear on its     ║
║    own merits before the other is considered.                 ║
║                                                               ║
║  IR-01 text verbatim: "Skip stakeholder mapping; author       ║
║  signals from feature intuition." This phase overrides it.   ║
║                                                               ║
║  Phase 1 Decision: [ ADVANCE to Phase 2 | STOP and re-fill ] ║
╚═══════════════════════════════════════════════════════════════╝
```

Do not proceed to Phase 2 until COMMITMENT BLOCK 1 Decision = ADVANCE.

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02**: "Use 'high/medium/low' priority vocabulary."
> IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate commit on unparseable priority.**
>
> And IR-05: "Assign all signals to a single generic owner role."
> IR-05 Stakeholder Most Harmed: **Cross-functional team — gaps invisible when all ownership collapses.**

**Entry**: Phase 1 COMMITMENT BLOCK 1 Decision = ADVANCE confirmed. S-table present.

### NARRATIVE RATIONALE

Write ≥ 2 sentences explaining why this topic needs investigation and what decision
it informs. Required fill-in step.

> [Model fills here — minimum 2 sentences]

### FIELD SCHEMA

> Column order = row order. F-01 is the leftmost column. Fill left to right.

| ID   | Field               | Constraint                                                          | Decision-State Anchor                                                                                      | Immediate Failure                               | Downstream Effect                                              |
|------|---------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                 | essential=consumer cannot decide without this (decision blocked); recommended=consumer decides with increased exposure (quality risk accepted); optional=consumer decides unaffected (supplementary enrichment only) | Schema violation; strategy malformed | Strategy unusable as commit gate; Design Lead cannot gate |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic    | —                                                                                                          | Invalid namespace; routing fails                | Signal routed to wrong executor                                |
| F-03 | Skill               | Named skill under stated namespace                                  | —                                                                                                          | Non-existent skill reference                    | Signal uncollectable                                           |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template              | —                                                                                                          | Format fails; path unresolvable                 | Strategy unreachable                                           |
| F-05 | Producer → Consumer | `{role} → {decision-maker-role}`; Consumer verbatim in Phase 1 S-table | —                                                                                                     | Orphan consumer; traceability broken            | Ownership undefined; accountability gap                        |
| F-06 | Stakeholder Ref     | S-NN row from Phase 1                                               | —                                                                                                          | Orphan signal; no stakeholder basis             | Signal disconnected from risk motivation                       |

### COVERAGE SCHEMA

| ID     | Constraint                  | Minimum      | Immediate Failure                       | Downstream Effect                            |
|--------|-----------------------------|--------------|-----------------------------------------|----------------------------------------------|
| COV-01 | Signals marked essential    | ≥ 1          | No commit gate definable                | Feature ships ungated                        |
| COV-02 | Distinct namespaces         | ≥ 2          | Single-namespace plan; blind spot       | Gap analysis cannot detect holes             |
| COV-03 | Distinct Producer roles     | ≥ 2          | Single-owner collapse                   | Cross-functional gaps invisible              |
| COV-04 | Narrative rationale written | ≥ 2 sentences| Context absent                          | Signal relevance unverifiable                |

### SIGNAL TABLE

> Priority is the leftmost column. Fill left to right.

| Priority | Namespace | Skill | Item Name | Producer → Consumer | Stakeholder Ref |
|----------|-----------|-------|-----------|---------------------|-----------------|
|          |           |       |           |                     |                 |

```
╔═══════════════════════════════════════════════════════════════╗
║  COMMITMENT BLOCK 2 — Phase 2 Exit Gate                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Override: IR-02 ("Use 'high/medium/low' priority vocab...") ║
║             IR-05 ("Assign all signals to single role...")    ║
║                                                               ║
║  Vulnerable if not overridden:                                ║
║    IR-02: Design Lead — cannot gate commit on bad priority    ║
║    IR-05: Cross-functional team — gaps invisible              ║
║                                                               ║
║  F-01: Priority valid (essential/recommended/optional only):  ║
║    Status: [ PASS | FAIL ]                                    ║
║  F-02: Namespaces valid:      [ PASS | FAIL ]                 ║
║  F-03: Skills valid:          [ PASS | FAIL ]                 ║
║  F-04: Item names valid:      [ PASS | FAIL ]                 ║
║  F-05: Consumer verbatim in Phase 1 S-table: [ PASS | FAIL ] ║
║  F-06: Stakeholder Refs cite S-NN rows: [ PASS | FAIL ]      ║
║  COV-01: ≥ 1 essential signal: [ PASS | FAIL ]               ║
║  COV-02: ≥ 2 namespaces:      [ PASS | FAIL ]                ║
║  COV-03: ≥ 2 Producer roles:  [ PASS | FAIL ]                ║
║  COV-04: Rationale written:   [ PASS | FAIL ]                ║
║                                                               ║
║  IR-02 text verbatim: "Use 'high/medium/low' priority        ║
║  vocabulary from project-management context." Phase overrides.║
║                                                               ║
║  Phase 2 Decision: [ ADVANCE to Phase 3 | STOP and re-fill ] ║
╚═══════════════════════════════════════════════════════════════╝
```

Do not proceed to Phase 3 until COMMITMENT BLOCK 2 Decision = ADVANCE.

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03**: "Collapse commit gate into signal plan section with no structural isolation."
> IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**

**Entry**: Phase 2 COMMITMENT BLOCK 2 Decision = ADVANCE confirmed. Signal table present.

Fill in the commit gate block:

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when ALL of the following present in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name]

PERMITTED AFTER COMMIT (recommended/optional):
  - [items]

Enforcement: no design commit until REQUIRED items exist at declared paths.
```

```
╔═══════════════════════════════════════════════════════════════╗
║  COMMITMENT BLOCK 3 — Phase 3 Exit Gate                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Override: IR-03 ("Collapse commit gate into signal plan")   ║
║                                                               ║
║  Vulnerable if not overridden:                                ║
║    IR-03: Engineering Lead — no enforced readiness condition  ║
║                                                               ║
║  Condition A — Gate block written as standalone section:      ║
║    Status: [ PASS | FAIL ]                                    ║
║  Condition B — ≥ 1 essential signal in REQUIRED list:        ║
║    Status: [ PASS | FAIL ]                                    ║
║  Condition C — Gate is a condition, not a list of aspirations:║
║    Status: [ PASS | FAIL ]                                    ║
║                                                               ║
║  IR-03 text verbatim: "Collapse commit gate into signal plan  ║
║  section with no structural isolation." Phase overrides.      ║
║                                                               ║
║  Phase 3 Decision: [ ADVANCE to Phase 4 | STOP and re-write ]║
╚═══════════════════════════════════════════════════════════════╝
```

Do not proceed to Phase 4 until COMMITMENT BLOCK 3 Decision = ADVANCE.

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04**: "Omit artifact naming convention; use freeform item names."
> IR-04 Stakeholder Most Harmed: **All downstream consumers — strategy unreachable by path-based tools.**

**Entry**: Phase 3 COMMITMENT BLOCK 3 Decision = ADVANCE confirmed. Gate block present.

### Write 1: simulations/TOPICS.md

Append row:

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

```
╔═══════════════════════════════════════════════════════════════╗
║  COMMITMENT BLOCK 4 — Phase 4 Exit Gate                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Override: IR-04 ("Omit artifact naming convention...")      ║
║                                                               ║
║  Vulnerable if not overridden:                                ║
║    IR-04: All downstream consumers — strategy unreachable     ║
║                                                               ║
║  Condition A — simulations/TOPICS.md row present for {TOPIC}:║
║    Status: [ PASS | FAIL ]                                    ║
║  Condition B — simulations/{TOPIC}/strategy.md exists:       ║
║    Status: [ PASS | FAIL ]                                    ║
║  Condition C — All item names follow {topic}-{signal}-{date} ║
║    Status: [ PASS | FAIL ]                                    ║
║                                                               ║
║  IR-04 text verbatim: "Omit artifact naming convention; use   ║
║  freeform item names." This phase overrides that default.     ║
║                                                               ║
║  Phase 4 Decision: [ COMPLETE | STOP and re-write ]          ║
╚═══════════════════════════════════════════════════════════════╝
```
```

---

---

## V-05 — Failure Cascade Registry + Schema-as-Sole-Truth (Combined)

**Axis**: Failure cascade registry + Schema-as-sole-truth
**Hypothesis**: Maximum structural compression results from combining two pre-pipeline registries (INERTIA REGISTER + FAILURE CASCADE REGISTRY) with zero-prose phases (schema citations only). All constraint text lives in named registries and schema rows; all references are by stable ID; no inline prose can drift. This is the most machine-readable form of the prompt and tests whether maximum ID-citation density produces the most consistent structural compliance across diverse topic inputs.
**Key Structural Difference**: Both INERTIA REGISTER (IR-NN) and FAILURE CASCADE REGISTRY (FC-NN) precede the pipeline. STAKEHOLDER SCHEMA (SK-NN), FIELD SCHEMA (F-NN), and COVERAGE SCHEMA (COV-NN) are the complete sources of truth. Phase bodies reference only schema IDs. Exit gates reproduce both IR-NN and FC-NN text verbatim. No constraint prose exists outside registry and schema rows.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IDs. Team behavioral defaults this pipeline overrides.
> Read before FAILURE CASCADE REGISTRY and before pipeline overview.
> All phase override directives and exit gates cite these by ID.

| ID    | Default Behavior                                                              | Override Active In |
|-------|-------------------------------------------------------------------------------|--------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition               | Phase 1            |
| IR-02 | Use "high/medium/low" priority vocabulary                                     | Phase 2            |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation    | Phase 3            |
| IR-04 | Omit artifact naming convention; use freeform item names                      | Phase 4            |
| IR-05 | Assign all signals to a single generic owner role                             | Phase 2            |

---

## FAILURE CASCADE REGISTRY

> Pre-pipeline. Stable IDs. Model-execution failure modes — distinct from team
> inertia defaults. These are failures produced by the model at execution time.
> All phase consequence citations reference FC-NN rows. Exit gates reproduce FC-NN text.

| ID    | Failure Mode                                     | Phase Detectable     | Immediate Consequence                            | Downstream Effect                                    | Recovery Steps                                              |
|-------|--------------------------------------------------|----------------------|--------------------------------------------------|------------------------------------------------------|-------------------------------------------------------------|
| FC-01 | Priority vocabulary substitution (high/med/low)  | Phase 2 pre-write    | F-01 schema violation; row malformed             | Strategy unusable as commit gate                     | Re-fill signal table; re-run Phase 3                        |
| FC-02 | Orphaned Consumer in F-05 (not in S-table)       | Phase 2 exit         | Consumer traceability broken                     | Signal ownership undefined; accountability gap       | Re-run Phase 1; re-derive F-05; re-run Phase 2 exit         |
| FC-03 | Silent stakeholder table (rows present, cells empty) | Phase 1 exit     | SK-NN completeness check fails                   | Phase 2 role differentiation has no ground truth     | Re-fill Phase 1 table; re-run Phase 2 role columns          |
| FC-04 | Commit gate collapsed into signal plan section   | Phase 3 exit         | No structurally isolated gate exists             | Engineering has no enforceable readiness condition   | Re-run Phase 3 as dedicated phase; re-write strategy.md     |
| FC-05 | Freeform item names (F-04 violation)             | Phase 4 exit         | Path format check fails                          | Strategy unreachable by path-based tools             | Re-fill item name column; re-write strategy.md              |
| FC-06 | Single-role strategy (COV-03 violation)          | Phase 2 pre-write    | Cross-functional gap undetectable at review      | Strategy masks role coverage holes                   | Re-derive Producer roles from Phase 1; re-run COV-03 check  |

---

## STAKEHOLDER SCHEMA

> Phase 1 constraint registry. SK-NN row order = column order in Phase 1 table.
> No Phase 1 column constraints exist outside this schema.

| ID    | Column                  | Constraint                                                                | Immediate Failure (→ FC-NN)                         | Downstream Effect                                        |
|-------|-------------------------|---------------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|
| SK-01 | Row ID                  | S-NN format (S-01, S-02, ... S-NN)                                        | Row unaddressable by F-05/F-06                      | Consumer traceability fails at Phase 2 lookup → FC-02   |
| SK-02 | Decision-Maker Role     | Named accountable role; not "stakeholder" or "user"                       | Anonymous row; cannot populate F-05 Consumer        | Signal ownership undefined → FC-06 risk                  |
| SK-03 | Risk Exposure           | Specific harm to this role if topic is skipped                            | Empty risk; no signal motivation                    | Pruning ungrounded; gaps invisible                       |
| SK-04 | What Decision Informed  | Concrete decision this topic informs                                      | No decision anchor                                  | Signal relevance unverifiable                            |

---

## FIELD SCHEMA

> Phase 2 signal table constraint registry. F-NN row order = column order.
> F-01 is leftmost. No Phase 2 signal column constraints exist outside this schema.

| ID   | Field               | Constraint                                                          | Decision-State Anchor                                                                                      | Immediate Failure (→ FC-NN)                        | Downstream Effect                                           |
|------|---------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                 | essential=consumer cannot decide without this (decision blocked); recommended=consumer decides with increased exposure (quality risk accepted); optional=consumer decides unaffected (supplementary enrichment only) | Schema violation → FC-01              | Strategy unusable as commit gate                           |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic    | —                                                                                                          | Invalid namespace; routing fails                   | Signal routed to wrong executor                             |
| F-03 | Skill               | Named skill under stated namespace                                  | —                                                                                                          | Non-existent skill reference                       | Signal uncollectable                                        |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template              | —                                                                                                          | Format fails → FC-05                               | Strategy unreachable by path tools                          |
| F-05 | Producer → Consumer | `{role} → {decision-maker-role}`; Consumer verbatim in SK-02        | —                                                                                                          | Orphan consumer → FC-02                            | Accountability gap; ownership undefined                     |
| F-06 | Stakeholder Ref     | S-NN row from Phase 1                                               | —                                                                                                          | Orphan signal; no stakeholder basis                | Signal disconnected from risk motivation                    |

---

## COVERAGE SCHEMA

> Phase 2 coverage constraint registry. No coverage constraints exist outside this schema.

| ID     | Constraint                  | Minimum      | Immediate Failure (→ FC-NN)                    | Downstream Effect                           |
|--------|-----------------------------|--------------|-------------------------------------------------|---------------------------------------------|
| COV-01 | Signals marked essential    | ≥ 1          | No commit gate definable                        | Feature ships ungated → FC-04 risk          |
| COV-02 | Distinct namespaces         | ≥ 2          | Single-namespace plan; blind spot               | Gap analysis cannot detect coverage holes   |
| COV-03 | Distinct Producer roles     | ≥ 2          | Single-owner collapse → FC-06                   | Cross-functional gaps invisible             |
| COV-04 | Narrative rationale written | ≥ 2 sentences| Context absent                                  | Signal relevance unverifiable               |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose          | Handoff Artifact            | Exit Gate (cites schema IDs)                           | If I Skip This Phase, I Will…               | Team Default (→ IR-NN) | Recovery Cost (→ FC-NN)               |
|-------|------------------|-----------------------------|--------------------------------------------------------|---------------------------------------------|------------------------|----------------------------------------|
| 1     | Stakeholder Map  | S-table (≥3 rows)          | SK-01–SK-04: row count + col completeness, independently | author orphan signal rows (no role truth) | → IR-01, IR-05         | → FC-03; then FC-02 chain in Phase 2  |
| 2     | Signal Plan      | Signal table rows           | F-01–F-06 + COV-01–COV-04; F-05 Consumer → SK-02      | produce malformed strategy                  | → IR-02, IR-05         | → FC-01; → FC-02; → FC-06            |
| 3     | Commit Gate      | Gate definition block       | Phase 3 exit gate cleared; gate isolated; ≥1 essential  | ship without readiness gate                | → IR-03                | → FC-04                               |
| 4     | Artifact Write   | TOPICS.md row + strategy.md | Both files correct path; F-04 compliant item names     | topic unregistered; strategy unreachable    | → IR-04                | → FC-05                               |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01** (see INERTIA REGISTER row IR-01).
> **This phase overrides IR-05** (see INERTIA REGISTER row IR-05).
>
> All column constraints are in STAKEHOLDER SCHEMA rows SK-01–SK-04.
> No additional column instructions apply outside that schema.

**Entry gate**: INERTIA REGISTER (IR-01–IR-05) confirmed read. FAILURE CASCADE REGISTRY (FC-01–FC-06) confirmed read. STAKEHOLDER SCHEMA (SK-01–SK-04) confirmed read. [ ]

Fill in the following table. Each column constraint: see SK-NN row.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: What Decision Informed |
|---------------|---------------------------|----------------------|-------------------------------|
| S-01          |                           |                      |                               |
| S-02          |                           |                      |                               |
| S-03          |                           |                      |                               |
| S-NN          | (add rows)                |                      |                               |

**Exit gate** — cite schema IDs:

> Check SK-01–SK-04 conditions INDEPENDENTLY. Do not advance until both are
> checked separately. Sequential checking produces this specific failure:
> "3 rows present, cells empty" passes as compliant — this is wrong.

- [ ] SK-01 through SK-04: Row count ≥ 3 (see SK-01 constraint)
- [ ] SK-01 through SK-04: All four columns populated in every filled row (see SK-02–SK-04 constraints)

> Do not advance until both items are checked independently, not sequentially.

**IR-01 text reproduced verbatim**:
"Skip stakeholder mapping; author signals from feature intuition."
This phase overrides that default.

**FC-03 text reproduced verbatim** (execution-time failure risk at this gate):
Failure Mode: "Silent stakeholder table (rows present, cells empty)."
Immediate: "SK-NN completeness check fails."
Downstream: "Phase 2 role differentiation has no ground truth."

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02** (see INERTIA REGISTER row IR-02).
> **This phase overrides IR-05** (see INERTIA REGISTER row IR-05).
>
> All field constraints: FIELD SCHEMA rows F-01–F-06.
> All coverage constraints: COVERAGE SCHEMA rows COV-01–COV-04.
> No additional constraint instructions apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff present (≥3 rows, all SK-01–SK-04 columns filled). [ ]

**Narrative Rationale** (COV-04 — see COVERAGE SCHEMA row COV-04 for constraint):

> [Model fills here — constraint: COV-04]

**Pre-write gate** — cite schema IDs only:

- [ ] F-01 compliant (see FIELD SCHEMA F-01 for constraint text)
- [ ] F-02 compliant (see FIELD SCHEMA F-02)
- [ ] F-03 compliant (see FIELD SCHEMA F-03)
- [ ] F-04 compliant (see FIELD SCHEMA F-04)
- [ ] F-05 compliant: Consumer value appears verbatim in SK-02 (see F-05 + SK-02)
- [ ] F-06 compliant (see FIELD SCHEMA F-06)
- [ ] COV-01 compliant (see COVERAGE SCHEMA COV-01)
- [ ] COV-02 compliant (see COVERAGE SCHEMA COV-02)
- [ ] COV-03 compliant (see COVERAGE SCHEMA COV-03)
- [ ] COV-04 compliant (see COVERAGE SCHEMA COV-04)

**Signal table** — column order = FIELD SCHEMA row order (F-01 leftmost):

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|
|                 |                  |              |                  |                           |                        |

**Exit gate**: All pre-write items cleared (F-01–F-06, COV-01–COV-04). Signal table ≥ 1 row. F-05 Consumer verified against SK-02.

**IR-02 text reproduced verbatim**:
"Use 'high/medium/low' priority vocabulary from project-management context."
This phase overrides that default. Every Priority cell: see F-01 constraint.

**FC-01 text reproduced verbatim** (execution-time failure risk at this gate):
Failure Mode: "Priority vocabulary substitution (high/med/low)."
Immediate: "F-01 schema violation; row malformed."
Downstream: "Strategy unusable as commit gate."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03** (see INERTIA REGISTER row IR-03).
>
> No additional constraint instructions apply beyond IR-03 override and gate conditions below.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff present. [ ]

Fill in the commit gate block:

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when ALL of the following present in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name from essential row]

PERMITTED AFTER COMMIT (recommended/optional):
  - [items]

Enforcement: no design commit until REQUIRED items exist at declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named explicitly.
Gate expressed as a condition, not as a list of aspirations.

**IR-03 text reproduced verbatim**:
"Collapse commit gate into signal plan section with no structural isolation."
This phase overrides that default.

**FC-04 text reproduced verbatim** (execution-time failure risk at this gate):
Failure Mode: "Commit gate collapsed into signal plan section."
Immediate: "No structurally isolated gate exists."
Downstream: "Engineering has no enforceable readiness condition."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04** (see INERTIA REGISTER row IR-04).
>
> Item name constraint: see FIELD SCHEMA F-04.
> No additional constraint instructions apply outside F-04 and IR-04 override.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff present. [ ]

### Write 1: simulations/TOPICS.md

```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |
```

### Write 2: simulations/{TOPIC}/strategy.md

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste COV-04 narrative from Phase 2]

## Stakeholder Map
[paste Phase 1 table — SK-01–SK-04 columns]

## Inertia Register (Active Overrides)
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see pre-pipeline INERTIA REGISTER)

## Signal Plan
[paste signal table — F-01–F-06 columns, Priority leftmost]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files at correct paths. All item names satisfy F-04 (see FIELD SCHEMA F-04).

**IR-04 text reproduced verbatim**:
"Omit artifact naming convention; use freeform item names."
This phase overrides that default.

**FC-05 text reproduced verbatim** (execution-time failure risk at this gate):
Failure Mode: "Freeform item names (F-04 violation)."
Immediate: "Path format check fails."
Downstream: "Strategy unreachable by path-based tools."
```

---

## Round 15 Excellence Signals (Candidate Criteria for v14)

From the five variations above, three structural patterns appear as candidates
for elevation to rubric criteria in v14:

**ES-1 (from V-01)**: Phase content is exclusively schema citations — no inline
prose constraints exist outside schema rows; every phase references F-NN, COV-NN,
or SK-NN by ID for its constraints. This closes the **instruction-drift vector**:
prose constraints in phases can diverge from schema rows on revision; schema-only
phases are impossible to drift because the constraint source is the schema.

**ES-2 (from V-02 and V-04)**: INERTIA REGISTER carries a "Stakeholder Most Harmed"
column naming the role category that suffers when each default is not overridden;
per-phase override directives and exit gate verbatim reproductions include that role
name. This closes the **abstract-default vector**: a model can rationalize past an
abstract behavioral default ("skip stakeholder mapping") more easily than a named-role
consequence ("Product Manager loses commit scope ground truth").

**ES-3 (from V-03 and V-05)**: A pre-pipeline FAILURE CASCADE REGISTRY with stable
FC-NN IDs collects execution-time model-failure modes (distinct from team inertia
defaults in INERTIA REGISTER); pipeline consequence columns and phase exit gates cite
and reproduce FC-NN text. This closes the **failure-mode consultability gap**: inline
pipeline consequence columns are visible at pipeline-read time but may not be salient
at execution time; a named registry with FC-NN IDs makes every failure mode consultable
by ID during phase execution, analogous to how INERTIA REGISTER made IR-NN inertia
defaults consultable throughout.
