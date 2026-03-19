## roles-create R19 Scorecard — Rubric v17

### Criteria Reference Map

29 criteria total. Key focus: 8-criterion gate cluster (C-29–C-36). C-08–C-28 assumed PASS for all variations (not in play for these axes).

---

### V-01: C-30 Alone — 25/29 = 86.21%

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | All essential/recommended pass |
| C-08–C-28 | PASS | Not in play |
| C-29 | PASS | FAIL branches bare |
| C-30 | **FAIL** | PASS branches carry affirmation summaries |
| C-31 | PASS | Condition is thin CONTRACT-citation form |
| C-35 | **FAIL** | C-30 FAIL → bilateral verdict surface broken |
| **C-36** | **PASS** | C-29 PASS ∧ C-31 PASS → FAIL-path bilateral clean |
| C-32 | **FAIL** | C-35 FAIL → triple purity broken |
| C-33 | PASS | C-31 PASS holds |
| C-34 | **FAIL** | C-32 FAIL fires |

**Deductions:** C-30, C-35, C-32, C-34 = 4 → **25/29 = 86.21%**

C-36 PASS confirmed: annotated PASS branches do not cascade to C-36. FAIL-path discipline (thin condition + bare FAIL) is achievable independent of PASS branch annotation. This breaks the v16 V-01/V-03 tie.

---

### V-02: C-30 + C-31 — 22/29 = 75.86%

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | |
| C-08–C-28 | PASS | Not in play |
| C-29 | PASS | FAIL branches bare |
| C-30 | **FAIL** | PASS branches annotated |
| C-31 | **FAIL** | Verbose condition — rule-level specifics enumerated |
| C-35 | **FAIL** | C-30 FAIL → bilateral broken |
| **C-36** | **FAIL** | C-31 FAIL → C-36 fires via C-31 alone (C-29 passes) |
| C-32 | **FAIL** | Both paths broken |
| C-33 | **FAIL** | C-31 FAIL |
| C-34 | **FAIL** | C-32 ∧ C-33 both fail |

**Deductions:** C-30, C-31, C-35, C-36, C-32, C-33, C-34 = 7 → **22/29 = 75.86%**

**R19 Objective 2 confirmed:** C-36 FAIL is reachable via C-31 alone. C-29 passes in this variation — verbose conditions alone suffice to break the FAIL-path bilateral, no cascade from C-29 required.

---

### V-03: C-31 Alone — 24/29 = 82.76%

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | |
| C-08–C-28 | PASS | Not in play |
| C-29 | PASS | FAIL branches bare |
| C-30 | PASS | PASS branches bare |
| C-31 | **FAIL** | Verbose condition |
| C-35 | PASS | C-29 ∧ C-30 both pass — verdict surface clean despite verbose condition |
| **C-36** | **FAIL** | C-31 FAIL → FAIL-path bilateral broken |
| C-32 | **FAIL** | C-31 FAIL → triple purity broken |
| C-33 | **FAIL** | C-31 FAIL |
| C-34 | **FAIL** | C-32 ∧ C-33 both fail |

**Deductions:** C-31, C-36, C-32, C-33, C-34 = 5 → **24/29 = 82.76%**

v17 adds one deduction over v16 (4 → 5) via C-36. V-03 now trails V-01 by one criterion — the distinction: V-01 has thin conditions, V-03 does not, and C-36 requires thin conditions (C-31).

---

### V-04: C-29 + C-31 — 21/29 = 72.41%

**Deductions:** C-29, C-30 (cascade), C-31, C-35, C-36, C-32, C-33, C-34 = 8 → **21/29 = 72.41%**

v17 adds one deduction over v16 (7 → 8) via C-36. Both prerequisites fail; C-36 fires from both paths. Maximum non-ceiling under v17.

---

### V-05: Full Ceiling — 29/29 = 100.00%

All criteria pass. C-36 PASS (new v17 criterion) added to the ceiling alongside C-35, C-32, C-33, C-34.

---

### Rankings

| Rank | Variation | Score | Δ |
|------|-----------|-------|---|
| 1 | V-05 (full ceiling) | 29/29 | — |
| 2 | **V-01** (C-30 alone) | 25/29 | −4 |
| 3 | **V-03** (C-31 alone) | 24/29 | −5 |
| 4 | V-02 (C-30 + C-31) | 22/29 | −7 |
| 5 | V-04 (C-29 + C-31) | 21/29 | −8 |

