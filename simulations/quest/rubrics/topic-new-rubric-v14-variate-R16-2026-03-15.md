# topic-new — Round 16 Variations (V-01 through V-05)
# Rubric target: v14 (38 aspirational criteria, denominator 38)
# Date: 2026-03-15

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Combined registry baseline | Synthesizing R15 V-01 (schema-as-sole-truth, C-45) and R15 V-02 (stakeholder-named inertia, C-46) into one coherent architecture — where pre-pipeline schemas are the sole constraint source AND the INERTIA REGISTER carries a "Stakeholder Most Harmed" column — produces the minimal v14-compliant prompt; all phases cite only schema IDs; IR-NN citations carry role names at every override directive and exit gate reproduction |
| V-02 | V-01 + PIPELINE CONSEQUENCE REGISTER (PCR-NN) | Extracting the "If Skipped" costs from the pipeline overview into a dedicated pre-pipeline PIPELINE CONSEQUENCE REGISTER (PCR-01 through PCR-04) with stable IDs — parallel to INERTIA REGISTER architecture — makes skip costs consultable by ID throughout execution rather than only at the pipeline overview row; the pipeline overview "If Skipped" column becomes PCR-NN citations rather than prose, closing the skip-cost prose-drift channel that remains in V-01 |
| V-03 | V-01 + PRIORITY SCHEMA isolation | Elevating priority vocabulary from an F-01 constraint cell to a dedicated pre-pipeline PRIORITY SCHEMA block (P-01 / P-02 / P-03) with stable IDs, decision-state anchors, and consequences — and having F-01 reference "see PRIORITY SCHEMA" rather than restating vocabulary inline — makes the commit-gate vocabulary mechanically auditable: any revision to priority semantics propagates from one named schema block rather than from F-01 cell text scattered across three citation points |
| V-04 | V-01 + COMMITMENT BLOCK gate topology | Replacing checkbox exit gate lists with structured COMMITMENT BLOCK fill-in templates — where the model must actively author the compliance state of each condition (e.g., "Row count: ___ ≥ 3: Status: PASS / FAIL") — produces stronger phase-boundary enforcement: active authorship of each gate condition is a higher-fidelity commitment act than passive checkbox ticking; C-28 and C-30 independence conditions are satisfied by template structure rather than by an explicit prose instruction |
| V-05 | V-01 + PCR-NN + PRIORITY SCHEMA + COMMITMENT BLOCK | Maximum structural compression: three new pre-pipeline registries (INERTIA REGISTER, PIPELINE CONSEQUENCE REGISTER, PRIORITY SCHEMA) alongside the four pre-pipeline schemas (STAKEHOLDER, FIELD, COVERAGE); phases contain only registry/schema-ID references and COMMITMENT BLOCK fill-in slots; all prose that could drift lives in a named block with a stable ID; tests whether maximum pre-execution registry density produces the most consistent structural compliance across all 38 criteria |

---

---

## V-01 — Combined Registry Baseline

**Axis**: Schema-as-sole-truth (C-45) + Stakeholder-named inertia (C-46) synthesized as one coherent prompt.
**Hypothesis**: R15 V-01 satisfied C-45 but failed C-42/C-43/C-44. R15 V-02 satisfied C-42/C-43/C-44 but had inline prose in phase bodies (fails C-45). No R15 variation satisfies both simultaneously. V-01 here merges both: pre-pipeline schemas are the SOLE source of all constraints; INERTIA REGISTER carries "Stakeholder Most Harmed" column; every IR-NN citation at phase overrides and exit gates includes the role name.
**Key Structural Difference from R15**: All four schemas (STAKEHOLDER, FIELD, COVERAGE) are pre-pipeline blocks; INERTIA REGISTER has four columns including "Stakeholder Most Harmed"; phase bodies contain zero inline prose constraint restatements; IR-NN cited with role name at every enforcement point.

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

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                              | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|-------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                          | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user" | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for the signal |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm       | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                  | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is the leftmost column. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                               | Decision-State Anchor                                                                                                                                                                     | Immediate Failure                           | Downstream Effect                                                   |
|------|---------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                      | essential = consumer cannot decide without this (decision blocked); recommended = consumer decides with increased exposure (quality risk accepted); optional = consumer decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic         | —                                                                                                                                                                                         | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                          |
| F-03 | Skill               | Named skill existing under stated namespace                              | —                                                                                                                                                                                         | Non-existent reference                      | Signal uncollectable; evidence gap invisible                        |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form     | —                                                                                                                                                                                         | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                            |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1 table | —                                                                                                                                                                        | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability      |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                   | —                                                                                                                                                                                         | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded        |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role          | —                                                                                                                                                                                         | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time            |

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
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                              | If I Skip This Phase, I Will…                       | Team Default (→ IR-NN) | Recovery Cost If Caught Late                               |
|-------|-----------------|--------------------------|------------------------------------------------------------------|-----------------------------------------------------|------------------------|------------------------------------------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND col completeness independently        | author orphan signal rows with no role ground truth | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05+F-06+F-07; re-run Phases 2–4 |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table              | produce malformed strategy unusable as commit gate  | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md       |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2    | ship feature with no enforced readiness condition   | → IR-03                | Re-run Phase 3; re-write commit gate section               |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files at correct paths; item names follow F-04             | topic unregistered; strategy unreachable            | → IR-04                | Re-write both artifacts; re-run path verification          |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate** — check these two conditions INDEPENDENTLY:

> Check independently. Sequential checking produces this failure: "3 rows, columns empty" reads as compliant — this is wrong. Check both items as separate acts before advancing.

