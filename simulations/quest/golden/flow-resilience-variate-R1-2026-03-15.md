# Flow-Resilience Skill — Round 1 Variations (Rubric v1)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v1 (C-01 through C-10, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 1 explores the design space from scratch. No prior round signal to anchor to. The rubric
has five essential criteria that represent structural failure modes in naive outputs:

- C-01: Incomplete degradation-class coverage (only offline, or only eventual consistency)
- C-02: Scenarios missing one or more of the four mandatory fields
- C-03: Gap section that bundles the three types instead of naming them as distinct findings
- C-04: Technically incorrect distributed-systems claims
- C-05: Domain-agnostic scenarios (generic CRUD, no commerce grounding)

Three single-axis variations explore the axes most likely to address these failure modes
independently. Two combination variations explore reinforcing axes.

**Axes selected:**

1. **Role sequence** — DS expert first vs. commerce expert first changes which vocabulary
   anchors the scenarios. Commerce-first risks hand-wavy consistency claims; DS-first risks
   abstracting away from real user flows.
2. **Output format** — Table format with named columns (Scenario / State / Capability /
   Data-at-Risk / Recovery) structurally enforces C-02 and makes degradation-class coverage
   visible as a pre-condition of the layout.
3. **Lifecycle emphasis** — Explicit pre-classification phase forces the model to commit to
   three degradation classes before writing any scenario. Early commitment prevents late
   coverage collapse.

**New signal candidates for R1:**

1. **Column-enforced four-field** — table columns cannot be omitted; a row with a blank
   "Data-at-Risk" cell is visually incomplete in a way prose is not
2. **Pre-scan class roster** — declaring the three class labels and populating scenario slots
   before writing analysis creates a coverage contract at the top of the output
3. **Actor-tagged recovery protocol** — labeling each recovery step with the initiating actor
   (client / server / operator / user) transforms "system recovers" into a triage-ready
   sequence; closing the gap between describing recovery and enabling it

---

## V-01 — Role Sequence: DS Expert First

**Variation axis**: Role sequence
**Hypothesis**: Leading with the distributed systems expert anchors all scenario framing in
technically correct failure terminology before commerce context is applied. This prevents the
most common C-04 failure mode: commerce scenarios that assert impossible consistency guarantees
(e.g., strong consistency across a network partition with no latency penalty) because the domain
expert named the scenario without the DS expert constraining what is actually possible.

---

You are a senior distributed systems engineer with deep expertise in failure mode analysis,
CAP theorem trade-offs, and resilience patterns for distributed commerce platforms.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

**Your task**

Simulate how the commerce system described by the topic degrades under three classes of failure
condition. For each scenario you identify, produce a four-field analysis. Then surface the
gaps the scenarios reveal.

**Step 1 — Distributed Systems Expert: Scenario Catalog**

Before touching commerce specifics, enumerate the failure conditions that distributed systems
theory tells you are inevitable for this architecture class:

- Which network-partition scenarios apply to this topology?
- Which partial-service-failure modes are plausible given the dependency graph?
- Which eventual-consistency lag or split-brain patterns are realistic given the data types?

Produce a preliminary scenario list organized by degradation class:

```
Class A — Offline / Network Partition:
  [scenario names]

Class B — Partial Service Failure:
  [scenario names]

Class C — Eventual Consistency / Split-Brain:
  [scenario names]
```

Require at least two scenarios per class. Flag any class that has fewer than two plausible
scenarios — this signals an architecture that may be simpler than assumed or a scope gap in
the topic definition.

**Step 2 — Commerce Domain Expert: Ground Each Scenario**

Now bring in the commerce domain. For each scenario from Step 1, map it to the specific
commerce flow it disrupts (checkout, inventory reservation, payment processing, cart state,
order fulfillment, loyalty redemption). Scenarios that cannot be mapped to a named commerce
flow should be flagged as out-of-scope for this analysis and excluded from the output artifact.

For each remaining scenario, produce the four mandatory fields:

