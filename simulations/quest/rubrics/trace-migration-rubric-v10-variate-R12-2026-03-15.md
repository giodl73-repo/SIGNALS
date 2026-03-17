# trace-migration — Round 12 Variations (Rubric v10)
# Generated: 2026-03-15

## Overview

Five complete, runnable skill body prompt variations for the `trace-migration` skill,
targeting the v10 rubric (220 pts, C-01 through C-34).

**R10/R11 history**: No prior trace-migration variate files exist in the repo. This is the
first variate round for this skill. The baseline is constructed from rubric criteria
C-01 through C-34 directly.

**R12 objective**: C-34 (Phase Boundary Dual-Anchor Gate Block) is the new criterion.
V-01 and V-02 are regression tests confirming C-34 is load-bearing by ablating one anchor
side each. V-03 is the full structural expression targeting C-34 PASS plus a new
excellence signal. V-04 and V-05 are combinations.

**Variation axes chosen:**
- **Axis A — Phrasing register (C-34 EXIT BLOCK ablation)**: exit blocks at bottom of
  preceding phases are softened to advisory NOTEs; only ENTRY REFERENCEs remain mandatory.
- **Axis B — Phrasing register (C-34 ENTRY REFERENCE ablation)**: entry references at top
  of succeeding phases are softened to advisory NOTEs; only EXIT BLOCKs remain mandatory.
- **Axis C — Lifecycle emphasis (dual-anchor bilateral gate block)**: every phase boundary
  carries a named BOUNDARY PROTOCOL block containing both EXIT BLOCK and ENTRY REFERENCE
  as explicit structural fields, both with "(BINARY FIELD)" annotation, creating a
  boundary-verifiable gate protocol rather than two loose annotations.
- **Axis D — Inertia framing**: a named STATUS QUO COST section precedes Phase A domain
  questions, establishing the three-part inertia-contrast baseline before analysis begins.
- **Axis E — Role sequence**: Operations Expert leads Phase A (Q1), Commerce Expert is Q2,
  Finance Expert is Q3.

| V | Axes | Key structural change | C-34 | New signal | Predicted |
|---|------|-----------------------|------|------------|-----------|
| V-01 | A only: EXIT BLOCK advisory | EXIT BLOCKs removed from phase bottoms; only ENTRY REFERENCEs at phase tops | FAIL | none | 215/220 |
| V-02 | B only: ENTRY REFERENCE advisory | ENTRY REFERENCEs removed from phase tops; only EXIT BLOCKs at phase bottoms | FAIL | none | 215/220 |
| V-03 | C only: BOUNDARY PROTOCOL block | Both EXIT BLOCK and ENTRY REFERENCE appear as named fields in a BOUNDARY PROTOCOL block at every boundary; bilateral detectability | PASS | C-35 candidate: BOUNDARY PROTOCOL as a named structured artifact (gate compliance computable from protocol block count) | 220/220 |
| V-04 | C + D: BOUNDARY PROTOCOL + inertia-first | V-03 plus named STATUS QUO COST section before Q1 seeding three-part inertia-contrast baseline | PASS | V-03 signal + inertia framing density elevated in Phase A | 220/220 |
| V-05 | C + D + E: all three axes | V-04 plus Operations-first role ordering; inertia baseline exposed to Operations lens first | PASS | Richest signal set; potential C-36 candidate from Operations-first inertia anchor | 220/220 |

---

## V-01 — Axis A: C-34 EXIT BLOCK Advisory

### Variation axis
EXIT BLOCK annotations at the bottom of preceding phases are removed. Every phase
transition carries only an ENTRY REFERENCE at the top of the succeeding phase with a
"(BINARY FIELD)" annotation. The gate state is declared once at the entry of each phase
rather than at both the exit of the prior phase and the entry of the succeeding phase.
All C-21, C-17, C-23, C-24, C-26 structural requirements are preserved in full.

### Hypothesis
Removing the EXIT BLOCK from the bottom of each preceding phase causes C-34 FAIL while
C-21 (complete phase gate chain) and C-17 (gate field annotation compound) remain PASS.
A response will carry valid binary gate fields with "(BINARY FIELD)" annotation at every
phase entry, satisfying C-21 single-point coverage and C-17 annotation, but will not
have the bilateral detectability required by C-34: a gate violation is visible only from
the succeeding phase's entry, not from the preceding phase's exit. Predicted: 215/220.

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A
question. Available roles:

- **Commerce Expert** -- order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** -- ledger tables, transaction logs, audit trails, amount columns
- **Operations Expert** -- job queues, infrastructure metadata, monitoring tables,
  deployment scaffolding

---

## PARSE PHASE

### P0 — Migration Step Registry

Produce a numbered registry of every step in this migration, in execution order:

| Step # | Operation | Target Table | Target Object (column / index / constraint) | Change Type |
|--------|-----------|--------------|---------------------------------------------|-------------|

Change Type must be exactly one of: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT
/ DROP CONSTRAINT / ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

DISQUALIFIER: Steps listed alphabetically by table rather than in execution order fails
C-05 (chronological ordering is satisfied by Phase B alone; this registry establishes the
canonical ordinal that all subsequent sections must cite).

At least two downstream sections must reference steps as "Step N from P0" to satisfy C-11.

### P0a — Constraint Type Registry

Enumerate every constraint type present in this migration. Complete this table before any
constraint analysis begins:

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

This registry is the binding manifest. A constraint type marked YES that later lacks a
dedicated Phase A field or a Phase B canonical table column is a manifest violation
(fails C-31 and C-32 simultaneously).

PARSE GATE (BINARY FIELD): OPEN / BLOCKED

Set to OPEN when P0 registry is complete (all steps numbered, Change Type populated) AND
P0a enumerates all four constraint types. Set to BLOCKED if either is incomplete.

---

## PHASE A -- INTERROGATION
## (Entry prerequisite: PARSE GATE (BINARY FIELD) = OPEN)
## If PARSE GATE = BLOCKED, complete PARSE PHASE before writing any Phase A content.

---

### PARITY ENFORCEMENT BLOCK

Every domain-role question (Q1, Q2, Q3) must apply the following checklist in full.
Violation of any item is an instruction violation, not a silent omission:

1. Before/After state per changed entity -- DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path identification -- apply to ALL steps, not just destructive ones
3. Constraint violation analysis with dedicated field per type -- DO NOT ROUTE ANY TYPE
   THROUGH A FREE-FORM FIELD
4. DEFAULT presence check for new NOT NULL columns -- DO NOT LIMIT TO FINANCIAL COLUMNS
5. Zero-downtime viability assessment -- apply to ALL domain roles, not Commerce only
6. Performance cliff detection -- DO NOT SCOPE TO ONE ROLE
7. Rollback viability classification per destructive step using fixed taxonomy
8. Idempotency check per step

Citation mandate (applies to all Q1 through Q3): Reference each affected step as
"Step N from P0" in every question. This instruction must appear in every question.

---

### Q1 -- Commerce Expert Analysis

**Role**: Commerce Expert -- order pipelines, catalog, pricing, SKU management.
**Citation**: Reference each affected step as "Step N from P0."

