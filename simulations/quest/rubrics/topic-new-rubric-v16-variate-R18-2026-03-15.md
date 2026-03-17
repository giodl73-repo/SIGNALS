# topic-new — Round 18 Variations (V-01 through V-05)
# Rubric target: v16 (47 aspirational criteria, denominator 47)
# Date: 2026-03-15

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Phrasing register — command throughout (C-50, C-51, C-52, C-53) | Applying command register at every directive point simultaneously — prohibition at pipeline read (C-50), "Stop." + "Record both results." at independence gate (C-51), second-person failure example (C-52), "Stop. You are overriding IR-NN:" at phase headers (C-53) — converts all ambient directives to mandatory decision points in a single sweep; tests whether phrasing register alone, without structural changes, closes the decisional-vs-informational gap across all four directive sites |
| V-02 | Override mission opener (C-49 only) | Adding a dedicated OVERRIDE MISSION block before any schema content — "These are the defaults this skill overrides. Every block that follows exists to prevent these defaults from applying." — gives the model a document-purpose frame before it reads any constraint; C-15 stakeholder enumeration names who is at risk; C-49 names why the document exists; tests whether the override-mission declaration alone changes how the model reads subsequent schema blocks |
| V-03 | BEFORE/AFTER failure table (C-54 only) | Replacing the FER-01 prose description with a labeled BEFORE/AFTER comparison block — one column shows the exact output sequential checking accepts; the other shows the condition independent checking would have caught — makes the failure-to-correct trajectory visible by column inspection without requiring the model to hold both states in narrative context; tests whether structural contrast format improves gate-compliance independently of phrasing register |
| V-04 | Combined: command register (V-01) + BEFORE/AFTER table (V-03) | Command register addresses the phrasing channel (ambient directives processed as advisory); BEFORE/AFTER table addresses the visualization channel (failure recognizable by inspection vs narrative); both channels are independent and may compound; V-04 tests whether combining C-51/C-52/C-53 phrasing with C-54 structural contrast produces a gate compliance rate above either single-axis variation |
| V-05 | Full integration: V-01 + V-02 + V-03 + C-55 PCR cross-cites FER-NN | All seven new v16 criteria activated simultaneously: C-49 override-mission opener + C-50 prohibition clause + C-51 Stop.+record + C-52 second-person failure example + C-53 Stop.You are overriding + C-54 BEFORE/AFTER table + C-55 PCR-to-FER cross-citation; PCR consequence entries end with "skip failure recognizable by FER-01 output inspection" closing the consequence-without-detection gap above C-48; tests whether full v16 activation produces a coherent prompt that scores near-perfect against the 47-criterion denominator |

---

---

## V-01 — Command Register Throughout

**Axis**: Phrasing register — apply command form at all four directive sites: pipeline prohibition (C-50), independence gate with "Stop." + "Record both results." (C-51), second-person failure example (C-52), phase headers with "Stop. You are overriding IR-NN:" (C-53).
**Hypothesis**: R17 V-01 had FER-NN + PCR-NN with declarative directives ("This phase overrides IR-NN", "Check these two conditions INDEPENDENTLY"). Declarative directives operate in informational register — the model may process them as ambient context. Command register forces a halt at every structural decision point: phase entry, gate execution, and failure recognition. Second-person framing at FER-01 addresses the model as the agent that produced the malformed output, enabling self-recognition rather than pattern abstraction.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read this register before reading the pipeline overview.
> All phase directives and exit gates cite rows by IR-NN ID.
> "Stakeholder Most Harmed" names who suffers most when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## FAILURE EXAMPLE REGISTRY

> Pre-pipeline. Stable FER-NN IDs.
> Each row shows a concrete output state that sequential checking would accept
> but independent checking would reject. Gate instructions cite FER-NN IDs.
> Do not restate example text inline at gates; cite FER-NN ID only.

| ID     | Phase | Output You Accepted (sequential — THIS IS WRONG)                                                   | What Independent Checking Catches                                                                                                   |
|--------|-------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| FER-01 | 1     | "Output you accepted: 'S-01 \| Product Manager \| \| ' — SK-03 and SK-04 empty on all rows. This output is malformed." | Row-count check (≥ 3) passes; column-completeness check then reveals SK-03 and SK-04 empty on every row — sequential checking called this compliant |
| FER-02 | 2     | "Output you accepted: signal table with 4 rows; Priority column reads 'high / medium / low'. This output is malformed." | Row-count check passes; priority-vocabulary check reveals F-01 violation — "high" is not in {essential/recommended/optional}        |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs. Defines the consequence of bypassing each pipeline phase.
> Pipeline overview consequence column cites PCR-NN IDs only.
> Do not embed consequence prose in the overview table.

