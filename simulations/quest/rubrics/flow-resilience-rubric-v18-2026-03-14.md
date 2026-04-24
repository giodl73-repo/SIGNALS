Written to `simulations/quest/rubrics/flow-resilience-rubric-v18-2026-03-15.md`.

---

**v18 summary:**

| | v17 | v18 |
|---|---|---|
| Denominator | 45 | **48** |
| New criteria | C-51, C-52, C-53 | **C-54, C-55, C-56** |
| R17 ceiling | 99.78 (44/45) | **99.17 (44/48) -- V-03** |
| R18 ceiling | open | **99.79 (47/48) -- V-03** |

**Three new criteria from R18:**

**C-54 — Sequential Instance Count Labels Across All Enforcement Locations** *(E-46)* — Every enforcement location carries "Enforcement Instance K of N" or equivalent, making the total count explicit at every independent location. C-53 requires two self-labeled restatements; C-54 requires every location to carry a sequential count. V-03 PASS; V-01/V-02/V-04/V-05 FAIL.

**C-55 — Originating Declaration Self-Label on Document-Header Enforcement Element** *(E-47)* — The document-header element (C-52) self-labels as "(originating declaration)" — the source anchor from which all lower levels derive. C-52 requires the preamble to name the document-header element; C-55 requires the document-header element to name itself as the source. V-03 PASS ("Enforcement Instance 1 of 4 (originating declaration)"); V-01/V-02/V-04/V-05 FAIL.

**C-56 — Mutual Cross-Reference Between Document-Header Element and Enforcement Preamble** *(E-48)* — Both the document-header element and the preamble name each other by label (bidirectional). C-52 requires only preamble → document-header. V-02 PASS, V-04 PASS (§0 names preamble rule by label; preamble names §0 by label); V-01/V-03/V-05 FAIL.

**R18 per-variation scores:** V-01/V-05 = 99.38 | V-02/V-04 = 99.58 | V-03 = **99.79** (ceiling). Open axis: synthesize C-54 + C-55 (V-03 pattern) with C-56 (V-02/V-04 pattern) simultaneously.
