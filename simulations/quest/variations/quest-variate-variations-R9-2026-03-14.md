Here are the R9 variations, written to `simulations/quest/rubrics/quest-variate-rubric-v9-2026-03-15.md`.

---

## R9 Design Summary

The R9 set is structured as a **C-28/C-29/C-30 evidence matrix** — each variation holds two of the three new v9 criteria and ablates the third:

| V-ID | C-28 (*Prevents:* >=2 modes) | C-29 (Phase 3 gate) | C-30 (sibling text in primary-effect) | Expected score |
|------|------------------------------|---------------------|----------------------------------------|----------------|
| V-01 | PASS (3 modes) | PASS | PASS | 23/23 — first variation to satisfy all |
| V-02 | PASS | PASS | FAIL (directional) | R8/V-05 state — 89.57 |
| V-03 | PASS | FAIL | PASS | R8/V-01+C30 state |
| V-04 | FAIL (1 mode) | PASS | PASS | New combination not tested in R8 |
| V-05 | PASS | FAIL | FAIL | R8/V-01 state exactly — 89.57 |

**Key structural decisions:**

**V-01** closes both gaps from R8's co-leaders: takes V-05's Phase 3 STOP CONDITION (C-29) and V-01's cross-variation text anchor technique (C-30). The primary-effect field embeds V-03's exact positive expected text — *"Output V-01 through V-05 in order"* as the first words of V-03's un-gated Phase 3 — satisfying C-30 through the sibling's positive expected content rather than absence framing.

**V-02** is the clean C-30 ablation: full structural enforcement retained (Phase 3 gate present, 3-mode label), but primary-effect reverts to directional framing. This is the R8/V-05 state, now providing the isolated C-30 measurement.

**V-03** is the clean C-29 ablation: sibling text anchor present in primary-effect (C-30 passes), 3-mode label present (C-28 passes), but Phase 3 STOP CONDITION removed. Primary-effect embeds V-01's expected gate text as its sibling anchor.

**V-04** is the new C-28 ablation with C-29+C-30 both present — a combination not available in R8 since C-30 wasn't defined yet. Tests whether named-mode density adds behavioral value when structural gate enforcement is already in place.

**V-05** is the dual C-29+C-30 ablation (= R8/V-01 exactly), providing the floor for the joint-contribution measurement. If V-05 degrades more than V-02 and V-03 alone, the mechanisms are positively interactive.
