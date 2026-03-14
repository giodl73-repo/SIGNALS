# Experiment C: Developer Subrole User Testing (Workflow & Integration Heavy)

## Protocol

Ten proposed Tier 3 simulation skills were tested against 10 developer subroles from the craftworks role library. Each subrole file was read to understand the persona's daily work, pain points, and mental model. For each persona, the evaluator adopted that developer's perspective and answered: (1) which 3 skills they would reach for first and why, (2) what simulation they want that is not in the list, (3) which skills overlap or confuse them, and (4) a 1-5 usefulness score for each skill against their daily work.

The 10 skills under test:

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

Developer personas tested: Automate, Connectors, Copilot Studio, Power Apps, Dataverse, Sales, Commerce, Customer Service, Finance, Operations.

---

## Results by Persona

### Developer: Automate

**Top 3**:
1. `/simulate:request-trace` -- "This is my bread and butter. A cloud flow IS a request trace -- trigger fires, actions execute in sequence, connectors get called, error scopes catch failures. If I could trace a flow run from trigger through every action to completion or failure, that covers 80% of my debugging work."
2. `/simulate:plugin-chain` -- "When my flow writes to Dataverse, I need to know what plugins and business rules fire. I have had flows fail because a sync plugin threw an exception I did not expect. Tracing the record operation through the pipeline from my flow's perspective is critical."
3. `/simulate:state-validation` -- "Approval flows are all about state. Start with a record in 'Submitted' state, run the approval flow, expect 'Approved' or 'Rejected' state plus the approval history record plus the adaptive card response. If I could simulate that state progression, I would catch half my bugs before testing."

**Missing**: "I need a `/simulate:flow-execution` -- trace a cloud flow from trigger through every action, including branching logic (conditions, switch), parallel branches, Apply to Each loops, and scope-based error handling. The request-trace skill is close but it does not understand flow designer concepts like 'configure run after', sub-flows, or the scope try-catch-finally pattern. Flows are not generic request pipelines -- they have their own execution model with concurrency settings, trigger filtering, and expression evaluation."

**Overlap/Confusion**: "Request-trace and integration-trace feel like they overlap for my work. When my flow calls a connector, is that a request-trace or an integration-trace? Also, plugin-chain is relevant but I am usually on the calling side -- my flow triggers the plugin chain, I do not author the plugins. I want to see the chain from my flow's perspective, not from the plugin author's perspective."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Flow execution IS request tracing |
| state-validation | 4 | Approval flows, status transitions |
| contract-testing | 3 | Useful for connector response validation |
| deployment-trace | 4 | Solution import with connection references is painful |
| plugin-chain | 4 | Need to understand what fires when my flow writes |
| permission-walkthrough | 3 | Connection references and service principals matter |
| data-flow | 3 | Batch flows move data but this feels more ETL-oriented |
| component-trace | 2 | I build adaptive cards, not full UI components |
| migration-testing | 3 | Environment promotion breaks flows regularly |
| integration-trace | 4 | Flows are integration glue -- every flow is cross-system |

---

### Developer: Connectors

**Top 3**:
1. `/simulate:contract-testing` -- "This is literally what I do. My OpenAPI definition IS the contract. Expected schema versus actual API response -- if those diverge, every flow and app using my connector breaks at runtime. I would use this skill every single day."
2. `/simulate:request-trace` -- "Custom connectors are middleware. A request comes from a flow, hits my connector, goes through policy templates (transforms, rate limiting), hits the external API, response comes back through transforms. Tracing that path with auth headers, DLP classification checks, and throttle handling is exactly what I need."
3. `/simulate:integration-trace` -- "Connectors ARE the integration boundary. Tracing how a flow's connector call goes through auth (OAuth consent, token refresh), DLP policy evaluation, gateway routing (on-prem or VNet), and finally reaches the external system -- that is my entire job in one simulation."

**Missing**: "I need `/simulate:auth-flow` -- trace the full authentication lifecycle from OAuth consent through token acquisition, refresh token handling, managed identity resolution, and connection reference binding. Auth is the number one failure mode for connectors. When a connector breaks in production, 90% of the time it is an auth issue -- expired tokens, missing consent, wrong audience, service principal misconfiguration. None of the 10 skills focus on auth flows specifically."

