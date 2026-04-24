Written to `simulations/quest/golden/prove-topic-variate-R19-v14-2026-03-16.md`.

---

# prove-topic Variations — Round 19 (rubric v14)

**Skill**: prove-topic | **Rubric**: v14 | **Date**: 2026-03-16 | **Round**: R19

---

## Axes explored

| Variation | Axis | Type |
|-----------|------|------|
| V-01 | output_format | single |
| V-02 | inertia_framing | single |
| V-03 | lifecycle_emphasis | single |
| V-04 | output_format + inertia_framing | combined |
| V-05 | all three + full R19 baseline stack | full integration |

**Baseline**: R19 V-01 (resume_audit_gate) — RESUME AUDIT block, ROLE OWNERSHIP TABLE with C→B→A dependency, SESSION INVARIANTS (D/A/B/C), count-gated exits (S2≥5, S3≥3, S4≥3), three-block Stage 5 with ATOMIC DUAL-LOCK, HANDOFF TABLE with derivation annotations.

---

## Variation hypotheses

**V-01 — Output Format**
All tables replaced with inline key: value blocks and numbered lists. Tests whether format transformation from tabular to prose preserves rubric compliance. Criterion targets: C-03 (artifact write clarity), C-04 (synthesis readiness signal).

**V-02 — Inertia Framing**
DISPLACEMENT THESIS block inserted after CAMPAIGN OPEN. Each evidence stage (S2, S3, S4) opens with a labeled STAGE DISPLACEMENT QUESTION. Stage 5 synthesis leads with `displacement_conclusion` before `hypothesis_verdict`. Criterion targets: C-02 (scout grounding), C-05 (incumbent-displacement thread maintained throughout).

**V-03 — Lifecycle Emphasis**
Stage 0 compressed to a 6-item checklist. Stages 1–4 reduced to essential output fields only. Stage 5 significantly expanded: each block gets its own entry conditions, explicit intermediate compute steps (chain integrity check, open_risk accumulation, tally cross-check), and BLOCK COMPLETE guards before any synthesis field is populated. Criterion targets: C-04 (synthesis readiness signal), C-05 (cleaner exit signal recognizable to /topic-story).

**V-04 — Output Format + Inertia Framing**
V-01 + V-02. Inline prose format with displacement thesis as narrative lead at every decision point.

**V-05 — Full Integration**
V-01 + V-02 + V-03 on top of full R19 baseline. Inline format, displacement-first framing, compressed setup, maximally expanded Stage 5 with per-block entry conditions and explicit intermediate variables. Tests whether all three structural transformations simultaneously satisfy all 10 v14 rubric criteria.

---

The key structural innovations across variations:

- **V-02/V-04/V-05** add `displacement_per_stage` (S2/S3/S4 aggregate displacement verdicts) and `incumbent_defense_closed` to BLOCK 3, giving synthesis a per-stage displacement chain rather than a single Stage 4 verdict
- **V-03/V-05** expand BLOCK 1 with `chain_integrity_check` — verifies `running_confidence` at Stage 4 close matches the reconstructed chain sum
- **V-03/V-05** expand BLOCK 3 with an explicit incumbent defense closure step citing all three stages
- **V-05** is the only variation that combines all three axes plus the full R19 structural floor (RESUME AUDIT, DEPENDENCY column, ATOMIC DUAL-LOCK, per-block entry conditions)
