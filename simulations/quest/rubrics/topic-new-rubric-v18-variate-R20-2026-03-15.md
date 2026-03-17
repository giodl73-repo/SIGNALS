# topic-new — Round 20 Variations (V-01 through V-05)
# Rubric target: v18 (51 aspirational criteria, denominator 51)
# Date: 2026-03-15

---

## R20 Design Notes

R19 V-05 is the full-integration baseline for this round. It satisfied all 49 criteria through
C-57. Two new criteria extracted from R19 V-04/V-05 excellence signals:

- **C-58**: OVERRIDE MISSION table maps each IR-NN ID to its override **instrument class**
  (schema / gate / exit condition) — controlled vocabulary that converts the enumeration from
  a flat list into a navigable two-column mapping before the INERTIA REGISTER is encountered.
- **C-59**: PCR **header** carries a present-tense auditability assertion — "FER coverage is
  auditable by structural inspection of this table, not by content inference" — declaring the
  property as a table-level structural fact rather than an implicit consequence of row content.

**R19 baseline gap analysis**:

- **C-59**: R19 V-05 **already satisfies** C-59 — its PCR header includes the exact phrase
  "FER coverage is auditable by structural inspection of this table, not by content inference."
  R19 V-01 through V-04 do NOT satisfy C-59. V-04 used prohibition form ("Silent omission is
  not permitted") — a requirement, not a structural-property declaration.
- **C-58**: No R19 variation satisfies C-58. R19 V-04 and V-05 OVERRIDE MISSION tables both
  map IR-NN to prose descriptions ("What This Skill Overrides It With") rather than to
  instrument classes. C-58 requires the controlled vocabulary (schema / gate / exit condition)
  as the mapping target — so the column heading and values must be from that vocabulary, not
  from free-form override descriptions.

**Instrument class mapping** (used in V-01, V-03, V-04, V-05):

| IR-NN | Override Instrument Class |
|-------|--------------------------|
| IR-01 | gate — Phase 1 exit gate |
| IR-02 | schema — FIELD SCHEMA F-01 |
| IR-03 | gate — Phase 3 structural isolation |
| IR-04 | schema — FIELD SCHEMA F-04 |
| IR-05 | schema — COVERAGE SCHEMA COV-03 |

**Primary R20 structural challenge — C-58**: whether the instrument-class column REPLACES
the description column (two-column instrument-class-only map) or SUPPLEMENTS it (three-column
map: IR-NN | description | instrument class). V-01 and V-04 test the replace form; V-03 and
V-05 test the supplement form. V-02 isolates C-59 without C-58.

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Inertia framing — C-58 only: instrument-class column replaces description column, R19 V-01 minimal base (no BEFORE/AFTER, no PCR FER citations, no C-59) | The instrument-class column converts the OVERRIDE MISSION table from a prose-description map to a pure IR-NN-to-instrument-class map. Tests whether controlled-vocabulary instrument-class column alone (no description of what the override does) produces navigable register-reading on a minimal base. C-59 absent — PCR header stays at basic form. |
| V-02 | Output format — C-59 only: PCR header upgrades prohibition form to auditability declaration, R19 V-04 base (OVERRIDE MISSION with description table, BEFORE/AFTER FER, exhaustive PCR FER, no C-58) | R19 V-04's PCR header used prohibition form: "Silent omission is not permitted." C-59's declaration form asserts: "FER coverage is auditable by structural inspection of this table, not by content inference." Tests whether the distinction between a requirement the table must satisfy and a structural property the table asserts produces a compliance shift at the consequence-registry layer, without any C-58 instrument-class change. |
| V-03 | Phrasing register — C-58 as third column supplementing the existing description column (three-column OVERRIDE MISSION table), on R19 V-05 base (all 49 criteria, C-59 already present) | R19 V-05 had a description column. C-58 adds an instrument-class column as a THIRD column rather than replacing the description. Tests whether the combined three-column form (IR-NN | description | instrument class) provides stronger navigability than the two-column instrument-class-only form in V-01/V-04, by preserving the narrative "why" alongside the structural "how." |
| V-04 | Combined — C-58 (replace form) + C-59 (auditability declaration) on R19 V-04 base (command register + BEFORE/AFTER) | Apply both new criteria to R19 V-04: C-58 replaces description column with instrument-class-only column; C-59 upgrades PCR header from prohibition to declaration form. Tests whether both endpoint changes — instrument-class map at document opener and auditability assertion at consequence registry — compound coherently on command-register + BEFORE/AFTER base without full V-05 integration. |
| V-05 | Full integration — all 51 criteria: R19 V-05 + C-58 (three-column supplement form) + C-59 (already present in R19 V-05) | R19 V-05 already satisfies C-59. C-58 is the only addition: add Override Instrument Class column to the existing OVERRIDE MISSION table. Three-column form (IR-NN | description | instrument class) satisfies C-49 (purpose frame via description), C-56 (enumeration sentence), and C-58 (instrument-class map). Full 51-criterion activation. |

---

---

## V-01 — C-58 Instrument-Class Map Only (minimal base)

**Axis**: Inertia framing — replace OVERRIDE MISSION description column with instrument-class
column (controlled vocabulary: schema / gate / exit condition). Base: R19 V-01
(OVERRIDE MISSION present, command register, simple FER without BEFORE/AFTER, PCR with no
FER citations). No C-59 (PCR header stays at basic form).

**Hypothesis**: R19 V-04/V-05 mapped IR-NN to prose descriptions of what the override does
("Phase 1 — mandatory fill-in table with exit gate"). C-58 requires mapping to the instrument
class that enforces the override (gate / schema / exit condition) — controlled vocabulary.
The distinction: a description tells the model what the override produces; an instrument class
tells the model what structural mechanism enforces it. A model that reads "IR-02 → schema
(FIELD SCHEMA F-01)" before encountering the INERTIA REGISTER enters with a structural map,
not a narrative summary. Tests whether the instrument-class-only form (no description column)
produces a measurable reading-register shift on a minimal base without BEFORE/AFTER or PCR FER
enrichment.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## OVERRIDE MISSION

> **Read this block before reading any schema, phase, or gate.**

The defaults being overridden by this skill: **IR-01, IR-02, IR-03, IR-04, IR-05**.
Every block that follows exists to prevent these defaults from applying.

| Default (IR-NN) | Override Instrument Class |
|-----------------|--------------------------|
| IR-01: Skip stakeholder mapping | gate — Phase 1 exit gate |
| IR-02: Use high/medium/low priority | schema — FIELD SCHEMA F-01 |
| IR-03: Collapse commit gate into signal plan | gate — Phase 3 structural isolation |
| IR-04: Use freeform item names | schema — FIELD SCHEMA F-04 |
| IR-05: Single generic owner role | schema — COVERAGE SCHEMA COV-03 |

A model that applies its defaults is the failure mode this skill exists to prevent.

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

| ID     | Phase | Output You Accepted (sequential — THIS IS WRONG)                                                       | What Independent Checking Catches                                                                                            |
|--------|-------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| FER-01 | 1     | "Output you accepted: 'S-01 \| Product Manager \| \| ' — SK-03 and SK-04 empty on all rows. This output is malformed." | Row-count check (≥ 3) passes; column-completeness check reveals SK-03 and SK-04 empty on every row — sequential checking called this compliant |
| FER-02 | 2     | "Output you accepted: signal table with 4 rows; Priority column reads 'high / medium / low'. This output is malformed." | Row-count check passes; priority-vocabulary check reveals F-01 violation — "high" is not in {essential/recommended/optional} |

---

## PHASE CONSEQUENCE REGISTRY

> Pre-pipeline. Stable PCR-NN IDs. Defines the consequence of bypassing each pipeline phase.
> Pipeline overview consequence column cites PCR-NN IDs only.
> Do not embed consequence prose in the overview table.

| ID     | Phase Skipped | Consequence                                                                                        |
|--------|---------------|----------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated   |
| PCR-04 | Phase 4       | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools           |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                           |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row        |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal  |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance               |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                              | Decision-State Anchor                                                                                                        | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                     | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                        | —                                                                                                                            | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                             | —                                                                                                                            | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                    | —                                                                                                                            | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1 | —                                                                                                                            | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                  | —                                                                                                                            | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                         | —                                                                                                                            | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

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

| Phase | Purpose         | Handoff Artifact        | Exit Gate (summary)                                                       | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|-------------------------|---------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)      | SK-01–SK-04; row count AND column completeness independently (see FER-01) | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table                       | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block   | Gate names ≥ 1 essential; structurally isolated from Phase 2              | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md | Both files at correct paths; item names follow F-04                       | → PCR-04               | → IR-04                |

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
> by sequential checking and rejected by independent checking. FER-01 shows the exact output
> state in second-person form: "Output you accepted: 'S-01 | Product Manager | | '."

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

