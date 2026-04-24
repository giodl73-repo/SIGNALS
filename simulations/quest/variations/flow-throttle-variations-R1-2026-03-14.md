Written to `simulations/quest/variations/flow-throttle-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — Summary

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Pre-printed tier table + backpressure chain + UX mapping table; C-01/C-02/C-03/C-04 enforced by column structure |
| **V-02** | Phrasing register | 10 numbered imperative steps, each commanding exactly one criterion's output |
| **V-03** | Lifecycle emphasis | Four gated phases (SETUP → SIMULATE → FAILURE ANALYSIS → REMEDIATION); C-06/C-07/C-08 each get a named sub-section with a gate |
| **V-04** | Role sequence | Connectors expert runs ROLES 1.1–1.5; PA expert validates PA constructs, maps UX, assesses Retry-After (ROLE 2) |
| **V-05** | Full synthesis | All axes: phase gates + pre-printed tables + imperative rules + role sequence + inertia framing |

---

**Key design decisions:**

- **C-01/C-02 (bottleneck + ordering)** — The pre-printed `Hit order` column in V-01/V-03/V-05 makes an unordered list structurally impossible. V-02 relies on the "ordered list" imperative; V-04 relies on the Connectors expert's natural tier sequencing. Column enforcement is the stronger bet.

- **C-05 (PA domain grounding)** — V-04 and V-05 are the only variations with a two-pass PA construct validation (ROLE 2.1 / PHASE 4A). This makes C-05 a structural second check rather than a one-shot rule header. Open question: does the validation pass produce better PA terminology than a strong domain rule?

- **C-08 (cascade) gating** — In V-03/V-05, the cascade lives at sub-section 3C inside a gated FAILURE ANALYSIS phase, forcing it before remediation. Strongest structural guarantee of any variation.

- **Inertia framing** (V-05 only) — "The naive assumption: each rate limit is independent, built-in retries keep the system safe. Find where that assumption breaks." Design bet that belief-disproving framing drives cascade + retry-after analysis more naturally than explicit rules. Untested — open question for R1 scoring.

**Predicted V-golden:** V-05. Every criterion has a structural home. **V-03** is the closest single-mechanism competitor; **V-04** is the wildcard on C-05/C-10 depth.
ntime behavior. Open question: does
  the two-role structure produce richer cascade analysis?
- **Inertia framing** (V-05 only): "The naive assumption you are testing: each rate limit is
  independent, and built-in retries keep the system safe. Find where that assumption breaks."
  This is a design bet — positioning the prompt as disproving a status-quo belief may push the
  model toward cascade and retry-after analysis without explicit rules.

**Predicted V-golden:** V-05. Every criterion has a structural home. V-03 is closest competitor —
phase gates enforce C-06/C-07/C-08 but lack the two-role PA validation for C-05 and the
inertia framing that drives cascade analysis.

---

## V-01: Pre-Printed Tier Table

**Axis:** Output format — the core output is a set of pre-printed tables with named columns. The
model fills in rows rather than writing prose. Column headers for Hit Order, Component, PA
construct, Limit, Volume, and Margin are the structural mechanism for C-01, C-02, C-09.
**Hypothesis:** A pre-printed tier table with a mandatory "Hit order" column makes C-02 (ordered
sequence) mechanically unavoidable — an unordered list cannot satisfy a table with an ordering
column. The required "Bottleneck statement:" sentence template forces C-01 (named component +
volume). Pre-printed UX table forces C-04. Tests whether format alone is sufficient for all 5
essentials without explicit phase gates or role sequence.

```
You are running /flow:throttle.

Inputs:
  Topic:     {topic}
  Consumers: {consumers}  [list of flow/connector/plugin names and call rates, or ask the user]

Role: Connectors / Power Automate throughput domain expert.

Domain rule: Every rate limit cited must name a specific Power Automate or connector construct
(Power Platform request entitlement, connector throttling policy, flow run concurrency limit,
action call limit, Microsoft 365 service protection limit). Generic "API rate limits" without
PA-specific naming do not satisfy this requirement.

---

### CONSUMER INVENTORY

Fill in one row per consumer. Include only PA-identified consumers (flows, connectors, plugins,
Power Automate triggers).

| Consumer | Type | Call rate (req/min) | Concurrency | Retry config | Service principal |
|----------|------|---------------------|-------------|--------------|-------------------|
| [name]   | [cloud flow / standard connector / custom connector / plugin / trigger] | [N req/min] | [N concurrent / unbounded] | [retries=N, backoff=fixed/exponential, reads Retry-After=yes/no] | [dedicated / shared with: name] |
(Add rows for each consumer.)

---

### THROTTLE TIER TABLE

List every applicable rate limit tier in the order they saturate under this scenario's aggregate
request volume. Row 1 must be the bottleneck — the tier that reaches 100% utilization first.

| Hit order | Tier | Component | PA construct (exact name) | Limit | Your volume | Margin | First hit at |
|-----------|------|-----------|--------------------------|-------|-------------|--------|--------------|
| 1 (bottleneck) | [connector / user / tenant / org] | [specific named component -- not "the API"] | [e.g., "Standard connector: 500 req/min per connection"] | [N/unit-time] | [N/unit-time] | [+N% headroom / -N% over] | [minute N / record N] |
| 2 | ... | ... | ... | ... | ... | ... | ... |
(Add rows for each additional tier.)

Bottleneck statement:
  "[Specific component] at [PA construct: exact name and limit] is the binding bottleneck.
   It saturates at [N req/unit-time] under this scenario because [reason the hit ordering holds]."

---

### BACKPRESSURE PROPAGATION CHAIN

Trace the signal path from the bottleneck to the caller or downstream consumer.
Fill one row per propagation hop.