**Overlap/Confusion**: "Request-trace and integration-trace overlap significantly for me. A connector request IS a cross-system integration. The distinction between 'tracing through service boundaries' and 'tracing cross-system interaction through connectors' is not meaningful when you ARE the connector. Also, contract-testing and state-validation could overlap -- validating that a connector response matches the OpenAPI schema is both a contract test and a state validation."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Connector is middleware -- this is the trace |
| state-validation | 3 | Connection state (active, expired, broken) matters |
| contract-testing | 5 | OpenAPI schema is THE contract |
| deployment-trace | 3 | Connector certification and deployment matters |
| plugin-chain | 2 | Connectors do not interact with the plugin pipeline |
| permission-walkthrough | 4 | DLP classification, connection sharing, consent flows |
| data-flow | 3 | Connectors move data but I care about the boundary, not the pipeline |
| component-trace | 2 | I define operation visibility metadata, not UI components |
| migration-testing | 3 | API version upgrades break connectors |
| integration-trace | 5 | I AM the integration layer |

---

### Developer: Copilot Studio

**Top 3**:
1. `/simulate:request-trace` -- "An agent conversation IS a request trace. User utterance triggers topic matching, trigger phrases evaluate, nodes execute in sequence -- message, question, condition, action, redirect. Each action node calls a flow or connector. I need to trace the entire conversation turn from utterance through topic resolution, node execution, action invocation, and response generation."
2. `/simulate:plugin-chain` -- "When my agent calls a Custom API action, it enters the Dataverse plugin pipeline. If the Custom API has pre/post plugins, business rules, or triggers other flows, I need to see that chain. Agent actions must be idempotent because the runtime retries on timeout -- tracing what actually happens on each invocation is essential."
3. `/simulate:state-validation` -- "Agent conversations are stateful. Topic variables, global variables, system variables -- they change as the conversation progresses through nodes. I need to simulate: starting state (user says X, global variable Y = Z), conversation flows through nodes, expected ending state (variable A = B, action was called, response was generated). This is how I validate topic logic."

**Missing**: "I need `/simulate:conversation-trace` -- trace a multi-turn agent conversation through topic matching, generative orchestration, knowledge retrieval (RAG), and action execution. The agent runtime does not work like a request pipeline. It has topic matching with trigger phrases, generative orchestration that decides WHICH topic to activate, knowledge grounding that retrieves and synthesizes from multiple sources, and fallback behavior when no topic matches. None of the 10 skills understand conversational AI patterns -- turn-taking, context carryover, disambiguation, escalation to human agent."

**Overlap/Confusion**: "Request-trace and component-trace both partially apply but neither fully fits. A topic is not a UI component -- it is a conversational flow with branching logic, variable scoping, and action side effects. The agent canvas is visual but it is not a component tree in the React sense. Also, plugin-chain is useful but only for the action execution part -- it does not cover topic matching, knowledge retrieval, or generative answers."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 4 | Conversation turns are request-like but more complex |
| state-validation | 5 | Topic variables, conversation state -- core concern |
| contract-testing | 3 | Action input/output contracts matter |
| deployment-trace | 4 | Agent publishing and channel deployment are tricky |
| plugin-chain | 4 | Custom API actions hit the plugin pipeline |
| permission-walkthrough | 4 | Agent auth, knowledge scoping, DLP on actions |
| data-flow | 2 | Knowledge retrieval is data-adjacent but not ETL |
| component-trace | 3 | Topic editor is visual but not a component tree |
| migration-testing | 3 | Agent schema changes across versions |
| integration-trace | 3 | Agent actions call connectors, but the core is conversation |

---

### Developer: Power Apps

