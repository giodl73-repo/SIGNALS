# topic-new — Round 17 Variations (V-01 through V-05)
# Rubric target: v15 (40 aspirational criteria, denominator 40)
# Date: 2026-03-15

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | C-47 as named FAILURE EXAMPLE REGISTRY (FER-NN) | Elevating the C-47 example from inline gate prose into a pre-pipeline FAILURE EXAMPLE REGISTRY (FER-01, FER-02) with stable IDs — parallel to IR-NN architecture — makes the failure example addressable by reference: the independence gate cites FER-01 by ID rather than embedding the example inline; any revision to the example propagates from one registry row; the C-48 PCR is added as a minimal 4-row block whose IDs the pipeline overview consequence column cites |
| V-02 | PCR with temporal consequence layering | Extending the PCR to carry Immediate / Downstream consequence columns — mirroring the FIELD SCHEMA C-20 pattern — makes phase-skip consequences auditable at both validation time and production time; the model reading the overview sees both "what breaks now" and "what breaks when the team uses the strategy"; C-47 is satisfied by inline gate example (V-01/R16 style) embedded at the independence gate without a separate registry |
| V-03 | Inertia-first block ordering with expanded failure table | Inverting the pre-pipeline block order so INERTIA REGISTER leads all blocks, explicitly framing every subsequent schema as an override instrument; C-47 example is expanded from a prose string into a structured BEFORE/AFTER comparison table showing the exact output sequential checking accepts and independent checking rejects; C-48 PCR is a standard 4-row block |
| V-04 | Combined: FER-NN (V-01) + PCR temporal layering (V-02) | Cross-registry citation: PCR-01 cites FER-01 in its downstream effect field ("skip failure is recognizable by FER-01 output inspection"), and FER-01 is also independently cited at the Phase 1 independence gate; two separate execution paths reach the failure example — the PCR (when reading the overview) and the gate instruction (when executing) — producing redundant C-47 satisfaction that is robust to single-path skips |
| V-05 | Combined: V-03 (inertia-first) + imperative phrasing register | Inertia-first block order with command-register phrasing throughout phase bodies ("Stop. Before Phase 1: read IR-01. Here is what wrong output looks like.") + BEFORE/AFTER failure format from V-03; tests whether direct-address framing with visual BEFORE/AFTER gate blocks increases gate-compliance rate versus the ID-citation architecture in V-04 |

---

---

## V-01 — C-47 as Named FAILURE EXAMPLE REGISTRY (FER-NN)

**Axis**: Elevate C-47 failure example to a pre-pipeline FER-NN block with stable IDs; add minimal PCR-NN for C-48.
**Hypothesis**: R16 V-01 embedded the C-47 example as inline prose at the gate. A named FER-01 block with a stable ID creates the same mechanical-coupling property as C-23 (schema IDs cited at gates): the example cannot drift from the gate because the gate cites FER-01 by reference, not by reproducing the example text. Parallel FER / IR / PCR registry architecture makes all named failure modes and consequences auditable by ID from a single pre-pipeline section.

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
> Do not begin Phase 1 until you have read every row.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                                           | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|-------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently (gate cites FER-01) | → PCR-01            | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table                            | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2                  | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04                           | → PCR-04               | → IR-04                |

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

## V-02 — PCR with Temporal Consequence Layering

**Axis**: Extend PCR columns to Immediate / Downstream split (mirroring C-20 in FIELD SCHEMA); C-47 satisfied by inline gate example rather than FER-NN registry.
**Hypothesis**: R16 V-02 had a single-column PCR. Splitting each PCR row into Immediate (what breaks at skip time) and Downstream (what breaks when the team uses the strategy) mirrors the temporal-layering pattern already required for FIELD SCHEMA by C-20, making skip-cost reasoning as auditable as field-level reasoning. The C-47 example embedded inline at the gate (not in a registry) tests whether registry-free inline placement can satisfy C-47 when the example is sufficiently concrete.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read before the pipeline overview.
> "Stakeholder Most Harmed" names who suffers most when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs.
> Pipeline overview consequence column cites PCR-NN IDs. Do not embed consequence prose in the overview.
> Each consequence is split into Immediate (at skip time) and Downstream (at use time) tiers.

