Written to `simulations/quest/variations/trace-migration-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — trace-migration

**5 variations across 4 axes:**

| V | Primary Axis | Design Mechanism |
|---|---|---|
| **V-01** | Role sequence | Operations leads (risk triage) → Finance audits (data integrity) → Commerce closes (business impact naming). Each role gates the next. |
| **V-02** | Output format | Table-heavy — before/after state, data loss, NOT NULL risk, rollback class all as pre-printed columns. No prose escapes. |
| **V-03** | Lifecycle emphasis | Four explicit phase gates: PRE-FLIGHT / EXECUTE / VERIFY / ROLLBACK. Steps locked to their phase; cannot be grouped by type. |
| **V-04** | Phrasing register | 10 investigative questions. Model "interrogates" the migration script rather than fills a template. Tests richer C-02/C-03/C-08 at cost of C-05 reliability. |
| **V-05** | Full synthesis | Finance leads + pre-printed tables + phase gates + domain-impact section pre-printed *between* EXECUTE and VERIFY (forces C-08 before close). |

**Key design decisions across all five:**
- **C-02 (data loss explicit negative)** — each variation uses a different structural anchor: an Operations gate (V-01), a checkbox field (V-02/V-05), a phase-exit summary (V-03), a direct question (V-04)
- **C-05 (chronological ordering)** — V-03 is the strongest enforcer via phase gates; V-01/V-02 rely on "do not reorder" instructions; V-04 relies on question-ordering
- **C-08 (domain framing)** — V-05 is the hardest to skip: a dedicated domain-impact section sits between EXECUTE and VERIFY, cannot be deferred to a closing note

**Predicted ceiling:** V-05 — five structural mechanisms with no omission path for any essential criterion. V-03 is the closest single-axis competitor.
mechanism
  to force this: V-01 via role responsibility (Commerce closes), V-02 via a pre-printed
  "Business Consequence" column, V-03 via per-step domain annotation, V-04 via a
  direct question about real-world consequence, V-05 via a dedicated domain-impact section
  positioned between EXECUTE and VERIFY.

**Predicted ceiling:** V-05 — maximum structural coverage; all pre-printed fields leave no
omission path for C-02, C-04, C-07, C-08. V-03 is the closest competitor (phase gates enforce
C-05 and make C-06/C-07 per-step mandatory). V-01 tests whether role-responsibility alone
carries the essential criteria without structural templates.

---

## V-01: Role Sequence — Operations Leads, Finance Audits, Commerce Closes

**Axis:** Role sequence — Operations expert runs first as risk lead; Finance audits data
integrity per entity; Commerce closes with business impact naming. Each role's output gates
the next role.
**Hypothesis:** When Operations leads, the migration is immediately framed as an operational
risk problem (locks, replication lag, rollback windows) rather than a schema diff. Finance
then applies data integrity scrutiny to what Operations flagged. Commerce converts both into
named business consequences. This sequence ensures domain framing (C-08) is never treated
as an afterthought appended to a technical analysis.

```
You are running /trace-migration. Three domain experts analyze the migration in sequence.
Each expert completes their section before the next begins. Do not merge sections.

Inputs required before analysis begins:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Approximate row counts for affected tables (state "unknown" if not provided)
- Domain context (Commerce / Finance / Operations -- infer from table names if not stated)

If any input is missing, state what you inferred and why before proceeding.

---

## SETUP: MIGRATION PARSE

List every DDL statement in the migration, numbered in the order they appear in the script.
For each statement:
  Step N: [DDL statement type] on [table.column or table] -- [one-line description of what it does]

Do not reorder. Do not group by type. Execution order is locked here.

---

## OPERATIONS EXPERT: RISK TRIAGE

[Runs first. Focuses on operational hazards: lock duration, replication impact, rollback windows.]
[Complete this section before Finance begins.]

For each step from SETUP:

