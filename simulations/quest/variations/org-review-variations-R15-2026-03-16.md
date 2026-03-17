Written to `simulations/quest/golden/crew-review-variate-R15-2026-03-17.md`.

---

## org-review -- Variate R15 Summary

**Design target**: Combine V-05 R11's §14/§15/§16 contracts (C-30+C-31+C-32 PASS, 210/225) with V-02 R12's three new criteria (C-33+C-34+C-35). Perfect 225/225 for the first time.

**Variation plan:**

| Variant | Axis | C-33 | C-34 | C-35 | Predicted |
|---------|------|------|------|------|-----------|
| V-01 | Inertia framing | FAIL | vacuous | **PASS** | 215 |
| V-02 | Output format | **PASS** | FAIL | FAIL | 215 |
| V-03 | Lifecycle emphasis | **PASS** | **PASS** | FAIL | 220 |
| V-04 | Inertia + Output | **PASS** | FAIL | **PASS** | 220 |
| V-05 | All three axes | **PASS** | **PASS** | **PASS** | **225** |

**What each axis adds:**

- **Inertia framing (C-35)**: `NULL HYPOTHESIS DIMENSION TABLE` at BRACKET OPENING — current-state vs proposed-state per dimension, g_null derivable from table values alone.
- **Output format (C-33)**: `Applicability` column added to LENS COVERAGE TABLE (HIGH/MEDIUM/LOW per-artifact rating); preamble pre-commits coverage tier expectations per applicability level.
- **Lifecycle emphasis (C-34)**: `§17 DOMAIN COVERAGE GAP-CHECK PROTOCOL` + `§9.5` section after LENS COVERAGE TABLE; identifies artifact domains with no HIGH-applicability reviewer; ADVISORY-GAP items promoted to ACTION ITEM REGISTER.

**C-34 dependency note**: C-34 is vacuous when C-33 is FAIL (no HIGH-applicability tier to check against). V-03 includes C-33 as a structural precondition for C-34 — the "lifecycle emphasis" axis covers both. This matches the V-02 R12 canonical pattern where C-34 and C-33 co-appeared.
