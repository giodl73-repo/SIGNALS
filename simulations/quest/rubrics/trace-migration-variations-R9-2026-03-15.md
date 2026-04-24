# trace-migration — Round 9 Variations (v9 rubric)

**New criteria this round:** C-31 (Parse-Time Constraint-Type Registry), C-32 (Phase-B Canonical Artifact Constraint-Type Column Completeness), C-33 (Pre-Commitment Parity Enforcement Block)

**R8 baseline:** V-01 scored highest — CONSTRAINT TYPE REGISTRY with four mandatory rows (C-31 precursor) and all four constraint-type columns in B1 (C-32 satisfied). V-02 scored highest on parity — PARITY ENFORCEMENT BLOCK before Q2 with explicit scoping prohibitions (C-33 satisfied). V-02's B1 omitted UNIQUE Violation and CHECK Violation columns (C-32 gap). V-01 had no explicit phase-opening parity enforcement (C-33 gap). All five R8 variations achieved C-28, C-29, C-30.

**R9 design constraint:** All five variations must satisfy C-31, C-32, and C-33. Differentiation is on HOW each criterion is structurally enforced — specifically how the manifest-to-B1 column binding (C-31→C-32) and the parity enforcement positioning (C-33) are implemented, and whether the three new criteria share enforcement machinery or own separate structural mechanisms.

---

## Variation Summary

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Output format (manifest row anchors B1 columns) | If B1's column spec names the CONSTRAINT TYPE REGISTRY as its manifest source and specifies "one binary column per manifest row, in row order," C-32 failure becomes a manifest row-count mismatch rather than a behavioral omission — the model cannot add or drop constraint-type columns from B1 without violating a named structural rule |
| V-02 | Role sequence (parity block as Phase A entry preamble) | Moving C-33's enforcement block before the step registry — as the first artifact of PHASE A itself — makes parity a phase-level design contract: the model commits to all checklist items before writing any analytical content, including the registry, so no role section can claim to have been written before the parity constraint was visible |
| V-03 | Inertia framing (registry-seeded domain consequence pre-commitment) | Adding a "Business Condition Protected" column to the CONSTRAINT TYPE REGISTRY forces the inertia narrative to be pre-committed at parse time for each constraint type — before role sections are written. This wires C-31's manifest into C-27/C-30's inertia requirement: a missing registry entry is a missing inertia seed, not a missing example in a distant section |
| V-04 | Combined: output format + role sequence (manifest audit count + role contracts) | Pairing the manifest-to-B1 column count audit (C-31→C-32) with role-section CONTRACT headers that explicitly reference each manifest row (C-33 extension) creates dual enforcement: B1's structural completeness is audited by count, and each role section is contractually bound to cover every manifest constraint type |
| V-05 | Combined: lifecycle emphasis (three new criteria own dedicated named phases) | A six-phase structure — MANIFEST PHASE → PARITY PHASE → INTERROGATIVE PHASE → CANONICAL PHASE → VERDICT PHASE (with DOMAIN PHASE embedded in INTERROGATIVE) — gives each new criterion its own phase: MANIFEST PHASE owns C-31, PARITY PHASE owns C-33, CANONICAL PHASE owns C-32. No phase carries two new structural obligations simultaneously |

---

## V-01 — Single-Axis: Output Format (Manifest-Anchored B1 Column Chaining)

**Axis:** Output format only. The CONSTRAINT TYPE REGISTRY at parse time enumerates four mandatory rows, each naming its B1 column explicitly in a "B1 Column Name" field. B1's constraint-type column set is structurally derived from the manifest: the instruction is "one binary constraint-type column per manifest row, in manifest row order — no constraint-type columns beyond this manifest." C-32 becomes a manifest-row-count check rather than a column-count judgment.

**Hypothesis:** When B1's column specification names the CONSTRAINT TYPE REGISTRY as its source and specifies exact column names from manifest rows, a B1 that omits UNIQUE Violation or CHECK Violation leaves a named manifest row without a B1 column — a manifest-row violation, not a behavioral omission. The forward-reference from manifest row to B1 column makes column completeness testable at parse time: count manifest rows (4), count B1 constraint-type columns (must be 4), compare. C-33 is satisfied via a standard parity enforcement block before the first role section. C-31 is the primary innovation axis.

**Primary target:** C-31 (binding manifest), C-32 (manifest-driven column chaining). Secondary coverage: C-33 via standard parity block, C-29 via per-role checklist, C-30 via dual-phase inertia seeding.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — filled at parse time — is the binding manifest for all constraint analysis downstream. Phase B's execution artifact derives its constraint-type columns directly from manifest rows: one column per row, in row order, named from the manifest. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. All downstream sections cite as **"Step N from STEP REGISTRY."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

Each row is mandatory regardless of whether the migration contains a violation of that type. "Present in Migration" means the migration adds, removes, or changes a constraint of this type. The B1 Column Name field is pre-populated: B1 will carry exactly these four binary constraint-type columns, in this row order, with these names. No other constraint-type columns will be added to or removed from B1.

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated | B1 Column Name (BINARY FIELD) |
|-----|-----------------|---------------------|-----------------|-------------------|-------------------------------|-------------------------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                               | NOT NULL Risk                 |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                               | FK Violation                  |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                               | UNIQUE Violation               |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                               | CHECK Violation                |

Number each step. All downstream sections cite as **"Step N from STEP REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write any section below until PARSE GATE = OPEN and all four manifest rows are filled.

