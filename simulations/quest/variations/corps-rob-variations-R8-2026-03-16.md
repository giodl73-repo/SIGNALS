Written to `simulations/quest/golden/corps-rob-variate-R8-2026-03-16.md`.

---

## Variate R8 -- corps-rob

5 complete prompt body variations targeting the two new v8 criteria (C-28, C-29) and their interaction with C-25 and C-26.

### Context

R7 produced two disjoint 140-point paths:
- **V-01 path**: C-25 + C-28 + C-29 (named triage schema + enumerated result), no C-26
- **V-02 path**: C-26 (RULE AUDIT-SUITE + anti-patterns), no C-25/C-28/C-29

No R7 variation achieved all four simultaneously. R8 targets their combination.

### Variation Axes Selected

| Variation | Axis | Target |
|-----------|------|--------|
| **V-01** | Graft TRIAGE NOTE AUDIT SCHEMA into RULE AUDIT-SUITE Triage Note Compliance section | C-25 + C-26 + C-28 + C-29 |
| **V-02** | Preamble-level schema declaration (schema before any stage runs) | C-28 separation strengthened |
| **V-03** | RULE CONDITION-ENUM as a named run-level rule forbidding aggregate NONE | C-29 as named enforceable rule |
| **V-04** | Symmetric schema: ROLE CONCERN AUDIT SCHEMA mirrors TRIAGE NOTE AUDIT SCHEMA | C-27 + C-28/C-29 symmetry |
| **V-05** | Full R8 stack: preamble schemas + RULE CONDITION-ENUM + RULE AUDIT-SUITE graft + symmetric coverage + RULE BOOKEND-AUDIT | C-25, C-26, C-27, C-28, C-29 |

### Key structural claims

**V-01**: Installing the three-condition named schema within the RULE AUDIT-SUITE Triage Note Compliance section deepens that section without merging it with others (no ANTI-PATTERN-1) and without repeating a dimension (no ANTI-PATTERN-2). C-25/C-28/C-29 should be achievable alongside C-26.

**V-02**: Moving the schema declaration to the preamble makes C-28's "separate from per-stage instances" requirement unambiguous -- the post-stage audit section references the preamble schema by name rather than declaring it inline.

**V-03**: Named run-level rules are checkable at output time. RULE CONDITION-ENUM prevents the aggregate-NONE collapse that C-29 was designed to detect.

**V-04**: The named-schema + enumerated-result pattern applied symmetrically to ROLE CONCERN GAPS tests whether the mechanism generalizes beyond triage notes.

**V-05**: All axes stacked with explicit named-rule cross-references to prevent collapse under prompt length pressure.
