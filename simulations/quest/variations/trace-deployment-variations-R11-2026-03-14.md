Now I have the full picture. The rubric ceiling note is explicit: *"A future variation combining interrogative headers with exactly three rollback fields would reach 160/185."* That's the primary target for R11. The remaining four axes test unconfirmed combinations from the criteria map.

---

# trace-deployment Variations R11

**Rubric version**: v9 | **Criteria**: 27 | **Total**: 185 pts
**Current ceiling**: 155/185 — C-26 and C-27 never simultaneously achieved in R10

**Variation map**:

| Variation | Single-axis | Primary new criterion target |
|-----------|-------------|------------------------------|
| V-01 | Phrasing register — interrogative + bare + minimum rollback | C-26 ∩ C-22 ∩ C-27 (ceiling test; predicts 160/185) |
| V-02 | Inertia framing — dual role-block voice | C-23 ∩ C-25 simultaneous |
| V-03 | Output format — prose path + question-form disqualifiers | C-19/C-20 via question-form negation syntax |
| V-04 | Lifecycle emphasis — rollback-heavy asymmetric depth | C-16/C-18 at asymmetric field distribution; interleaved step/verify pattern |
| V-05 | Combination: V-01 + V-02 axes | C-26 + C-22 + C-27 + C-23 + C-25 all simultaneous |

---

## V-01

**Variation axis**: Phrasing register — interrogative-question section headers (C-26) + bare field labels (C-22) + exactly 3 rollback fields (C-27)

**Hypothesis**: C-26, C-22, and C-27 are jointly satisfiable in a single variation. R10 V-01 passed C-26 but had `undo-2` beyond the minimum, preventing C-27. R10 V-02 passed C-27 at minimum rollback but used non-interrogative headers, preventing C-26. The rubric ceiling note predicts this combination yields 160/185 — this variation tests whether that ceiling is achievable. The interrogative register is orthogonal to field-label sparsity and rollback depth.

**Expected criteria**: C-01–C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21, C-22, C-24, C-25, C-26, C-27 — 18 criteria passing if hypothesis holds.

```markdown
ROLE: Commerce/Operations deployment engineer.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
schema migration, service mesh cutover, feature flag gate, blast radius, rollback window.
Current practice: deployments follow a manual runbook executed day-of; post-deploy
validation is a verbal team check with no defined pass/fail threshold.
Known failure mode: rollback is initiated by engineer judgment — no trigger condition
exists; engineers debate whether to roll back while the incident is active.

INPUT: {{solution}} — {{deployment_type}} (deploy / import / migrate)

---

GAP SKELETON — fill this before Phase 1. Return after each phase to update severity
with evidence from the trace. Compare all gaps against each other before finalizing
ranks — a gap that blocks rollback outranks a gap that only delays detection.
Do not pre-fill.

| Phase | Gap | Severity | Why |
|-------|-----|----------|-----|
| pre-deploy | | | |
| sequence | | | |
| post-deploy | | | |
| rollback | | | |

---

what needs to be true before we touch this?

check-1:
check-2:
check-3:
check-4:

what's the deployment order?

step-1:
step-2:
step-3:
step-4:
step-5:

order-dep-1:

did it land?

val-1:
val-2:
val-3:

hook-1:

what do we do if it didn't?

undo-trigger:
undo-1:
confirmed-back:
```

---

## V-02

**Variation axis**: Inertia framing — role block contains both present-tense operational baseline (C-25) AND first-person inertia narrative (C-23) simultaneously

**Hypothesis**: C-23 and C-25 are jointly satisfiable — the two role-block voice patterns occupy the same structural position without conflict. C-25 requires "Current practice: / Known failure mode:" framing without incident narrative; C-23 requires incident narrative without that disqualifying C-20. The rubric states "A variation whose role block contains only present-tense operational framing passes C-25 and fails C-23; a variation with inertia narrative but no operational baseline framing passes C-23 and fails C-25." Neither criterion states the other's pattern must be absent — they are non-overlapping on the inertia-narrative-presence dimension. A role block with both patterns should satisfy each independently. The disqualifier in the body uses domain-contextual vocabulary only (no incident framing) to keep C-20 evaluable.

