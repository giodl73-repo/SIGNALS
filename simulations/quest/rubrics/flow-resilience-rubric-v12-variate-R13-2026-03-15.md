# flow-resilience — Round 13 Variations (Rubric v12)

**Rubric**: v12 · 30 aspirational criteria (C-09 – C-38) · Ceiling entering R13: 30/30 → 100.00 (R12 V-05)
**Open criteria entering R13**: None — V-05 cracks all 30 criteria including C-38.
**R13 objective**: With no new criteria open, all five variations hold the R12 ceiling (30/30) while exploring structural diversity. Axes probe role sequence, output format, phrasing register, inertia emphasis, and compactness — finding distinct paths to the same 100.00 ceiling.

**Variation axes chosen:**
- **Role Sequence** — which expert phase runs first within each row (D-first vs C-first)
- **Output Format** — structural presentation of the Gap Register (finding-forward vs observability-forward)
- **Phrasing Register** — imperative command form vs explanation-backed directive form
- **Inertia Framing** — inertia assessment as prelude vs inertia as organizing spine of the whole output
- **Lifecycle Emphasis** — how much space the recovery path stages occupy relative to other columns

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | Role sequence: C-phase leads, D-phase follows | Reversing the intra-row column-group gate to C-first tests whether commerce grounding as the first fill commitment drives richer scenario naming and class labeling — and confirms C-32's column-group gate is axis-agnostic (direction of D/C phase ordering does not determine whether the gate exists) |
| V-02 | Output format: observability-forward Gap Register | Leading each finding with Metric / Alert / Owner before the finding description forces the model to commit to named monitoring signals before authoring the gap text — hypothesis: reduces generic observability fills without weakening C-10/C-13/C-15/C-16 |
| V-03 | Phrasing register: explanation-backed directives | Replacing hard-stop imperatives ("Write this row now. Do not advance until...") with rationale-embedded directives ("Row 1 is complete only when all four stages carry a named VS; advancing before that produces a structurally incomplete row") — hypothesis: explanation-backed language achieves equivalent structural enforcement while improving prompt readability |
| V-04 | Inertia framing dominant + lifecycle emphasis | Inverting the organizing spine: the Inertia Assessment drives the whole output; scenarios are evidence for inertia claims, not the reverse; the Investment Verdict becomes a formal recommendation rather than a synthesis note — hypothesis: inertia-first framing pulls chronic-consequence thinking into the early columns rather than appending it as Status Quo Risk |
| V-05 | Compact synthesis: minimum prose, all 30 criteria | The tightest prompt achieving all 30 criteria — architecture table compressed, row descriptors shortened, anti-boundary umbrella (C-38) carries all four escape negations without per-section restatement — hypothesis: identifies the minimum load-bearing structure achieving the R12 ceiling |

---

---

## V-01 — Role Sequence: Commerce Expert Leads (C-First, D-Second)

**Variation axis**: Role sequence — C-phase (commerce labeling, severity, user capability, inertia link) completes before D-phase (trigger condition, system state, data at risk, recovery path) within each row.

**Hypothesis**: Commerce grounding is the scarce commodity in resilience analysis — locking in the commerce scenario name, failure class, severity, and user capability first forces a specific, domain-grounded frame before the distributed-systems machinery fills in. C-first ordering may produce richer scenario naming and cleaner class labeling than the D-first order, while still satisfying C-32 (column-group gate exists, direction is not mandated by the criterion).

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment (complete before scenario table)

Before building the scenario table, produce an Inertia Assessment naming the status-quo competitor.

**1a. Status Quo Threat**: Name the do-nothing path. Why do teams defer resilience investment for this topic? Assess: HIGH / MEDIUM / LOW with one-sentence justification. What does the current system do under each failure class (Class 1 / Class 2 / Class 3) without intervention?

**1b. Carrying Costs by Class**: For each class, name the chronic accumulation without remediation. Format: *[named metric] accumulates at [rate], [horizon trajectory] without intervention*.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: One observable threshold per class at which deferral becomes indefensible — quantified condition + named metric being monitored (e.g., "oversell-event count exceeds 50/month", "cart-abandonment rate rises > 2% above baseline").

> Produce the Inertia Assessment now. Do not advance to the architecture section until all three parts (1a, 1b, 1c) are complete with non-placeholder content for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table + chaos blocks before Gap Register | Phase gate: all 3 rows + co-located chaos blocks complete before Gap Register begins | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — C-phase before D-phase | Intra-row C-first gate: complete all C-owned columns before beginning D-owned columns | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications with actor-chain notation | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from C-phase to D-phase.** The Inertia Assessment is a pre-table section — not a structural boundary within the scenario table. Chaos Test Blocks are co-located supplements appended immediately after each row — **not a separate chaos section, not a standalone chaos table, not a structural boundary**. Per-finding observability metadata is inline with each Gap Register finding — **not a separate observability section**.

---

### Chaos Test Block Specification

Each scenario row is immediately followed by a co-located Chaos Test Block. Do not consolidate chaos blocks into a separate section.

| Component | Fill Requirement |
|-----------|-----------------|
| **Inject** | Named failure condition: service + injection method + duration. Reproducible in a test harness (e.g., "kill inventory-service pod via `kubectl delete pod`", "drop client-server TCP packets for 60s via network policy", "halt write replication on replica-1 for 10s"). |
| **Expected Behavior** | Named observables (dashboard, operator, user) during injection if the system handles the failure correctly. Name specific signals, not desired end-states. |
| **Pass Signal** | Named observable confirming the system handled the failure per the row's recovery path (e.g., "circuit-breaker = OPEN in dashboard within 60s, inventory-accept-mode = CONSERVATIVE, zero checkout errors in error-rate monitor"). |
| **Fail Signal** | Named observable confirming failure to handle (e.g., "order-service error rate > 50%, circuit-breaker = CLOSED, oversell-event count > 0 in inventory monitor"). |

---

### Column Contract

> Process this contract before constructing any row. Column omission is a contract violation. Status Quo Risk entries must be consistent with Inertia Assessment Step 1b.
>
> **Conflict vocabulary constraint (applies to all columns)**: All references to conflict resolution strategies must use canonical vocabulary: `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale`. Free-text descriptions (e.g., "the most recent write wins", "reconcile manually") do not satisfy this constraint — the canonical term must appear as a discrete label.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Scenario Name | C | Specific commerce operation and failure mode. Named before any technical analysis. |
| Class Label | — | Exactly one of: **Class 1** / **Class 2** / **Class 3**. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment. |
| User Capability | C | What the user *can still do*. At least one surviving capability. Named from the commerce perspective. |
| Status Quo Risk | C | Must use metric and framing from Inertia Assessment Step 1b for this class. *Rate* + *horizon* + *named business metric*. All three required. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying threshold crossing. Qualitative-only fails. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. For Class 3 rows, name the active conflict resolution strategy using canonical vocabulary. |
| Data at Risk | D | Specific consistency violation type + scope. For Class 3 rows, name the conflict resolution strategy using canonical vocabulary and include an adequacy judgment (is this strategy appropriate for this data type?). |
| Recovery Path | D | All four stage sub-specifications with actor-chain notation (see below). Every stage: actor-chain mechanism + SLA target + named VS. |

**Column order in output table**: `#` | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk | Trigger Condition | System State | Data at Risk | Recovery Path

**Recovery Path — Stage Sub-Specifications with Actor-Chain Notation**

Each stage's Mechanism must begin with an actor-chain prefix: `client →`, `server →`, `operator →`, or `user →`. At least three of the four stages in every row must carry a labeled actor-chain prefix.

> **Stage 1 — Detect / TTD**: *Mechanism*: [actor →] action. *SLA target*: TTD. *VS*: named observable confirming detection.
> **Stage 2 — Contain / TTC**: *Mechanism*: [actor →] action. *SLA target*: TTC. *VS*: named observable confirming containment.
> **Stage 3 — Recover / TTR**: *Mechanism*: [actor →] action. *SLA target*: TTR. *VS*: named observable confirming recovery.
> **Stage 4 — Validate / TTV**: *Mechanism*: [actor →] action. *SLA target*: TTV. *VS*: named observable confirming validation.

