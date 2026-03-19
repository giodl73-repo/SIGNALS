Now I have all the information needed. Let me write the scorecard.

---

## Scorecard — discover-feasibility-alt Round 11 (Rubric v9, /25 aspirational)

---

### Scoring Framework (v9)

| Tier | Criteria | Weight | Scoring |
|------|----------|--------|---------|
| Essential | C-01–C-05 | 60 pts (12 each) | PASS=1.0, PARTIAL=0.5, FAIL=0 |
| Recommended | C-06–C-08 | 30 pts (10 each) | PASS=1.0, FAIL=0 |
| Aspirational | C-09–C-33 | 10 pts (0.4 each) | PASS/N/A=1.0, FAIL=0 |

**Golden gate**: no essential criterion may be PARTIAL or FAIL.

---

### V-01 — Phrasing Register: Formal/Technical

**Axis**: Single-axis. All structural requirements intact; phrasing shifted throughout from conversational to formal/technical register. Tests C-32 bidirectionality: if conversational register (R10 V-01) is criterion-neutral, formal register must score identically.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | All three required fields present (Feature, Team, Timeline). |
| C-02 | PM: BUDGET Delta + Flag present | **PASS** | Full arithmetic block: Estimated / Available / Delta / Flag all authored. |
| C-03 | Named incumbent propagates to 2+ downstream anchors | **PASS** | INERTIA heading anchor (1), INERTIA table column header anchor (2), AMENDMENTS anchor (3) all present. |
| C-04 | ARCHITECT Do-nothing cost column on every row | **PASS** | "Do-nothing cost (hrs/sprint or $)" column required on every row; template enforces it. |
| C-05 | Focus mechanics: focus_adjusted_total propagates to INERTIA + VERDICT + AMENDMENTS | **PASS** | Full Propagation Contract + FORMULA CONTRACT CHECK authored; focus inactive path also explicit. |
| C-06 | AMENDMENTS color-transition line explicit per component | **PASS** | "This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." authored verbatim. |
| C-07 | Focus integration visibly influences base analysis | **PASS** | N/A (focus inactive) → counts as PASS. |
| C-08 | STRATEGY: BUILD-VS-BUY covers >= 50% of components | **PASS** | STRATEGY section fully intact; proceed-gate present. |
| C-09 | Focus constraint propagates to 2+ downstream sections | **PASS** | N/A (focus inactive) → PASS. |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY is present and positioned before ARCHITECT in template. |
| C-11–C-16 | Mechanism text / ordering / cascade / body-encoding | **PASS** | All mechanism sentences authored as body text; proceed-gate and back-reference intact. |
| C-17–C-22 | VERDICT guard / AMENDMENTS 3-slot / independence | **PASS** | Guard text present; three sub-lines in AMENDMENTS; criterion independence preserved. |
| C-23–C-27 | Focus cascade / INERTIA baseline / formula sequence / scoped alternative / do-nothing | **PASS** | All authored; focus inactive path handled. |
| C-28–C-31 | Composite independence / ranking inversion / golden border / C-06/C-08 orthogonality | **PASS** | Structural properties of scoring formula — all PASS by definition when all criteria PASS. |
| C-32 | Register is zero-cost axis | **PASS** | Formal/technical phrasing throughout does not affect any criterion. Bidirectionality confirmed: conversational (R10) = formal (R11) = 100.000. |
| C-33 | Propagation Contract table present (4-row) | **PASS** | N/A (focus inactive) → counts as PASS. |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 25/25 × 10 = **10.000**

**Composite: 100.000 — GOLDEN**

---

### V-02 — Role Sequence: STRATEGY Section Omitted

