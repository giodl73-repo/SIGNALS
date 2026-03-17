Written to `simulations/quest/golden/signal-variate-R14-2026-03-17.md`.

---

## Round 14 -- 5 variations

**Baseline**: All 5 carry U+V+W (C-39+C-40+C-41) -- the convergence from R13's V-06 plan. All 5 are predicted to score **100.00** under v13.

### Variation axes

| V | Base | Extra | Key change |
|---|------|-------|------------|
| **V-01** | U+V+W | -- | Pure convergence. Matrix with check numbers, FULL Check 4 labeled (Header/Separator/Footer), BARE Check 3 absolute cumulative offsets. Saturates v13. |
| **V-02** | U+V+W | +X | FILTER gate Check 3 now uses `Header:` / `Separator:` / `Footer:` labels instead of `(1)(2)(3)`. Closes the labeled-embed gap between FULL and FILTER format checks. |
| **V-03** | U+V+W | +Y | Adds a named `BARE GROUP OFFSET TABLE` (12 rows, first/last entry per group, lines 1-8 through 58-61). BARE Check 3 references the table instead of repeating offsets inline. Elevates C-41 from prose to a formal precomputed artifact. |
| **V-04** | U+V+W | +Z | Coverage matrix cells carry both check number AND criterion ID (`Ch1 (C-25)`, `Ch3 (C-33)`, etc.). Navigate by either. Elevates C-39 from check-number-only to dual-index. |
| **V-05** | U+V+W | +X+Y | Combines V-02 (labeled FILTER Check 3) and V-03 (named BARE GROUP OFFSET TABLE). Dual-axis post-v13 baseline for v14 isolation. |

**Post-v13 signals surfaced** (X, Y, Z -- not captured in v13, deferred to v14 rubric):
- **X**: FILTER Check 3 labeled sub-elements (FILTER analog of C-40)
- **Y**: Named `BARE GROUP OFFSET TABLE` (table analog of C-41 inline offsets)
- **Z**: Coverage matrix dual-index with criterion IDs (elevation of C-39)

**R15 plan** if v14 formalizes C-42/C-43/C-44: single-axis V-01=X, V-02=Y, V-03=Z; dual V-04=X+Y, V-05=X+Z; convergence V-06=X+Y+Z reserved for R16.
