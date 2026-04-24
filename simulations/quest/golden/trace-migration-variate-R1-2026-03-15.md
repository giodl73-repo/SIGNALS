# trace-migration Variate — Round 1
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-10, new rubric)
**Target criteria:** C-01 (entity enumeration), C-02 (before/after state documentation), C-03 (migration action tracing), C-04 (data loss path identification), C-05 (constraint violation identification)

---

## Round 1 Variation Map

| Variation | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | Notes |
|-----------|------|------|------|------|------|------|-------|
| V-01 | Role sequence | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Operations-first substrate declaration locks entity enumeration before domain roles analyze consequences; all five essentials addressed structurally |
| V-02 | Output format | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Table-first entity registry anchors C-01; per-row BEFORE/AFTER columns satisfy C-02; OPERATION column enforces C-03; dedicated DATA LOSS and CONSTRAINT columns enforce C-04/C-05 |
| V-03 | Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Explicit phase gates with coverage floors prevent silent omission; INVENTORY phase must close before BEFORE-STATE phase can open; each phase has a named required output |
| V-04 | Role sequence + Phrasing register | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | DIRECTIVE imperatives per role eliminate the most common omission path — a domain role skipping entities outside its vocabulary; DIRECTIVE language names failure modes explicitly |
| V-05 | Role sequence + Output format + Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Three-layer completeness: entity registry table (format) + INVENTORY phase floor (lifecycle) + Operations substrate declaration (role sequence) — any entity surviving one omission mechanism is caught by another |

---

## V-01 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Running Operations first forces entity enumeration to happen at the infrastructure level — from the schema itself — before domain roles apply their filters. Commerce and Finance experts naturally narrow their view to their domain entities; if they run first, they silently omit infrastructure-only entities (junction tables, index structures, sequence tables) that have no obvious Commerce or Finance owner. Operations runs first, enumerates every changed entity as a registry, and then all subsequent roles operate only within that registry. This prevents C-01 silent omission at the source. The sequential role constraint also enforces C-02 and C-03: each role produces before/after blocks and named operations for its assigned entities within the same registry, preventing the merged or ambiguous descriptions that cause C-02 failures.

---

You are running a migration trace signal for: {{topic}}

Role sequence: **Operations** runs first and declares the entity registry. **Finance** then analyzes its domain entities within that registry. **Commerce** analyzes last. No entity may appear in Finance or Commerce analysis unless it was first registered by Operations.

---

### OPERATIONS — SCHEMA MIGRATION EXPERT

You run first. Your job is to establish the ground truth of what changed. No domain role may add entities you did not register. No domain role may reference a table, view, index, or sequence that is not in your registry.

**Step 1 — ENTITY REGISTRY**

List every database object touched by this migration. For each object:

| Entity | Type | Change Class |
|--------|------|--------------|
| [name] | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER / PROCEDURE | ADDED / DROPPED / ALTERED / RENAMED |

Fill this table completely before continuing. If you are unsure whether an object was touched, include it and mark it POSSIBLE. Do not omit objects to keep the list clean — omission is a higher risk than false inclusion.

**Step 2 — PER-ENTITY ANALYSIS**

For each entity in your registry, produce the following analysis. Use the exact labels shown — do not merge sections or substitute synonyms.

---

**ENTITY: [name]**

BEFORE STATE:
Describe the exact schema state before the migration executes. List every column with its type, nullability, default value, and any constraints (NOT NULL, UNIQUE, CHECK, FK). List index names and their covered columns. Do not say "standard schema" or "no unusual constraints" — enumerate what is actually there. If you do not know the current state, state that explicitly and flag it as a gap requiring schema inspection before migration runs.

MIGRATION ACTION:
Name every DDL or DML operation this migration performs on this entity. Use explicit operation names from this set: ADD COLUMN, DROP COLUMN, ALTER COLUMN TYPE, ADD NOT NULL, DROP NOT NULL, ADD DEFAULT, DROP DEFAULT, ADD UNIQUE, DROP UNIQUE, ADD CHECK, DROP CHECK, ADD FOREIGN KEY, DROP FOREIGN KEY, DROP INDEX, CREATE INDEX, UPDATE (backfill), DELETE CASCADE, RENAME COLUMN, RENAME TABLE, TRUNCATE. At least one named operation is required per entity. The statement "column changes" or "schema updated" does not pass — name the operation.

AFTER STATE:
Describe the exact schema state after the migration completes. List the updated column definitions, changed constraints, and any new or dropped indexes. Label this section clearly as the post-migration state. BEFORE STATE and AFTER STATE must be independently readable — a reader who sees only AFTER STATE must be able to determine the final schema without reading BEFORE STATE.

DATA LOSS PATHS:
Identify every path where existing data could be destroyed, silently truncated, or changed in a non-reversible way. Check each of the following:
- Column drops: what data is permanently gone
- Type narrowing (e.g., TEXT to VARCHAR(64)): values over the length limit are truncated or the migration aborts
- Lossy casts (e.g., DECIMAL to INTEGER): fractional precision is discarded
- Cascaded deletes triggered by new or modified FK constraints: which child rows are deleted when parents are deleted
- Overwrite backfills: UPDATE statements that replace existing non-null values with a new default

If no data loss paths exist for this entity, state: "No data loss paths identified for [entity]. Reasoning: [explain why not]." Silence on this dimension does not pass.

CONSTRAINT VIOLATIONS:
Identify every constraint this migration adds or tightens and analyze whether the pre-migration data state would violate it. For each:
- NOT NULL added: are there rows with NULL in this column? If the table has any rows, assume yes unless you can verify otherwise.
- UNIQUE added: are there duplicate values in this column? Describe deduplication strategy or flag as unhandled.
- CHECK added: do existing rows satisfy the new condition? Identify any value ranges or formats that would fail.
- FK added: do all child values have matching parent rows? Identify orphan row risk.

