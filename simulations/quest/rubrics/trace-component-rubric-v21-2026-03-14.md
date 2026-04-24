Written to `simulations/quest/rubrics/trace-component-rubric-v21-2026-03-15.md`.

---

**Three R20 signals promoted:**

| # | Name | Source differential | Precondition |
|---|------|---------------------|--------------|
| **C-62** | Schema Area 5 Gate-Type Vocabulary Declaration | R20 V-02/V-04/V-05 have a named Area 5 in the schema that defines DIRECTIVE/REQUIREMENT and any other gate semantic types as a structured table with Type-Name, Applies-To, Exclusion-Condition columns; V-01/V-03 use the type labels without schema-defining them | Requires C-60 (gate-type labels must exist before their schema declaration can be required) |
| **C-63** | Causal Question Grounding for Gate-Type Schema Declaration | R20 V-02/V-04/V-05 differential -- the causal question block includes at least one question asking why a gate-type label coined at write-time is epistemically weaker than a schema-declared type; variations without Area 5 have no such question | Requires C-62 (declaration must exist before its causal grounding can be required) |
| **C-64** | Phase-Vocabulary Source Citation in REQUIREMENT-Type Gate Blocks | R20 V-03/V-05 differential -- REQUIREMENT-type gate blocks that enforce vocabulary scope within a phase cite the phase manifest's PHASE VOCABULARY field as their source, closing the manifest-gate-citation chain; V-01/V-02/V-04 either lack phase vocabulary or carry REQUIREMENT gates without manifest citations | Requires C-60 and C-61 (both semantic typing and per-phase vocabulary must be present for the citation to be possible) |

**Ceiling: 196 → 202 pts. 61 → 64 criteria.**

The dependency graph for the new tier: C-62 → C-63 (causal grounding is downstream of the declaration it grounds); C-60 + C-61 → C-64 (citation chain requires both typed gates and phase-scoped vocabulary). C-62 and C-64 are independent of each other.
