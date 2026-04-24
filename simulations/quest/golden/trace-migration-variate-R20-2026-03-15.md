# trace-migration Variate — Round 20
**Date:** 2026-03-15
**Rubric:** v18 (C-51, C-52, C-53 introduced)
**Target criteria:** C-51 (STATUS QUO COST FRAME pre-parse positioning), C-52 (B2 as explicit STATUS QUO COST FRAME closure), C-53 (ENTRY REFERENCE structural incompleteness verdict)

---

## Round 20 Variation Map

| Variation | Axis | C-51 | C-52 | C-53 | Notes |
|-----------|------|------|------|------|-------|
| V-01 | Role sequence | Expected PASS | Expected PASS | Expected PASS | Substrate-first narrative places STATUS QUO COST FRAME before parse phase as architectural premise; B2 closure named as consequence of same narrative; C-53 delivered as inline structural note at ENTRY REFERENCE |
| V-02 | Output format | Expected PASS | Expected PASS | Expected PASS | STATUS QUO COST FRAME table precedes CONSTRAINT TYPE REGISTRY table in section order; B2 table has mandatory FRAME CLOSURE row; ENTRY REFERENCE table has structural completeness verdict row with pre-filled incompleteness language |
| V-03 | Phrasing register | Expected PASS | Expected PASS | Expected PASS | DIRECTIVE imperatives: DIRECTIVE A-0 mandates pre-parse frame placement (C-51), DIRECTIVE B-1a states structural incompleteness verdict verbatim (C-53), DIRECTIVE B-2 mandates explicit frame closure at B2 (C-52) |
| V-04 | Role sequence + Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | Per-phase coverage floors name frame-boundary vocabulary as required terms; frame open (pre-parse) and frame close (B2) are auditable as vocabulary presence checks; ENTRY REFERENCE completeness verdict included in Phase B floor |
| V-05 | Role sequence + Output format + Inertia framing | Expected PASS | Expected PASS | Expected PASS | Full combination: inertia framing given maximum structural weight — precedes ALL content including parse phase; B2 is over-specified as STATUS QUO COST FRAME CLOSE with two named closure statements; ENTRY REFERENCE table structural incompleteness verdict is a mandatory pre-filled cell |

---

## V-01 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Framing the STATUS QUO COST FRAME as the architectural premise for all analysis — the thing the analyst commits to before touching any constraint enumeration or schema architecture — creates a structural ordering that satisfies C-51 naturally: the inertia-cost frame precedes not just Q1 but the parse phase itself, because the analyst must understand what inaction costs before deciding which constraints to enumerate. B2's role as cross-role consequence synthesizer follows from the same substrate continuity: the analyst has been operating within the inertia-cost frame from before parsing, and B2 is where that frame's accumulated multi-role cost is demonstrated and named closed. The ENTRY REFERENCE structural incompleteness verdict (C-53) follows from the prompt's own enforcement register: named structural failures are block-level verdicts, not missing-element observations.

---

You are running a migration trace signal for: {{topic}}

---

### STATUS QUO COST FRAME — OPEN

*This section opens the STATUS QUO COST FRAME. All analysis that follows — constraint type enumeration, schema parsing, domain role review, Phase B synthesis — is conducted within this frame. The frame closes at B2.*

The Status Quo Cost is the damage the current schema state is already inflicting without the migration. It is not a migration risk — it is the accumulating cost of inaction. Establish this baseline before the parse phase begins. The inertia-cost commitment made here is the architectural premise for every constraint enumerated and every role analyzed.

**COST LEDGER**

| Row | Category | Current State | Accumulation Mechanism |
|-----|----------|---------------|------------------------|
| (a) | Schema substrate | [Name the exact schema condition, migration-state dependency, or infrastructure constraint that is the structural source of the cost. Infrastructure or schema condition only — not a business process outcome.] | |
| (b) | Dependent process | [Name the business process or data flow that is breaking because of row (a). Concrete disruption.] | |
| (c) | Accumulation | [State how the cost in row (b) compounds over time without migration. Name the trajectory: data debt, query degradation, reconciliation overhead, etc.] | |

**COST LEDGER SUBSTRATE GATE**
Row (a) category check: if row (a) names a business process outcome or financial metric rather than a schema or infrastructure condition, do not proceed to the parse phase. Return here and re-identify the infrastructure substrate. Row (a) must name the structural source, not a downstream symptom.

**ALIGNMENT STATE BINDING**
The infrastructure condition named in COST LEDGER row (a) is the binding substrate for this entire trace. Q1's analysis domain must name this same condition class. B2's cross-role chain substrate must cite this same condition. Record before proceeding:

> ALIGNMENT STATE substrate: ___________________________
> Binding rule: COST LEDGER row (a), Q1 analysis domain, and B2 chain substrate must name the same infrastructure condition class. Any deviation across the three artifacts constitutes ALIGNMENT STATE = MISALIGNED.

---

### PARSE PHASE — CONSTRAINT TYPE REGISTRY

*The STATUS QUO COST FRAME is open. Enumerate constraint types within that frame.*

Before per-role analysis begins, enumerate every constraint type the migration touches:

**CONSTRAINT TYPE REGISTRY**

| Constraint Type | Tables Affected | Migration Action | Risk Level |
|-----------------|-----------------|------------------|------------|
| NOT NULL | | | |
| FOREIGN KEY | | | |
| UNIQUE | | | |
| CHECK | | | |

Fill all rows before proceeding. If a constraint type has no affected tables, state "none confirmed" — do not omit the row. Every type listed here must appear in a dedicated analytical field in both Phase A and Phase B. Constraint types not in this registry may not appear in analysis.

---

### PHASE A — SCHEMA SUBSTRATE AND DOMAIN ANALYSIS

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE**

Q1 runs first because it establishes the shared schema substrate that all domain-role consequence analysis derives from. Operations declares the substrate; Commerce and Finance interpret what breaks when it fails. Q1's analysis domain must match the ALIGNMENT STATE substrate declared above.

Analytical checklist — apply to every changed entity in this role's domain:
- Schema state before migration: column types, nullability constraints, index coverage, FK bindings
- Migration action: what the DDL or data script does to this entity
- Schema state after migration: post-execution entity state
- Data loss path: any transformation, truncation, or drop that loses rows or precision
- Nullable violation: NOT NULL introduced on a column with existing nulls
- Missing default: new NOT NULL without a DEFAULT on a non-empty table
- Performance cliff: full-table scan, index disable, statistics baseline disruption
- Rollback path: reversible? What does reversal leave behind?

