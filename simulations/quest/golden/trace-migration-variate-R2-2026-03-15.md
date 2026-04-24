# trace-migration Variate — Round 2
**Date:** 2026-03-15
**Rubric:** v2 (C-01 through C-12; C-11 and C-12 new; C-09 tightened)
**Target criteria:** C-11 (admission-gate vocabulary enforcement), C-12 (halt-on-gap escalation protocol), C-09 (at least two cascade traces — single-entry no longer passes)

---

## Round 2 Variation Map

| Variation | Axis | C-11 | C-12 | C-09 | Notes |
|-----------|------|------|------|------|-------|
| V-01 | Phrasing register | Expected PASS | Expected PASS | Expected PASS | DIRECTIVE-0 vocabulary contract precedes all analytical content; DIRECTIVE-1 halt protocol is a named architectural primitive; all roles cite both by reference |
| V-02 | Output format | Expected PASS | Expected PASS | Expected PASS | OPERATION column schema carries approved-verb annotation inline; COMPLIANCE STATUS column flags disallowed phrases on creation; halt protocol is a mandatory form that fires when GAP-DETECTED cell is non-empty |
| V-03 | Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | VOCABULARY GATE and GAP HALT GATE are explicit phase checkpoints; phases cannot advance without clearing both gates; vocabulary enforcement is a re-entry mechanism, not a post-hoc review |
| V-04 | Role sequence + Phrasing register | Expected PASS | Expected PASS | Expected PASS | Operations-first role sequence (from Round 1 V-04) + DIRECTIVE vocabulary contract + halt protocol as named DIRECTIVES; two cascade traces are DIRECTIVES D-1 and D-2 with explicit pass condition stated |
| V-05 | Role sequence + Output format + Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | Three-layer combination: Operations entity registry table (role sequence) + vocabulary-compliance column (output format) + phase-gate halt blocks (lifecycle); each layer enforces a different failure mode |

---

## V-01 — Phrasing Register

**Axis:** Phrasing register
**Hypothesis:** DIRECTIVE-capitalized vocabulary enforcement as a pre-flight contract makes C-11 structurally unavoidable. If the approved-verb list and disallowed-phrase list are defined as DIRECTIVE 0 — a named block that all subsequent content is subordinate to — then every entity entry is governed by the contract before the analyst begins writing. The enforcement example in DIRECTIVE 0 shows the rejection form ("X is not an approved verb — use Y"), so the analyst has the rejection template before the first entity is written. DIRECTIVE 1 defines the halt protocol as a named structural primitive: when a gap fires, the halt form is the output — analysis does not continue until the named responsible role signs the acknowledgment gate. Both DIRECTIVEs are capitalized imperatives; the analyst cannot proceed past them to begin analysis without absorbing the contract.

---

You are running a migration trace signal for: {{topic}}

---

### DIRECTIVE 0 — VOCABULARY CONTRACT

> All migration operation descriptions in this output are governed by this vocabulary contract. DIRECTIVE 0 applies before the first entity is named. Compliance is spot-checkable: any reader may verify any operation cell against this list without reading surrounding prose.

**APPROVED VERB LIST** (DDL/DML only — use these exact terms):

| # | Approved Verb | Example Use |
|---|---------------|-------------|
| 1 | ADD COLUMN | ADD COLUMN `status` VARCHAR(20) NOT NULL DEFAULT 'active' |
| 2 | DROP COLUMN | DROP COLUMN `legacy_code` — data permanently removed |
| 3 | ALTER COLUMN TYPE | ALTER COLUMN `amount` from DECIMAL(18,4) to INTEGER |
| 4 | ADD NOT NULL | ADD NOT NULL constraint on `customer_id` (existing nulls must be backfilled first) |
| 5 | DROP NOT NULL | DROP NOT NULL on `notes` — column becomes nullable |
| 6 | ADD DEFAULT | ADD DEFAULT '0.00' on `discount_rate` |
| 7 | DROP DEFAULT | DROP DEFAULT on `created_at` — application must supply value |
| 8 | ADD FOREIGN KEY | ADD FOREIGN KEY `order_id` REFERENCES `orders(id)` ON DELETE CASCADE |
| 9 | DROP FOREIGN KEY | DROP FOREIGN KEY `fk_order_product` |
| 10 | ADD UNIQUE | ADD UNIQUE constraint on `sku` |
| 11 | DROP UNIQUE | DROP UNIQUE on `email` — duplicates now permitted |
| 12 | ADD CHECK | ADD CHECK (`price` > 0) |
| 13 | DROP CHECK | DROP CHECK `chk_status_valid` |
| 14 | CREATE INDEX | CREATE INDEX `idx_order_date` ON `orders(created_at)` |
| 15 | DROP INDEX | DROP INDEX `idx_legacy_code` |
| 16 | UPDATE (backfill) | UPDATE `orders` SET `status` = 'active' WHERE `status` IS NULL |
| 17 | DELETE CASCADE | DELETE CASCADE on `order_items` when parent `orders` row is deleted |
| 18 | RENAME COLUMN | RENAME COLUMN `qty` TO `quantity` |
| 19 | RENAME TABLE | RENAME TABLE `promo_codes` TO `promotion_codes` |
| 20 | TRUNCATE | TRUNCATE `migration_staging` — all rows removed |

**DISALLOWED PHRASE LIST** (these phrases are rejected at admission — do not use them):

| Disallowed Phrase | Rejection Form | Approved Replacement |
|-------------------|---------------|---------------------|
| "changes" | "CHANGES is not an approved verb — use ALTER COLUMN TYPE, ADD NOT NULL, or the specific DDL operation" | The specific DDL operation from the approved list |
| "modified" | "MODIFIED is not an approved verb — use ALTER COLUMN TYPE, ADD DEFAULT, or the specific DDL operation" | The specific DDL operation from the approved list |
| "updated" | "UPDATED is not an approved verb — use UPDATE (backfill) if performing a DML backfill, or the specific DDL operation" | UPDATE (backfill) or specific DDL |
| "schema updated" | "SCHEMA UPDATED is not an approved phrase — identify the specific DDL operation performed" | The specific DDL operation |
| "column changes" | "COLUMN CHANGES is not an approved phrase — name every operation performed on the column" | Each DDL operation listed separately |

**Enforcement rule:** Any MIGRATION ACTION field that contains a disallowed phrase is flagged as non-compliant. Flag format: `[NON-COMPLIANT: "X" is not an approved verb — use Y]`. The non-compliant entry is not counted as a passing MIGRATION ACTION for C-03 purposes. Rewrite required before the entity entry is complete.

