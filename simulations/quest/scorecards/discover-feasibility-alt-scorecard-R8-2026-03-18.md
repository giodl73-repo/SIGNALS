## Round 8 Scorecard -- `discover-feasibility-alt` (v6 Rubric)

### Results

| Rank | Variation | Composite | Golden? | Key failure |
|------|-----------|-----------|---------|-------------|
| 1 | **V-01** | **100.000** | Yes | -- |
| 2 | **V-02** | **99.286** | Yes | C-09 FAIL (aspirational) |
| 3 | **V-03** | **90.000** | Yes | C-07 FAIL (recommended) |
| 4 | **V-05** | **89.286** | Yes | C-07 + C-09 FAIL |
| 5 | **V-04** | **77.286** | **No** | C-05 FAIL (essential) + C-07 + C-09 cascade |

All five hypotheses confirmed against the v6 rubric.

---

### Per-variation criterion summary

**All variations**: C-01–C-04 PASS, C-06 PASS, C-08 PASS, C-10–C-18 PASS, C-13 N/A=1, C-19–C-22 PASS (structural formula properties).

The R8 axis is C-05 / C-07 / C-09 (focus active for the first time):

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05 (ess) | PASS | PASS | PASS | **FAIL** | PASS |
| C-07 (rec) | PASS | PASS | **FAIL** | **FAIL** | **FAIL** |
| C-09 (asp) | PASS | **FAIL** | PASS | **FAIL** | **FAIL** |

**Score derivations:**
- **V-01**: `(5/5 × 60) + (3/3 × 30) + (14/14 × 10) = 100.000`
- **V-02**: `(5/5 × 60) + (3/3 × 30) + (13/14 × 10) = 99.286`
- **V-03**: `(5/5 × 60) + (2/3 × 30) + (14/14 × 10) = 90.000`
- **V-05**: `(5/5 × 60) + (2/3 × 30) + (13/14 × 10) = 89.286`
- **V-04**: `(4/5 × 60) + (2/3 × 30) + (13/14 × 10) = 77.286`

---

### Excellence signals (V-01)

