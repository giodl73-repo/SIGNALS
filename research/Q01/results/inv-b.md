# Experiment B: Frontend Developer User Testing

## Protocol

Ten proposed Tier 3 simulation skills were user-tested against 9 frontend developer personas from the Dynamics 365 and Power Platform ecosystem. Each persona role file was read to understand their daily work, pain points, and mental model. For each persona, the tester adopted that perspective and answered: (1) which 3 skills they would use first and why, (2) what simulation is missing, (3) which skills overlap or confuse them, and (4) a 1-5 usefulness score for each skill against their daily work.

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

### Frontend: Sales

**Top 3**:
1. **`/simulate:component-trace`** -- "I spend my day in opportunity forms and pipeline Kanban views. When a seller drags a deal to the next stage and something doesn't update, I need to trace through the form event, the BPF stage transition, and whatever renders next. This is my bread and butter."
2. **`/simulate:plugin-chain`** -- "Opportunity records are the most customized entity in Sales. Every org has plugins that fire on opportunity update -- recalculating forecast rollups, triggering notifications, locking fields. When a seller reports 'the form froze when I moved the deal to Propose,' I need to see what plugins ran."
3. **`/simulate:state-validation`** -- "Pipeline views depend on opportunity stage, estimated close date, estimated revenue. I need to validate that after a BPF stage transition, the expected fields are set, the pipeline view reflects the new position, and the forecast dashboard rolls up correctly. Starting state -> operation -> expected outcome is exactly how I think about it."

**Missing**: "I want a `/simulate:form-lifecycle` -- trace what happens when a model-driven form loads, including which tabs render, which business rules fire, which fields become visible/required at each BPF stage, and how quick views resolve. The form load sequence in Sales is where 80% of my bugs live."

**Overlap/Confusion**: "I see overlap between `request-trace` and `integration-trace`. From my seat in the Sales app, I don't think about 'service boundaries' or 'connectors' -- I think about what happens when the seller clicks Save. Both of those sound like backend concerns to me. Also, `contract-testing` and `state-validation` feel like the same thing worded differently -- both are 'did I get what I expected?'"

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 2 | I rarely trace HTTP calls; I'm in Unified Interface |
| state-validation | 5 | Core to validating BPF transitions and forecast rollups |
| contract-testing | 3 | Useful for API testing but not my primary surface |
| deployment-trace | 3 | Matters at solution import time, not daily |
| plugin-chain | 5 | Critical -- plugins on opportunity are my top debugging target |
| permission-walkthrough | 3 | Relevant when sellers can't see pipeline views, but not daily |
| data-flow | 2 | Forecast rollups are data flow, but I think about them as state |
| component-trace | 5 | This is literally my job -- trace user actions through UI components |
| migration-testing | 2 | Rare -- only during major upgrades |
| integration-trace | 2 | Sales integrations are usually connector-based, not my layer |

---

### Frontend: Commerce

**Top 3**:
1. **`/simulate:component-trace`** -- "I work on two separate frontend stacks: POS (touch-optimized transaction terminal) and e-commerce storefront (React SDK modules). In both cases, I need to trace a user action -- scanning an item, adding to cart, clicking checkout -- through the component tree to see what renders and when. This is my daily debugging tool."
2. **`/simulate:request-trace`** -- "The e-commerce storefront makes data action calls to Commerce Scale Unit APIs. When product pages load slowly or cart operations fail, I need to trace from the React component through the data action to the CSU endpoint and back. POS does the same against Retail Server. This is real for me."
3. **`/simulate:contract-testing`** -- "POS and storefront must show the same prices, promotions, and product data. When they diverge, it's a business integrity failure, not just a bug. I need to validate that the same product query returns the same pricing on both channels. Expected vs actual comparison across channels is critical."

**Missing**: "I need `/simulate:offline-sync` -- trace what happens when POS goes offline, transactions queue locally in the CRT offline database, and then reconnect triggers sync. I need to see: which transactions are pending, what happens on conflict, do I get duplicates? Offline mode is where our scariest bugs live."