---

### Section Order Requirement

Produce all 3 scenario rows, each immediately followed by its co-located Chaos Test Block, before writing the Gap Register. Do not write the Gap Register until Row 3 and its Chaos Block are complete. Do not write Recommendations until the Gap Register and Completeness Checklist are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path.

C-phase fill: Scenario = specific commerce operation interrupted by client disconnection. Class 1. Severity = Impaired, ~2% of active sessions. User Capability = at least one capability the user retains during offline state (e.g., browse cached catalog, queue draft order). Status Quo Risk = must use Class 1 carrying cost from Step 1b with rate + horizon + named metric. Acute consequence branches: enumerate at least two specific commerce outcomes if the recovery path is absent (e.g., double-charge on reconnect, cart state lost, inventory oversell on reconnect burst).

D-phase fill after C-phase complete: Trigger = client keepalive fails 3 × 10s probes / heartbeat no-response. System State = order-service unreachable; cart cached locally; payment token pending. Data at Risk = uncommitted cart state, pending payment token. Recovery Path with actor-chain notation — Stage 1 Detect/TTD: client → detects offline / VS named; Stage 2 Contain/TTC: client → writes queued with idempotency key / VS named; Stage 3 Recover/TTR: client → queue flushes, server → idempotency-protected endpoint / VS named; Stage 4 Validate/TTV: server → confirms order state / VS named.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism (labeled prefix), SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 1 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 1 (co-located; complete before advancing to Row 2).**

Fill: Inject = [named injection for Class 1]; Expected Behavior = [named observables if handled correctly]; Pass Signal = [named observable confirming correct handling]; Fail Signal = [named observable confirming failure]. All four components required.

**Do not advance to Row 2 until this row's scenario cells AND the Chaos Block both contain non-placeholder content with all four chaos components.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path.

C-phase fill: Scenario = specific commerce operation blocked by a dependent service outage. Class 2. Severity = Degraded, all users attempting the operation during outage window. User Capability = at least one capability that remains available via cached or degraded-mode operation. Status Quo Risk = Class 2 carrying cost from Step 1b with rate + horizon + named metric. Acute consequence branches: no circuit breaker → cascade; no snapshot → all placement blocked; no oversell buffer → customer-visible oversell on recovery.

D-phase fill after C-phase complete: Trigger = dependent-service error rate > 5% / 60s rolling window / probe 503 × 3 consecutive probes. System State = order-service operational; dependent-service circuit-breaker OPEN; last-known snapshot stale. Data at Risk = reservation accuracy against stale snapshot; oversell risk. Recovery Path — Stage 1 Detect/TTD: server → circuit breaker opens at threshold / VS named; Stage 2 Contain/TTC: server → snapshot-mode with oversell buffer active / VS named; Stage 3 Recover/TTR: server → breaker half-opens, operator → reconciliation triggered / VS named; Stage 4 Validate/TTV: operator → counts verified / VS named.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 2 carrying cost from Step 1b.**

**Chaos Block — Row 2 (co-located; complete before advancing to Row 3).**

Fill: Inject = [named injection for Class 2]; Expected Behavior = [named observables]; Pass Signal = [named observable]; Fail Signal = [named observable]. All four required.

**Do not advance to Row 3 until Row 2 scenario cells AND the Chaos Block both contain non-placeholder content with all four chaos components.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path.

C-phase fill: Scenario = specific commerce operation where concurrent writes from partitioned nodes produce conflicting state. Class 3. Severity = Impaired, <1% of users (high-contention SKUs, flash sale windows), high data integrity risk. User Capability = at least one capability available on primary node during containment. Status Quo Risk = Class 3 carrying cost from Step 1b. Acute consequence branches: `last-write-wins` without detection → both orders fulfilled → oversell; naive `merge` → phantom inventory; rollback without notification → silent order cancellation.

D-phase fill after C-phase complete: Trigger = replica lag > 5s / replica-lag metric fires split-brain alert. System State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Data at Risk = inventory count integrity; post-merge count non-deterministic; adequacy judgment: `last-write-wins` inadequate — `manual-reconcile` with lower-count-wins rule required. Recovery Path — Stage 1 Detect/TTD: server → lag alert fires / VS named; Stage 2 Contain/TTC: operator → writes fenced to primary / VS named; Stage 3 Recover/TTR: server → `manual-reconcile` resolution job / VS named; Stage 4 Validate/TTV: operator → post-merge cross-check / VS named.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism, SLA target, and named VS, a Data at Risk entry naming the conflict strategy in canonical vocabulary with an adequacy judgment, and a Status Quo Risk entry consistent with the Class 3 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 3 (co-located; complete before advancing to Gap Register).**

Fill: Inject = [named injection for Class 3]; Expected Behavior = [named observables]; Pass Signal = [named observable]; Fail Signal = [named observable]. All four required.

**Do not advance to the Gap Register until Row 3's scenario cells AND its Chaos Block both contain non-placeholder content with all four chaos components.**

---

### Output Table

Produce a **single unified table**. All three scenario rows appear in this one table. After each scenario row, append its co-located Chaos Test Block immediately — before the next row begins.

**Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts. Do not consolidate the three chaos blocks into a separate chaos-engineering section — each is co-located with its row.**

Column order: `#` | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk | Trigger Condition | System State | Data at Risk | Recovery Path

---

### Gap Register

After completing all three rows and their co-located chaos blocks, produce a Gap Register with exactly three labeled findings. Each finding must include inline observability metadata — **not a separate observability section**.

**Per-finding format**:
> **[Finding Type] — [specific, actionable description]**
> `Metric:` [named monitoring metric]
> `Alert:` [condition triggering alert]
> `Owner:` [Commerce Expert / Distributed Systems Expert / SRE]

1. **Offline Experience Gap** — specific Class 1 capability not addressed by the recovery path. `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — specific Class 2 or 3 violation the system cannot currently detect or correct. `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — specific absent mechanism. `Metric:` ... `Alert:` ... `Owner:` ...

A finding without all three inline fields fails the format requirement.

Produce one **Inertia Verdict**: given the carrying costs named in Step 1b and the gaps identified above, is inertia a HIGH / MEDIUM / LOW threat, and what is the single strongest argument against deferral? (2–3 sentences.)

