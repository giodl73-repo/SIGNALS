Written to `simulations/quest/golden/campaign-brief-variate-R9-2026-03-16.md`.

---

## campaign-brief / Round 9 — Variation Summary

**Base:** R8 V-05 (expected 260/260 — all three of C-24/C-25/C-26 implemented)

**R9 investigation targets from rubric:**
1. Does C-25's named-rule form survive higher token pressure?
2. Does C-26's `action:` sub-label survive when COMPRESSED + last-block VERDICT interact?

---

### Axes and hypotheses

| Var | Axis | Mechanism | Expected |
|-----|------|-----------|----------|
| **V-01** | C-25 token-pressure guard | Adds a third clause to the ZERO-SIGNAL SYNTHESIS RULE: "this rule fires unconditionally at any token budget — stated here to prevent conditional-context suppression when `found` is large, not as evidence of non-applicability." Rule stays mid-document. | C-24 P / C-25 P / C-26 P = 260 |
| **V-02** | C-26 COMPRESSED x VERDICT guard | Adds a VERDICT COMPRESSION GUARD in the VERDICT execution note: "`action:` sub-labels are required regardless of COMPRESSED state — VERDICT is never abbreviated." C-25 stays at R8 V-05 mid-document form. | C-24 P / C-25 P / C-26 P = 260 |
| **V-03** | C-25 preamble placement | Moves the ZERO-SIGNAL SYNTHESIS RULE to before "Run the phases in order" — global-constraint position, processed before the model enters block-execution mode. No token-pressure guard clause; the position is the mechanism. | C-24 P / C-25 P / C-26 P = 260 |
| **V-04** | C-25 pressure guard + C-26 VERDICT guard | V-01 + V-02 combined, no preamble placement. Tests additivity of both guards. | 260 if independent; lower reveals interaction |
| **V-05** | Full R9 sweep | Preamble placement (V-03) + token-pressure guard clause (V-01) + VERDICT compression guard (V-02). Ceiling candidate. | 260 if non-conflicting |

**Falsification logic:**
- If V-01 FAIL → position is the variable, not the guard clause → V-03 is the primary mechanism
- If V-02 FAIL → budget depletion at VERDICT, not instruction inference → R10 target is VERDICT block elevation
- If V-05 < V-03 or V-04 → preamble instruction budget is consuming model attention before VERDICT → R10 target is preamble length reduction or pre-VERDICT standalone note