## V-02 — C-59 Auditability Declaration Only (R19 V-04 base)

**Axis**: Output format — upgrade PCR header from prohibition form ("Silent omission is not
permitted") to present-tense auditability declaration ("FER coverage is auditable by structural
inspection of this table, not by content inference"). Base: R19 V-04 (OVERRIDE MISSION with
IR-NN enumeration sentence + description table, command register, BEFORE/AFTER FER, exhaustive
PCR FER declarations). No C-58 — OVERRIDE MISSION table keeps description column.

**Hypothesis**: R19 V-04's PCR header used prohibition form — it named a violation as not
permitted but did not declare the table's structural property. C-59 requires a present-tense
assertion: "FER coverage IS auditable by structural inspection of this table, not by content
inference." This converts the auditability from a requirement the table must satisfy (inferred
by a reviewer checking each row) to a structural property the table asserts (verifiable by
header declaration alone). Tests whether the declaration form closes the auditability-claim
gap at the consequence-registry layer without any instrument-class change at the opener.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## OVERRIDE MISSION

> **Read this block before reading any schema, phase, or gate.**

The defaults being overridden by this skill: **IR-01, IR-02, IR-03, IR-04, IR-05**.
Every block that follows exists to prevent these defaults from applying.

| Default (IR-NN) | What This Skill Overrides It With |
|-----------------|-----------------------------------|
| IR-01: Skip stakeholder mapping | Phase 1 — mandatory stakeholder fill-in table with exit gate |
| IR-02: Use high/medium/low priority | Phase 2 — FIELD SCHEMA F-01 enforces {essential/recommended/optional} only |
| IR-03: Collapse commit gate into signal plan | Phase 3 — commit gate is its own structurally isolated phase |
| IR-04: Use freeform item names | Phase 4 — item names must follow `{topic}-{signal}-{date}.md` |
| IR-05: Single generic owner role | Phase 2 — COV-03 requires ≥ 2 distinct Producer roles |

