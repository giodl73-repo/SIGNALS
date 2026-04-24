Here are the 5 complete R7 variations:

---

**R6 → R7 diagnosis**: The v7 rubric added C-23 (column-header schema) and C-24 (sub-phase synthesis slot alignment), expanding the denominator to /16. All five R6 variants score below 100.0 under v7 — V-02 R6 and V-03 R6 each hit 99.4 by opposite paths. R7's goal is the first 100.0.

**Axes chosen:**

| Variant | Axis | Change | Predicted |
|---------|------|--------|-----------|
| **V-01** | C-24 only | V-02 R6 base (already C-23 PASS) — split Because block from 5 to 6 slots | **100.0** |
| **V-02** | Strict C-23 | V-03 R6 base (already C-24 PASS) — all phases redesigned with domain-specific column headers, no `\| Field \| Value \|` anywhere | **100.0** |
| **V-03** | Phase 5 column decomposition (boundary test) | V-01 R6 base — Phase 5 only gets named-column sub-tables; Phases 0–4 stay inline | **98.8** (C-23 FAIL on inline phases documents "each phase" is absolute) |
| **V-04** | Combined: strict C-23 + C-24 + Phase 4 quote fix | V-02 R7 base — Phase 5 refined, Phase 4 adds "Source Context" column to relieve quote compression | **100.0** (most robust — no interpretation ambiguity) |
| **V-05** | Conversational + liberal C-23 + C-24 | V-05 R6 base — tables replace inline rows, 6-slot synthesis, preamble explains WHY 6 slots | **100.0** (liberal C-23) / **99.4** (strict C-23) |

**Key finding**: V-01 is the minimal convergence proof (one Because-block change). V-02 eliminates all C-23 scoring ambiguity by design. V-04 is the production-ready variant that combines both with a Phase 4 quote-fidelity fix noted as a risk since R6.
