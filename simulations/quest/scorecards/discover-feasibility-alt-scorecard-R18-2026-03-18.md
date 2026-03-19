Scorecard written. Here is the final JSON block:

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Inertia-prominence framing is criterion-neutral: aggressive incumbent narrative ('holds the field', 'inertia is not passive', focus sharpens competitive case against named incumbent) does not move any criterion; free dimension beyond register axis", "V-09 floor at /42 confirmed: 78 - 10/42 = 77.762; C-23 formula monotone-increasing in N empirically anchored at N=42; C-50 mechanism-neutrality holds at N=42", "STRATEGY format (table vs. prose-list) is criterion-neutral across C-08/C-10/C-11/C-12/C-16: prose bullets with explicit Build/Buy/Use labels and proceed-gate sentence satisfy all STRATEGY mechanism criteria as well as a markdown table; format is a confirmed free dimension", "C-02+C-04 essential pair = 76.000 = C-01+C-03 canonical; two-essential-FAIL floor is pair-neutral, extending C-44; C-34 (formal register) confirmed at compound-FAIL floor", "New compound floor 65.762: C-03 FAIL (anchor propagation, 1 of 3 anchors) + C-05 cascade (C-07+C-09); first cross-essential-propagation compound; additive (12+12+10+0.238 = 34.238 pts from 100); candidate V-12 in rubric floor table"]}
```
lta (explicit signed number), Flag (explicit label) all authored. |
| C-03 | PASS | All three anchors: (1) INERTIA heading rename directive, (2) ARCHITECT "vs. named incumbent" column, (3) AMENDMENTS Inertia saved. 3 >= 2. |
| C-04 | PASS | Do-nothing cost column present; "No row may be blank" enforcement explicit. |
| C-05 | PASS | Focus active. Propagation Contract routes focus_adjusted_total to INERTIA, VERDICT, AMENDMENTS -- all three required destinations intact despite preamble framing intensification. |

**Essential: 5/5. No PARTIALs.**

### Recommended (weight 30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "(2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." explicit. |
| C-07 | PASS | focus_adjusted_total demonstrably changes INERTIA baseline and ARCHITECT ratings; base analysis visibly altered. |
| C-08 | PASS | STRATEGY present with Build/Buy/Use for all components; proceed-gate enforced. |

**Recommended: 3/3.**

### Aspirational (weight 10)

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 | PASS | Propagation Contract table rows obligate 4 named sections; C-05 PASS -> by-construction holds. 4 >= 2. |
| C-10 | PASS | STRATEGY precedes ARCHITECT in template body. |
| C-11 | PASS | Forward-declaration with proceed-gate: "Carrying all listed components forward to ARCHITECT." |
| C-12 | PASS | "Confirmation: STRATEGY: BUILD-VS-BUY is written above." |
| C-13 | PASS | Preamble directives consistent with body ordering. |
| C-14 | PASS | Body structurally places STRATEGY before ARCHITECT. |
| C-15 | PASS | Cascade-safe: C-14 PASS. |
| C-16 | PASS | Proceed-gate in STRATEGY body; confirmation in ARCHITECT body. |
| C-17 | PASS | "[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]" static guard present. |
| C-18 | PASS | Three orthogonal sub-lines in AMENDMENTS. |
| C-19-C-22 | PASS | Scoring formula asymmetry, parity, floor, independence structural properties. |
| C-23-C-27 | PASS | Cascade formula, ratio, multiplier, independence structural properties. |
| C-28-C-31 | PASS | Golden gate dual condition, ranking inversion, border, axis orthogonality. |
| C-32/C-34 | PASS | Register criterion-neutral (both poles); structural property. Intensified incumbent framing is a narrative/motivational axis, not register. |
| C-33 | PASS | 4-row Propagation Contract table present in Step 0 Item A; C-05 PASS -> by-construction guarantee holds. |
| C-35-C-42 | PASS | N/A dissolution, single-FAIL golden-compatible, PARTIAL anatomy, symmetry, tier profiles, PARTIAL gate. |
| C-43-C-50 | PASS | C-33/C-09 independence, additivity profiles, C-46 conditionality (C-05 PASS direction), isolation profile, multi-FAIL, cascade mechanism-neutrality. |

**Aspirational: 42/42.**

### Composite

`5/5 x 60 + 3/3 x 30 + 42/42 x 10 = 60 + 30 + 10 = 100.000`

**Golden: Yes.**

### New Pattern

**Inertia-prominence framing is criterion-neutral.** Phrasing the incumbent as "holding the field," treating inertia as "not passive," and directing focus to "sharpen the competitive case against the named incumbent" do not move any criterion score. The free-dimension space extends beyond the register axis (C-32/C-34) to competitive/motivational framing of the incumbent's role. No rubric criterion tests how aggressively the incumbent is positioned as the narrative antagonist.

---

## V-02 -- Lifecycle Emphasis: C-05 FAIL Cascade at /42 (V-09 Floor Confirmation)

**Hypothesis**: C-05 FAIL (C-46), C-07 FAIL, C-09 FAIL. C-33 PASS. Composite = 77.762. Not golden.

### Essential (weight 60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Feature, Team, Timeline present. |
| C-02 | PASS | All four BUDGET fields authored. |
| C-03 | PASS | (1) INERTIA heading rename, (2) ARCHITECT named-incumbent reference, (3) AMENDMENTS Inertia saved. 3 >= 2. |
| C-04 | PASS | Do-nothing cost column present; explicit value on every row enforced. |
| C-05 | FAIL | 3rd preamble directive: "conduct a dedicated focus analysis in a ## FOCUS ANALYSIS block placed immediately after AMENDMENTS. In the main analysis sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS), use base_cost only." C-46 mechanism: focus_adjusted_total absent from all three required destinations (INERTIA, VERDICT, AMENDMENTS). Step 0 table commits to propagation; downstream override voids it. |

**Essential: 4/5. C-05 FAIL.**

### Recommended (weight 30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Color-transition lines explicit per amendment. |
| C-07 | FAIL | Named sections use base_cost throughout; base analysis not demonstrably changed by focus. ## FOCUS ANALYSIS block is segregated; does not affect the base sections. |
| C-08 | PASS | STRATEGY present with Build/Buy/Use. |

**Recommended: 2/3. C-07 FAIL.**

### Aspirational (weight 10)

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 | FAIL | focus_adjusted_total in 0 named downstream sections {INERTIA, ARCHITECT, VERDICT, AMENDMENTS}. ## FOCUS ANALYSIS not a named downstream section per C-50. 0 < 2 required. |
| C-10-C-16 | PASS | STRATEGY precedes ARCHITECT; forward-declaration, proceed-gate, back-reference, mechanism texts all present. |
| C-17 | PASS | iff-guard static body text in VERDICT. |
| C-18 | PASS | Three sub-lines in AMENDMENTS. |
| C-19-C-32 | PASS | Formula and independence structural properties. |
| C-33 | PASS | Step 0 4-row Propagation Contract table structurally intact (Constraint/Section/Effect columns complete). C-33 tests Step 0 structure only -- downstream override does not affect C-33 score. |
| C-34-C-42 | PASS | Structural formula properties. |
| C-43 | PASS | C-33/C-09 scored independently. |
| C-44-C-45 | PASS | Additivity formula properties. |
| C-46 | PASS | Canonical R18 V-02 case: C-05 FAIL + C-33 PASS + C-09 FAIL coexist. Table commitment voided by downstream "[use base_cost only]" override. Four-quadrant matrix confirmed. |
| C-47-C-49 | PASS | Multi-FAIL profile formula properties. |
| C-50 | PASS | Dedicated ## FOCUS ANALYSIS isolation architecture produces same C-05->C-07+C-09 cascade as append pattern. Mechanism-neutrality empirically confirmed at N=42. |

**Aspirational: 41/42. C-09 FAIL.**

### Composite

`4/5 x 60 + 2/3 x 30 + 41/42 x 10 = 48 + 20 + 9.762 = 77.762`

**Golden: No.** Essential FAIL gate (C-05) + composite < 80.

### New Pattern

**V-09 floor at /42 confirmed: 77.762.** C-23 formula `78 - 10/N` at N=42. R17 V-02 confirmed at N=40 (77.750); R18 V-02 confirms at N=42 (77.762). Monotone increasing in N as predicted. C-50 mechanism-neutrality: dedicated ## FOCUS ANALYSIS block isolation architecture produces same cascade as the append pattern.

---

## V-03 -- Output Format: STRATEGY as Prose-List, All PASS

**Hypothesis**: STRATEGY format criterion-neutral across C-08/C-10/C-11/C-12/C-16. Composite = 100.000. Golden.

### Essential (weight 60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Feature, Team, Timeline present. |
| C-02 | PASS | All four BUDGET fields authored. |
| C-03 | PASS | (1) INERTIA heading rename, (2) ARCHITECT "vs. named incumbent" column header, (3) AMENDMENTS Inertia saved. 3 >= 2. |
| C-04 | PASS | Do-nothing cost column present; "[focus_adjusted_total or base_cost -- explicit value per row, no blanks]" enforced. |
| C-05 | N/A (PASS) | No focus active. |

**Essential: 5/5. No PARTIALs.**

### Recommended (weight 30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Color-transition lines explicit per amendment. |
| C-07 | N/A (PASS) | No focus. |
| C-08 | PASS | Each prose bullet carries explicit "Build / Buy / Use existing" label. All components covered. >=50% by construction. |

**Recommended: 3/3.**

### Aspirational (weight 10)

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 | N/A (PASS) | No focus. |
| C-10 | PASS | STRATEGY prose-list section physically precedes ARCHITECT table in body. |
| C-11 | PASS | Prose bullets forward-declare components by name; proceed-gate: "Proceed gate: every component listed above carries an explicit Build / Buy / Use existing recommendation. All listed components are committed to ARCHITECT. No new components may be added in ARCHITECT without a corresponding entry above." |
| C-12 | PASS | ARCHITECT: "Confirmation: STRATEGY: BUILD-VS-BUY is written above." |
| C-13 | PASS | No ordering conflict in preamble. |
| C-14 | PASS | Body structurally places STRATEGY before ARCHITECT regardless of format. |
| C-15 | PASS | Cascade-safe. |
| C-16 | PASS | Proceed-gate sentence in STRATEGY prose body; confirmation sentence in ARCHITECT body. Format change (table -> prose-list) does not remove mechanism text. |
| C-17 | PASS | iff-guard present in VERDICT. |
| C-18 | PASS | Three sub-lines in AMENDMENTS. |
| C-19-C-22 | PASS | Formula properties. |
| C-23-C-27 | N/A (PASS) | No focus. |
| C-28-C-42 | PASS | Golden gate, independence, formula structural properties. |
| C-43 | N/A (PASS) | No focus. |
| C-44-C-45 | PASS | Additivity formula properties. |
| C-46/C-50 | N/A (PASS) | No focus. |
| C-47-C-49 | PASS | Multi-FAIL formula properties. |

**Aspirational: 42/42.**

### Composite

`5/5 x 60 + 3/3 x 30 + 42/42 x 10 = 60 + 30 + 10 = 100.000`

**Golden: Yes.**

### New Pattern

**STRATEGY format (table vs. prose-list) is criterion-neutral across C-08/C-10/C-11/C-12/C-16.** A bulleted prose list with explicit Build/Buy/Use labels per component satisfies C-08 (>=50% coverage), C-10 (section precedes ARCHITECT), C-11 (forward-declaration with proceed-gate sentence), C-12 (ARCHITECT back-references STRATEGY by name), and C-16 (proceed-gate + confirmation texts present as static body text) as well as a markdown table. The mechanism text content is what the rubric tests -- not the format that organizes it. Format is a confirmed free dimension.

---

## V-04 -- Phrasing Register + Lifecycle Emphasis: C-02 FAIL + C-04 FAIL, Formal Register

**Hypothesis**: C-02 FAIL + C-04 FAIL. All recommended PASS. All aspirational PASS/N/A. Composite = 76.000. Not golden.

### Essential (weight 60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Feature, Team, Timeline present in INFERENCE GATE. |
| C-02 | FAIL | PM: BUDGET block absent entirely. No Estimated/Available/Delta/Flag authored. |
| C-03 | PASS | (1) "Rename this heading per anchor (1)" directive; (2) ARCHITECT "competitive position vs. named incumbent" column; (3) AMENDMENTS "Inertia saved: recaptured from [Named incumbent]." 3 >= 2. |
| C-04 | FAIL | ARCHITECT table: `Component | Rating | Estimated hours | Rationale` -- no Do-nothing cost column. RED Blockers also lack Do-nothing cost line. Column absent entirely = FAIL per C-37 anatomy. |
| C-05 | N/A (PASS) | No focus. |

**Essential: 3/5. C-02, C-04 FAIL.**

### Recommended (weight 30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "(2) This action transitions [Component] from [COLOR] to [COLOR], increasing the composite score by approximately [N] pts." explicit. |
| C-07 | N/A (PASS) | No focus. |
| C-08 | PASS | STRATEGY table with Build/Buy/Use recommendations for all components. |

**Recommended: 3/3.**

### Aspirational (weight 10)

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 | N/A (PASS) | No focus. |
| C-10-C-12 | PASS | STRATEGY precedes ARCHITECT; forward-declaration; back-reference: "Verification: STRATEGY: BUILD-VS-BUY is recorded above. Component ratings below apply the procurement decisions established there." |
| C-13 | N/A (PASS) | Preamble Directives 1-5 contain no ordering directive specifically between STRATEGY and ARCHITECT. |
| C-14-C-16 | PASS | Body enforces STRATEGY before ARCHITECT structurally; proceed-gate and confirmation texts present. |
| C-17 | PASS | "[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]" static guard present in VERDICT. |
| C-18 | PASS | Three sub-lines in AMENDMENTS: (1) action, (2) color-transition, (3) Inertia saved. |
| C-22 | PASS | C-04 FAIL (ARCHITECT column absent) does not cascade to C-04 surface 4 (AMENDMENTS Inertia saved, which IS present). C-06 (color-transition present). C-18 (sub-lines present). All three independently scored -- non-subsumption confirmed. |
| C-32/C-34 | PASS | Formal/technical register (Directives 1-5, passive constructions, "The analysis proceeds as follows") is criterion-neutral at compound-FAIL floor. C-34 canonical extension: zero-cost axis holds at formal pole at 76.000. |
| C-23-C-27 | N/A (PASS) | No focus. |
| C-33/C-43/C-46/C-50 | N/A (PASS) | No focus. |
| All others | PASS | Formula-structural properties hold. |

**Aspirational: 42/42.**

### Composite

`3/5 x 60 + 3/3 x 30 + 42/42 x 10 = 36 + 30 + 10 = 76.000`

**Golden: No.** Essential FAIL gate (2 FAILs).

### New Pattern

**C-02+C-04 essential pair = 76.000; pair-neutrality extends C-44.** The canonical two-essential-FAIL pair was C-01+C-03 (R13 V-04 = 76.000). C-02+C-04 produces the same 76.000 floor. The two-essential-FAIL deduction (24 pts = 2 x 12 pts) is pair-neutral: the floor depends only on the count of essential FAILs, not which pair fails. C-34 (formal register criterion-neutral) confirmed at compound-FAIL floor.

---

## V-05 -- Lifecycle Emphasis + Inertia Framing: C-03 FAIL + C-05 FAIL Cascade, Focus Active

**Hypothesis**: C-03 FAIL + C-05 cascade (C-07+C-09). C-33 PASS. Composite = 65.762. Not golden. New compound floor.

### Essential (weight 60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Feature, Team, Timeline present in INFERENCE GATE. |
| C-02 | PASS | Estimated, Available, Delta, Flag all authored. |
| C-03 | FAIL | Anchor (1): INERTIA heading = "INERTIA: STATUS QUO -- What the Feature Must Beat" -- not renamed to named incumbent. FAIL. Anchor (2): ARCHITECT "Rationale" column -- generic, no "vs. [Named incumbent]" reference. FAIL. Anchor (3): AMENDMENTS "Inertia saved: recaptured from [Named incumbent]" -- PASS. Count: 1 of 3. 1 < 2 required = C-03 FAIL. |
| C-04 | PASS | ARCHITECT table has "Do-nothing cost" column: "[base_cost only -- explicit value per row, no blanks]" enforced. |
| C-05 | FAIL | Same C-46 mechanism as V-02: 3rd preamble directive routes focus to ## FOCUS ANALYSIS block after AMENDMENTS; named sections carry "[Focus active: use base_cost only in this section.]". focus_adjusted_total absent from INERTIA, VERDICT, AMENDMENTS. |

**Essential: 3/5. C-03, C-05 FAIL.**

### Recommended (weight 30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "(2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." explicit. |
| C-07 | FAIL | Named sections unchanged by focus (same C-46 mechanism as V-02). Base analysis identical to no-focus baseline. |
| C-08 | PASS | STRATEGY present with Build/Buy/Use. |

**Recommended: 2/3. C-07 FAIL.**

### Aspirational (weight 10)

| ID | Verdict | Notes |
|----|---------|-------|
| C-09 | FAIL | focus_adjusted_total in 0 named downstream sections. ## FOCUS ANALYSIS excluded from section pool per C-50. 0 < 2 required. |
| C-10-C-12 | PASS | STRATEGY precedes ARCHITECT; forward-declaration; back-reference: "Confirmation: STRATEGY: BUILD-VS-BUY is written above." |
| C-13 | N/A (PASS) | Preamble 4 directives contain no ordering directive between STRATEGY/ARCHITECT. |
| C-14-C-16 | PASS | Body enforces ordering; proceed-gate and confirmation texts present as static body text. |
| C-17 | PASS | "[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]" present in VERDICT. |
| C-18 | PASS | Three sub-lines in AMENDMENTS: action, color-transition "(2) This moves...", "Inertia saved:" line. |
| C-33 | PASS | Step 0 4-row Propagation Contract table structurally intact. |
| C-44 | PASS | C-03+C-05 essential pair: additive (12 + 12 = 24 pts deduction from essential block). No amplification. |
| C-46 | PASS | C-05 FAIL + C-33 PASS + C-09 FAIL coexist -- same quadrant as V-02. Confirmed. |
| C-50 | PASS | Dedicated block isolation architecture (## FOCUS ANALYSIS) produces same cascade. |
| All others | PASS | Formula-structural properties hold; focus-inactive criteria pass N/A as applicable. |

**Aspirational: 41/42. C-09 FAIL.**

### Composite

`3/5 x 60 + 2/3 x 30 + 41/42 x 10 = 36 + 20 + 9.762 = 65.762`

**Golden: No.** Two essential FAILs (essential FAIL gate) + composite < 80.

### New Pattern

**New compound floor 65.762: C-03 FAIL (anchor propagation essential) + C-05 cascade (C-07+C-09).** First empirical data point combining a structural-propagation essential FAIL (C-03: anchor count = 1, less than 2 required) with the focus-cascade essential FAIL (C-05 -> C-07 + C-09). Costs are additive across tier boundaries: C-03 FAIL (-12 essential) + C-05 FAIL (-12 essential) + C-07 FAIL (-10 recommended) + C-09 FAIL (-0.238 aspirational) = 34.238 pts total from 100. Composite = 65.762. Not in v16 rubric floor table; candidate for V-12 if nominated as canonical.

---

## New Patterns Extracted (R18)

| # | Pattern | Source | Confirmed By |
|---|---------|--------|-------------|
| 1 | **Inertia-prominence framing is criterion-neutral.** Aggressive incumbent narrative ("holds the field," "inertia is not passive," focus sharpens competitive case against incumbent specifically) does not move any criterion. Free dimension beyond register axis. | V-01 | 100.000 Golden |
| 2 | **V-09 floor at /42 confirmed: 77.762.** C-23 formula 78 - 10/N at N=42. Monotone increase from 77.750 at /40 (R17). C-50: mechanism-neutrality holds at N=42. | V-02 | 77.762 composite |
| 3 | **STRATEGY format criterion-neutral across C-08/C-10/C-11/C-12/C-16.** Prose-list with explicit Build/Buy/Use bullets = markdown table when mechanism text (proceed-gate, confirmation sentences) is present. Format is a confirmed free dimension. | V-03 | 100.000 Golden |
| 4 | **C-02+C-04 essential pair = 76.000; pair-neutrality extends C-44.** Two-essential-FAIL floor is pair-neutral. C-34 (formal register) confirmed at compound-FAIL floor. | V-04 | 76.000 composite |
| 5 | **New compound floor 65.762: C-03 FAIL + C-05 cascade.** First cross-essential-propagation compound floor. C-03 FAIL (anchor count) + C-05->C-07+C-09 cascade. Additive, not amplifying. Candidate V-12. | V-05 | 65.762 composite |

---

## Floor Table -- v16 + R18 New Data Point

| Label | Definition | Formula | Composite | Golden? |
|-------|-----------|---------|-----------|---------|
| V-01 | All PASS | 5/5x60 + 3/3x30 + 42/42x10 | 100.000 | Yes |
| V-02 | C-33 FAIL only (prose propagation PASSES C-09, table absent) | 5/5x60 + 3/3x30 + 41/42x10 | 99.762 | Yes |
| V-03 | C-04 PARTIAL, C-33 PASS | (54/60) + 3/3x30 + 42/42x10 | 94.000 | No (PARTIAL gate) |
| V-04 | C-06 + C-08 FAIL (C-33 N/A) | 5/5x60 + 1/3x30 + 42/42x10 | 80.000 | Yes (border) |
| V-05 | C-04 PARTIAL + C-09 FAIL + C-33 FAIL | (54/60) + 3/3x30 + 40/42x10 | 93.524 | No (PARTIAL gate) |
| V-06 | C-08 FAIL, C-10 N/A (STRATEGY absent) | 5/5x60 + 2/3x30 + 42/42x10 | 90.000 | Yes |
| V-07 | C-01 + C-03 FAIL | 3/5x60 + 3/3x30 + 42/42x10 | 76.000 | No |
| V-08 | C-03 + C-08 FAIL (essential + recommended) | 4/5x60 + 2/3x30 + 42/42x10 | 78.000 | No |
| V-09 | C-05 FAIL cascade (C-05+C-07+C-09 FAIL, C-33 PASS) | 4/5x60 + 2/3x30 + 41/42x10 | 77.762 | No |
| V-10 | C-01 + C-03 + C-04 FAIL (three essential FAILs) | 2/5x60 + 3/3x30 + 42/42x10 | 64.000 | No |
| V-11 | C-01 + C-02 + C-03 + C-04 FAIL (four essential FAILs) | 1/5x60 + 3/3x30 + 42/42x10 | 52.000 | No |
| **R18-new** | **C-03 + C-05 cascade (C-03 FAIL + C-05->C-07+C-09)** | **3/5x60 + 2/3x30 + 41/42x10** | **65.762** | **No** |

R18-new detail: 36 + 20 + 9.762 = 65.762. C-03 FAIL (-12 essential) + C-05 FAIL (-12 essential) + C-07 FAIL (-10 recommended) + C-09 FAIL (-0.238 aspirational) = 34.238 total cost from 100. Falls between V-10 (64.000) and V-08 (78.000). Cross-axis compound: essential anchor-propagation FAIL + focus cascade.