A model that applies its defaults is the failure mode this skill exists to prevent.

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
> **FER coverage is auditable by structural inspection of this table, not by content
> inference. Every entry either cites a FER-NN ID (detectable output-state failure) or
> carries an explicit "No FER entry ([reason])" note (structural-absence failure). Silent
> omission is not permitted.**

| ID     | Phase Skipped | Consequence                                                                                                                                              |
|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence — failure is the missing phase boundary, not an inspectable output state). |
| PCR-04 | Phase 4       | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools. No FER entry (file-path verification — gate checks file existence at declared path, not table output state). |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                           |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row        |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal  |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance               |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                              | Decision-State Anchor                                                                                                        | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                     | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                        | —                                                                                                                            | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                             | —                                                                                                                            | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                    | —                                                                                                                            | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1 | —                                                                                                                            | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                  | —                                                                                                                            | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                         | —                                                                                                                            | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

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

| Phase | Purpose         | Handoff Artifact        | Exit Gate (summary)                                                                     | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)      | SK-01–SK-04; row count AND column completeness independently (see FER-01)               | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table (see FER-02)                        | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block   | Gate names ≥ 1 essential; structurally isolated from Phase 2                            | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md | Both files at correct paths; item names follow F-04                                     | → PCR-04               | → IR-04                |

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
> Match your output against FER-01 SEQUENTIAL PATH (wrong column): "Output you accepted:
> 'S-01 | Product Manager | | '" — SK-03/SK-04 empty on any row — correct before advancing.
> FER-01 INDEPENDENT PATH shows what valid output requires. PCR-01: skip failure recognizable
> by FER-01 output inspection.

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

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate expressed as a condition, not a list of aspirations. PCR-03: No FER entry (structural absence — failure is the missing phase boundary, not an inspectable output state).

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

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04. PCR-04: No FER entry (file-path verification — gate checks file existence at declared path, not table output state).

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-03 — C-58 as Third Column Supplementing Description (phrasing register, R19 V-05 base)

