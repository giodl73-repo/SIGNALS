# quest-score Variations -- Round 14

Generated `simulations/quest/golden/quest-score-variate-R14-variations-2026-03-15.md`.

---

## Design summary

**Base**: R13 V-01 architecture (C-33/C-36/C-37/C-38 PASS, C-34/C-35 FAIL open)
**Formula**: `aspirational_pass / 31 * 220` (v13, all five variations)

| Variation | Axis | C-34 | C-35 | Mechanism tested |
|-----------|------|------|------|-----------------|
| V-01 | NCA | PASS | FAIL | Terminal assertion "No prohibited content category lacks a named destination" appended to PROHIBITED list |
| V-02 | DSC | FAIL | PASS | Separate Type-level / Intra-run columns in VERIFIER TABLE; combined Specificity omitted |
| V-03 | TFS | FAIL | FAIL | Table-format SCORER (criterion rows instead of blocks); tests C-33/C-36/C-37/C-38 stability across schema format change |
| V-04 | NCA+DSC | PASS | PASS | Both mechanisms combined; R14 ceiling prediction 31/31 |
| V-05 | NCA+DSC+inertia | PASS | PASS | V-04 rewritten in inertia-framing register; each constraint named as an override of a specific model default |

**Single-axis logic**: V-01 and V-02 are the cleanest isolations. V-03 introduces the table-format question to test whether C-36/C-37/C-38 degrade when the SCORER surface changes -- potentially generating v14 criteria if a new excellence signal appears.

**Ceiling**: V-04 closes both open items simultaneously; V-05 tests whether the inertia-framing register produces measurably different execution behavior at the same structural ceiling.
