Writing V-01 through V-03 now. V-04 and V-05 follow in the next piece.

---

## R16 Variations — trace-migration (Rubric v14)
**Target**: C-42 (Three-Artifact Alignment Binding Statement) and C-43 (Conditional Return-to-Parse Gate on Row (a) Category Violation). Residual gap from R15: C-17 PARTIAL.

**Variation axes chosen:**
- Axis A — C-42: pre-Q1 named THREE-ARTIFACT SUBSTRATE ALIGNMENT block
- Axis B — C-43: named COST LEDGER SUBSTRATE GATE with conditional return instruction
- Axis C — C-17: "(BINARY FIELD)" annotation at ENTRY REFERENCE positions (not only EXIT BLOCK)

**Isolation design:**

| V | Axes | C-42 | C-43 | C-17 | Predicted |
|---|------|------|------|------|-----------|
| V-01 | A only | PASS (named block, names all 3 artifacts) | FAIL (negative constraint only, no return path) | PARTIAL (ENTRY REFERENCE lacks annotation) | ~250/265 |
| V-02 | B only | FAIL (B2 inline names 2 artifacts; no named block) | PASS (named gate block, conditional return) | PARTIAL | ~250/265 |
| V-03 | C only | FAIL | FAIL | PASS (annotation at all bilateral positions) | ~248/265 |
| V-04 | A + B | PASS | PASS | PARTIAL | ~258/265 |
| V-05 | A + B + C + D | PASS | PASS | PASS | ~265/265 |

---

## V-01 — Axis A: C-42 Three-Artifact Alignment Block (Pre-Q1)

**Variation axis**: A named THREE-ARTIFACT SUBSTRATE ALIGNMENT section is placed between STATUS QUO COST and ROLE ANALYSIS ENFORCEMENT. It explicitly names all three artifacts — COST LEDGER row (a), Phase A Q1 analytical domain, and B2 chain substrate — and mandates they name the same infrastructure condition before Q1 is written. C-43 is intentionally absent (only a negative categorical prohibition on row (a), no conditional return path). C-17 is PARTIAL.

**Hypothesis**: Pre-Q1 placement forces three-artifact alignment as a structural commit-before-analyze requirement. Prior variations achieved alignment as a B2 assertion; V-01 tests whether a pre-Q1 mandate (naming all three artifacts before the first analysis sentence is written) produces tighter three-artifact coherence and a clean C-42 PASS. C-43 FAIL isolates the axis: the return path adds no value here, only the named alignment mandate.

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A question. Available roles:

- **Operations Expert** — job queues, infrastructure metadata, monitoring tables, deployment scaffolding, schema version management
- **Commerce Expert** — order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** — ledger tables, transaction logs, audit trails, amount columns

---

## PARSE PHASE

### P0 — Migration Step Registry

Produce a numbered registry of every step in this migration, in execution order:

| Step # | Operation | Target Table | Target Object (column / index / constraint) | Change Type |
|--------|-----------|--------------|---------------------------------------------|-------------|

Change Type must be exactly one of: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT / DROP CONSTRAINT / ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

DISQUALIFIER: Steps listed alphabetically by table rather than in execution order fails C-05. C-05 is satisfied by Phase B alone; this registry establishes the canonical ordinal all downstream sections must cite.

Citation anchor: All downstream sections reference steps as "Step N from P0." At least two sections must use this form (C-11 requirement).

### P0a — Constraint Type Registry

Enumerate every constraint type present in this migration. Complete before any constraint analysis begins:

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

This is the binding manifest. A constraint type marked YES that later lacks a dedicated Phase A BINARY FIELD or a Phase B canonical table column is a manifest violation (fails C-31 and C-32 simultaneously).

---

### BOUNDARY PROTOCOL — Parse-to-A

```
EXIT BLOCK (bottom of PARSE PHASE):
  PARSE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: P0 Step Registry complete (all steps numbered, Change Type populated)
             AND P0a enumerates all four constraint types with YES/NO stated.
  BLOCKED if: either condition unmet.
  Guards: PHASE A INTERROGATION.

ENTRY REFERENCE (top of PHASE A INTERROGATION):
  PARSE GATE = OPEN required before writing any Phase A content.
  If BLOCKED: return to PARSE PHASE and complete P0 and P0a.
```

---

## PHASE A — INTERROGATION
### (PARSE GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL Parse-to-A)

---

### STATUS QUO COST

Before writing Q1, establish the status quo from an infrastructure perspective. This section precedes all domain-role analysis.

**COST LEDGER** (required three-row table — completeness verifiable by row count):

| Row | Category | Content |
|-----|----------|---------| 
| (a) | CURRENT SCHEMA CONDITION | [name a specific schema state, migration-state dependency, or infrastructure constraint] |
| (b) | DEPENDENT PROCESS | [name the specific business process that currently works because condition (a) holds] |
| (c) | ACCUMULATION TRAJECTORY | [chronic cost, risk rate, or technical debt if migration abandoned; rate + horizon + named metric] |

**Row (a) enforcement**: Row (a) MUST name a current schema condition, migration-state dependency, or infrastructure constraint. Row (a) MUST NOT name a revenue metric, a Commerce process disruption, or a Finance outcome.

---

### THREE-ARTIFACT SUBSTRATE ALIGNMENT

Before writing Q1, confirm and record the three-artifact alignment. This section is a structural commitment that precedes all analytical content.

