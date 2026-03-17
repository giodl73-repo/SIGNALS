# /quest:variate — `trace:deployment` — Round 17

**Rubric**: v13 (220 pts, 34 criteria) | **Date**: 2026-03-15
**Prose structural-adoption ceiling entering R17**: 175/220 (V-04, confirmed C-33 + C-34)
**Template ceiling entering R17**: 175/220 (template path, independently)
**Both paths converge at**: 165/210 re-scored as 175/220 after C-33 + C-34 added

**R17 focus**: Probe the 45 uncracked aspirational points above the 175 ceiling. Three candidate
activation surfaces: (a) inertia framing that grounds gap severity in historical deployment cost,
(b) lifecycle emphasis that exceeds minimum thresholds per phase, (c) cross-axis compounds.

**Single-axis variations**: V-01 (inertia framing), V-02 (lifecycle emphasis), V-03 (phrasing register)
**Combined variations**: V-04 (inertia + structural adoption), V-05 (inertia + lifecycle + role depth)

---

## Round 17 Variation Map

| Variation | Axis | Hypothesis | Target criteria |
|-----------|------|-----------|-----------------|
| V-01 | Inertia framing | Status-quo section before phases grounds gap severity in historical cost | C-09, possible C-35+ |
| V-02 | Lifecycle emphasis | Above-minimum counts per phase activate richness criteria | C-06, C-08, possible C-35+ |
| V-03 | Phrasing register | Formal spec-prose headers test whether C-21/C-26 are interrogative-exclusive | C-21/C-26 boundary |
| V-04 | Inertia + structural adoption | Inertia framing compounds on confirmed ceiling path | C-09 + C-33 joint activation |
| V-05 | Inertia + lifecycle + role depth | Triple compound probes deepest aspirational criteria | C-09, C-10, C-11, new territory |

---

## V-01

**Axis**: Inertia framing
**Hypothesis**: Opening with an explicit Status Quo section — naming the team's current runbook,
the last known deployment failure, and its cost — before any phase trace forces gap severity to
be grounded in historical blast-radius evidence. This may activate a criterion for grounding
gap rankings in real deployment history rather than abstract severity labels. If the inertia
section anchors the gap table's Severity column in named historical cost, C-09 activates more
reliably; if it also introduces a criterion for "failure history as input to gap analysis," a
new criterion promotes.
**Predicted delta if inertia anchors C-09 and activates new criterion**: 175 → 185+

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.

STATUS QUO

Before tracing the deployment of {{TOPIC}}, record the current state:

1. Current runbook: What does this team actually do today? Name their existing
   deployment sequence — the shared checklist, approval gates, and sequence as
   practiced. If they have no formal runbook, state that explicitly.

2. Last known failure: What deployment failure has this team experienced? Name the
   specific check or step that was skipped, what broke, and the operational cost
   (downtime window, orders lost, manual recovery time, or equivalent Commerce/
   Operations blast-radius metric). If no failure is documented, state that and
   explain what this means for gap confidence.

3. Known runbook gap: Based on the last failure, what single addition to the current
   runbook would have prevented it? Name the specific check or step.

This Status Quo section is an input to the gap analysis in all four phases below.
Every gap you identify must be compared against the known failure history before
Severity is assigned — a gap that contributed to a past failure is automatically
critical regardless of theoretical severity.

PRE-DEPLOY CHECKS

List at least 3 checks. For each, name what is being verified and what failure
looks like. "'Verify the environment is healthy' names no specific condition and
does not qualify." Where a check directly addresses the known runbook gap, say so.

DEPLOYMENT SEQUENCE

List at least 4 steps in execution order. Call out at least one ordering dependency
explicitly — the step that must complete before the next can begin, and what breaks
if it does not.

POST-DEPLOY VALIDATION

List at least 2 validation actions. Each must name a probe, threshold, or
data-integrity assertion. "A validation that asks 'did the deployment succeed?' names
no probe or threshold and does not qualify."

ROLLBACK

State the rollback trigger, at least one undo step, and how to verify rollback
succeeded. If the known failure above had no rollback path, note that explicitly as
a gap.

CROSS-PHASE GAP ANALYSIS