1. **Propagation Contract as the weave mechanism** — the four-row table (INERTIA / ARCHITECT / VERDICT / AMENDMENTS) makes C-05 structural: the model must plan focus propagation before writing any section.
2. **`focus_adjusted_total` as the economics linchpin** — the CONDITION (i)/(ii) two-phase check forces the formula token into both the table (Item A) and the equation (Item C) before Item B proceeds, making C-07 by-construction.
3. **Item D failure-mode rejection as the C-05 guard** — the explicit "Never add a standalone focus section after AMENDMENTS" prohibition converts C-05 from an inferred constraint to a structural one.
4. **Mandatory row completeness drives C-09** — all four Propagation Contract rows required (not optional) forces 4-section propagation; optional rows would default to V-02 behavior.
5. **C-05/C-07/C-09 tier stratification** — the three focus criteria span all three tiers, creating a natural failure cost gradient: appending = golden-breaking, cosmetic = 10 pts, under-propagated = 0.714 pts.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-05 is the focus golden-predicate: appending focus (V-04) breaks golden at 77.286 while woven-but-cosmetic (V-03) preserves golden at 90.000 -- structure test and effect test are independently binding", "C-07 FAIL dominates C-09 FAIL by 14x: C-07 recommended-tier costs 10 pts; C-09 aspirational-tier costs 0.714 pts at /14 denominator -- same tier-weight ratio as C-02/C-17 asymmetry from R7", "C-05 FAIL cascade multiplier: appending focus triggers C-07 FAIL + C-09 FAIL simultaneously; total 22.714 pts = 31.8x C-09-only failure; mirrors C-02/C-17 cascade pattern from R7", "C-05/C-09 independence: woven into 1 section (V-02) passes C-05 structural check while failing C-09 propagation threshold -- woven != propagated", "C-07/C-09 independence: focus in 2+ sections (V-03) passes C-09 propagation threshold while failing C-07 effect test -- propagated != effective"]}
```
 as forward commitments and states proceed gate before ARCHITECT evaluation. |
| C-12 | aspirational | PASS | ARCHITECT opens with explicit semantic cross-reference to prior STRATEGY decisions. |
| C-13 | aspirational | N/A | No preamble ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body enforces STRATEGY-before-ARCHITECT independently of any preamble directive. |
| C-15 | aspirational | PASS | No preamble-template conflict possible. C-11 and C-12 reachable by-construction. |
| C-16 | aspirational | PASS | STRATEGY body has explicit proceed-gate sentence; ARCHITECT body has explicit confirmation sentence citing STRATEGY. Both static body text. |
| C-17 | aspirational | PASS | `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` authored as static template body text preceding prerequisites block. |
| C-18 | aspirational | PASS | AMENDMENTS authors three independently-removable sub-lines per entry: (1) action line, (2) color-transition line with delta, (3) "Inertia saved:" line. |
| C-19 | aspirational | PASS | Formula structural: guard-removal costs 12 pts essential + 0.714 aspirational ~= 12.714 pts total; inference-only costs 0.714 pts. Ratio ~17.8x at /14. Essential/aspirational tier ratio preserved. |
| C-20 | aspirational | PASS | C-17 and C-18 each count 1/14 * 10 = 0.714 pts. Equal weight in aspirational denominator. |
| C-21 | aspirational | PASS | (5/5 * 60) + (3/3 * 30) = 90.000 >= 80. Aspirational failure ceiling holds structurally. |
| C-22 | aspirational | PASS | C-04 surface 4, C-06, and C-18 scored from independent evidence without inference between them. |

```
Essential:    5/5   * 60 = 60.000
Recommended:  3/3   * 30 = 30.000
Aspirational: 14/14 * 10 = 10.000   (C-13 N/A=1)
Composite: 100.000
```

**Golden. All essential PASS, all recommended PASS, all aspirational PASS or N/A. Establishes focus-active ceiling under v6 /14 denominator.**

---

### V-02 -- C-09 FAIL Only: Focus Woven but Not Propagated

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE unchanged. All fields present. |
| C-02 | essential | PASS | VERDICT score/label correct. Static iff-guard present. |
| C-03 | essential | PASS | ARCHITECT table with traffic-light ratings and RED Blockers. |
| C-04 | essential | PASS | All four inertia surfaces present including "Inertia saved:" in AMENDMENTS. |
| C-05 | essential | PASS | Focus woven into INERTIA via Propagation Contract. Content integrated, not appended. |
| C-06 | recommended | PASS | AMENDMENTS traceable with component name, color transition, and delta. |
| C-07 | recommended | PASS | INERTIA shows focus_adjusted_total changing the named incumbent's baseline cost. Analysis demonstrably different from no-focus baseline in that section. |
| C-08 | recommended | PASS | STRATEGY >= 50% component coverage. |
| C-09 | aspirational | FAIL | Focus constraint present in INERTIA only (1 section). Propagation Contract has INERTIA row only -- ARCHITECT, VERDICT, AMENDMENTS rows absent or focus-neutral. Requires 2+ distinct sections. C-05/C-09 independence: woven (C-05 PASS) does not imply propagated (C-09 PASS). |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in body. |
| C-11 | aspirational | PASS | Forward-declaration and proceed gate present. |
| C-12 | aspirational | PASS | ARCHITECT back-reference to STRATEGY present. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering enforced independently. |
| C-15 | aspirational | PASS | Cascade-safe. |
| C-16 | aspirational | PASS | Both mechanism sentences present as static body text. |
| C-17 | aspirational | PASS | Static iff-guard present as body text. |
| C-18 | aspirational | PASS | Three independent AMENDMENTS sub-lines. |
| C-19 | aspirational | PASS | Formula structural property preserved. |
| C-20 | aspirational | PASS | C-17 and C-18 equal weight. |
| C-21 | aspirational | PASS | 5/5 * 60 + 3/3 * 30 = 90 >= 80. |
| C-22 | aspirational | PASS | Three surfaces scored independently. |

```
Essential:    5/5   * 60 = 60.000
Recommended:  3/3   * 30 = 30.000
Aspirational: 13/14 * 10 =  9.286   (C-09 FAIL=0; C-13 N/A=1)
Composite: 99.286
```

**Golden. C-09 FAIL is aspirational-only -- 0.714 pt cost, golden-compatible. C-05/C-09 independence confirmed: woven into 1 section passes C-05 (structural check) while failing C-09 (propagation threshold).**

---

### V-03 -- C-07 FAIL Only: Focus Woven in 2+ Sections but Cosmetic

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE fields present. |
| C-02 | essential | PASS | VERDICT score/label correct. Static iff-guard present. |
| C-03 | essential | PASS | ARCHITECT table with traffic-light ratings and RED Blockers. |
| C-04 | essential | PASS | All four inertia surfaces present. |
| C-05 | essential | PASS | Focus woven into INERTIA and ARCHITECT (not appended). Structurally integrated. |
| C-06 | recommended | PASS | AMENDMENTS traceable with component name, color transition, delta. |
| C-07 | recommended | FAIL | Focus appears in INERTIA + ARCHITECT but does not demonstrably change the base analysis. Component ratings and VERDICT economics are identical to a no-focus run; focus content is cosmetic commentary rather than a driver of analysis outcomes. C-07/C-09 independence: present in 2+ sections (C-09 PASS) does not imply analysis changed (C-07 PASS). |
| C-08 | recommended | PASS | STRATEGY >= 50% component coverage. |
| C-09 | aspirational | PASS | Focus constraint appears in INERTIA + ARCHITECT = 2 sections. Propagation threshold satisfied. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in body. |
| C-11 | aspirational | PASS | Forward-declaration and proceed gate present. |
| C-12 | aspirational | PASS | ARCHITECT back-reference to STRATEGY present. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering enforced independently. |
| C-15 | aspirational | PASS | Cascade-safe. |
| C-16 | aspirational | PASS | Both mechanism sentences present. |
| C-17 | aspirational | PASS | Static iff-guard present. |
| C-18 | aspirational | PASS | Three independent AMENDMENTS sub-lines. |
| C-19 | aspirational | PASS | Formula structural property preserved. |
| C-20 | aspirational | PASS | C-17 and C-18 equal weight. |
| C-21 | aspirational | PASS | 5/5 * 60 + 3/3 * 30 = 90 >= 80. |
| C-22 | aspirational | PASS | Three surfaces scored independently. |

```
Essential:    5/5   * 60 = 60.000
Recommended:  2/3   * 30 = 20.000   (C-07 FAIL=0)
Aspirational: 14/14 * 10 = 10.000   (C-09 PASS; C-13 N/A=1)
Composite: 90.000
```

**Golden. C-07 FAIL is recommended-tier -- 10 pt cost, golden barely preserved (90 >= 80). Highest-cost single focus-criterion failure that does not break golden. C-07/C-09 independence confirmed: 2+ sections (C-09 PASS) != analysis changed (C-07 PASS).**

---

### V-04 -- C-05 FAIL Cascade: Focus Appended

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE fields present. |
| C-02 | essential | PASS | VERDICT score/label correct. Static iff-guard present. |
| C-03 | essential | PASS | ARCHITECT table with traffic-light ratings and RED Blockers. |
| C-04 | essential | PASS | All four inertia surfaces present in the core output. |
| C-05 | essential | FAIL | Focus content appears as a standalone section after AMENDMENTS (e.g., `## COMPLIANCE`). Template adds focus as an additive block rather than weaving it through the Propagation Contract -> section chain. Structural integration test fails regardless of content quality in the appended block. |
| C-06 | recommended | PASS | Core AMENDMENTS traceable entries unchanged (component, color transition, delta present). |
| C-07 | recommended | FAIL | Appended block does not change base section analysis. INERTIA, ARCHITECT, VERDICT written without focus integration; economics and ratings are focus-neutral. Cascade from C-05 FAIL: appending structurally prevents existing sections from being influenced. |
| C-08 | recommended | PASS | STRATEGY >= 50% component coverage. |
| C-09 | aspirational | FAIL | Focus constraint exists only in appended standalone block. No propagation into INERTIA, ARCHITECT, VERDICT, or AMENDMENTS via the existing section structure. Cascade from C-05 FAIL: an appended block is not a downstream section and cannot satisfy the 2+ propagation requirement. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in body. |
| C-11 | aspirational | PASS | Forward-declaration and proceed gate present. |
| C-12 | aspirational | PASS | ARCHITECT back-reference to STRATEGY present. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering enforced independently. |
| C-15 | aspirational | PASS | Cascade-safe. |
| C-16 | aspirational | PASS | Both mechanism sentences present. |
| C-17 | aspirational | PASS | Static iff-guard present. |
| C-18 | aspirational | PASS | Three independent AMENDMENTS sub-lines. |
| C-19 | aspirational | PASS | Formula structural property preserved. C-21 tests the formula guarantee as a structural property -- holds regardless of whether a given variation passes all essentials. |
| C-20 | aspirational | PASS | C-17 and C-18 equal weight. |
| C-21 | aspirational | PASS | (5/5 * 60) + (3/3 * 30) = 90 >= 80. Structural formula guarantee holds; C-21 tests the formula, not the variation's actual essential scores. |
| C-22 | aspirational | PASS | Three surfaces scored independently. |

