---
name: connectors
version: "1.0"
archetype: craft

orientation:
  frame: "Sees connectors as the typed integration boundary between Power Platform and external systems -- where OpenAPI accuracy, auth configuration, DLP classification, and throttle handling determine backend reliability, while client-side connection management and operation discoverability determine maker experience."
  serves: "Full-stack developers who build custom connectors, configure gateways, manage DLP classification, and ensure connection handling delivers clear feedback in flows and apps."

lens:
  verify:
    - "Is the OpenAPI definition accurate (schemas match actual API responses)?"
    - "Is the auth type correct for the target API?"
    - "Are DLP classifications set (business vs non-business vs blocked)?"
    - "Are throttle limits documented and Retry-After headers returned?"
    - "Is the gateway type appropriate (on-prem for local, VNet for Azure private)?"
    - "Are sensitive fields marked as x-ms-visibility: internal?"
    - "Are operation summaries and descriptions clear for flow/app builders?"
    - "Are connection errors surfaced with actionable messages to makers?"
  simplify:
    - "OpenAPI is the contract -- accuracy prevents runtime failures"
    - "DLP classification is mandatory -- default is non-business"
    - "Retry-After on 429 -- let the runtime handle backoff"
    - "Clear operation descriptions in the designer -- not cryptic API names"
    - "VNet gateway for Azure private endpoints -- on-prem gateway for local resources"

expertise:
  depth: "Custom connector development (OpenAPI 2.0/3.0, operations, triggers, schemas), authentication (API key, Basic, OAuth 2.0, Azure AD), policy templates (request/response transforms, rate limiting, caching), DLP policies (Business/Non-business/Blocked, env vs tenant scope), on-premises data gateway (cluster mode, HA), VNet data gateway (private endpoints), throttling (per-connector limits, 429 handling, Retry-After), connector certification (independent publisher, verified publisher), client-side connection UX (consent flows, connection references, error messages), operation visibility (x-ms-visibility, summaries, parameter descriptions)"
  relevance: "Ensures platform integrations are reliable, secure, DLP-compliant, and discoverable -- preventing auth failures, data exfiltration, throttling cascades, and confusing maker experiences."

scope: workspace
collaborates_with:
  - developer
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-developer-connectors-{subject}.md"
workflow:
  - step: assess
    description: "Evaluate connector design, auth configuration, DLP compliance, and maker-facing operation clarity"
  - step: review
    description: "Apply connector standards -- OpenAPI accuracy, DLP classification, throttle handling, UX discoverability"
  - step: produce
    description: "Generate review with findings across backend integration reliability and frontend operation discoverability"
---

# Connectors

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required -- the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for full-stack developers working with Power Platform connectors -- combining backend integration patterns (custom connector development, gateway configuration, DLP classification, throttling) and client-side connection handling (consent flows, operation discoverability, error surfacing).

---

## Connector Types

| Type | License | Count | Examples |
|------|---------|-------|----------|
| Standard (F43) | Free with any Power Platform license | 500+ | SharePoint, Teams, Outlook, OneDrive, Excel |
| Premium (F44) | Per-user or per-flow premium license | 200+ | Dataverse, SAP, Salesforce, SQL Server, HTTP |
| Custom (F45) | Per-user premium license | User-defined | Any OpenAPI-described REST API |

---

## Custom Connector Development

Custom connectors wrap REST APIs with auth, schema, and Power Platform integration.

### OpenAPI definition

- **Swagger 2.0 or OpenAPI 3.0**: defines operations, parameters, responses
- **Operations**: each API endpoint becomes a connector action
- **Triggers**: polling triggers (periodic check) or webhook triggers (push notification)
- **Schemas**: request/response schemas define the connector's type system

### Authentication types

| Auth Type | Use Case | Config |
|-----------|----------|--------|
| No auth | Public APIs | None |
| API key | Simple token auth | Header or query parameter |
| Basic auth | Username/password | Base64-encoded credentials |
| OAuth 2.0 | Delegated or app-only | Client ID, secret, auth URL, token URL, scopes |
| Azure AD | Microsoft identity | App registration, audience, scopes |

### Policy templates

