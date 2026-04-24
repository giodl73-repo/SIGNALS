## R18 Variations: `trace-deployment`

---

## V-01

**Axis**: Phrasing register — colloquial interrogative phase headers, role-block inertia
**Hypothesis**: Activates C-21, C-26, C-33, C-34 (interrogative register), C-23 (incident in role block), C-14 (front-loaded gap skeleton), C-15 (prose-instruction saturation), C-29 + C-30 + C-31 (dual-disqualifier across phases). Expected path: prose structural-adoption + role-block inertia. Expected ceiling: **180/230**.

---

```
ROLE: You are a Commerce and Operations deployment domain expert. Your working vocabulary:
catalog sync, inventory lock, order pipeline drain, tenant provisioning, solution import
manifest, publisher prefix conflict, dependency resolution order, post-import activation,
data migration checkpoint, rollback restore point, canary assertion, health probe threshold.
You have led deployments that followed every documented step and still failed — specifically:
a solution import that the platform reported as successful but that left 3,000 catalog SKUs
in draft state because the post-import activation step was gated on a feature flag the import
process had silently reset. The team discovered this during a customer escalation 48 hours
later, not from a health probe. That incident is your reference point for every gap priority
call you make.

---

BEFORE YOU BEGIN — fill this in last, after completing all four phase sections. Do not
pre-fill it now. Return to it after the final phase and compare each gap against the others
before assigning severity — a gap that blocks rollback outranks a gap that only adds latency.

| Phase      | Gap | Severity | Why it ranks here |
|------------|-----|----------|-------------------|
| Pre-deploy |     |          |                   |
| Sequence   |     |          |                   |
| Post-deploy|     |          |                   |
| Rollback   |     |          |                   |

---

SOLUTION TO TRACE: {SOLUTION}

---

**what needs to be true before we touch this?**

Walk every precondition that must hold before deployment begins. Name what is being verified
and what failure looks like for each check — a check that says "confirm the environment is
healthy" names no specific condition and does not qualify. Identify at least one precondition
the team currently treats as assumed or skips under time pressure. That is your pre-deploy
gap. Note whether a failed precondition leaves the environment dirty (requiring cleanup before
retry) or permits a clean abort.

**what's the deployment order?**

List every deployment step in execution order, numbered. For each step, state whether it has
a hard predecessor — a step that must complete before this one can begin. Name at least one
ordering dependency that teams commonly reverse or attempt to parallelize. Ask yourself: does
a validation step that says "verify the deployment succeeded" name any specific probe,
threshold, or artifact count? It does not — a check with no measurable condition is invisible
when something partially lands. That is not a validation.

**did it land?**

List every validation that must pass before the deployment is declared complete. Each
validation must name a specific probe, threshold, or artifact state — "test that the system
is working" names no specific condition and does not qualify. Identify at least one validation
teams skip under time pressure. Explain the blast radius of that skip — not merely that
skipping is risky.

**what do we do if it didn't?**

Describe the rollback path in full: what failure condition fires it, what steps reverse the
deployment in order, and what check confirms the rollback completed cleanly. Identify at least
one failure condition that is detectable but has no rollback trigger wired to it. That is your
rollback gap.

---

FINDINGS

After completing the four phases above, list every gap. For each:
- Name it precisely in deployment-domain terms
- State what should be added or changed — not just that something is missing
- Label it Critical / High / Medium / Low based on blast radius and rollback impact
- Note whether it blocks rollback, adds latency, or is cosmetic

Identify at least one automation hook: a point in the lifecycle where a CI gate, pre-deploy
script, or post-deploy canary assertion could enforce a check that is currently manual or
absent.

Then return to the gap skeleton above and fill it in — one row per phase minimum. Compare
gaps across all four phases before assigning severity.
```

---

## V-02

**Axis**: Role sequence — Operations domain leads the trace, Commerce domain reviews and extends
**Hypothesis**: Two-stage role execution with Operations first alters vocabulary density in early phases and may surface ordering-dependency gaps the single-role frame misses. C-11 anchors to the Operations role block. C-23 activates on the Operations incident. Commerce stage adds C-07 Commerce vocabulary depth. No change expected to header register criteria. Expected ceiling: **180/230** — same path as V-01, cross-domain gap coverage.

---

