# trace-deployment — Round 8 Variations

---

## V-01 — Prose Saturation, Domain Disqualifier, No Inertia

**Axis**: Prose-instruction saturation — no template apparatus; named output elements, cross-gap comparison mandate, domain-vocabulary disqualifier without incident narrative anywhere.

**Hypothesis**: C-15 and C-17 pass through per-phase prose that names required output elements (column names, count floors, element names), mandates comparative cross-gap ranking, and disqualifies by deployment-domain example at single-paragraph density. C-19 and C-20 pass because the disqualifier ("'keep an eye on error rates' does not name a probe or threshold") uses deployment vocabulary only — no inertia framing anywhere in the prompt. Estimated ceiling: ~135/170 (C-09–C-13, C-15, C-17, C-19, C-20).

**Criteria targeted**: C-01–C-05 (essential), C-06–C-08 (recommended), C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20

---

```markdown
**ROLE**: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
schema migration, service restart, health-check threshold, canary validation,
rollback trigger, smoke test.
Current practice: deployments run from a shared manual checklist. Known failure mode:
pre-deploy checks pass on paper but are never verified against live environment state
before the sequence begins.

**TASK**: Trace the full deployment lifecycle for **{{topic}}** across four phases.

**Phase 1 — Pre-Deploy**: List at least 3 named checks. Each check states what is
being verified and what failure looks like. "Verify the environment" does not pass —
name the specific state being confirmed.

**Phase 2 — Deployment Sequence**: Present a numbered sequence of at least 4 ordered
steps, each discrete. Call out at least one explicit ordering dependency: which step
must complete before the next can start and why.

**Phase 3 — Post-Deploy Validation**: Name at least 2 specific validation actions with
concrete probes, thresholds, or assertions. "'Keep an eye on error rates' does not name
a probe or threshold" — it does not pass.

**Phase 4 — Rollback**: Define the trigger condition, the rollback steps, and how to
verify rollback succeeded. No rollback content fails.

**Gap Analysis**: Produce a cross-phase gap table with columns: Rank, Phase, Gap,
Severity (critical/moderate/low), Why. Include at least one gap per phase. For each
gap, state what should be added or changed — not just that something is missing. Rank
gaps comparatively across all four phases before assigning severity. Also identify at
least one automation hook: a point where a CI gate, pre-deploy script, or canary
assertion could enforce a currently manual check.
```

---

## V-02 — Prose Saturation, Inertia Role Block (C-23 Orthogonality)

**Axis**: Inertia framing in role persona — first-person incident narrative in the role block; disqualifier remains domain-vocabulary-only in the gap analysis instruction.

**Hypothesis**: C-23 passes because the role block's inertia content ("after the catalog sync outage we learned…") occupies a separate structural position from the disqualifier. C-20 is evaluated only on the disqualifier, which stays in deployment-domain vocabulary with no incident reference. Inertia in the persona does not contaminate C-20 — the two are fully independent structural positions. Estimated ceiling: ~140/170 (V-01 criteria + C-23).

**Criteria targeted**: V-01 criteria + C-23

---

