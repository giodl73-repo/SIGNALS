Written to `simulations/quest/variations/flow-resilience-variations-R2-2026-03-14.md`.

---

## Round 2 Summary

| Variation | Axis | Target criteria | Hypothesis |
|-----------|------|-----------------|------------|
| **V-01** | Chaos test block per scenario | C-09 | Pre-printed injection/expected/pass/fail table after Classification block — model fills, doesn't design |
| **V-02** | Per-finding observability hook | C-10 | Inline `metric / alert / owner` on every GAP/DCV/MRF entry — can't omit by section-collapsing |
| **V-03** | Resilience contract (integrated) | C-09, C-10 | Merges chaos + observability into one extended table per scenario — tests whether integration reduces section-skip risk vs. separate appendage blocks |
| **V-04** | Combined: chaos + observability | C-09, C-10 | V-01 + V-02 on the V-05 R1 golden base — targets both missing aspirational criteria without structural conflict |
| **V-05** | Full aspirational scaffold | C-09–C-13 | V-04 + actor-chain as template label, conflict vocabulary as constrained-choice field, "3 of 3" completeness marker as fill-in — all five aspirational criteria are fills, zero format design left to the model |

**Ceiling analysis**: V-05 R1 scores ~96/100 under v2 rubric (C-11/12/13 already implicit). V-04 R2 should push to ~100. V-05 R2 makes the implicit explicit — the completeness marker in Section 4 appears in the output itself, satisfying C-13's "marker must appear in the output itself, not only in the prompt instruction" pass condition.
Round 2 single-axis variations explore three distinct integration patterns for those criteria (per-scenario block, per-finding field, integrated extension). Round 2 V-04 and V-05 combine them — V-05 closes the remaining gap by making all aspirational criteria structural fills rather than model design choices.

**Important**: All Round 2 variations preserve the V-05 Round 1 blocking mechanisms — (1) pre-printed four-field table, (2) ops-first role sequence, (3) "mandatory — do not omit or merge" Section 4. These are the foundation; Round 2 adds on top of them.

---

## V-01 — Chaos Engineering Test Block Per Scenario

**Axis**: Output format — per-scenario chaos test table appended after Classification block
**Hypothesis**: A pre-printed chaos test table (injection / expected behavior / pass signal / fail
signal) appended after each scenario's Classification block forces C-09 compliance without
relaxing any of V-05's essential or recommended constraints. The model fills a template rather
than designing the chaos test structure — following the same fill-vs-design principle that made
the four-field trace table effective in Round 1.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**

Run roles in this order. Each role contributes to the same output sections — do not produce
separate documents per role.

1. **Store Operations SME** — speaks first in every scenario. Describes what the cashier, shift
   manager, and customer experience from the floor. Does not speculate about system internals.
   Does identify operational workarounds, manual steps, and human impact.

2. **Commerce Developer** — speaks second in every scenario. Validates or corrects the SME
   account, adds technical detail, fills in the four-field trace table, and writes the chaos
   test block.

---

### Section 1 — Offline / Network Loss Scenario

**SME account** (1–3 short paragraphs):
What does the floor experience? What does the cashier do? What do customers see?
What operations stop? What workarounds appear?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | [failure injected and how — e.g., drop network interface at OS level, block DNS, kill connectivity mid-transaction] |
| Expected behavior| [what the system should do: queue locally, show degraded-mode UI, reject with user-visible error, etc.] |
| Pass signal      | [observable outcome confirming correct behavior — log event, UI state, metric value, queue depth] |
| Fail signal      | [observable outcome indicating a gap — data loss, silent failure, incorrect state, blocking error with no recovery] |

---

### Section 2 — Partial Service Failure Scenario

Choose the dependency most critical to `{topic}`'s commerce operations (pricing service, loyalty
service, inventory service, payment gateway). That service is now returning 503s or timing out.

**SME account** (1–3 short paragraphs):
Does the cashier know? What do they tell customers? What is escalated?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | [how to inject the dependency failure — e.g., block the service endpoint, return 503 after N requests, inject artificial latency above circuit-breaker threshold] |
| Expected behavior| [what the system should do — circuit-break and cache last-known price, fall back to zero-loyalty mode, etc.] |
| Pass signal      | [observable outcome confirming graceful degradation] |
| Fail signal      | [observable outcome indicating a gap — transaction blocked, incorrect fallback applied, error not surfaced to user] |

