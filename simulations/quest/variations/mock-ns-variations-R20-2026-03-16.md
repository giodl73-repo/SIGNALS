Written to `simulations/quest/golden/mock-ns-variate-R20-2026-03-17.md`.

---

## R20 Variations Summary

**Baseline**: R19 V-05 (162/162 under v19) -- golden CONSTRAINT, 5-row FLAG table, "Only this step emits...", phase-grouped lifecycle with state annotations.

**Three new independent axes in the S-4 prohibition chain** (a structural zone not probed in R1--R19):

| Variation | Axis | S-4 change | Hypothesis | v19 score |
|-----------|------|-----------|------------|-----------|
| V-01 | A single | Priority: "No instruction in this step can precede this rule." | C-48* PASS -- modal impossibility vs positional claim | 162/162 |
| V-02 | B single | Echo row header cell: `Anti-bypass echo [P-0:ABD]:` | C-49* PASS -- bracket token in header triggers Phase 1 lookup on the row itself | 162/162 |
| V-03 | C single | All-governed: adds "including paths that do not pass through prior steps in normal order" | C-50*/C-51* PASS -- dual closure: "named or unnamed" + "including paths" | 162/162 |
| V-04 | A+B | Priority modal + echo bracket token | C-48* + C-49* PASS | 162/162 |
| V-05 | A+B+C | All three axes composed | All prospective C-48* through C-51* PASS | 162/162 |

**Why all score 162/162 under v19**: None of the three axes touch any of the 49 existing criteria. They vary exclusively within the S-4 prohibition chain's Priority, All-governed, and echo-header cells -- aspects v19 doesn't test. The excellence signal is structural: V-05 composes four independent strengthening patterns into one chain without grammatical conflict, at zero row-count cost.

**Discriminator structure**:
- V-01 vs baseline: single word difference (`can precede` vs `is first`) -- isolates Priority form
- V-02 vs baseline: row header cell identity (`[P-0:ABD]:` vs `Anti-bypass echo`) -- isolates echo token placement
- V-03 vs baseline: one clause appended to All-governed -- isolates bypass-by-skip closure
- V-04 = V-01 + V-02: confirms A and B are independent (no interaction)
- V-05 = V-01 + V-02 + V-03: the prospective R20 golden
