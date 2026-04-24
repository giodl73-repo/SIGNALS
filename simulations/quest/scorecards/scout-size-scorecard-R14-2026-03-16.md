# Scout-Size — Round 14 Scorecard

**Skill**: scout-size | **Rubric**: v14 (C-01–C-37, 29 aspirational criteria) | **Date**: 2026-03-17

---

## Variation Architecture Summary

| Var | Phase design | C-36 implementation | C-37 implementation |
|-----|-------------|---------------------|---------------------|
| V-01 | Single-phase, Phase 0 two-precondition | Per-precondition CLOSED identification — prose gate | Three-field block in standalone CHECKPOINT |
| V-02 | Single-phase (second-person), Phase 0 two-precondition | Same as V-01, second-person framing | Three-field, second-person voice |
| V-03 | Three-phase (P0 + Sizing Analyst + Risk Assessor), targeted upgrade of R13 V-04 | Two-precondition Phase 0, prose gate output | Three-field in Phase 2 CHECKPOINT WRONG block |
| V-04 | Three-phase, expanded Phase 0 (subsections per precondition, gate decision table) | Two named subsections + gate checklist table | Three-field in Phase 2 CHECKPOINT WRONG block |
| V-05 | Three-phase, Phase 0 as two-row precondition TABLE (STATUS / CLOSED-LABEL columns) | Schema-level: CLOSED-LABEL column per row | Three-field inside named "── DIAGNOSTIC PATTERN ──" sub-section |

---

## Essential Criteria (C-01–C-05) — 60 pts

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Surface area enumerated | PASS | PASS | PASS | PASS | PASS |
| C-02 | Complexity tier on-scale | PASS | PASS | PASS | PASS | PASS |
| C-03 | Inertia check present | PASS | PASS | PASS | PASS | PASS |
| C-04 | Confidence level stated with basis | PASS | PASS | PASS | PASS | PASS |
| C-05 | Signal boundary respected | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 all variants → 60 pts each. All essential PASS.**

---

## Recommended Criteria (C-06–C-08) — 30 pts

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Team-size signal names specialist types | PASS | PASS | PASS | PASS | PASS |
| C-07 | Timeline signal given as sprint range | PASS | PASS | PASS | PASS | PASS |
| C-08 | Primary complexity driver identified | PASS | PASS | PASS | PASS | PASS |

**Recommended: 3/3 all variants → 30 pts each.**

---

## Aspirational Criteria (C-09–C-37) — 29 criteria, up to 10 pts

### Block 1: Depth / Sensitivity / Calibration (C-09–C-19)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Sensitivity: tier-up and tier-down conditions | PASS | PASS | PASS | PASS | PASS |
| C-10 | Confidence calibration: what would change it | PASS | PASS | PASS | PASS | PASS |
| C-11 | Confidence gap named | PASS | PASS | PASS | PASS | PASS |
| C-12 | Sensitivity framed as single named conditions | PASS | PASS | PASS | PASS | PASS |
| C-13 | Sensitivity names explicit tier destination | PASS | PASS | PASS | PASS | PASS |
| C-14 | Sensitivity conditions are falsifiable | PASS | PASS | PASS | PASS | PASS |
| C-15 | Confidence basis and gap non-overlapping | PASS | PASS | PASS | PASS | PASS |
| C-16 | Sensitivity destination tier differs from current | PASS | PASS | PASS | PASS | PASS |
| C-17 | High-risk constraints carry inline failure examples | PASS | PASS | PASS | PASS | PASS |
| C-18 | Constraints encoded as structural features | PASS | PASS | PASS | PASS | PASS |
| C-19 | Inline failure examples precede the output field | PASS | PASS | PASS | PASS | PASS |

Evidence notes:
- C-13/C-16: All variants encode "Destination Tier [must differ from current tier — fill with LOW / MEDIUM / HIGH / XL]" as column header. Schema-level for all.
- C-15: CONFIDENCE GAP CHECKPOINT standalone section in all variants enforces non-overlap via self-test and field label.
- C-19: WRONG/CORRECT examples precede "Gap: _____" in all variants. Tier sensitivity examples precede sensitivity table in all variants. No post-output checklist placement.

### Block 2: Role Architecture (C-20–C-29)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-20 | Complementary constraint pairs use role-separated production | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-21 | Inline failure examples provide WRONG and CORRECT instances | PASS | PASS | PASS | PASS | PASS |
| C-22 | Relational constraints co-encoded in dependent field's definition | PASS | PASS | PASS | PASS | PASS |
| C-23 | Role charters assign explicit ownership of all output fields | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-24 | Phase 2 non-access clause names prohibited content category | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-25 | Phase 2 charter embeds self-test falsifiability query | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-26 | Role ownership co-encoded in output structure field labels | **FAIL** | **FAIL** | PASS | PASS | PASS |
| C-27 | Cross-phase relational constraints in compilation table | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **FAIL** |
| C-28 | Single-phase self-test query in gap field body | PASS | PASS | **FAIL** | **FAIL** | **FAIL** |
| C-29 | Phase 1 charter carries explicit field exclusion list | **FAIL** | **FAIL** | PASS | PASS | PASS |

