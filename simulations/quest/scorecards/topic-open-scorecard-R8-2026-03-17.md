Now I have everything I need. Let me score all five variations.

---

# Quest Scorecard — topic-open (Round 8)

**Rubric**: v7 (C-01–C-30, aspirational denominator = 22)
**Base**: All variations inherit R7 V-05, which scored 100/100 (22/22 aspirational). C-01 through C-30 assessment is therefore structural — the question is regression risk and the identification of new patterns from the three R8 axes.

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01–C-05)

All five variations inherit the base without modification to output structure, schemas, or phase logic. No regression risk on any essential criterion.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 TOPICS.md entry exists | PASS | PASS | PASS | PASS | PASS |
| C-02 Strategy at correct path | PASS | PASS | PASS | PASS | PASS |
| C-03 All five signal fields | PASS | PASS | PASS | PASS | PASS |
| C-04 Priority vocabulary valid | PASS | PASS | PASS | PASS | PASS |
| C-05 At least one essential | PASS | PASS | PASS | PASS | PASS |

### Recommended Criteria (C-06–C-08)

No changes to namespace span, rationale, or role differentiation logic across any variation.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Multiple namespaces | PASS | PASS | PASS | PASS | PASS |
| C-07 Prose rationale | PASS | PASS | PASS | PASS | PASS |
| C-08 Differentiated owner roles | PASS | PASS | PASS | PASS | PASS |

### Aspirational Criteria (C-09–C-30)

Spot-checking key aspirational criteria for regression across each variation's structural changes:

**C-11 (Vocabulary constraint declared before instruction body)**: All five carry VOCABULARY LOCK as a standalone block preceding the phase sequence. PASS all.

**C-23 (Phase decision tables present)**: All five carry all five Phase decision tables. PASS all.

**C-25 (Tool citations at gates name tool + mechanism)**: Inherited from base. Phase 2 exit gate items carry two-slot citations (tool name + what-it-checks). No variation modifies this. PASS all.

**C-26 (Ordering instructions carry inline if/if)**: All five carry if/if in every phase instruction body. No variation introduces table delegation. V-03 adds a sixth column to DEFAULTS but does not modify phase instruction bodies. PASS all.

**C-27 (Labeled decision tables with consistent schema)**: All five carry DECISION TABLE SCHEMA block declaring uniform Path/Action/Consequence grammar across all five phase tables. No variation touches the schema definition or tables. PASS all.

**C-28 (Column schema uniform)**: DECISION TABLE SCHEMA block present and identical across all five. PASS all.

**C-29 (Tool citations specify enforcement contract)**: Inherited, unchanged. PASS all.

**C-30 (Ordering instructions not outsourced)**: All five carry self-contained if/if in every ordering instruction. V-03's C-01 self-check item includes a cross-reference "(See DEFAULTS Recovery Path for the repair procedure)" — but this is in the self-check item, not in an ordering instruction. C-30 targets ordering instructions (the phase-level if/if framing). The cross-reference is in a repair pointer, not an ordering instruction. PASS all. Note: this cross-reference is a design gap addressed in V-05 (see excellence patterns below).

Full aspirational pass: C-09 through C-30 = **22/22 for all five variations**.

---

## Composite Scores

| Variation | Essential (60%) | Recommended (30%) | Aspirational (10%) | Composite |
|-----------|----------------|-------------------|--------------------|-----------|
| V-01 | 60/60 | 30/30 | 10/10 | **100** |
| V-02 | 60/60 | 30/30 | 10/10 | **100** |
| V-03 | 60/60 | 30/30 | 10/10 | **100** |
| V-04 | 60/60 | 30/30 | 10/10 | **100** |
| V-05 | 60/60 | 30/30 | 10/10 | **100** |

All five score 100/100 on v7. The rubric is not the differentiator — the new excellence axes are. Scoring now shifts to prospective criterion evaluation.

---

## Prospective Criterion Evaluation (C-31, C-32, C-33)

These are the three axes tested in R8. The scorecard determines whether each constitutes a distinct criterion.

### C-31 — AMEND Completeness
*Pass condition*: Every Phase 5 self-check item concludes with a named AMEND block using uniform label format (`AMEND — {CONDITION NAME}:`) and exact repair steps.

