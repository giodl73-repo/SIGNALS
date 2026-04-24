Written to `simulations/quest/variations/trace-migration-variations-R4-2026-03-14.md`.

---

## Round 4 Variations — trace-migration

**The gap from v3 to v4:** R3 V-05 scored 130/130. v4 adds C-17 (gate field annotation compound) and C-18 (named artifact citation) — both were excellence signals in R3 V-05. R4's job is to pre-print both so they're structurally unavoidable, not emergent.

| V | Axis | Mechanism | Predicted |
|---|------|-----------|-----------|
| **V-01** | Role sequence: Finance→Ops→Commerce (two-phase) | Finance-first surfaces amount truncation before structural trace. C-17 pre-printed at Phase A→B domain gate. C-18 in global Phase A citation rule + every Q body. | 140 |
| **V-02** | Output format: All-table, single-phase | Pre-printed GATE STATE TABLE with "(BINARY FIELD)" column header guarantees C-17. Citation rule in SECTION 0 header: "Step N from SECTION 0 REGISTRY" everywhere. | 140 |
| **V-03** | Lifecycle emphasis: 5-gate chain, single-phase | 5 gate fields pre-printed with "(BINARY FIELD): OPEN / BLOCKED" — compound fires at every boundary. Citation instruction repeated in each phase: "Step N from PARSE PHASE REGISTRY." | 140 |
| **V-04** | Combined: Commerce-first + table-driven Phase B | Commerce-first strengthens C-08 for e-commerce schema changes. Phase B table column headers carry type annotations as a synthesis contract. C-17 at Phase A→B gate. | 140 |
| **V-05** | Combined: Lifecycle + conversational phrasing | 3 pre-printed gate fields with "(BINARY FIELD)" — DOMAIN GATE, VERIFY GATE, VERDICT GATE. Conversational register lowers generic-description drift, improving C-08 quality in live runs. C-18 in global rule + every Q that cites steps. | 140 |

---

### Key design decisions for R4

**C-17 mechanism**: All five variations pre-print at least one gate state field as `GATE NAME (BINARY FIELD): OPEN / BLOCKED` — not as an instruction to the model but as a literal label in the template. The model fills in `OPEN` or `BLOCKED` at that pre-printed field. V-03 does this at 5 gates; V-05 at 3 gates (DOMAIN, VERIFY, VERDICT).

**C-18 mechanism**: All five variations pre-print the source artifact name in citation instructions. Two-phase variations (V-01, V-04, V-05) use `"Step N from Q1"` in a global Phase A rule and repeat it in every Q body. Single-phase variations (V-02, V-03) embed the instruction in the section header: `"cite steps as 'Step N from SECTION 0 REGISTRY'"` / `"Step N from PARSE PHASE REGISTRY."` The instruction appears at the definition site, not only at the registry.

**Within-140 structural guarantee ranking** (C-17 surfaces):

| Strength | Variation | C-17 surfaces | C-18 surfaces |
|----------|-----------|---------------|---------------|
| Strongest | V-03 | 5 (one per gate) | 5 (one per phase) |
| Strong | V-05 | 3 (DOMAIN + VERIFY + VERDICT) | 11 (global + every Q) |
| Moderate | V-01, V-04 | 1 (Phase A→B gate) | 10 (global + every Q) |
| Moderate | V-02 | 1 (GATE STATE TABLE column header) | 1 (SECTION 0 header) |

**New patterns for potential v5 rubric candidates:**

1. **Verdict-level gate** (V-05 B5): A VERDICT GATE that blocks on REQUIRES REMEDIATION without listed remediation steps creates a third enforcement level — not just domain and verify gates but a final go/no-go gate at the output. No existing criterion covers this level.

2. **Multi-gate C-17 chain** (V-03): Applying C-17 at all 5 gates creates a structural guarantee stronger than C-17's minimum requirement (at least one gate). The pass condition for C-17 would pass all five variations, but the within-140 structural guarantee is substantially different.

3. **Table column header as type annotation site** (V-02): The column header `DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION` makes the type annotation travel with every row rather than appearing once in instruction text. This is a stronger structural guarantee than an instruction-based annotation.
 | ...  | ...                  |

*This is the Q1 STEP REGISTRY. Cite all Phase A steps as "Step N from Q1."*

---

### Q2 — Finance Expert Lens (run first)

*You are a Finance migration expert. Domain: amounts, decimal precision, ledger integrity, invoice records, refund processing, subscription billing.*

For each table or column that supports financial records:

**Before state:** column type, precision, nullability, constraint state before the migration.
**After state:** what has changed after each relevant step from Q1.

**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
For any step from Q1 that narrows a numeric type or reduces decimal precision: does it silently truncate financial values? Reference each affected step as "Step N from Q1."
If TRUNCATION or SILENT DROP: name the concrete Finance consequence with a dollar threshold. Example: "Step 2 from Q1 reduces decimal(19,4) to decimal(10,2) — invoices over $9,999,999.99 silently capped, revenue recognition error." Generic database terminology ("precision is reduced") does not satisfy this field.

**NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**
For any step from Q1 that adds a NOT NULL column to a financial table: is a DEFAULT provided?
If AT RISK: name the column, the financial table, an estimated row count if derivable from context, and the required backfill instruction.

---

### Q3 — Operations Expert Lens (second)

*You are an Operations migration expert. Domain: shipments, fulfillment status, inventory counts, order-in-flight records, workflow state transitions.*

For each table or column that supports operational workflows:

**Before state / After state** per changed column or constraint. Reference each step as "Step N from Q1."

