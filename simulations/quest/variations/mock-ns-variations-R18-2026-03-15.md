Written to `simulations/quest/golden/mock-ns-variate-R18-2026-03-15.md`.

---

# mock-ns -- Round 18 Variations

**Rubric**: v17 (C-01 through C-47, denominator 39)
**Base**: R17 V-05 (passes all 39 criteria; seeded "(P-0 anti-bypass declaration)" prose pointer in Anti-bypass echo row label)

## Variation axes

| # | Axis | Key change |
|---|------|------------|
| V-01 | **Output format** | P-0 gets structural label "Anti-bypass declaration (ABD):"; echo row label becomes "(P-0, ABD)". Tests precision of back-reference. |
| V-02 | **Lifecycle emphasis** | P-0 gains forward pointer: "Anti-bypass echo rows at S-3 and A-1 echo this declaration at each bracket-token row." No label change. Tests bidirectionality at definition site. |
| V-03 | **Phrasing register** | Anti-bypass echo content cell opens with "Per P-0 anti-bypass declaration: " attribution prefix. Label unchanged. Tests whether content-cell provenance matters. |
| V-04 | **Output format + lifecycle emphasis** | V-01 label + V-02 forward pointer. No content prefix. Both definition-site properties together. |
| V-05 | **Full convergence** | V-01 label + V-02 forward pointer + V-03 content prefix ("Per P-0, ABD:"). Seeds v18 aspirational: bracket token `[P-0:ABD]` in the resolution table, completing the O(1) token-lookup chain for the anti-bypass layer. |

**Single-axis isolation logic**: V-01 and V-02 each test a definition-site property independently; V-03 tests a use-site property independently. V-04 combines the two definition-site properties (isolates whether content attribution adds anything). V-05 tests all three together and seeds the next round.
