Written to `simulations/quest/variations/trace-migration-variations-R13-2026-03-14.md`.

---

# trace-migration — Round 13 Variations (Rubric v11)

## Overview

Rubric: v11 · 36 criteria · 230 pts · Golden 184 (80%).
New criteria: **C-35** (Boundary Protocol Named-Artifact Countability) and **C-36** (Pre-Interrogation Status Quo Cost Section), 5 pts each.

Baseline: R12 V-04 passes all C-01–C-34 at 220 pts. Every variation holds that baseline; only C-35 and C-36 are open.

---

## Variation Summary

| V | Axis | C-35 | C-36 | Predicted |
|---|------|------|------|-----------|
| **V-01** | Lifecycle emphasis (single) — BOUNDARY PROTOCOL promoted to named section headers | PASS | FAIL | 225/230 |
| **V-02** | Inertia framing (single) — STATUS QUO COST promoted to pre-Q1 named section with gate | FAIL | PASS | 225/230 |
| **V-03** | Phrasing register (single) — both mechanisms active, declarative rather than imperative register | PASS | PASS | 230/230 |
| **V-04** | Lifecycle + Inertia combined — Operations-first, cross-role inertia chain in B2 | PASS | PASS | 230/230 |
| **V-05** | Lifecycle + Inertia + Output format — PROTOCOL COUNT MANIFEST table + COST LEDGER table | PASS (dual-surface) | PASS (columnar) | 230/230 + new signals |

---

## Design Logic

**V-01 vs V-02** are clean ablations: one isolates C-35, one isolates C-36. Together they confirm the criteria are orthogonal — V-01 adds named `### BOUNDARY PROTOCOL` section headers (count-scannable without reading prose) but keeps STATUS QUO COST embedded in Q1; V-02 adds a named `### STATUS QUO COST` section with its own STATUS QUO GATE before Q1 but keeps BOUNDARY PROTOCOL as inline code fences.

**V-03** confirms both mechanisms hold when the phrasing register switches from imperative ("DO NOT advance until...") to declarative ("this section establishes... / the boundary below marks..."). The structural criteria test artifact presence, not instruction word-form.

**V-04** combines both axes on the R12 V-05 backbone (Operations-first, infrastructure-oriented STATUS QUO COST, cross-role inertia chain in B2). The COST LEDGER orientation — grounding the inertia baseline in the infrastructure substrate before Commerce reframes it — generates a richer three-part anchor for all three domain-role sections.

**V-05** adds the output format axis: a **PROTOCOL COUNT MANIFEST** table at Phase B entry pre-commits the expected count and names of all BOUNDARY PROTOCOL sections, making C-35 verifiable by manifest comparison (not only by header scan). The **COST LEDGER** table replaces STATUS QUO COST prose with a three-column structure, making C-36's three-part requirement machine-countable (a missing column is a visible table gap, not a prose omission). The PROTOCOL COUNT MANIFEST is the primary new excellence signal — it creates a second, independent verification surface for C-35 without requiring the reader to scan all section headers.
equirement structurally enforced.
- **V-05 rationale:** V-04 + PROTOCOL COUNT MANIFEST (output format axis): a named table at Phase B entry pre-commits the expected count of BOUNDARY PROTOCOL blocks and their resolved gate states. This makes C-35 verification a two-surface test — header scan count AND manifest count — creating structural redundancy. COST LEDGER replaces STATUS QUO COST prose with a three-column table, making the three-part structure machine-countable.

---

## V-01 — Axis: Lifecycle Emphasis (C-35 only)

**Variation axis:** Lifecycle emphasis — BOUNDARY PROTOCOL promoted from inline annotation to named section header at every phase boundary.
**Hypothesis:** C-35 PASS because BOUNDARY PROTOCOL section headers are scannable without reading phase interiors (N headers = N boundaries). C-36 FAIL because STATUS QUO COST remains embedded inside Q1 as instruction text rather than as a pre-Q1 named section.
**Predicted score:** 225/230 (C-35 PASS +5, C-36 FAIL).

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest for all downstream constraint analysis. BOUNDARY PROTOCOL sections mark every phase boundary as named structural artifacts: the count of BOUNDARY PROTOCOL section headers must equal the count of phase-to-phase transitions. Follow the structure exactly.

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

