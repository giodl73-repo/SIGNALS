Written to `simulations/quest/golden/campaign-decide-variate-R13-2026-03-17.md`.

---

## R13 Summary

**New criterion in v12:** C-34 — confidence thresholds must appear in a pre-Phase-0 schema definition's column header (not just inline or in Phase 5 output tables).

**Single-axis variations (V-01 through V-03):**

| Var | Axis | C-34 anchor |
|-----|------|-------------|
| V-01 | Phrasing register (imperative → descriptive) | Entry schema at top |
| V-02 | C-34 anchor location | Recommendation schema pre-seeded before Phase 0 |
| V-03 | Lifecycle emphasis (unified schema preamble block) | All schemas hoisted into a single `SCHEMA PREAMBLE` block |

**Combined variations (V-04 through V-05):**

| Var | Axes | C-34 coverage |
|-----|------|---------------|
| V-04 | Inertia framing + C-34 dual anchor | Entry schema + recommendation schema both carry threshold before Phase 0 |
| V-05 | Full integration (103.0/103.0) | Schema preamble defines all 4 schemas (entry, Phase 0 lifecycle, recommendation record, Because block); Phase 5 adds Hypothesis resolution sub-table (C-08/C-13) and Counter-evidence distinct from Counter Block (C-19/C-32) |

**Key V-05 additions beyond R12:**
- `SCHEMA PREAMBLE` block with 4 named schemas before Phase 0 — one definition, unlimited propagation (C-34 fully structurally anchored)
- Phase 0 schema adds `Prior Confidence` column (C-13)
- Phase 5 has both **Counter-evidence** (C-07/C-19: 4-column) AND **Counter Block** (C-32: 3-column) as distinct sub-tables
- **Hypothesis resolution** sub-table added to Phase 5 (C-08)