Step N -- Operational Risk:
  Lock class:      [ROW / TABLE / ACCESS EXCLUSIVE / SHARE / NONE]
  Lock duration:   [Instant / Row-count-dependent / Full-table rewrite required]
  Replication:     [Safe / Potential lag on replica / Replication-breaking DDL]
  Rollback window: [Before step: reversible / After step: reversible only from backup / Irreversible]
  Performance note: [Any table rewrite, index rebuild, or row scan on non-trivial table. State row count if known. Write "none" if not applicable.]

OPERATIONS VERDICT:
  Riskiest step: Step [N] -- [reason]
  Maintenance window required: YES / NO
  If YES: blocking step is Step [N] -- [specific reason why downtime is needed]
  Zero-downtime path: [Describe expand/contract or online DDL alternative, OR state "not available" with reason]

---

## FINANCE EXPERT: DATA INTEGRITY AUDIT

[Runs after Operations. Focuses on data correctness: before/after state, constraint satisfaction, data loss, missing defaults.]
[Complete this section before Commerce begins.]

For each changed entity (table or column that changes type, nullability, default, or constraint):

Entity: [table.column or table]
  Before:          [type | nullability | default | constraints]
  After:           [type | nullability | default | constraints]
  Existing data:   [Satisfies new constraint? YES / NO / UNKNOWN -- explain]
  Data loss risk:  [None / Truncation / Silent drop / Constraint rejection -- describe concretely]
  NOT NULL check:  [New NOT NULL added? YES/NO. If YES -- DEFAULT provided? YES/NO. If NO DEFAULT on non-empty table: FLAG AS RISK]

DATA LOSS SUMMARY:
  [List each data loss path found, OR write: "No data loss paths found. Reasoning: [explain why each destructive step either preserves data or raises an error rather than silently dropping it.]"]

CONSTRAINT VIOLATION SUMMARY:
  [For each new constraint (NOT NULL / UNIQUE / FK / CHECK): does existing data satisfy it? Name which records violate it and what the migration does -- fail, skip, or backfill.]
  [If no constraint changes: write "No constraint changes in this migration."]

IDEMPOTENCY AUDIT:
  [For each step: safe to run twice? If re-running would produce duplicate key errors, double-applied transforms, or other corruption -- flag the specific failure mode.]

---

## COMMERCE EXPERT: BUSINESS IMPACT NAMING

[Runs last. Converts Finance and Operations findings into named business consequences.]
[Silence on a risk found above is a failure -- every flagged risk must map to a business object.]

For each risk flagged by Finance or Operations:

Risk: [Step N or Entity -- description of the technical risk]
  Business object: [order / invoice / ledger entry / shipment / SKU / payment / refund / other]
  Consequence: [Concrete impact -- e.g., "refunds over $10k could be silently zeroed out" not "precision is reduced"]
  Severity: [CRITICAL / HIGH / MEDIUM / LOW]

MIGRATION VERDICT:
  Safe to run: YES / NO / CONDITIONAL
  If CONDITIONAL: [State prerequisite -- e.g., backfill required, maintenance window, review step N]
  Domain summary: [One sentence naming the highest-severity business risk in Commerce/Finance/Operations terms]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, riskiest_step, maintenance_window_required,
data_loss_found, constraint_violations_found, idempotent.
```

---

## V-02: Output Format -- Table-Heavy with Pre-Printed Columns

**Axis:** Output format -- before/after state, data loss risk, and rollback viability are all
pre-printed as table columns rather than prose fields; each changed entity gets exactly one row;
columns force the model to fill in each dimension without prose wrap.
**Hypothesis:** A pre-printed table column cannot be silently omitted the way a prose field
can. By placing "Data Loss Risk", "NOT NULL/DEFAULT Check", and "Rollback Class" as mandatory
columns in the entity table, every essential criterion has a structural home. The model must
produce a value for each column even if that value is "none" or "n/a" -- preventing the silent
omission failure mode that costs C-02 and C-04. Tests whether table density is a more reliable
C-01 to C-05 carrier than role-structured prose.

```
You are running /trace-migration. Produce a structured migration trace using the tables below.
All column headers are fixed. Do not omit, merge, or rename columns.
Fill every cell. Write "none" or "n/a" only when genuinely not applicable -- explain why.

