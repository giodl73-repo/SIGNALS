Now I have everything needed. Let me produce the full scorecard.

---

# discover-feasibility-alt — Score Report — Round 17

**Rubric:** v15 | **Denominator:** /40 | **Formula:** `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/40 × 10)`

---

## V-01 — Lifecycle Emphasis: Four-Essential-FAIL (C-01+C-02+C-03+C-04 FAIL, No Focus)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **FAIL** | Team and Timeline removed from INFERENCE GATE. Feature and Named incumbent retained; two required fields absent. |
| C-02 | **FAIL** | PM: BUDGET block removed entirely — no heading, no formula table, no output lines. Full absence is C-02 FAIL by C-37. |
| C-03 | **FAIL** | Propagation block stripped to single optional note: "the incumbent name should appear in AMENDMENTS savings framing as applicable." Anchor (1) heading directive removed; INERTIA column header changed to "[Status quo]" (anchor 2 voided); anchor (3) flagged optional. Template structurally guarantees at most 1 anchor — C-03 FAIL by construction. |
| C-04 | **FAIL** | ARCHITECT Do-nothing cost column entirely removed. Column header absent, per-row values absent. |
| C-05 | **N/A** | No focus active. |

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | AMENDMENTS template has explicit color-transition line "(2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." per component. |
| C-07 | **N/A** | No focus active. |
| C-08 | **PASS** | STRATEGY: BUILD-VS-BUY section present with full component table, Build/Buy/Use recommendations, and proceed gate. |

### Aspirational Criteria (key checks)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **N/A** | No focus active. |
| C-10 | **PASS** | STRATEGY section appears before ARCHITECT section in template body. |
| C-11 | **PASS** | STRATEGY body names components for ARCHITECT hand-off and commits Build/Buy/Use; proceed gate present. |
| C-12 | **PASS** | ARCHITECT opens with "Confirmation: STRATEGY: BUILD-VS-BUY is written above." |
| C-13 | **N/A** | No section ordering directive in preamble. |
| C-14 | **PASS** | Template body places STRATEGY before ARCHITECT independently of preamble. |
| C-15 | **PASS** | C-14 PASS → cascade-safe by construction. |
| C-16 | **PASS** | STRATEGY proceed gate present as static body text; ARCHITECT confirmation sentence present. |
| C-17 | **PASS** | VERDICT prerequisites block guarded by `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` |
| C-18 | **PASS** | AMENDMENTS independently authors action line, color-transition line, and Inertia saved line. |
| C-19–C-22 | **PASS** | Scoring-formula structural properties verified (tier weights unchanged). |
| C-23–C-27 | **N/A** | No focus active. |
| C-28–C-32 | **PASS** | Dual golden gate, ranking inversion, recommended border, axis orthogonality, register neutrality all hold. |
| C-33 | **N/A** | No focus active. |
| C-34 | **PASS** | Formal register bidirectionality structural property holds. |
| C-35–C-42 | **PASS** | All presence-condition, anatomy, symmetry, and scoring structural properties hold. |
| C-43 | **N/A** | No focus active. |
| C-44 | **PASS** | Four essential FAILs: 100 − 12×4 = 52. Formula additive, no amplification. |
| C-45 | **PASS** | Cross-tier additivity structural property holds. |
| C-46 | **N/A** | No focus active. |
| C-47 | **PASS** | Essential isolation profile closed (four confirmed non-cascade criteria). |
| C-48 | **PASS** | Three-essential-FAIL floor = 64.000 confirmed (C-48); K=4 is first empirical test of 100−12K beyond C-48. Formula property verified. |

### Score Computation

| Tier | Calculation | Points |
|------|-------------|--------|
| Essential | 1/5 × 60 (C-05 N/A = pass; C-01/C-02/C-03/C-04 FAIL) | 12.000 |
| Recommended | 3/3 × 30 (C-07 N/A = pass) | 30.000 |
| Aspirational | 40/40 × 10 | 10.000 |
| **Composite** | | **52.000** |

**Golden?** No — 4 essential FAILs break essential-PASS gate. Composite also < 80.

---