Per-constraint analysis fields (one field per registry type; do not combine types):

**NOT NULL ANALYSIS — Q1**
[Constraint type: NOT NULL · Tables: [name affected tables] · Pre-migration state: [current nullability] · Migration action: [DDL] · Violation path: [rows that will fail on execution] · Enforcement response: [abort / default injection / backfill required]]

**FOREIGN KEY ANALYSIS — Q1**
[Constraint type: FK · Tables: [parent/child tables] · Pre-migration state: [referential integrity state] · Migration action: [what changes] · Violation path: [orphan rows, cascade implications] · Enforcement response: [on violation]]

**UNIQUE ANALYSIS — Q1**
[Constraint type: UNIQUE · Tables: [name tables] · Pre-migration state: [uniqueness state] · Migration action: [DDL] · Violation path: [duplicate rows that will violate] · Enforcement response: [dedup strategy or abort condition]]

**CHECK ANALYSIS — Q1**
[Constraint type: CHECK · Tables: [name tables] · Pre-migration state: [current check condition] · Migration action: [DDL] · Violation path: [rows failing the new check] · Enforcement response: [migration response to violations]]

**Phase A inertia-contrast example — Operations domain:**
Three-part structure: (1) prior working state that depended on the pre-migration schema, (2) how this migration breaks that working state, (3) the concrete consequence in Operations terms. This example must be distinct from the Phase B inertia example — different migration step, different table, or different consequence.

---

**Q2 — COMMERCE ROLE**

You are the Commerce expert. Apply the same analytical checklist and all four per-constraint analysis fields for Commerce domain entities (catalog tables, pricing structures, order schema, promotion rules, entitlement records). Name specific tables and columns — do not generalize to "Commerce data."

[Apply full Q1 checklist to Commerce domain entities. All four constraint-type analysis fields. Name specific tables.]

---

**Q3 — FINANCE ROLE**

You are the Finance expert. Apply the same analytical checklist and all four per-constraint analysis fields for Finance domain entities (ledger tables, transaction records, cost center schema, period-end views, audit trail structures). Name specific tables and columns.

[Apply full Q1 checklist to Finance domain entities. All four constraint-type analysis fields. Name specific tables.]

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
  Do not proceed to Phase B until all constraint-type fields are
  filled in all role sections.

If ALIGNMENT STATE = MISALIGNED:
  Return to Q1. Align Q1 domain with COST LEDGER row (a) substrate class.
  Re-confirm B2 substrate pre-commitment before proceeding.