**Overlap/Confusion**: "The `plugin-chain` skill talks about 'plugins, business rules, workflows' -- that's Dataverse language. In Commerce, we have Commerce Runtime (CRT) handlers and request pipelines. I'd use `plugin-chain` conceptually but the name makes me think it's Dataverse-only. Also, `data-flow` and `request-trace` overlap for me: tracing a product lookup through the storefront IS a data flow AND a request trace."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | CSU API calls from both POS and storefront -- this is core |
| state-validation | 4 | Cart state after operations (add, discount, void) must be correct |
| contract-testing | 5 | Cross-channel price/promotion consistency is non-negotiable |
| deployment-trace | 4 | CSU deployment, POS app updates, storefront publish -- all matter |
| plugin-chain | 3 | CRT handlers are conceptually similar but naming is confusing |
| permission-walkthrough | 2 | POS has roles but it's not my main concern |
| data-flow | 3 | Product data from HQ to channels, but I think of it as sync |
| component-trace | 5 | Both POS UI and React storefront -- this is my world |
| migration-testing | 4 | Commerce version upgrades break POS/CSU compatibility regularly |
| integration-trace | 3 | ERP-to-Commerce sync is important but more backend |

---

### Frontend: Power Apps (Canvas)

**Top 3**:
1. **`/simulate:data-flow`** -- "Canvas apps are all about data flow. My daily headache is delegation -- when does the filter push to the server vs pull all rows to the client? I need to trace how data flows from Dataverse (or SharePoint, or SQL) through my Filter/Sort/LookUp formulas, into galleries, and out through Patch/Collect. If I can't trace that flow, I can't fix delegation bugs."
2. **`/simulate:component-trace`** -- "I build component libraries with custom properties, behavior properties, output properties. When a screen hosts my component and the user interacts with it, I need to trace: did the input property propagate? Did the behavior property fire? Did the output property update? Component debugging in canvas apps is painful without tracing."
3. **`/simulate:state-validation`** -- "Canvas app state is scattered: global variables (Set), context variables (UpdateContext), collections (Collect), and named formulas. After a sequence of user actions, I need to validate that all these state containers hold the expected values. This is how I catch the bugs where Screen2 shows stale data because Screen1 forgot to ClearCollect."

**Missing**: "I desperately need `/simulate:formula-evaluation` -- trace how a Power Fx formula evaluates step by step, including delegation boundaries. Show me: this Filter is delegable, this nested CountRows is not, so the result is truncated at 500 rows. The delegation boundary is the invisible wall in canvas apps and no tool traces it."

**Overlap/Confusion**: "I don't see much overlap from my perspective, but several skills feel irrelevant. `plugin-chain` is Dataverse backend -- I'm on the canvas side. `deployment-trace` sounds like solution import, which matters but isn't what I debug daily. `permission-walkthrough` -- canvas apps have app sharing, not RBAC in the traditional sense. The names feel oriented toward server-side developers."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | Useful for tracing connector calls, but I think in formulas |
| state-validation | 5 | Global/context/collection state validation is critical |
| contract-testing | 3 | Useful for connector response shapes, not daily |
| deployment-trace | 2 | Solution import is IT admin work, not mine |
| plugin-chain | 1 | I'm canvas-side, not server-side |
| permission-walkthrough | 2 | App sharing is simpler than RBAC -- not my pain point |
| data-flow | 5 | Delegation tracing IS data flow tracing -- this is my #1 need |
| component-trace | 5 | Component library debugging is where I spend my time |
| migration-testing | 2 | Canvas apps don't really have schema migrations |
| integration-trace | 3 | Multi-connector apps need this but it's not daily |

---

### Frontend: Copilot Studio

**Top 3**:
1. **`/simulate:request-trace`** -- "When a user sends a message to my agent, it goes through the orchestrator, hits knowledge sources, maybe calls a plugin action or Power Automate flow, and comes back with a response. I need to trace that full request path to understand why my agent gave a wrong answer or took too long. This is my #1 debugging need."
2. **`/simulate:component-trace`** -- "The topic editor is a visual node graph -- trigger, question, condition, action, message, redirect. When a conversation takes an unexpected path, I need to trace through the node tree: which condition branch was taken, which variable was set, which redirect fired. Tracing through my component tree (topics are components) is essential."
3. **`/simulate:contract-testing`** -- "I set up knowledge sources and expect the agent to return grounded answers. But does it? I need expected vs actual: given this user utterance and this knowledge base, did the agent return the correct grounded response? This is exactly contract testing -- expected input, expected output, actual output."