| ID     | Phase Skipped | Consequence                                                                                         |
|--------|--------------|-----------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1      | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails  |
| PCR-02 | Phase 2      | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness   |
| PCR-03 | Phase 3      | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated    |
| PCR-04 | Phase 4      | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools            |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                               | Decision-State Anchor                                                                                                             | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                      | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected      | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                         | —                                                                                                                                 | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                              | —                                                                                                                                 | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                     | —                                                                                                                                 | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1  | —                                                                                                                                 | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                   | —                                                                                                                                 | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                          | —                                                                                                                                 | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> These rows are the SOLE source of Phase 2 coverage constraints.
> Phase 2 body contains no inline prose coverage constraint restatements; cite COV-NN only.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip consequences are declared here.
> Consequence column cites PCR-NN IDs from PHASE CONSEQUENCE REGISTRY.
> **Do not begin Phase 1 until you have read every row.**

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                                               | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|-----------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently (see FER-01)         | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table                               | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2                     | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04                              | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **Stop. You are overriding IR-01:** "Skip stakeholder mapping; author signals from feature intuition." Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **Stop. You are overriding IR-05:** "Assign all signals to a single generic owner role." Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. FAILURE EXAMPLE REGISTRY FER-01 confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate:**

> **Stop. Do not advance until you have run BOTH of the following checks as separate acts. Record both results.**
> Failure mode: see **FER-01** — a table with ≥ 3 rows and empty SK-03/SK-04 cells is accepted
> by sequential checking and rejected by independent checking. FER-01 shows the exact output state
> in second-person form: "Output you accepted: 'S-01 | Product Manager | | '."

- [ ] Row count ≥ 3 (checked independently of column completeness — record result before next check)
- [ ] All four columns populated in every filled row (checked independently of row count — record result)

> Do not advance to Phase 2 until both results are recorded as separate acts.

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 2 — SIGNAL PLAN

> **Stop. You are overriding IR-02:** "Use 'high/medium/low' priority vocabulary from project-management context." Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **Stop. You are overriding IR-05:** "Assign all signals to a single generic owner role." Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

> Cite schema rows by ID. Do not restate constraint text inline.

- [ ] F-01: Priority vocabulary (see F-01)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN rows from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: ≥ 1 essential signal (see COV-01)
- [ ] COV-02: ≥ 2 distinct namespaces (see COV-02)
- [ ] COV-03: ≥ 2 distinct Producer roles (see COV-03)
- [ ] COV-04: Narrative rationale present above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row in signal table. F-05 Consumer values verified against Phase 1 SK-02. F-07 values cite IR-NN entries.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **Stop. You are overriding IR-03:** "Collapse commit gate into signal plan section with no structural isolation." Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA. No additional constraint statements apply outside schemas.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (essential — see COV-01):
  1. [item name from essential row]
  2. [additional essential rows if any]

PERMITTED AFTER COMMIT (recommended / optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate expressed as a condition, not a list of aspirations.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **Stop. You are overriding IR-04:** "Omit artifact naming convention; use freeform item names." Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md entry), C-02 (strategy.md at correct path). Item name constraint: see F-04 in FIELD SCHEMA.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff artifact present. [ ]

### Write 1: simulations/TOPICS.md

> Constraint: C-01. Append a row.

| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |

### Write 2: simulations/{TOPIC}/strategy.md

> Path constraint: C-02. Item name constraint: see F-04.

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste COV-04 narrative from Phase 2]

## Stakeholder Map
[paste Phase 1 fill-in table]

## Active Inertia Overrides
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-02 — Override Mission Opener

**Axis**: Add a dedicated OVERRIDE MISSION block before any schema or phase content (C-49 only). All other structure identical to R17 V-01.
**Hypothesis**: R17 V-03 placed "Read this register first. These are the defaults this skill overrides. Every block that follows exists to prevent these defaults from applying." as an INERTIA REGISTER sub-header — one line inside a schema block. C-49 requires the override-mission declaration as an opener that precedes all schema content, framing the entire document as an anti-default construct. A dedicated OVERRIDE MISSION section before INERTIA REGISTER gives the model its document-purpose frame at first-read, before any constraint schema is encountered. Tests whether the override-mission declaration changes the reading register for all subsequent blocks, vs. V-01 where the same information is implicit in the schema structure.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## OVERRIDE MISSION

> **Read this block before reading any schema, phase, or gate.**

These are the defaults this skill overrides. Every block that follows exists to prevent
these defaults from applying.

