**flow-trigger-rubric-v8** written to `simulations/quest/rubrics/flow-trigger-rubric-v8-2026-03-16.md`.

---

**Three new aspirational criteria (C-27–C-29), N_aspirational: 18 → 21, max (raw): 110 → 117.5:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-27 | V-02 advance — Status enum aggregate | Phase 0 exit signal must be *computable* from typed per-condition status values (`SATISFIED/PENDING/BLOCKED`), not a declarative free-text assertion; evaluator re-derives exit decision by counting status column rows | C-25 (the exit signal it makes computable) |
| C-28 | V-03 advance — Article refutation conditions | Each named Phase 0 obligation carries a co-located refutation condition — an explicit "violated if [X]" statement inspectable by string match or structural scan, without rubric re-evaluation; applies the C-24 breach-token principle upstream to Phase 0 obligations | C-25 (the obligations it makes violation-detectable), C-24 (the breach-visibility principle it extends) |
| C-29 | V-05 pattern — INERTIA CONTRAST inline columns | C-26's contrast section becomes typed columns within the mechanism's own registry row ("Weaker alternative" and "Failure mode" columns), so rationale is co-located at cell level rather than section level — rationale cannot be stripped by removing a heading | C-26 (the rationale co-location it strengthens from section-level to cell-level) |

**Structural relationship:** C-27 makes Phase 0 exit trustworthiness self-verifiable (status aggregate, not assertion); C-28 makes Phase 0 violation self-detectable (refutation conditions, not rubric re-scoring); C-29 makes structural rationale non-separable from the mechanism it motivates (cell columns, not a section). Together they complete a self-explaining, self-enforcing, self-verifying Phase 0 gate: an evaluator can check completion (C-27), detect violation (C-28), and read motivation (C-29) from the Phase 0 registry alone, without consulting the rubric.
