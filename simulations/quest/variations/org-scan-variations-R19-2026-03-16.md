**Written**: `simulations/quest/golden/org-scan-variate-R19-2026-03-16.md` — 1,665 lines, 5 complete variations.

---

## Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Role sequence | SCANNER / SYNTHESIZER as GROUP A / GROUP B with all SCHEMA DECLARATIONS in the preamble — schema-first placement maximises C-68 structural detectability |
| **V-02** | Output format | Phase footer `PHASE OUTPUTS` blocks declare row counts at phase exit — creates a second independent verification path for C-68 (attestation count) and C-69 (TABLE H count) |
| **V-03** | Lifecycle emphasis | Maximum preamble density — all 8 table schemas, GATE TOKEN PROTOCOL, INERTIA PATTERN DICTIONARY, BRIDGE RULE, and TABLE F form declared upfront; GROUP A/GROUP B reference rather than re-declare |
| **V-04** | Phrasing register | Imperative/prescriptive throughout ("Write PASS TOKEN only when…", "Omitting Analytical Purpose is a C-67 violation") — tests whether imperative phrasing produces more reliable gate-blocking on the three new criteria |
| **V-05** | Combined | V-02 phase footers + V-03 maximum preamble density — dual verification paths, preamble declares what will be produced, footers confirm what was produced |

---

## New criteria coverage (all 5 variations)

**C-67 — Transport manifest** — TABLE F schema requires all three columns (`Consuming Role | Tables Consumed | Analytical Purpose`); any row lacking Analytical Purpose is called out as a structurally detectable C-67 omission.

**C-68 — COVERAGE ATTESTATION schema-declared** — COVERAGE ATTESTATION appears in SCHEMA DECLARATIONS with `Minimum rows: 7` annotation; SCANNER references "source types declared in COVERAGE ATTESTATION schema" rather than restating inline; gate checklist item reads: *"COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement)"*.

**C-69 — TABLE H dynamic floor + BRIDGE RULE** — SYNTHESIZER writes `Org Shape Dimension count: N — TABLE H must contain exactly N rows` as an execution-time artifact before producing the table; BRIDGE RULE is a named constraint in the TABLE H schema: *"Every TABLE H row must carry at least one `(cite TABLE B row)` annotation in its Driving Evidence cell"*; BRIDGE RULE violations are flagged as `[BRIDGE RULE VIOLATION]` and verifiable by table correspondence alone.