**Missing**: "I need `/simulate:conversation-flow` -- trace a multi-turn conversation through topic triggers, variable scoping (topic vs global vs system), and context handoffs. My bugs aren't single-request failures -- they're multi-turn failures where the agent loses context at turn 3 because a topic variable went out of scope. Single-request tracing doesn't capture this."

**Overlap/Confusion**: "The `plugin-chain` skill sounds like Dataverse plugins, but Copilot Studio has 'plugin actions' which are different. I'd be confused about whether this skill applies to my world. The `integration-trace` skill also overlaps with `request-trace` for me -- when my agent calls an external API via a plugin action, is that a request trace or an integration trace? I'd pick one and not know why the other exists."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Core -- trace user message through orchestrator to response |
| state-validation | 4 | Validate conversation state (variables) after each turn |
| contract-testing | 5 | Knowledge grounding verification is contract testing |
| deployment-trace | 3 | Publishing to channels matters, but authoring is my focus |
| plugin-chain | 2 | Name suggests Dataverse, confusing for Copilot Studio actions |
| permission-walkthrough | 2 | Channel auth is relevant but not my daily concern |
| data-flow | 3 | Knowledge source data flow matters but it's a subset of request-trace for me |
| component-trace | 5 | Topic node tree tracing is exactly component tracing |
| migration-testing | 1 | Not applicable to my world |
| integration-trace | 3 | Overlaps with request-trace for plugin action calls |

---

### Frontend: Dataverse (Model-Driven Apps)

**Top 3**:
1. **`/simulate:plugin-chain`** -- "This is literally what I debug. A user saves a record, and a chain of plugins fire -- synchronous pre-validation, pre-operation, post-operation, then async workflows. When the form hangs on save or a business rule conflicts with a plugin, I need to see the full execution chain. This skill was designed for me."
2. **`/simulate:component-trace`** -- "Model-driven app forms have tabs, sections, business rules, PCF controls, and form scripts all interacting. When a user clicks a field and three things change (another field becomes required, a tab becomes visible, a PCF control re-renders), I need to trace through that component hierarchy."
3. **`/simulate:permission-walkthrough`** -- "Security roles, field-level security, team privileges, business unit hierarchies -- this is the permission model I live in. When a user reports 'I can't see the Notes tab' or 'I can't edit the Status field,' I trace through RBAC to find out which privilege is missing. This is easily a weekly activity."

**Missing**: "I want `/simulate:form-event-chain` -- trace the sequence of events when a form loads or a field changes: OnLoad handlers, business rule evaluation order, attribute onChange handlers, and the resulting show/hide/require/lock actions. Business rules and scripts can conflict, and there's no way to see the combined effect without mental simulation."

**Overlap/Confusion**: "I struggle with the difference between `state-validation` and `contract-testing`. For me, checking that a record has the right field values after a plugin chain IS state validation, but comparing what my API returns vs what I expected IS contract testing. The line between them is blurry. Also, `request-trace` and `plugin-chain` overlap significantly -- a Dataverse save IS a request that goes through a plugin chain."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | Dataverse API calls matter but I think at the record/plugin level |
| state-validation | 4 | Record state after plugin chain execution |
| contract-testing | 3 | Web API response validation -- useful but not daily |
| deployment-trace | 4 | Solution import/export is a regular pain point |
| plugin-chain | 5 | My #1 skill -- this is what I debug most |
| permission-walkthrough | 5 | Security role debugging is weekly work |
| data-flow | 3 | Data import/migration flows, but not my primary concern |
| component-trace | 5 | Form + PCF + business rule interaction tracing |
| migration-testing | 4 | Solution upgrades break customizations regularly |
| integration-trace | 3 | Dataverse connectors exist but are more backend |

---

### Frontend: Customer Service

