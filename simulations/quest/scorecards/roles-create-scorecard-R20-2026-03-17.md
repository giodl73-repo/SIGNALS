## roles-create R20 Scorecard -- Rubric v18

### Criteria Reference Map

30 criteria total. Key focus: 9-criterion gate cluster (C-29--C-37). C-08--C-28 PASS for all variations (not in play). C-37 = C-35 ^ C-36 = bilateral purity closure, new in v18.

---

### V-01: C-30 Alone (C-37 FAIL via C-35 Path) -- 25/30 = 83.33%

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-07 | PASS | All essential/recommended pass |
| C-08--C-28 | PASS | Not in play |
| C-29 | PASS | FAIL branches bare |
| C-30 | **FAIL** | PASS branches carry affirmation summaries |
| C-31 | PASS | Condition form is thin CONTRACT-citation |
| C-35 | **FAIL** | C-29 PASS ^ C-30 FAIL = FAIL |
| C-36 | PASS | C-29 PASS ^ C-31 PASS = PASS |
| C-37 | **FAIL** | C-35 FAIL ^ C-36 PASS = FAIL -- C-35 path sufficient alone |
| C-32 | **FAIL** | Triple purity broken |
| C-33 | PASS | C-31 PASS holds |
| C-34 | **FAIL** | C-32 FAIL fires |

**Deductions: 5 -- 25/30 = 83.33%** (was 25/29 = 86.21%)

---

### V-02: C-31 Alone (C-37 FAIL via C-36 Path) -- 24/30 = 80.00%

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-28 | PASS | Not in play |
| C-29 | PASS | FAIL branches bare |
| C-30 | PASS | PASS branches bare |
| C-31 | **FAIL** | Verbose conditions enumerate CONTRACT specifics |
| C-35 | PASS | C-29 PASS ^ C-30 PASS = PASS |
| C-36 | **FAIL** | C-29 PASS ^ C-31 FAIL = FAIL -- C-36 path sufficient alone |
| C-37 | **FAIL** | C-35 PASS ^ C-36 FAIL = FAIL |
| C-32 | **FAIL** | Triple purity broken |
| C-33 | **FAIL** | C-31 FAIL |
| C-34 | **FAIL** | C-32 FAIL fires |

**Deductions: 6 -- 24/30 = 80.00%** (was 24/29 = 82.76%)

---

### V-03: C-30 + C-31 -- 22/30 = 73.33%

Deductions: C-30, C-31, C-35, C-36, C-37, C-32, C-33, C-34 = 8. C-37 single-deduction rule confirmed: one deduction even with both prerequisite paths broken.

---

### V-04: C-29 + C-31 (Maximum Non-Ceiling) -- 21/30 = 70.00%

Deductions: C-29, C-30 (cascade), C-31, C-35, C-36, C-37, C-32, C-33, C-34 = 9. Maximum non-ceiling under v18 confirmed.

---

### V-05: Full Ceiling -- 30/30 = 100.00%

All C-29--C-37 PASS. Thin conditions + bare FAIL + bare PASS simultaneously: the sole path to C-37 PASS (bilateral purity closure).

---

### Rankings

| Rank | Variation | Score | Delta |
|------|-----------|-------|-------|
| 1 | V-05 | 30/30 = 100.00% | -- |
| 2 | V-01 | 25/30 = 83.33% | -5 |
| 3 | V-02 | 24/30 = 80.00% | -6 |
| 4 | V-03 | 22/30 = 73.33% | -8 |
| 5 | V-04 | 21/30 = 70.00% | -9 |

v17 rankings preserved. All non-ceiling gaps widen by exactly 1 under v18.

---

### Excellence Signals (V-05)

**E-01 -- Gate annotation triple-surface simultaneous purity.** C-37 PASS requires all three surfaces clean at once (C-29, C-30, C-31). No partial combination suffices -- V-01 and V-02 confirm each partial surface failure independently breaks C-37.

**E-02 -- C-37 single-deduction structure.** Confirmed from both directions: V-05 earns one PASS point; V-03 and V-04 each lose exactly one point regardless of how many prerequisite paths fail.

