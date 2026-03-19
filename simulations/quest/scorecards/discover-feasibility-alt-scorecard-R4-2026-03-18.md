## discover-feasibility-alt — Round 4 Scorecard

**Rubric**: v4 | **Denominator**: /8 aspirational | **Date**: 2026-03-18

---

## Evaluation Matrix

### V-01 — Baseline (V-01-R3 carried forward, both mechanism sentences present)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | PASS | Template has Feature, Team, Timeline, Named incumbent — all required fields present |
| C-02 | VERDICT score + label consistent | PASS | VERDICT structure present with score/label contract; range-label mapping enforced by template |
| C-03 | ARCHITECT traffic-light ratings + RED Blockers | PASS | Table requires GREEN/YELLOW/RED per row; RED Blockers section with blocker/Lift/Do-nothing-cost sub-fields |
| C-04 | Inertia in all four locations | PASS | (1) INERTIA: STATUS QUO section with Baseline sentence; (2) Do-nothing cost column on every ARCHITECT row; (3) "Not building this means:" in VERDICT; (4) "Inertia saved:" in AMENDMENTS |
| C-05 | Focus content woven, not appended | N/A=1 | No focus active; auto-pass confirmed by Item D failure-mode rejection clause |
| C-06 | AMENDMENTS traceable to RED/YELLOW | PASS | Template requires component name, color transition, score-delta per amendment |
| C-07 | Focus integration influences base analysis | N/A=1 | No focus active |
| C-08 | STRATEGY covers ≥50% of components | PASS | STRATEGY table lists all ARCHITECT components; proceed-gate instruction enforces ≥50% coverage before handoff |
| C-09 | Focus propagates to 2+ sections | N/A=1 | No focus active |
| C-10 | STRATEGY precedes ARCHITECT in body | PASS | Template body places STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY — ordering by-construction |
| C-11 | STRATEGY forward-declaration + proceed gate | PASS | Proceed-gate sentence present: "List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT." |
| C-12 | ARCHITECT opens with back-reference to STRATEGY | PASS | Confirmation sentence present: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity." |
| C-13 | Preamble directive consistent with template | N/A=1 | No preamble ordering directive present |
| C-14 | Body is sole structural source for ordering | PASS | Body places STRATEGY before ARCHITECT independently; any preamble directive would be documentational only |
| C-15 | Cascade-safe guarantee chain | PASS | No preamble-template conflict; C-10 is by-construction, making C-11/C-12 structurally reachable |
| C-16 | Proceed-gate + confirmation text body-encoded | PASS | Both static sentences present: proceed-gate in STRATEGY body, confirmation in ARCHITECT body |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 8/8 × 10 = **10.000**
**Composite: 100.000**

---

### V-02 — Confirmation sentence removed from ARCHITECT only

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | PASS | Unchanged from V-01 |
| C-02 | VERDICT score + label consistent | PASS | Unchanged |
| C-03 | ARCHITECT traffic-light ratings + RED Blockers | PASS | Unchanged |
| C-04 | Inertia in four locations | PASS | Unchanged |
| C-05 | Focus content woven | N/A=1 | No focus |
| C-06 | AMENDMENTS traceable | PASS | Unchanged |
| C-07 | Focus integration visible | N/A=1 | No focus |
| C-08 | STRATEGY covers ≥50% | PASS | Proceed-gate sentence still present in STRATEGY |
| C-09 | Focus propagates 2+ sections | N/A=1 | No focus |
| C-10 | STRATEGY precedes ARCHITECT | PASS | Body ordering unchanged |
| C-11 | STRATEGY forward-declaration + proceed gate | PASS | Proceed-gate sentence still present in STRATEGY body |
| C-12 | ARCHITECT back-reference to STRATEGY | **FAIL** | Confirmation sentence removed — ARCHITECT section contains no semantic cross-reference to STRATEGY |
| C-13 | Preamble consistent with template | N/A=1 | No preamble directive |
| C-14 | Body is sole structural source | PASS | STRATEGY still precedes ARCHITECT in body |
| C-15 | Cascade-safe guarantee chain | PASS | No preamble-template conflict; C-10 remains by-construction despite C-12 FAIL |
| C-16 | Proceed-gate + confirmation text body-encoded | **FAIL** | Confirmation sentence absent from ARCHITECT body — one of two required mechanism sentences missing |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 6/8 × 10 = **7.500**
**Composite: 97.500**

