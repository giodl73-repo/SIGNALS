Written to `simulations/quest/golden/crew-review-variate-R9-2026-03-16.md`.

---

**What changed R8 -> R9:**

R8 V-01 scored 157.5 (C-26 PASS, C-27 FAIL). R8 V-02 scored 157.5 (C-27 PASS, C-26 FAIL). R8 V-04 combined them but its criterion-check table was labeled "through v7" and stopped at C-25 -- meaning under rubric v8, it still fails C-26 because C-26 now requires the table to include C-26 and C-27 as rows.

R9 attacks three distinct paths to close that gap:

| V | Axis | What changes | Target |
|---|------|-------------|--------|
| V-01 | Lifecycle emphasis | Criterion-check table adds C-26 and C-27 rows; C-27 row creates revision obligation if synthesis is minimum-count | C-26 via force-function |
| V-02 | Output format | R3 synthesis is per-slot explicit contract; table stops at C-25 | C-27 via direct text |
| V-03 | Role sequence | Verbatim `expertise.relevance` quotes in manifest + L5 verification | C-28 candidate |
| V-04 | Lifecycle + Output format | V-01 table + V-02 explicit R3 synthesis | C-26 + C-27 = 160/160 |
| V-05 | Lifecycle + Output format + Role sequence | V-04 + verbatim quotes | C-26 + C-27 + C-28 |

**Key structural insight for R9:** The criterion-check table containing a C-27 row is not a passive record -- it is an execution contract. If synthesis is minimum-count, the C-27 row scores NO, which triggers the "return to relevant phase and revise" instruction. V-01 tests whether this force-function alone is sufficient to achieve C-27 without changing the R3 text. V-04 uses both paths.

**Predicted scores under v8:**
- V-01: 160 if the force-function works; 157.5 if the model satisfies C-26 (self-referential table) but minimum-count synthesis slips through without triggering revision
- V-02: 157.5 (C-27 PASS via explicit R3 text; C-26 FAIL -- table stops at C-25)
- V-03: 157.5 (C-28 candidate established; C-26 and C-27 state unchanged from base)
- V-04: 160 (belt-and-suspenders: table self-referential + R3 explicit per-slot)
- V-05: 160 + C-28 if verbatim quotes produce the new pattern without degrading V-04's properties
