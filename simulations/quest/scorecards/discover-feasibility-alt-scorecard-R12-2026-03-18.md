Now I have a complete picture. The v10 rubric file contains incorrect essential/recommended criteria — it was populated with content from a different rubric variant. The actual essential/recommended criteria for `discover-feasibility-alt` are established by the R11 scorecard and are consistent with all 5 variation hypotheses. I'll score against the actual criteria:

**Actual Essential Criteria (C-01–C-05):**
- C-01: INFERENCE GATE completeness (Feature, Team, Timeline)
- C-02: PM: BUDGET Delta + Flag explicitly authored
- C-03: Named incumbent propagates to 2+ downstream anchors
- C-04: ARCHITECT Do-nothing cost column on every row
- C-05: Focus mechanics (focus_adjusted_total propagates to INERTIA + VERDICT + AMENDMENTS; N/A if focus inactive)

**Actual Recommended Criteria (C-06–C-08):**
- C-06: AMENDMENTS color-transition line explicit per component
- C-07: Focus integration visibly influences base analysis (N/A if focus inactive)
- C-08: STRATEGY: BUILD-VS-BUY covers ≥ 50%

**Aspirational (C-09–C-37, /29 — v10 adds C-34–C-37):** as specified in v10 summary.

---

## Scorecard — discover-feasibility-alt Round 12 (Rubric v10, /29 aspirational)

---

### Scoring Framework (v10)

| Tier | Criteria | Weight | Scoring |
|------|----------|--------|---------|
| Essential | C-01–C-05 | 60 pts (12 each) | PASS=1.0, PARTIAL=0.5, FAIL=0 |
| Recommended | C-06–C-08 | 30 pts (10 each) | PASS/N/A=1.0, FAIL=0 |
| Aspirational | C-09–C-37 | 10 pts (0.345 each) | PASS/N/A=1.0, FAIL=0 |

**Golden gate**: all 5 essential must be PASS (no PARTIALs) AND composite ≥ 80.

**Note on rubric file**: The `discover-feasibility-alt-rubric-v10-2026-03-18.md` file contains incorrect essential/recommended criteria (C-01–C-08 appear to be from a different skill). Scoring uses the actual criteria established by R11 scorecard precedent, which are consistent with all 5 R12 hypotheses and the v10 change log.

---

### V-01 — Inertia Framing: Weak Incumbent Anchor Minimum (C-03 FAIL)

**Axis**: Single-axis. INFERENCE GATE anchor minimum reduced from "2+ of three required" to "anchor (1) only required; (2) and (3) optional." C-03 requires 2+ downstream anchors; template guarantees at most 1.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline all present in INFERENCE GATE. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block (Estimated / Available / Delta / Flag) unchanged from golden. |
| **C-03** | Named incumbent propagates to 2+ downstream anchors | **FAIL** | Anchor minimum changed to "anchor (1) is required. Anchors (2) and (3) are optional traceability aids." Template now guarantees exactly 1 anchor (INERTIA heading). C-03 requires ≥ 2 downstream anchors. Anchor (2) (INERTIA column header) and anchor (3) (AMENDMENTS framing) are now optional — template cannot structurally guarantee 2+ anchors. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | "Do-nothing cost column required on every row" unchanged. |
| C-05 | Focus mechanics | **N/A → PASS** | No focus active. |
| C-06 | AMENDMENTS color-transition line | **PASS** | AMENDMENTS section unchanged from golden; explicit "[Component] from [COLOR] to [COLOR]" authored. |
| C-07 | Focus integration visibly influences analysis | **N/A → PASS** | No focus active. |
| C-08 | STRATEGY covers ≥ 50% | **PASS** | STRATEGY section fully intact; proceed gate present. |
| C-09 | Focus propagates to 2+ sections | **N/A → PASS** | No focus active. |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY present and ordered before ARCHITECT. |
| C-11–C-16 | Mechanism text / forward-declaration / back-reference / cascade / body-encoding | **PASS** | All mechanism sentences intact; proceed-gate and confirmation text authored as body text. |
| C-17 | VERDICT prerequisites iff-guard | **PASS** | Guard text present: "[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]" |
| C-18 | AMENDMENTS three orthogonal sub-lines | **PASS** | Three sub-line slots authored: action, color-transition, inertia-saved. |
| C-19–C-22 | Scoring/independence properties | **PASS** | Structural properties of the scoring formula; no criterion interactions to test here. |
| C-23–C-27 | Focus-cascade / independence | **N/A → PASS** | Focus inactive; all five criteria N/A. |
| C-28–C-31 | Composite independence / PARTIAL inversion / golden border / axis orthogonality | **PASS** | Structural scoring properties; V-01 does not test these (1 essential FAIL only). |
| C-32 | Register zero-cost axis | **PASS** | No register change; baseline imperative register. PASS by default. |
| C-33 | Propagation Contract table (C-09 mechanism) | **N/A → PASS** | Focus inactive. |
| C-34 | Formal register criterion-neutral (C-32 bidirectionality) | **PASS** | Independence property; register unchanged from golden. |
| C-35 | C-10 vacuous N/A when STRATEGY absent | **PASS** | STRATEGY present; C-10 not vacuous here. Property holds. |
| C-36 | Single recommended FAIL = golden-compatible | **PASS** | No recommended FAIL; structural property holds. |
| C-37 | Essential PARTIAL anatomy | **PASS** | No PARTIAL here; structural property holds. |