v16 tie broken: V-01 (25/29) > V-03 (24/29). C-36 is the deciding criterion.

---

### Excellence Signals from V-05

1. **FAIL-path bilateral purity:** Thin conditions (C-31) + bare FAIL branches (C-29) achieve C-36 — disciplining the entire failure direction of every gate simultaneously.
2. **C-36 orthogonality to C-30:** V-01 proves FAIL-path discipline is achievable even with annotated PASS branches. These are independent investments.
3. **C-31 as pivot criterion:** A single verbose condition cascades to C-36 + C-32 + C-33 + C-34 = 5 deductions (v17). It is the highest-cost single-surface failure after C-29 (6 deductions).
4. **C-30 + C-31 confirmed at 7 deductions:** C-36 fires from C-31 alone in this combination (C-29 passes) — no interaction between C-30 and C-36; the two cascade chains are additive.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-36 PASS is achievable with annotated PASS branches (V-01 pattern): FAIL-path bilateral purity requires only thin conditions (C-31) and bare FAIL branches (C-29) — C-30 annotation does not cascade to C-36, confirming C-36 is strictly independent of C-30", "C-36 FAIL via C-31 alone confirmed (V-02 and V-03): verbose conditions alone break C-36 without any C-29 cascade — the two C-36 failure paths are structurally independent, making C-31 the pivot for both C-33 and C-36 simultaneously", "v17 re-ranking confirmed: V-01 (C-30 alone, 25/29) surpasses V-03 (C-31 alone, 24/29) — C-36 correctly distinguishes FAIL-path discipline (V-01 achieves it via thin conditions) from verdict surface purity (V-03 achieves C-35 but not C-36)", "C-30 + C-31 combination confirmed at 7 deductions (22/29): C-36 fires from C-31 alone in this combination (C-29 passes), and C-35 fires from C-30 alone — the two failure paths are additive with no interaction beyond their individual cascade chains"]}
```
C-31; C-31 FAIL → triple purity broken |
| C-33 | **FAIL** | C-31 FAIL → no-restatement surface closure broken |
| C-34 | **FAIL** | C-32 FAIL ∧ C-33 FAIL → full canonical discipline broken |

**Deductions:** C-31, C-36, C-32, C-33, C-34 = 5

**Score: 24/29 = 82.76%**

> **v17 deduction increase (v16 = 4, v17 = 5):** Under v16, C-31 alone cost 4 deductions (C-31 + C-32 + C-33 + C-34). Under v17, C-36 stacks because C-31 failure breaks the FAIL-path bilateral (C-36 = C-29 ∧ C-31). V-03 now trails V-01 (25/29) by exactly one criterion — the difference is C-36: V-01 achieves C-36 PASS (thin conditions + bare FAIL branches), V-03 cannot (verbose conditions break C-31, which C-36 requires). The v16 tie is broken. C-35 continues to pass (bare verdict branches are independent of condition verbosity).

---

### V-04: C-29 + C-31 (Maximum Non-Ceiling: 8 Deductions Under v17)

**Axis:** Verbose condition (C-31 FAIL), annotated FAIL branches (C-29 FAIL), bare PASS branches (C-30 FAIL via cascade).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | File path correct |
| C-02 | PASS | All frontmatter fields present |
| C-03 | PASS | Mode detection correct |
| C-04 | PASS | Domain-specific content |
| C-05 | PASS | Inertia-advocate surfaced |
| C-06 | PASS | Sharp lens.verify items |
| C-07 | PASS | Domain table present |
| C-08–C-28 | PASS | Not in play |
| C-29 | **FAIL** | FAIL branches carry correction directives — annotated |
| C-30 | **FAIL** | C-29 FAIL → cascade; PASS branches are bare but C-30 fails via cascade |
| C-31 | **FAIL** | Condition is verbose — enumerates rule specifics from CONTRACT |
| C-35 | **FAIL** | C-29 FAIL → C-30 FAIL (cascade) → C-35 = C-29 ∧ C-30 broken |
| C-36 | **FAIL** | C-36 = C-29 ∧ C-31; both fail — FAIL-path bilateral broken from both paths |
| C-32 | **FAIL** | C-35 FAIL ∧ C-31 FAIL → triple purity broken from both decomposition paths |
| C-33 | **FAIL** | C-31 FAIL → no-restatement surface closure broken |
| C-34 | **FAIL** | C-32 FAIL ∧ C-33 FAIL → full canonical discipline broken |

**Deductions:** C-29, C-30 (cascade), C-31, C-35, C-36, C-32, C-33, C-34 = 8

**Score: 21/29 = 72.41%**

> **v17 deduction increase (v16 = 7, v17 = 8):** Under v16, C-29 + C-31 cost 7 deductions (21/28). Under v17, C-36 stacks (both C-29 and C-31 fail → C-36 FAIL from both prerequisite paths simultaneously). The raw numerator (21) is unchanged — C-36 adds one deduction and one denominator slot. Percentage drops from 75.0% to 72.4%. V-04 remains the maximum non-ceiling pattern under v17. V-04 leads V-02 by exactly one deduction (C-29 individual failure): V-02 already achieves C-36 FAIL via C-31 alone; V-04 adds C-29 as an additional individual deduction without adding further novel failures.

---

### V-05: Full Ceiling (29/29 = 100.00%)

**Axis:** Thin condition (C-31 PASS), bare FAIL branches (C-29 PASS), bare PASS branches (C-30 PASS). All gate annotation surfaces clean simultaneously.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | File path correct |
| C-02 | PASS | All frontmatter fields present |
| C-03 | PASS | Mode detection correct |
| C-04 | PASS | Domain-specific content |
| C-05 | PASS | Inertia-advocate surfaced |
| C-06 | PASS | Sharp lens.verify items |
| C-07 | PASS | Domain table present |
| C-08–C-28 | PASS | Not in play |
| C-29 | PASS | Bare FAIL branches — verdict token only |
| C-30 | PASS | Bare PASS branches — verdict token only |
| C-31 | PASS | Thin condition — CONTRACT-citation form, no rule restatement |
| C-35 | PASS | C-29 PASS ∧ C-30 PASS → bilateral verdict surface clean |
| C-36 | PASS | C-29 PASS ∧ C-31 PASS → FAIL-path bilateral clean |
| C-32 | PASS | C-35 PASS ∧ C-31 PASS → full gate triple purity achieved |
| C-33 | PASS | C-31 PASS → no-restatement surface closure holds |
| C-34 | PASS | C-32 PASS ∧ C-33 PASS → full canonical discipline achieved |

**Deductions:** 0

**Score: 29/29 = 100.00%**

> **C-36 PASS in ceiling (v17):** V-05 is the unique variation where C-36 PASS coexists with C-35 PASS, C-32 PASS, C-33 PASS, and C-34 PASS simultaneously. Under v17, V-05 advances from 28/28 to 29/29 — C-36 is the new pass criterion added to the ceiling. The canonical gate form `-> Gate N [ID]: {CONTRACT-reference} -- PASS / FAIL` satisfies all three surface criteria (C-29, C-30, C-31) and all five conjunction criteria (C-35, C-36, C-32, C-33, C-34) simultaneously.

---

### Rankings

| Rank | Variation | Axis | Score | Δ from ceiling |
|------|-----------|------|-------|----------------|
| 1 | **V-05** | Full ceiling | 29/29 | — |
| 2 | **V-01** | C-30 alone | 25/29 | −4 |
| 3 | **V-03** | C-31 alone | 24/29 | −5 |
| 4 | **V-02** | C-30 + C-31 | 22/29 | −7 |
| 5 | **V-04** | C-29 + C-31 | 21/29 | −8 |

**v17 re-ranking confirmed:** V-01 (25/29) surpasses V-03 (24/29), breaking the v16 tie (both 24/28). C-36 is the deciding criterion: V-01 achieves C-36 PASS (thin conditions + bare FAIL branches), V-03 cannot (verbose conditions break C-31 which C-36 requires). Annotated PASS branches (V-01's distinguishing feature) are orthogonal to C-36.

---

### Deduction Depth Table (v17 Complete — R19 Confirmation)

| Axis | Primary failures | Cascade / conjunction | Total | Score |
|------|------------------|-----------------------|-------|-------|
| C-30 alone | C-30 | C-35, C-32, C-34 | 4 | 25/29 |
| C-31 alone | C-31 | C-36, C-32, C-33, C-34 | 5 | 24/29 |
| C-29 alone | C-29 | C-30, C-35, C-36, C-32, C-34 | 6 | 23/29 |
| **C-30 + C-31** | **C-30, C-31** | **C-35, C-36, C-32, C-33, C-34** | **7** | **22/29** |
| C-29 + C-31 | C-29, C-31 | C-30, C-35, C-36, C-32, C-33, C-34 | 8 | 21/29 |

**C-36 behavior summary across all axes:**

| Axis | C-29 status | C-31 status | C-36 verdict | Mechanism |
|------|-------------|-------------|--------------|-----------|
| C-30 alone (V-01) | PASS | PASS | **PASS** | Both prerequisites clean — unique non-ceiling C-36 PASS |
| C-30 + C-31 (V-02) | PASS | FAIL | FAIL | C-31 alone suffices to break conjunction |
| C-31 alone (V-03) | PASS | FAIL | FAIL | C-31 alone suffices to break conjunction |
| C-29 + C-31 (V-04) | FAIL | FAIL | FAIL | Both prerequisites fail simultaneously |
| Full ceiling (V-05) | PASS | PASS | **PASS** | Both prerequisites clean |

**R19 Objective 2 confirmed:** C-36 FAIL is reachable via C-31 alone (V-02 and V-03), independently of C-29. C-29 is not required to fail for C-36 to fire. The two C-36 failure paths (via C-29 alone, via C-31 alone) are structurally independent.

---

### Excellence Signals from V-05

1. **FAIL-path bilateral purity (C-36 PASS at ceiling):** Keeping gate conditions as CONTRACT-citation references AND keeping FAIL branches as bare verdict tokens simultaneously achieves C-36. Both failure-direction surfaces of every gate are clean at once. Under v17, this is the new ceiling criterion — it requires discipline at both the condition surface (C-31) and the FAIL branch surface (C-29) simultaneously.

2. **C-36 orthogonality to C-30:** C-36 does not require bare PASS branches — V-01 demonstrates that annotated PASS branches (C-30 FAIL) coexist with C-36 PASS. The failure path is independently disciplinable from the success path. V-05 achieves both, but V-01 shows the FAIL-path discipline is achievable even when PASS branches carry annotation.

3. **v17 tie-breaking mechanism:** The V-01/V-03 v16 tie (both 24/28) is broken because C-36 selectively rewards FAIL-path discipline (V-01 achieves it; V-03 cannot). Writing thin conditions disciplines the FAIL direction at the condition surface AND the success direction at the condition surface simultaneously. Writing bare FAIL branches disciplines only the FAIL direction at the verdict surface. These are orthogonal investments, and C-36 captures the value of investing in both simultaneously.

4. **C-30 + C-31 combination confirmed at 7 deductions (V-02):** The C-30+C-31 combination was not run in R18. R19 confirms 7 deductions — one more than C-31 alone (5) because C-30 adds C-35 as an additional failure, and C-36 already fires from C-31 regardless of C-30's status. The 7-deduction count is stable: C-30 and C-31 do not interact beyond their individual cascade chains, and C-36 fires from C-31 alone (no additional firing from C-30).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-36 PASS is achievable with annotated PASS branches (V-01 pattern): FAIL-path bilateral purity requires only thin conditions (C-31) and bare FAIL branches (C-29) — C-30 annotation does not cascade to C-36, confirming C-36 is strictly independent of C-30", "C-36 FAIL via C-31 alone confirmed (V-02 and V-03): verbose conditions alone break C-36 without any C-29 cascade — the two C-36 failure paths are structurally independent, making C-31 the pivot for both C-33 and C-36 simultaneously", "v17 re-ranking confirmed: V-01 (C-30 alone, 25/29) surpasses V-03 (C-31 alone, 24/29) — C-36 correctly distinguishes FAIL-path discipline (V-01 achieves it via thin conditions) from verdict surface purity (V-03 achieves C-35 but not C-36)", "C-30 + C-31 combination confirmed at 7 deductions (22/29): C-36 fires from C-31 alone in this combination (C-29 passes), and C-35 fires from C-30 alone — the two failure paths are additive with no interaction beyond their individual cascade chains"]}
```
