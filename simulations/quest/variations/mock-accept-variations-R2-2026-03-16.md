Written to `simulations/quest/golden/mock-accept-variate-R2-2026-03-16.md`.

---

## Summary

5 complete variations produced. Axis assignments for R2:

| V | Axis | Single/Combined | Primary target |
|---|------|-----------------|----------------|
| V-01 | phrasing-register | single | C-12 — Slot 2 before Slot 1 via imperative mandate + template reorder |
| V-02 | output-format | single | C-13 — SKIP cells in evaluation table; partial SKIP = contamination |
| V-03 | lifecycle-emphasis | single | C-11 — bypass error codes as explicit `bypass-error-code:` output fields |
| V-04 | phrasing-register + output-format | combined | C-12 + C-13 — non-overlapping regions, additive |
| V-05 | output-format + phrasing-register + lifecycle-emphasis | combined | C-11 + C-12 + C-13 + R1 phase scaffold carried forward |

Key structural deltas from the R1 baseline:
- **V-01**: only MOCK-ACCEPTED template changes — Slot 2 label moves above Slot 1 + `WRITE CONTRAST SLOT FIRST` imperative + `SLOT-ORDER-INVERSION` error name
- **V-02**: Steps 3–5 collapse into a single evaluation table; SKIP fills all three role columns for auto-flagged rows simultaneously
- **V-03**: Each step-transition guard adds a `bypass-error-code:` field to the blocked-list record format; empty-blocked case must state "not triggered"
- **V-04**: V-02 table + V-01 slot reorder, nothing else changed
- **V-05**: V-03 bypass fields + V-04 (table + slot reorder) + R1 named-phase STOP-gate scaffold as the outer wrapper
