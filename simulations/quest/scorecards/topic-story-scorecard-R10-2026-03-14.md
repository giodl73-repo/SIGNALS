I now have all the information needed to score the five R10 variations against the v10 rubric. Let me compile the full analysis.

---

# Round 10 Scorecard — `topic-story` (v10 Rubric, 36 Criteria)

**Date**: 2026-03-15
**Rubric**: `topic-story-rubric-v10-2026-03-14.md`
**New criteria this round**: C-34, C-35, C-36
**R9 baseline under v10**: 99.83 (V-05 → 28 PASS + 1 PARTIAL on C-36)

---

## Inherited Criteria Status (C-01 -- C-33)

All five variations carry the full structural body of R9 V-05. The R9 analysis confirmed complete PASS across C-01--C-33 for that baseline. All variations in R10 preserve this structure without regression.

**C-01 through C-33**: PASS for all five variations — not re-derived below.

---

## New Criterion Scoring — Per Variation

### C-34 — Repair Operation Supplies an Instantiable Item Template

**Pass condition**: The `**Repair operation**:` block contains a quotable item template parameterized by field name and section name, from which a C-22-compliant replacement item can be produced by substitution alone.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | Repair block contains the quotable template AND names the substitution variables explicitly: "`[Section name]` → the section's heading text (e.g., 'Signal Findings', 'Recommendation'). `[field name]` → the field's label string from the inventory (e.g., 'Prior position', 'Verdict'). Do not derive -- substitute directly from these two sources." Instantiation is prescribed, not inferred. C-34 passes (template + named sources). |
| V-02 | PASS | Repair block contains the quotable template `"Does [Section name] include the label **[field name]**:?"` — parameterized by field name and section name. Variables are unnamed but the template is substitutable by inspection. C-34 pass condition met; no substitution variable labels (that is the V-01 axis). |
| V-03 | PASS | Same repair template as V-02 (R9 V-05 baseline). Parameterized, quotable, substitutable. PASS. |
| V-04 | PASS | V-01 repair formula — explicit substitution variable labels plus template. Same as V-01. PASS. |
| V-05 | PASS | V-01 repair formula — explicit substitution variable labels plus template. Same as V-01. PASS. |

**Note**: C-34 passes across all five variations because the parameterized template (present in all) satisfies the pass condition. V-01, V-04, V-05 go beyond C-34 by labeling substitution variables — a property that could generate C-37.

---

### C-35 — Section Template Anti-Consolidation Directive Designates Field Inventory as Canonical Source

**Pass condition**: The directive includes an explicit cross-reference to the field inventory as source (not an independent restatement). The cross-reference must identify the inventory as the source, not merely suggest consulting it.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | Section 4: "Anti-consolidation directive **(see inventory Structural Constraint column for the authoritative rule)**". Names the inventory column as the authoritative source. Directive is a reference, not a standalone restatement. Same as R9 V-05. PASS. |
| V-02 | PASS | Section 4: "Anti-consolidation directive **(authoritative rule: field inventory above, Structural Constraint column, Inertia-framing axis row -- that cell is the single point of update for this constraint; this directive is a reference to it)**". Upgrades from column-level to cell-level navigation. Names the cell as single point of update. Explicitly self-designates the directive as a reference. Stronger than V-01's C-35 PASS, still PASS. |
| V-03 | PASS | Section 4: "Anti-consolidation directive **(see inventory Structural Constraint column for the authoritative rule)**". Same as R9 V-05. PASS. |
| V-04 | PASS | V-02 directive — exact cell navigation, "single point of update," "this directive is a reference to it." Same as V-02. PASS. |
| V-05 | PASS | "Anti-consolidation directive **(authoritative rule: field inventory above, Structural Constraint column, Inertia-framing axis row -- that cell is the single point of update for this constraint; this directive is a reference to it, not an independent restatement)**". V-02 cell navigation plus explicit "not an independent restatement." Strongest C-35 expression. PASS. |

---

### C-36 — Checklist Explicitly Designates Field Inventory as Authoritative Constraint Source and Its Own Items as References

**Pass condition**: Checklist contains an explicit statement that (a) designates the inventory as authoritative for consolidation constraints and (b) identifies the corresponding items as references, not independent restatements. Implicit dependency does not satisfy.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PARTIAL | Footer: "Structural constraints for items 10-12 are registered in the inventory table's Structural Constraint column -- the anti-consolidation rule is auditable from the inventory without re-reading this checklist." Implies inventory authority (auditable from inventory) without asserting it. Does not designate items 10-12 as references vs. restatements. Same as R9 V-05. C-36 requires the explicit assertion; implication does not pass. PARTIAL. |
| V-02 | PARTIAL | Same footer as V-01/R9 V-05. Same analysis. PARTIAL. |
| V-03 | **PASS** | Footer: "The inventory is the authoritative constraint source. Items 10-12 are references to the inventory's Structural Constraint column, not independent restatements -- updating the inventory propagates to these items; the checklist is not separately authoritative for constraint content." Explicitly: (a) designates inventory as authoritative, (b) names items as references, (c) names items as NOT independent restatements, (d) names propagation rule. All three C-36 requirements met. PASS. |
| V-04 | PARTIAL | Same footer as V-01/R9 V-05. Same analysis. PARTIAL. |
| V-05 | **PASS** | Footer: "The inventory is the authoritative constraint source. Items 10-12 are references to the inventory's Structural Constraint column, Inertia-framing axis row -- not independent restatements. Updating that inventory cell propagates to the Section 4 directive and to these items; the checklist is not separately authoritative for constraint content." Same assertions as V-03 plus cell-level specificity and explicit "propagates to the Section 4 directive." PASS — stronger than V-03. |

