Reading the R13 variation design before writing the rubric file. (Rubric is v11 — no new criteria promoted yet. R13 variate file follows.)

---

# Round 13 Variations — trace:deployment

**Rubric version**: v11 (200 pts, 30 criteria)
**Date**: 2026-03-15
**Session goal**: Target C-30 (question-form disqualifier as third C-19 generator), C-29 (non-question-form disqualifier sufficiency), C-17/C-30 joint satisfaction at compressed density, C-23/C-30 joint (role-block inertia orthogonal to question-form disqualifier source), and the full template-path ceiling via C-28 + C-24 simultaneous satisfaction.

---

## Variation axes selected

**Single-axis (V-01 through V-03):**
1. Phrasing register — question-form disqualifier on prose path (C-30 axis)
2. Output format — declarative domain-contextual disqualifier at compressed prose density (C-29 + C-17 joint)
3. Lifecycle emphasis + phrasing register — template-path ceiling via interrogative phase headers (C-26), rollback triple fields (C-27), colloquial bare labels (C-21/C-22/C-24), and C-14/C-16/C-18 together (C-28 joint)

**Combination (V-04 through V-05):**
4. Inertia framing + phrasing register — role-block inertia narrative (C-23) with question-form disqualifier outside role block (C-30): tests orthogonality of C-23 and C-30
5. Output format + phrasing register — question-form disqualifier (C-30) at single-paragraph compressed density (C-17): tests whether question-form expression enables C-17 compliance more naturally than inertia narrative form

---

## V-01: Question-form disqualifier — prose path, standard density

**Axis**: Phrasing register — disqualifying examples expressed as interrogative statements
**Hypothesis**: When the disqualifying example is expressed as a question that names no specific condition ("a check that asks 'is the environment ready?' names no specific condition"), C-19, C-20, and C-30 all pass. C-15 passes via prose. C-17 fails (standard density — one section per phase). C-29 fails (disqualifier is question-form, not declarative).

**Predicted score**: 140/200
**Predicted criteria**: C-01–C-13 (essential + recommended + lower aspirational), C-15, C-19, C-20, C-25, C-30

---

```
ROLE: You are a Commerce/Operations deployment domain expert.
Domain vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
health-check threshold, rollback trigger, canary assertion, migration gate.
Current practice: deployments are initiated from a shared runbook with a Slack approval thread;
no automated pre-flight verification; rollback is executed manually by restoring a snapshot.
Known failure mode: services restart before database migrations complete, causing order pipeline
drain failures.

Trace the deployment of [solution] across four phases.

PRE-DEPLOY: List at least 3 pre-deploy checks. For each check, name the specific condition being
verified and what failure looks like. A check that asks "is the environment ready?" names no
specific condition and does not qualify.

DEPLOYMENT SEQUENCE: List at least 4 discrete numbered steps in execution order. Explicitly call
out at least one ordering dependency — a step that must complete before the next can begin.

POST-DEPLOY VALIDATION: List at least 2 validation actions. Each must name a probe, threshold, or
data-integrity assertion. A validation that asks "did it deploy correctly?" names no probe or
threshold and does not qualify.

ROLLBACK: State the rollback trigger, at least one undo step, and how to verify the rollback
succeeded.

For each phase, identify at least one gap. For each gap, state what should be added or changed —
naming a gap without prescribing a remedy does not qualify. Identify at least one automation hook
in the deployment lifecycle. Produce a cross-phase gap summary table with columns: Phase, Gap,
Severity (critical / moderate / low), Why. For each gap in the table, compare it against the
other gaps before assigning Severity.
```

---

## V-02: Declarative domain-contextual disqualifier — prose path, compressed density

**Axis**: Output format — all phase instructions collapsed to a single flowing paragraph; disqualifier is declarative (C-29 axis + C-17 joint)
**Hypothesis**: A single compressed instruction paragraph that names output elements, mandates cross-gap comparison, and provides a declarative domain-contextual disqualifier ("'keep an eye on error rates' names no threshold and does not qualify") passes C-15, C-17, C-19, C-20, and C-29 simultaneously. C-30 fails (disqualifier is declarative, not question-form). C-14 and all template-path criteria fail (prose path, no skeleton).