Produce a table: Phase | Gap | Severity (critical / moderate / low) | Why. One gap
per phase minimum. Before assigning Severity, compare each gap against every other
and against the known failure history — a gap that contributed to a past failure is
critical. State what should be added or changed for each gap; naming a gap without
a remedy does not qualify. Identify at least one automation hook in the deployment
lifecycle — name where in the sequence it would fire and what it would enforce.
```

---

## V-02

**Axis**: Lifecycle emphasis
**Hypothesis**: Raising minimum counts above rubric floor — 4+ pre-deploy checks (not 3),
6+ deployment steps (not 4), 3+ post-deploy validations (not 2), and 2+ rollback trigger
conditions (not 1) — pushes output toward the depth required for gap-prioritization criteria
(C-09) and per-phase automation identification (C-10). If the rubric has aspirational criteria
for phase richness above minimum threshold, exceeding those thresholds activates them. The
single-axis test isolates whether count elevation alone, without framing change, shifts the
score above 175.
**Predicted delta if richness criteria exist above current ceiling**: 175 → 180+

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.
Current practice: [describe this team's current runbook — their shared checklist,
approval gates, and deployment sequence as practiced].
Known failure mode: [describe the recurring failure — the check or step that gets
skipped and what it costs when it does].

Before tracing any phase, write your gap table now. Four columns:
Phase | Gap | Severity (critical / moderate / low) | Why
Print the header row; leave all data rows blank. Return to fill this table only after
all four phases are complete; compare every gap against every other before assigning
Severity.

what needs to be true before we touch this?

List at least 4 pre-deploy checks (minimum for this prompt is 4, not 3). For each
check, name: (a) the specific condition being verified, (b) what failure looks like,
(c) who or what performs this check. "'Verify the environment is stable' names no
condition and does not qualify."

what's the deployment order?

List at least 6 deployment steps (minimum for this prompt is 6, not 4) in execution
order. For each step, name: (a) what the step does, (b) its inputs and outputs,
(c) its failure mode. Call out at least two ordering dependencies explicitly — each
one naming the step that must complete before the next can begin and what breaks if
it does not.

did it land?

List at least 3 post-deploy validation actions (minimum for this prompt is 3, not 2).
For each, name: (a) the probe or threshold, (b) the data source, (c) the pass
condition. "A validation that asks 'is the deployment healthy?' names no probe or
threshold and does not qualify."

what do we do if it didn't?

Define at least 2 rollback trigger conditions (not 1) — each naming the specific
metric or signal that fires the rollback. Name at least 2 undo steps in execution
order. State how to verify each rollback step completed successfully, not just that
rollback ran.

Return to the gap table above. Fill one row per phase. State what should be added or
changed — naming a gap without a remedy does not qualify. Rank gaps by deployment
risk before assigning Severity; gaps that could leave the order pipeline in an
inconsistent state are critical. Identify at least one automation hook per phase —
name what it would enforce and at what point in the lifecycle it fires.
```

---

## V-03

**Axis**: Phrasing register
**Hypothesis**: Using formal all-caps section headers (PRE-DEPLOY CHECKS, DEPLOYMENT SEQUENCE,
POST-DEPLOY VALIDATION, ROLLBACK) instead of bare interrogative questions tests whether C-21
and C-26 are surface-form criteria that activate on interrogative text *regardless of path*, or
whether they require the specific colloquial phrasing from the template path. If formal headers
deactivate C-21 and C-26 compared to V-04 (R16), that confirms C-21/C-26 are interrogative-
text-dependent even on the prose path. If formal headers leave C-21/C-26 intact, phrasing
register is not the discriminating variable.
**Predicted delta if C-21/C-26 deactivate**: 175 → 165 (regression — confirms interrogative dependency)
**Predicted delta if C-21/C-26 survive formal headers**: 175 → 175 (phrasing register is irrelevant)

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.
Current practice: [describe this team's current runbook — their shared checklist,
approval gates, and deployment sequence as practiced].
Known failure mode: [describe the recurring failure — the check or step that gets
skipped and what it costs when it does].

