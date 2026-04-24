Scorecard written to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R4-2026-03-17.md`.

---

## Results

| Rank | Variation | Score | Band | Missing |
|------|-----------|-------|------|---------|
| **1** | **V-04** | **100.000** | Golden | — |
| **1** | **V-05** | **100.000** | Golden | — |
| 3 | V-03 | 99.500 | Golden | C-14 PARTIAL (lettered steps) |
| 4 | V-01 | 99.000 | Golden | C-18 FAIL (generic headers) |
| 4 | V-02 | 99.000 | Golden | C-17 FAIL (table third) |

**All five variations are Golden.** The two diagnostics (V-01, V-02) confirmed C-17 and C-18 are independent axes. V-03 confirmed the numbered (1)-(4) format is load-bearing for C-14 PASS — Step A-B-C-D with identical content scores PARTIAL. V-04 is the minimum-change ceiling.

**Note on V-03 score discrepancy**: Design estimated ~98.5; actual 99.5. The /10 denominator in v4 makes a C-14 PARTIAL cost only 0.5 pts (vs. 0.625 pts under v3's /8). Estimate was calibrated to the old model.

**New pattern from V-05** (potential C-19): Stated Effect cells in the propagation contract table reference `focus_adjusted_total` by exact variable name, creating a closed contract-to-formula loop. Does not score under v4 but improves production reliability by eliminating the prose-drift gap.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Stated Effect cells in the propagation contract table reference the exact formula variable (focus_adjusted_total) that the economics section will compute, creating a closed contract-to-formula loop at the token level"]}
```
PASS** | STRATEGY template: "Cover at least half the components from ARCHITECT" -- enforced by instruction |
| C-09 | **PASS** | Propagation Contract table routes constraint to 4 named sections (INERTIA -> ARCHITECT -> VERDICT -> AMENDMENTS), well above 2-section threshold |
| C-10 | **PASS** | AMEND PROTOCOL identifies affected vs. unaffected sections; re-weaves only affected sections |
| C-11 | **PASS** | Propagation Contract table (pre-section, before INFERENCE GATE) names constraint and explicitly lists downstream sections |
| C-12 | **PASS** | Item D names exact section headings to avoid ("## COMPLIANCE", "## STAKEHOLDERS") -- specificity exceeds structural-correctness bar |
| C-13 | **PASS** | Focus-adjusted do-nothing cost (base + focus_adjustment = total) demonstrably shifts competitive calculation vs. base-cost-only run |
| C-15 | **PASS** (all) | All five variations include a decomposable arithmetic formula: base + adjustment = TOTAL per sprint, verifiable by inspection. V-05 adds exact variable names `focus_adjusted_total = base_cost + focus_adjustment` -- same PASS result, stronger production signal |
| C-16 | **PASS** (all) | Every variation has a 3-column (Constraint / Section / Effect) table before INFERENCE GATE. Table positioning within Step 0 varies, but the pre-INFERENCE-GATE requirement is satisfied in all |

---

### Variation-Level Scoring (C-14, C-17, C-18)

---

#### V-01 -- C-17 Ordering Only (Table-First, Generic Headers)

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PASS** | AMEND PROTOCOL uses explicit numbered steps (1)-(4) with "Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten." -- both structure and unaffected-declaration present. Inherited from R3 V-04 base. |
| C-17 | **PASS** | Step 0 instruction reads "complete all four items in the order given -- Item A first." Item A is the table; Item B is Lens definition; Item C is Focus Economics. Table is the first element in Step 0, before lens prose and before economics formula. Binary condition satisfied. |
| C-18 | **FAIL** | Column headers are bare generics: `Constraint \| Downstream Section \| Stated Effect`. Sub-condition (1) fails: headers do not use rubric-aligned vocabulary ("Constraint introduced by focus", "Section where it surfaces", "Effect on that section"). Rows 2-4 use `[same constraint phrase as row 1]` -- a placeholder phrase, not `[same]`. Sub-condition (2) borderline but header failure alone satisfies the binary-FAIL rule. |