| Default (IR-NN) | What This Skill Overrides It With |
|-----------------|-----------------------------------|
| IR-01: Skip stakeholder mapping | Phase 1 — mandatory stakeholder fill-in table with exit gate |
| IR-02: Use high/medium/low priority | Phase 2 — FIELD SCHEMA F-01 enforces {essential/recommended/optional} only |
| IR-03: Collapse commit gate into signal plan | Phase 3 — commit gate is its own structurally isolated phase |
| IR-04: Use freeform item names | Phase 4 — item names must follow `{topic}-{signal}-{date}.md` |
| IR-05: Single generic owner role | Phase 2 — COV-03 requires ≥ 2 distinct Producer roles |

A model that reads this document and applies its defaults is the failure mode this skill exists to prevent.
Every schema, every gate, and every exit condition in this document is an override instrument.

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read this register before reading the pipeline overview.
> All phase directives and exit gates cite rows by IR-NN ID.
> "Stakeholder Most Harmed" names who suffers most when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## FAILURE EXAMPLE REGISTRY

> Pre-pipeline. Stable FER-NN IDs.
> Each row shows a concrete output state that sequential checking would accept
> but independent checking would reject. Gate instructions cite FER-NN IDs.
> Do not restate example text inline at gates; cite FER-NN ID only.

| ID     | Phase | Sequential Output State (would be ACCEPTED — this is wrong)                                        | Independent Rejection (what the independent check catches)                                                          |
|--------|-------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| FER-01 | 1     | Table has 3 rows; SK-01 column is populated; SK-03 and SK-04 cells are empty on all rows            | Row-count check (≥ 3) passes; column-completeness check then reveals SK-03 and SK-04 empty on every row — a table that sequential checking calls compliant is not |
| FER-02 | 2     | Signal table has 4 rows; Priority column contains "high / medium / low"                             | Row-count check passes; priority-vocabulary check reveals F-01 violation — "high" is not in {essential/recommended/optional} |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs. Defines the consequence of bypassing each pipeline phase.
> Pipeline overview consequence column cites PCR-NN IDs only.
> Do not embed consequence prose in the overview table.

| ID     | Phase Skipped | Consequence                                                                                         |
|--------|--------------|-----------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1      | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails  |
| PCR-02 | Phase 2      | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness   |
| PCR-03 | Phase 3      | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated    |
| PCR-04 | Phase 4      | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools            |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                               | Decision-State Anchor                                                                                                             | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                      | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected      | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                         | —                                                                                                                                 | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                              | —                                                                                                                                 | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                     | —                                                                                                                                 | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1  | —                                                                                                                                 | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                   | —                                                                                                                                 | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                          | —                                                                                                                                 | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> These rows are the SOLE source of Phase 2 coverage constraints.
> Phase 2 body contains no inline prose coverage constraint restatements; cite COV-NN only.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip consequences are declared here.
> Consequence column cites PCR-NN IDs from PHASE CONSEQUENCE REGISTRY.
> **Do not begin Phase 1 until you have read every row.**

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                                               | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|-----------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently (gate cites FER-01)  | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table                               | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2                     | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04                              | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. FAILURE EXAMPLE REGISTRY FER-01 confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate — check these two conditions INDEPENDENTLY:**

> **Independence instruction**: Check row count and column completeness as two separate acts.
> Do not chain these checks. Complete and record the row-count check before beginning the
> column-completeness check.
> Failure mode: see **FER-01** — a table with ≥ 3 rows and empty SK-03/SK-04 cells is accepted
> by sequential checking and rejected by independent checking. FER-01 names the exact output state.

- [ ] Row count ≥ 3 (see SK-01 through SK-04 in STAKEHOLDER SCHEMA)
- [ ] All four columns populated in every filled row (see SK-01 through SK-04 in STAKEHOLDER SCHEMA)

> Do not advance to Phase 2 until both items are checked as separate acts.

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02.** IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

> Cite schema rows by ID. Do not restate constraint text inline.

- [ ] F-01: Priority vocabulary (see F-01)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN rows from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: ≥ 1 essential signal (see COV-01)
- [ ] COV-02: ≥ 2 distinct namespaces (see COV-02)
- [ ] COV-03: ≥ 2 distinct Producer roles (see COV-03)
- [ ] COV-04: Narrative rationale present above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row in signal table. F-05 Consumer values verified against Phase 1 SK-02. F-07 values cite IR-NN entries.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA. No additional constraint statements apply outside schemas.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (essential — see COV-01):
  1. [item name from essential row]
  2. [additional essential rows if any]

PERMITTED AFTER COMMIT (recommended / optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate expressed as a condition, not a list of aspirations.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md entry), C-02 (strategy.md at correct path). Item name constraint: see F-04 in FIELD SCHEMA.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff artifact present. [ ]

