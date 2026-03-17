# flow-resilience — Round 12 Variations (Rubric v11)

**Rubric**: v11 · 29 aspirational criteria (C-09 – C-37) · Ceiling entering R12: 21/29 → 97.24 (R11 V-03 and V-05)
**Open criteria entering R12**: None new in v11 — all three v11 additions (C-35/C-36/C-37) cracked by R11.
**Persistent uncracked block**: C-09 through C-16 (8 criteria, never targeted across any round).
**R12 objective**: All five variations carry the full R11 ceiling (21/29). Variation axes probe C-09–C-16 territory.

**Variation axes chosen:**
- **Axis D — Chaos Co-Location** (C-09 + C-14): Each scenario row carries a co-located Chaos Test Block (Inject / Expected Behavior / Pass Signal / Fail Signal) appended immediately after the row — never consolidated into a standalone chaos section. The advance inhibitor gate is extended to include chaos block completion.
- **Axis E — Per-Finding Observability + Completeness Checklist** (C-10 + C-13 + C-15 + C-16): Gap Register findings carry inline observability metadata (Metric / Alert / Owner) co-located at finding granularity. The output contains a fill-in completeness checklist confirming "3 of 3" finding types present.
- **Axis F — Recovery Specificity Upgrade** (C-11 + C-12): Recovery Path stage mechanisms use actor-chain notation (`client →`, `server →`, `operator →`) as labeled prefixes. Conflict resolution strategies use canonical vocabulary (`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`) — no free-text paraphrase.

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | D only: Chaos co-location | Embedding a chaos block inside each row descriptor forces runnable test specifications at scenario granularity; co-location prevents deferral to a standalone section where chaos blocks are routinely compressed or dropped |
| V-02 | E only: Observability + completeness checklist | Requiring Metric/Alert/Owner adjacent to each finding transforms the Gap Register from narrative to structured specification; the in-artifact checklist makes finding omission visible as a self-evident count failure |
| V-03 | F only: Recovery specificity upgrade | Mandating actor-chain prefixes and constrained conflict vocabulary replaces free-text descriptions with template-fill constraints; constrained vocabulary eliminates the paraphrase failure mode (e.g., "most recent write wins" → `last-write-wins`) |
| V-04 | D + E: Chaos + observability | Chaos blocks and observability hooks address orthogonal output sections (scenario rows vs. Gap Register); combining should produce no structural interference |
| V-05 | D + E + F: All three new axes | All three axes address distinct structural slots: chaos blocks target scenario rows, observability hooks target Gap Register findings, actor-chain/conflict-vocab target Recovery Path column content — they should compose without conflict |

---

## V-01 — Axis D: Chaos Co-Location

**Variation axis**: Each scenario row carries a co-located Chaos Test Block appended immediately after it. Chaos blocks are never consolidated into a standalone section. The advance-inhibitor gate for each row includes chaos block completion as a non-bypass condition.

**Hypothesis**: When chaos scenarios are embedded co-located with each row descriptor, the model fills them in sequence at scenario granularity. A standalone chaos section invites deferral and collapse; an in-row co-located block makes omission structurally visible as an incomplete row rather than a missing section.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment (complete before scenario table)

Before building the scenario table, produce an Inertia Assessment naming the status-quo competitor — the cost of doing nothing about resilience gaps for this topic.

**1a. Status Quo Threat**: Name the do-nothing path. Why do teams defer resilience investment for this topic? Assess the threat: HIGH / MEDIUM / LOW with one-sentence justification. What does the current system actually do under each failure class (Class 1 / Class 2 / Class 3) without intervention?

**1b. Carrying Costs by Class**: For each failure class, name the chronic accumulation that persists without remediation. Format: *[named metric] accumulates at [rate], [horizon trajectory] without intervention*.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: For each class, name one observable threshold at which deferral becomes indefensible (quantified condition + named metric being monitored, e.g., "oversell-event count exceeds 50/month", "cart-abandonment rate rises > 2% above baseline").

> Produce the Inertia Assessment now. Do not advance to the architecture section until all three parts (1a, 1b, 1c) are complete for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table + chaos blocks before Gap Register | Phase gate: all 3 rows complete with co-located chaos blocks before Gap Register begins | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first sequencing gate: complete all D-owned columns before beginning any C-owned columns within the same row | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** Chaos Test Blocks are co-located supplements appended immediately after each scenario row — **they are not a separate chaos section, not a standalone chaos-engineering table, and not a structural boundary** within the scenario output.

---

### Chaos Test Block Specification

Each scenario row is immediately followed by a co-located Chaos Test Block in the output. The chaos block appears after the row and before the next row begins. **Do not consolidate the three chaos blocks into a single separate section.**

Each chaos block requires all four components:

| Component | Fill Requirement |
|-----------|-----------------|
| **Inject** | Named failure condition: service or component + injection method (e.g., "kill inventory-service pod via `kubectl delete pod`", "drop all client-server TCP packets for 60s via network policy", "halt write replication on replica-1 for 10s via replica pause"). Must be reproducible in a test harness. |
| **Expected Behavior** | What the monitoring dashboard, user, and operator should observe during the injection if the system handles it correctly. Name specific observables (not desired end-states). |
| **Pass Signal** | Named observable confirming the system handled the failure per the recovery path (e.g., "circuit-breaker = OPEN in dashboard within 60s, orders queued, zero checkout errors in error-rate monitor"). |
| **Fail Signal** | Named observable confirming the system failed to handle the failure (e.g., "order-service error rate > 50%, circuit-breaker = CLOSED, oversell-event count > 0 in inventory monitor"). |

---

### Column Contract

> Process this contract before constructing any row. Column omission is a contract violation, not an oversight. Status Quo Risk entries must be consistent with Inertia Assessment Step 1b.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified condition activating the scenario. (2) *Detection signal* — observable mechanism identifying the threshold crossing. Qualitative-only descriptions fail. |
| System State | D | Service states, data states, replication state, consistency model in effect. Name specific services and their operational modes. |
| Data at Risk | D | Specific consistency violation type (stale read, lost write, write-write conflict, phantom read) + scope. |
| Recovery Path | D | All four stage sub-specifications (see below). Every stage: mechanism + SLA target + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** (full connectivity loss) / **Class 2** (partial failure) / **Class 3** (split-brain). No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment and scale. |
| User Capability | C | What the user *can still do*. At least one surviving capability named. |
| Status Quo Risk | C | Must use the metric and framing from Inertia Assessment Step 1b for this class. *Rate* + *horizon* + *named business metric*. All three required. |

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications**

> **Stage 1 — Detect / TTD**
> *Mechanism*: signal or action surfacing the failure condition.
> *SLA target*: TTD — time-to-detect commitment.
> *VS*: named observable confirming detection complete (e.g., "offline banner renders in UI", "circuit-breaker = OPEN in observability dashboard", "conflict-detection-alert fires with partition-id in alerting system").