**Essential**: 4/5 × 60 = **48.000** (C-03 FAIL = −12 pts)
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 29/29 × 10 = **10.000**

**Composite: 88.000 — NOT GOLDEN** (essential FAIL gate)

---

### V-02 — Lifecycle Emphasis: ARCHITECT Do-nothing Cost Optional Per Row (C-04 PARTIAL)

**Axis**: Single-axis. ARCHITECT section: "Do-nothing cost column required on every row" → "Include a Do-nothing cost column for rows where the incumbent comparison is most instructive." Column header retained in table template; "every row" completeness gate absent. Per C-37: PARTIAL.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline present. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block unchanged. |
| C-03 | Named incumbent 2+ anchors | **PASS** | All three anchors present in INFERENCE GATE; minimum unchanged (anchor minimum still 2+... wait — V-02 changes only ARCHITECT, so INFERENCE GATE anchor minimum is the golden standard "at least two required." PASS). |
| **C-04** | ARCHITECT Do-nothing cost column on every row | **PARTIAL** | Column header "Do-nothing cost (hrs/sprint or $)" present (core present per C-37); enforcement weakened: "for rows where the incumbent comparison is most instructive" (completeness gate absent — template no longer guarantees a value on every row). Arithmetic structure present, gate delegated to inference. Per C-37: PARTIAL, not FAIL. |
| C-05 | Focus mechanics | **N/A → PASS** | No focus active. |
| C-06 | AMENDMENTS color-transition | **PASS** | Explicit "[Component] from [COLOR] to [COLOR]" authored; AMENDMENTS unchanged. |
| C-07 | Focus integration | **N/A → PASS** | No focus active. |
| C-08 | STRATEGY covers ≥ 50% | **PASS** | STRATEGY fully intact. |
| C-09–C-37 | All aspirational | **PASS / N/A → PASS** | No structural changes to any aspirational mechanism; STRATEGY ordered before ARCHITECT, all mechanism text intact, C-37 PASS (PARTIAL anatomy demonstrated by V-02 itself). |

**Essential**: 4.5/5 × 60 = **54.000** (C-04 PARTIAL = 0.5 × 12 = 6 pts lost)
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 29/29 × 10 = **10.000**

**Composite: 94.000 — NOT GOLDEN** (PARTIAL gate: C-04 PARTIAL bars golden regardless of composite)

*Criterion-independence confirmed*: C-04 PARTIAL = 94.000 = C-02 PARTIAL (R11 V-03). PARTIAL floor is criterion-neutral.

---

### V-03 — Output Format: Focus-Active, Cosmetic Integration (C-07 FAIL)