**Constraint change analysis:** For each FK, CHECK, or UNIQUE constraint change (not constraints unchanged before and after): does existing operational data satisfy the new constraint? If not: name which records violate it and what the migration does (fail-hard, skip silently, backfill).

**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
Any step from Q1 that can silently drop rows or discard column data without surfacing an error? Reference as "Step N from Q1."

**NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**
Same assessment as Q2 but for operational tables.

---

### Q4 — Commerce Expert Lens (third)

*You are a Commerce migration expert. Domain: orders, carts, SKUs, product catalog, customer deduplication, pricing records.*

For each table or column that supports customer-facing operations:

**Before state / After state.** Reference steps as "Step N from Q1."

**UNIQUE constraint changes:** Does any UNIQUE constraint removal or modification affect order deduplication or SKU uniqueness? Name the business object and the specific duplication risk. Example: "Step 4 from Q1 drops UNIQUE on orders.external_ref — duplicate orders from retry storms become possible."

**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION**
Reference any loss-risk step as "Step N from Q1."

**Commerce consequence:** Name the concrete customer-facing consequence with a threshold or count scenario.

---

### Q5 — Execution Order Check

Review the Q1 STEP REGISTRY. Are there ordering dependencies (a step must execute before another for correctness)? List any dependency, citing both steps as "Step N from Q1."

---

### Q6 — Performance Cliffs

For each step from Q1 that touches a large or high-traffic table:

**PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT** — "Step N from Q1."
If PRESENT: table name, operation type (full-table rewrite, index rebuild, type cast requiring row scan), estimated row count if derivable, and the specific risk (lock duration, I/O spike, replication lag).

---

### Q7 — Rollback Viability

For each destructive step from Q1 (DROP COLUMN, DROP TABLE, type narrowing, data truncation):

**ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY): FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE** — "Step N from Q1."
Brief rationale per step.

---

### Q8 — Zero-Downtime and Idempotency

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
If NO or PARTIAL: blocking step as "Step N from Q1" — why it requires a maintenance window.

For each step from Q1:
**IDEMPOTENT (BINARY FIELD): YES / NO** — If NO: failure mode on second run. "Step N from Q1."

---

### Q9 — Data Loss Summary

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS PATHS — [argument: why no step from Q1 silently drops rows, truncates values, or discards columns without surfacing an error]
- [ ] DATA LOSS PATHS EXIST — [list: "Step N from Q1 — what is lost, does an error surface?"]

---

## DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED

Review Q2 (Finance), Q3 (Operations), Q4 (Commerce). Set to BLOCKED if any DATA LOSS field is TRUNCATION, SILENT DROP, or REJECTION and has no documented mitigation in the relevant Q section.

**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
Blocking step (if BLOCKED): Step N from Q1 — [reason]
Required mitigation (if BLOCKED): [what must be resolved before Phase B]

*Phase B begins only when DOMAIN GATE (BINARY FIELD) = OPEN.*

---

## PHASE B — CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)

*Authoritative, chronologically ordered output. Satisfies C-05. Organized strictly by execution order from Q1 STEP REGISTRY. Do not reorder, regroup, or rename steps. All step citations in Phase B use "Step N from Q1."*

---

### B1 — Step-Ordered Trace Table

One row per step from Q1 STEP REGISTRY, in execution order. Do not omit any step. Do not leave any binary field blank — a blank cell means the criterion was not assessed.

| Step (Q1) | Statement | Before State | After State | DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) | ROLLBACK CLASS (FIXED TAXONOMY) | PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |
|-----------|-----------|--------------|-------------|--------------------------|------------------------------|----------------------------------|--------------------------|--------------------------|
| 1         | ...       | ...          | ...         | NONE/TRUNCATION/SILENT DROP/REJECTION | CLEAR/AT RISK/N/A | FULLY_REVERSIBLE/BACKUP_ONLY/IRREVERSIBLE | NONE/PRESENT | YES/NO |

---

### B2 — Domain Impact (POSITIONED BEFORE B3 VERIFY — complete before writing B3)

Synthesize Q2, Q3, Q4 findings into concrete domain consequences:

**Finance impact:** [Specific consequence with dollar threshold — name the business object: invoice, ledger entry, refund, subscription charge. Cite step as "Step N from Q1."]

**Operations impact:** [Specific consequence — name shipment state, inventory record, fulfillment workflow. Cite step as "Step N from Q1."]

**Commerce impact:** [Specific consequence — name order, SKU, cart, or product object. Cite step as "Step N from Q1."]

At least one domain consequence must include a numeric threshold (dollar amount, record count, or business event frequency).

---

### B3 — Verification (requires DOMAIN GATE = OPEN before writing this section)

- [ ] All steps from Q1 STEP REGISTRY appear in B1 in execution order
- [ ] Every DATA LOSS (BINARY FIELD) in B1 has a value — no blanks
- [ ] Every NOT NULL RISK (BINARY FIELD) in B1 has a value — no blanks
- [ ] Every ROLLBACK CLASS uses exactly: FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE
- [ ] DATA LOSS STATEMENT in Q9 has exactly one box checked
- [ ] DOMAIN GATE (BINARY FIELD) is resolved to OPEN or BLOCKED — not blank or prose
- [ ] B2 Domain Impact appears before this section

---

### B4 — Rollback Summary

For each step from B1 with ROLLBACK CLASS != FULLY_REVERSIBLE:

| Step (Q1) | Rollback class | Recovery path | Estimated data window at risk |
|-----------|----------------|---------------|-------------------------------|
| ...       | BACKUP_ONLY    | ...           | ...                           |

