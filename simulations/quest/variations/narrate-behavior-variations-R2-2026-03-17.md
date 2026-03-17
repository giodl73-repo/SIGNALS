Written to `simulations/quest/variations/narrate-behavior-variations-R9-2026-03-17.md`.

---

## narrate-behavior Variations — Round 9 (V-41 through V-45)

**Base**: V-40 (R8 champion). **Critical finding**: V-40's ASSUMPTION CONSERVATION uses a 3-term equation (N_inertia_rows + N_covered + N_none = N_total) that merges FINDING+INVESTIGATION — this likely fails C-31, which requires all four disposition types as separate terms.

---

### Variation Table

| # | Axis | Key bet |
|---|------|---------|
| **V-41** | Inertia framing — 4-term conservation | Split N_inertia_rows into N_finding + N_investigation. Derivation: N_investigation = TRIAGE GATE entry count (each INVESTIGATION A-NN produces exactly one entry). Direct C-31 fix. |
| **V-42** | Output format — risk-density grid | Add RISK DENSITY MATRIX to REPORT: blast-radius × severity 2D grid with F-IDs per cell. WIDE×HIGH = critical quadrant. Every F-ID appears in exactly one cell. New candidate: `risk-density-matrix`. |
| **V-43** | Phrasing register — condensed imperative | V-40 condensed to terse bullets (~40% token reduction). All structural artifacts (INERTIA SURFACE, BOUNDARY REGISTRY, TRIAGE GATE, CROSS-ARTIFACT UTILIZATION MATRIX) unchanged. Tests whether elaborate instruction is load-bearing at V-40 density. |
| **V-44** | Combo: 4-term conservation + lifecycle phases | V-41 + S3 decomposed into 5 named phase blocks (INIT / NOMINAL / DEGRADED / TEARDOWN / HANDOFF) each with PHASE EXIT CONDITION. S3 aggregate EXIT GATE sums all phases. New candidate: `lifecycle-phase-structure`. |
| **V-45** | Combo: 4-term conservation + B-ID risk density | V-41 + CROSS-ARTIFACT UTILIZATION MATRIX gains a **Risk Density Score** column: RDS = sum(blast_weight × findings) per B-ID where WIDE=3, MEDIUM=2, NARROW=1. B-IDs sorted by RDS descending. New candidate: `boundary-risk-density-score`. |

---

### New excellence signal candidates

- **`4-term-assumption-conservation-equation`** (V-41, V-44, V-45) — the direct C-31 compliance fix; strongest realization because N_investigation derivation from TRIAGE GATE entry count creates a cross-artifact equality check
- **`risk-density-matrix`** (V-42) — blast × severity grid gives a visual triage map orthogonal to all existing structural artifacts
- **`lifecycle-phase-structure`** (V-44) — S3 becomes a 5-phase mini-campaign, increasing blast-radius attribution precision per lifecycle stage
- **`boundary-risk-density-score`** (V-45) — quantifies the cross-artifact utilization matrix with blast-weighted risk, enabling ordinal B-ID ranking and a portfolio-level risk invariant

### Open question of interest

Does V-40's 3-term conservation fully fail C-31, or get partial credit? If C-31 awards partial pass for having per-disposition counts present but summed incorrectly, V-40 may score 80/80 anyway (since partial pass still earns a pass toward the 12-of-24 aspirational threshold). V-41 makes C-31 a clean full-pass regardless.