**Top 3**:
1. **`/simulate:component-trace`** -- "The agent workspace is a multisession app with case forms, omnichannel widget, knowledge sidebar, activity timeline, and SLA timers all on screen simultaneously. When an agent reports 'the knowledge sidebar didn't update when I switched cases,' I need to trace through the session/tab switching, the case context propagation, and the sidebar re-render. This is a complex component tree."
2. **`/simulate:request-trace`** -- "Omnichannel routing is a real-time system. When a chat comes in, it goes through routing rules, skills matching, queue assignment, and lands on an agent's screen. When routing sends a chat to the wrong agent or takes too long, I need to trace that request end-to-end. Same for knowledge search -- the request goes from sidebar to knowledge service and back."
3. **`/simulate:plugin-chain`** -- "Case creation and escalation trigger a chain of plugins and workflows: SLA timer start, entitlement validation, auto-routing, notification, and record creation. When an SLA timer doesn't start or an entitlement doesn't decrement, I need to see what fired and what didn't."

**Missing**: "I need `/simulate:session-trace` -- trace what happens when an agent opens a new session tab, switches between active conversations, and context propagates (or fails to propagate) across the workspace. The multisession workspace has its own lifecycle that's distinct from individual component rendering. Session context loss is our most reported bug category."

**Overlap/Confusion**: "The `data-flow` and `request-trace` skills overlap from my perspective. When I trace omnichannel routing, it's both a request (incoming chat) and a data flow (routing rules, queue metrics). I'd want one skill that handles the full path. Also, `permission-walkthrough` is relevant for me -- agents have different privilege levels for case actions -- but I'd rank it below the tracing skills for daily use."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Omnichannel routing and knowledge search tracing |
| state-validation | 4 | Case state after SLA timer start, entitlement check |
| contract-testing | 3 | Knowledge search result quality, but not the primary tool |
| deployment-trace | 3 | Solution import matters but not daily |
| plugin-chain | 5 | Case lifecycle plugins are heavily customized |
| permission-walkthrough | 4 | Agent privilege levels affect what actions are available |
| data-flow | 3 | Routing rules are data flow but I think of them as request routing |
| component-trace | 5 | Multisession workspace is the most complex component tree in D365 |
| migration-testing | 2 | Rare concern |
| integration-trace | 3 | Telephony/social channel integration exists but is specialized |

---

### Frontend: Finance

**Top 3**:
1. **`/simulate:state-validation`** -- "Journal entry is the foundation. I need to validate: starting state (ledger balances), operation (post a journal entry with specific account-dimension combinations), expected outcome (updated trial balance, subledger entries, dimension totals). If the journal posts and the trial balance doesn't match, that's an audit finding. State validation is my core mental model."
2. **`/simulate:data-flow`** -- "Financial data flows through a strict pipeline: source document -> accounting distribution -> subledger journal -> general ledger. When a vendor invoice posts but the GL entry has wrong dimensions, I need to trace that data flow step by step. Budget control is another pipeline: transaction entry -> budget check -> reservation -> hard stop or warning. Data flow tracing is how I find dimension mismatches."
3. **`/simulate:component-trace`** -- "The financial reporting viewer renders row definitions, column definitions, and reporting trees into formatted statements. When a column total doesn't match the GL or a drill-through lands on the wrong transactions, I need to trace through the report rendering components. Also, journal entry forms have complex dimension selectors that must respect account structure validation -- tracing that component interaction matters."

**Missing**: "I need `/simulate:period-close-sequence` -- trace the financial period close workflow through its task dependencies. Period close has mandatory sequencing: subledger posting must complete before GL close, intercompany must settle before consolidation, foreign currency revaluation must precede reporting. If a task runs out of sequence, the close is wrong. This isn't a component trace or a data flow -- it's a dependency-constrained sequence simulation."

**Overlap/Confusion**: "The `contract-testing` and `state-validation` skills are nearly identical from my perspective. When I validate that a posted journal entry produces the expected GL balances, is that 'state validation' (starting state -> operation -> expected outcome) or 'contract testing' (expected output vs actual output)? I'd use whichever one I found first and ignore the other. Also, `migration-testing` is just a specialized version of `state-validation` -- validate state before and after upgrade."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 2 | I don't think about HTTP requests; I think about posting pipelines |
| state-validation | 5 | Core -- GL balance validation after every posting operation |
| contract-testing | 3 | Overlaps with state-validation for me |
| deployment-trace | 3 | Package deployment matters at go-live, not daily |
| plugin-chain | 3 | F&O has event handlers, not Dataverse plugins; name is confusing |
| permission-walkthrough | 4 | Segregation of duties is a legal requirement in finance |
| data-flow | 5 | Source doc -> subledger -> GL pipeline tracing is essential |
| component-trace | 4 | Report viewer and dimension selector tracing |
| migration-testing | 3 | Version upgrades matter but are periodic |
| integration-trace | 2 | Finance integrations are batch-based, not real-time |