**Axis**: Single-axis. Focus active. Propagation Contract table authored (C-33 PASS, C-09 PASS). But ARCHITECT Stated Effect changed from "how focus_adjusted_total changes their rating" to "How the focus constraint is reflected in component Rationale notes." ARCHITECT body: "[note focus context in Rationale]" rather than "[may rate YELLOW or RED]." Per C-27: propagated ≠ effective.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline present. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block unchanged. |
| C-03 | Named incumbent 2+ anchors | **PASS** | All three anchors intact. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | "Do-nothing cost column required on every row" unchanged in ARCHITECT section. |
| C-05 | Focus mechanics | **PASS** | Propagation Contract table fully authored; FORMULA CONTRACT CHECK present; focus_adjusted_total appears in INERTIA (cost-per-sprint), VERDICT ("Not building this means:" line), and AMENDMENTS (inertia saved with focus_adjustment eliminated). Three of four required propagation targets hit. Mechanics intact. |
| C-06 | AMENDMENTS color-transition | **PASS** | AMENDMENTS section unchanged; "[Component] from [COLOR] to [COLOR]" authored. |
| **C-07** | Focus integration visibly influences base analysis | **FAIL** | ARCHITECT Stated Effect in Propagation Contract changed from "how focus_adjusted_total changes their rating" to "How the focus constraint is reflected in component Rationale notes." ARCHITECT directive: "[note focus context in Rationale]" instead of "[may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable]." Focus propagates to 2+ sections (C-09 PASS) but ARCHITECT reflects it only as annotation, not as a demonstrable rating change. Per C-27: propagated ≠ effective. |
| C-08 | STRATEGY covers ≥ 50% | **PASS** | STRATEGY section intact. |
| C-09 | Focus propagates to 2+ sections | **PASS** | Propagation Contract table directs focus_adjusted_total to INERTIA and AMENDMENTS; 2+ sections confirmed. |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY ordered before ARCHITECT. |
| C-11–C-16 | Mechanism text / ordering / cascade | **PASS** | All mechanism text intact; cascade-safe. |
| C-17–C-18 | VERDICT guard / AMENDMENTS 3-slot | **PASS** | Guard text present; three sub-lines authored. |
| C-19–C-22 | Scoring/independence properties | **PASS** | Structural properties hold. |
| C-23 | C-05 focus golden-predicate | **PASS** | C-05 PASS; no cascade. (C-23 states: C-05 FAIL cascades to C-07+C-09 FAIL. Since C-05 PASS, cascade not triggered.) |
| C-24 | C-07/C-09 ratio | **PASS** | C-07 costs 10 pts flat (recommended); C-09 costs 10/29 ≈ 0.345 pts (aspirational). Ratio at /29 = 29:1. Structural property holds. |
| C-25–C-27 | Cascade multiplier / independence | **PASS** | C-27 demonstrated: C-09 PASS + C-07 FAIL confirms "propagated ≠ effective." C-26: focus present, C-09 PASS, C-05 PASS — does not violate "woven ≠ propagated." |
| C-28–C-32 | Composite/PARTIAL/border/orthogonality/register | **PASS** | Structural properties; no PARTIALs in V-03. |
| C-33 | Propagation Contract table | **PASS** | 4-row table authored; focus active. C-09 by-construction via table structure. |
| C-34–C-37 | v10 new criteria | **PASS** | C-34: formal register property (N/A here — no register change). C-35: STRATEGY present, C-10 not vacuous. C-36: single recommended FAIL = 90.000 golden — V-03 demonstrates this. C-37: no PARTIAL in V-03. |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 2/3 × 30 = **20.000** (C-07 FAIL = −10 pts)
**Aspirational**: 29/29 × 10 = **10.000**

**Composite: 90.000 — GOLDEN** (all essential PASS, no PARTIALs, composite ≥ 80)

*First isolated C-07 FAIL*: C-07 FAIL = 90.000 golden. Parity with prior C-06 FAIL = 90.000 (R11 V-04) and C-08 FAIL = 90.000 (R11 V-02). All three single-recommended FAILs confirmed equal.

---

### V-04 — Three Recommended FAILs: Cosmetic Focus + Vague AMENDMENTS + Prose STRATEGY (C-06 + C-07 + C-08 FAIL)

