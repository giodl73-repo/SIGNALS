# trace-migration — Round 7 Variations (v7 rubric)

Five complete variations written to `simulations/quest/rubrics/trace-migration-variations-R7-2026-03-14.md`.

---

## Variation Summary

| V | Single/Combo | Axis | C-26 mechanism | C-27 mechanism |
|---|-------------|------|----------------|----------------|
| **V-01** | Single | Inertia framing as organizational lens | RECOMMENDATIONS GATE B4→VERDICT | DOMAIN BREACH phase — three-part structure is the section's organizing frame; B2 inherits it |
| **V-02** | Single | Output format (per-step scorecard) | RECOMMENDATIONS GATE B4→VERDICT | Mandatory PRIOR WORKING STATE field — structural slot, cannot be omitted without visible blank |
| **V-03** | Single | Phrasing register (adversarial/investigative) | RECOMMENDATIONS GATE B4→VERDICT | "Find what the business was relying on" instruction + seeded example — register forces prior-state naming as the investigative answer |
| **V-04** | Combo | Commerce-first role sequence + inertia framing | RECOMMENDATIONS GATE B4→VERDICT | Two domain-role pre-seeded examples: Q2 Commerce (ENUM/order state) + Q3 Finance (decimal/payment), each demonstrating C-27 independently |
| **V-05** | Combo | Lifecycle + dual-phase inertia pre-seeding + complete terminal gate chain | RECOMMENDATIONS GATE B4→VERDICT (explicit in header) | Pre-seeded C-27 example at DOMAIN IMPACT (Phase A) AND a **distinct** example at DOMAIN SYNTHESIS (Phase B) — prevents Phase B synthesis from reverting to Phase A's example |

---

## Key design decisions

**C-26:** All five use `RECOMMENDATIONS GATE B4→VERDICT` with the VERDICT header explicitly naming it as entry prerequisite. V-05 has the deepest intra-Phase-B gate chain (B2→B3, B3→B4, B4→VERDICT — three gates total).

**C-27:** Three enforcement mechanisms explored:
- *Structural* (V-01 organizational lens, V-02 scorecard field): C-27 is architecturally embedded
- *Posture-driven* (V-03 adversarial register): C-27 emerges from the investigative frame
- *Multi-example seeding* (V-04 per-role, V-05 dual-phase): C-27 is demonstrated at multiple levels

**Unscored differentiator predictions:**
- **C-28 candidate** — V-05 is the only variation with a Phase B pre-seeded C-27 example explicitly distinct from the Phase A example (Finance wire transfer in Phase A → Commerce refund in Phase B). If Phase B synthesis depth varies across runs, this dual-distinct seeding is the source.
- **C-29 candidate** — V-01 and V-03 extend C-20 into Phase A: the Phase A domain section forward-names B2 as its downstream prerequisite, adding a double-layered completion constraint not present in V-02/V-04.
