## roles-create R18 Scorecard — Rubric v16

### Criteria Reference Map

The rubric exposes 28 criteria across three tiers. The visible set:

| Tier | IDs | Count |
|------|-----|-------|
| Essential | C-01 – C-05 | 5 |
| Recommended | C-06 – C-07 | 2 |
| Gate/citation cluster | C-29 – C-35 | 7 |
| Other (not shown, assumed PASS all variations) | C-08 – C-28 (excl. gate set) | 14 |
| **Total** | | **28** |

Cascade chain: C-29 → C-30 → C-35 → C-32 → C-34. C-31 → C-33 → C-32 → C-34. C-32 = C-35 ∧ C-31.

---

### V-01: C-30 Alone

**Axis:** Bare FAIL branches (C-29 PASS), annotated PASS branches (C-30 FAIL), thin condition (C-31 PASS).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | File written to `.roles/{area}/{subrole}.md` |
| C-02 | PASS | All required frontmatter fields present |
| C-03 | PASS | Mode detection routes correctly on name-only input |
| C-04 | PASS | Frontmatter content is domain-specific |
| C-05 | PASS | Inertia-advocate surfaced |
| C-06 | PASS | Lens.verify questions sharp and actionable |
| C-07 | PASS | Domain specializations table present |
| C-08–C-28 | PASS | Not in play for this axis |
| C-29 | PASS | FAIL branches carry bare verdict tokens only |
| C-30 | **FAIL** | PASS branches carry affirmation summaries — annotated, not bare |
| C-31 | PASS | Condition is thin CONTRACT-citation form |
| C-35 | **FAIL** | C-29 PASS ∧ C-30 FAIL → bilateral conjunction broken |
| C-32 | **FAIL** | C-35 FAIL → triple purity broken |
| C-33 | PASS | C-31 PASS → no verbose-condition consequence |
| C-34 | **FAIL** | C-32 FAIL, C-33 PASS → C-34 fires |

**Deductions:** C-30, C-35, C-32, C-34 = 4

**Score: 24/28 = 85.71%**

---

### V-02: C-29 Alone

**Axis:** Annotated FAIL branches (C-29 FAIL), bare PASS branches (C-30 PASS independently, FAIL via cascade), thin condition (C-31 PASS).

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
| C-29 | **FAIL** | FAIL branches carry annotation alongside verdict token |
| C-30 | **FAIL** | C-29 FAIL → cascade; PASS branches are bare but C-29's cascade propagates |
| C-31 | PASS | Condition is thin |
| C-35 | **FAIL** | C-29 FAIL → C-30 FAIL (via cascade) → C-35 FAIL |
| C-32 | **FAIL** | C-35 FAIL → C-32 FAIL |
| C-33 | PASS | C-31 PASS → no consequence |
| C-34 | **FAIL** | C-32 FAIL, C-33 PASS → C-34 fires |

**Deductions:** C-29, C-30 (cascade), C-35, C-32, C-34 = 5

**Score: 23/28 = 82.14%**

---

### V-03: C-31 Alone

**Axis:** Bare FAIL branches (C-29 PASS), bare PASS branches (C-30 PASS), verbose condition (C-31 FAIL).

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
| C-29 | PASS | FAIL branches are bare |
| C-30 | PASS | PASS branches are bare |
| C-31 | **FAIL** | Condition is verbose — restates checked predicate |
| C-35 | PASS | C-29 PASS ∧ C-30 PASS → bilateral surface clean despite verbose condition |
| C-32 | **FAIL** | C-35 PASS but C-31 FAIL → triple purity broken |
| C-33 | **FAIL** | C-31 FAIL → C-33 fires |
| C-34 | **FAIL** | C-32 FAIL → C-34 fires |

**Deductions:** C-31, C-32, C-33, C-34 = 4

**Score: 24/28 = 85.71%**

> **C-35 structural note:** V-03 demonstrates that C-35 is strictly weaker than C-32. Verbose condition (C-31 FAIL) breaks C-32 but leaves C-35 intact — the bilateral verdict surface is clean in both directions regardless of condition verbosity. This is the case C-35 was introduced to name.

---

### V-04: C-29 + C-31 (Maximum Pairwise)

