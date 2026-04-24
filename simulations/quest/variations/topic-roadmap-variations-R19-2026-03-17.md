Written to `simulations/quest/golden/topic-roadmap-variate-R19-2026-03-17.md`.

---

## R19 Variation Summary

| Var | Axis | C-45 | C-46 | Expected |
|-----|------|:----:|:----:|:--------:|
| V-01 | Single: C-45 — §9 named inside self-sufficiency declaration body | FULL | FAIL | 74/76 = 9.74 |
| V-02 | Single: C-46 — CONSISTENCY AUDIT CLAUSE with satisfaction confirmations + intra-block pointers | FAIL | FULL | 74/76 = 9.74 |
| V-03 | Partial: §9 reference in preamble annotation (outside declaration body) | PARTIAL | FULL | 75/76 = 9.87 |
| V-04 | Combined: C-45 FULL + C-46 PARTIAL (confirmations without location pointers) | FULL | PARTIAL | 75/76 = 9.87 |
| V-05 | Maximal: §9 named inside declaration + CONSISTENCY AUDIT CLAUSE with confirmations + location pointers | FULL | FULL | 76/76 = **10.00** |

**Key structural moves:**

- **C-45 FULL** (V-01/V-04/V-05): `The compliance enforcement site for this declaration is the PROPOSAL BIAS AUDIT guard [§9] at Phase 6 entry.` placed *inside* the SCORER SELF-SUFFICIENCY DECLARATION body — closing the triangle leg CONTRACT B→§9.

- **C-45 PARTIAL** (V-03): §9 reference lives in `[>> Enforcement site: ... <<]` preamble annotation *before* the declaration — reference exists, wrong structural location.

- **C-46 FULL** (V-02/V-03/V-05): CONSISTENCY AUDIT CLAUSE with `This CONTRACT B block satisfies the EXACT-VALUE REQUIREMENT at the "Compliant value" line above` and `satisfies the TAXONOMY-SPLIT REQUIREMENT at the "Violation taxonomy" section above` — both confirmations with intra-block pointers.

- **C-46 PARTIAL** (V-04): `This CONTRACT B block satisfies the EXACT-VALUE REQUIREMENT` and `satisfies the TAXONOMY-SPLIT REQUIREMENT` — confirmations declared but no pointer to *where* within the block satisfaction is met.

- **V-05 maximal**: adds full bidirectional §9 language in the compliance obligation (`The guard-contract relationship is bidirectional: CONTRACT B declares the governed value; this §9 obligation names the value and declares CONTRACT B as source authority; CONTRACT B's self-sufficiency declaration names §9 as the enforcement site.`), completing the three-directional pointer triangle from both artifact entry points.
