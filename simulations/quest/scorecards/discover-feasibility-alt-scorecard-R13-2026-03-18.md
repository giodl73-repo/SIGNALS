## Scorecard — discover-feasibility-alt Round 13

Written to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R13-2026-03-18.md`.

---

### Rankings

| Rank | Variation | Composite | Golden? | Failures |
|------|-----------|-----------|---------|----------|
| 1 | **V-02** | **99.706** | **Yes** | C-33 FAIL (aspirational only) |
| 2 | **V-01** | **88.000** | No | C-01 FAIL (essential) |
| 3 | **V-05** | **78.000** | No | C-03 FAIL (essential) + C-08 FAIL (recommended) |
| 4 | **V-03** | **77.706** | No | C-05 FAIL + C-07 FAIL + C-09 FAIL (cascade) |
| 5 | **V-04** | **76.000** | No | C-01 FAIL + C-03 FAIL (both essential) |

---

### Excellence Signals (V-02)

**C-33/C-09 independence**: Prose propagation satisfies C-09 (focus_adjusted_total in 2+ sections) while failing C-33 (table structure). The two criteria are independently assessable — the table is a structural encoding criterion, not a propagation criterion. Single aspirational FAIL costs only 0.294 pts at /34.

---

### New Patterns for v12

| # | Pattern | Source |
|---|---------|--------|
| P-01 | C-33 FAIL independent of C-09 — prose contract can PASS propagation while FAIL table structure. New composite 99.706 (1 aspirational FAIL) vs prior compound 99.412 (2 FAILs). | V-02 |
| P-02 | Two-essential-FAIL additivity — C-01+C-03 FAIL = 76.000. Co-occurring essential FAILs additive, no amplification. Floor sequence: 1 FAIL=88, 2 FAILs=76, 3 FAILs=64 (predicted). | V-04 |
| P-03 | Cross-tier FAIL additivity — C-03 FAIL (essential, -12) + C-08 FAIL (recommended, -10) = 78.000. Tier costs add independently, no cross-tier amplification. | V-05 |

---

```json
{"top_score": 99.706, "all_essential_pass": false, "new_patterns": ["C-33 FAIL independent of C-09: prose propagation contract satisfies C-09 (focus_adjusted_total in 2+ sections, PASS) while failing C-33 (4-row table structure absent, FAIL). Previously C-33 FAIL was always compound with C-09 FAIL. New composite 99.706 vs prior compound 99.412.", "Two-essential-FAIL additivity: C-01 FAIL + C-03 FAIL = 76.000. Co-occurring essential FAILs are additive with no amplification. Extends C-38 to double-FAIL topology: 1 FAIL=88.000, 2 FAILs=76.000, 3 FAILs=64.000 (predicted).", "Cross-tier FAIL additivity: C-03 FAIL (essential, -12 pts) + C-08 FAIL (recommended, -10 pts) = 78.000. Essential and recommended tier costs add independently across tier boundary. New floor between single-recommended-FAIL golden (90.000) and two-essential-FAIL floor (76.000)."]}
```
changed; focus inactive so base_cost used. |
| C-05 | Focus mechanics | **N/A -> PASS** | Focus inactive. |
| C-06 | AMENDMENTS color-transition line | **PASS** | AMENDMENTS section unchanged from golden; explicit "[Component] from [COLOR] to [COLOR]" authored. |
| C-07 | Focus integration visibly influences analysis | **N/A -> PASS** | Focus inactive. |
| C-08 | STRATEGY covers >= 50% | **PASS** | STRATEGY section fully intact with proceed gate. |
| C-09 | Focus propagates to 2+ sections | **N/A -> PASS** | Focus inactive. |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY present and ordered before ARCHITECT. |
| C-11–C-16 | Mechanism text / forward-declaration / cascade | **PASS** | All mechanism sentences intact; no ordering disruption. |
| C-17 | VERDICT prerequisites iff-guard | **PASS** | Guard text present and unchanged. |
| C-18 | AMENDMENTS three orthogonal sub-lines | **PASS** | Three sub-line slots authored: action, color-transition, inertia-saved. |
| C-19–C-22 | Scoring/independence properties | **PASS** | Structural properties; V-01 tests single essential FAIL only. |
| C-23–C-27 | Focus-cascade / independence | **N/A -> PASS** | Focus inactive; all five N/A. |
| C-28–C-32 | Composite / PARTIAL / border / axis / register | **PASS** | C-38: essential FAIL criterion-neutrality demonstrated for C-01 — confirmed equal to C-03 FAIL (R12 V-01) at 88.000. |
| C-33 | Propagation Contract table | **N/A -> PASS** | Focus inactive. |
| C-34–C-42 | v9–v11 new criteria | **PASS** | C-35: STRATEGY present, C-10 not vacuous. C-38 criterion-neutrality confirmed: C-01 FAIL = C-03 FAIL = 88.000. |

**Essential**: 4/5 x 60 = **48.000** (C-01 FAIL = -12 pts)
**Recommended**: 3/3 x 30 = **30.000**
**Aspirational**: 34/34 x 10 = **10.000**

**Composite: 88.000 — NOT GOLDEN** (essential FAIL gate)

*C-38 criterion-neutrality confirmed for C-01*: C-01 FAIL = 88.000. Matches C-03 FAIL (R12 V-01) = 88.000 at the same denominator (/34). The essential tier is symmetric: any single FAIL among C-01–C-05 yields 88.000 regardless of which criterion.

---

### V-02 — Output Format: Focus-Active Prose Contract (C-33 FAIL, C-09 PASS)

**Axis**: Single-axis. Focus active. Step 0 Item A replaced with prose description of the four propagation effects (not a 4-row table). Formula Contract Check and Items B–D retained. All downstream section directives retain focus_adjusted_total references — C-09 PASS (focus_adjusted_total in 2+ sections). C-33 requires 4-row table structure; prose form fails C-33 regardless of propagation coverage. All essential criteria unchanged from golden.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline all present; unchanged from golden. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block unchanged. |
| C-03 | Named incumbent 2+ anchors | **PASS** | Anchor minimum unchanged; all three forms present in INFERENCE GATE. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | "Do-nothing cost column required on every row" unchanged; uses focus_adjusted_total. |
| C-05 | Focus mechanics | **PASS** | Focus active. Propagation Contract authored (prose, not table). Formula Contract Check present. focus_adjusted_total computed in Item C and appears in INERTIA (cost-per-sprint), VERDICT ("Not building this means:"), and AMENDMENTS (inertia-saved framing). All four propagation targets satisfied. |
| C-06 | AMENDMENTS color-transition line | **PASS** | AMENDMENTS section unchanged from golden; explicit per-component authored. |
| C-07 | Focus integration visibly influences analysis | **PASS** | ARCHITECT directive unchanged: "[may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable]." Focus demonstrably changes component ratings. |
| C-08 | STRATEGY covers >= 50% | **PASS** | STRATEGY section fully intact with proceed gate. |
| C-09 | Focus propagates to 2+ sections | **PASS** | Prose contract explicitly directs focus_adjusted_total to INERTIA, ARCHITECT, VERDICT, and AMENDMENTS. All downstream section directives retain focus_adjusted_total references. 2+ sections confirmed. |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY ordered before ARCHITECT. |
| C-11–C-18 | Mechanism / ordering / guard / 3-slot | **PASS** | All mechanism sentences intact; guard text and three-slot AMENDMENTS unchanged. |
| C-19–C-22 | Scoring/independence properties | **PASS** | C-19: aspirational criterion independence demonstrated — C-33 FAIL costs aspirational pts only. |
| C-23–C-27 | Focus-cascade / independence | **PASS** | C-23: C-05 PASS, no cascade. C-26: V-02 shows woven integration in prose form != table format. C-27: C-09 PASS (2+ sections) independent of C-07 PASS (rating changes). |
| C-28–C-32 | Composite / PARTIAL / border / axis / register | **PASS** | V-02 is golden: 99.706 >= 80, all essential PASS, no PARTIALs. C-31: C-33 axis (table format) proven orthogonal to C-05 axis (focus propagation). |
| **C-33** | Propagation Contract table (C-09 mechanism) | **FAIL** | Step 0 Item A replaced with prose description of four propagation effects. No markdown table with Constraint / Section / Effect columns authored. C-33 requires the 4-row table structure by construction; prose propagation contract fails C-33 regardless of whether C-09 is satisfied. |
| C-34–C-42 | v9–v11 new criteria | **PASS** | C-32/C-34: register unchanged. C-35: STRATEGY present. C-33/C-09 independence newly demonstrated: prose satisfies C-09 (propagation) while failing C-33 (table structure). |

**Essential**: 5/5 x 60 = **60.000**
**Recommended**: 3/3 x 30 = **30.000**
**Aspirational**: 33/34 x 10 = **9.706** (C-33 FAIL = -10/34 pts)

**Composite: 99.706 — GOLDEN** (all essential PASS, no PARTIALs, composite >= 80)

*C-33/C-09 independence confirmed*: C-33 and C-09 are independently assessable. Prose propagation satisfies C-09 (focus_adjusted_total in 2+ sections) while failing C-33 (table structure absent). Previously C-33 FAIL was always compound with C-09 FAIL. New composite 99.706 (one aspirational FAIL) vs. prior compound 99.412 (two aspirational FAILs, C-33 + C-09).

---

### V-03 — Role Sequence: focus_adjusted_total Stripped from Downstream (C-05 FAIL + Cascade)

**Axis**: Single-axis trigger, cascade output. Focus active. Step 0 computes focus_adjusted_total via Items A–D (4-row table present). But all downstream section directives strip focus_adjusted_total references: INERTIA uses [base_cost] unconditionally, ARCHITECT do-nothing cost uses base_cost, VERDICT references base_cost only, AMENDMENTS omits focus_adjustment. C-05 FAIL triggers cascade per C-23: C-07 FAIL (focus never visible in base analysis) and C-09 FAIL (focus_adjusted_total in 0 downstream sections). C-33 PASS (table structurally intact; deficiency is downstream-only).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline all present. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block unchanged. |
| C-03 | Named incumbent 2+ anchors | **PASS** | Anchor minimum unchanged; all three anchor forms present. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | Do-nothing cost column present on every row. Column uses base_cost (focus stripped), but column mandate satisfied — C-04 tests column presence, not value source. |
| **C-05** | Focus mechanics | **FAIL** | Focus active. focus_adjusted_total computed in Step 0 Item C. But INERTIA table uses "[base_cost]" unconditionally; ARCHITECT do-nothing column uses base_cost; VERDICT "Not building this means:" references base_cost only; AMENDMENTS "inertia-saved framing" omits focus_adjustment. focus_adjusted_total absent from INERTIA + VERDICT + AMENDMENTS — all three required targets missed. FAIL. |
| C-06 | AMENDMENTS color-transition line | **PASS** | AMENDMENTS structural form unchanged; color-transition slots present. C-06 tests transition-line presence, not focus integration in inertia-saved framing. |
| **C-07** | Focus integration visibly influences analysis | **FAIL** | Cascade from C-05 FAIL per C-23: focus_adjusted_total stripped from all downstream directives. ARCHITECT base analysis uses base_cost with no focus-driven rating adjustments. Focus computed but invisible in rated components. Per C-27: zero propagation != effective integration. |
| C-08 | STRATEGY covers >= 50% | **PASS** | STRATEGY section intact with procurement recommendations and proceed gate. |
| **C-09** | Focus propagates to 2+ sections | **FAIL** | Cascade from C-05 FAIL per C-23: focus_adjusted_total in 0 downstream sections. INERTIA uses base_cost; ARCHITECT uses base_cost; VERDICT uses base_cost; AMENDMENTS omits focus_adjustment. Zero sections carry focus_adjusted_total as required value. FAIL. |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY ordered before ARCHITECT. |
| C-11–C-18 | Mechanism / ordering / guard / 3-slot | **PASS** | All mechanism sentences intact. VERDICT guard present. Three-slot AMENDMENTS present. |
| C-19–C-22 | Scoring / independence | **PASS** | C-21: C-05 FAIL independently produces C-07+C-09 co-FAILs via cascade, not composite amplification. |
| C-23 | C-05 focus golden-predicate / cascade trigger | **FAIL triggered** | C-05 FAIL -> C-07 FAIL + C-09 FAIL cascade confirmed. C-23 documents this as a structural implication, not an additional penalty. |
| C-24 | C-07/C-09 severity ratio | **PASS** | At /34: C-07 = 10 pts (recommended), C-09 = 10/34 pts (aspirational). Ratio = 34:1. Confirms C-24 linear growth: /29 -> 29:1, /34 -> 34:1. |
| C-25 | Cascade multiplier | **PASS** | At /34: 2.2x34 + 1 = 75.8x. Confirms linear growth. |
| C-26–C-27 | Focus woven / propagated independence | **PASS** | C-26: Step 0 computation present but downstream stripped = computed != woven. C-27: table present (C-33 PASS) but downstream stripped = propagated != effective. |
| C-28–C-32 | Composite / PARTIAL / border / axis / register | **PASS** | V-03 not golden: 77.706 < 80 AND essential FAIL. No PARTIALs. |
| C-33 | Propagation Contract table | **PASS** | 4-row table structurally intact in Step 0. FORMULA CONTRACT CHECK present. Deficiency is downstream-only — C-33 PASS; C-09 FAIL from cascade only. |
| C-34–C-42 | v9–v11 new criteria | **PASS** | C-35: STRATEGY present. C-38: V-03 has 1 essential FAIL (C-05); cascade FAILs (C-07, C-09) are not double-counted as additional essential FAILs. |

**Essential**: 4/5 x 60 = **48.000** (C-05 FAIL = -12 pts)
**Recommended**: 2/3 x 30 = **20.000** (C-07 FAIL = -10 pts)
**Aspirational**: 33/34 x 10 = **9.706** (C-09 FAIL = -10/34 pts)

**Composite: 77.706 — NOT GOLDEN** (essential FAIL gate; composite < 80)

*C-05 cascade at /34 confirmed*: Formula 4/5x60 + 2/3x30 + 33/34x10 = 77.706. Cascade mechanism from C-23 produces compound failure across three criteria from a single essential trigger. At /34, each cascaded aspirational FAIL costs 0.294 pts (vs. 0.345 at /29). Cascade composite < 80 is preserved at /34.

---

### V-04 — Lifecycle + Inertia Compound: Two Essential FAILs (C-01 FAIL + C-03 FAIL)

**Axis**: Two-essential-FAIL compound. INFERENCE GATE removes Team and Timeline lines (C-01 FAIL per V-01 mechanism). INFERENCE GATE anchor minimum reduced to "anchor (1) is required. Anchors (2) and (3) are optional traceability aids" (C-03 FAIL per R12 V-01 mechanism). All recommended and aspirational unchanged from golden.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| **C-01** | INFERENCE GATE completeness | **FAIL** | Team and Timeline lines removed from INFERENCE GATE template. Feature retained. C-01 requires Feature + Team + Timeline; two of three slots absent. FAIL. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Budget arithmetic unchanged; placeholders [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] independent of INFERENCE GATE lines. |
| **C-03** | Named incumbent 2+ anchors | **FAIL** | Anchor minimum reduced to "anchor (1) is required. Anchors (2) and (3) are optional traceability aids." Template now guarantees exactly 1 anchor (INERTIA heading). C-03 requires >= 2; with (2) and (3) optional, structural guarantee drops below minimum. FAIL. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | "Do-nothing cost column required on every row" unchanged. |
| C-05 | Focus mechanics | **N/A -> PASS** | All recommended and aspirational unchanged from golden; focus criteria PASS or N/A->PASS regardless of focus state. |
| C-06 | AMENDMENTS color-transition line | **PASS** | AMENDMENTS unchanged from golden. |
| C-07 | Focus integration | **PASS / N/A -> PASS** | Unchanged from golden. |
| C-08 | STRATEGY covers >= 50% | **PASS** | STRATEGY section intact. |
| C-09–C-33 | All aspirational | **PASS / N/A -> PASS** | All unchanged from golden. INFERENCE GATE and anchor minimum changes do not affect mechanism sentences, propagation contract, or focus directives. 34/34 PASS. |
| C-34–C-42 | v9–v11 new criteria | **PASS** | C-38: V-04 demonstrates two-essential-FAIL additivity. Each FAIL costs 12 pts independently; two FAILs cost 24 pts with no amplification. |

**Essential**: 3/5 x 60 = **36.000** (C-01 FAIL + C-03 FAIL = -24 pts)
**Recommended**: 3/3 x 30 = **30.000**
**Aspirational**: 34/34 x 10 = **10.000**

**Composite: 76.000 — NOT GOLDEN** (essential FAIL gate; composite < 80)

*Two-essential-FAIL additivity confirmed*: C-01 FAIL + C-03 FAIL = 76.000. The two essential FAILs are additive: 88.000 - 12 = 76.000. No amplification between co-occurring essential FAILs. Lower essential floor topology: single essential FAIL = 88.000 (C-38), double essential FAIL = 76.000 (new), triple essential FAIL = 64.000 (predicted).

---

### V-05 — Inertia + Role Sequence Compound: Cross-Tier FAILs (C-03 FAIL + C-08 FAIL)

**Axis**: Cross-tier compound. C-03 FAIL (anchor minimum = 1, per R12 V-01 mechanism) + C-08 FAIL (STRATEGY section removed, procurement captured inline in ARCHITECT Rationale). C-10 N/A per C-35 (STRATEGY absent). Focus inactive: C-05, C-07, C-09, C-33 all N/A.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | INFERENCE GATE unchanged; Feature, Team, Timeline all present. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block unchanged. |
| **C-03** | Named incumbent 2+ anchors | **FAIL** | Anchor minimum reduced to "anchor (1) is required. Anchors (2) and (3) are optional traceability aids." Template guarantees <= 1 anchor. C-03 requires >= 2. FAIL. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | "Do-nothing cost column required on every row" unchanged; uses base_cost (focus inactive). |
| C-05 | Focus mechanics | **N/A -> PASS** | Focus inactive. |
| C-06 | AMENDMENTS color-transition line | **PASS** | Explicit per-component color-transition line authored; AMENDMENTS unchanged from golden. |
| C-07 | Focus integration | **N/A -> PASS** | Focus inactive. |
| **C-08** | STRATEGY covers >= 50% | **FAIL** | STRATEGY section removed entirely. Procurement captured inline in ARCHITECT Rationale column per R11 V-02 mechanism. 0% < 50% required. FAIL. |
| C-09 | Focus propagates to 2+ sections | **N/A -> PASS** | Focus inactive. |
| C-10 | STRATEGY precedes ARCHITECT | **N/A -> PASS** | STRATEGY absent; presence-dependent ordering criterion dissolves to N/A per C-35. Not FAIL. |
| C-11–C-16 | Mechanism / ordering / cascade | **N/A -> PASS** | No STRATEGY section; all N/A per C-35 logic. |
| C-17 | VERDICT prerequisites iff-guard | **PASS** | Guard text present and unchanged. |
| C-18 | AMENDMENTS three orthogonal sub-lines | **PASS** | Three slot structure intact: action, color-transition, inertia-saved. |
| C-19–C-22 | Scoring / independence | **PASS** | C-20: essential FAIL and recommended FAIL interact only by independent additive costs. |
| C-23–C-27 | Focus-cascade / independence | **N/A -> PASS** | Focus inactive. |
| C-28–C-32 | Composite / PARTIAL / border / axis / register | **PASS** | V-05 = 78.000 (not golden: essential FAIL gate). C-38 + cross-tier additivity: essential FAIL (12 pts) + recommended FAIL (10 pts) add independently = 22 pts total deduction. |
| C-33 | Propagation Contract table | **N/A -> PASS** | Focus inactive. |
| C-34–C-42 | v9–v11 new criteria | **PASS** | C-35: C-10 correctly N/A (STRATEGY absent). C-36: single recommended FAIL (C-08) = golden-compatible in isolation (90.000); V-05 non-golden only because C-03 FAIL co-present. |

**Essential**: 4/5 x 60 = **48.000** (C-03 FAIL = -12 pts)
**Recommended**: 2/3 x 30 = **20.000** (C-08 FAIL = -10 pts)
**Aspirational**: 34/34 x 10 = **10.000** (C-10 N/A and all focus N/As count as PASS)

**Composite: 78.000 — NOT GOLDEN** (essential FAIL gate; composite < 80)

*Cross-tier FAIL additivity confirmed*: C-03 FAIL (essential, -12 pts) + C-08 FAIL (recommended, -10 pts) = 78.000. Essential and recommended tier costs add independently with no cross-tier amplification. New floor at 78.000 — between single-recommended-FAIL golden floor (90.000) and two-essential-FAIL floor (76.000).

---

### Rankings

| Rank | Variation | Composite | Golden? | Failures |
|------|-----------|-----------|---------|----------|
| 1 | **V-02** | **99.706** | **Yes** | C-33 FAIL (aspirational only) |
| 2 | **V-01** | **88.000** | No | C-01 FAIL (essential) |
| 3 | **V-05** | **78.000** | No | C-03 FAIL (essential) + C-08 FAIL (recommended) |
| 4 | **V-03** | **77.706** | No | C-05 FAIL (essential) + C-07 FAIL (recommended) + C-09 FAIL (aspirational) cascade |
| 5 | **V-04** | **76.000** | No | C-01 FAIL + C-03 FAIL (both essential) |

*Golden ranking*: V-02 (99.706) is the only golden variation. V-01 (88.000) is the highest non-golden — one essential FAIL, all other tiers intact.

---

### Excellence Signals from V-02 (top-scoring, 99.706, Golden)

V-02 achieves 99.706 golden with a single aspirational FAIL (C-33) because it preserves every structural property at the essential and recommended tiers:

1. **C-33/C-09 independence is the key structural insight**: Prose propagation contracts satisfy C-09 (focus_adjusted_total in 2+ downstream sections) while failing C-33 (4-row table structure). The two criteria are independently assessable. Prose that explicitly directs focus_adjusted_total to all four downstream sections passes C-09 at full propagation fidelity. The table is a structural encoding criterion, not a propagation criterion. Single-criterion failure at aspirational level costs only 10/34 = 0.294 pts.

2. **All five essential criteria intact**: C-05 PASS requires only that focus_adjusted_total propagates to INERTIA + VERDICT + AMENDMENTS — the prose contract satisfies this equally to the table format. C-01/C-02/C-03/C-04 are unaffected by format changes in Step 0. Zero essential deduction = maximum 60 pts.

3. **All three recommended criteria intact**: C-07 PASS because ARCHITECT directive unchanged — format change in Step 0 does not affect ARCHITECT body. C-06/C-08 unchanged. 30/30 recommended pts.

4. **Focus-active at maximum integration depth**: C-09 PASS with prose demonstrates that the propagation requirement is deeper than its encoding mechanism. A prose contract that explicitly names focus_adjusted_total in every downstream directive satisfies C-09 without the table scaffold.

---

### New Patterns for v12 Rubric Update

| # | Pattern | Evidence |
|---|---------|----------|
| **P-01** | **C-33 FAIL independent of C-09**: C-33 (Propagation Contract table structure) and C-09 (focus_adjusted_total propagates to 2+ sections) are independently assessable. Prose contract can satisfy C-09 while failing C-33. Previously C-33 FAIL was always compound with C-09 FAIL. New composite 99.706 (1 aspirational FAIL) vs. prior compound 99.412 (2 aspirational FAILs). | V-02: C-33 FAIL + C-09 PASS = 99.706 |
| **P-02** | **Two-essential-FAIL additivity**: Co-occurring essential FAILs are additive with no amplification. C-01 FAIL + C-03 FAIL = 76.000 = 88.000 - 12. Extends C-38 (single essential FAIL = 88.000) to double-FAIL topology. Floor sequence: 1 FAIL=88, 2 FAILs=76 (new), 3 FAILs=64 (predicted). | V-04: 3/5x60 + 3/3x30 + 34/34x10 = 76.000 |
| **P-03** | **Cross-tier FAIL additivity**: Essential FAIL and recommended FAIL costs add independently across tier boundary. C-03 FAIL (-12 pts) + C-08 FAIL (-10 pts) = 78.000. New floor between single-recommended-FAIL golden (90.000) and two-essential-FAIL floor (76.000). Confirms no cross-tier amplification or discounting. | V-05: 4/5x60 + 2/3x30 + 34/34x10 = 78.000 |

---

### Floor Derivations Under v11 (updated from v10)

| Variation | Definition | Formula | Composite | Golden? |
|-----------|-----------|---------|-----------|---------|
| V-01 | All PASS | 5/5x60 + 3/3x30 + 34/34x10 | 100.000 | Yes |
| V-02 | C-09 FAIL + C-33 FAIL (prose contract, compound) | 5/5x60 + 3/3x30 + 32/34x10 | 99.412 | Yes |
| V-03 | C-04 PARTIAL, C-33 PASS (table) | (54/60) + 3/3x30 + 34/34x10 | 94.000 | No (PARTIAL gate) |
| V-04 | C-06 + C-08 FAIL (C-33 N/A) | 5/5x60 + 1/3x30 + 34/34x10 | 80.000 | Yes (border) |
| V-05 | C-04 PARTIAL + C-09 FAIL + C-33 FAIL | (54/60) + 3/3x30 + 32/34x10 | 93.412 | No (PARTIAL gate) |
| V-06 | C-08 FAIL, C-10 N/A (STRATEGY absent) | 5/5x60 + 2/3x30 + 34/34x10 | 90.000 | Yes |
| **V-07** | **C-33 FAIL, C-09 PASS (prose independent)** | 5/5x60 + 3/3x30 + 33/34x10 | **99.706** | **Yes** |
| **V-08** | **C-01 FAIL** | 4/5x60 + 3/3x30 + 34/34x10 | **88.000** | No |
| **V-09** | **C-01 FAIL + C-03 FAIL (two essential)** | 3/5x60 + 3/3x30 + 34/34x10 | **76.000** | No |
| **V-10** | **C-03 FAIL + C-08 FAIL (cross-tier)** | 4/5x60 + 2/3x30 + 34/34x10 | **78.000** | No |

*V-08 (C-01 FAIL = 88.000) confirms C-38: same composite as C-03 FAIL (R12 V-01), essential FAIL criterion-neutral across C-01–C-05.*

---

```json
{"top_score": 99.706, "all_essential_pass": false, "new_patterns": ["C-33 FAIL independent of C-09: prose propagation contract satisfies C-09 (focus_adjusted_total in 2+ sections, PASS) while failing C-33 (4-row table structure absent, FAIL). Previously C-33 FAIL was always compound with C-09 FAIL. New composite 99.706 vs prior compound 99.412.", "Two-essential-FAIL additivity: C-01 FAIL + C-03 FAIL = 76.000. Co-occurring essential FAILs are additive with no amplification. Extends C-38 to double-FAIL topology: 1 FAIL=88.000, 2 FAILs=76.000, 3 FAILs=64.000 (predicted).", "Cross-tier FAIL additivity: C-03 FAIL (essential, -12 pts) + C-08 FAIL (recommended, -10 pts) = 78.000. Essential and recommended tier costs add independently across tier boundary. New floor between single-recommended-FAIL golden (90.000) and two-essential-FAIL floor (76.000)."]}
```
