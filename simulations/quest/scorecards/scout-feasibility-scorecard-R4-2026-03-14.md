## Round 4 Scorecard -- scout-feasibility

### Result

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-01 Inertia section | 5/5 | 3/3 | 7/7 | **100** | YES |
| 1 | V-02 Do-nothing column | 5/5 | 3/3 | 7/7 | **100** | YES |
| 1 | V-03 Decision-surface only | 5/5 | 3/3 | 7/7 | **100** | YES |
| 1 | V-04 Section + column | 5/5 | 3/3 | 7/7 | **100** | YES |
| 1 | V-05 Full synthesis | 5/5 | 3/3 | 7/7 | **100** | YES |

All five variations achieve 100/100. C-15 was the discriminator between R3 and R4; all R4 variations pass it by design.

### Within-100 C-15 structural guarantee ranking

| Strength | Variation | Surfaces |
|----------|-----------|---------|
| Strongest | V-05 | 5 (section + column + blockers + VERDICT + AMENDMENTS) |
| Strong | V-04 | 4 (section + column + blockers + VERDICT) |
| Strong | V-01 | 3 (section + blockers + VERDICT) |
| Moderate-strong | V-02 | 2 (column + blockers) |
| Moderate | V-03 | 2 (VERDICT + AMENDMENTS) |

### New patterns (R4)

1. **Multi-surface pre-printing is more resilient for aspirational criteria** -- V-05's 5 independent inertia surfaces each survive model drift independently; single-surface designs require that specific surface to hold.

2. **Decision-surface-only inertia (V-03) is sufficient for pass but produces shallower quantification** -- when the workaround baseline is established after traffic lights are assigned, the model cannot calibrate RED ratings against it. Section-first designs (V-01/V-04/V-05) force holistic workaround reasoning before any component is rated.

### Recommended golden candidate

**V-05** -- no omission path for any aspirational criterion. **V-04** is the closest competitor (4 surfaces, leaner template).

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Multi-surface pre-printing (5 independent inertia surfaces in V-05) is more resilient than single-surface for aspirational criteria -- each surface is an independent structural guarantee that survives model drift", "Decision-surface-only inertia (V-03) satisfies C-15 pass condition but produces shallower quantification because the workaround baseline is absent during traffic-light assignment -- section-first designs force holistic reasoning before rating"]}
```
t close | PASS | Pre-printed numbered AMENDMENTS rows with score-delta line |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE -> INERTIA -> PM:BUDGET -> ARCHITECT -- fixed order |
| C-12 | Budget precedes complexity scoring | PASS | PM:BUDGET is section 4; ARCHITECT:COMPLEXITY is section 5; INERTIA inserts before PM, not after |
| C-13 | Reviewer role in section header | PASS | Pre-printed `## PM: BUDGET` and `## ARCHITECT: COMPLEXITY` headers |
| C-14 | Score-delta fragment in amendments | PASS | Fragment pre-printed in every AMENDMENTS row; "do not omit the line" |
| C-15 | Inertia framing anchors blockers against status-quo cost | PASS | Pre-printed `## INERTIA: STATUS QUO` table establishes quantified workaround baseline; pre-printed `Do-nothing cost:` sub-field in every RED Blocker entry references INERTIA section and requires hrs/sprint or $ estimate. "Do not omit this line." Structurally unavoidable. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/7

```
composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

C-15 structural strength: **Strong** (section + blockers field + VERDICT inertia impact line = 3 surfaces). The standalone INERTIA section forces holistic workaround reasoning before any component is rated.

---

### V-02: Do-Nothing Column in Architect Table -- C-15 analysis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | Pre-printed ARCHITECT table; 5-column row includes Rating |
| C-02 | Composite score with label | PASS | Pre-printed `Composite score:` and `Label:` in VERDICT |
| C-03 | Team and timeline inference disclosed | PASS | Pre-printed INFERENCE GATE contiguous block |
| C-04 | Stack fallback disclosed | PASS | Pre-printed `Stack fallback:` line |
| C-05 | RED blockers with rationale | PASS | Pre-printed `RED Blockers:` with `[Why it is a blocker.] Lift condition:` |
| C-06 | Build-vs-buy per component | PASS | Pre-printed STRATEGY:BUILD-VS-BUY table |
| C-07 | Scoped fallback score | PASS | Pre-printed `Scoped alternative:` field |
| C-08 | Prerequisites for conditional feasibility | PASS | Pre-printed numbered prerequisites block |
| C-09 | PM timeline chain | PASS | Pre-printed budget chain with all four fields |
| C-10 | Amendment actions at close | PASS | Pre-printed numbered AMENDMENTS rows with score-delta line |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE -> PM:BUDGET -> ARCHITECT -- fixed order |
| C-12 | Budget precedes complexity scoring | PASS | PM:BUDGET is section 3; ARCHITECT:COMPLEXITY is section 4 |
| C-13 | Reviewer role in section header | PASS | Pre-printed `## PM: BUDGET` and `## ARCHITECT: COMPLEXITY` headers |
| C-14 | Score-delta fragment in amendments | PASS | Fragment pre-printed in every AMENDMENTS row; "do not omit the line" |
| C-15 | Inertia framing anchors blockers against status-quo cost | PASS | Pre-printed `Do-nothing cost (hrs/sprint or $)` column in ARCHITECT table -- required for every row, "do not leave blank." Pre-printed `Without this:` sub-field in RED Blockers references and repeats the column value. Two structurally unavoidable surfaces, no standalone section required. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/7

