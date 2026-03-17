---

## prove-topic Variations — Round 17 (Rubric v14)

**Round context**: R2 (v14) hit the ceiling — four of five variations scored 100/100. R17 carries the R2 V-05 structural stack (SCOUT READY exit-signal chain + two-write Stage 5 + THIN-flag format) as the mandatory baseline and explores three new single-axis patterns.

---

### V-01 — Per-Stage Inertia Displacement

**Axis**: per_stage_inertia_displacement (single)

R1 V-04 named a static inertia anchor in setup. V-01 extends it to every evidence stage: Stages 2, 3, and 4 each emit an `inertia_delta` field in their exit signal. Stage 4 aggregates these into `displacement_verdict`. Stage 5 Write B references it. The hypothesis: per-stage displacement tracking makes inertia framing a first-class evidence dimension rather than a setup note, surfacing a pattern for rubric v15.

---

### V-02 — Resume Audit

**Axis**: resume_audit (single)

A RESUME AUDIT step runs between SETUP and Stage 1. It globs all five artifact paths, marks each DONE or MISSING, and resumes from the first MISSING. The structural consequence: artifact paths in C-05 become a mechanical necessity for resumability, not just a formatting preference. If Stage 1 is RESUME-SKIP, `confidence_prior` is read from the existing artifact.

---

### V-03 — Confidence Chain with Count Gates

**Axis**: confidence_chain_count_gated (single)

Numeric confidence 1-10 flows as a chain: `confidence_prior` (Stage 1) + `s2_delta` + `s3_delta` + `s4_delta` = `confidence_final` (Stage 5). Stage 2 requires ≥3 web sources, Stage 3 requires ≥2 internal signals — count gates appear in exit signal payloads. The hypothesis: numeric chain + count thresholds makes C-09 (thin propagation) structural by chain construction and introduces a new aspirational pattern.

---

### V-04 — Combined (Inertia + Resume)

V-01 + V-02. The `inertia_anchor` is carried through the resume boundary and propagated into resumed stages. Tests whether two independent structural additions coexist cleanly.

---

### V-05 — Full Stack (All Three + R2 Champion)

V-01 + V-02 + V-03 on the complete R2 V-05 structural stack. Adds resume audit, per-stage inertia deltas, numeric confidence chain with count gates, and DISPLACEMENT AGGREGATE into Stage 4. Tests for 100/100 on v14 AND surface of two new aspirational patterns for rubric v15.

---

File written to `simulations/quest/golden/prove-topic-variate-R17-2026-03-16-v14.md`.
