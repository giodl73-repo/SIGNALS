## Quest Score — corps-achievements R4

**Rubric:** v4 (5E + 3R + 10A) | **Variations:** V-01 through V-05

---

## Criterion Evaluation

### ESSENTIAL (5) — gate criteria

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 Grounded scan | PASS | PASS | PASS | PASS | PASS |
| C-02 Every topic in achievements | PASS | PASS | PASS | PASS | PASS |
| C-03 All 3 milestone names | PASS | PASS | PASS | PASS | PASS |
| C-04 Leaderboard present | PASS | PASS | PASS | PASS | PASS |
| C-05 Action names achievement it unlocks | PASS | PASS | PASS | PASS | PASS |

All five variations: 5/5 essential. ✅

---

### RECOMMENDED (3)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 Earned/available separated | PASS | PASS | PASS | PASS | PASS |
| C-07 ≥2 named categories | PASS | PASS | PASS | PASS | PASS |
| C-08 Sprint/date framing | PASS | PASS | PASS | PASS | PASS |

All five variations: 3/3 recommended. ✅

**Notes:**
- C-06: V-02's axis makes EARNED/AVAILABLE the PRIMARY structural split (Steps 2 vs 3), the strongest possible expression of this criterion. V-01/V-03/V-04 use phase-level section headers; V-05 uses 2A/2B numbered sections. All unambiguously pass.
- V-02 milestones are split across Steps 2 and 3 (earned / not-yet) with no single status table — all three names appear across both steps, satisfying C-03 but with weaker single-view clarity.

---

### ASPIRATIONAL (10)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 Dedicated 1-away section | PASS | PASS | PASS | PASS | PASS |
| C-10 Named cross-topic insight, non-stagnation | PASS | PASS | PASS | PASS | PASS |
| C-11 Pre-write self-test gate | PASS | PASS | PASS | PASS | PASS |
| C-12 Anti-inertia → Unlocks → Breaks format | PASS | PASS | PASS | PASS | PASS |
| C-13 TEAM INSIGHT named artifact format | PASS | PASS | PASS | PASS | PASS |
| C-14 Registry syntax + no invented labels | PASS | PASS | PASS | PASS | PASS |
| C-15 Gate failures name specific instance | PASS | PASS | PASS | PASS | PASS |
| C-16 Weighted formula explicit + auditable | PASS | **PARTIAL** | PASS | **PARTIAL** | PASS |
| C-17 Semantic stagnation labels | PASS | PASS | PASS | PASS | PASS |
| C-18 1-away as 4-column table | PASS | PASS | PASS | PASS | PASS |

---

### C-16 Analysis (the differentiator)

C-16 requires "making each contributor's score auditable from raw counts." Three criteria components:
1. Explicit formula present — **all 5 pass**
2. Raw count columns in table — **all 5 pass**
3. Score auditable inline (reader can verify without reconstruction) — **V-01/V-03/V-05 explicitly instruct rank-1 calculation**; V-02/V-04 only state formula and show raw columns

**V-01** Phase 3: *"Show formula calculation for rank-1 contributor to make the scoring auditable: e.g., 'Score = 8×1 + 3×3 + 1×5 = 22.'"* → Explicit instruction generates inline verification. **PASS.**

**V-02** Step 5: *"The formula makes rank auditable from raw counts and encodes the team's priorities."* → Asserts auditability but does not instruct the model to produce the calculation inline. A model following V-02 may output the formula and numbers without the verification step. **PARTIAL.**

**V-03** Section 4: *"I will show the formula and show the calculation for rank-1 so the score is auditable."* + template `Rank-1 calculation: Score = {n}×1 + {n}×3 + {n}×5 = {total}.` → Gate explicitly commits to showing calc. **PASS.**

**V-04** Phase 3: Formula + rationale text + table. No instruction to show rank-1 calculation. Same weakness as V-02: formula is present but inline auditing is not enforced. **PARTIAL.**

**V-05** Section 4: Gate `[C-04/C-16]` + explicit template `Rank-1 calculation: Score = {n}×1 + {n}×3 + {n}×5 = {total}`. **PASS.**

---

### Aspirational Totals

| Variation | Aspirational PASS | Score Contribution |
|-----------|-------------------|--------------------|
| V-01 | 10/10 | +10 |
| V-02 | 9/10 (C-16 PARTIAL) | +9 |
| V-03 | 10/10 | +10 |
| V-04 | 9/10 (C-16 PARTIAL) | +9 |
| V-05 | 10/10 | +10 |

---

## Composite Scores

`score = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/10 × 10)`

| Variation | Essential | Recommended | Aspirational | **Score** | Golden? |
|-----------|-----------|-------------|-------------|-----------|---------|
| **V-01** | 60 | 30 | 10 | **100** | ✅ |
| V-02 | 60 | 30 | 9 | **99** | ✅ |
| **V-03** | 60 | 30 | 10 | **100** | ✅ |
| V-04 | 60 | 30 | 9 | **99** | ✅ |
| **V-05** | 60 | 30 | 10 | **100** | ✅ |

**Golden threshold:** all 5 essential pass AND composite ≥ 80 — all five clear the bar.

---

## Ranking (tie-broken by enforcement density)

Within the three 100-scoring variations, enforcement strength differentiates:

1. **V-05 — 100** | Pre-flight criterion-to-section mapping + criterion-ID-labeled gates + explicit rank-1 calc. Highest enforcement density.
2. **V-03 — 100** | One named gate per aspirational-criterion section (`GATE [C-09/C-18]` format) + explicit rank-1 calc gate. Strongest per-section enforcement.
3. **V-01 — 100** | Solid narrative enforcement, explicit rank-1 calc instruction, Phase 5 registry with Phase 6 anchoring. Clean and complete.
4. **V-04 — 99** | Strongest C-14/C-17 (registry-first preamble before all output); C-16 partial.
5. **V-02 — 99** | Strongest C-06 (EARNED/AVAILABLE as top-level structure); C-16 partial.

---

## Excellence Signals from Top-Scoring Variations

Two patterns appear in V-03/V-05 that are not currently a rubric criterion:

**P-01 — Criterion-ID-labeled gates (V-03, V-05):**
Gates are labeled with the specific criterion IDs they enforce: `**GATE [C-09/C-18]:**`. This makes the connection between enforcement and rubric explicit, enabling criterion-by-criterion tracing. An upgrade to C-11 ("at least one gate") could require gates to name which criteria they enforce.

**P-02 — Pre-flight criterion-to-section mapping table (V-05):**
Before any content generation, a table maps every criterion to its expected section. This meta-enforcement layer makes overall compliance visible at a glance and eliminates the possibility of accidentally skipping a section. Not currently a criterion — candidate for R5 aspirational.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Criterion-ID-labeled gates (GATE [C-09/C-18] format) that trace enforcement to specific rubric criteria rather than generic phase boundaries", "Pre-flight criterion-to-section mapping table before any output generation that makes overall compliance visible and structurally prevents criterion omissions"]}
```