The infrastructure condition named in COST LEDGER row (a) MUST be:
1. The primary analytical domain of Phase A Q1 (Operations Expert).
2. The shared failure substrate cited in B2's cross-role causal chain.

**ALIGNMENT MANDATE**: COST LEDGER row (a) [infrastructure condition], Phase A Q1 [analytical domain], and B2 chain substrate [shared failure condition] MUST name the same infrastructure condition class. A divergence — where row (a) names condition X, Q1 analyzes condition Y, and B2's chain substrate names condition Z — is a three-artifact alignment failure requiring revision before Phase B may proceed.

Declare the aligned condition before writing Q1:

- COST LEDGER row (a) names: _______________________________________________
- Q1 will analyze: _______________________________________________
- B2 cross-role chain substrate will be: _______________________________________________

ALIGNMENT STATE (BINARY FIELD): ALIGNED / MISALIGNED

Set to ALIGNED only when all three fields above name the same infrastructure condition class. If MISALIGNED: revise COST LEDGER row (a) and re-confirm before writing Q1.

---

### ROLE ANALYSIS ENFORCEMENT

Every domain-role question (Q1, Q2, Q3) must apply the following checklist in full. Failure to apply any item is an instruction violation, not a silent omission. DO NOT SCOPE OR SHORTEN any item for any role:

1. Before/After state per changed entity — DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path identification — apply to ALL steps, not only destructive ones
3. Constraint violation analysis with dedicated BINARY FIELD per type — DO NOT ROUTE ANY TYPE THROUGH A FREE-FORM FIELD
4. DEFAULT presence check for ALL new NOT NULL columns in ALL tables — NOT financial columns only
5. Zero-downtime viability assessment — apply to ALL domain roles, not Commerce only
6. Performance cliff detection — apply to ALL roles
7. Rollback viability per destructive step using fixed taxonomy (FULL / BACKUP-ONLY / IRREVERSIBLE)
8. Idempotency check per step

Citation mandate: "Reference each affected step as 'Step N from P0'" must appear in every question (Q1, Q2, Q3).

---

### Q1 — Operations Expert Analysis (leads Phase A)

**Role**: Operations Expert — job queues, infrastructure metadata, monitoring tables, deployment scaffolding, schema version management.
**Citation**: Reference each affected step as "Step N from P0."

Q1 establishes the shared infrastructure conditions that Commerce and Finance both depend on. Ground Q1 analysis in the COST LEDGER row (a) condition declared in THREE-ARTIFACT SUBSTRATE ALIGNMENT above.

**A. Before/After State**
For each step in P0, state schema state before and after. Use exact type names, constraint definitions, and index specifications. Include ALL tables.

DISQUALIFIER: "column type changed" without naming old and new types fails C-01.

**B. Data Loss Path**
DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE
If YES or POSSIBLE: Step N from P0, mechanism (silent truncation / row drop / value cast without error / precision loss), condition.
If NO: state explicit reasoning.

**C. Constraint Violation Analysis**
For each type marked YES in P0a:

NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
— If YES or PARTIAL: Step N from P0, table, column, estimated affected rows, migration response (fail / skip / backfill).

FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
— If YES or PARTIAL: Step N from P0, FK name, parent table, orphaned-record condition, migration response.

UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
— If YES or PARTIAL: Step N from P0, column, duplicate value scenario, migration response.

CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
— If YES or PARTIAL: Step N from P0, CHECK expression, failing record condition, migration response.

DISQUALIFIER: Routing any constraint type through a free-form NOTES or DISRUPTION field fails C-28.

**D. DEFAULT Presence Check**
For every ADD COLUMN NOT NULL step in P0: does the migration supply a DEFAULT? Apply to ALL new NOT NULL columns in ALL tables. Flag as migration risk if DEFAULT absent on non-empty table.

**E. Zero-Downtime Viability**
Can this migration run without a maintenance window using online DDL or expand/contract pattern? If not: Step N from P0 requiring maintenance window, engine-level reason (table lock / replication pause / blocking DDL), rolling deploy compatibility window.

**F. Performance Cliff Detection**
Identify every Step N from P0 likely to cause a performance cliff (full-table rewrite, index rebuild on wide table, type cast requiring row scan). For each: table name, estimated row count, specific risk (lock duration / I/O spike / replication lag).

**G. Rollback Viability**
ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE) for each destructive step (Step N from P0). Classify at least one step.

**H. Idempotency Check**
For each step in P0: safe to run twice? If not: name the specific failure mode (duplicate key error / double-applied data transform / constraint re-add error / orphaned trigger from re-run).

---

Q1 EXIT GATE: Q1_COMPLETE (BINARY FIELD): OPEN / BLOCKED
OPEN when: all changed entities traced AND shared infrastructure conditions named.
BLOCKED if: any entity untouched or shared conditions absent.

---

### Q2 — Commerce Expert Analysis

**Role**: Commerce Expert — order pipelines, catalog tables, pricing, SKU inventory.
**Citation**: Reference each affected step as "Step N from P0."

Apply the complete ROLE ANALYSIS ENFORCEMENT checklist. Ground at least one example in the COST LEDGER row (a) condition. DO NOT limit DEFAULT checks to commerce tables. DO NOT limit zero-downtime assessment to Commerce role only.

Q2 EXIT GATE: Q2_COMPLETE (BINARY FIELD): OPEN / BLOCKED

