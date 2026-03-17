The file is complete at 936 lines / 67KB. Let me present the R7 variations to the user:

---

Written to `simulations/quest/rubrics/program-plan-rubric-v7-R7-variate-2026-03-14.md` (936 lines, 67KB).

## R7 Variate Summary — program-plan (Round 7)

All five variations inherit the full R6 V-05 baseline (C-11 through C-27, 185/185). The R7 axes are:

---

### V-01 — Stage Displacement Register
**Axis**: For every non-echo stage, produce a pre-YAML register row stating why it cannot fire one position earlier and what breaks if it does (2+ hop cascade crossing arc-layer boundaries). Stage 1 = N/A; stages 2–N each require displacement justification.

**Hypothesis**: Stage-level displacement-impossibility register (per stage) is absent in all R6 variations. Mirrors the actor ordering table pattern at the stage-boundary granularity. Candidate for C-28.

---

### V-02 — Stage Cohesion Audit Table
**Axis**: Before YAML assembly, produce a Stage Cohesion Audit Table: per stage — constituent skills, shared phase goal, what breaks if any one skill is moved to a different stage.

**Hypothesis**: Stage membership rationale (why these exact skills belong together) is uncovered by C-06 (checks output) and C-25 (checks gate cascades). This is the skill-grouping parallel of the Gate Cascade Audit Table. Candidate for C-29.

---

### V-03 — Skill Omission Register
**Axis**: After YAML assembly, produce an explicit register of every catalog skill NOT included, each with a topic-specific exclusion reason (generic reasons such as "not needed" fail).

**Hypothesis**: Deliberate exclusion reasoning is the complement of C-03 (validates inclusions). Makes skill selection two-sided: inclusions visible in YAML, exclusions visible in register. Candidate for C-30.

---

### V-04 — V-01 + V-02
**Combination**: Stage Displacement Register + Stage Cohesion Audit Table. Pre-YAML sequence: grouping proposal → displacement register → cohesion audit → gate cascade audit → gate assembly. The two registers are orthogonal (V-01 is stage-boundary; V-02 is skill-membership).

---

### V-05 — V-01 + V-02 + V-03 + Artifact Lineage Chain
**Fourth axis**: Gate format string prefixed with `"[Skill X in stage N produces artifact_type];"` — ties every threshold to the specific producing skill, not an abstract artifact count. Gate Cascade Audit pre-computes the lineage. Full pre-YAML sequence: grouping → displacement register → cohesion audit → artifact lineage chain → gate cascade audit → gate assembly.

**Hypothesis**: Artifact provenance in gate thresholds (which specific skill produces the required artifact) is uncovered by C-16/C-22/C-24 (which specify format and cascade but not artifact lineage). Candidate for C-31.

---

### Design Principle Behind All Four R7 Axes

| Axis | Pattern | Extends |
|------|---------|---------|
| Stage Displacement Register | Displacement-impossibility per stage | C-18 (per-actor) → per-stage |
| Stage Cohesion Audit Table | Pre-computation table for grouping | C-25 (gate cascades) → skill groupings |
| Skill Omission Register | Complement-side catalog coverage | C-11 (inclusion) → exclusion justified |
| Artifact Lineage Chain | Provenance in gate threshold | C-22/C-24 (cascade in gate) → producing skill in gate |

**R7 expected scoring under v7 rubric**: All five pass C-24/C-25/C-26/C-27 by design, so all should score 185/185. The four new axes above will generate the R8 rubric candidates if validated.
