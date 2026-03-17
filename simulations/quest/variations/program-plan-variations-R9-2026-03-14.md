File written. Here's the R9 variate summary:

---

## program-plan R9 Variate — V-01 through V-05

All five inherit R8 V-05 ceiling (all of C-32/33/34/35). Three new single-axis variations, one combination, one ceiling:

| Variation | Axis | New Gate Format Elements | New Steps |
|-----------|------|--------------------------|-----------|
| **V-01** | Gate Entry Precondition | + `requires:` (entry evidence state) | +Step 10a |
| **V-02** | Semantic Gate Chain | `asserting:` + `(grounded-in:)` | modifies Step 10 |
| **V-03** | Gate Assertion Falsification | + `falsified-if:` (invalidation condition) | +Step 10a |
| **V-04** | V-01 + V-02 | `requires:` + `asserting: (grounded-in:)` | +Step 10a |
| **V-05** | V-01 + V-02 + V-03 + Program Arc | full format + `arc-asserts:` in YAML | +Steps 10a, 10b, 15a |

**Design family positions:**
- C-35 (`asserting:`) = gate post-condition. V-01 adds the pre-condition complement (`requires:`).
- C-27 (structural gate cascade chain) is now paralleled at the semantic level by V-02 (`grounded-in:`).
- V-03 turns C-35's declaration into a falsifiable claim (`falsified-if:`).
- V-05's `arc-asserts:` is the program-level analogue of C-35's gate-level assertion — the R10 anchor candidate.

**Expected R9 scoring pattern:** V-01/V-02/V-03 each pass one new axis; V-04 passes two; V-05 passes all three plus the R10 anchor. V-05 is the ceiling.