### BOUNDARY PROTOCOL — PARSE → PHASE A

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). Guards: Phase A — INTERROGATIVE.
- **ENTRY REFERENCE:** Phase A requires `PARSE GATE = OPEN` from PARSE PHASE above.

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Commerce, Finance, Operations). DO NOT SCOPE OR SHORTEN any item for any role. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window? Name any blocking step and why. *(ALL roles — not scoped to one domain.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is a DEFAULT provided? Flag missing DEFAULTs. *(ALL new NOT NULL columns — not only financial columns.)*
3. **Constraint violation analysis** — fill all four binary fields (manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name the step and mechanism.
5. **Inertia-contrast example** — three-part structure: (a) prior working state, (b) how migration breaks it, (c) specific numeric consequence. *(See STATUS QUO COST baseline in Q1 — anchor to it.)*
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — does any step force full-table rewrite, index rebuild, or row-scan cast? Name table, row count estimate, specific risk.
8. **Idempotency per step** — SAFE / UNSAFE. If UNSAFE, name exact failure mode.

**If any item is absent from any role section, the parity constraint is violated.**

---

### PHASE A — INTERROGATIVE *(requires PARSE GATE = OPEN)*

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### Q1 — COMMERCE EXPERT

> **CITATION ANCHOR:** All step references in this section use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Before per-step analysis, establish the inertia baseline for Commerce: (a) name the current schema condition that makes the Commerce process work today, (b) name the specific Commerce process that depends on it, (c) state the accumulation trajectory if migration is deferred (rate + horizon + metric). Then apply all eight PARITY ENFORCEMENT BLOCK items to Commerce: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables.

Pre-seeded example (write your own at equal specificity):
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — any order in `processing` state becomes structurally invalid; the warehouse dispatch queue stops routing those orders.
> (c) Consequence: ~50,000 orders per day silently stranded at dispatch. No error raised; failure surfaces only via missing dispatch events.
> Rollback: FULL DOWN MIGRATION — ENUM restore is reversible.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until DOMAIN GATE 1 = OPEN.

---

#### Q2 — FINANCE EXPERT

> **CITATION ANCHOR:** All step references in this section use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Finance scope: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables. Do not limit DEFAULT checks to financial columns — apply to ALL new NOT NULL columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` supported wire totals up to $999,999,999,999.9999 without truncation.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — precision beyond two decimal places is discarded.
> (c) Consequence: any wire over $9,999,999.99 is silently capped. Discrepancy surfaces only post-settlement.
> Rollback: BACKUP ONLY — precision data is gone once the column is narrowed.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until DOMAIN GATE 2 = OPEN.

---

#### Q3 — OPERATIONS EXPERT

> **CITATION ANCHOR:** All step references in this section use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, schema migration tooling behavior, replication lag. Include performance cliff detection for every step with large table impact.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

All three DOMAIN GATEs must be OPEN before TRACE GATE can be OPEN.

---

### BOUNDARY PROTOCOL — PHASE A → PHASE B

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards: Phase B — CANONICAL MIGRATION TRACE.
- **ENTRY REFERENCE:** Phase B requires `TRACE GATE = OPEN` from Phase A above.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section. This phase provides the mandatory chronological execution-ordered output.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."** Do not use generic ordinals.

**MANIFEST COLUMN AUDIT:** This table carries exactly four binary constraint-type columns derived from CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order. Adding or omitting a constraint-type column is a manifest violation.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 → B2

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards: B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 requires `EXECUTION GATE = OPEN` from B1 above.

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

Synthesize domain impact across Commerce, Finance, and Operations. Then seed a NEW inertia-contrast example that names a **different step, table, and business consequence** than any Q1/Q2/Q3 example. Repeating a Phase A example does not satisfy this section.

*(a) Before Step N, [process different from Phase A examples] worked because [condition different from Phase A].*
*(b) After Step N, [condition no longer holds] because [migration change].*
*(c) Consequence: [specific numeric or named failure — different step, table, consequence from Phase A].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 → B3

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards: B3 — VERIFY.
- **ENTRY REFERENCE:** B3 requires `DOMAIN SYNTHESIS GATE = OPEN` from B2 above.

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

For each step from B1 with DATA LOSS = YES or NOT NULL RISK = YES: write one verification query or check that would confirm the migration succeeded without data loss. Name the table, column, and expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 → B4

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards: B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 requires `VERIFY GATE = OPEN` from B3 above.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."** Do not use generic ordinals.

List at most five ranked recommendations. For each: name the affected step, the specific risk it addresses, and the action to take before running the migration in production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 → VERDICT

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards: VERDICT.
- **ENTRY REFERENCE:** VERDICT requires `RECOMMENDATIONS GATE = OPEN` from B4 above.

---

### VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

State the blocking factor if BLOCKED, or the required mitigations if RUN WITH MITIGATIONS.

---

---

## V-02 — Axis: Inertia Framing (C-36 only)

**Variation axis:** Inertia framing — STATUS QUO COST promoted from Q1-embedded instruction to named pre-Q1 section with its own gate.
**Hypothesis:** C-36 PASS because the named STATUS QUO COST section precedes all analytical content in Phase A and carries the three-part baseline as a structural entry precondition. C-35 FAIL because BOUNDARY PROTOCOL is implemented as inline code fences rather than named section headers — C-34 PASS (bilateral EXIT BLOCK + ENTRY REFERENCE present) but C-35 FAIL (gate compliance requires reading prose, not scanning headers).
**Predicted score:** 225/230 (C-36 PASS +5, C-35 FAIL).

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest for all downstream constraint analysis. Before any per-entity or per-role analysis begins, a STATUS QUO COST section establishes the three-part inertia baseline: (a) current schema condition, (b) dependent business process, (c) accumulation trajectory. Follow the structure exactly.

---

### PARSE PHASE

*Entry: none. Exit: PARSE GATE (BINARY FIELD).*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT)*

Number every migration step in strict execution order.

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

```
EXIT BLOCK (BINARY FIELD): PARSE GATE = ___
Downstream: Phase A. Do not advance to Phase A until PARSE GATE = OPEN.
```

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section. DO NOT SCOPE OR SHORTEN any item. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window? Name blocking step and why. *(ALL roles.)*
2. **DEFAULT presence check** — for every new NOT NULL column on non-empty table: is DEFAULT provided? Flag missing DEFAULTs. *(ALL new NOT NULL columns.)*
3. **Constraint violation analysis** — fill all four binary fields (manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name step and mechanism.
5. **Inertia-contrast example** — three-part: (a) prior working state, (b) how migration breaks it, (c) numeric consequence. Anchor back to STATUS QUO COST baseline.
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — full-table rewrite, index rebuild, or row-scan cast? Name table, row count, specific risk.
8. **Idempotency per step** — SAFE / UNSAFE. If UNSAFE, name failure mode.

---

### PHASE A — INTERROGATIVE

```
ENTRY REFERENCE: Phase A requires PARSE GATE = OPEN (BINARY FIELD) from PARSE PHASE above.
```

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone.**

---

#### STATUS QUO COST *(Pre-Interrogation — complete before Q1)*

Establish the three-part inertia baseline BEFORE any per-entity or per-role analysis begins. All Q1/Q2/Q3 inertia-contrast examples must anchor back to this baseline.

**(a) CURRENT SCHEMA CONDITION:** [the specific schema condition that makes the affected business process work today — name the table, column, type, and constraint]

**(b) DEPENDENT PROCESS:** [the specific business process that depends on that condition — name it precisely with volume or frequency data if available]

**(c) ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE):** [the cost, risk, or technical debt that accumulates if the migration is deferred or abandoned — name the rate, horizon, and metric. Example: "Each quarter of deferral adds ~12% to the backfill dataset as new orders arrive without the constraint; at current growth a 6-month deferral makes the migration 2× more expensive."]

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN.

---

#### Q1 — COMMERCE EXPERT *(requires STATUS QUO GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables. Anchor inertia-contrast example back to STATUS QUO COST condition (a).

Pre-seeded example:
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` removed — any order in `processing` state is structurally invalid; dispatch queue stops routing.
> (c) ~50,000 orders/day silently stranded. No error raised.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q2 — FINANCE EXPERT

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Finance scope: monetary precision, ledger integrity, settlement accuracy. Do not limit DEFAULT checks to financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` — wire totals up to $999,999,999,999.9999 without precision loss.
> (b) After Step 3, becomes `decimal(10,2)` — precision beyond two places discarded.
> (c) Any wire over $9,999,999.99 is silently capped.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q3 — OPERATIONS EXPERT

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, replication lag.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

```
EXIT BLOCK (BINARY FIELD): TRACE GATE = ___
Downstream: Phase B. Do not advance to Phase B until TRACE GATE = OPEN.
```

---

### PHASE B — CANONICAL MIGRATION TRACE

```
ENTRY REFERENCE: Phase B requires TRACE GATE = OPEN (BINARY FIELD) from Phase A above.
```

**C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."**

**MANIFEST COLUMN AUDIT:** Table carries exactly four binary constraint-type columns in manifest row order.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

```
EXIT BLOCK (BINARY FIELD): EXECUTION GATE = ___
Downstream: B2 DOMAIN SYNTHESIS.
```

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

```
ENTRY REFERENCE: B2 requires EXECUTION GATE = OPEN (BINARY FIELD).
```

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

Synthesize domain impact. Seed a NEW inertia-contrast example naming a **different step, table, and consequence** than any Phase A example — and naming a different aspect of the STATUS QUO COST baseline than Q1/Q2/Q3 used.

*(a) Before Step N, [different process] worked because [different condition from STATUS QUO COST baseline].*
*(b) After Step N, [condition broken].*
*(c) Consequence: [specific numeric or named failure].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

```
EXIT BLOCK (BINARY FIELD): DOMAIN SYNTHESIS GATE = ___
Downstream: B3 VERIFY.
```

---

#### B3 — VERIFY

```
ENTRY REFERENCE: B3 requires DOMAIN SYNTHESIS GATE = OPEN (BINARY FIELD).
```

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

For each step with DATA LOSS = YES or NOT NULL RISK = YES: write one verification query confirming the migration succeeded. Name table, column, expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

```
EXIT BLOCK (BINARY FIELD): VERIFY GATE = ___
Downstream: B4 RECOMMENDATIONS.
```

---

#### B4 — RECOMMENDATIONS

```
ENTRY REFERENCE: B4 requires VERIFY GATE = OPEN (BINARY FIELD).
```

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

At most five ranked recommendations. For each: name the affected step, the specific risk addressed, and the action to take before running in production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

```
EXIT BLOCK (BINARY FIELD): RECOMMENDATIONS GATE = ___
Downstream: VERDICT.
```

---

### VERDICT

```
ENTRY REFERENCE: VERDICT requires RECOMMENDATIONS GATE = OPEN (BINARY FIELD).
```

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

---

---

## V-03 — Axis: Phrasing Register (Declarative, Both C-35 and C-36)

**Variation axis:** Phrasing register — formal declarative rather than imperative. Both C-35 and C-36 mechanisms are active (named BOUNDARY PROTOCOL section headers + named pre-Q1 STATUS QUO COST section with gate) but all instructions are written as descriptive declarations ("this section establishes...," "the boundary below marks...") rather than imperatives ("DO NOT advance until...," "fill all four rows before proceeding"). Confirms structural criteria depend on named artifact presence, not instruction word-form.
**Hypothesis:** C-35 PASS and C-36 PASS regardless of register because the criteria test whether named sections exist and can be located by header scan — not whether the instructions use imperative phrasing. Role order: Commerce Q1, Finance Q2, Operations Q3 (standard order, different from V-04/V-05 which use Operations-first).
**Predicted score:** 230/230.

---

This prompt traces a database migration in two phases. The PARSE PHASE establishes the STEP REGISTRY and CONSTRAINT TYPE REGISTRY before analysis begins. BOUNDARY PROTOCOL sections mark each phase boundary as a named structural artifact: the number of such sections equals the number of phase-to-phase transitions. A STATUS QUO COST section establishes the three-part inertia baseline before the first domain-role question.

---

### PARSE PHASE

*The parse phase registers all migration steps and constraint types before any per-step analysis occurs.*

**STEP REGISTRY** *(AUTHORITATIVE ARTIFACT — the source of step numbers for all downstream references)*

Migration steps are listed here in strict execution order. Each row carries the exact type names, constraint definitions, and default values — not paraphrases.

| Step | Table | Operation | Before (exact type/constraint/default) | After (exact type/constraint/default) |
|------|-------|-----------|----------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY** *(BINDING MANIFEST — this table is the authoritative source for which constraint types receive dedicated analysis slots downstream)*

All four rows are filled at parse time, regardless of whether the migration contains a violation of each type. The B1 Column Name column establishes the exact column label that will appear in the Phase B canonical table.

| Row | Constraint Type | Present | Affected Tables | Violation Possible | Migration Response | B1 Column Name |
|-----|-----------------|---------|-----------------|-------------------|--------------------|----------------|
| 1 | NOT NULL | YES / NO | | YES / NO / UNKNOWN | | NOT NULL Risk |
| 2 | FK | YES / NO | | YES / NO / UNKNOWN | | FK Violation |
| 3 | UNIQUE | YES / NO | | YES / NO / UNKNOWN | | UNIQUE Violation |
| 4 | CHECK | YES / NO | | YES / NO / UNKNOWN | | CHECK Violation |

The PARSE GATE records whether the step registry and constraint type registry are complete.

**PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — PARSE → PHASE A

*This section marks the boundary between the PARSE PHASE and Phase A. The boundary is present as a named section header so that the count of BOUNDARY PROTOCOL sections is verifiable by scanning headers alone.*

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). The PARSE GATE state established above governs entry into Phase A.
- **ENTRY REFERENCE:** Phase A draws on `PARSE GATE = OPEN` from PARSE PHASE as its entry condition.

---

### PARITY ENFORCEMENT BLOCK

*This block lists every required analytical item once, before any domain-role section is written. Its purpose is to make cross-role analysis gaps structurally detectable as deviations from this list.*

Every domain-role section (Commerce, Finance, Operations) addresses all eight items below. No item is scoped to a subset of roles or tables.

1. **Zero-downtime viability** — assessment of whether steps can run without a maintenance window using expand/contract or online DDL. Any blocking step is named with the reason. This assessment applies to all three domain roles.
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: whether a DEFAULT is provided. Missing DEFAULTs on non-empty tables are flagged as migration blockers. This check applies to all new NOT NULL columns across all three domain roles, not only financial columns.
3. **Constraint violation analysis** — four binary fields in manifest row order:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. A YES value names the step and the silent loss mechanism.
5. **Inertia-contrast example** — three-part structure: (a) the working state before the migration, (b) how the migration breaks that state, (c) a numeric or named business consequence. The example anchors to the STATUS QUO COST baseline.
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — identification of any step that forces a full-table rewrite, index rebuild, or row-scan type cast, with table name, row count estimate, and specific risk type.
8. **Idempotency** — for each step: SAFE / UNSAFE, with the exact failure mode named for UNSAFE steps.

---

### PHASE A — INTERROGATIVE *(entry condition: PARSE GATE = OPEN)*

*Phase A organizes analytical work by domain lens and constraint type. It does not provide chronological step ordering — that responsibility belongs to Phase B alone. C-05 is satisfied by Phase B, not by any section of Phase A.*

---

#### STATUS QUO COST *(Pre-Interrogation — this section precedes all per-entity and per-role analysis)*

*This section establishes the three-part inertia baseline before Q1 begins. All Phase A domain-role sections and the Phase B domain synthesis section anchor their inertia-contrast examples to the baseline established here.*

**(a) CURRENT SCHEMA CONDITION:** [the specific schema element — table, column, type, constraint, index — whose current state makes the relevant business process function correctly today]

**(b) DEPENDENT PROCESS:** [the specific business process that currently works because of the condition in (a), with volume or frequency data if available]

**(c) ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE):** [the cost, risk, or technical debt that accumulates over time if the migration is deferred or abandoned — expressed as a rate, horizon, and named metric]

*The STATUS QUO GATE records whether the baseline is complete. Q1 draws on this baseline as its entry condition.*

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q1 — COMMERCE EXPERT *(entry condition: STATUS QUO GATE = OPEN)*

*This section applies the complete PARITY ENFORCEMENT BLOCK checklist from a Commerce domain lens.*

> **Citation:** Step references in this section take the form "Step N from STEP REGISTRY."

Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables. The inertia-contrast example anchors to the STATUS QUO COST condition (a) as its prior-working-state anchor.

Pre-seeded example:
> (a) Before Step 2, Commerce order fulfillment worked correctly because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` state gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed from the ENUM — orders in `processing` state become structurally invalid; the warehouse dispatch queue stops routing them.
> (c) ~50,000 orders per day are silently stranded at dispatch. No database error is raised.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q2 — FINANCE EXPERT *(entry condition: DOMAIN GATE 1 = OPEN)*

*This section applies the complete PARITY ENFORCEMENT BLOCK checklist from a Finance domain lens.*

> **Citation:** Step references in this section take the form "Step N from STEP REGISTRY."

Finance scope: monetary precision, ledger integrity, settlement accuracy, FK cascades through payment and invoice tables. The DEFAULT presence check applies to all new NOT NULL columns, not only financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement processing worked because `payment_amount decimal(19,4)` — daily settlement batches at wire-transfer scale ran without precision loss.
> (b) After Step 3, `payment_amount` becomes `decimal(10,2)` — fractional precision beyond two places is discarded.
> (c) Wire transfers over $9,999,999.99 are silently capped. Finance audit reports show truncated totals.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q3 — OPERATIONS EXPERT *(entry condition: DOMAIN GATE 2 = OPEN)*

*This section applies the complete PARITY ENFORCEMENT BLOCK checklist from an Operations domain lens.*

> **Citation:** Step references in this section take the form "Step N from STEP REGISTRY."

Operations scope: deployment constraints, job queue dependencies, index maintenance windows, schema migration tooling behavior, replication lag. Performance cliff detection applies to all steps with large-table impact.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

*The TRACE GATE is OPEN when all three DOMAIN GATEs are OPEN. It serves as the exit condition for Phase A and the entry condition for Phase B.*

---

### BOUNDARY PROTOCOL — PHASE A → PHASE B

*This section marks the boundary between Phase A and Phase B.*

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). The TRACE GATE state established in Q3 governs entry into Phase B.
- **ENTRY REFERENCE:** Phase B draws on `TRACE GATE = OPEN` from Phase A as its entry condition.

---

### PHASE B — CANONICAL MIGRATION TRACE *(entry condition: TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section. This phase provides the authoritative chronological execution-ordered output.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **Citation:** B-section step references take the form "Step N from B1."

*The MANIFEST COLUMN AUDIT confirms that this table carries exactly four binary constraint-type columns derived from CONSTRAINT TYPE REGISTRY manifest rows, in manifest row order. Constraint types present in the migration that lack a dedicated column here constitute a manifest violation.*

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 → B2

*This section marks the boundary between B1 and B2.*

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 draws on `EXECUTION GATE = OPEN` from B1 as its entry condition.

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — entry condition: EXECUTION GATE = OPEN)*

