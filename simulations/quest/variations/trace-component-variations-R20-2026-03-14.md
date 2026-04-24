Written to `simulations/quest/golden/trace-component-variate-R20-2026-03-15.md`.

---

## R20 Variations -- trace-component

**Ceiling**: 196 pts. **3 new criteria targeted**: C-59, C-60, C-61.

---

### Variation map

| # | Axis | New mechanism | C-59 | C-60 | C-61 |
|---|------|---------------|------|------|------|
| V-01 | Role sequence | **NHQ-3** -- forces schema Enforcement Rationale cells to name specific simpler alternatives + failure modes, making schema artifact independently satisfy C-12 without TABLE-7/TABLE-8 | PASS | FAIL | FAIL |
| V-02 | Output format | **Area 5 Gate Semantic Type Vocabulary** (DIRECTIVE / REQUIREMENT) -- schema-defined labels annotate every `[GATE-N: TYPE: ...]` bracket | FAIL | PASS | FAIL |
| V-03 | Lifecycle emphasis | **PHASE VOCABULARY field** in all 5 manifests -- minimum two phase-scoped framework terms per manifest | FAIL | FAIL | PASS |
| V-04 | Role seq + Output fmt | V-01 + V-02: NHQ-3 AND Area 5 gate vocabulary | PASS | PASS | FAIL |
| V-05 | All three axes | V-01 + V-02 + V-03: all three mechanisms | PASS | PASS | PASS |

---

### Key design decisions

**NHQ-3 design** (C-59): The question gives the model two versions of an Enforcement Rationale column -- Version A with named alternatives + failure modes, Version B with generic affirmations -- and asks which permits independent comparison-column verification when the analysis tables are removed. This forces the reasoning that "specific named alternative = independently verifiable comparison; generic affirmation = not." The Area 3 schema instruction then explicitly prohibits generic affirmation language and requires a verifier reading only the schema to be able to identify the alternative and why it fails.

**Area 5 design** (C-60): DIRECTIVE and REQUIREMENT are defined in the self-authored schema as a named table with Scope and Definition columns. All gate blocks get the label as the first component after the ordinal: `[GATE-N: TYPE: ...]`. Gates 1-4 and 7 are REQUIREMENT; Gate 6 is DIRECTIVE (structural four-phase form). Using 6 annotated gates clears C-60's threshold of 3.

**PHASE VOCABULARY design** (C-61): Field added to every manifest template with concrete example terms per phase (event: SyntheticEvent/addEventListener; traversal: props/context/HOC; mutation: useState/dispatch; re-render: React.memo/useMemo; settle: useEffect/AbortController). Area 4 of the schema declares the four-field manifest structure so vocab omission is a self-contradiction against the authored schema.
