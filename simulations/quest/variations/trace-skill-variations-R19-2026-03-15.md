Written to `simulations/quest/golden/trace-skill-variate-R19-2026-03-15.md`.

---

## trace-skill Variations -- Round 19

**Baseline**: R18 V-05 (passes C-01 through C-53)
**New criteria targeted**: C-54 and C-55

---

### Variation Map

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Single: C-54 | SCORER HEURISTIC STEP FORMAT note → full `STRUCTURAL MANDATE (C-52)` block with all 4 canonical components. TCR gains row 7. SCORER HEURISTIC gains step (f) `-> confirms C-52 (C-52)`. ANTI-PATTERN adds row 7 by name (C-55 not active). CONFORMANCE-COLLAPSE CLAIM: "rows 1-7." |
| V-02 | Single: C-55 simple | ANTI-PATTERN body replaces enumerated names with TCR delegation: "any Required=YES TCR row." No closure statement. SCORER HEURISTIC STEP FORMAT stays a note (C-54 not active). |
| V-03 | Single: C-55 + closure | Same TCR delegation as V-02, but adds `**ANTI-PATTERN CLOSED ASSERTION**` terminus line naming row count -- making C-55's self-completeness claim structurally mandated, not just implied by the quantifier. |
| V-04 | Combined: C-54 + C-55 simple | V-01 + V-02. TCR has 7 rows. ANTI-PATTERN delegates to "rows 1-7" without closure statement. Proves composability: the delegation automatically covers the new Component 7 without a body update. |
| V-05 | Combined: C-54 + C-55 tight | V-01 + V-03. TCR has 7 rows. ANTI-PATTERN delegates + explicit CLOSED ASSERTION names "rows 1-7." SCORER HEURISTIC steps (a)-(f) each carry exactly one `->` operator. Tightest integration. |

---

### Key structural decisions

**C-54**: The `STRUCTURAL MANDATE (C-52)` block follows the canonical 4-component form (label → scope → verification instruction → independence statement). ASR count stays **6** -- the TCR's `Required (RequiredVocabulary)` column is already tracked at ASR row 5; adding a 7th TCR row reuses that annotation site, not a new one.

**C-55**: The design gap in R18's ANTI-PATTERN is that body-scanning is required to verify coverage against TCR rows. V-02/V-03 fix this by delegating to the TCR rather than enumerating names. V-03 strengthens this with an explicit terminus that names the row count, giving scorers a location-independent confirmation path parallel to the Coverage Matrix CLOSED ASSERTION and ASR closure terminus.

**V-04 composability proof**: When C-54 adds TCR row 7 and C-55's delegation says "any Required=YES row," the ANTI-PATTERN automatically covers Component 7 without editing its body. This is the primary argument that C-54 and C-55 are compositionally independent.
