# trace-migration Variations — Round 17
**Date:** 2026-03-15
**Rubric:** v15
**Target criteria:** C-44 (ALIGNMENT STATE wired into Phase A-to-B EXIT BLOCK as named gate condition), C-45 (PROTOCOL COUNT MANIFEST extended to include all named content-category gates)

**Gate promotion chain context:** C-41 (row (a) category constraint) → C-43 (parse-return gate on violation) → C-42 (ALIGNMENT STATE record) → C-44 (ALIGNMENT STATE wired into boundary EXIT BLOCK). C-45 closes the manifest coverage gap: the PROTOCOL COUNT MANIFEST becomes authoritative for the complete gate architecture only when it enumerates content-category gates (COST LEDGER SUBSTRATE GATE, ALIGNMENT STATE gate) alongside boundary-transition gates.

**Isolation design:**

| V | Axes | C-44 | C-45 | Notes |
|---|------|------|------|-------|
| V-01 | Role Sequence | PASS | FAIL | Operations runs explicit alignment review step before EXIT BLOCK; manifest = boundary gates only |
| V-02 | Output Format | FAIL | PASS | Full gate-registry table at Phase B entry (C-45); ALIGNMENT STATE tracked in manifest but not wired into EXIT BLOCK (C-44 absent) |
| V-03 | Inertia Framing | FAIL | FAIL | Prominent inertia gate before parse; three-artifact alignment emerges from inertia frame but neither C-44 nor C-45 structurally present |
| V-04 | Role Sequence + Phrasing Register | PASS | PASS | DIRECTIVE/GATE syntax; Operations authority certifies EXIT BLOCK gate conditions; manifest extended to full registry |
| V-05 | Output Format + Lifecycle Emphasis + Inertia Framing | PASS | PASS | Ceiling architecture: inertia first, per-phase tables, full gate registry, bilateral alignment gate |

---

## V-01 — Role Sequence

**Axis:** Role sequence — Operations expert acts as named alignment authority at Phase A exit. Commerce/Finance complete Q2/Q3; Operations then runs a formal three-artifact alignment review before the EXIT BLOCK gate is declared.

**Hypothesis:** When C-44 is the natural climax of an Operations authority review step (not an automatic structural annotation), the ALIGNMENT STATE gate in the EXIT BLOCK is load-bearing: the role cannot exit Phase A without declaring a gate state on the alignment record. The alignment review step makes ALIGNMENT STATE = ALIGNED a signed commitment equivalent to PARSE GATE = OPEN — both are conditions declared by the Operations authority before Phase B. C-45 is intentionally absent to isolate the role-sequence axis.

---

You are running a migration trace signal for: {{topic}}

---

### P0 — PARSE PHASE

**Role:** Senior Operations / infrastructure migration expert. You own schema execution sequencing, constraint lifecycle management, and migration failure modes.

List all schema entities affected by {{topic}} **in execution order** — the order constraints must be disabled, altered, and re-enabled. NOT alphabetically. Alphabetical ordering is a DISQUALIFIER.

For each entity: table name · current column definitions · current constraint definitions (type, name, columns covered) · index definitions (type, uniqueness, columns covered).

**CONSTRAINT TYPE REGISTRY** — declare before any analysis:

| Constraint Type | Present? | Entities affected |
|-----------------|----------|------------------|
| NOT NULL | YES / NO | |
| Foreign Key (FK) | YES / NO | |
| UNIQUE | YES / NO | |
| CHECK | YES / NO | |

Binding manifest: every type declared YES must appear in a dedicated field in every domain-role section below.

**Citation anchor:** this section is "P0." Every Phase A finding must cite "(Step N from P0)."

---

**BOUNDARY PROTOCOL — Parse-to-A**

> EXIT BLOCK:
> PARSE GATE (BINARY FIELD) = OPEN
> Condition: entities in execution order; registry complete.
> If CLOSED: stop. Revise P0 until open.

> ENTRY REFERENCE:
> PARSE GATE (BINARY FIELD) = OPEN required for Phase A entry.

---

### PHASE A — PRE-MIGRATION ANALYSIS

**STATUS QUO COST**

COST LEDGER — establish before any entity analysis:

| Row | Item | Content |
|-----|------|---------|
| (a) | Current schema condition | (name the specific schema constraint, migration-state dependency, or infrastructure condition — NOT a revenue metric, Commerce disruption, or Finance outcome) |
| (b) | Dependent-process consequence | (name the process that depends on the schema condition and what breaks when migration is deferred) |
| (c) | Accumulation trajectory | (name what compounds if migration is deferred indefinitely) |

Row (a) category enforcement — **COST LEDGER SUBSTRATE GATE:**

IF row (a) names a revenue metric, Commerce disruption, or Finance outcome:
→ RETURN TO PARSE PHASE. Revise row (a) to name a schema condition, migration-state dependency, or infrastructure constraint. Do not begin Q1.

IF row (a) names a schema or infrastructure condition:
→ COST LEDGER SUBSTRATE GATE = OPEN. Proceed to alignment block.

---

**THREE-ARTIFACT SUBSTRATE ALIGNMENT**

Before Q1 begins, align three artifacts:

1. **COST LEDGER row (a)** — the schema condition named above
2. **Phase A Q1 analytical domain** — the infrastructure condition Q1 will analyze
3. **B2 chain substrate pre-commitment** — the shared condition B2's cross-role chain will cite

ALIGNMENT MANDATE: all three MUST name the same infrastructure condition or condition class.

**ALIGNMENT STATE (BINARY FIELD):** ALIGNED / MISALIGNED

Declare ALIGNMENT STATE before writing Q1. Three-artifact divergence = alignment failure; revise before continuing.

---

**ROLE ANALYSIS ENFORCEMENT**

Apply to Q1, Q2, Q3. DO NOT SCOPE OR SHORTEN. DO NOT limit to financial columns. DO NOT ROUTE ANY CONSTRAINT TYPE THROUGH A FREE-FORM FIELD. Every type declared YES in the CONSTRAINT TYPE REGISTRY must appear in a dedicated binary-state field in every role section.

---

**Q1 — OPERATIONS EXPERT (Infrastructure Lead)**

*(Step N from P0)*

Q1 establishes the shared infrastructure substrate Commerce and Finance depend on. B2's cross-role chain substrate derives from Q1.

