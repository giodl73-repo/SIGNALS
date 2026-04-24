Written to `simulations/quest/variations/flow-integration-variations-R2-2026-03-14.md`.

---

## Round 2 Variations -- flow-integration

**5 variations, 3 single-axis + 2 combined:**

| V | Axis | Core mechanism | C-10/C-11/C-12 strategy |
|---|------|----------------|------------------------|
| **V-01** | Output format: repaired V-05 | Happy-path column + dedicated Request/Response subsections | Table is inventory (C-10); subsections are single-concern (C-11); "Happy path only?" dual-flags per call (C-12 partial) |
| **V-02** | Lifecycle: minimal gates | V-04's five phases compressed to single gate conditions only — no prose | Gate conditions alone enforce C-10/C-11/C-12 — tests whether V-04's verbosity is structural |
| **V-03** | Phrasing register: imperative upgraded | V-03 voice + pre-printed rate-limit/idempotency tables + MEDIUM/LOW rationale prompts + CALL COMPLETE marker | Targeted additions address all five R1 PARTIALs without changing the register |
| **V-04** | Role sequence + Lifecycle: embedded Security | V-04 gated phases + Security Engineer inside Phase 2 Part B | Eliminates V-02's split-finding C-07 risk; full C-10/C-11/C-12 from phase structure |
| **V-05** | Output format + Lifecycle: per-call gate blocks | Inventory table, then per-call five-concern blocks each with an explicit named completion checklist | Directly instantiates C-12 (4 new pts): completion condition is structural at call level, not section level |

**R1 open questions addressed:**
1. **V-05 C-03 failure** → V-01 repairs it with a dedicated section; happy-path column retained
2. **V-03 barely golden (81)** → V-03 upgraded adds three structural aids while keeping the register
3. **V-02 Security Engineer split-finding risk** → V-04 embeds Security into Phase 2 Part B — one collection point, no separate security table

**v2 rubric changes addressed in all five:**
- **C-03 tightened**: All five use separate labeled lines or dedicated sections — no merged cells
- **C-08 tightened**: All five include explicit "MEDIUM and LOW require rationale" instruction
- **C-10/C-11/C-12 new (12 pts total)**: V-05 targets C-12 directly; V-04/V-02 inherit all three from gated structure; V-01/V-03 reach partial coverage

**Predicted top candidates:** V-05 (C-12 explicit), V-04 (security depth + phase discipline)
**Predicted floor:** V-03 (CALL COMPLETE marker is the weakest C-12 instantiation)
y-path inertia column retained from R1 V-05; Request/Response
concern moved to a dedicated named section (not merged into table cell); the inventory table
completing before the dedicated subsections satisfies C-10 partially.

**Hypothesis:** V-05 failed golden on C-03 because method + headers + body + response were
compressed into a single markdown table cell. The happy-path column is V-05's best feature
(dual-flagging C-04 and C-07 simultaneously). Separating the Request/Response into a
dedicated section per call fixes C-03 without losing the inertia framing's gap-surfacing
power. Explicit MEDIUM/LOW rationale prompts in the final table address the tightened C-08.