**Top 3**:
1. `/simulate:state-validation` -- "Canvas apps are ALL about state. User taps a gallery item, form switches to Edit mode, user changes fields, SubmitForm writes to Dataverse, form resets. I need to simulate: starting state (screen loads, gallery items = X), user action (tap, type, select), expected state (form mode, variable values, data source state). This is how I catch delegation bugs and form mode errors."
2. `/simulate:component-trace` -- "Finally, a skill that speaks my language. User taps a button, it fires OnSelect, which calls UpdateContext, which triggers a gallery refresh, which calls Filter on a Dataverse table. Tracing that through the component tree -- screen, container, gallery, form, button -- with state changes at each level is exactly what I debug every day."
3. `/simulate:data-flow` -- "Delegation is a data flow problem. A formula like `Filter(Accounts, StartsWith(Name, SearchBox.Text))` pushes to the server. But `Filter(Accounts, Len(Name) > 5)` pulls all data client-side and truncates at 500 rows. Tracing where data goes -- server-side filter vs client-side collection -- is how I prevent delegation disasters."

**Missing**: "I need `/simulate:delegation-trace` -- trace a Power Fx formula through the delegation engine to show exactly what executes server-side vs client-side, what the row limit impact is, and what data the user actually sees vs what exists in the source. Delegation bugs are silent -- the app works perfectly with 100 records and silently drops data at 501 records. None of the 10 skills understand the delegation boundary, which is the single most important concept in canvas app development."

**Overlap/Confusion**: "Data-flow and request-trace overlap for my use case. When my app calls Concurrent(ClearCollect(...), ClearCollect(...)), that is both a data flow and a set of requests. Also, state-validation and component-trace overlap -- tracing a user action through components IS tracing state transitions. I would not know which to use for 'user taps Save button, form submits, gallery refreshes with new record' -- that is both a component trace and a state validation."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | Data source calls are requests but the app is formula-driven |
| state-validation | 5 | Form modes, variables, collections -- state is everything |
| contract-testing | 3 | Connector response schemas matter |
| deployment-trace | 3 | App publishing and solution import |
| plugin-chain | 3 | Dataverse writes trigger plugins from my app |
| permission-walkthrough | 3 | Data source permissions affect what galleries show |
| data-flow | 4 | Delegation = where data flows (server vs client) |
| component-trace | 5 | Screen -> container -> gallery -> form -> button = my world |
| migration-testing | 3 | App version upgrades, connector changes |
| integration-trace | 3 | Multi-connector apps exist but are not the core challenge |

---

### Developer: Dataverse

**Top 3**:
1. `/simulate:plugin-chain` -- "This is MY skill. A record operation enters the pipeline at pre-validation, flows through pre-operation, main operation, post-operation. Each stage can have sync or async plugins, business rules, flows. Tracing a Create or Update through the full pipeline with pre/post images, execution context, and exception handling is the most important simulation I could ever run."
2. `/simulate:request-trace` -- "Every OData Web API call is a request trace -- HTTP request hits the endpoint, auth is validated, the message enters the pipeline, plugins fire, response comes back. I need to trace $batch requests, $expand chains, and Custom API calls through the full stack from HTTP to Azure SQL and back."
3. `/simulate:state-validation` -- "Dataverse is a state machine. Records have statecode/statuscode. Business process flows have stages. Optimistic concurrency uses etag values. I need to simulate: starting state (record with statecode=0, statuscode=1), operation (Update with field changes), expected state (record with new values, audit trail entry, modified timestamps, triggered async jobs). This catches plugin registration errors before deployment."

**Missing**: "I need `/simulate:pipeline-trace` specifically for the Dataverse message pipeline. The plugin-chain skill is close but 'plugin chain' implies just plugins. The Dataverse pipeline includes: message processing, pre-validation plugins, pre-operation plugins, core operation (Azure SQL write), post-operation plugins, async plugins, service endpoint (Service Bus/Event Hub/webhook) delivery, and change tracking delta generation. I also want to trace what happens with Elastic Table writes (Cosmos DB path) vs Standard Table writes (Azure SQL path) -- the pipeline behaves differently for each storage tier."

