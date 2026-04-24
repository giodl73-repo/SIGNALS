# /trace: Specification

**Topic**: sim
**Namespace**: /trace:
**Skills**: 7
**Default mode**: Full
**Audience**: System developers -- Dataverse platform engineers, Commerce backend developers, Power Automate backend developers, Connectors developers, and full-stack developers who build and debug at the platform/infrastructure layer across Dynamics 365 and Power Platform

## Purpose

Does the system work? /trace: lets a system developer hand-compile a request, state transition, contract, component interaction, deployment, migration, or permission chain through the platform's actual service layers -- and discover failure points, contract mismatches, and architectural assumptions that are wrong before code ships.

## Skills

### /trace:request

**What**: Hand-compile a single request through every service boundary from entry point to data layer and back, producing a structured layer-by-layer trace with latency budgets and failure modes.
**Validated by**: Dataverse (5/5 across all three persona categories -- "every OData call I debug"), Commerce (5/5 -- "CSU API tracing is my primary debugging tool"), Customer Service (5/5 -- "omnichannel message routing is multi-hop tracing"), Automate (5/5 -- "flow execution IS request tracing"), Copilot Studio (5/5 -- "agent runtime execution tracing")
**Input**: The request (HTTP method, URL, payload), the entry point (API gateway, POS app, flow trigger, agent runtime), the expected endpoint (record created, response returned, message delivered), and the system context (product area, solution, environment tier).
**Output**: Structured trace artifact (table format: Layer | Entry | Processing | Exit | Latency | Failure Modes) with findings on failure points, latency risks, contract mismatches, and missing error handling.
**Lifecycle**:
- Setup: Identify the request (POST /api/data/v9.2/accounts with payload {name: "Contoso", revenue: 50000}). Entry point: Dataverse Web API gateway. Expected endpoint: Account record created in Azure SQL, 201 response with OData entity. System context: Dynamics 365 Sales, standard table, production environment. Select roles (Dataverse Platform Engineer, API Designer).
- Execute: Hand-compile layer by layer.
  Layer 1 -- API Gateway: HTTPS terminates, request authenticated via Entra ID bearer token. Token validated: audience=https://org.crm.dynamics.com, scope=user_impersonation. CallerObjectId extracted. Latency: 15ms.
  Layer 2 -- OData Routing: URI parsed. Entity set=accounts, operation=Create. Entity metadata loaded from solution layer cache. Custom fields validated against entity schema. Latency: 8ms.
  Layer 3 -- Plugin Pipeline (Pre-Validation, Stage 10): 2 registered steps. Step 1: DuplicateDetection (sync, order 1) -- queries accounts where name='Contoso', finds 0 matches, passes. Step 2: DataValidation (sync, order 2) -- validates revenue > 0, passes. Pre/post images: pre-image not available (Create operation). Latency: 45ms (DuplicateDetection query is the bottleneck).
  Layer 4 -- Plugin Pipeline (Pre-Operation, Stage 20): 1 registered step. TerritoryAssignment (sync, order 1) -- evaluates territory rules, assigns territory "West-US". Modifies the target entity to include territoryid. Latency: 12ms.
  Layer 5 -- Core Operation: Azure SQL INSERT into AccountBase table. Record ID generated (GUID). Created/modified timestamps set. Row version (@@ROWVERSION) stamped. Optimistic concurrency ETag generated. Latency: 22ms.
  Layer 6 -- Plugin Pipeline (Post-Operation, Stage 40): 2 steps. Step 1: AuditTrail (sync, order 1) -- creates audit record in AuditBase. Step 2: SearchIndex (async, order 1) -- queues index update for Dataverse Search. Latency: 18ms (sync only).
  Layer 7 -- Service Endpoints: 1 registered. WebhookToServiceBus (async) -- serializes RemoteExecutionContext, posts to Service Bus topic. Latency: async, not on critical path.
  Layer 8 -- Response Assembly: OData entity serialized. 201 Created. Headers: OData-EntityId, ETag. Response body includes all fields with computed values (createdon, modifiedon, ownerid, territoryid). Latency: 5ms.
  Total synchronous latency: 125ms. Async tail: SearchIndex (~500ms), ServiceBus webhook (~200ms).
- Findings: P1: DuplicateDetection plugin queries accounts by name with no index on the name column -- at scale (>500K accounts), this query degrades to 2-3 seconds, pushing total latency past the 429 protection threshold for high-volume import scenarios. P2: Pre-image is not configured for the DuplicateDetection step but the plugin code attempts to read it -- fails silently and skips duplicate check on Update operations (only works on Create because Create has no pre-image). P3: Response body includes the full entity representation (142 fields) when the caller only needs the record ID -- no $select on the response, wasting bandwidth on mobile clients.
- Amend: Platform engineer reviews: "DuplicateDetection was rewritten in 10.0.39 to use Dataverse Search instead of a direct SQL query -- re-trace Layer 3 with the new implementation." Re-trace: Search API call replaces SQL query, latency drops to 8ms. P1 resolved. Engineer also notes: "Pre-image for Update is intentionally not registered to avoid the performance cost of retrieving the full record before every update." P2 reclassified as "by design" with documentation needed.
**Lightweight**: --quick traces the request as a 3-layer summary (entry -> processing -> exit) with total latency, no per-plugin or per-layer detail.
**Artifact**: `trace/request/sim-create-account-2026-03-14.md`
**Example**:
```
User: /trace:request
> Request: POST /api/data/v9.2/accounts {name: "Contoso", revenue: 50000}
> Entry: Dataverse Web API gateway (Sales, production)
> Expected: Account created, 201 response

| Layer | Entry | Processing | Exit | Latency | Failure Modes |
|-------|-------|------------|------|---------|---------------|
| API Gateway | HTTPS request | Entra token validation | Authenticated principal | 15ms | 401 (expired token), 403 (wrong audience) |
| OData Routing | Entity set: accounts | Schema validation, field mapping | Validated create message | 8ms | 400 (unknown field), 412 (schema mismatch) |
| Pre-Validation | Create message | DuplicateDetection, DataValidation | Passed | 45ms | DuplicateDetection query timeout at scale |
| Pre-Operation | Validated message | TerritoryAssignment | Territory assigned | 12ms | Territory rules misconfigured |
| Core Operation | Entity with territory | Azure SQL INSERT | Record created (GUID) | 22ms | Deadlock on concurrent insert |
| Post-Operation | Created record | AuditTrail (sync), SearchIndex (async) | Audited + indexed | 18ms | Audit table full, search service down |
| Service Endpoints | Execution context | ServiceBus webhook (async) | Message queued | async | Service Bus throttle, serialization error |
| Response | OData entity | Serialize 142 fields | 201 Created + ETag | 5ms | Serialization timeout on large entity |

Total sync: 125ms | Async tail: ~700ms
Findings:
  P1: DuplicateDetection name query has no index -- degrades at >500K records
  P2: Pre-image not registered -- duplicate check silently fails on Update
  P3: Full entity in response (142 fields) -- no $select optimization
```

