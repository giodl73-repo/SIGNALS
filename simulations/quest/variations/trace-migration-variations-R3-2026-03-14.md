Written to `simulations/quest/variations/trace-migration-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — trace-migration

**5 complete variations targeting v3 rubric (130 pts, C-01 to C-16):**

| V | Axis | Primary Mechanism | Predicted |
|---|------|-------------------|-----------|
| **V-01** | C-14 focus | "(BINARY FIELD)" type annotation at every definition site: column headers, section labels, inline labels | 120 |
| **V-02** | C-15 focus | Cascading OPEN/BLOCKED gate chain — each downstream phase header names its prerequisite gate as a structural condition | 120 |
| **V-03** | C-16 focus | Two-phase with Phase A C-11 fix: every question explicitly instructs "reference each step by its Step N from Q1" | 120 |
| **V-04** | C-14 + C-15 | Type annotations + binary gates, single-phase. Field-level type integrity + phase-level sequencing. | 125 |
| **V-05** | Full v3 synthesis | C-14 + C-15 + C-16: type annotations in both phases + binary gates in Phase B + two-phase with citation discipline | 130 |

**Key design decisions:**
- **V-01 vs V-03 R2 (prior C-13 focus):** V-03 R2 used "BINARY FIELD" labels in instruction text. V-01 R3 puts them in column headers themselves — the annotation travels with the definition site.
- **V-02 vs V-02 R2:** R2 had one DOMAIN GATE. V-02 R3 cascades five gates (PRE-FLIGHT, EXECUTE, DOMAIN IMPACT, VERIFY, ROLLBACK) each blocking its downstream phase header.
- **V-03 C-11 fix is surgical:** Every Phase A question (Q2-Q10) adds "reference each step by its Step N from Q1" — this is the exact residual from V-04 R2's 3/5 C-11 score.
- **V-04 non-redundance:** C-14 enforces at field level; C-15 enforces at phase level. Neither requires two-phase structure. 125/130 predicted with C-16 as the isolated gap.
- **V-05 130/130 path:** Phase A step-citation (C-11 + C-16) + Phase B type annotations (C-14) + Phase B gates (C-15).
anized by concern allowed models to re-describe steps by name without citing "Step N." Fix: every Phase A question explicitly instructs "reference each step by its Step N from Q1." Tests whether the citation instruction alone closes the C-11 gap.
- **V-04 combination** -- single-phase with both C-14 (type annotations) and C-15 (binary gates + downstream-header prerequisites). Two enforcement layers without two-phase structure. Tests whether C-14+C-15 alone reaches 125/130.
- **V-05 synthesis** -- two-phase with type annotations in both phases and binary gates in Phase B. Should produce 130/130.

---

## V-01: C-14 Focus -- Type Annotation at Every Definition Site

**Axis:** C-14 -- critical fields carry an explicit structural type annotation at every definition site: column headers, section labels, inline field labels. The annotation "(BINARY FIELD)", "(BINARY)", or "(FIXED TAXONOMY)" names the structural class of the expected value wherever the field is defined -- not just where the value is filled in.

**Hypothesis:** When "(BINARY FIELD)" appears in the column header itself, a model filling that column with free-form prose has a visible type mismatch at the column level. The label converts the formatting convention into a structural contract. Repeated at every occurrence (section header, column name, inline label), it closes the drift path that a label-only-at-first-introduction leaves open.

```
You are running /trace-migration.

Role: Commerce / Finance / Operations migration expert.
Task: Trace a schema migration step by step. For each changed entity: what data exists
before, what the migration does to it, what the state is after. Identify data loss paths,
nullable violations, missing defaults, and performance cliffs.

Inputs required before analysis begins:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

Type annotation convention used throughout this template:
  (BINARY FIELD)    -- value must be one of exactly two options (e.g., YES/NO, CLEAR/AT RISK)
  (BINARY)          -- same as BINARY FIELD, used inline
  (FIXED TAXONOMY)  -- value must be chosen from a named enumerated set

These annotations appear at every definition site: column headers, section labels, inline labels.
A response at a "(BINARY FIELD)" site that uses free-form prose is a type error, not an omission.

---

## SECTION 0: STEP REGISTRY (AUTHORITATIVE ARTIFACT)

Number every DDL statement in execution order. All downstream sections reference steps by number.

| Step # | DDL Type | Table | Object | What It Does (one line) |
|--------|---------|-------|--------|------------------------|
| 1 | [type] | [table] | [column/index/constraint] | [description] |
| 2 | ... | ... | ... | ... |

---

## SECTION 1: BEFORE-STATE SNAPSHOT

For each entity modified by a step in the registry, document its state before the migration.
Reference each entry by step number from SECTION 0.

**Step N -- [table.column or table] (referenced by Step N from registry):**
  Type:                              [current type]
  Nullable:                          YES / NO
  Default:                           [value or "none"]
  Constraints:                       [list or "none"]
  Row count:                         [N or "unknown"]
  NOT NULL RISK (BINARY FIELD):      CLEAR / AT RISK / N/A
    -- CLEAR: step does not add NOT NULL, or table is empty, or DEFAULT is provided
    -- AT RISK: step adds NOT NULL with no DEFAULT on non-empty table
    -- N/A: step does not touch this column's nullability
    [If AT RISK: row count, DEFAULT provided YES/NO, remediation plan required]
    [If N/A: "Step N does not change nullability of this column."]

