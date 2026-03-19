I have all five variations. Now I'll score them.

---

## discover-feasibility-alt — Scorecard R6

**Rubric version**: v4 | **Date**: 2026-03-18 | **Evaluator**: Quest

---

### Scoring Formula (v4)

| Block | Formula | Denominator |
|---|---|---|
| Essential (C-01–C-05) | `(passed/5) * 60` | PARTIAL = 0.5 |
| Recommended (C-06–C-08) | `(passed/3) * 30` | N/A = 1 |
| Aspirational (C-09–C-16) | `(passed/8) * 10` | N/A = 1 |

**Golden threshold**: All 5 essential PASS (no PARTIAL, no FAIL) + composite >= 80.

---

### V-01 — Golden Baseline

**Axis**: Full template, no focus, all sections present. STRATEGY→ARCHITECT order enforced in body. AMENDMENTS has all 3 lines (action, color transition, inertia saved). VERDICT prerequisites conditional.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | **PASS** | Feature, Team, Timeline fields present. Focus optional and marked optional. |
| C-02 | VERDICT score+label+prerequisites | **PASS** | `[Only if label is FEASIBLE WITH CAVEATS:]` guard wraps prerequisites block — iff constraint holds. |
| C-03 | ARCHITECT traffic lights + RED Blockers | **PASS** | Every row gets GREEN/YELLOW/RED. RED Blockers block with blocker, Lift condition, Do-nothing cost. Fallback: "No RED components -- write exactly that." |
| C-04 | Inertia in all 4 locations | **PASS** | (1) INERTIA section + Baseline sentence; (2) Do-nothing cost column in ARCHITECT; (3) "Not building this means:" in VERDICT; (4) "Inertia saved: recaptured from [Named incumbent]:" in AMENDMENTS. All 4 present. |
| C-05 | Focus woven (no focus) | **N/A** | No focus active — auto-pass. |
| C-06 | AMENDMENTS traceable | **PASS** | Amendment contains: action line (names component), color transition line ("This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts."), and inertia saved line. All three C-06 sub-requirements met. |
| C-07 | Focus integration changes analysis | **N/A** | No focus active — auto-pass. |
| C-08 | STRATEGY covers ≥ 50% components | **PASS** | "At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT." Proceed gate enforces coverage. |
| C-09 | Focus propagates 2+ sections | **N/A** | No focus — auto-pass. |
| C-10 | STRATEGY precedes ARCHITECT | **PASS** | Template body: STRATEGY section written before ARCHITECT section by construction. |
| C-11 | STRATEGY forward-declaration + proceed gate | **PASS** | Proceed gate text: "Carrying all listed components forward to ARCHITECT. ARCHITECT will rate each component for complexity using these procurement decisions; no new components may be added in ARCHITECT without a corresponding STRATEGY entry." Components declared and committed before ARCHITECT row appears. |
| C-12 | ARCHITECT back-references STRATEGY | **PASS** | "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component." Explicit semantic cross-reference by name. |
| C-13 | Preamble ordering directive consistent | **N/A** | No explicit section ordering directive in preamble — auto-pass. |
| C-14 | Body is sole structural source | **PASS** | Body enforces STRATEGY→ARCHITECT independently. No preamble directive creates an instrumental dependency. |
| C-15 | Cascade-safe guarantee chain | **PASS** | C-10, C-11, C-12 all satisfiable by-construction from the body. No preamble-template conflict to resolve. |
| C-16 | Proceed-gate + back-reference text body-encoded | **PASS** | STRATEGY contains explicit proceed-gate sentence. ARCHITECT contains explicit confirmation sentence citing STRATEGY by name. Both present as static body text. |

**Essential**: 5/5 (C-05 N/A=1) → 5/5 × 60 = **60**
**Recommended**: 3/3 (C-07 N/A=1) → 3/3 × 30 = **30**
**Aspirational**: 8/8 (C-09 N/A=1, C-13 N/A=1) → 8/8 × 10 = **10**

**Composite: 100.000** | **Golden: YES**

---

### V-02 — C-04 PARTIAL: "Inertia saved:" Removed from AMENDMENTS

