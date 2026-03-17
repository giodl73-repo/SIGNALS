Written to `simulations/quest/variations/trace-migration-variations-R14-2026-03-14.md`.

---

**R14 Variation Summary**

| V | Axis | C-37 | C-38 | C-39 | Predicted |
|---|------|------|------|------|-----------|
| V-01 | Output format (single) — PROTOCOL COUNT MANIFEST | PASS | FAIL | FAIL | 235/245 |
| V-02 | Inertia framing (single) — COST LEDGER table | FAIL | PASS | FAIL | 235/245 |
| V-03 | Role sequence (single) — cross-role B2 chain, two domain roles | FAIL | FAIL | PASS | 235/245 |
| V-04 | Output format + Inertia framing | PASS | PASS | FAIL | 240/245 |
| V-05 | All three + Operations-first | PASS | PASS | PASS | 245/245 |

**Ablation design:**

- V-01/V-02/V-03 are clean single-axis isolations — each criterion is confirmed orthogonal to the other two before combining.
- V-03 uses Commerce-first Phase A (same as V-01/V-02) to confirm C-39 is a B2 content criterion, not a Phase A ordering criterion.
- V-04 confirms C-37 and C-38 are jointly achievable with a single-role B2 (C-39 FAIL) — the two table mechanisms place no obligation on cross-role B2 content.
- V-05 adds Operations-first role order to V-04 and requires B2 to name an Operations substrate failure with named Commerce AND Finance downstream consequences in a single chain.

The three new criteria are fully orthogonal — each tests a distinct structural property: manifest second surface (C-37), table row-countability (C-38), cross-role dependency evidence (C-39).
led prose. V-02 replaces STATUS QUO COST prose with a three-row COST LEDGER table (completeness machine-countable by row count) while no manifest is present.

**V-03** isolates C-39 with standard Commerce-first role order, confirming that C-39 depends on B2 content — whether two domain roles' consequences are explicitly named in a single cross-role chain — not on Phase A role ordering. A Commerce-first Phase A can still produce a C-39-passing B2 if B2 explicitly chains an Operations substrate failure to named Commerce AND Finance downstream consequences.

**V-04** confirms C-37 and C-38 are jointly achievable without C-39. B2 seeds a new inertia-contrast example naming a single domain role's consequence (distinct step from Phase A, passes C-30, fails C-39). Establishes that the two table-format mechanisms are additive and independent of B2 content.

**V-05** adds the cross-role B2 axis to V-04, switches to Operations-first role ordering so the infrastructure substrate is established in Q1 before Commerce and Finance reframe it, and requires B2 to name an Operations condition whose disruption produces named consequences for Commerce AND Finance simultaneously.

---

## V-01 — Axis: Output Format (C-37 only)

**Variation axis:** Output format — PROTOCOL COUNT MANIFEST added at Phase B entry. STATUS QUO COST is labeled prose (satisfies C-36, fails C-38). B2 seeds one domain role's consequence (satisfies C-30, fails C-39).
**Hypothesis:** C-37 PASS because the manifest pre-commits all six boundary names, gate names, and gate states at Phase B entry, creating a second verification surface independent of header scan. C-38 FAIL: the three-part prose structure satisfies C-36 but requires reading to confirm completeness — no row-count check is possible. C-39 FAIL: B2 names Commerce consequence only.
**Predicted score:** 235/245.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest for all downstream constraint analysis. BOUNDARY PROTOCOL sections mark every phase boundary as named structural artifacts: the count of BOUNDARY PROTOCOL section headers must equal the count of phase-to-phase transitions. A PROTOCOL COUNT MANIFEST at Phase B entry pre-commits the expected boundary count and gate states before B1 is written. A STATUS QUO COST section establishes the three-part inertia baseline before Q1. Follow the structure exactly.

---

### PARSE PHASE

*Entry: none. Exit: PARSE GATE (BINARY FIELD).*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order.

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

Each row is mandatory. The B1 Column Name field is pre-populated: Phase B's execution table carries exactly these four binary columns.

