Written to `simulations/quest/golden/corps-pr-variate-R16-2026-03-17.md`.

---

## R16 — corps-pr — 5 Variations

**Baseline delta from R15 V-03**: Two fixes applied in all five variations:
1. `; no inline-cell alternative path [C-46]` added to C-40 entry in structural enforcement levels (or as named `Eliminated [C-46]:` sub-entry in V-03/V-04/V-05)
2. Alternative form removed from format rules entirely — only cross-reference or prohibition directive remains (no path offered)

**Variation axes:**

| Var | Role Sequence | C-43 Coverage | C-46 Form | Predicted |
|-----|--------------|---------------|-----------|-----------|
| V-01 | PM/TPM first | CLOSED PATHS only (xref in format rules) | Inline clause on C-40 | 38/38 |
| V-02 | Security first | CLOSED PATHS + format-rules restatement | Inline clause on C-40 | 38/38 |
| V-03 | Security first | CLOSED PATHS only (xref in format rules) | Named `Eliminated [C-46]:` sub-entry | 38/38 |
| V-04 | PM/TPM first | CLOSED PATHS only (xref in format rules) | Named `Eliminated [C-46]:` sub-entry | 38/38 |
| V-05 | Security first | CLOSED PATHS + format-rules restatement | Named `Eliminated [C-46]:` sub-entry | 38/38 |

**Diagnostic questions R16 will answer:**
- V-01/V-04: Does sequence permutation interact with C-14 (IA anchoring) or the PRE-COMMITMENT chain when PM/TPM runs before security?
- V-02/V-05: Does double C-43 coverage (declaration + format rules) create any scorer ambiguity about which location satisfies C-45?
- V-03/V-04/V-05: Is the named `Eliminated [C-46]:` sub-entry form more robustly auditable than the inline clause, or equally compliant?
- V-05 (combination): Does the cross-link `Path negation: see "Eliminated [C-46]:"` in the CLOSED PATHS block connect the two declaration sections in a way that tightens the C-45/C-46 joint audit?