[If Step N creates a new entity: "Step N creates new entity -- no before-state.
 NOT NULL RISK (BINARY FIELD): N/A"]

---

## SECTION 2: AFTER-STATE AND DATA RISK

For each step in the registry, document after-state and data loss risk.
Reference by step number. Do not re-describe the step -- cite it by number.

**Step N (from registry):**
  After type:                           [new type or "unchanged"]
  After nullable:                       YES / NO (was: YES/NO -- or "unchanged")
  After default:                        [new value / "unchanged" / "removed"]
  Type changed (BINARY FIELD):          YES / NO
  Nullability tightened (BINARY FIELD): YES / NO
  DATA LOSS RISK (BINARY FIELD):        NONE / TRUNCATION / SILENT DROP / REJECTION
    [If TRUNCATION: which column, value range affected, rows at risk]
    [If SILENT DROP: which rows, what condition triggers drop, what is lost]
    [If REJECTION: what fails, what is the error, how migration handles it]
    [If NONE: one-sentence argument -- why this step cannot silently lose data]

DATA LOSS STATEMENT (BINARY FIELD -- check exactly one):
[ ] Data loss paths found in this migration:
    Step N: [column, affected range, mechanism]
    [Repeat for all steps with DATA LOSS RISK != NONE]
[ ] No data loss paths found.
    Per-step argument (required -- one line per destructive step in registry):
    Step N: [why this step cannot silently lose data]

---

## SECTION 3: CONSTRAINT RISK

For each step that adds, removes, or modifies a constraint (NOT NULL / UNIQUE / FK / CHECK):
Reference by step number.

**Step N (from registry) -- [constraint type]:**
  Constraint change:                      [adds / removes / modifies]
  Constraint type:                        NOT NULL / UNIQUE / FK / CHECK
  Existing data satisfies (BINARY FIELD): YES / NO / UNKNOWN
    [If NO or UNKNOWN: which records violate it, migration behavior -- fail / skip / backfill]

[If no constraint changes in registry:
  "Step Registry has no constraint additions, removals, or modifications.
   Steps [N, N, ...]: no NOT NULL/UNIQUE/FK/CHECK changes."]

---

## SECTION 4: PERFORMANCE AND OPERATIONAL RISK

For each step in the registry, annotate lock behavior and operational risk.
Reference by step number.

**Step N (from registry):**
  Lock class:                        NONE / ROW / TABLE / ACCESS EXCLUSIVE
  Lock duration:                     Instant / Row-count-dependent / Full-table rewrite
  Full-table rewrite (BINARY FIELD): YES / NO
  Replication risk (FIXED TAXONOMY): NONE / LAG / BREAKING
  PERFORMANCE CLIFF (BINARY FIELD):  NONE / PRESENT
    [If PRESENT: table name, estimated row count, specific risk -- lock duration, I/O spike,
     replication lag]

---

## SECTION 5: DOMAIN IMPACT

[Positioned before SECTION 6: VERIFY. Complete this section before writing verification checks.]

For each step in the registry with DATA LOSS RISK (BINARY FIELD) = TRUNCATION or SILENT DROP,
or PERFORMANCE CLIFF (BINARY FIELD) = PRESENT: name the domain consequence.
Silence on a flagged step is a structural failure -- every flagged step requires an entry.

**Step N (from registry) -- [technical risk from SECTION 2 or 4]:**
  Business object:           [order / invoice / ledger entry / shipment / SKU / payment / refund / subscription]
  Consequence:               [concrete impact in domain terms -- name value threshold or condition at risk]
                             [Good: "invoices over $9,999,999.99 silently capped -- revenue recognition error"]
                             [Bad: "decimal precision is reduced"]
  Domain:                    Commerce / Finance / Operations
  SEVERITY (FIXED TAXONOMY): CRITICAL / HIGH / MEDIUM / LOW

[If no steps in registry have TRUNCATION, SILENT DROP, or PRESENT cliff:
  "No domain-level risks across all registry steps. Migration is data-safe and performant."]

---

## SECTION 6: VERIFY CHECKS

[SECTION 5 must be complete before this section begins.]

Post-migration checks that confirm schema and data are in the expected state.
Reference each check to its step number from SECTION 0.

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| 1 | Step [N] | [what is confirmed] | [SQL query or test] | [expected] |

---

## SECTION 7: ROLLBACK ASSESSMENT

For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation,
constraint drop): assess rollback viability. Reference by step number.

**Step N (from registry) -- [destructive operation]:**
  ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY): REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
    -- REVERSIBLE: a down migration DDL can restore schema and data
    -- BACKUP-ONLY: schema restores with DDL; data requires backup restore
    -- IRREVERSIBLE: no down migration possible -- data permanently gone
  Down migration DDL: [DDL to reverse, OR "not possible -- data is gone"]
  Notes:              [qualifying condition -- e.g., "reversible only before Step N+2 runs"]

[If no destructive steps:
  "No destructive steps in registry.
   ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY): REVERSIBLE for all steps."]

ROLLBACK SUMMARY (BINARY FIELD -- check exactly one):
[ ] All registry steps REVERSIBLE -- full down migration is possible.
[ ] Irreversible steps present: Steps [N, N] are BACKUP-ONLY or IRREVERSIBLE.
    [State what is permanently lost per step.]

---

## SECTION 8: ZERO-DOWNTIME AND IDEMPOTENCY

Zero-downtime viability:
  VIABLE (BINARY FIELD): YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step:  Step [N] -- [DDL from registry and specific reason]
    Alternative:    [expand/contract pattern, online DDL for engine, OR "none available -- reason"]

Idempotency per step:
  Step [N]: IDEMPOTENT / NOT IDEMPOTENT (BINARY FIELD)
    [If NOT IDEMPOTENT: failure mode on second run -- duplicate key / double-applied transform / other]
  [If all idempotent: "All Step Registry steps IDEMPOTENT (BINARY FIELD) -- safe to re-run."]

---