If no constraints are added or tightened, state: "No new or tightened constraints for [entity]." Missing constraint analysis does not pass.

DEFAULT VALUE ANALYSIS:
For every new NOT NULL column, or any column whose DEFAULT changes: identify what value will be written to existing rows during backfill. Assess whether that value is semantically correct for the domain. Flag: empty strings on required code fields, zero amounts on financial totals, 1970-01-01 on dates that require a meaningful default, NULL-equivalent sentinels on columns that reject NULL.

PERFORMANCE CLIFF:
Identify operations on this entity that could cause table lock escalation, full-table scans, or index rebuilds. For each such operation: name it, assign a risk level (LOW / MEDIUM / HIGH), and provide a mitigation (batched UPDATE, online DDL flag, maintenance window scheduling). A HIGH risk operation with no mitigation proposed is a flag for the migration coordinator.

REVERSIBILITY:
State one verdict: REVERSIBLE / CONDITIONAL / IRREVERSIBLE. Rationale: what rollback requires. CONDITIONAL means rollback is possible but leaves a residual consequence (e.g., DROP COLUMN is reversible to re-ADD, but any data that was in the column is gone). IRREVERSIBLE means no migration path exists to the pre-migration state.

---

### FINANCE — MIGRATION IMPACT EXPERT

You analyze Finance domain entities from the Operations registry: ledger tables, transaction records, cost center schema, period-end views, audit trail structures, reconciliation tables.

You may only reference entities that appear in the Operations registry. If a Finance domain entity is missing from the registry, halt and report: "REGISTRY GAP: [entity] is a Finance domain entity affected by this migration but is not present in the Operations registry. Do not proceed until Operations registers this entity."

For each Finance domain entity in the registry, apply the same analysis structure: BEFORE STATE / MIGRATION ACTION / AFTER STATE / DATA LOSS PATHS / CONSTRAINT VIOLATIONS / DEFAULT VALUE ANALYSIS / PERFORMANCE CLIFF / REVERSIBILITY.

Finance-specific addition: for any data loss path on a Finance entity, flag whether the lost data is subject to audit retention, regulatory archival, or period-close lock requirements. These are CRITICAL severity by default regardless of row volume.

---

### COMMERCE — MIGRATION IMPACT EXPERT

You analyze Commerce domain entities from the Operations registry: product catalog tables, pricing structures, order schema, promotion rules, entitlement records, inventory tables.

You may only reference entities that appear in the Operations registry. If a Commerce domain entity is missing from the registry, report the registry gap before continuing.

For each Commerce domain entity in the registry, apply the same analysis structure: BEFORE STATE / MIGRATION ACTION / AFTER STATE / DATA LOSS PATHS / CONSTRAINT VIOLATIONS / DEFAULT VALUE ANALYSIS / PERFORMANCE CLIFF / REVERSIBILITY.

Commerce-specific addition: for any constraint violation on a Commerce entity, flag whether the violation would cause a customer-visible failure (checkout abort, catalog display error, entitlement gap) and assign an urgency level.

---

### CROSS-ENTITY DEPENDENCY CASCADE

After all three role analyses are complete, trace second-order effects:

1. For each FK added or dropped: trace the full cascade chain (parent → child → grandchild) and name every entity that inherits the migration's consequences.
2. For each dropped or renamed column: identify any views, stored procedures, application queries, or ETL jobs that reference that column and will break.
3. For each type change: identify application-layer code that formats or casts the column's value and will produce wrong output after migration.

Produce at least two end-to-end traces in the format:
[source entity / column / change] → [impact entity or component] → [consequence] → [mitigation before migration runs]

---

### RISK REGISTER

One row per identified issue. Every data loss path, constraint violation, performance cliff, irreversible operation, and cross-entity cascade must have an entry.

| Issue | Entity | Severity | Likelihood | Remediation |
|-------|--------|----------|------------|-------------|
| [description] | [table.column] | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | [action required before migration runs] |

Severity definitions: CRITICAL = data loss or migration abort on a non-empty production table; HIGH = silent data corruption or multi-minute table lock on a table touched by production traffic; MEDIUM = incorrect default values or broken non-critical views; LOW = dev-environment or cosmetic impact only.

---

## V-02 — Output Format

**Axis:** Output format
**Hypothesis:** A table-first format makes C-01 (entity enumeration) structurally unavoidable: the ENTITY REGISTRY TABLE is the first artifact produced, and its rows are the contract for everything that follows. Empty rows in a table are visually obvious in a way that missing prose sections are not — a reviewer can immediately see that an entity was registered but not analyzed. The per-column schema enforces C-02 and C-03 directly: BEFORE and AFTER are named columns, and OPERATION is a named column that requires a specific DDL verb. C-04 and C-05 are enforced as mandatory table columns in the per-entity detail table — absent entries are visually flagged as cells that were not filled, not as missing sections in unstructured prose.

---

You are running a migration trace signal for: {{topic}}

Produce all output in structured tables. Every entity, every finding, every risk must appear in a table row. Prose is permitted only in the NOTES column of a table or in hypothesis/rationale fields explicitly labeled as such.

---

### TABLE 1 — ENTITY REGISTRY

Enumerate every database object this migration touches. Fill this table completely before writing any other table.

| # | Entity | Type | Change Class | Owner Domain |
|---|--------|------|--------------|--------------|
| 1 | | TABLE / VIEW / INDEX / SEQUENCE | ADDED / DROPPED / ALTERED / RENAMED | Operations / Finance / Commerce / Shared |

Rules:
- Every entity that appears in any subsequent table must have a row here first.
- An entity that appears in analysis but not in this table is an enumeration gap.
- Change Class ALTERED requires a TABLE 2 row. Change Class ADDED or DROPPED requires a TABLE 2 row. Change Class RENAMED requires a TABLE 2 row.

