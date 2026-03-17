Written to `simulations/quest/golden/topic-plan-variate-R13-2026-03-15.md`.

---

## Round 13 — V-01 through V-05

**Three gaps from R12, three single-axis variations, two combinations:**

| Variation | Axis | Mechanism | Criteria |
|-----------|------|-----------|----------|
| V-01 | Lifecycle emphasis | `Gate-0 --` prefix in section header | C-44 only |
| V-02 | Output format A | Phase 2/3/5 gates name each column individually (`[2a][2b][2c]`, `[5a]–[5f]`) | C-43 only |
| V-03 | Output format B | CONTRACT COMPLETENESS GATE splits check [A] into [A1]–[A8], one per §ID | C-45 only |
| V-04 | Combined lifecycle + format A | V-01 header + V-02 column gates | C-44 + C-43 |
| V-05 | Combined all three | V-01 header + V-02 column gates + V-03 per-§ID schema atomicity | C-44 + C-43 + C-45 |

**Key structural changes vs R12:**

- **C-44 fix** (V-01, V-04, V-05): `CONTRACT COMPLETENESS GATE` → `Gate-0 -- CONTRACT COMPLETENESS GATE`; condition label → `[GATE-0: PASS/STOP ...]`
- **C-43 fix** (V-02, V-04, V-05): Phase 2 gate changes from `all 9 namespace rows present` to `namespace column [2a] + total-artifacts column [2b] + new column [2c] all non-null across all 9 rows`; same column-by-name pattern in Phase 3 and Phase 5 (6-column check on §6)
- **C-45 fix** (V-03, V-05): Check [A] (4-item gate, 8 §IDs bundled) → [A1]–[A8] + [B][C][D] = 11 items, count equals schema count
