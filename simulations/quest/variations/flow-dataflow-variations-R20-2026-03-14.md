Written to `simulations/quest/golden/flow-dataflow-variate-R20-2026-03-15.md`.

---

## Summary

**5 complete variations (V-01 through V-05)** targeting C-54 + C-55 in v19 rubric.

### Variation axes used

| Var | Axis | Domain | Sequence | SCs | [A-00] columns | Phase Gate 0 items |
|-----|------|--------|----------|-----|----------------|--------------------|
| V-01 | Lifecycle emphasis | Healthcare claims adjudication | F→O→C | 15 | 3 | 2 |
| V-02 | Role sequence | Automotive warranty claims | **C→O→F** (new) | 15 | 3 | 2 |
| V-03 | Output format | Telecom billing mediation | F→O→C (prose) | 15 | 3 (prose enum) | 2 (prose pre-conditions) |
| V-04 | Role sequence + inertia | Insurance premium refund | **F→C→O** (new) | 15 | 3 | 2 |
| V-05 | Lifecycle + role sequence | Media streaming royalties | O→C→F | 16 | **4** | **3** |

### Key C-54/C-55 mechanics per variation

- **V-01**: Clean reference — SC-0 + SC-14 each carry `[A-00]` in governed-artifact and enforcement slots independently. Phase Gate 0 has two items (row count + Responsible Role completeness).
- **V-02**: Same C-54/C-55 pattern under a new non-natural role sequence (C→O→F, not used in R19). Skip-level crosses to Finance as the last role.
- **V-03**: Prose-mode equivalent — SC-14 substitution governs `Responsible Role:` as a labeled phrase per enumeration item rather than a column cell. Phase Gate 0 is a two-condition prose pre-condition.
- **V-04**: Combines heavy inertia framing (≥7 incumbent steps in Finance) with F→C→O (new in R20). SC-12 governs Operations citing Finance skip-level.
- **V-05**: Deepest: 4-column index adds `SLA Impact` (Yes/No) governed by SC-15. Three independent [A-00]-governing SCs (SC-0, SC-14, SC-15), each with dual-slot anchoring. Phase Gate 0 has three structural items.
