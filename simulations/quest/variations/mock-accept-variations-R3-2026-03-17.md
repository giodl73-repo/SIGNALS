**5 variations written** to `simulations/quest/golden/mock-accept-variate-R3-2026-03-17.md`

---

## R3 Axis-Assignment Plan

| Variation | Axis | New criteria targeted | Predicted ceiling |
|-----------|------|----------------------|-------------------|
| **V-01** | Lifecycle emphasis | C-16 (written-gate blocking), C-17 (named gate registry GATE A–F) | 88.0 |
| **V-02** | Phrasing register | C-15 (forbidden-form enumeration in standing rule), C-10 (tier sourcing fix) | 88.0 |
| **V-03** | Output format | C-18 (constraint co-located with field, no intervening prose), C-14 (blank `___` slots) | 88.0 |
| **V-04** | Lifecycle + Phrasing | C-10, C-15, C-16, C-17 — V-01 gate structure + V-02 forbidden-form | 94.0 |
| **V-05** | Full integration | C-10, C-14, C-15, C-16, C-17, C-18 — all new criteria + both R2 gaps | 100.0 |

---

## Key design decisions

**V-01 vs V-03 distinction**: V-01 restructures phase *transitions* into named GATE A–F records (C-17); V-03 restructures field *templates* so constraints sit adjacent to fill-ins (C-18). These are structurally non-overlapping — phase headers vs field bodies.

**C-18 implementation** (V-03, V-05): Every fill-in target has its `CONSTRAINT:` line immediately after it with zero intervening prose. The R2 pattern of preamble instructions + downstream templates violates C-18 wherever the constraint is not adjacent. V-05 tests whether this discipline holds across all 6 phases without slippage.

**C-15 vs C-09**: C-09 requires a standing rule; C-15 requires that standing rule to name the forbidden alternatives. V-02 adds the `FAIL forms:` enumeration to the existing V-01 standing rule — the positive form is unchanged, the forbidden forms are added alongside it.

**V-05 reference loop**: The review artifact (Phase 6) is instructed to cite "GATE C Arch-blocked list" and "GATE D" by name — this closes the C-17 referenceable-registry property at the output level, not just the instruction level.

**Testable failure prediction for V-05**: C-18 is the hardest criterion because any single preamble-only constraint anywhere in the prompt is a violation. If V-05 fails C-18 but passes C-15/C-16/C-17, the next round should isolate co-location as a single-axis variation.
