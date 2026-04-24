---

# Scorecard: `discover-feasibility-alt` — Round 2

**Rubric**: v2 (36 criteria: 5 essential / 3 recommended / 28 aspirational)

---

## New Criteria Results (C-32 through C-36)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-32 Named component inventory | FAIL | **PASS** | FAIL | FAIL | **PASS** |
| C-33 Dual-layer independence | PASS | PASS | PASS | PASS | PASS |
| C-34 3-verb unaffected declaration | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| C-35 MANIFEST formula variable bindings | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |
| C-36 Composability without regression | N/A | N/A | N/A | N/A | **PASS** |

**C-33 is a free PASS** from the baseline — V-05-R1 already had both enforcement layers (Item E manifest in Step 0 + per-section `[INERTIA MANIFEST Surface N]` markers). Neither layer can substitute for the other. Primary R2 hypothesis confirmed.

---

## Scores (fixed denominator = 28)

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-05 Combined | **100.00** | YES |
| 2 | V-02 Named Inventory | **99.11** | YES |
| 2 | V-03 3-Verb Declaration | **99.11** | YES |
| 4 | V-04 Formula Bindings | **98.93** | YES |
| 5 | V-01 Baseline confirm | **98.75** | YES |

All five variations Golden. V-05 is the production promotion candidate.

**Note on V-04 vs V-02/V-03 ordering**: A FAIL→PASS improvement (+1 credit, +0.357 pts) outweighs a PARTIAL→PASS improvement (+0.5 credit, +0.179 pts). The expected table had this reversed; fixed denominator 28 is canonical.

---

## All Hypotheses Confirmed

