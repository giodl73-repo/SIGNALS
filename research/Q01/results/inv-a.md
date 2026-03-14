# Experiment A: Backend Developer User Testing

## Protocol

Ten proposed Tier 3 simulation skills were tested against 9 backend developer personas from the Dynamics 365 and Power Platform ecosystem. Each persona's role file was read to understand their daily work, domain expertise, pain points, and mental model. For each persona, we adopted their perspective and answered: (1) which 3 skills they would reach for first and why, (2) what simulation they want that is not represented, (3) which skills overlap or confuse them, and (4) a 1-5 usefulness score for each skill against their daily work. Responses are written in the persona's voice.

### Skills Under Test

| # | Skill | Description |
|---|-------|-------------|
| 1 | `/simulate:request-trace` | Trace a request through service boundaries, APIs, middleware |
| 2 | `/simulate:state-validation` | Starting state -> operations -> expected outcome |
| 3 | `/simulate:contract-testing` | Expected vs actual output comparison |
| 4 | `/simulate:deployment-trace` | Trace what happens when you deploy, import, or migrate |
| 5 | `/simulate:plugin-chain` | Trace record operation through plugins, business rules, workflows |
| 6 | `/simulate:permission-walkthrough` | Trace who can do what through RBAC, security roles, teams |
| 7 | `/simulate:data-flow` | Trace data through ETL, pipelines, transformations |
| 8 | `/simulate:component-trace` | Trace user action through UI component tree, state, renders |
| 9 | `/simulate:migration-testing` | Expected vs actual after schema change, version upgrade |
| 10 | `/simulate:integration-trace` | Trace cross-system interaction through connectors, MCP, APIs |

---

## Results by Persona

### Backend: Dataverse

**Top 3**:
1. `/simulate:plugin-chain` -- "This is my bread and butter. I register plug-ins on pre-validation, pre-operation, post-operation. When a Create message fires on an account and three different plug-ins fire in sequence, I need to trace exactly what each stage does, what images are available, and whether an async plug-in downstream is going to break the chain. This skill maps directly to how I think about the pipeline."
2. `/simulate:request-trace` -- "Every Dataverse call starts as an OData HTTP request, hits the Web API layer, goes through the plug-in pipeline, hits Azure SQL or Cosmos DB depending on table type, and comes back. I debug these traces constantly -- especially when we get 429s from throttling or when batch requests fail partway through a changeset. Tracing the request through the API boundary into the storage tier is what I do."
3. `/simulate:integration-trace` -- "Service endpoints, webhooks, Event Hub, Service Bus -- I wire all of these. When a record changes in Dataverse and a message goes to Service Bus, I need to trace the full path: plug-in fires, service endpoint step triggers, message serializes as RemoteExecutionContext, hits the queue, consumer picks it up. Cross-system tracing is critical for my integration work."

**Missing**: "I want a `/simulate:storage-tier` skill -- something that lets me simulate what happens when I choose Standard Table vs Elastic Table for a workload. Show me the cost at $40/GB vs $2/GB, the query patterns that work and don't work (no joins on Cosmos), the partition behavior. Storage tier selection is a permanent decision and I get asked about it weekly."

**Overlap/Confusion**: "I see overlap between `request-trace` and `plugin-chain`. A Dataverse request IS a plug-in chain in many cases. The OData call triggers the message pipeline, which is the plug-in chain. If I use `request-trace` on a Dataverse Create operation, am I not already tracing the plug-in chain? The boundary between these two feels blurry for Dataverse-native work. Also, `component-trace` is UI -- I never touch UI code. That one is not for me."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Every OData call I debug |
| state-validation | 4 | Useful for testing plug-in pre/post image expectations |
| contract-testing | 4 | Validating OData response shapes, Custom API contracts |
| deployment-trace | 3 | Solution import matters but I don't own it daily |
| plugin-chain | 5 | Core of my daily work |
| permission-walkthrough | 3 | Security roles matter but security team owns this |
| data-flow | 4 | Change tracking, delta sync, CDX -- data movement is real |
| component-trace | 1 | I don't work on UI |
| migration-testing | 3 | Schema changes happen but are not frequent |
| integration-trace | 5 | Service endpoints, webhooks, Event Hub -- my integration layer |