---

### Section 3 — Eventual Consistency Conflict Scenario

Simulate a state conflict: two writes to the same record occurred in different partitions during
the offline or failure window (e.g., cross-store refund, dual-write inventory decrement, stale
price applied to offline transaction).

**SME account** (1–3 short paragraphs):
What does the reconciliation screen look like to the shift manager? What is the escalation path
if they cannot resolve it?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Conflict resolution**:
State the strategy in use: `last-write-wins | merge | manual-reconcile | reject-stale`.
Assess whether that strategy is adequate for the record type involved. If not adequate, name
the failure mode.

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | [how to reproduce the conflict — e.g., take two nodes offline independently, write conflicting state to each, reconnect simultaneously] |
| Expected behavior| [how conflict detection and resolution should proceed — which system component detects, how operator is notified, what the resolution UI offers] |
| Pass signal      | [observable outcome confirming correct conflict resolution — record in correct final state, audit log entry, operator notification sent] |
| Fail signal      | [observable outcome indicating a gap — silent merge error, incorrect winner, operator not notified, record left in split state] |

---

### Section 4 — Gap Identification (mandatory — do not omit or merge with scenarios)

This section is separate from the scenarios. Each subsection must name specific, actionable
findings — not generic observations.

**Offline Experience Gaps**

For each gap: name the operation, describe what the user must do instead, and state whether
the workaround creates downstream data problems.

- GAP-01: [name] — [description] — [downstream risk]
- GAP-02: ...

(minimum one; add as many as found)

**Data Consistency Violations**

For each violation: name the record type, describe the inconsistency, state whether it is
detectable before customer impact.

- DCV-01: [record] — [inconsistency] — [detectability]
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the current manual workaround, estimate
frequency × impact.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
- MRF-02: ...

(minimum one)

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Return the file path when done.

---

## V-02 — Per-Finding Observability Hook

**Axis**: Output format — observability field (`metric / alert / owner`) attached to each
numbered finding in Section 4
**Hypothesis**: Requiring a named metric, alert condition, and owning role for every GAP, DCV,
and MRF finding forces each finding to be anchored to a detectable system state (C-10) and
improves C-03 finding specificity in the process. The hook is inline per finding rather than
a separate section — so it cannot be omitted by collapsing sections.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**

Run roles in this order.

1. **Store Operations SME** — speaks first in every scenario. Describes the floor experience,
   cashier behavior, customer impact, and manual workarounds. Does not speculate about system
   internals.

2. **Commerce Developer** — speaks second in every scenario. Validates or corrects the SME
   account, fills in the four-field trace table, classifies severity and blast radius, and adds
   the observability hook to each finding in Section 4.

---

### Section 1 — Offline / Network Loss Scenario

**SME account** (1–3 short paragraphs):
What does the floor experience? What does the cashier do? What do customers see?
What operations stop? What workarounds appear?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

---

### Section 2 — Partial Service Failure Scenario

Choose the dependency most critical to `{topic}`'s commerce operations (pricing service, loyalty
service, inventory service, payment gateway). That service is now returning 503s or timing out.

**SME account** (1–3 short paragraphs):
Does the cashier know? What do they tell customers? What is escalated?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

---

### Section 3 — Eventual Consistency Conflict Scenario

Simulate a state conflict: two writes to the same record occurred in different partitions during
the offline or failure window (e.g., cross-store refund, dual-write inventory decrement, stale
price applied to offline transaction).

**SME account** (1–3 short paragraphs):
What does the reconciliation screen look like to the shift manager? What is the escalation path
if they cannot resolve it?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Conflict resolution**:
State the strategy in use: `last-write-wins | merge | manual-reconcile | reject-stale`.
Assess whether that strategy is adequate for the record type involved. If not adequate, name
the failure mode.

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

---

### Section 4 — Gap Identification (mandatory — do not omit or merge with scenarios)

This section is separate from the scenarios. Each finding must include an observability hook:
the metric that would surface this gap in a live system, the alert condition that fires, and
the team or role that owns the alert.

**Offline Experience Gaps**

For each gap: name the operation, describe what the user must do instead, state whether the
workaround creates downstream data problems, and add the observability hook.

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[metric name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one; add as many as found)

**Data Consistency Violations**

