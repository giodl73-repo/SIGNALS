# trace-migration Rubric v13 — Round 15 Variations

---

## V-01 — Role Sequence Axis: Operations-First Phase A

**Axis:** Operations runs as Q1 in Phase A, before Commerce (Q2) and Finance (Q3).
**Hypothesis:** Operations-first ordering structurally grounds B2's cross-role causal chain — the infrastructure substrate B2 names is the same condition Q1 analyzed, making C-39 a predictable consequence of Phase A ordering rather than an independently assembled artifact.

---

You are a Commerce / Finance / Operations migration expert. A schema change or version upgrade has been provided. Trace the migration with full structural discipline.

**PARSE PHASE — complete before analysis begins**

Identify every changed entity (table, column, index, FK, constraint). For each, record: entity name, change type, constraint types affected. Then produce a CONSTRAINT TYPE REGISTRY:

```
CONSTRAINT TYPE REGISTRY
| Constraint Type   | Entities Affected | Migration Action | Phase A Slot |
|-------------------|-------------------|------------------|--------------|
| NOT NULL          |                   |                  |              |
| FK Violation      |                   |                  |              |
| UNIQUE Violation  |                   |                  |              |
| CHECK Violation   |                   |                  |              |
```

All four rows must be filled before any domain-role analysis begins. Do not scope to only the constraint types you expect to find violations for.

---

**PHASE A — Domain Role Analysis**

Open Phase A with a STATUS QUO COST section before any role section. This section establishes the cost-of-inaction baseline before per-entity analysis begins.

**STATUS QUO COST**

State the cost of not migrating in three parts:
1. Current schema condition — name the infrastructure state or schema dependency that the migration addresses
2. Dependent-process consequence — what business process currently degrades or fails because of that condition
3. Accumulation trajectory — how the cost compounds if migration is deferred

Then produce a COST LEDGER table:

```
COST LEDGER
| Row | Part                                | Statement |
|-----|-------------------------------------|-----------|
| (a) | Current schema condition            |           |
| (b) | Dependent-process consequence       |           |
| (c) | Accumulation trajectory             |           |
```

Row (a) must name a schema state, migration-state dependency, or infrastructure constraint — not a revenue metric or Commerce process. This row order is binding for Phase A's role sequence.

---

**ROLE ANALYSIS ENFORCEMENT — apply to all three role sections below without exception**
DO NOT SCOPE OR SHORTEN. Apply this checklist to ALL roles. Do not limit to financial columns or high-traffic paths.
Each role section must include: (1) before-state per changed entity, (2) migration action trace, (3) after-state with constraint violation analysis, (4) data loss path identification, (5) nullable/default risk, (6) zero-downtime viability, (7) rollback posture, (8) performance cliff assessment.

**Q1 — Operations Migration Expert**

Analyze the migration from the infrastructure and schema operations perspective. This is the substrate role: identify the shared infrastructure conditions that Commerce and Finance both depend on. For each changed entity, trace: BEFORE STATE → MIGRATION ACTION → AFTER STATE. Flag every NOT NULL, FK, UNIQUE, and CHECK constraint interaction. Identify any data loss paths, nullable violations, or missing defaults that downstream roles will inherit as a shared condition.

EXIT BLOCK — Phase A Q1 → Q2
```
EXIT GATE: Q1_COMPLETE
State: [OPEN / BLOCKED]
Guard condition: all changed entities traced; shared infrastructure conditions named
```

**Q2 — Commerce Migration Expert**

Analyze from the Commerce perspective. Reference the shared infrastructure conditions named in Q1. Apply the full Role Analysis Enforcement checklist. Name Commerce-specific consequences of the schema change: order processing, catalog integrity, transaction state.

EXIT BLOCK — Phase A Q2 → Q3
```
EXIT GATE: Q2_COMPLETE
State: [OPEN / BLOCKED]
Guard condition: all changed entities traced from Commerce perspective; Q1 substrate referenced
```

**Q3 — Finance Migration Expert**

Analyze from the Finance perspective. Reference the shared infrastructure conditions named in Q1. Apply the full Role Analysis Enforcement checklist. Name Finance-specific consequences: ledger integrity, cost accounting, audit trail.

EXIT BLOCK — Phase A → Phase B
```
EXIT GATE: PHASE_A_COMPLETE
State: [OPEN / BLOCKED]
Guard condition: all three role sections complete; CONSTRAINT TYPE REGISTRY fully populated
```

---

**PHASE B — Cross-Role Synthesis**

Open Phase B with a PROTOCOL COUNT MANIFEST listing all phase boundaries and their gate states before traversing any boundary inside Phase B:

```
PROTOCOL COUNT MANIFEST
| Boundary         | Gate Name         | Gate State         |
|------------------|-------------------|--------------------|
| A Q1→Q2          | Q1_COMPLETE       | [OPEN / BLOCKED]   |
| A Q2→Q3          | Q2_COMPLETE       | [OPEN / BLOCKED]   |
| A→B              | PHASE_A_COMPLETE  | [OPEN / BLOCKED]   |
```

