Written to `simulations/quest/golden/flow-resilience-variate-R12-2026-03-15.md`.

---

## Round 12 Variations — Summary

**Variation axes selected**:

| V | Axis | Target | Key intervention |
|---|---|---|---|
| V-01 | Lifecycle emphasis | C-15 | Gate 1 Argued-Impossible template: named `DS Primitive cited:` field + inline VALID/INVALID annotated examples |
| V-02 | Output format | C-36 | Gate 2b Column Contract added: explicit identity assertion — "chaos activation boundary expression IS the Trigger Condition threshold expression" — with Gate 2b precondition acknowledgement |
| V-03 | Output format | C-38 | Chaos-Observability Coverage Matrix replaced with Bidirectional form: Part A (chaos → signal) + Part B (signal → chaos) + CHAOS-OBS-GAP-NN + OBS-CHAOS-GAP-NN gap findings |
| V-04 | Combination | C-36 + C-38 | V-02 identity assertion + V-03 bidirectional matrix; C-15 absent (tests C-36/C-38 independence from C-15) |
| V-05 | Full integration | C-15 + C-36 + C-38 | All three: DS Primitive VALID/INVALID template + identity assertion column contract + bidirectional matrix |

**Design rationale per criterion**:

- **C-15**: The existing "Topic does not mention X is not a DS Primitive" prose is advisory. The `DS Primitive cited:` field with inline VALID/INVALID converts it to a structural gate violation, giving the model an inline scoring key to evaluate each Argued-Impossible instance before Gate 1 CLOSE.

- **C-36**: R11 V-05 used "copy the threshold expression" (reference). The v12 rubric requires "identity claim, not a reference link" in the template structure. The Gate 2b Column Contract places the word "IS" explicitly in a named fill requirement — not in prose, not in a row example — satisfying the rubric's "must appear in the template structure" condition.

- **C-38**: R11 V-05's matrix linked scenario → {chaos test present?, gap ID}. The v12 pass condition requires each chaos ID linked to Observable Signal IDs AND each Observable Signal ID linked back to chaos IDs. Part A and Part B are explicit separate tables with named gap finding types (CHAOS-OBS-GAP-NN / OBS-CHAOS-GAP-NN), satisfying "both directions verified" and "gap findings emitted."

**Persistent structural baseline from R11 V-05** (unchanged in all R12 variations): six-rule registry, bypass gate-reopening protocol, anti-omission architecture, Gate 2 column contract with Detection Horizon in Gate 3 observable signal columns (C-37), Gate 2b chaos rows linked to Trigger Condition threshold, detection horizon as concrete time window in gap tables.