> **Stage 2 — Contain / TTC**
> *Mechanism*: action bounding blast radius and preventing propagation.
> *SLA target*: TTC — time-to-contain commitment.
> *VS*: named observable confirming containment active (e.g., "write-queue depth > 0 in client telemetry", "inventory-accept-mode = CONSERVATIVE in feature flag store", "write-fence-flag = PRIMARY-ONLY in distributed config store").

> **Stage 3 — Recover / TTR**
> *Mechanism*: action restoring normal service operation.
> *SLA target*: TTR — time-to-recover commitment.
> *VS*: named observable confirming recovery complete (e.g., "order-service 200 with idempotency-key echo", "health probe returns 200 + reconciliation-job-status = COMPLETE", "resolution-job-status = COMPLETE with 0 unresolved records").

> **Stage 4 — Validate / TTV**
> *Mechanism*: action confirming post-recovery system consistency.
> *SLA target*: TTV — time-to-validate commitment.
> *VS*: named observable confirming validation complete (e.g., "order-id in sync response matches local draft", "reconciliation-discrepancy-counter = 0 for 5 consecutive min", "inventory-order-consistency-check = 0 discrepancies").

---

### Section Order Requirement

Produce all 3 scenario rows, each immediately followed by its co-located Chaos Test Block, before writing the Gap Register. Do not write the Gap Register until Row 3 and its Chaos Block are complete. Do not write Recommendations until the Gap Register is complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (mechanism + SLA target + named VS each) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat returns no response. System State = order-service unreachable from client; local cart state cached in app memory; payment-authorization token pending; no write path to server. Data at Risk = uncommitted cart modifications (stale write risk); pending payment-authorization token (expiry risk); orphaned server reservation until recovery sync. Recovery Path: Stage 1 Detect/TTD = client heartbeat detects offline / VS: offline-indicator renders in UI; Stage 2 Contain/TTC = pending writes queued locally with idempotency key / VS: local write-queue depth > 0 logged to client telemetry; Stage 3 Recover/TTR = queue flushes through idempotency-protected endpoint on reconnect / VS: order-service returns 200 with idempotency-key echo; Stage 4 Validate/TTV = order state confirmed server-side / VS: order-id returned in sync response matches local draft.
C-phase fill: Scenario = "Checkout Interrupted — Client Offline Mid-Payment"; Class 1; Severity Impaired, ~2% sessions; User Capability = browse cached product catalog, queue draft order for retry; Status Quo Risk = must use Class 1 carrying cost from Step 1b (rate + horizon + metric). Acute branches: no idempotency key → double-charge on reconnect; no local queue → cart state lost on disconnect; naive retry without TTD gate → inventory oversell during reconnect burst.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 1 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 1 (co-located; complete before advancing to Row 2).**

Fill: Inject = [specific, named injection to simulate Class 1 in a test harness — name the service, the method, and the duration]; Expected Behavior = [what monitoring, user, and operator should observe during the injection if the system handles it correctly — name specific observables, not desired states]; Pass Signal = [named observable confirming the system handled the failure per the Row 1 recovery path]; Fail Signal = [named observable confirming the system failed to handle the failure].

**Do not advance to Row 2 until the scenario cells AND the Chaos Block both contain non-placeholder content with all four chaos components (Inject, Expected Behavior, Pass Signal, Fail Signal).**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory-service error rate exceeds 5% over 60s rolling window / health probe returns 503 for 3 consecutive probes on 10s interval. System State = order-service operational; inventory-service circuit-breaker OPEN; last-known snapshot stale by TTD seconds; payment-service operational. Data at Risk = inventory reservation accuracy — reads against stale snapshot may oversell; orders placed during outage may commit against unavailable counts. Recovery Path: Stage 1 Detect/TTD = circuit breaker opens at error threshold / VS: circuit-breaker-state metric = OPEN in observability dashboard; Stage 2 Contain/TTC = orders accepted only against stale snapshot with oversell buffer / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Stage 3 Recover/TTR = service recovers, circuit breaker half-opens, reconciliation job runs / VS: health probe 200 + reconciliation-job-status = COMPLETE; Stage 4 Validate/TTV = counts verified against commitments made during outage / VS: reconciliation-discrepancy-counter = 0 for 5 consecutive min.
C-phase fill: Scenario = "Order Placement During Inventory Service Outage"; Class 2; Severity Degraded, all users placing orders during window; User Capability = browse and search catalog (cached), add to cart, place orders against snapshot with oversell buffer; Status Quo Risk = use Class 2 carrying cost from Step 1b. Acute branches: no circuit breaker → cascading failure into order-service; no snapshot fallback → all order placement blocked; no oversell buffer → customer-visible oversell on recovery.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 2 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 2 (co-located; complete before advancing to Row 3).**

Fill: Inject = [specific, named injection to simulate Class 2 in a test harness]; Expected Behavior = [monitoring + operator + user signals during injection if handled correctly]; Pass Signal = [named observable confirming correct handling per Row 2 recovery path]; Fail Signal = [named observable confirming failure to handle].

**Do not advance to Row 3 until the scenario cells AND the Chaos Block both contain non-placeholder content with all four chaos components.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = write-replica replication lag on inventory store exceeds 5s / replica-lag metric fires split-brain detection alert. System State = two nodes each accepting writes to the same inventory record; vector clocks diverged; last-write-wins policy active without application-level conflict detection; eventual consistency promised but partition not healed. Data at Risk = inventory count integrity — concurrent reservation commits from partitioned nodes may each decrement the same stock; post-merge count non-deterministic without conflict-resolution rule. Recovery Path: Stage 1 Detect/TTD = replication-lag alert fires at threshold crossing / VS: conflict-detection-alert fires with partition-id and affected-record set in alerting system; Stage 2 Contain/TTC = writes to conflicting records fenced to primary node only / VS: write-fence-flag = PRIMARY-ONLY in distributed config store; Stage 3 Recover/TTR = conflict-resolution job merges diverged records with lower-count-wins rule / VS: resolution-job-status = COMPLETE with 0 unresolved records; Stage 4 Validate/TTV = post-merge counts cross-checked against order commitments placed during partition / VS: inventory-order-consistency-check = 0 discrepancies.
C-phase fill: Scenario = "Concurrent Inventory Reservation — Partition Write Conflict"; Class 3; Severity Impaired, <1% users (high-contention SKUs during flash sale), high data integrity risk; User Capability = reserve inventory on primary node, view cart totals, proceed to checkout (conflict pending resolution); Status Quo Risk = use Class 3 carrying cost from Step 1b. Acute branches: last-write-wins without app-level detection → both orders fulfilled → oversell; naive higher-count merge → phantom inventory; rollback without notification → silent order cancellation.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 3 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 3 (co-located; complete before advancing to Gap Register).**

Fill: Inject = [specific, named injection to simulate Class 3 in a test harness]; Expected Behavior = [monitoring + operator + user signals during injection if handled correctly]; Pass Signal = [named observable confirming correct handling per Row 3 recovery path]; Fail Signal = [named observable confirming failure to handle].

