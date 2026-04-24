# trace-migration — Round 8 Variations (v8 rubric)

**New criteria this round:** C-28 (all-constraint-type structured fields), C-29 (Phase-A cross-role analytical coverage parity), C-30 (dual-phase inertia-contrast seeding)

**R7 baseline:** V-01, V-03, V-05 scored 185/185 (100%). V-02 PARTIAL on C-03 (FK/UNIQUE/CHECK in free-form MIGRATION DISRUPTION). V-04 PARTIAL on C-04 (DEFAULT check scoped to financial columns) and C-09 (zero-downtime Commerce-only).

**R8 design constraint:** All five variations must satisfy C-28, C-29, and C-30. Differentiation is on HOW each criterion is achieved and whether the structural mechanism produces the criterion naturally or requires the model to remember a behavioral instruction.

---

## Variation Summary

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Output format (constraint-type taxonomy table) | A CONSTRAINT TYPE REGISTRY with four mandatory rows forces C-28 at parse time: each constraint type occupies a named slot before any analysis is written, making a missing constraint-type slot structurally visible rather than an analytical omission |
| V-02 | Role sequence (parity-first mandate) | Printing the complete required checklist as a PARITY ENFORCEMENT BLOCK before the first role section, with explicit "DO NOT SCOPE OR SHORTEN" language, forces C-29 compliance before the model writes Q2 — preventing the pattern where zero-downtime is scoped to Commerce and DEFAULT checks are scoped to financial columns |
| V-03 | Inertia framing (named dual-phase seed slots with distinctness requirement) | Naming the inertia-contrast slots as required output artifacts — PHASE-A-INERTIA-SEED and PHASE-B-INERTIA-SEED — with an explicit DISTINCTNESS REQUIREMENT that names what "distinct" means (different step, table, or business consequence), eliminates the C-30 failure mode where Phase B copies Phase A's example |
| V-04 | Combined: output format + role sequence (C-28 + C-29) | The constraint taxonomy table and the parity mandate are structurally independent and compound cleanly: each role section references the constraint type registry for C-28 and applies the uniform checklist for C-29 |
| V-05 | Combined: lifecycle + all three axes (C-28 + C-29 + C-30) | A five-phase lifecycle structure distributes all three new structural obligations across named phases, reducing overload at any single phase: PARSE PHASE establishes the constraint type registry (C-28), domain-role TRACE sections apply the parity checklist (C-29), and named inertia seed slots span both phases (C-30) |

---

## V-01 — Single-Axis: Output Format (Constraint-Type Taxonomy Table)

**Axis:** Output format only. The CONSTRAINT TYPE REGISTRY at parse time creates four dedicated rows — one per constraint type — that must be filled before any analysis section is written. Per-constraint binary fields propagate through Phase A and into the B1 execution table.

**Hypothesis:** When constraint-type routing is a data-entry obligation at parse time — not an analytical judgment made inline — the model cannot route FK or CHECK violations into a free-form field without leaving the corresponding CONSTRAINT TYPE REGISTRY row visibly incomplete. C-28 compliance becomes a structural consequence of filling the registry rather than a requirement the model must remember. The taxonomy table also unlocks per-constraint binary columns in B1, making C-28 enforcement extend into the canonical output phase.

**Primary target:** C-28. Secondary coverage: C-29 via Commerce/Finance/Operations sub-sections in DOMAIN IMPACT. C-30 via standard dual-phase seeding.

---

You are a database migration expert. You trace migrations using a structured two-phase format. Every constraint type present in the migration has its own dedicated analysis field — no constraint violation analysis is routed through free-form notes or generic fields. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order.

| Step | Table | Operation | Before (exact type/constraint) | After (exact type/constraint) |
|------|-------|-----------|-------------------------------|------------------------------|

**CONSTRAINT TYPE REGISTRY**

Fill all four rows. Each row is mandatory regardless of whether the migration contains a violation of that type. "Present in Migration" means the migration adds, removes, or changes a constraint of this type.

| Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated |
|-----------------|---------------------|-----------------|-------------------|-------------------------------|
| NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| FK              | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                               |

Number each step. All downstream sections cite as **"Step N from STEP REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write CONSTRAINT TRACE until PARSE GATE = OPEN and all four CONSTRAINT TYPE REGISTRY rows are filled.

---

#### CONSTRAINT TRACE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from STEP REGISTRY"**):

Analyze each constraint type in its own dedicated sub-section. Do not merge constraint types into a shared field or free-form note.

**NOT NULL:**
- For each new NOT NULL column on a non-empty table: is a DEFAULT provided? If not, flag as migration blocker.
- Do existing rows satisfy this constraint? Name violating records and migration's response (fail / skip / backfill).
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**FK:**
- Do existing rows satisfy this FK constraint? Name violating records and migration's response.
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**UNIQUE:**
- Do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**CHECK:**
- Do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

Conclude:
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism (silent row drop, value truncation, column discard).
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode.

**CONSTRAINT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN IMPACT until CONSTRAINT GATE = OPEN.

---

#### DOMAIN IMPACT *(requires CONSTRAINT GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Apply the same complete checklist to ALL THREE domain lenses below. Do not scope or shorten any item for any lens.

**Required checklist per lens:**
1. Zero-downtime viability: can this step run without a maintenance window? If not, name the blocking step and why expand/contract or online DDL cannot apply.
2. DEFAULT presence: for every new NOT NULL column — is a DEFAULT provided? Flag missing DEFAULTs regardless of column domain label.
3. Inertia-contrast: state the three-part working-state-first structure (see template below).
4. Rollback viability (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**Commerce Lens:**
[Apply all four checklist items. Reference steps from STEP REGISTRY.]

**Finance Lens:**
[Apply all four checklist items — same checklist as Commerce. Reference steps from STEP REGISTRY.]

**Operations Lens:**
[Apply all four checklist items — same checklist as Commerce. Reference steps from STEP REGISTRY.]

Inertia-contrast template:

*(a) Before Step N, [business process] worked because [specific condition in the working schema].*
*(b) After Step N, [condition no longer holds] because [what the migration changes].*
*(c) The consequence: [specific business failure — numeric or named].*

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 3, Finance wire transfer processing worked correctly because `payment_amount decimal(19,4)` represented amounts up to $999,999,999,999.9999 without loss. Daily settlement batches at this scale ran without truncation.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the `decimal(19,4)` precision guarantee no longer holds; the column type is narrowed by two integer digits and two fractional digits.
> (c) The consequence: any wire transfer over $9,999,999.99 is silently capped. Finance reconciliation reports show truncated totals; the discrepancy only surfaces post-settlement. No database error raised.
>
> Rollback: BACKUP ONLY — precision data cannot be recovered from the narrowed column.

**DOMAIN IMPACT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write OPERATIONAL ANALYSIS until DOMAIN IMPACT GATE = OPEN.

---

#### OPERATIONAL ANALYSIS *(requires DOMAIN IMPACT GATE = OPEN)*

For each step (reference as **"Step N from STEP REGISTRY"**):

- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast on an existing table? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).
- **Zero-downtime (consolidated verdict):** after applying the per-lens zero-downtime checks in DOMAIN IMPACT, state the overall zero-downtime verdict here. If any step requires a maintenance window, name it.
- **Idempotency:** is each step safe to run twice? If not, name the exact failure mode.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until OPERATIONAL GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires OPERATIONAL GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by constraint type and concern; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — this example must name a different migration step, table, AND business consequence than your DOMAIN IMPACT Phase A example. Repeating the Phase A example does not satisfy this section.