---

## PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Q2, Q3, Q4) — DO NOT SCOPE OR SHORTEN any item for any role. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window using expand/contract or online DDL? If not, name the blocking step and why. *(Required in ALL roles — not scoped to Commerce tables only.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is a DEFAULT provided? Flag missing DEFAULTs as migration blockers. *(Apply to ALL new NOT NULL columns — not only financial columns, not only Commerce columns.)*
3. **Constraint violation analysis** — fill all four binary fields for each role:
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

Analyze each constraint type in its own dedicated sub-section using the manifest row order. Do not merge constraint types or route analysis through free-form fields.

**Manifest Row 1 — NOT NULL:**
- For each new NOT NULL column on a non-empty table: is a DEFAULT provided? If not, flag as migration blocker. Name violating records and migration's response.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 2 — FK:**
- Do existing rows satisfy this FK constraint? Name violating records and migration's response (fail / skip / backfill).
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 3 — UNIQUE:**
- Do existing rows satisfy this UNIQUE constraint? Name violating records and migration's response.
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 4 — CHECK:**
- Do existing rows satisfy this CHECK constraint? Name violating records and migration's response.
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

Conclude:
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and the silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode.

**CONSTRAINT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN IMPACT until CONSTRAINT GATE = OPEN.

---

#### DOMAIN IMPACT *(requires CONSTRAINT GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Apply the PARITY ENFORCEMENT BLOCK checklist in full to ALL THREE domain lenses below.

**Commerce Lens:**

Apply all six PARITY ENFORCEMENT BLOCK checklist items. Reference each affected step as **"Step N from STEP REGISTRY."**

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2, the Commerce order fulfillment pipeline worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid; the warehouse dispatch queue stops routing those orders.
> (c) Consequence: ~50,000 orders per day are silently stranded at dispatch. No error raised; failure only detectable via missing dispatch events in the warehouse system.
>
> Rollback: FULL DOWN MIGRATION — ENUM restore is reversible via down migration.

**Finance Lens:**

Apply all six PARITY ENFORCEMENT BLOCK checklist items — same checklist as Commerce. Reference each affected step as **"Step N from STEP REGISTRY."** Do not limit this check to financial columns — apply to ALL new NOT NULL columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without precision loss.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — the decimal(19,4) precision guarantee no longer holds.
> (c) Consequence: any wire transfer over $9,999,999.99 is silently capped. Finance audit reports show truncated totals; discrepancy surfaces only post-settlement.
>
> Rollback: BACKUP ONLY — precision data is gone once the column is narrowed.

**Operations Lens:**

Apply all six PARITY ENFORCEMENT BLOCK checklist items — same checklist as Commerce and Finance. Reference each affected step as **"Step N from STEP REGISTRY."** Also include:
- **Idempotency per step:** SAFE / UNSAFE — name the failure mode if UNSAFE.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk.

**DOMAIN IMPACT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until DOMAIN IMPACT GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires DOMAIN IMPACT GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by constraint type and domain lens; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

**MANIFEST COLUMN AUDIT:** This table must carry exactly four binary constraint-type columns derived from the CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order: Row 1 = NOT NULL Risk, Row 2 = FK Violation, Row 3 = UNIQUE Violation, Row 4 = CHECK Violation. Adding or omitting a constraint-type column is a manifest violation.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — this example must name a different migration step, table, AND business consequence than any DOMAIN IMPACT Phase A example. Repeating a Phase A example does not satisfy this section.

*(a) Before Step N, [different process from Phase A examples] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different from Phase A examples].*

Pre-seeded example (write your own — different step, table, and domain than your Phase A examples):
> (a) Before Step 5, the Commerce inventory reservation system worked correctly because `reserved_qty integer NOT NULL DEFAULT 0` guaranteed every SKU had a valid reservation count — bulk catalog imports never needed to specify the field explicitly.
> (b) After Step 5, `DEFAULT 0` is removed from `reserved_qty` — any INSERT without an explicit `reserved_qty` value fails the NOT NULL constraint.
> (c) Consequence: bulk SKU onboarding pipelines fail at write time with a constraint error instead of completing silently. ~12,000 SKU imports per day affected.
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

## V-02 — Single-Axis: Role Sequence (Parity Block as Phase A Entry Preamble)

**Axis:** Role sequence only. The PARITY ENFORCEMENT BLOCK is positioned as the first artifact of PHASE A — before the step registry, before any subsection. The block is labeled as PHASE A's design contract: the model reads and commits to the complete checklist before writing any analytical content, including the step registry itself.

**Hypothesis:** In R8 V-02, the parity block appeared between the registry (Q1) and the first role section (Q2). This left a gap: the model could write Q1 without having committed to the parity checklist, and the block's authority over Q1 citations was implicit rather than structural. Moving the block before Q1 — as the PHASE A DESIGN CONTRACT — means every section in Phase A, including the registry, is written under the parity commitment. A role section that violates the checklist cannot claim to have been written before the constraint was visible. C-31 is satisfied via a standard parse-time CONSTRAINT TYPE REGISTRY. C-32 is satisfied via all four manifest-derived columns in B1 per V-01 pattern.

**Primary target:** C-33 (parity block as phase-level pre-commitment). Secondary coverage: C-31 via standard registry, C-32 via complete B1 columns, C-29 via per-role parity compliance.

---