**A — Before/After Schema State:** exact type names, constraint definitions, index specs for every affected column. ALL tables. Missing tables = DISQUALIFIER.

**B — Data Loss Paths:** every execution path where data is silently lost or truncated. Column · data lost · migration step.

**C — Constraint Violation Analysis:**

| Constraint Type | Risk (BINARY FIELD) | Violation Scenario | Migration Response |
|-----------------|--------------------|--------------------|-------------------|
| NOT NULL | YES / NO | | |
| Foreign Key (FK) | YES / NO | | |
| UNIQUE | YES / NO | | |
| CHECK | YES / NO | | |

DO NOT route any type through a free-form field.

**D — DEFAULT Value Check:** every column with DEFAULT. Whether existing rows receive default or retain NULL after migration.

**E — Zero-Downtime Viability:** yes/no · strategy name if yes · minimum window and cause if no.

**F — Performance Cliff:** every index rebuild, table scan, or lock acquisition. Table · operation · row-count threshold.

**G — Rollback Viability:** last rollback point · whether partial rollback leaves schema consistent · rollback steps in execution order.

**H — Idempotency:** yes/no · mechanism if yes · duplicate-execution failure mode if no.

---

**Q2 — COMMERCE EXPERT**

*(Step N from P0)*

Analyze {{topic}} across Commerce entities: catalog, SKU, pricing, promotions, order management schema.

Apply the complete A–H checklist from Q1 structure to Commerce domain entities. DO NOT SCOPE OR SHORTEN. All constraint types declared YES in the registry must appear in dedicated binary-state fields.

---

**Q3 — FINANCE EXPERT**

*(Step N from P0)*

Analyze {{topic}} across Finance entities: ledger, transactions, reporting views, audit trail, fiscal period columns.

Apply the complete A–H checklist from Q1 structure to Finance domain entities. DO NOT SCOPE OR SHORTEN. All constraint types declared YES in the registry must appear in dedicated binary-state fields.

---

**OPERATIONS ALIGNMENT REVIEW** — Phase A Exit Authority

Operations expert: review all three artifacts for substrate alignment before the Phase A-to-B gate is declared.

Audit record:
- COST LEDGER row (a) names: ______________________
- Q1 analytical domain names: ______________________
- B2 chain substrate pre-commitment names: ______________________

Are all three naming the same infrastructure condition or condition class?

**Declare ALIGNMENT STATE (BINARY FIELD) = ALIGNED or MISALIGNED.**

If MISALIGNED: name the specific artifact(s) requiring revision — COST LEDGER row (a), Q1 analysis domain, or B2 chain substrate pre-commitment — and the divergence. Do not proceed to EXIT BLOCK until ALIGNMENT STATE = ALIGNED.

---

**BOUNDARY PROTOCOL — Phase A-to-B**

> EXIT BLOCK:
> PARSE GATE (BINARY FIELD) = OPEN — Phase A sections complete; constraint types in dedicated fields.
> ALIGNMENT STATE (BINARY FIELD) = ALIGNED — COST LEDGER row (a), Q1 analytical domain, and B2 substrate pre-commitment name the same infrastructure condition class.
>
> Both conditions required for Phase B entry.
>
> If PARSE GATE = CLOSED: name the incomplete Phase A section. Do not begin Phase B.
> If ALIGNMENT STATE = MISALIGNED: name the divergent artifact(s) — COST LEDGER row (a), Q1 domain, or B2 substrate pre-commitment — requiring revision before Phase B may proceed.

> ENTRY REFERENCE:
> PARSE GATE (BINARY FIELD) = OPEN required.
> ALIGNMENT STATE (BINARY FIELD) = ALIGNED required.
> Phase B may not begin unless both conditions hold.

---

### PHASE B — MIGRATION EXECUTION

**PROTOCOL COUNT MANIFEST** — pre-commit gate states before any Phase B content:

| Boundary | Gate Name | Required State | Current State |
|----------|-----------|---------------|--------------|
| Parse-to-A | PARSE GATE (BINARY FIELD) | OPEN | |
| Phase A-to-B | PARSE GATE (BINARY FIELD) | OPEN | |
| Phase A-to-B | ALIGNMENT STATE (BINARY FIELD) | ALIGNED | |

All rows must show required state before Phase B content begins.

---

**B1 — Migration Execution Steps**

List every migration step in execution order. Per step: step number · DDL/DML operation · constraint type affected · transaction boundary · failure mode if skipped or reordered.

---

**B2 — Cross-Role Impact Chain**

Name a shared infrastructure condition from Q1's analysis whose disruption during migration produces named consequences in at least two distinct domain roles.

**Substrate condition:** (must match COST LEDGER row (a) and Q1 analytical domain)
**Commerce consequence:** (specific Commerce entity, process, or data state that fails)
**Finance consequence:** (specific Finance entity, ledger state, or reporting output that fails)

Substrate must match Q1 analytical domain. Divergence = substrate alignment failure.

---

**B3 — Canonical Execution Table**

| Step | Entity | Constraint Type | Risk (BINARY FIELD) | Migration Action | Rollback Action |
|------|--------|----------------|--------------------|--------------------|----------------|
| | | NOT NULL | YES / NO | | |
| | | FK | YES / NO | | |
| | | UNIQUE | YES / NO | | |
| | | CHECK | YES / NO | | |

All four constraint type columns required. At least one row per type declared YES in the registry.

---

**BOUNDARY PROTOCOL — Phase B-to-Close**

> EXIT BLOCK:
> PHASE B COMPLETION GATE (BINARY FIELD) = COMPLETE
> Condition: B1 steps listed; B2 cross-role chain named with matching substrate; B3 complete with all four constraint type columns.

> ENTRY REFERENCE:
> PHASE B COMPLETION GATE (BINARY FIELD) = COMPLETE required.

---

## V-02 — Output Format

**Axis:** Output format — fully table-anchored throughout. The PROTOCOL COUNT MANIFEST is a full gate-registry table at Phase B entry that includes COST LEDGER SUBSTRATE GATE and ALIGNMENT STATE gate as named rows alongside boundary-transition gates (C-45). ALIGNMENT STATE is recorded in the alignment block and appears as a manifest row, but is NOT listed as a condition in the Phase A-to-B EXIT BLOCK (C-44 absent — alignment tracked, not gated at boundary).