---

### TABLE 2 — BEFORE / AFTER STATE

One row per column or constraint per entity. Do not merge multiple column changes into a single row.

| Entity | Object Name | Object Type | Before State | Migration Operation | After State | Change Reason |
|--------|-------------|-------------|-------------|---------------------|-------------|---------------|
| | | COLUMN / CONSTRAINT / INDEX / DEFAULT | [type, nullability, default, current constraint] | ADD COLUMN / DROP COLUMN / ALTER TYPE / ADD NOT NULL / DROP NOT NULL / ADD DEFAULT / ADD FK / DROP FK / ADD UNIQUE / CREATE INDEX / DROP INDEX / UPDATE backfill / DELETE CASCADE | [type, nullability, default, new constraint] | |

Rules for TABLE 2:
- Before State: must name the actual type and nullability, not "existing state" or "as-is."
- Migration Operation: must be a named DDL/DML operation from the list above. "Modified" or "changed" does not pass.
- After State: must be independently readable — state the full column definition, not just the delta.
- If Before State is unknown: write "UNKNOWN — schema inspection required before migration runs" and flag the row in TABLE 5.

---

### TABLE 3 — DATA LOSS ANALYSIS

One row per identified data loss path. If no loss paths exist for an entity, write one row with "None identified" and a brief reasoning note.

| Entity | Column / Object | Loss Mechanism | Data at Risk | Volume Estimate | Severity |
|--------|----------------|----------------|-------------|-----------------|----------|
| | | TYPE NARROWING / COLUMN DROP / LOSSY CAST / CASCADE DELETE / OVERWRITE BACKFILL / TRUNCATION | [description of what data is lost or at risk] | [estimated row count or % of table] | CRITICAL / HIGH / MEDIUM / LOW |

Loss Mechanism definitions:
- TYPE NARROWING: column type shrinks (TEXT → VARCHAR(64), DECIMAL(18,4) → INTEGER)
- COLUMN DROP: column and all its data is removed
- LOSSY CAST: type conversion that discards precision or changes value
- CASCADE DELETE: FK cascade removes child rows when parents change
- OVERWRITE BACKFILL: UPDATE replaces existing non-null values

---

### TABLE 4 — CONSTRAINT VIOLATION ANALYSIS

One row per new or tightened constraint. If no new constraints are added, write one row with "No new constraints" and state why.

| Entity | Constraint Name | Constraint Type | Pre-Migration Data Condition | Violation Path | Migration Response | Handled? |
|--------|----------------|-----------------|------------------------------|----------------|-------------------|----------|
| | | NOT NULL / UNIQUE / CHECK / FOREIGN KEY | [current data state: how many rows have null / duplicate / out-of-range values] | [rows that will fail when the constraint is enforced] | ABORT / DEFAULT INJECTION / BACKFILL / DEDUP REQUIRED / UNKNOWN | YES / NO / PARTIAL |

Handled = YES: migration script explicitly addresses the violation before applying the constraint.
Handled = NO: no remediation exists in the migration script.
Handled = PARTIAL: some cases handled, edge cases remain.

---

### TABLE 5 — DEFAULT VALUE GAP ANALYSIS

One row per new NOT NULL column or column with a changed DEFAULT.

| Entity | Column | New NOT NULL? | Default Value Applied | Backfill Target (rows) | Semantically Correct? | Risk |
|--------|--------|---------------|----------------------|------------------------|----------------------|------|
| | | YES / NO | [value that will be written to existing rows] | [estimated row count] | YES / NO / UNKNOWN | [describe semantic mismatch if NO or UNKNOWN] |

Semantically Correct = NO means: the default value will produce incorrect data. Example: 0 for a balance column where 0 means "paid in full," empty string for a required classification code where empty string fails downstream validation.

---

### TABLE 6 — PERFORMANCE CLIFF ANALYSIS

One row per operation that could cause lock escalation, full-table scan, or index rebuild.

| Entity | Operation | Table Size Estimate | Lock Type | Duration Estimate | Risk Level | Mitigation |
|--------|-----------|--------------------|-----------|--------------------|------------|------------|
| | ADD NOT NULL / UPDATE backfill / CREATE INDEX / DROP INDEX / ALTER TYPE | [rows] | ROW / PAGE / TABLE | [seconds / minutes on estimated size] | LOW / MEDIUM / HIGH | [batching strategy / online DDL / maintenance window] |

HIGH risk with no mitigation = migration coordinator must be notified before this runs in production.

---

### TABLE 7 — REVERSIBILITY ASSESSMENT

One row per entity.

| Entity | Verdict | Rollback Requires | Residual Consequence of Rollback | Time to Rollback |
|--------|---------|-------------------|----------------------------------|-----------------|
| | REVERSIBLE / CONDITIONAL / IRREVERSIBLE | [what the rollback script must do] | [what is left behind even after successful rollback] | [estimated duration] |

---

### TABLE 8 — CROSS-ENTITY DEPENDENCY CASCADE

One row per identified second-order effect.

| Source Entity | Source Change | Impact Entity / Component | Impact Type | Consequence | Mitigation |
|---------------|--------------|--------------------------|-------------|-------------|------------|
| | [DDL change] | [downstream table / view / procedure / ETL / app layer] | FK CASCADE / VIEW INVALIDATION / PROCEDURE BREAK / TYPE MISMATCH / ETL BREAK | [concrete failure after migration] | [action before migration runs] |

Minimum: two rows. If no cascades are identified, write two rows explaining why each major change class produces no downstream impact — do not leave this table empty.

---

### TABLE 9 — RISK REGISTER

One row per identified issue across all previous tables. This is the migration coordinator's action list.