| ID     | Phase | Immediate Consequence (at skip time)                                              | Downstream Effect (at use time)                                                |
|--------|-------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| PCR-01 | 1     | Signal rows carry no role ground truth; ownership undefined at write time          | Coverage gaps invisible at strategy review; gap detection fails on execution    |
| PCR-02 | 2     | Priority values fail schema validation at write time; strategy malformed           | Design Lead cannot parse readiness at decision time; commit gate unusable       |
| PCR-03 | 3     | Commit gate implicit; no structural isolation from signal plan at write time       | Engineering Lead has no enforced condition at commit time; feature ships ungated |
| PCR-04 | 4     | Topic unregistered; strategy at wrong path or with freeform names at write time   | Strategy unreachable by path-based tools; signal consumers cannot locate it     |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table. SK-NN row order = column order.
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

> Column constraint registry for the Phase 2 signal table. F-01 is leftmost. Fill left to right.
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

> Coverage constraint registry for Phase 2 aggregate. These rows are the SOLE source of Phase 2 coverage constraints.
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
> Consequence column cites PCR-NN IDs; full immediate + downstream detail in PHASE CONSEQUENCE REGISTRY above.
> Do not begin Phase 1 until you have read every row.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                              | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently     | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table              | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2    | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04             | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. [ ]

Fill in the table below. Column constraint: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate — check these two conditions INDEPENDENTLY:**

> **Independence instruction**: Check row count and column completeness as two separate acts.
> Do not chain: complete and record each check before beginning the next.
>
> Concrete sequential failure output (what independent checking rejects):
> A table reading "S-01 | Product Manager | | " — three rows present, SK-03 and SK-04 empty —
> passes the row-count condition when checked first; sequential execution advances without
> catching that SK-03/SK-04 are empty on every row. This is wrong. Check both items independently.

- [ ] Row count ≥ 3 (see SK-01 through SK-04)
- [ ] All four columns populated in every filled row (see SK-01 through SK-04)

> Do not advance to Phase 2 until both items are checked as separate, recorded acts.

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

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

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

> F-01 (Priority) is leftmost. Fill left to right.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row present. F-05 Consumer verified against Phase 1 SK-02. F-07 cites IR-NN.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

```
COMMIT GATE for {TOPIC}
========================
REQUIRED (essential — see COV-01):
  1. [item name from essential row]

PERMITTED AFTER COMMIT:
  - [remaining signals]

Enforcement: no design commit proceeds until REQUIRED signals exist as files.
```

**Exit gate**: Gate written. ≥ 1 essential signal named. Gate expressed as a condition.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md), C-02 (strategy.md). Item name constraint: see F-04.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block present. [ ]

Write `simulations/TOPICS.md` row (C-01): `| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |`

Write `simulations/{TOPIC}/strategy.md` (C-02): include Rationale, Stakeholder Map, Signal Plan, Commit Gate sections.

**Exit gate**: Both files at correct paths. All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-03 — Inertia-First Block Ordering with Expanded Failure Table

**Axis**: INERTIA REGISTER leads all pre-pipeline blocks; C-47 example formatted as a BEFORE/AFTER comparison table; standard PCR-NN for C-48.
**Hypothesis**: In V-01 and V-02, constraints appear before the inertia context that motivates them. A model reading FIELD SCHEMA before INERTIA REGISTER encounters enforcement rules without knowing what defaults they override. Placing INERTIA REGISTER first — with an explicit header: "These are the defaults this skill overrides. Every block that follows exists to prevent these defaults from applying" — makes each schema feel motivated by a named inertia pattern. The C-47 example is expanded into a structured BEFORE/AFTER comparison table showing the full sequential-output state and the full independent-rejection outcome, making the failure recognizable as a visual inspection pattern rather than as a named description.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> **Read this register first. These are the defaults this skill overrides.**
> Every schema, phase, and gate that follows exists to prevent these defaults from applying.
> "Stakeholder Most Harmed" names who bears the cost when a default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs.
> Pipeline overview consequence column cites PCR-NN IDs. Do not embed consequence prose in overview.

| ID     | Phase | Consequence                                                                                         |
|--------|-------|-----------------------------------------------------------------------------------------------------|
| PCR-01 | 1     | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails  |
| PCR-02 | 2     | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness   |
| PCR-03 | 3     | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated    |
| PCR-04 | 4     | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools            |

---

## STAKEHOLDER SCHEMA

> Column constraints for the Phase 1 fill-in table. Exists to override IR-01 and IR-05.
> SK-NN row order = column order. SOLE source of Phase 1 column constraints.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraints for the Phase 2 signal table. Exists to override IR-02, IR-04, IR-05.
> F-01 is leftmost. Fill left to right. SOLE source of Phase 2 column constraints.

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

> Coverage constraints for Phase 2 aggregate. Exists to override IR-02, IR-05.
> SOLE source of Phase 2 coverage constraints.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> Skip consequences cite PCR-NN IDs. Inertia defaults cite IR-NN IDs.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                              | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently     | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table              | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2    | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04             | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read. STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. [ ]