| Hop | From component | Signal emitted | Signal type | To component | Receiver response |
|-----|---------------|----------------|-------------|--------------|-------------------|
| 1   | [bottleneck]  | [HTTP 429 / Retry-After: N / queue depth increase / event / ...] | [error code / header / queue event / backpressure] | [connector runtime / PA scheduler / calling flow / end user] | [queues retry in Ns / fails run / propagates to caller / exponential backoff / ...] |
| 2   | [next component] | ... | ... | ... | ... |
(Continue until the chain reaches the end user or a terminal state.)

---

### USER EXPERIENCE PER THROTTLE TIER

Map each throttle tier from the TIER TABLE to a distinct user-facing outcome.
Do not assign the same UX category to more than one tier.

| Throttle tier | Trigger condition | What the user sees or experiences | UX category |
|---------------|-------------------|------------------------------------|-------------|
| Tier 1 (bottleneck) | [when this tier hits] | [run delayed N min in history / error message: "..." displayed in flow / silent -- user never notified / data record silently dropped] | [transparent retry / visible delay / error surfaced / silent data loss] |
| Tier 2 | ... | [must differ from Tier 1] | [different category from Tier 1] |
(Add rows for each tier. Same category on two rows does not satisfy C-04.)

---

### BURST PATH INVENTORY

Identify flow constructs that emit a burst of requests without a rate-limiting guard.
Common patterns: Apply to Each with Concurrency Control=Off, parallel branches with unbounded
fan-out, a high-frequency trigger with no debounce.

Burst path [N]:
  Construct:   [specific PA construct -- e.g., "Apply to Each, Concurrency Control=Off"]
  Location:    [where in the flow this occurs]
  Peak rate:   [estimated N req/min this construct can emit at maximum]
  Exposure:    [why this construct bypasses or overwhelms the tier-1 rate limit]

If no burst paths exist: "No unguarded burst paths identified. Guards in place: [list PA
concurrency controls configured and their settings]."

---

### RETRY-AFTER HANDLING GAPS

For each consumer that can receive a 429 in this scenario, assess Retry-After handling.

| Consumer | Action / connector call | Retry-After received? | Behavior | Consequence |
|----------|------------------------|-----------------------|----------|-------------|
| [name]   | [specific action name] | [yes / no -- N/A, call never throttled] | [reads + respects header / fixed Ns backoff ignoring header / immediate retry / not implemented] | [correct / hammering / premature retry at wrong interval / outage extension] |
(Add rows for each consumer.)

---

### CASCADE FAILURE CHAIN

Identify at least one scenario where throttling at tier 1 causes tier 2 to also throttle.