| # | Issue Description | Source Table | Entity | Severity | Likelihood | Remediation Action | Owner |
|---|------------------|-------------|--------|----------|------------|-------------------|-------|
| | | TABLE 3 / 4 / 5 / 6 / 7 / 8 | | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | | Operations / Finance / Commerce / DBA / AppTeam |

Every CRITICAL and HIGH row requires a named Remediation Action. An issue in this register with "TBD" as its remediation is not complete.

---

## V-03 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** A migration has four distinct temporal states — the schema before the migration, the operations the migration performs, the schema after, and the risk consequences. Prompts that mix these phases in a single analytical pass produce merged descriptions that fail C-02 (before/after not clearly labeled) and C-03 (operations not distinguished from state). Enforcing explicit phase gates with coverage floors ensures each temporal state is documented separately and completely. The INVENTORY phase must close before the BEFORE STATE phase opens; the BEFORE STATE phase must close before the MIGRATION PHASE opens. Each phase has a required output floor — analysis may not proceed to the next phase until the current phase's floor is satisfied.

---

You are running a migration trace signal for: {{topic}}

This trace runs in five sequential phases. Each phase has a coverage floor. You may not begin a phase until the previous phase's floor is satisfied. Write each phase header as you enter it.

---

### PHASE 1 — INVENTORY
**Coverage floor: every changed entity is listed before this phase closes.**

List every database object this migration touches. For each:
- Name
- Object type (TABLE, VIEW, INDEX, SEQUENCE, TRIGGER, STORED PROCEDURE)
- Change class (ADDED, DROPPED, ALTERED, RENAMED)

No analysis yet — only enumeration. If you begin analysis before this list is complete, stop and return here.

**PHASE 1 GATE:** Count the entities in your list. Write: "PHASE 1 COMPLETE: [N] entities registered. Proceeding to PHASE 2."

If you cannot enumerate all entities because schema documentation is unavailable, write: "PHASE 1 INCOMPLETE: schema inspection required for [entity names]. Migration should not proceed until these are confirmed." Then halt.

---

### PHASE 2 — BEFORE STATE
**Coverage floor: every entity from PHASE 1 has a documented pre-migration state before this phase closes.**

For each entity registered in PHASE 1, document its current state before the migration executes.

**ENTITY: [name] — BEFORE STATE**

Document:
- Table columns: name, data type, nullable (YES/NO), default value (or none), any column-level CHECK constraint
- Table constraints: primary key, unique keys, foreign keys, table-level CHECK constraints — name each and describe its definition
- Indexes: name, columns covered, unique flag, partial condition if any
- Row volume estimate: approximate number of rows (this informs constraint violation and performance analysis in later phases)

Do not describe what will change — this phase captures only the current state.

**PHASE 2 GATE:** Confirm every entity from PHASE 1 has a BEFORE STATE block. Write: "PHASE 2 COMPLETE: before state documented for all [N] entities. Proceeding to PHASE 3."

---

### PHASE 3 — MIGRATION ACTIONS
**Coverage floor: every entity from PHASE 1 has at least one named migration operation before this phase closes.**

For each entity registered in PHASE 1, document what the migration does to it.

**ENTITY: [name] — MIGRATION ACTIONS**

For each operation the migration performs on this entity, write one operation block:

Operation: [ADD COLUMN / DROP COLUMN / ALTER COLUMN TYPE / ADD NOT NULL / DROP NOT NULL / ADD DEFAULT / DROP DEFAULT / ADD UNIQUE / DROP UNIQUE / ADD CHECK / DROP CHECK / ADD FOREIGN KEY / DROP FOREIGN KEY / DROP INDEX / CREATE INDEX / UPDATE (backfill: describe what the UPDATE sets) / DELETE CASCADE / RENAME COLUMN / RENAME TABLE]

Target: [column name / constraint name / index name]
Script fragment: [the actual DDL or DML statement, or a faithful paraphrase if the exact SQL is unavailable]

Do not blend operations. Each ADD COLUMN is a separate operation block. Each ALTER TYPE is a separate operation block.

**PHASE 3 GATE:** Confirm every entity has at least one named operation block. Write: "PHASE 3 COMPLETE: migration actions documented for all [N] entities. Proceeding to PHASE 4."

---

### PHASE 4 — AFTER STATE AND RISK IDENTIFICATION
**Coverage floor: every entity has a documented after state, a data loss assessment, and a constraint violation assessment before this phase closes.**

For each entity:

**ENTITY: [name] — AFTER STATE**
Document the entity's schema state after the migration completes. List all columns, constraints, and indexes in their post-migration form. This block must be independently readable — a reader must understand the final schema without consulting PHASE 2.

**ENTITY: [name] — DATA LOSS ASSESSMENT**
Assess each operation from PHASE 3 for data loss potential:
- DROP COLUMN: all data in [column] is permanently deleted. Affected rows: [N]. This loss is IRREVERSIBLE.
- ALTER COLUMN TYPE (narrowing): values exceeding [new limit] will be truncated or migration will abort. Risk rows: [describe range].
- UPDATE (backfill): existing non-null values in [column] will be replaced with [new value]. Prior values cannot be recovered after migration.
- DELETE CASCADE: rows in [child table] with [FK column] referencing deleted parents will be deleted. Estimated cascade rows: [N].

If no operation produces data loss: state "No data loss identified for [entity]. Reasoning: [all operations are additive / no existing data is overwritten or deleted / etc.]." Do not leave this section blank.