> **Citation:** Step references take the form "Step N from B1."

*Domain synthesis across Commerce, Finance, and Operations. This section seeds a NEW inertia-contrast example naming a different step, table, and consequence than any Q1/Q2/Q3 example.*

*(a) Before Step N, [a different process from Phase A] worked because [a different schema condition from Phase A — one not used in any Q section's example].*
*(b) After Step N, [that condition no longer holds].*
*(c) Consequence: [specific numeric or named failure — a different step, table, and domain consequence than all Phase A examples].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 → B3

*This section marks the boundary between B2 and B3.*

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards B3 — VERIFY.
- **ENTRY REFERENCE:** B3 draws on `DOMAIN SYNTHESIS GATE = OPEN` from B2.

---

#### B3 — VERIFY *(entry condition: DOMAIN SYNTHESIS GATE = OPEN)*

> **Citation:** Step references take the form "Step N from B1."

For each step in B1 with DATA LOSS = YES or NOT NULL RISK = YES: one verification query confirming migration success. Each query names the table, column, and expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 → B4

*This section marks the boundary between B3 and B4.*

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 draws on `VERIFY GATE = OPEN` from B3.

---

#### B4 — RECOMMENDATIONS *(entry condition: VERIFY GATE = OPEN)*

> **Citation:** Step references take the form "Step N from B1."

At most five ranked recommendations. Each names the affected step, the specific risk addressed, and the required action before production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 → VERDICT

*This section marks the boundary between B4 and VERDICT.*

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards VERDICT.
- **ENTRY REFERENCE:** VERDICT draws on `RECOMMENDATIONS GATE = OPEN` from B4.

---

### VERDICT *(entry condition: RECOMMENDATIONS GATE = OPEN)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

---

---

## V-04 — Axes: Lifecycle Emphasis + Inertia Framing

**Variation axes:** Lifecycle emphasis (V-01 BOUNDARY PROTOCOL named section headers) + Inertia framing (V-02 STATUS QUO COST pre-Q1 named section with gate). Operations-first role sequence (Q1 = Operations, Q2 = Commerce, Q3 = Finance). The STATUS QUO COST section is infrastructure-oriented, exposing the inertia baseline to an Operations lens before Commerce reframes it.
**Hypothesis:** C-35 PASS (named BOUNDARY PROTOCOL section headers) and C-36 PASS (named STATUS QUO COST section before Q1 with STATUS QUO GATE). Operations-first means the three-part inertia baseline is grounded in infrastructure risk (schema rigidity → deployment constraint → commerce dependency) before per-entity commerce analysis begins.
**Predicted score:** 230/230.

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest. BOUNDARY PROTOCOL sections mark every phase boundary as named structural artifacts (count of headers = count of phase-to-phase transitions). A STATUS QUO COST section establishes the three-part inertia baseline before Q1. Operations analysis runs before Commerce and Finance, so the infrastructure-grounded cost of inaction is established before domain-commerce framing begins. Follow the structure exactly.

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

### BOUNDARY PROTOCOL — PARSE → PHASE A

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). Guards: Phase A — INTERROGATIVE.
- **ENTRY REFERENCE:** Phase A requires `PARSE GATE = OPEN` from PARSE PHASE above.

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Operations, Commerce, Finance). DO NOT SCOPE OR SHORTEN any item. Apply to ALL roles, ALL tables, ALL columns:**

