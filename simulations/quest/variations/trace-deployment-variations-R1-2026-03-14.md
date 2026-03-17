Written to `simulations/quest/variations/trace-deployment-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — trace-deployment

5 variations across 3 single-axis then 2 combined:

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Pre-printed phase template — labeled fields per phase enforce C-01–C-05 structurally |
| **V-02** | Lifecycle emphasis | Explicit phase gates with "Do not proceed" barriers — gates state minimum counts and gap-with-fix requirement |
| **V-03** | Phrasing register | Conversational/imperative — no apparatus, short sentences, tests minimum-framing floor |
| **V-04** | Format + lifecycle | Template fields inside gates — pre-printed `Missing element:` / `Recommended fix:` sub-fields close C-05+C-08 simultaneously |
| **V-05** | Full synthesis | All axes + role sequence (Domain Expert named at top) + inertia framing (STATUS-QUO BASELINE block before PHASE 1) + GAP PRIORITY SUMMARY table (C-09) + automation hooks (C-10) |

**Key design bets:**

- **C-05** is the hardest to close. V-01 tests whether a pre-printed `Gap (phase):` field is enough. V-02 tests whether a gate condition naming "gap with fix" is enough. V-04 uses both. V-03 tests if plain imperative text is enough at all.
- **C-08 (actionable gaps)** is addressed in V-04+ by splitting the gap field into two sub-fields: `Missing element:` and `Recommended fix:`. A model filling two labeled sub-fields cannot satisfy the structural form with "missing X" alone.
- **Inertia framing** in V-05 anchors gap analysis to the known failure mode of the current deployment practice — the hypothesis being that gaps named relative to a concrete baseline are sharper than gaps generated in the abstract.
- **Predicted ceiling:** V-05 — all 10 rubric criteria have structural homes. V-04 is the closest competitor, missing only C-09 (gap priority ranking) and C-10 (automation hooks).
t deployment practice and its risk -- testing whether anchoring to
  the incumbent makes gap analysis sharper.

**Predicted ceiling:** V-05 -- maximum structural coverage; all C-01--C-10 have structural
homes. V-04 is the closest competitor (template + gates, closes C-01--C-08). V-03 tests the
minimum-overhead floor: can plain conversational instructions produce a passing trace?

---

## V-01: Pre-Printed Phase Template

**Axis:** Output format -- each phase is a pre-printed template block with labeled fields.
The model populates fields; it does not invent structure.
**Hypothesis:** Structural position enforces C-01 (>=3 checks), C-02 (>=4 steps), C-03
(>=2 validations), C-04 (rollback fields), and C-05 (pre-printed Gap field per phase)
more reliably than instructional prose. A model filling in `Gap (pre-deploy):` cannot omit
gap analysis for that phase. Tests whether template format alone, without explicit gates,
is sufficient for all essential criteria.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

Fill in this four-phase template exactly. Do not skip, rename, or reorder any section.
Every field must be populated. Use Commerce or Operations deployment vocabulary.

---

## PHASE 1: PRE-DEPLOY CHECKS

Check-01: [What is verified -- pass condition -- failure condition]
Check-02: [What is verified -- pass condition -- failure condition]
Check-03: [What is verified -- pass condition -- failure condition]
(Add Check-04+ if additional checks exist.)

Gap (pre-deploy): [One element missing or weak in this checklist -- and what should be added
                   to address it. "Missing X" alone does not pass; state the fix.]

---

## PHASE 2: DEPLOYMENT SEQUENCE

Step-01: [Action -- what is done, what it produces, precondition if any]
Step-02: [Action -- what is done, what it produces, precondition if any]
Step-03: [Action -- what is done, what it produces, precondition if any]
Step-04: [Action -- what is done, what it produces, precondition if any]
(Add Step-05+ if additional steps exist.)

Ordering dependency: [Name at least one step pair where Step-X MUST complete before Step-Y
                      can begin. Format: "Step-X must precede Step-Y because [reason]."
                      Implicit ordering in the list above does not satisfy this field.]

Gap (deployment sequence): [One element missing or weak in this sequence -- and the fix.]

---

## PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [What is checked -- expected result -- how failure appears]
Validation-02: [What is checked -- expected result -- how failure appears]
(Add Validation-03+ if additional validations exist.)

Gap (post-deploy): [One element missing or weak in post-deploy validation -- and the fix.]

---

## PHASE 4: ROLLBACK PATH

Trigger:      [Specific observable condition that initiates rollback -- not "if something fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
Rollback-03:  [Action]
Verification: [How you confirm rollback succeeded -- observable state, not "check the logs"]

Gap (rollback): [One element missing or weak in this rollback path -- and the fix.]

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count.
```

