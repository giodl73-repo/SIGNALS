Written to `simulations/quest/rubrics/org-chart-rubric-v17-2026-03-17.md`.

---

## v17 summary

**One new criterion** extracted from Round 16 excellence signals:

**C-46** -- CHECKPOINT-0 pass checklist item (b) anti-pointer prohibition (behavior, 5 pts)

The signal comes from V-03's explicit DO NOT prohibition:

> `DO NOT write item (b) in pointer-reference form (e.g., "as listed above" or "as enumerated in the inventory block") -- the four transitions MUST be restated inline`

**The bypass C-45 leaves open:** C-45 requires inline enumeration as a positive instruction but names no prohibited forms in the spec itself. A model following a C-45-satisfying spec knows "enumerate inline" but has no named anti-form to close the reversion path. At execution time, especially when the ARTIFACT-HANDOFF INVENTORY block is nearby, the model can revert to pointer-reference form — satisfying C-43 (confirmation present) while failing C-45. C-46 closes this: the named prohibition with two example banned forms makes reversion impossible without violating an explicit in-spec rule.

**Subsumes C-45.** Extends the deepening chain to six stages:

```
C-38  explicit GATE CHAIN block with named artifact handoffs
  +-- C-40  pre-GATE 0 preamble position
       +-- C-42  CHECKPOINT-0 FAIL condition (consultation-blocking)
            +-- C-43  CHECKPOINT-0 pass checklist with artifact enumeration
                 +-- C-45  CHECKPOINT-0 pass checklist item (b) inline enumeration
                      +-- C-46  CHECKPOINT-0 pass checklist item (b) anti-pointer prohibition
```

**Updated totals: 280 pts. Golden = 224/280 (80%).**