---

### /trace:state

**What**: Hand-compile a state transition through the platform's state machine -- starting state, operation sequence, expected outcome -- validating that every intermediate state is correct and every side effect fires.
**Validated by**: Dataverse (5/5 -- "record state, statecode/statuscode, concurrency"), Sales (5/5 -- "sales IS state transitions -- lead to opportunity to close"), Customer Service (5/5 -- "case lifecycle + SLA timers are pure state machines"), Finance (5/5 -- "every financial posting is a state transition")
**Input**: The entity type, starting state (field values), operation sequence (one or more API calls or user actions), and expected ending state (field values, related records, side effects).
**Output**: State trace artifact (per-operation: pre-state snapshot, operation, post-state snapshot, side effects, assertions pass/fail) with findings on unexpected state, missing side effects, and concurrency issues.
**Lifecycle**:
- Setup: Identify the entity and state machine. Entity: Case (incident) in Dynamics 365 Customer Service. Starting state: Case created (statecode=0 Active, statuscode=1 InProgress, Priority=High, SLA KPI instance started at 09:00 AM, business calendar=M-F 8AM-5PM). Operation sequence: (1) Agent puts case on hold at 2:00 PM Monday, (2) Customer responds Tuesday 10:00 AM, agent resumes, (3) Agent resolves case Wednesday 3:00 PM. Expected ending state: Case resolved (statecode=1 Resolved, statuscode=5 ProblemSolved), SLA elapsed time = 14 business hours (Monday 9AM-2PM = 5h + Tuesday 10AM-5PM = 7h + Wednesday 8AM-3PM... wait, that exceeds the target). Select roles (Customer Service Dev, SLA Administrator).
- Execute: Hand-compile each operation.
  Operation 1 -- SetState(statecode=0, statuscode=2 OnHold) at Monday 2:00 PM:
    Pre-state: {statecode:0, statuscode:1, SLA elapsed: 5h (9AM-2PM), SLA paused: false}
    Processing: SetState message fires. Plugin "SLAPauseHandler" (pre-op) detects statuscode change to OnHold. SLA KPI instance updated: pausedon=2:00 PM, elapsed=5h, status=InProgress. Business rule "RequireHoldReason" fires: hold reason field becomes required.
    Post-state: {statecode:0, statuscode:2, SLA elapsed: 5h, SLA paused: true, holdReasonRequired: true}
    Assertion: SLA timer paused at exactly 5 business hours? PASS.
  Operation 2 -- SetState(statecode=0, statuscode=1 InProgress) at Tuesday 10:00 AM:
    Pre-state: {statecode:0, statuscode:2, SLA elapsed: 5h, SLA paused: true}
    Processing: SetState to InProgress. SLAResumeHandler (pre-op) calculates pause duration: Monday 2PM to Tuesday 10AM = 0 business hours on Monday (past 2PM, remaining 3h but paused) + 2 business hours on Tuesday (8AM-10AM). Wait -- the SLA was PAUSED during this time. The pause duration is not added to elapsed; elapsed stays at 5h. SLA resumes counting from Tuesday 10:00 AM.
    Post-state: {statecode:0, statuscode:1, SLA elapsed: 5h, SLA paused: false, SLA resumedon: Tue 10AM}
    Assertion: SLA elapsed still 5h after resume? PASS. SLA counting from Tuesday 10AM? PASS.
  Operation 3 -- CloseIncident(Resolution="Fixed display driver") at Wednesday 3:00 PM:
    Pre-state: {statecode:0, statuscode:1, SLA elapsed: 5h + Tue 10AM-5PM(7h) + Wed 8AM-3PM(7h) = 19h}
    Processing: CloseIncident message fires. SLA KPI instance finalized: elapsed=19 business hours. SLA target for Priority=High: 16 business hours. SLA status: BREACHED (19h > 16h target). SLA breach notification plugin fires: sends email to case owner's manager.
    Post-state: {statecode:1, statuscode:5, SLA elapsed: 19h, SLA status: Breached, resolution: "Fixed display driver"}
    Assertion: SLA correctly calculated as 19 business hours? PASS. SLA correctly breached? PASS.