**A. Before/After State** [full enumeration, exact types, ALL tables]
**B.** DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE [Commerce: truncation on price/amount, catalog row drops]
**C.** NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL | FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL [each: Step N from P0 + table + column + migration response]
**D.** DEFAULT Presence Check [ALL tables]
**E.** Zero-Downtime Viability [Commerce: checkout pipeline continuity during DDL]
**F.** Performance Cliff [Commerce: catalog scan, order index rebuild]
**G.** ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)
**H.** Idempotency Check [double-submit risk on order tables, SKU re-insert]

---

### Q3 — Finance Expert Analysis

**Role**: Finance Expert — ledger tables, transaction logs, audit trails, amount columns.
**Citation**: Reference each affected step as "Step N from P0."

Apply the complete ROLE ANALYSIS ENFORCEMENT checklist. DO NOT limit DEFAULT checks to financial columns. DO NOT limit zero-downtime to Commerce only.

Q3 EXIT GATE: Q3_COMPLETE (BINARY FIELD): OPEN / BLOCKED

**A. Before/After State** [ledger and audit focus, ALL tables]
**B.** DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE [Finance: decimal precision loss, audit truncation, ledger row drops]
**C.** NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL | FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D.** DEFAULT Presence Check [ALL tables, NOT financial only]
**E.** Zero-Downtime Viability [Finance: transaction log lock, audit continuity]
**F.** Performance Cliff [Finance: ledger scan cost, audit log rebuild]
**G.** ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)
**H.** Idempotency Check [ledger double-apply, audit log re-insert]

---

### BOUNDARY PROTOCOL — A-to-B

```
EXIT BLOCK (bottom of PHASE A INTERROGATION):
  TRACE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: THREE-ARTIFACT ALIGNMENT STATE = ALIGNED AND Q1_COMPLETE = OPEN
             AND Q2_COMPLETE = OPEN AND Q3_COMPLETE = OPEN AND every BINARY
             FIELD in Q1/Q2/Q3 carries a value.
  BLOCKED if: ALIGNMENT STATE = MISALIGNED or any BINARY FIELD unresolved.
  Guards: PHASE B CANONICAL OUTPUT.

ENTRY REFERENCE (top of PHASE B CANONICAL OUTPUT):
  TRACE GATE = OPEN required before writing any Phase B content.
  If BLOCKED: resolve THREE-ARTIFACT ALIGNMENT STATE and all Phase A gaps first.
```

---

## PHASE B — CANONICAL OUTPUT
### (TRACE GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL A-to-B)
### C-05 is satisfied by Phase B alone, not by any Phase A section.

---

### PROTOCOL COUNT MANIFEST

Before writing any Phase B content, pre-commit all Phase B boundaries:

| Boundary | Gate Name | Gate State |
|----------|-----------|------------|
| B1-to-B2 | DOMAIN SYNTHESIS GATE | OPEN / BLOCKED |
| B2-to-B3 | VERIFY GATE | OPEN / BLOCKED |
| B3-to-B4 | RECOMMENDATIONS GATE | OPEN / BLOCKED |
| B4-to-VERDICT | VERDICT GATE | OPEN / BLOCKED |

A boundary present in this table but absent from Phase B BOUNDARY PROTOCOL headers — or vice versa — is a cross-document alignment failure.

---

### B1 — Canonical Execution Table

Produce a single execution-ordered table. Step # must match P0 exactly.

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

All four constraint-type columns required for every type enumerated in P0a. Use NONE (not N/A, not blank) if no violation exists for a given step on a type marked YES in P0a.

---

### BOUNDARY PROTOCOL — B1-to-B2

```
EXIT BLOCK (bottom of B1):
  DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B1 complete, all constraint-type columns populated, step numbers match P0.
  BLOCKED if: any column missing, any row has blank constraint-type cell.
  Guards: B2 DOMAIN SYNTHESIS.

ENTRY REFERENCE (top of B2 DOMAIN SYNTHESIS):
  DOMAIN SYNTHESIS GATE = OPEN required.
  If BLOCKED: complete B1 before writing B2.
```

---

### B2 — Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY — complete before writing B3)
### (DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B1-to-B2)

THREE-ARTIFACT ALIGNMENT CONFIRMATION: The substrate condition cited in B2's cross-role causal chain MUST be the same infrastructure state named in COST LEDGER row (a) and analyzed in Q1. Confirm: ALIGNMENT STATE recorded in Phase A = ALIGNED before writing the B2 example.

**Cross-role causal chain requirement**: B2 must name a shared infrastructure substrate failure whose consequences cascade to BOTH Commerce and Finance roles. Structure:
- Operations substrate condition (Step N from P0, named schema condition)
- Commerce consequence (named business outcome for Commerce role)
- Finance consequence (named business outcome for Finance role)

**Pre-seeded cross-role inertia chain** (model output — not an instruction):
> The STATUS QUO COST established that `migration_jobs.job_version` NOT NULL constraint is absent (Step 4 from P0). Before Step 4, the order dispatch pipeline worked because the scheduler inserted job records without `job_version` and orders fulfilled in FIFO sequence. After Step 4, `job_version = NULL` violates the new constraint, causing INSERT failures on any node not yet running the updated scheduler.
> Commerce consequence: orders placed during the rolling deploy window stall silently; at 200 orders/minute over a 5-minute window, 1,000 orders accumulate in the dispatch queue with no customer notification.
> Finance consequence: stalled dispatch records create `payment_events` with `status = 'pending_dispatch'` that cannot advance to `'settled'`; the AR ledger shows unbounded pending-payment balances until the scheduler patch propagates.