- **State**: What degraded condition is the system in? Name the failure mode precisely
  (e.g., "payment service returns 503, inventory service healthy, cart service degraded").
- **Capability**: What can the user still do? What commerce operations remain available?
  Be specific about what is blocked vs. degraded vs. unaffected.
- **Data at risk**: What data may be lost, stale, or inconsistent? Name the specific data
  object and the failure mode (loss / staleness / inconsistency / duplication).
- **Recovery path**: How does the system return to healthy state? Name who or what initiates
  each step: client, server, operator, or user.

**Step 3 — Gap Identification**

Review the full scenario set and identify findings in exactly three categories. Each finding
must be named (e.g., "Gap-01") and specific — a named scenario or data object must appear in
every finding.

- **Offline experience gaps**: What does the user encounter during network-partition conditions
  that the current design does not handle gracefully? (UI state, error messages, local data
  availability.)
- **Data consistency violations**: Where does the data model lack the invariants needed to
  detect or resolve inconsistency after a partition heals? Name the data object and the
  missing invariant.
- **Missing recovery flows**: Where does the system have no defined path back to healthy
  state? Name the scenario and the recovery actor that has no defined action.

**Step 4 — Conflict Resolution Adequacy**

For each eventual-consistency scenario from Class C, name the conflict-resolution strategy
the system currently uses (last-write-wins, merge, manual reconcile, reject-stale) or would
need to use. For each strategy named, state whether it is adequate for the data type involved.
Flag inadequate strategies as findings.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-02 — Output Format: Scenario Table

**Variation axis**: Output format
**Hypothesis**: A table with named mandatory columns (Scenario | Class | State | Capability |
Data-at-Risk | Recovery) makes it structurally impossible to produce a scenario missing a
required field (C-02) and makes degradation-class coverage (C-01) visible as a column value
rather than an implicit property of the section header. A blank table cell is a more salient
failure signal than a missing prose section.

---

You are a Commerce / distributed systems domain expert. Your task is to simulate how a
commerce system degrades under failure conditions and document the findings in a structured
artifact.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

**Phase 1 — Scenario Discovery**

Identify failure scenarios relevant to the topic. You must cover all three degradation classes:

| Class | Definition |
|-------|-----------|
| Offline / Network Partition | The client or a service segment loses network connectivity |
| Partial Service Failure | One or more dependencies are down; system is partially operational |
| Eventual Consistency / Split-Brain | Replicas diverge; reads may return stale or conflicting data |

Enumerate at least two scenarios per class before proceeding. Write the scenario names only
(no analysis yet). If fewer than two scenarios exist for a class, expand the topic scope or
flag the class as architecturally absent.

**Phase 2 — Four-Field Analysis Table**

For each scenario, complete one row of the following table. Every cell is mandatory — a dash
or "N/A" is not acceptable; rephrase or split the scenario if a field has no meaningful content.

| Scenario | Class | State | Capability | Data-at-Risk | Recovery |
|----------|-------|-------|------------|--------------|----------|

Column definitions:

- **Scenario**: Named scenario identifier (e.g., "Payment-503-During-Checkout")
- **Class**: One of: Offline / Partial-Failure / Eventual-Consistency
- **State**: The degraded system condition — which services are affected and how
- **Capability**: What the user can still accomplish; what is blocked vs. degraded
- **Data-at-Risk**: The specific data object(s) and failure mode (lost / stale / inconsistent / duplicated)
- **Recovery**: Ordered steps to return to healthy state; each step prefixed with its actor
  in brackets — [client], [server], [operator], [user]

The table must contain at least six rows total (minimum two per class).

**Phase 3 — Gap Findings**

Below the table, produce three labeled finding sections. Each finding must reference a specific
scenario or data object from Phase 2 by name.

**Offline Experience Gaps**

List each gap as: `OEG-NN: [scenario name] — [what the user encounters that is unhandled]`

**Data Consistency Violations**

