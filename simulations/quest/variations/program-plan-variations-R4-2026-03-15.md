Written to `simulations/quest/golden/program-plan-variate-R4-2026-03-16.md`.

---

## R4 Variate Summary

**Three new criteria in v4**: C-16 (criterion-referenced error tagging), C-17 (per-zone gate contrast), C-18 (correction table). R3's best variate (V-04 lifecycle bands) was the top scorer under v3 but hit none of the three new criteria.

**Single-axis variations:**

| Variation | Axis | New criteria targeted | Expected gap |
|-----------|------|-----------------------|--------------|
| V-01 | Criterion-referenced error tagging | C-16 PASS | C-17, C-18 FAIL by design |
| V-02 | Per-zone gate contrast | C-17 PASS | C-16, C-18 FAIL by design |
| V-03 | Correction table | C-18 PASS | C-16, C-17 FAIL by design |

**Combined variations:**

- **V-04** (C-16 + C-17): criterion-tagged BAD PLAN block + FAIL/PASS at every zone header — C-16 and C-17 PASS, C-18 FAIL by design. ~130/145.
- **V-05** (all 18, golden): correction table first → criterion-tagged BAD PLAN → GOOD plan → zone-by-zone template with FAIL/PASS + `# WRONG C-NN` + REQUIRED annotations. Targets all 18 criteria. ~145/145 predicted.

**Key design decision**: V-05 stacks all three mechanisms without removing R3's foundation — the correction table is pre-generation (active avoidance), the criterion tags are in-example (causal mapping), and the per-zone PASS/FAIL is in-template (point-of-authoring feedback). Three different pedagogical modes for the same essential requirements.