**Axis**: Phrasing register — add Override Instrument Class as a THIRD column to the existing
OVERRIDE MISSION table (keep description column). Base: R19 V-05 (all 49 criteria, C-59
already present in PCR header). The OVERRIDE MISSION becomes a three-column table: IR-NN |
What This Skill Overrides It With | Override Instrument Class.

**Hypothesis**: R19 V-04 and V-05 had a two-column description table. C-58 requires the
instrument-class mapping. V-01 tests replacing the description column; V-03 tests supplementing
it. The three-column form preserves the narrative "why" (description column, supporting C-49's
purpose frame) while adding the structural "how" (instrument-class column, satisfying C-58).
The hypothesis: the description column carries purpose-frame value (C-49 mechanism) that the
pure instrument-class table in V-01 loses; combining both columns serves both C-49 and C-58
simultaneously. A model reading the three-column table enters the INERTIA REGISTER with both
a purpose frame and a structural map, making the two additive rather than substitutable.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## OVERRIDE MISSION

> **Read this block before reading any schema, phase, or gate.**

These are the defaults this skill overrides: **IR-01, IR-02, IR-03, IR-04, IR-05**.
Every block that follows exists to prevent these defaults from applying.

| Default (IR-NN) | What This Skill Overrides It With | Override Instrument Class |
|-----------------|-----------------------------------|-----------------------------|
| IR-01: Skip stakeholder mapping | Phase 1 — mandatory stakeholder fill-in table with exit gate | gate — Phase 1 exit gate |
| IR-02: Use high/medium/low priority | Phase 2 — FIELD SCHEMA F-01 enforces {essential/recommended/optional} only | schema — FIELD SCHEMA F-01 |
| IR-03: Collapse commit gate into signal plan | Phase 3 — commit gate is its own structurally isolated phase | gate — Phase 3 structural isolation |
| IR-04: Use freeform item names | Phase 4 — item names must follow `{topic}-{signal}-{date}.md` | schema — FIELD SCHEMA F-04 |
| IR-05: Single generic owner role | Phase 2 — COV-03 requires ≥ 2 distinct Producer roles | schema — COVERAGE SCHEMA COV-03 |

A model that reads this document and applies its defaults is the failure mode this skill
exists to prevent. Every schema, every gate, and every exit condition in this document is
an override instrument.

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
> **Exhaustive FER coverage requirement: every entry must either (a) cite a FER-NN ID for
> detectable output-state failures, or (b) carry an explicit "No FER entry ([reason])" note
> for structural-absence failures. Silent omission is not permitted — FER coverage is
> auditable by structural inspection of this table, not by content inference.**

| ID     | Phase Skipped | Consequence                                                                                                                                              |
|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence — failure is the missing phase boundary, not an output-inspection state). |
| PCR-04 | Phase 4       | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools. No FER entry (file-path verification — gate checks file existence at declared path, not table output state). |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                           |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row        |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal  |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance               |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                              | Decision-State Anchor                                                                                                        | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                     | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                        | —                                                                                                                            | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                             | —                                                                                                                            | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                    | —                                                                                                                            | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1 | —                                                                                                                            | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                  | —                                                                                                                            | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                         | —                                                                                                                            | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

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

| Phase | Purpose         | Handoff Artifact        | Exit Gate (summary)                                                                     | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)      | SK-01–SK-04; row count AND column completeness independently (see FER-01)               | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table (see FER-02)                        | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block   | Gate names ≥ 1 essential; structurally isolated from Phase 2                            | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md | Both files at correct paths; item names follow F-04                                     | → PCR-04               | → IR-04                |

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
> valid output requires. PCR-01 consequence: skip failure recognizable by FER-01 output inspection.

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

---

## V-04 — Combined C-58 (replace form) + C-59 (R19 V-04 base)

**Axis**: Combined — instrument-class-only OVERRIDE MISSION table (C-58, replace form) plus
PCR header auditability declaration (C-59) on R19 V-04 base (command register, BEFORE/AFTER
FER, exhaustive PCR FER declarations, OVERRIDE MISSION with enumeration sentence).