1. **Zero-downtime viability** — can steps run without a maintenance window? Name blocking step and why. *(ALL roles.)*
2. **DEFAULT presence check** — for every new NOT NULL column on any non-empty table: is DEFAULT provided? Flag missing DEFAULTs. *(ALL new NOT NULL columns — not only financial or commerce columns.)*
3. **Constraint violation analysis** — four binary fields (manifest row order):
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name step and mechanism.
5. **Inertia-contrast example** — three-part: (a) prior working state, (b) how migration breaks it, (c) numeric consequence. Anchor back to STATUS QUO COST baseline.
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — full-table rewrite, index rebuild, row-scan cast? Name table, row count, specific risk.
8. **Idempotency per step** — SAFE / UNSAFE. Name failure mode if UNSAFE.

**If any item is absent from any role section, the parity constraint is violated.**

---

### PHASE A — INTERROGATIVE *(requires PARSE GATE = OPEN)*

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### STATUS QUO COST *(Pre-Interrogation — complete before Q1)*

Establish the three-part inertia baseline BEFORE any per-entity or per-role analysis begins. The STATUS QUO COST baseline is infrastructure-oriented: ground the prior working state in the operational substrate (migration tooling, deployment sequencing, schema-version dependencies) that Commerce and Finance processes depend on. All Q1/Q2/Q3 inertia-contrast examples must anchor back to this baseline.

