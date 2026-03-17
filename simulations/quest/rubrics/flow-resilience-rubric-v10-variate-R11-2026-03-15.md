# flow-resilience — Round 11 Variations (Rubric v10)

**Rubric**: v10 · 26 aspirational criteria · Ceiling entering R11: 18/26 → 96.92 (R10 V-05)
**Open criteria entering R11**: None — all three new criteria (C-32, C-33, C-34) cracked by R10 V-05.
**Persistent uncracked block**: C-09 through C-16 (8 criteria, unaddressed across all rounds).
**R11 objective**: All five variations carry the full R10 V-05 ceiling (18/26). Variation axes probe potential C-35+ territory. Single-axis first (V-01 through V-03), then combine.

**Variation axes chosen:**
- **Axis A — Role sequence**: which owner phase populates columns first within a row (standard: C-then-D; variation: D-then-C).
- **Axis B — Lifecycle emphasis**: Recovery Path stages given expanded structural prominence — each stage defined as a named sub-specification with explicit stage header, rather than listed inline in a fill requirement.
- **Axis C — Inertia framing**: Status-quo competitor (do-nothing inertia) featured as an explicit named section before the scenario table, with the Status Quo Risk column linking back to the inertia entry.

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | A only: D-phase-first column ordering | Reversing column-group gate direction tests whether D-phase-first sequencing improves technical completeness (Recovery Path filled before commerce framing applies pressure to abbreviate) |
| V-02 | B only: lifecycle stage sub-specifications | Making each stage a named structural element rather than an inline fill clause makes stage-level omission visible as a named-section gap rather than a fill shortfall |
| V-03 | C only: inertia-first framing | Leading with the "do nothing" cost before the scenario table forces chronic-consequence framing to be established before the acute scenarios are written, potentially elevating Status Quo Risk density |
| V-04 | A + B: D-phase-first + lifecycle sub-specs | D-owned Recovery Path fully specified before C-owned commerce framing; lifecycle stages named at section level within D-phase specification |
| V-05 | A + B + C: all three axes | D-phase-first + named lifecycle sub-specs + inertia-first framing: the richest specification of all three axes simultaneously |

---

## V-01 — Axis A: D-Phase-First Column Ordering

**Variation axis**: Role sequence — D-phase (Distributed Systems Expert) columns are ordered first in the Column Contract and the intra-row column-group gate runs D-phase-first, C-phase-second. Standard order is C-then-D; this variation reverses it.

**Hypothesis**: Filling the technical failure topology (D-phase: Trigger Condition, System State, Data at Risk, Recovery Path) before the business-impact layer (C-phase: Scenario Name, Severity, User Capability, Status Quo Risk) may improve Recovery Path completeness. When commerce framing is written first, SLA targets and Verification Signals are sometimes abbreviated under narrative pressure. D-phase-first forces full technical specification before any commerce framing is applied.

---

You are running **flow-resilience** for topic: {Topic}.

### Role Definitions

Two specialist roles contribute all columns in this analysis:

- **D — Distributed Systems Expert**: owns the technical failure topology. Columns (filled first within each row): Trigger Condition, System State, Data at Risk, Recovery Path.
- **C — Commerce Expert**: owns the business impact layer. Columns (filled second within each row): Scenario Name, Class Label, Severity + Blast Radius, User Capability, Status Quo Risk.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table before Gap Register | Phase gate: all rows complete before Gap Register begins | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase columns before C-phase columns | Intra-row D-phase-first sequencing gate: complete all D-owned columns before beginning any C-owned columns within the same row | Column Contract (below) |
| Column | Per column | Named owner in Column Contract | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** An in-progress row that contains only D-phase cells is not a section boundary — it is an incomplete row awaiting C-phase cells.

---

### Column Contract

> Process this contract before constructing any row. Column omission is a contract violation, not an oversight.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both components required**: (1) *Threshold expression* — the quantified condition that activates this scenario (e.g., "inventory count drops below safety-stock threshold of 50 units", "payment API p99 latency exceeds 500ms"). (2) *Detection signal* — the observable mechanism by which the system identifies the threshold has been crossed (e.g., "inventory-service health probe returns `degraded`", "payment-timeout counter exceeds circuit-breaker limit of 5 in 30s"). A trigger description that is qualitative only ("when the service is unavailable") without a threshold expression and named detection signal fails this fill requirement. |
| System State | D | What the system state is when the failure scenario is active: service states, data states, replication lag, consistency model in effect. Name specific services and their operational modes. |
| Data at Risk | D | What data may be lost, stale, or inconsistent. Name the specific consistency violation type (stale read, lost write, write-write conflict, phantom read). Quantify scope where possible. |
| Recovery Path | D | Four lifecycle stages, each with **three components**: (1) *Mechanism* — the action taken to advance the stage; (2) *SLA target* — named time commitment: Detect/TTD, Contain/TTC, Recover/TTR, Validate/TTV; (3) *Verification Signal (VS)* — a named observable artifact confirming the stage is complete (e.g., "inventory-service heartbeat returns HTTP 200", "payment-ACK written to audit log", "conflict-counter resets to 0 for 60s"). A stage without a named VS is not operationally verifiable. |
| Scenario Name | C | The specific commerce operation and failure mode. Example: "Checkout Interrupted — Client Offline Mid-Payment". |
| Class Label | — | Exactly one of: **Class 1** (full connectivity loss — client offline) / **Class 2** (partial failure — dependent service unavailable) / **Class 3** (split-brain — concurrent writes across a partition). Do not merge classes. |
| Severity + Blast Radius | C | Severity level (Degraded / Impaired / Down) and blast radius — which user segment and approximate scale is affected. |
| User Capability | C | What the user *can still do* during the failure. Not what they cannot do. Name at least one capability that survives the failure mode. |
| Status Quo Risk | C | Chronic accumulation if this gap is never addressed. **Three components required**: (1) *Rate* — the accumulation trigger/interval (e.g., "per-offline-incident", "per-deploy", "per-transaction"); (2) *Horizon* — the trajectory without intervention (e.g., "indefinitely", "without ceiling", "unbounded"); (3) *Named business metric* — the specific counter that accumulates (e.g., oversell count, reconciliation backlog items, duplicate charge events). |

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Section Order Requirement

Produce all 3 scenario rows in the unified table before writing the Gap Register. Do not write the Gap Register until all rows are complete. Do not write Recommendations until the Gap Register is complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and Recovery Path before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

