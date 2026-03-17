Here are the 5 variations for `crew-roles` Round 15:

---

**Baseline**: R14 all-three-combined (C-30 inertia-first gate + C-31 vocab plan-to-write binding + C-32 inline LENS AUDIT). No single R14 variation contained all three — R14 V-04 had C-30+C-31, V-05 had C-31+C-32. R15 synthesizes all three as the starting point.

**Gaps closed**:

| Gap | Criteria | Root cause |
|-----|----------|------------|
| Gap-A | C-08 perspective diversity | Phase 5 has a Perspective column; Phase 6 says "3 distinct"; Phase 7 has no CHECK auditing it — no structural gate |
| Gap-B | C-25 / C-27 source phrase citation | FRAME FILL cites CONVERGENCE SUMMARY answers but never traces back to the Phase 1 verbatim source phrase that grounded each term |
| Gap-C | C-24 replacement re-audit | CHECK 3B / 4B mismatch correction is ad hoc — no ROLE-REPLACE sub-procedure producing a confirmed re-evaluation artifact |

**Variation summary**:

| # | Axis | Single/Combined | New mechanism |
|---|------|-----------------|---------------|
| V-01 | Perspective diversity gate | Single | PERSPECTIVE AUDIT in Phase 5; CHECK 8 in Phase 7 (>= 3 distinct perspective values) |
| V-02 | Source phrase forensic citation | Single | `Phase 1 source:` lines in FRAME FILL; CHECK 5 splits into 5A (frame match) + 5B (source citations) |
| V-03 | Role replacement re-audit | Single | ROLE-REPLACE sub-procedure at every CHECK 3B / 4B mismatch — records event, re-evaluates row, emits CONFIRMED signal |
| V-04 | V-01 + V-02 | Combined | Gap-A + Gap-B closed; CHECK 8 + CHECK 5B both added |
| V-05 | V-01 + V-02 + V-03 | Combined | All three gaps closed; maximum criterion coverage |

**Key structural additions**:
- V-01/V-04/V-05: `PERSPECTIVE AUDIT PASS` required before Phase 6 opens; CHECK 8 re-validates from written files
- V-02/V-04/V-05: Each FRAME FILL slot has a `Phase 1 source: {row-id} = "{verbatim phrase}"` line; CHECK 5B flags missing or unverifiable citations
- V-03/V-05: `ROLE-REPLACE` block fires at each mismatch with four fields (planned, written, resolution, re-evaluation) and `ROLE-REPLACE CONFIRMED: YES/NO` — CHECK 3B / 4B cannot close until all CONFIRMED signals are YES

Written to: `simulations/quest/golden/crew-roles-variate-R15-2026-03-17.md`