---

### B5 — Verdict

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
Blocking step (if NO or PARTIAL): Step N from Q1 — [maintenance window requirement]

**IDEMPOTENCY SUMMARY (BINARY FIELD): SAFE / UNSAFE / MIXED**
Non-idempotent steps (if UNSAFE or MIXED): Step N from Q1 — [failure mode on re-run]

**Migration risk level:** SAFE TO RUN / RUN WITH PRECAUTIONS / REQUIRES REMEDIATION
Primary risk: [one sentence naming the risk type and affected domain]
Required action before production: [one sentence]

---

---

## V-02: Single-Axis — Output Format (All-Table, Single-Phase)

**Axis:** Output format — pre-printed table templates replace prose analytical sections; single-phase execution-ordered structure.
**Hypothesis:** Pre-printed table column headers with type annotations make C-13 and C-14 structurally unavoidable — blank cells are visually detectable and column headers carry the type annotation to every row. A single-phase all-table format satisfies C-05 directly. C-17 is guaranteed by a pre-printed GATE STATE TABLE with a "(BINARY FIELD)" column header at the gate state field. C-18 is guaranteed by the citation instruction embedded in the SECTION 0 header: "all subsequent sections reference steps as 'Step N from SECTION 0 REGISTRY.'"

---

You are a senior database migration analyst. Fill in every pre-printed table below — blank cells are structural omissions, not acceptable defaults. Complete sections in order.

Migration to analyze:

```
{migration}
```

---

## SECTION 0 — STEP REGISTRY (AUTHORITATIVE ARTIFACT)

Parse the migration. Assign a step number to each DDL or DML statement in execution order.

*Citation instruction: all subsequent sections reference steps as "Step N from SECTION 0 REGISTRY." Do not describe steps by DDL text when a step number is available.*

| Step | Statement (abbreviated) | Type (DDL/DML/DCL) | Primary Table/Entity |
|------|-------------------------|---------------------|----------------------|
| 1    | ...                     | ...                 | ...                  |

---

## SECTION 1 — BEFORE/AFTER STATE TABLE

One row per changed entity (table, column, constraint, index). "Changed" includes: additions, removals, type changes, nullability changes, constraint changes. Omitting an entity is a structural failure.

| Step (SECTION 0) | Entity (table.column or table.constraint) | Change type | Before state (type / nullability / constraint) | After state |
|------------------|-------------------------------------------|-------------|------------------------------------------------|-------------|
| Step N from SECTION 0 REGISTRY | ...           | ADD / DROP / MODIFY | ...                              | ...         |

---

## SECTION 2 — CRITICAL RISK TABLE

One row per step from SECTION 0 REGISTRY. Steps with no risk still require a row with all binary fields filled. Do not leave any binary field blank.

| Step (SECTION 0) | DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION | NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A | ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY): FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE | PERF CLIFF (BINARY FIELD): NONE / PRESENT | IDEMPOTENT (BINARY FIELD): YES / NO |
|------------------|------------------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------|
| Step N from SECTION 0 REGISTRY | ...                                                 | ...                                                 | ...                                                                                           | ...                                       | ...                                 |

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS PATHS — [argument: cite each relevant step as "Step N from SECTION 0 REGISTRY" and state why it does not silently discard data]
- [ ] DATA LOSS PATHS EXIST — [list: "Step N from SECTION 0 REGISTRY — what is lost, does an error surface?"]

**NOT NULL RISK DETAIL** (fill only for rows where NOT NULL RISK = AT RISK):
Column: [table.column] | Table row count: [estimate or "unknown"] | DEFAULT provided: YES / NO | Required backfill value: [value or instruction]

**PERF CLIFF DETAIL** (fill only for rows where PERF CLIFF = PRESENT):
Step N from SECTION 0 REGISTRY | Table: [name] | Operation: [full-table rewrite / index rebuild / row scan] | Estimated rows: [count] | Risk: [lock duration / I/O spike / replication lag]

**ROLLBACK DETAIL** (fill only for rows where ROLLBACK CLASS != FULLY_REVERSIBLE):
Step N from SECTION 0 REGISTRY | Recovery path: [description] | Data window at risk: [estimate]

---

## SECTION 3 — CONSTRAINT CHANGE TABLE

One row per constraint change (NOT NULL, UNIQUE, FK, CHECK) in the migration. Only constraints that change — not constraints unchanged before and after.

| Step (SECTION 0) | Constraint type | Before state | After state | Existing data violates new constraint? (YES / NO / UNKNOWN) | Migration action (FAIL / SKIP / BACKFILL / N/A) |
|------------------|-----------------|--------------|-------------|-------------------------------------------------------------|--------------------------------------------------|
| Step N from SECTION 0 REGISTRY | ...     | ...          | ...         | ...                                                         | ...                                              |

---

## SECTION 4 — DOMAIN IMPACT TABLE

*(Positioned before SECTION 5 GATE CHECK. Complete before writing SECTION 5.)*

| Domain | Business object | Step (SECTION 0) | Risk condition | Concrete consequence (threshold required — $ amount, record count, or business event frequency) |
|--------|----------------|------------------|----------------|--------------------------------------------------------------------------------------------------|
| Finance | invoice / ledger entry / refund / subscription | Step N from SECTION 0 REGISTRY | [specific condition] | [$ threshold — e.g., "charges over $X silently truncated"] |
| Operations | shipment / inventory / fulfillment record | Step N from SECTION 0 REGISTRY | [specific condition] | [operational scenario with record count or state] |
| Commerce | order / SKU / cart / product | Step N from SECTION 0 REGISTRY | [specific condition] | [customer-facing scenario] |