```

The `(BINARY FIELD)` compound annotation on PARSE GATE is the type annotation that makes the binary enforcement mechanism self-documenting at its definition site. This same annotation appears at the ENTRY REFERENCE position opening Phase B — both structural anchors carry it independently.

---

### PHASE B — SYNTHESIS AND CROSS-ROLE CONSEQUENCES

**ENTRY REFERENCE — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

This ENTRY REFERENCE opens Phase B within the same STATUS QUO COST FRAME established before the parse phase. The `(BINARY FIELD)` compound annotation on PARSE GATE is identical to the EXIT BLOCK annotation — present at this position so that a reader consulting only Phase B's opening block sees the binary constraint type without cross-referencing Phase A's EXIT BLOCK. This self-documenting property is the reason the annotation appears at both structural anchors: neither position requires its partner to be interpretable.

*An ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete.*

---

**PROTOCOL COUNT MANIFEST**

All named gates in this trace, enumerated at Phase B entry before any analytical content:

| Gate Name | Block Location | Required State | Blocks Transition? |
|-----------|----------------|----------------|-------------------|
| PARSE GATE (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes — Phase B entry |
| PARSE GATE (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | Phase A-to-B EXIT BLOCK | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**Completeness rule:** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position in this trace but absent from this manifest = incomplete registry. Apply this rule to detect omissions — do not rely on cross-document search to verify gate coverage.

---

**B1 — MIGRATION EXECUTION SUMMARY**

One row per changed entity:

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**B2 — CROSS-ROLE CAUSAL CHAIN**

*This section closes the STATUS QUO COST FRAME opened before the parse phase.*

The Phase B inertia-contrast example names a cross-role causal chain: a shared infrastructure substrate condition (matching the ALIGNMENT STATE substrate declared in Phase A) whose disruption produces direct, named consequences in at least two distinct domain roles. Structure:

1. **Shared substrate**: Name the schema state or migration-step dependency that Operations Q1 established — must match the ALIGNMENT STATE substrate class.
2. **Commerce consequence**: Name the specific Commerce domain failure when the substrate is violated — table, business process, user-visible outcome.
3. **Finance consequence**: Name the specific Finance domain failure from the same substrate violation — ledger table, transaction type, reconciliation impact.
4. **Causal link**: State why both consequences follow from the same substrate condition. Demonstrating the substrate failure once demonstrates both downstream failures simultaneously.

*STATUS QUO COST FRAME CLOSE: B2 demonstrates the accumulated cross-role cost that the STATUS QUO COST FRAME established before parsing. The inertia-cost frame opened before constraint enumeration began is now closed at this cross-role synthesis.*

This example must be distinct from Q1's Phase A inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

One row per constraint type from the registry. Every registry type must appear as a row — a registry type absent from this table is a cross-reference gap.

| Constraint Type | Q1 Finding | Q2 Finding | Q3 Finding | Migration Response | Residual Risk |
|-----------------|-----------|-----------|-----------|-------------------|---------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Residual Risk: state NONE CONFIRMED if all instances are addressed by the migration.

---

---

## V-02 — Output Format

**Axis:** Output format
**Hypothesis:** Making C-51, C-52, and C-53 structural formatting requirements — expressed as named table sections with explicit fill rules and pre-positioned section headers — removes all aspirational ambiguity. When the STATUS QUO COST FRAME occupies its own section header that precedes the PARSE PHASE section header, C-51 is a section-ordering requirement. When the B2 table schema includes a mandatory FRAME CLOSURE row with required fill content, C-52 cannot be omitted without leaving a blank required row. When the ENTRY REFERENCE table schema includes a structural completeness verdict row whose pre-filled content names the incompleteness condition verbatim, C-53 passes by format.

---

You are running a migration trace signal for: {{topic}}

---

### STATUS QUO COST FRAME

*Section order requirement: this section precedes the PARSE PHASE section. The inertia-cost commitment established here is the architectural premise for constraint enumeration and all subsequent analysis.*

**COST LEDGER TABLE** — populate before the parse phase

| Row | Part | Content | Validation |
|-----|------|---------|-----------|
| (a) | Schema substrate | [Name the exact schema condition, migration-state dependency, or infrastructure constraint — infrastructure/schema class only, not a business outcome] | Infrastructure/schema class only |
| (b) | Dependent process | [Name the specific business process or data flow degrading because of row (a)] | Name a specific process |
| (c) | Accumulation | [State how row (b) damage compounds: data debt, query degradation, reconciliation load, etc.] | Name a trajectory |

**COST LEDGER SUBSTRATE GATE TABLE**

| Check | Result | Action on FAIL |
|-------|--------|----------------|
| Row (a) is infrastructure/schema class, not business metric or process outcome | [PASS / FAIL] | FAIL: stop; return to this section; re-identify substrate before proceeding to parse phase |

**ALIGNMENT STATE TABLE** — commits three artifacts to the same substrate class

| Artifact | Infrastructure Condition Class Named | Matches Row (a)? |
|----------|--------------------------------------|------------------|
| COST LEDGER row (a) | [fill from Cost Ledger above] | — (reference anchor) |
| Phase A Q1 analysis domain | [must match row (a) class] | [YES / NO] |
| Phase B B2 chain substrate (pre-commit) | [commit to same class now — before parse phase] | [YES / NO] |

Record: ALIGNMENT STATE = SATISFIED (all three agree) or ALIGNMENT STATE = MISALIGNED (name deviating artifact).

---

### PARSE PHASE

**CONSTRAINT TYPE REGISTRY TABLE** — required before Phase A; fill all rows

| ID | Constraint Type | Affected Tables | Migration Action | Risk Level |
|----|-----------------|-----------------|------------------|------------|
| CT-1 | NOT NULL | | | |
| CT-2 | FOREIGN KEY | | | |
| CT-3 | UNIQUE | | | |
| CT-4 | CHECK | | | |

Registry lock: no constraint type may appear in analysis unless listed here. Every listed type must appear in per-role constraint-type tables (Q1, Q2, Q3) and in B3.

---

### PHASE A

**Q1 — OPERATIONS ROLE** (analyzes ALIGNMENT STATE substrate; runs before Q2 and Q3)

Per-entity analysis table (minimum 4 rows; Operations/infrastructure domain entities only):

| Entity | Pre-State | Migration Action | Post-State | Data Loss Path | Nullable Violation | Missing Default | Perf Cliff | Rollback |
|--------|-----------|-----------------|-----------|----------------|-------------------|----------------|------------|---------|

Per-constraint-type tables (one table per CT-registry entry; do not combine types):

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
| Table | Column | Current Check Condition | New Check Condition | Rows Failing | Response |
|-------|--------|------------------------|---------------------|--------------|---------|

**Phase A inertia table — Operations domain** (must be distinct entity/step from Phase B B2 example):
| Prior working state | Migration action that breaks it | Concrete Operations consequence |
|--------------------|---------------------------------|---------------------------------|

---

**Q2 — COMMERCE ROLE** (same table schemas as Q1; Commerce domain entities only)

[Per-entity table · CT-1 through CT-4 tables · Commerce entities only — no repetition of Q1 entities]

---

**Q3 — FINANCE ROLE** (same table schemas as Q1; Finance domain entities only)

[Per-entity table · CT-1 through CT-4 tables · Finance entities only]

---

**PHASE A-TO-B BOUNDARY PROTOCOL TABLE**

| Field | Value | Annotation |
|-------|-------|------------|
| PARSE GATE | [OPEN \| CLOSED] | (BINARY FIELD) |
| ALIGNMENT STATE | [SATISFIED \| MISALIGNED] | — |
| Phase B entry condition | PARSE GATE (BINARY FIELD) = OPEN AND ALIGNMENT STATE = SATISFIED | both required |
| On PARSE GATE CLOSED | Return to parse phase · complete CONSTRAINT TYPE REGISTRY · fill all CT tables in all role sections | — |
| On ALIGNMENT STATE MISALIGNED | Return to Q1 · align Q1 domain with COST LEDGER row (a) class · re-confirm B2 substrate pre-commitment | — |

The `(BINARY FIELD)` annotation in the Annotation column is the compound type annotation for PARSE GATE at this EXIT BLOCK position. It appears identically at the ENTRY REFERENCE table in Phase B — both structural anchors carry the annotation independently.

---

### PHASE B

**PHASE B ENTRY REFERENCE TABLE** — first block in Phase B; before all analytical content

| Field | Required State | Annotation |
|-------|---------------|------------|
| PARSE GATE | OPEN | (BINARY FIELD) |
| ALIGNMENT STATE | SATISFIED | — |

**ENTRY REFERENCE STRUCTURAL COMPLETENESS TABLE** — required immediately below the gate table above

| Property | Required Content |
|----------|-----------------|
| Self-documenting rationale | [State why the `(BINARY FIELD)` annotation is present at this ENTRY REFERENCE position: that the compound type makes the gate condition interpretable here without consulting the EXIT BLOCK. A reader consulting only Phase B's opening sees both the required state and the binary constraint type, independently.] |
| Structural completeness verdict | An ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete. |

Both rows are required. An ENTRY REFERENCE table with a blank or placeholder Self-documenting rationale row fails the structural completeness check stated in the row immediately below it.

---

**PROTOCOL COUNT MANIFEST TABLE** — second block of Phase B; before B1

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|-----------------|-----------------|--------------------|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes — Phase B entry |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | — | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**MANIFEST COMPLETENESS RULE TABLE**

| Rule | Scope | Action Directive |
|------|-------|-----------------|
| A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position in this trace but absent from this manifest = incomplete registry | Scope: BOUNDARY PROTOCOL blocks, EXIT BLOCK positions, ENTRY REFERENCE positions | Apply this rule to detect omissions — do not rely on cross-document search. Check this rule against all gate-bearing blocks before proceeding to B1. |

---

**B1 — MIGRATION EXECUTION SUMMARY TABLE**

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**B2 — CROSS-ROLE CAUSAL CHAIN TABLE**

| Component | Content |
|-----------|---------|
| FRAME CLOSURE STATEMENT | *This section closes the STATUS QUO COST FRAME established before the parse phase. B2 demonstrates the accumulated cross-role cost that the STATUS QUO COST FRAME was opened to establish. The inertia-cost frame is now closed.* |
| Shared substrate | [Name the schema state or migration-step dependency matching the ALIGNMENT STATE substrate — same class as COST LEDGER row (a)] |
| Commerce consequence | [Name the specific Commerce domain failure: table, business process, user-visible outcome] |
| Finance consequence | [Name the specific Finance domain failure: ledger table, transaction type, reconciliation impact] |
| Causal link | [State why both consequences follow from the same substrate condition — demonstrating the substrate failure once demonstrates both failures simultaneously] |

The FRAME CLOSURE STATEMENT row is required. An absent or placeholder FRAME CLOSURE STATEMENT row means B2 is not explicitly positioned as the STATUS QUO COST FRAME close — the frame opened before the parse phase has no named close.

This example must be distinct from Q1's Phase A inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| Constraint Type | Q1 Finding | Q2 Finding | Q3 Finding | Migration Response | Residual Risk |
|-----------------|-----------|-----------|-----------|-------------------|---------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Every registry type must appear as a row. Residual Risk: NONE CONFIRMED if all instances addressed.

---

---

## V-03 — Phrasing Register

**Axis:** Phrasing register (DIRECTIVE imperatives with exact required text)
**Hypothesis:** Expressing C-51, C-52, and C-53 as named DIRECTIVE commands — each with exact required text and explicit prohibitions — removes interpretive latitude. DIRECTIVE A-0 mandates that the STATUS QUO COST FRAME precede the parse phase as a named architectural rule. DIRECTIVE B-1a states the structural incompleteness verdict verbatim: "An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete." DIRECTIVE B-2 mandates that B2 include an explicit named closure statement linking B2 to the STATUS QUO COST FRAME. When the criterion text is embedded in the prompt as a DIRECTIVE command, its absence is a DIRECTIVE violation — not an aspirational omission.

---

You are running a migration trace signal for: {{topic}}

---

**DIRECTIVE A-0 — STATUS QUO COST FRAME PLACEMENT**

> WRITE the STATUS QUO COST FRAME section as the first section of this output, before the PARSE PHASE and before any constraint enumeration. The inertia-cost commitment is not a Phase A framing section — it is an architectural premise that precedes the analytical pipeline. A STATUS QUO COST FRAME that first appears after constraint type enumeration has begun violates this directive. The baseline must be established before any CONSTRAINT TYPE REGISTRY content is written.

---

### STATUS QUO COST FRAME

*DIRECTIVE A-0 compliance position: this section precedes PARSE PHASE and all constraint enumeration.*

The Status Quo Cost is the damage the current schema state is already inflicting without the migration. Three-part structure expressed as a COST LEDGER table:

**COST LEDGER**

| Row | Category | Current State | Accumulation Mechanism |
|-----|----------|---------------|------------------------|
| (a) | Schema substrate | [Infrastructure/schema condition only — the structural source of the cost, not a downstream symptom] | |
| (b) | Dependent process | [Business process or data flow breaking because of row (a)] | |
| (c) | Accumulation | [How row (b) damage compounds over time — name the trajectory] | |

**COST LEDGER SUBSTRATE GATE**
If row (a) names a business process outcome or financial metric rather than a schema or infrastructure condition: stop. Return to this section. Re-identify the infrastructure substrate. Row (a) must name the structural source.

**ALIGNMENT STATE BINDING**
> ALIGNMENT STATE substrate: ___________________________
> Binding rule: COST LEDGER row (a), Q1 analysis domain, and B2 chain substrate must name the same infrastructure condition class.

---

### PARSE PHASE — CONSTRAINT TYPE REGISTRY

**CONSTRAINT TYPE REGISTRY**

| Constraint Type | Tables Affected | Migration Action | Risk Level |
|-----------------|-----------------|------------------|------------|
| NOT NULL | | | |
| FOREIGN KEY | | | |
| UNIQUE | | | |
| CHECK | | | |

Fill all rows before proceeding. "None confirmed" is valid — do not omit rows. Every listed type must appear in dedicated analytical fields in Phase A and Phase B.

---

### PHASE A — SCHEMA SUBSTRATE AND DOMAIN ANALYSIS

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE**

Q1 analyzes the ALIGNMENT STATE substrate declared above. Q1 runs first because the shared infrastructure substrate must be established before Commerce and Finance consequence analysis proceeds.

Analytical checklist — apply to every changed entity:
- Schema state before migration: column types, nullability, index coverage, FK bindings
- Migration action: what the DDL or data script does
- Schema state after migration: post-execution state
- Data loss path: transformation, truncation, or drop that loses rows or precision
- Nullable violation: NOT NULL on a column with existing nulls
- Missing default: new NOT NULL without DEFAULT on a non-empty table
- Performance cliff: full-table scan, index disable, statistics baseline disruption
- Rollback path: reversible? What does reversal leave behind?

Per-constraint analysis fields (one per registry type; do not combine):

**NOT NULL ANALYSIS — Q1**
[Type: NOT NULL · Tables: · Pre-state: · Migration action: · Violation path: · Enforcement response:]

**FOREIGN KEY ANALYSIS — Q1**
[Type: FK · Tables: · Pre-state: · Migration action: · Violation path: · Enforcement response:]

**UNIQUE ANALYSIS — Q1**
[Type: UNIQUE · Tables: · Pre-state: · Migration action: · Violation path: · Enforcement response:]

**CHECK ANALYSIS — Q1**
[Type: CHECK · Tables: · Pre-state: · Migration action: · Violation path: · Enforcement response:]

**Phase A inertia-contrast example — Operations domain** (distinct from Phase B example):
Three-part: (1) prior working state, (2) how migration breaks it, (3) concrete Operations consequence.

---

**Q2 — COMMERCE ROLE**

Apply full Q1 checklist and all four constraint-type fields to Commerce domain entities. Name specific tables.

---

**Q3 — FINANCE ROLE**

Apply full Q1 checklist and all four constraint-type fields to Finance domain entities. Name specific tables.

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
  Return to parse phase. Complete CONSTRAINT TYPE REGISTRY.
  Fill all constraint-type fields in all role sections.

If ALIGNMENT STATE = MISALIGNED:
  Return to Q1. Align Q1 domain with COST LEDGER row (a) substrate class.
```

