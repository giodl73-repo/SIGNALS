Written to `simulations/quest/golden/trace-migration-golden-2026-03-14.md`.

Key structural decisions in the document:

- **Prompt body**: verbatim from the QU5-simplified V-03 (991 words, 23% reduction from the R20 V-03 at 1,286 words)
- **"What made it golden"** captures the five patterns that are V-03-specific and not present in V-01: the DIRECTIVE register, absent-verdict symmetry (C-53/C-54 both closed), enforcement-register elevation for C-55, the universal scope claim for C-56, and the counter-intuitive result that simplification increased criterion coverage
- **Rubric summary** is organized in the same tier structure as v19 — Essential (5), then Aspirational grouped by cluster, with C-51 through C-56 broken out as their own chain and annotated with which rubric version introduced each

The C-33 (pre-role enforcement block) is the one criterion V-03 still FAILs in Round 20 — it's listed in the rubric summary but V-03's score reflects that miss.
hema condition only — not a downstream symptom or business outcome] | |
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

## What Made It Golden

**1. DIRECTIVE register with named violation conditions.**
V-03 replaced advisory framing with imperative directives — DIRECTIVE A-0, B-1a, B-2 — each paired with an explicit failure statement. "Violates this directive," "is structurally incomplete," "fails this directive" convert aspirational misses into named block-level failures. V-01 used narrative momentum to imply the same requirements without ever stating what non-compliance looks like.

**2. Absent-verdict symmetry across both enforcement chains.**
C-53 (ENTRY REFERENCE) and C-54 (B2 FRAME CLOSURE) follow the same structure: requirement → present-form instruction → named absence-verdict. V-03 is the only variation where both chains are closed: "An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete" (C-53) and "is not positioned as the STATUS QUO COST FRAME close" (C-54). V-01 carries the annotation and the closure instruction but not the absence verdicts at either position.

**3. STATUS QUO COST FRAME placement as DIRECTIVE infraction (C-55).**
Late placement is named as a directive violation, not an aspirational miss. "A STATUS QUO COST FRAME that first appears after constraint type enumeration has begun violates this directive." This enforcement-register distinction — infraction vs. miss — is precisely what C-55 tests. V-01 placed the frame correctly through ordering but never named late placement as a violation.

**4. Universal scope claim at frame open (C-56).**
"Everything that follows operates within this frame. The frame closes at B2." declares the STATUS QUO COST FRAME's coverage domain at the moment of opening, not at the close. V-01 established the open/close pair but left the scope implicit — a reader could infer the frame bounded only the COST LEDGER. V-03's universal scope claim makes the architecture a stated property of the output rather than an emergent one.

**5. Simplification compounded the signal density.**
The QU5 pass removed 176 words of redundant annotation (restated directives, implied headers, explanatory asides) while adding 26 words for C-54 and C-56. The result is 23% shorter but covers 6 new aspirational criteria. The DIRECTIVE register tolerates stripping because the violation conditions are load-bearing — everything explanatory surrounding them is not.

---

## Final Rubric Criteria Summary — v19 (56 criteria, 330 pts)

### Essential (5 criteria, 60 pts — all must pass)

| ID | Criterion |
|----|-----------|
| C-01 | Before/After State — schema state documented before and after migration |
| C-02 | Data Loss Path — transformation, truncation, or drop that loses rows or precision |
| C-03 | Constraint Violation Analysis — four per-constraint fields per role (NOT NULL / FK / UNIQUE / CHECK) |
| C-04 | Missing Default Detection — new NOT NULL without DEFAULT on non-empty table |
| C-05 | Chronological Step Ordering — B1 execution table; Q1 to Q2 to Q3 follows schema layer order |

### Aspirational (51 criteria, 270 pts)

**Architecture and gate structure (C-06 to C-21)**

| ID | Criterion |
|----|-----------|
| C-06 | Two-phase architecture: PARSE PHASE before Phase A |
| C-07 | Three-role structure: Q1 Operations / Q2 Commerce / Q3 Finance |
| C-08 | EXIT BLOCK at Phase A close |
| C-09 | ENTRY REFERENCE at Phase B open |
| C-10 | PROTOCOL COUNT MANIFEST present before B1 |
| C-11 | BOUNDARY PROTOCOL named section header at phase transition |
| C-12 | PARSE GATE present in EXIT BLOCK |
| C-13 | ALIGNMENT STATE present in EXIT BLOCK |
| C-14 | COST LEDGER SUBSTRATE GATE present after COST LEDGER |
| C-15 | ALIGNMENT STATE BINDING statement present |
| C-16 | Per-phase analytical checklist (8 items) present at Q1 |
| C-17 | Q2 and Q3 explicitly mandated to apply same checklist as Q1 |
| C-18 | Q1 runs first — substrate-before-consequences ordering stated |
| C-19 | B1 migration execution summary table with Net Data Effect values |
| C-20 | B3 canonical cross-reference table covers all four constraint types |
| C-21 | Binary gate at Phase A-to-B transition — PARSE GATE is BINARY FIELD |