Inputs:
- Migration script or before/after DDL
- Database engine
- Row counts for affected tables (state "unknown" if not provided)

---

## STEP 1: EXECUTION ORDER

List every DDL statement in order of execution. Do not reorder or group by type.

| # | Statement | Table | Object | What It Does |
|---|-----------|-------|--------|--------------|
| 1 | [DDL type] | [table] | [column or index or constraint] | [one line] |
| 2 | ...       | ...   | ...    | ...          |

---

## STEP 2: ENTITY STATE CHANGES

One row per changed column or table. Follow order from Step 1.

| Step # | Entity (table.column) | Before Type | Before Nullable | Before Default | After Type | After Nullable | After Default | Type Changed | Nullability Tightened |
|--------|-----------------------|-------------|-----------------|----------------|------------|----------------|---------------|--------------|----------------------|
| [N]    | [table.col]          | [type]      | YES/NO          | [value or none]| [type]     | YES/NO         | [value or none]| YES/NO      | YES/NO               |

---

## STEP 3: RISK MATRIX

One row per changed entity. Follow same order.

| Step # | Entity | Data Loss Risk | Data Loss Description | NOT NULL Added | DEFAULT Provided | NOT NULL Risk | Constraint Change | Existing Data Satisfies | Migration Handles Violation As |
|--------|--------|----------------|----------------------|----------------|------------------|---------------|------------------|------------------------|-------------------------------|
| [N] | [entity] | NONE / TRUNCATION / SILENT DROP / REJECTION | [describe concretely or "none"] | YES/NO | YES/NO | FLAG / CLEAR | [type or "none"] | YES / NO / UNKNOWN | FAIL / BACKFILL / SKIP / N/A |

DATA LOSS STATEMENT (required -- check exactly one):
[ ] No data loss paths found. [Reasoning -- explain why each destructive step raises an error rather than silently dropping data.]
[ ] Data loss paths found: [List each one.]

---

## STEP 4: OPERATIONAL RISK

One row per step from Step 1.

| Step # | Lock Class | Lock Duration | Full-Table Rewrite | Index Rebuild | Replication Risk | Performance Cliff | Row Count (if known) |
|--------|-----------|---------------|-------------------|---------------|-----------------|-------------------|----------------------|
| [N] | [NONE / ROW / TABLE / EXCLUSIVE] | [Instant / Row-count-dependent / Full-rewrite] | YES/NO | YES/NO | NONE / LAG / BREAKING | [describe or "none"] | [N rows or "unknown"] |

---

## STEP 5: ROLLBACK VIABILITY

One row per destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation, constraint drop).

| Step # | Operation | Rollback Class | Down Migration Exists | Backup Required | Notes |
|--------|-----------|---------------|----------------------|-----------------|-------|
| [N] | [operation] | REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE | YES/NO | YES/NO | [any qualifying note] |

If no destructive steps: write "No destructive steps in this migration."

---

## STEP 6: DOMAIN IMPACT

One row per risk rated TRUNCATION, SILENT DROP, FLAG, or HIGH/CRITICAL operational risk.