```
You are running /flow-integration.

Before you document a single call, state the assumption under pressure:

> The integration was built and tested under happy-path conditions: tokens valid, systems
> available, rates within limits, calls completing on first attempt. The calls below may
> work in demo. They do not yet work in production until each one is hardened beyond its
> happy-path design.

Fill in the pre-printed template below. All column headers are fixed. Fill in every cell
for every call row. Do not add, rename, reorder, or remove any column. A blank cell is a
visible gap -- do not leave any cell blank.

---

## CALL INVENTORY

[Complete this table before writing any per-call subsections below. The table is the
named inventory -- all subsequent sections reference Call IDs from this table.]

Column instructions:
- **Call ID**: Assign INT-01, INT-02, ... sequentially. Every subsequent section uses this ID.
- **System + protocol**: Named target system and protocol. E.g., "Salesforce REST API",
  "Azure Service Bus AMQP", "MCP tool: calendar-read". "The API" is not a name.
- **Call type**: Create / Read / Update / Delete / Event publish / Event subscribe /
  Webhook callback / Token acquire / Health check / Other:[specify].
- **Auth mechanism**: API key (header name) / OAuth 2.0 Bearer (flow: [flow]) / service
  identity (MSI/managed identity) / shared secret (location: [env/vault/config]) /
  none (public endpoint -- intentional) / Unknown -- gap.
- **Error disposition**: Surfaced (returned to caller) / Transformed (caught; raises [signal])
  / Retried ([strategy], max [N]) / Swallowed (logged; execution continues -- gap) /
  No handling -- gap. Do not write "handles errors" without a disposition type.
- **Happy path only?**: Does the current implementation only handle the success path?
  Yes -- gap / Partial -- gap / No. "Yes -- gap" means no hardening beyond the success
  case. "Partial -- gap" means some hardening exists but gaps remain.

| Call ID | System + protocol | Call type | Auth mechanism | Error disposition | Happy path only? |
|---------|-------------------|-----------|----------------|-------------------|-----------------|
| INT-01  | [Name + protocol] | [Type]    | [Mechanism or "Unknown -- gap"] | [Disposition or "No handling -- gap"] | [Yes -- gap / Partial -- gap / No] |
| INT-02  | [Name + protocol] | [Type]    | [Mechanism or "Unknown -- gap"] | [Disposition or "No handling -- gap"] | [Yes -- gap / Partial -- gap / No] |
[Add one row per distinct cross-system call. Include: direct API calls, MCP tool invocations,
connector actions, event publishes, event subscribes, webhook callbacks, token acquisition
calls, health checks. Include calls that are "background" or "assumed to work." Include
calls to unknown systems. Minimum two rows.]

[The inventory is complete when every cross-system call has a row. Do not write per-call
subsections below until this table has a row for every call.]

---

## REQUEST AND RESPONSE FORMAT

[One entry per Call ID from the inventory above. Do not omit any call. Partial schemas are
acceptable -- note incompleteness explicitly. All four fields are required per call and
must appear as separate labeled lines. A single merged line does not satisfy this section.]

**[INT-NN] -- [System + protocol]**
- Method: [HTTP method or protocol operation: GET / POST / PUT / DELETE / PUBLISH /
  SUBSCRIBE / other]
- Key request headers: [Headers affecting routing, auth, content type, or idempotency.
  At minimum: Authorization (type + flow), Content-Type. Note any X-Idempotency-Key or
  correlation headers. Note incompleteness if schema is partial.]
- Body key fields: [Required fields in the request body. Write "No body" for side-effect-free
  reads. Note schema incompleteness if partial.]
- Expected response: [Status code(s) + key response fields. Note error response shape if
  documented. E.g., "200 with {id, status, created_at}; 429 with Retry-After header".]

[Repeat for each Call ID. Omission is not acceptable. This section addresses format only --
do not repeat auth or error disposition here.]

---

## RATE LIMITS AND HAPPY PATH RISK

[One entry per external system. Systems with no documented rate limit are exposures.]

| System | Rate limit documented? | Limit | Burst behavior | Throttle response | Happy path risk |
|--------|------------------------|-------|----------------|-------------------|----------------|
| [Name] | Yes / No -- exposure   | [calls/min, calls/day, token budget, or "Unknown"] | [Queued / rejected / delayed / unknown] | [429 + Retry-After / silent drop / unknown] | [What breaks at 2x / 10x happy-path traffic, or "Unknown -- gap"] |
[One row per distinct external system. "No -- exposure" rows are findings for GAP INVENTORY.]

---

## RETRY AND IDEMPOTENCY

[One entry per Call ID that can fail transiently. "Happy path risk" states what happens
on duplicate delivery or retry.]

| Call ID | Retry strategy | Max attempts | Backoff | Jitter | Idempotent? | Mitigation if not | Happy path risk |
|---------|---------------|--------------|---------|--------|-------------|-------------------|----------------|
| [INT-NN] | Fixed / Exponential / None | [N or "none"] | [Factor or "none"] | [Yes / No / N/A] | [Yes / No / Unknown] | [Idempotency key / dedup / at-most-once / None -- gap] | ["Duplicate delivery causes [X]" or "Retry creates duplicate [resource]" or "N/A"] |
[Calls with "None" retry that can fail transiently are findings. Non-idempotent calls
without mitigation are findings.]

---

## HAPPY PATH GAP SUMMARY

[Before the formal gap inventory: collect all "Yes -- gap" and "Partial -- gap" rows from
the inventory table, plus rate-limit exposures and idempotency gaps. This pre-collection
ensures hardening gaps cannot be omitted from the formal inventory below.]

| Call ID / System | Hardening gap | Section | Description |
|-----------------|---------------|---------|-------------|
| [INT-NN or system] | Error disposition / Rate limit / Retry / Idempotency / Auth | Inventory / Rate limits / Retry | [One sentence: what the happy path assumes and what production requires] |

[Every "Yes -- gap" inventory row, every "No -- exposure" rate limit row, and every
"None -- gap" mitigation row must appear here before they appear in GAP INVENTORY.]

---

## GAP INVENTORY

[Collect all gaps from the Happy Path Gap Summary and any additional gaps identified.]

| Finding ID | Call ID / System | Gap type | Description |
|------------|-----------------|----------|-------------|
| GAP-01 | [INT-NN or system] | [Auth gap / Rate limit exposure / Error swallowing / No error handling / Missing retry / Missing idempotency / Unknown auth] | [One sentence describing the specific gap] |
[At minimum: every "Unknown -- gap" auth, every "Swallowed" or "No handling -- gap"
error disposition, every "No -- exposure" rate limit, every non-idempotent call without
mitigation must appear here.]

---

## SEVERITY AND REMEDIATION

[ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. For HIGH findings,
also provide a specific remediation sketch.]

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [One line stating the risk -- required for HIGH, MEDIUM, and LOW: data loss / auth bypass / silent failure / latency spike / duplicate write / audit exposure] | [HIGH only: specific fix for this call. E.g., "Add X-Idempotency-Key: {topic}-{call-id}-{timestamp}"; "Exponential backoff: initial=500ms, factor=2, max=30s, jitter=uniform(0,500ms)"; "Replace delegated user token with application identity to eliminate expiry failures at runtime"] |
[Order: HIGH first, then MEDIUM, then LOW. Rationale is mandatory for every row.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, happy_path_gaps, auth_gaps, error_gaps,
rate_limit_gaps, idempotency_gaps, findings_count, high_severity_count.
```

---

## V-02: Lifecycle emphasis -- Minimal Gated Phases

**Axis:** Lifecycle emphasis -- V-04's five-phase gated structure compressed to single gate
conditions per phase; all paragraph explanations removed; enforcement carried entirely by
the gate statement and one pre-printed example row per section.