---

## V-02: Explicit Phase Gates

**Axis:** Lifecycle emphasis -- four phases separated by explicit "Do not proceed" gate
conditions. Each gate names the minimum counts and the gap requirement as pass conditions.
**Hypothesis:** A model that must explicitly pass GATE N before proceeding is less likely to
shortcut any phase. Gate conditions stating "at least one gap called out with a recommended
fix" are harder to skip than a pre-printed field the model can populate with a placeholder.
Tests whether gate enforcement outperforms template format for C-05 and C-08.

```
You are running /trace:deployment as a Commerce/Operations deployment domain expert.

Inputs:
  Topic:  {topic}
  Signal: {signal}

Trace the deployment lifecycle in four sequential phases. Each phase ends with a gate.
Do not begin the next phase until the current gate is met.

---

## PHASE 1: PRE-DEPLOY CHECKS

List every check that must pass before deployment begins. For each check: name what is
verified and what the failure condition is. Use Commerce or Operations domain vocabulary
(e.g., catalog sync state, inventory lock, tenant provisioning, order pipeline drain).

GATE 1: At least 3 concrete pre-deploy checks, each with a named failure condition.
        At least one gap in this checklist is identified with a specific recommended fix
        (not just a label). Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: DEPLOYMENT SEQUENCE

List every deployment step in numbered order. For each step: state the action, what it
produces, and what precondition (if any) must be true before it can begin. Identify at
least one ordering dependency explicitly -- a step that cannot start until a prior step
has fully completed. State why the ordering matters.

GATE 2: At least 4 numbered steps. At least one ordering dependency named explicitly with
        a reason. At least one gap in the sequence is identified with a specific recommended
        fix. Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: POST-DEPLOY VALIDATION

List every action taken after deployment to confirm the system is healthy. For each
validation: name what is checked, the expected result, and how failure would appear.

GATE 3: At least 2 specific validation actions with expected results and failure indicators.
        At least one gap in post-deploy validation is identified with a specific recommended
        fix. Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: ROLLBACK PATH

Describe the complete rollback path: what triggers it, each rollback step in order, and
how to confirm rollback succeeded. The trigger must be a specific observable condition --
not a general "if deployment fails" statement.

GATE 4: Trigger condition named as a specific observable signal. At least 2 rollback steps.
        Verification method states an observable outcome, not a process step.
        At least one gap in this rollback path is identified with a specific recommended fix.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count.
```

---

## V-03: Conversational / Imperative Register

**Axis:** Phrasing register -- short imperative sentences, no structural apparatus, no
pre-printed fields, no gates. Plain language.
**Hypothesis:** Some models perform better without structural scaffolding that creates
compliance overhead. A direct imperative style ("List the checks. Say what is missing.")
reduces the model's inference load about what counts as satisfying a gate. Tests whether
minimal-framing produces an acceptable trace for C-01--C-05 and how many recommended and
aspirational criteria survive without explicit structural prompts.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

You are a deployment domain expert for Commerce and Operations systems. Work through the
deployment lifecycle one phase at a time. Be specific. Use domain vocabulary.

---

**Pre-deploy checks.**
What has to be true before you touch anything? List at least 3 checks.
For each: name what you are verifying and what "failed" looks like.
Then: what is missing from this checklist? Name it and say what you would add.

**Deployment sequence.**
Walk through every deployment step in order. Number them. At least 4 steps.
For each step: say what is done and what it produces.
Call out at least one pair of steps where the second cannot start until the first is
completely finished -- and say why.
Then: what is fragile or missing in this sequence? Name it and say what you would fix.

**Post-deploy validation.**
What do you check after the deployment lands? List at least 2 specific actions.
For each: what are you looking for and what does failure look like?
Then: what is missing from this validation? Say what you would add.

**Rollback.**
What specific condition triggers a rollback? Name it.
Walk through the rollback steps.
How do you know rollback succeeded? State the observable outcome.
Then: what is weak or missing in this rollback path? Say what you would change.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count.
```

---

## V-04: Template Fields Inside Phase Gates (V-01 + V-02)

**Axis:** Format + lifecycle -- pre-printed template fields (V-01) inside explicit gate
conditions (V-02). Both mechanisms target C-05 simultaneously: the pre-printed Gap field
creates a structural home; the gate condition states the fill requirement.
**Hypothesis:** Neither format alone nor gates alone closes every failure mode for C-05 and
C-08. A model filling a pre-printed field may write "missing X" without a fix (fails C-08).
A gate condition without a field may allow a model to write a gap at the wrong granularity.
Combining them leaves no compliant path that fails either criterion.

```
You are running /trace:deployment as a Commerce/Operations deployment domain expert.