The B2 example must name a DIFFERENT step, table, or consequence than STATUS QUO COST row (a).

---

### BOUNDARY PROTOCOL — B2-to-B3

```
EXIT BLOCK (bottom of B2):
  VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B2 contains at least one cross-role causal chain (Operations substrate
             → Commerce consequence AND Finance consequence) with named steps from P0,
             grounded in COST LEDGER row (a) infrastructure condition.
  BLOCKED if: B2 lacks cross-role framing, or substrate diverges from COST LEDGER
              row (a) condition, or single-role consequence only.
  Guards: B3 VERIFICATION.

ENTRY REFERENCE (top of B3 VERIFICATION):
  VERIFY GATE = OPEN required.
  If BLOCKED: complete B2 cross-role chain before writing B3.
```

---

### B3 — Verification Checks
### (VERIFY GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B2-to-B3)

At least one SQL verification query per data loss path found in B1. Each query must reference "Step N from P0" and name the table and condition verified.

Example: `SELECT COUNT(*) FROM orders WHERE amount > 9999999.99` — verifies Step 3 truncation scope before migration.

---

### BOUNDARY PROTOCOL — B3-to-B4

```
EXIT BLOCK (bottom of B3):
  RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: at least one concrete verification query per data loss path in B1.
  BLOCKED if: verification absent or contains only generic descriptions.
  Guards: B4 RECOMMENDATIONS.

ENTRY REFERENCE (top of B4 RECOMMENDATIONS):
  RECOMMENDATIONS GATE = OPEN required.
  If BLOCKED: add concrete verification queries before writing B4.
```

---

### B4 — Recommendations
### (RECOMMENDATIONS GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B3-to-B4)

At least one concrete recommendation per destructive step classified BACKUP-ONLY or IRREVERSIBLE in B1. Reference "Step N from P0." Include at least one recommendation addressing the B2 cross-role inertia chain.

---

### BOUNDARY PROTOCOL — B4-to-VERDICT

```
EXIT BLOCK (bottom of B4):
  VERDICT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: every BACKUP-ONLY or IRREVERSIBLE step in B1 has a recommendation
             in B4, AND B2 cross-role chain has a mitigation in B4.
  BLOCKED if: any irreversible step or B2 chain unaddressed.
  Guards: VERDICT.

ENTRY REFERENCE (top of VERDICT):
  VERDICT GATE = OPEN required.
  If BLOCKED: address all irreversible steps and B2 chain in B4 first.
```

---

### VERDICT
### (VERDICT GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B4-to-VERDICT)

State: overall migration risk level (LOW / MEDIUM / HIGH / CRITICAL), count of data loss paths, count of irreversible steps, zero-downtime viability verdict, STATUS QUO COST accumulation trajectory summary (infrastructure condition named, Commerce consequence, Finance consequence).

---

---

## V-02 — Axis B: C-43 Named COST LEDGER SUBSTRATE GATE

**Variation axis**: A named COST LEDGER SUBSTRATE GATE block replaces the inline row (a) enforcement text immediately after the COST LEDGER table. The gate has a fixed structure — ROW (a) CATEGORY GATE (BINARY FIELD): VALID / INVALID — with explicit VALID and INVALID conditions and a hard conditional return-to-parse instruction on INVALID. No THREE-ARTIFACT SUBSTRATE ALIGNMENT block (C-42 intentionally absent). B2 inline statement names COST LEDGER row (a) and Q1 but does not explicitly name B2 chain substrate as the third artifact.

**Hypothesis**: V-02 tests whether C-43 is most effectively enforced as a named gate block (structurally co-located with the COST LEDGER and as machine-scannable as a BOUNDARY PROTOCOL) vs inline prohibition text. The named gate block elevates row (a) category enforcement to the same structural level as phase-transition gates: a wrong-category row (a) is a gate failure requiring parse restart, not a style note. C-42 is intentionally absent to isolate the return-path axis from the binding-mandate axis; the combination is tested in V-04.

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A question. Available roles:

- **Operations Expert** — job queues, infrastructure metadata, monitoring tables, deployment scaffolding, schema version management
- **Commerce Expert** — order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** — ledger tables, transaction logs, audit trails, amount columns

---

## PARSE PHASE

### P0 — Migration Step Registry

| Step # | Operation | Target Table | Target Object (column / index / constraint) | Change Type |
|--------|-----------|--------------|---------------------------------------------|-------------|

Change Type: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT / DROP CONSTRAINT / ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

Citation anchor: All downstream sections cite steps as "Step N from P0." At least two sections must use this form.

### P0a — Constraint Type Registry

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

Binding manifest: a constraint type marked YES that later lacks a dedicated Phase A BINARY FIELD or Phase B canonical column is a manifest violation (fails C-31 and C-32).

---

### BOUNDARY PROTOCOL — Parse-to-A

```
EXIT BLOCK (bottom of PARSE PHASE):
  PARSE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: P0 complete AND P0a enumerates all four constraint types.
  BLOCKED if: either condition unmet.
  Guards: PHASE A INTERROGATION.

ENTRY REFERENCE (top of PHASE A INTERROGATION):
  PARSE GATE = OPEN required before writing any Phase A content.
  If BLOCKED: return to PARSE PHASE.
```

---

## PHASE A — INTERROGATION
### (PARSE GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL Parse-to-A)