Fill guidance — D-phase: Trigger Condition = client keepalive to order-service fails for 3 consecutive 10s probes / detected via client-side heartbeat returning no response. System State = order-service unreachable from client; local cart state cached in app memory; payment-token pending authorization; no write path to server available. Data at Risk = uncommitted cart modifications (stale write risk); pending payment-authorization token (expiry risk); any pre-disconnect server reservation (orphan risk until recovery sync). Recovery Path: Detect/TTD — client heartbeat detects offline within 30s, VS: "offline" indicator renders in UI; Contain/TTC — pending writes queued locally with idempotency key within TTD+5s, VS: local write-queue depth > 0 logged to client telemetry; Recover/TTR — on reconnect, queue flushes through idempotency-protected endpoint within 60s, VS: order-service returns 200 with idempotency-key echo; Validate/TTV — order state confirmed server-side within TTR+30s, VS: order-id returned in sync response matches local draft. Fill guidance — C-phase: Scenario Name = "Checkout Interrupted — Client Offline Mid-Payment". Severity = Impaired; Blast Radius = all users losing connectivity mid-checkout (~2% of sessions). User Capability = browse cached product catalog; view saved payment methods; queue draft orders for retry. Status Quo Risk = cart-abandonment count accumulates per-offline-incident, unbounded without queue-and-retry UX, metric: cart-abandonment events. Acute consequence branches: no idempotency key → double-charge on reconnect; no local queue → cart state lost on disconnect; naive retry without TTD gate → inventory oversell during reconnect burst.

**Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stages each with mechanism + SLA target + named VS, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and Recovery Path before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

Fill guidance — D-phase: Trigger Condition = inventory-service error rate exceeds 5% of requests over 60s rolling window / detected via inventory-service health probe returning 503 for 3 consecutive probes on 10s interval. System State = order-service operational; inventory-service circuit breaker OPEN; last-known inventory snapshot stale by up to TTD seconds; payment-service operational. Data at Risk = inventory reservation accuracy — reads against stale snapshot may commit against unavailable counts; orders placed during outage may oversell without real-time inventory gate. Recovery Path: Detect/TTD — circuit breaker opens at error threshold within 60s, VS: circuit-breaker-state metric transitions to OPEN in observability dashboard; Contain/TTC — orders accepted only against stale snapshot with configured oversell buffer applied, VS: inventory-accept-mode flag transitions to CONSERVATIVE in feature flag store; Recover/TTR — inventory-service recovers, circuit breaker half-opens, reconciliation job runs, VS: inventory-service health probe returns 200 and reconciliation-job-status = COMPLETE; Validate/TTV — inventory counts verified against order commitments made during outage, VS: reconciliation-discrepancy counter = 0 for 5 consecutive minutes. Fill guidance — C-phase: Scenario Name = "Order Placement During Inventory Service Outage". Severity = Degraded; Blast Radius = all users placing orders during outage window; oversell risk affects all low-stock SKUs. User Capability = browse and search catalog (cached); add to cart; place orders (against snapshot with oversell buffer). Status Quo Risk = oversell events accumulate per-outage-incident, unbounded without reconciliation automation, metric: oversell-event count per SKU. Acute consequence branches: no circuit breaker → cascading failure into order-service; no snapshot fallback → all order placement blocked; commit without oversell buffer → customer-visible oversell on recovery.

**Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stages each with mechanism + SLA target + named VS, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and Recovery Path before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

Fill guidance — D-phase: Trigger Condition = write-replica replication lag on inventory store exceeds 5s / detected via replica-lag metric exceeding threshold in monitoring, triggering split-brain detection alert. System State = two nodes each accepting writes to the same inventory record; vector clocks diverged; last-write-wins policy active without application-level conflict detection; eventual consistency promised but partition not yet healed. Data at Risk = inventory count integrity — concurrent reservation commits from partitioned nodes may each decrement the same stock without awareness of the concurrent write; post-merge inventory count non-deterministic without conflict-resolution rule. Recovery Path: Detect/TTD — replication-lag alert fires within 30s of threshold crossing, VS: conflict-detection-alert appears in alerting system with partition-id and affected-record set; Contain/TTC — writes to conflicting records fenced to primary node only, VS: write-fence flag transitions to PRIMARY-ONLY in distributed config store within 60s; Recover/TTR — conflict resolution job merges diverged records using lower-count-wins rule, VS: conflict-resolution-job status = COMPLETE with 0 unresolved records; Validate/TTV — post-merge counts cross-checked against order commitments placed during partition, VS: inventory-order-consistency-check returns 0 discrepancies. Fill guidance — C-phase: Scenario Name = "Concurrent Inventory Reservation — Partition Write Conflict". Severity = Impaired; Blast Radius = <1% of users (high-contention SKUs during flash sale); data integrity risk high even at low blast radius. User Capability = reserve inventory on primary node; view cart totals; proceed to checkout — apparent success, conflict pending resolution. Status Quo Risk = duplicate-fulfillment events accumulate per-flash-sale-incident, indefinitely without conflict-resolution logic, metric: duplicate-fulfillment count per SKU per event. Acute consequence branches: last-write-wins without app-level detection → both orders fulfilled → oversell; naive merge takes higher count → phantom inventory; rollback without notification → silent order cancellation.

**Do not advance to the Gap Register until this row contains non-placeholder content in every column, including all four Recovery Path stages each with mechanism + SLA target + named VS, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

### Output Table

Produce a **single unified table**. All three rows appear in this one table.

**Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows, produce a Gap Register with exactly three labeled, actionable findings:

1. **Offline Experience Gap** — a specific capability that breaks under Class 1 and is not addressed by the current recovery path.
2. **Data Consistency Violation** — a specific violation under Class 2 or Class 3 that the system currently cannot detect or correct.
3. **Missing Recovery Flow** — a specific recovery mechanism absent from the current implementation and required to complete the lifecycle.

Each finding must be specific and actionable. Generic statements ("offline support may be limited", "consistency issues may arise") fail — name the specific gap, violation, and missing mechanism.

---
---

## V-02 — Axis B: Lifecycle Stage Sub-Specifications

**Variation axis**: Lifecycle emphasis — Recovery Path stages are elevated from inline fill-requirement clauses to named sub-specifications within the Column Contract. Each stage (Detect, Contain, Recover, Validate) has its own structural entry with an explicit stage header, making stage-level omission visible as a named-section gap rather than a fill shortfall.

**Hypothesis**: When lifecycle stages appear only as an inline list inside a fill requirement cell, a model under token pressure may abbreviate later stages (Recover/Validate). Promoting each stage to a named sub-specification creates stage-level anchors that prevent silent omission of Validate/TTV or its Verification Signal — the stage can be checked by title rather than inferred from content density.

---

You are running **flow-resilience** for topic: {Topic}.

### Role Definitions

Two specialist roles contribute all columns in this analysis:

