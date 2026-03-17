```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["sequential stop-token gate structure with blocked CONDITION (i)/(ii) format and Satisfied/Not-satisfied branching enforces independent per-condition verification and eliminates merged-condition verification as a production risk", "AMEND lifecycle re-invocation embeds FORMULA CONTRACT RE-CHECK block at AMEND step (3)(b) before updated Item B, preventing C-22 dropout during focus-shift amendment cycles without affecting first-invocation compliance", "source-level worked substitution examples per C-23 anchor using a representative multi-word incumbent name shift the propagation contract from abstract template to demonstrated output form, making form-drift for unusual incumbent names structurally prevented at declaration time", "three reliability improvements target non-overlapping output positions (Step 0 Item A gate / AMEND PROTOCOL step 3b / INFERENCE GATE Named incumbent field) -- composable without structural interference, enabling safe combination as V-05"]}
```

---

**R7 result**: All 5 variations score **100.000 / Golden**. V-05 is the top-ranked production candidate.

Key findings:
- **V-01 confirmed**: V-05-R6 already satisfies C-22 and C-23 under the v7 rubric -- the ceiling holds.
- **V-02 > V-01 on reliability**: Blocked CONDITION (i)/(ii) gate with stop-tokens prevents merged-condition verification without adding any rubric risk.
- **V-03 closes the AMEND gap**: The inline C-22 gate in Step 0 is never re-invoked explicitly during AMEND cycles in V-01; V-03 fixes this with a `FORMULA CONTRACT RE-CHECK` block inside AMEND step (3)(b).
- **V-04 hardens C-23**: Replacing abstract `[Named incumbent]` placeholders in the anchor list with `Form:` labels + worked `e.g.` substitutions reduces anchor form-drift for multi-word or unusual incumbent names.
- **V-05 combines all three** with zero structural interference -- the three reliability axes occupy non-overlapping positions in the output flow (Step 0 Item A / AMEND step 3b / INFERENCE GATE Named incumbent field).
to [COLOR], raising score by approximately [N] pts" on every action. Color transition and score-delta are mandatory fields in all V.
- **C-07**: Item C computes a `focus_adjusted_total` that is arithmetically different from `base_cost`; the formula is carried into ARCHITECT Do-nothing cost cells and VERDICT "Not building this means:" -- demonstrably different from a no-focus run. Focus economics driven by the named incumbent's liability.
- **C-08**: STRATEGY section carries "Cover at least half the components from ARCHITECT" directive in all V.

---

#### Aspirational Criteria (weight 10 total, denominator /15)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-09 Focus constraint in 2+ downstream sections | PASS | PASS | PASS | PASS | PASS | Propagation Contract routes constraint to INERTIA / ARCHITECT / VERDICT / AMENDMENTS |
| C-10 AMEND selectively re-weaves affected sections | PASS | PASS | PASS | PASS | PASS | AMEND PROTOCOL step (2) declares affected/unaffected; step (3) rewrites only listed sections |
| C-11 Explicit constraint routing pre-section | PASS | PASS | PASS | PASS | PASS | Step 0 Item A table appears before INFERENCE GATE heading in all V |
| C-12 Named failure-mode prohibition | PASS | PASS | PASS | PASS | PASS | Item D names the forbidden pattern ("## COMPLIANCE", "## STAKEHOLDERS") explicitly in all V |
| C-13 Competitive inertia reshapes feasibility calc | PASS | PASS | PASS | PASS | PASS | Named incumbent + focus_adjusted_total change ARCHITECT ratings vs base_cost-only run |
| C-14 AMEND: 4-step protocol + unaffected-sections declaration | PASS | PASS | PASS | PASS | PASS | All 4 AMEND steps present; step (2) requires explicit unaffected-sections list with "will not be rewritten" |
| C-15 Focus economics as verifiable arithmetic formula | PASS | PASS | PASS | PASS | PASS | Item C: `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`; verifiable by subtraction |
| C-16 Propagation contract in tabular form pre-section | PASS | PASS | PASS | PASS | PASS | Item A table with 3 column headers before INFERENCE GATE in all V |
| C-17 Table first within Step 0 (before lens + economics) | PASS | PASS | PASS | PASS | PASS | Ordering enforced: Item A (table) -> Item B (lens) -> Item C (economics) -> Item D (rejection) |
| C-18 Rubric-aligned column headers + [same] back-refs | PASS | PASS | PASS | PASS | PASS | Headers: "Constraint introduced by focus" / "Section where it surfaces" / "Effect on that section"; rows 2-4 use `[same]` |
| C-19 Stated Effect cells bind to exact formula variable | PASS | PASS | PASS | PASS | PASS | AMENDMENTS row Stated Effect explicitly names `focus_adjusted_total`; closes contract-to-formula loop |
| C-20 Formula contract check as generation-time gate | PASS | PASS | PASS | PASS | PASS | Gate appears inside Step 0 before Item B; "Do not write Item B until both are confirmed" in all V |
| C-21 Named-incumbent field anchors downstream refs (2+ of 3 anchors) | PASS | PASS | PASS | PASS | PASS | Named incumbent field with 3-anchor propagation list present in all V; 2-anchor minimum stated |
| **C-22** Dual-assertion gate with per-location repair instructions | PASS | PASS | PASS | PASS | PASS | See detailed analysis below |
| **C-23** Named-incumbent field: explicit 3-anchor list + minimum-count declaration | PASS | PASS | PASS | PASS | PASS | See detailed analysis below |

