# trace-migration Variate — Round 19
**Date:** 2026-03-15
**Rubric:** v17 (C-48, C-49, C-50 introduced)
**Target criteria:** C-48 (ENTRY REFERENCE inline self-documentation rationale note), C-49 (manifest completeness rule action directive), C-50 (manifest completeness rule enumerated block-type scope)

---

## Round 19 Variation Map

| Variation | Axis | C-48 | C-49 | C-50 | Notes |
|-----------|------|------|------|------|-------|
| V-01 | Role sequence | Expected PASS | Expected PASS | Expected PASS | Operations-as-substrate narrative motivates rationale note organically; three-artifact architecture names its own block types; action directive framed as verification closure |
| V-02 | Output format | Expected PASS | Expected PASS | Expected PASS | ENTRY REFERENCE table gets mandatory "Rationale" row; manifest rule is a pre-formatted fill-complete template with block-type slots and action directive slot |
| V-03 | Phrasing register | Expected PASS | Expected PASS | Expected PASS | DIRECTIVE imperatives make C-48/C-49/C-50 non-optional; each criterion is a named WRITE command with exact required text |
| V-04 | Role sequence + Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | Phase B vocabulary list includes rationale-note terms; coverage floor requires enumerated-scope rule and action directive explicitly |
| V-05 | Role sequence + Output format + Inertia framing | Expected PASS | Expected PASS | Expected PASS | Full combination: inertia framing section given dedicated structural weight; table schemas enforce C-48 as a fill column; manifest rule is over-specified at two sites |

---

## V-01 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Framing Operations as the "substrate declaration" role (Q1) creates a narrative through-line that the ENTRY REFERENCE must honor. When the prompt instructs the model to open Phase B by confirming the same annotation that Operations Q1 first established, the inline rationale note emerges naturally from the substrate continuity requirement: "Phase B inherits the Operations substrate — the annotation here confirms what Q1 declared." The three-artifact alignment architecture (COST LEDGER row (a) / Q1 domain / B2 substrate) naturally names BOUNDARY PROTOCOL blocks, EXIT BLOCK positions, and ENTRY REFERENCE positions as its own structural vocabulary, making the enumerated-scope completeness rule a natural close. The action directive frames the manifest as a verification instrument, not a record.

---

You are running a migration trace signal for: {{topic}}

---

### PARSE PHASE — CONSTRAINT TYPE REGISTRY

Before analysis begins, enumerate every constraint type the migration touches. Use this exact registry format:

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
|-----|----------|---------------|------------------------|
| (a) Schema substrate | Name the exact schema condition, migration-state dependency, or infrastructure constraint that is the structural source of the cost. This must be an infrastructure or schema condition — not a business process outcome. | | |
| (b) Dependent process | Name the business process or data flow that is breaking because of row (a). Name the disruption concretely. | | |
| (c) Accumulation | State how the cost in row (b) compounds over time without migration. Name the trajectory. | | |

**COST LEDGER SUBSTRATE GATE**
Row (a) category check: if row (a) names a business process outcome or financial metric rather than a schema or infrastructure condition, do not proceed to Q1. Return to parse phase, re-examine the constraint type registry, and re-identify the infrastructure substrate. Row (a) must name the structural source, not the downstream symptom.

**ALIGNMENT STATE BINDING**
The infrastructure condition named in COST LEDGER row (a) is the binding substrate for this entire trace. Q1's domain must analyze this same condition class. B2's cross-role chain must cite this same substrate as its shared failure point. Record the substrate class here before proceeding:

> ALIGNMENT STATE substrate: ___________________________
> Binding rule: COST LEDGER row (a), Q1 analysis domain, and B2 chain substrate must name the same infrastructure condition class.

---

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE**

Q1 runs first because it establishes the schema substrate that all domain-role consequence analysis derives from. Operations declares the substrate; Commerce and Finance interpret what breaks when the substrate fails. The COST LEDGER row (a) infrastructure condition class is Q1's declared domain — not a constraint on Q1's scope, but the shared substrate that makes B2's cross-role chain computable.

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
[Constraint type: NOT NULL · Tables: [name affected tables] · Pre-migration state: [current nullability] · Migration action: [DDL] · Violation path: [rows at risk] · Enforcement response: [abort / default injection / backfill required]]

**FOREIGN KEY ANALYSIS — Q1**
[Constraint type: FK · Tables: [parent/child tables] · Pre-migration state: [referential integrity state] · Migration action: [change] · Violation path: [orphan rows, cascade implications] · Enforcement response: [on violation]]

**UNIQUE ANALYSIS — Q1**
[Constraint type: UNIQUE · Tables: [name tables] · Pre-migration state: [uniqueness state] · Migration action: [DDL] · Violation path: [duplicate rows] · Enforcement response: [dedup or abort]]

**CHECK ANALYSIS — Q1**
[Constraint type: CHECK · Tables: [name tables] · Pre-migration state: [current check] · Migration action: [DDL] · Violation path: [rows failing new check] · Enforcement response: [migration response]]

**Phase A inertia-contrast example (Operations domain):**
Three-part structure: (1) prior working state that depended on the pre-migration schema, (2) how the migration breaks that working state, (3) the concrete consequence in Operations terms. This example must be distinct from the Phase B inertia example.

---

**Q2 — COMMERCE ROLE**

You are the Commerce expert. Apply the same analytical checklist and per-constraint analysis fields as Q1, now for the Commerce domain's affected entities (catalog tables, pricing structures, order schema, promotion rules, entitlement records). Name specific tables and columns — do not generalize to "Commerce data."

[Apply full Q1 checklist to Commerce domain entities. Apply all four constraint-type analysis fields.]

---

**Q3 — FINANCE ROLE**

You are the Finance expert. Apply the same analytical checklist and per-constraint analysis fields, now for Finance domain entities (ledger tables, transaction records, cost center schema, period-end views, audit trail structures). Name specific tables and columns.

