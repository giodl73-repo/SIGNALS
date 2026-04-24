# trace-migration Scoring — Round 15, Rubric v13

**Note:** Only V-01 and V-02 are provided. V-03 through V-05 are absent from the variation set; scoring covers the two supplied prompts only.

---

## V-01 — Role Sequence Axis: Operations-First Phase A

### Parse Phase

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-31 CONSTRAINT TYPE REGISTRY at parse time | **PASS** | Named block with all four rows explicitly mandated before domain-role analysis |
| C-28 Dedicated constraint-type structural slots | **PASS** | Four-column table with fixed taxonomy; no constraint type relegated to free-form field |

### Phase A Structure

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-36 Named STATUS QUO COST before Q1 | **PASS** | Named section placed before ROLE ANALYSIS ENFORCEMENT, before Q1 — structural entry condition |
| C-38 COST LEDGER three-row table | **PASS** | Three-row template (a)(b)(c) — completeness verifiable by row count |
| C-41 Row (a) infrastructure/schema condition | **PASS** | Explicit: "must name a schema state, migration-state dependency, or infrastructure constraint — not a revenue metric or Commerce process" — negative constraint enforced in prompt |
| C-27 At least one three-part inertia example | **PASS** | Three-part structure (current schema condition → dependent-process consequence → accumulation trajectory) in STATUS QUO COST |
| C-33 Named enforcement block before Q1 | **PASS** | "ROLE ANALYSIS ENFORCEMENT" block with explicit "DO NOT SCOPE OR SHORTEN / apply to ALL roles" language positioned before Q1 |
| C-29 Complete checklist in every domain-role section | **PASS** | Eight-item checklist in enforcement block explicitly applied to "ALL roles" — structural mandate, not suggestion |

### Role Ordering

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-40 Phase A Q1 = Operations/infrastructure role | **PASS** | Q1 = "Operations Migration Expert" (Q2 = Commerce, Q3 = Finance) — substrate role leads; Q1 explicitly tasked to "identify the shared infrastructure conditions that Commerce and Finance both depend on" |

### Gate / Boundary

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-21 Named binary gate at every phase transition | **PASS** | EXIT GATE blocks at Q1→Q2, Q2→Q3, A→B — all three transitions covered |
| C-17 Compound "(BINARY FIELD)" annotation | **PARTIAL** | Gates show `State: [OPEN / BLOCKED]` which is functional binary but does not carry the literal "(BINARY FIELD)" label at the definition site; pattern matches structurally, label absent |
| C-34 Bilateral EXIT BLOCK + ENTRY REFERENCE at both positions | **PASS** | EXIT BLOCKs at each phase-section boundary; ENTRY REFERENCE at Phase B entry naming PHASE_A_COMPLETE as required state |
| C-35 Named BOUNDARY PROTOCOL blocks (countable) | **PASS** | Three explicit "BOUNDARY PROTOCOL" headers in Phase B — countable without reading phase interiors |

### Phase B

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-37 PROTOCOL COUNT MANIFEST at Phase B entry | **PASS** | Named three-row table listing all boundaries, gate names, and states before any Phase B traversal |
| C-30 Distinct three-part inertia example in Phase B | **PASS** | B1 mandates "a migration step, system boundary, or cross-role dependency not used in the STATUS QUO COST section" — distinctness enforced |
| C-39 B2 explicit cross-role causal chain | **PASS** | B2 template requires: Operations substrate condition (named) → Commerce consequence (named) → Finance consequence (named) |
| C-32 Canonical table with all four constraint-type columns | **PASS** | B3 template shows all four columns: NOT NULL Risk, FK Violation, UNIQUE Violation, CHECK Violation |
| C-03 / C-04 / C-09 Correctness criteria | **PASS** | Structural design forces checklist coverage including zero-downtime (item 6), nullable risk, data loss paths |

### Three-Artifact Alignment Check (C-40 + C-41 joint condition)

B2 explicitly states: *"The substrate condition must be the same infrastructure state named in COST LEDGER row (a) and analyzed in Q1."* — the three-artifact binding (COST LEDGER row (a) → Phase A Q1 → B2 chain substrate) is structurally enforced in the prompt. This is the full joint pass condition for C-40 + C-41.

### V-01 Composite Score

| Category | Criteria Passing | Estimated Pts |
|----------|-----------------|---------------|
| Parse phase | 2/2 | ~13 |
| Phase A structure | 6/6 | ~40 |
| Role ordering (C-40) | 1/1 | 5 |
| Gate / boundary | 3.5/4 (C-17 partial) | ~24 |
| Phase B | 5/5 | ~33 |
| Remaining criteria (C-01–C-16, C-18–C-20, C-22–C-26, etc.) | estimated ~26/27 | ~130 |
| **Total** | **~40.5/41** | **~245/255** |