- [ ] SK-01–SK-04: Row count ≥ 3 (see SK-01, SK-02, SK-03, SK-04)
- [ ] SK-01–SK-04: All four columns populated in every filled row (see SK-01, SK-02, SK-03, SK-04)

> Do not advance to Phase 2 until both conditions are independently satisfied.

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

[Model fills here]

### PRE-WRITE GATE

> Cite schema rows by ID. Do not restate constraint text inline.

- [ ] F-01: Priority vocabulary (see F-01)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN rows from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: Essential signal count (see COV-01)
- [ ] COV-02: Namespace count (see COV-02)
- [ ] COV-03: Distinct Producer role count (see COV-03)
- [ ] COV-04: Narrative rationale present above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: All pre-write gate items cleared. Signal table contains ≥ 1 row. F-05 Consumer values verified against Phase 1 SK-02. F-07 values cite IR-NN entries.

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
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see pre-pipeline INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04 (see F-04).

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-02 — V-01 + PIPELINE CONSEQUENCE REGISTER (PCR-NN)

**Axis**: PIPELINE CONSEQUENCE REGISTER — extracting skip costs from pipeline overview into a named pre-pipeline registry with stable PCR-NN IDs.
**Hypothesis**: In V-01, the "If Skipped" consequence for each phase lives only as prose in the pipeline overview table row. When a model is executing Phase 2 it cannot retrieve PCR text by ID — it must re-read the overview row. Extracting skip costs into a dedicated PIPELINE CONSEQUENCE REGISTER (PCR-01 through PCR-04) with stable IDs — parallel to INERTIA REGISTER — makes phase skip consequences consultable by ID at any pipeline point, mirrors the IR-NN registry architecture, and closes the skip-cost prose-drift channel that persists in V-01.
**Key Structural Difference from V-01**: Adds a PIPELINE CONSEQUENCE REGISTER block (PCR-01–PCR-04) before the pipeline overview; pipeline overview "If I Skip" column carries → PCR-NN references rather than inline prose; phase entry gates cite PCR-NN alongside IR-NN.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read before pipeline overview.
> "Stakeholder Most Harmed" names who suffers when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## PIPELINE CONSEQUENCE REGISTER

> Pre-pipeline. Stable PCR-NN IDs. Read before pipeline overview.
> Names what breaks when each phase is skipped. Pipeline overview "If Skipped" column cites by PCR-NN.
> Phase entry gates reproduce PCR-NN text so skip consequences are visible at execution time.

| ID     | Phase Skipped | Consequence                                                                                             | Who Bears the Cost              |
|--------|---------------|---------------------------------------------------------------------------------------------------------|---------------------------------|
| PCR-01 | Phase 1       | Signal rows authored with no stakeholder basis; F-05 Consumer and F-06 Stakeholder Ref are orphaned; Phase 2 cannot satisfy COV-03 without rework | Product Manager, Engineering Lead |
| PCR-02 | Phase 2       | Strategy file produced without valid priority vocabulary or cross-functional ownership; strategy cannot serve as a commit gate | Design Lead, cross-functional team |
| PCR-03 | Phase 3       | No enforced readiness condition exists at design commit; feature can ship without any evidence gate     | Engineering Lead                |
| PCR-04 | Phase 4       | Topic not registered in TOPICS.md; strategy.md absent or at wrong path; downstream tools cannot locate signals | All consumers                  |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for Phase 1. SK-NN row order = column order.
> SOLE source of Phase 1 column constraints. No inline prose constraint restatements in Phase 1 body.

| ID    | Column Name         | Constraint                                                              | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|-------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                          | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user" | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for the signal |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm       | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                  | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for Phase 2 signal table. F-01 leftmost. Fill left to right.
> SOLE source of Phase 2 column constraints. No inline prose constraint restatements in Phase 2 body.

| ID   | Field               | Constraint                                                               | Decision-State Anchor                                                                                                                                                                     | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                      | essential = consumer cannot decide without this (decision blocked); recommended = consumer decides with increased exposure (quality risk accepted); optional = consumer decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness  |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic         | —                                                                                                                                                                                         | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                              | —                                                                                                                                                                                         | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form     | —                                                                                                                                                                                         | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer verbatim as SK-02 in Phase 1 | —                                                                                                                                                                                      | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                   | —                                                                                                                                                                                         | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role          | —                                                                                                                                                                                         | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> SOLE source of Phase 2 coverage constraints. No inline prose coverage restatements in Phase 2 body.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                           | If I Skip This Phase (→ PCR-NN) | Team Default (→ IR-NN) | Recovery Cost If Caught Late                               |
|-------|-----------------|--------------------------|---------------------------------------------------------------|---------------------------------|------------------------|------------------------------------------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND col completeness independently     | → PCR-01                        | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05+F-06+F-07; re-run Phases 2–4 |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table           | → PCR-02                        | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md       |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2 | → PCR-03                        | → IR-03                | Re-run Phase 3; re-write commit gate section               |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files correct paths; item names follow F-04             | → PCR-04                        | → IR-04                | Re-write both artifacts; re-run path verification          |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
> Skipping this phase activates PCR-01: see PIPELINE CONSEQUENCE REGISTER.
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read. PIPELINE CONSEQUENCE REGISTER confirmed read. STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate** — check these two conditions INDEPENDENTLY:

> Check independently. Sequential checking produces this failure: "3 rows, columns empty" reads as compliant. Check both items as separate acts before advancing.

