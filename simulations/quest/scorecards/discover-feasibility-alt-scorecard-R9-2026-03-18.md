```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["Essential PARTIAL is composite-independent: V-03 at 94.000 and V-05 at 93.474 are not golden despite composite >= 80; the PARTIAL rule operates outside the 80-threshold gate entirely", "PARTIAL inverts composite-to-golden ranking: V-03 (94.000) not golden, V-04 (80.000) golden -- 14-point composite advantage overridden by one PARTIAL on an essential criterion", "C-09 cost confirmed at 0.526 pts under v7 /19 denominator (was 0.714 at /14); C-07 vs C-09 ratio now 19:1, confirming C-24", "Two recommended FAILs = golden border: C-06 + C-08 compound costs exactly 20 pts, landing at 80.000 minimum golden; a third recommended FAIL drops to 70.000", "C-06/C-08 axis is orthogonal to focus axis: STRATEGY/AMENDMENTS degradation (V-04) has zero interaction with C-05/C-07/C-09 focus criteria -- independently satisfiable pairs"]}
```

---

**Scorecard written** to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R9-2026-03-18.md`.

**Summary**:

| Variation | Composite | Golden? | Key failure |
|-----------|-----------|---------|-------------|
| V-01 | 100.000 | Yes | none |
| V-02 | 99.474 | Yes | C-09 FAIL (0.526 pts) |
| V-03 | 94.000 | **No** | C-04 PARTIAL |
| V-05 | 93.474 | **No** | C-04 PARTIAL + C-09 FAIL |
| V-04 | 80.000 | Yes (border) | C-06 + C-08 FAIL |

The critical R9 finding: **PARTIAL inverts the ranking**. V-03 (94.000) and V-05 (93.474) fail golden while V-04 (80.000) passes — a 14-point composite advantage erased by one essential PARTIAL. This is composite-independent by design: no amount of aspirational or recommended passing can recover from an essential PARTIAL.
ated != effective |

---

## V-01 -- Focus Active Golden Baseline (v7)

**Axis**: Full golden template, focus active, 4-row Propagation Contract, all mechanisms present.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | INFERENCE GATE fields (Feature/Team/Timeline) all present and non-empty. |
| C-02 | PASS | VERDICT has score/label with consistent range logic; static iff-guard gates prerequisites block. |
| C-03 | PASS | ARCHITECT table uses GREEN/YELLOW/RED traffic lights; RED Blockers template has all three sub-fields (blocker/Lift condition/Do-nothing cost). |
| C-04 | PASS | All 4 surfaces: (1) INERTIA Baseline sentence, (2) Do-nothing cost column required on every ARCHITECT row ("required on every row"), (3) VERDICT "Not building this means:", (4) AMENDMENTS "Inertia saved:" per sub-line 3. |
| C-05 | PASS | 4-row Propagation Contract wires focus into INERTIA/ARCHITECT/VERDICT/AMENDMENTS. Item D explicitly rejects standalone focus section. No "## COMPLIANCE" block permitted. |
| C-06 | PASS | AMENDMENTS template sub-line 2 mandates "[Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." |
| C-07 | PASS | focus_adjusted_total propagated to INERTIA (Do-nothing cost cell), ARCHITECT (rating rationale), VERDICT ("Not building this means:"), AMENDMENTS (inertia arithmetic). Demonstrably changes all downstream sections. |
| C-08 | PASS | STRATEGY proceed gate: "at least half must carry an explicit Build / Buy / Use existing recommendation" + mandatory column format. >= 50% structural guarantee. |
| C-09 | PASS | 4-row Propagation Contract directs focus into INERTIA + ARCHITECT + VERDICT + AMENDMENTS = 4 distinct sections >= 2. |
| C-10 | PASS | Template body: STRATEGY section appears before ARCHITECT section. By-construction ordering. |
| C-11 | PASS | STRATEGY names all components as ARCHITECT-bound forward commitments; proceed gate sentence: "Carrying all listed components forward to ARCHITECT. ARCHITECT will rate each component..." |
| C-12 | PASS | ARCHITECT opens: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions..." -- semantic back-reference by name. |
| C-13 | N/A | No explicit ordering directive in preamble; STRATEGY section body text enforces ordering independently. |
| C-14 | PASS | Template body places STRATEGY before ARCHITECT independently of any preamble directive. Ordering is body-structural. |
| C-15 | PASS | C-14 PASS => cascade-safe: C-11 and C-12 are by-construction reachable; no preamble-template conflict can degrade them to probabilistic. |
| C-16 | PASS | Proceed-gate sentence (STRATEGY body): "Carrying all listed components forward to ARCHITECT." Confirmation sentence (ARCHITECT body): "Confirmation: STRATEGY: BUILD-VS-BUY is written above." Both present as static body text. |
| C-17 | PASS | VERDICT prerequisites block preceded by static iff-guard: "[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]" |
| C-18 | PASS | AMENDMENTS template independently authors: (1) action line naming component, (2) "This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.", (3) "Inertia saved: recaptured from [Named incumbent]: ..." All three sub-lines separately present. |
| C-19 | PASS | Formula preserves essential/aspirational tier ratio: guard-removal (C-17 FAIL + C-02 FAIL) costs 12 + 10/19 pts vs inference-only (C-17 FAIL alone) costs 10/19 pts. Multiplier = 22.8x at /19. Essential-tier activation dominates. |
| C-20 | PASS | C-17 and C-18 each count as 1/19 toward aspirational denominator. Equal weight; no asymmetric incentive. |
| C-21 | PASS | (5/5 x 60) + (3/3 x 30) = 90.000 >= 80 -- structural formula property, independent of N. |
| C-22 | PASS | AMENDMENTS surfaces C-04/C-06/C-18 scored independently: C-18 FAIL could occur without C-04/C-06 FAIL (V-04 R7 evidence); C-04/C-06 PASS does not imply C-18 PASS. Non-subsuming confirmed. |
| C-23 | PASS | C-05 assigned to essential tier. Cascade composite = (4/5 x 60) + (2/3 x 30) + ((N-1)/N x 10) = 78 - 10/N < 80 for all N >= 1. Golden-predicate holds unconditionally. |
| C-24 | PASS | C-07 in recommended tier (10 pts flat); C-09 in aspirational tier (10/19 = 0.526 pts at /19). Ratio 19:1. Tier assignments confirmed. |
| C-25 | PASS | C-05 FAIL (appended) semantically implies C-07 FAIL (integration precondition not met) + C-09 FAIL (0 sections < 2). Total cascade = 12 + 10 + 0.526 = 22.526 pts = 42.8x C-09-only. Entailment holds by definition of appended focus. |
| C-26 | PASS | C-05 and C-09 evaluated independently. Woven-once satisfies C-05 structural test while potentially failing C-09 threshold -- demonstrated by V-02 design. Non-subsuming confirmed. |
| C-27 | PASS | C-09 and C-07 evaluated independently. Propagated-but-cosmetic passes C-09 section-count while failing C-07 effect test -- demonstrated by V-03 R8 design. Non-subsuming confirmed. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 19/19 (C-13 N/A = PASS)

```
Composite = (5/5 x 60) + (3/3 x 30) + (19/19 x 10)
          = 60 + 30 + 10
          = 100.000
