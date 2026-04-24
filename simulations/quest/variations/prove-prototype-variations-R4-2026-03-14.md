**Round 4 variations written** to `simulations/quest/scorecards/prove-prototype-variate-R4-2026-03-14.md`.

---

## Summary

Five complete variations targeting the two new v4 criteria:

| Variation | Axis | C-18 Mechanism | C-19 Mechanism |
|-----------|------|----------------|----------------|
| **V-01** | Table-dominant | Sections 6, 8, 9 each end with Disposition A/B terminal element | Inline `*[Gate: ...]*` labels within each ordering-constrained section |
| **V-02** | Phase gates | Phases 6, 8, 9 each end with A/B disposition before gate-check line | `*Execute before Phase N*` / `*Execute before any build activity*` inline per phase |
| **V-03** | Labeled-pair blocks (no tables) | Blocks 6, 8, 9 each end with two-path terminal labeled pair | Bracketed gate labels in each block header |
| **V-04** | Conversational/imperative | Steps 5, 7, 8 each close with "exactly one of the following two sentences" | Model writes `Measurement protocol established before build.` gate line inline at Step 2 |
| **V-05** | Hybrid (phase gates + tables) | Phases 6, 8, 9 each have A/B phase-close block | Inline `*[Phase gate: ...]*` labels in every phase header + output contract |

**Key design decision for C-19**: The R3 V-01 output contract at the end was not sufficient alone. All five variations add gate markers *within* each constrained section, not only in the end-of-document contract. V-01 and V-05 retain the output contract as a second enforcement pass; V-02 uses phase-check lines inline; V-04 has the model write the gate line itself into the output.

**Key design decision for C-18**: R3 V-01 had binary closure only on Section 6 (counter-evidence, per C-16). V4 generalizes this to all optional sections: counter-evidence, limitations, and replication path. Every variation now closes those three sections with exactly one of two named dispositions.
