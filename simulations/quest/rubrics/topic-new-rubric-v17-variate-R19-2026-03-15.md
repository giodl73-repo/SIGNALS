# topic-new — Round 19 Variations (V-01 through V-05)
# Rubric target: v17 (49 aspirational criteria, denominator 49)
# Date: 2026-03-15

---

## R19 Design Notes

R18 V-05 is the full-integration baseline for this round. It satisfied all seven v16 criteria
(C-49 through C-55). Two new criteria extracted from R18 excellence signals:

- **C-56**: Override mission block enumerates the specific IR-NN IDs it introduces — compact
  closed list before the register is presented. Sharpens C-49.
- **C-57**: PCR FER coverage is exhaustively declared — every entry either cites FER-NN or
  carries an explicit "No FER entry ([reason])" note. Sharpens C-55.

**R18 V-05 gap analysis**:
R18 V-05 already satisfies C-57 — PCR-03 and PCR-04 carry explicit "No FER entry" notes.
R18 V-05 does NOT satisfy C-56 — the OVERRIDE MISSION table lists IR-NN IDs in rows but
does not produce a compact closed-list enumeration sentence before the register. The
distinction: a table row "IR-01: Skip stakeholder mapping | Phase 1 — ..." requires the
model to parse table columns to extract the ID list. A compact sentence "These are the
defaults this skill overrides: IR-01, IR-02, IR-03, IR-04, IR-05" delivers the closed list
in one sequence-read before any register is encountered.

The primary structural challenge for R19 is C-56: where does the closed-list enumeration
live, what form does it take, and whether inline-sentence vs. table-embedded enumeration
produces different reading-register effects.

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Inertia framing — IR-NN closed-list enumeration in OVERRIDE MISSION (C-56 only, R18 V-01 base) | Adding the compact "The defaults being overridden: IR-01, IR-02, IR-03, IR-04, IR-05" sentence plus a purpose-override table to R18 V-01's command-register structure; model enters INERTIA REGISTER with pre-declared closed set; tests whether forward index alone — no BEFORE/AFTER table, no PCR FER citations — shifts register-reading behavior |
| V-02 | Output format — exhaustive FER declaration in PCR (C-55 + C-57, R18 V-04 base) | Adding FER-01/FER-02 citations to PCR-01/PCR-02 and explicit "No FER entry ([reason])" notes to PCR-03/PCR-04 on R18 V-04's command-register + BEFORE/AFTER base; every PCR entry's FER status explicitly declared; tests whether exhaustive coverage declaration closes the scoping-ambiguity gap without the opener's purpose frame |
| V-03 | Phrasing register — C-56 as inline sentence only, no table (on V-05 baseline) | R18 V-05 had a purpose declaration + IR-NN table in OVERRIDE MISSION (C-49 satisfied); this variation implements C-56 as a compact inline sentence only — "These are the defaults this skill overrides: IR-01, IR-02, IR-03, IR-04, IR-05" — before the INERTIA REGISTER, with no OVERRIDE MISSION table; tests whether the minimal sentence form produces a stronger reading-register effect than the table-structured form in V-01/V-05 |
| V-04 | Combined — C-56 + C-55 + C-57 on command-register base (R18 V-04) | Apply both new criteria plus the PCR FER baseline (C-55) to R18 V-04, which has command register and BEFORE/AFTER table but neither OVERRIDE MISSION nor PCR FER citations; the OVERRIDE MISSION with enumeration simultaneously satisfies C-49 and C-56; the exhaustive PCR FER declaration simultaneously satisfies C-55 and C-57; tests whether both endpoint additions — document opener + consequence registry — compound on a command-register base |
| V-05 | Full integration — R18 V-05 + C-56 (inline + table form) + C-57 refinement (all 49 criteria) | R18 V-05 satisfied C-49 through C-55; C-56 adds the IR-NN closed-list sentence to the OVERRIDE MISSION that V-05 already had; C-57 adds an explicit PCR header requirement making exhaustive FER declaration structurally named; the reading-register effect of C-56 compounds with C-49's purpose frame, so the model enters INERTIA REGISTER with both why the document exists and exactly which defaults it will encounter |

---

---

## V-01 — C-56: IR-NN Forward Index in Override Mission

**Axis**: Inertia framing — add OVERRIDE MISSION with C-56 closed-list enumeration to R18 V-01
command-register base. C-49 purpose frame included. No BEFORE/AFTER table (retains narrative FER
format from V-01). No PCR FER cross-citations (no C-55, no C-57).

