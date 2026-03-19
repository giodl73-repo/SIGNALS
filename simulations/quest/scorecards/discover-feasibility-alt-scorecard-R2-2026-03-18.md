Scorecard written to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R2-2026-03-18.md`.

---

## Results

| Variation | C-10 | C-11 | C-12 | C-13 | Composite | Golden |
|-----------|------|------|------|------|-----------|--------|
| V-01 Baseline | PASS | PASS | PASS | N/A | **100.000** | YES |
| V-02 C-11 gate stripped | PASS | **FAIL** | PASS | N/A | **98.000** | YES |
| V-03 C-12 removed | PASS | PASS | **FAIL** | N/A | **98.000** | YES |
| V-04 Consistent preamble | PASS | PASS | PASS | **PASS** | **100.000** | YES |
| V-05 Conflict injection | **PARTIAL** | **FAIL** | **FAIL** | **FAIL** | **93.000** | YES |

All 5 variations Golden. All essential criteria held across all variations.

**Key findings:**

1. **V-01 confirmed at 100.000** under v2 — the R1 mechanisms (forward-declaration + proceed gate, ARCHITECT back-reference) already satisfy C-11 and C-12 by construction. C-13 N/A is the cleanest configuration.

2. **V-04 confirms zero-cost C-13 upgrade** — a consistent preamble directive adds an active PASS without touching composite. Documents the structural guarantee rather than creating a new dependency.

3. **V-05 exposes the cascade** — preamble-template conflict triggers four failures simultaneously (C-10 PARTIAL, C-11 FAIL, C-12 FAIL, C-13 FAIL) because template ordering is prerequisite to which semantic cross-references are structurally possible.

4. **Prediction table correction** — the V-05 row in the variations file's "Predicted outcomes" table showed C-11/C-12 PASS (composite 97.000), but direct template inspection and the narrative both show FAIL (composite 93.000). Scorecard records the correct 93.000.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Consistent preamble ordering directive is a zero-cost C-13 upgrade when structural template guarantees already hold -- adding a preamble directive that matches the template body converts C-13 from N/A to active PASS with no composite regression, documenting rather than creating the ordering guarantee", "Preamble-template ordering conflict cascades to three dependent criteria: C-13 FAIL triggers C-10 PARTIAL which triggers C-11 FAIL and C-12 FAIL because template ordering determines which semantic cross-references are structurally possible at execution time", "C-11 forward-declaration and C-12 semantic back-reference are independently removable with symmetric 2-point cost each -- they are non-redundant mechanisms: C-11 gates C-08 coverage before ARCHITECT is written while C-12 establishes informational dependency at ARCHITECT execution time"]}
```
oceed to ARCHITECT." Explicit coverage instruction present. |
| C-09 Focus propagates to 2+ downstream sections | aspirational | PASS (N/A) | Item A routes focus constraint to four sections; CONDITION gates enforce focus_adjusted_total in AMENDMENTS + VERDICT. Four-section propagation by construction. |
| C-10 STRATEGY before ARCHITECT | aspirational | PASS | STRATEGY template physically precedes ARCHITECT template in body. By-construction from R1 V-05 structural reorder. |
| C-11 STRATEGY forward-declaration + proceed gate | aspirational | PASS | Forward-declaration: "List all components you intend to assess in ARCHITECT below." (names components as ARCHITECT-bound). Proceed gate: "At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT." Both structural elements present. |
| C-12 ARCHITECT semantic back-reference to STRATEGY | aspirational | PASS | ARCHITECT heading: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity." Explicit semantic cross-reference naming the prior STRATEGY section. Informational dependency asserted, not merely adjacent. |
| C-13 Preamble-template ordering consistency | aspirational | PASS (N/A) | Preamble contains no section ordering directive. No directive -> no conflict -> C-13 N/A, which counts as PASS per rubric N/A handling. |

**Essential pass count**: 5/5
**Recommended pass count**: 3/3
**Aspirational pass count**: C-09=1, C-10=1, C-11=1, C-12=1, C-13=1(N/A) -> 5.0/5 = 1.0