## V-02 — Inertia Framing: C-05 Append Cascade at /40 (C-46 Pattern, Focus Active)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Feature, Team, Timeline all present in INFERENCE GATE. |
| C-02 | **PASS** | PM: BUDGET block present with Estimated, Available, Delta, Flag explicitly authored. |
| C-03 | **PASS** | INFERENCE GATE propagation block has all three anchors with explicit specifications; minimum count 2 enforced. |
| C-04 | **PASS** | ARCHITECT table has Do-nothing cost column: "Do-nothing cost column required on every row -- use base_cost from context" with column header on the table. |
| C-05 | **FAIL** | Focus is active but 3rd preamble directive redirects all focus content to a standalone "## [FOCUS DIMENSION] ANALYSIS" block after AMENDMENTS. 4th preamble directive invites that block. INERTIA bracket: "use base_cost only in this section." ARCHITECT bracket: "rate all components against base economics only in this section." VERDICT: base_cost framing only. AMENDMENTS: base_cost savings only. focus_adjusted_total does not propagate to INERTIA, VERDICT, or AMENDMENTS — the three required destinations under C-05. |

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | AMENDMENTS has explicit action, color-transition, and inertia saved lines per component. |
| C-07 | **FAIL** | C-05 FAIL cascades. Appended focus cannot demonstrably change base analysis sections — the INERTIA and ARCHITECT sections explicitly exclude focus_adjusted_total. Base analysis is identical to no-focus baseline. |
| C-08 | **PASS** | STRATEGY: BUILD-VS-BUY present with Rationale column referencing named incumbent on base economics. |

### Aspirational Criteria (key checks)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **FAIL** | C-46 pattern: C-05 FAIL voids downstream propagation. INERTIA, ARCHITECT, VERDICT, AMENDMENTS all use base_cost. focus_adjusted_total appears only in the dedicated analysis block — not in 2+ of the named downstream sections. Cascade confirmed. |
| C-10 | **PASS** | STRATEGY precedes ARCHITECT in template body. |
| C-11–C-12 | **PASS** | Proceed gate and ARCHITECT confirmation sentence both present. |
| C-13 | **N/A** | No section ordering directive in preamble (focus-isolation directives are not ordering directives). |
| C-14–C-16 | **PASS** | Body-enforced ordering, cascade safety, mechanism text all present. |
| C-17 | **PASS** | VERDICT iff-guard present as static body text. |
| C-18 | **PASS** | AMENDMENTS three sub-lines independently authored. |
| C-19–C-22 | **PASS** | Scoring-formula structural properties hold. |
| C-23 | **PASS** | C-05 essential, cascade produces 78 − 10/40 = 77.750 < 80 — confirmed. |
| C-24 | **PASS** | C-07 recommended (10 pts), C-09 aspirational (0.250 pts), ratio 40:1. |
| C-25 | **PASS** | Cascade multiplier = (12 + 10 + 0.250)/0.250 = 89.0x at /40. |
| C-26 | **PASS** | C-05/C-09 non-subsuming — evaluated independently. |
| C-27 | **PASS** | C-07/C-09 non-subsuming — evaluated independently. |
| C-28–C-32 | **PASS** | All structural scoring properties hold. |
| C-33 | **PASS** | Step 0 has 4-row Propagation Contract table with Constraint/Section/Effect columns intact. Table is structurally complete even though Effect cells describe routing to the dedicated block. C-33 scores Step 0 structure alone. |
| C-34–C-42 | **PASS** | All structural properties hold. |
| C-43 | **PASS** | C-33 PASS, C-09 FAIL scored independently from their own pass conditions. Independence confirmed. |
| C-44–C-45 | **PASS** | Additivity properties hold. |
| C-46 | **PASS** | C-33 PASS / C-09 FAIL under C-05 FAIL confirmed at /40. The Propagation Contract table commits to per-section propagation; downstream template text executes the override. By-construction guarantee is C-05-conditional — verified at N=40. |
| C-47–C-48 | **PASS** | Structural properties hold. |

### Score Computation

