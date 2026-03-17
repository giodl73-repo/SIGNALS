`simulations/quest/rubrics/quest-variate-rubric-v16-variations-R18-2026-03-15.md` written.

---

## R18 Design Summary

**New structural candidate: C-49 -- Phase 1 STOP CONDITION defeat-condition coverage gate**

V-01's Phase 1 adversary block (C-48) states a DEFEAT CONDITION but nothing in the Phase 1 STOP CONDITION gates on it. C-49 adds a 4th predicate requiring at least one Axis cell to address coverage-boundary behavior. Key design choice: the predicate is **vacuously satisfied when no Phase 1 adversary block is present** -- this cleanly decouples C-49 from C-48, preserving V-03's single-axis isolation.

**Variation map:**

| Variation | C-47 (labeled chain) | C-48 (P1 adversary) | C-49 (STOP pred 4) | Score (v16) |
|-----------|---------------------|---------------------|--------------------|-------------|
| V-01 | 3 labels (P1+P2+P3) | present | present | 295 |
| V-02 | prose only | present | present | 290 |
| V-03 | 2 labels (P2+P3) | absent | present (vacuous) | 290 |
| V-04 | 3 labels (P1+P2+P3) | present | absent (3 preds) | 295 |
| V-05 | prose only | absent | present (vacuous) | 285 |

**V-03 redesign (from R17):** the C-48 ADVERSARY/DEFEAT CONDITION block is now a discrete sub-section positioned AFTER the `*Prevents:*` annotation, ensuring ablation of C-48 cannot touch C-12/C-20. The prior R16 contamination (-10 pts) is eliminated.

**V-01 vs V-04** both score 295 under v16 (C-49 not yet a rubric criterion) -- the behavioral test is whether V-01 generates higher empty-glob axis incidence than V-04 despite both having identical C-48 blocks.
