Written to `simulations/quest/rubrics/trace-request-rubric-v10-variate-R11-2026-03-15.md`.

---

## R11 Variation Summary

| V | Axis | C-28 | C-29 | C-30 | New signal | Predicted |
|---|------|------|------|------|------------|-----------|
| **V-01** | Regression: C-28 advisory | FAIL | PASS | FAIL | none | 195/205 |
| **V-02** | Regression: C-29 advisory | PASS | FAIL | FAIL | none | 195/205 |
| **V-03** | Lifecycle: contradiction halt | PASS | PASS | PASS | C-31 candidate: contradiction is a **named halt type** with required Rem# format | 205/205 |
| **V-04** | Role sequence: Step 8 scope-token re-affirmation | PASS | PASS | PASS | C-31 candidate: Step 8 header makes Match? computation **self-contained** (no other section needed) | 205/205 |
| **V-05** | Combination V-03 + V-04 | PASS | PASS | PASS | C-31 candidate: **automated enforcement pre-conditions** established — reference set (header) + halt type + Rem# format all present | 205/205 |

---

**Single-axis coverage:**

- **V-01** isolates C-28 by softening Step 8b to a NOTE — C-29 table remains REQUIRED, so if V-01 scores 195 that confirms C-28 and C-30 are jointly load-bearing and independently accountable from C-29.
- **V-02** isolates C-29 by softening Step 8c to advisory — Step 8b gate remains REQUIRED, so if V-02 scores 195 that confirms C-29 and C-30 are jointly load-bearing and independently accountable from C-28.
- **V-03** introduces the CONTRADICTION HALT as a typed structural event (`CONTRADICTION SIGNAL: Seq# N`) with a required `Scope String Correction` Rem# mechanism. This is the C-31 pre-condition: the halt is machine-detectable (look for "Coherence confirmed" at Seq# N + Match? = N at Seq# N) and produces a required output in a named format.

**The C-31 design surface (V-04/V-05):** The Step 8 Header re-affirmation creates a co-located reference set. A downstream checker needs only (a) the header VT# token list and (b) the Step 8c table to compute all Match? values without reading Steps 0, 3, or 11. V-05 combines that with the contradiction halt — if both properties appear consistently across R11 rounds, the automated-check predicate is specifiable.
