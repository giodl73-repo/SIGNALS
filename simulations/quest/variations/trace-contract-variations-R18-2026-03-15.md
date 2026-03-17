`simulations/quest/golden/trace-contract-variate-R18-2026-03-15.md` written — 5 complete variations.

**Round 18 Variation Map**

| V | Axis | Targets | Key move |
|---|------|---------|----------|
| V-01 | output-format | C-48 | `[FINDINGS-COMPLETE count=N findings]` at findings boundary; count-assertion makes section self-verifying |
| V-02 | output-format | C-49 | `AmendmentProtocol:` + `TaxonomyVersion:` in MechanismTypeTaxonomy; converts `closed: true` from assertion to enforceable contract |
| V-03 | lifecycle-emphasis | C-50 | `OmissionRule:` declared inside GateTokenSchema; absent row = automatic `SCHEMA-PHASE-FAIL` by row-count test |
| V-04 | output-format combination | C-48 + C-49 | Count-bearing findings seal + AmendmentProtocol — orthogonal layers, no shared state |
| V-05 | output-format + lifecycle-emphasis | C-48 + C-49 + C-50 | All three R18 advances as named `ContractGovernancePreamble` layers — phases cite by reference, none restate |

**Structural choices:**
- V-01 adds the count seal but leaves `[FINDINGS-COMPLETE]` unadorned in prior round — this is the clean single-axis test for C-48
- V-02 adds `AmendmentProtocol:` + `TaxonomyVersion: 1.0` making taxonomy evolution auditable (version increment = detectable amendment)
- V-03 embeds `OmissionRule:` directly in the `GateTokenSchema` block so the rule is co-located with the schema it governs — row-count is the compliance test, not prose reading
- V-05 introduces `ContractGovernancePreamble` as a named structural section, a pattern not present in any R17 variation; `FindingsClosureProtocol:` is declared in the preamble alongside `ObligationBlock` rather than as a standalone instruction