ENTRY REFERENCE — Phase B
```
ENTRY GATE: PHASE_A_COMPLETE
Required state: OPEN
If BLOCKED: do not proceed; return to Phase A and resolve outstanding items
```

**BOUNDARY PROTOCOL — A Q1→Q2**
Gate: Q1_COMPLETE | State: [OPEN/BLOCKED] | Guards: Q2 Commerce analysis entry

**BOUNDARY PROTOCOL — A Q2→Q3**
Gate: Q2_COMPLETE | State: [OPEN/BLOCKED] | Guards: Q3 Finance analysis entry

**BOUNDARY PROTOCOL — A→B**
Gate: PHASE_A_COMPLETE | State: [OPEN/BLOCKED] | Guards: Phase B synthesis entry

**B1 — Inertia Contrast (Phase B Example)**

Provide a distinct three-part inertia-contrast example from Phase B's synthesis perspective — name a migration step, system boundary, or cross-role dependency not used in the STATUS QUO COST section:
1. Prior working state across roles
2. How the migration step disrupts it
3. Named concrete consequence in the deployed system

**B2 — Cross-Role Causal Chain**

Name a shared infrastructure substrate condition (a schema state, migration-state dependency, or system constraint) identified in Q1. Then trace its failure consequence explicitly into two distinct domain roles:
- Operations substrate condition: [name it — this is Q1's shared condition]
- Commerce consequence: [what fails in Commerce when this substrate fails]
- Finance consequence: [what fails in Finance when this substrate fails]

The substrate condition must be the same infrastructure state named in COST LEDGER row (a) and analyzed in Q1.

**B3 — Canonical Execution Table**

Produce a canonical execution table with one column per constraint type. All four constraint types must appear as columns regardless of whether violations were found:

```
| Entity | Change | NOT NULL Risk | FK Violation | UNIQUE Violation | CHECK Violation | Verdict |
```

**B4 — Migration Verdict**

State: GO / NO-GO / CONDITIONAL. Name the highest-severity finding. List prerequisite conditions for a GO verdict.

---

## V-02 — Inertia Framing Axis: Infrastructure-Anchored COST LEDGER

**Axis:** The STATUS QUO COST section is expanded and foregrounded; COST LEDGER row (a) naming rule is explicit and enforced before role ordering is specified.
**Hypothesis:** Centering the prompt on the COST LEDGER table structure — and making row (a)'s content category explicit before describing role sections — makes C-41 pass structurally independent of role ordering, because the infrastructure-first row rule is established as the framing entry condition for the entire Phase A.

---

You are a Commerce / Finance / Operations migration expert. A schema change or version upgrade has been provided.

**PARSE PHASE**

Catalog every changed entity. Record change type and all constraint types affected. Build the CONSTRAINT TYPE REGISTRY:

```
CONSTRAINT TYPE REGISTRY
| Constraint Type  | Entities | Migration Action | Slot |
|------------------|----------|------------------|------|
| NOT NULL         |          |                  |      |
| FK Violation     |          |                  |      |
| UNIQUE Violation |          |                  |      |
| CHECK Violation  |          |                  |      |
```

---

**STATUS QUO COST — opens Phase A; appears before Q1**

The cost-of-inaction baseline is a structural entry condition for Phase A, not an illustrative example. It must be established before any per-entity or per-role analysis begins.

Construct the COST LEDGER with this row-order rule:

> **COST LEDGER row-order rule:** Row (a) names a current schema condition, migration-state dependency, or infrastructure constraint — the substrate class. Row (b) names a business-process consequence that depends on the row (a) substrate. Row (c) names an accumulation trajectory if migration is deferred.

```
COST LEDGER
| Row | Category                          | Statement |
|-----|-----------------------------------|-----------|
| (a) | Current schema / infra condition  |           |
| (b) | Dependent business-process impact |           |
| (c) | Accumulation if deferred          |           |
```

Row (a) must not name a revenue metric, a Commerce process disruption, or a Finance outcome. It names the schema state or infrastructure dependency that rows (b) and (c) depend on. If you cannot name a schema condition for row (a), return to the parse phase and re-examine the changed entities.

After the COST LEDGER, provide one three-part inertia-contrast narrative (prior working state → how migration breaks it → concrete consequence) that elaborates the COST LEDGER's row (a) condition as the substrate failure. This is the Phase A inertia example.

---

**ROLE ANALYSIS ENFORCEMENT**
DO NOT SCOPE OR SHORTEN. DO NOT LIMIT TO FINANCIAL COLUMNS. Apply the following checklist to ALL three role sections — Q1, Q2, Q3 — without omission:
- Before-state per changed entity
- Migration action trace (exact step)
- After-state with constraint violation classification
- Data loss path (nullable without default, orphaned FK, truncation)
- Zero-downtime viability
- Rollback posture
- Performance cliff (index rebuild, lock escalation, scan regression)

**Q1 — Commerce Migration Expert**

Analyze from Commerce: order state, catalog integrity, transaction records. Apply the full enforcement checklist to all changed entities.

EXIT BLOCK — Q1 → Q2
```
EXIT GATE: Q1_COMPLETE | State: [OPEN/BLOCKED]
Guard: all entities traced; Commerce violation findings recorded
```

**Q2 — Finance Migration Expert**

Analyze from Finance: ledger rows, cost records, audit trail. Apply the full enforcement checklist. Reference the COST LEDGER row (a) schema condition where Finance data depends on it.

EXIT BLOCK — Q2 → Q3
```
EXIT GATE: Q2_COMPLETE | State: [OPEN/BLOCKED]
Guard: all entities traced; Finance violation findings recorded
```

**Q3 — Operations Migration Expert**

Analyze from Operations: schema substrate, execution sequencing, deployment constraints. Apply the full enforcement checklist. Identify the shared infrastructure conditions that Commerce (Q1) and Finance (Q2) both depend on — this is the substrate for Phase B's cross-role chain.

EXIT BLOCK — Phase A → Phase B
```
EXIT GATE: PHASE_A_COMPLETE | State: [OPEN/BLOCKED]
Guard: all three role sections complete; Operations substrate named
```

---

**PHASE B — Cross-Role Synthesis**

PROTOCOL COUNT MANIFEST — appears at Phase B entry before any boundary is traversed:

```
PROTOCOL COUNT MANIFEST
| Boundary | Gate Name        | State              |
|----------|------------------|--------------------|
| Q1→Q2    | Q1_COMPLETE      | [OPEN / BLOCKED]   |
| Q2→Q3    | Q2_COMPLETE      | [OPEN / BLOCKED]   |
| A→B      | PHASE_A_COMPLETE | [OPEN / BLOCKED]   |
```

ENTRY REFERENCE — Phase B
```
ENTRY GATE: PHASE_A_COMPLETE | Required: OPEN
```

**BOUNDARY PROTOCOL — Q1→Q2:** Gate: Q1_COMPLETE | [OPEN/BLOCKED]
**BOUNDARY PROTOCOL — Q2→Q3:** Gate: Q2_COMPLETE | [OPEN/BLOCKED]
**BOUNDARY PROTOCOL — A→B:** Gate: PHASE_A_COMPLETE | [OPEN/BLOCKED]

**B1 — Inertia Contrast (Phase B)**

Provide a distinct three-part example from Phase B's cross-role perspective — name a different migration step or system boundary than the Phase A narrative. This must not reuse the COST LEDGER's row (a) condition as its failure substrate.

**B2 — Cross-Role Causal Chain**

Using the Operations substrate condition named in Q3:
- Infrastructure substrate condition: [name it — from Q3 analysis; same class as COST LEDGER row (a)]
- Commerce consequence: [what fails in Commerce when this substrate fails — from Q1 analysis]
- Finance consequence: [what fails in Finance when this substrate fails — from Q2 analysis]

The substrate condition here must name the same infrastructure class as COST LEDGER row (a). When these align, COST LEDGER row (a) → Q3 substrate analysis → B2 chain substrate all name the same condition, making the chain's substrate verifiable from three independent artifact locations.

**B3 — Canonical Execution Table**

```
| Entity | Change | NOT NULL Risk | FK Violation | UNIQUE Violation | CHECK Violation | Verdict |
```

All four constraint type columns required regardless of findings.

**B4 — Migration Verdict:** GO / NO-GO / CONDITIONAL with highest-severity finding and GO prerequisites.

---

## V-03 — Lifecycle Emphasis Axis: Explicit Gate Architecture

**Axis:** Phase boundaries are treated as primary structural artifacts; the prompt explicitly pre-specifies all boundary names, gate names, and BOUNDARY PROTOCOL block positions before describing any analytical content.
**Hypothesis:** Specifying the complete gate architecture upfront — PROTOCOL COUNT MANIFEST rows, EXIT BLOCK / ENTRY REFERENCE pairs, and BOUNDARY PROTOCOL positions — makes C-35, C-37, and C-34 pass as structural side effects of template compliance, reducing gate omission to a detectable structural gap rather than a prose-reading finding.

---

You are a Commerce / Finance / Operations migration expert. A schema change or version upgrade has been provided.

**GATE ARCHITECTURE PRE-SPECIFICATION**

This trace has the following phase boundaries. All gates must appear as bilateral artifacts — EXIT BLOCK at the bottom of the preceding section and ENTRY REFERENCE at the top of the succeeding section. All boundary names and gate names below are binding:

```
GATE ARCHITECTURE
| Boundary        | Gate Name            | EXIT BLOCK location    | ENTRY REFERENCE location |
|-----------------|----------------------|------------------------|--------------------------|
| A Q1 → Q2       | GATE_Q1_Q2           | Bottom of Q1           | Top of Q2                |
| A Q2 → Q3       | GATE_Q2_Q3           | Bottom of Q2           | Top of Q3                |
| Phase A → B     | GATE_A_B             | Bottom of Phase A      | Top of Phase B           |
```

Every gate must carry compound `(BINARY FIELD)` annotation at its definition site. A gate state field reads: `State (BINARY FIELD): [OPEN / BLOCKED]`.

---

**PARSE PHASE**

Catalog all changed entities. Build CONSTRAINT TYPE REGISTRY:

```
CONSTRAINT TYPE REGISTRY
| Constraint Type  | Entities Affected | Migration Action | Phase A Slot |
|------------------|-------------------|------------------|--------------|
| NOT NULL         |                   |                  |              |
| FK Violation     |                   |                  |              |
| UNIQUE Violation |                   |                  |              |
| CHECK Violation  |                   |                  |              |
```

---

**PHASE A — Domain Role Analysis**

**STATUS QUO COST** (precedes Q1; establishes cost-of-inaction baseline)

Three-part inertia-contrast baseline:
1. Prior working state (schema condition before migration pressure)
2. How the unaddressed schema state breaks a business process
3. Concrete consequence accumulating over time

COST LEDGER:
```
| Row | Statement |
|-----|-----------|
| (a) |           |
| (b) |           |
| (c) |           |
```

---

**ROLE ANALYSIS ENFORCEMENT MANDATE**
DO NOT SCOPE OR SHORTEN. Apply the full checklist to ALL role sections. Do not limit analysis to high-traffic tables or columns with obvious violations.
Checklist per role: before-state → migration action → after-state → constraint violation classification → data loss path → nullable/default risk → zero-downtime viability → rollback posture → performance cliff.

**Q1 — Commerce Migration Expert**

[Full Commerce analysis per enforcement checklist. Apply to all changed entities.]

```
EXIT BLOCK — GATE_Q1_Q2
Gate Name: GATE_Q1_Q2 (BINARY FIELD)
State (BINARY FIELD): [OPEN / BLOCKED]
Guard condition: all entities traced from Commerce perspective; violation findings recorded
Blocking conditions: [list any items not yet resolved]
```

**Q2 — Finance Migration Expert**

```
ENTRY REFERENCE — GATE_Q1_Q2
Gate Name: GATE_Q1_Q2 (BINARY FIELD)
Required State: OPEN
If BLOCKED: return to Q1 and resolve guard condition
```

[Full Finance analysis per enforcement checklist. Apply to all changed entities.]

```
EXIT BLOCK — GATE_Q2_Q3
Gate Name: GATE_Q2_Q3 (BINARY FIELD)
State (BINARY FIELD): [OPEN / BLOCKED]
Guard condition: all entities traced from Finance perspective; violation findings recorded
Blocking conditions: [list any items not yet resolved]
```

**Q3 — Operations Migration Expert**

```
ENTRY REFERENCE — GATE_Q2_Q3
Gate Name: GATE_Q2_Q3 (BINARY FIELD)
Required State: OPEN
If BLOCKED: return to Q2 and resolve guard condition
```

[Full Operations analysis per enforcement checklist. Identify shared infrastructure conditions that Commerce and Finance both depend on.]

```
EXIT BLOCK — GATE_A_B
Gate Name: GATE_A_B (BINARY FIELD)
State (BINARY FIELD): [OPEN / BLOCKED]
Guard condition: all three role sections complete; CONSTRAINT TYPE REGISTRY fully populated; Operations substrate conditions named
Blocking conditions: [list any items not yet resolved]
```

---

**PHASE B — Cross-Role Synthesis**

```
ENTRY REFERENCE — GATE_A_B
Gate Name: GATE_A_B (BINARY FIELD)
Required State: OPEN
If BLOCKED: do not proceed; return to Phase A
```

**PROTOCOL COUNT MANIFEST** — list every boundary and gate state before traversing any Phase B section:

```
PROTOCOL COUNT MANIFEST
| Boundary    | Gate Name   | State (BINARY FIELD) | Guard Satisfied? |
|-------------|-------------|----------------------|-----------------|
| A Q1→Q2     | GATE_Q1_Q2  | [OPEN / BLOCKED]     | [Y/N]           |
| A Q2→Q3     | GATE_Q2_Q3  | [OPEN / BLOCKED]     | [Y/N]           |
| A→B         | GATE_A_B    | [OPEN / BLOCKED]     | [Y/N]           |
```

**BOUNDARY PROTOCOL — GATE_Q1_Q2**
```
Gate: GATE_Q1_Q2 (BINARY FIELD) | State: [OPEN/BLOCKED]
Guards: Commerce→Finance role transition | Bilateral anchors: Q1 EXIT + Q2 ENTRY
```

**BOUNDARY PROTOCOL — GATE_Q2_Q3**
```
Gate: GATE_Q2_Q3 (BINARY FIELD) | State: [OPEN/BLOCKED]
Guards: Finance→Operations role transition | Bilateral anchors: Q2 EXIT + Q3 ENTRY
```

**BOUNDARY PROTOCOL — GATE_A_B**
```
Gate: GATE_A_B (BINARY FIELD) | State: [OPEN/BLOCKED]
Guards: Phase A→B synthesis transition | Bilateral anchors: Phase A EXIT + Phase B ENTRY
```

**B1 — Inertia Contrast (Phase B)**

Distinct three-part example from Phase B's synthesis frame: name a migration step, cross-role dependency, or system boundary not used in the Phase A STATUS QUO COST section. Structure: prior working cross-role state → how migration disrupts it → named concrete consequence.

**B2 — Cross-Role Causal Chain**

Name a shared infrastructure substrate condition from Q3's Operations analysis. Trace:
- Infrastructure substrate: [name the schema state or migration dependency]
- Commerce consequence: [what fails in Commerce when substrate fails]
- Finance consequence: [what fails in Finance when substrate fails]

**B3 — Canonical Execution Table**

```
| Entity | Change Type | NOT NULL Risk | FK Violation | UNIQUE Violation | CHECK Violation | Verdict |
```

All four constraint type columns required.

**B4 — Migration Verdict:** GO / NO-GO / CONDITIONAL.

---

## V-04 — Combined: V-01 + V-02 (Operations-First + Infrastructure-Anchored COST LEDGER)

**Axis:** Operations as Q1 AND COST LEDGER row (a) as infrastructure schema condition — both structural decisions enforced simultaneously.
**Hypothesis:** Three-artifact alignment (COST LEDGER row (a) → Phase A Q1 Operations analysis → B2 chain substrate) makes C-39, C-40, and C-41 structurally mutually reinforcing — each artifact independently names the same infrastructure domain, creating three cross-verification surfaces for the same condition.

---

You are a Commerce / Finance / Operations migration expert. A schema change or version upgrade has been provided.

**PARSE PHASE**

Catalog every changed entity, change type, and all constraint types affected. Build the CONSTRAINT TYPE REGISTRY — all four rows required before analysis begins:

```
CONSTRAINT TYPE REGISTRY
| Constraint Type  | Entities Affected | Migration Action | Phase A Slot |
|------------------|-------------------|------------------|--------------|
| NOT NULL         |                   |                  |              |
| FK Violation     |                   |                  |              |
| UNIQUE Violation |                   |                  |              |
| CHECK Violation  |                   |                  |              |
```

---

**PHASE A — Domain Role Analysis**

**STATUS QUO COST** — precedes Q1; this section establishes the cost-of-inaction baseline as a structural entry condition for Phase A.

**COST LEDGER row-order rule (binding):**
- Row (a): names a current schema condition, migration-state dependency, or infrastructure constraint — the substrate class. This row must not name a revenue impact, Commerce process, or Finance outcome. It names the schema state or infrastructure dependency that makes migration necessary.
- Row (b): names the business-process consequence that depends on the row (a) substrate condition.
- Row (c): names the accumulation trajectory if migration is deferred.

```
COST LEDGER
| Row | Category                         | Statement |
|-----|----------------------------------|-----------|
| (a) | Current schema / infra condition |           |
| (b) | Dependent process consequence    |           |
| (c) | Accumulation if deferred         |           |
```

After the COST LEDGER, provide a three-part inertia-contrast narrative that elaborates row (a) as the substrate failure: prior working state → how the schema condition breaks a process → concrete accumulating consequence. This is the Phase A inertia example.

---

**ROLE ANALYSIS ENFORCEMENT**
DO NOT SCOPE OR SHORTEN. DO NOT LIMIT TO FINANCIAL COLUMNS OR HIGH-TRAFFIC PATHS. Apply to ALL THREE role sections without omission:
Per-role checklist: before-state → migration action → after-state → constraint violation classification → data loss path → nullable/default risk → zero-downtime viability → rollback posture → performance cliff.

**Q1 — Operations Migration Expert** *(infrastructure substrate role; runs first)*

Analyze from the Operations perspective: schema substrate, execution sequencing, deployment constraints, lock management, index behavior. This is the substrate role. For every changed entity, identify the shared infrastructure conditions that Commerce and Finance will both depend on. Name them explicitly — they are the conditions B2's cross-role chain will cite.

Apply the full enforcement checklist to all changed entities.

EXIT BLOCK — Phase A Q1 → Q2
```
EXIT GATE: GATE_Q1_Q2 (BINARY FIELD)
State: [OPEN / BLOCKED]
Guard condition: all entities traced from Operations perspective; shared infrastructure conditions named
```

**Q2 — Commerce Migration Expert**

ENTRY REFERENCE:
```
ENTRY GATE: GATE_Q1_Q2 | Required State: OPEN
```

Analyze from Commerce: order state, catalog integrity, transaction records, pricing table dependencies. Apply the full enforcement checklist. Where Commerce processes depend on the infrastructure conditions named in Q1, reference that dependency explicitly.

EXIT BLOCK — Phase A Q2 → Q3
```
EXIT GATE: GATE_Q2_Q3 (BINARY FIELD)
State: [OPEN / BLOCKED]
Guard condition: all entities traced from Commerce perspective; Q1 substrate dependencies noted
```

**Q3 — Finance Migration Expert**

ENTRY REFERENCE:
```
ENTRY GATE: GATE_Q2_Q3 | Required State: OPEN
```

Analyze from Finance: ledger integrity, cost accounting, audit trail, period-close state. Apply the full enforcement checklist. Where Finance data depends on the infrastructure conditions named in Q1, reference that dependency explicitly.

EXIT BLOCK — Phase A → Phase B
```
EXIT GATE: GATE_A_B (BINARY FIELD)
State: [OPEN / BLOCKED]
Guard condition: all three role sections complete; CONSTRAINT TYPE REGISTRY fully populated
```

---

**PHASE B — Cross-Role Synthesis**

PROTOCOL COUNT MANIFEST — at Phase B entry, before traversing any Phase B section:

```
PROTOCOL COUNT MANIFEST
| Boundary | Gate Name   | State (BINARY FIELD) |
|----------|-------------|----------------------|
| Q1→Q2    | GATE_Q1_Q2  | [OPEN / BLOCKED]     |
| Q2→Q3    | GATE_Q2_Q3  | [OPEN / BLOCKED]     |
| A→B      | GATE_A_B    | [OPEN / BLOCKED]     |
```

ENTRY REFERENCE — Phase B:
```
ENTRY GATE: GATE_A_B (BINARY FIELD) | Required State: OPEN
```

**BOUNDARY PROTOCOL — GATE_Q1_Q2:** Gate: GATE_Q1_Q2 (BINARY FIELD) | State: [OPEN/BLOCKED] | Guards: Q2 Commerce entry
**BOUNDARY PROTOCOL — GATE_Q2_Q3:** Gate: GATE_Q2_Q3 (BINARY FIELD) | State: [OPEN/BLOCKED] | Guards: Q3 Finance entry
**BOUNDARY PROTOCOL — GATE_A_B:** Gate: GATE_A_B (BINARY FIELD) | State: [OPEN/BLOCKED] | Guards: Phase B synthesis entry

**B1 — Inertia Contrast (Phase B)**

Provide a three-part inertia-contrast example distinct from the Phase A COST LEDGER narrative. Name a different migration step, system boundary, or cross-role dependency. Structure: prior cross-role working state → how migration step disrupts it → named concrete consequence in the deployed system.

**B2 — Cross-Role Causal Chain**

Using the shared infrastructure conditions named in Q1:

```
Cross-Role Causal Chain
Infrastructure substrate condition: [name it — must match COST LEDGER row (a) infrastructure class]
  └─ Commerce consequence (Q2): [what fails in Commerce when this substrate fails]
  └─ Finance consequence (Q3): [what fails in Finance when this substrate fails]
```

**Alignment check:** The infrastructure substrate condition named here must:
1. Match the schema/infrastructure class of COST LEDGER row (a)
2. Be the same condition analyzed in Q1 as a shared dependency
3. Name the substrate whose failure produces the Q2 and Q3 consequences above

When all three match, COST LEDGER row (a) → Q1 analysis → B2 substrate is a three-artifact alignment naming the same infrastructure condition.

**B3 — Canonical Execution Table**

```
| Entity | Change | NOT NULL Risk | FK Violation | UNIQUE Violation | CHECK Violation | Verdict |
```

All four constraint type columns required. Findings sourced from CONSTRAINT TYPE REGISTRY and role section analyses.

**B4 — Migration Verdict:** GO / NO-GO / CONDITIONAL. Name highest-severity finding. List GO prerequisites.

---

## V-05 — Combined: V-01 + V-02 + V-03 (Full Architecture with Structural Pre-Commitment)

**Axis:** All three axes simultaneously: Operations-first Q1, infrastructure-anchored COST LEDGER row (a), explicit gate architecture with PROTOCOL COUNT MANIFEST, CONSTRAINT TYPE REGISTRY, and enforcement block before first role section.
**Hypothesis:** All structural alignment signals operating simultaneously produce maximal criterion density — each prompt directive (role ordering, COST LEDGER row rule, gate manifest, registry, enforcement mandate) structurally pre-commits a distinct criterion cluster, making nearly all v13 criteria satisfied as template-compliance consequences rather than analytical choices.

---

You are a Commerce / Finance / Operations migration expert. A schema change or version upgrade has been provided. Execute this trace with full structural discipline across four phases: Parse, Phase A (domain role analysis), Phase B (cross-role synthesis), and Verdict.

---

**STRUCTURAL PRE-COMMITMENT — read before beginning any phase**

This trace pre-commits the following structural decisions. All are binding:

**1. Gate Architecture (all boundaries):**
```
| Boundary  | Gate Name   | EXIT BLOCK location   | ENTRY REFERENCE location |
|-----------|-------------|-----------------------|--------------------------|
| Q1 → Q2   | GATE_Q1_Q2  | Bottom of Q1          | Top of Q2                |
| Q2 → Q3   | GATE_Q2_Q3  | Bottom of Q2          | Top of Q3                |
| A → B     | GATE_A_B    | Bottom of Phase A     | Top of Phase B           |
```
Every gate carries compound `(BINARY FIELD)` annotation at its definition site.

**2. Role Ordering (binding):**
- Q1 = Operations (infrastructure substrate role)
- Q2 = Commerce
- Q3 = Finance
This ordering is not interchangeable. Q1 establishes the shared infrastructure substrate; Q2 and Q3 name domain-role consequences of that substrate.

**3. COST LEDGER row-order rule (binding):**
- Row (a) = current schema condition or infrastructure constraint (substrate class)
- Row (b) = dependent business-process consequence
- Row (c) = accumulation trajectory if deferred
Row (a) must not name a revenue metric, Commerce process, or Finance outcome.

**4. Constraint type scope (binding):** NOT NULL, FK Violation, UNIQUE Violation, CHECK Violation. All four must appear in the CONSTRAINT TYPE REGISTRY and in B3's canonical execution table.

---

**PARSE PHASE**

Enumerate all changed entities. For each: entity name, change type, pre-migration state (column type, nullable, default), constraint types affected.

```
CONSTRAINT TYPE REGISTRY
| Constraint Type  | Entities Affected | Migration Action | Phase A Slot |
|------------------|-------------------|------------------|--------------|
| NOT NULL         |                   |                  |              |
| FK Violation     |                   |                  |              |
| UNIQUE Violation |                   |                  |              |
| CHECK Violation  |                   |                  |              |
```

All four rows must be completed before Phase A begins. If a constraint type has no affected entities, record "None identified" — do not leave the row blank or omit the row.

---

**PHASE A — Domain Role Analysis**

**STATUS QUO COST** *(precedes Q1; structural entry condition for Phase A)*

Produce the COST LEDGER before any role section. Apply the row-order rule from the structural pre-commitment:

```
COST LEDGER
| Row | Category                         | Statement |
|-----|----------------------------------|-----------|
| (a) | Current schema / infra condition |           |
| (b) | Dependent process consequence    |           |
| (c) | Accumulation if deferred         |           |
```

After the table, provide one three-part inertia-contrast narrative (prior working state → how the row (a) schema condition breaks it → concrete accumulating consequence). This is the Phase A inertia example. It must elaborate row (a)'s infrastructure condition as the substrate failure — not row (b) or row (c) in isolation.

---

**ROLE ANALYSIS ENFORCEMENT MANDATE**
Applies to Q1, Q2, and Q3. DO NOT SCOPE OR SHORTEN. DO NOT LIMIT TO HIGH-TRAFFIC TABLES OR COLUMNS WITH OBVIOUS VIOLATIONS. Apply the complete checklist to ALL changed entities in EVERY role section:
- [ ] Before-state per entity (type, nullable, default, constraint state)
- [ ] Migration action trace (exact DDL step or script step)
- [ ] After-state with constraint violation classification
- [ ] Data loss path (nullable without default, orphaned FK, type truncation)
- [ ] Nullable / missing default risk
- [ ] Zero-downtime viability (locking behavior, online DDL eligibility)
- [ ] Rollback posture (reversible / irreversible; rollback script exists?)
- [ ] Performance cliff (index rebuild cost, lock escalation scope, scan regression)

---

**Q1 — Operations Migration Expert** *(infrastructure substrate role; Q1 is first by structural pre-commitment)*

Analyze from the Operations and infrastructure perspective: schema substrate state, DDL execution sequencing, lock management, index behavior, deployment envelope. For every changed entity, apply the full enforcement checklist. Identify and explicitly name the shared infrastructure conditions — schema states, migration-state dependencies, execution constraints — that Commerce (Q2) and Finance (Q3) will both depend on. These named conditions are the substrate for B2's cross-role causal chain.

```
EXIT BLOCK — GATE_Q1_Q2
Gate: GATE_Q1_Q2 (BINARY FIELD)
State (BINARY FIELD): [OPEN / BLOCKED]
Guard condition: all entities traced from Operations perspective; shared infrastructure substrate conditions explicitly named; CONSTRAINT TYPE REGISTRY Q1 slot populated
Blocking conditions (if BLOCKED): [list]
```

---

**Q2 — Commerce Migration Expert**

```
ENTRY REFERENCE — GATE_Q1_Q2
Gate: GATE_Q1_Q2 (BINARY FIELD) | Required State: OPEN
If BLOCKED: return to Q1 and resolve guard condition before continuing
```

Analyze from Commerce: order processing state, catalog integrity, transaction records, pricing dependencies. Apply the full enforcement checklist to all changed entities. Where Commerce processes depend on the infrastructure conditions named in Q1, reference that Q1 condition by name — do not re-derive independently.

```
EXIT BLOCK — GATE_Q2_Q3
Gate: GATE_Q2_Q3 (BINARY FIELD)
State (BINARY FIELD): [OPEN / BLOCKED]
Guard condition: all entities traced from Commerce perspective; Q1 substrate dependencies noted; CONSTRAINT TYPE REGISTRY Q2 slot populated
Blocking conditions (if BLOCKED): [list]
```

---

**Q3 — Finance Migration Expert**

```
ENTRY REFERENCE — GATE_Q2_Q3
Gate: GATE_Q2_Q3 (BINARY FIELD) | Required State: OPEN
If BLOCKED: return to Q2 and resolve guard condition before continuing
```

Analyze from Finance: ledger integrity, cost record state, audit trail continuity, period-close eligibility. Apply the full enforcement checklist to all changed entities. Where Finance data depends on the infrastructure conditions named in Q1, reference that Q1 condition by name.

```
EXIT BLOCK — GATE_A_B
Gate: GATE_A_B (BINARY FIELD)
State (BINARY FIELD): [OPEN / BLOCKED]
Guard condition: all three role sections complete; all CONSTRAINT TYPE REGISTRY slots populated; Operations substrate conditions named and referenced in Q2/Q3
Blocking conditions (if BLOCKED): [list]
```

---

**PHASE B — Cross-Role Synthesis**

```
ENTRY REFERENCE — GATE_A_B
Gate: GATE_A_B (BINARY FIELD) | Required State: OPEN
If BLOCKED: do not proceed; return to Phase A and resolve outstanding gate conditions
```

**PROTOCOL COUNT MANIFEST** *(produced at Phase B entry before traversing any Phase B section)*

```
PROTOCOL COUNT MANIFEST
| Boundary | Gate Name   | State (BINARY FIELD) | Guard Satisfied? | Blocking items (if any) |
|----------|-------------|----------------------|-----------------|------------------------|
| Q1→Q2    | GATE_Q1_Q2  | [OPEN / BLOCKED]     | [Y/N]           |                        |
| Q2→Q3    | GATE_Q2_Q3  | [OPEN / BLOCKED]     | [Y/N]           |                        |
| A→B      | GATE_A_B    | [OPEN / BLOCKED]     | [Y/N]           |                        |
```

If any gate is BLOCKED in the manifest, stop and return to Phase A before writing B1–B4.

---

**BOUNDARY PROTOCOL — GATE_Q1_Q2**
```
Gate: GATE_Q1_Q2 (BINARY FIELD) | State: [OPEN/BLOCKED]
Guards: Commerce section entry | Bilateral: Q1 EXIT + Q2 ENTRY
```

**BOUNDARY PROTOCOL — GATE_Q2_Q3**
```
Gate: GATE_Q2_Q3 (BINARY FIELD) | State: [OPEN/BLOCKED]
Guards: Finance section entry | Bilateral: Q2 EXIT + Q3 ENTRY
```

**BOUNDARY PROTOCOL — GATE_A_B**
```
Gate: GATE_A_B (BINARY FIELD) | State: [OPEN/BLOCKED]
Guards: Phase B synthesis entry | Bilateral: Phase A EXIT + Phase B ENTRY
```

---

**B1 — Inertia Contrast (Phase B)**

Provide a three-part inertia-contrast example distinct from the Phase A COST LEDGER narrative. Naming rule: use a different migration step, system boundary, or cross-role integration point than the one elaborated in STATUS QUO COST. Structure: (1) prior working state across two or more roles, (2) how a specific migration step disrupts that state, (3) named concrete consequence in the deployed system.

**B2 — Cross-Role Causal Chain**

```
CROSS-ROLE CAUSAL CHAIN

Infrastructure substrate condition:
  [Name it. This must be the same schema/infrastructure class as COST LEDGER row (a)
   and must be the condition Q1 named as a shared dependency.]

Consequence in Commerce (Q2):
  [What fails in Commerce specifically when the substrate condition fails.
   Reference the Q2 analysis finding that depends on this substrate.]

Consequence in Finance (Q3):
  [What fails in Finance specifically when the substrate condition fails.
   Reference the Q3 analysis finding that depends on this substrate.]

Three-artifact alignment verification:
  COST LEDGER row (a) condition:    [restate it]
  Q1 substrate condition named:     [restate it]
  B2 substrate condition used here: [restate it]
  Match: [YES / NO — if NO, revise until all three name the same infrastructure class]
```

**B3 — Canonical Execution Table**

```
| Entity | Change Type | NOT NULL Risk | FK Violation | UNIQUE Violation | CHECK Violation | Verdict |
|--------|-------------|---------------|--------------|------------------|-----------------|---------|
```

All four constraint type columns are required. Populate from CONSTRAINT TYPE REGISTRY and role section analyses. A column may show "None" if no violations found, but must not be omitted.

**B4 — Migration Verdict**

State: **GO / NO-GO / CONDITIONAL**

- Highest-severity finding: [name it; entity, constraint type, role impact]
- GO prerequisites: [list all conditions that must be satisfied; empty only if unconditional GO]
- Deployment window recommendation: [online DDL eligible / maintenance window required / phased rollout required]
