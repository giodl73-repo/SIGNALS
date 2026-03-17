All changes verified. Here is the complete updated rubric as Markdown — output below:

---

Written to `simulations/quest/rubrics/program-plan-rubric-v17-2026-03-16.md`.

**v17 summary — two new criteria from R16 excellence signals:**

| Criterion | Pattern | Source | Prerequisite |
|-----------|---------|--------|--------------|
| **C-52** | C-51 protocol declaration section explicitly pre-declares the C-41 index table column schema (naming all 4 columns by purpose) before the BAD PLAN block — creating dual exposure: model reads column spec in protocol section, then instantiated table in header | V-05 exclusively (dual-exposure via C-50+C-51 conjunction) | C-50, C-51 |
| **C-53** | C-52 pre-declaration uses prescriptive/directive language ("Component 1 must/will/shall be a 4-column table") rather than descriptive language — converting C-50 from observed structural choice into protocol-mandated format requirement, making mutual reinforcement an explicit architectural fact | V-05 exclusively (mandate language completing the conversion) | C-52 |

**Scoring delta**: 44 → 46 aspirational · 220 → 230 aspirational pts · **310 → 320 total pts**. Formula denominator: `aspirational_pass/46 * 230`. Golden threshold unchanged (>= 80).

The two criteria are strictly chained (C-53 requires C-52 requires C-50+C-51), so only a variate that already passes all four of C-48, C-49, C-50, C-51 can reach C-52, and only a variate passing C-52 can reach C-53. The top reachable score for V-05 is now 320.
