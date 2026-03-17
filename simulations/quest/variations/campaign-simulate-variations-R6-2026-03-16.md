Written to `simulations/quest/golden/campaign-simulate-variate-R6-2026-03-16.md`.

---

## campaign-simulate — Round 6 Variations

**Base**: R5 V-05 (100/100 under v5 rubric). Under v6: R5 V-05 without C-22/C-23 = **96.4 normalized** (106/110, divisor 1.10). Both new criteria needed for 100.

**C-22** (new): Observational discipline must be a co-equal structural axis — row 5 in the axis table with the same Observable Output column depth as rows 1-4 (3+ distinct named sub-observables), not just a co-located section.

**C-23** (new): T-1 must be falsified — the filter log or its resolution must cite a named observation that was evaluated, failed T-1, and was withheld. Declaration alone is insufficient.

---

### Variation Summary

| Variation | Axis | Hypothesis | C-22 | C-23 |
|-----------|------|-----------|------|------|
| **V-01** | C-22 only — co-equal axis row depth | Row 5 has 3 named sub-observables (genre section, T-1 in filter log, per-scope gates); evaluator can verify C-22 from declaration table alone | PASS | RISK |
| **V-02** | C-23 only — T-1 rejection obligation | Filter Log Resolution gains a mandatory T-1 ANNEX; must name a withheld-T1 observation or invoke T-1 RECALIBRATION; report cannot close without it | RISK | PASS |
| **V-03** | C-23 alt — per-scope T-1 evaluation log | Each sub-skill's gate table has a Disposition column (elevated/withheld-T1/withheld-rule); T-1 EVALUATION SUMMARY aggregates across all five scopes; T-1 evidence co-located with execution | RISK | PASS |
| **V-04** | Combined C-22 + C-23 on R5 V-05 base | Equal-depth row 5 + mandatory T-1 ANNEX; both pass by construction; compliance checklist row 6 cites the named T-1 rejection | PASS | PASS |
| **V-05** | Full integration: C-22 + C-23 + hardened partial compliance | Same as V-04 + compliance checklist row 6 uses `fired/partial/not fired` with three independently-verifiable sub-claims; partial verdict names which sub-claim failed | PASS | PASS |

**Key structural differences vs R5 V-05:**
- **V-01**: Adds explicit depth requirements to the axis declaration ("2+ distinct observables per row"); row 5 names three sub-observables rather than one summary
- **V-02**: Introduces `T-1 ANNEX` as a mandatory named block after Template A/B; adds the `T-1 ANNEX RECALIBRATION` empty-state template
- **V-03**: Distributes T-1 evidence to per-scope gate tables with a Disposition column; adds T-1 EVALUATION SUMMARY section; partial-compliance verdicability is by scope
- **V-04**: Combines V-01 and V-02 cleanly on the R5 V-05 base with minimal structural overhead
- **V-05**: Adds the "Partial verdict guidance" block to row 6 of the compliance checklist — names which sub-claim failed, rather than just reporting partial