Inputs:
  Topic:  {topic}
  Signal: {signal}

Fill in the template below. All section headers and labeled fields are fixed.
Each phase ends with a gate -- do not proceed until the gate condition is met.

---

## PHASE 1: PRE-DEPLOY CHECKS

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing element: [Name what is absent or weak]
  Recommended fix: [What should be added or changed -- not just a label]

GATE 1: At least 3 checks present, each with a failure condition. Gap field has both
        sub-fields populated. Do not proceed to PHASE 2 until this gate is met.

---

## PHASE 2: DEPLOYMENT SEQUENCE

Step-01: [Action -- output -- precondition]
Step-02: [Action -- output -- precondition]
Step-03: [Action -- output -- precondition]
Step-04: [Action -- output -- precondition]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [Step numbers and explicit reason. Implicit list order
                                does not satisfy this field.]

Gap (deployment sequence):
  Missing element: [Name what is absent or weak]
  Recommended fix: [What should be added or changed]

GATE 2: At least 4 numbered steps. Ordering dependency field populated with explicit
        reason. Gap field has both sub-fields populated.
        Do not proceed to PHASE 3 until this gate is met.

---

## PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [Check -- expected result -- failure indicator]
Validation-02: [Check -- expected result -- failure indicator]
(Add Validation-03+ as needed.)

Gap (post-deploy):
  Missing element: [Name what is absent or weak]
  Recommended fix: [What should be added or changed]

GATE 3: At least 2 validations with expected results and failure indicators. Gap field
        has both sub-fields populated. Do not proceed to PHASE 4 until this gate is met.

---

## PHASE 4: ROLLBACK PATH

Trigger:      [Specific observable condition -- not "if deployment fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
Verification: [Observable outcome that confirms rollback succeeded]

Gap (rollback):
  Missing element: [Name what is absent or weak]
  Recommended fix: [What should be added or changed]

GATE 4: Trigger is a specific observable condition. At least 2 rollback steps. Verification
        states an observable outcome. Gap field has both sub-fields populated.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count.
```

---

## V-05: Full Synthesis (All Axes + Role Sequence + Inertia Framing)

**Axis:** All axes combined -- role sequence (Domain Expert role invoked by name before the
trace begins), inertia framing (current deployment practice and its risk named before any
phase), template fields (V-01), phase gates (V-02), and automation hooks as a pre-printed
field (C-10).
**Hypothesis:** Naming the status-quo deployment practice before the trace begins anchors
gap analysis to what is actually absent in the current process, not what is abstractly
possible to add. Role invocation at the top of the prompt biases domain vocabulary (C-07)
across all four phases without needing per-phase reminders. The automation hooks field in
PHASE 2 and PHASE 3 provides a structural home for C-10 that does not compete with gap
fields for C-05/C-08.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. You have seen deployments fail
at every phase -- pre-deploy environment drift, silent sequence violations, post-deploy
health gaps, and rollback triggers that never fire. You trace deployments to surface the
gaps before they surface in production.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest.

---

## STATUS-QUO BASELINE

Before tracing the deployment, name the current practice this deployment replaces or
builds on:

  Current approach: [How {topic} is currently deployed or provisioned -- or "no prior
                     process" if net-new]
  Known risk:       [What failure mode the current approach is exposed to that this
                     deployment must not inherit]

This baseline is referenced in the gap analysis for each phase below.

GATE 0: Current approach named. Known risk stated as a specific failure mode, not a
        general concern. Do not proceed to PHASE 1 until this gate is met.

---

## PHASE 1: PRE-DEPLOY CHECKS

Check-01: [Verified item -- pass condition -- failure condition]
Check-02: [Verified item -- pass condition -- failure condition]
Check-03: [Verified item -- pass condition -- failure condition]
(Add Check-04+ as needed.)

Gap (pre-deploy):
  Missing element: [What is absent or weak -- anchored to the STATUS-QUO baseline risk
                    if relevant]
  Recommended fix: [Specific change -- not just a label]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 1: At least 3 checks, each with a failure condition. Gap field fully populated
        with fix and severity. Do not proceed to PHASE 2 until this gate is met.

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
        Automation hook populated. Gap field fully populated with fix and severity.
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
        hook populated. Gap field fully populated with fix and severity.
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
  Missing element: [What is absent or weak -- e.g., trigger threshold undefined, no
                    verification probe, manual step with no owner]
  Recommended fix: [Specific change]
  Risk severity:   [critical / moderate / low -- one sentence justification]

GATE 4: Trigger is a specific observable condition. At least 2 rollback steps.
        Verification states an observable outcome. Gap field fully populated with fix
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