```
Essential:     5/5   x 60 = 60.000
Recommended:   3/3   x 30 = 30.000
Aspirational:  9/10  x 10 =  9.000   (C-18 = 0)
Total:         99.000   -- Golden
```

---

#### V-02 -- C-18 Column Semantics Only (Table Third, Rubric-Aligned Headers)

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PASS** | Same numbered (1)-(4) protocol + named unaffected declaration as V-01. Inherited from R3 V-04 base. |
| C-17 | **FAIL** | Step 0 order is: Item A = Lens definition, Item B = Focus Economics, Item C = Propagation Contract table. The table is the third element in Step 0 -- after lens prose and after economics text. Binary condition: table must precede both. Unambiguous FAIL. |
| C-18 | **PASS** | Column headers: `Constraint introduced by focus \| Section where it surfaces \| Effect on that section` -- rubric-aligned vocabulary confirmed. Rows 2-4 use `[same]` back-reference instead of verbatim constraint phrase. Both sub-conditions satisfied. |

```
Essential:     5/5   x 60 = 60.000
Recommended:   3/3   x 30 = 30.000
Aspirational:  9/10  x 10 =  9.000   (C-17 = 0)
Total:         99.000   -- Golden
```

---

#### V-03 -- C-17 + C-18 on Minimal Base (Step A-B-C-D AMEND)

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PARTIAL** | AMEND PROTOCOL uses lettered steps (Step A / Step B / Step C / Step D) rather than numbered (1)-(4). Step B carries "Declare: 'Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten.'" -- unaffected-sections declaration is present. 4-step content is complete. However, the lettered labeling style does not satisfy the "named 4-step protocol: (1) parse... (2) identify... (3) re-weave... (4) update VERDICT" pass condition as strictly as numbered format. R3 precedent: Step A-B-C variants scored PARTIAL. Structure is present; formalism is weak. Score: PARTIAL (0.5). |
| C-17 | **PASS** | Step 0 instruction: "complete all four items in the order given -- Item A first." Item A is the table. Item B is Lens. Item C is Economics. Table is first -- binary condition satisfied. Same table-first structure as V-01. |
| C-18 | **PASS** | Column headers: `Constraint introduced by focus \| Section where it surfaces \| Effect on that section` -- rubric-aligned. Rows 2-4 use `[same]` back-reference. Both sub-conditions satisfied. Same semantics as V-02. |

*Diagnostic finding: C-14 PARTIAL persists even with 4-step lettered AMEND. The numbered (1)-(4) format is load-bearing for C-14 PASS. This confirms V-04 (which adds numbered steps to the V-03 structure) is the correct ceiling upgrade path.*

*Score note: Estimated ~98.5 in variation design; actual 99.5 under v4. Discrepancy attributable to denominator shift from /8 (v3) to /10 (v4): a C-14 PARTIAL costs 0.5/10 x 10 = 0.5 pts under v4 vs. 0.5/8 x 10 = 0.625 pts under v3. Estimate was calculated against v3 proportional model.*

```
Essential:     5/5    x 60 = 60.000
Recommended:   3/3    x 30 = 30.000
Aspirational:  9.5/10 x 10 =  9.500   (C-14 = 0.5)
Total:         99.500   -- Golden
```

---

#### V-04 -- C-17 + C-18 Combined on V-04-R3 Base (Ceiling Test)

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PASS** | Numbered (1)-(4) steps + "Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten." Inherited from R3 V-04 base, unchanged. |
| C-17 | **PASS** | Step 0: "complete all four items in the order given -- Item A first." Item A = table, Item B = Lens, Item C = Economics. Table first -- binary condition satisfied. |
| C-18 | **PASS** | Headers: `Constraint introduced by focus \| Section where it surfaces \| Effect on that section` -- rubric-aligned. Rows 2-4: `[same]` back-reference. Both sub-conditions satisfied. |

