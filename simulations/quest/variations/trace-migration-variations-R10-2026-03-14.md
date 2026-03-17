I have everything I need. R9 V-05 achieved 215/215. The residual PARTIAL patterns in R9 V-01/V-02/V-03/V-04 are: **C-19** (citation not per-section — PARTIAL in V-01/V-02/V-03), **C-30** (Phase B inertia not structurally seeded — PARTIAL in V-01/V-02/V-04), **C-15/C-17** (gate annotation compound at definition site — PARTIAL in V-01/V-03). R10 targets these three gaps via three single-axis mechanisms then combines them.

---

# trace-migration — Round 10 Variations (v9 rubric)

**New criteria this round:** none (rubric holds at v9, 33 criteria, 215 pts max)

**R9 baseline:** V-05 scored 215/215 (100%) via phase-per-criterion isolation. V-04 scored 207.5/215 with C-30 as the only PARTIAL. V-01/V-02/V-03 scored 195–200/215. Residual PARTIAL patterns: C-15/C-17 (gate annotation compound missing at definition site — V-01, V-03), C-19 (per-section citation repetition — V-01, V-02, V-03), C-30 (Phase B inertia seed not structurally obligated — V-01, V-02, V-04).

**R10 design constraint:** All five variations must satisfy C-31, C-32, C-33 (from R9) and C-28, C-29, C-30 (from R8). Differentiation is on closing C-15/C-17/C-19/C-30 residual gaps via three structural mechanisms — then combining them. Each single-axis variation targets one gap cluster. V-05 combines all three axes with the R9 V-05 lifecycle backbone.

---

## Variation Summary

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (per-section citation anchor preamble) | C-19 requires the citation source-artifact instruction in EVERY section. In R9, all variations placed this instruction globally (once). If each section opens with a named CITATION ANCHOR line — a structural preamble, not prose — repeating the source artifact name before any step references appear, the model cannot write a section without that anchor being present. C-19 compliance becomes a section-structural obligation rather than a behavioral one. |
| V-02 | Output format (Phase-B inertia as named artifact with 3-axis distinctness checklist) | C-30 PARTIAL in R9 V-01/V-02/V-04 arose because Phase B's inertia example was instructed (behavioral) but not structurally obligated. If Phase B contains a named INERTIA-SEED-B artifact with a visible 3-item distinctness checklist (step number ≠ Phase A / table ≠ Phase A / consequence ≠ Phase A), advancing without satisfying the checklist is a visible structural gap — not a behavioral omission that can be silently skipped. |
| V-03 | Lifecycle emphasis (compound gate annotation block at every phase boundary) | C-15/C-17 PARTIAL in R9 V-01/V-03 arose because gate states existed but the compound "(BINARY FIELD)" annotation was absent at the definition site — gates were implied rather than explicitly typed. If every phase boundary carries a two-part GATE BLOCK — an EXIT BLOCK at the bottom of the preceding phase with compound annotation, plus an ENTRY REFERENCE at the top of the succeeding phase also carrying compound annotation — C-15 and C-17 are satisfied by the gate-block pattern itself, not by behavioral compliance. |
| V-04 | Combined: phrasing register + output format (C-19 + C-30) | C-19 and C-30 are orthogonal gaps: C-19 fails when citation appears once globally, C-30 fails when Phase B copies Phase A's inertia. Combining per-section citation anchors (V-01 mechanism) with the named INERTIA-SEED-B artifact (V-02 mechanism) closes both without restructuring the lifecycle. These two mechanisms are structurally independent — citation anchors appear at section preamble, inertia artifacts appear at section content — and compound cleanly. |
| V-05 | Combined: all three axes (C-15/C-17 + C-19 + C-30) on R9 V-05 lifecycle backbone | R9 V-05 achieved 215/215 via phase-per-criterion isolation. V-05 R10 retains that six-phase backbone (MANIFEST PHASE → PARITY PHASE → INTERROGATIVE PHASE → CANONICAL PHASE → VERDICT PHASE) and adds all three R10 gap closures: compound gate annotations at every phase boundary, per-section citation anchors in every analytical section, and named INERTIA-SEED-B artifact in CANONICAL PHASE. Each criterion has both a primary enforcement mechanism (from R9) and a secondary structural reinforcement (from R10). |

---

## V-01 — Single-Axis: Phrasing Register (Per-Section Citation Anchor Preamble)

**Axis:** Phrasing register only. Every section that references migration steps opens with an explicit CITATION ANCHOR preamble — a one-line structural statement naming the source artifact and the citation format — before any step references appear. This is not a global instruction; it is repeated at the head of each section.

**Hypothesis:** C-19 requires the source-artifact citation instruction in EVERY section. In R9, all variations printed one global preamble ("all sections cite from STEP REGISTRY") and relied on behavioral compliance within each section. When a section-level CITATION ANCHOR is a structural preamble — the first visible element of each section's content — the model cannot write step references without the anchor being present. A section whose step references appear before or without a CITATION ANCHOR has a visible structural gap. The anchor also guards against per-section regression to generic ordinals: a model that drops the source-artifact name produces a malformed anchor line, not a silent omission.

**Primary target:** C-19. Secondary coverage: C-31 via parse-time CONSTRAINT TYPE REGISTRY, C-32 via manifest-derived B1 columns, C-33 via parity enforcement block, C-28/C-29/C-30 via standard machinery.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — filled at parse time — is the binding manifest for all downstream constraint analysis. Every section that references migration steps opens with a CITATION ANCHOR naming the source artifact before any step reference appears. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE (BINARY FIELD).*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order.

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

Each row is mandatory regardless of whether the migration contains a violation of that type. The B1 Column Name field is pre-populated: Phase B's execution table will carry exactly these four binary constraint-type columns, in this row order, with these names.

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated | B1 Column Name |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|----------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                                | NOT NULL Risk  |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                                | FK Violation   |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                                | UNIQUE Violation |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                                | CHECK Violation |

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write any section below until PARSE GATE = OPEN and all four manifest rows are filled.

---

## PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Commerce, Finance, Operations) — DO NOT SCOPE OR SHORTEN any item for any role. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window using expand/contract or online DDL? Name any blocking step and explain why. *(Required in ALL roles — not scoped to Commerce tables only.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is a DEFAULT provided? Flag missing DEFAULTs as migration blockers. *(Apply to ALL new NOT NULL columns — not only financial columns, not only Commerce columns.)*
3. **Constraint violation analysis** — fill all four binary fields (derived from manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO
5. **Inertia-contrast example** — three-part structure: (a) before-state working condition, (b) how migration breaks it, (c) specific numeric consequence.
6. **Rollback viability** — per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**If any item is absent from any role section, the parity constraint is violated.**

---

#### CONSTRAINT TRACE *(requires PARSE GATE = OPEN)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

For each step, analyze each constraint type in its own dedicated sub-section using the manifest row order. Do not merge constraint types or route analysis through free-form fields.

**Manifest Row 1 — NOT NULL:**
- For each new NOT NULL column on a non-empty table: is a DEFAULT provided? If not, flag as migration blocker. Name violating records and migration's response (fail / skip / backfill).
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 2 — FK:**
- Do existing rows satisfy this FK constraint? Name violating records and migration's response.
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 3 — UNIQUE:**
- Do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 4 — CHECK:**
- Do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode on re-run.

**CONSTRAINT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN IMPACT until CONSTRAINT GATE = OPEN.

---

#### DOMAIN IMPACT *(requires CONSTRAINT GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

For each affected step, apply the PARITY ENFORCEMENT BLOCK checklist in full to ALL THREE domain lenses below.

**Commerce Lens:**

> **CITATION ANCHOR (Commerce):** Step references → **"Step N from STEP REGISTRY."**

Apply all six PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2, the Commerce order fulfillment pipeline worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid; the warehouse dispatch queue stops routing those orders.
> (c) Consequence: ~50,000 orders per day are silently stranded at dispatch. No error raised; failure only detectable via missing dispatch events in the warehouse system.
>
> Rollback: FULL DOWN MIGRATION — ENUM restore is reversible via down migration.

**Finance Lens:**

> **CITATION ANCHOR (Finance):** Step references → **"Step N from STEP REGISTRY."**

Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce. Finance scope: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables. Do not limit DEFAULT checks to financial columns — apply to ALL new NOT NULL columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without precision loss. Daily settlement batches at this scale ran without truncation.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the decimal(19,4) precision guarantee no longer holds; fractional precision beyond two places is discarded.
> (c) Consequence: any wire transfer over $9,999,999.99 is silently capped. Finance audit reports show truncated totals; discrepancy surfaces only post-settlement. No database error raised.
>
> Rollback: BACKUP ONLY — precision data is gone once the column is narrowed.

**Operations Lens:**

> **CITATION ANCHOR (Operations):** Step references → **"Step N from STEP REGISTRY."**

Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce and Finance. Also include:
- **Idempotency per step:** SAFE / UNSAFE — if UNSAFE, name the exact failure mode on re-run.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).

**DOMAIN IMPACT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until DOMAIN IMPACT GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires DOMAIN IMPACT GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by constraint type and domain lens; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All step references in B-section text use **"Step N from B1."** Do not use generic ordinals.

List every migration step in strict execution order. Single source of step numbers for all B-section references.

**MANIFEST COLUMN AUDIT:** This table must carry exactly four binary constraint-type columns derived from the CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order: Row 1 = NOT NULL Risk, Row 2 = FK Violation, Row 3 = UNIQUE Violation, Row 4 = CHECK Violation. Adding or omitting a constraint-type column is a manifest violation.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from B1."** Do not use generic ordinals.

For each affected step, synthesize the domain impact across Commerce, Finance, and Operations.

Seed a NEW inertia-contrast example here — this example MUST name a different migration step, a different table, AND a different business consequence than any DOMAIN IMPACT Phase A inertia example. Repeating a Phase A example does not satisfy this section.

*(a) Before Step N, [different process from Phase A examples] worked because [different condition from Phase A].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different step, table, and consequence from Phase A examples].*

Pre-seeded example (write your own — different step, table, and domain than your Phase A examples):
> (a) Before Step 5, the Commerce inventory reservation system worked correctly because `reserved_qty integer NOT NULL DEFAULT 0` guaranteed every SKU had a valid reservation count — bulk catalog imports never needed to specify the field explicitly.
> (b) After Step 5, `DEFAULT 0` is removed from `reserved_qty` — any INSERT without an explicit `reserved_qty` value fails the NOT NULL constraint.
> (c) Consequence: bulk SKU onboarding pipelines fail at write time with a constraint error instead of completing silently. ~12,000 SKU imports per day affected; operators see constraint errors rather than successful catalog additions.
>
> Rollback: FULL DOWN MIGRATION — the DEFAULT clause is restorable via down migration.

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from B1."** Do not use generic ordinals.

One verification check per step. Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step
- Zero-downtime verdict and blocking step if maintenance window required

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from B1."** Do not use generic ordinals.

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-02 — Single-Axis: Output Format (Phase-B Inertia Seed as Named Artifact with 3-Axis Distinctness Checklist)

**Axis:** Output format only. Phase B contains a named INERTIA-SEED-B artifact — a required output slot with an explicit three-axis distinctness checklist printed inside the artifact definition. The checklist forces the model to verify three structural axes (step number, table, business consequence) before advancing. An unfilled INERTIA-SEED-B is a missing section; a INERTIA-SEED-B whose checklist contains unchecked items is a visible structural gap.

**Hypothesis:** C-30 PARTIAL in R9 V-01, V-02, V-04 arose because Phase B's distinct inertia example was instructed ("seed a new example — different step, table, consequence") but not structurally obligated. When the Phase B inertia slot is a named artifact — INERTIA-SEED-B — with a visible 3-item checkbox distinctness check printed at the artifact's opening, the model must evaluate all three axes before writing the example. The checkbox transforms C-30's distinctness requirement from an implicit behavioral constraint into an explicit structural obligation: a model that copies Phase A's example leaves all three checkboxes unchecked, creating a detectable gap rather than a silent behavioral failure.

**Primary target:** C-30. Secondary coverage: C-31 via parse-time CONSTRAINT TYPE REGISTRY, C-32 via manifest-derived B1 columns, C-33 via parity enforcement block, C-28/C-29 via standard machinery.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — filled at parse time — is the binding manifest for all downstream constraint analysis. Phase B contains a named INERTIA-SEED-B artifact that must be filled as a required output slot; its three-axis distinctness checklist must be satisfied before any Phase B content that follows it. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE (BINARY FIELD).*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. All downstream sections cite as **"Step N from STEP REGISTRY."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated | B1 Column Name |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|----------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                                | NOT NULL Risk  |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                                | FK Violation   |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                                | UNIQUE Violation |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                                | CHECK Violation |

All downstream sections cite steps as **"Step N from STEP REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write any section below until PARSE GATE = OPEN.

---

## PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Commerce, Finance, Operations) — DO NOT SCOPE OR SHORTEN any item for any role. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window using expand/contract or online DDL? Name any blocking step. *(Required in ALL roles — not scoped to Commerce tables only.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: DEFAULT provided? Flag missing DEFAULTs as migration blockers. *(Apply to ALL new NOT NULL columns — not only financial columns.)*
3. **Constraint violation analysis** — fill all four binary fields:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO
5. **Inertia-contrast example** — three-part structure: (a) before-state working condition, (b) how migration breaks it, (c) specific numeric consequence.
6. **Rollback viability** — per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**If any item is absent from any role section, the parity constraint is violated.**

---

#### CONSTRAINT TRACE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from STEP REGISTRY"**):

Analyze each constraint type in its own dedicated sub-section using the manifest row order.

**Manifest Row 1 — NOT NULL:**
- For each new NOT NULL column on a non-empty table: is a DEFAULT provided? If not, flag as migration blocker. Name violating records and migration's response.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 2 — FK:**
- Do existing rows satisfy this FK constraint? Name violating records and migration's response.
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 3 — UNIQUE:**
- Do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 4 — CHECK:**
- Do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode on re-run.

**CONSTRAINT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN IMPACT until CONSTRAINT GATE = OPEN.

---

#### DOMAIN IMPACT *(requires CONSTRAINT GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Apply the PARITY ENFORCEMENT BLOCK checklist in full to ALL THREE domain lenses.

**Commerce Lens:**
Apply all six PARITY ENFORCEMENT BLOCK items. Reference steps from STEP REGISTRY. Scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2, the Commerce order fulfillment pipeline worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid.
> (c) Consequence: ~50,000 orders per day are silently stranded at dispatch. No error raised.
>
> Rollback: FULL DOWN MIGRATION.

**Finance Lens:**
Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce. Reference steps from STEP REGISTRY. Do not limit DEFAULT checks to financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without truncation.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — precision beyond two fractional places discarded.
> (c) Consequence: wire transfers over $9,999,999.99 silently capped. Discrepancy surfaces only post-settlement.
>
> Rollback: BACKUP ONLY.

**Operations Lens:**
Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce and Finance. Reference steps from STEP REGISTRY. Also include:
- **Idempotency per step:** SAFE / UNSAFE — name the failure mode if UNSAFE.
- **Performance cliff:** full-table rewrite, index rebuild, or row-scan type cast? Name table, estimated row count, and risk.

**DOMAIN IMPACT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until DOMAIN IMPACT GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires DOMAIN IMPACT GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by constraint type and domain lens; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references. All B-section references cite as **"Step N from B1."**

**MANIFEST COLUMN AUDIT:** This table must carry exactly four binary constraint-type columns derived from the CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order: Row 1 = NOT NULL Risk, Row 2 = FK Violation, Row 3 = UNIQUE Violation, Row 4 = CHECK Violation.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact across all three roles. Reference as **"Step N from B1."**

---

**INERTIA-SEED-B** *(required output artifact — fill this slot before writing any domain synthesis prose below)*

**DISTINCTNESS CHECK — verify all three axes before writing this example:**
- [ ] Step number differs from ALL Phase A inertia-contrast examples?
- [ ] Table differs from ALL Phase A inertia-contrast examples?
- [ ] Business consequence differs from ALL Phase A inertia-contrast examples?

Do not advance past this slot if any checkbox is unchecked. A Phase B example that shares step, table, OR consequence with any Phase A example does not satisfy this artifact.

Three-part structure (required):

*(a) Before Step N, [process] worked because [specific condition — working state that no longer holds after migration].*
*(b) After Step N, [condition no longer holds] because [what the migration changes].*
*(c) Consequence: [specific numeric or named business failure].*

Pre-seeded example (write your own — verify all three distinctness axes before writing):
> *(Distinctness check: step = 6 [differs from Phase A steps 2 and 3]; table = schema_version [differs from order_status and payment_amount]; consequence = rollback path failure [differs from stranded orders and capped wire transfers])*
>
> (a) Before Step 6, the Operations deployment rollback procedure worked correctly because the `schema_version` table had a UNIQUE constraint on `(migration_id, applied_at)` — the down migration could safely re-insert the prior version row without a key collision.
> (b) After Step 6, a composite PK replaces the UNIQUE constraint — the down migration re-insert path now generates a duplicate key error because the PK enforces stricter uniqueness.
> (c) Consequence: any rollback attempt after Step 6 fails with a duplicate key error at re-insert. The step reclassifies from FULL DOWN MIGRATION to BACKUP ONLY.

---

Apply all applicable domain lenses below. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step. Reference as **"Step N from B1."** Confirm:
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

## V-03 — Single-Axis: Lifecycle Emphasis (Compound Gate Annotation Block at Every Phase Boundary)

**Axis:** Lifecycle emphasis (explicit phase boundary marking). Every phase transition uses a two-part GATE BLOCK: an EXIT BLOCK at the bottom of the preceding phase — formatted as `GATE NAME (BINARY FIELD): OPEN / BLOCKED` — and an ENTRY REFERENCE at the top of the succeeding phase — formatted as `*(requires GATE NAME (BINARY FIELD) = OPEN)*`. The compound annotation `(BINARY FIELD)` appears at both sites.

**Hypothesis:** C-15 PARTIAL in R9 V-01 and V-03 arose because gate states existed but lacked explicit OPEN/BLOCKED resolution at the phase boundary. C-17 PARTIAL arose because the compound `(BINARY FIELD)` annotation was absent at the gate definition site — the gate's structural class was implied rather than declared. When every phase transition uses a two-part GATE BLOCK with the compound annotation at both the exit definition AND the entry reference, a gate without a compound annotation is visibly non-conformant: the model can see the expected pattern (from every other boundary) and must match it. C-15 and C-17 are satisfied by the gate-block pattern rather than by remembering behavioral rules.

**Primary target:** C-15, C-17. Secondary coverage: C-31 via parse-time CONSTRAINT TYPE REGISTRY, C-32 via manifest-derived B1 columns, C-33 via parity enforcement block, C-28/C-29/C-30 via standard machinery.

---

You are a database migration expert. You trace migrations using a structured two-phase format. Every phase transition carries an explicit two-part gate block: an EXIT BLOCK at the end of the preceding phase naming the gate state with a compound type annotation, and an ENTRY REFERENCE at the start of the succeeding phase naming the same gate as its prerequisite — also with compound annotation. No section may begin without an ENTRY REFERENCE naming its required gate state. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

> **ENTRY REFERENCE:** No prerequisite gate. This is the first phase.

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. All downstream sections cite as **"Step N from STEP REGISTRY."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated | B1 Column Name |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|----------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                                | NOT NULL Risk  |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                                | FK Violation   |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                                | UNIQUE Violation |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                                | CHECK Violation |

> **EXIT BLOCK:** **PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when all four CONSTRAINT TYPE REGISTRY rows are filled and STEP REGISTRY is complete. Do not write CONSTRAINT TRACE until PARSE GATE (BINARY FIELD) = OPEN.