Then produce the **Finding Completeness Checklist** as output content:

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap in one phrase]
[ ] Data Consistency Violation — [named violation in one phrase]
[ ] Missing Recovery Flow — [named mechanism in one phrase]
Finding types present: ___ of 3
```

Mark each `[x]` only when that finding is specific, actionable, non-generic, and has all three inline fields. Write "3 of 3" only when all three pass.

---
---

## V-02 — Output Format: Observability-Forward Gap Register

**Variation axis**: Output format — the Gap Register presents each finding with Metric / Alert / Owner *first*, then the gap description, reversing the finding-forward order of the baseline.

**Hypothesis**: When the model must commit to a named monitoring signal before writing the finding description, the metric and alert entries are more likely to be specific and actionable (naming a real metric path, a real threshold) rather than being retrofitted onto a generic gap description. The observability-forward format reduces the pattern where a model writes a vague finding and then appends a vague metric. All other structural requirements remain identical to R12 V-05.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment (complete before scenario table)

**1a. Status Quo Threat**: Name the do-nothing path. Assess HIGH / MEDIUM / LOW with one-sentence justification. What does the current system do under Class 1 / Class 2 / Class 3 without intervention?

**1b. Carrying Costs by Class**: Format: *[named metric] accumulates at [rate], [horizon trajectory] without intervention*.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: One observable threshold per class — quantified condition + named metric being monitored.

> Produce the Inertia Assessment now. Do not advance until all three parts are complete for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table + chaos blocks before Gap Register | Phase gate: all 3 rows + co-located chaos blocks before Gap Register begins | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first gate: complete D-owned columns before C-owned columns | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications with actor-chain notation | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** The Inertia Assessment is a pre-table section — not a structural boundary within the scenario table. Chaos Test Blocks are co-located supplements appended immediately after each row — **not a separate chaos section, not a standalone chaos table, not a structural boundary**. Per-finding observability metadata is inline with each Gap Register finding — **not a separate observability section**.

---

### Chaos Test Block Specification

Each scenario row is immediately followed by a co-located Chaos Test Block. Do not consolidate chaos blocks into a separate section.

| Component | Fill Requirement |
|-----------|-----------------|
| **Inject** | Named failure condition: service + injection method + duration. Reproducible in a test harness. |
| **Expected Behavior** | Named observables (dashboard, operator, user) during injection if handled correctly. Specific signals, not desired end-states. |
| **Pass Signal** | Named observable confirming the system handled the failure per the row's recovery path. |
| **Fail Signal** | Named observable confirming failure to handle. |

---

### Column Contract

> Process this contract before constructing any row. Column omission is a contract violation. Status Quo Risk entries must be consistent with Inertia Assessment Step 1b.
>
> **Conflict vocabulary constraint**: All references to conflict resolution strategies must use canonical vocabulary: `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale`. Free-text descriptions do not satisfy this constraint.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying threshold crossing. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. For Class 3 rows, name the conflict resolution strategy using canonical vocabulary. |
| Data at Risk | D | Specific consistency violation type + scope. For Class 3 rows, name the conflict resolution strategy using canonical vocabulary with adequacy judgment. |
| Recovery Path | D | All four stage sub-specifications with actor-chain notation. Every stage: actor-chain mechanism + SLA target + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** / **Class 2** / **Class 3**. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment. |
| User Capability | C | What the user *can still do*. At least one surviving capability. |
| Status Quo Risk | C | Must use metric and framing from Inertia Assessment Step 1b for this class. *Rate* + *horizon* + *named business metric*. All three required. |

**Column order**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications with Actor-Chain Notation**

Each stage's Mechanism must begin with `client →`, `server →`, `operator →`, or `user →`. At least three of four stages per row must carry a labeled prefix.

> **Stage 1 — Detect / TTD**: *Mechanism*: [actor →] action. *SLA*: TTD. *VS*: named observable confirming detection.
> **Stage 2 — Contain / TTC**: *Mechanism*: [actor →] action. *SLA*: TTC. *VS*: named observable confirming containment.
> **Stage 3 — Recover / TTR**: *Mechanism*: [actor →] action. *SLA*: TTR. *VS*: named observable confirming recovery.
> **Stage 4 — Validate / TTV**: *Mechanism*: [actor →] action. *SLA*: TTV. *VS*: named observable confirming validation.

---

### Section Order Requirement

Produce all 3 scenario rows, each immediately followed by its co-located Chaos Test Block, before writing the Gap Register. Do not write the Gap Register until Row 3 and its Chaos Block are complete. Do not write Recommendations until the Gap Register and Completeness Checklist are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat returns no response. System State = order-service unreachable; local cart state cached; payment-authorization token pending. Data at Risk = uncommitted cart modifications (stale write risk); pending payment token (expiry risk). Recovery Path — Stage 1 Detect/TTD: client → heartbeat detects offline / VS named; Stage 2 Contain/TTC: client → writes queued with idempotency key / VS named; Stage 3 Recover/TTR: client → queue flushes on reconnect, server → idempotency-protected endpoint / VS named; Stage 4 Validate/TTV: server → confirms order state / VS named.
C-phase fill: Scenario name; Class 1; Severity Impaired ~2% sessions; User Capability; Status Quo Risk = Class 1 carrying cost from Step 1b. Acute branches: no idempotency → double-charge; no queue → cart lost; naive retry → oversell burst.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column including all four Recovery Path stage sub-specifications each with actor-chain mechanism, SLA target, and named VS, and a Status Quo Risk entry with rate, horizon, and named metric from Step 1b.**

**Chaos Block — Row 1 (co-located; complete before advancing to Row 2).**

Fill: Inject = [named injection for Class 1]; Expected Behavior = [named observables if handled correctly]; Pass Signal = [named observable]; Fail Signal = [named observable]. All four required.

**Do not advance to Row 2 until Row 1 scenario cells AND Chaos Block both contain non-placeholder content with all four chaos components.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory-service error rate > 5% / 60s rolling / health probe 503 × 3. System State = circuit breaker OPEN; snapshot stale. Data at Risk = reservation accuracy against stale snapshot; oversell risk. Recovery Path — Stage 1 Detect/TTD: server → circuit breaker trips / VS named; Stage 2 Contain/TTC: server → snapshot-mode with oversell buffer / VS named; Stage 3 Recover/TTR: server → half-open, operator → reconciliation triggered / VS named; Stage 4 Validate/TTV: operator → counts verified / VS named.
C-phase fill: Scenario name; Class 2; Severity Degraded all users during window; User Capability; Status Quo Risk = Class 2 carrying cost from Step 1b. Acute branches: no breaker → cascade; no snapshot → blocked; no buffer → oversell.

**Do not advance to the Chaos Block until all four Recovery Path stages each have actor-chain mechanism, SLA target, and named VS.**

**Chaos Block — Row 2 (co-located; complete before advancing to Row 3).**

Fill: Inject / Expected Behavior / Pass Signal / Fail Signal — all four required with named observables.

**Do not advance to Row 3 until Row 2 scenario cells AND Chaos Block both contain non-placeholder content.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = replica lag > 5s / lag metric fires split-brain alert. System State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Data at Risk = inventory count integrity; adequacy judgment: `last-write-wins` inadequate — `manual-reconcile` with lower-count-wins rule required. Recovery Path — Stage 1 Detect/TTD: server → lag alert fires / VS named; Stage 2 Contain/TTC: operator → writes fenced to primary / VS named; Stage 3 Recover/TTR: server → `manual-reconcile` resolution job / VS named; Stage 4 Validate/TTV: operator → post-merge cross-check / VS named.
C-phase fill: Scenario name; Class 3; Severity Impaired <1% users high integrity risk; User Capability; Status Quo Risk = Class 3 carrying cost from Step 1b. Acute branches: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback without notification → silent cancellation.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications, a Data at Risk entry naming the conflict strategy in canonical vocabulary with adequacy judgment, and a Status Quo Risk entry with rate, horizon, and named metric from Step 1b.**

**Chaos Block — Row 3 (co-located; complete before advancing to Gap Register).**

Fill: Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to the Gap Register until Row 3's scenario cells AND Chaos Block both contain non-placeholder content with all four chaos components.**

---

### Output Table

Produce a **single unified table**. After each scenario row, append its co-located Chaos Test Block immediately — before the next row begins.

**Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts. Do not consolidate the three chaos blocks into a separate chaos-engineering section.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register (Observability-Forward Format)

After completing all three rows and their co-located chaos blocks, produce a Gap Register with exactly three findings in observability-forward format. Commit to the monitoring specification *before* writing the finding description. Do not produce a separate observability section — the monitoring specification is the leading inline block for each finding.

**Per-finding format** (observability-forward):
> `Metric:` [named monitoring metric that surfaces this gap in production — commit to this first]
> `Alert:` [named condition on that metric triggering an alert, e.g., "metric > threshold for N samples"]
> `Owner:` [Commerce Expert / Distributed Systems Expert / SRE]
> **[Finding Type] — [specific, actionable description of the gap this monitoring will surface]**

Required findings (each must include all three observability fields before the finding description):

1. `Metric:` ... `Alert:` ... `Owner:` ... **Offline Experience Gap** — specific Class 1 capability not addressed by the recovery path.
2. `Metric:` ... `Alert:` ... `Owner:` ... **Data Consistency Violation** — specific Class 2 or 3 violation the system cannot currently detect or correct.
3. `Metric:` ... `Alert:` ... `Owner:` ... **Missing Recovery Flow** — specific absent mechanism.

A finding where the monitoring fields are generic ("TBD", "some metric") fails the format requirement regardless of the gap description quality.

Produce one **Inertia Verdict**: carrying costs from Step 1b + gaps identified → HIGH / MEDIUM / LOW threat + single strongest argument against deferral (2–3 sentences).

Then produce the **Finding Completeness Checklist** as output content:

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap in one phrase]
[ ] Data Consistency Violation — [named violation in one phrase]
[ ] Missing Recovery Flow — [named mechanism in one phrase]
Finding types present: ___ of 3
```

