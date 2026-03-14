# /flow: Specification

**Topic**: sim
**Namespace**: /flow:
**Skills**: 7
**Default mode**: Full
**Audience**: Domain developers -- Sales, Finance, Operations, Commerce, Copilot Studio, Power Automate, and Connectors developers who build and debug business processes on Dynamics 365 and Power Platform

## Purpose

Does the business process work? /flow: lets a domain developer simulate an end-to-end process -- lead qualification, period close, order fulfillment, conversation routing, flow execution -- and discover missing steps, broken handoffs, and unhandled exceptions before anything reaches production.

## Skills

### /flow:lifecycle

**What**: Simulate a multi-step business document or entity lifecycle from start state to end state, tracing every status transition, side effect, and exception path.
**Validated by**: Sales (BPF stage traversal, L2O conversion), Finance (period close sequences, P2P posting), Operations (document flow -- PO confirmation through invoicing)
**Input**: Business process name, start state (entity + field values), end state (expected outcome), and optionally the BPF or workflow definition driving the process.
**Output**: Process trace artifact (structured table per step: step number, operation, pre-state, post-state, side effects, decision points, exception paths) with prioritized findings.
**Lifecycle**:
- Setup: Identify the process (e.g., Lead-to-Opportunity), define start state (Lead with Status=Open, BANT fields populated), end state (Opportunity with Status=Won, ActualRevenue set), select roles (Sales Dev, CRM Admin). Detect if a BPF governs the process and load its stage definitions.
- Execute: Walk each step sequentially and through branching paths. Step 1: QualifyLead fires -- creates Account, Contact, Opportunity atomically. Step 2: BPF advances to Develop stage -- EstimatedRevenue required. Step 3: Opportunity product lines added -- price list lookup, discount calculation. At each step, record pre-state, post-state, plugins that fire, async jobs queued, and records created. Flag branching: lead disqualification branches to close, opportunity reassignment branches to different BPF.
- Findings: Synthesize into prioritized list. P1: No duplicate lead detection before QualifyLead -- two sellers can qualify the same lead simultaneously. P2: BPF Propose-to-Close gate requires approval but no timeout is configured -- deals stall indefinitely. P3: Forecast rollup does not recalculate when opportunity owner changes.
- Amend: Domain expert reviews: "Duplicates are handled by a real-time plugin on pre-validation of QualifyLead -- re-simulate step 1 with that plugin in the chain." Re-trace step 1 with the duplicate detection plugin, verify it blocks the second qualification attempt, update findings.
**Lightweight**: --quick collapses to: user names the process, execute traces the happy path only (no branching), findings lists top 3 issues, no amend phase.
**Artifact**: `flow/lifecycle/sim-l2o-2026-03-14.md`
**Example**:
```
User: /flow:lifecycle
> What business process? Lead-to-Opportunity in Dynamics 365 Sales
> Setup: L2O pipeline. Start=Lead(Status=Open, CompanyName set, BudgetAmount > 0).
  End=Opportunity(Status=Won, ActualRevenue > 0). Roles=Sales Dev + CRM Admin.
  BPF detected: Sales Process (4 stages: Qualify, Develop, Propose, Close).
> Execute:
  Step 1: QualifyLead API call
    Pre: Lead(statecode=0, statuscode=1)
    Post: Account created, Contact created, Opportunity created (statecode=0, statuscode=1)
    Plugins: DuplicateDetection (pre-validation, sync), LeadScoring (post-op, async)
    Side effects: BPF instance created, Sales Accelerator sequence triggered
    Branch: If Lead(statuscode=4 Disqualified) -> skip to close, no records created
  Step 2: BPF Develop stage
    Pre: Opportunity(estimatedvalue=null, BPF stage=Qualify)
    Post: Opportunity(estimatedvalue=50000, BPF stage=Develop)
    Gate: estimatedvalue required, estimatedclosedate required
    Plugins: ForecastRollup (post-op, async)
  [... steps 3-6 ...]
> Findings:
  P1: No concurrency guard on QualifyLead -- two simultaneous calls create duplicate opportunities
  P2: BPF Propose->Close gate has no approval timeout -- 47 opportunities stuck >30 days
  P3: Owner reassignment does not trigger forecast recalculation
> Amend: "DuplicateDetection plugin handles this on pre-validation"
  -> Re-simulated step 1: confirmed plugin throws InvalidPluginExecutionException on duplicate
  -> P1 downgraded to P3 (plugin exists but error message is not user-friendly)
```

