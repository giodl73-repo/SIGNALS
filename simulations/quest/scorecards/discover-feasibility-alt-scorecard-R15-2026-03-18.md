Now I have everything needed. Let me evaluate all five variations.

---

# discover-feasibility-alt — Round 15 Scorecard

**Rubric**: v13 | **Denominator**: /38 | **Scoring**: `(E/5×60) + (R/3×30) + (A/38×10)`

---

## V-01: ARCHITECT Do-nothing Cost Column Absent (C-04 FAIL)

**Focus**: inactive

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Feature, Team, Timeline all present in INFERENCE GATE |
| C-02 | PASS | PM: BUDGET block unchanged; Estimated/Available/Delta/Flag all present as static template text |
| C-03 | PASS | "Minimum count: at least two of these three anchors" text intact; named incumbent propagation requirements unchanged |
| C-04 | **FAIL** | Column header "Do-nothing cost (hrs/sprint or $)" removed, per-row placeholders removed, heading directive "Do-nothing cost column required..." removed, RED Blockers "Do-nothing cost:" line removed — column entirely absent |
| C-05 | N/A | Focus inactive |
| C-06 | PASS | AMENDMENTS section unchanged; color-transition + score-delta sub-line present |
| C-07 | N/A | Focus inactive |
| C-08 | PASS | STRATEGY section unchanged |
| C-09 | N/A | Focus inactive |
| C-10 | PASS | STRATEGY physically precedes ARCHITECT in body |
| C-11 | PASS | "Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation" present |
| C-12 | PASS | "Confirmation: STRATEGY: BUILD-VS-BUY is written above" present |
| C-13 | PASS | Preamble "Write this section before ARCHITECT" consistent with body ordering |
| C-14 | PASS | Body places STRATEGY before ARCHITECT independently |
| C-15 | PASS | Cascade-safe: C-14 PASS → C-15 PASS |
| C-16 | PASS | Proceed-gate sentence in STRATEGY body; confirmation sentence in ARCHITECT body |
| C-17 | PASS | "[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]" guard present |
| C-18 | PASS | AMENDMENTS has all three sub-lines: action, color-transition, inertia-saved |
| C-19–C-22 | PASS | Structural formula properties hold |
| C-23–C-27 | N/A | Focus inactive |
| C-28–C-32 | PASS | Structural properties hold |
| C-33 | N/A | Focus inactive |
| C-34–C-42 | PASS | Structural properties hold |
| C-43 | N/A | Focus inactive |
| C-44 | PASS | Formula property: single essential FAIL → -12 pts |
| C-45 | PASS | Structural |
| C-46 | N/A | Focus inactive |

**Essential**: 4/5 (C-04 FAIL) | **Recommended**: 3/3 | **Aspirational**: 38/38

**Composite**: `4/5×60 + 3/3×30 + 38/38×10 = 48 + 30 + 10 = **88.000**`

**Golden**: No (essential FAIL gate)

**Hypothesis**: CONFIRMED. Fourth empirical confirmation of C-38 criterion-neutrality: C-04 FAIL = C-01 FAIL (R13) = C-02 FAIL (R14) = C-03 FAIL (R12) = 88.000. Essential-tier isolation profile is now confirmed for 4 of 5 essential criteria (C-05 cannot be isolated due to cascade).

---

## V-02: Prose Propagation Contract (C-33 FAIL + C-09 PASS)