```
Composite = (5/5 x 60) + (3/3 x 30) + (1.0 x 10)
          = 60.000 + 30.000 + 10.000
          = 100.000
```

**Golden**: YES -- all 5 essential PASS (no PARTIALs), composite 100.000 >= 80.

---

## V-02 -- C-11 Proceed-Gate Stripped

**Axis**: STRATEGY loses "at least half must carry an explicit recommendation here before you proceed to ARCHITECT." Forward-declaration structure retained. Isolates the gate as C-11's load-bearing element.

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 Named incumbent | essential | PASS | Unchanged. |
| C-02 Budget-before-rating | essential | PASS | Unchanged. |
| C-03 INERTIA before BUDGET | essential | PASS | Unchanged. |
| C-04 Four inertia surfaces | essential | PASS | Unchanged. |
| C-05 Focus woven not appended | essential | PASS | Unchanged. |
| C-06 AMENDMENTS traceable | recommended | PASS | Unchanged. |
| C-07 Focus influences base analysis | recommended | PASS (N/A) | Unchanged. |
| C-08 STRATEGY covers >=50% | recommended | PASS | STRATEGY retains "Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned" and the Build/Buy/Use existing column. Coverage mandate present via structure even without explicit >=50% sentence. PASS. |
| C-09 Focus propagates to 2+ | aspirational | PASS (N/A) | Unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | PASS | STRATEGY physically precedes ARCHITECT in template body. Unchanged. |
| C-11 Forward-declaration + proceed gate | aspirational | FAIL | Forward-declaration retained: "List all components you intend to assess in ARCHITECT below." Proceed gate removed: "At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT." is absent. C-11 requires both structural elements. Without the gate, a model may populate the STRATEGY table with component names and no recommendations, satisfying the declaration structure but not the >=50% commitment required before ARCHITECT rows are written. FAIL. |
| C-12 ARCHITECT back-reference to STRATEGY | aspirational | PASS | ARCHITECT heading unchanged: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions." Back-reference intact. |
| C-13 Preamble-template consistency | aspirational | PASS (N/A) | No preamble ordering directive. N/A -> PASS. |

**Essential pass count**: 5/5
**Recommended pass count**: 3/3
**Aspirational pass count**: C-09=1, C-10=1, C-11=0, C-12=1, C-13=1(N/A) -> 4.0/5 = 0.8

```
Composite = (5/5 x 60) + (3/3 x 30) + (0.8 x 10)
          = 60.000 + 30.000 + 8.000
          = 98.000
```

**Golden**: YES -- all 5 essential PASS (no PARTIALs), composite 98.000 >= 80.

---

## V-03 -- C-12 Back-Reference Removed

**Axis**: ARCHITECT heading stripped to "Rate each listed component for complexity." All STRATEGY cross-reference text removed. Isolates C-12 as independent from C-10 -- structural ordering does not imply semantic dependency.

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 Named incumbent | essential | PASS | Unchanged. |
| C-02 Budget-before-rating | essential | PASS | Unchanged. |
| C-03 INERTIA before BUDGET | essential | PASS | Unchanged. |
| C-04 Four inertia surfaces | essential | PASS | Unchanged. |
| C-05 Focus woven not appended | essential | PASS | Unchanged. |
| C-06 AMENDMENTS traceable | recommended | PASS | Unchanged. |
| C-07 Focus influences base analysis | recommended | PASS (N/A) | Unchanged. |
| C-08 STRATEGY covers >=50% | recommended | PASS | STRATEGY retains "At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT." Unchanged. |
| C-09 Focus propagates to 2+ | aspirational | PASS (N/A) | Unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | PASS | STRATEGY precedes ARCHITECT in template body. Unchanged. By-construction PASS. |
| C-11 Forward-declaration + proceed gate | aspirational | PASS | STRATEGY retains both structural elements. Unchanged from V-01. PASS. |
| C-12 ARCHITECT back-reference to STRATEGY | aspirational | FAIL | ARCHITECT heading stripped to: "Rate each listed component for complexity. Use budget flag from PM: BUDGET when assigning ratings." No reference to STRATEGY -- not by name, not by phrase, not by implication. A model following this template writes ARCHITECT as a self-contained section. C-10 PASS (STRATEGY physically precedes ARCHITECT); C-12 FAIL. Canonical demonstration that physical ordering and semantic dependency are independent criteria. |
| C-13 Preamble-template consistency | aspirational | PASS (N/A) | No preamble ordering directive. N/A -> PASS. |