**A. Before/After State**
For each step in P0, state schema state before and after. Use exact type names, constraint
definitions, and index specifications.

DISQUALIFIER: "column type changed" without naming the old and new types fails C-01.

**B. Data Loss Path**
DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE

If YES or POSSIBLE: name the specific Step N from P0, the mechanism (silent truncation /
row drop / value cast without error / precision loss), and the condition under which data
is silently lost.

If NO: state the reasoning -- e.g., "Step 3 adds a nullable column with no data movement;
no data loss path exists."

**C. Constraint Violation Analysis**

For each constraint type marked YES in P0a, complete the corresponding field:

NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
-- If YES or PARTIAL: Step N from P0, table, column, estimated affected row count,
   migration response (fail / skip / backfill).

FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
-- If YES or PARTIAL: Step N from P0, FK name, parent table, orphaned-record condition,
   migration response.

UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
-- If YES or PARTIAL: Step N from P0, column, duplicate value scenario, migration response.

CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
-- If YES or PARTIAL: Step N from P0, CHECK expression, failing record condition,
   migration response.

DISQUALIFIER: Routing any constraint type through a free-form NOTES or DISRUPTION field
rather than the dedicated BINARY FIELD above fails C-28.

**D. DEFAULT Presence Check**
For every ADD COLUMN NOT NULL step in P0: does the migration supply a DEFAULT? Apply to
ALL new NOT NULL columns in ALL tables, not only order or commerce tables. Flag as
migration risk if DEFAULT is absent and table is non-empty.

**E. Zero-Downtime Viability**
Can this migration run without a maintenance window using online DDL or expand/contract
pattern? If not: name the specific Step N from P0 that requires a maintenance window and
the engine-level reason (table lock, replication pause, blocking DDL).

**F. Performance Cliff Detection**
Identify every Step N from P0 likely to cause a performance cliff (full-table rewrite,
index rebuild on wide table, type cast requiring row scan). For each: table name,
estimated row count if knowable, specific risk (lock duration / I/O spike / replication
lag amplification).

**G. Rollback Viability**
ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE) for each
destructive step (Step N from P0). Classify at least one step. "FULL" means a down
migration exists and is safe. "BACKUP-ONLY" means restoration requires a backup restore.
"IRREVERSIBLE" means the operation cannot be undone.

**H. Idempotency Check**
For each step in P0: safe to run twice? If not: name the specific failure mode
(duplicate key error / double-applied data transform / constraint re-add error /
orphaned trigger from re-run).

---

### Q2 -- Finance Expert Analysis

**Role**: Finance Expert -- ledger tables, transaction logs, audit trails, amount columns.
**Citation**: Reference each affected step as "Step N from P0."

Apply the complete checklist from the PARITY ENFORCEMENT BLOCK. All eight items are
required. Do not scope DEFAULT presence check to financial columns only. Do not scope
zero-downtime assessment to Commerce only.

**A. Before/After State**
[Same instruction as Q1 A -- full schema state, exact type names, all changed entities]

**B. Data Loss Path**
DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE
[Same instruction and binary field as Q1 B]

**C. Constraint Violation Analysis**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Same dedicated fields as Q1 C -- do not merge into free-form fields]

**D. DEFAULT Presence Check**
[Same instruction as Q1 D -- apply to ALL new NOT NULL columns, not financial only]

**E. Zero-Downtime Viability**
[Same instruction as Q1 E -- apply the assessment for the Finance role perspective]

**F. Performance Cliff Detection**
[Same instruction as Q1 F -- apply from Finance Expert lens: focus on audit table
row counts, ledger table lock contention under transaction load]

**G. Rollback Viability**
ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE) per destructive
step -- classify each Step N from P0 that drops, narrows, or transforms audit-critical
data.

**H. Idempotency Check**
[Same instruction as Q1 H -- focus on ledger double-apply and audit log re-insert risks]

---

### Q3 -- Operations Expert Analysis

**Role**: Operations Expert -- job queues, infrastructure metadata, monitoring tables.
**Citation**: Reference each affected step as "Step N from P0."

Apply the complete checklist from the PARITY ENFORCEMENT BLOCK. Do not scope zero-downtime
assessment to Commerce only. Do not limit DEFAULT checks to financial columns.

**A. Before/After State** [Same as Q1 A]

**B. Data Loss Path**
DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE
[Same as Q1 B -- focus on job queue row drops, monitoring metadata truncation]

**C. Constraint Violation Analysis**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL

**D. DEFAULT Presence Check** [Same as Q1 D -- ALL tables]

**E. Zero-Downtime Viability** [Same as Q1 E -- Operations lens: migration job scheduling,
rolling deploy compatibility, backward-compatible schema windows]

**F. Performance Cliff Detection** [Same as Q1 F -- Operations lens: monitoring table
scan impact, job queue index rebuild during peak processing]

**G. Rollback Viability**
ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)

**H. Idempotency Check** [Same as Q1 H -- job deduplication key risks, monitoring
counter double-apply]

---

TRACE GATE (BINARY FIELD): OPEN / BLOCKED

Set to OPEN when all three questions (Q1, Q2, Q3) are complete and every BINARY FIELD
carries a value. Set to BLOCKED if any field is unresolved. This gate guards Phase B.

---

## PHASE B -- CANONICAL OUTPUT
## (Entry prerequisite: TRACE GATE (BINARY FIELD) = OPEN)
## C-05 is satisfied by Phase B alone, not by any Phase A section.
## If TRACE GATE = BLOCKED, resolve all Phase A BINARY FIELD gaps before writing Phase B.

---

### B1 -- Canonical Execution Table

Produce a single execution-ordered table. Step # values must match P0 exactly.

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

Constraint-type columns must appear for every type enumerated in P0a regardless of
whether a violation exists. "N/A" is not a valid value for a constraint type marked YES
in P0a -- use NONE if no violation exists for this step.

DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED

Set to OPEN when B1 table is complete with all constraint-type columns populated.
Set to BLOCKED if any column is missing or any row has a blank constraint-type cell.

---

### B2 -- Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY -- complete before writing B3)
### (Entry prerequisite: DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN)

Apply at least one Commerce, Finance, or Operations lens. State a real-world consequence
of the migration risk in domain terms -- not just the schema-level change.

**Pre-seeded worked example** (model output -- not an instruction):
> Step 3 narrows payment_amount from decimal(19,4) to decimal(10,2) on the orders table.
> Before Step 3, all charges up to $9,999,999,999.9999 were stored exactly.
> After Step 3, any charge exceeding $9,999,999.99 is silently truncated to that ceiling.
> Before Step 3, the refund pipeline worked because payment_amount carried full
> precision and refund logic mirrored it exactly. After Step 3, that condition no longer
> holds because decimal(10,2) caps the representable amount. Specific consequence:
> refunds on orders over $9.99M are silently under-refunded with no error raised.

Apply the same three-part inertia-contrast structure for at least one step from B1:
(a) Before Step N, [process] worked because [condition].
(b) After Step N, [condition] no longer holds because [migration change].
(c) [Specific business consequence with numeric threshold or named metric.]

VERIFY GATE (BINARY FIELD): OPEN / BLOCKED