---

### /flow:conversation

**What**: Simulate a multi-turn conversation through a Copilot Studio agent's topic graph, tracing topic activation, variable state, knowledge retrieval, and escalation paths.
**Validated by**: Copilot Studio (5, both backend and developer personas), Customer Service (session context propagation)
**Input**: Agent name or topic graph definition, initial user utterance, and optionally a sequence of follow-up utterances for multi-turn simulation.
**Output**: Conversation trace artifact (per-turn: user utterance, topic matched, nodes executed, variables set, actions called, response generated) with findings on context loss, misrouting, and fallback quality.
**Lifecycle**:
- Setup: Identify the agent (e.g., Contoso Support Bot), load topic graph, define the conversation scenario (3-turn: "I need to return a product" -> "Order 12345" -> "It arrived damaged"). Select roles (Copilot Studio Dev, Customer Service SME). Identify knowledge sources configured (SharePoint KB, Dataverse FAQ table).
- Execute: Simulate each turn. Turn 1: utterance "I need to return a product" -> trigger phrase matching evaluates 23 topics -> "Product Returns" topic activates (confidence 0.92) -> Question node asks for order number -> variable OrderNumber awaits input. Turn 2: "Order 12345" -> entity extraction fills OrderNumber=12345 -> Condition node checks order status via Power Automate flow -> flow returns Status=Delivered -> branch to "Return Eligible" path -> Action node calls CreateReturnRequest Custom API. Turn 3: "It arrived damaged" -> Condition node checks DamageReport variable (null) -> redirects to "Damage Report" topic -> generative answers retrieves return policy from SharePoint KB -> response generated with citation.
- Findings: P1: If the flow call in Turn 2 times out (>30s), the agent gives no feedback -- user sees silence for 30 seconds, then a generic error. No retry or graceful degradation. P2: "Damage Report" topic does not carry OrderNumber from the parent topic -- variable scoping is topic-level, not session-level. Agent will ask for the order number again. P3: Generative answer in Turn 3 cites a 2024 return policy document; the 2025 policy with updated damage thresholds is not in the knowledge source.
- Amend: Dev reviews: "OrderNumber is actually a global variable, not topic-scoped -- re-simulate Turn 3 with global scope." Re-trace: confirmed global variable carries through. P2 resolved. Dev also adds: "The flow timeout is 10s, not 30s -- re-simulate the timeout path." Re-trace with 10s timeout: agent shows "I'm still looking..." message at 5s, then retries once. P1 downgraded to P2 (timeout handling exists but retry only happens once).
**Lightweight**: --quick collapses to single-turn simulation: one utterance, trace topic match and response, list top findings.
**Artifact**: `flow/conversation/sim-contoso-returns-2026-03-14.md`
**Example**:
```
User: /flow:conversation
> Which agent? Contoso Support Bot (3 knowledge sources, 23 topics)
> Scenario: Customer wants to return a damaged product (3 turns)
> Turn 1: "I need to return a product"
  Topic matched: Product Returns (confidence 0.92, 2nd: General Inquiry 0.34)
  Nodes: Trigger -> Message("I can help with returns") -> Question("Order number?")
  Variables: OrderNumber=awaiting_input
  Response: "I can help with that! What's your order number?"
> Turn 2: "Order 12345"
  Entity extraction: OrderNumber=12345
  Nodes: Condition(OrderStatus) -> Action(GetOrderDetails flow) -> Branch(Delivered->eligible)
  Flow call: GetOrderDetails(12345) -> {status: "Delivered", date: "2026-03-01"}
  Variables: OrderNumber=12345, OrderStatus=Delivered, ReturnEligible=true
  Response: "Order 12345 is eligible for return. What's the reason?"
> Turn 3: "It arrived damaged"
  Topic redirect: Product Returns -> Damage Report
  Knowledge retrieval: SharePoint KB -> "Return Policy 2024.pdf" chunk 3 (damage threshold: $50)
  Variables: DamageReason="arrived damaged", OrderNumber=12345 (global, carried)
  Response: "I'm sorry to hear that. For damaged items, [policy details]. I've started a return..."
> Findings:
  P1: Flow timeout path shows 30s silence with no user feedback
  P2: Knowledge source outdated -- 2024 policy, 2025 policy not indexed
  P3: No disambiguation when multiple orders exist for the customer
```