- **C — Commerce Expert**: owns the business-impact layer. Columns: Scenario Name, Class Label, Severity + Blast Radius, User Capability, Status Quo Risk.
- **D — Distributed Systems Expert**: owns the technical failure topology. Columns: Trigger Condition, System State, Data at Risk, Recovery Path.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table before Gap Register | Phase gate: all rows complete before Gap Register begins | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — C-phase columns before D-phase columns | Intra-row C-phase-first sequencing gate: complete all C-owned columns before beginning any D-owned columns | Column Contract (below) |
| Column | Per column | Named owner + stage-level sub-specification for Recovery Path | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.** Each Recovery Path stage sub-specification is a fill requirement — it is not a section header triggering a new output section.

---

### Column Contract

> Process this contract before constructing any row. Column omission is a contract violation.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Scenario Name | C | The specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** (full connectivity loss) / **Class 2** (partial failure) / **Class 3** (split-brain). Do not merge classes. |
| Severity + Blast Radius | C | Severity level (Degraded / Impaired / Down) + affected user segment and scale. |
| User Capability | C | What the user *can still do* during the failure. At least one surviving capability. |
| Status Quo Risk | C | Chronic accumulation if this gap is never addressed: *rate* (accumulation trigger) + *horizon* (trajectory without intervention) + *named business metric*. All three components required. |
| Trigger Condition | D | **Both components required**: (1) *Threshold expression* — quantified condition activating the scenario. (2) *Detection signal* — observable mechanism by which the system identifies the threshold has been crossed. Qualitative-only descriptions fail. |
| System State | D | Service states, data states, replication lag, consistency model in effect at failure onset. Name specific services. |
| Data at Risk | D | Data that may be lost, stale, or inconsistent. Name the specific consistency violation type and quantify scope. |
| Recovery Path | D | Four lifecycle stage sub-specifications (see expanded specification below). Every stage requires all three components. |

**Recovery Path — Stage Sub-Specifications**

Each row's Recovery Path cell must satisfy all four stage sub-specifications. A cell that omits a stage name, SLA target, or Verification Signal fails the fill requirement for that stage.

> **Stage 1 — Detect / TTD (Time to Detect)**
> *Mechanism*: the action or signal that surfaces the failure condition.
> *SLA target*: TTD — the named time-to-detect commitment.
> *Verification Signal (VS)*: the named observable artifact confirming detection is complete (e.g., circuit-breaker-state metric transitions to OPEN, offline banner renders in UI, conflict-detection-alert appears in alerting system with partition-id).

> **Stage 2 — Contain / TTC (Time to Contain)**
> *Mechanism*: the action taken to bound the blast radius and prevent failure propagation.
> *SLA target*: TTC — the named time-to-contain commitment.
> *Verification Signal (VS)*: the named observable artifact confirming containment is active (e.g., inventory-accept-mode flag set to CONSERVATIVE in feature flag store, write-fence flag transitions to PRIMARY-ONLY in distributed config store, local write-queue depth > 0 logged).

> **Stage 3 — Recover / TTR (Time to Recover)**
> *Mechanism*: the action taken to restore service to normal operation.
> *SLA target*: TTR — the named time-to-recover commitment.
> *Verification Signal (VS)*: the named observable artifact confirming recovery is complete (e.g., inventory-service health probe returns 200 and reconciliation-job-status = COMPLETE, order-service returns 200 with idempotency-key echo, conflict-resolution-job status = COMPLETE with 0 unresolved records).

> **Stage 4 — Validate / TTV (Time to Validate)**
> *Mechanism*: the action taken to confirm system state is consistent post-recovery.
> *SLA target*: TTV — the named time-to-validate commitment.
> *Verification Signal (VS)*: the named observable artifact confirming post-recovery validation is complete (e.g., reconciliation-discrepancy counter = 0, order-id returned in sync response matches local draft, inventory-order-consistency-check returns 0 discrepancies).

**Column order in output table**: `#` | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk | Trigger Condition | System State | Data at Risk | Recovery Path

---

### Section Order Requirement

Produce all 3 scenario rows in the unified table before writing the Gap Register. Do not write the Gap Register until all rows are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path.

Fill guidance: Scenario = checkout interrupted when client loses network mid-payment. C-phase: name the scenario as a specific commerce operation; classify as Class 1; set severity Impaired, blast radius ~2% of sessions; identify at least one surviving capability (cache browse, saved payment view, draft-order queue); set Status Quo Risk with rate = per-offline-incident, horizon = unbounded without retry UX, metric = cart-abandonment events. D-phase: Trigger Condition threshold = client keepalive fails 3 consecutive 10s probes; detection signal = client-side heartbeat returns no response. System State = order-service unreachable; local cart cached; payment token pending. Data at Risk = uncommitted cart modifications (stale write risk), pending payment token (expiry risk). Recovery Path — complete all four stage sub-specifications: Detect/TTD with VS (UI offline banner); Contain/TTC with VS (local write-queue depth > 0 in telemetry); Recover/TTR with VS (order-service 200 with idempotency echo); Validate/TTV with VS (order-id in sync response matches draft). Acute consequence branches: no idempotency key → double-charge; no local queue → cart lost; naive retry → oversell.

**Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with named mechanism, SLA target, and Verification Signal, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path.

Fill guidance: Scenario = order placement during inventory service outage. C-phase: classify as Class 2; severity Degraded, blast radius all users placing orders during window; User Capability = browse catalog (cached), add to cart, place orders (against snapshot with oversell buffer); Status Quo Risk: rate = per-outage-incident, horizon = unbounded without reconciliation automation, metric = oversell-event count per SKU. D-phase: Trigger Condition threshold = inventory-service error rate > 5% over 60s; detection signal = health probe 503 × 3 on 10s interval. System State = order-service operational; inventory circuit breaker OPEN; snapshot stale by up to TTD. Data at Risk = inventory reservation accuracy, orders committed against stale snapshot. Recovery Path — all four stage sub-specifications: Detect/TTD with VS (circuit-breaker-state = OPEN in dashboard); Contain/TTC with VS (inventory-accept-mode = CONSERVATIVE in feature flag store); Recover/TTR with VS (health probe 200 + reconciliation-job-status = COMPLETE); Validate/TTV with VS (reconciliation-discrepancy counter = 0 for 5 min). Acute consequence branches: no circuit breaker → cascade; no snapshot → order placement blocked; no oversell buffer → customer-visible oversell.

**Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with named mechanism, SLA target, and Verification Signal, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path.