**Do not advance to the Gap Register until Row 3's scenario cells AND its Chaos Block both contain non-placeholder content with all four chaos components (Inject, Expected Behavior, Pass Signal, Fail Signal).**

---

### Output Table

Produce a **single unified table**. All three scenario rows appear in this one table. After each scenario row, append its co-located Chaos Test Block immediately — before the next row begins.

**Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts. Do not consolidate the three chaos blocks into a separate chaos-engineering section — each chaos block is co-located with its row.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows and their co-located chaos blocks, produce a Gap Register with exactly three labeled, actionable findings:

1. **Offline Experience Gap** — specific capability breaking under Class 1, not addressed by the current recovery path.
2. **Data Consistency Violation** — specific violation under Class 2 or Class 3 the system cannot currently detect or correct.
3. **Missing Recovery Flow** — specific mechanism absent from the current implementation and required to complete the lifecycle.

Produce one **Inertia Verdict**: given the carrying costs named in Step 1b and the gaps identified above, is inertia a HIGH / MEDIUM / LOW threat, and what is the single strongest argument against deferral? (2–3 sentences.)

Generic statements fail. Name the specific gap, violation, missing mechanism, and inertia argument.

---
---

## V-02 — Axis E: Per-Finding Observability + Completeness Checklist

**Variation axis**: The Gap Register is upgraded to require per-finding inline observability metadata (Metric / Alert / Owner) co-located at finding granularity, not as a standalone observability section. The output must also contain a fill-in completeness checklist confirming all three finding types present.

**Hypothesis**: Requiring Metric, Alert, and Owner adjacent to each finding transforms the Gap Register from a narrative into a structured specification. A standalone observability section can be collapsed or omitted under token pressure; per-finding inline hooks cannot be omitted without a structurally visible finding entry missing its required fields. The in-artifact checklist makes omission manifest as a count failure ("2 of 3") rather than requiring the reader to audit prose.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment (complete before scenario table)

**1a. Status Quo Threat**: Name the do-nothing path. Why do teams defer resilience investment for this topic? Assess: HIGH / MEDIUM / LOW with one-sentence justification. What does the current system do under each failure class without intervention?

**1b. Carrying Costs by Class**: For each failure class, name the chronic accumulation without remediation. Format: *[metric] accumulates at [rate], [horizon trajectory] without intervention*.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: For each class, name one observable threshold at which deferral becomes indefensible (quantified condition + named metric, e.g., "oversell-event count exceeds 50/month").

> Produce the Inertia Assessment now. Do not advance until all three parts are complete for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table before Gap Register | Phase gate: all 3 rows complete before Gap Register begins | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first sequencing gate: complete all D-owned columns before beginning C-owned columns | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** The Inertia Assessment is a pre-table section — not a structural boundary within the scenario table.

---

### Column Contract

> Process this contract before constructing any row. Column omission is a contract violation. Status Quo Risk entries must be consistent with Inertia Assessment Step 1b.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified condition activating the scenario. (2) *Detection signal* — observable mechanism identifying threshold crossing. Qualitative-only fails. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. |
| Data at Risk | D | Specific consistency violation type + scope. |
| Recovery Path | D | All four stage sub-specifications (see below). Every stage: mechanism + SLA target + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** / **Class 2** / **Class 3**. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment and scale. |
| User Capability | C | What the user *can still do*. At least one surviving capability. |
| Status Quo Risk | C | Must use the metric and framing from Inertia Assessment Step 1b for this class. *Rate* + *horizon* + *named business metric*. All three required. |

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications**

> **Stage 1 — Detect / TTD**: *Mechanism* | *SLA target*: TTD | *VS*: named observable confirming detection complete.

> **Stage 2 — Contain / TTC**: *Mechanism* | *SLA target*: TTC | *VS*: named observable confirming containment active.

> **Stage 3 — Recover / TTR**: *Mechanism* | *SLA target*: TTR | *VS*: named observable confirming recovery complete.

> **Stage 4 — Validate / TTV**: *Mechanism* | *SLA target*: TTV | *VS*: named observable confirming validation complete.

---

### Section Order Requirement

Produce all 3 scenario rows before writing the Gap Register. Do not write the Gap Register until all rows are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (mechanism + SLA + named VS) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat no-response. System State = order-service unreachable; local cart cached; payment token pending; no write path to server. Data at Risk = uncommitted cart state (stale write); pending payment token (expiry); orphaned server reservation. Recovery: Detect/TTD = heartbeat detects offline / VS: offline-indicator in UI; Contain/TTC = writes queued with idempotency key / VS: write-queue > 0 in client telemetry; Recover/TTR = queue flushes on reconnect through idempotency-protected endpoint / VS: order-service 200 with idempotency-key echo; Validate/TTV = order state confirmed server-side / VS: order-id in sync response matches local draft.
C-phase fill: Scenario = "Checkout Interrupted — Client Offline Mid-Payment"; Class 1; Impaired, ~2% sessions; User Capability = browse cached catalog, draft-order queue; Status Quo Risk = must use Class 1 carrying cost from Step 1b. Acute branches: no idempotency → double-charge; no queue → cart lost; naive retry → oversell.

**Do not advance to Row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 1 carrying cost from Step 1b with rate, horizon, and named metric.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory error rate > 5% / 60s rolling window / probe 503 × 3 on 10s. System State = circuit breaker OPEN; snapshot stale by TTD; payment-service operational. Data at Risk = inventory reservation accuracy, oversell against stale count. Recovery: Detect/TTD = circuit breaker trips at threshold / VS: circuit-breaker-state = OPEN in observability dashboard; Contain/TTC = orders accepted with oversell buffer / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Recover/TTR = service recovers, breaker half-opens, reconciliation runs / VS: probe 200 + reconciliation-job = COMPLETE; Validate/TTV = counts verified against commitments / VS: discrepancy-counter = 0 for 5 min.
C-phase fill: Scenario = "Order Placement During Inventory Service Outage"; Class 2; Degraded, all orders in window; User Capability = browse cached, add to cart, place with oversell buffer; Status Quo Risk = must use Class 2 carrying cost from Step 1b. Acute branches: no circuit breaker → cascade; no snapshot → blocked; no buffer → customer-visible oversell.

**Do not advance to Row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 2 carrying cost from Step 1b with rate, horizon, and named metric.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = replica lag > 5s / replica-lag metric fires split-brain alert. System State = two nodes accepting writes; vector clocks diverged; LWW active without app-level conflict detection. Data at Risk = inventory count integrity, non-deterministic post-merge count. Recovery: Detect/TTD = lag alert fires at threshold / VS: conflict-detection-alert with partition-id in alerting system; Contain/TTC = writes fenced to primary only / VS: write-fence-flag = PRIMARY-ONLY in config store; Recover/TTR = conflict-resolution job merges with lower-count-wins rule / VS: resolution-job = COMPLETE with 0 unresolved records; Validate/TTV = post-merge counts cross-checked against commitments / VS: consistency-check = 0 discrepancies.
C-phase fill: Scenario = "Concurrent Inventory Reservation — Partition Write Conflict"; Class 3; Impaired, <1% users, high data integrity risk; User Capability = reserve on primary, view cart, proceed to checkout; Status Quo Risk = must use Class 3 carrying cost from Step 1b. Acute branches: LWW without detection → both orders fulfilled; naive higher-count merge → phantom inventory; rollback without notification → silent cancellation.