---

### Backend: Sales

**Top 3**:
1. `/simulate:state-validation` -- "The sales process is all about state transitions. A lead moves from Open to Qualified via QualifyLead, which atomically creates an account, contact, and opportunity. An opportunity moves through BPF stages -- Qualify, Develop, Propose, Close -- with required fields gating each transition. I need to validate that the starting state (lead with BANT fields populated) produces the expected outcome (opportunity with correct probability and linked records). State validation is literally what the sales pipeline is."
2. `/simulate:plugin-chain` -- "We have plug-ins on lead qualification, opportunity close, and product line item calculations. When someone calls WinOpportunity, I need to trace through the plug-in chain to make sure actual revenue gets calculated, the forecast rollup updates, and the Exchange integration logs the activity. One bad plug-in registration can break the whole close process."
3. `/simulate:request-trace` -- "When a seller qualification call comes in -- POST to QualifyLead -- I need to trace what happens. It creates three records atomically, fires plug-ins on each, updates BPF stage, and may trigger a Sales Accelerator sequence. Tracing that full request path helps me debug the 'I qualified a lead but the opportunity didn't appear' support tickets."

**Missing**: "I want `/simulate:business-process` -- something that traces a BPF (Business Process Flow) end-to-end. BPFs are their own beast: they have stages, gates, required fields, branching paths. When a seller tries to advance from Propose to Close and gets blocked, I need to simulate what the BPF validation engine is checking. This is different from a plug-in chain -- BPFs are declarative configuration, not code."

**Overlap/Confusion**: "The `contract-testing` and `state-validation` skills feel very similar from my perspective. When I validate that QualifyLead with Status=3 creates the right records, am I doing state-validation or contract-testing? Both are 'expected vs actual' comparisons. I'd need clearer guidance on when to use which. Also `data-flow` vs `integration-trace` -- when forecast data flows to Power BI, is that a data flow or an integration? The line is fuzzy."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 4 | Debugging QualifyLead and WinOpportunity API calls |
| state-validation | 5 | Sales pipeline is pure state machine work |
| contract-testing | 3 | Overlaps with state-validation for my use cases |
| deployment-trace | 2 | Solution deployment is admin work for me |
| plugin-chain | 5 | Plug-ins on every sales message |
| permission-walkthrough | 3 | Sales territories and security matter but are configured once |
| data-flow | 3 | Forecast rollup is data flow, but niche |
| component-trace | 1 | Backend developer -- no UI work |
| migration-testing | 2 | Sales entities rarely change schema |
| integration-trace | 3 | Exchange/Teams integration matters but is mostly config |

---

### Backend: Commerce

**Top 3**:
1. `/simulate:request-trace` -- "Commerce Scale Unit is a headless REST API layer. Every POS transaction, every e-commerce checkout, every real-time HQ call goes through CSU. When a Store Commerce app calls the cart API and it has to do a real-time price check against HQ, I need to trace that full request: POS -> CSU REST endpoint -> CRT handler pipeline -> real-time service call to HQ -> X++ pricing engine -> response back. This is multi-hop, multi-runtime tracing and it's exactly what I debug daily."
2. `/simulate:deployment-trace` -- "Commerce deployments are complex. When I deploy a CSU extension package, it has to go through LCS, hit the right scale unit, update the CRT handler registrations, and the CDX jobs need to re-sync. One missed step and POS stops working in stores. I've had outages from deployment issues. Tracing what happens during a CSU deployment would save me hours."
3. `/simulate:data-flow` -- "CDX (Commerce Data Exchange) is literally a data distribution engine. Download jobs push pricing, products, and customers from HQ to channels. Upload jobs push transactions back. If a CDX job fails or runs in the wrong order -- say pricing updates haven't synced before a promotion starts -- customers see wrong prices at POS. Tracing data through the CDX pipeline is essential."