**Axis:** Verbose condition (C-31 FAIL), annotated FAIL branches (C-29 FAIL), bare PASS branches (C-30 PASS independently — C-30 cascades from C-29 only, not from its own annotation).

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
| C-29 | **FAIL** | Annotated FAIL branches |
| C-30 | **FAIL** | C-29 FAIL → cascade; PASS branches are bare (C-30 fails via cascade path only) |
| C-31 | **FAIL** | Verbose condition |
| C-35 | **FAIL** | C-29 FAIL → C-30 FAIL → C-35 FAIL |
| C-32 | **FAIL** | C-35 FAIL ∧ C-31 FAIL → triple purity broken from both paths |
| C-33 | **FAIL** | C-31 FAIL → C-33 fires |
| C-34 | **FAIL** | C-32 FAIL → C-34 fires |

**Deductions:** C-29, C-30 (cascade), C-31, C-35, C-32, C-33, C-34 = 7

**Score: 21/28 = 75.00%**

> **Maximum pairwise confirmation:** C-29 and C-31 are structurally orthogonal failure paths that both converge on C-32 and C-34. C-29 exhausts the cascade chain (→ C-30 → C-35 → C-32 → C-34); C-31 exhausts its own chain (→ C-33 → C-32 → C-34). Seven distinct criteria fail — the highest non-ceiling deduction count under v16. Primary R18 open question answered: yes, exactly 7.

---

### V-05: Full Ceiling

**Axis:** Thin condition (C-31 PASS), bare FAIL branches (C-29 PASS), bare PASS branches (C-30 PASS). All criteria pass.

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
| C-29 | PASS | Bare FAIL branches |
| C-30 | PASS | Bare PASS branches |
| C-31 | PASS | Thin condition |
| C-35 | PASS | C-29 PASS ∧ C-30 PASS |
| C-32 | PASS | C-35 PASS ∧ C-31 PASS |
| C-33 | PASS | C-31 PASS |
| C-34 | PASS | C-32 PASS |

**Deductions:** 0

**Score: 28/28 = 100.00%**

---

### Rankings

| Rank | Variation | Axis | Score | Δ from ceiling |
|------|-----------|------|-------|----------------|
| 1 | **V-05** | Full ceiling | 28/28 | — |
| 2T | **V-01** | C-30 alone | 24/28 | −4 |
| 2T | **V-03** | C-31 alone | 24/28 | −4 |
| 4 | **V-02** | C-29 alone | 23/28 | −5 |
| 5 | **V-04** | C-29 + C-31 | 21/28 | −7 |

---

### Deduction Depth Table (v16 Complete — R18 Confirmation)

| Axis | Primary failures | Cascade / conjunction | Total | Score |
|------|------------------|-----------------------|-------|-------|
| C-30 alone | C-30 | C-35, C-32, C-34 | 4 | 24/28 |
| C-31 alone | C-31 | C-32, C-33, C-34 | 4 | 24/28 |
| C-29 alone | C-29 | C-30, C-35, C-32, C-34 | 5 | 23/28 |
| C-30 + C-31 | C-30, C-31 | C-35, C-32, C-33, C-34 | 6 | 22/28 |
| **C-29 + C-31** | **C-29, C-31** | **C-30, C-35, C-32, C-33, C-34** | **7** | **21/28** |

All four open questions from R18 confirmed.

---

### Excellence Signals from V-05

1. **Bilateral verdict surface purity:** Keeping both FAIL and PASS branches as bare tokens (no affirmation summaries, no annotation) satisfies C-29 ∧ C-30 simultaneously, unlocking C-35 as a prerequisite for C-32.

2. **Condition leanness:** A thin CONTRACT-citation form condition (C-31 PASS) avoids the verbose-condition cascade (→ C-33 → C-32 → C-34), eliminating 3 downstream failures from a single authoring decision.

3. **Cascade insulation:** When C-29 and C-30 both pass, C-35 is insulated from C-31's fate — demonstrating that verdict surface purity and condition verbosity are orthogonal axes with no cross-contamination.

4. **V-03 structural proof:** V-03's C-35 PASS (verbose condition but bare verdict branches) isolates condition verbosity as a C-32-breaking mechanism that does not affect the bilateral verdict surface — a pattern only nameable with C-35 in the rubric.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-29+C-31 confirmed as 7-deduction maximum pairwise under v16 — the two cascade chains are structurally orthogonal and converge on C-32 and C-34 without redundancy", "V-01 and V-03 tie at 24/28: C-30-alone and C-31-alone both cost exactly 4 deductions, but via different cascade paths — C-35 equalizes what v15 separated", "C-35 passes when C-31 fails (V-03): bilateral verdict surface purity is independent of condition verbosity, confirming C-35 is a strict prerequisite for C-32 with non-empty pass space"]}
```