**(a) CURRENT SCHEMA CONDITION:** [the specific schema element whose current state makes the affected infrastructure or operational process work today — name the table, column, type, constraint, or index]

**(b) DEPENDENT PROCESS:** [the specific operational process that depends on the condition in (a) — name it with volume or frequency. If Commerce or Finance processes downstream depend on this operational process, name the dependency chain: operations condition → commerce/finance dependency]

**(c) ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE):** [the infrastructure cost, operational risk, or technical debt that accumulates if the migration is deferred — name rate, horizon, and metric. Example: "Each sprint of deferral increases the schema drift between staging and production by one table version; at current release cadence, a 3-month deferral creates a 6-version gap that requires a coordinated multi-table catch-up migration rather than a single-table patch."]

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN.

---

#### Q1 — OPERATIONS EXPERT *(requires STATUS QUO GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, schema migration tooling behavior, replication lag, migration rollback feasibility at the infrastructure layer. Anchor inertia-contrast example to STATUS QUO COST condition (a) — the infrastructure substrate.

Pre-seeded example (write your own at equal specificity):
> (a) Before Step 1, the migration pipeline worked because `schema_version` FK constraint on the job queue table enforced version continuity — migration jobs only ran against the schema version they were compiled against, preventing version-drift execution.
> (b) After Step 1, the FK is dropped — the job queue can now execute migration jobs against any schema version; version-drift execution becomes possible without a structural error.
> (c) A job compiled against v3 executes against a v5 schema: column assumptions fail silently; partial writes go undetected until audit. At 200 migration jobs/day, one version-drift failure affects ~8 jobs before detection.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q2 until DOMAIN GATE 1 = OPEN.