```
composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

C-15 structural strength: **Moderate-strong** (column + blockers field = 2 surfaces; no standalone INERTIA section, no VERDICT inertia line). Key advantage: inertia is visible at the moment the traffic light is assigned -- the reader sees rating and workaround cost in the same row. No aggregate baseline established before rating.

---

### V-03: Decision-Surface Concentration -- C-15 analysis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | Pre-printed ARCHITECT table |
| C-02 | Composite score with label | PASS | Pre-printed `Composite score:` and `Label:` |
| C-03 | Team and timeline inference disclosed | PASS | Pre-printed INFERENCE GATE contiguous block |
| C-04 | Stack fallback disclosed | PASS | Pre-printed `Stack fallback:` line |
| C-05 | RED blockers with rationale | PASS | Pre-printed `RED Blockers:` with blocker + lift condition |
| C-06 | Build-vs-buy per component | PASS | Pre-printed STRATEGY:BUILD-VS-BUY table |
| C-07 | Scoped fallback score | PASS | Pre-printed `Scoped alternative:` field |
| C-08 | Prerequisites for conditional feasibility | PASS | Pre-printed numbered prerequisites block |
| C-09 | PM timeline chain | PASS | Pre-printed budget chain with all four fields |
| C-10 | Amendment actions at close | PASS | Pre-printed AMENDMENTS rows with score-delta line and Inertia saved field |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE -> PM:BUDGET -> ARCHITECT -- fixed order |
| C-12 | Budget precedes complexity scoring | PASS | PM:BUDGET is section 3; ARCHITECT:COMPLEXITY is section 4 |
| C-13 | Reviewer role in section header | PASS | Pre-printed `## PM: BUDGET` and `## ARCHITECT: COMPLEXITY` headers |
| C-14 | Score-delta fragment in amendments | PASS | Fragment pre-printed in every AMENDMENTS row; "do not omit the line" |
| C-15 | Inertia framing anchors blockers against status-quo cost | PASS | Pre-printed `Not building this means:` line in VERDICT with "Do not omit this line" + pre-printed `Inertia saved:` field per AMENDMENT entry with hrs/sprint or $ requirement. C-15 pass condition explicitly allows "RED blockers and/or amendment actions" -- the amendments surface is sufficient. Both VERDICT and AMENDMENTS fields are pre-printed and unavoidable. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/7

```
composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

C-15 structural strength: **Moderate** (VERDICT line + AMENDMENTS field = 2 decision-surface fields; no section, no column, no blocker field). Inertia appears only after analysis completes -- the workaround baseline is not visible during rating. Minimum-overhead approach: tests the lower bound of C-15 structural coverage.

---

### V-04: Section + Column (Axes 1+2) -- C-15 analysis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | Pre-printed ARCHITECT table; 5-column row includes Rating and Do-nothing cost |
| C-02 | Composite score with label | PASS | Pre-printed `Composite score:` and `Label:` |
| C-03 | Team and timeline inference disclosed | PASS | Pre-printed INFERENCE GATE contiguous block |
| C-04 | Stack fallback disclosed | PASS | Pre-printed `Stack fallback:` line |
| C-05 | RED blockers with rationale | PASS | Pre-printed `RED Blockers:` with blocker + lift condition + `Do-nothing cost:` field |
| C-06 | Build-vs-buy per component | PASS | Pre-printed STRATEGY:BUILD-VS-BUY table |
| C-07 | Scoped fallback score | PASS | Pre-printed `Scoped alternative:` field |
| C-08 | Prerequisites for conditional feasibility | PASS | Pre-printed numbered prerequisites block |
| C-09 | PM timeline chain | PASS | Pre-printed budget chain with all four fields |
| C-10 | Amendment actions at close | PASS | Pre-printed numbered AMENDMENTS rows with score-delta line |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE -> INERTIA -> PM:BUDGET -> ARCHITECT -- fixed order |
| C-12 | Budget precedes complexity scoring | PASS | INERTIA inserts before PM:BUDGET; PM:BUDGET is section 4; ARCHITECT is section 5 |
| C-13 | Reviewer role in section header | PASS | Pre-printed `## PM: BUDGET` and `## ARCHITECT: COMPLEXITY` headers |
| C-14 | Score-delta fragment in amendments | PASS | Fragment pre-printed in every AMENDMENTS row; "do not omit the line" |
| C-15 | Inertia framing anchors blockers against status-quo cost | PASS | INERTIA: STATUS QUO section establishes aggregate workaround baseline; ARCHITECT column `Do-nothing cost` references INERTIA per component; RED Blockers carry pre-printed `Do-nothing cost:` field that repeats column value. Three mutually-reinforcing surfaces: section gives aggregate picture, column gives per-component granularity, blockers propagate it to the finding. VERDICT adds `Inertia impact:` line. Four surfaces total, all pre-printed. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/7