[Apply full Q1 checklist to Finance domain entities. Apply all four constraint-type analysis fields.]

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
  constraint-type analysis fields are filled in all role sections.

If ALIGNMENT STATE = MISALIGNED:
  Return to Q1. The infrastructure condition in COST LEDGER row (a)
  and the domain analyzed in Q1 do not name the same substrate class.
  Revise Q1 analysis domain and re-confirm B2 substrate pre-commitment.
```

The `(BINARY FIELD)` compound annotation on PARSE GATE is the type annotation that makes the binary enforcement mechanism self-documenting at its definition site. This annotation will also appear at the ENTRY REFERENCE position in Phase B — both structural anchors carry the full annotation independently, so neither position requires the other to be interpretable.

---

### PHASE B — SYNTHESIS AND CROSS-ROLE CONSEQUENCES

**ENTRY REFERENCE — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

This ENTRY REFERENCE is the Phase B opening of the same substrate that Operations Q1 declared. The `(BINARY FIELD)` compound annotation here is not decorative — it is the same annotation the EXIT BLOCK carries, present at this position so that a reader consulting only Phase B's opening block sees the binary constraint type without needing to cross-reference Phase A.

Include an inline note at this position stating the self-documenting property explicitly: that the `(BINARY FIELD)` annotation on PARSE GATE makes the gate condition interpretable at this ENTRY REFERENCE position without consulting the EXIT BLOCK. The note confirms what a Phase-B-only reader needs to know: both the required state (OPEN) and the binary constraint type are present here, independently of their Phase A definition.

---

**PROTOCOL COUNT MANIFEST**

All named gates in this trace, enumerated at Phase B entry before any analytical content:

| Gate Name | Block Location | State Required | Blocks Transition? |
|-----------|----------------|----------------|-------------------|
| PARSE GATE (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes — Phase B entry |
| PARSE GATE (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | Phase A-to-B EXIT BLOCK | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**Completeness rule:** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK position, or ENTRY REFERENCE position in this trace that is absent from this manifest = incomplete registry. Apply this rule to detect omissions — do not rely on cross-document search to verify gate coverage.

---

**B1 — MIGRATION EXECUTION SUMMARY**

One row per changed entity:

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**B2 — CROSS-ROLE CAUSAL CHAIN**

The Phase B inertia-contrast example must name a cross-role causal chain: a shared infrastructure substrate condition (the same class declared in ALIGNMENT STATE BINDING) whose disruption produces direct, named consequences in at least two distinct domain roles.

1. **Shared substrate**: Name the schema state or migration-step dependency that Operations Q1 established (must match ALIGNMENT STATE substrate class).
2. **Commerce consequence**: Name the specific Commerce domain failure — table, business process, user-visible outcome.
3. **Finance consequence**: Name the specific Finance domain failure — ledger table, transaction type, reconciliation impact.
4. **Causal link**: State why both consequences follow from the same substrate condition. Both domain failures are avoidable only if the substrate holds.

This example must be distinct from Q1's Phase A inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| Constraint Type | Q1 Finding | Q2 Finding | Q3 Finding | Migration Response | Residual Risk |
|-----------------|-----------|-----------|-----------|-------------------|---------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Every constraint type from the registry must appear as a row. A registry type absent from this table = cross-reference gap. Residual Risk: state NONE CONFIRMED if all instances are addressed by the migration.

---

---

## V-02 — Output Format

**Axis:** Output format
**Hypothesis:** Encoding C-48/C-49/C-50 as table fill requirements makes compliance structural rather than aspirational. The ENTRY REFERENCE section becomes a two-part block: a gate state table and a mandatory rationale row. The PROTOCOL COUNT MANIFEST becomes a table with an explicit "Completeness Rule" section whose template pre-formats the enumerated-scope and action-directive requirements as fill slots. A model filling in the template produces a C-49 and C-50 compliant rule automatically.

---

You are running a migration trace signal for: {{topic}}

---

### PARSE PHASE

**CONSTRAINT TYPE REGISTRY TABLE**

Required before any analysis. Fill all rows. "None confirmed" is valid for absent types — do not omit rows.

| ID | Constraint Type | Affected Tables | Migration Action | Risk Level |
|----|-----------------|-----------------|------------------|------------|
| CT-1 | NOT NULL | | | |
| CT-2 | FOREIGN KEY | | | |
| CT-3 | UNIQUE | | | |
| CT-4 | CHECK | | | |

Registry lock: no constraint type may appear in Phase A or Phase B analysis unless listed here. Every listed type must appear in per-role constraint-type tables and in B3.

---

### PHASE A

**COST LEDGER TABLE** — populate before Q1

| Row | Part | Content | Validation |
|-----|------|---------|-----------|
| (a) | Schema substrate | [name the exact schema condition, migration-state dependency, or infrastructure constraint — infrastructure/schema class only] | Must be infrastructure/schema class, not business metric |
| (b) | Dependent process | [name the specific business process or data flow degrading because of row (a)] | Must name a specific process |
| (c) | Accumulation | [state how the damage in row (b) compounds: data debt, query degradation, reconciliation load] | Must name a trajectory |

**COST LEDGER SUBSTRATE GATE TABLE**

| Check | Result | Action on FAIL |
|-------|--------|----------------|
| Row (a) is infrastructure/schema class (not business metric or process outcome) | [PASS / FAIL] | FAIL: return to parse phase, re-identify substrate |

**ALIGNMENT STATE TABLE** — binds three artifacts before Q1

| Artifact | Infrastructure Condition Class Named | Match to Row (a)? |
|----------|--------------------------------------|-------------------|
| COST LEDGER row (a) | [fill from Cost Ledger] | — (reference anchor) |
| Phase A Q1 analysis domain | [must match row (a) class] | [YES / NO] |
| Phase B B2 substrate (pre-commit) | [commit to same class now] | [YES / NO] |

ALIGNMENT STATE = SATISFIED when all three rows agree. ALIGNMENT STATE = MISALIGNED when any row deviates — name the deviating artifact.

---

**Q1 — OPERATIONS ROLE** (analyzes ALIGNMENT STATE substrate; runs before Q2 and Q3)

**Q1 per-entity analysis table** (minimum 4 rows; Operations/infrastructure domain entities only)

| Entity | Pre-State | Migration Action | Post-State | Data Loss Path | Nullable Violation | Missing Default | Perf Cliff | Rollback |
|--------|-----------|-----------------|-----------|----------------|-------------------|----------------|------------|---------|

**NOT NULL — Q1 TABLE** (CT-1)
| Table | Column | Pre-Nullability | Migration DDL | Rows at Risk | Enforcement Response |
|-------|--------|-----------------|---------------|--------------|----------------------|

**FOREIGN KEY — Q1 TABLE** (CT-2)
| Parent Table | Child Table | Current FK State | Migration Change | Orphan Risk | Cascade Behavior |
|-------------|------------|-----------------|-----------------|-------------|-----------------|

**UNIQUE — Q1 TABLE** (CT-3)
| Table | Column(s) | Current Uniqueness | Migration Change | Duplicate Risk | Dedup Strategy |
|-------|----------|-------------------|-----------------|----------------|----------------|

**CHECK — Q1 TABLE** (CT-4)
| Table | Column | Current Check Condition | New Check Condition | Rows Failing | Response |
|-------|--------|------------------------|---------------------|--------------|---------|

**Phase A inertia table — Operations domain** (must be distinct entity/step from Phase B inertia example)
| Prior working state | Migration action that breaks it | Concrete Operations consequence |
|--------------------|--------------------------------|---------------------------------|

---

**Q2 — COMMERCE ROLE** (same table schemas as Q1; Commerce domain entities only)

[Per-entity table · CT-1 table · CT-2 table · CT-3 table · CT-4 table · Commerce domain entities only]

---

**Q3 — FINANCE ROLE** (same table schemas as Q1; Finance domain entities only)

[Per-entity table · CT-1 table · CT-2 table · CT-3 table · CT-4 table · Finance domain entities only]

---

**PHASE A-TO-B BOUNDARY PROTOCOL TABLE**

| Field | Value | Annotation |
|-------|-------|------------|
| PARSE GATE | [OPEN \| CLOSED] | (BINARY FIELD) |
| ALIGNMENT STATE | [SATISFIED \| MISALIGNED] | — |
| Phase B entry condition | PARSE GATE (BINARY FIELD) = OPEN AND ALIGNMENT STATE = SATISFIED | both conditions required |
| On PARSE GATE CLOSED | Return to parse phase · complete registry · fill all constraint-type tables in all role sections | — |
| On ALIGNMENT STATE MISALIGNED | Return to Q1 · align domain with COST LEDGER row (a) substrate class · re-confirm B2 pre-commitment | — |

The `(BINARY FIELD)` annotation in the Annotation column is the compound type annotation for PARSE GATE at this EXIT BLOCK position. It appears identically at the ENTRY REFERENCE position in Phase B — both structural anchors carry it independently.

---

### PHASE B

**PHASE B ENTRY REFERENCE TABLE** — first block of Phase B; before all analytical content

| Field | Required State | Annotation |
|-------|---------------|------------|
| PARSE GATE | OPEN | (BINARY FIELD) |
| ALIGNMENT STATE | SATISFIED | — |

**ENTRY REFERENCE RATIONALE ROW** — required immediately below the gate state table above

| Property | Statement |
|----------|-----------|
| Self-documenting annotation | [State why the `(BINARY FIELD)` annotation is present at this position: that the compound type makes the gate condition interpretable at this ENTRY REFERENCE without consulting the EXIT BLOCK. A reader consulting only this block sees both the required state and the binary constraint type independently.] |

Fill the Statement column with language that names the self-documenting property explicitly. Do not leave this row blank or filled with a placeholder.

---

**PROTOCOL COUNT MANIFEST TABLE** — second block of Phase B; before B1

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|----|---|---|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS | Yes |

**MANIFEST COMPLETENESS RULE TABLE** — required section, immediately below the manifest gate table

| Rule element | Required content |
|-------------|-----------------|
| Scope (enumerate block types) | A gate named in any [fill: name the three block types — BOUNDARY PROTOCOL blocks · EXIT BLOCK positions · ENTRY REFERENCE positions] that is absent from this manifest = incomplete registry |
| Action directive | [fill: a positive instruction to apply the rule, a negative prohibition, or both — e.g., "Apply this rule to detect omissions" or "do not rely on cross-document search"] |

Fill both rows. A scope cell that uses "any block" without naming the three block types = incomplete. An action-directive cell that is empty = rule not operationalized.

---

**B1 — ENTITY STATE TABLE**

| Entity | Domain | Pre-Migration State | Migration DDL/Script | Post-Migration State | Net Data Effect |
|--------|--------|--------------------|--------------------|---------------------|----------------|

Net Data Effect: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE. Minimum 1 row per domain role (Operations, Commerce, Finance).

---

**B2 — CROSS-ROLE CAUSAL CHAIN TABLE**

| Element | Content |
|---------|---------|
| Shared substrate | [infrastructure condition from ALIGNMENT STATE binding — must match COST LEDGER row (a) class] |
| Commerce consequence | [table · process · user-visible outcome when substrate is violated] |
| Finance consequence | [ledger table · transaction type · reconciliation impact when same substrate is violated] |
| Causal link | [why both consequences follow from the same substrate failure] |

The substrate named here must match the ALIGNMENT STATE binding from Phase A. This is the Phase B inertia example — distinct from the Phase A Operations inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| CT-ID | Constraint Type | Q1 Summary | Q2 Summary | Q3 Summary | Migration Response | Residual Risk |
|-------|----------------|-----------|-----------|-----------|-------------------|--------------|
| CT-1 | NOT NULL | | | | | |
| CT-2 | FOREIGN KEY | | | | | |
| CT-3 | UNIQUE | | | | | |
| CT-4 | CHECK | | | | | |

All CT-IDs from the registry must appear. A registry entry absent from B3 = cross-reference gap.

---

---

## V-03 — Phrasing Register

**Axis:** Phrasing register (formal/imperative DIRECTIVE blocks)
**Hypothesis:** Naming C-48/C-49/C-50 as explicit WRITE commands eliminates the model's discretion over whether to include the rationale note or the action directive. A DIRECTIVE that says "WRITE an inline rationale note at the ENTRY REFERENCE position stating the self-documenting property" closes C-48 with the same force as a syntax requirement. Similarly, a DIRECTIVE that specifies the exact form of the completeness rule — including enumerated block types and action directive text — closes C-49 and C-50 without relying on model inference about what "best practice" looks like.

---

You are running a migration trace signal for: {{topic}}

This is a structured, gated, two-phase analysis. Execute each DIRECTIVE exactly. Do not reorder phases or sections. Do not omit named blocks.

---

### PARSE PHASE DIRECTIVES

**DIRECTIVE P-1:** WRITE a block named CONSTRAINT TYPE REGISTRY before Phase A begins. Format: four rows, one per constraint type (NOT NULL · FK · UNIQUE · CHECK). Per row: constraint type · affected tables · migration action · risk level. If a constraint type has no affected tables, write "none confirmed" in Tables Affected — do not omit the row.

**DIRECTIVE P-2:** The CONSTRAINT TYPE REGISTRY is binding. Every type listed must appear in dedicated analysis fields in Phase A Q1, Q2, and Q3, and in Phase B B3. Types absent from the registry may not appear in analysis.

---

### PHASE A DIRECTIVES

**DIRECTIVE A-1:** WRITE a section named STATUS QUO COST as the first section of Phase A, before any role section.

**DIRECTIVE A-2:** Inside STATUS QUO COST, WRITE a COST LEDGER table with exactly three rows:
- Row (a): schema substrate — the exact infrastructure or schema condition that is the structural source of accumulating cost. Infrastructure or schema class only — not a business outcome.
- Row (b): dependent process — the specific business process or data pipeline breaking because of row (a).
- Row (c): accumulation trajectory — how the row (b) damage compounds over time without migration.

**DIRECTIVE A-3:** After COST LEDGER, WRITE a COST LEDGER SUBSTRATE GATE block. State: if row (a) names a business outcome rather than a schema condition, return to parse phase. Q1 may not begin until COST LEDGER SUBSTRATE GATE = PASS.

**DIRECTIVE A-4:** After COST LEDGER SUBSTRATE GATE, WRITE an ALIGNMENT STATE BINDING block. State the infrastructure condition class from COST LEDGER row (a) explicitly. State the binding rule: Q1 domain, B2 chain substrate, and COST LEDGER row (a) must name the same infrastructure condition class. ALIGNMENT STATE = SATISFIED when the rule holds; ALIGNMENT STATE = MISALIGNED when any artifact deviates.

**DIRECTIVE A-5:** WRITE Q1 as the first role section. Q1 role: Operations / infrastructure. Do not begin Phase A with Commerce or Finance. Q1 establishes the schema substrate; Q2 (Commerce) and Q3 (Finance) analyze domain consequences that derive from the substrate Q1 declares.

**DIRECTIVE A-6:** In Q1, Q2, and Q3, WRITE four dedicated constraint-type analysis fields, one per registry type. Use these exact labels: NOT NULL ANALYSIS — [ROLE] · FOREIGN KEY ANALYSIS — [ROLE] · UNIQUE ANALYSIS — [ROLE] · CHECK ANALYSIS — [ROLE]. Do not combine constraint types in a shared field.

**DIRECTIVE A-7:** In Q1, Q2, and Q3, apply this analytical checklist to every changed entity: before-state · migration action · after-state · data loss path · nullable violation · missing default · performance cliff · rollback reversibility.

**DIRECTIVE A-8:** WRITE a Phase A inertia-contrast example inside Q1. Three-part structure: prior working state + migration action that breaks it + concrete Operations-domain consequence. This example must name a different entity or migration step than the Phase B inertia example.

**DIRECTIVE A-9:** WRITE the Phase A-to-B BOUNDARY PROTOCOL as a named block at Phase A close. Include an EXIT BLOCK with this exact structure:

```
EXIT BLOCK — PHASE A TO PHASE B