**Hypothesis**: R19 V-04 had the enumeration sentence (C-56 satisfied) and the description
table (C-49 satisfied) and exhaustive PCR FER declarations (C-57 satisfied) but: (1) the
table mapped IR-NN to descriptions not instrument classes (C-58 gap), and (2) the PCR header
used prohibition form not declaration form (C-59 gap). V-04 applies both fixes simultaneously
on the command-register + BEFORE/AFTER base: the description column is REPLACED with an
instrument-class column (two-column table), and the PCR header is upgraded to the present-tense
auditability assertion. Tests whether both endpoint changes compound coherently on R19 V-04's
strong command-register base, or whether replacing the description column (losing the C-49
narrative purpose frame) creates a regression.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## OVERRIDE MISSION

> **Read this block before reading any schema, phase, or gate.**

The defaults being overridden by this skill: **IR-01, IR-02, IR-03, IR-04, IR-05**.
Every block that follows exists to prevent these defaults from applying.

| Default (IR-NN) | Override Instrument Class |
|-----------------|--------------------------|
| IR-01: Skip stakeholder mapping | gate — Phase 1 exit gate |
| IR-02: Use high/medium/low priority | schema — FIELD SCHEMA F-01 |
| IR-03: Collapse commit gate into signal plan | gate — Phase 3 structural isolation |
| IR-04: Use freeform item names | schema — FIELD SCHEMA F-04 |
| IR-05: Single generic owner role | schema — COVERAGE SCHEMA COV-03 |

A model that applies its defaults is the failure mode this skill exists to prevent.

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
> **FER coverage is auditable by structural inspection of this table, not by content
> inference. Every entry either cites a FER-NN ID (detectable output-state failure) or
> carries an explicit "No FER entry ([reason])" note (structural-absence failure). Silent
> omission is not permitted.**

| ID     | Phase Skipped | Consequence                                                                                                                                              |
|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence — failure is the missing phase boundary, not an inspectable output state). |
| PCR-04 | Phase 4       | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools. No FER entry (file-path verification — gate checks file existence at declared path, not table output state). |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                           |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row        |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal  |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance               |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                              | Decision-State Anchor                                                                                                        | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                     | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                        | —                                                                                                                            | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                             | —                                                                                                                            | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                    | —                                                                                                                            | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1 | —                                                                                                                            | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                  | —                                                                                                                            | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                         | —                                                                                                                            | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

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

| Phase | Purpose         | Handoff Artifact        | Exit Gate (summary)                                                                     | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)      | SK-01–SK-04; row count AND column completeness independently (see FER-01)               | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table (see FER-02)                        | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block   | Gate names ≥ 1 essential; structurally isolated from Phase 2                            | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md | Both files at correct paths; item names follow F-04                                     | → PCR-04               | → IR-04                |

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
> Match your output against FER-01 SEQUENTIAL PATH (wrong column): "Output you accepted:
> 'S-01 | Product Manager | | '" — SK-03/SK-04 empty on any row — correct before advancing.
> FER-01 INDEPENDENT PATH shows what valid output requires. PCR-01: skip failure recognizable
> by FER-01 output inspection.

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

