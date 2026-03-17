Written to `simulations/quest/rubrics/discover-feasibility-alt-rubric-v10-2026-03-17.md`.

**What changed (v9 -> v10):**

| ID | Criterion | Source Pattern |
|----|-----------|----------------|
| C-28 | STRATEGY precedes ARCHITECT — structural guarantee | role-inversion-as-structural-guarantee |
| C-29 | Ordering constraints carry explicit causal rationale | dependency-rationale-over-prohibition |
| C-30 | INERTIA MANIFEST pre-declares all 4 C-04 surfaces in Step 0 | holistic-pre-declaration-before-analysis |
| C-31 | C-28+C-29+C-30 compose without regressing any prior criterion | additive-architecture-without-interference |

**Scoring formula updated**: aspirational denominator `/19` -> `/23`. All other tiers and thresholds unchanged.

**Key design notes:**
- C-28 has no focus dependency — it fires whenever STRATEGY is present, since the guarantee is unconditional
- C-29 fires on ordering constraints in Step 0, whether focus is active or not
- C-30 has no N/A path — MANIFEST is warranted whenever C-04 applies (always), since the criterion tests pre-declaration vs. distributed coverage
- C-31 is the composability sentinel: score it last, and use any regression it surfaces to identify the interference layer for next-round variation work
