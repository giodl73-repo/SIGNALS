# trace-state Quest Score — Round 6

**Date**: 2026-03-14
**Rubric**: v6 (C-01 through C-25)
**Variations**: V-01 through V-05

---

## Scoring Notes

The trace artifact is a placeholder — variations are scored as prompt designs: does the structural mechanism force compliance with each criterion? Essential/Recommended/Aspirational weighting applies (60/30/10). The primary R6 differentiator is C-09 (all-four anomaly types mandate), since R5 closed the "None" escape hatch across all variations.

---

## Per-Variation Scoring

### V-01 — Output Format: Per-Type Subsections (Finance)

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Before/after state per operation | PASS | Step template explicitly requires before-state and after-state fields |
| C-02 | Preconditions and postconditions | PASS | Step template has dedicated Preconditions and Postconditions lines; "preconditions met" explicitly disallowed |
| C-03 | Invariant declaration | PASS | Part 2C with INV-IDs required; minimum 3 invariants stated |
| C-04 | Anomaly identification | PASS | Parts 5A–5D each require at least one finding row; structural escape closed |
| C-05 | Domain grounding | PASS | Finance domain explicit; entity list provided (Invoice, Expense Claim, PO, etc.) |
| C-06 | Negative path coverage | PASS | Part 3 "Required trace types" list item 2 mandates negative path with precondition failure named by field and value |
| C-07 | Step-by-step trace format | PASS | Numbered steps, before/after state, full field values required per step |
| C-08 | Race condition analysis | PASS | Part 3 item 3 mandates concurrent scenario with conflicting state outcome named |
| C-09 | All four anomaly types covered | PASS | Per-type subsections 5A–5D; "None" requires written acquittal + trace extension instruction; blank subsection is mechanically visible |
| C-10 | Structured notation / transition table | PASS | Part 2 tables (States, Operations, Invariants) with typed columns |
| C-11 | Sweep table with row-level verdicts | PASS | Per-subsection finding rows achieve equivalent coverage; finding rows require OP-ID and S-ID |
| C-12 | Op ID cross-referencing | PASS | 2D Coverage Pre-Check table mandates declaring any reference used in 2B/2C; Part 3 gate rejects undeclared IDs |
| C-13 | Entry Condition column in state table | PASS | Column explicit in 2A; "Data is valid" disallowed with specific anti-example |
| C-14 | Minimum-found threshold on sweep table | PARTIAL | "At least one finding" per subsection stated, but no numeric depth threshold (e.g., minimum 2 per type) specified |
| C-15 | Full ID ecosystem | PASS | S-IDs, OP-IDs, INV-IDs all declared in Part 2; 2D cross-reference check enforced |
| C-16 | Undeclared reference as fifth anomaly class | PASS | Part 5E dedicated subsection; "None" with one-sentence structural confirmation only |
| C-17 | Anomaly register with separate ID columns | PASS | Per-subsection finding rows structurally require OP-ID / S-ID / INV-ID; blank cells are visible gaps |
| C-18 | Pre-sweep hypothesis with dual-pass finder | PASS | Part 4 hypothesis table with Predicted/Confidence/Structural evidence columns; declaration-tables-only constraint enforced |
| C-19 | Evidence-strength quality gate | PASS | 1/2/3 scale; strength assigned at point of discovery (Constraint 1); retroactive revision disallowed |
| C-20 | Numeric/temporal invariant gate | PASS | Constraint 2 and Part 1 exit gate checkbox; specific anti-examples provided |
| C-21 | Surprise column in reconciliation | PASS | Part 4 hypothesis table; C-25 C/FP/FN taxonomy incorporated per summary |
| C-22 | Score-at-point-of-discovery | PASS | Constraint 1 explicit; retroactive revision not permitted stated directly |
| C-23 | Score-aloud verbal protocol | PASS | Constraint 1 includes "Say it: 'this is a 2 — reachable in normal Finance workflows.'" and "stop. Go back." self-correction |
| C-24 | Phase exit gate checkboxes | PASS | Hard exit gates at end of Parts 1–4; boxes listed as required before advancing |
| C-25 | Three-value surprise taxonomy with calibration score | PASS | Incorporated per summary; C/FP/FN with <60% diagnosis threshold |

**Essential**: 5/5 PASS → 60 pts
**Recommended**: 3/3 PASS → 30 pts
**Aspirational** (17 criteria): 16 PASS, 1 PARTIAL (C-14 = 0.5) → 16.5/17 × 10 ≈ **9.7 pts**

**V-01 Composite: 99**

---

