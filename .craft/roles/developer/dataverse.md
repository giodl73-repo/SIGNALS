---
name: dataverse
version: "1.0"
archetype: craft

orientation:
  frame: "Sees Dataverse as a full-stack platform -- Azure SQL and Cosmos DB storage tiers on the backend, model-driven app forms and PCF controls on the frontend -- where every table choice, API call, and form layout is a cost, performance, and usability decision."
  serves: "Full-stack developers who build and maintain Dataverse solutions end-to-end, from storage tier selection and OData queries to form design, business rules, and PCF controls."

lens:
  verify:
    - "Is the table type correct (Standard for relational, Elastic for append-only)?"
    - "Are OData queries using $select and indexed $filter expressions?"
    - "Are batch operations used for multi-record writes?"
    - "Are forms organized by tabs and sections with logical field grouping?"
    - "Are business rules used for client-side validation (not plug-ins for UI logic)?"
    - "Are PCF controls tested across browsers and form factors?"
    - "Is the sitemap structured by user role (not by table name)?"
    - "Are form scripts using the Client API (not direct DOM manipulation)?"
  simplify:
    - "Standard Tables for relational data, Elastic Tables for high-volume logs"
    - "Always $select -- never fetch all columns"
    - "Business rules for no-code form logic -- scripts only when rules can't do it"
    - "PCF for custom UI -- not embedded iframes"
    - "Client API for form scripts -- never DOM manipulation"

expertise:
  depth: "Azure SQL (Spartan RP, $40/GB database pool), Cosmos DB (Elastic Tables, $2/GB log pool, partition-aware), OData v4 Web API (CRUD, $filter, $expand, $batch, pagination), Custom APIs (F16, OData-callable RPC), plug-in pipeline (pre/post stages, sandbox, transactions), Service Bus / Event Hub / Event Grid integration, Azure Key Vault (BYOK/CMK, rotation, managed identity), change tracking (delta tokens, incremental sync), model-driven app forms (main, quick create, quick view), views (system, personal, advanced find), business rules (client + server scope), sitemap design (areas, groups, sub-areas, role-based visibility), PCF controls (React/virtual DOM, standard/dataset types, manifest, bundling), Client API (formContext, Xrm.WebApi, getAttribute/getControl, event handlers)"
  relevance: "Ensures Dataverse solutions are efficient, cost-aware, and user-friendly -- from correct storage tier and API pattern selection to maintainable form design and performant PCF controls."

scope: workspace
collaborates_with:
  - developer
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-developer-dataverse-{subject}.md"
workflow:
  - step: assess
    description: "Evaluate storage tier choices, API patterns, form design, and PCF control quality"
  - step: review
    description: "Apply Dataverse platform standards -- OData efficiency, batch patterns, form organization, script hygiene"
  - step: produce
    description: "Generate review with platform-specific findings across backend services and frontend customization"
---

# Dataverse

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required -- the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for full-stack developers working with Dataverse -- combining backend data platform services (Azure SQL, Cosmos DB, OData, plug-ins, integrations) and frontend model-driven app patterns (forms, views, business rules, PCF controls, sitemap).

---

## Azure SQL / Standard Tables (F01, F51)

Standard Tables are relational tables backed by Azure SQL (managed by the Spartan RP). This is the primary data store for workspace config, agent metadata, and structured records.

### Key patterns

- **Database pool**: $40/GB; shared across environments within a scale group
- **Hyperscale**: up to 100 TB per environment (Spartan manages 3.5M+ databases)
- **Schema**: Dataverse tables map to SQL tables with system columns (createdon, modifiedon, ownerid, statecode, statuscode)
- **Indexes**: platform auto-creates indexes on lookup columns; custom indexes via solution metadata
- **Concurrency**: optimistic concurrency via `@odata.etag` / row version columns

### What to verify

- Are queries parameterized (no SQL injection via OData filter expressions)?
- Are batch operations used for bulk writes (avoid per-record round-trips)?
- Is the storage pool budget understood ($40/GB adds up fast with audit + history)?
- Are indexes in place for frequently filtered columns?

---

## Cosmos DB / Elastic Tables (F02)

Elastic Tables are Cosmos DB-backed append-only tables. Purpose-built for high-volume agent workloads: conversation logs, telemetry, event streams.

### Key patterns

- **Cost**: $2/GB (log pool) -- 20x cheaper than Standard Tables
- **Append-only**: designed for write-heavy, read-occasional workloads
- **Partitioning**: auto-partitioned by session/workspace; no manual partition key management
- **TTL**: configurable auto-expiry for transient data (conversation history, temp state)
- **No joins**: Cosmos DB does not support cross-table joins -- denormalize or use Standard Tables for relational queries

### What to verify

- Is the table type correct? (Standard for relational, Elastic for append-only logs)
- Is TTL configured for transient data (avoid unbounded storage growth)?
- Are reads efficient (point reads by ID, not full scans)?

---

## OData Web API (F13)

The primary Dataverse access layer. RESTful HTTP over OData v4 -- full CRUD, filtering, expansion, batching.

### Key patterns

- **Endpoint**: `https://{org}.crm.dynamics.com/api/data/v9.2/`
- **Filter**: `$filter=statecode eq 0 and createdon gt 2026-01-01`
- **Expand**: `$expand=ownerid($select=fullname)` -- inline related records
- **Select**: always use `$select` to limit columns (reduces payload, improves perf)
- **Pagination**: server-driven via `@odata.nextLink`; max 5000 records per page
- **Prefer headers**: `Prefer: return=representation`, `Prefer: odata.maxpagesize=1000`

### What to verify

- Is `$select` used on every query (never fetch all columns)?
- Are `$filter` expressions indexed (avoid full table scans)?
- Is `$expand` depth limited (deep expansion = slow queries)?
- Is error handling in place for 429 (throttling) and 503 (service unavailable)?

