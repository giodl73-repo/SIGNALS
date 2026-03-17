# trace-migration — Round 7 Variations (v7 rubric)

**New criteria this round:** C-26 (terminal output gating), C-27 (inertia-contrast framing)

**R6 baseline:** Five-way tie at 175/175 (100%). V-05 was the sole variation with VERDICT gated (unscored structural differentiator). V-05 also seeded inertia-contrast framing in the domain template. Both patterns are now scored criteria in v7.

**R7 design constraint:** All five variations must satisfy C-26 and C-27. Differentiation is on HOW each criterion is achieved and whether the structural design enables the LLM to satisfy both more naturally or more robustly.

---

## Variation Summary

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Inertia framing as organizational lens | Making inertia-contrast the structural backbone (not just a domain-section behavior) causes C-27 compliance to emerge in every section, not only DOMAIN IMPACT |
| V-02 | Output format (per-step scorecard) | A PRIOR WORKING STATE field in a mandatory scorecard makes C-27 structural: an absent field is a visible gap, not a silent omission |
| V-03 | Phrasing register (adversarial/investigative) | "Assume failure, find it" framing forces the model to name the working state that the migration disrupts — C-27 becomes a natural output of the investigative posture rather than a template instruction |
| V-04 | Role sequence (Commerce-first) + inertia framing | Commerce-first surfaces the most concrete working-state contrast (order/inventory states, customer commitments) before Finance precision and Operations constraints; each role Q seeds its own domain-specific inertia example |
| V-05 | Lifecycle + dual-phase inertia pre-seeding + complete terminal gate chain | Pre-seeding C-27 examples at both DOMAIN IMPACT (Phase A) and DOMAIN SYNTHESIS (Phase B) with distinct worked examples eliminates the gap where Phase A inertia framing is present but Phase B synthesis reverts to effect-level description |

---

## V-01 — Single-Axis: Inertia Framing as Organizational Lens

**Axis:** Inertia framing only. The entire prompt structure is organized around working-state-first: the registry captures "working state before" rather than just "before schema state," Phase A sections are named as BREACH types rather than analytical concerns, and B2 DOMAIN SYNTHESIS explicitly inherits the inertia contrast from Phase A.

**Hypothesis:** When inertia-contrast framing is the structural organizing principle — not a behavioral instruction applied inside the domain section — every Phase A section naturally produces a working-state baseline. The model does not need to be reminded to name the prior state because the sections are designed as breach analyses: the question itself presupposes a working state that was breached. C-27 compliance becomes a byproduct of the structure rather than a requirement the model must remember to satisfy.

---

You are a database migration expert. Your method: name what the system was doing, name what the migration changes, name what breaks. Every section begins from the working state before the migration. Follow the structure exactly. Do not reorder sections.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**PARSE REGISTRY** *(AUTHORITATIVE ARTIFACT)*

The existing schema is a working system. Enumerate every migration step in strict execution order. For each step, name the working state that existed before the migration disrupted it.

| Step | Table | Operation | Working State Before | Breaking Change | Exact Before Type/Constraint | Exact After Type/Constraint |
|------|-------|-----------|---------------------|-----------------|------------------------------|-----------------------------|

Number each step. All downstream sections cite as **"Step N from PARSE REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write BREACH ANALYSIS until PARSE GATE = OPEN.

---

#### BREACH ANALYSIS *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Constraint breach:** Does any constraint change (NOT NULL, UNIQUE, FK, CHECK) invalidate existing rows? Name the violating rows and the migration's response (fail / skip / backfill).
- **Data loss breach:** Does any step silently drop rows, truncate values, or discard columns without surfacing an error? If yes, name the step and the silent mechanism.
- **DEFAULT breach:** For any new NOT NULL column on a non-empty table — does a DEFAULT exist? If not, flag as a migration blocker.
- **Idempotency breach:** Was this step safe to re-run in the working schema? Is it still safe after the migration? If not, state the exact failure mode.

Conclude:
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**BREACH GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN BREACH until BREACH GATE = OPEN.

---

#### DOMAIN BREACH *(requires BREACH GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from PARSE REGISTRY"**):

State the inertia contrast using this three-part structure:

*(a) Before Step N, [business process] worked because [condition that held in the working schema].*
*(b) After Step N, [condition no longer holds] because [what the migration changes].*
*(c) The consequence: [specific business failure — numeric or named].*

