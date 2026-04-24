# Rubric: trace-deployment (v3)

**Skill**: `trace:deployment`
**Version**: 3 (updated from R2 scorecard — 2 excellence patterns promoted to aspirational criteria)
**Date**: 2026-03-14
**Criteria**: 15 across 4 tiers | **Total**: 125 pts
**Golden**: All of C-01–C-05 pass AND composite >= 80.

---

## What This Rubric Evaluates

A `trace:deployment` output must do more than narrate a deployment sequence. It must enumerate pre-deploy checks with failure conditions, order steps explicitly, specify post-deploy validation, define a concrete rollback path, and identify at least one gap per phase. The hard discriminator (C-05) forces gap analysis across all four phases — not just a happy-path trace.

---

## Essential Criteria (60 pts — all must pass)

Failure on any single essential criterion sets the composite to 0 regardless of other scores.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Pre-deploy checks enumerated** | coverage | Output lists at least 3 concrete pre-deploy checks. Each check names what is being verified and what failure looks like. "Verify the environment" does not pass. |
| C-02 | **Deployment sequence is step-by-step** | correctness | Output presents an ordered, numbered sequence of deployment steps. Steps are discrete and ordered — not a summary paragraph. At least 4 steps present. |
| C-03 | **Post-deploy validation specified** | coverage | Output identifies at least 2 specific post-deploy validation actions (e.g., smoke tests, health checks, data integrity probes). "Test that it works" does not pass. |
| C-04 | **Rollback path is defined** | correctness | Output describes a concrete rollback path: what triggers rollback, what steps undo the deployment, and how to verify rollback succeeded. Absence of any rollback content fails. |
| C-05 | **At least one gap identified per phase** | behavior | Output calls out at least one missing or weak element in pre-deploy, sequence, post-deploy, and rollback — four gaps minimum, one per phase. Pure happy-path trace with no gap analysis fails. |

---

## Recommended Criteria (30 pts — better with these)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Deployment order dependencies made explicit** | depth | Output calls out at least one ordering dependency — steps that must complete before others can start (e.g., "database migration must precede service restart"). Implicit ordering in a list does not satisfy this. |
| C-07 | **Domain framing applied** | depth | Output uses Commerce or Operations deployment vocabulary appropriate to the solution context (e.g., catalog sync, order pipeline, inventory lock, tenant provisioning). Generic cloud-deploy framing without domain anchoring does not pass. |
| C-08 | **Gaps are actionable, not just named** | correctness | For each identified gap, the output states what should be added or changed — not just that something is missing. "No rollback trigger defined — add a health-check threshold that fires the revert script" passes; "missing rollback trigger" alone does not. |

---

## Aspirational Criteria (35 pts — structural excellence)

C-09 through C-13 carried over from v2. C-14 and C-15 are new — promoted from R2 excellence patterns.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Gaps prioritized by deployment risk** | depth | Output ranks or labels identified gaps by severity or blast radius (e.g., critical / moderate / low, or "blocks rollback" vs "cosmetic"). Unranked gap lists do not satisfy this. |
| C-10 | **Automation hooks identified** | behavior | Output identifies at least one place in the deployment lifecycle where automation could enforce a check that is currently manual or absent (e.g., CI gate, pre-deploy script, post-deploy canary assertion). |
| C-11 | **Vocabulary list anchored in role block** | depth | Output (or the prompt producing it) includes a named list of domain terms in the role/persona block rather than relying on a generic domain label. A bare "Commerce/Operations expert" role does not pass; a role block that enumerates terms like "catalog sync, inventory lock, order pipeline drain, tenant provisioning" does. Per-phase vocabulary distribution is not a substitute — role-block placement is load-bearing. *(Pattern: vocabulary-list-in-role)* |
| C-12 | **Status-quo baseline established before gap analysis** | behavior | Output grounds gap analysis in current practice — not an abstract ideal. A STATUS-QUO BASELINE section (or equivalent, e.g., named fields in the ROLE block such as "Current practice / Known failure mode") states what the team currently does before identifying what is missing. Gap analysis that compares against an unstated ideal does not pass. *(Pattern: status-quo-anchor)* |
| C-13 | **Cross-phase gap summary table present** | correctness | Output includes a summary table (or equivalent structured block) that consolidates all identified gaps across phases with at least Rank, Severity, and Why columns. Per-phase gap lists without a cross-phase rollup do not satisfy this — the structural forcing of a summary table is what closes C-09 reliably. *(Pattern: cross-phase-gap-summary)* |
| C-14 | **Front-loaded gap skeleton with comparative return instruction** | behavior | Output (or the prompt producing it) places the cross-phase gap summary table as an empty skeleton *before* Phase 1, includes an explicit do-not-pre-fill guard, and includes a return instruction that mandates cross-gap comparison — "compare this gap against the others" — not merely per-phase severity justification in isolation. A post-trace gap table satisfies C-13 but not C-14; upfront commitment plus comparative forcing is the additional requirement. *(Pattern: front-loaded-gap-skeleton)* |
| C-15 | **Prose-instruction saturation closes structural criteria** | correctness | Output (or the prompt producing it) achieves C-12 and C-13 through explicit prose instructions alone — naming required output elements, stating comparison requirements, and disqualifying weak compliance by example — without structural template apparatus (named sections, template fields, or gate markers). Specificity of instruction is the floor: prose must name columns and mandate cross-gap comparison to qualify. Vague prose ("include a gap analysis") does not pass. *(Pattern: prose-instruction-saturation)* |

---

## Scoring Summary

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (all must pass) | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-15 (5 pts each) | 35 |
| **Total** | | **125** |

**Golden**: All of C-01–C-05 pass AND composite >= 80.

---

## Changelog

| Version | Change |
|---------|--------|
| v1 | 10 criteria, 100 pts. Essential C-01–C-05, Recommended C-06–C-08, Aspirational C-09–C-10. |
| v2 | +3 aspirational criteria (C-11, C-12, C-13) from R1 excellence signals. Aspirational tier expands to 25 pts; total becomes 115. Golden threshold unchanged (>=80). |
| v3 | +2 aspirational criteria (C-14, C-15) from R2 excellence signals. C-14: front-loaded gap skeleton with comparative return instruction. C-15: prose-instruction saturation as alternative path to structural criteria. Aspirational tier expands to 35 pts; total becomes 125. Golden threshold unchanged (>=80). C-11 pass condition updated to explicitly state per-phase vocabulary is not a substitute (role-block-placement-confirmed finding). |
