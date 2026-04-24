# flow-resilience — Round 14 Variations (Rubric v13)

**Rubric**: v13 · 32 aspirational criteria (C-09 – C-40) · Ceiling entering R14: 32/32 → 100.00 (R13 V-01/V-02/V-04/V-05)
**Open criteria entering R14**: None — four of five R13 variations crack all 32 criteria. V-03 failed C-39 (locational "Begin Row N here" vs performative "Write this row now").
**R14 objective**: With no new criteria open, all five variations hold the R14 ceiling (32/32) while exploring structural diversity. Axes probe SLA pre-commitment, Failure Signature column addition, and Inertia Assessment container format — finding distinct paths to the same 100.00 ceiling.

**Variation axes chosen:**
- **Axis A: Pre-committed SLA Budget** — the Inertia Assessment adds sub-section 1d naming TTD/TTC/TTR/TTV targets per class; the Column Contract's Recovery Path entry references this budget, paralleling the Status Quo Risk → Step 1b pre-commitment chain; closes the per-row SLA invention escape
- **Axis B: Failure Signature column** — a new D-owned column added to the Column Contract; fill requirement: the named production observable pattern distinguishing this failure class from the other two in live telemetry; forces class disambiguation below the Class Label column
- **Axis C: Three-Act Investment Memo** — the Inertia Assessment is re-containerized as a prose Investment Memo (Act I: Situation / Act II: Risk Accumulation / Act III: Decision Trigger) rather than numbered sub-sections; the pre-commitment constraint chain (C-35/C-36) is preserved through renamed references

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | Axis A: Pre-committed SLA Budget | Adding SLA targets to the pre-commitment chain forces specific TTD/TTC/TTR/TTV fills referenced to a named budget rather than invented per row — hypothesis: SLA precision increases and generic `TTD: minutes` style fills decline without weakening any existing criterion |
| V-02 | Axis B: Failure Signature column | Requiring an explicit Failure Signature per row forces class disambiguation at column granularity in live telemetry — hypothesis: distinguishing production patterns per class prevents scenario drift toward generic "service unavailable" fills and sharpens Class 2 / Class 3 boundary coverage |
| V-03 | Axis C: Three-Act Investment Memo | Re-containerizing the Inertia Assessment as a prose memo tests whether the C-35 pre-commitment constraint survives a register change — hypothesis: narrative memo framing produces richer carrying-cost content without weakening the structural reference chain; C-39 is preserved because the re-containerization affects the Inertia Assessment, not the row imperatives |
| V-04 | Axes A + B: SLA Budget + Failure Signature | Combined pre-commitment across both SLA targets and class identification signals — hypothesis: the two additions are orthogonal (SLA budget constrains Recovery Path; Failure Signature constrains System State / class boundary) and coexist without structural conflict |
| V-05 | Axes A + B + C compact | All three axes in minimum viable structure — the tightest prompt achieving 32/32 with the SLA Budget sub-section, Failure Signature column, and prose Investment Memo container |

---

---

## V-01 — Pre-committed SLA Budget (Axis A)

**Variation axis**: Inertia Assessment gains sub-section 1d (SLA Budget) pre-committing TTD/TTC/TTR/TTV targets per failure class. The Column Contract's Recovery Path entry requires SLA fills to reference the budget; per-row SLA invention without reference does not satisfy the constraint. At least one Row Descriptor names Step 1d as the SLA source.

**Hypothesis**: SLA targets pre-committed in the Inertia Assessment travel into the Recovery Path column with the same constraint force as carrying costs in Status Quo Risk. The pre-commitment closes the escape where a model writes "TTD: within minutes" without naming a specific target — reducing generic SLA fills and making the Recovery Path specification falsifiable against a named commitment.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment

Produce before the scenario table. Do not advance until all four parts are non-placeholder for all three classes.

**1a. Status Quo Threat**: Name the do-nothing path. HIGH / MEDIUM / LOW with one-sentence justification. What does the system do under Class 1 / Class 2 / Class 3 without intervention?

**1b. Carrying Costs** (pre-committed constraints for Status Quo Risk column — each fill must reference these):
- Class 1: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 2: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 3: *[named metric] accumulates at [rate], [horizon] without intervention*

**1c. Tipping Point Signals** (quantified threshold + named metric per class — the empirical exit condition for each inertia claim):
- Class 1:
- Class 2:
- Class 3:

**1d. SLA Budget** (pre-committed Recovery Path targets — all Recovery Path SLA fills must reference this budget; per-row SLA values not drawn from this table do not satisfy the SLA constraint):
- Class 1: TTD: [target] / TTC: [target] / TTR: [target] / TTV: [target]
- Class 2: TTD: [target] / TTC: [target] / TTR: [target] / TTV: [target]
- Class 3: TTD: [target] / TTC: [target] / TTR: [target] / TTV: [target]

---

### Pre-Output Specification

**Five-Level Anti-Omission Architecture**

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows | `#` row-index + anti-split instruction | Output table (below) |
| Section | Table + chaos blocks → Gap Register | Phase gate: all 3 rows + co-located chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | Within row | Bold in-row imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within row: D-phase → C-phase | D-first intra-row gate: D-owned columns complete before C-owned | Column Contract (below) |
| Column | Per column | Named owner + stage sub-specs with actor-chain notation | Column Contract (below) |

**Anti-boundary umbrella** (four escape forms closed simultaneously): **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns [escape 1: table split]. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts [escape 2: intra-table boundary]. Do not consolidate chaos blocks into a standalone chaos section or standalone chaos table [escape 3: chaos consolidation]. Do not produce a standalone observability section or observability table for Gap Register findings [escape 4: observability consolidation].**

**Chaos Test Block Specification**

| Component | Fill Requirement |
|-----------|-----------------|
| Inject | Named: service + injection method + duration. Reproducible in test harness. |
| Expected Behavior | Named observables during injection if handled correctly. Specific signals, not desired end-states. |
| Pass Signal | Named observable confirming correct handling per the row's recovery path. |
| Fail Signal | Named observable confirming failure to handle. |

**Column Contract** — process before any row; column omission is a contract violation.

