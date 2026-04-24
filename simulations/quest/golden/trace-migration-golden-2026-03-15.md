# trace-migration Golden — QU5 Simplification Pass
**Date:** 2026-03-15
**Base:** V-03 (DIRECTIVE register) + C-54/C-56 additions
**Original:** trace-migration-variate-R20-2026-03-15.md V-03 (1,286 words)
**Result:** 991 words (23% reduction)

---

## Simplification Report

### What was removed and why

| Removed | Words | Reason |
|---------|-------|--------|
| "The inertia-cost commitment is not a Phase A framing section — it is an architectural premise that precedes the analytical pipeline." | 22 | Redundant with the preceding sentence in DIRECTIVE A-0 |
| "The baseline must be established before any CONSTRAINT TYPE REGISTRY content is written." | 14 | Redundant: "before any constraint enumeration" in the same directive already covers this |
| "*DIRECTIVE A-0 compliance position: this section precedes PARSE PHASE and all constraint enumeration.*" italic line | 12 | Section IS in that position; annotation merely restates the directive |
| "Three-part structure expressed as a COST LEDGER table:" | 7 | Implied by the table immediately following |
| "Row (a) must name the structural source." | 7 | Already covered by "Re-identify the infrastructure substrate" in the same gate |
| Second verbatim occurrence of structural incompleteness verdict after fill-in template | 26 | Duplicate of the verdict already stated in DIRECTIVE B-1a above |
| DIRECTIVE B-1a example clause: "that the `(BINARY FIELD)` annotation makes the gate condition interpretable at this ENTRY REFERENCE position without consulting the EXIT BLOCK" | 22 | Self-documenting property already present in the fill-in template text |
| DIRECTIVE B-2 example: "for example: 'This section closes the STATUS QUO COST FRAME opened before the parse phase.'" | 18 | The WRITE instruction is clear without an example; the fill-in carries the pattern |
| "Then provide the cross-role causal chain demonstrating the accumulated cost." | 13 | Implied by the B2 structure that follows |
| "the cross-role chain provides the evidence but does not name the frame closure" | 14 | Explanatory aside — the infraction condition is sufficient |
| EXIT BLOCK annotation sentence (condensed 33→19 words) | 14 | Shortened while preserving both-anchors-independent claim |
| PROTOCOL COUNT MANIFEST section header annotation | 7 | "before B1" redundant — manifest already appears before B1 in the structure |

**Total removed:** ~176 words of redundant/explanatory text

### What was added (net new, for C-54 and C-56)

| Added | Words | Criterion |
|-------|-------|-----------|
| "Everything that follows operates within this frame. The frame closes at B2." | 14 | C-56 (universal scope claim) |
| "— and is not positioned as the STATUS QUO COST FRAME close" in DIRECTIVE B-2 | 12 | C-54 (absent closure = named structural failure) |

**Total added:** 26 words

### Net change: 1,286 → 991 words (-295 words, -23%)

### Essential criteria verification (C-01 through C-05)

| Criterion | Passes? | Carrier |
|-----------|---------|---------|
| C-01 Before/After State | ✅ YES | Checklist items "Schema state before migration" + "Schema state after migration" + B1 table |
| C-02 Data Loss Path | ✅ YES | Checklist: "Data loss path: transformation, truncation, or drop that loses rows or precision" |
| C-03 Constraint Violation Analysis | ✅ YES | Four per-constraint analysis fields per role (NOT NULL / FK / UNIQUE / CHECK) |
| C-04 Missing Default Detection | ✅ YES | Checklist: "Missing default: new NOT NULL without DEFAULT on a non-empty table" |
| C-05 Chronological Step Ordering | ✅ YES | B1 migration execution summary table; Q1 → Q2 → Q3 follows schema layer order |

**All essential criteria: PASS**

### Key aspirational criteria preserved or added

| Criterion | Status | How |
|-----------|--------|-----|
| C-51 Pre-parse frame positioning | ✅ | DIRECTIVE A-0: "before the PARSE PHASE and before any constraint enumeration" |
| C-52 B2 as explicit frame close | ✅ | DIRECTIVE B-2: "WRITE B2 as the explicit close of the STATUS QUO COST FRAME" |
| C-53 ENTRY REFERENCE structural incompleteness verdict | ✅ | DIRECTIVE B-1a verbatim: "An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete" |
| C-54 Absent closure = named failure | ✅ ADDED | DIRECTIVE B-2: "is not positioned as the STATUS QUO COST FRAME close" |
| C-55 Placement as DIRECTIVE infraction | ✅ | DIRECTIVE A-0: "violates this directive" |
| C-56 Universal scope claim | ✅ ADDED | STATUS QUO COST FRAME opening: "Everything that follows operates within this frame" |

---

## Simplified Prompt Body

You are running a migration trace signal for: {{topic}}

---

**DIRECTIVE A-0 — STATUS QUO COST FRAME PLACEMENT**

> WRITE the STATUS QUO COST FRAME section first, before the PARSE PHASE and before any constraint enumeration. A STATUS QUO COST FRAME that first appears after constraint type enumeration has begun violates this directive.