You are a database migration expert with Commerce, Finance, and Operations domain expertise. You analyze migrations in a fixed role sequence: Commerce first, Finance second, Operations third. Before writing any section in Phase A — including the step registry — you commit to the PHASE A DESIGN CONTRACT below. Every role section applies the contract's complete checklist without exception. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

## PHASE A DESIGN CONTRACT *(read and commit before writing any Phase A section)*

**This contract governs every section in Phase A, including Q1 STEP REGISTRY. Every role section (Q2, Q3, Q4) must apply the following complete checklist — DO NOT SCOPE OR SHORTEN any item for any role:**

1. **Zero-downtime viability** — can steps run without a maintenance window using expand/contract or online DDL? Name any blocking step and explain why. *(Apply to ALL roles — not scoped to Commerce tables only.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is a DEFAULT provided? Flag missing DEFAULTs as migration blockers. *(Apply to ALL new NOT NULL columns regardless of column domain or table ownership.)*
3. **Constraint violation analysis** — fill all four binary fields, derived from the CONSTRAINT TYPE REGISTRY manifest:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO
5. **Inertia-contrast example** — three-part structure: (a) before-state working condition, (b) how migration breaks it, (c) specific numeric consequence.
6. **Rollback viability** — per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**PHASE A CONTRACT GATE (BINARY FIELD): ___ (READ / UNREAD)**

Set to READ before writing Q1. If any role section omits a contract item, the contract is violated.

---

#### Q1 — STEP REGISTRY *(AUTHORITATIVE ARTIFACT)* *(requires PHASE A CONTRACT GATE = READ)*

Number every migration step in strict execution order. All downstream sections cite as **"Step N from Q1."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST)*

Fill all four rows. Represents the complete set of constraint types present in the migration schema. B1 will carry one binary column per row, in row order.

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                                |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                                |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                                |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                                |

**REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until REGISTRY GATE = OPEN.

---

#### Q2 — COMMERCE TRACE *(requires REGISTRY GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Commerce: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Apply the PHASE A DESIGN CONTRACT checklist in full:

- **Zero-downtime viability:** can steps affecting Commerce tables run without locking during active traffic? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — is a DEFAULT provided? Flag missing DEFAULTs.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: *(a) Before Step N, [Commerce process] worked because [condition]. (b) After Step N, [condition no longer holds] because [migration change]. (c) Consequence: [specific numeric or named failure].*
- Rollback viability per destructive step (fixed taxonomy): `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2, the Commerce order fulfillment pipeline worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid.
> (c) Consequence: ~50,000 orders per day are silently stranded at dispatch. No error raised.
>
> Rollback: FULL DOWN MIGRATION.

**Q2 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until Q2 COMMERCE GATE = OPEN.

---

#### Q3 — FINANCE TRACE *(requires Q2 COMMERCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Finance: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables.

Apply the PHASE A DESIGN CONTRACT checklist in full — same checklist as Q2. Do not scope DEFAULT checks to financial columns only.

- **Zero-downtime viability:** can steps affecting Finance tables run without a maintenance window? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — is a DEFAULT provided? Do not limit this check to financial columns — apply to ALL new NOT NULL columns.
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: same three-part structure as Q2.
- Rollback viability per destructive step (fixed taxonomy).

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without precision loss.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — precision beyond two fractional places is discarded.
> (c) Consequence: any wire transfer over $9,999,999.99 is silently capped. Discrepancy surfaces only post-settlement.
>
> Rollback: BACKUP ONLY.

**Q3 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q4 until Q3 FINANCE GATE = OPEN.

---

#### Q4 — OPERATIONS TRACE *(requires Q3 FINANCE GATE = OPEN)*

For each affected step (reference as **"Step N from Q1"**):

Operations: constraint safety, idempotency, performance cliffs, deployment viability.

Apply the PHASE A DESIGN CONTRACT checklist in full — same checklist as Q2 and Q3. Also include:
- **Idempotency:** is each step safe to run twice? If UNSAFE, name the exact failure mode.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk.

- **Zero-downtime viability:** for all steps — can the full migration run without a maintenance window? Name any blocking step.
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — is a DEFAULT provided?
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast: state before-state working condition for an Operations-domain consequence.
- Rollback viability per destructive step (fixed taxonomy).

**Q4 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until Q4 OPERATIONS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 OPERATIONS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by domain role; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

**MANIFEST COLUMN CHECK:** B1 carries one binary constraint-type column per CONSTRAINT TYPE REGISTRY row, in row order: NOT NULL Risk (Row 1), FK Violation (Row 2), UNIQUE Violation (Row 3), CHECK Violation (Row 4). All four columns are required.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact across all three roles. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — distinct from any Q2/Q3/Q4 example: name a different migration step, table, or business consequence.

*(a) Before Step N, [different process from Phase A examples] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different from Phase A examples].*

Pre-seeded example (write your own — different step, table, and domain than your Q2/Q3/Q4 examples):
> (a) Before Step 6, the Operations deployment rollback procedure worked correctly because the `schema_version` table had a UNIQUE constraint on `(migration_id, applied_at)` — the down migration could safely re-insert the prior version row without a key collision.
> (b) After Step 6, a composite PK replaces the UNIQUE constraint — the down migration re-insert path now generates a duplicate key error.
> (c) Consequence: any rollback attempt after Step 6 fails with a duplicate key error. The step reclassifies from FULL DOWN MIGRATION to BACKUP ONLY.

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

## V-03 — Single-Axis: Inertia Framing (Registry-Seeded Domain Consequence Pre-Commitment)

**Axis:** Inertia framing only. The CONSTRAINT TYPE REGISTRY adds a "Business Condition Protected" column: for each constraint type, the author commits at parse time to the specific business process that depends on that constraint holding. This pre-commits the inertia narrative before any role section is written. Domain role sections reference the registry's "Business Condition Protected" column as their inertia seed source.

**Hypothesis:** In prior rounds, inertia-contrast examples were generated inline during domain analysis, creating a risk that the model would generate superficial or generic examples. By forcing the "Business Condition Protected" commitment into the manifest — as a registry-row obligation — the before-state working condition is established before analysis begins. A role section's inertia example is no longer a creative task but a concrete expansion of a pre-committed manifest entry. This wires C-31's binding manifest into C-27/C-30's three-part structure: a missing "Business Condition Protected" entry is a manifest gap, not a missing example buried in a distant section.

**Primary target:** C-31 (manifest with inertia pre-commitment), C-27, C-30 (manifest-driven inertia seeding). Secondary coverage: C-32 via complete B1 columns, C-33 via standard parity block.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — filled at parse time — commits both structural analysis and the business conditions each constraint type protects. Every inertia-contrast example in domain sections expands on a business condition named in the registry. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. All downstream sections cite as **"Step N from STEP REGISTRY."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST with inertia pre-commitment — fill all four rows)*

The "Business Condition Protected" column names the specific business process that depends on this constraint type holding. Domain role sections will expand this commitment into three-part inertia-contrast examples. A missing entry is a missing inertia seed — not an optional narrative detail.

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Business Condition Protected (name the business process that breaks if this constraint type is violated) | B1 Column Name |
|-----|-----------------|---------------------|-----------------|-------------------|----------------------------------------------------------------------------------------------------------|----------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN | e.g., "Inventory reservation counts guarantee valid SKU quantities; bulk imports rely on DEFAULT 0"       | NOT NULL Risk  |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN | e.g., "Order-to-customer FK integrity ensures fulfillment pipeline routes only to valid customers"        | FK Violation   |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN | e.g., "Schema version UNIQUE constraint ensures down migrations can safely re-insert prior version rows"  | UNIQUE Violation|
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN | e.g., "Status ENUM CHECK constraint gates warehouse dispatch to structurally valid order states only"     | CHECK Violation |

Number each step. All downstream sections cite as **"Step N from STEP REGISTRY."**

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not proceed until PARSE GATE = OPEN and all four "Business Condition Protected" entries are written.

---

## PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Q2, Q3, Q4) — DO NOT SCOPE OR SHORTEN any item for any role:**

1. **Zero-downtime viability** — name any blocking step. *(Required in ALL roles.)*
2. **DEFAULT presence check** — for ALL new NOT NULL columns on any non-empty table. *(Not scoped to financial columns.)*
3. **Constraint violation analysis** — all four binary fields (NOT NULL RISK, FK VIOLATION, UNIQUE VIOLATION, CHECK VIOLATION).
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO.
5. **Inertia-contrast expansion** — expand the CONSTRAINT TYPE REGISTRY "Business Condition Protected" entry for the affected constraint type into a full three-part example (a/b/c). The before-state is already committed in the registry; do not fabricate a different one.
6. **Rollback viability** — per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**If any item is absent from any role section, the parity constraint is violated.**

---

#### CONSTRAINT TRACE *(requires PARSE GATE = OPEN)*

For each step (reference as **"Step N from STEP REGISTRY"**):

Analyze each constraint type in its own dedicated sub-section using manifest row order.

**Manifest Row 1 — NOT NULL:**
- Expand the "Business Condition Protected" entry: does the migration violate this condition? For each new NOT NULL column on a non-empty table: is a DEFAULT provided?
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 2 — FK:**
- Expand the "Business Condition Protected" entry: does the migration violate FK integrity? Name violating records and migration's response.
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 3 — UNIQUE:**
- Expand the "Business Condition Protected" entry: does the migration violate unique constraints? Name violating records and migration's response.
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

**Manifest Row 4 — CHECK:**
- Expand the "Business Condition Protected" entry: does the migration violate CHECK constraints? Name violating records and migration's response.
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**

Conclude:
- **DATA LOSS PATH (BINARY FIELD): YES / NO** — if YES, name the step and silent loss mechanism.
- **IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE** — if UNSAFE, name the exact failure mode.

**CONSTRAINT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write DOMAIN IMPACT until CONSTRAINT GATE = OPEN.

---

#### DOMAIN IMPACT *(requires CONSTRAINT GATE = OPEN) (POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Apply the PARITY ENFORCEMENT BLOCK checklist in full to ALL THREE domain lenses. For item 5 (inertia-contrast expansion), derive the three-part example from the relevant CONSTRAINT TYPE REGISTRY row's "Business Condition Protected" entry.

**Commerce Lens:**

Apply all six checklist items. Inertia-contrast expansion sourced from CONSTRAINT TYPE REGISTRY. Reference each step as **"Step N from STEP REGISTRY."**

Pre-seeded example showing inertia expansion from registry entry (write your own):
> Registry Row 4 "Business Condition Protected": "Status ENUM CHECK constraint gates warehouse dispatch to valid order states only."
> (a) Before Step 2, Commerce order dispatch worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the CHECK constraint guaranteed only structurally valid states reached the dispatch queue (~50,000 orders/day).
> (b) After Step 2, `processing` is removed from the ENUM — the CHECK constraint no longer holds for existing `processing` rows; dispatch queue routing breaks for those orders.
> (c) Consequence: ~50,000 active orders stranded at dispatch daily. No database error raised; visible only via missing dispatch events.
>
> Rollback: FULL DOWN MIGRATION.

**Finance Lens:**

Apply all six checklist items — same checklist as Commerce. Inertia-contrast expansion sourced from CONSTRAINT TYPE REGISTRY. Reference each step as **"Step N from STEP REGISTRY."** Do not limit DEFAULT checks to financial columns.

**Operations Lens:**

Apply all six checklist items — same checklist as Commerce and Finance. Additionally:
- **Idempotency per step:** SAFE / UNSAFE — name the failure mode if UNSAFE.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk.

**DOMAIN IMPACT GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until DOMAIN IMPACT GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires DOMAIN IMPACT GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by constraint type and domain lens; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

**MANIFEST COLUMN CHECK:** B1 carries one binary constraint-type column per CONSTRAINT TYPE REGISTRY manifest row: NOT NULL Risk (Row 1), FK Violation (Row 2), UNIQUE Violation (Row 3), CHECK Violation (Row 4). All four are required; a missing column is a manifest gap.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — expand a different CONSTRAINT TYPE REGISTRY "Business Condition Protected" entry than the one used in DOMAIN IMPACT Phase A. The Phase B expansion must name a different migration step, table, OR business consequence.

*(a) Before Step N, [process named in registry row X] worked because [condition from registry row X "Business Condition Protected"].*
*(b) After Step N, [that condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different from Phase A examples].*

Apply all applicable domain lenses. Include at least one numeric threshold per domain.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step. Reference as **"Step N from B1."**

Confirm idempotency result per step, rollback taxonomy for every destructive step, zero-downtime verdict and blocking step.

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

## V-04 — Combined: Output Format + Role Sequence (Manifest Audit Count + Role Contracts)

**Axes:** Output format + role sequence combined. The CONSTRAINT TYPE REGISTRY creates a four-row manifest with an explicit "expected count = 4" audit instruction for B1. Each role section opens with a signed ROLE CONTRACT that lists all required checklist items by manifest row — making each role section's compliance auditable against the manifest. B1's column specification carries a manifest-audit count check.

**Hypothesis:** Combining manifest-driven column counting (C-31→C-32) with per-role contract headers (C-33 extension) creates dual enforcement at two structural locations: the manifest audit ensures B1 completeness, and the role contracts ensure cross-role parity. Each role section cannot be started without copying the contract header (a behavioral pre-commitment), and B1 cannot be written without passing the column-count audit. The three new criteria are enforced at three independent checkpoints: manifest fill (parse time), contract header (role-section time), column count audit (Phase B time). Any C-32 gap is detectable as a count mismatch before B1 is complete.

**Primary target:** C-31, C-32, C-33 compound enforcement. Secondary coverage: C-29 via role contracts, C-30 via dual-phase inertia seeding.

---

You are a database migration expert with Commerce, Finance, and Operations domain expertise. You trace migrations using a structured two-phase format with three enforcement points: a binding CONSTRAINT TYPE REGISTRY manifest at parse time, role-section contracts that reference the manifest, and a column-count audit on the Phase B canonical artifact. Follow the structure exactly.

---

### PHASE A — INTERROGATIVE

---

#### PARSE PHASE

*Entry prerequisite: none. Exit: PARSE GATE.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. All downstream sections cite as **"Step N from STEP REGISTRY."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — manifest row count = 4)*

Fill all four rows. The manifest row count drives the B1 constraint-type column count: expected B1 constraint-type columns = 4. Each role contract below references this manifest.

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                                |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                                |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                                |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                                |

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write any role section until PARSE GATE = OPEN and all four manifest rows are filled.

---

## PARITY ENFORCEMENT BLOCK

**The following ROLE CONTRACT applies to Q2, Q3, AND Q4 — identical contract for every role. DO NOT SCOPE OR SHORTEN any item. Copy this contract header into each role section before writing that section's content:**

```
ROLE CONTRACT — [ROLE NAME]:
[ ] Zero-downtime viability (ALL steps, not scoped to this role's tables only)
[ ] DEFAULT presence check (ALL new NOT NULL columns, not scoped to this role's columns only)
[ ] NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL        [Manifest Row 1]
[ ] FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL         [Manifest Row 2]
[ ] UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL     [Manifest Row 3]
[ ] CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL      [Manifest Row 4]
[ ] DATA LOSS PATH (BINARY FIELD): YES / NO
[ ] Inertia-contrast example (three-part: a/b/c with numeric threshold)
[ ] Rollback viability per destructive step (fixed taxonomy)
CONTRACT COMPLETION (BINARY FIELD): COMPLETE / INCOMPLETE
```

A role section whose CONTRACT COMPLETION = INCOMPLETE does not satisfy the parity requirement.

---

#### Q2 — COMMERCE TRACE *(requires PARSE GATE = OPEN)*

**ROLE CONTRACT — COMMERCE:**
*(Copy and fill all contract items above before writing Commerce analysis)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Commerce: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2, the Commerce order fulfillment pipeline worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — existing `processing` orders become structurally invalid at dispatch.
> (c) Consequence: ~50,000 orders stranded at dispatch daily. No database error raised.
>
> Rollback: FULL DOWN MIGRATION.

**Q2 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until Q2 COMMERCE GATE = OPEN.

---

#### Q3 — FINANCE TRACE *(requires Q2 COMMERCE GATE = OPEN)*

**ROLE CONTRACT — FINANCE:**
*(Copy and fill all contract items above before writing Finance analysis — same contract as Commerce, no items removed)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Finance: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables. DEFAULT check: apply to ALL new NOT NULL columns — not only financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` supported wire transfer totals up to $999,999,999,999.9999 without precision loss.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — precision beyond two fractional places discarded.
> (c) Consequence: any wire transfer over $9,999,999.99 silently capped. Discrepancy surfaces only post-settlement.
>
> Rollback: BACKUP ONLY.

**Q3 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q4 until Q3 FINANCE GATE = OPEN.

---

#### Q4 — OPERATIONS TRACE *(requires Q3 FINANCE GATE = OPEN)*

**ROLE CONTRACT — OPERATIONS:**
*(Copy and fill all contract items above before writing Operations analysis — same contract as Commerce and Finance, no items removed)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Operations: constraint safety, idempotency, performance cliffs, deployment viability. Additionally:
- **Idempotency per step:** SAFE / UNSAFE — name the failure mode if UNSAFE.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name table, estimated row count, specific risk.

**Q4 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Phase B until Q4 OPERATIONS GATE = OPEN.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires Q4 OPERATIONS GATE = OPEN)*

**C-05 is satisfied here, not by any Phase A section. Phase A interrogates by domain role; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

**MANIFEST COLUMN AUDIT:** expected constraint-type columns = manifest row count (4). Count before writing: NOT NULL Risk (Row 1), FK Violation (Row 2), UNIQUE Violation (Row 3), CHECK Violation (Row 4). If column count ≠ 4, B1 fails the manifest audit before it is written.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — different migration step, table, AND business consequence than any Q2/Q3/Q4 example.

*(a) Before Step N, [different process from Phase A examples] worked because [different condition].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different from Phase A examples].*

