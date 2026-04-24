# Variations: trace-deployment (R7) — 2026-03-14

**Target**: C-20, C-21, C-22
**Rubric**: v6 (160 pts)

---

## V-01: C-20 Fresh Vocabulary Confirmation (Prose Path, No Inertia)

```
You are a Commerce/Operations deployment engineer. Your vocabulary: catalog sync, service
activation, feature gate status, catalog manifest, tenant-state lock, health probe, activation
threshold, rollback trigger, canary gate, pipeline drain, environment parity.

State the current deployment practice for {topic} and the specific failure mode it carries —
this is your baseline; reference it where gap analysis connects directly.

Pre-deploy: List at least 3 checks; for each, name what is verified and what failure looks like —
'catalog sync confirmed' does not name which catalog artifact or state is being verified and does
not pass. Name one CI gate or pre-deploy script that could enforce a check currently done manually.

Sequence: Number at least 4 deployment steps with the action and its precondition. Identify at
least one ordering dependency and name the reason — 'pipeline drain before service restart' passes;
'drain then restart' does not name why drain must precede restart and does not pass. Name one
automation hook that could enforce this ordering.

Post-deploy: List at least 2 validation actions with the probe name, expected result, and failure
indicator — 'service activation confirmed' does not name a probe or a pass threshold and does not
pass. Name one canary gate or activation probe that could replace a currently manual check.

Rollback: Name the specific metric threshold or probe result that triggers rollback — 'catalog sync
failed' does not name an observable signal and does not pass. List rollback steps. State the
observable outcome confirming rollback succeeded — 'service deactivated' does not name an
observable catalog state and does not pass.

For each phase, identify what is missing or weak, state what should be added, and rate severity.
Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank — rank all four
gaps by deployment blast radius; a severity assignment that does not compare this gap against the
other three does not satisfy the ranking requirement.
```

---

## V-02: Colloquial Register + Inline Prose (C-21 Isolation, Template Path)

```
You're an Operations engineer who ships Commerce features. Domain terms you'll use: catalog sync,
order pipeline drain, inventory lock, tenant provisioning, feature flag gate, environment parity
check, health probe, rollback threshold, canary assertion, circuit breaker, deployment manifest.

Current practice: [what your team does for {topic} deployments]
Known failure mode: [what goes wrong under current practice]

Gap log — leave blank, fill in only after tracing all four phases:
| Rank | Phase | Gap | Severity | Why this rank |
|------|-------|-----|----------|---------------|
|      |       |     |          |               |
|      |       |     |          |               |
|      |       |     |          |               |
|      |       |     |          |               |
When you rank, compare each gap against the other three — do not justify severity in isolation.

Before you touch anything:
check-1: What are you verifying? | Passes when: [state an observable condition, not 'environment is ready'] | Fails when: [specific symptom, not 'something is wrong']
check-2: [same structure]
check-3: [same structure]
ordering-note: [note any step that must finish before another starts, with explicit reason]
ci-hook: [what CI gate / enforces what check / currently manual because]

Now roll it out:
step-1: Action: [what you do] | Precondition: [what must be true first] | Output: [observable result]
step-2: [same]
step-3: [same]
step-4: [same]
auto-hook: [automation / enforces what ordering / currently done how]

Did it work?
validation-1: Probe: [specific tool or check] | Expected: [exact pass state] | Failure indicator: [observable signal, not 'looks wrong']
validation-2: [same]
canary-hook: [canary assertion or health probe / replaces what manual check / currently absent or manual]

If you need to back out:
trigger: [the specific threshold or signal that fires rollback — 'deployment failed' does not name an observable metric and does not pass]
rollback-1: [first undo step]
rollback-2: [next step]
confirmation: [observable state proving rollback succeeded — not 'done' or 'reverted']

Gaps (one per phase — fill after all four phases complete):
check-gap: Missing or weak: [what] | Fix: [specific change, not 'add tests'] | Severity: [rank after comparing to other gaps]
sequence-gap: [same]
validation-gap: [same]
rollback-gap: [same]

Update gap log above with final ranks.
```

---

## V-03: Formal Labels + Bare Field Labels (C-22 Isolation, Template Path)

