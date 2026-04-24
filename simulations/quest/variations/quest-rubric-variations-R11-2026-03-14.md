Written to `simulations/quest/rubrics/quest-rubric-rubric-v11-variate-R11-2026-03-15.md`.

---

## R11 Variations Summary

**Five complete, runnable quest-rubric skill body prompts.**

### Axis map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | R11 full integration baseline | C-33 fix: "or equivalent block" in SetCoherenceAuditor role definition + Contract item 4 requires the phrase there; Contract item 5 adds DR sub-section labeling; two independent checkpoint rows |
| **V-02** | Role-definition phrase ablation | Phrase absent from role definition — Contract achieves structural equivalence but role-definition layer is bare. Reproduces R10/V-01 state exactly. Predicts C-25 PARTIAL + C-26 FAIL (joint failure from one root cause) |
| **V-03** | Contract item 5 absent | DR sub-section labeling Contract item removed. Role-definition phrase retained. Tests whether C-27 (labeled sub-sections) is achievable via Phase 3 ordering instruction alone or requires Contract enforcement |
| **V-04** | Merged checkpoint row | Both novel Contract items (phrase + DR labeling) present, but covered by one merged checkpoint row instead of two independent rows. Tests v12 candidate `c31-checkpoint-row-minimum-count-scales-with-contract-depth` |
| **V-05** | Advisory register + no Phase 1 (combination) | R10/V-02 × R10/V-05 dual-ablation floor. Imperative gates replaced with advisory language; planning phase removed. Measures superadditivity against R10 single-ablation baselines |

### What R11 tests

- **C-33 confirmation**: V-01 vs V-02 is the clean isolation — does the phrase at the role-definition layer add value over Contract structural equivalence alone?
- **v12 candidate `and-gate-contract-does-not-propagate-to-dr-sub-section-labeling`**: V-01 vs V-03 — does Contract item 5 drive C-27 compliance or is Phase 3 ordering sufficient?
- **v12 candidate `c31-checkpoint-row-minimum-count`**: V-04 — does the merged row cause silent drop of one novel element?
- **C-34 superadditivity**: V-05 vs R10/V-02 and R10/V-05 — do advisory register and absent planning compound beyond each alone?
