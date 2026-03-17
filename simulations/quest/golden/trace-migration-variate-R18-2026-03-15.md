# trace-migration Variate — Round 18
**Date:** 2026-03-15
**Rubric:** v16 (C-46 + C-47 introduced)
**Target criteria:** C-46 (BINARY FIELD annotation symmetry at ENTRY REFERENCE positions), C-47 (PROTOCOL COUNT MANIFEST self-referential completeness assertion)

---

## Round 18 Variation Map

| Variation | Axis | C-46 | C-47 | Notes |
|-----------|------|------|------|-------|
| V-01 | Role sequence | Expected PASS | Expected PASS | Operations-as-substrate framing drives both gate positions to carry compound annotation naturally; manifest structured as a verification contract |
| V-02 | Output format | Expected PASS | Expected PASS | Table-first format specifies manifest schema explicitly including completeness rule; gate schema specified at both anchor positions |
| V-03 | Lifecycle emphasis | Expected PASS | Expected PARTIAL | Per-phase vocabulary + coverage floors anchor the gate chain; manifest completeness rule present but emergent rather than required |
| V-04 | Role sequence + Phrasing register | Expected PASS | Expected PASS | Imperative DIRECTIVE fields eliminate annotation omission paths; manifest DIRECTIVE explicitly requires self-referential rule |
| V-05 | Combined: Role sequence + Output format + Lifecycle emphasis | Expected PASS | Expected PASS | Full combination: three-artifact alignment + table gates + per-phase floors + explicit completeness contract |

---

## V-01 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Framing Operations as the "substrate declaration" role (Q1) and Commerce/Finance as "downstream consequence" roles (Q2, Q3) creates a structural incentive to carry the `(BINARY FIELD)` compound annotation to the ENTRY REFERENCE: Phase B's opening reads the same substrate that Operations Q1 declared, and the annotation at the ENTRY REFERENCE confirms the same binary constraint that the EXIT BLOCK sealed. The three-artifact alignment (COST LEDGER row (a) / Operations Q1 / B2 substrate) makes the manifest self-referential rule a natural close to the phase-boundary architecture.

---

You are running a migration trace signal for: {{topic}}

---

### PARSE PHASE — CONSTRAINT TYPE REGISTRY

Before analysis begins, enumerate every constraint type that the migration touches. Use this exact registry format:

**CONSTRAINT TYPE REGISTRY**

| Constraint Type | Tables Affected | Migration Action | Risk Level |
|-----------------|-----------------|------------------|------------|
| NOT NULL | | | |
| FOREIGN KEY | | | |
| UNIQUE | | | |
| CHECK | | | |

Fill all rows before proceeding. If a constraint type has no affected tables, state "none confirmed" in Tables Affected — do not omit the row. The registry is a pre-commitment: every constraint type listed here must appear in a dedicated analytical field in both Phase A and Phase B. Constraint types not in this registry may not appear in analysis.

---

### PHASE A — SCHEMA SUBSTRATE AND DOMAIN ANALYSIS

**STATUS QUO COST** — establish this section before any per-role analysis begins.

The Status Quo Cost is the cost of not migrating. It is not a migration risk — it is the accumulating damage the existing schema state is already inflicting. Three-part structure, expressed as a COST LEDGER table:

**COST LEDGER**

| Row | Category | Current State | Accumulation Mechanism |
|-----|----------|---------------|----------------------|
| (a) Schema substrate | Name the exact schema condition, migration-state dependency, or infrastructure constraint that is the structural source of the cost. This must be an infrastructure or schema condition — not a business process outcome. | | |
| (b) Dependent process | Name the business process or data flow that is breaking because of row (a). Name the disruption concretely. | | |
| (c) Accumulation | State how the cost in row (b) compounds over time without migration. Name the trajectory (data debt, query degradation, reconciliation overhead, etc.) | | |

**COST LEDGER SUBSTRATE GATE**
Row (a) category check: if row (a) names a business process outcome or financial metric rather than a schema or infrastructure condition, do not proceed to Q1. Return to parse phase, re-examine the constraint type registry, and re-identify the infrastructure substrate. Row (a) must name the structural source, not the downstream symptom.

**ALIGNMENT STATE BINDING**
The infrastructure condition named in COST LEDGER row (a) is the binding substrate for this entire trace. Q1's domain must analyze this same condition class. B2's cross-role chain must cite this same substrate as its shared failure point. Record the substrate class here before proceeding:

> ALIGNMENT STATE substrate: ___________________________
> Binding rule: COST LEDGER row (a), Q1 analysis domain, and B2 chain substrate must name the same infrastructure condition class. Any deviation from this class across the three artifacts constitutes misalignment.

---

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE**

You are the Operations and infrastructure expert. Q1 runs before Commerce and Finance because the schema substrate must be established before domain consequence analysis can proceed. You analyze the migration's effect on the infrastructure layer — not business processes yet.