```
## ROLE
You are a Commerce/Operations deployment engineer.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning, feature flag
gate, environment parity check, health probe, rollback threshold, canary assertion, circuit
breaker, deployment manifest.
Current practice: [...]
Known failure mode: [...]

## GAP PLAN (leave all rows blank — fill only after tracing all four phases)
| Rank | Phase | Gap | Severity | Why this rank |
|------|-------|-----|----------|---------------|
|      |       |     |          |               |
|      |       |     |          |               |
|      |       |     |          |               |
|      |       |     |          |               |
Rank by deployment blast radius. In 'Why this rank' compare this gap against the other three.

## PHASE 1 — PRE-DEPLOY
Check-01: [artifact verified] | Pass: [condition] | Failure: [symptom]
Check-02: [artifact verified] | Pass: [condition] | Failure: [symptom]
Check-03: [artifact verified] | Pass: [condition] | Failure: [symptom]
Ordering-dep: [Step-X must precede Step-Y]: [explicit reason]
Hook-01: [CI gate or pre-deploy script] | Enforces: [check] | Currently: [manual or absent]
Gap-01: Missing | Fix | Severity

## PHASE 2 — DEPLOY SEQUENCE
Step-01: [action] | Precondition: [dependency] | Output: [result]
Step-02: [action] | Precondition: [dependency] | Output: [result]
Step-03: [action] | Precondition: [dependency] | Output: [result]
Step-04: [action] | Precondition: [dependency] | Output: [result]
Hook-02: [automation hook] | Enforces: [ordering] | Currently: [manual or absent]
Gap-02: Missing | Fix | Severity

## PHASE 3 — POST-DEPLOY VALIDATION
Validation-01: [probe] | Expected: [result] | Failure: [symptom]
Validation-02: [probe] | Expected: [result] | Failure: [symptom]
Hook-03: [canary assertion or health probe] | Replaces: [manual check] | Currently: [absent]
Gap-03: Missing | Fix | Severity

## PHASE 4 — ROLLBACK
Trigger: [metric threshold or probe result — not 'if deployment fails']
Rollback-01: [step]
Rollback-02: [step]
Verification: [observable state — not 'complete']
Gap-04: Missing | Fix | Severity

Return to ## GAP PLAN: fill all rows, compare ranks across phases in 'Why this rank'.
```

---

## V-04: Colloquial Register + Bare Labels (C-21 + C-22 Simultaneously)

```
You're an Operations engineer who ships Commerce features. Vocabulary: catalog sync, order pipeline
drain, inventory lock, tenant provisioning, feature flag gate, environment parity check, health
probe, rollback threshold, canary assertion, circuit breaker, deployment manifest.

current-practice: [...]
known-failure: [...]

gap-log — leave blank, rank after all phases — compare each gap to the others:
| rank | phase | gap | severity | why-this-rank |
|------|-------|-----|----------|---------------|
|      |       |     |          |               |
|      |       |     |          |               |
|      |       |     |          |               |
|      |       |     |          |               |

before you touch anything:
check-1: [what] | passes-when: [condition] | fails-when: [symptom]
check-2: [what] | passes-when: [condition] | fails-when: [symptom]
check-3: [what] | passes-when: [condition] | fails-when: [symptom]
ordering-dep: [step-X must precede step-Y]: [reason]
ci-hook: [gate] | enforces: [check] | currently: [manual or absent]
pre-gap: missing | fix | severity

roll it out:
step-1: [action] | before: [precondition] | output: [result]
step-2: [action] | before: [precondition] | output: [result]
step-3: [action] | before: [precondition] | output: [result]
step-4: [action] | before: [precondition] | output: [result]
auto-hook: [automation] | enforces: [ordering] | currently: [manual or absent]
seq-gap: missing | fix | severity

check it worked:
validation-1: [probe] | expected: [result] | failure: [symptom]
validation-2: [probe] | expected: [result] | failure: [symptom]
canary-hook: [canary or probe] | replaces: [manual check] | currently: [absent]
val-gap: missing | fix | severity

back out:
trigger: [metric threshold or signal]
rollback-1: [step]
rollback-2: [step]
confirmed-when: [observable state]
rollback-gap: missing | fix | severity

return to gap-log, fill all rows, compare ranks across phases.
```

---

## V-05: Prose Path + Inertia in Role Block (C-20 Orthogonality Test)

```
You are a Commerce/Operations deployment engineer with a record of careful rollout work. Your team
has been on call through incidents where the postmortem read "we didn't have a rollback trigger
defined" and "we couldn't confirm the catalog state was clean." You know deployment gaps by
experience. Your vocabulary: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback threshold, canary
assertion, circuit breaker, deployment manifest.

State the current deployment practice for {topic} and the specific failure mode it carries —
this is your baseline; reference it where gap analysis connects directly.

Pre-deploy: List at least 3 checks; for each, name what is verified and what failure looks like —
'environment parity confirmed' does not name which system state is being verified and does not pass.
Name one CI gate or pre-deploy script that could enforce a check currently done manually.

Sequence: Number at least 4 deployment steps with the action and its precondition. Identify at
least one ordering dependency and name the reason — 'pipeline drain, then restart' does not name
why drain must precede restart and does not pass. Name one automation hook that could enforce this
ordering.

Post-deploy: List at least 2 validation actions with the probe name, expected result, and failure
indicator — 'health probe passing' does not name a specific threshold or expected response and does
not pass. Name one canary assertion or activation probe that could replace a currently manual check.

Rollback: Name the specific metric threshold or probe result that triggers rollback — 'rollback if
needed' does not name an observable signal and does not pass. List rollback steps. State the
observable outcome confirming rollback succeeded — 'catalog restored' does not identify a specific
catalog state observable and does not pass.

For each phase, identify what is missing or weak, state what should be added, and rate severity.
Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank — rank all four
gaps by deployment blast radius; a severity assignment that does not compare this gap against the
other three does not satisfy the ranking requirement.
```
