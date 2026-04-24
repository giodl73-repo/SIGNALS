Written to `simulations/quest/golden/flow-trigger-variate-R11-2026-03-16.md`.

---

## flow-trigger — Round 11 Variations

**New criteria targeted:** C-27 (computable exit signal), C-28 (per-obligation refutation conditions), C-29 (INERTIA CONTRAST as inline columns)

### Variation table

| Var | Axis | Hypothesis |
|-----|------|------------|
| **V-01** | Output format — typed status aggregate (C-27) | Phase 0 exit conditions as a named `Status` enum column (`SATISFIED\|PENDING\|BLOCKED`). EXIT SIGNAL becomes a counted aggregate ("5/5 SATISFIED") derivable by scanning the column — no semantic evaluation. Adds FM-38 for uncomputable signals. |
| **V-02** | Lifecycle emphasis — per-obligation refutation conditions (C-28) | Each Phase 0 obligation gets a co-located `Violated if:` clause naming a string-detectable breach. Extends C-24's breach-token principle upstream: violation is a named property of the artifact, not something rubric re-scoring discovers. Adds FM-39 for absent refutation clauses. |
| **V-03** | Inertia framing — INERTIA CONTRAST as typed inline columns (C-29) | `Weaker alternative` and `Failure mode` become typed column headers in the Phase 0 registry (not a separate section). Rationale is non-separable at cell level — removing the INERTIA CONTRAST section heading strips nothing because the columns live in the obligation table. Adds FM-40. |
| **V-04** | Role sequence + Output format — computed inter-role gate (C-27 + role boundary) | Phase 0 is a sealed Role 0 that produces a computable aggregate. Role 1 (Auditor) carries an explicit entry check: "AUTHORIZED when count(Status = SATISFIED) = 5." The inter-role gate resolves mechanically from the status column before any content is evaluated. |
| **V-05** | Output format + Inertia framing — unified 7-column Phase 0 registry (C-27 + C-28 + C-29) | All three criteria merged into one table with 7 named columns: EC-ID, Exit Condition, Required Artifact, Status, Violated if, Weaker alternative, Failure mode. Each row is simultaneously self-computing, self-detecting, and self-motivating. The Phase 0 table alone is sufficient for full evaluation of all three new criteria. |

### Structural relationship of the three new criteria as reflected in the variations

- **C-27** (V-01, V-04, V-05): moves EXIT SIGNAL from assertion → aggregate count
- **C-28** (V-02, V-05): moves violation detection from rubric re-scoring → string inspection
- **C-29** (V-03, V-05): moves design rationale from section level → cell level (non-separable)

V-05 is the strong candidate for golden advancement — it unifies all three into one table that satisfies all three criteria from a single scan pass.
