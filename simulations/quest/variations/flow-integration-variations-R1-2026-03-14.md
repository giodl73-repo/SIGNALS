Written to `simulations/quest/variations/flow-integration-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- flow-integration

**5 variations, 3 single-axis + 2 combined:**

| V | Axis | Core mechanism | C-04 guarantee |
|---|------|----------------|----------------|
| **V-01** | Output format: per-call table | Fixed columns map to C-01--C-04; one row per call | `Error disposition` column cannot be blank |
| **V-02** | Role sequence: sequential domain experts | Integration Architect -> Reliability Engineer -> Security Engineer | Reliability Engineer reviews every INT-NN from Pass 1 for error fate |
| **V-03** | Phrasing register: imperative | Four numbered commands per call; no table structure | Step 3 is a discrete, non-mergeable imperative |
| **V-04** | Role sequence + Lifecycle: gated phases | Five gates (INVENTORY -> AUTH -> FORMAT -> ERROR -> RATE+IDEMPOTENCY) | Phase 4 is dedicated solely to error-disposition; no other concern allowed |
| **V-05** | Output format + Inertia framing: table + "Happy path only?" column | Pre-stated happy-path baseline; per-row column flags calls with no hardening beyond the success case | Error disposition column + "Happy path only?" column make error-swallowing doubly visible |

**Inertia framing translation:** The status-quo competitor is the **happy-path integration** -- built and tested under ideal conditions, never hardened for auth expiry, rate limits, or transient failures. V-05 makes this assumption explicit before any row is filled, then forces "Yes -- gap / Partial -- gap / No" per call. "Yes -- gap" rows do triple duty: they flag C-04 (error handling), C-05 (rate limit), and C-06 (retry/idempotency) simultaneously.

**Predicted V-golden candidates:** V-04 for aspirational depth (Phase 4 gate produces call-specific error detail that feeds C-09 remediation quality). V-05 for gap inventory completeness (structural findings cannot be omitted from GAP INVENTORY). V-01 as the control -- if it reaches golden without gates or role sequence, the added complexity is not justified.
e under happy-path conditions, then determines whether each call's actual design exceeds that baseline. Calls that match the baseline are integration hardening gaps.

**Predicted ceiling:** V-01 and V-05 (table columns cannot be skipped). V-05 is richer if happy-path framing improves C-06 depth and gap inventory (C-07) completeness. V-04 is strongest for aspirational C-08/C-09 via gated phase structure. V-03 is the minimum-structure floor test.

---

## V-01: Per-Call Table

**Axis:** Output format -- pre-printed 5-column table with columns mapped directly to C-01--C-04; one row per call; supplementary sections for rate limits, retry/idempotency, gap inventory, and severity
**Hypothesis:** A pre-printed table whose columns correspond to the four essential criteria physically cannot omit auth or error-disposition for any call: a blank cell is a visible, detectable gap. The supplementary sections are pre-printed to guarantee C-05, C-06, C-07 surface even when the per-call table is complete. Tests whether table structure is sufficient to guarantee essential criterion coverage without gating, phasing, or imperative instruction.

```
You are running /flow-integration. Fill in the pre-printed template below.
All column headers are fixed. Fill in every cell for every call row. Do not add, rename,
reorder, or remove any column. Do not leave any cell blank.

---

## CALL INVENTORY TABLE

[Read all column instructions before filling in any row.]

Column instructions:
- **Call ID** (C-01): Assign a sequential ID: INT-01, INT-02, etc. Use this ID in all subsequent
  sections.
- **System + protocol** (C-01): Named target system and protocol. E.g., "Salesforce REST API",
  "Azure Service Bus AMQP", "MCP tool: calendar-read", "Dataverse OData v4". "The API" is not a
  name.
- **Call type** (C-01): Choose one: Create / Read / Update / Delete / Event publish /
  Event subscribe / Webhook callback / Token acquire / Health check / Other:[specify].
- **Auth mechanism** (C-02): How this call authenticates: API key (header/query param name),
  OAuth 2.0 Bearer (flow: client credentials / auth code / on-behalf-of), service identity
  (MSI/managed identity), shared secret (location: [env/vault/config]), none (public endpoint --
  state intentional), or Unknown -- gap.
- **Error disposition** (C-04): What happens when this call fails: Surfaced (returned to caller) /
  Transformed (caught; raises [signal]) / Retried ([strategy: interval/exponential], max [N]) /
  Swallowed (logged; execution continues -- gap) / No handling -- gap. Do not write "handles
  errors" without a disposition type.

| Call ID | System + protocol | Call type | Auth mechanism | Error disposition |
|---------|-------------------|-----------|---------------|-------------------|
| INT-01  | [Name + protocol] | [Type]    | [Mechanism or "Unknown -- gap"] | [Disposition or "No handling -- gap"] |
| INT-02  | [Name + protocol] | [Type]    | [Mechanism or "Unknown -- gap"] | [Disposition or "No handling -- gap"] |
[Add one row per distinct cross-system call. Include: direct API calls, MCP tool invocations,
connector actions, event publishes, event subscribes, webhook callbacks, token acquisition calls,
health checks. Include calls that are "background" or "assumed to work." Minimum two rows.]

---