Cascade [N]:
  Tier 1 throttles: [specific component]
  Causal link:      [how tier-1 throttling increases load on tier-2 component -- e.g.,
                    "retry storm from [consumer] adds [N] req/min to [component], which
                    then hits its [PA construct] limit of [N/unit]"]
  Load added:       [N additional req/min reaching tier-2 component]
  Tier 2 throttles: [specific component]
  Failure mode:     [brownout / full stop / partial data / oscillation]

---

### QUANTIFIED RISK SUMMARY

State whether this scenario is safe, marginal (within 20% of limit), or over-limit per tier.

| Tier | Limit | Projected volume | Status | Headroom / deficit |
|------|-------|-----------------|--------|--------------------|
| Tier 1 (bottleneck) | [N/unit] | [N/unit] | [SAFE / MARGINAL / OVER-LIMIT] | [+N% remaining / -N% over] |
(Add rows for all tiers.)

---

### PA-SPECIFIC REMEDIATIONS

Provide at least two distinct remediations. Each must name a specific Power Automate feature
or setting. "Add retries" and "reduce load" do not count.

Remediation [N]:
  Problem addressed: [reference: Burst path N / Cascade N / Retry-After gap for [consumer] /
                     Tier N over-limit -- be specific]
  PA feature:        [exact feature name: e.g., "Apply to Each > Concurrency Control (set to N)",
                     "Service principal pooling (N additional principals)",
                     "Flow run queue -- max concurrent runs: N",
                     "Premium connector entitlement upgrade",
                     "Scheduled trigger: distribute across [time window] using run offset"]
  Configuration:     [what the developer sets and what effect it has on the identified problem]

---

Write artifact: simulations/flow/throttle/{topic}-throttle-{date}.md
Frontmatter: skill, topic, date, consumer_count, tier_count, bottleneck_component,
             burst_path_count, retry_after_gap_count, cascade_count,
             over_limit_tier_count, remediation_count.
```

---

## V-02: Imperative / Direct Register

**Axis:** Phrasing register — all instructions written as direct commands in numbered steps.
Each step commands exactly one criterion's output. Short sentences, no prose explanations of
why each step matters.
**Hypothesis:** Imperative phrasing keeps the model in execution mode rather than meta-commentary
mode. When the instruction says "Name the component. State the request volume." rather than
"the output must identify a specific component and state the request volume," the action is
closer to the surface. Tests whether register change alone improves C-01/C-02/C-05 compliance
without pre-printed table columns or phase gates.

```
You are running /flow:throttle.

Topic:     {topic}
Consumers: {consumers}

Role: Connectors / Power Automate throughput domain expert.

Before you start: Every rate limit you name must reference a specific PA construct --
Power Platform request entitlements, connector throttling policies, flow run concurrency
limits, action call limits, Microsoft 365 service protection limits. Do not say "the API."
Name the tier.

---

Step 1: Inventory your consumers.

List every flow, connector, plugin, or scheduled trigger that calls an API in this scenario.
For each one, write:
  - Name: [consumer name]
  - Type: [cloud flow / standard connector / custom connector / plugin / PA trigger]
  - Call rate: [N requests per minute, or N records per batch at N concurrent]
  - Retry config: [retries=N, backoff=fixed/exponential, reads Retry-After header=yes/no]
  - Service principal: [dedicated / shared with: name]

Step 2: State the aggregate volume.

Add up the peak request rate across all consumers. Write: "Aggregate peak: [N req/min]."

Step 3: Find the bottleneck.

List the applicable rate limit tiers from lowest threshold to highest. State which one your
aggregate volume hits first. Write exactly:
  "[Specific component name] at [PA construct: exact name and limit] is the binding bottleneck.
   It saturates at [N req/unit-time] because [one sentence: why this tier hits before the others]."
Do not say "the system slows down." Do not say "the API." Name the component.

Step 4: Order all the tiers.

List each throttle tier in the sequence it is reached -- bottleneck first. For each:
  - Tier N: [component name] -- [PA construct] -- limit: [N/unit] -- volume: [N/unit]
    -- hits at: [minute N / record N] -- why before next tier: [one sentence]

Step 5: Trace the backpressure.

Start at the bottleneck. For each propagation hop, write:
  - [Component A] emits [signal: HTTP 429 / Retry-After: N sec / queue overflow / event]
  - [Component B] receives it and responds by: [retry in Ns / fail run / propagate / ...]
Continue until you reach the end user or a terminal state.

Step 6: Map what the user experiences.

For each throttle tier from Step 4, write what the user actually sees or experiences.
Not what the system does internally -- what the user's experience is.
  - Tier 1: [transparent retry (user sees nothing) / run delayed N min visible in history /
             error message: "..." displayed / silent data loss -- record dropped]
  - Tier 2: [must differ from Tier 1]
  - (continue for each tier)

Step 7: Find burst paths.

Look for flow constructs that emit bursts with no rate-limiting guard:
  - Apply to Each with Concurrency Control=Off
  - Parallel branches with unbounded fan-out
  - High-frequency trigger with no debounce
  - Other unbounded loops or fan-outs

For each burst path found: name the construct, estimate its peak request rate, explain why
it overwhelms the tier-1 limit.
If none exist: say so and list the concurrency guards currently in place.

Step 8: Check Retry-After handling.

For each consumer that can receive a 429: does it read and respect the Retry-After header?
  - [Consumer] / [action or connector]: [reads + respects / fixed Ns backoff ignoring header /
    immediate retry / not implemented]
  - If Retry-After is ignored or absent: name the consequence (hammering / premature retry /
    extended outage).

Step 9: Find the cascade.

Name at least one scenario where tier-1 throttling causes tier-2 to also throttle.
Write:
  - Tier 1 throttles: [component]
  - This causes: [N additional req/min] to reach [tier-2 component] because [retry storm /
    fan-out / fixed-interval hammering / ...]
  - Tier 2 throttles: [component]
  - Result: [brownout / full stop / partial data / oscillation]

Step 10: Quantify the risk and remediate.

For each tier, write: [Tier N]: limit=[N/unit], projected=[N/unit], status=[SAFE / MARGINAL /
OVER-LIMIT].

Then give at least two remediations using specific Power Automate features or settings.
"Add retries" and "reduce load" do not count.
  - Remediation 1: [PA feature exact name] -- addresses [burst path / cascade / retry gap /
    over-limit tier] -- configure: [what to set and to what value]
  - Remediation 2: [different PA feature] -- addresses [different finding] -- configure: [...]

---

Write artifact: simulations/flow/throttle/{topic}-throttle-{date}.md
Frontmatter: skill, topic, date, consumer_count, tier_count, bottleneck_component,
             burst_path_count, retry_after_gap_count, cascade_count, over_limit_tier_count.
```

---

## V-03: Explicit Gated Phases

**Axis:** Lifecycle emphasis — the skill is divided into four named, gated phases. Each phase
must produce a declared output before the next begins. The gate structure makes the lifecycle
explicit and prevents phases from collapsing (e.g., remediation appearing before cascade is
traced, or UX mapping skipped because the simulation moved straight to findings).
**Hypothesis:** Explicit phase gates improve C-06/C-07/C-08 coverage by giving each a named
sub-section inside a gated FAILURE ANALYSIS phase, forcing all three before remediation. A
REMEDIATION phase with a required PA-feature column enforces C-10. Tests whether lifecycle
structure alone — without pre-printed table templates or role sequence — drives coverage of
all recommended and aspirational criteria.

```
You are running /flow:throttle.
All phase headers are fixed. Every gate must fire before the next phase begins.
Do not reorder, rename, or remove any phase header or sub-section.

Topic:     {topic}
Consumers: {consumers}

Role: Connectors / Power Automate throughput domain expert.

Domain rule: Every rate limit cited must name a specific Power Automate or connector construct
(Power Platform request entitlement, connector throttling policy, flow run concurrency limit,
action call limit, Microsoft 365 service protection limit). "The API" or "the service" without
a named PA construct does not satisfy this requirement.

---

## PHASE 1: SCENARIO SETUP
[Define consumers and applicable limits before simulating anything.]

Consumer inventory:
  | Consumer | Type | Call rate (req/min) | Concurrency | Retry config | Service principal |
  |----------|------|---------------------|-------------|--------------|-------------------|
  | [name]   | [cloud flow / connector / plugin] | [N/min] | [N / unbounded] | [retries=N, backoff=type, reads Retry-After=yes/no] | [dedicated / shared with: ...] |
  (Add rows for each consumer.)

Applicable PA rate limit tiers:
  | Tier | Component | PA construct (exact name) | Limit |
  |------|-----------|--------------------------|-------|
  | connector | [...] | [e.g., "Standard connector throttling: 500 req/min per connection"] | [N/min] |
  | user | [...] | [e.g., "Power Platform request entitlement -- Per User Plan: 40,000 req/day"] | [N/day] |
  | tenant | [...] | [...] | [...] |
  (List all tiers applicable to this scenario.)

Aggregate peak volume: [total req/min across all consumers at peak load]

GATE 1: Consumer inventory filled. Each PA tier row has an exact PA construct name.
        Aggregate peak volume stated. Proceed to PHASE 2 only after this gate is met.

---

## PHASE 2: THROTTLE SIMULATION
[Run the simulation. Do not advance to PHASE 3 until all three sub-sections are complete.]

### 2A — Rate Limit Hit Ordering

Rank the tiers by the order they saturate under the aggregate volume from PHASE 1.
Row 1 is the bottleneck — the tier that reaches its limit first.

  | Hit order | Tier | Component | PA construct | Limit | Projected volume | First hit at | Why this order |
  |-----------|------|-----------|-------------|-------|-----------------|-------------|----------------|
  | 1 (bottleneck) | [...] | [specific component -- not "the API"] | [...] | [N/unit] | [N/unit] | [min N / record N] | [one sentence] |
  | 2 | ... | ... | ... | ... | ... | ... | ... |
  (Add rows for each tier from PHASE 1.)

  Bottleneck statement: "[Specific component] at [PA construct] is the binding bottleneck.
  It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
  for this aggregate volume]."