**ENTITY: [name] — CONSTRAINT VIOLATION ASSESSMENT**
Assess each new or tightened constraint from PHASE 3:
- For each NOT NULL added: query or estimate how many existing rows have NULL in this column. If any exist, the migration will fail or silently corrupt depending on the database's enforcement mode.
- For each UNIQUE added: assess whether duplicate values exist. If the table has any user-generated data, assume duplicates exist unless proven otherwise.
- For each CHECK added: assess whether existing rows satisfy the condition. Describe the violation range.
- For each FK added: assess whether all child values have a matching parent. Describe orphan row risk.

For new NOT NULL columns: also assess the DEFAULT value — see DEFAULT VALUE ASSESSMENT below.

**ENTITY: [name] — DEFAULT VALUE ASSESSMENT**
For each new NOT NULL column or changed DEFAULT:
- What value will be written to existing rows during backfill?
- Is that value semantically correct for the domain (Commerce / Finance / Operations)?
- Are there rows where this default would produce incorrect or misleading data?
- What is the count of affected rows?

**ENTITY: [name] — PERFORMANCE ASSESSMENT**
For each operation from PHASE 3 that touches a non-trivial table:
- Does it require a full-table scan or full-table rewrite? (ALTER TYPE on a non-nullable column typically does.)
- Does it acquire a table-level lock? (Most DDL operations in non-online mode do.)
- Does it trigger an index rebuild? (DROP INDEX + CREATE INDEX on a large table can take minutes to hours.)
- Assign: risk level LOW / MEDIUM / HIGH, estimated duration on a 100M-row table, and mitigation recommendation.

**ENTITY: [name] — REVERSIBILITY**
Verdict: REVERSIBLE / CONDITIONAL / IRREVERSIBLE
Rationale: what the rollback script must do and what residual consequence remains after rollback.

**PHASE 4 GATE:** Confirm every entity has AFTER STATE, DATA LOSS ASSESSMENT, CONSTRAINT VIOLATION ASSESSMENT, DEFAULT VALUE ASSESSMENT, PERFORMANCE ASSESSMENT, and REVERSIBILITY. Write: "PHASE 4 COMPLETE: all assessments documented for all [N] entities. Proceeding to PHASE 5."

---

### PHASE 5 — RISK SYNTHESIS
**Coverage floor: a risk register with one row per issue, and at least two cross-entity dependency traces.**

**CROSS-ENTITY DEPENDENCY CASCADE**

Trace second-order effects now that all per-entity analysis is complete:

1. For each FK added or dropped in PHASE 3: trace the cascade chain to every dependent entity. Name the cascade path end-to-end.
2. For each column dropped or renamed: name every view, procedure, ETL query, or application query that references this column and will break.
3. For each type change: name every downstream consumer (application layer, reporting layer, API response format) that casts or formats this column's value.

Minimum two end-to-end traces required. Format:
[source entity.column → change type] → [downstream entity / component] → [failure mode] → [pre-migration remediation]

**RISK REGISTER**

One row per identified issue from PHASE 4 assessments and the cascade analysis above.

| Issue | Source Phase | Entity | Severity | Likelihood | Remediation |
|-------|-------------|--------|----------|------------|-------------|
| | PHASE 4: DATA LOSS / CONSTRAINT / DEFAULT / PERFORMANCE / REVERSIBILITY · PHASE 5: CASCADE | | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | [action required before migration runs] |

**PHASE 5 GATE:** Confirm the risk register has one row per identified issue and at least two cascade traces. Write: "PHASE 5 COMPLETE. Migration trace signal complete."

---

## V-04 — Role Sequence + Phrasing Register

**Axis:** Role sequence + Phrasing register
**Hypothesis:** The most common failure mode for C-01 is a domain expert role skipping entities outside its vocabulary — a Finance expert who never considers the junction table between cost centers and projects because it has no "financial" name. Combining Operations-first role ordering with DIRECTIVE imperative language closes this gap at two levels: the role sequencing ensures Operations sees every entity before domain roles filter, and the DIRECTIVE phrasing names the failure mode explicitly ("do not omit entities because they have no [domain] owner — all entities in the registry are in scope"). DIRECTIVE language also eliminates hedged migration action descriptions: rather than "the column is modified," the DIRECTIVE specifies "name the DDL operation using a verb from the approved list; 'modified' is not an approved verb."

---

You are running a migration trace signal for: {{topic}}

DIRECTIVE: Follow role sequence exactly. Operations runs first. Finance runs second. Commerce runs third. No role may reference an entity that Operations did not register. No role may skip an entity in the registry because it appears to belong to another role's domain.

---

### OPERATIONS — SCHEMA MIGRATION EXPERT

DIRECTIVE A-1: Enumerate every database object this migration touches. Produce the ENTITY REGISTRY before any analysis begins. The registry is the contract for this trace — every subsequent role is bound by it.

**ENTITY REGISTRY**

| Entity | Type | Change Class |
|--------|------|--------------|
| | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER / PROCEDURE | ADDED / DROPPED / ALTERED / RENAMED |

DIRECTIVE A-2: Do not omit entities because they have no clear domain owner, because they are infrastructure-only, or because they are "unchanged in the migration." ALTERED includes partial changes. If a table gains a new index as a side effect of a constraint addition, that is an ALTERED entry. If a view is invalidated by a column rename, that view is an ALTERED entry.

---

DIRECTIVE A-3: For each entity in the registry, produce the following five fields in order. Do not merge fields. Do not reorder fields.

**ENTITY: [name]**

FIELD 1 — BEFORE STATE:
DIRECTIVE: Name every column with its exact type, nullability, default, and any column-level constraint. Name every table-level constraint: primary key, unique, foreign key, check. Name every index. Do not write "standard relational schema" or "no unusual configuration" — enumerate the actual structure. If you do not have access to the current schema definition, write: "BEFORE STATE UNKNOWN — schema inspection required. Migration must not run until this is confirmed."