---

### DIRECTIVE 1 — HALT-ON-GAP ESCALATION PROTOCOL

> This directive defines the halt protocol. All role sections and all cascade trace sections are governed by it. The halt protocol fires when any of the following conditions are detected: (a) an entity appears in domain role analysis that is not present in the entity registry, (b) a constraint type analysis field is empty for a registered entity, (c) a cascade trace references a downstream entity whose schema state is unknown.

**HALT BLOCK FORM** — use this exact structure whenever a gap fires:

```
HALT — GAP DETECTED
Gap condition: [name the specific gap: missing entity / empty constraint field / unknown downstream schema]
Scope: [entity name and field where the gap was detected]
Responsible role: [Operations / Commerce / Finance — the role accountable for resolving this gap]
Acknowledgment gate: Analysis does not continue past this block until the responsible role confirms:
  (1) the gap has been investigated,
  (2) either the missing information has been supplied or the gap has been explicitly scoped out with reasoning,
  (3) the responsible role name is recorded in the acknowledgment.
Acknowledgment: [PENDING / RESOLVED BY: (role name) — (resolution summary)]
```

**Protocol rule:** An output that flags a gap without issuing a HALT BLOCK does not satisfy this directive. The HALT BLOCK is not optional when a gap fires. If no gaps fire in this migration, the HALT BLOCK FORM must still appear once as a declared protocol — populated with "No gaps detected in this migration" and signed by Operations.

---

### ENTITY REGISTRY

List every database object this migration touches. This registry is the contract for all role sections. Roles may not reference entities absent from this registry.

| # | Entity | Type | Change Class | Owner Domain |
|---|--------|------|--------------|--------------|
| | | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER / PROCEDURE | ADDED / DROPPED / ALTERED / RENAMED | Operations / Commerce / Finance / Shared |

Rules:
- Enumerate every object. Omission is a higher risk than false inclusion — mark uncertain entries POSSIBLE.
- If an entity is missing, issue a HALT BLOCK (DIRECTIVE 1) before continuing.
- Change Class ALTERED requires per-entity analysis below. Change Class ADDED or DROPPED also requires per-entity analysis.

---

### OPERATIONS — SCHEMA MIGRATION EXPERT

You run first. Analyze every entity in the registry from the infrastructure and schema substrate perspective.

For each entity, produce the following sections using the exact labels. All MIGRATION ACTION fields must use DIRECTIVE 0 approved verbs. Disallowed phrases trigger the enforcement rule in DIRECTIVE 0.

**ENTITY: [name]**

BEFORE STATE:
Column types, nullability, defaults, constraints (NOT NULL / UNIQUE / CHECK / FK), index names and covered columns. If the current state is unknown: state that explicitly. Issue a HALT BLOCK (DIRECTIVE 1) — gap condition: unknown pre-migration schema state, responsible role: Operations.

MIGRATION ACTION:
[DIRECTIVE 0 applies. Each operation must use an approved verb from the list above. One named operation minimum per entity. If you write "column changes" or "modified" here, issue the enforcement flag and rewrite.]

AFTER STATE:
Full post-migration schema state. Independently readable — a reader who sees only this section can determine the final schema without reading BEFORE STATE.

DATA LOSS PATHS:
Check each: column drops (data permanently gone), type narrowing (values truncated or migration aborts), lossy casts (precision discarded), cascaded deletes (child rows removed), overwrite backfills (existing non-null values replaced). If none: state "No data loss paths identified for [entity]. Reasoning: [explain]." Silence does not pass.

CONSTRAINT VIOLATIONS:
For each new or tightened constraint: analyze whether pre-migration data would violate it. NOT NULL — existing nulls? UNIQUE — duplicate values? CHECK — out-of-range values? FK — orphan rows? If no new constraints: state "No new or tightened constraints for [entity]." Missing constraint analysis does not pass.

DEFAULT VALUE ANALYSIS:
For each new NOT NULL column or changed default: what value is written to existing rows? Is that value semantically correct for the Operations domain? Flag: empty strings on required code fields, zero amounts on financial totals, 1970-01-01 on required dates.

PERFORMANCE CLIFF:
For each high-risk operation (full-table UPDATE, DROP INDEX / CREATE INDEX, ALTER COLUMN TYPE requiring rewrite, FK addition without concurrent index): name it, assign risk level (LOW / MEDIUM / HIGH), state mitigation (batched UPDATE, online DDL flag, maintenance window).

REVERSIBILITY:
Verdict: REVERSIBLE / CONDITIONAL / IRREVERSIBLE. Rationale.

---

### COMMERCE — MIGRATION IMPACT EXPERT

Analyze Commerce domain entities from the registry: product catalog, pricing, order schema, promotion rules, entitlement records, inventory.

You may only reference entities in the registry. If a Commerce entity is missing: issue a HALT BLOCK (DIRECTIVE 1) — gap condition: Commerce entity not in registry, responsible role: Operations (to register), acknowledge before continuing.

Apply the same section structure as Operations. Commerce-specific addition: for any constraint violation, flag whether it causes a customer-visible failure (checkout abort, catalog display error, entitlement gap) and assign urgency.

---

### FINANCE — MIGRATION IMPACT EXPERT

Analyze Finance domain entities from the registry: ledger tables, transaction records, cost center schema, period-end views, audit trail structures, reconciliation tables.

You may only reference entities in the registry. If a Finance entity is missing: issue a HALT BLOCK (DIRECTIVE 1) — gap condition: Finance entity not in registry, responsible role: Operations (to register), acknowledge before continuing.

Apply the same section structure as Operations. Finance-specific addition: for any data loss path on a Finance entity, flag whether the lost data is subject to audit retention, regulatory archival, or period-close lock requirements. These are CRITICAL severity by default regardless of row volume.

---

### CROSS-ENTITY DEPENDENCY CASCADE

**DIRECTIVE D-1:** Produce at least two end-to-end cascade traces. A section with one trace does not pass C-09. Each trace must follow the form: [source entity / column / change] → [impact entity or component] → [consequence] → [mitigation before migration runs].

**DIRECTIVE D-2:** At least one trace must cross layers (schema → application layer, schema → ETL job, schema → view or stored procedure). A trace that stays entirely within the schema layer counts as one trace but does not satisfy the cross-layer requirement on its own.

Required traces:

**TRACE 1 — [name the path]:**
[source] → [impact] → [consequence] → [mitigation]

**TRACE 2 — [name the path]:**
[source] → [impact] → [consequence] → [mitigation]