```

**Golden: YES** -- all essential PASS (no PARTIALs), composite 100.000 >= 80.

---

## V-02 -- C-09 FAIL Only: INERTIA-only Propagation Contract (v7 Denominator Check)

**Axis**: Focus woven into INERTIA only (1-row contract). C-05 PASS (woven, not appended). C-07 PASS (focus_adjusted_total changes INERTIA economics). C-09 FAIL (1 section < 2 required).

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | INFERENCE GATE fields present. |
| C-02 | PASS | VERDICT score/label/prerequisites iff-guarded. |
| C-03 | PASS | ARCHITECT traffic lights + RED Blockers sub-fields intact (Do-nothing cost present in RED Blockers at base_cost). |
| C-04 | PASS | All 4 surfaces: (1) INERTIA Baseline with focus_adjusted_total, (2) Do-nothing cost on every ARCHITECT row (base_cost; no ARCHITECT contract row, but column instruction is "required"), (3) VERDICT "Not building this means:" with base_cost, (4) AMENDMENTS "Inertia saved:" sub-line 3. |
| C-05 | PASS | Focus is woven into INERTIA via 1-row INERTIA Focus Contract. Item D prohibits standalone section. Focus is NOT appended -- structural test passes. |
| C-06 | PASS | AMENDMENTS template retains explicit color-transition sub-line: "This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." |
| C-07 | PASS | focus_adjusted_total appears in INERTIA Do-nothing cost cell and Baseline sentence, demonstrably changing the named incumbent's per-sprint cost vs. base_cost. Economically meaningful change in INERTIA section. |
| C-08 | PASS | STRATEGY proceed gate requires >= 50% explicit Build/Buy/Use coverage. Intact from V-01. |
| C-09 | FAIL | 1-row Propagation Contract: focus surfaces in INERTIA only. ARCHITECT/VERDICT/AMENDMENTS rows absent; downstream sections use base_cost, not focus_adjusted_total. Focus present in 1 section < 2 required threshold. |
| C-10 | PASS | STRATEGY physically precedes ARCHITECT in template body. |
| C-11 | PASS | STRATEGY forward-declaration and proceed gate sentence intact. |
| C-12 | PASS | ARCHITECT "Confirmation: STRATEGY: BUILD-VS-BUY is written above." Semantic back-reference present. |
| C-13 | N/A | No preamble ordering directive. |
| C-14 | PASS | Body ordering enforces STRATEGY before ARCHITECT independently. |
| C-15 | PASS | C-14 PASS => cascade-safe. |
| C-16 | PASS | Proceed-gate and confirmation sentences present as body text in respective sections. |
| C-17 | PASS | Static iff-guard present on prerequisites block in VERDICT. |
| C-18 | PASS | Three independent sub-lines in AMENDMENTS template. |
| C-19 | PASS | Structural formula property preserved. |
| C-20 | PASS | C-17 and C-18 equal weight. |
| C-21 | PASS | (5/5 x 60) + (3/3 x 30) = 90.000 >= 80. |
| C-22 | PASS | Three AMENDMENTS surfaces scored independently. |
| C-23 | PASS | C-05 essential tier; cascade composite < 80 at any N. |
| C-24 | PASS | C-07 recommended (10 pts), C-09 aspirational (0.526 pts). Ratio 19:1 confirmed. |
| C-25 | PASS | Semantic entailment C-05 FAIL => C-07 FAIL + C-09 FAIL holds by definition. |
| C-26 | PASS | V-02 is the canonical C-26 evidence case: focus woven into exactly 1 section passes C-05 structural test (not appended) while failing C-09 propagation threshold (1 < 2). Evaluated independently -- non-subsuming confirmed. |
| C-27 | PASS | C-09 and C-07 scored against own conditions independently. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 18/19 (C-09 FAIL=0; C-13 N/A=PASS)

```
Composite = (5/5 x 60) + (3/3 x 30) + (18/19 x 10)
          = 60 + 30 + 9.474
          = 99.474
