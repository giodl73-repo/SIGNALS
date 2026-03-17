Written to `simulations/quest/golden/corps-scan-variate-R8-2026-03-17.md`.

---

## R8 Variate -- corps-scan (Round 8)

### Invariants baked into all 5 variations (from v8 rubric)

| Criterion | What every variation carries |
|-----------|------------------------------|
| C-31 | Three audit surfaces simultaneously: manifest table + phase-contract table + per-phase predicates |
| C-32 | PHASE CONTRACT TABLE placed before any phase body |
| C-33 | Incompleteness predicate is the FIRST line of each phase body -- before ENTRY, before IVR triples |
| C-34 | CONSTRAINT MANIFEST has `| TOTAL | | 14 labeled triples -- count to verify completeness |` as terminal row |

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Blockquote predicate format | `> **Phase N is not complete until**: ...` creates a rendered-markdown scan surface -- a reviewer verifies C-15/C-33 by scanning blockquotes only |
| **V-02** | Extended manifest with VIOLATION column | 4-column manifest (Label / Phase / Summary / Violation Pattern) makes anti-pattern identification possible from the manifest alone, without reading IVR triple bodies |
| **V-03** | Phase-contract table with test-item-count column | "Test items" count column (P1=2, P2=5, P3=6, P4=1) creates a mechanical cross-check: table count must equal YES/NO items in test block; also reveals that TOTAL triples = TOTAL test items (14=14) |
| **V-04** | V-01 + V-02 | Four independent surfaces: manifest labels, manifest violations, contract table ENTRY/EXIT, blockquote predicates |
| **V-05** | V-01 + V-02 + V-03 | Five surfaces: adds test-item counts; V-05 also demonstrates the cross-manifest invariant (14 IVR triples = 14 total test items), a potential C-35 signal |

### V-05 excellence signals (potential v9 criteria)

V-05 demonstrates two behaviors not yet formalized:
1. **Cross-manifest count invariant** -- CONSTRAINT MANIFEST TOTAL (14) equals sum of all phase test-item counts in PHASE CONTRACT TABLE (2+5+6+1=14). Both tables declare the same count from different structural perspectives. Mechanical discrepancy detection across two front-matter tables.
2. **Violation column as scan surface** -- the manifest VIOLATION column is a fifth audit surface that lets a reviewer identify anti-patterns without entering any phase body. The four manifest columns collectively carry the full IVR semantic without requiring phase-body traversal.