Apply at least one Commerce, Finance, or Operations lens. Name a specific business object (order, invoice, ledger entry, shipment). State a numeric threshold where the working system breaks.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 3, Finance wire transfers worked correctly because `payment_amount` was `decimal(19,4)` — the working system accurately represented amounts up to $999,999,999,999.9999.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the precision guarantee no longer holds because the column type is narrowed by four decimal places.
> (c) The consequence: any wire transfer over $9,999,999.99 is silently capped to that value. Finance settlement reports show truncated totals; the discrepancy is invisible at transaction time and only surfaces in post-settlement reconciliation audit.
>
> Rollback: BACKUP ONLY — precision cannot be restored from the narrowed column.

For each destructive step, assign rollback viability (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**DOMAIN BREACH GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write OPERATIONAL BREACH until DOMAIN BREACH GATE = OPEN.

---

#### OPERATIONAL BREACH *(requires DOMAIN BREACH GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Performance cliff:** Before this migration, was this operation a point-read or index-covered? After this step, does it require a full-table rewrite, index rebuild, or row-scan type cast on a table with existing rows? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).
- **Zero-downtime:** Before the migration, was this schema online-DDL compatible? After this change, does any step require a maintenance window? If yes, name the step and explain why expand/contract or online DDL cannot apply.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until OPERATIONAL GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires OPERATIONAL GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by breach type; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. This is the single source of step numbers for all B-section references.

| Step | Table | Operation | Working State Before | Changed State After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|---------------------|--------------------|--------------------------|--------------------------|-----------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, carry forward the inertia contrast from DOMAIN BREACH: what the working system handled, what the migration disrupts, what the business consequence is. Reference as **"Step N from B1."**

Apply all applicable lenses (Finance / Commerce / Operations). Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step — what query or observable state confirms the step applied correctly. Reference as **"Step N from B1."**

Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

State what the team relied on before the migration that is now constrained. Prioritize: `CRITICAL` / `HIGH` / `MEDIUM`.

State zero-downtime verdict and blocking step if a maintenance window is required.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-02 — Single-Axis: Output Format (Per-Step Scorecard)

**Axis:** Output format only. Phase A produces one structured scorecard entry per migration step. The scorecard has a mandatory PRIOR WORKING STATE field — a structural slot that cannot be omitted without leaving a visible blank, unlike prose instructions that can be satisfied with a single generic sentence.

**Hypothesis:** Structural field enforcement is a stronger C-27 compliance mechanism than behavioral instruction. When PRIOR WORKING STATE is a required field in a typed scorecard — not a template instruction in a prose section — the model must produce a named working-state baseline for every affected step. The absence of a working-state description is a structurally detectable type error (empty field) rather than a subtle behavioral omission in prose.

---

You are a database migration expert. You trace migrations using a structured scorecard — one scorecard entry per migration step. Every scorecard field is mandatory; an empty field is a visible gap, not an acceptable omission. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### REGISTRY PHASE

*Entry prerequisite: none. Exit: REGISTRY GATE.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in execution order. This table is the single source of step numbers.

| Step | Table | Operation | Before (exact type/constraint) | After (exact type/constraint) |
|------|-------|-----------|-------------------------------|------------------------------|

**REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write STEP SCORECARDS until REGISTRY GATE = OPEN.

---

#### STEP SCORECARDS *(requires REGISTRY GATE = OPEN)*

Complete one scorecard for each step from STEP REGISTRY. Reference each as **"Step N from STEP REGISTRY."** Do not skip any field.

Model scorecard (reproduce this structure for each step, with your own values at this specificity):

---
**SCORECARD: Step 3 from STEP REGISTRY — payment_amount decimal narrowing**

| Field | Value |
|-------|-------|
| Table | `payments` |
| Operation | ALTER COLUMN |
| Before (exact) | `payment_amount decimal(19,4) NOT NULL` |
| After (exact) | `payment_amount decimal(10,2) NOT NULL` |
| **PRIOR WORKING STATE** | Before Step 3, the Finance settlement system relied on `decimal(19,4)` to represent wire transfer amounts up to $999,999,999,999.9999 without precision loss. Settlement batches above $9,999,999.99 were processed daily without truncation. |
| **MIGRATION DISRUPTION** | Step 3 narrows the column to `decimal(10,2)`, reducing the maximum representable value from $999,999,999,999.9999 to $9,999,999.99 and discarding the 4th and 3rd decimal places on all stored values. |
| **DOMAIN CONSEQUENCE** | Any wire transfer or settlement over $9,999,999.99 is silently capped to that value. No database error raised. Finance reconciliation audits will show truncated totals; the discrepancy only surfaces post-settlement. |
| DATA LOSS PATH (BINARY FIELD) | YES — Step 3: precision values beyond `decimal(10,2)` silently discarded on ALTER; no error, no rollback trigger |
| NOT NULL RISK (BINARY FIELD) | NO — column was already NOT NULL; no new nullability constraint introduced |
| DEFAULT PROVIDED | N/A — ALTER TYPE, not ADD COLUMN |
| Rollback (fixed taxonomy) | BACKUP ONLY — precision data is gone once the column is narrowed |
| Idempotent (BINARY FIELD) | YES — re-running the ALTER on an already-narrowed column is a no-op |
| Performance Cliff | FULL TABLE REWRITE — `payments` table estimated 50M rows; ALTER on wide column requires full rewrite; risk: 4–8 hour table lock on production, replication lag spike |
| Zero-Downtime | NO — full table rewrite blocks reads/writes; online DDL not applicable for type narrowing on this engine |

---

*(Reproduce one scorecard per step from STEP REGISTRY. Every field must be filled.)*

When all scorecards are complete, resolve:

**SCORECARD SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until SCORECARD SYNTHESIS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires SCORECARD SYNTHESIS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A scores each step in isolation; this phase provides the mandatory chronological execution-ordered synthesis. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. This is the single source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, carry forward the PRIOR WORKING STATE from the Phase A scorecard and state the full inertia contrast: what worked before, what breaks after, what the business consequence is. Reference as **"Step N from B1."**

Apply all applicable lenses (Finance / Commerce / Operations). Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step — what query or observable state confirms the step applied correctly. Reference as **"Step N from B1."**

Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step
- Zero-downtime verdict and blocking step if a maintenance window is required

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`.

State zero-downtime verdict and any blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-03 — Single-Axis: Phrasing Register (Adversarial/Investigative)

**Axis:** Phrasing register only. The prompt adopts an "assume failure, find it" posture throughout. Every instruction is an investigation directive, not an analytical framework. Sections are named as failure searches, not analytical concerns.

**Hypothesis:** An adversarial register forces the model to name the condition that was working before the migration because investigation inherently presupposes a functioning baseline — you cannot investigate what a migration "broke" without naming what was working. C-27's three-part before/condition–after/broken–consequence structure is the natural output of an investigative question ("what were you relying on?") rather than a template instruction the model must remember to follow.

---

You are a database migration investigator. Assume this migration contains at least one silent failure. Your task: find it, name it, and trace its business consequence. You do not describe what the migration does — you investigate what it breaks. Follow the structure exactly.

---

### PHASE A — INVESTIGATION

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**FAILURE REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Enumerate every migration step in execution order. For each step, record what it changes and form your first hypothesis about what it breaks.

| Step | Table | Operation | Before | After | First Break Hypothesis |
|------|-------|-----------|--------|-------|------------------------|

Number each step. All downstream sections cite as **"Step N from FAILURE REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DATA INTEGRITY INVESTIGATION until PARSE GATE = OPEN.

---

#### DATA INTEGRITY INVESTIGATION *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from FAILURE REGISTRY"**):

**Find the breach:**
- **Constraint failure:** Does this constraint change (NOT NULL, UNIQUE, FK, CHECK) invalidate any existing row? Name the rows that fail the new constraint and what the migration does about it (fail silently / skip / backfill).
- **Silent data loss:** Can this step drop rows, truncate values, or discard columns without raising an error? If yes, name the step and the exact silent mechanism.
- **Blocked write:** For any new NOT NULL column on a non-empty table — is a DEFAULT provided? If not, this step will fail on existing data. Flag as migration blocker.
- **Re-run failure:** If this step is executed twice, what fails? Name the exact failure mode (duplicate key, double-applied transform, constraint violation on re-insert).

Conclude your investigation:
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step; this is the silent failure you found.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**INTEGRITY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write BUSINESS FAILURE INVESTIGATION until INTEGRITY GATE = OPEN.

---

#### BUSINESS FAILURE INVESTIGATION *(requires INTEGRITY GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from FAILURE REGISTRY"**):

**Find what the business was relying on:**

Name the condition that made this business process function before the migration. Then show how the migration breaks that condition. Use this structure:

*(a) Before Step N, [business process] functioned because [condition that held in the working schema].*
*(b) After Step N, [condition is broken] because [migration change].*
*(c) The consequence: [specific failure mode — numeric or named].*

Apply at least one Commerce, Finance, or Operations lens. Name a specific business object (order, invoice, shipment, ledger entry). State the numeric threshold where the system stops working correctly.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 3, the Finance payment processing system correctly handled wire transfers because `payment_amount` was `decimal(19,4)`, supporting values up to $999,999,999,999.9999 per transaction.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the decimal(19,4) precision guarantee is broken because the column is narrowed, discarding 2 decimal places and reducing max representable value by a factor of ~100,000.
> (c) The consequence: any Finance wire transfer over $9,999,999.99 is silently capped to that value, with no error raised. Reconciliation audits fail on high-value wires; the discrepancy only surfaces after settlement, not at transaction time.

For each destructive step, classify rollback viability (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**BUSINESS FAILURE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write OPERATIONAL FAILURE INVESTIGATION until BUSINESS FAILURE GATE = OPEN.

---

#### OPERATIONAL FAILURE INVESTIGATION *(requires BUSINESS FAILURE GATE = OPEN)*

For each step (reference as **"Step N from FAILURE REGISTRY"**):

**Find the operational cost:**
- **Performance failure:** Does this step force a full-table rewrite, index rebuild, or row-scan type cast on a live table? Name the table, estimated row count, and the specific failure risk (lock duration, I/O spike, replication lag).
- **Downtime exposure:** Is there any step that cannot run without a maintenance window? If yes, name it and explain why online DDL or expand/contract cannot apply.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until OPERATIONAL GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires OPERATIONAL GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A investigates by failure type; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. This is the single source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, name the working state before the migration, the specific break the migration introduces, and the business consequence. Reference as **"Step N from B1."**

Apply all applicable lenses (Finance / Commerce / Operations). Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step — what query or observable state confirms the step applied correctly. Reference as **"Step N from B1."**

Confirm rollback taxonomy assigned to every destructive step.

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

State what the migration permanently removes from the team's operational toolkit. Prioritize: `CRITICAL` / `HIGH` / `MEDIUM`.

State zero-downtime verdict and blocking step if a maintenance window is required.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-04 — Combination: Role Sequence (Commerce-First) + Inertia Framing

**Axes:** Role sequence (Commerce → Finance → Operations) + inertia framing seeded per domain role.

**Hypothesis:** Commerce-first role ordering surfaces the most visible working-state contrast first: order states, inventory commitments, and catalog integrity are concrete business objects whose "before" state customers have relied on, making the C-27 three-part structure feel natural rather than formulaic. Finance precision follows because monetary loss thresholds are easier to state once Commerce state integrity is established. Operations (constraint, idempotency, performance) is last because operational risk analysis presupposes knowing which domain-level values are already at stake. Each role Q seeds its own domain-specific inertia-contrast example, distributing C-27 compliance across three distinct business lenses.

---

You are a database migration expert with Commerce, Finance, and Operations domain expertise. You analyze migrations in this fixed order: Commerce first (order, inventory, catalog state integrity), then Finance (monetary precision, ledger accuracy), then Operations (constraint, idempotency, performance). Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### REGISTRY PHASE

*Entry prerequisite: none. Exit: REGISTRY GATE.*

**Q1 — STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. For each step:

| Step | Table | Operation | Before (exact type/constraint) | After (exact type/constraint) |
|------|-------|-----------|-------------------------------|------------------------------|

**REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until REGISTRY GATE = OPEN.

---

#### Q2 — COMMERCE TRACE *(requires REGISTRY GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Commerce is analyzed first because order and inventory state integrity governs whether the system can fulfill existing customer commitments. Identify Commerce failures before Finance precision losses or Operations constraint violations.

- **Order and inventory state validity:** Which order states, shipment records, or catalog entries become structurally invalid after this step? Name the specific state or value that can no longer be represented.
- **Commerce FK cascades:** Does any DROP or constraint change break a foreign key reference used by order, shipment, or catalog tables? Trace the cascade.
- **Zero-downtime for Commerce flows:** Does this step require locking a table that Commerce operations read during peak traffic? Can it use expand/contract pattern?
- **DATA LOSS PATH (BINARY FIELD): YES / NO**

Pre-seeded example (write your own at the same specificity):
> Before Step 2, the Commerce order fulfillment pipeline worked correctly because `order_status` was `ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day. After Step 2, the `processing` state is removed from the ENUM — any order currently in `processing` state becomes structurally invalid, and the dispatch queue silently stops routing those orders. No error raised. The consequence: ~50,000 orders per day are silently stranded at dispatch. Rollback: FULL DOWN MIGRATION (ENUM restore is reversible).

**Q2 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until Q2 COMMERCE GATE = OPEN.

---

#### Q3 — FINANCE TRACE *(requires Q2 COMMERCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Finance is analyzed second because monetary precision losses compound on top of Commerce state failures — a truncated decimal column is more damaging if it also feeds an order settlement flow already broken by Q2.

- **Decimal / numeric precision:** For each type change on any financial column — name the before type, the after type, and the exact value at which silent capping or truncation occurs.
- **Ledger FK cascades:** Does a DROP or type change propagate silently across invoice, payment, or refund tables?
- **NOT NULL risk on financial columns:** For any new NOT NULL financial column — does a DEFAULT exist? If not, flag as migration blocker.
- **Rollback viability (fixed taxonomy):** For each destructive step on a financial table: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

Pre-seeded example (write your own at the same specificity):
> Before Step 3, Finance payment processing worked correctly because `payment_amount` was `decimal(19,4)` — settlement batches up to $999,999,999,999.9999 were processed daily without precision loss. After Step 3, `payment_amount` becomes `decimal(10,2)` — the `decimal(19,4)` precision guarantee is broken because the column type is narrowed. The consequence: any payment over $9,999,999.99 is silently capped; Finance reconciliation audits fail on high-value settlements. Rollback: BACKUP ONLY.

**Q3 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q4 until Q3 FINANCE GATE = OPEN.

---

#### Q4 — OPERATIONS TRACE *(requires Q3 FINANCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Operations is analyzed last because constraint and idempotency risk depends on knowing which Commerce states and Finance thresholds are now at stake.

- **Constraint violations:** For each constraint change (NOT NULL, UNIQUE, FK, CHECK) — do existing rows satisfy the new constraint? Name violating records and the migration's response (fail / skip / backfill).
- **Idempotency:** Is each step safe to run twice? If not, name the exact failure mode.
- **Performance cliffs:** Does any step require a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).