Fill guidance: Scenario = concurrent inventory reservation during flash-sale partition. C-phase: classify as Class 3; severity Impaired, blast radius <1% of users but high data-integrity risk; User Capability = reserve on primary, view cart totals, proceed to checkout; Status Quo Risk: rate = per-flash-sale-incident, horizon = indefinitely without conflict-resolution logic, metric = duplicate-fulfillment count per SKU per event. D-phase: Trigger Condition threshold = write-replica replication lag > 5s; detection signal = replica-lag metric exceeds threshold, split-brain alert fires. System State = two nodes accepting writes to same record; vector clocks diverged; LWW active without app-level detection. Data at Risk = inventory count integrity — concurrent decrements without mutual awareness, non-deterministic post-merge count. Recovery Path — all four stage sub-specifications: Detect/TTD with VS (conflict-detection-alert with partition-id in alerting system); Contain/TTC with VS (write-fence flag = PRIMARY-ONLY in distributed config store); Recover/TTR with VS (conflict-resolution-job status = COMPLETE, 0 unresolved records); Validate/TTV with VS (inventory-order-consistency-check = 0 discrepancies). Acute consequence branches: LWW without detection → both orders fulfilled → oversell; naive higher-count merge → phantom inventory; rollback without notification → silent cancellation.

**Do not advance to the Gap Register until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with named mechanism, SLA target, and Verification Signal, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

### Output Table

Produce a **single unified table**. All three rows appear in this one table. **Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.**

Column order: `#` | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk | Trigger Condition | System State | Data at Risk | Recovery Path

---

### Gap Register

After completing all three rows, produce a Gap Register with exactly three labeled, actionable findings:

1. **Offline Experience Gap** — specific capability breaking under Class 1, not addressed by the current recovery path.
2. **Data Consistency Violation** — specific violation under Class 2 or Class 3 that the system cannot currently detect or correct.
3. **Missing Recovery Flow** — specific mechanism absent from the current implementation and required to complete the lifecycle.

Generic statements fail. Name the specific gap, violation, and missing mechanism.

---
---

## V-03 — Axis C: Inertia-First Framing

**Variation axis**: Inertia framing — before the scenario table, the prompt requires an explicit "Inertia Assessment" section that names the status-quo competitor (do-nothing) with a threat score and carrying cost. The Status Quo Risk column in the scenario table links back to this assessment, connecting row-level chronic accumulation to the strategic inertia framing established upfront.

**Hypothesis**: When the chronic cost of inaction is named and quantified before scenario construction begins, the Status Quo Risk column is written against a pre-committed frame rather than retrofitted. This may produce higher-quality chronic consequence entries — the model cannot abbreviate the carrying cost without visibly contradicting the upfront inertia assessment.

---

You are running **flow-resilience** for topic: {Topic}.

### Role Definitions

Two specialist roles contribute all columns in this analysis:

- **C — Commerce Expert**: owns the business-impact layer. Columns: Scenario Name, Class Label, Severity + Blast Radius, User Capability, Status Quo Risk.
- **D — Distributed Systems Expert**: owns the technical failure topology. Columns: Trigger Condition, System State, Data at Risk, Recovery Path.

---

### Step 1: Inertia Assessment (complete before scenario table)

**Before building the scenario table, produce an Inertia Assessment.** This assessment names the status-quo competitor — the cost of doing nothing about resilience gaps — and establishes the chronic accumulation baseline that the Status Quo Risk column in the scenario table will quantify per failure class.

The Inertia Assessment has three parts:

**1a. The Primary Competitor — Status Quo**
Name the do-nothing path explicitly. Why do teams defer resilience investment? What does the current system do when each failure class occurs (Class 1 / Class 2 / Class 3)? Assess the threat of inertia as HIGH / MEDIUM / LOW and justify the rating.

**1b. The Carrying Cost**
For each failure class, name one chronic accumulation that persists if resilience gaps are never addressed. Structure each as: *[metric] accumulates at [rate], [horizon trajectory] without intervention*. This is the pre-commitment that the Status Quo Risk column will fill for each scenario row.

**1c. The Tipping Point Signal**
Name one observable signal per class that indicates the carrying cost has crossed a threshold requiring action (e.g., "oversell-event count exceeds 50 per month", "cart-abandonment rate rises more than 2% above baseline"). This transforms inertia from a qualitative risk into a detectable condition.

> Produce the Inertia Assessment now. Do not advance to the Five-Level Architecture section until all three parts (1a, 1b, 1c) are complete with non-placeholder content for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table before Gap Register | Phase gate: all rows complete before Gap Register begins | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — C-phase columns before D-phase columns | Intra-row C-phase-first sequencing gate: complete all C-owned columns before beginning any D-owned columns | Column Contract (below) |
| Column | Per column | Named owner in Column Contract | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.** The Inertia Assessment above is a pre-table section — it is not a structural boundary within the scenario table.

---

### Column Contract

> Process this contract before constructing any row. The Status Quo Risk column must be consistent with the carrying costs established in the Inertia Assessment (Step 1b).

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: **Class 1** / **Class 2** / **Class 3**. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment and scale. |
| User Capability | C | What the user *can still do*. At least one surviving capability. |
| Status Quo Risk | C | Chronic accumulation consistent with Inertia Assessment Step 1b. **Three components required**: *rate* (accumulation interval) + *horizon* (trajectory without intervention) + *named business metric*. Must reference the same metric named in Step 1b for this class. |
| Trigger Condition | D | **Both components required**: (1) *Threshold expression* — quantified condition that activates the scenario. (2) *Detection signal* — observable mechanism identifying the threshold crossing. Qualitative-only descriptions fail. |
| System State | D | Service states, data states, replication state, consistency model in effect. Name specific services. |
| Data at Risk | D | Specific consistency violation type + scope. |
| Recovery Path | D | Four lifecycle stages, each with three components: *Mechanism* + *SLA target* (TTD/TTC/TTR/TTV) + *Verification Signal* (named observable confirming stage completion). A stage without a named VS is operationally unverifiable. |

**Column order in output table**: `#` | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk | Trigger Condition | System State | Data at Risk | Recovery Path

---

### Section Order Requirement

Produce all 3 scenario rows before writing the Gap Register. Do not write the Gap Register until all rows are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path. The Status Quo Risk entry must use the metric established for Class 1 in Inertia Assessment Step 1b.

Fill guidance: Scenario = checkout interrupted when client goes offline mid-payment. Status Quo Risk must match the Class 1 carrying cost from Step 1b (e.g., cart-abandonment events accumulating per-incident, unbounded without queue-and-retry, metric: cart-abandonment count). Trigger Condition = client keepalive fails 3 × 10s probes / heartbeat returns no response. System State = order-service unreachable; cart cached locally; payment token pending. Data at Risk = uncommitted cart state, pending payment token. Recovery Path: Detect/TTD + VS (offline banner in UI); Contain/TTC + VS (write-queue depth > 0 in telemetry); Recover/TTR + VS (order-service 200 with idempotency echo); Validate/TTV + VS (order-id in sync response matches draft). Acute consequence branches: no idempotency key → double-charge; no local queue → cart lost; naive retry → oversell.

**Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stages with mechanism + SLA + named VS, and a Status Quo Risk entry using the Class 1 metric from the Inertia Assessment with rate, horizon, and named metric.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path. The Status Quo Risk entry must use the metric established for Class 2 in Inertia Assessment Step 1b.

Fill guidance: Scenario = order placement during inventory service outage. Status Quo Risk must match the Class 2 carrying cost from Step 1b (e.g., oversell events accumulating per-outage-incident, unbounded without reconciliation automation, metric: oversell-event count per SKU). Trigger Condition = inventory-service error rate > 5% over 60s / health probe 503 × 3 on 10s. System State = circuit breaker OPEN; snapshot stale. Data at Risk = inventory reservation accuracy, potential oversell. Recovery Path: Detect/TTD + VS (circuit-breaker = OPEN in dashboard); Contain/TTC + VS (inventory-accept-mode = CONSERVATIVE in feature flag store); Recover/TTR + VS (probe 200 + reconciliation = COMPLETE); Validate/TTV + VS (discrepancy counter = 0 for 5 min). Acute branches: no circuit breaker → cascade; no snapshot → blocked; no buffer → customer-visible oversell.

**Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stages with mechanism + SLA + named VS, and a Status Quo Risk entry using the Class 2 metric from the Inertia Assessment with rate, horizon, and named metric.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (C-phase first): Complete Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk before writing Trigger Condition, System State, Data at Risk, and Recovery Path. The Status Quo Risk entry must use the metric established for Class 3 in Inertia Assessment Step 1b.

Fill guidance: Scenario = concurrent inventory reservation during flash-sale partition. Status Quo Risk must match the Class 3 carrying cost from Step 1b (e.g., duplicate-fulfillment events accumulating per-flash-sale-incident, indefinitely without conflict resolution, metric: duplicate-fulfillment count per SKU per event). Trigger Condition = replica lag > 5s / replica-lag metric triggers split-brain alert. System State = two nodes accepting writes; vector clocks diverged; LWW active. Data at Risk = inventory count integrity, non-deterministic post-merge count. Recovery Path: Detect/TTD + VS (conflict-detection-alert with partition-id in alerting system); Contain/TTC + VS (write-fence = PRIMARY-ONLY in config store); Recover/TTR + VS (resolution-job = COMPLETE, 0 unresolved); Validate/TTV + VS (consistency-check = 0 discrepancies). Acute branches: LWW without detection → both orders fulfilled; naive higher-count merge → phantom inventory; rollback without notification → silent cancellation.

**Do not advance to the Gap Register until this row contains non-placeholder content in every column, including all four Recovery Path stages with mechanism + SLA + named VS, and a Status Quo Risk entry using the Class 3 metric from the Inertia Assessment with rate, horizon, and named metric.**

---

### Output Table

Produce a **single unified table**. All three rows appear in this one table. **Do not create separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.**

Column order: `#` | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk | Trigger Condition | System State | Data at Risk | Recovery Path

---

### Gap Register

After completing all three rows, produce a Gap Register with exactly three labeled, actionable findings:

1. **Offline Experience Gap** — specific capability breaking under Class 1, not addressed by the recovery path.
2. **Data Consistency Violation** — specific violation under Class 2 or Class 3 the system cannot detect or correct.
3. **Missing Recovery Flow** — specific mechanism absent from the current implementation.

Also produce one **Inertia Verdict**: given the carrying costs named in Step 1b and the gaps identified above, is inertia a HIGH / MEDIUM / LOW threat, and what is the single strongest argument against deferral? (2–3 sentences.)

Generic statements fail. Name the specific gap, violation, missing mechanism, and inertia argument.

---
---

## V-04 — Axes A + B: D-Phase-First + Lifecycle Stage Sub-Specifications

**Variation axes**: Role sequence (D-phase-first) combined with lifecycle emphasis (stage sub-specifications). The intra-row column-group gate runs D-phase before C-phase. Each Recovery Path stage is defined as a named sub-specification within the Column Contract.

**Hypothesis**: Combining D-phase-first ordering with stage-level sub-specifications creates the strongest technical completeness constraint: the Recovery Path (D-owned, filled first) must satisfy all four stage sub-specifications before the C-phase commerce framing can be written. The stage sub-specification anchors prevent late-stage omission while D-first sequencing prevents commerce framing from compressing Recovery Path detail.

---

You are running **flow-resilience** for topic: {Topic}.

### Role Definitions

- **D — Distributed Systems Expert**: owns the technical failure topology. Columns (filled first within each row): Trigger Condition, System State, Data at Risk, Recovery Path.
- **C — Commerce Expert**: owns the business-impact layer. Columns (filled second within each row): Scenario Name, Class Label, Severity + Blast Radius, User Capability, Status Quo Risk.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table before Gap Register | Phase gate: all rows complete before Gap Register | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase columns before C-phase columns | Intra-row D-phase-first sequencing gate: complete Trigger Condition, System State, Data at Risk, Recovery Path before beginning Scenario Name, Severity, User Capability, Status Quo Risk | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** Recovery Path stage sub-specifications are fill requirements — they are not section boundaries within the output table.

---

### Column Contract

> Process this contract in full before constructing any row.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying the threshold crossing. Qualitative-only descriptions fail. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. |
| Data at Risk | D | Specific consistency violation type + scope. |
| Recovery Path | D | All four stage sub-specifications (see below). Every stage requires all three components. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment. |
| User Capability | C | What the user can still do. At least one surviving capability. |
| Status Quo Risk | C | *Rate* + *horizon* + *named business metric*. All three required. |

**Recovery Path — Stage Sub-Specifications**

> **Stage 1 — Detect / TTD**
> *Mechanism*: the signal or action that surfaces the failure.
> *SLA target*: TTD — time-to-detect commitment.
> *VS*: named observable confirming detection (e.g., "circuit-breaker = OPEN in dashboard", "offline banner renders in UI", "conflict-alert fires with partition-id").

> **Stage 2 — Contain / TTC**
> *Mechanism*: action bounding blast radius and preventing propagation.
> *SLA target*: TTC — time-to-contain commitment.
> *VS*: named observable confirming containment (e.g., "inventory-accept-mode = CONSERVATIVE in feature flag store", "write-fence = PRIMARY-ONLY in config store", "write-queue depth > 0 in telemetry").

> **Stage 3 — Recover / TTR**
> *Mechanism*: action restoring normal service operation.
> *SLA target*: TTR — time-to-recover commitment.
> *VS*: named observable confirming recovery (e.g., "health probe returns 200 + reconciliation = COMPLETE", "order-service 200 with idempotency echo", "resolution-job = COMPLETE with 0 unresolved records").

