```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["correct-wrong example pair for substituted form field names the anti-pattern beside the positive instruction", "checklist gate as hard phase-transition exit converts rubric criteria into pre-conditions", "pre-printed field label combined with explicit prohibition text closes verbal fill-in gap", "L-00 pre-printed as always-UNSTATED inertia row replaces generic reviewer-will-ask with specific named attack"]}
```

---

**Scorecard written** to `simulations/quest/scorecards/discover-limiting-cases-scorecard-R1-2026-03-20.md`.

**Summary:**

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1 | V-01 (Fully Templated) | 100 | YES |
| 1 | V-05 (Checklist Gates) | 100 | YES |
| 3 | V-03 (Inertia Framing) | 97.5 | YES |
| 4 | V-04 (Three-Role Pipeline) | 94 | NO |
| 5 | V-02 (Conversational) | 48.5 | NO |

**Key finding:** V-01 and V-05 tie at 100. The C-09 research question is answered: a named field + explicit prohibition ("write the algebra, not a description") is sufficient without needing a role boundary or gate. V-05's gates add insurance but V-01 achieves equivalent compliance more simply.

V-04 misses golden on C-02 only -- the three-role split produces the best algebra (strongest C-09 enforcement of any variation) but breaks the unified Phase 3 block structure the rubric requires. The R2 opportunity: embed V-04's multi-step algebraic example into V-05's Phase 3 block instructions.

V-03's L-00 inertia anchor is the only pattern unique to one variation that demonstrably improves C-06 quality -- worth carrying into R2 as an addition to V-01 or V-05.
 one-line justification" |
| C-07 | Amendment fixes per class | PASS | Phase 5 template names equation + section per class; generic advice explicitly prohibited |
| C-08 | Stated-in-paper column | PASS | Column pre-printed with explicit prohibition against blanks |
| C-09 | Algebraic substitution | PASS | "Substituted form must show the equation with the limit value substituted in -- write the algebra, not a description of what happens" |
| C-10 | FAIL error-type classification | PASS | "If FAIL -- error type: mathematical error / unstated approximation / model design choice" as pre-printed labeled slot |

```
essential_score   = (5/5) * 60 = 60
recommended_score = (3/3) * 30 = 30
aspirational_score = (2/2) * 10 = 10
composite = 100   golden: YES
```

---

### V-02: Phrasing Register (Conversational / Question-Driven)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Inventory table | FAIL | Artifact spec table lists "(L-ID, equation, variable, direction, verdict)" -- missing "Expected behavior" and "Is expected behavior stated in paper?" columns |
| C-02 | Verification blocks | PARTIAL | Artifact block spec has 4 fields (equation, substitution, result, verdict); missing Expected, At-limit notation, If FAIL, If UNSTATED |
| C-03 | PASS/FAIL/UNSTATED verdicts | PARTIAL | Verdict vocabulary not locked in block template; "verdict" column without explicit restriction to three canonical options |
| C-04 | Standard limit classes | PASS | Four separate questions explicitly cover equilibrium, zero-input, saturation, degenerate parameter |
| C-05 | Frontmatter fields | PASS | "YAML frontmatter: skill, topic, date, limits_checked, p1_failures, unstated_limits" listed at end |
| C-06 | Severity with justification | PARTIAL | P1/P2/P3 defined and asked about; fix instruction present but one-line justification of severity not required |
| C-07 | Amendment fixes per class | PARTIAL | "For each P1 and P2, state exactly what sentence or equation change would resolve it" -- P3 fixes not addressed |
| C-08 | Stated-in-paper column | FAIL | YES/NO elicited in prose but output table spec omits the column entirely |
| C-09 | Algebraic substitution | FAIL | No labeled "Substituted form" field; "Write out what the equation becomes" produces verbal descriptions (confirmed by hypothesis prediction) |
| C-10 | FAIL error-type classification | PARTIAL | Classification question asked in prose but no labeled field; will produce prose classification, not structured capture |

```
essential_score   = ((0+0.5+0.5+1+1)/5) * 60 = 36
recommended_score = ((0.5+0.5+0)/3) * 30 = 10
aspirational_score = ((0+0.5)/2) * 10 = 2.5
composite = 48.5   golden: NO
```

---