- [ ] SK-01–SK-04: Row count ≥ 3 (see SK-01, SK-02, SK-03, SK-04)
- [ ] SK-01–SK-04: All four columns populated in every filled row (see SK-01, SK-02, SK-03, SK-04)

> Do not advance to Phase 2 until both conditions are independently satisfied.

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

**PCR-01 verbatim at exit**: "Signal rows authored with no stakeholder basis; F-05 Consumer and F-06 Stakeholder Ref are orphaned; Phase 2 cannot satisfy COV-03 without rework." Phase 1 overrides this consequence.

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02.** IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
> Skipping this phase activates PCR-02: see PIPELINE CONSEQUENCE REGISTER.
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here]

### PRE-WRITE GATE

- [ ] F-01: Priority vocabulary (see F-01)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: Essential signal count (see COV-01)
- [ ] COV-02: Namespace count (see COV-02)
- [ ] COV-03: Distinct Producer role count (see COV-03)
- [ ] COV-04: Narrative rationale written above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: All pre-write gate items cleared. Signal table ≥ 1 row. F-05 Consumer verified against Phase 1 SK-02. F-07 cites IR-NN.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

**PCR-02 verbatim at exit**: "Strategy file produced without valid priority vocabulary or cross-functional ownership; strategy cannot serve as a commit gate." Phase 2 overrides this consequence.

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
> Skipping this phase activates PCR-03: see PIPELINE CONSEQUENCE REGISTER.
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA. No additional constraints apply outside schemas.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

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

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate is a condition, not a list of aspirations.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

**PCR-03 verbatim at exit**: "No enforced readiness condition exists at design commit; feature can ship without any evidence gate." Phase 3 overrides this consequence.

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
> Skipping this phase activates PCR-04: see PIPELINE CONSEQUENCE REGISTER.
>
> Path constraints: C-01, C-02. Item name constraint: see F-04.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block present. [ ]

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
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see pre-pipeline INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files at correct paths (see C-01, C-02). Item names follow F-04 (see F-04).

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."