---

### STATUS QUO COST

Before writing Q1, establish the status quo from an infrastructure perspective.

**COST LEDGER** (required three-row table):

| Row | Category | Content |
|-----|----------|---------| 
| (a) | CURRENT SCHEMA CONDITION | [name a specific schema state, migration-state dependency, or infrastructure constraint] |
| (b) | DEPENDENT PROCESS | [name the business process that currently works because condition (a) holds] |
| (c) | ACCUMULATION TRAJECTORY | [chronic cost, risk rate, or technical debt if migration abandoned; rate + horizon + named metric] |

---

### COST LEDGER SUBSTRATE GATE

```
ROW (a) CATEGORY GATE (BINARY FIELD): VALID / INVALID

VALID when: row (a) names a current schema condition, migration-state dependency,
            or infrastructure constraint.

INVALID if: row (a) names a revenue metric, a Commerce process disruption, or a
            Finance outcome.

CONDITIONAL RETURN INSTRUCTION: If ROW (a) CATEGORY GATE = INVALID, return to
PARSE PHASE. Rewrite COST LEDGER row (a) to name a schema state or infrastructure
condition before writing Q1. Do not advance to Q1 with an INVALID row (a).
```

---

### ROLE ANALYSIS ENFORCEMENT

Every domain-role question (Q1, Q2, Q3) must apply the following checklist in full. Failure to apply any item is an instruction violation. DO NOT SCOPE OR SHORTEN any item:

1. Before/After state per changed entity — DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path identification — apply to ALL steps
3. Constraint violation analysis with dedicated BINARY FIELD per type — DO NOT ROUTE ANY TYPE THROUGH A FREE-FORM FIELD
4. DEFAULT presence check for ALL new NOT NULL columns in ALL tables — NOT financial columns only
5. Zero-downtime viability assessment — apply to ALL domain roles
6. Performance cliff detection — apply to ALL roles
7. Rollback viability per destructive step using fixed taxonomy (FULL / BACKUP-ONLY / IRREVERSIBLE)
8. Idempotency check per step

Citation mandate: "Reference each affected step as 'Step N from P0'" in every question.

---

### Q1 — Operations Expert Analysis (leads Phase A)

**Role**: Operations Expert.
**Citation**: Reference each affected step as "Step N from P0."

Q1 establishes the shared infrastructure conditions that Commerce and Finance both depend on. Ground Q1 analysis in the COST LEDGER row (a) condition. Q1 EXIT GATE condition: all changed entities traced AND shared infrastructure conditions named.

Q1 EXIT GATE: Q1_COMPLETE (BINARY FIELD): OPEN / BLOCKED

**A. Before/After State** — exact types, constraint definitions, index specs, ALL tables.

**B.** DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE
[Step N from P0, mechanism, condition; or NO with reasoning]

**C.** NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL | FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Each: Step N from P0 + table + column + migration response]

**D.** DEFAULT Presence Check [ALL new NOT NULL columns, ALL tables]

**E.** Zero-Downtime Viability [Operations: rolling deploy compatibility, schema version backward-compat window, scheduler compatibility during DDL]

**F.** Performance Cliff [Operations: job queue index rebuild during peak, monitoring table scan]

**G.** ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE) [classify each destructive step]

**H.** Idempotency Check [job dedup key risks, monitoring counter double-apply, deployment scaffolding table re-run]

---

### Q2 — Commerce Expert Analysis

**Role**: Commerce Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply ROLE ANALYSIS ENFORCEMENT checklist in full. Ground at least one example in COST LEDGER row (a). DO NOT limit DEFAULT checks to commerce tables. Q2 EXIT GATE: Q2_COMPLETE (BINARY FIELD): OPEN / BLOCKED.

**A.** Before/After State [ALL tables, exact types]
**B.** DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE [Commerce: price/amount truncation, catalog drops]
**C.** NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL | FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D.** DEFAULT Presence Check [ALL tables]
**E.** Zero-Downtime Viability [Commerce: checkout continuity during DDL]
**F.** Performance Cliff [Commerce: catalog scan, order index rebuild]
**G.** ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)
**H.** Idempotency Check [double-submit on orders, SKU re-insert]

---

### Q3 — Finance Expert Analysis

**Role**: Finance Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply ROLE ANALYSIS ENFORCEMENT checklist in full. DO NOT limit DEFAULT checks to financial columns. Q3 EXIT GATE: Q3_COMPLETE (BINARY FIELD): OPEN / BLOCKED.

**A.** Before/After State [ledger/audit focus, ALL tables]
**B.** DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE [decimal precision loss, audit truncation]
**C.** NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL | FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D.** DEFAULT Presence Check [ALL tables, NOT financial only]
**E.** Zero-Downtime Viability [Finance: transaction log lock, audit continuity]
**F.** Performance Cliff [Finance: ledger scan cost, audit log rebuild]
**G.** ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)
**H.** Idempotency Check [ledger double-apply, audit log re-insert]

---

### BOUNDARY PROTOCOL — A-to-B

