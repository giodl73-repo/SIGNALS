Written to `simulations/quest/rubrics/quest-score-rubric-v11-2026-03-15.md`.

---

**Two new criteria extracted from R10 V-01 excellence signals:**

**C-28 — Regression signals Variation column in causal position** (continuity)
V-01's table used `Criterion / Prior / Current / Variation / Mechanism` — Variation as column 4, not appended after Mechanism. C-27 requires the column to exist; C-28 requires it to occupy the causal slot between Current Verdict and Mechanism. Column 5 ordering satisfies C-27 but inverts the narrative: detection logic before identified cause. C-28 auto-PASS when C-07 auto-PASS fires.

**C-29 — Auto-PASS cascade dependencies name triggering criterion** (structure)
V-01's preamble declared "C-28 auto-PASS when C-07 auto-PASS fires" — naming the gating criterion by ID rather than repeating the data condition. C-16 requires named declarations; C-29 requires cascade declarations to identify the triggering criterion ID. Repeating the condition ("when no prior-round data") obscures the cascade graph; naming the trigger makes it maintainable. C-29 auto-PASS when the rubric has no cascade dependencies.

**Cascade updates in v11:**
- N_aspirational: 20 → 22; each criterion contributes 10/22 pt (~0.45 pt)
- C-11: C-28 and C-29 added to required auto-PASS declaration list
- C-14: 27-row → 29-row
- C-25 "Applied in this rubric": added `C-28 (for C-27), C-29 (for C-16)`
- Both C-28 and C-29 apply the C-25 three-scale enumeration principle (each has a PARTIAL defined by one of two required elements present), so both are registered in the inventory