> **Conflict vocabulary constraint**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale` — canonical label required; free-text descriptions do not satisfy.
> **Status Quo Risk constraint**: must use Step 1b metric for the row's class; rate + horizon + named metric all required.
> **SLA constraint**: Recovery Path SLA targets must reference Step 1d budget for the row's class. A stage SLA value not drawn from Step 1d does not satisfy the SLA constraint; per-row SLA invention is a contract violation.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | 1, 2, 3. |
| Trigger Condition | D | (1) Threshold expression — quantified activation condition. (2) Detection signal — observable mechanism identifying threshold crossing. Both required. |
| System State | D | Named services, data states, consistency model. Class 3: canonical conflict vocabulary required. |
| Data at Risk | D | Consistency violation type + scope. Class 3: canonical vocabulary + adequacy judgment. |
| Recovery Path | D | 4 stages with actor-chain notation: mechanism (`client →` / `server →` / `operator →` / `user →`) + SLA target drawn from Step 1d budget for this class (TTD/TTC/TTR/TTV) + named VS. ≥3 of 4 stages must carry labeled actor prefix. |
| Scenario Name | C | Specific commerce operation + failure mode. |
| Class Label | — | Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded/Impaired/Down) + affected segment. |
| User Capability | C | What user can still do. ≥1 surviving capability. |
| Status Quo Risk | C | Step 1b carrying cost for this class. Rate + horizon + named metric. |

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Section Order Requirement**: Produce all 3 scenario rows, each immediately followed by its co-located Chaos Block, before the Gap Register. Do not advance to Row 2 until Row 1 scenario cells AND its Chaos Block are complete. Do not advance to Row 3 until Row 2 scenario cells AND its Chaos Block are complete. Do not advance to the Gap Register until Row 3 scenario cells AND its Chaos Block are complete. Gap Register before Inertia Verdict. Inertia Verdict before Recommendations.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss)**

**Write this row now.**

D-first gate: complete Trigger Condition, System State, Data at Risk, and all four Recovery Path stages (actor-chain + SLA from Step 1d Class 1 budget + VS each) before writing Scenario Name, Class Label, Severity, User Capability, Status Quo Risk.

D-phase: Trigger = keepalive fails 3 × 10s / heartbeat no-response [threshold + detection signal both present]. State = order-service unreachable; cart cached locally; payment token pending. Risk = uncommitted cart (stale-write risk); pending token (expiry risk). Recovery: Stage 1 client → heartbeat detects offline / TTD = Step 1d Class 1 budget / VS named; Stage 2 client → idempotency-keyed write queue / TTC = Step 1d Class 1 budget / VS named; Stage 3 client → queue flush + server → idempotency endpoint / TTR = Step 1d Class 1 budget / VS named; Stage 4 server → order state confirmed / TTV = Step 1d Class 1 budget / VS named.
C-phase: Scenario name; Class 1; Impaired ~2% sessions; surviving capability; Status Quo Risk = Class 1 Step 1b carrying cost (rate + horizon + named metric). Acute consequence branches: no idempotency → double-charge on reconnect; no write queue → cart lost; naive retry burst → oversell. Chronic: if Class 1 gap never addressed, [metric from Step 1b] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until every column is non-placeholder, including all four Recovery Path stages each with actor-chain mechanism (labeled prefix), SLA target drawn from Step 1d Class 1 budget, and named VS, and Status Quo Risk with rate + horizon + named metric from Step 1b.**

**Chaos Block — Row 1 (co-located).**
Inject: [named service + method + duration]; Expected Behavior: [named observables if handled correctly]; Pass Signal: [named observable confirming correct handling]; Fail Signal: [named observable confirming failure]. All four required.

**Do not advance to Row 2 until Row 1 scenario cells AND Chaos Block are both complete with non-placeholder content.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

D-first gate: same sequence as Row 1. SLA targets must reference Step 1d Class 2 budget — not invented independently.

D-phase: Trigger = inventory-service error rate > 5% / 60s rolling window / health probe 503 × 3 [threshold + detection signal]. State = order-service operational; inventory-service circuit-breaker OPEN; last-known snapshot stale. Risk = reservation accuracy against stale snapshot; oversell risk during outage window. Recovery: Stage 1 server → circuit breaker trips at threshold / TTD = Step 1d Class 2 budget / VS named; Stage 2 server → snapshot-mode + oversell buffer active / TTC = Step 1d Class 2 budget / VS named; Stage 3 server → half-open probe + operator → reconciliation triggered / TTR = Step 1d Class 2 budget / VS named; Stage 4 operator → discrepancy counter verified / TTV = Step 1d Class 2 budget / VS named.
C-phase: Scenario; Class 2; Degraded all orders in outage window; surviving capability; Status Quo Risk = Class 2 Step 1b. Acute: no circuit breaker → cascade; no snapshot → placement blocked; no oversell buffer → customer-visible oversell. Chronic: if Class 2 gap never addressed, [metric] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until all four Recovery Path stages have actor-chain mechanism (labeled prefix), SLA target from Step 1d Class 2 budget, and named VS, and Status Quo Risk has rate + horizon + named metric from Step 1b.**

**Chaos Block — Row 2 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required with named observables.

**Do not advance to Row 3 until Row 2 scenario cells AND Chaos Block are both complete.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

D-first gate: same sequence as Rows 1–2. SLA targets must reference Step 1d Class 3 budget. Data at Risk must include canonical conflict vocabulary + adequacy judgment.

D-phase: Trigger = replica lag > 5s / lag metric fires split-brain alert [threshold + detection signal]. State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Risk = inventory count integrity; `last-write-wins` inadequate for inventory reservation — `manual-reconcile` with lower-count-wins rule required [adequacy judgment]. Recovery: Stage 1 server → lag alert fires / TTD = Step 1d Class 3 budget / VS named; Stage 2 operator → writes fenced to primary / TTC = Step 1d Class 3 budget / VS named; Stage 3 server → `manual-reconcile` resolution job / TTR = Step 1d Class 3 budget / VS named; Stage 4 operator → post-merge cross-check / TTV = Step 1d Class 3 budget / VS named.
C-phase: Scenario; Class 3; Impaired <1% users high-integrity risk; surviving capability; Status Quo Risk = Class 3 Step 1b. Acute: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback without notification → silent cancellation. Chronic: if Class 3 gap never addressed, [metric] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until all four Recovery Path stages have actor-chain mechanism (labeled prefix), SLA target from Step 1d Class 3 budget, and named VS; Data at Risk names canonical conflict strategy with adequacy judgment; Status Quo Risk has rate + horizon + metric from Step 1b.**

**Chaos Block — Row 3 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to the Gap Register until Row 3 scenario cells AND Chaos Block are both complete with all four chaos components.**

---

### Output Table

Single unified table. After each scenario row, append its co-located Chaos Block immediately — before the next row begins. **Do not split by column owner. Do not insert horizontal rules or section breaks between rows. Do not consolidate chaos blocks. Do not produce a standalone observability section.**

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

**Inertia Verdict**: Step 1b carrying costs + Step 1d SLA budget gaps identified above → HIGH / MEDIUM / LOW + single strongest argument against deferral (2–3 sentences).

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

## V-02 — Failure Signature Column (Axis B)

**Variation axis**: Output format — the Column Contract gains a `Failure Signature` column (Owner: D) positioned immediately after `#`. Fill requirement: the named production observable pattern — visible in telemetry during the active failure — that distinguishes this failure class from the other two. This is not the Trigger Condition (entry threshold) but the in-flight signature: the set of dashboard / log / metric signals that would appear in an on-call investigation and confirm "this is Class N, not Class 1 or 2."

**Hypothesis**: Forcing an explicit Failure Signature fill per row closes the scenario-name drift escape: a model that writes a Failure Signature must commit to a telemetry pattern before any commerce framing, making the class boundary operationally specific rather than label-only. Classes 2 and 3 collapse most often in practice (both involve a distributed component in an unexpected state); the Failure Signature column forces their distinguishing observables to be explicitly named.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment

Produce before the scenario table. Do not advance until all three parts are non-placeholder for all three classes.

**1a. Status Quo Threat**: Name the do-nothing path. HIGH / MEDIUM / LOW with one-sentence justification. What does the system do under Class 1 / Class 2 / Class 3 without intervention?

**1b. Carrying Costs** (pre-committed constraints for Status Quo Risk column):
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
| Section | Table + chaos blocks → Gap Register | Phase gate: all 3 rows + co-located chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | Within row | Bold in-row imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within row: D-phase → C-phase | D-first intra-row gate: D-owned columns complete before C-owned | Column Contract (below) |
| Column | Per column | Named owner + stage sub-specs with actor-chain notation | Column Contract (below) |

**Anti-boundary umbrella** (four escape forms closed simultaneously): **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns [escape 1: table split]. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts [escape 2: intra-table boundary]. Do not consolidate chaos blocks into a standalone chaos section or standalone chaos table [escape 3: chaos consolidation]. Do not produce a standalone observability section or observability table for Gap Register findings [escape 4: observability consolidation].**

**Chaos Test Block Specification**