> **Stage 4 — Validate / TTV**
> *Mechanism*: action confirming post-recovery system consistency.
> *SLA target*: TTV — time-to-validate commitment.
> *VS*: named observable confirming validation (e.g., "reconciliation-discrepancy counter = 0 for 5 min", "order-id in sync response matches draft", "consistency-check = 0 discrepancies").

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Section Order Requirement

Produce all 3 scenario rows before writing the Gap Register. Do not write the Gap Register until all rows are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and Recovery Path (all four stage sub-specifications with mechanism + SLA + VS) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s / heartbeat returns no response. System State = order-service unreachable; cart cached locally; payment token pending. Data at Risk = uncommitted cart state (stale write risk), pending payment token (expiry risk). Recovery Path: Stage 1 Detect/TTD = heartbeat detects offline within 30s / VS: offline banner in UI; Stage 2 Contain/TTC = writes queued with idempotency key / VS: write-queue > 0 in client telemetry; Stage 3 Recover/TTR = queue flushes on reconnect via idempotency-protected endpoint / VS: order-service 200 with idempotency echo; Stage 4 Validate/TTV = server-side order state confirmed / VS: order-id in sync response matches draft. C-phase fill: Scenario = checkout interrupted mid-payment; Class 1; Impaired, ~2% sessions; User Capability = cache browse, draft-order queue; Status Quo Risk = cart-abandonment events per-offline-incident, unbounded, metric: cart-abandonment count. Acute branches: no idempotency → double-charge; no queue → cart lost; naive retry → oversell.

**Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and Recovery Path (all four stage sub-specifications) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory error rate > 5% / 60s / probe 503 × 3 on 10s. System State = circuit breaker OPEN; snapshot stale by TTD. Data at Risk = inventory reservation accuracy, potential oversell against stale count. Recovery Path: Stage 1 Detect/TTD = circuit breaker trips at threshold / VS: breaker-state = OPEN in dashboard; Stage 2 Contain/TTC = orders accepted against snapshot with oversell buffer / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Stage 3 Recover/TTR = service recovers, breaker half-opens, reconciliation runs / VS: probe 200 + reconciliation-job = COMPLETE; Stage 4 Validate/TTV = counts verified against commitments / VS: discrepancy counter = 0 for 5 min. C-phase fill: Scenario = order placement during inventory outage; Class 2; Degraded, all orders in window; User Capability = browse (cached), add to cart, place orders (with oversell buffer); Status Quo Risk = oversell events per-outage-incident, unbounded, metric: oversell-event count per SKU. Acute branches: no circuit breaker → cascade; no snapshot → blocked; no buffer → customer-visible oversell.

**Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and Recovery Path (all four stage sub-specifications) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = replica lag > 5s / replica-lag metric triggers split-brain alert. System State = two nodes accepting writes; vector clocks diverged; LWW active without app-level detection. Data at Risk = inventory count integrity, non-deterministic post-merge count. Recovery Path: Stage 1 Detect/TTD = replication-lag alert fires / VS: conflict-alert with partition-id in alerting system; Stage 2 Contain/TTC = writes fenced to primary only / VS: write-fence = PRIMARY-ONLY in config store; Stage 3 Recover/TTR = conflict-resolution job merges with lower-count-wins rule / VS: resolution-job = COMPLETE with 0 unresolved; Stage 4 Validate/TTV = post-merge counts cross-checked against order commitments / VS: consistency-check = 0 discrepancies. C-phase fill: Scenario = concurrent reservation during flash-sale partition; Class 3; Impaired, <1% users, high data integrity risk; User Capability = reserve on primary, view cart, proceed to checkout; Status Quo Risk = duplicate-fulfillment events per-flash-sale-incident, indefinitely, metric: duplicate-fulfillment count per SKU. Acute branches: LWW → both orders fulfilled; naive higher-count merge → phantom inventory; rollback without notification → silent cancellation.

**Do not advance to Gap Register until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry with rate, horizon, and named metric.**

---

### Output Table

Produce a **single unified table**. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows, produce a Gap Register with exactly three labeled, actionable findings:

1. **Offline Experience Gap** — specific capability breaking under Class 1.
2. **Data Consistency Violation** — specific violation under Class 2 or 3.
3. **Missing Recovery Flow** — specific absent mechanism required to complete the lifecycle.

Generic statements fail. Name the specific gap, violation, and missing mechanism.

---
---

## V-05 — Axes A + B + C: D-Phase-First + Lifecycle Stage Sub-Specifications + Inertia-First Framing

**Variation axes**: All three axes combined. D-phase columns filled first (role sequence). Recovery Path stages are named sub-specifications (lifecycle emphasis). Inertia Assessment leads the prompt, with Status Quo Risk linking back to per-class carrying costs (inertia framing).

**Hypothesis**: The three axes address orthogonal completeness risks: D-first prevents commerce framing from compressing technical detail; stage sub-specifications prevent silent late-stage omission; inertia-first framing prevents chronic-consequence abbreviation by pre-committing to carrying costs before scenario construction begins. Running all three simultaneously tests whether they compose without mutual interference — each should improve a distinct column or stage, not compete for the same structural slot.

---

You are running **flow-resilience** for topic: {Topic}.

### Role Definitions

- **D — Distributed Systems Expert**: owns the technical failure topology. Columns (filled first within each row): Trigger Condition, System State, Data at Risk, Recovery Path.
- **C — Commerce Expert**: owns the business-impact layer. Columns (filled second within each row): Scenario Name, Class Label, Severity + Blast Radius, User Capability, Status Quo Risk.

---

### Step 1: Inertia Assessment (complete before scenario table)

Before building the scenario table, produce an Inertia Assessment naming the status-quo competitor — the cost of doing nothing about resilience gaps for this topic.

**1a. The Primary Competitor — Status Quo**: Name the do-nothing path. Why do teams defer resilience investment for this topic? Assess the inertia threat as HIGH / MEDIUM / LOW with a one-sentence justification. What does the current system actually do under each failure class (Class 1 / Class 2 / Class 3) without intervention?

**1b. Carrying Costs by Class**: For each failure class, name the chronic accumulation that persists without remediation. Format: *[named metric] accumulates at [rate], [horizon trajectory] without intervention*. These three entries are the Status Quo Risk pre-commitments that each scenario row must fill consistently.

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**1c. Tipping Point Signals**: For each class, name one observable signal that indicates the carrying cost has crossed a threshold requiring action (e.g., "oversell-event count exceeds 50/month", "cart-abandonment rate rises > 2% above baseline"). These signals define when inertia becomes indefensible.

> Produce the Inertia Assessment now. Do not advance to the architecture section until all three parts (1a, 1b, 1c) are complete with non-placeholder content for all three failure classes.

---