**Overlap/Confusion**: "Plugin-chain and request-trace feel like they should be one skill for Dataverse work. Every request IS a plugin chain traversal. Also, contract-testing and state-validation overlap -- I validate that an OData response matches expected schema (contract) AND that the record state is correct (state). These are the same validation from two angles."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | OData API calls are my primary interface |
| state-validation | 5 | Record state, statecode/statuscode, concurrency |
| contract-testing | 4 | OData response schema validation |
| deployment-trace | 4 | Solution import, managed layers, component conflicts |
| plugin-chain | 5 | THE core Dataverse developer concern |
| permission-walkthrough | 5 | Security roles, teams, field-level security, BU scoping |
| data-flow | 4 | Change tracking, delta sync, Service Bus delivery |
| component-trace | 3 | PCF controls and form scripts have UI state |
| migration-testing | 4 | Schema changes, solution upgrades, managed layer conflicts |
| integration-trace | 4 | Dual-write, virtual entities, webhook delivery |

---

### Developer: Sales

**Top 3**:
1. `/simulate:state-validation` -- "The entire sales process is state transitions. Lead qualification converts a lead to opportunity + account + contact atomically via QualifyLead API. Opportunity stages progress through BPF gates with required fields. WinOpportunity and LoseOpportunity close the deal. I need to simulate every state transition with field validation, BPF enforcement, and revenue recalculation."
2. `/simulate:plugin-chain` -- "Sales entities are heavily customized. Every organization adds plugins to opportunity create, lead qualify, and quote generation. I need to trace what happens when a seller clicks 'Qualify' -- the QualifyLead message fires, plugins execute, account/contact/opportunity get created. If a plugin throws, I need to see where in the chain it failed."
3. `/simulate:request-trace` -- "Sales Accelerator sequences are automated workflows -- email steps, phone steps, task steps. Tracing a sequence execution through assignment rules, work list prioritization, and predictive scoring integration helps me understand why a seller sees what they see in their workspace."

**Missing**: "I need `/simulate:process-flow` -- trace a business process flow (BPF) from first stage to close. BPFs are unique to Dynamics 365 -- they have stages with gate conditions, required fields per stage, stage transitions that trigger server-side logic, and cross-entity traversal (lead BPF transitions to opportunity BPF). The plugin-chain skill does not understand BPF stage semantics. The state-validation skill is close but BPFs are more than state machines -- they are guided processes with UI rendering in the form header."

**Overlap/Confusion**: "State-validation and plugin-chain overlap when I am tracing a stage transition. Moving from 'Propose' to 'Close' is both a state change AND a plugin chain event. Which skill do I use? Also, request-trace feels generic for my domain -- I think in terms of sales processes (qualify, propose, close), not in terms of HTTP requests."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | API calls matter but I think in business process terms |
| state-validation | 5 | Sales IS state transitions -- lead to opportunity to close |
| contract-testing | 3 | Quote-to-order contract validation |
| deployment-trace | 3 | Solution deployment with sales customizations |
| plugin-chain | 5 | Heavily customized entities with deep plugin chains |
| permission-walkthrough | 4 | Territory-based access, hierarchy security |
| data-flow | 3 | Forecast rollup is data aggregation but not ETL |
| component-trace | 3 | Pipeline view, forecast dashboards have UI complexity |
| migration-testing | 3 | Sales process changes across upgrades |
| integration-trace | 4 | Exchange, Teams, LinkedIn Sales Navigator integrations |

---

### Developer: Commerce

**Top 3**:
1. `/simulate:request-trace` -- "Commerce Scale Unit is a headless API layer. Every POS transaction, every storefront checkout, every real-time operation to HQ goes through CSU APIs. Tracing a cart-add operation from POS UI through CSU REST API, through CRT request handlers, through the pricing engine, and back is my primary debugging workflow."
2. `/simulate:data-flow` -- "CDX (Commerce Data Exchange) is pure data flow -- download jobs push products and pricing from HQ to channels, upload jobs push transactions back. If a price is wrong at POS, I need to trace: was the price list updated in HQ? Did the CDX download job run? Did the channel database receive the update? This is ETL tracing for retail."
3. `/simulate:deployment-trace` -- "Commerce deployments are uniquely complex. You deploy a CSU package, an e-commerce module, a POS extension, and CRT handlers -- all independently. A deployment that works in dev can break in production because the CRT handler version does not match the CSU version. Tracing what happens during deployment across these components is critical."

