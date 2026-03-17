Written to `simulations/quest/golden/flow-conversation-variate-R4-2026-03-15.md`.

---

## Round 4 Variation Map

| Variation | Axis | C-13 | C-14 | Predicted |
|-----------|------|------|------|-----------|
| **V-01** | Pre-instruction register only | PASS | FAIL | 120/125 |
| **V-02** | Per-section foil only | FAIL | PASS | 120/125 |
| **V-03** | Role sequence reversal (defect-first) | FAIL | FAIL | 115/125 |
| **V-04** | C-13 + C-14, no phase gates | PASS | PASS | 120/125 |
| **V-05** | Full ceiling — all five mechanisms | PASS | PASS | 125/125 |

---

## Design decisions per variation

**V-01 (C-13 only):** Scoring register is the first thing in the prompt — before role priming, before any instruction. Each table row has a named zero-point output (`"No significant issues found. Consider adding error handling."`). R3 V-03's phase gates retained verbatim for C-12. No foils distributed to individual sections, so C-14 FAIL.

**V-02 (C-14 only):** No pre-instruction table. Each phase opens with `"A first-pass X would say: '...'"` before the exit condition. Five phases, five foils — each foil is a specific output instance, not a generic prohibition. C-13 FAIL because the bad-form examples are distributed per-section rather than gathered into a pre-instruction register.

**V-03 (role sequence reversal):** The hypothesis-before-trace ordering is new to the series. PHASE 1 is a defect hypothesis table (candidate nodes, suspected conditions, confidence). PHASE 4's exception path is explicitly directed to route through the Phase 1 candidate to confirm or refute. No new C-13/C-14 mechanisms — this is a control variation testing whether cognitive reordering alone preserves the existing 115 floor.

**V-04 (C-13 + C-14, no gates):** Pre-instruction register + per-section foils active simultaneously. Phase exit conditions deliberately removed. Tests whether the two new mechanisms reach 120 without phase gate infrastructure — and confirms C-12 as independently load-bearing.

**V-05 (full ceiling):** The scoring register's zero-point column and the per-section foils both contain named bad-form examples — the prohibitions are duplicated at two structural levels. Phase exit conditions add a third level. The combination closes three escape routes independently: artifact-opening frame, section-opening frame, and phase-completion gate.