| Component | Fill Requirement |
|-----------|-----------------|
| Inject | Named: service + injection method + duration. Reproducible in test harness. |
| Expected Behavior | Named observables during injection if handled correctly. |
| Pass Signal | Named observable confirming correct handling per the row's recovery path. |
| Fail Signal | Named observable confirming failure to handle. |

**Column Contract** — process before any row; column omission is a contract violation.

> **Conflict vocabulary constraint**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale` — canonical label required; free-text descriptions do not satisfy.
> **Status Quo Risk constraint**: must use Step 1b metric for the row's class; rate + horizon + named metric all required.
> **Failure Signature constraint**: must name telemetry signals observable in a live investigation — not a restatement of the Trigger Condition (entry threshold) and not the Class Label. The signature must be distinct for each row: a signature that could apply to two classes does not satisfy this criterion.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | 1, 2, 3. |
| Failure Signature | D | Named production observable pattern confirming this class is active in live telemetry. Three components: (1) *Metric or log signal* — the named dashboard metric or log pattern that is elevated or anomalous. (2) *Normal-state baseline* — what the same signal reads when the system is healthy. (3) *Class boundary discriminator* — the single observable that distinguishes this class from the most similar other class (Class 1 vs 2: client vs server origination; Class 2 vs 3: circuit-breaker state vs dual-write conflict counter). |
| Trigger Condition | D | (1) Threshold expression — quantified activation condition. (2) Detection signal — observable mechanism identifying threshold crossing. Both required. |
| System State | D | Named services, data states, consistency model. Class 3: canonical conflict vocabulary. |
| Data at Risk | D | Consistency violation type + scope. Class 3: canonical vocabulary + adequacy judgment. |
| Recovery Path | D | 4 stages with actor-chain notation: mechanism (`client →` / `server →` / `operator →` / `user →`) + SLA target (TTD/TTC/TTR/TTV) + named VS. ≥3 of 4 stages carry labeled actor prefix. |
| Scenario Name | C | Specific commerce operation + failure mode. |
| Class Label | — | Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded/Impaired/Down) + affected segment. |
| User Capability | C | What user can still do. ≥1 surviving capability. |
| Status Quo Risk | C | Step 1b carrying cost for this class. Rate + horizon + named metric. |

Column order: `#` | Failure Signature | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Section Order Requirement**: Produce all 3 scenario rows, each immediately followed by its co-located Chaos Block, before the Gap Register. Do not advance to Row 2 until Row 1 scenario cells AND its Chaos Block are complete. Do not advance to Row 3 until Row 2 scenario cells AND its Chaos Block are complete. Do not advance to the Gap Register until Row 3 scenario cells AND its Chaos Block are complete. Gap Register before Inertia Verdict.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss)**

**Write this row now.**

D-first gate: complete Failure Signature, Trigger Condition, System State, Data at Risk, and all four Recovery Path stages before writing C-phase columns.

D-phase: Failure Signature = client-write-queue-depth > 0 + zero server ACKs in client telemetry [metric: client-write-queue-depth, baseline: 0, discriminator from Class 2: this is client-originated — server-side circuit-breaker state is nominal]. Trigger = client keepalive fails 3 × 10s / heartbeat no-response [threshold + detection]. State = order-service unreachable; cart cached locally; payment token pending. Risk = uncommitted cart (stale-write risk); pending token (expiry risk). Recovery: Stage 1 client → heartbeat / TTD / VS named; Stage 2 client → idempotency-keyed write queue / TTC / VS named; Stage 3 client → queue flush + server → idempotency endpoint / TTR / VS named; Stage 4 server → order state confirmed / TTV / VS named.
C-phase: Scenario name; Class 1; Impaired ~2% sessions; surviving capability; Status Quo Risk = Class 1 Step 1b. Acute: no idempotency → double-charge; no queue → cart lost; naive retry → oversell. Chronic: if gap never addressed, [metric] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until every column is non-placeholder, including Failure Signature with all three sub-components (metric/baseline/discriminator), all four Recovery Path stages each with actor-chain mechanism, SLA, and named VS, and Status Quo Risk with rate + horizon + named metric.**

**Chaos Block — Row 1 (co-located).**
Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 2 until Row 1 scenario cells AND Chaos Block are both complete.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

D-first gate: same sequence as Row 1. Failure Signature must be distinct from Row 1 — name the Class 2 discriminator that would not appear in a Class 1 or Class 3 investigation.

D-phase: Failure Signature = circuit-breaker state = OPEN in service-mesh dashboard + order-error-rate spike [metric: circuit-breaker-state, baseline: CLOSED, discriminator from Class 3: circuit-breaker is OPEN (dependent service unreachable) vs Class 3 where circuit-breaker is CLOSED but dual-write conflict counter > 0]. Trigger = inventory-service error rate > 5% / 60s rolling / probe 503 × 3 [threshold + detection]. State = order-service operational; circuit-breaker OPEN; snapshot stale. Risk = reservation accuracy; oversell risk. Recovery: Stage 1 server → breaker trips / TTD / VS named; Stage 2 server → snapshot-mode + buffer / TTC / VS named; Stage 3 server → half-open + operator → reconciliation / TTR / VS named; Stage 4 operator → counts verified / TTV / VS named.
C-phase: Scenario; Class 2; Degraded all orders in window; capability; Status Quo Risk = Class 2 Step 1b. Acute: no breaker → cascade; no snapshot → blocked; no buffer → oversell. Chronic: [metric] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until the Failure Signature names all three sub-components and is operationally distinct from Row 1, all four Recovery Path stages have actor-chain mechanism, SLA, and named VS, and Status Quo Risk has all three components.**

**Chaos Block — Row 2 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 3 until Row 2 scenario cells AND Chaos Block are both complete.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

D-first gate: same sequence. Failure Signature must be distinct from both Row 1 and Row 2 — name the Class 3 telemetry pattern that would not appear in Classes 1 or 2. Data at Risk requires canonical conflict vocabulary + adequacy judgment.

D-phase: Failure Signature = replica-lag-alert firing + dual-write-conflict-counter > 0 in conflict monitoring dashboard [metric: dual-write-conflict-counter, baseline: 0 (no concurrent writes), discriminator from Class 2: circuit-breaker is CLOSED (service is accepting writes) but conflict counter is elevated — writes are landing, not failing]. Trigger = replica lag > 5s / lag metric fires split-brain alert [threshold + detection]. State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Risk = inventory count integrity; `last-write-wins` inadequate — `manual-reconcile` with lower-count-wins required [adequacy judgment]. Recovery: Stage 1 server → lag alert fires / TTD / VS named; Stage 2 operator → writes fenced to primary / TTC / VS named; Stage 3 server → `manual-reconcile` job / TTR / VS named; Stage 4 operator → post-merge cross-check / TTV / VS named.
C-phase: Scenario; Class 3; Impaired <1% high-integrity risk; capability; Status Quo Risk = Class 3 Step 1b. Acute: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback → silent cancellation. Chronic: [metric] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until Failure Signature is distinct from Rows 1 and 2 with all three sub-components; all four Recovery Path stages have actor-chain mechanism, SLA, and named VS; Data at Risk names canonical conflict strategy with adequacy judgment; Status Quo Risk has rate + horizon + metric.**

**Chaos Block — Row 3 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to the Gap Register until Row 3 scenario cells AND Chaos Block are both complete.**

---

### Output Table

Single unified table. After each row, append its Chaos Block immediately. **Do not split by column owner. Do not insert horizontal rules between rows. Do not consolidate chaos blocks. Do not produce standalone observability section.**

Column order: `#` | Failure Signature | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

Three findings, inline observability at finding granularity — not a separate section.