| Row | Constraint Type | Present | Affected Tables | Violation Possible | Migration Response | B1 Column Name |
|-----|-----------------|---------|-----------------|-------------------|--------------------|----------------|
| 1 | NOT NULL | YES / NO | | YES / NO / UNKNOWN | | NOT NULL Risk |
| 2 | FK | YES / NO | | YES / NO / UNKNOWN | | FK Violation |
| 3 | UNIQUE | YES / NO | | YES / NO / UNKNOWN | | UNIQUE Violation |
| 4 | CHECK | YES / NO | | YES / NO / UNKNOWN | | CHECK Violation |

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — PARSE -> PHASE A

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). Guards: Phase A — INTERROGATIVE.
- **ENTRY REFERENCE:** Phase A requires `PARSE GATE = OPEN` from PARSE PHASE above.

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Commerce, Finance, Operations). DO NOT SCOPE OR SHORTEN any item for any role. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window? Name any blocking step and why. *(ALL roles.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is a DEFAULT provided? Flag missing DEFAULTs. *(ALL new NOT NULL columns — not only financial columns.)*
3. **Constraint violation analysis** — fill all four binary fields (manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name the step and mechanism.
5. **Inertia-contrast example** — three-part: (a) prior working state, (b) how migration breaks it, (c) specific numeric consequence. Anchor to STATUS QUO COST baseline.
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — full-table rewrite, index rebuild, or row-scan cast? Name table, row count estimate, specific risk.
8. **Idempotency per step** — SAFE / UNSAFE. If UNSAFE, name exact failure mode.

**If any item is absent from any role section, the parity constraint is violated.**

---

### PHASE A — INTERROGATIVE *(requires PARSE GATE = OPEN)*

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### STATUS QUO COST *(Pre-Interrogation — complete before Q1)*

Establish the three-part inertia baseline BEFORE any per-entity or per-role analysis begins. All Q1/Q2/Q3 inertia-contrast examples must anchor back to this baseline.

**(a) CURRENT SCHEMA CONDITION:** [the specific schema element — table, column, type, constraint, or index — whose current state makes the relevant business process function correctly today]

**(b) DEPENDENT PROCESS:** [the specific business process that depends on condition (a) — name it precisely with volume or frequency data if available]

**(c) ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE):** [the cost, risk, or technical debt that accumulates if the migration is deferred or abandoned — name the rate, horizon, and metric. Example: "Each quarter of deferral adds ~12% to the backfill dataset; at current growth a 6-month deferral makes the migration 2x more expensive."]

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN.

---

#### Q1 — COMMERCE EXPERT *(requires STATUS QUO GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables. Anchor inertia-contrast example to STATUS QUO COST condition (a).

Pre-seeded example (write your own at equal specificity):
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid; the warehouse dispatch queue stops routing those orders.
> (c) ~50,000 orders per day silently stranded at dispatch. No error raised.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until DOMAIN GATE 1 = OPEN.

---

#### Q2 — FINANCE EXPERT *(requires DOMAIN GATE 1 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Finance scope: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables. Do not limit DEFAULT checks to financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` — wire totals up to $999,999,999,999.9999 without precision loss.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — precision beyond two decimal places discarded.
> (c) Any wire over $9,999,999.99 is silently capped. Discrepancy surfaces only post-settlement.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until DOMAIN GATE 2 = OPEN.

---

#### Q3 — OPERATIONS EXPERT *(requires DOMAIN GATE 2 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, schema migration tooling behavior, replication lag.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

All three DOMAIN GATEs must be OPEN before TRACE GATE can be OPEN.

---

### BOUNDARY PROTOCOL — PHASE A -> PHASE B

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards: Phase B — CANONICAL MIGRATION TRACE.
- **ENTRY REFERENCE:** Phase B requires `TRACE GATE = OPEN` from Phase A above.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section. This phase provides the mandatory chronological execution-ordered output.**

**PROTOCOL COUNT MANIFEST** *(pre-committed gate coverage — fill this table at Phase B entry before writing B1)*

This manifest pre-commits the expected count of BOUNDARY PROTOCOL sections. The count of filled rows must equal the count of `### BOUNDARY PROTOCOL` section headers in the complete output. A row present in this table but missing a corresponding section header is a cross-document inconsistency detectable at Phase B entry without reading any phase body interior.

| # | Boundary | Gate Name | Gate State (BINARY FIELD) | Status |
|---|----------|-----------|--------------------------|--------|
| 1 | PARSE -> PHASE A | PARSE GATE | OPEN / BLOCKED | [ ] present |
| 2 | PHASE A -> PHASE B | TRACE GATE | OPEN / BLOCKED | [ ] present |
| 3 | B1 -> B2 | EXECUTION GATE | OPEN / BLOCKED | [ ] present |
| 4 | B2 -> B3 | DOMAIN SYNTHESIS GATE | OPEN / BLOCKED | [ ] present |
| 5 | B3 -> B4 | VERIFY GATE | OPEN / BLOCKED | [ ] present |
| 6 | B4 -> VERDICT | RECOMMENDATIONS GATE | OPEN / BLOCKED | [ ] present |

**PROTOCOL MANIFEST GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B1 until all six rows are filled and all gate states are resolved.

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."** Do not use generic ordinals.

**MANIFEST COLUMN AUDIT:** This table carries exactly four binary constraint-type columns derived from CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order. Adding or omitting a column is a manifest violation.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 -> B2

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards: B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 requires `EXECUTION GATE = OPEN` from B1 above.

*(PROTOCOL COUNT MANIFEST row 3 — mark [ ] present after writing this block.)*

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

Synthesize domain impact across Commerce, Finance, and Operations. Then seed a NEW inertia-contrast example naming a **different step, table, and business consequence** than any Q1/Q2/Q3 example. Repeating a Phase A example does not satisfy this section.

*(a) Before Step N, [process different from Phase A examples] worked because [condition different from Phase A].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different step, table, and domain consequence from all Phase A examples].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 -> B3

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards: B3 — VERIFY.
- **ENTRY REFERENCE:** B3 requires `DOMAIN SYNTHESIS GATE = OPEN` from B2 above.

*(PROTOCOL COUNT MANIFEST row 4 — mark [ ] present after writing this block.)*

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

For each step from B1 with DATA LOSS = YES or NOT NULL RISK = YES: write one verification query confirming migration success. Name the table, column, and expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 -> B4

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards: B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 requires `VERIFY GATE = OPEN` from B3 above.

*(PROTOCOL COUNT MANIFEST row 5 — mark [ ] present after writing this block.)*

---

#### B4 — RECOMMENDATIONS *(requires VERIFY GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

List at most five ranked recommendations. For each: name the affected step, the specific risk it addresses, and the action to take before running the migration in production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 -> VERDICT

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards: VERDICT.
- **ENTRY REFERENCE:** VERDICT requires `RECOMMENDATIONS GATE = OPEN` from B4 above.

*(PROTOCOL COUNT MANIFEST row 6 — mark [ ] present after writing this block.)*

---

### VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*

*(PROTOCOL COUNT MANIFEST verification: confirm all six rows marked [ ] present before writing MIGRATION READINESS.)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

State the blocking factor if BLOCKED, or the required mitigations if RUN WITH MITIGATIONS.

---

---

## V-02 — Axis: Inertia Framing (C-38 only)

**Variation axis:** Inertia framing — STATUS QUO COST replaced with a three-row COST LEDGER table. No PROTOCOL COUNT MANIFEST. B2 seeds one domain role's consequence (satisfies C-30, fails C-39).
**Hypothesis:** C-38 PASS because COST LEDGER expresses the three-part baseline as a table with one row per part — completeness is verifiable by row count alone, without reading cell contents. C-37 FAIL: no manifest at Phase B entry (C-35 PASS by header scan, but no second surface). C-39 FAIL: B2 names Finance consequence only.
**Predicted score:** 235/245.

---

This prompt traces a database migration in two phases. The PARSE PHASE establishes the STEP REGISTRY and CONSTRAINT TYPE REGISTRY before analysis begins. BOUNDARY PROTOCOL sections mark each phase boundary as a named structural artifact: the number of such sections equals the number of phase-to-phase transitions. A STATUS QUO COST section expressed as a COST LEDGER table establishes the three-part inertia baseline before the first domain-role question — completeness is verifiable by row count.

---

### PARSE PHASE

*The parse phase registers all migration steps and constraint types before any per-step analysis occurs.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT — the source of step numbers for all downstream references)*

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — all four rows filled at parse time regardless of violation presence)*

