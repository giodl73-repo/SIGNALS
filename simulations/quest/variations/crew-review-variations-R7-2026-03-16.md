Written to `simulations/quest/golden/crew-review-variate-R7-2026-03-16.md`.

---

# crew-review -- Variate R7

5 complete prompt body variations targeting the three open gaps from R6: C-22 (slot-anchored matrix), C-23 (validation as named phase), and C-12 (per-role lens-lock — failed every prior round).

## Variation axes

| Variation | Axis | C-22 | C-23 | C-12 | C-19 |
|-----------|------|------|------|------|------|
| **V-01** | Role sequence: Slot as typed schema column with downstream reference obligation | Target | — | — | — |
| **V-02** | Lifecycle: Named VALIDATE phase + Lens as typed column | — | Target | Target | Target |
| **V-03** | Output format: Lens column (isolated single axis) | — | — | Target | Target |
| **V-04** | Slot-anchored + Named VALIDATE (two axes) | Target | Target | — | — |
| **V-05** | Slot + VALIDATE + Lens maximal (three axes, full stack) | Target | Target | Target | Target |

## Key mechanism differences from R6

**V-01** strengthens C-22 over R6 V-03: the Slot column is a typed schema column with a typed contract, and synthesis/AMEND are given explicit output contracts requiring slot-number references — not a convention arising from the manifest architecture.

**V-02** adds Lens as a typed column to R6 V-02's five-phase structure: Lens is no longer an execution instruction but a required schema cell, with anti-pattern exclusion ("NOT: generic role restatements") in the column definition.

**V-03** isolates the Lens-column mechanism cleanly: 5-column schema (Role, Lens, Findings, Severity, Recommendation), per-row validation gate on Lens, no confounding slot/phase changes.

**V-04** is the first variation designed to achieve C-22 + C-23 simultaneously, testing their structural independence (matrix-schema vs. execution-model properties).

**V-05** is the maximal three-axis combination targeting C-22 + C-23 + C-12 with a 6-column schema, PHASE 4 VALIDATE, slot manifest, and a PHASE 4 criterion-check table over the full C-11 through C-23 aspirational stack.