**Missing**: "I want `/simulate:offline-resilience` -- something that simulates what happens when the POS loses network connectivity. Store Commerce must keep working offline: cached product catalog, local transaction storage, eventual upload. I need to simulate the offline scenario end-to-end: what data is cached locally, what operations work without network, what happens when connectivity restores, how transactions reconcile. This is a Commerce-specific concern that none of these skills address."

**Overlap/Confusion**: "I'm confused about `plugin-chain` vs `request-trace` for my domain. CRT handlers ARE the Commerce equivalent of Dataverse plug-ins -- they're a request handler pipeline. But the skill name says 'plugins, business rules, workflows' which sounds Dataverse-specific. Would I use `plugin-chain` for CRT handlers or `request-trace`? The naming suggests Dataverse only. Also, `migration-testing` vs `deployment-trace` -- deploying a new CSU package IS a kind of migration. When do I use which?"

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | CSU API tracing is my primary debugging tool |
| state-validation | 3 | Cart state transitions matter but are secondary |
| contract-testing | 4 | CSU API response contracts must be validated |
| deployment-trace | 5 | CSU deployment is high-risk and complex |
| plugin-chain | 3 | CRT handlers are similar but the name is misleading |
| permission-walkthrough | 2 | Commerce security is mostly POS-role based, simpler |
| data-flow | 5 | CDX data distribution is critical daily work |
| component-trace | 2 | E-commerce React modules are somewhat relevant |
| migration-testing | 4 | CSU version upgrades are risky |
| integration-trace | 4 | Adyen payments, inventory visibility, recommendations |

---

### Backend: Customer Service

**Top 3**:
1. `/simulate:request-trace` -- "When a customer sends a message on live chat, it goes through Azure Communication Services, hits the omnichannel middleware, creates an `msdyn_ocliveworkitem` conversation record, triggers unified routing intake rules, matches to an agent based on skills and capacity, and routes to a queue. That's a six-hop request trace. When a case gets misrouted, I need to trace every hop to find where the routing decision went wrong."
2. `/simulate:permission-walkthrough` -- "Unified routing is deeply tied to security. Agents can only see cases in their queue. Capacity profiles limit how many cases they handle. Skill-based routing means an agent without the 'billing' skill never sees billing cases. When a manager says 'my agent can't see this case,' I need to walk through the full permission chain: security role, business unit, queue membership, capacity, skill match. This is daily work."
3. `/simulate:state-validation` -- "SLA timers are state machines. A case is created, the SLA KPI instance starts counting. The case goes to 'Customer Hold' status -- the timer pauses. It goes back to 'Active' -- the timer resumes. If it hits the warning threshold, an action fires. If it hits the failure threshold, it breaches. I need to simulate state transitions on cases and verify the SLA timer behaves correctly through each status change."

**Missing**: "I want `/simulate:sla-timeline` -- something that simulates the SLA clock through a case lifecycle. Given a case with Priority=High, created at 9:00 AM Monday, put on hold at 2:00 PM, resumed at 10:00 AM Tuesday, show me the elapsed business hours accounting for the business calendar, holidays, and pause/resume. SLA calculation bugs are the most common support tickets I get, and they're always about business hours math."

**Overlap/Confusion**: "The distinction between `request-trace` and `integration-trace` is unclear for omnichannel. When a Teams message comes in through Azure Communication Services and creates a case, is that a request trace or an integration trace? ACS is an external system (integration) but the request flows through our middleware (request trace). I'd probably try both and waste time figuring out which gives me the answer. Also `contract-testing` -- I test CloseIncident API responses, but that feels like it should be part of `state-validation` for my domain."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Omnichannel message routing is multi-hop tracing |
| state-validation | 5 | Case lifecycle + SLA timers are pure state machines |
| contract-testing | 3 | CloseIncident API contracts, but overlaps with state-validation |
| deployment-trace | 2 | Not my primary concern |
| plugin-chain | 4 | Plug-ins on case creation, routing intake rules |
| permission-walkthrough | 5 | Unified routing security is daily debugging |
| data-flow | 2 | Less relevant -- Customer Service is transactional, not ETL |
| component-trace | 2 | Agent workspace is UI but I'm backend |
| migration-testing | 2 | Schema changes are infrequent |
| integration-trace | 4 | ACS channels, Teams, IoT alerts -- external systems |

