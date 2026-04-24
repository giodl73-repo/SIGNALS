# flow-throttle — Round 2 Variations (v16 Rubric)

## Context and Variation Strategy

v16 adds four new aspirational criteria (C-11 through C-14) derived from R1 excellence signals.
None of the four appeared reliably in R1 output — each targets a structural property that
generic prompts elide:

| ID | What it requires | Why prompts skip it |
|----|-----------------|---------------------|
| C-11 | Per-hop mechanism as a discrete column in propagation trace | Narrators default to prose causation; table column forces attribution per hop |
| C-12 | Step-by-step arithmetic with each named limit cited inline | Models state conclusions; arithmetic-writing requires an explicit mandate |
| C-13 | Upfront component-limit inventory before any analysis | Analysis phases start immediately; inventory gets folded into Phase 1 prose |
| C-14 | Fixed 1×/3×/5×/10× rows + error-rate column in tier matrix | Free-form tier summaries omit multiplier rows and degrade error-rate to qualitative |

**R2 design goals:**
1. C-11 isolation: does forcing a named-column table schema in the prompt header unlock C-11
   independently of other changes?
2. C-13 gate: does a blocking Phase 0 gate (inventory must complete before analysis starts)
   drive C-13 without also requiring C-11/C-14 scaffolding?
3. C-12 arithmetic mandate: does "show your work, name each limit" phrasing in a conversational
   register produce auditable arithmetic without rigid table schemas?
4. Combined ceiling: does assigning tables to specific roles (each role owns one table) achieve
   all four new aspirational criteria simultaneously?

Three single-axis variations (V-01, V-02, V-04), two combined or role-sequence variations
(V-03, V-05):

| Variation | Axis | C-11 | C-12 | C-13 | C-14 | Predicted composite |
|-----------|------|------|------|------|------|---------------------|
| V-01 | Output format — pre-committed table schemas | PASS | PASS | PASS | PASS | 100/100 |
| V-02 | Lifecycle emphasis — phase-gated inventory-first | PASS | PASS | PASS | PASS | 100/100 |
| V-03 | Role sequence — expert-as-inventory-anchor | PASS | PASS | PASS | PASS | 100/100 |
| V-04 | Phrasing register — conversational worked-example | PARTIAL | PASS | PARTIAL | PASS | ~85/100 |
| V-05 | Combined: output format + role sequence | PASS | PASS | PASS | PASS | 100/100 |

V-04 is the isolation test for C-12 via register alone (no table schema), with a hypothesis
that conversational "show your work" framing reaches C-12 but falls short on C-11/C-13 without
structural scaffolding. If V-04 reaches C-11 and C-13, that confirms register alone is sufficient;
if it does not, that confirms structural mandates are required for those two.

---

## V-01 — Output Format: Pre-committed Table Schemas

**Axis:** Output format — embedding all four required table schemas (with column names fixed)
at the top of the prompt before any analytical instructions.

**Hypothesis:** Declaring table schemas as an "output contract" upfront — before analytical
phases — forces C-11 (mechanism column declared in TABLE B), C-13 (inventory table declared as
TABLE A prerequisite), and C-14 (fixed multiplier rows in TABLE C) without relying on phase
gates. C-12 is covered by the Arithmetic column in TABLE C requiring step-by-step text.
V-04 tests whether conversational framing alone reaches the same criteria; V-01 uses
schema-first structure instead.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### OUTPUT CONTRACT — Four Required Tables

This simulation must produce the following four structured tables. Column schemas are
fixed — add rows as needed, do not remove or rename columns.

**TABLE A — Component-Limit Inventory**
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

*Every component reachable from the entry trigger to the terminal action must have a row.
PA construct type must be drawn from the Power Platform taxonomy (see Phase 1). Components
with unknown limits use the platform-documented default and receive status `estimated`.
Components with genuinely unknown limits receive `?-unresolved` — they may not be silently
omitted.*

**TABLE B — Backpressure Propagation Trace**
| Hop | From component | To component | Causal mechanism | Effect observed |
|-----|---------------|-------------|-----------------|-----------------|