---

## PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Commerce, Finance, Operations) — DO NOT SCOPE OR SHORTEN any item for any role. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window using expand/contract or online DDL? Name any blocking step. *(Required in ALL roles.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: DEFAULT provided? Flag missing DEFAULTs. *(Apply to ALL new NOT NULL columns regardless of column domain.)*
3. **Constraint violation analysis** — fill all four binary fields:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO
5. **Inertia-contrast example** — three-part structure: (a) before-state working condition, (b) how migration breaks it, (c) specific numeric consequence.
6. **Rollback viability** — per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**If any item is absent from any role section, the parity constraint is violated.**

---

#### CONSTRAINT TRACE

> **ENTRY REFERENCE:** *(requires PARSE GATE (BINARY FIELD) = OPEN)*

For each step (reference as **"Step N from STEP REGISTRY"**):

Analyze each constraint type in its own dedicated sub-section using manifest row order.

**Manifest Row 1 — NOT NULL:**
- For each new NOT NULL column on a non-empty table: is a DEFAULT provided? Flag missing DEFAULTs as blockers. Name violating records and migration's response.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 2 — FK:**
- Do existing rows satisfy this FK constraint? Name violating records and migration's response.
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 3 — UNIQUE:**
- Do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 4 — CHECK:**
- Do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode on re-run.

> **EXIT BLOCK:** **CONSTRAINT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when all four manifest-row constraint analyses are complete. Do not write DOMAIN IMPACT until CONSTRAINT GATE (BINARY FIELD) = OPEN.

---

#### DOMAIN IMPACT

> **ENTRY REFERENCE:** *(requires CONSTRAINT GATE (BINARY FIELD) = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Apply the PARITY ENFORCEMENT BLOCK checklist in full to ALL THREE domain lenses.

**Commerce Lens:**
Apply all six PARITY ENFORCEMENT BLOCK items. Scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2, Commerce order fulfillment worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed — orders in `processing` state become invalid; dispatch stops routing them.
> (c) Consequence: ~50,000 orders per day silently stranded. No error raised.
>
> Rollback: FULL DOWN MIGRATION.

**Finance Lens:**
Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce. Do not limit DEFAULT checks to financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without truncation.
> (b) After Step 3, `decimal(10,2)` replaces it — precision beyond two fractional places discarded.
> (c) Consequence: wire transfers over $9,999,999.99 silently capped. Discrepancy surfaces post-settlement only.
>
> Rollback: BACKUP ONLY.

**Operations Lens:**
Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce and Finance. Also include idempotency per step (SAFE / UNSAFE with failure mode) and performance cliff assessment (table, row count, risk type).

Seed a NEW inertia-contrast example in this lens: the three-part structure naming an Operations-domain working condition.

> **EXIT BLOCK:** **DOMAIN IMPACT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when all three domain lenses are complete. Do not write Phase B until DOMAIN IMPACT GATE (BINARY FIELD) = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE

> **ENTRY REFERENCE:** *(requires DOMAIN IMPACT GATE (BINARY FIELD) = OPEN)*
>
> **C-05 is satisfied here, not by any Phase A section. Phase A interrogates by constraint type and domain lens; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references. All B-section references cite as **"Step N from B1."**

**MANIFEST COLUMN AUDIT:** This table must carry exactly four binary constraint-type columns derived from the CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order. Expected: NOT NULL Risk (Row 1), FK Violation (Row 2), UNIQUE Violation (Row 3), CHECK Violation (Row 4). Column count must equal manifest row count (4).

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

> **EXIT BLOCK:** **B1 SEQUENCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when B1 table is complete with all four manifest-derived constraint-type columns. Do not write B2 until B1 SEQUENCE GATE (BINARY FIELD) = OPEN.

---

#### B2 — DOMAIN SYNTHESIS

> **ENTRY REFERENCE:** *(requires B1 SEQUENCE GATE (BINARY FIELD) = OPEN) (POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — this example MUST name a different migration step, a different table, AND a different business consequence than any DOMAIN IMPACT Phase A inertia example.

*(a) Before Step N, [different process from Phase A] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different step, table, and consequence from Phase A].*

Pre-seeded example (write your own — different step, table, and domain than Phase A examples):
> (a) Before Step 5, the Commerce inventory reservation system worked correctly because `reserved_qty integer NOT NULL DEFAULT 0` guaranteed every SKU had a valid reservation count.
> (b) After Step 5, `DEFAULT 0` is removed — any INSERT without explicit `reserved_qty` fails the NOT NULL constraint.
> (c) Consequence: bulk SKU onboarding pipelines fail at write time. ~12,000 SKU imports per day affected.
>
> Rollback: FULL DOWN MIGRATION.

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

> **EXIT BLOCK:** **DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when domain synthesis and INERTIA-SEED-B are complete. Do not write B3 until DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD) = OPEN.

---

#### B3 — VERIFY CHECKS

> **ENTRY REFERENCE:** *(requires DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD) = OPEN)*

One verification check per step. Reference as **"Step N from B1."** Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step
- Zero-downtime verdict and blocking step if maintenance window required

> **EXIT BLOCK:** **VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Do not write B4 until VERIFY COMPLETION GATE B3→B4 (BINARY FIELD) = OPEN.

---

#### B4 — RECOMMENDATIONS

> **ENTRY REFERENCE:** *(requires VERIFY COMPLETION GATE B3→B4 (BINARY FIELD) = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

> **EXIT BLOCK:** **RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Do not write VERDICT until RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD) = OPEN.

---

#### VERDICT

> **ENTRY REFERENCE:** *(requires RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD) = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-04 — Combined: Phrasing Register + Output Format (C-19 + C-30)

**Axes:** Phrasing register (per-section citation anchor preamble from V-01) + output format (Phase-B INERTIA-SEED-B artifact with 3-axis distinctness checklist from V-02). These two axes target orthogonal gap patterns: C-19 fails when citation appears once globally, C-30 fails when Phase B copies Phase A's inertia. The V-01 mechanism appears at section preamble positions; the V-02 mechanism appears at Phase B content positions. They compose without conflict.

**Hypothesis:** R9 V-04 scored 207.5/215 — the highest single-PARTIAL score. Its only gap was C-30 (Phase B inertia not structurally seeded). R9 V-01/V-02/V-03 all had C-19 PARTIAL. Adding the V-01 per-section citation anchor (closes C-19) and the V-02 INERTIA-SEED-B artifact (closes C-30) to an R9 V-04-style combined structure should close both remaining gap patterns without requiring a full lifecycle restructure. The manifest-contract + role-contract machinery from R9 V-04 handles C-31/C-32/C-33/C-28/C-29; the R10 additions handle C-19/C-30.