List each violation as: `DCV-NN: [data object] — [missing invariant or undetected divergence]`

**Missing Recovery Flows**

List each gap as: `MRF-NN: [scenario name] — [the recovery actor with no defined action]`

**Phase 4 — Conflict Resolution Adequacy**

For each Eventual-Consistency scenario, produce one entry:

```
Scenario: [name]
Strategy: [last-write-wins | merge | manual-reconcile | reject-stale | none]
Adequate for [data type]: [yes / no — rationale in one sentence]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-03 — Lifecycle Emphasis: Pre-Classification Gate

**Variation axis**: Lifecycle emphasis
**Hypothesis**: An explicit pre-classification phase — where the model commits to populating
scenario slots for all three degradation classes before writing any analysis — prevents late
coverage collapse. Without a pre-scan, models tend to write one class in depth and then run
out of momentum or conclude the analysis. The classification gate creates a visible contract
at the top of the output that a reviewer can check without reading the full artifact.

---

You are a Commerce / distributed systems domain expert. Simulate how the commerce system
described by the topic behaves under degraded conditions.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Gate 0 — Coverage Contract

Before writing any analysis, declare your coverage plan. Fill in the scenario roster:

```
DEGRADATION CLASS ROSTER
========================
Class A — Offline / Network Partition
  A-01: [scenario name]
  A-02: [scenario name]
  A-03: [optional]

Class B — Partial Service Failure
  B-01: [scenario name]
  B-02: [scenario name]
  B-03: [optional]

Class C — Eventual Consistency / Split-Brain
  C-01: [scenario name]
  C-02: [scenario name]
  C-03: [optional]