| Row | Constraint Type | Present | Affected Tables | Violation Possible | Migration Response | B1 Column Name |
|-----|-----------------|---------|-----------------|-------------------|--------------------|----------------|
| 1 | NOT NULL | YES / NO | | YES / NO / UNKNOWN | | NOT NULL Risk |
| 2 | FK | YES / NO | | YES / NO / UNKNOWN | | FK Violation |
| 3 | UNIQUE | YES / NO | | YES / NO / UNKNOWN | | UNIQUE Violation |
| 4 | CHECK | YES / NO | | YES / NO / UNKNOWN | | CHECK Violation |

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — PARSE -> PHASE A

*This section marks the PARSE -> Phase A boundary as a named structural artifact.*

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). The PARSE GATE state governs entry into Phase A.
- **ENTRY REFERENCE:** Phase A draws on `PARSE GATE = OPEN` from PARSE PHASE as its entry condition.

---

### PARITY ENFORCEMENT BLOCK

*This block lists every required analytical item before any domain-role section is written.*

Every domain-role section (Commerce, Finance, Operations) addresses all eight items below. No item is scoped to a subset of roles or tables.

1. **Zero-downtime viability** — assessment of whether steps can run without a maintenance window. Any blocking step named with reason. Applies to all three domain roles.
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: whether a DEFAULT is provided. Missing DEFAULTs flagged as migration blockers. Applies to all new NOT NULL columns across all roles, not only financial columns.
3. **Constraint violation analysis** — four binary fields in manifest row order:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. A YES value names the step and the silent loss mechanism.
5. **Inertia-contrast example** — three-part: (a) working state before migration, (b) how migration breaks it, (c) numeric or named consequence. Example anchors to COST LEDGER row (a).
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — any step forcing full-table rewrite, index rebuild, or row-scan type cast, with table name, row count estimate, and specific risk type.
8. **Idempotency** — for each step: SAFE / UNSAFE, with exact failure mode for UNSAFE steps.

---

### PHASE A — INTERROGATIVE *(entry condition: PARSE GATE = OPEN)*

*Phase A organizes analytical work by domain lens and constraint type. C-05 is satisfied by Phase B alone.*

---

#### STATUS QUO COST *(Pre-Interrogation — COST LEDGER format — complete before Q1)*

*The three-part inertia baseline is established in COST LEDGER table format before Q1 begins. All Phase A domain-role sections and the Phase B domain synthesis section anchor their inertia-contrast examples to the row(s) of this table. Completeness is verifiable by row count: a table with fewer than three filled rows has a visible structural gap.*

**COST LEDGER**

| Row | Part | Value |
|-----|------|-------|
| **(a)** | **CURRENT SCHEMA CONDITION** | [the specific schema element — table, column, type, constraint, index — whose current state makes the affected business process function correctly today. Name precisely.] |
| **(b)** | **DEPENDENT PROCESS** | [the specific business process that depends on condition (a). Name it with volume or frequency data if available.] |
| **(c)** | **ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE)** | [the cost, risk, or technical debt that accumulates if migration is deferred. Name rate + horizon + metric.] |

*The STATUS QUO GATE records whether all three COST LEDGER rows are filled. Q1 draws on this table as its entry condition.*

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN and all three COST LEDGER rows are filled.

---

#### Q1 — COMMERCE EXPERT *(entry condition: STATUS QUO GATE = OPEN)*

*This section applies the complete PARITY ENFORCEMENT BLOCK checklist from a Commerce domain lens.*

> **Citation:** Step references take the form "Step N from STEP REGISTRY."

Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables. Inertia-contrast example anchors to COST LEDGER row (a).

Pre-seeded example:
> (a) Before Step 2, Commerce order fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed — orders in `processing` state become structurally invalid; dispatch queue stops routing.
> (c) ~50,000 orders per day silently stranded. No database error raised.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q2 — FINANCE EXPERT *(entry condition: DOMAIN GATE 1 = OPEN)*

*This section applies the complete PARITY ENFORCEMENT BLOCK checklist from a Finance domain lens.*

> **Citation:** Step references take the form "Step N from STEP REGISTRY."