---

### Backend: Finance

**Top 3**:
1. `/simulate:data-flow` -- "Finance is data flow. A vendor invoice enters AP, flows through accounting distributions, gets posted to the subledger, transfers to GL with financial dimensions, and lands in the trial balance. Period close is a multi-step data transformation pipeline: foreign currency revaluation, then inventory close, then depreciation, then accruals, then consolidation. If any step in that pipeline is wrong or out of order, the financial statements are wrong. Tracing data through the posting pipeline is my core job."
2. `/simulate:state-validation` -- "Every financial document has a posting state. A purchase order goes from Draft to Confirmed to Received to Invoiced. Each transition has validation rules: you can't invoice without a product receipt, you can't confirm without budget check. And each transition creates subledger entries. I need to validate that a starting state (PO with lines, dimensions, posting profile) produces the correct GL entries after each state transition."
3. `/simulate:deployment-trace` -- "F&O deployments go through LCS -- deployable packages with X++ code, data entities, configurations. A bad deployment can break posting profiles, corrupt number sequences, or introduce dimension validation errors that aren't caught until month-end close. When we deploy a new posting profile configuration, I need to trace exactly what changes in the system and verify that existing transactions still post correctly."

**Missing**: "I want `/simulate:period-close` -- something that simulates a full month-end close sequence. Given the current state of open transactions, show me what happens when I run foreign currency revaluation, then inventory close, then depreciation, then accruals. What GL entries does each step create? Do they balance? What happens if I run them out of order? Period close is the highest-stakes operation in finance and there is no skill here that addresses it as a first-class concept."

**Overlap/Confusion**: "I find `data-flow` and `request-trace` confusing for finance. When a vendor invoice posts, is the subledger-to-GL transfer a 'data flow' or a 'request trace'? It's a transaction in the same system (not cross-system), it transforms data (subledger to GL), but it's also a platform operation with a specific execution path. I'd probably use `data-flow` but I'm not confident. Also, `contract-testing` and `state-validation` overlap -- validating that a PO confirmation produces the right GL entries is both a contract test and a state validation."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | OData entity calls, but finance is more about posting pipelines |
| state-validation | 5 | Document lifecycle validation is core finance work |
| contract-testing | 3 | Posting profile output validation, but overlaps with state-validation |
| deployment-trace | 4 | LCS deployments are high-risk for finance config |
| plugin-chain | 2 | F&O uses X++ chain of command, not Dataverse plug-ins |
| permission-walkthrough | 3 | Posting permission, period access control |
| data-flow | 5 | Subledger-to-GL, period close pipeline, consolidation |
| component-trace | 1 | No UI work |
| migration-testing | 4 | Schema changes in finance entities break posting |
| integration-trace | 3 | Dual-write sync, bank import |

---

### Backend: Operations (Supply Chain)

**Top 3**:
1. `/simulate:data-flow` -- "Supply chain is document flow. Procure-to-pay: requisition -> PO -> product receipt -> vendor invoice -> payment. Order-to-cash: quotation -> sales order -> packing slip -> invoice -> payment. Each step creates inventory transactions, financial postings, and dual-write syncs. When a product receipt doesn't update available inventory, I need to trace the data flow through inventory dimensions, posting logic, and the financial/physical update split. Data entities and staging tables add another transformation layer for imports."
2. `/simulate:integration-trace` -- "F&O talks to Dataverse via dual-write, to external systems via data entities and OData, to warehouses via the mobile app, and to business events via Service Bus. When dual-write sync fails on a customer record because of a conflict between F&O and Dataverse, I need to trace the full cross-system interaction: which table map, which direction, what conflict resolution policy, where in the integration journal the error landed. Cross-system tracing is daily debugging for me."
3. `/simulate:deployment-trace` -- "LCS deployments in supply chain are terrifying. A deployable package might include new data entity versions (V2 to V3), changed posting logic, updated number sequences. If I deploy a package that changes the SalesOrderHeaderV2 entity schema and there are active dual-write maps pointing at the old schema, everything breaks. I need to trace the deployment impact: what entities changed, what maps need updating, what batch jobs need restarting."

