Written to `simulations/quest/variations/trace-migration-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — trace-migration

**5 complete variations targeting the v2 rubric (115 pts, C-01 to C-13):**

| V | Axis | Primary Mechanism | Predicted Score |
|---|---|---|---|
| **V-01** | C-11 focus | Step registry as named contract; every section header says "extends Step Registry by step number"; re-describing steps by name without citing N is prohibited | 115 |
| **V-02** | C-12 focus | Domain section becomes a binary gate checkpoint (DOMAIN GATE: OPEN/BLOCKED) between EXECUTE and VERIFY; VERIFY phase cannot begin until gate resolves | 115 |
| **V-03** | C-13 focus | All three critical fields labeled "BINARY FIELD" with fixed taxonomy everywhere they appear; free-form prose explicitly prohibited for DATA LOSS RISK, NOT NULL RISK, ROLLBACK CLASS | 115 |
| **V-04** | C-05 rehab | Two-phase: Phase A interrogates by analytical concern (any order); Phase B synthesizes a mandatory step-ordered trace table from Phase A findings; C-05 enforced by Phase B structure | 115 |
| **V-05** | Full v2 synthesis | All three new mechanisms combined: "AUTHORITATIVE NAMED ARTIFACT" step registry (C-11) + DOMAIN GATE: OPEN/BLOCKED checkpoint (C-12) + "BINARY FIELD" labels on all three critical dimensions (C-13) + phase gates | 115 |

**Key design decisions:**
- **V-04 rehabilitation** — the R1 root cause was questions organizing by concern rather than execution sequence. Two phases solve it cleanly: Phase A reasons freely, Phase B produces the canonical step-ordered artifact. C-05 is now enforced by Phase B's mandatory table structure, not by question ordering.
- **C-13 isolation in V-03** — "BINARY FIELD" as an explicit label is the single-axis hypothesis: when a field is named as a structural type annotation rather than a formatting convention, the model treats its absence as a type error rather than an optional omission.
- **C-12 gate vs. position** — V-02 tests whether a gate binary (BLOCKED state that prevents forward progress) is more reliable than positional placement alone. V-05 uses both together.
- **Strength ranking**: C-11: V-01 > V-05 | C-12: V-02 = V-05 | C-13: V-03 > V-05 | C-05: V-05 > V-02 > V-04
so uses gate; V-01/V-03/V-04 use positioning alone
- **C-13** — strongest enforcement in V-03 ("BINARY FIELD" label + explicit prohibition on free-form); V-05 applies same labels; V-01/V-02/V-04 use checkboxes and fixed taxonomies
- **V-04 rehabilitation** — two-phase structure resolves the R1 V-04 failure: Phase A questions organize by concern, Phase B table enforces step-order output; C-05 passes because the canonical artifact (Phase B) is chronological

**Predicted ceiling:** V-05 (maximum structural coverage: three new mechanisms combined). V-02 and V-03 are closest single-axis competitors for their target criteria. V-04 tests whether investigative depth can coexist with chronological output.

---

## V-01: C-11 Focus — Step Registry Contract

**Axis:** C-11 — the step registry is declared as a named contract artifact in section 0; every downstream section header announces that it "extends" the registry by step number; sections are prohibited from re-describing steps by table name or operation type alone.
**Hypothesis:** When sections are framed as extensions of a contract rather than standalone analyses, the model uses step numbers in downstream prose because it is annotating an existing artifact, not describing a migration from scratch. This produces more reliable C-11 cross-references than embedding ordering instructions in section prose.

```
You are running /trace-migration.

Inputs required before analysis begins:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

---

## SECTION 0: STEP REGISTRY (AUTHORITATIVE ARTIFACT)

This table is the execution contract. Every section below extends it by step number.
No section may describe a step by table name or operation type alone -- always cite "Step N."

| Step # | DDL Type | Table | Object | What It Does (one line) |
|--------|---------|-------|--------|------------------------|
| 1 | [type] | [table] | [column/index/constraint] | [description] |
| 2 | ... | ... | ... | ... |

---

## SECTION 1: BEFORE-STATE (extends Step Registry for steps that modify existing entities)

For each step in the registry that modifies an existing table or column, document the entity's
state before this migration runs. Reference each entry by step number from SECTION 0.
Do not re-describe the operation -- cite it: "Step N modifies this entity."

Step N -- Before-state of [table.column or table] (Step N modifies this entity):
  Type:        [current type]
  Nullable:    YES / NO
  Default:     [value or "none"]
  Constraints: [list or "none"]
  Row count:   [N or "unknown"]
  NOT NULL check: [Will Step N add NOT NULL? YES/NO.
    If YES -- DEFAULT provided: YES / NO.
    If NO DEFAULT on non-empty table: "RISK -- NOT NULL with no DEFAULT. Row count: [N or unknown]."]

[If a step in the registry has no before-state to document: "Step N: no pre-existing entity state (new table/column)."]

---

## SECTION 2: AFTER-STATE AND DATA RISK (extends Step Registry for all steps)

For each step in the registry, complete the after-state and data risk fields.
Reference each entry by step number from SECTION 0. Do not re-describe the operation.

Step N (Step Registry entry):
  After type:          [new type or "unchanged"]
  After nullable:      YES / NO (changed from: YES/NO -- or "unchanged")
  After default:       [new value / "unchanged" / "removed"]
  Type changed:        YES / NO
  Nullability tightened: YES / NO
  Data loss risk:      NONE / TRUNCATION / SILENT DROP / REJECTION
    [If not NONE: describe concretely -- which rows, which values, what happens to them.]
    [If NONE: one sentence explaining why -- does it error? Is the table empty? Is the change lossless?]