**Focus**: active

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Feature, Team, Timeline present |
| C-02 | PASS | PM: BUDGET unchanged |
| C-03 | PASS | Anchors intact |
| C-04 | PASS | "Do-nothing cost column required on every row" directive present; column header and per-row cells present in ARCHITECT table; "Do-nothing cost: [focus_adjusted_total...]" in RED Blockers |
| C-05 | PASS | Focus active; prose Item A names INERTIA and VERDICT as propagation targets; Items B–D intact; INERTIA uses focus_adjusted_total; VERDICT "Not building this means:" uses focus_adjusted_total; AMENDMENTS has focus_adjustment eliminated framing |
| C-06 | PASS | AMENDMENTS unchanged |
| C-07 | PASS | Focus propagated to INERTIA and VERDICT; base analysis demonstrably changes (focus_adjusted_total in cost cells) |
| C-08 | PASS | STRATEGY unchanged |
| C-09 | PASS | Prose explicitly names INERTIA and VERDICT as sections where focus_adjusted_total surfaces (≥2 sections); C-43 mechanism: C-33 FAIL does not cascade to C-09 FAIL when prose covers 2+ sections |
| C-10 | PASS | STRATEGY before ARCHITECT |
| C-11–C-16 | PASS | Ordering/mechanism criteria all satisfied |
| C-17 | PASS | VERDICT iff-guard present |
| C-18 | PASS | AMENDMENTS three sub-lines present |
| C-19–C-22 | PASS | Structural |
| C-23–C-27 | PASS | Focus active; C-05 in essential tier; formula properties hold |
| C-28–C-32 | PASS | Structural |
| C-33 | **FAIL** | Step 0 Item A is prose paragraph — no 4-row table with Constraint/Section/Effect columns; by-construction C-09 guarantee replaced by author-discipline dependency |
| C-34–C-42 | PASS | Structural |
| C-43 | PASS | C-33 FAIL + C-09 PASS — independently scored; C-33 FAIL does not imply C-09 FAIL (prose covers 2+ sections) |
| C-44–C-45 | PASS | Structural |
| C-46 | PASS | C-05 PASS → C-46 conditionality concern not triggered; C-09 scored from downstream sections (PASS), C-33 from Step 0 (FAIL), independently |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 37/38 (C-33 FAIL)

**Composite**: `5/5×60 + 3/3×30 + 37/38×10 = 60 + 30 + 9.737 = **99.737**`

**Golden**: Yes (all essential PASS, composite ≥ 80)

**Hypothesis**: CONFIRMED. V-02 rubric floor empirically confirmed at /38 (99.730→99.737). C-43 independence holds at new denominator.

---

## V-03: C-05 Cascade at /38 (C-05 FAIL + C-07 FAIL + C-09 FAIL, C-33 PASS)

**Focus**: active

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Feature, Team, Timeline present |
| C-02 | PASS | PM: BUDGET unchanged |
| C-03 | PASS | Anchors intact |
| C-04 | PASS | "Do-nothing cost column required on every row — use base_cost for all rows" directive present; column header present with [base_cost] per row |
| C-05 | **FAIL** | Focus active but INERTIA uses [base_cost], VERDICT "Not building this means:" uses base_cost, AMENDMENTS has no focus_adjustment_eliminated block; focus_adjusted_total computed in Step 0 Item C only, explicitly declared "for reference only" with downstream sections using base_cost unconditionally |
| C-06 | PASS | AMENDMENTS unchanged format |
| C-07 | **FAIL** | Focus active but base analysis demonstrably unchanged — all downstream sections use base_cost; no rating shift attributable to focus_adjusted_total |
| C-08 | PASS | STRATEGY unchanged |
| C-09 | **FAIL** | Focus active; focus_adjusted_total appears in 0 downstream sections (INERTIA/VERDICT/AMENDMENTS all use base_cost) — below 2-section threshold |
| C-10–C-16 | PASS | Ordering/mechanism criteria satisfied |
| C-17 | PASS | VERDICT iff-guard present |
| C-18 | PASS | AMENDMENTS has three sub-lines: action, color-transition+delta, inertia-saved (base_cost only) |
| C-19–C-22 | PASS | Structural |
| C-23 | PASS | C-05 in essential tier; cascade formula 78 - 10/38 = 77.737 confirmed |
| C-24 | PASS | C-07 recommended (10 pts flat), C-09 aspirational (10/38 pts); ratio 38:1 |
| C-25 | PASS | C-05 FAIL → C-07 FAIL + C-09 FAIL; multiplier 2.2×38 + 1 = 84.6× |
| C-26–C-27 | PASS | Independence criteria scored independently |
| C-28–C-32 | PASS | Structural |
| C-33 | PASS | Step 0 has intact 4-row table with Constraint/Section/Effect columns — table structure present in Step 0 regardless of downstream override |
| C-34–C-42 | PASS | Structural |
| C-43 | PASS | C-33 PASS + C-09 FAIL — scored independently; C-43 governs criterion independence |
| C-44–C-45 | PASS | Structural |
| C-46 | PASS | C-05 FAIL + C-33 PASS + C-09 FAIL — C-46 mechanism triggered and correctly applied: C-09 scored from downstream (FAIL, all use base_cost), C-33 from Step 0 (PASS, table intact); by-construction guarantee voided by C-05 FAIL |

**Essential**: 4/5 (C-05 FAIL) | **Recommended**: 2/3 (C-07 FAIL) | **Aspirational**: 37/38 (C-09 FAIL)