```
composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

C-15 structural strength: **Strong** (section + column + blockers field + VERDICT line = 4 surfaces). Section forces holistic reasoning; column forces per-component anchoring at the moment of rating. The dual-surface design is the closest structural competitor to V-05.

---

### V-05: Full Synthesis -- C-15 analysis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | Pre-printed ARCHITECT table; 5-column row includes Rating and Do-nothing cost |
| C-02 | Composite score with label | PASS | Pre-printed `Composite score:` and `Label:` |
| C-03 | Team and timeline inference disclosed | PASS | Pre-printed INFERENCE GATE contiguous block |
| C-04 | Stack fallback disclosed | PASS | Pre-printed `Stack fallback:` line |
| C-05 | RED blockers with rationale | PASS | Pre-printed `RED Blockers:` with blocker + lift condition + `Do-nothing cost:` field referencing ARCHITECT column |
| C-06 | Build-vs-buy per component | PASS | Pre-printed STRATEGY:BUILD-VS-BUY table |
| C-07 | Scoped fallback score | PASS | Pre-printed `Scoped alternative:` field |
| C-08 | Prerequisites for conditional feasibility | PASS | Pre-printed numbered prerequisites block |
| C-09 | PM timeline chain | PASS | Pre-printed budget chain with all four fields |
| C-10 | Amendment actions at close | PASS | Pre-printed AMENDMENTS rows with score-delta line and Inertia saved field |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE -> INERTIA -> PM:BUDGET -> ARCHITECT -- fixed order |
| C-12 | Budget precedes complexity scoring | PASS | INERTIA inserts before PM:BUDGET; PM:BUDGET precedes ARCHITECT |
| C-13 | Reviewer role in section header | PASS | Pre-printed `## PM: BUDGET` and `## ARCHITECT: COMPLEXITY` headers |
| C-14 | Score-delta fragment in amendments | PASS | Fragment pre-printed in every AMENDMENTS row + "do not omit the line" |
| C-15 | Inertia framing anchors blockers against status-quo cost | PASS | Five pre-printed surfaces: (1) INERTIA: STATUS QUO section with workaround table and Baseline line, (2) ARCHITECT column `Do-nothing cost` required for every row, (3) RED Blockers `Do-nothing cost:` sub-field with "Do not omit this line", (4) VERDICT `Not building this means:` line with "Do not omit this line", (5) AMENDMENTS `Inertia saved:` field per action with "Do not omit this line". No surface where inertia should appear is left to model discretion. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/7