```
Essential:    4/5   * 60 = 48.000   (C-05 FAIL=0)
Recommended:  2/3   * 30 = 20.000   (C-07 FAIL=0)
Aspirational: 13/14 * 10 =  9.286   (C-09 FAIL=0; C-13 N/A=1)
Composite: 77.286
```

**NOT GOLDEN. C-05 FAIL (essential) is the disqualifier; composite 77.286 < 80. C-05 is the A/B test criterion: appending focus is the structural failure the alt version exists to prevent. Cascade: C-05 FAIL simultaneously triggers C-07 FAIL + C-09 FAIL; 22.714 pts total = 31.8x C-09-only failure.**

---

### V-05 -- C-07 + C-09 Compound: Focus Woven Passively into One Section

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE fields present. |
| C-02 | essential | PASS | VERDICT score/label correct. Static iff-guard present. |
| C-03 | essential | PASS | ARCHITECT table with traffic-light ratings and RED Blockers. |
| C-04 | essential | PASS | All four inertia surfaces present. |
| C-05 | essential | PASS | Focus woven into at least one section (INERTIA) -- not appended. Structural integration satisfied. |
| C-06 | recommended | PASS | AMENDMENTS traceable with component, color transition, delta. |
| C-07 | recommended | FAIL | Focus in INERTIA only and passive: Propagation Contract has INERTIA row with no economics formula -- focus_adjusted_total not computed. Base section analysis not demonstrably changed; no focus-adjusted component ratings, no focus-driven VERDICT adjustment. C-05 PASS (structure) does not rescue C-07 (effect). |
| C-08 | recommended | PASS | STRATEGY >= 50% component coverage. |
| C-09 | aspirational | FAIL | Focus woven into 1 section only. Propagation threshold requires 2+. Compound with C-07 FAIL: passive focus in one section fails both the effect test and the propagation test simultaneously. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in body. |
| C-11 | aspirational | PASS | Forward-declaration and proceed gate present. |
| C-12 | aspirational | PASS | ARCHITECT back-reference to STRATEGY present. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering enforced independently. |
| C-15 | aspirational | PASS | Cascade-safe. |
| C-16 | aspirational | PASS | Both mechanism sentences present. |
| C-17 | aspirational | PASS | Static iff-guard present. |
| C-18 | aspirational | PASS | Three independent AMENDMENTS sub-lines. |
| C-19 | aspirational | PASS | Formula structural property preserved. |
| C-20 | aspirational | PASS | C-17 and C-18 equal weight. |
| C-21 | aspirational | PASS | 5/5 * 60 + 3/3 * 30 = 90 >= 80. |
| C-22 | aspirational | PASS | Three surfaces scored independently. |