**Do not advance to the Gap Register until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 3 carrying cost from Step 1b with rate, horizon, and named metric.**

---

### Output Table

Produce a **single unified table**. All three rows appear in this one table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows, produce a Gap Register with exactly three labeled findings. Each finding must include inline observability metadata co-located with the finding — not in a separate observability section.

**Per-finding format**:

> **[Finding Type] — [specific, actionable description]**
> `Metric:` [named monitoring metric that would surface this gap in production]
> `Alert:` [condition on that metric that triggers an alert, e.g., "metric > threshold for N consecutive samples"]
> `Owner:` [role responsible for monitoring and response — Commerce Expert / Distributed Systems Expert / SRE]

Required findings (each must include all three inline fields):

1. **Offline Experience Gap** — specific capability breaking under Class 1, not addressed by the recovery path. `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — specific violation under Class 2 or Class 3 the system cannot currently detect or correct. `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — specific mechanism absent from the current implementation. `Metric:` ... `Alert:` ... `Owner:` ...

A finding without all three inline fields (Metric, Alert, Owner) fails the format requirement. Generic descriptions ("offline support may be limited") fail the content requirement.

After the three findings, produce one **Inertia Verdict**: given the carrying costs from Step 1b and the gaps identified above, is inertia HIGH / MEDIUM / LOW, and what is the single strongest argument against deferral? (2–3 sentences.)

