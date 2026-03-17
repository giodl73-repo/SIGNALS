Written to `simulations/quest/golden/mock-review-variate-R20-2026-03-16.md`.

---

## R20 Variate Summary

**What R19 left open:** R19 established the three C-42 levels (PASS/PARTIAL/FAIL) through observation. R20's job is to confirm those levels are stable properties of the *labeling pattern* — not artifacts of role ordering — and to exercise the belt-and-suspenders ceiling the v20 definition explicitly names as still-PASS.

### Variation matrix

| Var | C-42 | C-43 | Role seq | Primary axis | What it tests |
|-----|------|------|----------|--------------|---------------|
| V-01 | **PARTIAL** | PASS | Arch-first (C-36 ✓) | C-42 level × role seq | PARTIAL boundary holds under Arch-first: TRIAD header is the sole unlabeled element regardless of ordering |
| V-02 | **FAIL** | PASS | Strat-first (C-35 ✓) | C-42 level × role seq | FAIL floor holds under Strat-first: minimal labeling (template slots only) is the floor regardless of ordering |
| V-03 | PASS | PASS | Arch-first (C-36 ✓) | Inertia framing (heavy) | Named RESISTANCE CHECK block with 3-item checklist; inertia axis is independent of labeling level |
| V-04 | PASS | PASS | Strat-first (C-35 ✓) | Phrasing register (conversational) | Explanatory/descriptive register preserves `[C-NN]` comment annotations and Row # column; register is orthogonal to both C-42 and C-43 |
| V-05 | **PASS + belt-and-suspenders** | PASS | Arch-first (C-36 ✓) | Lifecycle emphasis + ceiling | Per-row `[C-15]` in SQ table cells: explicitly redundant per v20, still PASS; lifecycle phase rationale commentary compatible with full coverage |

### Single-axis choices (V-01, V-02, V-03)
- **V-01 / V-02** — Role sequence as the varying dimension, holding C-42 level constant at PARTIAL/FAIL respectively. Confirms levels are a labeling property, not an ordering property.
- **V-03** — Inertia framing as the varying dimension; C-42/C-43 held at PASS. The RESISTANCE CHECK expands DEFAULT DECISION POSITION from a paragraph to a 3-item mechanical checklist.

### Combined axes (V-04, V-05)
- **V-04** — Phrasing register + role sequence. The `<!-- C-42: ... -->` annotations and `| Row # |` columns survive a shift from imperative commands to explanatory prose — confirming those are formatting elements, not style elements.
- **V-05** — Lifecycle emphasis + belt-and-suspenders ceiling + role sequence. Each step gains a `Lifecycle role:` rationale sentence. Per-row cell annotations appear in all three SQ tables to explicitly exercise the v20 "still-PASS" ruling.