---

### /flow:trigger

**What**: Simulate which automations fire when a specific record change occurs -- evaluate all registered triggers (plugin steps, flows, business rules, workflows, agent topics) against a record event.
**Validated by**: Automate (trigger evaluation -- "which of my 15 flows fire?"), Copilot Studio (topic activation), Dataverse (plugin registration pipeline)
**Input**: Table name, event type (create/update/delete), and the specific field changes (e.g., Account.revenue changed from 50000 to 100000).
**Output**: Trigger evaluation matrix (each registered automation with match/no-match reasoning, execution order, concurrency behavior) with findings on conflicts and gaps.
**Lifecycle**:
- Setup: Identify the record event (Update on Account, fields changed: revenue, ownerid). Load all registered automations: 4 plugin steps (2 sync pre-op, 1 sync post-op, 1 async), 3 cloud flows with Dataverse triggers, 2 business rules, 1 classic workflow. Define the record context (business unit, owner, status).
- Execute: Evaluate each automation's filter against the event. Plugin "RevenueValidation" (pre-op, sync): filters on revenue field change -> MATCH, executes at stage 20, order 1. Plugin "TerritoryAssignment" (pre-op, sync): filters on ownerid change -> MATCH, executes at stage 20, order 2. Cloud flow "NotifyManager": trigger condition `@triggerBody()?['revenue']` changed -> MATCH, runs async after commit. Cloud flow "UpdateForecast": trigger condition `@triggerBody()?['statecode']` eq 0 AND revenue changed -> MATCH. Cloud flow "SyncToMarketing": trigger filters on `statuscode` change only -> NO MATCH (statuscode not changed). Business rule "RequireDescription": condition revenue > 100000 -> MATCH, sets description to required.
- Findings: P1: RevenueValidation and TerritoryAssignment both fire at stage 20 pre-operation -- execution order depends on registration order, which is fragile. If TerritoryAssignment changes the owner before RevenueValidation reads it, validation uses stale data. P2: NotifyManager and UpdateForecast both trigger on revenue change with no deduplication -- if both modify the same record, the last writer wins. P3: No automation handles the case where revenue is set to $0 (deal lost but not formally closed).
- Amend: Dev reviews: "RevenueValidation is registered at order 1, TerritoryAssignment at order 2 -- the ordering is intentional." Re-evaluate: confirmed order is deterministic. P1 downgraded to P3 (ordering works but is undocumented). Dev adds: "UpdateForecast uses a 2-minute delay to avoid conflict with NotifyManager." P2 resolved.
**Lightweight**: --quick lists all matching triggers with match reasoning in a single table, no execution order analysis or conflict detection.
**Artifact**: `flow/trigger/sim-account-revenue-update-2026-03-14.md`
**Example**:
```
User: /flow:trigger
> What record change? Update on Account, revenue changed from 50000 to 100000, ownerid changed
> Registered automations found: 4 plugins, 3 flows, 2 business rules, 1 workflow
> Evaluation:
  | Automation | Type | Filter | Match | Order | Timing |
  |-----------|------|--------|-------|-------|--------|
  | RevenueValidation | Plugin (pre-op) | revenue changed | YES | Stage 20, order 1 | Sync |
  | TerritoryAssignment | Plugin (pre-op) | ownerid changed | YES | Stage 20, order 2 | Sync |
  | AuditTrail | Plugin (post-op) | any field | YES | Stage 40, order 1 | Sync |
  | ForecastAsync | Plugin (async) | revenue changed | YES | Stage 40, async | Async |
  | NotifyManager | Cloud flow | revenue changed | YES | N/A | Async post-commit |
  | UpdateForecast | Cloud flow | revenue changed, statecode=0 | YES | N/A | Async post-commit |
  | SyncToMarketing | Cloud flow | statuscode changed | NO | -- | -- |
  | RequireDescription | Business rule | revenue > 100000 | YES | Client + server | Sync |
  | ApprovalWorkflow | Workflow | revenue > 500000 | NO | -- | -- |
> Findings:
  P1: Two sync pre-op plugins at same stage -- order-dependent behavior
  P2: Two async flows both modify forecast -- potential last-writer-wins conflict
  P3: No automation for revenue=$0 edge case
```