*(a) Before Step N, [different process from Phase A] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different from Phase A example].*

Pre-seeded example (write your own — different step, table, and domain than your Phase A example):
> (a) Before Step 5, the Commerce inventory reservation system worked correctly because `reserved_qty integer NOT NULL DEFAULT 0` guaranteed every SKU had a valid reservation count — the DEFAULT 0 meant bulk catalog imports never needed to specify the field explicitly.
> (b) After Step 5, `DEFAULT 0` is removed from `reserved_qty` — the guarantee no longer holds; any INSERT without an explicit `reserved_qty` value fails the NOT NULL constraint.
> (c) Consequence: bulk SKU onboarding pipelines that relied on the default fail at write time with a constraint error instead of completing silently. ~12,000 SKU imports per day are affected; operators see constraint errors rather than successful catalog additions.
>
> Rollback: FULL DOWN MIGRATION — the DEFAULT clause is restorable via down migration.

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

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
- Zero-downtime verdict and blocking step if maintenance window required

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-02 — Single-Axis: Role Sequence (Parity-First Mandate)

**Axis:** Role sequence only. A PARITY ENFORCEMENT BLOCK is printed before the first role section, listing every required checklist item that must appear in ALL THREE role sections. The block includes explicit scoping prohibitions: zero-downtime is not scoped to Commerce tables only, DEFAULT checks are not scoped to financial columns only.

**Hypothesis:** The R7 V-04 gap (C-04 PARTIAL, C-09 PARTIAL) arose because the role sections had different analytical content: zero-downtime only in Q2, DEFAULT only for financial columns in Q3, no DEFAULT in Q4. Printing the full checklist as a hard constraint before Q2 — before the model writes any role section — creates a pre-commitment the model must satisfy for every role section or visibly violate. When the checklist includes zero-downtime AND DEFAULT checks with explicit "ALL ROLES — DO NOT SCOPE" language, the model must apply both to every domain or leave a detectable checklist gap.

**Primary target:** C-29. Secondary coverage: C-28 via per-role constraint binary fields. C-30 via per-role inertia seeding and distinct Phase B example.

---

You are a database migration expert with Commerce, Finance, and Operations domain expertise. You analyze migrations in a fixed role sequence: Commerce first, Finance second, Operations third. Every role section applies an identical analytical checklist — the checklist is not shortened, scoped, or reordered for any domain. Follow the structure exactly.

---

## PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in Q2, Q3, AND Q4 — without exception, without scoping to column subsets or domain-specific tables:**

1. **Zero-downtime viability** — can steps relevant to this domain run without a maintenance window using expand/contract or online DDL? If not, name the blocking step and explain why. *(Required in Commerce, Finance, AND Operations — not scoped to any single role.)*

2. **DEFAULT presence check** — for every new NOT NULL column on a non-empty table: is a DEFAULT provided? Flag missing DEFAULTs as migration blockers. *(Apply to ALL new NOT NULL columns — not only financial columns, not only Commerce columns.)*

3. **Constraint violation analysis** — for each constraint type, fill a dedicated binary field:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL

4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO

5. **Inertia-contrast example** — for at least one affected step: (a) before-state working condition, (b) how the migration breaks it, (c) specific business consequence with numeric threshold.