**Hypothesis:** A table-first format where every structural element is a named table tests whether C-45 passes when the manifest is a machine-countable gate registry, while C-44's absence exposes the gap: a manifest row for ALIGNMENT STATE is insufficient if that row's state cannot block Phase B entry via the EXIT BLOCK. The format variation should isolate C-45 cleanly — manifest completeness achieved without gate enforcement at the boundary.

---

You are running a migration trace signal for: {{topic}}

---

### P0 — PARSE PHASE

**Role:** Senior Operations / infrastructure migration expert.

Produce the schema entity table for {{topic}}. Entries in execution order — NOT alphabetically. Alphabetical ordering = DISQUALIFIER.

**ENTITY TABLE:**

| # | Entity | Columns (name · type · nullable) | Constraints (type · name · columns) | Indexes (type · uniqueness · columns) |
|---|--------|----------------------------------|--------------------------------------|---------------------------------------|

**CONSTRAINT TYPE REGISTRY:**

| Type | Present? | Entities |
|------|----------|---------|
| NOT NULL | YES / NO | |
| FK | YES / NO | |
| UNIQUE | YES / NO | |
| CHECK | YES / NO | |

Binding manifest: all YES types must appear as dedicated binary-state fields in every role section.

**Citation anchor:** section = "P0." All Phase A findings cite "(Step N from P0)."

---

**BOUNDARY PROTOCOL TABLE — Parse-to-A:**

| Gate | Type | Required | Current |
|------|------|----------|---------|
| PARSE GATE | BINARY FIELD | OPEN | |

If PARSE GATE current ≠ OPEN: stop. Revise P0.

---

### PHASE A — PRE-MIGRATION ANALYSIS

**COST LEDGER:**

| Row | Category | Content |
|-----|----------|---------|
| (a) | Current schema condition | (schema constraint, migration-state dependency, or infrastructure condition — NOT revenue metric, Commerce disruption, Finance outcome) |
| (b) | Dependent-process consequence | |
| (c) | Accumulation trajectory | |

**COST LEDGER SUBSTRATE GATE TABLE:**

| Check | Row (a) Category | Gate State |
|-------|-----------------|-----------|
| Is row (a) a schema condition, migration-state dependency, or infrastructure constraint? | YES / NO | OPEN (YES) / CLOSED (NO) |

If gate state = CLOSED: RETURN TO PARSE PHASE. Revise row (a). Do not begin Q1.

---

**THREE-ARTIFACT ALIGNMENT TABLE:**

| Artifact | Names | Same condition class? |
|----------|-------|-----------------------|
| COST LEDGER row (a) | | |
| Phase A Q1 analytical domain | | |
| B2 chain substrate pre-commitment | | |
| **ALIGNMENT STATE (BINARY FIELD)** | **ALIGNED / MISALIGNED** | |

Declare ALIGNMENT STATE before writing Q1. All three artifacts must name the same infrastructure condition class.

---

**ROLE ANALYSIS ENFORCEMENT:**

| Rule | Applies to |
|------|-----------|
| DO NOT SCOPE OR SHORTEN | Q1, Q2, Q3 |
| DO NOT limit to financial columns | Q1, Q2, Q3 |
| DO NOT ROUTE ANY CONSTRAINT TYPE THROUGH A FREE-FORM FIELD | Q1, Q2, Q3 |
| Every YES type in registry must appear in dedicated binary-state field | Q1, Q2, Q3 |

---

**Q1 — OPERATIONS EXPERT**

*(Step N from P0)* — Q1 establishes shared infrastructure substrate.

**A — Before/After State Table:**

| Column | Before type | After type | Constraint before | Constraint after |
|--------|------------|-----------|-------------------|-----------------|

ALL affected tables. Missing tables = DISQUALIFIER.

**B — Data Loss Table:**

| Column | Data lost/truncated | Migration step | Cause |
|--------|--------------------|--------------:|-------|

**C — Constraint Risk Table:**

| Type | Risk (BINARY FIELD) | Violation Scenario | Migration Response |
|------|--------------------|--------------------|-------------------|
| NOT NULL | YES / NO | | |
| FK | YES / NO | | |
| UNIQUE | YES / NO | | |
| CHECK | YES / NO | | |

No free-form routing.

**D — DEFAULT Table:**

| Column | Default value | Existing rows receive default? | Post-migration state |
|--------|--------------|-------------------------------|---------------------|

**E — Zero-Downtime Table:**

| Viable? | Strategy (if yes) | Downtime window (if no) | Cause |
|---------|-------------------|------------------------|-------|

**F — Performance Cliff Table:**

| Table | Operation | Row-count threshold | Expected duration |
|-------|-----------|--------------------:|------------------|

**G — Rollback Table:**

| Last rollback point | Partial rollback consistent? | Steps (ordered) |
|--------------------|-----------------------------:|----------------|

**H — Idempotency Table:**

| Idempotent? | Mechanism (if yes) | Duplicate-execution failure (if no) |
|------------|-------------------|--------------------------------------|

---

**Q2 — COMMERCE EXPERT**

*(Step N from P0)*

Analyze {{topic}} across Commerce entities (catalog, SKU, pricing, promotions, order management). Apply full A–H table structure from Q1 to Commerce entities. All YES constraint types in dedicated binary-state fields.

---

**Q3 — FINANCE EXPERT**

*(Step N from P0)*

Analyze {{topic}} across Finance entities (ledger, transactions, reporting views, audit trail, fiscal period). Apply full A–H table structure from Q1 to Finance entities. All YES constraint types in dedicated binary-state fields.

---

**BOUNDARY PROTOCOL TABLE — Phase A-to-B:**

| Gate | Type | Required | Current |
|------|------|----------|---------|
| PARSE GATE | BINARY FIELD | OPEN | |
| ALIGNMENT STATE | BINARY FIELD | (tracked) | ALIGNED / MISALIGNED |

Note: ALIGNMENT STATE is tracked at this boundary for manifest completeness. Phase B entry requires PARSE GATE = OPEN.

If PARSE GATE current ≠ OPEN: stop. Name the incomplete Phase A section. Do not begin Phase B.

---

### PHASE B — MIGRATION EXECUTION

**PROTOCOL COUNT MANIFEST** — complete gate registry before any Phase B content:

| Gate Name | Gate Type | Boundary / Source | Required State | Current State |
|-----------|-----------|-------------------|---------------|--------------|
| PARSE GATE | BINARY FIELD | Parse-to-A BOUNDARY PROTOCOL | OPEN | |
| PARSE GATE | BINARY FIELD | Phase A-to-B BOUNDARY PROTOCOL | OPEN | |
| COST LEDGER SUBSTRATE GATE | BINARY FIELD | Phase A COST LEDGER (C-43) | OPEN | |
| ALIGNMENT STATE | BINARY FIELD | Phase A THREE-ARTIFACT ALIGNMENT | ALIGNED | |

Single verification surface: all named gates in one manifest. A manifest row absent for any named gate = incomplete registry.

---

**B1 — Migration Execution Steps Table:**

| Step | Operation (DDL/DML) | Constraint type affected | Transaction boundary | Failure mode |
|------|--------------------|--------------------------|--------------------|-------------|

---

**B2 — Cross-Role Impact Chain**

**Substrate condition:** (must match COST LEDGER row (a) and Q1 analytical domain)
**Commerce consequence:** (specific Commerce entity/process/data state that fails on substrate disruption)
**Finance consequence:** (specific Finance entity/ledger/reporting output that fails on substrate disruption)

---

**B3 — Canonical Execution Table:**

| Step | Entity | NOT NULL Risk (BINARY FIELD) | FK Risk (BINARY FIELD) | UNIQUE Risk (BINARY FIELD) | CHECK Risk (BINARY FIELD) | Migration Action | Rollback Action |
|------|--------|-----------------------------|----------------------|--------------------------|--------------------------|-----------------|----------------|

All four constraint type columns required.

---

**BOUNDARY PROTOCOL TABLE — Phase B-to-Close:**

| Gate | Type | Required | Current |
|------|------|----------|---------|
| PHASE B COMPLETION GATE | BINARY FIELD | COMPLETE | |

---

## V-03 — Inertia Framing

**Axis:** Inertia framing — the migration value case is established as a structural entry gate before parse. The COST LEDGER appears before P0 as the "migration cost justification gate"; only when the inertia cost is quantified does parse begin. The three-artifact alignment emerges organically from the inertia substrate condition anchoring Q1 and B2. C-44 and C-45 are intentionally absent to isolate the inertia axis.

**Hypothesis:** Foregrounding the inertia cost as a pre-parse gate tests whether the substrate alignment mechanism emerges from structural pressure (the inertia condition anchors all downstream analysis) without explicit gate wiring at Phase A-to-B. When the COST LEDGER row (a) is the foundation on which the entire analysis rests, the alignment of Q1 and B2 to that substrate may be implicit — but will be structurally unverifiable without C-44 and C-45. The absence of both mechanisms exposes the gap between alignment-as-foundation and alignment-as-enforced-gate.

---

You are running a migration trace signal for: {{topic}}

---

### MIGRATION VALUE CASE — Pre-Analysis Gate

Before any schema entity is listed, establish why {{topic}} must happen. The cost of inaction is the frame for every subsequent analysis step.

**COST LEDGER:**

| Row | Item | Content |
|-----|------|---------|
| (a) | Current schema condition | (name the specific schema constraint, migration-state dependency, or infrastructure condition being addressed — this is the substrate every downstream role will analyze) |
| (b) | What breaks if this migration does not happen | (name the operational or business process that fails or degrades when migration is deferred) |
| (c) | What compounds if this migration is deferred indefinitely | (name the technical debt trajectory, data integrity risk, or failure accumulation mode) |

Row (a) is the anchor condition. Every domain role in Phase A must analyze the same substrate condition named in row (a). B2's cross-role chain cites row (a) as its shared failure substrate.

Row (a) MUST name a schema condition, migration-state dependency, or infrastructure constraint. Row (a) MUST NOT name a revenue metric, Commerce process disruption, or Finance outcome.

If row (a) names a revenue metric, Commerce disruption, or Finance outcome: revise before listing any schema entities. The migration value case must be grounded in the schema condition being changed.

---

### P0 — PARSE PHASE

**Role:** Senior Operations / infrastructure migration expert.

List all schema entities affected by {{topic}} in execution order. NOT alphabetically. Alphabetical ordering = DISQUALIFIER.

For each entity: table name · column definitions · constraint definitions (type, name, columns) · index definitions (type, uniqueness, columns).

**CONSTRAINT TYPE REGISTRY:**

| Constraint Type | Present? | Entities |
|-----------------|----------|---------|
| NOT NULL | YES / NO | |
| FK | YES / NO | |
| UNIQUE | YES / NO | |
| CHECK | YES / NO | |

All types declared YES must appear in dedicated binary-state fields in every domain-role section.

**Citation anchor:** section = "P0." All Phase A findings cite "(Step N from P0)."

---

**BOUNDARY PROTOCOL — Parse-to-A**

> EXIT BLOCK:
> PARSE GATE (BINARY FIELD) = OPEN
> Condition: entities in execution order; registry complete.
> CLOSED: stop. Revise P0.

> ENTRY REFERENCE:
> PARSE GATE (BINARY FIELD) = OPEN required.

---

### PHASE A — PRE-MIGRATION ANALYSIS

The COST LEDGER row (a) substrate condition established before parse is the analytical anchor for Phase A. Every domain role section analyzes how {{topic}} affects the systems that depend on that substrate condition.

**ROLE ANALYSIS ENFORCEMENT**

Apply to Q1, Q2, Q3. DO NOT SCOPE OR SHORTEN. DO NOT limit to financial columns. DO NOT ROUTE ANY CONSTRAINT TYPE THROUGH A FREE-FORM FIELD. Every YES type in the registry in a dedicated binary-state field.

---

**Q1 — OPERATIONS EXPERT (Infrastructure Lead)**

*(Step N from P0)* — analyze the infrastructure substrate named in COST LEDGER row (a).

Q1 establishes how {{topic}} affects the infrastructure condition that both Commerce and Finance depend on. The shared substrate B2's cross-role chain will cite is the condition Q1 analyzes here.

**A — Before/After Schema State:** exact type names, constraint definitions, index specs for all affected columns. ALL tables. Missing tables = DISQUALIFIER.

**B — Data Loss Paths:** every path where data is silently lost or truncated. Column · data lost · migration step.

