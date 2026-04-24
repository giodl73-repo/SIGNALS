Looking at the R8 scorecard, the one new excellence pattern to promote is the **V-01 vs V-02 distinction on C-23**: V-01's role block uses present-tense operational language ("Current practice: X. Known failure mode: Y.") rather than inertia narrative — and the scorecard explicitly names this as a distinct, non-overlapping persona voice that satisfies C-12 without reaching C-23. That pattern is new and uncodified in v7.

C-24 remains a gap (V-05 not yet tested) — already in v7, nothing to promote.

```markdown
# Rubric: trace-deployment (v8)

**Skill**: `trace:deployment`
**Version**: 8 (updated from R8 scorecard — 1 excellence pattern promoted to C-25; ceiling updated to 150/175)
**Date**: 2026-03-14
**Criteria**: 25 across 4 tiers | **Total**: 175 pts
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

## Aspirational Criteria (85 pts — structural excellence)

C-09 through C-18 carried over from v5 unchanged. C-19 updated in v6 to reflect R6
source-orthogonality confirmation. C-20, C-21, and C-22 promoted from R6 excellence patterns.
C-23 and C-24 promoted from R7 excellence patterns. C-25 promoted from R8 excellence pattern.

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
| C-19 | **C-15 disqualifier satisfied by contextual failure-mode framing** | correctness | C-15 passes AND the disqualifying example is expressed as a contextual failure-mode statement — naming a specific weak response pattern in domain terms (e.g., "'someone notices it looks bad' does not pass", "'keep an eye on error rates' does not name a probe or threshold") rather than an abstract criterion label. The distinguishing condition: disqualifier source is not load-bearing for C-15 compliance; both inertia narrative framing and domain-contextual framing (without any incident reference) satisfy C-15's disqualifying-example requirement with equivalent force. Variations whose C-15 pass relies solely on abstract disqualifiers do not fail C-19, but also do not pass — contextual framing in domain vocabulary is the distinguishing condition. *(Patterns: inertia-framing-disqualifier-passes-c15; domain-contextual-disqualifier-without-inertia-passes-c19)* |
| C-20 | **C-19 passes without inertia narrative source** | correctness | C-19 passes AND the contextual disqualifying example is grounded in domain deployment vocabulary alone — naming a specific wrong pattern in deployment terms without reference to any incident, postmortem, or "we learned" framing (e.g., "'keep an eye on error rates' does not name a probe or threshold" rather than "after the outage we learned that monitoring thresholds had to be explicit"). The distinguishing condition: inertia narrative framing is one generator of contextual disqualifiers; domain-contextual framing without incident narrative is a second independent generator. Variations that pass C-19 only through inertia-sourced disqualifiers do not fail C-20, but also do not pass — non-inertia domain vocabulary is the distinguishing condition. *(Pattern: domain-contextual-disqualifier-without-inertia-passes-c19)* |
| C-21 | **Template path passes under colloquial register** | behavior | C-14, C-16, and C-18 all pass AND the prompt uses colloquial field labels and section headers rather than formal patterns (e.g., "check-1:", "step-1:", "Before you touch anything:" rather than "## PHASE 1 — PRE-DEPLOY", "Check-NN:"). The distinguishing condition: template-path criteria are register-agnostic; structural requirements (field count, skeleton position, do-not-pre-fill guard, vocabulary list in role block, return instruction) are satisfied regardless of label formality. Variations using formal labels do not fail C-21, but also do not pass — colloquial register is the distinguishing condition. *(Pattern: conversational-register-orthogonal-to-template-path)* |
| C-22 | **Template-path ceiling reached with bare field labels** | behavior | The template path (C-14, C-16, C-18) passes AND the prompt contains no inline prose instructions within fields, no illustrative examples, and no explicit guards beyond the skeleton structure itself. Pass condition: field labels are bare identifiers only (e.g., "Check-NN:", "Step-NN:", "Gap-NN:"); no embedded instruction prose appears inside any field; the skeleton, return instruction, vocabulary list in role block, baseline fields, and hook fields constitute the complete apparatus. The distinguishing condition: instruction richness within fields is optional for the 130/145 ceiling — field count plus skeleton architecture is sufficient. Prompts with inline field prose do not fail C-22, but also do not pass — bare-label structure is the distinguishing condition. *(Pattern: minimum-viable-template-bare-field-labels)* |
| C-23 | **Role-block inertia framing orthogonal to C-20 disqualifier source** | correctness | C-20 passes AND the role block includes an inertia narrative — first-person incident framing such as "we learned that..." or "after the outage we found..." — without that framing contaminating the C-20 disqualifier-source evaluation. The distinguishing condition: C-20 evaluates whether the disqualifier example avoids incident narrative; the role persona occupies a separate structural position and is not load-bearing for C-20 compliance. A variation whose role block is rich with inertia framing but whose disqualifier content is expressed in domain-vocabulary-only terms passes both C-20 and C-23 simultaneously. Role persona framing and disqualifier source are fully independent dimensions. *(Pattern: role-block-inertia-orthogonal-to-c20-disqualifier-source)* |
| C-24 | **C-21 and C-22 jointly satisfied in a single variation** | behavior | C-21 and C-22 both pass in the same variation — colloquial register AND bare field labels — and the composite reaches 150/175, confirming that the two criteria are orthogonal template-path axes whose joint satisfaction is additive. The distinguishing condition: satisfying C-21 alone (colloquial + non-bare) or C-22 alone (formal + bare) each add 5 pts to the C-14/C-16/C-18 base; joint satisfaction adds 10 pts. Variations that satisfy only one of the two axes do not fail C-24, but also do not pass — simultaneous satisfaction under a single variation is the requirement. *(Pattern: c21-c22-orthogonal-template-path-ceiling-150)* |
| C-25 | **Present-tense operational persona passes C-20 as distinct role-block voice** | correctness | C-20 passes AND the role block uses present-tense operational baseline framing — a "Current practice: [X]" plus "Known failure mode: [Y]" pattern or equivalent — without first-person incident narrative ("we learned...", "after the outage we found..."). The distinguishing condition: present-tense operational voice satisfies C-12's status-quo baseline requirement independently of inertia narrative; it is a third categorized role-persona voice, distinct from the generic domain label (fails C-11), the vocabulary-list-only role block (passes C-11 but neither C-23 nor C-25), and the inertia narrative (passes C-23). A variation whose role block contains only present-tense operational framing passes C-25 and fails C-23; a variation with inertia narrative but no operational baseline framing passes C-23 and fails C-25. Variations whose role block contains both voice patterns satisfy C-23 independently of C-25 evaluation — the two criteria are non-overlapping on the dimension of inertia-narrative presence. *(Pattern: present-tense-operational-persona-orthogonal-to-c23)* |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-05 | 60 |
| Recommended | C-06–C-08 | 30 |
| Aspirational | C-09–C-25 | 85 |
| **Total** | **25** | **175** |
```
