Written to `simulations/quest/rubrics/program-plan-rubric-v7-2026-03-16.md`.

---

## Three new criteria from R6 excellence signals

**C-25 — Gate Contrast Rationale Annotation**
Per-zone contrast (C-17) or structural gate fields (C-24) carry an explicit `Why:` explanation for each FAIL and PASS verdict — why the FAIL form violates the criterion, why the PASS form satisfies it. C-17 requires the contrast pair; C-25 requires the reasoning, converting contrast from pattern-teaching to principle-teaching. R6 source: V-02's `# FAIL gate: "..." Why: ...` / `# PASS gate: "..." Why: ...` at all five non-echo zones — first variate to include per-pair rationale.

**C-26 — Criterion-Tagged Structural Gate Values**
When structural gate fields are used (C-24), each `FAIL gate:` field carries an inline criterion-reference tag (`# WRONG C-04`) co-located at the structural field position itself — not only in a separate BAD block. C-16 requires criterion tags in error artifacts; C-24 requires structural fields; C-26 requires both to coincide at the field position. R6 source: V-03's `gate_fail:` fields carrying `# WRONG C-04` inline, achieving the most compact teaching form — wrong shape, structural forcing, and criterion reference in one atomic location.

**C-27 — Uniform Dependency Reminder Syntax**
All dependency reminders across all dependency-bearing zones and both positions (C-23) use identical syntactic form — `# requires: <artifact> from Zone: <name> (C-05)` — so the reminder is scannable as a machine-recognizable pattern rather than varied natural-language prose. C-23 requires dual-position placement; C-27 requires that placement to be syntactically uniform. R6 source: V-02's C-23 PASS explicitly cited "in same format" at all four dependent zones; V-01's C-23 FAIL was attributed to "inconsistent framing."

**Scoring change:** Aspirational 17 → 20 criteria, 85 → 100 pts. Total max: **190 pts.** Golden threshold (>= 80) unchanged.