```

Rules for Gate 0:
- Every slot you leave blank is a coverage gap you are declaring intentionally
- Every slot must be a named, commerce-grounded scenario (not "TBD" or "generic failure")
- You may not proceed to Gate 1 until every class has at least two slots filled
- If a class genuinely has no applicable scenarios for this topic, state why in one sentence
  and note it as an architecture finding

---

### Gate 1 — Scenario Analysis

For each scenario declared in Gate 0, produce the four mandatory fields.

**[Scenario ID]: [Scenario Name]**

- **State**: What degraded condition is the system in? Which services, which data stores,
  which network segments are affected? Name the failure precisely.
- **Capability**: What can the user still do? Name each commerce operation that remains
  available. Name each that is blocked. Name each that is degraded (slower, unreliable, or
  read-only).
- **Data at risk**: What specific data objects may be lost, stale, inconsistent, or duplicated?
  For each: name the object, the failure mode, and the scope (per-user, per-session, global).
- **Recovery path**: How does the system return to healthy state? Write each step on its own
  line. Prefix each step with the actor who initiates it: [client] / [server] / [operator] /
  [user]. Include the trigger condition (what causes each step to fire) and the observable
  signal that it succeeded.

---

### Gate 2 — Gap Identification

Review all Gate 1 outputs. Produce findings in three sections. A finding that spans multiple
scenarios must appear in each applicable section, not bundled.

**Offline Experience Gaps** (label each: OEG-NN)
What does the user encounter during Class A scenarios that the design does not handle
gracefully? Focus on: missing local state, unhelpful error messages, silent data loss,
and absent retry affordances.

**Data Consistency Violations** (label each: DCV-NN)
Where does the data model lack the invariants to detect or resolve inconsistency after a
partition heals? Name the data object and the specific invariant that is absent.

**Missing Recovery Flows** (label each: MRF-NN)
Where does the system have no defined path back to healthy state? Identify the scenario,
the stuck recovery actor, and why no action is defined.

---

### Gate 3 — Conflict Resolution Review

For each Class C scenario, complete:

```
Scenario: [C-NN scenario name]
Conflict strategy: [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Data type: [what object is in conflict]
Adequacy verdict: [adequate / inadequate]
Rationale: [one sentence — why this strategy does or does not preserve the invariants
            for this data type]
```

Flag each "inadequate" verdict as an additional DCV finding.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-04 — Combination: DS Expert First + Scenario Table

**Variation axes**: Role sequence + Output format
**Hypothesis**: The DS expert role sequence enforces technical correctness (C-04) by anchoring
the scenario catalog in failure-mode theory before commerce context is applied. The scenario
table enforces structural completeness (C-02) and makes degradation-class coverage (C-01)
visible. These two axes are compatible: the DS expert generates the scenario catalog; the table
is the format for the four-field analysis that follows. Together they address the two most
commonly co-occurring failure modes: technically incorrect scenarios that look complete, and
technically correct scenarios that are missing analysis fields.

---

You are operating in two roles. Begin as the distributed systems expert. Transition to the
commerce domain expert when instructed.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Role 1 — Distributed Systems Expert: Failure Mode Catalog

Map the architecture implied by the topic to its failure envelope. For each degradation class,
enumerate the failure modes that the architecture cannot avoid:

**Class A — Offline / Network Partition**
- What partition scenarios does this topology expose? (Client-to-service, service-to-service,
  database replica lag becoming unbounded.)
- Which consistency guarantees dissolve under partition, per CAP?
- What retry semantics are required for idempotent vs. non-idempotent operations?

**Class B — Partial Service Failure**
- Which dependency failures cause the most blast radius? (Payment service down vs. search
  service down — different severity.)
- Which partial failures are invisible to the client until a downstream operation fails?
- Which operations must degrade gracefully vs. fail fast?

**Class C — Eventual Consistency / Split-Brain**
- Which data objects are replicated? Which have conflicting-write risk?
- What is the expected convergence lag under normal conditions? Under high-write load?
- Which conflict resolution strategies are implied by the data type semantics?
  (Inventory counts are additive; user preferences are last-write; order state is a state machine.)

Produce a preliminary scenario list with a DS expert confidence note for each:

```
Scenario: [name]
Class: [A / B / C]
DS confidence: [high / medium / low — one sentence reason]
Commerce grounding needed: [yes / no]
```

Exclude any scenario with low confidence from the analysis table unless the topic signal
explicitly references that failure mode.

---

### Role 2 — Commerce Domain Expert: Analysis Table

Ground each DS-cataloged scenario in a specific commerce flow. Scenarios that cannot be mapped
to a named commerce operation (checkout, cart, inventory reservation, payment processing,
order fulfillment, loyalty redemption) are out of scope for this artifact.

Complete the analysis table. Every cell is mandatory.

| Scenario | Class | Commerce Flow | State | Capability | Data-at-Risk | Recovery |
|----------|-------|---------------|-------|------------|--------------|----------|

Column notes:
- **Commerce Flow**: the named commerce operation this scenario disrupts (be specific: not
  "checkout" but "checkout — payment capture step")
- **State**: precise failure description (which services, which replicas, which network segments)
- **Capability**: explicit blocked / degraded / unaffected split for user-visible operations
- **Data-at-Risk**: named data object + failure mode (lost / stale / inconsistent / duplicated)
- **Recovery**: actor-prefixed steps — [client] retries with back-off; [server] surfaces
  reconcile UI; [operator] manually resolves stuck order; [user] re-enters payment

Minimum table size: six rows (two per class).

---

### Gap Identification

**Offline Experience Gaps** — `OEG-NN: [scenario] — [unhandled user encounter]`

**Data Consistency Violations** — `DCV-NN: [data object] — [missing invariant]`

**Missing Recovery Flows** — `MRF-NN: [scenario] — [actor with no defined action]`

---

### Conflict Resolution Adequacy

```
Scenario: [Class C scenario]
Strategy: [named strategy]
Data type: [object in conflict]
Adequate: [yes / no — one sentence]
```

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`

---

## V-05 — Combination: Scenario Table + Pre-Classification Gate + Conversational Register

**Variation axes**: Output format + Lifecycle emphasis + Phrasing register
**Hypothesis**: Conversational phrasing lowers the abstraction barrier for commerce-domain
scenario generation. "What could a shopper still do?" surfaces better user-capability analysis
than "enumerate user capabilities in the degraded state." The table format then structures that
conversational discovery into a rigid schema (enforcing C-02). The pre-classification gate
prevents the conversational register from causing coverage drift — the model commits to three
class labels before any analysis begins.

---

You are a senior commerce engineer who has been on-call for a high-traffic retail platform.
You know from experience how things fail. Your job is to walk through the failure scenarios
that matter for this system.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### First: claim your scenarios

Before any analysis, decide what you are going to cover. Fill in the roster below. Think
about what actually goes wrong on a busy platform — not theoretical failures, but the ones
that page you at 2am.

```
SCENARIO ROSTER
===============
Offline / Network Partition (need at least 2):
  1. _______________________________________________
  2. _______________________________________________
  3. (optional) ____________________________________

Partial Service Failure (need at least 2):
  1. _______________________________________________
  2. _______________________________________________
  3. (optional) ____________________________________

Eventual Consistency / Split-Brain (need at least 2):
  1. _______________________________________________
  2. _______________________________________________
  3. (optional) ____________________________________
```

If you can't fill in two slots for a class — really think about why. Is the system genuinely
not vulnerable there? Or is the topic scoped in a way that hides the risk? Either answer is
valid, but you have to state it.

---

### Then: work through each scenario

For each scenario in your roster, fill out the table row. Be specific — "payment service is
down" is not specific enough. Name the exact operation that is disrupted, name the data object
that is at risk, and name who actually does each step in the recovery sequence.

| Scenario | Class | State | What can the shopper still do? | What data is at risk? | Recovery (who does what, in order) |
|----------|-------|-------|-------------------------------|----------------------|-------------------------------------|

A few things that make rows useful vs. useless:

- **State**: "503 from payment service; cart service healthy; inventory cache stale by up to
  30s" is useful. "System is degraded" is not.
- **Shopper capability**: "Can browse and add to cart; cannot complete checkout; gift card
  balance visible but cannot be applied" is useful. "Limited functionality" is not.
- **Data at risk**: "Cart contents lost if session token expires during partition (no local
  persistence)" is useful. "Data may be lost" is not.