FIELD 2 — MIGRATION OPERATION:
DIRECTIVE: Name the DDL or DML operation using a verb from this approved list only: ADD COLUMN, DROP COLUMN, ALTER COLUMN TYPE, ADD NOT NULL, DROP NOT NULL, ADD DEFAULT, DROP DEFAULT, ADD UNIQUE, DROP UNIQUE, ADD CHECK, DROP CHECK, ADD FOREIGN KEY, DROP FOREIGN KEY, DROP INDEX, CREATE INDEX, UPDATE (backfill), DELETE CASCADE, RENAME COLUMN, RENAME TABLE, TRUNCATE. If the migration performs multiple operations on this entity, list each as a separate line item. "Modified," "updated," "changed," "adjusted," and "migrated" are not approved verbs and do not pass.

FIELD 3 — AFTER STATE:
DIRECTIVE: Describe the entity's full schema state after the migration completes. This field must be independently readable — a reader who consults only FIELD 3 must understand the complete post-migration schema without reading FIELD 1. Do not write "as above, with [change]" — write the complete state.

FIELD 4 — DATA LOSS PATHS:
DIRECTIVE: Analyze every operation from FIELD 2 for data loss. For DROP COLUMN operations: the data is gone; state what it was and estimate row count. For TYPE NARROWING operations: values exceeding the new limit will be truncated or cause abort; state the truncation boundary. For UPDATE backfill operations: state what existing values are being overwritten and confirm whether pre-migration values are backed up. For DELETE CASCADE: trace which child tables lose rows and estimate count. If no operation in FIELD 2 produces data loss, write: "NO DATA LOSS PATHS: [operation list from FIELD 2] are all additive or schema-only changes that do not alter or remove existing data." Do not leave FIELD 4 blank for any entity.

FIELD 5 — CONSTRAINT VIOLATIONS:
DIRECTIVE: For every constraint in FIELD 2's operations that is new or tightened, analyze the pre-migration data state against it. NOT NULL added: are there NULL rows? Assume yes on any non-empty table unless proven otherwise. UNIQUE added: are there duplicate rows? Assess by distribution or assume yes on any user-generated column. CHECK added: do existing rows satisfy the condition? Assess by value range. FK added: do orphan rows exist? Assess by referential integrity state. For each violation path: state it, state the migration's response (abort / backfill required / undefined), and state whether the migration script handles it. If no constraints are added: write "NO NEW CONSTRAINTS — no constraint violation analysis required. Operations added: [list from FIELD 2]."

---

DIRECTIVE A-4: After completing all five fields for all Operations-domain entities, produce a PERFORMANCE AND REVERSIBILITY SUMMARY.

**OPERATIONS PERFORMANCE AND REVERSIBILITY SUMMARY**

For each entity, on one line:
[Entity] | [highest-risk operation] | [risk level: LOW / MEDIUM / HIGH] | [mitigation] | [reversibility verdict: REVERSIBLE / CONDITIONAL / IRREVERSIBLE]

---

### FINANCE — MIGRATION IMPACT EXPERT

DIRECTIVE B-1: You analyze Finance domain entities from the Operations registry only. Finance domain entities: ledger tables, transaction records, cost center schema, period-end views, audit trail structures, reconciliation tables, journal entry tables.

DIRECTIVE B-2: Do not add entities to the registry. If a Finance entity is missing from the Operations registry, write: "REGISTRY GAP — [entity] is a Finance domain entity affected by this migration but was not registered by Operations. Finance analysis halted until Operations registers this entity."

DIRECTIVE B-3: Apply all five FIELDS (BEFORE STATE / MIGRATION OPERATION / AFTER STATE / DATA LOSS PATHS / CONSTRAINT VIOLATIONS) to each Finance domain entity, using the same DIRECTIVE language as Operations. Finance-specific enforcement: any data loss path on a Finance entity where the lost data is subject to audit retention or regulatory archival is CRITICAL severity regardless of row volume. Name the regulation or audit requirement that applies.

DIRECTIVE B-4: Produce a Finance PERFORMANCE AND REVERSIBILITY SUMMARY using the same one-line format as Operations.

---

### COMMERCE — MIGRATION IMPACT EXPERT

DIRECTIVE C-1: You analyze Commerce domain entities from the Operations registry only. Commerce domain entities: product catalog tables, pricing structures, order schema, promotion rules, entitlement records, inventory tables, subscription tables.

DIRECTIVE C-2: Do not add entities to the registry. Report registry gaps before continuing.

DIRECTIVE C-3: Apply all five FIELDS to each Commerce domain entity. Commerce-specific enforcement: any constraint violation on a Commerce entity that would cause a customer-visible failure (checkout abort, catalog item disappearing, entitlement gap) is HIGH severity and requires a named remediation action before the migration runs.

DIRECTIVE C-4: Produce a Commerce PERFORMANCE AND REVERSIBILITY SUMMARY.

---

### CROSS-ENTITY DEPENDENCY CASCADE

DIRECTIVE D-1: After all role analyses, trace every second-order effect. For each dropped or renamed column, every FK change, and every type change, produce one trace in the format:

[source entity.column] → [operation: DROP / RENAME / TYPE CHANGE / FK CHANGE] → [downstream entity or component] → [failure mode] → [remediation required before migration]

DIRECTIVE D-2: Minimum two traces required. If fewer than two genuine cascades exist, explain in each trace why the operation does not cascade further — do not leave the section with fewer than two entries.

---

### RISK REGISTER

DIRECTIVE E-1: Produce one row per issue identified in any FIELD 4, FIELD 5, PERFORMANCE AND REVERSIBILITY SUMMARY, or cascade trace. Every identified issue must have a row. An issue without a row in this register is an incomplete trace.

| Issue | Entity | Role | Severity | Likelihood | Remediation | Owner |
|-------|--------|------|----------|------------|-------------|-------|
| | | Operations / Finance / Commerce | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | [specific action before migration runs] | DBA / AppTeam / Finance / Commerce |