**C — Constraint Violation Analysis** (dedicated fields — no free-form routing):

| Type | Risk (BINARY FIELD) | Violation Scenario | Migration Response |
|------|--------------------|--------------------|-------------------|
| NOT NULL | YES / NO | | |
| FK | YES / NO | | |
| UNIQUE | YES / NO | | |
| CHECK | YES / NO | | |

**D — DEFAULT Value Check:** every DEFAULT column. Whether existing rows receive default or retain NULL.

**E — Zero-Downtime Viability:** yes/no · strategy if yes · minimum window and cause if no.

**F — Performance Cliff:** every index rebuild, scan, or lock acquisition. Table · operation · threshold.

**G — Rollback Viability:** last rollback point · partial consistency · steps in order.

**H — Idempotency:** yes/no · mechanism if yes · duplicate failure if no.

---

**Q2 — COMMERCE EXPERT**

*(Step N from P0)* — analyze how the infrastructure substrate change in {{topic}} cascades into Commerce domain entities: catalog, SKU, pricing, promotions, order management.

The Commerce analysis builds on Q1's substrate findings. Commerce systems that depend on the COST LEDGER row (a) condition must be analyzed here.

Apply the complete A–H checklist to Commerce entities. All YES constraint types in dedicated binary-state fields. DO NOT SCOPE OR SHORTEN.

---

**Q3 — FINANCE EXPERT**

*(Step N from P0)* — analyze how the infrastructure substrate change in {{topic}} cascades into Finance domain entities: ledger, transactions, reporting views, audit trail, fiscal period columns.

The Finance analysis builds on Q1's substrate findings. Finance systems that depend on the COST LEDGER row (a) condition must be analyzed here.

Apply the complete A–H checklist to Finance entities. All YES constraint types in dedicated binary-state fields. DO NOT SCOPE OR SHORTEN.

---

**BOUNDARY PROTOCOL — Phase A-to-B**

> EXIT BLOCK:
> PARSE GATE (BINARY FIELD) = OPEN — Phase A sections complete; all constraint types in dedicated fields.
> If CLOSED: name the incomplete section. Do not begin Phase B.

> ENTRY REFERENCE:
> PARSE GATE (BINARY FIELD) = OPEN required.

---

### PHASE B — MIGRATION EXECUTION

**PROTOCOL COUNT MANIFEST:**

| Boundary | Gate | Required | Current |
|----------|------|----------|---------|
| Parse-to-A | PARSE GATE (BINARY FIELD) | OPEN | |
| Phase A-to-B | PARSE GATE (BINARY FIELD) | OPEN | |

All gates open before Phase B content begins.

---

**B1 — Migration Execution Steps**

List every migration step in execution order. Per step: step number · DDL/DML operation · constraint type affected · transaction boundary · failure mode if skipped or reordered.

---

**B2 — Cross-Role Impact Chain**

The shared infrastructure substrate from COST LEDGER row (a) is the failure node. Name how its disruption during migration cascades across domain roles.

**Substrate condition:** (must match COST LEDGER row (a) and the condition Q1 analyzed)
**Commerce consequence:** (specific Commerce entity, process, or data state that fails)
**Finance consequence:** (specific Finance entity, ledger state, or reporting output that fails)

The substrate must match the inertia anchor established before parse. A B2 chain where the substrate diverges from COST LEDGER row (a) has broken the migration value case.

---

**B3 — Canonical Execution Table**

| Step | Entity | Constraint Type | Risk (BINARY FIELD) | Migration Action | Rollback Action |
|------|--------|----------------|--------------------|--------------------|----------------|
| | | NOT NULL | YES / NO | | |
| | | FK | YES / NO | | |
| | | UNIQUE | YES / NO | | |
| | | CHECK | YES / NO | | |

All four constraint type columns required. At least one row per YES type in registry.

---

**BOUNDARY PROTOCOL — Phase B-to-Close**

> EXIT BLOCK:
> PHASE B COMPLETION GATE (BINARY FIELD) = COMPLETE
> Condition: B1 complete; B2 substrate matches COST LEDGER row (a); B3 all four columns.

> ENTRY REFERENCE:
> PHASE B COMPLETION GATE (BINARY FIELD) = COMPLETE required.

---

## V-04 — Role Sequence + Phrasing Register

**Axis:** Role sequence + phrasing register (formal DIRECTIVE/GATE syntax)

**Hypothesis:** Formal imperative register combined with named GATE DIRECTIVEs tests whether C-44 and C-45 hold under maximum structural explicitness. Every gate is a GATE DIRECTIVE with REQUIRED FIELDS. The Phase A-to-B EXIT BLOCK is a GATE EVALUATION DIRECTIVE naming ALIGNMENT STATE = ALIGNED and PARSE GATE = OPEN as co-equal binary conditions. The PROTOCOL COUNT MANIFEST is a MANIFEST DIRECTIVE at Phase B entry listing all named gates — boundary-transition and content-category — with gate types and states (C-45). The combination tests whether DIRECTIVE language eliminates the ambiguity that prose blocks can leave around gate enforcement.

---

You are executing a migration trace signal. Topic: {{topic}}

---

### PARSE DIRECTIVE P0

**Adopt role:** Operations / infrastructure migration authority. Scope: schema constraint lifecycle, execution sequencing, migration failure modes. You do not hedge. You name every entity and constraint.

**Execute in order. Do not summarize. Do not write prose introductions.**

---

**DIRECTIVE P0-1 — SCHEMA ENTITY ENUMERATION**

List all schema entities affected by {{topic}} in EXECUTION ORDER — the order constraints must be disabled, altered, re-enabled. Required fields per entity:
- ENTITY: table name
- COLUMNS: name · type · nullable · default
- CONSTRAINTS: type · constraint name · columns covered
- INDEXES: type · uniqueness · columns covered

EXECUTION ORDER MANDATE: alphabetical ordering is a DISQUALIFIER.

---

**DIRECTIVE P0-2 — CONSTRAINT TYPE REGISTRY**

Declare before any analysis. Required fields:

| Type | Present (YES/NO) | Entities |
|------|-----------------|---------|
| NOT NULL | | |
| FK | | |
| UNIQUE | | |
| CHECK | | |

BINDING MANDATE: every type declared YES must appear in a DEDICATED BINARY-STATE FIELD in every role section. Routing any type through a free-form field is a DISQUALIFIER.