---

### Frontend: Power Automate

**Top 3**:
1. **`/simulate:request-trace`** -- "When a flow runs, every action is an HTTP request to a connector. The run history shows me inputs and outputs per action, but what I really need is an end-to-end request trace: trigger fires, first action calls Dataverse, second action calls SharePoint, third action sends an email. When the flow fails at action 47, I need to trace the request chain to find the root cause. This is my debugging model."
2. **`/simulate:component-trace`** -- "Adaptive cards render differently across Teams, Outlook, and web. When a card looks wrong in Teams but fine in Outlook, I need to trace through the card schema, the rendering host, and the host-specific constraints (28KB payload limit in Teams, no Action.Execute in Outlook). Component tracing across rendering hosts is my cross-platform testing need."
3. **`/simulate:contract-testing`** -- "Custom connectors define operations with input schemas and response schemas. When a connector action returns unexpected data, I need to compare the expected schema (from the OpenAPI definition) against the actual response. This is pure contract testing. Same for adaptive card Action.Submit -- the submitted data must match what the flow expects."

**Missing**: "I want `/simulate:trigger-evaluation` -- trace how a flow trigger evaluates whether to fire. Recurrence triggers are simple, but 'when a record is created or updated' triggers with filter conditions, 'when an item is created' with folder scope, and webhook triggers with retry policies are complex. When a flow doesn't fire and the user says 'but I updated the record,' I need to trace the trigger evaluation to explain why."

**Overlap/Confusion**: "The `plugin-chain` skill makes no sense for me. Power Automate flows ARE the automation layer -- they're not calling plugins, they ARE the plugin equivalent. The `data-flow` skill overlaps heavily with `request-trace` in my world -- a flow IS a data flow. I'd use request-trace for everything. Also, `integration-trace` sounds like a more specific version of `request-trace` -- every flow that calls an external connector is an integration."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 5 | Every flow action is a request -- this is my primary model |
| state-validation | 3 | Useful for approval state (pending/approved/rejected/timeout) |
| contract-testing | 5 | Connector schema validation is daily work |
| deployment-trace | 3 | Solution export/import for flows, not daily |
| plugin-chain | 1 | Not applicable -- flows are the automation, not plugin consumers |
| permission-walkthrough | 2 | Connection sharing exists but isn't complex |
| data-flow | 3 | Overlaps with request-trace for me |
| component-trace | 5 | Adaptive card cross-host rendering is critical |
| migration-testing | 2 | Flow migration is connection reference management, not schema |
| integration-trace | 3 | Every connector call is integration, but request-trace covers it |

---

### Frontend: Operations (F&O)

**Top 3**:
1. **`/simulate:component-trace`** -- "F&O has the densest form patterns in the portfolio: list pages, details masters, dialogs, FactBox panes, action pane hierarchies, grid controls with inline editing. When a user reports that the action pane button didn't do what they expected or the FactBox didn't refresh after a save, I need to trace through the form pattern, the action handler, and the rendering lifecycle. This is my daily work."
2. **`/simulate:state-validation`** -- "Operations is all about transaction throughput. After processing a purchase order (header -> lines -> confirm -> receive -> invoice), the state at each step must be correct: status fields, inventory reservations, financial dimensions, workflow approvals. I validate state transitions constantly -- starting state, operation, expected outcome."
3. **`/simulate:deployment-trace`** -- "F&O deployments are complex: packages include form customizations, data entities, batch jobs, and configurations. When a deployment breaks a form pattern or changes an action pane hierarchy, I need to trace what the deployment actually did. LCS package deployment is a frequent pain point -- tracing what changed and what broke is essential."

**Missing**: "I want `/simulate:batch-trace` -- trace what happens when a batch job runs: which tasks execute, in what order, with what parameters, and what the resulting state is. F&O is heavily batch-driven (MRP runs, inventory closing, financial posting schedules) and the batch monitoring forms are the primary diagnostic surface. Batch jobs affect what the UI shows tomorrow, and I need to trace that connection."

