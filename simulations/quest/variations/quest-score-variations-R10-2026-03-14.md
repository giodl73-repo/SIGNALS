File written: `simulations/quest/rubrics/quest-score-rubric-v10-variations-R10-2026-03-15.md` — 973 lines, 5 complete variations.

---

**R10 Design Summary**

**Variation axes and predicted evidence ladders:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-26 | PASS | PARTIAL | FAIL | PASS | FAIL |
| C-27 | PASS | PASS | PASS | PARTIAL | PARTIAL |

**What each variation tests:**

- **V-01 — Full-stack baseline.** N_aspirational=20, 27-row roster, C-25 section has paired inventory `C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18)`, regression table has 5 columns including Variation, C-11 includes C-27 auto-PASS declaration.

- **V-02 — C-26 PARTIAL.** Inventory present but lists only applying criterion IDs: `C-23, C-24, C-26, C-27` without target pairings. Discriminates PARTIAL from PASS on the "both fields required" boundary.

- **V-03 — C-26 FAIL.** No inventory at all — only the general principle prose. C-25 PASS holds (standalone section intact). Discriminates FAIL from PARTIAL.

- **V-04 — C-27 PARTIAL.** Regression table has 4 columns (C-18 satisfied), Variation column absent. C-26 PASS (full inventory). Discriminates PARTIAL from PASS on the Variation column boundary.

- **V-05 — Floor.** C-26 FAIL (no inventory) + C-27 PARTIAL (4-column table). Predicted composite 99.25 — all golden, 0.75 pt spread from V-01.

**Predicted score range:** 99.25–100.00, spread 0.75 pt (clusters by C-09 threshold). Each aspirational FAIL costs 0.5 pt; each PARTIAL costs 0.25 pt.