**PCR-04 verbatim at exit**: "Topic not registered in TOPICS.md; strategy.md absent or at wrong path; downstream tools cannot locate signals." Phase 4 overrides this consequence.
```

---

---

## V-03 — V-01 + PRIORITY SCHEMA Isolation

**Axis**: Priority vocabulary elevated from an F-01 constraint cell to a dedicated pre-pipeline PRIORITY SCHEMA block with stable P-01/P-02/P-03 IDs and decision-state anchors.
**Hypothesis**: In V-01, priority vocabulary lives inside F-01's "Constraint" cell as a list of three values plus a multi-clause anchor. When F-01 is cited at gates ("see F-01"), the model retrieves the full cell text — but the vocabulary and decision-state anchors are buried inside a field definition alongside routing failures and downstream effects. Isolating priority vocabulary into its own named PRIORITY SCHEMA block with P-01/P-02/P-03 IDs makes each value independently citable ("see P-01 for essential"), makes the decision-state anchor for each value available as a standalone reference, and creates a mechanically auditable vocabulary register. F-01 in FIELD SCHEMA becomes a pointer ("see PRIORITY SCHEMA") rather than a definition, eliminating the dual-source drift risk where cell text and external PRIORITY SCHEMA could diverge.
**Key Structural Difference from V-01**: Adds PRIORITY SCHEMA block (P-01/P-02/P-03) before FIELD SCHEMA; F-01 constraint cell references PRIORITY SCHEMA rather than listing vocabulary inline; pre-write gate cites P-NN alongside F-NN for priority validation.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read before pipeline overview.
> "Stakeholder Most Harmed" names who suffers when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## PRIORITY SCHEMA

> Valid vocabulary registry for the F-01 Priority field.
> P-NN row order = decision-state severity (descending). Cite P-NN when referencing a specific priority value.
> These rows are the SOLE source of priority vocabulary definitions.
> Do not restate priority vocabulary or decision-state anchors in any other block or phase body.

| ID   | Value        | Decision-State Anchor                                                                             | If Used Incorrectly                                                                            | Downstream Effect                                                            |
|------|--------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| P-01 | essential    | Consumer cannot make this decision without this signal — decision is blocked until signal exists  | Strategy lists a non-blocking signal as essential; commit gate requires unnecessary evidence  | Team blocks commit on optional evidence; velocity loss with no quality gain  |
| P-02 | recommended  | Consumer can decide without this signal but accepts increased exposure — quality risk is accepted | Strategy omits a recommended signal; consumer decides blind on a quality dimension            | Decision made with unacceptable evidence gap; defect surfaces post-commit    |
| P-03 | optional     | Consumer decides unaffected — signal is supplementary enrichment only                            | Strategy marks an enrichment signal as essential; commit gate is unnecessarily broad          | Same as P-01 downstream; commit gated on enrichment, not readiness evidence  |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for Phase 1. SK-NN row order = column order.
> SOLE source of Phase 1 column constraints. No inline prose constraint restatements in Phase 1 body.

| ID    | Column Name         | Constraint                                                              | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|-------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                          | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user" | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for the signal |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm       | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                  | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for Phase 2 signal table. F-01 leftmost. Fill left to right.
> SOLE source of Phase 2 column constraints. No inline prose constraint restatements in Phase 2 body.
> F-01 vocabulary is defined in PRIORITY SCHEMA; see P-01/P-02/P-03 for valid values and anchors.

| ID   | Field               | Constraint                                                               | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|--------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | See PRIORITY SCHEMA (P-01 / P-02 / P-03) — no other values valid        | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness  |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic         | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                              | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form     | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer verbatim as SK-02         | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                   | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role          | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> SOLE source of Phase 2 coverage constraints. No inline prose coverage restatements in Phase 2 body.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                           | If I Skip This Phase, I Will…                       | Team Default (→ IR-NN) | Recovery Cost If Caught Late                               |
|-------|-----------------|--------------------------|---------------------------------------------------------------|-----------------------------------------------------|------------------------|------------------------------------------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | SK-01–SK-04; row count AND col completeness independently     | author orphan signal rows with no role ground truth | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05+F-06+F-07; re-run Phases 2–4 |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table           | produce malformed strategy unusable as commit gate  | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md       |
| 3     | Commit Gate     | Gate definition block    | Gate names ≥ 1 essential; structurally isolated from Phase 2 | ship feature with no enforced readiness condition   | → IR-03                | Re-run Phase 3; re-write commit gate section               |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | Both files correct paths; item names follow F-04             | topic unregistered; strategy unreachable            | → IR-04                | Re-write both artifacts; re-run path verification          |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). PRIORITY SCHEMA P-01–P-03 confirmed read. STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**Exit gate** — check these two conditions INDEPENDENTLY:

> Check independently. Sequential checking produces this failure: "3 rows, columns empty" reads as compliant. Check both as separate acts before advancing.

- [ ] SK-01–SK-04: Row count ≥ 3 (see SK-01, SK-02, SK-03, SK-04)
- [ ] SK-01–SK-04: All four columns populated in every filled row (see SK-01, SK-02, SK-03, SK-04)

**IR-01 verbatim at exit**: Default: "Skip stakeholder mapping; author signals from feature intuition." Override active: Phase 1. Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02.** IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Priority vocabulary: see PRIORITY SCHEMA (P-01/P-02/P-03). Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here]

### PRE-WRITE GATE

- [ ] F-01 / P-01–P-03: Priority values are P-01 (essential), P-02 (recommended), or P-03 (optional) only (see F-01, PRIORITY SCHEMA)
- [ ] F-02: Namespace values (see F-02)
- [ ] F-03: Skill values (see F-03)
- [ ] F-04: Item names (see F-04)
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 (see F-05)
- [ ] F-06: Stakeholder Ref values cite S-NN from Phase 1 (see F-06)
- [ ] F-07: Team Default values cite IR-NN (see F-07)
- [ ] COV-01: Essential signal count (see COV-01)
- [ ] COV-02: Namespace count (see COV-02)
- [ ] COV-03: Distinct Producer role count (see COV-03)
- [ ] COV-04: Narrative rationale written above (see COV-04)

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Priority values: P-01 = essential, P-02 = recommended, P-03 = optional (see PRIORITY SCHEMA).

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**Exit gate**: All pre-write gate items cleared. Signal table ≥ 1 row. F-05 Consumer verified against Phase 1 SK-02. F-01 values verified against PRIORITY SCHEMA.

**IR-02 verbatim at exit**: Default: "Use 'high/medium/low' priority vocabulary from project-management context." Override active: Phase 2. Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority."

**IR-05 verbatim at exit**: Default: "Assign all signals to a single generic owner role." Override active: Phase 2. Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses."

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01. Essential signal vocabulary: see P-01 in PRIORITY SCHEMA. No additional constraints apply outside schemas.

**Entry gate**: Phase 2 exit gate cleared AND signal table handoff artifact present. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (P-01 essential — see PRIORITY SCHEMA P-01, COV-01):
  1. [item name from P-01 row]
  2. [additional P-01 rows if any]

PERMITTED AFTER COMMIT (P-02 recommended / P-03 optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Commit gate block written. ≥ 1 P-01 essential signal named (see P-01, COV-01). Gate is a condition, not a list of aspirations.

**IR-03 verbatim at exit**: Default: "Collapse commit gate into signal plan section with no structural isolation." Override active: Phase 3. Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time."

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01, C-02. Item name constraint: see F-04.

**Entry gate**: Phase 3 exit gate cleared AND commit gate block present. [ ]

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
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see pre-pipeline INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files at correct paths (see C-01, C-02). Item names follow F-04 (see F-04). Priority values in strategy.md match PRIORITY SCHEMA vocabulary.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-04 — V-01 + COMMITMENT BLOCK Gate Topology

**Axis**: Replaces checkbox exit gate lists with structured COMMITMENT BLOCK fill-in templates requiring active authorship of each compliance condition.
**Hypothesis**: Checkbox gates (V-01 through V-03) require the model to passively acknowledge conditions — marking a box is a one-bit act that can be performed without engaging with the condition content. COMMITMENT BLOCK templates require active authorship: the model must write the actual observed value (e.g., "Row count: 3") and a Status verdict (PASS / FAIL). This two-field authorship act requires the model to retrieve and state the actual state rather than affirm a condition abstractly. C-28 (row count AND column completeness independently) and C-30 (independence instruction explicit) are satisfied by template structure rather than by a prose independence instruction — each field in the block is an independent authorship act.
**Key Structural Difference from V-01**: All phase exit gates are COMMITMENT BLOCKs with `Observed: ___` and `Status: PASS / FAIL` fields rather than checkbox lists; independence between row count and column completeness is structural (two separate template fields) rather than instructional (a prose reminder).

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read before pipeline overview.
> "Stakeholder Most Harmed" names who suffers when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for Phase 1. SK-NN row order = column order.
> SOLE source of Phase 1 column constraints. No inline prose constraint restatements in Phase 1 body.

| ID    | Column Name         | Constraint                                                              | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|-------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                          | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user" | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for the signal |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm       | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                  | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for Phase 2 signal table. F-01 leftmost. Fill left to right.
> SOLE source of Phase 2 column constraints. No inline prose constraint restatements in Phase 2 body.

| ID   | Field               | Constraint                                                               | Decision-State Anchor                                                                                                                                                                     | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                      | essential = consumer cannot decide without this (decision blocked); recommended = consumer decides with increased exposure (quality risk accepted); optional = consumer decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness  |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic         | —                                                                                                                                                                                         | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                              | —                                                                                                                                                                                         | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form     | —                                                                                                                                                                                         | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer verbatim as SK-02         | —                                                                                                                                                                                         | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                   | —                                                                                                                                                                                         | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role          | —                                                                                                                                                                                         | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> SOLE source of Phase 2 coverage constraints. No inline prose coverage restatements in Phase 2 body.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                           | If I Skip This Phase, I Will…                       | Team Default (→ IR-NN) | Recovery Cost If Caught Late                               |
|-------|-----------------|--------------------------|---------------------------------------------------------------|-----------------------------------------------------|------------------------|------------------------------------------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | COMMITMENT BLOCK: row count ≥ 3 AND all cols populated        | author orphan signal rows with no role ground truth | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05+F-06+F-07; re-run Phases 2–4 |
| 2     | Signal Plan     | Signal table + rationale | COMMITMENT BLOCK: F-01–F-07 + COV-01–COV-04 each PASS        | produce malformed strategy unusable as commit gate  | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md       |
| 3     | Commit Gate     | Gate definition block    | COMMITMENT BLOCK: ≥ 1 essential named; block is structurally isolated | ship feature with no enforced readiness condition | → IR-03              | Re-run Phase 3; re-write commit gate section               |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | COMMITMENT BLOCK: both files at correct paths; F-04 verified  | topic unregistered; strategy unreachable            | → IR-04                | Re-write both artifacts; re-run path verification          |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: INERTIA REGISTER confirmed read (Stakeholder Most Harmed column included). STAKEHOLDER SCHEMA SK-01–SK-04 confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**COMMITMENT BLOCK — Phase 1 Exit**

> Author this block completely before advancing to Phase 2. Each field is an independent authorship act. Do not advance if any Status is FAIL.

```
COMMITMENT BLOCK: Phase 1 — Stakeholder Map