**Expected criteria**: C-01–C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-20, C-23, C-25 — 16 criteria passing if hypothesis holds. C-21/C-22/C-24 do not pass (formal template labels; inline prose present). C-26/C-27 do not pass (non-interrogative headers; rollback exceeds 3 fields).

```markdown
ROLE: Commerce/Operations deployment engineer.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
schema migration, service mesh cutover, feature flag gate, blast radius, rollback window.
Current practice: pre-deploy checks are manual and vary by engineer; post-deploy
validation is a 15-minute observation window with no defined pass/fail signal.
Known failure mode: rollback trigger is undefined — engineers decide by consensus
whether to roll back, with no threshold forcing the decision.
After the tenant provisioning outage we learned that observation windows without named
pass/fail conditions cannot tell you when to call a deployment clean — "it seems OK"
is not a validation outcome.

INPUT: {{solution}} — {{deployment_type}} (deploy / import / migrate)

---

GAP SKELETON — complete before Phase 1. Return after each phase to update.
Compare gaps across all phases before finalizing severity — a gap that removes the
ability to roll back ranks above all others. Do not pre-fill.

| Phase | Gap | Severity | Why |
|-------|-----|----------|-----|
| pre-deploy | | | |
| sequence | | | |
| post-deploy | | | |
| rollback | | | |

---

## PHASE 1 — PRE-DEPLOY CHECKS

Check-01:
Check-02:
Check-03:
Check-04:

## PHASE 2 — DEPLOYMENT SEQUENCE

Step-01:
Step-02:
Step-03:
Step-04:
Step-05:
Step-06:

Ordering-dep-01:

## PHASE 3 — POST-DEPLOY VALIDATION

Validation-01:
Validation-02:
Validation-03:

Hook-01:
Hook-02:

## PHASE 4 — ROLLBACK PATH

Trigger:
Rollback-01:
Rollback-02:
Rollback-03:
Verification:
```

---

## V-03

**Variation axis**: Output format — prose-instruction path (C-15/C-17) with question-form disqualifying examples as the syntax for C-19/C-20

**Hypothesis**: A disqualifying example expressed as question-form negation — "'Did it come back up?' is not a post-deploy validation — it names no probe, threshold, or observable system state" — satisfies C-19's contextual failure-mode requirement at equal force to declarative domain-contextual framing. C-20 compliance follows because no incident narrative is invoked. If this holds, question-form negation is a fourth disqualifier syntax, distinct from: abstract criterion label (fails C-19), inertia-sourced (passes C-19, fails C-20), domain-contextual declarative (passes C-20). The prose path (C-15) requires explicit naming of output elements, a cross-gap comparison mandate, and a disqualifying example — all three are satisfied here at single-paragraph-per-phase density (C-17).

**Expected criteria**: C-01–C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-25 — 14 criteria passing if hypothesis holds. C-14/C-16/C-18 do not pass (no front-loaded skeleton; no template fields). C-21/C-22/C-24/C-26/C-27 not applicable (prose path, no fields).

```markdown
ROLE: Commerce/Operations deployment engineer.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
schema migration, service mesh cutover, feature flag gate, blast radius, rollback window.
Current practice: deployments follow a runbook maintained by infrastructure; post-deploy
validation is a passive monitoring period with no named signals.
Known failure mode: rollback trigger is undefined — engineers initiate rollback by
consensus when something seems wrong, not when a defined threshold is crossed.

INPUT: {{solution}} — {{deployment_type}} (deploy / import / migrate)

---

Trace the full deployment lifecycle across four phases.

Pre-deploy: list at least 3 concrete checks. For each check, name what is being
verified and what failure looks like. A check that asks "is everything ready?" names
no specific condition and does not qualify — name the system state being confirmed.

Deployment sequence: number every step. Provide at least 4 discrete steps in explicit
order. Call out at least one ordering dependency — a step that cannot begin until a
prior step is confirmed complete.

Post-deploy validation: identify at least 2 specific validation actions. For each,
name the probe and the pass/fail threshold. "Did it come back up?" is not a validation
action — it names no probe, no threshold, and no observable system state.

Rollback: define the trigger condition, the steps that undo the deployment, and the
verification that rollback succeeded. A rollback path containing no trigger condition
does not satisfy this requirement.

Gap analysis: call out at least one missing or weak element per phase — pre-deploy,
sequence, post-deploy, rollback. For each gap, state what should be added or changed;
naming the gap without stating the fix does not pass. Compile all gaps into a
cross-phase summary table with columns: Phase, Gap, Severity, Why. Assign severity
only after comparing gaps across phases — a gap that blocks rollback ranks above a
gap that only delays detection.

Identify at least one place in the deployment lifecycle where a CI gate, pre-deploy
script, or canary assertion could enforce a check that is currently manual.

Use Commerce/Operations deployment vocabulary throughout: catalog sync, order pipeline
drain, inventory lock, tenant provisioning, schema migration, service mesh cutover.
```

