## discover-feasibility-alt — Round 5 Scoring (Rubric v4)

### Scoring Setup

**Formula:**
- Essential (C-01–C-05): `(passed/5) × 60` — each criterion worth 12 pts
- Recommended (C-06–C-08): `(passed/3) × 30` — each criterion worth 10 pts
- Aspirational (C-09–C-16): `(PASS+N/A)/8 × 10` — each criterion worth 1.25 pts

**Focus axis criteria for this round:** C-05 (essential), C-07 (recommended), C-09 (aspirational)

---

### V-01 — Focus-Active Baseline

**Axis:** Golden template (V-01-R4 body) with focus activated. Hypothesis: focus criteria convert N/A → PASS at zero composite cost.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | INFERENCE GATE has Feature, Team, Timeline, Named incumbent |
| C-02 | PASS | VERDICT score + label + prerequisites consistent |
| C-03 | PASS | ARCHITECT rows have traffic-light ratings; RED Blockers present |
| C-04 | PASS | All four inertia surfaces present |
| C-05 | PASS | Focus woven into INERTIA, ARCHITECT, VERDICT, AMENDMENTS via Propagation Contract; no standalone section appended |
| C-06 | PASS | AMENDMENTS trace to named components with color-transition and score-delta |
| C-07 | PASS | focus_adjusted_total formula computed in Item C; Do-nothing cost cells and "Not building this means:" differ from base_cost — demonstrably changes analysis |
| C-08 | PASS | STRATEGY covers all components with Build/Buy/Use before ARCHITECT |
| C-09 | PASS | Focus constraint propagates to INERTIA, ARCHITECT, VERDICT, AMENDMENTS — all four downstream sections, exceeds 2-section minimum |
| C-10 | PASS | STRATEGY appears before ARCHITECT in template body |
| C-11 | PASS | STRATEGY forward-declares components with Build/Buy/Use before ARCHITECT rows |
| C-12 | PASS | ARCHITECT opens with semantic back-reference to STRATEGY decisions |
| C-13 | N/A=1 | No preamble ordering directive |
| C-14 | PASS | Template body alone enforces STRATEGY-before-ARCHITECT ordering |
| C-15 | PASS | No preamble-template conflict; C-11/C-12 by-construction reachable |
| C-16 | PASS | STRATEGY body contains explicit proceed-gate sentence; ARCHITECT body contains explicit confirmation sentence citing STRATEGY |

**Block scores:**
- Essential: 5/5 × 60 = **60.000**
- Recommended: 3/3 × 30 = **30.000**
- Aspirational: 8/8 × 10 = **10.000** (7 PASS + 1 N/A)

**Composite: 100.000**

---

### V-02 — Focus Appended as Standalone Section (Anti-Pattern)

**Axis:** Focus content delivered as a new block after AMENDMENTS instead of woven into existing sections.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | INFERENCE GATE fields present |
| C-02 | PASS | VERDICT fields consistent |
| C-03 | PASS | Traffic-light ratings and RED Blockers correct |
| C-04 | PASS | All four inertia surfaces present |
| C-05 | FAIL | Focus content is additive — a standalone section (e.g., "## COMPLIANCE") appended after AMENDMENTS rather than integrated within existing sections |
| C-06 | PASS | AMENDMENTS remain traceable to components |
| C-07 | FAIL | Focus in standalone block does not demonstrably change base analysis; no focus_adjusted_total arithmetic changing ratings or scores in existing sections |
| C-08 | PASS | STRATEGY covers components before ARCHITECT |
| C-09 | FAIL | Focus content exists only in the appended standalone section — it does not propagate into 2+ distinct downstream sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) |
| C-10 | PASS | STRATEGY precedes ARCHITECT |
| C-11 | PASS | Forward-declaration present |
| C-12 | PASS | Back-reference present |
| C-13 | N/A=1 | No preamble directive |
| C-14 | PASS | Body enforces ordering |
| C-15 | PASS | Cascade-safe; no conflict |
| C-16 | PASS | Mechanism sentences present in template body |

**Block scores:**
- Essential: 4/5 × 60 = **48.000** (C-05 FAIL: −12)
- Recommended: 2/3 × 30 = **20.000** (C-07 FAIL: −10)
- Aspirational: 7/8 × 10 = **8.750** (C-09 FAIL: −1.25)

