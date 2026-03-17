Written to `simulations/quest/golden/mock-ns-variate-R7-2026-03-16.md`.

---

## Round 7 Variates -- mock-ns (rubric v7, max 116)

Five complete prompts targeting C-25 and C-26. All changes are isolated to S-0's opening gate and CONSTRAINT block; steps S-1 through A-5 are identical across all variates.

### Variation axes

| # | Axis | Single change from R6 V-05 | C-25 pred | C-26 pred | Score pred |
|---|------|---------------------------|-----------|-----------|------------|
| **V-01** | C-25 order boundary | Gate sentences transposed: imperative first, declarative second | **FAIL** | PASS | **114/116** |
| **V-02** | C-26 partial boundary | CONSTRAINT: 4/5 synonymized, op-5 uses canonical phrase | PASS | **FAIL** | **114/116** |
| **V-03** | C-25 count boundary | Gate expanded to 3 sentences (declarative + elaboration + imperative) | **UNCERTAIN** | PASS | **114 or 116** |
| **V-04** | C-25 identity-type boundary | Gate declarative asserts output ordering, not step role | **FAIL** | PASS | **114/116** |
| **V-05** | C-26 depth probe | CONSTRAINT synonyms deepened to zero shared lexemes with canonical | PASS | PASS | **116/116** |

### Key new traps documented

- **"Reversed two-sentence gate"** (V-01): Both sentences present, imperative precedes declarative. C-25 specifies declarative-first order; presence of both is necessary but not sufficient.

- **"4/5 synonymization"** (V-02): One canonical phrase survives in CONSTRAINT. C-26 is all-or-nothing; even one canonical phrase disqualifies regardless of synonym coverage elsewhere.

- **"Three-sentence gate count"** (V-03): Open question -- does C-25 "consists of two sentences" mean exactly two or at least two with both types? Result determines whether v8 needs a count clarification.

- **"Output-primacy declarative"** (V-04): Declarative sentence frames *what comes out first* ("the first observable output is X") rather than *what the step is* ("this step emits first"). C-25 requires step-role assertion, not output-sequence assertion.

- **"Zero-lexeme synonyms"** (V-05): Tests whether C-26 has an implicit proximity bound on synonym forms. If V-05 somehow fails, a C-27 on synonym depth would be extracted for rubric v8.