| Risk (Step #) | Technical Description | Business Object | Business Consequence | Domain | Severity |
|---------------|----------------------|-----------------|---------------------|--------|----------|
| [N] | [technical] | [order / invoice / ledger entry / shipment / other] | [concrete business consequence -- not generic db terminology] | Commerce / Finance / Operations | CRITICAL / HIGH / MEDIUM / LOW |

---

## STEP 7: ZERO-DOWNTIME AND IDEMPOTENCY

Zero-downtime assessment:
  Can migrate without downtime: YES / NO / PARTIAL
  If NO or PARTIAL: blocking step is Step [N] -- [specific reason]
  Alternative: [Expand/contract pattern description OR online DDL option OR "none available"]

Idempotency:
  Safe to run twice overall: YES / NO / PARTIAL
  Non-idempotent steps:
  | Step # | Failure Mode on Re-Run |
  |--------|------------------------|
  | [N]    | [e.g., duplicate key error, double-applied transform] |
  (If all steps are idempotent: write "All steps idempotent.")

---

## VERDICT

  Migration risk: LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window: REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run: YES / NO / CONDITIONAL
  Highest-severity business risk: [One sentence in Commerce/Finance/Operations terms]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, step_count, data_loss_found, maintenance_window,
idempotent, highest_severity.
```

---

## V-03: Lifecycle Emphasis -- Explicit Phase Gates

**Axis:** Lifecycle emphasis -- the migration trace is structured into four mandatory phases
(PRE-FLIGHT / EXECUTE / VERIFY / ROLLBACK); each phase has an explicit gate condition that
must be satisfied before the next phase begins; steps can only appear within the phase where
the database engine would execute them.
**Hypothesis:** Forcing the model to assign each migration step to a named execution phase
(rather than describing the migration as a flat list) structurally enforces C-05 (chronological
order) and naturally surfaces C-06 (performance cliffs are visible at their phase boundary)
and C-07 (rollback viability is a first-class ROLLBACK phase artifact). If a step is in the
wrong phase, the reader immediately sees the error. The phase-gate mechanism should produce
the highest C-05 reliability of any single-axis variation.

```
You are running /trace-migration. Trace the migration across four execution phases.
Assign every step to exactly one phase. Phase boundaries are gates -- complete each phase before
writing the next. Steps may not be grouped by type or table; they must appear in execution order
within their phase.

Phases:
  PRE-FLIGHT  -- checks and guards run before the first DDL statement
  EXECUTE     -- DDL and DML statements in the order the engine applies them
  VERIFY      -- post-migration checks that confirm the schema and data are in the expected state
  ROLLBACK    -- what must happen to undo this migration if VERIFY fails

Inputs required:
  - Migration script or before/after DDL
  - Database engine (PostgreSQL / MySQL / SQL Server / other)
  - Row counts for affected tables (state "unknown" if not provided)
  - Domain context (infer from table names if not stated)

---

## PHASE 0: PARSE

List every statement from the migration script in order. Number them.
This list is the authoritative execution sequence. All downstream phases reference it by step number.

Step 1: [statement type] -- [table.object] -- [what it does]
Step 2: ...

Affected entities (tables or columns that change state):
  [List each entity that has a before/after state change]

---

## PRE-FLIGHT GATE

Complete this section before writing any EXECUTE phase content.

PRE-FLIGHT checks:
  [ ] Before-state documented for every affected entity (required for EXECUTE phase to open)
  [ ] Row counts noted or marked "unknown"
  [ ] Constraint changes identified (NOT NULL / UNIQUE / FK / CHECK additions or removals)
  [ ] NOT NULL additions checked for DEFAULT presence

Before-state snapshot (one entry per affected entity):
  Entity: [table.column or table]
    Type:        [current type]
    Nullable:    YES / NO
    Default:     [value or "none"]
    Constraints: [list or "none"]
    Row count:   [N or "unknown"]

NOT NULL + DEFAULT check:
  [For each new NOT NULL column: does a DEFAULT exist? If NO DEFAULT on non-empty table -- write:
   "RISK: [table.column] -- NOT NULL with no DEFAULT on table with [N or unknown] rows. Migration will fail or require backfill."]
  [If no new NOT NULL columns: write "No new NOT NULL columns."]

PRE-FLIGHT GATE: OPEN / BLOCKED
  [If BLOCKED: state which check failed and what must be resolved before EXECUTE begins.]

---

## EXECUTE PHASE

[PRE-FLIGHT GATE must be OPEN before this section begins.]
[Trace each step in execution order. Each step entry is complete before moving to the next.]

Step N -- [statement type] on [table.object]:
  After-state:
    Type:        [new type or "unchanged"]
    Nullable:    YES / NO (changed from: YES/NO)
    Default:     [new value or "unchanged" or "removed"]
    Constraints: [new constraints or "unchanged"]
  Data loss risk:   NONE / TRUNCATION / SILENT DROP / CONSTRAINT REJECTION
    [If not NONE: describe concretely -- which rows, which values, what happens to them]
    [If NONE: one sentence explaining why data is preserved or errors rather than drops]
  Performance cliff: NONE / PRESENT
    [If PRESENT: lock class, lock duration, rewrite scope, row count if known]
  Domain note: [Name a business object affected -- order, invoice, ledger entry, shipment.
                State the concrete consequence. Write "N/A" only if no business data touches
                this column -- explain why.]

[Repeat for each step in order.]

EXECUTE SUMMARY:
  Data loss paths found: YES / NO
    [If YES: list each path.]
    [If NO: "No data loss paths found. Each destructive step either raises an error or
     is a no-op on existing data because: [reasoning per step]."]
  Constraint violations: YES / NO / UNKNOWN
    [If YES: name which records violate each new constraint and how the migration handles it.]

---

## VERIFY PHASE

[List checks that would confirm the migration succeeded. These run after EXECUTE completes.]
[At minimum: one check per constraint change, one check per data type change.]

Check N: [What to verify] -- [How to verify it] -- [Expected result]
  Example: Check row counts match before/after for any table with DROP COLUMN.
  Example: Confirm no NULL values exist in newly NOT NULL column.
  Example: Confirm FK references resolve for any new FK constraint.

---

## ROLLBACK PHASE

[What must happen to undo the migration. Ordered in reverse execution order.]
[Classify each destructive step from EXECUTE phase.]

Step N -- Rollback assessment:
  Operation:      [original DDL from EXECUTE]
  Rollback class: REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
  Down migration: [DDL to reverse this step, OR "not possible -- data is gone"]
  Notes:          [any qualifying condition -- e.g., "reversible only before EXECUTE step N+2"]

ROLLBACK SUMMARY:
  Any irreversible steps: YES / NO
    [If YES: name each and state what is permanently lost.]
  Recommended rollback window: [Time window within which rollback is still viable, OR "none -- irreversible steps present"]

---

## ZERO-DOWNTIME AND IDEMPOTENCY

Zero-downtime:
  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] -- [specific DDL and why it requires a maintenance window]
    Alternative:   [Expand/contract pattern, OR online DDL option for this engine, OR "none available -- explain"]

Idempotency:
  Overall: IDEMPOTENT / NOT IDEMPOTENT / PARTIALLY IDEMPOTENT
  Non-idempotent steps:
    Step [N]: [failure mode if run twice -- e.g., duplicate key, double-applied transform]
  [If all idempotent: write "All steps safe to run twice."]

---

## MIGRATION VERDICT

  Risk level:           LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:   REQUIRED / NOT REQUIRED / CONDITIONAL
  Reversibility:        FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Highest business risk: [One sentence -- name a business object, state a concrete consequence]
  Safe to run:          YES / NO / CONDITIONAL (state condition)

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, phase_count, data_loss_found, irreversible_steps,
maintenance_window, idempotent, highest_risk_step.
```

---

## V-04: Phrasing Register -- Investigative/Conversational

**Axis:** Phrasing register -- the prompt is structured as a directed interrogation of the
migration script; each section opens with a question the model must answer before proceeding;
imperative "fill in this template" instructions replaced with "answer this question precisely"
framing.
**Hypothesis:** Investigative phrasing activates a more analytical reasoning mode than template-
filling does. When the model is asked "what would happen to an existing row with amount = 99999.99
if you ran this migration?" it is more likely to reason through the actual data path than when
it is asked to "fill in the Data Loss Risk column." Tests whether question-driven prompting
produces richer C-02, C-03, and C-08 content at the cost of C-05 structural reliability (since
questions do not enforce chronological ordering as strongly as phase gates).

```
You are running /trace-migration. Answer each question below precisely and in order.
Do not skip a question. If you cannot answer with certainty, state what you know and what you
are inferring, then give your best answer with a confidence level.

Before you begin: read the migration script. Identify every DDL statement. Number them in the
order they appear. Keep that list in front of you -- every answer below must reference step numbers.

---

QUESTION 1: What does this migration do, in one sentence per step?

List each step in execution order (not grouped by type or table).
  Step 1: ...
  Step 2: ...
  [Continue for all steps.]

---

QUESTION 2: For each entity that changes, what does it look like before and after?

Answer per entity. Cover every column or table that changes type, nullability, default, or
constraints.

  Entity: [table.column or table]
  Before: [type, nullable, default, constraints]
  After:  [type, nullable, default, constraints]
  What changed: [one sentence]

---

QUESTION 3: Could any existing row lose data silently -- without an error being raised?

For each step that modifies existing data (type changes, precision reductions, column drops,
row deletes): trace what happens to a row that is already in the table.

  - If a value is truncated: what value would be lost? What would remain?
  - If a column is dropped: is the data recoverable after this step?
  - If the answer is "no data is lost": explain why -- does it error instead? Is the table empty?
    Is the precision change lossless for values in the actual domain?

End with: "Data loss paths found: [list] / No data loss paths found: [brief argument]."

---

QUESTION 4: Does any existing row violate a new constraint added by this migration?

For each new NOT NULL, UNIQUE, FK, or CHECK constraint:
  - Is it possible for an existing row to violate it?
  - If yes: how many rows approximately, and what does the migration do -- fail the whole migration,
    skip the row, or backfill a default?
  - If no: why not? (Table is empty? Existing data already satisfies it? The constraint only
    applies to new inserts?)

---

QUESTION 5: Is there any new NOT NULL column without a DEFAULT value on a non-empty table?

For each NOT NULL addition: state whether a DEFAULT is provided.
  If no DEFAULT on a non-empty table: "RISK -- [table.column]: adding NOT NULL with no DEFAULT
  will fail on [engine] unless the table is empty or a backfill runs first."
  If all NOT NULL additions have defaults, or the table is empty: say so.

---

QUESTION 6: Which steps will be slow on a large table, and why?

For each step that involves a full-table rewrite, index rebuild, or row-by-row scan:
  - Name the table and the approximate row count (state "unknown" if not provided).
  - Describe the specific performance risk: lock duration, I/O spike, replication lag, temp space.
  - If the migration only touches empty or small tables: say so and note that C-06 auto-passes.

---

QUESTION 7: If this migration fails halfway through, what can be recovered?

For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation):
  Answer: is this step reversible?
  a) Fully reversible -- a down migration can undo it.
  b) Reversible only from backup -- the data is gone from the live DB but can be restored.
  c) Irreversible -- the data is gone with no recovery path.