6. **Rollback viability** — for each destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE` (fixed taxonomy).

**If any item from this checklist is absent from any role section, the parity constraint is violated.**

---

### PHASE A — INTERROGATIVE

---

#### REGISTRY PHASE

*Entry prerequisite: none. Exit: REGISTRY GATE.*

**Q1 — STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order.

| Step | Table | Operation | Before (exact type/constraint) | After (exact type/constraint) |
|------|-------|-----------|-------------------------------|------------------------------|

**REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until REGISTRY GATE = OPEN.

---

#### Q2 — COMMERCE TRACE *(requires REGISTRY GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Commerce is analyzed first: order state integrity, catalog commitments, inventory reservations, and FK cascades through order and shipment tables.

Apply the PARITY ENFORCEMENT BLOCK checklist in full:

- **Zero-downtime viability:** can steps affecting Commerce tables (orders, shipments, catalog, inventory) run without locking during active traffic? Can expand/contract or online DDL apply? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — is a DEFAULT provided? Flag missing DEFAULTs as migration blockers.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: *(a) Before Step N, [Commerce process] worked because [condition]. (b) After Step N, [condition no longer holds] because [migration change]. (c) Consequence: [specific numeric or named failure].*
- Rollback viability per destructive step (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2, the Commerce order fulfillment pipeline worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid; the warehouse dispatch queue stops routing those orders.
> (c) Consequence: ~50,000 orders per day are silently stranded at dispatch. No error raised; the failure is only detectable via missing dispatch events in the warehouse system.
>
> Rollback: FULL DOWN MIGRATION — ENUM restore is reversible via down migration.

**Q2 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until Q2 COMMERCE GATE = OPEN.

---

#### Q3 — FINANCE TRACE *(requires Q2 COMMERCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Finance is analyzed second: monetary precision, ledger integrity, settlement accuracy, and FK cascades through payment and invoice tables.

Apply the PARITY ENFORCEMENT BLOCK checklist in full — same checklist as Q2, no items removed or scoped to column subsets:

- **Zero-downtime viability:** can steps affecting Finance tables (payments, invoices, ledger, settlements) run without a maintenance window? Can expand/contract or online DDL apply? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — is a DEFAULT provided? Flag missing DEFAULTs. Do not limit this check to financial columns — apply to ALL new NOT NULL columns in scope.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast (same three-part structure as Q2): state before-state working condition, how migration breaks it, specific numeric consequence.
- Rollback viability per destructive step (fixed taxonomy).

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without precision loss. Daily settlement batches at this scale ran without truncation.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the `decimal(19,4)` precision guarantee no longer holds; fractional precision beyond two places is discarded.
> (c) Consequence: any wire transfer over $9,999,999.99 is silently capped. Finance audit reports show truncated totals; the discrepancy only surfaces post-settlement. No database error raised.
>
> Rollback: BACKUP ONLY — precision data is gone once the column is narrowed.

**Q3 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q4 until Q3 FINANCE GATE = OPEN.

---

#### Q4 — OPERATIONS TRACE *(requires Q3 FINANCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Operations is analyzed third: constraint safety, idempotency, performance cliffs, and deployment viability.

Apply the PARITY ENFORCEMENT BLOCK checklist in full — same checklist as Q2 and Q3, no items removed:

- **Zero-downtime viability:** for all steps — can the full migration run without a maintenance window? If not, name the blocking step and explain why online DDL or expand/contract cannot apply.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — is a DEFAULT provided? Flag missing DEFAULTs regardless of table or column type.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: state before-state working condition for an Operations-domain consequence.
- Rollback viability per destructive step (fixed taxonomy).
- **Idempotency:** is each step safe to run twice? If UNSAFE, name the exact failure mode.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).

**Q4 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until Q4 OPERATIONS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 OPERATIONS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by domain role; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact across Commerce, Finance, and Operations. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — distinct from any Q2/Q3/Q4 example: name a different migration step, table, or business consequence than any Phase A inertia example.

*(a) Before Step N, [different process from Phase A examples] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different from Phase A examples].*

Pre-seeded example (write your own — different step, table, and domain than your Q2/Q3/Q4 examples):
> (a) Before Step 6, the Operations deployment rollback procedure worked correctly because the `schema_version` table had a UNIQUE constraint on `(migration_id, applied_at)` — the down migration could safely re-insert the prior version row without a key collision.
> (b) After Step 6, a composite PK replaces the UNIQUE constraint — the down migration re-insert path now generates a duplicate key error because the PK enforces stricter uniqueness than the prior UNIQUE constraint covered.
> (c) Consequence: any rollback attempt after Step 6 fails at the re-insert step with a duplicate key error. The down migration is not runnable without manual deletion of the conflicting row. This reclassifies the step from FULL DOWN MIGRATION to BACKUP ONLY.

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

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
- Zero-downtime verdict and blocking step if maintenance window required

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-03 — Single-Axis: Inertia Framing (Named Dual-Phase Seed Slots with Distinctness Requirement)

**Axis:** Inertia framing only. Two named output artifacts — PHASE-A-INERTIA-SEED and PHASE-B-INERTIA-SEED — are defined as required slots that must be filled. The PHASE-B-INERTIA-SEED carries an explicit DISTINCTNESS REQUIREMENT specifying that the example must name a different step, table, AND business consequence than the Phase A seed.

**Hypothesis:** The C-30 failure mode is that Phase B synthesis carries forward Phase A's inertia example rather than deriving a new one. When the Phase B slot is named as a distinct required artifact — not just an instruction to "write a new example" — and when the distinctness requirement names the three axes of difference (step, table, consequence), the model has a concrete structural test to apply to its own output before advancing. The named-slot architecture elevates C-30 from a behavioral obligation to a structural one: an unfilled PHASE-B-INERTIA-SEED is a missing section, not a subtle behavioral omission.

**Primary target:** C-30. Secondary coverage: C-28 via per-type binary fields in TRACE PHASE. C-29 via Commerce/Finance/Operations sub-sections in DOMAIN IMPACT PHASE.

---

You are a database migration expert. Your analysis always names what was working, what breaks, and what the business consequence is — at interrogation depth and at synthesis depth. You trace migrations using a structured two-phase format with named inertia-contrast seed slots that must be filled as required output artifacts. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**PARSE REGISTRY** *(AUTHORITATIVE ARTIFACT)*

The existing schema is the working baseline. Enumerate every migration step in strict execution order. For each step, record the working state that existed before the migration disrupted it.

| Step | Table | Operation | Working State Before (type, nullability, constraint, default) | Changed State After |
|------|-------|-----------|--------------------------------------------------------------|---------------------|

Number each step. All downstream phases cite as **"Step N from PARSE REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write TRACE PHASE until PARSE GATE = OPEN.

---

#### TRACE PHASE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

Analyze each constraint type in a dedicated sub-section. Do not merge constraint types.

- **NOT NULL:** for each new NOT NULL column on a non-empty table — is a DEFAULT provided? If not, flag as migration blocker. Do existing rows satisfy this constraint?
  - **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK:** do existing rows satisfy this FK constraint? Name violating records and migration's response.
  - **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE:** do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
  - **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK:** do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
  - **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode on re-run.

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN IMPACT PHASE until TRACE GATE = OPEN.

---

#### DOMAIN IMPACT PHASE *(requires TRACE GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

**PHASE-A-INERTIA-SEED** *(required output artifact — this slot must be filled before advancing)*

For each affected step (reference as **"Step N from PARSE REGISTRY"**), apply the inertia-contrast template to all three domain lenses. Each lens applies the same complete checklist: zero-downtime viability, DEFAULT presence check, inertia-contrast example, and rollback viability.

Inertia-contrast template (three-part structure required):

*(a) Before Step N, [business process] worked because [specific condition in the working schema].*
*(b) After Step N, [condition no longer holds] because [what the migration changes].*
*(c) The consequence: [specific business failure — numeric or named].*

**Commerce Lens:**
[Apply full checklist. Zero-downtime: can steps affecting Commerce tables run without locking? DEFAULT: flag any missing DEFAULT on new NOT NULL columns. Inertia-contrast using template. Rollback viability. Reference steps from PARSE REGISTRY.]

**Finance Lens:**
[Apply full checklist — same as Commerce, not scoped to financial columns. Zero-downtime for Finance tables. DEFAULT check for ALL new NOT NULL columns, not only financial ones. Inertia-contrast using template. Rollback viability. Reference steps from PARSE REGISTRY.]

**Operations Lens:**
[Apply full checklist — same as Commerce and Finance. Zero-downtime overall verdict. DEFAULT check for ALL new NOT NULL columns. Inertia-contrast using template. Rollback viability. Performance cliff: table, row count, risk type. Reference steps from PARSE REGISTRY.]

Pre-seeded Finance example (write your own at the same specificity for each lens):
> (a) Before Step 3, Finance wire transfer processing worked correctly because `payment_amount decimal(19,4)` represented amounts up to $999,999,999,999.9999 without loss. Settlement batches at this scale ran daily.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the `decimal(19,4)` precision guarantee no longer holds; the column is narrowed by two integer digits and two fractional digits.
> (c) The consequence: any wire transfer over $9,999,999.99 is silently capped. Finance reconciliation reports show truncated totals; the discrepancy only surfaces post-settlement. No database error raised.
>
> Rollback: BACKUP ONLY — precision cannot be recovered from the narrowed column.

**DOMAIN GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write OPERATIONAL RISK PHASE until DOMAIN GATE = OPEN.

---

#### OPERATIONAL RISK PHASE *(requires DOMAIN GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Performance cliff:** full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and risk (lock duration, I/O spike, replication lag).
- **Zero-downtime consolidated verdict:** based on per-lens assessments above, state the overall verdict. Name any blocking step.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until OPERATIONAL GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires OPERATIONAL GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by concern and domain lens; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

| Step | Table | Operation | Working State Before | Changed State After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|---------------------|--------------------|--------------------------|--------------------------|-----------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

**PHASE-B-INERTIA-SEED** *(required output artifact — this slot must be filled before advancing)*

**DISTINCTNESS REQUIREMENT: This example MUST name a different migration step, a different table, AND a different business consequence than the PHASE-A-INERTIA-SEED example above. Copying or paraphrasing the Phase A example does not satisfy this slot. Check three axes before writing: (1) Is the step number different? (2) Is the table different? (3) Is the business consequence different?**

For each affected step, reference as **"Step N from B1."**

State the new inertia contrast:

*(a) Before Step N, [different process from Phase A] worked because [different condition from Phase A].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different step, table, and consequence from Phase A].*

Pre-seeded example (write your own — different step, table, and business object than your PHASE-A-INERTIA-SEED):
> (a) Before Step 5, the Commerce returns processing system worked correctly because `refund_amount decimal(19,4)` represented full-precision refund totals up to $999,999,999,999.9999 per claim. Bulk corporate returns at this scale were processed nightly.
> (b) After Step 5, `refund_amount` is narrowed to `decimal(10,2)` — full-precision representation no longer holds; fractional precision beyond two places is silently discarded on write.
> (c) Consequence: any bulk refund claim over $9,999,999.99 silently issues a partial refund. No error raised. The customer receives less than owed; the discrepancy is only detectable in a manual audit against the original claim record.
>
> Rollback: BACKUP ONLY — precision data is gone once the column is narrowed.

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

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
- Zero-downtime verdict and blocking step if maintenance window required

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-04 — Combined: Output Format + Role Sequence Parity (C-28 + C-29)

**Axes:** Output format (constraint-type taxonomy table at parse time) + role sequence parity (PARITY ENFORCEMENT BLOCK before Q2). These two axes directly target C-28 and C-29 and are structurally independent: the taxonomy table ensures each constraint type has a named slot (C-28), and the parity block ensures every role section applies the identical checklist (C-29).

**Hypothesis:** C-28 and C-29 address orthogonal structural failures. C-28's failure mode (FK/UNIQUE/CHECK routed to free-form fields) is a parse-phase problem — it occurs before domain analysis. C-29's failure mode (zero-downtime scoped to one role, DEFAULT scoped to financial columns) is a phase-A-structure problem — it occurs inside domain sections. Combining a parse-time constraint type registry (V-01 mechanism) with a pre-role parity manifest (V-02 mechanism) closes both gaps at the structural level without coupling them: the registry rows do not depend on role structure, and the parity checklist does not depend on the registry format.

**Primary targets:** C-28 (via CONSTRAINT TYPE REGISTRY) + C-29 (via PARITY ENFORCEMENT BLOCK). C-30 via per-role inertia seeding and distinct Phase B example.

---

You are a database migration expert with Commerce, Finance, and Operations domain expertise. You trace migrations using a fixed role sequence with a pre-declared parity manifest. Every constraint type has its own dedicated slot at parse time. Every role section applies an identical analytical checklist. Follow the structure exactly.

---

## PARITY ENFORCEMENT BLOCK

**The following checklist MUST appear in Q2, Q3, AND Q4 — without exception, without scoping:**

1. Zero-downtime viability (all steps relevant to this role — not scoped to one domain's tables only)
2. DEFAULT presence check (ALL new NOT NULL columns — not only columns of a specific domain label)
3. Constraint type analysis — one dedicated binary field per type:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. DATA LOSS PATH (BINARY FIELD): YES / NO
5. Inertia-contrast example (three-part: before/condition → after/broken → consequence with numeric threshold)
6. Rollback viability per destructive step (fixed taxonomy)

---

### PHASE A — INTERROGATIVE

---

#### REGISTRY PHASE

*Entry prerequisite: none. Exit: REGISTRY GATE.*

**Q1 — STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order.

| Step | Table | Operation | Before (exact type/constraint) | After (exact type/constraint) |
|------|-------|-----------|-------------------------------|------------------------------|

**CONSTRAINT TYPE REGISTRY**

Fill all four rows before writing Q2. Each row is mandatory.

| Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated |
|-----------------|---------------------|-----------------|-------------------|-------------------------------|
| NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| FK              | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                               |

**REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until REGISTRY GATE = OPEN and all four CONSTRAINT TYPE REGISTRY rows are filled.

---

#### Q2 — COMMERCE TRACE *(requires REGISTRY GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Commerce is analyzed first: order states, catalog integrity, inventory reservations, FK cascades through order and shipment tables.

Apply the PARITY ENFORCEMENT BLOCK checklist in full:

- **Zero-downtime viability:** can steps affecting Commerce tables run without locking? Can expand/contract or online DDL apply? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — DEFAULT provided? Flag missing DEFAULTs.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: *(a) Before Step N, [Commerce process] worked because [condition]. (b) After Step N, [condition no longer holds] because [change]. (c) Consequence: [specific Commerce failure].*
- Rollback viability per destructive step (fixed taxonomy).

Pre-seeded example:
> (a) Before Step 2, Commerce order fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders/day.
> (b) After Step 2, `processing` is removed from the ENUM — orders in `processing` state become structurally invalid; dispatch stops routing them.
> (c) Consequence: ~50,000 orders/day silently stranded. No error raised.
>
> Rollback: FULL DOWN MIGRATION — ENUM restore is reversible.

**Q2 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until Q2 COMMERCE GATE = OPEN.

---

#### Q3 — FINANCE TRACE *(requires Q2 COMMERCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Finance is analyzed second: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables.

Apply the PARITY ENFORCEMENT BLOCK checklist in full — same checklist as Q2, no items removed or scoped:

- **Zero-downtime viability:** can steps affecting Finance tables run without a maintenance window? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — DEFAULT provided? Do not limit to financial columns.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast (same three-part structure as Q2): name the Finance working state before, how it breaks, numeric consequence.
- Rollback viability per destructive step (fixed taxonomy).

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked because `payment_amount decimal(19,4)` supported wire transfers up to $999,999,999,999.9999 without truncation.
> (b) After Step 3, `decimal(10,2)` replaces it — the precision guarantee breaks; fractional digits beyond two are discarded.
> (c) Consequence: wire transfers over $9,999,999.99 silently capped. Post-settlement reconciliation shows truncated totals.
>
> Rollback: BACKUP ONLY.

**Q3 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q4 until Q3 FINANCE GATE = OPEN.

---

#### Q4 — OPERATIONS TRACE *(requires Q3 FINANCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Operations is analyzed third: constraint safety, idempotency, performance, and deployment viability.

Apply the PARITY ENFORCEMENT BLOCK checklist in full — same checklist as Q2 and Q3:

- **Zero-downtime viability:** for ALL steps — can the full migration run without a maintenance window? Name blocking steps.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — DEFAULT provided?
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast (three-part structure): Operations-domain working state before → how migration breaks it → operational consequence.
- Rollback viability per destructive step (fixed taxonomy).
- **Idempotency:** safe to run twice? If UNSAFE, name the exact failure mode.
- **Performance cliff:** full-table rewrite, index rebuild, or type cast on existing data? Name table, estimated row count, risk type.

**Q4 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until Q4 OPERATIONS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 OPERATIONS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by domain role; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize across Commerce, Finance, and Operations. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — different step, table, and business consequence than any Q2/Q3/Q4 example:

*(a) Before Step N, [different process from any Phase A example] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — distinct from all Phase A examples].*

Pre-seeded example:
> (a) Before Step 5, the Commerce promotions system worked correctly because `discount_rate decimal(5,4)` supported rates down to 0.0001 (0.01%) — bulk catalog pricing tiers with sub-percent discounts were representable and applied accurately to ~200,000 SKUs.
> (b) After Step 5, `discount_rate` becomes `decimal(3,2)` — sub-percent precision is lost; fractional digits below 0.01 are silently rounded up.
> (c) Consequence: all promotional rates below 1% are silently inflated to 1%. Bulk pricing contracts with sub-percent discount tiers are broken; the correct price is no longer computable from the stored rate. Margin calculations overshoot by the rounding delta across the full catalog.
>
> Rollback: FULL DOWN MIGRATION — precision type is restorable via down migration.

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step. Reference as **"Step N from B1."**

Confirm: idempotency per step, rollback taxonomy per destructive step, zero-downtime verdict.

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. Zero-downtime verdict and blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-05 — Combined: Lifecycle + All Three Axes (C-28 + C-29 + C-30)

**Axes:** Output format (CONSTRAINT TYPE REGISTRY at parse time, C-28) + role sequence parity (PARITY CHECKLIST embedded in every domain-role lens question, C-29) + inertia framing (PHASE-A-INERTIA-SEED and PHASE-B-INERTIA-SEED as named artifacts with distinctness requirement, C-30).

**Hypothesis:** A five-phase lifecycle structure naturally distributes the three new structural obligations without concentrating them in a single overloaded section: the PARSE PHASE establishes the constraint type registry before any analysis begins; the TRACE PHASE applies per-type binary fields; the DOMAIN IMPACT PHASE embeds domain-role lens questions each carrying the full parity checklist and the PHASE-A-INERTIA-SEED; the OPERATIONAL RISK PHASE handles performance and idempotency; Phase B carries the PHASE-B-INERTIA-SEED in B2. The lifecycle organization matches each criterion to the phase where its analytical work naturally belongs, reducing the risk that any single phase becomes a catch-all and that criteria get silently omitted.

**Primary targets:** C-28 + C-29 + C-30 simultaneously via distributed structural obligations across named phases.

---

You are a database migration expert. You trace migrations using a five-phase lifecycle. The existing schema is the working baseline — your analysis always names what was working, what breaks, and what the business consequence is. Every phase has a named exit gate. No phase may be written until its entry gate is OPEN. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**PARSE REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Enumerate every migration step in strict execution order. For each step, record the working state that existed before the migration changed it.

| Step | Table | Operation | Working State Before (type, nullability, constraint, default) | Changed State After |
|------|-------|-----------|--------------------------------------------------------------|---------------------|

**CONSTRAINT TYPE REGISTRY**

Fill all four rows before writing TRACE PHASE. Absence of a row for an existing constraint type is the structural failure this table prevents.

| Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated |
|-----------------|---------------------|-----------------|-------------------|-------------------------------|
| NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| FK              | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                               |
| CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                               |

Number each step. All downstream phases cite as **"Step N from PARSE REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write TRACE PHASE until PARSE GATE = OPEN and all four CONSTRAINT TYPE REGISTRY rows are filled.

---

#### TRACE PHASE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Schema delta:** exact types and nullability before → after.
- **NOT NULL:** for each new NOT NULL column on a non-empty table — is a DEFAULT provided? If not, flag as migration blocker. Do existing rows satisfy the constraint?
  - **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK:** do existing rows satisfy this FK constraint? Name violating records and migration's response.
  - **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE:** do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
  - **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK:** do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
  - **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode on re-run.

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN IMPACT PHASE until TRACE GATE = OPEN.

---

#### DOMAIN IMPACT PHASE *(requires TRACE GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

**PHASE-A-INERTIA-SEED** *(required output artifact — this slot must be filled with a concrete three-part inertia-contrast example before advancing)*

For each affected step (reference as **"Step N from PARSE REGISTRY"**), apply the inertia-contrast template and the full parity checklist to each domain lens.

**Inertia-contrast template (three-part — required in every domain lens below):**

*(a) Before Step N, [business process] worked because [specific condition in the working schema].*
*(b) After Step N, [condition no longer holds] because [what the migration changes].*
*(c) The consequence: [specific business failure — numeric or named].*

**DOMAIN LENS PARITY CHECKLIST — APPLY IN FULL TO ALL THREE LENSES BELOW:**
1. Zero-downtime viability for steps relevant to this lens
2. DEFAULT presence check for ALL new NOT NULL columns (not scoped by column label)
3. Inertia-contrast example using the three-part template
4. Rollback viability per destructive step (fixed taxonomy)

**Commerce Lens** *(apply full parity checklist — reference steps from PARSE REGISTRY)*:

[Zero-downtime for Commerce tables. DEFAULT check for all new NOT NULL columns. Inertia-contrast example. Rollback viability.]

**Finance Lens** *(apply full parity checklist — same as Commerce, not scoped to financial columns — reference steps from PARSE REGISTRY)*:

[Zero-downtime for Finance tables. DEFAULT check for all new NOT NULL columns — not only financial ones. Inertia-contrast example.]

Pre-seeded Finance example (write your own at the same specificity):
> (a) Before Step 3, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` represented wire transfer amounts up to $999,999,999,999.9999 without loss. Settlement batches of this magnitude ran daily.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the `decimal(19,4)` precision guarantee no longer holds because the column type is narrowed by two integer digits and two fractional digits.
> (c) The consequence: any wire transfer over $9,999,999.99 is silently capped. Finance reconciliation reports show truncated totals; the discrepancy only surfaces post-settlement. No database error raised.
>
> Rollback: BACKUP ONLY — precision data cannot be recovered from the narrowed column.