Set to OPEN when B2 contains at least one domain-framed risk with three-part
inertia-contrast structure. Set to BLOCKED if B2 contains only schema-level description.

---

### B3 -- Verification Checks
### (Entry prerequisite: VERIFY GATE (BINARY FIELD) = OPEN)

List at least one SQL verification query or check per data loss path found in B1.
Each check must reference "Step N from P0" and name the table and condition being
verified.

RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED

Set to OPEN when B3 contains at least one concrete verification query per data loss
path. Set to BLOCKED if verification is absent or generic.

---

### B4 -- Recommendations
### (Entry prerequisite: RECOMMENDATIONS GATE (BINARY FIELD) = OPEN)

Provide at least one concrete recommendation per destructive step classified as
BACKUP-ONLY or IRREVERSIBLE in B1. Reference "Step N from P0" in each recommendation.

VERDICT GATE (BINARY FIELD): OPEN / BLOCKED

Set to OPEN when B4 contains at least one recommendation per irreversible step.
Set to BLOCKED if any irreversible step from B1 is unaddressed.

---

### VERDICT
### (Entry prerequisite: VERDICT GATE (BINARY FIELD) = OPEN)

State: overall migration risk level (LOW / MEDIUM / HIGH / CRITICAL), count of data
loss paths, count of irreversible steps, and whether zero-downtime execution is viable.

---

---

## V-02 — Axis B: C-34 ENTRY REFERENCE Advisory

### Variation axis
ENTRY REFERENCE annotations at the top of succeeding phases are removed. Every phase
transition carries only an EXIT BLOCK at the bottom of the preceding phase with a
"(BINARY FIELD)" annotation. The gate state is declared once at the exit of each phase
rather than at both positions. All C-21, C-17, C-23, C-24, C-26 structural requirements
are preserved in full.

### Hypothesis
Removing the ENTRY REFERENCE from the top of each succeeding phase causes C-34 FAIL
while C-21 and C-17 remain PASS. Each gate is anchored only at the preceding phase's
exit, so a gate violation is visible only from the preceding phase's text -- not
detectable by reading the succeeding phase's opening alone. Predicted: 215/220.

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A
question. Available roles:

- **Commerce Expert** -- order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** -- ledger tables, transaction logs, audit trails, amount columns
- **Operations Expert** -- job queues, infrastructure metadata, monitoring tables

---

## PARSE PHASE

### P0 -- Migration Step Registry

Produce a numbered registry of every step in this migration, in execution order:

| Step # | Operation | Target Table | Target Object | Change Type |
|--------|-----------|--------------|---------------|-------------|

Change Type: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT / DROP CONSTRAINT /
ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

Reference all downstream steps as "Step N from P0."

### P0a -- Constraint Type Registry

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

Enumerate all four types. This is the binding manifest for Phase A fields and Phase B
canonical table columns.

---

### PARSE PHASE EXIT BLOCK (C-34 anchor -- exit side only)

> PARSE GATE (BINARY FIELD): OPEN / BLOCKED
>
> OPEN when: P0 Step Registry complete AND P0a enumerates all four constraint types.
> BLOCKED if either is incomplete.
> This gate guards entry to PHASE A INTERROGATION. Do not begin Phase A until OPEN.

---

## PHASE A -- INTERROGATION

---

### PARITY ENFORCEMENT BLOCK

Every domain-role question (Q1, Q2, Q3) must apply the following checklist:

1. Before/After state per changed entity -- DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path identification -- apply to ALL steps
3. Constraint violation analysis with dedicated BINARY FIELD per type -- DO NOT ROUTE
   ANY TYPE THROUGH A FREE-FORM FIELD
4. DEFAULT presence check for ALL new NOT NULL columns -- not financial columns only
5. Zero-downtime viability assessment -- apply to ALL domain roles
6. Performance cliff detection -- apply to ALL roles
7. Rollback viability per destructive step using fixed taxonomy
8. Idempotency check per step

Citation: Reference each affected step as "Step N from P0" in every question.

---

### Q1 -- Commerce Expert Analysis

**Role**: Commerce Expert.
**Citation**: Reference each affected step as "Step N from P0."

**A. Before/After State** -- exact type names, constraint definitions, index specs.

**B. Data Loss Path**
DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE
If YES or POSSIBLE: Step N from P0, mechanism, condition.
If NO: state reasoning.

**C. Constraint Violation Analysis**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
Each field: if YES or PARTIAL, name Step N from P0, affected table/column, migration
response.

**D. DEFAULT Presence Check** -- ALL new NOT NULL columns, ALL tables.

**E. Zero-Downtime Viability** -- can this run online? If not, Step N from P0 requiring
maintenance window and engine-level reason.

**F. Performance Cliff** -- Step N from P0, table, row count estimate, specific risk.

**G. Rollback Viability**
ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE) per destructive
step.

**H. Idempotency Check** -- per step, failure mode if not idempotent.

---

### Q2 -- Finance Expert Analysis

**Role**: Finance Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply full PARITY ENFORCEMENT BLOCK checklist. Do not scope to financial columns only.

**A. Before/After State** [full entity enumeration]
**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
**C.**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D. DEFAULT Presence Check** [ALL tables]
**E. Zero-Downtime Viability** [Finance lens: transaction log lock contention]
**F. Performance Cliff** [Finance lens: ledger table scan costs]
**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
**H. Idempotency Check** [ledger double-apply, audit log re-insert risks]

---

### Q3 -- Operations Expert Analysis

**Role**: Operations Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply full PARITY ENFORCEMENT BLOCK checklist.

**A. Before/After State** [full entity enumeration]
**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
**C.**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D. DEFAULT Presence Check** [ALL tables]
**E. Zero-Downtime Viability** [Operations lens: rolling deploy compatibility,
backward-compatible schema window]
**F. Performance Cliff** [Operations lens: job queue index rebuild during peak]
**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
**H. Idempotency Check** [job deduplication key risks]

---

### PHASE A EXIT BLOCK (C-34 anchor -- exit side only)

> TRACE GATE (BINARY FIELD): OPEN / BLOCKED
>
> OPEN when all three questions complete and every BINARY FIELD carries a value.
> BLOCKED if any field is unresolved.
> This gate guards Phase B. Do not write Phase B until TRACE GATE = OPEN.

---

## PHASE B -- CANONICAL OUTPUT
## C-05 is satisfied by Phase B alone, not by any Phase A section.

---

### B1 -- Canonical Execution Table

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

All four constraint-type columns required for types marked YES in P0a.

---

### DOMAIN SYNTHESIS GATE EXIT BLOCK (C-34 anchor -- exit side only)

> DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED
>
> OPEN when B1 table is complete. BLOCKED if any constraint-type column is missing.
> This gate guards B2. Do not write B2 until OPEN.

---

### B2 -- Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY -- complete before writing B3)

Apply at least one domain lens. Include a three-part inertia-contrast example:
(a) Before Step N, [process] worked because [condition].
(b) After Step N, [condition] no longer holds because [change].
(c) [Specific business consequence with numeric threshold.]