Mark each `[x]` only when that finding type is present with specific, actionable, non-generic content and all three observability fields complete with named (non-generic) content. Write "3 of 3" only when all three pass.

---
---

## V-03 — Phrasing Register: Explanation-Backed Directives

**Variation axis**: Phrasing register — replaces hard-stop imperatives ("Write this row now. Do not advance until...") with explanation-backed directives ("Row 1 is complete only when... advancing before this produces a structurally incomplete row because..."). All structural requirements are identical to R12 V-05; only the phrasing of enforcement instructions changes.

**Hypothesis**: Hard-stop imperatives are effective but create a command-heavy prompt that can feel adversarial. Explanation-backed directives name *why* the gate exists — which may produce more thoughtful fills, since the model understands the structural risk being prevented rather than only receiving a prohibition. If explanation-backed language achieves equivalent structural enforcement, it is preferable for readability and maintainability.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment (complete before scenario table)

Before the scenario table, commit to an Inertia Assessment. This section is the source of truth for Status Quo Risk fills — scenario rows must reference it, not author carrying costs independently.

**1a. Status Quo Threat**: Name the do-nothing path. Assess HIGH / MEDIUM / LOW with one-sentence justification. What does the current system do under each failure class without intervention?

**1b. Carrying Costs by Class**: For each class, name the chronic accumulation without remediation. Format: *[named metric] accumulates at [rate], [horizon trajectory] without intervention*. These three carrying costs are pre-committed constraints for Status Quo Risk column fills.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: One observable threshold per class — quantified condition + named metric. These signals are the empirical evidence that carrying costs have reached a decision point.

The Inertia Assessment is complete only when all three parts contain non-placeholder content for all three failure classes. The scenario table should not begin until all three parts are filled — starting the table with incomplete inertia data produces a Status Quo Risk column that cannot reference pre-committed carrying costs, undermining the two-horizon consequence specification.

---

### Five-Level Anti-Omission Architecture

The scenario table uses five structural mechanisms to prevent omission at different granularities. Each mechanism targets a distinct failure mode: a mechanism that prevents table-splitting does not prevent in-row phase confusion, and a mechanism that prevents phase confusion does not prevent cell-level placeholder content.

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table + chaos blocks before Gap Register | Phase gate: all rows + chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | Within a row | Explanation-backed directive at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first gate | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications with actor-chain notation | Column Contract (below) |

The anti-boundary requirement exists because model output under token pressure may interpret a column ownership transition as a natural section break and introduce a horizontal rule, heading, or sub-table boundary. This structural drift produces an artifact that passes a casual read but fails the unified-table requirement: **All three scenario rows must appear in a single unified table. The correct output contains no separate tables for Distributed Systems Expert columns and Commerce Expert columns, no horizontal rules or section breaks between rows when column ownership shifts from D-phase to C-phase.** The Inertia Assessment is a pre-table section — not a boundary inside the scenario table. Chaos Test Blocks are row-appended supplements — **not a standalone chaos section, not a separate chaos table**. Per-finding observability metadata is row-finding-inline — **not a standalone observability section or table**.

---

### Chaos Test Block Specification

A Chaos Test Block immediately follows each scenario row — before the next row begins. Consolidating chaos blocks into a standalone section after all rows means the model may compress or drop components under token pressure; co-location prevents this by keeping each block adjacent to the row it verifies.

| Component | Fill Requirement |
|-----------|-----------------|
| **Inject** | Named failure condition: service + injection method + duration. Reproducible in a test harness (e.g., "kill inventory-service pod via `kubectl delete pod`", "drop client-server TCP packets for 60s via network policy"). |
| **Expected Behavior** | Named observables (dashboard, operator, user) during injection if handled correctly — specific signals, not desired end-states. |
| **Pass Signal** | Named observable confirming the system handled the failure per the row's recovery path. |
| **Fail Signal** | Named observable confirming failure to handle. |

---

### Column Contract

Processing this contract before constructing any row creates structural pre-commitment: the model has assigned responsibility and fill requirements to each column before building any cell. Column omission is a contract violation, detectable against this pre-commitment rather than only discovered by post-hoc audit.

> Status Quo Risk entries must be consistent with Inertia Assessment Step 1b — they are not independently authored per row.
>
> **Conflict vocabulary constraint**: All references to conflict resolution strategies must use canonical vocabulary: `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale`. Free-text descriptions do not satisfy this constraint — the canonical term must appear as a discrete label. This constraint applies to System State, Data at Risk, and Recovery Path columns wherever a conflict resolution reference appears.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying threshold crossing. Qualitative descriptions without a threshold expression are incomplete. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. For Class 3 rows, name the active conflict resolution strategy using canonical vocabulary. |
| Data at Risk | D | Specific consistency violation type + scope. For Class 3 rows, name the conflict resolution strategy in canonical vocabulary with an adequacy judgment. |
| Recovery Path | D | All four stage sub-specifications with actor-chain notation (defined in the Stage Sub-Specifications section below). Every stage requires: actor-chain mechanism + SLA target + named Verification Signal (VS). |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** / **Class 2** / **Class 3**. Merging two classes into one row is a content failure that produces a structural gap. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment. |
| User Capability | C | What the user *can still do*. At least one surviving capability. |
| Status Quo Risk | C | The carrying cost pre-committed in Inertia Assessment Step 1b for this class. *Rate* + *horizon* + *named business metric* — all three components required; a status quo risk entry missing any component is incomplete against the three-component framing requirement. |

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications with Actor-Chain Notation**

Each stage mechanism must begin with an actor-chain prefix (`client →`, `server →`, `operator →`, or `user →`) that identifies which system actor owns the transition. The prefix requirement exists because prose stage descriptions ("the circuit breaker opens", "the system retries") obscure ownership, which becomes a gap identification problem: it is unclear whether a missing mechanism requires client instrumentation, server-side logic change, or operator runbook. At least three of the four stages in every row must carry a labeled prefix; a stage mechanism without a labeled actor prefix is incomplete against this standard.

> **Stage 1 — Detect / TTD**: *Mechanism*: [actor →] action surfacing the failure. *SLA target*: TTD. *VS*: named observable confirming detection complete.
> **Stage 2 — Contain / TTC**: *Mechanism*: [actor →] action bounding blast radius. *SLA target*: TTC. *VS*: named observable confirming containment active.
> **Stage 3 — Recover / TTR**: *Mechanism*: [actor →] action restoring service. *SLA target*: TTR. *VS*: named observable confirming recovery complete.
> **Stage 4 — Validate / TTV**: *Mechanism*: [actor →] action confirming post-recovery consistency. *SLA target*: TTV. *VS*: named observable confirming validation complete.

---

### Section Order Requirement

Produce all 3 scenario rows, each immediately followed by its co-located Chaos Test Block, before writing the Gap Register. Beginning the Gap Register before Row 3 and its Chaos Block are complete produces a Gap Register that may not reflect all three failure classes and may not have the chaos-testability evidence to support specific findings. Do not write Recommendations until the Gap Register and Completeness Checklist are both complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

Row 1 covers full client-side connectivity loss — the scenario where the client cannot reach any server-side endpoint. This is the only class where the client is the primary containment actor; rows 2 and 3 both involve server-side and operator-side containment. Filling this row completely before advancing ensures Class 1 is represented by a distinct scenario with client-side recovery path, not collapsed into Class 2 as a variant of service unavailability.

**Begin Row 1 here.** The row is complete only when every column contains non-placeholder content.