PARSE GATE (BINARY FIELD) = [OPEN | CLOSED]
ALIGNMENT STATE = [SATISFIED | MISALIGNED]

Entry condition for Phase B:
  PARSE GATE (BINARY FIELD) = OPEN
  ALIGNMENT STATE = SATISFIED

On PARSE GATE (BINARY FIELD) = CLOSED:
  Return path: parse phase -> complete CONSTRAINT TYPE REGISTRY ->
  fill all constraint-type analysis fields in all role sections.

On ALIGNMENT STATE = MISALIGNED:
  Return path: Q1 -> align domain with COST LEDGER row (a) class ->
  re-confirm B2 substrate pre-commitment.
```

**DIRECTIVE A-10:** The `(BINARY FIELD)` compound annotation on PARSE GATE in the EXIT BLOCK is the type annotation for the binary gate. WRITE this annotation at the EXIT BLOCK position. Per DIRECTIVE B-1, you will also write it at the ENTRY REFERENCE position. Both positions carry the annotation independently.

---

### PHASE B DIRECTIVES

**DIRECTIVE B-1:** WRITE an ENTRY REFERENCE block as the FIRST block of Phase B, before any analytical section. Use this gate structure:

```
ENTRY REFERENCE — PHASE A TO PHASE B

PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

Do not write `PARSE GATE = OPEN required` at this position — the `(BINARY FIELD)` annotation is required at the ENTRY REFERENCE anchor, not only at the EXIT BLOCK.

