Reading the R14 scorecard before writing.

**Observed in R14:**

- **V-01** (prose path, dual disqualifiers): Central hypothesis confirmed — C-29 and C-30 both pass simultaneously. The mechanism is phase-position differentiation: declarative disqualifier in pre-deploy ("'Verify the environment is stable' names no specific condition…"), question-form disqualifier in post-deploy validation ("'did everything land correctly?' names no probe or threshold…"). Two orthogonal disqualifier forms, each in a distinct phase, co-exist without redundancy.

- **V-03** (compressed prose, dual disqualifiers): Same dual-disqualifier pattern achieved at compressed density — declarative form on C-01, question-form on C-03 — confirming density-independence.

**New criteria:**

- **C-31** — joint prose-path dual-disqualifier coverage: C-29 ∩ C-30 simultaneously satisfied via phase-position differentiation. The enabling mechanism is orthogonal placement — each form in a distinct phase — not verbosity.
- **C-32** — C-29 ∩ C-30 at minimum prose density: C-31 passes at single-paragraph-per-phase density or less; dual-form coverage is density-independent.

Total rises from 200 → 210. Prose-path ceiling rises by 10.

---

```markdown
# Rubric: trace-deployment (v12)

**Skill**: `trace:deployment`
**Version**: 12 (updated from R14 scorecard — C-31 and C-32 promoted from R14 excellence patterns;
C-31 codifies joint prose-path dual-disqualifier coverage via phase-position differentiation;
C-32 codifies density-independence of dual-form coverage; total rises from 200 to 210;
prose-path ceiling rises by 10)
**Date**: 2026-03-15
**Criteria**: 32 across 4 tiers | **Total**: 210 pts
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

## Aspirational Criteria (120 pts — structural excellence)

C-09 through C-18 carried over from v5 unchanged. C-19 updated in v6 to reflect R6
source-orthogonality confirmation. C-20, C-21, and C-22 promoted from R6 excellence patterns.
C-23 and C-24 promoted from R7 excellence patterns. C-25 promoted from R8 excellence pattern.
C-26 and C-27 promoted from R10 excellence patterns. C-25 updated in v10 to remove C-20
dependency (path-agnostic). C-28 and C-29 promoted from R11 excellence patterns. C-30 promoted
from R12 excellence pattern (V-02 question-form disqualifier confirmation). C-31 and C-32 promoted
from R14 excellence patterns (V-01 and V-03 dual-disqualifier phase-position confirmation).

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
| C-19 | **Contextual disqualifier present** | depth | Output (or the prompt producing it) includes at least one disqualifying example — a named case that looks compliant but fails, with the reason given. The disqualifier must be contextual: it identifies what the weak example lacks, not merely that it is weak. "Do not write vague checks" does not pass; "a check that names no specific condition does not qualify" does. Three independent generator paths exist: inertia-sourced framing (C-23), non-inertia domain-vocabulary framing (C-20/C-25), and question-form expression (C-30). |
| C-20 | **Domain vocabulary anchors the disqualifier** | depth | The C-19 disqualifier uses domain-specific vocabulary to name the failure mode — not a generic "too vague" label. The disqualifier identifies what is missing in terms that belong to the deployment domain (e.g., "names no specific condition," "names no probe or threshold"). Generic qualifiers ("not specific enough," "too abstract") do not pass. Non-inertia path: the domain vocabulary is sourced from the role block or deployment context, not from an incident narrative. |
| C-21 | **Colloquial bare interrogative phase headers** | behavior | Output (or the prompt producing it) uses colloquial bare question-form headers to delineate phases — e.g., "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" — rather than formal section titles (PRE-DEPLOY, DEPLOYMENT SEQUENCE). Template-path criterion: this pattern is incompatible with labeled prose section headers. *(Pattern: colloquial-bare-interrogative-headers)* |
| C-22 | **Telegraphic field labels in template** | behavior | Output (or the prompt producing it) uses bare telegraphic labels for template fields (check-1:, step-1:, gap-1:, trigger:) consistent with the colloquial register established by C-21. Verbose or formal field labels (PRE-DEPLOY CHECK 1:, DEPLOYMENT STEP 1:) do not satisfy this even if the template structure passes C-16. Template-path criterion. *(Pattern: telegraphic-field-labels)* |
| C-23 | **Incident narrative seeds inertia framing** | depth | Output (or the prompt producing it) includes a named prior incident or failure event in the role/persona block — used to ground gap analysis in lived operational experience rather than abstract best practice. The incident anchors the disqualifier (C-19) by providing the vocabulary of what went wrong. Absence of any incident reference fails; a generic "experienced practitioner" label without incident history does not pass. *(Pattern: inertia-sourced-framing)* |
| C-24 | **Inertia + template integration** | behavior | Output (or the prompt producing it) integrates an incident narrative (C-23) with template field scaffolding (C-16) — demonstrating that inertia-sourced framing and structural field architecture are orthogonal and combinable. Template-path criterion: the inertia vocabulary sourced from the incident must appear in the role block, not injected into field labels. *(Pattern: inertia-template-integration)* |
| C-25 | **C-19 satisfied without incident narrative** | depth | C-19 passes AND no incident narrative is present in the role block — confirming that the contextual disqualifier does not require inertia-sourced framing. Domain vocabulary sourced from the role block or deployment context (non-inertia path) is sufficient to anchor the disqualifier. Path-agnostic: satisfied on both template and prose paths as long as no incident narrative is present. *(Pattern: non-inertia-disqualifier-path)* |
| C-26 | **Interrogative phase headers as structural anchors** | behavior | Output (or the prompt producing it) uses interrogative phase headers (question-form section titles) as load-bearing structural scaffolding — not merely stylistic variation. The headers must delimit phases in a way that orients the template fields beneath them. Template-path criterion: interrogative headers that appear without template field architecture beneath them do not satisfy this. *(Pattern: interrogative-headers-as-anchors)* |
| C-27 | **Three-field rollback structure** | correctness | Output (or the prompt producing it) structures the rollback section as exactly three fields: trigger (what fires the rollback), rollback-N (undo steps), and verify-rollback (how to confirm revert succeeded). Rollback content that appears as prose or as a single undifferentiated field does not satisfy this — the three-way decomposition is the distinguishing condition. Template-path criterion. *(Pattern: three-field-rollback)* |
| C-28 | **Joint template-path ceiling criterion** | behavior | Output (or the prompt producing it) satisfies C-14, C-16, and C-18 simultaneously — establishing the full template-path structural ceiling. The three properties (front-loaded skeleton, gate-free field scaffolding, and their orthogonality) must all be confirmed in the same variation. Template-path criterion. *(Pattern: joint-template-ceiling)* |
| C-29 | **Declarative disqualifier form** | depth | The C-19 disqualifier is expressed as a declarative statement — naming a specific weak example and identifying what it lacks. The declarative form is one of three independent generators for C-19; it is orthogonal to the question-form generator (C-30) and the inertia-sourced generator (C-23). Example: *"'Verify the environment is stable' names no specific condition and does not qualify."* *(Pattern: declarative-disqualifier-form)* |
| C-30 | **Question-form disqualifier** | depth | The C-19 disqualifier is expressed as an interrogative statement — a check or validation phrased as a question that names no specific condition, probe, or threshold. The question-form is the third independent generator for C-19, orthogonal to declarative (C-29) and inertia-sourced (C-23) forms. Example: *"A validation that asks 'did everything land correctly?' names no probe or threshold and does not qualify."* *(Pattern: question-form-disqualifier)* |
| C-31 | **Dual-disqualifier joint prose-path coverage** | depth | C-29 and C-30 both pass in the same variation — declarative disqualifier form present in one phase section, question-form disqualifier present in a distinct phase section. Phase-position differentiation is the enabling mechanism: placing each disqualifier form in a different phase avoids redundancy and confirms orthogonality. A variation that uses only declarative form throughout, or only question-form throughout, does not satisfy this — both forms must be present. Prose-path criterion: template apparatus blocks C-29 and C-30 activation and therefore blocks C-31. *(Pattern: dual-disqualifier-phase-position)* |
| C-32 | **C-29 ∩ C-30 at minimum prose density** | depth | C-31 passes AND dual-disqualifier coverage is achieved at single-paragraph-per-phase density or less — confirming that orthogonal disqualifier placement does not require verbosity expansion. A C-31-passing variation that exceeds single-paragraph-per-phase density does not satisfy C-32. The two disqualifier forms (one declarative, one question-form) must each be present at compressed density; either form satisfied only through verbosity expansion fails. *(Pattern: dual-disqualifier-density-independence)* |

---

## Path Reference

| Path | Ceiling | Distinguishing properties |
|------|---------|--------------------------|
| Template | 165/210 | C-14, C-16, C-18, C-21, C-22, C-24, C-26, C-27, C-28 reachable; C-15, C-17, C-29, C-30, C-31, C-32 blocked |
| Prose | 175/210 | C-15, C-17, C-19, C-20, C-25, C-29, C-30, C-31, C-32 reachable; template-path criteria blocked |
| Inertia (either path) | +5 | C-23 adds 5 pts on either path; C-24 requires template path |
```