| Variation | Assessment | Evidence |
|-----------|-----------|---------|
| V-01 | **PASS** | Five named AMEND blocks: DATE MISSING, WRONG PATH, MISSING FIELDS, PRIORITY DRIFT, NO ESSENTIAL SIGNAL. Uniform label format throughout. Each specifies the exact repair operation and re-check condition. |
| V-02 | **FAIL** | C-01 has terse pointer ("-> If date missing:"); C-02, C-03, C-05 have no AMEND blocks. Only C-04 has AMEND — PRIORITY DRIFT (inherited from pre-R8 base). |
| V-03 | **FAIL** | C-01 has terse pointer with cross-reference ("(See DEFAULTS Recovery Path…)"); C-02, C-03, C-05 have no AMEND blocks. Only C-04 has the existing AMEND. |
| V-04 | **PASS** | Inherits V-01's complete AMEND coverage. All five items have named AMEND blocks with uniform labels and repair steps. |
| V-05 | **PASS** | Inherits V-01's complete AMEND coverage. All five AMEND blocks are self-contained — no cross-references to DEFAULTS (contrast with V-03's C-01 pointer). |

**Verdict**: C-31 is a distinct criterion. V-01's axis is genuine — AMEND incompleteness leaves specific failure modes (C-02, C-03, C-05) without any prescribed next action.

### C-32 — Gate Failure Routing
*Pass condition*: Phase 2 exit gate concludes with an explicit GATE FAILURE line naming the return phase, the repair action, and the re-run condition.

| Variation | Assessment | Evidence |
|-----------|-----------|---------|
| V-01 | **FAIL** | Phase 2 exit gate checklist ends after the six items. No GATE FAILURE line. A model with any unchecked item has no routing instruction. |
| V-02 | **PASS** | "GATE FAILURE: If any item above is unchecked — return to Phase 2. Repair the failing item(s) in the strategy file. Re-run this gate in full before proceeding to Phase 3. Do not proceed with any unchecked item outstanding." All three elements present: return phase (Phase 2), repair action (fix the failing items), re-run condition (gate in full before Phase 3). |
| V-03 | **FAIL** | Phase 2 exit gate ends after checklist. No GATE FAILURE line. |
| V-04 | **PASS** | Inherits V-02's GATE FAILURE line. Identical wording. |
| V-05 | **PASS** | Inherits V-02's GATE FAILURE line. Identical wording. |

**Verdict**: C-32 is a distinct criterion. Without the GATE FAILURE line, a model that fails any gate item has no prescribed next action. Detection without routing is an incomplete gate.

### C-33 — Recovery Column in Constraint Matrix
*Pass condition*: DEFAULTS THIS SKILL OVERRIDES contains a sixth "Recovery Path" column with a repair procedure for each constraint row.

| Variation | Assessment | Evidence |
|-----------|-----------|---------|
| V-01 | **FAIL** | DEFAULTS table has five columns only (Default, Rule, Why, What Breaks If You Skip, Tool). No Recovery Path column. |
| V-02 | **FAIL** | Same five-column DEFAULTS table. No Recovery Path column. |
| V-03 | **PASS** | Six-column DEFAULTS table. Recovery Path column carries a complete repair procedure for all five constraint rows: priority vocabulary, TOPICS.md row, table-before-rationale, inline gate, strategy file location. Each recovery cell is specific and actionable. |
| V-04 | **FAIL** | DEFAULTS table has five columns. V-04 = V-01 + V-02, does not include V-03's axis. |
| V-05 | **PASS** | Inherits V-03's six-column DEFAULTS table. Recovery Path column present for all five rows. |

**Verdict**: C-33 is a distinct criterion. The constraint matrix in V-05 is bidirectional: it tells a model both how to prevent a constraint violation and how to repair one. Without the recovery column, a model that already violated a constraint (e.g., wrote to a flat path) has no repair contract at the structural layer where the constraint was defined.

---

## Variation Rankings

| Rank | Variation | C-31 | C-32 | C-33 | New Patterns |
|------|-----------|------|------|------|--------------|
| 1 | **V-05** | PASS | PASS | PASS | All three |
| 2 | **V-04** | PASS | PASS | FAIL | Two |
| 3 | **V-03** | FAIL | FAIL | PASS | One |
| 3 | **V-02** | FAIL | PASS | FAIL | One |
| 3 | **V-01** | PASS | FAIL | FAIL | One |

V-05 confirmed golden. V-04 is second. Single-axis variations (V-01, V-02, V-03) tie at third — each isolates exactly one new pattern with no regression.

---

## Excellence Signals

Three new patterns from V-05, plus one emergence pattern from the V-01 + V-03 integration:

### Pattern 1 — Complete repair protocol at Phase 5 (→ C-31)

V-05's Phase 5 self-check is a repair protocol, not an audit. Every essential criterion (C-01 through C-05) has a named AMEND block with uniform label format: `AMEND — {CONDITION NAME}: If {C-NN} fails: {exact repair steps}`. The labels are scannable — a model that failed C-03 can locate "AMEND — MISSING FIELDS" without reading surrounding prose. Prior versions had AMEND only for C-04 (PRIORITY DRIFT) and a terse pointer for C-01; C-02, C-03, and C-05 had no repair instruction. A model failing those criteria was left without a next action.