### 2B — Backpressure Propagation Trace

Starting from the bottleneck, trace the signal path to the caller or downstream consumer.

  Hop 1: [Bottleneck component] emits [HTTP 429 / Retry-After: N / queue overflow / ...]
         -> received by [connector runtime / PA scheduler / calling flow / end user / ...]
         -> response: [retry queued at T+Ns / run failed / error propagated / ...]
  Hop 2: [next component] -> ...
  (Continue until you reach the end user or a terminal state.)

### 2C — User Experience per Throttle Tier

Map each tier from 2A to a user-facing outcome. Outcomes must differ across tiers.

  | Throttle tier | What the user sees or experiences | UX category |
  |---------------|-----------------------------------|-------------|
  | Tier 1 (bottleneck) | [transparent retry -- user unaware / run delayed N min in history / error "..." displayed / silent data loss] | [transparent retry / visible delay / error surfaced / silent data loss] |
  | Tier 2 | [different from Tier 1] | [different category] |
  (Add rows for each tier. Repeating the same UX category across two rows does not pass.)

GATE 2: Hit ordering with bottleneck statement, backpressure trace (at least one hop), and
        UX mapping (at least two tiers with distinct UX categories) are all complete.
        Proceed to PHASE 3 only after this gate is met.

---

## PHASE 3: FAILURE ANALYSIS
[Identify the failure modes produced by the throttle simulation. All three sub-sections
 must be complete before proceeding to PHASE 4.]

### 3A — Unprotected Burst Paths

Identify flow constructs that can emit a burst of requests without a rate-limiting guard.

  Burst path [N]:
    Construct:  [specific PA construct -- e.g., "Apply to Each, Concurrency Control=Off"]
    Peak rate:  [estimated N req/min this construct emits at maximum throughput]
    Exposure:   [why this construct bypasses or overwhelms the tier-1 rate limit]

  If none: "No unguarded burst paths found. Guards active: [list PA concurrency controls
  in use and their configured values]."

### 3B — Missing Retry-After Handling

For each consumer that can receive a 429 in this scenario:

  | Consumer | Action / connector call | Retry-After behavior | Consequence |
  |----------|------------------------|---------------------|-------------|
  | [name]   | [specific action name] | [reads + respects header / fixed Ns backoff (ignores header) / immediate retry / not configured] | [correct / hammering / premature retry at wrong interval / outage extension] |
  (Add rows for each consumer. If all handle Retry-After correctly, say so.)

### 3C — Cascade Failure Chain