**Composite: 76.750** ← First variation below golden threshold (80)

---

### V-03 — Focus Woven to INERTIA Only (1-Section Propagation)

**Axis:** Focus correctly woven (not appended), but propagates to only one downstream section (INERTIA). Tests C-09 in isolation.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | INFERENCE GATE fields present |
| C-02 | PASS | VERDICT consistent |
| C-03 | PASS | Traffic-light ratings and RED Blockers correct |
| C-04 | PASS | All four inertia surfaces present |
| C-05 | PASS | Focus content is woven into INERTIA — not appended as a standalone section |
| C-06 | PASS | AMENDMENTS traceable |
| C-07 | PASS | focus_adjusted_total arithmetic appears in INERTIA's Do-nothing cost cell — the analysis is demonstrably different from a no-focus run for that section |
| C-08 | PASS | STRATEGY covers components |
| C-09 | FAIL | Focus-introduced constraint appears in only one downstream section (INERTIA). Two-section minimum required; ARCHITECT, VERDICT, AMENDMENTS do not carry the focus constraint |
| C-10 | PASS | STRATEGY precedes ARCHITECT |
| C-11 | PASS | Forward-declaration present |
| C-12 | PASS | Back-reference present |
| C-13 | N/A=1 | No preamble directive |
| C-14 | PASS | Body enforces ordering |
| C-15 | PASS | Cascade-safe |
| C-16 | PASS | Mechanism sentences present |

**Block scores:**
- Essential: 5/5 × 60 = **60.000**
- Recommended: 3/3 × 30 = **30.000**
- Aspirational: 7/8 × 10 = **8.750** (C-09 FAIL: −1.25)

**Composite: 98.750**

---

### V-04 — Focus Woven to 4 Sections but Qualitative/Cosmetic Only

**Axis:** Focus correctly propagates to 4 sections (C-09 PASS), correctly woven not appended (C-05 PASS), but uses qualitative notes only — no focus_adjusted_total arithmetic, no rating or score changes.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | INFERENCE GATE fields present |
| C-02 | PASS | VERDICT consistent |
| C-03 | PASS | Traffic-light ratings and RED Blockers correct |
| C-04 | PASS | All four inertia surfaces present |
| C-05 | PASS | Focus content woven into existing sections across INERTIA, ARCHITECT, VERDICT, AMENDMENTS — no standalone block |
| C-06 | PASS | AMENDMENTS traceable |
| C-07 | FAIL | Focus content is qualitative/cosmetic (e.g., "compliance note: audit trail required") — no focus_adjusted_total formula computed, no Do-nothing cost cells changed, no rating shifts attributable to focus. Analysis is not demonstrably different from a no-focus run |
| C-08 | PASS | STRATEGY covers components |
| C-09 | PASS | Focus constraint present in 4 sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) — exceeds 2-section minimum |
| C-10 | PASS | STRATEGY precedes ARCHITECT |
| C-11 | PASS | Forward-declaration present |
| C-12 | PASS | Back-reference present |
| C-13 | N/A=1 | No preamble directive |
| C-14 | PASS | Body enforces ordering |
| C-15 | PASS | Cascade-safe |
| C-16 | PASS | Mechanism sentences present |

**Block scores:**
- Essential: 5/5 × 60 = **60.000**
- Recommended: 2/3 × 30 = **20.000** (C-07 FAIL: −10)
- Aspirational: 8/8 × 10 = **10.000** (7 PASS + 1 N/A)

**Composite: 90.000**

---

### V-05 — Focus-Active Golden + Consistent Preamble (Zero-Cost C-13)