Evidence notes:
- **C-20/C-23–C-26/C-29 (V-01, V-02)**: Single-phase architecture — no roles defined. All five criteria require role-separated production or explicit role charters. FAIL for both.
- **C-20/C-23–C-26/C-29 (V-03/V-04/V-05)**: Three-phase design satisfies all. Phase 1 charter explicitly names "Fields reserved for Phase 2 [do not produce here]: Confidence Gap · Confidence Calibration · Tier Sensitivity" (C-29). Phase 2 non-access clause names prohibited category: "any item in the P1-5 confirmed set — e.g., 'API contract is stable'" (C-24). Column headers carry "[Phase 1 Sizing Analyst]" / "[Phase 2 Risk Assessor]" tags (C-26).
- **C-27 (all variants)**: All five variants use C-32 (gap in standalone section, excluded from compilation table). C-27 requires the basis/gap relational constraint encoded in the gap's column header within the compilation table. Since the gap is not a column in any compilation table, C-27 cannot be satisfied. This is the structural cost of C-32: removing the gap from the table eliminates C-31's problem but also C-27's enforcement site. **All FAIL.**
- **C-28 (V-01, V-02)**: Single-phase. CONFIDENCE GAP CHECKPOINT contains: "Ask: if I reversed something from my Step 5 basis... If yes: you have written a basis-negation." Concrete executable query in gap field body. PASS.
- **C-28 (V-03/V-04/V-05)**: C-28 specifies "In single-phase designs where role-separated production (C-20) is not used." These three-phase variants use C-20. C-25 covers the Phase 2 charter self-test; C-28 does not apply. **FAIL** (criterion condition not met).

### Block 3: Defense Cluster and Gate Architecture (C-30–C-37)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-30 | Defense cluster on gap field (label + self-test + WRONG/CORRECT) | PASS | PASS | PASS | PASS | PASS |
| C-31 | Named pre-commit gate block for in-table field constraints | PASS | PASS | PASS | PASS | PASS |
| C-32 | Gap field promoted to named standalone section | PASS | PASS | PASS | PASS | PASS |
| C-33 | Self-test consequence branch names detected failure class | PASS | PASS | PASS | PASS | PASS |
| C-34 | Failure-class label co-encoded in WRONG instance | PASS | PASS | PASS | PASS | PASS |
| C-35 | Pre-analysis gate phase with binary entry signal | PASS | PASS | PASS | PASS | PASS |
| C-36 | Phase 0 gate names C-05 signal boundary as independent precondition | PASS | PASS | PASS | PASS | PASS |
| C-37 | WRONG instance uses full three-field sub-block (FAILURE CLASS / DETECTION PATTERN / WHY IT FAILS) | PASS | PASS | PASS | PASS | PASS |

Evidence notes:
- **C-30 (all)**: All variants have all three enforcement mechanisms in the CONFIDENCE GAP CHECKPOINT section: (1) field label "must address a different dimension / not a negation of it" (label-level); (2) "Ask: could a reader produce this gap by negating P1-5? If yes: you have written a basis-negation" (self-test); (3) WRONG/CORRECT inline block. Defense cluster intact.
- **C-31 (all)**: Vacuously satisfied — all C-17-scoped fields either use C-32 (gap in standalone section) or have C-19-compliant pre-row examples (sensitivity table). C-31's triggering condition (in-table field with no pre-row examples) is never met.
- **C-32 (all)**: All five variants have "── CONFIDENCE GAP CHECKPOINT ──" as a named standalone section with visual delimiter, positioned after confidence basis and before calibration.
- **C-33 (all)**: "If yes: you have written a basis-negation" — failure class named in affirmative branch. V-03/V-04/V-05 add "— a Phase 2 charter violation" for architectural specificity.
- **C-36 (all)**: All five variants include both Precondition A (inertia) and Precondition B (signal boundary) as named gate preconditions. CLOSED output format: "CLOSED — Precondition [A / B]: [name unmet condition]." V-05 encodes this as a table column (CLOSED-LABEL), but criterion passes at prose level too.
- **C-37 (all)**: All five variants have three separately labeled fields in the WRONG block:
  - `**FAILURE CLASS**: basis-negation`
  - `**DETECTION PATTERN**: [derivation-by-negation description]`
  - `**WHY IT FAILS**: [architectural reason]`

---

## Aspirational Score Totals

| Criterion group | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------------|------|------|------|------|------|
| C-09–C-19 (11 criteria) | 11 | 11 | 11 | 11 | 11 |
| C-20–C-29 (10 criteria) | 3 | 3 | 8 | 8 | 8 |
| C-30–C-37 (8 criteria) | 8 | 8 | 8 | 8 | 8 |
| **Total aspirational passes** | **22** | **22** | **27** | **27** | **27** |

