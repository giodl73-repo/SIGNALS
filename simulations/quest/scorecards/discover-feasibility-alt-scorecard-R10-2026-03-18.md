Scorecard written to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R10-2026-03-18.md`.

---

## Scorecard — discover-feasibility-alt R10 (Rubric v8, /23)

### Rankings

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-01 Conversational framing | **100.000** | Yes |
| 2 | V-02 Prose Propagation Contract | **99.565** | Yes |
| 3 | V-04 De-emphasized incumbent | **80.000** | Yes (border) |
| — | V-03 Complexity-first, cost optional | 94.000 | **No** (PARTIAL gate) |
| — | V-05 Prose + cost optional | 93.565 | **No** (PARTIAL gate) |

Golden: 3/5. The C-28/C-29 inversion is the defining structural result: V-03 leads V-04 by 14 composite points yet V-04 is golden and V-03 is not.

### Failure Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-04 (inertia 4 surfaces) | P | P | **PR** | P | **PR** |
| C-06 (amendments traceable) | P | P | P | **F** | P |
| C-08 (strategy >= 50%) | P | P | P | **F** | P |
| C-09 (propagation 2+ sections) | P | **F** | P | N/A | **F** |

All other criteria PASS or N/A across all five variations.

### Excellence Signals from V-01

**Pattern R10-A — Phrasing register is a zero-cost axis.** Conversational framing ("we", "let's", "Before proceeding...") vs imperative ("STOP", "You will record") costs exactly 0 composite points. All 31 criteria are structural, not tonal. Register is the first confirmed free dimension in the variation space.

**Pattern R10-B — The 4-row Propagation Contract table is the by-construction C-09 mechanism; prose substitution localizes focus to 1 section.** Each table row maps to one downstream section (INERTIA / ARCHITECT / VERDICT / AMENDMENTS), forcing 4-section propagation structurally. A prose contract describes INERTIA and stops — no row obligation exists. Table : C-09 :: STRATEGY-before-ARCHITECT body ordering : C-10. Both are by-construction guarantees that prose/preamble cannot replicate.

```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["Phrasing register is a zero-cost axis: conversational/colloquial framing is criterion-neutral across all 31 criteria — register and structural compliance are orthogonal, with 0 composite cost at any denominator", "The 4-row Propagation Contract table is the by-construction structural mechanism for C-09; prose substitution localizes focus to exactly 1 section because prose has no row-per-section obligation, making C-09 PASS discipline-dependent rather than structure-guaranteed"]}
```
 >= 50% coverage guaranteed. |
| C-09 | aspirational | PASS | 4-row Propagation Contract table forces propagation to INERTIA, ARCHITECT, VERDICT, AMENDMENTS (4 sections >= 2). |
| C-10 | aspirational | PASS | STRATEGY section heading appears before ARCHITECT in template body. |
| C-11 | aspirational | PASS | STRATEGY proceed-gate explicitly names components and commits Build/Buy/Use before ARCHITECT rows. |
| C-12 | aspirational | PASS | ARCHITECT opens with "Confirmation: STRATEGY: BUILD-VS-BUY is written above" -- explicit semantic back-reference. |
| C-13 | aspirational | PASS | Preamble and template body agree on section order; no conflict. |
| C-14 | aspirational | PASS | Template body ordering (STRATEGY before ARCHITECT) structural, independent of preamble directive. |
| C-15 | aspirational | PASS | C-14 PASS implies C-15 PASS; no preamble-template conflict degrades the chain. |
| C-16 | aspirational | PASS | Proceed-gate sentence in STRATEGY body; confirmation sentence in ARCHITECT body -- both static text. |
| C-17 | aspirational | PASS | VERDICT prerequisites block preceded by explicit iff-guard. |
| C-18 | aspirational | PASS | AMENDMENTS template: three independent sub-lines (action, color-transition, "Inertia saved:") each removable independently. |
| C-19 | aspirational | PASS | Guard-removal severity >> inference-only; essential-tier asymmetry preserved by formula. |
| C-20 | aspirational | PASS | C-17 and C-18 each cost 0.435 pts at /23; symmetric weight confirmed. |
| C-21 | aspirational | PASS | (5/5x60) + (3/3x30) = 90.000 >= 80; aspirational-floor ceiling holds at any N. |
| C-22 | aspirational | PASS | C-04 surface 4, C-06 traceability, C-18 sub-line independence scored independently. |
| C-23 | aspirational | PASS | C-05 essential; cascade composite = 78 - 10/N < 80 for all N >= 1. |
| C-24 | aspirational | PASS | C-07 recommended (10 pts), C-09 aspirational (0.435 pts at /23); ratio 23:1 confirmed. |
| C-25 | aspirational | PASS | C-05 FAIL semantically implies C-07 + C-09 FAIL; multiplier = 2.2x23 + 1 = 51.6x. |
| C-26 | aspirational | PASS | C-05 and C-09 scored independently; woven-once does not imply 2-section propagation. |
| C-27 | aspirational | PASS | C-09 and C-07 scored independently; propagated does not imply effective. |
| C-28 | aspirational | PASS | No essential PARTIALs; dual golden gate: PARTIAL gate not triggered, composite 100.000 >= 80 -- Golden confirmed. |
| C-29 | aspirational | PASS | No PARTIAL inversion in V-01; V-03/V-04 cross-variation inversion structurally possible under this rubric. |
| C-30 | aspirational | PASS | Recommended tier: 3 criteria x 10 pts; 1/3 pass + full essential + full aspirational = 80.000 border -- formula verified. |
| C-31 | aspirational | PASS | C-06/C-08 and C-05/C-07/C-09 axes independently scored; zero cross-axis interaction. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 23/23
**Composite**: 100.000 | **Golden**: Yes

---

## V-02 -- Output Format: Prose Propagation Contract

**Axis**: Single-axis. Output format -- prose Propagation Contract.
**Key failure**: C-09 FAIL
**Hypothesis result**: CONFIRMED -- 99.565, Golden.

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE fields unchanged; prose format does not affect preamble gate. |
| C-02 | essential | PASS | VERDICT structure intact. |
| C-03 | essential | PASS | ARCHITECT traffic-lights and RED Blockers unchanged. |
| C-04 | essential | PASS | All four inertia surfaces present; Do-nothing cost column required (not made optional). |
| C-05 | essential | PASS | Focus-weaving prohibition still present; prose format describes focus within existing sections. |
| C-06 | recommended | PASS | AMENDMENTS slot 2 fully specified; no underspecification. |
| C-07 | recommended | PASS | Prose Item C formula (focus_adjusted_total) unchanged; focus demonstrably changes base economics. |
| C-08 | recommended | PASS | STRATEGY proceed-gate mechanism unchanged. |
| C-09 | aspirational | FAIL | Prose Propagation Contract describes INERTIA impact only; no row-per-section structure forces downstream sections. Focus propagates to 1 section (< 2 required). Canonical C-26 evidence: C-05 PASS (woven into INERTIA), C-09 FAIL (1 section < 2). |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in template body. |
| C-11 | aspirational | PASS | Forward-declaration proceed-gate unchanged. |
| C-12 | aspirational | PASS | ARCHITECT back-reference to STRATEGY unchanged. |
| C-13 | aspirational | PASS | No preamble-template ordering conflict. |
| C-14 | aspirational | PASS | Body-enforced ordering unchanged. |
| C-15 | aspirational | PASS | C-14 PASS implies C-15 PASS. |
| C-16 | aspirational | PASS | Mechanism sentences in body unchanged. |
| C-17 | aspirational | PASS | VERDICT iff-guard present. |
| C-18 | aspirational | PASS | AMENDMENTS three sub-lines intact. |
| C-19 | aspirational | PASS | Formula structural property. |
| C-20 | aspirational | PASS | C-17 and C-18 symmetric at /23. |
| C-21 | aspirational | PASS | Aspirational-floor ceiling holds. |
| C-22 | aspirational | PASS | Three AMENDMENTS surfaces scored independently. |
| C-23 | aspirational | PASS | C-05 essential; cascade formula holds. |
| C-24 | aspirational | PASS | C-07/C-09 ratio = 23:1 at /23; C-09 FAIL here costs 0.435 pts -- confirmed. |
| C-25 | aspirational | PASS | Cascade multiplier semantic entailment holds. |
| C-26 | aspirational | PASS | V-02 is canonical C-26 evidence; C-05/C-09 scored independently. |
| C-27 | aspirational | PASS | Propagated != effective; each scored against own pass condition. |
| C-28 | aspirational | PASS | No essential PARTIALs; composite 99.565 >= 80, all essential PASS -- Golden. |
| C-29 | aspirational | PASS | No PARTIAL present; inversion structurally possible under rubric. |
| C-30 | aspirational | PASS | Formula border holds. |
| C-31 | aspirational | PASS | C-09 FAIL (focus axis) with C-06 PASS / C-08 PASS (strategy/amendments axis) -- zero cross-axis interaction. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 22/23 (C-09 FAIL)
**Composite**: 99.565 | **Golden**: Yes

---

## V-03 -- Lifecycle Emphasis: Complexity-first, Cost Optional

**Axis**: Single-axis. Lifecycle emphasis -- complexity-first, cost optional.
**Key failure**: C-04 PARTIAL
**Hypothesis result**: CONFIRMED -- 94.000, NOT Golden (PARTIAL gate).

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE fields present. |
| C-02 | essential | PASS | VERDICT score + label intact. |
| C-03 | essential | PASS | ARCHITECT traffic-lights and RED Blockers intact. |
| C-04 | essential | PARTIAL | Do-nothing cost column in ARCHITECT table made optional ("include if relevant"). Surface (2) may be omitted on any row -- PARTIAL: column present on some rows but not guaranteed on every row. Surfaces (1), (3), (4) intact. One of four surfaces degraded to optional. |
| C-05 | essential | PASS | Focus-weaving structure unchanged by lifecycle emphasis axis. |
| C-06 | recommended | PASS | AMENDMENTS traceability mechanism unchanged. |
| C-07 | recommended | PASS | Focus integration effect unchanged. |
| C-08 | recommended | PASS | STRATEGY build-vs-buy coverage unchanged. |
| C-09 | aspirational | PASS | 4-row Propagation Contract table structure intact; 4-section propagation preserved. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in body. |
| C-11 | aspirational | PASS | Forward-declaration unchanged. |
| C-12 | aspirational | PASS | ARCHITECT back-reference unchanged. |
| C-13 | aspirational | PASS | No preamble-template conflict. |
| C-14 | aspirational | PASS | Body-enforced ordering unchanged. |
| C-15 | aspirational | PASS | C-14 PASS implies C-15 PASS. |
| C-16 | aspirational | PASS | Mechanism sentences unchanged. |
| C-17 | aspirational | PASS | VERDICT iff-guard present. |
| C-18 | aspirational | PASS | AMENDMENTS three sub-lines intact. |
| C-19 | aspirational | PASS | Formula structural property. |
| C-20 | aspirational | PASS | Symmetric mechanism-check weights. |
| C-21 | aspirational | PASS | Aspirational-floor ceiling holds. |
| C-22 | aspirational | PASS | Three AMENDMENTS surfaces scored independently. |
| C-23 | aspirational | PASS | C-05 essential; cascade formula holds. |
| C-24 | aspirational | PASS | C-07/C-09 ratio = 23:1. |
| C-25 | aspirational | PASS | Cascade multiplier holds. |
| C-26 | aspirational | PASS | C-05/C-09 scored independently. |
| C-27 | aspirational | PASS | C-09/C-07 scored independently. |
| C-28 | aspirational | PASS | C-04 PARTIAL present; rubric correctly applies dual golden gate -- 94.000 not golden. Criterion PASS confirms gate operates correctly. |
| C-29 | aspirational | PASS | V-03 (94.000, not golden) outranked in golden status by V-04 (80.000, golden) -- canonical C-29 inversion evidence. |
| C-30 | aspirational | PASS | Formula border holds. |
| C-31 | aspirational | PASS | Lifecycle axis and strategy/amendments axis have zero interaction; C-04 PARTIAL does not cascade to C-06/C-08. |

**Essential**: 4.5/5 (C-04 PARTIAL) | **Recommended**: 3/3 | **Aspirational**: 23/23
**Composite**: 94.000 | **Golden**: No (C-04 PARTIAL triggers essential PARTIAL gate per C-28)

---

## V-04 -- Inertia Framing + Phrasing Register: De-emphasized Incumbent (combo)

**Axis**: Combo. Inertia framing + phrasing register -- de-emphasized incumbent.
**Key failures**: C-06 FAIL, C-08 FAIL
**Hypothesis result**: CONFIRMED -- 80.000, Golden (border).

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE fields present; Named Incumbent field included but de-emphasized downstream. |
| C-02 | essential | PASS | VERDICT score + label structure intact. |
| C-03 | essential | PASS | ARCHITECT traffic-lights and RED Blockers intact. |
| C-04 | essential | PASS | All four inertia surfaces present; Do-nothing cost column required on every row; incumbent name de-emphasized in headings but inertia structure preserved. |
| C-05 | essential | N/A | No focus active in this variation. |
| C-06 | recommended | FAIL | AMENDMENTS slot 2 underspecified: "If a color change is expected, note it." -- conditional phrasing produces no explicit color-transition + score-delta line. Three slots structurally present (C-18 PASS) but slot 2 content insufficient for traceability. |
| C-07 | recommended | N/A | No focus active. |
| C-08 | recommended | FAIL | De-emphasized incumbent framing weakens STRATEGY: BUILD-VS-BUY; fewer than 50% of components receive explicit Build/Buy/Use recommendations. |
| C-09 | aspirational | N/A | No focus active. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT -- structural ordering unchanged. |
| C-11 | aspirational | PASS | Forward-declaration proceed-gate present (C-08 FAIL tests coverage count, not declaration structure). |
| C-12 | aspirational | PASS | ARCHITECT back-reference to STRATEGY present. |
| C-13 | aspirational | PASS | No preamble-template conflict. |
| C-14 | aspirational | PASS | Body-enforced ordering unchanged. |
| C-15 | aspirational | PASS | C-14 PASS implies C-15 PASS. |
| C-16 | aspirational | PASS | Mechanism sentences present in body. |
| C-17 | aspirational | PASS | VERDICT iff-guard present. |
| C-18 | aspirational | PASS | Three sub-line slots structurally present; slot 2 underspecification causes C-06 FAIL but three independently-authored slots remain (C-18 tests template authoring, not slot content quality). C-22 independence confirmed. |
| C-19 | aspirational | PASS | Formula structural property. |
| C-20 | aspirational | PASS | Symmetric mechanism-check weights. |
| C-21 | aspirational | PASS | Aspirational-floor ceiling holds. |
| C-22 | aspirational | PASS | C-04 PASS / C-06 FAIL / C-18 PASS -- scored independently, no subsumption. |
| C-23 | aspirational | N/A | No focus active. |
| C-24 | aspirational | N/A | No focus active. |
| C-25 | aspirational | N/A | No focus active. |
| C-26 | aspirational | N/A | No focus active. |
| C-27 | aspirational | N/A | No focus active. |
| C-28 | aspirational | PASS | No essential PARTIALs; composite 80.000 >= 80, all essential PASS -- Golden (border). |
| C-29 | aspirational | PASS | V-04 (80.000, golden) is the lower-composite golden half of the canonical V-03/V-04 inversion pair. |
| C-30 | aspirational | PASS | C-06 FAIL + C-08 FAIL = 2 recommended FAILs = 20 pts -> 80.000. Canonical C-30 evidence. |
| C-31 | aspirational | PASS | C-06 FAIL + C-08 FAIL (strategy/amendments axis) with C-05/C-07/C-09 all N/A (no focus) -- zero cross-axis interaction. Canonical C-31 evidence. |

**Essential**: 5/5 (C-05 N/A=PASS) | **Recommended**: 1/3 (C-06 F, C-07 N/A=P, C-08 F) | **Aspirational**: 23/23 (focus N/A=PASS)
**Composite**: 80.000 | **Golden**: Yes (border)

---

## V-05 -- Output Format + Lifecycle Emphasis: Prose Contract + Cost Optional (combo)

**Axis**: Combo. Output format + lifecycle emphasis -- prose contract + cost optional.
**Key failures**: C-04 PARTIAL, C-09 FAIL
**Hypothesis result**: CONFIRMED -- 93.565, NOT Golden (PARTIAL gate).

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE intact. |
| C-02 | essential | PASS | VERDICT structure intact. |
| C-03 | essential | PASS | ARCHITECT ratings and RED Blockers intact. |
| C-04 | essential | PARTIAL | Do-nothing cost column optional (lifecycle axis) -> surface (2) degraded to PARTIAL. Prose format does not restore surface (2) obligation. Same C-04 mechanism as V-03. |
| C-05 | essential | PASS | Focus-weaving prohibition unchanged. |
| C-06 | recommended | PASS | AMENDMENTS slot 2 fully specified. |
| C-07 | recommended | PASS | Focus Item C formula unchanged; demonstrable effect mechanism intact. |
| C-08 | recommended | PASS | STRATEGY coverage mechanism unchanged. |
| C-09 | aspirational | FAIL | Prose Propagation Contract: same mechanism as V-02 -- describes INERTIA impact only. Focus propagates to 1 section (< 2). |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in body. |
| C-11 | aspirational | PASS | Forward-declaration unchanged. |
| C-12 | aspirational | PASS | ARCHITECT back-reference unchanged. |
| C-13 | aspirational | PASS | No preamble-template conflict. |
| C-14 | aspirational | PASS | Body-enforced ordering unchanged. |
| C-15 | aspirational | PASS | C-14 PASS implies C-15 PASS. |
| C-16 | aspirational | PASS | Mechanism sentences unchanged. |
| C-17 | aspirational | PASS | VERDICT iff-guard present. |
| C-18 | aspirational | PASS | AMENDMENTS three sub-lines intact. |
| C-19 | aspirational | PASS | Formula structural property. |
| C-20 | aspirational | PASS | Symmetric weights. |
| C-21 | aspirational | PASS | Aspirational-floor ceiling holds. |
| C-22 | aspirational | PASS | Three AMENDMENTS surfaces scored independently. |
| C-23 | aspirational | PASS | C-05 essential; cascade formula holds. |
| C-24 | aspirational | PASS | C-07/C-09 ratio = 23:1. |
| C-25 | aspirational | PASS | Cascade multiplier holds. |
| C-26 | aspirational | PASS | C-05 PASS (woven), C-09 FAIL (1 section) -- C-26 independence confirmed. |
| C-27 | aspirational | PASS | C-09/C-07 scored independently. |
| C-28 | aspirational | PASS | C-04 PARTIAL -> not golden at composite 93.565; dual gate confirmed. |
| C-29 | aspirational | PASS | PARTIAL inversion structurally possible under rubric. |
| C-30 | aspirational | PASS | Formula border holds. |
| C-31 | aspirational | PASS | C-09 FAIL (focus axis) with C-06/C-08 PASS (strategy/amendments axis) -- zero cross-axis interaction. |

**Essential**: 4.5/5 (C-04 PARTIAL) | **Recommended**: 3/3 | **Aspirational**: 22/23 (C-09 FAIL)
**Composite**: 93.565 | **Golden**: No (C-04 PARTIAL triggers essential PARTIAL gate)

---

## Rankings

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-01 Conversational framing | 100.000 | Yes |
| 2 | V-02 Prose Propagation Contract | 99.565 | Yes |
| 3 | V-04 De-emphasized incumbent | 80.000 | Yes (border) |
| 4 | V-03 Complexity-first, cost optional | 94.000 | No (PARTIAL gate) |
| 5 | V-05 Prose + cost optional | 93.565 | No (PARTIAL gate) |

Ranking inversion (C-29): V-03 outranks V-04 by 14 composite points yet V-04 is golden and V-03 is not. Canonical C-28/C-29 evidence at /23.

---

## Excellence Signals -- V-01

**Pattern R10-A -- Phrasing register is a zero-cost axis: conversational framing is criterion-neutral across all 31 criteria.**
V-01 shifted from imperative to conversational register throughout ("record" vs "You will record", "Before proceeding..." vs "STOP"). All 31 criteria PASS. No criterion is gated on imperative mood or formal register -- rubric detects structural compliance, not tonal compliance. Phrasing register is the first confirmed free dimension in the variation space (0 pts cost at any denominator). Comparison: V-02 prose substitution costs 0.435 pts (C-09); the register shift costs 0.000 pts. Register and format are structurally orthogonal axes.

**Pattern R10-B -- The 4-row Propagation Contract table is the by-construction structural mechanism for C-09; prose substitution localizes focus to 1 section.**
V-01 retains the 4-row table and C-09 PASS. V-02 and V-05 substitute prose and C-09 FAIL. Mechanism: each table row maps to one downstream section (INERTIA, ARCHITECT, VERDICT, AMENDMENTS); filling all four rows forces 4-section propagation structurally without writer discipline. A prose Propagation Contract describes INERTIA and stops -- no row obligation exists. The table is to C-09 what STRATEGY-before-ARCHITECT body ordering is to C-10: a by-construction guarantee that prose cannot replicate. This is the direct structural parallel of C-14's body-independence principle applied to the propagation axis.

---

## Hypotheses Confirmed in R10

| Hypothesis | Variation | Confirmed |
|-----------|-----------|-----------|
| All PASS -> 100.000, golden | V-01 | Yes |
| C-09 FAIL only -> 99.565, golden | V-02 | Yes |
| C-04 PARTIAL -> 94.000, NOT golden (PARTIAL gate) | V-03 | Yes |
| C-06+C-08 FAIL -> 80.000, golden border | V-04 | Yes |
| C-04 PARTIAL + C-09 FAIL -> 93.565, NOT golden (PARTIAL gate) | V-05 | Yes |
| C-09 cost = 0.435 pts at /23, ratio 23:1 | V-02/V-05 | Yes |
| Phrasing register is criterion-neutral (C-01 through C-31) | V-01 | Yes (new) |
| Prose format structurally localizes C-09 propagation to 1 section | V-02/V-05 | Yes (new) |