**Hypothesis**: R18 V-02 added a purpose-declaration OVERRIDE MISSION (C-49 only) with a table
of overrides. C-56 requires a compact IR-NN enumeration sentence — "The defaults being
overridden: IR-01, IR-02, IR-03, IR-04, IR-05" — before any schema content. This sentence
delivers a closed list in one read, so when the model encounters IR-01 through IR-05 in the
INERTIA REGISTER, each entry is expected and named rather than discovered by parsing. Tests
whether the compact forward-index sentence alone (without the full V-05 integration) produces
a measurable reading-register shift on a command-register base.

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

## V-02 — Exhaustive FER Declaration in PCR (C-55 + C-57)

**Axis**: Output format — add exhaustive PCR FER declaration to R18 V-04 base (command register
+ BEFORE/AFTER table, no OVERRIDE MISSION). PCR-01 and PCR-02 cite FER-NN (C-55). PCR-03 and
PCR-04 carry explicit "No FER entry ([reason])" notes (C-57). PCR header names exhaustive
coverage as a structural requirement. No OVERRIDE MISSION (no C-49, no C-56).

**Hypothesis**: R18 V-04 had command register and BEFORE/AFTER table but a PCR with no FER
treatment — PCR-03 and PCR-04 were silent on FER status. Silent omission is structurally
indistinguishable from a missing citation. C-57 requires every entry's FER status explicitly
declared. This variation adds: FER-01 citation on PCR-01, FER-02 citation on PCR-02,
"No FER entry (structural absence)" on PCR-03, "No FER entry (file-path verification)" on
PCR-04. Tests whether exhaustive FER coverage declaration alone — without the opener's
purpose frame — closes the consequence-detection gap at the PCR layer.

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
> **Every entry either cites a FER-NN ID (detectable output-state failure) or carries an
> explicit "No FER entry ([reason])" note (structural-absence failure). Silent omission
> is not permitted — FER coverage must be auditable by structural inspection.**

| ID     | Phase Skipped | Consequence                                                                                                                                              |
|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence — no isolated block to inspect; failure is absence of a phase boundary, not an output state). |
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

## V-03 — C-56 as Inline Sentence Only (phrasing register variant on V-05 base)

**Axis**: Phrasing register — implement C-56 as a single compact sentence before the INERTIA
REGISTER, with no OVERRIDE MISSION table. All other structure from R18 V-05 (all C-49 through
C-55 satisfied). C-57 inherited unchanged from R18 V-05.

**Hypothesis**: R18 V-05 satisfied C-49 with an OVERRIDE MISSION table listing IR-NN IDs in
table rows alongside descriptions. C-56 requires a forward index before the register — a closed
list the model can read in sequence before encountering any schema. A table row requires column
parsing to extract the ID; an inline sentence "These are the defaults this skill overrides:
IR-01, IR-02, IR-03, IR-04, IR-05" delivers the list in one read. This variation tests whether
the minimal sentence form — no table, no purpose-override column — produces a stronger
reading-register effect (closed-list loaded before register parsing begins) than V-01's
sentence-plus-table form or V-05's full OVERRIDE MISSION block. The hypothesis: if C-56's
mechanism is the closed-list pre-loading, the sentence form is sufficient and the table adds
no additional benefit to the forward-index function.

---