---

### /flow:dataflow

**What**: Simulate data movement through an ETL/sync pipeline -- CDX distribution, subledger-to-GL posting, dual-write sync, or data entity import -- tracing transformations at each stage.
**Validated by**: Commerce (CDX -- 5/5 from backend and developer), Finance (subledger-to-GL -- 5/5 from backend and developer), Operations (dual-write, data entities -- 5/5 from backend and developer)
**Input**: Pipeline name or description (e.g., "CDX download job for product pricing"), source system, target system, and optionally a specific record to trace.
**Output**: Data flow trace artifact (per-stage: source schema, transformation, target schema, record count, latency, failure modes) with findings on data loss, transformation errors, and timing issues.
**Lifecycle**:
- Setup: Identify the pipeline (CDX download job 1040 -- Product Pricing). Source: F&O HQ (RetailChannelTable, RetailProductPrice). Target: Channel database (CSU). Scope: all active channel price groups for store "Houston-001". Select roles (Commerce Dev, Data Engineer).
- Execute: Trace the pipeline. Stage 1: HQ extracts price records from RetailProductPrice where PriceGroup in Houston-001's channel price groups -> 2,847 records. Stage 2: CDX serialization transforms records into the channel schema (flattens price tiers, converts currency, applies effective date filter) -> 2,611 records (236 filtered by effective date). Stage 3: CDX transport packages the data and pushes to the channel database via async job. Stage 4: Channel database applies the records, updating local price cache. Stage 5: CSU cache invalidation triggers POS to reload pricing on next transaction.
- Findings: P1: 236 records were filtered because their effective date is tomorrow -- but the store operates in a timezone 3 hours ahead of HQ. Prices that should be active at store opening (6 AM local) are not available until 9 AM local because the CDX job uses HQ timezone for effective date filtering. P2: No delta tracking on price group membership changes -- if a product is removed from a price group, the channel database retains the old price until a full sync. P3: Cache invalidation is fire-and-forget -- no confirmation that POS terminals actually reloaded.
- Amend: Commerce dev reviews: "CDX 1040 actually runs on a 15-minute schedule, and the timezone issue was fixed in 10.0.38 with store-local effective dates." Re-simulate with store-local dates: P1 resolved for current version. Dev confirms P2 is a known gap tracked in backlog.
**Lightweight**: --quick traces the pipeline as a linear flow diagram (source -> transform -> target) with record counts, no detailed transformation analysis.
**Artifact**: `flow/dataflow/sim-cdx-pricing-houston-2026-03-14.md`
**Example**:
```
User: /flow:dataflow
> What pipeline? CDX job 1040 -- Product Pricing to Houston-001 store
> Setup: Source=F&O HQ RetailProductPrice, Target=Houston-001 channel DB, Scope=active price groups
> Stage 1: Extract -> 2,847 records from 3 price groups
> Stage 2: Transform -> 2,611 records (236 filtered: effective date not yet active)
> Stage 3: Transport -> async package, 1.2 MB compressed, ETA 45 seconds
> Stage 4: Apply -> channel DB updated, 12 conflicts resolved (last-writer-wins)
> Stage 5: Cache invalidation -> 8 POS terminals notified, 0 confirmations received
> Findings:
  P1: Timezone mismatch -- effective date filter uses HQ timezone, store is UTC-6
  P2: No delta handling for price group membership removal
  P3: Cache invalidation is unconfirmed -- POS may serve stale prices for up to 15 minutes
```

---

### /flow:integration

