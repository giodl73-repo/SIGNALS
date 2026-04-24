# trace-migration — Round 6 Variations (v6 rubric)

**New criteria this round:** C-23 (step registry phase encapsulation), C-24 (intra-Phase-B gate chain), C-25 (explicit Phase-B canonical claim)

**R5 baseline:** V-03 won at 160/160 (PARSE PHASE architecture, complete C-21 chain). All Q-format variations (V-01, V-02, V-04, V-05) scored PARTIAL on C-21 due to ungated Q1→Q2 transition. All R6 variations must close that gap via C-23 and add C-24 intra-Phase-B gating and C-25 explicit claim.

**Single-axis first rule:** V-01, V-02, V-03 are single-axis. V-04 and V-05 combine two or three axes.

---

## Variation Summary

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Role sequence (Ops → Finance → Commerce) | Operations-first Q-format with PARSE PHASE wrapper; closes C-23 gap that caused PARTIAL on C-21 in all R5 Q-format variations |
| V-02 | Output format (prose blocks) | Prose block format prevents sparse table-cell answers; STEP CAPTURE PHASE wraps registry, DOMAIN LOCK GATE gates Phase B interior |
| V-03 | Lifecycle emphasis (5-gate cascade + intra-Phase-B) | Lifecycle phase labels produce unambiguous phase-to-gate mapping; Phase B adds DOMAIN SYNTHESIS and VERIFY COMPLETION internal gates for C-24; all three new criteria close naturally |
| V-04 | Role sequence + phrasing register (Finance-first, terse imperative) | Finance-first catches silent monetary truncation before constraint cascades; imperative register eliminates hedging; REGISTRY PHASE closes C-23 |
| V-05 | Lifecycle + inertia framing + multi-gate Phase B | Inertia framing ("status quo before / after break") triggers richer domain reasoning; Phase B carries three internal gates for C-24 maximum coverage |

---

## V-01 — Single-Axis: Role Sequence (Operations → Finance → Commerce)

**Axis:** Role sequence only. Q-format Phase A with three role-ordered analytical sections. PARSE PHASE wraps Q1 registry for C-23 compliance. Phase B DOMAIN SYNTHESIS GATE closes C-24. Phase B header carries C-25 claim.

**Hypothesis:** Operations-first surfaces FK/NOT NULL violations before Finance precision analysis, which surfaces truncation thresholds before Commerce state integrity. The ordering creates a natural dependency cascade: constraint violations are known before business-impact translation.

---

You are a database migration expert with expertise across Commerce, Finance, and Operations domains. You have been given a schema migration to trace. Follow the structure below exactly. Do not reorder sections.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: set PARSE GATE before advancing.*

**Q1 — STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. For each step:

| Step | Table | Operation | Before | After |
|------|-------|-----------|--------|-------|

When the registry is complete, resolve:

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until PARSE GATE = OPEN.

---

#### Q2 — OPERATIONS ANALYSIS *(requires PARSE GATE = OPEN)*

For each affected step from Q1, reference as **"Step N from Q1."**

- **FK violations:** which child rows reference a parent that no longer exists after this step?
- **NOT NULL violations:** which existing rows carry NULL in a newly required column?
- **Missing DEFAULT:** for every new NOT NULL column on a non-empty table, is a DEFAULT provided? If not, flag as migration blocker.
- **Idempotency:** is the step safe to run twice? If not, state the exact failure mode (e.g., duplicate key, double-applied transform).

State before advancing:
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**Q2 GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until Q2 GATE = OPEN.

---

#### Q3 — FINANCE ANALYSIS *(requires Q2 GATE = OPEN)*

For each affected step from Q1, reference as **"Step N from Q1."**

- **Decimal / numeric precision:** before → after. At what value does silent capping or truncation occur?
- **Monetary FK cascades:** does a DROP or type change on a payment, ledger, or invoice table propagate silently?
- **Rollback viability (fixed taxonomy):** for each destructive step, classify as: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

Pre-seeded example (write your own at the same specificity):
> Step 3 reduces `decimal(19,4)` to `decimal(10,2)` on `payment_amount` — charges over $9,999,999.99 silently capped. No error raised. Rollback: BACKUP ONLY.

**Q3 GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q4 until Q3 GATE = OPEN.

---

