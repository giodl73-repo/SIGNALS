Written to `simulations/quest/golden/trace-contract-variate-R20-2026-03-15.md`.

---

## Round 20 Variation Map

| V | Axis | Targets | Key Escalation |
|---|------|---------|----------------|
| **V-01** | output-format (single) | C-54 | Named `VerbatimRule: findings-sealed-echo` block declared in preamble (Step 2); referenced by name from Step 13. Converts the C-51 enforcement prose into a string-comparison contract: any reformulation is detectable without semantic judgment. |
| **V-02** | output-format (single) | C-55 | `taxonomy-version: [TAXONOMY-DECLARED version=N]` added as a named Summary field (Step 12), parallel to `findings-sealed:`. Makes taxonomy version auditable from the summary anchor without locating the seal in the body. |
| **V-03** | lifecycle-emphasis (single) | C-56 | `FailureToken:` block upgraded with named `remediation:` field per entry (`remediation: correct field type and re-sweep` vs `remediation: add absent row and re-sweep`). Remediation path machine-derivable by field lookup alone. |
| **V-04** | output-format combination | C-54 + C-55 | `GovernancePreamble:` with both `VerbatimRule:` (Layer-1) and `TaxonomyEchoRule:` (Layer-2). Summary carries both `findings-sealed:` and `taxonomy-version:` as a dual-anchor audit point. |
| **V-05** | output-format + lifecycle-emphasis | C-54 + C-55 + C-56 | All three advances declared as `GovernancePreamble:` Layers 1–3. Each governing step cross-references its layer by name. Summary carries a `Governance:` status block confirming all three layer obligations as `SATISFIED / VIOLATED / NOT-TRIGGERED`. |

**Structural note on V-05:** The `GovernancePreamble:` block is the same compositional pattern as `ObligationBlock:` — a single addressable declaration unit that later phases cite by name rather than re-stating inline. A governance audit reads only the preamble; a body audit reads only the phases. The two layers are orthogonal.
