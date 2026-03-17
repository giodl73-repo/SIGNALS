Written to `simulations/quest/golden/campaign-decide-variate-R2-2026-03-16.md`.

---

## R2 Variation Summary

**R1 diagnosis driving axis choices:** V-02 won at 100 by using per-phase table schemas (C-11) and `because Phase N, [section]` syntax (C-12). V-01 hit 60 despite passing all essentials because both aspirational criteria were absent. R2 targets C-11 and C-12 directly in every variation.

| ID | Axis | C-11 mechanism | C-12 mechanism | Key hypothesis |
|----|------|----------------|----------------|----------------|
| **V-01** | Per-phase named-field schema | Required labeled fields per phase | `Because Phase N, field` in Phase 6 | Named fields are more rendering-robust than tables |
| **V-02** | Role sequence (hypothesis-first) | Table per phase (V-02 R1 pattern) | `because Phase N, [row]` | Hypothesis-first improves C-08 — evidence tests a prior, not post-hoc confirms |
| **V-03** | Citation anchor (finding-ID) | FID-prefixed rows per phase | `because FID` prescribed format | FID citations are more precise than Phase+section — pin to a specific row |
| **V-04** | Named fields + finding-IDs | FID-labeled named fields per phase | `because FID` min 4 citations | Combines rendering robustness with maximum citation precision |
| **V-05** | Hypothesis-first + V-02 R1 tables | Complete table schema per phase | Exact V-02 R1 syntax preserved | Best-of synthesis — V-02's proven 100-score structure + anchor ordering |

**Predicted leaderboard**: V-05 >= V-02 > V-01 > V-04 >= V-03.

- V-05 preserves V-02's proven formula while adding hypothesis-anchor depth
- V-03 and V-04 share a C-12 risk: the rubric example is `Phase N, section` — FID format satisfies the spirit (mechanically auditable) but differs in syntax; scorer interpretation determines pass/fail