```
# topic-new — Register Topic and Plan Signals

You are executing the `topic-new` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

> **These are the defaults this skill overrides: IR-01, IR-02, IR-03, IR-04, IR-05.**
> Every block that follows exists to prevent these defaults from applying.
> A model that applies its defaults is the failure mode this skill exists to prevent.

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
> Each entry either cites a FER-NN ID or carries an explicit "No FER entry ([reason])" note.

| ID     | Phase Skipped | Consequence                                                                                                                                              |
|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCR-01 | Phase 1       | Signal rows carry no role ground truth; ownership collapses at assignment time; gap detection fails. Skip failure recognizable by FER-01 output inspection. |
| PCR-02 | Phase 2       | Priority vocabulary invalid; strategy unusable as commit gate; Design Lead cannot parse readiness. Skip failure recognizable by FER-02 output inspection.  |
| PCR-03 | Phase 3       | Commit gate implicit; Engineering Lead has no enforced readiness condition; feature ships ungated. No FER entry (structural absence, not output-state failure). |
| PCR-04 | Phase 4       | Topic unregistered in TOPICS.md; strategy at wrong path; unreachable by path-based tools. No FER entry (file-path check, not table-output inspection). |

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
> you must correct before advancing. FER-01 INDEPENDENT PATH shows what valid output requires.
> PCR-01: skip failure recognizable by FER-01 output inspection.

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

## V-04 — C-56 + C-55 + C-57 Combined (command-register base, R18 V-04)

**Axis**: Combined — OVERRIDE MISSION with IR-NN enumeration (C-56, also satisfies C-49) and
exhaustive PCR FER declaration (C-55 + C-57) on R18 V-04's command-register + BEFORE/AFTER
base. No OVERRIDE MISSION table was in V-04; PCR had no FER treatment. Both endpoint additions
applied together.

**Hypothesis**: C-56 closes the opener gap (closed-list forward index before the register) and
C-57 closes the terminal-layer gap (every PCR entry's FER status explicitly declared). These
two gaps are at opposite structural ends of the document: C-56 is the first block before any
schema; C-57 is the consequence registry. A prompt can satisfy C-56 without C-57 and vice
versa. V-04 tests whether activating both endpoints simultaneously on a command-register +
BEFORE/AFTER base (without the remaining V-05 additions) produces coherent integration, and
whether the opener-plus-registry combination produces a measurable compliance rate above either
single-axis fix alone.

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
> **Every entry either cites a FER-NN ID (detectable output-state failure) or carries an
> explicit "No FER entry ([reason])" note (structural-absence failure). Silent omission
> is not permitted.**

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

## V-05 — Full Integration (all 49 criteria: R18 V-05 + C-56 + C-57 refinement)

**Axis**: Full integration — R18 V-05 (all C-49 through C-55 satisfied) with C-56 added as a
compact enumeration sentence inside the OVERRIDE MISSION block, and C-57 reinforced via an
explicit PCR header requirement naming exhaustive FER declaration as a structural rule.

**Hypothesis**: R18 V-05 satisfied C-49 (purpose declaration) but not C-56 (closed-list forward
index with IR-NN IDs before the register). Adding "These are the defaults this skill overrides:
IR-01, IR-02, IR-03, IR-04, IR-05" as the first sentence of the OVERRIDE MISSION — before the
table — gives the model both a purpose frame (C-49: why the document exists) and a forward
index (C-56: exactly which defaults it will encounter). The two compound: C-49 sets the
reading register as anti-default; C-56 pre-loads the specific ID list so every INERTIA
REGISTER row is encountered as an expected named entry rather than a discovered one.
C-57 is already structurally present in R18 V-05 via PCR-03/04 "No FER entry" notes; this
variation adds a named requirement in the PCR header to make the exhaustive-coverage rule
explicit and auditable by structural inspection rather than discoverable only by reading
each PCR row. Tests whether full 49-criterion activation produces a coherent, non-redundant
prompt that scores near-perfect against the v17 denominator.

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

| Default (IR-NN) | What This Skill Overrides It With |
|-----------------|-----------------------------------|
| IR-01: Skip stakeholder mapping | Phase 1 — mandatory stakeholder fill-in table with exit gate |
| IR-02: Use high/medium/low priority | Phase 2 — FIELD SCHEMA F-01 enforces {essential/recommended/optional} only |
| IR-03: Collapse commit gate into signal plan | Phase 3 — commit gate is its own structurally isolated phase |
| IR-04: Use freeform item names | Phase 4 — item names must follow `{topic}-{signal}-{date}.md` |
| IR-05: Single generic owner role | Phase 2 — COV-03 requires ≥ 2 distinct Producer roles |

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

## Criteria Coverage Map — R19

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-49: Opener declares override mission (purpose declaration) | YES | — | YES (inherited from V-05) | YES | YES |
| C-50: Pipeline read prohibition clause | YES (inherited) | YES (inherited) | YES (inherited) | YES (inherited) | YES |
| C-51: Stop. + Record both results at independence gate | YES | YES | YES (inherited) | YES | YES |
| C-52: Second-person failure example ("Output you accepted:") | YES | YES | YES (inherited) | YES | YES |
| C-53: Stop. You are overriding IR-NN: at phase headers | YES | YES | YES (inherited) | YES | YES |
| C-54: BEFORE/AFTER failure table | — | YES | YES (inherited) | YES | YES |
| C-55: PCR entries cite FER-NN (detectable entries) | — | YES | YES (inherited) | YES | YES |
| C-56: Override mission enumerates specific IR-NN IDs (forward index) | YES | — | YES (inline sentence form) | YES | YES |
| C-57: PCR FER coverage exhaustively declared (no silent omissions) | — | YES | YES (inherited) | YES | YES |

Single-axis: V-01 targets C-56 (inertia framing — forward index). V-02 targets C-55+C-57 (output format — exhaustive FER coverage).
Phrasing variant: V-03 tests C-56 as inline-sentence-only (minimal form) vs V-01/V-05 sentence-plus-table form.
Combined: V-04 = C-56 + C-55 + C-57 (opener + registry endpoints on command-register base).
Full integration: V-05 = all C-49 through C-57 (all 49 criteria active).