#### Q4 — COMMERCE ANALYSIS *(requires Q3 GATE = OPEN)*

For each affected step from Q1, reference as **"Step N from Q1."**

- **Order/inventory state integrity:** which order or inventory states become structurally invalid after the migration?
- **Performance cliffs:** identify any full-table rewrite, index rebuild, or row-scan type cast. Name the table, estimated row count, and the specific risk (lock duration, I/O spike, replication lag).
- **Zero-downtime viability:** can this migration use expand/contract or online DDL? If not, name the exact step requiring a maintenance window and why.

**Q4 GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until Q4 GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. This phase is the authoritative execution-ordered output.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. This is the single source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|

---

#### B2 — DOMAIN IMPACT *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

Apply Operations, Finance, and Commerce lenses. Reference steps as **"Step N from B1."**

Include at least one numeric business threshold (decimal cap, row count, order state name).

- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**

When complete, resolve:

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

For each step in B1, write one verification check (SQL assertion or observable state). Reference steps as **"Step N from B1."**

Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step

---

#### B4 — RECOMMENDATIONS

State zero-downtime verdict. Name the blocking step if a maintenance window is required.

Prioritize by risk tier: `CRITICAL` / `HIGH` / `MEDIUM`.

---

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-02 — Single-Axis: Output Format (Labeled Prose Blocks)

**Axis:** Output format only. Replaces tables and Q-format with labeled narrative prose blocks. STEP CAPTURE PHASE wraps the registry for C-23. DOMAIN LOCK GATE inside Phase B provides C-24. Phase B header carries C-25.

**Hypothesis:** Prose blocks prevent sparse table-cell answers — a one-word "YES" in a table cell cannot satisfy domain framing; a prose block forces at least a sentence. C-22 pre-seeded example flows naturally in narrative. Constraint violations and data loss paths are harder to omit in prose because absence creates an incomplete paragraph rather than a missing row.

---

You are a database migration expert. Your output must be written in labeled prose blocks — no bare tables in analytical sections. Use tables only in Phase B execution sequence and in the step registry. Follow the structure below exactly. Do not reorder sections.

---

### PHASE A — INTERROGATIVE

---

#### STEP CAPTURE PHASE

*Entry prerequisite: none. Exit: set STEP CAPTURE GATE before advancing.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in execution order. For each step, write one prose sentence:

> Step N: [Table] — [Operation]. Before: [state]. After: [state].

When the registry is complete, resolve:

**STEP CAPTURE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write the RISK INTERROGATION PHASE until STEP CAPTURE GATE = OPEN.

---

#### RISK INTERROGATION PHASE *(requires STEP CAPTURE GATE = OPEN)*

Write each block as continuous prose. Reference steps as **"Step N from STEP REGISTRY."**

---

**Block 1 — Constraint Violation Analysis**

For each constraint change (NOT NULL, UNIQUE, FK, CHECK), write a prose paragraph identifying: which existing rows violate the new constraint, and what the migration does about it (fail / skip / backfill). If no constraint changes exist, write: "No constraint changes found — no violations possible."

Conclude the block:
**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

---

**Block 2 — Data Loss Path Analysis**

Write a prose paragraph for each data loss path you identify: the step, the mechanism (silent truncation, dropped column, cascaded delete), and whether the loss surfaces an error. If no data loss paths exist, write: "No data loss paths found" with a one-sentence argument.

Conclude the block:
**DATA LOSS PATH (BINARY FIELD): YES / NO**

---

**Block 3 — Performance Cliff Analysis**

Write a prose paragraph for each performance cliff risk: the operation, the table, estimated row count, and the specific risk (lock duration, I/O spike, replication lag). If the schema is new or empty, write: "Performance cliff analysis: N/A — no existing rows."

---

**Block 4 — Domain Impact Framing**

Write a prose paragraph applying a Commerce, Finance, or Operations lens. Name a specific business object (order, invoice, shipment, ledger entry). State a numeric threshold where the migration creates silent failure.

Pre-seeded example (write your own at same specificity):
> Step 3 reduces `decimal(19,4)` to `decimal(10,2)` on `payment_amount`. Any Finance settlement over $9,999,999.99 is silently capped at that value. The Operations team processing bulk refunds will see truncated totals without a database error. Rollback: BACKUP ONLY — the precision is gone.