**Axis**: AMENDMENTS instruction reduced to 2 lines (action + color transition). "Inertia saved:" line removed. AMEND PROTOCOL step (3) inertia savings instruction also removed.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Unchanged from V-01. |
| C-02 | **PASS** | Unchanged — prerequisite conditional still present. |
| C-03 | **PASS** | Unchanged. |
| C-04 | **PARTIAL** | 3 of 4 required inertia surfaces: (1) INERTIA section+Baseline ✓, (2) ARCHITECT Do-nothing column ✓, (3) VERDICT "Not building this means:" ✓, (4) AMENDMENTS "Inertia saved:" ✗ — instruction replaced with "Include both lines for every amendment" and "Inertia saved:" line removed. Surface 4 absent = PARTIAL. |
| C-05 | **N/A** | No focus. |
| C-06 | **PASS** | Color transition line still present: "This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." Component named in action line. Score-delta in color transition line. All 3 C-06 sub-requirements met. |
| C-07 | **N/A** | No focus. |
| C-08 | **PASS** | STRATEGY section unchanged. |
| C-09–C-16 | **PASS/N/A** | All aspirational unchanged from V-01. |

**Essential**: 4.5/5 (C-04 PARTIAL = 0.5) → 4.5/5 × 60 = **54**
**Recommended**: 3/3 → 3/3 × 30 = **30**
**Aspirational**: 8/8 → 8/8 × 10 = **10**

**Composite: 94.000** | **Golden: NO** (C-04 PARTIAL on essential)

---

### V-03 — C-02 FAIL: Prerequisites Rendered Unconditionally

**Axis**: VERDICT prerequisites block rendered unconditionally — "[Only if label is FEASIBLE WITH CAVEATS:]" guard removed. Prerequisites appear for every output including FEASIBLE.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Unchanged. |
| C-02 | **FAIL** | V-03 VERDICT: "Prerequisites -- clear these before proceeding; the named incumbent stays ahead until resolved: ... 1. [Prerequisite -- list any open RED component prerequisites here, or write 'None' if no RED components exist.]" — no iff guard. For a FEASIBLE output (score ≥75, no RED), the template instructs the model to render a prerequisites block. Even the "write 'None'" fallback still renders the block. C-02 pass condition requires prerequisites absent when label ≠ FEASIBLE WITH CAVEATS. FAIL. |
| C-03 | **PASS** | Unchanged. |
| C-04 | **PASS** | AMENDMENTS "Inertia saved:" unchanged from V-01. |
| C-05 | **N/A** | No focus. |
| C-06 | **PASS** | All 3 amendment lines present as in V-01. |
| C-07 | **N/A** | No focus. |
| C-08 | **PASS** | Unchanged. |
| C-09–C-16 | **PASS/N/A** | Unchanged from V-01. |

**Essential**: 4/5 (C-02 FAIL = 0) → 4/5 × 60 = **48**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: 8/8 × 10 = **10**

**Composite: 88.000** | **Golden: NO** (C-02 FAIL on essential)

---

### V-04 — C-06 FAIL: Color Transition Removed from AMENDMENTS

**Axis**: AMENDMENTS color transition line ("This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.") removed. Remaining lines: action + inertia saved. VERDICT conditional intact.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Unchanged. |
| C-02 | **PASS** | Prerequisite conditional intact: "[Only if label is FEASIBLE WITH CAVEATS:]" guard present. |
| C-03 | **PASS** | Unchanged. |
| C-04 | **PASS** | "Inertia saved: recaptured from [Named incumbent]:" line retained in AMENDMENTS. All 4 surfaces intact. |
| C-05 | **N/A** | No focus. |
| C-06 | **FAIL** | AMENDMENTS reduced to action line + inertia saved line. Color transition ("This moves [Component] from [COLOR] to [COLOR]") absent. Score-delta ("raising score by approximately [N] pts.") absent. C-06 requires both. FAIL. |
| C-07 | **N/A** | No focus. |
| C-08 | **PASS** | Unchanged. |
| C-09–C-16 | **PASS/N/A** | Unchanged from V-01. |

**Essential**: 5/5 (C-05 N/A=1) → 5/5 × 60 = **60**
**Recommended**: 2/3 (C-06 FAIL=0, C-07 N/A=1, C-08 PASS) → 2/3 × 30 = **20**
**Aspirational**: 8/8 × 10 = **10**

**Composite: 90.000** | **Golden: YES** (all 5 essential PASS, composite 90 ≥ 80)

---

### V-05 — Compound: C-04 PARTIAL + C-06 FAIL