Column-group gate: D-phase columns (Trigger Condition, System State, Data at Risk, Recovery Path) should be complete before C-phase columns (Scenario Name, Class Label, Severity + Blast Radius, User Capability, Status Quo Risk). This sequencing ensures the technical failure analysis is grounded before the commerce framing is applied — reducing the risk that the scenario name drives the failure analysis rather than reflecting it.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat no-response; threshold and detection signal both present. System State = order-service unreachable from client; local cart state cached; payment-authorization token pending; no write path available. Data at Risk = uncommitted cart modifications (stale write risk), pending payment token (expiry risk), orphaned server reservation until sync. Recovery Path with actor-chain notation: Stage 1 Detect/TTD = client → heartbeat detects offline / VS: offline-indicator renders in UI; Stage 2 Contain/TTC = client → pending writes queued with idempotency key / VS: write-queue depth > 0 in client telemetry; Stage 3 Recover/TTR = client → queue flushes via idempotency-protected endpoint on reconnect, server → returns 200 / VS: order-service 200 with idempotency-key echo; Stage 4 Validate/TTV = server → confirms order state post-sync / VS: order-id in sync response matches local draft.
C-phase fill: Scenario name; Class 1; Severity Impaired ~2% sessions; User Capability = browse cached catalog, queue draft order for retry; Status Quo Risk = Class 1 carrying cost from Step 1b. Acute branches: no idempotency key → double-charge on reconnect; no local queue → cart lost on disconnect; naive retry without TTD gate → oversell burst.

The Chaos Block for Row 1 belongs immediately after this row — before Row 2 begins. Advancing to Row 2 before the chaos block is complete leaves Row 1 without a testability specification, which means the scenario cannot be verified in a test harness.

**Chaos Block — Row 1 (co-located).**

Fill all four components: Inject = [named, reproducible failure injection]; Expected Behavior = [named observables if handled correctly]; Pass Signal = [named observable confirming correct handling]; Fail Signal = [named observable confirming failure]. The chaos block is complete only when all four components are specific and named — a partial chaos block (e.g., missing a fail signal) is not a complete testability specification.

Row 1 is ready to advance when: scenario cells are non-placeholder across all columns including all four Recovery Path stages (each with labeled actor prefix, SLA target, and named VS), and the Chaos Block contains all four components.

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

Row 2 covers partial server-side failure — a dependent service becomes unavailable while the primary service remains operational. This class requires server-side circuit-breaking and snapshot-mode degraded operation; the client experience is degraded rather than disconnected.

**Begin Row 2 here.** The row is complete only when every column contains non-placeholder content.

Column-group gate: D-phase complete before C-phase (same rationale as Row 1 — technical analysis grounds the commerce framing).

D-phase fill: Trigger = inventory-service error rate > 5% / 60s rolling window / health probe 503 × 3 consecutive. System State = order-service operational; inventory-service circuit-breaker OPEN; last-known snapshot stale. Data at Risk = reservation accuracy against stale snapshot; oversell risk during outage window. Recovery Path — Stage 1 Detect/TTD: server → circuit breaker opens at threshold / VS named; Stage 2 Contain/TTC: server → snapshot-mode with oversell buffer active / VS named; Stage 3 Recover/TTR: server → half-open probe, operator → reconciliation triggered / VS named; Stage 4 Validate/TTV: operator → discrepancy counter verified / VS named.
C-phase fill: Scenario name; Class 2; Severity Degraded all orders in window; User Capability; Status Quo Risk = Class 2 carrying cost from Step 1b. Acute branches: no circuit breaker → cascade; no snapshot → blocked; no buffer → oversell.

The Chaos Block for Row 2 belongs immediately after — before Row 3 begins.

**Chaos Block — Row 2 (co-located).**

Fill: Inject / Expected Behavior / Pass Signal / Fail Signal — all four required with named observables.

Row 2 is ready to advance when scenario cells and Chaos Block are both complete with non-placeholder content.

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

Row 3 covers split-brain — two nodes accepting concurrent writes to the same record, producing divergent state. This class is distinct from Class 2: the service is not unavailable (writes are accepted), but the resulting state is inconsistent. The conflict resolution strategy is the critical data at risk specification.

**Begin Row 3 here.** The row is complete only when every column contains non-placeholder content including a conflict resolution strategy in canonical vocabulary.

Column-group gate: D-phase complete before C-phase.

D-phase fill: Trigger = replica lag > 5s / lag metric fires split-brain alert. System State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Data at Risk = inventory count integrity; post-merge count non-deterministic; adequacy judgment: `last-write-wins` is inadequate for inventory reservation — `manual-reconcile` with lower-count-wins rule required. Recovery Path — Stage 1 Detect/TTD: server → lag alert fires / VS named; Stage 2 Contain/TTC: operator → writes fenced to primary / VS named; Stage 3 Recover/TTR: server → `manual-reconcile` resolution job / VS named; Stage 4 Validate/TTV: operator → post-merge cross-check / VS named.
C-phase fill: Scenario name; Class 3; Severity Impaired <1% users high integrity risk; User Capability; Status Quo Risk = Class 3 carrying cost from Step 1b. Acute branches: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback without notification → silent cancellation.

The Chaos Block for Row 3 belongs immediately after — before the Gap Register begins. The Gap Register depends on all three chaos blocks being complete to ensure finding descriptions are grounded in testable evidence.

**Chaos Block — Row 3 (co-located).**

Fill: Inject / Expected Behavior / Pass Signal / Fail Signal — all four required with named observables.

Row 3 is ready to advance when scenario cells and Chaos Block are both complete with all four chaos components.

---

### Output Table

Produce a **single unified table**. After each scenario row, append its co-located Chaos Test Block immediately — before the next row begins.

The correct output structure is: Row 1 → Chaos Block 1 → Row 2 → Chaos Block 2 → Row 3 → Chaos Block 3 → Gap Register. Producing a separate chaos section after all three rows, or splitting the table by column owner, produces a structurally non-conforming output: **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows. Do not consolidate chaos blocks into a separate section.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows and their co-located chaos blocks, produce a Gap Register with exactly three labeled findings. Each finding includes inline observability metadata — placing this metadata in a separate section is a structural drift that the completeness checklist will register as a finding format failure.

**Per-finding format**:
> **[Finding Type] — [specific, actionable description]**
> `Metric:` [named monitoring metric surfacing this gap]
> `Alert:` [condition triggering alert on that metric]
> `Owner:` [Commerce Expert / Distributed Systems Expert / SRE]

1. **Offline Experience Gap** — specific Class 1 capability not addressed. `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — specific Class 2 or 3 violation the system cannot currently detect or correct. `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — specific absent mechanism. `Metric:` ... `Alert:` ... `Owner:` ...

A finding without all three inline fields is incomplete against the format requirement. Generic descriptions are incomplete against the content requirement.

Produce one **Inertia Verdict**: given the carrying costs from Step 1b and the gaps identified, what is the inertia threat level (HIGH / MEDIUM / LOW) and what is the single strongest argument against deferral? (2–3 sentences.) The verdict should synthesize rather than restate — connecting the carrying costs to the specific gaps surfaced.