**Predicted score**: 145/200
**Predicted criteria**: C-01–C-13, C-15, C-17, C-19, C-20, C-25, C-29

---

```
ROLE: You are a Commerce/Operations deployment domain expert.
Domain vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
health-check threshold, rollback trigger, canary assertion, migration gate.
Current practice: deployments follow a shared runbook with manual Slack approval; no automated
pre-flight verification.
Known failure mode: database migrations execute after service restart, causing order pipeline
drain failures at checkout.

Trace the deployment of [solution] through pre-deploy checks, deployment sequence, post-deploy
validation, and rollback. For pre-deploy list 3+ checks — each names the specific condition and
what failure looks like; "'verify the environment is stable' names no condition and does not
qualify." For sequence list 4+ ordered steps and call out at least one explicit ordering
dependency. For validation list 2+ probes, thresholds, or data-integrity assertions; "'keep an
eye on error rates' names no probe or threshold and does not qualify." For rollback state trigger,
undo steps, and revert verification. Per phase identify at least one gap and state its remedy.
Identify at least one automation hook. Produce a cross-phase gap summary table (columns: Phase,
Gap, Severity, Why) and compare each gap against the others before assigning Severity.
```

---

## V-03: Template-path ceiling — interrogative headers + rollback triple + colloquial bare labels

**Axis**: Lifecycle emphasis + phrasing register — interrogative phase headers (C-26), minimum rollback field count (C-27), colloquial register (C-21), bare field labels (C-22), front-loaded gate-free skeleton (C-14 + C-16 + C-18), and C-24/C-28 joint satisfaction; targeting the 165/200 template-path ceiling
**Hypothesis**: A colloquial bare-label template with interrogative phase headers and exactly three rollback fields satisfies C-21, C-22, C-24, C-26, C-27, and C-28 simultaneously in a single variation, reaching the template-path ceiling. Prose-path criteria (C-15, C-17, C-19, C-20, C-23, C-29, C-30) all fail — template apparatus is present.

**Predicted score**: 165/200
**Predicted criteria**: C-01–C-14, C-16, C-18, C-21, C-22, C-24, C-25, C-26, C-27, C-28

---

```
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
health-check threshold, rollback trigger, canary assertion, migration gate.
Current practice: [fill]
Known failure mode: [fill]

---

Gap registry — fill this last; do not pre-fill any row:
| Phase | Gap | Severity | Why |
|-------|-----|----------|-----|
|       |     |          |     |
|       |     |          |     |
|       |     |          |     |
|       |     |          |     |

---

what needs to be true before we touch this?
check-1:
check-2:
check-3:
automation-hook:
gap-1:

what's the deployment order?
step-1:
step-2:
step-3:
step-4:
ordering-dependency:
gap-2:

did it land?
validation-1:
validation-2:
gap-3:

what do we do if it didn't?
trigger:
rollback-1:
verify-rollback:
gap-4:

---

Return to the Gap registry. For each row, state what should be added or changed. Compare each
gap against the others before assigning Severity.
```

---

## V-04: Role-block inertia + question-form disqualifier — C-23 and C-30 joint

**Axis**: Inertia framing + phrasing register — role block contains incident narrative (C-23 axis); disqualifying examples outside role block are expressed as questions (C-30 axis); tests whether C-23 and C-30 are jointly satisfiable
**Hypothesis**: When the role block contains an inertia narrative ("After the catalog sync outage we learned...") AND the disqualifier in the prose instructions is expressed as a question form, C-20 passes (question-form disqualifier carries no incident narrative), C-23 passes (C-20 passes and role block has inertia), and C-30 passes (question-form disqualifier). C-25 fails (role block has incident narrative). C-29 fails (disqualifier is question-form). Role-block inertia and disqualifier source are confirmed orthogonal when disqualifier is question-form.

**Predicted score**: 140/200
**Predicted criteria**: C-01–C-13, C-15, C-19, C-20, C-23, C-30

---