Rows with generic descriptions ("data may be affected") do not satisfy this section. At least one row must include a numeric threshold.

---

## SECTION 5 — GATE STATE TABLE

| Gate | Criterion | GATE STATE (BINARY FIELD): OPEN / BLOCKED | Blocking step (if BLOCKED) | Required action (if BLOCKED) |
|------|-----------|------------------------------------------|----------------------------|------------------------------|
| DOMAIN GATE | All DATA LOSS PATHS EXIST entries in SECTION 2 have a documented domain consequence in SECTION 4 | OPEN / BLOCKED | Step N from SECTION 0 REGISTRY | ... |
| VERIFY GATE | All binary fields in SECTION 2 are filled (no blanks) | OPEN / BLOCKED | Step N from SECTION 0 REGISTRY | ... |

*SECTION 6 may not be written until both GATE STATE (BINARY FIELD) values above are OPEN.*

---

## SECTION 6 — OPERATIONAL ASSESSMENT (requires DOMAIN GATE = OPEN and VERIFY GATE = OPEN)

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
Blocking step (if NO or PARTIAL): Step N from SECTION 0 REGISTRY — [maintenance window requirement]

**Idempotency failures** (from SECTION 2 rows where IDEMPOTENT = NO):

| Step (SECTION 0) | Failure mode on second run |
|------------------|---------------------------|
| Step N from SECTION 0 REGISTRY | ... |

---

## SECTION 7 — VERDICT

**Migration risk level:** SAFE TO RUN / RUN WITH PRECAUTIONS / REQUIRES REMEDIATION
Primary risk: [one sentence — name type, step as "Step N from SECTION 0 REGISTRY," and affected domain]
Required action before production: [one sentence]

---

---

## V-03: Single-Axis — Lifecycle Emphasis (5-Gate Chain, Single-Phase)

**Axis:** Lifecycle emphasis — five explicit gate states control progression through the migration trace. Each gate state field is pre-printed with "(BINARY FIELD): OPEN / BLOCKED." Single-phase, execution-ordered structure.
**Hypothesis:** Gate state fields pre-printed with "(BINARY FIELD)" at every phase boundary eliminate C-15 and C-17 simultaneously — the compound fires at every boundary, not just one. Each downstream section header names its prerequisite gate state as a precondition. The five-gate structure creates a mechanical dependency chain that forces binary resolution at each step before progression. C-18 is pre-printed in the PARSE PHASE header: "cite all steps as 'Step N from PARSE PHASE REGISTRY'" — this instruction appears again in each phase section where citation is required.

---

You are a senior database migration analyst. Complete each phase in order. A BLOCKED gate means STOP — do not write the next phase until the blocker is resolved.

Migration to analyze:

```
{migration}
```

---

## PARSE PHASE — STEP REGISTRY

*Citation instruction: all subsequent phases reference steps as "Step N from PARSE PHASE REGISTRY." This instruction applies in every phase below.*

Parse the migration into a numbered step list in execution order.

| Step | Statement (abbreviated) | Type | Table/Entity |
|------|-------------------------|------|--------------|
| 1    | ...                     | ...  | ...          |

**PARSE GATE (BINARY FIELD): OPEN / BLOCKED**
Criterion: Every migration statement has a step number assigned. No unassigned statements remain.
PARSE GATE (BINARY FIELD): OPEN / BLOCKED
If BLOCKED: [list unassigned statements]

---

## TRACE PHASE (requires PARSE GATE = OPEN)

For each changed entity (table, column, constraint, index) — "changed" means added, dropped, type-changed, nullability-changed, or constraint-changed:

**Before state:** type / nullability / constraint / value range before the migration.
**After state:** type / nullability / constraint after "Step N from PARSE PHASE REGISTRY."

**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION** — cite affected step as "Step N from PARSE PHASE REGISTRY."

**NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A** per new NOT NULL column.
If AT RISK: column and table, DEFAULT provided (YES/NO), row count estimate, backfill instruction.

**Constraint change analysis:** For each constraint that changes:
Before state / After state. Does existing data satisfy the new constraint? YES / NO / UNKNOWN. Migration action: FAIL / SKIP / BACKFILL.

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS PATHS — [argument citing "Step N from PARSE PHASE REGISTRY" for each safe step]
- [ ] DATA LOSS PATHS EXIST — [list: "Step N from PARSE PHASE REGISTRY — what is lost, does an error surface?"]

**TRACE GATE (BINARY FIELD): OPEN / BLOCKED**
Criterion: Every changed entity has explicit Before and After state. DATA LOSS STATEMENT has exactly one box checked. All NOT NULL RISK = AT RISK entries have a backfill instruction.
TRACE GATE (BINARY FIELD): OPEN / BLOCKED
Blocking entry (if BLOCKED): [entity or Step N from PARSE PHASE REGISTRY] — [what is missing]

---

## DOMAIN IMPACT PHASE (requires TRACE GATE = OPEN)

Apply Commerce, Finance, and Operations domain lenses. Name concrete business consequences — not database terminology.

**Finance lens:** For each step from PARSE PHASE REGISTRY affecting financial amounts:
Business object: invoice / ledger entry / refund / subscription charge
Consequence: [specific — name dollar threshold. Example: "Step 3 from PARSE PHASE REGISTRY reduces decimal(19,4) to decimal(10,2) on payment_amount — charges over $9,999,999.99 silently capped."]

