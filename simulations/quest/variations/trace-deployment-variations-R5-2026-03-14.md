Written to `simulations/quest/variations/trace-deployment-variations-R5-2026-03-14.md`.

---

## Round 5 Variations — trace-deployment

**Rubric v5 context:** C-18 and C-19 were promoted from R4 patterns. Under v5, R4's V-02, V-04, V-05 retroactively score **130/145** (each picks up the new criterion they demonstrated). The ceiling is architecturally bounded at 130.

| V | Axis | Key mechanism | Predicted |
|---|------|---------------|-----------|
| **V-01** | Template ceiling (C-18 confirmation) | Gate-free fields + front-loaded skeleton | **130/145** |
| **V-02** | Prose ceiling (C-19 confirmation) | Inertia framing + prose saturation | **130/145** |
| **V-03** | C-17 + C-19 at single-sentence density | Contextual disqualifiers in semicolon-packed single sentences | **130/145** |
| **V-04** | Ceiling wall test (template + prose richness) | Template apparatus + contextual prose disqualifiers per phase | **130/145** |
| **V-05** | C-11 isolation (per-phase vocabulary) | V-01 with vocabulary moved from role block to per-phase sections | **125/145** |

**Three questions R5 answers:**

1. **Do both ceiling paths score 130 under v5?** V-01 and V-02 confirm — one via template, one via prose.

2. **Can C-17 + C-19 coexist at single-sentence density?** V-03 packs inertia-framing disqualifiers ("'someone escalates on Slack' does not pass") into one sentence per phase. If they survive compression, C-17 and C-19 both pass.

3. **Is C-11 role-block placement truly load-bearing?** V-05 is V-01 minus the role-block vocabulary list. Predicted 5-pt delta (125 vs 130) isolates the criterion cleanly.

**Ceiling architecture:**
```
Template path: C-09–C-14, C-16, C-18 = 8 criteria = 40 aspirational pts -> 130/145
Prose path:    C-09–C-13, C-15, C-17, C-19 = 8 criteria = 40 aspirational pts -> 130/145
Wall: C-14 (skeleton) and C-15 (no apparatus) are mutually exclusive
      -> C-18 and C-19 can never coexist -> hard ceiling 130/145
```

V-04 tests the wall directly: prose richness inside a template variation cannot convert C-15 because the template fields are still present. It stays at 130 via the template path regardless of how contextual the phase-level prose becomes.
g Confirmation (C-18)

**Axis:** Template field scaffolding -- gate-free fields + front-loaded skeleton.
**Hypothesis:** R4-V-02 confirmed C-14 and C-16 coexist. Under v5, that variation now
scores 130/145 by picking up C-18. V-01 is the clean minimal form of the template ceiling
path: V-01-R4 (gate-free fields, no skeleton = 120) + skeleton = +C-14 +C-18 = 130.
All three aspirational template criteria (C-14, C-16, C-18) pass simultaneously; C-15,
C-17, C-19 are blocked by template apparatus.
Predicted: C-14 PASS, C-16 PASS, C-18 PASS; C-15 FAIL, C-17 FAIL, C-19 FAIL -> **130/145**.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. You trace deployments to find
gaps before they surface in production.

Vocabulary in scope: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest.

Current practice:   [How {topic} is currently deployed -- or "net-new" if no prior
                     process exists]
Known failure mode: [The specific risk the current practice carries. One sentence,
                     concrete.]

Reference the current practice and failure mode in gap fields where relevant.

---

## GAP PLAN

Leave all rows blank. Do not pre-fill before tracing. Return here after Phase 4 and
rank all four gaps by deployment risk. The "Why this rank" column must compare this
gap against the others across all four phases -- not justify the phase's severity in
isolation.

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

Proceed to PHASE 1.

---

## PHASE 1: PRE-DEPLOY CHECKS

Check-01: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
Check-02: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
Check-03: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
(Add Check-04+ as needed.)

Automation hook:
  Hook-01: [Phase 1 location] | Enforces: [CI gate or pre-deploy script check] |
           Currently: [manual or absent]

Gap (pre-deploy):
  Missing:  [What is absent or weak -- reference baseline if relevant]
  Fix:      [Specific change -- not just a label]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 2: DEPLOYMENT SEQUENCE