Finance scope: monetary precision, ledger integrity, settlement accuracy. DEFAULT presence check applies to all new NOT NULL columns, not only financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` — daily settlement at wire-transfer scale ran without precision loss.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — fractional precision beyond two places discarded.
> (c) Wire transfers over $9,999,999.99 silently capped. Audit reports show truncated totals.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q3 — OPERATIONS EXPERT *(entry condition: DOMAIN GATE 2 = OPEN)*

*This section applies the complete PARITY ENFORCEMENT BLOCK checklist from an Operations domain lens.*

> **Citation:** Step references take the form "Step N from STEP REGISTRY."

Operations scope: deployment constraints, job queue dependencies, index maintenance windows, schema migration tooling behavior, replication lag. Performance cliff detection applies to all steps with large-table impact.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

*The TRACE GATE is OPEN when all three DOMAIN GATEs are OPEN.*

---

### BOUNDARY PROTOCOL — PHASE A -> PHASE B

*This section marks the Phase A -> Phase B boundary.*

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards Phase B — CANONICAL MIGRATION TRACE.
- **ENTRY REFERENCE:** Phase B draws on `TRACE GATE = OPEN` from Phase A.

---

### PHASE B — CANONICAL MIGRATION TRACE *(entry condition: TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section. This phase provides the authoritative chronological execution-ordered output.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **Citation:** B-section step references take the form "Step N from B1."

*The MANIFEST COLUMN AUDIT confirms this table carries exactly four binary constraint-type columns derived from CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order.*

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 -> B2

*This section marks the B1 -> B2 boundary.*

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 draws on `EXECUTION GATE = OPEN` from B1.

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — entry condition: EXECUTION GATE = OPEN)*

> **Citation:** Step references take the form "Step N from B1."

*Domain synthesis across Commerce, Finance, and Operations. This section seeds a NEW inertia-contrast example naming a different step, table, and consequence than any Q section example. The example names a single Finance consequence not covered in Q2 — anchoring to COST LEDGER row (a) from a Finance perspective distinct from the Q2 example.*

*(a) Before Step N, [a Finance process different from Q2's example] worked because [a schema condition not used in Q2's example].*
*(b) After Step N, [that condition no longer holds].*
*(c) Finance consequence: [specific numeric or named failure — different step, table, and consequence than all Phase A examples].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 -> B3

*This section marks the B2 -> B3 boundary.*

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards B3 — VERIFY.
- **ENTRY REFERENCE:** B3 draws on `DOMAIN SYNTHESIS GATE = OPEN` from B2.

---

#### B3 — VERIFY *(entry condition: DOMAIN SYNTHESIS GATE = OPEN)*

> **Citation:** Step references take the form "Step N from B1."

For each step in B1 with DATA LOSS = YES or NOT NULL RISK = YES: one verification query confirming migration success. Each query names the table, column, and expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 -> B4

*This section marks the B3 -> B4 boundary.*

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 draws on `VERIFY GATE = OPEN` from B3.

---

#### B4 — RECOMMENDATIONS *(entry condition: VERIFY GATE = OPEN)*

> **Citation:** Step references take the form "Step N from B1."

At most five ranked recommendations. Each names the affected step, the specific risk addressed, and the required action before production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 -> VERDICT

*This section marks the B4 -> VERDICT boundary.*

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards VERDICT.
- **ENTRY REFERENCE:** VERDICT draws on `RECOMMENDATIONS GATE = OPEN` from B4.

---

### VERDICT *(entry condition: RECOMMENDATIONS GATE = OPEN)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

---

---

## V-03 — Axis: Role Sequence / B2 Cross-Role Chain (C-39 only)

**Variation axis:** Role sequence — Commerce-first Phase A, B2 inertia example explicitly chains an Operations substrate failure to consequences in TWO DISTINCT DOMAIN ROLES (Commerce AND Finance). No PROTOCOL COUNT MANIFEST. STATUS QUO COST is labeled prose.
**Hypothesis:** C-39 PASS because B2 names a shared Operations infrastructure condition whose disruption produces direct, named consequences for both Commerce and Finance simultaneously — dependency evidence no single-role analysis can produce. C-37 FAIL: no manifest. C-38 FAIL: STATUS QUO COST is labeled prose, not a row-countable table.
**Predicted score:** 235/245.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest. BOUNDARY PROTOCOL sections mark every phase boundary as named structural artifacts (count of headers = count of transitions). A STATUS QUO COST section establishes the three-part inertia baseline before Q1. Phase B domain synthesis (B2) must contain a cross-role inertia chain: a shared Operations infrastructure condition whose disruption produces named consequences in AT LEAST TWO DISTINCT DOMAIN ROLES. Follow the structure exactly.

---

### PARSE PHASE

*Entry: none. Exit: PARSE GATE (BINARY FIELD).*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

| Row | Constraint Type | Present | Affected Tables | Violation Possible | Migration Response | B1 Column Name |
|-----|-----------------|---------|-----------------|-------------------|--------------------|----------------|
| 1 | NOT NULL | YES / NO | | YES / NO / UNKNOWN | | NOT NULL Risk |
| 2 | FK | YES / NO | | YES / NO / UNKNOWN | | FK Violation |
| 3 | UNIQUE | YES / NO | | YES / NO / UNKNOWN | | UNIQUE Violation |
| 4 | CHECK | YES / NO | | YES / NO / UNKNOWN | | CHECK Violation |

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — PARSE -> PHASE A

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). Guards: Phase A — INTERROGATIVE.
- **ENTRY REFERENCE:** Phase A requires `PARSE GATE = OPEN` from PARSE PHASE above.

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Commerce, Finance, Operations). DO NOT SCOPE OR SHORTEN any item. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — name blocking step and why. *(ALL roles.)*
2. **DEFAULT presence check** — flag missing DEFAULTs on any new NOT NULL column on any non-empty table. *(ALL new NOT NULL columns.)*
3. **Constraint violation analysis** — four binary fields (manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name step and mechanism.
5. **Inertia-contrast example** — three-part: (a) prior working state, (b) how migration breaks it, (c) numeric consequence. Anchor to STATUS QUO COST baseline.
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — table, row count estimate, specific risk type.
8. **Idempotency per step** — SAFE / UNSAFE. Name failure mode if UNSAFE.

**If any item is absent from any role section, the parity constraint is violated.**

---

### PHASE A — INTERROGATIVE *(requires PARSE GATE = OPEN)*

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### STATUS QUO COST *(Pre-Interrogation — complete before Q1)*

Establish the three-part inertia baseline BEFORE any per-entity or per-role analysis begins. All Q section inertia-contrast examples must anchor back to this baseline.

**(a) CURRENT SCHEMA CONDITION:** [the specific schema element whose current state makes the affected business process work today — name the table, column, type, and constraint]

**(b) DEPENDENT PROCESS:** [the specific business process that depends on the condition in (a) — name it with volume or frequency data if available]

**(c) ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE):** [the cost, risk, or technical debt that accumulates if migration is deferred — name the rate, horizon, and metric]

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN.

---

#### Q1 — COMMERCE EXPERT *(requires STATUS QUO GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades. Anchor inertia-contrast example to STATUS QUO COST condition (a).

Pre-seeded example:
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` removed — dispatch queue stops routing those orders.
> (c) ~50,000 orders/day silently stranded. No error raised.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until DOMAIN GATE 1 = OPEN.

---

#### Q2 — FINANCE EXPERT *(requires DOMAIN GATE 1 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Finance scope: monetary precision, ledger integrity, settlement accuracy. Do not limit DEFAULT checks to financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` — wire totals up to $999,999,999,999.9999 without loss.
> (b) After Step 3, becomes `decimal(10,2)` — precision beyond two decimal places discarded.
> (c) Wire over $9,999,999.99 silently capped.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until DOMAIN GATE 2 = OPEN.

---

#### Q3 — OPERATIONS EXPERT *(requires DOMAIN GATE 2 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, migration tooling behavior, replication lag.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

All three DOMAIN GATEs must be OPEN before TRACE GATE can be OPEN.

---

### BOUNDARY PROTOCOL — PHASE A -> PHASE B

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards: Phase B — CANONICAL MIGRATION TRACE.
- **ENTRY REFERENCE:** Phase B requires `TRACE GATE = OPEN` from Phase A above.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."** Do not use generic ordinals.

