Round 5 variations written to `simulations/quest/golden/flow-dataflow-variate-R5-2026-03-15.md`.

---

**R5 design rationale:**

The v4 rubric crystallized two patterns from R4's top scorers (V-03, V-05) into formal criteria:
- **C-15**: baseline must be a table with 3+ columns, each row referenceable by ID/name
- **C-16**: *every* recovery prescription cites a step-level identifier (not just "at least one")

**Five variations, three hypotheses:**

| Variation | Core Test |
|-----------|-----------|
| **V-01** | 3-col minimal table (C-15 floor) — does removing the Entity Handled column degrade C-16 citation precision? |
| **V-02** | Recovery audit table with "Baseline Step Cited" column — enforcement at the recovery surface vs the baseline surface |
| **V-03** | MS-NN step IDs — does machine-verifiable citation format produce higher C-16 precision than step name citation? |
| **V-04** | Hard imperative + positional citation mandate ("Fallback: MS-03 — step name" opens every entry) |
| **V-05** | All three axes combined + schema-diff tables — quadruple scaffolding coherence test |

**New signals:**
1. **Recovery audit table** (V-02, V-05) — blank cell = missing C-16 citation, co-located with the mechanism
2. **Step ID format** (V-03–V-05) — substring-verifiable citation removes interpretation ambiguity
3. **Positional citation mandate** (V-04, V-05) — first structural element of each entry forces the citation before the mechanism