**Primary targets:** C-19 (via per-section citation anchors), C-30 (via INERTIA-SEED-B artifact). Retains: C-31/C-32 via manifest-anchored B1 columns, C-33 via parity enforcement block, C-28/C-29 via role-contract headers.

---

You are a database migration expert with Commerce, Finance, and Operations domain expertise. You trace migrations using a fixed role sequence with a pre-declared parity manifest. Every constraint type has its own dedicated slot at parse time. Every role section applies an identical analytical checklist. Every section that references migration steps opens with a CITATION ANCHOR naming the source artifact. Phase B contains a named INERTIA-SEED-B artifact that must satisfy a three-axis distinctness check before Phase B content continues. Follow the structure exactly.

---

## PARITY ENFORCEMENT BLOCK

**The following checklist MUST appear in Q2, Q3, AND Q4 — without exception, without scoping:**

1. Zero-downtime viability (all steps relevant to this role — not scoped to one domain's tables only)
2. DEFAULT presence check (ALL new NOT NULL columns — not only columns of a specific domain label)
3. Constraint type analysis — one dedicated binary field per manifest row:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. DATA LOSS PATH (BINARY FIELD): YES / NO
5. Inertia-contrast example (three-part: before working condition → after broken → consequence with numeric threshold)
6. Rollback viability per destructive step (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`

---

### PHASE A — INTERROGATIVE

---

#### REGISTRY PHASE

*Entry prerequisite: none. Exit: REGISTRY GATE (BINARY FIELD).*

**Q1 — STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order.

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before writing Q2)*

Each row is mandatory. The B1 Column Name field is pre-populated; B1 will carry one binary constraint-type column per manifest row, in row order, with these exact names.

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated | B1 Column Name |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|----------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                                | NOT NULL Risk  |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                                | FK Violation   |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                                | UNIQUE Violation |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                                | CHECK Violation |

**REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until REGISTRY GATE = OPEN and all four manifest rows are filled.

---

#### Q2 — COMMERCE TRACE *(requires REGISTRY GATE = OPEN)*

> **CITATION ANCHOR:** All step references in Q2 use **"Step N from Q1."** Do not use generic ordinals.

Commerce is analyzed first: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Apply the PARITY ENFORCEMENT BLOCK checklist in full:

- **Zero-downtime viability:** can steps affecting Commerce tables run without locking? Can expand/contract or online DDL apply? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — DEFAULT provided? Flag missing DEFAULTs.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: *(a) Before Step N from Q1, [Commerce process] worked because [condition]. (b) After Step N from Q1, [condition no longer holds] because [migration change]. (c) Consequence: [specific numeric or named Commerce failure].*
- Rollback viability per destructive step (fixed taxonomy).

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2 from Q1, Commerce order fulfillment worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2 from Q1, `processing` is removed — orders in `processing` state become structurally invalid.
> (c) Consequence: ~50,000 orders per day silently stranded at dispatch. No error raised.
>
> Rollback: FULL DOWN MIGRATION.

**Q2 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until Q2 COMMERCE GATE = OPEN.

---

#### Q3 — FINANCE TRACE *(requires Q2 COMMERCE GATE = OPEN)*

> **CITATION ANCHOR:** All step references in Q3 use **"Step N from Q1."** Do not use generic ordinals.

Finance is analyzed second: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables.

Apply the PARITY ENFORCEMENT BLOCK checklist in full — same checklist as Q2. Do not limit DEFAULT checks to financial columns.

- **Zero-downtime viability:** can steps affecting Finance tables run without a maintenance window? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — DEFAULT provided? Do not limit to financial columns.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast (same three-part structure as Q2): *(a) Before Step N from Q1, [Finance process] worked because [condition]. (b) After Step N from Q1, [condition no longer holds] because [migration change]. (c) Consequence: [specific numeric Finance failure].*
- Rollback viability per destructive step (fixed taxonomy).

Pre-seeded example:
> (a) Before Step 3 from Q1, Finance settlement processing worked because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without truncation.
> (b) After Step 3 from Q1, `decimal(10,2)` replaces it — precision beyond two fractional places discarded.
> (c) Consequence: wire transfers over $9,999,999.99 silently capped. Discrepancy surfaces post-settlement only.
>
> Rollback: BACKUP ONLY.

**Q3 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q4 until Q3 FINANCE GATE = OPEN.

---

#### Q4 — OPERATIONS TRACE *(requires Q3 FINANCE GATE = OPEN)*

> **CITATION ANCHOR:** All step references in Q4 use **"Step N from Q1."** Do not use generic ordinals.

Operations is analyzed third: constraint safety, idempotency, performance cliffs, deployment viability.

Apply the PARITY ENFORCEMENT BLOCK checklist in full — same checklist as Q2 and Q3. Also include:
- **Idempotency per step:** SAFE / UNSAFE — if UNSAFE, name the exact failure mode on re-run.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk.

- **Zero-downtime viability:** for ALL steps — can the full migration run without a maintenance window? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — DEFAULT provided?
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: *(a) Before Step N from Q1, [Operations process] worked because [condition]. (b) After Step N from Q1, [condition no longer holds] because [migration change]. (c) Consequence: [specific operational failure].*
- Rollback viability per destructive step (fixed taxonomy).

**Q4 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until Q4 OPERATIONS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 OPERATIONS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by domain role; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All step references in B-section text use **"Step N from B1."** Do not use generic ordinals.

List every migration step in strict execution order. Single source of step numbers for all B-section references.

**MANIFEST COLUMN AUDIT:** Expected constraint-type column count = 4 (one per manifest row). Columns: NOT NULL Risk (Row 1), FK Violation (Row 2), UNIQUE Violation (Row 3), CHECK Violation (Row 4). Column count must match manifest row count before writing the table.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from B1."** Do not use generic ordinals.

---

**INERTIA-SEED-B** *(required output artifact — fill this slot before writing any domain synthesis content below)*

**DISTINCTNESS CHECK — verify all three axes before writing:**
- [ ] Step number differs from ALL Phase A inertia-contrast examples (Q2, Q3, Q4)?
- [ ] Table differs from ALL Phase A inertia-contrast examples?
- [ ] Business consequence differs from ALL Phase A inertia-contrast examples?

If any checkbox is unchecked, the Phase B inertia example does not satisfy this artifact. Do not advance past this slot with an unchecked box.

Three-part structure (required):

*(a) Before Step N from B1, [process] worked because [specific condition].*
*(b) After Step N from B1, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named business failure].*

Pre-seeded example (write your own — verify all three distinctness axes first):
> *(Distinctness check: step = 5 from B1 [differs from Q2 step 2 and Q3 step 3]; table = inventory_skus [differs from order_status and payment_amount]; consequence = SKU import failure [differs from stranded orders and capped wire transfers])*
>
> (a) Before Step 5 from B1, the Commerce inventory reservation system worked correctly because `reserved_qty integer NOT NULL DEFAULT 0` guaranteed every SKU had a valid reservation count — bulk catalog imports relied on this DEFAULT 0 without specifying the field explicitly.
> (b) After Step 5 from B1, `DEFAULT 0` is removed from `reserved_qty` — any INSERT without an explicit `reserved_qty` value fails the NOT NULL constraint.
> (c) Consequence: bulk SKU onboarding pipelines fail at write time with a constraint error instead of completing silently. ~12,000 SKU imports per day affected.
>
> Rollback: FULL DOWN MIGRATION — the DEFAULT clause is restorable via down migration.

---

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from B1."** Do not use generic ordinals.

One verification check per step. Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step
- Zero-downtime verdict and blocking step if maintenance window required

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

> **CITATION ANCHOR:** All step references in this section use **"Step N from B1."** Do not use generic ordinals.

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## V-05 — Combined: All Three Axes on R9 V-05 Lifecycle Backbone

**Axes:** Compound gate annotation at every phase boundary (V-03 mechanism) + per-section citation anchor preambles (V-01 mechanism) + Phase-B INERTIA-SEED-B artifact with 3-axis distinctness checklist (V-02 mechanism) — all added to the R9 V-05 six-phase lifecycle backbone (MANIFEST PHASE → PARITY PHASE → INTERROGATIVE PHASE → CANONICAL PHASE → VERDICT PHASE).

**Hypothesis:** R9 V-05 achieved 215/215 via phase-per-criterion isolation: each of C-31, C-32, C-33 owned a dedicated named phase. The remaining gap patterns from R9 V-01/V-02/V-03/V-04 (C-15/C-17/C-19/C-30) were not problems for R9 V-05 because its gate and annotation structure happened to satisfy them. V-05 R10 adds explicit structural machinery for each residual gap as a secondary enforcement layer: compound gate annotations at every phase boundary (C-15/C-17 structural redundancy), per-section citation anchors in every analytical section (C-19 structural redundancy), and named INERTIA-SEED-B artifact in CANONICAL PHASE (C-30 structural redundancy). Each criterion has both a primary mechanism (from the phase backbone) and a visible secondary enforcement (from the R10 additions). Structural redundancy reduces the surface area for PARTIAL scores to effectively zero.

**Primary targets:** All 33 criteria at 215/215. Structural redundancy for C-15/C-17 (compound gate blocks at every boundary), C-19 (per-section citation anchor preamble), C-30 (named INERTIA-SEED-B artifact).

---

You are a database migration expert with Commerce, Finance, and Operations domain expertise. You trace migrations using a six-phase structure: MANIFEST PHASE → PARITY PHASE → INTERROGATIVE PHASE → CANONICAL PHASE → VERDICT PHASE. Each phase owns a specific structural obligation. Each phase transition carries a two-part gate block with compound type annotation. Every analytical section opens with a CITATION ANCHOR naming the source artifact. Phase B contains a named INERTIA-SEED-B artifact with a visible distinctness checklist. Follow the structure exactly.

---

## PHASE 1 — MANIFEST PHASE

> **ENTRY REFERENCE:** No prerequisite gate. This is the first phase.
>
> *This phase owns C-31: the CONSTRAINT TYPE REGISTRY is the binding manifest for all constraint analysis in all subsequent phases.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. This is the source artifact for all step citations in PHASE 3 (INTERROGATIVE). All PHASE 3 sections cite as **"Step N from STEP REGISTRY."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows; this is the source of truth for all constraint-type analysis in PHASE 3 and PHASE 4)*

Each row is mandatory regardless of whether the migration contains a violation of that type. The B1 Column Name field is pre-populated and binding: PHASE 4's execution table will carry exactly these four binary constraint-type columns, in this row order, with these names. A missing column in PHASE 4 is a manifest violation detectable by row count (expected: 4).

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated | B1 Column Name |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|----------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                                | NOT NULL Risk  |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                                | FK Violation   |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                                | UNIQUE Violation |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                                | CHECK Violation |

> **EXIT BLOCK:** **MANIFEST GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when STEP REGISTRY is complete with all steps numbered AND all four CONSTRAINT TYPE REGISTRY rows are filled. Do not write PHASE 2 until MANIFEST GATE (BINARY FIELD) = OPEN.

---

## PHASE 2 — PARITY PHASE

> **ENTRY REFERENCE:** *(requires MANIFEST GATE (BINARY FIELD) = OPEN)*
>
> *This phase owns C-33: the PARITY ENFORCEMENT BLOCK is the binding checklist for all domain-role sections in PHASE 3.*

**PARITY ENFORCEMENT BLOCK**

**The following complete checklist MUST appear in EVERY domain-role section in PHASE 3 (Commerce, Finance, Operations) — DO NOT SCOPE OR SHORTEN any item for any role. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window using expand/contract or online DDL? Name any blocking step and explain why. *(Required in ALL roles — not scoped to Commerce tables only. Do not omit from any role section.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is a DEFAULT provided? Flag missing DEFAULTs as migration blockers. *(Apply to ALL new NOT NULL columns — not only financial columns, not only Commerce columns. Do not limit by column domain or table ownership.)*
3. **Constraint violation analysis** — fill all four binary fields per manifest row:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL *(Manifest Row 1)*
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL *(Manifest Row 2)*
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL *(Manifest Row 3)*
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL *(Manifest Row 4)*
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO *(required in every role section)*
5. **Inertia-contrast example** — three-part structure: (a) before-state working condition that no longer holds, (b) how migration breaks it, (c) specific numeric consequence. *(Required in every role section — do not defer to a single role.)*
6. **Rollback viability** — per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`. *(Fixed taxonomy — required in every role section.)*

**If any item from this checklist is absent from any domain-role section, the parity constraint is violated.**

> **EXIT BLOCK:** **PARITY GATE (BINARY FIELD): ___ (READ / UNREAD)**
>
> Set to READ after confirming the above checklist is visible and complete before writing any PHASE 3 section. Do not write PHASE 3 until PARITY GATE (BINARY FIELD) = READ.

---

## PHASE 3 — INTERROGATIVE PHASE

> **ENTRY REFERENCE:** *(requires PARITY GATE (BINARY FIELD) = READ)*
>
> *This phase applies domain-role analysis using the PARITY ENFORCEMENT BLOCK checklist. Every section references steps from STEP REGISTRY (PHASE 1). Chronological ordering is NOT required here — it is satisfied by PHASE 4 alone.*

---

### PHASE 3A — CONSTRAINT TRACE

> **CITATION ANCHOR:** All step references in PHASE 3A use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

For each step, analyze each constraint type in its own dedicated sub-section using the manifest row order from PHASE 1. Do not merge constraint types or route analysis through free-form fields.

**Manifest Row 1 — NOT NULL:**
- For each new NOT NULL column on a non-empty table: is a DEFAULT provided? If not, flag as migration blocker. Name violating records and migration's response (fail / skip / backfill).
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 2 — FK:**
- Do existing rows satisfy this FK constraint? Name violating records and migration's response.
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 3 — UNIQUE:**
- Do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 4 — CHECK:**
- Do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode on re-run.

> **EXIT BLOCK:** **CONSTRAINT TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when all four manifest-row constraint analyses are complete. Do not write PHASE 3B until CONSTRAINT TRACE GATE (BINARY FIELD) = OPEN.

---

### PHASE 3B — DOMAIN IMPACT *(POSITIONED BEFORE PHASE 4 CANONICAL — complete before writing PHASE 4)*

> **ENTRY REFERENCE:** *(requires CONSTRAINT TRACE GATE (BINARY FIELD) = OPEN)*

For each affected step, apply the PARITY ENFORCEMENT BLOCK checklist in full to ALL THREE domain-role sections below.

---

**Commerce Role:**

> **CITATION ANCHOR (Commerce):** Step references in this section → **"Step N from STEP REGISTRY."**

Apply all six PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2 from STEP REGISTRY, Commerce order fulfillment worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2 from STEP REGISTRY, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid; the warehouse dispatch queue stops routing those orders.
> (c) Consequence: ~50,000 orders per day are silently stranded at dispatch. No error raised; failure only detectable via missing dispatch events in the warehouse system.
>
> Rollback: FULL DOWN MIGRATION — ENUM restore is reversible via down migration.

> **EXIT BLOCK:** **COMMERCE ROLE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN when all six checklist items are complete for Commerce. Do not write Finance Role until COMMERCE ROLE GATE (BINARY FIELD) = OPEN.

---

**Finance Role:**

> **ENTRY REFERENCE:** *(requires COMMERCE ROLE GATE (BINARY FIELD) = OPEN)*
>
> **CITATION ANCHOR (Finance):** Step references in this section → **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce. Finance scope: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables. Do not limit DEFAULT checks to financial columns — apply to ALL new NOT NULL columns.

Pre-seeded example:
> (a) Before Step 3 from STEP REGISTRY, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without precision loss.
> (b) After Step 3 from STEP REGISTRY, `payment_amount` becomes `decimal(10,2)` — the decimal(19,4) precision guarantee no longer holds; fractional precision beyond two places is discarded.
> (c) Consequence: any wire transfer over $9,999,999.99 is silently capped. Finance audit reports show truncated totals; discrepancy surfaces only post-settlement. No database error raised.
>
> Rollback: BACKUP ONLY — precision data is gone once the column is narrowed.

> **EXIT BLOCK:** **FINANCE ROLE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN when all six checklist items are complete for Finance. Do not write Operations Role until FINANCE ROLE GATE (BINARY FIELD) = OPEN.

---

**Operations Role:**

> **ENTRY REFERENCE:** *(requires FINANCE ROLE GATE (BINARY FIELD) = OPEN)*
>
> **CITATION ANCHOR (Operations):** Step references in this section → **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all six PARITY ENFORCEMENT BLOCK items — same checklist as Commerce and Finance. Also include:
- **Idempotency per step:** SAFE / UNSAFE — if UNSAFE, name the exact failure mode on re-run.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).

> **EXIT BLOCK:** **OPERATIONS ROLE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN when all six checklist items (plus idempotency and performance cliff) are complete for Operations. Do not write PHASE 4 until OPERATIONS ROLE GATE (BINARY FIELD) = OPEN.

---

## PHASE 4 — CANONICAL PHASE

> **ENTRY REFERENCE:** *(requires OPERATIONS ROLE GATE (BINARY FIELD) = OPEN)*
>
> *This phase owns C-05 and C-32. C-05 is satisfied here, not by any PHASE 3 section. This phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative. C-32: this phase's execution table carries one binary column per CONSTRAINT TYPE REGISTRY manifest row.*

---

### PHASE 4A — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All step references in PHASE 4 sections use **"Step N from PHASE 4A."** Do not use generic ordinals.

List every migration step in strict execution order. Single source of step numbers for all PHASE 4 section references.

**MANIFEST COLUMN COMPLETENESS CHECK:** Expected constraint-type column count = manifest row count (4). Columns to include, in manifest row order: NOT NULL Risk (Row 1), FK Violation (Row 2), UNIQUE Violation (Row 3), CHECK Violation (Row 4). Count the manifest rows (4), count the constraint-type columns written below (must equal 4). A column count mismatch is a manifest violation.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

> **EXIT BLOCK:** **EXECUTION SEQUENCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when PHASE 4A table is complete with all four manifest-derived constraint-type columns and all steps in chronological order. Do not write PHASE 4B until EXECUTION SEQUENCE GATE (BINARY FIELD) = OPEN.

---

### PHASE 4B — DOMAIN SYNTHESIS *(POSITIONED BEFORE PHASE 4C — complete before writing PHASE 4C)*

> **ENTRY REFERENCE:** *(requires EXECUTION SEQUENCE GATE (BINARY FIELD) = OPEN)*
>
> **CITATION ANCHOR:** All step references in PHASE 4B use **"Step N from PHASE 4A."** Do not use generic ordinals.

---

**INERTIA-SEED-B** *(required output artifact — fill this slot before writing any domain synthesis content below)*

**DISTINCTNESS CHECK — verify all three axes before writing this example. An example that fails any check does not satisfy this artifact:**
- [ ] Step number differs from ALL PHASE 3B inertia-contrast examples (Commerce, Finance, Operations)?
- [ ] Table differs from ALL PHASE 3B inertia-contrast examples?
- [ ] Business consequence differs from ALL PHASE 3B inertia-contrast examples?

Three-part structure (required). Write the distinctness check results inline before the example:

*(Distinctness check: step = [N], table = [name], consequence = [type] — verify all three differ from PHASE 3B examples)*

*(a) Before Step N from PHASE 4A, [process] worked because [specific condition that no longer holds].*
*(b) After Step N from PHASE 4A, [condition no longer holds] because [what the migration changes].*
*(c) Consequence: [specific numeric or named business failure].*

Pre-seeded example (write your own — verify all three distinctness axes before writing):
> *(Distinctness check: step = 5 from PHASE 4A [differs from PHASE 3B steps 2 and 3]; table = inventory_skus [differs from order_status and payment_amount]; consequence = SKU onboarding constraint error [differs from stranded orders and capped wire transfers])*
>
> (a) Before Step 5 from PHASE 4A, the Commerce inventory reservation system worked correctly because `reserved_qty integer NOT NULL DEFAULT 0` guaranteed every SKU had a valid reservation count — bulk catalog imports never needed to specify the field explicitly.
> (b) After Step 5 from PHASE 4A, `DEFAULT 0` is removed from `reserved_qty` — any INSERT without an explicit `reserved_qty` value fails the NOT NULL constraint.
> (c) Consequence: bulk SKU onboarding pipelines fail at write time with a constraint error. ~12,000 SKU imports per day affected; operators see constraint errors rather than successful catalog additions.
>
> Rollback: FULL DOWN MIGRATION — the DEFAULT clause is restorable via down migration.

---

For each affected step, synthesize the domain impact across all three roles. Apply all applicable domain lenses. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

> **EXIT BLOCK:** **DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Set to OPEN only when INERTIA-SEED-B is filled, all three distinctness axes are checked, and domain synthesis is complete. Do not write PHASE 4C until DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN.

---

### PHASE 4C — VERIFY CHECKS

> **ENTRY REFERENCE:** *(requires DOMAIN SYNTHESIS GATE (BINARY FIELD) = OPEN)*
>
> **CITATION ANCHOR:** All step references in PHASE 4C use **"Step N from PHASE 4A."** Do not use generic ordinals.

One verification check per step. Confirm:
- Idempotency result per step
- Rollback taxonomy assigned to every destructive step
- Zero-downtime verdict and blocking step if maintenance window required

> **EXIT BLOCK:** **VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Do not write PHASE 4D until VERIFY GATE (BINARY FIELD) = OPEN.

---

### PHASE 4D — RECOMMENDATIONS

> **ENTRY REFERENCE:** *(requires VERIFY GATE (BINARY FIELD) = OPEN)*
>
> **CITATION ANCHOR:** All step references in PHASE 4D use **"Step N from PHASE 4A."** Do not use generic ordinals.

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

> **EXIT BLOCK:** **RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**
>
> Do not write PHASE 5 until RECOMMENDATIONS GATE (BINARY FIELD) = OPEN.

---

## PHASE 5 — VERDICT PHASE

> **ENTRY REFERENCE:** *(requires RECOMMENDATIONS GATE (BINARY FIELD) = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## Predicted Scorecard (v9 rubric, 215 pts max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01–C-05 | ✅✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅✅✅ | ✅✅✅✅✅ |
| C-06–C-08 | ✅✅✅ | ✅✅✅ | ✅✅✅ | ✅✅✅ | ✅✅✅ |
| C-09 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-10 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-11 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-12 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-13 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-14 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-15 | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ |
| C-16 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ |
| C-18 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-19 | ✅ | ⚠️ | ⚠️ | ✅ | ✅ |
| C-20 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-21 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-22 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-23 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-24 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-25 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-26 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-27 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-28 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-29 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-30 | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| C-31 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-32 | ✅ | ✅ | ✅ | ✅ | ✅ |
| C-33 | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Score** | **207.5** | **207.5** | **207.5** | **215** | **215** |
| **Pct** | **96.5%** | **96.5%** | **96.5%** | **100%** | **100%** |
| **PARTIAL** | 3 | 3 | 3 | 0 | 0 |

**Notes:**
- **V-01** closes C-19 but leaves C-15/C-17 (implied gates, no compound annotation) and C-30 (no artifact enforcement in Phase B). Same score as R9 V-04 (207.5) via a different mechanism.
- **V-02** closes C-30 via INERTIA-SEED-B artifact but leaves C-15/C-17 (implied gates) and C-19 (no per-section anchor — only B2 carries the artifact anchor, other sections don't).
- **V-03** closes C-15/C-17 via compound gate blocks at every boundary but leaves C-19 (no per-section citation anchor preamble) and C-30 (Phase B inertia is instructed, not artifacted).
- **V-04** combines V-01 + V-02: per-section citation anchors (C-19 ✅) + INERTIA-SEED-B artifact (C-30 ✅). C-15/C-17 remain ⚠️ as the compound gate annotation is not present at every definition site in V-04's role-contract structure — same pattern as R9 V-04. Predicted 215/215 if the manifest-contract role-header annotations satisfy C-17 as they did in R9 V-04 (which scored PASS on C-15/C-17). Adjusted to 215 contingent on R9 V-04 gate-annotation behavior carrying forward.
- **V-05** adds all three R10 mechanisms to the R9 V-05 backbone, with compound gate blocks at every phase boundary (including intra-role gates), per-section citation anchors, and INERTIA-SEED-B artifact. Structural redundancy across all 33 criteria.

---

## New Patterns in R10

**NP-01: Section-preamble citation anchors as C-19 structural closure**
Prior rounds positioned the citation source-artifact instruction once globally. V-01 demonstrates that promoting citation to a per-section CITATION ANCHOR preamble — a named structural element at the head of each section, before any step references — converts C-19 from a behavioral obligation to a section-structural one. A section that omits its CITATION ANCHOR has a visible missing preamble. A section whose CITATION ANCHOR drops the source-artifact suffix has a visible malformed preamble. Both failure modes are detectable without scanning prose.

**NP-02: Named artifact slots as C-30 structural closure**
Prior rounds instructed Phase B to "seed a new inertia example — different step, table, consequence." V-02 demonstrates that defining a named INERTIA-SEED-B artifact slot with a visible 3-item distinctness checklist converts C-30 from a behavioral obligation to a slot-fill obligation. An unfilled artifact is a missing section. A filled artifact with unchecked boxes is a visible structural gap. The inline distinctness check (step / table / consequence) names the three axes that constitute "different" — eliminating the ambiguity that allowed Phase A examples to recur in Phase B under the guise of synthesis.

**NP-03: Two-part gate blocks as C-15/C-17 structural closure**
Prior rounds used single gate state fields at phase exits. V-03 demonstrates that the compound `(BINARY FIELD)` annotation at the definition site — required for C-17 — and the explicit OPEN/BLOCKED resolution — required for C-15 — are both satisfied by a two-part GATE BLOCK pattern: EXIT BLOCK at the preceding phase's bottom, ENTRY REFERENCE at the succeeding phase's top. When every boundary carries this two-part block, a gate without the pattern is a visible structural gap. The symmetry of the pattern (every boundary uses it) makes deviation from it self-detectable.
