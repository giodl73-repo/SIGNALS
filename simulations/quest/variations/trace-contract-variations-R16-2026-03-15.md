Written to `simulations/quest/golden/trace-contract-variate-R16-2026-03-15.md`.

---

## Round 16 Variation Map

| Variation | Axis | New Criteria Targeted | Hypothesis |
|-----------|------|-----------------------|------------|
| **V-01** | output-format | C-42 | `GateTokenSchema` as a **typed-column table** (field / type / constraint / co-required-with) — an untyped field produces a visually incomplete row, not a silently missing annotation |
| **V-02** | lifecycle-emphasis | C-43 | **ObligationBlock as an explicit named construction phase** before Sub-task A — declared once, given an addressable name, cross-referenced from Sub-task A, Sub-task B, and S6.5 with `see: ObligationBlock: census-gate-obligations` rather than restated prose |
| **V-03** | role-sequence | C-44 | **Witness-first execution** — Gate Witness fills `verification-by:` / `verification-result:` in an isolated Phase W before Census Owner fills `attestation-by:` / `attestation-result:` in Phase A; gate closes only when both phases contribute non-null values |
| **V-04** | output-format + lifecycle-emphasis | C-42 + C-43 | V-01 and V-02 operate at orthogonal layers (schema declaration vs. imperative chain) with no shared state — they compound without axis interference |
| **V-05** | all three axes | C-42 + C-43 + C-44 | Three R16 advances declared as **co-equal contract layers in a preamble** (`[CONTRACT-LAYER-PREAMBLE-SEALED]`) before any execution begins — later phases reference pre-declared layers by name rather than constructing them inline |

**Key structural innovations per variation:**

- **V-01** adds a pre-execution `GateTokenSchema` typed-column table and a `## Schema Diff` phase that checks value conformance against declared type tokens before the element-level diff
- **V-02** adds a `[OBLIGATION-BLOCK-SEALED]` token and replaces inline imperative blocks at Sub-task A, Sub-task B, and S6.5 with `see: ObligationBlock: census-gate-obligations`
- **V-03** introduces `ROLE: Gate Witness` with `[PHASE-W-COMPLETE]` isolation before the census owner attests, making single-party satisfaction structurally impossible
- **V-04** combines V-01's typed table with V-02's named phase; adds schema conformance check inline at S6.5
- **V-05** declares all three layers as `Contract Layer 1` / `Contract Layer 2` / `Contract Layer 3` in a sealed preamble, with `AuditProtocol: census-gate-audit` as a first-class named entity alongside the schema and obligation block