**Overlap/Confusion**: "The `plugin-chain` name is wrong for F&O. We have event handlers and CoC (Chain of Command) extensions, not Dataverse plugins. The concept maps, but the name makes it sound like it's for a different product. Also, `request-trace` and `data-flow` overlap -- when I trace a purchase order confirmation, the request goes through the PO confirmation service, which moves data through validation, posting, and inventory updates. Is that a request or a data flow? It's both."

**Scores**:

| Skill | Score | Rationale |
|-------|-------|-----------|
| request-trace | 3 | Relevant for X++ service calls but I think in form patterns |
| state-validation | 5 | Transaction state validation at every processing step |
| contract-testing | 3 | Data entity response validation, useful but not primary |
| deployment-trace | 5 | LCS package deployment tracing is critical for F&O |
| plugin-chain | 2 | Conceptually relevant but naming is wrong (CoC, not plugins) |
| permission-walkthrough | 3 | Security roles and duties matter, periodic need |
| data-flow | 4 | Order processing pipelines are data flows |
| component-trace | 5 | F&O form pattern tracing is core to my role |
| migration-testing | 4 | Version upgrades are major events in F&O |
| integration-trace | 3 | Dual-write and data entity integrations, but specialized |

---

## Cross-Persona Synthesis

### Consensus Top Skills

| Rank | Skill | Avg Score | Personas Rating 5 |
|------|-------|-----------|-------------------|
| 1 | `/simulate:component-trace` | 4.89 | 8 of 9 (all except Finance at 4) |
| 2 | `/simulate:state-validation` | 4.33 | 5 of 9 |
| 3 | `/simulate:request-trace` | 3.67 | 3 of 9 (Commerce, Copilot Studio, Customer Service, Automate) |
| 4 | `/simulate:plugin-chain` | 3.00 | 2 of 9 (Dataverse, Customer Service) |
| 5 | `/simulate:data-flow` | 3.44 | 2 of 9 (Power Apps, Finance) |
| 6 | `/simulate:contract-testing` | 3.67 | 2 of 9 (Commerce, Automate) |
| 7 | `/simulate:deployment-trace` | 3.33 | 1 of 9 (Operations) |
| 8 | `/simulate:permission-walkthrough` | 3.00 | 1 of 9 (Dataverse) |
| 9 | `/simulate:migration-testing` | 2.67 | 0 of 9 |
| 10 | `/simulate:integration-trace` | 2.78 | 0 of 9 |

**Clear winner**: `/simulate:component-trace` is the universal frontend skill. Every frontend persona traces user actions through UI component hierarchies as their core debugging activity.

**Strong second**: `/simulate:state-validation` resonates across Sales (BPF transitions), Power Apps (variable state), Finance (GL balances), and Operations (transaction state).

**Polarized skills**: `/simulate:request-trace` is essential for personas with API-heavy surfaces (Commerce, Copilot Studio, Automate) but irrelevant for form-centric personas (Sales, Finance). `/simulate:plugin-chain` is critical for Dataverse but confusing or irrelevant for everyone else.

### Consensus Gaps

Seven of nine personas identified a missing simulation need. Four distinct gap categories emerged:

1. **Form/UI lifecycle tracing** (Sales, Dataverse): Trace the full form load or field change event chain -- business rules, event handlers, show/hide/require cascades. Distinct from component-trace because it covers the temporal sequence of events on a single form, not the structural component tree.

2. **Multi-turn/session state tracing** (Copilot Studio, Customer Service): Trace state across conversation turns or workspace sessions. Single-request tracing doesn't capture context loss at turn boundaries or session switches.

3. **Offline/sync tracing** (Commerce): Trace the offline queue, conflict resolution, and resynchronization lifecycle. No existing skill addresses the offline-to-online transition.

4. **Trigger/batch evaluation tracing** (Automate, Operations): Trace why an automation fired or didn't fire, and what a batch job produced. The trigger evaluation is upstream of request-trace but currently invisible.

5. **Domain-specific sequence tracing** (Finance): Trace dependency-constrained workflows like period close. Not a data flow, not a component trace -- it's a dependency graph execution trace.