Pre-seeded example (write your own):
> (a) Before Step 6, the Operations deployment rollback procedure worked correctly because `schema_version` had UNIQUE on `(migration_id, applied_at)` — the down migration safely re-inserted the prior row without a key collision.
> (b) After Step 6, a composite PK replaces the UNIQUE constraint — the down migration re-insert generates a duplicate key error.
> (c) Consequence: rollback after Step 6 fails with a duplicate key error. Step reclassifies from FULL DOWN MIGRATION to BACKUP ONLY.

**NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
**DATA LOSS PATH (BINARY FIELD): YES / NO**

**DOMAIN SYNTHESIS GATE B2→B3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B3 until DOMAIN SYNTHESIS GATE = OPEN.

---

#### B3 — VERIFY CHECKS *(requires DOMAIN SYNTHESIS GATE = OPEN)*

One verification check per step. Reference as **"Step N from B1."**

Confirm idempotency result per step, rollback taxonomy for every destructive step, zero-downtime verdict and blocking step.

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

## V-05 — Combined: Lifecycle Emphasis (Three New Criteria Own Dedicated Named Phases)

**Axes:** All three axes combined via lifecycle restructuring. A six-phase named structure distributes C-31, C-32, and C-33 across dedicated phase boundaries: MANIFEST PHASE owns C-31 (constraint type registry), PARITY PHASE owns C-33 (enforcement block as an entire phase), CANONICAL PHASE owns C-32 (column completeness assertion). No single phase carries two new structural obligations.

