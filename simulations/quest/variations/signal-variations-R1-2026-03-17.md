Written to `simulations/quest/golden/signal-variate-R1-2026-03-17.md`.

---

# Quest Variate -- `/signal` Round 1

**5 variations generated across 3 axes.**

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Output format: table layout | Table-per-namespace enforces column discipline → better C-06 count accuracy; may hurt C-07 (no natural footer slot) |
| V-02 | Phrasing register: conversational imperative | User-intent framing elicits natural routing footers (C-07) and better dispatch (C-05); delegates layout → risks C-10 |
| V-03 | Lifecycle emphasis: explicit branching + output contracts | Named output contracts per mode make `--bare` and `<namespace>` reliable (C-04, C-05); verbose → mechanical feel |
| V-04 | Combination: format + phrasing | `->` list precision + warm footer phrasing → best of V-01 and V-02 on C-07 + C-10 together |
| V-05 | Full integration: format + phrasing + explicit lifecycle | Explicit mode-parse gate + canonical list inlined as reference + dispatch footer → targets all 5 essential + C-06/C-07/C-08 directly |

---

## Design Decisions

**Single-axis first (V-01, V-02, V-03)**: each isolates one variable. If V-03 scores highest on C-04/C-05 but lowest on C-09/C-10, we know the lifecycle axis trades correctness for scannability.

**V-04 combines format + phrasing** (the two axes most likely to interact positively — one gives structure, the other gives warmth).

**V-05 is the max-coverage bet**: it inlines the full reference catalog verbatim (so descriptions can't drift from canonical) and wraps everything in a compliance gate. The gate directly addresses the most common failure mode seen in prior rounds: models emitting partial output or merging `--bare` with prose.

**Key structural choice across all variations**: the authoritative sub-skill descriptions are embedded verbatim in every prompt. This locks C-09 (canonical one-liners) from the supply side rather than hoping the model recalls them. V-05 adds the explicit instruction "do not invent new descriptions" to make the constraint undeniable.