**Axis**: Single-axis. STRATEGY: BUILD-VS-BUY section removed entirely. Components proceed directly to ARCHITECT with procurement approach captured inline in Rationale column. Tests C-10 N/A pass condition on STRATEGY absence.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline all present. |
| C-02 | PM: BUDGET Delta + Flag present | **PASS** | Full arithmetic block unchanged from V-01. Delta and Flag present. |
| C-03 | Named incumbent anchors | **PASS** | All three anchors present in template. |
| C-04 | ARCHITECT Do-nothing cost column | **PASS** | Column present on every row. |
| C-05 | Focus mechanics propagation | **PASS** | Propagation Contract table intact; focus inactive path present. |
| C-06 | AMENDMENTS color-transition line | **PASS** | "This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." present. |
| C-07 | Focus integration | **PASS** | N/A (focus inactive). |
| **C-08** | STRATEGY covers >= 50% | **FAIL** | No STRATEGY section exists. 0% < 50% coverage. |
| C-09 | Focus propagates to 2+ sections | **PASS** | N/A (focus inactive). |
| **C-10** | STRATEGY precedes ARCHITECT | **N/A → PASS** | No STRATEGY section present in output → precondition absent → criterion vacuously N/A. Key finding: STRATEGY omission ≠ C-10 FAIL. C-10 FAIL requires ARCHITECT before a *present* STRATEGY. |
| C-11–C-16 | Mechanism text / ordering / cascade / body-encoding | **PASS** | STRATEGY-specific mechanism text removed, but remaining mechanisms intact. C-16: proceed-gate text absent only for STRATEGY→ARCHITECT chain (which is vacuous). Remaining body-encoding intact. |
| C-17–C-33 | All remaining aspirational | **PASS** | VERDICT guard, AMENDMENTS 3-slot, focus cascade, C-32 (formal register per V-01 axis), C-33 N/A (focus inactive). |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 2/3 × 30 = **20.000** (C-08 FAIL)
**Aspirational**: 25/25 × 10 = **10.000** (C-10 N/A = PASS)

**Composite: 90.000 — GOLDEN**

---

### V-03 — Lifecycle Emphasis: BUDGET No Delta/Flag

**Axis**: Single-axis. PM: BUDGET section retains available-hours formula and component estimate table but removes Estimated / Available / Delta / Flag closing lines. Replaced with: "Compare Total to Available hours when assigning the VERDICT score."

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline all present. |
| **C-02** | PM: BUDGET Delta + Flag present | **PARTIAL** | Budget arithmetic present (formula, component table, summed total) but structural completeness gate absent: no explicit Delta line and no Flag (OVER/UNDER/ON-BUDGET). The substitute instruction ("Compare Total to Available hours...") delegates the comparison to model inference rather than authoring it. Arithmetic present → not FAIL; Delta/Flag absent → not full PASS. |
| C-03 | Named incumbent anchors | **PASS** | All three anchors intact. |
| C-04 | ARCHITECT Do-nothing cost column | **PASS** | Column present on every row. |
| C-05 | Focus mechanics | **PASS** | Propagation Contract table intact. |
| C-06 | AMENDMENTS color-transition | **PASS** | Full three-line AMENDMENTS structure intact. |
| C-07 | Focus integration | **PASS** | N/A (focus inactive). |
| C-08 | STRATEGY coverage | **PASS** | STRATEGY fully intact; proceed-gate present. |
| C-09 | Focus propagation | **PASS** | N/A (focus inactive). |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY present and ordered before ARCHITECT. |
| C-11–C-16 | Mechanism text / ordering / body-encoding | **PASS** | All mechanism sentences authored. |
| C-17–C-33 | Remaining aspirational | **PASS** | VERDICT guard intact; C-33 PASS (Propagation Contract table present for focus-active path); C-32 PASS (formal register). |

**Essential**: 4.5/5 × 60 = **54.000** (C-02 PARTIAL = 0.5 × 12 = 6 pts lost)
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 25/25 × 10 = **10.000**

**Composite: 94.000 — NOT GOLDEN** (PARTIAL gate: C-02 PARTIAL bars golden regardless of composite)

---

### V-04 — Output Format: AMENDMENTS C-06 Isolated FAIL

**Axis**: Single-axis. AMENDMENTS sub-line 2 replaced from explicit color-transition template to vague directive "(2) If a rating change is expected, note it." Three sub-line slots preserved (C-18 PASS); slot 2 instruction does not author the required "[Component] from [COLOR] to [COLOR], raising score by [N] pts" output.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline all present. |
| C-02 | PM: BUDGET Delta + Flag | **PASS** | Full arithmetic block: Estimated / Available / Delta / Flag present. |
| C-03 | Named incumbent anchors | **PASS** | All three anchors present. |
| C-04 | ARCHITECT Do-nothing cost column | **PASS** | Required on every row. |
| C-05 | Focus mechanics | **PASS** | Propagation Contract table intact. |
| **C-06** | AMENDMENTS color-transition line | **FAIL** | Slot 2 reads "(2) If a rating change is expected, note it." — does not author "[Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." The vague instruction delegates to model inference rather than structuring the output. C-06 requires the line to be authored explicitly in the template. |
| C-07 | Focus integration | **PASS** | N/A (focus inactive). |
| C-08 | STRATEGY coverage | **PASS** | STRATEGY fully intact. |
| C-09 | Focus propagation | **PASS** | N/A (focus inactive). |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | STRATEGY present and ordered before ARCHITECT. |
| C-11–C-17 | Mechanism text / ordering / cascade / body-encoding / VERDICT guard | **PASS** | All mechanism sentences intact; VERDICT guard present. |
| C-18 | AMENDMENTS template independently authors 3 sub-line slots | **PASS** | Three sub-line slots are present in the template structure (slot 1 = action, slot 2 = vague rating note, slot 3 = inertia saved). C-18 tests slot presence, not slot specificity. C-18 PASS; C-06 FAIL. Confirms C-18 and C-06 are orthogonal. |
| C-19–C-33 | Remaining aspirational | **PASS** | C-33 PASS (Propagation Contract table, focus-active path); C-32 PASS (formal register). |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 2/3 × 30 = **20.000** (C-06 FAIL)
**Aspirational**: 25/25 × 10 = **10.000**