Step-01: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-02: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-03: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-04: [Action] | Output: [result] | Precondition: [dependency or "none"]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [step numbers -- explicit reason, not sequential position]

Automation hook:
  Hook-01: [Phase 2 location] | Enforces: [CI gate or pre-deploy script check] |
           Currently: [manual or absent]

Gap (deployment sequence):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 3: POST-DEPLOY VALIDATION

Validation-01: [Check] | Expected: [result] | Failure indicator: [observable symptom]
Validation-02: [Check] | Expected: [result] | Failure indicator: [observable symptom]
(Add Validation-03+ as needed.)

Automation hook:
  Hook-01: [Phase 3 location] | Enforces: [canary assertion or health probe check] |
           Currently: [manual or absent]

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
(Add Rollback-03+ as needed.)
Verification: [Observable outcome -- state, metric, or probe result --
               that confirms rollback succeeded. Not "rollback complete."]

Gap (rollback):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

Return to the GAP PLAN above. Fill all four rows. Rank by deployment risk. The "Why
this rank" column must compare this gap against the others -- not justify phase
severity in isolation.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## V-02: Prose Ceiling Confirmation (C-19)

**Axis:** Prose saturation -- inertia framing + contextual failure-mode disqualifiers +
single-paragraph-per-phase density.
**Hypothesis:** R4-V-05 confirmed inertia-framing disqualifiers satisfy C-15. Under v5,
that variation now scores 130/145 by picking up C-19. V-02 is the clean minimal form of
the prose ceiling path. No template apparatus (no named sections, no template fields, no
gate markers) -> C-14 FAIL, C-16 FAIL, C-18 FAIL. Prose achieves C-12 and C-13 through
explicit instructions. Contextual disqualifiers satisfy C-19. Paragraph-per-phase density
satisfies C-17.
Predicted: C-15 PASS, C-17 PASS, C-19 PASS; C-14 FAIL, C-16 FAIL, C-18 FAIL -> **130/145**.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

You are a Commerce/Operations deployment domain expert who has traced the same {topic}
deployment failure twice: engineers run the sequence from memory, a step executes out
of order, schema changes hit in-flight transactions, logs look clean, and data
corruption surfaces hours later from customer reports. Your vocabulary: catalog sync,
order pipeline drain, inventory lock, tenant provisioning, feature flag gate,
environment parity check, health probe, rollback threshold, canary assertion, circuit
breaker, deployment manifest. Use these terms.

State the current deployment practice for {topic} and the specific failure mode it
carries -- this is your baseline; reference it where gap analysis connects directly.

---

List at least 3 pre-deploy checks; for each, name what is verified and what failure
looks like -- a check that says "confirm environment is ready" does not name a
verifiable condition and does not pass; then identify what the current practice leaves
unchecked, state what should be added, and rate severity (critical / moderate / low)
with a one-sentence comparison to the risk the baseline failure mode already carries.

Number at least 4 deployment steps with the action and its precondition; name at
least one step pair where the second cannot begin until the first fully completes and
state why -- "schema migration before service restart" passes; "migration, then
restart" does not; name one CI gate or pre-deploy script that could enforce a check
currently done from memory; then identify what ordering gap or missing enforcement the
current practice embeds, state the fix, and rate severity.

List at least 2 post-deploy validation actions with the probe name, expected result,
and failure indicator -- "monitor for errors" does not name a probe or an expected
state and does not pass; name one canary assertion or health probe that could replace
the current practice of watching logs; then identify what the current validation
approach misses, state what should replace it, and rate severity.