**Operations lens:** For each step from PARSE PHASE REGISTRY affecting operational workflow data:
Business object: shipment / inventory record / fulfillment status / order-in-flight
Consequence: [specific operational consequence with record count or workflow state scenario]

**Commerce lens:** For each step from PARSE PHASE REGISTRY affecting customer-facing data:
Business object: order / cart / SKU / product listing
Consequence: [specific customer-facing consequence with threshold]

At least one lens must include a numeric threshold. Generic descriptions ("data may be lost") do not satisfy this phase.

**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
Criterion: At least one domain lens includes a concrete consequence with a numeric threshold. All DATA LOSS PATHS EXIST entries from TRACE PHASE have a domain consequence assigned.
DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED
Blocking entry (if BLOCKED): [domain or Step N from PARSE PHASE REGISTRY] — [what is missing or unresolved]

---

## PERFORMANCE AND ROLLBACK PHASE (requires DOMAIN GATE = OPEN)

**Performance cliffs:** For each step from PARSE PHASE REGISTRY on a large table:
PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT — "Step N from PARSE PHASE REGISTRY."
If PRESENT: table, operation type (full-table rewrite / index rebuild / row scan), estimated rows, risk type (lock duration / I/O spike / replication lag).

**Zero-downtime viability:**
ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL
Blocking step (if NO/PARTIAL): Step N from PARSE PHASE REGISTRY — [lock type, table scale issue, maintenance window estimate]

**Idempotency:** For each step from PARSE PHASE REGISTRY:
IDEMPOTENT (BINARY FIELD): YES / NO
If NO: failure mode on second run — Step N from PARSE PHASE REGISTRY — [specific error or data corruption]

**Rollback viability:** For each destructive step from PARSE PHASE REGISTRY:
ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY): FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE
Recovery path and data window at risk.

**OPERATIONAL GATE (BINARY FIELD): OPEN / BLOCKED**
Criterion: All PERFORMANCE CLIFF, ZERO-DOWNTIME VIABLE, and IDEMPOTENT fields are filled. All destructive steps have a ROLLBACK CLASS.
OPERATIONAL GATE (BINARY FIELD): OPEN / BLOCKED
Blocking entry (if BLOCKED): Step N from PARSE PHASE REGISTRY — [what is missing]

---

## VERIFY PHASE (requires OPERATIONAL GATE = OPEN)

- [ ] All steps from PARSE PHASE REGISTRY appear in TRACE PHASE in execution order
- [ ] DATA LOSS STATEMENT has exactly one box checked
- [ ] All NOT NULL RISK = AT RISK entries have a backfill instruction
- [ ] All ROLLBACK CLASS values use only: FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE
- [ ] DOMAIN GATE (BINARY FIELD) is OPEN — not blank, not prose
- [ ] DOMAIN IMPACT PHASE appears before this section

**VERIFY GATE (BINARY FIELD): OPEN / BLOCKED**
Criterion: All checklist items above are checked.
VERIFY GATE (BINARY FIELD): OPEN / BLOCKED

---

## VERDICT (requires VERIFY GATE = OPEN)

**Migration risk level:** SAFE TO RUN / RUN WITH PRECAUTIONS / REQUIRES REMEDIATION
Primary risk (cite as Step N from PARSE PHASE REGISTRY): [one sentence]
Required action before production: [one sentence]

---

---

## V-04: Combined — Role Sequence + Output Format (Commerce First, Table-Driven Phase B)

**Axes:** Role sequence (Commerce expert first, Finance second, Operations third) + Output format (Phase B uses pre-printed table templates with annotated column headers).
**Hypothesis:** Commerce-first ordering brings customer-facing deduplication and order uniqueness risks to the top of the domain analysis — the most common trace-migration use case for e-commerce schema changes. The combination with table-driven Phase B produces the strongest C-08 + C-14 compound: Phase A establishes Commerce/Finance/Operations framing free-form, Phase B enforces type-annotated column headers as a synthesis contract. C-17 is pre-printed at the Phase A→B domain gate: "DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED." C-18 is pre-printed in the Phase A global instruction, with the source artifact named in every Q body.

---

You are a senior database migration analyst with Commerce, Finance, and Operations expertise. Analyze the migration in two phases.

Migration to analyze:

```
{migration}
```

---

## PHASE A — INTERROGATIVE REASONING

*Reasoning layer. Analytical questions by domain concern. Not the authoritative output — Phase B is.*

**GLOBAL CITATION RULE:** All step references in Phase A use "Step N from Q1." Do not describe steps by DDL text or table name when a step number from Q1 is available.

---

### Q1 — STEP REGISTRY (NAMED ARTIFACT)

| Step | Statement (abbreviated) | Type | Primary Table/Entity |
|------|-------------------------|------|----------------------|
| 1    | ...                     | ...  | ...                  |

*Q1 STEP REGISTRY: authoritative step-number source. Cite all Phase A steps as "Step N from Q1."*

---

### Q2 — Commerce Expert Lens (first)

*You are a Commerce migration expert. Domain: orders, carts, SKUs, product catalog, customer identity, deduplication, pricing.*

For each entity supporting customer-facing operations:

**Before / After state** for each changed column or constraint. Cite as "Step N from Q1."

**UNIQUE constraint changes:** Does any UNIQUE removal affect order deduplication or SKU uniqueness? Name the business object and the duplication scenario. Example: "Step 2 from Q1 removes UNIQUE on orders.idempotency_key — duplicate orders from payment retry loops become possible."

**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION** — cite blocking step as "Step N from Q1."

**Commerce consequence:** Concrete customer-facing consequence with scenario. Include order count range, retry event, or SKU collision threshold.

**NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**

---