**E-03 -- Path isolation confirmed by adjacent pairing.** V-01 (C-35 path) and V-02 (C-36 path) positioned consecutively confirm the bilateral paths are structurally independent -- each sufficient alone to break C-37 without the other participating.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Gate annotation triple-surface simultaneous purity is the sole path to bilateral purity closure (C-37) -- all three surfaces (condition form C-31, FAIL branch C-29, PASS branch C-30) must be simultaneously clean; no partial combination achieves C-37 PASS", "C-37 single-deduction rule confirmed across all non-ceiling variations -- bilateral purity closure contributes exactly one deduction regardless of whether one or both prerequisite paths (C-35 via C-30, C-36 via C-31) are broken", "Adjacent variation pairing for bilateral path isolation -- V-01 (C-35 path, C-30 alone) and V-02 (C-36 path, C-31 alone) positioned consecutively confirm C-37 fails independently via each prerequisite path without the other participating"]}
```
 prerequisite paths fail (C-35 FAIL and C-36 FAIL simultaneously). C-37 is a conjunction criterion; it does not double-count when both conjuncts are broken. Under v17: 22/29 = 75.86%; under v18: 22/30 = 73.33%.

---

### V-04: C-29 + C-31 (Maximum Non-Ceiling -- 9 Deductions) -- 21/30 = 70.00%

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-07 | PASS | All essential/recommended pass |
| C-08--C-28 | PASS | Not in play |
| C-29 | **FAIL** | FAIL branches carry correction directives (`/ FAIL: [correction]`) |
| C-30 | **FAIL** | C-29 FAIL cascades to C-30 FAIL |
| C-31 | **FAIL** | Conditions enumerate rule-level specifics (verbose form) |
| C-35 | **FAIL** | C-29 FAIL ^ C-30 FAIL = FAIL |
| C-36 | **FAIL** | C-29 FAIL ^ C-31 FAIL = FAIL |
| C-37 | **FAIL** | C-35 FAIL ^ C-36 FAIL = FAIL -- one deduction despite both prerequisite paths broken |
| C-32 | **FAIL** | C-29 FAIL ^ C-30 FAIL ^ C-31 FAIL = FAIL |
| C-33 | **FAIL** | C-31 FAIL -- no-restatement surface closure broken |
| C-34 | **FAIL** | C-32 FAIL fires |

**Deductions:** C-29, C-30 (cascade), C-31, C-35, C-36, C-37, C-32, C-33, C-34 = 9 -- **21/30 = 70.00%**

Maximum non-ceiling under v18: no variation outside the full ceiling exceeds 9 deductions. C-37 adds exactly one deduction here as well, confirming the single-deduction rule under maximum non-ceiling conditions. Under v17: 21/29 = 72.41%; under v18: 21/30 = 70.00%.

---

### V-05: Full Ceiling (C-37 PASS) -- 30/30 = 100.00%

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-07 | PASS | All essential/recommended pass |
| C-08--C-28 | PASS | Not in play |
| C-29 | PASS | FAIL branches bare (`/ FAIL`) |
| C-30 | PASS | PASS branches bare (`PASS /`) |
| C-31 | PASS | Conditions are thin CONTRACT-citation form |
| C-35 | PASS | C-29 PASS ^ C-30 PASS = PASS -- verdict-surface bilateral clean |
| C-36 | PASS | C-29 PASS ^ C-31 PASS = PASS -- FAIL-path bilateral clean |
| C-37 | PASS | C-35 PASS ^ C-36 PASS = PASS -- bilateral purity closure achieved |
| C-32 | PASS | C-29 PASS ^ C-30 PASS ^ C-31 PASS = PASS -- triple purity achieved |
| C-33 | PASS | C-31 PASS -- no-restatement surface closure intact |
| C-34 | PASS | C-32 PASS -- canonical discipline holds |

**Deductions:** 0 -- **30/30 = 100.00%**

C-37 v18 ceiling confirmed: V-05 is the unique variation where C-37 PASS coexists with C-35 PASS, C-36 PASS, C-32 PASS, C-33 PASS, and C-34 PASS simultaneously. The canonical gate form `-> Gate N [ID]: {CONTRACT-citation} -- PASS / FAIL` satisfies all three annotation surfaces (C-29, C-30, C-31) and all six conjunction criteria (C-35, C-36, C-37, C-32, C-33, C-34). Under v17: 29/29 = 100%; under v18: 30/30 = 100% -- C-37 is the new PASS criterion added to the ceiling.

---

### Rankings

| Rank | Variation | Axis | Score | Delta |
|------|-----------|------|-------|-------|
| 1 | V-05 | Full ceiling | 30/30 = 100.00% | -- |
| 2 | V-01 | C-30 alone | 25/30 = 83.33% | -5 |
| 3 | V-02 | C-31 alone | 24/30 = 80.00% | -6 |
| 4 | V-03 | C-30 + C-31 | 22/30 = 73.33% | -8 |
| 5 | V-04 | C-29 + C-31 | 21/30 = 70.00% | -9 |

v17 rankings preserved. V-01 > V-02 gap: 1 criterion (25 vs 24). Both gained exactly one C-37 deduction under v18 -- the gap is unchanged. All non-ceiling distances from ceiling widened by exactly 1 under v18.

---

### Excellence Signals (V-05)

**E-01 -- Gate annotation triple-surface simultaneous purity.** V-05 achieves C-37 PASS by satisfying all three annotation surfaces at once: thin condition (C-31 PASS), bare FAIL (C-29 PASS), bare PASS (C-30 PASS). C-37 PASS is only achievable by this simultaneous triple-surface purity -- no partial combination suffices. This is the sole gate format that clears the bilateral purity closure.

**E-02 -- Single-deduction rule at ceiling.** C-37 contributes exactly one criterion slot to the denominator regardless of how many prerequisite paths pass or fail. V-05 earns the C-37 PASS point by satisfying both prerequisites simultaneously -- not by a path shortcut. The ceiling requires all prerequisites clean; the single deduction at failure confirms the same single-slot structure from both directions.

**E-03 -- C-35/C-36 path independence resolved at the ceiling.** V-01 and V-02 confirm that each path (C-35 via C-30; C-36 via C-31) independently breaks C-37. V-05 confirms that clearing both paths simultaneously is the only way to restore C-37 PASS. The ceiling is not path-selective: it requires C-29 ^ C-30 ^ C-31 simultaneously.

---

### v18 Deduction Table (Confirmed)

| Axis | Direct | Cascade | Total | Score |
|------|--------|---------|-------|-------|
| C-30 alone | C-30 | C-35, C-37, C-32, C-34 | 5 | 25/30 = 83.33% |
| C-31 alone | C-31 | C-36, C-37, C-32, C-33, C-34 | 6 | 24/30 = 80.00% |
| C-30 + C-31 | C-30, C-31 | C-35, C-36, C-37, C-32, C-33, C-34 | 8 | 22/30 = 73.33% |
| C-29 + C-31 | C-29, C-31 | C-30 (cascade), C-35, C-36, C-37, C-32, C-33, C-34 | 9 | 21/30 = 70.00% |
| Full ceiling | -- | -- | 0 | 30/30 = 100.00% |

All v18 hypotheses confirmed. C-37 single-deduction rule holds across all non-ceiling variations regardless of whether one or both prerequisite paths are broken.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Gate annotation triple-surface simultaneous purity is the sole path to bilateral purity closure (C-37) -- all three surfaces (condition form C-31, FAIL branch C-29, PASS branch C-30) must be simultaneously clean; no partial combination achieves C-37 PASS", "C-37 single-deduction rule confirmed across all non-ceiling variations -- bilateral purity closure contributes exactly one deduction regardless of whether one or both prerequisite paths (C-35 via C-30, C-36 via C-31) are broken", "Adjacent variation pairing for bilateral path isolation -- V-01 (C-35 path, C-30 alone) and V-02 (C-36 path, C-31 alone) positioned consecutively confirm C-37 fails independently via each prerequisite path without the other participating"]}
```