CITATION MANDATE: every Phase A finding must carry "(Step N from P0)."

---

**GATE DIRECTIVE — Parse-to-A Boundary**

```
EXIT BLOCK (P0 exit):
  PARSE GATE (BINARY FIELD) = OPEN
  Condition met: entities in execution order; CONSTRAINT TYPE REGISTRY complete.
  If CLOSED: STOP. Revise P0-1 and P0-2. Do not execute Phase A directives.

ENTRY REFERENCE (Phase A entry):
  PARSE GATE (BINARY FIELD) = OPEN required.
  Entry blocked when PARSE GATE ≠ OPEN.
```

---

### PHASE A DIRECTIVES

---

**DIRECTIVE A-1 — COST LEDGER**

Produce the COST LEDGER before any entity analysis. Required fields:

| Row | Category | Content |
|-----|----------|---------|
| (a) | Schema condition | (schema constraint, migration-state dependency, or infrastructure condition — NOT revenue metric, Commerce disruption, Finance outcome) |
| (b) | Dependent-process consequence | |
| (c) | Accumulation trajectory | |

---

**GATE DIRECTIVE — COST LEDGER SUBSTRATE GATE**

```
Evaluate row (a) category:

IF row (a) names revenue metric, Commerce disruption, or Finance outcome:
  COST LEDGER SUBSTRATE GATE (BINARY FIELD) = CLOSED
  RETURN TO PARSE. Revise row (a) to name a schema condition,
  migration-state dependency, or infrastructure constraint.
  Do not execute DIRECTIVE A-2 or any Q directives until gate reopens.

IF row (a) names schema condition, migration-state dependency, or infrastructure constraint:
  COST LEDGER SUBSTRATE GATE (BINARY FIELD) = OPEN
  Proceed to DIRECTIVE A-2.
```

---

**DIRECTIVE A-2 — THREE-ARTIFACT ALIGNMENT MANDATE**

Execute before Q1. Required fields:

| Artifact | Named condition |
|----------|----------------|
| COST LEDGER row (a) | |
| Phase A Q1 analytical domain | |
| B2 chain substrate pre-commitment | |

ALIGNMENT MANDATE: all three must name the same infrastructure condition or condition class.

**DECLARE: ALIGNMENT STATE (BINARY FIELD) = ALIGNED or MISALIGNED**

If MISALIGNED: identify the divergent artifact(s). Do not execute Q1 until ALIGNMENT STATE = ALIGNED.

---

**DIRECTIVE A-3 — ROLE ANALYSIS ENFORCEMENT**

MANDATORY RULES — apply to all Q directives:

- DO NOT SCOPE OR SHORTEN any Q directive
- DO NOT limit analysis to financial columns or high-volume tables
- DO NOT ROUTE ANY CONSTRAINT TYPE THROUGH A FREE-FORM FIELD
- Every type declared YES in DIRECTIVE P0-2 must appear in a dedicated binary-state field
- Every finding must carry "(Step N from P0)"

---

**DIRECTIVE Q1 — OPERATIONS ROLE**

*(Step N from P0)*

Q1 establishes shared infrastructure substrate. Operations-first ordering mandated.

REQUIRED FIELDS:

- **BEFORE/AFTER STATE:** exact type names, constraint definitions, index specs for all affected columns in ALL tables. Missing table = DISQUALIFIER.
- **DATA LOSS PATHS:** every column where data is silently lost or truncated. Column · data lost · step.
- **CONSTRAINT RISK TABLE:**

  | Type | Risk (BINARY FIELD) | Violation scenario | Migration response |
  |------|--------------------|--------------------|-------------------|
  | NOT NULL | YES / NO | | |
  | FK | YES / NO | | |
  | UNIQUE | YES / NO | | |
  | CHECK | YES / NO | | |

- **DEFAULT AUDIT:** every DEFAULT column. Existing row behavior after migration.
- **ZERO-DOWNTIME:** YES/NO · strategy if yes · window and cause if no.
- **PERFORMANCE CLIFF:** every index rebuild, scan, lock. Table · operation · threshold.
- **ROLLBACK:** last point · partial consistency · ordered steps.
- **IDEMPOTENCY:** YES/NO · mechanism or failure mode.

---

**DIRECTIVE Q2 — COMMERCE ROLE**

*(Step N from P0)*

Commerce entities: catalog, SKU, pricing, promotions, order management.

Execute all REQUIRED FIELDS from Q1 structure for Commerce entities. DIRECTIVE A-3 rules apply without exception. All YES constraint types in dedicated binary-state fields.

---

**DIRECTIVE Q3 — FINANCE ROLE**

*(Step N from P0)*

Finance entities: ledger, transactions, reporting views, audit trail, fiscal period.

Execute all REQUIRED FIELDS from Q1 structure for Finance entities. DIRECTIVE A-3 rules apply without exception. All YES constraint types in dedicated binary-state fields.

---

**GATE DIRECTIVE — Phase A-to-B Boundary**

```
EXIT BLOCK (Phase A exit):
  PARSE GATE (BINARY FIELD) = OPEN
    Condition: all Q directives complete; all constraint types in dedicated fields.
  ALIGNMENT STATE (BINARY FIELD) = ALIGNED
    Condition: COST LEDGER row (a), Q1 analytical domain, and B2 substrate
    pre-commitment name the same infrastructure condition class.

  Both conditions required for Phase B entry.

  If PARSE GATE = CLOSED:
    Name the incomplete Q directive. Do not execute Phase B directives.
  If ALIGNMENT STATE = MISALIGNED:
    Name the divergent artifact(s): COST LEDGER row (a), Q1 domain,
    or B2 substrate pre-commitment. Name the revision required.
    Do not execute Phase B directives.

ENTRY REFERENCE (Phase B entry):
  PARSE GATE (BINARY FIELD) = OPEN required.
  ALIGNMENT STATE (BINARY FIELD) = ALIGNED required.
  Phase B directives blocked unless both conditions hold.
```

---

### PHASE B DIRECTIVES

---

**DIRECTIVE B-0 — PROTOCOL COUNT MANIFEST**

Execute before any Phase B content directive. Required: one row per named gate in this prompt.