```
Essential:    5/5   * 60 = 60.000
Recommended:  2/3   * 30 = 20.000   (C-07 FAIL=0)
Aspirational: 13/14 * 10 =  9.286   (C-09 FAIL=0; C-13 N/A=1)
Composite: 89.286
```

**Golden. C-07 + C-09 compound FAIL costs 10.714 pts total -- still golden at 89.286. Compound non-essential failures do not accumulate to golden-breaking deficit when C-05 (essential) holds.**

---

### Ranking

| Rank | Variation | Composite | Golden? | Failures |
|------|-----------|-----------|---------|---------|
| 1 | V-01 | 100.000 | Yes | none |
| 2 | V-02 | 99.286 | Yes | C-09 (asp) |
| 3 | V-03 | 90.000 | Yes | C-07 (rec) |
| 4 | V-05 | 89.286 | Yes | C-07 (rec) + C-09 (asp) |
| 5 | V-04 | 77.286 | No | C-05 (ess) + C-07 (rec) + C-09 (asp) |

Gap analysis:
- V-01 -> V-02: -0.714 (C-09 alone; aspirational cost only)
- V-02 -> V-03: -9.286 (C-07 alone; recommended vs aspirational; 14x tier ratio)
- V-03 -> V-05: -0.714 (C-09 added to C-07; additive, no escalation)
- V-05 -> V-04: -12.000 (C-05 essential; golden-breaking cliff)