### Q3 — Finance Expert Lens (second)

*You are a Finance migration expert. Domain: payment amounts, decimal precision, invoice records, ledger entries, refund processing, subscription billing.*

For each entity supporting financial records:

**Before / After state.** Cite as "Step N from Q1."

**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION** — Does any type narrowing silently truncate financial amounts? Cite as "Step N from Q1."
If TRUNCATION or SILENT DROP: name the Finance consequence with a dollar threshold. Example: "Step 3 from Q1 reduces amount precision — invoices over $9,999,999.99 silently capped."

**NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A**
If AT RISK: name the column, financial table, estimated row count, and the backfill instruction.

---

### Q4 — Operations Expert Lens (third)

*You are an Operations migration expert. Domain: shipments, fulfillment records, inventory counts, workflow state, order-in-flight.*

For each entity supporting operational workflows:

**Before / After state.** Cite as "Step N from Q1."

**Constraint change analysis:** For each FK, CHECK, or UNIQUE constraint change — does existing operational data satisfy the new constraint? Name which records violate it and what the migration does (fail, skip, backfill).

**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION** — Cite as "Step N from Q1."

**Operations consequence:** Concrete operational consequence. Name the workflow object and what happens to in-flight records.

---

### Q5 — Technical Analysis

**Performance cliffs:** For each step from Q1 touching a large table:
PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT — "Step N from Q1."
If PRESENT: table, operation type, estimated rows, risk type.

**Zero-downtime:** ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL
Blocking step (if NO/PARTIAL): "Step N from Q1" — maintenance window reason.

**Rollback:** For each destructive step from Q1:
ROLLBACK CLASS (BINARY FIELD — FIXED TAXONOMY): FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE — "Step N from Q1."

**Idempotency:** For each step from Q1:
IDEMPOTENT (BINARY FIELD): YES / NO — If NO: failure mode. "Step N from Q1."

---

### Q6 — Data Loss Summary

**DATA LOSS STATEMENT (BINARY FIELD — check exactly one):**
- [ ] NO DATA LOSS PATHS — [argument citing each relevant "Step N from Q1"]
- [ ] DATA LOSS PATHS EXIST — [list: "Step N from Q1 — what is lost, error surfaced?"]

---

## DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED

Review Q2 (Commerce), Q3 (Finance), Q4 (Operations). Set to BLOCKED if any DATA LOSS field is TRUNCATION, SILENT DROP, or REJECTION with no documented mitigation.

**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
Blocking step (if BLOCKED): Step N from Q1 — [reason]
Required mitigation: [what must be resolved]

*Phase B begins only when DOMAIN GATE (BINARY FIELD) = OPEN.*

---

## PHASE B — CANONICAL SYNTHESIS (AUTHORITATIVE ARTIFACT)

*Authoritative, execution-ordered output. Satisfies C-05. Do not reorder steps from Q1. All citations use "Step N from Q1."*

---

### B1 — Step-Ordered Trace Table

One row per step from Q1 STEP REGISTRY, in execution order. No blank cells.

| Step (Q1) | Statement | Before State | After State | DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) | ROLLBACK CLASS (FIXED TAXONOMY) | PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |
|-----------|-----------|--------------|-------------|--------------------------|------------------------------|----------------------------------|--------------------------|--------------------------|
| 1         | ...       | ...          | ...         | NONE/TRUNCATION/SILENT DROP/REJECTION | CLEAR/AT RISK/N/A | FULLY_REVERSIBLE/BACKUP_ONLY/IRREVERSIBLE | NONE/PRESENT | YES/NO |

---

### B2 — Domain Impact Table (POSITIONED BEFORE B3 VERIFY — complete before writing B3)

| Domain | Business object | Step (Q1) | Risk condition | Concrete consequence (numeric threshold required) |
|--------|----------------|-----------|----------------|---------------------------------------------------|
| Commerce | order / SKU / cart / product | Step N from Q1 | ... | [customer scenario — order count, retry, SKU collision] |
| Finance | invoice / ledger entry / refund | Step N from Q1 | ... | [$ threshold — e.g., "charges over $X silently truncated"] |
| Operations | shipment / inventory / workflow | Step N from Q1 | ... | [workflow state, record count, SLA consequence] |

At least one row must include a numeric threshold. Generic descriptions fail this section.

---

### B3 — Constraint Change Summary (requires DOMAIN GATE = OPEN)

| Step (Q1) | Constraint | Type | Change | Existing data violates? | Migration action |
|-----------|------------|------|--------|-------------------------|------------------|
| Step N from Q1 | ... | FK/UNIQUE/NOT NULL/CHECK | ADD/DROP/MODIFY | YES/NO/UNKNOWN | FAIL/SKIP/BACKFILL |

---

### B4 — Rollback Registry

| Step (Q1) | Rollback class | Recovery path | Data window at risk |
|-----------|----------------|---------------|---------------------|
| Step N from Q1 | BACKUP_ONLY / IRREVERSIBLE | ... | ... |

*(Omit FULLY_REVERSIBLE steps.)*

---

### B5 — Verify and Verdict

**Verification:**
- [ ] All Q1 steps appear in B1 in execution order
- [ ] Every binary field in B1 has a value — no blanks
- [ ] DATA LOSS STATEMENT in Q6 has exactly one box checked
- [ ] DOMAIN GATE (BINARY FIELD) is resolved — not blank
- [ ] B2 Domain Impact appears before this section

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
Blocking step (if NO/PARTIAL): Step N from Q1 — [reason]