DIRECTIVE E-2: Every CRITICAL row must have a specific, named remediation action. "Investigate further" and "confirm with team" do not pass as remediation actions at CRITICAL severity.

---

## V-05 — Role Sequence + Output Format + Lifecycle Emphasis

**Axis:** Role sequence + Output format + Lifecycle emphasis
**Hypothesis:** C-01 entity enumeration has three structural enforcement points in this variation: the ENTITY REGISTRY TABLE (format enforcement — gaps are empty rows, visually obvious), the INVENTORY PHASE gate (lifecycle enforcement — the phase cannot close until every entity is registered), and the Operations substrate declaration (role enforcement — Operations sees the schema first and cannot skip infrastructure-only entities). An entity that survives omission through one mechanism is caught by another. The same three-layer structure applies to C-02 and C-03: table columns force before/after separation, phases force temporal ordering, and Operations-first sequencing establishes the base state that all domain roles inherit. The full combination also surfaces inertia framing — the cost of not running this migration at all — as a structural element, which drives completeness by requiring the analyst to articulate what problem the migration solves before cataloguing what it risks.

---

You are running a migration trace signal for: {{topic}}

---

### INERTIA FRAME

Before any schema analysis begins, establish why this migration is happening. The inertia frame is not a risk section — it is the answer to: what does the current schema state cost if this migration never runs?

Complete this frame before the INVENTORY PHASE opens.

**CURRENT STATE COST**

| Dimension | Current Schema Condition | Ongoing Cost of Inaction |
|-----------|--------------------------|--------------------------|
| Data integrity | [what structural deficiency exists in the pre-migration schema] | [what continues to go wrong because of it] |
| Operations | [what operational burden the current schema creates] | [how that burden compounds over time] |
| Downstream | [what downstream consumers — Finance, Commerce, ETL — are affected by the current schema state] | [what breaks or degrades if migration is delayed] |

This frame sets the threshold against which every migration risk is measured. A risk that is smaller than the ongoing cost of inaction is a risk worth taking. A risk larger than the cost of inaction requires explicit sign-off.

---

### PHASE 1 — INVENTORY
**Phase gate: every changed entity registered before PHASE 2 opens.**

Role sequence: **Operations** runs the inventory. Finance and Commerce may not add entities — they may only flag registry gaps.

**TABLE 1 — ENTITY REGISTRY**

| # | Entity | Type | Change Class | Domain Affinity | PHASE 2 Assigned To |
|---|--------|------|--------------|-----------------|---------------------|
| | | TABLE / VIEW / INDEX / SEQUENCE / TRIGGER / PROCEDURE | ADDED / DROPPED / ALTERED / RENAMED | Operations / Finance / Commerce / Shared | Operations / Finance / Commerce |

Rules:
- Operations fills this table completely before Finance or Commerce review it.
- Domain Affinity is informational — it does not exempt an entity from analysis. Operations-affinity entities are analyzed by Operations, Finance-affinity by Finance, Commerce-affinity by Commerce. Shared entities are analyzed by all three.
- If Finance or Commerce identifies a missing entity: write a REGISTRY GAP flag as a table comment before proceeding. Do not proceed until Operations registers the missing entity.

**PHASE 1 GATE:** Write: "PHASE 1 COMPLETE — [N] entities registered: [list]. Opening PHASE 2."

---

### PHASE 2 — BEFORE STATE AND MIGRATION ACTIONS
**Phase gate: every entity has a BEFORE STATE row and at least one MIGRATION ACTION row before PHASE 3 opens.**

**TABLE 2 — BEFORE STATE**

| Entity | Column / Constraint / Index | Object Type | Type / Definition | Nullable | Default | Constraint Detail |
|--------|----------------------------|-------------|-------------------|----------|---------|------------------|
| | | COLUMN / CONSTRAINT / INDEX | [exact type or constraint definition] | YES / NO / N/A | [value or none] | [PK / UNIQUE / FK references / CHECK expression / INDEX columns] |

One row per structural element per entity. Do not summarize multiple columns into one row.

**TABLE 3 — MIGRATION ACTIONS**

| Entity | Operation | Target Object | Script Fragment | Execution Order |
|--------|-----------|--------------|-----------------|-----------------|
| | ADD COLUMN / DROP COLUMN / ALTER COLUMN TYPE / ADD NOT NULL / DROP NOT NULL / ADD DEFAULT / DROP DEFAULT / ADD UNIQUE / ADD CHECK / ADD FOREIGN KEY / DROP FOREIGN KEY / DROP INDEX / CREATE INDEX / UPDATE backfill / DELETE CASCADE / RENAME COLUMN / RENAME TABLE | [column name / constraint name / index name] | [DDL or DML statement] | [1, 2, 3 — order within the migration script] |

One row per operation per entity. Multiple operations on the same entity are separate rows with sequential Execution Order values.

**PHASE 2 GATE:** Confirm every entity from TABLE 1 has at least one row in TABLE 2 and at least one row in TABLE 3. Write: "PHASE 2 COMPLETE — before state and migration actions documented for all [N] entities. Opening PHASE 3."

---

### PHASE 3 — AFTER STATE
**Phase gate: every entity has an AFTER STATE row before PHASE 4 opens.**

**TABLE 4 — AFTER STATE**

Same schema as TABLE 2. Reflects post-migration state.

| Entity | Column / Constraint / Index | Object Type | Type / Definition | Nullable | Default | Constraint Detail |
|--------|----------------------------|-------------|-------------------|----------|---------|------------------|

