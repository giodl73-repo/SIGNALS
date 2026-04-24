Written to `simulations/quest/golden/corps-scan-variate-R7-2026-03-17.md`.

---

## Variate R7 -- corps-scan: 5 Complete Variations

**Invariants baked into all 5 variations** (the three new v7 criteria):

- **C-28**: META-RULE enumerates all 14 IVR labels by identifier and states the count ("14 labeled triples"). Discrepancy detection is mechanical.
- **C-29**: Every phase (including P1 and P4) opens with a named ENTRY block. ENTRY-P1 is "no prerequisites"; P2/P3/P4 gate on prior phase completion tests.
- **C-30**: Full suite -- explicit incompleteness predicate, directed YES/NO completion test, conditional advance -- on all four phases without exception.

---

### Variation Axes

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | **Phase-contract summary table** at prompt opening | A single table showing ENTRY/EXIT/predicate/test for all 4 phases gives a reviewer a top-level audit guide before reading any phase body -- C-29/C-30 doubly anchored (table + phase bodies) |
| V-02 | **Manifest as markdown table** with terminal count row | Count row mirrors C-14 gate-row pattern -- discrepancy detection becomes structural (count table rows vs count cell), not textual parsing |
| V-03 | **Explicit "Phase N is not complete until X"** predicate phrasing at phase start | Canonical C-15 form placed first in each phase body -- a reviewer checks C-30 by scanning first line of each phase, without reading completion tests |
| V-04 | V-01 + V-02 combined | Two tables: phase-contract table (ENTRY/EXIT) + manifest table (label inventory) -- triple-anchored with phase bodies |
| V-05 | V-01 + V-02 + V-03 combined | Four independent surfaces for C-28/C-29/C-30: manifest table + phase-contract table + explicit predicates + per-phase completion tests |