Then produce the **Finding Completeness Checklist** as output content:

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap in one phrase]
[ ] Data Consistency Violation — [named violation in one phrase]
[ ] Missing Recovery Flow — [named mechanism in one phrase]
Finding types present: ___ of 3
```

Mark each checkbox `[x]` only when that finding type is present with specific, actionable, non-generic content. Write "Finding types present: 3 of 3" only if all three pass. If any finding is missing or generic, leave its checkbox unchecked and write the true count.

---
---

## V-03 — Axis F: Recovery Specificity Upgrade

**Variation axis**: Recovery Path stages require actor-chain notation (`client →`, `server →`, `operator →`, `user →`) as labeled handoff prefixes on Mechanism fields. Conflict resolution strategies across all columns use canonical vocabulary (`last-write-wins` | `merge` | `manual-reconcile` | `reject-stale`) — free-text paraphrase is prohibited.

**Hypothesis**: Free-text actor attribution ("the system retries", "operators monitor") produces ambiguous ownership. Actor-chain prefixes make handoffs labeled constraints rather than prose choices. Similarly, "the most recent write wins" is semantically equivalent to `last-write-wins` but escapes C-12's pass condition — a constrained vocabulary requirement forces the canonical term and eliminates the paraphrase escape route.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment (complete before scenario table)

**1a. Status Quo Threat**: Name the do-nothing path. Assess threat: HIGH / MEDIUM / LOW with one-sentence justification. What does the current system do under each failure class without intervention?

**1b. Carrying Costs by Class**: For each class, name the chronic accumulation without remediation. Format: *[metric] accumulates at [rate], [horizon trajectory] without intervention*.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: One observable threshold per class at which deferral becomes indefensible (quantified condition + named metric).

> Produce the Inertia Assessment now. Do not advance until all three parts are complete for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table before Gap Register | Phase gate: all 3 rows complete before Gap Register | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first gate: complete all D-owned columns before C-owned | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.**

---

### Column Contract

> Process this contract before constructing any row. Column omission is a contract violation. Status Quo Risk entries must be consistent with Inertia Assessment Step 1b.
>
> **Conflict vocabulary constraint**: All references to conflict resolution strategies in any column must use canonical vocabulary: `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale`. Free-text descriptions (e.g., "the most recent write wins", "reconcile manually", "prefer the lower value") do not satisfy this constraint — the canonical term must appear as a discrete label. This constraint applies to System State, Data at Risk, Recovery Path, and any other column containing a conflict resolution reference.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying threshold crossing. Qualitative-only fails. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. For Class 3 rows, name the active conflict resolution strategy using canonical vocabulary. |
| Data at Risk | D | Specific consistency violation type + scope. For Class 3 rows, name the conflict resolution strategy assumed using canonical vocabulary and include an adequacy judgment: is the strategy appropriate for this data type? |
| Recovery Path | D | All four stage sub-specifications (see below). Every stage: actor-chain mechanism + SLA target + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** / **Class 2** / **Class 3**. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment. |
| User Capability | C | What the user *can still do*. At least one surviving capability. |
| Status Quo Risk | C | Must use metric and framing from Inertia Assessment Step 1b. *Rate* + *horizon* + *named metric*. All three required. |

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications with Actor-Chain Notation**

Each stage's Mechanism must begin with an actor-chain prefix identifying the initiating actor: `client →`, `server →`, `operator →`, or `user →`. At least three of the four stages in every row must carry an actor-chain prefix. A mechanism described in prose without a labeled actor prefix does not satisfy the actor-chain requirement.

> **Stage 1 — Detect / TTD**
> *Mechanism*: [actor →] action surfacing the failure.
> *SLA target*: TTD.
> *VS*: named observable confirming detection complete (e.g., "client → offline-indicator renders in UI", "server → circuit-breaker-state = OPEN in dashboard").

> **Stage 2 — Contain / TTC**
> *Mechanism*: [actor →] action bounding blast radius.
> *SLA target*: TTC.
> *VS*: named observable confirming containment active (e.g., "client → write-queue depth > 0 in telemetry", "server → inventory-accept-mode = CONSERVATIVE in feature flag store").

> **Stage 3 — Recover / TTR**
> *Mechanism*: [actor →] action restoring service.
> *SLA target*: TTR.
> *VS*: named observable confirming recovery complete (e.g., "server → order-service 200 with idempotency echo", "operator → reconciliation-job = COMPLETE").

> **Stage 4 — Validate / TTV**
> *Mechanism*: [actor →] action confirming post-recovery consistency.
> *SLA target*: TTV.
> *VS*: named observable confirming validation complete (e.g., "server → order-id in sync response matches draft", "operator → discrepancy-counter = 0 for 5 min").

---

### Section Order Requirement

Produce all 3 scenario rows before writing the Gap Register. Do not write the Gap Register until all rows are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (actor-chain mechanism + SLA + named VS each) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat no-response. System State = order-service unreachable; cart cached locally; payment token pending. Data at Risk = uncommitted cart state (stale write risk), pending payment token (expiry risk). Recovery Path with actor-chain notation: Stage 1 Detect/TTD = client → heartbeat detects offline within 30s / VS: offline-indicator in UI; Stage 2 Contain/TTC = client → writes queued with idempotency key / VS: write-queue > 0 in client telemetry; Stage 3 Recover/TTR = client → queue flushes through idempotency-protected endpoint on reconnect, server → returns 200 / VS: order-service 200 with idempotency echo; Stage 4 Validate/TTV = server → confirms order state / VS: order-id in sync response matches local draft.
C-phase fill: Scenario = "Checkout Interrupted — Client Offline Mid-Payment"; Class 1; Impaired, ~2% sessions; User Capability = browse cached catalog, queue draft order; Status Quo Risk = must use Class 1 carrying cost from Step 1b. Acute branches: no idempotency → double-charge; no queue → cart lost; naive retry → oversell.

**Do not advance to Row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 1 carrying cost from Step 1b with rate, horizon, and named metric.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (actor-chain mechanism + SLA + named VS) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory error rate > 5% / 60s rolling / probe 503 × 3 on 10s. System State = circuit breaker OPEN; snapshot stale. Data at Risk = inventory reservation accuracy, oversell against stale count. Recovery Path with actor-chain notation: Stage 1 Detect/TTD = server → circuit breaker trips at threshold / VS: circuit-breaker-state = OPEN in observability dashboard; Stage 2 Contain/TTC = server → orders accepted with oversell buffer applied / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Stage 3 Recover/TTR = server → circuit breaker half-opens, operator → reconciliation job triggered / VS: probe 200 + reconciliation-job = COMPLETE; Stage 4 Validate/TTV = operator → count verification against commitments / VS: discrepancy-counter = 0 for 5 min.
C-phase fill: Scenario = "Order Placement During Inventory Service Outage"; Class 2; Degraded, all orders in window; User Capability = browse cached, add to cart, place with buffer; Status Quo Risk = must use Class 2 carrying cost from Step 1b. Acute branches: no circuit breaker → cascade; no snapshot → blocked; no buffer → customer-visible oversell.

**Do not advance to Row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 2 carrying cost from Step 1b.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (actor-chain mechanism + SLA + named VS) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = replica lag > 5s / lag metric fires split-brain alert. System State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active without app-level conflict detection (canonical vocabulary required). Data at Risk = inventory count integrity — non-deterministic post-merge count under `last-write-wins`; both conflicting writes may succeed; adequacy judgment: `last-write-wins` is inadequate for inventory reservation — lower-count-wins or `merge` with reservation semantics required. Recovery Path with actor-chain notation: Stage 1 Detect/TTD = server → replication-lag alert fires / VS: conflict-detection-alert with partition-id in alerting system; Stage 2 Contain/TTC = operator → writes fenced to primary via config change / VS: write-fence-flag = PRIMARY-ONLY in config store; Stage 3 Recover/TTR = server → conflict-resolution job executes `manual-reconcile` with lower-count-wins rule / VS: resolution-job = COMPLETE with 0 unresolved records; Stage 4 Validate/TTV = operator → post-merge counts verified against commitments / VS: consistency-check = 0 discrepancies.
C-phase fill: Scenario = "Concurrent Inventory Reservation — Partition Write Conflict"; Class 3; Impaired, <1% users, high integrity risk; User Capability = reserve on primary, view cart, checkout; Status Quo Risk = must use Class 3 carrying cost from Step 1b. Acute branches: `last-write-wins` without detection → oversell; naive higher-count merge → phantom inventory; rollback without notification → silent cancellation.

**Do not advance to the Gap Register until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism (labeled with canonical actor prefix), SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 3 carrying cost from Step 1b, and a Data at Risk entry naming the conflict resolution strategy using canonical vocabulary with an adequacy judgment.**

---

### Output Table

Produce a **single unified table**. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows, produce a Gap Register with exactly three labeled, actionable findings:

1. **Offline Experience Gap** — specific capability breaking under Class 1, not addressed by the recovery path.
2. **Data Consistency Violation** — specific violation under Class 2 or Class 3 the system cannot detect or correct.
3. **Missing Recovery Flow** — specific mechanism absent from the current implementation.

Produce one **Inertia Verdict**: given the carrying costs from Step 1b and the gaps identified above, is inertia HIGH / MEDIUM / LOW, and what is the single strongest argument against deferral? (2–3 sentences.)

Generic statements fail. Name the specific gap, violation, missing mechanism, and inertia argument.

---
---

## V-04 — Axes D + E: Chaos Co-Location + Per-Finding Observability + Completeness Checklist

**Variation axes**: Chaos Test Blocks co-located per scenario row (Axis D) combined with per-finding inline observability hooks and completeness checklist (Axis E).

**Hypothesis**: Axes D and E address orthogonal structural positions — chaos blocks target scenario rows (during table construction), observability hooks target Gap Register findings (after table completion). They should compose without structural interference: completing each row's chaos block is a condition for advancing to the next row; completing all findings with inline hooks is a condition for writing the completeness checklist.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment (complete before scenario table)

**1a. Status Quo Threat**: Name the do-nothing path. Assess threat: HIGH / MEDIUM / LOW with one-sentence justification. What does the current system do under each failure class without intervention?

**1b. Carrying Costs by Class**: For each class, name the chronic accumulation without remediation. *[metric] accumulates at [rate], [horizon] without intervention*.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: One observable threshold per class at which deferral becomes indefensible (quantified condition + named metric).

> Produce the Inertia Assessment now. Do not advance until all three parts are complete for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table + chaos blocks before Gap Register | Phase gate: all rows + co-located chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first gate | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for D and C columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.** Chaos Test Blocks are co-located supplements appended immediately after each scenario row — **not a separate chaos section, not a standalone table, not a structural boundary** within the scenario output. Per-finding observability metadata is inline with each Gap Register finding — **not a separate observability section**.

---

### Chaos Test Block Specification

Each scenario row is immediately followed by a co-located Chaos Test Block. Do not consolidate chaos blocks into a separate section.

| Component | Fill Requirement |
|-----------|-----------------|
| **Inject** | Named failure condition: service + injection method + duration. Reproducible in a test harness. |
| **Expected Behavior** | Named observables (dashboard, operator, user) during injection if handled correctly. |
| **Pass Signal** | Named observable confirming correct handling per the row's recovery path. |
| **Fail Signal** | Named observable confirming failure to handle. |

---

### Column Contract

> Process this contract before constructing any row. Status Quo Risk entries must be consistent with Inertia Assessment Step 1b.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | Threshold expression + detection signal. Both required. Qualitative-only fails. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. |
| Data at Risk | D | Consistency violation type + scope. |
| Recovery Path | D | All four stage sub-specifications. Every stage: mechanism + SLA + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity level + affected user segment. |
| User Capability | C | What the user can still do. At least one capability. |
| Status Quo Risk | C | Use Inertia Assessment Step 1b metric for this class. Rate + horizon + named metric. |

**Column order**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications**

> **Stage 1 — Detect / TTD**: *Mechanism* | TTD | *VS*: named observable confirming detection.
> **Stage 2 — Contain / TTC**: *Mechanism* | TTC | *VS*: named observable confirming containment.
> **Stage 3 — Recover / TTR**: *Mechanism* | TTR | *VS*: named observable confirming recovery.
> **Stage 4 — Validate / TTV**: *Mechanism* | TTV | *VS*: named observable confirming validation.

---

### Section Order Requirement

Produce all 3 scenario rows, each immediately followed by its co-located Chaos Test Block, before writing the Gap Register. Do not write the Gap Register until Row 3 and its Chaos Block are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat no-response. System State = order-service unreachable; cart cached locally; payment token pending. Data at Risk = uncommitted cart state, pending payment token. Recovery: Detect/TTD = heartbeat detects offline / VS: offline-indicator in UI; Contain/TTC = writes queued with idempotency key / VS: write-queue > 0 in client telemetry; Recover/TTR = queue flushes on reconnect through idempotency-protected endpoint / VS: order-service 200 with idempotency echo; Validate/TTV = server confirms order state / VS: order-id in sync response matches draft.
C-phase fill: Class 1; Impaired, ~2% sessions; browse cached catalog, draft-order queue; Status Quo Risk = Class 1 carrying cost from Step 1b. Acute branches: no idempotency → double-charge; no queue → cart lost; naive retry → oversell.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS.**

**Chaos Block — Row 1 (co-located; complete before advancing to Row 2).**
Inject = [named failure injection for Class 1]; Expected Behavior = [named observables if handled correctly]; Pass Signal = [named observable confirming correct handling]; Fail Signal = [named observable confirming failure]. All four components required.

**Do not advance to Row 2 until scenario cells AND Chaos Block both contain non-placeholder content.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory error rate > 5% / 60s / probe 503 × 3. System State = circuit breaker OPEN; snapshot stale. Data at Risk = inventory reservation accuracy, oversell against stale count. Recovery: Detect/TTD = circuit breaker trips / VS: breaker-state = OPEN in dashboard; Contain/TTC = orders with oversell buffer / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Recover/TTR = service recovers, reconciliation runs / VS: probe 200 + reconciliation = COMPLETE; Validate/TTV = counts verified / VS: discrepancy-counter = 0 for 5 min.
C-phase fill: Class 2; Degraded, all orders in window; browse cached, place with buffer; Status Quo Risk = Class 2 carrying cost from Step 1b. Acute branches: no circuit breaker → cascade; no snapshot → blocked; no buffer → oversell.

**Do not advance to the Chaos Block until all four Recovery Path stages each have mechanism, SLA target, and named VS.**

**Chaos Block — Row 2 (co-located; complete before advancing to Row 3).**
Inject = [named failure injection for Class 2]; Expected Behavior = [named observables if handled correctly]; Pass Signal = [named observable confirming correct handling]; Fail Signal = [named observable confirming failure].

**Do not advance to Row 3 until scenario cells AND Chaos Block both contain non-placeholder content.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = replica lag > 5s / lag metric fires split-brain alert. System State = two nodes accepting writes; vector clocks diverged; LWW active. Data at Risk = inventory count integrity, non-deterministic post-merge count. Recovery: Detect/TTD = lag alert fires / VS: conflict-alert with partition-id in alerting system; Contain/TTC = writes fenced to primary / VS: write-fence = PRIMARY-ONLY in config store; Recover/TTR = conflict-resolution job with lower-count-wins rule / VS: resolution-job = COMPLETE, 0 unresolved; Validate/TTV = post-merge cross-check / VS: consistency-check = 0 discrepancies.
C-phase fill: Class 3; Impaired, <1% users, high integrity risk; reserve on primary, view cart, checkout; Status Quo Risk = Class 3 carrying cost from Step 1b. Acute branches: LWW → both fulfilled; naive merge → phantom inventory; rollback → silent cancellation.

**Do not advance to the Chaos Block until all four Recovery Path stages each have mechanism, SLA target, and named VS.**

**Chaos Block — Row 3 (co-located; complete before advancing to Gap Register).**
Inject = [named failure injection for Class 3]; Expected Behavior = [named observables if handled correctly]; Pass Signal = [named observable confirming correct handling]; Fail Signal = [named observable confirming failure]. All four components required.

**Do not advance to the Gap Register until Row 3's scenario cells AND its Chaos Block both contain non-placeholder content with all four chaos components.**

---

### Output Table

Produce a **single unified table**. After each scenario row, append its co-located Chaos Test Block immediately — before the next row. **Do not create separate D/C tables. Do not insert a horizontal rule or section break between rows. Do not consolidate chaos blocks into a separate section.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all rows and chaos blocks, produce a Gap Register with exactly three findings, each with inline observability metadata. **Do not produce a separate observability section — the metadata is inline with each finding.**

**Per-finding format**:
> **[Finding Type] — [specific description]**
> `Metric:` [named metric surfacing this gap in production]
> `Alert:` [condition triggering an alert on that metric]
> `Owner:` [Commerce Expert / Distributed Systems Expert / SRE]

1. **Offline Experience Gap** — specific Class 1 capability not addressed by the recovery path. `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — specific Class 2 or 3 violation the system cannot detect/correct. `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — specific absent mechanism. `Metric:` ... `Alert:` ... `Owner:` ...

Produce one **Inertia Verdict**: carrying costs from Step 1b + gaps identified → HIGH / MEDIUM / LOW threat + single strongest argument against deferral (2–3 sentences).

Then produce the **Finding Completeness Checklist** as output content:

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap]
[ ] Data Consistency Violation — [named violation]
[ ] Missing Recovery Flow — [named mechanism]
Finding types present: ___ of 3
```