### V-03: Inertia Framing (Status-Quo as Named Competitor)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Inventory table | PASS | Full 6-column table pre-printed with L-00 row as always-UNSTATED inertia anchor |
| C-02 | Verification blocks | PASS | Phase 3 block has all required fields plus "Reviewer attack this defends against" extension |
| C-03 | PASS/FAIL/UNSTATED verdicts | PASS | "Verdict: PASS / FAIL / UNSTATED" pre-printed; L-00 models the UNSTATED verdict throughout |
| C-04 | Standard limit classes | PASS | "[Include at least one equilibrium row and one additional class: zero-input, saturation, or degenerate parameter]" |
| C-05 | Frontmatter fields | PASS | All 6 fields listed |
| C-06 | Severity with justification | PASS | Phase 4 "Reviewer attack" column names specific question per non-PASS row; L-00 pre-filled P2 + attack as model |
| C-07 | Amendment fixes per class | PASS | Phase 5: "Equation / Section / Change / Defends against" per class; anti-generic-advice rule enforced |
| C-08 | Stated-in-paper column | PASS | Column pre-printed; L-00 shows "NO -- this is the inertia assumption" as model for all NO rows |
| C-09 | Algebraic substitution | PARTIAL | "Substituted form: [equation with limit value substituted -- show the algebra]" present but no explicit wrong-form anti-pattern named; weaker gate than V-01/V-05 |
| C-10 | FAIL error-type classification | PASS | "If FAIL -- error type: mathematical error / unstated approximation / model design choice" pre-printed labeled slot |

```
essential_score   = (5/5) * 60 = 60
recommended_score = (3/3) * 30 = 30
aspirational_score = ((0.5+1)/2) * 10 = 7.5
composite = 97.5   golden: YES
```

---

### V-04: Role Sequence + Output Format (Three-Role Pipeline)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Inventory table | PASS | Extractor produces full 6-column table; "Fill every cell, including 'Is expected behavior stated in paper?' -- answer YES or NO only" |
| C-02 | Verification blocks | PARTIAL | Block information split: Mathematician (Equation, Substituted form, Result, Math check) + Auditor (Verdict, severity, notes) -- no single Phase 3 block per L-ID as rubric specifies |
| C-03 | PASS/FAIL/UNSTATED verdicts | PASS | Auditor verdict decision tree is explicit: matches=PASS, does not match=FAIL, cannot determine=UNSTATED; consistent with register |
| C-04 | Standard limit classes | PASS | Extractor: "Include at minimum: One equilibrium / steady-state row... At least one additional row: zero-input, saturation, or degenerate parameter" |
| C-05 | Frontmatter fields | PASS | All 6 fields with role-sourced count instructions: "n -- count of L-IDs in Extractor table" |
| C-06 | Severity with justification | PASS | Auditor verdict block: "severity = P1 -- [one-line justification: what result does the formula give that is wrong?]" per class |
| C-07 | Amendment fixes per class | PASS | Auditor Step 3: "P1 fix (if any): Equation / Section / Change" per severity class |
| C-08 | Stated-in-paper column | PASS | Extractor: "answer YES or NO only" for stated-in-paper column |
| C-09 | Algebraic substitution | PASS | Mathematician role writes algebra before verdict; explicit multi-step example shown; strongest algebraic enforcement of any variation |
| C-10 | FAIL error-type classification | PASS | Mathematician block: "If 'does not match': error type: mathematical error / unstated approximation / model design choice" as pre-printed slot |

```
essential_score   = ((1+0.5+1+1+1)/5) * 60 = 54
recommended_score = (3/3) * 30 = 30
aspirational_score = (2/2) * 10 = 10
composite = 94   golden: NO (C-02 PARTIAL -- verification block split across roles fails all-essential requirement)
```

---