---

#### Q2 — COMMERCE EXPERT *(requires DOMAIN GATE 1 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades through order and shipment tables. Anchor inertia-contrast example to STATUS QUO COST condition (a) — if Commerce depends on the infrastructure substrate from Q1, name the dependency.

Pre-seeded example:
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` — `processing` gated warehouse dispatch for ~50,000 active orders per day.
> (b) After Step 2, `processing` is removed — orders in `processing` state become structurally invalid; dispatch queue stops routing.
> (c) ~50,000 orders/day silently stranded. No database error.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write Q3 until DOMAIN GATE 2 = OPEN.

---

#### Q3 — FINANCE EXPERT *(requires DOMAIN GATE 2 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Finance scope: monetary precision, ledger integrity, settlement accuracy. Do not limit DEFAULT checks to financial columns.

Pre-seeded example:
> (a) Before Step 3, Finance settlement worked because `payment_amount decimal(19,4)` — wire totals up to $999,999,999,999.9999 without loss.
> (b) After Step 3, becomes `decimal(10,2)` — precision beyond two decimal places discarded.
> (c) Wire over $9,999,999.99 silently capped.
> Rollback: BACKUP ONLY.

**DOMAIN GATE 3 (BINARY FIELD): ___ (OPEN / BLOCKED)**

**TRACE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

All three DOMAIN GATEs must be OPEN before TRACE GATE can be OPEN.

---

### BOUNDARY PROTOCOL — PHASE A → PHASE B

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards: Phase B — CANONICAL MIGRATION TRACE.
- **ENTRY REFERENCE:** Phase B requires `TRACE GATE = OPEN` from Phase A above.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section.**

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."**

**MANIFEST COLUMN AUDIT:** This table carries exactly four binary constraint-type columns in manifest row order.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 → B2

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards: B2 — DOMAIN SYNTHESIS.
- **ENTRY REFERENCE:** B2 requires `EXECUTION GATE = OPEN` from B1 above.

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

Synthesize domain impact across Operations, Commerce, and Finance. Then seed a NEW inertia-contrast example that (1) names a **different step, table, and consequence** than any Q1/Q2/Q3 example, AND (2) forms a **cross-role inertia chain**: name an Operations-grounded cause from Q1/STATUS QUO COST expressed as a Commerce or Finance consequence — a cause-consequence pair that neither role section alone could produce.

Cross-role inertia chain structure:
*(a) Before Step N, the Operations infrastructure condition [from STATUS QUO COST / Q1 — name the specific operational substrate] kept the [Commerce / Finance] process working because [dependency chain].*
*(b) After Step N, the Operations condition is broken — the [Commerce / Finance] downstream process loses its structural guarantee.*
*(c) Consequence: [named Commerce or Finance failure with numeric or business-process specificity — different step, table, and domain from all Q section examples].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 → B3

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards: B3 — VERIFY.
- **ENTRY REFERENCE:** B3 requires `DOMAIN SYNTHESIS GATE = OPEN` from B2 above.

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

For each step with DATA LOSS = YES or NOT NULL RISK = YES: one verification query confirming migration success. Name table, column, expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 → B4

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards: B4 — RECOMMENDATIONS.
- **ENTRY REFERENCE:** B4 requires `VERIFY GATE = OPEN` from B3 above.

---

#### B4 — RECOMMENDATIONS *(requires VERIFY GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

At most five ranked recommendations. For each: name the affected step, the risk addressed, and the required action before production.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 → VERDICT

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards: VERDICT.
- **ENTRY REFERENCE:** VERDICT requires `RECOMMENDATIONS GATE = OPEN` from B4 above.

---

### VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

---

---

## V-05 — Axes: Lifecycle Emphasis + Inertia Framing + Output Format

**Variation axes:** V-04 backbone + output format axis: (1) **PROTOCOL COUNT MANIFEST** — a named table at Phase B entry pre-committing the expected count of BOUNDARY PROTOCOL sections and their gate names, making C-35 verifiable at Phase B entry by manifest count in addition to header scan; (2) **COST LEDGER** — STATUS QUO COST expressed as a three-column table (CONDITION / PROCESS / TRAJECTORY) rather than labeled prose, making the three-part structure machine-countable.
**Hypothesis:** C-35 PASS via two independent surfaces: header scan count AND PROTOCOL COUNT MANIFEST pre-commitment. C-36 PASS: COST LEDGER table format makes the three-part structure of STATUS QUO COST structurally verifiable by column count. The PROTOCOL COUNT MANIFEST creates a new excellence signal: a reader at Phase B entry can verify gate coverage by comparing the manifest row count to the BOUNDARY PROTOCOL header count without reading any phase interiors. Operations-first role sequence. Cross-role inertia chain required in B2 (same as V-04).
**Predicted score:** 230/230 + new signal (PROTOCOL COUNT MANIFEST as dual-surface C-35 verification artifact).

---

You are a database migration expert. You trace migrations using a structured two-phase format. The CONSTRAINT TYPE REGISTRY — established at parse time — is the binding manifest for all constraint analysis. BOUNDARY PROTOCOL sections mark every phase boundary as named structural artifacts; their count is pre-committed in a PROTOCOL COUNT MANIFEST at Phase B entry. A STATUS QUO COST section expressed as a three-column COST LEDGER table establishes the inertia baseline before Q1. Operations analysis runs before Commerce and Finance. Follow the structure exactly.

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

### BOUNDARY PROTOCOL — PARSE → PHASE A

- **EXIT BLOCK (BINARY FIELD):** PARSE GATE = ___ (OPEN / BLOCKED). Guards: Phase A.
- **ENTRY REFERENCE:** Phase A requires `PARSE GATE = OPEN` from PARSE PHASE.

---

### PARITY ENFORCEMENT BLOCK

**The following complete checklist MUST appear in every domain-role section (Operations, Commerce, Finance). DO NOT SCOPE OR SHORTEN any item:**

1. **Zero-downtime viability** — name any blocking step and why. *(ALL roles.)*
2. **DEFAULT presence check** — flag missing DEFAULTs on any new NOT NULL column on any non-empty table. *(ALL new NOT NULL columns.)*
3. **Constraint violation analysis** — four binary fields:
   - NOT NULL RISK (BINARY FIELD): YES / NO / PARTIAL
   - FK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - UNIQUE VIOLATION (BINARY FIELD): YES / NO / PARTIAL
   - CHECK VIOLATION (BINARY FIELD): YES / NO / PARTIAL
4. **Data loss path** — DATA LOSS PATH (BINARY FIELD): YES / NO. If YES, name step and mechanism.
5. **Inertia-contrast example** — three-part: prior working state / migration breaks it / numeric consequence. Anchor to COST LEDGER row.
6. **Rollback viability** — per destructive step: FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE.
7. **Performance cliff** — table, row count estimate, specific risk type.
8. **Idempotency** — SAFE / UNSAFE per step. Failure mode if UNSAFE.

---

### PHASE A — INTERROGATIVE *(requires PARSE GATE = OPEN)*

**Phase B is the authoritative chronological output. C-05 is satisfied by Phase B alone.**

---

#### STATUS QUO COST *(Pre-Interrogation — COST LEDGER format — complete before Q1)*

The three-part inertia baseline is established in COST LEDGER table format before any per-entity or per-role analysis begins. All Q section inertia-contrast examples anchor to the row(s) of this table. The Operations Q1 lens is applied to the CONDITION column first.

**COST LEDGER**

| Column | Value |
|--------|-------|
| **(a) CURRENT SCHEMA CONDITION** | [the specific schema element — table, column, type, constraint, index — whose current state makes the affected process work today. Name it precisely.] |
| **(b) DEPENDENT PROCESS** | [the specific process that depends on condition (a). Infrastructure-first: name the operational substrate, then the commerce/finance dependency chain it supports. Include volume or frequency data.] |
| **(c) ACCUMULATION TRAJECTORY (BINARY FIELD — GROWING / STABLE)** | [cost, risk, or technical debt that accumulates if migration is deferred. Name rate + horizon + metric. Express as a compounding operational liability if GROWING.] |

**STATUS QUO GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not begin Q1 until STATUS QUO GATE = OPEN and all three COST LEDGER cells are filled.

---

#### Q1 — OPERATIONS EXPERT *(requires STATUS QUO GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Operations scope: deployment constraints, job queue dependencies, index maintenance windows, migration tooling behavior, replication lag. Anchor inertia-contrast example to COST LEDGER row (a) — the infrastructure substrate.

Pre-seeded example:
> (a) Before Step 1, migration pipeline integrity was maintained because `schema_version` FK on the job queue enforced version continuity — migration jobs only ran against the schema version they were compiled for.
> (b) After Step 1, FK dropped — version-drift execution possible without structural error.
> (c) At 200 migration jobs/day, one version-drift execution affects ~8 jobs before detection; each produces partial writes that require manual reconciliation.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 1 (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

#### Q2 — COMMERCE EXPERT *(requires DOMAIN GATE 1 = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from STEP REGISTRY."** Do not use generic ordinals.

Apply all eight PARITY ENFORCEMENT BLOCK items. Commerce scope: order state integrity, catalog commitments, inventory reservations, FK cascades. Anchor inertia-contrast example to COST LEDGER row (a); if Commerce depends on the Q1 operational substrate, name the dependency.

Pre-seeded example:
> (a) Before Step 2, Commerce fulfillment worked because `order_status ENUM('pending','processing','shipped','delivered')` gated warehouse dispatch for ~50,000 active orders/day.
> (b) After Step 2, `processing` removed — dispatch queue stops routing those orders.
> (c) ~50,000 orders/day silently stranded.
> Rollback: FULL DOWN MIGRATION.

**DOMAIN GATE 2 (BINARY FIELD): ___ (OPEN / BLOCKED)**

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

---

### BOUNDARY PROTOCOL — PHASE A → PHASE B

- **EXIT BLOCK (BINARY FIELD):** TRACE GATE = ___ (OPEN / BLOCKED). Guards: Phase B.
- **ENTRY REFERENCE:** Phase B requires `TRACE GATE = OPEN` from Phase A.

---

### PHASE B — CANONICAL MIGRATION TRACE *(requires TRACE GATE = OPEN)*

**C-05 is satisfied by Phase B alone, not by any Phase A section.**

**PROTOCOL COUNT MANIFEST** *(pre-committed gate coverage — fill this table at Phase B entry before writing B1)*

This manifest pre-commits the expected count of BOUNDARY PROTOCOL sections. The count of filled rows below must equal the count of `### BOUNDARY PROTOCOL` section headers in the complete output. A row without a corresponding section header is a named-section gap.

