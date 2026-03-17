Written to `simulations/quest/variations/trace-deployment-variations-R3-2026-03-14.md`.

---

## Round 3 Variations — trace-deployment

Rubric v3 adds C-14 (front-loaded skeleton) and C-15 (prose-only saturation). R2 confirmed they are **structurally mutually exclusive** — C-14 requires a pre-printed skeleton before Phase 1; C-15 requires achieving C-12/C-13 through prose *alone*, without template apparatus. The ceiling for any single variation is **120/125**.

| V | Axis | Key mechanism | Predicted |
|---|------|---------------|-----------|
| **V-01** | Apparatus minimization + C-14 | Gates and automation hooks stripped; ROLE-embedded baseline; front-loaded skeleton | **115/125** — C-10 FAIL (no hook field), C-14 PASS |
| **V-02** | Inertia framing + C-14 | ROLE-embedded baseline (no STATUS-QUO section, no GATE 0) + front-loaded skeleton; full gates and hooks intact | **120/125** — lightest full-apparatus C-14 path |
| **V-03** | Phrasing register + C-15 | Aggressively compressed prose saturation — same specificity as R2 V-04, ~half the words | **120/125** — C-15 PASS if compression preserves specificity; C-14 FAIL |
| **V-04** | Role sequence + C-14 | Adversarial two-pass (R2 V-05 lineage) + front-loaded skeleton before PASS 1; GAP PLAN spans both expert and adversarial findings | **120/125** — C-14 PASS; stronger cross-pass comparison mandate |
| **V-05** | Hybrid C-14 + C-15 | Full apparatus + front-loaded skeleton (C-14) AND saturated prose instructions co-present — negative exclusivity test | **120/125** — C-14 PASS, C-15 FAIL; confirms ceiling |

**Three questions R3 answers:**

1. **Are gate markers load-bearing for essential criteria?** V-01 strips them. Template fields (Check-01/02/03, Step-01–04) may provide the floor without gate enforcement text.

2. **What is the minimum-word path to C-15?** V-03 compresses R2 V-04 prose significantly. If C-15 still passes, the finding is: specificity is the floor, not verbosity.

3. **Does C-14/C-15 exclusivity hold?** V-05 puts saturated prose *on top of* full apparatus. If C-15 still fails (expected), the 120/125 ceiling is structurally confirmed.
C-15 exclusivity hold under adversarial and hybrid designs?** V-04 tests
   C-14 in a multi-pass context. V-05 adds saturated prose on top of full apparatus to
   confirm that apparatus presence alone blocks C-15.

---

## V-01: Apparatus-Stripped C-14

**Axis:** Apparatus minimization + C-14 front-loaded skeleton.
**Hypothesis:** Gate markers ("GATE 1: Do not proceed until...") are belt-and-suspenders.
The template fields themselves (Check-01/02/03, Step-01/02/03/04) provide the minimum count
floor. Automation hook fields drive C-10. Stripping both tests: (1) do essential criteria
survive without gates? (2) does C-14 require the surrounding apparatus to be complete, or
does the skeleton mechanism work independently? ROLE-embedded baseline satisfies C-12 (as
confirmed in R2 V-02). Front-loaded skeleton with do-not-pre-fill guard and comparative
return instruction satisfies C-14. No automation hook fields → C-10 FAIL (5 pts lost).
Predicted score: 115/125 (C-10 FAIL, C-15 FAIL).

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. Trace deployments to find
gaps before they reach production. You have seen failures at every phase.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest.

Current practice:   [How {topic} is currently deployed -- or "net-new" if no prior
                     process exists]
Known failure mode: [The specific risk the current practice carries into this deployment.
                     One sentence, concrete.]

Reference the current practice and failure mode in gap fields where they connect.

---

## GAP PLAN

Leave blank. Do not pre-fill before tracing. Return here after Phase 4 and rank all
four gaps by deployment risk.

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

The "Why this rank" column must compare this gap against the others -- not justify
the phase's severity in isolation.

Proceed to Phase 1.

---

## PHASE 1: PRE-DEPLOY CHECKS