**Pre-seeded example**:
> Step 2 drops the fulfillment_date column from the shipments table.
> Before Step 2, the dispatch pipeline worked because fulfillment_date was the trigger
> condition for SLA-breach alerting (threshold: 48 hours post-order). After Step 2, that
> condition no longer holds because the column is absent. Consequence: all in-flight
> orders placed before migration lose their SLA-breach detection signal; breach events
> accumulate silently until the next monitoring reconciliation.

Also seed a second distinct inertia-contrast example naming a DIFFERENT step, table, or
consequence than the pre-seeded example above.

---

### VERIFY GATE EXIT BLOCK (C-34 anchor -- exit side only)

> VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
>
> OPEN when B2 contains at least one three-part inertia-contrast example with numeric
> threshold. BLOCKED if B2 contains only schema-level description.
> This gate guards B3.

---

### B3 -- Verification Checks

At least one SQL verification query per data loss path from B1. Each query must reference
"Step N from P0" and name the table and condition being verified.

---

### RECOMMENDATIONS GATE EXIT BLOCK (C-34 anchor -- exit side only)

> RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED
>
> OPEN when B3 contains at least one concrete verification query per data loss path.
> BLOCKED if verification is absent or generic.
> This gate guards B4.

---

### B4 -- Recommendations

At least one concrete recommendation per BACKUP-ONLY or IRREVERSIBLE step from B1.
Reference "Step N from P0."

---

### VERDICT GATE EXIT BLOCK (C-34 anchor -- exit side only)

> VERDICT GATE (BINARY FIELD): OPEN / BLOCKED
>
> OPEN when B4 addresses all irreversible steps. BLOCKED if any irreversible step is
> unaddressed.
> This gate guards VERDICT.

---

### VERDICT

Risk level (LOW / MEDIUM / HIGH / CRITICAL), data loss path count, irreversible step
count, zero-downtime viability verdict.

---

---

## V-03 — Axis C: BOUNDARY PROTOCOL Dual-Anchor Block

### Variation axis
Lifecycle emphasis: every phase boundary carries a named BOUNDARY PROTOCOL block
containing both EXIT BLOCK and ENTRY REFERENCE as explicit structural fields, both with
"(BINARY FIELD)" annotation. The block appears at the boundary itself -- after the last
content of the preceding phase and before the first content of the succeeding phase --
as a self-contained gate specification. Gate compliance is verifiable from either phase's
text without cross-referencing.

### Hypothesis
The BOUNDARY PROTOCOL block as a named artifact makes C-34 structurally explicit: the
block is present or absent as a named unit, making gate omission detectable by scanning
for BOUNDARY PROTOCOL headings rather than by reading both phase texts. This satisfies
C-34 and may generate a new excellence signal: BOUNDARY PROTOCOL as a first-class
structural artifact whose count equals the number of phase boundaries, making gate
coverage computable from protocol block count alone. Predicted: 220/220 + C-35 candidate.

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A
question. Available roles:

- **Commerce Expert** -- order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** -- ledger tables, transaction logs, audit trails, amount columns
- **Operations Expert** -- job queues, infrastructure metadata, monitoring tables

---

## PARSE PHASE

### P0 -- Migration Step Registry

Produce a numbered registry of every step in this migration, in execution order:

| Step # | Operation | Target Table | Target Object | Change Type |
|--------|-----------|--------------|---------------|-------------|

Change Type: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT / DROP CONSTRAINT /
ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

All downstream sections cite steps as "Step N from P0." At least two sections must cite
by Step N to satisfy C-11.

### P0a -- Constraint Type Registry

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

Binding manifest: every type marked YES must appear as a dedicated BINARY FIELD in Phase A
and as a named column in Phase B B1 canonical table.

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

---

## PHASE A -- INTERROGATION
### (PARSE GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL Parse-to-A)

---

### PARITY ENFORCEMENT BLOCK

Every domain-role question (Q1, Q2, Q3) must apply:

1. Before/After state per changed entity -- DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path identification -- ALL steps
3. Dedicated BINARY FIELD per constraint type -- DO NOT ROUTE THROUGH FREE-FORM FIELD
4. DEFAULT presence check -- ALL new NOT NULL columns in ALL tables
5. Zero-downtime viability -- ALL domain roles, not Commerce only
6. Performance cliff detection -- ALL roles
7. Rollback viability (fixed taxonomy) per destructive step
8. Idempotency check per step

Citation: Each question carries its own citation instruction: "Reference each affected
step as 'Step N from P0.'"

---

### Q1 -- Commerce Expert Analysis

**Role**: Commerce Expert.
**Citation**: Reference each affected step as "Step N from P0."

**A. Before/After State** -- exact type names, constraint definitions, index specs for
every changed entity. Generic descriptions without values fail C-01.

**B. Data Loss Path**
DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE
If YES or POSSIBLE: Step N from P0, mechanism, condition under which loss is silent.
If NO: state reasoning explicitly.

**C. Constraint Violation Analysis**

NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
-- YES/PARTIAL: Step N from P0, table, column, estimated affected rows, migration
   response (fail / skip / backfill / none).

FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
-- YES/PARTIAL: Step N from P0, FK name, parent table, orphan condition, response.

UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
-- YES/PARTIAL: Step N from P0, column, duplicate scenario, response.

CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
-- YES/PARTIAL: Step N from P0, CHECK expression, failing condition, response.

Do not route any constraint type through NOTES or DISRUPTION fields. Each type has its
own BINARY FIELD above.

**D. DEFAULT Presence Check**
Every ADD COLUMN NOT NULL step in P0: is DEFAULT supplied? Apply to ALL tables.
Flag as migration risk if DEFAULT absent and table is non-empty.

**E. Zero-Downtime Viability**
Can this migration run online (expand/contract, online DDL)? If not: Step N from P0
requiring maintenance window + engine-level reason (table lock / blocking DDL /
replication pause).

**F. Performance Cliff Detection**
Each Step N from P0 with full-table rewrite, index rebuild, or type cast requiring row
scan: table name, row count estimate, specific risk (lock duration / I/O spike /
replication lag).

**G. Rollback Viability**
ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE) for every
destructive step (Step N from P0). Classify at least one.

**H. Idempotency Check**
Per step: safe to run twice? If not: specific failure mode (duplicate key /
double-applied transform / constraint re-add error).

---

### Q2 -- Finance Expert Analysis

**Role**: Finance Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply the PARITY ENFORCEMENT BLOCK checklist in full. Do not scope DEFAULT checks to
financial columns only. Do not scope zero-downtime to Commerce role only.

**A. Before/After State** [full entity enumeration, same depth as Q1]

**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
[Focus: decimal precision loss on amount columns, ledger row truncation risks]
[If YES or POSSIBLE: Step N from P0, mechanism, condition]
[If NO: explicit reasoning]

**C. Constraint Violation Analysis**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: new NOT NULL constraints on transaction log columns, audit trail rows]
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: FK to parent ledger entries, orphaned transaction references]
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: unique transaction IDs, audit reference numbers]
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: amount range constraints, status enum constraints on financial records]
Each field: if YES or PARTIAL, Step N from P0 + table + column + response.

**D. DEFAULT Presence Check** [ALL tables, not financial columns only]

**E. Zero-Downtime Viability** [Finance lens: transaction log lock contention,
audit trail continuity during DDL]

