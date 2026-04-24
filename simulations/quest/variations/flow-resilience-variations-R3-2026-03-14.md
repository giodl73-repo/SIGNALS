Written to `simulations/quest/variations/flow-resilience-variations-R3-2026-03-14.md`.

---

## Round 3 Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format — full single-table contract | V-03 R2's integration (chaos rows inside the table) + V-05 R2's per-finding hooks + output checklist, all in one compact structure — the Round 3 target |
| **V-02** | Role sequence — chaos engineer first | Chaos engineer defines injection/expected/pass/fail before SME grounds it in floor operations; more technically precise chaos blocks without SME framing contamination |
| **V-03** | Lifecycle emphasis — three explicit phases with gates | Phase gating prevents gap identification collapse; checklist becomes a mandatory Phase 3 certification gate, not a trailing element |
| **V-04** | Combined: single-table + chaos-first roles | Role-specific row ownership inside one table (SME owns rows 1–4, Chaos Eng owns rows 5–10) sequences both roles' contributions without structural ambiguity |
| **V-05** | Combined: single-table + phase gates + imperative phrasing | Structural integration + phase gating + imperative micro-commands co-located at each slot — maximum constraint, minimum structural creativity left to the model |

---

## Key design decisions for Round 3

**Why V-01 is the primary target**: V-03 R2 scored ~98.75 under v3 because its per-scenario observability row doesn't satisfy C-15 (which requires per-finding inline hooks) and it has no output checklist (C-16). V-01 corrects both while keeping V-03 R2's strongest property — chaos rows are *inside* the contract table, so there is no section boundary at which the model can defer or omit them.

**Why V-02 is worth testing**: Every prior variation uses SME-first or single-expert framing. The hypothesis is that chaos-engineer-first produces more technically rigorous injection methods. The risk is C-05 (commerce grounding) becoming thinner — the SME's floor account follows the Chaos Engineer's framing rather than setting it.

**Why V-03's phase gates are distinct**: Prior variations co-locate chaos with the scenario and observability with the finding, but both Section 4 and the checklist are still presented as trailing requirements that can be collapsed. Explicit phase gates with named stop conditions make them mandatory stops, not optional appendages.

**V-04 and V-05 structural bets**: V-04 tests whether the "owned by" column in the contract table removes role confusion without adding commentary overhead. V-05 tests whether imperative micro-commands placed immediately before each slot ("Write row 7 now. Do not advance to Scenario 2 until row 10 is filled.") reduce structural omission beyond what co-location and phase gating achieve alone.
lation
for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

Each failure scenario is a single resilience contract table. The four-field trace, severity,
blast radius, chaos test, and conflict resolution are all rows in the same table. Fill every
row. Do not split the table into sub-tables. Do not move chaos rows to a separate section.

**Actor chain notation** (use in all Recovery rows):
`client →` | `server →` | `operator →` | `user →`
Each step must begin with one of these four labels.

**Conflict resolution vocabulary** (use in Scenario 3 row 5 only):
`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one. Do not paraphrase.

---

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations. Specify
which operations continue locally, which fail immediately, and what is queued vs. discarded.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | [system state at point of failure: what is cached, what is lost, what is unknown] |
| 2 | Capability | [what the cashier / customer / operator can still do, with specific named limitations] |
| 3 | Data at risk | [named records that may be lost, stale, or inconsistent — not generic "transaction data"] |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | [scope and population affected] |
| 7 | Chaos injection | [how to reproduce: what to break, at which layer, for how long — e.g., drop network interface at OS level, block DNS mid-transaction] |
| 8 | Expected behavior | [what correct system behavior looks like — queue locally, surface degraded-mode indicator, reject with user-visible error, fail-open vs. fail-closed] |
| 9 | Pass signal | [observable outcome confirming correct behavior — log event, UI state, metric value, queue depth] |
| 10 | Fail signal | [observable outcome indicating a gap — data loss, silent failure, incorrect state, blocking error with no recovery path] |

---

### Scenario 2 — Dependent Service Unavailable

One downstream service critical to `{topic}`'s commerce operations is returning 503s or
timing out. Name the specific service (pricing, loyalty, inventory, payment gateway).

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | |
| 7 | Chaos injection | [how to inject: block the service endpoint, return 503 after N requests, inject artificial latency above circuit-breaker threshold] |
| 8 | Expected behavior | [circuit-break and serve cached fallback, degrade to zero-loyalty mode, surface specific error with recovery guidance] |
| 9 | Pass signal | |
| 10 | Fail signal | |

---

### Scenario 3 — Eventual Consistency Conflict

Two writes to the same record occurred in different partitions during the offline or failure
window. Name the record type, the partition boundary, and the conflict-producing operation.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` → Selected: ___ → Adequacy: [adequate / inadequate — if inadequate, name the failure mode this strategy produces for this record type] |
| 6 | Severity | [degraded / impaired / down] |
| 7 | Blast radius | |
| 8 | Chaos injection | [how to produce the conflict — take two nodes offline independently, write conflicting state to each, reconnect simultaneously; specify the conflicting write sequence] |
| 9 | Expected behavior | [how conflict detection proceeds — which component detects, how operator is notified, what the resolution UI offers] |
| 10 | Pass signal | [record in correct final state, audit log entry present, operator notification sent] |
| 11 | Fail signal | [silent merge error, wrong writer wins, record left in split state, operator not notified] |