### Write 1: simulations/TOPICS.md

> Constraint: C-01. Append a row.

| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |

### Write 2: simulations/{TOPIC}/strategy.md

> Path constraint: C-02. Item name constraint: see F-04.

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste COV-04 narrative from Phase 2]

## Stakeholder Map
[paste Phase 1 fill-in table]

## Active Inertia Overrides
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-03 — BEFORE/AFTER Failure Table

**Axis**: Replace FER-01 sequential-rejection row with a labeled BEFORE/AFTER comparison block (C-54 only). All other structure identical to R17 V-01.
**Hypothesis**: R17 V-03 expanded the C-47 example into a "structured BEFORE/AFTER comparison table" but embedded it as an INERTIA REGISTER design choice. This variation isolates C-54 as the sole axis: FER-01 in the FAILURE EXAMPLE REGISTRY is replaced with a labeled two-column contrast block showing the sequential path (wrong) on the left and the independent path (correct) on the right. The structural contrast makes the failure-to-correct trajectory visible by column inspection — the model sees both the wrong accepted output and the correct detection condition side by side, without needing to hold both in narrative context. Tests whether C-54 structural contrast alone, without command-register phrasing, improves gate compliance.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read this register before reading the pipeline overview.
> All phase directives and exit gates cite rows by IR-NN ID.
> "Stakeholder Most Harmed" names who suffers most when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## FAILURE EXAMPLE REGISTRY

> Pre-pipeline. Stable FER-NN IDs.
> Each entry shows the SEQUENTIAL PATH (wrong — what sequential checking accepts) and the
> INDEPENDENT PATH (correct — what independent checking catches) side by side.
> Gate instructions cite FER-NN IDs. Do not restate example text inline at gates.

### FER-01 — Phase 1 Stakeholder Table Exit Gate

| | SEQUENTIAL PATH (wrong — accepted by sequential checking) | INDEPENDENT PATH (correct — caught by independent checking) |
|--|-----------------------------------------------------------|-------------------------------------------------------------|
| What the output looks like | S-01 \| Product Manager \| \| (SK-03 empty, SK-04 empty) | S-01 \| Product Manager \| [risk text] \| [decision text] |
| Row count check | PASSES: 3 rows present — sequential check advances | PASSES: 3 rows present |
| Column completeness check | SKIPPED: row count passed, advance proceeds — SK-03/SK-04 emptiness undetected | INDEPENDENT CHECK: SK-03 and SK-04 empty on all rows — gate fails |
| Gate result | MALFORMED TABLE ACCEPTED — this is wrong | Malformed table caught and blocked |

### FER-02 — Phase 2 Signal Table Exit Gate

| | SEQUENTIAL PATH (wrong — accepted by sequential checking) | INDEPENDENT PATH (correct — caught by independent checking) |
|--|-----------------------------------------------------------|-------------------------------------------------------------|
| What the output looks like | Priority column contains "high / medium / low" | Priority column contains "high / medium / low" |
| Row count check | PASSES: 4 rows present — sequential check advances | PASSES: 4 rows present |
| Vocabulary check | SKIPPED: row count passed — "high/medium/low" vocabulary undetected | INDEPENDENT CHECK: F-01 violation — "high" not in {essential/recommended/optional} |
| Gate result | MALFORMED TABLE ACCEPTED — this is wrong | Malformed table caught and blocked |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs. Defines the consequence of bypassing each pipeline phase.
> Pipeline overview consequence column cites PCR-NN IDs only.
> Do not embed consequence prose in the overview table.

| ID     | Phase Skipped | Consequence                                                                                         |
|--------|--------------|-----------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1      | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails  |
| PCR-02 | Phase 2      | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness   |
| PCR-03 | Phase 3      | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated    |
| PCR-04 | Phase 4      | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools            |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                               | Decision-State Anchor                                                                                                             | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                      | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected      | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                         | —                                                                                                                                 | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                              | —                                                                                                                                 | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                     | —                                                                                                                                 | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1  | —                                                                                                                                 | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                   | —                                                                                                                                 | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                          | —                                                                                                                                 | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> These rows are the SOLE source of Phase 2 coverage constraints.
> Phase 2 body contains no inline prose coverage constraint restatements; cite COV-NN only.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip consequences are declared here.
> Consequence column cites PCR-NN IDs from PHASE CONSEQUENCE REGISTRY.
> **Do not begin Phase 1 until you have read every row.**

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                                               | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|-----------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently (see FER-01)         | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table                               | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2                     | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04                              | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. FAILURE EXAMPLE REGISTRY FER-01 confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate — check these two conditions INDEPENDENTLY:**