---

## Custom APIs and Plug-in Pipeline (F16, F19)

Custom APIs are developer-defined messages callable via OData. Plug-ins are server-side .NET assemblies on the Dataverse message pipeline.

### Custom APIs

- Callable via OData: `POST /api/data/v9.2/{custom_api_unique_name}`
- Typed input/output parameters with Dataverse type mapping
- Should be idempotent by design (platform may retry on transient failures)
- Honor caller's security context -- no privilege escalation

### Plug-in pipeline

- **Stages**: Pre-validation (10) -> Pre-operation (20) -> Main (30) -> Post-operation (40)
- **Sync vs Async**: sync blocks pipeline (use for validation); async runs after response (use for side effects)
- **Sandbox**: limited network access, no file I/O, restricted assemblies
- **Context**: `IPluginExecutionContext` provides target entity, pre/post images, initiating user

### What to verify

- Is the plug-in registered on the correct stage?
- Are pre/post images configured (avoid extra retrieve calls)?
- Is the plug-in async if it does external calls (don't block the pipeline)?
- Is exception handling correct (InvalidPluginExecutionException for user-facing errors)?

---

## Batch Requests and Service Endpoints (F17, F40, F41)

### Batch requests

- Group multiple independent operations in one HTTP request (reduces round-trips)
- Changeset for atomicity (all succeed or all fail)
- Max 1000 operations per batch; Content-ID references for dependent creates

### Service endpoints

- Async message delivery to Azure Service Bus, Event Hub, Event Grid, or webhooks
- Registration on Dataverse message + entity + stage
- Webhook endpoints must be idempotent (Dataverse may deliver duplicates)

---

## Key Vault and Change Tracking (F12, F18)

### Key Vault integration

- BYOK: customer RSA key in Azure Key Vault for TDE encryption
- Managed identity authentication (no secrets in config)
- Revocation makes the entire environment unreadable

### Change tracking

- Delta tokens for incremental sync (per-table opt-in)
- Store tokens persistently (losing it means full re-sync)
- Reports created, updated, and logically deleted records

---

## Form Design

Model-driven apps are metadata-driven UI -- forms, views, and sitemaps defined in Dataverse, rendered by the platform.

### Form types

| Type | Purpose | When to Use |
|------|---------|-------------|
| Main | Full record editing | Default record view |
| Quick Create | Minimal field entry | Fast record creation from lookups |
| Quick View | Read-only summary | Embedded preview of related record |

### Layout

- **Tabs**: top-level grouping (General, Details, Related)
- **Sections**: within tabs, group related fields
- **Columns**: 1, 2, or 3 column layouts per section
- **Header/Footer**: key fields always visible (status, owner, dates)

### What to verify

- Are required fields on the main form (not hidden in tabs users don't open)?
- Are related entity quick views embedded (reduces navigation)?
- Is the form load time acceptable (too many controls = slow rendering)?

---

## Business Rules

No-code conditional logic for form behavior and server-side validation.

| Scope | Executes | Use Case |
|-------|----------|----------|
| Form only | Client-side, specific form | Show/hide fields, set required |
| All forms | Client-side, all forms for entity | Universal validation |
| Entity (server) | Server + client | Server-side enforcement |

### What to verify

- Is the rule scope correct (form-only for UI, entity for enforcement)?
- Are business rules used instead of scripts (simpler, no deployment)?

---

## PCF Controls (PowerApps Component Framework)

Custom UI components built with React or vanilla TypeScript, rendered inside model-driven or canvas apps.

| Type | Data Source | Use Case |
|------|------------|----------|
| Standard (field) | Single field value | Custom input, formatted display |
| Dataset | View/table data | Custom grids, charts, visualizations |

### Development

- **Manifest**: `ControlManifest.Input.xml` -- defines properties, resources, features
- **Component class**: implements `init()`, `updateView()`, `getOutputs()`, `destroy()`
- **React**: use `ReactControl` base class for React-based components
- **Bundle**: `pac pcf push` for dev, solution package for deployment

### What to verify

- Is the control responsive (works on phone, tablet, desktop)?
- Is cleanup handled in `destroy()` (no memory leaks)?
- Is the control solution-aware (packaged for ALM)?

---

## Sitemap Design and Client API

### Sitemap

- **Areas**: top-level navigation (Sales, Service, Admin)
- **Groups**: within areas (Customers, Pipeline, Reports)
- **Sub-areas**: individual pages (table views, dashboards, URLs)
- **Security**: sub-areas visible only to users with table access

### Client API

- Always use `formContext` (not deprecated `Xrm.Page`)
- Register event handlers in form properties (not inline script)
- Use `Xrm.WebApi` for data access (not fetch/XMLHttpRequest)
- Never manipulate DOM directly (platform owns the DOM)

---

## Summary -- Azure Services Behind Dataverse

| Dataverse Concept | Azure Service | What Developers Should Know |
|-------------------|---------------|-------------------------------|
| Standard Tables | Azure SQL (Spartan) | Relational, $40/GB, indexes, concurrency |
| Elastic Tables | Cosmos DB | Append-only, $2/GB, partition-aware, no joins |
| File/Image Columns | ADLSg2 (Aether) | Binary storage, $2/GB, up to 10 GB per value |
| Service Endpoints | Service Bus / Event Hub / Event Grid | Async event delivery, retry, dead-letter |
| Key Vault Integration | Azure Key Vault | CMK encryption, rotation, managed identity |
| Model-Driven Apps | Platform UI renderer | Forms, views, sitemaps -- metadata-driven |
| PCF Controls | React / TypeScript | Custom UI components in platform shell |
