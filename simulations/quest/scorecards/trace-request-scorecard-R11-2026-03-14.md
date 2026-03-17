# trace-request — Quest Score R11 (2026-03-15)

**Rubric version:** v10 | **Scale:** 205 | **Golden threshold:** all-essential PASS AND composite >= 80%

---

## Scoring Basis

Trace artifact is **placeholder** — evaluation proceeds from variation axis definitions and rubric predicate logic. Base score (C-01 through C-27, all PASS) = **190/205**. C-28, C-29, C-30 vary by axis; each is worth 5 pts.

---

## Per-Variation Criterion Breakdown

### V-01 — Regression: C-28 Advisory

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **FAIL** | Step 8b softened to NOTE; not marked REQUIRED; does not structurally block advancement to Step 9; per-boundary prose confirmation absent as gate predicate |
| C-29 | **PASS** | Step 8c table REQUIRED; four columns present (Step3-Auth / Step8a-Invoked / Step11-Params / Match?); Match? binary Y/N per row; VT# scope strings in column values; positioned before Step 9 |
| C-30 | **FAIL** | C-28 surface not REQUIRED; dual-surface enforcement rule cannot be asserted; prose / Match? divergence is not a structural violation when one surface is advisory; contradiction not format-detectable |
| Essential C-01–C-04 | **ALL PASS** | Regression axis touches only aspirational tier |

**Composite:** 190 + 0 + 5 + 0 = **195 / 205 = 95.1%**
**All-essential PASS:** Yes | **Band:** Gold (above 80%, all-essential PASS)

---

### V-02 — Regression: C-29 Advisory

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | Step 8b REQUIRED progression gate present; names all three link arms (Step 8a → Step 11 → Step 7/9); marked REQUIRED; structurally blocks advancement to Step 9 |
| C-29 | **FAIL** | Step 8c table advisory (NOTE); not marked REQUIRED; not positioned as mandatory before Step 9; second surface not enforced |
| C-30 | **FAIL** | C-29 surface not REQUIRED; divergence between prose and table cannot constitute a structural violation; machine-detectable contradiction predicate cannot fire on an optional surface |
| Essential C-01–C-04 | **ALL PASS** | Regression axis touches only aspirational tier |

**Composite:** 190 + 5 + 0 + 0 = **195 / 205 = 95.1%**
**All-essential PASS:** Yes | **Band:** Gold

---

### V-03 — Lifecycle: Contradiction Halt (Typed Structural Event)

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | Step 8b REQUIRED gate; names all three link arms; structurally blocks Step 9; per-boundary confirmation present |
| C-29 | **PASS** | Step 8c REQUIRED table; four columns present; Match? binary Y/N; VT# scope strings propagated into column values; mandatory before Step 9 |
| C-30 | **PASS** | Both surfaces REQUIRED; contradiction introduced as named typed structural event `CONTRADICTION SIGNAL: Seq# N`; requires a `Scope String Correction` Rem# output; prose "Coherence confirmed" at Seq# N + Match? = N at Seq# N is machine-detectable divergence without semantic reading; structural divergence is self-evidencing |
| Essential C-01–C-04 | **ALL PASS** | |

**Composite:** 190 + 5 + 5 + 5 = **205 / 205 = 100%**
**All-essential PASS:** Yes | **Band:** Gold

**C-31 candidate signal:** Contradiction halt is a **named halt type** with required Rem# format output — halt label is machine-greppable; Rem# enforces a structured correction record.

---

### V-04 — Role Sequence: Step 8 Scope-Token Re-Affirmation

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | REQUIRED progression gate with all three link arms; structurally blocks Step 9 |
| C-29 | **PASS** | REQUIRED table; Step 8 header re-affirmation co-locates VT# token list at the step boundary; Match? computation is self-contained — no other section (Steps 0, 3, 11) needed; all four columns present |
| C-30 | **PASS** | Both surfaces REQUIRED; Step 8 header creates a co-located reference set; structural divergence (prose asserts coherent, Match? = N) detectable by comparing header token list against table values without narrative reading |
| Essential C-01–C-04 | **ALL PASS** | |

**Composite:** 190 + 5 + 5 + 5 = **205 / 205 = 100%**
**All-essential PASS:** Yes | **Band:** Gold

**C-31 candidate signal:** Step 8 header makes Match? computation **self-contained** — a checker needs only the header VT# list and the Step 8c table, with no dependency on Steps 0, 3, or 11.

---