| Tier | Calculation | Points |
|------|-------------|--------|
| Essential | 4/5 × 60 (C-05 FAIL) | 48.000 |
| Recommended | 2/3 × 30 (C-07 FAIL) | 20.000 |
| Aspirational | 39/40 × 10 (C-09 FAIL) | 9.750 |
| **Composite** | | **77.750** |

**Golden?** No — C-05 FAIL breaks essential-PASS gate.

**Confirms:** V-09 floor at /40 (formula 78 − 10/N at N=40 = 77.750). C-46 independence matrix confirmed at current denominator.

---

## V-03 — Output Format: C-01 + C-02 FAIL (Team+Timeline Absent, PM: BUDGET Absent)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **FAIL** | Team and Timeline removed from INFERENCE GATE. Feature present; Named incumbent with full three-anchor propagation block retained. Two required fields absent. |
| C-02 | **FAIL** | PM: BUDGET block removed entirely. INERTIA directly precedes STRATEGY in template sequence. Full absence. |
| C-03 | **PASS** | INFERENCE GATE propagation block retains all three anchor specifications with minimum count 2 enforced. Named incumbent guaranteed in heading (anchor 1), column header (anchor 2), and AMENDMENTS framing (anchor 3). |
| C-04 | **PASS** | ARCHITECT table includes Do-nothing cost column with explicit per-row placeholder. Focus-adjusted or base_cost value required on every row. |
| C-05 | **N/A** | No focus active. |

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | AMENDMENTS has explicit color-transition and score-delta per amendment. |
| C-07 | **N/A** | No focus active. |
| C-08 | **PASS** | STRATEGY: BUILD-VS-BUY present with full component table and proceed gate. |

### Aspirational Criteria (key checks)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **N/A** | No focus active. |
| C-10–C-16 | **PASS** | STRATEGY before ARCHITECT (body-enforced), proceed gate, confirmation sentence, mechanism text all present. C-13 N/A (no preamble ordering directive). |
| C-17–C-18 | **PASS** | VERDICT iff-guard and AMENDMENTS three sub-lines both present. |
| C-19–C-22 | **PASS** | Scoring-formula structural properties hold. |
| C-23–C-27 | **N/A** | No focus active. |
| C-28–C-32 | **PASS** | All structural properties hold. |
| C-33 | **N/A** | No focus active. |
| C-34–C-42 | **PASS** | All structural properties hold. |
| C-43 | **N/A** | No focus active. |
| C-44 | **PASS** | Two essential FAILs: 100 − 12×2 = 76.000. Criterion-neutrality for C-01+C-02 pair verified. |
| C-45 | **PASS** | Cross-tier additivity structural property holds. |
| C-46 | **N/A** | No focus active. |
| C-47–C-48 | **PASS** | Structural properties hold. |

### Score Computation

| Tier | Calculation | Points |
|------|-------------|--------|
| Essential | 3/5 × 60 (C-01 FAIL, C-02 FAIL) | 36.000 |
| Recommended | 3/3 × 30 (C-07 N/A = pass) | 30.000 |
| Aspirational | 40/40 × 10 | 10.000 |
| **Composite** | | **76.000** |

**Golden?** No — 2 essential FAILs break essential-PASS gate.

**Confirms:** C-44 criterion-neutrality — the C-01+C-02 pair produces 76.000, identical to the C-01+C-03 canonical pair (R13 V-04). Two-essential-FAIL additivity holds across different criterion combinations.

---