**Missing**: "I need `/simulate:channel-sync` -- trace data consistency across retail channels. The core commerce question is: does the customer see the same price, same inventory, same promotion in-store and online? This requires tracing CDX job execution, pricing engine evaluation per channel, inventory visibility sync, and customer profile unification. None of the 10 skills understand multi-channel consistency -- data-flow is close but it does not understand the channel dimension."

**Overlap/Confusion**: "Request-trace and integration-trace overlap for POS-to-HQ real-time operations. A real-time inventory lookup from POS goes through CSU to HQ -- is that a request trace or an integration trace? Also, contract-testing and state-validation both apply to the pricing engine -- I need to verify that the pricing engine produces the correct output (contract) AND that the cart state reflects the correct totals (state)."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | CSU API calls are the primary interaction model |
| state-validation | 4 | Cart state, transaction state, offline sync state |
| contract-testing | 4 | CRT handler contracts, API response validation |
| deployment-trace | 5 | Multi-component deployment is uniquely complex |
| plugin-chain | 4 | CRT request handlers are a plugin-like pipeline |
| permission-walkthrough | 3 | POS roles, channel permissions |
| data-flow | 5 | CDX is pure ETL -- products, prices, transactions |
| component-trace | 4 | POS UI and storefront React modules |
| migration-testing | 4 | F&O version upgrades break CRT extensions |
| integration-trace | 4 | Payment providers, inventory visibility, loyalty |

---

### Developer: Customer Service

**Top 3**:
1. `/simulate:request-trace` -- "A case follows a lifecycle: creation (email-to-case, portal, API), classification, routing (unified routing with intake rules, workstreams, assignment rules, capacity checks, skill matching), agent work, resolution (CloseIncident). Tracing a case from creation through the routing engine to agent assignment is how I diagnose misrouted cases."
2. `/simulate:state-validation` -- "Cases have a strict lifecycle with SLA timers. When a case moves to 'On Hold', the SLA timer must pause. When it moves back to 'In Progress', the timer resumes. I need to simulate: case created (SLA starts), agent puts on hold (SLA pauses), customer responds (SLA resumes), agent resolves (CloseIncident, SLA stops). Any deviation is a service contract violation."
3. `/simulate:permission-walkthrough` -- "Unified routing assigns cases based on agent capacity, skills, and presence. Agents only see cases in their queues. Supervisors see all queues in their scope. Knowledge articles have their own access rules. I need to trace who can see what -- which agents get which cases, which knowledge articles are visible, which supervisor dashboards show which queues."

**Missing**: "I need `/simulate:routing-trace` -- trace a work item through the unified routing engine from intake rule evaluation through workstream classification, skill matching, capacity checking, agent presence evaluation, and final assignment. Unified routing is a sophisticated rules engine with fallback and overflow handling. None of the 10 skills understand routing semantics -- request-trace is close but routing is not a request pipeline, it is a matching and optimization problem."

**Overlap/Confusion**: "Request-trace and data-flow overlap for omnichannel scenarios. When a chat escalates from Copilot Studio bot to live agent, is that a request trace (conversation handoff) or a data flow (context transfer)? Also, state-validation covers SLA timer behavior but does not capture the timer-specific semantics of pause/resume/breach/warning thresholds."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Case lifecycle and routing are request pipelines |
| state-validation | 5 | SLA timers, case status, routing state |
| contract-testing | 3 | Omnichannel API response validation |
| deployment-trace | 3 | Omnichannel deployment with channel config |
| plugin-chain | 4 | Case entity customizations, business rules |
| permission-walkthrough | 5 | Routing, queue access, knowledge access |
| data-flow | 3 | Conversation transcripts, case data for reporting |
| component-trace | 3 | Agent workspace has complex UI but not my focus |
| migration-testing | 3 | Unified routing migration from classic queues |
| integration-trace | 4 | Copilot Studio escalation, Teams swarming |

---

### Developer: Finance