---

### STATUS QUO COST FRAME

The Status Quo Cost is the damage the current schema state is already inflicting without the migration. Everything that follows operates within this frame. The frame closes at B2.

**COST LEDGER**

| Row | Category | Current State | Accumulation Mechanism |
|-----|----------|---------------|------------------------|
| (a) | Schema substrate | [Infrastructure/schema condition only — not a downstream symptom or business outcome] | |
| (b) | Dependent process | [Business process or data flow breaking because of row (a)] | |
| (c) | Accumulation | [How row (b) damage compounds over time — name the trajectory] | |

**COST LEDGER SUBSTRATE GATE**
If row (a) names a business process outcome or financial metric rather than a schema or infrastructure condition: stop. Return to this section. Re-identify the infrastructure substrate.

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

Fill all rows. "None confirmed" valid — do not omit rows. Every listed type must appear in dedicated analytical fields in Phase A and Phase B.

---

### PHASE A — SCHEMA SUBSTRATE AND DOMAIN ANALYSIS

**Q1 — OPERATIONS / INFRASTRUCTURE ROLE**

Q1 analyzes the ALIGNMENT STATE substrate. Q1 runs first — shared infrastructure substrate must be established before Commerce and Finance consequence analysis proceeds.

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

**Phase A inertia-contrast example — Operations domain** (distinct from B2):
Three-part: (1) prior working state, (2) how migration breaks it, (3) concrete Operations consequence.

---

**Q2 — COMMERCE ROLE**

Apply full Q1 checklist and all four constraint-type fields to Commerce domain entities. Name specific tables.

---

**Q3 — FINANCE ROLE**

Apply full Q1 checklist and all four constraint-type fields to Finance domain entities. Name specific tables.

---

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

The `(BINARY FIELD)` annotation on PARSE GATE is self-documenting at this EXIT BLOCK. It appears identically at the Phase B ENTRY REFERENCE — both structural anchors carry it independently.

---

### PHASE B — SYNTHESIS AND CROSS-ROLE CONSEQUENCES

**DIRECTIVE B-1a — ENTRY REFERENCE STRUCTURAL COMPLETENESS**

> WRITE the ENTRY REFERENCE block as the first element of Phase B, before any other content. The block must carry the `(BINARY FIELD)` compound annotation on PARSE GATE. Immediately below, WRITE an inline rationale note stating the self-documenting property. An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete.

**ENTRY REFERENCE — PHASE A TO PHASE B**

```
PARSE GATE (BINARY FIELD) = OPEN required
ALIGNMENT STATE = SATISFIED required
```

*[WRITE inline rationale here: the `(BINARY FIELD)` annotation on PARSE GATE makes the binary constraint type self-documenting at this position. A reader consulting only Phase B's opening block sees both the required state (OPEN) and the constraint type (BINARY FIELD) without cross-referencing Phase A's EXIT BLOCK.]*

---

**PROTOCOL COUNT MANIFEST**

| Gate Name | Block Location | Required State | Blocks Transition? |
|-----------|----------------|----------------|-------------------|
| PARSE GATE (BINARY FIELD) | Phase A-to-B EXIT BLOCK | OPEN | Yes — Phase B entry |
| PARSE GATE (BINARY FIELD) | Phase A-to-B ENTRY REFERENCE | OPEN | Yes — Phase B continuation |
| ALIGNMENT STATE | Phase A-to-B EXIT BLOCK | SATISFIED | Yes — Phase B entry |
| COST LEDGER SUBSTRATE GATE | Phase A body (post-COST LEDGER) | PASS | Yes — Q1 entry |

**Completeness rule:** A gate named in any BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position but absent from this manifest = incomplete registry. Apply this rule to detect omissions — do not rely on cross-document search. Check this rule against all gate-bearing blocks before proceeding to B1.

---

**B1 — MIGRATION EXECUTION SUMMARY**

| Entity | Pre-Migration State | Migration Action | Post-Migration State | Net Data Effect |
|--------|--------------------|--------------------|---------------------|-----------------|

Net Data Effect values: NO LOSS · TRANSFORMATION LOSS · ROW LOSS · PRECISION LOSS · NO CHANGE

---

**DIRECTIVE B-2 — STATUS QUO COST FRAME CLOSURE AT B2**

> WRITE B2 as the explicit close of the STATUS QUO COST FRAME established before the parse phase. The first sentence of B2 must name B2 as the STATUS QUO COST FRAME close. A B2 section that provides a cross-role causal chain without an explicit STATUS QUO COST FRAME closure statement fails this directive — and is not positioned as the STATUS QUO COST FRAME close.

**B2 — CROSS-ROLE CAUSAL CHAIN**

*[STATUS QUO COST FRAME CLOSE: state that this section closes the STATUS QUO COST FRAME opened before the parse phase.]*

Cross-role causal chain:

1. **Shared substrate**: Schema state or migration-step dependency matching ALIGNMENT STATE substrate (same class as COST LEDGER row (a)).
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