| Gate Name | Gate Type | Source | Required State | Current State |
|-----------|-----------|--------|---------------|--------------|
| PARSE GATE | BINARY FIELD | Parse-to-A BOUNDARY | OPEN | |
| PARSE GATE | BINARY FIELD | Phase A-to-B BOUNDARY | OPEN | |
| COST LEDGER SUBSTRATE GATE | BINARY FIELD | DIRECTIVE A-1/GATE | OPEN | |
| ALIGNMENT STATE | BINARY FIELD | DIRECTIVE A-2 | ALIGNED | |

Single verification surface. A named gate absent from this manifest = incomplete registry. A manifest row with no corresponding named gate block = cross-document structural failure.

All rows in required state before executing DIRECTIVE B-1.

---

**DIRECTIVE B-1 — MIGRATION EXECUTION STEPS**

Required fields per step:
- STEP: number and action name
- OPERATION: DDL or DML statement type
- CONSTRAINT TYPE AFFECTED: from registry
- TRANSACTION BOUNDARY: begin/commit scope
- SKIP CONSEQUENCE: failure mode if step is skipped or reordered

---

**DIRECTIVE B-2 — CROSS-ROLE IMPACT CHAIN**

Required fields:
- SUBSTRATE CONDITION: must match COST LEDGER row (a) and Q1 analytical domain
- COMMERCE CONSEQUENCE: specific Commerce entity or process that fails on substrate disruption
- FINANCE CONSEQUENCE: specific Finance entity or ledger state that fails on substrate disruption

Substrate divergence from Q1 domain = alignment failure.

---

**DIRECTIVE B-3 — CANONICAL EXECUTION TABLE**

| Step | Entity | NOT NULL Risk (BINARY FIELD) | FK Risk (BINARY FIELD) | UNIQUE Risk (BINARY FIELD) | CHECK Risk (BINARY FIELD) | Migration Action | Rollback Action |
|------|--------|-----------------------------|----------------------|--------------------------|--------------------------|-----------------|----------------|

All four constraint type columns required. At least one row per YES type in DIRECTIVE P0-2 registry.

---

**GATE DIRECTIVE — Phase B-to-Close**

```
EXIT BLOCK:
  PHASE B COMPLETION GATE (BINARY FIELD) = COMPLETE
  Conditions: B-1 steps complete; B-2 substrate matches COST LEDGER row (a);
  B-3 all four constraint type columns present and filled.

ENTRY REFERENCE:
  PHASE B COMPLETION GATE (BINARY FIELD) = COMPLETE required.
```

---

## V-05 — Combined: Output Format + Lifecycle Emphasis + Inertia Framing

**Axis:** Combined — output format + lifecycle emphasis + inertia framing

**Hypothesis:** Maximum-coverage architecture. Inertia framing first: the COST LEDGER is a pre-parse structural commitment that makes row (a) substrate condition load-bearing before any schema entity is listed. Output format: every structural element is a named table, making all coverage verifiable by row count. Lifecycle emphasis: per-section GATE TABLES make every boundary machine-countable. C-44 is wired via a Phase A-to-B GATE TABLE that names ALIGNMENT STATE = ALIGNED as a co-equal condition with PARSE GATE = OPEN. C-45 is wired via the PROTOCOL COUNT MANIFEST as a full gate-registry table at Phase B entry with explicit rows for COST LEDGER SUBSTRATE GATE and ALIGNMENT STATE gate. This is the ceiling architecture for R17.

---

You are running a migration trace signal for: {{topic}}

---

### PRE-PARSE — MIGRATION COST COMMITMENT

Before any schema entity is listed, establish the inertia cost. This commitment gates the entire analysis: the substrate condition named in COST LEDGER row (a) is the anchor every role analyzes and the substrate B2's chain cites.

**COST LEDGER:**

| Row | Category | Content |
|-----|----------|---------|
| (a) | Current schema condition | (the specific schema constraint, migration-state dependency, or infrastructure condition this migration addresses — NOT a revenue metric, Commerce disruption, or Finance outcome) |
| (b) | Dependent-process consequence | (the process that depends on row (a) condition and degrades when migration is deferred) |
| (c) | Accumulation trajectory | (what compounds indefinitely if migration is not executed) |

**COST LEDGER SUBSTRATE GATE:**

| Check | Answer | Gate State |
|-------|--------|-----------|
| Does row (a) name a schema condition, migration-state dependency, or infrastructure constraint? | YES / NO | OPEN (YES) / CLOSED (NO) |

If CLOSED: revise row (a). Do not proceed to P0. The entire analysis depends on row (a) naming the right category.

---

### P0 — PARSE PHASE

**Role:** Senior Operations / infrastructure migration expert.

**ENTITY TABLE** — execution order, not alphabetical. Alphabetical = DISQUALIFIER.

| # | Entity | Columns (name · type · nullable · default) | Constraints (type · name · columns) | Indexes (type · unique · columns) |
|---|--------|--------------------------------------------|--------------------------------------|----------------------------------|

**CONSTRAINT TYPE REGISTRY:**

| Type | Present? | Entities |
|------|----------|---------|
| NOT NULL | YES / NO | |
| FK | YES / NO | |
| UNIQUE | YES / NO | |
| CHECK | YES / NO | |

Binding manifest. All YES types in dedicated binary-state fields in every role section.

Citation anchor: this section = "P0." All Phase A findings cite "(Step N from P0)."

**PARSE-TO-A GATE TABLE:**

| Gate | Type | Required | Current |
|------|------|----------|---------|
| PARSE GATE | BINARY FIELD | OPEN | |

If Current ≠ OPEN: stop. Revise P0.

---

### PHASE A — PRE-MIGRATION ANALYSIS

**THREE-ARTIFACT ALIGNMENT TABLE** — declare before Q1:

| Artifact | Named condition | Same class? |
|----------|----------------|------------|
| COST LEDGER row (a) | (from pre-parse) | — |
| Phase A Q1 analytical domain | | YES / NO |
| B2 chain substrate pre-commitment | | YES / NO |
| **ALIGNMENT STATE (BINARY FIELD)** | **ALIGNED / MISALIGNED** | |

All three must name the same infrastructure condition class. ALIGNMENT STATE = MISALIGNED blocks Q1. Name the divergent artifact(s) and revise before continuing.

---

**ROLE ANALYSIS ENFORCEMENT TABLE:**