Row count (constraint: SK-01–SK-04, minimum 3):
  Observed: ___
  Status: PASS / FAIL

All four columns populated in every filled row (constraint: SK-01, SK-02, SK-03, SK-04):
  Observed: ___
  Status: PASS / FAIL

IR-01 override active (default: "Skip stakeholder mapping..."):
  Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth"
  Override confirmed: PASS / FAIL

IR-05 override active (default: "Assign all signals to a single generic owner role..."):
  Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses"
  Override confirmed: PASS / FAIL

Advance to Phase 2: YES only when all four Status fields above are PASS
```

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02.** IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
>
> Field constraints: F-01 through F-07. Coverage constraints: COV-01 through COV-04.
> No additional constraint statements apply outside those schemas.

**Entry gate**: Phase 1 COMMITMENT BLOCK all PASS AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here]

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**COMMITMENT BLOCK — Phase 2 Exit**

> Author this block completely before advancing to Phase 3. Each field is an independent authorship act.

```
COMMITMENT BLOCK: Phase 2 — Signal Plan

F-01 Priority vocabulary valid — values are essential / recommended / optional only:
  Observed values: ___
  Status: PASS / FAIL

F-02 Namespace values valid (see F-02):
  Status: PASS / FAIL

F-03 Skill values valid (see F-03):
  Status: PASS / FAIL

F-04 Item names follow {topic}-{signal}-{date}.md (see F-04):
  Status: PASS / FAIL

F-05 Consumer values appear verbatim in Phase 1 SK-02 column (see F-05):
  Observed Consumer values: ___
  Phase 1 SK-02 values: ___
  Status: PASS / FAIL

F-06 Stakeholder Ref values cite S-NN from Phase 1 (see F-06):
  Status: PASS / FAIL

F-07 Team Default values cite IR-NN (see F-07):
  Status: PASS / FAIL

COV-01 Essential signal count ≥ 1 (see COV-01):
  Observed count: ___
  Status: PASS / FAIL

COV-02 Distinct namespace count ≥ 2 (see COV-02):
  Observed count: ___
  Status: PASS / FAIL

COV-03 Distinct Producer role count ≥ 2 (see COV-03):
  Observed count: ___
  Status: PASS / FAIL

COV-04 Narrative rationale present ≥ 2 sentences (see COV-04):
  Status: PASS / FAIL

IR-02 override active (default: "Use 'high/medium/low' priority vocabulary..."):
  Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority"
  Override confirmed: PASS / FAIL

IR-05 override active (default: "Assign all signals to a single generic owner role..."):
  Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses"
  Override confirmed: PASS / FAIL

Advance to Phase 3: YES only when all Status fields above are PASS
```

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
>
> Coverage constraint: see COV-01 in COVERAGE SCHEMA. No additional constraints apply outside schemas.

**Entry gate**: Phase 2 COMMITMENT BLOCK all PASS AND signal table handoff artifact present. [ ]

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

**COMMITMENT BLOCK — Phase 3 Exit**

```
COMMITMENT BLOCK: Phase 3 — Commit Gate

Commit gate block written:
  Status: PASS / FAIL

Essential signal count in gate ≥ 1 (see COV-01):
  Observed count: ___
  Status: PASS / FAIL

Gate occupies structurally isolated block (not embedded in Phase 2):
  Status: PASS / FAIL