**MANIFEST COLUMN AUDIT:** This table carries exactly four binary constraint-type columns in manifest row order.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 -> B2

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards: B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 requires `EXECUTION GATE = OPEN` from B1 above.

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

Synthesize domain impact across Commerce, Finance, and Operations. Then seed a NEW inertia-contrast example that satisfies BOTH requirements:

1. **Different from all Phase A examples** — names a different step, table, and business consequence than Q1, Q2, and Q3.
2. **Cross-role inertia chain** — names a shared Operations infrastructure condition (schema state, migration step, or system dependency) whose disruption produces direct, named consequences in AT LEAST TWO DISTINCT DOMAIN ROLES. Removing one role's consequence from this analysis would leave the other incomplete — the Operations substrate must hold for both downstream role consequences to follow.

Cross-role chain structure:
*(a) Before Step N, the Operations infrastructure condition [name the specific shared schema element or migration-tooling dependency] kept BOTH the [Commerce process] AND the [Finance process] functioning because [shared dependency: one structural guarantee, two downstream processes].*
*(b) After Step N, [the Operations condition is broken — name the migration step] — BOTH [Commerce] and [Finance] lose their structural guarantee simultaneously.*
*(c) Commerce consequence: [specific named failure with numeric threshold — different step and consequence from Q1]. Finance consequence: [specific named failure with numeric threshold — different step and consequence from Q2]. Shared substrate: [the Operations condition whose removal causes both consequences].*

A B2 example that names only one domain role's consequence PASSES C-30 and FAILS C-39.

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 -> B3

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards: B3 — VERIFY.
- **ENTRY REFERENCE:** B3 requires `DOMAIN SYNTHESIS GATE = OPEN` from B2 above.

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

For each step with DATA LOSS = YES or NOT NULL RISK = YES: one verification query. Name table, column, expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 -> B4

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards: B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 requires `VERIFY GATE = OPEN` from B3 above.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

At most five ranked recommendations. For each: step, risk addressed, required action before production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 -> VERDICT

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards: VERDICT.
- **ENTRY REFERENCE:** VERDICT requires `RECOMMENDATIONS GATE = OPEN` from B4 above.

---

### VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

---

---

## V-04 — Axes: Output Format + Inertia Framing (C-37 + C-38)

**Variation axes:** Output format (PROTOCOL COUNT MANIFEST at Phase B entry) + Inertia framing (COST LEDGER table for STATUS QUO COST). Commerce-first role order. B2 seeds one domain role's consequence (satisfies C-30, fails C-39).
**Hypothesis:** C-37 PASS (manifest at Phase B entry, second verification surface) + C-38 PASS (COST LEDGER table, row-count completeness check). C-39 FAIL: B2 example names Operations consequence only — one domain role, different step from Phase A. Confirms C-37 and C-38 are independent of B2 cross-role content.
**Predicted score:** 240/245.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest. BOUNDARY PROTOCOL sections mark every phase boundary as named structural artifacts (count of headers = count of transitions). A PROTOCOL COUNT MANIFEST at Phase B entry pre-commits all boundary names and gate states before B1 is written. A STATUS QUO COST section expressed as a COST LEDGER table (three rows, one per part) establishes the inertia baseline before Q1 — completeness is verifiable by row count. Follow the structure exactly.

---

### PARSE PHASE

*Entry: none. Exit: PARSE GATE (BINARY FIELD).*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

| Row | Constraint Type | Present | Affected Tables | Violation Possible | Migration Response | B1 Column Name |
|-----|-----------------|---------|-----------------|-------------------|--------------------|----------------|
| 1 | NOT NULL | YES / NO | | YES / NO / UNKNOWN | | NOT NULL Risk |
| 2 | FK | YES / NO | | YES / NO / UNKNOWN | | FK Violation |
| 3 | UNIQUE | YES / NO | | YES / NO / UNKNOWN | | UNIQUE Violation |
| 4 | CHECK | YES / NO | | YES / NO / UNKNOWN | | CHECK Violation |

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — PARSE -> PHASE A

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). Guards: Phase A — INTERROGATIVE.
- **ENTRY REFERENCE:** Phase A requires `PARSE GATE = OPEN` from PARSE PHASE above.

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Commerce, Finance, Operations). DO NOT SCOPE OR SHORTEN any item:**

1. **Zero-downtime viability** — name blocking step and why. *(ALL roles.)*
2. **DEFAULT presence check** — flag missing DEFAULTs on any new NOT NULL column. *(ALL new NOT NULL columns.)*
3. **Constraint violation analysis** — four binary fields (manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name step and mechanism.
5. **Inertia-contrast example** — three-part: prior working state / migration breaks it / numeric consequence. Anchor to COST LEDGER row (a).
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — table, row count, specific risk type.
8. **Idempotency per step** — SAFE / UNSAFE. Name failure mode if UNSAFE.

---

### PHASE A — INTERROGATIVE *(requires PARSE GATE = OPEN)*

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone.**

---

#### STATUS QUO COST *(Pre-Interrogation — COST LEDGER format — complete before Q1)*

The three-part inertia baseline is established in COST LEDGER table format before any per-entity or per-role analysis begins. Completeness is verifiable by row count: a table with fewer than three filled rows has a visible structural gap without reading cell contents.

**COST LEDGER**

| Row | Part | Value |
|-----|------|-------|
| **(a)** | **CURRENT SCHEMA CONDITION** | [the specific schema element — table, column, type, constraint, or index — whose current state makes the affected business process work today. Name precisely.] |
| **(b)** | **DEPENDENT PROCESS** | [the specific business process that depends on condition (a). Name it with volume or frequency data if available.] |
| **(c)** | **ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE)** | [cost, risk, or technical debt that accumulates if migration is deferred. Name rate + horizon + metric.] |

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN and all three COST LEDGER rows are filled.

---

#### Q1 — COMMERCE EXPERT *(requires STATUS QUO GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades. Anchor inertia-contrast example to COST LEDGER row (a).

Pre-seeded example:
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders/day.
> (b) After Step 2, `processing` removed — dispatch queue stops routing those orders.
> (c) ~50,000 orders/day silently stranded.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until DOMAIN GATE 1 = OPEN.

---