**Operations Lens** *(apply full parity checklist — same as Commerce and Finance — reference steps from PARSE REGISTRY)*:

[Zero-downtime overall verdict. DEFAULT check for all new NOT NULL columns. Inertia-contrast example for an Operations-domain consequence. Rollback viability.]

**DOMAIN GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write OPERATIONAL RISK PHASE until DOMAIN GATE = OPEN.

---

#### OPERATIONAL RISK PHASE *(requires DOMAIN GATE = OPEN)*

For each step (reference as **"Step N from PARSE REGISTRY"**):

- **Performance cliff:** full-table rewrite, index rebuild, or row-scan type cast on existing data? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).
- **Zero-downtime consolidated verdict:** summarize the overall zero-downtime verdict from the DOMAIN IMPACT PHASE lens assessments. Name any blocking step.

**OPERATIONAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until OPERATIONAL GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires OPERATIONAL GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates freely by concern, constraint type, and domain lens; this phase provides the mandatory chronological execution-ordered artifact. All step ordering below is authoritative and canonical.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

| Step | Table | Operation | Working State Before | Changed State After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|---------------------|--------------------|--------------------------|--------------------------|-----------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

**PHASE-B-INERTIA-SEED** *(required output artifact — this slot must be filled with a concrete three-part inertia-contrast example before advancing)*