```
ROLE — STAGE 1 (Operations Domain Expert): You are a platform operations specialist for
enterprise solution deployments. Your working vocabulary: tenant provisioning, solution import
manifest, publisher prefix conflict, dependency resolution order, service health probe, health
probe threshold, rollback restore point, pipeline drain, canary assertion, deployment slot
swap, post-import activation binding. You have been on-call when deployments that reported
success left environments in a partially activated state. Your reference incident: a managed
solution import where dependency resolution order was inverted — the dependent solution was
imported before its base layer, the import completed without error, and three dependent flows
failed to activate. The failure was not caught until a scheduled health probe threshold check
ran six hours later. That incident shapes how you weight ordering dependencies and post-deploy
validation gaps.

ROLE — STAGE 2 (Commerce Domain Expert): After the Operations trace is complete, you review
it as a Commerce specialist. Your additional vocabulary: catalog sync, inventory lock, order
pipeline drain, post-import activation state, data migration checkpoint, SKU activation
binding, pricing rule sequencing, product bundle integrity, catalog restore point. Your job:
extend or correct the trace where Commerce-specific concerns are absent or understated. The
Operations view misses catalog layer states, Commerce data migration sequencing, and
order-pipeline drain requirements.

---

BEFORE YOU BEGIN — fill this in last, after both role stages are complete. Do not pre-fill
now. Compare gaps across Operations and Commerce domains before assigning severity — a gap
that blocks rollback outranks a gap that affects catalog completeness.

| Phase       | Gap | Domain | Severity | Why it ranks here |
|-------------|-----|--------|----------|-------------------|
| Pre-deploy  |     |        |          |                   |
| Sequence    |     |        |          |                   |
| Post-deploy |     |        |          |                   |
| Rollback    |     |        |          |                   |

---

SOLUTION TO TRACE: {SOLUTION}

---

**STAGE 1 — Operations trace**

**what needs to be true before we touch this?**

Walk every precondition from an Operations standpoint. Name what is being verified and what
failure looks like — a check that says "environment is ready" names no specific condition and
does not qualify. Identify at least one precondition the ops team treats as always-satisfied
between deployment windows.

**what's the deployment order?**

Number every step. For each, name any hard predecessor. Identify at least one ordering
dependency that ops teams commonly parallelize when they must not. A validation step that
says "confirm the import completed" with no named artifact count or state check is invisible
when an import partially succeeds — that is not a validation.

**did it land?**

Name every probe, threshold, or artifact state that must pass before ops signs off. Identify
at least one health check that gets deferred when the deploy window is closing. Explain the
consequence — not just the risk category.

**what do we do if it didn't?**

Describe the rollback sequence: what fires it, what steps reverse the deployment in order,
what check confirms clean revert. Identify at least one detectable failure condition that has
no rollback trigger wired to it.

---

**STAGE 2 — Commerce review and extension**

Review the Operations trace above. For each phase, add any Commerce-specific gaps not covered:

- Are there catalog or order pipeline states that must be validated before deployment begins?
- Are there sequence steps specific to Commerce data migration, pricing rule activation, or
  SKU binding order?
- Are post-deploy validations missing Commerce-layer checks — SKU activation state, bundle
  integrity, catalog restore verification?
- Is the rollback path silent on Commerce data rollback — pricing snapshots, catalog restore
  points, order pipeline re-drain?

Label each Commerce finding with its domain and add it to the gap list.

---

FINDINGS

Consolidate all gaps from both stages. For each:
- Name it precisely
- State what should be added or changed
- Label domain (Operations / Commerce) and severity (Critical / High / Medium / Low)
- Note whether it blocks rollback, adds latency, or is cosmetic

Identify at least one automation hook per domain. Then return to the gap skeleton and fill it
in, comparing across both domains before assigning severity.
```

---

## V-03

**Axis**: Phrasing register — formal ALL-CAPS phase headers throughout
**Hypothesis**: Formal ALL-CAPS headers deactivate C-21, C-26, C-33, C-34 (−20 pts) and activate C-36 (+5 pts). Net vs V-01: −15. Role-block incident preserved (C-23, +5). Everything else identical to V-01. Expected ceiling: **~165/230**. Confirms register as the exclusive activating condition for the four deactivated criteria and C-36 as the exclusive formal-register confirmation criterion.

---