| # | Boundary | Gate Name | Gate State (BINARY FIELD) | Status |
|---|----------|-----------|--------------------------|--------|
| 1 | PARSE → PHASE A | PARSE GATE | OPEN / BLOCKED | [ ] present |
| 2 | PHASE A → PHASE B | TRACE GATE | OPEN / BLOCKED | [ ] present |
| 3 | B1 → B2 | EXECUTION GATE | OPEN / BLOCKED | [ ] present |
| 4 | B2 → B3 | DOMAIN SYNTHESIS GATE | OPEN / BLOCKED | [ ] present |
| 5 | B3 → B4 | VERIFY GATE | OPEN / BLOCKED | [ ] present |
| 6 | B4 → VERDICT | RECOMMENDATIONS GATE | OPEN / BLOCKED | [ ] present |

**PROTOCOL MANIFEST GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

Do not write B1 until all six rows are filled and all six gate states are resolved.

---

#### B1 — EXECUTION SEQUENCE *(AUTHORITATIVE ARTIFACT)*

> **CITATION ANCHOR:** All B-section step references use **"Step N from B1."**

**MANIFEST COLUMN AUDIT:** Exactly four binary constraint-type columns in manifest row order.

| Step | Table | Operation | Before | After | Rollback (fixed taxonomy) | Data Loss (BINARY FIELD) | NOT NULL Risk (BINARY FIELD) | FK Violation (BINARY FIELD) | UNIQUE Violation (BINARY FIELD) | CHECK Violation (BINARY FIELD) | Idempotent (BINARY FIELD) |
|------|-------|-----------|--------|-------|--------------------------|--------------------------|------------------------------|-----------------------------|---------------------------------|-------------------------------|---------------------------|