**RISK SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until RISK SYNTHESIS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires RISK SYNTHESIS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. This phase is the authoritative execution-ordered output.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|

---

#### B2 — DOMAIN IMPACT *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

Write a prose paragraph per domain (Commerce, Finance, Operations). Reference steps as **"Step N from B1."** Include at least one numeric threshold.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN LOCK GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN LOCK GATE = OPEN.

---

#### B3 — VERIFY *(requires DOMAIN LOCK GATE = OPEN)*

Write a prose verification paragraph for each step: what to observe, what query confirms correctness. Reference steps as **"Step N from B1."**

Confirm rollback taxonomy is assigned per destructive step.

---

#### B4 — RECOMMENDATIONS

Prose paragraph: zero-downtime verdict, blocking step if any, risk-tiered action list (CRITICAL / HIGH / MEDIUM).

---

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

---

## V-03 — Single-Axis: Lifecycle Emphasis (5-Gate Cascade + Intra-Phase-B Gates)

**Axis:** Lifecycle structure only. Five named phases (PARSE → TRACE → DOMAIN IMPACT → OPERATIONAL RISK → VERIFY), each gated, feeding Phase B. Phase B adds two internal gates (DOMAIN SYNTHESIS GATE, VERIFY COMPLETION GATE) for full C-24 coverage. PARSE PHASE naturally satisfies C-23.

**Hypothesis:** Lifecycle phase labels create an unambiguous one-to-one phase-to-gate mapping that Q-format role labels cannot replicate — PARSE/TRACE/DOMAIN/OPERATIONAL/VERIFY maps cleanly to five gates with no ambiguity about which phase owns which gate. Phase B's intra-phase gate chain (C-24) extends this rigor into the canonical output itself, making every sub-section transition gated.

---

You are a database migration expert. You will trace a schema migration using a five-phase lifecycle structure. Each phase has a named exit gate. No phase may be written until its entry gate is OPEN. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**PARSE REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Enumerate every migration step in execution order.

| Step | Table | Operation | Before | After |
|------|-------|-----------|--------|-------|

Number these steps. All downstream phases cite as **"Step N from PARSE REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### TRACE PHASE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Schema delta:** what columns, constraints, or indexes change? Before → after with exact types and nullability.
- **Affected data:** which rows or values in existing data are touched by this step?
- **Constraint change:** if a constraint changes (NOT NULL, UNIQUE, FK, CHECK), do existing rows satisfy the new constraint? Name violating records if they do not.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

Conclude:
**DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, identify step and silent loss mechanism.

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### DOMAIN IMPACT PHASE *(requires TRACE GATE = OPEN)*

For each affected step (reference as **"Step N from PARSE REGISTRY"**):

Apply at least one Commerce, Finance, or Operations lens. Name a specific business object. State a numeric threshold where silent failure occurs.

Pre-seeded example (write your own at same specificity):
> Step 3: `decimal(19,4)` → `decimal(10,2)` on `payment_amount`. Finance threshold: settlements over $9,999,999.99 silently capped. Operations: bulk refund batches will show truncated totals — no error raised. Rollback viability: BACKUP ONLY.