### Five-Level Anti-Omission Architecture

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows unified | Row-index `#` column + anti-split instruction | Output table (this document) |
| Section | Table before Gap Register | Phase gate: all rows complete before Gap Register | Section Order Requirement (below) |
| Slot | Within a row | In-row bold imperative co-located at cell granularity | Row Descriptors (below) |
| Column-Group | Within a row — D-phase before C-phase | Intra-row D-phase-first sequencing gate: complete Trigger Condition, System State, Data at Risk, Recovery Path (all stage sub-specifications) before beginning Scenario Name, Severity, User Capability, Status Quo Risk | Column Contract (below) |
| Column | Per column | Named owner + Recovery Path stage sub-specifications | Column Contract (below) |

**Anti-boundary instruction**: All three scenario rows must appear in a single unified table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns.** **Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts from D-phase to C-phase.** The Inertia Assessment above is a pre-table section, not a structural boundary within the scenario table. Recovery Path stage sub-specifications are fill requirements, not section boundaries within the output table.

---

### Column Contract

> Process this contract in full before constructing any row. Status Quo Risk entries must be consistent with Inertia Assessment Step 1b.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | Sequential integer: 1, 2, 3. |
| Trigger Condition | D | **Both required**: (1) *Threshold expression* — quantified activation condition. (2) *Detection signal* — observable mechanism identifying threshold crossing. Qualitative-only fails. |
| System State | D | Service states, data states, replication state, consistency model. Name specific services. |
| Data at Risk | D | Specific consistency violation type + scope. |
| Recovery Path | D | All four stage sub-specifications (see below). Every stage requires mechanism + SLA target + named VS. |
| Scenario Name | C | Specific commerce operation and failure mode. |
| Class Label | — | Exactly one of: Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded / Impaired / Down) + affected user segment. |
| User Capability | C | What the user can still do. At least one surviving capability. |
| Status Quo Risk | C | Must use the metric and framing from Inertia Assessment Step 1b for this class. *Rate* + *horizon* + *named business metric*. All three required. |

**Recovery Path — Stage Sub-Specifications**

> **Stage 1 — Detect / TTD**
> *Mechanism*: signal or action surfacing the failure.
> *SLA target*: TTD.
> *VS*: named observable confirming detection complete (e.g., circuit-breaker = OPEN in dashboard, offline banner in UI, conflict-alert with partition-id in alerting system).

> **Stage 2 — Contain / TTC**
> *Mechanism*: action bounding blast radius.
> *SLA target*: TTC.
> *VS*: named observable confirming containment active (e.g., inventory-accept-mode = CONSERVATIVE in feature flag store, write-fence = PRIMARY-ONLY in config store, write-queue depth > 0 in client telemetry).

> **Stage 3 — Recover / TTR**
> *Mechanism*: action restoring service.
> *SLA target*: TTR.
> *VS*: named observable confirming recovery complete (e.g., probe 200 + reconciliation-job = COMPLETE, order-service 200 with idempotency echo, resolution-job = COMPLETE with 0 unresolved).

> **Stage 4 — Validate / TTV**
> *Mechanism*: action confirming post-recovery consistency.
> *SLA target*: TTV.
> *VS*: named observable confirming validation complete (e.g., discrepancy-counter = 0 for 5 min, order-id in sync response matches draft, consistency-check = 0 discrepancies).

**Column order in output table**: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Section Order Requirement

Produce all 3 scenario rows before writing the Gap Register. Do not write the Gap Register until all rows are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss / Client Offline)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (each with mechanism + SLA + named VS) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = client keepalive fails 3 × 10s probes / heartbeat returns no response. System State = order-service unreachable; local cart cached; payment token pending. Data at Risk = uncommitted cart state (stale write risk), pending payment token (expiry risk). Recovery Path: Stage 1 = heartbeat detects offline within 30s / TTD / VS: offline banner in UI; Stage 2 = writes queued with idempotency key / TTC / VS: write-queue > 0 in client telemetry; Stage 3 = queue flushes on reconnect through idempotency-protected endpoint / TTR / VS: order-service 200 with idempotency echo; Stage 4 = server-side order state confirmed / TTV / VS: order-id in sync response matches local draft. C-phase fill: Scenario = checkout interrupted mid-payment; Class 1; Severity Impaired, ~2% sessions; User Capability = cache browse, draft-order queue for retry; Status Quo Risk = must use Class 1 carrying cost from Step 1b (rate + horizon + metric as established). Acute branches: no idempotency key → double-charge; no local queue → cart lost; naive retry without TTD gate → inventory oversell.

**Do not advance to row 2 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 1 carrying cost from Step 1b with rate, horizon, and named metric.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (each with mechanism + SLA + named VS) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = inventory error rate > 5% over 60s / probe 503 × 3 on 10s. System State = circuit breaker OPEN; snapshot stale by TTD. Data at Risk = inventory reservation accuracy, orders committed against stale snapshot. Recovery Path: Stage 1 = circuit breaker trips at threshold / TTD / VS: breaker-state = OPEN in observability dashboard; Stage 2 = orders accepted against snapshot with oversell buffer / TTC / VS: inventory-accept-mode = CONSERVATIVE in feature flag store; Stage 3 = service recovers, breaker half-opens, reconciliation runs / TTR / VS: probe 200 + reconciliation-job-status = COMPLETE; Stage 4 = counts verified against commitments / TTV / VS: reconciliation-discrepancy-counter = 0 for 5 consecutive min. C-phase fill: Scenario = order placement during inventory outage; Class 2; Degraded, all orders in window; User Capability = browse cached, add to cart, place with oversell buffer; Status Quo Risk = must use Class 2 carrying cost from Step 1b (rate + horizon + metric). Acute branches: no circuit breaker → cascade; no snapshot → blocked; no buffer → customer-visible oversell.

**Do not advance to row 3 until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 2 carrying cost from Step 1b with rate, horizon, and named metric.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

Column-group gate (D-phase first): Complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stage sub-specifications (each with mechanism + SLA + named VS) before writing Scenario Name, Class Label, Severity + Blast Radius, User Capability, and Status Quo Risk.

D-phase fill: Trigger = write-replica lag > 5s / replica-lag metric fires split-brain alert. System State = two nodes accepting writes to same record; vector clocks diverged; LWW active without app-level detection. Data at Risk = inventory count integrity, non-deterministic post-merge count. Recovery Path: Stage 1 = lag alert fires / TTD / VS: conflict-detection-alert with partition-id in alerting system; Stage 2 = writes fenced to primary only / TTC / VS: write-fence-flag = PRIMARY-ONLY in distributed config store; Stage 3 = resolution job merges with lower-count-wins rule / TTR / VS: resolution-job = COMPLETE with 0 unresolved records; Stage 4 = post-merge counts cross-checked against commitments / TTV / VS: inventory-order-consistency-check = 0 discrepancies. C-phase fill: Scenario = concurrent reservation during flash-sale partition; Class 3; Impaired, <1% users but high integrity risk; User Capability = reserve on primary, view cart, proceed to checkout; Status Quo Risk = must use Class 3 carrying cost from Step 1b (rate + horizon + metric). Acute branches: LWW without detection → both orders fulfilled; naive higher-count merge → phantom inventory; rollback without notification → silent cancellation.