Fill in the table below. Column constraint for each cell: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate — check these two conditions INDEPENDENTLY:**

> **Independence instruction**: Check row count and column completeness as two separate acts.
> Do not chain. Complete and record each check before beginning the next.
>
> **Sequential failure example** — output that sequential checking accepts and independent checking rejects:
>
> SEQUENTIAL CHECKING (WRONG):
> | Row ID | Decision-Maker Role | Risk Exposure | Decision Informed |
> | S-01   | Product Manager     |               |                   |
> | S-02   | Design Lead         |               |                   |
> | S-03   | Engineering Lead    |               |                   |
> Step 1 — row count: 3 rows present. ≥ 3. PASS. Execution advances without checking columns.
>
> INDEPENDENT CHECKING (CORRECT):
> Step 1 — row count: 3 rows present. ≥ 3. PASS. Record result. Stop.
> Step 2 — column completeness: SK-03 empty on S-01, S-02, S-03. SK-04 empty on S-01, S-02, S-03. FAIL.
> Do not advance. Table is not compliant. Sequential checking above would have missed this.

- [ ] Row count ≥ 3 (see SK-01 through SK-04)
- [ ] All four columns populated in every filled row (see SK-01 through SK-04)

> Do not advance to Phase 2 until both items are checked as independent acts and both pass.

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

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

- [ ] F-01 through F-07 (see FIELD SCHEMA)
- [ ] COV-01 through COV-04 (see COVERAGE SCHEMA)
- [ ] F-05 Consumer values verified verbatim against Phase 1 SK-02 column

### SIGNAL TABLE

> F-01 (Priority) is leftmost. Fill left to right. Constraint per column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row. F-05 Consumer verified against Phase 1 SK-02. F-07 cites IR-NN.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA.

**Entry gate**: Phase 2 exit gate cleared AND signal table present. [ ]

```
COMMIT GATE for {TOPIC}
========================
REQUIRED (essential — see COV-01):
  1. [item name from essential row]

PERMITTED AFTER COMMIT:
  - [remaining signals]

Enforcement: no design commit proceeds until REQUIRED signals exist as files.
```

**Exit gate**: Gate written. ≥ 1 essential signal named. Gate expressed as a condition.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md), C-02 (strategy.md). Item name constraint: see F-04.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block present. [ ]

Write `simulations/TOPICS.md` row (C-01): `| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |`

Write `simulations/{TOPIC}/strategy.md` (C-02): Rationale, Stakeholder Map, Signal Plan, Commit Gate sections.

**Exit gate**: Both files at correct paths. All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-04 — Combined: FER-NN (V-01) + PCR Temporal Layering (V-02)