Additional traces if applicable.

If a cascade trace encounters an unknown downstream schema state: issue a HALT BLOCK (DIRECTIVE 1) — gap condition: unknown downstream schema state in cascade trace, responsible role: Operations.

---

### RISK REGISTER

One row per identified issue. Every data loss path, constraint violation, performance cliff, irreversible operation, and cascade consequence must have an entry.

| Issue | Entity | Severity | Likelihood | Remediation |
|-------|--------|----------|------------|-------------|
| | | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | [action required before migration runs] |

Severity definitions: CRITICAL = data loss or migration abort on non-empty production table; HIGH = silent data corruption or multi-minute lock on production-traffic table; MEDIUM = incorrect default or broken non-critical view; LOW = dev-environment or cosmetic impact only.

---

## V-02 — Output Format

**Axis:** Output format
**Hypothesis:** A compliance ledger format makes C-11 violations visible as malformed cells rather than missing prose sections. The OPERATION column header carries the approved-verb annotation inline — any reader scanning that column sees immediately whether each cell is compliant. A COMPLIANCE STATUS column (PASS / DISALLOWED PHRASE FLAGGED / REWRITE REQUIRED) makes the enforcement spot-checkable without re-reading the surrounding analysis. C-12 halt protocol is a mandatory form row in the REGISTRY COMPLETENESS TABLE — if the GAP-DETECTED column is non-empty, the HALT BLOCK row fires automatically. The form structure makes "gap without halt" structurally impossible: the HALT BLOCK row is adjacent to the GAP cell, and an empty halt cell when the gap cell is populated is a visible omission.

---

You are running a migration trace signal for: {{topic}}

Produce all output in structured tables. Every entity, every finding, every risk must appear in a table row. Prose is permitted only in NOTES cells and in the RATIONALE column of the risk register.

---

### TABLE 0 — VOCABULARY CONTRACT

This table governs all MIGRATION OPERATION cells in this output. It must appear before TABLE 1.

**Approved Verbs** (OPERATION cells must use one of these):

| Approved Verb | Scope |
|---------------|-------|
| ADD COLUMN | DDL: new column added to existing table |
| DROP COLUMN | DDL: column removed permanently |
| ALTER COLUMN TYPE | DDL: column data type changed |
| ADD NOT NULL | DDL: nullability constraint tightened |
| DROP NOT NULL | DDL: nullability constraint relaxed |
| ADD DEFAULT | DDL: default value added |
| DROP DEFAULT | DDL: default value removed |
| ADD FOREIGN KEY | DDL: referential constraint added |
| DROP FOREIGN KEY | DDL: referential constraint removed |
| ADD UNIQUE | DDL: uniqueness constraint added |
| DROP UNIQUE | DDL: uniqueness constraint removed |
| ADD CHECK | DDL: check constraint added |
| DROP CHECK | DDL: check constraint removed |
| CREATE INDEX | DDL: index created |
| DROP INDEX | DDL: index dropped |
| UPDATE (backfill) | DML: existing rows updated to supply new value |
| DELETE CASCADE | DML: child rows deleted via FK cascade |
| RENAME COLUMN | DDL: column renamed |
| RENAME TABLE | DDL: table renamed |
| TRUNCATE | DML: all rows removed |

**Disallowed Phrases** (rejection fires when detected in any OPERATION cell):

| Disallowed Phrase | Rejection Message | Required Replacement |
|-------------------|------------------|----------------------|
| "changes" | CHANGES is not an approved verb — identify the specific DDL operation | Specific approved verb from the list above |
| "modified" | MODIFIED is not an approved verb — use ALTER COLUMN TYPE, ADD DEFAULT, or the specific DDL operation | Specific approved verb |
| "updated" | UPDATED is not an approved verb for DDL — use UPDATE (backfill) for DML backfills, or the specific DDL verb | UPDATE (backfill) or specific DDL verb |
| "schema updated" | SCHEMA UPDATED is not an approved phrase — identify each DDL operation individually | Each DDL operation as a separate row |
| "altered" (lowercase prose) | "altered" is ambiguous — use ALTER COLUMN TYPE, ADD NOT NULL, DROP NOT NULL, or the specific DDL operation | Specific approved verb |

**Enforcement:** If any OPERATION cell contains a disallowed phrase, the COMPLIANCE STATUS cell for that row must read: `DISALLOWED PHRASE: "[phrase]" — REWRITE REQUIRED`. The row does not count as a passing MIGRATION ACTION entry until rewritten.

---

### TABLE 1 — ENTITY REGISTRY

Fill completely before any other analysis table.

| # | Entity | Object Type | Change Class | Owner Domain | Registry Status |
|---|--------|-------------|--------------|--------------|-----------------|
| | | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER | ADDED / DROPPED / ALTERED / RENAMED | Operations / Commerce / Finance / Shared | REGISTERED / GAP-DETECTED |

**Registry Completeness:** Any row with Registry Status = GAP-DETECTED triggers the HALT BLOCK in TABLE 1-HALT below.

---

### TABLE 1-HALT — REGISTRY GAP HALT PROTOCOL

This table fires when any TABLE 1 row has Registry Status = GAP-DETECTED. If no gaps: complete the no-gap declaration row.

| Field | Value |
|-------|-------|
| Gap condition | [NONE / description of missing entity or unknown object] |
| Scope | [Entity name and the role that detected the gap] |
| Responsible role | Operations — entity registration is the Operations responsibility |
| Acknowledgment gate | Analysis does not proceed to TABLE 2 until this row is complete |
| Acknowledgment | [PENDING / RESOLVED: (summary) / NO GAPS DETECTED — signed by Operations] |

---

### TABLE 2 — BEFORE / AFTER STATE

One row per column or constraint per entity. Do not merge multiple changes into a single row.

| # | Entity | Object Name | Object Type | Before State | Migration Operation | Compliance Status | After State | Change Reason |
|---|--------|-------------|-------------|-------------|---------------------|------------------|-------------|---------------|
| | | | COLUMN / CONSTRAINT / INDEX / DEFAULT | [type, nullability, default, current value] | [Approved verb from TABLE 0] | PASS / DISALLOWED PHRASE FLAGGED / BEFORE STATE UNKNOWN | [post-migration state, fully described] | |

Rules:
- Before State: name actual type and nullability. "Existing state" or "as-is" does not pass.
- Migration Operation: must be an approved verb from TABLE 0. Compliance Status fires automatically for disallowed phrases.
- After State: independently readable — full column definition, not just the delta.
- Before State UNKNOWN: write "UNKNOWN — schema inspection required before migration runs" and enter DISALLOWED PHRASE FLAGGED in Compliance Status. Issue TABLE 1-HALT for the unknown state.

