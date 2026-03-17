Written to `simulations/quest/golden/corps-rob-variate-R7-2026-03-17.md`.

---

## R7 Summary

**Baseline**: V-05 R6 achieves the v6 ceiling -- 18 raw / composite 100 / tie-break 18. All three v6 criteria (C-24, C-25, C-26) pass. R7 cannot score higher under v6; the goal shifts to probing excellence patterns that could evolve the rubric to v7.

**Three open axes identified after V-05 R6:**

| Variation | Axis | What it probes |
|-----------|------|----------------|
| V-01 | D-ID Ref column in Findings table | C-25 currently enforced via prose constraint; V-01 makes the D-ID citation a 6th column in the finding row -- empty = visible format failure |
| V-02 | Blocker forward propagation rule | BLOCKER=YES has no structural obligation on the receiving stage; V-02 requires `[BLOCKER: F-ID from stage]` as the first entry in the next stage's PRIOR-STAGE ESCALATIONS |
| V-03 | Verdict calibration table | APPROVED/BLOCKED/DEFERRED are uncalibrated; V-03 adds a severity x resolution-status -> verdict mapping, making C-05 GO/NO-GO deterministic |
| V-04 | V-01 + V-02 | Inertia-finding citation + blocker reception, both column-level |
| V-05 | V-01 + V-02 + V-03 | Full integration -- every path from inertia-driven finding to blocking verdict to downstream reception is structurally enforced |

All five preserve the complete V-05 R6 architecture (Part 0, fill-slot, Displacement Map, table-first findings). None drop any v6-passing criterion.

**Predicted scoring against v6**: All five should match V-05 R6 at 18 raw / 100 composite (tie-break 18). The differentiation will appear if any axis produces an output quality marker the scorer identifies as an excellence signal -- which would seed C-27+ in a potential rubric v7.
