Written to `simulations/quest/rubrics/org-roles-rubric-v10-2026-03-16.md`.

---

**6 new criteria extracted from Round 9 excellence signals:**

| ID | Source | Pattern | Distinguishes from |
|----|--------|---------|-------------------|
| **C-42** | R9 V-01/V-04/V-05 (PARTIAL C-38: enumeration embedded in Phase 1) | Enumeration of all verify questions is a standalone named phase that precedes and never shares a label with the anchor-orthogonality phase | C-38 requires three named phases including enumeration; C-42 requires enumeration to be a clean standalone phase — never merged with anchor-orthogonality under a single phase header |
| **C-43** | R9 V-01/V-04/V-05 (PARTIAL C-38: resolution not labeled as a phase) | Revision/resolution step carries its own top-level named phase header at the same structural level as the checking phases | C-38 requires a revision step; C-43 requires that step to be a separately labeled named phase, not an appended trailing instruction |
| **C-44** | R9 V-02/V-04 (GAP-{slug} identifiers vs. R8 V-03/R9 V-01 positional "Gap N") | Gap analysis artifact assigns formal slug identifiers; downstream POSITIVE SOURCING and Diagnosis Card fields cite slugs, not positions | C-41 requires the provenance field to reference a named entry; C-44 requires that reference to use a stable slug key rather than a position-dependent label |
| **C-45** | R9 V-02/V-04 (per-expert POSITIVE SOURCING inline records) | Each expert derivation record contains an explicit inline sourcing field citing the specific GAP-{slug} and vocabulary term used in the expert's name | C-40 requires the positive naming constraint at gate or step level; C-45 requires it embedded as a format field within every individual derivation record |
| **C-46** | R9 V-03/V-04 (YAML persistence of `orthogonality` field) | Non-anchor YAML role files include an `orthogonality` field persisted from the Diagnosis Card's orthogonality-to-anchor statement | C-37 tests the per-card orthogonality field in Diagnosis Cards; C-46 tests whether that claim is carried through into the emitted YAML role files |
| **C-47** | R9 V-03/V-04 (YAML persistence of `inertia_gap_inherited` field) | Domain expert YAML role files include an `inertia_gap_inherited` field completing the three-artifact chain (gap artifact → Diagnosis Card → YAML role file) | C-41 tests the Diagnosis Card provenance field; C-47 tests whether the same inheritance is persisted into the final emitted YAML |

**Formula**: `/33` → `/39`. R9 V-04 leads at **99.36** — the R10 frontier is combining V-04's full pipeline with C-42 + C-43 PASS (which also upgrades C-38 from PARTIAL to PASS) to reach **39/39 = 100.00**.

**Cross-round ceiling under v10**: R9 V-04 at 99.36, V-05 at 99.10, V-02/V-03 tied at 98.46, V-01 at 98.33.