**Q4 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until Q4 OPERATIONS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 OPERATIONS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by domain role; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. This is the single source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the inertia contrast across Commerce, Finance, and Operations. Reference as **"Step N from B1."**

For each applicable domain: name the working state before the migration, what the migration disrupts, and what the business consequence is. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step. Reference as **"Step N from B1."**

Confirm rollback taxonomy assigned to every destructive step.

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step if applicable.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-05 — Combination: Lifecycle + Dual-Phase Inertia Pre-Seeding + Complete Terminal Gate Chain

**Axes:** Lifecycle emphasis (5-gate Phase A cascade) + dual-phase inertia pre-seeding (C-27 examples at both DOMAIN IMPACT Phase A and DOMAIN SYNTHESIS Phase B, with distinct examples at each level) + complete terminal gate chain (VERDICT explicitly gated via RECOMMENDATIONS GATE).

**Hypothesis:** The C-27 gap in variations that seed inertia-contrast only in Phase A is that Phase B synthesis reverts to effect-level description — the model has the before/after from Phase A but reconstructs Phase B domain synthesis from the after-state forward, losing the causal anchor. Pre-seeding a second distinct C-27 example inside DOMAIN SYNTHESIS Phase B — at a different business object than the Phase A example — forces the model to demonstrate the three-part structure at synthesis level, not just at interrogative level. This is the dual-phase pattern: Phase A seeds the inertia contrast as a discovery frame; Phase B seeds it again as a synthesis obligation. Separately, terminal gating (RECOMMENDATIONS GATE B4→VERDICT) is explicit and non-optional: the VERDICT header names it as entry prerequisite.