The `(BINARY FIELD)` compound annotation on PARSE GATE is the self-documenting type annotation at the EXIT BLOCK definition site. It will also appear identically at the ENTRY REFERENCE position opening Phase B.

---

### PHASE B — SYNTHESIS AND CROSS-ROLE CONSEQUENCES

**DIRECTIVE B-1a — ENTRY REFERENCE STRUCTURAL COMPLETENESS**

> WRITE the ENTRY REFERENCE block as the first element of Phase B, before any other content. The block must carry the `(BINARY FIELD)` compound annotation on PARSE GATE. Immediately below the gate state block, WRITE an inline rationale note stating the self-documenting property: that the `(BINARY FIELD)` annotation makes the gate condition interpretable at this ENTRY REFERENCE position without consulting the EXIT BLOCK. An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete.

**ENTRY REFERENCE — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

*[WRITE the inline rationale note here: state that the `(BINARY FIELD)` compound annotation on PARSE GATE makes the binary constraint type self-documenting at this position. A reader consulting only Phase B's opening block sees the required state (OPEN) and the constraint type (BINARY FIELD) without cross-referencing Phase A's EXIT BLOCK. Both structural anchors carry the full annotation independently.]*

*Per DIRECTIVE B-1a: an ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete.*

---

**PROTOCOL COUNT MANIFEST**

