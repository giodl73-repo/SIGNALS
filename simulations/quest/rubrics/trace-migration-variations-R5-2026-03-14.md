# trace-migration — Round 5 Variations (v5 rubric)

**New criteria this round:** C-19 (per-section citation repetition), C-20 (domain header completion constraint), C-21 (complete phase gate chain), C-22 (pre-seeded inline domain example)

**R4 baseline:** V-01 / V-04 / V-05 scored 140/140; V-02 / V-03 failed C-05 (single-phase). All R5 variations use two-phase structure to preserve C-05 / C-16.

---

## Variation Summary

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Role sequence (Ops → Finance → Commerce) | Operations-first surfaces FK/NOT NULL violations before precision loss; cascading gates enforce ordering with C-21 complete chain |
| V-02 | Output format (labeled prose blocks) | Prose blocks prevent sparse table-cell answers and make domain consequence omission visible; C-22 example flows naturally in narrative |
| V-03 | Lifecycle emphasis (5-gate two-phase) | Five lifecycle phases (PARSE → TRACE → DOMAIN → OPERATIONAL → VERIFY) each gated by a binary gate, then Phase B synthesis — cleanest C-21 complete chain architecture |
| V-04 | Role sequence + phrasing register (Finance-first, terse imperative) | Finance-first catches silent monetary truncation before constraint cascades; imperative register eliminates hedging, making each instruction non-optional |
| V-05 | Lifecycle emphasis + phrasing register + inertia framing (conversational, multi-gate) | Conversational scenario questions ("what happens to a $250,000 settlement?") trigger richer domain reasoning than instruction templates; inertia framing tests status-quo cost |

---

## V-01 — Single-Axis: Role Sequence (Operations → Finance → Commerce)

**Axis:** Role sequence only. Structure follows R4 V-01 two-phase pattern. Gates chain through every Q-to-Q transition for C-21 compliance.

**Hypothesis:** Leading with Operations analysis (constraint integrity, FK violations, NOT NULL risks) before Finance (precision loss) before Commerce (uniqueness) surfaces the most dangerous migration failures first, because operational failures cascade downstream. Tests ordering only.

---