For each violation: name the record type, describe the inconsistency, state detectability,
and add the observability hook.

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[metric name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the current manual workaround, estimate
frequency × impact, and add the observability hook that would indicate the manual flow is
running when it should be automated.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[metric name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Return the file path when done.

---

## V-03 — Resilience Contract as Integrated Scenario Extension

**Axis**: Lifecycle emphasis — chaos test and observability hook merged into an extended
scenario table ("Resilience contract") rather than separate sections
**Hypothesis**: Integrating chaos and observability into the scenario structure itself rather
than adding them as separate appendage sections produces tighter coupling between the scenario
and its test/observable properties — each scenario becomes a self-contained resilience contract.
The integration test: does merging them into one table per scenario reduce section-skip risk
(C-09, C-10) while preserving the four-field structure (C-02)?

---

You are a **Commerce / Distributed Systems domain expert** running a resilience simulation
for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

Each failure scenario in this simulation is a **resilience contract**: a statement of failure
conditions, system behavior, data risk, recovery path, testability, and observability. Every
scenario must produce a complete contract — no field may be omitted.

---

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely for a sustained period during active commerce
operations. Specify: detection latency, which operations continue locally, which fail
immediately, and what is queued vs. discarded.

**Resilience contract**:

| Contract field   | Content |
|------------------|---------|
| State            | [system state at point of failure — what is cached, what is lost, what is unknown] |
| Capability       | [operations the cashier / customer / operator can still perform, with limitations] |
| Data at risk     | [records that may be lost, stale, or in an inconsistent state — named specifically] |
| Recovery         | [client → server → operator → user: ordered actor-labeled step sequence] |
| Chaos injection  | [how to reproduce: what to break, at which layer, for how long] |
| Expected outcome | [what correct system behavior looks like during this failure] |
| Pass signal      | [metric / log event / UI state confirming correct behavior] |
| Fail signal      | [observable outcome that would indicate a gap and trigger a finding] |
| Observability    | `metric=[name]` | `alert=[condition]` | `owner=[role]` |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

---

### Scenario 2 — Dependent Service Unavailable

One downstream service critical to `{topic}`'s commerce operations is returning 503s or
timing out. Name the specific service (pricing, loyalty, inventory, payment gateway).

**Resilience contract**:

| Contract field   | Content |
|------------------|---------|
| State            | |
| Capability       | |
| Data at risk     | |
| Recovery         | [client → server → operator → user: ordered actor-labeled step sequence] |
| Chaos injection  | [how to inject: endpoint block, latency spike, error rate injection, kill signal] |
| Expected outcome | [circuit-breaker behavior, fallback mode, degraded-service indicator] |
| Pass signal      | |
| Fail signal      | |
| Observability    | `metric=[name]` | `alert=[condition]` | `owner=[role]` |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

---

### Scenario 3 — Eventual Consistency Conflict

Two writes to the same record occurred in different partitions during the offline or failure
window. Name the record type, the partition boundary, and the conflict-producing operation.

**Resilience contract**:

| Contract field       | Content |
|----------------------|---------|
| State                | |
| Capability           | |
| Data at risk         | |
| Recovery             | [client → server → operator → user: ordered actor-labeled step sequence] |
| Conflict resolution  | [strategy: `last-write-wins \| merge \| manual-reconcile \| reject-stale` — assess adequacy] |
| Chaos injection      | [how to produce the conflict: dual-partition write sequence] |
| Expected outcome     | [how conflict is detected, surfaced, and resolved] |
| Pass signal          | |
| Fail signal          | |
| Observability        | `metric=[name]` | `alert=[condition]` | `owner=[role]` |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

---

### Section 4 — Gap Identification (mandatory — do not omit or merge with scenarios)

The scenarios above surface failure behavior. This section names the gaps — operations,
records, and flows that the system does not handle adequately. Each gap is a distinct finding.

**Offline Experience Gaps**

For each gap: name the operation, describe the user's forced workaround, state downstream risk.

- GAP-01: [name] — [description] — [downstream risk]
- GAP-02: ...

(minimum one)

**Data Consistency Violations**

For each violation: name the record, describe the inconsistency, state detectability
(before / only after customer impact).

- DCV-01: [record] — [inconsistency] — [detectability]
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the current manual workaround,
estimate frequency × impact.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
- MRF-02: ...

(minimum one)

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Return the file path when done.

---

## V-04 — Combined: Chaos Per Scenario + Observability Per Finding

**Axis**: Combined — per-scenario chaos test block (V-01 axis) + per-finding observability
hook (V-02 axis) added to V-05 Round 1 base
**Hypothesis**: The two mechanisms target different rubric criteria without structural conflict:
chaos blocks are per-scenario and owned by the Commerce Developer role; observability hooks
are per-finding and inline in Section 4. The combination can push the composite from ~96 to
~100 under v2 scoring without introducing the section-skip risk that separate appendage
sections would create.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**

Run roles in this order. Each role contributes to the same output sections — do not produce
separate documents per role.

1. **Store Operations SME** — speaks first in every scenario. Describes the floor experience,
   cashier behavior, customer impact, and manual workarounds. Does not speculate about system
   internals.

2. **Commerce Developer** — speaks second in every scenario. Validates or corrects the SME
   account, fills in the four-field trace table, writes the chaos test block, classifies
   severity and blast radius, and adds observability hooks to Section 4 findings.

---

### Section 1 — Offline / Network Loss Scenario

**SME account** (1–3 short paragraphs):
What does the floor experience? What does the cashier do? What do customers see?
What operations stop? What workarounds appear?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | [failure injected and how — e.g., drop network interface at OS level, block DNS, kill connectivity mid-transaction] |
| Expected behavior| [what the system should do: queue locally, show degraded-mode indicator, reject with user-visible error] |
| Pass signal      | [observable outcome confirming correct behavior — log event, UI state, metric value, queue depth] |
| Fail signal      | [observable outcome indicating a gap — data loss, silent failure, incorrect state, blocking error with no recovery] |

---

### Section 2 — Partial Service Failure Scenario

Choose the dependency most critical to `{topic}`'s commerce operations (pricing service, loyalty
service, inventory service, payment gateway). That service is now returning 503s or timing out.

**SME account** (1–3 short paragraphs):
Does the cashier know? What do they tell customers? What is escalated?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | [how to inject the dependency failure — block the service endpoint, return 503 after N requests, inject artificial latency above circuit-breaker threshold] |
| Expected behavior| [what the system should do — circuit-break and serve cached data, fall back to zero-loyalty mode, reject with specific error code] |
| Pass signal      | [observable outcome confirming graceful degradation] |
| Fail signal      | [observable outcome indicating a gap — transaction blocked, incorrect fallback applied, error not surfaced] |

---

### Section 3 — Eventual Consistency Conflict Scenario

Simulate a state conflict: two writes to the same record occurred in different partitions during
the offline or failure window (e.g., cross-store refund, dual-write inventory decrement, stale
price applied to offline transaction).

**SME account** (1–3 short paragraphs):
What does the reconciliation screen look like to the shift manager? What is the escalation path
if they cannot resolve it?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | [client → server → operator → user: step-by-step actor-labeled sequence] |

**Conflict resolution**:
State the strategy in use: `last-write-wins | merge | manual-reconcile | reject-stale`.
Assess whether that strategy is adequate for the record type involved. If not adequate, name
the failure mode.

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | [how to reproduce the conflict — take two nodes offline independently, write conflicting state to each, reconnect simultaneously] |
| Expected behavior| [how conflict detection and resolution should proceed — which component detects, how operator is notified, what resolution UI offers] |
| Pass signal      | [observable outcome confirming correct conflict resolution — record in correct final state, audit log entry, operator notification sent] |
| Fail signal      | [observable outcome indicating a gap — silent merge error, wrong winner selected, record left in split state] |

---

### Section 4 — Gap Identification (mandatory — do not omit or merge with scenarios)

This section is separate from the scenarios. Each finding must include an inline observability
hook. The hook names the metric that surfaces the gap, the alert condition that fires, and the
owning role. Do not defer the observability hook to a separate section.

**Offline Experience Gaps**

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[metric name]` | `alert=[condition]` | `owner=[team or role]`
- GAP-02: ...

(minimum one; add as many as found)

**Data Consistency Violations**

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[metric name]` | `alert=[condition]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[metric name]` | `alert=[condition]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Return the file path when done.

---

## V-05 — Full Aspirational Scaffold (all five criteria structurally embedded)

**Axis**: Combined — V-04 base (chaos + observability) + explicit C-11/C-12/C-13 structural
markers in the output template itself
**Hypothesis**: V-05 Round 1 implicitly satisfies C-11/C-12/C-13 but they rely on instruction
compliance rather than output structure. Making all five aspirational criteria fill-in slots
(actor-chain notation as a template label not just an instruction, constrained vocabulary as a
bracketed choice not just a list to reference, and a "3 of 3 complete" output marker in Section
4) eliminates the last model-design decisions from the prompt. Every field in the output is
either fill-in or constrained-choice — the model can reach 100 without exercising any structural
creativity at all.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**

Run roles in this order. Each role contributes to the same output sections — do not produce
separate documents per role.

1. **Store Operations SME** — speaks first in every scenario. Describes the floor experience,
   cashier behavior, customer impact, and manual workarounds. Does not speculate about system
   internals.

2. **Commerce Developer** — speaks second in every scenario. Validates or corrects the SME
   account, fills every table field, selects from constrained-choice fields, and writes all
   actor-chain labels using the canonical notation.

**Actor chain notation** (use in all Recovery fields): `client →` | `server →` | `operator →` | `user →`
Each step in a Recovery field must begin with one of these four labels. Do not describe actor
actions in prose — use the actor chain as a step prefix.

**Conflict resolution vocabulary** (use in all Conflict resolution fields):
`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one term per strategy reference. Do not paraphrase.

---

### Section 1 — Offline / Network Loss Scenario

**SME account** (1–3 short paragraphs):
What does the floor experience? What does the cashier do? What do customers see?
What operations stop? What workarounds appear?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | client → [action] / server → [action] / operator → [action] / user → [action] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | |
| Expected behavior| |
| Pass signal      | |
| Fail signal      | |

**Observability** (for this scenario):
`scenario-metric=[name]` | `alert=[condition]` | `owner=[role]`

---

### Section 2 — Partial Service Failure Scenario

Choose the dependency most critical to `{topic}`'s commerce operations (pricing service, loyalty
service, inventory service, payment gateway). That service is now returning 503s or timing out.