---

### TABLE 3 — DATA LOSS ANALYSIS

One row per identified data loss path. If no paths exist for an entity, write a NONE row with reasoning.

| Entity | Column / Object | Loss Mechanism | Data at Risk Description | Volume Estimate | Severity | Mitigation |
|--------|----------------|----------------|--------------------------|-----------------|----------|------------|
| | | TYPE NARROWING / COLUMN DROP / LOSSY CAST / CASCADE DELETE / OVERWRITE BACKFILL / TRUNCATION | | [rows or % of table] | CRITICAL / HIGH / MEDIUM / LOW | |

---

### TABLE 4 — CONSTRAINT VIOLATION ANALYSIS

One row per new or tightened constraint per entity.

| Entity | Constraint Type | Constraint Detail | Pre-Migration Data Risk | Violation Likelihood | Domain Impact | Severity |
|--------|----------------|------------------|------------------------|---------------------|---------------|----------|
| | NOT NULL / UNIQUE / CHECK / FOREIGN KEY | [column and constraint definition] | [analysis of existing data state] | CERTAIN / PROBABLE / POSSIBLE / NONE | Operations / Commerce / Finance | CRITICAL / HIGH / MEDIUM / LOW |

If no new or tightened constraints: write one row per entity with "No new or tightened constraints — [reasoning]."

---

### TABLE 5 — DEFAULT VALUE GAP ANALYSIS

One row per new NOT NULL column or changed default.

| Entity | Column | New Constraint | Default Value Written to Existing Rows | Semantically Correct? | Domain Concern | Action Required |
|--------|--------|----------------|----------------------------------------|----------------------|----------------|-----------------|
| | | ADD NOT NULL / ADD DEFAULT | [exact value that will be written] | YES / NO / UNKNOWN | [Commerce / Finance / Operations concern] | [backfill required / default is safe / verify before migration] |

---

### TABLE 6 — PERFORMANCE CLIFF

One row per high-risk operation.

| Entity | Operation | Risk Type | Risk Level | Estimated Lock Duration | Mitigation | Scheduling Constraint |
|--------|-----------|-----------|------------|------------------------|------------|----------------------|
| | [Approved verb from TABLE 0] | TABLE SCAN / LOCK ESCALATION / INDEX REBUILD / STATISTICS DISRUPTION | LOW / MEDIUM / HIGH | [estimate or UNKNOWN] | [batching / online DDL / maintenance window / concurrent index] | [none / maintenance window required / off-peak only] |

---

### TABLE 7 — REVERSIBILITY ASSESSMENT

One row per entity.

| Entity | Reversibility Verdict | Rollback Path | Residual Consequence | Net Irreversibility Risk |
|--------|----------------------|---------------|---------------------|--------------------------|
| | REVERSIBLE / CONDITIONAL / IRREVERSIBLE | [what rollback requires] | [what rollback leaves behind] | LOW / MEDIUM / HIGH |

---

### TABLE 8 — CROSS-ENTITY CASCADE TRACES

**Minimum two complete traces required. Single-trace sections do not pass C-09.**

At least one trace must cross layers (schema → application / schema → ETL / schema → view or stored procedure).

| Trace # | Source Entity / Column / Change | Impact Entity or Component | Impact Layer | Consequence | Mitigation Before Migration |
|---------|---------------------------------|---------------------------|-------------|-------------|----------------------------|
| 1 | | | SCHEMA / APPLICATION / ETL / REPORTING / VIEW | | |
| 2 | | | SCHEMA / APPLICATION / ETL / REPORTING / VIEW | | |

If a cascade trace encounters an unknown downstream schema: add a row with "GAP-DETECTED — downstream schema unknown" and fire TABLE 1-HALT with responsible role = Operations.

---

### TABLE 9 — RISK REGISTER

One row per identified issue. All TABLE 3, 4, 5, 6, 7, 8 findings with severity >= MEDIUM must have a row here.

| Issue # | Issue Description | Entity | Source Table | Severity | Likelihood | Remediation Before Migration Runs |
|---------|-----------------|--------|-------------|----------|------------|-----------------------------------|
| | | | TABLE 3 / 4 / 5 / 6 / 7 / 8 | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | |

---

## V-03 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** Making the vocabulary enforcement and halt protocol explicit named lifecycle checkpoints — gates that must be cleared before the next phase can begin — prevents silent omission at the structural level. VOCABULARY GATE fires at the entry to each phase: before writing any MIGRATION ACTION content, the analyst must clear the vocabulary check (all operations in this phase use approved verbs). GAP HALT GATE fires at the boundary between enumeration and analysis phases: if any registry entry is incomplete, the analysis phase cannot begin. Both gates are re-entry mechanisms: a failed gate sends the analyst back to the upstream phase, not forward. The lifecycle structure makes advancement past a gap or vocabulary violation structurally visible as a gate that was skipped, not as missing prose in an unstructured section.

---

You are running a migration trace signal for: {{topic}}

---

### PHASE 0 — VOCABULARY AND HALT PROTOCOL INITIALIZATION

This phase initializes two cross-cutting protocols before any analytical content begins.

**0-A: VOCABULARY PROTOCOL**

All migration operations in this output must use an approved verb from this list. This protocol applies to every phase.

Approved verbs: ADD COLUMN, DROP COLUMN, ALTER COLUMN TYPE, ADD NOT NULL, DROP NOT NULL, ADD DEFAULT, DROP DEFAULT, ADD FOREIGN KEY, DROP FOREIGN KEY, ADD UNIQUE, DROP UNIQUE, ADD CHECK, DROP CHECK, CREATE INDEX, DROP INDEX, UPDATE (backfill), DELETE CASCADE, RENAME COLUMN, RENAME TABLE, TRUNCATE.

Disallowed phrases: "changes," "modified," "updated," "schema updated," "column changes."

Enforcement example — if a MIGRATION ACTION field reads "The status column was modified to add a NOT NULL constraint," the vocabulary check fires:
> [VOCABULARY VIOLATION: "modified" is not an approved verb. Rewrite: "ADD NOT NULL on `status` column — existing nulls must be backfilled before constraint is applied."]

The enforcement form is: `[VOCABULARY VIOLATION: "X" is not an approved verb — rewrite using Y.]`

Any entry containing a disallowed phrase must be rewritten before the phase it appears in can advance to its closing gate.