**Top 3**:
1. `/simulate:state-validation` -- "Finance is the domain where every state transition must balance to the penny. A vendor invoice starts as a draft, gets validated against purchase order, accounting distributions are generated (debit/credit), subledger journal is created, and finally posts to GL. Each step must produce exactly the right financial dimension combination, the right account, the right amount. If I could simulate that state chain with penny-level precision, I would catch posting errors before they become audit findings."
2. `/simulate:data-flow` -- "The subledger-to-GL flow is pure data transformation. Module transaction originates in AP/AR/inventory, generates accounting distributions, creates subledger journal entries, and posts to the general ledger with voucher trail. Period close is an orchestrated data flow: revaluation, reconciliation, inventory close, depreciation, accruals, consolidation, reporting. Tracing data through this pipeline is my core concern."
3. `/simulate:contract-testing` -- "Financial reports are contracts. The trial balance must tie to the GL. The P&L must match revenue minus expenses. The balance sheet must balance. If I change a posting profile or add a financial dimension, I need to verify that every downstream report still produces the correct output. Expected vs actual is literally how auditors work."

**Missing**: "I need `/simulate:posting-trace` -- trace a financial transaction from source document through accounting distributions, subledger journal, GL posting, and downstream financial reporting impact. Finance has a unique data architecture where every transaction must maintain debit/credit balance, dimension integrity, and audit trail. None of the 10 skills understand double-entry bookkeeping semantics, fiscal period boundaries, or the posting profile indirection layer."

**Overlap/Confusion**: "State-validation and data-flow overlap heavily for finance. A vendor invoice posting is both a state transition (draft -> posted) AND a data flow (AP -> subledger -> GL). Which do I use? Also, contract-testing and state-validation overlap -- verifying that the GL balance is correct after a posting is both contract testing (report = expected) and state validation (account balance = expected amount)."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 2 | F&O is not primarily API-driven from my perspective |
| state-validation | 5 | Every financial posting is a state transition |
| contract-testing | 5 | Financial reports are contracts with auditors |
| deployment-trace | 3 | LCS package deployment matters |
| plugin-chain | 3 | X++ event handlers exist but "plugin" is Dataverse language |
| permission-walkthrough | 4 | GL posting permissions, period access controls |
| data-flow | 5 | Subledger-to-GL is THE data flow |
| component-trace | 2 | F&O forms are transactional, not component-heavy |
| migration-testing | 4 | Fiscal year changes, chart of accounts restructuring |
| integration-trace | 3 | Dual-write for customer/vendor sync but not my core |

---

### Developer: Operations

**Top 3**:
1. `/simulate:data-flow` -- "Supply chain IS data flow. Procure-to-pay: purchase requisition -> purchase order -> product receipt -> vendor invoice -> payment. Order-to-cash: sales quotation -> sales order -> packing slip -> invoice -> payment. Plan-to-produce: demand forecast -> master planning -> planned orders -> production order -> report as finished. Each step transforms data and creates downstream documents. Tracing this flow is my entire job."
2. `/simulate:integration-trace` -- "F&O lives in an integration web. Dual-write syncs to Dataverse in real time. Data entities feed external systems via OData. Business events publish to Service Bus and Event Grid. Virtual entities let Dataverse read F&O data without copying. I need to trace cross-system interactions because every supply chain process touches multiple systems."
3. `/simulate:deployment-trace` -- "F&O deployments go through LCS: build a deployable package, apply to sandbox, database refresh from production, validate, then promote to production. A bad deployment can take down the entire supply chain. Tracing what happens during deployment -- which entities are affected, which batch jobs restart, which integrations reconnect -- is critical."

**Missing**: "I need `/simulate:document-flow` -- trace a business document (purchase order, sales order, production order) through its full lifecycle with all status transitions, related document generation, financial posting, and inventory impact. F&O is organized around document flows, not individual API calls or plugin chains. A purchase order goes through confirmation, receipt, invoicing -- each step creates new documents and triggers downstream processing. The data-flow skill is close but it does not understand document lifecycle semantics."