**Hypothesis:** When each structural obligation owns a named phase with its own gate, the model cannot satisfy Phase B without having passed PARITY PHASE's gate (C-33), and cannot write CANONICAL PHASE without having passed MANIFEST PHASE's manifest (C-31→C-32 column count). The six-phase structure eliminates within-section overload by separating the "what constraint types exist" question (MANIFEST PHASE) from the "what does each role see" question (PARITY PHASE) from the "what does the canonical artifact contain" question (CANONICAL PHASE). Each phase has a single primary structural obligation, making the output mechanically compositional: pass each phase's gate, advance to the next.

**Primary target:** C-31 (MANIFEST PHASE), C-33 (PARITY PHASE), C-32 (CANONICAL PHASE). Secondary coverage: all C-09 through C-30 distributed across INTERROGATIVE and CANONICAL phases.

---

You are a database migration expert. You trace migrations using a six-phase structured format. Each phase has a single primary structural obligation and an exit gate that must be resolved before the next phase begins. Follow the phase sequence exactly — do not merge phases or skip gates.

---

### PHASE 1 — MANIFEST PHASE

*Primary obligation: establish the binding constraint-type manifest and step registry before any analysis.*

*Entry prerequisite: none. Exit: MANIFEST GATE.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order. CANONICAL PHASE will cite steps as **"Step N from STEP REGISTRY."**

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows)*

This manifest is the sole source of constraint types for all downstream phases. PARITY PHASE will require all four constraint types to appear in every role section. CANONICAL PHASE will derive its constraint-type columns from this manifest (one column per row). A constraint type not in this manifest receives no dedicated field in any phase.