**Composite: 90.000 — GOLDEN**

*Parity note*: V-02 (C-08 FAIL = 90.000) and V-04 (C-06 FAIL = 90.000) match exactly. Each recommended criterion costs independently 10 pts (10/30 at 3 recommended criteria). No amplification, no discount. Additivity confirmed.

---

### V-05 — Role Sequence + Lifecycle: STRATEGY Omitted + BUDGET No Delta/Flag

**Axis**: Combination. V-02 mechanism (STRATEGY removed, inline procurement in ARCHITECT) + V-03 mechanism (BUDGET no Delta/Flag, substitute instruction). C-02 PARTIAL + C-08 FAIL. C-10 N/A (STRATEGY absent). All other essential PASS.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline all present. |
| **C-02** | PM: BUDGET Delta + Flag | **PARTIAL** | Same mechanism as V-03: budget arithmetic present, Delta and Flag absent, substitute instruction delegates to model inference. |
| C-03 | Named incumbent anchors | **PASS** | All three anchors intact. |
| C-04 | ARCHITECT Do-nothing cost column | **PASS** | Column present; procurement approach captured inline in Rationale. |
| C-05 | Focus mechanics | **PASS** | Propagation Contract table intact. |
| C-06 | AMENDMENTS color-transition | **PASS** | Full three-line AMENDMENTS structure with explicit color-transition authored. |
| C-07 | Focus integration | **PASS** | N/A (focus inactive). |
| **C-08** | STRATEGY coverage | **FAIL** | No STRATEGY section. 0% < 50%. Same mechanism as V-02. |
| C-09 | Focus propagation | **PASS** | N/A (focus inactive). |
| **C-10** | STRATEGY precedes ARCHITECT | **N/A → PASS** | STRATEGY absent → criterion vacuously N/A. Same ruling as V-02. |
| C-11–C-33 | Remaining aspirational | **PASS** | C-33 PASS (Propagation Contract table present); C-32 PASS (formal register from V-01 base). |

**Essential**: 4.5/5 × 60 = **54.000** (C-02 PARTIAL)
**Recommended**: 2/3 × 30 = **20.000** (C-08 FAIL)
**Aspirational**: 25/25 × 10 = **10.000**

**Composite: 84.000 — NOT GOLDEN** (PARTIAL gate: C-02 PARTIAL bars golden regardless of composite)

*Ranking inversion note*: V-05 (84.000) outranks R10 V-04 (80.000) by composite but is not golden while R10 V-04 is. C-28/C-29 ranking inversion confirmed for C-02 PARTIAL, not just C-04 PARTIAL. Any essential PARTIAL creates the inversion regardless of which essential criterion carries it or how many recommended FAILs co-occur.

---

### Rankings

| Rank | Variation | Composite | Golden? | Failures |
|------|-----------|-----------|---------|----------|
| 1 | **V-01** | **100.000** | **Yes** | None |
| 2 | **V-03** | **94.000** | **No** | C-02 PARTIAL |
| 3 | **V-02** | **90.000** | **Yes** | C-08 FAIL |
| 3 | **V-04** | **90.000** | **Yes** | C-06 FAIL |
| 5 | **V-05** | **84.000** | **No** | C-02 PARTIAL + C-08 FAIL |

*Ranking inversion*: V-03 (94.000, not golden) and V-05 (84.000, not golden) are both outranked in golden status by V-02 and V-04 (90.000 each, golden). PARTIAL gate dominates composite rank.

---

### Excellence Signals from V-01

V-01 (100.000) is the top-scoring variation. Three structural properties made it score maximum:

1. **Register freedom fully exploited**: Formal/technical phrasing ("You are acting as", "Do not", "STOP. Revise...") satisfies C-32 as completely as conversational phrasing. The variation demonstrates that the zero-cost axis is symmetrical — a designer can choose any register without composite penalty.

