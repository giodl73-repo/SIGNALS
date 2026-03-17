Written to `simulations/quest/rubrics/review-design-variate-R14-2026-03-15.md`.

---

## Round 14 Variations — Summary

**Rubric version**: v13 → C-41 + C-42 encoded in all 5 variations (denominator 35)
**New F-IDs introduced**: F-28 (C-42 cross-block section miss), F-29 (registry spurious entry), F-30 (registry block absent)

---

### Variation Plan

| | V | Axis | Single/Combo | Key Structural Change |
|---|---|------|-------------|----------------------|
| | V-01 | F-28 named halt | Single | Minimal: Section leftmost in BLOCK 5 + F-28 inline. No upstream change from R13 V-01. |
| | V-02 | BLOCK 2.7 registry | Single | New dedicated extraction block between 2.5 and 3; F-28 references it. Adds F-29 + F-30. |
| | V-03 | Pre-check enumeration | Single | No new block. BLOCK 5 header requires a bulleted valid-section list before the table. F-28 fires against the list. |
| | V-04 | BLOCK 2.7 + formula + F-28 | Combo | Registry + cost derivation formula + F-28. Three independently verifiable chains. |
| | V-05 | BLOCK 2.7 + elevation + declarative + F-28 | Combo | Declarative register (R13 V-04) + consensus elevation gate (R13 V-03) + registry + F-28. Four-axis convergence. |

---

### Axis Logic

- **V-01 vs V-02 vs V-03** isolate *where* C-42 enforcement lives: inline at use-point (V-01), upstream dedicated block (V-02), or inline pre-enumeration in same block (V-03). This is the core C-42 enforcement placement experiment.
- **V-04** adds cost formula continuity (proven 100.00 in R13) on top of V-02 — tests whether the three-chain combination produces a new enforcement gap at the Priority Rank formula layer.
- **V-05** stacks the full ceiling: declarative register + elevation record + registry + F-28. The novel target is the intersection: can an ELEVATED finding (consensus-amplified) reference a section the review never identified? If yes, that's a dual-gate failure class not previously reachable.