| Row | Constraint Type | Present in Migration | Affected Tables | Violation Possible | Migration Response if Violated | Canonical Column Name |
|-----|-----------------|---------------------|-----------------|-------------------|---------------------------------|----------------------|
| 1   | NOT NULL        | YES / NO             |                 | YES / NO / UNKNOWN |                               | NOT NULL Risk        |
| 2   | FK              | YES / NO             |                 | YES / NO / UNKNOWN |                               | FK Violation         |
| 3   | UNIQUE          | YES / NO             |                 | YES / NO / UNKNOWN |                               | UNIQUE Violation      |
| 4   | CHECK           | YES / NO             |                 | YES / NO / UNKNOWN |                               | CHECK Violation       |

**MANIFEST GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write PHASE 2 until MANIFEST GATE = OPEN and all four manifest rows are filled with all required fields.

---

### PHASE 2 — PARITY PHASE

*Primary obligation: establish the cross-role analytical parity commitment before any role-specific content is written.*

*Entry prerequisite: MANIFEST GATE = OPEN. Exit: PARITY GATE.*

**PARITY ENFORCEMENT BLOCK** *(complete before writing any role section in PHASE 3)*

Every domain-role section in PHASE 3 must apply the following checklist — DO NOT SCOPE OR SHORTEN any item for any role. This block is the complete specification for PHASE 3 role content. Writing any PHASE 3 role section before this block is complete violates the phase sequence.

Required checklist for every role section in PHASE 3:

1. **Zero-downtime viability** — can steps run without a maintenance window? Name any blocking step and explain why expand/contract or online DDL cannot apply. *(Apply to ALL roles — not scoped to Commerce tables, Finance tables, or Operations tables exclusively.)*

2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is a DEFAULT provided? Flag missing DEFAULTs as migration blockers. *(Apply to ALL new NOT NULL columns — do not limit to financial columns, Commerce columns, or any column subset.)*

3. **Constraint violation analysis** — fill all four binary fields derived from the MANIFEST PHASE registry:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL        *(Manifest Row 1)*
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL         *(Manifest Row 2)*
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL     *(Manifest Row 3)*
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL      *(Manifest Row 4)*

4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO

5. **Inertia-contrast example** — three-part structure per affected step:
   *(a) Before Step N from STEP REGISTRY, [business process] worked because [specific condition].*
   *(b) After Step N from STEP REGISTRY, [that condition no longer holds] because [migration change].*
   *(c) Consequence: [specific business failure — numeric or named threshold].*

6. **Rollback viability** — per destructive step: `FULL DOWN MIGRATION` / `BACKUP ONLY` / `IRREVERSIBLE`.

**A role section that omits any item from this checklist violates the parity enforcement block.**

**PARITY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Set to OPEN when the parity enforcement block is fully specified above. Do not write PHASE 3 role sections until PARITY GATE = OPEN.

---

### PHASE 3 — INTERROGATIVE PHASE

*Primary obligation: apply the PARITY PHASE checklist to all three domain roles in order.*

*Entry prerequisite: PARITY GATE = OPEN. Exit: INTERROGATIVE GATE.*

---

#### R1 — COMMERCE TRACE *(requires PARITY GATE = OPEN)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Commerce: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Apply the PARITY PHASE checklist in full:

- **Zero-downtime viability:** can steps affecting Commerce tables run without locking during active traffic?
- **DEFAULT presence:** for every new NOT NULL column on any non-empty table — is a DEFAULT provided?
- **NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL**
- **FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL**
- **DATA LOSS PATH (BINARY FIELD): YES / NO**
- Inertia-contrast (a/b/c with numeric threshold). Reference steps as **"Step N from STEP REGISTRY."**
- Rollback viability per destructive step (fixed taxonomy).

