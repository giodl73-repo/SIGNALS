Here are the 5 complete R9 variations:

---

## Variation Summary

| V | Axis | C-31 Mechanism | C-32 Mechanism | C-33 Mechanism |
|---|------|----------------|----------------|----------------|
| **V-01** | Output format (manifest-anchored B1 columns) | CONSTRAINT TYPE REGISTRY with pre-populated "B1 Column Name" field per row | B1 carries a named MANIFEST COLUMN AUDIT instruction: "one binary column per manifest row, in row order" — missing UNIQUE or CHECK is a manifest-row violation | Standard parity block before first role section |
| **V-02** | Role sequence (parity block as Phase A entry preamble) | Standard registry inside PHASE A, after the design contract | MANIFEST COLUMN CHECK in B1 header citing row names | PHASE A DESIGN CONTRACT is the _first artifact of Phase A_ — before the step registry, before Q1; model must commit before writing any analytical content |
| **V-03** | Inertia framing (registry-seeded domain consequences) | Registry adds "Business Condition Protected" column — forces inertia pre-commitment per constraint type at parse time | Manifest row-to-column mapping in B1 header | Standard parity block; item 5 is "expand the registry row's Business Condition Protected entry" rather than "write an example" |
| **V-04** | Combined: output format + role sequence (manifest audit count + role contracts) | Four-row manifest with "manifest row count = 4" stated explicitly | B1 MANIFEST COLUMN AUDIT: "expected constraint-type columns = manifest row count (4)" — a count mismatch is detectable before writing | Role CONTRACT headers with checkbox items referencing manifest rows by number — copied verbatim before each role section |
| **V-05** | Combined: lifecycle (three criteria own dedicated phases) | MANIFEST PHASE (Phase 1) is the sole owner of the constraint type registry | CANONICAL PHASE (Phase 4) opens with MANIFEST COLUMN COMPLETENESS CHECK counting expected vs actual columns | PARITY PHASE (Phase 2) is an entire dedicated phase that must gate-complete before any INTERROGATIVE PHASE role section is written |

**Key structural difference across variations:**

- **C-31** moves from "table in parse phase" (V-01/V-03/V-04) → "design contract names it" (V-02) → "owns entire phase" (V-05)
- **C-32** moves from "manifest row forward-reference" (V-01) → "count audit" (V-04) → "manifest completeness check with expected count stated before table write" (V-05)
- **C-33** moves from "block before first role" (V-01/V-03) → "block before registry itself" (V-02) → "role contract headers" (V-04) → "full dedicated phase" (V-05)

The **V-02 innovation** is the most aggressive: positioning C-33 before Q1 means the model commits to parity _before writing the step registry_. The **V-05 innovation** is most composable: each new criterion owns a named phase, so rubric evaluation maps directly to phase presence rather than within-section content scanning.
