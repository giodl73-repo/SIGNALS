---

# Variate R11 — corps-leaderboard

Written to `simulations/quest/golden/corps-leaderboard-variate-R11-2026-03-17.md`.

---

## Design summary

**R10 gaps closed in R11:**

| Variation | R10 score | What changed | R11 score |
|-----------|-----------|-------------|-----------|
| V-01 | 97.83 (18/23) | Added C-27 (health/inertia split in Sec 2), C-30 (contamination gate item), C-31 (inertia-aware Skeptic scope) | **99.13** (21/23) |
| V-02 | 98.70 (20/23) | Same three additions; Analyst gains Health + Inertia sub-phases; Analyst Gate updated; Publisher Skeptic scope names inertia flags | **100.00** (23/23) |
| V-03 | new | Novel axis: inertia-first lifecycle (Phase 2a = Inertia, Phase 2b = Health); contamination direction reversed; cluster table seed | **99.13** (21/23) |
| V-04 | 97.83 (18/23) | Restructured to 3-role (Surveyor/Assessor/Strategist) — gains C-27/C-28/C-29/C-30/C-31 | **100.00** (23/23) |
| V-05 | 100.00 (23/23) | Carries all 23 + adds both seed patterns as structural requirements | **100.00** (23/23) |

**C-27 remains load-bearing** for three criteria (C-27, C-30, C-31). Every variation now includes the health/inertia structural split.

---

## Two v12 seed patterns introduced

**Seed A — Inertia Flag-to-Action Traceability** (V-01, V-05 — candidate v12-C-32): actions resolving a trajectory gap declare `resolves: {flag-name}`. Orthogonal to the `prevents:` machinery (C-20/C-22/C-24) and the achievement-name requirement (C-05). Presupposes C-27.

**Seed B — Pre-Synthesis Cross-Dimensional Reconciliation** (V-02, V-05 — candidate v12-C-33): before the Team Insight, the Publisher emits a named pairing (one Health observation + one Inertia observation + interaction statement); the Skeptic gate then requires the insight to advance beyond the pairing. Orthogonal to C-25 (novelty relative to analysis) and C-31 (Skeptic knowledge scope). Presupposes C-27 and C-31.

**Ceiling-breaking condition for v12**: a variation that passes both C-32 and C-33 would reach 25/25 (if both are added). V-05 is the template — it already has both patterns as required structural elements.