Check-01: [What is verified -- pass condition -- failure condition]
Check-02: [What is verified -- pass condition -- failure condition]
Check-03: [What is verified -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing:  [What is absent or weak -- reference baseline failure mode if relevant]
  Fix:      [Specific change -- not just a label]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 2: DEPLOYMENT SEQUENCE

Step-01: [Action -- output -- precondition]
Step-02: [Action -- output -- precondition]
Step-03: [Action -- output -- precondition]
Step-04: [Action -- output -- precondition]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [Step numbers -- explicit reason, not sequential position]

Gap (deployment sequence):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Gap (post-deploy):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 4: ROLLBACK PATH

Trigger:      [Specific observable condition -- threshold, probe result, or signal --
               not "if deployment fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
Verification: [Observable outcome that confirms rollback succeeded]

Gap (rollback):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

Return to the GAP PLAN above and fill it in. Rank the four gaps against each other by
deployment risk. The "Why this rank" column must compare this gap to the others -- not
simply justify the phase's own severity.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, status_quo_baseline.
```

---

## V-02: ROLE-Embedded Baseline + Front-Loaded Skeleton

**Axis:** Inertia framing + C-14 front-loaded skeleton. Lightest full-apparatus path to
120/125.
**Hypothesis:** R2 V-02 confirmed that ROLE-embedded named fields ("Current practice /
Known failure mode") satisfy C-12 without a separate STATUS-QUO BASELINE section. R2 V-03
confirmed that a front-loaded GAP PLAN skeleton with do-not-pre-fill guard and comparative
return instruction satisfies C-14. V-02 merges both: embed baseline in ROLE (remove STATUS-QUO
BASELINE section, remove GATE 0), keep full gates and automation hooks, add front-loaded
skeleton. Result: one fewer section, one fewer gate vs. R2 V-03. All 15 criteria should
pass except C-15 (apparatus present). Establishes the minimum-overhead structural path to
C-14. Predicted score: 120/125 (C-14 PASS, C-15 FAIL).

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

You are tracing the deployment of {topic}. Complete this baseline now:

  Current practice:   [How {topic} is currently deployed or provisioned -- or "net-new"
                       if no prior process exists]
  Known failure mode: [The specific risk the current practice carries -- the failure this
                       deployment must not inherit. One sentence, concrete.]

This baseline anchors your gap analysis. Reference it in gap fields where applicable.

---

## GAP PLAN

Leave all rows blank. Do not pre-fill before tracing. Return here after Phase 4 is
complete and rank all four gaps by deployment risk.

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

The "Why this rank" column must compare this gap against the others across all four
phases -- not justify the phase's severity in isolation.

Proceed to PHASE 1.

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

Return to the GAP PLAN table above and fill it in. Rank the four gaps by deployment
risk. The "Why this rank" column must compare this gap against the others -- not simply
justify the phase's own severity in isolation.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## V-03: Compressed Prose Saturation

**Axis:** Phrasing register + C-15 floor test. Compressed V-04 (R2) prose -- same
specificity, significantly fewer words.
**Hypothesis:** R2 V-04 achieved C-15 at approximately 450 words of prose. C-15's pass
condition is about specificity, not verbosity: name required output elements, state the
comparison requirement, disqualify weak compliance by example. V-03 compresses all phase
instructions to single-paragraph flat prose blocks while preserving those three properties.
If C-15 passes at this compression level, the finding is: specificity is the floor, not
word count. If C-15 fails, the R2 V-04 verbosity was structurally necessary -- some
minimum surface area of prose instruction is required to satisfy C-15.
No structural apparatus (no named sections, no template fields, no gate markers) → C-14 FAIL.
Predicted score: 120/125 (C-15 PASS, C-14 FAIL).

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

You are a Commerce/Operations deployment domain expert.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest. Use these terms.
Do not use generic cloud-deploy language.

Before tracing: state the current deployment practice for {topic} and the specific
failure mode it carries into this deployment. This is your baseline -- reference it
in gap analysis where the connection is direct.

---

Pre-deploy checks. List at least 3 checks. For each: what is verified and what failure
looks like. "Verify the environment" does not pass -- name the specific artifact or
state being checked. Then: what is missing from this checklist? Name the specific gap,
state what you would add or change, and rate severity as critical, moderate, or low with
a one-sentence justification.

Deployment sequence. Number at least 4 steps. For each: the action and its output. Name
at least one step pair where the second cannot begin until the first is fully complete --
state why the order is required, not just that it exists. Name one place where a CI gate
or pre-deploy script could enforce a check that is currently manual -- state what the hook
verifies. Then: what is fragile or missing in this sequence? Name the specific gap, state
the fix, and rate severity with justification.

Post-deploy validation. List at least 2 validation actions. For each: what is checked,
the expected result, and what failure looks like. Name one place where a canary assertion
or health probe could replace a currently manual check. Then: what is missing? Name the
gap, state the fix, and rate severity with justification.

Rollback. Name the specific observable condition that triggers rollback -- a threshold,
probe result, or signal, not "if deployment fails." List rollback steps. State the
observable outcome that confirms rollback succeeded -- a metric, state, or probe result.
Then: what is weak or missing in this rollback path? Name the gap, state the fix, and
rate severity with justification.

Gap summary. Produce a table with columns: Rank, Phase, Gap summary, Severity, Why this
rank. Rank all four gaps against each other by deployment blast radius. A "Why this rank"
cell that only restates the phase's own severity without comparing it to the other three
gaps does not satisfy this requirement.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count.
```

---

## V-04: Adversarial Two-Pass + Front-Loaded Skeleton

**Axis:** Role sequence + C-14 front-loaded skeleton.
**Hypothesis:** R2 V-05 (adversarial two-pass) scored 115/125 under v3 because the GAP
PRIORITY SUMMARY was post-trace only (no C-14). V-04 places the empty gap table BEFORE
PASS 1 PHASE 1, to be filled after PASS 2 completes. The comparative return instruction
spans both passes: "compare this gap against the others across both passes." This is a
stronger cross-gap comparison mandate than single-pass V-02 -- the model must compare
expert gaps and adversarial findings simultaneously when filling the table. The front-loaded
skeleton also primes the adversarial second pass: by the time PASS 2 begins, the model
knows the table needs one entry per phase, which may drive PASS 2 toward finding exactly
the gaps that would change the table's ranking. C-14 PASS (skeleton before Phase 1,
do-not-pre-fill guard, comparative return instruction). C-15 FAIL (apparatus present).
Predicted score: 120/125.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

This skill runs in two passes. Complete PASS 1 fully before beginning PASS 2.

---

## ROLE (Pass 1 -- Domain Expert)

You are a Commerce/Operations deployment domain expert. You have seen deployments fail
at every phase -- pre-deploy environment drift, silent sequence violations, post-deploy
health gaps, and rollback triggers that never fire. You trace deployments to surface
the gaps before they surface in production.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest.

---

## STATUS-QUO BASELINE

  Current approach: [How {topic} is currently deployed or provisioned -- or "no prior
                     process" if net-new]
  Known risk:       [Specific failure mode the current approach is exposed to that this
                     deployment must not inherit]

GATE 0: Current approach named. Known risk stated as a specific failure mode, not a
        general concern. Do not proceed to GAP PLAN until this gate is met.

---

## GAP PLAN

Leave all rows blank. Do not pre-fill before tracing. Return here after PASS 2 is
complete and rank all identified gaps -- expert and adversarial -- by deployment risk.

| Rank | Phase | Source | Gap summary | Severity | Why this rank |
|------|-------|--------|-------------|----------|---------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
(Add rows for distinct adversarial findings that are not duplicates of expert gaps.)

The "Why this rank" column must compare this gap against the others across both passes --
not justify the phase's severity in isolation.

Proceed to PASS 1 PHASE 1.

---

## PASS 1: DOMAIN EXPERT TRACE

### PHASE 1: PRE-DEPLOY CHECKS

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing element: [What is absent or weak -- anchored to STATUS-QUO baseline risk if relevant]
  Recommended fix: [Specific change -- not just a label]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 1: At least 3 checks with failure conditions. Gap fully populated with fix and
        severity. Do not proceed to PHASE 2 until this gate is met.

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

GATE 2: At least 4 numbered steps. Ordering dependency with reason. Automation hook
        populated. Gap fully populated. Do not proceed to PHASE 3 until this gate is met.

---

### PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Automation hook:
  [One place where a canary assertion, health probe script, or synthetic transaction
   could replace or enforce a currently manual check.]

Gap (post-deploy):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 3: At least 2 validations with failure indicators. Automation hook populated. Gap
        fully populated. Do not proceed to PHASE 4 until this gate is met.

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
        Verification states an observable outcome. Gap fully populated.
        Do not proceed to PASS 2 until this gate is met.

---

## PASS 2: ADVERSARIAL CHALLENGE

### ROLE (Pass 2)

You are a deployment adversary reviewing the Domain Expert's trace above. Your mandate:
find what the expert missed or understated. Be adversarial, not collaborative.

For each phase: name at least one assumption the expert embedded that could fail in
production. State the failure scenario concretely. If the expert's fix was insufficient,
state a stronger fix. If a more dangerous issue exists in the same phase that the expert
did not identify, name it and explain why it outranks the expert's gap.

Findings must be at least as specific as the expert's gaps. Generic challenges ("this
could be more robust") do not pass. A finding that restates the expert's gap in different
words does not pass.

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

Return to the GAP PLAN table above and fill it in. Rank ALL gaps -- expert and
adversarial -- by deployment risk. Add rows for adversarial findings that are distinct
from the expert's gaps. The "Why this rank" column must compare this gap against the
others across both passes -- not justify the phase's severity in isolation.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline, red_team_findings_count.
```

---

## V-05: Hybrid Apparatus + Saturated Prose (C-14/C-15 Exclusivity Test)

**Axis:** Cross-axis -- tests rubric boundary. Full structural apparatus (named sections,
template fields, gate markers) + front-loaded skeleton (C-14) AND fully saturated prose
instructions (C-15 style) co-present throughout.
**Hypothesis:** C-15 requires achieving C-12 and C-13 "through explicit prose instructions
alone -- without structural template apparatus." If structural apparatus is present alongside
saturated prose, C-15 FAILS by the "alone" / "without apparatus" language. V-05 confirms this
boundary definitively. The prose instructions in this variation are independently complete --
each phase section instructs the model what to output, names required counts, disqualifies
weak compliance -- but the structural template fields and gate markers are also present. If
C-15 passes here, the rubric's "without structural template apparatus" clause needs to be
tightened. If C-15 fails (expected), V-05 confirms: the 120/125 ceiling is firm, and C-14
and C-15 are mechanically exclusive paths to the same 5-point aspirational criterion slot.
Predicted score: 120/125 (C-14 PASS from front-loaded skeleton + return instruction,
C-15 FAIL because apparatus is present).

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
threshold, canary assertion, circuit breaker, deployment manifest. Use these terms.
Do not use generic cloud-deploy framing.

Before tracing: state the current deployment practice for {topic} and the specific
failure mode it carries into this deployment. This is your baseline -- reference it in
gap fields where the connection is direct. A gap analysis that compares against an
abstract ideal rather than the stated current practice does not pass.

---

## STATUS-QUO BASELINE

  Current approach: [How {topic} is currently deployed or provisioned -- or "no prior
                     process" if net-new]
  Known risk:       [Specific failure mode the current approach is exposed to that this
                     deployment must not inherit]

GATE 0: Current approach named. Known risk stated as a specific failure mode, not a
        general concern. Do not proceed until this gate is met.

---

## GAP PLAN

Leave all rows blank. Do not pre-fill before tracing. Return here after Phase 4 and
rank all four gaps by deployment risk.

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

The "Why this rank" column must compare this gap against the others across all four
phases -- a cell that only restates the phase's own severity without comparing to the
other three gaps does not satisfy this requirement.

Proceed to PHASE 1.

---

## PHASE 1: PRE-DEPLOY CHECKS

List at least 3 checks. For each check: name the specific artifact or state being
verified, the pass condition, and what failure looks like. "Verify the environment"
does not pass -- name the specific artifact.

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

After the checks: identify what is missing from this checklist. Name the specific gap,
state what you would add or change (not just that something is missing), and rate
severity as critical, moderate, or low with a one-sentence justification. A severity
rating without justification does not pass.

Gap (pre-deploy):
  Missing element: [What is absent or weak -- reference baseline failure mode if relevant]
  Recommended fix: [Specific change -- not just a label]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 1: At least 3 checks with failure conditions. Gap fields fully populated with fix
        and severity. Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: DEPLOYMENT SEQUENCE

Number at least 4 deployment steps. For each step: the action, its output, and its
precondition. Call out at least one step pair where the second cannot begin until the
first is fully complete -- state the explicit reason, not just relative position in
the list. Name one place where a CI gate, pre-deploy script, or manifest validator
could enforce a check that is currently manual -- state what the hook verifies and why
it must be automated rather than manual.

Step-01: [Action -- output -- precondition]
Step-02: [Action -- output -- precondition]
Step-03: [Action -- output -- precondition]
Step-04: [Action -- output -- precondition]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [Step numbers and explicit reason -- not just position]

Automation hook:
  [Hook type -- what it enforces -- why manual enforcement is insufficient]

Gap (deployment sequence):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 2: At least 4 numbered steps. Ordering dependency with explicit reason. Automation
        hook populated. Gap fully populated. Do not proceed to PHASE 3.

---

## PHASE 3: POST-DEPLOY VALIDATION

List at least 2 specific validation actions. For each: what is checked, the expected
result, and what the failure indicator looks like. Name one place where a canary
assertion, health probe script, or synthetic transaction could replace a currently
manual check -- state what it checks and why automation is preferable.

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Automation hook:
  [Canary assertion / health probe / synthetic transaction -- what it checks -- why]

Gap (post-deploy):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 3: At least 2 validations with expected results and failure indicators. Automation
        hook populated. Gap fully populated. Do not proceed to PHASE 4.

---

## PHASE 4: ROLLBACK PATH

Name the specific observable condition that triggers rollback -- a threshold, probe
result, or signal. "If deployment fails" does not pass. List rollback steps. State
the observable outcome that confirms rollback succeeded -- a metric, state, or probe
result, not "rollback complete."

Trigger:      [Specific observable condition -- threshold, probe result, or signal]
Rollback-01:  [Action]
Rollback-02:  [Action]
Verification: [Observable outcome -- state, metric, or probe result]

Gap (rollback):
  Missing element: [What is absent or weak]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 4: Trigger is specific. At least 2 rollback steps. Verification states observable
        outcome. Gap fully populated.

---

Return to the GAP PLAN table and fill it in. Rank all four gaps by deployment risk. The
"Why this rank" column must compare this gap against the others -- a cell that only
justifies the phase's own severity without comparing it to the other three gaps does not
satisfy this requirement.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```