```
You are an Operations, Finance, and Commerce migration expert — in that order of analysis.
You have been given a schema migration. Produce a structured migration trace.

## PHASE A — INTERROGATIVE ANALYSIS

Organize by concern. Phase B synthesizes the execution-ordered authoritative output.

---

### Q1 — MIGRATION STEP REGISTRY  *(NAMED ARTIFACT)*

List every migration step in execution order. Assign Step 1, Step 2, … . For each:
- Step number
- Operation type (ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD CONSTRAINT /
  DROP INDEX / CREATE TABLE / …)
- Target (schema.table.column or schema.table)
- One-line description

*This is the Q1 STEP REGISTRY. Every subsequent question cites steps as
"Step N from Q1." No other citation form is acceptable.*

---

### Q2 — OPERATIONS: Constraint and Integrity Analysis
*(Reference each affected step as "Step N from Q1")*

You are the Operations migration expert. For each step from Q1 that changes a
NOT NULL constraint, FK, CHECK, UNIQUE, or DEFAULT:

- Step N from Q1:
  - Before state: constraint definition
  - After state: constraint definition after this step
  - Does existing data satisfy the new constraint? YES / NO / UNKNOWN
  - Migration action if not: FAIL / SKIP / BACKFILL / N/A
  - **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**
    - If AT RISK: table, column, row count estimate, DEFAULT provided (YES / NO),
      backfill value required
  - **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
    - If not NONE: column, what is lost, whether it is silent

**OPERATIONS GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every constraint change analyzed, no unresolved AT RISK without backfill plan.
BLOCKED: any NOT NULL AT RISK or REJECTION with no migration action.
*Q3 requires OPERATIONS GATE = OPEN.*

---

### Q3 — FINANCE: Precision and Monetary Risk
*(Requires OPERATIONS GATE = OPEN. Reference each affected step as "Step N from Q1")*

You are the Finance migration expert. For each step from Q1 that changes a numeric
type, precision, scale, or monetary column:

- Step N from Q1:
  - Before state: type(precision, scale), nullability
  - After state: type after this step
  - **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
    - If TRUNCATION: column, old precision, new precision, dollar threshold where
      truncation begins silently
  - **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**

If no precision changes: write "NONE — confirmed no monetary impact."

**FINANCE GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every precision change has a named dollar threshold or confirmed NONE.
BLOCKED: any numeric type change without a concrete business-impact threshold.
*Q4 requires FINANCE GATE = OPEN.*

---

### Q4 — COMMERCE: Uniqueness, Deduplication, and Catalog Integrity
*(Requires FINANCE GATE = OPEN. Reference each affected step as "Step N from Q1")*

You are the Commerce migration expert. For each step from Q1 that changes a UNIQUE
index, primary key, or order/SKU identifier:

- Step N from Q1:
  - Before state: uniqueness guarantee
  - After state: uniqueness guarantee after this step
  - Can two products share the same SKU? YES / NO / UNKNOWN
  - Can an order be double-charged? YES / NO / UNKNOWN
  - **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
  - **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**

If no uniqueness changes: write "NONE — confirmed no catalog impact."

**COMMERCE GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every uniqueness change assessed, no unresolved SKU collision or double-charge risk.
BLOCKED: any open YES / UNKNOWN on double-charge or SKU collision without mitigation.
*Q5 requires COMMERCE GATE = OPEN.*

---

### Q5 — DOMAIN IMPACT SUMMARY
*(Requires COMMERCE GATE = OPEN.*
***POSITIONED BEFORE Q7 VERIFY — complete this section before writing Q7.***
*Reference each affected step as "Step N from Q1")*

Synthesize the three domain perspectives into a business consequence table.

**Pre-seeded example — model output text:**
> Step 3 from Q1 narrows `transactions.payment_amount` from `decimal(19,4)` to
> `decimal(10,2)`.
> — Operations: existing `pending_refund` rows with `amount > 99999999.99` fail
>   reinsertion under the new column type. Backfill required before migration. ~14 rows.
> — Finance: any charge or refund exceeding $99,999,999.99 is silently capped at that
>   value. A $250,000 settlement posts as $99,999,999.99 with no error raised.
> — Commerce: no SKU or order deduplication impact on this step.

For each step from Q1 that carries a domain consequence:

| Step (from Q1) | Operations Consequence | Finance Consequence (threshold) | Commerce Consequence |
|----------------|----------------------|---------------------------------|----------------------|
| Step N         | …                    | …                               | …                    |

If a domain has no consequence for a step, write "NONE — confirmed no
business-object impact."

**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every step has a consequence or explicit NONE for all three domains.
BLOCKED: any step with DATA LOSS ≠ NONE or NOT NULL AT RISK has no domain
consequence named.
*Q6 and Phase B require DOMAIN GATE = OPEN.*

---

### Q6 — PERFORMANCE, ROLLBACK, AND EXECUTION RISK
*(Requires DOMAIN GATE = OPEN. Reference each affected step as "Step N from Q1")*

For each step from Q1:
- **PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT**
  - If PRESENT: table, operation, estimated row count, risk type
    (LOCK_DURATION / IO_SPIKE / REPLICATION_LAG)
- **ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY):
  FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE**
  - If BACKUP_ONLY or IRREVERSIBLE: failure mode on re-run
- **ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
  - If NO or PARTIAL: step from Q1 requiring maintenance window
- **IDEMPOTENT (BINARY FIELD): YES / NO**
  - If NO: failure mode on re-run (duplicate key, double-apply, etc.)

**EXECUTION GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all four fields stated for every step, no IRREVERSIBLE step without
acknowledgment.
BLOCKED: any blank field or IRREVERSIBLE step without explicit plan.
*Q7 requires EXECUTION GATE = OPEN.*

---

### Q7 — VERIFY CHECKLIST
*(Requires EXECUTION GATE = OPEN. Reference each affected step as "Step N from Q1")*

- [ ] All steps from Q1 have DATA LOSS (BINARY FIELD) values — no blank cells
- [ ] All NOT NULL AT RISK entries have backfill plans stated
- [ ] All IRREVERSIBLE steps are acknowledged with owner noted
- [ ] OPERATIONS GATE = OPEN
- [ ] FINANCE GATE = OPEN
- [ ] COMMERCE GATE = OPEN
- [ ] DOMAIN GATE = OPEN
- [ ] EXECUTION GATE = OPEN

**VERIFY GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all checklist items pass.
BLOCKED: any item unchecked.
*Phase B requires VERIFY GATE = OPEN.*

---

## PHASE B — CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)
*(Requires VERIFY GATE = OPEN. This is the execution-ordered authoritative output.)*

### B1 — Step-by-Step Migration Trace

One row per step from Q1, in execution order. No reordering. No blank cells.

| Step (from Q1) | Entity | Before State | Operation | After State |
  DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) |
  ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY) |
  PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |

### B2 — Domain Impact Registry
*(Source: Q5 domain consequence table)*

| Step (from Q1) | Operations Consequence | Finance Consequence (threshold) | Commerce Consequence |

### B3 — Migration Verdict

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS — confirmed no rows, values, or columns silently dropped or truncated
- [ ] DATA LOSS PRESENT — at least one path exists (see B1 DATA LOSS column)
- [ ] DATA LOSS CONDITIONAL — depends on runtime data values (specify condition)

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
If NO or PARTIAL: step from Q1 requiring maintenance window: __________

**VERDICT GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: DATA LOSS = NO DATA LOSS or DATA LOSS CONDITIONAL with mitigations listed,
      and all IRREVERSIBLE steps acknowledged.
BLOCKED: DATA LOSS PRESENT with no mitigation plan, or any IRREVERSIBLE step
         unacknowledged.
Migration proceeds only when VERDICT GATE = OPEN.
```

---

## V-02 — Single-Axis: Output Format (Labeled Prose Blocks)

**Axis:** Output format only. Role order (Ops → Finance → Commerce) and gate chain held constant from V-01.

**Hypothesis:** Replacing question tables with labeled prose blocks forces more connected analytical reasoning — a prose block cannot be silently left sparse the way a table cell can. The evaluator can see when a paragraph says nothing. C-22's pre-seeded domain example integrates naturally in narrative prose. Tests format only.

---