**Format per finding**:
> **[Finding Type] — [specific description]**
> `Metric:` [named] `Alert:` [condition] `Owner:` [role]

1. **Offline Experience Gap** — `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — `Metric:` ... `Alert:` ... `Owner:` ...

**Inertia Verdict**: Step 1b carrying costs + gap findings above → HIGH / MEDIUM / LOW + single strongest argument against deferral (2–3 sentences).

**Finding Completeness Checklist** (required output content):

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap]
[ ] Data Consistency Violation — [named violation]
[ ] Missing Recovery Flow — [named mechanism]
Finding types present: ___ of 3
```

Mark `[x]` only when specific, actionable, non-generic, all three inline fields present. Write "3 of 3" only when all three pass.

---
---

## V-03 — Three-Act Investment Memo (Axis C)

**Variation axis**: Phrasing register for the Inertia Assessment — the numbered sub-section structure (1a / 1b / 1c) is replaced by a prose Investment Memo organized as three acts: Act I (Situation), Act II (Risk Accumulation), Act III (Decision Trigger). The pre-commitment constraint chain is preserved by renaming references: Column Contract references "Act II" instead of "Step 1b"; at least one Row Descriptor names "Act II" as the carrying cost source. All structural requirements outside the Inertia Assessment container are identical to the R13 V-05 compact baseline, including "**Write this row now.**" imperatives.

**Hypothesis**: Prose memo framing may produce denser, more contextually specific carrying-cost statements than structured bullet lists — because the act format encourages narrative continuity across the three components (rate / horizon / metric) rather than checklist satisfaction. C-35 and C-36 are satisfied by the named section and the Act III tipping-point content. C-39 is unaffected because it targets Row Descriptors, not the Inertia Assessment.

---

You are running **flow-resilience** for topic: {Topic}.

### Investment Memo (complete before scenario table)

This section is the source of truth for Status Quo Risk fills. Do not begin the scenario table until all three acts are complete with non-placeholder content for all three failure classes.

**Act I — Situation**: Name the status-quo competitor: the do-nothing path teams actually take when they defer resilience investment for this topic. Assess the threat level as HIGH / MEDIUM / LOW with one-sentence justification. Describe what the current system does under each failure class without intervention: Class 1 behavior, Class 2 behavior, Class 3 behavior. One sentence per class.

**Act II — Risk Accumulation**: For each failure class, state the chronic carrying cost without remediation. Each statement must name the accumulation metric, the rate interval or trigger, and the trajectory horizon. These three carrying costs are pre-committed constraints: every Status Quo Risk cell in the scenario table must draw from the relevant class statement here — not author an independent risk description.

Format: *[named metric] accumulates at [rate], [horizon trajectory] without intervention.*

- Class 1 carrying cost:
- Class 2 carrying cost:
- Class 3 carrying cost:

**Act III — Decision Trigger**: For each class, name the observable threshold at which carrying costs have crossed the point where deferral becomes indefensible. Each threshold must be quantified (a named metric with a specific value or rate) paired with the monitoring signal that surfaces it.

Format: *[quantified threshold condition] / [named metric being monitored]*

- Class 1 tipping point:
- Class 2 tipping point:
- Class 3 tipping point:

---

### Pre-Output Specification

**Five-Level Anti-Omission Architecture**

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows | `#` row-index + anti-split instruction | Output table (below) |
| Section | Table + chaos blocks → Gap Register | Phase gate: all 3 rows + co-located chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | Within row | Bold in-row imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within row: D-phase → C-phase | D-first intra-row gate: D-owned columns complete before C-owned | Column Contract (below) |
| Column | Per column | Named owner + stage sub-specs with actor-chain notation | Column Contract (below) |

**Anti-boundary umbrella** (four escape forms closed simultaneously): **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns [escape 1: table split]. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts [escape 2: intra-table boundary]. Do not consolidate chaos blocks into a standalone chaos section or standalone chaos table [escape 3: chaos consolidation]. Do not produce a standalone observability section or observability table for Gap Register findings [escape 4: observability consolidation].**

**Chaos Test Block Specification**

| Component | Fill Requirement |
|-----------|-----------------|
| Inject | Named: service + injection method + duration. Reproducible in test harness. |
| Expected Behavior | Named observables during injection if handled correctly. |
| Pass Signal | Named observable confirming correct handling per the row's recovery path. |
| Fail Signal | Named observable confirming failure to handle. |

**Column Contract** — process before any row; column omission is a contract violation.

> **Conflict vocabulary constraint**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale` — canonical label required; free-text descriptions do not satisfy.
> **Status Quo Risk constraint**: must use the Act II carrying cost statement for the row's class; rate + horizon + named metric all required. An independently authored risk statement not drawn from Act II does not satisfy this constraint.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | 1, 2, 3. |
| Trigger Condition | D | (1) Threshold expression — quantified activation condition. (2) Detection signal — observable crossing mechanism. Both required. |
| System State | D | Named services, data states, consistency model. Class 3: canonical conflict vocabulary. |
| Data at Risk | D | Consistency violation type + scope. Class 3: canonical vocabulary + adequacy judgment. |
| Recovery Path | D | 4 stages with actor-chain notation: mechanism (`client →` / `server →` / `operator →` / `user →`) + SLA target (TTD/TTC/TTR/TTV) + named VS. ≥3 of 4 stages carry labeled actor prefix. |
| Scenario Name | C | Specific commerce operation + failure mode. |
| Class Label | — | Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded/Impaired/Down) + affected segment. |
| User Capability | C | What user can still do. ≥1 surviving capability. |
| Status Quo Risk | C | Act II carrying cost for this class. Rate + horizon + named metric — drawn from the Investment Memo, not authored independently. |

Column order: `#` | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Section Order Requirement**: Produce all 3 scenario rows, each immediately followed by its co-located Chaos Block, before the Gap Register. Do not advance to Row 2 until Row 1 scenario cells AND its Chaos Block are complete. Do not advance to Row 3 until Row 2 scenario cells AND its Chaos Block are complete. Do not advance to the Gap Register until Row 3 scenario cells AND its Chaos Block are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss)**

**Write this row now.**

D-first gate: complete Trigger Condition, System State, Data at Risk, all four Recovery Path stages (actor-chain + SLA + VS) before writing C-phase columns.

D-phase: Trigger = keepalive fails 3 × 10s / heartbeat no-response [threshold + detection]. State = order-service unreachable; cart cached; payment token pending. Risk = uncommitted cart (stale-write risk); pending token (expiry risk). Recovery: Stage 1 client → heartbeat / TTD / VS named; Stage 2 client → idempotency-keyed write queue / TTC / VS named; Stage 3 client → queue flush + server → idempotency endpoint / TTR / VS named; Stage 4 server → order state confirmed / TTV / VS named.
C-phase: Scenario name; Class 1; Impaired ~2%; surviving capability; Status Quo Risk = Class 1 Act II carrying cost (rate + horizon + named metric — drawn from Investment Memo). Acute: no idempotency → double-charge; no queue → cart lost; naive retry → oversell. Chronic: if Class 1 gap never addressed, [metric from Act II] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until every column is non-placeholder, including all four Recovery Path stages each with actor-chain mechanism (labeled prefix), SLA, and named VS, and Status Quo Risk drawn from Act II with rate + horizon + named metric.**

**Chaos Block — Row 1 (co-located).**
Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 2 until Row 1 scenario cells AND Chaos Block are both complete.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

D-first gate: same sequence as Row 1.

