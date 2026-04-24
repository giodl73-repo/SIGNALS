Written to `simulations/quest/golden/corps-leaderboard-variate-R12-2026-03-17.md`.

---

## R12 — corps-leaderboard — 5 Variations

**R11 ceiling entering R12**: V-02, V-04, V-05 = 23/23 = 100.00. V-01, V-03 = 21/23 = 99.13 (no named role pipeline → fail C-26, C-28). R12 fixes both gaps across all 5 variations.

**Expected against v11**: all 5 → 23/23 = 100.00.

---

### Variation Axes

| | Axis | Seeds |
|--|------|-------|
| **V-01** | Phrasing register — RFC-style numbered requirements (REQ-N.M identifiers) replacing role-block imperative prose. 3-role pipeline carried forward as sections, not role blocks. | Seed A (`resolves:` annotation), Seed D (inertia severity tier column) |
| **V-02** | Role sequence — 4-role pipeline splits Publisher into Strategist (actions) + Narrator (reconciliation + insight). Three handoffs strengthen C-28. Narrator sees completed action list *before* writing the insight, raising the novelty bar. | Seeds A+B formalized, Seed E (Narrator confidence gate: commit `high`/`medium`/`low` on reconciliation before writing insight) |
| **V-03** | Output format — dashboard-first sprint briefing. Archivist opens with a compact Sprint Velocity Dashboard *before* the registry table, committing to a preliminary posture that the Analyst's Inertia Phase must confirm or correct. 3-role pipeline. | Seed F (action dependency chain: `requires: {action-N}` for sequentially dependent actions) |
| **V-04** | Combination — inertia-first lifecycle (trajectory assessed before current state, inside Assessor) + 4-role pipeline (Archivist/Assessor/Synthesizer/Publisher). Fixes R11 V-03's C-26/C-28 gap. Synthesizer introduces Co-Contribution Network Map. | Seeds D (severity tier), G (co-contribution network map with collaboration bridges) |
| **V-05** | Full integration — 4-role (Archivist/Analyst/Strategist/Narrator) + Sprint Velocity Dashboard + inertia severity tier + Inertia Cluster Table + reconciliation + confidence gate + `resolves:` + `requires:` + Co-Contribution Network Map. Maximum v12 seeding. | Seeds A+B+D+E+F+G |

---

### New seeds (v12 candidates)

| Seed | Candidate | What it captures | Presupposes |
|------|-----------|-----------------|-------------|
| D | v12-C-34 | Inertia severity tier column (`critical`/`warning`/`healthy`) per topic in inertia table — urgency classification beyond flag presence | C-27 |
| E | v12-C-35 | Narrator confidence gate: model emits `high`/`medium`/`low` confidence on its reconciliation pairing before writing the insight; insight must advance beyond the committed framing | C-27, C-31, C-33 |
| F | v12-C-36 | Action dependency chain: `requires: {action-N}` annotation for sequentially dependent actions — DAG structure for sprint sequencing | C-27 (via inertia flags driving dependency) |
| G | v12-C-37 | Co-contribution network map: contributor nodes + pair counts for all Team Topic topics + named collaboration bridges | C-09 presupposed |

Seeds A (C-32) and B (C-33) carried from R11, now formalized as explicit structural requirements across multiple variations rather than single-variation seeds.