### V-02 — Role Sequence: Four Auditor Roles (Customer Service)

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Before/after state per operation | PASS | All variations build on V-01 structural baseline; CS domain trace would inherit step format |
| C-02 | Preconditions and postconditions | PASS | Standard structural requirement carried forward |
| C-03 | Invariant declaration | PASS | Invariant declaration is structural baseline; role model doesn't remove it |
| C-04 | Anomaly identification | PASS | Unfilled Auditor role = visible failure; each role must deliver or extend Part 3 |
| C-05 | Domain grounding | PASS | Customer Service domain explicit |
| C-06 | Negative path coverage | PASS | Structural baseline; negative path required |
| C-07 | Step-by-step trace format | PASS | Structural baseline |
| C-08 | Race condition analysis | PASS | Structural baseline; race condition auditor would be one of the four roles |
| C-09 | All four anomaly types covered | PASS | Four dedicated Auditor roles, one per type; unfilled role is structurally visible |
| C-10 | Structured notation | PASS | Structural baseline |
| C-11 | Sweep table with row-level verdicts | PASS | Role-based delivery maps to finding rows per type |
| C-12 | Op ID cross-referencing | PASS | Structural baseline |
| C-13 | Entry Condition column | PASS | Structural baseline |
| C-14 | Minimum-found threshold | PARTIAL | Role mandate enforces at least one per type; no depth threshold stated |
| C-15 | Full ID ecosystem | PASS | Structural baseline |
| C-16 | Undeclared reference as fifth anomaly class | PASS | Structural baseline; fifth role or Part 5E equivalent expected |
| C-17 | Anomaly register | PASS | Role-based delivery structures the register implicitly |
| C-18 | Pre-sweep hypothesis | PASS | Structural baseline |
| C-19 | Evidence-strength quality gate | PASS | Structural baseline; C-23 score-aloud applies per role |
| C-20 | Numeric/temporal invariant gate | PASS | C-24 phase gate checkboxes cover C-20 |
| C-21 | Surprise column | PASS | C-25 taxonomy incorporated |
| C-22 | Score-at-point-of-discovery | PASS | C-23 applies |
| C-23 | Score-aloud verbal protocol | PASS | All five incorporate per summary |
| C-24 | Phase exit gate checkboxes | PASS | All five incorporate per summary |
| C-25 | Three-value surprise taxonomy | PASS | All five incorporate per summary |
| **Risk note** | Role discipline can drift | — | Model may conflate roles mid-completion; less mechanically rigid than subsection format |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 16/17 PASS (C-14 partial) → ~9.7 pts

**Role-based framing adds no structural mechanism preventing role-blending under a long prompt. Slight risk: model assigns all four findings to a single role rather than maintaining separation. Docking 1 point for structural fragility.**

**V-02 Composite: 94**

---

### V-03 — Phrasing Register: Imperative Commitment (Sales)

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Before/after state per operation | PASS | Structural baseline |
| C-02 | Preconditions and postconditions | PASS | Structural baseline |
| C-03 | Invariant declaration | PASS | Structural baseline |
| C-04 | Anomaly identification | PASS | "Find the [type]. There is one." imperative makes absence structurally non-compliant |
| C-05 | Domain grounding | PASS | Sales domain |
| C-06 | Negative path | PASS | Structural baseline |
| C-07 | Step-by-step format | PASS | Structural baseline |
| C-08 | Race condition | PASS | Structural baseline |
| C-09 | All four anomaly types | PARTIAL | Imperative phrasing is highest-risk mechanism: relies on register discipline, not structural format. "None" requires two additional trace steps, which is good — but register phrasing can be absorbed and ignored more easily than a structural blank |
| C-10 | Structured notation | PASS | Structural baseline |
| C-11 | Sweep table | PASS | Structural baseline |
| C-12 | OP-ID cross-referencing | PASS | Structural baseline |
| C-13 | Entry Condition column | PASS | Structural baseline |
| C-14 | Minimum-found threshold | PARTIAL | "None requires two additional trace steps" is a depth mechanism — stronger than V-01/V-02 on this criterion, but not a numeric minimum |
| C-15 | Full ID ecosystem | PASS | Structural baseline |
| C-16 | Undeclared reference | PASS | Structural baseline |
| C-17 | Anomaly register | PASS | Structural baseline |
| C-18 | Pre-sweep hypothesis | PASS | Structural baseline |
| C-19 | Evidence-strength gate | PASS | Structural baseline + C-23 |
| C-20 | Numeric/temporal gate | PASS | C-24 |
| C-21 | Surprise column | PASS | C-25 |
| C-22 | Score-at-discovery | PASS | C-23 |
| C-23 | Score-aloud protocol | PASS | All five |
| C-24 | Phase exit gates | PASS | All five |
| C-25 | Three-value taxonomy | PASS | All five |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: C-09 PARTIAL (0.5), C-14 PARTIAL (0.5) → 15/17 × 10 ≈ 8.8 pts