D-phase: Trigger = error rate > 5% / 60s / probe 503 × 3 [threshold + detection]. State = circuit breaker OPEN; snapshot stale. Risk = reservation accuracy; oversell risk. Recovery: Stage 1 server → breaker trips / TTD / VS named; Stage 2 server → snapshot-mode + buffer / TTC / VS named; Stage 3 server → half-open + operator → reconciliation / TTR / VS named; Stage 4 operator → counts verified / TTV / VS named.
C-phase: Scenario; Class 2; Degraded all orders in window; capability; Status Quo Risk = Class 2 Act II carrying cost. Acute: no breaker → cascade; no snapshot → blocked; no buffer → oversell. Chronic: [metric from Act II] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until all four Recovery Path stages have actor-chain mechanism, SLA, and VS, and Status Quo Risk is drawn from Act II with rate + horizon + metric.**

**Chaos Block — Row 2 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 3 until Row 2 scenario cells AND Chaos Block are both complete.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

D-first gate: same sequence as Rows 1–2. Data at Risk must include canonical conflict vocabulary + adequacy judgment.

D-phase: Trigger = replica lag > 5s / lag metric fires split-brain alert [threshold + detection]. State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Risk = inventory count integrity; `last-write-wins` inadequate — `manual-reconcile` with lower-count-wins required [adequacy judgment]. Recovery: Stage 1 server → lag alert fires / TTD / VS named; Stage 2 operator → writes fenced to primary / TTC / VS named; Stage 3 server → `manual-reconcile` job / TTR / VS named; Stage 4 operator → post-merge cross-check / TTV / VS named.
C-phase: Scenario; Class 3; Impaired <1% high-integrity risk; capability; Status Quo Risk = Class 3 Act II carrying cost. Acute: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback → silent cancellation. Chronic: [metric from Act II] accumulates at [rate], [horizon].

**Do not advance to the Chaos Block until all four stages have actor-chain mechanism, SLA, and VS; Data at Risk names canonical conflict strategy with adequacy judgment; Status Quo Risk is drawn from Act II with rate + horizon + metric.**

**Chaos Block — Row 3 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to the Gap Register until Row 3 scenario cells AND Chaos Block are both complete.**

---

### Output Table

Single unified table. After each row, append its Chaos Block immediately. **Do not split by column owner. Do not insert horizontal rules between rows. Do not consolidate chaos blocks. Do not produce standalone observability section.**

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

**Inertia Verdict**: Act II carrying costs + Act III tipping point signals + gap findings above → HIGH / MEDIUM / LOW + single strongest argument against deferral (2–3 sentences, synthesizing rather than restating).

**Finding Completeness Checklist** (required output content):

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap]
[ ] Data Consistency Violation — [named violation]
[ ] Missing Recovery Flow — [named mechanism]
Finding types present: ___ of 3
```

Mark `[x]` only when specific, actionable, non-generic, all three inline fields present. Write "3 of 3" only when all three pass.

---
---

## V-04 — SLA Budget + Failure Signature (Axes A + B)

**Variation axes**: Pre-committed SLA Budget (Axis A) combined with Failure Signature column (Axis B). Both additions extend the pre-commitment chain in orthogonal directions: the SLA Budget constrains Recovery Path stage targets; the Failure Signature column constrains in-flight class identification. Together they require the model to commit to two additional class-specific data structures before building any row.

**Hypothesis**: The two axes are structurally independent — SLA Budget targets travel through the Recovery Path column (D-owned, last in D-phase); Failure Signature travels through its own column (D-owned, first in D-phase). No criterion dependency conflict exists. The combined pre-commitment chain (carrying costs + SLA budget + failure signature) produces a scenario table where each row is falsifiable on three pre-committed dimensions before any gap finding is written.

---

You are running **flow-resilience** for topic: {Topic}.

### Step 1: Inertia Assessment

Produce before the scenario table. Do not advance until all four parts are non-placeholder for all three classes.

**1a. Status Quo Threat**: HIGH / MEDIUM / LOW with one-sentence justification. Current system behavior under each class without intervention.

**1b. Carrying Costs** (pre-committed constraints for Status Quo Risk column):
- Class 1: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 2: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 3: *[named metric] accumulates at [rate], [horizon] without intervention*

**1c. Tipping Point Signals** (quantified threshold + named metric per class):
- Class 1:
- Class 2:
- Class 3:

**1d. SLA Budget** (pre-committed Recovery Path targets — all Recovery Path SLA fills must reference this budget):
- Class 1: TTD: [target] / TTC: [target] / TTR: [target] / TTV: [target]
- Class 2: TTD: [target] / TTC: [target] / TTR: [target] / TTV: [target]
- Class 3: TTD: [target] / TTC: [target] / TTR: [target] / TTV: [target]

---

### Pre-Output Specification

**Five-Level Anti-Omission Architecture**

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows | `#` row-index + anti-split instruction | Output table (below) |
| Section | Table + chaos blocks → Gap Register | Phase gate: all 3 rows + co-located chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | Within row | Bold in-row imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within row: D-phase → C-phase | D-first intra-row gate: D-owned columns complete before C-owned | Column Contract (below) |
| Column | Per column | Named owner + stage sub-specs with actor-chain notation | Column Contract (below) |

**Anti-boundary umbrella** (four escape forms closed simultaneously): **Do not create separate tables for Distributed Systems Expert columns and Commerce Expert columns [escape 1: table split]. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts [escape 2: intra-table boundary]. Do not consolidate chaos blocks into a standalone chaos section or standalone chaos table [escape 3: chaos consolidation]. Do not produce a standalone observability section or observability table for Gap Register findings [escape 4: observability consolidation].**

**Chaos Test Block Specification**

| Component | Fill Requirement |
|-----------|-----------------|
| Inject | Named: service + injection method + duration. Reproducible in test harness. |
| Expected Behavior | Named observables during injection if handled correctly. |
| Pass Signal | Named observable confirming correct handling per the row's recovery path. |
| Fail Signal | Named observable confirming failure to handle. |

**Column Contract** — process before any row; column omission is a contract violation.

> **Conflict vocabulary constraint**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale` — canonical label required.
> **Status Quo Risk constraint**: must use Step 1b metric for the row's class; rate + horizon + named metric all required.
> **SLA constraint**: Recovery Path SLA targets must reference Step 1d budget for the row's class.
> **Failure Signature constraint**: must name operationally distinct telemetry signals; must include class boundary discriminator.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | 1, 2, 3. |
| Failure Signature | D | Named production observable pattern active during this failure class. Three components: (1) metric/log signal elevated or anomalous; (2) normal-state baseline for that signal; (3) class boundary discriminator — the single observable distinguishing this class from its nearest neighbor. |
| Trigger Condition | D | (1) Threshold expression — quantified activation condition. (2) Detection signal — observable crossing mechanism. Both required. |
| System State | D | Named services, data states, consistency model. Class 3: canonical conflict vocabulary. |
| Data at Risk | D | Consistency violation type + scope. Class 3: canonical vocabulary + adequacy judgment. |
| Recovery Path | D | 4 stages with actor-chain notation: mechanism (`client →` / `server →` / `operator →` / `user →`) + SLA target referencing Step 1d budget for this class + named VS. ≥3 of 4 stages carry labeled actor prefix. |
| Scenario Name | C | Specific commerce operation + failure mode. |
| Class Label | — | Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded/Impaired/Down) + affected segment. |
| User Capability | C | What user can still do. ≥1 surviving capability. |
| Status Quo Risk | C | Step 1b carrying cost for this class. Rate + horizon + named metric. |

Column order: `#` | Failure Signature | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Section Order Requirement**: Produce all 3 scenario rows, each immediately followed by its co-located Chaos Block, before the Gap Register. Do not advance to Row 2 until Row 1 scenario cells AND its Chaos Block are complete. Do not advance to Row 3 until Row 2 scenario cells AND its Chaos Block are complete. Do not advance to the Gap Register until Row 3 scenario cells AND its Chaos Block are complete.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss)**