**0-B: HALT-ON-GAP PROTOCOL**

When any coverage gap is detected (missing entity, unknown pre-migration state, empty constraint field, unknown downstream component), the following halt block fires immediately:

```
GAP HALT — [Phase name where gap was detected]
Gap condition: [specific: missing entity / unknown schema / empty constraint field / unknown downstream]
Entity / scope: [name]
Responsible role: [Operations / Commerce / Finance]
Acknowledgment gate: This block must be resolved before the current phase closes.
Resolution: [PENDING / RESOLVED: (role) confirmed (summary) / NOT APPLICABLE: no gaps detected]
```

**No-gap declaration (required even when no gaps fire):**

```
GAP HALT PROTOCOL — PHASE 0 INITIALIZATION
Gap condition: None detected at protocol initialization
Responsible role: Operations
Acknowledgment gate: Protocol declared and active for all subsequent phases
Resolution: RESOLVED — Operations declares protocol active. No gaps at initialization.
```

---

### PHASE 1 — ENTITY INVENTORY

**Phase 1 entry condition:** Phase 0-A and Phase 0-B protocols initialized.

**Phase 1 objective:** Enumerate every database object this migration touches. This is the contract for Phases 2 and 3.

**ENTITY INVENTORY TABLE**

| # | Entity | Object Type | Change Class | Owner Domain |
|---|--------|-------------|--------------|--------------|
| | | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER | ADDED / DROPPED / ALTERED / RENAMED | Operations / Commerce / Finance / Shared |

**Phase 1 VOCABULARY GATE:**
Before closing Phase 1: verify that no MIGRATION ACTION content has been written yet (inventory phase does not produce migration operations). Gate: PASS (no vocabulary content in Phase 1 to check).

**Phase 1 GAP HALT GATE:**
Before advancing to Phase 2: check whether any entity's Change Class is UNKNOWN or any Object Type is uncertain.
- If yes: fire the GAP HALT BLOCK (Protocol 0-B). Phase 2 does not begin until the halt block is resolved.
- If no: state "Phase 1 GAP HALT GATE: CLEAR — all entities registered with known change class."

---

### PHASE 2 — BEFORE-STATE DOCUMENTATION

**Phase 2 entry condition:** Phase 1 GAP HALT GATE = CLEAR.

**Phase 2 objective:** For every entity in the Phase 1 inventory, document the exact schema state before the migration executes.

For each entity:

**ENTITY: [name] — BEFORE STATE**

Columns: [list each column with type, nullability, default value, and any constraints]
Indexes: [list index names and covered columns]
Constraints: [list all NOT NULL, UNIQUE, CHECK, FK constraints with their definitions]
Known gaps: [any schema element whose current state is UNKNOWN — fire GAP HALT BLOCK if present]

**Phase 2 VOCABULARY GATE:**
Before closing Phase 2: verify no migration operation verbs appear in BEFORE STATE descriptions. BEFORE STATE is descriptive only — no approved or disallowed verbs should appear here. Gate: PASS if no operation language was used in before-state descriptions.

**Phase 2 GAP HALT GATE:**
Before advancing to Phase 3: check whether any BEFORE STATE contains UNKNOWN fields.
- If yes: fire GAP HALT BLOCK. Phase 3 does not begin until the halt block is resolved.
- If no: state "Phase 2 GAP HALT GATE: CLEAR — all before-states documented."

---

### PHASE 3 — MIGRATION ACTION TRACING

**Phase 3 entry condition:** Phase 2 GAP HALT GATE = CLEAR.

**Phase 3 objective:** For each entity, name every DDL or DML operation the migration performs. All operations must use Phase 0-A approved verbs.

For each entity:

**ENTITY: [name] — MIGRATION ACTIONS**

| Operation | Object | Detail |
|-----------|--------|--------|
| [Approved verb] | [Column / constraint / index name] | [Specific parameters: type, value, reference] |

**Phase 3 VOCABULARY GATE:**
Before closing Phase 3: scan every Operation cell in this phase. Any disallowed phrase fires the enforcement form and requires rewrite before this gate clears.
- State: "Phase 3 VOCABULARY GATE: [PASS — all operations use approved verbs / HOLD — (entity: operation) contains disallowed phrase, rewrite required]"

**Phase 3 GAP HALT GATE:**
Before advancing to Phase 4: verify that every entity in the Phase 1 inventory has at least one operation in Phase 3.
- If an entity has no operations listed: fire GAP HALT BLOCK — gap condition: entity in inventory has no migration actions recorded, responsible role: Operations.
- If all entities have operations: state "Phase 3 GAP HALT GATE: CLEAR — all inventory entities have at least one migration action."

---

### PHASE 4 — ANALYTICAL REVIEW

**Phase 4 entry condition:** Phase 3 VOCABULARY GATE = PASS, Phase 3 GAP HALT GATE = CLEAR.

**Phase 4 objective:** Apply domain role analysis to every entity. Three roles run in sequence: Operations (infrastructure), Commerce (domain), Finance (domain).

For each entity, each role applies:

DATA LOSS ANALYSIS:
Check: column drops, type narrowing, lossy casts, cascaded deletes, overwrite backfills. State explicitly if none.

CONSTRAINT VIOLATION ANALYSIS:
For each new/tightened constraint: analyze pre-migration data risk. NOT NULL: existing nulls? UNIQUE: duplicates? CHECK: out-of-range values? FK: orphan rows? State explicitly if no new constraints.

DEFAULT VALUE ANALYSIS:
For each new NOT NULL column or changed default: what value is written to existing rows? Semantically correct for this domain? Flag domain-specific concerns.

PERFORMANCE CLIFF:
High-risk operations: full-table UPDATE backfill, DROP INDEX / CREATE INDEX, ALTER COLUMN TYPE requiring rewrite, FK addition without concurrent index. Risk level (LOW / MEDIUM / HIGH) + mitigation for each.

REVERSIBILITY:
Verdict: REVERSIBLE / CONDITIONAL / IRREVERSIBLE. Rationale.

**Phase 4 VOCABULARY GATE:**
Before closing Phase 4: verify that all MIGRATION ACTION references in analytical commentary use approved verbs. Gate: PASS or HOLD with specific violating entry.

**Phase 4 GAP HALT GATE:**
Before advancing to Phase 5: verify that every constraint type appearing in any Phase 4 constraint analysis has been analyzed by all three roles.
- If a constraint type was analyzed by Operations but not Commerce or Finance: fire GAP HALT BLOCK — gap condition: constraint type analysis incomplete for (role), responsible role: (Commerce or Finance).
- If complete: state "Phase 4 GAP HALT GATE: CLEAR — all constraint types analyzed by all three roles."