Name the specific threshold or probe result that triggers rollback -- "someone notices
it looks bad" does not pass; list rollback steps; state the observable outcome that
confirms rollback succeeded -- not "we redeployed"; then identify what the rollback
path still leaves undefined, state the fix, and rate severity.

Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank
-- rank all four gaps by deployment blast radius; a severity assignment that does not
compare this gap against the baseline failure mode and the other three gaps does not
satisfy the ranking requirement.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count.
```

---

## V-03: C-17 + C-19 at Single-Sentence Density

**Axis:** Phrasing register (extreme compression) x inertia framing (contextual
failure-mode disqualifiers). Tests whether contextual disqualifiers survive semicolon-
packed single-sentence-per-phase form.
**Hypothesis:** R4-V-03 confirmed C-17 holds at single-sentence density using abstract
disqualifiers. R4-V-05 confirmed contextual disqualifiers satisfy C-19. V-03 combines
both: contextual disqualifiers ("someone escalates on Slack does not pass") packed into
single-sentence form. If inertia-framing disqualifiers compress without losing the named-
weak-response-form function, C-17 and C-19 pass simultaneously. No template apparatus ->
C-14 FAIL, C-16 FAIL, C-18 FAIL.
Predicted: C-15 PASS, C-17 PASS, C-19 PASS; C-14 FAIL, C-16 FAIL, C-18 FAIL -> **130/145**.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

You are a Commerce/Operations deployment expert who last traced a {topic} incident
where the rollback trigger was "someone escalates on Slack" -- firing 4 hours after
health degraded and leaving orphaned inventory locks because nobody defined what
"rollback succeeded" meant. Vocabulary: catalog sync, order pipeline drain, inventory
lock, tenant provisioning, feature flag gate, environment parity check, health probe,
rollback threshold, canary assertion, circuit breaker, deployment manifest. Use these
terms.

State the current deployment practice and its specific failure mode before tracing.

---

List at least 3 pre-deploy checks (what is verified, what failure looks like) --
"check that the environment is ready" does not identify a verifiable artifact or state
and does not pass; then name what the current practice leaves unchecked, state the
fix, and rate severity (critical / moderate / low) with one sentence comparing this
gap to the failure mode the current practice already carries.

Number at least 4 deployment steps (action, precondition); name at least one step
pair where the second cannot start until the first fully completes and state why --
"schema migration must precede service restart to prevent in-flight transaction
corruption" passes; "run them in order" does not; name one CI gate enforcing a check
currently run from memory; then name the gap, fix, and severity.

List at least 2 post-deploy validations (probe name, expected result, failure
indicator) -- "confirm the service is working" does not name a measurable probe or
pass threshold and does not pass; name one canary assertion replacing a currently
manual observation; then name the gap, fix, and severity.

Name the specific metric threshold or probe result that triggers rollback -- "someone
escalates on Slack" does not name an observable threshold and does not pass; list
rollback steps; state the observable outcome confirming rollback succeeded -- not
"rollback complete"; then name the gap, fix, and severity.

Produce a gap table (Rank, Phase, Gap summary, Severity, Why this rank) ranked by
deployment blast radius -- a Why cell that does not compare this gap against the other
three and the stated failure mode does not satisfy the cross-comparison requirement.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count.
```

---

## V-04: Ceiling Wall Test (Template + Contextual Prose Richness)

**Axes:** Output format (template fields + skeleton) x inertia framing (contextual
prose disqualifiers per phase). Tests whether prose richness inside a template-path
variation can unlock C-15.
**Hypothesis:** C-15 requires absence of "structural template apparatus (named sections,
template fields, or gate markers)." V-04 embeds rich prose instructions -- including
contextual disqualifiers -- alongside template fields and a front-loaded skeleton.
Prediction: the template apparatus is present regardless of prose richness, so C-15
fails. V-04 lands at 130/145 via the template path (C-14 + C-16 + C-18), not by
crossing into the prose path. The ceiling wall holds: prose richness cannot convert
C-15/C-17/C-19 when template fields are present.
Predicted: C-14 PASS, C-16 PASS, C-18 PASS; C-15 FAIL, C-17 FAIL, C-19 FAIL -> **130/145**.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. In your last {topic} incident,
a schema migration executed after a service restart -- the rollback script ran but
left orphaned inventory locks because nobody defined what "rollback succeeded" meant.
Your vocabulary: catalog sync, order pipeline drain, inventory lock, tenant
provisioning, feature flag gate, environment parity check, health probe, rollback
threshold, canary assertion, circuit breaker, deployment manifest. Use these terms.

Current practice:   [How {topic} is currently deployed -- or "net-new" if no prior
                     process exists]
Known failure mode: [The specific risk the current practice carries. One sentence.]

Reference the current practice and failure mode in gap fields where relevant.

---

## GAP PLAN