```
ROLE: You are a Commerce/Operations deployment domain expert.
Domain vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
health-check threshold, rollback trigger, canary assertion, migration gate.
Current practice: deployments follow a shared runbook with manual Slack approval; no automated
pre-flight verification.
Known failure mode: services restart before database migrations complete, causing order pipeline
drain failures.
After the catalog sync outage we learned that missing pre-deploy dependency health checks were
the primary gap — downstream services were unavailable before the deployment began. We carry
that lesson into every deployment trace.

Trace the deployment of [solution] across four phases.

PRE-DEPLOY: List at least 3 checks. Each must name the specific condition being verified and what
failure looks like. A check that asks "is the dependency available?" names no specific condition
and does not qualify.

DEPLOYMENT SEQUENCE: List at least 4 numbered steps in execution order. Call out at least one
step that must complete before the next can begin.

POST-DEPLOY VALIDATION: List at least 2 validation actions. Each must name a probe, threshold, or
data-integrity assertion. A validation that asks "is the service healthy?" names no probe or
threshold and does not qualify.

ROLLBACK: State the rollback trigger, at least one undo step, and how to verify the rollback
succeeded.

For each phase, identify at least one gap and state what should be added or changed. Identify at
least one automation hook. Produce a cross-phase gap summary table with columns: Phase, Gap,
Severity, Why. Compare each gap against the others before assigning Severity.
```

---

## V-05: Compressed prose + question-form disqualifier — C-17 and C-30 joint

**Axis**: Output format + phrasing register — single compressed instruction block (C-17 axis) with question-form disqualifiers (C-30 axis); tests whether question-form expression enables C-17 compliance at minimum density
**Hypothesis**: Question-form disqualifiers ("a check that asks 'is everything ready?' names no condition") are more naturally compressed than inertia-narrative disqualifiers and achieve C-15 compliance at below-single-paragraph-per-phase density. C-17 and C-30 jointly pass in a single compressed prompt. C-29 fails (question-form source). C-25 passes (no incident narrative anywhere). C-23 fails (no inertia in role block).

**Predicted score**: 145/200
**Predicted criteria**: C-01–C-13, C-15, C-17, C-19, C-20, C-25, C-30

---

```
ROLE: Commerce/Operations deployment expert.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
health-check threshold, rollback trigger, canary assertion, migration gate.
Current practice: manual Slack-approval runbook, no automated pre-flight.
Known failure mode: service restart before migration gate completion.

Trace the deployment of [solution] through pre-deploy checks, sequence, post-deploy validation,
and rollback. For pre-deploy list 3+ checks naming a specific condition and failure; a check that
asks "is the system ready?" names no condition. For sequence list 4+ ordered steps with one
explicit ordering dependency. For validation list 2+ probes or thresholds; a validation that asks
"did it work?" names no probe. For rollback state trigger, undo steps, and revert verification.
Per phase identify one gap with its remedy; rank all gaps in a cross-phase summary table (Phase,
Gap, Severity, Why) comparing each against the others before assigning Severity. Identify one
automation hook.
```

---

## Predicted scorecard

| Rank | Variation | Essential | Recommended | Aspirational | Score | Key new patterns |
|------|-----------|-----------|-------------|--------------|-------|-----------------|
| 1 | V-03 Template ceiling | 5/5 | 3/3 | 15/22 | **165** | C-24 + C-28 joint |
| 2 | V-02 Compressed declarative | 5/5 | 3/3 | 11/22 | **145** | C-17 + C-29 joint |
| 2 | V-05 Compressed question-form | 5/5 | 3/3 | 11/22 | **145** | C-17 + C-30 joint |
| 4 | V-01 Question-form standard | 5/5 | 3/3 | 10/22 | **140** | C-30 isolated |
| 4 | V-04 Inertia + question-form | 5/5 | 3/3 | 10/22 | **140** | C-23 + C-30 joint |

**Discriminating axis between V-02 and V-05**: C-29 (declarative disqualifier) vs C-30 (question-form disqualifier) — mutually exclusive at the disqualifier source level.
**Key question for R13**: Does the question-form compress more naturally than declarative? V-05 vs V-02 at equal predicted scores will show whether compression advantage is real or nominal.
**Template ceiling confirmed at 165**: V-03 is the ceiling test. C-15 through C-30 (prose path and overlap criteria) all fail on the template path.
