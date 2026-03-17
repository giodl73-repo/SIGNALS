Written to `simulations/quest/golden/quest-score-variate-R5-v5-2026-03-16.md`.

---

## Round 5 Variations -- Summary

**Rubric**: v5 (C-01--C-18, N_aspirational=10). Two new criteria targeted: C-17 (inertia departure labeling) and C-18 (bilateral symmetry audit sweep).

**New axes this round:**

| Code | Axis | Target | Mechanism |
|------|------|--------|-----------|
| N | Standardized Inertia Labels | C-17 | Required `Inertia: [failure mode]` output field after every structural enforcement mechanism -- upgrades R4's informal M-axis prose to a mandatory labeled field in the scorer's artifact |
| O | Bilateral Symmetry Audit Sweep | C-18 | `Symmetric: YES/NO` table at Phase 1 exit for each comparison in the DELTA REGISTER -- independent catch mechanism analogous to E's YES/NO for arithmetic |
| K+N | Mechanism Index with Departure Labels | C-16, C-17 | Pre-Phase-1 table declaring mechanism / phase / criterion / inertia failure; departure labels planned before execution and reproduced at each mechanism |

**Variations:**

| Variation | Axes | C-17 | C-18 | Purpose |
|-----------|------|------|------|---------|
| V-01 | N only | PASS | FAIL | C-17 PASS / C-18 FAIL baseline |
| V-02 | O only | PARTIAL | PASS | C-18 PASS / C-17-inherited baseline -- tests whether R4 M-axis satisfies C-17 |
| V-03 | N+O | PASS | PASS | Minimum combination for both; tests whether K is additive |
| V-04 | K+N | PASS | FAIL | Mechanism index approach without sweep -- tests whether declaring the sweep satisfies C-18 |
| V-05 | N+O+K | PASS | PASS | Full integration -- expected ceiling candidate |

**Key diagnostic**: V-03 vs V-05 will reveal whether the mechanism index (K) adds ceiling value or is redundant given N+O. If V-03 == V-05, the golden prompt is N+O without K.