**Hypothesis:** V-04 reached 100 in R1 with verbose phase descriptions and rich per-concern
instructions. This variation tests whether the gate condition alone -- "Phase N is complete
when X is true for every call in the inventory" -- produces equivalent structural coverage
without instructional prose. If minimal phases perform identically, V-04's verbosity is
aesthetic, not structural. C-08 tightening is addressed with a mandatory MEDIUM/LOW
rationale instruction. C-10, C-11, C-12 should fire from gate conditions alone.

```
You are running /flow-integration. Complete five phases in order. Do not begin a phase
until the previous phase's gate condition is met for every call in the inventory.

---

## PHASE 1: CALL INVENTORY

List every cross-system boundary crossing: direct API calls, MCP tool invocations,
connector actions, event publishes, event subscribes, webhook callbacks, token
acquisitions, health checks, and any call that is "background," "assumed to work," or
has an unknown target system. Assign each call a sequential ID: INT-01, INT-02, etc.

| Call ID | System | Protocol | Call type |
|---------|--------|----------|-----------|
| INT-01  | [Named system -- "The API" is not a name] | [REST / AMQP / OData / GraphQL / MCP / gRPC / other] | [Create / Read / Update / Delete / Event publish / Event subscribe / Webhook / Token acquire / Health check / Other] |
[Include unknown systems as "Unknown system" with a gap flag. Minimum two rows.]

[GATE 1: Phase 1 is complete when every cross-system call has a row with Call ID, named
system, protocol, and call type. Phase 2 does not begin until this gate fires. No per-call
analysis of any kind appears in Phase 1.]

---

## PHASE 2: AUTHENTICATION

For every Call ID in Phase 1, document the auth mechanism. Authentication only -- no
format, error handling, or rate limits in this phase.

| Call ID | Auth mechanism | Token expiry handling | Credential rotation |
|---------|----------------|----------------------|---------------------|
| INT-NN  | [API key (header: [name]) / OAuth 2.0 Bearer (flow: [flow]) / service identity (MSI) / shared secret (location: [vault/env/config]) / none (public -- intentional) / Unknown -- gap] | [Handled in error path / Not handled -- gap / N/A] | [Documented policy / Not documented -- gap / N/A] |

[GATE 2: Phase 2 is complete when every Call ID from Phase 1 has an auth mechanism entry.
"Unknown -- gap" is acceptable only if explicitly stated. No format or error content
appears in this phase.]

---

## PHASE 3: REQUEST AND RESPONSE FORMAT

For every Call ID in Phase 1, document the call's shape. Format only -- no auth, error
handling, or rate limits in this phase. All four fields are required per call as separate
labeled lines.

**[INT-NN] -- [System]**
- Method: [HTTP method or protocol operation]
- Key request headers: [Authorization type + flow, Content-Type, idempotency or correlation
  headers. Note incompleteness explicitly if schema is partial.]
- Body key fields: [Required fields. "No body" for side-effect-free reads.]
- Expected response: [Status code(s) + key fields. Note error response shape if documented.]

[Repeat for each Call ID. Omission is not acceptable.]

[GATE 3: Phase 3 is complete when every Call ID from Phase 1 has method, key request
headers, body key fields, and expected response documented as separate labeled fields.
A single merged "Request / Response" field does not fire this gate. No error or rate-limit
content appears in this phase.]

---

## PHASE 4: ERROR FATE

For every Call ID in Phase 1, state the error disposition. Error handling only -- no auth,
format, or rate-limit content in this phase. A call that "never fails" still requires a
disposition.

| Call ID | Error disposition | Gap flag |
|---------|-------------------|----------|
| INT-NN  | [Surfaced (returned to caller) / Transformed (caught; raises [signal]) / Retried (strategy: [fixed/exp], interval: [Xms], max: [N]) / Swallowed (logged; execution continues) / No handling] | [-- / GAP: swallowed / GAP: no handling / GAP: token expiry not in error path] |

[GATE 4: Phase 4 is complete when every Call ID from Phase 1 has an error-disposition
entry and every "Swallowed" or "No handling" entry has an explicit gap flag. No other
concern is addressed in this phase.]

---

## PHASE 5: RATE LIMITS AND IDEMPOTENCY

Document rate limits per system and idempotency per call. These two concerns only -- no
auth, format, or error re-documentation in this phase.

### Rate Limits

| System | Rate limit documented? | Limit | Burst behavior | Throttle response |
|--------|------------------------|-------|----------------|-------------------|
| [Name] | Yes / No -- exposure   | [Limit or "Unknown"] | [Queued / rejected / delayed / unknown] | [429 + Retry-After / silent drop / unknown] |
[One row per distinct external system. "No -- exposure" rows are gap findings.]

### Retry and Idempotency

| Call ID | Retry strategy | Max attempts | Backoff | Jitter | Idempotent? | Mitigation if not |
|---------|---------------|--------------|---------|--------|-------------|-------------------|
| INT-NN  | [Fixed / Exponential / None] | [N or "none"] | [Factor or "N/A"] | [Yes / No / N/A] | [Yes / No / Unknown] | [Idempotency key / dedup / at-most-once / None -- gap] |
[Calls with "None" retry that can fail transiently are findings. Non-idempotent write calls
without mitigation are findings.]

[GATE 5: Phase 5 is complete when every external system has a rate-limit entry and every
non-read call has an idempotency assessment. "No -- exposure" and "Unknown" entries count
toward gate completion as flagged gaps.]

---

## GAP INVENTORY

Collect all gap flags from Phases 2, 4, and 5. Reference Call IDs.

| Finding ID | Call ID / System | Phase | Gap type | Description |
|------------|-----------------|-------|----------|-------------|
| GAP-01 | [INT-NN or system] | [2/4/5] | [Auth gap / Rate limit exposure / Error swallowing / No error handling / Missing retry / Missing idempotency / Unknown auth] | [One sentence] |
[At minimum: every Phase 2 "Unknown -- gap" auth, every Phase 4 "Swallowed" or "No handling"
flag, every Phase 5 "No -- exposure" rate limit, and every Phase 5 "None -- gap" idempotency
must appear here.]

---

## SEVERITY AND REMEDIATION

Rank all findings. ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [Why this severity -- required for HIGH, MEDIUM, and LOW: data loss / auth bypass / silent failure / latency spike / duplicate write] | [HIGH: specific fix for this call. E.g., "Exponential backoff: initial=500ms, factor=2, max=30s"; "X-Idempotency-Key: {topic}-{call-id}-{timestamp}"; "Switch to application identity to prevent token expiry at runtime"] |
[Order: HIGH first, then MEDIUM, then LOW. Leave Remediation blank for MEDIUM and LOW.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, auth_gaps, error_gaps, rate_limit_gaps,
idempotency_gaps, findings_count, high_severity_count.
```

