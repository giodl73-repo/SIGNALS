I have all the information needed. Now I can score all five variations.

---

# discover-feasibility-alt — Round 1 Scorecard

**Rubric version**: v1 (2026-03-18)  
**Session goal**: Validate C-10 (STRATEGY before ARCHITECT) — the only unconfirmed aspirational criterion from R7.  
**Floor**: C-01 through C-09 all confirmed PASS 100.0 in prior session. Only C-10 varies across variations.

---

## V-01 — Baseline Confirm (V-05-R7 exact)

**Axis**: Establish 95.000 gap baseline. ARCHITECT template precedes STRATEGY template; no ordering directive.

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 INFERENCE GATE fields | essential | PASS | Feature / Team / Timeline present; Named incumbent propagation anchors all present. Unchanged from confirmed R7 base. |
| C-02 VERDICT score + label consistency | essential | PASS | VERDICT template with numeric score, label, and conditional prerequisites structure intact. |
| C-03 ARCHITECT traffic-light + RED Blockers | essential | PASS | Every component row requires GREEN/YELLOW/RED; RED Blockers template with all 3 sub-fields present. |
| C-04 Four inertia surfaces | essential | PASS | (1) INERTIA STATUS QUO section + Baseline sentence; (2) Do-nothing cost column on ARCHITECT row template; (3) "Not building this means:" in VERDICT; (4) "Inertia saved:" in AMENDMENTS. All four present and templated. |
| C-05 Focus woven not appended | essential | PASS | Item D "Failure-mode rejection" explicitly prohibits standalone focus section after AMENDMENTS. No focus-appended block in template. |
| C-06 AMENDMENTS traceable | recommended | PASS | AMENDMENTS template requires component name, color transition, score-delta, and Inertia saved arithmetic on every entry. |
| C-07 Focus visibly influences base analysis | recommended | PASS | Propagation Contract (Item A table) + CONDITION (i)/(ii) gates force `focus_adjusted_total` to appear in ARCHITECT/INERTIA/VERDICT/AMENDMENTS. Focus changes the analysis by construction. |
| C-08 STRATEGY covers ≥50% components | recommended | PASS | STRATEGY template: "Cover at least half the components from ARCHITECT." Explicit coverage instruction. |
| C-09 Focus propagates to 2+ downstream sections | aspirational | PASS | Item A table routes focus constraint to INERTIA, ARCHITECT, VERDICT, AMENDMENTS — four sections guaranteed. CONDITION (i)/(ii) gates enforce arithmetic presence in AMENDMENTS + VERDICT. |
| C-10 STRATEGY before ARCHITECT | aspirational | **FAIL** | Template presents ARCHITECT section (line ~175) before STRATEGY section (line ~194). No ordering instruction in preamble or at section boundaries. A model executing in template order writes ARCHITECT before STRATEGY. |

**Essential pass count**: 5/5  
**Recommended pass count**: 3/3  
**Aspirational pass count**: C-09=1.0, C-10=0.0 → (1.0+0.0)/2 = 0.5

```
Composite = (5/5 × 60) + (3/3 × 30) + (0.5 × 10)
          = 60.000 + 30.000 + 5.000
          = 95.000
```

**Golden**: YES (all 5 essential PASS, composite 95.000 ≥ 80) — but C-10 gap confirmed.

---

## V-02 — Section Ordering (structural C-10 fix)

**Axis**: STRATEGY template physically moved before ARCHITECT template. STRATEGY instruction updated to forward declaration ("List components you intend to assess in ARCHITECT; at least half must carry a recommendation here before you proceed"). ARCHITECT instruction updated to "Using the STRATEGY decisions above, rate each listed component."

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 INFERENCE GATE fields | essential | PASS | Fields and Named incumbent anchors unchanged from V-01 base. |
| C-02 VERDICT score + label consistency | essential | PASS | VERDICT template unchanged. |
| C-03 ARCHITECT traffic-light + RED Blockers | essential | PASS | ARCHITECT section content unchanged; only position relative to STRATEGY changed. |
| C-04 Four inertia surfaces | essential | PASS | All four surfaces present. STRATEGY section move does not affect any inertia surface. |
| C-05 Focus woven not appended | essential | PASS | Item D prohibition intact; no structural change introduces a standalone focus section. |
| C-06 AMENDMENTS traceable | recommended | PASS | AMENDMENTS template unchanged from V-01. |
| C-07 Focus visibly influences base analysis | recommended | PASS | Propagation Contract unchanged; focus_adjusted_total gates unchanged. |
| C-08 STRATEGY covers ≥50% components | recommended | PASS | Forward-declaration instruction: "at least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT." Equivalent semantics to V-01; enforced pre-ARCHITECT by construction. |
| C-09 Focus propagates to 2+ downstream sections | aspirational | PASS | Four-section propagation unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | **PASS** | STRATEGY template at line 418 physically precedes ARCHITECT template at line 430. ARCHITECT section reads "Using the STRATEGY decisions above." By-construction guarantee: a model executing in template sequence writes STRATEGY before ARCHITECT. No instruction can fail; the template's own structure enforces it. |