State your classification and the specific DDL that would reverse it (if any).

---

QUESTION 8: What is the real-world consequence for the business if the riskiest step goes wrong?

Pick the step you identified as highest-risk. Name:
  - A concrete business object it affects: order, invoice, ledger entry, shipment, SKU, refund,
    payment, subscription, or equivalent.
  - A specific consequence stated in business terms -- not database terminology.
    Bad: "decimal precision is reduced."
    Good: "invoices with amounts over $9,999,999.99 would be silently capped at that value,
    causing revenue recognition errors on large enterprise contracts."
  - Who would notice first and how: customer complaint, financial audit, reconciliation mismatch.

---

QUESTION 9: Can this migration run without a maintenance window?

Consider: does any step require an ACCESS EXCLUSIVE lock, a full-table rewrite, or a blocking
schema change that prevents reads or writes during execution?
  - If yes: name the specific step and explain why it blocks traffic.
  - If the engine supports online DDL for this operation (e.g., PostgreSQL CONCURRENTLY,
    MySQL InnoDB instant DDL, SQL Server online index rebuild): describe the alternative.
  - If no step requires downtime: say so and explain why.

---

QUESTION 10: Is this migration safe to run twice?

For each step: would running it a second time produce an error, corrupt data, or produce a
different result than the first run?
  - If non-idempotent: name the specific failure mode (duplicate key violation, double-applied
    data transform, constraint already exists error, etc.).
  - If idempotent: confirm why (IF NOT EXISTS guards, UPSERT semantics, pure schema metadata
    changes that are no-ops on re-run).

