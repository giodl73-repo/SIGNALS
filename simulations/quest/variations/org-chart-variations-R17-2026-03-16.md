Written to `simulations/quest/golden/org-chart-variate-R17-2026-03-17.md`.

---

## Summary

**R17 baseline:** R16 V-05 (numbered 1-4 + anti-pointer prohibition + self-containment directive) — C-46 is now the standard.

**Three gaps identified after R16 V-05:**

1. **Count-guard bypass** — the 1-4 numbered format implies four but doesn't enforce four. A model can write 1, 2, 3 and stop.
2. **Gate-label format bypass** — GATE X->Y: format is shown by example but never required. A model can write informal names ("role list", "inertia result") without gate notation.
3. **Introductory preamble bypass** — "The following four transitions restated from the inventory:" is declarative, not pointer-reference, so C-46's prohibition doesn't fire — but it anchors the list to a prior block.

**Three variation axes:**

| Axis | Form | Mechanism |
|------|------|-----------|
| A | Count guard | `COUNT CHECK: exactly 4 entries required -- if any missing, checkpoint FAILS` |
| B | Gate-label format anchor | `each entry MUST use GATE X->Y: [artifact name]` -- prohibits informal/paraphrase names |
| C | Preamble prohibition | `DO NOT write a preamble sentence referencing the inventory block -- item (b) MUST open directly with entry 1` |

**Five variations:**
- V-01: Axis A alone (count guard)
- V-02: Axis B alone (format anchor)
- V-03: Axis C alone (preamble prohibition)
- V-04: Axis A + B combined
- V-05: Axis A + B + C — strongest form; the C-47 candidate if the preamble bypass surfaces in scoring