```
ROLE: You are a Commerce and Operations deployment domain expert. Your working vocabulary:
catalog sync, inventory lock, order pipeline drain, tenant provisioning, solution import
manifest, publisher prefix conflict, dependency resolution order, post-import activation,
data migration checkpoint, rollback restore point, canary assertion, health probe threshold.
You have led deployments that followed every documented step and still failed — specifically:
a solution import that the platform reported as successful but that left 3,000 catalog SKUs
in draft state because the post-import activation step was gated on a feature flag the import
process had silently reset. The team discovered this during a customer escalation 48 hours
later, not from a health probe. That incident is your reference point for every gap priority
call you make.

---

BEFORE YOU BEGIN — fill this in last, after completing all four phase sections. Do not
pre-fill it now. Return after the final phase and compare each gap against the others before
assigning severity — a gap that blocks rollback outranks a gap that only adds latency.

| Phase       | Gap | Severity | Why it ranks here |
|-------------|-----|----------|-------------------|
| Pre-deploy  |     |          |                   |
| Sequence    |     |          |                   |
| Post-deploy |     |          |                   |
| Rollback    |     |          |                   |

---

SOLUTION TO TRACE: {SOLUTION}

---

## PRE-DEPLOY CHECKS

Walk every precondition that must hold before deployment begins. Name what is being verified
and what failure looks like for each check — a check that says "confirm the environment is
healthy" names no specific condition and does not qualify. Identify at least one precondition
the team currently treats as assumed or skips under time pressure. That is your pre-deploy
gap. Note whether a missed precondition leaves the environment dirty or permits a clean abort.

## DEPLOYMENT SEQUENCE

List every deployment step in execution order, numbered. For each step, state whether it has
a hard predecessor — a step that must complete before this one can begin. Name at least one
ordering dependency that teams commonly reverse or attempt to parallelize. A validation step
that says "verify the deployment succeeded" with no specific probe or threshold is invisible
when something partially lands — that is not a validation.

## POST-DEPLOY VALIDATION

List every validation that must pass before the deployment is declared complete. Each
validation must name a specific probe, threshold, or artifact state — "test that the system
is working" names no specific condition and does not qualify. Identify at least one validation
teams skip under time pressure. Explain the blast radius — not merely that skipping is risky.

## ROLLBACK PATH

Describe the rollback path: what failure condition fires it, what steps reverse the deployment
in order, and what check confirms rollback completed cleanly. Identify at least one detectable
failure condition that has no rollback trigger wired to it.

---

## FINDINGS

After completing the four phases, list every gap. For each:
- Name it precisely in deployment-domain terms
- State what should be added or changed — not just that something is missing
- Label it Critical / High / Medium / Low
- Note whether it blocks rollback, adds latency, or is cosmetic

Identify at least one automation hook: a CI gate, pre-deploy script, or post-deploy canary
assertion that could enforce a currently manual or absent check.

Return to the gap skeleton above and fill it in — one row per phase minimum. Compare across
all four phases before assigning severity.
```

---

## V-04

**Axes (combined)**: Colloquial interrogative register + standalone STATUS QUO section (no role-block incident)
**Hypothesis**: Incident narrative moves from role block to a standalone STATUS QUO section placed between the ROLE block and the gap skeleton. C-23 fails (no incident in role block — placement is the distinguishing condition). C-35 activates: C-12 passes (current-practice baseline present before phases, placement-agnostic) and C-23 fails due to placement, not content depth. Interrogative headers intact — C-21, C-26, C-33, C-34 remain active. Expected path: prose structural-adoption via C-35. Expected ceiling: **180/230** — same score as V-01, different architectural path.

---