**What**: Simulate a cross-system interaction through connectors, webhooks, service endpoints, or dual-write maps -- tracing the full path from source event to target system response.
**Validated by**: Connectors (5/5 backend and developer -- "I AM the integration boundary"), Operations (5/5 -- dual-write, data entities, business events), Automate (5/5 -- multi-connector flow execution)
**Input**: Integration description (e.g., "Dataverse Account update triggers dual-write sync to F&O Customer"), source event, and the expected outcome in the target system.
**Output**: Integration trace artifact (per-hop: system boundary, auth mechanism, payload transformation, response, latency, failure mode) with findings on auth failures, contract drift, and data loss.
**Lifecycle**:
- Setup: Identify the integration (dual-write: Account in Dataverse -> Customer V3 entity in F&O). Source event: Account record updated (name changed, revenue changed). Expected outcome: Customer V3 record in F&O reflects changes within 5 seconds. Select roles (Operations Dev, Integration Architect). Load the dual-write table map and field mappings.
- Execute: Trace hop by hop. Hop 1: Dataverse post-operation plugin fires "DualWriteSync" -> captures change set (Account.name, Account.revenue). Hop 2: Dual-write runtime evaluates table map "Account -> Customer V3" -> maps name to CustomerName, revenue to CreditLimit (custom mapping). Hop 3: Dual-write calls F&O OData endpoint PUT /data/CustomersV3('CUST-001') with mapped payload. Hop 4: F&O receives request, validates against entity schema, applies X++ chain of command extensions on CustomerEntity. Hop 5: F&O commits record, returns 200 OK with updated ETag. Hop 6: Dual-write runtime updates sync status in integration journal.
- Findings: P1: revenue -> CreditLimit mapping is a custom extension -- if the mapping is removed during a dual-write solution upgrade, revenue changes silently stop syncing to F&O. No alert on mapping removal. P2: F&O CustomerEntity has a chain of command extension that validates CreditLimit > 0 -- if Dataverse revenue is set to $0, the F&O extension throws, dual-write logs an error, and the sync enters a retry loop. P3: The 5-second SLA assumes F&O is responsive -- during batch processing windows (nightly MRP), F&O OData response times spike to 15-30 seconds, breaching the SLA.
- Amend: Operations dev reviews: "The CreditLimit > 0 validation was added for a specific customer segment. It should check the customer group first." Re-simulate with updated validation logic: Hop 4 now passes for revenue=$0 when CustomerGroup != 'Premium'. P2 partially resolved (still fails for Premium customers, which is correct business logic).
**Lightweight**: --quick traces the integration as a hop diagram (System A -> boundary -> System B) with auth type and expected latency per hop, no detailed payload analysis.
**Artifact**: `flow/integration/sim-dualwrite-account-customer-2026-03-14.md`
**Example**:
```
User: /flow:integration
> What integration? Dual-write: Dataverse Account -> F&O Customer V3
> Source event: Account update (name, revenue changed)
> Hop 1: Dataverse -> DualWriteSync plugin captures change set
> Hop 2: Dual-write runtime -> maps Account.name->CustomerName, Account.revenue->CreditLimit
> Hop 3: Dual-write -> PUT /data/CustomersV3('CUST-001') to F&O
> Hop 4: F&O -> entity validation, CoC extensions, commit
> Hop 5: F&O -> 200 OK, ETag updated
> Hop 6: Dual-write -> integration journal updated, sync status=success
> Total latency: 2.3 seconds (within 5-second SLA)
> Findings:
  P1: Custom field mapping (revenue->CreditLimit) not protected against solution upgrade
  P2: F&O validation rejects revenue=$0 -- dual-write enters retry loop
  P3: Batch processing window causes latency spikes to 15-30 seconds
```

---

### /flow:throttle

