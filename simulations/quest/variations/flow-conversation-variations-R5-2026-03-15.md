Written to `simulations/quest/golden/flow-conversation-variate-R5-2026-03-15.md`.

---

## Round 5 Variation Map

| Variation | Axis | C-13 | C-14 | C-15 | C-12 | Predicted |
|-----------|------|------|------|------|------|-----------|
| V-01 | C-15 only + base mechanisms | FAIL | FAIL | PASS | PASS | 120/130 |
| V-02 | C-15 + C-13 (hypothesis + register) | PASS | FAIL | PASS | PASS | 125/130 |
| V-03 | C-15 + C-14 (hypothesis + foils) | FAIL | PASS | PASS | PASS | 125/130 |
| V-04 | C-15 + C-13 + C-14 without phase gates | PASS | PASS | PASS | FAIL | 125/130 |
| V-05 | All six mechanisms | PASS | PASS | PASS | PASS | 130/130 |

---

**Design rationale:**

**V-01** cleanly isolates C-15 from R4 V-03's noise — same defect-first structure, same base mechanisms, no register or foils. Establishes the C-15 floor at 120/130 before any combination.

**V-02 and V-03** are single-addition tests. V-02 adds C-13 (pre-instruction register) to V-01; V-03 adds C-14 (per-section foils) to V-01. Each should land at 125/130, confirming independence in both directions. The key structural distinction is preserved: V-02's zero-point examples are gathered into one pre-instruction table; V-03's foils are distributed to open each individual phase.

**V-04** tests whether the three meta-cognitive mechanisms (predict, frame, challenge) together reach 125 *without* the phase gate infrastructure. If V-04 = 125/130 with C-12 FAIL, it confirms all three C-15/C-13/C-14 mechanisms are independently load-bearing and that C-12 stays isolated. If V-04 < 125, something in the cluster degrades without the MAY NOT scaffold.

**V-05** is the expected ceiling proof. Six mechanisms close six escape routes at different structural levels: before any instruction (C-13), before each section (C-14), before any trace (C-15), at each phase exit (C-12), in every column header (C-11), and via named examples (C-10).