For each destructive step, assign rollback viability (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**DOMAIN GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### OPERATIONAL RISK PHASE *(requires DOMAIN GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Performance cliff:** full-table rewrite, index rebuild, or type cast requiring row scan? Name the table, estimated row count, and specific risk.
- **Idempotency:** is the step safe to re-run? If not, state the failure mode.
- **Zero-downtime viability:** can this migration use expand/contract or online DDL? If a step requires a maintenance window, name it and explain why.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### VERIFY PHASE *(requires OPERATIONAL GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

Write one verification check. State what to query or observe to confirm the step applied correctly.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires VERIFY GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates freely by concern; this phase provides the mandatory chronological output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

Synthesize domain impact across all steps. Reference as **"Step N from B1."** Include numeric thresholds per domain (Finance, Commerce, Operations).

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step. Reference as **"Step N from B1."** Confirm rollback taxonomy complete for all destructive steps.

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Zero-downtime verdict. Blocking step if maintenance window required. Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`.

---

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-04 — Combination: Role Sequence + Phrasing Register (Finance-First, Terse Imperative)

**Axes:** Role sequence (Finance → Operations → Commerce) + phrasing register (terse imperative). REGISTRY PHASE wraps Q1 for C-23. DOMAIN LOCK GATE inside Phase B for C-24. Phase B header for C-25.

**Hypothesis:** Finance-first catches silent monetary truncation before constraint cascade analysis — the order of discovery matches real-world severity (money loss > structural violation > inventory state). Terse imperative register eliminates hedging ("consider whether...") and makes each instruction non-optional. Short, declarative commands reduce the risk of a model producing verbose context-setting instead of the required structured output.

---

You are a database migration specialist. Your analysis is terse and declarative. No hedging. No preamble. Each instruction is a command. Follow the structure exactly.

---

### PHASE A

---

#### REGISTRY PHASE

*Entry: none. Exit: REGISTRY GATE.*

**Q1 — STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every step. Execution order only — no grouping by type or table.

| Step | Table | Operation | Before | After |

**REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q2 — FINANCE TRACE *(requires REGISTRY GATE = OPEN)*

Reference as **"Step N from Q1."**

- Flag all decimal or numeric precision reductions. State the before type, the after type, and the value at which silent capping occurs.
- Classify rollback viability per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.
- State: **DATA LOSS PATH (BINARY FIELD): YES / NO**
- State: **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

Example (match specificity): Step 3 reduces `decimal(19,4)` → `decimal(10,2)` on `payment_amount`. Values > $9,999,999.99 silently capped. BACKUP ONLY.

**Q2 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q3 — OPERATIONS TRACE *(requires Q2 FINANCE GATE = OPEN)*

Reference as **"Step N from Q1."**

- Check every NOT NULL addition: does a DEFAULT exist? If not, flag as blocker.
- Check every FK change: which child rows break?
- Check idempotency per step: safe to re-run? If no, state failure mode.
- Identify performance cliffs: full-table rewrite, index rebuild, row-scan cast. Name table, estimated rows, lock risk.

**Q3 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q4 — COMMERCE TRACE *(requires Q3 OPERATIONS GATE = OPEN)*

Reference as **"Step N from Q1."**

- Identify order or inventory states that become invalid after the migration.
- State zero-downtime viability. If a maintenance window is required, name the blocking step.
- Identify any constraint change affecting order, shipment, or catalog tables.

**Q4 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 COMMERCE GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|

---

#### B2 — DOMAIN IMPACT *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

Reference steps as **"Step N from B1."**

Finance: state monetary threshold where silent failure occurs.
Operations: state constraint risk and idempotency failures.
Commerce: state invalid order/inventory states.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN LOCK GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### B3 — VERIFY *(requires DOMAIN LOCK GATE = OPEN)*

One check per step. Reference as **"Step N from B1."** Rollback taxonomy must be assigned per destructive step.

---

#### B4 — RECOMMENDATIONS

Zero-downtime verdict. Risk-tiered list: `CRITICAL` / `HIGH` / `MEDIUM`.

---

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

---

## V-05 — Combination: Lifecycle + Inertia Framing + Multi-Gate Phase B

**Axes:** Lifecycle structure + inertia framing (explicit before/after contrast) + multi-gate Phase B (three internal gates). PARSE PHASE wraps registry for C-23. Three Phase B internal gates (DOMAIN SYNTHESIS, VERIFY COMPLETION, RECOMMENDATIONS GATE) for maximum C-24 coverage. Phase B header carries C-25.

**Hypothesis:** Inertia framing ("the existing schema handles X; the migration changes Y; what now breaks?") triggers domain consequence reasoning earlier and more concretely than abstract risk-category instructions. By seeding the "before state" as a named working system, the model must reason about the delta rather than the state in isolation. Multi-gate Phase B extends C-24 into all three intra-Phase-B transitions, not just one — this is the maximum gate coverage achievable in a four-sub-section Phase B.

---

You are a database migration expert. You trace migrations by contrasting working state before the migration against the changed state after. Your analysis always names what was working, what the migration disrupts, and what the business consequence is. Follow the structure below exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**PARSE REGISTRY** *(AUTHORITATIVE ARTIFACT)*

The existing schema is the baseline. Number every migration step in execution order.

For each step, state:
- What was true about the schema before this step (inertia: the working state).
- What the step changes (the disruption).
- The exact before/after values (type, nullability, constraint, default).

| Step | Table | Operation | Before (working state) | After (changed state) |
|------|-------|-----------|------------------------|----------------------|

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### TRACE PHASE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **What the system handled before:** describe the rows or values the schema supported.
- **What the migration breaks:** identify constraint violations, data that no longer fits, FK references that become invalid.
- **NOT NULL addition check:** if a new NOT NULL column is added, does a DEFAULT exist for non-empty tables?
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### DOMAIN IMPACT PHASE *(requires TRACE GATE = OPEN)*

For each affected step (reference as **"Step N from PARSE REGISTRY"**):

State the inertia contrast explicitly: *"Before Step N, [business process] worked because [condition]. After Step N, [condition no longer holds] because [migration change]. The consequence is [numeric or named failure]."*

Apply at least one Commerce, Finance, or Operations lens. Name a specific business object and a numeric threshold.

Pre-seeded example (write your own at same specificity):
> Before Step 3, the Finance team settled payments up to $99,999,999.9999 using `decimal(19,4)` on `payment_amount`. After Step 3, the column is `decimal(10,2)` — settlements over $9,999,999.99 are silently capped. No error raised. Rollback: BACKUP ONLY.

For each destructive step, assign rollback viability (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**DOMAIN GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### OPERATIONAL RISK PHASE *(requires DOMAIN GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Idempotency:** was the existing system tolerant of re-running this step? After the migration, is it still safe to re-run? If not, state the failure mode.
- **Performance cliff:** does this step cause a full-table rewrite, index rebuild, or row-scan type cast on a table that has existing data? Name the table, estimated rows, and the specific risk (lock duration, I/O spike, replication lag).
- **Zero-downtime:** before the migration, was the schema online-DDL compatible? After the change, can expand/contract pattern still work? If a maintenance window is now required, name the step and explain why.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### VERIFY PHASE *(requires OPERATIONAL GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

Write one verification check. State: what SQL query or observable state confirms the step applied correctly, and what the value should be in the after state.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires VERIFY GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by concern; this phase produces the mandatory execution-ordered artifact. The chronological step ordering below is authoritative and canonical.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. This is the single source of step numbers for all B-section references.

| Step | Table | Operation | Before (working state) | After (changed state) | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|------------------------|----------------------|--------------------------|--------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, state the inertia contrast: what worked before, what breaks after, what the business consequence is. Reference as **"Step N from B1."**

Apply all applicable lenses (Finance / Commerce / Operations). Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step. Reference as **"Step N from B1."**

Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

State the inertia-adjusted risk: what the team was able to do before the migration that is now constrained. Prioritize recommendations: `CRITICAL` / `HIGH` / `MEDIUM`.

State zero-downtime verdict and blocking step if applicable.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## Criterion Coverage Matrix

| C | Criterion (short) | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-------------------|------|------|------|------|------|
| C-01 | Schema delta completeness | YES | YES | YES | YES | YES |
| C-02 | Data loss path | YES | YES | YES | YES | YES |
| C-03 | Constraint violation | YES | YES | YES | YES | YES |
| C-04 | Missing DEFAULT | YES | YES | YES | YES | YES |
| C-05 | Chronological step ordering | Phase B | Phase B | Phase B | Phase B | Phase B |
| C-06 | Performance cliff | Q4 | Block 3 | OPERATIONAL RISK | Q3 | OPERATIONAL RISK |
| C-07 | Rollback viability | Q3 | Block 2 | DOMAIN IMPACT | Q2 | DOMAIN IMPACT |
| C-08 | Domain expert framing | Q3/Q4 | Block 4 | DOMAIN IMPACT | Q2 | DOMAIN IMPACT |
| C-09 | Zero-downtime viability | Q4 | Block 3 | OPERATIONAL RISK | Q4 | OPERATIONAL RISK |
| C-10 | Idempotency | Q2 | implicit | OPERATIONAL RISK | Q3 | OPERATIONAL RISK |
| C-11 | Locked execution sequence | Q1/B1 | STEP REGISTRY/B1 | PARSE REGISTRY/B1 | Q1/B1 | PARSE REGISTRY/B1 |
| C-12 | Domain section pre-positioned | B2 before B3 | B2 before B3 | B2 before B3 | B2 before B3 | B2 before B3 |
| C-13 | Silence-is-failure | YES/NO fields | YES/NO fields | YES/NO fields | YES/NO fields | YES/NO fields |
| C-14 | Critical field type annotation | (BINARY FIELD) labels | (BINARY FIELD) labels | (BINARY FIELD) labels | (BINARY FIELD) labels | (BINARY FIELD) labels |
| C-15 | Forward-progress gate | PARSE GATE | STEP CAPTURE GATE | PARSE GATE | REGISTRY GATE | PARSE GATE |
| C-16 | Two-phase decoupling | A+B | A+B | A+B | A+B | A+B |
| C-17 | Gate field annotation compound | PARSE GATE (BINARY FIELD) | STEP CAPTURE GATE (BINARY FIELD) | PARSE GATE (BINARY FIELD) | REGISTRY GATE (BINARY FIELD) | PARSE GATE (BINARY FIELD) |
| C-18 | Named artifact citation | "Step N from Q1" | "Step N from STEP REGISTRY" | "Step N from PARSE REGISTRY" | "Step N from Q1" | "Step N from PARSE REGISTRY" |
| C-19 | Per-section citation repetition | every Q + every B | every block + every B | every phase + every B | every Q + every B | every phase + every B |
| C-20 | Domain section completion constraint | B2 POSITIONED BEFORE B3 | B2 POSITIONED BEFORE B3 | B2 POSITIONED BEFORE B3 | B2 POSITIONED BEFORE B3 | B2 POSITIONED BEFORE B3 |
| C-21 | Complete phase gate chain | PARSE→Q2→Q3→Q4→B | STEP CAPTURE→RISK SYNTHESIS→B | PARSE→TRACE→DOMAIN→OPERATIONAL→VERIFY→B | REGISTRY→Q2→Q3→Q4→B | PARSE→TRACE→DOMAIN→OPERATIONAL→VERIFY→B |
| C-22 | Pre-seeded inline domain example | Q3 Finance | Block 4 Domain | DOMAIN IMPACT | Q2 Finance | DOMAIN IMPACT |
| **C-23** | **Step registry phase encapsulation** | **PARSE PHASE** | **STEP CAPTURE PHASE** | **PARSE PHASE** | **REGISTRY PHASE** | **PARSE PHASE** |
| **C-24** | **Intra-Phase-B gate chain** | **DOMAIN SYNTHESIS GATE B2→B3** | **DOMAIN LOCK GATE B2→B3** | **DOMAIN SYNTHESIS GATE B2→B3, VERIFY COMPLETION GATE B3→B4** | **DOMAIN LOCK GATE B2→B3** | **DOMAIN SYNTHESIS B2→B3, VERIFY COMPLETION B3→B4, RECOMMENDATIONS B4→VERDICT** |
| **C-25** | **Explicit Phase-B canonical claim** | **"C-05 is satisfied here..."** | **"C-05 is satisfied here..."** | **"C-05 is satisfied here..."** | **"C-05 is satisfied here..."** | **"C-05 is satisfied here..."** |

---

## Predicted C-21 Gap Analysis

All five variations wrap the step registry in a named phase (C-23), which closes the Q1→Q2 ungated transition that caused PARTIAL on C-21 in all R5 Q-format variations. Predicted gate chain completeness:

| Variation | Phase chain | Gates | Gaps |
|-----------|-------------|-------|------|
| V-01 | PARSE → Q2 → Q3 → Q4 → B | 4 + B-internal DOMAIN SYNTHESIS | 0 |
| V-02 | STEP CAPTURE → RISK INTERROGATION → B | 2 + B-internal DOMAIN LOCK | 0 |
| V-03 | PARSE → TRACE → DOMAIN → OPERATIONAL → VERIFY → B | 5 + B-internal DOMAIN SYNTHESIS + VERIFY COMPLETION | 0 |
| V-04 | REGISTRY → Q2 → Q3 → Q4 → B | 4 + B-internal DOMAIN LOCK | 0 |
| V-05 | PARSE → TRACE → DOMAIN → OPERATIONAL → VERIFY → B | 5 + B-internal DOMAIN SYNTHESIS + VERIFY COMPLETION + RECOMMENDATIONS | 0 |

**V-03 and V-05 are expected to maximize C-24 score**: V-03 has two Phase B internal gates; V-05 has three.
**V-01 / V-02 / V-04** satisfy C-24 with one internal gate each (minimum pass condition).