---

#### C-22 Detailed Analysis

Pass condition: Two independently named conditions with separate repair instructions; single-statement gate naming only table-side fails even if output is correct.

| Variation | Gate Form | Condition (i) | Repair (i) | Condition (ii) | Repair (ii) | Verdict |
|-----------|-----------|---------------|------------|----------------|-------------|---------|
| V-01 | Inline list | `focus_adjusted_total` in at least one Stated Effect cell | "revise the AMENDMENTS row now to name the variable explicitly" | `focus_adjusted_total` as LHS of Item C equation | "revise Item C to use `focus_adjusted_total` as the equation label" | **PASS** |
| V-02 | Blocked CONDITION (i) / (ii) | Scan Effect column; token present? | "STOP. Revise AMENDMENTS row... Do not write CONDITION (ii) until satisfied." | Confirm Item C LHS label | "STOP. Adjust your Item C plan now... Do not write Item B until LHS label confirmed." | **PASS** (stronger -- sequential stop-tokens) |
| V-03 | Inline (Step 0) + RE-CHECK block in AMEND | Same as V-01 (Step 0) + (i) repeated in AMEND RE-CHECK | Same as V-01 + AMEND repair instruction | Same as V-01 (Step 0) + (ii) repeated in AMEND RE-CHECK | Same as V-01 + AMEND repair instruction | **PASS** (plus lifecycle coverage) |
| V-04 | Inline (same as V-01) | Same as V-01 | Same as V-01 | Same as V-01 | Same as V-01 | **PASS** |
| V-05 | Blocked (V-02) + AMEND RE-CHECK (V-03) | Blocked form; scan Effect column | "STOP. Revise AMENDMENTS row..." | Confirm Item C LHS | "STOP. Adjust your Item C plan..." | **PASS** (strongest: blocks + lifecycle) |

---

#### C-23 Detailed Analysis

Pass condition: Named-incumbent field lists all 3 anchors by location AND form, with explicit minimum-count declaration. C-21 PASS without the list is C-23 FAIL.

| Variation | Anchor List Present | All 3 Anchors by Location + Form | Inline Examples | Minimum-Count Declared | Verdict |
|-----------|--------------------|---------------------------------|-----------------|----------------------|---------|
| V-01 | Yes | (1) INERTIA heading form; (2) table column header form; (3) AMENDMENTS framing form | No | "At least two of these three anchors are required; all three are recommended." | **PASS** |
| V-02 | Yes (same as V-01) | Same as V-01 | No | Same as V-01 | **PASS** |
| V-03 | Yes (same as V-01) | Same as V-01 | No | Same as V-01 | **PASS** |
| V-04 | Yes | (1)-(3) with explicit `Form:` label per anchor + `e.g., if Named incumbent = "manual CSV export + shared Google Sheet"` worked substitution per anchor | Yes -- concrete substituted output per anchor | "Minimum count: At least two of these three anchors are required in the output; all three are recommended." | **PASS** (stronger -- source-level worked examples) |
| V-05 | Yes (V-04 form) | Same as V-04 | Yes (same as V-04) | Same as V-04 | **PASS** (strongest) |