**Overlap/Confusion**: "Data-flow and integration-trace overlap for dual-write scenarios. When a sales order in F&O syncs to Dataverse via dual-write, is that data flow or integration? Also, deployment-trace and migration-testing overlap -- deploying a new package to F&O IS a migration that can break data entities and batch jobs. I would not know which skill to pick."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | OData entity calls matter but I think in document terms |
| state-validation | 4 | Document statuses, inventory transactions |
| contract-testing | 3 | Data entity response validation |
| deployment-trace | 5 | LCS deployment is high-stakes |
| plugin-chain | 3 | X++ event handlers but different terminology |
| permission-walkthrough | 3 | Security roles, duty-privilege hierarchy |
| data-flow | 5 | Supply chain = document flow = data flow |
| component-trace | 2 | F&O forms follow rigid patterns, not components |
| migration-testing | 4 | Entity version upgrades, schema changes |
| integration-trace | 5 | Dual-write, data entities, business events |

---

## Cross-Persona Synthesis

### Consensus Top Skills

| Rank | Skill | Avg Score | Personas Rating 5 |
|------|-------|-----------|-------------------|
| 1 | `/simulate:state-validation` | 4.4 | 6 (Automate 4, PowerApps 5, Dataverse 5, Sales 5, CustServ 5, Finance 5) |
| 2 | `/simulate:request-trace` | 4.0 | 5 (Automate 5, Connectors 5, Commerce 5, CustServ 5, Dataverse 5) |
| 3 | `/simulate:data-flow` | 3.7 | 3 (Commerce 5, Finance 5, Operations 5) |
| 4 | `/simulate:plugin-chain` | 3.7 | 2 (Dataverse 5, Sales 5) |
| 5 | `/simulate:deployment-trace` | 3.7 | 2 (Commerce 5, Operations 5) |
| 6 | `/simulate:integration-trace` | 3.9 | 2 (Connectors 5, Operations 5) |
| 7 | `/simulate:permission-walkthrough` | 3.8 | 2 (Dataverse 5, CustServ 5) |
| 8 | `/simulate:contract-testing` | 3.6 | 2 (Connectors 5, Finance 5) |
| 9 | `/simulate:component-trace` | 2.9 | 1 (PowerApps 5) |
| 10 | `/simulate:migration-testing` | 3.4 | 0 (max 4 from multiple personas) |

**State-validation is the consensus winner** -- 6 of 10 personas rated it 4 or 5. Every workflow-heavy and integration-heavy developer thinks in terms of state transitions, whether it is case lifecycle, sales pipeline stages, financial postings, or flow execution outcomes.

**Request-trace is the universal second choice** -- every persona can map their work to "trace a request through the system," but several noted it is too generic for their domain-specific tracing needs.

### Consensus Gaps

Every persona identified a domain-specific simulation gap. The gaps cluster into three categories:

**1. Domain-specific execution models** (5 personas):
- Automate: flow execution with branching, scopes, concurrency
- Copilot Studio: multi-turn conversation with topic matching, RAG, orchestration
- Sales: business process flow (BPF) stage traversal with gate conditions
- Finance: financial posting with double-entry, dimension integrity, audit trail
- Operations: document lifecycle with status transitions and downstream generation

**2. Specialized tracing patterns** (3 personas):
- Connectors: authentication lifecycle (OAuth, tokens, managed identity)
- Customer Service: routing engine (intake rules, skill matching, capacity, overflow)
- Commerce: cross-channel consistency (same price/inventory/promotion everywhere)

**3. Platform-specific pipeline variants** (2 personas):
- Dataverse: full message pipeline (not just plugins -- includes service endpoints, change tracking)
- Power Apps: delegation boundary tracing (server-side vs client-side formula evaluation)

### Redundancies Identified

Three pairs of skills were flagged as confusing or overlapping by multiple personas:

| Overlap Pair | Flagged By | Nature of Confusion |
|-------------|-----------|-------------------|
| `request-trace` vs `integration-trace` | Automate, Connectors, Commerce, Operations | Both trace requests across system boundaries -- the distinction is unclear |
| `state-validation` vs `contract-testing` | Connectors, Dataverse, Finance | Validating expected output IS validating expected state |
| `deployment-trace` vs `migration-testing` | Operations, Commerce | Deploying a new version IS a migration |