---

## V-04

**Variation axis**: Lifecycle emphasis — rollback-heavy asymmetric template with interleaved step/verify field pairs; other phases held at essential-coverage floor

**Hypothesis**: Template-path criteria (C-14, C-16, C-18) are satisfied at asymmetric field depth. Essential-coverage floors are per-phase minimums, not symmetric density requirements — the rubric specifies field-count floors for each phase independently. A rollback section elaborated beyond C-27's 3-field minimum (using interleaved `undo-N` + `undo-verify-N` pairs) satisfies C-04 and C-16 more thoroughly without disqualifying the template path. C-27 does not pass (field count exceeds exactly-3 minimum), but C-27 non-passage does not affect C-16/C-18 evaluation. New discovery target: whether interleaved per-step verification within rollback is a structural pattern distinct from the minimum-viable floor — a candidate for future codification.

**Expected criteria**: C-01–C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21 — 13 criteria passing. C-22/C-24 do not pass (imperative colloquial register but inline hook instruction present). C-26 does not pass (imperative, not interrogative). C-27 does not pass (exceeds minimum rollback field count). C-23/C-25 depend on role-block voice used.

```markdown
ROLE: Commerce/Operations deployment engineer.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
schema migration, service mesh cutover, feature flag gate, blast radius, rollback window.
Current practice: rollback procedures are documented but untested in production;
pre-deploy checks are manual and vary by engineer.
Known failure mode: rollback steps assume a clean prior state that may not exist —
there is no intermediate verification between rollback steps to confirm each prior
state was restored before proceeding.

INPUT: {{solution}} — {{deployment_type}} (deploy / import / migrate)

---

GAP SKELETON — fill before any phase. Return after each phase to update. Compare
all gaps against each other before assigning final severity — a gap that makes
rollback unreliable ranks above all others. Do not pre-fill.

| Phase | Gap | Severity | Why |
|-------|-----|----------|-----|
| pre-deploy | | | |
| sequence | | | |
| post-deploy | | | |
| rollback | | | |

---

Before you touch anything:

check-1:
check-2:
check-3:

Deployment steps:

step-1:
step-2:
step-3:
step-4:

order-dep-1:

Did it land?

val-1:
val-2:

Automation hook — where in this sequence could a CI gate, pre-deploy script, or
canary assertion catch a failure that is currently manual?
hook-1:

If rollback is needed:

undo-trigger:
undo-1:
undo-verify-1:
undo-2:
undo-verify-2:
undo-3:
undo-verify-3:
rollback-complete:
```

---

## V-05

**Variation axis**: Combination — interrogative-question headers (C-26) + bare field labels (C-22) + exactly 3 rollback fields (C-27) + dual role-block voice (C-23 inertia + C-25 operational baseline)

**Hypothesis**: C-23, C-25, C-26, C-22, and C-27 are simultaneously satisfiable. V-01 establishes the interrogative/bare/minimum-rollback architecture. V-02 establishes dual role-block voice. The two sets of criteria are structurally independent: role-block voice (C-23/C-25) is evaluated on the persona block content; template architecture (C-26/C-22/C-27) is evaluated on field structure and section headers. No criterion in either set requires the other to be absent. If this variation passes, it confirms that the full set of R8/R9/R10 excellence criteria can coexist, and establishes a new ceiling candidate above 160/185. Disqualifier in the body is absent (prose-instruction path not used) — C-19/C-20 are not the target here; the role block's inertia narrative is evaluated only for C-23.