**IDEMPOTENCY SUMMARY (BINARY FIELD): SAFE / UNSAFE / MIXED**
Non-idempotent steps: Step N from Q1 — [failure mode]

**Migration risk level:** SAFE TO RUN / RUN WITH PRECAUTIONS / REQUIRES REMEDIATION
Primary risk: [one sentence, citing "Step N from Q1"]
Required action before production: [one sentence]

---

---

## V-05: Combined — Lifecycle Emphasis + Phrasing Register (Explicit Gates + Conversational Framing, Two-Phase)

**Axis 1:** Lifecycle emphasis — explicit OPEN/BLOCKED gates at three boundaries, all pre-printed with "(BINARY FIELD)." C-17 fires at every gate field — the compound is pre-printed, not emergent.
**Axis 2:** Phrasing register — conversational framing replaces formal expert-role declarations. Imperative instructions become interrogative prompts. The model is asked "what does this look like for a $10,000 invoice?" rather than "name the Finance consequence with a dollar threshold."
**Combined hypothesis:** The lifecycle gate structure ensures structural completeness across all C-15/C-17 criteria. The conversational register lowers the model's tendency toward generic database descriptions and encourages concrete, scenario-based consequence naming (improving C-08 quality in live runs). Neither axis satisfies the other's target: structurally complete but generically-framed output is possible with gates alone; concretely-framed but structurally incomplete output is possible with conversational framing alone. The combination targets both failure modes simultaneously.
**C-17 coverage:** Three gate state fields pre-printed with "(BINARY FIELD)": DOMAIN GATE, VERIFY GATE (Phase A→B), and VERDICT GATE (Phase B).
**C-18 coverage:** Pre-printed global citation rule in Phase A global instruction AND in every question body that requires step citation.

---

You are a senior database migration analyst. Walk through this migration as if you are briefing the team before running it in production. Be specific — name dollar amounts, record counts, and concrete business scenarios. "Data may be affected" is not an acceptable finding anywhere in this analysis.

Migration to analyze:

```
{migration}
```

---

## PHASE A — LET'S MAP IT OUT

*Work through the migration concern by concern. Organize by what you need to understand — not by execution order. Phase B produces the execution-ordered authoritative output.*

**One rule throughout Phase A:** every step reference uses "Step N from Q1." Don't paraphrase DDL — cite the step number. This instruction applies to every question below.

---

### Q1 — What are we actually running?

Read the migration top to bottom. Give each statement a step number in execution order. This is your Q1 STEP REGISTRY — you'll reference these numbers throughout the analysis.

| Step | What it does (plain English) | Technical statement | Type | Table |
|------|------------------------------|---------------------|------|-------|
| 1    | ...                          | ...                 | ...  | ...   |

*Q1 STEP REGISTRY — cite all steps as "Step N from Q1" in every question below.*

---

### Q2 — What does the data look like before and after?

For each entity the migration touches: what does it look like before the migration? What does it look like after? Reference each change as "Step N from Q1."

For each changed column: type before, type after, nullability before, nullability after. Flag anything that could silently change what's stored:
**DATA LOSS (BINARY FIELD): NONE / TRUNCATION / SILENT DROP / REJECTION** — cite as "Step N from Q1."

---

### Q3 — What's the NOT NULL situation?

For any step from Q1 that adds a NOT NULL column to an existing table: is there a DEFAULT? If not, what happens to the rows already there?

**NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A** — cite as "Step N from Q1."
If AT RISK: name the column and table. How many rows are affected? What value should existing rows get?

---

### Q4 — Are there constraints that could break existing data?

Walk through each constraint change (added, dropped, or modified). Can the data already in the table satisfy the new rule? If not, what does the migration do — fail hard, silently skip, or backfill?

Reference each constraint change as "Step N from Q1."

---

### Q5 — Could any step silently lose data?

Think through each step from Q1 that could discard rows, truncate values, or drop columns. The key question: does the migration tell you when this happens, or does it happen silently?

**DATA LOSS STATEMENT (BINARY FIELD — pick exactly one):**
- [ ] NO DATA LOSS PATHS — here's why each relevant step from Q1 is safe: [argument]
- [ ] DATA LOSS PATHS EXIST — for each: "Step N from Q1 — what is discarded, does it surface an error?"

---

### Q6 — What does this mean for the business?

This is where database analysis becomes a real-world risk brief. Walk through three perspectives. For each one: name the business object, cite the relevant step as "Step N from Q1," and give a concrete scenario with a specific threshold.

**Finance perspective:** Think about amounts, invoices, ledger entries, refunds. If Step N from Q1 changes a financial column — what does that mean at a $10,000 threshold? A $1,000,000 threshold? What specifically gets silently truncated, zeroed, or lost?

**Operations perspective:** Think about shipments in transit, inventory counts, fulfillment status. If Step N from Q1 drops a column or changes a constraint on an operations table — what's the worst-case scenario for an in-flight shipment?

**Commerce perspective:** Think about orders, SKUs, cart state, product listings. If Step N from Q1 changes uniqueness rules or nullability — what does a customer see? Can two products get the same SKU? Can an order be charged twice?

For each domain where a risk exists: name a specific threshold. "Data could be affected" does not satisfy this question.

---

### Q7 — Can we roll back if something goes wrong?

For each destructive step from Q1 (dropping a column or table, narrowing a type, running a data transform):

**ROLLBACK CLASS (BINARY FIELD — pick exactly one): FULLY_REVERSIBLE / BACKUP_ONLY / IRREVERSIBLE** — cite as "Step N from Q1."
For BACKUP_ONLY or IRREVERSIBLE: what's the recovery window? What data falls in that window?