Mark `[x]` only when the finding is specific, actionable, and non-generic with all three inline fields present. Write "3 of 3" only when all three pass.

---
---

## V-05 — Axes D + E + F: All Three New Axes

**Variation axes**: Chaos co-location (D) + per-finding observability and completeness checklist (E) + actor-chain notation and constrained conflict vocabulary (F). All three axes applied simultaneously to the R11 V-05 base.

**Hypothesis**: The three axes address orthogonal structural slots: D targets scenario row content (chaos blocks appended per row), E targets Gap Register finding content (inline hooks + completeness checklist), F targets Recovery Path column content (actor-chain notation) and Data at Risk content (conflict vocabulary). Because each axis operates at a distinct structural position, they should compose without interference — each should independently improve a distinct set of criteria without competing for the same structural slot.

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
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-first gate: complete all D-owned columns before beginning C-owned | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications with actor-chain notation | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** The Inertia Assessment is a pre-table section — not a structural boundary within the scenario table. Chaos Test Blocks are co-located supplements appended immediately after each row — **not a separate chaos section, not a standalone chaos table, not a structural boundary**. Per-finding observability metadata is inline with each Gap Register finding — **not a separate observability section**.

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
> **Conflict vocabulary constraint (applies to all columns)**: All references to conflict resolution strategies must use canonical vocabulary: `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale`. Free-text descriptions (e.g., "the most recent write wins", "reconcile manually") do not satisfy this constraint — the canonical term must appear as a discrete label. Applies to System State, Data at Risk, Recovery Path, and any other column containing a conflict resolution reference.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying threshold crossing. Qualitative-only fails. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. For Class 3 rows, name the active conflict resolution strategy using canonical vocabulary. |
| Data at Risk | D | Specific consistency violation type + scope. For Class 3 rows, name the conflict resolution strategy using canonical vocabulary and include an adequacy judgment (is this strategy appropriate for this data type?). |
| Recovery Path | D | All four stage sub-specifications with actor-chain notation (see below). Every stage: actor-chain mechanism + SLA target + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** / **Class 2** / **Class 3**. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment. |
| User Capability | C | What the user *can still do*. At least one surviving capability. |
| Status Quo Risk | C | Must use metric and framing from Inertia Assessment Step 1b for this class. *Rate* + *horizon* + *named business metric*. All three required. |

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Recovery Path — Stage Sub-Specifications with Actor-Chain Notation**