IR-03 override active (default: "Collapse commit gate into signal plan section..."):
  Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time"
  Override confirmed: PASS / FAIL

Advance to Phase 4: YES only when all Status fields above are PASS
```

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
>
> Path constraints: C-01, C-02. Item name constraint: see F-04.

**Entry gate**: Phase 3 COMMITMENT BLOCK all PASS AND commit gate block present. [ ]

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
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see pre-pipeline INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**COMMITMENT BLOCK — Phase 4 Exit**

```
COMMITMENT BLOCK: Phase 4 — Artifact Write

simulations/TOPICS.md row appended (see C-01):
  Status: PASS / FAIL

simulations/{TOPIC}/strategy.md written at correct path (see C-02):
  Status: PASS / FAIL

All item names in strategy.md follow F-04 convention (see F-04):
  Status: PASS / FAIL

IR-04 override active (default: "Omit artifact naming convention; use freeform item names..."):
  Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools"
  Override confirmed: PASS / FAIL

Phase 4 complete: YES only when all Status fields above are PASS
```
```

---

---

## V-05 — V-01 + PCR-NN + PRIORITY SCHEMA + COMMITMENT BLOCK (Maximum Integration)

**Axis**: All three new axes combined — PIPELINE CONSEQUENCE REGISTER (V-02) + PRIORITY SCHEMA isolation (V-03) + COMMITMENT BLOCK gate topology (V-04) — applied on the V-01 combined baseline.
**Hypothesis**: Five pre-pipeline blocks (INERTIA REGISTER, PIPELINE CONSEQUENCE REGISTER, PRIORITY SCHEMA, STAKEHOLDER SCHEMA, FIELD SCHEMA, COVERAGE SCHEMA) cover every category of named reference: team behavioral defaults (IR-NN), phase skip consequences (PCR-NN), priority vocabulary (P-NN), stakeholder column constraints (SK-NN), signal field constraints (F-NN), and coverage constraints (COV-NN). Phase bodies contain only block-ID references and COMMITMENT BLOCK fill-in slots. No prose that can drift exists outside a named block with a stable ID. COMMITMENT BLOCK gates require active authorship of every constraint state. This is the maximum-registry architecture — tests whether saturating pre-pipeline reference coverage produces the most consistent criterion compliance across all 38 v14 criteria.
**Key Structural Difference from V-01**: Six pre-pipeline reference blocks; priority vocabulary isolated to P-01/P-02/P-03; skip costs in PCR-01–PCR-04; all exit gates are COMMITMENT BLOCKs; zero prose in phase bodies that could drift from any block definition.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read before pipeline overview.
> "Stakeholder Most Harmed" names who suffers when the default is not overridden.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed                                                  |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth                        |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority          |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time        |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools                 |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## PIPELINE CONSEQUENCE REGISTER

> Pre-pipeline. Stable PCR-NN IDs. Read before pipeline overview.
> Names what breaks when each phase is skipped.
> Pipeline overview "If Skipped" column cites PCR-NN by ID.

| ID     | Phase Skipped | Consequence                                                                                                       | Who Bears the Cost                |
|--------|---------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| PCR-01 | Phase 1       | Signal rows authored with no stakeholder basis; F-05 Consumer and F-06 Stakeholder Ref orphaned; COV-03 unachievable without rework | Product Manager, Engineering Lead |
| PCR-02 | Phase 2       | Strategy produced without valid priority vocabulary or cross-functional ownership; cannot serve as commit gate    | Design Lead, cross-functional team |
| PCR-03 | Phase 3       | No enforced readiness condition at design commit; feature can ship without any evidence gate                      | Engineering Lead                  |
| PCR-04 | Phase 4       | Topic not registered; strategy.md absent or at wrong path; downstream tools cannot locate signals                 | All consumers                     |

---

## PRIORITY SCHEMA

> Valid vocabulary registry for the F-01 Priority field. P-NN row order = decision-state severity.
> SOLE source of priority vocabulary definitions.
> Do not restate priority vocabulary or decision-state anchors outside this block.

| ID   | Value       | Decision-State Anchor                                                                             | If Used Incorrectly                                                                       | Downstream Effect                                                        |
|------|-------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| P-01 | essential   | Consumer cannot make this decision without this signal — decision is blocked until signal exists  | Non-blocking signal gated as essential; commit blocked on unnecessary evidence           | Velocity loss with no quality gain; team blocks commit on enrichment     |
| P-02 | recommended | Consumer can decide without this signal but accepts increased exposure — quality risk accepted     | Recommended signal omitted; consumer decides blind on a quality dimension                | Decision made with unacceptable gap; defect surfaces post-commit         |
| P-03 | optional    | Consumer decides unaffected — signal is supplementary enrichment only                             | Optional enrichment marked essential; commit gate unnecessarily broad                    | Same as P-01 downstream; commit gated on supplementary signal            |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for Phase 1. SK-NN row order = column order.
> SOLE source of Phase 1 column constraints. No inline prose constraint restatements in Phase 1 body.

| ID    | Column Name         | Constraint                                                              | Immediate Failure                            | Downstream Effect                                              |
|-------|---------------------|-------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                          | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row           |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user" | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for the signal |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm       | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible    |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                  | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance                  |

---

## FIELD SCHEMA

> Column constraint registry for Phase 2 signal table. F-01 leftmost. Fill left to right.
> SOLE source of Phase 2 column constraints. No inline prose constraint restatements in Phase 2 body.
> F-01 vocabulary defined in PRIORITY SCHEMA; see P-01/P-02/P-03 for valid values.

