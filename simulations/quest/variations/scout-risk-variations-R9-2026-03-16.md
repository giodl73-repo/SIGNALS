**Scout-Risk R9 — 5 variations written** to `simulations/quest/golden/scout-risk-variate-R9-2026-03-17.md`

---

## Summary

**R9 baseline diagnosis** — R8 V-05 passes C-28, C-30, and all C-01 through C-27, but fails:
- **C-29**: No Decision Window column in the inertia table
- **C-31**: Row floor stated (7 rows) but no dedicated repair loop for underpopulation

---

### Variation axes and targets

| Variation | Axis | New criteria targeted | Format |
|-----------|------|-----------------------|--------|
| **V-01** | Inertia framing | C-29 (Decision Window in prose) | Prose |
| **V-02** | Output format | C-31 (row floor + Repair Loop A) | Table |
| **V-03** | Phase structure | C-29 + C-30 (Decision Window column in dedicated Table 1) | Table |
| **V-04** | V-01 + V-02 | C-29 + C-31 (prose + Decision Window + row floor loop) | Prose |
| **V-05** | Full combination | C-29 + C-30 + C-31 + all prior criteria | Table |

---

### Key structural decisions in V-05 (the full combination)

- **4 named repair loops** satisfying C-23 and C-21:
  - **Repair Loop A** — row-count gate (C-31)
  - **Repair Loop B** — quality gate / prohibited phrases (C-19 + C-11)
  - **Repair Loop C** — type-diversity count gate (C-18 + C-21)
  - **Repair Loop D** — interdependency count gate (C-16 + C-21)
- C-21 satisfaction: 3 count gates × 3 count-gate loops (A, C, D) = 1:1 match
- **Table 1** has 7 columns including Decision Window, distinct from Table 2's 6 columns (C-28, C-29, C-30)
- **Phase 2b** is explicitly labeled as standalone — not merged with Phase 2 (C-25)
- **From-Severity / To-Severity** vocabulary-constrained to `{HIGH, MEDIUM, LOW}` at cell level (C-22)