**Missing**: "I want `/simulate:document-flow` -- something that traces a complete business document lifecycle. Given a purchase order with 3 lines, simulate the full P2P flow: PO confirmation (what inventory transactions are created), product receipt (physical update, what dimensions are stamped), vendor invoice (financial update, what GL entries post), payment (bank transaction, cash impact). Each step has specific business rules and the entire chain must balance. None of these skills capture a multi-step business document lifecycle."

**Overlap/Confusion**: "The `data-flow` and `integration-trace` skills overlap heavily in my world. Dual-write IS data flow AND integration. When F&O inventory data syncs to Dataverse via a table map, is that `data-flow` (ETL pipeline) or `integration-trace` (cross-system connector)? I could argue either way. Also, `plugin-chain` is named for Dataverse -- F&O has chain of command extensions and business events, not plug-ins. I would skip `plugin-chain` because of the name even though the concept applies to my domain."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | OData data entity calls, but less central than data flow |
| state-validation | 4 | Document status transitions (PO confirmed, received, invoiced) |
| contract-testing | 3 | Data entity response validation |
| deployment-trace | 5 | LCS package deployment is high-risk |
| plugin-chain | 2 | Name implies Dataverse; F&O uses chain of command |
| permission-walkthrough | 2 | Less security complexity than other domains |
| data-flow | 5 | Supply chain IS data/document flow |
| component-trace | 1 | No UI work |
| migration-testing | 4 | Entity version upgrades (V2->V3) are real risk |
| integration-trace | 5 | Dual-write, data entities, business events |

---

### Backend: Power Automate

**Top 3**:
1. `/simulate:request-trace` -- "A cloud flow is a request pipeline. Trigger fires, enters the Logic Apps runtime, executes actions sequentially or in parallel branches, each action is an HTTP call to a connector, and the whole thing has concurrency, retry, and timeout behavior. When a flow fails on action 7 of 12, I need to trace the full request path: what trigger payload came in, what each action produced, where the failure occurred, what the retry behavior was. This is debugging cloud flows."
2. `/simulate:integration-trace` -- "Flows are integration glue. A typical flow connects Dataverse, SharePoint, Teams, and a custom connector in a single automation. When the Dataverse trigger fires, it calls a custom connector action, writes to SharePoint, and posts a Teams notification. If the custom connector returns a 429, I need to trace the cross-system interaction: Dataverse trigger -> connector call -> throttle response -> retry -> SharePoint write -> Teams post. Each connector has its own auth, throttling, and error behavior."
3. `/simulate:contract-testing` -- "Connector actions have typed contracts: input schemas and output schemas defined by OpenAPI. When a connector action returns a response that doesn't match the expected schema, the Parse JSON action downstream fails. I need to validate that the connector's actual output matches the expected contract. This is especially critical for custom connectors where the OpenAPI definition may drift from the actual API."

**Missing**: "I want `/simulate:trigger-evaluation` -- something that simulates which flows fire when a Dataverse record changes. I have 15 automated flows with Dataverse triggers on the same table. Each has different filter rows, select columns, and scope settings. When I update a record, which of those 15 flows actually fire? In what order? With what concurrency? Trigger evaluation is the most opaque part of Power Automate and there is nothing here that addresses it."

**Overlap/Confusion**: "The `request-trace` and `plugin-chain` skills confuse me. A Power Automate flow triggered by a Dataverse change IS part of the plug-in chain in a sense -- it runs as an async side effect of the record operation. But it's also a standalone request with its own execution trace. Do I trace the Dataverse operation (plugin-chain) or the flow execution (request-trace)? If the flow calls back into Dataverse, do I switch skills? Also, `data-flow` vs `integration-trace` -- a flow that moves data from SQL to SharePoint to Dataverse is both data movement and cross-system integration."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Flow execution tracing is core debugging |
| state-validation | 3 | Flow run states matter but are secondary |
| contract-testing | 5 | Connector schema validation is critical |
| deployment-trace | 3 | Solution deployment with connection references |
| plugin-chain | 2 | Flows aren't plug-ins, naming is confusing |
| permission-walkthrough | 3 | Connection auth, DLP policy -- relevant but niche |
| data-flow | 4 | Flows often move data between systems |
| component-trace | 1 | No UI |
| migration-testing | 2 | Flows rarely have schema migrations |
| integration-trace | 5 | Flows ARE integration -- multi-connector orchestration |