**Expected criteria**: C-01–C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-18, C-21, C-22, C-23, C-24, C-25, C-26, C-27 — 19 criteria passing if hypothesis holds.

```markdown
ROLE: Commerce/Operations deployment engineer.
Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning,
schema migration, service mesh cutover, feature flag gate, blast radius, rollback window.
Current practice: pre-deploy checks are manual; post-deploy validation is a verbal
team check with no defined pass/fail threshold.
Known failure mode: rollback trigger is undefined — engineers debate whether to roll
back while the incident is active; the decision is made by consensus, not by signal.
After the catalog sync migration we learned that undefined rollback triggers do not get
called until the blast radius is already wide — the decision needs to be pre-made,
not debated in the moment.

INPUT: {{solution}} — {{deployment_type}} (deploy / import / migrate)

---

GAP SKELETON — fill before Phase 1. Return after each phase to update severity with
evidence from the trace. Compare all gaps against each other before finalizing ranks
— a gap that removes the ability to roll back outranks all others. Do not pre-fill.

| Phase | Gap | Severity | Why |
|-------|-----|----------|-----|
| pre-deploy | | | |
| sequence | | | |
| post-deploy | | | |
| rollback | | | |

---

what needs to be true before we touch this?

check-1:
check-2:
check-3:
check-4:

what's the deployment order?

step-1:
step-2:
step-3:
step-4:
step-5:

order-dep-1:

did it land?

val-1:
val-2:
val-3:

hook-1:

what do we do if it didn't?

undo-trigger:
undo-1:
confirmed-back:
```

---

## Criteria coverage matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01–C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 order dep | PASS | PASS | PASS | PASS | PASS |
| C-07 domain vocab | PASS | PASS | PASS | PASS | PASS |
| C-08 actionable gaps | PASS | PASS | PASS | PASS | PASS |
| C-09 gap priority | PASS | PASS | PASS | PASS | PASS |
| C-10 automation hook | PASS | PASS | PASS | PASS | PASS |
| C-11 vocab in role block | PASS | PASS | PASS | PASS | PASS |
| C-12 status-quo baseline | PASS | PASS | PASS | PASS | PASS |
| C-13 cross-phase gap table | PASS | PASS | PASS | PASS | PASS |
| C-14 front-loaded skeleton | PASS | PASS | — | PASS | PASS |
| C-15 prose saturation | — | — | PASS | — | — |
| C-16 gate-free template | PASS | PASS | — | PASS | PASS |
| C-17 C-15 at min density | — | — | PASS | — | — |
| C-18 C-14 + C-16 | PASS | PASS | — | PASS | PASS |
| C-19 contextual disqualifier | — | — | ? | — | — |
| C-20 non-inertia disqualifier | — | PASS | ? | — | — |
| C-21 colloquial register | PASS | — | — | PASS | PASS |
| C-22 bare field labels | PASS | — | — | — | PASS |
| C-23 role inertia narrative | — | ? | — | — | ? |
| C-24 C-21 + C-22 | PASS | — | — | — | PASS |
| C-25 operational persona | PASS | ? | PASS | — | ? |
| C-26 interrogative register | PASS | — | — | — | PASS |
| C-27 min rollback 3 fields | PASS | — | — | — | PASS |

`?` = new test; answer unknown before scoring. `—` = not applicable / not targeted by this variation.

**Primary discovery targets**:
- V-01: Does C-26 ∩ C-22 ∩ C-27 hold? Rubric ceiling note predicts 160/185 if yes.
- V-02/V-05: Does C-23 ∩ C-25 hold in a single role block?
- V-03: Does question-form negation satisfy C-19/C-20?
- V-04: Does the interleaved `undo-N` + `undo-verify-N` pattern warrant codification above C-27?