```
EXIT BLOCK (bottom of PHASE A INTERROGATION):
  TRACE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: ROW (a) CATEGORY GATE = VALID AND Q1_COMPLETE = OPEN AND
             Q2_COMPLETE = OPEN AND Q3_COMPLETE = OPEN AND every BINARY FIELD
             in Q1/Q2/Q3 carries a value.
  BLOCKED if: ROW (a) CATEGORY GATE = INVALID or any BINARY FIELD unresolved.
  Guards: PHASE B CANONICAL OUTPUT.

ENTRY REFERENCE (top of PHASE B CANONICAL OUTPUT):
  TRACE GATE = OPEN required before writing any Phase B content.
  If BLOCKED: resolve COST LEDGER SUBSTRATE GATE and all Phase A gaps first.
```

---

## PHASE B — CANONICAL OUTPUT
### (TRACE GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL A-to-B)
### C-05 is satisfied by Phase B alone, not by any Phase A section.

---

### PROTOCOL COUNT MANIFEST

| Boundary | Gate Name | Gate State |
|----------|-----------|------------|
| B1-to-B2 | DOMAIN SYNTHESIS GATE | OPEN / BLOCKED |
| B2-to-B3 | VERIFY GATE | OPEN / BLOCKED |
| B3-to-B4 | RECOMMENDATIONS GATE | OPEN / BLOCKED |
| B4-to-VERDICT | VERDICT GATE | OPEN / BLOCKED |

---

### B1 — Canonical Execution Table

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

All four constraint-type columns required for types marked YES in P0a. Use NONE for types with no violation on a given step.

---

### BOUNDARY PROTOCOL — B1-to-B2

```
EXIT BLOCK (bottom of B1):
  DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B1 complete, all constraint-type columns populated, step numbers match P0.
  BLOCKED if: any column missing or blank constraint-type cell.
  Guards: B2 DOMAIN SYNTHESIS.

ENTRY REFERENCE (top of B2):
  DOMAIN SYNTHESIS GATE = OPEN required.
```

---

### B2 — Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY — complete before writing B3)
### (DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B1-to-B2)

The substrate condition cited in B2's cross-role causal chain must be the same infrastructure state named in COST LEDGER row (a) and analyzed in Q1.

**Cross-role causal chain requirement**: B2 names a shared infrastructure substrate failure whose consequences cascade to BOTH Commerce and Finance roles. Structure: Operations substrate condition → Commerce consequence → Finance consequence.

**Pre-seeded cross-role inertia chain** (model output — not an instruction):
> COST LEDGER row (a) established that `migration_jobs.job_version` NOT NULL constraint is absent. Before Step 4, the order dispatch pipeline worked because the scheduler inserted job records without `job_version`. After Step 4, `job_version = NULL` violates the constraint causing INSERT failures on nodes not yet updated.
> Commerce consequence: orders stall silently at 200/minute during rolling deploy window — 1,000 orders in stalled dispatch queue with no customer notification.
> Finance consequence: stalled records create `payment_events` stuck in `pending_dispatch`; AR ledger shows unbounded pending-payment balances.

The B2 example must name a DIFFERENT step or consequence than STATUS QUO COST row (a).

---

### BOUNDARY PROTOCOL — B2-to-B3

```
EXIT BLOCK (bottom of B2):
  VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B2 contains cross-role chain (Operations substrate → Commerce + Finance
             consequence) grounded in COST LEDGER row (a) condition.
  BLOCKED if: single-role consequence, substrate diverges from row (a), or no named step.
  Guards: B3 VERIFICATION.

ENTRY REFERENCE (top of B3):
  VERIFY GATE = OPEN required.
```

---

### B3 — Verification Checks
### (VERIFY GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B2-to-B3)

At least one SQL verification query per data loss path in B1. Each references "Step N from P0" with table and condition.

---

### BOUNDARY PROTOCOL — B3-to-B4

```
EXIT BLOCK (bottom of B3):
  RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: at least one concrete verification query per data loss path.
  BLOCKED if: absent or generic.
  Guards: B4 RECOMMENDATIONS.

ENTRY REFERENCE (top of B4):
  RECOMMENDATIONS GATE = OPEN required.
```

---

### B4 — Recommendations
### (RECOMMENDATIONS GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B3-to-B4)

At least one concrete recommendation per BACKUP-ONLY or IRREVERSIBLE step. Reference "Step N from P0." Include a recommendation addressing the B2 cross-role chain.

---

### BOUNDARY PROTOCOL — B4-to-VERDICT

```
EXIT BLOCK (bottom of B4):
  VERDICT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: every irreversible step has recommendation AND B2 chain has mitigation.
  BLOCKED if: any unaddressed.
  Guards: VERDICT.

ENTRY REFERENCE (top of VERDICT):
  VERDICT GATE = OPEN required.
```

---

### VERDICT
### (VERDICT GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B4-to-VERDICT)

State: risk level (LOW / MEDIUM / HIGH / CRITICAL), data loss path count, irreversible step count, zero-downtime viability, STATUS QUO COST trajectory summary.

---

---

## V-03 — Axis C: C-17 Full "(BINARY FIELD)" Annotation at Both Bilateral Positions

**Variation axis**: Every gate state field in every BOUNDARY PROTOCOL block carries the explicit "(BINARY FIELD)" annotation at BOTH the EXIT BLOCK definition position AND the ENTRY REFERENCE position. In V-01 and V-02 the ENTRY REFERENCE lines use "GATE = OPEN required" (no "(BINARY FIELD)" label). V-03 upgrades every ENTRY REFERENCE to "GATE (BINARY FIELD) = OPEN required." No THREE-ARTIFACT block (C-42 absent). No COST LEDGER SUBSTRATE GATE (C-43 absent). Only negative C-41 constraint.

