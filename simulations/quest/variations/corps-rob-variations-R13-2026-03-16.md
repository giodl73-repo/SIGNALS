Written to `simulations/quest/golden/corps-rob-variate-R13-2026-03-17.md`.

---

## R13 Variations Summary

| Variation | Axis | C-35 | C-40 | C-41 | C-42 | Expected |
|-----------|------|------|------|------|------|----------|
| **V-01** | C-42 inline criterion enumeration | FAIL | PASS | -- | **PASS** | 245/260 |
| **V-02** | C-35 + C-41 clean reproduction | PASS | FAIL | **PASS** | -- | 245/260 |
| **V-03** | Imperative-register + GLOSSARY-GOVERNED CRITERIA block | FAIL | PASS | -- | **PASS** | 245/260 |
| **V-04** | V-01 + V-02 combined | PASS | PASS | **PASS** | **PASS** | 255/260 |
| **V-05** | V-04 + RULE IB-URGENCY-CASCADE | PASS | PASS | **PASS** | **PASS** | 260/260 |

---

**Three single-axis variations:**

- **V-01** adds named-criterion enumeration to R12 V-01's existing exclusivity preamble -- the minimal change to push C-40 past the C-42 threshold. Tests whether inline criterion sentences satisfy C-42.
- **V-02** reproduces R12 V-02's C-35 + C-41 in isolation, verifying the signal is stable before combining with C-42.
- **V-03** tests the same C-42 target via a different structural approach: a dedicated `GLOSSARY-GOVERNED CRITERIA` block with `SHALL NOT / MUST` phrasing, rather than inline sentences. The V-01 vs V-03 comparison will reveal which C-42 signal is more reliable.

**Two combination variations:**

- **V-04** is the minimum-change path to all four v13 target criteria simultaneously -- V-01's preamble + V-02's RULE AUDIT-TABLE, no other changes.
- **V-05** adds `RULE IB-URGENCY-CASCADE` to the glossary for C-39 reliability, plus a temporal `Urgency Gradient` field on IB-02. Targets 260/260 under v13.