> **Independence instruction**: Check row count and column completeness as two separate acts.
> Do not chain these checks. Complete and record the row-count check before beginning the
> column-completeness check.
> Failure mode: see **FER-01** — the SEQUENTIAL PATH column shows the exact output sequential
> checking accepts (SK-03/SK-04 empty, gate passes). The INDEPENDENT PATH column shows what
> independent checking catches. Match your table against FER-01 SEQUENTIAL PATH before advancing.

- [ ] Row count ≥ 3 (see SK-01 through SK-04 in STAKEHOLDER SCHEMA)
- [ ] All four columns populated in every filled row (see SK-01 through SK-04 in STAKEHOLDER SCHEMA)

> Do not advance to Phase 2 until both items are checked as separate acts.

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02.** IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

> Cite schema rows by ID. Do not restate constraint text inline.

- [ ] F-01: Priority vocabulary (see F-01)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN rows from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: ≥ 1 essential signal (see COV-01)
- [ ] COV-02: ≥ 2 distinct namespaces (see COV-02)
- [ ] COV-03: ≥ 2 distinct Producer roles (see COV-03)
- [ ] COV-04: Narrative rationale present above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row in signal table. F-05 Consumer values verified against Phase 1 SK-02. F-07 values cite IR-NN entries.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA. No additional constraint statements apply outside schemas.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (essential — see COV-01):
  1. [item name from essential row]
  2. [additional essential rows if any]

PERMITTED AFTER COMMIT (recommended / optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate expressed as a condition, not a list of aspirations.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md entry), C-02 (strategy.md at correct path). Item name constraint: see F-04 in FIELD SCHEMA.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff artifact present. [ ]

### Write 1: simulations/TOPICS.md

> Constraint: C-01. Append a row.

| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |

### Write 2: simulations/{TOPIC}/strategy.md

> Path constraint: C-02. Item name constraint: see F-04.

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste COV-04 narrative from Phase 2]

## Stakeholder Map
[paste Phase 1 fill-in table]

## Active Inertia Overrides
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-04 — Combined: Command Register + BEFORE/AFTER Failure Table

**Axis**: V-01 (command register: C-51 Stop.+record, C-52 second-person, C-53 Stop.You are overriding) combined with V-03 (C-54 BEFORE/AFTER table). Both axes are applied to FER-01: second-person framing ("Output you accepted") in the SEQUENTIAL PATH column, and BEFORE/AFTER structural contrast layout.
**Hypothesis**: Command register and structural contrast address independent failure channels. Command register closes the ambient-vs-decisional gap: "Stop." forces a halt before reading the directive; "Record both results." makes compliance auditable. BEFORE/AFTER closes the narrative-vs-inspection gap: the model can verify its output by column-matching rather than by abstract reasoning. V-04 tests whether the two channels compound — whether a prompt that halts the model at the gate AND gives it a visual inspection target produces gate compliance above either single-axis variation.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read this register before reading the pipeline overview.
> All phase directives and exit gates cite rows by IR-NN ID.
> "Stakeholder Most Harmed" names who suffers most when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## FAILURE EXAMPLE REGISTRY

> Pre-pipeline. Stable FER-NN IDs.
> Each entry presents a BEFORE/AFTER comparison: SEQUENTIAL PATH (wrong — what you accepted)
> vs INDEPENDENT PATH (correct — what independent checking catches).
> Second-person framing: "Output you accepted:" addresses the output as yours to self-recognize.
> Gate instructions cite FER-NN IDs. Do not restate example text inline at gates.

### FER-01 — Phase 1 Stakeholder Table Exit Gate

| | SEQUENTIAL PATH — Output you accepted (WRONG) | INDEPENDENT PATH — What independent checking catches (CORRECT) |
|--|-----------------------------------------------|----------------------------------------------------------------|
| Output state | "Output you accepted: 'S-01 \| Product Manager \| \| ' — SK-03 and SK-04 empty on all rows. This output is malformed." | S-01 \| Product Manager \| [risk populated] \| [decision populated] — all four columns filled |
| Row count check | PASSES: ≥ 3 rows — sequential execution advances | PASSES: ≥ 3 rows |
| Column completeness | SKIPPED: row count passed; SK-03/SK-04 emptiness not checked | INDEPENDENT: SK-03 and SK-04 empty on every row — gate FAILS |
| Result | Malformed table accepted — you advanced on wrong output | Malformed table blocked — correct result |

### FER-02 — Phase 2 Signal Table Exit Gate

