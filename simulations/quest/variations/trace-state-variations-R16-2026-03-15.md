Written to `simulations/quest/golden/trace-state-variate-R16-2026-03-15.md`.

---

## Round 16 — trace-state Variations Summary

Five complete prompt bodies targeting the five new v14 criteria (C-40–C-44):

| Var | Axis | New Criteria | Key Innovation |
|-----|------|-------------|----------------|
| **V-01** | Role sequence Finance → Sales → CS | C-40, C-41, C-42 | Pass headings carry ordering hypothesis (C-42); explicit bridge tables link pass N postconditions to pass N+1 preconditions (C-41); per-pass defect log enforces independent coverage (C-40) |
| **V-02** | Step-block single-pass + lifecycle emphasis | C-43, C-44 | Phase labels in every Starting/Ending State field (`Lead [phase: Acquisition]`) (C-43); 4 mandatory sub-steps per record each with independent state triple (C-44) |
| **V-03** | Role sequence CS → Finance → Sales (non-standard) | C-40, C-42 | CS-first hypothesis annotated as InvariantViolation-class target; Finance-second as MissingPrecondition; each pass heading names its defect-class rationale; per-pass defect logs confirm class coverage |
| **V-04** | Step-block multi-pass Sales → CS + lifecycle | C-41, C-43 | Explicit bridge block between passes (C-41) with named PreconditionSeed/InvariantPropagation/StateConstraintForward entries; phase labels throughout step-block state fields (C-43) |
| **V-05** | All five new criteria ceiling | C-40, C-41, C-42, C-43, C-44 | Tabular multi-pass with phase labels in all state cells + ordering hypothesis at pass headings + cross-domain bridge tables + per-pass defect + Defect Analysis sub-steps decomposed into 3-step before/op/after triples |

**Design decisions:**
- C-42 is strictly multi-pass (single-pass formats cannot satisfy it) — V-02 correctly excludes it
- C-41 is multi-pass-only — V-02 and V-03 (no bridge table) correctly exclude it
- C-44 in V-05 is achieved through Defect Analysis sub-steps rather than operation sub-steps, avoiding format conflict with tabular trace rows
- V-05 projected ceiling: **90.0** composite (50 essential + 30 recommended + 10 aspirational) if all prior criteria also pass
