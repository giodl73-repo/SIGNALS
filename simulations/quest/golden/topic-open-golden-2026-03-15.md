# topic-new — QU5 Simplification — 2026-03-15
# Base: R20 V-05 (51/51 on v18 rubric, 52 criteria denominator with v19)
# Simplification: zero essential criteria lost, ~9-10% word reduction

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

---

## INERTIA REGISTER

> Pre-pipeline. Stable IR-NN IDs. Read this register before reading the pipeline overview.
> All phase directives and exit gates cite rows by IR-NN ID.

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

> Pre-pipeline. Stable PCR-NN IDs.
> Pipeline overview consequence column cites PCR-NN IDs only.
> Do not embed consequence prose in the overview table.
> **Exhaustive FER coverage requirement: every entry must either (a) cite a FER-NN ID for
> detectable output-state failures, or (b) carry an explicit "No FER entry ([reason])" note
> for structural-absence failures. FER coverage is auditable by structural inspection of
> this table, not by content inference.**

| ID     | Phase Skipped | Consequence                                                                                                                                              |
|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence — failure is the missing phase boundary, not an output-inspection state). |
| PCR-04 | Phase 4       | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools. No FER entry (file-path verification — gate checks file existence at declared path, not table output state). |

---

## STAKEHOLDER SCHEMA

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
> Column constraints: SK-01 through SK-04.

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
> Match your output against FER-01 SEQUENTIAL PATH (wrong column) before advancing. FER-01 INDEPENDENT PATH (correct column) shows what valid output requires.

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

**Entry gate**: Phase 1 exit gate cleared AND S-table handoff artifact present. [ ]

### NARRATIVE RATIONALE

> Fill-in step. Constraint: see COV-04 in COVERAGE SCHEMA.

[Model fills here — ≥ 2 sentences]

### PRE-WRITE GATE

> Cite schema rows by ID. Do not restate constraint text inline.

- [ ] F-01: Priority vocabulary
- [ ] F-02: Namespace values
- [ ] F-03: Skill values
- [ ] F-04: Item names
- [ ] F-05: Consumer values appear verbatim in Phase 1 SK-02 column
- [ ] F-06: Stakeholder Ref values cite S-NN rows from Phase 1
- [ ] F-07: Team Default values cite IR-NN
- [ ] COV-01: ≥ 1 essential signal
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct Producer roles
- [ ] COV-04: Narrative rationale present above

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
> Coverage constraint: see COV-01 in COVERAGE SCHEMA.

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

## Signal Plan
[paste Priority-first signal table from Phase 2]

## Commit Gate
[paste commit gate block from Phase 3]
```

**Exit gate**: Both files written at correct paths (see C-01, C-02). All item names follow F-04.

**IR-04 verbatim at exit**: Default: "Omit artifact naming convention; use freeform item names." Override active: Phase 4. Stakeholder Most Harmed: "All consumers — strategy unreachable by path-based tools."
```