| ID   | Field               | Constraint                                                               | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|--------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | See PRIORITY SCHEMA (P-01 / P-02 / P-03) — no other values valid        | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness  |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic         | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                              | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form     | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer verbatim as SK-02         | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                   | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role          | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

---

## COVERAGE SCHEMA

> Coverage constraint registry for Phase 2 aggregate.
> SOLE source of Phase 2 coverage constraints. No inline prose coverage restatements in Phase 2 body.

| ID     | Constraint                     | Minimum       | Immediate Failure                            | Downstream Effect                                          |
|--------|--------------------------------|---------------|----------------------------------------------|------------------------------------------------------------|
| COV-01 | Signals marked essential       | ≥ 1           | No commit gate definable                     | Feature ships without evidence gate; design commit ungated |
| COV-02 | Distinct namespaces            | ≥ 2           | Single-namespace plan; structural blind spot | Namespace gap analysis cannot detect coverage holes        |
| COV-03 | Distinct Producer roles (F-05) | ≥ 2           | Single-owner strategy; collapses on change   | Cross-functional gaps invisible; strategy untrustworthy    |
| COV-04 | Narrative rationale            | ≥ 2 sentences | Decision context absent                      | Topic purpose lost; signal relevance unverifiable          |

---

## PIPELINE OVERVIEW

> **READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1.**
> All exit gate conditions, handoff artifacts, and skip costs are declared here.
> Do not begin Phase 1 until you have read every row of this table.

| Phase | Purpose         | Handoff Artifact         | Exit Gate (summary)                                           | If Skipped (→ PCR-NN) | Team Default (→ IR-NN) | Recovery Cost If Caught Late                               |
|-------|-----------------|--------------------------|---------------------------------------------------------------|-----------------------|------------------------|------------------------------------------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)       | COMMITMENT BLOCK: row count ≥ 3 AND cols complete             | → PCR-01              | → IR-01, IR-05         | Re-run Phase 1; re-derive F-05+F-06+F-07; re-run Phases 2–4 |
| 2     | Signal Plan     | Signal table + rationale | COMMITMENT BLOCK: F-01–F-07 + COV-01–COV-04 all PASS         | → PCR-02              | → IR-02, IR-05         | Re-run Phase 2; re-run Phase 3; re-write strategy.md       |
| 3     | Commit Gate     | Gate definition block    | COMMITMENT BLOCK: ≥ 1 essential named; block structurally isolated | → PCR-03          | → IR-03                | Re-run Phase 3; re-write commit gate section               |
| 4     | Artifact Write  | TOPICS.md + strategy.md  | COMMITMENT BLOCK: both files correct paths; F-04 verified     | → PCR-04              | → IR-04                | Re-write both artifacts; re-run path verification          |

---

## PHASE 1 — STAKEHOLDER MAP

> **This phase overrides IR-01.** IR-01 Stakeholder Most Harmed: **Product Manager — loses commit-scope ground truth.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
> Skipping activates → PCR-01.
>
> Column constraints: SK-01 through SK-04. No additional column constraints apply outside STAKEHOLDER SCHEMA.

**Entry gate**: All six pre-pipeline blocks confirmed read. [ ]

Fill in the table below. Constraint for each column: see SK-NN in STAKEHOLDER SCHEMA.

| SK-01: Row ID | SK-02: Decision-Maker Role | SK-03: Risk Exposure | SK-04: Decision Informed |
|---------------|---------------------------|----------------------|--------------------------|
| S-01          |                           |                      |                          |
| S-02          |                           |                      |                          |
| S-03          |                           |                      |                          |
| S-NN          | (add rows as needed)      |                      |                          |

**COMMITMENT BLOCK — Phase 1 Exit**

```
COMMITMENT BLOCK: Phase 1 — Stakeholder Map

Row count (see SK-01–SK-04, minimum 3):
  Observed: ___
  Status: PASS / FAIL

All four columns populated in every filled row (see SK-01, SK-02, SK-03, SK-04):
  Observed: ___
  Status: PASS / FAIL

IR-01 override active — Default: "Skip stakeholder mapping; author signals from feature intuition.":
  Stakeholder Most Harmed: "Product Manager — loses commit-scope ground truth"
  Override confirmed: PASS / FAIL

IR-05 override active — Default: "Assign all signals to a single generic owner role.":
  Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses"
  Override confirmed: PASS / FAIL

PCR-01 consequence avoided — "Signal rows authored with no stakeholder basis; F-05 Consumer and F-06 Stakeholder Ref orphaned":
  Consequence avoided: PASS / FAIL

Advance to Phase 2: YES only when all five Status fields above are PASS
```

---

## PHASE 2 — SIGNAL PLAN

> **This phase overrides IR-02.** IR-02 Stakeholder Most Harmed: **Design Lead — cannot gate design commit on unparseable priority.**
> **This phase overrides IR-05.** IR-05 Stakeholder Most Harmed: **Cross-functional team — coverage gaps invisible when ownership collapses.**
> Skipping activates → PCR-02.
>
> Priority vocabulary: see PRIORITY SCHEMA (P-01/P-02/P-03). Field constraints: F-01–F-07. Coverage constraints: COV-01–COV-04.
> No additional constraint statements apply outside those blocks.

**Entry gate**: Phase 1 COMMITMENT BLOCK all PASS AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA. No additional instructions apply.

[Model fills here]

### SIGNAL TABLE