```
Essential:     5/5   x 60 = 60.000
Recommended:   3/3   x 30 = 30.000
Aspirational:  10/10 x 10 = 10.000
Total:         100.000  -- Golden
```

---

#### V-05 -- Full Battery: C-17 + C-18 on V-05-R3 Base (Maximum Precision)

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PASS** | Same numbered (1)-(4) structure + named unaffected declaration as V-04. |
| C-17 | **PASS** | Item A first in Step 0, same table-first structure as V-04. |
| C-18 | **PASS** | Headers rubric-aligned; `[same]` on rows 2-4. Same as V-04. |

*Distinguishing feature vs. V-04: Stated Effect cells reference `focus_adjusted_total` by exact variable name (e.g., "How focus_adjusted_total from Item C appears in the Baseline sentence"). This creates a closed contract where the table's cells name the specific variable the economics section will compute -- wiring the contract to the formula at the token level. Does not add points under v4 (C-15 and C-16 are already PASS in both), but closes the paraphrase gap that could cause a downstream model to produce prose instead of arithmetic. Potential C-19 candidate.*

```
Essential:     5/5   x 60 = 60.000
Recommended:   3/3   x 30 = 30.000
Aspirational:  10/10 x 10 = 10.000
Total:         100.000  -- Golden
```

---

### Ranking

| Rank | Variation | Score | Band | C-14 | C-17 | C-18 | Axis |
|------|-----------|-------|------|------|------|------|------|
| **1** | **V-04** | **100.000** | Golden | PASS | PASS | PASS | C-17+C-18 on C-14-PASS base |
| **1** | **V-05** | **100.000** | Golden | PASS | PASS | PASS | V-04 + `focus_adjusted_total` in cells |
| 3 | V-03 | 99.500 | Golden | PARTIAL | PASS | PASS | C-17+C-18 on Step A-B-C-D base |
| 4 | V-01 | 99.000 | Golden | PASS | PASS | FAIL | C-17 only (generic headers) |
| 4 | V-02 | 99.000 | Golden | PASS | FAIL | PASS | C-18 only (table third) |

---

### Diagnostic Findings

1. **C-17 and C-18 are independently achievable** -- V-01 passes C-17 alone (99.0), V-02 passes C-18 alone (99.0). Both axes confirmed independent before combination.
2. **C-14 is load-bearing for reaching 100** -- V-03 has C-17+C-18 but Step A-B-C-D and scores 99.5, not 100.0.
3. **Numbered (1)-(4) format separates C-14 PASS from PARTIAL** -- Step A-B-C-D with identical 4-step content scores PARTIAL; (1)-(2)-(3)-(4) scores PASS.
4. **V-04 is the minimum-change ceiling** -- adds exactly C-17 and C-18 to R3 V-04 base; reaches 100.0.
5. **V-05 adds a production reliability upgrade not captured by v4** -- contract-to-formula token binding in Stated Effect cells is a potential C-19 criterion.

---

### Excellence Signals (V-04 / V-05)

1. **Table-first Step 0 ordering**: Item A = propagation contract table, written before lens interpretation (Item B) and before economics formula (Item C). Enforces "name the contract before deriving the costs."
2. **Rubric-aligned headers + `[same]` back-references**: Headers match the rubric's own vocabulary; repeated constraint rows use `[same]` to eliminate verbatim repetition while preserving traceability.
3. **Numbered (1)-(4) AMEND with named unaffected-sections list**: The decimal-numbered step format with explicit "Unaffected sections: [list]. Unaffected sections will not be rewritten." is the only pattern that reliably achieves C-14 PASS across rounds.
4. **(V-05 only) Stated Effect cells reference formula variable names**: `focus_adjusted_total` named inside the table's Effect cells closes the loop between the contract and the economics formula at the token level -- potential C-19 candidate.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Stated Effect cells in the propagation contract table reference the exact formula variable (focus_adjusted_total) that the economics section will compute, creating a closed contract-to-formula loop at the token level"]}
```
