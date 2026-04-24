Written to `simulations/quest/golden/signal-variate-R8-2026-03-16.md`.

---

# Quest Variate -- /signal (Round 8)

**Rubric**: v7 (15 aspirational criteria, C-09 through C-23)
**Base**: R7 V-05 (14 rules, bijective invariant declared, RULES 12-14 carry inline evidence -- C-23 satisfied by behavior but no dedicated RULE 15)

**R8 structural obligation**: Add RULE 15 (C-23) to close the bijection. Update RULE 9 count to 15, COMPLIANCE AUDIT to 15 checkboxes, gate to "15/15 checked = valid output."

---

## Variation Summary

| Variation | Axis | Key structural change |
|-----------|------|-----------------------|
| **V-01** | C-23 single-axis | RULE 15 (C-23) added as minimal dedicated labeled rule. No inventory, no citations. |
| **V-02** | Named meta-rule inventory | RULE 15 names RULE 12, 13, 14 by number -- O(1) target identification. |
| **V-03** | Full evidence citations | RULE 15 names all three AND states the expected evidence string for each. Self-contained audit. |
| **V-04** | Header evidence chain declaration | Evidence chain declared in QUALITY CONTRACT header alongside bijective invariant. Two contract-level structural properties now visible before any rule is read. |
| **V-05** | Recursive self-example | RULE 15 names the three meta-rules, quotes their evidence, AND explicitly states that RULE 15 itself demonstrates C-23 compliance by carrying its own inline evidence. The rule about requiring evidence is self-demonstrating. |

**Hypothesized champion**: V-05. The recursive self-example closes the audit loop at the meta-level: every rule in the contract, including the rule about meta-rule evidence, is verifiable O(1) from the rule itself without searching elsewhere.

**Expected score if V-05 passes all 15 aspirational on v7**: 100/100 (5/5 essential × 12 + 3/3 recommended × 10 + 15/15 aspirational × 0.67 = 60 + 30 + 10 = 100).