**What**: Simulate throughput behavior when multiple API consumers (flows, plugins, connectors) hit rate limits simultaneously -- model the cascade of 429 responses, retries, and backpressure.
**Validated by**: Connectors (throttle-cascade -- "the hardest debugging problem I face"), Automate (429 throttling risks across parallel branches), Dataverse (API protection limits)
**Input**: Set of API consumers with their call patterns (requests per minute), the target API's rate limits, and the concurrency/retry configuration for each consumer.
**Output**: Throughput simulation artifact (timeline of requests, 429 responses, retry attempts, effective throughput per consumer, and the bottleneck identification) with findings on cascading failures.
**Lifecycle**:
- Setup: Define consumers. Consumer 1: Power Automate flow "SyncAccounts" -- 200 records/batch, 5 concurrent threads, Dataverse connector retry=3 with exponential backoff. Consumer 2: Custom connector "EnrichmentAPI" -- 50 requests/minute, retry=2, linear backoff 5s. Consumer 3: Plugin "RealTimeValidation" -- fires on every Account create, ~20 creates/minute during import. Target: Dataverse API protection limits (6,000 requests per 5 minutes per user, 60,000 per org). Select roles (Connectors Dev, Platform Architect).
- Execute: Simulate minute-by-minute. Minute 1: SyncAccounts sends 200 requests (5 threads x 40/thread), EnrichmentAPI sends 50, Plugin sends 20. Total: 270 requests. Well within limits. Minute 2: SyncAccounts batch 2 starts while batch 1 retries 12 failed records. 200 + 12 retries + 50 + 20 = 282 requests. Still fine. Minute 5: Cumulative requests reach 1,350. SyncAccounts has generated 180 retries from transient errors. Effective request rate: 270 base + 36 retries/minute = 306/minute. At minute 17, cumulative 5-minute window hits 5,800 requests. By minute 19, the 5-minute rolling window exceeds 6,000 -- Dataverse returns 429 to all callers using the service account.
- Findings: P1: All three consumers share a single service account -- the 6,000/5-min per-user limit is the binding constraint. Separating the plugin onto a dedicated service principal would isolate real-time validation from batch operations. P2: SyncAccounts retry logic compounds the problem -- 180 retries in 5 minutes adds 30% to the request volume. Implementing circuit-breaker pattern (stop retrying after 3 consecutive 429s) would prevent cascade. P3: EnrichmentAPI has no backoff awareness of the Dataverse rate limit -- it retries at a fixed 5-second interval regardless of the Retry-After header value returned by Dataverse.
- Amend: Platform architect reviews: "The service account separation is already planned for Q2. Re-simulate with two service principals." Re-simulation: SyncAccounts + EnrichmentAPI on principal A (250/min), Plugin on principal B (20/min). Principal A never exceeds 6,000/5-min. P1 resolved.
**Lightweight**: --quick calculates aggregate request rate vs known limits and reports whether the system is within, near, or over the threshold -- no minute-by-minute simulation.
**Artifact**: `flow/throttle/sim-account-import-throttle-2026-03-14.md`
**Example**:
```
User: /flow:throttle
> Consumers: SyncAccounts flow (200 req/batch, 5 threads), EnrichmentAPI connector (50/min),
  RealTimeValidation plugin (20/min during import)
> Target: Dataverse API limits (6,000/5-min per user, 60,000/org)
> Minute-by-minute simulation:
  Min 1-4: 270 req/min, cumulative 1,080 -- OK
  Min 5-15: 306 req/min (retries compounding), cumulative 3,960 -- approaching limit
  Min 17: 5-min window = 5,800 -- WARNING
  Min 19: 5-min window = 6,120 -- 429 TRIGGERED for all callers on shared principal
  Min 20-25: cascade -- retries from all 3 consumers spike to 450 req/min
  Min 30: circuit breaker not implemented -- system oscillates between 429 and recovery
> Findings:
  P1: Shared service account -- user-level limit is binding constraint
  P2: No circuit breaker -- retries compound the overload
  P3: EnrichmentAPI ignores Retry-After header
```

---

### /flow:resilience