- Findings: P1: The SLA breach occurred at Tuesday 10AM + 11h = 11 business hours remaining, which means the breach actually happened at Wednesday 1:00 PM (5PM Tuesday = 12h, 8AM-1PM Wednesday = 17h... recalculating: 5h pre-pause + 7h Tuesday + 4h Wednesday 8AM-12PM = 16h = breach at Wednesday 12:00 PM noon). The agent resolved at 3:00 PM, 3 hours after breach. The SLA warning (80% = 12.8h) should have fired at Tuesday ~4:48 PM, but no warning notification was configured. P2: The hold reason field is required by business rule when status=OnHold, but the API call SetState does not include it in the update -- the business rule fires client-side only. API callers bypass the hold reason requirement. P3: CloseIncident does not validate that all child activities are completed -- 2 open tasks remain on this case.
- Amend: SLA admin reviews: "The warning threshold is configured at 75%, not 80%. Re-calculate." Re-trace: 75% of 16h = 12h. Warning at 5h + 7h = 12h = Tuesday 5:00 PM exactly. Warning fires at end of business Tuesday. Agent sees it Wednesday morning. P1 adjusted: warning fired but agent had 4 business hours to resolve, and took 7h. The gap is operational (agent response time), not system (SLA calculation is correct).
**Lightweight**: --quick validates a single state transition (one operation) with pre/post assertions, no multi-step sequence.
**Artifact**: `trace/state/sim-case-sla-lifecycle-2026-03-14.md`
**Example**:
```
User: /trace:state
> Entity: Case (incident), Customer Service
> Start: Active, Priority=High, SLA started 09:00 AM Monday
> Operations: (1) OnHold Mon 2PM, (2) Resume Tue 10AM, (3) Resolve Wed 3PM

| # | Operation | Pre-State | Processing | Post-State | SLA Elapsed | Assertions |
|---|-----------|-----------|------------|------------|-------------|------------|
| 1 | SetState -> OnHold | Active, 5h elapsed | SLAPauseHandler, RequireHoldReason BR | OnHold, paused | 5h (paused) | Timer paused: PASS |
| 2 | SetState -> InProgress | OnHold, 5h frozen | SLAResumeHandler | Active, counting | 5h (resumed) | Elapsed unchanged: PASS |
| 3 | CloseIncident | Active, 19h elapsed | SLA finalized, breach detected | Resolved, breached | 19h (3h over) | Breach detected: PASS |

Findings:
  P1: SLA breached at Wed 12:00 PM -- warning at Tue 5:00 PM gave agent only 4h next-day window
  P2: Hold reason required by BR but not enforced on API -- bypass possible
  P3: 2 open child activities not validated before close
```

---

### /trace:contract

**What**: Hand-compile expected vs actual output for an API contract, connector schema, or inter-service agreement -- validating that the producer's output matches the consumer's expectations.
**Validated by**: Connectors (5/5 -- "OpenAPI schema validation is my entire job"), Automate (5/5 -- "connector schema validation is critical"), Copilot Studio (5/5 -- "action I/O parameter contracts"), Finance (5/5 developer -- "financial reports are contracts with auditors"), Commerce (5/5 frontend -- "cross-channel price/promotion consistency is non-negotiable")
**Input**: The contract definition (OpenAPI schema, typed action parameters, report specification, or data entity schema), a test input, and the expected output.
**Output**: Contract validation artifact (field-by-field comparison: expected type/value vs actual type/value, MATCH/MISMATCH/MISSING per field) with findings on schema drift, type coercion issues, and breaking changes.
**Lifecycle**:
- Setup: Identify the contract. Contract: Custom connector "WeatherEnrichment" operation GetForecast. OpenAPI definition specifies response schema: {temperature: number, condition: string, humidity: number, forecast: array[{date: string, high: number, low: number}]}. Test input: location="Seattle". Consumer: Power Automate flow that parses the response with Parse JSON action using the schema above. Select roles (Connectors Dev, API Designer).
- Execute: Hand-compile the expected vs actual.
  Call the operation mentally: GET /forecast?location=Seattle.
  Expected response (from OpenAPI schema):
    {temperature: 58.2, condition: "Partly Cloudy", humidity: 72, forecast: [{date: "2026-03-15", high: 62, low: 48}, {date: "2026-03-16", high: 59, low: 45}]}
  Actual response (from API documentation / last known response):
    {temp: 58.2, condition: "Partly Cloudy", humidity: "72%", forecast: [{date: "2026-03-15", high: 62, low: 48}, {date: "2026-03-16", high: 59, low: 45}], wind: {speed: 12, direction: "NW"}}
  Field-by-field comparison:
    | Field | Expected | Actual | Status |
    |-------|----------|--------|--------|
    | temperature | number (58.2) | -- | MISSING (field renamed to "temp") |
    | temp | -- | number (58.2) | UNEXPECTED (not in schema) |
    | condition | string | string | MATCH |
    | humidity | number (72) | string ("72%") | TYPE MISMATCH (number vs string) |
    | forecast | array[object] | array[object] | MATCH (structure) |
    | forecast[].date | string | string | MATCH |
    | forecast[].high | number | number | MATCH |
    | forecast[].low | number | number | MATCH |
    | wind | -- | object | UNEXPECTED (not in schema) |
