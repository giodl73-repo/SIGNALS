## Scoring Report — draft-brainstorm R7 (Rubric v7)

---

### Baseline Established

All five variations inherit a clean C-01..C-24 pass record from R6. The R7 rubric coverage analysis table in the variate file confirms this explicitly for every criterion. Baseline subtotal before R7 criteria:

| Tier | Pass | Max | Pts |
|------|------|-----|-----|
| Essential (C-01..C-05) | 5/5 | 60 | 60 |
| Recommended (C-06..C-08) | 3/3 | 30 | 30 |
| Aspirational (C-09..C-10) | 2/2 | 10 | 10 |
| R2 (C-11..C-14) | 4/4 | 10 | 10 |
| R3 (C-15..C-18) | 4/4 | 10 | 10 |
| R4 (C-19..C-20) | 2/2 | 5 | 5 |
| R5 (C-21..C-22) | 2/2 | 5 | 5 |
| R6 (C-23..C-24) | 2/2 | 5 | 5 |
| **Subtotal** | | | **135** |

---

### V-01 — Schema-Lock Registry (C-25 isolation)

**Base**: R6-V-03. **Axis**: Check B upgraded to structural Registry with null-gated `Selected?` column; Check C retains basic re-invocability bar only.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-25 Marking-Gate Schema Lock | **PASS** | Selected? column rule: "cannot hold any value until all 5 rows of this Registry are complete — this is a schema constraint of the Registry, not a deferred choice." Gate is architectural: column-null until batch rows exist. Distinct from the Prohibition A prose ban (C-23). |
| C-26 AMEND Pool-Composition Constraint | **FAIL** | Check C: "would they get a noticeably different pool?" — re-invocability bar only (C-12 level). Distribution-shift test ("different ideas, not different labels") intentionally absent to isolate C-25. |

**R7 pts**: 2.5 (C-25 only)
**Score: 135 + 2.5 = 137.5**

---

### V-02 — Distribution-Shift AMEND Test (C-26 isolation)

**Base**: R6-V-03. **Axis**: Check C renamed "AMEND Distribution-Shift Test"; the criterion is explicitly stated as different candidate ideas, not different labels; prose Prohibition Battery retained without structural column.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-25 Marking-Gate Schema Lock | **FAIL** | Check B uses prose numbered sentences with Prohibition A marking ban. The gate is behavioral (model must honor the prohibition), not architectural. No structural column with null condition. Intentional isolation. |
| C-26 AMEND Pool-Composition Constraint | **PASS** | Check C Distribution-Shift Test: "must surface candidate ideas that would not have appeared in the original pool — different ideas, not different labels on the same ideas. A directive that changes only category names, emphasis framing, or grouping taxonomy without introducing different underlying candidates fails this test." Explicitly names the distribution-shift test as the governing criterion, enumerates the failing mode. |

**R7 pts**: 2.5 (C-26 only)
**Score: 135 + 2.5 = 137.5**

---

### V-03 — Schema-Lock Registry + Distribution-Shift (C-25 + C-26, Prohibition Battery base)

**Base**: R6-V-03. **Axes**: Both V-01 and V-02 combined on the compact Prohibition Battery scaffold.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-25 Marking-Gate Schema Lock | **PASS** | Selected? column: "Schema null constraint. This column cannot hold any value until all 5 rows of this Registry are complete." Structural; Prohibition A coexists as named prohibition but C-25 is satisfied independently by the schema property. |
| C-26 AMEND Pool-Composition Constraint | **PASS** | Check C: "different ideas, not different labels on the same ideas. A directive that shifts only category names, framing emphasis, or grouping taxonomy without introducing different underlying candidates fails this test." Distribution-shift named as the criterion. |

**R7 pts**: 5.0 (C-25 + C-26)
**Score: 135 + 5.0 = 140**

---

### V-04 — Schema Registry Lineage + Explicit Distribution-Shift (R6-V-04 + C-26)

**Base**: R6-V-04 (table Top-5? column + Pre-Selection Batch Registry, C-25 inherited). **Axis**: Minimum-viable single edit — Review B and Step 5 condition (c) upgraded with distribution-shift language.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-25 Marking-Gate Schema Lock | **PASS** (inherited) | Top-5? column in idea table: "Leave this column blank during Step 1. The Top-5? column will be filled only after the Pre-Selection Batch Registry (Step 2b) is fully complete." Step 3 is gated: "Only after Step 2b is fully written." Schema-level gate; the column cannot be populated until the Registry rows exist. |
| C-26 AMEND Pool-Composition Constraint | **PASS** | Review B: "whether different ideas enter the pool — not whether the same ideas appear under different labels, different Dimension headings, or different framing emphasis. A directive that shifts only category taxonomy or presentation without introducing new candidate ideas fails this test." Step 5 condition (c): "distribution-shift guarantee — re-running must surface candidate ideas that would not appear in the original table; different ideas, not different labels on the same ideas." |

**R7 pts**: 5.0 (C-25 + C-26)
**Score: 135 + 5.0 = 140**

---

### V-05 — Full-Stack Layered Architecture + Schema-Lock Registry (R6-V-05 + C-25)