| | SEQUENTIAL PATH — Output you accepted (WRONG) | INDEPENDENT PATH — What independent checking catches (CORRECT) |
|--|-----------------------------------------------|----------------------------------------------------------------|
| Output state | "Output you accepted: Priority column reads 'high / medium / low'. This output is malformed." | Priority column reads "essential / recommended / optional" throughout |
| Row count check | PASSES: ≥ 4 rows — sequential execution advances | PASSES: ≥ 4 rows |
| Vocabulary check | SKIPPED: row count passed; F-01 violation not checked | INDEPENDENT: "high" not in {essential/recommended/optional} — gate FAILS |
| Result | Malformed table accepted — you advanced on wrong output | Malformed table blocked — correct result |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs. Defines the consequence of bypassing each pipeline phase.
> Pipeline overview consequence column cites PCR-NN IDs only.
> Do not embed consequence prose in the overview table.

| ID     | Phase Skipped | Consequence                                                                                         |
|--------|--------------|-----------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1      | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails  |
| PCR-02 | Phase 2      | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness   |
| PCR-03 | Phase 3      | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated    |
| PCR-04 | Phase 4      | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools            |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                               | Decision-State Anchor                                                                                                             | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                      | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected      | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                         | —                                                                                                                                 | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                              | —                                                                                                                                 | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                     | —                                                                                                                                 | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1  | —                                                                                                                                 | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                   | —                                                                                                                                 | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                          | —                                                                                                                                 | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> These rows are the SOLE source of Phase 2 coverage constraints.
> Phase 2 body contains no inline prose coverage constraint restatements; cite COV-NN only.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip consequences are declared here.
> Consequence column cites PCR-NN IDs from PHASE CONSEQUENCE REGISTRY.
> **Do not begin Phase 1 until you have read every row.**

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                                               | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|-----------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently (see FER-01)         | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table                               | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2                     | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04                              | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **Stop. You are overriding IR-01:** "Skip stakeholder mapping; author signals from feature intuition." Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **Stop. You are overriding IR-05:** "Assign all signals to a single generic owner role." Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. FAILURE EXAMPLE REGISTRY FER-01 confirmed read (BEFORE/AFTER columns reviewed). [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate:**

> **Stop. Do not advance until you have run BOTH of the following checks as separate acts. Record both results.**
> Match your output against FER-01 SEQUENTIAL PATH (wrong column): if your table looks like
> "Output you accepted: 'S-01 | Product Manager | | '" — SK-03/SK-04 empty — you must stop
> and populate those columns before advancing. The INDEPENDENT PATH (correct column) shows what
> the valid output looks like.

- [ ] Row count ≥ 3 (checked independently — record: "row count = N, condition met/not met")
- [ ] All four columns populated in every filled row (checked independently — record: "column completeness met/not met")

> Do not advance to Phase 2 until both results are recorded as separate acts.

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 2 — SIGNAL PLAN

> **Stop. You are overriding IR-02:** "Use 'high/medium/low' priority vocabulary from project-management context." Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **Stop. You are overriding IR-05:** "Assign all signals to a single generic owner role." Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

> Cite schema rows by ID. Do not restate constraint text inline.

- [ ] F-01: Priority vocabulary (see F-01)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN rows from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: ≥ 1 essential signal (see COV-01)
- [ ] COV-02: ≥ 2 distinct namespaces (see COV-02)
- [ ] COV-03: ≥ 2 distinct Producer roles (see COV-03)
- [ ] COV-04: Narrative rationale present above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row in signal table. F-05 Consumer values verified against Phase 1 SK-02. F-07 values cite IR-NN entries.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **Stop. You are overriding IR-03:** "Collapse commit gate into signal plan section with no structural isolation." Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA. No additional constraint statements apply outside schemas.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (essential — see COV-01):
  1. [item name from essential row]
  2. [additional essential rows if any]

PERMITTED AFTER COMMIT (recommended / optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate expressed as a condition, not a list of aspirations.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **Stop. You are overriding IR-04:** "Omit artifact naming convention; use freeform item names." Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md entry), C-02 (strategy.md at correct path). Item name constraint: see F-04 in FIELD SCHEMA.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff artifact present. [ ]

### Write 1: simulations/TOPICS.md

> Constraint: C-01. Append a row.

| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |

### Write 2: simulations/{TOPIC}/strategy.md

> Path constraint: C-02. Item name constraint: see F-04.

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste COV-04 narrative from Phase 2]

## Stakeholder Map
[paste Phase 1 fill-in table]

## Active Inertia Overrides
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-05 — Full Integration (C-49 through C-55)