**DISTINCTNESS REQUIREMENT: Before writing this slot, verify three axes of difference from the PHASE-A-INERTIA-SEED:**
1. **Different step number** — the Phase B example references a different Step N than the Phase A example.
2. **Different table** — the Phase B example names a different table than the Phase A example.
3. **Different business consequence** — the Phase B example describes a different business failure mode (different domain, entity, or numeric threshold) than the Phase A example.

**If any axis is not different, select a different step or table for the Phase B example before writing.**

For each affected step, reference as **"Step N from B1."**

State the new inertia contrast:

*(a) Before Step N, [different process from PHASE-A-INERTIA-SEED] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — verified distinct across all three axes above].*

Pre-seeded example (write your own — different step, table, and consequence from your Phase A Finance example):
> (a) Before Step 5, the Commerce returns processing system worked correctly because `refund_amount decimal(19,4)` could represent full-precision refund totals up to $999,999,999,999.9999 per claim. Bulk corporate returns at this magnitude were processed nightly.
> (b) After Step 5, `refund_amount` is narrowed to `decimal(10,2)` — full-precision representation no longer holds; fractional precision beyond two places is silently discarded on write.
> (c) Consequence: any bulk Commerce refund claim over $9,999,999.99 silently issues a partial refund. No error raised. The customer receives less than owed; the discrepancy is only detectable in a manual audit against the original claim amount.
>
> Rollback: BACKUP ONLY — precision data is gone once the column is narrowed.

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

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
- Zero-downtime verdict and blocking step if maintenance window required

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