```

**Golden: YES** -- all essential PASS, composite 99.474 >= 80.

**C-09 cost under v7**: 10/19 = **0.526 pts** (was 0.714 at R8's /14 denominator). C-07 vs C-09 ratio = **19:1** at /19, confirming C-24.

---

## V-03 -- C-04 PARTIAL: Do-Nothing Cost Column Optional

**Axis**: ARCHITECT table Do-nothing cost column downgraded from mandatory to conditional. Surface 2 present but incomplete (some rows blank). 4-row Propagation Contract intact; C-05/C-07/C-09 all PASS.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | INFERENCE GATE fields present. |
| C-02 | PASS | VERDICT score/label/prerequisites iff-guarded. |
| C-03 | PASS | ARCHITECT traffic lights intact. RED Blockers Do-nothing cost sub-field removed from template, but no RED components produced under this template's conditional column instruction -- "No RED components" acceptable. |
| C-04 | PARTIAL | Surface 2 degraded: ARCHITECT column instruction changed to "include where cost is estimable and material -- leave blank if unknown." Cell instruction: "[N hrs/sprint if estimable; leave blank if not yet quantified]." Do-nothing cost column IS present in the table structure but value on every row is not guaranteed -- some rows will be blank. Surfaces 1 (INERTIA Baseline), 3 (VERDICT "Not building this means:"), 4 (AMENDMENTS "Inertia saved:") all PASS. PARTIAL because surface 2 conditionally populated. |
| C-05 | PASS | 4-row Propagation Contract intact. focus_adjusted_total woven through all four sections. Item D prohibits standalone section. |
| C-06 | PASS | AMENDMENTS color-transition sub-line intact: explicit "[Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." |
| C-07 | PASS | focus_adjusted_total propagated to INERTIA/ARCHITECT/VERDICT/AMENDMENTS via 4-row contract; demonstrably changes base analysis. ARCHITECT section retains "[If focus active: deliver on the ARCHITECT row...]" directive. |
| C-08 | PASS | STRATEGY >= 50% proceed gate intact. |
| C-09 | PASS | 4-row contract -> 4 sections >= 2. |
| C-10 | PASS | STRATEGY before ARCHITECT in body. |
| C-11 | PASS | Forward-declaration + proceed gate intact. |
| C-12 | PASS | ARCHITECT semantic back-reference to STRATEGY. |
| C-13 | N/A | No preamble ordering directive. |
| C-14 | PASS | Body ordering enforces STRATEGY before ARCHITECT. |
| C-15 | PASS | Cascade-safe. |
| C-16 | PASS | Proceed-gate + confirmation sentences in body. |
| C-17 | PASS | Static iff-guard on prerequisites. |
| C-18 | PASS | Three independent sub-lines in AMENDMENTS template. |
| C-19 | PASS | Structural formula property preserved. |
| C-20 | PASS | C-17/C-18 equal weight. |
| C-21 | PASS | 90.000 >= 80. |
| C-22 | PASS | Three AMENDMENTS surfaces non-subsuming. |
| C-23 | PASS | C-05 essential tier; cascade holds. |
| C-24 | PASS | Tier assignments confirmed. |
| C-25 | PASS | Semantic entailment holds. |
| C-26 | PASS | C-05/C-09 scored independently. |
| C-27 | PASS | C-09/C-07 scored independently against own conditions. |

**Essential**: 4.5/5 (C-04 PARTIAL = 0.5) | **Recommended**: 3/3 | **Aspirational**: 19/19 (C-13 N/A=PASS)

```
Composite = (4.5/5 x 60) + (3/3 x 30) + (19/19 x 10)
          = 54 + 30 + 10
          = 94.000
