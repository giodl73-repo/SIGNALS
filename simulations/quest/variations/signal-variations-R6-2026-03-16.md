Written to `simulations/quest/golden/signal-variate-R6-2026-03-16.md`.

---

# Quest Variate -- /signal (Round 6)

**R5 champion**: V-05 scored 100/100 on v5 rubric with 9 rules (RULE 1 C-09 through RULE 9 C-17), 9-checkpoint COMPLIANCE AUDIT, and COMPLETENESS SEAL.

**R6 structural gap identified**: R5 V-05 satisfies C-18 (all rules are labeled) and C-19 (gate exists), but neither has a *dedicated RULE entry*. Under R5's own E-1 pattern ("one criterion = one labeled rule, no merges"), RULE 10 (C-18) and RULE 11 (C-19) are the logical obligation.

**Axes explored (single → combination → full integration)**:

| Variation | Axis | Key change |
|-----------|------|------------|
| **V-01** | E-1 single-axis (C-18) | Add RULE 10 (C-18); 10 checkboxes |
| **V-02** | E-1 + E-3 dual-axis (C-19 + bijection) | Add RULE 11 (C-19); 11 checkboxes; bijection restored |
| **V-03** | + E-2 range update | RULE 9 (C-17) updated to assert "C-09 through C-19, 11 rules" explicitly |
| **V-04** | + bijective header declared | COMPLIANCE AUDIT header explicitly names bijection; post-gate `11/11 checked` line |
| **V-05** | Full integration | `FORMAT RULES` → `QUALITY CONTRACT`; `COMPLIANCE AUDIT` → `QUALITY GATE`; RULE 11 names the gate block by its new name -- double-lock |

**Structural champion hypothesis**: V-05 achieves maximum explicit declaration. Every structural property (11-rule bijection, range C-09..C-19, gate block name, naming aligned with C-17's exact terminology) is stated in the prompt rather than inferred from structure. A scorer can verify each criterion by reading the relevant block header without counting or inferring.