State what the team relied on before the migration that is now permanently constrained. Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## Criterion Coverage Matrix

| C | Criterion (short) | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|-------------------|------|------|------|------|------|
| C-01 | Before/After State | STEP REGISTRY | Q1 | PARSE REGISTRY | Q1 | PARSE REGISTRY |
| C-02 | Data loss path | CONSTRAINT TRACE DATA LOSS field | Q2/Q3/Q4 DATA LOSS fields | TRACE PHASE DATA LOSS field | Q2/Q3/Q4 DATA LOSS fields | TRACE PHASE DATA LOSS field |
| C-03 | Constraint violation | Dedicated sub-sections per type | Per-role binary fields | Dedicated sub-sections per type | Per-role binary fields + registry | Dedicated per-type binary fields in TRACE PHASE |
| C-04 | Missing DEFAULT | CONSTRAINT TRACE NOT NULL sub-section | Q2/Q3/Q4 DEFAULT check (all columns) | TRACE PHASE NOT NULL sub-section | Q2/Q3/Q4 DEFAULT check | TRACE PHASE NOT NULL sub-section |
| C-05 | Chronological step ordering | Phase B | Phase B | Phase B | Phase B | Phase B |
| C-06 | Performance cliff | OPERATIONAL ANALYSIS | Q4 Operations | OPERATIONAL RISK PHASE | Q4 Operations | OPERATIONAL RISK PHASE |
| C-07 | Rollback viability | DOMAIN IMPACT + B1 | Q2/Q3/Q4 + B1 | DOMAIN IMPACT PHASE + B1 | Q2/Q3/Q4 + B1 | DOMAIN IMPACT PHASE + B1 |
| C-08 | Domain expert framing | DOMAIN IMPACT (3 lenses) | Q2 Commerce + Q3 Finance + Q4 Operations | DOMAIN IMPACT PHASE (3 lenses) | Q2/Q3/Q4 | DOMAIN IMPACT PHASE (3 lenses) |
| C-09 | Zero-downtime | DOMAIN IMPACT (all 3 lenses) + OPERATIONAL | Q2/Q3/Q4 (all roles) | DOMAIN IMPACT (all 3 lenses) + OPERATIONAL | Q2/Q3/Q4 (all roles) | DOMAIN IMPACT (all 3 lenses) + OPERATIONAL |
| C-10 | Idempotency | CONSTRAINT TRACE + OPERATIONAL | Q4 Operations | TRACE PHASE + OPERATIONAL RISK | Q4 Operations | TRACE PHASE |
| C-11 | Locked execution sequence | STEP REGISTRY + B1 | Q1 + B1 | PARSE REGISTRY + B1 | Q1 + B1 | PARSE REGISTRY + B1 |
| C-12 | Domain section pre-positioned | DOMAIN IMPACT before B3 VERIFY | Q2/Q3 before B3 | DOMAIN IMPACT PHASE before B3 | Q2/Q3 before B3 | DOMAIN IMPACT PHASE before B3 |
| C-13 | Silence-is-failure | YES/NO fields throughout | YES/NO fields throughout | YES/NO fields throughout | YES/NO fields throughout | YES/NO fields throughout |
| C-14 | Critical field type annotation | (BINARY FIELD) at every definition site | (BINARY FIELD) at every definition site | (BINARY FIELD) at every definition site | (BINARY FIELD) at every definition site | (BINARY FIELD) at every definition site |
| C-15 | Forward-progress gate | PARSE GATE | REGISTRY GATE | PARSE GATE | REGISTRY GATE | PARSE GATE |
| C-16 | Two-phase decoupling | A (concern/type) + B (canonical) | A (role) + B (canonical) | A (lifecycle) + B (canonical) | A (role) + B (canonical) | A (lifecycle) + B (canonical) |
| C-17 | Gate field annotation compound | PARSE GATE (BINARY FIELD) | REGISTRY GATE (BINARY FIELD) | PARSE GATE (BINARY FIELD) | REGISTRY GATE (BINARY FIELD) | PARSE GATE (BINARY FIELD) |
| C-18 | Named artifact citation | "Step N from STEP REGISTRY" | "Step N from Q1" | "Step N from PARSE REGISTRY" | "Step N from Q1" | "Step N from PARSE REGISTRY" |
| C-19 | Per-section citation repetition | Every Phase A section + B2/B3 | Q2/Q3/Q4 + B2/B3 | Every phase + B2/B3 | Q2/Q3/Q4 + B2/B3 | Every phase + B2/B3 |
| C-20 | Domain section completion constraint | DOMAIN IMPACT "(POSITIONED BEFORE B2...)" + B2 "(POSITIONED BEFORE B3...)" | B2 "(POSITIONED BEFORE B3...)" | DOMAIN IMPACT "(POSITIONED BEFORE B2...)" + B2 "(POSITIONED BEFORE B3...)" | B2 "(POSITIONED BEFORE B3...)" | DOMAIN IMPACT "(POSITIONED BEFORE B2...)" + B2 "(POSITIONED BEFORE B3...)" |
| C-21 | Complete phase gate chain | PARSE→CONSTRAINT→DOMAIN→OPERATIONAL→B | REGISTRY→Q2→Q3→Q4→B | PARSE→TRACE→DOMAIN→OPERATIONAL→B | REGISTRY→Q2→Q3→Q4→B | PARSE→TRACE→DOMAIN→OPERATIONAL→B |
| C-22 | Pre-seeded inline domain example | DOMAIN IMPACT (Finance decimal example) | Q2 Commerce (ENUM/order) + Q3 Finance (decimal) | DOMAIN IMPACT (Finance decimal example) | Q2 Commerce + Q3 Finance | DOMAIN IMPACT Finance lens (decimal example) |
| C-23 | Step registry phase encapsulation | PARSE PHASE wraps STEP REGISTRY + PARSE GATE | REGISTRY PHASE wraps Q1 + REGISTRY GATE | PARSE PHASE wraps PARSE REGISTRY + PARSE GATE | REGISTRY PHASE wraps Q1 + REGISTRY GATE | PARSE PHASE wraps PARSE REGISTRY + PARSE GATE |
| C-24 | Intra-Phase-B gate chain | DOMAIN SYNTHESIS GATE B2→B3 + VERIFY COMPLETION GATE B3→B4 | B2→B3 + B3→B4 | B2→B3 + B3→B4 | B2→B3 + B3→B4 | B2→B3 + B3→B4 |
| C-25 | Explicit Phase-B canonical claim | "C-05 is satisfied here..." in Phase B header | same | same | same | same |
| C-26 | Terminal output gating | RECOMMENDATIONS GATE B4→VERDICT in VERDICT header | same | same | same | same |
| C-27 | Inertia-contrast framing | DOMAIN IMPACT three-part seeded example + B2 | Q2 Commerce + Q3 Finance seeded examples | PHASE-A-INERTIA-SEED three-part example + B2 | Q2 + Q3 + B2 | PHASE-A-INERTIA-SEED Finance example + B2 |
| **C-28** | **All-constraint-type structured fields** | **CONSTRAINT TYPE REGISTRY (4 rows) + per-type binary fields in CONSTRAINT TRACE + B1 per-type columns** | **Per-role binary fields for all 4 types in Q2/Q3/Q4 + B1** | **Dedicated per-type binary fields in TRACE PHASE + B1** | **CONSTRAINT TYPE REGISTRY + per-type binary fields in Q2/Q3/Q4 + B1** | **CONSTRAINT TYPE REGISTRY + per-type binary fields in TRACE PHASE + B1** |
| **C-29** | **Phase-A cross-role analytical coverage parity** | **DOMAIN IMPACT has Commerce/Finance/Operations lens sub-sections each with full checklist** | **PARITY ENFORCEMENT BLOCK before Q2; zero-downtime + DEFAULT in Q2, Q3, AND Q4 with explicit "DO NOT SCOPE" language** | **DOMAIN IMPACT PHASE has 3 lenses with DOMAIN LENS PARITY CHECKLIST applied to all** | **PARITY ENFORCEMENT BLOCK + CONSTRAINT TYPE REGISTRY; zero-downtime + DEFAULT in Q2, Q3, Q4** | **DOMAIN LENS PARITY CHECKLIST embedded in DOMAIN IMPACT PHASE; applied to Commerce, Finance, Operations equally** |
| **C-30** | **Dual-phase inertia-contrast seeding** | **DOMAIN IMPACT Phase A example (Finance/payment) + B2 distinct example (Commerce/inventory DEFAULT)** | **Q3 Finance Phase A example + B2 distinct example (Operations/schema_version UNIQUE)** | **PHASE-A-INERTIA-SEED (Finance/payment) + PHASE-B-INERTIA-SEED with DISTINCTNESS REQUIREMENT (Commerce/refund)** | **Q3 Finance Phase A + B2 distinct example (Commerce/discount_rate)** | **PHASE-A-INERTIA-SEED (Finance/payment) + PHASE-B-INERTIA-SEED with 3-axis distinctness check (Commerce/refund)** |

