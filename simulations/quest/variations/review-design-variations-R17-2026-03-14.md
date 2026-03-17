Written to `simulations/quest/rubrics/review-design-variate-R17-2026-03-15.md`.

---

# review-design — Round 17 Variations
**Rubric version**: v16 (C-01–C-49, denominator 42)
**Baseline**: R16 V-05

**Single-axis plan**: V-01 (C-47), V-02 (C-48), V-03 (C-49)
**Combination plan**: V-04 (C-47 + C-48), V-05 (C-47 + C-48 + C-49 — ceiling)

---

## Variation Map

| V | Axis | Criteria | Baseline | Key change |
|---|------|----------|----------|------------|
| V-01 | Lifecycle emphasis | C-47 | R16 V-01 | F-31 added to BLOCK 3 body + SEALED; BLOCK 2.7 gap retained |
| V-02 | Output format | C-48 | R16 V-04 | BLOCK 2.7 SEALED adds F-29 + F-30; C-47 already carried |
| V-03 | Phrasing register | C-49 | R16 V-02 | BLOCK 5 CONSENSUS ELEVATION RULE converted to numbered algorithm + non-conformance prohibition |
| V-04 | C-47 + C-48 | C-47 + C-48 | R16 V-01 | F-31 + BLOCK 2.7 F-29/F-30 fix; C-49 prose |
| V-05 | All three | C-47 + C-48 + C-49 | R16 V-05 | BLOCK 2.7 SEALED adds F-29/F-30 invariant descriptions |

---

## Encoding delta per new criterion

**C-47** (V-01, V-04, V-05): F-31 constraint bullet in BLOCK 3 Elevation Record section; F-31 named in BLOCK 3 SEALED.

**C-48** (V-02, V-04, V-05): BLOCK 2.7 SEALED updated from `"F-28 resolves against this registry exclusively"` to enumerate all three applicable gates — F-29 (no spurious entries), F-30 (registry present in conformant position), F-28 (BLOCK 5 Section validation gate). This is the only change needed in V-05: every other block's SEALED was already complete in R16 V-05.

**C-49** (V-03, V-05): BLOCK 5 prose rule replaced by a three-step numbered algorithm: ELEVATED tier → ranks 1..n by Amendment Cost then reviewer count; BASELINE tier → ranks n+1..P1_count same keys; no ties. Closing sentence: `"Re-assessing consensus status at BLOCK 5 generation time is non-conformant."` V-03 tests this in isolation (no SEALED, no F-31); V-05 carries it in the ceiling.

---

## Key diagnostic predictions

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-47 | PASS | PASS | FAIL | PASS | PASS |
| C-48 | FAIL (BLOCK 2.7) | PASS | FAIL | PASS | PASS |
| C-49 | FAIL | FAIL | PASS | FAIL | PASS |

V-01 is the C-47 isolation test — C-48 should score the BLOCK 2.7 gap exactly.
V-02 is the C-48 completion test — the BLOCK 2.7 fix is the only delta from R16 V-04.
V-03 confirms C-49 is independently testable without SEALED infrastructure.
V-05 is the first variation expected to pass all three simultaneously.