**Essential pass count**: 5/5  
**Recommended pass count**: 3/3  
**Aspirational pass count**: (1.0+1.0)/2 = 1.0

```
Composite = (5/5 × 60) + (3/3 × 30) + (1.0 × 10)
          = 60.000 + 30.000 + 10.000
          = 100.000
```

**Golden**: YES — all essential PASS, composite 100.000.

---

## V-03 — Preamble Directive (instruction-only C-10 fix)

**Axis**: Preamble gains explicit ordering directive: *"Write STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY. Required section sequence: INERTIA -> PM: BUDGET -> STRATEGY -> ARCHITECT -> VERDICT -> AMENDMENTS. Do not write ARCHITECT before STRATEGY appears in the output."* Template order unchanged — ARCHITECT still precedes STRATEGY in the template body.

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 INFERENCE GATE fields | essential | PASS | Fields and propagation anchors unchanged. |
| C-02 VERDICT score + label consistency | essential | PASS | VERDICT template unchanged. |
| C-03 ARCHITECT traffic-light + RED Blockers | essential | PASS | ARCHITECT section content unchanged. |
| C-04 Four inertia surfaces | essential | PASS | All four surfaces present and unchanged. |
| C-05 Focus woven not appended | essential | PASS | Item D prohibition intact. |
| C-06 AMENDMENTS traceable | recommended | PASS | AMENDMENTS template unchanged. |
| C-07 Focus visibly influences base analysis | recommended | PASS | Propagation Contract gates unchanged. |
| C-08 STRATEGY covers ≥50% components | recommended | PASS | STRATEGY instruction unchanged from V-01. |
| C-09 Focus propagates to 2+ downstream sections | aspirational | PASS | Four-section propagation unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | **PARTIAL** | Preamble instruction is explicit: "Do not write ARCHITECT before STRATEGY appears in the output" with a stated sequence. This is in the most-read part of the prompt and states a hard prohibition. However, the template body places ARCHITECT before STRATEGY, creating a structural execution-order conflict. The preamble instruction is strong and prohibitive — models generally respect explicit "do not" constraints — but a model treating the template as an execution script may follow template order regardless of preamble directives after processing several prior sections. Scored PARTIAL: strong instruction likelihood of success (~70%) but structural template conflict introduces non-negligible failure risk that V-02's by-construction guarantee eliminates. |

**Essential pass count**: 5/5  
**Recommended pass count**: 3/3  
**Aspirational pass count**: (1.0+0.5)/2 = 0.75

```
Composite = (5/5 × 60) + (3/3 × 30) + (0.75 × 10)
          = 60.000 + 30.000 + 7.500
          = 97.500
```

**Golden**: YES — all essential PASS, composite 97.500 ≥ 80.

---

## V-04 — ARCHITECT Prerequisite Gate (section-level stop)