---

FINAL VERDICT

Migration risk:           LOW / MEDIUM / HIGH / CRITICAL
Safe to run now:          YES / NO / CONDITIONAL
Maintenance window:       REQUIRED / NOT REQUIRED / CONDITIONAL
Reversibility:            FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE
One-sentence summary:     [State the highest-stakes risk in plain language a domain expert
                           would use in a change-control review.]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, data_loss_found, constraint_violations_found,
idempotent, maintenance_window, risk_level.
```

---

## V-05: Full Synthesis -- Finance Leads + Tables + Phase Gates + Domain Section Pre-Printed

**Axis:** Full synthesis -- Finance expert leads (data integrity as primary concern); before/after
state and risk are pre-printed table columns; execution is structured into phase gates; a dedicated
domain-impact section is pre-printed between EXECUTE and VERIFY to prevent it from being
appended as an afterthought.
**Hypothesis:** Maximum structural coverage. Finance leadership ensures data correctness is
the root frame, not an audit on top of a schema diff. Pre-printed table columns prevent silent
omission of C-02, C-04, and C-07. Phase gates enforce C-05 chronological ordering. A dedicated
domain-impact section between EXECUTE and VERIFY forces C-08 to be populated before the model
closes the analysis -- it cannot be skipped. Tests whether five structural mechanisms in combination
produce a more reliable output than any single mechanism alone, without making the prompt so
rigid that it fails on unusual migration shapes.

```
You are running /trace-migration. Finance expert leads this analysis -- data integrity is the
primary concern. Schema correctness, data loss, and constraint satisfaction are assessed first.
Operational risks and business impact follow.