```markdown
**ROLE**: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
schema migration, service restart, health-check threshold, canary validation,
rollback trigger, smoke test.
Current practice: we run deployments against a runbook that has grown organically
over several quarters. After a catalog sync outage we learned that our post-deploy
health checks existed in the documentation but were not wired to any monitoring
threshold — they were aspirational entries that nobody enforced. After a tenant
provisioning rollback we found we had never written down the rollback verification
step; we improvised it under pressure during the incident.
Known failure mode: rollback triggers are added retroactively after the first incident
involving that deployment path.

**TASK**: Trace the full deployment lifecycle for **{{topic}}** across four phases.

**Phase 1 — Pre-Deploy**: List at least 3 named checks. Each check states what is
being verified and what failure looks like. "Verify the environment" does not pass —
name the specific state being confirmed.

**Phase 2 — Deployment Sequence**: Present a numbered sequence of at least 4 ordered
steps, each discrete. Call out at least one explicit ordering dependency: which step
must complete before the next can start and why.

**Phase 3 — Post-Deploy Validation**: Name at least 2 specific validation actions with
concrete probes, thresholds, or assertions. "'Keep an eye on error rates' does not name
a probe or threshold" — it does not pass.

**Phase 4 — Rollback**: Define the trigger condition, the rollback steps, and how to
verify rollback succeeded. No rollback content fails.

**Gap Analysis**: Produce a cross-phase gap table with columns: Rank, Phase, Gap,
Severity (critical/moderate/low), Why. Include at least one gap per phase. For each
gap, state what should be added or changed. Rank gaps comparatively across all four
phases before assigning severity. Identify at least one automation hook: a point
where a CI gate, pre-deploy script, or canary assertion could enforce a currently
manual check.
```

---

## V-03 — Template Path, Colloquial Register, Illustrated Fields (C-21)

**Axis**: Colloquial field labels and section headers — register-agnosticism of template-path criteria confirmed; inline field prose closes C-08 reliably but prevents C-22.

**Hypothesis**: C-14, C-16, C-18, and C-21 all pass. Labels like "check-1:", "before you touch anything:", "after deploy:", "if it breaks:" satisfy structural requirements identically to formal labels. Vocabulary list in role block + baseline fields + hook fields + front-loaded skeleton + comparative return instruction are sufficient regardless of label style. Inline field illustrations sacrifice C-22 in exchange for reliable C-08 closure. Estimated ceiling: ~135/170.

**Criteria targeted**: C-01–C-05, C-06–C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21

---

```markdown
**You are**: A veteran Commerce/Operations deployment lead.
Your terms: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
schema migration, canary check, health-check threshold, rollback trigger, smoke test,
service restart.
How deployments work today: manual checklist run against a doc that has drifted from
reality. Known weak spot: post-deploy validation entries are vague — they say "check
the service" rather than naming a threshold or probe.

**Topic**: {{topic}}

---

<!-- Empty — don't fill this yet. Come back after all four phases and rank comparatively. -->
| rank | phase | gap | severity | why |
|------|-------|-----|----------|-----|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

**Before you touch anything:**

check-1: [name what you're confirming and what failure looks like]
check-2: [name what you're confirming and what failure looks like]
check-3: [name what you're confirming and what failure looks like]
gap-pre: [what's missing in pre-deploy checks, and what to add]

**Deploy steps:**

step-1: [specific action]
step-2: [specific action]
step-3: [specific action]
step-4: [specific action]
must-happen-first: [which step before which, and why]
gap-sequence: [what's missing in the sequence, and what to add]

**After deploy, verify:**

validate-1: [specific probe, threshold, or assertion — not "look for errors"]
validate-2: [specific probe, threshold, or assertion]
automate-this: [one place a CI gate or script could enforce this automatically]
gap-validation: [what validation is missing, and what to add]

**If something breaks:**

trigger: [condition that fires the rollback]
undo-1: [step]
undo-2: [step]
confirm: [how you know rollback succeeded]
gap-rollback: [what's missing from the rollback path, and what to add]

---

Return to the table above. Before assigning rank and severity, compare all four gaps
against each other — not phase by phase in isolation. "'Keep an eye on error rates'
does not name a probe or threshold" — validation entries without a specific threshold
do not pass.
```

---

## V-04 — Template Path, Formal Register, Bare Field Labels (C-22)

**Axis**: Bare field labels — no inline prose within fields; field count plus skeleton architecture is sufficient for template-path ceiling without instruction richness per field.

**Hypothesis**: C-14, C-16, C-18, and C-22 all pass. The skeleton (front-loaded table, do-not-fill guard, return instruction) and field count alone close C-01–C-05 and C-10. C-08 is recovered via the return instruction ("state what to add — not just that it's missing"), which is part of the apparatus but not inside any field. Formal labels prevent C-21. Estimated ceiling: ~135/170.