---

## V-03: Phrasing register -- Imperative Upgraded

**Axis:** Phrasing register -- V-03's imperative voice retained; targeted structural
additions address R1 PARTIAL scores: pre-printed rate-limit table (C-05 PARTIAL in R1),
pre-printed idempotency table (C-06 PARTIAL in R1), explicit MEDIUM/LOW rationale prompts
(C-08 PARTIAL in R1), and a per-call CALL COMPLETE marker at Step 3 (toward C-12).

**Hypothesis:** V-03 scored 81 with every recommended and aspirational criterion at PARTIAL.
All five PARTIAL scores have structural causes -- no pre-printed rate-limit table, no
pre-printed idempotency table, no MEDIUM/LOW rationale structure, no per-call completion
signal. None require abandoning the imperative register. If three targeted structural
additions lift V-03 to golden without changing the voice, the register was not the
bottleneck -- missing scaffolding was.

```
You are running /flow-integration.

Trace every cross-system call in this integration. For each call, complete five steps in
order. No skipping steps. No merging steps. No producing Step N+1 output before Step N
is done.

---

**Step 0 -- Build the call list before analyzing anything.**

List every cross-system boundary crossing. Be complete:
- Direct API calls (REST, GraphQL, OData, gRPC)
- MCP tool invocations
- Connector actions
- Event publishes and event subscribes
- Webhook callbacks
- Token acquisition calls
- Health checks
- Any call that is "background," "assumed to work," or has an unknown target system

Assign each a sequential ID: INT-01, INT-02, etc. Name the system. Name the protocol.
If you cannot name the target system: list it as "Unknown system -- gap."

Call list:
- INT-01 | [System] | [Protocol] | [Call type]
- INT-02 | [System] | [Protocol] | [Call type]
[Continue until every cross-system call is listed. Do not begin Step 1 until every call
is listed here. Minimum two entries.]

---

**Step 1 -- Name the auth for every call.**

For every INT-NN in the call list: state how this call authenticates. Be specific.
Do not write "authenticated" -- name the mechanism.

INT-NN -- [System]
- Auth mechanism: [API key (header: [name]) / OAuth 2.0 Bearer (flow: [flow]) / service
  identity (MSI/managed identity) / shared secret (location: [env/vault/config]) /
  none (public endpoint -- intentional) / Unknown -- flag as gap]
- Token expiry handling: [Handled in error path / Not handled -- flag as gap / N/A]
- Credential rotation: [Documented policy / Not documented -- flag as gap / N/A]

[Repeat for every INT-NN. If auth is unknown: say so. Do not write "presumably uses auth"
without a mechanism.]

---

**Step 2 -- State the request and response shape for every call.**

For every INT-NN: state what goes in and what comes back. Do not write "sends a request"
without stating what is in it. All four fields are required -- do not compress them.

INT-NN -- [System]
- Method: [operation]
- Key request headers: [Authorization type, Content-Type, idempotency or correlation
  headers. Note incompleteness explicitly if schema is partial.]
- Body key fields: [Required fields. "No body" for side-effect-free reads.]
- Expected response: [Status code + key fields. Note error response shape if documented.]

[Repeat for every INT-NN.]

---

**Step 3 -- State the error fate for every call.**

For every INT-NN: state exactly what happens when this call fails. Do not skip this step.
Do not write "handles errors" without a disposition type. A call that "never fails" still
requires a disposition.

INT-NN -- [System]
- Error disposition: [Choose one: Surfaced (returned to caller) / Transformed (caught;
  raises [signal]) / Retried (strategy: [fixed/exponential], interval: [Xms], max: [N]) /
  Swallowed (logged at [level]; execution continues) / No handling]
- Gap flag: [-- / GAP: error swallowed -- execution continues silently / GAP: no handling --
  call failure is invisible / GAP: token expiry not handled in error path]
- CALL COMPLETE: [ ] Auth (Step 1) [ ] Format (Step 2) [ ] Error fate (Step 3)

[Mark CALL COMPLETE when all three steps are filled for this INT-NN. Every INT-NN must
reach CALL COMPLETE before Step 4 begins. Do not skip any call.]

---

**Step 4 -- Document rate limits per system.**

For every external system in the call list: state the documented rate limit. If not
documented: say so and flag it. Do not assume a system has no rate limit because you
have not seen one documented.

| System | Rate limit documented? | Limit | Burst behavior | Throttle response |
|--------|------------------------|-------|----------------|-------------------|
| [Name] | Yes / No -- exposure   | [Calls/min, calls/day, token budget, or "Unknown"] | [Queued / rejected / delayed / unknown] | [429 + Retry-After / silent drop / unknown] |
[One row per distinct external system. "No -- exposure" rows are findings.]

---

**Step 5 -- Document retry and idempotency per call.**

For every INT-NN that can fail transiently: state whether it has retry logic and whether
it is idempotent. If the call can fail and has no retry: flag it. If the call is not
idempotent and has no mitigation: flag it.

| Call ID | Retry strategy | Max attempts | Backoff | Jitter | Idempotent? | Mitigation if not |
|---------|---------------|--------------|---------|--------|-------------|-------------------|
| INT-NN  | [Fixed / Exponential / None] | [N or "none"] | [Factor or "N/A"] | [Yes / No / N/A] | [Yes / No / Unknown] | [Idempotency key / dedup / at-most-once / None -- gap] |
[Calls with "None" retry that can fail transiently are findings. Non-idempotent calls
without mitigation are findings.]

---

**Step 6 -- List every gap flagged in Steps 1--5.**

Collect every flagged gap from Steps 1, 2, 3, 4, and 5 into a numbered finding list.
Each finding references its INT-NN or system. Use the gap type taxonomy below.
Do not leave findings inline in the steps above -- collect them all here.

Gap type taxonomy: Auth gap / Rate limit exposure / Error swallowing / No error handling /
Missing retry / Missing idempotency / Unknown auth / Token expiry not handled

| Finding ID | Call ID / System | Gap type | Description |
|------------|-----------------|----------|-------------|
| GAP-01 | [INT-NN or system] | [Gap type] | [One sentence] |

---

**Step 7 -- Rank every finding by severity. Every finding needs a rationale.**

Assign severity to every finding. ALL findings -- HIGH, MEDIUM, and LOW -- require a
one-line rationale. Do not write only HIGH rationales. For HIGH findings, also provide a
specific, call-context remediation.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [Why this severity -- required for HIGH, MEDIUM, and LOW. E.g., HIGH: "error swallowing masks auth failure -- downstream write is silently lost"; MEDIUM: "rate limit undocumented -- burst traffic triggers 429 with no backoff to recover"; LOW: "credential rotation undocumented -- low immediate risk but creates audit exposure"] | [HIGH: specific fix for this call. Not generic advice.] |

[Order: HIGH first, then MEDIUM, then LOW. Rationale is not optional for any row.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, auth_gaps, error_gaps, rate_limit_gaps,
idempotency_gaps, findings_count, high_severity_count.
```