---

### V-03 — Proceed-gate sentence removed from STRATEGY only

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | PASS | Unchanged |
| C-02 | VERDICT score + label consistent | PASS | Unchanged |
| C-03 | ARCHITECT traffic-light ratings + RED Blockers | PASS | Unchanged |
| C-04 | Inertia in four locations | PASS | Unchanged |
| C-05 | Focus content woven | N/A=1 | No focus |
| C-06 | AMENDMENTS traceable | PASS | Unchanged |
| C-07 | Focus integration visible | N/A=1 | No focus |
| C-08 | STRATEGY covers ≥50% | PASS | STRATEGY table still instructs ≥50% coverage; absence of proceed-gate language degrades enforcement but C-08 passes on output-checked coverage |
| C-09 | Focus propagates 2+ sections | N/A=1 | No focus |
| C-10 | STRATEGY precedes ARCHITECT | PASS | Body ordering unchanged |
| C-11 | STRATEGY forward-declaration + proceed gate | **FAIL** | Proceed-gate sentence removed — STRATEGY no longer commits components as forward-declarations for ARCHITECT; coverage becomes output-checked (C-08) not by-construction |
| C-12 | ARCHITECT back-reference to STRATEGY | PASS | Confirmation sentence still present in ARCHITECT body |
| C-13 | Preamble consistent with template | N/A=1 | No preamble directive |
| C-14 | Body is sole structural source | PASS | STRATEGY still precedes ARCHITECT |
| C-15 | Cascade-safe guarantee chain | PASS | No preamble-template conflict; structural ordering preserved even though C-11 fails |
| C-16 | Proceed-gate + confirmation text body-encoded | **FAIL** | Proceed-gate sentence absent from STRATEGY body — one of two required mechanism sentences missing |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 6/8 × 10 = **7.500**
**Composite: 97.500**

---

### V-04 — Both mechanism sentences absent (V-04-R3 reconfirm under v4)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | PASS | Unchanged |
| C-02 | VERDICT score + label consistent | PASS | Unchanged |
| C-03 | ARCHITECT traffic-light ratings + RED Blockers | PASS | Unchanged |
| C-04 | Inertia in four locations | PASS | Unchanged |
| C-05 | Focus content woven | N/A=1 | No focus |
| C-06 | AMENDMENTS traceable | PASS | Unchanged |
| C-07 | Focus integration visible | N/A=1 | No focus |
| C-08 | STRATEGY covers ≥50% | PASS | Structural ordering still holds C-08 to output-checked pass |
| C-09 | Focus propagates 2+ sections | N/A=1 | No focus |
| C-10 | STRATEGY precedes ARCHITECT | PASS | Body ordering unchanged — structural guarantee of section precedence intact |
| C-11 | STRATEGY forward-declaration + proceed gate | **FAIL** | Proceed-gate sentence absent; no forward commitment linking STRATEGY components to ARCHITECT evaluation |
| C-12 | ARCHITECT back-reference to STRATEGY | **FAIL** | Confirmation sentence absent; ARCHITECT section makes no semantic reference to STRATEGY |
| C-13 | Preamble consistent with template | N/A=1 | No preamble directive |
| C-14 | Body is sole structural source | PASS | STRATEGY still physically precedes ARCHITECT in body; C-14 tests structural ordering, not mechanism text |
| C-15 | Cascade-safe guarantee chain | PASS | No preamble-template conflict; C-10 remains by-construction even with mechanism sentences absent |
| C-16 | Proceed-gate + confirmation text body-encoded | **FAIL** | Both mechanism sentences absent — neither the proceed-gate (STRATEGY) nor the confirmation (ARCHITECT) exists as static body text |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 5/8 × 10 = **6.250**
**Composite: 96.250**

> **Denominator note**: Under v3 (/7), V-04-R3 scored 95.714 with C-11+C-12 FAIL (5/7). Under v4 (/8), V-04 scores 96.250 with C-11+C-12+C-16 FAIL (5/8). Three failures score *higher* than two because per-criterion cost drops from 1.429 to 1.250 pts — the /8 denominator absorbs the additional failure.

---

