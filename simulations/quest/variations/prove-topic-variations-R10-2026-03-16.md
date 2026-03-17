Written to `simulations/quest/golden/prove-topic-variate-R10-v10-2026-03-16.md`.

---

## R10 Variation Summary

**5 complete, runnable skill body prompts** targeting rubric v10, built from V-05 R9 (103/104) as base.

### Variation Matrix

| Variation | Single Axis | New Structural Pattern | C-39+ Candidate |
|-----------|-------------|----------------------|-----------------|
| **V-01** | Five-invariant coverage declaration | `FIVE-INVARIANT ARCHITECTURE COMPLETE` block with `COVERAGE FAIL` label; ROLE A echoes `five_invariant_coverage_confirmed` by block name; Stage 5 ENTRY CONDITIONS verify block active | C-39 |
| **V-02** | Stage 0 pre-commit ROLE A crosscheck | ROLE A commits `stage0_precommit_verification_plan` naming expected values of both Stage 0 forward-commitment fields; Stage 5 ENTRY CONDITIONS verify by field name cross-referencing ROLE A plan | C-40 |
| **V-03** | Closure canonical form consistency check | Stage 0 EXIT SIGNAL explicitly cross-verifies `synthesis_closure_form` matches the registered CAMPAIGN CLOSURE CANONICAL FORM entry (CLOSURE FORMAT ERROR if mismatch); closes registration-to-commitment loop at Stage 0 | C-41 |
| **V-04** | V-01 + V-02 | Coverage gate + three-anchor chain | C-39 + C-40 |
| **V-05** | V-01 + V-02 + V-03 | All three axes; R10 convergence candidate | C-39 + C-40 + C-41 |

### What's new per axis

**V-01**: The `FIVE-INVARIANT ARCHITECTURE COMPLETE` block is a coverage-level structural gate sitting above the per-invariant entries. It registers `COVERAGE FAIL` as the canonical label for an incomplete invariant set, and requires ROLE A to echo it by block name (`five_invariant_coverage_confirmed`). This is the registration-level analog of what C-12 does for the standalone block requirement — but at the _completeness_ level rather than the _existence_ level.

**V-02**: ROLE A (executing before Stage 0) commits `stage0_precommit_verification_plan` — naming the expected values of `synthesis_closure_form` and `synthesis_mandate_label` that Stage 0 will commit. Stage 5 ENTRY CONDITIONS cross-reference both fields "per ROLE A `stage0_precommit_verification_plan`" by field name. Creates the Stage 0 dimension of the C-27/C-31 chain pattern.

**V-03**: Stage 0 EXIT SIGNAL runs a MATCH/MISMATCH check: does `synthesis_closure_form: 'Chain closed.'` match the CAMPAIGN CLOSURE CANONICAL FORM table entry? Mismatch = `CLOSURE FORMAT ERROR. Halt.` Closes the gap where a campaign could have an internally inconsistent CANONICAL FORM and Stage 0 commitment without detection until Stage 5.