2. **All three sub-tier chains intact**: Every tier contribution is maximal. Essential 5/5 — no arithmetic section is incomplete. Recommended 3/3 — STRATEGY present, AMENDMENTS explicit, focus mechanics authored. Aspirational 25/25 — Propagation Contract in table form (C-33), STRATEGY ordered before ARCHITECT (C-10), VERDICT guard text authored (C-17), three-slot AMENDMENTS template (C-18).

3. **Propagation Contract table (C-33) and FORMULA CONTRACT CHECK close the loop**: The table format enforces focus propagation by construction. CONDITION (i) and CONDITION (ii) gate writes to Item B behind dual verification — a STOP instruction blocks progression if either condition fails. This is the by-construction C-09 mechanism: the table ensures constraint appears in 4 downstream sections simultaneously.

---

### New Patterns for v10 Rubric Update

| # | Pattern | Evidence |
|---|---------|----------|
| **P-01** | **C-32 bidirectionality confirmed**: formal register = conversational register = 100.000. The zero-cost axis spans the full register spectrum. | V-01: all PASS with strict second-person imperative framing. |
| **P-02** | **C-10 N/A on STRATEGY omission, not FAIL**: STRATEGY omission fires N/A (vacuous pass), not FAIL. The precondition of C-10 ("STRATEGY section present") is simply absent. C-10 FAIL requires ARCHITECT to appear *before* a *present* STRATEGY — a reordering, not a removal. Omission and reordering are asymmetric C-10 consequences: omission = 0 cost; reordering = full 10-pt cost (1/25 aspirational). | V-02 and V-05: C-10 N/A = PASS; composite at 90.000 and 84.000 respectively. |
| **P-03** | **C-02 PARTIAL = 94.000 confirms criterion-independent essential PARTIAL weight**: C-02 PARTIAL (BUDGET arithmetic present, Delta/Flag absent) yields 94.000 — identical to C-04 PARTIAL from R10. Essential PARTIAL penalty = 6 pts regardless of which essential criterion is PARTIAL (each essential = 12 pts; PARTIAL = 0.5 × 12 = 6 pts). The formula is uniform across the entire essential tier. | V-03: 4.5/5 × 60 + 3/3 × 30 + 25/25 × 10 = 54 + 30 + 10 = 94.000. |
| **P-04** | **C-06 FAIL and C-08 FAIL are equal-cost and independently accountable at 10 pts each**: V-02 (C-08 FAIL = 90.000) and V-04 (C-06 FAIL = 90.000) are parity-matched. Combined with R10 V-04 (C-06+C-08 = 80.000 = 20 pts compound), additivity is confirmed: no amplification or discount for pairing recommended criteria. Each recommended FAIL costs exactly 10/30 pts independently. | V-02: 5/5×60 + 2/3×30 + 25/25×10 = 90.000; V-04: same. |
| **P-05** | **PARTIAL gate dominates composite rank at 84.000**: V-05 (C-02 PARTIAL + C-08 FAIL = 84.000) is not golden; R10 V-04 (C-06+C-08 FAIL = 80.000) is golden. The ranking inversion from C-28/C-29 is criterion-independent: any essential PARTIAL blocks golden status regardless of which essential criterion carries the PARTIAL, regardless of how many recommended FAILs co-occur, and regardless of whether the composite exceeds the 80.000 golden border. The PARTIAL gate is absolute. | V-05: 4.5/5×60 + 2/3×30 + 25/25×10 = 84.000, not golden. |

---

```json
{"top_score": 100.000, "all_essential_pass": false, "new_patterns": ["C-32 bidirectionality confirmed: formal register scores identically to conversational register (both 100.000), spanning the full register spectrum on the zero-cost axis", "C-10 N/A on STRATEGY omission: STRATEGY omission fires N/A (vacuous pass), not FAIL -- C-10 FAIL requires ARCHITECT before a present STRATEGY (reordering), not removal; omission and reordering have asymmetric C-10 consequences", "C-02 PARTIAL = 94.000 confirms criterion-independent essential PARTIAL weight: uniform 6-pt penalty across essential tier regardless of which essential criterion is PARTIAL (C-02 PARTIAL = C-04 PARTIAL = 94.000)", "C-06 FAIL and C-08 FAIL are equal-cost and independently accountable at 10 pts each: parity confirmed across different recommended-tier single FAILs; additivity holds (no amplification or discount for pairing)", "PARTIAL gate dominates composite rank at 84.000: any essential PARTIAL blocks golden status regardless of which criterion, regardless of co-occurring recommended FAILs, regardless of composite exceeding 80.000 -- the gate is absolute and criterion-independent"]}
```
