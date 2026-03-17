Looking at the C-17 variation analysis in the scorecard, two distinct excellence patterns emerged that aren't captured by any existing criterion:

1. **V-01 / V-04**: The pre-barrier *container name itself* encodes its positional role — "PRE-EVALUATION HEADER (before any construct evaluation begins)" — making placement verifiable from structure without reading content.
2. **V-03 / V-04 / V-05**: Both labeled directives (independence + scope extension) appear *together* in the pre-barrier section, combining C-17 + C-19 into a single structural unit.

These become C-21 and C-22. Max score: 130 → 136.

---

```markdown
# flow-throttle — Scoring Rubric v5

---

## What changed (v4 → v5)

**Two new aspirational criteria, 3 points each. Max score: 130 → 136.**

### C-21 — Pre-Barrier Container Name Encodes Positional Role
*Source: R4 V-01 / V-04 section header naming pattern*

The container holding the pre-barrier directives must **encode its positional role in its
name** — making placement self-documenting and structurally verifiable without reading
content. Pass condition: the section header, phase label, or preamble title includes a
positional qualifier (e.g., "PRE-EVALUATION," "PRE-ANALYSIS ASSERTION," or "(before any
construct evaluation begins)"). A named section whose title does not encode position does
not pass, even if its content appears before evaluative output.

### C-22 — Pre-Barrier Labeled Pair Co-location
*Source: R4 V-03 / V-04 / V-05 combined C-17+C-19 structural pattern*

The pre-barrier container must hold **both** the independence directive (C-15 mechanism,
labeled e.g. "Independence:") and the scope extension directive (C-16 mechanism, labeled
e.g. "Scope extension:"), each with a distinct named label, in the same section that
precedes all construct-by-construct evaluation. Pass condition: a single pre-barrier
section carries a labeled independence statement AND a labeled scope extension declaration,
both before the first evaluative output line. Satisfying only one labeled directive in the
pre-barrier position, or carrying both directives unlabeled, does not pass.

---

**Pass condition clarifications** (no point changes):

- **C-17**: the explicit positional announcement pattern (V-01) is sufficient but not
  required — any pre-barrier placement before evaluative output satisfies C-17. C-21
  captures the stronger self-documenting form.
- **C-22**: extends C-19 (labeled co-location) by adding the C-17 placement requirement.
  A labeled pair appearing *after* evaluative output satisfies C-19 but fails C-22.

---

## What changed (v3 → v4)

**Four new aspirational criteria, 3 points each. Max score: 118 → 130.**

### C-17 — Pre-Barrier Independence Instruction Placement
*Source: R3 V-02 single-sentence C-15 isolation*

The non-deference sentence must appear **before** the second barrier's first evaluative
output. An instruction placed inside or after barrier output was absent when the barrier
opened. Pass condition: sentence in preamble/header, before any construct-by-construct
output, naming the prior layer and asserting confidence-is-not-evidence. One sentence in
the correct position is sufficient.

### C-18 — Structural Closure Reason for Scope Extension
*Source: R3 V-03 single-axis C-16 isolation*

The scope declaration must name the **structural reason** why the first barrier's execution
window excluded those categories — not just which categories are covered. Without the
closure reason, the declaration is a preference, not a structural argument. Pass condition:
at least one closure reason (e.g., "introduced after the first barrier's window had
closed"). Naming categories without a reason does not pass.

### C-19 — Label-Enforced Co-location Independence
*Source: R3 V-04 C-15+C-16 co-location finding*

When two independent directives occupy the same block, each must carry a **distinct named
label**. Unlabeled co-location scores as one mechanism for both criteria. Labels are
structurally load-bearing, not decoration. Pass condition: a single preamble can carry both
C-15 and C-16 and score them independently when both are labeled (e.g., "Independence:" /
"Scope extension:").

### C-20 — Gate Mechanism Prose Portability
*Source: R3 V-01 gate syntax confirmation*

A gate defined in prose satisfies C-14 when it carries all three structural elements:
**(a)** name/label, **(b)** conditional prerequisite, **(c)** named block target. Format is
decorative. This criterion distinguishes conditional instructions from advisory notes:
advice can carry a label and recommendation without naming what it blocks.

---

**Pass condition updates** (no point changes):
- **C-14**: tabular structure and role separation not required — confirmed by V-01
- **C-15**: one sentence is the minimum sufficient mechanism — confirmed by V-02
- **C-16**: named populations + structural closure reason satisfies criterion alone —
  confirmed by V-03

---

## Essential Criteria (weight: 60)

### C-01 — Bottleneck Localization
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The output identifies the primary throughput bottleneck in the scenario —
  naming the specific component, PA construct, and volume condition that causes throttling
  first.
- **Pass condition**: Output names a specific system component (not a generic "the API")
  as the bottleneck and states the request volume or rate at which it saturates. Vague
  statements like "the system slows down" do not pass.

### C-02 — Rate Limit Hit Ordering
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The output establishes which rate limits are hit first, second, and so on —
  producing a ranked sequence rather than a flat list of limits.
- **Pass condition**: Output presents at least two throttle tiers in explicit order (e.g.,
  "connector-level at 600 req/min hits before tenant-level at 1200 req/min") and explains
  why that ordering holds for the scenario's request volume. An unordered list of limits
  does not pass.

### C-03 — Backpressure Propagation Trace
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The output traces how throttling at one tier propagates upstream or downstream
  — showing the causal chain from the first throttled component to the caller or downstream
  consumer.
- **Pass condition**: Output describes at least one propagation step: what signal travels
  (error code, retry-after header, queue depth, etc.), which component receives it, and
  what that component does in response. Stating only that "backpressure occurs" without a
  causal chain does not pass.

### C-04 — User Experience per Throttle Tier
- **Category**: coverage
- **Weight**: essential (12)
- **Text**: The output characterizes the user-facing experience at each identified throttle
  tier — distinguishing between transparent retry, visible delay, error surfaced to user,
  and silent data loss.
- **Pass condition**: Output maps at least two distinct throttle tiers to distinct UX
  outcomes (not the same outcome for all tiers). Each mapping must state what the user sees
  or experiences, not just what the system does internally.

### C-05 — Domain Grounding in Connectors / Power Automate
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The analysis uses terminology and limits specific to the Connectors / Power
  Automate throughput domain — not generic API rate-limiting theory.
- **Pass condition**: Output references at least one Power Automate or connector-specific
  construct (e.g., Power Platform request entitlements, connector throttling policies, flow
  run concurrency limits, action call limits, premium vs. standard connector tiers, or
  Microsoft 365 service protection limits). Generic HTTP 429 descriptions without connector
  context do not pass.

---

## Recommended Criteria (weight: 30)

### C-06 — Unprotected Burst Path Detection
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output identifies at least one path in the flow that can emit a burst of
  requests without a rate-limiting guard — e.g., an Apply to Each loop with no concurrency
  cap, a parallel branch with unbounded fan-out, or a trigger with no debounce.
- **Pass condition**: Output names a specific flow construct or pattern that creates
  unprotected burst exposure and explains why it bypasses or overwhelms the rate limit.
  Must be specific to the scenario, not a generic warning.

### C-07 — Missing Retry-After Handling
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output identifies gaps in retry-after handling — cases where a 429 response
  is received but the retry-after header value is ignored, not read, or results in a fixed
  backoff that undershoots or overshoots the required wait.
- **Pass condition**: Output names at least one specific flow construct or location where
  retry-after header duration is not honored and states the resulting failure mode (retry
  storm, fixed-backoff misalignment, or silent discard). Generic recommendations to
  implement retry-after handling without a specific gap do not pass.

### C-08 — Cascade Risk Register
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output produces a risk register identifying multi-tier cascade scenarios —
  cases where throttling at one limit triggers a secondary throttle at a downstream tier
  before recovery is possible.
- **Pass condition**: Output identifies at least two cascade pairs (tier A throttle →
  tier B throttle) with the mechanism linking them and an assessed severity. A flat list of
  independent risks without cascade relationships does not pass.

---

## Advisory Criteria (weight: 20)

### C-09 — PA-Specific Remediation Proposals
- **Category**: actionability
- **Weight**: advisory (6)
- **Text**: The output proposes mitigations using Power Automate–native constructs —
  not generic backoff advice — matched to the specific bottlenecks identified.
- **Pass condition**: Output names at least two PA-native remediation options (e.g.,
  concurrency control settings, flow run queuing, Delay action with retry-after value,
  request batching via Data Operations, premium connector entitlement upgrade) and maps
  each to a specific identified bottleneck. Generic "add retry logic" advice does not pass.

### C-10 — Monitoring and Alerting Coverage
- **Category**: operability
- **Weight**: advisory (5)
- **Text**: The output identifies what PA monitoring signals would reveal the throttle
  conditions before they become user-visible failures.
- **Pass condition**: Output names at least one PA-observable signal (e.g., flow run
  history throttle status, connector call telemetry, Power Platform admin center request
  usage dashboard) and explains what condition it surfaces. Generic "set up alerting"
  statements do not pass.

### C-11 — License and Entitlement Boundary Identification
- **Category**: coverage
- **Weight**: advisory (4)
- **Text**: The output identifies where license tier or entitlement type changes the
  throttle ceiling — distinguishing behavior under per-user, per-flow, and environment-
  level entitlement models.
- **Pass condition**: Output names at least one entitlement boundary where the throttle
  limit materially differs (e.g., Office 365 E3 vs. Power Apps per-user plan request
  entitlements) and explains the impact on the scenario's volume. Entitlement-neutral
  analysis does not pass.

### C-12 — Throttle Budget Projection
- **Category**: depth
- **Weight**: advisory (3)
- **Text**: The output projects the throttle budget consumed at the scenario's expected
  request volume — showing headroom or deficit against each identified limit.
- **Pass condition**: Output calculates or estimates request consumption against at least
  one limit (e.g., "500 records × 3 connector calls = 1,500 req, against a 600 req/min
  connector limit → saturates in 24 seconds") and states whether headroom exists. A
  qualitative "this will hit the limit" without a numeric projection does not pass.

### C-13 — Test and Validation Approach
- **Category**: operability
- **Weight**: advisory (2)
- **Text**: The output proposes a method to validate the throttle analysis before
  production deployment — specifying how the identified limits and cascade paths can be
  exercised in a test environment.
- **Pass condition**: Output describes at least one concrete test step using PA tooling
  (e.g., run flow with synthetic volume in dev environment, inject throttle error via
  mock connector, observe run history for 429 patterns). "Test in staging" without a
  specific method does not pass.

---

## Structural Criteria (weight: 8)

### C-14 — Gate Mechanism
- **Category**: structure
- **Weight**: structural (4)
- **Text**: The output uses an explicit gate to block progression to a second evaluation
  layer until named conditions in the first layer are satisfied.
- **Pass condition**: Output names a gate (labeled "GATE N:" or equivalent), states the
  conditional prerequisite (what must be true to proceed), and names the target block that
  is blocked until the gate passes. A gate may be expressed in prose — tabular or role-
  structured format is not required (confirmed C-20). Advisory notes carrying a label and
  a recommendation without naming a blocked target do not satisfy this criterion.

### C-15 — Non-Deference Sentence
- **Category**: structure
- **Weight**: structural (2)
- **Text**: The second evaluation barrier opens with an explicit statement that the first
  barrier's confidence does not substitute for the second barrier's independent precision
  check.
- **Pass condition**: Output contains one sentence asserting that the first layer's
  results (confidence, completeness, or score) are not evidence of the second layer's
  precision. The sentence must name the prior layer. One sentence is the minimum sufficient
  mechanism (confirmed C-17). The sentence must appear before any construct-by-construct
  output in the second barrier (confirmed C-17).

### C-16 — Scope Extension Declaration
- **Category**: structure
- **Weight**: structural (2)
- **Text**: The second barrier declares which construct populations were excluded from the
  first barrier's execution window and why — providing a structural reason for the
  extension, not merely a category enumeration.
- **Pass condition**: Output names at least one construct population excluded from the
  first barrier and states the structural reason for the exclusion (e.g., "introduced
  after the first barrier's window had closed"). Naming populations without a closure
  reason does not pass (confirmed C-18).

---

## Aspirational Criteria — v4 (weight: 12)

### C-17 — Pre-Barrier Independence Instruction Placement
- **Category**: structure
- **Weight**: aspirational (3)
- **Text**: The non-deference sentence (C-15) appears before the second barrier's first
  evaluative output — not inside or after construct-by-construct analysis.
- **Pass condition**: Sentence appears in preamble or header, before any construct-level
  evaluation line, naming the prior layer and asserting confidence-is-not-evidence.
  One correctly placed sentence is sufficient.

### C-18 — Structural Closure Reason for Scope Extension
- **Category**: structure
- **Weight**: aspirational (3)
- **Text**: The scope extension declaration (C-16) names the structural reason why the
  first barrier's execution window excluded the declared categories — not just which
  categories are covered.
- **Pass condition**: At least one closure reason stated (e.g., "introduced after the
  first barrier's window had closed"). Naming categories without a reason does not pass.

### C-19 — Label-Enforced Co-location Independence
- **Category**: structure
- **Weight**: aspirational (3)
- **Text**: When the C-15 and C-16 directives occupy the same block, each carries a
  distinct named label — making them independently scorable despite physical co-location.
- **Pass condition**: Each directive in the shared block has a label (e.g.,
  "Independence:" and "Scope extension:"). Unlabeled co-location scores as one mechanism
  for both criteria.

### C-20 — Gate Mechanism Prose Portability
- **Category**: structure
- **Weight**: aspirational (3)
- **Text**: A gate defined in prose (not a table or structured template) satisfies C-14
  when it carries all three structural elements: (a) name/label, (b) conditional
  prerequisite, (c) named block target.
- **Pass condition**: Prose gate names itself, states what must be true to proceed, and
  names the section or output that is blocked. Advisory notes carrying only a label and
  a recommendation without a named block target do not pass.

---

## Aspirational Criteria — v5 (weight: 6)

### C-21 — Pre-Barrier Container Name Encodes Positional Role
- **Category**: structure
- **Weight**: aspirational (3)
- **Text**: The container holding the pre-barrier directives encodes its positional role
  in its name — making pre-barrier placement self-documenting and structurally verifiable
  without reading content.
- **Pass condition**: Section header, phase label, or preamble title includes a positional
  qualifier such as "PRE-EVALUATION," "PRE-ANALYSIS ASSERTION," or "(before any construct
  evaluation begins)." A named section whose title does not encode positional role does
  not pass, even if its content precedes evaluative output.

### C-22 — Pre-Barrier Labeled Pair Co-location
- **Category**: structure
- **Weight**: aspirational (3)
- **Text**: The pre-barrier container holds both the C-15 mechanism (labeled) and the
  C-16 mechanism (labeled) in the same section that precedes all construct-by-construct
  evaluation — satisfying C-17 and C-19 simultaneously as a single structural unit.
- **Pass condition**: A single pre-barrier section carries a labeled independence
  statement AND a labeled scope extension declaration, both before the first evaluative
  output line. Satisfying only one labeled directive in pre-barrier position, or carrying
  both directives unlabeled, does not pass.

---

## Score Summary

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 – C-05 | 60 |
| Recommended | C-06 – C-08 | 30 |
| Advisory | C-09 – C-13 | 20 |
| Structural | C-14 – C-16 | 8 |
| Aspirational v4 | C-17 – C-20 | 12 |
| Aspirational v5 | C-21 – C-22 | 6 |
| **Total** | | **136** |
```