- Findings: P1: "temperature" renamed to "temp" -- the Parse JSON action in the consuming flow will fail on this field because it expects "temperature". Every flow using this connector's GetForecast operation will get a null temperature value. P2: "humidity" changed from number to string ("72%") -- Parse JSON will fail type validation. Flows with strict schema validation enabled will throw; flows without strict validation will coerce to null. P3: "wind" field added but not in the OpenAPI schema -- not a breaking change (extra fields are ignored by Parse JSON), but the schema is stale and consumers cannot use the new field until the connector is updated.
- Amend: Connectors dev reviews: "The API provider changed the schema in v2.1. We need to update the OpenAPI definition. But we also need a backwards-compatibility shim: accept both 'temperature' and 'temp', parse '72%' to 72." Re-trace with updated OpenAPI and shim: all fields match. P1 and P2 resolved. P3 remains (wind field should be added to schema for consumer use).
**Lightweight**: --quick compares top-level field names and types only, no nested object traversal or value comparison.
**Artifact**: `trace/contract/sim-weather-connector-getforecast-2026-03-14.md`
**Example**:
```
User: /trace:contract
> Contract: WeatherEnrichment connector, GetForecast operation
> OpenAPI schema: {temperature: number, condition: string, humidity: number, forecast: array}
> Test input: location="Seattle"

| Field | Schema Type | Actual Type | Actual Value | Status |
|-------|------------|-------------|-------------|--------|
| temperature | number | -- | -- | MISSING (renamed to "temp") |
| temp | -- | number | 58.2 | UNEXPECTED |
| condition | string | string | "Partly Cloudy" | MATCH |
| humidity | number | string | "72%" | TYPE MISMATCH |
| forecast | array | array | [2 items] | MATCH |
| forecast[0].date | string | string | "2026-03-15" | MATCH |
| forecast[0].high | number | number | 62 | MATCH |
| forecast[0].low | number | number | 48 | MATCH |
| wind | -- | object | {speed:12, dir:"NW"} | UNEXPECTED |

Findings:
  P1: Field rename (temperature -> temp) breaks all consumers
  P2: Type change (humidity: number -> string) breaks strict parsers
  P3: New field (wind) not in schema -- stale OpenAPI definition
```

---

### /trace:component

**What**: Hand-compile a user action through the UI component tree -- form load, field change, button click -- tracing event handlers, business rules, PCF control renders, and state propagation.
**Validated by**: Frontend personas universally (4.89 average, 8 of 9 scored 5): Sales (BPF + form), Commerce (POS + storefront), PowerApps (canvas components), Copilot Studio (topic node tree), Dataverse (model-driven forms), Customer Service (multisession workspace), Operations (F&O form patterns), Automate (adaptive cards)
**Input**: The UI surface (form name, app, page), the user action (click, field change, navigation), and the expected visual/state outcome.
**Output**: Component trace artifact (event sequence: trigger -> handler chain -> state changes -> renders -> visual outcome) with findings on event conflicts, render failures, and state inconsistencies.
**Lifecycle**:
- Setup: Identify the surface. Surface: Opportunity Main Form in Dynamics 365 Sales, model-driven app. User action: seller drags opportunity from "Develop" to "Propose" in the pipeline Kanban view. Expected outcome: BPF stage updates, EstimatedRevenue recalculates, forecast dashboard reflects new stage. Select roles (Sales Frontend Dev, UX Designer).
- Execute: Hand-compile the event chain.
  Event 1 -- Kanban drag: User drops opportunity card on "Propose" column. Kanban control fires onStageChange event with opportunityid and target stage "Propose".
  Event 2 -- BPF stage transition: Unified Interface calls MoveToNextStage API. BPF validates gate conditions: is "estimatedclosedate" set? YES. Is "customer need" filled? YES. Is "proposed solution" filled? NO -- gate condition fails.
  Event 3 -- Validation feedback: BPF returns error: "Complete required field: Proposed Solution." Kanban control receives error, reverts the card to "Develop" column. Toast notification appears: "Please fill in Proposed Solution before advancing to Propose."
  Event 4 -- Form context: User opens the opportunity record from the Kanban card. Form loads in a side panel. OnLoad fires: 3 business rules evaluate. BR-1: "Show Competitor tab when BPF stage >= Develop" -> Competitor tab visible. BR-2: "Require Budget Amount when stage = Propose" -> budget field not yet required (still in Develop). BR-3: "Lock Won/Lost fields until stage = Close" -> fields locked.
  Event 5 -- Field change: User fills "Proposed Solution" field. onChange fires. No form script registered on this field. Business rules re-evaluate: BR-2 still not triggered (stage is still Develop). PCF control "RichTextEditor" renders the field value.
  Event 6 -- Retry stage transition: User clicks "Next Stage" button in BPF header. MoveToNextStage re-validates. Gate passes. BPF stage updates to "Propose". BR-2 fires: Budget Amount becomes required. Form refresh: Propose stage fields appear. EstimatedRevenue recalculation plugin fires (async).
  Event 7 -- Dashboard impact: Forecast dashboard (separate tab) polls for updates on 30-second interval. Next poll picks up the stage change. Opportunity moves from "Develop" forecast category to "Propose" category. Revenue column updates.
- Findings: P1: The Kanban drag-and-drop provides no inline guidance about which fields are missing for the gate condition -- the toast notification says "Proposed Solution" but the user must open the record to find the field. A pre-validation tooltip on the Kanban card would prevent the failed drag. P2: The 30-second polling interval on the forecast dashboard means the manager sees stale data for up to 30 seconds after the seller advances the stage -- during pipeline reviews, this causes confusion ("I just moved it, why doesn't it show?"). P3: Business rule BR-2 (Require Budget Amount) fires when stage reaches Propose, but the BPF gate for Propose does not include Budget Amount -- so the user can advance to Propose without a budget, then immediately sees a required field that was not part of the gate. Inconsistent validation experience.
- Amend: Sales frontend dev reviews: "The Kanban pre-validation tooltip is available in the 2026 Wave 1 release -- re-trace with the new control." Re-trace: Kanban now shows a popover listing required fields before allowing the drop. P1 resolved. Dev also notes: "Budget Amount should be added to the BPF gate, not just the business rule. The business rule fires too late." P3 escalated to a configuration change request.
**Lightweight**: --quick traces only the primary event chain (one user action -> one outcome), no business rule evaluation or dashboard propagation.
**Artifact**: `trace/component/sim-opportunity-kanban-stage-2026-03-14.md`
**Example**:
```
User: /trace:component
> Surface: Opportunity Kanban, Dynamics 365 Sales
> Action: Drag opportunity from Develop to Propose
> Expected: Stage advances, revenue recalculates, forecast updates

Event chain:
  1. Kanban onStageChange -> MoveToNextStage API
  2. BPF gate validation: estimatedclosedate=PASS, customerneed=PASS, proposedsolution=FAIL
  3. Kanban reverts card, toast: "Complete Proposed Solution"
  4. User opens record, fills Proposed Solution
  5. User clicks Next Stage -> gate passes -> stage=Propose
  6. BR-2 fires: Budget Amount now required
  7. Forecast dashboard polls at +30s, reflects new stage

Findings:
  P1: No inline Kanban pre-validation -- user must open record to see missing fields
  P2: 30s dashboard polling delay causes confusion during pipeline reviews
  P3: BPF gate and business rule disagree on required fields at Propose stage
```