---

### Excellence Signals (V-01)

1. **Propagation Contract as the weave mechanism**: the four-row table (INERTIA / ARCHITECT / VERDICT / AMENDMENTS) is what makes C-05 structural rather than instructional. It forces the model to plan focus propagation before writing any section -- without the contract, focus integration is probabilistic.

2. **focus_adjusted_total as the economics linchpin**: C-07 passes because the formula variable is named and wired in Item C before any section is written. The CONDITION (i) / CONDITION (ii) two-phase check enforces that focus_adjusted_total appears in both the table (Item A) and the equation (Item C) before Item B proceeds. This makes C-07 by-construction rather than output-dependent.

3. **Item D / failure-mode rejection as the C-05 guard**: the explicit prohibition ("Never add a standalone focus section after AMENDMENTS") directly guards against the V-04 failure mode at the template level. Negative instruction converts C-05 from an inferred constraint to a structural one.

4. **Mandatory row completeness drives C-09**: all four Propagation Contract rows are required (not optional) -- this is what drives 4-section propagation. If ARCHITECT/VERDICT/AMENDMENTS rows were optional, V-02 (INERTIA-only) would be the default behavior.

5. **C-05/C-07/C-09 tier stratification**: the three focus criteria span all three scoring tiers (essential / recommended / aspirational), creating a natural failure cost gradient: appending = golden-breaking (C-05 essential), cosmetic = 10 pts (C-07 recommended), under-propagated = 0.714 pts (C-09 aspirational). Each criterion tests a different quality dimension of the same behavior.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-05 is the focus golden-predicate: appending focus (V-04) breaks golden at 77.286 while woven-but-cosmetic (V-03) preserves golden at 90.000 -- structure test and effect test are independently binding", "C-07 FAIL dominates C-09 FAIL by 14x: C-07 recommended-tier costs 10 pts; C-09 aspirational-tier costs 0.714 pts at /14 denominator -- same tier-weight ratio as C-02/C-17 asymmetry from R7", "C-05 FAIL cascade multiplier: appending focus triggers C-07 FAIL + C-09 FAIL simultaneously; total 22.714 pts = 31.8x C-09-only failure; mirrors C-02/C-17 cascade pattern from R7", "C-05/C-09 independence: woven into 1 section (V-02) passes C-05 structural check while failing C-09 propagation threshold -- woven != propagated", "C-07/C-09 independence: focus in 2+ sections (V-03) passes C-09 propagation threshold while failing C-07 effect test -- propagated != effective"]}
```

Scorecard written to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R8-2026-03-18.md`.