```
You are an Operations, Finance, and Commerce migration expert. You have been given a
schema migration. Produce a structured migration trace.

## PHASE A — ANALYTICAL TRACE

Write Phase A as labeled prose blocks with inline binary fields. Phase B synthesizes
the step-ordered authoritative output.

---

**STEP REGISTRY  (NAMED ARTIFACT)**
*(All Phase A and Phase B step references use "Step N from STEP REGISTRY")*

Write every migration step in execution order, numbered Step 1, Step 2, … . For each
step: operation type, target entity, one-line description. Do not reorder. This list
is the STEP REGISTRY — the authoritative citation source for all step references.

---

**OPERATIONS ANALYSIS**
*(Reference each affected step as "Step N from STEP REGISTRY")*

Write a prose block for each step from STEP REGISTRY that touches a constraint (NOT
NULL, FK, CHECK, UNIQUE, DEFAULT). For each, state: the constraint before, the
constraint after Step N from STEP REGISTRY, whether existing data satisfies the new
constraint (YES / NO / UNKNOWN), and the migration action if it does not
(FAIL / SKIP / BACKFILL / N/A).

Within each block, state:
- **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A** — if AT RISK: table,
  column, row count, DEFAULT provided (YES / NO), backfill value
- **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION** — if not
  NONE: what is lost and whether it is silent

Close this section with:
**OPERATIONS GATE (BINARY FIELD): OPEN / BLOCKED**
Open: all constraint changes analyzed, no unresolved AT RISK without backfill plan.
Blocked: any NOT NULL AT RISK or REJECTION without a migration action.
*FINANCE ANALYSIS requires OPERATIONS GATE = OPEN.*

---

**FINANCE ANALYSIS**
*(Requires OPERATIONS GATE = OPEN.
Reference each affected step as "Step N from STEP REGISTRY")*

Write a prose block for each step from STEP REGISTRY that changes a numeric type,
precision, or scale. For each, state: the old type with precision and scale, the new
type after Step N from STEP REGISTRY, and the exact dollar threshold at which values
are silently affected.

Within each block, state:
- **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
- **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**

If no precision changes: write "NONE — confirmed no monetary impact in this migration."

Close with:
**FINANCE GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every precision change has a named dollar threshold or confirmed NONE.
Blocked: any numeric type change without a concrete dollar threshold.
*COMMERCE ANALYSIS requires FINANCE GATE = OPEN.*

---

**COMMERCE ANALYSIS**
*(Requires FINANCE GATE = OPEN.
Reference each affected step as "Step N from STEP REGISTRY")*

Write a prose block for each step from STEP REGISTRY that changes a UNIQUE constraint,
primary key, or order/SKU identifier. State: the uniqueness guarantee before, the
guarantee after Step N from STEP REGISTRY, whether two products can share a SKU
(YES / NO / UNKNOWN), and whether an order can be double-charged (YES / NO / UNKNOWN).

Within each block, state:
- **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
- **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**

If no uniqueness changes: write "NONE — confirmed no catalog or deduplication impact."

Close with:
**COMMERCE GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every uniqueness change assessed, no unresolved collision or double-charge risk.
Blocked: any open YES or UNKNOWN on SKU collision or double-charge without mitigation.
*DOMAIN IMPACT requires COMMERCE GATE = OPEN.*

---

**DOMAIN IMPACT**
*(Requires COMMERCE GATE = OPEN.*
***POSITIONED BEFORE VERIFY CHECKLIST — complete this section before writing
VERIFY CHECKLIST.***
*Reference each affected step as "Step N from STEP REGISTRY")*

**Pre-seeded example — model output text:**
> Step 3 from STEP REGISTRY narrows `transactions.payment_amount` from
> `decimal(19,4)` to `decimal(10,2)`. This has three domain consequences.
>
> Operations: existing rows in `pending_refund` where `amount > 99999999.99`
> fail reinsertion under the new column type — approximately 14 rows at risk.
> A backfill capping values before migration is required.
>
> Finance: any invoice, refund, or charge above $99,999,999.99 is silently
> truncated to $99,999,999.99 with no error raised. A $250,000 enterprise
> settlement appears as $99,999,999.99 in the ledger. Monthly close totals
> are wrong for any account at that scale.
>
> Commerce: no order deduplication or SKU uniqueness impact on this step.

Write one prose paragraph per step from STEP REGISTRY that carries a domain
consequence. State Operations, Finance, and Commerce impact explicitly. For each
domain with no consequence, write "no impact."

Close with:
**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every step has domain consequences or explicit NONE for all three domains.
Blocked: any step with DATA LOSS ≠ NONE or NOT NULL AT RISK without a domain
consequence named.
*EXECUTION RISK and Phase B require DOMAIN GATE = OPEN.*

---

**EXECUTION RISK**
*(Requires DOMAIN GATE = OPEN.
Reference each affected step as "Step N from STEP REGISTRY")*

Write a prose block for each step from STEP REGISTRY. For each, state:
- **PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT** — if PRESENT: table,
  operation, estimated row count, risk type
- **ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY):
  FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE** — if BACKUP_ONLY or IRREVERSIBLE:
  failure mode on re-run
- **ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL** — if NO or PARTIAL:
  step from STEP REGISTRY requiring maintenance window
- **IDEMPOTENT (BINARY FIELD): YES / NO** — if NO: failure mode on re-run

Close with:
**EXECUTION GATE (BINARY FIELD): OPEN / BLOCKED**
Open: all four fields stated for every step, no IRREVERSIBLE step without plan.
Blocked: any field omitted or IRREVERSIBLE step without explicit acknowledgment.
*VERIFY CHECKLIST requires EXECUTION GATE = OPEN.*

---

**VERIFY CHECKLIST**
*(Requires EXECUTION GATE = OPEN.
Reference each affected step as "Step N from STEP REGISTRY")*

- [ ] Every step from STEP REGISTRY has DATA LOSS (BINARY FIELD) stated — no omissions
- [ ] Every NOT NULL AT RISK entry has a backfill plan stated
- [ ] Every IRREVERSIBLE step has owner acknowledgment noted
- [ ] OPERATIONS GATE = OPEN
- [ ] FINANCE GATE = OPEN
- [ ] COMMERCE GATE = OPEN
- [ ] DOMAIN GATE = OPEN
- [ ] EXECUTION GATE = OPEN

**VERIFY GATE (BINARY FIELD): OPEN / BLOCKED**
Open: all checklist items pass.
Blocked: any item unchecked.
*Phase B requires VERIFY GATE = OPEN.*

---

## PHASE B — CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)
*(Requires VERIFY GATE = OPEN. Execution-ordered, one row per step from STEP REGISTRY.
No blank cells.)*

### B1 — Step-by-Step Migration Trace

| Step (from STEP REGISTRY) | Entity | Before State | Operation | After State |
  DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) |
  ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY) |
  PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |

### B2 — Domain Consequence Summary
*(Source: DOMAIN IMPACT prose blocks)*

| Step (from STEP REGISTRY) | Operations Consequence | Finance Consequence (threshold) | Commerce Consequence |

### B3 — Migration Verdict

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS — confirmed
- [ ] DATA LOSS PRESENT — at least one path (see B1)
- [ ] DATA LOSS CONDITIONAL — depends on runtime data (specify condition)

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**

**VERDICT GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: DATA LOSS = NO DATA LOSS or DATA LOSS CONDITIONAL with mitigations,
      and all IRREVERSIBLE steps acknowledged.
BLOCKED: DATA LOSS PRESENT without mitigation, or any IRREVERSIBLE step unacknowledged.
Migration proceeds only when VERDICT GATE = OPEN.
```

