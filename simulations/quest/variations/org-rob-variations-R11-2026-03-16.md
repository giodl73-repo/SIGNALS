Written to `simulations/quest/golden/corps-rob-variate-R11-2026-03-16.md`.

---

## Variate R11 -- org-rob

**Context:** V-03 R10 hit 128/128 under v10. R11 probes beyond the ceiling to find C-28.

### Variation Axes

| | Axis | Target |
|---|---|---|
| V-01 | Risk-finding traceability -- `Source-LIDs:` column in risk register + VIOLATION-12 | C-28 candidate |
| V-02 | Stage prerequisite registry -- document-level prereq table before Stage 1 + VIOLATION-12 | C-28 candidate |
| V-03 | Evidence tier grading -- `Evidence:` field on findings + VIOLATION-12/13 | C-28 candidate |
| V-04 | V-01 + V-03 (risk traceability + evidence tiers) | C-28 x2 |
| V-05 | Full convergence -- all three + VIOLATION-12..15, five enforcement loops total | C-28 discovery |

### Three C-28 Candidate Dimensions

**Dimension A -- Risk Provenance** (V-01, V-04, V-05): The risk register has `Inertia Link` but no pointer to the findings that justified each risk entry. `Source-LIDs` creates bidirectional ledger-to-risk traceability parallel to how C-12 creates finding-to-finding traceability.

**Dimension B -- Document-Level Sequencing** (V-02, V-05): Phase gates (C-11) define per-stage conditions but no document-level execution dependency graph exists before Stage 1 runs. The `STAGE PREREQUISITE REGISTRY` occupies the same pre-stage position as `INERTIA BASELINES` and makes ordering structurally verifiable before execution begins.

**Dimension C -- Evidence Quality Gating** (V-03, V-04, V-05): Findings carry severity but no evidentiary basis. `Evidence: DOCUMENTED / OBSERVED / INFERRED` as the third column (after `Via:`, preserving C-19) gates HIGH INFERRED findings and blocks GO verdicts over unresolved INFERRED concerns.

### Strongest C-28 Candidate
Dimension A (risk provenance) is the smallest increment with the cleanest criterion definition -- it adds `Source-LIDs` to an already-specified artifact (C-07) without restructuring anything else. Dimension C is the richest addition but may be two criteria. **R12 should score all five variations to extract the clearest ++ threshold.**