| Mandate | Applies to |
|---------|-----------|
| DO NOT SCOPE OR SHORTEN | Q1, Q2, Q3 |
| DO NOT limit to financial columns | Q1, Q2, Q3 |
| DO NOT ROUTE ANY CONSTRAINT TYPE THROUGH A FREE-FORM FIELD | Q1, Q2, Q3 |
| All YES types in dedicated binary-state fields | Q1, Q2, Q3 |
| All findings cite "(Step N from P0)" | Q1, Q2, Q3 |

---

**Q1 — OPERATIONS EXPERT** *(Step N from P0)*

Q1 establishes shared infrastructure substrate. Operations-first ordering mandated (C-40 compliance). B2 substrate derives from Q1.

**A — BEFORE/AFTER STATE TABLE:**

| Column | Before type | Before constraints | After type | After constraints |
|--------|------------|-------------------|-----------|-----------------|

ALL tables. Missing = DISQUALIFIER.

**B — DATA LOSS TABLE:**

| Column | Data lost/truncated | Migration step | Loss mechanism |
|--------|---------------------|----------------|---------------|

**C — CONSTRAINT RISK TABLE:**

| Type | Risk (BINARY FIELD) | Violation Scenario | Migration Response |
|------|--------------------|--------------------|-------------------|
| NOT NULL | YES / NO | | |
| FK | YES / NO | | |
| UNIQUE | YES / NO | | |
| CHECK | YES / NO | | |

**D — DEFAULT AUDIT TABLE:**

| Column | Default | Existing rows: receive default or retain NULL? | Post-migration state |
|--------|---------|------------------------------------------------|---------------------|

**E — ZERO-DOWNTIME TABLE:**

| Viable | Strategy | Downtime window | Cause |
|--------|----------|-----------------|-------|

**F — PERFORMANCE CLIFF TABLE:**

| Table | Operation | Row-count threshold | Duration estimate |
|-------|-----------|--------------------:|------------------|

**G — ROLLBACK TABLE:**

| Last rollback point | Partial rollback consistent? | Steps (ordered) |
|---------------------|------------------------------|----------------|

**H — IDEMPOTENCY TABLE:**

| Idempotent? | Mechanism or duplicate-execution failure |
|------------|------------------------------------------|

---

**Q2 — COMMERCE EXPERT** *(Step N from P0)*

Commerce entities: catalog, SKU, pricing, promotions, order management.

Apply full A–H table structure from Q1 to Commerce entities. All YES constraint types in dedicated binary-state fields. DO NOT SCOPE OR SHORTEN. DO NOT ROUTE THROUGH FREE-FORM FIELDS.

---

**Q3 — FINANCE EXPERT** *(Step N from P0)*

Finance entities: ledger, transactions, reporting views, audit trail, fiscal period.

Apply full A–H table structure from Q1 to Finance entities. All YES constraint types in dedicated binary-state fields. DO NOT SCOPE OR SHORTEN. DO NOT ROUTE THROUGH FREE-FORM FIELDS.

---

**PHASE A-TO-B GATE TABLE:**

| Gate | Type | Required State | Current State | Blocking instruction |
|------|------|---------------|--------------|---------------------|
| PARSE GATE | BINARY FIELD | OPEN | | If CLOSED: name incomplete Q section. Do not begin Phase B. |
| ALIGNMENT STATE | BINARY FIELD | ALIGNED | | If MISALIGNED: name divergent artifact(s) — COST LEDGER row (a), Q1 domain, or B2 substrate pre-commitment — and the revision required. Do not begin Phase B. |

Both conditions required for Phase B entry. A single CLOSED or MISALIGNED row blocks Phase B.

---

### PHASE B — MIGRATION EXECUTION

**PROTOCOL COUNT MANIFEST** — complete gate registry. One row per named gate in this prompt. Fill before any B-section content.

| Gate Name | Gate Type | Source block | Required State | Current State |
|-----------|-----------|-------------|---------------|--------------|
| PARSE GATE | BINARY FIELD | P0 PARSE-TO-A GATE TABLE | OPEN | |
| PARSE GATE | BINARY FIELD | Phase A PHASE A-TO-B GATE TABLE | OPEN | |
| COST LEDGER SUBSTRATE GATE | BINARY FIELD | PRE-PARSE COST LEDGER SUBSTRATE GATE | OPEN | |
| ALIGNMENT STATE | BINARY FIELD | Phase A THREE-ARTIFACT ALIGNMENT TABLE / PHASE A-TO-B GATE TABLE | ALIGNED | |

Single verification surface: all named gates enumerated. A gate named in any block but absent from this manifest = incomplete registry. A manifest row whose Current State ≠ Required State = Phase B blocked at that gate's boundary. Resolve before continuing.

---

**B1 — MIGRATION EXECUTION STEPS TABLE:**

| Step | Operation | Constraint type affected | Transaction boundary | Failure mode |
|------|-----------|-------------------------|---------------------|-------------|

Coverage: ≥ 1 row per constraint type declared YES in CONSTRAINT TYPE REGISTRY.

---

**B2 — CROSS-ROLE IMPACT CHAIN TABLE:**

| Field | Content |
|-------|---------|
| Substrate condition | (must match COST LEDGER row (a), Q1 domain, and THREE-ARTIFACT ALIGNMENT TABLE row 1) |
| Commerce consequence | (specific Commerce entity/process/data state that fails on substrate disruption) |
| Finance consequence | (specific Finance entity/ledger/reporting output that fails on substrate disruption) |

Substrate divergence from Q1 domain = alignment failure; revise before submission.

---

**B3 — CANONICAL EXECUTION TABLE:**

| Step | Entity | NOT NULL Risk (BINARY FIELD) | FK Risk (BINARY FIELD) | UNIQUE Risk (BINARY FIELD) | CHECK Risk (BINARY FIELD) | Migration Action | Rollback Action |
|------|--------|-----------------------------|----------------------|--------------------------|--------------------------|-----------------|----------------|

All four constraint type columns required. At least one row per YES type in CONSTRAINT TYPE REGISTRY.

---

**PHASE B-TO-CLOSE GATE TABLE:**

| Gate | Type | Required | Current |
|------|------|----------|---------|
| PHASE B COMPLETION GATE | BINARY FIELD | COMPLETE | |

Condition: B1 rows present; B2 substrate matches COST LEDGER row (a) and Q1 domain; B3 all four constraint type columns filled.
