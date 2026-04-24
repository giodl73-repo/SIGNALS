Now I have enough to evaluate all five variations. Let me compile the full scoring.

---

## Scoring: `topic:status` Round 18 — Rubric v16 (max 295)

### Variation Feature Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-47 (labeled PN-ADVERSARY entries) | 3 labels (P1+P2+P3) | prose only | 2 labels (P2+P3) | 3 labels (P1+P2+P3) | prose only |
| C-48 (PHASE 1 adversary block) | present | present | absent | present | absent |
| C-49 (STOP pred 4) | present | present | present (vacuous) | absent | present (vacuous) |

---

### Criterion-by-Criterion Evaluation

#### Essential (C-01–C-04, 15 pts each)

| ID | Name | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|------|
| C-01 | Signal discovery | PASS | PASS | PASS | PASS | PASS |
| C-02 | Coverage percentage | PASS | PASS | PASS | PASS | PASS |
| C-03 | Gap identification | PASS | PASS | PASS | PASS | PASS |
| C-04 | Display-only behavior | PASS | PASS | PASS | PASS | PASS |

All variations are full-stack R17 baselines with surgical ablations only; display-only behavior and core coverage mechanics are untouched in all five.

#### Recommended (C-05–C-07, 10 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-05 Readiness verdict | PASS | PASS | PASS | PASS | PASS |
| C-06 Namespace breakdown | PASS | PASS | PASS | PASS | PASS |
| C-07 Strategy cross-reference | PASS | PASS | PASS | PASS | PASS |

#### Aspirational (C-08–C-12, 5 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-08 Recency awareness | PASS | PASS | PASS | PASS | PASS |
| C-09 Actionable next step | PASS | PASS | PASS | PASS | PASS |
| C-10 Structural namespace completeness | PASS | PASS | PASS | PASS | PASS |
| C-11 Phase-gated execution | PASS | PASS | PASS | PASS | PASS |
| C-12 Gap-first output ordering | PASS | PASS | PASS | PASS | PASS |

V-03 redesign specifically preserved the *Prevents:* annotation and planning table ordering, eliminating the C-12/C-20 contamination observed in R16's V-03. The discrete sub-section removal of the PHASE 1 adversary block does not touch readiness-first template ordering. PASS confirmed for all.

#### Structural Tiers 2–10 (C-13–C-38, 5 pts each)

All twenty-six criteria: **PASS for all five variations.** The ablations are confined to (a) preamble ADVERSARY CHAIN entry labeling, (b) PHASE 1 execution body adversary block, and (c) Phase 1 STOP CONDITION predicate count. No ablation touches the structural-tier-2-through-10 machinery (triple redundancy, template-first absorption, per-signal assertion chain, consequence vocabulary, dual-axis exit, named-exit labeling, preamble invariant declarations).

#### Structural Tier 11–13 (C-39–C-44, 5 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-39 OUTPUT DECL trigger characterization | PASS | PASS | PASS | PASS | PASS |
| C-40 OUTPUT DECL sub-component labeling | PASS | PASS | PASS | PASS | PASS |
| C-41 PHASE 3 output decl + labeled sub-components | PASS | PASS | PASS | PASS | PASS |
| C-42 Phase-entry adversary declaration (PHASE 2) | PASS | PASS | PASS | PASS | PASS |
| C-43 PHASE 3 execution-body adversary declaration | PASS | PASS | PASS | PASS | PASS |
| C-44 Preamble output declaration chain | PASS | PASS | PASS | PASS | PASS |

PHASE 2 and PHASE 3 adversary blocks are explicitly retained in all five variations. Output declaration machinery untouched.

#### Structural Tier 14 (C-45–C-46, 5 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-45 Preamble adversary chain declaration | PASS | PASS | PASS | PASS | PASS |
| C-46 Adversary defeat condition sub-component | PASS | PASS | PASS | PASS | PASS |

C-45 requires the ADVERSARY CHAIN block to name Phase 2 and Phase 3 adversaries as a two-element chain — not to use labeled entries (that is C-47). V-02 and V-05 revert to running prose but the block and its two-phase chain content are intact: PASS. V-03 has two labeled sub-entries (P2+P3) — fully satisfies the two-phase chain requirement: PASS.

C-46 requires DEFEAT CONDITION sub-components at Phase 2 and Phase 3 adversary sites. All five variations retain Phase 2 and Phase 3 three-part blocks explicitly: PASS.

#### Structural Tier 15 (C-47–C-48, 5 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-47 | Preamble adversary chain labeled sub-entries | **PASS** | **FAIL** | **PASS** | **PASS** | **FAIL** |
| C-48 | PHASE 1 execution-body adversary declaration | **PASS** | **PASS** | **FAIL** | **PASS** | **FAIL** |

**C-47 evidence:**

- V-01: Three labeled sub-entries `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` present. C-48 is present so three labels required — exactly satisfied. PASS.
- V-02 (C-47 ablation axis): ADVERSARY CHAIN block present in running prose. No `PN-ADVERSARY:` labels at any position. Explicit C-47 FAIL. C-48 retained, so the three-adversary count is still present in the chain — but without labeled sub-entries, C-47 fails regardless of adversary count.
- V-03: Two labeled sub-entries `P2-ADVERSARY:` and `P3-ADVERSARY:`. C-48 is absent; per rubric "when C-48 is absent (two-phase chain), two labels are sufficient for C-47 compliance — the absence of a P1-ADVERSARY: label is not a C-47 violation when no PHASE 1 adversary body has been declared." PASS.
- V-04: Three labeled sub-entries retained (C-48 also present). PASS.
- V-05 (C-47 ablation axis): Running prose, no labels. FAIL. Note: prose enumerates Phase 2 and Phase 3 adversaries only (Phase 1 absent from chain), but labeling failure is the controlling reason.