---

### Q8 — Can we run this without downtime?

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**

Walk through the migration looking for full-table rewrites, index rebuilds, or lock-heavy operations. Can these run via online DDL or an expand/contract pattern?

If NO or PARTIAL: name the blocker as "Step N from Q1." What specifically is the lock, and what does it mean at production table size?

---

### Q9 — Can we run this twice safely?

Walk through each step from Q1. If the migration is re-run after a partial failure or deploy retry:

**IDEMPOTENT (BINARY FIELD): YES / NO** per step — cite as "Step N from Q1."
If NO: what breaks on the second run? Duplicate key? Column already dropped? Be specific.

---

### Q10 — What's the performance picture?

For each step from Q1 that touches a large or high-traffic table:

**PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT** — "Step N from Q1."
If PRESENT: name the table, what the operation does (full-table rewrite, index rebuild on wide table, row scan for type cast), estimated row count, and the performance impact (lock duration, I/O spike, replication lag).

---

## DOMAIN GATE CHECK

Review Q5 (data loss), Q6 (domain impact), Q3 (NOT NULL risk). Is there any path where data is silently lost or transformed without documentation and mitigation?

**DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED**
Set to BLOCKED if any data loss path from Q5 or Q6 has no mitigation documented.
Blocking step (if BLOCKED): Step N from Q1 — [what is unresolved and why it blocks Phase B]

*Phase B begins only when DOMAIN GATE (BINARY FIELD) = OPEN. Do not write Phase B until this is resolved.*

---

## PHASE B — HERE'S WHAT WE'RE RUNNING (AUTHORITATIVE ARTIFACT)

*This is the authoritative output. Walk through the migration in execution order from Q1. Don't reorder or regroup steps. All citations use "Step N from Q1."*

---

### B1 — Step-by-Step Trace

One row per step from Q1, in order. Every cell gets a value — blank cells are structural omissions.

| Step (Q1) | What it does | Before State | After State | DATA LOSS (BINARY FIELD) | NOT NULL RISK (BINARY FIELD) | ROLLBACK CLASS (FIXED TAXONOMY) | PERF CLIFF (BINARY FIELD) | IDEMPOTENT (BINARY FIELD) |
|-----------|-------------|--------------|-------------|--------------------------|------------------------------|----------------------------------|--------------------------|--------------------------|
| 1         | ...         | ...          | ...         | NONE/TRUNCATION/SILENT DROP/REJECTION | CLEAR/AT RISK/N/A | FULLY_REVERSIBLE/BACKUP_ONLY/IRREVERSIBLE | NONE/PRESENT | YES/NO |

---

### B2 — Business Impact Summary (write this before B3 — context before checklist)

What does this migration mean for the business? One paragraph per domain. Be specific. Cite steps as "Step N from Q1."

**Commerce:** [Name the order/SKU/cart object. Give a scenario with a count or threshold. "Step N from Q1 removes the idempotency key constraint — any order with two payment attempts may produce two charged records."]

**Finance:** [Name the invoice/refund/ledger object. Give a threshold. "Step N from Q1 reduces amount precision — any charge over $X rounds down silently."]

**Operations:** [Name the shipment/inventory/fulfillment object. Give a state scenario. "Step N from Q1 drops the FK on shipment.order_id — in-flight shipments lose their order reference."]

---

### B3 — Did we cover everything?

**VERIFY GATE (BINARY FIELD): OPEN / BLOCKED**
Checklist:
- [ ] All Q1 steps appear in B1 in execution order
- [ ] Every DATA LOSS (BINARY FIELD) in B1 has a value — no blanks
- [ ] Every NOT NULL RISK (BINARY FIELD) in B1 has a value — no blanks
- [ ] ROLLBACK CLASS values use only the fixed taxonomy
- [ ] DATA LOSS STATEMENT in Q5 has exactly one box checked
- [ ] DOMAIN GATE (BINARY FIELD) is OPEN — not blank, not prose
- [ ] B2 Business Impact Summary appears before this section

VERIFY GATE (BINARY FIELD): OPEN / BLOCKED
Blocking item (if BLOCKED): [checklist item] — [reason it cannot be checked]

---

### B4 — Rollback Summary

For each step from Q1 where ROLLBACK CLASS != FULLY_REVERSIBLE:

| Step (Q1) | Class | Recovery path | Data window at risk |
|-----------|-------|---------------|---------------------|
| Step N from Q1 | BACKUP_ONLY / IRREVERSIBLE | ... | ... |

---

### B5 — Go / No-Go (requires VERIFY GATE = OPEN)

**ZERO-DOWNTIME VIABLE (BINARY FIELD): YES / NO / PARTIAL**
Blocker (if NO/PARTIAL): Step N from Q1 — [maintenance window requirement]

**IDEMPOTENCY SUMMARY (BINARY FIELD): SAFE / UNSAFE / MIXED**
Unsafe steps: Step N from Q1 — [what breaks on retry]

**VERDICT GATE (BINARY FIELD): OPEN / BLOCKED**
Set to OPEN if migration risk level is SAFE TO RUN or RUN WITH PRECAUTIONS with documented precautions.
Set to BLOCKED if REQUIRES REMEDIATION and remediation steps are not listed.
VERDICT GATE (BINARY FIELD): OPEN / BLOCKED

**Migration risk level:** SAFE TO RUN / RUN WITH PRECAUTIONS / REQUIRES REMEDIATION
The one thing the team needs to know: [one sentence — specific step as "Step N from Q1," specific risk, specific threshold]
What we must do before running in production: [one sentence]