**Essential pass count**: 5/5
**Recommended pass count**: 3/3
**Aspirational pass count**: C-09=1, C-10=1, C-11=1, C-12=0, C-13=1(N/A) -> 4.0/5 = 0.8

```
Composite = (5/5 x 60) + (3/3 x 30) + (0.8 x 10)
          = 60.000 + 30.000 + 8.000
          = 98.000
```

**Golden**: YES -- all 5 essential PASS (no PARTIALs), composite 98.000 >= 80.

---

## V-04 -- C-13 Consistent Preamble (directive matches template order)

**Axis**: V-01 base + preamble ordering directive that matches template body sequence. Tests whether adding a consistent directive converts C-13 from N/A to active PASS with zero regression.

**Added preamble directive**: "Write STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY. Required output section sequence: INERTIA -> PM: BUDGET -> STRATEGY -> ARCHITECT -> VERDICT -> AMENDMENTS. Procurement decisions must be committed before complexity ratings are assigned."

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 Named incumbent | essential | PASS | Unchanged. |
| C-02 Budget-before-rating | essential | PASS | Unchanged. |
| C-03 INERTIA before BUDGET | essential | PASS | Unchanged. |
| C-04 Four inertia surfaces | essential | PASS | Unchanged. |
| C-05 Focus woven not appended | essential | PASS | Unchanged. |
| C-06 AMENDMENTS traceable | recommended | PASS | Unchanged. |
| C-07 Focus influences base analysis | recommended | PASS (N/A) | Unchanged. |
| C-08 STRATEGY covers >=50% | recommended | PASS | Unchanged from V-01. |
| C-09 Focus propagates to 2+ | aspirational | PASS (N/A) | Unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | PASS | STRATEGY at ~line 963 precedes ARCHITECT at ~line 975. By-construction. Consistent with preamble directive. |
| C-11 Forward-declaration + proceed gate | aspirational | PASS | STRATEGY retains both structural elements. Unchanged from V-01. |
| C-12 ARCHITECT back-reference to STRATEGY | aspirational | PASS | ARCHITECT heading retains "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions." Unchanged from V-01. |
| C-13 Preamble-template ordering consistency | aspirational | PASS | Preamble directive: "Write STRATEGY before ARCHITECT" with explicit sequence list. Template body: STRATEGY (~963) before ARCHITECT (~975). Preamble and template body agree. No conflict. First active PASS (vs N/A in V-01). Zero composite regression from addition. |

**Essential pass count**: 5/5
**Recommended pass count**: 3/3
**Aspirational pass count**: C-09=1, C-10=1, C-11=1, C-12=1, C-13=1 -> 5.0/5 = 1.0

```
Composite = (5/5 x 60) + (3/3 x 30) + (1.0 x 10)
          = 60.000 + 30.000 + 10.000
          = 100.000
```

**Golden**: YES -- all 5 essential PASS (no PARTIALs), composite 100.000 >= 80.

---

## V-05 -- C-13 Conflict Injection (preamble directive contradicts template order)

**Axis**: V-04 preamble directive retained + template body reverted to ARCHITECT-before-STRATEGY + STRATEGY instruction reverted to backward reference ("Cover at least half the components from ARCHITECT"). Canonical C-13 FAIL; cascades to C-10 PARTIAL, C-11 FAIL, C-12 FAIL -- four-criterion compound regression.