**Write this row now.**

D-first gate: complete Failure Signature, Trigger Condition, System State, Data at Risk, and all four Recovery Path stages (actor-chain + SLA from Step 1d Class 1 budget + VS) before C-phase columns.

D-phase: Failure Signature = client-write-queue-depth > 0 + zero server ACKs / baseline: queue-depth = 0 / discriminator: client-originated (server circuit-breaker is CLOSED). Trigger = keepalive fails 3 × 10s / heartbeat no-response. State = order-service unreachable; cart cached; payment token pending. Risk = uncommitted cart; pending token. Recovery: Stage 1 client → heartbeat / TTD = Step 1d Class 1 / VS named; Stage 2 client → idempotency write queue / TTC = Step 1d Class 1 / VS named; Stage 3 client → flush + server → idempotency endpoint / TTR = Step 1d Class 1 / VS named; Stage 4 server → state confirmed / TTV = Step 1d Class 1 / VS named.
C-phase: Scenario; Class 1; Impaired ~2%; capability; Status Quo Risk = Class 1 Step 1b. Acute: no idempotency → double-charge; no queue → cart lost; naive retry → oversell. Chronic: [metric] at [rate], [horizon].

**Do not advance to the Chaos Block until Failure Signature (3 sub-components), all four Recovery Path stages (actor-chain + Step 1d SLA + VS), and Status Quo Risk (rate + horizon + metric) are all non-placeholder.**

**Chaos Block — Row 1 (co-located).**
Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 2 until Row 1 cells AND Chaos Block are both complete.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

D-first gate: same sequence. Failure Signature must be operationally distinct from Row 1. SLA targets from Step 1d Class 2 budget.

D-phase: Failure Signature = circuit-breaker-state = OPEN in service-mesh dashboard + order-error-rate spike / baseline: CLOSED + error-rate nominal / discriminator from Class 3: OPEN = service unreachable (Class 2); CLOSED + dual-write-conflict-counter > 0 = concurrent writes landing (Class 3). Trigger = error rate > 5% / 60s / probe 503 × 3. State = circuit breaker OPEN; snapshot stale. Risk = reservation accuracy; oversell. Recovery: Stage 1 server → breaker trips / TTD = Step 1d Class 2 / VS named; Stage 2 server → snapshot-mode + buffer / TTC = Step 1d Class 2 / VS named; Stage 3 server → half-open + operator → reconciliation / TTR = Step 1d Class 2 / VS named; Stage 4 operator → counts verified / TTV = Step 1d Class 2 / VS named.
C-phase: Scenario; Class 2; Degraded all orders; capability; Status Quo Risk = Class 2 Step 1b. Acute: no breaker → cascade; no snapshot → blocked; no buffer → oversell. Chronic: [metric] at [rate], [horizon].

**Do not advance to the Chaos Block until Failure Signature (3 sub-components, distinct from Row 1), all four Recovery Path stages (actor-chain + Step 1d Class 2 SLA + VS), and Status Quo Risk (rate + horizon + metric) are all non-placeholder.**

**Chaos Block — Row 2 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 3 until Row 2 cells AND Chaos Block are both complete.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

D-first gate: same sequence. Failure Signature distinct from Rows 1 and 2. SLA targets from Step 1d Class 3 budget. Data at Risk: canonical vocabulary + adequacy judgment required.

D-phase: Failure Signature = replica-lag-alert firing + dual-write-conflict-counter > 0 in conflict-monitor / baseline: lag < 1s + counter = 0 / discriminator from Class 2: circuit-breaker CLOSED (writes accepted) but conflict counter elevated — service is up, data is diverging. Trigger = replica lag > 5s / lag metric fires split-brain alert. State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Risk = inventory count integrity; `last-write-wins` inadequate — `manual-reconcile` with lower-count-wins required. Recovery: Stage 1 server → lag alert fires / TTD = Step 1d Class 3 / VS named; Stage 2 operator → writes fenced to primary / TTC = Step 1d Class 3 / VS named; Stage 3 server → `manual-reconcile` job / TTR = Step 1d Class 3 / VS named; Stage 4 operator → cross-check / TTV = Step 1d Class 3 / VS named.
C-phase: Scenario; Class 3; Impaired <1%; capability; Status Quo Risk = Class 3 Step 1b. Acute: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback → silent cancellation. Chronic: [metric] at [rate], [horizon].

**Do not advance to the Chaos Block until Failure Signature (3 sub-components, distinct from Rows 1 and 2), all four Recovery Path stages (actor-chain + Step 1d Class 3 SLA + VS), Data at Risk (canonical vocabulary + adequacy judgment), and Status Quo Risk (rate + horizon + metric) are all non-placeholder.**

**Chaos Block — Row 3 (co-located).** Inject / Expected Behavior / Pass Signal / Fail Signal — all four required.

**Do not advance to the Gap Register until Row 3 cells AND Chaos Block are both complete.**

---

### Output Table

Single unified table. After each row, append its Chaos Block immediately. **Do not split by column owner. Do not insert horizontal rules between rows. Do not consolidate chaos blocks. Do not produce standalone observability section.**

Column order: `#` | Failure Signature | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

Three findings, inline observability — not a separate section.

> **[Finding Type] — [specific description]**
> `Metric:` [named] `Alert:` [condition] `Owner:` [role]

1. **Offline Experience Gap** — `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — `Metric:` ... `Alert:` ... `Owner:` ...

**Inertia Verdict**: Step 1b costs + Step 1d SLA budget gaps + findings → HIGH / MEDIUM / LOW + single strongest argument against deferral (2–3 sentences).

**Finding Completeness Checklist** (required output content):

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap]
[ ] Data Consistency Violation — [named violation]
[ ] Missing Recovery Flow — [named mechanism]
Finding types present: ___ of 3
```

Mark `[x]` only when specific, actionable, non-generic, all three inline fields present. Write "3 of 3" only when all three pass.

---
---

## V-05 — Compact Synthesis: SLA Budget + Failure Signature + Three-Act Memo (Axes A + B + C)

**Variation axes**: All three axes in minimum viable structure. The Investment Memo (Axis C) replaces numbered sub-sections; Step 1d SLA Budget (Axis A) is a compact table within the memo; the Failure Signature column (Axis B) is in the Column Contract. Architecture table, anti-boundary umbrella, chaos specification, column contract, and row descriptors are compressed to eliminate redundancy while preserving every load-bearing element for all 32 criteria.

**Hypothesis**: The minimum-token prompt achieving 32/32 with three structural additions (SLA Budget, Failure Signature, Investment Memo) reveals which elements are load-bearing across the three axes and which are restatements. Compact structure is also the most maintainable baseline for future criterion additions.

---

You are running **flow-resilience** for topic: {Topic}.

### Investment Memo (complete before scenario table)

Do not advance to the scenario table until all four parts contain non-placeholder content for all three classes.

**Act I — Situation**: Name the do-nothing competitor. HIGH / MEDIUM / LOW threat + one-sentence justification. Current system behavior under Class 1 / Class 2 / Class 3 without intervention (one sentence each).

**Act II — Risk Accumulation** (pre-committed carrying cost constraints — Status Quo Risk cells must reference these; independently authored risk statements do not satisfy):
- Class 1: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 2: *[named metric] accumulates at [rate], [horizon] without intervention*
- Class 3: *[named metric] accumulates at [rate], [horizon] without intervention*