---

### Backend: Copilot Studio

**Top 3**:
1. `/simulate:request-trace` -- "When a user types a message in a Copilot Studio agent, here's what happens: message hits the agent runtime, trigger phrase matching selects a topic, the topic walks through nodes (question, condition, action, generative answers), action nodes call Power Automate flows or Custom APIs, knowledge retrieval does RAG against configured sources, and the response goes back. I need to trace this full path. When a topic produces the wrong answer, I need to see: which topic fired, which knowledge chunks were retrieved, which action was called, what it returned."
2. `/simulate:integration-trace` -- "An agent is a composition of integrations. Topic A calls a Power Automate flow that hits a custom connector. Topic B queries a Dataverse Custom API. Topic C retrieves knowledge from SharePoint. Each integration has its own auth (connection reference), its own error behavior, and its own DLP policy constraints. When an action fails silently in a conversation, I need to trace the cross-system interaction to find out if it's an auth issue, a DLP block, a throttle, or a bad connector response."
3. `/simulate:contract-testing` -- "Actions have typed input/output parameters. Power Automate flows called from topics must return specific output variables that map to topic variables. Custom APIs have typed request/response parameters. Knowledge RAG returns chunks with citations. I need to validate these contracts: does the flow actually return the variables the topic expects? Does the Custom API response match the schema the agent is wired to consume? Contract drift between the agent definition and the backend action is a common bug."

**Missing**: "I want `/simulate:conversation-flow` -- something that simulates a multi-turn conversation through an agent's topic graph. Given a user message, which topic activates? If the topic has a question node, what happens with different user responses? When does the agent redirect to another topic? When does it escalate? When does it fall back to generative answers? I need to simulate the conversational state machine -- topic selection, variable accumulation, redirect chains, escalation triggers. This is fundamentally different from a request trace; it's a conversation-level simulation."

**Overlap/Confusion**: "The `plugin-chain` skill name is misleading for my domain. Copilot Studio agents don't have plug-ins -- they have topics and actions. If I want to trace how a topic executes its nodes (message, question, condition, action, generative answers), is that `plugin-chain` or `request-trace`? The topic execution pipeline is conceptually similar to a plug-in pipeline but the terminology doesn't match. I'd avoid `plugin-chain` entirely because of the name. Also, `component-trace` mentions 'UI component tree' -- agent conversation UI is a tree of topic nodes with state, but the skill seems to be about frontend rendering, not conversation flows."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Agent runtime execution tracing |
| state-validation | 3 | Topic variable state, but secondary |
| contract-testing | 5 | Action I/O parameter contracts, knowledge RAG contracts |
| deployment-trace | 3 | Agent publishing + solution promotion |
| plugin-chain | 2 | Name is wrong for my domain |
| permission-walkthrough | 4 | DLP policies, auth modes, knowledge scoping |
| data-flow | 2 | Agents don't do ETL |
| component-trace | 2 | Agent conversation tree is a stretch |
| migration-testing | 2 | Agent schema changes are rare |
| integration-trace | 5 | Agents compose multiple external systems |

---

### Backend: Connectors

**Top 3**:
1. `/simulate:contract-testing` -- "This is my entire job. I write OpenAPI definitions for custom connectors, and the OpenAPI schema IS the contract. When the upstream API changes a response field from string to array, my connector's schema is wrong and every flow using it breaks. I need to validate that the OpenAPI definition matches the actual API behavior. Expected schema vs actual response -- that's contract-testing. I would use this skill daily."
2. `/simulate:integration-trace` -- "Custom connectors sit at the boundary between Power Platform and external systems. When a flow calls my connector, the request goes: flow action -> connector runtime -> auth injection (OAuth token, API key) -> outbound HTTP call -> external API -> response -> response transform (policy template) -> back to flow. If the auth token is expired, or the response transform strips a field, or the DLP policy blocks the connector, I need to trace the full path."
3. `/simulate:request-trace` -- "At the individual operation level, I need to trace a connector action call. The OpenAPI operation defines the request shape, the auth config adds headers, policy templates may transform the request or response, and the connector runtime handles retry/throttle. When an operation returns an unexpected error, tracing from the flow's action call through the connector runtime to the external API response is essential."

