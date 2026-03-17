Written to `simulations/quest/golden/signal-variate-R4-2026-03-16.md`.

---

## Quest Variate -- /signal (Round 4)

**5 variations generated**, targeting C-16 (`->` enforcement) and C-17 (explicit numbered RULE list), carrying forward all R3 base (C-09 through C-15).

### Spread design

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | C-16 single-axis | SEPARATOR CONTRACT block declares `->` a structural validity requirement (not just a style rule). Hybrid base (R3 V-04). Tests whether a named fail-condition declaration satisfies C-16 without structural pre-print. |
| **V-02** | C-17 single-axis | R3 V-05's 5 merged FORMAT RULES expanded to 7 individually numbered rules (one per criterion, no merges). Pre-print base. Tests whether splitting merged rules satisfies C-17 without changing enforcement. |
| **V-03** | C-16 + criterion-ID labels | R3 V-04 base + SEPARATOR CONTRACT + `(C-NN)` label on each RULE. Tests whether criterion-ID annotations add auditability for C-17 beyond bare numbering. |
| **V-04** | Pre-print + 7 rules with IDs | R3 V-05 structural base + 7 individually labeled rules (replaces 5 merged). Structural enforcement (C-16) + complete enumeration (C-17). Cleanest combination. |
| **V-05** | Pre-print + 7 rules + COMPLIANCE AUDIT | V-04 + a COMPLIANCE AUDIT checklist block before namespace sections. Tests whether a discrete, named contract section adds measurable C-17 value beyond the rule list. |

### Predicted key spread

V-01 vs V-02-V-05 on **C-17**: V-01's SEPARATOR CONTRACT is an unnumbered quality rule outside the main RULE list. If C-17 requires all rules numbered in a single list, V-01 scores PARTIAL (~99). V-02-V-05 all have 7 individually numbered rules and are predicted to PASS C-17.

C-16 is predicted PASS across all 5 variations — the SEPARATOR CONTRACT (V-01, V-03) and structural pre-print (V-02, V-04, V-05) both satisfy the enforcement requirement, but scoring may reveal whether declaration vs. structural enforcement produces different confidence.
