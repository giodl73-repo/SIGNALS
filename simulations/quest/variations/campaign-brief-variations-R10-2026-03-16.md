---

# Variations -- campaign-brief / Round 10

Written to `simulations/quest/variations/campaign-brief-variations-R10-2026-03-17.md`.

---

## Summary

**R10 investigation:** C-29's dual-mechanism independence requirement — the rubric v9 requires BOTH positional (preamble) AND declarative (named guard) mechanisms on the same compression-critical rule. R9 could not distinguish V-04 (mid-doc + both guards) from V-05 (preamble + both guards) because both hit the v8 ceiling. R10 isolates the two mechanisms.

| Variation | Axis | C-27 | C-28 | C-29 | Predicted |
|---|---|---|---|---|---|
| **V-01** | Preamble-only, no TOKEN-PRESSURE GUARD | PARTIAL | PASS | PARTIAL | 270/290 |
| **V-02** | Declarative-only (mid-doc guard, no preamble) | PASS | PASS | PARTIAL | 280/290 |
| **V-03** | C-29 generalized to VERDICT action: rule | PASS | PASS | PASS or PARTIAL | 280-290/290 |
| **V-04** | R9 V-05 form (preamble + guard, VERDICT guard) | PASS | PASS | PASS | 290/290 |
| **V-05** | Dual-mechanism on BOTH compression-critical rules | PASS | PASS | PASS | 290/290 |

**Falsification logic:**
- If V-01 scores C-29 PASS → preamble alone is sufficient → criterion should be narrowed
- If V-02 scores C-29 PASS → declarative guard alone is sufficient → criterion should be narrowed
- If both V-01 and V-02 score C-29 PARTIAL → independence requirement is validated → V-04/V-05 combined form is genuinely necessary

**V-03 secondary test:** Whether C-29 credit is earnable by applying dual-mechanism to the VERDICT action: rule instead of the zero-signal rule. If V-03 = 290, C-29 is rule-agnostic; if V-03 = 280, C-29 requires the specific zero-signal + preamble pairing.

**V-05 excellence signal target:** Whether naming both compression-critical rules at preamble level with their failure-mode framing is a generalizable skill-architecture pattern worth a future criterion.