```

**Golden: NO** -- C-04 PARTIAL on essential criterion. PARTIAL on any essential criterion fails golden threshold regardless of composite score (94.000 > 80 is irrelevant).

---

## V-04 -- C-06 + C-08 FAIL: Amendment Traceability + Strategy Coverage Degraded

**Axis**: STRATEGY drops mandatory Build/Buy/Use format -> C-08 FAIL. AMENDMENTS color-transition sub-line vague ("note any rating change") -> C-06 FAIL. Full 4-row Propagation Contract intact; C-05/C-07/C-09 PASS.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | INFERENCE GATE fields present. |
| C-02 | PASS | VERDICT score/label/prerequisites iff-guarded (static guard present). |
| C-03 | PASS | ARCHITECT traffic lights + RED Blockers with all three sub-fields (blocker/Lift condition/Do-nothing cost retained in RED Blockers template). |
| C-04 | PASS | ARCHITECT section: "Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable." Column instruction intact; value on every row guaranteed by template. All 4 surfaces present. |
| C-05 | PASS | 4-row Propagation Contract intact. focus_adjusted_total woven through all sections. Item D prohibits standalone section. |
| C-06 | FAIL | AMENDMENTS color-transition sub-line degraded: "Note any rating change this action enables." does not mandate "[Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." Output will lack explicit component name + color transition + delta. |
| C-07 | PASS | Full Propagation Contract with focus_adjusted_total in all four downstream sections. ARCHITECT section directive "[deliver on the ARCHITECT row...]" intact. Focus demonstrably changes base analysis. |
| C-08 | FAIL | STRATEGY column renamed "Procurement Notes"; cell instruction: "[Build / Buy / Use existing or approach notes]" -- not mandatory explicit format. Proceed gate simplified to "Proceeding to ARCHITECT with the components listed above." No >= 50% coverage mandate. Template does not structurally guarantee >= 50% explicit Build/Buy/Use in output. |
| C-09 | PASS | 4-row Propagation Contract -> 4 sections >= 2. |
| C-10 | PASS | STRATEGY before ARCHITECT in body (unchanged from V-01). |
| C-11 | PASS | Components named in STRATEGY table; forward-declaration mechanism present. Simplified proceed gate "Proceeding to ARCHITECT with the components listed above" declares components as ARCHITECT-bound. Structural forward-commitment mechanism passes (C-11 is a mechanism test, not a coverage test). |
| C-12 | PASS | ARCHITECT: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement notes..." -- semantic back-reference to STRATEGY by name. |
| C-13 | N/A | No preamble ordering directive. |
| C-14 | PASS | Body enforces STRATEGY before ARCHITECT. |
| C-15 | PASS | Cascade-safe. |
| C-16 | PASS | Proceed-gate sentence ("Proceeding to ARCHITECT...") in STRATEGY body; confirmation sentence ("Confirmation: STRATEGY: BUILD-VS-BUY is written above") in ARCHITECT body. Both present as static text. |
| C-17 | PASS | Static iff-guard present on prerequisites block. |
| C-18 | PASS | AMENDMENTS template has three sub-line slots: (1) action line "[Action for COMPONENT: ...]", (2) rating note "Note any rating change this action enables.", (3) "Inertia saved: recaptured from [Named incumbent]: ..." Three slots independently present -- template authoring passes. C-06 FAIL is the output-level consequence of slot 2 being underspecified; C-18 tests slot presence, not slot precision. C-06 and C-18 independently satisfiable -- confirms C-22. |
| C-19 | PASS | Structural formula property preserved. |
| C-20 | PASS | C-17/C-18 equal weight. |
| C-21 | PASS | 90.000 >= 80. |
| C-22 | PASS | V-04 is a C-22 evidence case: C-18 PASS (three sub-line slots present) + C-06 FAIL (underspecified slot 2 -> output lacks explicit color/delta) + C-04 PASS (surface 4 "Inertia saved:" intact). Three surfaces scored independently from distinct evidence. Non-subsuming confirmed: C-18 PASS does not imply C-06 PASS. |
| C-23 | PASS | C-05 essential tier; cascade < 80. |
| C-24 | PASS | Tier assignments confirmed. |
| C-25 | PASS | Semantic entailment holds. |
| C-26 | PASS | C-05/C-09 independent. |
| C-27 | PASS | C-09/C-07 independent. |

**Essential**: 5/5 | **Recommended**: 1/3 (C-06 FAIL, C-07 PASS, C-08 FAIL) | **Aspirational**: 19/19 (C-13 N/A=PASS)

```
Composite = (5/5 x 60) + (1/3 x 30) + (19/19 x 10)
          = 60 + 10 + 10
          = 80.000
