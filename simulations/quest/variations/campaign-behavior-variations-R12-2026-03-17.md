Written to `simulations/quest/golden/campaign-behavior-variate-R12-2026-03-17.md`.

---

## R12 Variations — Summary

**Context:** R11 V-05 already scores 90/90 under v10. R12 explores structural territory *beyond* the current ceiling, targeting the CONSOLIDATE pipeline the same way R11 targeted EXECUTIVE SUMMARY.

### Axes explored

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Per-phase T-NN exit gate | Catch free-form terminus drift at each phase exit, before it propagates to CONSOLIDATE or EXECUTIVE SUMMARY — currently only Q1 catches it post-hoc |
| V-02 | Registry-lock declaration | Explicit close statement at end of Phase 0 prevents silent terminus additions during phases 1–5; Phase 0 becomes immutably authoritative |
| V-03 | Q8 CONSOLIDATE completeness gate | Post-write audit of all 7-field finding blocks after CONSOLIDATE is written, before VERDICT — EXECUTIVE SUMMARY has Q7; CONSOLIDATE has no equivalent |
| V-04 | V-02 + V-01 (upstream enforcement) | Registry-lock + per-phase exit gates compose to prevent drift before it reaches any output section |
| V-05 | V-04 + V-03 (full pipeline) | Three-layer enforcement for CONSOLIDATE: registry-lock (pre-execution gate) + per-phase exit gates (production-time gate per phase) + Q8 (post-write gate) — mirrors the three-layer architecture V-05 R11 introduced for EXECUTIVE SUMMARY |

### Candidate v11 criteria

If V-05 R12 scores well under evaluation:
- **C-35** — Registry-lock declaration in Phase 0 (analogous to C-32 write-time gate for EXECUTIVE SUMMARY)
- **C-36** — Per-phase T-NN exit gate in each phase's EXIT CRITERIA (no EXECUTIVE SUMMARY parallel — new pattern)
- **C-37** — Q8 CONSOLIDATE completeness gate (analogous to C-33 Q7 post-write audit for EXECUTIVE SUMMARY)

The V-05 R12 architecture would make the full finding pipeline — from Phase 0 registry through CONSOLIDATE blocks through EXECUTIVE SUMMARY — structurally enforced at every production point.
