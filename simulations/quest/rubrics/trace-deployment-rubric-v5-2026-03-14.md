```markdown
# Rubric: trace-deployment (v5)

**Skill**: `trace:deployment`
**Version**: 5 (updated from R4 scorecard — 2 excellence patterns promoted to aspirational criteria)
**Date**: 2026-03-14
**Criteria**: 19 across 4 tiers | **Total**: 145 pts
**Golden**: All of C-01–C-05 pass AND composite >= 80.

---

## What This Rubric Evaluates

A `trace:deployment` output must do more than narrate a deployment sequence. It must enumerate
pre-deploy checks with failure conditions, order steps explicitly, specify post-deploy validation,
define a concrete rollback path, and identify at least one gap per phase. The hard discriminator
(C-05) forces gap analysis across all four phases — not just a happy-path trace.

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

## Aspirational Criteria (55 pts — structural excellence)

C-09 through C-17 carried over from v4. C-18 and C-19 are new — promoted from R4 excellence
patterns.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Gaps prioritized by deployment risk** | depth | Output ranks or labels identified gaps by severity or blast radius (e.g., critical / moderate / low, or "blocks rollback" vs "cosmetic"). Unranked gap lists do not satisfy this. |
| C-10 | **Automation hooks identified** | behavior | Output identifies at least one place in the deployment lifecycle where automation could enforce a check that is currently manual or absent (e.g., CI gate, pre-deploy script, post-deploy canary assertion). |
| C-11 | **Vocabulary list anchored in role block** | depth | Output (or the prompt producing it) includes a named list of domain terms in the role/persona block rather than relying on a generic domain label. A bare "Commerce/Operations expert" role does not pass; a role block that enumerates terms like "catalog sync, inventory lock, order pipeline drain, tenant provisioning" does. Per-phase vocabulary distribution is not a substitute — role-block placement is load-bearing. *(Pattern: vocabulary-list-in-role)* |
| C-12 | **Status-quo baseline established before gap analysis** | behavior | Output grounds gap analysis in current practice — not an abstract ideal. A STATUS-QUO BASELINE section (or equivalent, e.g., named fields in the ROLE block such as "Current practice / Known failure mode") states what the team currently does before identifying what is missing. Gap analysis that compares against an unstated ideal does not pass. *(Pattern: status-quo-anchor)* |
| C-13 | **Cross-phase gap summary table present** | correctness | Output includes a summary table (or equivalent structured block) that consolidates all identified gaps across phases with at least Rank, Severity, and Why columns. Per-phase gap lists without a cross-phase rollup do not satisfy this — the structural forcing of a summary table is what closes C-09 reliably. *(Pattern: cross-phase-gap-summary)* |
| C-14 | **Front-loaded gap skeleton with comparative return instruction** | behavior | Output (or the prompt producing it) places the cross-phase gap summary table as an empty skeleton *before* Phase 1, includes an explicit do-not-pre-fill guard, and includes a return instruction that mandates cross-gap comparison — "compare this gap against the others" — not merely per-phase severity justification in isolation. A post-trace gap table satisfies C-13 but not C-14; upfront commitment plus comparative forcing is the additional requirement. *(Pattern: front-loaded-gap-skeleton)* |
| C-15 | **Prose-instruction saturation closes structural criteria** | correctness | Output (or the prompt producing it) achieves C-12 and C-13 through explicit prose instructions alone — naming required output elements, stating comparison requirements, and disqualifying weak compliance by example — without structural template apparatus (named sections, template fields, or gate markers). Specificity of instruction is the floor: prose must name columns and mandate cross-gap comparison to qualify. Vague prose ("include a gap analysis") does not pass. *(Pattern: prose-instruction-saturation)* |
| C-16 | **Gate-free essential coverage via template field scaffolding** | behavior | Output (or the prompt producing it) achieves all five essential criteria (C-01–C-05) and C-10 through template field count alone — without GATE enforcement text. The field count floors must be met (≥3 Check-NN fields, ≥4 Step-NN fields, ≥2 Validation-NN fields, Trigger + Rollback-NN + Verification fields, gap block per phase). Automation hook fields must be present to satisfy C-10. Prompts that include gate markers alongside fields do not fail C-16, but also do not pass — gate-free architecture is the distinguishing condition. *(Pattern: gate-markers-not-load-bearing)* |
| C-17 | **C-15 achieved at minimum prose density** | correctness | C-15 passes AND the prose instructions satisfy all three C-15 structural requirements at single-paragraph-per-phase density or less — confirming that specificity, not verbosity, is the floor. A C-15-passing prompt that exceeds single-paragraph-per-phase density does not satisfy C-17. The three requirements (named output elements, cross-gap comparison mandate, disqualifying example) must be present at compressed density; any one requirement satisfied only through verbosity expansion fails. *(Pattern: c15-compression-confirms-specificity-floor)* |
| C-18 | **C-14 and C-16 satisfied simultaneously** | behavior | Output (or the prompt producing it) passes both C-14 and C-16 in the same variation — demonstrating that the front-loaded skeleton commitment device and gate-free field scaffolding are orthogonal structural properties. The distinguishing condition: a front-loaded empty table with a do-not-pre-fill guard is not GATE enforcement text, so its presence does not disqualify C-16. Variations that satisfy C-14 but include explicit "GATE N: Do not proceed until..." blocks fail C-16 and therefore fail C-18. *(Pattern: skeleton-and-gate-free-orthogonal)* |
| C-19 | **C-15 disqualifier satisfied by contextual failure-mode framing** | correctness | C-15 passes AND the disqualifying example is expressed as a contextual failure-mode statement — naming a specific weak response pattern in domain terms (e.g., "'someone notices it looks bad' does not pass") rather than an abstract criterion label. The distinguishing condition: disqualifier source is not load-bearing for C-15 compliance; inertia framing and abstract pattern framing satisfy C-15's disqualifying-example requirement with equivalent force. Variations whose C-15 pass relies solely on abstract disqualifiers do not fail C-19, but also do not pass — contextual framing is the distinguishing condition. *(Pattern: inertia-framing-disqualifier-passes-c15)* |

---

## Scoring Summary

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (all must pass) | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-19 (5 pts each) | 55 |
| **Total** | | **145** |

---

## Architectural Split (stable as of R4)

Two structural paths reach equal ceilings at 125/145 until C-18 and C-19 are tested:

| Path | Required | Blocked | Max Score |
|------|----------|---------|-----------|
| Template/structural | C-14, C-16, C-18 | C-15, C-17, C-19 | 130 |
| Prose saturation | C-15, C-17, C-19 | C-16, C-18 | 130 |
| Hybrid (C-14 + C-16 + C-15) | — | C-17, C-18, C-19 | 125 |

C-18 adds 5 pts exclusively to the template path (requires C-16). C-19 adds 5 pts exclusively
to the prose path (requires C-15 with contextual disqualifier). Full 145 requires a variation
that satisfies both paths — currently untested; expected to require C-15 + C-16 coexistence,
which the R4 structural split rules out. The ceiling may be structurally bounded at 130.
```