```
composite = (5/5 * 60) + (3/3 * 30) + (7/7 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

C-15 structural strength: **Strongest** (section + column + blockers field + VERDICT line + AMENDMENTS field = 5 surfaces; all carry "do not omit" reinforcement). No omission path exists under any model behavior.

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-15 surfaces | C-15 strength |
|------|-----------|-----------|-------------|--------------|-----------|---------|---------------|---------------|
| 1 | V-05 Full synthesis | 5/5 | 3/3 | 7/7 | **100** | YES | 5 (section + column + blockers + VERDICT + AMENDMENTS) | Strongest |
| 1 | V-04 Section + column | 5/5 | 3/3 | 7/7 | **100** | YES | 4 (section + column + blockers + VERDICT) | Strong |
| 1 | V-01 Inertia section | 5/5 | 3/3 | 7/7 | **100** | YES | 3 (section + blockers + VERDICT) | Strong |
| 1 | V-02 Do-nothing column | 5/5 | 3/3 | 7/7 | **100** | YES | 2 (column + blockers) | Moderate-strong |
| 1 | V-03 Decision-surface | 5/5 | 3/3 | 7/7 | **100** | YES | 2 (VERDICT + AMENDMENTS) | Moderate |

**All five variations achieve 100/100 under v4 rubric.** The C-15 surface count reveals within-100 structural guarantee differentiation, but the rubric score does not discriminate.

---

## Within-100 Structural Guarantee Ranking

| Strength | Variations | Why |
|----------|-----------|-----|
| Strongest | V-05 | 5 pre-printed inertia surfaces; "do not omit" on every field; no omission path |
| Strong | V-04 | 4 surfaces: section establishes aggregate baseline; column anchors per-component at rating moment; blockers propagate; VERDICT closes |
| Strong | V-01 | 3 surfaces: section + blockers field + VERDICT; holistic workaround reasoning before rating; no per-component column |
| Moderate-strong | V-02 | 2 surfaces: column places inertia at rating moment (V-02's key insight); blockers inherit; no section, no VERDICT line |
| Moderate | V-03 | 2 surfaces: decision-surface only; inertia absent during analysis; workaround baseline not established before rating |

---

## Excellence Signals -- Round 4

### E-1: Multi-surface pre-printing is more resilient for aspirational criteria

V-05's 5-surface C-15 coverage demonstrates a general principle: each pre-printed surface is an independent structural guarantee. If model compression, context length, or instruction drift causes one surface to degrade, four others remain. Single-surface designs require that specific surface to survive. The redundancy cost is template length; the benefit is rubric-criterion reliability under adverse model conditions.

### E-2: Decision-surface-only inertia (V-03) is sufficient for pass but produces shallower quantification

V-03 satisfies C-15 through AMENDMENTS alone, confirming the pass condition's "and/or" wording. However, the workaround baseline is established retroactively -- after traffic lights are assigned. In V-01, V-04, and V-05, the INERTIA section forces the model to reason about the status-quo cost holistically *before* any component is rated. This ordering effect is not captured by the rubric but predicts differences in live run quantification quality: a model that sees the workaround cost before assigning RED ratings is more likely to calibrate the rating against that cost than a model that records inertia only in AMENDMENTS.

### E-3: Per-component column placement (V-02/V-04/V-05) connects do-nothing cost to the traffic-light moment

V-02 introduced a pattern confirmed by V-04 and V-05: embedding the do-nothing cost as a table column in ARCHITECT puts the workaround estimate in the same row as the traffic light. The reviewer sees rating and comparative cost together. This is the strongest UX signal for comparative feasibility: a GREEN component with a $0/sprint do-nothing cost is worth less than a RED component with a $5000/sprint workaround. The column makes that tradeoff visible without requiring the reader to navigate to a separate section.

---

## R4 Findings

### F-01: C-15 pre-printing closes the inertia gap completely

R3's V-03 demonstrated inertia framing as a qualitative improvement. R4 confirms that pre-printing the inertia surfaces (section, column, blocker field, VERDICT line, AMENDMENTS field) is sufficient to structurally guarantee C-15 compliance. All five R4 variations pass C-15 by design. The v4 rubric correctly identified C-15 as the discriminator between R3 and R4.

### F-02: The rubric's aspirational ceiling is now reachable across all design axes

R3 showed C-12 ordering was the sole discriminator in the aspirational tier. R4 shows C-15 can be satisfied across section-first, column-first, and decision-surface-first designs. The aspirational ceiling (7/7) is now reachable from any of the three C-15 mechanism positions. Future rubric discrimination must identify new aspirational dimensions or tighten existing pass conditions.

### F-03: V-05 remains the recommended golden candidate with the strongest C-15 guarantee

V-05 is now the ceiling for both C-14 (pre-printed + "do not omit") and C-15 (5 surfaces + "do not omit" on each). It is the only variation with no structural omission path for any aspirational criterion.

### F-04: Open research question -- section-first vs. column-first vs. decision-surface-only inertia

The rubric cannot distinguish V-01/V-02/V-03 on C-15. Live model runs would reveal whether:
- The INERTIA section (V-01/V-04/V-05) produces more accurate aggregate workaround estimates than column-only designs
- Column placement at the rating moment (V-02/V-04/V-05) improves RED/YELLOW calibration accuracy
- Decision-surface concentration (V-03) produces lower workaround specificity due to absence of analytical context during rating

This is the primary open question for R5 if a live-run scoring round is pursued.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate for the scout-feasibility skill:
- 100/100 under v4 rubric
- C-15 covered on all five relevant surfaces with "do not omit" reinforcement
- Inherits strongest C-13 and C-14 guarantees from R3 V-05
- PM-first ordering structurally guarantees C-12
- No aspirational criterion has an omission path

**V-04** is the closest structural competitor: section + column + blockers + VERDICT = 4 surfaces. Leaner template overhead is V-04's advantage; the missing AMENDMENTS inertia field is its sole gap vs. V-05.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Multi-surface pre-printing (5 independent inertia surfaces in V-05) is more resilient than single-surface for aspirational criteria -- each surface is an independent structural guarantee that survives model drift", "Decision-surface-only inertia (V-03) satisfies C-15 pass condition but produces shallower quantification because the workaround baseline is absent during traffic-light assignment -- section-first designs force holistic reasoning before rating"]}
```