---

## V-04: Role sequence + Lifecycle -- Security Embedded in Phase 2

**Combined axes:** Role sequence (Security Engineer from R1 V-02) + Lifecycle emphasis
(V-04 gated phases). Security Engineer audit is performed inside Phase 2 (Auth phase)
as Part B, not as a separate Pass 3. Security gap findings flow into Phase 2's gate
and feed the single GAP INVENTORY with no split-finding risk.

**Hypothesis:** R1 V-02 scored 95 but got a C-07 PARTIAL because the Security Engineer
produced a separate "Security Gap Summary" that preceded the unified GAP INVENTORY,
creating a completeness risk. V-04's phase isolation prevents this: Security is a lens
inside Phase 2, not an independent pass. All security findings are Phase 2 outputs and
the GAP INVENTORY has one collection point. Explicit MEDIUM/LOW rationale prompts
address C-08 tightening.

```
You are running /flow-integration. Six phases complete the integration trace. No analysis
begins until the inventory is complete. No phase begins until the previous phase's gate
fires.

---

## PHASE 1: CALL INVENTORY

Role: Integration Architect.
Concern: Call enumeration only. No auth, format, error, or rate-limit content in this phase.

Enumerate every cross-system call: direct API calls, MCP tool invocations, connector
actions, event publishes, event subscribes, webhook callbacks, token acquisitions, health
checks. Include calls that are "background," "assumed to work," or have unknown target
systems. Assign each call a sequential ID: INT-01, INT-02, etc.

| Call ID | System | Protocol | Call type |
|---------|--------|----------|-----------|
| INT-01  | [Named system -- "The API" is not a name] | [REST / AMQP / OData / GraphQL / MCP / gRPC / other] | [Create / Read / Update / Delete / Event publish / Event subscribe / Webhook / Token acquire / Health check / Other] |
[Unknown system calls: list as "Unknown system" with a gap flag. Minimum two rows.]

[GATE 1: Phase 1 is complete when every cross-system call has a row with Call ID, named
system, protocol, and call type. Phase 2 does not begin until this gate fires. No per-call
analysis of any kind appears in Phase 1.]

---

## PHASE 2: AUTHENTICATION

Roles: Integration Architect (Part A) + Security Engineer (Part B).
Concern: Authentication only. No request format, error handling, or rate limits in this
phase. Both parts address auth -- no other concern appears here.

**Part A -- Integration Architect: Document auth per call.**

| Call ID | Auth mechanism | Token expiry handling | Credential rotation |
|---------|----------------|----------------------|---------------------|
| INT-NN  | [API key (header: [name]) / OAuth 2.0 Bearer (flow: client credentials / auth code / on-behalf-of) / service identity (MSI/managed identity) / shared secret (location: [vault/env/config]) / none (public -- intentional) / Unknown -- gap] | [Handled in error path / Not handled -- gap / N/A] | [Documented rotation policy / Not documented -- gap / N/A] |

**Part B -- Security Engineer: Auth audit.**

Review each call's Part A entry for security posture. Flag any of:
- "Unknown -- gap" mechanism --> UNKNOWN AUTH finding
- Delegated user token where application identity would be safer (avoids expiry failures)
  --> RECOMMEND APPLICATION IDENTITY finding
- Token expiry not handled in error path --> AUTH EXPIRY finding
- Credentials in environment without rotation documentation --> CREDENTIAL ROTATION finding
- No auth on a non-public endpoint --> MISSING AUTH finding

Document security findings with GAP-S-NN IDs:
- GAP-S-01 | INT-NN | [Auth gap type] | [One sentence: what the issue is and its
  runtime consequence]

[GATE 2: Phase 2 is complete when every Call ID has a Part A auth entry AND every auth
issue has a GAP-S-NN finding in Part B. "Unknown -- gap" entries must have a corresponding
GAP-S-NN. No format, error, or rate-limit content appears in this phase.]

---

## PHASE 3: REQUEST AND RESPONSE FORMAT

Role: Integration Architect.
Concern: Request and response shape only. No auth, error handling, or rate limits here.
All four fields are required per call as separate labeled lines.

**[INT-NN] -- [System]**
- Method: [HTTP method or protocol operation]
- Key request headers: [Authorization type + flow, Content-Type, idempotency or correlation
  headers. Note incompleteness explicitly if schema is partial.]
- Body key fields: [Required fields. "No body" for side-effect-free reads.]
- Expected response: [Status code(s) + key fields. Note error response shape if documented.
  E.g., "200 with {id, status, created_at}; 429 with Retry-After header".]

[Repeat for each Call ID. Omission is not acceptable.]

[GATE 3: Phase 3 is complete when every Call ID from Phase 1 has method, key request
headers, body key fields, and expected response documented as separate labeled fields.
A single merged field does not fire this gate. No other concern is addressed here.]

---

## PHASE 4: ERROR FATE

Role: Reliability Engineer.
Concern: Error disposition and propagation path only. No auth, format, or rate limits
in this phase. A call that "never fails" still requires a disposition.

| Call ID | Error disposition | Gap flag |
|---------|-------------------|----------|
| INT-NN  | [Surfaced (returned to caller with context) / Transformed (caught; raises [signal]) / Retried (strategy: [fixed/exponential], interval: [Xms], max: [N], jitter: [yes/no]) / Swallowed (logged at [level]; execution continues) / No handling] | [-- / GAP: error swallowed / GAP: no handling / GAP: token expiry produces silent auth failure] |

[GATE 4: Phase 4 is complete when every Call ID has an error-disposition entry. Every
"Swallowed" or "No handling" entry must have a gap flag. No other concern is addressed
in this phase.]

---

## PHASE 5: RATE LIMITS AND IDEMPOTENCY

Role: Reliability Engineer.
Concern: Rate limit exposure and idempotency only. No auth, format, or error re-documentation.

### Rate Limits

| System | Rate limit documented? | Limit | Burst behavior | Throttle response | Retry-After respected? |
|--------|------------------------|-------|----------------|-------------------|-----------------------|
| [Name] | Yes / No -- exposure   | [calls/min, calls/day, token budget, or "Unknown"] | [Queued / rejected / delayed / unknown] | [429 + Retry-After / silent drop / unknown] | [Yes / No / N/A -- no retry logic] |

### Retry and Idempotency

| Call ID | Idempotent? | Retry strategy | Backoff (initial / factor / max / jitter) | Mitigation if not idempotent |
|---------|-------------|----------------|-------------------------------------------|------------------------------|
| INT-NN  | [Yes / No / Unknown] | [Fixed / Exponential / None] | [e.g., 500ms / 2x / 30s / uniform(0,500ms) or N/A] | [X-Idempotency-Key header / dedup log / at-most-once / None -- gap] |

[GATE 5: Phase 5 is complete when every external system has a rate-limit entry and every
non-read call has an idempotency assessment. "No -- exposure" and "None -- gap" entries
count toward gate completion as flagged gaps.]

---

## GAP INVENTORY

Collect all gap flags from Phases 2 (Part A unknown auth + all GAP-S-NN), 4, and 5
into a single numbered finding list. GAP-S-NN findings from Phase 2 Part B are
renumbered into the GAP-NN sequence here. No separate security table exists.

| Finding ID | Call ID / System | Phase | Gap type | Description |
|------------|-----------------|-------|----------|-------------|
| GAP-01 | [INT-NN or system] | [2A / 2B / 4 / 5] | [Auth gap / Unknown auth / Token expiry / Rate limit exposure / Error swallowing / No error handling / Missing retry / Missing idempotency / Credential rotation gap] | [One sentence] |
[At minimum: every Phase 2A "Unknown -- gap" auth, every Phase 2B GAP-S-NN, every Phase 4
"Swallowed" or "No handling" flag, every Phase 5 "No -- exposure" rate limit, and every
Phase 5 "None -- gap" idempotency must appear here.]

---

## SEVERITY AND REMEDIATION

Rank all findings. ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale.
HIGH findings also require a specific, call-context remediation.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [Why this severity -- required for every row: data loss / auth bypass / silent failure / latency spike / duplicate write / information leakage / audit exposure] | [HIGH: specific fix. E.g., "Add X-Idempotency-Key: {topic}-{call-id}-{timestamp}"; "Exponential backoff: initial=500ms, factor=2, max=30s, jitter=uniform(0,500ms)"; "Replace on-behalf-of token with client_credentials flow to eliminate runtime expiry failures"] |
[Order: HIGH first, then MEDIUM, then LOW. Rationale is mandatory for every row.
Leave Remediation blank for MEDIUM and LOW.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, auth_gaps, security_gaps, error_gaps,
rate_limit_gaps, idempotency_gaps, findings_count, high_severity_count.
```