DATA LOSS STATEMENT (required -- check exactly one):
[ ] Data loss paths found: [list each by Step N from the registry]
[ ] No data loss paths found. Per-step argument (one line per destructive step in registry):
    Step N: [why this step does not cause silent data loss]

---

## SECTION 3: CONSTRAINT RISK (extends Step Registry for steps with constraint changes)

For each step in the registry that adds or removes a constraint (NOT NULL / UNIQUE / FK / CHECK):
Reference by step number from SECTION 0. Do not re-describe the operation.

Step N (Step Registry entry):
  Constraint change: [type -- NOT NULL / UNIQUE / FK / CHECK]
  Existing data satisfies new constraint: YES / NO / UNKNOWN
    [If NO or UNKNOWN: name which records violate it and how the migration handles it -- fail, skip, or backfill]

[If no constraint changes in this migration:
  "No constraint changes. Step Registry entries [list step numbers] have no NOT NULL/UNIQUE/FK/CHECK
   additions or removals."]

---

## SECTION 4: PERFORMANCE AND OPERATIONAL RISK (extends Step Registry for all steps)

For each step in the registry, annotate operational risk.
Reference by step number from SECTION 0.

Step N (Step Registry entry):
  Lock class:         [NONE / ROW / TABLE / ACCESS EXCLUSIVE]
  Lock duration:      [Instant / Row-count-dependent / Full-table rewrite]
  Full-table rewrite: YES / NO
  Replication risk:   NONE / LAG / BREAKING
  Performance cliff:  NONE / PRESENT
    [If PRESENT: describe -- lock duration, I/O scope, row count if known]

---

## SECTION 5: DOMAIN IMPACT (extends Step Registry for steps with TRUNCATION, SILENT DROP, or PRESENT cliff)

[Positioned before SECTION 6: VERIFY. Complete this section before writing verification checks.]

For each step in the registry with a data loss risk of TRUNCATION or SILENT DROP, or a
performance cliff of PRESENT: extend the registry with domain framing.
Reference by step number from SECTION 0. Silence on a flagged step is a failure.

Step N (Step Registry entry) -- [technical risk from SECTION 2 or 4]:
  Business object:   [order / invoice / ledger entry / shipment / SKU / payment / refund / subscription]
  Consequence:       [concrete impact in domain terms -- not database terminology]
                     [Required: name the value threshold or condition at risk]
                     [Good: "invoices over $9,999,999.99 silently capped -- revenue recognition error on enterprise contracts"]
                     [Bad: "decimal precision is reduced"]
  Domain:            Commerce / Finance / Operations
  Severity:          CRITICAL / HIGH / MEDIUM / LOW

[If no steps in the registry have TRUNCATION, SILENT DROP, or PRESENT cliff:
  "No domain-level risks. Step Registry is data-safe and performant. Domain assessment: complete."]

---

## SECTION 6: VERIFY CHECKS (extends Step Registry with post-migration confirmations)

[SECTION 5 must be complete before this section begins.]

Post-migration checks that confirm the schema and data are in the expected state.
Reference each check to its step number from SECTION 0.

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| 1 | Step [N] | [e.g., no NULLs in new NOT NULL column] | [query] | [expected] |

---

## SECTION 7: ROLLBACK (extends Step Registry for destructive steps)

For each step in the registry that is a DROP COLUMN, DROP TABLE, type narrowing,
data truncation, or constraint drop -- extend the registry with rollback classification.
Reference by step number from SECTION 0.

Step N (Step Registry entry):
  Rollback class:    REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
  Down migration:    [DDL to reverse OR "not possible -- data is gone"]
  Notes:             [qualifying condition if any -- e.g., "reversible only before Step N+2 runs"]

[If no destructive steps in registry: "No destructive steps. Step Registry is fully reversible."]

ROLLBACK SUMMARY (required -- check exactly one):
[ ] All registry steps reversible with down migration.
[ ] Partial reversibility: Steps [N, N] are BACKUP-ONLY or IRREVERSIBLE. [State what is permanently lost per step.]

---

## SECTION 8: ZERO-DOWNTIME AND IDEMPOTENCY (extends Step Registry with operational assessment)

Zero-downtime (reference blocking steps by Step N from registry):
  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] -- [DDL from registry and specific reason]
    Alternative: [expand/contract pattern, online DDL for this engine, OR "none available -- explain why"]

Idempotency per step (extends Step Registry):
  Step [N]: [IDEMPOTENT / NOT IDEMPOTENT] -- [if NOT: failure mode on second run -- duplicate key / double transform / other]
  [Repeat for all steps. If all idempotent: "All Step Registry entries safe to run twice."]

---