Then produce the **Finding Completeness Checklist** as output content — this is a required output section, not a reader audit tool:

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap in one phrase]
[ ] Data Consistency Violation — [named violation in one phrase]
[ ] Missing Recovery Flow — [named mechanism in one phrase]
Finding types present: ___ of 3
```

A correct count ("3 of 3") is only accurate when all three finding types are genuinely present with specific, non-generic content and all three inline fields complete. Writing "3 of 3" without meeting those conditions produces an inaccurate checklist.

---
---

## V-04 — Inertia-Dominant Spine: Investment Framework Leads

**Variation axes**: Inertia framing dominant + lifecycle emphasis on pre-table phase. The Inertia Assessment is elevated to a full Investment Case with four sub-sections per class. The scenario table is positioned as evidence for the investment claims. The post-gap synthesis becomes an Investment Verdict with a recommended action tier.

**Hypothesis**: When the business decision framework is the primary organizing spine — and the scenario table is explicitly framed as evidence that informs the verdict rather than the primary deliverable — the model integrates chronic-consequence thinking into the row fills more naturally. Status Quo Risk cells referencing a pre-committed investment analysis are more likely to contain substantive rate+horizon+metric fills than rows where carrying cost is a trailing annotation. The Investment Verdict may produce stronger HIGH/MEDIUM/LOW justifications when it explicitly synthesizes gap findings + carrying costs.

---

You are running **flow-resilience** for topic: {Topic}.

---

### Investment Case (complete before all other sections)

The Investment Case is the primary output of this skill. The scenario table and gap register exist to support it with evidence. Produce the full Investment Case before the scenario table.

**Part A — Status Quo Threat**

Name the status-quo competitor: the do-nothing path teams actually take when they defer resilience investment for this topic. Assess the threat level as HIGH / MEDIUM / LOW with one-sentence justification. Describe what the current system does under each failure class without any resilience investment:

- Class 1 (full connectivity loss): current behavior without intervention
- Class 2 (partial failure): current behavior without intervention
- Class 3 (split-brain / concurrent write conflict): current behavior without intervention

**Part B — Carrying Costs by Class**

For each class, specify the chronic accumulation without remediation. All three components are required: rate qualifier (accumulation interval or trigger), horizon qualifier (trajectory without intervention), named business metric.

Format: *[named metric] accumulates at [rate], [horizon trajectory] without intervention*

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

These three carrying costs are pre-committed constraints. Every Status Quo Risk cell in the scenario table must reference the relevant class carrying cost — not author an independent risk statement.

**Part C — Tipping Point Signals**

For each class, one observable threshold at which deferral becomes indefensible — the empirical evidence that carrying costs have crossed a decision boundary.

Format: *[quantified threshold condition] / [named metric being monitored]*

- Class 1 tipping point:
- Class 2 tipping point:
- Class 3 tipping point:

**Part D — Remediation Thresholds**

For each class, name the intervention that would stop the carrying cost from accumulating. One sentence per class: "If [specific remediation] is implemented, [Class N carrying cost metric] stabilizes."

- Class 1 remediation threshold:
- Class 2 remediation threshold:
- Class 3 remediation threshold:

> The Investment Case is complete only when all four parts (A, B, C, D) contain non-placeholder content for all three failure classes. Do not begin the architecture section until the Investment Case is complete.

---

### Five-Level Anti-Omission Architecture

The scenario table evidence is structured across five anti-omission levels so that the model cannot produce a structurally incomplete evidence artifact.

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table + chaos blocks before Gap Register | Phase gate: all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first gate: D-owned columns complete before C-owned | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications with actor-chain notation | Column Contract (below) |

**Anti-boundary instruction**: All scenario rows appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** The Investment Case is a pre-table section — not a structural boundary inside the scenario table. Chaos Test Blocks are co-located row-appended supplements — **not a standalone chaos section, not a standalone chaos table**. Per-finding observability metadata is inline at finding granularity — **not a standalone observability section**.

---

### Chaos Test Block Specification

Each scenario row is immediately followed by a co-located Chaos Test Block — positioned before the next row.

| Component | Fill Requirement |
|-----------|-----------------|
| **Inject** | Named failure condition: service + injection method + duration. Reproducible in a test harness. |
| **Expected Behavior** | Named observables during injection if handled correctly. |
| **Pass Signal** | Named observable confirming the system handled the failure per the row's recovery path. |
| **Fail Signal** | Named observable confirming failure to handle. |

---

### Column Contract

> Process before constructing any row. Status Quo Risk must use the carrying cost pre-committed in Investment Case Part B for the relevant class — not an independently authored risk statement.
>
> **Conflict vocabulary constraint**: Canonical vocabulary only: `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale`. Free-text descriptions do not satisfy this constraint.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying threshold crossing. |
| System State | D | Service states, data states, replication state. Name specific services. Class 3: canonical conflict vocabulary required. |
| Data at Risk | D | Consistency violation type + scope. Class 3: canonical conflict vocabulary + adequacy judgment. |
| Recovery Path | D | All four stage sub-specifications with actor-chain notation. Every stage: actor-chain mechanism + SLA target + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | **Class 1** / **Class 2** / **Class 3**. No merging. |
| Severity + Blast Radius | C | Severity level + affected user segment. |
| User Capability | C | What the user can still do — at least one surviving capability. |
| Status Quo Risk | C | **Must reference Investment Case Part B** for this class: rate + horizon + named metric. Three components required. |

**Column order**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications with Actor-Chain Notation**

Each stage mechanism begins with `client →`, `server →`, `operator →`, or `user →`. At least three of four stages per row carry a labeled prefix.

> **Stage 1 — Detect / TTD**: Mechanism: [actor →] action. SLA: TTD. VS: named observable confirming detection.
> **Stage 2 — Contain / TTC**: Mechanism: [actor →] action. SLA: TTC. VS: named observable confirming containment.
> **Stage 3 — Recover / TTR**: Mechanism: [actor →] action. SLA: TTR. VS: named observable confirming recovery.
> **Stage 4 — Validate / TTV**: Mechanism: [actor →] action. SLA: TTV. VS: named observable confirming validation.

---

### Section Order Requirement

Produce all 3 scenario rows, each immediately followed by its co-located Chaos Test Block, before writing the Gap Register. Do not write the Investment Verdict until the Gap Register and Completeness Checklist are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.** This row is the primary evidence for the Class 1 carrying cost named in Investment Case Part B. The Status Quo Risk cell must reference that carrying cost explicitly — a row-1 Status Quo Risk cell that authors an independent risk statement is inconsistent with the Investment Case framing.

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat no-response. System State = order-service unreachable; local cart cached; payment token pending. Data at Risk = uncommitted cart state (stale write risk), pending token (expiry risk). Recovery Path — Stage 1: client → detects offline / VS named; Stage 2: client → writes queued with idempotency key / VS named; Stage 3: client → queue flushes, server → idempotency endpoint / VS named; Stage 4: server → confirms order state / VS named.
C-phase fill: Scenario name; Class 1; Severity Impaired ~2% sessions; User Capability; Status Quo Risk = Class 1 carrying cost from Investment Case Part B (rate + horizon + named metric). Acute branches: no idempotency → double-charge; no queue → cart lost; naive retry → oversell.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column including all four Recovery Path stage sub-specifications each with actor-chain mechanism, SLA, and named VS, and a Status Quo Risk cell referencing Investment Case Part B with all three components.**

**Chaos Block — Row 1 (co-located; complete before Row 2).**

Fill: Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 2 until Row 1 scenario cells AND Chaos Block both contain non-placeholder content with all four chaos components.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.** This row is the primary evidence for the Class 2 carrying cost named in Investment Case Part B.

Column-group gate (D-phase first): complete D-phase before C-phase.

D-phase fill: Trigger = inventory error rate > 5% / 60s / probe 503 × 3. System State = circuit breaker OPEN; snapshot stale. Data at Risk = reservation accuracy; oversell risk. Recovery Path — Stage 1: server → circuit breaker trips / VS named; Stage 2: server → snapshot-mode + buffer / VS named; Stage 3: server → half-open, operator → reconciliation / VS named; Stage 4: operator → counts verified / VS named.
C-phase fill: Scenario; Class 2; Severity Degraded all orders; User Capability; Status Quo Risk = Class 2 carrying cost from Investment Case Part B. Acute branches: no breaker → cascade; no snapshot → blocked; no buffer → oversell.

**Do not advance to the Chaos Block until all four Recovery Path stages have actor-chain mechanism, SLA, and named VS, and Status Quo Risk references Investment Case Part B with rate, horizon, and named metric.**

**Chaos Block — Row 2 (co-located; complete before Row 3).**

Fill: Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 3 until Row 2 cells AND Chaos Block are complete.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.** This row is the primary evidence for the Class 3 carrying cost named in Investment Case Part B. The Data at Risk cell must include a conflict resolution strategy in canonical vocabulary — "the most recent write wins" does not satisfy the canonical vocabulary constraint.

Column-group gate (D-phase first): complete D-phase before C-phase.

D-phase fill: Trigger = replica lag > 5s / lag metric fires split-brain alert. System State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Data at Risk = inventory count integrity; adequacy judgment: `last-write-wins` inadequate — `manual-reconcile` required. Recovery Path — Stage 1: server → lag alert fires / VS named; Stage 2: operator → writes fenced to primary / VS named; Stage 3: server → `manual-reconcile` job / VS named; Stage 4: operator → post-merge cross-check / VS named.
C-phase fill: Scenario; Class 3; Severity Impaired <1% users high integrity risk; User Capability; Status Quo Risk = Class 3 carrying cost from Investment Case Part B. Acute branches: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback → silent cancellation.

**Do not advance to the Chaos Block until all four Recovery Path stages have actor-chain mechanism, SLA, and named VS, a Data at Risk entry with canonical conflict vocabulary and adequacy judgment, and Status Quo Risk referencing Investment Case Part B with all three components.**

**Chaos Block — Row 3 (co-located; complete before Gap Register).**

Fill: Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to the Gap Register until Row 3 cells AND Chaos Block are complete with all four components.**

---

### Output Table

Produce a **single unified table**. After each scenario row, append its co-located Chaos Test Block immediately.

**Do not create separate tables for Distributed Systems Expert and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows. Do not consolidate chaos blocks into a separate section. Do not produce a standalone observability section.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

Produce a Gap Register with exactly three findings, each with inline observability metadata — not a separate observability section.

**Per-finding format**:
> **[Finding Type] — [specific description]**
> `Metric:` [named metric] `Alert:` [condition] `Owner:` [role]

1. **Offline Experience Gap** — `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — `Metric:` ... `Alert:` ... `Owner:` ...