- **Recovery**: "[client] polls every 30s with exponential back-off; [server] queues payment
  capture for retry; [operator] monitors dead-letter queue and manually triggers reconcile
  if queue depth exceeds threshold" is useful. "System recovers automatically" is not.

Minimum: six rows, with at least two in each class column.

---

### Then: name the gaps

Review your table. For each of the three finding types, list what you found. If you found
nothing in a category, say so explicitly and explain why — "no offline experience gaps because
the product is server-side rendered with no client state" is a valid finding.

**Offline experience gaps** (OEG-NN)
What happens to the user during a network partition that the design doesn't handle well?
Think: blank screens, spinner that never resolves, silent data loss, no way to get their
cart back.

**Data consistency violations** (DCV-NN)
Where does the system not have the machinery to detect or resolve inconsistency after
things come back? Think: inventory oversell, duplicate orders, stale loyalty balances.

**Missing recovery flows** (MRF-NN)
Where does the system just... not have a path back? No retry, no reconcile UI, no operator
runbook step. Name the scenario and the actor who would need to act but has no defined action.

---

### Finally: think about the split-brain scenarios

For each eventual-consistency scenario in your table, answer:

> When two replicas disagree, which one wins — and is that the right choice?

```
Scenario: [name]
What's in conflict: [data object]
Who wins (or what strategy): [last-write-wins / merge / manual-reconcile / reject-stale / undefined]
Is that right for this data?: [yes / no]
Why it matters: [one sentence — what goes wrong if the strategy is wrong]
```

If the strategy is "undefined" or "no" — add it as a DCV finding.

**Output artifact**: `simulations/flow/resilience/{{topic}}-resilience-{{date}}.md`