---

## V-03 — Single-Axis: Lifecycle Emphasis (5-Gate Two-Phase)

**Axis:** Lifecycle phase structure only. Adds Phase B to fix R4 V-03's C-05 failure while preserving its 5-gate C-21 architecture.

**Hypothesis:** A 5-phase lifecycle structure (PARSE → TRACE → DOMAIN IMPACT → OPERATIONAL RISK → VERIFY) with a named binary gate at every lifecycle boundary, followed by Phase B as canonical synthesis, achieves full C-21 compliance with the cleanest possible gate chain. Each phase transition is explicit and named in the subsequent phase header. Tests lifecycle granularity only.

---

```
You are a Commerce, Finance, and Operations migration expert. You have been given a
schema migration. Produce a structured migration trace across five analysis phases,
then synthesize.

## PHASE A — FIVE-PHASE ANALYSIS

---

### PARSE PHASE
*(Step citation: all subsequent phases cite steps as "Step N from PARSE PHASE REGISTRY")*

**PARSE PHASE REGISTRY  (NAMED ARTIFACT):**
List every migration step in execution order. Assign Step 1, Step 2, … . For each:
operation type, target entity (schema.table.column or schema.table), one-line
description.

*This is the PARSE PHASE REGISTRY. Do not reorder. Every phase below cites steps as
"Step N from PARSE PHASE REGISTRY."*

**PARSE GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every step numbered and described.
BLOCKED: any step without an operation type or target.
*TRACE PHASE requires PARSE GATE = OPEN.*

---

### TRACE PHASE
*(Requires PARSE GATE = OPEN.
Reference each affected step as "Step N from PARSE PHASE REGISTRY")*

For each step from PARSE PHASE REGISTRY, trace the entity state:
- Step N from PARSE PHASE REGISTRY:
  - Before state: type, nullability, constraint, value range (if knowable)
  - After state: what changes after this step
  - **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
    - If not NONE: column, what is lost, whether it is silent
  - **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**
    - If AT RISK: table, column, row count estimate, DEFAULT provided (YES / NO),
      required backfill value
  - Constraint change (if any): Before constraint / After constraint /
    Data satisfies new constraint (YES / NO / UNKNOWN) /
    Migration action (FAIL / SKIP / BACKFILL / N/A)

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS — confirmed no rows, values, or columns silently affected
- [ ] DATA LOSS PRESENT — at least one path identified above
- [ ] DATA LOSS CONDITIONAL — depends on runtime data values (specify)

**TRACE GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every step has DATA LOSS and NOT NULL RISK stated; DATA LOSS STATEMENT checked.
BLOCKED: any step missing either field or DATA LOSS STATEMENT unchecked.
*DOMAIN IMPACT PHASE requires TRACE GATE = OPEN.*

---

### DOMAIN IMPACT PHASE
*(Requires TRACE GATE = OPEN.*
***POSITIONED BEFORE VERIFY PHASE — complete this section before writing VERIFY PHASE.***
*Reference each affected step as "Step N from PARSE PHASE REGISTRY")*

Apply Commerce, Finance, and Operations lenses to the trace findings.

**Pre-seeded example — model output text:**
> Step 3 from PARSE PHASE REGISTRY changes `transactions.payment_amount` from
> `decimal(19,4)` to `decimal(10,2)`.
>
> **Commerce:** No SKU or order uniqueness impact on this step. No double-charge risk.
>
> **Finance:** Charges and refunds above $99,999,999.99 are silently capped at that
> value. A $250,000 settlement appears as $99,999,999.99 in the ledger with no error
> raised. Any batch settlement file containing values above that threshold produces
> systematically wrong totals — with no signal to the operator.
>
> **Operations:** Existing `pending_refund` rows where `amount > 99999999.99` fail
> reinsertion under the new column type. Approximately 14 rows at risk. A pre-migration
> backfill capping those values is required before executing Step 3.

For each step from PARSE PHASE REGISTRY with a DATA LOSS, NOT NULL RISK, or
constraint change:

| Step (from PARSE PHASE REGISTRY) | Commerce Impact | Finance Impact (threshold) | Operations Impact |
|----------------------------------|-----------------|---------------------------|-------------------|

For steps with no domain consequence, write "NONE — confirmed no business-object
impact for any domain."

**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every step with a trace finding has a domain consequence or explicit NONE.
BLOCKED: any DATA LOSS or NOT NULL AT RISK step without a domain consequence named.
*OPERATIONAL RISK PHASE requires DOMAIN GATE = OPEN.*

---

### OPERATIONAL RISK PHASE
*(Requires DOMAIN GATE = OPEN.
Reference each affected step as "Step N from PARSE PHASE REGISTRY")*

For each step from PARSE PHASE REGISTRY:
- **PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT**
  - If PRESENT: table, operation, estimated row count,
    risk type (LOCK_DURATION / IO_SPIKE / REPLICATION_LAG)
- **ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY):
  FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE**
  - If BACKUP_ONLY or IRREVERSIBLE: failure mode on re-run
- **ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
  - If NO or PARTIAL: step from PARSE PHASE REGISTRY requiring maintenance window
- **IDEMPOTENT (BINARY FIELD): YES / NO**
  - If NO: failure mode on re-run (duplicate key, double-applied transform, etc.)

**OPERATIONAL GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all four fields stated for every step, no IRREVERSIBLE step without
acknowledgment.
BLOCKED: any field omitted, or IRREVERSIBLE step without explicit plan.
*VERIFY PHASE requires OPERATIONAL GATE = OPEN.*

---

### VERIFY PHASE
*(Requires OPERATIONAL GATE = OPEN.
Reference each affected step as "Step N from PARSE PHASE REGISTRY")*

- [ ] Every step from PARSE PHASE REGISTRY has DATA LOSS (BINARY FIELD) stated
- [ ] Every step from PARSE PHASE REGISTRY has NOT NULL RISK (BINARY FIELD) stated
- [ ] DATA LOSS STATEMENT checked in TRACE PHASE
- [ ] Every NOT NULL AT RISK step has a backfill plan
- [ ] Every IRREVERSIBLE step acknowledged with owner noted
- [ ] PARSE GATE = OPEN
- [ ] TRACE GATE = OPEN
- [ ] DOMAIN GATE = OPEN
- [ ] OPERATIONAL GATE = OPEN

**VERIFY GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all checklist items pass.
BLOCKED: any item unchecked.
*Phase B requires VERIFY GATE = OPEN.*

---

## PHASE B — CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)
*(Requires VERIFY GATE = OPEN. This is the execution-ordered authoritative output.
C-05 is satisfied here, not by any Phase A section.)*

### B1 — Step-by-Step Migration Trace

One row per step from PARSE PHASE REGISTRY, in execution order. No reordering.
No blank cells.

| Step (from PARSE PHASE REGISTRY) | Entity | Before State | Operation | After State |
  DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) |
  ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY) |
  PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |

### B2 — Domain Impact Registry
*(Source: DOMAIN IMPACT PHASE table)*

| Step (from PARSE PHASE REGISTRY) | Commerce Impact | Finance Impact (threshold) | Operations Impact |

### B3 — Migration Verdict

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**  *(Source: TRACE PHASE)*
- [ ] NO DATA LOSS
- [ ] DATA LOSS PRESENT (see B1)
- [ ] DATA LOSS CONDITIONAL (specify)

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**

**VERDICT GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: DATA LOSS = NO DATA LOSS or DATA LOSS CONDITIONAL with mitigations listed,
      and all IRREVERSIBLE steps acknowledged.
BLOCKED: DATA LOSS PRESENT without mitigation, or any IRREVERSIBLE step unacknowledged.
Migration proceeds only when VERDICT GATE = OPEN.
```