*Each row covers exactly one directed hop. "Causal mechanism" names the specific
technical cause at this hop (e.g., "429 returned to action; no Retry-After handler
present; immediate retry issued within same throttle window" or "connector queue fills;
runtime queues new trigger invocations; trigger backlog accumulates"). A narrative
paragraph listing affected components does not satisfy this column — mechanism must be
attributed at each individual hop.*

**TABLE C — Volume-Multiplier Tier Matrix**
| Multiplier | Est. req/min | First throttle tier hit | Behavior at this tier | Est. error rate | Arithmetic |
|-----------|-------------|------------------------|----------------------|----------------|------------|
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

*Rows 1×/3×/5×/10× are required. "Est. error rate" must be a numeric value or bracketed
range (e.g., "8–12%") derived from TABLE A limits. "Arithmetic" must show the calculation
step-by-step with each TABLE A limit named inline — not asserted as a conclusion.*

**TABLE D — Mitigation Prescriptions**
| Finding | Root cause | Prescribed remediation | Specific PA config or pattern |
|---------|-----------|----------------------|------------------------------|

---

### Phase 1 — TABLE A: Component-Limit Inventory

Fill TABLE A before any propagation or UX analysis begins. PA construct types must come
from this list: Power Platform request entitlement, connector throttling policy (standard
or premium tier), flow run concurrency limit (per environment), action call limit (per
24-hour window), Microsoft 365 service protection limit, trigger polling frequency cap.

Generic descriptions ("API limit", "service limit") are not acceptable PA construct types.

---

### Phase 2 — TABLE B: Backpressure Propagation Trace

With TABLE A complete, identify the FIRST BOTTLENECK — the TABLE A component whose limit
is hit first at baseline request volume. Fill TABLE B starting from that component.
Trace every downstream hop until propagation terminates. For components in TABLE A that
are not on the propagation path, add a row with Effect = `OUT-OF-PATH`.

---

### Phase 3 — Unprotected Burst Paths

Identify at least one structural gap where burst traffic bypasses throttle controls:
a trigger that fires parallel flow runs without a concurrency cap, a loop without
concurrency constraint, or an action sequence without a retry policy. Name the specific
PA construct and the structural absence.

---

### Phase 4 — Retry-After Handling Audit

For each TABLE B hop where a 429 or throttle signal is received, check whether the
flow reads and honors the `Retry-After` header. Produce `FINDING-RH-NN` for each gap.

---

### Phase 5 — User Experience by Tier

For each distinct throttle tier reached in TABLE B, describe observable user-facing
behavior: what the user sees, how long they wait, whether failure is surfaced or silent.
Cover at least two tiers if multiple exist.

---

### Phase 6 — Cascading Throttle Failure

Construct or identify one scenario where throttling at a TABLE B tier triggers a second
throttle event at a different tier. Name both tiers, the causal link, and the compounded
effect on throughput or error rate.

---

### Phase 7 — TABLE C: Tier Matrix with Arithmetic

Fill TABLE C. For the Arithmetic column, write the step-by-step calculation:
> "TABLE A row 2: connector limit = 600 req/min. At 5×: inbound = 1500 req/min.
> Excess = 900 req/min. Queue capacity = 300 (estimated from platform default).
> After queue fills: 600/1500 = 40% overflow rate → ~40% error rate."

State assumptions explicitly if any TABLE A limit is `?-unresolved`.

---

### Phase 8 — TABLE D: Mitigation Prescriptions

Fill TABLE D. One row per FINDING-RH-NN from Phase 4 and one row per unprotected burst
path from Phase 3. Prescribed remediations must name the specific PA config or pattern:
the exact flow setting, the backoff formula, the queue integration point. Generic guidance
("implement retry") does not pass.

---

## V-02 — Lifecycle Emphasis: Phase-Gated Inventory-First

**Axis:** Lifecycle emphasis — making Phase 0 (complete component-limit inventory) a
blocking gate before any analysis phase runs, with explicit GATE conditions that prevent
forward progress if the gate is not satisfied.

**Hypothesis:** A blocking Phase 0 gate drives C-13 more reliably than a soft instruction
to "start with an inventory" because it reframes the inventory as a precondition, not an
optional step. Phase 1 backpressure trace then inherits the inventory as a constraint
(must trace every TABLE 0 component), driving C-11. Phase 5 arithmetic gate drives C-12.
Phase 7 tier matrix with fixed rows drives C-14. Single-axis: only lifecycle structure
changes; table schemas, register, and roles are held constant.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PHASE 0 — Component-Limit Inventory (BLOCKING GATE)

**Phase 1 is blocked until this phase is complete.**

Before any propagation or UX analysis: list every component in the request path for
`{{topic}}`. For each component provide:
- Exact component name as it appears in Power Automate or the connector ecosystem
- PA construct type from: Power Platform request entitlement | connector throttling
  policy | flow run concurrency limit | action call limit | M365 service protection
  limit | trigger polling frequency cap
- Numeric rate limit with unit (e.g., "600 req/min", "5 concurrent runs")
- Whether the value is confirmed (from documentation) or estimated (from platform default)

If a component's exact limit is unknown, use the documented platform default and mark
as `estimated`. If no default is available, mark the limit as `?-unresolved`. Components
may not be omitted because their limit is uncertain.

**GATE 0:** Phase 1 does not begin until every component on the request path from entry
trigger to terminal action has a Phase 0 row. A row marked `?-unresolved` satisfies
GATE 0; a missing row does not.

---

### PHASE 1 — Bottleneck Localization

With Phase 0 complete, identify the FIRST BOTTLENECK: the Phase 0 component whose
numeric limit is reached first at the scenario's baseline request volume. State:
1. Component name (must match a Phase 0 row)
2. Limit type and numeric threshold
3. Estimated baseline request rate that exceeds this limit

---

### PHASE 2 — Backpressure Propagation Trace

Trace how throttling at the Phase 1 bottleneck propagates through the system. For each
hop, use this format:

**Hop N:** `[From component]` → `[To component]`
**Mechanism:** [Specific technical cause — e.g., "429 returned to action; action has no
Retry-After handler; immediate retry issued within same throttle window; connector
re-throttles before window resets"]
**Effect:** [Observable change at the To component]

Do not describe propagation as a flat list of affected components. Each hop must state
the mechanism — the specific technical cause. "Also throttled" or "cascades to" are not
mechanism statements.

**GATE 1:** Before proceeding to Phase 3, review every hop. Any hop with a generic or
absent mechanism must be rewritten with the specific cause. Only then proceed.

---

### PHASE 3 — User Experience at Each Throttle Tier

For each distinct throttle tier reached in Phase 2, describe the observable user-facing
behavior: what the user sees (429 message? queue delay? flow failure with error?), how
long they wait, and whether failure is surfaced or silent. Cover at least two tiers if
multiple tiers exist.

---

### PHASE 4 — Unprotected Burst Paths

Identify at least one structural gap where burst traffic bypasses throttle controls. Name:
- The specific PA construct involved (trigger type, action type, loop type)
- The structural absence (no concurrency cap configured, no retry policy, unbounded
  parallel branch)

This is a structurally unprotected path — a path that is throttled at a higher limit
does not qualify.

---

### PHASE 5 — Retry-After Handling Audit

For each action in the Phase 2 trace that receives a 429 or throttle signal, check
whether the flow reads and honors the `Retry-After` header or equivalent backoff signal.
Produce `FINDING-RH-NN: [action name] — [specific gap]` for each missing handler.

---

### PHASE 6 — Cascading Throttle Failure Scenario

Construct a scenario where throttling at one Phase 2 tier triggers a second throttle
event at a different tier. Name both tiers, the causal link, and the compounded impact
on throughput or error rate.

---

### PHASE 7 — Quantified Impact with Arithmetic

For a 10× volume spike, write the arithmetic step by step. Each step must name the
specific limit from Phase 0:

1. State baseline throughput (requests/min or relevant unit)
2. State 10× inbound volume
3. Name the limiting component (Phase 0 row) and its numeric threshold
4. Calculate excess volume above the limit
5. Estimate queue absorption (state assumption if queue capacity is from Phase 0
   `?-unresolved` row)
6. Compute estimated error rate as a percentage

**GATE 2:** The arithmetic must be auditable — each limit named in the calculation
must correspond to a Phase 0 row. Conclusions stated without showing the step-by-step
chain do not satisfy this gate.

---

### PHASE 8 — Throttle Tier Matrix

Produce the tier matrix. Use the Phase 7 arithmetic as the basis for the error rate column.

| Load | Est. req/min | First tier hit | Behavior | Est. error rate |
|------|-------------|----------------|----------|----------------|
| 1× (baseline) | | | | |
| 3× | | | | |
| 5× | | | | |
| 10× | | | | |

Rows 1×/3×/5×/10× are required. Error rate must be a numeric value or bracketed range —
qualitative labels ("high", "low") do not qualify. Estimates must trace back to Phase 0
limits via Phase 7 arithmetic.

---

### PHASE 9 — Mitigation Prescriptions

For each FINDING-RH-NN (Phase 5) and each unprotected burst path (Phase 4), prescribe
a specific, actionable remediation:
- Name the exact PA config field or setting (e.g., "Trigger concurrency: set to 1 in
  trigger settings panel")
- Or name the specific pattern with parameters (e.g., "Exponential backoff: base 10s,
  multiplier 2×, max 5 retries, jitter ±20%")
- Or name the queue integration point (e.g., "Route to Service Bus queue with max
  concurrency 10 on the consuming flow")

Generic guidance ("implement retry logic", "add throttle handling") does not qualify.

---

## V-03 — Role Sequence: Expert-as-Inventory-Anchor

**Axis:** Role sequence — running the domain expert first with an explicit mandate to
produce a complete component-limit inventory as a handoff artifact, before the trace
analyst or quantitative reviewer execute.

**Hypothesis:** When the domain expert runs first and produces the inventory table as
the primary handoff artifact (rather than as a preamble to their own analysis), the
inventory becomes a constraint on subsequent roles: Role 2 must trace every TABLE 1
component, driving C-11 through inheritance; Role 3 must cite TABLE 1 limits in
arithmetic, driving C-12. The expert-as-anchor sequence separates inventory (domain
expertise) from tracing (analytical skill) from quantification (math), matching the
natural expertise separation and preventing each role from eliding what it "should
already know." V-03 changes only role sequence and handoff contract; format and register
are held constant relative to V-01.

---

You are running a three-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence; each role receives the prior role's structured output.
No role may skip or abbreviate the prior role's tables — they appear verbatim.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### ROLE 1 — Throughput Domain Expert

**Mandate:** Produce a complete component-limit inventory before simulation begins.
This inventory is the Role 2 input — Role 2 may not trace components not in this table.

**Produce: INVENTORY TABLE**
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

PA construct type must be drawn from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

For every component reachable from the entry trigger to the terminal action: add a row.
Status values: `confirmed` (from documentation), `estimated` (platform default applied),
`?-unresolved` (no default available). Components may not be omitted.

After the INVENTORY TABLE, declare the FIRST BOTTLENECK: the row whose limit is reached
first at the baseline request volume for `{{topic}}`. Annotate that row `<-- FIRST BOTTLENECK`.

**Domain check:** Flag any Phase 0 `?-unresolved` rows as potential hidden bottlenecks —
their absence from the trace does not mean they are safe; it means they are unknown.

---

### ROLE 2 — Trace Analyst

**Receives:** INVENTORY TABLE + FIRST BOTTLENECK declaration from Role 1.
**Mandate:** Trace backpressure propagation from the FIRST BOTTLENECK through the system.

**Produce: PROPAGATION TABLE**
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|

Rules:
- One row per directed hop (From → To).
- "Causal mechanism" names the specific technical cause at this hop. Acceptable forms:
  "429 returned; no Retry-After handler; immediate retry within throttle window;
  connector re-throttles" or "concurrency cap reached; runtime queues new trigger
  invocations; trigger backlog grows at PA runtime layer."
  Unacceptable: "also throttled," "cascade to next component," "propagates."
- Every INVENTORY TABLE component on the propagation path must appear in at least
  one row (From or To). Components not on the propagation path: add a row with
  Effect = `OUT-OF-PATH`.
- Continue tracing until no further downstream component is affected.

After the PROPAGATION TABLE, produce:
1. **Retry-After audit:** for each hop where a 429 signal is received, check whether
   the flow honors the `Retry-After` header. Produce `FINDING-RH-NN` for each gap.
2. **Unprotected burst path:** identify at least one structural gap (missing concurrency
   cap, no retry policy, unbounded parallelism) naming the specific PA construct and
   the structural absence.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** INVENTORY TABLE (Role 1) + PROPAGATION TABLE + findings (Role 2).
**Mandate:** Quantify scale impact, produce the tier matrix and mitigations.

**Task A — User Experience by Tier**
For each distinct throttle tier in the PROPAGATION TABLE, describe the observable
user-facing behavior: what the user sees, how long they wait, whether failure is silent
or surfaced with an error message. Cover at least two tiers if multiple exist.

**Task B — Cascading Failure Scenario**
Using PROPAGATION TABLE hops, construct a scenario where throttling at one tier triggers
a second throttle event at a different tier. Name both PROPAGATION TABLE rows, the causal
link, and the compounded effect on throughput or error rate.

**Task C — Tier Matrix with Step-by-step Arithmetic**
Produce:

| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

The Arithmetic column must show the step-by-step calculation that produces the error rate
estimate, naming each INVENTORY TABLE limit used:
> "INVENTORY row 2: connector limit = 600 req/min. At 3×: inbound = 900 req/min.
> Excess = 300 req/min. Queue capacity = 300 (INVENTORY row 4, estimated).
> After queue saturates: 300/900 = 33% overflow → ~33% error rate."

If a limit is `?-unresolved`, state the assumption and proceed — do not leave the
Arithmetic column empty.

**Task D — Mitigation Prescriptions**
For each FINDING-RH-NN from Role 2 and each unprotected burst path from Role 2, prescribe
a specific, actionable remediation naming the exact PA config or pattern:
- Concurrency setting location and value
- Backoff formula with base delay, multiplier, and max retries
- Queue integration point with consuming flow concurrency
Generic guidance does not qualify.

**Consistency check before submitting:**
1. Every PROPAGATION TABLE component appears in the INVENTORY TABLE (no phantom components).
2. Every Arithmetic cell traces to a named INVENTORY TABLE row.
3. Every TABLE D finding corresponds to a Role 2 FINDING-ID or named burst path.
Flag violations as `CONSISTENCY-FLAG-NN`.

---

## V-04 — Phrasing Register: Conversational Worked-Example

**Axis:** Phrasing register — conversational, teacher-to-colleague framing with
explicit "show your work" instructions, replacing structured phase headers and gate
conditions with natural-language directives.

**Hypothesis:** Conversational "walk me through the math" phrasing with an explicit
"name each limit you use in the calculation" instruction is sufficient to drive C-12
(step-by-step arithmetic with named limits) without rigid table schemas. The hypothesis
under test is whether C-11 (per-hop mechanism column) and C-13 (upfront inventory)
require structural mandates, or whether natural-language directives achieve the same
result. If V-04 scores lower than V-01/V-02 on C-11 and C-13, that confirms structural
scaffolding is load-bearing for those criteria.

---

You are a senior Power Automate throughput specialist walking your team through a
rate-limiting simulation for `{{topic}}`. Be specific, show your work, name the numbers.
The team needs to understand not just what happens but why — the mechanism at each step,
the math behind the estimates.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

**Start by mapping every component.**

Before tracing anything, give a complete picture of what we are working with: every
component in the `{{topic}}` request path, what kind of throttle control governs it —
Power Platform request entitlement? connector policy? run concurrency? M365 service
protection? trigger polling cap? — and the actual numeric limit. If the exact number is
not known, state the platform default and call it an estimate. Name every component even
if the limit is uncertain — an unknown limit is not the same as no limit.

---

**Walk through what happens when volume climbs.**

Starting from the component that hits its limit first, walk hop by hop through the
propagation. For each hop: name the two components involved, then explain the
mechanism — what specifically causes the next component to see the effect? A 429 with
no handler that triggers an immediate retry? A queue that fills? A concurrency cap
that starts stacking trigger invocations? "It propagates" is not a mechanism.

---

**Tell the user experience story.**

At each distinct throttle tier reached in the trace, describe what the user actually
experiences: what error message appears, how long they wait, does the flow fail silently
or show an explicit error? Cover at least two tiers if multiple exist.

---

**Flag the structural weak spots.**

Walk through any path where burst traffic bypasses throttle protection — a trigger that
fires parallel runs without a concurrency cap, a loop without a concurrency constraint,
a parallel branch that issues actions without retry policy. Name the specific construct
and what is structurally absent.

Also: for each action that receives a 429 signal, is the flow reading and honoring the
`Retry-After` header? Call out any gap explicitly.

---

**Show the math.**

For a 10× volume spike on `{{topic}}`, walk through the arithmetic step by step.
Write it out — do not just state the conclusion:
1. Baseline throughput (how many requests per minute at normal load)
2. 10× inbound volume
3. The specific limit being exceeded — name the component and the numeric threshold
4. Excess volume above the limit
5. How much the queue absorbs, if anything — state the assumption if uncertain
6. The resulting error rate as a percentage, derived from the numbers above

The calculation should be auditable — someone reading it should be able to follow from
the stated limits to the stated error rate without taking any step on faith.

---

**Give the tier comparison.**

Fill in this table for 1×, 3×, 5×, and 10× of normal load. For the error rate column,
use the arithmetic above — a bracketed range is fine, but explain how it was derived.

| Load | Est. req/min | First throttle tier | What happens | Est. error rate |
|------|-------------|---------------------|-------------|----------------|
| 1× | | | | |
| 3× | | | | |
| 5× | | | | |
| 10× | | | | |

---

**Describe the domino case.**

Walk through a specific scenario where throttling at one tier sets off throttling at a
second tier — what triggers the first, what carries it to the second, what does the
compounded effect do to throughput or failure rate?

---

**End with specific prescriptions.**

For every weak spot found — unprotected burst paths, missing Retry-After handling,
cascading failure patterns — state the specific fix: the PA setting name, the backoff
formula with parameters, the queue integration point. Not "implement retry logic" —
the actual config.

---

## V-05 — Combined: Output Format + Role Sequence

**Axis:** Combined — output format (pre-committed table schemas) and role sequence
(each role owns one or more specific tables), integrated so that role handoff contracts
are expressed as table ownership rather than prose-described responsibilities.

**Hypothesis:** The combination of table-schema pre-commitment (V-01 axis) and role
ownership (V-03 axis) achieves more reliable C-11/C-12/C-13/C-14 coverage than either
axis alone, because table ownership eliminates the elision risk that single-role prompts
have (the model can skip a table by omitting a phase), while the pre-committed schema
eliminates the structural ambiguity that multi-role prompts have (roles can satisfy
their mandate in prose if no schema is declared). The consistency check from V-03 Role 3
is retained as a structural verification gate.

---

You are running a three-role Power Automate throttle simulation for `{{topic}}`.
Each role owns specific output tables declared below. Tables must be complete before
the next role begins. No role may fulfill its table mandate in prose — the schema columns
are required.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### OUTPUT TABLES — Pre-committed schemas

**TABLE 1 — Component-Limit Inventory** *(Role 1 owns this table)*
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
*(Status: confirmed / estimated / ?-unresolved. All reachable components required.)*

**TABLE 2 — Backpressure Propagation Trace** *(Role 2 owns this table)*
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
*(One row per directed hop. "Causal mechanism" = specific technical cause at this hop.
Narrative paragraph listing affected components does not substitute for this column.)*

**TABLE 3 — Volume-Multiplier Tier Matrix** *(Role 3 owns this table)*
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |
*(Arithmetic column = step-by-step calculation citing TABLE 1 limits by row. Must be
auditable: from named limit → at N× load → % error rate. Not a conclusion.)*

**TABLE 4 — Mitigation Prescriptions** *(Role 3 owns this table)*
| Finding ID | Type | Root cause | Prescribed remediation | Specific config |
|-----------|------|-----------|----------------------|----------------|

---

### ROLE 1 — Domain Expert

**Owns:** TABLE 1 + Bottleneck Declaration

Fill TABLE 1. PA construct type must come from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

For every component reachable from the entry trigger: add a TABLE 1 row. Generic labels
("API limit", "service rate limit") are not PA construct types.

Status rules: use `confirmed` for documented values, `estimated` for platform defaults,
`?-unresolved` when no default is available. Do not omit components — a `?-unresolved`
row is better than an absent row.

After TABLE 1: declare the FIRST BOTTLENECK by annotating the row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK annotation from Role 1.
**Owns:** TABLE 2 + Retry-After findings + Unprotected burst path identification

Fill TABLE 2 starting from the FIRST BOTTLENECK. Rules:
- One row per directed hop. A hop is a propagation event (From → To).
- "Causal mechanism" must name the technical cause:
  "429 returned; no Retry-After handler; immediate retry issued within same throttle
  window" or "concurrency cap reached; runtime queues trigger invocations; backlog
  accumulates at PA runtime layer" or "queue fills; overflow requests returned with
  503; upstream connector interprets as failure; retries compound inbound load."
  Generic text ("also throttled", "cascade occurs") fails.
- All TABLE 1 components on the propagation path: appear as From or To.
- TABLE 1 components not on the path: add a row with Effect = `OUT-OF-PATH`.
- Trace continues until no further downstream component is affected.

After TABLE 2:
1. **Retry-After audit:** For each TABLE 2 hop receiving a 429 signal, check whether the
   flow reads and honors `Retry-After`. Produce `FINDING-RH-NN: [component] — [gap]`.
2. **Unprotected burst path:** Identify at least one structural gap (missing concurrency
   cap, no retry policy, unbounded parallel branch). Name the PA construct and the
   structural absence.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** TABLE 3 + TABLE 4 + UX description + cascade scenario

**UX by Throttle Tier**
For each distinct tier in TABLE 2: describe what the user observes — error message,
wait time, silent vs. visible failure. Cover at least two tiers if multiple exist.

**Cascading Failure Scenario**
Using TABLE 2 hops: construct a scenario where throttling at one tier triggers a second
throttle event at a different tier. Name both TABLE 2 rows, the causal link, and the
compounded impact.

**TABLE 3 — Tier Matrix**
Fill TABLE 3. The Arithmetic column must show the step-by-step chain from named TABLE 1
limit to stated error rate:
> "TABLE 1 row 2: connector limit = 600 req/min. At 5×: inbound = 1500 req/min.
> Excess = 900 req/min. Queue capacity = 300 (TABLE 1 row 4, estimated). After queue
> saturates: 600 req/min dropped → 600/1500 = 40% error rate."

For `?-unresolved` TABLE 1 rows: state the assumption, proceed with arithmetic.
Do not leave Arithmetic blank.

**TABLE 4 — Mitigations**
Fill TABLE 4. One row per FINDING-RH-NN and one row per unprotected burst path. The
"Specific config" column must name the exact PA setting or pattern — not generic guidance.

**Consistency Verification**
Before submitting Role 3 output, verify:
1. Every TABLE 2 component appears in TABLE 1 (no phantom components).
2. Every TABLE 3 Arithmetic cell traces to a named TABLE 1 row.
3. Every TABLE 4 row corresponds to a Role 2 FINDING-ID or named burst path.

Flag violations as `CONSISTENCY-FLAG-NN`.