Analytical checklist (apply to every changed entity in this role's domain):
- Schema state before migration: column types, nullability constraints, index coverage, FK bindings
- Migration action: what the DDL or data script does to this entity
- Schema state after migration: what the entity looks like post-execution
- Data loss path: is there any transformation, truncation, or drop that loses rows or precision?
- Nullable violation: does the migration introduce a NOT NULL constraint on a column with existing nulls?
- Missing default: does the migration remove a default value or introduce a new NOT NULL without a default?
- Performance cliff: does the migration add a full-table scan, disable an index, or break a statistics baseline?
- Rollback path: is the migration reversible? If yes, what does reversal leave behind?

Per-constraint analysis fields (one field per constraint type from the registry; do not combine types):

**NOT NULL ANALYSIS — Q1**
[Constraint type: NOT NULL · Tables: [name affected tables] · Pre-migration state: [describe current nullability] · Migration action: [what the DDL does] · Violation path: [rows that will fail on execution] · Enforcement response: [migration abort / default injection / backfill required]]

**FOREIGN KEY ANALYSIS — Q1**
[Constraint type: FK · Tables: [name parent/child tables] · Pre-migration state: [current referential integrity state] · Migration action: [what changes] · Violation path: [orphan rows, cascade implications] · Enforcement response: [what the migration script does on violation]]

**UNIQUE ANALYSIS — Q1**
[Constraint type: UNIQUE · Tables: [name tables] · Pre-migration state: [current uniqueness state] · Migration action: [what the DDL does] · Violation path: [duplicate rows that will violate] · Enforcement response: [dedup strategy or abort condition]]

**CHECK ANALYSIS — Q1**
[Constraint type: CHECK · Tables: [name tables] · Pre-migration state: [current check condition] · Migration action: [what the DDL does] · Violation path: [rows failing the new check] · Enforcement response: [migration response to violations]]

**Phase A inertia-contrast example (Operations domain):**
Three-part structure: (1) prior working state that depended on the pre-migration schema, (2) how the migration breaks that working state, (3) the concrete consequence in Operations terms. This example must be distinct from the Phase B inertia example — different migration step or different schema entity.

---

**Q2 — COMMERCE ROLE**

You are the Commerce expert. Apply the same analytical checklist and per-constraint analysis fields as Q1, now for the Commerce domain's affected entities (catalog tables, pricing structures, order schema, promotion rules, entitlement records). Name specific tables and columns — do not generalize to "Commerce data."

[Apply full Q1 checklist to Commerce domain entities. Apply all four constraint-type analysis fields. Name specific tables.]

---

**Q3 — FINANCE ROLE**

You are the Finance expert. Apply the same analytical checklist and per-constraint analysis fields, now for Finance domain entities (ledger tables, transaction records, cost center schema, period-end views, audit trail structures). Name specific tables and columns.

[Apply full Q1 checklist to Finance domain entities. Apply all four constraint-type analysis fields. Name specific tables.]

---

**PHASE A CLOSE — BOUNDARY PROTOCOL: PHASE A TO PHASE B**

**EXIT BLOCK — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = [OPEN | CLOSED]
ALIGNMENT STATE = [SATISFIED | MISALIGNED]

Required for Phase B entry:
  PARSE GATE (BINARY FIELD) = OPEN
  ALIGNMENT STATE = SATISFIED

If PARSE GATE (BINARY FIELD) = CLOSED:
  Return to parse phase. Re-examine CONSTRAINT TYPE REGISTRY.
  Do not proceed to Phase B until registry is complete and all
  constraint-type analysis fields are filled.

If ALIGNMENT STATE = MISALIGNED:
  Return to Q1. The infrastructure condition in COST LEDGER row (a)
  and the domain analyzed in Q1 do not name the same substrate class.
  Revise Q1 analysis domain before proceeding.
```

Guard: The EXIT BLOCK must carry the compound type annotation `(BINARY FIELD)` on the PARSE GATE field. A gate state without the type annotation is structurally incomplete — the binary enforcement mechanism is not self-documenting without the compound annotation at the definition site.

---

### PHASE B — SYNTHESIS AND CROSS-ROLE CONSEQUENCES

**ENTRY REFERENCE — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

This ENTRY REFERENCE carries the same compound type annotation as the EXIT BLOCK. A reader consulting only Phase B's opening block must see `PARSE GATE (BINARY FIELD) = OPEN required` — not `PARSE GATE = OPEN required` — to verify the binary constraint without cross-referencing Phase A. Both structural anchors carry the full compound annotation independently.

---

**PROTOCOL COUNT MANIFEST**

All named gates in this trace, enumerated before Phase B analysis begins:

| Gate Name | Block Location | State Required | Blocks Transition? |
|-----------|----------------|----------------|-------------------|
| PARSE GATE (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes — Phase B entry |
| PARSE GATE (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | Phase A-to-B EXIT BLOCK | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**Completeness rule: A gate named in any block but absent from this manifest = incomplete registry. Apply this rule to detect omissions — do not rely on cross-document search.**

---

**B1 — MIGRATION EXECUTION SUMMARY**

Summarize the full migration as a before/after state change. One row per changed entity:

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**B2 — CROSS-ROLE CAUSAL CHAIN**

The Phase B inertia-contrast example must name a cross-role causal chain: a shared infrastructure substrate condition whose disruption produces direct, named consequences in at least two distinct domain roles. Structure:

1. **Shared substrate**: Name the schema state or migration-step dependency that Operations Q1 established as the binding substrate (matching ALIGNMENT STATE substrate declared in Phase A).
2. **Commerce consequence**: Name the specific Commerce domain failure that results when the substrate is violated — name the table, the business process, and the user-visible outcome.
3. **Finance consequence**: Name the specific Finance domain failure from the same substrate violation — name the ledger table, the transaction type, and the reconciliation impact.
4. **Causal link**: State why both consequences follow from the same substrate condition. The substrate must hold for both downstream consequences to be avoidable — demonstrating the substrate failure once demonstrates both failures simultaneously.

This example must be distinct from Q1's Phase A inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

One row per constraint type from the registry. Verify completeness against the PROTOCOL COUNT MANIFEST — every constraint type in the registry must appear as a row:

| Constraint Type | Q1 Finding | Q2 Finding | Q3 Finding | Migration Response | Residual Risk |
|-----------------|-----------|-----------|-----------|-------------------|---------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Residual Risk: risk that remains after migration completes. State NONE CONFIRMED if all instances are addressed.

---

---

## V-02 — Output Format

**Axis:** Output format
**Hypothesis:** Anchoring every structural layer to a named table with explicit fill rules (column schema, row minimums, fill validation) prevents prose collapse and makes C-46 and C-47 compliance structurally natural. When the PROTOCOL COUNT MANIFEST is specified as a table with a required completeness-rule row, C-47 cannot be omitted. When the gate schema is specified at both anchor positions with the `(BINARY FIELD)` token, C-46 compliance is a formatting requirement rather than an aspirational annotation.

---

You are running a migration trace signal for: {{topic}}

---

### PARSE PHASE

**CONSTRAINT TYPE REGISTRY TABLE**

Required before any analysis. Fill all rows. "None" is a valid entry for Tables Affected if the constraint type is confirmed absent.

| ID | Constraint Type | Affected Tables | Migration Action | Risk |
|----|-----------------|-----------------|------------------|------|
| CT-1 | NOT NULL | | | |
| CT-2 | FOREIGN KEY | | | |
| CT-3 | UNIQUE | | | |
| CT-4 | CHECK | | | |

Registry lock: after this table is filled, no constraint type may appear in analysis that is not listed here. No constraint type listed here may be omitted from Phase A per-role analysis or Phase B cross-reference.

---

### PHASE A

**COST LEDGER TABLE** — populate before Q1

| Row | Part | Substrate / Process / Trajectory | Verification |
|-----|------|----------------------------------|-------------|
| (a) | Schema substrate | [name the schema condition, migration-state dependency, or infrastructure constraint — infrastructure class only] | Must be infrastructure/schema class |
| (b) | Dependent process | [name the business process or data flow that breaks because of row (a)] | Must name a specific process |
| (c) | Accumulation | [state how the damage in row (b) compounds — data debt, degradation curve, reconciliation load] | Must name a trajectory |

**COST LEDGER SUBSTRATE GATE TABLE**

| Check | Result | Action if FAIL |
|-------|--------|----------------|
| Row (a) is infrastructure/schema class (not business metric or process outcome) | [PASS / FAIL] | FAIL: return to parse phase, re-identify substrate |

**ALIGNMENT STATE TABLE** — binds three artifacts

| Artifact | Infrastructure Condition Class Named |
|----------|--------------------------------------|
| COST LEDGER row (a) | [fill from Cost Ledger] |
| Phase A Q1 domain | [must match row (a) class] |
| Phase B B2 substrate | [must match row (a) class — pre-commit here] |

Binding rule: all three rows must name the same infrastructure condition class. Record as: `ALIGNMENT STATE = SATISFIED` or `ALIGNMENT STATE = MISALIGNED (deviation: [describe which artifact diverges])`.

---

**Q1 — OPERATIONS ROLE** (analyzes ALIGNMENT STATE substrate from table above)

Per-entity analysis table. One row per changed entity in the Operations/infrastructure domain. Minimum 4 rows.

| Entity | Pre-State | Migration Action | Post-State | Data Loss Path | Nullable Violation | Missing Default | Perf Cliff | Rollback |
|--------|-----------|-----------------|-----------|----------------|-------------------|----------------|------------|---------|

Constraint-type analysis tables (one table per CT-registry entry; do not combine types):

**NOT NULL — Q1 TABLE**
| Table | Column | Pre-Nullability | Migration DDL | Rows at Risk | Enforcement Response |
|-------|--------|-----------------|---------------|--------------|----------------------|

**FOREIGN KEY — Q1 TABLE**
| Parent Table | Child Table | Current FK State | Migration Change | Orphan Risk | Cascade Behavior |
|-------------|------------|-----------------|-----------------|-------------|-----------------|

**UNIQUE — Q1 TABLE**
| Table | Column(s) | Current Uniqueness | Migration Change | Duplicate Risk | Dedup Strategy |
|-------|----------|-------------------|-----------------|----------------|----------------|

**CHECK — Q1 TABLE**
| Table | Column | Current Check | New Check | Rows Failing | Response |
|-------|--------|---------------|-----------|--------------|---------|

**Phase A inertia table — Operations domain** (must be distinct from Phase B inertia example)
| Prior working state | Migration action that breaks it | Concrete consequence |
|--------------------|--------------------------------|---------------------|
| [row 1] | | |

---

**Q2 — COMMERCE ROLE** (same table schemas as Q1, Commerce domain entities)

[Per-entity table. All four constraint-type tables. Phase-specific entities only — no repetition of Q1 entities.]

---

**Q3 — FINANCE ROLE** (same table schemas as Q1, Finance domain entities)

[Per-entity table. All four constraint-type tables. Phase-specific entities only.]

---

**PHASE A-TO-B BOUNDARY PROTOCOL TABLE**

| Field | Value | Annotation |
|-------|-------|------------|
| PARSE GATE | [OPEN \| CLOSED] | (BINARY FIELD) |
| ALIGNMENT STATE | [SATISFIED \| MISALIGNED] | |
| Phase B entry condition | PARSE GATE (BINARY FIELD) = OPEN AND ALIGNMENT STATE = SATISFIED | both conditions required |
| On PARSE GATE CLOSED | Return to parse phase · re-examine CONSTRAINT TYPE REGISTRY · fill any empty registry rows | |
| On ALIGNMENT STATE MISALIGNED | Return to Q1 · align Q1 domain with COST LEDGER row (a) substrate class · re-check B2 pre-commit | |

The `(BINARY FIELD)` annotation in the Annotation column is the compound type annotation for PARSE GATE. It must appear at both anchor positions: this EXIT BLOCK and the Phase B ENTRY REFERENCE table.

---

### PHASE B

**PHASE B ENTRY REFERENCE TABLE** — first block of Phase B, before any analytical content

| Field | Required State | Annotation |
|-------|---------------|------------|
| PARSE GATE | OPEN | (BINARY FIELD) |
| ALIGNMENT STATE | SATISFIED | |

This table is the ENTRY REFERENCE for the Phase A-to-B boundary. The `(BINARY FIELD)` annotation on PARSE GATE is identical to the EXIT BLOCK annotation — the compound type is self-documenting at this position without requiring the EXIT BLOCK to be consulted.

---

**PROTOCOL COUNT MANIFEST TABLE**

All named gates in this trace. Populated at Phase B entry before any B-section analysis.

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|--------------|----|---|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS | Yes — Q1 entry |

**Manifest completeness rule:** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position that is absent from this manifest = incomplete registry. Check this rule against all gate-bearing blocks in this document before proceeding.

---

**B1 — ENTITY STATE TABLE**

| Entity | Pre-Migration State | Migration DDL/Script | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|----------------|

Net Data Effect: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE. Minimum 1 row per domain role (Operations, Commerce, Finance).

---

**B2 — CROSS-ROLE CAUSAL CHAIN TABLE**

| Element | Content |
|---------|---------|
| Shared substrate | [name the infrastructure condition from ALIGNMENT STATE binding — must match COST LEDGER row (a) class] |
| Commerce consequence | [table · process · user-visible outcome when substrate is violated] |
| Finance consequence | [ledger table · transaction type · reconciliation impact when same substrate is violated] |
| Causal link | [why both consequences follow from the same substrate failure] |

The substrate named here must match the ALIGNMENT STATE binding recorded in Phase A.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| CT-ID | Constraint Type | Q1 Summary | Q2 Summary | Q3 Summary | Migration Response | Residual Risk |
|-------|----------------|-----------|-----------|-----------|-------------------|--------------|
| CT-1 | NOT NULL | | | | | |
| CT-2 | FOREIGN KEY | | | | | |
| CT-3 | UNIQUE | | | | | |
| CT-4 | CHECK | | | | | |

Fill all cells. Every CT-registry row must appear. A CT-registry entry with no B3 row = cross-reference gap.

---

---

## V-03 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** Assigning dedicated vocabulary lists and coverage floors per phase prevents phase collapse. The gate chain annotations emerge naturally from the lifecycle framing: each phase boundary is a vocabulary checkpoint, and the BOUNDARY PROTOCOL inherits the lifecycle register. C-46 passes because per-phase vocabulary includes the compound annotation as a named term. C-47 partially passes — the manifest self-referential rule is structurally motivated but not explicitly required by the prompt text (expected PARTIAL).

---

You are running a migration trace signal for: {{topic}}

The trace has two phases separated by a structured gate boundary. Each phase has its own analytical vocabulary and coverage requirements. Do not collapse phases or borrow vocabulary across phase boundaries.

---

### PARSE PHASE

**Parse vocabulary:** constraint registry · schema snapshot · migration manifest · DDL audit · nullability survey · FK map · index baseline · check condition inventory

Before Phase A begins, enumerate every constraint type the migration touches in a named **CONSTRAINT TYPE REGISTRY**. The registry lists: constraint type · affected tables · migration action · risk level. All four standard types (NOT NULL, FK, UNIQUE, CHECK) must appear; state "none confirmed" for absent types. The registry is a binding manifest — constraint types absent from it may not appear in Phase A or Phase B analysis.

---

### PHASE A — BEFORE-STATE AND DOMAIN CONSEQUENCE ANALYSIS

**Phase A vocabulary:** before-state · schema substrate · nullable violation · data loss path · missing default · performance cliff · rollback reversibility · inertia cost · constraint enforcement · domain propagation

**Coverage requirements for Phase A:**
- STATUS QUO COST section must precede Q1
- COST LEDGER must have exactly three filled rows before Q1 begins
- ALIGNMENT STATE binding must be declared before Q1
- Each role section (Q1, Q2, Q3) must include all four constraint-type analysis fields
- Phase A inertia example must be distinct from Phase B inertia example

---

**STATUS QUO COST** — this section precedes Q1 and all per-role analysis

Establish the cost of not migrating before any entity-level analysis begins. The cost is not a future migration risk — it is the present, accumulating damage the current schema state is already imposing.

**COST LEDGER** — three rows, in this order:

| Row | Part | Content |
|-----|------|---------|
| (a) | Schema substrate | Name the exact schema condition, migration-state dependency, or infrastructure constraint that is the structural source of accumulating cost. Infrastructure or schema class only — not a business process outcome. |
| (b) | Dependent process | Name the business process or data pipeline that is degrading because of the substrate condition in row (a). Name the specific disruption. |
| (c) | Accumulation trajectory | State how the damage in row (b) compounds over time without migration: data debt curve, query degradation rate, reconciliation cost growth, or equivalent. |

**COST LEDGER SUBSTRATE GATE** — after table fill, before Q1
If row (a) names a business outcome or financial metric rather than a schema/infrastructure condition: stop. Return to parse phase. Re-examine the constraint type registry and re-identify the structural substrate. Q1 may not begin until row (a) names an infrastructure or schema condition.

**ALIGNMENT STATE** — binding declaration before Q1
The infrastructure condition class named in COST LEDGER row (a) is the binding substrate for this trace. State it here explicitly:
> Binding substrate class: ___________________________
> This class must appear in: Q1 analysis domain · B2 cross-role chain substrate.
> ALIGNMENT STATE = SATISFIED when all three artifacts name the same class.
> ALIGNMENT STATE = MISALIGNED when any artifact diverges.

---

**Q1 — OPERATIONS / INFRASTRUCTURE** (Phase A vocabulary applies; Q1 runs before Q2 and Q3)

Operations analyzes the infrastructure substrate first. Commerce and Finance follow because their domain consequences derive from the substrate state Q1 establishes.

Apply Phase A vocabulary throughout. For each changed entity in the Operations/infrastructure domain:
- Name the entity (table, index, constraint, sequence, or stored procedure)
- Before-state: schema snapshot before migration runs
- Migration action: what the DDL or data script does to this entity
- After-state: schema state post-execution
- Data loss path: any row drop, precision loss, or transformation artifact
- Nullable violation: NOT NULL constraint on a column carrying nulls
- Missing default: NOT NULL introduced without a default on existing rows
- Performance cliff: index disabled, statistics invalidated, full-table scan introduced
- Rollback reversibility: reversible / irreversible / conditional (name the condition)

Apply all four constraint-type analysis fields from the registry. Use fixed vocabulary labels — do not combine types in free-form fields.

**NOT NULL ANALYSIS — Q1**
Constraint type: NOT NULL | Tables: [name] | Pre-state: [nullability] | Migration action: [DDL] | Violation path: [rows at risk] | Response: [abort / backfill / default inject]

**FOREIGN KEY ANALYSIS — Q1**
Constraint type: FK | Parent/child tables: [name] | Pre-state: [referential integrity state] | Migration action: [change] | Orphan risk: [describe] | Cascade response: [behavior]

**UNIQUE ANALYSIS — Q1**
Constraint type: UNIQUE | Tables: [name] | Pre-state: [uniqueness state] | Migration action: [change] | Duplicate risk: [describe] | Dedup strategy: [action]

**CHECK ANALYSIS — Q1**
Constraint type: CHECK | Tables: [name] | Condition: [before / after] | Rows failing new check: [count or description] | Response: [abort / backfill / waiver]

**Phase A inertia example — Operations domain:**
Prior working state: [name the exact schema condition that worked]
Migration break: [what the migration does to it]
Consequence: [concrete Operations-domain outcome]
(This example must be distinct from the Phase B inertia example — different entity or migration step.)

---

**Q2 — COMMERCE** (Phase A vocabulary; apply same checklist and constraint-type fields as Q1, Commerce entities only)

[Per-entity analysis. All four constraint-type analysis fields. Commerce-domain tables and columns only.]

---

**Q3 — FINANCE** (Phase A vocabulary; apply same checklist and constraint-type fields, Finance entities only)

[Per-entity analysis. All four constraint-type analysis fields. Finance-domain tables and columns only.]

---

**PHASE A-TO-B GATE BOUNDARY**

**Phase A vocabulary for boundary block:** EXIT BLOCK · gate state · BINARY FIELD · compound annotation · return path · blocking condition

**EXIT BLOCK — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = [OPEN | CLOSED]
ALIGNMENT STATE = [SATISFIED | MISALIGNED]

Phase B entry requires both conditions OPEN / SATISFIED.

On PARSE GATE (BINARY FIELD) = CLOSED:
  Blocking condition: constraint type registry incomplete or constraint-type
  analysis fields unfilled in one or more role sections.
  Return path: parse phase → re-examine registry → complete unfilled fields.

On ALIGNMENT STATE = MISALIGNED:
  Blocking condition: Q1 analysis domain does not match COST LEDGER row (a)
  infrastructure class, or B2 substrate pre-commitment deviates.
  Return path: Q1 → revise analysis domain → re-confirm B2 pre-commitment.
```

The `(BINARY FIELD)` compound type annotation is the machine-readable enforcement token for this gate. It must appear at both structural anchors of this boundary: this EXIT BLOCK and Phase B's ENTRY REFERENCE opening block. Both anchors carry the full annotation independently — neither requires the other to be interpretable.

---

### PHASE B — SYNTHESIS AND MIGRATION EXECUTION RECORD

**Phase B vocabulary:** after-state · cross-role consequence · substrate chain · migration execution table · constraint cross-reference · residual risk · causal chain · inertia inversion · ENTRY REFERENCE · PROTOCOL COUNT MANIFEST · completeness contract

**Coverage requirements for Phase B:**
- ENTRY REFERENCE block must be the first block of Phase B, before any analytical content
- PROTOCOL COUNT MANIFEST must follow ENTRY REFERENCE immediately
- B1 must name all changed entities with before/after state
- B2 must name a cross-role causal chain with Commerce and Finance consequences
- Phase B inertia example must be distinct from Phase A example
- B3 must include all four constraint types from the registry

---

**ENTRY REFERENCE — PHASE A TO PHASE B** (Phase B vocabulary applies from this point)

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

The `(BINARY FIELD)` annotation at this position is the same compound type annotation carried by the EXIT BLOCK. A reader consulting only this ENTRY REFERENCE block can verify both the gate state requirement and the binary constraint type without cross-referencing Phase A.

---

**PROTOCOL COUNT MANIFEST** — all gates enumerated at Phase B entry, before any B-section analysis

| Gate | Compound Annotation | Location | Required State |
|------|--------------------|----|------|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS |

**Manifest completeness contract:** a gate named in any block of this trace that is absent from this manifest = incomplete registry. This manifest is the single authoritative enumeration of all binary gates in this trace.

---

**B1 — MIGRATION EXECUTION RECORD**

After-state for all changed entities. Phase B vocabulary applies.

| Entity | Domain | Before-State | Migration Executed | After-State | Net Data Effect |
|--------|--------|-------------|-------------------|-------------|----------------|

---

**B2 — CROSS-ROLE CAUSAL CHAIN** (Phase B inertia example)

The causal chain names a shared infrastructure substrate whose disruption produces consequences in at least two distinct domain roles. This is the Phase B inertia example — distinct from the Phase A Operations example.

Infrastructure substrate: [name the substrate — must match ALIGNMENT STATE binding substrate class from Phase A]
Commerce consequence: [what breaks in Commerce when this substrate is violated — table, process, user impact]
Finance consequence: [what breaks in Finance when the same substrate is violated — ledger, transaction, reconciliation impact]
Causal link: [why both consequences trace to the same substrate — the substrate's integrity is a shared dependency for both domain roles]

---

**B3 — CONSTRAINT CROSS-REFERENCE**

| Constraint | Q1 Risk | Q2 Risk | Q3 Risk | Migration Response | Residual Risk |
|-----------|--------|--------|--------|-------------------|--------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Every row from the CONSTRAINT TYPE REGISTRY must appear here. A registry entry absent from this table = cross-reference gap.

---

---

## V-04 — Role Sequence + Phrasing Register

**Axis:** Role sequence + formal/imperative phrasing register
**Hypothesis:** Imperative DIRECTIVE blocks, rather than prose instructions, eliminate ambiguity about annotation requirements. A DIRECTIVE that states "WRITE the compound annotation `(BINARY FIELD)` at the ENTRY REFERENCE position. Do not omit the annotation at this position." creates an unambiguous requirement. Similarly, a DIRECTIVE stating "INCLUDE the self-referential completeness rule in the PROTOCOL COUNT MANIFEST as a named assertion" closes the C-47 gap without relying on model inference. Operations-first role sequence is enforced via DIRECTIVE ordering, not suggestion.

---

You are running a migration trace signal for: {{topic}}

This is a structured, gated, two-phase analysis. Follow each DIRECTIVE exactly. Do not reorder phases or role sections. Do not omit named blocks.

---

### PARSE PHASE DIRECTIVES

**DIRECTIVE P-1:** WRITE a block named CONSTRAINT TYPE REGISTRY before Phase A begins.

CONSTRAINT TYPE REGISTRY format:
- Four rows: NOT NULL · FOREIGN KEY · UNIQUE · CHECK
- Per row: constraint type · affected tables · migration action · risk level
- If no tables are affected for a type: state "none confirmed" — do not omit the row

**DIRECTIVE P-2:** The CONSTRAINT TYPE REGISTRY is a binding manifest. Every type listed must appear in dedicated analysis fields in Phase A Q1, Q2, Q3, and Phase B B3. Types absent from the registry may not appear elsewhere.

---

### PHASE A DIRECTIVES

**DIRECTIVE A-1:** WRITE a block named STATUS QUO COST as the first named section of Phase A, before any role section (Q1, Q2, Q3).

**DIRECTIVE A-2:** Inside STATUS QUO COST, WRITE a COST LEDGER table with exactly three rows:
- Row (a): schema substrate — the structural schema condition or migration-state dependency that is the source of accumulating cost. This row must name an infrastructure or schema condition. Business outcomes or financial metrics are rejected.
- Row (b): dependent process — the specific business process or data pipeline breaking because of row (a).
- Row (c): accumulation trajectory — how the row (b) damage compounds over time.

**DIRECTIVE A-3:** After COST LEDGER, WRITE a COST LEDGER SUBSTRATE GATE block. State: if row (a) names a business outcome rather than a schema condition, return to parse phase. Do not proceed to Q1 until COST LEDGER SUBSTRATE GATE = PASS.

**DIRECTIVE A-4:** After COST LEDGER SUBSTRATE GATE, WRITE an ALIGNMENT STATE BINDING block. State the infrastructure condition class from COST LEDGER row (a) explicitly. State: Q1 domain, B2 substrate, and COST LEDGER row (a) must name the same infrastructure condition class. ALIGNMENT STATE = SATISFIED when this rule holds; ALIGNMENT STATE = MISALIGNED when any artifact deviates.

**DIRECTIVE A-5:** WRITE Q1 as the first role section of Phase A. Q1 role: Operations / infrastructure. Do not begin with Commerce or Finance. Q1 analyzes the infrastructure substrate declared in ALIGNMENT STATE BINDING. Commerce (Q2) and Finance (Q3) follow because their domain consequences derive from the substrate Q1 establishes.

**DIRECTIVE A-6:** In Q1, Q2, and Q3, WRITE four dedicated constraint-type analysis fields, one per registry entry. Use these exact labels:
- NOT NULL ANALYSIS — [ROLE]
- FOREIGN KEY ANALYSIS — [ROLE]
- UNIQUE ANALYSIS — [ROLE]
- CHECK ANALYSIS — [ROLE]

Do not combine constraint types in a shared field. Do not use a free-form CONSTRAINT RISK field as a substitute.

**DIRECTIVE A-7:** In Q1, Q2, and Q3, APPLY this analytical checklist to every changed entity:
1. Before-state: schema snapshot pre-migration
2. Migration action: DDL or data script action
3. After-state: schema state post-execution
4. Data loss path: row drop, precision loss, or transformation artifact
5. Nullable violation: NOT NULL on a column carrying nulls
6. Missing default: NOT NULL introduced without a default
7. Performance cliff: index disabled, statistics invalidated, full-table scan introduced
8. Rollback reversibility: reversible / irreversible / conditional (name condition)

**DIRECTIVE A-8:** Include a Phase A inertia-contrast example inside Q1. Three-part structure: (1) prior working state, (2) migration action that breaks it, (3) concrete Operations-domain consequence. This example must name a different entity or migration step than the Phase B inertia example.

**DIRECTIVE A-9:** WRITE the Phase A-to-B BOUNDARY PROTOCOL as a named block at the close of Phase A. Include an EXIT BLOCK with this exact structure:

```
EXIT BLOCK — PHASE A TO PHASE B

PARSE GATE (BINARY FIELD) = [OPEN | CLOSED]
ALIGNMENT STATE = [SATISFIED | MISALIGNED]

Entry condition for Phase B:
  PARSE GATE (BINARY FIELD) = OPEN
  ALIGNMENT STATE = SATISFIED

On PARSE GATE (BINARY FIELD) = CLOSED:
  Return path: parse phase → complete CONSTRAINT TYPE REGISTRY →
  fill all constraint-type analysis fields in all role sections.

On ALIGNMENT STATE = MISALIGNED:
  Return path: Q1 → align domain with COST LEDGER row (a) class →
  re-confirm B2 substrate pre-commitment.
```

**DIRECTIVE A-10:** The `(BINARY FIELD)` compound annotation on PARSE GATE in the EXIT BLOCK is the type annotation that makes the binary enforcement mechanism self-documenting at the definition site. WRITE this annotation at the EXIT BLOCK position. You will also write it at the ENTRY REFERENCE position in Phase B (DIRECTIVE B-1). Both positions carry the annotation independently.

---

### PHASE B DIRECTIVES

**DIRECTIVE B-1:** WRITE an ENTRY REFERENCE block as the FIRST block of Phase B, before any analytical section (B1, B2, B3). Use this exact structure:

```
ENTRY REFERENCE — PHASE A TO PHASE B

PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

The `(BINARY FIELD)` compound annotation at this position is identical to the EXIT BLOCK annotation. A reader consulting only this ENTRY REFERENCE block must see the compound type annotation to verify the gate condition without consulting the EXIT BLOCK. Do not write `PARSE GATE = OPEN required` at this position — the annotation is not optional at the ENTRY REFERENCE anchor.

**DIRECTIVE B-2:** Immediately after the ENTRY REFERENCE block, WRITE a PROTOCOL COUNT MANIFEST block. This is a named table that enumerates every gate in this trace. Minimum rows:

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|----|---|---|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS | Yes |

**DIRECTIVE B-3:** After the PROTOCOL COUNT MANIFEST table, WRITE this rule as a named assertion:

> **Manifest completeness rule:** A gate named in any EXIT BLOCK, ENTRY REFERENCE, or BOUNDARY PROTOCOL block in this trace that is absent from this manifest = incomplete registry.

This rule is not a comment — it is a structural assertion that defines the condition under which this manifest would be incomplete. It must appear as a named, labeled statement in the PROTOCOL COUNT MANIFEST block.

**DIRECTIVE B-4:** WRITE B1 — MIGRATION EXECUTION RECORD. One row per changed entity: domain · before-state · migration action · after-state · net data effect.

**DIRECTIVE B-5:** WRITE B2 — CROSS-ROLE CAUSAL CHAIN. This is the Phase B inertia example. Name a shared infrastructure substrate condition (matching ALIGNMENT STATE binding substrate) whose failure produces consequences in at least two domain roles. Name: the substrate · the Commerce consequence (table + process + user impact) · the Finance consequence (ledger + transaction + reconciliation impact) · the causal link (why both follow from the same substrate).

**DIRECTIVE B-6:** WRITE B3 — CONSTRAINT CROSS-REFERENCE TABLE. One row per constraint type from the registry: Q1 finding · Q2 finding · Q3 finding · migration response · residual risk. Every registry type must appear. Residual risk = NONE CONFIRMED when migration fully addresses the constraint class.

---

---

## V-05 — Combined: Role Sequence + Output Format + Lifecycle Emphasis

**Axis:** Role sequence + output format + lifecycle emphasis
**Hypothesis:** Full combination creates a self-reinforcing prompt: Operations-first role sequence establishes the infrastructure substrate that the gate chain protects; table-anchored format enforces completeness at every layer; per-phase vocabulary anchors the BOUNDARY PROTOCOL in the lifecycle register. C-46 and C-47 compliance is overdetermined — three independent structural pressures converge on annotation symmetry and manifest completeness. Designed to approach the 285-point ceiling.

---

You are running a migration trace signal for: {{topic}}

Two-phase analysis with per-phase vocabulary, table-anchored output, and a structured gate boundary. Each phase has coverage requirements. Do not collapse phases. Do not combine constraint types in shared fields.

---

### PARSE PHASE

**Parse vocabulary:** constraint registry · schema snapshot · nullability audit · FK map · index baseline · migration manifest · DDL scope

**CONSTRAINT TYPE REGISTRY TABLE** — required before Phase A; fill all rows

| ID | Constraint Type | Affected Tables | Migration DDL Action | Risk Level |
|----|----------------|-----------------|---------------------|------------|
| CT-1 | NOT NULL | | | |
| CT-2 | FOREIGN KEY | | | |
| CT-3 | UNIQUE | | | |
| CT-4 | CHECK | | | |

**Registry lock:** every CT-ID row must appear in Phase A per-role constraint-type tables and Phase B B3 cross-reference table. Absent rows = coverage gap.

---

### PHASE A — BEFORE-STATE AND DOMAIN ANALYSIS

**Phase A vocabulary:** before-state · schema substrate · nullable violation · missing default · data loss path · performance cliff · rollback reversibility · inertia cost · domain propagation · constraint enforcement

**Phase A coverage requirements:**
- STATUS QUO COST section with COST LEDGER (3 rows) before Q1
- ALIGNMENT STATE binding declaration before Q1
- Q1 = Operations (first) · Q2 = Commerce · Q3 = Finance
- All four constraint-type tables in each role section
- Full 8-item analytical checklist per entity in each role section
- Phase A inertia example inside Q1 (distinct entity or step from Phase B example)

---

**STATUS QUO COST SECTION** — before Q1, before any per-entity analysis

**COST LEDGER TABLE**

| Row | Part | Content | Validation |
|-----|------|---------|-----------|
| (a) | Schema substrate | [exact schema condition, migration-state dependency, or infrastructure constraint that is the structural source of accumulating cost — infrastructure/schema class only] | Must not be a business metric or process outcome |
| (b) | Dependent process | [specific business process or data pipeline degrading because of row (a) substrate] | Must name a specific named process |
| (c) | Accumulation trajectory | [how the row (b) damage compounds without migration: data debt, query degradation, reconciliation load growth] | Must name a trajectory class |

**COST LEDGER SUBSTRATE GATE TABLE**

| Gate | Check | Result | On FAIL |
|------|-------|--------|---------|
| COST LEDGER SUBSTRATE GATE | Row (a) names infrastructure/schema condition (not business outcome or financial metric) | [PASS / FAIL] | Return to parse phase · re-examine registry · re-identify substrate |

**ALIGNMENT STATE BINDING TABLE**

| Artifact | Infrastructure Condition Class | Match? |
|----------|-------------------------------|--------|
| COST LEDGER row (a) | [fill from Cost Ledger] | — (reference anchor) |
| Phase A Q1 analysis domain | [must name same class as row (a)] | [YES / NO] |
| Phase B B2 substrate (pre-commit) | [commit to same class now, before Phase A begins] | [YES / NO] |

ALIGNMENT STATE = SATISFIED when all three artifact rows match. ALIGNMENT STATE = MISALIGNED when any row deviates — name the deviating artifact.

---

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE**
Phase A vocabulary applies. Operations runs first because the infrastructure substrate must be established before domain-role consequence analysis can proceed.

**Q1 per-entity analysis table** (Phase A vocabulary; minimum 4 rows; Infrastructure/Operations domain entities only)

| Entity | Before-State | Migration Action | After-State | Data Loss Path | Nullable Violation | Missing Default | Perf Cliff | Rollback |
|--------|-------------|-----------------|-------------|---------------|-------------------|----------------|------------|---------|

**Q1 NOT NULL TABLE** (CT-1)
| Table | Column | Pre-Nullability | Migration DDL | Rows at Risk | Enforcement Response |
|-------|--------|----------------|--------------|-------------|---------------------|

**Q1 FOREIGN KEY TABLE** (CT-2)
| Parent Table | Child Table | Current FK State | Migration Change | Orphan Risk | Cascade Behavior |
|-------------|------------|-----------------|----------------|------------|-----------------|

**Q1 UNIQUE TABLE** (CT-3)
| Table | Column(s) | Current Uniqueness | Migration Change | Duplicate Risk | Dedup Strategy |
|-------|----------|-------------------|----------------|--------------|---------------|

**Q1 CHECK TABLE** (CT-4)
| Table | Column | Current Condition | New Condition | Rows Failing | Response |
|-------|--------|-----------------|--------------|-------------|---------|

**Q1 Phase A inertia table** (distinct entity/step from B2 inertia example)
| Prior working state | Migration break | Operations consequence |
|--------------------|----------------|----------------------|

---

**Q2 — COMMERCE ROLE**
Phase A vocabulary applies. Same table schemas as Q1. Commerce-domain entities only.

[Q2 per-entity table. Q2 NOT NULL table. Q2 FOREIGN KEY table. Q2 UNIQUE table. Q2 CHECK table.]

---

**Q3 — FINANCE ROLE**
Phase A vocabulary applies. Same table schemas as Q1. Finance-domain entities only.

[Q3 per-entity table. Q3 NOT NULL table. Q3 FOREIGN KEY table. Q3 UNIQUE table. Q3 CHECK table.]

---

**PHASE A-TO-B BOUNDARY PROTOCOL BLOCK** — Phase A close

**EXIT BLOCK — PHASE A TO PHASE B**

| Field | Value | Compound Annotation |
|-------|-------|---------------------|
| PARSE GATE | [OPEN \| CLOSED] | (BINARY FIELD) |
| ALIGNMENT STATE | [SATISFIED \| MISALIGNED] | — |
| Phase B entry condition | Both: PARSE GATE (BINARY FIELD) = OPEN and ALIGNMENT STATE = SATISFIED | — |
| On PARSE GATE CLOSED | Return: parse phase → complete registry → fill constraint-type tables in all role sections | — |
| On ALIGNMENT STATE MISALIGNED | Return: Q1 → align domain with row (a) substrate class → re-confirm B2 pre-commitment | — |

The `(BINARY FIELD)` compound annotation is the type annotation for PARSE GATE. It appears at this EXIT BLOCK position and at the Phase B ENTRY REFERENCE position. Both structural anchors carry the full compound annotation — the binary constraint is self-documenting at either position without consulting the other.

---

### PHASE B — SYNTHESIS AND MIGRATION EXECUTION RECORD

**Phase B vocabulary:** after-state · ENTRY REFERENCE · PROTOCOL COUNT MANIFEST · completeness contract · cross-role chain · substrate propagation · constraint resolution · residual risk · migration execution record · inertia inversion

**Phase B coverage requirements:**
- ENTRY REFERENCE table (first block of Phase B, before any analytical content)
- PROTOCOL COUNT MANIFEST with completeness rule (second block)
- B1 entity state table (all changed entities)
- B2 cross-role causal chain (2+ domain roles, shared substrate)
- B3 constraint cross-reference (all CT-IDs from registry)

---

**ENTRY REFERENCE TABLE** — Phase B vocabulary applies from this point

| Field | Required State | Compound Annotation |
|-------|---------------|---------------------|
| PARSE GATE | OPEN | (BINARY FIELD) |
| ALIGNMENT STATE | SATISFIED | — |

The `(BINARY FIELD)` annotation at this ENTRY REFERENCE position is identical to the EXIT BLOCK annotation. A reader verifying this gate without consulting Phase A sees both the required state and the binary constraint type from this position alone.

---

**PROTOCOL COUNT MANIFEST TABLE** — second block of Phase B; all gates enumerated before B1

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|----|---|---|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS | Yes |

**Manifest completeness rule:** A gate named in any EXIT BLOCK, ENTRY REFERENCE, or BOUNDARY PROTOCOL block in this trace that is absent from this manifest = incomplete registry. This rule is a named structural assertion — not a comment — and defines the condition under which this manifest would be incomplete.

---

**B1 — MIGRATION EXECUTION RECORD TABLE**

| Entity | Domain | Before-State | Migration Executed | After-State | Net Data Effect |
|--------|--------|-------------|-------------------|-------------|----------------|

Net Data Effect: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE.
Minimum: 1 Operations row + 1 Commerce row + 1 Finance row.

---

**B2 — CROSS-ROLE CAUSAL CHAIN TABLE**

| Element | Content |
|---------|---------|
| Shared substrate | [infrastructure condition — must match ALIGNMENT STATE binding substrate class from Phase A; same class as COST LEDGER row (a)] |
| Commerce consequence | [specific Commerce table + business process + user-visible failure when substrate is violated] |
| Finance consequence | [specific Finance ledger + transaction type + reconciliation impact when same substrate is violated] |
| Causal link | [why both domain consequences follow from the same substrate failure — substrate integrity is a shared dependency] |

Phase B inertia inversion: state what migration success looks like for each domain role. One row per domain.

| Domain | Pre-migration inertia cost | Post-migration state | Inertia inversion achieved? |
|--------|--------------------------|---------------------|----------------------------|
| Operations | | | |
| Commerce | | | |
| Finance | | | |

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| CT-ID | Constraint Type | Q1 Summary | Q2 Summary | Q3 Summary | Migration Response | Residual Risk |
|-------|----------------|-----------|-----------|-----------|-------------------|--------------|
| CT-1 | NOT NULL | | | | | |
| CT-2 | FOREIGN KEY | | | | | |
| CT-3 | UNIQUE | | | | | |
| CT-4 | CHECK | | | | | |

**Coverage check:** every CT-ID from the CONSTRAINT TYPE REGISTRY must appear as a row. A missing CT-ID = cross-reference gap detectable without reading phase interiors.
