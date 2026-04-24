Written to `simulations/quest/rubrics/quest-variate-rubric-v14-variations-R15-2026-03-15.md`.

---

## R15 Variations — Summary

**C-39 candidate: Secondary-effect FROM/TO gate at Phase 1 STOP CONDITION**

The structural gap in R14/V-01: the Phase 1 STOP has 3 gate conditions — completeness, primary-effect specificity (C-26 parallel), predicted-site V-ID citation (C-26). There is no gate condition for the secondary-effect FROM/TO endpoint requirement (C-34). A model can pass the Phase 1 STOP with directional-only secondary-effect cells and the FROM/TO requirement is only caught at rubric-review time. R15 adds a 4th gate condition.

Design chain: C-18 (countervailing consequence) → C-34 (FROM/TO endpoints named) → **C-39** (FROM/TO gate enforced at Phase 1 STOP, blocking Phase 2 until at least one endpoint pair is committed) — parallel to the predicted-site ladder C-19 → C-20 → C-26.

---

| Variation | Axis | Predicted failures |
|-----------|------|--------------------|
| V-01 | R15 full stack (R14 + C-39: 4th Phase 1 STOP condition for FROM/TO endpoints) | — |
| V-02 | C-39 ablation — Phase 1 STOP has 3 conditions; FROM/TO column header (C-34) retained; C-38 retained | C-39 |
| V-03 | C-38 ablation + C-39 retained — unified checkpoint failure routing; equivalent to R14/V-02 + C-39 | C-38 |
| V-04 | C-37 ablation + C-39 retained — Phase 2 STOP routes to Phase 3 generically; equivalent to R14/V-03 + C-39 | C-37 |
| V-05 | C-39 + C-38 combination — no FROM/TO gate + unified failure routing; superadditivity test | C-39, C-38 |

**Predicted tier structure under v14:** V-01 at 100.00; V-02/V-03/V-04 symmetric at 99.68 (each a single independent failure at a distinct structural boundary); V-05 at 99.35 (two failures, no entailment).