---

### /trace:deployment

**What**: Hand-compile what happens when you deploy, import, or publish a solution -- tracing component resolution, dependency validation, managed layer merging, and post-import side effects.
**Validated by**: Commerce (5/5 -- "CSU deployment is high-risk and complex"), Operations (5/5 -- "LCS package deployment is high-stakes"), Dataverse developer (4/4 -- "solution import, managed layers, component conflicts")
**Input**: The deployment artifact (solution file, LCS package, CSU extension, agent publish), source environment, target environment, and the expected post-deployment state.
**Output**: Deployment trace artifact (per-phase: pre-flight validation, component extraction, dependency resolution, layer merge, post-import actions, verification) with findings on breaking changes, missing dependencies, and layer conflicts.
**Lifecycle**:
- Setup: Identify the deployment. Artifact: Managed solution "ContosoSalesExtensions_1.2.0" (20 components: 3 entities, 5 forms, 4 views, 3 plugins, 2 flows, 2 web resources, 1 sitemap). Source: Dev environment (org-dev.crm.dynamics.com). Target: Production (org-prod.crm.dynamics.com). Production currently has ContosoSalesExtensions_1.1.0 installed. Select roles (Dataverse Platform Engineer, Release Manager).
- Execute: Hand-compile each deployment phase.
  Phase 1 -- Pre-flight: Solution checker validates XML. 20 components parsed. Dependency check: solution depends on "MicrosoftDynamics365Sales" version >= 9.0.2.1. Target has version 9.0.2.3. PASS. Solution depends on "CustomConnectorShared" version >= 1.0.0. Target has version 1.0.0. PASS.
  Phase 2 -- Component extraction: 20 components unpacked. Entity "new_dealroom" has 3 new columns in v1.2.0 (new_priority, new_riskrating, new_dealvalue). Form "DealRoom Main" has a new tab "Risk Assessment". View "Active Deal Rooms" has new columns in the layout. Plugin "DealRoomScoring" is a new registration (Create message, post-operation, async).
  Phase 3 -- Dependency resolution: Plugin "DealRoomScoring" depends on assembly "ContosoScoring.dll" v2.1 -- check target plugin registration. Target has v2.0 from solution v1.1.0. Managed solution upgrade: v2.0 assembly will be replaced by v2.1. Existing plugin step registrations on the v2.0 assembly: 2 steps (DealRoomValidation, DealRoomAutoAssign). These steps reference types in the assembly -- verify type names unchanged. DealRoomValidation type: "ContosoScoring.DealRoomValidation" -> still exists in v2.1. PASS. DealRoomAutoAssign type: "ContosoScoring.DealRoomAutoAssign" -> RENAMED to "ContosoScoring.AutoAssignment" in v2.1. FAIL -- plugin step will break.
  Phase 4 -- Layer merge: Production has an unmanaged customization on the "DealRoom Main" form (added a custom tab "Local Notes" by the production admin). Managed solution import merges layers: managed layer (new "Risk Assessment" tab) + unmanaged layer ("Local Notes" tab). Both tabs preserved. Form section ordering: managed sections render first, unmanaged sections append. "Local Notes" tab moves to the end of the tab order.
  Phase 5 -- Post-import: Connection references: flow "DealRoomNotification" requires a Dataverse connection reference. Target environment has the connection reference from v1.1.0. Connection still valid. Flow activates automatically. Plugin assembly registered. Async plugin "DealRoomScoring" registered on Create message.
  Phase 6 -- Verification: 19 of 20 components imported successfully. Plugin step "DealRoomAutoAssign" failed: type "ContosoScoring.DealRoomAutoAssign" not found in assembly v2.1.
- Findings: P1: Plugin type rename (DealRoomAutoAssign -> AutoAssignment) breaks the existing plugin step registration. The managed solution import will succeed for 19 components but the DealRoomAutoAssign step will be orphaned -- it references a type that no longer exists in the assembly. Any Account Create operation that triggers this step will throw TypeLoadException at runtime. P2: The "Local Notes" unmanaged tab moves to the end of the tab order after import -- production users who added this tab expect it in position 3. The reordering is cosmetic but will generate support tickets. P3: Flow "DealRoomNotification" activates automatically on import -- if it sends notifications, production users will receive unexpected emails immediately after deployment. The flow should be imported in an inactive state.
- Amend: Release manager reviews: "The type rename was intentional but the old plugin step should have been removed in the solution. Add a delete component for the old step registration." Re-trace with the delete component included: Phase 3 now removes the old step before registering the new assembly. P1 resolved. Release manager also adds: "Set the flow to import as inactive using the environment variable 'ActivateFlowsOnImport=false'." P3 resolved.
**Lightweight**: --quick runs pre-flight dependency check and lists components being added/modified/removed, no layer merge or post-import analysis.
**Artifact**: `trace/deployment/sim-contoso-sales-v120-2026-03-14.md`
**Example**:
```
User: /trace:deployment
> Artifact: ContosoSalesExtensions_1.2.0 (managed, 20 components)
> Source: Dev, Target: Production (has v1.1.0)

| Phase | Input | Processing | Result |
|-------|-------|------------|--------|
| Pre-flight | solution.xml | Dependency check (Sales >= 9.0.2.1) | PASS |
| Extraction | 20 components | 3 entities, 5 forms, 4 views, 3 plugins, 2 flows, 2 WR, 1 sitemap | Parsed |
| Dependencies | Plugin assembly v2.1 | Type check: Validation=PASS, AutoAssign=RENAMED | FAIL on AutoAssign |
| Layer merge | Form + unmanaged layer | Managed tabs + Local Notes tab | Local Notes moves to end |
| Post-import | Flows, plugins | DealRoomNotification auto-activates | Active (unintended) |
| Verification | 20 components | 19 success, 1 orphaned step | DealRoomAutoAssign broken |

Findings:
  P1: Type rename breaks plugin step -- TypeLoadException at runtime
  P2: Unmanaged tab reordering -- cosmetic but generates tickets
  P3: Flow auto-activates -- sends unexpected notifications
```

