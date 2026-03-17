Here are the 5 complete variations for trace-skill Round 12.

---

## trace-skill Variations R12 — Summary

**Entry state**: R11 V-01 scores 99.33 (C-01 through C-36 PASS, 28/30 aspirational). v11 adds C-39/C-40/C-41 (denominator 30 → 33). Two structural failures carry forward: C-37 (COUNT GATE emits no defect code) and C-38 (PRE-READ GATE emits no defect code).

---

### Variation axes

| Variation | Axis | Targets | C-37 | C-38 | C-39 | C-40 | C-41 |
|-----------|------|---------|------|------|------|------|------|
| V-01 | Lifecycle emphasis — canonical template declared | C-41 | FAIL | FAIL | PASS (by contract) | FAIL | PASS |
| V-02 | Phrasing register — scorer heuristic in every block | C-40 | FAIL | FAIL | PASS (by inheritance) | PASS | FAIL |
| V-03 | Lifecycle emphasis — defect-emitting gates | C-37 + C-38 | PASS | PASS | PARTIAL | FAIL | FAIL |
| V-04 | Combined: gates + canonical template | C-37 + C-38 + C-41 | PASS | PASS | PASS | FAIL | PASS |
| V-05 | Combined: gates + template + heuristics | All five | PASS | PASS | PASS | PASS | PASS |

---

### What each variation adds to the R11 V-01 base

**V-01**: Inserts `### Canonical Structural Mandate Template` before Phase Label Schema. Declares the `> STRUCTURAL MANDATE (C-XX): ... Reproduce it exactly as shown.` form explicitly. C-26 and C-36 blocks already conform; conformance is now by contract rather than practice. C-37/C-38 unfixed.

**V-02**: Adds scorer confirmation closing line to C-26 and C-36 blocks. C-26 gets: *"A scorer confirms C-26 compliance by closure terminus line presence alone without parsing the CLOSED ASSERTION block content."* C-36 gets a heuristic specific to block-header presence. C-37/C-38 unfixed; canonical template absent.

**V-03**: Extends DefectCodeVocab to `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`. COUNT GATE ELSE branch emits `DEFECT: COUNT-MISMATCH`. PRE-READ GATE (c)-fail branch emits `DEFECT: EMPTY-CELL`. Adds `STRUCTURAL MANDATE (C-37)` and `STRUCTURAL MANDATE (C-38)` blocks. Canonical template and C-40 heuristics absent.

**V-04**: Combines V-01 + V-03. Canonical template + defect-emitting gates. All four STRUCTURAL MANDATE blocks (C-26, C-36, C-37, C-38) conform to the declared canonical form by contract. C-40 scorer heuristics absent from block bodies.

**V-05**: Full R12 ceiling. Canonical template extended to include the scorer confirmation line as a required template element. All four STRUCTURAL MANDATE blocks carry inline criterion ID (`STRUCTURAL MANDATE (C-XX)`) and scorer confirmation heuristic. DefectCodeVocab extended. Both gates defect-emitting. No prior passing criterion is degraded — gate blocks add no new `(TypeName)`-annotated columns, so the C-28 COUNT GATE expected count is unchanged from R11 V-01.