---

### PHASE 5 — CASCADE TRACE AND SYNTHESIS

**Phase 5 entry condition:** Phase 4 GAP HALT GATE = CLEAR.

**Phase 5 objective:** Trace second-order effects and synthesize cross-role findings. Minimum two complete cascade traces required — a Phase 5 section with one trace does not pass.

**CASCADE TRACE 1 — [name the path]:**
[Source entity / column / change] → [impact entity or component] → [impact layer: schema / application / ETL / reporting] → [consequence] → [mitigation before migration runs]

**CASCADE TRACE 2 — [name the path]:**
[Source entity / column / change] → [impact entity or component] → [impact layer: schema / application / ETL / reporting] → [consequence] → [mitigation before migration runs]

At least one trace must be cross-layer (schema → application or schema → ETL or schema → view / stored procedure).

**Phase 5 GAP HALT GATE:**
Before closing Phase 5: verify that each cascade trace has a named mitigation. A trace without a mitigation is incomplete.
- If incomplete: fire GAP HALT BLOCK — gap condition: cascade trace has no mitigation, responsible role: Operations.
- If complete: state "Phase 5 GAP HALT GATE: CLEAR."

**RISK REGISTER:**

| Issue | Entity | Severity | Likelihood | Remediation Before Migration Runs |
|-------|--------|----------|------------|-----------------------------------|
| | | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | |

---

## V-04 — Role Sequence + Phrasing Register

**Axis:** Role sequence + Phrasing register (combined)
**Hypothesis:** Round 1's best performer (V-04, DIRECTIVE phrasing) demonstrated that DIRECTIVE-capitalized imperatives eliminate the most common omission path — a role skipping entities outside its vocabulary. Round 2's new criteria are structurally analogous: C-11 is a vocabulary omission problem (analyst uses generic phrases instead of specific verbs) and C-12 is a gap-escalation omission problem (analyst flags a gap instead of halting). Both are best addressed by DIRECTIVE imperatives that name the failure mode explicitly before it can occur. Adding Operations-first role sequencing ensures entity enumeration happens at the schema level before domain roles apply their filters, which is the root-cause fix for registry gaps. DIRECTIVEs 0 and 1 are standalone named blocks that precede all role content — they govern every role section by position, not by per-role embedding.

---

You are running a migration trace signal for: {{topic}}

---

**DIRECTIVE 0 — VOCABULARY ENFORCEMENT CONTRACT**

> All MIGRATION ACTION fields in this output are governed by this vocabulary contract. DIRECTIVE 0 is declared before the first entity is written. It applies to all role sections, all cascade traces, and all synthesis sections.

Approved verbs (use these exact terms in MIGRATION ACTION fields):
ADD COLUMN | DROP COLUMN | ALTER COLUMN TYPE | ADD NOT NULL | DROP NOT NULL | ADD DEFAULT | DROP DEFAULT | ADD FOREIGN KEY | DROP FOREIGN KEY | ADD UNIQUE | DROP UNIQUE | ADD CHECK | DROP CHECK | CREATE INDEX | DROP INDEX | UPDATE (backfill) | DELETE CASCADE | RENAME COLUMN | RENAME TABLE | TRUNCATE

Disallowed phrases (these are rejected at admission):
- "changes" → enforcement: `[DIRECTIVE 0 VIOLATION: "changes" is not an approved verb — use the specific DDL operation, e.g., ALTER COLUMN TYPE or ADD NOT NULL]`
- "modified" → enforcement: `[DIRECTIVE 0 VIOLATION: "modified" is not an approved verb — use ALTER COLUMN TYPE, ADD DEFAULT, or the specific DDL operation]`
- "updated" → enforcement: `[DIRECTIVE 0 VIOLATION: "updated" is not an approved verb for DDL — use UPDATE (backfill) for DML backfills, or the specific DDL verb]`

Enforcement rule: A MIGRATION ACTION field containing a disallowed phrase must carry the DIRECTIVE 0 VIOLATION tag and must be rewritten. The entry does not count as a passing operation until it uses an approved verb.

---

**DIRECTIVE 1 — HALT-ON-GAP ESCALATION**

> When any coverage gap is detected, issue the HALT BLOCK below and do not advance analysis past it until the acknowledgment gate is cleared.

Gap conditions that trigger DIRECTIVE 1: (a) entity in domain role analysis not present in Operations registry; (b) MIGRATION ACTION field left empty for a registered entity; (c) constraint type analysis field incomplete; (d) cascade trace downstream component with unknown schema state.

HALT BLOCK form:
```
DIRECTIVE 1 — HALT
Gap detected: [specific condition]
Entity / scope: [name]
Responsible role: [Operations / Commerce / Finance]
Acknowledgment gate: [responsible role] must confirm gap is resolved before analysis continues.
Resolution: [PENDING / RESOLVED BY: (role) — (summary)]
```

DIRECTIVE 1 no-gap declaration (required even if no gaps fire):
```
DIRECTIVE 1 — NO GAPS DETECTED
Gap condition: None in this migration
Responsible role: Operations
Acknowledgment gate: Operations confirms entity registry is complete and all constraint fields are populated.
Resolution: RESOLVED BY: Operations — registry complete, no gaps detected.
```

---

**DIRECTIVE A — ENTITY REGISTRY (Operations runs first)**

> Operations runs first. The entity registry is the contract for all role sections. Finance and Commerce may not reference entities absent from this registry.

Operations: enumerate every database object this migration touches.

| # | Entity | Object Type | Change Class | Owner Domain |
|---|--------|-------------|--------------|--------------|
| | | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER | ADDED / DROPPED / ALTERED / RENAMED | Operations / Commerce / Finance / Shared |

After completing the registry: check for gaps. If any entity is uncertain or missing, issue a DIRECTIVE 1 HALT BLOCK before proceeding to per-entity analysis.

---

**DIRECTIVE B — OPERATIONS ANALYSIS (runs first; establishes infrastructure baseline)**

> Operations runs before Finance and Commerce. Infrastructure substrate must be established before domain role consequence analysis proceeds.

For each entity in the registry, produce the following. All MIGRATION ACTION fields: apply DIRECTIVE 0. DIRECTIVE 0 violations: apply the enforcement tag and rewrite.

**ENTITY: [name]**

BEFORE STATE:
[Enumerate columns: type, nullability, default, constraints, indexes. Unknown state: issue DIRECTIVE 1 HALT BLOCK.]