**Hypothesis**: R15 V-01 scored C-17 PARTIAL because gate state fields lacked "(BINARY FIELD)" at the ENTRY REFERENCE definition site. V-03 tests whether adding the annotation at ENTRY REFERENCE positions closes that specific gap without touching C-42 or C-43. Expected: C-17 PASS, residual C-42/C-43 FAIL. The structural gain is modest (~3 pts on C-17) but validates the C-17 partial diagnosis before combining with V-04/V-05.

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A question. Available roles:

- **Operations Expert** — job queues, infrastructure metadata, monitoring tables, deployment scaffolding, schema version management
- **Commerce Expert** — order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** — ledger tables, transaction logs, audit trails, amount columns

---

## PARSE PHASE

### P0 — Migration Step Registry

| Step # | Operation | Target Table | Target Object (column / index / constraint) | Change Type |
|--------|-----------|--------------|---------------------------------------------|-------------|

Change Type: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT / DROP CONSTRAINT / ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

Citation anchor: All sections cite steps as "Step N from P0." At least two sections must use this form.

### P0a — Constraint Type Registry

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

Binding manifest: constraint type marked YES that lacks a dedicated Phase A BINARY FIELD or Phase B canonical column = manifest violation (fails C-31 and C-32).

---

### BOUNDARY PROTOCOL — Parse-to-A

```
EXIT BLOCK (bottom of PARSE PHASE):
  PARSE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: P0 complete AND P0a enumerates all four constraint types.
  BLOCKED if: either condition unmet.
  Guards: PHASE A INTERROGATION.

ENTRY REFERENCE (top of PHASE A INTERROGATION):
  PARSE GATE (BINARY FIELD) = OPEN required before writing any Phase A content.
  If BLOCKED: return to PARSE PHASE.
```

*[C-17 axis: ENTRY REFERENCE carries "(BINARY FIELD)" annotation — all BOUNDARY PROTOCOL ENTRY REFERENCEs follow this pattern throughout.]*

---

## PHASE A — INTERROGATION
### (PARSE GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL Parse-to-A)

---

### STATUS QUO COST

Before writing Q1, establish the status quo from an infrastructure perspective.

**COST LEDGER** (required three-row table):

| Row | Category | Content |
|-----|----------|---------| 
| (a) | CURRENT SCHEMA CONDITION | [name a specific schema state, migration-state dependency, or infrastructure constraint — NOT a revenue metric, Commerce process disruption, or Finance outcome] |
| (b) | DEPENDENT PROCESS | [name the business process that currently works because condition (a) holds] |
| (c) | ACCUMULATION TRAJECTORY | [chronic cost, risk rate, or technical debt if migration abandoned; rate + horizon + named metric] |

Row (a) MUST name a schema condition or infrastructure constraint. Row (a) MUST NOT name a revenue metric, a Commerce process disruption, or a Finance outcome.

---

### ROLE ANALYSIS ENFORCEMENT

Every domain-role question (Q1, Q2, Q3) must apply the following checklist in full. DO NOT SCOPE OR SHORTEN any item for any role:

1. Before/After state per changed entity — DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path identification — apply to ALL steps
3. Constraint violation analysis with dedicated BINARY FIELD per type — DO NOT ROUTE ANY TYPE THROUGH A FREE-FORM FIELD
4. DEFAULT presence check for ALL new NOT NULL columns in ALL tables — NOT financial columns only
5. Zero-downtime viability assessment — apply to ALL domain roles
6. Performance cliff detection — apply to ALL roles
7. Rollback viability per destructive step (FULL / BACKUP-ONLY / IRREVERSIBLE)
8. Idempotency check per step

Citation mandate: "Reference each affected step as 'Step N from P0'" in every question.

---

### Q1 — Operations Expert Analysis (leads Phase A)

**Role**: Operations Expert.
**Citation**: Reference each affected step as "Step N from P0."

Q1 establishes shared infrastructure conditions that Commerce and Finance depend on. Ground Q1 analysis in COST LEDGER row (a).

Q1 EXIT GATE: Q1_COMPLETE (BINARY FIELD): OPEN / BLOCKED
OPEN when: all changed entities traced AND shared infrastructure conditions named.

**A.** Before/After State [exact types, constraint definitions, index specs, ALL tables]
**B.** DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE [Step N from P0, mechanism, condition; or NO with reasoning]
**C.** NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL | FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL | CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D.** DEFAULT Presence Check [ALL tables]
**E.** Zero-Downtime Viability [Operations: rolling deploy compat, scheduler during DDL]
**F.** Performance Cliff [Operations: job queue index rebuild, monitoring table scan]
**G.** ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)
**H.** Idempotency Check [job dedup key, monitoring counter double-apply]

---

### Q2 — Commerce Expert Analysis

**Role**: Commerce Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply ROLE ANALYSIS ENFORCEMENT in full. Ground at least one example in COST LEDGER row (a). Q2 EXIT GATE: Q2_COMPLETE (BINARY FIELD): OPEN / BLOCKED.

**A–H.** [Apply full 8-item checklist from ROLE ANALYSIS ENFORCEMENT. Commerce focus: price/amount truncation, catalog drops, checkout pipeline, SKU re-insert risk.]

---

### Q3 — Finance Expert Analysis

**Role**: Finance Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply ROLE ANALYSIS ENFORCEMENT in full. DO NOT limit DEFAULT checks to financial columns. Q3 EXIT GATE: Q3_COMPLETE (BINARY FIELD): OPEN / BLOCKED.

