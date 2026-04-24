I have all the information needed. Now I'll make the final rulings on C-22 and C-23, then write the full scorecard.

**Ruling — C-22 (V-01/V-02):** The R7 failure mode was embedded *prose* — a procedure with no table structure. V-01/V-02 embed an actual table with a Resolution column inside each per-role review block. The criterion requires "a conflict table with resolution column," not "a global standalone section." Structural presence confirmed. **C-22 PASS** for V-01 and V-02.

**Ruling — C-23 (V-05):** C-23 definition: "PASS requires an explicit mechanical/non-judgment statement paired with the resolution mechanism." V-05's opening reconciliation rule states "the conflict resolves mechanically from the authority chain — no judgment required" — this IS a description of the resolution mechanism's operation. The phrase is paired with the conflict resolution process at its governance declaration point, not merely mentioned in passing. C-23 is a content criterion; location within the conflict-resolution governance context satisfies "paired with the resolution mechanism." **C-23 PASS** for V-05.

---

## Scorecard — org-pr Round 8 (evaluated against v7 rubric)

**Rubric**: v7 | **N_essential**: 5 | **N_recommended**: 5 | **N_aspirational**: 17

---

### Essential Criteria (60 pts / 12 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Multi-role coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 P1/P2/P3 on every finding | PASS | PASS | PASS | PASS | PASS |
| C-03 File-based role selection | PASS | PASS | PASS | PASS | PASS |
| C-04 Explicit go/no-go verdict | PASS | PASS | PASS | PASS | PASS |
| C-05 Per-role structure / no bleeding | PASS | PASS | PASS | PASS | PASS |
| **Essential total** | **60** | **60** | **60** | **60** | **60** |

All essential criteria pass in all five variations without exception.

---

### Recommended Criteria (30 pts / 6 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Projection-aware consensus | PASS | PASS | PASS | PASS | PASS |
| C-07 Conflict analysis (resolution present) | PASS | PASS | PASS | PASS | PASS |
| C-08 Locator self-correction gate | PASS | PASS | PASS | PASS | PASS |
| C-09 Phase/lifecycle gating | PASS | PASS | PASS | PASS | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **30** | **30** | **30** | **30** | **30** |

Evidence notes:

**C-07 all**: V-01/V-02 resolve conflicts through per-role inline sub-tables (conditional, inline). V-03/V-04/V-05 use standalone Conflict Analysis sections. C-07 tests *presence* of a resolution mechanism, not its form. PASS for all five.

**C-09 all**: All five include an explicit PRE-MERGE phase gate with halt instruction. PASS for all five.

---

### Aspirational Criteria (10 pts, N=17)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | PASS | PASS | PASS | PASS | PASS |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PARTIAL | PASS | PASS | PASS | PASS |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | PASS | PASS | PASS | PASS |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A | N/A | N/A | N/A | N/A |
| C-19 Verdict hardening pair | PARTIAL | PASS | PASS | PASS | PASS |
| C-20 Priority table | N/A | N/A | N/A | N/A | N/A |
| C-21 Authority-inertia reconciliation rule | PASS | PASS | PASS | N/A | PASS |
| C-22 Conflict resolution column | **PASS** | **PASS** | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | **PASS** |
| C-24 Correction-paired invalid form catalog | PASS | PASS | PASS | PASS | PASS |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | PASS | PASS | PASS | N/A | PASS |
| C-27 Priority axis non-redundancy | N/A | N/A | N/A | N/A | N/A |

**All N/A entries count as PASS_equiv = 1.0.**

---

#### Evidence Notes — Contested and Notable Criteria

**C-14 V-01**: "There is no fourth outcome. Reclassify any P1 or accept No-Go." Names two escape paths; does not include the exclusion statement "No other escape path exists." PARTIAL (0.5). Caps C-19 at PARTIAL.

**C-14 V-02 through V-05**: "No other escape path exists. A P1 + Go claim is invalid under this formula." Explicit exclusion statement present. PASS.