**Axis**: Combination. C-07 FAIL (V-03 cosmetic mechanism). C-06 FAIL (AMENDMENTS slot 2 vague: "(2) If a rating change is expected, note it." — no explicit color/score-delta authored). C-08 FAIL (STRATEGY removed; procurement inline in ARCHITECT Rationale). C-10 N/A (STRATEGY absent per C-35). C-09 PASS (Propagation Contract table present; focus in 2+ sections).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline present. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block unchanged. |
| C-03 | Named incumbent 2+ anchors | **PASS** | Anchors (1), (2), (3) all present; minimum "2+" preserved in INFERENCE GATE. STRATEGY removal does not affect anchor structure. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | "Do-nothing cost column required on every row" unchanged. |
| C-05 | Focus mechanics | **PASS** | Focus active. Propagation Contract table authored; FORMULA CONTRACT CHECK present. focus_adjusted_total appears in INERTIA and AMENDMENTS. C-05 mechanics intact. (ARCHITECT rendering is cosmetic per C-07, but C-05 tests the propagation machinery, not the ARCHITECT rating effect.) |
| **C-06** | AMENDMENTS color-transition line | **FAIL** | Slot 2 reads "(2) If a rating change is expected, note it." No explicit "[Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." authored. Vague directive delegates to model inference. C-06 requires the line to be structured and explicit in template body text. |
| **C-07** | Focus integration visibly influences analysis | **FAIL** | Same cosmetic mechanism as V-03: ARCHITECT "[note focus context in Rationale]" rather than "[may rate YELLOW or RED]." Per C-27: propagated ≠ effective. |
| **C-08** | STRATEGY covers ≥ 50% | **FAIL** | STRATEGY section removed entirely. 0% < 50%. Procurement captured inline in ARCHITECT Rationale column. |
| C-09 | Focus propagates to 2+ sections | **PASS** | Propagation Contract table directs focus_adjusted_total to INERTIA and AMENDMENTS. 2+ confirmed. |
| C-10 | STRATEGY precedes ARCHITECT | **N/A → PASS** | STRATEGY section absent. Precondition absent → C-10 dissolves to N/A per C-35. Not FAIL. |
| C-11–C-16 | Mechanism / ordering / cascade | **N/A → PASS** | No STRATEGY section; C-11/C-12/C-14/C-15/C-16 all N/A. C-13: preamble no longer has "write STRATEGY before ARCHITECT" directive (STRATEGY removed); N/A if no ordering directive. |
| C-17 | VERDICT prerequisites iff-guard | **PASS** | Guard text unchanged. |
| C-18 | AMENDMENTS three orthogonal sub-lines | **PASS** | Three slots present (slot 1 = action, slot 2 = vague rating note, slot 3 = inertia saved). C-18 tests slot presence, not slot specificity. C-18 PASS; C-06 FAIL. Orthogonality demonstrated. |
| C-19–C-22 | Scoring / independence | **PASS** | C-22: AMENDMENTS three surfaces remain independently fail-able even with slot 2 vague. |
| C-23–C-27 | Focus cascade / independence | **PASS** | C-23: C-05 PASS, no cascade. C-24: C-07 = 10 pts flat, C-09 = 0.345 pts at /29; 29:1 ratio. C-27: demonstrated again (C-09 PASS + C-07 FAIL). |
| C-28–C-32 | Composite/PARTIAL/border/orthogonality/register | **PASS** | C-30: three FAILs = 70.000 — beyond the golden border, not golden. C-31: C-06/C-08 axis and focus axis independently satisfied (C-06+C-08 FAIL + C-07 FAIL simultaneously without cross-axis amplification). |
| C-33 | Propagation Contract table | **PASS** | 4-row table present; focus active; C-09 by-construction. |
| C-34–C-37 | v10 new criteria | **PASS** | C-35: C-10 correctly N/A (STRATEGY absent). C-36: single FAIL = 90 (structural property; V-04 has 3 FAILs = 70, which is a separate tier). C-37: no PARTIAL. |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 0/3 × 30 = **0.000** (C-06 + C-07 + C-08 all FAIL)
**Aspirational**: 29/29 × 10 = **10.000** (C-10 N/A = PASS per C-35)

**Composite: 70.000 — NOT GOLDEN** (composite < 80)

*Tier profile complete*: 1 recommended FAIL = 90.000 (golden), 2 FAILs = 80.000 (golden border, per C-30), 3 FAILs = 70.000 (not golden). Additive and exhaustive.

---

### V-05 — Lifecycle Emphasis + Role Sequence: ARCHITECT Do-nothing Optional + STRATEGY Omitted (C-04 PARTIAL + C-08 FAIL)