Leave all rows blank. Do not pre-fill before tracing. Return here after Phase 4 and
rank all four gaps by deployment risk. The "Why this rank" column must compare this
gap against the others -- not justify phase severity in isolation.

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

Proceed to PHASE 1.

---

## PHASE 1: PRE-DEPLOY CHECKS

Name at least 3 checks -- "verify the environment" does not name a verifiable artifact
or state and does not pass; each check must name what is verified and what failure
looks like.

Check-01: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
Check-02: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
Check-03: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
(Add Check-04+ as needed.)

Automation hook:
  Hook-01: [Phase 1 location] | Enforces: [CI gate or pre-deploy script] |
           Currently: [manual or absent]

Gap (pre-deploy):
  Missing:  [What is absent -- reference baseline where the connection is direct]
  Fix:      [Specific change -- not just a label]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 2: DEPLOYMENT SEQUENCE

Name at least 4 steps -- "run the deploy script" is not a discrete step and does not
pass; each step must name an action, its output, and its precondition.

Step-01: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-02: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-03: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-04: [Action] | Output: [result] | Precondition: [dependency or "none"]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [step numbers -- explicit reason, not sequential position]

Automation hook:
  Hook-01: [Phase 2 location] | Enforces: [CI gate or pre-deploy script] |
           Currently: [manual or absent]

Gap (deployment sequence):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 3: POST-DEPLOY VALIDATION

Name at least 2 validations -- "monitor the logs" does not name a probe or a pass
threshold and does not pass; each validation must name the probe, expected result,
and failure indicator.

Validation-01: [Check] | Expected: [result] | Failure indicator: [observable symptom]
Validation-02: [Check] | Expected: [result] | Failure indicator: [observable symptom]
(Add Validation-03+ as needed.)

Automation hook:
  Hook-01: [Phase 3 location] | Enforces: [canary assertion or health probe] |
           Currently: [manual or absent]

Gap (post-deploy):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 4: ROLLBACK PATH

Name the trigger -- "if deployment fails" does not name an observable threshold and
does not pass; name the specific metric, probe result, or signal. State what "rollback
succeeded" means -- not "we redeployed."

Trigger:      [Specific observable condition]
Rollback-01:  [Action]
Rollback-02:  [Action]
(Add Rollback-03+ as needed.)
Verification: [Observable outcome confirming rollback succeeded]

Gap (rollback):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

Return to GAP PLAN. Fill all rows. Rank by deployment blast radius. "Why this rank"
must compare this gap against the others -- not restate phase severity in isolation.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## V-05: C-11 Isolation (Per-Phase Vocabulary Distribution)

**Axis:** Output format -- V-01 architecture with vocabulary moved from role block to
per-phase "Use these domain terms" instructions.
**Hypothesis:** C-11 requires "a named list of domain terms in the role/persona block"
and states "Per-phase vocabulary distribution is not a substitute -- role-block placement
is load-bearing." V-05 keeps all other V-01 features intact (gate-free fields, front-
loaded skeleton, baseline fields in ROLE) but moves the vocabulary list to per-phase
sections. Predicted C-11 FAIL causes a clean 5-pt delta: 130 (V-01) -> 125. C-14 and
C-18 are unaffected. C-12 passes via "Current practice / Known failure mode" fields
remaining in ROLE, confirming C-12 does not require C-11.
Predicted: C-14 PASS, C-16 PASS, C-18 PASS, C-11 FAIL; C-15 FAIL, C-17 FAIL, C-19 FAIL
-> **125/145**.