---

### Investment Verdict

Synthesize the Investment Case (Part B carrying costs + Part C tipping point signals) with the three Gap Register findings into a formal verdict.

**Inertia threat level**: HIGH / MEDIUM / LOW

**Evidence**: Name the single gap finding with the strongest connection to the pre-committed carrying costs. In 2–3 sentences, state why this gap makes deferral indefensible at current trajectory — referencing both the carrying cost metric and the tipping point signal from Part C.

**Recommended action tier**: Given the findings and carrying costs, what is the minimum intervention that would stop the most costly carrying cost from accumulating? Name the specific recovery flow, circuit-breaker implementation, or conflict resolution strategy.

Then produce the **Finding Completeness Checklist** as output content:

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap]
[ ] Data Consistency Violation — [named violation]
[ ] Missing Recovery Flow — [named mechanism]
Finding types present: ___ of 3
```

Mark each `[x]` only when that finding is specific, actionable, non-generic, and has all three inline fields complete. Write "3 of 3" only when all three pass.

---
---

## V-05 — Compact Synthesis: Minimum Viable Structure, All 30 Criteria

**Variation axes**: All axes, minimum prose overhead. The architecture table, anti-boundary umbrella, chaos specification, and column contract are consolidated to eliminate redundancy. Row descriptors are shorter. The C-38 umbrella carries all four escape negations in a single compact block without per-section restatement. Every load-bearing element for all 30 criteria is present; no element appears twice.

**Hypothesis**: The minimum-token prompt that still achieves 30/30 is structurally valuable: it reveals which elements are load-bearing (cannot be removed without dropping a criterion) and which are restatements. A compact V-05 is also more maintainable — future criteria additions need not navigate lengthy preamble.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment

Produce before the scenario table. Do not advance until all three parts are non-placeholder for all three classes.

**1a. Status Quo Threat**: Name the do-nothing path. HIGH / MEDIUM / LOW with one-sentence justification. What does the system do under each class without intervention?

**1b. Carrying Costs** (pre-committed constraints for Status Quo Risk column — each fill must reference these):
- Class 1: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 2: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 3: *[named metric] accumulates at [rate], [horizon] without intervention*

**1c. Tipping Point Signals** (quantified threshold + named metric per class):
- Class 1:
- Class 2:
- Class 3:

---

### Pre-Output Specification

**Five-Level Anti-Omission Architecture**

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows | `#` row-index + anti-split instruction | Output table (below) |
| Section | Table + chaos blocks → Gap Register | Phase gate: rows + chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | Within row | Bold in-row imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within row: D-phase → C-phase | D-first intra-row gate: D-owned columns complete before C-owned | Column Contract (below) |
| Column | Per column | Named owner + stage sub-specs with actor-chain notation | Column Contract (below) |

**Anti-boundary umbrella** (four escape forms closed simultaneously): **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns [escape 1: table split]. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts [escape 2: intra-table boundary]. Do not consolidate chaos blocks into a standalone chaos section or standalone chaos table [escape 3: chaos consolidation]. Do not produce a standalone observability section or observability table for Gap Register findings [escape 4: observability consolidation].**

**Chaos Test Block Specification**

| Component | Fill Requirement |
|-----------|-----------------|
| Inject | Named: service + method + duration. Reproducible in test harness. |
| Expected Behavior | Named observables during injection if handled correctly. |
| Pass Signal | Named observable confirming correct handling per row's recovery path. |
| Fail Signal | Named observable confirming failure to handle. |

**Column Contract** — process before any row; column omission is a contract violation.

> **Conflict vocabulary constraint**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale` — canonical label required; free-text descriptions do not satisfy.
> **Status Quo Risk constraint**: must use Step 1b metric for the row's class; rate + horizon + named metric all required.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | 1, 2, 3. |
| Trigger Condition | D | (1) Threshold expression — quantified activation. (2) Detection signal — observable crossing mechanism. Both required. |
| System State | D | Named services, data states, consistency model. Class 3: canonical conflict vocabulary. |
| Data at Risk | D | Consistency violation type + scope. Class 3: canonical vocabulary + adequacy judgment. |
| Recovery Path | D | 4 stages with actor-chain notation: mechanism (`client →` / `server →` / `operator →` / `user →`) + SLA (TTD/TTC/TTR/TTV) + named VS. ≥3 of 4 stages must carry labeled actor prefix. |
| Scenario Name | C | Specific commerce operation + failure mode. |
| Class Label | — | Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded/Impaired/Down) + affected segment. |
| User Capability | C | What user can still do. ≥1 surviving capability. |
| Status Quo Risk | C | Step 1b carrying cost for this class. Rate + horizon + named metric. |

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Section Order Requirement**: Produce all 3 rows (each followed immediately by its Chaos Block) before the Gap Register. Gap Register before Inertia Verdict. Inertia Verdict before Recommendations.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss)**

**Write this row now.**

D-first gate: Trigger Condition, System State, Data at Risk, all four Recovery Path stages (actor-chain + SLA + VS each) complete before Scenario Name, Class Label, Severity, User Capability, Status Quo Risk.

D-phase: Trigger = keepalive fails 3 × 10s / heartbeat no-response [threshold + detection]. State = order-service unreachable; cart cached; payment token pending. Risk = uncommitted cart (stale-write risk); token (expiry risk). Recovery: Stage 1 client → heartbeat / TTD / VS: offline-indicator in UI; Stage 2 client → idempotency-keyed write queue / TTC / VS: queue-depth > 0 in telemetry; Stage 3 client → queue flush, server → idempotency endpoint / TTR / VS: 200 + idempotency-key echo; Stage 4 server → order state confirmed / TTV / VS: order-id in sync response matches draft.
C-phase: Scenario name; Class 1; Impaired ~2%; surviving capability; Status Quo Risk = Class 1 Step 1b (rate + horizon + metric). Acute: no idempotency → double-charge [C-27]; no queue → cart lost; naive retry → oversell. Chronic: if Class 1 gap never addressed, [metric from Step 1b] accumulates at [rate], [horizon] [C-29 / C-31].

**Do not advance to Chaos Block until every column is non-placeholder, including all four Recovery Path stages each with actor-chain mechanism (labeled prefix), SLA target, and named VS, and Status Quo Risk with rate + horizon + named metric from Step 1b.**

**Chaos Block — Row 1 (co-located).**
Inject: [named]; Expected Behavior: [named observables]; Pass Signal: [named]; Fail Signal: [named]. All four required.

**Do not advance to Row 2 until Row 1 cells AND Chaos Block are complete.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

D-first gate: same as Row 1.

D-phase: Trigger = error rate > 5% / 60s / probe 503 × 3 [threshold + detection]. State = circuit breaker OPEN; snapshot stale. Risk = reservation accuracy; oversell against stale count. Recovery: Stage 1 server → breaker trips / TTD / VS: breaker-state = OPEN in dashboard; Stage 2 server → snapshot-mode + oversell buffer / TTC / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Stage 3 server → half-open, operator → reconciliation / TTR / VS: probe 200 + reconciliation = COMPLETE; Stage 4 operator → counts verified / TTV / VS: discrepancy-counter = 0 for 5 min.
C-phase: Scenario; Class 2; Degraded all orders in window; capability; Status Quo Risk = Class 2 Step 1b. Acute: no breaker → cascade; no snapshot → blocked; no buffer → oversell. Chronic: if Class 2 gap never addressed, [metric from Step 1b] accumulates at [rate], [horizon].

**Do not advance to Chaos Block until all four stages have actor-chain mechanism, SLA, and VS, and Status Quo Risk has rate + horizon + metric.**

**Chaos Block — Row 2 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 3 until Row 2 cells AND Chaos Block are complete.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

D-first gate: same as Rows 1–2.

D-phase: Trigger = replica lag > 5s / lag metric fires split-brain alert [threshold + detection]. State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Risk = inventory count integrity; `last-write-wins` inadequate — `manual-reconcile` with lower-count-wins required [adequacy judgment]. Recovery: Stage 1 server → lag alert fires / TTD / VS: conflict-alert with partition-id in alerting system; Stage 2 operator → writes fenced to primary / TTC / VS: write-fence = PRIMARY-ONLY in config store; Stage 3 server → `manual-reconcile` resolution job / TTR / VS: resolution-job = COMPLETE, 0 unresolved; Stage 4 operator → post-merge cross-check / TTV / VS: consistency-check = 0 discrepancies.
C-phase: Scenario; Class 3; Impaired <1% high-integrity risk; capability; Status Quo Risk = Class 3 Step 1b. Acute: `last-write-wins` → oversell [C-27]; naive `merge` → phantom inventory; rollback → silent cancellation. Chronic: if Class 3 gap never addressed, [metric from Step 1b] accumulates at [rate], [horizon] [C-29 / C-31].

**Do not advance to Chaos Block until all four stages have actor-chain mechanism, SLA, and VS; Data at Risk names canonical conflict strategy with adequacy judgment; Status Quo Risk has rate + horizon + metric.**

**Chaos Block — Row 3 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Gap Register until Row 3 cells AND Chaos Block are complete.**

---

### Output Table

Single unified table. After each row, append its co-located Chaos Block before the next row. **Do not split by column owner. Do not insert horizontal rules between rows. Do not consolidate chaos blocks. Do not produce standalone observability section.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

Three findings, inline observability at finding granularity — not a separate section.

**Format per finding**:
> **[Finding Type] — [specific description]**
> `Metric:` [named] `Alert:` [condition] `Owner:` [role]

1. **Offline Experience Gap** — `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — `Metric:` ... `Alert:` ... `Owner:` ...

