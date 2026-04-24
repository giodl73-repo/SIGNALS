Scorecard written to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R3-2026-03-18.md`.

```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["C-14 and C-15 are independent detectors: C-14 fires on wrong body ordering regardless of preamble state; C-15 fires only when a preamble-template conflict makes C-11/C-12 runtime-dependent -- V-02 isolates this by showing C-14 FAIL with C-15 PASS when body inverts but no preamble exists", "V-05 zero-cost C-13 upgrade pattern holds under v3 /7 denominator: consistent preamble converts C-13 from N/A to active PASS at zero composite cost because C-14 PASS means the body independently enforces ordering -- the preamble is documentational, not instrumental", "V-03 floor drops from 93.000 (R2) to 92.143 (v3) for the identical failure set: the /7 denominator absorbs two new FAIL criteria (C-14, C-15) across the same failure set, widening the aspiration-block penalty by 0.857 pts"]}
```
label + prerequisites | PASS | Score/label format present; prerequisites gated to FEASIBLE WITH CAVEATS + RED |
| C-03 ARCHITECT traffic-lights + RED Blockers | PASS | All rows carry GREEN/YELLOW/RED; RED Blockers template has all three sub-fields |
| C-04 Four inertia surfaces | PASS | All four: INERTIA section + Baseline, Do-nothing cost column, "Not building this means:", "Inertia saved:" |
| C-05 Focus woven in, not appended | PASS | Propagation Contract routes focus to INERTIA/ARCHITECT/VERDICT/AMENDMENTS; Item D explicitly rejects standalone focus section |
| C-06 AMENDMENTS traceable to RED/YELLOW | PASS | Each amendment names component, color transition, score-delta |
| C-07 Focus visibly influences base analysis | PASS/N/A | focus_adjusted_total changes ARCHITECT ratings; economics routed to all downstream cells |
| C-08 STRATEGY covers >=50% components | PASS | "At least half must carry an explicit recommendation" enforced by-construction (STRATEGY written before ARCHITECT) |
| C-09 Focus propagates to 2+ sections | PASS | Contract routes same constraint to INERTIA + ARCHITECT + VERDICT + AMENDMENTS |
| C-10 STRATEGY precedes ARCHITECT | PASS | Body sequence: STRATEGY before ARCHITECT |
| C-11 STRATEGY forward-declaration + proceed gate | PASS | "List all components you intend to assess in ARCHITECT below. At least half must carry an explicit recommendation here before you proceed to ARCHITECT." |
| C-12 ARCHITECT back-reference to STRATEGY | PASS | "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions..." |
| C-13 Preamble-body ordering consistency | N/A -> PASS | No preamble directive present; no conflict to evaluate |
| C-14 Body is sole structural source for ordering | PASS | Body places STRATEGY before ARCHITECT independently; no preamble directive means body is the only source |
| C-15 Cascade-safe guarantee chain | PASS | No preamble-template conflict exists; C-11/C-12 by-construction reachable; C-10 holds by body structure |

**Essential**: 5/5 PASS | **Recommended**: 3/3 PASS | **Aspirational**: 7/7

```
Composite = (5/5 x 60) + (3/3 x 30) + (7/7 x 10) = 60 + 30 + 10 = 100.000
```

**Band: GOLDEN** | all essential PASS (no PARTIALs) + 100.000 >= 80

---

## V-02 — C-14 Isolated Failure (body inverted, no preamble)

**Template structure**: Body places ARCHITECT -> STRATEGY (inverted). No preamble directive. STRATEGY loses forward-declaration (now backward-reference: "Cover at least half the components from ARCHITECT above"). ARCHITECT loses confirmation/back-reference.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 INFERENCE GATE completeness | PASS | Fields present and non-empty |
| C-02 VERDICT score + label + prerequisites | PASS | Format intact |
| C-03 ARCHITECT traffic-lights + RED Blockers | PASS | Template unchanged for this section |
| C-04 Four inertia surfaces | PASS | All four surfaces preserved |
| C-05 Focus woven in | PASS | Propagation Contract + Item D still present |
| C-06 AMENDMENTS traceable | PASS | Amendment format unchanged |
| C-07 Focus influences analysis | PASS/N/A | Economics intact |
| C-08 STRATEGY covers >=50% components | PASS | Coverage instruction present; passes as output check even though ordering is wrong |
| C-09 Focus propagates to 2+ sections | PASS | Contract still routes to 4 sections |
| C-10 STRATEGY precedes ARCHITECT | FAIL | Body places ARCHITECT before STRATEGY; no by-construction guarantee |
| C-11 STRATEGY forward-declaration + proceed gate | FAIL | STRATEGY written after ARCHITECT in body order; "Cover at least half the components from ARCHITECT above" is backward-reference, not forward-declaration |
| C-12 ARCHITECT back-reference to STRATEGY | FAIL | ARCHITECT heading stripped of confirmation/back-reference; STRATEGY has not been written at ARCHITECT's body-execution time |
| C-13 Preamble-body ordering consistency | N/A -> PASS | No preamble directive |
| C-14 Body is sole structural source for ordering | FAIL | Body places ARCHITECT before STRATEGY -- body actively enforces wrong ordering; it is not the sole structural source of correct ordering |
| C-15 Cascade-safe guarantee chain | PASS | No preamble-template conflict exists (no preamble). C-10/C-11/C-12 fail due to body-order inversion, not conflict-cascade. C-15 failure condition ("preamble-template ordering conflict makes C-11/C-12 runtime-dependent") is absent. |

**Essential**: 5/5 PASS | **Recommended**: 3/3 PASS | **Aspirational**: 3/7 (C-09=1, C-10=0, C-11=0, C-12=0, C-13=N/A=1, C-14=0, C-15=1)

```
Composite = (5/5 x 60) + (3/3 x 30) + (3/7 x 10) = 60 + 30 + 4.286 = 94.286
```

**Band: GOLDEN** | all essential PASS (no PARTIALs) + 94.286 >= 80

---

## V-03 — C-14 + C-15 Compound Failure (body inverted + conflicting preamble)

**Template structure**: Body places ARCHITECT -> STRATEGY (inverted). Preamble directive says "Write STRATEGY before ARCHITECT" -- direct conflict. STRATEGY is backward-reference. ARCHITECT has no back-reference.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 INFERENCE GATE completeness | PASS | Fields present |
| C-02 VERDICT score + label + prerequisites | PASS | Format intact |
| C-03 ARCHITECT traffic-lights + RED Blockers | PASS | Template unchanged |
| C-04 Four inertia surfaces | PASS | All four present |
| C-05 Focus woven in | PASS | Propagation Contract + Item D present |
| C-06 AMENDMENTS traceable | PASS | Format intact |
| C-07 Focus influences analysis | PASS/N/A | Economics intact |
| C-08 STRATEGY covers >=50% components | PASS | Coverage instruction present |
| C-09 Focus propagates to 2+ sections | PASS | Contract routes to 4 sections |
| C-10 STRATEGY precedes ARCHITECT | PARTIAL | Preamble instructs STRATEGY first; body writes ARCHITECT first. Execution order uncertain -- model may follow preamble or body. Probabilistic, not by-construction. |
| C-11 STRATEGY forward-declaration + proceed gate | FAIL | At STRATEGY's body-execution time, ARCHITECT has already been written; forward-declaration is structurally impossible |
| C-12 ARCHITECT back-reference to STRATEGY | FAIL | At ARCHITECT's body-execution time, STRATEGY has not been written; back-reference has no target |
| C-13 Preamble-body ordering consistency | FAIL | Preamble: "STRATEGY before ARCHITECT." Body: ARCHITECT before STRATEGY. Direct structural contradiction. |
| C-14 Body is sole structural source for ordering | FAIL | Body places ARCHITECT before STRATEGY; preamble directive cannot substitute; body enforces wrong ordering |
| C-15 Cascade-safe guarantee chain | FAIL | Preamble-template ordering conflict explicitly exists (C-13 FAIL). This degrades C-10 from by-construction to probabilistic (PARTIAL), and cascades to C-11 and C-12: both are runtime-dependent rather than structurally guaranteed. Cascade condition is present. |

**Essential**: 5/5 PASS | **Recommended**: 3/3 PASS | **Aspirational**: 1.5/7 (C-09=1, C-10=0.5, C-11=0, C-12=0, C-13=0, C-14=0, C-15=0)

```
Composite = (5/5 x 60) + (3/3 x 30) + (1.5/7 x 10) = 60 + 30 + 2.143 = 92.143
```

**Band: GOLDEN** | all essential PASS (C-10 PARTIAL is aspirational, not essential) + 92.143 >= 80

Note: V-03 floor under v3 = 92.143, vs V-05-R2's 93.000. The 0.857-pt drop is the /7 denominator absorbing two new FAIL criteria (C-14, C-15) across the same failure set.

---

## V-04 — C-15 Cascade Independence (correct body, C-11 + C-12 mechanisms removed)

**Template structure**: Body preserves STRATEGY -> ARCHITECT order. No preamble directive. STRATEGY loses proceed gate sentence. ARCHITECT loses confirmation + back-reference sentence.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 INFERENCE GATE completeness | PASS | Fields present |
| C-02 VERDICT score + label + prerequisites | PASS | Format intact |
| C-03 ARCHITECT traffic-lights + RED Blockers | PASS | Template unchanged |
| C-04 Four inertia surfaces | PASS | All four present |
| C-05 Focus woven in | PASS | Propagation Contract + Item D intact |
| C-06 AMENDMENTS traceable | PASS | Format intact |
| C-07 Focus influences analysis | PASS/N/A | Economics intact |
| C-08 STRATEGY covers >=50% components | PASS | Coverage instruction still present ("List all components you intend to assess in ARCHITECT") |
| C-09 Focus propagates to 2+ sections | PASS | Contract routes to 4 sections |
| C-10 STRATEGY precedes ARCHITECT | PASS | Body enforces STRATEGY before ARCHITECT; by-construction |
| C-11 STRATEGY forward-declaration + proceed gate | FAIL | Proceed gate sentence removed; "at least half must carry an explicit recommendation here before you proceed" absent. Components named but no commit threshold stated. |
| C-12 ARCHITECT back-reference to STRATEGY | FAIL | "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions..." removed; ARCHITECT heading is standalone |
| C-13 Preamble-body ordering consistency | N/A -> PASS | No preamble directive |
| C-14 Body is sole structural source for ordering | PASS | Body places STRATEGY before ARCHITECT; no preamble directive; body is sole structural source and enforces correct ordering |
| C-15 Cascade-safe guarantee chain | PASS | No preamble-template conflict. C-11 and C-12 fail because their specific mechanisms were removed -- independent mechanism failures, not conflict-cascade. C-10 holds by construction. Cascade condition absent. |

**Essential**: 5/5 PASS | **Recommended**: 3/3 PASS | **Aspirational**: 4/7 (C-09=1, C-10=1, C-11=0, C-12=0, C-13=N/A=1, C-14=1, C-15=1)

```
Composite = (5/5 x 60) + (3/3 x 30) + (4/7 x 10) = 60 + 30 + 5.714 = 95.714
```

**Band: GOLDEN** | all essential PASS (no PARTIALs) + 95.714 >= 80

---

## V-05 — Zero-Cost C-13 Upgrade (consistent preamble + correct body)

**Template structure**: Body preserves STRATEGY -> ARCHITECT (V-01 structure). Preamble directive added: "Write STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY." Preamble matches body sequence -- no conflict. All C-11 and C-12 mechanisms intact.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 INFERENCE GATE completeness | PASS | Fields present |
| C-02 VERDICT score + label + prerequisites | PASS | Format intact |
| C-03 ARCHITECT traffic-lights + RED Blockers | PASS | Template unchanged |
| C-04 Four inertia surfaces | PASS | All four present |
| C-05 Focus woven in | PASS | Propagation Contract + Item D intact |
| C-06 AMENDMENTS traceable | PASS | Format intact |
| C-07 Focus influences analysis | PASS/N/A | Economics intact |
| C-08 STRATEGY covers >=50% components | PASS | By-construction; STRATEGY precedes ARCHITECT and names components |
| C-09 Focus propagates to 2+ sections | PASS | Contract routes to 4 sections |
| C-10 STRATEGY precedes ARCHITECT | PASS | Body enforces STRATEGY before ARCHITECT by construction; preamble agrees |
| C-11 STRATEGY forward-declaration + proceed gate | PASS | "At least half must carry an explicit recommendation here before you proceed to ARCHITECT" intact |
| C-12 ARCHITECT back-reference to STRATEGY | PASS | "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions..." present |
| C-13 Preamble-body ordering consistency | PASS | Preamble instructs STRATEGY before ARCHITECT; body places STRATEGY before ARCHITECT. No conflict. |
| C-14 Body is sole structural source for ordering | PASS | Body enforces correct ordering independently; preamble is documentational -- removing it would not change body behavior |
| C-15 Cascade-safe guarantee chain | PASS | No preamble-template conflict (C-13 PASS). C-14 PASS ensures body independently enforces ordering. C-11/C-12 by-construction reachable. Cascade-safe. |

**Essential**: 5/5 PASS | **Recommended**: 3/3 PASS | **Aspirational**: 7/7 (all PASS)

```
Composite = (5/5 x 60) + (3/3 x 30) + (7/7 x 10) = 60 + 30 + 10 = 100.000
```

**Band: GOLDEN** | all essential PASS (no PARTIALs) + 100.000 >= 80

---

## Rankings

| Rank | Variation | Aspirational | Composite | Golden |
|------|-----------|-------------|-----------|--------|
| 1 (tie) | V-01 -- Baseline (no preamble, correct body, full mechanisms) | 7/7 | 100.000 | YES |
| 1 (tie) | V-05 -- Consistent preamble + correct body (C-13 upgrade) | 7/7 | 100.000 | YES |
| 3 | V-04 -- Correct body, C-11/C-12 removed | 4/7 | 95.714 | YES |
| 4 | V-02 -- Body inverted, no preamble (C-14 isolated failure) | 3/7 | 94.286 | YES |
| 5 | V-03 -- Body inverted + conflicting preamble (cascade) | 1.5/7 | 92.143 | YES |

All five variations pass Golden. Discriminators are entirely aspirational.

---

## Excellence Signals

**1. Body-enforced ordering is the load-bearing guarantee.** The template body placing STRATEGY before ARCHITECT is what makes C-10, C-14, and C-15 pass structurally. All three cascade from this single design decision. V-02 and V-03 lose 5-8 aspirational points by inverting this -- no preamble can recover it.

**2. C-14 and C-15 are independent detectors with distinct failure conditions.** C-14 fires when the body enforces wrong ordering (V-02, V-03). C-15 fires only when a preamble-template conflict makes C-11/C-12 runtime-dependent (V-03 only). V-04 confirms C-15 does not fire when C-11/C-12 fail for independent mechanism reasons.

**3. The V-05 zero-cost C-13 upgrade pattern holds under v3 /7 denominator.** Adding a consistent preamble directive converts C-13 from N/A to active PASS at zero composite cost (100.000 unchanged vs V-01). A conflicting preamble (V-03) costs 7.857 pts; a consistent preamble costs 0.

**4. C-11 and C-12 are independently removable at symmetric cost.** V-04 removes both while preserving C-10/C-14/C-15. Score drops 4.286 pts (100 to 95.714) -- 2.143 pts each under the /7 denominator. Non-redundant, independently scored, independently dropped.

---

## Key Discriminators (v3 new findings)

- **V-02 vs V-03 (C-15 isolation)**: Both have inverted body order. V-02 has no preamble (C-15 PASS). V-03 adds conflicting preamble (C-15 FAIL). The 2.143-pt difference between them is the exact cost of the cascade condition.
- **V-04 vs V-02 (C-15 probe)**: Both have C-11 and C-12 failing. V-04: body correct, no conflict, C-15 PASS. V-02: body inverted, no conflict, C-15 PASS. Neither triggers cascade. Confirms C-15 is a conflict detector, not a C-10 detector.
- **V-03 floor under v3**: 92.143 (vs 93.000 in R2 for the same failure set). The 0.857-pt drop reflects two new FAIL criteria (C-14, C-15) diluting the aspirational fraction across the wider /7 denominator.

---

## Scorecard Summary

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|-------------|-----------|------|
| V-01 | 5/5 | 3/3 | 7/7 | 100.000 | GOLDEN |
| V-02 | 5/5 | 3/3 | 3/7 | 94.286 | GOLDEN |
| V-03 | 5/5 | 3/3 | 1.5/7 | 92.143 | GOLDEN |
| V-04 | 5/5 | 3/3 | 4/7 | 95.714 | GOLDEN |
| V-05 | 5/5 | 3/3 | 7/7 | 100.000 | GOLDEN |