**What**: Simulate system behavior under degraded conditions -- network disconnection (POS offline), service unavailability (503), partial batch failure, and eventual consistency conflicts.
**Validated by**: Commerce (offline POS resilience -- "where our scariest bugs live"), Operations (dual-write conflict resolution), Customer Service (omnichannel session recovery)
**Input**: System description, the degradation scenario (e.g., "POS loses network for 45 minutes during peak hours"), and the expected recovery behavior.
**Output**: Resilience trace artifact (timeline of degradation, system behavior during outage, recovery sequence, data reconciliation) with findings on data loss, inconsistency, and recovery failures.
**Lifecycle**:
- Setup: Identify the system (Store Commerce POS at Houston-001). Define degradation: network connectivity lost at 11:15 AM (peak lunch rush), restored at 12:00 PM. Expected behavior: POS continues processing transactions offline, queues for upload on reconnect. Select roles (Commerce Dev, Store Operations SME). Load offline capability profile (which operations work offline, which don't).
- Execute: Simulate the timeline. 11:15 AM: Network drops. POS detects loss within 5 seconds, switches to offline mode. CRT switches to local channel database. 11:16-11:59 AM: 73 transactions processed offline. Local inventory decremented. Prices served from cached price list (last CDX sync: 10:45 AM). 11:32 AM: Customer attempts loyalty point redemption -- FAILS (loyalty service requires real-time HQ call). Cashier overrides with manual discount. 11:45 AM: Flash sale pricing activated in HQ at 11:30 AM -- POS is serving pre-sale prices (CDX job queued but not delivered). 12:00 PM: Network restored. POS begins upload: 73 transactions queued. 12:02 PM: Transaction 47 conflicts -- customer was refunded at another store during the outage, available refund amount now negative. Upload pauses on conflict. 12:05 PM: Remaining 72 transactions upload successfully. Transaction 47 flagged for manual resolution.
- Findings: P1: Flash sale pricing gap -- 30 minutes of transactions at wrong price ($2,340 in price differences across 18 affected transactions). No mechanism to retroactively apply correct pricing to offline transactions. P2: Loyalty redemption failure has no graceful fallback -- cashier had to manually calculate and apply a discount, which is not tracked as loyalty activity. Customer's loyalty balance is now incorrect. P3: Transaction 47 conflict halted the upload queue -- remaining transactions waited 3 minutes unnecessarily. Upload should continue with parallel conflict resolution.
- Amend: Commerce dev reviews: "The flash sale gap is a known limitation. The workaround is to schedule CDX push 30 minutes before sale activation. Re-simulate with a 10:45 AM pre-push." Re-simulation: CDX delivers flash sale prices at 11:00 AM, POS cache is current when network drops. P1 resolved (with operational workaround, not a code fix). Dev also notes: "Transaction 47 conflict resolution is new in 10.0.40 -- upload no longer blocks on conflicts." P3 resolved.
**Lightweight**: --quick identifies which operations work offline and which don't, without the full timeline simulation.
**Artifact**: `flow/resilience/sim-pos-offline-houston-2026-03-14.md`
**Example**:
```
User: /flow:resilience
> System: Store Commerce POS, Houston-001
> Scenario: Network loss 11:15 AM - 12:00 PM (45 min, peak hours)
> Timeline:
  11:15: Network drops -> offline mode activated (5s detection)
  11:16-11:59: 73 transactions processed offline, local DB only
  11:32: Loyalty redemption FAILS (requires real-time) -> manual override
  11:45: Flash sale prices not available (CDX queued, not delivered)
  12:00: Network restored -> upload begins (73 transactions)
  12:02: Transaction 47 conflicts (cross-store refund during outage) -> queue paused
  12:05: 72/73 uploaded, 1 flagged for manual resolution
> Findings:
  P1: 30-minute flash sale pricing gap -- $2,340 in incorrect prices
  P2: Loyalty fallback not tracked -- customer balance incorrect
  P3: Upload queue blocks on single conflict -- should process in parallel
```

## Roles

### Stock roles

Selection logic: /flow: skills auto-select roles based on the business domain detected in the process description. The system matches against Dynamics 365 product area keywords.

| Process keywords | Primary role | Secondary role |
|-----------------|-------------|----------------|
| Lead, Opportunity, Quote, Sales, BPF, Forecast | Sales Developer | CRM Admin |
| Invoice, GL, Posting, Period Close, Subledger | Finance Developer | Financial Controller |
| PO, Sales Order, Production, Warehouse, MRP | Operations Developer | Supply Chain Planner |
| POS, Cart, CDX, Channel, Storefront, Pricing | Commerce Developer | Store Operations SME |
| Case, SLA, Routing, Queue, Omnichannel | Customer Service Developer | Contact Center Manager |
| Flow, Trigger, Connector, Action, DLP | Automate Developer | Integration Architect |
| Agent, Topic, Knowledge, Conversation, Copilot | Copilot Studio Developer | Conversation Designer |

### Custom roles (optional)

All skills benefit from custom domain expert roles. For /flow:lifecycle, adding a business analyst role who knows the real-world process (not just the system implementation) catches gaps between business intent and system behavior. For /flow:resilience, adding a store operations manager who knows the physical workflow (cashier workarounds, customer expectations during outage) grounds the simulation in operational reality.

## Artifacts

```
flow/
  lifecycle/
    sim-{process-slug}-{date}.md        # e.g., sim-l2o-2026-03-14.md
  conversation/
    sim-{agent-slug}-{date}.md           # e.g., sim-contoso-returns-2026-03-14.md
  trigger/
    sim-{table}-{event}-{date}.md        # e.g., sim-account-revenue-update-2026-03-14.md
  dataflow/
    sim-{pipeline-slug}-{date}.md        # e.g., sim-cdx-pricing-houston-2026-03-14.md
  integration/
    sim-{integration-slug}-{date}.md     # e.g., sim-dualwrite-account-customer-2026-03-14.md
  throttle/
    sim-{workload-slug}-{date}.md        # e.g., sim-account-import-throttle-2026-03-14.md
  resilience/
    sim-{system}-{scenario-slug}-{date}.md  # e.g., sim-pos-offline-houston-2026-03-14.md
```

Naming convention: `sim-{descriptive-slug}-{YYYY-MM-DD}.md`. Slugs are lowercase, hyphenated, derived from the process/system being simulated.

## Technique Heritage

/flow: introduces new simulation techniques derived from Q01 user testing (domain process simulation). These are distinct from the existing hand-compilation and state-operation-outcome techniques because they operate at the business process level, not the compiler or SDK level.

| Skill | Primary technique | Evidence |
|-------|------------------|----------|
| lifecycle | Domain process simulation (new from Q01) | Q01 inv-a: Sales/Finance/Operations all requested document lifecycle tracing. Q01 inv-c: "document-flow" gap identified by 3 personas. |
| conversation | Conversational state machine simulation (new from Q01) | Q01 inv-a: Copilot Studio requested "conversation-flow." Q01 inv-b: "session-trace" gap from Customer Service. |
| trigger | Trigger evaluation simulation (new from Q01) | Q01 inv-a: Automate requested "trigger-evaluation." Q01 inv-c: Automate and Operations flagged trigger opacity. |
| dataflow | Adapted from 03 Three-Directory (input -> expected -> actual pattern applied to pipeline stages) | `simulate/techniques/03-three-directory/README.md`. Q01 inv-a: Commerce CDX, Finance subledger-to-GL, Operations dual-write. |
| integration | Adapted from 02 State-Operation-Outcome (state transitions across system boundaries) | `simulate/techniques/02-state-operation-outcome/README.md`. Q01 inv-a: Dataverse/Operations/Automate/Connectors all scored 5. |
| throttle | Throughput modeling (new from Q01) | Q01 inv-a: Connectors requested "throttle-cascade." Q01 inv-c: "cascading 429" identified as hardest debugging problem. |
| resilience | Degraded-mode simulation (new from Q01) | Q01 inv-a: Commerce requested "offline-resilience." Q01 inv-b: Commerce requested "offline-sync." |

## Cross-Namespace Integration

| /flow: output | Feeds into | How |
|--------------|-----------|-----|
| lifecycle findings | /review:design | Process findings (missing steps, exception gaps) become review items for the spec that defines the process. |
| lifecycle trace | /trace:state | The state transitions identified in a lifecycle simulation become the starting points for /trace:state to validate at the platform level. |
| conversation findings | /listen:feedback | Conversation flow issues (context loss, escalation triggers) become dimensions for customer persona feedback simulation. |
| trigger evaluation | /trace:request | The set of automations that fire on a record change defines the scope for a /trace:request simulation of the resulting execution. |
| dataflow findings | /trace:contract | Pipeline transformation issues (schema drift, missing fields) become contract test cases between systems. |
| integration trace | /trace:deployment | Integration mappings identified in /flow:integration become deployment validation targets -- did the mapping survive solution import? |
| throttle findings | /program:plan | Throttle limits and bottlenecks become capacity constraints in a /program:plan, gating the batch size or concurrency of planned operations. |
| resilience findings | /review:architecture | Degraded-mode gaps (missing fallbacks, data loss) become architectural review items for the resilience story. |