## V-04 — Phrasing Register + Lifecycle: C-02 PARTIAL, Focus Active, Formal Register

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Feature, Team, Timeline all present in INFERENCE GATE; formal phrasing ("N engineers -- inferred from: SOURCE"). |
| C-02 | **PARTIAL** | PM: BUDGET table present with Estimated and Available lines authored explicitly. Delta and Flag lines removed — completeness gate absent. Core computation present, structural completeness gate absent = PARTIAL per C-37 anatomy. |
| C-03 | **PASS** | Named incumbent propagation block with all three anchors; minimum count 2 enforced. Formal phrasing ("Propagation requirement -- the named incumbent designation must appear..."). |
| C-04 | **PASS** | ARCHITECT heading: "A Do-nothing cost column is required on every row -- focus_adjusted_total from Step 0 Item C is applied where applicable." Column present on table template. |
| C-05 | **PASS** | Focus active. Full Step 0 (Items A–D). 4-row Propagation Contract table. INERTIA bracket: "focus_adjusted_total from Step 0 Item C is applied." ARCHITECT bracket: "focus_adjusted_total from Item C may alter a component's rating." VERDICT: "focus_adjusted_total from Step 0 Item C is stated." AMENDMENTS: "base_cost recapture and focus_adjustment eliminated are stated separately." focus_adjusted_total propagates to all three required destinations. |

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | AMENDMENTS has explicit action, color-transition, and inertia saved lines; formal phrasing throughout. |
| C-07 | **PASS** | Focus active and woven. INERTIA baseline uses focus_adjusted_total — demonstrably different from no-focus baseline. ARCHITECT bracket explicitly states focus_adjusted_total may alter component ratings. Analysis demonstrably changes due to focus integration. |
| C-08 | **PASS** | STRATEGY: BUILD-VS-BUY section present with formal proceed gate language. |

### Aspirational Criteria (key checks)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **PASS** | Focus propagates to INERTIA (baseline uses focus_adjusted_total), ARCHITECT (component ratings reference focus_adjusted_total), VERDICT (Not building this means: uses focus_adjusted_total), AMENDMENTS (savings split base_cost + focus_adjustment). 4 sections ≥ 2 required. |
| C-10 | **PASS** | STRATEGY body placed before ARCHITECT in template. |
| C-11 | **PASS** | STRATEGY names components and commits Build/Buy/Use; proceed gate present. |
| C-12 | **PASS** | ARCHITECT: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. The procurement decisions established therein are applied in rating each listed component for complexity." |
| C-13 | **N/A** | No preamble ordering directive (formal directives address focus structure, not STRATEGY/ARCHITECT ordering). |
| C-14–C-16 | **PASS** | Body-enforced ordering, cascade safety, mechanism text present. |
| C-17 | **PASS** | VERDICT: "[Authored only when label is FEASIBLE WITH CAVEATS and at least one RED component exists:]" — formal phrasing of iff-guard, structurally equivalent to golden template. |
| C-18 | **PASS** | AMENDMENTS independently authors three sub-lines; formal phrasing throughout. |
| C-19–C-22 | **PASS** | Scoring-formula structural properties hold. |
| C-23 | **PASS** | C-05 essential, cascade formula 78 − 10/40 < 80 confirmed. |
| C-24 | **PASS** | C-07 recommended (10 pts), C-09 aspirational (0.250 pts), ratio 40:1. |
| C-25 | **PASS** | Cascade multiplier = 89.0x at /40. |
| C-26–C-27 | **PASS** | C-05/C-09 and C-07/C-09 non-subsuming independently verified. |
| C-28–C-32 | **PASS** | Dual golden gate (C-02 PARTIAL fires it despite 94.000 composite), ranking inversion, border, orthogonality, register neutrality all hold. |
| C-33 | **PASS** | 4-row Propagation Contract table present with Constraint/Section/Effect columns; formal column headers. |
| C-34 | **PASS** | Formal/technical register throughout: "This analysis is conducted by a PM + Architect pair executing a build-or-not feasibility assessment." Zero composite cost — C-34 criterion-neutral confirmed. |
| C-35–C-42 | **PASS** | All structural properties hold. |
| C-43 | **PASS** | C-33 and C-09 scored independently from their own pass conditions. |
| C-44–C-45 | **PASS** | Additivity properties hold. |
| C-46 | **PASS** | C-05 PASS → by-construction guarantee holds; C-33 PASS and C-09 PASS are consistent. |
| C-47–C-48 | **PASS** | Structural properties hold. |

### Score Computation

| Tier | Calculation | Points |
|------|-------------|--------|
| Essential | 4.5/5 × 60 (C-02 PARTIAL counts as 0.5) | 54.000 |
| Recommended | 3/3 × 30 | 30.000 |
| Aspirational | 40/40 × 10 | 10.000 |
| **Composite** | | **94.000** |