**DIRECTIVE B-1a:** Immediately after the ENTRY REFERENCE gate block, WRITE an inline rationale note. The note must state the self-documenting property of the annotation at this position: that the `(BINARY FIELD)` compound annotation makes the gate condition interpretable here without consulting the EXIT BLOCK. The note may take either of these forms (or equivalent language that names the same property):

- *"A reader consulting only this ENTRY REFERENCE block must see `PARSE GATE (BINARY FIELD) = OPEN required` — the compound type annotation makes the binary constraint self-documenting at this position without requiring Phase A's EXIT BLOCK to be consulted."*
- *"The `(BINARY FIELD)` annotation on PARSE GATE is identical to the EXIT BLOCK annotation — the compound type is self-documenting at this ENTRY REFERENCE position without requiring the EXIT BLOCK to be read."*

Do not omit this note. An ENTRY REFERENCE block that carries the annotation but contains no inline rationale statement is structurally incomplete under this protocol.

**DIRECTIVE B-2:** Immediately after the ENTRY REFERENCE block and its rationale note, WRITE a PROTOCOL COUNT MANIFEST block. This is a named table enumerating every gate in this trace. Minimum rows:

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|----|---|---|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS | Yes |

**DIRECTIVE B-3:** After the PROTOCOL COUNT MANIFEST table, WRITE the manifest completeness rule as a named labeled assertion using this exact form:

> **Manifest completeness rule:** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK position, or ENTRY REFERENCE position in this trace that is absent from this manifest = incomplete registry. Apply this rule to detect omissions — do not rely on cross-document search to verify gate coverage.

Do not use "any block" as the scope term — the rule must enumerate the three block types. Do not omit the action directive after the rule statement. The rule is not a comment — it is a structural assertion that defines the condition under which this manifest would be incomplete and specifies how the assertion is to be applied.

**DIRECTIVE B-4:** WRITE B1 — MIGRATION EXECUTION RECORD. One row per changed entity: domain · before-state · migration action · after-state · net data effect (NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE).

**DIRECTIVE B-5:** WRITE B2 — CROSS-ROLE CAUSAL CHAIN. This is the Phase B inertia-contrast example. Name a shared infrastructure substrate (matching ALIGNMENT STATE binding substrate class from Phase A) whose failure produces named consequences in at least two distinct domain roles. Structure: shared substrate · Commerce consequence (table + process + user impact) · Finance consequence (ledger + transaction + reconciliation impact) · causal link (why both follow from the same substrate). Distinct from the Phase A inertia example.

**DIRECTIVE B-6:** WRITE B3 — CONSTRAINT CROSS-REFERENCE TABLE. One row per constraint type from the registry: Q1 finding · Q2 finding · Q3 finding · migration response · residual risk. Every registry type must appear. Residual risk = NONE CONFIRMED when migration fully addresses the constraint class.

---

---

## V-04 — Role Sequence + Lifecycle Emphasis

**Axis:** Role sequence + lifecycle emphasis
**Hypothesis:** Combining Operations-first role sequencing with per-phase vocabulary lists that explicitly include C-48/C-49/C-50 target terms creates two independent structural pressures for compliance. The Phase B vocabulary list names "self-documenting annotation rationale" and "block-type enumeration" and "operationalized completeness rule" as required terms — making omission of the rationale note or an under-specified completeness rule a vocabulary violation, not just a structural gap. Coverage floors that explicitly name the rationale note and enumerated-scope rule as required items remove inference from the compliance path.

---

You are running a migration trace signal for: {{topic}}

The trace has two phases separated by a structured gate boundary. Each phase has its own analytical vocabulary and coverage requirements. Do not collapse phases or borrow vocabulary across phase boundaries. Do not omit named blocks.

---

### PARSE PHASE

**Parse vocabulary:** constraint registry · schema snapshot · migration manifest · DDL audit · nullability survey · FK map · index baseline · check condition inventory

Before Phase A begins, enumerate every constraint type the migration touches in a named **CONSTRAINT TYPE REGISTRY**. The registry lists: constraint type · affected tables · migration action · risk level. All four standard types (NOT NULL, FK, UNIQUE, CHECK) must appear; state "none confirmed" for absent types. The registry is a binding manifest — constraint types absent from it may not appear in Phase A or Phase B analysis.

---

### PHASE A — BEFORE-STATE AND DOMAIN CONSEQUENCE ANALYSIS

**Phase A vocabulary:** before-state · schema substrate · nullable violation · data loss path · missing default · performance cliff · rollback reversibility · inertia cost · constraint enforcement · domain propagation · infrastructure substrate declaration

**Phase A coverage requirements:**
- STATUS QUO COST section with COST LEDGER (3 rows) before Q1
- COST LEDGER SUBSTRATE GATE after COST LEDGER
- ALIGNMENT STATE binding declaration after COST LEDGER SUBSTRATE GATE, before Q1
- Q1 = Operations (first — declares schema substrate) · Q2 = Commerce · Q3 = Finance
- All four constraint-type analysis fields in each role section
- Full 8-item analytical checklist per changed entity in each role section
- Phase A inertia-contrast example inside Q1 (distinct entity or step from Phase B example)

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
The infrastructure condition class named in COST LEDGER row (a) is the binding substrate for this trace. State it explicitly:
> Binding substrate class: ___________________________
> This class must appear in: Q1 analysis domain · B2 cross-role chain substrate.
> ALIGNMENT STATE = SATISFIED when all three artifacts name the same class.
> ALIGNMENT STATE = MISALIGNED when any artifact diverges.

---

**Q1 — OPERATIONS / INFRASTRUCTURE** (Phase A vocabulary; Q1 runs before Q2 and Q3 because the substrate must be declared before domain consequences can be analyzed)

Operations declares the infrastructure substrate condition class that B2's cross-role chain will cite. Commerce and Finance analyze domain consequences that derive from the substrate Q1 establishes.

Apply Phase A vocabulary throughout. For each changed entity in the Operations/infrastructure domain: before-state · migration action · after-state · data loss path · nullable violation · missing default · performance cliff · rollback reversibility.