**Act III — Decision Trigger** (quantified threshold + named metric per class — empirical exit condition for each inertia claim):
- Class 1:
- Class 2:
- Class 3:

**SLA Budget** (pre-committed Recovery Path targets — all Recovery Path SLA fills must reference this table; per-row SLA invention without reference does not satisfy):

| Class | TTD | TTC | TTR | TTV |
|-------|-----|-----|-----|-----|
| Class 1 | | | | |
| Class 2 | | | | |
| Class 3 | | | | |

---

### Pre-Output Specification

**Five-Level Anti-Omission Architecture**

| Level | Scope | Mechanism | Artifact |
|-------|-------|-----------|---------|
| Table | All rows | `#` row-index + anti-split | Output table (below) |
| Section | Table + chaos blocks → Gap Register | Phase gate: rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | Within row | Bold in-row imperative at cell granularity | Row Descriptors (below) |
| Column-Group | Within row: D-phase → C-phase | D-first gate | Column Contract (below) |
| Column | Per column | Named owner + actor-chain stage sub-specs | Column Contract (below) |

**Anti-boundary umbrella**: **Do not create separate tables for Distributed Systems Expert and Commerce Expert columns [escape 1]. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts [escape 2]. Do not consolidate chaos blocks into a standalone chaos section or standalone chaos table [escape 3]. Do not produce a standalone observability section or observability table for Gap Register findings [escape 4].**

**Chaos Test Block Specification**

| Component | Fill Requirement |
|-----------|-----------------|
| Inject | Named: service + method + duration. Reproducible. |
| Expected Behavior | Named observables if handled correctly. |
| Pass Signal | Named observable confirming correct handling. |
| Fail Signal | Named observable confirming failure. |

**Column Contract** — process before any row; column omission is a contract violation.

> **Conflict vocabulary**: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale` — canonical label only.
> **Status Quo Risk**: Act II carrying cost for this class — rate + horizon + named metric.
> **SLA**: Recovery Path SLA targets drawn from SLA Budget table — per-row invention is a contract violation.
> **Failure Signature**: operationally distinct telemetry pattern; must include class boundary discriminator.

| Name | Owner | Fill Requirement |
|------|-------|-----------------|
| `#` | — | 1, 2, 3. |
| Failure Signature | D | (1) Named metric/log signal anomalous during failure. (2) Normal-state baseline. (3) Class boundary discriminator — observable distinguishing this class from nearest neighbor. |
| Trigger Condition | D | (1) Threshold expression — quantified. (2) Detection signal — observable. Both required. |
| System State | D | Named services, data states, consistency model. Class 3: canonical conflict vocabulary. |
| Data at Risk | D | Violation type + scope. Class 3: canonical vocabulary + adequacy judgment. |
| Recovery Path | D | 4 stages: actor-chain mechanism + SLA from SLA Budget + named VS. ≥3 stages carry labeled prefix. |
| Scenario Name | C | Specific commerce operation + failure mode. |
| Class Label | — | Class 1 / Class 2 / Class 3. No merging. |
| Severity + Blast Radius | C | Severity (Degraded/Impaired/Down) + segment. |
| User Capability | C | ≥1 surviving capability. |
| Status Quo Risk | C | Act II carrying cost for this class. Rate + horizon + metric. |

Column order: `#` | Failure Signature | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

**Section Order Requirement**: Produce all 3 rows each followed immediately by its Chaos Block before the Gap Register. Do not advance to Row N+1 until Row N scenario cells AND its Chaos Block are complete. Gap Register before Inertia Verdict.

---

### Row Descriptors

**Row 1 — Class 1 (Full Connectivity Loss)**

**Write this row now.**

D-first gate: Failure Signature, Trigger, State, Risk, Recovery Path (all 4 stages) complete before Scenario Name, Class Label, Severity, Capability, Status Quo Risk.

D-phase: FS = client-write-queue-depth > 0 + zero server ACKs / baseline: 0 / discriminator: client-origin (server CB CLOSED). Trigger = keepalive fails 3 × 10s / heartbeat no-response. State = order-service unreachable; cart cached; payment token pending. Risk = uncommitted cart; pending token. Recovery: S1 client → heartbeat / TTD from SLA Budget Class 1 / VS named; S2 client → idempotency write queue / TTC / VS named; S3 client → flush + server → idempotency endpoint / TTR / VS named; S4 server → state confirmed / TTV / VS named.
C-phase: Scenario; Class 1; Impaired ~2%; capability; SQR = Class 1 Act II (rate + horizon + metric). Acute: no idempotency → double-charge; no queue → cart lost; retry burst → oversell. Chronic: [Act II metric] at [rate], [horizon].

**Do not advance to Chaos Block until: Failure Signature (3 sub-components), all 4 Recovery Path stages (actor-chain prefix + SLA Budget SLA + named VS each), Status Quo Risk (rate + horizon + metric from Act II) — all non-placeholder.**

**Chaos Block — Row 1 (co-located).** Inject / Expected / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 2 until Row 1 cells AND Chaos Block are both complete.**

---

**Row 2 — Class 2 (Partial Failure / Dependent Service Unavailable)**

**Write this row now.**

D-first gate: same sequence. FS must be distinct from Row 1. SLA from Class 2 SLA Budget.

D-phase: FS = CB-state = OPEN + error-rate spike / baseline: CLOSED + nominal / discriminator from Class 3: OPEN = unreachable (Class 2); CLOSED + conflict-counter > 0 = concurrent writes (Class 3). Trigger = error rate > 5% / 60s / probe 503 × 3. State = CB OPEN; snapshot stale. Risk = reservation accuracy; oversell risk. Recovery: S1 server → CB trips / TTD Class 2 / VS named; S2 server → snapshot-mode + buffer / TTC Class 2 / VS named; S3 server → half-open + operator → reconcile / TTR Class 2 / VS named; S4 operator → counts verified / TTV Class 2 / VS named.
C-phase: Scenario; Class 2; Degraded all orders; capability; SQR = Class 2 Act II. Acute: no breaker → cascade; no snapshot → blocked; no buffer → oversell. Chronic: [Act II metric] at [rate], [horizon].

**Do not advance to Chaos Block until: FS (3 sub-components, distinct from R1), all 4 stages (actor-chain + Class 2 SLA Budget + VS), SQR (rate + horizon + metric) — all non-placeholder.**

**Chaos Block — Row 2 (co-located).** Inject / Expected / Pass Signal / Fail Signal — all four required.

**Do not advance to Row 3 until Row 2 cells AND Chaos Block are both complete.**

---

**Row 3 — Class 3 (Split-Brain / Concurrent Write Conflict)**

**Write this row now.**

D-first gate: same sequence. FS distinct from Rows 1 and 2. SLA from Class 3 SLA Budget. Data at Risk: canonical vocabulary + adequacy judgment.

D-phase: FS = replica-lag-alert + dual-write-conflict-counter > 0 / baseline: lag < 1s + counter = 0 / discriminator from Class 2: CB CLOSED (writes accepted) but counter elevated — service up, data diverging. Trigger = replica lag > 5s / lag metric fires split-brain alert. State = two nodes accepting writes; vector clocks diverged; `last-write-wins` active. Risk = inventory count integrity; `last-write-wins` inadequate — `manual-reconcile` with lower-count-wins required. Recovery: S1 server → lag alert / TTD Class 3 / VS named; S2 operator → writes fenced to primary / TTC Class 3 / VS named; S3 server → `manual-reconcile` job / TTR Class 3 / VS named; S4 operator → cross-check / TTV Class 3 / VS named.
C-phase: Scenario; Class 3; Impaired <1%; capability; SQR = Class 3 Act II. Acute: `last-write-wins` → oversell; naive `merge` → phantom inventory; rollback → silent cancellation. Chronic: [Act II metric] at [rate], [horizon].