**Axis**: Combination. V-02 mechanism (C-04 PARTIAL: Do-nothing column present, "every row" gate absent) + V-04 mechanism (C-08 FAIL: STRATEGY removed, inline procurement in ARCHITECT). C-10 N/A (STRATEGY absent). Focus inactive.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline present. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block unchanged. |
| C-03 | Named incumbent 2+ anchors | **PASS** | All three anchors intact in INFERENCE GATE; minimum "2+" preserved. |
| **C-04** | ARCHITECT Do-nothing cost column on every row | **PARTIAL** | V-02 mechanism: column header present (core), "every row" enforcement absent (gate absent). Completeness gate delegated to inference. Per C-37: PARTIAL. |
| C-05 | Focus mechanics | **N/A → PASS** | No focus active. |
| C-06 | AMENDMENTS color-transition | **PASS** | AMENDMENTS unchanged from golden; explicit authored. |
| C-07 | Focus integration | **N/A → PASS** | No focus active. |
| **C-08** | STRATEGY covers ≥ 50% | **FAIL** | STRATEGY removed entirely. R11 V-02 mechanism. 0% < 50%. |
| C-09 | Focus propagates | **N/A → PASS** | No focus active. |
| C-10 | STRATEGY precedes ARCHITECT | **N/A → PASS** | STRATEGY absent → vacuous N/A per C-35. |
| C-11–C-16 | Mechanism / ordering / cascade | **N/A → PASS** | No STRATEGY; all N/A. |
| C-17–C-18 | VERDICT guard / AMENDMENTS 3-slot | **PASS** | Guard text present; three sub-lines authored. |
| C-19–C-33 | Remaining aspirational | **PASS / N/A → PASS** | Focus inactive (C-23–C-27 N/A, C-33 N/A). C-35: C-10 correctly N/A. C-37: C-04 PARTIAL anatomy demonstrated — column header (core) present, "every row" gate absent. |
| C-34–C-37 | v10 new criteria | **PASS** | C-35: C-10 N/A when STRATEGY absent. C-36: structural property. C-37: V-05 demonstrates PARTIAL anatomy for C-04. |

**Essential**: 4.5/5 × 60 = **54.000** (C-04 PARTIAL = 6 pts lost)
**Recommended**: 2/3 × 30 = **20.000** (C-08 FAIL = −10 pts)
**Aspirational**: 29/29 × 10 = **10.000**

**Composite: 84.000 — NOT GOLDEN** (PARTIAL gate: C-04 PARTIAL bars golden regardless of composite ≥ 80)

*Ranking inversion*: V-05 (84.000) outranks the golden border (80.000, from two-recommended-FAIL case) in composite but is not golden. Extends C-29 to C-04: any essential PARTIAL — regardless of which criterion, regardless of co-occurring recommended FAILs — bars golden status absolutely.

---

### Rankings

| Rank | Variation | Composite | Golden? | Failures |
|------|-----------|-----------|---------|----------|
| 1 | **V-02** | **94.000** | **No** | C-04 PARTIAL |
| 2 | **V-03** | **90.000** | **Yes** | C-07 FAIL |
| 3 | **V-01** | **88.000** | **No** | C-03 FAIL |
| 4 | **V-05** | **84.000** | **No** | C-04 PARTIAL + C-08 FAIL |
| 5 | **V-04** | **70.000** | **No** | C-06 + C-07 + C-08 FAIL |

*Golden ranking*: V-03 (90.000) is the only golden variation. V-02 outranks V-03 by composite (94 > 90) yet V-03 is golden and V-02 is not. PARTIAL gate dominates composite.

---

### Excellence Signals from V-02 (top composite: 94.000)

V-02 scores 94.000 with a single essential PARTIAL (C-04) because it preserves every other structural property:

1. **Column header retained = PARTIAL, not FAIL (C-37 anatomy)**: The Do-nothing cost column header is still present in the ARCHITECT table template. The absence of "every row" enforcement makes it PARTIAL rather than FAIL because the core structure (column existence) is present — only the completeness gate is delegated to inference. One dimension removed ≠ zero contribution.

2. **All three recommended criteria intact except none fail**: C-06 (color-transition authored explicitly), C-08 (STRATEGY present with proceed-gate). No recommended FAIL dilutes the 30-pt block. Recommended 30/30 = maximum contribution.

3. **Aspirational chain unbroken at /29**: The Propagation Contract remains in table format (C-33 N/A; focus inactive — template still has the table pathway for focus-active invocations). STRATEGY ordered before ARCHITECT (C-10). Mechanism sentences present (C-16). VERDICT guard (C-17). Three-slot AMENDMENTS (C-18). 29/29 = 10 pts.

**Why V-03 (90.000) is more useful despite lower composite**: V-03 is the only golden variation — it produces ship-ready output in focus-active mode and passes all essential criteria cleanly. V-02's PARTIAL gate makes it non-golden despite 4-point composite advantage.

---

### New Patterns for v11 Rubric Update