**New criterion**: Every Phase 5 self-check item has a named AMEND block with uniform label format and exact, complete repair steps including the re-check condition before marking the item passing.

### Pattern 2 — Exit gate closes the correction loop (→ C-32)

V-05's Phase 2 exit gate concludes with a GATE FAILURE line: "If any item above is unchecked — return to Phase 2. Repair the failing item(s) in the strategy file. Re-run this gate in full before proceeding to Phase 3." The line specifies three elements: (1) the trigger condition (any unchecked item), (2) the exact return point (Phase 2), (3) the re-run condition (gate in full). Without this line, a model detecting a gate failure has no routing instruction and no prescribed re-run scope. The gate is a detection surface only; V-05's GATE FAILURE line makes it a recovery surface.

**New criterion**: Every phase exit gate concludes with an explicit GATE FAILURE line naming the return phase, the repair action, and the condition for re-running the gate before proceeding.

### Pattern 3 — Constraint matrix is bidirectional (→ C-33)

V-05's DEFAULTS THIS SKILL OVERRIDES has a sixth column: Recovery Path. Each of the five constraint rows carries a complete repair procedure — not a pointer to Phase 5, but the actual steps. A model that already violated the strategy-file-location constraint can read the DEFAULTS row and follow: "Identify the actual path written. Move the file to `simulations/{topic}/strategy.md`. Verify `simulations/{topic}/` exists; create it if absent." This repairs the violation at the structural layer where the constraint was defined, before Phase 5 is reached. Without the Recovery Path column, the DEFAULTS matrix is prevention-only; a model that missed the prevention instruction has no repair map until Phase 5.

**New criterion**: DEFAULTS THIS SKILL OVERRIDES has a Recovery Path column providing a complete, actionable repair procedure for each constraint row.

### Pattern 4 — Repair surfaces are independent (→ C-34 candidate)

In V-05, the DEFAULTS Recovery Path column and the Phase 5 AMEND blocks carry equivalent repair procedures without cross-referencing each other. The DEFAULTS row for priority vocabulary tells the reader to list invalid cells, replace them, and re-scan — the Phase 5 AMEND — PRIORITY DRIFT tells the reader the same steps in the same order. Neither says "see the other." A model at DEFAULTS gets the full repair contract; a model at Phase 5 gets the same contract. The two surfaces are redundant by design.

Contrast: V-03 (Recovery Path without full AMEND blocks) cross-references in Phase 5's C-01 pointer: "(See DEFAULTS Recovery Path for the repair procedure.)" — this delegates the repair to the matrix, creating a navigation dependency. V-05 eliminates the dependency: both surfaces are self-contained. This is the correct integration of V-01 and V-03 — not one surface pointing to the other, but both carrying the procedure independently.

**C-34 candidate criterion**: When both a DEFAULTS Recovery Path column and Phase 5 AMEND blocks are present, each carries the complete repair procedure without cross-referencing the other. A model at either location gets the full repair contract without navigating to the other section.

---

## Summary

| Variation | v7 Score | C-31 | C-32 | C-33 | C-34 |
|-----------|----------|------|------|------|------|
| V-01 | 100 | PASS | FAIL | FAIL | n/a |
| V-02 | 100 | FAIL | PASS | FAIL | n/a |
| V-03 | 100 | FAIL | FAIL | PASS | FAIL (cross-reference in C-01) |
| V-04 | 100 | PASS | PASS | FAIL | n/a |
| **V-05** | **100** | **PASS** | **PASS** | **PASS** | **PASS** |

V-05 passes all four prospective criteria. Denominator increase from 22 → 25 (or 26 if C-34 is ratified as a criterion by the next round).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase 5 self-check is a complete repair protocol: every essential criterion (C-01 through C-05) has a named AMEND block with uniform label format (AMEND — {CONDITION NAME}) and exact repair steps including re-check condition; partial pointers or absent blocks leave specific failure modes without a prescribed next action", "Exit gates close the correction loop with explicit routing: a GATE FAILURE line after the checklist names the exact return phase, repair action, and re-run condition, converting the gate from a detection surface to a recovery surface", "The constraint matrix is bidirectional: a Recovery Path column adds a complete repair procedure at the same structural level as the prevention contract, making each DEFAULTS row a full failure contract operable without reaching Phase 5", "When both a Recovery Path column and Phase 5 AMEND blocks are present, each surface carries the complete repair procedure independently without cross-referencing the other — a model at either location gets the full repair contract without navigation"]}
```