#### Q2 — FINANCE EXPERT *(requires DOMAIN GATE 1 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Finance scope: monetary precision, ledger integrity, settlement accuracy. DEFAULT checks apply to ALL new NOT NULL columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` — no precision loss up to $999,999,999,999.9999.
> (b) After Step 3, becomes `decimal(10,2)` — precision beyond two places discarded.
> (c) Wire over $9,999,999.99 silently capped.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until DOMAIN GATE 2 = OPEN.

---

#### Q3 — OPERATIONS EXPERT *(requires DOMAIN GATE 2 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, migration tooling behavior, replication lag.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

All three DOMAIN GATEs must be OPEN before TRACE GATE can be OPEN.

---

### BOUNDARY PROTOCOL — PHASE A -> PHASE B

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards: Phase B — CANONICAL MIGRATION TRACE.
- **ENTRY REFERENCE:** Phase B requires `TRACE GATE = OPEN` from Phase A above.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section.**

**PROTOCOL COUNT MANIFEST** *(pre-committed gate coverage — fill this table at Phase B entry before writing B1)*

This manifest pre-commits the expected count of BOUNDARY PROTOCOL sections. Row count must equal `### BOUNDARY PROTOCOL` header count in the complete output. A discrepancy between the two counts is a structural failure signal detectable at Phase B entry without reading phase body interiors.

| # | Boundary | Gate Name | Gate State (BINARY FIELD) | Status |
|---|----------|-----------|--------------------------|--------|
| 1 | PARSE -> PHASE A | PARSE GATE | OPEN / BLOCKED | [ ] present |
| 2 | PHASE A -> PHASE B | TRACE GATE | OPEN / BLOCKED | [ ] present |
| 3 | B1 -> B2 | EXECUTION GATE | OPEN / BLOCKED | [ ] present |
| 4 | B2 -> B3 | DOMAIN SYNTHESIS GATE | OPEN / BLOCKED | [ ] present |
| 5 | B3 -> B4 | VERIFY GATE | OPEN / BLOCKED | [ ] present |
| 6 | B4 -> VERDICT | RECOMMENDATIONS GATE | OPEN / BLOCKED | [ ] present |

**PROTOCOL MANIFEST GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B1 until all six rows are filled and all gate states are resolved.

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."** Do not use generic ordinals.

**MANIFEST COLUMN AUDIT:** Exactly four binary constraint-type columns in manifest row order.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 -> B2

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards: B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 requires `EXECUTION GATE = OPEN` from B1 above.

*(PROTOCOL COUNT MANIFEST row 3 — mark [ ] present after writing this block.)*

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

Synthesize domain impact. Seed a NEW inertia-contrast example naming a **different step, table, and business consequence** than any Q section example. The example names a single domain role's consequence — the test for this section is that the step and outcome are distinct from Phase A, not that multiple roles are chained.

*(a) Before Step N, [an Operations / Commerce / Finance process different from all Q examples] worked because [condition not used in any Q section].*
*(b) After Step N, [condition no longer holds].*
*(c) [Domain role] consequence: [specific numeric or named failure — different step, table, and role consequence than all Phase A examples].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 -> B3

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards: B3 — VERIFY.
- **ENTRY REFERENCE:** B3 requires `DOMAIN SYNTHESIS GATE = OPEN` from B2 above.

*(PROTOCOL COUNT MANIFEST row 4 — mark [ ] present after writing this block.)*

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

For each step with DATA LOSS = YES or NOT NULL RISK = YES: one verification query. Name table, column, expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 -> B4

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards: B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 requires `VERIFY GATE = OPEN` from B3 above.

*(PROTOCOL COUNT MANIFEST row 5 — mark [ ] present after writing this block.)*

---

#### B4 — RECOMMENDATIONS *(requires VERIFY GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

At most five ranked recommendations. For each: step, risk addressed, required action before production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 -> VERDICT

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards: VERDICT.
- **ENTRY REFERENCE:** VERDICT requires `RECOMMENDATIONS GATE = OPEN` from B4 above.

*(PROTOCOL COUNT MANIFEST row 6 — mark [ ] present after writing this block.)*

---

### VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*

*(PROTOCOL COUNT MANIFEST verification: confirm all six rows marked [ ] present before writing MIGRATION READINESS.)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

---

---

## V-05 — Axes: Output Format + Inertia Framing + Role Sequence (C-37 + C-38 + C-39)

**Variation axes:** V-04 backbone + cross-role B2 inertia chain + Operations-first role order. COST LEDGER is infrastructure-oriented. B2 explicitly names an Operations infrastructure condition whose disruption produces named consequences for Commerce AND Finance simultaneously.
**Hypothesis:** C-37 PASS (PROTOCOL COUNT MANIFEST at Phase B entry, dual verification surface). C-38 PASS (COST LEDGER table, row-count completeness). C-39 PASS (B2 cross-role chain: Operations substrate -> Commerce + Finance consequences in a single chain naming both downstream roles). Operations-first in Phase A ensures the infrastructure substrate is established in Q1 before Commerce and Finance encounter it in Q2 and Q3, making the B2 dependency chain traceable to a Q1-grounded condition.
**Predicted score:** 245/245.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest for all constraint analysis. BOUNDARY PROTOCOL sections mark every phase boundary as named structural artifacts; their count is pre-committed in a PROTOCOL COUNT MANIFEST at Phase B entry. A STATUS QUO COST section expressed as a three-row COST LEDGER table establishes the inertia baseline before Q1 — completeness verifiable by row count. Operations analysis runs before Commerce and Finance, establishing the infrastructure substrate before domain-commerce framing begins. Phase B domain synthesis requires a cross-role inertia chain linking an Operations infrastructure condition to named consequences in at least two distinct domain roles. Follow the structure exactly.

---

### PARSE PHASE

*Entry: none. Exit: PARSE GATE (BINARY FIELD).*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — fill all four rows before proceeding)*

