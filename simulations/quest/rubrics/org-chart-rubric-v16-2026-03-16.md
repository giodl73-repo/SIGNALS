Written to `simulations/quest/rubrics/org-chart-rubric-v16-2026-03-17.md`.

---

## v16 summary

**One new criterion** extracted from Round 15 excellence signals:

**C-45** -- CHECKPOINT-0 pass checklist item (b) inline artifact enumeration (behavior, 5 pts)

The signal comes from the V-01 vs. V-02 C-43 PASS/PARTIAL divergence:

- **V-01 PASS**: item (b) enumerates all four transitions inline within the checkbox body as a parenthetical list -- `(GATE 0->1: typed role list, GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE, GATE 2->3: org diagram, GATE 3->STATUS: charter set)`
- **V-02 PARTIAL**: item (b) says "All four gate->artifact pairs are known by name as listed above" -- pointer-reference form, deferring to the inventory block

**The bypass C-43 leaves open:** C-43 requires an affirmative PASS CHECKLIST with an item confirming knowledge of all four transitions -- but does not specify that the transitions must be enumerated inline within the checkbox body. A pointer-reference form satisfies C-43's confirmation requirement without forcing the model to re-emit all four gate+artifact pairs at checkpoint execution time. C-45 closes this: inline enumeration is self-contained and verifiable at the checkpoint location without cross-referencing the inventory block.

**Subsumes C-43.** Extends the deepening chain to five stages:

```
C-38  explicit GATE CHAIN block with named artifact handoffs
  +-- C-40  pre-GATE 0 preamble position
       +-- C-42  CHECKPOINT-0 FAIL condition (consultation-blocking)
            +-- C-43  CHECKPOINT-0 pass checklist with artifact enumeration
                 +-- C-45  CHECKPOINT-0 pass checklist item (b) inline enumeration
```

**Updated totals: 275 pts. Golden = 220/275 (80%).**