### V-05: Lifecycle Emphasis + Inertia Framing (Checklist Gates)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Inventory table | PASS | Full 6-column table; "Blank cells, 'unknown', or 'unclear' are not valid answers" |
| C-02 | Verification blocks | PASS | Phase 3 block has all required fields including two If UNSTATED fields; GATE 3 verifies every L-ID has a block |
| C-03 | PASS/FAIL/UNSTATED verdicts | PASS | GATE 3: "Every verdict is exactly one of: PASS / FAIL / UNSTATED (no 'looks correct', no 'unclear')" -- hardest enforcement of any variation |
| C-04 | Standard limit classes | PASS | GATE 2: "At least one equilibrium row present?" and "At least one additional class row present?" as hard exit conditions |
| C-05 | Frontmatter fields | PASS | GATE 4 verifies all counts match body before writing; all 6 fields listed |
| C-06 | Severity with justification | PASS | Phase 4 register with Impact + Justification columns; "Every non-PASS row needs justification AND a specific fix" |
| C-07 | Amendment fixes per class | PASS | Phase 4 AMEND: "Target equation / Target section / Fix [exact correction/sentence]" per severity class |
| C-08 | Stated-in-paper column | PASS | GATE 2: "Every row has YES or NO in the 'Is expected behavior stated in paper?' column?" -- hardest enforcement; "If any cell is blank: fill it before proceeding" |
| C-09 | Algebraic substitution | PASS | GATE 3: "Every 'Substituted form' field shows an equation, not a description?" with explicit correct/wrong example pair; "If any 'Substituted form' is a description: rewrite it as algebra" |
| C-10 | FAIL error-type classification | PASS | "If FAIL -- error type: mathematical error / unstated approximation / model design choice" pre-printed labeled slot |

```
essential_score   = (5/5) * 60 = 60
recommended_score = (3/3) * 30 = 30
aspirational_score = (2/2) * 10 = 10
composite = 100   golden: YES
```

---

## Composite Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Total | Golden |
|------|-----------|-----------|-------------|--------------|-------|--------|
| 1 | V-01 | 60 | 30 | 10 | **100** | YES |
| 1 | V-05 | 60 | 30 | 10 | **100** | YES |
| 3 | V-03 | 60 | 30 | 7.5 | **97.5** | YES |
| 4 | V-04 | 54 | 30 | 10 | **94** | NO |
| 5 | V-02 | 36 | 10 | 2.5 | **48.5** | NO |

---

## Excellence Signals

Patterns from top-scoring variations that produced rubric compliance:

**1. Correct/wrong example pair for C-09 (V-05)**
Naming the failure mode in the prompt alongside the correct form: "Correct: [shows algebra] / Wrong: 'the derivative vanishes at steady state'". Positive instruction alone ("write the algebra") is weaker than naming the anti-pattern. This directly addresses the highest-value gap in the baseline skill.

**2. Checklist gate as hard phase-transition exit (V-05)**
"Do not begin Phase 3 until all three boxes are checked." Gates convert rubric criteria (C-08, C-09, C-03) from recommendations into pre-conditions. No other mechanism produces the same compliance guarantee at the same token cost.

**3. Pre-printed field labels with explicit prohibition text (V-01)**
"A blank field is a failed criterion" combined with "write the algebra, not a description" in the Phase 3 template. The label creates the slot; the prohibition names the disqualifying fill. Together these close the gap that a label alone leaves open.

**4. Error type as pre-printed labeled sub-field (V-01, V-03, V-04, V-05)**
"If FAIL -- error type: mathematical error / unstated approximation / model design choice" as a named slot in the block makes C-10 structural in four of five variations. Slot naming converts an aspirational criterion into a format requirement.

**5. Frontmatter count verification gate (V-05 GATE 4)**
"limits_checked = number of L-ID rows in Phase 2 inventory?" checked before writing. V-01 achieves this through annotation ("[n -- must match row count in Phase 2]"); V-05 through an explicit gate. Both prevent the silent count mismatch that fails C-05.

---

## Key Finding for R2

The C-09 research question is partially resolved: V-01 (named field + prohibition text) and V-05 (gate + correct/wrong example) both achieve PASS. V-04 (role dependency, strongest algebraic enforcement) also achieves PASS but fails golden on C-02. This suggests the named-field-plus-prohibition combination is sufficient to reliably produce algebra without needing a role boundary. The gate in V-05 adds insurance but the prohibition text in V-01 does equivalent work more simply.

V-04's C-02 PARTIAL is the most actionable finding: the three-role split produces excellent algebraic output (C-09, C-10) but sacrifices the unified Phase 3 block structure. R2 should test a hybrid: V-05 gates with V-04's multi-step algebraic example embedded in the Phase 3 block instructions.

V-03's L-00 inertia anchor is the only pattern not replicated elsewhere that improves C-06 quality: replacing "reviewer will ask" justifications with specific named reviewer attacks. This pattern is worth carrying into R2 as a standalone addition to V-01 or V-05.