---

### Section 4 — Gap Identification

(mandatory — do not omit or merge with scenarios)

Each finding carries an observability hook on the line immediately after the finding entry.
Do not collect hooks into a separate observability section.

**Offline Experience Gaps**

For each gap: name the operation, describe the forced workaround, state downstream risk.

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one; add as many as found)

**Data Consistency Violations**

For each violation: name the record, describe the inconsistency, state detectability
(before / only after customer impact).

- DCV-01: [record] — [inconsistency] — [detectability]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the current manual workaround,
estimate frequency x impact.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### Completeness Check

Include this block in the artifact. Fill all boxes and the count before writing the file.

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

Do not write the artifact until all three boxes are checked and the count reads "3 of 3".

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Include the Completeness Check block in the artifact with all three boxes checked and
"Finding types present: 3 of 3" confirmed. Return the file path when done.

---

## V-02 — Chaos-First Role Sequence (Role Sequence Axis)

**Axis**: Role sequence — Distributed Systems Chaos Engineer speaks first in every scenario,
defining failure injection and expected behaviors; Commerce SME speaks second, grounding the
technical failure in floor operations and business impact
**Hypothesis**: All prior variations (R1 and R2) use ops-first (SME leads) or single-expert
framing. A chaos-first sequence lets the chaos engineer define the exact failure mode before
the SME contextualizes it — producing more technically precise injection methods and pass/fail
signals uncontaminated by floor-level narrative. The SME still satisfies C-05 (commerce
grounding) but responds to the technical framing rather than originating it. The structural
compliance baseline (C-14, C-15, C-16) is preserved on the V-04 R2 scaffold.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**

Run roles in this order. Each role contributes to the same output sections — do not produce
separate documents per role.

1. **Distributed Systems Chaos Engineer** — speaks first in every scenario. Defines the
   exact failure mode, injection method, expected system behavior, and observable pass/fail
   signals. Assesses CAP theorem trade-offs, retry semantics, idempotency requirements, and
   conflict resolution strategy adequacy. Does not describe floor experience.

2. **Commerce Domain SME** — speaks second in every scenario. Takes the Chaos Engineer's
   failure definition as given and describes what it means on the floor: cashier experience,
   customer impact, manual workarounds, and business consequence. Fills the four-field trace
   table after the Chaos Engineer's block. Does not redesign the failure injection.

**Actor chain notation** (SME uses in Recovery fields):
`client →` | `server →` | `operator →` | `user →`

**Conflict resolution vocabulary** (Chaos Engineer uses in Scenario 3):
`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`

---

### Section 1 — Full Connectivity Loss Scenario

**Chaos Engineer speaks first** — define the failure:

Chaos injection: [exact failure injection — e.g., block all outbound TCP at the OS firewall,
drop DNS resolution, partition the network segment at the switch layer; specify layer and
duration]

Expected behavior: [what correct system behavior looks like — queue depth, local cache
behavior, degraded-mode surface, rejection semantics, fail-open vs. fail-closed]

Pass signal: [observable outcome confirming correct behavior — log event, metric value,
UI state, queue depth]

Fail signal: [observable outcome indicating a gap — silent data loss, blocking error with
no recovery path, incorrect state persisted]

---

**Commerce SME speaks second** — ground the technical failure:

[1-3 short paragraphs: what the cashier experiences, what customers see, what operations
are blocked, what manual workarounds appear on the floor, what the human escalation path is]

---

**Four-field trace** (SME fills from the floor account, constrained by Chaos Engineer's
failure definition):

| Field | Content |
|-------|---------|
| State | [system state at failure: what is cached, lost, unknown — from operations perspective] |
| Capability | [what the cashier / customer / operator can still do] |
| Data at risk | [named records at risk — receipts, offline basket, loyalty points, etc.] |
| Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test block** (appended immediately — do not move to a separate section):

| Field | Content |
|-------|---------|
| Injection | [from Chaos Engineer's definition above] |
| Expected behavior | [from Chaos Engineer's definition above] |
| Pass signal | [from Chaos Engineer's definition above] |
| Fail signal | [from Chaos Engineer's definition above] |

---

### Section 2 — Partial Service Failure Scenario

Name the specific dependent service (pricing, loyalty, inventory, payment gateway) most
critical to `{topic}`'s operations.

**Chaos Engineer speaks first** — define the failure:

Chaos injection: [how to inject — block the service endpoint at the proxy layer, return 503
after N requests, inject artificial latency above the circuit-breaker timeout threshold;
specify the injection point and the trigger condition]

Expected behavior: [circuit-break behavior, fallback data source, degraded-service indicator,
specific rejection code and user-visible message]

Pass signal: [observable outcome — circuit-breaker state change metric, fallback counter
fires, operator alert threshold crossed]

Fail signal: [transaction blocked without fallback, incorrect cached data applied, circuit
breaker not tripping within SLA, no operator visibility into degraded state]

---

**Commerce SME speaks second** — ground the technical failure:

[1-3 short paragraphs: does the cashier know the service is down? What do they tell
customers? What is escalated? What is the workaround while the service is unavailable?]

---

**Four-field trace**:

| Field | Content |
|-------|---------|
| State | |
| Capability | |
| Data at risk | |
| Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test block**:

| Field | Content |
|-------|---------|
| Injection | |
| Expected behavior | |
| Pass signal | |
| Fail signal | |

---

### Section 3 — Eventual Consistency Conflict Scenario

**Chaos Engineer speaks first** — define the failure:

Record type and partition boundary: [name the specific record and the partition that produced
the conflict — e.g., inventory count split across two regional nodes during a simultaneous
decrement]

Chaos injection: [how to reproduce — take two nodes offline independently, write conflicting
state to each, reconnect simultaneously; specify the conflicting write operations and the
reconnect timing window]

Conflict resolution strategy in use (select one):
`last-write-wins | merge | manual-reconcile | reject-stale` → Selected: ___
Adequacy assessment: [adequate / inadequate — if inadequate, name the specific failure mode
this strategy produces for this record type]

Expected behavior: [how conflict detection proceeds — which system component detects, what
notification is sent to the operator, what the resolution path is, how long until resolution]

Pass signal: [record in correct final state, audit log entry present, operator notified
within SLA]

Fail signal: [silent merge error, wrong writer wins, record left in split state, no operator
notification, audit log missing]

---

**Commerce SME speaks second** — ground the technical failure:

[1-3 short paragraphs: what does the reconciliation screen look like to the shift manager?
What is the escalation path if they cannot resolve it? What is the customer-visible impact
during the conflict window?]

---

**Four-field trace**:

| Field | Content |
|-------|---------|
| State | |
| Capability | |
| Data at risk | |
| Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test block**:

| Field | Content |
|-------|---------|
| Injection | |
| Expected behavior | |
| Pass signal | |
| Fail signal | |

---

### Section 4 — Gap Identification

(mandatory — do not omit or merge with scenarios)

Both roles contribute: Chaos Engineer names technical gaps in system behavior; Commerce SME
names operational gaps in the user experience. Every finding carries an inline observability
hook on the line immediately following the finding entry. Do not collect hooks into a
separate section.

**Offline Experience Gaps**

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one)

**Data Consistency Violations**

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### Completeness Check

Include this block in the artifact with all boxes checked and the count confirmed.

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Include the Completeness Check block in the artifact with all three boxes checked and
"Finding types present: 3 of 3" confirmed. Return the file path when done.

---

## V-03 — Three-Phase Lifecycle with Gates (Lifecycle Emphasis Axis)

**Axis**: Lifecycle emphasis — the prompt is structured as three explicit numbered phases,
each with a completion gate before advancing; chaos test is appended per scenario in Phase 1,
per-finding hooks are written in Phase 2, and the completeness checklist is filled and
certified in Phase 3 before the artifact is written
**Hypothesis**: All R1/R2 variations present all requirements simultaneously and rely on
instruction compliance to sequence them correctly. An explicit three-phase structure with
named gates prevents gap identification collapse (Phase 2 is a required stop, not an
appendage after the scenarios) and makes the checklist a mandatory certification gate rather
than a trailing element that can be omitted. The phase-gate mechanism is distinct from all
prior variations — it enforces sequence rather than co-location alone.

---

You are a **Commerce / Distributed Systems domain expert** running a resilience simulation
for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

This simulation runs in three phases. Complete each phase fully before advancing to the next.
Do not skip phases. Do not merge phase outputs into a single pass.

**Actor chain notation**: `client →` | `server →` | `operator →` | `user →`
**Conflict vocabulary**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`

---

## PHASE 1 — Scenario Contracts

Write all three scenario contracts. Each contract is a four-field trace table followed
immediately by a Classification block and a Chaos Test block. The Chaos Test block is
appended to the scenario — do not defer chaos tests to Phase 2 or a separate section.

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations.

**Four-field trace**:

| Field | Content |
|-------|---------|
| State | [system state at point of failure] |
| Capability | [what the user can still do, with named limitations] |
| Data at risk | [named records at risk — specific, not generic] |
| Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test** (append immediately after Classification — do not move to a separate section):

| Field | Content |
|-------|---------|
| Injection | [how to reproduce: what to break, at which layer, for how long] |
| Expected behavior | [what correct system behavior looks like during this failure] |
| Pass signal | [observable outcome confirming correct behavior] |
| Fail signal | [observable outcome indicating a gap] |

---

### Scenario 2 — Dependent Service Unavailable

Name the specific dependent service (pricing, loyalty, inventory, payment gateway).

**Four-field trace**:

| Field | Content |
|-------|---------|
| State | |
| Capability | |
| Data at risk | |
| Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field | Content |
|-------|---------|
| Injection | [block endpoint, return 503 after N requests, inject latency above circuit-breaker threshold] |
| Expected behavior | [circuit-break behavior, fallback mode, degraded-service indicator] |
| Pass signal | |
| Fail signal | |

---

### Scenario 3 — Eventual Consistency Conflict

Name the record type, partition boundary, and conflict-producing operation.

**Four-field trace**:

| Field | Content |
|-------|---------|
| State | |
| Capability | |
| Data at risk | |
| Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |

**Conflict resolution**:
Strategy (select one): `last-write-wins | merge | manual-reconcile | reject-stale`
-> Selected: ___
-> Adequacy: [adequate / inadequate — if inadequate, name the failure mode]

**Classification**:
```
Severity: [degraded | impaired | down]  |  Blast radius: [scope and population affected]
```

**Chaos test**:

| Field | Content |
|-------|---------|
| Injection | [dual-partition write sequence — how to produce the conflict reproducibly] |
| Expected behavior | [how conflict is detected, surfaced, and resolved] |
| Pass signal | [correct final state, audit log, operator notified] |
| Fail signal | [silent merge, wrong winner, split state, no notification] |

---

**PHASE 1 GATE** — before advancing to Phase 2, verify:
- All three scenario four-field trace tables are complete (no empty rows)
- All three Chaos test blocks are present immediately after their Classification block
- No chaos tests are grouped into a separate section

---

## PHASE 2 — Gap Registry

Identify every gap surfaced by the Phase 1 scenarios. Write all three subsections. Every
finding carries an inline observability hook on the line immediately following it — not in a
separate observability section, not at the end of the registry.

**Offline Experience Gaps**

For each gap: name the operation, describe the forced workaround, state downstream risk.

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one; add as many as found)

**Data Consistency Violations**

For each violation: name the record, describe the inconsistency, state detectability.

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

For each: name the missing automated flow, describe the manual workaround, estimate risk.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

**PHASE 2 GATE** — before advancing to Phase 3, verify:
- GAP, DCV, and MRF subsections are all present
- Every finding has an inline observability hook on the line immediately following it
- No findings are missing metric= | alert= | owner=

---

## PHASE 3 — Completeness Certification

Fill this checklist now. Include it in the artifact. Do not write the artifact file until
all three boxes are checked and the count reads "3 of 3".

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

The artifact must include all Phase 1 scenario contracts (with co-located Chaos test blocks),
all Phase 2 gap findings (with inline observability hooks), and the Phase 3 completeness
checklist with all three boxes checked and "Finding types present: 3 of 3" confirmed.

Return the file path when done.

---

## V-04 — Combined: Single-Table + Chaos-First Roles

**Axis**: Combined — V-01 (full single-table contract per scenario) + V-02 (chaos engineer
first)
**Hypothesis**: The single-table format (V-01) sequences row filling by structure; the
chaos-first role sequence (V-02) assigns natural row ownership — the Chaos Engineer owns
rows 5–10 (severity, blast radius, chaos test fields), the Commerce SME owns rows 1–4
(state, capability, data at risk, recovery). Combining them removes the structural ambiguity
in V-02 about which role "decides" table format, while maintaining the technical rigor of
chaos-first framing. The "owned by" column makes role contribution explicit without requiring
a separate commentary block per role.

---

You are running a two-role resilience simulation for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

**Roles**

Run roles in this order. Each role owns specific rows in every contract table — do not
produce separate documents per role.

1. **Distributed Systems Chaos Engineer** — fills rows 5–10 (or 5–11 for Scenario 3) of
   every contract table (Severity, Blast radius, Chaos injection, Expected behavior, Pass
   signal, Fail signal). Defines failure modes using CAP theorem trade-offs, retry semantics,
   and idempotency analysis. Validates conflict resolution strategy adequacy for the record
   type involved. Does not describe floor experience.

2. **Commerce Domain SME** — fills rows 1–4 of every contract table (State, Capability, Data
   at risk, Recovery). Grounds the Chaos Engineer's technical failure in commerce operations:
   cashier behavior, customer experience, manual workarounds, and business impact. Uses the
   actor chain notation for Recovery. Does not redesign the failure injection.

Fill all rows. Both roles contribute to Section 4 gap findings.

**Actor chain notation** (SME uses in Recovery rows):
`client →` | `server →` | `operator →` | `user →`

**Conflict resolution vocabulary** (Chaos Engineer selects in Scenario 3 row 5):
`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`

---

### Scenario 1 — Full Connectivity Loss

The system loses network connectivity entirely during active commerce operations. Chaos
Engineer defines the failure; Commerce SME fills the business context rows.

**Resilience contract**:

| Row | Owned by | Field | Content |
|-----|----------|-------|---------|
| 1 | SME | State | [system state from the operations perspective: what is inaccessible, what is still available locally] |
| 2 | SME | Capability | [what the cashier / customer / operator can still do] |
| 3 | SME | Data at risk | [named records at risk — receipts, loyalty points, offline basket, etc.] |
| 4 | SME | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Chaos Eng | Severity | [degraded / impaired / down] |
| 6 | Chaos Eng | Blast radius | [scope and population affected] |
| 7 | Chaos Eng | Chaos injection | [exact failure injection — what to break, at which layer, for how long] |
| 8 | Chaos Eng | Expected behavior | [correct system behavior — queue, reject, degrade, fail-open vs. fail-closed] |
| 9 | Chaos Eng | Pass signal | [observable outcome confirming correct behavior] |
| 10 | Chaos Eng | Fail signal | [observable outcome indicating a gap] |

---

### Scenario 2 — Dependent Service Unavailable

Name the specific service (pricing, loyalty, inventory, payment gateway) most critical to
`{topic}`'s commerce operations.

**Resilience contract**:

| Row | Owned by | Field | Content |
|-----|----------|-------|---------|
| 1 | SME | State | |
| 2 | SME | Capability | |
| 3 | SME | Data at risk | |
| 4 | SME | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Chaos Eng | Severity | [degraded / impaired / down] |
| 6 | Chaos Eng | Blast radius | |
| 7 | Chaos Eng | Chaos injection | [block endpoint, return 503 after N requests, inject latency above circuit-breaker threshold] |
| 8 | Chaos Eng | Expected behavior | [circuit-break behavior, fallback mode, degraded-service indicator] |
| 9 | Chaos Eng | Pass signal | |
| 10 | Chaos Eng | Fail signal | |

---

### Scenario 3 — Eventual Consistency Conflict

Name the record type, partition boundary, and conflict-producing operation.

**Resilience contract**:

| Row | Owned by | Field | Content |
|-----|----------|-------|---------|
| 1 | SME | State | |
| 2 | SME | Capability | |
| 3 | SME | Data at risk | |
| 4 | SME | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Chaos Eng | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` -> Selected: ___ -> Adequacy: [adequate / inadequate] |
| 6 | Chaos Eng | Severity | [degraded / impaired / down] |
| 7 | Chaos Eng | Blast radius | |
| 8 | Chaos Eng | Chaos injection | [dual-partition write sequence — how to produce the conflict reproducibly] |
| 9 | Chaos Eng | Expected behavior | [conflict detection, operator notification, resolution UI behavior] |
| 10 | Chaos Eng | Pass signal | [correct final state, audit log, notification sent] |
| 11 | Chaos Eng | Fail signal | [silent merge, wrong winner, split state, no notification] |

---

### Section 4 — Gap Identification

(mandatory — do not omit or merge with scenarios)

Both roles contribute: Chaos Engineer names technical gaps in system behavior; Commerce SME
names operational gaps in the user experience. Every finding carries an inline observability
hook on the line immediately following the finding entry. Do not collect hooks into a
separate section.

**Offline Experience Gaps**

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- GAP-02: ...

(minimum one)

**Data Consistency Violations**

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- DCV-02: ...

(minimum one)

**Missing Recovery Flows**

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`
- MRF-02: ...

(minimum one)

---

### Completeness Check

Include this block in the artifact with all boxes checked and the count confirmed.

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

Include the Completeness Check block in the artifact with all three boxes checked and
"Finding types present: 3 of 3" confirmed. Return the file path when done.

---

## V-05 — Combined: Single-Table + Phase Gates + Imperative Phrasing

**Axis**: Combined — V-01 (full single-table contract) + V-03 (three explicit phase gates)
+ imperative phrasing register: every structural requirement is a direct command co-located
with its output slot, not a requirement list at the top of the prompt
**Hypothesis**: The combination of structural integration (no section boundary between chaos
and trace rows, so chaos cannot be deferred), phase gating (gaps and checklist are mandatory
stops, not trailing requirements), and imperative co-location (each instruction is a command
at the exact point of writing) produces the tightest possible Round 3 structure. No
structural decision is left to the model. Every field is fill-in, constrained-choice, or
actor-chain slot. Every phase has an explicit stop. The V-03 integration approach + V-05 R2
output checklist are achieved in a single table format with lower output volume than V-05 R2.

---

You are a **Commerce / Distributed Systems domain expert** running a resilience simulation
for `{topic}`.

**Input**
- `{topic}` — the system or flow under analysis
- `{signal}` — read any existing signal artifacts for `{topic}` before starting

Run in three phases. Stop at each gate. Do not advance until the gate condition is satisfied.

**Fill every row in every table.** If a row is empty in your output, stop and fill it before
continuing. Empty rows are failures, not placeholders.

**Actor chain**: `client →` | `server →` | `operator →` | `user →`
Every Recovery row must prefix each step with one of these four labels. No prose recovery.

**Conflict vocabulary**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`
Select exactly one in Scenario 3 row 5. Do not paraphrase.

---

## PHASE 1 — Scenario Contracts

> Write each scenario as a single contract table. Fill all rows now, including the chaos
> rows. Do not defer chaos rows to Phase 2 or to a separate section. The chaos rows are part
> of the scenario table — fill them before moving to the next scenario.

### Scenario 1 — Full Connectivity Loss

> Write the table now. Fill all 10 rows. Do not advance to Scenario 2 until row 10 is filled.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | [system state at point of failure: what is cached, what is lost, what is unknown] |
| 2 | Capability | [named operations the user can still perform, with specific limitations] |
| 3 | Data at risk | [specific named records — not "transaction data" — that may be lost, stale, or inconsistent] |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | [scope and population affected] |
| 7 | Chaos injection | [exact failure injection: what to break, at which layer, for how long — e.g., drop outbound TCP at OS firewall, block DNS mid-transaction] |
| 8 | Expected behavior | [what correct system behavior looks like — queue depth, degraded-mode indicator, rejection semantics, fail-open or fail-closed decision] |
| 9 | Pass signal | [observable outcome confirming correct behavior — log event, UI state, metric reading, queue depth] |
| 10 | Fail signal | [observable outcome indicating a gap — silent data loss, blocking error with no recovery path, incorrect state persisted] |

---

### Scenario 2 — Dependent Service Unavailable

> Name the specific service now. Write the table. Fill all 10 rows before advancing.

Name the dependent service (pricing, loyalty, inventory, payment gateway) most critical to
`{topic}`'s commerce operations.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Severity | [degraded / impaired / down] |
| 6 | Blast radius | |
| 7 | Chaos injection | [how to inject: block the endpoint, return 503 after N requests, inject latency above the circuit-breaker timeout threshold] |
| 8 | Expected behavior | [circuit-break behavior, fallback data source, degraded-service UI, specific rejection semantics] |
| 9 | Pass signal | |
| 10 | Fail signal | |

---

### Scenario 3 — Eventual Consistency Conflict

> Name the record type and conflict-producing operation now. Write the table. Fill all 11
> rows. Select the conflict resolution strategy in row 5 — do not leave it blank.

Name the record type, partition boundary, and conflict-producing operation.

**Resilience contract**:

| Row | Field | Content |
|-----|-------|---------|
| 1 | State | |
| 2 | Capability | |
| 3 | Data at risk | |
| 4 | Recovery | client → [action] / server → [action] / operator → [action] / user → [action] |
| 5 | Conflict resolution | Strategy (select one): `last-write-wins \| merge \| manual-reconcile \| reject-stale` -> Selected: ___ -> Adequacy: [adequate / inadequate — if inadequate, name the exact failure mode this strategy produces for this record type] |
| 6 | Severity | [degraded / impaired / down] |
| 7 | Blast radius | |
| 8 | Chaos injection | [how to produce the conflict: dual-partition write sequence, reconnect timing, specific conflicting write operations] |
| 9 | Expected behavior | [how conflict is detected, what notification fires, what the resolution UI offers, resolution latency] |
| 10 | Pass signal | [record in correct final state, audit log entry present, operator notification sent within SLA] |
| 11 | Fail signal | [silent merge, wrong writer wins, record left in split state, operator not notified, audit log missing] |

---

**PHASE 1 GATE** — verify before advancing:
- All three scenario tables complete (no empty rows)
- Chaos injection / Expected behavior / Pass signal / Fail signal are rows inside the
  scenario table for all three scenarios — not in a separate section

---

## PHASE 2 — Gap Registry

> Write all three subsections now. After each finding entry, write the observability hook
> on the very next line. Do not collect hooks into a separate section at the end.

Identify every gap surfaced by the Phase 1 scenarios. Each finding is distinct, named, and
actionable. After each finding, write: `metric=[name]` | `alert=[condition]` | `owner=[role]`

**Offline Experience Gaps**

> Write GAP-01 now. Write the observability hook on the next line. Then write GAP-02.

- GAP-01: [name] — [description] — [downstream risk]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`

(minimum one; add as many as found)

**Data Consistency Violations**

> Write DCV-01 now. Write the observability hook on the next line. Then write DCV-02.

- DCV-01: [record] — [inconsistency] — [detectable before / only after customer impact]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`

(minimum one)

**Missing Recovery Flows**

> Write MRF-01 now. Write the observability hook on the next line. Then write MRF-02.

- MRF-01: [name] — [manual workaround] — [risk if stays manual]
  `metric=[name]` | `alert=[condition that fires]` | `owner=[team or role]`

(minimum one)

---

**PHASE 2 GATE** — verify before advancing:
- GAP, DCV, and MRF subsections all present
- Every finding has metric= | alert= | owner= on the line immediately following it

---

## PHASE 3 — Completeness Certification

> Fill this checklist now. Check each box. Write the count. Include this block in the
> artifact exactly as filled. Do not write the artifact file until the count reads "3 of 3".

- [ ] GAP subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] DCV subsection present with >=1 finding carrying inline metric/alert/owner
- [ ] MRF subsection present with >=1 finding carrying inline metric/alert/owner

Finding types present: ___ of 3

---

### Output

Write the artifact to:
`simulations/flow/resilience/{topic}-resilience-{date}.md`

The artifact must include:
1. All three Phase 1 scenario contracts (single tables, all rows filled, chaos rows inside)
2. All Phase 2 gap findings (each with inline observability hook on the following line)
3. The Phase 3 completeness checklist with all three boxes checked and
   "Finding types present: 3 of 3" confirmed

Return the file path when done.