Apply all four constraint-type analysis fields from the registry. Use fixed vocabulary labels:

**NOT NULL ANALYSIS — Q1**
Constraint type: NOT NULL | Tables: [name] | Pre-state: [nullability] | Migration action: [DDL] | Violation path: [rows at risk] | Response: [abort / backfill / default inject]

**FOREIGN KEY ANALYSIS — Q1**
Constraint type: FK | Parent/child tables: [name] | Pre-state: [referential integrity state] | Migration action: [change] | Orphan risk: [describe] | Cascade response: [behavior]

**UNIQUE ANALYSIS — Q1**
Constraint type: UNIQUE | Tables: [name] | Pre-state: [uniqueness state] | Migration action: [change] | Duplicate risk: [describe] | Dedup strategy: [action]

**CHECK ANALYSIS — Q1**
Constraint type: CHECK | Tables: [name] | Condition: [before / after] | Rows failing new check: [count or description] | Response: [abort / backfill / waiver]

**Phase A inertia-contrast example — Operations domain:**
Prior working state: [name the schema condition that worked before the migration]
Migration break: [what the migration does to it]
Operations consequence: [concrete operational outcome]
(This example must be distinct from the Phase B inertia example — different entity or migration step.)

---

**Q2 — COMMERCE** (Phase A vocabulary; same checklist and constraint-type fields as Q1; Commerce domain entities only)

[Per-entity analysis · all four constraint-type analysis fields · Commerce tables and columns only]

---

**Q3 — FINANCE** (Phase A vocabulary; same checklist and constraint-type fields; Finance domain entities only)

[Per-entity analysis · all four constraint-type analysis fields · Finance tables and columns only]

---

**PHASE A-TO-B GATE BOUNDARY**

**Phase A boundary vocabulary:** EXIT BLOCK · gate state · BINARY FIELD · compound annotation · return path · blocking condition

**EXIT BLOCK — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = [OPEN | CLOSED]
ALIGNMENT STATE = [SATISFIED | MISALIGNED]

Phase B entry requires: PARSE GATE (BINARY FIELD) = OPEN AND ALIGNMENT STATE = SATISFIED.

On PARSE GATE (BINARY FIELD) = CLOSED:
  Blocking condition: CONSTRAINT TYPE REGISTRY incomplete or
  constraint-type analysis fields unfilled in one or more role sections.
  Return path: parse phase -> re-examine registry -> complete unfilled fields.

On ALIGNMENT STATE = MISALIGNED:
  Blocking condition: Q1 analysis domain does not match COST LEDGER row (a)
  infrastructure class, or B2 substrate pre-commitment deviates.
  Return path: Q1 -> revise analysis domain -> re-confirm B2 pre-commitment.