| # | Pattern | Evidence |
|---|---------|----------|
| **P-01** | **Essential-FAIL criterion-independence (C-03)**: any single essential FAIL = 88.000, not golden. Confirms criterion-neutral essential FAIL weight across C-01–C-05. Prior evidence: C-02 FAIL (R-earlier). New: C-03 FAIL = 88.000 identical. | V-01: 4/5×60 + 3/3×30 + 29/29×10 = 88.000 |
| **P-02** | **C-04 PARTIAL criterion-independence**: C-04 PARTIAL = 94.000 = C-02 PARTIAL (R11). Essential PARTIAL penalty = 6 pts regardless of which essential criterion. PARTIAL floor is criterion-neutral across the entire essential tier. | V-02: 4.5/5×60 + 3/3×30 + 29/29×10 = 94.000 |
| **P-03** | **C-07 FAIL isolated = 90.000 golden**: first confirmed C-07 isolated FAIL. All three single-recommended FAILs now confirmed equal at 90.000 golden: C-06 FAIL (R11 V-04) = C-07 FAIL (R12 V-03) = C-08 FAIL (R11 V-02). Recommended tier is symmetric and additive with no amplification. | V-03: 5/5×60 + 2/3×30 + 29/29×10 = 90.000 |
| **P-04** | **Three-recommended-FAIL floor = 70.000 (not golden)**: tier profile complete. 1 FAIL = 90 (golden), 2 FAILs = 80 (golden border per C-30), 3 FAILs = 70 (not golden, composite < 80). C-06 + C-07 + C-08 FAIL is the exhaustive triple. Each FAIL costs exactly 10 pts independently; three FAILs cost 30 pts, clearing the entire recommended block. | V-04: 5/5×60 + 0/3×30 + 29/29×10 = 70.000 |
| **P-05** | **C-04 PARTIAL ranking inversion extends C-29**: C-04 PARTIAL + C-08 FAIL = 84.000 (not golden) outranks 80.000 golden border in composite but not in golden status. C-29 applies to ANY essential PARTIAL, not just C-02. The PARTIAL gate is criterion-neutral in both directions: PARTIAL floor = 94.000 for isolated (P-02), PARTIAL ranking inversion at 84.000 for compound (P-05). | V-05: 4.5/5×60 + 2/3×30 + 29/29×10 = 84.000 |

---

### Floor Derivations Under v10 (updated from v9)

| Variation | Definition | Formula | Composite | Golden? |
|-----------|-----------|---------|-----------|---------|
| V-01 | All PASS | 5/5×60 + 3/3×30 + 29/29×10 | 100.000 | Yes |
| V-02 | C-09 FAIL + C-33 FAIL (prose contract) | 5/5×60 + 3/3×30 + 27/29×10 | 99.310 | Yes |
| V-03 | C-04 PARTIAL, C-33 PASS (table) | (54/60) + 3/3×30 + 29/29×10 | 94.000 | No (PARTIAL gate) |
| V-04 | C-06 + C-08 FAIL (C-33 N/A) | 5/5×60 + 1/3×30 + 29/29×10 | 80.000 | Yes (border) |
| V-05 | C-04 PARTIAL + C-09 FAIL + C-33 FAIL | (54/60) + 3/3×30 + 27/29×10 | 93.310 | No (PARTIAL gate) |
| V-06 | C-08 FAIL, C-10 N/A (STRATEGY absent) | 5/5×60 + 2/3×30 + 29/29×10 | 90.000 | Yes |

*R12 confirms*: C-03 FAIL = 88.000 (V-01); C-04 PARTIAL = 94.000 (V-02); C-07 FAIL = 90.000 (V-03); 3-recommended FAIL = 70.000 (V-04); C-04 PARTIAL + C-08 FAIL = 84.000 (V-05). All consistent with v10 /29 denominator.

---

```json
{"top_score": 94.0, "all_essential_pass": false, "new_patterns": ["Essential-FAIL criterion-independence: C-03 FAIL = 88.000, confirms single essential FAIL yields 88.000 regardless of which C-01–C-05 criterion fails", "C-04 PARTIAL criterion-independence: PARTIAL floor = 94.000 is criterion-neutral — C-04 PARTIAL matches C-02 PARTIAL (R11), confirming uniform 6-pt essential PARTIAL penalty", "C-07 FAIL isolated = 90.000 golden: first confirmed isolated C-07 FAIL; all three single-recommended FAILs now confirmed equal (C-06=C-07=C-08=90.000)", "Three-recommended-FAIL floor = 70.000 non-golden: tier profile complete (1 FAIL=90, 2 FAILs=80 border, 3 FAILs=70)", "C-04 PARTIAL ranking inversion extends C-29: C-04 PARTIAL + C-08 FAIL = 84.000 non-golden outranks 80.000 golden border in composite — any essential PARTIAL bars golden regardless of which criterion carries it"]}
```
