Written to `simulations/quest/golden/crew-review-golden-2026-03-17.md`.

**Score**: 225/225 | **Variation**: V-05 R20 (three-axis)

**What made it golden** (vs V-01 baseline):

1. **Three orthogonal chain-of-custody protocols** -- V-01 closes C-33 only (Applicability inheritance). V-05 adds §9 for C-34 (domain source anchored at step 1) and §3 Phase 1/2 split for C-35 (NH construction integrity). No protocol touches the others.

2. **Immutable Phase 1/Phase 2 NH split** -- V-01's NH table had no construction-order enforcement. V-05's Phase 1 (DIMENSION REGISTRATION: names, basis, scale) is immutable before Phase 2 (VALUE ASSIGNMENT) begins. Closes the back-fill failure mode: prose cannot retroactively reshape what was measured.

3. **Domain source committed at declaration time** -- V-01 referenced "from SCOPE DECLARATION" by text. V-05's §9 tags every IN-SCOPE surface with a `| Surface | Domain |` column at step 1, making the gap-check input set structurally anchored, not inferrable from findings. UNDECLARED-DOMAIN flag for any escape paths.

4. **Named alert syntax for every deviation** -- `INHERITANCE-DEVIATION-ALERT`, `NH-CONSTRUCTION-DEVIATION`, `UNDECLARED-DOMAIN` each name their failure mode explicitly. All surface in CROSS-ROLE SIGNALS; none silently pass.

5. **Order contract encodes protocol dependencies** -- §8 step annotations (`[domain tags committed here per §9]`, `[Applicability authority per §10]`, `[Applicability verbatim-copy from step 2 per §11]`) make the dependency graph explicit in the execution sequence itself.