**V-01 Score: ~245/255 (96%)** — above golden (206); C-17 annotation format is the sole structural gap.

---

## V-02 — Inertia Framing Axis: Infrastructure-Anchored COST LEDGER

V-02 is a partial prompt — the provided template covers the PARSE PHASE and STATUS QUO COST sections only. No role sections (Q1/Q2/Q3), no EXIT BLOCKs, no Phase B structure appear in the shown text.

### Parse Phase

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-31 CONSTRAINT TYPE REGISTRY | **PASS** | Named block with four rows |
| C-28 Dedicated structural slots | **PASS** | Four-column table |

### Phase A Structure (Partial)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-36 Named STATUS QUO COST before Q1 | **PASS** | Explicit: "opens Phase A; appears before Q1" |
| C-38 COST LEDGER three-row table | **PASS** | Three-row table with named category column |
| C-41 Row (a) infrastructure/schema condition | **PASS** | Strong enforcement: explicit prohibition "must not name a revenue metric, a Commerce process disruption, or a Finance outcome"; includes conditional return-to-parse instruction |
| C-27 Three-part inertia example | **PASS** | "three-part inertia-contrast narrative" explicitly required after COST LEDGER |

### Not Present / Not Enforced

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-40 Q1 = Operations/infrastructure role | **FAIL** | No role ordering specified; axis hypothesis explicitly tests C-41 "independent of role ordering" — C-40 absent by design |
| C-33 Named enforcement block before roles | **ABSENT** | No role analysis enforcement section shown |
| C-29 Complete checklist in every role section | **ABSENT** | No role section structure present |
| C-21 / C-34 / C-35 Gates and boundary protocols | **ABSENT** | No EXIT BLOCK, ENTRY REFERENCE, or BOUNDARY PROTOCOL structures present |
| C-37 PROTOCOL COUNT MANIFEST | **ABSENT** | Phase B not specified |
| C-30 / C-39 / C-32 Phase B synthesis | **ABSENT** | Phase B structure absent |

### V-02 Composite Score

| Category | Criteria Passing | Estimated Pts |
|----------|-----------------|---------------|
| Parse phase | 2/2 | ~13 |
| Phase A entry (STATUS QUO COST, C-41) | 4/6 (C-33, C-29 absent) | ~26 |
| Role ordering | 0/1 | 0 |
| Gate / boundary | 0/4 | 0 |
| Phase B | 0/5 | 0 |
| Remaining criteria | ~12/27 (baseline correctness possible) | ~60 |
| **Total** | **~18/41** | **~99/255** |

**V-02 Score: ~99/255 (39%)** — well below golden; structural scaffold after COST LEDGER is absent from the prompt design. C-41 passes strongly; C-40 fails by axis design; remainder fails by omission.

---

## Rankings

| Rank | Variation | Score | Essential Pass |
|------|-----------|-------|---------------|
| 1 | V-01 — Operations-First Phase A | **~245/255 (96%)** | Yes |
| 2 | V-02 — Infrastructure-Anchored COST LEDGER | **~99/255 (39%)** | No |

*V-03 through V-05 not provided; ranking reflects supplied variations only.*

---

## Excellence Signals — V-01

**S-01: Gate guard condition as infrastructure-naming checkpoint.** V-01's Q1_COMPLETE exit gate carries the guard condition *"all changed entities traced; shared infrastructure conditions named."* This means the gate cannot be marked OPEN unless the substrate conditions B2 will reference already exist as named artifacts. This creates a structural dependency: B2's chain substrate is guaranteed by Q1's gate guard, not by editorial discipline. No prior variation made the gate guard condition carry infrastructure-naming semantics explicitly; prior gates guarded "all entities traced" without binding that to the shared-condition naming requirement.

**S-02: Negative constraint in COST LEDGER row (a) enforcement.** The instruction *"not a revenue metric or Commerce process"* is a structural prohibition, not a preference. V-02 also uses this pattern and strengthens it with a conditional return instruction ("If you cannot name a schema condition for row (a), return to the parse phase"). The negative constraint eliminates the most common failure mode for C-41 — defaulting to a business-process statement — by naming the failure explicitly before the slot is filled.

**S-03: Three-artifact alignment made explicit in B2.** V-01 directly states: *"The substrate condition must be the same infrastructure state named in COST LEDGER row (a) and analyzed in Q1."* Prior prompts relied on structural ordering to produce alignment; V-01 adds a binding constraint that makes cross-document consistency a named requirement, not an emergent property. This eliminates a class of C-40+C-41 failures where all three artifacts are present but reference different infrastructure domains.

---

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["Gate guard condition as infrastructure-naming checkpoint — Q1_COMPLETE guard condition requires 'shared infrastructure conditions named', binding B2 chain substrate existence to Q1 gate completion before Commerce analysis begins"]}
```
