---

# Variate R17 -- corps-rob

**Written to:** `simulations/quest/golden/corps-rob-variate-R17-2026-03-17.md`

---

## R17 Situation Report

**R16 diagnostic conclusion**: All three hypotheses (H-A: RULE IB-REVISION, H-B: RULE BLOCKER-PROTOCOL, H-C: RULE STAGE-HANDOFF) were eliminated. All five R16 variations tied at **285/290**. The gap lies outside the cross-stage artifact naming space.

**R17 pivot**: The probe moves to named-rule structural completeness -- specifically, which named rules are missing structural fields that their sibling rules already have.

---

## Variation Table

| Var | Axis | Hypothesis | Delta from R16 V-05 base |
|-----|------|------------|--------------------------|
| V-01 | Phrasing register | H-D: RULE ZERO-STATE Anti-pattern | Add labeled Anti-pattern to RULE ZERO-STATE naming the silent-last-row disqualifying form |
| V-02 | Lifecycle emphasis | H-E: RULE VIOLATION-TAXONOMY elevation | Add RULE VIOLATION-TAXONOMY to glossary: structural element (ID / Description / Consequence / Series-state), two anti-patterns, series-state terminator |
| V-03 | Role sequence | H-F: RULE PHASE-GATE second anti-pattern | Add Anti-pattern-2 to RULE PHASE-GATE naming the category-without-instance disqualifying form |
| V-04 | Phrasing register + Lifecycle emphasis | H-D + H-E | V-01 + V-02 combined |
| V-05 | Phrasing register + Lifecycle emphasis + Role sequence | H-D + H-E + H-F full target | V-01 + V-02 + V-03 combined |

---

## Key Structural Observations

**RULE ZERO-STATE asymmetry (H-D)**: Every named rule in the R16 V-05 glossary that governs a structural output artifact has a labeled Anti-pattern field *except* RULE ZERO-STATE. It declares the requirement positively but never names what silent failure looks like. The anti-pattern: "a section whose last line is a populated entry row with no explicit labeled zero-state line following it."

**RULE VIOLATION-TAXONOMY gap (H-E)**: The violation taxonomy is the only structural artifact in the format spec not governed by a named rule. Every other artifact (FINDING LEDGER, CARRY FORWARD, BLOCKER records, SYNTHESIS, the audit suite) has a named rule with structural element and anti-pattern. The taxonomy governs other artifacts' compliance but is itself ungoverned. RULE VIOLATION-TAXONOMY adds structural element (ID / Description / Consequence), anti-pattern-1 (entry without Consequence annotation), anti-pattern-2 (no series-state terminator), and the series-state constraint.

**RULE PHASE-GATE second anti-pattern (H-F)**: RULE PHASE-GATE has one anti-pattern. RULE BLOCKER-PROTOCOL, RULE STAGE-HANDOFF, RULE CONDITIONAL-ITEM, and RULE AUDIT-SUITE all have two. Anti-pattern-2 names the adjacent-but-wrong form: a phase gate that cites an artifact *category* ("all HIGH findings from teams") rather than a specific LID or risk ID from the current run.

**C-45 invariant**: None of the three additions create new criteria requiring glossary scope in the C-30/C-34 sense. "Exactly 2" remains accurate in all five variations.

**Predicted score distribution:**
- V-01, V-02, V-03: 285 each (if gap is not H-D, H-E, or H-F respectively) or 290 (if it is)
- V-04: 290 if H-D or H-E; 285 if only H-F is the gap
- V-05: 290/290 if gap is any of {H-D, H-E, H-F}; 285/290 if gap is outside all three → confirms R18 needs a new probe space
