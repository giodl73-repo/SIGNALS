Written to `simulations/quest/golden/prove-topic-variate-R16-2026-03-16.md`.

---

## prove-topic — Variate Round 16 (rubric v14)

**Anchor**: R15 V-05 (roles + tables + lifecycle gates + inertia framing, correct sequence)

**Three new axes explored, then combined:**

| Var | Axis | Mechanism | Primary criteria targeted |
|-----|------|-----------|--------------------------|
| V-01 | session_invariants | SESSION INVARIANTS block — 4 fields declared read-only after CAMPAIGN OPEN; stages reference by SI-NN field name only | C-02 (scout integrity, no re-inference) |
| V-02 | atomic_dual_lock | DUAL-LOCK GATE in Stage 5 — `hypothesis_verdict [LOCKED]` AND `displacement_conclusion [LOCKED]` both required before `synthesis_complete` fires | C-04 (synthesis completeness) |
| V-03 | counter_hypothesis_resolution_block | Stage 5 split into BLOCK 1 (resolve counter_hypothesis → typed resolution_verdict) + BLOCK 2 (synthesis verdict); BLOCK 2 gated on BLOCK 1 | C-05 (counter-hypothesis resolution) |
| V-04 | session_invariants + atomic_dual_lock | V-01 + V-02 without full structural stack | C-02, C-04 |
| V-05 | all three + R15 V-05 full stack | SESSION INVARIANTS + ATOMIC DUAL-LOCK + two-block Stage 5 on top of numbered dependency roles, table evidence, displacement template, lifecycle exit signals | C-01 through C-05 + recommended/aspirational |

**Why these axes**: The two structural gaps in R15 V-05 are (a) fields can drift mid-campaign and (b) synthesis can exit with the displacement case blank. V-03 targets the third gap: no explicit gate forces the counter-hypothesis to be resolved before the verdict. V-05 tests all three simultaneously on the proven R15 base.