**Axis**: ARCHITECT section heading gains prerequisite stop condition: "Check before writing any table row: is the STRATEGY: BUILD-VS-BUY section already present in the output above? Yes — proceed. No — STOP. Write the full STRATEGY: BUILD-VS-BUY section now using the template below, then return here." Template order unchanged — ARCHITECT still precedes STRATEGY template.

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 INFERENCE GATE fields | essential | PASS | Unchanged. |
| C-02 VERDICT score + label consistency | essential | PASS | Unchanged. |
| C-03 ARCHITECT traffic-light + RED Blockers | essential | PASS | Stop condition precedes table rows; does not alter rating or RED Blockers structure. |
| C-04 Four inertia surfaces | essential | PASS | All four surfaces present; stop condition does not displace any inertia surface. |
| C-05 Focus woven not appended | essential | PASS | Item D prohibition intact. |
| C-06 AMENDMENTS traceable | recommended | PASS | AMENDMENTS unchanged. |
| C-07 Focus visibly influences base analysis | recommended | PASS | Propagation Contract gates unchanged. |
| C-08 STRATEGY covers ≥50% components | recommended | PASS | STRATEGY template at line 931 retains "Cover at least half the components from ARCHITECT." When the stop condition routes to this template, the coverage instruction is executed. |
| C-09 Focus propagates to 2+ downstream sections | aspirational | PASS | Unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | **PASS** | The stop condition fires at the ARCHITECT section heading, before any table row is written. The check "is STRATEGY already present?" evaluates to No in a first-run following template order. The model is directed to "Write the full STRATEGY: BUILD-VS-BUY section now using the template below." The template routes to the STRATEGY section at line 931 — a complete, standalone section template. The model writes STRATEGY as a standalone section, then returns to complete ARCHITECT table rows. In the output, STRATEGY appears before the ARCHITECT table. The ARCHITECT section heading is written first, but the C-10 pass condition checks "STRATEGY section appears before the ARCHITECT table" — the heading alone does not constitute the ARCHITECT table, so STRATEGY-before-table ordering satisfies C-10. The execution-time enforcement point (at the ARCHITECT section boundary) catches ordering violations that preamble instructions (V-03) cannot guarantee when template order conflicts. |

**Essential pass count**: 5/5  
**Recommended pass count**: 3/3  
**Aspirational pass count**: (1.0+1.0)/2 = 1.0

```
Composite = (5/5 × 60) + (3/3 × 30) + (1.0 × 10)
          = 60.000 + 30.000 + 10.000
          = 100.000
```

**Golden**: YES — all essential PASS, composite 100.000.

---

## V-05 — Combined V-02 + V-04 (belt-and-suspenders)

**Axis**: V-02 structural reordering (STRATEGY before ARCHITECT in template) + V-04 gate adapted as confirmation: ARCHITECT heading reads "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity."

| Criterion | Tier | Score | Evidence |
|-----------|------|-------|----------|
| C-01 INFERENCE GATE fields | essential | PASS | Unchanged. |
| C-02 VERDICT score + label consistency | essential | PASS | Unchanged. |
| C-03 ARCHITECT traffic-light + RED Blockers | essential | PASS | ARCHITECT content unchanged; confirmation statement precedes table but does not alter structure. |
| C-04 Four inertia surfaces | essential | PASS | All four surfaces present. |
| C-05 Focus woven not appended | essential | PASS | Item D prohibition intact. |
| C-06 AMENDMENTS traceable | recommended | PASS | Unchanged. |
| C-07 Focus visibly influences base analysis | recommended | PASS | Propagation Contract unchanged. |
| C-08 STRATEGY covers ≥50% components | recommended | PASS | STRATEGY template at line 1155-1163 has forward-declaration instruction (V-02 form): "List all components you intend to assess in ARCHITECT; at least half must carry an explicit recommendation here before you proceed to ARCHITECT." By-construction enforcement since STRATEGY is written before ARCHITECT. |
| C-09 Focus propagates to 2+ downstream sections | aspirational | PASS | Unchanged. |
| C-10 STRATEGY before ARCHITECT | aspirational | **PASS** | STRATEGY template at line 1155 physically precedes ARCHITECT at line 1167 (by-construction, V-02 inheritance). Additionally, ARCHITECT heading opens with "Confirmation: STRATEGY: BUILD-VS-BUY is written above" — this produces observable evidence in the output that the model registered the ordering constraint at ARCHITECT execution time. The confirmation gate also provides AMEND-path protection: if an AMEND rewrites only ARCHITECT, the confirmation statement at the ARCHITECT heading re-asserts the ordering requirement at the moment of rewrite. Dual-guarantee: structural + behavioral. |

**Essential pass count**: 5/5  
**Recommended pass count**: 3/3  
**Aspirational pass count**: (1.0+1.0)/2 = 1.0

```
Composite = (5/5 × 60) + (3/3 × 30) + (1.0 × 10)
          = 60.000 + 30.000 + 10.000
          = 100.000
```

**Golden**: YES — all essential PASS, composite 100.000.

---

## Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Composite | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|-----------|--------|
| V-01 Baseline | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL** | 95.000 | YES |
| V-02 Structural reorder | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | 100.000 | YES |
| V-03 Preamble directive | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PARTIAL** | 97.500 | YES |
| V-04 ARCHITECT gate | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | 100.000 | YES |
| V-05 Combined | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** | 100.000 | YES |

**Ranking**: V-02, V-04, V-05 tied (100.000) > V-03 (97.500) > V-01 (95.000)

---

## C-10 Discriminator Analysis

The key finding from this round:

- **V-02 PASS (structural)** and **V-04 PASS (execution-gate)** both satisfy C-10 through different mechanisms, confirming C-10 is achievable by construction and by instruction.
- **V-03 PARTIAL** confirms that a preamble directive alone, when structurally contradicted by template order, carries non-trivial failure risk. The explicit "do not" constraint is strong but not deterministic when template order conflicts.
- **V-03 fails to close the gap V-02 closes**: instruction-only fixes do not eliminate structural ordering risk. Template order is a load-bearing execution signal.
- **V-04 vs V-03 verdict**: execution-time enforcement (V-04) outperforms preamble-time instruction (V-03) when template order conflicts with the intended sequence. The stop condition fires at the exact decision point and the model has not yet written any ARCHITECT table rows.
- **V-05 is the production promotion candidate**: V-02's structural guarantee + V-04's confirmation gate. The confirmation gate converts from a stop condition to an assertion, and provides AMEND-path traceability that neither V-02 nor V-04 alone provides.

---

## Excellence Signals

**From V-02, V-04, V-05:**

1. **Structural reordering converts output-checked criteria into by-construction properties.** Moving STRATEGY before ARCHITECT in the template eliminates C-10 as a compliance check entirely — the template's own sequence is the guarantee. This is the same principle that makes CONDITION (i)/(ii) gates reliable: structure enforces what instructions can only recommend.

2. **Execution-point gates outperform preamble directives for mid-stream ordering enforcement.** When template order conflicts with intended execution order, a stop condition at the conflicted section boundary (V-04) is more reliable than a preamble instruction (V-03). By the time a model reaches section N in a long template, preamble instructions may not dominate; the gate at section N fires at the exact decision moment.

3. **Confirmation gates as AMEND-path protection.** V-05's "Confirmation: STRATEGY: BUILD-VS-BUY is written above" at the ARCHITECT heading protects against AMEND-path failures where a partial rewrite could re-introduce ordering violations. Structural guarantees from V-02 may be disrupted in amendment rewrites; the confirmation gate re-asserts the ordering requirement at ARCHITECT execution time in every invocation including AMEND.

4. **Forward-reference inversion in STRATEGY instruction (V-02/V-05).** Changing STRATEGY from "Cover at least half the components from ARCHITECT" (backward reference — ARCHITECT not yet written) to "List all components you intend to assess in ARCHITECT; at least half must carry an explicit recommendation here before you proceed" (forward declaration — ARCHITECT not yet written, that's the point) eliminates the broken forward reference while preserving C-08 semantics. The instruction now matches the execution context: STRATEGY runs before ARCHITECT, so it plans ARCHITECT's component list, not reviews it.

---

## Recommendation

**Promote V-05 to production.** V-05 achieves 100.000 by construction (V-02 structural guarantee) with explicit confirmation evidence at the ARCHITECT heading (V-04 adaptation) and AMEND-path protection. V-02 and V-04 each individually achieve 100.000, confirming the mechanisms are independently valid. The combined form is the safe production choice.

**Retire V-03's instruction-only approach for ordering constraints.** PARTIAL on C-10 under V-03 confirms that when template order conflicts with a preamble directive, structural fixes are required. Preamble instructions work for additive constraints (do not add a section); they are insufficient for reordering constraints (write section A before section B) when the template presents section B before section A.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Execution-point gates outperform preamble directives for mid-stream ordering enforcement when template order conflicts with intended sequence — a stop condition at the conflicted section boundary fires at the exact decision moment where preamble instructions may no longer dominate", "Forward-reference inversion: STRATEGY instruction updated from backward-looking coverage check ('cover at least half the components from ARCHITECT') to forward declaration ('list components you intend to assess in ARCHITECT') to match pre-ARCHITECT execution context", "Confirmation gates as AMEND-path protection: converting a stop condition into an assertion at the ARCHITECT heading produces observable traceability in every invocation including AMEND rewrites, defending against partial-rewrite ordering regressions"]}
```