MIGRATION ACTION:
[Apply DIRECTIVE 0. At least one approved verb. No disallowed phrases.]

AFTER STATE:
[Full post-migration schema. Independently readable.]

DATA LOSS PATHS:
[Column drops / type narrowing / lossy casts / cascaded deletes / overwrite backfills. Explicit "none" with reasoning if not applicable.]

CONSTRAINT VIOLATIONS:
[NOT NULL / UNIQUE / CHECK / FK analysis against pre-migration data. Explicit "none" if no new constraints.]

DEFAULT VALUE ANALYSIS:
[New NOT NULL columns and changed defaults: what value is written, is it semantically correct for the Operations domain.]

PERFORMANCE CLIFF:
[HIGH-risk: full-table UPDATE backfill / DROP-CREATE index pair / ALTER COLUMN TYPE rewrite / FK without concurrent index. Risk level: LOW / MEDIUM / HIGH. Mitigation.]

REVERSIBILITY:
[REVERSIBLE / CONDITIONAL / IRREVERSIBLE. Rationale.]

---

**DIRECTIVE C — FINANCE ANALYSIS (runs after Operations)**

> Finance runs after Operations. Finance may only reference entities in the Operations registry. Missing Finance entity: issue DIRECTIVE 1 HALT BLOCK — responsible role: Operations.

For each Finance domain entity in the registry (ledger tables, transaction records, cost center schema, period-end views, audit trail structures, reconciliation tables): apply all DIRECTIVE B sections. Finance-specific addition: flag data loss paths on Finance entities for audit retention, regulatory archival, or period-close lock requirements — CRITICAL severity by default.

---

**DIRECTIVE D — COMMERCE ANALYSIS (runs after Finance)**

> Commerce runs last. Commerce may only reference entities in the Operations registry. Missing Commerce entity: issue DIRECTIVE 1 HALT BLOCK — responsible role: Operations.

For each Commerce domain entity in the registry (product catalog, pricing, order schema, promotion rules, entitlement records, inventory): apply all DIRECTIVE B sections. Commerce-specific addition: flag constraint violations for customer-visible failures (checkout abort, catalog display error, entitlement gap) and assign urgency.

---

**DIRECTIVE D-1 — CASCADE TRACE (minimum two traces required)**

> Produce at least two complete end-to-end cascade traces. A section with one trace does not satisfy C-09. Single-entity cascade sections do not pass.

**TRACE 1:**
[Source entity / column / change] → [impact entity or component] → [impact layer] → [consequence] → [mitigation]

**TRACE 2:**
[Source entity / column / change] → [impact entity or component] → [impact layer] → [consequence] → [mitigation]

**DIRECTIVE D-2 — CROSS-LAYER REQUIREMENT**

> At least one of the two required traces must cross layers: schema → application code, schema → ETL pipeline, schema → view or stored procedure, or schema → reporting query. A trace that stays entirely within the schema layer (table → table) satisfies the two-trace count but does not satisfy the cross-layer requirement independently.

For each cascade trace: if a downstream component's schema state is unknown, issue DIRECTIVE 1 HALT BLOCK — responsible role: Operations.

---

**DIRECTIVE E — RISK REGISTER**

> One row per identified issue. Every data loss path, constraint violation, performance cliff, irreversible operation, and cascade consequence must appear here. An issue present in role analysis but absent from the risk register is a coverage gap — issue DIRECTIVE 1 HALT BLOCK if detected.

| Issue | Entity | Severity | Likelihood | Remediation Before Migration Runs |
|-------|--------|----------|------------|-----------------------------------|
| | | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | |

Severity definitions: CRITICAL = data loss or migration abort on non-empty production table; HIGH = silent corruption or multi-minute lock on production-traffic table; MEDIUM = incorrect default or broken non-critical view; LOW = dev or cosmetic impact only.

---

## V-05 — Role Sequence + Output Format + Lifecycle Emphasis

**Axis:** Role sequence + Output format + Lifecycle emphasis (combined)
**Hypothesis:** Three independently sufficient enforcement layers — each targeting a different failure mode — produce coverage that survives any single-layer failure. Layer 1 (role sequence): Operations runs first and registers every entity; domain roles cannot introduce entities the registry doesn't contain; registry gaps are structurally visible. Layer 2 (output format): the OPERATION column carries the vocabulary contract as a column header annotation; any cell that violates the contract produces a COMPLIANCE flag in the adjacent column; violations are visible without reading surrounding prose. Layer 3 (lifecycle emphasis): phase-gate halt blocks prevent advancement past gaps; the halt form is a named structural unit, not an embedded note; a skipped halt block is an empty form cell, not a missing paragraph. C-11 is primarily a Layer 2 property, C-12 is primarily a Layer 3 property, and C-09 is a Layer 3 property (two-trace floor enforced at the CASCADE TRACE phase gate).

---

You are running a migration trace signal for: {{topic}}

---

### VOCABULARY CONTRACT (declared before analysis begins)

Approved verbs for all MIGRATION OPERATION cells:
ADD COLUMN | DROP COLUMN | ALTER COLUMN TYPE | ADD NOT NULL | DROP NOT NULL | ADD DEFAULT | DROP DEFAULT | ADD FOREIGN KEY | DROP FOREIGN KEY | ADD UNIQUE | DROP UNIQUE | ADD CHECK | DROP CHECK | CREATE INDEX | DROP INDEX | UPDATE (backfill) | DELETE CASCADE | RENAME COLUMN | RENAME TABLE | TRUNCATE

Disallowed phrases (fire compliance flag on detection):
- "changes" — COMPLIANCE FLAG: `NOT-APPROVED: "changes" — use specific DDL verb`
- "modified" — COMPLIANCE FLAG: `NOT-APPROVED: "modified" — use ALTER COLUMN TYPE or specific DDL verb`
- "updated" (in DDL context) — COMPLIANCE FLAG: `NOT-APPROVED: "updated" — use UPDATE (backfill) for DML or specific DDL verb`

Enforcement example: an OPERATION cell reading "status column was modified" fires: `NOT-APPROVED: "modified" — use ADD NOT NULL or ALTER COLUMN TYPE and describe the specific change.`

---

### HALT PROTOCOL (declared before analysis begins)

When a gap is detected, fire the HALT BLOCK immediately. Analysis does not advance past an unresolved halt block.

**HALT BLOCK FORM:**