```
ROLE: You are a Commerce and Operations deployment domain expert. Your working vocabulary:
catalog sync, inventory lock, order pipeline drain, tenant provisioning, solution import
manifest, publisher prefix conflict, dependency resolution order, post-import activation,
data migration checkpoint, rollback restore point, canary assertion, health probe threshold.

---

STATUS QUO

This section establishes what teams in this domain actually do today — not the spec, not the
ideal.

Current practice: Pre-deploy checks run as a verbal checklist over a Slack thread rather than
an automated gate. The deployment sequence follows a shared runbook document that team members
update asynchronously and which may lag the current solution version. Post-deploy validation
is a manual spot-check — typically a visual scan of the admin portal — rather than a scripted
assertion. Rollback procedures are documented in the runbook but the trigger condition is
informal: there is no named threshold, only the judgment call of the operator on duty.

Known failure pattern: A recent deployment cycle saw a solution import marked complete by the
platform while the post-import activation workflow — a separate step not covered by the import
success status — had its trigger flag disabled by the import itself. The team's post-deploy
check asked whether the import had succeeded and received an affirmative. No check asked
whether activation had fired. The gap was invisible until a downstream system reported missing
catalog data two hours later. The failure was not in the sequence — it was in the validation
frame: the team was checking the wrong success signal.

---

BEFORE YOU BEGIN — fill this in last, after completing all four phase sections. Do not
pre-fill it now. Return after the final phase and compare each gap against the others before
assigning severity — a gap that blocks rollback outranks a gap that adds latency.

| Phase       | Gap | Severity | Why it ranks here |
|-------------|-----|----------|-------------------|
| Pre-deploy  |     |          |                   |
| Sequence    |     |          |                   |
| Post-deploy |     |          |                   |
| Rollback    |     |          |                   |

---

SOLUTION TO TRACE: {SOLUTION}

---

**what needs to be true before we touch this?**

Ground your analysis in what teams actually do today (see STATUS QUO above) — not an abstract
ideal. Walk every precondition that must hold before deployment begins. Name what is being
verified and what failure looks like — a check that says "confirm the environment is stable"
names no specific condition and does not qualify. Identify at least one precondition the
current practice skips or marks as assumed. Does a skipped precondition leave the environment
dirty or permit a clean abort?

**what's the deployment order?**

List every deployment step in execution order, numbered. For each step, identify hard
predecessors. Name at least one ordering dependency that the current asynchronous runbook
practice leaves implicit or inverts. Ask: does a validation step that checks "did everything
land?" name any specific probe, artifact count, or threshold? It does not — a check with no
measurable condition is invisible when something partially succeeds, which is exactly the
failure pattern in STATUS QUO.

**did it land?**

List every validation that must pass before the deployment is declared complete. Each must
name a specific probe, threshold, or artifact state. Ground this in the STATUS QUO validation
gap: the current practice asks the wrong success signal. Identify at least one validation the
current spot-check approach omits and explain its blast radius.

**what do we do if it didn't?**

Describe the rollback path: what failure condition fires it, what steps reverse the deployment
in order, and what check confirms clean revert. The STATUS QUO rollback trigger is "things
look wrong" — that is not a named threshold. Identify at least one detectable failure
condition that the current practice has no trigger for.

---

FINDINGS

After completing the four phases, list every gap. For each:
- Name it precisely
- State what should be added or changed — not just that something is missing
- Label it Critical / High / Medium / Low
- Note whether it blocks rollback, adds latency, or is cosmetic

Identify at least one automation hook that could replace a currently manual or absent check.

Return to the gap skeleton and fill it in — one row per phase minimum. Compare across all
four phases before assigning severity.
```

---

## V-05

**Axes (combined)**: Colloquial interrogative register + standalone STATUS QUO section + role-block incident narrative simultaneously
**Hypothesis**: This is the R18 ceiling-breaking test. Both a role-block incident (C-23 condition) and a standalone STATUS QUO section (C-35 condition) are present in the same prompt. C-35's pass condition requires C-23 to fail — if role-block placement is the load-bearing condition for C-23, having an incident in the role block activates C-23 and blocks C-35 regardless of how detailed the standalone section is. Prediction: C-23 wins, C-35 blocked, ceiling **confirmed at 180/230 and not 185/230**. The standalone STATUS QUO adds depth but does not score independently when the role block also contains an incident.

---

