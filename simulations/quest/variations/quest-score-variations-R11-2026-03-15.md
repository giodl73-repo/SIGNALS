Written to `simulations/quest/golden/quest-score-variate-R11-2026-03-15.md`.

---

## R11 design summary

**Primary gap closed:** C-30 VERIFIER pair-omission prohibition. Every R10 variation scored PARTIAL or FAIL on this criterion.

**Forced infrastructure change:** Formula `/22 * 220` → `/23 * 220` (C-03).

### Single-axis variations

| Variation | Base | Axis | Key change |
|-----------|------|------|------------|
| V-01 | R10 V-01 | C-30 on role-sequence base | Add "Do not omit any pair even where Specificity appears to PASS" after the positive mandate |
| V-02 | R10 V-02 | C-30 on table-format base | Replace "Cells with Specificity PASS may be omitted" (C-30 FAIL) with explicit prohibition — minimum repair to a FAIL |
| V-03 | R10 V-03 | C-30 on lifecycle-phase base | Insert prohibition inside Phase 3 — tests whether PRH survives double-inscription without interference |

### Combination variations

| Variation | C-30 | C-29 | C-28 | Composite |
|-----------|------|------|------|-----------|
| V-04 | PASS | PASS (adds dual-scope IRQ to V-01 R11) | PARTIAL | ~300 |
| V-05 | PASS | PASS (inherited) | PASS (inherited) | 310 |

**Design principle for C-30:** C-30 follows C-15 over C-13 exactly. C-13 defined a conditional CHANGE slot; C-15 closed the silent-omission path by making the field mandatory with three named values. C-12 defines the VERIFIER schema and states a positive coverage mandate; C-30 closes the explicit-exception path by naming "PASS cells may be omitted" as a prohibited deviation. The positive mandate alone (V-01 R10) is insufficient — the prohibition must name the anti-pattern.