### V-05 — Full mechanism text + consistent preamble (zero-cost C-13 upgrade)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | INFERENCE GATE completeness | PASS | Unchanged |
| C-02 | VERDICT score + label consistent | PASS | Unchanged |
| C-03 | ARCHITECT traffic-light ratings + RED Blockers | PASS | Unchanged |
| C-04 | Inertia in four locations | PASS | Unchanged |
| C-05 | Focus content woven | N/A=1 | No focus |
| C-06 | AMENDMENTS traceable | PASS | Unchanged |
| C-07 | Focus integration visible | N/A=1 | No focus |
| C-08 | STRATEGY covers ≥50% | PASS | Proceed-gate present; C-13 PASS adds documentational confirmation of ordering but does not change C-08 |
| C-09 | Focus propagates 2+ sections | N/A=1 | No focus |
| C-10 | STRATEGY precedes ARCHITECT | PASS | Body ordering unchanged; preamble directive matches body — no conflict introduced |
| C-11 | STRATEGY forward-declaration + proceed gate | PASS | Proceed-gate sentence present, identical to V-01 |
| C-12 | ARCHITECT back-reference to STRATEGY | PASS | Confirmation sentence present, identical to V-01 |
| C-13 | Preamble directive consistent with template | **PASS** | Preamble directive added and matches body section order (STRATEGY before ARCHITECT) — upgrades from N/A to PASS at zero composite cost |
| C-14 | Body is sole structural source | PASS | Body ordering enforces STRATEGY-before-ARCHITECT independently; preamble directive is purely documentational |
| C-15 | Cascade-safe guarantee chain | PASS | Preamble directive consistent with body — no conflict; C-13 PASS confirms cascade-safe, not merely N/A |
| C-16 | Proceed-gate + confirmation text body-encoded | PASS | Both mechanism sentences present, identical to V-01 |

**Essential**: 5/5 × 60 = **60.000**
**Recommended**: 3/3 × 30 = **30.000**
**Aspirational**: 8/8 × 10 = **10.000**
**Composite: 100.000**

> **Zero-cost confirmation**: C-13 N/A (V-01) and C-13 PASS (V-05) both contribute 1 to the numerator. Adding a consistent preamble directive upgrades C-13 from N/A to active PASS without touching any other criterion. Denominator-invariant property confirmed under /8.

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60.000 | 30.000 | 10.000 | **100.000** |
| V-02 | 60.000 | 30.000 | 7.500 | **97.500** |
| V-03 | 60.000 | 30.000 | 7.500 | **97.500** |
| V-04 | 60.000 | 30.000 | 6.250 | **96.250** |
| V-05 | 60.000 | 30.000 | 10.000 | **100.000** |

**Rank**: V-01 = V-05 (100.000) > V-02 = V-03 (97.500) > V-04 (96.250)

---

## Excellence Signals (from V-01 / V-05)

1. **Mechanism text as static body sentences, not implicit convention** — The proceed-gate ("List all components... At least half must carry an explicit Build/Buy/Use recommendation here before you proceed to ARCHITECT") and confirmation ("Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions...") are verbatim body text, not inferred from section adjacency. C-16 is satisfied by text presence, not structural proximity.

2. **Proceed-gate as forward commitment, not coverage instruction** — The proceed-gate names the handoff explicitly and sets a threshold ("at least half") before ARCHITECT evaluation begins. This converts C-08 from an output-checked instruction into a by-construction property: coverage exists in STRATEGY before ARCHITECT rows are written.

3. **Confirmation sentence establishes semantic dependency by name** — Citing "STRATEGY: BUILD-VS-BUY" by exact section name in the ARCHITECT opening makes the informational dependency explicit. Adjacency alone does not establish dependency; naming does.

4. **Body-first ordering makes preamble purely documentational** — STRATEGY preceding ARCHITECT in the template body means C-10, C-14, and C-15 all hold structurally. A matching preamble directive (V-05) then adds C-13 PASS at zero cost — it documents the guarantee rather than creating a new model-compliance dependency.

5. **Denominator growth absorbs per-criterion failure cost** — V-04's three failures under /8 score higher than V-04-R3's two failures under /7 (96.250 vs 95.714). The rubric correctly encodes that adding a new aspirational criterion should not penalize templates that fail it any harder than the existing failure cost per criterion.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": []}
```
