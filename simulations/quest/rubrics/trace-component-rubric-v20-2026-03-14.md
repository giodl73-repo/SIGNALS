Written to `simulations/quest/rubrics/trace-component-rubric-v20-2026-03-15.md`.

---

**Three R19 signals promoted:**

| # | Name | Source differential | Precondition |
|---|------|---------------------|--------------|
| **C-59** | Schema-Artifact Comparison Column Independence | R19 C-12 differential -- V-02/V-04/V-05 satisfy C-12 additionally via Area 3 Enforcement Rationale column; V-01/V-03 satisfy C-12 only through TABLE-7/TABLE-8 | Requires C-58 (schema must already carry enforcement table before independence test applies) |
| **C-60** | Gate-Block Semantic Type Annotation | R19 C-19 differential -- V-04 adds DIRECTIVE/REQUIREMENT labels inside bracket syntax; all others have gate formalism without semantic typing | Requires C-19 (semantic type extends, not replaces, gate-block formalism) |
| **C-61** | Per-Phase Vocabulary Declaration in Manifest | R19 C-33 differential -- V-03/V-05 include per-phase vocabulary lines within each manifest; all others have C-33's three fields but no vocabulary scoping | Requires C-33 (vocabulary line is an additional manifest field) |

**Ceiling: 190 → 196 pts. 58 → 61 criteria.**