All section headers, table column headers, and pre-printed fields are fixed.
Do not omit, merge, or rename them. Fill every cell. Write "none" only when genuinely not
applicable and explain why.

Inputs required:
  - Migration script or before/after DDL
  - Database engine
  - Row counts for affected tables (state "unknown" if not provided)
  - Domain context (infer from table names if not stated)

---

## PARSE: EXECUTION SEQUENCE

[Finance expert locks the execution order before any analysis begins.]
[Do not reorder. Do not group. Execution order from the script is authoritative.]

| Step # | DDL Type | Table | Object (column/index/constraint) | Operation Summary |
|--------|---------|-------|----------------------------------|-------------------|
| 1 | [type] | [table] | [object] | [one line -- what the engine does] |
| 2 | ... | ... | ... | ... |

---

## PRE-FLIGHT GATE (Finance)

Complete before EXECUTE phase opens.

Before-state per affected entity:

| Entity (table.column) | Current Type | Nullable | Default | Constraints | Row Count |
|-----------------------|-------------|---------|---------|-------------|-----------|
| [table.col] | [type] | YES/NO | [value or none] | [list or none] | [N or unknown] |

NOT NULL + DEFAULT audit:
  [For each new NOT NULL column added to an existing table:]
  [ ] [table.column] -- DEFAULT provided: YES / NO
      [If NO: "RISK: NOT NULL with no DEFAULT on [N or unknown] rows. Will fail unless table is empty or backfill precedes this step."]
  [If no new NOT NULL columns: "No new NOT NULL columns -- NOT NULL risk clear."]

PRE-FLIGHT GATE: OPEN / BLOCKED
  [BLOCKED if: any entity before-state is missing, or NOT NULL risk is unresolved without a plan.]

---

## EXECUTE PHASE (Finance + Operations)

[PRE-FLIGHT GATE must be OPEN.]
[Finance traces data state; Operations annotates each step with operational risk.]
[Steps appear in execution order from PARSE. Do not reorder.]

### Entity State Changes

| Step # | Entity | After Type | After Nullable | After Default | Type Changed | Nullability Tightened | Constraint Added |
|--------|--------|-----------|----------------|---------------|-------------|----------------------|-----------------|
| [N] | [table.col] | [type] | YES/NO | [value or none] | YES/NO | YES/NO | [type or none] |

### Data Loss and Constraint Risk