**C-48 evidence:**

- V-01: PHASE 1 execution body contains three-part block: `ADVERSARY: inertia toward empty-glob assumption` + `DEFEAT CONDITION: DISK_SIGNALS populated from live glob with zero-result case handled explicitly`. PASS.
- V-02: PHASE 1 adversary block explicitly retained in ablation description. C-47 is the sole ablation axis. PASS.
- V-03 (C-48 ablation axis, redesigned): PHASE 1 adversary block removed as a discrete sub-section. No ADVERSARY / DEFEAT CONDITION sub-section between *Prevents:* annotation and planning table. P1-ADVERSARY label absent from chain. Explicit C-48 FAIL. Clean isolation confirmed: the *Prevents:* annotation, planning table, and all C-12/C-20 structural elements are intact — contamination from R16 eliminated by sub-section form design.
- V-04: PHASE 1 adversary block fully present. PASS.
- V-05 (C-47+C-48 combination): Phase 1 adversary block absent. FAIL.

---

### Composite Scores

| Variation | C-01–C-46 | C-47 | C-48 | Total | Delta from V-01 |
|-----------|-----------|------|------|-------|-----------------|
| V-01 | 285 | +5 | +5 | **295** | — |
| V-02 | 285 | 0 | +5 | **290** | −5 |
| V-03 | 285 | +5 | 0 | **290** | −5 |
| V-04 | 285 | +5 | +5 | **295** | 0 |
| V-05 | 285 | 0 | 0 | **285** | −10 |

**Ranking:** V-01 = V-04 (295) > V-02 = V-03 (290) > V-05 (285)

---

### Isolation Audit

| Comparison | Observed delta | Mechanism isolated | Clean? |
|------------|---------------|--------------------|--------|
| V-01 vs V-02 | −5 | C-47 only (labeled sub-entries) | **YES** — V-02 FAIL C-47; PASS C-48 |
| V-01 vs V-03 | −5 | C-48 only (PHASE 1 adversary block) | **YES** — V-03 FAIL C-48; PASS C-47 (2-label compliance) |
| V-01 vs V-04 | 0 | C-49 candidate (not yet rubric criterion) | **YES** — confirms C-49 is a behavioral candidate, not yet scoring |
| V-01 vs V-05 | −10 | C-47+C-48 combined | Combination pass — superadditivity hypothesis |
| V-02 vs V-03 | 0 | C-47 and C-48 orthogonal | **CONFIRMED** — symmetric 5-pt deltas, same composite |

R18 achieves what R16's V-03 failed: a clean single-axis C-48 isolation. The redesign (discrete sub-section removal, vacuous predicate-4 preservation) eliminates the prior C-12/C-20 contamination.

---

### Excellence Signals from Top-Scoring Variations (V-01 / V-04)

**What V-01 and V-04 have that V-02 does not:** Three labeled `PN-ADVERSARY:` sub-entries in the preamble ADVERSARY CHAIN block. Each phase adversary is independently addressable by its phase label without prose scanning. Label count correctly tracks chain length (three when C-48 present).

**What V-01 and V-04 have that V-03 does not:** PHASE 1 execution-body adversary block carrying both `ADVERSARY:` and `DEFEAT CONDITION:` sub-components as a three-part block, extending the execution-body adversary chain from two phases (Phase 2 + Phase 3) to all three principal phases.

**What V-01 has that V-04 does not (not yet a scoring criterion):** Phase 1 STOP CONDITION predicate 4 — "At least one Axis cell explicitly addresses the defeat condition of the Phase 1 adversary" with vacuous-satisfaction clause. This is the C-49 structural candidate: the Phase 1 adversary block (C-48) declares the adversary and defeat condition, but without a STOP CONDITION gate, a model can satisfy all three existing predicates while leaving the Phase 1 adversary undefeated. The predicate-4 gate closes this gap. The vacuous-satisfaction clause correctly decouples C-49 from C-48: when C-48 is absent, the predicate is automatically satisfied (no adversary means no defeat condition to require coverage of).

**Superadditivity candidate (V-05):** Both C-47 and C-48 removed simultaneously yields the floor score (285), exactly equal to the sum of the two individual deficits (5+5=10). Under v16, no interaction effect is observable — V-05's score is the additive sum. Whether behavioral output (axis selection, empty-glob incidence) shows superadditive degradation is the behavioral test that Round 18 is designed to run.

---

### Summary Table

| Variation | Top Criteria Failing | Score | Rank |
|-----------|---------------------|-------|------|
| V-01 | None | 295 | 1 (tie) |
| V-04 | None (C-49 absent, not yet scored) | 295 | 1 (tie) |
| V-02 | C-47 | 290 | 3 (tie) |
| V-03 | C-48 | 290 | 3 (tie) |
| V-05 | C-47, C-48 | 285 | 5 |

All five variations pass all Essential criteria (C-01–C-04). No variation falls below the passing threshold.

---

```json
{"top_score": 295, "all_essential_pass": true, "new_patterns": ["Phase 1 STOP CONDITION defeat-condition coverage gate: fourth predicate requiring at least one Axis cell to address Phase 1 adversary defeat condition, vacuously satisfied when C-48 absent — closes the gap where a model satisfies three STOP predicates while leaving the Phase 1 adversary undefeated"]}
```