## REQUEST AND RESPONSE FORMAT

[Required. One entry per Call ID from the table above. Do not omit any call. Partial schemas are
acceptable -- note incompleteness explicitly.]

**[INT-NN] -- [System + protocol]**
- Method: [HTTP method or protocol operation: GET / POST / PUT / DELETE / PUBLISH / SUBSCRIBE / etc.]
- Key request headers: [List headers that affect routing, auth, content type, or idempotency.
  At minimum: Authorization (type), Content-Type. Note any X-Idempotency-Key or correlation headers.]
- Body key fields: [List the fields that must be present in the request body. Write "No body" for
  side-effect-free reads. Note schema incompleteness if partial.]
- Expected response: [Status code(s) + key response fields. E.g., "200 with {id, status,
  created_at}". Note error response shape if documented.]

[Repeat for each Call ID. One entry per call is mandatory.]

---

## RATE LIMIT EXPOSURE

[One entry per external system contacted. Systems with no documented rate limit are findings.]

| System | Rate limit documented? | Limit | Burst behavior | Throttle response |
|--------|------------------------|-------|----------------|-------------------|
| [Name] | Yes / No -- exposure   | [Calls/min, calls/day, token budget, or "Unknown"] | [Queued / rejected / delayed / unknown] | [429 + Retry-After / silent drop / unknown] |
[One row per distinct external system. "No -- exposure" rows are findings for GAP INVENTORY.]

---

## RETRY AND IDEMPOTENCY

[One entry per Call ID that can fail transiently. Calls with no retry strategy are findings.
Calls omitted must have a stated reason (e.g., fire-and-forget by design, pure read).]

| Call ID | Retry strategy | Max attempts | Backoff | Jitter | Idempotent? | Mitigation if not |
|---------|---------------|--------------|---------|--------|-------------|-------------------|
| [INT-NN] | Fixed interval / Exponential / None | [N or "none"] | [Factor or "none"] | [Yes / No / N/A] | [Yes / No / Unknown] | [Idempotency key / deduplication / at-most-once / None -- gap] |
[Calls with "None" retry strategy that can fail transiently are findings. Non-idempotent calls
without mitigation are findings.]

---

## GAP INVENTORY

[Collect authentication gaps, rate limit exposures, error-swallowing instances, and missing
idempotency into named findings. Each finding must reference a Call ID or system from above.]

| Finding ID | Call ID / System | Gap type | Description |
|------------|-----------------|----------|-------------|
| GAP-01 | [INT-NN or system] | [Auth gap / Rate limit exposure / Error swallowing / No error handling / Missing retry / Missing idempotency / Unknown auth] | [One sentence describing the specific gap] |
[At minimum: every "Unknown -- gap" auth entry, every "No handling -- gap" or "Swallowed" error
disposition, every "No -- exposure" rate limit row, and every non-idempotent call without
mitigation must appear here.]

---

## SEVERITY AND REMEDIATION