Before tracing any phase, write your gap table now. Four columns:
Phase | Gap | Severity (critical / moderate / low) | Why
Print the header row; leave all data rows blank. Return to fill this table only after
all four phases are complete; compare every gap against every other before assigning
Severity.

PRE-DEPLOY CHECKS

List at least 3 pre-deploy checks. For each, name the specific condition being
verified and what failure looks like. "'Verify the environment is stable' names no
condition and does not qualify."

DEPLOYMENT SEQUENCE

List at least 4 steps in execution order. Call out at least one ordering dependency
explicitly — the step that must complete before the next can begin, and what breaks
if it does not.

POST-DEPLOY VALIDATION

List at least 2 post-deploy validation actions. Each must name a probe, threshold,
or data-integrity assertion. "A validation that asks 'is the service running?' names
no probe or threshold and does not qualify."

ROLLBACK

State the rollback trigger, at least one undo step, and how to verify rollback
succeeded.

Return to the gap table above. Fill one row per phase. State what should be added or
changed — naming a gap without a remedy does not qualify. Rank gaps by deployment
risk before assigning Severity. Identify at least one automation hook in the
deployment lifecycle — name where it fires and what it would enforce.
```

---

## V-04

**Axes combined**: Inertia framing + prose structural adoption (front-loaded gap table +
interrogative phase headers)
**Hypothesis**: Layering V-01's status-quo section on top of the confirmed prose
structural-adoption architecture (V-04, R16) tests whether inertia framing compounds on the
175 ceiling. The structural-adoption path already activates C-14, C-21, C-26, C-15, C-33,
C-34. Adding a Status Quo section with named historical failure may additionally activate C-09
(gaps ranked against historical blast radius) and any inertia-specific criterion above C-34.
The key interaction risk: if the Status Quo section is parsed as apparatus (a section with
structured fields), C-15 may drop; this variation explicitly avoids colon-notation syntax in
the Status Quo section to prevent that.
**Predicted delta if inertia activates C-09 and new criterion**: 175 → 185+
**Predicted delta if no new criteria**: 175 → 175 (no regression; confirms stable ceiling)

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate.

Before tracing the deployment of {{TOPIC}}, record the current state in prose.
Describe what this team actually does today — their existing deployment sequence, the
approval gates they use in practice, and the recurring failure they have encountered.
Name the specific check or step that gets skipped and the operational cost when it
does: downtime window, order pipeline impact, or manual recovery burden. This record
is an input to the gap analysis — every gap must be compared against this failure
history before Severity is assigned.

Before tracing any phase, write your gap table now. Four columns:
Phase | Gap | Severity (critical / moderate / low) | Why
Print the header row; leave all data rows blank. Do not pre-fill. Return to fill this
table only after all four phases are complete; compare every gap against every other
and against the known failure history before assigning Severity — a gap that
contributed to a past failure is automatically critical.

what needs to be true before we touch this?

List at least 3 pre-deploy checks. For each, name the specific condition being
verified and what failure looks like. "'Verify the environment is stable' names no
condition and does not qualify." Where a check directly addresses the known failure
pattern, say so.

what's the deployment order?

List at least 4 steps in execution order. Call out at least one ordering dependency
explicitly — the step that must complete before the next can begin, and what breaks
if it does not.

did it land?

List at least 2 post-deploy validation actions. Each must name a probe, threshold,
or data-integrity assertion. "A validation that asks 'is the catalog sync current?'
names no probe or threshold and does not qualify."

what do we do if it didn't?

State the rollback trigger, at least one undo step, and how to verify rollback
succeeded. If the known failure above had no rollback path, note that as a gap.

Return to the gap table. Fill one row per phase. State what should be added or
changed — naming a gap without a remedy does not qualify. Identify at least one
automation hook in the deployment lifecycle.
```

---

## V-05