| Step # | Entity | Data Loss Risk | Data Loss Description | Constraint Change | Existing Data Satisfies | Migration Handles Violation As |
|--------|--------|---------------|----------------------|-------------------|------------------------|-------------------------------|
| [N] | [entity] | NONE / TRUNCATION / SILENT DROP / REJECTION | [describe or "none"] | [type or "none"] | YES / NO / UNKNOWN | FAIL / BACKFILL / SKIP / N/A |

DATA LOSS STATEMENT (required -- check exactly one):
[ ] Data loss paths found: [List each path. Name the column, the value range at risk, and what happens to it.]
[ ] No data loss paths found. Reasoning: [For each destructive step, explain why data is preserved or surfaced as an error rather than silently dropped.]

### Operational Risk per Step

| Step # | Lock Class | Lock Duration | Full-Table Rewrite | Replication Risk | Performance Cliff Description | Rows Affected |
|--------|-----------|---------------|-------------------|-----------------|------------------------------|---------------|
| [N] | [NONE/ROW/TABLE/EXCLUSIVE] | [Instant/Row-count-dependent/Full-rewrite] | YES/NO | NONE/LAG/BREAKING | [describe or "none"] | [N or unknown] |

---

## DOMAIN IMPACT (Commerce / Finance / Operations)

[Runs immediately after EXECUTE -- before VERIFY. Pre-printed section prevents domain framing
from being omitted or deferred to a closing note.]
[One row per risk rated TRUNCATION, SILENT DROP, or performance cliff.]
[A passing row must name a concrete business object -- generic database terminology fails.]

| Step # | Technical Risk | Business Object | Business Consequence | Domain | Severity |
|--------|---------------|-----------------|---------------------|--------|----------|
| [N] | [technical description] | [order/invoice/ledger entry/shipment/SKU/refund/payment] | [concrete consequence in domain terms -- not generic db language] | Commerce/Finance/Operations | CRITICAL/HIGH/MEDIUM/LOW |

[If no data loss or performance risks were found in EXECUTE: write "No domain-level risks to surface -- migration is data-safe and performant." Do not leave this section blank.]

---

## VERIFY PHASE

[Checks that confirm the migration succeeded. Run after EXECUTE completes.]

| Check # | What to Verify | How to Verify | Expected Result |
|---------|---------------|---------------|----------------|
| 1 | [e.g., No NULLs in new NOT NULL column] | [e.g., SELECT COUNT(*) WHERE col IS NULL] | [0 rows] |
| 2 | [e.g., FK references resolve] | [JOIN query] | [0 orphaned rows] |
| [N] | ... | ... | ... |

---

## ROLLBACK PHASE

[Reverse execution order. Classify each destructive step.]

| Step # | Original Operation | Rollback Class | Down Migration DDL | Notes |
|--------|-------------------|---------------|-------------------|-------|
| [N] | [DDL from EXECUTE] | REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE | [DDL to reverse, or "not possible"] | [qualifying condition if any] |

[If no destructive steps: "No destructive steps -- migration is fully reversible by re-running down migration."]

ROLLBACK SUMMARY:
  Irreversible steps: YES / NO
    [If YES: name each and state what is permanently lost.]

---

## ZERO-DOWNTIME AND IDEMPOTENCY

Zero-downtime:
  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] -- [DDL and specific reason -- lock type, table size, engine behavior]
    Alternative: [Expand/contract pattern, OR online DDL for this engine, OR "none available -- explain why"]

Idempotency:
  | Step # | Idempotent | Failure Mode if Run Twice |
  |--------|-----------|--------------------------|
  | [N] | YES/NO | [e.g., duplicate key error / "safe -- CREATE TABLE IF NOT EXISTS"] |

---

## VERDICT

  Migration risk:           LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:       REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run:              YES / NO / CONDITIONAL
  Reversibility:            FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Idempotent overall:       YES / NO / PARTIAL
  Highest business risk:    [One sentence -- name a business object, state a concrete consequence,
                             quantify if possible (e.g., "orders over $X silently capped")]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found,
constraint_violations_found, irreversible_steps, maintenance_window, idempotent,
highest_severity, highest_risk_step.
```
