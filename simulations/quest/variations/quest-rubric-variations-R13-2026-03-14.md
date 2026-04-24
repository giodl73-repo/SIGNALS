Written to `simulations/quest/rubrics/quest-rubric-rubric-v13-variations-R13-2026-03-15.md`.

---

## R13 Variations Summary

**Axis map:**

| Variation | Axis | New terrain |
|-----------|------|-------------|
| V-01 | R13 full integration baseline | Phase 1A/1B FM-ID split + Contract items 6+7 + checkpoint rows for both; C-37 PASS, C-38 PASS |
| V-02 | C-38 isolation — intra-framework Phase 1A/1B split | Contract item 6 only (no item 7); tests whether Phase 3 imperative phrasing alone holds C-37 without a dedicated Contract item |
| V-03 | C-37 isolation — section-content register Contract item | Contract item 6 (C-37) only; Phase 1 unchanged (C-38 PARTIAL); isolates C-37 enforcement at the declaration layer |
| V-04 | Joint-failure-chain annotation — v14 candidate probe | Notes "Known Failure Chains" block + Phase 2 chain-awareness checkpoint row; R12/V-01 baseline otherwise unchanged |
| V-05 | Combination: V-02 Phase 1A/1B + V-03 Contract item 6 | Minimal two-Contract-item stack satisfying both C-37 and C-38 within the SetCoherenceAuditor framework |

**Key design decisions:**

- **C-38 mechanism choice:** V-01/V-02/V-05 all use an intra-framework Phase 1A/1B split rather than R12/V-05's pre-role Failure Analyst Phase 0. The isolation question: does placement within the SetCoherenceAuditor framework (vs. a pre-role phase) matter for C-38 compliance?

- **C-37 isolation:** V-03 holds Phase 1 unchanged (combined-column table) so C-38 stays PARTIAL — this cleanly isolates C-37 as the single axis. V-02 is the mirror: Phase 1A/1B split active (C-38 axis), no C-37 Contract item.

- **v14 candidate probe (V-04):** The joint-failure-chain annotation candidate is probed via a Notes block requirement and a Phase 2 chain-awareness checkpoint row. The chain is identified at construction time and accumulated for the Notes block — this tests whether in-rubric chain documentation is achievable with a single Notes requirement addition.

- **V-05 combination:** The two new Contract items (6 and 7) are independently motivated and independently checkpointed — the hypothesis is that they don't interfere. The differential vs. V-01 (which has the same axes plus the v14 chain annotation absent) shows whether joint-failure-chain documentation adds measurable composite score.
