Written to `simulations/quest/golden/org-pr-variate-R5-2026-03-16.md`.

---

## org-pr — Round 5 Variations

**5 variations generated. Two unsealed gaps targeted: C-07/C-22 (all 4 rounds PARTIAL) and C-09 (all 4 rounds FAIL/PARTIAL).**

### Variation Plan

| Variation | Axis | Primary Targets |
|-----------|------|----------------|
| **V-01** | C-22 isolation | C-07 → C-22 PASS (minimal prompt, Resolution column only) |
| **V-02** | C-09 isolation | C-09 PASS (pre-merge phase gate, single axis) |
| **V-03** | C-22 + C-09 two-axis | Both gaps, no priority table needed |
| **V-04** | C-22 + C-21 + C-09 + priority table | Three new criteria; C-20 table required at N=3 |
| **V-05** | Full integration (R4 V-05 + all v5 criteria) | All remaining gaps; eight-axis priority table; verdict hardening pair explicit |

### Key Design Decisions

**V-01 (C-22 isolation)**: Minimal delta from R4 V-03. The Resolution column adds a single rule: lower authority position number governs; higher-position role records as downstream risk entry, not counter-finding. This is the R5 hypothesis for closing C-07.

**V-02 (C-09 isolation)**: Phase gate first, clean minimal structure. Explicit do-not-run-after-merge boundary with a halt instruction. No inertia framing to isolate the axis cleanly.

**V-04 (three-axis + table)**: Priority table required per C-20 (3 axes present). Each axis assigned a non-overlapping governance domain. C-21 declaration explicit: "if-stays projection on upstream surface = compounding cost description, not reclassification." This is what separates C-21 PASS from the implicit handling in R4.

**V-05 (full integration)**: Eight-axis table. Verdict hardening pair declared explicitly as a named unit — formula lock + escape closure must co-occur (C-19). Resolution column wired to authority-position logic with the mechanical derivation stated. Pre-commit self-check extended to 7 items covering all new criteria.

### Expected Score Trajectory

| Variation | C-07 | C-09 | C-19 | C-20 | C-21 | C-22 | Expected |
|-----------|------|------|------|------|------|------|----------|
| V-01 | PASS | FAIL | — | N/A | N/A | PASS | ~84 |
| V-02 | PARTIAL | PASS | — | N/A | N/A | N/A | ~84 |
| V-03 | PASS | PASS | PARTIAL | N/A | N/A | PASS | ~88 |
| V-04 | PASS | PASS | PARTIAL | PASS | PASS | PASS | ~91 |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | ~96+ |
