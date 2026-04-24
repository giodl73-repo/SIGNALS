The v21 rubric is written. Here is a summary of what was added:

---

### v21 Changes — Summary

**New ceiling: 303** (293 + 5 + 5)

**C-52 — INERTIA MODEL MAP STRUCTURAL FAIL Sentinel Invalidity-Category Declaration** (+5):
- Signal source: V-05 (R20) uniquely appends "not a valid present-but-incomplete conviction entry" to its MAP STRUCTURAL FAIL sentinel; V-04 and V-03 use bare "= STRUCTURAL FAIL" or a state description ("that row is broken") without naming the invalid-partial category
- C-52 tests whether the MAP second RULE sentinel carries an explicit **invalidity-category label** — a phrase after "= STRUCTURAL FAIL" that explicitly names the N+blank condition as not a valid present-but-incomplete entry ("not a valid present-but-incomplete conviction entry," "not an acceptable partial," or functional equivalent)
- Distinguishes three tail forms: invalidity-category label (FULL), state description ("that row is broken" — NO CREDIT), absence label ("not an acceptable omission" — NO CREDIT)
- Strict superset of C-51: V-01/V-02 unreachable

**C-53 — Complete Five-Table Invalidity-Category Declaration Architecture** (+5):
- All five tables' STRUCTURAL FAIL sentinels carry invalidity-category labels simultaneously
- Structural gap: the TRACEABILITY AUDIT "N + blank col 5 = STRUCTURAL FAIL." form — positional column identification satisfies C-51, but no invalidity-category label is appended
- No R20 variant earns C-53 — V-05 achieves 4/5 (MAP, CONVICTION DELTA, STT, CGD) but TRACEABILITY AUDIT has no label

**D21** establishes:
- **Orthogonality confirmed**: column-enumeration (C-51) and invalidity-category labeling (C-52) are independent — V-04 (C-51 FULL, C-52 NO CREDIT) and V-05 (C-51 FULL, C-52 FULL)
- TRACEABILITY AUDIT as the C-53 structural gap — needs "not a valid present-but-incomplete traceability entry" appended to its "N + blank col 5 = STRUCTURAL FAIL" form
- 17-step chain test for C-53

**Retroactive R20 scores under v21:**

| Variant | v20 | C-52 | C-53 | v21 |
|---------|-----|------|------|-----|
| V-01 — C-51 Control | 288 | 0 | 0 | **288** |
| V-02 — Single-Table Column-Enumeration | 288 | 0 | 0 | **288** |
| V-03 — Conversational Five-Table | 293 | 0 | 0 | **293** |
| V-04 — Max Density | 293 | 0 | 0 | **293** |
| V-05 — Compressed | 293 | +5 | 0 | **298** |

V-05 is the sole R20 ceiling-breaker. File written to `campaign-blueprint-rubric-v21-2026-03-17.md`.