---

### /trace:migration

**What**: Hand-compile expected vs actual system state after a schema change, version upgrade, or data migration -- validating that existing data, customizations, and integrations survive the transition.
**Validated by**: Commerce (4/4 -- "CSU version upgrades break CRT extensions regularly"), Operations (4/4 -- "entity version upgrades V2->V3 are real risk"), Finance (4/4 -- "fiscal year changes, chart of accounts restructuring"), Dataverse developer (4/4 -- "schema changes, solution upgrades, managed layer conflicts")
**Input**: The migration (schema change, version upgrade, data transformation), the pre-migration state (current schema, data sample, active integrations), and the expected post-migration state.
**Output**: Migration trace artifact (pre-state snapshot, migration steps, post-state snapshot, diff report, integration impact assessment) with findings on data loss, breaking changes, and integration failures.
**Lifecycle**:
- Setup: Identify the migration. Migration: F&O data entity upgrade from SalesOrderHeaderV2 to SalesOrderHeaderV3 during 10.0.40 platform update. Pre-migration: 145,000 sales order records, 12 active dual-write maps referencing V2, 3 Power Automate flows using the V2 OData endpoint, 1 custom report using V2 fields. Select roles (Operations Dev, Data Migration Architect). Load the V2->V3 schema diff (4 fields renamed, 2 fields removed, 6 fields added, 1 field type changed).
- Execute: Hand-compile the migration impact.
  Schema changes:
    Renamed: SalesOrderNumber -> OrderNumber, CustomerAccount -> InvoiceAccount, DeliveryAddress -> ShipToAddress, RequestedShipDate -> ConfirmedShipDate
    Removed: LegacyOrderType (deprecated in V2, removed in V3), CustomField_01 (never used, cleanup)
    Added: OrderPriority (int), FulfillmentChannel (string), EstimatedDeliveryDate (datetime), WarehouseCode (string), ReturnReasonCode (string), SustainabilityScore (decimal)
    Type changed: DiscountPercent from decimal(5,2) to decimal(7,4) -- increased precision
  Impact on 12 dual-write maps:
    Maps 1-8: Reference SalesOrderNumber -> BROKEN (field renamed to OrderNumber)
    Maps 9-10: Reference CustomerAccount -> BROKEN (renamed to InvoiceAccount)
    Maps 11-12: Use only common fields that were not renamed -> PASS
  Impact on 3 Power Automate flows:
    Flow 1 "OrderSync": $select=SalesOrderNumber,CustomerAccount -> BROKEN (both renamed)
    Flow 2 "OrderApproval": $filter=StatusCode eq 1 -> PASS (StatusCode unchanged)
    Flow 3 "OrderExport": $expand=SalesOrderLines -> PASS (navigation property unchanged)
  Impact on custom report:
    Report uses LegacyOrderType in a grouping column -> BROKEN (field removed)
  Data migration:
    145,000 records: field renames are metadata-only (no data movement). Type change on DiscountPercent: existing values (max 2 decimal places) fit in new precision (4 decimal places) -- no data loss.
- Findings: P1: 10 of 12 dual-write maps will fail immediately after upgrade. Dual-write sync will log errors in the integration journal, and the 5-second sync SLA will be missed for all sales order changes until maps are updated. This affects real-time order visibility in Dataverse/Sales. P2: Flow "OrderSync" will return HTTP 400 (unknown field) on the next trigger event after upgrade. The flow will enter a failed state and require manual re-activation with updated field names. P3: Custom report breaks silently -- the grouping column returns null instead of erroring, producing a report with all orders grouped under "(blank)". Finance team will not notice until the next monthly review.
- Amend: Data migration architect reviews: "The dual-write maps should be updated before the upgrade, not after. Re-sequence: update maps in staging -> validate -> apply upgrade -> verify." Re-trace with pre-updated maps: maps reference new field names before the entity upgrade occurs -> maps fail during the brief window between map update and entity upgrade (V2 entity, V3 field names). Revised approach: pause dual-write, apply upgrade, update maps, resume. P1 mitigated (downtime instead of data loss, 15-minute window).
**Lightweight**: --quick lists schema changes (renamed/removed/added/type-changed) and counts affected integrations, no per-integration detailed analysis.
**Artifact**: `trace/migration/sim-salesorderv2-to-v3-2026-03-14.md`
**Example**:
```
User: /trace:migration
> Migration: SalesOrderHeaderV2 -> V3 (F&O 10.0.40)
> Pre-state: 145K records, 12 dual-write maps, 3 flows, 1 report

Schema changes:
  Renamed: 4 fields | Removed: 2 fields | Added: 6 fields | Type changed: 1 field

| Consumer | Type | References | Status |
|----------|------|------------|--------|
| DW Map 1-8 | Dual-write | SalesOrderNumber | BROKEN (renamed) |
| DW Map 9-10 | Dual-write | CustomerAccount | BROKEN (renamed) |
| DW Map 11-12 | Dual-write | Common fields only | PASS |
| OrderSync flow | Power Automate | SalesOrderNumber, CustomerAccount | BROKEN |
| OrderApproval flow | Power Automate | StatusCode | PASS |
| OrderExport flow | Power Automate | SalesOrderLines (nav prop) | PASS |
| Monthly Report | SSRS | LegacyOrderType | BROKEN (field removed) |

Findings:
  P1: 10/12 dual-write maps fail -- real-time order sync down until maps updated
  P2: OrderSync flow enters failed state -- requires manual reactivation
  P3: Report silently breaks -- groups all orders under "(blank)"
```