**Criteria targeted**: C-01–C-05, C-06–C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-22

---

```markdown
**ROLE**: Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
schema migration, service restart, health-check threshold, canary validation,
rollback trigger, smoke test.
Current practice: checklist-driven manual deployments. Known failure mode: health-check
entries in the runbook are aspirational — no enforced thresholds back them.

**TOPIC**: {{topic}}

---

<!-- Do not fill. Return after all four phases. Compare all gaps before ranking. -->
| Rank | Phase | Gap | Severity | Why |
|------|-------|-----|----------|-----|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

## Phase 1 — Pre-Deploy

Check-01:
Check-02:
Check-03:
Gap-01:

## Phase 2 — Deployment Sequence

Step-01:
Step-02:
Step-03:
Step-04:
OrderDep-01:
Gap-02:

## Phase 3 — Post-Deploy Validation

Validation-01:
Validation-02:
AutomationHook-01:
Gap-03:

## Phase 4 — Rollback

Trigger-01:
Rollback-01:
Rollback-02:
Verification-01:
Gap-04:

---

Return to the table above. Each Check field must name what is being verified and what
failure looks like. For each Gap field, state what to add — not just that it's missing.
Compare all four gaps before ranking.
```

---

## V-05 — Template Path, Colloquial Register, Bare Field Labels (C-24 Ceiling)

**Axis**: Joint C-21 + C-22 satisfaction — colloquial register AND bare field labels in a single variation; confirms the two axes are orthogonal.

**Hypothesis**: C-24 passes. Colloquial labels ("check-1:", "step-1:", "before you start:") satisfy C-21 while containing no inline prose — satisfying C-22 simultaneously. Register is independent of label richness: the same bare-label structure that achieves C-22 under formal labels achieves it identically under colloquial ones. Composite reaches ~145/170, matching the joint-satisfaction ceiling (C-21 + C-22 + C-24 add 15 pts to the C-09–C-18 template base).

**Criteria targeted**: C-01–C-05, C-06–C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21, C-22, C-24

---

```markdown
**You are**: A Commerce/Operations deployment lead.
Your terms: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
schema migration, canary check, health-check threshold, rollback trigger, smoke test,
service restart.
How deployments work today: manual checklist-driven runs. Known weak spot: post-deploy
checks are documented but not threshold-bound — nobody enforces the numbers.

**Topic**: {{topic}}

---

<!-- Leave blank. Fill after all four phases. Compare gaps before ranking. -->
| rank | phase | gap | severity | why |
|------|-------|-----|----------|-----|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

before you start:

check-1:
check-2:
check-3:
gap-1:

deploy steps:

step-1:
step-2:
step-3:
step-4:
must-first:
gap-2:

after deploy:

validate-1:
validate-2:
hook-1:
gap-3:

if it breaks:

trigger-1:
undo-1:
undo-2:
confirm-1:
gap-4:

---

Back to the table. Each check must name what's being verified and what failure looks
like. State what to add for each gap — not just that it's missing. Compare all four
gaps before ranking.
```

---

## Variation Map

| Variation | Path | Register | Field Labels | Key New Criteria | Est. Score |
|-----------|------|----------|--------------|-----------------|------------|
| V-01 | Prose | — | — | C-15, C-17, C-19, C-20 | ~135/170 |
| V-02 | Prose | — | — | +C-23 (inertia role orthogonal) | ~140/170 |
| V-03 | Template | Colloquial | Illustrated | C-14, C-16, C-18, C-21 | ~135/170 |
| V-04 | Template | Formal | Bare | C-14, C-16, C-18, C-22 | ~135/170 |
| V-05 | Template | Colloquial | Bare | C-14, C-16, C-18, C-21, C-22, C-24 | ~145/170 |
