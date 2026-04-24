Written to `simulations/quest/golden/mock-ns-variate-R8-2026-03-15.md`.

---

## mock-ns -- Round 8 Variations

**Rubric**: v8 (C-01 through C-26, aspirational denominator 18)  
**New criteria**: C-25 (guarantee-break framing) + C-26 (cross-site reference), both compute-side refinements of C-23.

---

### Variation axes

| # | Axis | New criteria | Expected composite |
|---|------|-------------|-------------------|
| V-01 | Inertia framing (C-25 only) | C-25 | 17/18 ~= 99.4 |
| V-02 | Phrasing register (C-26 only) | C-26 | 17/18 ~= 99.4 |
| V-03 | Lifecycle emphasis (R7 baseline) | none | 16/18 ~= 98.9 |
| V-04 | Output format + role sequence (C-25 + C-26, table S-3) | C-25 + C-26 | 100 |
| V-05 | Role sequence (full convergence, prose) | C-25 + C-26 | 100 |

---

### What changes across variations

The single axis of variation is in **S-3's consequence sentence** -- the fragment appended after the C-21 affirmative closure ("Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt."):

| Variant | Consequence sentence form |
|---------|--------------------------|
| V-03 (baseline) | `...A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one.` |
| V-01 (C-25 only) | `...the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one.` |
| V-02 (C-26 only) | `...A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site.` |
| V-04/V-05 (both) | `...the guarantee stated above is broken: A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one, producing the same silent category mismatch described at the consumption site.` |

V-04 wraps S-3 flag cases in a table (output format axis). V-05 uses standard `STEP S-N` prose labels (role sequence / convergence axis).

---

### Key discriminant for R8

The primary empirical question is whether **C-25** (a logical connective, backward-pointing to C-21) or **C-26** (a navigational pointer, sideways to C-20) is the stronger standalone addition under execution pressure. R7 found C-23 was the stronger single addition over C-24. R8 puts two structurally different mechanisms -- logical bridge vs. cross-reference -- head-to-head for the first time.