---

## Composite Score Calculation

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_score/29 * 10)
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.0 | 30.0 | 22/29 × 10 = 7.59 | **97.6** |
| V-02 | 60.0 | 30.0 | 22/29 × 10 = 7.59 | **97.6** |
| V-03 | 60.0 | 30.0 | 27/29 × 10 = 9.31 | **99.3** |
| V-04 | 60.0 | 30.0 | 27/29 × 10 = 9.31 | **99.3** |
| V-05 | 60.0 | 30.0 | 27/29 × 10 = 9.31 | **99.3** |

---

## Rankings

1. **V-03, V-04, V-05** — 99.3 (three-way tie)
2. **V-01, V-02** — 97.6 (two-way tie)

### Tiebreaker: V-05 as R14 Champion

V-03/V-04/V-05 score identically against v14 criteria. Two architectural innovations distinguish V-05:

**V-05 innovation 1 — Schema-level Phase 0 encoding (C-36)**:

V-03 and V-04 express C-36's per-precondition CLOSED identification as prose gate output format. V-05 encodes it as a table column:

```
| Precondition | Requirement | Status [CLEAR / BLOCKED] | CLOSED Label [fill only if BLOCKED — format: ...] |
| A — Inertia  | ...         |                          |                                                   |
| B — Signal   | ...         |                          |                                                   |
```

The CLOSED-LABEL column is a schema constraint: a blocked precondition row structurally requires a filled CLOSED-LABEL cell. This is C-36's C-18 analog — encoding a constraint in a column header rather than prose instruction. Not yet captured as a criterion.

**V-05 innovation 2 — Named diagnostic sub-section (C-37)**:

V-03 and V-04 embed the three-field WRONG block inside a blockquote. V-05 promotes it to a named sub-section with visual delimiter:

```
### ── DIAGNOSTIC PATTERN ──

The following pattern names and diagnoses the most common failure for this field.
Absorb the failure class, detection procedure, and failure reason before producing your gap.

**WRONG** (basis-negation — Phase 2 charter violation):
> **FAILURE CLASS**: basis-negation
> **DETECTION PATTERN**: ...
> **WHY IT FAILS**: ...
```

This parallels C-32's treatment of the gap field: both are elevated from in-flow content to named structural elements with visual delimiters. Not yet captured as a criterion.

---

## Excellence Signals from V-05

1. **Schema-level Phase 0 constraint encoding**: the CLOSED-LABEL column converts C-36's per-precondition identification from a gate output prose format into a schema constraint that is visible without consulting the gate definition prose. The column header makes a blocked row's failure reason a structural requirement, not a remembered instruction.

2. **Diagnostic block as first-class section**: the "── DIAGNOSTIC PATTERN ──" sub-section with visual delimiter gives the three-field WRONG block the same structural status as the gap checkpoint itself. The delimiter signals that a priming event is in progress — not a blockquote to skim, but a named diagnostic procedure to absorb.

3. **Both innovations are structural analogs of existing patterns**: CLOSED-LABEL column is the Phase 0 analog of C-18 (constraints as column headers). DIAGNOSTIC PATTERN sub-section is the C-37 analog of C-32 (standalone section with visual delimiter). Both extend the rubric's encoding-over-instruction architecture to new attachment points.

---

## R14 Gaps (not yet formalizable as criteria)

| Gap | Pattern | Affects |
|-----|---------|---------|
| C-27 ↔ C-32 tension | All five variants fail C-27 because C-32 removes the gap from the compilation table — the same design choice that makes C-32 possible makes C-27 unreachable. A possible C-38: "When C-32 is used, the compilation table carries a named footnote or caption referencing the CHECKPOINT section and naming the non-overlap constraint." | All variants |
| Phase 0 CLOSED-LABEL as schema column | V-05 encodes C-36's per-precondition failure identification as a column header in the precondition table. No criterion distinguishes schema-level vs prose-level C-36 satisfaction. | V-05 only |
| Diagnostic sub-section with delimiter | V-05 elevates the three-field WRONG block to a named visual section. No criterion distinguishes section-level vs blockquote-level C-37 satisfaction. | V-05 only |

---

```json
{"top_score": 99.3, "all_essential_pass": true, "new_patterns": ["Phase 0 precondition table with CLOSED-LABEL column encodes per-precondition failure identification at the schema level — the CLOSED output format becomes a column constraint rather than a prose instruction, paralleling C-18's encoding-over-instruction principle applied to the gate phase", "WRONG instance diagnostic block elevated to named visual sub-section with delimiter ('── DIAGNOSTIC PATTERN ──') parallel to C-32's standalone gap section — treats diagnostic priming as a first-class structural event rather than annotated blockquote content"]}
```
