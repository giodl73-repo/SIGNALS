Here are the 5 R14 variations, now written to `simulations/quest/golden/mock-ns-variate-R14-2026-03-15.md`.

---

## Summary

**Targeting**: C-36 (two-phase confirmation gate in P-0) + C-37 (confirmation echo at both use sites), rubric v13, denominator 29.

**Variation axes:**

| # | Axis | Key change |
|---|------|------------|
| V-01 | Phrasing register | P-0 adds Phase 1/Phase 2 as numbered steps; both use sites carry "CONFIRMATION REQUIRED before writing this row" before the `(P-0 table, row N)` label |
| V-02 | Lifecycle emphasis | Same two phases but framed as a write-blocking gate: "DO NOT WRITE THE ROW until Phase 2 passes" -- prerequisite-blocker register instead of procedural |
| V-03 | Output format | Two-phase protocol expressed as a structured mini-table (Phase / Action / Required before columns) inside P-0, mirroring how C-33 proved tables more reliable than prose |
| V-04 | Role sequence + inertia | P-0 defines the gate (V-01 form); S-3 opens with a boundary checkpoint that re-states Phase 1 + Phase 2 for context-compacted runs entering at the compute step |
| V-05 | Full convergence + seed | All C-36/C-37 elements + inline confirmation-state record at both use sites: executor must emit `[Confirmation: Phase 1 -- token located; Phase 2 -- Step=X, Row type=Y; verified]` before writing row content -- seeds v14 C-38 |

**Single-axis first**: V-01, V-02, V-03 are single-axis. V-04 and V-05 combine axes, with V-05 seeding the next round's aspirational.