---

## V-05: Output format + Lifecycle -- Per-Call Completion Gate Blocks

**Combined axes:** Output format (per-call structured blocks instead of table rows) +
Lifecycle emphasis (inventory-first gate, then per-call blocks each with an explicit
named completion checklist). Directly targets C-12 (gate-enforced per-call completion,
4 new pts in v2).

**Hypothesis:** V-04 and V-01 both reached 100 in R1, but neither fully instantiated C-12
because their completion conditions were section-level, not call-level. C-12 is worth
4 new points in v2. Moving from table rows to per-call blocks with an explicit five-concern
completion checklist makes the completion condition structural at the call level, directly
satisfying C-12. C-10 fires from the inventory table completing before any block begins.
C-11 fires because each concern within a block is a labeled section that cannot bleed.
C-08 tightening is addressed with explicit MEDIUM/LOW rationale instruction.

```
You are running /flow-integration. The trace runs in two stages: inventory first, then
per-call analysis blocks. No per-call block may begin until the inventory is complete.
Each per-call block has a named completion checklist -- the block is not complete until
all five concern sections are checked.

---

## STAGE 1: CALL INVENTORY

[Complete this inventory before writing any per-call analysis block. All Stage 2 blocks
reference Call IDs from this table. A call discovered during Stage 2 must be added to this
table and assigned a Call ID before its block is written.]

| Call ID | System | Protocol | Call type |
|---------|--------|----------|-----------|
| INT-01  | [Named system] | [REST / AMQP / OData / GraphQL / MCP / gRPC / other] | [Create / Read / Update / Delete / Event publish / Event subscribe / Webhook / Token acquire / Health check / Other] |
[Include every cross-system boundary crossing: direct API calls, MCP tool invocations,
connector actions, event publishes, event subscribes, webhook callbacks, token acquisitions,
health checks, "background" calls, "assumed to work" calls, and calls to unknown systems.
Minimum two rows.]

[INVENTORY GATE: Stage 2 does not begin until this table has a row for every cross-system
call. No call may appear in a Stage 2 block whose Call ID is not present in this table.]

---

## STAGE 2: PER-CALL ANALYSIS BLOCKS

[Write one block per Call ID from the inventory. Block order follows Call ID order.
Each block contains five concern sections -- one concern per section. No section may
address more than one concern. Each block ends with a completion checklist. A block is
not complete until all five checklist items are marked. Do not begin a new block until
the previous block's checklist is fully marked.]

---

### Block INT-NN: [System + protocol]

**Section A -- Authentication**
[Concern: authentication only. Do not document format, error handling, or rate limits here.]

- Auth mechanism: [API key (header: [name]) / OAuth 2.0 Bearer (flow: [flow]) / service
  identity (MSI/managed identity) / shared secret (location: [vault/env/config]) /
  none (public -- intentional) / Unknown -- gap]
- Token expiry handling: [Handled in error path / Not handled -- gap / N/A]
- Credential rotation: [Documented policy / Not documented -- gap / N/A]
- Security note: [Any over-privileged scope, delegation chain risk, or auth concern.
  "None identified" is acceptable.]

**Section B -- Request and Response Format**
[Concern: call shape only. Do not document auth, error handling, or rate limits here.
All four fields are required as separate labeled lines.]

- Method: [HTTP method or protocol operation]
- Key request headers: [Authorization type, Content-Type, idempotency or correlation
  headers. Note incompleteness if schema is partial.]
- Body key fields: [Required request fields. "No body" for side-effect-free reads.]
- Expected response: [Status code(s) + key fields. Note error response shape if documented.]

**Section C -- Error Fate**
[Concern: error disposition only. Do not repeat auth or format content here. A call that
"never fails" still requires a disposition.]

- Error disposition: [Surfaced / Transformed (catches; raises [signal]) /
  Retried (strategy: [fixed/exponential], interval: [Xms], max: [N]) /
  Swallowed (logged; execution continues) / No handling]
- Gap flag: [-- / GAP: error swallowed -- execution continues silently / GAP: no handling /
  GAP: token expiry produces silent auth failure at runtime]

**Section D -- Rate Limit**
[Concern: rate limit exposure for this call's target system only. Do not repeat error or
auth content here.]

- Rate limit documented for [System]? [Yes / No -- exposure]
- If Yes: [calls/min, calls/day, token budget, or "Unknown"]
- Burst behavior: [Queued / rejected / delayed / unknown]
- Throttle response: [429 + Retry-After / silent drop / unknown]
- Gap flag: [-- / GAP: rate limit not documented -- exposure at sustained volume]

**Section E -- Retry and Idempotency**
[Concern: retry logic and idempotency only. Do not repeat error disposition or rate limit
content here.]

- Retry strategy: [Fixed interval / Exponential backoff (initial: [Xms], factor: [Y],
  max: [Zms]) / None]
- Jitter: [Yes / No / N/A]
- Idempotent by design? [Yes / No / Unknown]
- Mitigation if not: [X-Idempotency-Key header ([format]) / deduplication log /
  at-most-once delivery / None -- gap]
- Gap flag: [-- / GAP: no retry on transient-failure call / GAP: non-idempotent write
  without mitigation]

**Block Completion Checklist:**
[Mark each section. The block is not complete until all five are checked. Do not begin
the next block until this checklist is fully marked.]
- [ ] Section A (Auth): mechanism, expiry handling, rotation documented
- [ ] Section B (Format): method, headers, body, response documented as separate fields
- [ ] Section C (Error fate): disposition and gap flag documented
- [ ] Section D (Rate limit): limit documentation status and gap flag documented
- [ ] Section E (Retry/Idempotency): strategy and idempotency assessment documented

[Block INT-NN is complete when all five items are checked.]

---

[Repeat Block pattern for every Call ID in the inventory. The trace is not complete until
every Call ID from Stage 1 has a fully checked completion checklist.]

---

## GAP INVENTORY

[Collect all gap flags from all per-call blocks. One finding per gap flag. Reference
the Call ID and section letter.]

| Finding ID | Call ID | Section | Gap type | Description |
|------------|---------|---------|----------|-------------|
| GAP-01 | INT-NN | [A/B/C/D/E] | [Auth gap / Unknown auth / Token expiry not handled / Rate limit exposure / Error swallowing / No error handling / Missing retry / Missing idempotency / Credential rotation gap] | [One sentence describing the specific gap] |
[At minimum: every Section A "Unknown -- gap" auth, every Section C "GAP: error swallowed"
or "GAP: no handling" flag, every Section D "GAP: rate limit not documented", and every
Section E "GAP: non-idempotent write without mitigation" must appear here.]

---

## SEVERITY AND REMEDIATION

[Rank all findings. ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale.
HIGH findings also require a specific, call-context remediation.]

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|
| GAP-01 | HIGH / MEDIUM / LOW | [Why this severity -- required for HIGH, MEDIUM, and LOW: data loss / auth bypass / silent failure / latency spike / duplicate write / information leakage / audit exposure] | [HIGH only: specific fix. E.g., "Add X-Idempotency-Key: {topic}-{call-id}-{timestamp} to prevent duplicate resource creation on retry"; "Exponential backoff: initial=500ms, factor=2, max=30s, jitter=uniform(0,500ms) with Retry-After header respect on 429"; "Replace on-behalf-of token with client_credentials flow to eliminate user-token expiry as a runtime failure mode"] |
[Order: HIGH first, then MEDIUM, then LOW. Rationale is not optional for any row.
Leave Remediation blank for MEDIUM and LOW.]

---

Write artifact: simulations/flow/integration/{topic}-integration-{date}.md
Frontmatter: skill, topic, date, calls_inventoried, blocks_completed, auth_gaps, error_gaps,
rate_limit_gaps, idempotency_gaps, findings_count, high_severity_count.
```