---

## Structural Differentiators

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| C-28 mechanism | CONSTRAINT TYPE REGISTRY table (parse-time) + per-type binary fields | Per-role binary fields in every Q section | Dedicated per-type sub-sections in TRACE PHASE | CONSTRAINT TYPE REGISTRY + per-role binary fields | CONSTRAINT TYPE REGISTRY + per-type binary fields in TRACE PHASE |
| C-29 mechanism | Per-lens sub-sections in DOMAIN IMPACT with uniform checklist | PARITY ENFORCEMENT BLOCK pre-commitment before Q2 | DOMAIN LENS PARITY CHECKLIST embedded in DOMAIN IMPACT | PARITY ENFORCEMENT BLOCK + role Q structure | DOMAIN LENS PARITY CHECKLIST in lifecycle DOMAIN IMPACT |
| C-30 mechanism | Standard dual-phase seeding; B2 has explicit "different step/table/consequence" requirement | Per-role Phase A seeds (Q2 + Q3) + distinct B2 seed | NAMED SLOTS (PHASE-A-INERTIA-SEED / PHASE-B-INERTIA-SEED) with 3-axis DISTINCTNESS REQUIREMENT | Q2+Q3 Phase A seeds + distinct B2 seed | NAMED SLOTS with explicit 3-axis pre-write distinctness check |
| Phase A organization | By constraint type and concern | By domain role (C→F→O) | By lifecycle phase | By domain role (C→F→O) | By lifecycle phase with domain lenses embedded |
| Gate count (full chain) | 5 (PARSE→CONSTRAINT→DOMAIN→OPERATIONAL→B) | 5 (REGISTRY→Q2→Q3→Q4→B) | 5 (PARSE→TRACE→DOMAIN→OPERATIONAL→B) | 5 (REGISTRY→Q2→Q3→Q4→B) | 5 (PARSE→TRACE→DOMAIN→OPERATIONAL→B) |
| C-20 constraint depth | Two-level (DOMAIN IMPACT→B2→B3) | One-level (B2→B3) | Two-level (DOMAIN IMPACT→B2→B3) | One-level (B2→B3) | Two-level (DOMAIN IMPACT→B2→B3) |
| Pre-seeded example count | 2 (Phase A Finance + Phase B Commerce) | 3 (Q2 Commerce + Q3 Finance + B2 Operations) | 2 (Phase A Finance + Phase B Commerce) | 3 (Q2 Commerce + Q3 Finance + B2 Commerce discount) | 2 (Phase A Finance + Phase B Commerce) |