**Missing**: "I want `/simulate:throttle-cascade` -- something that simulates throttling behavior across a chain of connectors. When a flow hits my custom connector's rate limit (429), the runtime retries with backoff. But if the flow is calling three different connectors and two of them throttle simultaneously, the concurrency and retry behavior cascades. I need to simulate: given these connector throttle limits, this flow concurrency setting, and this trigger volume, what's the effective throughput? Where does the bottleneck land? Throttle cascading is the hardest debugging problem I face."

**Overlap/Confusion**: "The `request-trace` and `integration-trace` skills overlap significantly from a connector perspective. A connector action IS a request AND an integration. The connector is the integration boundary -- tracing a request through a connector is the same as tracing a cross-system integration. I'd pick one but I genuinely don't know which. Also, `data-flow` could apply to connectors that move bulk data (SQL connector, SharePoint list operations), but the skill description says 'ETL, pipelines, transformations' which sounds more like data engineering than connector operations."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 4 | Connector operation tracing |
| state-validation | 2 | Connectors are stateless |
| contract-testing | 5 | OpenAPI schema validation is my core job |
| deployment-trace | 3 | Connector certification and publishing |
| plugin-chain | 1 | Connectors have no plug-in concept |
| permission-walkthrough | 4 | DLP classification, auth types, gateway access |
| data-flow | 3 | Bulk data connectors only |
| component-trace | 1 | No UI |
| migration-testing | 3 | API version upgrades break connectors |
| integration-trace | 5 | Connectors ARE the integration boundary |

---

## Cross-Persona Synthesis

### Consensus Top Skills

| Rank | Skill | Avg Score | Top Scorer(s) | Why |
|------|-------|-----------|---------------|-----|
| 1 | `/simulate:request-trace` | 4.33 | Dataverse (5), Commerce (5), Customer Service (5), Automate (5), Copilot Studio (5) | Universal -- every persona traces requests through their platform's execution pipeline |
| 2 | `/simulate:integration-trace` | 4.22 | Dataverse (5), Operations (5), Automate (5), Copilot Studio (5), Connectors (5) | The D365/PP ecosystem is inherently multi-system; cross-boundary tracing is universal |
| 3 | `/simulate:state-validation` | 3.78 | Sales (5), Customer Service (5), Finance (5) | Business app personas live in state machines (pipeline stages, case lifecycle, document posting) |
| 4 | `/simulate:data-flow` | 3.67 | Commerce (5), Finance (5), Operations (5) | F&O-adjacent personas deal with data distribution (CDX, subledger posting, dual-write) |
| 5 | `/simulate:contract-testing` | 3.67 | Automate (5), Copilot Studio (5), Connectors (5) | Integration-heavy personas validate typed contracts between systems |

### Bottom Skills

| Rank | Skill | Avg Score | Why |
|------|-------|-----------|-----|
| 9 | `/simulate:component-trace` | 1.22 | Backend personas do not work on UI. Not a single persona scored this above 2. |
| 8 | `/simulate:plugin-chain` | 2.89 | Useful only for Dataverse/Sales/Customer Service. F&O, Automate, Copilot Studio, and Connectors personas find the name misleading or inapplicable. |

### Consensus Gaps

Five distinct gaps emerged across multiple personas:

1. **Business process / document lifecycle simulation** (requested by Sales, Finance, Operations) -- Tracing a multi-step business document through its full lifecycle: L2O conversion, P2P flow, period close sequence. These are multi-operation, multi-state business processes that span many API calls. Neither `request-trace` (single request) nor `state-validation` (single transition) captures the full lifecycle.