**Composite**: `4/5×60 + 2/3×30 + 37/38×10 = 48 + 20 + 9.737 = **77.737**`

**Golden**: No (essential FAIL gate AND composite < 80)

**Hypothesis**: CONFIRMED. V-09 rubric floor empirically confirmed at /38. C-23 formula 78 - 10/38 = 77.737 confirmed. C-46 mechanism confirmed: C-33 PASS + C-09 FAIL coexist under C-05 FAIL.

---

## V-04: Prose Propagation + Do-nothing Column Absent (C-04 FAIL + C-33 FAIL, C-09 PASS)

**Focus**: active

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Feature, Team, Timeline present |
| C-02 | PASS | PM: BUDGET unchanged |
| C-03 | PASS | Anchors intact |
| C-04 | **FAIL** | ARCHITECT heading directive removed, column header "Do-nothing cost (hrs/sprint or $)" removed, per-row cells removed, RED Blockers "Do-nothing cost:" line removed — compound V-01 mechanism |
| C-05 | PASS | Focus active; prose Item A names INERTIA + VERDICT; Items B–D intact; INERTIA uses focus_adjusted_total; VERDICT "Not building this means:" uses focus_adjusted_total; AMENDMENTS has focus_adjustment eliminated framing |
| C-06 | PASS | AMENDMENTS "(2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." present |
| C-07 | PASS | Focus propagated via prose to INERTIA and VERDICT; base analysis demonstrably different from no-focus run |
| C-08 | PASS | STRATEGY unchanged |
| C-09 | PASS | Prose names INERTIA and VERDICT explicitly; C-43 mechanism: prose covers 2+ sections; C-05 PASS means downstream honors the commitment |
| C-10–C-16 | PASS | All ordering/mechanism criteria satisfied |
| C-17 | PASS | VERDICT iff-guard present |
| C-18 | PASS | AMENDMENTS three sub-lines present |
| C-19–C-22 | PASS | Structural |
| C-23–C-27 | PASS | Focus active; formula properties hold |
| C-28–C-32 | PASS | Structural |
| C-33 | **FAIL** | Step 0 Item A is prose — same mechanism as V-02; no 4-row table |
| C-34–C-42 | PASS | Structural |
| C-43 | PASS | C-33 FAIL + C-09 PASS — C-43 independence confirmed; prose covers 2+ sections |
| C-44–C-45 | PASS | Structural |
| C-46 | PASS | C-05 PASS → C-46 conditionality not triggered |

**Essential**: 4/5 (C-04 FAIL) | **Recommended**: 3/3 | **Aspirational**: 37/38 (C-33 FAIL)

**Composite**: `4/5×60 + 3/3×30 + 37/38×10 = 48 + 30 + 9.737 = **87.737**`

**Golden**: No (essential FAIL gate)

**Hypothesis**: CONFIRMED. New compound floor: essential FAIL (C-04, −12 pts) + isolated aspirational FAIL (C-33, −10/38 = −0.263 pts) = −12.263 pts from 100 = 87.737. C-38 × C-43 cross-pattern independence holds across the essential/aspirational tier boundary.

---

## V-05: C-01 FAIL + C-04 FAIL (Two Essential FAILs)

**Focus**: inactive

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **FAIL** | INFERENCE GATE: Team and Timeline lines removed entirely; only Feature and Named incumbent remain — two required fields absent |
| C-02 | PASS | PM: BUDGET section unchanged; all four items (Estimated/Available/Delta/Flag) present as template text |
| C-03 | PASS | "Minimum count: at least two of these three anchors are required" text intact; named incumbent propagation anchors unchanged |
| C-04 | **FAIL** | ARCHITECT Do-nothing cost column entirely removed: heading directive absent, column header absent, per-row cells absent, RED Blockers "Do-nothing cost:" line absent |
| C-05 | N/A | Focus inactive |
| C-06 | PASS | AMENDMENTS unchanged |
| C-07 | N/A | Focus inactive |
| C-08 | PASS | STRATEGY section unchanged |
| C-09 | N/A | Focus inactive |
| C-10–C-18 | PASS | All ordering/mechanism criteria satisfied; structure otherwise unchanged |
| C-19–C-22 | PASS | Structural |
| C-23–C-27 | N/A | Focus inactive |
| C-28–C-32 | PASS | Structural |
| C-33 | N/A | Focus inactive |
| C-34–C-42 | PASS | Structural |
| C-43 | N/A | Focus inactive |
| C-44 | PASS | Two-essential-FAIL additivity confirmed: C-01 + C-04 = −24 pts; formula 3/5×60 = 36 |
| C-45 | PASS | Structural |
| C-46 | N/A | Focus inactive |