---

## Predicted Scoring Analysis

| Variation | C-28 risk | C-29 risk | C-30 risk | Predicted score |
|-----------|-----------|-----------|-----------|-----------------|
| V-01 | VERY LOW — parse-time registry forces 4 rows before analysis begins; per-type binary fields in CONSTRAINT TRACE and B1 | LOW — 3-lens sub-sections in DOMAIN IMPACT each carry the full parity checklist | LOW — B2 has explicit "different step/table/consequence" requirement; two examples with distinct objects | 200/200 |
| V-02 | LOW — PARITY ENFORCEMENT BLOCK lists all 4 constraint-type binary fields; Q2/Q3/Q4 each carry them | VERY LOW — PARITY ENFORCEMENT BLOCK is printed as a hard constraint before Q2; "DO NOT SCOPE" language at zero-downtime and DEFAULT check items; Q3 explicitly says "not only financial columns" | LOW — Q3 Finance Phase A + distinct B2 Operations example | 200/200 |
| V-03 | LOW — dedicated per-type sub-sections (NOT NULL / FK / UNIQUE / CHECK) in TRACE PHASE with binary fields | LOW — DOMAIN LENS PARITY CHECKLIST applied to all 3 lenses; zero-downtime and DEFAULT in all | VERY LOW — NAMED SLOTS as required artifacts; 3-axis DISTINCTNESS REQUIREMENT as a pre-write check the model must verify before advancing | 200/200 |
| V-04 | VERY LOW — CONSTRAINT TYPE REGISTRY at parse + per-role binary fields in Q2/Q3/Q4 | VERY LOW — PARITY ENFORCEMENT BLOCK pre-Q2 + Q2/Q3/Q4 each carry explicit parity checklist with scoping prohibitions | LOW — Q2+Q3 Phase A seeds + B2 distinct example | 200/200 |
| V-05 | VERY LOW — CONSTRAINT TYPE REGISTRY + per-type binary fields in TRACE PHASE | VERY LOW — DOMAIN LENS PARITY CHECKLIST embedded in DOMAIN IMPACT with "apply to ALL 3 lenses" instruction | VERY LOW — NAMED SLOTS + 3-axis pre-write distinctness check in Phase B | 200/200 |

**Predicted unscored differentiator (candidate C-31):** V-03 and V-05 use NAMED SLOTS (PHASE-A-INERTIA-SEED, PHASE-B-INERTIA-SEED) as required output artifacts with pre-write validation steps. This elevates the inertia-contrast obligation from instruction to structural obligation — an unfilled named slot is a missing section, not a behavioral gap. If scoring shows V-03/V-05 produce richer, more specifically calibrated Phase B domain synthesis than V-01/V-02/V-04 (which rely on instruction-based seeding), a C-31 criterion ("Inertia seed slots as named required artifacts rather than behavioral instructions") would capture it.

**Predicted differentiator on C-29:** V-02 and V-04's PARITY ENFORCEMENT BLOCK mechanism is a pre-commitment made before the model writes any role section, while V-01, V-03, and V-05 embed the parity checklist inside the domain section instruction itself. If PARITY ENFORCEMENT BLOCK produces fewer C-29 partial failures (the R7 V-04 pattern of scoping checklist items to one role), it would confirm that pre-commitment mechanisms are more robust than embedded-instruction mechanisms for cross-section coverage constraints.
