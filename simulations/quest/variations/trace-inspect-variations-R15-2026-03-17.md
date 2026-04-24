`C:\src\sim\simulations\quest\golden\trace-inspect-variate-R15-2026-03-17.md` written.

---

## R15 Summary

**Entry state**: R14 V-05 = 104.5/104.5 (rubric v10). Rubric v11 adds C-32 and C-33 (+0.5 each). Baseline = 104.5/105.5.

**What C-32/C-33 require** (the gap from R14 V-05):

| Criterion | Gap from R14 V-05 | What R15 must add |
|-----------|------------------|-------------------|
| C-32 | Item 11 describes count-substitution failure but never uses "ID substitution attack vector" as a named term; never says "closes C-30" | Named term + explicit closure declaration + *why* per-ID membership exists |
| C-33 | Item 12 describes forward-reference opacity but never uses "forward-reference opacity anti-pattern" as a named term; never says "closes C-31" | Named term + explicit closure declaration |

**Five variations**:

| Var | Axis | C-32 | C-33 | Notes |
|-----|------|------|------|-------|
| V-01 | Lifecycle emphasis | Leading label `ID SUBSTITUTION ATTACK VECTOR (closes C-30):` | unchanged | Single-axis, C-32 only |
| V-02 | Output format | unchanged | Leading label `FORWARD-REFERENCE OPACITY ANTI-PATTERN (closes C-31):` | Single-axis, C-33 only |
| V-03 | Phrasing register | Trailing assertion: "This is the ID substitution attack vector. C-30 closes this: ..." | Trailing assertion: "This is the forward-reference opacity anti-pattern. C-31 closes this: ..." | Tests whether trailing form satisfies vs leading |
| V-04 | Combined | V-01 leading label | V-02 leading label | Predicted golden |
| V-05 | Full integration | V-01 + registry cites item 11 | V-02 + registry cites item 12 | Predicted golden, durability advantage |

**Predicted outcome**: V-04 and V-05 both score 105.5/105.5. V-03 is the risk variation -- trailing assertions may pass C-32/C-33 nominally (term present, closure declared) but lack label-scan confirmability, which the rubric may or may not require. V-05 excellence signals point toward C-34/C-35: registry-level inertia item citation and block-header self-identification of what criterion a structural element closes.
