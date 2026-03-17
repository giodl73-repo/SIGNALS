Written to `simulations/quest/golden/signal-variate-R13-2026-03-17.md`.

---

**R13 summary** -- 5 complete prompt bodies targeting C-39/C-40/C-41 independence:

| V | Axis | Change | Predicted |
|---|------|--------|-----------|
| V-01 | U only | Matrix cells -> gate-qualified Ch# (e.g. `Ch1`, `Ch2`) | 99.39 |
| V-02 | V only | Check 4 labels -> `Header:` / `Separator:` / `Footer:` | 99.39 |
| V-03 | W only | BARE Check 3 -> absolute offsets (`lines 1-8`, `lines 9-12`...) | 99.39 |
| V-04 | U+V | Matrix Ch# + labeled Check 4 | 99.70 |
| V-05 | U+W | Matrix Ch# + absolute offsets | 99.70 |

**Axis-specific changes** (all other sections identical):
- **U (C-39)**: Replaced criterion-ID matrix cells (`C-25`, `C-34`...) with gate-qualified check numbers (`Ch1`, `Ch2`, `Ch3`, `Ch4`). 11 applicable cells all annotated.
- **V (C-40)**: Replaced numbered `(1)(2)(3)` sub-element labels in FULL Check 4 with explicit named labels `Header:` / `Separator:` / `Footer:`.
- **W (C-41)**: Replaced relative incremental BARE Check 3 notation (`first 8, next 4, next 4...`) with precomputed absolute offsets (`lines 1-8`, `lines 9-12`, `lines 13-16`... through `lines 58-61`).

If independence holds: V-06 (U+V+W) saturates v13 at 100.00.
