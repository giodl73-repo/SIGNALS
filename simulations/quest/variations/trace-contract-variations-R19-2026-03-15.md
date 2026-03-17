Written to `simulations/quest/golden/trace-contract-variate-R19-2026-03-15.md`.

---

## Round 19 Variation Map

| Var | Axis | Target | Key Change |
|-----|------|--------|------------|
| V-01 | output-format | C-51 | `findings-sealed:` field in Step 12 Summary mirrors `[FINDINGS-COMPLETE count=N findings]` verbatim — count assertion verifiable from summary anchor without cross-referencing findings boundary |
| V-02 | output-format | C-52 | `[TAXONOMY-DECLARED version=0]` seal carries version counter; `AmendmentVersion:` field in taxonomy block; version-skew detectable by counter comparison alone; Summary echoes as `taxonomy-version:` |
| V-03 | lifecycle-emphasis | C-53 | `FailureToken:` block in GateTokenSchema declares `SCHEMA-PHASE-FAIL` (present row, type violation) and `SCHEMA-OMISSION-FAIL` (absent row) as distinct named tokens with distinct remediation paths; Step 7 applies them categorically |
| V-04 | combination | C-51+C-52 | V-01 + V-02 combined; Summary carries both `findings-sealed:` and `taxonomy-version:` as co-equal audit-echo fields; auditor can verify both from summary alone |
| V-05 | combination preamble | C-51+C-52+C-53 | All three R19 advances declared in a `ContractGovernance:` preamble block before Step 1; later phases reference rules by name ("per ContractGovernance findings-sealed-rule"); Summary carries all three echo fields as governance verification checklist |

**Single-axis selection:** Role sequence was already explored heavily in prior rounds (roles are stable). This round's single axes target the three output-format/lifecycle escalations directly.

**V-05 structural innovation:** The `ContractGovernance:` preamble makes the governance commitments discoverable from the document head — preamble + summary form a complete audit circuit without entering any intermediate step. This is the strongest C-51/C-52/C-53 candidate.