## VERDICT

  Migration risk (FIXED TAXONOMY):   LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window (BINARY FIELD): REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run (BINARY FIELD):        YES / NO / CONDITIONAL
  REVERSIBILITY (BINARY FIELD):      FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Highest business risk:             [One sentence -- cite Step N, name business object, state concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count,
data_loss_found (BINARY FIELD), constraint_violations_found (BINARY FIELD),
irreversible_steps, maintenance_window, idempotent (BINARY FIELD),
highest_severity, highest_risk_step.
```

---

## V-02: C-15 Focus -- Forward-Progress Gate Binary Chain

**Axis:** C-15 -- every phase transition is controlled by an explicit OPEN/BLOCKED gate. Each downstream phase header names its prerequisite gate state as a structural condition: e.g., "EXECUTE PHASE (requires PRE-FLIGHT GATE = OPEN)". The gate state must be resolved before the downstream phase can open. Multiple gates cascade across the full sequence.

**Hypothesis:** V-02 R2 had one domain gate between EXECUTE and VERIFY. This variation generalizes to a cascading gate chain: PRE-FLIGHT GATE -> EXECUTE -> EXECUTE GATE -> DOMAIN IMPACT -> DOMAIN IMPACT GATE -> VERIFY -> VERIFY GATE -> ROLLBACK -> ROLLBACK GATE -> OPERATIONAL. Each downstream phase header explicitly names the prerequisite gate state, converting positional sequencing into a resolvable binary dependency. A model rationalizing "I'll cover this later" must first resolve the gate to write the next section header.

```
You are running /trace-migration.

Role: Commerce / Finance / Operations migration expert.
Task: Trace a schema migration through sequential phases. Each phase ends with a gate.
The downstream phase header names the prerequisite gate. Resolve each gate before proceeding.
Do not write a phase whose prerequisite gate is BLOCKED.

Inputs required:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

Gate discipline:
  Each gate resolves to OPEN or BLOCKED.
  OPEN: all criteria for this phase are satisfied.
  BLOCKED: one or more criteria are unmet -- state which.
  The downstream phase header names the prerequisite: "(requires [GATE NAME] = OPEN)"
  If the prerequisite gate is BLOCKED: write the phase header, write "[PHASE] BLOCKED -- [reason]", stop.

---

## PARSE PHASE

Number every DDL statement in execution order. This is the step registry.
All downstream phases reference steps by this number.

Step 1: [DDL type] on [table.object] -- [what it does]
Step 2: ...
[Continue for all steps.]

Affected entities: [list tables and columns that change state]

---

## PRE-FLIGHT PHASE

Inspect entities before migration. Document before-state and flag NOT NULL risks.

### Before-State Snapshot

One entry per affected entity (reference by step number from PARSE):

  Entity: [table.column or table] -- referenced by Step [N]:
    Type:        [current type]
    Nullable:    YES / NO
    Default:     [value or "none"]
    Constraints: [list or "none"]
    Row count:   [N or "unknown"]

### NOT NULL + DEFAULT Audit

For each step that adds a NOT NULL column:

  Step [N], [table.column]:
    DEFAULT provided: YES / NO
    [If NO on non-empty table: "RISK -- NOT NULL with no DEFAULT on [N or unknown] rows.
     Requires backfill before Step [N] or migration will fail."]

[If no new NOT NULL columns: "NOT NULL RISK: CLEAR -- no new NOT NULL additions in this migration."]

PRE-FLIGHT GATE: OPEN / BLOCKED
  Criteria to OPEN: (a) all entity before-states documented, (b) all NOT NULL risks resolved or remediated.
  Criteria to BLOCK: any entity undocumented; any NOT NULL risk without a remediation plan.
  [State which condition applies and why.]

---

## EXECUTE PHASE (requires PRE-FLIGHT GATE = OPEN)

[If PRE-FLIGHT GATE = BLOCKED: write "EXECUTE PHASE BLOCKED -- [reason]." Stop here.]

For each step from PARSE, in execution order, document after-state and risk:

  Step N:
    After type:            [new type or "unchanged"]
    After nullable:        YES / NO (was: YES/NO -- or "unchanged")
    After default:         [new value / "unchanged" / "removed"]
    Type changed:          YES / NO
    Nullability tightened: YES / NO
    Data loss risk:        NONE / TRUNCATION / SILENT DROP / REJECTION
      [If not NONE: which rows, which values, what happens to them]
      [If NONE: one-sentence argument why]
    Constraint change:     [type or "none"]
    Existing data satisfies: YES / NO / UNKNOWN / N/A
      [If NO or UNKNOWN: violating records and migration behavior -- fail / skip / backfill]
    Lock class:            NONE / ROW / TABLE / ACCESS EXCLUSIVE
    Performance cliff:     NONE / PRESENT
      [If PRESENT: lock duration, I/O scope, row count if known]

DATA LOSS STATEMENT (required -- check exactly one):
[ ] Data loss paths found: Step [N]: [column, range, mechanism] -- [repeat for all flagged steps]
[ ] No data loss paths found. Per-step argument for all destructive steps:
    Step [N]: [why this step does not silently lose data]

EXECUTE GATE: OPEN / BLOCKED
  Criteria to OPEN: all steps traced with after-state; DATA LOSS STATEMENT completed.
  Criteria to BLOCK: any step untraced; DATA LOSS STATEMENT missing.
  [State which condition applies.]

---

## DOMAIN IMPACT PHASE (requires EXECUTE GATE = OPEN)

[If EXECUTE GATE = BLOCKED: write "DOMAIN IMPACT PHASE BLOCKED -- [reason]." Stop here.]

For each step from PARSE with data loss risk TRUNCATION or SILENT DROP,
or performance cliff PRESENT: state the domain consequence.
Silence on a flagged risk is a gate failure.

  Step N -- [technical risk]:
    Business object:   [order / invoice / ledger entry / shipment / SKU / payment / refund / subscription]
    Consequence:       [concrete impact in domain terms -- name value threshold or condition at risk]
                       [Good: "refunds over $10k silently zeroed due to decimal truncation"]
                       [Bad: "decimal precision is reduced"]
    Domain:            Commerce / Finance / Operations
    Severity:          CRITICAL / HIGH / MEDIUM / LOW

[If no steps flagged with TRUNCATION, SILENT DROP, or PRESENT cliff:
  "No data loss or performance cliff risks in EXECUTE phase.
   Domain assessment: migration is data-safe and performant. No business objects at risk."]

DOMAIN IMPACT GATE: OPEN / BLOCKED
  Criteria to OPEN: all flagged risks have a domain entry (or no flagged risks exist).
  Criteria to BLOCK: any flagged risk has no domain entry; any Consequence uses generic DB terminology.
  [State which condition applies.]

---

## VERIFY PHASE (requires DOMAIN IMPACT GATE = OPEN)

[If DOMAIN IMPACT GATE = BLOCKED: write "VERIFY PHASE BLOCKED -- [reason]." Stop here.]

Post-migration verification checks. Each check cites its step number from PARSE.

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| 1 | Step [N] | [what is confirmed] | [SQL query or test] | [expected] |

VERIFY GATE: OPEN / BLOCKED
  Criteria to OPEN: at least one check per step in the registry.
  Criteria to BLOCK: any registry step has no verification check.
  [State which condition applies.]

---

## ROLLBACK PHASE (requires VERIFY GATE = OPEN)

[If VERIFY GATE = BLOCKED: write "ROLLBACK PHASE BLOCKED -- [reason]." Stop here.]

For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, truncation, constraint drop):
classify rollback viability. Reference by step number.

  Step N -- [destructive operation]:
    Rollback class:    REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
    Down migration:    [DDL to reverse, OR "not possible -- data is gone"]
    Notes:             [qualifying condition -- e.g., "reversible only before Step N+2 runs"]

[If no destructive steps: "No destructive steps. Migration fully reversible."]

ROLLBACK SUMMARY (check exactly one):
[ ] All steps REVERSIBLE -- full down migration possible.
[ ] Partial or full irreversibility: Steps [N, N] are BACKUP-ONLY or IRREVERSIBLE.
    Per step: [what is permanently lost]

ROLLBACK GATE: OPEN / BLOCKED
  Criteria to OPEN: all destructive steps classified; rollback summary completed.
  Criteria to BLOCK: any destructive step unclassified.
  [State which condition applies.]

---

## OPERATIONAL PHASE (requires ROLLBACK GATE = OPEN)

[If ROLLBACK GATE = BLOCKED: write "OPERATIONAL PHASE BLOCKED -- [reason]." Stop here.]

Zero-downtime viability (reference blocking steps by Step N from PARSE):
  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] -- [DDL and reason it blocks zero-downtime]
    Alternative:   [expand/contract pattern, online DDL for engine, OR "none available -- reason"]

Idempotency per step:
  Step [N]: IDEMPOTENT / NOT IDEMPOTENT -- [if NOT: failure mode on second run]
  [If all idempotent: "All steps safe to re-run."]

---

## VERDICT

  Migration risk:        LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:    REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run:           YES / NO / CONDITIONAL
  Reversibility:         FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Highest business risk: [One sentence -- Step N, business object, concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found,
constraint_violations_found, irreversible_steps, maintenance_window, idempotent,
highest_severity, highest_risk_step.
```

---

## V-03: C-16 Focus -- Two-Phase with Phase A Step-Citation Fix

**Axis:** C-16 -- two-phase structure: Phase A interrogates by analytical concern (any order); Phase B produces the AUTHORITATIVE ARTIFACT step-ordered synthesis. **C-11 gap fix from V-04 R2:** every Phase A question explicitly instructs "reference each step by its Step N from Q1." This closes the re-description path that V-04 R2 left open (C-11 PARTIAL at 3/5).

**Hypothesis:** V-04 R2 established two-phase structure satisfies C-05 via Phase B. The C-11 residual was Phase A questions organized by entity/concern allowing re-description by name without "Step N." The fix is surgical: add "reference each step/entity by its Step N from Q1" to every Phase A question text. Tests whether citation instruction in Phase A alone closes the C-11 gap, without adding type annotations (C-14) or gate states (C-15).

```
You are running /trace-migration.

Role: Commerce / Finance / Operations migration expert.

This skill runs in two phases:
  PHASE A -- Interrogative: answer analytical questions organized by concern.
             Questions may be answered in any order.
             Every answer must reference steps, entities, and risks by their Step N from Q1.
  PHASE B -- Canonical Synthesis (AUTHORITATIVE ARTIFACT): produce mandatory step-ordered tables.
             Phase B is the authoritative output. Phase A is the reasoning layer.
             Phase B must follow execution order from Q1 exactly -- no reordering.

Inputs required before Phase A begins:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

---

## PHASE A: INTERROGATIVE

Answer each question. Organize each answer by the analytical concern named.
Reference all steps, entities, and risks by their Step N from Q1 throughout Phase A.
Do not organize Phase A by execution order -- that obligation belongs to Phase B.

### Q1: DDL Inventory (Step Registry -- first substantive section)

List every DDL statement in execution order and number each one.
This is the step registry. All Q2-Q10 answers reference steps by this number.

Step 1: [DDL type] on [table.object] -- [what it does]
Step 2: ...
[Continue for all steps.]

### Q2: Before-State per Entity

For each entity modified by any Step N from Q1: describe its state before the migration.
Reference each entity as "the entity modified by Step N" -- not by table name alone.

Step N -- entity [table.column or table]:
  Type:        [current type]
  Nullable:    YES / NO
  Default:     [value or "none"]
  Constraints: [list or "none"]
  Row count:   [N or "unknown"]

[If Step N creates a new entity: "Step N creates new entity -- no before-state."]

### Q3: NOT NULL and Nullability Risks

For each Step N from Q1 that adds a NOT NULL column or tightens nullability:
Does the target table have existing rows? Is a DEFAULT provided?
Reference the step as "Step N" -- not by operation description alone.

Step N:
  Table has existing rows: YES / NO / UNKNOWN
  DEFAULT provided:        YES / NO
  NOT NULL RISK:           CLEAR / AT RISK / N/A
  [If AT RISK: "Step N adds NOT NULL to [table.column] with no DEFAULT on [N or unknown] rows."]
  [If CLEAR or N/A: one line -- why Step N does not create NOT NULL risk]

[If no Step N adds NOT NULL: "No Step N adds NOT NULL. NOT NULL RISK: CLEAR for all steps in Q1."]

### Q4: Data Loss Paths

For each Step N from Q1 that is destructive (type narrowing, DROP, truncation, CAST):
Can existing data be silently lost? Reference the step as "Step N" throughout.

Step N:
  Data loss risk: NONE / TRUNCATION / SILENT DROP / REJECTION
  [If not NONE: "Step N -- [which rows, which values, what happens to them]"]
  [If NONE: "Step N -- [one-sentence argument why this step cannot silently lose data]"]

DATA LOSS STATEMENT (required -- check exactly one):
[ ] Data loss paths found: cite each by Step N.
[ ] No data loss found. Per-step argument for all destructive steps in Q1.

### Q5: Constraint Violations

For each Step N from Q1 that adds or removes a constraint:
Does existing data satisfy the new constraint?
Reference the step as "Step N" -- not by constraint name alone.

Step N:
  Constraint change: [adds / removes] [NOT NULL / UNIQUE / FK / CHECK]
  Existing data satisfies: YES / NO / UNKNOWN
  [If NO or UNKNOWN: "Step N -- violating records: [description], migration behavior: fail / skip / backfill"]

[If no Step N changes constraints: "No Step N adds, removes, or modifies constraints in Q1."]

### Q6: Performance Cliffs

For each Step N from Q1 that touches a large table:
Is this step likely to cause a performance cliff on the target engine?
Reference the step as "Step N" -- cite the step number when naming the risk.

Step N:
  Table:      [table name -- modified by Step N from Q1]
  Row count:  [N or "unknown"]
  Risk:       NONE / PRESENT
  [If PRESENT: "Step N -- [lock duration, I/O spike, or replication lag]"]

[If no Step N affects large tables: "No performance cliff risks found for any Step N in Q1."]

### Q7: Rollback Viability

For each Step N from Q1 that is destructive:
Can it be reversed? Reference the step as "Step N" throughout.

Step N:
  Rollback class: REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
    -- REVERSIBLE: DDL down migration restores schema and data
    -- BACKUP-ONLY: schema restores with DDL; data requires backup restore
    -- IRREVERSIBLE: no down migration possible
  Down migration: [DDL to reverse Step N, OR "not possible -- data permanently lost at Step N"]
  Notes: [qualifying condition -- e.g., "Step N reversible only before Step N+2 runs"]

[If no destructive Step N in Q1: "No destructive steps. Migration fully reversible."]

### Q8: Domain Impact

For each Step N from Q4 with data loss risk TRUNCATION or SILENT DROP,
or Step N from Q6 with performance cliff PRESENT:
Name the business consequence in domain terms. Reference the step as "Step N."

Step N -- [technical risk from Q4 or Q6]:
  Business object: [order / invoice / ledger entry / shipment / SKU / payment / refund / subscription]
  Consequence: [concrete impact in domain terms -- name value threshold or condition at risk]
               [Good: "Step N truncates DECIMAL(15,2) -- invoices over $9,999,999.99 silently capped"]
               [Bad: "decimal precision is reduced"]
  Domain: Commerce / Finance / Operations
  Severity: CRITICAL / HIGH / MEDIUM / LOW

[If no steps flagged: "No domain-level risks across all Step N entries in Q1."]

### Q9: Zero-Downtime Viability

For this migration -- can it run without a maintenance window?
When referencing blocking steps, cite them as "Step N from Q1."

  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] from Q1 -- [why online DDL or expand/contract is not viable here]
    Alternative:   [expand/contract pattern OR engine-specific online DDL OR "none available -- reason"]

### Q10: Idempotency

For each Step N from Q1: is the step safe to run a second time?
Reference each assessment as "Step N."

  Step N: IDEMPOTENT / NOT IDEMPOTENT
  [If NOT IDEMPOTENT: "Step N -- failure mode on re-run: [duplicate key / double-applied transform / other]"]
  [If all idempotent: "All Step N entries in Q1 are idempotent -- migration safe to re-run."]

---

## PHASE B: CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)

Synthesize Phase A findings into mandatory step-ordered tables.
Phase B is the authoritative output. Follow execution order from Q1 exactly.
Do not reorder, regroup, or rename steps -- reference by Step # from Q1 throughout.

### B1: Execution Trace Table

Populate strictly from Phase A findings, in execution order from Q1.

| Step # | DDL Type | Table | Before Type | Before Nullable | After Type | After Nullable | NOT NULL Risk | Data Loss Risk | Constraint Change | Perf Cliff |
|--------|---------|-------|-------------|-----------------|------------|----------------|---------------|----------------|-------------------|-----------|
| [N] | [type] | [table] | [type] | YES/NO | [type] | YES/NO | CLEAR/AT RISK/N/A | NONE/TRUNC/DROP/REJECT | [type or none] | NONE/PRESENT |

For each row with Data Loss Risk != NONE:
  Step [N]: [which rows, which values, what happens to them -- from Q4]
For each row with Perf Cliff = PRESENT:
  Step [N]: [lock duration, I/O scope, row count -- from Q6]

DATA LOSS STATEMENT (required -- check exactly one):
[ ] Data loss paths found: Step [N]: [column, range, mechanism]
[ ] No data loss paths found. Per-step argument: Step [N]: [argument]

### B2: Domain Impact Table

[Positioned before B3 VERIFY. Complete before writing B3.]

| Step # | Business Object | Consequence (domain terms -- name threshold) | Domain | Severity |
|--------|----------------|---------------------------------------------|--------|---------|
| [N] | [object] | [concrete consequence -- cite Step N] | Commerce/Finance/Operations | CRIT/HIGH/MED/LOW |

[If no flagged steps: "No domain-level risks. Migration is data-safe and performant."]

### B3: Verification Checks

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| [N] | Step [N] | [what is confirmed] | [SQL or test] | [expected] |

### B4: Rollback Summary

| Step # | Rollback Class | Down Migration DDL | Notes |
|--------|---------------|-------------------|-------|
| [N] | REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE | [DDL or "not possible"] | [condition] |

ROLLBACK SUMMARY (check exactly one):
[ ] All steps REVERSIBLE.
[ ] Steps [N, N] are BACKUP-ONLY or IRREVERSIBLE. [What is permanently lost per step.]

### B5: Verdict

  Migration risk:        LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:    REQUIRED / NOT REQUIRED / CONDITIONAL
  Safe to run:           YES / NO / CONDITIONAL
  Reversibility:         FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Zero-downtime viable:  YES / NO / PARTIAL
  Idempotent:            YES / NO / PARTIAL
  Highest business risk: [One sentence -- cite Step N, business object, concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found,
constraint_violations_found, irreversible_steps, maintenance_window, idempotent,
highest_severity, highest_risk_step.
```

---

## V-04: C-14 + C-15 Combination -- Type Annotations + Binary Gates

**Axis:** Dual enforcement: (1) type annotations at every definition site -- column headers, section labels, gate labels -- convert critical fields from formatting conventions to structural types (C-14); (2) binary gate states (OPEN/BLOCKED) that downstream phase headers name as prerequisites, blocking forward progress (C-15). Single-phase.

**Hypothesis:** C-14 closes the "free-form prose slips in" path; C-15 closes the "defer to the end" path. Together they create two independent enforcement layers without two-phase structure. A model cannot emit non-conformant values (type annotation makes the mismatch visible at the column header) AND cannot skip phases (gate blocks the next header). Tests whether C-14+C-15 alone reaches 125/130.

```
You are running /trace-migration.

Role: Commerce / Finance / Operations migration expert.
Task: Trace a schema migration step by step. Document before-state, per-step changes,
after-state. Identify data loss paths, nullable violations, missing defaults, performance cliffs.
Apply domain framing to every flagged risk.

Inputs required:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

Type annotation key (appears at every critical field definition site in this template):
  (BINARY FIELD)    -- exactly two choices; free-form prose at this site is a type error
  (FIXED TAXONOMY)  -- one choice from the named set; values outside the set are invalid

Gate discipline:
  Each phase ends with a gate labeled "(BINARY FIELD): OPEN / BLOCKED".
  The downstream phase header states the prerequisite: "(requires [GATE] = OPEN)".
  If the prerequisite gate is BLOCKED: write the phase header, write "[PHASE] BLOCKED -- [reason]", stop.

---

## PARSE: STEP REGISTRY (AUTHORITATIVE NAMED ARTIFACT)

Number every DDL statement in execution order. This is the execution contract.
All downstream phases reference steps by this number.

| Step # | DDL Type | Table | Object | What It Does (one line) |
|--------|---------|-------|--------|------------------------|
| 1 | [type] | [table] | [column/index/constraint] | [description] |
| 2 | ... | ... | ... | ... |

---

## PRE-FLIGHT PHASE

Document before-state and audit nullable risks.

### Before-State Snapshot

| Step # | Entity | Type | Nullable | Default | Row Count |
|--------|--------|------|----------|---------|-----------|
| [N] | [table.col or table] | [type] | YES/NO | [value/none] | [N/unknown] |

### NOT NULL Audit

| Step # | Table.Column | DEFAULT Provided (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) |
|--------|-------------|----------------------------------|------------------------------|
| [N] | [table.col] | YES / NO | CLEAR / AT RISK / N/A |

  -- CLEAR: no new NOT NULL addition, or table is empty, or DEFAULT is provided
  -- AT RISK: new NOT NULL with no DEFAULT on non-empty table
  -- N/A: step does not change nullability

For each AT RISK row:
  Step [N]: Row count [N or unknown], DEFAULT provided NO,
  Remediation: [backfill plan or "none -- migration will fail on non-empty table"]

PRE-FLIGHT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: all entity before-states documented; all AT RISK rows have a remediation plan.
  BLOCKED when: any entity undocumented; any AT RISK row lacks remediation.
  Current state: OPEN / BLOCKED -- [reason]

---

## EXECUTE PHASE (requires PRE-FLIGHT GATE = OPEN)

[If PRE-FLIGHT GATE = BLOCKED: write "EXECUTE PHASE BLOCKED -- [reason]." Stop here.]

Execution trace table (strict execution order from PARSE):

| Step # | After Type | After Nullable (BINARY FIELD) | Type Changed (BINARY FIELD) | Nullability Tightened (BINARY FIELD) | DATA LOSS RISK (BINARY FIELD) | Constraint Change | Existing Data Satisfies (BINARY FIELD) | Lock Class | PERFORMANCE CLIFF (BINARY FIELD) |
|--------|-----------|-------------------------------|-----------------------------|------------------------------------|-------------------------------|-------------------|----------------------------------------|-----------|-----------------------------------|
| [N] | [type/unchanged] | YES/NO | YES/NO | YES/NO | NONE/TRUNCATION/SILENT DROP/REJECTION | [type or none] | YES/NO/UNKNOWN/N/A | [class] | NONE/PRESENT |

For each row with DATA LOSS RISK (BINARY FIELD) = TRUNCATION or SILENT DROP:
  Step [N]: [which rows, which values, what happens to them]
For each row with DATA LOSS RISK (BINARY FIELD) = REJECTION:
  Step [N]: [what fails, what is the error, how migration handles it]
For each row with Existing Data Satisfies (BINARY FIELD) = NO or UNKNOWN:
  Step [N]: [violating records, migration behavior -- fail / skip / backfill]
For each row with PERFORMANCE CLIFF (BINARY FIELD) = PRESENT:
  Step [N]: [table name, estimated row count, lock duration, I/O scope, replication risk]

DATA LOSS STATEMENT (BINARY FIELD -- check exactly one):
[ ] Data loss paths found: Step [N]: [column, affected range, mechanism]
    [Repeat for all rows with DATA LOSS RISK (BINARY FIELD) != NONE]
[ ] No data loss paths found.
    Per-step argument (required for all destructive steps in registry):
    Step [N]: [why this step cannot silently lose data]

EXECUTE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: all registry steps traced; DATA LOSS STATEMENT (BINARY FIELD) completed.
  BLOCKED when: any step untraced; DATA LOSS STATEMENT missing.
  Current state: OPEN / BLOCKED -- [reason]

---

## DOMAIN IMPACT PHASE (requires EXECUTE GATE = OPEN)

[If EXECUTE GATE = BLOCKED: write "DOMAIN IMPACT PHASE BLOCKED -- [reason]." Stop here.]

For each step with DATA LOSS RISK (BINARY FIELD) = TRUNCATION or SILENT DROP,
or PERFORMANCE CLIFF (BINARY FIELD) = PRESENT: state the domain consequence.
Silence on a flagged step is a gate failure.

| Step # | Business Object | Consequence (domain terms -- name value threshold) | Domain | SEVERITY (FIXED TAXONOMY) |
|--------|----------------|--------------------------------------------------|--------|---------------------------|
| [N] | [object] | [concrete consequence -- not generic DB terminology] | Commerce/Finance/Operations | CRITICAL/HIGH/MEDIUM/LOW |

Required: Consequence must name a concrete business object and a value threshold or condition.
  Good: "Step N truncates amount column -- refunds over $10k silently zeroed out"
  Bad: "decimal precision is reduced"

[If no flagged steps: "No TRUNCATION, SILENT DROP, or PRESENT cliff steps.
 Domain assessment: data-safe and performant. No business objects at risk."]

DOMAIN IMPACT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: all flagged steps have domain entry with concrete consequence; or no flagged steps.
  BLOCKED when: any flagged step lacks domain entry; any Consequence uses generic DB terminology.
  Current state: OPEN / BLOCKED -- [reason]

---

## VERIFY PHASE (requires DOMAIN IMPACT GATE = OPEN)

[If DOMAIN IMPACT GATE = BLOCKED: write "VERIFY PHASE BLOCKED -- [reason]. Domain coverage incomplete." Stop here.]

Post-migration verification checks. Reference each check to its step number from PARSE.

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| [N] | Step [N] | [what is confirmed] | [SQL or test] | [expected] |

VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN when: at least one check per registry step.
  BLOCKED when: any registry step lacks a verification check.
  Current state: OPEN / BLOCKED -- [reason]

---

## ROLLBACK PHASE (requires VERIFY GATE = OPEN)

[If VERIFY GATE = BLOCKED: write "ROLLBACK PHASE BLOCKED -- [reason]." Stop here.]

For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation, constraint drop):

| Step # | Destructive Operation | ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY) | Down Migration DDL | Notes |
|--------|----------------------|------------------------------------------------|-------------------|-------|
| [N] | [operation] | REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE | [DDL or "not possible"] | [condition] |

[If no destructive steps: "No destructive steps in registry.
 ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY): REVERSIBLE for all steps."]

ROLLBACK SUMMARY (BINARY FIELD -- check exactly one):
[ ] All steps REVERSIBLE -- full down migration possible.
[ ] Irreversible steps present: Steps [N, N] are BACKUP-ONLY or IRREVERSIBLE.
    Per step: [what is permanently lost]

---

## VERDICT

  Migration risk (FIXED TAXONOMY):     LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window (BINARY FIELD):   REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run (BINARY FIELD):          YES / NO / CONDITIONAL
  REVERSIBILITY (BINARY FIELD):        FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Zero-downtime viable (BINARY FIELD): YES / NO / PARTIAL
  Idempotent (BINARY FIELD):           YES / NO / PARTIAL
  Highest business risk: [One sentence -- Step N, business object, concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count,
data_loss_found (BINARY FIELD), constraint_violations_found (BINARY FIELD),
irreversible_steps, maintenance_window, idempotent (BINARY FIELD),
highest_severity, highest_risk_step.
```

---

## V-05: Full v3 Synthesis -- C-14 + C-15 + C-16

**Axis:** All three new v3 criteria combined on the V-05 R2 foundation: type annotations at every definition site in both phases (C-14) + binary gate states with downstream-section header prerequisites in Phase B (C-15) + two-phase analytical decoupling with Phase A step-citation discipline throughout (C-16 + C-11 gap closed).

**Hypothesis:** V-05 R2 reached 115/115 on the v2 rubric. Adding C-14 (type annotations in Phase B column headers and gate labels) + C-15 (OPEN/BLOCKED gates that Phase B section headers name as prerequisites) + C-16 (Phase A interrogates freely with step-citation enforcement; Phase B labeled AUTHORITATIVE ARTIFACT) should produce 130/130. The three mechanisms are non-redundant: C-14 targets field-level type integrity; C-15 targets phase-level sequencing; C-16 targets the analytical-depth vs. chronological-output trade-off.

```
You are running /trace-migration.

Role: Commerce / Finance / Operations migration expert.

This skill runs in two phases:
  PHASE A -- Interrogative: answer analytical questions organized by concern.
             Questions may be in any order. Organize by risk type, entity, or concern freely.
             Every answer must reference steps, entities, and risks by their Step N from Q1.
             Do not organize Phase A by execution sequence -- Phase B owns that obligation.
  PHASE B -- Canonical Synthesis (AUTHORITATIVE ARTIFACT): produce mandatory step-ordered tables.
             Phase B is the authoritative output. Phase A is the reasoning layer.
             Phase B enforces execution order, type annotations, and gate sequencing.

Type annotation key (appears at every critical field definition site in PHASE B):
  (BINARY FIELD)    -- exactly two choices; free-form prose at this site is a type error
  (FIXED TAXONOMY)  -- one choice from the named set; values outside the set are invalid

Gate discipline (PHASE B only):
  Each phase gate resolves to OPEN or BLOCKED (BINARY FIELD).
  The downstream section header names the prerequisite: "(requires [GATE] = OPEN)".
  If the prerequisite gate is BLOCKED: write the section header, write "BLOCKED -- [reason]", stop.

Inputs required before Phase A:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before beginning Phase A.

---

## PHASE A: INTERROGATIVE

Answer each question organized by the concern named. Reference all steps, entities, and risks
by their Step N from Q1. Phase A may answer questions in any order -- organization by execution
sequence is Phase B's obligation, not Phase A's.

### Q1: DDL Inventory (Step Registry -- first substantive section)

List every DDL statement in execution order and number each one.
This is the step registry. All Q2-Q10 reference steps by this number.

Step 1: [DDL type] on [table.object] -- [what it does]
Step 2: ...
[Continue for all steps.]

### Q2: Before-State per Entity

For each entity modified by Step N from Q1: describe its state before the migration.
Reference each entity by "Step N" -- not by table name alone.

Step N -- [table.column or table]:
  Type:        [current type]
  Nullable:    YES / NO
  Default:     [value or "none"]
  Constraints: [list or "none"]
  Row count:   [N or "unknown"]

[If Step N creates a new entity: "Step N creates new entity -- no before-state."]

### Q3: NOT NULL and Nullability Risks

For each Step N from Q1 that adds NOT NULL or tightens nullability:
NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A -- cite the step as "Step N."

Step N:
  NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A
  [AT RISK: "Step N adds NOT NULL to [table.column] with no DEFAULT on [N or unknown] rows."]
  [CLEAR: "Step N: DEFAULT provided / table empty / does not affect nullability."]
  [N/A: "Step N does not change nullability."]
  [If AT RISK: row count, DEFAULT provided YES/NO, remediation plan]

[If no Step N changes nullability: "NOT NULL RISK (BINARY FIELD): CLEAR for all steps."]

### Q4: Data Loss Paths

For each Step N from Q1 that is destructive: can existing data be silently lost?
DATA LOSS RISK (BINARY FIELD) per step: NONE / TRUNCATION / SILENT DROP / REJECTION.

Step N:
  DATA LOSS RISK (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION
  [If not NONE: "Step N -- [which rows, which values, what happens to them]"]
  [If NONE: "Step N -- [one-sentence argument why this step cannot silently lose data]"]

DATA LOSS STATEMENT (BINARY FIELD -- check exactly one):
[ ] Data loss paths found: cite each by Step N.
[ ] No data loss found. Per-step argument for all destructive steps in Q1.

### Q5: Constraint Violations

For each Step N from Q1 that adds or removes a constraint:
Existing data satisfies (BINARY FIELD): YES / NO / UNKNOWN -- cite as "Step N."

Step N:
  Constraint change: [adds / removes] [NOT NULL / UNIQUE / FK / CHECK]
  Existing data satisfies (BINARY FIELD): YES / NO / UNKNOWN
  [If NO or UNKNOWN: "Step N -- [violating records], migration behavior: fail / skip / backfill"]

[If no Step N changes constraints: "No Step N adds, removes, or modifies constraints."]

### Q6: Performance Cliffs

For each Step N from Q1 touching a large table:
PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT -- cite as "Step N."

Step N:
  Table: [from Q1, referenced by Step N]
  Row count: [N or "unknown"]
  PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT
  [If PRESENT: "Step N -- [lock duration, I/O spike, replication lag]"]

[If no Step N affects large tables: "PERFORMANCE CLIFF (BINARY FIELD): NONE for all steps."]

### Q7: Rollback Viability

For each destructive Step N from Q1:
ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY): REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE.

Step N:
  ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY): REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
  Down migration: [DDL to reverse Step N, OR "not possible -- cite Step N"]
  Notes: [qualifying condition -- e.g., "Step N reversible only before Step N+2 runs"]

[If no destructive Step N: "No destructive steps. ROLLBACK CLASS: REVERSIBLE for all."]

### Q8: Domain Impact

For each Step N with DATA LOSS RISK (BINARY FIELD) != NONE, or PERFORMANCE CLIFF (BINARY FIELD) = PRESENT:
Name the business consequence. Reference as "Step N." SEVERITY (FIXED TAXONOMY): CRITICAL/HIGH/MEDIUM/LOW.

Step N -- [technical risk]:
  Business object: [order / invoice / ledger entry / shipment / SKU / payment / refund / subscription]
  Consequence: [concrete impact in domain terms -- name value threshold or condition]
               [Good: "Step N truncates DECIMAL -- invoices over $9,999,999.99 silently capped"]
               [Bad: "decimal precision is reduced"]
  Domain: Commerce / Finance / Operations
  SEVERITY (FIXED TAXONOMY): CRITICAL / HIGH / MEDIUM / LOW

[If no steps flagged: "No domain-level risks across all Step N entries."]

### Q9: Zero-Downtime Viability

For this migration: viable without maintenance window?
VIABLE (BINARY FIELD): YES / NO / PARTIAL. Cite blocking steps as "Step N from Q1."

  VIABLE (BINARY FIELD): YES / NO / PARTIAL
  [If NO or PARTIAL: "Blocking step: Step [N] -- [reason]. Alternative: [pattern or DDL or none]"]

### Q10: Idempotency

For each Step N from Q1: IDEMPOTENT / NOT IDEMPOTENT (BINARY FIELD).

  Step N: IDEMPOTENT / NOT IDEMPOTENT (BINARY FIELD)
  [If NOT IDEMPOTENT: "Step N -- failure mode on re-run: [duplicate key / double transform / other]"]
  [If all idempotent: "All Step N entries: IDEMPOTENT (BINARY FIELD)."]

---

## PHASE B: CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)

Phase B is the authoritative output. Synthesize Phase A findings into step-ordered tables.
Follow execution order from Q1 exactly. All critical fields carry type annotations.
Gate discipline applies: each section may be BLOCKED by its prerequisite gate.

### PRE-FLIGHT TABLES (synthesized from Q2, Q3)

Before-state table:
| Step # | Entity | Type | Nullable | Default | Row Count | NOT NULL RISK (BINARY FIELD) |
|--------|--------|------|----------|---------|-----------|------------------------------|
| [N] | [table.col] | [type] | YES/NO | [val/none] | [N/unknown] | CLEAR / AT RISK / N/A |

For each AT RISK row: Step [N] -- remediation: [plan or "none -- will fail on non-empty table"]

PRE-FLIGHT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN: all entity before-states documented; all AT RISK rows have remediation plans.
  BLOCKED: any entity undocumented; any AT RISK row lacks remediation.
  Current state: OPEN / BLOCKED -- [reason]

---

### B1: EXECUTION TRACE TABLE (requires PRE-FLIGHT GATE = OPEN)

[If PRE-FLIGHT GATE = BLOCKED: write "B1 BLOCKED -- [reason]." Stop Phase B here.]

Authoritative step-ordered execution trace. Strict execution order from Q1.

| Step # | After Type | After Nullable (BINARY FIELD) | Type Changed (BINARY FIELD) | Nullability Tightened (BINARY FIELD) | DATA LOSS RISK (BINARY FIELD) | Constraint Change | Existing Data Satisfies (BINARY FIELD) | PERFORMANCE CLIFF (BINARY FIELD) |
|--------|-----------|-------------------------------|-----------------------------|------------------------------------|-------------------------------|-------------------|----------------------------------------|----------------------------------|
| [N] | [type/unchanged] | YES/NO | YES/NO | YES/NO | NONE/TRUNCATION/SILENT DROP/REJECTION | [type/none] | YES/NO/UNKNOWN/N/A | NONE/PRESENT |

Annotations for DATA LOSS RISK (BINARY FIELD) != NONE rows: Step [N] -- [rows, values, mechanism]
Annotations for PERFORMANCE CLIFF (BINARY FIELD) = PRESENT rows: Step [N] -- [table, rows, duration]
Annotations for Existing Data Satisfies (BINARY FIELD) = NO/UNKNOWN: Step [N] -- [records, behavior]

DATA LOSS STATEMENT (BINARY FIELD -- check exactly one):
[ ] Data loss paths found: Step [N]: [column, range, mechanism]
[ ] No data loss paths found. Per-step argument: Step [N]: [argument]

EXECUTE GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN: all steps traced; DATA LOSS STATEMENT (BINARY FIELD) completed.
  BLOCKED: any step untraced; statement missing.
  Current state: OPEN / BLOCKED -- [reason]

---

### B2: DOMAIN IMPACT TABLE (requires EXECUTE GATE = OPEN)

[If EXECUTE GATE = BLOCKED: write "B2 BLOCKED -- [reason]." Stop Phase B here.]
[Positioned before B3 VERIFY. Complete before writing verification checks.]

| Step # | Business Object | Consequence (domain terms -- name value threshold) | Domain | SEVERITY (FIXED TAXONOMY) |
|--------|----------------|--------------------------------------------------|--------|---------------------------|
| [N] | [object] | [concrete consequence -- cite Step N] | Commerce/Finance/Operations | CRITICAL/HIGH/MEDIUM/LOW |

[If no flagged steps: "No TRUNCATION, SILENT DROP, or PRESENT cliff steps. Domain: data-safe."]

DOMAIN IMPACT GATE (BINARY FIELD): OPEN / BLOCKED
  OPEN: all flagged steps have domain entry with concrete consequence; or no flagged steps.
  BLOCKED: any flagged step lacks a domain entry; any Consequence uses generic DB terminology.
  Current state: OPEN / BLOCKED -- [reason]

---

### B3: VERIFY CHECKS (requires DOMAIN IMPACT GATE = OPEN)

[If DOMAIN IMPACT GATE = BLOCKED: write "B3 BLOCKED -- Domain coverage incomplete." Stop here.]

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| [N] | Step [N] | [what] | [SQL or test] | [expected] |

---

### B4: ROLLBACK TABLE

| Step # | Destructive Operation | ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY) | Down Migration DDL | Notes |
|--------|----------------------|------------------------------------------------|-------------------|-------|
| [N] | [operation] | REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE | [DDL or "not possible"] | [condition] |

[If no destructive steps: "No destructive steps. ROLLBACK CLASS (BINARY FIELD): REVERSIBLE for all."]

ROLLBACK SUMMARY (BINARY FIELD -- check exactly one):
[ ] All destructive steps REVERSIBLE.
[ ] Irreversible steps present: Steps [N, N]. [What is permanently lost per step.]

---

### B5: VERDICT

  Migration risk (FIXED TAXONOMY):     LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window (BINARY FIELD):   REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run (BINARY FIELD):          YES / NO / CONDITIONAL
  REVERSIBILITY (BINARY FIELD):        FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Zero-downtime viable (BINARY FIELD): YES / NO / PARTIAL
  Idempotent (BINARY FIELD):           YES / NO / PARTIAL
  Highest business risk: [One sentence -- cite Step N, name business object, state concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count,
data_loss_found (BINARY FIELD), constraint_violations_found (BINARY FIELD),
irreversible_steps, maintenance_window, idempotent (BINARY FIELD),
highest_severity, highest_risk_step.
```

---

## Score Predictions

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | Total | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 Type Annotation | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | **5** | 0 | 0 | **120** | YES |
| V-02 Gate Binary Chain | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | 0 | **5** | 0 | **120** | YES |
| V-03 Two-Phase Citation Fix | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **5** | 5 | 5 | 0 | 0 | **5** | **120** | YES |
| V-04 C-14+C-15 Combo | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | **5** | **5** | 0 | **125** | YES |
| V-05 Full v3 Synthesis | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **5** | 5 | 5 | **5** | **5** | **5** | **130** | YES |

Golden threshold: 80% of 130 = 104 pts. All variations exceed threshold.

---

## Criterion Coverage by Variation

| New v3 Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|------------------|------|------|------|------|------|
| C-14 Type Annotation at Definition Site | **PRIMARY** | -- | -- | yes | yes |
| C-15 Binary Gate with Downstream Header | -- | **PRIMARY** | -- | yes | yes |
| C-16 Two-Phase Decoupling | -- | -- | **PRIMARY** | -- | yes |

---

## Design Notes

**V-01 C-14 mechanism:** "(BINARY FIELD)" appears in column headers (e.g., `NOT NULL RISK (BINARY FIELD)`), section labels (e.g., `DATA LOSS STATEMENT (BINARY FIELD)`), and verdict fields (e.g., `REVERSIBILITY (BINARY FIELD)`). The annotation travels with the field definition site, not just a first-occurrence instruction note. A model filling `NOT NULL RISK (BINARY FIELD): <prose>` encounters a type mismatch visible at the column level. Prior C-13 enforcement required binary values; C-14 adds the explicit type annotation at every definition site, converting absence or non-conformance from an implicit omission into a visible type error.

**V-02 C-15 mechanism:** Five gates cascade across the sequence (PRE-FLIGHT, EXECUTE, DOMAIN IMPACT, VERIFY, ROLLBACK). Each downstream phase header explicitly names its prerequisite gate state: "(requires [GATE] = OPEN)". The evaluator distinction from C-12: C-12 requires positional placement of the domain section before verify. C-15 requires the model to *resolve* a binary state AND the downstream section to *name* that state as a condition of opening. The cascading chain means a BLOCKED gate at any point stops all downstream phases.

**V-03 C-11 fix:** V-04 R2 had the C-11 residual (3/5) because Phase A questions organized by entity/concern allowed re-description by name without "Step N." The fix is minimal and surgical: every Phase A question (Q2-Q10) explicitly says "reference each step/entity by its Step N from Q1." This is the single-axis test -- does citation instruction in Phase A question text alone close the C-11 gap, without adding type annotations (C-14) or gate states (C-15)?

**V-04 combination:** Type annotations and binary gates are structurally independent. C-14 enforces at the field level (what value is acceptable); C-15 enforces at the phase level (when a section may be written). Neither requires two-phase structure. V-04 tests whether these two layers together are sufficient for 125/130, with C-16 as the isolated remaining gap.

**V-05 synthesis strength:** Three non-redundant mechanisms: Phase A step-citation discipline closes the analytical-depth C-11 gap (from V-03). Phase B type annotations close the critical-field type integrity gap (from V-01). Phase B binary gates close the phase-sequencing gap (from V-02). Each targets a different failure mode and cannot substitute for the others.

```json
{"target_rubric": "v3", "max_score": 130, "new_criteria": ["C-14", "C-15", "C-16"], "predicted_top": 130, "all_golden": true, "single_axis": ["V-01:C-14", "V-02:C-15", "V-03:C-16"], "combinations": ["V-04:C-14+C-15", "V-05:C-14+C-15+C-16"], "key_fix": "V-03 closes V-04-R2 C-11 gap by adding explicit Step-N citation instruction to every Phase A question text"}
```