2. **Trigger evaluation simulation** (requested by Automate, implied by Copilot Studio) -- When a Dataverse record changes, which flows fire? Which topics activate? Trigger evaluation is opaque and causes cascading issues that no current skill addresses.

3. **Throttle/capacity simulation** (requested by Connectors, implied by Automate, Dataverse) -- Simulating throughput bottlenecks when multiple connectors, flows, or API consumers hit rate limits simultaneously. This is an operational concern that crosses individual request boundaries.

4. **Offline/resilience simulation** (requested by Commerce) -- Simulating disconnected operation, local caching, and eventual consistency for scenarios like POS offline mode. Relevant beyond Commerce to any eventually-consistent architecture.

5. **Conversation flow simulation** (requested by Copilot Studio) -- Simulating multi-turn conversation state machines: topic selection, variable accumulation, redirect chains, escalation. Distinct from request tracing because it operates at the conversation session level, not the individual message level.

### Redundancies Identified

1. **`request-trace` vs `plugin-chain`** -- 5 of 9 personas flagged this overlap. For Dataverse-native work, a request trace through the OData API IS the plug-in chain. For non-Dataverse personas (F&O, Automate, Connectors), `plugin-chain` is either inapplicable or misleadingly named. Consider merging `plugin-chain` into `request-trace` as a pipeline-detail mode, or renaming it to `/simulate:pipeline-trace` to be platform-neutral.

2. **`request-trace` vs `integration-trace`** -- 4 of 9 personas (Automate, Connectors, Customer Service, Commerce) noted overlap. A connector action is both a request and a cross-system integration. The distinction -- single-system execution path vs cross-system boundary -- is often unclear when the request itself crosses systems.

3. **`contract-testing` vs `state-validation`** -- 3 of 9 personas (Sales, Finance, Customer Service) found these overlapping. Both compare expected vs actual outcomes. The distinction -- schema/shape validation vs state transition validation -- is clear in theory but blurry in practice when you're validating that an API call produces the right state change with the right output shape.

4. **`data-flow` vs `integration-trace`** -- 3 of 9 personas (Operations, Automate, Sales) noted that data flowing between systems via dual-write, CDX, or connectors is both "data flow" and "integration." The ETL framing of `data-flow` doesn't capture real-time bidirectional sync patterns.

5. **`component-trace`** -- Not a redundancy but a misfit. 0 of 9 backend personas found this useful. This skill belongs in a frontend-developer persona set, not backend.

### Proposed New Skills

Based on gap analysis across all 9 personas:

1. **`/simulate:lifecycle-trace`** -- Trace a business document or entity through its complete multi-step lifecycle (L2O, P2P, O2C, case lifecycle, period close). Starting state + lifecycle definition -> expected state after each step + cumulative side effects (GL entries, inventory transactions, related records). Addresses the gap requested by Sales (BPF), Finance (period close), and Operations (document flow).

2. **`/simulate:trigger-evaluation`** -- Given a record change (table, columns changed, values), evaluate which automation triggers fire: Dataverse flows, plug-in registrations, business rules, workflows, agent topics. Show trigger filter evaluation, match/no-match reasoning, execution order, and concurrency. Addresses the gap requested by Automate and implied by Copilot Studio.

3. **`/simulate:throttle-cascade`** -- Given a set of API consumers (flows, plug-ins, connectors) with their throttle limits and a workload volume, simulate the throughput bottleneck: where 429s occur, how retries cascade, what the effective throughput is, and where the system backs up. Addresses the gap requested by Connectors and implied by Automate and Dataverse.

4. **`/simulate:conversation-trace`** -- Trace a multi-turn user conversation through a Copilot Studio agent's topic graph: topic activation, node execution, variable state accumulation, topic redirects, escalation triggers, generative answer fallback. Distinct from `request-trace` because it operates at the session level across multiple turns. Addresses the gap requested by Copilot Studio.

5. **`/simulate:resilience-scenario`** -- Simulate a system under degraded conditions: network disconnection (POS offline), service unavailability (429, 503), partial failure (batch with some items failing), eventual consistency (dual-write conflict). Show what works, what fails, and how recovery proceeds. Addresses the gap requested by Commerce and applicable to any distributed system persona.