**Essential**: 3/5 (C-01 FAIL + C-04 FAIL) | **Recommended**: 3/3 | **Aspirational**: 38/38

**Composite**: `3/5×60 + 3/3×30 + 38/38×10 = 36 + 30 + 10 = **76.000**`

**Golden**: No (two essential FAILs gate AND composite < 80)

**Hypothesis**: CONFIRMED. C-44 cross-criterion two-essential symmetry: C-01+C-04 = 76.000, same as C-01+C-03 (R13 V-04). Two-essential-FAIL additivity holds regardless of which pair is chosen.

---

## Ranking

| Rank | Variation | Composite | Golden | FAILs |
|------|-----------|-----------|--------|-------|
| 1 | **V-02** | **99.737** | **Yes** | C-33 only (aspirational) |
| 2 | V-01 | 88.000 | No | C-04 (essential) |
| 3 | V-04 | 87.737 | No | C-04 (essential) + C-33 (aspirational) |
| 4 | V-03 | 77.737 | No | C-05 (essential) + C-07 (recommended) + C-09 (aspirational) |
| 5 | V-05 | 76.000 | No | C-01 + C-04 (two essential) |

---

## Excellence Signals from V-02

**Why V-02 is the top scorer:**

1. **Structural substitution preserves essential compliance** — Replacing the Propagation Contract table with prose does not touch any essential criterion. All five essential criteria remain PASS because prose can still satisfy C-05 (focus_adjusted_total computed and propagated) and C-04 (Do-nothing cost column in ARCHITECT is untouched). The substitution is asymmetric: it costs only C-33 (one aspirational criterion, -0.263 pts).

2. **C-43 mechanism at /38 confirmed** — The prose names INERTIA and VERDICT explicitly, satisfying C-09's 2-section threshold despite C-33 FAIL. The denominator shift from /37 to /38 raises the V-02 floor from 99.730 to 99.737 — a 0.007 pt gain that confirms the denominator sensitivity formula.

3. **Recommended tier fully preserved** — With C-05 PASS, C-07 can also PASS (focus demonstrably changes INERTIA and VERDICT cost cells). Single aspirational FAIL leaves recommended tier intact at 3/3×30 = 30 pts.

4. **Minimum-cost axis for golden** — V-02 demonstrates the minimum-loss path for a focus-active template: prose substitution is the lightest possible deviation from 100.000, costing exactly 10/38 = 0.263 pts. Any other single FAIL costs ≥10 pts (essential or recommended tier), making C-33 isolation the golden-optimal failure mode.

---

## New Patterns

| Pattern | Source | What it confirms |
|---------|--------|-----------------|
| C-38 fourth confirmation: C-04 FAIL = 88.000 | V-01 | Essential-tier isolation profile now empirically confirmed for C-01 (R13), C-02 (R14), C-03 (R12), C-04 (R15) — only C-05 remains unconfirmable in isolation due to cascade |
| New compound floor 87.737 | V-04 | Essential FAIL (−12) + isolated aspirational FAIL (−10/38 = −0.263) = −12.263 from 100; C-38 × C-43 cross-pattern additivity holds across the essential/aspirational tier boundary |
| C-44 cross-criterion symmetry: C-01+C-04 = 76.000 | V-05 | Two-essential-FAIL floor holds for any pairing — C-01+C-04 produces the same composite as C-01+C-03 (R13); confirms two-essential-FAIL additivity is criterion-pair-independent |

---

```json
{"top_score": 99.737, "all_essential_pass": true, "new_patterns": ["C-38 fourth empirical confirmation: C-04 isolated FAIL = 88.000, closing essential-tier isolation profile for 4 of 5 criteria (C-01/C-02/C-03/C-04 all confirmed at 88.000)", "New compound floor 87.737: essential FAIL (-12) + isolated aspirational FAIL (-10/38) strictly additive across tier boundary; C-38 x C-43 cross-pattern independence holds", "C-44 cross-criterion two-essential symmetry confirmed: C-01+C-04 = 76.000, same as C-01+C-03 (R13); two-essential-FAIL floor is criterion-pair-independent"]}
```