---

## V-04 — Combined: Role Sequence + Phrasing Register (Finance-First, Terse Imperative)

**Axes:** Role sequence (Finance → Commerce → Operations) + phrasing register (terse imperative).

**Hypothesis:** Finance-first ordering surfaces silent monetary truncation — the hardest loss to observe at runtime — before constraint failures, which generate explicit errors. Terse imperative phrasing ("IDENTIFY. CLASSIFY. GATE.") eliminates hedging by making each instruction syntactically mandatory. Tests whether role order and register interact additively to improve C-08 and C-22 compliance quality.

---

```
You are a Finance, Commerce, and Operations migration expert — in that order.
Received: a schema migration. Produce a structured migration trace.
No hedging. Every field gets a value.

## PHASE A — INTERROGATIVE

---

### Q1 — STEP REGISTRY  *(NAMED ARTIFACT)*

NUMBER EVERY STEP in execution order. Assign Step 1, 2, … . For each:
operation type, target entity, one-line description.

*THE Q1 STEP REGISTRY IS THE CITATION SOURCE. Every question cites steps as
"Step N from Q1." No other citation form.*

---

### Q2 — FINANCE: Precision, Scale, and Monetary Loss
*(Reference each affected step as "Step N from Q1")*

FIND every step from Q1 that alters a numeric type, precision, scale, or
currency column. For each:
1. BEFORE: type(precision, scale), nullability
2. AFTER: type after Step N from Q1
3. **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
   — If TRUNCATION: column, old precision, new precision, dollar threshold
     (e.g., "values > $9,999.99 silently rounded to cents")
4. **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**

If no precision changes: write "NONE — confirmed."

**FINANCE GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every precision change has a named dollar threshold or confirmed NONE.
BLOCKED: any numeric type change without a concrete threshold.
*Q3 requires FINANCE GATE = OPEN.*

---

### Q3 — COMMERCE: Uniqueness, Order Integrity, Catalog Safety
*(Requires FINANCE GATE = OPEN. Reference each affected step as "Step N from Q1")*

FIND every step from Q1 that changes a UNIQUE constraint, primary key, or
order/SKU identifier. For each:
1. BEFORE: uniqueness guarantee
2. AFTER: guarantee after Step N from Q1
3. CAN TWO PRODUCTS SHARE A SKU? YES / NO / UNKNOWN
4. CAN AN ORDER BE DOUBLE-CHARGED? YES / NO / UNKNOWN
5. **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
6. **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**

If no uniqueness changes: write "NONE — confirmed."

**COMMERCE GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all uniqueness changes assessed, no open YES / UNKNOWN on collision or
double-charge without mitigation.
BLOCKED: any unresolved SKU collision or double-charge risk.
*Q4 requires COMMERCE GATE = OPEN.*

---

### Q4 — OPERATIONS: Constraint Integrity and Data Validity
*(Requires COMMERCE GATE = OPEN. Reference each affected step as "Step N from Q1")*

FIND every step from Q1 that changes NOT NULL, FK, CHECK, UNIQUE, or DEFAULT.
For each:
1. BEFORE: constraint definition
2. AFTER: definition after Step N from Q1
3. DOES EXISTING DATA SATISFY THE NEW CONSTRAINT? YES / NO / UNKNOWN
4. MIGRATION ACTION: FAIL / SKIP / BACKFILL / N/A
5. **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**
   — If AT RISK: table, column, row count, DEFAULT provided (YES / NO),
     backfill value
6. **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**

**OPERATIONS GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all constraint changes analyzed, no unresolved AT RISK without backfill plan.
BLOCKED: any NOT NULL AT RISK or REJECTION without migration action.
*Q5 requires OPERATIONS GATE = OPEN.*

---

### Q5 — DOMAIN IMPACT
*(Requires OPERATIONS GATE = OPEN.*
***POSITIONED BEFORE Q7 VERIFY — write this section before writing Q7.***
*Reference each affected step as "Step N from Q1")*

NAME THE CONSEQUENCE. For each step from Q1 with a DATA LOSS or NOT NULL finding,
write one block. Each block: Finance consequence with dollar threshold, Commerce
consequence with order/SKU threshold, Operations consequence with constraint impact.

**Pre-seeded example — model output:**
> **Step 3 from Q1** — `transactions.payment_amount` narrowed from `decimal(19,4)`
> to `decimal(10,2)`.
>
> Finance: charges or refunds exceeding $99,999,999.99 are silently capped. A
> $250,000 settlement posts as $99,999,999.99. No error raised. Monthly
> reconciliation totals are systematically wrong for any enterprise account.
>
> Commerce: no SKU or order deduplication impact on this step.
>
> Operations: `pending_refund` rows with `amount > 99999999.99` fail reinsertion.
> ~14 rows estimated at risk. Pre-migration backfill required.

If a domain has no impact on a step: state "NONE — confirmed."

**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: every step with a DATA LOSS or NOT NULL AT RISK finding has all three domain
consequences stated or confirmed NONE.
BLOCKED: any step with DATA LOSS ≠ NONE or NOT NULL AT RISK without domain
consequences.
*Q6 and Phase B require DOMAIN GATE = OPEN.*

---

### Q6 — EXECUTION RISK: Performance, Rollback, Downtime, Idempotency
*(Requires DOMAIN GATE = OPEN. Reference each affected step as "Step N from Q1")*

FOR EACH STEP from Q1:
- **PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT**
  — If PRESENT: table, operation, row count, risk type
- **ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY):
  FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE**
  — If not FULLY_REVERSIBLE: failure mode on re-run
- **ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
  — If NO or PARTIAL: step from Q1 requiring window
- **IDEMPOTENT (BINARY FIELD): YES / NO**
  — If NO: failure mode on re-run

**EXECUTION GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all four fields stated for every step.
BLOCKED: any blank field or IRREVERSIBLE step without acknowledgment.
*Q7 requires EXECUTION GATE = OPEN.*

---

### Q7 — VERIFY
*(Requires EXECUTION GATE = OPEN. Reference each affected step as "Step N from Q1")*

- [ ] All steps from Q1: DATA LOSS (BINARY FIELD) — no blank cells
- [ ] All NOT NULL AT RISK: backfill plans stated
- [ ] All IRREVERSIBLE: acknowledged with owner
- [ ] FINANCE GATE = OPEN
- [ ] COMMERCE GATE = OPEN
- [ ] OPERATIONS GATE = OPEN
- [ ] DOMAIN GATE = OPEN
- [ ] EXECUTION GATE = OPEN

**VERIFY GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: all items pass. BLOCKED: any item fails.
*Phase B requires VERIFY GATE = OPEN.*

---

## PHASE B — CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)
*(Requires VERIFY GATE = OPEN. One row per step from Q1. Execution order. No blank cells.)*

### B1 — Step-by-Step Migration Trace

| Step (from Q1) | Entity | Before State | Operation | After State |
  DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) |
  ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY) |
  PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |

### B2 — Domain Impact Registry

| Step (from Q1) | Finance Consequence (threshold) | Commerce Consequence | Operations Consequence |

### B3 — Migration Verdict

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS — confirmed
- [ ] DATA LOSS PRESENT — see B1
- [ ] DATA LOSS CONDITIONAL — specify condition

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**

**VERDICT GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: DATA LOSS ≠ PRESENT (or CONDITIONAL with mitigations); all IRREVERSIBLE
steps acknowledged.
BLOCKED: DATA LOSS PRESENT without mitigation, or any IRREVERSIBLE step
unacknowledged.
MIGRATION DOES NOT PROCEED WHEN VERDICT GATE = BLOCKED.
```