**F. Performance Cliff** [Finance lens: ledger table full scan costs, audit log
index rebuild under write pressure]

**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
[Classify each destructive step from Finance perspective]

**H. Idempotency Check** [Ledger double-apply risk, audit log re-insert condition]

---

### Q3 -- Operations Expert Analysis

**Role**: Operations Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply the PARITY ENFORCEMENT BLOCK checklist in full.

**A. Before/After State** [full entity enumeration]

**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
[Focus: job queue row drops, monitoring metadata truncation, deployment record loss]

**C. Constraint Violation Analysis**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: new NOT NULL on job queue columns, infrastructure metadata tables]
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: FK from job records to parent workflow entities]
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: unique job IDs, monitoring metric keys]
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Focus: status enum constraints on job state machine columns]

**D. DEFAULT Presence Check** [ALL tables]

**E. Zero-Downtime Viability** [Operations lens: rolling deploy compatibility,
schema version backward compatibility window, job queue processing continuity]

**F. Performance Cliff** [Operations lens: job queue index rebuild during peak
processing, monitoring table scan during high-cardinality inserts]

**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**

**H. Idempotency Check** [Job deduplication key risks, monitoring counter
double-increment on replay]

---

### BOUNDARY PROTOCOL — A-to-B

```
EXIT BLOCK (bottom of PHASE A INTERROGATION):
  TRACE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: all three questions (Q1, Q2, Q3) complete and every BINARY FIELD carries
             a value (not blank, not placeholder).
  BLOCKED if: any analytical BINARY FIELD is unresolved.
  Guards: PHASE B CANONICAL OUTPUT.

ENTRY REFERENCE (top of PHASE B CANONICAL OUTPUT):
  TRACE GATE (BINARY FIELD) = OPEN required before writing any Phase B content.
  If BLOCKED: return to Phase A and resolve all unresolved BINARY FIELD gaps.
```

---

## PHASE B -- CANONICAL OUTPUT
### (TRACE GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL A-to-B)
### C-05 is satisfied by Phase B alone, not by any Phase A section.

---

### B1 -- Canonical Execution Table

Produce a single execution-ordered table. Step # must match P0 exactly.

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

All four constraint-type columns required for all types marked YES in P0a, even if no
violation exists for a given step (use NONE). BLANK is not valid.

---

### BOUNDARY PROTOCOL — B1-to-B2

```
EXIT BLOCK (bottom of B1):
  DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B1 table complete, all constraint-type columns populated.
  BLOCKED if: any column missing or any row has blank constraint-type cell.
  Guards: B2 DOMAIN SYNTHESIS.

ENTRY REFERENCE (top of B2 DOMAIN SYNTHESIS):
  DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: complete B1 before writing B2.
```

---

### B2 -- Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY -- complete before writing B3)
### (DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B1-to-B2)

Apply at least one domain lens. Name a real-world consequence in domain terms with a
numeric business threshold.

**Pre-seeded inertia-contrast example** (model output, not an instruction):
> Step 3 narrows unit_price from decimal(19,4) to decimal(10,2) on the products table.
> Before Step 3, the repricing pipeline worked because unit_price carried four decimal
> places and the bulk-discount calculation rounded at the final step. After Step 3, that
> condition no longer holds because decimal(10,2) rounds at storage, not at calculation.
> Consequence: bulk orders applying fractional-cent discounts accumulate a systematic
> underpayment of $0.001-$0.003 per line item; on a 50,000-line-item order, that is
> $50-$150 of billing drift per run with no error raised.

Seed a second distinct inertia-contrast example naming a DIFFERENT step, table, or
business consequence. The second example satisfies C-30 (dual-phase seeding):
> [Your second example here -- different Step N from P0 than used above]

---

### BOUNDARY PROTOCOL — B2-to-B3

```
EXIT BLOCK (bottom of B2):
  VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B2 contains at least two three-part inertia-contrast examples, each with
             a numeric threshold or named metric, naming distinct steps.
  BLOCKED if: B2 contains only schema-level description or only one example.
  Guards: B3 VERIFICATION.

ENTRY REFERENCE (top of B3 VERIFICATION):
  VERIFY GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: complete B2 domain synthesis before writing B3.
```

---

### B3 -- Verification Checks
### (VERIFY GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B2-to-B3)

At least one SQL verification query per data loss path from B1. Each query must
reference "Step N from P0" and name the table and condition:

Example: `SELECT COUNT(*) FROM orders WHERE amount > 9999999.99` -- verifies Step 3
truncation scope before migration.

---

### BOUNDARY PROTOCOL — B3-to-B4

```
EXIT BLOCK (bottom of B3):
  RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: at least one concrete verification query per data loss path in B1.
  BLOCKED if: verification section is absent or contains only generic descriptions.
  Guards: B4 RECOMMENDATIONS.

ENTRY REFERENCE (top of B4 RECOMMENDATIONS):
  RECOMMENDATIONS GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: add concrete verification queries before writing B4.
```

---

### B4 -- Recommendations
### (RECOMMENDATIONS GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B3-to-B4)

At least one concrete recommendation per BACKUP-ONLY or IRREVERSIBLE step from B1.
Reference "Step N from P0."

---

### BOUNDARY PROTOCOL — B4-to-VERDICT

```
EXIT BLOCK (bottom of B4):
  VERDICT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: every step classified BACKUP-ONLY or IRREVERSIBLE in B1 has a
             corresponding recommendation in B4.
  BLOCKED if: any irreversible step is unaddressed.
  Guards: VERDICT.

ENTRY REFERENCE (top of VERDICT):
  VERDICT GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: address all irreversible steps in B4 before writing VERDICT.
```

---

### VERDICT
### (VERDICT GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B4-to-VERDICT)

State: overall migration risk level (LOW / MEDIUM / HIGH / CRITICAL), data loss path
count, irreversible step count, zero-downtime viability verdict.

---

---

## V-04 — Axes C + D: BOUNDARY PROTOCOL + Inertia-First Framing

### Variation axis
Two axes combined:
- **C (lifecycle emphasis)**: all V-03 BOUNDARY PROTOCOL blocks preserved at every
  boundary.
- **D (inertia framing)**: a named STATUS QUO COST section precedes Phase A domain
  questions (before Q1), establishing the three-part inertia baseline before any
  role-specific analysis begins. The section names the current system state, the
  specific capability that will be disrupted, and the chronic accumulation cost if the
  migration is abandoned in favor of doing nothing.

### Hypothesis
Leading Phase A with an explicit STATUS QUO COST section forces inertia framing to be
established before the analytical questions are written, so Q1/Q2/Q3 examples anchor
back to a named prior condition rather than introducing it ad hoc. This may increase
inertia-contrast density in Phase A domain content and seed a richer Phase B B2 example.
Combined with V-03 BOUNDARY PROTOCOL, C-34 and C-27/C-30 signals should both improve.
Predicted: 220/220 + dual signal (C-35 BOUNDARY PROTOCOL count, C-36 STATUS QUO COST
as pre-commitment inertia anchor).

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A
question. Available roles:

- **Commerce Expert** -- order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** -- ledger tables, transaction logs, audit trails, amount columns
- **Operations Expert** -- job queues, infrastructure metadata, monitoring tables

