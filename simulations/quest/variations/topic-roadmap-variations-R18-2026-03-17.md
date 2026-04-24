Written to `simulations/quest/golden/topic-roadmap-variate-R18-2026-03-17.md`.

---

**R18 Variation Summary**

| Var | Axis | C-43 | C-44 | Expected |
|-----|------|:----:|:----:|:--------:|
| V-01 | C-43 single — governing declaration inside obligation statement | FULL | FAIL | 70/72 = 9.72 |
| V-02 | C-44 single — assertion names structural prerequisites by property type | FAIL | FULL | 70/72 = 9.72 |
| V-03 | C-43 partial — governing reference in preamble only | PARTIAL | FULL | 71/72 = 9.86 |
| V-04 | C-43+C-44 combined standard | FULL | FULL | 72/72 = 10.00 |
| V-05 | C-43+C-44 maximal — bidirectional pointer + CONSISTENCY AUDIT CLAUSE | FULL | FULL | 72/72 = 10.00 |

**Key structural moves:**

- **C-43 FULL** (V-01/V-04/V-05): `CONTRACT B is the governing authority for this value requirement` placed *inside* the COMPLIANCE OBLIGATION statement — not in a title, preamble line, or parenthetical after the obligation.

- **C-43 PARTIAL** (V-03): governing reference lives in a `[>> ... <<]` preamble annotation on the guard block, *not* inside the COMPLIANCE OBLIGATION text itself.

- **C-44 FULL** (V-02/V-03/V-04/V-05): falsifiability clause names prerequisites as `EXACT-VALUE REQUIREMENT` and `TAXONOMY-SPLIT REQUIREMENT` — structural property labels, not test-type descriptions.

- **C-44 FAIL** (V-01): falsifiability clause uses "structural compliance test" / "value compliance test" — test-type names only.

- **V-05 maximal**: adds a formal `CONSISTENCY AUDIT CLAUSE` block inside CONTRACT B with named labels `EXACT-VALUE REQUIREMENT` / `TAXONOMY-SPLIT REQUIREMENT`, and the §9 obligation declares the guard-contract relationship as explicitly bidirectional (CONTRACT B → §9 naming, §9 → CONTRACT B governing declaration).