---

### /trace:permissions

**What**: Hand-compile a permission chain from user identity through security roles, teams, business unit hierarchy, field-level security, and conditional access to determine whether a specific user can perform a specific action on a specific record.
**Validated by**: Dataverse developer (5/5 -- "security roles, teams, field-level security, BU scoping"), Customer Service (5/5 -- "routing, queue access, knowledge access"), Finance frontend (4/5 -- "segregation of duties is a legal requirement"), Sales developer (4/4 -- "territory-based access, hierarchy security")
**Input**: The user identity (name, business unit, teams, security roles), the action (Create, Read, Update, Delete, Append, AppendTo, Share, Assign), the target record (entity, record ID, owner, business unit), and optionally the specific fields involved.
**Output**: Permission trace artifact (decision chain: identity -> role resolution -> privilege check -> scope evaluation -> field-level security -> conditional access -> ALLOW/DENY with reasoning at each step) with findings on over-permissioning, gaps, and segregation-of-duties violations.
**Lifecycle**:
- Setup: Identify the permission question. User: Sarah Chen, Business Unit: West Region, Teams: Sales Team West (owner team), Marketing Collaboration (access team). Security roles: Salesperson (BU-level), Marketing Reader (org-level read only). Action: Update the "estimatedrevenue" field on Opportunity record OPP-4521 (owner: James Park, BU: West Region). Select roles (Dataverse Security Admin, Compliance Officer).
- Execute: Hand-compile the permission chain.
  Step 1 -- Role resolution: Sarah has 2 roles. Salesperson role grants Update on Opportunity at Business Unit scope. Marketing Reader grants Read on Opportunity at Organization scope. For Update, Salesperson is the relevant role.
  Step 2 -- Entity-level privilege: Salesperson role has "Update" privilege on Opportunity entity? YES. Privilege depth: Business Unit (user's BU + child BUs).
  Step 3 -- Record scope: Opportunity OPP-4521 is in BU "West Region". Sarah is in BU "West Region". Same BU. BU-level privilege covers same-BU records. PASS.
  Step 4 -- Ownership check: Record owner is James Park (same BU). Sarah is not the owner. Salesperson role at BU level grants update to records owned by users in the same BU. PASS.
  Step 5 -- Team membership: Sales Team West is an owner team in BU West Region. If OPP-4521 were owned by the team, Sarah would have team-level access. Not applicable here (record owned by James, not the team).
  Step 6 -- Field-level security: Is "estimatedrevenue" protected by a field security profile? CHECK. Field security profile "Revenue Fields" exists. Profile grants: Read=YES, Update=YES to role "Salesperson". Sarah has the Salesperson role. PASS.
  Step 7 -- Sharing: No explicit sharing records on OPP-4521 for Sarah. Not needed (BU-level access already granted).
  Step 8 -- Conditional Access (Entra): Conditional access policy "Block External Updates" requires: device compliance=managed, location=corporate network OR VPN. Sarah's current session: managed device, VPN connected. PASS.
  Final decision: ALLOW. Sarah can update estimatedrevenue on OPP-4521.
- Findings: P1: Sarah's Salesperson role grants BU-level Update on ALL opportunity fields, including "actualrevenue" and "closeddate" which should only be modifiable by the CloseOpportunity API. A user with BU-level Update can directly edit these fields, bypassing the WinOpportunity/LoseOpportunity workflow. This is a segregation-of-duties gap. P2: The Marketing Reader role grants Organization-level Read on Opportunity -- Sarah can read every opportunity in the entire organization, including competitors' deals in the East Region BU. This is likely over-permissioned for a regional salesperson. P3: Field security profile "Revenue Fields" grants Update to the entire "Salesperson" role -- this means every salesperson can modify revenue fields on any opportunity in their BU scope, including overriding AI-generated revenue predictions.
- Amend: Security admin reviews: "actualrevenue and closeddate should have field-level security with Update restricted to the 'Sales Manager' role only. Add that profile." Re-trace with updated field security: Step 6 now blocks Sarah from updating actualrevenue (field security profile denies Update for Salesperson role). P1 resolved. Admin also notes: "Marketing Reader at org-level is intentional for cross-region collaboration -- this is accepted risk." P2 marked as accepted.
**Lightweight**: --quick resolves the ALLOW/DENY decision with the top-level reason, no field-level security or conditional access evaluation.
**Artifact**: `trace/permissions/sim-opportunity-update-revenue-2026-03-14.md`
**Example**:
```
User: /trace:permissions
> User: Sarah Chen (BU: West Region, Roles: Salesperson, Marketing Reader)
> Action: Update "estimatedrevenue" on Opportunity OPP-4521 (Owner: James Park, BU: West)

| Step | Check | Input | Result |
|------|-------|-------|--------|
| 1 | Role resolution | 2 roles | Salesperson grants Update (BU scope) |
| 2 | Entity privilege | Update on Opportunity | YES |
| 3 | Record scope | Record BU=West, User BU=West | PASS (same BU) |
| 4 | Ownership | Owner=James (same BU) | PASS (BU-level covers) |
| 5 | Team membership | Not applicable | SKIP |
| 6 | Field-level security | estimatedrevenue in "Revenue Fields" profile | PASS (Salesperson has Update) |
| 7 | Sharing | No sharing records | N/A |
| 8 | Conditional Access | Managed device + VPN | PASS |

Decision: ALLOW

Findings:
  P1: actualrevenue/closeddate unprotected -- bypasses WinOpportunity workflow
  P2: Marketing Reader grants org-wide Read -- over-permissioned for regional seller
  P3: Revenue field security too broad -- all salespersons can override AI predictions
```

## Roles

### Stock roles

Selection logic: /trace: skills auto-select roles based on the platform layer being traced. The system matches against service boundary keywords in the request/operation description.

| Trace keywords | Primary role | Secondary role |
|---------------|-------------|----------------|
| OData, Web API, Plugin, Message pipeline | Dataverse Platform Engineer | API Designer |
| CSU, CRT, POS, CDX, Channel DB | Commerce Platform Engineer | Retail Architect |
| Cloud flow, Trigger, Action, Connector | Power Automate Platform Engineer | Integration Architect |
| Topic, Agent, Knowledge, Orchestrator | Copilot Studio Platform Engineer | Conversation Architect |
| X++, Data entity, LCS, Batch, AOS | F&O Platform Engineer | Release Manager |
| Security role, BU, Field security, RBAC | Dataverse Security Admin | Compliance Officer |
| Solution, Managed layer, Import, Publish | Dataverse Platform Engineer | Release Manager |

### Custom roles (optional)

/trace:request benefits from adding a Performance Engineer role when latency is the primary concern -- they focus on per-layer latency budgets and bottleneck identification. /trace:permissions benefits from adding a Compliance Officer role for regulated industries (finance, healthcare) where segregation of duties is a legal requirement. /trace:deployment benefits from adding a DevOps Engineer role who knows the CI/CD pipeline and can validate that the deployment artifact was built correctly before tracing the import.

## Artifacts

```
trace/
  request/
    sim-{operation-slug}-{date}.md       # e.g., sim-create-account-2026-03-14.md
  state/
    sim-{entity}-{scenario-slug}-{date}.md  # e.g., sim-case-sla-lifecycle-2026-03-14.md
  contract/
    sim-{contract-slug}-{date}.md        # e.g., sim-weather-connector-getforecast-2026-03-14.md
  component/
    sim-{surface}-{action-slug}-{date}.md   # e.g., sim-opportunity-kanban-stage-2026-03-14.md
  deployment/
    sim-{artifact-slug}-{date}.md        # e.g., sim-contoso-sales-v120-2026-03-14.md
  migration/
    sim-{migration-slug}-{date}.md       # e.g., sim-salesorderv2-to-v3-2026-03-14.md
  permissions/
    sim-{entity}-{action-slug}-{date}.md    # e.g., sim-opportunity-update-revenue-2026-03-14.md
```

Naming convention: `sim-{descriptive-slug}-{YYYY-MM-DD}.md`. Slugs are lowercase, hyphenated, derived from the system surface being traced.

## Technique Heritage

/trace: is directly powered by the three proven simulation techniques from the craftworks evidence corpus. Hand-compilation is the core method; state-operation-outcome and three-directory provide the structural patterns for specific skills.

| Skill | Primary technique | Evidence | Natural fit score |
|-------|------------------|----------|-------------------|
| request | 01 Hand-Compilation | Layer-by-layer trace is the same pattern as compiler pass tracing. `simulate/techniques/01-hand-compilation/README.md` -- 730+ scenarios across Astro/Craft/Flows. | 4.7/5 |
| state | 02 State-Operation-Outcome | Starting state -> operation -> expected outcome is exactly the SOO pattern. `simulate/techniques/02-state-operation-outcome/README.md` -- 199 scenarios across 6 admin series. | 4.7/5 |
| contract | 03 Three-Directory | Expected vs actual comparison is the 20+expected / 30+actual pattern. `simulate/techniques/03-three-directory/README.md` -- 24 scenarios in Flash. | 4.7/5 |
| component | 01 Hand-Compilation | Event chain tracing through a component tree is compiler pass tracing applied to UI. Same methodology, different domain. | 4.7/5 |
| deployment | 02 State-Operation-Outcome + 01 Hand-Compilation | Deployment is a state transition (pre-deploy -> deploy -> post-deploy) traced through multiple phases. | 4.7/5 |
| migration | 03 Three-Directory + 02 State-Operation-Outcome | Pre-migration state is "input", expected post-migration state is "expected", actual is "actual". Combined with SOO for the migration operation itself. | 4.7/5 |
| permissions | 02 State-Operation-Outcome | Permission evaluation is a state machine: identity state -> privilege evaluation -> scope resolution -> ALLOW/DENY outcome. | 4.7/5 |

## Cross-Namespace Integration

| /trace: output | Feeds into | How |
|---------------|-----------|-----|
| request findings | /flow:lifecycle | Latency bottlenecks and failure points discovered in a request trace become constraints in the process lifecycle simulation (e.g., "step 3 takes 2 seconds because of the DuplicateDetection query"). |
| state findings | /review:design | State machine gaps (missing transitions, unhandled statuses) become design review items for the specification that defines the entity lifecycle. |
| contract findings | /flow:integration | Schema drift discovered in contract testing becomes the input for re-simulating the integration that consumes the drifted contract. |
| component findings | /listen:feedback | UI event chain issues (confusing validation, delayed updates) become dimensions for simulating user reactions in /listen:feedback. |
| deployment findings | /program:plan | Deployment risks (breaking changes, layer conflicts, auto-activation) become gates in a /program:plan -- "deployment trace must show 0 P1 findings before production push." |
| migration findings | /flow:dataflow | Integration consumers broken by a migration become the scope for a /flow:dataflow re-simulation to validate the updated pipeline. |
| permissions findings | /review:security | Over-permissioning and segregation-of-duties gaps become security review items with specific remediation recommendations. |