All named gates, enumerated at Phase B entry before B1:

| Gate Name | Block Location | Required State | Blocks Transition? |
|-----------|----------------|----------------|-------------------|
| PARSE GATE (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes — Phase B entry |
| PARSE GATE (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | Phase A-to-B EXIT BLOCK | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**Completeness rule:** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position but absent from this manifest = incomplete registry. Apply this rule to detect omissions — do not rely on cross-document search to verify gate coverage. Check this rule against all gate-bearing blocks before proceeding to B1.

---

**B1 — MIGRATION EXECUTION SUMMARY**

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**DIRECTIVE B-2 — STATUS QUO COST FRAME CLOSURE AT B2**

> WRITE the B2 section as the explicit close of the STATUS QUO COST FRAME established before the parse phase. The first sentence of B2 must name B2 as the STATUS QUO COST FRAME close — for example: "This section closes the STATUS QUO COST FRAME opened before the parse phase." Then provide the cross-role causal chain demonstrating the accumulated cost. A B2 section that provides a cross-role causal chain without an explicit STATUS QUO COST FRAME closure statement fails this directive: the cross-role chain provides the evidence but does not name the frame closure.

**B2 — CROSS-ROLE CAUSAL CHAIN**

> *[WRITE STATUS QUO COST FRAME CLOSE statement here, per DIRECTIVE B-2. Example: "This section closes the STATUS QUO COST FRAME opened before the parse phase. B2 demonstrates the accumulated cross-role cost that the STATUS QUO COST FRAME was established to quantify."]*

Cross-role causal chain structure:

1. **Shared substrate**: Name the schema state or migration-step dependency matching the ALIGNMENT STATE substrate (same class as COST LEDGER row (a)).
2. **Commerce consequence**: Specific Commerce domain failure — table, business process, user-visible outcome.
3. **Finance consequence**: Specific Finance domain failure — ledger table, transaction type, reconciliation impact.
4. **Causal link**: Why both consequences follow from the same substrate condition. Demonstrating the substrate failure once demonstrates both downstream failures simultaneously.

This example must be distinct from Q1's Phase A inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| Constraint Type | Q1 Finding | Q2 Finding | Q3 Finding | Migration Response | Residual Risk |
|-----------------|-----------|-----------|-----------|-------------------|---------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Every registry type must appear as a row. Residual Risk: NONE CONFIRMED if all instances addressed.

---

---

## V-04 — Role Sequence + Lifecycle Emphasis

**Axis:** Role sequence + Lifecycle emphasis
**Hypothesis:** Combining Operations-as-substrate sequencing with explicit per-phase coverage floors that include frame-boundary vocabulary as required terms makes C-51, C-52, and C-53 auditable as vocabulary presence checks. When Phase A's coverage floor requires the terms "STATUS QUO COST FRAME", "pre-parse", and "architectural premise", an output that opens Phase A without those terms fails the floor. When Phase B's coverage floor requires "FRAME CLOSE", "STATUS QUO COST FRAME", and "structurally incomplete", the frame closure and completeness verdict are auditable as floor violations, not as aspirational annotation gaps. The lifecycle emphasis forces every phase to name its relationship to the frame explicitly.

---

You are running a migration trace signal for: {{topic}}

---

### PHASE ARCHITECTURE AND COVERAGE FLOORS

This trace operates in three phases: STATUS QUO COST FRAME → PARSE PHASE → PHASE A → PHASE B. Each phase has a coverage floor — required vocabulary and structural elements that must be present. A phase that lacks any floor item is incomplete.

**STATUS QUO COST FRAME floor** (required before PARSE PHASE begins):
- Term "STATUS QUO COST FRAME" in a named section header or opening statement
- Term "architectural premise" or "before the parse phase" naming the frame's position
- COST LEDGER with three filled rows (a), (b), (c)
- ALIGNMENT STATE substrate declared

**PARSE PHASE floor**:
- CONSTRAINT TYPE REGISTRY with all four constraint types present (even if "none confirmed")

**PHASE A floor**:
- Q1 = Operations/Infrastructure (runs before Q2 and Q3)
- All four constraint-type analysis fields in each role section
- Phase A inertia-contrast example distinct from Phase B B2 example
- EXIT BLOCK with `(BINARY FIELD)` annotation on PARSE GATE and ALIGNMENT STATE as listed gate

**PHASE B floor**:
- ENTRY REFERENCE with `(BINARY FIELD)` annotation
- Term "structurally incomplete" in an inline rationale note at the ENTRY REFERENCE position, naming the consequence of annotation without rationale
- PROTOCOL COUNT MANIFEST with completeness rule naming BOUNDARY PROTOCOL blocks, EXIT BLOCK positions, and ENTRY REFERENCE positions as the scope
- B2 containing term "FRAME CLOSE" or "closes the STATUS QUO COST FRAME" explicitly naming B2 as the frame's narrative close

---

### STATUS QUO COST FRAME

*Architectural premise: the STATUS QUO COST FRAME is established here, before the parse phase and before any constraint enumeration, making the inertia-cost commitment the first analytical act in this trace.*

**COST LEDGER**

| Row | Category | Current State | Accumulation Mechanism |
|-----|----------|---------------|------------------------|
| (a) | Schema substrate | [Exact schema condition or infrastructure constraint — not a business process outcome] | |
| (b) | Dependent process | [Business process or data flow breaking because of row (a)] | |
| (c) | Accumulation | [How row (b) cost compounds — data debt, degradation, reconciliation overhead] | |

**COST LEDGER SUBSTRATE GATE**
Row (a) category check: if row (a) names a business process outcome or financial metric, stop. Return to this section and re-identify the infrastructure substrate before proceeding to the parse phase.

**ALIGNMENT STATE BINDING**
> ALIGNMENT STATE substrate: ___________________________
> Binding rule: COST LEDGER row (a), Q1 analysis domain, and B2 chain substrate must name the same infrastructure condition class.

---

### PARSE PHASE — CONSTRAINT TYPE REGISTRY

*The STATUS QUO COST FRAME is open. The parse phase enumerates constraint types within that frame.*

**CONSTRAINT TYPE REGISTRY**

| Constraint Type | Tables Affected | Migration Action | Risk Level |
|-----------------|-----------------|------------------|------------|
| NOT NULL | | | |
| FOREIGN KEY | | | |
| UNIQUE | | | |
| CHECK | | | |

Fill all rows. "None confirmed" for unaffected types — do not omit rows. Registry lock: every listed type must have dedicated analysis fields in Phase A and Phase B.

---

### PHASE A — SCHEMA SUBSTRATE AND DOMAIN ANALYSIS

*STATUS QUO COST FRAME is open. All Phase A analysis is conducted within the inertia-cost premise established before parsing.*

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE**

Operations runs first as the substrate-declaration role. Q1 establishes the shared infrastructure condition (matching ALIGNMENT STATE substrate) that Commerce and Finance consequence analysis derives from. Commerce and Finance interpret downstream breaks; Operations declares the schema layer.

Analytical checklist — apply to every changed entity:
- Before/after schema state (column types, nullability, index coverage, FK bindings)
- Migration action: DDL or data script behavior on this entity
- Data loss path: any truncation, row drop, or transformation loss
- Nullable violation: NOT NULL on a column with existing nulls
- Missing default: new NOT NULL without DEFAULT on a non-empty table
- Performance cliff: full-table scan, index disable, statistics disruption
- Rollback path: reversibility and residual state after reversal

Per-constraint analysis fields — one per registry type; do not combine:

**NOT NULL ANALYSIS — Q1** · **FOREIGN KEY ANALYSIS — Q1** · **UNIQUE ANALYSIS — Q1** · **CHECK ANALYSIS — Q1**
[Apply each field format: Type · Tables · Pre-state · Migration action · Violation path · Enforcement response]

**Phase A inertia-contrast example — Operations domain:**
Three-part: (1) prior working state, (2) how migration breaks it, (3) concrete Operations consequence. Distinct from B2.

---

**Q2 — COMMERCE ROLE**

Commerce inherits the infrastructure substrate Q1 declared. Analyze Commerce domain entities (catalog tables, pricing, order schema, entitlement records). Name specific tables. Apply full checklist and all four constraint-type fields.

---

**Q3 — FINANCE ROLE**

Finance inherits the same substrate. Analyze Finance domain entities (ledger tables, transaction records, period-end views, audit trail structures). Name specific tables. Apply full checklist and all four constraint-type fields.

---

**BOUNDARY PROTOCOL: PHASE A TO PHASE B**

**EXIT BLOCK — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = [OPEN | CLOSED]
ALIGNMENT STATE = [SATISFIED | MISALIGNED]

Required for Phase B entry:
  PARSE GATE (BINARY FIELD) = OPEN
  ALIGNMENT STATE = SATISFIED

If PARSE GATE (BINARY FIELD) = CLOSED:
  Return to parse phase. Complete registry. Fill all constraint-type fields
  in Q1, Q2, Q3.

If ALIGNMENT STATE = MISALIGNED:
  Return to Q1. Align Q1 domain with COST LEDGER row (a) substrate.
  Re-confirm B2 substrate pre-commitment.
```

The `(BINARY FIELD)` compound annotation makes PARSE GATE self-documenting at this EXIT BLOCK. The same annotation appears at the Phase B ENTRY REFERENCE position. Both anchors carry it independently — neither requires the other to be interpretable.

---

### PHASE B — SYNTHESIS AND CROSS-ROLE CONSEQUENCES

*The STATUS QUO COST FRAME opened before the parse phase remains open. Phase B closes the frame at B2.*

**ENTRY REFERENCE — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

*Inline rationale: The `(BINARY FIELD)` annotation on PARSE GATE at this ENTRY REFERENCE position makes the binary constraint type self-documenting here — a reader consulting only Phase B's opening block sees both the required state (OPEN) and the constraint type (BINARY FIELD) without cross-referencing Phase A's EXIT BLOCK. This is the self-documenting property the annotation is present to provide.*

*An ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete.*

Phase B floor check: confirm the following terms appear in Phase B before proceeding to B1:
- ☐ "structurally incomplete" — in ENTRY REFERENCE inline rationale
- ☐ "closes the STATUS QUO COST FRAME" or equivalent — in B2 FRAME CLOSE statement
- ☐ "BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position" — in manifest completeness rule

If any floor item is absent, complete it before continuing.

---

**PROTOCOL COUNT MANIFEST**

| Gate Name | Block Location | Required State | Blocks Transition? |
|-----------|----------------|----------------|-------------------|
| PARSE GATE (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes — Phase B entry |
| PARSE GATE (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | Phase A-to-B EXIT BLOCK | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**Completeness rule:** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position in this trace but absent from this manifest = incomplete registry. Apply this rule to detect omissions — do not rely on cross-document search. Check this rule against all gate-bearing blocks before proceeding to B1.

---

**B1 — MIGRATION EXECUTION SUMMARY**

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**B2 — CROSS-ROLE CAUSAL CHAIN**

*STATUS QUO COST FRAME CLOSE: this section closes the STATUS QUO COST FRAME opened before the parse phase. B2 demonstrates the accumulated cross-role cost of inaction — the multi-role evidence that makes the inertia-cost premise concrete.*

Cross-role causal chain — must name a shared infrastructure substrate condition (matching ALIGNMENT STATE substrate) whose disruption produces named consequences in at least two distinct domain roles:

1. **Shared substrate**: Schema state or migration-step dependency matching ALIGNMENT STATE substrate class.
2. **Commerce consequence**: Specific Commerce domain failure — table, business process, user-visible outcome.
3. **Finance consequence**: Specific Finance domain failure — ledger table, transaction type, reconciliation impact.
4. **Causal link**: Why both consequences follow from the same substrate condition.

This example must be distinct from Q1's Phase A inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| Constraint Type | Q1 Finding | Q2 Finding | Q3 Finding | Migration Response | Residual Risk |
|-----------------|-----------|-----------|-----------|-------------------|---------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Every registry type must appear as a row. Residual Risk: NONE CONFIRMED if all instances addressed.

---

---

## V-05 — Role Sequence + Output Format + Inertia Framing

**Axis:** Role sequence + Output format + Inertia framing (full combination)
**Hypothesis:** Maximum structural weight on the inertia frame — positioned before all content as the explicit structural first-mover, preceded by nothing — and then enforced at two named closure sites (pre-parse OPEN declaration + B2 named CLOSE) creates the most auditable STATUS QUO COST FRAME pair. Table schemas enforce all three new criteria: the STATUS QUO COST FRAME precedes the CONSTRAINT TYPE REGISTRY section by section-header ordering (C-51); B2's table schema has a mandatory FRAME CLOSURE row that is pre-filled with the closure statement and flags its own absence (C-52); the ENTRY REFERENCE table's structural completeness row contains verbatim C-53 language as a pre-filled cell value, making the incompleteness verdict part of the table schema itself. The three-artifact alignment architecture names its own block types in the manifest completeness rule, fully satisfying C-49/C-50 as carry-through.

---

You are running a migration trace signal for: {{topic}}

---

### STATUS QUO COST FRAME — OPEN
#### *Structural position: before the parse phase, before constraint enumeration, before any analytical content*

This section is the architectural premise for the entire trace. The inertia-cost commitment established here precedes constraint type enumeration, phase boundary construction, and all role analysis. Everything that follows operates within this frame. The frame closes at B2.

**COST LEDGER TABLE**

| Row | Part | Infrastructure Condition / Process / Trajectory | Validation |
|-----|------|-------------------------------------------------|-----------|
| (a) | Schema substrate | [Name the exact schema condition, migration-state dependency, or infrastructure constraint. Infrastructure/schema class only — not a business process outcome or financial metric.] | ☐ Infrastructure/schema class confirmed |
| (b) | Dependent process | [Name the specific business process or data flow degrading because of row (a). Name the mechanism of disruption.] | ☐ Specific process named |
| (c) | Accumulation | [State how the row (b) damage compounds over time without migration. Name the trajectory.] | ☐ Trajectory named |

**COST LEDGER SUBSTRATE GATE TABLE**

| Condition | Result | Action on FAIL |
|-----------|--------|----------------|
| COST LEDGER row (a) names an infrastructure or schema condition (not a business metric or process outcome) | [PASS / FAIL] | FAIL: stop; return to this section; re-identify the schema substrate before proceeding to the parse phase |

**ALIGNMENT STATE PRE-COMMITMENT TABLE**

| Artifact | Infrastructure Condition Class | Match? |
|----------|-------------------------------|--------|
| COST LEDGER row (a) — substrate anchor | [fill from Cost Ledger] | — |
| Phase A Q1 analysis domain | [must name same class as row (a)] | [YES / NO] |
| Phase B B2 chain substrate (pre-commit now) | [commit to same class now — before constraint enumeration begins] | [YES / NO] |

**ALIGNMENT STATE** = SATISFIED if all three agree · MISALIGNED if any deviate (name the deviating artifact)

---

### PARSE PHASE — CONSTRAINT TYPE REGISTRY

*The STATUS QUO COST FRAME is open. All constraint enumeration occurs within the inertia-cost frame established above.*

**CONSTRAINT TYPE REGISTRY TABLE**

| ID | Constraint Type | Affected Tables | Migration Action | Risk Level |
|----|-----------------|-----------------|------------------|------------|
| CT-1 | NOT NULL | | | |
| CT-2 | FOREIGN KEY | | | |
| CT-3 | UNIQUE | | | |
| CT-4 | CHECK | | | |

Fill all rows. "None confirmed" valid for unaffected types — do not omit rows. Registry lock: every listed type must appear in all per-role constraint-type tables (Q1, Q2, Q3) and in B3.

---

### PHASE A — SCHEMA SUBSTRATE AND DOMAIN ANALYSIS

*STATUS QUO COST FRAME is open. Phase A operates within the inertia-cost premise established before the parse phase.*

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE** *(runs first as substrate-declaration role)*

Q1 declares the shared infrastructure substrate that B2's cross-role chain will cite. Operations is the substrate source; Commerce (Q2) and Finance (Q3) interpret what breaks downstream. Q1's analysis domain must match the ALIGNMENT STATE substrate pre-committed above.

**Q1 per-entity analysis table** (minimum 4 rows; Operations/infrastructure entities only):

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Data Loss Path | Nullable Violation | Missing Default | Perf Cliff | Rollback Path |
|--------|--------------------|--------------------|---------------------|----------------|-------------------|----------------|------------|--------------|

**NOT NULL — Q1 TABLE** (CT-1)
| Table | Column | Pre-Nullability | Migration DDL | Rows at Risk | Enforcement Response |
|-------|--------|-----------------|---------------|--------------|----------------------|

**FOREIGN KEY — Q1 TABLE** (CT-2)
| Parent Table | Child Table | Current FK State | Migration Change | Orphan Risk | Cascade Behavior |
|-------------|------------|-----------------|-----------------|-------------|-----------------|

**UNIQUE — Q1 TABLE** (CT-3)
| Table | Column(s) | Current Uniqueness State | Migration Change | Duplicate Risk | Dedup Strategy |
|-------|----------|--------------------------|-----------------|----------------|----------------|

**CHECK — Q1 TABLE** (CT-4)
| Table | Column | Current Check Condition | New Check Condition | Rows Failing | Enforcement Response |
|-------|--------|------------------------|---------------------|--------------|----------------------|

**Phase A inertia table — Operations domain** (must be distinct entity/step from B2):
| Prior working state | Migration action that breaks it | Concrete Operations consequence |
|--------------------|--------------------------------|---------------------------------|

---

**Q2 — COMMERCE ROLE** *(inherits infrastructure substrate established by Q1)*

Commerce interprets downstream consequences of the Q1 substrate state. Analyze Commerce domain entities (catalog tables, pricing, order schema, promotion rules, entitlement records). Name specific tables — no entity from Q1.

[Per-entity table (minimum 3 rows) · CT-1 through CT-4 tables · Commerce entities only]

---

**Q3 — FINANCE ROLE** *(inherits infrastructure substrate established by Q1)*

Finance interprets financial consequences of the Q1 substrate state. Analyze Finance domain entities (ledger tables, transaction records, cost center schema, period-end views, audit trail structures). Name specific tables — no entities from Q1 or Q2.

[Per-entity table (minimum 3 rows) · CT-1 through CT-4 tables · Finance entities only]

---

**PHASE A-TO-B BOUNDARY PROTOCOL TABLE**

| Field | Value | Annotation | Notes |
|-------|-------|------------|-------|
| PARSE GATE | [OPEN \| CLOSED] | (BINARY FIELD) | Compound type annotation — self-documenting at this EXIT BLOCK site |
| ALIGNMENT STATE | [SATISFIED \| MISALIGNED] | — | Three-artifact alignment check |
| Phase B entry condition | PARSE GATE (BINARY FIELD) = OPEN AND ALIGNMENT STATE = SATISFIED | — | Both required |
| On PARSE GATE CLOSED | Return to parse phase · complete CONSTRAINT TYPE REGISTRY · fill all CT tables in Q1, Q2, Q3 | — | Hard gate |
| On ALIGNMENT STATE MISALIGNED | Return to Q1 · align domain with COST LEDGER row (a) substrate class · re-confirm B2 pre-commitment | — | Hard gate |

The `(BINARY FIELD)` annotation appears identically at the ENTRY REFERENCE position in Phase B — both structural anchors carry it independently, so neither requires its partner to determine the binary constraint type.

---

### PHASE B — SYNTHESIS AND CROSS-ROLE CONSEQUENCES

*STATUS QUO COST FRAME remains open. Phase B closes the frame at B2.*

**PHASE B ENTRY REFERENCE TABLE** — first block of Phase B; before all analytical content

| Field | Required State | Annotation |
|-------|---------------|------------|
| PARSE GATE | OPEN | (BINARY FIELD) |
| ALIGNMENT STATE | SATISFIED | — |

**ENTRY REFERENCE STRUCTURAL COMPLETENESS TABLE** — required immediately below the gate table above; both rows required

| Property | Content |
|----------|---------|
| Self-documenting rationale | [State why the `(BINARY FIELD)` annotation is present at this ENTRY REFERENCE position: the compound type annotation makes the gate condition interpretable here without consulting the EXIT BLOCK. A reader consulting only Phase B's opening block sees both the required state (OPEN) and the binary constraint type (BINARY FIELD) independently.] |
| Structural completeness verdict | An ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete. |

The structural completeness verdict row is pre-filled and must be reproduced verbatim. An ENTRY REFERENCE table that carries the gate annotation rows but omits the structural completeness verdict row is itself structurally incomplete — the verdict is not optional content but a block-level completeness requirement.

---

**PROTOCOL COUNT MANIFEST TABLE** — second block of Phase B; before B1

| Gate Name | Compound Annotation | Block Location | Required State | Blocks Transition? |
|-----------|--------------------|-----------------|-----------------|--------------------|
| PARSE GATE | (BINARY FIELD) | Phase A-to-B EXIT BLOCK (BOUNDARY PROTOCOL) | OPEN | Yes — Phase B entry |
| PARSE GATE | (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | — | Phase A-to-B EXIT BLOCK (BOUNDARY PROTOCOL) | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | — | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**MANIFEST COMPLETENESS RULE TABLE**

| Rule | Scope | Action Directive |
|------|-------|-----------------|
| A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position in this trace but absent from this manifest = incomplete registry | BOUNDARY PROTOCOL blocks · EXIT BLOCK positions · ENTRY REFERENCE positions | Apply this rule to detect omissions before proceeding to B1 — do not rely on cross-document search to verify gate coverage |

---

**B1 — MIGRATION EXECUTION SUMMARY TABLE**

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**B2 — CROSS-ROLE CAUSAL CHAIN TABLE**

| Component | Required Content |
|-----------|-----------------|
| **STATUS QUO COST FRAME CLOSE** | *This section closes the STATUS QUO COST FRAME opened before the parse phase. B2 is the named close of the inertia-cost frame: it demonstrates the accumulated cross-role cost that the STATUS QUO COST FRAME was established to quantify. The frame opened as an architectural premise before constraint enumeration began; it closes here with cross-role evidence.* *(Reproduce this statement or equivalent; a B2 section that provides a cross-role causal chain without an explicit STATUS QUO COST FRAME closure statement does not close the frame — the frame remains structurally open.)* |
| Shared substrate | [Name the schema state or migration-step dependency matching the ALIGNMENT STATE substrate class — same condition as COST LEDGER row (a)] |
| Commerce consequence | [Specific Commerce domain failure when the substrate is violated: table, business process, user-visible outcome] |
| Finance consequence | [Specific Finance domain failure from the same substrate violation: ledger table, transaction type, reconciliation impact] |
| Causal link | [Why both consequences follow from the same substrate condition — demonstrating the substrate failure once demonstrates both domain failures simultaneously] |

The STATUS QUO COST FRAME CLOSE row is required. A B2 table that omits or leaves blank the STATUS QUO COST FRAME CLOSE row means the STATUS QUO COST FRAME opened before the parse phase has no named close — the frame boundary pair is incomplete.

This example must be distinct from Q1's Phase A inertia example.

---

**B3 — CONSTRAINT CROSS-REFERENCE TABLE**

| Constraint Type | Q1 Finding | Q2 Finding | Q3 Finding | Migration Response | Residual Risk |
|-----------------|-----------|-----------|-----------|-------------------|---------------|
| NOT NULL | | | | | |
| FOREIGN KEY | | | | | |
| UNIQUE | | | | | |
| CHECK | | | | | |

Every registry type must appear as a row. A registry type absent from this table = cross-reference gap. Residual Risk: NONE CONFIRMED if all instances addressed by the migration.

---
