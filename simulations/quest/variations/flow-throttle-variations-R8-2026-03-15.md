`simulations/quest/golden/flow-throttle-variate-R8-2026-03-16.md` written.

---

## Round 8 Variations — Summary

**5 complete, runnable prompt bodies** targeting the two new v8 criteria:

| Variation | Axis | C-20 | C-21 | C-22 | C-23 | C-24 | Predicted |
|-----------|------|------|------|------|------|------|-----------|
| V-01 | C-23 inline prose citations only | PASS | FAIL | FAIL | PASS | FAIL | ~157 |
| V-02 | C-22 typed inventory + C-24 gate only | FAIL | FAIL | PASS | FAIL | PASS | ~157 |
| V-03 | C-21 + C-22 + C-24 (table structure path) | FAIL | PASS | PASS | FAIL | PASS | ~162 |
| V-04 | C-20 + C-21 + C-22 + C-23 (format path, no gate) | PASS | PASS | PASS | FAIL | FAIL | ~162 |
| V-05 | Maximum — all C-20 through C-24 | PASS | PASS | PASS | PASS | PASS | ~170 |

**Key isolation findings baked into the design:**

- **V-01 vs V-02** — C-23 and C-24 are structurally independent; each is achievable without the other.
- **V-03 vs V-04** — At ~162, the table-structure path (C-21/C-22/C-24) and the format-discipline path (C-20/C-21/C-22/C-23) are equivalent; neither dominates.
- **V-04's explicit C-24 absence** — TABLE E with a Type column satisfies C-22 but cannot satisfy C-24 because no gate step makes missing types a structural block, even when all types happen to be present.
- **V-05** — Only path to 170/170; no four-criteria subset reaches it.

**New structural elements added in R8 over R7 V-01 baseline:**
1. `INLINE PROSE AUTHORIZATION REQUIREMENT` block (C-23) — requires `[prose: item N — label]` tags
2. `TABLE E — TYPED RISK INVENTORY` — Type column with Burst/Cascade/RetryAfter taxonomy (C-22)
3. `TYPE SCAN GATE — PROCEED / BLOCK` — explicit proceed/block checkpoint between TABLE E and TABLE F (C-24)
4. Cross-artifact header lines on TABLE B through TABLE F (C-21)