**EXECUTION GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B1 → B2

- **EXIT BLOCK (BINARY FIELD):** EXECUTION GATE = ___ (OPEN / BLOCKED). Guards: B2.
- **ENTRY REFERENCE:** B2 requires `EXECUTION GATE = OPEN` from B1.

*(PROTOCOL COUNT MANIFEST row 3 — mark [ ] present after writing this block.)*

---

#### B2 — DOMAIN SYNTHESIS *(POSITIONED BEFORE B3 VERIFY — complete before writing B3)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

Synthesize domain impact. Seed a NEW inertia-contrast example that (1) names a different step, table, and consequence than any Q section example, AND (2) forms a **cross-role inertia chain**: an Operations-grounded cause from Q1/COST LEDGER expressed as a Commerce or Finance consequence.

Cross-role inertia chain:
*(a) Before Step N, the Operations infrastructure condition [from COST LEDGER row (a) / Q1] kept the [Commerce / Finance] process structurally sound because [dependency].*
*(b) After Step N, the Operations condition is broken — [Commerce / Finance] downstream process loses its guarantee.*
*(c) Consequence: [named Commerce or Finance failure, different step/table/domain from all Q section examples].*

**DOMAIN SYNTHESIS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B2 → B3

- **EXIT BLOCK (BINARY FIELD):** DOMAIN SYNTHESIS GATE = ___ (OPEN / BLOCKED). Guards: B3.
- **ENTRY REFERENCE:** B3 requires `DOMAIN SYNTHESIS GATE = OPEN` from B2.

*(PROTOCOL COUNT MANIFEST row 4 — mark [ ] present.)*

---

#### B3 — VERIFY *(requires DOMAIN SYNTHESIS GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

For each step with DATA LOSS = YES or NOT NULL RISK = YES: one verification query. Name table, column, expected result.

**VERIFY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B3 → B4

- **EXIT BLOCK (BINARY FIELD):** VERIFY GATE = ___ (OPEN / BLOCKED). Guards: B4.
- **ENTRY REFERENCE:** B4 requires `VERIFY GATE = OPEN` from B3.

*(PROTOCOL COUNT MANIFEST row 5 — mark [ ] present.)*

---

#### B4 — RECOMMENDATIONS *(requires VERIFY GATE = OPEN)*

> **CITATION ANCHOR:** All step references use **"Step N from B1."**

At most five ranked recommendations. For each: step, risk addressed, required action.

**RECOMMENDATIONS GATE (BINARY FIELD): ___ (OPEN / BLOCKED)**

---

### BOUNDARY PROTOCOL — B4 → VERDICT

- **EXIT BLOCK (BINARY FIELD):** RECOMMENDATIONS GATE = ___ (OPEN / BLOCKED). Guards: VERDICT.
- **ENTRY REFERENCE:** VERDICT requires `RECOMMENDATIONS GATE = OPEN` from B4.

*(PROTOCOL COUNT MANIFEST row 6 — mark [ ] present.)*

---

### VERDICT *(requires RECOMMENDATIONS GATE = OPEN)*

**MIGRATION READINESS (fixed taxonomy): SAFE TO RUN / RUN WITH MITIGATIONS / BLOCKED**

*(PROTOCOL COUNT MANIFEST verification: confirm all six rows marked [ ] present before writing MIGRATION READINESS verdict.)*

---

---

## Predicted Outcomes

| V | Score | / 230 | % | Golden (≥184) | C-35 | C-36 | Key distinguishing mechanism |
|---|-------|-------|---|---------------|------|------|------------------------------|
| V-01 | 225 | 225/230 | 97.8% | YES | PASS | FAIL | Named BOUNDARY PROTOCOL section headers (count-scannable); STATUS QUO COST Q1-embedded |
| V-02 | 225 | 225/230 | 97.8% | YES | FAIL | PASS | Inline BOUNDARY PROTOCOL code fences; STATUS QUO COST pre-Q1 named section with gate |
| V-03 | 230 | 230/230 | 100% | YES | PASS | PASS | Both mechanisms active; declarative register; Commerce-first |
| V-04 | 230 | 230/230 | 100% | YES | PASS | PASS | Both mechanisms active; imperative register; Operations-first; cross-role inertia chain |
| V-05 | 230 | 230/230 | 100% | YES | PASS (dual-surface) | PASS (table format) | PROTOCOL COUNT MANIFEST + COST LEDGER; dual-surface C-35 + machine-countable C-36 |

**Rank**: V-03 = V-04 = V-05 (230) > V-01 = V-02 (225)
**Tiebreak within top tier**: V-05 > V-04 > V-03 by excellence signal density

**New signals in V-05:**
- PROTOCOL COUNT MANIFEST as a pre-committed Phase B artifact that makes BOUNDARY PROTOCOL header count verifiable by manifest comparison at Phase B entry — a second surface for C-35 enforcement independent of header scanning.
- COST LEDGER table format for STATUS QUO COST makes the three-part structure (a)/(b)/(c) machine-countable by column: a STATUS QUO COST section with fewer than three filled rows has a visible gap without reading prose.
