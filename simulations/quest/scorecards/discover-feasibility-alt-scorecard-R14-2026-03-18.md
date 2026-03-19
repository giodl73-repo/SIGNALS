# discover-feasibility-alt Scorecard — Round 14 (Rubric v12)

## Scoring Reference

**Denominator**: /37 aspirational. Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/37 × 10)`

**N/A handling**: All N/A criteria count as PASS in the numerator. Focus-axis criteria (C-05, C-07, C-09, C-23–C-27, C-33, C-43) → N/A when no focus active. STRATEGY-axis criteria (C-10–C-16) → N/A when STRATEGY absent. C-07 → N/A when no focus active.

---

## V-01 — C-02 FAIL (PM:BUDGET Section Absent)

### Essential Criteria (weight: /5 × 60)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | INFERENCE GATE: Feature, Team, Timeline present | PASS | Team + Timeline unchanged from golden |
| C-02 | PM:BUDGET block: Estimated, Available, Delta, Flag authored | FAIL | Section removed entirely; heading, table, and four-field block absent; template jumps from INERTIA directly to STRATEGY |
| C-03 | Named incumbent in 2+ downstream anchors | PASS | Anchor minimum "at least two of these three anchors required" unchanged |
| C-04 | ARCHITECT Do-nothing cost column, explicit value every row | PASS | Column and value instruction unchanged from golden |
| C-05 | focus_adjusted_total propagates to INERTIA/VERDICT/AMENDMENTS | N/A | Focus inactive |

**Essential pass count**: 4/5

### Recommended Criteria (weight: /3 × 30)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | AMENDMENTS color-transition line explicit | PASS | Explicit "(2) This moves [Component] from [COLOR] to [COLOR]" line unchanged |
| C-07 | Focus integration visibly influences base analysis | N/A | Focus inactive |
| C-08 | STRATEGY covers at least half of components | PASS | STRATEGY section present and unchanged |

**Recommended pass count**: 3/3

### Aspirational Criteria (weight: /37 × 10)

All 37 PASS or N/A (PASS). No focus active → C-05, C-07, C-09, C-23–C-27, C-33, C-43 all N/A. STRATEGY present → C-10–C-16 evaluated normally, all PASS (unchanged from golden). All scoring-formula structural criteria (C-19–C-22, C-28–C-45) PASS unconditionally under current formula.

**Aspirational pass count**: 37/37

### Score

```
(4/5 × 60) + (3/3 × 30) + (37/37 × 10) = 48 + 30 + 10 = 88.000
```

**Composite: 88.000 | Golden: No** (essential FAIL gate — C-02 FAIL bars golden regardless of composite)

**Hypothesis match: YES** (predicted 88.000)

---

## V-02 — C-05 FAIL Cascade at /37

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | INFERENCE GATE: Feature, Team, Timeline present | PASS | Unchanged from golden |
| C-02 | PM:BUDGET block complete | PASS | Present and unchanged |
| C-03 | Named incumbent in 2+ downstream anchors | PASS | Anchor minimum unchanged ("at least two required") |
| C-04 | ARCHITECT Do-nothing cost column, explicit value every row | PASS | `[base_cost]` unconditionally on every row — column header present, explicit placeholder on every row |
| C-05 | focus_adjusted_total propagates to INERTIA/VERDICT/AMENDMENTS | FAIL | Focus active. Step 0 Item C computes focus_adjusted_total correctly (4-row table present). But: INERTIA table uses `[base_cost]` unconditionally; Baseline uses `[base_cost]`; VERDICT uses `base_cost`; AMENDMENTS omits `focus_adjustment eliminated` entirely. Propagation to zero of three required destinations. |

**Essential pass count**: 4/5

**C-05 FAIL cascade (per C-23):**

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | AMENDMENTS color-transition line explicit | PASS | Explicit "(2) This moves [Component] from [COLOR] to [COLOR]" line present and unchanged |
| C-07 | Focus integration visibly influences base analysis | FAIL | Per C-23 cascade: with all downstream sections using `base_cost`, focus_adjusted_total produces no demonstrable change to ARCHITECT ratings, INERTIA baseline, or VERDICT economics. Integration is recorded in Step 0 but not propagated — cosmetic, not effective. |
| C-08 | STRATEGY covers at least half of components | PASS | STRATEGY section present and unchanged |

**Recommended pass count**: 2/3

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | FAIL | Focus active but focus_adjusted_total present in 0 downstream sections (all stripped to base_cost); threshold requires 2+ sections |
| C-33 | PASS | 4-row Propagation Contract table structurally intact in Step 0 Item A (Constraint/Section/Effect columns, one row per downstream section); table structure satisfies C-33 — deficiency is downstream only |
| C-43 | PASS | C-33 and C-09 scored independently per C-43. C-33 PASS + C-09 FAIL is the valid isolated C-33 PASS / C-09 FAIL state — table guarantees structure, prose propagation failure is downstream. |
| All others | PASS/N/A | Focus-axis meta-criteria (C-23–C-27): PASS (formula properties; C-05 essential tier assignment verified). STRATEGY-axis (C-10–C-16): PASS (STRATEGY present). C-17, C-18, C-19–C-22, C-28–C-45: PASS (unchanged formula/template). |

**Aspirational pass count**: 36/37 (C-09 FAIL)

### Score

```
(4/5 × 60) + (2/3 × 30) + (36/37 × 10) = 48 + 20 + 9.730 = 77.730
```

**Composite: 77.730 | Golden: No** (essential FAIL gate + composite < 80)

**Hypothesis match: YES** (predicted 77.730)

---

## V-03 — Three-Essential-FAIL (C-01 + C-03 + C-04)

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | INFERENCE GATE: Feature, Team, Timeline present | FAIL | Team and Timeline lines removed entirely; only Feature and Named incumbent retained |
| C-02 | PM:BUDGET block complete | PASS | Unchanged from golden |
| C-03 | Named incumbent in 2+ downstream anchors | FAIL | Anchor minimum changed to "anchor (1) is required. Anchors (2) and (3) are optional traceability aids." Template structurally guarantees at most 1 anchor — C-03 FAIL by construction. |
| C-04 | ARCHITECT Do-nothing cost column, explicit value every row | FAIL | Do-nothing cost column removed entirely: column header absent, no per-row entry, column directive stripped from ARCHITECT heading |
| C-05 | focus_adjusted_total propagates | N/A | Focus inactive |

**Essential pass count**: 2/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | AMENDMENTS color-transition line explicit | PASS | Unchanged from golden |
| C-07 | Focus visibly influences base analysis | N/A | Focus inactive |
| C-08 | STRATEGY covers at least half | PASS | STRATEGY section present and unchanged |

**Recommended pass count**: 3/3

### Aspirational Criteria

All 37 PASS or N/A. No focus → C-09, C-23–C-27, C-33, C-43 all N/A. STRATEGY present → C-10–C-16 all PASS (STRATEGY section and ARCHITECT section both present, body ordering unchanged). All scoring-formula structural criteria PASS. C-17 PASS (iff-guard present). C-18 PASS (three sub-lines present).

**Aspirational pass count**: 37/37

### Score

```
(2/5 × 60) + (3/3 × 30) + (37/37 × 10) = 24 + 30 + 10 = 64.000
```

**Composite: 64.000 | Golden: No** (essential FAIL gate + composite < 80)

**Hypothesis match: YES** (predicted 64.000) — first empirical confirmation of C-44 three-FAIL floor

---

## V-04 — C-03 FAIL + C-06 FAIL + C-08 FAIL (1-essential + 2-recommended)

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | INFERENCE GATE: Feature, Team, Timeline present | PASS | Team + Timeline present; only anchor minimum clause changed |
| C-02 | PM:BUDGET block complete | PASS | Unchanged |
| C-03 | Named incumbent in 2+ downstream anchors | FAIL | Anchor minimum changed to "anchor (1) is required. Anchors (2) and (3) are optional traceability aids." Structurally guarantees at most 1 anchor — C-03 FAIL by construction. |
| C-04 | ARCHITECT Do-nothing cost column, explicit value every row | PASS | Directive "Do-nothing cost column required on every row" retained; column header and `[focus_adjusted_total ... if active; base_cost if no focus]` instruction present on every row |
| C-05 | focus_adjusted_total propagates | N/A | Focus inactive |

**Essential pass count**: 4/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | AMENDMENTS color-transition line explicit | FAIL | Sub-line (2) replaced with "Note any expected rating improvements as appropriate" — no explicit component name, no explicit color-change form `[COLOR] to [COLOR]`, no score-delta estimate; structure delegated to model inference |
| C-07 | Focus visibly influences base analysis | N/A | Focus inactive |
| C-08 | STRATEGY covers at least half | FAIL | STRATEGY section removed entirely; inline Build/Buy/Use in ARCHITECT Rationale does not satisfy C-08 (dedicated STRATEGY section required) |

**Recommended pass count**: 1/3

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-10 | N/A → PASS | STRATEGY absent; C-35 dissolves ordering criterion to N/A — absence penalized by C-08, not double-counted here |
| C-11–C-16 | N/A → PASS | STRATEGY absent |
| C-18 | PASS | Three distinct sub-line instructions structurally present: (1) action line, (2) vague rating-improvement note (present as a distinct instruction even if content fails C-06), (3) Inertia saved line. C-22 independence applies: C-06 FAIL does not cascade to C-18 FAIL — content quality is C-06's domain, structural presence is C-18's domain |
| C-09, C-23–C-27, C-33, C-43 | N/A → PASS | Focus inactive |
| All others | PASS | Formula/independence structural properties unchanged |

**Aspirational pass count**: 37/37

### Score

```
(4/5 × 60) + (1/3 × 30) + (37/37 × 10) = 48 + 10 + 10 = 68.000
```

**Composite: 68.000 | Golden: No** (essential FAIL gate + composite < 80)

**Hypothesis match: YES** (predicted 68.000) — new 1-essential + 2-recommended cross-tier floor

---

## V-05 — C-01 FAIL + C-03 FAIL + C-08 FAIL (2-essential + 1-recommended)

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | INFERENCE GATE: Feature, Team, Timeline present | FAIL | Team and Timeline lines removed; Feature + Named incumbent retained |
| C-02 | PM:BUDGET block complete | PASS | Unchanged |
| C-03 | Named incumbent in 2+ downstream anchors | FAIL | Anchor minimum = 1 ("anchor (1) is required; anchors (2) and (3) are optional traceability aids") — structurally guarantees at most 1 anchor |
| C-04 | ARCHITECT Do-nothing cost column, explicit value every row | PASS | Directive retained; column header and per-row value instruction present |
| C-05 | focus_adjusted_total propagates | N/A | Focus inactive |

**Essential pass count**: 3/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | AMENDMENTS color-transition line explicit | PASS | Unchanged from golden: "(2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." explicit and intact |
| C-07 | Focus visibly influences base analysis | N/A | Focus inactive |
| C-08 | STRATEGY covers at least half | FAIL | STRATEGY section removed entirely; inline procurement in ARCHITECT Rationale does not satisfy C-08 |

**Recommended pass count**: 2/3

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-10–C-16 | N/A → PASS | STRATEGY absent (C-35 dissolves C-10; C-14/C-15/C-16 N/A) |
| C-09, C-23–C-27, C-33, C-43 | N/A → PASS | Focus inactive |
| C-18 | PASS | Three explicit sub-lines present and unchanged from golden |
| C-17 | PASS | VERDICT iff-guard present as static body text (unchanged) |
| All others | PASS | Formula/independence structural properties |

**Aspirational pass count**: 37/37

### Score

```
(3/5 × 60) + (2/3 × 30) + (37/37 × 10) = 36 + 20 + 10 = 66.000
```

**Composite: 66.000 | Golden: No** (essential FAIL gate + composite < 80)

**Hypothesis match: YES** (predicted 66.000) — new 2-essential + 1-recommended cross-tier floor

---

## Ranking

| Rank | Variation | Composite | Golden | FAILs |
|------|-----------|-----------|--------|-------|
| 1 | V-01 (C-02 FAIL) | 88.000 | No | 1 essential |
| 2 | V-02 (C-05 cascade) | 77.730 | No | 1 essential + 1 recommended + 1 aspirational |
| 3 | V-04 (C-03 + C-06 + C-08) | 68.000 | No | 1 essential + 2 recommended |
| 4 | V-05 (C-01 + C-03 + C-08) | 66.000 | No | 2 essential + 1 recommended |
| 5 | V-03 (C-01 + C-03 + C-04) | 64.000 | No | 3 essential |

---

## Excellence Signals (V-01)

V-01 achieves the highest composite (88.000) by isolating a single essential failure axis with no structural interactions or cascades:

1. **Section-removal is cleaner than field-removal**: Removing an entire section (PM:BUDGET) produces an unambiguous C-02 FAIL with no PARTIAL risk, no cascade risk, and no contamination of any other section's evaluation.
2. **Single-axis isolation preserves all aspirational mechanisms**: Because every other structural element (Step 0, INFERENCE GATE with Team+Timeline, INERTIA, STRATEGY, ARCHITECT, VERDICT, AMENDMENTS) is intact, all 37 aspirational criteria evaluate against their normal pass conditions. No structural disruption propagates.
3. **Focus inactive eliminates the focus-axis cost surface entirely**: With no focus active, C-05/C-07/C-09/C-23–C-27/C-33/C-43 all pass as N/A, removing the most expensive cascade path (C-05 FAIL → 77.730, as seen in V-02).
4. **Third C-38 confirmation**: C-02 FAIL = 88.000, closing per-criterion coverage through C-01, C-02, C-03 — essential tier fully confirmed criterion-neutral at the single-FAIL level.

---

## New Patterns

**Pattern 1 — C-38 C-02 confirmation**: C-02 FAIL (V-01) = 88.000. Third direct data point confirming C-38 criterion-neutrality. C-01 (R13), C-02 (R14), C-03 (R12) all confirmed at 88.000. Essential-tier single-FAIL symmetry is now confirmed across three distinct criteria.

**Pattern 2 — C-44 three-essential-FAIL floor confirmed**: Three simultaneous essential FAILs (V-03) = 64.000. First empirical confirmation of C-44's third step (1=88, 2=76, 3=64). Profile: formula at 2/5 × 60 + 30 + 10 = 64.000. Strict additivity holds: 88 − 12 − 12 = 64.

**Pattern 3 — Cross-tier topology complete for common FAIL counts**: V-04 (1-essential + 2-recommended = 68.000) and V-05 (2-essential + 1-recommended = 66.000) complete the floor sequence between 64 and 80. Full sequence: 64 (3E), 66 (2E+1R), 68 (1E+2R), 70 (3R), 76 (2E), 78 (1E+1R), 80 (2R, golden border). All positions confirmed empirically or formula-derivable. Global additivity holds across all tier boundaries with no interaction terms.

---

```json
{"top_score": 88.000, "all_essential_pass": false, "new_patterns": ["C-38 third confirmation: C-02 FAIL = 88.000, closing per-criterion coverage for C-01/C-02/C-03 at 88.000; essential single-FAIL symmetry empirically complete across three criteria", "C-44 three-essential-FAIL floor 64.000 confirmed empirically (V-03): additivity extends to triple-essential failure; profile (1=88, 2=76, 3=64) now empirically grounded at all three steps", "Cross-tier topology complete: V-04 (1E+2R=68.000) and V-05 (2E+1R=66.000) close the floor sequence 64/66/68/70/76/78/80; global additivity confirmed with no cross-tier interaction terms across all common FAIL count combinations"]}
```
