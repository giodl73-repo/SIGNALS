Written to `simulations/quest/rubrics/quest-variate-rubric-v12-variations-R12-2026-03-15.md`.

---

# quest-variate — R12 Variations

## R12 Design Notes

The R12 key structural move is the **C-36 independent ablation** (V-02). In R11, V-02 ablated C-35 (no manifest), which entailed C-36 failure as a side effect — both criteria fell together, so C-36 was never isolated. R12/V-02 fixes this: the manifest is fully present (C-35 satisfied), but the Phase 3 STOP CONDITION uses generic language. This is the first round where C-36 is tested with the manifest present.

Predicted scoring under v12 (denominator: 29):

| Tier | Variation | Score | Failures |
|------|-----------|-------|---------|
| 1 | V-01 | 100.00 | -- |
| 2 | V-02, V-04 | 99.66 | C-36 / C-31 (single ablations, manifest retained in both) |
| 3 | V-03, V-05 | 99.31 | V-03: C-35+C-36 entangled; V-05: C-36+C-31 combination |

**Key asymmetry vs R11:** R12's tier 2 is symmetric (V-02 and V-04 both score 99.66). In R11, the C-35 ablation sat a tier below the C-31 ablation because it entailed C-36. R12 resolves that: C-36 alone is one failure, just like C-31 alone.

---

## Variation Summary

| V-ID | Axis | What changes | C-35 | C-36 | C-31 | Score |
|------|------|-------------|------|------|------|-------|
| V-01 | Full R12 baseline | Nothing — all criteria present | pass | pass | pass | 100.00 |
| V-02 | C-36 ablation (new in R12) | Phase 3 STOP CONDITION uses generic phase-completion language; manifest fully present | pass | **fail** | pass | 99.66 |
| V-03 | C-35 ablation = R11/V-02 state | No manifest table; Phase 2 ends at STOP CONDITION, transitions directly to Phase 3 | **fail** | **fail** (entailed) | pass | 99.31 |
| V-04 | C-31 ablation = R11/V-03 state | Predicted-site column: V-IDs required but no conditional if-then framing | pass | pass | **fail** | 99.66 |
| V-05 | Combination C-36 × C-31 | Manifest present, Phase 3 gate generic (V-02 axis) + directional predicted-site (V-04 axis) | pass | **fail** | **fail** | 99.31 |

---

## V-01 — Full R12 baseline

**Axis:** Baseline — R12 full stack: all R11 structures retained (SetCoherenceAuditor persona, role-constitutive obligations preamble with manifest duty, five-column planning table with FROM/TO secondary-effect column header and V-ID citation gate, uniform imperative stop conditions, per-variation checkpoint with set-level predicates, Phase 2 Variation Completion Manifest with internal *Prevents:* label and Manifest STOP CONDITION) plus C-36 mechanism: Phase 3 STOP CONDITION names the Variation Completion Manifest by name as the specific evidence artifact

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | V-01's Phase 3 STOP CONDITION will contain the phrase "Variation Completion Manifest" as the named evidence artifact — specifically in the sentence "All 5 rows in the Variation Completion Manifest are filled and confirmed with no noted-but-unresolved failures"; V-02's Phase 3 STOP CONDITION will contain no reference to "Variation Completion Manifest" by name — the absence of this phrase in V-02's Phase 3 STOP CONDITION block is the positive falsification anchor |
| Secondary effect | Naming the manifest in the Phase 3 gate shifts completion-gate specificity FROM phase-level sequencing TO artifact-level evidence, potentially increasing gate resolution fidelity in V-01 while shifting truncation-detection responsibility FROM undetected Phase 3 emission TO explicit pre-emission manifest verification |
| Predicted sites | V-02 (C-36 ablation, manifest present): if V-01 shows lower Phase 3 premature-entry incidence than V-02 despite identical manifest presence, the Phase 3 gate artifact-name coupling adds enforcement beyond the manifest's own Manifest STOP CONDITION; equivalence means C-36 does not warrant independent criterion status |

*(Full skill body in output file)*

---

## V-02 — C-36 ablation *(new in R12)*

**Axis:** C-36 ablation — Phase 3 STOP CONDITION uses generic phase-completion language ("Do not begin Phase 3 until Phase 2 is complete"); does not name the Variation Completion Manifest by name; manifest table fully present in Phase 2 (C-35 satisfied)

The single-character change: Phase 3 gate reads `Do not begin Phase 3 until Phase 2 is complete and all per-variation checkpoints have passed with no noted-but-unresolved failures` instead of `All 5 rows in the Variation Completion Manifest are filled and confirmed...`.

---

## V-03 — C-35 ablation (R11/V-02 state exactly)

**Axis:** C-35 ablation — Phase 2 Variation Completion Manifest absent; Phase 3 STOP CONDITION retained (C-29 compliant); R11/V-02 state exactly; C-36 entailed by C-35 absence

The manifest obligation line is removed from the preamble. Phase 2 ends at the Phase 2 STOP CONDITION and transitions directly to the Phase 3 heading. Both C-35 and C-36 fail.

---

## V-04 — C-31 ablation (R11/V-03 state exactly)

**Axis:** C-31 ablation — Predicted-manifestation-site column requires sibling V-ID citation (C-19 satisfied) but drops the conditional if-then structure requirement; R11/V-03 state exactly; manifest and Phase 3 manifest-name coupling fully retained

Column header drops `using conditional if-then structure: "if [baseline] outperforms [sibling] on [observable metric], [mechanism] adds [type of] value beyond [competing mechanism]"`.

---

## V-05 — Combination C-36 × C-31

**Axis:** Combination pass — C-36 ablation × C-31 ablation; superadditivity test: V-02 tests C-36 alone, V-04 tests C-31 alone; V-05 tests whether the compound degrades output quality more than either single ablation

**Hypothesis primary effect:** V-05 contains both ablations simultaneously — no manifest name in Phase 3 gate (V-02 axis) and no conditional if-then in predicted-site column (V-04 axis). The co-presence of both structural weaknesses in the same body is the falsification anchor.
