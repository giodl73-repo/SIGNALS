`simulations/quest/golden/flow-resilience-variate-R4-2026-03-15.md` written.

---

## Round 4 Variations — Summary

**New criteria targeted**: C-16 (named gate-state vocabulary), C-17 (permanently BARRED entries as coverage gaps), C-18 (explicit phase entry/exit conditions), C-15 strengthened (DS Primitive cited: field + VALID/INVALID examples).

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | Named gate-state vocabulary (C-16) | Defining the three-label vocabulary (`Include` / `BARRED` / `Argued-Impossible`) and explicitly rejecting "Flagged" as a label eliminates the free-text workaround that let R3 earn only PARTIAL on C-16. The OPEN/CLOSED gate binary is declared after every discovery phase. |
| **V-02** | Barred-entry lifecycle to coverage gaps (C-17) | Introducing a `BARRED Resolution Gate` with a `Permanently BARRED` list forces every BARRED entry to either resolve or produce a named `CG-NN` entry. The reader can distinguish "analyzed, excluded" from "not analyzed." |
| **V-03** | Explicit phase entry/exit conditions (C-18) | Each of four gates carries a stated entry condition (citing prior gate IDs) and a stated exit condition (what must be true). Phases cannot run out of order; closure must be declared, not inferred from prose position. |
| **V-04** | Gate-state vocabulary + barred-entry lifecycle (C-16 + C-17) | The named vocabulary is a prerequisite for the tracking mechanism — both in a single prompt creates a closed loop from discovery disposition to coverage gap registry, without the full formal sequencing overhead. |
| **V-05** | Full formalization — all four v4 changes (C-15 + C-16 + C-17 + C-18) | Six gates with explicit entry/exit conditions, a BARRED Register phase, an Impossibility Register with `DS Primitive cited:` + `VALID:` / `INVALID:` counter-examples, and a Coverage Gap Registry. Every entry is traceable from Gate 1 to final artifact. |

**Single-axis variations** (V-01, V-02, V-03): test whether each new criterion can be earned with a focused, minimal mechanism.

**Combination variations** (V-04, V-05): test whether the mutual reinforcement between vocabulary, lifecycle tracking, and formal sequencing is necessary to earn all three simultaneously, or whether any two are sufficient for their respective criteria.