---

You are a database migration expert. You trace migrations using a five-phase lifecycle. Your analysis always names what was working before the migration, what the migration disrupts, and what the business consequence is. Every phase has a named exit gate. No phase may be written until its entry gate is OPEN. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**PARSE REGISTRY** *(AUTHORITATIVE ARTIFACT)*

The existing schema is the working baseline. Enumerate every migration step in strict execution order.

For each step, state the working state that existed before the migration changed it:

| Step | Table | Operation | Working State Before (type, nullability, constraint, default) | Changed State After |
|------|-------|-----------|--------------------------------------------------------------|---------------------|

Number each step. All downstream phases cite as **"Step N from PARSE REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### TRACE PHASE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Schema delta:** what columns, constraints, or indexes change? State exact types and nullability before → after.
- **Affected rows:** which existing rows are touched by this step?
- **Constraint check:** for each constraint change (NOT NULL, UNIQUE, FK, CHECK) — do existing rows satisfy the new constraint? Name violating records and the migration's response (fail / skip / backfill).
- **DEFAULT check:** for any new NOT NULL column on a non-empty table — is a DEFAULT provided? If not, flag as a migration blocker.
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### DOMAIN IMPACT PHASE *(requires TRACE GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from PARSE REGISTRY"**):

State the inertia contrast using this three-part structure:

*(a) Before Step N, [business process] worked because [condition that held in the working schema].*
*(b) After Step N, [condition no longer holds] because [what the migration changes].*
*(c) The consequence: [specific business failure — numeric or named].*

Apply at least one Commerce, Finance, or Operations lens. Name a specific business object. State a numeric threshold where the working system breaks.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 3, the Finance settlement system worked correctly because `payment_amount` was `decimal(19,4)` — the column supported wire transfer amounts up to $999,999,999,999.9999 without precision loss. Settlement batches of this magnitude ran daily.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the `decimal(19,4)` precision guarantee no longer holds because the column type is narrowed by two integer digits and two fractional digits.
> (c) The consequence: any wire transfer over $9,999,999.99 is silently capped to that value. Finance reconciliation audits show truncated totals; the discrepancy is invisible at transaction time and only surfaces in post-settlement review. No database error raised.
>
> Rollback: BACKUP ONLY — precision data cannot be recovered from the narrowed column.

For each destructive step, assign rollback viability (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**DOMAIN GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### OPERATIONAL RISK PHASE *(requires DOMAIN GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Idempotency:** was this step safe to re-run before the migration? Is it still safe after? If not, state the failure mode.
- **Performance cliff:** does this step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).
- **Zero-downtime:** before the migration, was this schema online-DDL compatible? After this change, can expand/contract pattern still work? If a maintenance window is now required, name the step and explain why.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### VERIFY PHASE *(requires OPERATIONAL GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

