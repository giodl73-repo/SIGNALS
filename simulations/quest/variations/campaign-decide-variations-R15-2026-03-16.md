Written to `simulations/quest/golden/campaign-decide-variate-R15-2026-03-17.md`.

---

## R15 — campaign-decide variations

**New criteria targeted**: C-37 + C-38 (both carried in all five variations as baseline).

### Change summary

| Gap | Criterion | Fix applied |
|-----|-----------|-------------|
| C-37 | Hypothesis resolution schema in SCHEMA PREAMBLE with fill-forward directive | ALL variations carry the Phase 5 hypothesis resolution schema in the SCHEMA PREAMBLE; encoding varied per variation (header annotation, body directive, documentation voice) |
| C-38 | Column-specific FINDING REGISTER closure directives | ALL variations carry column-named closure directives; encoding format varies (prose, bracket notation, documentation voice) |

### Variation axes

| Var | Axis | Hypothesis |
|-----|------|------------|
| **V-01** | C-37 fill-forward in Phase 5 **header annotation** | `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]` on the Phase 5 header fires at phase-boundary evaluation time — stronger C-37 signal than a body-level directive. C-38: prose column naming (baseline). |
| **V-02** | C-38 **bracket notation** column enumeration | `Close FINDING REGISTER Phase N rows [columns: FID, ...]` across all phases — structurally uniform, enables partial-fill detection at each gate. C-37: body-level fill-forward directive (baseline). |
| **V-03** | **Phrasing register** — documentation voice for C-37/C-38 | Descriptive phrasing ("Phase N register rows are committed here, populating..."; "The Phase 5 resolution sub-table uses the schema defined in the Schema Preamble") preserves structural compliance while reading as specification rather than imperative. |
| **V-04** | Combined: **schema architecture overview** (lifecycle) + bracket notation | A Schema Architecture table at SCHEMA PREAMBLE top lists all 5 schemas and their propagation scope — C-37 self-documents at the architecture level before any schema definition is read. Combined with bracket notation for C-38. |
| **V-05** | **Full integration** targeting 105.0/105.0 | V-01 header annotation + V-02 bracket notation + V-04 architecture overview + all 38 criteria structurally encoded with no prose serving as load-bearing element. |

### Key structural novelties in R15 vs R14

- **V-04/V-05 schema architecture table** — a pre-SCHEMA-PREAMBLE index naming all 5 schemas and their usage phases; makes C-37 verifiable from the index alone without reading phase bodies.
- **V-01 header annotation** — `[USE SCHEMA PREAMBLE DEFINITIONS]` as a gate-sibling on the Phase 5 header; C-37 fire-point moves from inside Phase 5 body to the phase boundary itself.
- **V-02/V-04/V-05 bracket notation** — `[columns: FID, Finding Summary, Primary Competitor, Switching Cost]` replaces prose naming; Phase 1a bracket uniquely exposes all 4 extended-schema columns.