| Row | Constraint Type | Present | Affected Tables | Violation Possible | Migration Response | B1 Column Name |
|-----|-----------------|---------|-----------------|-------------------|--------------------|----------------|
| 1 | NOT NULL | YES / NO | | YES / NO / UNKNOWN | | NOT NULL Risk |
| 2 | FK | YES / NO | | YES / NO / UNKNOWN | | FK Violation |
| 3 | UNIQUE | YES / NO | | YES / NO / UNKNOWN | | UNIQUE Violation |
| 4 | CHECK | YES / NO | | YES / NO / UNKNOWN | | CHECK Violation |

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — PARSE -> PHASE A

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). Guards: Phase A — INTERROGATIVE.
- **ENTRY REFERENCE:** Phase A requires `PARSE GATE = OPEN` from PARSE PHASE above.

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Operations, Commerce, Finance). DO NOT SCOPE OR SHORTEN any item. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — name blocking step and why. *(ALL roles — not scoped to one domain.)*
2. **DEFAULT presence check** — flag missing DEFAULTs on any new NOT NULL column on any non-empty table. *(ALL new NOT NULL columns — not only financial or commerce columns.)*
3. **Constraint violation analysis** — four binary fields (manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name step and mechanism.
5. **Inertia-contrast example** — three-part: prior working state / migration breaks it / numeric consequence. Anchor to COST LEDGER row (a).
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — table, row count estimate, specific risk type.
8. **Idempotency per step** — SAFE / UNSAFE. Name failure mode if UNSAFE.

**If any item is absent from any role section, the parity constraint is violated.**

---

### PHASE A — INTERROGATIVE *(requires PARSE GATE = OPEN)*

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### STATUS QUO COST *(Pre-Interrogation — COST LEDGER format — complete before Q1)*

The three-part inertia baseline is established in COST LEDGER table format before any per-entity or per-role analysis begins. The COST LEDGER is infrastructure-oriented: ground the prior working state in the operational substrate (migration tooling, deployment sequencing, schema-version dependencies) that Commerce and Finance processes depend on. Completeness is verifiable by row count: a table with fewer than three filled rows has a visible structural gap without reading cell contents.

**COST LEDGER**

| Row | Part | Value |
|-----|------|-------|
| **(a)** | **CURRENT SCHEMA CONDITION** | [the specific schema element — table, column, type, constraint, or index — whose current state makes the affected infrastructure or operational process work today. If Commerce or Finance processes depend downstream on this operational condition, name the dependency chain.] |
| **(b)** | **DEPENDENT PROCESS** | [the specific operational process that depends on condition (a), with volume or frequency data. Then name the Commerce and Finance processes that depend on this operational substrate — making the cross-role dependency explicit at baseline.] |
| **(c)** | **ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE)** | [infrastructure cost, operational risk, or technical debt that accumulates if migration is deferred. Name rate + horizon + metric. Express as a compounding operational liability if GROWING.] |

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN and all three COST LEDGER rows are filled.

---

#### Q1 — OPERATIONS EXPERT *(requires STATUS QUO GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, migration tooling behavior, replication lag, rollback feasibility at the infrastructure layer. Anchor inertia-contrast example to COST LEDGER row (a) — the infrastructure substrate.

Pre-seeded example (write your own at equal specificity):
> (a) Before Step 1, migration pipeline integrity was maintained because `schema_version` FK on the job queue table enforced version continuity — migration jobs only ran against the schema version they were compiled for.
> (b) After Step 1, FK dropped — version-drift execution possible without structural error.
> (c) At 200 migration jobs/day, one version-drift execution affects ~8 jobs before detection; each produces partial writes requiring manual reconciliation.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until DOMAIN GATE 1 = OPEN.

---

#### Q2 — COMMERCE EXPERT *(requires DOMAIN GATE 1 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades. Anchor inertia-contrast example to COST LEDGER row (a); if Commerce depends on the Q1 operational substrate, name the dependency chain explicitly.

Pre-seeded example:
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders/day.
> (b) After Step 2, `processing` removed — dispatch queue stops routing those orders.
> (c) ~50,000 orders/day silently stranded.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until DOMAIN GATE 2 = OPEN.

---

#### Q3 — FINANCE EXPERT *(requires DOMAIN GATE 2 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Finance scope: monetary precision, ledger integrity, settlement accuracy. DEFAULT checks apply to ALL new NOT NULL columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` — no precision loss up to $999,999,999,999.9999.
> (b) After Step 3, becomes `decimal(10,2)` — precision beyond two places discarded.
> (c) Wire over $9,999,999.99 silently capped.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

All three DOMAIN GATEs must be OPEN before TRACE GATE can be OPEN.

---

### BOUNDARY PROTOCOL — PHASE A -> PHASE B

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards: Phase B — CANONICAL MIGRATION TRACE.
- **ENTRY REFERENCE:** Phase B requires `TRACE GATE = OPEN` from Phase A above.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section.**

**PROTOCOL COUNT MANIFEST** *(pre-committed gate coverage — fill this table at Phase B entry before writing B1)*

This manifest pre-commits the expected count of BOUNDARY PROTOCOL sections. The count of filled rows must equal the count of `### BOUNDARY PROTOCOL` section headers in the complete output. A discrepancy between the header scan count and the manifest row count is a structural failure signal independently detectable from either surface: a boundary present in headers but absent from the manifest, or vice versa, is a cross-document inconsistency detectable here without reading any phase body interior.

| # | Boundary | Gate Name | Gate State (BINARY FIELD) | Status |
|---|----------|-----------|--------------------------|--------|
| 1 | PARSE -> PHASE A | PARSE GATE | OPEN / BLOCKED | [ ] present |
| 2 | PHASE A -> PHASE B | TRACE GATE | OPEN / BLOCKED | [ ] present |
| 3 | B1 -> B2 | EXECUTION GATE | OPEN / BLOCKED | [ ] present |
| 4 | B2 -> B3 | DOMAIN SYNTHESIS GATE | OPEN / BLOCKED | [ ] present |
| 5 | B3 -> B4 | VERIFY GATE | OPEN / BLOCKED | [ ] present |
| 6 | B4 -> VERDICT | RECOMMENDATIONS GATE | OPEN / BLOCKED | [ ] present |

**PROTOCOL MANIFEST GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B1 until all six rows are filled and all gate states are resolved.

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."** Do not use generic ordinals.

**MANIFEST COLUMN AUDIT:** Exactly four binary constraint-type columns in manifest row order.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 -> B2

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards: B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 requires `EXECUTION GATE = OPEN` from B1 above.