---

## PARSE PHASE

### P0 -- Migration Step Registry

| Step # | Operation | Target Table | Target Object | Change Type |
|--------|-----------|--------------|---------------|-------------|

Change Type: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT / DROP CONSTRAINT /
ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

Citation anchor: All downstream sections cite steps as "Step N from P0."

### P0a -- Constraint Type Registry

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

---

### BOUNDARY PROTOCOL — Parse-to-A

```
EXIT BLOCK (bottom of PARSE PHASE):
  PARSE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: P0 complete AND P0a enumerates all four constraint types.
  BLOCKED if: either condition unmet.
  Guards: PHASE A INTERROGATION.

ENTRY REFERENCE (top of PHASE A INTERROGATION):
  PARSE GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: return to PARSE PHASE.
```

---

## PHASE A -- INTERROGATION
### (PARSE GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL Parse-to-A)

---

### STATUS QUO COST (pre-commitment inertia baseline -- complete before Q1)

Before writing Q1, establish the status quo: what the current system state is that makes
this migration necessary, and what the chronic accumulation cost is if the migration is
abandoned and the schema is left as-is.

**Required three-part structure**:
(a) **Current condition**: what specific schema state exists now that creates the risk
    (e.g., "payment_amount is decimal(10,2); amounts over $9,999,999.99 are already
    silently truncated at insert").
(b) **Process dependency**: what business process currently works despite this condition
    (e.g., "refund pipeline functions because no order in production has exceeded the
    cap to date").
(c) **Accumulation trajectory**: what chronic cost accumulates if the migration is
    abandoned (rate + horizon + named metric, e.g., "each quarter as transaction volumes
    grow, oversized-order risk accumulates per-order; unbounded without schema fix;
    metric: refund-discrepancy event count").

This section establishes the inertia-contrast baseline. Q1, Q2, and Q3 domain examples
should anchor back to this condition using the three-part structure:
"Before Step N, [process] worked because [this condition held]."

---

### PARITY ENFORCEMENT BLOCK

Every domain-role question (Q1, Q2, Q3) must apply:

1. Before/After state per changed entity -- DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path -- ALL steps
3. Dedicated BINARY FIELD per constraint type -- NO FREE-FORM ROUTING
4. DEFAULT presence check -- ALL new NOT NULL columns in ALL tables
5. Zero-downtime viability -- ALL domain roles
6. Performance cliff -- ALL roles
7. Rollback viability (fixed taxonomy)
8. Idempotency check

Citation: Each question carries its own instruction: "Reference each affected step as
'Step N from P0.'"

---

### Q1 -- Commerce Expert Analysis

**Role**: Commerce Expert.
**Citation**: Reference each affected step as "Step N from P0."

Ground at least one example in the STATUS QUO COST baseline above: "Before Step N,
[process] worked because [condition from STATUS QUO COST section]."

**A. Before/After State** [exact type names, constraint definitions, index specs]

**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
Step N from P0, mechanism, condition. Or explicit NO with reasoning.

**C. Constraint Violation Analysis**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
Each: Step N from P0 + table + column + response.

**D. DEFAULT Presence Check** [ALL tables]

**E. Zero-Downtime Viability** [can run online? If not: Step N from P0 + reason]

**F. Performance Cliff** [Step N from P0, table, row count, specific risk]

**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**

**H. Idempotency Check** [per step, failure mode]

---

### Q2 -- Finance Expert Analysis

**Role**: Finance Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply PARITY ENFORCEMENT BLOCK in full. Ground at least one example in the STATUS QUO
COST baseline.

**A. Before/After State** [full enumeration, ledger and audit focus]
**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
[Focus: decimal precision loss, ledger row truncation]
**C.**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D. DEFAULT Presence Check** [ALL tables]
**E. Zero-Downtime Viability** [Finance lens: transaction log lock]
**F. Performance Cliff** [Finance lens: ledger scan cost]
**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
**H. Idempotency Check** [double-apply risk on ledger]

---

### Q3 -- Operations Expert Analysis

**Role**: Operations Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply PARITY ENFORCEMENT BLOCK in full. Ground at least one example in STATUS QUO COST.

**A. Before/After State** [full enumeration, job queue and monitoring focus]
**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
**C.**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D. DEFAULT Presence Check** [ALL tables]
**E. Zero-Downtime Viability** [Operations: rolling deploy compatibility]
**F. Performance Cliff** [Operations: job queue rebuild during peak]
**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
**H. Idempotency Check** [job dedup key, monitoring counter re-apply]

---

### BOUNDARY PROTOCOL — A-to-B

```
EXIT BLOCK (bottom of PHASE A INTERROGATION):
  TRACE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: STATUS QUO COST section complete AND all three questions complete
             AND every BINARY FIELD carries a value.
  BLOCKED if: STATUS QUO COST incomplete or any BINARY FIELD unresolved.
  Guards: PHASE B CANONICAL OUTPUT.

ENTRY REFERENCE (top of PHASE B CANONICAL OUTPUT):
  TRACE GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: complete STATUS QUO COST and all Phase A questions first.
```

---

## PHASE B -- CANONICAL OUTPUT
### (TRACE GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL A-to-B)
### C-05 is satisfied by Phase B alone, not by any Phase A section.

---

### B1 -- Canonical Execution Table

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

All four constraint-type columns required for types marked YES in P0a.

---

### BOUNDARY PROTOCOL — B1-to-B2

```
EXIT BLOCK (bottom of B1):
  DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B1 complete with all constraint-type columns.
  BLOCKED if: any column missing.
  Guards: B2 DOMAIN SYNTHESIS.

ENTRY REFERENCE (top of B2):
  DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN required.
```

---

### B2 -- Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY -- complete before writing B3)
### (DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B1-to-B2)

Apply inertia-contrast framing anchored in the STATUS QUO COST baseline from Phase A.

**Example seeded for Phase B** (distinct from STATUS QUO COST example):
> Step 4 adds a NOT NULL column job_version INT to the migration_jobs table without a
> DEFAULT. Before Step 4, the job scheduler worked because all job records were
> insertable with the existing five columns; the scheduler's INSERT statement did not
> reference job_version. After Step 4, that condition no longer holds because any
> INSERT without job_version raises a constraint violation. Consequence: all in-flight
> migration jobs initiated before the schema change fail silently if the scheduler is
> not updated atomically with the DDL; job queue depth accumulates unboundedly until
> the scheduler is patched.

The B2 example must name a DIFFERENT step, table, or consequence than the STATUS QUO
COST example seeded in Phase A (satisfying C-30 dual-phase seeding requirement).

---

### BOUNDARY PROTOCOL — B2-to-B3

```
EXIT BLOCK (bottom of B2):
  VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B2 contains domain-framed risk grounded in STATUS QUO COST baseline,
             with three-part inertia-contrast structure and distinct step from Phase A.
  BLOCKED if: B2 repeats Phase A example or lacks numeric threshold.
  Guards: B3 VERIFICATION.

ENTRY REFERENCE (top of B3):
  VERIFY GATE (BINARY FIELD) = OPEN required.
```

---

### B3 -- Verification Checks
### (VERIFY GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B2-to-B3)

At least one SQL verification query per data loss path from B1. Each references
"Step N from P0" with table and condition.

---

### BOUNDARY PROTOCOL — B3-to-B4

```
EXIT BLOCK (bottom of B3):
  RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: at least one verification query per data loss path.
  BLOCKED if: absent or generic.
  Guards: B4 RECOMMENDATIONS.

ENTRY REFERENCE (top of B4):
  RECOMMENDATIONS GATE (BINARY FIELD) = OPEN required.
```

---

### B4 -- Recommendations
### (RECOMMENDATIONS GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B3-to-B4)

At least one concrete recommendation per BACKUP-ONLY or IRREVERSIBLE step. Reference
"Step N from P0." Include mitigation that addresses the STATUS QUO COST accumulation
trajectory if migration is abandoned.

---

### BOUNDARY PROTOCOL — B4-to-VERDICT

```
EXIT BLOCK (bottom of B4):
  VERDICT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: every irreversible step from B1 has a recommendation in B4.
  BLOCKED if: any irreversible step unaddressed.
  Guards: VERDICT.

ENTRY REFERENCE (top of VERDICT):
  VERDICT GATE (BINARY FIELD) = OPEN required.
```

---

### VERDICT
### (VERDICT GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B4-to-VERDICT)

Risk level (LOW / MEDIUM / HIGH / CRITICAL), data loss path count, irreversible step
count, zero-downtime viability, STATUS QUO COST trajectory summary.

---

---

## V-05 — Axes C + D + E: BOUNDARY PROTOCOL + Inertia-First + Operations-First Role Sequence

### Variation axis
Three axes combined:
- **C (lifecycle emphasis)**: all V-03 BOUNDARY PROTOCOL blocks at every boundary.
- **D (inertia framing)**: STATUS QUO COST section before Q1 (from V-04).
- **E (role sequence)**: Phase A role order reversed -- Operations Expert leads as Q1,
  Commerce Expert is Q2, Finance Expert is Q3. The STATUS QUO COST section is oriented
  toward infrastructure and operational risk first, then commerce and financial impact.

### Hypothesis
Operations-first ordering exposes the STATUS QUO COST baseline to an infrastructure lens
before commerce framing applies. When Operations is Q1, the inertia-contrast anchor is
established around job queue and schema version risk -- the conditions most likely to
affect the migration operator themselves -- before Commerce and Finance perspectives
add their layers. This may generate a richer three-part inertia example in Phase A Q1
(an Operations-grounded cause-level risk), a more distinct Phase B B2 example (Commerce
consequence derived from an infrastructure-level gap), and a potential new excellence
signal: cross-role inertia chain where the Phase A anchor role is Operations and the
Phase B synthesis role is Commerce -- creating a cross-role cause-consequence pair that
neither role section alone establishes. Predicted: 220/220 + three signals.

---

### Complete Prompt Body

You are a migration analyst. Declare your active role at the start of each Phase A
question. Available roles:

- **Operations Expert** -- job queues, infrastructure metadata, monitoring tables,
  deployment scaffolding
- **Commerce Expert** -- order pipelines, catalog tables, pricing, SKU inventory
- **Finance Expert** -- ledger tables, transaction logs, audit trails, amount columns

---

## PARSE PHASE

### P0 -- Migration Step Registry

| Step # | Operation | Target Table | Target Object | Change Type |
|--------|-----------|--------------|---------------|-------------|

Change Type: ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT / DROP CONSTRAINT /
ADD INDEX / DROP INDEX / DATA TRANSFORM / TABLE RENAME / TABLE DROP.

All downstream sections cite steps as "Step N from P0."

### P0a -- Constraint Type Registry

| Constraint Type | Present? (YES/NO) | Tables / Columns Affected |
|----------------|-------------------|---------------------------|
| NOT NULL | | |
| FK (Foreign Key) | | |
| UNIQUE | | |
| CHECK | | |

---

### BOUNDARY PROTOCOL — Parse-to-A

```
EXIT BLOCK (bottom of PARSE PHASE):
  PARSE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: P0 complete AND P0a enumerates all four constraint types.
  BLOCKED if: either condition unmet.
  Guards: PHASE A INTERROGATION.

ENTRY REFERENCE (top of PHASE A INTERROGATION):
  PARSE GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: return to PARSE PHASE.
```

---

## PHASE A -- INTERROGATION
### (PARSE GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL Parse-to-A)

---

### STATUS QUO COST (Operations-first framing -- complete before Q1)

Establish the status quo from an infrastructure perspective before any domain-role
analysis begins:

(a) **Current infrastructure condition**: what specific schema state creates operational
    risk (e.g., "migration_jobs.status is VARCHAR(20); the job scheduler accepts
    unconstrained status strings, allowing silent insertion of invalid state transitions").
(b) **Operational dependency**: what deployment process currently works despite this gap
    (e.g., "rolling deploys succeed because the scheduler validates status client-side
    before insert; schema-level constraint does not exist").
(c) **Infrastructure accumulation trajectory**: what accumulates if migration is
    abandoned (rate + horizon + metric, e.g., "per deploy, unconstrained status rows
    accumulate; unbounded without schema-level CHECK; metric: invalid-state-transition
    count per deployment cycle").

Q1 (Operations), Q2 (Commerce), Q3 (Finance) examples should anchor back to this
condition. Phase B B2 must seed a DIFFERENT step or consequence.

---

### PARITY ENFORCEMENT BLOCK

Every domain-role question (Q1, Q2, Q3) must apply:

1. Before/After state per changed entity -- DO NOT SCOPE TO SUBSET OF TABLES
2. Data loss path -- ALL steps
3. Dedicated BINARY FIELD per constraint type -- NO FREE-FORM ROUTING
4. DEFAULT presence check -- ALL new NOT NULL columns in ALL tables
5. Zero-downtime viability -- ALL domain roles
6. Performance cliff -- ALL roles
7. Rollback viability (fixed taxonomy)
8. Idempotency check

Citation: Each question carries: "Reference each affected step as 'Step N from P0.'"

---

### Q1 -- Operations Expert Analysis (leads Phase A)

**Role**: Operations Expert.
**Citation**: Reference each affected step as "Step N from P0."

Ground at least one example in the STATUS QUO COST baseline established above.

**A. Before/After State** [exact type names, constraint definitions, index specs,
all tables including job queues and monitoring]

**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
[Focus: job queue row drops on DELETE, monitoring metadata loss on column truncation,
deployment scaffolding record drops]
Step N from P0, mechanism, condition. Or NO with explicit reasoning.

**C. Constraint Violation Analysis**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
[Operations: new NOT NULL on job columns, infrastructure metadata rows]
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Operations: FK from job records to workflow parents, orphaned monitor references]
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Operations: job ID uniqueness, monitor key uniqueness]
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
[Operations: job state machine constraints, status enum validation]
Each: Step N from P0 + table + column + migration response.

**D. DEFAULT Presence Check** [ALL tables, not only job tables]

**E. Zero-Downtime Viability** [Operations lens: rolling deploy compatibility,
schema version backward-compat window, job scheduler compatibility during DDL]

**F. Performance Cliff** [Operations: job queue index rebuild during peak processing,
monitoring table scan during high-cardinality insert bursts]

**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
[Classify each destructive step; focus on job history and monitoring record loss]

**H. Idempotency Check** [Job deduplication key risks, monitoring counter double-apply
on replay, deployment scaffolding table re-run behavior]

---

### Q2 -- Commerce Expert Analysis

**Role**: Commerce Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply PARITY ENFORCEMENT BLOCK in full. Ground at least one example in the STATUS QUO
COST baseline established above (anchor to the infrastructure condition identified in
Q1 and show its commerce consequence).

**A. Before/After State** [full enumeration, catalog and order pipeline focus]
**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
[Commerce: silent truncation on price/amount columns, catalog row drops]
**C.**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D. DEFAULT Presence Check** [ALL tables]
**E. Zero-Downtime Viability** [Commerce: checkout pipeline continuity during DDL]
**F. Performance Cliff** [Commerce: catalog table full scan, order index rebuild]
**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
**H. Idempotency Check** [Double-submit risk on order tables, SKU re-insert]

---

### Q3 -- Finance Expert Analysis

**Role**: Finance Expert.
**Citation**: Reference each affected step as "Step N from P0."

Apply PARITY ENFORCEMENT BLOCK in full. Ground at least one example in STATUS QUO COST.

**A. Before/After State** [ledger and audit focus]
**B. DATA LOSS PATH (BINARY FIELD): YES / NO / POSSIBLE**
[Finance: decimal precision loss, audit trail truncation]
**C.**
NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
FK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
UNIQUE VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
CHECK VIOLATION RISK (BINARY FIELD): YES / NO / PARTIAL
**D. DEFAULT Presence Check** [ALL tables, not financial only]
**E. Zero-Downtime Viability** [Finance: transaction log lock, audit continuity]
**F. Performance Cliff** [Finance: ledger scan cost, audit log rebuild]
**G. ROLLBACK VIABILITY (fixed taxonomy: FULL / BACKUP-ONLY / IRREVERSIBLE)**
**H. Idempotency Check** [Ledger double-apply, audit log re-insert]

---

### BOUNDARY PROTOCOL — A-to-B

```
EXIT BLOCK (bottom of PHASE A INTERROGATION):
  TRACE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: STATUS QUO COST section complete (Operations framing) AND all three
             questions (Q1 Operations, Q2 Commerce, Q3 Finance) complete AND every
             BINARY FIELD carries a value.
  BLOCKED if: STATUS QUO COST incomplete or any BINARY FIELD unresolved.
  Guards: PHASE B CANONICAL OUTPUT.

ENTRY REFERENCE (top of PHASE B CANONICAL OUTPUT):
  TRACE GATE (BINARY FIELD) = OPEN required.
  If BLOCKED: complete STATUS QUO COST (Operations) and all Phase A questions first.
```

---

## PHASE B -- CANONICAL OUTPUT
### (TRACE GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL A-to-B)
### C-05 is satisfied by Phase B alone, not by any Phase A section.

---

### B1 -- Canonical Execution Table

| Step # | Operation | Before State | After State | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Rollback Viability |
|--------|-----------|-------------|-------------|--------------------------|------------------------------|-----------------------------|---------------------------------|--------------------------------|--------------------|

All four constraint-type columns required for types marked YES in P0a.

---

### BOUNDARY PROTOCOL — B1-to-B2

```
EXIT BLOCK (bottom of B1):
  DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B1 complete, all constraint-type columns populated.
  BLOCKED if: any column missing.
  Guards: B2 DOMAIN SYNTHESIS.

ENTRY REFERENCE (top of B2):
  DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN required.
```

---

### B2 -- Domain Synthesis
### (POSITIONED BEFORE B3 VERIFY -- complete before writing B3)
### (DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B1-to-B2)

Seed inertia-contrast example grounded in the Operations-first STATUS QUO COST
baseline, expressed through the Commerce or Finance consequence:

**Cross-role inertia chain example** (Operations cause -> Commerce consequence):
> The STATUS QUO COST established in Phase A identified that job_version NOT NULL
> constraint is absent from migration_jobs (Step 4). Before Step 4, the order dispatch
> pipeline worked because the scheduler inserted job records without job_version and
> orders were fulfilled in FIFO sequence. After Step 4, that condition no longer holds
> because job_version = NULL violates the new constraint, causing dispatcher INSERT
> failures on any node not yet running the updated scheduler. Consequence: orders
> placed during the rolling deploy window are silently queued without dispatch; at
> 200 orders/minute over a 5-minute rolling window, 1,000 orders accumulate in the
> stalled dispatch queue with no customer notification.

The B2 example must name a DIFFERENT step or consequence than the STATUS QUO COST
example in Phase A.

Seed a second distinct inertia-contrast example (Finance consequence from a different
step, satisfying C-30):
> [Second example here -- different Step N from P0]

---

### BOUNDARY PROTOCOL — B2-to-B3

```
EXIT BLOCK (bottom of B2):
  VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: B2 contains at least one cross-role inertia chain (Operations cause ->
             Commerce or Finance consequence) with numeric threshold, PLUS a second
             distinct example from a different step.
  BLOCKED if: B2 lacks cross-role framing or numeric threshold.
  Guards: B3 VERIFICATION.

ENTRY REFERENCE (top of B3):
  VERIFY GATE (BINARY FIELD) = OPEN required.
```

---

### B3 -- Verification Checks
### (VERIFY GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B2-to-B3)

At least one SQL verification query per data loss path from B1. Each references
"Step N from P0" with table and condition.

---

### BOUNDARY PROTOCOL — B3-to-B4

```
EXIT BLOCK (bottom of B3):
  RECOMMENDATIONS GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: at least one verification query per data loss path.
  BLOCKED if: absent or generic.
  Guards: B4 RECOMMENDATIONS.

ENTRY REFERENCE (top of B4):
  RECOMMENDATIONS GATE (BINARY FIELD) = OPEN required.
```

---

### B4 -- Recommendations
### (RECOMMENDATIONS GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B3-to-B4)

At least one recommendation per BACKUP-ONLY or IRREVERSIBLE step. Reference "Step N
from P0." Include at least one recommendation that addresses the cross-role inertia
chain identified in B2 (the Operations-cause consequence seeded there).

---

### BOUNDARY PROTOCOL — B4-to-VERDICT

```
EXIT BLOCK (bottom of B4):
  VERDICT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: every irreversible step from B1 has a recommendation in B4, AND the
             cross-role inertia chain from B2 has a mitigation.
  BLOCKED if: any irreversible step or B2 cross-role chain is unaddressed.
  Guards: VERDICT.

ENTRY REFERENCE (top of VERDICT):
  VERDICT GATE (BINARY FIELD) = OPEN required.
```

---

### VERDICT
### (VERDICT GATE (BINARY FIELD) = OPEN -- confirmed at BOUNDARY PROTOCOL B4-to-VERDICT)

Risk level (LOW / MEDIUM / HIGH / CRITICAL), data loss path count, irreversible step
count, zero-downtime viability verdict, STATUS QUO COST accumulation trajectory summary
(Operations-grounded, Commerce/Finance consequence stated).