**SME account** (1–3 short paragraphs):
Does the cashier know? What do they tell customers? What is escalated?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | client → [action] / server → [action] / operator → [action] / user → [action] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | |
| Expected behavior| |
| Pass signal      | |
| Fail signal      | |

**Observability** (for this scenario):
`scenario-metric=[name]` | `alert=[condition]` | `owner=[role]`

---

### Section 3 — Eventual Consistency Conflict Scenario

Simulate a state conflict: two writes to the same record occurred in different partitions during
the offline or failure window (e.g., cross-store refund, dual-write inventory decrement, stale
price applied to offline transaction).

**SME account** (1–3 short paragraphs):
What does the reconciliation screen look like to the shift manager? What is the escalation path
if they cannot resolve it?

**Developer four-field trace**:

| Field        | Content |
|--------------|---------|
| State        | |
| Capability   | |
| Data at risk | |
| Recovery     | client → [action] / server → [action] / operator → [action] / user → [action] |

**Conflict resolution**:
Strategy in use (select one): `last-write-wins | merge | manual-reconcile | reject-stale`
→ Selected: ___________
→ Adequacy assessment: [adequate / inadequate — if inadequate, name the failure mode]

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field            | Content |
|------------------|---------|
| Injection        | |
| Expected behavior| |
| Pass signal      | |
| Fail signal      | |

**Observability** (for this scenario):
`scenario-metric=[name]` | `alert=[condition]` | `owner=[role]`

---

### Section 4 — Gap Identification

**Completeness marker — fill before writing artifact**:
```
[ ] GAP subsection present (≥1 finding)
[ ] DCV subsection present (≥1 finding)
[ ] MRF subsection present (≥1 finding)
Finding types present: ___ of 3
```

Do not write the artifact until all three boxes are checked and "Finding types present: 3 of 3"
is confirmed. Do not merge gap types into a single section.

**Offline Experience Gaps**

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition]` | `owner=[role]`
- GAP-02: ...

(minimum one)

**Data Consistency Violations**

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition]` | `owner=[role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition]` | `owner=[role]`
- MRF-02: ...

(minimum one)

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Include the Section 4 completeness marker in the artifact with all three boxes checked and
"Finding types present: 3 of 3" confirmed. Return the file path when done.