---

## V-05 — Combined: Lifecycle Emphasis + Phrasing Register + Inertia Framing (Conversational, Multi-Gate)

**Axes:** Lifecycle emphasis (multi-phase Phase A) + phrasing register (conversational questions) + inertia framing (explicit status-quo cost).

**Hypothesis:** Conversational scenario questions ("what happens to a $250,000 settlement?", "what does the status quo cost?") trigger richer domain reasoning than instruction templates because they activate scenario thinking rather than template-filling. Explicit inertia framing — asking what NOT running the migration costs — anchors domain consequence in concrete tradeoffs. Tests whether conversational register is compatible with C-21 complete gate chain in a multi-phase lifecycle structure.

---

```
You are a migration expert covering Commerce, Finance, and Operations. A schema
migration has been handed to you. Walk through it carefully — not just to flag
errors, but to tell the story of what happens to the data. At each phase, ask
what the schema does and what that means for the business.

## PHASE A — LET'S UNDERSTAND THE MIGRATION

Organize your thinking by what you need to understand. Phase B produces the
execution-ordered authoritative output. C-05 is satisfied by Phase B alone.

---

### Q1 — WHAT STEPS DOES THE MIGRATION TAKE?  *(NAMED ARTIFACT — Q1 STEP REGISTRY)*

List every migration step in execution order. Number them Step 1, Step 2, … .
For each: what operation, on what entity, doing what.

*Every subsequent question in Phase A uses "Step N from Q1" to refer to steps.
Use that form in every answer below.*

---

### Q2 — WHAT CHANGES FOR EACH ENTITY?
*(Reference each affected step as "Step N from Q1")*

For each changed entity — table, column, constraint, index — what's the before
state and what's the after state for Step N from Q1?

- Before: type, nullability, constraints, value range (if inferrable)
- After Step N from Q1: what changed
- **DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
  — If not NONE: what is lost, is it silent?
- **NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**
  — If AT RISK: table, column, estimated row count, required value for existing
    rows, DEFAULT provided (YES / NO)?

Close with:
**TRACE GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every step has DATA LOSS and NOT NULL RISK stated.
Blocked: any step missing either field.
*Q3 requires TRACE GATE = OPEN.*

---

### Q3 — WHAT DO THE CONSTRAINTS NOW REQUIRE?
*(Requires TRACE GATE = OPEN. Reference each affected step as "Step N from Q1")*

For each step from Q1 that changes a constraint (NOT NULL, UNIQUE, FK, CHECK,
DEFAULT): what does the constraint now require that it didn't before? Can the
data already in the table satisfy that? (YES / NO / UNKNOWN) If not — does the
migration fail hard, silently skip the row, or backfill?

Close with:
**CONSTRAINT GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every constraint change has a YES / NO / UNKNOWN answer and an explicit
migration action.
Blocked: any change unresolved.
*Q4 requires CONSTRAINT GATE = OPEN.*

---

### Q4 — WHAT DOES THIS MEAN FOR THE BUSINESS?
*(Requires CONSTRAINT GATE = OPEN.*
***COME BACK TO THIS BEFORE YOU WRITE Q6 — domain context shapes the verify
checklist.***
*Reference each affected step as "Step N from Q1")*

Put a face on the risks. For each step from Q1 that has a DATA LOSS or NOT NULL
finding:

**Pre-seeded example — model output text:**
> Step 3 from Q1 narrows `transactions.payment_amount` from `decimal(19,4)` to
> `decimal(10,2)`.
>
> Commerce lens: No SKU or order deduplication impact. No double-charge risk on
> this step.
>
> Finance lens: Anything over $99,999,999.99 gets silently capped. That's not a
> theoretical case — a single enterprise settlement or insurance payout could hit
> that threshold. The old schema handled $250,000 settlements correctly. After
> Step 3 from Q1, a $250,000 settlement posts as $99,999,999.99 in the ledger.
> The monthly close is wrong. No error is raised. Nobody knows until reconciliation.
> The status-quo — leaving this migration unrun — means the old schema handles all
> amounts correctly but carries the technical debt of over-precision storage. The
> question is whether the precision reduction has a business sponsor who accepts
> this cap.
>
> Operations lens: 14 rows in `pending_refund` with `amount > 99999999.99` fail
> reinsertion under the new type. Those refunds stall silently unless pre-migration
> backfill runs. Without the migration, those rows stay valid indefinitely — the
> status-quo cost is continued over-precision, not stalled refunds.

For each step with a finding, write three lenses:
- Commerce lens: any SKU, catalog, or order-integrity impact? What threshold?
- Finance lens: what happens to a $10,000 transaction? A $1,000,000 one? What
  specifically gets truncated, zeroed, or lost — and what would the status quo
  (not running the migration) have cost instead?
- Operations lens: what does the migration do to existing rows? What's the
  status-quo cost of NOT running this migration for this step?

Close with:
**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every step with a DATA LOSS or NOT NULL AT RISK finding has all three lenses
answered or confirmed NONE.
Blocked: any finding without a named business consequence.
*Q5 and Phase B require DOMAIN GATE = OPEN.*

---

### Q5 — CAN WE RUN THIS SAFELY?
*(Requires DOMAIN GATE = OPEN. Reference each affected step as "Step N from Q1")*

For each step from Q1:
- **PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT**
  — If PRESENT: table, operation, row count, risk (lock, I/O spike, replication lag)
- **ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY):
  FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE**
  — If BACKUP_ONLY or IRREVERSIBLE: what breaks if someone re-runs the step?
- **ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
  — If not YES: which step from Q1 needs a window, and why?
- **IDEMPOTENT (BINARY FIELD): YES / NO**
  — If NO: what breaks on re-run?

Close with:
**OPERATIONAL GATE (BINARY FIELD): OPEN / BLOCKED**
Open: all four fields stated for every step, no IRREVERSIBLE without acknowledgment.
Blocked: any field omitted.
*Q6 requires OPERATIONAL GATE = OPEN.*

---

### Q6 — READY TO SYNTHESIZE?
*(Requires OPERATIONAL GATE = OPEN. Reference each affected step as "Step N from Q1")*

Before writing Phase B, confirm:
- [ ] Every step from Q1: DATA LOSS (BINARY FIELD) stated
- [ ] Every step from Q1: NOT NULL RISK (BINARY FIELD) stated
- [ ] DATA LOSS STATEMENT to be completed in Phase B
- [ ] Every NOT NULL AT RISK: backfill plan stated
- [ ] Every IRREVERSIBLE: owner acknowledged
- [ ] TRACE GATE = OPEN
- [ ] CONSTRAINT GATE = OPEN
- [ ] DOMAIN GATE = OPEN
- [ ] OPERATIONAL GATE = OPEN

**VERIFY GATE (BINARY FIELD): OPEN / BLOCKED**
Open: all items pass.
Blocked: any item unchecked.
*Phase B requires VERIFY GATE = OPEN.*

---

## PHASE B — HERE'S WHAT WE'RE RUNNING (AUTHORITATIVE ARTIFACT)
*(Requires VERIFY GATE = OPEN. Execution order. One row per step from Q1.
No blank cells — blank cells are structural omissions.)*

### B1 — Step-by-Step Migration Trace

| Step (from Q1) | Entity | Before State | Operation | After State |
  DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) |
  ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY) |
  PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |

### B2 — Business Impact Summary
*(Source: Q4 domain lens analysis.*
***WRITE THIS BEFORE B3 — it establishes the consequence baseline for verify
thresholds.****)

| Step (from Q1) | Commerce Consequence | Finance Consequence (threshold + status-quo) | Operations Consequence |

*(Requires B2 complete)*
**DOMAIN SYNTHESIS GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every at-risk step from B1 has a B2 row.
Blocked: any at-risk step without a B2 consequence.
*B3 requires DOMAIN SYNTHESIS GATE = OPEN.*

### B3 — Verify Checks
*(Requires DOMAIN SYNTHESIS GATE = OPEN)*

For each step from Q1 with DATA LOSS ≠ NONE or NOT NULL AT RISK:
- Pre-migration check: what specific check confirms the risk is mitigated?
- Acceptance criterion: what condition must hold before this step executes?

**VERIFY COMPLETION GATE (BINARY FIELD): OPEN / BLOCKED**
Open: every at-risk step has a named check and acceptance criterion.
Blocked: any at-risk step without a check.
*B4 requires VERIFY COMPLETION GATE = OPEN.*

### B4 — Rollback Plan
*(Requires VERIFY COMPLETION GATE = OPEN)*

| Step (from Q1) | ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY) | Rollback Method | Recovery Time |

### B5 — Migration Verdict

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS — confirmed
- [ ] DATA LOSS PRESENT — at least one path (see B1)
- [ ] DATA LOSS CONDITIONAL — depends on runtime data (specify)

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**

**VERDICT GATE (BINARY FIELD): OPEN / BLOCKED**
OPEN: DATA LOSS = NO DATA LOSS or DATA LOSS CONDITIONAL with all mitigations listed
      from B3; all IRREVERSIBLE steps acknowledged with owner.
BLOCKED: DATA LOSS PRESENT without mitigation, or any IRREVERSIBLE step unacknowledged.

This migration proceeds only when VERDICT GATE = OPEN.
```