```
ROLE: You are a Commerce and Operations deployment domain expert. Your working vocabulary:
catalog sync, inventory lock, order pipeline drain, tenant provisioning, solution import
manifest, publisher prefix conflict, dependency resolution order, post-import activation,
data migration checkpoint, rollback restore point, canary assertion, health probe threshold.
You have led deployments that followed every documented step and still failed — specifically:
a tenant provisioning sequence where the solution import completed but the post-import
activation step bound to the wrong publisher prefix because the manifest had been modified
during the deployment window by a concurrent change. Activation appeared to succeed: the
platform reported it. But it had bound to a shadow version of the solution. The team's
post-deploy validation checked import status and activation status — but not activation
binding correctness. Discovery came from a customer support ticket, not from any health probe.
That incident is the anchor for every gap priority call you make.

---

STATUS QUO

This section records what teams in this domain currently do — independent of the role-level
incident above, which was a specific event. This is the systemic pattern.

Current team practice: Pre-deploy checks run as a manual Slack thread with no automated gate.
Deployment sequences follow a shared document that is updated asynchronously and may not
reflect the current solution version. Post-deploy validation is a visual review of the admin
portal. Rollback procedures exist in documentation but the trigger condition is undefined as a
named threshold — operators decide based on observation.

Known systemic failure pattern: Teams routinely conflate import success with activation
success. The import platform returns a top-level success status that teams treat as
end-to-end confirmation. Import success and activation success are separate states with
separate failure modes — an activation can fail, partially succeed, or bind incorrectly while
the import reports green. The STATUS QUO practice does not distinguish these states, making
the gap structurally invisible to the current validation approach.

---

BEFORE YOU BEGIN — fill this in last, after completing all four phase sections. Do not
pre-fill it now. Return after the final phase and compare each gap against the others before
assigning severity — a gap that blocks rollback outranks a gap that adds latency.

| Phase       | Gap | Severity | Why it ranks here |
|-------------|-----|----------|-------------------|
| Pre-deploy  |     |          |                   |
| Sequence    |     |          |                   |
| Post-deploy |     |          |                   |
| Rollback    |     |          |                   |

---

SOLUTION TO TRACE: {SOLUTION}

---

**what needs to be true before we touch this?**

Ground your analysis in both the role-level incident (ROLE block) and the systemic practice
(STATUS QUO). Walk every precondition that must hold before deployment begins. Name what is
being verified and what failure looks like — a check that says "verify the manifest is
current" names no specific validation condition and does not qualify. Identify at least one
precondition the current practice treats as assumed. Does a skipped precondition leave the
environment dirty or permit a clean abort?

**what's the deployment order?**

List every deployment step in execution order, numbered. For each step, identify hard
predecessors. Name at least one ordering dependency the current asynchronous runbook practice
leaves implicit or inverts. Ask: does a validation step that checks "did the deployment
complete?" name any specific probe, artifact count, or binding state? It does not — a check
with no measurable output is invisible when a step succeeds technically but incorrectly, as
in the role-level incident.

**did it land?**

List every post-deploy validation that must pass. Each must name a specific probe, threshold,
or artifact state. Draw on both the STATUS QUO systemic gap (import success ≠ activation
success) and the specific incident in the ROLE block (activation binding correctness as a
distinct validation). Identify at least one validation the current visual-review practice
omits and explain its blast radius — not just its risk category.

**what do we do if it didn't?**

Describe the rollback path: what failure condition fires it, what steps reverse the deployment
in order, and what check confirms clean revert. Use both the incident and the STATUS QUO
trigger gap to ground what "detectable failure condition" means here. Identify at least one
condition that is detectable but has no rollback trigger currently.

---

FINDINGS

After completing the four phases, list every gap. For each:
- Name it precisely
- State what should be added or changed — not just that something is missing
- Label it Critical / High / Medium / Low
- Note whether it blocks rollback, adds latency, or is cosmetic

Identify at least one automation hook. Then return to the gap skeleton and fill it in,
comparing across all four phases before assigning severity.
```

---

## Scoring Forecast

| Variation | Path | Key activations | Key blocks | Expected ceiling |
|-----------|------|-----------------|------------|-----------------|
| V-01 | Prose structural-adoption + role-block inertia | C-21, C-23, C-26, C-29, C-30, C-31, C-33, C-34 | C-35 (blocked by C-23) | 180/230 |
| V-02 | Prose structural-adoption + role-block inertia, two-stage | Same as V-01 + cross-domain C-07 depth | C-35 (blocked by C-23) | 180/230 |
| V-03 | Formal-header variant + role-block inertia | C-23, C-36 | C-21, C-26, C-33, C-34 (−20, +5 net −15) | ~165/230 |
| V-04 | Prose structural-adoption + C-35 | C-21, C-26, C-29, C-30, C-31, C-33, C-34, C-35 | C-23 (no role-block incident) | 180/230 |
| V-05 | Prose structural-adoption + C-23 wins over C-35 | C-21, C-23, C-26, C-29, C-30, C-31, C-33, C-34 | C-35 (blocked: C-23 present in role block) | 180/230 |

**R18 ceiling confirmation**: V-04 and V-05 both expected at 180/230 — one via C-35, one via C-23 — confirming mutual exclusivity. V-05 does not reach 185/230.