### Redundancies Identified

Three redundancy clusters emerged from persona feedback:

1. **`contract-testing` vs `state-validation`**: 6 of 9 personas noted overlap. Both check "did I get what I expected?" The distinction (contract = interface/API boundary, state = system state after operation) is meaningful to backend engineers but not to frontend developers who think about both as validation.

2. **`request-trace` vs `integration-trace`**: 5 of 9 personas found these confusing. From the frontend perspective, a request that crosses a system boundary IS an integration. The distinction (request = within system, integration = across systems) is an infrastructure concern, not a frontend concern.

3. **`plugin-chain` naming**: 5 of 9 personas noted the name is Dataverse-specific. F&O uses "event handlers" and "Chain of Command." Power Automate uses "flow actions." Copilot Studio uses "plugin actions." The concept (trace through the automation/extension chain) is universal, but the name alienates non-Dataverse personas.

### Proposed New Skills

Based on gap analysis across all personas:

| Proposed Skill | Gap Source | Description |
|----------------|-----------|-------------|
| `/simulate:form-lifecycle` | Sales, Dataverse | Trace form load/save event sequence: business rules, event handlers, show/hide/require cascades, PCF renders, quick view resolution |
| `/simulate:session-trace` | Copilot Studio, Customer Service | Trace state propagation across multi-turn conversations or multisession workspace tab switches |
| `/simulate:offline-sync` | Commerce | Trace offline queue accumulation, conflict detection, and resynchronization after reconnect |
| `/simulate:trigger-evaluation` | Automate, Operations | Trace why an automation trigger or batch job did/did not fire, including filter conditions, recurrence, and retry policies |
| `/simulate:sequence-validation` | Finance | Trace dependency-constrained task sequences (period close, processing pipelines) for correct ordering and prerequisite enforcement |

### Score Distribution Summary

| Skill | Min | Max | Range | Consensus |
|-------|-----|-----|-------|-----------|
| component-trace | 4 | 5 | 1 | Strong universal |
| state-validation | 3 | 5 | 2 | Strong with variance |
| request-trace | 2 | 5 | 3 | Polarized by API-centricity |
| contract-testing | 3 | 5 | 2 | Moderate, overlap concern |
| data-flow | 2 | 5 | 3 | Polarized by data-centricity |
| plugin-chain | 1 | 5 | 4 | Highly polarized by product |
| deployment-trace | 2 | 5 | 3 | Spikes for F&O |
| permission-walkthrough | 2 | 5 | 3 | Spikes for Dataverse |
| migration-testing | 1 | 4 | 3 | Generally low |
| integration-trace | 2 | 3 | 1 | Uniformly moderate-low |

### Key Findings

1. **Component-trace is the universal frontend skill**. Every frontend persona, regardless of product, traces user actions through UI component hierarchies. This skill should be the flagship of the Tier 3 set for frontend audiences.

2. **State-validation is the universal verification skill**. Whether it's BPF stage transitions, GL balances, or conversation state, frontend developers think in terms of "starting state -> operation -> expected state."

3. **Rename plugin-chain to extension-chain or handler-chain**. The current name alienates 5 of 9 personas. A product-neutral name would capture Dataverse plugins, F&O event handlers/CoC, Power Automate flow actions, and Copilot Studio plugin actions.

4. **Merge or clearly differentiate contract-testing and state-validation**. Frontend developers don't distinguish between "API contract" and "system state" the way backend engineers do. Either merge them or add crystal-clear guidance on when to use which.

5. **Merge or clearly differentiate request-trace and integration-trace**. From the frontend perspective, all cross-boundary requests are integrations. Either merge them (with a flag for cross-system boundaries) or rename integration-trace to something that signals external/third-party systems specifically.

6. **Migration-testing and integration-trace scored lowest**. Consider whether these belong in Tier 3 or should be deferred to a Tier 4 expansion. Neither reached a score of 5 from any persona.

7. **Five new skills emerged from gaps**. The most actionable are `form-lifecycle` (addresses the #1 gap for the two largest persona groups: Sales and Dataverse) and `session-trace` (addresses the gap for the two fastest-growing product areas: Copilot Studio and Customer Service).
