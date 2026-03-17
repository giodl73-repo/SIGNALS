Written to `simulations/quest/variations/trace-deployment-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — trace-deployment

Rubric target: v2, 115 pts. All 5 R1 variations were golden; R1 V-05 would now score 115/115 under v2 since all three new criteria (C-11, C-12, C-13) already have structural homes in it. R2 probes the boundaries of those three new criteria.

| V | Axis | Key mechanism | Predicted score |
|---|------|---------------|-----------------|
| **V-01** | Vocabulary structure | Vocabulary distributed to each phase (not ROLE block) | **110/115** — C-11 FAIL; tests whether "role block" requirement is load-bearing |
| **V-02** | Inertia framing weight | Baseline embedded in ROLE as named fields (no separate STATUS-QUO block) | **110–115/115** — C-12 boundary; tests "or equivalent" clause |
| **V-03** | Summary table placement | GAP PLAN skeleton placed before phases, filled last | **115/115** — all criteria met; tests whether front-loading improves cross-phase gap quality |
| **V-04** | Inertia framing + phrasing register | Inline ROLE baseline + conversational prose + prose ranking instruction (no pre-printed table) | **105–115/115** — C-12 and C-13 both boundary; tests if prose instruction alone closes the table requirement |
| **V-05** | Role sequence + full apparatus | Two-pass: Domain Expert trace + Red Team adversarial challenge per phase | **115/115** — same rubric ceiling as R1 V-05; gap richness is the real test (not scored yet) |

**Three open questions this round answers:**

1. **Is the "role block" location in C-11 structurally necessary?** V-01 distributes vocabulary per-phase. If it scores 110 (C-11 fail), the placement requirement is real. If it scores 115, the rubric needs loosening.

2. **How tight is "or equivalent" in C-12?** V-02 puts the baseline inside ROLE with named fields. V-04 makes it a prose instruction. One or both will pass; the scoring tells us where the floor is.

3. **Does multi-role adversary produce richer gaps?** V-05 scores the same rubric ceiling as R1 V-05. The finding is qualitative — if red team challenges surface distinct, higher-severity issues not in the expert's gaps, that's a v3 criterion candidate.

  with at least Rank, Severity, and Why columns." V-04 instructs the model to produce a ranking
  table but provides no pre-printed skeleton. A model that complies will produce the table on its
  own; a model that doesn't will produce a ranked prose list that may not satisfy C-13. This is
  the meaningful boundary test for whether structural forcing (pre-printed skeleton) is required.

- **V-05 quality ceiling:** Predicted rubric score 115/115 (same as R1 V-05 under v2), but the
  adversarial second pass should produce gaps with a different generative prior. Tests whether
  multi-role design is a quality axis that the rubric does not yet capture. If red team findings
  are measurably richer than expert self-identified gaps, that is a v3 rubric signal.

---

## V-01: Phase-Level Vocabulary

**Axis:** Vocabulary structure -- vocabulary list distributed to each phase rather than anchored
in the ROLE block.
**Hypothesis:** Phase-anchored vocabulary creates stronger in-context priming at each phase
boundary than a single role-level list that may fade across four phases. However, the v2 rubric
(C-11) explicitly requires vocabulary to be "in the role/persona block." V-01 tests whether
this structural requirement is load-bearing: if phase-level vocabulary produces equal domain
framing, C-11 may need to accept distributed vocabulary as a valid alternative. If C-11 fails
here, the per-phase vocabulary cost (one extra line per phase) is not worth the tradeoff vs. a
single vocabulary list in ROLE. Predicted score: 110/115 (C-11 FAIL).

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. You have seen deployments fail
at every phase -- pre-deploy environment drift, silent sequence violations, post-deploy
health gaps, and rollback triggers that never fire. You trace deployments to surface
the gaps before they surface in production.

---

## STATUS-QUO BASELINE

Before tracing the deployment, name the current practice this deployment replaces or
builds on:

  Current approach: [How {topic} is currently deployed or provisioned -- or "no prior
                     process" if net-new]
  Known risk:       [Specific failure mode the current approach is exposed to that this
                     deployment must not inherit]

This baseline is referenced in the gap analysis for each phase below.

GATE 0: Current approach named. Known risk stated as a specific failure mode, not a
        general concern. Do not proceed to PHASE 1 until this gate is met.

---

## PHASE 1: PRE-DEPLOY CHECKS

Vocabulary: catalog sync state, inventory lock, tenant provisioning status, order
  pipeline drain, environment parity check, deployment manifest version, feature flag
  gate state.

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing element: [What is absent or weak -- anchored to STATUS-QUO baseline risk if relevant]
  Recommended fix: [Specific change -- not just a label]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 1: At least 3 checks, each with a failure condition. Gap fully populated with fix
        and severity. Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: DEPLOYMENT SEQUENCE

Vocabulary: deployment manifest apply, service restart sequence, database migration,
  feature flag promotion, canary rollout, circuit breaker arm, health probe
  initialization, traffic drain, blue-green cutover.

Step-01: [Action -- output -- precondition]
Step-02: [Action -- output -- precondition]
Step-03: [Action -- output -- precondition]
Step-04: [Action -- output -- precondition]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [Step numbers and explicit reason -- not just sequential
                                position in the list above]

Automation hook:
  [One place in this sequence where a CI gate, pre-deploy script, or manifest validation
   could enforce a check that is currently manual or absent. Name the hook type and what
   it would verify.]

Gap (deployment sequence):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 2: At least 4 numbered steps. Ordering dependency explicitly stated with reason.
        Automation hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: POST-DEPLOY VALIDATION

Vocabulary: health probe, smoke test, canary assertion, synthetic transaction, order
  pipeline health, catalog availability probe, inventory state consistency check,
  error rate gate, latency threshold, circuit breaker state.

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Automation hook:
  [One place in post-deploy validation where a canary assertion, health probe script,
   or synthetic transaction could replace or enforce a currently manual check.]

Gap (post-deploy):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 3: At least 2 validations with expected results and failure indicators. Automation
        hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: ROLLBACK PATH

Vocabulary: rollback threshold, revert script, state restoration, traffic drain,
  circuit breaker trip, rollback verification probe, deployment manifest revert,
  inventory state rollback, order pipeline restore.

Trigger:      [Specific observable condition -- threshold, signal, or probe failure --
               not "if deployment fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
Verification: [Observable outcome -- state, metric, or probe result -- that confirms
               rollback succeeded]

Gap (rollback):
  Missing element: [What is absent or weak -- e.g., trigger threshold undefined,
                    no verification probe, manual step with no owner]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 4: Trigger is a specific observable condition. At least 2 rollback steps.
        Verification states an observable outcome. Gap fully populated with fix
        and severity.

---

## GAP PRIORITY SUMMARY

After all four phases are complete, rank the four gaps by deployment risk:

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |
| 2 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |
| 3 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |
| 4 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## V-02: Inline Baseline in ROLE

**Axis:** Inertia framing weight -- baseline embedded in the ROLE block as named fields,
no separate STATUS-QUO section, no GATE 0.
**Hypothesis:** The v2 rubric (C-12) requires "a STATUS-QUO BASELINE section (or equivalent)."
V-02 tests whether ROLE-embedded baseline fields satisfy "or equivalent." The apparatus saving
is one block and one gate eliminated -- ROLE does double duty. If C-12 passes, V-02 is a
lighter-weight path to 115/115. If C-12 fails, the rubric's "or equivalent" clause needs a
tighter definition: inline fields in ROLE are not enough; a named section is required. All
other apparatus is identical to R1 V-05.
Predicted score: 115/115 (C-12 likely passes "or equivalent") or 110/115 (boundary).

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. You have seen deployments fail
at every phase -- pre-deploy environment drift, silent sequence violations, post-deploy
health gaps, and rollback triggers that never fire. You trace deployments to surface
the gaps before they surface in production.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest.

You are tracing the deployment of {topic}. Establish the deployment baseline now:

  Current practice:   [How {topic} is currently deployed or provisioned -- or "net-new"
                       if no prior process exists]
  Known failure mode: [The specific risk the current practice is exposed to -- the failure
                       this deployment must not inherit. One sentence, concrete.]

This baseline anchors your gap analysis. Reference it in gap fields where applicable.

---

## PHASE 1: PRE-DEPLOY CHECKS

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing element: [What is absent or weak -- reference baseline failure mode if relevant]
  Recommended fix: [Specific change -- not just a label]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 1: At least 3 checks, each with a failure condition. Gap fully populated with fix
        and severity. Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: DEPLOYMENT SEQUENCE

Step-01: [Action -- output -- precondition]
Step-02: [Action -- output -- precondition]
Step-03: [Action -- output -- precondition]
Step-04: [Action -- output -- precondition]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [Step numbers and explicit reason -- not just sequential
                                position in the list above]

Automation hook:
  [One place in this sequence where a CI gate, pre-deploy script, or manifest validation
   could enforce a check that is currently manual or absent. Name the hook type and what
   it would verify.]

Gap (deployment sequence):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 2: At least 4 numbered steps. Ordering dependency explicitly stated with reason.
        Automation hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Automation hook:
  [One place in post-deploy validation where a canary assertion, health probe script,
   or synthetic transaction could replace or enforce a currently manual check.]

Gap (post-deploy):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 3: At least 2 validations with expected results and failure indicators. Automation
        hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: ROLLBACK PATH

Trigger:      [Specific observable condition -- threshold, signal, or probe failure --
               not "if deployment fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
Verification: [Observable outcome -- state, metric, or probe result -- that confirms
               rollback succeeded]

Gap (rollback):
  Missing element: [What is absent or weak -- e.g., trigger threshold undefined,
                    no verification probe, manual step with no owner]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 4: Trigger is a specific observable condition. At least 2 rollback steps.
        Verification states an observable outcome. Gap fully populated with fix
        and severity.

---

## GAP PRIORITY SUMMARY

After all four phases are complete, rank the four gaps by deployment risk:

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |
| 2 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |
| 3 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |
| 4 | [phase] | [one-line summary] | [critical/moderate/low] | [one sentence] |

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## V-03: Front-Loaded Gap Table

**Axis:** Output format -- GAP PRIORITY SUMMARY placed BEFORE Phase 1 as an empty planning
skeleton, filled in after all four phases complete.
**Hypothesis:** Front-loading the summary table commits the model to gap structure before any
phase is traced. Knowing from the start that all four gaps must be comparable, ranked, and
labeled may produce more coherent cross-phase analysis than a retrospective rollup assembled
after the fact. The end-of-trace return instruction ("return to the GAP PLAN table above and
fill it in") makes the cross-phase comparison requirement explicit at both ends of the prompt.
Tests whether placement affects C-13 quality -- not just whether the table is present.
Full apparatus otherwise identical to R1 V-05.
Predicted score: 115/115. Gap quality hypothesis: front-loading produces better cross-phase
comparative reasoning than end-of-trace rollup.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. You have seen deployments fail
at every phase -- pre-deploy environment drift, silent sequence violations, post-deploy
health gaps, and rollback triggers that never fire. You trace deployments to surface
the gaps before they surface in production.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest.

---

## STATUS-QUO BASELINE

Before tracing the deployment, name the current practice this deployment replaces or
builds on:

  Current approach: [How {topic} is currently deployed or provisioned -- or "no prior
                     process" if net-new]
  Known risk:       [Specific failure mode the current approach is exposed to that this
                     deployment must not inherit]

GATE 0: Current approach named. Known risk stated as a specific failure mode, not a
        general concern. Do not proceed to GAP PLAN until this gate is met.

---

## GAP PLAN

Leave this table blank until PHASE 4 is complete. Then return here and rank all four
identified gaps by deployment risk. Rows must be filled based on the actual gaps found
in each phase -- do not pre-fill before tracing.

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

Proceed to PHASE 1.

---

## PHASE 1: PRE-DEPLOY CHECKS

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing element: [What is absent or weak -- anchored to STATUS-QUO baseline risk if relevant]
  Recommended fix: [Specific change -- not just a label]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 1: At least 3 checks, each with a failure condition. Gap fully populated with fix
        and severity. Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: DEPLOYMENT SEQUENCE

Step-01: [Action -- output -- precondition]
Step-02: [Action -- output -- precondition]
Step-03: [Action -- output -- precondition]
Step-04: [Action -- output -- precondition]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [Step numbers and explicit reason -- not just sequential
                                position in the list above]

Automation hook:
  [One place in this sequence where a CI gate, pre-deploy script, or manifest validation
   could enforce a check that is currently manual or absent. Name the hook type and what
   it would verify.]

Gap (deployment sequence):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 2: At least 4 numbered steps. Ordering dependency explicitly stated with reason.
        Automation hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Automation hook:
  [One place in post-deploy validation where a canary assertion, health probe script,
   or synthetic transaction could replace or enforce a currently manual check.]

Gap (post-deploy):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 3: At least 2 validations with expected results and failure indicators. Automation
        hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: ROLLBACK PATH

Trigger:      [Specific observable condition -- threshold, signal, or probe failure --
               not "if deployment fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
Verification: [Observable outcome -- state, metric, or probe result -- that confirms
               rollback succeeded]

Gap (rollback):
  Missing element: [What is absent or weak -- e.g., trigger threshold undefined,
                    no verification probe, manual step with no owner]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 4: Trigger is a specific observable condition. At least 2 rollback steps.
        Verification states an observable outcome. Gap fully populated with fix
        and severity.

---

Return to the GAP PLAN table above and fill it in. Rank the four gaps against each other
by deployment risk. The "Why this rank" column must compare this gap against the others --
not simply justify the phase's severity in isolation.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## V-04: Inline Baseline + Conversational Register

**Axes:** Inertia framing weight + phrasing register -- ROLE-level inline baseline (no separate
block), no template fields, no pre-printed table skeleton, imperative prose only. Prose
instruction to produce a ranking table at the end.
**Hypothesis:** R1 V-03 (pure conversational) scored 85/100 under v1, failing C-07 partial,
C-09, and C-10. Under v2 it would also fail C-11 (no vocabulary list), C-12 (no baseline),
and C-13 (no summary table structure). V-04 patches all three by adding vocabulary list to ROLE,
inline baseline in ROLE, and explicit instruction to produce a ranking table. Tests three boundary
conditions simultaneously: (1) Does vocabulary list in ROLE satisfy C-11 without template apparatus?
Yes -- this should pass. (2) Does prose baseline in ROLE satisfy C-12's "or equivalent" clause?
Boundary case. (3) Does "produce a ranking table" prose instruction satisfy C-13 without a
pre-printed skeleton? This is the key test -- a model following the instruction will produce a
table; the rubric's "or equivalent" may or may not accept the result.
Predicted score: 105-115/115. C-12 and C-13 are the boundary cases.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

You are a Commerce/Operations deployment domain expert. You trace deployments to find
failures before they reach production.

Your vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
feature flag gate, environment parity check, health probe, rollback threshold, canary
assertion, circuit breaker, deployment manifest. Use these terms. Do not use generic
cloud-deploy language.

Before you begin the trace: state the current deployment practice this replaces or builds
on, and the specific failure mode it is exposed to. This is your baseline -- reference it
when gaps connect to it.

---

**Pre-deploy checks.**
What has to be true before you touch anything? List at least 3 checks.
For each: name what you are verifying and what "failed" looks like.
Then: what is missing from this checklist? Name it, say what you would add, and say
whether the risk is critical, moderate, or low -- and why.

**Deployment sequence.**
Walk through every deployment step in order. Number them. At least 4 steps.
For each step: say what is done and what it produces.
Call out at least one pair of steps where the second cannot start until the first is
completely finished -- and say why the order matters.
Name one place in this sequence where a CI gate or pre-deploy script could enforce a
check that is currently manual. Say what the hook would verify.
Then: what is fragile or missing in this sequence? Name it, say what you would fix,
and rate the risk.

**Post-deploy validation.**
What do you check after the deployment lands? List at least 2 specific actions.
For each: what are you looking for and what does failure look like?
Name one place where a canary assertion or health probe could replace a manual check.
Then: what is missing from this validation? Say what you would add and rate the risk.

**Rollback.**
What specific condition triggers a rollback? Name it. It must be a threshold, signal,
or probe result -- not "if deployment fails."
Walk through the rollback steps.
How do you know rollback succeeded? State the observable outcome.
Then: what is weak or missing in this rollback path? Say what you would change and rate
the risk.

**Gap priority.**
Produce a table ranking the four gaps you identified -- one per phase -- by deployment
risk. The table must have at minimum: Rank, Phase, Gap summary, Severity, and a "Why
this rank" column. Rank the gaps against each other by blast radius. A "Why this rank"
cell that only justifies the phase's own severity without comparing to other gaps does
not pass.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## V-05: Multi-Role Adversary + Full Apparatus

**Axes:** Role sequence + full apparatus -- two passes run sequentially: (1) Domain Expert
produces the trace using the full R1 V-05 apparatus, (2) Red Team Adversary challenges each
phase for undetected gaps. Second pass must add findings the first pass missed.
**Hypothesis:** A model asked to self-identify gaps is structurally limited by the same priors
that shaped the trace. An adversarial second role breaks the confirmation loop: "find what the
expert missed -- be adversarial, not collaborative" generates from a different prior. Tests
whether role sequence is a quality axis the v2 rubric does not yet capture. Predicted rubric
score: 115/115 (same ceiling as R1 V-05 under v2). The real question is whether red team
findings are measurably richer than expert self-identified gaps -- and if so, whether v3 should
add a criterion for second-pass adversarial depth.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

This skill runs in two passes. Complete PASS 1 fully before beginning PASS 2.

---

## PASS 1: DOMAIN EXPERT TRACE

### ROLE (Pass 1)

You are a Commerce/Operations deployment domain expert. You have seen deployments fail
at every phase -- pre-deploy environment drift, silent sequence violations, post-deploy
health gaps, and rollback triggers that never fire. You trace deployments to surface
the gaps before they surface in production.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest.

---

### STATUS-QUO BASELINE

  Current approach: [How {topic} is currently deployed or provisioned -- or "no prior
                     process" if net-new]
  Known risk:       [Specific failure mode the current approach is exposed to that this
                     deployment must not inherit]

GATE 0: Current approach named. Known risk stated as a specific failure mode, not a
        general concern. Do not proceed to PHASE 1 until this gate is met.

---

### PHASE 1: PRE-DEPLOY CHECKS

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing element: [What is absent or weak -- anchored to STATUS-QUO baseline risk if relevant]
  Recommended fix: [Specific change -- not just a label]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 1: At least 3 checks with failure conditions. Gap fully populated with fix and severity.
        Do not proceed to PHASE 2 until this gate is met.

---

### PHASE 2: DEPLOYMENT SEQUENCE

Step-01: [Action -- output -- precondition]
Step-02: [Action -- output -- precondition]
Step-03: [Action -- output -- precondition]
Step-04: [Action -- output -- precondition]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [Step numbers and explicit reason -- not just sequential
                                position in the list above]

Automation hook:
  [One place in this sequence where a CI gate, pre-deploy script, or manifest validation
   could enforce a check that is currently manual or absent. Name the hook type and what
   it would verify.]

Gap (deployment sequence):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 2: At least 4 numbered steps. Ordering dependency explicitly stated with reason.
        Automation hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 3 until this gate is met.

---

### PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Automation hook:
  [One place in post-deploy validation where a canary assertion, health probe script,
   or synthetic transaction could replace or enforce a currently manual check.]

Gap (post-deploy):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 3: At least 2 validations with expected results and failure indicators. Automation
        hook populated. Gap fully populated with fix and severity.
        Do not proceed to PHASE 4 until this gate is met.

---

### PHASE 4: ROLLBACK PATH

Trigger:      [Specific observable condition -- threshold, signal, or probe failure --
               not "if deployment fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
Verification: [Observable outcome -- state, metric, or probe result -- that confirms
               rollback succeeded]

Gap (rollback):
  Missing element: [What is absent or weak -- e.g., trigger threshold undefined,
                    no verification probe, manual step with no owner]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 4: Trigger is a specific observable condition. At least 2 rollback steps.
        Verification states an observable outcome. Gap fully populated with fix and severity.
        Do not proceed to PASS 2 until this gate is met.

---

## PASS 2: RED TEAM CHALLENGE

### ROLE (Pass 2)

You are a deployment adversary reviewing the Domain Expert's trace above. Your mandate is
to find what the expert missed or understated. Be adversarial, not collaborative.

For each phase: name at least one assumption the expert made that could fail in production.
State the failure scenario concretely. If the expert's gap was correct but the fix was
insufficient, say so and state a stronger fix. If the expert's gap missed a more dangerous
issue in the same phase, name it and explain why it outranks what the expert identified.

Findings must be at least as specific as the expert's gaps. Generic challenges ("this
could be more robust") do not pass. A finding that merely restates the expert's gap in
different words does not pass.

Phase 1 challenge:
  Expert assumption challenged: [What assumption did the expert embed in Phase 1?]
  Failure scenario:             [How does it fail in production? Be concrete.]
  Finding severity:             [critical / moderate / low -- one sentence justification]

Phase 2 challenge:
  Expert assumption challenged: [What assumption did the expert embed in Phase 2?]
  Failure scenario:             [How does it fail in production? Be concrete.]
  Finding severity:             [critical / moderate / low -- one sentence justification]

Phase 3 challenge:
  Expert assumption challenged: [What assumption did the expert embed in Phase 3?]
  Failure scenario:             [How does it fail in production? Be concrete.]
  Finding severity:             [critical / moderate / low -- one sentence justification]

Phase 4 challenge:
  Expert assumption challenged: [What assumption did the expert embed in Phase 4?]
  Failure scenario:             [How does it fail in production? Be concrete.]
  Finding severity:             [critical / moderate / low -- one sentence justification]

---

## GAP PRIORITY SUMMARY (both passes)

Rank ALL gaps -- expert + red team -- by deployment risk. Include at minimum 4 rows
(one per phase expert gap). Add additional rows for red team findings that are distinct
from the expert's gaps.

| Rank | Phase | Source | Gap summary | Severity | Why this rank |
|------|-------|--------|-------------|----------|---------------|
| 1 | [phase] | [Expert/RedTeam] | [one-line] | [level] | [one sentence] |
| 2 | [phase] | [Expert/RedTeam] | [one-line] | [level] | [one sentence] |
| 3 | [phase] | [Expert/RedTeam] | [one-line] | [level] | [one sentence] |
| 4 | [phase] | [Expert/RedTeam] | [one-line] | [level] | [one sentence] |
(Add rows for distinct red team findings.)

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline, red_team_findings_count.
```