Each stage's Mechanism must begin with an actor-chain prefix: `client →`, `server →`, `operator →`, or `user →`. At least three of the four stages in every row must carry a labeled actor-chain prefix. A mechanism described in prose without an actor prefix does not satisfy the actor-chain requirement.

> **Stage 1 — Detect / TTD**
> *Mechanism*: [actor →] action surfacing the failure condition.
> *SLA target*: TTD — time-to-detect commitment.
> *VS*: named observable confirming detection complete (e.g., "client → offline-indicator renders in UI", "server → circuit-breaker-state = OPEN in observability dashboard", "server → conflict-detection-alert fires with partition-id in alerting system").

> **Stage 2 — Contain / TTC**
> *Mechanism*: [actor →] action bounding blast radius.
> *SLA target*: TTC — time-to-contain commitment.
> *VS*: named observable confirming containment active (e.g., "client → write-queue depth > 0 in telemetry", "server → inventory-accept-mode = CONSERVATIVE in feature flag store", "operator → write-fence-flag = PRIMARY-ONLY in config store").

> **Stage 3 — Recover / TTR**
> *Mechanism*: [actor →] action restoring service.
> *SLA target*: TTR — time-to-recover commitment.
> *VS*: named observable confirming recovery complete (e.g., "client → queue flushes, server → returns 200 with idempotency echo", "server → health probe 200 + reconciliation-job = COMPLETE", "server → resolution-job = COMPLETE with 0 unresolved").

> **Stage 4 — Validate / TTV**
> *Mechanism*: [actor →] action confirming post-recovery consistency.
> *SLA target*: TTV — time-to-validate commitment.
> *VS*: named observable confirming validation complete (e.g., "server → order-id in sync response matches local draft", "operator → discrepancy-counter = 0 for 5 consecutive min", "operator → consistency-check = 0 discrepancies").

---

### Section Order Requirement

Produce all 3 scenario rows, each immediately followed by its co-located Chaos Test Block, before writing the Gap Register. Do not write the Gap Register until Row 3 and its Chaos Block are complete. Do not write Recommendations until the Gap Register and Completeness Checklist are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (actor-chain mechanism + SLA target + named VS each) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat returns no response. System State = order-service unreachable from client; local cart state cached in app memory; payment-authorization token pending; no write path to server available. Data at Risk = uncommitted cart modifications (stale write risk); pending payment-authorization token (expiry risk); orphaned server reservation until recovery sync. Recovery Path with actor-chain notation: Stage 1 Detect/TTD = client → heartbeat detects offline within 30s / VS: offline-indicator renders in UI; Stage 2 Contain/TTC = client → pending writes queued with idempotency key / VS: write-queue depth > 0 logged to client telemetry; Stage 3 Recover/TTR = client → queue flushes through idempotency-protected endpoint on reconnect, server → returns 200 / VS: order-service 200 with idempotency-key echo; Stage 4 Validate/TTV = server → confirms order state post-sync / VS: order-id returned in sync response matches local draft.
C-phase fill: Scenario = "Checkout Interrupted — Client Offline Mid-Payment"; Class 1; Severity Impaired, ~2% sessions; User Capability = browse cached product catalog, queue draft order for retry; Status Quo Risk = must use Class 1 carrying cost from Step 1b (rate + horizon + named metric). Acute consequence branches: no idempotency key → double-charge on reconnect; no local queue → cart state lost on disconnect; naive retry without TTD gate → inventory oversell during reconnect burst.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism (labeled actor prefix), SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 1 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 1 (co-located; complete before advancing to Row 2).**

Fill: Inject = [specific, named injection to simulate Class 1 in a test harness — name the service, the method, and the duration]; Expected Behavior = [named observables on dashboard, for operator, and for user during injection if the system handles the failure correctly]; Pass Signal = [named observable confirming the system handled the failure per the Row 1 recovery path — circuit-breaker state, queue depth, or reconnect signal]; Fail Signal = [named observable confirming the system failed to handle the failure — error rate, queue depth zero, or customer-visible failure signal].

**Do not advance to Row 2 until this row's scenario cells AND the Chaos Block both contain non-placeholder content with all four chaos components (Inject, Expected Behavior, Pass Signal, Fail Signal).**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (actor-chain mechanism + SLA + named VS each) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory-service error rate exceeds 5% over 60s rolling window / health probe returns 503 for 3 consecutive probes on 10s interval. System State = order-service operational; inventory-service circuit-breaker OPEN; last-known inventory snapshot stale by TTD seconds; payment-service operational. Data at Risk = inventory reservation accuracy — reads against stale snapshot may commit against unavailable counts; orders during outage may oversell. Recovery Path with actor-chain notation: Stage 1 Detect/TTD = server → circuit breaker opens at error threshold / VS: circuit-breaker-state = OPEN in observability dashboard; Stage 2 Contain/TTC = server → orders accepted against snapshot with oversell buffer / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Stage 3 Recover/TTR = server → circuit breaker half-opens, operator → reconciliation job triggered / VS: health probe 200 + reconciliation-job-status = COMPLETE; Stage 4 Validate/TTV = operator → inventory counts verified against commitments / VS: reconciliation-discrepancy-counter = 0 for 5 consecutive min.
C-phase fill: Scenario = "Order Placement During Inventory Service Outage"; Class 2; Severity Degraded, all users placing orders during outage window; User Capability = browse and search cached catalog, add to cart, place orders (snapshot with oversell buffer); Status Quo Risk = must use Class 2 carrying cost from Step 1b. Acute branches: no circuit breaker → cascading failure; no snapshot → all order placement blocked; no oversell buffer → customer-visible oversell on recovery.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 2 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 2 (co-located; complete before advancing to Row 3).**

Fill: Inject = [specific, named injection to simulate Class 2 — inventory-service kill, network partition, or error injection]; Expected Behavior = [named observables on dashboard and for operator during injection if handled correctly]; Pass Signal = [named observable confirming correct handling per Row 2 recovery path]; Fail Signal = [named observable confirming failure to handle]. All four components required with named observables.