[Assign severity to each finding. For HIGH findings, provide a specific remediation sketch.]

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [One line: why this risk level -- data loss, auth bypass, silent failure, latency spike, etc.] | [HIGH only: specific fix for this call context. E.g., "Add idempotency key header X-Idempotency-Key: {topic}-{call-id}-{timestamp}"; "Implement exponential backoff: initial=1s, factor=2, max=30s, jitter=+-20%"; "Rotate scope from delegated user permission to application permission to avoid token expiry at runtime"] |
[Order: HIGH first, then MEDIUM, then LOW. Leave Remediation blank for non-HIGH findings.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, auth_gaps, error_gaps, rate_limit_gaps,
idempotency_gaps, findings_count, high_severity_count.
```

---

## V-02: Sequential Domain Expert Roles

**Axis:** Role sequence -- three domain experts review the call list in series: Integration Architect (inventory + format), Reliability Engineer (error handling + rate limits + retry), Security Engineer (auth audit + error-propagation security review); each pass operates on the same call IDs established in Pass 1
**Hypothesis:** Sequencing expertise by concern forces deeper per-concern analysis than a single-role walk-through. The Integration Architect's job is documentation completeness (C-01, C-03); the Reliability Engineer's job is operational hardening (C-04, C-05, C-06); the Security Engineer's job is auth correctness and error-propagation risk (C-02, C-07). Each expert reviews all calls, but from a single-concern lens. Tests whether role specialization produces richer per-criterion depth than general-purpose tracing.

```
You are running /flow-integration. Three domain experts will review the integration in sequence.
Each expert operates on the same call list. Complete each expert's review fully before the next
begins. Do not begin a later pass until the previous pass is complete.

---

## PASS 1: INTEGRATION ARCHITECT
Role: Connectors and backend integration domain expert.
Responsibility: Build the definitive call inventory. Document every cross-system boundary
crossing. Document request and response shapes.

### Call Inventory

Enumerate every cross-system call in this integration. A call is any boundary crossing: direct
API invocation, MCP tool call, connector action, event publish, event subscribe, webhook callback,
token acquisition, health check.

For each call, document:
- **Call ID**: INT-01, INT-02, ... (sequential; used in all subsequent passes)
- **Target system**: Named system. E.g., "Salesforce", "Azure Service Bus", "MCP server: calendar".
  "The API" is not a name.
- **Protocol**: REST / AMQP / GraphQL / OData / gRPC / MCP / other
- **Call type**: Create / Read / Update / Delete / Event publish / Event subscribe / Webhook /
  Token acquire / Health check / Other
- **Auth mechanism**: Be specific. API key (header: [name]) / OAuth 2.0 Bearer (flow: [flow]) /
  service identity (MSI) / shared secret (location: [env/vault/config]) / none (public endpoint,
  intentional) / Unknown -- flag as gap.

### Request and Response Format

For each call, document structure. Partial schemas are acceptable -- note incompleteness.

**[INT-NN] -- [System]**
- Method: [operation]
- Key request headers: [Authorization type, Content-Type, idempotency or correlation headers]
- Body key fields: [Required fields. "No body" for side-effect-free reads. Note if schema is partial.]
- Expected response: [Status code + key fields. Note error response shape if documented.]

[Repeat for each Call ID.]

[Pass 1 is complete when every call has a Call ID, system, protocol, call type, auth mechanism,
and request/response shape. Do not begin Pass 2 until this pass is complete.]

---

## PASS 2: RELIABILITY ENGINEER
Role: Systems reliability and fault-tolerance domain expert.
Responsibility: Review each call in the inventory for failure handling, retry behavior, and rate
limit exposure. Reference Call IDs from Pass 1 throughout.

For each Call ID from Pass 1:

**[INT-NN] -- [System]**
- **Error disposition**: What happens when this call fails? Choose one: Surfaced (returned to
  caller unchanged or with context added) / Transformed (caught; raises [signal]) / Retried
  (strategy: [fixed/exponential], interval: [Xms], max: [N], backoff factor: [Y], jitter: [yes/no])
  / Swallowed (logged at [level]; execution continues) / No handling. If Swallowed or No handling:
  flag as GAP.
- **Rate limit**: Is there a documented rate limit for this system? State: calls/min, calls/day,
  token budget. If not documented: "Not documented -- exposure." If the call has retry logic: does
  it respect Retry-After headers?
- **Retry strategy**: Does this call have retry logic? Fixed interval / Exponential backoff
  (initial: [Xms], factor: [Y], max: [Zms]) / None. If the call can fail transiently and has no
  retry: flag as GAP.
- **Idempotency**: Is this call idempotent by design? If not: is there an idempotency key header,
  deduplication mechanism, or at-most-once delivery guarantee? If none: flag as MISSING IDEMPOTENCY.

[Pass 2 is complete when every call has an error disposition, rate limit entry, retry strategy,
and idempotency assessment. Do not begin Pass 3 until this pass is complete.]

---

## PASS 3: SECURITY ENGINEER
Role: API security and authentication domain expert.
Responsibility: Audit auth documentation from Pass 1 and error-handling findings from Pass 2 for
security implications. Flag security-relevant gaps beyond what the previous passes identified.

### Authentication Audit

Review each call's auth mechanism from Pass 1:

| Call ID | Auth mechanism (from Pass 1) | Assessment | Notes |
|---------|------------------------------|------------|-------|
| INT-NN  | [Mechanism]                  | Adequate / Gap / Over-privileged | [Token scope, expiry handling, rotation policy, delegation chain, or gap description] |

Authentication issues to flag:
- Unknown auth mechanisms (Pass 1: "Unknown")
- No auth on non-public endpoints
- Delegated user tokens where application identity would be safer (avoids token expiry failures)
- Token expiry not handled in error path (will produce silent auth failures at runtime)
- Credentials in environment variables without documented rotation

### Error-Propagation Security Review

Review error dispositions from Pass 2 for security implications:

**[INT-NN] -- [System]**
- Does swallowing this error mask an auth failure? [Yes / No -- reason]
- Does surfacing this error leak internal system details? [Yes / No -- reason]
- Is this error distinguishable from a security event (unauthorized vs. unavailable)? [Yes / No]

### Security Gap Summary

| Gap ID | Call ID | Pass | Issue |
|--------|---------|------|-------|
| [S-NN] | INT-NN  | 1/2/3 | [Auth gap / Error masking auth failure / Information leakage / Over-privileged scope] -- [one sentence] |

[Pass 3 is complete when auth audit and error-propagation review are done for all calls.]

---

## GAP INVENTORY

[Collect all gaps flagged in Pass 1, Pass 2, and Pass 3 into a single numbered finding list.
Each finding references its Call ID and the pass where it was identified.]

| Finding ID | Call ID / System | Pass | Gap type | Description |
|------------|-----------------|------|----------|-------------|
| GAP-01 | [INT-NN / system] | [1/2/3] | [Auth gap / Rate limit exposure / Error swallowing / No error handling / Missing retry / Missing idempotency / Security exposure] | [One sentence] |

---

## SEVERITY AND REMEDIATION

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [One-line risk: data loss / auth bypass / silent failure / latency / information leakage] | [HIGH: specific, call-context fix. Not generic advice.] |
[Order: HIGH first, then MEDIUM, then LOW.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, pass_1_gaps, pass_2_gaps, pass_3_gaps,
findings_count, high_severity_count.
```

---

## V-03: Imperative Register

**Axis:** Phrasing register -- four numbered commands per call; direct imperatives replace formal section headers; no pre-printed table structure; call-list gate at the front; findings collected at the end
**Hypothesis:** Direct imperative phrasing ("Name the auth. State the error fate.") eliminates the hedge language and disposition-by-implication that formal descriptive templates invite. The numbered-step framing makes each obligation feel like a discrete action to complete, not a criterion to satisfy. Tests whether register alone -- without table structure or phase gates -- produces four-obligation coverage per call, and whether conversational phrasing reduces error-disposition omission compared to formal templates.

```
You are running /flow-integration.

Trace every cross-system call in this integration. For each call, complete four steps in order.
No skipping steps. No merging steps. No producing Step N+1 output before Step N is done.

---

**Step 0 -- Build the call list before analyzing anything.**

List every cross-system boundary crossing:
- Direct API calls (REST, GraphQL, OData, gRPC)
- MCP tool invocations
- Connector actions
- Event publishes and event subscribes
- Webhook callbacks
- Token acquisition calls
- Health checks

Assign a sequential ID to each call: INT-01, INT-02, etc.
Name the target system. Name the protocol.
Include calls that are "background" or "assumed to work." Include the ones nobody talks about.
If you cannot name the target system: the call is undocumented -- list it as "Unknown system"
and flag it.

Call list:
- INT-01: [System] via [Protocol] -- [Call type]
- INT-02: [System] via [Protocol] -- [Call type]
[Add all calls. Minimum two.]

Do not begin Step 1 until every call is listed here.

---

**For each call in the list, complete these four steps:**

---

**Step 1 -- Name the auth.**

State the authentication mechanism. Use one of these labels:
- API key: state which header or query parameter carries it
- OAuth 2.0 Bearer: state the flow (client credentials / auth code / on-behalf-of)
- Service identity: state the mechanism (MSI / managed identity / workload identity)
- Shared secret: state where it is stored (environment variable / key vault / config file)
- None: acceptable for public endpoints -- state explicitly that this is intentional
- Unknown: this is a gap -- say so

Do not write "authenticated" without a mechanism. Do not write "uses tokens" without a flow.
State how token expiry is handled if applicable (auto-refresh, retry on 401, or not handled).

**Step 2 -- State the request and response shape.**

State the method (GET / POST / PUT / DELETE / PUBLISH / etc.).
List key request headers. At minimum: Authorization (type), Content-Type.
Note any idempotency key header or correlation ID header.
List key request body fields. Write "No body" if none.
State the expected response: status code and key fields.
Note the error response shape if it is documented.

Do not write "sends a request" without stating what is in it.

**Step 3 -- State the error fate.**

What happens when this call fails? Pick one and state it explicitly:
- Surfaced: the error is returned to the caller, unchanged or with added context
- Transformed: the error is caught and a different signal is raised -- state what signal
- Retried: the call is retried -- state the strategy (fixed / exponential), interval, max attempts,
  and whether jitter is applied
- Swallowed: the error is logged or ignored and execution continues -- this is a gap, say so
- No handling: no error handling code exists for this call -- this is a gap, say so

Do not skip this step. Do not write "handles errors" without stating the fate.
"It logs the error" is Swallowed -- name it.

**Step 4 -- State the rate limit and idempotency.**

Does this system have a documented rate limit? State it (calls/minute, calls/day, token budget).
If not documented: say so -- this is a rate limit exposure.
If there is retry logic (from Step 3): does it respect Retry-After headers? State explicitly.
Is this call idempotent by design? If not: is there an idempotency key, deduplication mechanism,
or at-most-once delivery guarantee? If none: flag as missing idempotency.

---

**Work through each call now:**

[INT-01 -- System + Protocol]
Step 1 -- Auth: [FILL IN]
Step 2 -- Request/response: [FILL IN]
Step 3 -- Error fate: [FILL IN]
Step 4 -- Rate limit + idempotency: [FILL IN]

[INT-02 -- System + Protocol]
Step 1 -- Auth: [FILL IN]
Step 2 -- Request/response: [FILL IN]
Step 3 -- Error fate: [FILL IN]
Step 4 -- Rate limit + idempotency: [FILL IN]

[Continue for each call in the list. Use [INT-NN -- System + Protocol] as the section header.]

---

**When all calls are analyzed, collect findings.**

List every gap flagged in Steps 1--4 above. One line per finding:
- [INT-NN]: [Gap type: unknown auth / no error handling / error swallowed / no rate limit documented /
  non-idempotent without mitigation] -- [One sentence: what fails at runtime and when]

Rank by severity. For each HIGH finding, state a concrete fix:
- HIGH: [INT-NN] -- [Why HIGH: data loss / auth bypass / silent failure / cascade] --
  Fix: [Specific action for this call -- not generic advice]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, findings_count, high_severity_count.
```

---

## V-04: Gated Phase Lifecycle

**Axes:** Role sequence + Lifecycle emphasis -- five numbered phases with explicit GATE lines; each phase covers one concern for all calls; no phase output is valid until the previous GATE fires; gating prevents criteria from bleeding or collapsing
**Hypothesis:** Explicitly sequencing the four essential obligations as discrete phases with gate lines prevents the most common omission pattern in per-call trace skills: the model satisfies some criteria by implication while skipping others because they were never independently demanded. Separating auth documentation (PHASE 2) from request/response format (PHASE 3) from error propagation (PHASE 4) makes each obligation a standalone completion event with a visible gate. Tests whether gate-enforced sequencing produces higher per-criterion completeness than integrated per-call templates or table structures.

```
You are running /flow-integration. Execute each phase in order.
A GATE must be satisfied before the next phase begins. Do not skip phases, merge phases, or
produce output from a later phase before the current phase GATE is met.

---

## PHASE 1: CALL INVENTORY

[GATE: Name every cross-system boundary crossing before analyzing any. A call must be specifically
named -- target system, protocol, and call type. "The API" is not a name. Assign sequential IDs:
INT-01, INT-02, etc. Do not document auth, request shapes, or error handling here. Inventory only.]

Cross-system call types to include:
- Direct API calls (REST / GraphQL / OData / gRPC)
- MCP tool invocations
- Connector actions (Power Automate, Logic Apps, etc.)
- Event publishes and subscribes
- Webhook callbacks
- Token acquisition calls
- Health checks
Include calls that are "assumed to work" or only visible on the happy path.
If a call exists but its target system is unknown, list it with system = "Unknown" and note it.

| Call ID | Target system | Protocol | Call type |
|---------|---------------|----------|-----------|
| INT-01  | [Named system] | [REST / AMQP / OData / gRPC / MCP / other] | [Create / Read / Update / Delete / Event publish / Event subscribe / Webhook / Token acquire / Health / Other] |
| INT-02  | [Named system] | [Protocol] | [Type] |
[Add all calls. Minimum two rows required.]

PHASE 1 GATE: All cross-system calls inventoried with ID, system, protocol, and call type.
Proceed to PHASE 2.

---

## PHASE 2: AUTHENTICATION DOCUMENTATION

[GATE: For every call in PHASE 1, state the auth mechanism. This phase documents only auth --
no error handling, no request shapes, no rate limits. Auth only. Every call must have an explicit
entry. "Unknown" is acceptable only if explicitly flagged as a gap here.]

For each call:
- **[INT-NN] -- [System]**
  - Auth mechanism: [API key (header: [name]) / OAuth 2.0 Bearer (flow: [flow]) / service
    identity (MSI / managed identity) / shared secret (location: [env/vault/config]) / none
    (public endpoint, intentional) / Unknown -- gap]
  - Token expiry handling: [Auto-refresh before call / Retry on 401 with re-auth / Not handled
    (gap: will produce runtime auth failures) / Not applicable]
  - Credential rotation: [Documented policy / Not documented / Not applicable]

[One entry per Call ID from PHASE 1. Do not omit any call.]

PHASE 2 GATE: Every call has an explicit auth entry. All "Unknown" entries are flagged as gaps.
Proceed to PHASE 3.

---

## PHASE 3: REQUEST AND RESPONSE FORMAT

[GATE: For every call in PHASE 1, document the request shape and expected response. This phase
documents only structure -- no error handling, no auth review, no rate limits. Structure only.
Partial schemas are acceptable -- note incompleteness. Omission is not acceptable.]

For each call:
- **[INT-NN] -- [System]**
  - Method: [HTTP method or protocol operation: GET / POST / PUT / DELETE / PUBLISH / etc.]
  - Key request headers: [Authorization (type), Content-Type, idempotency key header (if any),
    correlation ID header (if any). Note if any key header is absent or unknown.]
  - Body key fields: [Fields that must be present in the request body. "No body" for reads.
    Note if schema is partial and what is unknown.]
  - Expected response: [Status code(s) + key response fields. Note error response shape if
    documented. If not documented, note as gap.]

[One entry per Call ID. Incompleteness must be noted explicitly; omission is not allowed.]

PHASE 3 GATE: Every call has method, headers, body summary, and response summary.
Proceed to PHASE 4.

---

## PHASE 4: ERROR PROPAGATION

[GATE: For every call in PHASE 1, state the error fate. This phase documents only what happens
on failure -- no auth, no format, no rate limits. Error fate only. Every call must have an
explicit error-disposition statement. "No handling" is acceptable only if flagged as a gap.
A call that "never fails" still requires a disposition ("Surfaced by design" or "No handling").]

For each call:
- **[INT-NN] -- [System]**
  - Error fate: [Choose one:
    Surfaced -- returned to caller unchanged or wrapped with context /
    Transformed -- caught; raises [specific signal or exception] /
    Retried -- strategy: [fixed/exponential]; interval: [Xms]; max attempts: [N];
      backoff factor: [Y]; jitter: [yes/no]; respects Retry-After: [yes/no/not applicable] /
    Swallowed -- logged at [level]; execution continues; caller unaware -- GAP /
    No handling -- no error handling code for this call -- GAP]
  - Gap flag: [Yes -- [gap type: error swallowing / no error handling] / No]

[No call may be omitted from this phase.]

PHASE 4 GATE: Every call has an error-fate statement. All "Swallowed" and "No handling" entries
are flagged as gaps. Proceed to PHASE 5.

---

## PHASE 5: RATE LIMITS AND IDEMPOTENCY

[GATE: For every external system from PHASE 1, document rate limit information. For every
non-read call, assess idempotency. "Not documented" and "None" are findings. This phase
documents only rate limits and idempotency -- no auth, no error handling review.]

Rate limits (one entry per distinct external system):
- **[System]**
  - Limit: [Calls/min, calls/day, token budget, or "Not documented -- rate limit exposure"]
  - Burst behavior: [Queued / Rejected / Delayed / Unknown]
  - Throttle response: [429 with Retry-After header / 429 without Retry-After / Silent drop /
    Unknown]
  - Integration handles throttle?: [Yes -- describe how / No -- gap / Not applicable]

Idempotency (one entry per non-read call):
- **[INT-NN] -- [System]**
  - Idempotent by design?: [Yes -- [reason: pure read / naturally idempotent UPSERT / etc.] /
    No -- [risk: duplicate creates / double-charges / duplicate events / etc.]]
  - Mitigation: [Idempotency key header [name] / Deduplication in [system] / At-most-once
    delivery guaranteed by [mechanism] / None -- gap]

PHASE 5 GATE: All systems have rate limit entries; all non-read calls have idempotency
assessments. Proceed to GAP INVENTORY.

---

## GAP INVENTORY

[Collect every gap flagged across PHASE 2 (auth), PHASE 4 (error), and PHASE 5 (rate limits,
idempotency) into a single named finding list. Each finding references its source phase.]

| Finding ID | Call ID / System | Phase | Gap type | Description |
|------------|-----------------|-------|----------|-------------|
| GAP-01 | [INT-NN / system] | [2 / 4 / 5] | [Auth gap / Unknown auth / Error swallowing / No error handling / Rate limit exposure / No throttle handling / Missing idempotency / Missing retry] | [One sentence describing the specific gap and its runtime consequence] |
[Minimum: every "Unknown" auth (Phase 2), every "Swallowed" or "No handling" (Phase 4), every
"Not documented" rate limit (Phase 5), every non-idempotent call without mitigation (Phase 5).]

---

## SEVERITY AND REMEDIATION

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [One-line risk: data loss / auth bypass / silent failure / duplicate write / cascade throttle] | [HIGH: specific, call-context fix. E.g., "Add X-Idempotency-Key: {correlation-id} header to INT-03 POST /orders"; "Implement exponential backoff for INT-02: initial=500ms, factor=2, max=30s, jitter=uniform(0, 500ms), check Retry-After header on 429"; "Replace delegated token flow with client credentials on INT-05 to eliminate user token expiry failures"] |
[Order: HIGH first, then MEDIUM, then LOW.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, auth_gaps, error_gaps, rate_limit_gaps,
idempotency_gaps, findings_count, high_severity_count.
```

---

## V-05: Table + Happy Path Column

**Axes:** Output format + Inertia framing -- pre-printed 5-column table adds a "Happy path only?" column that forces explicit comparison against what the call looks like if it was designed only for the success case; happy-path baseline is pre-stated before any row is filled
**Hypothesis:** The "inertia" of cross-system integrations is the happy-path assumption -- the integration was built and tested under ideal conditions (auth valid, rate limits not hit, errors rare). Explicitly naming the happy-path baseline before analysis and forcing a per-row "Happy path only?" judgment surfaces error-swallowing and missing auth hardening as structural omissions rather than omitted observations. "Yes -- gap" rows in the table ARE the hardening gaps; they cannot be hidden. Tests whether happy-path framing produces richer C-06 (retry/idempotency) analysis and more complete C-07 (gap inventory) than analysis that never names the baseline assumption.

```
You are running /flow-integration. Fill in the pre-printed template below.
All column headers are fixed. Fill in every cell for every call row.
The "Happy path only?" column is required -- it forces you to assess whether each call has been
designed beyond the success case, against the happy-path baseline you state before any row.
Do not rename, reorder, omit, or leave blank any column.

---

## HAPPY PATH BASELINE

[State what this integration looks like under happy-path conditions. One to three sentences.
Describe the integration as it works when auth tokens are valid, rate limits are not hit, all
calls succeed, and errors do not occur. This is the comparison baseline for every
"Happy path only?" cell in the table below. Fill this in before writing any table row.]

Happy path baseline: [FILL IN -- describe the integration under ideal conditions: what calls
fire, what they return, what the caller receives, what state changes occur]

---

## CALL INVENTORY AND ANALYSIS TABLE

[Column instructions -- read all before filling any row:]
- **Call ID** (C-01): Assign INT-01, INT-02, etc. Use in GAP INVENTORY.
- **System + protocol** (C-01): Named system and protocol. "The API" is not a name.
- **Auth mechanism** (C-02): API key (header: [name]) / OAuth 2.0 Bearer (flow: [flow]) /
  service identity (MSI) / shared secret (location) / none (public, intentional) / Unknown -- gap.
- **Request / Response** (C-03): Method + key headers (Authorization, Content-Type, idempotency
  header if any) + body key fields + expected response (status + key fields). Partial acceptable
  -- note it.
- **Error disposition** (C-04): Surfaced / Transformed ([to what signal]) / Retried ([strategy:
  interval/exponential, max: N]) / Swallowed -- gap / No handling -- gap.
- **Happy path only?**: Compare the call's actual design to the happy-path baseline above:
  - **No** -- this call has auth expiry handling, error recovery, retry logic, or rate limit
    awareness beyond what the baseline requires. Describe what hardening exists.
  - **Yes -- gap** -- this call matches the happy-path baseline: it works when conditions are
    ideal but has no defense against the baseline assumption failing. State the failure scenario.
  - **Partial -- gap** -- some hardening exists but not complete. State what is present and
    what remains missing.

| Call ID | System + protocol | Auth mechanism | Request / Response | Error disposition | Happy path only? |
|---------|-------------------|---------------|-------------------|-------------------|-----------------|
| INT-01  | [Name + protocol] | [Mechanism or "Unknown -- gap"] | [Method / headers / body fields / response shape] | [Disposition or "Swallowed -- gap" / "No handling -- gap"] | [No (hardening: ...) / Yes -- gap (failure scenario: ...) / Partial -- gap (present: ..., missing: ...)] |
| INT-02  | [Name + protocol] | [Mechanism or "Unknown -- gap"] | [Method / headers / body fields / response shape] | [Disposition or "Swallowed -- gap" / "No handling -- gap"] | [No / Yes -- gap / Partial -- gap] |
[Add one row per distinct cross-system call. Include: API calls, MCP tool invocations, connector
actions, event publishes, event subscribes, webhook callbacks, token acquisition, health checks.
Include calls only visible on the success path. Minimum two rows.]

---

## RATE LIMITS AND IDEMPOTENCY

[One entry per external system for rate limits. One entry per non-read call for idempotency.
"Not documented" and "None" are findings.]

**Rate limits:**

| System | Limit documented? | Limit | Burst behavior | Throttle response | Happy path risk |
|--------|------------------|-------|----------------|-------------------|----------------|
| [Name] | Yes / No -- exposure | [Calls/min or "Unknown"] | [Queued/rejected/delayed/unknown] | [429+Retry-After / silent drop / unknown] | [In the happy path, rate limits are not hit -- but at [N * baseline volume] this system will throttle: [expected behavior]] |

**Idempotency:**

| Call ID | Idempotent? | Mitigation | Happy path risk |
|---------|-------------|------------|----------------|
| [INT-NN] | Yes / No / Unknown | [Key / dedup / guarantee / None -- gap] | [In the happy path this fires once and succeeds -- on retry it would [duplicate / overwrite / error / be safe -- state which]] |

---

## HAPPY PATH GAP SUMMARY

[Collect all rows where "Happy path only?" is "Yes -- gap" or "Partial -- gap". These are the
hardening gaps. Required -- do not omit this section.]

- **[INT-NN] ([Yes / Partial] -- gap)**: [Under what non-ideal condition does this call fail
  silently, propagate incorrectly, or cause data inconsistency? Name the specific scenario:
  token expiry / rate limit hit / network partition / duplicate invocation / 5xx from system X]

[If no calls are "Yes -- gap" or "Partial -- gap":
"All documented calls exceed the happy-path baseline. Verify that these scenarios were explicitly
considered for each call: (1) auth token expiry mid-session, (2) rate limit hit under sustained
load, (3) transient 5xx from downstream system, (4) duplicate call from retry or user action.
If any was not considered, that call's 'No' rating should be revisited."]

---

## GAP INVENTORY

| Finding ID | Call ID / System | Gap type | Description |
|------------|-----------------|----------|-------------|
| GAP-01 | [INT-NN / system] | [Auth gap / Unknown auth / Error swallowing / No error handling / Rate limit exposure / Missing idempotency / Happy path only] | [One sentence: the gap and its runtime consequence] |
[Minimum: all "Yes -- gap" and "Partial -- gap" rows from the table, all "Unknown -- gap" auth
entries, all "Swallowed -- gap" / "No handling -- gap" error dispositions, all "No -- exposure"
rate limit rows, all non-idempotent calls without mitigation.]

---

## SEVERITY AND REMEDIATION

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [One-line risk: data loss / auth bypass / silent failure / duplicate write / cascade] | [HIGH: specific, call-context fix. Not generic advice.] |
[Order: HIGH first, then MEDIUM, then LOW.]

Happy path exposure summary:
"[N] of [M] documented calls are happy-path-only (no hardening beyond the success scenario).
[K] calls exceed the baseline. [J] calls have partial hardening.
Under non-ideal conditions (token expiry / rate limits / transient failures), the unhardened
calls will [describe the collective failure mode]."

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, happy_path_only_count,
happy_path_partial_count, happy_path_exceeds_count, auth_gaps, error_gaps, rate_limit_gaps,
idempotency_gaps, findings_count, high_severity_count.
```

---

## Round 1 Design Notes

### Core structural challenge for flow-integration

Like `prove-analysis`, `flow-integration` is a per-item loop: the model must apply four essential
obligations to every cross-system call. The primary failure modes:

- **Partial loop coverage**: auth documented for INT-01 and INT-02, silently omitted for INT-05
  (the "obvious background call that surely has auth")
- **Error-disposition omission**: error propagation described for the "main" calls; webhook
  callbacks, token acquisition, and health checks are omitted entirely
- **Happy-path collapse**: auth is documented as "uses Bearer token" rather than "OAuth 2.0
  client credentials flow; token acquired from Azure AD; expiry not handled -- gap"
- **Call undercounting**: the model names the three obvious REST calls and omits the MCP tool
  invocations, the token acquisition call, and the webhook callback that fires asynchronously
- **Gap suppression**: no gap inventory because the model only documents what it can confirm,
  never flags what it cannot confirm as "Unknown -- gap"

### How each variation addresses the per-call loop problem

| V | Loop mechanism | Call undercounting risk | Error-disposition omission risk |
|---|---------------|------------------------|--------------------------------|
| V-01 | Table rows + fixed columns | Moderate -- call list is self-generated | Very low -- fixed column; blank = visible gap |
| V-02 | Three-pass sequential review | Low -- Architect pass specifically names call types | Low -- Reliability Engineer reviews every Call ID from Pass 1 |
| V-03 | Imperative checklist per call | Moderate -- Step 0 gate helps but is not enforced structurally | Low -- Step 3 is a discrete, non-mergeable imperative |
| V-04 | Gated phases; Phase 1 inventory fires before Phase 4 error | Low -- Phase 1 is inventory-only; no analysis until complete | Very low -- Phase 4 is dedicated solely to error-disposition |
| V-05 | Table rows + "Happy path only?" column | Moderate -- call list is self-generated | Low -- both error disposition column AND "Happy path only?" column flag the omission |

### Inertia framing depth comparison

The "happy path only" assumption in V-05 is the integration analog of the `prove-analysis` null
hypothesis. Both force the analyst to state the status-quo baseline before examining any item, then
explicitly evaluate each item against that baseline:

| Analysis skill | Inertia / Null | V-05 column | What "Yes" means |
|---------------|----------------|-------------|-----------------|
| prove-analysis | Null hypothesis | "Null met?" | Data matches the null; hypothesis not supported here |
| flow-integration | Happy path only | "Happy path only?" | Call matches happy-path design; no hardening; gap |

The "Happy path only?" column is structurally richer than the prove-analysis null column because
every "Yes -- gap" row in the call table is simultaneously a C-04 finding (error disposition), a
potential C-05 finding (rate limit unhandled), and a potential C-06 finding (no retry). The column
does triple duty as a finding flag.

### C-04 structural guarantee comparison

| V | How C-04 is guaranteed |
|---|------------------------|
| V-01 | Fixed "Error disposition" column in the table -- blank = visible failure |
| V-02 | Pass 2 Reliability Engineer reviews every Call ID from Pass 1 explicitly for error fate |
| V-03 | Step 3 is a discrete imperative: "State the error fate" -- cannot be satisfied by implication |
| V-04 | Phase 4 is dedicated solely to error-disposition; no other content allowed in that phase |
| V-05 | "Error disposition" column (fixed) + "Happy path only?" column (structural flag for no error handling) |

### Predicted differentiation under rubric

All five variations target 100/100 under the v1 rubric. Within-100 differentiation:

| Dimension | Strongest | Why |
|-----------|----------|-----|
| C-01 call undercounting prevention | V-02, V-04 | Pass 1 / Phase 1 enumerates call types before any analysis |
| C-04 structural guarantee | V-01, V-04, V-05 | Fixed column, dedicated phase, or dual-column flag |
| C-07 gap inventory completeness | V-05 | "Yes -- gap" rows are structural findings; cannot be absent from GAP INVENTORY |
| C-08 severity depth | V-04 | Gated phases naturally elicit mechanism-level reasoning; Phase 4 "error fate" detail feeds severity rationale |
| C-09 remediation specificity | V-04 | Phase 5 idempotency and retry details provide the context for call-specific fix language |
| Template overhead | V-03 | Minimum structure; tests whether imperative register produces floor coverage without scaffolding |

### Open research questions for R1

1. Does V-03's imperative register produce shorter but more direct error-fate outputs, or does it
   produce "handles errors gracefully" with no disposition type -- exactly the pattern Step 3
   explicitly forbids?
2. Does V-05's happy-path column cause the model to over-report "No" (claims hardening exists
   when it doesn't) or does it produce more honest "Yes -- gap" acknowledgment because the
   failure scenario field forces concreteness?
3. Does V-04's inventory-only Phase 1 reduce call undercounting compared to V-01 and V-05 where
   the call list is generated as part of filling the table?
4. Does V-02's three-pass structure produce richer security-relevant auth findings (Pass 3) than
   the other variations, which treat auth as one field among several?

### V-golden candidate

**V-04** is the baseline target: gated phase structure guarantees per-phase completeness for all
calls; Phase 4 dedicated error-disposition phase is the strongest structural guarantee for C-04;
Phase 5 idempotency detail feeds C-09 remediation quality.

**V-05** is the richer candidate for gap inventory: happy-path column makes hardening gaps
structurally visible per call, and the "Happy path exposure summary" in SEVERITY AND REMEDIATION
produces a quantified gap statement that no other variation pre-prints. Key open question: does
the happy-path framing improve the quality of "Yes -- gap" descriptions (C-04, C-06) or cause
the model to claim "No" (hardening present) without substantiating it?

**V-01** is the control: pure table structure, no phase gates, no role sequence. If V-01 reaches
the golden threshold, the additional complexity of V-04 and V-05 is not justified for this skill.