---

### Composite Scores

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 15 * 10)
```

| Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-01 | 5/5 | 3/3 | 15/15 | **100.000** | YES |
| V-02 | 5/5 | 3/3 | 15/15 | **100.000** | YES |
| V-03 | 5/5 | 3/3 | 15/15 | **100.000** | YES |
| V-04 | 5/5 | 3/3 | 15/15 | **100.000** | YES |
| V-05 | 5/5 | 3/3 | 15/15 | **100.000** | YES |

All five variations achieve a perfect composite of 100.000 and clear the Golden threshold (all essential PASS, no PARTIALs, composite >= 80).

---

### Ranking

All variations tie at 100.000. Rank by production reliability -- how well the prompt prevents C-22/C-23 failures under adversarial conditions:

| Rank | Variation | Reliability improvement | Failure mode addressed |
|------|-----------|------------------------|------------------------|
| 1 | **V-05** | All three axes combined: blocked gate + AMEND RE-CHECK + inline examples | Merged-condition verification + amendment-cycle C-22 dropout + anchor form-drift |
| 2 | **V-02** | Blocked CONDITION (i)/(ii) gate with status markers and stop-tokens | Merged-condition verification in Step 0 |
| 3 | **V-03** | FORMULA CONTRACT RE-CHECK in AMEND step (3)(b) | C-22 dropout during focus-shift amendment cycles |
| 4 | **V-04** | Worked `e.g.` substitution per anchor in INFERENCE GATE | C-23 anchor form-drift for unusual multi-word incumbent names |
| 5 | **V-01** | Baseline confirm | Confirms 100.000 ceiling under v7 rubric; no new reliability axis |

Top variation: V-05 is the production promotion candidate.

---

### Excellence Signals

V-05 patterns that improve on V-01 without changing the score:

1. **Sequential stop-token gate structure**: Blocked CONDITION (i) / CONDITION (ii) format with explicit `Satisfied: proceed` / `Not satisfied: STOP` branching makes each condition a standalone stopping point. A model processing a linear checklist may treat "(i) + (ii)" as one logical unit; the block format enforces sequential halts, reducing merged-condition verification from a risk to a structural impossibility.

2. **AMEND lifecycle re-invocation**: Embedding the full FORMULA CONTRACT RE-CHECK block at step (3)(b) of the AMEND PROTOCOL (before updated Item B) means C-22 compliance is tested independently on focus-shift amendments, not just on first-invocation runs. Without this, the AMEND path relies on "update Step 0 Items A-D" being interpreted as including the gate -- an implicit dependency that can fail under context compression.

3. **Source-level substitution examples per anchor**: The V-04/V-05 INFERENCE GATE Named incumbent propagation list adds `Form:` labels and `e.g.` instantiations per anchor using a concrete multi-word incumbent name. This shifts C-23's contract from abstract template to demonstrated output -- checkable by mechanical comparison, not semantic judgment.

4. **Non-overlapping placement of all three axes**: V-02 changes live only in Step 0 Item A; V-03 changes live only in AMEND PROTOCOL step (3); V-04 changes live only in INFERENCE GATE Named incumbent field. These three positions do not interact in the output flow, making V-05's combination provably composable: no reliability improvement interferes with another.

---

### Round 7 Summary

**Rubric target**: All 15 aspirational criteria (C-09 through C-23), denominator /15.
**Result**: V-05-R6 already satisfied C-22 and C-23 -- confirmed by V-01 scoring 100.000 under v7.
**R7 achievement**: All three single-axis reliability improvements (V-02, V-03, V-04) each scored 100.000 independently. V-05 combines all three at 100.000 with demonstrably higher production stability than V-01.
**Promotion recommendation**: V-05 is ready for production. No rubric gaps remain. Next step is empirical production testing to measure C-22 PARTIAL rates between V-01 and V-05 under live topic/focus variation.