The `request-trace` / `integration-trace` overlap is the most severe. 4 of 10 personas could not distinguish between them. The difference ("within a system" vs "across systems") breaks down for workflow developers because their systems ARE integrations.

### Proposed New Skills

Based on the consensus gaps, 6 new skills are proposed:

| Proposed Skill | Source Personas | Description |
|----------------|----------------|-------------|
| `/simulate:flow-execution` | Automate | Trace a cloud flow from trigger through actions, branches, scopes, and error handling with flow-specific semantics (concurrency, configure-run-after, sub-flows) |
| `/simulate:conversation-trace` | Copilot Studio | Trace a multi-turn agent conversation through topic matching, generative orchestration, knowledge retrieval, action execution, and channel delivery |
| `/simulate:auth-flow` | Connectors | Trace authentication lifecycle from consent through token acquisition, refresh, managed identity resolution, and connection reference binding |
| `/simulate:routing-trace` | Customer Service | Trace a work item through intake rules, workstream classification, skill matching, capacity checking, and agent assignment with overflow handling |
| `/simulate:document-flow` | Operations, Sales, Finance | Trace a business document through its full lifecycle with status transitions, related document generation, financial posting, and downstream impact |
| `/simulate:channel-sync` | Commerce | Trace data consistency across retail channels -- pricing, inventory, promotions, and customer profiles across POS and storefront |

The `/simulate:document-flow` skill has the broadest appeal -- Operations, Sales, and Finance all think in terms of document lifecycles rather than individual API calls or plugin chains.

### Workflow/Integration Specific Findings

**1. Workflow developers think in domain processes, not system primitives.**

Code-heavy developers (Dataverse, Connectors) naturally map to request-trace and plugin-chain because they work at the system primitive level. Workflow-heavy developers (Sales, Finance, Operations, Customer Service) think in terms of business processes: "qualify a lead," "close a period," "route a case." They struggle to map their domain processes onto generic system-level tracing skills.

**Implication**: Tier 3 skills should include domain-process-aware variants, not just system-primitive-aware variants. A `/simulate:document-flow` that understands "purchase order confirmation triggers product receipt which triggers vendor invoice" is more useful to an Operations developer than a generic `/simulate:data-flow`.

**2. Integration developers need auth tracing as a first-class concern.**

The Connectors persona rated auth as the #1 missing skill. Automate and Copilot Studio also flagged connection references and authentication as pain points. Authentication failures are the most common integration failure mode, yet none of the 10 proposed skills explicitly address auth flows.

**Implication**: Either add `/simulate:auth-flow` as a dedicated skill or ensure that `request-trace` and `integration-trace` have explicit auth-lifecycle tracing built in.

**3. The request-trace / integration-trace distinction does not hold for this audience.**

For workflow and integration developers, every request crosses system boundaries. A Power Automate flow calling a Dataverse action is simultaneously a request trace, an integration trace, and a plugin chain. The 10-skill taxonomy assumes clear boundaries between "within a system" and "across systems," but these developers live on the boundary.

**Implication**: Consider merging `request-trace` and `integration-trace` into a single skill that can zoom in (single service boundary) or zoom out (cross-system), or redefine the boundary more precisely. The current split causes more confusion than clarity.

**4. State-validation is universally valuable because every domain has lifecycle semantics.**

State-validation scored highest because leads have statuses, cases have SLA timers, invoices have posting states, flows have run outcomes, POS transactions have completion states. This is the one skill that naturally maps to every workflow developer's mental model.

**Implication**: State-validation should be the anchor skill in Tier 3. It may benefit from domain-aware variants (financial state validation with debit/credit balance, sales state validation with BPF stage gates) or a rich parameter model that accepts domain-specific state schemas.

**5. Component-trace scored lowest because workflow developers do not build UIs.**

Only the Power Apps persona rated component-trace at 5. Every other persona rated it 2-3. Workflow and integration developers build backend processes, configure routing, design flows, and wire integrations. They occasionally touch forms and views but do not think in terms of UI component trees.

**Implication**: Component-trace is a valid skill for frontend-heavy developers (Power Apps, PCF control authors, e-commerce storefront developers) but should not be positioned as a general-purpose simulation skill for the workflow/integration audience.