**A–H.** [Apply full 8-item checklist. Finance focus: decimal precision loss, audit truncation, ledger double-apply, transaction log lock.]

---

### BOUNDARY PROTOCOL — A-to-B

```
EXIT BLOCK (bottom of PHASE A INTERROGATION):
  TRACE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: Q1_COMPLETE = OPEN AND Q2_COMPLETE = OPEN AND Q3_COMPLETE = OPEN
             AND every BINARY FIELD in Q1/Q2/Q3 carries a value.
  BLOCKED if: any BINARY FIELD unresolved.
  Guards: PHASE B CANONICAL OUTPUT.

ENTRY REFERENCE (top of PHASE B CANONICAL OUTPUT):
  TRACE GATE (BINARY FIELD) = OPEN required before writing any Phase B content.
  If BLOCKED: resolve all Phase A BINARY FIELD gaps first.
```

---

## PHASE B — CANONICAL OUTPUT
### (TRACE GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL A-to-B)
### C-05 is satisfied by Phase B alone, not by any Phase A section.

---

### PROTOCOL COUNT MANIFEST

| Boundary | Gate Name | Gate State |
|----------|-----------|------------|
| B1-to-B2 | DOMAIN SYNTHESIS GATE | OPEN / BLOCKED |
| B2-to-B3 | VERIFY GATE | OPEN / BLOCKED |
| B3-to-B4 | RECOMMENDATIONS GATE | OPEN / BLOCKED |
| B4-to-VERDICT | VERDICT GATE | OPEN / BLOCKED |

---

### B1 — Canonical Execution Table

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

All four constraint-type columns required for types marked YES in P0a. Use NONE (not blank) for types with no violation on a given step.

---

### BOUNDARY PROTOCOL — B1-to-B2

```
EXIT BLOCK (bottom of B1):
  DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B1 complete, all constraint-type columns populated, step numbers match P0.
  BLOCKED if: any column missing or blank cell.
  Guards: B2 DOMAIN SYNTHESIS.

ENTRY REFERENCE (top of B2 DOMAIN SYNTHESIS):
  DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: complete B1 before writing B2.
```

---

### B2 — Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY — complete before writing B3)
### (DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B1-to-B2)

The substrate condition cited in B2's cross-role causal chain must be the same infrastructure state named in COST LEDGER row (a) and analyzed in Q1.

**Cross-role causal chain**: B2 names a shared infrastructure substrate failure cascading to BOTH Commerce and Finance. Structure: Operations substrate → Commerce consequence → Finance consequence.

**Pre-seeded cross-role inertia chain** (model output):
> COST LEDGER row (a) established the absent `job_version NOT NULL` constraint (Step 4 from P0). Before Step 4, the order dispatch pipeline worked because job records inserted without `job_version` and orders fulfilled in FIFO sequence. After Step 4, NULL values violate the new constraint causing INSERT failures on nodes not yet updated.
> Commerce consequence: 1,000 orders stall silently in the dispatch queue during rolling deploy (200/min × 5 min window).
> Finance consequence: `payment_events` stuck in `pending_dispatch` create unbounded pending-payment balances in the AR ledger.

B2 example must name a DIFFERENT step or consequence than STATUS QUO COST row (a).

---

### BOUNDARY PROTOCOL — B2-to-B3

```
EXIT BLOCK (bottom of B2):
  VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B2 contains cross-role chain (Operations substrate → Commerce + Finance)
             grounded in COST LEDGER row (a).
  BLOCKED if: single-role consequence, substrate diverges from row (a).
  Guards: B3 VERIFICATION.

ENTRY REFERENCE (top of B3 VERIFICATION):
  VERIFY GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: complete B2 cross-role chain before writing B3.
```

---

### B3 — Verification Checks
### (VERIFY GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B2-to-B3)

At least one SQL verification query per data loss path in B1. Each references "Step N from P0" with table and condition.

---

### BOUNDARY PROTOCOL — B3-to-B4

```
EXIT BLOCK (bottom of B3):
  RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: at least one concrete verification query per data loss path.
  BLOCKED if: absent or generic.
  Guards: B4 RECOMMENDATIONS.

ENTRY REFERENCE (top of B4 RECOMMENDATIONS):
  RECOMMENDATIONS GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: add concrete verification queries before writing B4.
```

---

### B4 — Recommendations
### (RECOMMENDATIONS GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B3-to-B4)

At least one recommendation per BACKUP-ONLY or IRREVERSIBLE step. Reference "Step N from P0." Include a recommendation addressing the B2 cross-role chain.

---

### BOUNDARY PROTOCOL — B4-to-VERDICT

```
EXIT BLOCK (bottom of B4):
  VERDICT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: every irreversible step has recommendation AND B2 chain has mitigation.
  BLOCKED if: any unaddressed.
  Guards: VERDICT.

ENTRY REFERENCE (top of VERDICT):
  VERDICT GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: address all irreversible steps and B2 chain in B4 first.
```

---

### VERDICT
### (VERDICT GATE (BINARY FIELD) = OPEN — confirmed at BOUNDARY PROTOCOL B4-to-VERDICT)

State: risk level (LOW / MEDIUM / HIGH / CRITICAL), data loss path count, irreversible step count, zero-downtime viability verdict, STATUS QUO COST trajectory summary.

---

V-04 and V-05 continue in the next message.