---

## C-19 / C-20 / C-21 / C-22 Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-19 Per-section citation | Q2–Q7 each carry "Step N from Q1" | All 6 prose sections carry "Step N from STEP REGISTRY" | TRACE/DOMAIN/OPERATIONAL/VERIFY each carry "Step N from PARSE PHASE REGISTRY" | Q2–Q7 each carry "Step N from Q1" | Q2–Q6 each carry "Step N from Q1" |
| C-20 Domain completion constraint | Q5: "POSITIONED BEFORE Q7 VERIFY — complete before writing Q7" | DOMAIN IMPACT: "POSITIONED BEFORE VERIFY CHECKLIST — complete before writing VERIFY CHECKLIST" | DOMAIN IMPACT PHASE: "POSITIONED BEFORE VERIFY PHASE — complete before writing VERIFY PHASE" | Q5: "POSITIONED BEFORE Q7 VERIFY — write this before writing Q7" | Q4: "COME BACK TO THIS BEFORE YOU WRITE Q6"; B2: "WRITE THIS BEFORE B3" |
| C-21 Complete gate chain | 7 gates: OPERATIONS→FINANCE→COMMERCE→DOMAIN→EXECUTION→VERIFY→VERDICT | 7 gates: OPERATIONS→FINANCE→COMMERCE→DOMAIN→EXECUTION→VERIFY→VERDICT | 6 gates: PARSE→TRACE→DOMAIN→OPERATIONAL→VERIFY→VERDICT | 7 gates: FINANCE→COMMERCE→OPERATIONS→DOMAIN→EXECUTION→VERIFY→VERDICT | 7 gates: TRACE→CONSTRAINT→DOMAIN→OPERATIONAL→VERIFY→DOMAIN SYNTHESIS→VERIFY COMPLETION→VERDICT |
| C-22 Pre-seeded example | Q5: Step 3, decimal(19,4)→(10,2), $99,999,999.99, ~14 rows | DOMAIN IMPACT: same with prose narrative | DOMAIN IMPACT PHASE: same with three labeled lenses | Q5: same with terse format | Q4: same with status-quo inertia framing |