**Do not advance to Row 3 until Row 2 scenario cells AND the Chaos Block both contain non-placeholder content with all four chaos components.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (actor-chain mechanism + SLA + named VS each) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = write-replica replication lag on inventory store exceeds 5s / replica-lag metric fires split-brain detection alert. System State = two nodes each accepting writes to the same inventory record; vector clocks diverged; `last-write-wins` active without application-level conflict detection. Data at Risk = inventory count integrity — concurrent reservation commits from partitioned nodes may each decrement the same stock; post-merge count non-deterministic; adequacy judgment: `last-write-wins` is inadequate for inventory reservation — `manual-reconcile` with lower-count-wins rule required. Recovery Path with actor-chain notation: Stage 1 Detect/TTD = server → replication-lag alert fires at threshold / VS: conflict-detection-alert fires with partition-id and affected-record set in alerting system; Stage 2 Contain/TTC = operator → writes to conflicting records fenced to primary node via config change / VS: write-fence-flag = PRIMARY-ONLY in distributed config store within 60s; Stage 3 Recover/TTR = server → `manual-reconcile` conflict-resolution job runs with lower-count-wins rule / VS: resolution-job-status = COMPLETE with 0 unresolved records; Stage 4 Validate/TTV = operator → post-merge counts cross-checked against order commitments / VS: inventory-order-consistency-check = 0 discrepancies.
C-phase fill: Scenario = "Concurrent Inventory Reservation — Partition Write Conflict"; Class 3; Severity Impaired, <1% users (high-contention SKUs during flash sale), high data integrity risk; User Capability = reserve inventory on primary node, view cart totals, proceed to checkout (apparent success, conflict pending resolution); Status Quo Risk = must use Class 3 carrying cost from Step 1b. Acute branches: `last-write-wins` without detection → both orders fulfilled → oversell; naive higher-count merge → phantom inventory; rollback without notification → silent order cancellation.

**Do not advance to the Chaos Block until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with actor-chain mechanism (labeled actor prefix), SLA target, and named VS, a Data at Risk entry naming the conflict strategy in canonical vocabulary with an adequacy judgment, and a Status Quo Risk entry consistent with the Class 3 carrying cost from Step 1b with rate, horizon, and named metric.**

**Chaos Block — Row 3 (co-located; complete before advancing to Gap Register).**

Fill: Inject = [specific, named injection to simulate Class 3 — halt replication, introduce network partition between write nodes, or inject a concurrent write race]; Expected Behavior = [named observables during injection if the system detects and contains the partition correctly]; Pass Signal = [named observable confirming correct handling per Row 3 recovery path — write-fence state, resolution-job status, or conflict-alert firing]; Fail Signal = [named observable confirming failure — both nodes accepting conflicting writes, silent merge, or customer-visible duplicate fulfillment].

**Do not advance to the Gap Register until Row 3's scenario cells AND its Chaos Block both contain non-placeholder content with all four chaos components (Inject, Expected Behavior, Pass Signal, Fail Signal).**

---

### Output Table

Produce a **single unified table**. All three scenario rows appear in this one table. After each scenario row, append its co-located Chaos Test Block immediately — before the next row begins.

**Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts. Do not consolidate the three chaos blocks into a separate chaos-engineering section — each is co-located with its row.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows and their co-located chaos blocks, produce a Gap Register with exactly three labeled findings. Each finding must include inline observability metadata — **not a separate observability section**.

**Per-finding format**:
> **[Finding Type] — [specific, actionable description]**
> `Metric:` [named monitoring metric surfacing this gap in production]
> `Alert:` [condition on that metric triggering an alert, e.g., "metric > threshold for N samples"]
> `Owner:` [Commerce Expert / Distributed Systems Expert / SRE]

Required findings (each must include all three inline fields):

1. **Offline Experience Gap** — specific capability breaking under Class 1, not addressed by the recovery path. `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — specific violation under Class 2 or Class 3 the system cannot currently detect or correct. `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — specific mechanism absent from the current implementation. `Metric:` ... `Alert:` ... `Owner:` ...

A finding without all three inline fields (Metric, Alert, Owner) fails the format requirement. Generic descriptions fail the content requirement.

Produce one **Inertia Verdict**: given the carrying costs named in Step 1b and the gaps identified above, is inertia a HIGH / MEDIUM / LOW threat, and what is the single strongest argument against deferral? (2–3 sentences.)

Then produce the **Finding Completeness Checklist** as output content:

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap in one phrase]
[ ] Data Consistency Violation — [named violation in one phrase]
[ ] Missing Recovery Flow — [named mechanism in one phrase]
Finding types present: ___ of 3
```

Mark each checkbox `[x]` only when that finding type is present with specific, actionable, non-generic content and all three inline fields (Metric, Alert, Owner) complete. Write "Finding types present: 3 of 3" only when all three pass. If any finding is missing or generic, leave its checkbox unchecked and write the true count.

---
---

## Projected Criterion Coverage — R12 Variations

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-09 | Chaos Engineering Test Cases (runnable: inject + behavior + pass/fail) | **D** | — | — | **D** | **D** |
| C-10 | Observability Hooks tied to named gaps | — | **E** | — | **E** | **E** |
| C-11 | Named Actor Chain in Recovery Fields | — | — | **F** | — | **F** |
| C-12 | Constrained Conflict Resolution Vocabulary | — | — | **F** | — | **F** |
| C-13 | Structural Gap-Merge Prevention | — | **E** | — | **E** | **E** |
| C-14 | Chaos Table Co-Located Per Scenario | **D** | — | — | **D** | **D** |
| C-15 | Per-Finding Inline Observability Hook | — | **E** | — | **E** | **E** |
| C-16 | Completeness Checklist as Output Content | — | **E** | — | **E** | **E** |
| C-17–C-37 | Inherited from R11 V-05 baseline | all | all | all | all | all |

**Projected aspirational scores (v11 denominator 29)**:

| Variation | New criteria targeted | Projected pass count | Projected composite |
|-----------|-----------------------|---------------------|---------------------|
| V-01 | C-09, C-14 (Axis D) | 21 + 2 = 23/29 | 60 + 30 + 7.93 = **97.93** |
| V-02 | C-10, C-13, C-15, C-16 (Axis E) | 21 + 4 = 25/29 | 60 + 30 + 8.62 = **98.62** |
| V-03 | C-11, C-12 (Axis F) | 21 + 2 = 23/29 | 60 + 30 + 7.93 = **97.93** |
| V-04 | Axes D + E → C-09, C-10, C-13, C-14, C-15, C-16 | 21 + 6 = 27/29 | 60 + 30 + 9.31 = **99.31** |
| V-05 | Axes D + E + F → all 8 remaining | 21 + 8 = 29/29 | 60 + 30 + 10.00 = **100.00** |

*Projections assume all targeted criteria pass. Actual scores depend on rubric evaluation against generated output.*
