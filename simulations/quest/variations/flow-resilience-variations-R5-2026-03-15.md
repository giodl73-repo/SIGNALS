Written to `simulations/quest/golden/flow-resilience-variate-R5-2026-03-15.md`.

---

## Round 5 Variations — Summary

**Three new criteria targeted** (extracted from R4 excellence signals):

| Criterion | Source | What it closes |
|-----------|--------|----------------|
| C-19 | V-03 R4 gate templates | OPEN gates must name the *specific* blocking item (entry ID, class+count, pending verdict ID), not just a category |
| C-20 | V-03 R4 amendment pattern | Downstream CR findings must explicitly re-open the prior gate, cite the finding by ID, and re-close under a labeled sub-gate; no-amendment confirmation is mandatory |
| C-21 | V-05 R4 Capability field | Commerce operation list must be declared *before* Gate 1, not discovered from the scenario table; checked against final coverage |

---

**Five variations**:

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | C-21 only — pre-analysis scope declaration | Upfront `SCOPE DECLARATION COMPLETE` block + end-of-analysis `Scope Verification` section makes In-scope/Excluded/Gap tripartite distinction visible and checkable |
| **V-02** | C-19 only — specific Reason-if-OPEN | Replaces `[which condition is not met]` (category) with `[entry ID / class+count / pending verdict ID / outstanding amendment ID]` (specific item); bare OPEN is an error |
| **V-03** | C-20 only — sub-gate amendment protocol | Three-step amendment protocol: `GATE 3: REOPENED — triggered by CR-NN` → `DCV-CR-NN` → `GATE 3a: AMENDED — triggered by CR-NN / CLOSED`; mandatory No-Amendment Confirmation when none needed |
| **V-04** | C-21 + C-19 | Scope declaration preamble + specific Reason-if-OPEN on every gate — two independent audit points, entry (what will be covered) and transition (what is blocking closure) |
| **V-05** | C-19 + C-20 + C-21 + C-15–C-18 | Full R5 formalization: scope declaration before Gate 1, specific Reason-if-OPEN throughout, sub-gate amendment protocol in Gate 4, plus all prior R3/R4 structural mechanisms |

**Key structural changes in V-05 vs R4 V-05**:
1. `SCOPE DECLARATION COMPLETE` block precedes Gate 1
2. Every gate's `Open condition (if OPEN):` field renamed/tightened to `Reason if OPEN:` requiring a *specific named item*
3. Gate 4's `GATE 3 AMENDMENT: ... / GATE 3 REMAINS CLOSED` replaced with three-step sub-gate protocol with mandatory citation
4. `SCOPE VERIFICATION` section appended after Gate 4