```

The `(BINARY FIELD)` compound annotation is the machine-readable enforcement token for this gate. It appears at both structural anchors of this boundary: this EXIT BLOCK and Phase B's ENTRY REFERENCE. Both anchors carry the full annotation independently — neither requires the other to be interpretable.

---

### PHASE B — SYNTHESIS AND MIGRATION EXECUTION RECORD

**Phase B vocabulary:** after-state · cross-role consequence · substrate chain · migration execution table · constraint cross-reference · residual risk · causal chain · inertia inversion · ENTRY REFERENCE · self-documenting annotation rationale · PROTOCOL COUNT MANIFEST · block-type enumeration · operationalized completeness rule · action directive

**Phase B coverage requirements:**
- ENTRY REFERENCE block as the first named block of Phase B (before any analytical content)
- ENTRY REFERENCE must include an inline rationale note naming the self-documenting property: that the `(BINARY FIELD)` annotation at this position makes the gate condition interpretable without consulting the EXIT BLOCK — Phase B vocabulary term: "self-documenting annotation rationale"
- PROTOCOL COUNT MANIFEST immediately after ENTRY REFERENCE (before B1)
- Manifest completeness rule must enumerate the three block types: BOUNDARY PROTOCOL blocks · EXIT BLOCK positions · ENTRY REFERENCE positions — Phase B vocabulary term: "block-type enumeration"
- Manifest completeness rule must include an action directive instructing the evaluator to apply the rule — Phase B vocabulary term: "operationalized completeness rule / action directive"
- B1: all changed entities with before/after state
- B2: cross-role causal chain with at least two domain roles and shared substrate matching ALIGNMENT STATE binding
- Phase B inertia example (B2) distinct from Phase A inertia example
- B3: all four constraint types from registry

---

**ENTRY REFERENCE — PHASE A TO PHASE B** (Phase B vocabulary applies from this point)

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

Self-documenting annotation rationale (required inline note — Phase B coverage requirement): The `(BINARY FIELD)` annotation on PARSE GATE at this ENTRY REFERENCE position carries the same compound type annotation as the EXIT BLOCK. A reader consulting only this block sees both the required state and the binary constraint type without consulting Phase A — the annotation is self-documenting at this position independently of the EXIT BLOCK.

---

**PROTOCOL COUNT MANIFEST** — immediately after ENTRY REFERENCE; before B1

| Gate | Compound Annotation | Block Location | Required State | Blocks Transition? |
|------|--------------------|----|---|---|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS | Yes |

**Operationalized completeness rule (block-type enumeration + action directive required):** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK position, or ENTRY REFERENCE position in this trace that is absent from this manifest = incomplete registry. Apply this rule to detect omissions before proceeding to B1 — do not rely on cross-document search to verify gate coverage.

---

**B1 — MIGRATION EXECUTION RECORD**

| Entity | Domain | Before-State | Migration Executed | After-State | Net Data Effect |
|--------|--------|-------------|-------------------|-------------|----------------|

---

**B2 — CROSS-ROLE CAUSAL CHAIN** (Phase B inertia-contrast example; distinct from Phase A inertia example)

Infrastructure substrate: [name the substrate — must match ALIGNMENT STATE binding substrate class declared in Phase A]
Commerce consequence: [what breaks in Commerce when this substrate is violated — table · process · user impact]
Finance consequence: [what breaks in Finance when the same substrate is violated — ledger · transaction · reconciliation impact]
Causal link: [why both consequences trace to the same substrate failure]

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| Constraint Type | Q1 Risk | Q2 Risk | Q3 Risk | Migration Response | Residual Risk |
|----------------|--------|--------|--------|-------------------|--------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Every row from the CONSTRAINT TYPE REGISTRY must appear. A registry entry absent from B3 = cross-reference gap.

---

---

## V-05 — Role Sequence + Output Format + Inertia Framing

**Axis:** Role sequence + output format + inertia framing
**Hypothesis:** A full combination that adds inertia framing as an independent axis. The status quo cost is given a dedicated structural section before the registry — framing the migration decision as a cost-of-inaction problem before analysis begins. Table schemas enforce C-48 as a mandatory fill column in the ENTRY REFERENCE. The manifest completeness rule is over-specified at two sites: once as a fill-template in the PROTOCOL COUNT MANIFEST TABLE section (forcing block-type enumeration), and once as an ACTION REQUIRED note (forcing the action directive). The Operations-first role sequence preserves three-artifact alignment. Designed to approach the v17 ceiling across all new criteria.

---

You are running a migration trace signal for: {{topic}}

Two-phase analysis. The decision to migrate is a cost problem before it is a schema problem. Establish the cost of not migrating before enumeration or analysis begins. Then proceed through a structured gate boundary. Table-anchored output throughout. Each phase has coverage requirements.

---

### PRE-ANALYSIS — STATUS QUO COST FRAME

Before any constraint enumeration or schema analysis begins, establish the cost of inaction.

The status quo is not neutral. Every day the migration does not run, a structural schema condition is compounding a cost: a process is degrading, a data pipeline is accumulating debt, a query plan is worsening. The migration is not just a technical event — it is the termination of an ongoing cost. Name that cost before naming any constraint or schema entity.

**STATUS QUO COST FRAME TABLE**

| Dimension | Content |
|-----------|---------|
| Who is losing | [name the stakeholder(s) currently absorbing the cost — Operations team, Commerce workflow, Finance reconciliation cycle] |
| What the schema is doing to them | [name the exact infrastructure or schema condition that is inflicting the cost — infrastructure/schema class only] |
| How fast it accumulates | [state the compounding mechanism: data debt rate, query degradation slope, reconciliation cycle growth] |
| What migration terminates | [state what the migration ends — not what it adds, but what ongoing damage it stops] |

This frame is not the COST LEDGER — it is the narrative motivation that precedes it. The COST LEDGER (in Phase A) will formalize this frame as a structured three-row table.

---

### PARSE PHASE

**Parse vocabulary:** constraint registry · schema snapshot · migration manifest · DDL scope · nullability audit · FK map · index baseline

**CONSTRAINT TYPE REGISTRY TABLE** — required before Phase A; fill all rows

| ID | Constraint Type | Affected Tables | Migration DDL Action | Risk Level |
|----|----------------|-----------------|---------------------|------------|
| CT-1 | NOT NULL | | | |
| CT-2 | FOREIGN KEY | | | |
| CT-3 | UNIQUE | | | |
| CT-4 | CHECK | | | |

**Registry lock:** every CT-ID must appear in Phase A per-role constraint-type tables and in Phase B B3. An absent CT-ID row = coverage gap. Constraint types not listed here may not appear in analysis.

---

### PHASE A — BEFORE-STATE AND DOMAIN ANALYSIS

**Phase A coverage requirements:**
- COST LEDGER table (3 rows — formalizing STATUS QUO COST FRAME) before Q1
- COST LEDGER SUBSTRATE GATE after COST LEDGER
- ALIGNMENT STATE BINDING declaration before Q1
- Q1 = Operations (infrastructure substrate declaration, runs first) · Q2 = Commerce · Q3 = Finance
- All four constraint-type tables in each role section (one table per CT-ID)
- Full 8-item checklist per changed entity
- Phase A inertia example inside Q1 (distinct entity/step from B2 inertia example)

---

**COST LEDGER TABLE** — formalizes STATUS QUO COST FRAME into three-part structure

| Row | Part | Infrastructure/Schema Content | Validation Check |
|-----|------|-------------------------------|-----------------|
| (a) | Schema substrate | [exact schema condition, migration-state dependency, or infrastructure constraint — structural source. Must match "What the schema is doing to them" from STATUS QUO COST FRAME. Infrastructure/schema class only.] | Infrastructure class? [YES / NO] |
| (b) | Dependent process | [specific business process or data flow degrading because of row (a)] | Names specific process? [YES / NO] |
| (c) | Accumulation trajectory | [how the row (b) damage compounds without migration] | Names a trajectory? [YES / NO] |

**COST LEDGER SUBSTRATE GATE TABLE**

| Gate | Row (a) check | Result | On FAIL |
|------|--------------|--------|---------|
| COST LEDGER SUBSTRATE GATE | Row (a) names infrastructure/schema class (not business metric or process outcome) | [PASS / FAIL] | FAIL: stop. Return to parse phase. Re-identify substrate. Q1 entry blocked. |

**ALIGNMENT STATE BINDING TABLE** — before Q1

| Artifact | Infrastructure Condition Class | Match to Row (a)? |
|----------|-------------------------------|-------------------|
| COST LEDGER row (a) | [from Cost Ledger] | — (anchor) |
| Phase A Q1 analysis domain | [must name same class] | [YES / NO] |
| Phase B B2 substrate (pre-commit now) | [commit to same class before Phase A proceeds] | [YES / NO] |

ALIGNMENT STATE = SATISFIED when all rows agree. ALIGNMENT STATE = MISALIGNED when any row deviates — name the deviating artifact before proceeding.

---

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE** (analyzes ALIGNMENT STATE substrate; runs before Q2 and Q3)

Operations runs first because it declares the infrastructure substrate. Commerce and Finance analyze domain consequences that derive from the substrate condition Q1 establishes. The COST LEDGER row (a) names the same condition class Q1 analyzes.

**Q1 per-entity analysis table** (minimum 4 rows; Operations/infrastructure domain entities only)

| Entity | Pre-State | Migration Action | Post-State | Data Loss Path | Nullable Violation | Missing Default | Perf Cliff | Rollback |
|--------|-----------|-----------------|-----------|----------------|-------------------|----------------|------------|---------|

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
| Table | Column | Current Check | New Check | Rows Failing | Response |
|-------|--------|---------------|-----------|--------------|---------|

**Q1 Phase A inertia example** (must name a different entity/step than B2 inertia example)
| Prior working state | Migration action that breaks it | Operations consequence |
|--------------------|--------------------------------|----------------------|

---

**Q2 — COMMERCE ROLE** (same table schemas as Q1; Commerce domain entities only)

[Q2 per-entity table · Q2 CT-1 table · Q2 CT-2 table · Q2 CT-3 table · Q2 CT-4 table]

---

**Q3 — FINANCE ROLE** (same table schemas as Q1; Finance domain entities only)

[Q3 per-entity table · Q3 CT-1 table · Q3 CT-2 table · Q3 CT-3 table · Q3 CT-4 table]

---

**PHASE A-TO-B BOUNDARY PROTOCOL TABLE**

| Field | Value | Annotation |
|-------|-------|------------|
| PARSE GATE | [OPEN \| CLOSED] | (BINARY FIELD) |
| ALIGNMENT STATE | [SATISFIED \| MISALIGNED] | — |
| Phase B entry condition | PARSE GATE (BINARY FIELD) = OPEN AND ALIGNMENT STATE = SATISFIED | both required |
| On PARSE GATE CLOSED | Return to parse phase · complete registry · fill all CT tables in all role sections | — |
| On ALIGNMENT STATE MISALIGNED | Return to Q1 · align domain with COST LEDGER row (a) substrate class · re-confirm B2 pre-commitment | — |
| EXIT BLOCK annotation note | The `(BINARY FIELD)` annotation on PARSE GATE appears identically at the ENTRY REFERENCE position in Phase B — both structural anchors carry the compound type annotation independently | — |

---

### PHASE B — SYNTHESIS AND EXECUTION RECORD

**Phase B coverage requirements:**
- ENTRY REFERENCE TABLE (first block of Phase B; gate states + compound annotation + self-documenting rationale note)
- PROTOCOL COUNT MANIFEST TABLE with completeness rule (second block; enumerated block types; action directive)
- B1 entity state table (all changed entities from all domain roles)
- B2 cross-role causal chain (shared substrate from ALIGNMENT STATE binding; 2+ domain roles; distinct from Phase A inertia example)
- B3 constraint cross-reference (all CT-IDs from registry)

---

**PHASE B ENTRY REFERENCE TABLE** — first block of Phase B; before all analytical content

| Field | Required State | Annotation | Self-Documenting Rationale |
|-------|---------------|------------|---------------------------|
| PARSE GATE | OPEN | (BINARY FIELD) | [State here why the `(BINARY FIELD)` annotation is present at this ENTRY REFERENCE position: that a reader consulting only this block sees the binary constraint type and the required state without needing to consult the Phase A EXIT BLOCK. The annotation is self-documenting at this position.] |
| ALIGNMENT STATE | SATISFIED | — | — |

Fill the Self-Documenting Rationale column for PARSE GATE. Do not leave it blank. The rationale states why the compound annotation is present at the ENTRY REFERENCE anchor, not only at the EXIT BLOCK definition site.

---

**PROTOCOL COUNT MANIFEST TABLE** — second block of Phase B; before B1

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|----|---|---|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes |
| COST LEDGER SUBSTRATE GATE | — | Phase A body | PASS | Yes |

**MANIFEST COMPLETENESS RULE** — required section below the manifest table

Fill this rule template completely before proceeding to B1:

> A gate named in any **[fill: enumerate the three block types that constitute the gate inventory in this trace]** that is absent from this manifest = incomplete registry.

After the rule statement, add this action directive:

> **[fill: write a positive instruction directing the evaluator to apply this rule, or a negative prohibition naming what the rule replaces, or both]**

Do not use "any block" as the scope term in the rule — the rule must name the block types. Do not leave the action directive blank — the rule must specify how the evaluator is to use it.

---

**B1 — ENTITY STATE TABLE**

| Entity | Domain | Before-State | Migration Executed | After-State | Net Data Effect |
|--------|--------|-------------|-------------------|-------------|----------------|

Net Data Effect: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE. Minimum 1 row per domain role.

---

**B2 — CROSS-ROLE CAUSAL CHAIN** (Phase B inertia-contrast example; closes the STATUS QUO COST FRAME narrative by naming what happens when the status quo persists into the migration execution window)

| Element | Content |
|---------|---------|
| Shared substrate | [infrastructure condition from ALIGNMENT STATE binding — must match COST LEDGER row (a) class and STATUS QUO COST FRAME "what the schema is doing"] |
| Commerce consequence | [table · process · user-visible outcome when substrate is violated during migration] |
| Finance consequence | [ledger table · transaction type · reconciliation impact when same substrate is violated] |
| Causal link | [why both consequences follow from the same substrate condition — and why migration termination of the STATUS QUO COST prevents both] |

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| CT-ID | Constraint Type | Q1 Summary | Q2 Summary | Q3 Summary | Migration Response | Residual Risk |
|-------|----------------|-----------|-----------|-----------|-------------------|--------------|
| CT-1 | NOT NULL | | | | | |
| CT-2 | FOREIGN KEY | | | | | |
| CT-3 | UNIQUE | | | | | |
| CT-4 | CHECK | | | | | |

Every CT-ID from the registry must appear. A registry entry absent from B3 = cross-reference gap. Residual Risk = NONE CONFIRMED when migration fully addresses the constraint class.
