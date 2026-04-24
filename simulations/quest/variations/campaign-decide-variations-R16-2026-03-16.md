`campaign-decide-variate-R16-2026-03-17.md` written.

---

## R16 Summary

**Three single-axis variations, two combinations:**

| Var | Axis | Key structural change |
|-----|------|-----------------------|
| V-01 | C-39 hardening | Phase 5 header annotation names specific schemas: `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` instead of generic `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]` |
| V-02 | C-40 fill-phase metadata | Bracket notation encodes temporal commit per column: `[columns: FID (key, fill-now), Actual Outcome (defer-to-Phase-5)]` — enables two-pass audit (Phase N gate: fill-now columns; Phase 5 gate: deferred columns) |
| V-03 | Inertia framing | Opening persona sentence foregrounds status quo primacy + one-sentence Phase 1a inline rationale before the first table row — two semantic anchors before any gate or schema is processed |
| V-04 | V-01 + V-03 | Named-schema Phase 5 annotation + inertia persona framing |
| V-05 | Full integration | V-01 + V-02 + V-03, all 40 criteria structurally encoded, targeting **106.0/106.0** |

**New potential criteria surfaced for R17:**

- **C-41 candidate**: Named schema enumeration in fill-forward directive (V-01 axis — per-schema vs. "all" resolution)
- **C-42 candidate**: Fill-phase metadata in bracket notation column lists (V-02 axis — temporal commit verifiability per column)
