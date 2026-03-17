Now I have all five variations. Let me score them.

---

# Scorecard — campaign-specify / Round 10 / Rubric v10

**Date**: 2026-03-17
**Rubric version**: v10 (29 aspirational; C-36 and C-37 are the two new criteria)
**Denominator**: 29 aspirational

---

## Scoring Framework

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 29 * 10)
```

---

## V-01 — Output Format: Table + "Satisfied" Cell Values, No Gate Anchor

**Hypothesis**: Isolation test — adds "satisfied" to table cells and table format, removes gate anchor (C-34). Confirms C-36 structural dependency on C-34.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Three artifacts produced | PASS | Write gates at end of Phase 1, 2, 3 enforce spec/proposal/pitch production |
| C-02 | Spec has all six required sections | PASS | Sections listed by name; "no skipping, no merging" instruction |
| C-03 | Proposal has 3+ options including do-nothing | PASS | "Option 1 MUST be named Do Nothing"; all five fields required per option |
| C-04 | Pitch covers three audience versions | PASS | Exec/Dev/Maker versions plus Anti-Positioning all required |
| C-05 | Cross-artifact consistency | PASS | Step 0c voice contracts anchor all three artifacts to the same Phase 0 outputs |

**Essential: 5/5**

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Spec self-review flags gaps | PASS | "'No gaps found' fails" explicit instruction |
| C-07 | Pitch contains anti-positioning section | PASS | "3-5 This is not... statements. Structurally separate" |
| C-08 | Proposal recommendation cites trade-off rationale | PASS | Defeating blocks require "specific trade-off traceable to a risk, effort, or cons field" |

**Recommended: 3/3**

### Aspirational Criteria (C-09 to C-37)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09–C-26 | Inherited (18 criteria) | PASS (all 18) | Same template infrastructure as R7 V-05 baseline |
| C-27 | Formal VCA section with preamble enumeration | PASS | COMPLETION INDEX preamble enumerates "four named sections: Artifact Existence Record, Phase Gate Audit, Citation Audit, and Voice Compliance Audit" |
| C-28 | Per-audience gate Pass/Fail verdicts | PASS | Step 3 has individual Exec/Dev/Maker gates with independent Pass/Fail |
| C-29 | Step 0c contract naming in Step 3 | PASS | Step 1 of gate explicitly copies Step 0c voice contracts by name; contract names present in gate setup even without parenthetical attribution |
| C-30–C-32 | Inherited (3 criteria) | PASS (all 3) | Same as R9 V-01 which passed these; structure unchanged |
| C-33 | Per-audience audit rows in VCA | PASS | Table has three rows: Exec, Dev, Maker |
| C-34 | Gate parenthetical with contract attribution | **FAIL** | Step 3 uses bare behavioral criteria: "Pass (opening names a business cost...)" — no contract name in parenthetical |
| C-35 | Per-audience audit rows with contract attribution | PASS | Table cell template: "Step 0c exec voice contract satisfied" — contract named inline |
| C-36 | Lexical verb consistency gate↔audit | **FAIL** | C-34 fails → no gate parenthetical verb exists → C-36 is structurally inapplicable; isolation test confirms dependency |
| C-37 | Table format with dedicated contract column | PASS | Three-column table: Audience / Verdict / Step 0c Contract Verified |

**Aspirational: 27/29** (misses C-34, C-36)

### Composite

```
(5/5 * 60) + (3/3 * 30) + (27/29 * 10) = 60 + 30 + 9.31 = 99.31
```

**V-01 composite: 99.31**

---

## V-02 — Output Format: Table + "Satisfied" Cell Values + Gate Anchor (Minimal 29/29 Synthesis)

**Hypothesis**: Minimal synthesis — R9 V-03 verb ("satisfied" in row attribution) combined with R9 V-02 structure (table format) and gate anchor from both. Single-axis change from R9 V-02: table cell values gain "satisfied".

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Write gates enforce artifact production |
| C-02 | PASS | All six sections named; no-skip/merge instruction |
| C-03 | PASS | Do Nothing named; all option fields required |
| C-04 | PASS | Three audience versions + Anti-Positioning required |
| C-05 | PASS | Step 0c contracts anchor all artifacts |

**Essential: 5/5**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "No gaps found fails" instruction |
| C-07 | PASS | Anti-Positioning section required |
| C-08 | PASS | Defeating blocks require traceable trade-off |

**Recommended: 3/3**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-26 | PASS (18) | Inherited baseline |
| C-27 | PASS | VCA section named; preamble enumerates four sections |
| C-28 | PASS | Per-audience gates with independent verdicts |
| C-29 | PASS | Step 1 copies contracts by name; Step 3 parentheticals open with contract name |
| C-30–C-32 | PASS (3) | Inherited |
| C-33 | PASS | Three-row VCA table |
| C-34 | PASS | Gate parentheticals: "Pass (Step 0c exec voice contract satisfied: ...)" — contract name opens parenthetical |
| C-35 | PASS | Cell template: "Step 0c exec voice contract satisfied" — contract attributed inline |
| C-36 | PASS | Gate verb "satisfied"; cell verb "satisfied" — lexical match |
| C-37 | PASS | Table: Audience / Verdict / Step 0c Contract Verified |

**Aspirational: 29/29**

### Composite

```
(5/5 * 60) + (3/3 * 30) + (29/29 * 10) = 60 + 30 + 10 = 100.00
```

**V-02 composite: 100.00**

---

## V-03 — Lifecycle Emphasis: Explicit Verb Consistency Instruction Before Audit Table

**Hypothesis**: V-02 template achieves 29/29 implicitly. V-03 adds a prose instruction paragraph before the table naming (a) the table format requirement, (b) the required verb "satisfied", and (c) the consistency relationship with the gate parenthetical.

### Essential / Recommended

Identical structure to V-02. **Essential: 5/5. Recommended: 3/3.**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-26 | PASS (18) | Inherited baseline |
| C-27 | PASS | VCA section named with preamble |
| C-28 | PASS | Per-audience gates |
| C-29 | PASS | Gate parentheticals include contract names |
| C-30–C-32 | PASS (3) | Inherited |
| C-33 | PASS | Three-row VCA table |
| C-34 | PASS | Gate parenthetical opens: "Pass (Step 0c exec voice contract satisfied: ...)" |
| C-35 | PASS | Cells attribute Step 0c contract inline |
| C-36 | PASS | Instruction names required verb "satisfied" and consistency relationship; cell template reinforces; gate uses same verb. Note: "e.g., verified" negative example is a runtime robustness risk, but the instruction's primary directive and template are positive ("satisfied") — structural pass |
| C-37 | PASS | Table format with three columns including dedicated Step 0c Contract Verified column |

**Aspirational: 29/29**

### Composite

```
(5/5 * 60) + (3/3 * 30) + (29/29 * 10) = 100.00
```

**V-03 composite: 100.00**

---

## V-04 — Lifecycle Emphasis: Forward Reference from Gate Step 4 to Audit Table

**Hypothesis**: V-02 relies on the model recalling the gate verb when filling cells later. V-04 adds a forward reference in Step 4: "The audit record for these gate verdicts will appear in the Voice Compliance Audit table in the COMPLETION INDEX below. Use the verb 'satisfied' in both the gate parenthetical above and the Step 0c Contract Verified cell below — the two records must use the same verb."

### Essential / Recommended

Identical structure to V-02. **Essential: 5/5. Recommended: 3/3.**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-26 | PASS (18) | Inherited baseline |
| C-27 | PASS | VCA section named with preamble |
| C-28 | PASS | Per-audience gates |
| C-29 | PASS | Gate parentheticals include contract names |
| C-30–C-32 | PASS (3) | Inherited |
| C-33 | PASS | Three-row VCA table |
| C-34 | PASS | Gate parenthetical opens with contract attribution |
| C-35 | PASS | Cells attribute Step 0c contract inline |
| C-36 | PASS | Step 4 forward reference explicitly names "satisfied" as the verb for both gate parenthetical and cell — bridge instruction makes cross-section verb carry-through explicit; cell template reinforces |
| C-37 | PASS | Table format with dedicated contract column |

**Aspirational: 29/29**

### Composite

```
(5/5 * 60) + (3/3 * 30) + (29/29 * 10) = 100.00
```

**V-04 composite: 100.00**

---

## V-05 — Lifecycle Emphasis: Explicit Lexical-Consistency Constraint Block in VCA Section

**Hypothesis**: V-02 template approach, V-04 bridge approach. V-05 instead adds a constraint block inside the VCA section itself naming the mismatch failure mode: "a cell using 'verified' when the gate parenthetical used 'satisfied' creates a traceability mismatch."

### Essential / Recommended

Identical structure to V-02. **Essential: 5/5. Recommended: 3/3.**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-26 | PASS (18) | Inherited baseline |
| C-27 | PASS | VCA section named with preamble |
| C-28 | PASS | Per-audience gates |
| C-29 | PASS | Gate parentheticals include contract names |
| C-30–C-32 | PASS (3) | Inherited |
| C-33 | PASS | Three-row VCA table |
| C-34 | PASS | Gate parenthetical opens with contract attribution |
| C-35 | PASS | Cells attribute Step 0c contract inline |
| C-36 | PASS | Constraint block: names gate verb ("satisfied"), required cell verb ("satisfied"), and failure mode ("not 'verified' or any other verb"); cell template reinforces; self-enforcing within the audit section |
| C-37 | PASS | Table format with Audience / Verdict / Step 0c Contract Verified columns |

**Aspirational: 29/29**

### Composite

```
(5/5 * 60) + (3/3 * 30) + (29/29 * 10) = 100.00
```

**V-05 composite: 100.00**

---

## Summary Table

| Variation | Essential | Recommended | Asp (of 29) | Composite | Predicted | Confirmed? |
|-----------|-----------|-------------|-------------|-----------|-----------|------------|
| V-01 | 5/5 | 3/3 | 27/29 | 99.31 | 27/29 | Yes |
| V-02 | 5/5 | 3/3 | 29/29 | **100.00** | 29/29 | Yes |
| V-03 | 5/5 | 3/3 | 29/29 | **100.00** | 29/29 | Yes |
| V-04 | 5/5 | 3/3 | 29/29 | **100.00** | 29/29 | Yes |
| V-05 | 5/5 | 3/3 | 29/29 | **100.00** | 29/29 | Yes |

**All predictions confirmed. No surprises in R10.**

---

## Rank

1. V-02, V-03, V-04, V-05 — tied at 100.00 (29/29 aspirational)
2. V-01 — 99.31 (27/29 aspirational; isolation test, expected miss on C-34 and C-36)

---

## Key Finding — C-36 Structural Dependency Confirmed

V-01 is the decisive proof: a table with "satisfied" in the cell values **does not earn C-36** when C-34 is absent. The gate parenthetical is the reference verb; the audit cell is the echo. Without a parenthetical, there is no verb to echo, and C-36 is structurally inapplicable. The dependency is:

```
C-36 requires C-34 AND C-35
```

This is now confirmed experimentally.

---

## Excellence Signals — Top-Scoring Variations (V-02 through V-05)

Three distinct mechanisms for achieving C-36, each independently sufficient when C-34 is present:

1. **Verb-in-template as baseline** (V-02): Placing "satisfied" directly in the cell value slot of the table template — `Step 0c exec voice contract satisfied` — is the minimal reliable mechanism. The verb is baked into the template rather than left to model inference. No additional prose required.

2. **Forward reference as carry-forward anchor** (V-04): Adding a sentence in Step 4 pointing from the gate verdict to the downstream audit table, explicitly naming the verb to use in both locations, creates a cross-section consistency bridge before the COMPLETION INDEX is reached. Addresses temporal distance between gate and table.

3. **Constraint block with failure-mode callout** (V-05): Placing an explicit lexical-consistency requirement inside the VCA section itself — naming both the required verb and the non-passing alternative — makes C-36's pass condition self-enforcing at the point of execution. Requires no cross-section memory.

**All three strategies are structurally equivalent at the template level.** Their differential value is runtime robustness: V-02 relies on template fidelity; V-04 and V-05 provide redundant enforcement at different execution points.

**No new patterns emerge that weren't predicted.** R10 is a confirmation round, not a discovery round.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["verb-in-template is the minimal C-36 mechanism — placing satisfied directly in the cell value slot requires no additional prose", "C-36 structural dependency on C-34 confirmed: without a gate parenthetical, the audit cell has no reference verb to echo and C-36 is inapplicable", "three equivalent C-36 enforcement strategies exist: template value, forward-reference bridge, and in-section constraint block — all reach 29/29"]}
```