```

**Golden: YES (border)** -- all essential PASS, composite exactly 80.000. Two recommended FAILs cost exactly 20 pts, landing at the minimum golden threshold.

---

## V-05 -- C-04 PARTIAL + C-09 FAIL Compound

**Axis**: V-02 modification (INERTIA-only contract -> C-09 FAIL) + V-03 modification (optional Do-nothing cost column -> C-04 PARTIAL). Both defects active simultaneously.

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | INFERENCE GATE fields present. |
| C-02 | PASS | VERDICT score/label/prerequisites iff-guarded. |
| C-03 | PASS | ARCHITECT traffic lights + RED Blockers intact (same conditional column as V-03; no RED components). |
| C-04 | PARTIAL | V-03 modification: Do-nothing cost column optional ("leave blank if unknown"). Surface 2 present but incomplete. Surfaces 1/3/4 intact. |
| C-05 | PASS | Focus woven into INERTIA via 1-row contract (not appended). Item D prohibits standalone section. |
| C-06 | PASS | AMENDMENTS color-transition sub-line intact: explicit color/delta format. |
| C-07 | PASS | focus_adjusted_total in INERTIA Do-nothing cost and Baseline sentence -- demonstrably changes INERTIA economics vs. base_cost. |
| C-08 | PASS | STRATEGY >= 50% proceed gate intact (V-03 does not modify STRATEGY). |
| C-09 | FAIL | V-02 modification: INERTIA-only Focus Contract (1 row). ARCHITECT/VERDICT/AMENDMENTS rows absent; focus present in 1 section < 2 required. |
| C-10 | PASS | STRATEGY before ARCHITECT. |
| C-11 | PASS | Forward-declaration + proceed gate intact. |
| C-12 | PASS | ARCHITECT semantic back-reference to STRATEGY. |
| C-13 | N/A | No preamble ordering directive. |
| C-14 | PASS | Body ordering enforces STRATEGY before ARCHITECT. |
| C-15 | PASS | Cascade-safe. |
| C-16 | PASS | Proceed-gate + confirmation sentences in body. |
| C-17 | PASS | Static iff-guard on prerequisites. |
| C-18 | PASS | Three independent sub-lines in AMENDMENTS template. |
| C-19 | PASS | Structural formula property preserved. |
| C-20 | PASS | C-17/C-18 equal weight. |
| C-21 | PASS | 90.000 >= 80. |
| C-22 | PASS | Three AMENDMENTS surfaces non-subsuming. |
| C-23 | PASS | C-05 essential tier; cascade < 80. |
| C-24 | PASS | Tier assignments confirmed. |
| C-25 | PASS | Semantic entailment holds. |
| C-26 | PASS | Compound evidence for C-26: V-05 woven into 1 section (INERTIA) passes C-05 (not appended) while failing C-09 (1 < 2 sections). Non-subsuming confirmed. |
| C-27 | PASS | C-09/C-07 scored independently. |

**Essential**: 4.5/5 (C-04 PARTIAL = 0.5) | **Recommended**: 3/3 | **Aspirational**: 18/19 (C-09 FAIL=0; C-13 N/A=PASS)

```
Composite = (4.5/5 x 60) + (3/3 x 30) + (18/19 x 10)
          = 54 + 30 + 9.474
          = 93.474