**Exit gate**: Commit gate block written. ≥ 1 essential signal named (see COV-01). Gate expressed as a condition, not a list of aspirations. PCR-03: No FER entry (structural absence — failure is the missing phase boundary, not an inspectable output state).

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

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04. PCR-04: No FER entry (file-path verification — gate checks file existence at declared path, not table output state).

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```

---

---

## V-05 — Full Integration (all 51 criteria: R19 V-05 + C-58 three-column supplement)

**Axis**: Full integration — R19 V-05 (all 49 criteria, C-59 already present) with C-58 added
as a third "Override Instrument Class" column to the existing OVERRIDE MISSION table. The
three-column table (IR-NN | description | instrument class) satisfies C-49 (purpose frame via
description column), C-56 (enumeration sentence before the table), and C-58 (instrument-class
mapping). C-59 is carried forward unchanged from R19 V-05 (PCR header already contains "FER
coverage is auditable by structural inspection of this table, not by content inference.").

**Hypothesis**: R19 V-05 satisfied C-49 through C-57 plus C-59. The only gap is C-58: the
OVERRIDE MISSION table mapped IR-NN to prose descriptions but not to instrument classes.
Adding the instrument-class column as a third column — rather than replacing the description —
preserves C-49's purpose-frame value while simultaneously satisfying C-58's navigable-map
requirement. The three-column form is the structural completion of the OVERRIDE MISSION block:
enumeration sentence (C-56 forward index) + description column (C-49 purpose frame) +
instrument class column (C-58 structural map). A model reading the three-column OVERRIDE
MISSION block before the INERTIA REGISTER has: the closed list (C-56), the reason each default
is being overridden (C-49), and the enforcement mechanism class for each default (C-58). Full
51-criterion activation should produce a coherent, non-redundant prompt that scores
aspirational_pass / 51 at or near ceiling against the v18 denominator.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## OVERRIDE MISSION

> **Read this block before reading any schema, phase, or gate.**

These are the defaults this skill overrides: **IR-01, IR-02, IR-03, IR-04, IR-05**.
Every block that follows exists to prevent these defaults from applying.

| Default (IR-NN) | What This Skill Overrides It With | Override Instrument Class |
|-----------------|-----------------------------------|-----------------------------|
| IR-01: Skip stakeholder mapping | Phase 1 — mandatory stakeholder fill-in table with exit gate | gate — Phase 1 exit gate |
| IR-02: Use high/medium/low priority | Phase 2 — FIELD SCHEMA F-01 enforces {essential/recommended/optional} only | schema — FIELD SCHEMA F-01 |
| IR-03: Collapse commit gate into signal plan | Phase 3 — commit gate is its own structurally isolated phase | gate — Phase 3 structural isolation |
| IR-04: Use freeform item names | Phase 4 — item names must follow `{topic}-{signal}-{date}.md` | schema — FIELD SCHEMA F-04 |
| IR-05: Single generic owner role | Phase 2 — COV-03 requires ≥ 2 distinct Producer roles | schema — COVERAGE SCHEMA COV-03 |

A model that reads this document and applies its defaults is the failure mode this skill
exists to prevent. Every schema, every gate, and every exit condition in this document is
an override instrument.

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
> **Exhaustive FER coverage requirement: every entry must either (a) cite a FER-NN ID for
> detectable output-state failures, or (b) carry an explicit "No FER entry ([reason])" note
> for structural-absence failures. Silent omission is not permitted — FER coverage is
> auditable by structural inspection of this table, not by content inference.**

| ID     | Phase Skipped | Consequence                                                                                                                                              |
|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence — failure is the missing phase boundary, not an output-inspection state). |
| PCR-04 | Phase 4       | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools. No FER entry (file-path verification — gate checks file existence at declared path, not table output state). |

---

## STAKEHOLDER SCHEMA

> Column constraint registry for the Phase 1 fill-in table.
> SK-NN row order = column order in Phase 1 table.
> These rows are the SOLE source of Phase 1 column constraints.
> Phase 1 body contains no inline prose constraint restatements; cite SK-NN only.

| ID    | Column Name         | Constraint                                                               | Immediate Failure                            | Downstream Effect                                           |
|-------|---------------------|--------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------|
| SK-01 | Row ID              | Must be S-NN (S-01, S-02, ...)                                           | Row unaddressable; F-06 lookups break        | Phase 2 Stakeholder Ref cannot trace to Phase 1 row        |
| SK-02 | Decision-Maker Role | Named role accountable for a real decision; not "stakeholder" or "user"  | Anonymous row; cannot populate F-05 Consumer | Signal ownership undefined; nobody accountable for signal  |
| SK-03 | Risk Exposure       | What breaks for this role if the topic is skipped — specific harm        | Empty risk = no inclusion motivation         | Signal pruning has no ground truth; coverage gaps invisible |
| SK-04 | Decision Informed   | The concrete decision this topic provides evidence for                   | Row contributes no decision anchor           | Signal plan cannot be evaluated for relevance               |

---

## FIELD SCHEMA

> Column constraint registry for the Phase 2 signal table.
> F-NN row order = column order in signal table. F-01 is leftmost. Fill left to right.
> These rows are the SOLE source of Phase 2 column constraints.
> Phase 2 body contains no inline prose constraint restatements; cite F-NN only.

| ID   | Field               | Constraint                                                                              | Decision-State Anchor                                                                                                        | Immediate Failure                           | Downstream Effect                                                    |
|------|---------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority            | Must be exactly: essential / recommended / optional                                     | essential = consumer cannot decide without this; recommended = decides with increased exposure; optional = decides unaffected | Schema violation; strategy malformed        | Strategy unusable as commit gate; Design Lead cannot parse readiness |
| F-02 | Namespace           | One of: scout draft review flow trace prove listen program topic                        | —                                                                                                                            | Invalid namespace; routing fails            | Signal routed to wrong executor at runtime                           |
| F-03 | Skill               | Named skill existing under stated namespace                                             | —                                                                                                                            | Non-existent reference                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name           | `{topic}-{signal}-{date}.md` or parameterized template of that form                    | —                                                                                                                            | Format check fails; path unresolvable       | Strategy unreachable by path-based tools                             |
| F-05 | Producer → Consumer | `{producer-role} → {consumer-role}`; Consumer must appear verbatim as SK-02 in Phase 1 | —                                                                                                                            | Orphan consumer; traceability broken        | Ownership undefined; signals accumulate without accountability       |
| F-06 | Stakeholder Ref     | S-NN row ID from Phase 1 fill-in table                                                  | —                                                                                                                            | Orphan signal; no stakeholder basis         | Signal disconnected from risk motivation; pruning ungrounded         |
| F-07 | Team Default        | → IR-NN citing the inertia pattern for this signal's owner role                         | —                                                                                                                            | Unregistered default; not consultable by ID | Role's inertia pattern invisible at strategy review time             |

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

| Phase | Purpose         | Handoff Artifact        | Exit Gate (summary)                                                                     | Consequence If Skipped | Team Default (→ IR-NN) |
|-------|-----------------|-------------------------|-----------------------------------------------------------------------------------------|------------------------|------------------------|
| 1     | Stakeholder Map | S-table (≥ 3 rows)      | SK-01–SK-04; row count AND column completeness independently (see FER-01)               | → PCR-01               | → IR-01, IR-05         |
| 2     | Signal Plan     | Signal table + rationale | F-01–F-07 + COV-01–COV-04; Consumer traces S-table (see FER-02)                        | → PCR-02               | → IR-02, IR-05         |
| 3     | Commit Gate     | Gate definition block   | Gate names ≥ 1 essential; structurally isolated from Phase 2                            | → PCR-03               | → IR-03                |
| 4     | Artifact Write  | TOPICS.md + strategy.md | Both files at correct paths; item names follow F-04                                     | → PCR-04               | → IR-04                |

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
> valid output requires. PCR-01 consequence: skip failure recognizable by FER-01 output inspection.

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

## Criteria Coverage Map — R20

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-49: Opener declares override mission (purpose declaration) | YES | YES | YES | YES (instrument-class only — C-49 satisfied via enumeration sentence context) | YES |
| C-50: Pipeline read prohibition clause | YES | YES | YES | YES | YES |
| C-51: Stop. + Record both results at independence gate | YES | YES | YES | YES | YES |
| C-52: Second-person framing in FER | YES | YES | YES | YES | YES |
| C-53: Stop. command register at phase override directives | YES | YES | YES | YES | YES |
| C-54: BEFORE/AFTER comparison table in FER | — | YES | YES | YES | YES |
| C-55: PCR entries cross-cite FER-NN | — | YES | YES | YES | YES |
| C-56: Override mission enumerates IR-NN IDs (enumeration sentence) | YES | YES | YES | YES | YES |
| C-57: Every PCR entry cites FER-NN or carries explicit No-FER note | — | YES | YES | YES | YES |
| **C-58: Override mission table maps IR-NN to instrument class (schema/gate/exit condition)** | **YES** | **—** | **YES** | **YES** | **YES** |
| **C-59: PCR header carries present-tense auditability assertion** | **—** | **YES** | **YES** | **YES** | **YES** |
| New criteria count satisfied | C-58 only | C-59 only | C-58 + C-59 | C-58 + C-59 | C-58 + C-59 |
| Override mission form | two-column (instrument class only) | two-column (description only) | three-column (description + instrument class) | two-column (instrument class only) | three-column (description + instrument class) |
| PCR header form | basic | auditability declaration | auditability declaration (from V-05 base) | auditability declaration | auditability declaration (from V-05 base) |
| Base | R19 V-01 (minimal) | R19 V-04 | R19 V-05 | R19 V-04 | R19 V-05 |