**Inertia Verdict**: Step 1b carrying costs + gaps above → HIGH / MEDIUM / LOW + single strongest argument against deferral (2–3 sentences).

**Finding Completeness Checklist** (required output content):

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap]
[ ] Data Consistency Violation — [named violation]
[ ] Missing Recovery Flow — [named mechanism]
Finding types present: ___ of 3
```

Mark `[x]` only when finding is specific, actionable, non-generic, all three inline fields present. Write "3 of 3" only when all three pass.

---
---

## Projected Criterion Coverage — R13 Variations

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-09 | Chaos Test Block: Inject / Expected / Pass / Fail | PASS | PASS | PASS | PASS | PASS |
| C-10 | Per-finding observability hooks: Metric / Alert / Owner | PASS | PASS | PASS | PASS | PASS |
| C-11 | Actor-chain notation on Recovery Path stages | PASS | PASS | PASS | PASS | PASS |
| C-12 | Constrained conflict vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-13 | Gap-merge prevention via self-verifying count | PASS | PASS | PASS | PASS | PASS |
| C-14 | Chaos blocks co-located per row, anti-boundary | PASS | PASS | PASS | PASS | PASS |
| C-15 | Observability hooks inline, not standalone section | PASS | PASS | PASS | PASS | PASS |
| C-16 | Completeness checklist as model-generated output | PASS | PASS | PASS | PASS | PASS |
| C-17 | `#` column + anti-split instruction | PASS | PASS | PASS | PASS | PASS |
| C-18 | Section-level phase gate (rows + chaos before Gap Register) | PASS | PASS | PASS | PASS | PASS |
| C-19 | Slot-level in-row bold imperatives | PASS | PASS | PASS* | PASS | PASS |
| C-20 | Column-level ownership assignment | PASS | PASS | PASS | PASS | PASS |
| C-21 | Five-level anti-omission architecture named | PASS | PASS | PASS | PASS | PASS |
| C-22 | Anti-boundary by structural symptom | PASS | PASS | PASS | PASS | PASS |
| C-23 | In-row bold imperative at cell granularity | PASS | PASS | PASS* | PASS | PASS |
| C-24 | Column meta-table before output table | PASS | PASS | PASS | PASS | PASS |
| C-25 | Two-symptom anti-boundary (table split + intra-table boundary) | PASS | PASS | PASS | PASS | PASS |
| C-26 | Architecture-to-contract forward reference by section name | PASS | PASS | PASS | PASS | PASS |
| C-27 | Consequence enumeration per row descriptor | PASS | PASS | PASS | PASS | PASS |
| C-28 | Sub-field completeness gate naming stage sub-structure | PASS | PASS | PASS | PASS | PASS |
| C-29 | Chronic consequence (carrying cost, per row) | PASS | PASS | PASS | PASS | PASS |
| C-31 | Three-component chronic accumulation (rate + horizon + metric) | PASS | PASS | PASS | PASS | PASS |
| C-32 | Five-level architecture — column-group gate as 5th level | PASS | PASS | PASS | PASS | PASS |
| C-33 | Trigger condition: threshold expression + detection signal | PASS | PASS | PASS | PASS | PASS |
| C-34 | Verification signal per recovery stage (mechanism + SLA + VS) | PASS | PASS | PASS | PASS | PASS |
| C-35 | Pre-table inertia with per-class carrying costs pre-committed | PASS | PASS | PASS | PASS | PASS |
| C-36 | Per-class tipping point signal (quantified + named metric) | PASS | PASS | PASS | PASS | PASS |
| C-37 | Inertia verdict after Gap Register, references gaps + costs | PASS | PASS | PASS | PASS | PASS |
| C-38 | Four-escape anti-boundary umbrella in single block | PASS | PASS | PASS | PASS | PASS |

*V-03 softens imperative phrasing; bold emphasis and structural gate language still present at slot granularity. C-19 and C-23 pass conditions require bold imperative text co-located at cell level — V-03 satisfies this with "**Begin Row N here.**" and "Row N is complete only when..." constructions. Risk: scoring judges may apply stricter "Write this row now / Do not advance" pattern matching. V-03 is the highest-risk variation for C-19/C-23.

**Projected scores (v12 denominator 30)**: All five variations project 30/30 → composite 100.00. Discriminator is structural diversity achieving the same ceiling, not ceiling movement.

**R13 structural discriminators**:

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| Role sequence | C-first | D-first | D-first | D-first | D-first |
| Gap Register format | Finding-forward | Observability-forward | Finding-forward | Finding-forward | Finding-forward |
| Imperative form | Bold hard-stop | Bold hard-stop | Explanation-backed | Bold hard-stop | Bold hard-stop |
| Inertia framing | Standard Step 1 | Standard Step 1 | Standard Step 1 | Investment Case (expanded) | Compact Step 1 |
| Prompt length | ~R12 V-05 | ~R12 V-05 | Longer (explanations) | Longer (Investment Case) | Shorter (compressed) |
| C-19/C-23 risk | Low | Low | Medium | Low | Low |
| Novelty value | Role sequence reversal | Observability-first format | Register experiment | Business-decision spine | Minimum viable structure |