```

**Golden: NO** -- C-04 PARTIAL on essential criterion. Composite 93.474 > 80 is irrelevant; PARTIAL mechanism is composite-independent.

**PARTIAL override confirmed**: V-05 composite (93.474) > R8/V-05 composite (89.474), yet R8/V-05 was golden (no PARTIAL) and R9/V-05 is not. The PARTIAL rule operates outside the 80-threshold gate entirely.

---

## Composite Comparison Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| **V-01** | 5/5 | 3/3 | 19/19 | **100.000** | **Yes** |
| **V-02** | 5/5 | 3/3 | 18/19 | **99.474** | **Yes** |
| **V-03** | 4.5/5 (C-04 PARTIAL) | 3/3 | 19/19 | **94.000** | **No** |
| **V-05** | 4.5/5 (C-04 PARTIAL) | 3/3 | 18/19 | **93.474** | **No** |
| **V-04** | 5/5 | 1/3 | 19/19 | **80.000** | **Yes (border)** |

**Composite ranking**: V-01 > V-02 > V-03 > V-05 > V-04
**Golden ranking**: V-01 = V-02 = V-04 (golden) > V-03 = V-05 (not golden)

**PARTIAL inversion**: V-03 at 94.000 and V-05 at 93.474 rank 3rd and 4th by composite but are not golden. V-04 at 80.000 ranks last by composite but is golden. A 14-point composite advantage is overridden by the PARTIAL mechanism.

---

## Excellence Signals (from V-01, top-scoring variation)

**E-01 -- Four-row Propagation Contract as golden architecture**: The 4-row Item A table (INERTIA/ARCHITECT/VERDICT/AMENDMENTS) is the single mechanism that delivers C-05, C-07, and C-09 simultaneously. Removing any row downgrades the output predictably and independently. The contract is the load-bearing structure for the entire focus axis.

**E-02 -- Formula Contract CHECK gates ordering**: The CONDITION (i) / CONDITION (ii) self-verification loop before Item B ensures the model cannot proceed without placing `focus_adjusted_total` in both the table AND the formula. This is a runtime enforcement mechanism built into the template body -- not a preamble instruction.

**E-03 -- Item D as structural rejection, not behavioral instruction**: "No section heading matching the focus dimension will appear after AMENDMENTS. All focus content flows through the rows in Item A's table." Item D explicitly names the failure mode it prevents. The rejection is structural (prohibit a heading) not behavioral (advise the model). This makes C-05 by-construction rather than probabilistic.

**E-04 -- Proceed-gate names forbidden additions**: "no new components may be added in ARCHITECT without a corresponding STRATEGY entry." The V-01 proceed gate does not just hand off components -- it closes the loop by prohibiting orphan ARCHITECT rows. This makes C-08 by-construction (ARCHITECT can only have STRATEGY-traced components).

**E-05 -- Three independent sub-line slots in AMENDMENTS**: Sub-lines 1/2/3 map directly onto C-04 surface 4 / C-06 / C-18 at the three rubric tiers (essential/recommended/aspirational). Removing any sub-line degrades exactly one criterion at a different tier -- this structural orthogonality confirms all three AMENDMENTS criteria can be independently satisfied or failed.

---

## New Patterns (R9)

1. **Essential PARTIAL is composite-independent**: V-03 at 94.000 and V-05 at 93.474 are both not golden despite composite >= 80. The PARTIAL rule operates entirely outside the 80-threshold gate -- no composite calculation is needed to determine golden when an essential PARTIAL is present.

2. **PARTIAL inverts composite -> golden ranking**: V-03 (94.000) is not golden; V-04 (80.000) is. This is the strongest composite-golden inversion to date: a 14-point composite advantage overridden by a single PARTIAL. Essential PARTIAL is categorically distinct from essential FAIL (which reduces composite) and aspirational FAIL (which never breaks golden alone).

3. **C-09 cost confirmed at 0.526 pts under v7 /19 denominator**: 10/19 = 0.526 pts (was 10/14 = 0.714 at R8's /14 denominator). C-07 vs C-09 ratio now 19:1, confirming C-24 holds at /19.

4. **Two recommended FAILs = golden border**: C-06 + C-08 compound costs exactly 20 pts (2 x 10), landing at 80.000 minimum golden threshold. A third recommended FAIL would give 70.000 -- not golden. The golden floor under two recommended FAILs is exactly 80.000 regardless of aspirational performance.

5. **C-06/C-08 axis is orthogonal to focus axis**: V-04's STRATEGY coverage degradation and AMENDMENTS traceability degradation have zero interaction with focus weaving (C-05), focus propagation (C-09), or focus effectiveness (C-07). The two recommended degradations are independently satisfiable from the focus criteria.