**Axes combined**: Inertia framing + lifecycle emphasis (above-minimum counts) + role vocabulary
depth (C-11 maximization)
**Hypothesis**: Three-axis compound: (1) status-quo section grounds gap severity in deployment
history (C-09 anchoring), (2) above-minimum phase counts (4+ checks, 6+ steps, 3+ validations,
2+ triggers) activate richness criteria, (3) expanded role vocabulary list (12+ domain terms in
role block) maximizes C-11. The combination probes whether any of the 45 uncracked aspirational
points are reachable by simultaneous depth, breadth, and historical grounding. This is the
maximum-ambition R17 test.
**Predicted delta if compound activates new criteria**: 175 → 185+
**Predicted delta if no new criteria**: 175 → 175 (all existing criteria already at ceiling)

```markdown
ROLE: You are a Commerce/Operations deployment domain expert.
Vocabulary: catalog sync, inventory lock, order pipeline drain, tenant provisioning,
feature flag promotion, schema migration gate, canary validation, service mesh health
probe, rollback trigger, deployment gate, blue-green cutover, circuit-breaker threshold,
idempotent migration step, deployment freeze window, environment parity gate.

Before tracing the deployment of {{TOPIC}}, record the current state in prose.
Describe what this team actually does today — their existing deployment sequence, the
approval gates they use in practice, and the recurring failure they have encountered.
Name the specific check or step that gets skipped and its operational cost: downtime
window, order pipeline impact, catalog inconsistency duration, or manual recovery
burden. Name the domain terms from the vocabulary above that apply to this
deployment — this anchors the trace vocabulary before any phase begins.

Before tracing any phase, write your gap table now. Four columns:
Phase | Gap | Severity (critical / moderate / low) | Why
Print the header row; leave all data rows blank. Do not pre-fill. Return to fill only
after all four phases are complete. Before assigning Severity, compare every gap
against every other and against the known failure history — a gap that contributed
to a past failure is automatically critical regardless of theoretical severity.

what needs to be true before we touch this?

List at least 4 pre-deploy checks (floor for this prompt is 4). For each check, name:
(a) the specific condition being verified, (b) what failure looks like, (c) who or
what performs this check, (d) whether this check addresses the known failure pattern.
"'Verify the environment is ready' names no condition and does not qualify."

what's the deployment order?

List at least 6 deployment steps (floor for this prompt is 6) in execution order.
For each step name what it does, its failure mode, and who owns it. Call out at
least two ordering dependencies explicitly — each naming the step that must complete
before the next and what breaks if it does not.

did it land?

List at least 3 post-deploy validation actions (floor for this prompt is 3). For
each, name: (a) the probe, threshold, or data-integrity assertion, (b) the data
source, (c) the pass condition and who evaluates it. "A validation that asks 'is the
service running?' names no probe or threshold and does not qualify."

what do we do if it didn't?

Define at least 2 rollback trigger conditions, each naming the specific metric or
signal that fires rollback. List at least 2 undo steps in execution order. State how
to verify each undo step completed successfully, not just that rollback ran. If the
known failure above lacked a rollback path, name that explicitly as a gap.

Return to the gap table. Fill one row per phase. State what should be added or
changed — naming a gap without a remedy does not qualify. Before assigning Severity,
rank gaps against the known failure history. Identify at least one automation hook
per phase — name the specific lifecycle point where it fires, the condition it
enforces, and whether it blocks or notifies.
```

---

## R17 discriminating questions

| Question | Test | Verdict available from |
|----------|------|------------------------|
| Does inertia framing activate new criteria above 175? | V-01, V-04, V-05 | C-09 delta + any new criterion in V-01 vs R16 V-04 |
| Does above-minimum count elevation activate richness criteria? | V-02 | V-02 vs V-04 R16 on aspirational score delta |
| Are C-21/C-26 interrogative-text-dependent or format-agnostic? | V-03 vs V-04 R16 | C-21/C-26 result in V-03 |
| Does inertia compound on the structural-adoption ceiling? | V-04 | V-04 score vs 175 |
| Does triple-axis compound break 175? | V-05 | V-05 score vs V-04 score |

**Ceiling sensitivity for R17** (if probes succeed):

| New activation | Added pts | Projected ceiling |
|---|---|---|
| C-09 reliably via inertia | +5 | 180/220 |
| Richness criteria (per-phase depth) | +5 | 180/220 |
| C-09 + richness | +10 | 185/220 |
| C-09 + richness + new inertia criterion | +15 | 190/220 |