---

## Variation Summary

| V | Axis | Key R2 differentiator | C-10 | C-11 | C-12 | C-08 fix |
|---|------|-----------------------|------|------|------|----------|
| **V-01** | Output format: V-05 repaired | Dedicated Request/Response section fixes C-03; happy-path column retained | Inventory table before subsections | Table + subsections are single-concern | "Happy path only?" column + pre-collection (partial) | MEDIUM/LOW rationale mandatory |
| **V-02** | Lifecycle: minimal gates | Gate condition text alone -- no prose. Tests whether V-04 verbosity is structural | GATE 1 before Phase 2 | One-line concern label per phase | Gate per phase covers all calls | MEDIUM/LOW rationale mandatory |
| **V-03** | Register: imperative upgraded | Pre-printed tables + MEDIUM/LOW rationale lifts 81 to golden without changing voice | Call list before Step 1 (partial) | Each step is one concern (partial) | CALL COMPLETE marker per call (partial) | Explicit MEDIUM/LOW rationale prompts |
| **V-04** | Role + Lifecycle: embedded Security | Security in Phase 2 Part B eliminates V-02's split-finding C-07 risk | GATE 1 before Phase 2 | Security is Part B of Phase 2 -- one concern per phase | Gate per phase, per-call table | MEDIUM/LOW rationale mandatory |
| **V-05** | Format + Lifecycle: per-call gate blocks | Five-concern checklist per call block directly instantiates C-12 (4 new pts) | INVENTORY GATE before Stage 2 | Each block section is one labeled concern | Named completion checklist per call block | MEDIUM/LOW rationale mandatory |

**Predicted top candidates:** V-05 directly targets C-12 (4 pts new in v2) with an
explicit per-call checklist that V-04 and V-01 lacked. V-04 embedded Security inherits
V-04 R1 structural discipline plus deeper auth coverage without the split-finding risk.
V-02 minimal gates is the architectural test: can gate conditions alone produce the same
structural discipline as V-04's verbose phases?

**Predicted floor:** V-03 upgraded -- the CALL COMPLETE marker is the weakest C-12
instantiation of the five variations. If the rubric requires an explicit all-calls
completion condition, "CALL COMPLETE" per-call markers may still read as implicit at
the section level.