**Axis**: FER-NN pre-pipeline registry (from V-01) combined with temporally-layered PCR (from V-02); cross-registry citation in PCR-01.
**Hypothesis**: In V-01, FER-01 is cited at the gate. In V-02, the PCR has temporal layers. Combining both creates a cross-registry citation: PCR-01 includes in its Downstream Effect field a note that "skip failure is recognizable by FER-01 output inspection at Phase 1 gate." This means two independent execution paths reach the failure example: the PCR path (a model reading the overview sees PCR-01's downstream note citing FER-01) and the gate-instruction path (Phase 1 exit gate cites FER-01 directly). Redundant citation makes C-47 structurally robust to single-path skips.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read before pipeline overview.
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

> Pre-pipeline. Stable FER-NN IDs. Gate instructions cite FER-NN IDs by reference; do not restate inline.
> Each row: the concrete output sequential checking accepts AND independent checking rejects.

| ID     | Phase | Sequential Output State (ACCEPTED by sequential — wrong)                                           | Independent Rejection (what independent check catches)                                                              |
|--------|-------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| FER-01 | 1     | Stakeholder table has 3 rows; SK-01 populated; SK-03 and SK-04 cells empty on all rows             | Row-count check passes (≥ 3); column-completeness check finds SK-03/SK-04 empty — sequential checking would call this compliant; it is not |
| FER-02 | 2     | Signal table has 4 rows; F-01 (Priority) column contains "high / medium / low"                     | Row-count check passes; F-01 vocabulary check rejects "high" — not in {essential/recommended/optional}             |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs. Temporally layered: Immediate (at skip time) + Downstream (at use time).
> Pipeline overview consequence column cites PCR-NN IDs only; detail lives here.

| ID     | Phase | Immediate Consequence (at skip time)                                              | Downstream Effect (at use time)                                                                    |
|--------|-------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| PCR-01 | 1     | Signal rows carry no role ground truth; ownership undefined at write time          | Coverage gaps invisible at strategy review; skip failure recognizable by FER-01 output inspection  |
| PCR-02 | 2     | Priority values fail F-01 schema validation at write time; strategy malformed      | Design Lead cannot parse readiness at decision time; commit gate unusable; skip recognizable by FER-02 |
| PCR-03 | 3     | Commit gate implicit; no structural isolation from signal plan at write time       | Engineering Lead has no enforced condition at commit time; feature ships ungated                    |
| PCR-04 | 4     | Topic unregistered; strategy at wrong path or freeform item names at write time   | Strategy unreachable by path-based tools; signal consumers cannot locate artifacts                  |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table. SK-NN row order = column order.
> SOLE source of Phase 1 column constraints. Phase 1 body cites SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table. F-01 is leftmost. Fill left to right.
> SOLE source of Phase 2 column constraints. Phase 2 body cites F-NN only.

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

> Coverage constraint registry for Phase 2 aggregate. SOLE source of Phase 2 coverage constraints.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> Consequence column cites PCR-NN IDs; full detail (including FER citations) in PHASE CONSEQUENCE REGISTRY.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                              | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently     | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table              | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2    | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04             | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read. STAKEHOLDER SCHEMA confirmed read. FAILURE EXAMPLE REGISTRY FER-01 confirmed read. [ ]

Fill in the table below. Column constraint per cell: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate — check these two conditions INDEPENDENTLY:**

> **Independence instruction**: Check row count and column completeness as two separate acts.
> Do not chain. Complete and record each check before beginning the next.
> Failure mode: see **FER-01** — this entry shows the exact output sequential checking accepts
> (3 rows, SK-03/SK-04 empty) and names why independent checking rejects it.

- [ ] Row count ≥ 3 (see SK-01 through SK-04)
- [ ] All four columns populated in every filled row (see SK-01 through SK-04)

> Do not advance to Phase 2 until both items are independently checked and both pass.

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

> Fill-in step. Constraint: see COV-04.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

- [ ] F-01 through F-07 (see FIELD SCHEMA)
- [ ] COV-01 through COV-04 (see COVERAGE SCHEMA)
- [ ] F-05 Consumer values verified verbatim against Phase 1 SK-02 column

### SIGNAL TABLE

> F-01 (Priority) is leftmost. Fill left to right. Constraint per column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: Pre-write gate cleared. ≥ 1 row. F-05 Consumer verified against Phase 1 SK-02. F-07 cites IR-NN.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01.

**Entry gate**: Phase 2 exit gate cleared AND signal table present. [ ]

```
COMMIT GATE for {TOPIC}
========================
REQUIRED (essential — see COV-01):
  1. [item name from essential row]

PERMITTED AFTER COMMIT:
  - [remaining signals]

Enforcement: no design commit proceeds until REQUIRED signals exist as files.
```

**Exit gate**: Gate written. ≥ 1 essential signal named. Gate expressed as a condition.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01 (TOPICS.md), C-02 (strategy.md). Item name constraint: see F-04.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block present. [ ]

Write `simulations/TOPICS.md` row (C-01): `| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |`

Write `simulations/{TOPIC}/strategy.md` (C-02): Rationale, Stakeholder Map, Signal Plan, Commit Gate sections.

**Exit gate**: Both files at correct paths. All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-05 — Combined: V-03 (Inertia-First) + Imperative Phrasing Register

**Axis**: Inertia-first block ordering (from V-03) combined with command-register phrasing throughout; C-47 formatted as BEFORE/AFTER comparison block at the gate.
**Hypothesis**: V-01 through V-04 use instructional-register phrasing ("Fill in the table. Check these conditions."). A command register — direct address with imperative statements at each gate ("Stop. Before you write: run this check. Here is what wrong looks like.") — makes each gate a more active decision point. BEFORE/AFTER comparison at the Phase 1 independence gate formats the C-47 example as two labeled states — BEFORE (sequential path, wrong) and AFTER (independent path, correct) — that the model must explicitly distinguish before advancing. Tests whether imperative framing + labeled states outperforms ID-citation framing for gate-compliance rates.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Read this first. These are the defaults you are overriding.
> Each schema and phase that follows exists to prevent one or more of these defaults.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## PHASE CONSEQUENCE REGISTRY

> These are the costs of skipping each phase. Pipeline overview cites PCR-NN IDs only.

| ID     | Phase | Consequence                                                                                         |
|--------|-------|-----------------------------------------------------------------------------------------------------|
| PCR-01 | 1     | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails  |
| PCR-02 | 2     | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness   |
| PCR-03 | 3     | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated    |
| PCR-04 | 4     | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools            |

---

## STAKEHOLDER SCHEMA

> These column rules enforce the override of IR-01 and IR-05.
> All Phase 1 column constraints live here — nowhere else.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal     |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> These column rules enforce the overrides of IR-02, IR-04, IR-05.
> All Phase 2 column constraints live here — nowhere else. F-01 is leftmost.

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

> These coverage rules enforce the overrides of IR-02 and IR-05.
> All Phase 2 coverage constraints live here — nowhere else.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> Read this entire table before executing Phase 1.
> Consequences are in PHASE CONSEQUENCE REGISTRY (PCR-NN).

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                              | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|--------------------------|------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND column completeness independently     | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table              | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2    | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04             | → PCR-04               | → IR-04                |

---

## PHASE 1 — STAKEHOLDER MAP

Stop. Before you write anything in Phase 1, read this:

> You are overriding **IR-01**: "Skip stakeholder mapping; author signals from feature intuition."
> IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> You are also overriding **IR-05**: "Assign all signals to a single generic owner role."
> IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints for this phase: see SK-01 through SK-04 in STAKEHOLDER SCHEMA. No other column constraints apply.

**Entry gate**: INERTIA REGISTER confirmed read. STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. [ ]

Fill in the table below. Every cell: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Stop. Do not advance until you have run BOTH of the following checks as separate acts.**

Check these two conditions INDEPENDENTLY — one at a time, recorded individually:

> Here is what goes wrong when you check sequentially instead of independently:
>
> BEFORE — sequential path (wrong):
> You check row count first: 3 rows present. ≥ 3. Condition met.
> You advance. You never check column completeness.
> Output you accepted: "S-01 | Product Manager | | " — SK-03 and SK-04 empty on all rows.
> This output is malformed. Sequential checking accepted it. This is wrong.
>
> AFTER — independent path (correct):
> Check 1: Row count. 3 rows present. ≥ 3. PASS. Record result. Stop. Do not advance to Check 2 yet.
> Check 2: Column completeness. SK-03 empty on S-01, S-02, S-03. FAIL. Do not advance.
> The independent check catches what sequential checking missed.

- [ ] Row count ≥ 3 (see SK-01 through SK-04 in STAKEHOLDER SCHEMA)
- [ ] All four columns populated in every filled row (see SK-01 through SK-04 in STAKEHOLDER SCHEMA)

Record both results. Only advance to Phase 2 when both checks pass independently.

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 2 — SIGNAL PLAN

Stop. Before you write any signal rows, read this:

> You are overriding **IR-02**: "Use 'high/medium/low' priority vocabulary from project-management context."
> IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> You are also overriding **IR-05**. IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No other constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

Write ≥ 2 sentences here. Constraint: see COV-04 in COVERAGE SCHEMA.

[Model fills here]

### PRE-WRITE GATE

Run all items before writing the signal table:

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
- [ ] COV-04: Narrative rationale written above (see COV-04)

### SIGNAL TABLE

Write left to right. F-01 (Priority) is leftmost. Constraint per column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: All pre-write gate items cleared. ≥ 1 row present. F-05 Consumer verified against Phase 1 SK-02. F-07 cites IR-NN.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

Stop. You are overriding **IR-03**: "Collapse commit gate into signal plan section with no structural isolation."
IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**

Constraint: see COV-01 in COVERAGE SCHEMA.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

Write the commit gate block below. Do not embed it in the signal plan section.

```
COMMIT GATE for {TOPIC}
========================
REQUIRED (essential — see COV-01):
  1. [item name from essential row]

PERMITTED AFTER COMMIT:
  - [remaining signals]

Enforcement: no design commit proceeds until REQUIRED signals exist as files.
```

**Exit gate**: Gate block written as its own section. ≥ 1 essential signal named. Expressed as a condition.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

Stop. You are overriding **IR-04**: "Omit artifact naming convention; use freeform item names."
IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**

Path constraints: C-01 (TOPICS.md), C-02 (strategy.md). Item name constraint: see F-04 in FIELD SCHEMA.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block present. [ ]

Write `simulations/TOPICS.md` row (C-01): `| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |`

Write `simulations/{TOPIC}/strategy.md` (C-02): include Rationale, Stakeholder Map, Signal Plan, and Commit Gate sections.

**Exit gate**: Both files written at correct paths. All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```