Identify at least one cascade where tier-1 throttling causes tier-2 to also throttle.

  Cascade [N]:
    Tier 1 throttles: [specific component]
    Causal link:      [how tier-1 throttling increases load on tier-2 -- be specific:
                      "retry storm from [consumer] adds [N] req/min to [component], which
                       then hits its [PA construct] limit of [N/unit]"]
    Load added:       [N additional req/min to tier-2 component]
    Tier 2 throttles: [specific component]
    Failure mode:     [brownout / full stop / partial data / oscillation]
    Duration:         [self-resolving in N min / requires manual intervention / indefinite]

  (Add Cascade [2], etc. if additional cascades exist.)

GATE 3: At least one burst path (or explicit "none" with guards listed), all consumers present
        in Retry-After table, at least one cascade chain documented. Proceed to PHASE 4.

---

## PHASE 4: REMEDIATION
[Write after GATE 3. Reference specific findings from PHASES 2-3 by their labels.]

### 4A — Quantified Risk Register

  | Tier | Limit | Projected volume | Status | Headroom / deficit |
  |------|-------|-----------------|--------|-------------------|
  | Tier 1 (bottleneck) | [N/unit] | [N/unit] | [SAFE / MARGINAL (<20% headroom) / OVER-LIMIT] | [+N% / -N% over] |
  (All tiers from PHASE 2 must appear here.)

### 4B — PA-Specific Remediations

At least two remediations. Each must name a specific PA feature or setting.
"Add retries" and "reduce load" do not count. Name the feature.

  Remediation [N]:
    Finding addressed: [Burst path N / Cascade N / Retry-After gap for [consumer] / Tier N OVER-LIMIT]
    PA feature:        [exact feature name: e.g., "Apply to Each > Concurrency Control (set to N)",
                       "Service principal pooling (add N dedicated principals)",
                       "Flow run queue -- max concurrent runs setting",
                       "Premium connector entitlement upgrade for [consumer]",
                       "Scheduled trigger: distribute runs using time-based offset across [window]"]
    Configuration:     [what the developer configures and what it changes about the finding]

---

Write artifact: simulations/flow/throttle/{topic}-throttle-{date}.md
Frontmatter: skill, topic, date, consumer_count, tier_count, bottleneck_component,
             burst_path_count, retry_after_gap_count, cascade_count,
             over_limit_tier_count, remediation_count.
```

---

## V-04: Role Sequence — Connectors Expert Then PA Expert

**Axis:** Role sequence — the Connectors throughput expert runs the full simulation (throttle
tiers, backpressure, burst paths, cascades); the Power Automate domain expert then validates
PA-specific constructs, maps UX, assesses Retry-After from the PA runtime perspective, and
produces PA-specific remediations. The role handoff is the structural mechanism.
**Hypothesis:** A two-role handoff forces C-05 (domain grounding) as a second-pass validation:
the PA expert's sole job is to confirm or correct the PA-specific terminology the Connectors
expert used. This makes C-05 a structural gate rather than a stylistic requirement. The PA
expert's UX section (ROLE 2.2) also forces C-04 by giving it a dedicated role scope. Tests
whether role sequence produces richer PA-specific grounding than a single-role prompt.

```
You are running /flow:throttle with a two-role analysis sequence.
Complete ROLE 1 fully before starting ROLE 2. Do not merge the roles.

Topic:     {topic}
Consumers: {consumers}

---

## ROLE 1: CONNECTORS THROUGHPUT EXPERT

Your job: Simulate the throttle behavior from the connector runtime perspective.
Trace request volumes, identify the binding bottleneck, rank the throttle tiers,
trace backpressure, detect burst paths, and find cascade chains.

### 1.1 — Consumer Profile

For each consumer in the scenario:
  Consumer:        [name]
  Type:            [cloud flow / standard connector / custom connector / plugin / PA trigger]
  Call rate:       [N req/min or N records per batch at N concurrent threads]
  Retry config:    [retries=N, backoff=fixed/exponential, reads Retry-After header=yes/no]
  Service account: [dedicated / shared with: name of other consumers on same principal]

Total aggregate peak rate: [N req/min across all consumers]

### 1.2 — Rate Limit Tier Ranking

List applicable throttle tiers in the order they saturate under the aggregate rate above.
For each tier, state the limit, the volume hitting that tier, and why it hits before the next.

  Tier 1 (bottleneck): [component] -- limit: [N/unit] -- volume: [N/unit] -- first hit: [min N]
    Reason first: [one sentence]
  Tier 2: [component] -- limit: [N/unit] -- volume: [N/unit] -- hits at: [min N after tier 1]
    Reason after Tier 1: [one sentence]
  (Add tiers as applicable.)

  Bottleneck declaration: "[Specific component name] saturates first under this scenario at
  [N req/unit]. It is the binding constraint because [reason]."

### 1.3 — Backpressure Propagation Trace

From the bottleneck, trace the signal path upstream or downstream:
  Hop 1: [Bottleneck component] emits [HTTP 429 / Retry-After: N / queue overflow / ...]
         -> [Receiving component] responds by: [retry in Ns / fail the run / propagate error / ...]
  Hop 2: ...
  (Continue until terminal state or end user.)

### 1.4 — Burst Path Detection

Assess each of these connector / flow patterns for unguarded burst exposure:
  - Apply to Each with Concurrency Control: [Off -- BURST RISK / On (N) -- guarded / not present]
  - Parallel branches with unbounded fan-out: [present -- BURST RISK / not present]
  - High-frequency trigger with no debounce: [present -- BURST RISK / not present]
  - Other loops or fan-outs: [describe]

For each burst risk found:
  Construct: [exact PA construct name]
  Peak rate: [estimated N req/min at maximum]
  Exposure:  [why it bypasses or overwhelms the tier-1 limit]

### 1.5 — Cascade Chain

Identify at least one cascade where tier-1 throttling causes tier-2 to also throttle:
  Tier 1 throttles -> [causal mechanism: retry storm adds N req/min / fan-out compounds / ...]
  -> [Tier-2 component] also throttles.
  Failure mode: [brownout / full stop / partial data / oscillation]

---

## ROLE 2: POWER AUTOMATE DOMAIN EXPERT

Your job: Validate and augment ROLE 1 with Power Automate-specific constructs. For each
section below, confirm or correct what ROLE 1 produced, using exact PA terminology.

### 2.1 — PA Construct Validation

Review each consumer and tier from ROLE 1. For each, confirm the exact PA-specific construct
name and limit, or correct it:

  | Item from ROLE 1 | PA construct (exact name) | Correct limit | Confirmed / corrected |
  |------------------|--------------------------|---------------|----------------------|
  | [tier or consumer from 1.2 / 1.1] | [e.g., "Power Platform request entitlement -- Per User Plan: 40,000 req/day" / "Standard connector throttling: 500 req/min per connection" / "Flow run concurrency: 100 concurrent runs per flow"] | [N/unit-time] | [confirmed / corrected -- ROLE 1 said: "..." should be: "..."] |
  (Add a row for each tier and consumer from ROLE 1.)

### 2.2 — User Experience per Throttle Tier

For each throttle tier from ROLE 1.2, state what the Power Automate user actually experiences
when that tier is hit. Distinguish what the system does from what the user sees.

  | Throttle tier | PA runtime behavior | User-visible experience | UX category |
  |---------------|--------------------|-----------------------|-------------|
  | Tier 1 (bottleneck) | [PA engine behavior: throttles connector / queues flow run / marks run Failed / ...] | [run delayed N min (visible in run history) / error "..." in flow run details / user sees no indication / record silently dropped] | [transparent retry / visible delay / error surfaced / silent data loss] |
  | Tier 2 | [different PA behavior from Tier 1] | [different UX from Tier 1] | [different UX category] |
  (Add rows for each tier. UX categories must differ across rows.)

### 2.3 — Retry-After Handling Assessment (PA Runtime View)

For each consumer from ROLE 1.1, assess PA runtime behavior on a 429 response:

  | Consumer / connector | PA retry mechanism | Retry-After header behavior | Gap |
  |---------------------|-------------------|---------------------------|-----|
  | [name] | [built-in connector retry policy / custom retry in flow / no retry configured] | [reads header and waits the stated interval / uses fixed Ns backoff regardless of header / retries immediately / does not retry] | [none / hammering / premature retry / outage extension -- explain] |
  (Add rows for all consumers that can receive a 429.)

### 2.4 — PA-Specific Remediations

Provide at least two remediations using specific Power Automate features or settings.
Do not give generic advice. Name the PA feature and the specific configuration.

  Remediation 1:
    Finding addressed: [specific finding from ROLE 1 -- burst path / cascade / retry gap / over-limit tier]
    PA feature:  [exact name: e.g., "Apply to Each > Concurrency Control (Degree of Parallelism=N)",
                 "Service principal pooling -- distribute consumers across N dedicated principals",
                 "Flow run queue -- configure max queued runs to N",
                 "Premium connector entitlement upgrade for [consumer]",
                 "Scheduled trigger: stagger run times using N-minute offsets across [time window]"]
    Configuration: [exact setting the developer changes and what it does to the finding]

  Remediation 2:
    Finding addressed: [different finding from Remediation 1]
    PA feature:  [different PA feature from Remediation 1]
    Configuration: [exact setting and effect]

---

Write artifact: simulations/flow/throttle/{topic}-throttle-{date}.md
Frontmatter: skill, topic, date, consumer_count, tier_count, bottleneck_component,
             burst_path_count, cascade_count, retry_after_gap_count, remediation_count.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Pre-printed tables (V-01) + explicit phase gates (V-03) + imperative rule header
(V-02 register) + two-role sequence (V-04) + inertia framing
**Hypothesis:** Maximum structural coverage prevents omission of any criterion. Pre-printed
tables with named columns enforce C-01/C-02/C-09 (tier ordering and volume numbers cannot be
omitted from columns). Phase gates enforce C-06/C-07/C-08 by giving each a named sub-section
before the next gate fires. The PA expert role validates C-05 as a second pass. The inertia
framing -- "the naive assumption is that each rate limit is independent and built-in retries
keep the system safe" -- positions the prompt as disproving a status-quo belief, which is a
design bet that it drives cascade and retry-after analysis more naturally than explicit rules.
No surface where any criterion should appear is left to model discretion.

```
You are running /flow:throttle.

Rules first:
  1. Every rate limit must name a specific PA construct. Do not say "the API" or "the service."
     Name the tier: Power Platform request entitlement / connector throttling policy /
     flow run concurrency limit / action call limit / Microsoft 365 service protection limit.
  2. Fill in every pre-printed field and table column. Do not skip, rename, or remove any
     field, row header, or section header.
  3. Every phase gate must fire before the next phase begins.
  4. The naive assumption under test: each rate limit is independent, and built-in connector
     retries keep the system safe. Your job is to find where that assumption breaks.

Topic:     {topic}
Consumers: {consumers}

Roles: Connectors throughput expert (PHASES 1-3) + Power Automate domain expert (PHASE 4).

---

## PHASE 1: SCENARIO SETUP
[Connectors expert. Define consumers and limits before simulating.]

Consumer inventory:

| Consumer | Type | Call rate (req/min) | Concurrency | Retry config | Retry-After read? | Service principal |
|----------|------|---------------------|-------------|--------------|-------------------|------------------|
| [name]   | [cloud flow / standard connector / custom connector / plugin / trigger] | [N/min] | [N / unbounded] | [retries=N, backoff=fixed/exponential] | [yes / no / N/A] | [dedicated / shared with: name] |
(Add rows for each consumer.)

Applicable PA rate limit tiers:

| Tier | Component | PA construct (exact name) | Limit |
|------|-----------|--------------------------|-------|
| connector | [...] | [...] | [N/min] |
| user | [...] | [...] | [N/day] |
| tenant / org | [...] | [...] | [...] |
(Add rows for all applicable tiers. Each row must have an exact PA construct name.)

Aggregate peak volume: [N req/min across all consumers at peak]

GATE 1: Consumer inventory complete. All tier rows have named PA constructs. Aggregate peak
        volume stated. Proceed to PHASE 2 only after this gate is met.

---

## PHASE 2: THROTTLE SIMULATION
[Connectors expert. Do not advance to PHASE 3 until all three sub-sections are filled.]

### 2A — Tier Hit Ordering

Rank tiers in the order they saturate under the aggregate volume from PHASE 1. Row 1 = bottleneck.

| Hit order | Tier | Component | PA construct | Limit | Volume | Margin | First hit |
|-----------|------|-----------|-------------|-------|--------|--------|-----------|
| 1 (bottleneck) | [...] | [specific component -- not "the API"] | [...] | [N/unit] | [N/unit] | [-N% over / +N% headroom] | [min N / record N] |
| 2 | [...] | [...] | [...] | [...] | [...] | [...] | [...] |
(Add rows for each tier from PHASE 1.)

Bottleneck statement:
  "[Specific component] at [PA construct: exact name and limit] is the binding bottleneck.
   It saturates at [N req/unit-time] under this scenario because [reason the hit ordering
   holds for this aggregate volume]. The naive assumption that limits are independent fails
   here because [one sentence linking to cascade or shared principal]."

### 2B — Backpressure Propagation Chain

Starting from the bottleneck, fill one row per propagation hop.

| Hop | From component | Signal | Signal type | To component | Response |
|-----|---------------|--------|-------------|--------------|----------|
| 1   | [bottleneck]  | [HTTP 429 / Retry-After: N / queue depth spike / ...] | [error code / header / queue event / backpressure] | [connector runtime / PA scheduler / calling flow / ...] | [retry queued at T+Ns / flow run failed / error propagated / ...] |
| 2   | [next]        | [...] | [...] | [...] | [...] |
(Continue until you reach the end user or a terminal state.)

### 2C — UX per Throttle Tier (PA Expert Pre-Fill)
[Connectors expert: leave the PA runtime behavior column blank. PA expert fills it in PHASE 4.]

| Tier | User-visible experience (Connectors view) | UX category |
|------|-------------------------------------------|-------------|
| Tier 1 (bottleneck) | [transparent -- user unaware / run delayed N min / error displayed / data dropped silently] | [transparent retry / visible delay / error surfaced / silent data loss] |
| Tier 2 | [must differ from Tier 1] | [different category] |
(Add rows for each tier. Same UX category on two rows does not pass.)

GATE 2: Tier ordering with bottleneck statement, backpressure chain (min 1 hop), UX mapping
        (min 2 tiers, distinct outcomes) all filled. Proceed to PHASE 3.

---

## PHASE 3: FAILURE ANALYSIS
[Connectors expert. This is where the naive assumption breaks. Fill all three sub-sections.]

### 3A — Burst Path Inventory

| Path | PA construct | Location in flow | Peak rate (req/min) | Why it bypasses tier-1 guard |
|------|-------------|-----------------|--------------------|-----------------------------|
| B-01 | [e.g., "Apply to Each, Concurrency Control=Off"] | [specific location in flow] | [N req/min] | [why this construct overwhelms the tier-1 limit] |
(Add rows. If none: "No burst paths -- guards in place: [list PA concurrency controls and values].")

### 3B — Retry-After Gap Table

| Consumer | Action / connector call | Retry-After behavior | Consequence |
|----------|------------------------|---------------------|-------------|
| [name]   | [specific action]      | [reads + respects header / fixed Ns backoff ignoring header / immediate retry / not implemented] | [correct / hammering / premature retry at wrong interval / outage extension] |
(Add rows for each consumer that can receive a 429.)

### 3C — Cascade Chain

At least one cascade where tier-1 throttling causes tier-2 to also throttle.

Cascade C-01:
  Tier 1 throttles:     [specific component]
  Mechanism:            [retry storm adds N req/min / fan-out compounds / fixed-interval
                        hammering from [consumer] / shared-principal amplification / ...]
  Load added to Tier 2: [N additional req/min]
  Tier 2 throttles:     [specific component]
  Failure mode:         [brownout / full stop / partial data / oscillation]
  Duration:             [self-resolving in N min / requires intervention / indefinite]

(Add Cascade C-02, etc. if additional cascades exist.)

GATE 3: At least one burst path row (or explicit "none" with guards), all consumers in
        Retry-After table, at least one complete cascade chain. Proceed to PHASE 4.

---

## PHASE 4: REMEDIATION
[Power Automate domain expert takes over. Reference PHASES 2-3 findings by label (B-01, C-01, etc.)]

### 4A — PA Construct Validation

Review each tier from PHASE 2 and confirm or correct the PA construct name and limit:

| Tier / consumer from PHASE 2 | PA construct (exact, corrected if needed) | Correct limit | Status |
|------------------------------|------------------------------------------|---------------|--------|
| [tier or consumer]           | [exact PA construct name]                | [N/unit]      | [confirmed / corrected -- was: "..." now: "..."] |
(Add rows for all tiers and consumers. This is the C-05 validation pass.)

### 4B — UX Validation (PA Runtime View)

For each tier in PHASE 2.C, confirm or correct the UX based on PA runtime behavior:

| Tier | PA runtime behavior (what the PA engine does) | User-visible experience (corrected) | UX category |
|------|----------------------------------------------|-------------------------------------|-------------|
| Tier 1 | [PA throttles connector / queues run / marks run Failed / ...] | [confirmed from 2C / corrected: actual UX is "..."] | [transparent retry / visible delay / error surfaced / silent data loss] |
| Tier 2 | [...] | [...] | [different from Tier 1] |

### 4C — Quantified Risk Register

| Tier | Limit | Projected volume | Status | Headroom / deficit |
|------|-------|-----------------|--------|--------------------|
| Tier 1 (bottleneck) | [N/unit] | [N/unit] | [SAFE / MARGINAL (<20% headroom) / OVER-LIMIT] | [+N% / -N% over] |
(All tiers from PHASE 2 must appear here.)

### 4D — PA-Specific Remediations

At least two remediations. Each names a specific PA feature or setting — not generic advice.

| # | Finding addressed | PA feature (exact name) | Configuration | Effect on finding |
|---|------------------|------------------------|---------------|------------------|
| R-01 | [B-01 / C-01 / Retry-After gap: consumer / Tier N OVER-LIMIT] | [e.g., "Apply to Each > Concurrency Control (Degree of Parallelism)", "Service principal pooling", "Flow run queue max concurrent runs", "Premium entitlement upgrade", "Scheduled trigger time-offset distribution"] | [what the developer sets, to what value] | [how this changes the specific finding] |
| R-02 | [different finding] | [different PA feature] | [...] | [...] |
(Add rows for additional remediations.)

Inertia verdict: [One sentence -- what happens if this scenario reaches production with no
remediations applied? State the failure mode, which tier collapses first, and the user impact.]

---

Write artifact: simulations/flow/throttle/{topic}-throttle-{date}.md
Frontmatter: skill, topic, date, consumer_count, tier_count, bottleneck_component,
             burst_path_count, retry_after_gap_count, cascade_count,
             over_limit_tier_count, pa_construct_corrections, remediation_count.
```

---

## Round 1 Design Notes

### Criteria coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Bottleneck localization | "Bottleneck statement:" sentence template | Step 3 imperative + "Name the component" | 2A bottleneck declaration | ROLE 1.2 declaration | 2A sentence template + inertia link |
| C-02 Hit ordering | Hit order column in TIER TABLE | Step 4 ordered list | 2A table with Why column | ROLE 1.2 ordered tiers | 2A table with Hit order column |
| C-03 Backpressure trace | BACKPRESSURE CHAIN table | Step 5 hop-by-hop | 2B hop sequence | ROLE 1.3 trace | 2B pre-printed hop table |
| C-04 UX per tier | UX MAPPING table + distinct category rule | Step 6 list + "must differ" | 2C table + distinct category rule | ROLE 2.2 UX table | 2C + 4B PA validation pass |
| C-05 PA domain grounding | Domain rule header + PA construct column | "Name the tier" rule header | Domain rule header + PA construct column | ROLE 2.1 validation pass | GATE 1 check + 4A validation pass |
| C-06 Burst path detection | BURST PATH INVENTORY section | Step 7 structured | 3A named sub-section (gated) | ROLE 1.4 checklist | 3A pre-printed table (gated) |
| C-07 Retry-After gaps | RETRY-AFTER HANDLING GAPS table | Step 8 assessment | 3B named sub-section (gated) | ROLE 2.3 assessment | 3B pre-printed table (gated) |
| C-08 Cascade failure | CASCADE FAILURE CHAIN section | Step 9 structured | 3C named sub-section (gated) | ROLE 1.5 chain | 3C pre-printed chain (gated) |
| C-09 Quantified throughput | QUANTIFIED RISK SUMMARY table | Step 10 per-tier numbers | 4A RISK REGISTER table | Implicit in 1.2 tier volumes | 4C RISK REGISTER table |
| C-10 PA-specific remediation | PA-SPECIFIC REMEDIATIONS section | Step 10 remediation | 4B named sub-section | ROLE 2.4 named features | 4D pre-printed table |

### Structural mechanism comparison

| Mechanism | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| Pre-printed tables | Yes | No | Partial | No | Yes |
| Phase gates | No | No | Yes | No | Yes |
| Imperative register | Partial | Yes | No | No | Yes (rules header) |
| Role sequence | No | No | No | Yes | Yes |
| Inertia framing | No | No | No | No | Yes |

### Key design bets

- **C-02 bottleneck ordering**: The "Hit order" column in V-01/V-03/V-05 makes an unordered
  list structurally impossible. V-02 relies on the "ordered list" imperative in Step 4. V-04
  relies on the Connectors expert's natural tier sequencing. The column mechanism is the
  strongest bet.

- **C-05 PA grounding**: V-04 and V-05 are the only variations that run a PA expert validation
  pass (ROLE 2.1 / PHASE 4A). This makes C-05 a two-pass check rather than a one-shot rule.
  Open question: does a validation pass produce more accurate PA terminology than a strong
  domain rule header?

- **C-08 cascade placement**: In V-03 and V-05, the cascade is sub-section 3C inside a gated
  FAILURE ANALYSIS phase, forcing it before remediation. In V-04, the Connectors expert detects
  the cascade (ROLE 1.5) and the PA expert characterizes it implicitly through the UX section.
  The gated sub-section placement is the stronger structural guarantee.

- **Inertia framing** (V-05 only): Positioning the prompt as "find where the naive assumption
  breaks" is a hypothesis about whether belief-disproving framing drives cascade and retry-after
  analysis more naturally than explicit rule lists. No prior round has tested this for
  flow-throttle. May help or may produce over-engineered output. Open for R2 scoring.

### Predicted differentiation

| Dimension | Strongest | Reasoning |
|-----------|----------|-----------|
| C-01/C-02 structural enforcement | V-01/V-03/V-05 | Hit order column beats ordered list instruction |
| C-04 UX distinctness | V-04/V-05 | PA expert UX validation pass catches same-category errors |
| C-05 PA terminology accuracy | V-04/V-05 | Two-pass validation vs one-shot rule |
| C-06/C-07/C-08 coverage | V-03/V-05 | Gated sub-sections beat standalone sections |
| C-09 numbers | V-01/V-03/V-05 | Pre-printed risk table forces columns |
| Overhead / conciseness | V-02 | Fewest structural elements |
| Inertia framing payoff | V-05 (or backfire) | Untested — open question for R1 scoring |

### Predicted V-golden

**V-05** is the direct synthesis target: every criterion has a structural home through a
combination of pre-printed tables, phase gates, role sequence, and inertia framing. No surface
where any criterion should appear is left to model discretion.

**V-03** is the closest single-mechanism competitor — phase gates enforce C-06/C-07/C-08 at
gated sub-sections, but lacks the PA expert validation pass for C-05 and the pre-printed
bottleneck table columns for C-01/C-02. Expected score gap between V-03 and V-05: primarily
on C-05 (PA grounding depth) and C-10 (remediation PA feature specificity).

**V-04** is the wildcard: the role sequence is the only variation that structurally forces
PA grounding as an independent validation pass. If the PA expert role produces richer C-05
and C-10 output than a domain rule header, V-04 could outscore V-03 on those criteria.
Key open question for R1 scoring.
