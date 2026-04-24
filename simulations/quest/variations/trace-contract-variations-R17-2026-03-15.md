---

# trace-contract Variate — Round 17

Five complete variations written to `simulations/quest/golden/trace-contract-variate-R17-2026-03-15.md`.

## Variation Map

| Variation | Axis | Primary Target |
|-----------|------|----------------|
| **V-01** | lifecycle-emphasis | **C-45** — Schema Diff phase closes with `[SCHEMA-DIFF-COMPLETE]` token; element diff blocked until token is written; schema-validation coverage auditable independently of element coverage |
| **V-02** | output-format | **C-46** — `MechanismTypeTaxonomy` declared inline as closed enumerated set before first finding block; `[TAXONOMY-DECLARED]` token seals the declaration; C-22 conformance verifiable by reference to one block |
| **V-03** | phrasing-register | **C-47** — `Prohibit: re-derive-mechanism-type-shared` elevated from Sub-task B step prose into `ObligationBlock: census-gate-obligations` as its 7th imperative; Sub-task B carries `see: ObligationBlock (Prohibit: re-derive-mechanism-type-shared)` instead of the prose instruction |
| **V-04** | lifecycle-emphasis + output-format | **C-45 + C-46** — V-01 bounded phase + V-02 closed taxonomy combined; schema-diff closes before findings preamble opens; two phase/declaration tokens appear sequentially in the post-run section |
| **V-05** | lifecycle-emphasis + output-format + phrasing-register | **C-45 + C-46 + C-47** — all three R17 advances declared as **Contract Layer 4: Verification Infrastructure Layer** in the preamble; all three are infrastructure before execution begins, cross-referenced at Step 4, Step 5, and Sub-task B |

## Structural logic

- **V-01 through V-03**: Each takes R16-V05 (all three R16 advances: typed schema, named ObligationBlock, witness-first audit) as the baseline and adds exactly one R17 advance.
- **V-04**: Combines the two output-format/lifecycle axes (C-45 + C-46); V-03's phrasing axis held at R16 baseline.
- **V-05**: Introduces a fourth contract layer — `VerificationInfrastructure` — that declares all three R17 advances as pre-execution infrastructure, following the same pattern as the R16-V05 three-layer preamble.