**Do not advance to Chaos Block until: FS (3 sub-components, distinct from R1 and R2), all 4 stages (actor-chain + Class 3 SLA Budget + VS), Data at Risk (canonical conflict vocab + adequacy judgment), SQR (rate + horizon + metric from Act II) — all non-placeholder.**

**Chaos Block — Row 3 (co-located).** Inject / Expected / Pass Signal / Fail Signal — all four required.

**Do not advance to Gap Register until Row 3 cells AND Chaos Block are both complete.**

---

### Output Table

Single unified table. Append each row's Chaos Block immediately after that row — before the next row begins. **No column-owner split. No intra-row horizontal rules or section breaks. No standalone chaos section. No standalone observability section.**

Column order: `#` | Failure Signature | Trigger Condition | System State | Data at Risk | Recovery Path | Scenario Name | Class Label | Severity + Blast Radius | User Capability | Status Quo Risk

---

### Gap Register

Three findings, inline observability — not a separate section.

> **[Finding Type] — [specific description]**
> `Metric:` [named] `Alert:` [condition] `Owner:` [role]

1. **Offline Experience Gap** — `Metric:` ... `Alert:` ... `Owner:` ...
2. **Data Consistency Violation** — `Metric:` ... `Alert:` ... `Owner:` ...
3. **Missing Recovery Flow** — `Metric:` ... `Alert:` ... `Owner:` ...

**Inertia Verdict**: Act II costs + SLA Budget gaps + findings → HIGH / MEDIUM / LOW + single strongest argument against deferral (2–3 sentences).

**Finding Completeness Checklist** (required output content):

```
Finding Completeness:
[ ] Offline Experience Gap — [named gap]
[ ] Data Consistency Violation — [named violation]
[ ] Missing Recovery Flow — [named mechanism]
Finding types present: ___ of 3
```

Mark `[x]` only when specific, actionable, non-generic, all three inline fields present. Write "3 of 3" only when all three pass.

---
---

## Projected Criterion Coverage — R14 Variations

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-09 | Chaos Block: Inject / Expected / Pass / Fail | PASS | PASS | PASS | PASS | PASS |
| C-10 | Per-finding observability: Metric / Alert / Owner | PASS | PASS | PASS | PASS | PASS |
| C-11 | Actor-chain notation on Recovery Path stages | PASS | PASS | PASS | PASS | PASS |
| C-12 | Constrained conflict vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-13 | Gap-merge prevention via self-verifying count | PASS | PASS | PASS | PASS | PASS |
| C-14 | Chaos blocks co-located per row + anti-boundary | PASS | PASS | PASS | PASS | PASS |
| C-15 | Observability hooks inline, not standalone section | PASS | PASS | PASS | PASS | PASS |
| C-16 | Completeness checklist as model-generated output | PASS | PASS | PASS | PASS | PASS |
| C-17 | `#` column + anti-split instruction | PASS | PASS | PASS | PASS | PASS |
| C-18 | Section-level phase gate (rows + chaos before Gap Register) | PASS | PASS | PASS | PASS | PASS |
| C-19 | Slot-level in-row bold imperatives (two-part pattern) | PASS | PASS | PASS | PASS | PASS |
| C-20 | Column-level ownership assignment | PASS | PASS | PASS | PASS | PASS |
| C-21 | Five-level anti-omission architecture named | PASS | PASS | PASS | PASS | PASS |
| C-22 | Anti-boundary by structural symptom | PASS | PASS | PASS | PASS | PASS |
| C-23 | In-row bold imperative at cell granularity | PASS | PASS | PASS | PASS | PASS |
| C-24 | Column meta-table before output table | PASS | PASS | PASS | PASS | PASS |
| C-25 | Two-symptom anti-boundary (table split + intra-table boundary) | PASS | PASS | PASS | PASS | PASS |
| C-26 | Architecture-to-contract forward reference by section name | PASS | PASS | PASS | PASS | PASS |
| C-27 | Consequence enumeration per row descriptor | PASS | PASS | PASS | PASS | PASS |
| C-28 | Sub-field completeness gate naming stage sub-structure | PASS | PASS | PASS | PASS | PASS |
| C-29 | Chronic consequence per row (inaction framing) | PASS | PASS | PASS | PASS | PASS |
| C-31 | Three-component chronic accumulation: rate + horizon + metric | PASS | PASS | PASS | PASS | PASS |
| C-32 | Column-group gate as 5th level of architecture | PASS | PASS | PASS | PASS | PASS |
| C-33 | Trigger Condition: threshold expression + detection signal | PASS | PASS | PASS | PASS | PASS |
| C-34 | Verification Signal per Recovery Path stage | PASS | PASS | PASS | PASS | PASS |
| C-35 | Pre-table inertia with per-class carrying costs pre-committed | PASS | PASS | PASS | PASS | PASS |
| C-36 | Per-class tipping point signal (quantified + named metric) | PASS | PASS | PASS | PASS | PASS |
| C-37 | Inertia verdict after Gap Register referencing gaps + costs | PASS | PASS | PASS | PASS | PASS |
| C-38 | Four-escape anti-boundary umbrella in single block | PASS | PASS | PASS | PASS | PASS |
| C-39 | Present-tense write imperative: "Write this row now" | PASS | PASS | PASS | PASS | PASS |
| C-40 | Section Order Requirement names chaos blocks at row granularity | PASS | PASS | PASS | PASS | PASS |

**Projected scores (v13 denominator 32)**: All five variations project 32/32 → composite 100.00. Discriminator is structural diversity achieving the same ceiling, not ceiling movement.

**R14 structural discriminators**:

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| SLA Budget (Axis A) | YES | no | no | YES | YES |
| Failure Signature column (Axis B) | no | YES | no | YES | YES |
| Three-Act Investment Memo (Axis C) | no | no | YES | no | YES (compact) |
| Role sequence | D-first | D-first | D-first | D-first | D-first |
| Gap Register format | Finding-forward | Finding-forward | Finding-forward | Finding-forward | Finding-forward |
| Inertia Assessment container | Numbered (1a–1d) | Numbered (1a–1c) | Prose memo | Numbered (1a–1d) | Prose memo + SLA table |
| Column count | 10 | 11 | 10 | 11 | 11 |
| C-39 risk | Low | Low | Low | Low | Low |
| Novelty value | SLA pre-commitment | Class-boundary telemetry | Memo container format | Combined pre-commitment | Minimum viable 3-axis |

**Notes on C-39 compliance**: All five variations use "**Write this row now.**" in bold at cell granularity for at least two Row Descriptors. None use "Begin Row N here" or equivalent locational markers. C-39 risk is uniformly low — the variation axes (SLA Budget, Failure Signature, Memo container) do not modify the slot-level imperative phrasing.

**Notes on C-40 compliance**: All five Section Order Requirements explicitly name the Chaos Block as a row-level advance condition: "Do not advance to Row N+1 until Row N scenario cells AND its Chaos Block are complete." This names the chaos block at row granularity, satisfying C-40's requirement that chaos block completion be a sequencing dependency distinct from section-level gating.

**Notes on C-35 compliance for V-03**: The Investment Memo is a named pre-table section. The Column Contract references "Act II carrying cost" as the source for Status Quo Risk fills. Row Descriptors name "Act II" explicitly. The C-35 pass condition (named pre-table section + Column Contract names it + at least one row descriptor names it) is fully satisfied — the container rename from "Step 1: Inertia Assessment" to "Investment Memo" is a phrasing-register change, not a structural change.
