---

## campaign-simulate -- Round 4 Variations

**Context**: R3 V-05 introduced a structural-axis preamble (prompt-level instruction text) and an end-checklist (template with empty checkboxes). These were codified as C-17 (Pre-Finding Structural Axis Declaration) and C-18 (End-of-Report Structural Compliance Checklist) in rubric v4. R4 closes the two gaps: (1) the declaration must be a section the model *writes into the output* before findings, not just prompt intro text; (2) the checklist must require evidence citations (section name + actual counts), not just checked boxes.

---

**Round 4 axes:**
- Single-axis: V-01 (declaration section written by model into output / C-17), V-02 (evidence-citation compliance checklist / C-18), V-03 (audit register -- organic C-17+C-18 via domain framing)
- Combined: V-04 (C-17 + C-18 on R3 V-05 base), V-05 (4 structural axes: filtering + empty-state + comparison + declaration-compliance)

---

### V-01 — Pre-Finding Structural Axis Declaration Axis (single-axis, C-17)
Adds a `STRUCTURAL AXIS DECLARATION` table the model writes as the **first section of the output artifact** before any execution results. The table commits to axis names, mechanisms, and report sections. Hypothesis: C-17 fires by construction. C-18 is not targeted (no compliance checklist), so the closing verification gap remains.

### V-02 — End-of-Report Structural Compliance Checklist Axis (single-axis, C-18)
Upgrades the R3 V-05 end-checklist from empty-checkbox template to a `STRUCTURAL COMPLIANCE CHECKLIST` table the model writes as the **final section of the output artifact**. The Evidence column requires quoting actual counts and section names ("Filter Log: 4 obs, 1 rejected at Rule 2"). Hypothesis: C-18 fires by construction. C-17 is not targeted (no formal preamble section written by the model).

### V-03 — Audit Register Axis (single-axis, organic C-17+C-18)
Complete reframe as a formal technical audit. Sections become `AUDIT SCOPE AND STRUCTURAL CONTROLS` (analog to C-17) and `AUDIT COMPLIANCE SUMMARY` (analog to C-18). Tests whether an audit domain register generates the structural discipline organically — without explicit declaration/checklist templates. Risk: prose audit sections may not satisfy the mechanism-naming and section-citation requirements of C-17/C-18 pass conditions.

### V-04 — Combined: C-17 + C-18
R3 V-05 base + `STRUCTURAL AXIS DECLARATION` section (C-17, first in output) + `STRUCTURAL COMPLIANCE CHECKLIST` section (C-18, last in output, evidence citations required). All prior mechanisms carry forward. Hypothesis: both new criteria pass by construction.

### V-05 — Full Integration (four structural axes)
Extends V-04 with a fourth axis — the declaration-compliance axis (C-17 + C-18 as their own structural mechanism, declared in the preamble and verified in the checklist). The declaration table now names four axes. The compliance checklist covers all four. The checklist self-attests to its own presence ("Structural Compliance Checklist: present as final section"). This is the first variation in the series where the structural verification system verifies itself.

---

Written to `simulations/quest/golden/campaign-simulate-variate-R4-2026-03-16.md`.