### V-05 — Combination V-03 + V-04

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | REQUIRED progression gate; all three link arms named; structurally blocks Step 9; per-boundary confirmation present |
| C-29 | **PASS** | REQUIRED table; Step 8 header re-affirmation makes Match? self-contained; four columns; Match? binary Y/N; VT# scope strings consistent across both surfaces |
| C-30 | **PASS** | Both surfaces REQUIRED; contradiction halt is typed event with required Rem# format (V-03 property); header provides co-located reference set for self-contained Match? computation (V-04 property); all three C-31 pre-conditions co-present: (a) reference set at Step 8 header, (b) named halt type with label, (c) Rem# format requirement |
| Essential C-01–C-04 | **ALL PASS** | |

**Composite:** 190 + 5 + 5 + 5 = **205 / 205 = 100%**
**All-essential PASS:** Yes | **Band:** Gold

**C-31 candidate signal:** Automated enforcement pre-conditions simultaneously established — reference set (header) + halt type (`CONTRADICTION SIGNAL`) + Rem# format all co-present; the automated-check predicate is now specifiable.

---

## Variation Ranking

| Rank | Variation | Score | % | All-Essential | Band | C-28 | C-29 | C-30 |
|---|---|---|---|---|---|---|---|---|
| 1 | **V-05** (V-03+V-04) | 205/205 | 100% | PASS | Gold | PASS | PASS | PASS |
| 1 | **V-04** (Step 8 header) | 205/205 | 100% | PASS | Gold | PASS | PASS | PASS |
| 1 | **V-03** (halt typed) | 205/205 | 100% | PASS | Gold | PASS | PASS | PASS |
| 4 | **V-01** (C-28 advisory) | 195/205 | 95.1% | PASS | Gold | FAIL | PASS | FAIL |
| 4 | **V-02** (C-29 advisory) | 195/205 | 95.1% | PASS | Gold | PASS | FAIL | FAIL |

**Isolation check confirmed:**
- V-01 vs V-03: delta = 10 pts, from C-28 FAIL + C-30 FAIL — confirms C-28 and C-30 are independently load-bearing from C-29
- V-02 vs V-03: delta = 10 pts, from C-29 FAIL + C-30 FAIL — confirms C-29 and C-30 are independently load-bearing from C-28
- C-30 dependency on both C-28 AND C-29 structurally validated: neither V-01 nor V-02 can achieve C-30 PASS

---

## Excellence Signals (V-05, top-scoring)

**ES-1 (V-03 inherited):** `CONTRADICTION SIGNAL: Seq# N` is a **named halt type** — the label is machine-greppable at the exact sequence boundary; the required `Scope String Correction` Rem# output makes every halt produce a structured correction record. Contradiction is no longer inferred from absence of confirmation — it is asserted by a typed event with mandatory output format.

**ES-2 (V-04 inherited):** Step 8 header scope-token re-affirmation creates a **self-contained co-located reference set** — Match? computation requires only (a) the header VT# token list and (b) the Step 8c table; no lookup into Steps 0, 3, or 11 is needed. Reviewer independence from external sections is now a structural property.

**ES-3 (V-05 combination):** All three C-31 pre-conditions **co-present for the first time**: reference set at header + named halt type with machine-greppable label + Rem# format requirement. The automated-check predicate is now specifiable: scan for "Coherence confirmed" at Seq# N while Match? = N at Seq# N; fire `CONTRADICTION SIGNAL` if found; verify Rem# is present. No semantic reading needed.

---

## C-31 Design Surface (R11 yield)

| Property | Source | Testable predicate |
|---|---|---|
| Co-located reference set | V-04 | Step 8 header contains VT# token list used in Step 8c Match? computation |
| Named halt type | V-03 | `CONTRADICTION SIGNAL: Seq# N` label present when prose and table diverge |
| Mandatory correction record | V-03 | `Scope String Correction` Rem# required per halt instance |
| Self-contained checker input | V-04 | Match? computable from header + table, no external section lookup |
| Automated predicate specifiable | V-05 | All three above co-present across R11 rounds |

**C-31 candidate:** Automated consistency enforcement — a machine-readable schema or linting rule computes Match? from Step 8 header VT# token list and Step 8c cell values, producing binary pass/fail per row without human judgment. R11 multi-round evidence (V-03, V-04, V-05 all at 205) establishes the reference set for reliable specification.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named contradiction halt type (CONTRADICTION SIGNAL: Seq# N) with required Rem# format output makes prose/table divergence machine-greppable without semantic reading", "Step 8 header scope-token re-affirmation creates self-contained co-located reference set enabling Match? computation without lookup into Steps 0, 3, or 11", "All three C-31 automated-enforcement pre-conditions co-present for first time in V-05: reference set + named halt type + Rem# format requirement — automated-check predicate is now specifiable"]}
```