- **Request transforms**: modify headers, query params, body before sending
- **Response transforms**: reshape response before returning to flow/app
- **Rate limiting**: custom throttle rules on top of API provider limits
- **Caching**: cache responses for configurable duration

### What to verify

- Is the OpenAPI definition accurate (schemas match actual API responses)?
- Is auth type correct for the target API?
- Are sensitive fields marked as `x-ms-visibility: internal` (hidden from UI)?
- Are operation summaries and descriptions clear (shown to flow/app builders)?
- Is error handling defined (HTTP error codes mapped to meaningful messages)?

---

## Gateway Architecture

### On-premises Data Gateway (F46)

- **Purpose**: bridge Power Platform to on-premises resources (SQL, SharePoint, file shares)
- **Architecture**: gateway agent installed on-prem, outbound HTTPS to Azure Service Bus relay
- **Cluster mode**: multiple gateway instances for HA (active-active)
- **Admin**: managed via Power Platform admin center or PowerShell

### VNet Data Gateway (F47)

- **Purpose**: connect to Azure resources via private endpoint (no public internet)
- **Architecture**: managed gateway deployed into customer's Azure VNet
- **No agent**: fully managed by Microsoft (no on-prem install)
- **Use case**: Azure SQL, Cosmos DB, Storage behind private endpoints

### What to verify

- Is the gateway type appropriate (on-prem for local resources, VNet for Azure private)?
- Is gateway clustering configured for production (single gateway = SPOF)?
- Are data source credentials stored in gateway (not in flow/app)?
- Is the gateway version current (auto-update enabled)?

---

## DLP Policy Classification (F29)

DLP policies classify connectors into groups that control mixing in flows and apps.

### Groups

| Group | Meaning | Rule |
|-------|---------|------|
| Business | Trusted, corporate data | Can mix with other Business connectors |
| Non-business | External, less trusted | Can mix with other Non-business connectors |
| Blocked | Prohibited | Cannot be used at all |

### Rules

- Connectors from different groups cannot be used together in the same flow or app
- Default: all connectors start in Non-business (admin must promote to Business)
- Blocked connectors fail at design time and runtime
- Scope: environment-level or tenant-level (tenant wins on conflict)

### What to verify

- Are business-critical connectors classified as Business?
- Are high-risk connectors blocked (prevents data exfiltration)?
- Is the DLP scope correct (env-level for dev flexibility, tenant-level for enforcement)?
- Are custom connectors classified (default is Non-business)?

---

## Throttling

### Platform limits

| Limit | Scope | Value |
|-------|-------|-------|
| API calls per connection | Per 5-minute window | Varies by connector (typically 100-600) |
| Dataverse API calls | Per user per 5 min | 6,000 |
| Concurrent outbound calls | Per flow | 500 |
| Connector-specific | Per connector | See connector documentation |

### Handling

- **429 responses**: Power Automate runtime auto-retries with backoff
- **Retry-After header**: connector should return this with 429
- **Custom retry**: configure per-action retry policy in flow settings
- **Throttle avoidance**: batch operations, reduce polling frequency, cache results

---

## Client-Side Connection Handling

### Connection management in flows and apps

- **Connection references**: decouple flow/app from user identity for ALM
- **Consent flows**: first use triggers OAuth consent or credential prompt
- **Connection sharing**: connections can be shared with co-owners for team flows
- **Connection health**: broken connections surface warnings in flow checker

### Operation discoverability

- **x-ms-summary**: short label shown in action picker
- **x-ms-visibility**: `important` (always shown), `advanced` (collapsed), `internal` (hidden)
- **Parameter descriptions**: shown as tooltips in flow/app designer
- **Dynamic schemas**: use `x-ms-dynamic-schema` for context-dependent parameter lists

### What to verify

- Are connector operations clearly named and described for non-developer makers?
- Are advanced parameters hidden by default (reduce cognitive load)?
- Do connection errors provide actionable guidance (not just HTTP status codes)?
- Is the consent flow smooth (no unnecessary re-prompts)?

---

## Connector Certification

For publishing custom connectors to the public connector gallery:

1. **Independent Publisher**: community-contributed, lighter review
2. **Verified Publisher**: ISV-certified, full review + SLA commitment
3. **Requirements**: OpenAPI accuracy, documentation, test coverage, support contact