**Axis**: All seven v16 criteria activated simultaneously: override-mission opener (C-49) + prohibition clause already present (C-50) + Stop.+record at independence gate (C-51) + second-person BEFORE/AFTER failure table (C-52 + C-54) + Stop.You are overriding at phase headers (C-53) + PCR entries cross-cite FER-NN (C-55).
**Hypothesis**: Each of C-49 through C-55 closes a distinct gap above a prior criterion. C-49 closes the document-purpose gap above C-15. C-50 closes the advisory-vs-gate gap above C-26. C-51 closes the instructive-vs-command gap above C-30. C-52 closes the abstraction gap above C-47. C-53 closes the informational-vs-decisional gap above C-43. C-54 closes the narrative-vs-inspection gap above C-47. C-55 closes the consequence-without-detection gap above C-48. These gaps are structurally independent — no single-axis fix addresses all seven simultaneously. V-05 tests whether activating all seven produces a coherent, non-redundant prompt that scores near-perfect against the v16 denominator, or whether full integration introduces phrasing collision or structural overload.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## OVERRIDE MISSION

> **Read this block before reading any schema, phase, or gate.**

These are the defaults this skill overrides. Every block that follows exists to prevent
these defaults from applying.

| Default (IR-NN) | What This Skill Overrides It With |
|-----------------|-----------------------------------|
| IR-01: Skip stakeholder mapping | Phase 1 — mandatory stakeholder fill-in table with exit gate |
| IR-02: Use high/medium/low priority | Phase 2 — FIELD SCHEMA F-01 enforces {essential/recommended/optional} only |
| IR-03: Collapse commit gate into signal plan | Phase 3 — commit gate is its own structurally isolated phase |
| IR-04: Use freeform item names | Phase 4 — item names must follow `{topic}-{signal}-{date}.md` |
| IR-05: Single generic owner role | Phase 2 — COV-03 requires ≥ 2 distinct Producer roles |

A model that reads this document and applies its defaults is the failure mode this skill exists to prevent.
Every schema, every gate, and every exit condition in this document is an override instrument.

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read this register before reading the pipeline overview.
> All phase directives and exit gates cite rows by IR-NN ID.
> "Stakeholder Most Harmed" names who suffers most when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## FAILURE EXAMPLE REGISTRY

> Pre-pipeline. Stable FER-NN IDs.
> Each entry presents a labeled BEFORE/AFTER comparison: SEQUENTIAL PATH (what you accepted —
> wrong) vs INDEPENDENT PATH (what independent checking catches — correct).
> "Output you accepted:" addresses the malformed output as yours to enable self-recognition.
> Gate instructions cite FER-NN IDs. Do not restate example text inline at gates.

### FER-01 — Phase 1 Stakeholder Table Exit Gate

| | SEQUENTIAL PATH — Output you accepted (WRONG) | INDEPENDENT PATH — What independent checking catches (CORRECT) |
|--|-----------------------------------------------|----------------------------------------------------------------|
| Output state | "Output you accepted: 'S-01 \| Product Manager \| \| ' — SK-03 and SK-04 empty on all rows. This output is malformed." | S-01 \| Product Manager \| [specific harm text] \| [specific decision text] — all four columns filled |
| Row count check | PASSES: ≥ 3 rows present — sequential execution advances | PASSES: ≥ 3 rows present |
| Column completeness | SKIPPED: row count passed; SK-03/SK-04 emptiness never checked | INDEPENDENT: SK-03 and SK-04 empty on every row — gate FAILS |
| Result | Malformed table accepted — you advanced on wrong output | Malformed table blocked — advance requires correction |

### FER-02 — Phase 2 Signal Table Exit Gate

| | SEQUENTIAL PATH — Output you accepted (WRONG) | INDEPENDENT PATH — What independent checking catches (CORRECT) |
|--|-----------------------------------------------|----------------------------------------------------------------|
| Output state | "Output you accepted: Priority column reads 'high / medium / low'. This output is malformed." | Priority column reads "essential" or "recommended" or "optional" throughout |
| Row count check | PASSES: ≥ 4 rows present — sequential execution advances | PASSES: ≥ 4 rows present |
| Vocabulary check | SKIPPED: row count passed; F-01 violation never checked | INDEPENDENT: "high" not in {essential/recommended/optional} — gate FAILS |
| Result | Malformed table accepted — you advanced on wrong output | Malformed table blocked — advance requires correction |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs. Defines the consequence of bypassing each pipeline phase.
> Pipeline overview consequence column cites PCR-NN IDs only.
> Do not embed consequence prose in the overview table.
> Each PCR entry cross-cites the FER-NN entry that makes the skip consequence detectable.