> Column order = FIELD SCHEMA row order. F-01 (Priority) is leftmost. Fill left to right.
> Priority values: P-01 = essential, P-02 = recommended, P-03 = optional (see PRIORITY SCHEMA).
> Constraint for each column: see F-NN in FIELD SCHEMA.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Producer → Consumer (F-05) | Stakeholder Ref (F-06) | Team Default (F-07) |
|-----------------|------------------|--------------|------------------|---------------------------|------------------------|---------------------|
|                 |                  |              |                  |                           |                        |                     |

**COMMITMENT BLOCK — Phase 2 Exit**

```
COMMITMENT BLOCK: Phase 2 — Signal Plan

F-01 / PRIORITY SCHEMA: Priority values are P-01/P-02/P-03 only (see F-01, PRIORITY SCHEMA):
  Observed values: ___
  Status: PASS / FAIL

F-02 Namespace values valid (see F-02):
  Status: PASS / FAIL

F-03 Skill values valid (see F-03):
  Status: PASS / FAIL

F-04 Item names follow {topic}-{signal}-{date}.md (see F-04):
  Status: PASS / FAIL

F-05 Consumer values appear verbatim in Phase 1 SK-02 column (see F-05):
  Observed Consumer values: ___
  Phase 1 SK-02 values: ___
  Status: PASS / FAIL

F-06 Stakeholder Ref values cite S-NN from Phase 1 (see F-06):
  Status: PASS / FAIL

F-07 Team Default values cite IR-NN (see F-07):
  Status: PASS / FAIL

COV-01 Essential signal count ≥ 1 (see COV-01):
  Observed count: ___
  Status: PASS / FAIL

COV-02 Distinct namespace count ≥ 2 (see COV-02):
  Observed count: ___
  Status: PASS / FAIL

COV-03 Distinct Producer role count ≥ 2 (see COV-03):
  Observed count: ___
  Status: PASS / FAIL

COV-04 Narrative rationale present ≥ 2 sentences (see COV-04):
  Status: PASS / FAIL

IR-02 override active — Default: "Use 'high/medium/low' priority vocabulary...":
  Stakeholder Most Harmed: "Design Lead — cannot gate design commit on unparseable priority"
  Override confirmed: PASS / FAIL

IR-05 override active — Default: "Assign all signals to a single generic owner role.":
  Stakeholder Most Harmed: "Cross-functional team — coverage gaps invisible when ownership collapses"
  Override confirmed: PASS / FAIL

PCR-02 consequence avoided — "Strategy produced without valid priority vocabulary or cross-functional ownership":
  Consequence avoided: PASS / FAIL

Advance to Phase 3: YES only when all Status fields above are PASS
```

---

## PHASE 3 — COMMIT GATE

> **This phase overrides IR-03.** IR-03 Stakeholder Most Harmed: **Engineering Lead — no enforced readiness condition at commit time.**
> Skipping activates → PCR-03.
>
> Coverage constraint: see COV-01. Essential vocabulary: see P-01 in PRIORITY SCHEMA. No additional constraints apply outside blocks.

**Entry gate**: Phase 2 COMMITMENT BLOCK all PASS AND signal table handoff artifact present. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (P-01 essential — see PRIORITY SCHEMA P-01, COV-01):
  1. [item name from P-01 row]
  2. [additional P-01 rows if any]

PERMITTED AFTER COMMIT (P-02 recommended / P-03 optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**COMMITMENT BLOCK — Phase 3 Exit**

```
COMMITMENT BLOCK: Phase 3 — Commit Gate

Commit gate block written:
  Status: PASS / FAIL

P-01 essential signal count in gate ≥ 1 (see P-01, COV-01):
  Observed count: ___
  Status: PASS / FAIL

Gate occupies structurally isolated block separate from Phase 2:
  Status: PASS / FAIL

IR-03 override active — Default: "Collapse commit gate into signal plan section...":
  Stakeholder Most Harmed: "Engineering Lead — no enforced readiness condition at commit time"
  Override confirmed: PASS / FAIL

PCR-03 consequence avoided — "No enforced readiness condition at design commit; feature can ship without any evidence gate":
  Consequence avoided: PASS / FAIL

Advance to Phase 4: YES only when all five Status fields above are PASS
```

---

## PHASE 4 — ARTIFACT WRITE

> **This phase overrides IR-04.** IR-04 Stakeholder Most Harmed: **All consumers — strategy unreachable by path-based tools.**
> Skipping activates → PCR-04.
>
> Path constraints: C-01, C-02. Item name constraint: see F-04.

**Entry gate**: Phase 3 COMMITMENT BLOCK all PASS AND commit gate block present. [ ]

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
IR-01 | IR-02 | IR-03 | IR-04 | IR-05 (see pre-pipeline INERTIA REGISTER)

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**COMMITMENT BLOCK — Phase 4 Exit**

```
COMMITMENT BLOCK: Phase 4 — Artifact Write

simulations/TOPICS.md row appended (see C-01):
  Status: PASS / FAIL

simulations/{TOPIC}/strategy.md written at correct path (see C-02):
  Status: PASS / FAIL

All item names in strategy.md follow F-04 convention (see F-04):
  Status: PASS / FAIL

Priority values in strategy.md match PRIORITY SCHEMA vocabulary (see P-01/P-02/P-03):
  Status: PASS / FAIL

IR-04 override active — Default: "Omit artifact naming convention; use freeform item names.":
  Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools"
  Override confirmed: PASS / FAIL

PCR-04 consequence avoided — "Topic not registered; strategy.md absent or at wrong path":
  Consequence avoided: PASS / FAIL

Phase 4 complete: YES only when all six Status fields above are PASS
```
```