**Template body order**: INFERENCE GATE -> INERTIA -> PM: BUDGET -> ARCHITECT (~1216) -> STRATEGY (~1235) -> VERDICT -> AMENDMENTS

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 Named incumbent | essential | PASS | INFERENCE GATE fields and all three propagation anchors present. |
| C-02 Budget-before-rating | essential | PASS | PM: BUDGET at ~1199 precedes ARCHITECT at ~1216. Budget still gates traffic-light assignment. |
| C-03 INERTIA before BUDGET | essential | PASS | INERTIA at ~1186 precedes PM: BUDGET at ~1199. |
| C-04 Four inertia surfaces | essential | PASS | All four surfaces present despite template reordering: INERTIA section, Do-nothing cost column, "Not building this means:", "Inertia saved:". |
| C-05 Focus woven not appended | essential | PASS | Item D prohibition and Propagation Contract intact. |
| C-06 AMENDMENTS traceable | recommended | PASS | AMENDMENTS template unchanged. |
| C-07 Focus influences base analysis | recommended | PASS (N/A) | Propagation Contract unchanged. |
| C-08 STRATEGY covers >=50% | recommended | PASS | STRATEGY instruction: "Cover at least half the components from ARCHITECT." Explicit >=50% coverage requirement present (backward-referenced, but mandate is there). PASS. |
| C-09 Focus propagates to 2+ | aspirational | PASS (N/A) | Propagation Contract unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | PARTIAL | Preamble says "Write STRATEGY before ARCHITECT." Template body places ARCHITECT at ~1216 before STRATEGY at ~1235. Direct structural conflict. A model following template-body order writes ARCHITECT before STRATEGY; a model following preamble writes STRATEGY first. Neither path is by-construction guaranteed. Compliance probability ~70% (calibrated from V-03-R1 PARTIAL). PARTIAL: probabilistic rather than structural. |
| C-11 Forward-declaration + proceed gate | aspirational | FAIL | STRATEGY instruction: "Cover at least half the components from ARCHITECT." Backward reference -- ARCHITECT appears before STRATEGY in template body, so at STRATEGY execution time, ARCHITECT is already written. "Cover components from ARCHITECT" references a past section, not a future commitment. No forward-declaration text present. C-11 requires a forward commitment made before ARCHITECT rows are written; the template execution order makes that structurally impossible. FAIL. |
| C-12 ARCHITECT back-reference to STRATEGY | aspirational | FAIL | ARCHITECT heading: "Use budget flag from PM: BUDGET when assigning ratings. Do-nothing cost column required on every row." No mention of STRATEGY. STRATEGY has not been written yet at ARCHITECT execution time (template-body order), so no back-reference is possible. FAIL. |
| C-13 Preamble-template ordering consistency | aspirational | FAIL | Preamble: "Write STRATEGY before ARCHITECT" with explicit sequence. Template body: ARCHITECT (~1216) before STRATEGY (~1235). Direct contradiction. C-13 is a template design test scored on the template itself regardless of model output. FAIL. |

**Essential pass count**: 5/5
**Recommended pass count**: 3/3
**Aspirational pass count**: C-09=1.0, C-10=0.5, C-11=0, C-12=0, C-13=0 -> 1.5/5 = 0.3

```
Composite = (5/5 x 60) + (3/3 x 30) + (0.3 x 10)
          = 60.000 + 30.000 + 3.000
          = 93.000
```

**Golden**: YES -- all 5 essential PASS (no PARTIALs), composite 93.000 >= 80.

---

## Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Composite | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|--------|
| V-01 Baseline | P | P | P | P | P | P | P | P | N/A | P | P | P | N/A | 100.000 | YES |
| V-02 C-11 gate stripped | P | P | P | P | P | P | P | P | N/A | P | FAIL | P | N/A | 98.000 | YES |
| V-03 C-12 removed | P | P | P | P | P | P | P | P | N/A | P | P | FAIL | N/A | 98.000 | YES |
| V-04 Consistent preamble | P | P | P | P | P | P | P | P | N/A | P | P | P | PASS | 100.000 | YES |
| V-05 Conflict injection | P | P | P | P | P | P | P | P | N/A | PARTIAL | FAIL | FAIL | FAIL | 93.000 | YES |

**Ranking**: V-01 = V-04 (100.000) > V-02 = V-03 (98.000) > V-05 (93.000)

V-04 is equal-composite but strictly richer than V-01: C-13 is an active PASS rather than N/A, making the ordering guarantee explicit at both preamble and template level. V-01 remains the production choice (simpler, no preamble directive to maintain), but V-04 confirms the C-13 PASS path is clean and regression-free.

