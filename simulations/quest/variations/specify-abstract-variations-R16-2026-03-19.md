Written to `simulations/quest/variations/specify-abstract-variations-R16-2026-03-20.md`.

---

## R16 Variations Summary

**Five variations generated for C-46 (named pre-committed source-gate dependency protocol):**

| V | Axis | C-46 | C-44 | Predicted |
|---|------|------|------|-----------|
| V-01 | Lifecycle emphasis | PASS (3-col table, Phase 3b CANNOT-exist in rationale block) | FAIL (Phase 3/3b only) | 116/118 |
| V-02 | Output format | PASS (4-col table, CANNOT-exist embedded as table column) | PASS | 118/118 |
| V-03 | Phrasing register | PASS (numbered prose list, confirms format independence) | PASS | 118/118 |
| V-04 | Full synthesis | PASS (canonical 3-col table, all 11 criteria) | PASS | 118/118 |
| V-05 | Above-ceiling | PASS + completeness verification (Step V-B cross-audits Protocol V against all 9 Protocol II gates) | PASS | 118/118 + |

**Key design decisions:**

- **V-01** confirms C-46 is independent of C-44: Protocol V present, all-transition rationale absent. This is the isolation proof that C-46 can be tested without C-44.
- **V-02** tests whether embedding the CANNOT-exist reasoning directly in Protocol V's fourth table column (rather than a separate rationale block) satisfies C-46's requirement that "the CANNOT-exist reasoning appears in the Protocol V entry itself."
- **V-03** confirms format independence of C-46: the named-protocol requirement is structural (separately labeled, positioned before Phase 0, cited by Protocol II), not a table-format requirement.
- **V-04** is the synthesis base: canonical 3-column Protocol V + all-transition rationale + Protocol II citing `(Source gate: Phase X per Protocol V.)`.
- **V-05** above-ceiling probe adds **Step V-B** — a completeness verification table inside Protocol V that audits all nine Protocol II gates, confirming every output-dependent gate has a registry entry and every initiation gate explicitly does not require one. This creates bidirectional referenceability: Protocol II cites Protocol V; Protocol V's Step V-B accounts for all Protocol II gates.