Pre-seeded example (write your own at the same specificity):
> (a) Before Step 2 from STEP REGISTRY, the Commerce order fulfillment pipeline worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — the `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2 from STEP REGISTRY, `processing` is removed from the ENUM — existing `processing` orders are structurally invalid at dispatch.
> (c) Consequence: ~50,000 orders stranded at dispatch daily. No database error raised.
>
> Rollback: FULL DOWN MIGRATION.

**R1 COMMERCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write R2 until R1 COMMERCE GATE = OPEN.

---

#### R2 — FINANCE TRACE *(requires R1 COMMERCE GATE = OPEN)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Finance: monetary precision, ledger integrity, settlement accuracy. Apply the PARITY PHASE checklist in full — same checklist as R1. Do not scope DEFAULT checks to financial columns.

Pre-seeded example:
> (a) Before Step 3 from STEP REGISTRY, Finance settlement processing worked correctly because `payment_amount decimal(19,4)` — wire transfer totals up to $999,999,999,999.9999 processed without precision loss.
> (b) After Step 3 from STEP REGISTRY, `payment_amount` becomes `decimal(10,2)` — precision beyond two fractional places discarded.
> (c) Consequence: any wire transfer over $9,999,999.99 silently capped. Discrepancy surfaces only post-settlement.
>
> Rollback: BACKUP ONLY.

**R2 FINANCE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write R3 until R2 FINANCE GATE = OPEN.

---

#### R3 — OPERATIONS TRACE *(requires R2 FINANCE GATE = OPEN)*

For each affected step (reference as **"Step N from STEP REGISTRY"**):

Operations: constraint safety, idempotency, performance cliffs. Apply the PARITY PHASE checklist in full — same checklist as R1 and R2. Additionally:
- **Idempotency per step:** SAFE / UNSAFE — name the exact failure mode if UNSAFE.
- **Performance cliff:** does any step force a full-table rewrite, index rebuild, or row-scan type cast? Name the table, estimated row count, and specific risk (lock duration, I/O spike, replication lag).

**R3 OPERATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

**INTERROGATIVE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)** — set to OPEN when all three role traces are complete.

Do not write PHASE 4 until INTERROGATIVE GATE = OPEN.

---

### PHASE 4 — CANONICAL PHASE

*Primary obligation: produce the authoritative step-ordered execution artifact with all four manifest-derived constraint columns.*

*Entry prerequisite: INTERROGATIVE GATE = OPEN. Exit: CANONICAL GATE.*

**C-05 is satisfied here, not by any PHASE 3 section. PHASE 3 interrogates by domain role; this phase provides the mandatory chronological execution-ordered output. All step ordering below is authoritative.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

List every migration step in strict execution order. Single source of step numbers for all B-section references.

**MANIFEST COLUMN COMPLETENESS CHECK:** This table must carry one binary constraint-type column per MANIFEST PHASE registry row. Expected: NOT NULL Risk (Row 1), FK Violation (Row 2), UNIQUE Violation (Row 3), CHECK Violation (Row 4). Count = 4. Writing B1 with fewer than four constraint-type columns fails the manifest completeness check before the table is written.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

For each affected step, synthesize the domain impact. Reference as **"Step N from B1."**

Seed a NEW inertia-contrast example here — distinct from any PHASE 3 role section example. The Phase 4 example must name a different migration step, table, AND business consequence.

*(a) Before Step N from B1, [different process from PHASE 3 examples] worked because [different condition].*
*(b) After Step N from B1, [that condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different from all PHASE 3 examples].*

Pre-seeded example (write your own — different from R1/R2/R3 examples):
> (a) Before Step 5 from B1, the Commerce inventory reservation system worked correctly because `reserved_qty integer NOT NULL DEFAULT 0` guaranteed every SKU had a valid reservation count — bulk catalog imports relied on the DEFAULT 0.
> (b) After Step 5 from B1, `DEFAULT 0` is removed from `reserved_qty` — any INSERT without explicit `reserved_qty` fails the NOT NULL constraint.
> (c) Consequence: ~12,000 bulk SKU imports per day fail with a constraint error instead of completing silently. Operators see constraint errors rather than successful catalog additions.
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

Confirm: idempotency result per step, rollback taxonomy for every destructive step, zero-downtime verdict and blocking step if maintenance window required.

**VERIFY COMPLETION GATE B3→B4 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B4 until VERIFY COMPLETION GATE = OPEN.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY COMPLETION GATE = OPEN)*

Risk-tiered action list: `CRITICAL` / `HIGH` / `MEDIUM`. State zero-downtime verdict and blocking step.

**CANONICAL GATE (BINARY FIELD): ___ (OPEN / BLOCKED)** — set to OPEN when all B1 through B4 sections are complete.

---

### PHASE 5 — VERDICT PHASE

*Primary obligation: terminal assessment gated on canonical phase completion.*

*Entry prerequisite: CANONICAL GATE = OPEN.*

**RECOMMENDATIONS GATE B4→VERDICT (BINARY FIELD): ___ (OPEN / BLOCKED)**

**VERDICT** *(requires RECOMMENDATIONS GATE = OPEN)*

**VERDICT — BINARY FIELD: GOLDEN / NOT GOLDEN**

All essential criteria pass AND composite >= 80%?

---

## Criterion Coverage Summary (v9 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-31 Parse-Time Registry | Manifest rows with B1 Column Name field | Standard registry in Q1 REGISTRY PHASE | Registry with Business Condition Protected column | Manifest row count explicit | MANIFEST PHASE owns registry |
| C-32 Phase-B Column Completeness | Manifest-anchored column chaining, explicit audit instruction | Manifest column check in B1 header | Manifest row-to-column mapping in B1 header | Column count audit (expected = 4) in B1 header | CANONICAL PHASE manifest completeness check |
| C-33 Parity Enforcement Block | Standard block before Q2 Commerce | Phase A design contract before step registry | Standard block before domain roles | Role CONTRACT headers copy before each role section | PARITY PHASE (dedicated phase) owns enforcement block |
| C-28 All-Constraint Structured Fields | Per-type sub-sections using manifest row order | Per-type binary fields in each role section | Manifest row expansion sections | Per-type binary fields in role contracts | Per-type binary fields in INTERROGATIVE PHASE |
| C-29 Cross-Role Parity | Applied via parity block | Applied via phase A design contract | Applied via parity block | Applied via role contracts | Applied via parity enforcement block |
| C-30 Dual-Phase Inertia Seeding | Phase A + B2 distinct examples | Phase A + B2 distinct examples | Registry-sourced Phase A + different registry row in B2 | Phase A + B2 distinct examples | PHASE 3 + PHASE 4 B2 distinct examples |
| C-05 Phase-B Canonical Claim | Explicit in Phase B header | Explicit in Phase B header | Explicit in Phase B header | Explicit in Phase B header | Explicit in CANONICAL PHASE header |
| Gate Chain (C-21, C-24, C-26) | Full chain through B4→VERDICT | Full chain through B4→VERDICT | Full chain through B4→VERDICT | Full chain through B4→VERDICT | MANIFEST→PARITY→INTERROGATIVE→CANONICAL→VERDICT |