**Axis:** V-01 body with an explicit preamble ordering directive (e.g., "Write STRATEGY before ARCHITECT") that matches the template body's section sequence. Tests whether C-13 N/A → PASS conversion costs anything under /8 denominator.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | INFERENCE GATE fields present |
| C-02 | PASS | VERDICT consistent |
| C-03 | PASS | Traffic-light ratings and RED Blockers correct |
| C-04 | PASS | All four inertia surfaces present |
| C-05 | PASS | Focus woven via Propagation Contract; no standalone section |
| C-06 | PASS | AMENDMENTS traceable |
| C-07 | PASS | focus_adjusted_total arithmetic demonstrably changes base analysis |
| C-08 | PASS | STRATEGY covers components |
| C-09 | PASS | Focus propagates to 4+ downstream sections |
| C-10 | PASS | STRATEGY precedes ARCHITECT |
| C-11 | PASS | Forward-declaration present |
| C-12 | PASS | Back-reference present |
| C-13 | PASS | Preamble directive ("Write STRATEGY before ARCHITECT") is consistent with template body section order — no structural conflict; converts from N/A to PASS |
| C-14 | PASS | Body alone enforces ordering; preamble directive is documentational |
| C-15 | PASS | Cascade-safe; C-13 PASS does not introduce a conflict |
| C-16 | PASS | Mechanism sentences present |

**Block scores:**
- Essential: 5/5 × 60 = **60.000**
- Recommended: 3/3 × 30 = **30.000**
- Aspirational: 8/8 × 10 = **10.000** (8 PASS — C-13 now PASS instead of N/A, numerator unchanged at 8/8)

**Composite: 100.000**

---

### Summary Table

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Rank |
|-----------|---------------|-----------------|-------------------|-----------|------|
| V-01 | 60.000 (5/5) | 30.000 (3/3) | 10.000 (8/8) | **100.000** | 1 (tie) |
| V-05 | 60.000 (5/5) | 30.000 (3/3) | 10.000 (8/8) | **100.000** | 1 (tie) |
| V-03 | 60.000 (5/5) | 30.000 (3/3) | 8.750 (7/8) | **98.750** | 3 |
| V-04 | 60.000 (5/5) | 20.000 (2/3) | 10.000 (8/8) | **90.000** | 4 |
| V-02 | 48.000 (4/5) | 20.000 (2/3) | 8.750 (7/8) | **76.750** | 5 |

---

### Excellence Signals (V-01 / V-05)

**1. Propagation Contract structurally pre-wires all three focus criteria simultaneously.**
The Step 0 table with Item A (contract) → Item B (lens) → Item C (formula) → Item D (failure-mode rejection) creates a guaranteed execution path where C-05, C-07, and C-09 become by-construction rather than output-checked. A template without this contract degrades to qualitative notes (V-04) or appended blocks (V-02).

**2. focus_adjusted_total formula is the C-07 trigger — arithmetic, not prose.**
The labeled equation (`focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`) is what makes the analysis demonstrably different from a no-focus run. Qualitative descriptions of the focus (V-04) fail C-07 regardless of coverage breadth. The formula must appear as a verifiable arithmetic identity.

**3. 4-section propagation satisfies C-09 at zero marginal cost vs. 2-section minimum.**
Since the Propagation Contract already maps the focus constraint to all four sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS), C-09 is satisfied automatically. The cheapest C-09 path (INERTIA only, V-03) costs 1.25 pts. The compound failure path (V-02) costs 23.25 pts total across all three blocks.

**4. C-13 N/A → PASS upgrade is denominator-invariant under /8.**
V-05 confirms: adding a consistent preamble directive converts C-13 from N/A=1 to PASS=1. Numerator stays 8/8; composite unchanged at 100.000. The upgrade is free on the focus-active path, and free on the no-focus path — the /8 denominator absorbs it identically to /7.

**5. V-02 is the catastrophic compound failure — essential block is the breakpoint.**
The appended anti-pattern costs 12 pts from the essential block (C-05), 10 from recommended (C-07), and 1.25 from aspirational (C-09) — a total of 23.25 pts. The essential block failure alone (−12) is what pulls V-02 below the 80 golden threshold. Essential criteria are the load-bearing floor of the rubric.

---

```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["focus_adjusted_total formula is the binary C-07 trigger — qualitative focus notes always fail regardless of propagation breadth; arithmetic identity is required", "appended-block anti-pattern is the highest-cost single failure mode seen in the series: 23.25 pts across all three blocks, breaking the 80 golden threshold from essential alone", "C-09 failure cost is asymmetric: 1.25 pts in isolation (V-03) vs. 23.25 pts in compound with C-05+C-07 (V-02) — propagation breadth is cheap to satisfy when the Propagation Contract is present"]}
```