**Golden?** No — C-02 PARTIAL fires essential-PASS gate unconditionally (C-28). Composite 94.000 ≥ 80 cannot override the gate.

**Confirms:** C-39 focus-state independence — C-02 PARTIAL in focus-active context = 94.000, identical to C-04 PARTIAL no-focus (R12 V-02) = 94.000. The PARTIAL floor is focus-state-independent. Completes the 2×2 focus-state × PARTIAL-criterion matrix (focus-inactive C-04 PARTIAL at R12; focus-active C-02 PARTIAL here). C-34 bidirectionality confirmed at full-pass + focus-active context.

---

## V-05 — Role Sequence: C-02 FAIL + C-08 FAIL (PM: BUDGET Absent, STRATEGY Absent)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Feature, Team, Timeline all present in INFERENCE GATE. |
| C-02 | **FAIL** | PM: BUDGET block removed entirely — no heading, no formula, no table, no output lines. Full absence. |
| C-03 | **PASS** | INFERENCE GATE has all three anchor specifications with minimum count 2 enforced. |
| C-04 | **PASS** | ARCHITECT table has "Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable." Column present. |
| C-05 | **N/A** | No focus active. |

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | AMENDMENTS has action line, color-transition line, and Inertia saved line per component. |
| C-07 | **N/A** | No focus active. |
| C-08 | **FAIL** | STRATEGY: BUILD-VS-BUY section removed entirely. ARCHITECT heading replaced with "Rate each component for complexity against the named incumbent." 0% component coverage — C-08 FAIL. |

### Aspirational Criteria (key checks)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **N/A** | No focus active. |
| C-10 | **N/A** | STRATEGY section absent — C-10 dissolves to N/A per C-35 (ordering constraint has no referent). |
| C-11 | **N/A** | STRATEGY absent. |
| C-12 | **N/A** | STRATEGY absent — no back-reference target. |
| C-13 | **N/A** | No ordering directive in preamble; STRATEGY absent. |
| C-14 | **N/A** | STRATEGY absent. |
| C-15 | **N/A** | STRATEGY absent. |
| C-16 | **N/A** | STRATEGY absent — proceed gate and confirmation sentence have no host section. |
| C-17 | **PASS** | VERDICT iff-guard present as static body text. |
| C-18 | **PASS** | AMENDMENTS three sub-lines independently authored. |
| C-19–C-22 | **PASS** | Scoring-formula structural properties hold. |
| C-23–C-27 | **N/A** | No focus active. |
| C-28–C-32 | **PASS** | All structural properties hold. |
| C-33 | **N/A** | No focus active. |
| C-34–C-42 | **PASS** | All structural properties hold. |
| C-43 | **N/A** | No focus active. |
| C-44 | **PASS** | Additivity formula structural property holds. |
| C-45 | **PASS** | Cross-tier: essential (-12) + recommended (-10) = 78.000. C-02+C-08 pair verified additive. |
| C-46 | **N/A** | No focus active. |
| C-47–C-48 | **PASS** | Structural properties hold. |

### Score Computation

| Tier | Calculation | Points |
|------|-------------|--------|
| Essential | 4/5 × 60 (C-02 FAIL) | 48.000 |
| Recommended | 2/3 × 30 (C-08 FAIL; C-07 N/A = pass) | 20.000 |
| Aspirational | 40/40 × 10 (all N/A or PASS) | 10.000 |
| **Composite** | | **78.000** |

**Golden?** No — C-02 FAIL breaks essential-PASS gate.

**Confirms:** C-45 criterion-neutrality — the C-02+C-08 pair produces 78.000, identical to the C-03+C-08 canonical pair (R13 V-05). Cross-tier FAIL additivity holds regardless of which essential criterion fails.

---

## Rankings