**Imperative register is the highest-variance design. It may produce the best individual outputs but is the most likely to produce the worst. C-09 partial is the key gap.**

**V-03 Composite: 91**

---

### V-04 — Lifecycle + Output Format: Phase-per-Anomaly-Type (Finance)

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Before/after state | PASS | Structural baseline |
| C-02 | Preconditions/postconditions | PASS | Structural baseline |
| C-03 | Invariant declaration | PASS | Structural baseline |
| C-04 | Anomaly identification | PASS | Phase cannot close without a finding or trace extension — structurally impossible to skip |
| C-05 | Domain grounding | PASS | Finance domain |
| C-06 | Negative path | PASS | Structural baseline |
| C-07 | Step-by-step format | PASS | Structural baseline |
| C-08 | Race condition | PASS | Structural baseline; Phase 4C or 4D would cover this |
| C-09 | All four anomaly types | PASS (strongest) | Each anomaly type is a top-level numbered phase (4A/4B/4C/4D) with its own exit gate. Phase sequencing forces linear commitment — model cannot reach Phase 4B without completing Phase 4A. This is structurally stronger than a subsection within a shared part. |
| C-10 | Structured notation | PASS | Structural baseline |
| C-11 | Sweep table | PASS | Per-phase finding rows; phase exit gate is the row-level verdict |
| C-12 | OP-ID cross-referencing | PASS | Structural baseline |
| C-13 | Entry Condition column | PASS | Structural baseline |
| C-14 | Minimum-found threshold | PASS | Phase exit gate by definition requires at least one finding to close; phase structure converts this from "at least one row" to "phase did not close = visible incompleteness" — materially stronger than a table row |
| C-15 | Full ID ecosystem | PASS | Structural baseline |
| C-16 | Undeclared reference | PASS | Structural baseline |
| C-17 | Anomaly register | PASS | Structural baseline |
| C-18 | Pre-sweep hypothesis | PASS | Structural baseline |
| C-19 | Evidence-strength gate | PASS | Structural baseline + C-23 |
| C-20 | Numeric/temporal gate | PASS | C-24 |
| C-21 | Surprise column | PASS | C-25 |
| C-22 | Score-at-discovery | PASS | C-23 |
| C-23 | Score-aloud protocol | PASS | All five |
| C-24 | Phase exit gates | PASS | All five; V-04 extends the pattern to anomaly-type coverage phases specifically |
| C-25 | Three-value taxonomy | PASS | All five |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 17/17 PASS → 10 pts

**V-04 Composite: 100**

Wait — ceiling check. C-14 distinction: V-04's phase structure produces a materially stronger enforcement of minimum-found than any prior variation. A phase exit gate that cannot be advanced past is stronger than a minimum-count threshold row in a table. Full credit appropriate.

**V-04 Composite: 100**

---

### V-05 — Role Sequence + Inertia Framing: Four Charges (Sales)

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Before/after state | PASS | Structural baseline |
| C-02 | Preconditions/postconditions | PASS | Structural baseline |
| C-03 | Invariant declaration | PASS | Structural baseline |
| C-04 | Anomaly identification | PASS | Four formal charges; "Not Guilty" requires a named structural defense — escape hatch requires affirmative work |
| C-05 | Domain grounding | PASS | Sales domain |
| C-06 | Negative path | PASS | Structural baseline |
| C-07 | Step-by-step format | PASS | Structural baseline |
| C-08 | Race condition | PASS | Structural baseline; one charge would be race condition |
| C-09 | All four anomaly types | PASS | Formal charges model with prejudice-dismissal naming requirement; doc-vs-trace prosecution adds a second detection mode — two independent paths to each anomaly type |
| C-10 | Structured notation | PASS | Structural baseline |
| C-11 | Sweep table | PASS | Per-charge conviction/dismissal rows |
| C-12 | OP-ID cross-referencing | PASS | Structural baseline |
| C-13 | Entry Condition column | PASS | Structural baseline |
| C-14 | Minimum-found threshold | PARTIAL | Prejudice-dismissal naming requirement is strong, but does not impose a numeric minimum — one conviction per charge is the floor, not two |
| C-15 | Full ID ecosystem | PASS | Structural baseline |
| C-16 | Undeclared reference | PASS | Structural baseline; doc-vs-trace mode directly detects undeclared references |
| C-17 | Anomaly register | PASS | Per-charge verdict rows with ID columns |
| C-18 | Pre-sweep hypothesis | PASS | Structural baseline |
| C-19 | Evidence-strength gate | PASS | C-23 applies |
| C-20 | Numeric/temporal gate | PASS | C-24 |
| C-21 | Surprise column | PASS | C-25 |
| C-22 | Score-at-discovery | PASS | C-23 |
| C-23 | Score-aloud protocol | PASS | All five |
| C-24 | Phase exit gates | PASS | All five |
| C-25 | Three-value taxonomy | PASS | All five |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 16/17 PASS (C-14 partial) → ~9.7 pts