| ID     | Phase Skipped | Consequence                                                                                                                                         |
|--------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1      | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2      | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3      | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence, not output-state failure). |
| PCR-04 | Phase 4      | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools. No FER entry (file-path check, not table-output inspection). |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                               | Decision-State Anchor                                                                                                             | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                      | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected      | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                         | —                                                                                                                                 | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                              | —                                                                                                                                 | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                     | —                                                                                                                                 | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1  | —                                                                                                                                 | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                   | —                                                                                                                                 | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                          | —                                                                                                                                 | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> These rows are the SOLE source of Phase 2 coverage constraints.
> Phase 2 body contains no inline prose coverage constraint restatements; cite COV-NN only.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip consequences are declared here.
> Consequence column cites PCR-NN IDs from PHASE CONSEQUENCE REGISTRY.
> **Do not begin Phase 1 until you have read every row.**

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                                               | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|-----------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently (see FER-01)         | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table (see FER-02)                  | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2                     | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04                              | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **Stop. You are overriding IR-01:** "Skip stakeholder mapping; author signals from feature intuition." Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **Stop. You are overriding IR-05:** "Assign all signals to a single generic owner role." Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. FAILURE EXAMPLE REGISTRY FER-01 confirmed read (SEQUENTIAL and INDEPENDENT PATH columns reviewed). [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate:**

> **Stop. Do not advance until you have run BOTH of the following checks as separate acts. Record both results.**
> Match your output against FER-01 SEQUENTIAL PATH (wrong column): if your table contains
> "Output you accepted: 'S-01 | Product Manager | | '" — SK-03/SK-04 empty on any row —
> you must correct before advancing. FER-01 INDEPENDENT PATH (correct column) shows what
> the valid output requires. PCR-01 consequence: skip failure recognizable by FER-01 output inspection.

- [ ] Row count ≥ 3 (checked independently of column completeness — record result before next check)
- [ ] All four columns populated in every filled row (checked independently of row count — record result)

> Do not advance to Phase 2 until both results are recorded as separate acts.

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 2 — SIGNAL PLAN

> **Stop. You are overriding IR-02:** "Use 'high/medium/low' priority vocabulary from project-management context." Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **Stop. You are overriding IR-05:** "Assign all signals to a single generic owner role." Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

> Cite schema rows by ID. Do not restate constraint text inline.

- [ ] F-01: Priority vocabulary (see F-01)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN rows from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: ≥ 1 essential signal (see COV-01)
- [ ] COV-02: ≥ 2 distinct namespaces (see COV-02)
- [ ] COV-03: ≥ 2 distinct Producer roles (see COV-03)
- [ ] COV-04: Narrative rationale present above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row in signal table. F-05 Consumer values verified against Phase 1 SK-02. F-07 values cite IR-NN entries. Match Priority column against FER-02 SEQUENTIAL PATH before advancing.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **Stop. You are overriding IR-03:** "Collapse commit gate into signal plan section with no structural isolation." Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA. No additional constraint statements apply outside schemas.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Fill in the commit gate block:

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (essential — see COV-01):
  1. [item name from essential row]
  2. [additional essential rows if any]

PERMITTED AFTER COMMIT (recommended / optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate expressed as a condition, not a list of aspirations. PCR-03 note: this phase has no FER entry — structural absence (no isolated block) is the failure mode, not an output-inspection state.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **Stop. You are overriding IR-04:** "Omit artifact naming convention; use freeform item names." Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md entry), C-02 (strategy.md at correct path). Item name constraint: see F-04 in FIELD SCHEMA.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block handoff artifact present. [ ]

### Write 1: simulations/TOPICS.md

> Constraint: C-01. Append a row.

| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |

### Write 2: simulations/{TOPIC}/strategy.md

> Path constraint: C-02. Item name constraint: see F-04.

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste COV-04 narrative from Phase 2]

## Stakeholder Map
[paste Phase 1 fill-in table]

## Active Inertia Overrides
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04. PCR-04 note: this phase has no FER entry — path verification is the gate, not output-state inspection.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

## Criteria Coverage Map — R18

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-49: Opener declares override mission | — | YES | — | — | YES |
| C-50: Pipeline read prohibition clause | YES (inherited) | YES (inherited) | YES (inherited) | YES (inherited) | YES |
| C-51: Stop. + Record both results at independence gate | YES | — | — | YES | YES |
| C-52: Second-person failure example ("Output you accepted:") | YES | — | — | YES | YES |
| C-53: Stop. You are overriding IR-NN: at phase headers | YES | — | — | YES | YES |
| C-54: BEFORE/AFTER failure table | — | — | YES | YES | YES |
| C-55: PCR entries cross-cite FER-NN | — | — | — | — | YES |

Single-axis coverage: V-01 targets C-51/C-52/C-53 (phrasing register). V-02 targets C-49 (opener). V-03 targets C-54 (structural contrast).
Combined axes: V-04 = C-51/C-52/C-53 + C-54. V-05 = all seven.