**Base**: R6-V-05 (5-layer architecture, C-26 inherited). **Axis**: Check B prose batch upgraded to Verification Registry with structurally null-gated `Selected?` column.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-25 Marking-Gate Schema Lock | **PASS** (new in R7) | Verification Registry Selected? column: "Structural null constraint. This column cannot hold any value until all 5 rows of this Registry are complete — this is a property of the Registry schema, not a deferred instruction. Layer 4 may begin only when all 5 rows exist and Selected? is blank across all rows." Explicitly names schema as the source of the constraint. |
| C-26 AMEND Pool-Composition Constraint | **PASS** (inherited) | Check C: "The bar is a different candidate distribution, not different labels on the same ideas. Re-running with the directive must surface candidate ideas that would not have appeared in the original pool — new ideas enter, or existing ideas are clearly displaced by ideas that were absent. A directive that changes only framing emphasis, category naming, or grouping taxonomy without shifting which underlying ideas appear fails this test." |

Note: V-05 also contains a particularly strong rationalization-block formulation not present in other variations: "If you want to edit the rationale, treat that impulse as confirmation that the replacement obligation applies." This converts the cognitive escape route into a trigger signal for the constraint.

**R7 pts**: 5.0 (C-25 + C-26)
**Score: 135 + 5.0 = 140**

---

### Rankings

| Rank | Variation | Score | Delta |
|------|-----------|-------|-------|
| 1 (tie) | V-03 | **140** | +5 vs. baseline |
| 1 (tie) | V-04 | **140** | +5 vs. baseline |
| 1 (tie) | V-05 | **140** | +5 vs. baseline |
| 4 (tie) | V-01 | **137.5** | +2.5 vs. baseline |
| 4 (tie) | V-02 | **137.5** | +2.5 vs. baseline |

All variations pass all essentials. No essential failures. All are golden (>= 80, no essential fails).

---

### Excellence Signals from Top-Scoring Variations

**Signal 1 — Schema null constraint as explicit architectural label** (V-01, V-03, V-05)
All three independently arrive at a formulation that names the constraint as a *property of the schema*, not an instruction. The language "this is a schema constraint of the Registry, not a deferred choice" (V-01/V-03) and "this is a property of the Registry schema, not a deferred instruction" (V-05) frames the gate as structural rather than behavioral. This framing signals to the model that the constraint cannot be opted out of, unlike a prose instruction that can be "decided" to honor later.

**Signal 2 — Distribution-shift failure taxonomy as part of the criterion** (V-02, V-03, V-04, V-05)
All passing C-26 variations enumerate the failing modes explicitly: "category names, emphasis framing, grouping taxonomy." The criterion is defined not just positively ("different ideas") but with a named catalogue of what does NOT constitute a valid shift. This taxonomy closes the label-shift loophole by naming its specific manifestations rather than relying on the model to recognize label-shifting as a violation.

**Signal 3 — Minimum-viable-upgrade architecture** (V-04)
V-04 demonstrates that reaching 140 from a 137.5 baseline requires exactly one targeted edit: adding "different candidate ideas, not different rows under a different label" to Review B and condition (c) in Step 5. The schema lock (C-25) was already present; only the distribution-shift language was missing. This establishes a pattern: each aspired criterion can be added incrementally without structural redesign when the prior level's architecture is sound.

**Signal 4 — Impulse-as-confirmation meta-instruction** (V-05 only)
V-05's rationalization prohibition includes: "If you want to edit the rationale, treat that impulse as confirmation that the replacement obligation applies." This is a novel pattern — converting a cognitive escape route (desire to revise) into a positive trigger signal for the constraint, rather than just prohibiting the action. The loophole is closed by naming the desire itself as confirmation of failure, not just the action.

---

### Score Summary

| Variation | Ess | Rec | Asp | R2 | R3 | R4 | R5 | R6 | R7 | Score |
|-----------|-----|-----|-----|----|----|----|----|----|----|-------|
| V-01 | 5/5 | 3/3 | 2/2 | 4/4 | 4/4 | 2/2 | 2/2 | 2/2 | 1/2 | **137.5** |
| V-02 | 5/5 | 3/3 | 2/2 | 4/4 | 4/4 | 2/2 | 2/2 | 2/2 | 1/2 | **137.5** |
| V-03 | 5/5 | 3/3 | 2/2 | 4/4 | 4/4 | 2/2 | 2/2 | 2/2 | 2/2 | **140** |
| V-04 | 5/5 | 3/3 | 2/2 | 4/4 | 4/4 | 2/2 | 2/2 | 2/2 | 2/2 | **140** |
| V-05 | 5/5 | 3/3 | 2/2 | 4/4 | 4/4 | 2/2 | 2/2 | 2/2 | 2/2 | **140** |

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["schema-null-as-output-architecture: C-25 passing variations name the marking gate as a structural property of the output schema ('schema constraint of the Registry, not a deferred choice'), not a behavioral instruction -- framing the gate as architectural rather than instructional signals the constraint cannot be opted out of", "distribution-shift-failure-taxonomy: C-26 passing variations enumerate specific failing modes (category names, framing emphasis, grouping taxonomy) as a named catalogue alongside the positive requirement ('different ideas, not different labels') -- negative example taxonomy closes the loophole by naming its specific manifestations", "impulse-as-confirmation-meta-instruction: V-05 converts the desire to revise a rationale into a positive trigger signal for the replacement obligation ('if you want to edit the rationale, treat that impulse as confirmation that the replacement obligation applies'), closing the cognitive escape route rather than just prohibiting the action"]}
```