**C-18 all**: No priority table in any variation. N/A→PASS.

**C-20 all**: No priority table in any variation. N/A→PASS.

**C-21 V-01/V-02/V-03**: Opening declares "two governance axes: authority chain and inertia framing" plus reconciliation rule. Inertia is a declared governance axis. PASS.

**C-21 V-04**: No axis declaration. Inertia is not a declared governance axis — the If-Stays Projection column is a format feature only. No reconciliation rule present or needed. N/A→PASS.

**C-21 V-05**: Opening declares two axes and includes "the conflict resolves mechanically from the authority chain — no judgment required" as part of the reconciliation rule. Inertia is a declared governance axis. PASS.

**C-22 V-01/V-02 — FINAL RULING: PASS**: The R7 C-22 failure was an embedded *procedure* — a prose instruction with no table structure. V-01/V-02 embed an actual 4-column table (Surface / This Role's Assessment / Upstream Role Assessment / Resolution) within each per-role review block. The criterion requires "a conflict table with resolution column." A per-role sub-table with a Resolution column is structurally a conflict table; C-22 fires on structural presence, not on the table's position (global vs. per-role). PASS. This is the first round to confirm the embedded-table path satisfies C-22.

**C-22 V-03/V-04/V-05**: Standalone Conflict Analysis section with 4-column table including Resolution column. Consistent with all prior confirmed PASS forms.

**C-23 V-01 through V-04**: Phrase "derived mechanically from the authority chain, no judgment required" in the conflict table's resolution column instruction. V-01/V-02: per-role sub-table resolution entry. V-03/V-04: standalone Conflict Analysis section resolution column instruction. PASS for all.

**C-23 V-05 — FINAL RULING: PASS**: The phrase "no judgment required" appears in the opening reconciliation rule: "the conflict resolves mechanically from the authority chain — no judgment required." The resolution column says only "pos N governs; Role B's position recorded as compounding-cost entry." C-23 definition: "PASS requires an explicit mechanical/non-judgment statement *paired with the resolution mechanism.*" The opening reconciliation rule constitutes the governance declaration for the resolution mechanism — the phrase is paired with the mechanism's operation at its point of declaration. C-23 is a content criterion (phrase must appear in a conflict-resolution governance context), not a structural criterion (phrase must appear in the resolution column template). PASS. Prompts may concentrate all governance declarations in the opening rule without distributing them across resolution column instructions.

**C-25 all**: "Both must be satisfied simultaneously" present in V-01 through V-05. V-02 through V-05 additionally include the mutual-dependency explanation. PASS for all.

**C-26 V-01/V-02/V-03/V-05**: "This prompt operates under two governance axes" — explicit integer count declared. PASS.

**C-26 V-04**: No axis declaration — single-axis design. C-26: "N/A if only one axis is present — no declaration is needed for single-axis prompts (counts as PASS)." N/A→PASS.

**C-27 all**: No priority table in any variation. N/A→PASS.

---

### PASS_equiv Calculation

| Variation | Full-weight (PASS/N/A) | PARTIAL × 0.5 | PASS_equiv | Aspirational pts |
|-----------|------------------------|---------------|------------|-----------------|
| V-01 | 15 (C-14, C-19 excluded) | 2 × 0.5 = 1.0 | **16.0** | **9.41** |
| V-02 | 17 | 0 | **17.0** | **10.00** |
| V-03 | 17 | 0 | **17.0** | **10.00** |
| V-04 | 17 | 0 | **17.0** | **10.00** |
| V-05 | 17 | 0 | **17.0** | **10.00** |

V-01 PASS_equiv detail: C-11, C-12, C-13, C-15, C-16, C-17, C-18(N/A), C-20(N/A), C-21, C-22, C-23, C-24, C-25, C-26, C-27(N/A) = 15 full-weight + C-14(0.5) + C-19(0.5) = 16.0.

---

### Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 30 | 9.41 | **99.41** |
| V-02 | 60 | 30 | 10.00 | **100.00** |
| V-03 | 60 | 30 | 10.00 | **100.00** |
| V-04 | 60 | 30 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

---

### Ranking

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 (tied) | V-02 | 100.00 | Per-role sub-tables + escape closure; first 100.00 without standalone global Conflict section |
| 1 (tied) | V-03 | 100.00 | 2-axis + standalone Conflict section + escape closure; minimum-structure 100.00 path confirmed |
| 1 (tied) | V-04 | 100.00 | Single-axis + standalone Conflict + escape closure; minimum governance complexity 100.00 |
| 1 (tied) | V-05 | 100.00 | 2-axis + C-23 phrase in opening rule only; confirms C-23 is a content criterion |
| 5 | V-01 | 99.41 | Missing escape closure; C-14/C-19 PARTIAL |

---

### Excellence Signals

**1. C-22 is location-independent: per-role embedded conflict sub-tables satisfy the criterion.** V-01/V-02 embed conflict tables inside each role's review block rather than in a global standalone section. The criterion fires on structural presence (table + resolution column), not on the table's position in the document. The R7 failure mode was embedded *prose* (a procedure without table structure); embedded *tables* satisfy C-22 PASS. V-02 is the first variation in the series to reach 100.00 without a global Conflict Analysis section.

**2. C-23 is a content criterion: opening reconciliation rule placement satisfies the criterion.** V-05 places "no judgment required" exclusively in the opening reconciliation rule, omitting it from the resolution column. C-23 fires because the phrase appears in a conflict-resolution governance context — the opening rule governing how the mechanism operates. Prompts may declare judgment-elimination once at the governance level rather than distributing the phrase across every resolution column instruction.

**3. Single-axis design achieves 100.00: minimum governance complexity confirmed.** V-04 eliminates the inertia axis declaration entirely. C-21 (reconciliation rule), C-26 (governance scope declaration), C-18 (axis conflict rule), C-20 (priority table), and C-27 (axis non-redundancy) all collapse to N/A→PASS simultaneously. The If-Stays Projection column satisfies C-13 as a format feature independent of governance axis declaration. Minimum 100.00 design: one axis + standalone Conflict section + escape closure + invalid-form catalog.

**4. Four concurrent 100.00 paths confirmed in a single round.** V-02 (per-role sub-tables + escape closure), V-03 (2-axis standalone Conflict + escape closure), V-04 (single-axis standalone Conflict + escape closure), V-05 (2-axis + C-23 in opening only). No single design archetype is privileged. The rubric maps a score space with multiple structurally distinct maxima; teams may choose the path that fits their governance preference without sacrificing score.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-22 is location-independent: a per-role embedded conflict sub-table (conditional, inline within each role's review block) satisfies C-22 PASS — the criterion fires on structural presence (table + resolution column) regardless of whether the table is global or per-role; embedded tables resolve the R7 embedded-procedure failure mode", "C-23 is a content criterion not a structural criterion: the judgment-elimination phrase in the opening reconciliation rule satisfies C-23 PASS without requiring the phrase in the resolution column — prompts may declare mechanical resolution once at the governance level rather than distributing the phrase across resolution column instructions", "Single-axis design achieves 100.00 via uniform N/A collapse: removing the inertia axis declaration collapses C-21, C-26, C-18, C-20, and C-27 to N/A→PASS simultaneously; the If-Stays column satisfies C-13 as a format feature independent of governance axis declaration; minimum 100.00 requires one axis + standalone Conflict section + escape closure + invalid-form catalog", "Four concurrent 100.00 paths confirmed in a single round (V-02 per-role sub-tables, V-03 2-axis standalone, V-04 single-axis, V-05 opening-only C-23): the rubric maps multiple structurally distinct maxima; no single design archetype is privileged"]}
```