## VERDICT

  Migration risk:        LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:    REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run:           YES / NO / CONDITIONAL
  Reversibility:         FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Highest business risk: [One sentence -- cite Step N from registry, name business object, state concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found, constraint_violations_found,
irreversible_steps, maintenance_window, idempotent, highest_severity, highest_risk_step.
```

---

## V-02: C-12 Focus — Domain Gate as Binary Checkpoint

**Axis:** C-12 — the domain section becomes a mandatory binary gate (DOMAIN GATE: OPEN / BLOCKED) positioned between EXECUTE and VERIFY phases; the VERIFY phase cannot begin until the gate resolves to OPEN; the gate is BLOCKED if any flagged risk has no domain entry.
**Hypothesis:** Positioning a domain section before VERIFY helps, but a gate binary with an explicit BLOCKED state adds a second enforcement layer. The model cannot rationalize "I'll add domain notes at the end" when it must resolve DOMAIN GATE: OPEN before it can open the next phase. Tests whether a gate mechanism produces more reliable C-12 compliance than positional placement alone.

```
You are running /trace-migration. Four sequential phases. Each phase has a gate condition.
Complete the gate before opening the next phase. Do not write ahead.

Inputs required:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

---

## PARSE: EXECUTION SEQUENCE

Number every DDL statement in execution order. This list is authoritative.
Downstream phases reference steps by this number. Do not re-describe steps by table name alone.

Step 1: [DDL type] on [table.object] -- [what it does]
Step 2: ...
[Continue for all steps.]

Affected entities: [list tables or columns that change state]

---

## PRE-FLIGHT PHASE

Complete before EXECUTE phase opens.

### Before-State Snapshot

One entry per affected entity:

  Entity: [table.column or table] -- (referenced by Step [N] from PARSE)
    Type:        [current type]
    Nullable:    YES / NO
    Default:     [value or "none"]
    Constraints: [list or "none"]
    Row count:   [N or "unknown"]

### NOT NULL + DEFAULT Audit

For each new NOT NULL column added by any step:

  Step [N], [table.column]:
    DEFAULT provided: YES / NO
    [If NO on non-empty table: "RISK -- NOT NULL with no DEFAULT on [N or unknown] rows.
     Will fail unless table is empty or backfill precedes Step [N]."]

[If no new NOT NULL columns: "NOT NULL risk: CLEAR -- no new NOT NULL additions in this migration."]

PRE-FLIGHT GATE: OPEN / BLOCKED
  [BLOCKED if any entity before-state is undocumented or NOT NULL risk is unresolved without a remediation plan.]

---

## EXECUTE PHASE

[PRE-FLIGHT GATE must be OPEN before this phase begins.]

### After-State per Step

For each step, in execution order from PARSE (cite by step number):

  Step N:
    After type:          [new type or "unchanged"]
    After nullable:      YES / NO (changed from YES/NO -- or "unchanged")
    After default:       [new value / "unchanged" / "removed"]
    Type changed:        YES / NO
    Nullability tightened: YES / NO
    Constraint added:    [type or "none"]

### Data Loss and Constraint Risk

For each step that modifies existing data or adds a constraint (cite by step number):

  Step N:
    Data loss risk:      NONE / TRUNCATION / SILENT DROP / REJECTION
      [If not NONE: which rows, which values, what happens to them]
      [If NONE: why -- does it error? Is the table empty? Is the change lossless for values in domain?]
    Constraint change:   [type or "none"]
    Existing data satisfies new constraint: YES / NO / UNKNOWN / N/A
      [If NO or UNKNOWN: name violating records and migration behavior (fail / skip / backfill)]

DATA LOSS STATEMENT (required -- check exactly one):
[ ] Data loss paths found: Step [N]: [column, value range, what happens]
[ ] No data loss paths found. Per-step reasoning:
    Step [N]: [why this destructive step does not silently drop data -- one line per destructive step]

### Operational Risk per Step

For each step (cite by step number):

  Step N:
    Lock class:         [NONE / ROW / TABLE / ACCESS EXCLUSIVE]
    Lock duration:      [Instant / Row-count-dependent / Full-table rewrite]
    Full-table rewrite: YES / NO
    Replication risk:   NONE / LAG / BREAKING
    Performance cliff:  NONE / PRESENT
      [If PRESENT: describe -- lock class, duration, row count if known]

EXECUTE PHASE: COMPLETE (write this line when all steps are traced)

---

## DOMAIN GATE PHASE

[Runs immediately after EXECUTE PHASE. VERIFY PHASE may not begin until DOMAIN GATE is OPEN.]
[Converts every flagged risk from EXECUTE into a named business consequence.]
[Silence on a risk is a gate failure -- every step with TRUNCATION, SILENT DROP, or PRESENT cliff requires an entry.]

For each risk flagged in EXECUTE (cite by Step N from PARSE):

  Step N -- [technical risk]:
    Business object:   [order / invoice / ledger entry / shipment / SKU / payment / refund / subscription]
    Consequence:       [concrete impact in domain terms -- not generic database terminology]
                       [Required: name the value threshold or condition at risk]
                       [Good: "refunds over $10k silently zeroed out due to decimal truncation"]
                       [Bad: "decimal precision is reduced"]
    Domain:            Commerce / Finance / Operations
    Severity:          CRITICAL / HIGH / MEDIUM / LOW

[If no steps had TRUNCATION, SILENT DROP, or PRESENT cliff:
  "No data loss or performance cliff risks found in EXECUTE phase.
   Domain assessment: migration is data-safe and performant. No business objects at risk."]

DOMAIN GATE: OPEN / BLOCKED
  [BLOCKED if: any step with TRUNCATION, SILENT DROP, or PRESENT cliff from EXECUTE has no entry above.
   Name the missing step number and what domain assessment is needed to resolve the block.]

---

## VERIFY PHASE

[DOMAIN GATE must be OPEN before this phase begins.]

Post-migration checks that confirm the schema and data are in the expected state.
Reference each check to a step number from PARSE.

  Check N: [what to verify] -- references Step [N] -- [how to verify] -- [expected result]
  Example: Check row count unchanged for tables where DROP COLUMN was applied (Step N).
  Example: Confirm no NULL values in new NOT NULL column (Step N).
  Example: Confirm FK references resolve for new FK constraint (Step N).

---

## ROLLBACK PHASE

For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation, constraint drop):
Reference by Step N from PARSE.

  Step N:
    Rollback class:    REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
    Down migration:    [DDL to reverse OR "not possible -- data is gone"]
    Notes:             [qualifying condition -- e.g., "reversible only before Step N+2 runs"]

[If no destructive steps: "No destructive steps. Migration is fully reversible."]

ROLLBACK SUMMARY:
  Irreversible steps present: YES / NO
    [If YES: Step [N] -- [what is permanently lost]]

---

## ZERO-DOWNTIME AND IDEMPOTENCY

Zero-downtime:
  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:] Blocking step: Step [N] -- [DDL and specific reason]
  Alternative: [expand/contract or online DDL for this engine, OR "none available -- explain"]

Idempotency:
  Safe overall: YES / NO / PARTIAL
  Non-idempotent steps:
    Step [N]: [failure mode if run twice -- duplicate key / double-applied transform / other]
  [If all safe: "All steps idempotent."]

---

## VERDICT

  Migration risk:        LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:    REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run:           YES / NO / CONDITIONAL
  Reversibility:         FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Highest business risk: [One sentence -- Step N from PARSE, business object, concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found, constraint_violations_found,
irreversible_steps, maintenance_window, idempotent, highest_severity, highest_risk_step.
```

---

## V-03: C-13 Focus — Binary-First for Three Critical Fields

**Axis:** C-13 — data loss risk, NOT NULL risk, and rollback viability are labeled "BINARY FIELD" with explicit fixed taxonomies everywhere they appear; free-form prose is explicitly prohibited for these three fields; the label makes absence structurally detectable.
**Hypothesis:** Labeling a field "BINARY FIELD -- choose exactly one from this taxonomy" produces more reliable omission detection than a pre-printed checkbox alone, because the label names the field as a structural element of the output rather than a formatting convention. When the model sees "BINARY FIELD," it treats that slot as a required type annotation rather than an optional prose note. Tests whether explicit field-type labeling is a more reliable C-13 enforcement mechanism than table columns or checkboxes used without the label.

```
You are running /trace-migration.

Three critical fields apply throughout this analysis. Each is a BINARY FIELD -- fill it
wherever it appears. Do not substitute free-form prose for these fields.

  DATA LOSS RISK (BINARY FIELD):  NONE / TRUNCATION / SILENT DROP / REJECTION
  NOT NULL RISK  (BINARY FIELD):  CLEAR / AT RISK / N/A
  ROLLBACK CLASS (BINARY FIELD):  REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE / N/A

Inputs required:
- Migration script or before/after schema DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

---

## STEP 0: EXECUTION SEQUENCE

List every DDL statement in execution order. This list is the authoritative step registry.
All downstream steps reference entries by step number from this table.

| Step # | DDL Type | Table | Object | What It Does |
|--------|---------|-------|--------|--------------|
| 1 | [type] | [table] | [column/index/constraint] | [one line] |
| 2 | ... | ... | ... | ... |

---

## STEP 1: BEFORE-STATE

One entry per affected entity. Reference each by step number from STEP 0.

Entity: [table.column or table] -- (modified by Step [N])
  Type:        [current type]
  Nullable:    YES / NO
  Default:     [value or "none"]
  Constraints: [list or "none"]
  Row count:   [N or "unknown"]
  NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A
    [CLEAR if Step N does not add NOT NULL to this entity.]
    [AT RISK if Step N adds NOT NULL with no DEFAULT on non-empty table. Explain: row count, DEFAULT status.]
    [N/A if entity is not a column.]

---

## STEP 2: AFTER-STATE AND DATA RISK

One entry per step in execution order. Reference by step number from STEP 0.
Do not reorder or group.

Step N (from STEP 0):
  After type:          [new type or "unchanged"]
  After nullable:      YES / NO (changed from YES/NO -- or "unchanged")
  After default:       [new value / "unchanged" / "removed"]
  Type changed:        YES / NO
  Nullability tightened: YES / NO
  DATA LOSS RISK (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION
    [If TRUNCATION or SILENT DROP: describe which rows, which values, what happens to them.]
    [If NONE or REJECTION: one sentence -- why is data preserved or surfaced as an error rather than silently lost?]

DATA LOSS STATEMENT (required -- check exactly one):
[ ] Data loss paths found: [list each path as: Step N -- column -- value range -- what happens]
[ ] No data loss paths found. Per-step argument:
    Step N: [reason data is preserved or surfaces as error -- not silently lost. One line per destructive step.]

---

## STEP 3: CONSTRAINT RISK

One entry per step that adds or modifies a constraint. Reference by step number from STEP 0.

Step N (from STEP 0):
  Constraint type: [NOT NULL / UNIQUE / FK / CHECK]
  Existing data satisfies new constraint: YES / NO / UNKNOWN
    [If NO or UNKNOWN: which records violate it; how many approximately; migration behavior: FAIL / BACKFILL / SKIP]

[If no constraint changes in this migration:
  "No constraint changes. STEP 0 registry entries [list step numbers] have no
   NOT NULL/UNIQUE/FK/CHECK additions or removals."]

---

## STEP 4: PERFORMANCE RISK

One row per step from STEP 0 registry. Do not omit steps.

| Step # | Lock Class | Lock Duration | Full-Table Rewrite | Replication Risk | Performance Cliff | Row Count |
|--------|-----------|---------------|-------------------|-----------------|-------------------|-----------|
| [N] | NONE/ROW/TABLE/EXCLUSIVE | Instant/Row-count-dependent/Full-rewrite | YES/NO | NONE/LAG/BREAKING | NONE/PRESENT | [N or unknown] |

[If Performance Cliff is PRESENT for any step: add a row below that step describing the specific risk.]
| [N] cliff detail | [lock class explanation] | [duration estimate] | [I/O scope] | [replication impact] | [mitigation note] | |

---

## STEP 5: DOMAIN IMPACT

[Positioned before STEP 6: VERIFY. Complete this section before writing verification content.]
[One entry per step with DATA LOSS RISK of TRUNCATION or SILENT DROP, or Performance Cliff PRESENT.]
[Silence on a flagged step is a failure -- every flagged step requires an entry.]

| Step # | DATA LOSS RISK (Binary) | Business Object | Business Consequence | Domain | Severity |
|--------|------------------------|-----------------|---------------------|--------|----------|
| [N] | TRUNCATION/SILENT DROP/REJECTION | [order/invoice/ledger entry/shipment/SKU/payment/refund] | [concrete consequence -- name value threshold or business condition at risk, not generic db language] | Commerce/Finance/Operations | CRITICAL/HIGH/MEDIUM/LOW |

[If no steps have TRUNCATION, SILENT DROP, or PRESENT cliff:
  "No domain-level risks. Migration is data-safe and performant."]

---

## STEP 6: VERIFY

[STEP 5 must be complete before this step begins. Reference steps by number from STEP 0.]

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| 1 | Step [N] | [e.g., no NULLs in new NOT NULL column] | [query] | [expected] |

---

## STEP 7: ROLLBACK

One entry per destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation, constraint drop).
Reference by step number from STEP 0.

Step N (from STEP 0):
  ROLLBACK CLASS (BINARY FIELD): REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
    [REVERSIBLE: a down migration DDL can undo this step.]
    [BACKUP-ONLY: data is gone from live DB but can be restored from backup.]
    [IRREVERSIBLE: no recovery path exists.]
  Down migration: [DDL to reverse OR "not possible -- data is gone"]
  Notes: [qualifying condition if any -- e.g., "reversible only before Step N+2 runs"]

[If no destructive steps in STEP 0 registry: "No destructive steps. ROLLBACK CLASS: N/A -- migration is fully additive."]

ROLLBACK SUMMARY (required -- check exactly one):
[ ] All steps REVERSIBLE. Down migration covers full undo.
[ ] Mixed reversibility. Steps classified as BACKUP-ONLY or IRREVERSIBLE:
    Step [N]: [ROLLBACK CLASS] -- [what is permanently lost]

---

## STEP 8: ZERO-DOWNTIME AND IDEMPOTENCY

Zero-downtime:
  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] -- [DDL from STEP 0 and specific reason -- lock type, table size, engine behavior]
    Alternative: [expand/contract pattern, online DDL for this engine, OR "none available -- explain why"]

Idempotency per step (extend STEP 0 registry):
  Step [N]: IDEMPOTENT / NOT IDEMPOTENT
    [If NOT IDEMPOTENT: failure mode on second run -- duplicate key / double-applied transform / constraint already exists / other]
  [Repeat for all steps. If all idempotent: "All STEP 0 registry entries safe to run twice."]

---

## VERDICT

  Migration risk:        LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:    REQUIRED / NOT REQUIRED / CONDITIONAL (state condition)
  Safe to run:           YES / NO / CONDITIONAL
  Reversibility:         FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE
  Highest business risk: [One sentence -- Step N from STEP 0, business object, concrete consequence]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found, constraint_violations_found,
irreversible_steps, maintenance_window, idempotent, highest_severity, highest_risk_step.
```

---

## V-04: V-04 Rehabilitation -- Two-Phase: Interrogate Then Trace

**Axis:** C-05 rehabilitation -- Phase A is a directed interrogation organized by analytical concern (any order); Phase B is a mandatory chronological trace table derived from Phase A findings; C-05 is enforced structurally in Phase B because the canonical artifact is built in step order.
**Hypothesis:** Round 1 V-04 failed C-05 because investigative questions organized output by analytical concern, not execution sequence. Separating the format into two phases resolves this: Phase A gathers analytical depth via interrogation (order by concern is acceptable), Phase B synthesizes findings into a step-ordered trace. C-05 passes because the rubric-evaluated artifact (Phase B) is canonically chronological. Tests whether investigative depth and chronological output are compatible when separated into phases.

```
You are running /trace-migration. Two phases: interrogate, then trace.

Phase A gathers knowledge through directed questions. Answers may be organized by concern.
Phase B constructs the canonical step-ordered trace from Phase A findings.
Phase B is the authoritative output -- it is evaluated, not Phase A.

Before Phase A begins: read the migration script and number every DDL statement in execution order.
Keep that numbered list as your working reference. Every Phase A answer must cite step numbers.

---

## PHASE A: INTERROGATION

Answer each question in order. Do not skip a question.
If you cannot answer with certainty, state what you know, what you are inferring, and your
best answer with confidence level.

---

**Q1: What does this migration do?**

List each step in execution order using your numbered reference list:
  Step 1: [DDL type] on [table.object] -- [one-line description]
  Step 2: ...
  [Continue for all steps.]

---

**Q2: For each entity that changes, what is its state before and after?**

Entity: [table.column or table]
  Before: type=[X] | nullable=YES/NO | default=[X or none] | constraints=[list]
  After:  type=[X] | nullable=YES/NO | default=[X or none] | constraints=[list]
  Changed by: Step [N]
  Row count: [N or "unknown"]

---

**Q3: What are the NOT NULL risks?**

For each new NOT NULL column added by any step:
  Step [N], [table.column]:
    DEFAULT provided: YES / NO
    [If NO on non-empty table: "RISK -- NOT NULL with no DEFAULT will fail or require backfill. Row count: [N or unknown]."]
[If no new NOT NULL columns: "No new NOT NULL columns. NOT NULL risk: clear."]

---

**Q4: Could any existing row lose data silently?**

For each step that modifies existing data (type change, precision reduction, column drop, row delete):
  Step [N]: [trace what happens to a row already in the table]
    Value at risk: [describe the value or range]
    What happens: [truncated / dropped / errors if over threshold / other]
    Silent? YES / NO -- [explain why -- does the engine error, or does it silently transform?]

End with (required -- check exactly one):
[ ] Data loss paths found: [list by Step N -- column, value range, what happens]
[ ] No data loss paths found. Per-step reasoning:
    Step [N]: [why this destructive step does not silently lose data]

---

**Q5: Does any existing row violate a new constraint?**

For each new NOT NULL / UNIQUE / FK / CHECK constraint:
  Step [N], [constraint type] on [table.column]:
    Violation possible: YES / NO / UNKNOWN
      [If YES or UNKNOWN: approximate affected row count; migration behavior: FAIL / BACKFILL / SKIP]
      [If NO: brief reason -- table empty? existing data satisfies it? constraint applies only to new inserts?]

---

**Q6: Which steps will be slow on a large table?**

For each step with a full-table rewrite, index rebuild, or row-scan operation:
  Step [N]: table=[name], row count=[N or unknown]
    Risk: [lock duration / I/O spike / replication lag / temp space -- be specific about which]
[If no performance-cliff operations: "No performance cliff operations. C-06 auto-passes with this migration."]

---

**Q7: What does each destructive step do to rollback viability?**

For each step that drops a column, drops a table, narrows a type, truncates data, or drops a constraint:
  Step [N]:
    Rollback class: REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE
    Down migration: [DDL to reverse OR "not possible -- data is gone"]
    Reasoning: [one sentence why this classification]

---

**Q8: What is the real-world consequence if the riskiest step goes wrong?**

Riskiest step: Step [N] -- [name it briefly]
  Business object: [order / invoice / ledger entry / shipment / SKU / payment / refund / subscription]
  Consequence: [concrete -- name the value range, business function, or monetary exposure]
    [Required specificity: name a threshold or condition]
    [Good: "purchase orders over $1M silently truncated to $1,048,575 due to integer overflow"]
    [Bad: "integer precision is reduced"]
  Who notices first: [customer complaint / financial audit / reconciliation mismatch / support ticket / other]
  Domain: Commerce / Finance / Operations
  Severity: CRITICAL / HIGH / MEDIUM / LOW

---

**Q9: Can this migration run without a maintenance window?**

  Viable without downtime: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] -- [operation and why it blocks reads or writes during execution]
    Alternative: [online DDL option for this engine / expand-contract pattern, OR "none available -- explain"]

---

**Q10: Is this migration safe to run twice?**

For each step -- idempotent?
  Step [N]: YES / NO
    [If NO: specific failure mode on second run -- duplicate key / double-applied transform /
     constraint already exists / other]

---

## PHASE B: CHRONOLOGICAL TRACE

[Derived from Phase A findings. Organized strictly by execution order. This is the canonical artifact.]
[Every entry must reference its step number. Do not group by concern, table, or operation type.]
[Phase B is the evaluated output for all rubric criteria.]

### B1: Execution Trace

| Step # | DDL Type | Table | Object | Before (type / nullable / default) | After (type / nullable / default) | DATA LOSS RISK | NOT NULL RISK | Constraint Change | Performance Cliff |
|--------|---------|-------|--------|------------------------------------|-----------------------------------|---------------|--------------|------------------|------------------|
| [N] | [type] | [table] | [object] | [before summary] | [after summary] | NONE/TRUNCATION/SILENT DROP/REJECTION | CLEAR/AT RISK/N/A | [type or none] | NONE/PRESENT |

DATA LOSS STATEMENT (derived from Q4 -- required -- check exactly one):
[ ] Data loss paths found: [list by Step N]
[ ] No data loss paths found. Per-step reasoning: [derive from Q4 per-step arguments]

### B2: Domain Impact (before Verification)

[For each row in B1 with TRUNCATION, SILENT DROP, or PRESENT cliff -- from Q8 and Q6:]

| Step # | Technical Risk | Business Object | Business Consequence | Domain | Severity |
|--------|---------------|-----------------|---------------------|--------|----------|
| [N] | [from B1] | [object] | [concrete consequence from Q8] | Commerce/Finance/Operations | CRITICAL/HIGH/MEDIUM/LOW |

[If no flagged risks in B1: "No domain-level risks. Migration is data-safe and performant."]

### B3: Verification Checks

[Post-migration checks confirming schema and data are in expected state. Reference by Step N.]

| Check # | References Step # | What to Verify | How | Expected Result |
|---------|-------------------|----------------|-----|----------------|
| 1 | Step [N] | [from Q2/Q3/Q5] | [query] | [expected] |

### B4: Rollback Summary

[Derived from Q7. Destructive steps only. Reference by Step N.]

| Step # | Operation | ROLLBACK CLASS | Down Migration DDL |
|--------|-----------|---------------|-------------------|
| [N] | [destructive op from B1] | REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE | [DDL or "not possible"] |

[If no destructive steps: "No destructive steps. Migration is fully reversible."]

### B5: Migration Verdict

  Migration risk:        LOW / MEDIUM / HIGH / CRITICAL
  Maintenance window:    REQUIRED / NOT REQUIRED / CONDITIONAL (from Q9)
  Safe to run:           YES / NO / CONDITIONAL
  Reversibility:         FULLY REVERSIBLE / BACKUP-ONLY / PARTIALLY IRREVERSIBLE / FULLY IRREVERSIBLE (from Q7)
  Zero-downtime viable:  YES / NO / PARTIAL (from Q9)
  Idempotent:            YES / NO / PARTIAL (from Q10)
  Highest business risk: [One sentence -- Step N from B1, business object, concrete consequence from Q8]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found, constraint_violations_found,
irreversible_steps, maintenance_window, idempotent, highest_severity, highest_risk_step.
```

---

## V-05: Full v2 Synthesis -- All Three New Criteria + Phase Gates

**Axis:** Full v2 synthesis -- V-05 R1 base with all three new aspirational mechanisms added explicitly: step registry as named contract with cross-reference mandate (C-11), domain gate checkpoint between EXECUTE and VERIFY (C-12), binary field labels for all three critical dimensions everywhere they appear (C-13).
**Hypothesis:** V-05 R1 scored 100/100 but was designed against the 10-criterion rubric. Under v2 (13 criteria, 115 pts), it earns C-11 and C-12 via structure but lacks explicit enforcement for C-13's binary field requirement. Adding "BINARY FIELD" labels to all three critical dimensions and an explicit DOMAIN GATE binary converts V-05's structural positioning wins into explicit mechanism wins -- targeting 115/115 with no criterion relying on positional luck alone.

```
You are running /trace-migration. Finance expert leads this analysis.
Data integrity is the primary concern. Domain impact is gated before verification.

Three critical fields are BINARY throughout this analysis. Fill each wherever it appears.
Free-form prose may not substitute for these fields:
  DATA LOSS RISK   (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION
  NOT NULL RISK    (BINARY FIELD): CLEAR / AT RISK / N/A
  ROLLBACK CLASS   (BINARY FIELD): REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE / N/A

All section headers, table column headers, and pre-printed fields are fixed.
Do not omit, merge, or rename them. Fill every cell.
Write "none" or "N/A" only when genuinely not applicable -- explain why.

Inputs required:
- Migration script or before/after DDL
- Database engine (PostgreSQL / MySQL / SQL Server / SQLite / other)
- Row counts for affected tables (state "unknown" if not provided)
- Domain context (infer from table names if not stated)

State any inferences before proceeding.

---

## PARSE: STEP REGISTRY (AUTHORITATIVE NAMED ARTIFACT)

[Finance expert locks execution order before any analysis begins.]
[This table is the step registry. All downstream phases extend it by step number.]
[Do not reorder. Do not group. Downstream phases reference entries as "Step N from registry."]

| Step # | DDL Type | Table | Object (column/index/constraint) | Operation Summary |
|--------|---------|-------|----------------------------------|-------------------|
| 1 | [type] | [table] | [object] | [one line -- what the engine does] |
| 2 | ... | ... | ... | ... |

Registry count: [N] steps.

---

## PRE-FLIGHT GATE (Finance)

[Must be OPEN before EXECUTE phase begins. Extends Step Registry with before-state and NOT NULL risk.]

### Before-State per Affected Entity

[One row per entity that changes state. References step that changes it.]

| Entity (table.column) | Modified by Step # | Current Type | Nullable | Default | Constraints | Row Count |
|-----------------------|--------------------|-------------|---------|---------|-------------|-----------|
| [table.col] | [N] | [type] | YES/NO | [value or none] | [list or none] | [N or unknown] |

### NOT NULL + DEFAULT Audit

[Extends Step Registry: NOT NULL RISK (BINARY FIELD) per column that adds NOT NULL.]

For each new NOT NULL column added by any step in the registry:

  Step [N], [table.column]:
    NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK
    DEFAULT provided: YES / NO
    [If AT RISK: "NOT NULL with no DEFAULT on [N or unknown] rows.
     Migration will fail unless table is empty or backfill precedes Step [N]."]

[If no new NOT NULL additions in registry:
  "NOT NULL RISK (BINARY FIELD): CLEAR -- no new NOT NULL columns in step registry."]

PRE-FLIGHT GATE: OPEN / BLOCKED
  [BLOCKED if: any entity before-state is undocumented, or NOT NULL RISK is AT RISK
   without a remediation plan present in the migration script.]

---

## EXECUTE PHASE (Finance + Operations)

[PRE-FLIGHT GATE must be OPEN. Extends Step Registry with after-state and risk per step.]
[Steps appear in registry order. Do not reorder or group.]

### Entity State Changes

[Extends Step Registry: after-state columns for each step that changes a column or table.]

| Step # | Entity | After Type | After Nullable | After Default | Type Changed | Nullability Tightened | Constraint Added |
|--------|--------|-----------|----------------|---------------|-------------|----------------------|-----------------|
| [N] | [table.col] | [type] | YES/NO | [value or none] | YES/NO | YES/NO | [type or none] |

### Data Loss and Constraint Risk

[Extends Step Registry: DATA LOSS RISK (BINARY FIELD) and constraint assessment per step.]

| Step # | DATA LOSS RISK | Data Loss Description | Constraint Change | Existing Data Satisfies | Migration Handles Violation As |
|--------|---------------|----------------------|-------------------|------------------------|-------------------------------|
| [N] | NONE/TRUNCATION/SILENT DROP/REJECTION | [describe concretely or write "none"] | [type or "none"] | YES/NO/UNKNOWN/N/A | FAIL/BACKFILL/SKIP/N/A |

DATA LOSS STATEMENT (BINARY -- check exactly one):
[ ] Data loss paths found: Step [N]: [column -- value range -- what happens to it]
[ ] No data loss paths found. Per-step reasoning (one line per destructive step in registry):
    Step [N]: [why data is preserved or surfaced as error -- not silently dropped]

### Operational Risk per Step

[Extends Step Registry: lock class and performance cliff per step.]

| Step # | Lock Class | Lock Duration | Full-Table Rewrite | Replication Risk | Performance Cliff | Rows Affected |
|--------|-----------|---------------|-------------------|-----------------|-------------------|---------------|
| [N] | NONE/ROW/TABLE/EXCLUSIVE | Instant/Row-count-dependent/Full-rewrite | YES/NO | NONE/LAG/BREAKING | NONE/PRESENT | [N or unknown] |

[If Performance Cliff is PRESENT: add a line below that row describing lock duration, I/O scope, and mitigation.]

---

## DOMAIN IMPACT GATE (Commerce / Finance / Operations)

[Runs immediately after EXECUTE PHASE. VERIFY PHASE may not begin until DOMAIN GATE is OPEN.]
[Extends Step Registry: business consequence for each step with TRUNCATION, SILENT DROP, or PRESENT cliff.]
[Silence on a flagged step is a gate failure -- every such step requires an entry.]

| Step # | DATA LOSS RISK (Binary) | Business Object | Business Consequence | Domain | Severity |
|--------|------------------------|-----------------|---------------------|--------|----------|
| [N] | TRUNCATION/SILENT DROP/REJECTION/PRESENT cliff | [order/invoice/ledger entry/shipment/SKU/payment/refund/subscription] | [concrete consequence -- name value threshold or business condition; not generic db language] | Commerce/Finance/Operations | CRITICAL/HIGH/MEDIUM/LOW |

[If no TRUNCATION, SILENT DROP, or PRESENT cliff in EXECUTE:
  "No data loss or performance cliff risks in step registry.
   Domain assessment: migration is data-safe and performant. No business objects at risk."]

DOMAIN GATE: OPEN / BLOCKED
  [BLOCKED if: any step with TRUNCATION, SILENT DROP, or PRESENT cliff has no entry in this table.
   Name the missing step number and state what domain assessment is needed to resolve the block.]

---

## VERIFY PHASE

[DOMAIN GATE must be OPEN before this phase begins. References steps by number from Step Registry.]

| Check # | References Step # | What to Verify | How to Verify | Expected Result |
|---------|-------------------|----------------|---------------|----------------|
| 1 | Step [N] | [e.g., no NULLs in new NOT NULL column] | [e.g., SELECT COUNT(*) WHERE col IS NULL] | [0 rows] |
| 2 | Step [N] | [e.g., FK references resolve] | [JOIN query] | [0 orphaned rows] |

---

## ROLLBACK PHASE

[Extends Step Registry: ROLLBACK CLASS (BINARY FIELD) for each destructive step.]
[Reverse execution order. Classify each step that drops a column/table, narrows a type, truncates data.]

| Step # | Original Operation | ROLLBACK CLASS | Down Migration DDL | Notes |
|--------|--------------------|---------------|-------------------|-------|
| [N] | [DDL from EXECUTE] | REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE | [DDL to reverse or "not possible -- data is gone"] | [qualifying condition if any] |

[If no destructive steps in registry:
  "No destructive steps. ROLLBACK CLASS: N/A -- migration is fully reversible by re-running down migration."]

ROLLBACK SUMMARY:
  Irreversible steps present: YES / NO
    [If YES: Step [N] -- [what is permanently lost]]

---

## ZERO-DOWNTIME AND IDEMPOTENCY

[Extends Step Registry. References blocking steps by number.]

Zero-downtime:
  Viable: YES / NO / PARTIAL
  [If NO or PARTIAL:]
    Blocking step: Step [N] -- [DDL from registry and specific reason -- lock type, table size, engine behavior]
    Alternative: [expand/contract pattern, online DDL for this engine, OR "none available -- explain why"]

Idempotency (extends Step Registry -- one row per step):
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
  Highest business risk:    [One sentence -- Step N from registry, business object, concrete consequence,
                             quantify value threshold if possible]

---

Write artifact: simulations/trace/migration/{topic}-migration-{date}.md
Frontmatter: skill, topic, date, engine, domain, step_count, data_loss_found,
constraint_violations_found, irreversible_steps, maintenance_window, idempotent,
highest_severity, highest_risk_step.
```

---

## Predicted Score Summary

| V | C-11 Mechanism | C-12 Mechanism | C-13 Mechanism | Predicted Score |
|---|---|---|---|---|
| V-01 | Section headers mandate "extends Step Registry by step number" + prohibition on re-describing by name | SECTION 5 Domain Impact before SECTION 6 Verify | DATA LOSS STATEMENT checkbox + NOT NULL check binary per entity + ROLLBACK SUMMARY checkbox | 115 |
| V-02 | PARSE steps numbered; EXECUTE/VERIFY/ROLLBACK cite "by step number from PARSE" | DOMAIN GATE: OPEN/BLOCKED checkpoint; VERIFY blocked until gate resolves | DATA LOSS STATEMENT checkbox; NOT NULL: YES/NO with BLOCKED consequence; rollback taxonomy | 115 |
| V-03 | STEP 0 registry; STEP 2/3/7 all say "Reference by step number from STEP 0" | STEP 5 Domain Impact before STEP 6 Verify | "BINARY FIELD" label with explicit taxonomy for all three critical dimensions; free-form prohibited | 115 |
| V-04 | Phase B intro: "Every entry must reference its step number"; Q1 numbered list maintained through all Q answers | Phase B: Domain Impact (B2) before Verification Checks (B3) | DATA LOSS STATEMENT checkbox in Q4; NOT NULL YES/NO in Q3; ROLLBACK CLASS taxonomy in Q7 and B4 | 115 |
| V-05 | "AUTHORITATIVE NAMED ARTIFACT" label; all phases say "extends Step Registry by Step N"; cross-reference mandate in every phase header | DOMAIN IMPACT GATE: OPEN/BLOCKED between EXECUTE and VERIFY; VERIFY blocked until gate resolves | "BINARY FIELD" labels on all three critical dimensions throughout; explicit free-form prohibition | 115 |

**Key differentiators:**
- C-11 strength ranking: V-01 > V-05 > V-03 > V-02 > V-04 (V-01 has explicit prohibition on re-describing; V-05 uses "extends" framing consistently)
- C-12 strength ranking: V-02 = V-05 (gate binary) > V-01 = V-03 = V-04 (positional only)
- C-13 strength ranking: V-03 > V-05 (BINARY FIELD labels everywhere) > V-01 = V-02 = V-04 (checkboxes and taxonomy without label)
- C-05 strength ranking: V-05 > V-02 (phase gates) > V-01 = V-03 (step registry) > V-04 (Phase B enforces; Phase A can drift)