*(PROTOCOL COUNT MANIFEST row 3 — mark [ ] present after writing this block.)*

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

Synthesize domain impact across Operations, Commerce, and Finance. Then seed a NEW inertia-contrast example that satisfies BOTH requirements:

1. **Different from all Phase A examples** — names a different step, table, and business consequence than Q1, Q2, and Q3.
2. **Cross-role inertia chain** — names a shared Operations infrastructure condition (schema state, migration step, or system dependency) whose disruption produces direct, named consequences in AT LEAST TWO DISTINCT DOMAIN ROLES. The Operations substrate condition must hold for both downstream role consequences to follow — demonstrating the substrate failure once demonstrates both failures simultaneously. A B2 example naming only one domain role's consequence PASSES C-30 and FAILS this requirement.

Cross-role chain structure:
*(a) Before Step N, the Operations infrastructure condition [from COST LEDGER row (a) / Q1 — name the specific shared schema element] kept BOTH the [Commerce process] AND the [Finance process] functioning because [shared dependency: one structural guarantee supporting two downstream processes — name both explicitly].*
*(b) After Step N, [the Operations condition is broken — name the specific migration step] — BOTH [Commerce] and [Finance] lose their structural guarantee simultaneously.*
*(c) Commerce consequence: [specific named failure with numeric threshold — different step and domain consequence from Q2]. Finance consequence: [specific named failure with numeric threshold — different step and domain consequence from Q3]. Shared substrate: [name the single Operations condition whose removal causes both — removing either role's consequence from this analysis would leave the other incomplete].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 -> B3

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards: B3 — VERIFY.
- **ENTRY REFERENCE:** B3 requires `DOMAIN SYNTHESIS GATE = OPEN` from B2 above.

*(PROTOCOL COUNT MANIFEST row 4 — mark [ ] present after writing this block.)*

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

For each step with DATA LOSS = YES or NOT NULL RISK = YES: one verification query. Name table, column, expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 -> B4

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards: B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 requires `VERIFY GATE = OPEN` from B3 above.

*(PROTOCOL COUNT MANIFEST row 5 — mark [ ] present after writing this block.)*

---

#### B4 — RECOMMENDATIONS *(requires VERIFY GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

At most five ranked recommendations. For each: step, risk addressed, required action before production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 -> VERDICT

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards: VERDICT.
- **ENTRY REFERENCE:** VERDICT requires `RECOMMENDATIONS GATE = OPEN` from B4 above.

*(PROTOCOL COUNT MANIFEST row 6 — mark [ ] present after writing this block.)*

---

### VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*

*(PROTOCOL COUNT MANIFEST verification: confirm all six rows marked [ ] present before writing MIGRATION READINESS.)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

State the blocking factor if BLOCKED, or the required mitigations if RUN WITH MITIGATIONS.

---

---

## Predicted Outcomes

| V | Score | / 245 | % | Golden (>=196) | C-37 | C-38 | C-39 | Key distinguishing mechanism |
|---|-------|-------|---|----------------|------|------|------|------------------------------|
| V-01 | 235 | 235/245 | 96.0% | YES | PASS | FAIL | FAIL | PROTOCOL COUNT MANIFEST present; STATUS QUO COST prose (C-38 fails: reading required, no row count); B2 single-role |
| V-02 | 235 | 235/245 | 96.0% | YES | FAIL | PASS | FAIL | COST LEDGER table (row-count completeness); no manifest at Phase B entry; B2 single-role |
| V-03 | 235 | 235/245 | 96.0% | YES | FAIL | FAIL | PASS | B2 cross-role chain names Commerce + Finance from shared Operations substrate; prose SQC; no manifest |
| V-04 | 240 | 240/245 | 98.0% | YES | PASS | PASS | FAIL | PROTOCOL COUNT MANIFEST + COST LEDGER both present; B2 single-role confirms C-37/C-38 independent of C-39 |
| V-05 | 245 | 245/245 | 100% | YES | PASS | PASS | PASS | All three: manifest + COST LEDGER + Ops-first + cross-role B2 chain |

---

## Key Evaluator Distinctions (R14)

**C-37 ablation (V-01 vs V-02/V-03):** V-01 PASSES C-37 via PROTOCOL COUNT MANIFEST at Phase B entry; V-02 and V-03 FAIL because no manifest is present. C-35 remains satisfied by BOUNDARY PROTOCOL headers in all five variations (six headers = six transitions), but the second verification surface does not exist in V-02/V-03. A discrepancy between header count and manifest count cannot occur in V-02/V-03 because the manifest does not exist to generate a discrepancy.

**C-38 ablation (V-02 vs V-01/V-03):** V-02 PASSES C-38 via COST LEDGER table — a reviewer counts rows to verify three-part completeness without reading cell contents. V-01 and V-03 FAIL because STATUS QUO COST uses labeled (a)/(b)/(c) prose: all three parts may be present, but confirming this requires reading the prose. C-36 PASSES in all five variations (named pre-Q1 STATUS QUO COST section exists in all); C-38 adds the machine-countability requirement satisfied only by V-02/V-04/V-05.

**C-39 ablation (V-03 vs V-01/V-02):** V-03 PASSES C-39 because B2 names a single Operations substrate failure that produces consequences for both Commerce AND Finance in a single chain — removing either role's consequence would leave the other incomplete. V-01 and V-02 FAIL because their B2 instructions require only that the step and consequence differ from Phase A; no second domain role is required. V-04 also FAILS C-39: its B2 instruction explicitly notes that one role's consequence is sufficient for C-30 compliance.

**C-39 independence from Phase A role order:** V-03 uses Commerce-first Phase A and still achieves C-39 by requiring B2 to name two role consequences from an Operations substrate. C-39 is a B2 content criterion, not a Phase A ordering criterion. V-05 uses Operations-first to make the substrate dependency more naturally derivable from Q1, but C-39 would pass in either ordering if B2 content names two domain roles.

**C-37 + C-38 independence from C-39 (V-04):** V-04 PASSES both C-37 and C-38 with a single-role B2 example. This confirms neither the PROTOCOL COUNT MANIFEST mechanism nor the COST LEDGER table format creates any obligation on B2 content. The three criteria are fully orthogonal: each tests a distinct structural property (manifest surface, table completability, cross-role dependency).