```
You are running /trace:deployment.

Inputs:
  Topic:  {topic}
  Signal: {signal}

---

## ROLE

You are a Commerce/Operations deployment domain expert. You trace deployments to find
gaps before they surface in production.

Current practice:   [How {topic} is currently deployed -- or "net-new" if no prior
                     process exists]
Known failure mode: [The specific risk the current practice carries. One sentence,
                     concrete.]

Reference the current practice and failure mode in gap fields where relevant.

---

## GAP PLAN

Leave all rows blank. Do not pre-fill before tracing. Return here after Phase 4 and
rank all four gaps by deployment risk. The "Why this rank" column must compare this
gap against the others across all four phases -- not justify the phase's severity in
isolation.

| Rank | Phase | Gap summary | Severity | Why this rank |
|------|-------|-------------|----------|---------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

Proceed to PHASE 1.

---

## PHASE 1: PRE-DEPLOY CHECKS

Use these domain terms where relevant: environment parity check, feature flag gate,
deployment manifest, tenant provisioning.

Check-01: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
Check-02: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
Check-03: [What is verified] | Pass: [condition] | Failure: [what failure looks like]
(Add Check-04+ as needed.)

Automation hook:
  Hook-01: [Phase 1 location] | Enforces: [CI gate or pre-deploy script check] |
           Currently: [manual or absent]

Gap (pre-deploy):
  Missing:  [What is absent or weak -- reference baseline if relevant]
  Fix:      [Specific change -- not just a label]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 2: DEPLOYMENT SEQUENCE

Use these domain terms where relevant: catalog sync, order pipeline drain, inventory
lock, circuit breaker.

Step-01: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-02: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-03: [Action] | Output: [result] | Precondition: [dependency or "none"]
Step-04: [Action] | Output: [result] | Precondition: [dependency or "none"]
(Add Step-05+ as needed.)

Ordering dependency:
  Step-X must precede Step-Y: [step numbers -- explicit reason, not sequential position]

Automation hook:
  Hook-01: [Phase 2 location] | Enforces: [CI gate or pre-deploy script check] |
           Currently: [manual or absent]

Gap (deployment sequence):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 3: POST-DEPLOY VALIDATION

Use these domain terms where relevant: health probe, canary assertion, rollback
threshold, order pipeline drain.

Validation-01: [Check] | Expected: [result] | Failure indicator: [observable symptom]
Validation-02: [Check] | Expected: [result] | Failure indicator: [observable symptom]
(Add Validation-03+ as needed.)

Automation hook:
  Hook-01: [Phase 3 location] | Enforces: [canary assertion or health probe check] |
           Currently: [manual or absent]

Gap (post-deploy):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

## PHASE 4: ROLLBACK PATH

Use these domain terms where relevant: rollback threshold, health probe, inventory
lock, circuit breaker.

Trigger:      [Specific observable condition -- threshold, probe result, or signal --
               not "if deployment fails"]
Rollback-01:  [Action]
Rollback-02:  [Action]
(Add Rollback-03+ as needed.)
Verification: [Observable outcome -- state, metric, or probe result --
               that confirms rollback succeeded. Not "rollback complete."]

Gap (rollback):
  Missing:  [What is absent or weak]
  Fix:      [Specific change]
  Severity: [critical / moderate / low -- one sentence why]

---

Return to the GAP PLAN above. Fill all four rows. Rank by deployment risk. The "Why
this rank" column must compare this gap against the others -- not justify phase
severity in isolation.

---

Write artifact: simulations/trace/deployment/{topic}-deployment-{date}.md
Frontmatter: skill, topic, date, signal, phase_count, check_count, step_count,
             validation_count, rollback_step_count, gap_count, automation_hook_count,
             status_quo_baseline.
```

---

## Ceiling Architecture (R5 Stable View)

```
Template path:  C-09 C-10 C-11 C-12 C-13 C-14      C-16           C-18 = 8 x 5 = 40 pts
Prose path:     C-09 C-10 C-11 C-12 C-13      C-15      C-17 C-19      = 8 x 5 = 40 pts
Both paths:     60 (essential) + 30 (recommended) + 40 (aspirational)  = 130/145

Wall:           C-14 requires skeleton (structural apparatus)
                C-15 requires NO structural apparatus
                -> C-18 (needs C-14+C-16) and C-19 (needs C-15) never coexist
                -> Ceiling is 130/145 for any single variation

V-05 delta:     V-01 minus C-11 (vocabulary not in role block) = 130 - 5 = 125/145
                Confirms role-block placement in C-11 is load-bearing (per rubric spec)
```

```json
{"rubric_version": "v5", "rubric_total": 145, "predicted_ceiling": 130, "all_golden": true,
 "template_path_criteria": ["C-14","C-16","C-18"], "prose_path_criteria": ["C-15","C-17","C-19"],
 "wall_criteria": ["C-14","C-15"], "isolation_test": "C-11"}
```