**Constraint registry and coverage (C-22 to C-32)**

| ID | Criterion |
|----|-----------|
| C-22 | CONSTRAINT TYPE REGISTRY present in parse phase before Phase A |
| C-23 | All four constraint types listed as rows in registry |
| C-24 | "None confirmed" valid — no omission of registry rows |
| C-25 | Every registry type appears in dedicated fields across all role sections |
| C-26 | Per-entity rollback path field in analytical checklist |
| C-27 | Three-part inertia-contrast example present (Phase A, distinct from B2) |
| C-28 | Per-constraint-type dedicated fields: NOT NULL, FK, UNIQUE, CHECK in separate slots per role |
| C-29 | Cross-role checklist coverage: Q2/Q3 explicitly mandated to apply full Q1 checklist |
| C-30 | Distinct Phase A and Phase B inertia examples — distinctness required |
| C-31 | CONSTRAINT TYPE REGISTRY in parse phase before Phase A role sections |
| C-32 | B3 canonical table includes all four constraint types as rows |

**Pre-role enforcement (C-33)**

| ID | Criterion |
|----|-----------|
| C-33 | Named pre-role enforcement block before Q1 with explicit scoping-prohibition language |

**Boundary protocol completeness (C-34 to C-50)**

| ID | Criterion |
|----|-----------|
| C-34 | EXIT BLOCK at Phase A close AND ENTRY REFERENCE at Phase B open — both present |
| C-35 | BOUNDARY PROTOCOL as named section header at phase transition |
| C-36 | Named STATUS QUO COST FRAME section before Q1 |
| C-37 | PROTOCOL COUNT MANIFEST table before B1 |
| C-38 | COST LEDGER table with three named rows (a)/(b)/(c) |
| C-39 | B2 has: shared substrate + Commerce consequence + Finance consequence + causal link |
| C-40 | Q1 = OPERATIONS / INFRASTRUCTURE ROLE runs first |
| C-41 | Row (a) constraint: infrastructure or schema condition only — not a business process outcome |
| C-42 | ALIGNMENT STATE binding statement names three artifacts to same condition class |
| C-43 | COST LEDGER SUBSTRATE GATE: wrong-category row (a) = stop, return, re-identify |
| C-44 | ALIGNMENT STATE listed as condition in Phase A-to-B EXIT BLOCK |
| C-45 | MANIFEST includes: PARSE GATE (EXIT), PARSE GATE (ENTRY REF), ALIGNMENT STATE, COST LEDGER SUBSTRATE GATE |
| C-46 | `(BINARY FIELD)` annotation on PARSE GATE at ENTRY REFERENCE position |
| C-47 | Manifest completeness rule: gate named but absent from manifest = incomplete registry |
| C-48 | Inline rationale note at ENTRY REFERENCE position — self-documenting property named |
| C-49 | Completeness rule accompanied by action directive: "do not rely on cross-document search" |
| C-50 | Completeness rule names three block types: BOUNDARY PROTOCOL, EXIT BLOCK, ENTRY REFERENCE |

**STATUS QUO COST FRAME chain (C-51 to C-56)**

| ID | Criterion | Introduced |
|----|-----------|------------|
| C-51 | STATUS QUO COST FRAME precedes parse phase and all constraint enumeration | v18 |
| C-52 | B2 explicitly named as STATUS QUO COST FRAME close | v18 |
| C-53 | ENTRY REFERENCE without inline rationale = named structural incompleteness verdict | v18 |
| C-54 | Absent or placeholder FRAME CLOSURE STATEMENT at B2 = named structural failure | v19 |
| C-55 | Late STATUS QUO COST FRAME placement named as DIRECTIVE infraction (not aspirational miss) | v19 |
| C-56 | Universal scope claim at frame open: "Everything that follows operates within this frame" | v19 |

---

*Golden at Round 20. Simplification: PASS (23% reduction, 991 words). All 5 essential criteria pass. All 6 aspirational criteria C-51 through C-56 pass.*