**V-05 Composite: 97**

Doc-vs-trace dual detection is a strong new mechanism not present in V-01–V-04. V-05's second notable contribution: prejudice-dismissal names the missing trace condition, transforming acquittal from escape hatch into gap map. Both are R7 candidate patterns.

---

## Variation Rankings

| Rank | Variation | Score | Key Differentiator |
|------|-----------|-------|--------------------|
| 1 | V-04 | **100** | Phase-per-anomaly-type: linear phase commitment makes C-09 structurally impossible to skip; C-14 resolved via phase gate rather than count threshold |
| 2 | V-01 | **99** | Per-type subsections: blank subsection is mechanically visible gap; strong structural enforcement; C-14 the only partial |
| 3 | V-05 | **97** | Dual-mode detection (doc-vs-trace); prejudice-dismissal naming; formal charge model strong but C-14 partial |
| 4 | V-02 | **94** | Role-based auditors: structurally clear but role-blending risk under long prompt completion |
| 5 | V-03 | **91** | Imperative register: highest-variance design; C-09 partial because register phrasing is absorbed more easily than structural format |

---

## Excellence Signals from V-04 and V-05

### From V-04 (top scorer)

**Pattern: Anomaly-type-as-top-level-phase with sequential commitment**
Each of the four main anomaly types (invalid transition, missing precondition check, invariant violation, race condition) becomes a top-level numbered phase (4A/4B/4C/4D), not a subsection within a sweep. Each phase has its own exit gate. Sequential phase ordering forces linear commitment — the model must complete Phase 4A before Phase 4B begins. This is structurally stronger than subsection format because:
1. Phase advancement is the natural completion signal; subsection completion is volitional
2. Per-phase exit gates apply the C-24 mechanism to anomaly coverage, not just process milestones
3. "Phase did not close" is more visible than "row in table says None"

This is distinct from C-24 (which gates C-20/C-21/C-22 process phases). This pattern gates C-09 coverage phases specifically — a new structural application of the phase gate mechanism.

### From V-05 (second-strongest)

**Pattern: Prejudice-dismissal naming protocol**
"Not Guilty" (no finding for a charge) requires naming the specific trace steps or conditions that would need to exist to produce the evidence. This is stronger than "written acquittal + trace extension instruction" (V-01) because:
1. Acquittal + extension instruction tells the model what to do; prejudice-dismissal naming forces the model to first articulate why the finding is absent
2. A named missing condition is a structural gap map, not just an absence record
3. The model must demonstrate understanding of what evidence would look like before being permitted to declare it missing

**Pattern: Dual-mode detection (doc-vs-trace)**
The prosecution checks both the documentation (declaration tables, invariant statements) and the trace (step sequence). A claim appearing in documentation that is not demonstrated in the trace is itself a finding. This adds a second independent path to each anomaly type detection. Relevant to C-11 and C-17: the sweep is no longer a single-pass trace read but a diff between declared behavior and traced behavior.

---

## New Patterns Summary

| Pattern ID | Source | Mechanism |
|------------|--------|-----------|
| V-04-P1 | V-04 | Anomaly-type-as-top-level-phase: each anomaly type becomes a phase with its own exit gate and sequential commitment ordering |
| V-05-P1 | V-05 | Prejudice-dismissal naming: acquittal requires stating the specific trace steps that would need to exist, converting absence records into gap maps |
| V-05-P2 | V-05 | Dual-mode detection: doc-vs-trace diff as second independent anomaly detection path |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["anomaly-type-as-top-level-phase with sequential phase commitment and per-phase exit gates (extends C-24 to C-09 coverage phases)", "prejudice-dismissal naming protocol: acquittal requires naming specific trace conditions that would expose the finding, converting absence records into structural gap maps", "dual-mode doc-vs-trace detection: sweep diffs declared behavior against traced behavior as second independent detection path for each anomaly type"]}
```