---

## Composite Scores

**Scoring formula**: Essential (60) + Recommended (30) + Aspirational (10 pts / 29 criteria ≈ 0.3448 pts each; PARTIAL = 0.1724 pts).

All variations: C-01--C-04 PASS (60 pts), C-05--C-07 PASS (30 pts), C-08--C-33 all PASS (26 × 0.3448 = 8.965 pts).

| Variation | C-34 | C-35 | C-36 | Aspirational Total | **Score** |
|-----------|------|------|------|--------------------|-----------|
| V-01 | PASS | PASS | PARTIAL | 8.965 + 0.3448 + 0.3448 + 0.1724 = 9.827 | **99.83** |
| V-02 | PASS | PASS | PARTIAL | same | **99.83** |
| V-03 | PASS | PASS | PASS | 8.965 + 0.3448 + 0.3448 + 0.3448 = 10.0 | **100.0** |
| V-04 | PASS | PASS | PARTIAL | same as V-01 | **99.83** |
| V-05 | PASS | PASS | PASS | same as V-03 | **100.0** |

---

## Ranking

| Rank | Variation | Score | Distinguishing property |
|------|-----------|-------|------------------------|
| 1 (tie) | **V-05** | 100.0 | Full compound: V-01 + V-02 + V-03 + ordered extension protocol |
| 1 (tie) | **V-03** | 100.0 | Single axis: explicit C-36 footer in lean register |
| 3 (tie) | V-01 | 99.83 | Single axis: repair formula substitution variable labels; C-36 still PARTIAL |
| 3 (tie) | V-02 | 99.83 | Single axis: exact cell navigation in directive; C-36 still PARTIAL |
| 3 (tie) | V-04 | 99.83 | Compound V-01 + V-02; C-36 still PARTIAL |

---

## Excellence Signals

Both V-03 and V-05 achieve 100.0. V-03 shows C-36 is satisfiable independently of C-34/C-35 upgrades. V-05 combines all four axes into a structurally saturated form that goes beyond what any existing criterion captures.

**Signal 1 — Repair formula substitution variables are explicitly labeled with source declarations** (V-01, V-04, V-05).
C-34 fires on the template existing; all five variations pass. V-01/V-04/V-05 go further: `[Section name]` is named as "the section's heading text" with examples; `[field name]` is named as "the field's label string from the inventory" with examples; "Do not derive -- substitute directly from these two sources" makes the source of each variable a declared constraint. The template shifts from *parameterized-inferrable* (substitution is possible) to *parameterized-prescribed* (substitution sources are named). An auditor verifying the repair formula no longer needs to infer what the placeholders take — the substitution is fully specified.

**Signal 2 — Section directive explicitly self-designates as a reference to the inventory cell, not an independent restatement** (V-02, V-04, V-05 — strongest in V-05).
C-35 fires on the directive forming a reference chain to the inventory. V-02's directive goes further: it names the exact cell (column + row), declares the cell as "the single point of update," and explicitly says "this directive is a reference to it." V-05 adds "not an independent restatement" to close the loop. C-35 requires the directive to attribute constraint authority to the inventory; these variations have the directive *announce its own dependent status* — making the reference hierarchy legible to a reader without access to the rubric.

**Signal 3 — Extension protocol restructured as an ordered propagation sequence with inventory as origin** (V-05 only).
No existing criterion fires on the extension protocol's update sequence. R9 V-05 listed three parallel steps (name axis, register field, add checklist item) with no ordering. V-05 replaces this with a sequential propagation rule: inventory updated first (authoritative), then section templates cross-referencing the inventory entry, then checklist items designated as references to that entry. This makes the update dependency explicit and prevents divergence by design: a maintainer who follows the sequence cannot produce a state where section template or checklist contains a constraint that hasn't been registered in the inventory first. The hierarchy is not just structurally correct (C-33/C-35/C-36) — the *extension procedure* enforces it.

---

## Summary Assessment

V-03 demonstrates that C-36 is the critical gate: adding explicit inventory authority designation to the checklist footer, without any other change, is sufficient to achieve 100.0 under v10. C-34 and C-35 are already satisfied by the R9 V-05 baseline.

V-05 is the structurally richest variation and provides three excellence signals, all of which are candidates for v11 criteria. The ordered propagation sequence (Signal 3) is the genuinely novel structural property — it is not subsumed by any of C-34, C-35, or C-36.

The v11 criterion slate is well-defined:
- **C-37**: Repair formula substitution variables explicitly labeled with source declarations
- **C-38**: Section directive explicitly self-designates as a reference (not restatement) to the specific inventory cell
- **C-39**: Extension protocol specifies an ordered constraint-propagation sequence with inventory as the update origin

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["repair formula substitution variables explicitly labeled with source declarations converting the template from parameterized-inferrable to parameterized-prescribed", "section directive explicitly self-designates as a reference to the inventory cell and not an independent restatement making the reference hierarchy legible without the rubric", "extension protocol restructured as an ordered constraint-propagation sequence with inventory updated first making update dependency explicit and preventing divergence by design"]}
```