C-32 FAIL / C-33 PASS / C-34 FAIL / C-35 PARTIAL in V-01 — all predicted, all confirmed. V-05 achieves C-36 PASS with zero regressions on C-01 through C-31.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["named component inventory as distinct pre-list artifact before STRATEGY table converts coverage from write-time emergence to declare-time binding by separating the list from the table it constrains", "three-verb prohibition placed in the declaration step rather than only in the downstream execution instruction front-loads the contract at categorization time so all operations are forbidden the moment a section is labeled unaffected", "formula variable forward-references in manifest entries convert a location checklist into a typed document by naming the exact computation that populates each declared surface at declaration time"]}
```
---|------|------|------|
| C-06 | AMENDMENTS traceable to RED/YELLOW with color transition + score delta | PASS | PASS | PASS | PASS | PASS |
| C-07 | Focus integration visibly influences base analysis | PASS | PASS | PASS | PASS | PASS |
| C-08 | STRATEGY covers >= 50% of ARCHITECT components | PASS | PASS | PASS | PASS | PASS |

**Evidence (all PASS, all variations — inherited from R1 baseline):**
- **C-06**: "One action per RED or YELLOW component. Include all three lines -- do not drop any." Action -> color transition -> score delta -> Inertia saved. Format enforced in all variations.
- **C-07**: `focus_adjusted_total = base_cost + focus_adjustment` demonstrably changes INERTIA cost, ARCHITECT ratings, VERDICT "Not building this means:", AMENDMENTS savings vs. no-focus base_cost run.
- **C-08**: All variations: STRATEGY section precedes ARCHITECT; "The ARCHITECT table must contain exactly the components named here -- no more, no fewer." By-construction coverage in V-02/V-05 (COMPONENT INVENTORY pre-list). >= 50% guaranteed in all.

---

### Aspirational Criteria C-09 through C-31 (confirmed PASS from R1)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Focus constraint propagates to 2+ downstream sections | PASS | PASS | PASS | PASS | PASS |
| C-10 | AMEND selectively re-weaves only affected sections | PASS | PASS | PASS | PASS | PASS |
| C-11 | Explicit constraint routing in pre-section orientation step | PASS | PASS | PASS | PASS | PASS |
| C-12 | Named failure-mode prohibition | PASS | PASS | PASS | PASS | PASS |
| C-13 | Competitive inertia framing reshapes feasibility calculation | PASS | PASS | PASS | PASS | PASS |
| C-14 | AMEND PROTOCOL: 4-step with unaffected-sections declaration | PASS | PASS | PASS | PASS | PASS |
| C-15 | Focus economics as verifiable arithmetic formula | PASS | PASS | PASS | PASS | PASS |
| C-16 | Propagation contract in tabular form before INFERENCE GATE | PASS | PASS | PASS | PASS | PASS |
| C-17 | Propagation contract table precedes lens + economics in Step 0 | PASS | PASS | PASS | PASS | PASS |
| C-18 | Column headers rubric-aligned + back-references for repeated values | PASS | PASS | PASS | PASS | PASS |
| C-19 | Stated Effect cells bind to exact formula variable names | PASS | PASS | PASS | PASS | PASS |
| C-20 | Formula contract check converts binding into generation-time gate | PASS | PASS | PASS | PASS | PASS |
| C-21 | Named-incumbent field anchors >= 2 of 3 downstream references | PASS | PASS | PASS | PASS | PASS |
| C-22 | Dual-assertion gate with per-location repair instructions | PASS | PASS | PASS | PASS | PASS |
| C-23 | 3-anchor propagation list with minimum-count declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 | Sequential stop-token structure with Satisfied/Not-satisfied branching | PASS | PASS | PASS | PASS | PASS |
| C-25 | AMEND PROTOCOL embeds FORMULA CONTRACT RE-CHECK at step 3(b) | PASS | PASS | PASS | PASS | PASS |
| C-26 | Per-anchor Form: labels with worked substitution examples | PASS | PASS | PASS | PASS | PASS |
| C-27 | Three reliability axes at non-overlapping structural positions | PASS | PASS | PASS | PASS | PASS |
| C-28 | STRATEGY precedes ARCHITECT (section ordering) | PASS | PASS | PASS | PASS | PASS |
| C-29 | Ordering constraints carry causal rationale (because-clauses) | PASS | PASS | PASS | PASS | PASS |
| C-30 | INERTIA MANIFEST pre-declares all 4 C-04 surfaces in Step 0 | PASS | PASS | PASS | PASS | PASS |
| C-31 | Combined C-28+C-29+C-30 compose without regression | PASS | PASS | PASS | PASS | PASS |

**Stability note**: C-09 through C-31 (23 criteria) confirmed PASS at 100.0 in R1 (V-05-R1). None of the R2 variation changes touches the Propagation Contract table structure, INFERENCE GATE anchor list, AMEND PROTOCOL steps 3-4, VERDICT format, OC-1 through OC-5 rationale blocks, Item A-D content, or INERTIA MANIFEST structure. No regressions from V-01 through V-05.

---

### New Criteria: C-32, C-33, C-34, C-35, C-36

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-32 | STRATEGY pre-declares named component inventory constraining ARCHITECT rows | **FAIL** | **PASS** | **FAIL** | **FAIL** | **PASS** |
| C-33 | INERTIA MANIFEST + per-section reminders: independent dual-layer enforcement | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| C-34 | AMEND unaffected-sections declaration prohibits all three operations by name | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |
| C-35 | INERTIA MANIFEST entries include named formula variable bindings | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** | **PASS** |
| C-36 | Combined C-32+C-33+C-34+C-35 compose without regression on C-01-C-31 | **N/A** | **N/A** | **N/A** | **N/A** | **PASS** |

**Evidence:**

---

**C-32: STRATEGY pre-declares named component inventory constraining ARCHITECT row construction**

Pass condition: STRATEGY section declares an explicit named component inventory -- a labeled list of components from which ARCHITECT table rows will be drawn. Ordering alone (STRATEGY before ARCHITECT) does not satisfy C-32; a distinct named artifact is required.

- **V-01**: STRATEGY says "Every component listed here becomes a row in the ARCHITECT table" and "List all components you plan to evaluate in ARCHITECT. The ARCHITECT table must contain exactly the components named here." The component list IS the STRATEGY table rows, filled at write time. There is no distinct labeled pre-list artifact separate from the table itself. C-32 requires a named artifact that pre-exists the table. The table and the inventory are the same object. **FAIL**

- **V-02**: Adds COMPONENT INVENTORY block before the STRATEGY table:
  ```
  COMPONENT INVENTORY (declare all component names before filling the table):
  - [Component 1 -- name only; one line per component]
  - [Component 2]
  - [Component N]
  All rows in the table below and all rows in the ARCHITECT table must draw component names from this list exclusively -- no more, no fewer.
  ```
  OC-4 updated: "ARCHITECT rows draw component names exclusively from STRATEGY's named COMPONENT INVENTORY." ARCHITECT: "component names must match STRATEGY's COMPONENT INVENTORY exactly (see OC-4). Do not introduce component names not declared in the COMPONENT INVENTORY." Explicit named pre-list as distinct artifact; table below and ARCHITECT must match it. **PASS**

- **V-03**: Same as V-01. No COMPONENT INVENTORY block added (V-03 only modifies AMEND PROTOCOL step (2)). **FAIL**

- **V-04**: Same as V-01. No COMPONENT INVENTORY block added (V-04 only modifies Item E Surfaces 1 and 4). **FAIL**

- **V-05**: Contains COMPONENT INVENTORY block identical to V-02. OC-4 and ARCHITECT binding identical to V-02. **PASS**

---

**C-33: INERTIA MANIFEST and per-section reminders operate as independent dual-layer enforcement**

Pass condition: Both layers present and structurally independent: (1) MANIFEST pre-declares all four surfaces in Step 0; (2) each of the four output sections contains its own inline inertia enforcement instruction or reminder.

All five variations inherit the V-05-R1 structure which already has both layers:
- **Layer 1** (Step 0 Item E): INERTIA MANIFEST block pre-declares all four surfaces with location, value type, and required form checkboxes. Present in all five variations (identical Item E across all).
- **Layer 2** (per-section inline markers):
  - INERTIA: `[INERTIA MANIFEST Surface 1 -- write Baseline sentence here.]`
  - ARCHITECT: `[INERTIA MANIFEST Surface 2 -- Do-nothing cost column required on every row. No blank cells.]`
  - VERDICT: `[INERTIA MANIFEST Surface 3 -- write "Not building this means:" line here.]`
  - AMENDMENTS: `[INERTIA MANIFEST Surface 4 -- "Inertia saved:" line required on every amendment item.]`

Both layers are structurally independent: Layer 1 (Step 0) could be absent and Layer 2 markers would still fire, and vice versa. End-of-AMENDMENTS INERTIA MANIFEST VERIFICATION also present in all variations.

**PASS in all five variations.** This confirms the primary hypothesis of R2: V-05-R1 already satisfies dual-layer independence without modification. C-33 is a free PASS from the baseline.

---

**C-34: AMEND PROTOCOL unaffected-sections declaration explicitly prohibits all three surface-modification operations**

Pass condition: The declaration in step (2) explicitly names and prohibits all three operations: (1) rewriting, (2) summarizing, and (3) referencing. Test is lexical -- all three verbs must appear in the step (2) declaration text.

- **V-01**: AMEND PROTOCOL step (2) declares: `"Unaffected sections will not be rewritten."` -- one verb only. Step (3) does include all three verbs: "Do not rewrite, summarize, or reference any section listed as unaffected in step (2)." But C-34 requires all three in the declaration itself (step (2)), not only in a downstream execution instruction (step (3)). **FAIL**

- **V-02**: AMEND PROTOCOL step (2) is identical to V-01. V-02 changes are scoped to STRATEGY and ARCHITECT only. **FAIL**

- **V-03**: AMEND PROTOCOL step (2) changed to: `"Unaffected sections will not be rewritten, summarized, or referenced."` All three verbs present in the declaration. Step (3) retains "Do not rewrite, summarize, or reference" (unchanged). Both locations carry the full three-verb prohibition. **PASS**

- **V-04**: AMEND PROTOCOL step (2) is identical to V-01. V-04 changes are scoped to Item E Surfaces 1 and 4 only. **FAIL**

- **V-05**: AMEND PROTOCOL step (2): `"Unaffected sections will not be rewritten, summarized, or referenced."` Identical to V-03. **PASS**

---

**C-35: INERTIA MANIFEST entries include named formula variable bindings forward-referencing the economics layer**

Pass condition: Each of the four MANIFEST entries includes a named formula variable binding -- an explicit reference by exact variable name identifying which formula variable will compute that surface's value. PARTIAL if at least one but not all four entries carry a binding.

Entry-by-entry assessment for V-01 (baseline):

| Surface | V-01 Content | Has Variable Binding? |
|---------|-------------|----------------------|
| S-1 (INERTIA Baseline) | "Value type: prose sentence. Named incumbent required." | NO -- no formula variable named |
| S-2 (ARCHITECT Do-nothing cost) | "Value type: `focus_adjusted_total` if focus active; `base_cost` if not." | YES -- exact variable names present |
| S-3 (VERDICT Not-building line) | "Value type: one sentence referencing `focus_adjusted_total` (if active)" | YES -- `focus_adjusted_total` named |
| S-4 (AMENDMENTS Inertia saved) | "Value type: cost delta in same units as `base_cost`." | NO -- `base_cost` is a unit reference; `focus_adjusted_total` absent as the Total line variable |

S-1 and S-4 lack bindings: 2 of 4 pass -> **PARTIAL** for V-01/V-02/V-03.

- **V-04**: Adds formula variable bindings to S-1 and S-4:
  - S-1: "Formula variable: `base_cost` (no-focus run) or `focus_adjusted_total` (focus active) -- the cost-per-sprint value that fills this sentence is the value computed in Step 0 Item C." **PASS**
  - S-4: "Formula variable: `focus_adjusted_total` -- the Total line in the 'Inertia saved:' entry must equal the `focus_adjusted_total` value from Step 0 Item C." **PASS**
  All four entries carry named variable bindings. **PASS**

- **V-05**: Item E identical to V-04. All four surfaces have named variable bindings. **PASS**

---

**C-36: Combined C-32+C-33+C-34+C-35 compose without regression on C-01 through C-31**

Pass condition: When C-32, C-33, C-34, and C-35 are all PASS, every criterion from C-01 through C-31 must score PASS. N/A when the combined improvement is not fully active (at least one of the four is FAIL or PARTIAL).

- **V-01 through V-04**: At least one of C-32/C-34/C-35 is FAIL or PARTIAL. Combined improvement not fully active. **N/A**

- **V-05**: C-32 PASS, C-33 PASS, C-34 PASS, C-35 PASS -- all four active. Composability check:
  - C-01 through C-31: confirmed PASS (see stability note above)
  - V-05 changes vs V-01: (a) COMPONENT INVENTORY pre-list added to STRATEGY; (b) ARCHITECT draw instruction strengthened to "must match COMPONENT INVENTORY exactly"; (c) OC-4 rationale updated to reference "named COMPONENT INVENTORY"; (d) step (2) three-verb prohibition; (e) Surfaces 1 and 4 formula variable bindings; (f) inline Surface 1 reminder updated to "Cost = base_cost or focus_adjusted_total from Step 0 Item C"; (g) inline Surface 4 reminder updated to "Total must equal focus_adjusted_total from Step 0 Item C."
  - None of these touches: Propagation Contract table columns (C-16/C-17/C-18/C-19), stop-token gate structure (C-24), AMEND RE-CHECK block (C-25), anchor list in INFERENCE GATE (C-23/C-26), three-axis non-overlapping positions (C-27), section ordering (C-28), OC block rationale (C-29), or MANIFEST block location in Step 0 (C-30).
  - No regression on any C-01 through C-31 criterion. **PASS**

---

## Scoring Worksheet

| Variation | Essential (5) | Recommended (3) | Aspirational (/28) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 5/5 = 60 | 3/3 = 30 | 24.5/28 = 8.75 | **98.75** | YES |
| V-02 | 5/5 = 60 | 3/3 = 30 | 25.5/28 = 9.11 | **99.11** | YES |
| V-03 | 5/5 = 60 | 3/3 = 30 | 25.5/28 = 9.11 | **99.11** | YES |
| V-04 | 5/5 = 60 | 3/3 = 30 | 25.0/28 = 8.93 | **98.93** | YES |
| V-05 | 5/5 = 60 | 3/3 = 30 | 28.0/28 = 10.00 | **100.00** | YES |

*Aspirational numerator: PASS=1, PARTIAL=0.5, FAIL/N/A=0. Denominator fixed at 28.*

**Aspirational breakdown by variation:**

| Variation | C-09-C-31 (23) | C-32 | C-33 | C-34 | C-35 | C-36 | Numerator |
|-----------|---------------|------|------|------|------|------|-----------|
| V-01 | 23 PASS (+23) | FAIL (+0) | PASS (+1) | FAIL (+0) | PARTIAL (+0.5) | N/A (+0) | **24.5** |
| V-02 | 23 PASS (+23) | PASS (+1) | PASS (+1) | FAIL (+0) | PARTIAL (+0.5) | N/A (+0) | **25.5** |
| V-03 | 23 PASS (+23) | FAIL (+0) | PASS (+1) | PASS (+1) | PARTIAL (+0.5) | N/A (+0) | **25.5** |
| V-04 | 23 PASS (+23) | FAIL (+0) | PASS (+1) | FAIL (+0) | PASS (+1) | N/A (+0) | **25.0** |
| V-05 | 23 PASS (+23) | PASS (+1) | PASS (+1) | PASS (+1) | PASS (+1) | PASS (+1) | **28.0** |

---

## Variation Rankings

| Rank | Variation | Composite | C-32 | C-33 | C-34 | C-35 | C-36 | Golden |
|------|-----------|-----------|------|------|------|------|------|--------|
| 1 | V-05 Combined | **100.00** | PASS | PASS | PASS | PASS | PASS | YES |
| 2 | V-02 Named Inventory | **99.11** | PASS | PASS | FAIL | PARTIAL | N/A | YES |
| 2 | V-03 3-Verb Declaration | **99.11** | FAIL | PASS | PASS | PARTIAL | N/A | YES |
| 4 | V-04 Formula Bindings | **98.93** | FAIL | PASS | FAIL | PASS | N/A | YES |
| 5 | V-01 Baseline confirm | **98.75** | FAIL | PASS | FAIL | PARTIAL | N/A | YES |

---

## Hypothesis Validation

| Hypothesis | Predicted | Actual | Confirmed? |
|-----------|-----------|--------|------------|
| C-32 FAIL in V-01 | FAIL | FAIL | YES |
| C-33 PASS in V-01 (free PASS from R1 baseline) | PASS | PASS | YES |
| C-34 FAIL in V-01 | FAIL | FAIL | YES |
| C-35 PARTIAL in V-01 (Surfaces 1 and 4 missing) | PARTIAL | PARTIAL | YES |
| C-36 N/A in V-01 through V-04 | N/A | N/A | YES |
| V-02 adds C-32 PASS | PASS | PASS | YES |
| V-03 adds C-34 PASS | PASS | PASS | YES |
| V-04 upgrades C-35 PARTIAL -> PASS | PASS | PASS | YES |
| V-05 achieves C-36 PASS (composability) | PASS | PASS | YES |
| V-05 composite ~100 | ~100 | 100.00 | YES |

All R2 hypotheses confirmed. No surprises.

---

## Projection Accuracy

| Variation | Expected (variations doc) | Actual | Deviation |
|-----------|--------------------------|--------|-----------|
| V-01 | ~98.6 | 98.75 | +0.15 |
| V-02 | ~98.9 | 99.11 | +0.21 |
| V-03 | ~98.9 | 99.11 | +0.21 |
| V-04 | ~99.3 | 98.93 | -0.37 |
| V-05 | ~100 | 100.00 | 0 |

**Note on V-04 deviation**: The expected table ordered V-04 above V-02/V-03 (~99.3 vs ~98.9). With fixed denominator 28, V-04 scores 98.93 -- below V-02/V-03 at 99.11. The difference: a C-35 upgrade from PARTIAL to PASS nets +0.5/28x10 = +0.179 pts, while a C-32 or C-34 FAIL->PASS nets +1/28x10 = +0.357 pts. V-02 and V-03 each achieve a larger gain because they convert a full FAIL to PASS, while V-04 converts a PARTIAL (already worth 0.5 credit) to PASS for only +0.5 additional credit. The expected table overestimated V-04 and underestimated V-02/V-03. Using N/A-excluded denominator (27 for V-01-V-04) would match V-04's expected ~99.3 but fails to match the V-01/V-02/V-03 expected values. Fixed denominator 28 (consistent with R1 methodology) is the canonical approach.

---

## Excellence Signals from V-05

V-05 is the only variation achieving 100.0. Three structural patterns from V-02/V-03/V-04 compose cleanly:

**Pattern 1 -- Named component inventory as distinct pre-list artifact (C-32 pattern).** The COMPONENT INVENTORY bullet block is declared before the STRATEGY table and before the ARCHITECT table. The constraint is not "cover all components in the table" (same object) but "fill the table from this named list" (two objects that must match). This separation converts the coverage from a write-time property (emerged when the table is written) to a declare-time property (the list exists before writing begins). The downstream ARCHITECT reference "must match STRATEGY's COMPONENT INVENTORY exactly" creates a named binding at both ends. The pattern generalizes: any structural coverage requirement is stronger when the list and the content it constrains are distinct artifacts with explicit cross-references, rather than the same artifact serving both roles.

**Pattern 2 -- Three-verb prohibition placed at declaration time, not execution time (C-34 pattern).** The distinction between step (2) (declaration: what sections are affected vs. unaffected) and step (3) (execution: how to handle those sections) is load-bearing. Placing prohibitions only in the execution instruction creates a sequential dependency -- the prohibition is encountered only after the declaration phase. Placing all three verbs in the declaration means the prohibition is part of the categorization act: the moment a section is labeled "unaffected," all three operations are simultaneously forbidden. The pattern generalizes: front-load the contract at declaration time rather than at execution time; any multi-step protocol where declaration and execution are separated gains enforcement strength when the constraints travel with the declaration.

**Pattern 3 -- Formula variable forward-references in manifest entries (C-35 pattern).** Adding "Formula variable: `focus_adjusted_total`" to Surfaces 1 and 4 makes the INERTIA MANIFEST a typed document rather than a location checklist. Each entry now declares not only where the value goes but which computation produces it. The MANIFEST and the Item C economics formula are cross-linked by variable name at declaration time. The pattern generalizes: any pre-declaration checklist gains enforcement strength when its entries include explicit forward-references to the computation that will populate them, converting the checklist from a presence check to a type check.

---

## Key Findings

1. **C-33 PASS confirmed at baseline (V-01).** The primary R2 structural confirmation: V-05-R1 already satisfies dual-layer inertia enforcement without modification. Item E pre-declares in Step 0; `[INERTIA MANIFEST Surface N]` markers fire inline in all four output sections. The two layers are structurally independent and neither substitutes for the other.

2. **Three gaps confirmed and individually repaired.** C-32 gap (STRATEGY table vs. named inventory artifact) repaired in V-02. C-34 gap (one-verb vs. three-verb declaration) repaired in V-03. C-35 gap (Surfaces 1 and 4 missing variable bindings) repaired in V-04. Each repair is scoped to a single structural position with no cross-interference.

3. **V-05 achieves C-36 PASS -- composability confirmed.** All three improvements compose without regression on C-01 through C-31. V-05 is the first variation in the discover-feasibility-alt series to achieve all 28 aspirational criteria simultaneously.

4. **Score ordering: V-02 = V-03 > V-04 > V-01.** C-32/C-34 FAIL->PASS (+0.357 pts each) yields a larger per-criterion gain than C-35 PARTIAL->PASS (+0.179 pts net). A FAIL resolved contributes twice the credit gain of a PARTIAL resolved.

5. **All five variations are Golden.** The R1 baseline was already above 98.0 before any R2 improvements. V-05 at 100.0 is the production promotion candidate.

---

## Recommendation

**Promote V-05 as the v2 production prompt.** It is the only variation where C-32, C-33, C-34, C-35, and C-36 all PASS. All 28 aspirational criteria pass. No prior criterion regresses.

**Next round**: R2 confirms no structural gaps remain in the v2 rubric. If R3 is run, suggested adversarial axes:
- No-focus path: does the COMPONENT INVENTORY block behave correctly when focus is inactive and Items A-D are skipped?
- AMEND with threshold adjustment: does the three-verb step (2) declaration interact correctly with threshold-based amendments (different affected-section profile than focus shifts)?
- Inventory divergence risk: does a model maintain consistency between COMPONENT INVENTORY bullet list and STRATEGY table rows across multi-turn generation?

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["named component inventory as distinct pre-list artifact before STRATEGY table converts coverage from write-time emergence to declare-time binding by separating the list from the table it constrains", "three-verb prohibition placed in the declaration step rather than only in the downstream execution instruction front-loads the contract at categorization time so all operations are forbidden the moment a section is labeled unaffected", "formula variable forward-references in manifest entries convert a location checklist into a typed document by naming the exact computation that populates each declared surface at declaration time"]}
```
