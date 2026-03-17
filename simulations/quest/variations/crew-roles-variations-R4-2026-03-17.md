Written to `simulations/quest/golden/crew-roles-variate-R4-2026-03-17.md`.

---

## crew-roles — Variate R4 Summary

**The gap entering R4**: R3 V-05 scored 100 on v3 but C-20 (Q-domain-aligned vocabulary distribution) is the only new criterion it doesn't fully satisfy. Phase 2 requires `[vocab: {term}]` annotations but allows same-term reuse and cross-domain selection.

**Variation axes chosen**:

| Variation | Axis | C-17 | C-18 | C-19 | C-20 |
|-----------|------|------|------|------|------|
| V-01 | Three-bucket Phase 1 (prevent cross-domain at selection time) | PASS | PASS | PASS | PASS |
| V-02 | Domain-alignment audit table at Phase 2 exit (catch cross-domain after writing) | PASS | PASS | PASS | PASS |
| V-03 | Dedicated Phase 3 frame-fill step (pre-resolve Q-slots before file write) | PASS | PASS | PASS | PARTIAL |
| V-04 | V-01 buckets + V-03 frame-fill (both C-20 prevention + C-19 pre-resolution) | PASS | PASS | PASS | PASS |
| V-05 | Full synthesis: buckets + alignment audit + frame-fill + phase entry/exit conditions | PASS | PASS | PASS | PASS |

**Key design decisions**:

- **V-01 vs V-02**: Two orthogonal angles on C-20. V-01 prevents wrong-bucket selection by constraining the vocabulary menu at Phase 1. V-02 allows any selection and audits alignment after — detects failures V-01 could theoretically miss if inferred terms are miscategorized.
- **V-03**: Isolates the C-19 pre-resolution hypothesis. Adding Phase 3 as a standalone frame-fill step means the filled sentence is a completed artifact before Phase 5 begins — no slot instruction to drift. V-03 doesn't use buckets, so C-20 is still PARTIAL (no per-answer domain constraint).
- **V-05**: Full synthesis. Six phases. Phase 1 builds three-bucket vocabulary. Phase 2 uses bucket-constrained annotations + domain-alignment audit table. Phase 3 fills the frame. Phase 4 runs the scope audit. Phase 5 writes with all constraints. Phase 6 is the 4-check blocking gate. Every C-17/C-18/C-19/C-20 mechanism fires before the point where correction would require undoing completed work.
