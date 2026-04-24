Written to `simulations/quest/golden/corps-committee-variate-R3-2026-03-16.md`.

**R3 summary:**

| ID | Axis | New criterion targeted |
|----|------|------------------------|
| V-01 | Pre-skeleton rule block | C-12 |
| V-02 | Rewrite-before-proceed loop | C-13 |
| V-03 | Coupling integrity symmetry declaration | C-14 |
| V-04 | Pre-skeleton rule block + Rewrite-before-proceed | C-12 + C-13 |
| V-05 | Full integration | C-12 + C-13 + C-14 |

**Key mechanism differences from R2:**

- **V-01** adds a 7-rule `CONSTRAINTS` block before STEP 1 — the model reads commit placement, sealing contracts, and coupling integrity before the skeleton exists in context.
- **V-02** introduces `*** REWRITE PROTOCOL ***` with explicit STOP / Discard / Replace language — eliminates the incremental-append failure where findings get appended below the old attempt.
- **V-03** adds a named `SYMMETRY DECLARATION` block pairing COUPLING PAIR A (Phase 1) with COUPLING PAIR B (Phase 3), plus an inline `SYMMETRY CHECK` section in the skeleton itself that must be ticked before Phase 4 can proceed.
- **V-04 / V-05** are the combinations — each mechanism addresses an independent failure mode, so co-presence is additive.