**Axis**: Both V-02 and V-04 degradations combined. AMENDMENTS reduced to action line only. No inertia saved, no color transition.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Unchanged. |
| C-02 | **PASS** | Prerequisite conditional intact. |
| C-03 | **PASS** | Unchanged. |
| C-04 | **PARTIAL** | AMENDMENTS "Inertia saved:" absent (same failure as V-02). 3 of 4 surfaces. |
| C-05 | **N/A** | No focus. |
| C-06 | **FAIL** | Color transition line absent (same failure as V-04). |
| C-07 | **N/A** | No focus. |
| C-08 | **PASS** | Unchanged. |
| C-09–C-16 | **PASS/N/A** | Unchanged from V-01. |

**Essential**: 4.5/5 (C-04 PARTIAL = 0.5) → 4.5/5 × 60 = **54**
**Recommended**: 2/3 (C-06 FAIL, C-07 N/A=1, C-08 PASS) → 2/3 × 30 = **20**
**Aspirational**: 8/8 × 10 = **10**

**Composite: 84.000** | **Golden: NO** (C-04 PARTIAL on essential)

---

### Ranking

| Rank | Variation | Composite | Golden | Key criterion |
|------|-----------|-----------|--------|---------------|
| 1 | V-01 | **100.000** | Yes | Reference baseline |
| 2 | V-04 | **90.000** | **Yes** | C-06 FAIL only |
| 3 | V-02 | 94.000 | No | C-04 PARTIAL |
| 4 | V-03 | 88.000 | No | C-02 FAIL |
| 5 | V-05 | 84.000 | No | C-04 PARTIAL + C-06 FAIL |

> Note: V-02 ranks 3rd by composite (94) but ranks below V-04 (90) on the golden axis — V-04 achieves golden where V-02 does not. The composite order and golden order diverge here: 94 > 90 in composite, but V-04 > V-02 in golden status.

---

### Score Verification

| Variation | Expected | Computed | Match |
|-----------|----------|----------|-------|
| V-01 | 100.000 | 100.000 | ✓ |
| V-02 | 94.000 | 94.000 | ✓ |
| V-03 | 88.000 | 88.000 | ✓ |
| V-04 | 90.000 | 90.000 | ✓ |
| V-05 | 84.000 | 84.000 | ✓ |

All 5 scores match hypotheses exactly.

---

### Excellence Signals (from V-01 and V-04)

**V-01 (100.000)**:
1. **AMENDMENTS three-line discipline** — all three lines (action, color transition, inertia saved) make the amendment block satisfy both C-04 (essential) and C-06 (recommended) simultaneously. Each line is load-bearing for a different criterion tier.
2. **Proceed gate as forward commitment** — STRATEGY's proceed gate names components *and* commits Build/Buy/Use for each, then explicitly states "no new components may be added in ARCHITECT without a corresponding STRATEGY entry." The gate closes the coverage loop structurally rather than instructionally.
3. **VERDICT iff guard** — the "[Only if label is FEASIBLE WITH CAVEATS:]" guard is the sole difference between C-02 PASS and FAIL. It is a single conditional wrapper with high essential weight.

**V-04 (90.000, Golden)**:
1. **Recommended-tier FAIL is golden-compatible** — V-04 is the first golden variation with a FAIL criterion. C-06 FAIL costs 10 pts (composite 100→90) but does not disqualify when all 5 essential criteria PASS. This confirms the golden threshold is a categorical essential-tier gate, not a composite threshold.

---

### Key Findings

- **AMENDMENTS is dual-load-bearing**: the "Inertia saved:" line fires C-04 (essential PARTIAL when absent); the color transition line fires C-06 (recommended FAIL when absent). Same block, different tiers, different golden consequences.
- **Cost asymmetry confirmed**: C-02 FAIL (-12 pts, essential) > C-04 PARTIAL (-6 pts, essential PARTIAL) > C-06 FAIL (-10 pts, recommended). The ordering within essential tier is FAIL (-12) > PARTIAL (-6). Recommended FAIL (-10) falls between them in composite cost but is categorically less severe (golden-compatible).
- **Golden predicate**: `all_essential_pass` is the binding condition. V-04 at 90 beats V-02 at 94 on the golden axis because V-04 has no essential degradation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["FAIL-criterion golden-compatibility: a recommended-tier FAIL (C-06) coexists with golden when all 5 essential criteria PASS — first occurrence in the series; composite 90 achieves golden over composite 94 that has an essential PARTIAL", "AMENDMENTS dual-load-bearing: the same block satisfies C-04 (essential, inertia-saved line) and C-06 (recommended, color-transition line) independently; removing either line fires a different criterion at a different tier with a different golden consequence"]}
```