Rules:
- Every row in TABLE 2 must have a corresponding row in TABLE 4 showing its changed or unchanged state.
- Rows dropped by the migration appear in TABLE 4 with a note in the Constraint Detail column: "DROPPED BY MIGRATION — no longer present."
- New rows added by the migration appear in TABLE 4 only (no TABLE 2 row for newly added objects).

**PHASE 3 GATE:** Confirm every entity from TABLE 1 has at least one row in TABLE 4. Write: "PHASE 3 COMPLETE — after state documented for all [N] entities. Opening PHASE 4."

---

### PHASE 4 — RISK IDENTIFICATION
**Phase gate: all five risk tables (DATA LOSS, CONSTRAINT, DEFAULT, PERFORMANCE, REVERSIBILITY) completed before PHASE 5 opens.**

**TABLE 5 — DATA LOSS PATHS**

| Entity | Column / Object | Loss Mechanism | Data at Risk | Volume Estimate | Severity | Mitigable? |
|--------|----------------|----------------|-------------|-----------------|----------|-----------|
| | | TYPE NARROWING / COLUMN DROP / LOSSY CAST / CASCADE DELETE / OVERWRITE BACKFILL / TRUNCATION | [description] | [rows] | CRITICAL / HIGH / MEDIUM / LOW | YES — [how] / NO |

If no loss paths for an entity: one row with Loss Mechanism = "NONE" and Data at Risk = "No data loss. Reasoning: [all operations are additive / column has no existing data / etc.]."

**TABLE 6 — CONSTRAINT VIOLATION ANALYSIS**

| Entity | Constraint | Constraint Type | Pre-Migration Violation Risk | Violation Count Estimate | Migration Handles It? | Response if Unhandled |
|--------|-----------|-----------------|-----------------------------|--------------------------|-----------------------|----------------------|
| | | NOT NULL / UNIQUE / CHECK / FOREIGN KEY | [description of current data state] | [rows at risk] | YES / NO / PARTIAL | ABORT / SILENT CORRUPTION / UNDEFINED |

If no new constraints: one row with Constraint Type = "NONE" and explanation.

**TABLE 7 — DEFAULT VALUE GAP ANALYSIS**

| Entity | Column | Default Applied | Backfill Rows Estimate | Semantically Correct? | Mismatch Description |
|--------|--------|----------------|----------------------|----------------------|----------------------|
| | | [value] | [N] | YES / NO / UNKNOWN | [describe mismatch if NO or UNKNOWN] |

Only rows where Migration Action = ADD COLUMN (NOT NULL) or ADD DEFAULT or DROP DEFAULT. If no such operations exist, write one row: "No new NOT NULL columns or DEFAULT changes in this migration."

**TABLE 8 — PERFORMANCE CLIFF ANALYSIS**

| Entity | Operation | Lock Type | Duration Estimate | Risk Level | Mitigation |
|--------|-----------|-----------|-------------------|------------|------------|
| | | ROW / PAGE / TABLE / NONE | [estimated duration at production scale] | LOW / MEDIUM / HIGH | [batching / online DDL / maintenance window / no mitigation needed] |

HIGH risk with no mitigation = migration coordinator alert required.

**TABLE 9 — REVERSIBILITY ASSESSMENT**

| Entity | Verdict | Rollback Script Required | Residual Consequence | Time to Rollback |
|--------|---------|--------------------------|----------------------|-----------------|
| | REVERSIBLE / CONDITIONAL / IRREVERSIBLE | [what the rollback does] | [what is left behind] | [estimated duration] |

**PHASE 4 GATE:** Confirm all five tables completed for all entities. Write: "PHASE 4 COMPLETE — risk identification done for all [N] entities. Opening PHASE 5."

---

### PHASE 5 — SYNTHESIS
**Phase gate: cross-entity cascade traces + risk register complete.**

**TABLE 10 — CROSS-ENTITY DEPENDENCY CASCADE**

| # | Source Entity | Source Change | Downstream Entity / Component | Impact Type | Failure Mode | Mitigation |
|---|--------------|--------------|-------------------------------|-------------|-------------|------------|
| | | [from TABLE 3] | | FK CASCADE / VIEW INVALIDATION / PROCEDURE BREAK / ETL BREAK / APP LAYER BREAK | [concrete post-migration failure] | [pre-migration action] |

Minimum two rows. If genuine cascades are fewer than two, fill remaining rows explaining why further cascades do not exist — explicitly, not by omission.

**TABLE 11 — RISK REGISTER**

Consolidate all findings from TABLES 5 through 10 into a single prioritized register.

| # | Issue | Source Table | Entity | Severity | Likelihood | Remediation | Owner | Status |
|---|-------|-------------|--------|----------|------------|-------------|-------|--------|
| | | TABLE 5–10 | | CRITICAL / HIGH / MEDIUM / LOW | CERTAIN / PROBABLE / POSSIBLE | [specific action before migration runs] | DBA / AppTeam / Finance / Commerce | OPEN / RESOLVED |

**INERTIA FRAME CLOSE**

Return to the Inertia Frame established at the start. For each row in the CURRENT STATE COST table, state whether the risks identified in this trace exceed the ongoing cost of inaction. Write one verdict per dimension:

| Dimension | Ongoing Cost of Inaction | Maximum Identified Risk | Migration Recommended? |
|-----------|--------------------------|------------------------|----------------------|
| Data integrity | [from opening frame] | [from TABLE 5 / 6] | YES / NO / CONDITIONAL |
| Operations | [from opening frame] | [from TABLE 8] | YES / NO / CONDITIONAL |
| Downstream | [from opening frame] | [from TABLE 10] | YES / NO / CONDITIONAL |

CONDITIONAL means: recommended only if specific remediations in TABLE 11 are completed first. Name those remediations.

**PHASE 5 GATE:** Write: "PHASE 5 COMPLETE. Migration trace signal complete. [N] entities analyzed, [N] risks registered, [N] risks open."