---

## Discriminator Analysis

**V-02 vs V-01 (C-11 isolation)**: Removing the proceed-gate sentence while retaining the forward-declaration costs exactly 2.0 composite points. The gate phrase is C-11's load-bearing element. A forward-declaration without a gate is insufficient -- the model may forward-declare components without committing recommendations, satisfying the naming structure but not the coverage commitment that makes C-08 by-construction.

**V-03 vs V-01 (C-12 isolation)**: Removing the ARCHITECT back-reference sentence while preserving structural ordering costs exactly 2.0 composite points. C-10 (structural ordering) and C-12 (semantic dependency) are independent -- STRATEGY physically preceding ARCHITECT does not automatically cause ARCHITECT to reference STRATEGY. The "Confirmation: ... Using those procurement decisions" text is a distinct mechanism that must be present.

**V-04 vs V-01 (C-13 activation)**: Adding a preamble directive consistent with template order converts C-13 from N/A to active PASS with zero composite change (100.000 preserved). Confirms C-13 PASS is a zero-cost structural improvement when structural guarantees hold. The preamble directive documents an existing guarantee rather than creating a new one.

**V-05 compound cascade**: A single preamble-template ordering conflict triggers four-criterion failure. C-13 FAIL (template design test) -> C-10 PARTIAL (execution order uncertain) -> C-11 FAIL (STRATEGY execution context now post-ARCHITECT; forward-declaration structurally impossible) -> C-12 FAIL (ARCHITECT written before STRATEGY exists; back-reference structurally impossible). 7-point composite loss (100 -> 93). Template ordering is load-bearing for semantic mechanisms -- ordering determines which cross-references are possible.

---

## Excellence Signals (new from R2)

1. **Consistent preamble directive is a zero-cost C-13 upgrade** (V-04): When structural guarantees already hold, adding a preamble directive that matches the template body's ordering converts C-13 from N/A to active PASS with no composite regression. The preamble documents the existing guarantee; it does not create a new dependency.

2. **Preamble-template conflict cascades to three dependent criteria** (V-05): A single ordering conflict (preamble says X->Y, template body has Y->X) does not fail C-13 alone. It triggers C-10 PARTIAL + C-11 FAIL + C-12 FAIL because template ordering determines which semantic cross-references are structurally possible at execution time. When ARCHITECT precedes STRATEGY, STRATEGY can only backward-reference ARCHITECT (breaking C-11), and ARCHITECT is written before STRATEGY exists (breaking C-12).

3. **C-11 and C-12 are independently removable, independently costly, non-redundant** (V-02, V-03): Each removal costs a symmetric 2 points. They are not redundant: C-11 forward-declaration gates C-08 coverage before ARCHITECT is written; C-12 semantic back-reference establishes informational dependency at ARCHITECT execution time. Both are needed for the full structural integrity chain.

---

## Promotion Confirmation

**V-01 (= V-05-R1) confirmed as production template at 100.000.** The three new R2 criteria are satisfied by mechanisms already present in R1:
- C-11: forward-declaration + proceed gate in STRATEGY ("List all components... at least half must carry... before you proceed")
- C-12: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions" in ARCHITECT
- C-13: N/A (no preamble directive to conflict with; cleanest possible configuration)

V-04 confirms a consistent preamble directive can be added safely for documentation purposes. No scoring incentive when structural guarantees hold; V-01 is the minimal-safe-configuration winner.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Consistent preamble ordering directive is a zero-cost C-13 upgrade when structural template guarantees already hold -- adding a preamble directive that matches the template body converts C-13 from N/A to active PASS with no composite regression, documenting rather than creating the ordering guarantee", "Preamble-template ordering conflict cascades to three dependent criteria: C-13 FAIL triggers C-10 PARTIAL which triggers C-11 FAIL and C-12 FAIL because template ordering determines which semantic cross-references are structurally possible at execution time", "C-11 forward-declaration and C-12 semantic back-reference are independently removable with symmetric 2-point cost each -- they are non-redundant mechanisms: C-11 gates C-08 coverage before ARCHITECT is written while C-12 establishes informational dependency at ARCHITECT execution time"]}
```