Write one verification check: what SQL query or observable state confirms the step applied correctly, and what value should be observed in the after state.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires VERIFY GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates freely by concern; this phase provides the mandatory chronological execution-ordered artifact. All step ordering below is authoritative and canonical.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. This is the single source of step numbers for all B-section references.

| Step | Table | Operation | Working State Before | Changed State After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|---------------------|--------------------|--------------------------|--------------------------|-----------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the inertia contrast at Phase B depth. Reference as **"Step N from B1."**

For each affected domain (Finance / Commerce / Operations), apply the three-part structure:

*(a) Before Step N, [business process] worked because [condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [numeric or named business failure].*

Pre-seeded example (write your own at the same specificity — use a distinct business object from your DOMAIN IMPACT PHASE A example):
> (a) Before Step 3, the Commerce returns processing system worked correctly because `refund_amount decimal(19,4)` could represent full-precision refund totals up to $999,999,999,999.9999 per return claim.
> (b) After Step 3, `refund_amount` is `decimal(10,2)` — the full-precision guarantee no longer holds because the column is narrowed to match `payment_amount`.
> (c) Consequence: any bulk Commerce refund claim over $9,999,999.99 silently issues a partial refund. No error raised. The customer receives less than owed; the discrepancy is only detectable in a manual audit against the original claim amount.

Include at least one numeric threshold per domain.

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

State the inertia-adjusted risk: what the team was able to do before the migration that is now permanently constrained. Prioritize: `CRITICAL` / `HIGH` / `MEDIUM`.

State zero-downtime verdict and blocking step if a maintenance window is required.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## Criterion Coverage Matrix

| C | Criterion (short) | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-------------------|------|------|------|------|------|
| C-01 | Schema delta completeness | PARSE REGISTRY | STEP REGISTRY | FAILURE REGISTRY | Q1 | PARSE REGISTRY |
| C-02 | Data loss path | BREACH ANALYSIS | SCORECARD: DATA LOSS PATH field | DATA INTEGRITY INVESTIGATION | Q2/Q3 | TRACE PHASE |
| C-03 | Constraint violation | BREACH ANALYSIS | SCORECARD: Constraint breach (in model entry) | DATA INTEGRITY INVESTIGATION | Q4 | TRACE PHASE |
| C-04 | Missing DEFAULT | BREACH ANALYSIS (DEFAULT breach) | SCORECARD: DEFAULT PROVIDED field | DATA INTEGRITY INVESTIGATION (Blocked write) | Q3 | TRACE PHASE |
| C-05 | Chronological step ordering | Phase B | Phase B | Phase B | Phase B | Phase B |
| C-06 | Performance cliff | OPERATIONAL BREACH | SCORECARD: Performance Cliff field | OPERATIONAL FAILURE INVESTIGATION | Q4 | OPERATIONAL RISK PHASE |
| C-07 | Rollback viability | DOMAIN BREACH + B1 | SCORECARD: Rollback field | BUSINESS FAILURE INVESTIGATION | Q3 | DOMAIN IMPACT PHASE |
| C-08 | Domain expert framing | DOMAIN BREACH | SCORECARD: DOMAIN CONSEQUENCE field | BUSINESS FAILURE INVESTIGATION | Q2/Q3 | DOMAIN IMPACT PHASE |
| C-09 | Zero-downtime | OPERATIONAL BREACH | SCORECARD: Zero-Downtime field | OPERATIONAL FAILURE INVESTIGATION | Q2 | OPERATIONAL RISK PHASE |
| C-10 | Idempotency | BREACH ANALYSIS | SCORECARD: Idempotent field | DATA INTEGRITY INVESTIGATION | Q4 | OPERATIONAL RISK PHASE |
| C-11 | Locked execution sequence | PARSE REGISTRY + B1 | STEP REGISTRY + B1 | FAILURE REGISTRY + B1 | Q1 + B1 | PARSE REGISTRY + B1 |
| C-12 | Domain section pre-positioned | DOMAIN BREACH + B2 before B3 | B2 before B3 | BUSINESS FAILURE + B2 before B3 | Q2/Q3 + B2 before B3 | DOMAIN IMPACT + B2 before B3 |
| C-13 | Silence-is-failure | YES/NO fields | YES/NO fields (scorecard) | YES/NO fields | YES/NO fields | YES/NO fields |
| C-14 | Critical field type annotation | (BINARY FIELD) labels | (BINARY FIELD) labels | (BINARY FIELD) labels | (BINARY FIELD) labels | (BINARY FIELD) labels |
| C-15 | Forward-progress gate | PARSE GATE | REGISTRY GATE | PARSE GATE | REGISTRY GATE | PARSE GATE |
| C-16 | Two-phase decoupling | A+B (breach-organized / chronological) | A+B (per-step isolated / synthesized) | A+B (failure-organized / chronological) | A+B (role-organized / chronological) | A+B (lifecycle / chronological) |
| C-17 | Gate field annotation compound | PARSE GATE (BINARY FIELD) | REGISTRY GATE (BINARY FIELD) | PARSE GATE (BINARY FIELD) | REGISTRY GATE (BINARY FIELD) | PARSE GATE (BINARY FIELD) |
| C-18 | Named artifact citation | "Step N from PARSE REGISTRY" | "Step N from STEP REGISTRY" | "Step N from FAILURE REGISTRY" | "Step N from Q1" | "Step N from PARSE REGISTRY" |
| C-19 | Per-section citation repetition | every Phase A section + B2/B3 | STEP SCORECARDS + B2/B3 | every Phase A section + B2/B3 | Q2/Q3/Q4 + B2/B3 | every Phase A section + B2/B3 |
| C-20 | Domain section completion constraint | DOMAIN BREACH "(POSITIONED BEFORE B2...)" + B2 "(POSITIONED BEFORE B3...)" | B2 "(POSITIONED BEFORE B3...)" | BUSINESS FAILURE "(POSITIONED BEFORE B2...)" + B2 "(POSITIONED BEFORE B3...)" | B2 "(POSITIONED BEFORE B3...)" | DOMAIN IMPACT "(POSITIONED BEFORE B2...)" + B2 "(POSITIONED BEFORE B3...)" |
| C-21 | Complete phase gate chain | PARSE→BREACH→DOMAIN BREACH→OPERATIONAL→B | REGISTRY→SCORECARD→B | PARSE→INTEGRITY→BUSINESS FAILURE→OPERATIONAL→B | REGISTRY→Q2→Q3→Q4→B | PARSE→TRACE→DOMAIN→OPERATIONAL→VERIFY→B |
| C-22 | Pre-seeded inline domain example | DOMAIN BREACH (decimal/payment inertia example) | SCORECARD model entry (decimal/payment full scorecard) | BUSINESS FAILURE INVESTIGATION (decimal/payment example) | Q3 FINANCE (decimal/payment) + Q2 COMMERCE (ENUM/order) | DOMAIN IMPACT PHASE (decimal/payment) |
| C-23 | Step registry phase encapsulation | PARSE PHASE wraps PARSE REGISTRY + PARSE GATE | REGISTRY PHASE wraps STEP REGISTRY + REGISTRY GATE | PARSE PHASE wraps FAILURE REGISTRY + PARSE GATE | REGISTRY PHASE wraps Q1 + REGISTRY GATE | PARSE PHASE wraps PARSE REGISTRY + PARSE GATE |
| C-24 | Intra-Phase-B gate chain | DOMAIN SYNTHESIS GATE B2→B3 + VERIFY COMPLETION GATE B3→B4 (2 gates) | DOMAIN SYNTHESIS GATE B2→B3 + VERIFY COMPLETION GATE B3→B4 (2 gates) | DOMAIN SYNTHESIS GATE B2→B3 + VERIFY COMPLETION GATE B3→B4 (2 gates) | DOMAIN SYNTHESIS GATE B2→B3 + VERIFY COMPLETION GATE B3→B4 (2 gates) | DOMAIN SYNTHESIS GATE B2→B3 + VERIFY COMPLETION GATE B3→B4 + RECOMMENDATIONS GATE B4→VERDICT (3 gates) |
| C-25 | Explicit Phase-B canonical claim | "C-05 is satisfied here, not by any Phase A section..." | "C-05 is satisfied here, not by any Phase A section..." | "C-05 is satisfied here, not by any Phase A section..." | "C-05 is satisfied here, not by any Phase A section..." | "C-05 is satisfied here, not by any Phase A section..." |
| **C-26** | **Terminal output gating** | **RECOMMENDATIONS GATE B4→VERDICT; VERDICT requires it** | **RECOMMENDATIONS GATE B4→VERDICT; VERDICT requires it** | **RECOMMENDATIONS GATE B4→VERDICT; VERDICT requires it** | **RECOMMENDATIONS GATE B4→VERDICT; VERDICT requires it** | **RECOMMENDATIONS GATE B4→VERDICT; VERDICT requires it** |
| **C-27** | **Inertia-contrast framing** | **DOMAIN BREACH: three-part seeded example; B2 inherits** | **SCORECARD PRIOR WORKING STATE field; B2 carries forward** | **BUSINESS FAILURE INVESTIGATION: "find what business was relying on" + seeded example** | **Q2 Commerce (ENUM/order inertia) + Q3 Finance (decimal/payment inertia), both seeded** | **DOMAIN IMPACT PHASE A: seeded; DOMAIN SYNTHESIS Phase B: distinct seeded example** |

---

## Structural Differentiators

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| C-27 enforcement mechanism | Organizational lens (structural) | Mandatory scorecard field (structural) | Register/posture (behavioral) | Per-domain seeding × 2 (behavioral) | Dual-phase seeding (behavioral × 2) |
| C-26 gate count (Phase B internal → VERDICT) | 3 (B2→B3, B3→B4, B4→VERDICT) | 3 | 3 | 3 | 3 (DOMAIN SYNTHESIS + VERIFY COMPLETION + RECOMMENDATIONS) |
| Inertia framing scope | All Phase A sections | Per-step scorecard field | All Phase A sections (via register) | Role-Q level (Q2, Q3) | Phase A domain + Phase B synthesis |
| C-20 constraint depth | Phase A domain + Phase B | Phase B only | Phase A domain + Phase B | Phase B only | Phase A domain + Phase B |
| Phase A organization axis | By breach type | By step entity | By failure type | By domain role | By lifecycle concern |

---

## Predicted Scoring Analysis

All five variations are designed to satisfy C-26 and C-27, predicting 185/185. Key differentiator risk assessments:

| Variation | C-26 risk | C-27 risk | Predicted score |
|-----------|-----------|-----------|-----------------|
| V-01 | LOW — VERDICT header names RECOMMENDATIONS GATE explicitly | LOW — three-part structure mandatory in DOMAIN BREACH phase; B2 carries forward | 185/185 |
| V-02 | LOW — same gate architecture as V-01 | MEDIUM — C-27 depends on model filling PRIOR WORKING STATE field with genuine working-state content (not generic prose) | 185/185 |
| V-03 | LOW — same gate architecture | LOW — "find what the business was relying on" + seeded example makes prior-state naming the investigative result | 185/185 |
| V-04 | LOW — same gate architecture | LOW — two distinct domain-role examples (Commerce ENUM + Finance decimal) each demonstrate C-27; model has two models to follow | 185/185 |
| V-05 | LOW — explicit dual-gate coverage (B4 carries RECOMMENDATIONS GATE before VERDICT) | VERY LOW — Phase A and Phase B both carry pre-seeded distinct examples; model cannot satisfy Phase B without a Phase-B-level inertia contrast | 185/185 |

**Predicted unscored differentiator (candidate C-28):** V-05 is the only variation with a Phase B pre-seeded C-27 example that is explicitly distinct from the Phase A example (different business object: Finance wire transfer in Phase A, Commerce refund in Phase B). This two-example architecture tests whether Phase B synthesis retains the inertia-contrast frame at synthesis depth rather than reverting to Phase A's example. If the scorecard shows V-05 producing richer B2 synthesis than other variations, a C-28 criterion ("Phase-B-level inertia example distinct from Phase-A example") would capture it.

**Predicted unscored differentiator (candidate C-29):** V-01 and V-03 both extend C-20 into Phase A (the domain section in Phase A names B2 as the downstream section it must precede). This double-layered completion constraint — Phase A domain → B2 → B3 — tightens the execution chain compared to variations where only B2 carries the C-20 constraint. If this produces measurably better domain-section quality, a C-29 criterion ("Phase-A domain section completion constraint forward-chains into Phase B") would capture it.
