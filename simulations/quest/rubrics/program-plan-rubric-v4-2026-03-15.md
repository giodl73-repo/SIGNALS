Written to `simulations/quest/rubrics/program-plan-rubric-v4-2026-03-16.md`.

---

## Three new criteria added from R3 excellence signals

**C-16 — Criterion-Referenced Error Tagging**
Error examples (inline or block) carry explicit criterion tags: `# WRONG C-02`, `# WRONG C-04`. This goes beyond C-10 (contrast pair) and C-15 (bad YAML block) by indexing each error to the criterion it violates — a model sees WHY the example fails, not just THAT it fails. R3 source: V-03's BAD PLAN YAML with per-field criterion tags. Pass: at least one tagged error present. No partial.

**C-17 — Per-Zone Gate Contrast**
Every arc zone carries its own inline PASS/FAIL gate example, not just a central contrast section. C-10 requires one pair; C-17 requires coverage at each authoring decision point, removing the attention gap between contrast and gate. R3 source: V-01's zone headers with labeled PASS/FAIL at every zone. Pass: all non-echo zones; partial: >= half the zones.

**C-18 — Wrong-to-Correct Correction Table**
A structured lookup table (wrong skill → real skill, execution gate → artifact gate) with >= 3 pairs. Complements C-10/C-15/C-16 by enabling active avoidance before generation rather than pattern-matching from embedded examples. R3 source: V-03's correction table mapping invented skills and bad gates. Pass: table present with >= 3 pairs covering at least one essential criterion. No partial.

**Scoring change:** Aspirational tier 8 → 11 criteria, 40 → 55 pts. Total max is now **145**. Golden threshold (>= 80) unchanged.