**Do not advance to Gap Register until this row contains non-placeholder content in every column, including all four Recovery Path stage sub-specifications each with mechanism, SLA target, and named VS, and a Status Quo Risk entry consistent with the Class 3 carrying cost from Step 1b with rate, horizon, and named metric.**

---

### Output Table

Produce a **single unified table**. All three rows appear in this one table. **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts.**

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

After completing all three rows, produce a Gap Register with exactly three labeled, actionable findings:

1. **Offline Experience Gap** — specific capability breaking under Class 1.
2. **Data Consistency Violation** — specific violation under Class 2 or Class 3.
3. **Missing Recovery Flow** — specific mechanism absent from the current implementation.

Produce one **Inertia Verdict**: given the carrying costs named in Step 1b and the gaps identified above, is inertia a HIGH / MEDIUM / LOW threat, and what is the single strongest argument against deferral? (2–3 sentences.)

Generic statements fail. Name the specific gap, violation, missing mechanism, and inertia argument.

---
---

## Candidate Pattern Analysis — R11 Axes

### Candidate C-35: Pre-Table Inertia Assessment with Per-Class Carrying Cost Pre-Commitment

**Source**: V-03/V-05 Axis C — an explicit "Inertia Assessment" section appears before the scenario table, naming the status-quo competitor with a threat score and per-class carrying costs. The Status Quo Risk column in the scenario table is required to be *consistent with* the pre-committed carrying costs from the assessment (not independently authored per row). This creates a two-anchor chronic-consequence specification: the assessment names the cost at the strategic level; the row names it at the scenario level; a reader can verify that the row cost is consistent with the pre-commitment.

**Distinguishing property**: C-29 (Chronic Consequence Enumeration) requires a carrying cost in at least one row; C-31 (Three-Component Framing) requires rate + horizon + metric. C-35 would require that at least one row's chronic consequence is *pre-committed* at the inertia-assessment level before the row is written — making the row a constrained fill, not an independent assertion. A prompt that writes chronic consequences only in row descriptors without a prior strategic-level pre-commitment does not satisfy this candidate.

**Pass condition (candidate)**: An Inertia Assessment section (or equivalently named pre-table strategic assessment) appears before the output table, naming per-class carrying costs as pre-commitments. At least one scenario row's Status Quo Risk fill requirement explicitly references the pre-committed carrying cost by class. C-31 must also pass.

---

### Candidate C-36: Per-Class Inertia Tipping Point Signal

**Source**: V-03/V-05 Axis C — for each failure class, the Inertia Assessment names a tipping-point signal: a named observable condition at which the carrying cost becomes operationally indefensible (e.g., "oversell-event count exceeds 50/month"). This transforms the inertia assessment from a qualitative risk statement into a detectable condition — a reader can monitor the named signal and know when deferral is no longer defensible.

**Distinguishing property**: C-35 (candidate) requires carrying-cost pre-commitment; C-36 would additionally require a tipping-point signal that is observable (a named metric threshold, not a qualitative statement). The tipping-point signal binds the inertia assessment to the same operationalization standard as the Trigger Condition column (C-33): both require a threshold expression and a detection mechanism — but C-36 applies this standard to the inertia competitor rather than to failure-class activation.

**Pass condition (candidate)**: The Inertia Assessment (or equivalent pre-table section) names one tipping-point signal per failure class, each consisting of a threshold expression (quantified condition at which inertia becomes indefensible) and a named metric being monitored. A qualitative statement ("when oversells become frequent") without a quantified threshold fails. C-35 must also pass.

---

### Candidate C-37: Inertia Verdict Post-Gap Register

**Source**: V-03/V-05 Axis C — after the Gap Register, the prompt requires an "Inertia Verdict": given the identified gaps and carrying costs, a final threat assessment (HIGH / MEDIUM / LOW) with the single strongest argument against deferral. This creates a closed-loop inertia specification: pre-table assessment names the cost; row-level Status Quo Risk quantifies it per scenario; post-Gap-Register verdict synthesizes the gaps into a strategic recommendation.

**Distinguishing property**: The verdict is distinct from the Gap Register (which names technical gaps) and from the Inertia Assessment (which names costs before evidence). The verdict requires both the gap evidence and the carrying-cost pre-commitment to be complete before it can be written — it is structurally dependent on both. This makes it a second section-level phase gate: Gap Register must be complete before the Inertia Verdict can be written.

**Pass condition (candidate)**: A section appearing after the Gap Register (or equivalently positioned) synthesizes the gap findings and carrying costs into a named threat level (HIGH / MEDIUM / LOW) with at least one sentence of argument. The section must be structurally dependent on the Gap Register being complete. C-35 must also pass.

---

### R11 Axis Orthogonality Assessment

| Axis | Column(s) affected | Stage(s) affected | Candidate criterion |
|------|--------------------|------------------|---------------------|
| A — D-phase-first | All D-owned columns (order within row) | All Recovery Path stages | None identified — axis is structural, not content-generating |
| B — Lifecycle stage sub-specs | Recovery Path (all 4 stages) | Each stage individually | None identified — strengthens existing C-34 but does not exceed it |
| C — Inertia-first framing | Status Quo Risk (pre-commitment) | Pre-table and post-Gap-Register | C-35, C-36, C-37 (three candidate criteria, one per inertia framing sub-element) |

**Observation**: Axis A (role sequence) and Axis B (lifecycle emphasis) improve existing criteria (C-32 and C-34 respectively) without generating patterns that exceed the current rubric surface. Axis C (inertia framing) introduces three genuinely new structural patterns: pre-commitment, tipping-point signal, and post-gap verdict. All three are absent from the current rubric surface (C-17 through C-34) and from the persistent uncracked block (C-09 through C-16). Axis C is the R11 ceiling-raising candidate.

**Projected ceiling under a hypothetical v11 rubric (denominator 29, adding C-35 + C-36 + C-37)**:
- V-03 / V-05 (Axis C present): 18 + 3 = 21/29 → 21/29 × 10 = 7.24 → composite = 60 + 30 + 7.24 = **97.24**
- V-01 / V-02 / V-04 (Axis C absent): 18/29 → 6.21 → composite = **96.21**
- V-05 > V-04 by all three Axis C criteria; V-03 = V-05 (both carry Axis C only).