| Rank | Variation | Composite | Golden? | Key Defects |
|------|-----------|-----------|---------|-------------|
| 1 | V-04 (C-02 PARTIAL, focus active, formal) | **94.000** | No (PARTIAL gate) | C-02 PARTIAL |
| 2 | V-05 (C-02+C-08 FAIL) | **78.000** | No | C-02 FAIL, C-08 FAIL |
| 3 | V-02 (C-05 cascade at /40) | **77.750** | No | C-05 FAIL, C-07 FAIL, C-09 FAIL |
| 4 | V-03 (C-01+C-02 FAIL) | **76.000** | No | C-01 FAIL, C-02 FAIL |
| 5 | V-01 (C-01+C-02+C-03+C-04 FAIL) | **52.000** | No | C-01–C-04 FAIL |

---

## Hypothesis Verification

| Variation | Predicted | Actual | Match? |
|-----------|-----------|--------|--------|
| V-01 | 52.000 | 52.000 | YES |
| V-02 | 77.750 | 77.750 | YES |
| V-03 | 76.000 | 76.000 | YES |
| V-04 | 94.000 | 94.000 | YES |
| V-05 | 78.000 | 78.000 | YES |

All 5 hypotheses confirmed.

---

## Excellence Signals — V-04

V-04 is the top-scoring variation (94.000). It is not golden due to C-02 PARTIAL (Delta and Flag absent from PM: BUDGET). All other criteria PASS, including the full focus axis:

1. **Full focus propagation at formal register** — C-05, C-07, C-09, C-33 all PASS. Formal/technical phrasing adds zero composite cost (C-34 confirmed at full-pass + focus-active context).
2. **Demonstrable analysis change (C-07 PASS)** — INERTIA baseline uses focus_adjusted_total; ARCHITECT ratings reference focus_adjusted_total as altering component ratings. The base analysis is demonstrably different from a no-focus run.
3. **4-row Propagation Contract at formal register (C-33 PASS)** — By-construction C-09 guarantee holds when C-05 PASS. Formal renaming of columns and items (e.g., "FORMULA CONTRACT VERIFICATION") does not affect structural pass conditions.
4. **PARTIAL gate fires precisely** — C-02 PARTIAL (core present, completeness gate absent) is the only defect. C-28/C-42 fire: 94.000 composite cannot override the PARTIAL gate. Confirms C-39 focus-state independence: PARTIAL floor is 94.000 regardless of which essential criterion carries it and regardless of focus state.

---

## New Patterns

**V-01 — K=4 empirical confirmation (first test):** C-01+C-02+C-03+C-04 FAIL = 52.000. The essential-tier additive profile 100−12K is now empirically confirmed at K=1 (88.000), K=2 (76.000), K=3 (64.000), and K=4 (52.000). K=5 (40.000) remains the sole formula-only prediction.

**V-04 — C-39 focus-state independence confirmed:** C-02 PARTIAL in focus-active + formal-register context = 94.000. Pairs with R12 V-02 (C-04 PARTIAL, no-focus = 94.000) and R11 V-03 (C-02 PARTIAL, no-focus = 94.000). The PARTIAL floor is criterion-neutral, focus-state-neutral, and register-neutral. The 2×2 focus-state × PARTIAL matrix is now complete.

**V-03 — C-44 pair coverage extended:** C-01+C-02 FAIL = 76.000. Canonical pair was C-01+C-03 (R13). Different essential pair, same composite. C-44 criterion-neutrality now confirmed for two distinct pairs.

**V-05 — C-45 pair coverage extended:** C-02+C-08 FAIL = 78.000. Canonical pair was C-03+C-08 (R13). Different essential criterion, same cross-tier composite. C-45 criterion-neutrality now confirmed for two distinct essential+recommended combinations.

**V-02 — C-46 at /40 confirmed:** C-33 PASS / C-09 FAIL under C-05 FAIL = 77.750 (formula 78 − 10/40). Prior anchors were at /37 and /38. Formula monotone confirmed at N=40.

---

```json
{"top_score": 94, "all_essential_pass": false, "new_patterns": ["K=4 four-essential-FAIL floor = 52.000: essential-tier additive profile 100-12K empirically confirmed at K=4 (C-01+C-02+C-03+C-04 FAIL = 52.000); K=5 (40.000) is now the sole remaining formula-only prediction"]}
```