| Field | Required Value |
|-------|---------------|
| Phase | [Phase name where gap was detected] |
| Gap condition | [Missing entity / unknown schema / empty constraint field / unknown downstream component] |
| Scope | [Entity and field] |
| Responsible role | [Operations / Commerce / Finance] |
| Acknowledgment gate | Responsible role must confirm resolution before analysis advances |
| Resolution | [PENDING / RESOLVED BY: (role) — (summary)] |

**No-gap declaration** (required even if no gaps fire — place before PHASE 1):

| Field | Value |
|-------|-------|
| Phase | Pre-analysis initialization |
| Gap condition | None detected |
| Responsible role | Operations |
| Acknowledgment gate | Operations confirms: halt protocol is active, registry will be declared complete before Phase 2 entry |
| Resolution | RESOLVED BY: Operations — protocol initialized, no pre-analysis gaps |

---

### PHASE 1 — ENTITY REGISTRY (Operations runs first)

Operations runs first. All entities must be registered here before any role analysis begins. Domain roles (Commerce, Finance) may not reference entities not present in this registry. An entity appearing in domain analysis but absent here fires the HALT PROTOCOL.

| # | Entity | Object Type | Change Class | Owner Domain | Registry Completeness |
|---|--------|-------------|--------------|--------------|----------------------|
| | | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER | ADDED / DROPPED / ALTERED / RENAMED | Operations / Commerce / Finance / Shared | COMPLETE / GAP-DETECTED |

**Phase 1 gate:** Before advancing to Phase 2, verify all rows have Registry Completeness = COMPLETE. Any GAP-DETECTED row fires the HALT BLOCK. Gate: PASS or HALT.

---

### PHASE 2 — BEFORE / AFTER STATE (table format, one row per column or constraint)

**Phase 2 entry:** Phase 1 gate = PASS.

Do not merge multiple changes into one row. One row per column or constraint change per entity.

| Entity | Object Name | Object Type | Before State | Migration Operation | Compliance | After State |
|--------|-------------|-------------|-------------|---------------------|------------|-------------|
| | | COLUMN / CONSTRAINT / INDEX / DEFAULT | [type, nullability, default, constraint] | [Approved verb — see Vocabulary Contract] | PASS / NOT-APPROVED: "[phrase]" — rewrite required | [full post-migration definition] |

Rules:
- Before State: enumerate actual type and nullability. "As-is" does not pass.
- Migration Operation: approved verb only. Disallowed phrases fire the Compliance cell.
- After State: independently readable — full definition, not just the delta.
- Unknown Before State: write "UNKNOWN — schema inspection required" and fire HALT PROTOCOL.

**Phase 2 gate:** Before advancing to Phase 3, verify that no Compliance cell reads NOT-APPROVED, and no Before State reads UNKNOWN without a fired HALT BLOCK. Gate: PASS or HALT.

---

### PHASE 3 — ANALYTICAL REVIEW

**Phase 3 entry:** Phase 2 gate = PASS.

Three roles in sequence: Operations (infrastructure), Commerce (domain), Finance (domain). Each role applies the full analysis structure to its domain entities.

**Per-entity analysis structure** (apply for each role's entities):

DATA LOSS: | Entity | Column | Loss Mechanism | Data at Risk | Severity |
CHECK: TYPE NARROWING / COLUMN DROP / LOSSY CAST / CASCADE DELETE / OVERWRITE BACKFILL
If none: explicit "None — [reasoning]"

CONSTRAINT VIOLATION: | Entity | Constraint Type | Pre-Migration Data Risk | Violation Likelihood | Severity |
CHECK: NOT NULL (existing nulls?), UNIQUE (duplicate values?), CHECK (out-of-range values?), FK (orphan rows?)
If none: explicit "No new or tightened constraints — [reasoning]"

DEFAULT VALUE GAP: | Entity | Column | Default Written to Existing Rows | Semantically Correct? | Domain Concern |
CHECK: empty strings on code fields, zero on financial totals, sentinel values on NOT NULL columns
If none: explicit "No new NOT NULL columns or changed defaults"

PERFORMANCE CLIFF: | Entity | Operation | Risk Type | Risk Level | Mitigation |
CHECK: full-table UPDATE backfill, DROP-CREATE index pair, ALTER COLUMN TYPE requiring rewrite, FK without concurrent index
Risk level: LOW / MEDIUM / HIGH. Mitigation required for MEDIUM and HIGH.

REVERSIBILITY: | Entity | Verdict | Rollback Path | Residual Consequence |
Verdict: REVERSIBLE / CONDITIONAL / IRREVERSIBLE

**Commerce-specific addition:** flag constraint violations for customer-visible failures and assign urgency.
**Finance-specific addition:** flag data loss paths for audit retention, regulatory archival, or period-close lock — CRITICAL severity by default.

**Phase 3 gate:** Before advancing to Phase 4, verify that every entity in the Phase 1 registry has entries in all five analysis sections for all applicable roles. Missing analysis section fires HALT PROTOCOL — responsible role: the role that owns that entity. Gate: PASS or HALT.

---

### PHASE 4 — CASCADE TRACE AND RISK SYNTHESIS

**Phase 4 entry:** Phase 3 gate = PASS.

**Minimum two cascade traces required. A Phase 4 section with one trace does not pass. Single-entity cascade entries do not satisfy this requirement.**

**CASCADE TRACE TABLE** (minimum two rows):

| Trace # | Source Entity / Column / Change | Impact Entity or Component | Impact Layer | Consequence | Mitigation Before Migration |
|---------|---------------------------------|---------------------------|-------------|-------------|----------------------------|
| 1 | | | SCHEMA / APPLICATION / ETL / VIEW / REPORTING | | |
| 2 | | | SCHEMA / APPLICATION / ETL / VIEW / REPORTING | | |

Requirement: at least one trace in the SCHEMA/APPLICATION, SCHEMA/ETL, or SCHEMA/VIEW layer — a pure SCHEMA/SCHEMA trace satisfies the count but does not satisfy the cross-layer requirement alone.

For each trace where the downstream component's schema state is unknown: fire HALT PROTOCOL — responsible role: Operations.

**RISK REGISTER:**

| Issue # | Issue | Entity | Source Phase | Severity | Likelihood | Remediation |
|---------|-------|--------|-------------|----------|------------|-------------|
| | | | Phase 3 / Phase 4 | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | |

One row per issue. All Phase 3 severity >= MEDIUM and all Phase 4 cascade consequences must have risk register entries.

**Phase 4 gate:** Verify cascade trace count >= 2 and at least one cross-layer trace present. Verify risk register covers all findings. Gate: PASS or HALT.

---
