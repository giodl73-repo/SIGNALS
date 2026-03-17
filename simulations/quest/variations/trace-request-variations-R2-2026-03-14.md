Here are the 5 R2 variations:

---

## Summary

| V | Axis | Core mechanism | Predicted |
|---|------|----------------|-----------|
| **V-01** | Latency budget framing | Declare total budget; each boundary draws p50/p99; sequential chain sum = critical path via accounting, not post-hoc | 100/110 |
| **V-02** | Two-pass top-level structure | PASS 1 = traversal; PASS 2 = auth re-walk as coequal top-level sweep; C-11 structurally inescapable | 95/110 |
| **V-03** | Universal DISQUALIFIER blocks | Every section opens with explicit text-pattern failures ("may fail" / "standard auth" / "fast" / "lists sources without naming the chain") | 100/110 |
| **V-04** | Two-pass + latency budget + threat enumeration | C-11 via PASS 2, C-10 via budget exhaustion, C-09 via threat-class table before scenario selection | 105/110 |
| **V-05** | Full synthesis | R1 V-05 gate + table + boundary gate + budget column + PASS 2 + disqualifiers + threat table: every criterion has a structural mechanism | 110/110 |

**What changed from R1:**

The two new criteria (C-10, C-11) drove all five variation axes:

- **C-10 enforcement**: V-01's *latency budget* is the key novelty. Instead of asking "identify the critical path" after the trace, the model tracks sequential budget draws during the traversal — the critical path emerges from accounting. V-03 adds a DISQUALIFIER for the specific R1 failure pattern: listing sources without naming the sequential chain.

- **C-11 enforcement**: V-02 elevates the auth re-walk from R1's Phase 4 (subordinate phase) to **PASS 2** (coequal top-level pass). V-03 adds a DISQUALIFIER for the specific failure mode: a re-walk that mirrors inline auth fields without raising new questions.

- **C-09 upgrade**: V-04 and V-05 add a **threat enumeration table** (token abuse / payload abuse / concurrency / scope creep / trust abuse) before scenario selection. The model must evaluate all five classes and then select the highest-risk one overlapping with PASS 2 findings — targeting a real gap, not the easiest scenario.

- **R1 carry-forward**: V-05 preserves R1 V-05's boundary gate + table structure (proven for C-01/C-02/C-03/C-04) and layers all new mechanisms on top.
 inline findings and call it a re-walk.

- **C-09 (adversarial)**: V-04 and V-05 introduce threat enumeration before scenario selection: the model fills a threat-class table (token abuse / payload abuse / concurrency / scope creep / trust abuse), marks which apply, and then selects the highest-risk class to trace. This prevents the "pick whatever adversarial scenario is easiest" failure mode from R1.

- **Floor test**: V-02 — two-pass structure without budget framing or disqualifiers. If PASS 2 as a labeled top-level sweep alone produces C-11 compliance, the additional complexity in V-04/V-05 is not justified for this criterion.

- **R1 carry-forward**: The "may fail" disqualifier from R1 V-02's column rules is elevated to a universal header rule in V-03 and V-05. R1 V-05's boundary gate is preserved in V-05.

---

## V-01: Latency Budget Framing

**Axis**: Lifecycle emphasis — declares a total latency budget before the trace begins; each boundary draws from the budget at p50 and p99; sequential boundaries draw from the budget sequentially; parallel branches share a slot (only the longest draws); the critical path emerges from the sequential chain that exhausts the budget rather than being identified post-hoc

**Hypothesis**: When the model must track "remaining budget" across sequential hops during the traversal itself, the critical path is not a separate analytical task — it is the accounting output of the traversal. This is a stronger C-10 enforcement mechanism than asking "identify the critical path" after the trace: the model cannot complete the traversal without implicitly performing critical path analysis. C-05 (latency sources) is also strengthened because per-boundary latency is now budget-draw input, not optional annotation. Risk: the model may declare an unrealistic budget without grounding in SLA or timeout context; mitigated by requiring derivation from the first applicable source.

```
You are running /trace-request for: {{topic}}

Select your platform expert role from the request context:
- Dataverse platform expert (entity reads/writes, OData query pipeline, security roles, plugin
  execution pipeline, audit log emission)
- Commerce platform expert (pricing engine, cart session management, order lifecycle, payment
  gateway, tax service integration)
- Power Automate platform expert (trigger evaluation, action execution, connector API calls,
  flow runtime, throttle and retry behavior)

State your role before beginning.

---

## STEP 1 -- ENTRY POINT

Declare all four fields:

**Method / path / event**: [HTTP method + path, or event type + source for message-driven entry]
**Payload shape**: [Required fields, data types, size constraints -- not "a JSON body"]
**Caller identity**: [Service principal name, user identity type, anonymous -- be specific]
**Auth evidence at entry**: [Bearer token, API key, managed identity, session cookie, none]

---

## STEP 2 -- LATENCY BUDGET

Before tracing any boundary, declare the end-to-end latency budget for this request.
Derive it from the first source that applies:

1. A documented SLA or service contract for this operation (cite it)
2. The caller's configured request timeout (state the configured value)
3. A UX responsiveness threshold:
   - 500ms for interactive user-facing requests
   - 2000ms for synchronous background operations
   - 10000ms for async operations with visible progress indicator

**Budget: [N]ms** (source: [SLA reference / caller timeout value / UX threshold])

Budget accounting rules for the traversal:
- **Sequential boundaries**: each draws from the budget; draws sum on the critical path
- **Parallel branches**: only the longest branch draws; concurrent branches share the slot
- **Cached steps**: draw < 5ms on cache hit; draw their synchronous cost on cache miss

---

## STEP 3 -- BOUNDARY TRAVERSAL

For each boundary in traversal order, fill all fields. Continue until the response
reaches the original caller.

---

Boundary [N]: [name]
Draw type: [Sequential -- adds to critical path | Parallel with [boundary names] -- slot shared]
Budget draw (p50 / p99): [ms / ms]
Failure modes: [Concrete mechanism -- HTTP status code, timeout threshold + behavior, throttle
  rate + breach behavior, auth rejection type, payload validation rule, network failure class.
  "May fail" or "could error" without a named mechanism fails this field.]
Authorization: [Yes -- [exact permission, scope, or security role checked] | No -- AUTH GAP: [reason
  authorization is absent or assumed at this boundary]]
Cache behavior: [cached / not cached -- latency impact on draw]

---

[Repeat for every boundary from entry to response assembly. Token validation, gateway routing,
and audit emission are boundaries. Include them.]

---

## STEP 4 -- CRITICAL PATH ACCOUNTING

Review the budget draws and draw types from Step 3.

1. **Sequential chain** (these sum to the critical path):
   [boundary-1 -> boundary-2 -> ... -> boundary-N]

2. **Parallel branches excluded from chain**:
   [branch-A and branch-B run concurrently; only [the longer] adds to chain]

3. **Cached steps with near-zero draw**:
   [list steps that draw < 5ms on cache hit]

4. **Critical path cumulative p50**: [sum of sequential draws, p50] ms
   -- Headroom against [N]ms budget: [budget - p50] ms

5. **Critical path cumulative p99**: [sum of sequential draws, p99] ms
   -- Headroom (or overrun): [budget - p99] ms

6. **Dominant boundary**: [name -- p99 draw -- % of total chain p99]

---

## STEP 5 -- AUTHORIZATION RE-WALK

Return to the full boundary list from Step 3. Walk it a second time.
This pass focuses exclusively on authorization correctness.

For each boundary, answer:
1. Is the auth check at this boundary explicitly performed here, or assumed from an upstream
   result? If assumed: confirm what upstream check is relied upon, and whether a caller could
   reach this boundary without that upstream check executing.
2. Could a caller with adjacent permissions (broader scope, different role, borrowed service
   identity) reach a higher-privilege resource through this boundary?
3. Is the minimum required scope or role enforced? Or would a more permissive token also be
   accepted, granting unintended access?

**Required output**: Name at least one gap or privilege escalation path not surfaced in Step 3's
Authorization fields -- OR state: "Re-walk found no additional auth gaps --" followed by specific
justification for the three highest-risk boundaries confirming each is clean.

---

## STEP 6 -- ERROR PATH

Trace one complete error path from origination to caller response.
Select the highest-probability failure from Step 3.

Originating boundary: [name and step number]
Failure mode: [specific mechanism from Step 3]
At [next boundary]: [propagated unchanged / wrapped as {new type} / retried {N} times before
  giving up / swallowed -- caller receives no signal]
...
Caller receives: [status code + error body shape, or timeout, or silent empty response]

Show every boundary between origin and caller. Do not jump steps.

---

## STEP 7 -- ADVERSARIAL SCENARIO

Select one scenario most likely to expose a structural gap in this request's path -- target
a boundary where Step 5's re-walk found elevated risk:

- Expired or forged token on a multi-hop path where auth is not re-validated at every boundary
- Malformed payload that passes entry validation but fails a downstream domain constraint
- Concurrent callers mutating the same resource (two simultaneous requests, narrow window)
- Caller with broader-than-required scope accessing a sub-operation through an over-permissioned
  token at a boundary where minimum scope is not enforced

Adversarial condition: [specific input or state]
Divergence boundary: [exact boundary where path separates from nominal trace]
Path after divergence: [boundary-by-boundary outcome]
Outcome: [what the adversary achieves or receives -- name the impact]

---

## STEP 8 -- REMEDIATION

For every failure mode named in Step 3, provide one concrete remediation at the boundary
it targets:

- **Retry**: name algorithm (exponential backoff with jitter), max retry count, base delay, cap
- **Circuit breaker**: name error rate threshold, window duration, half-open probe interval
- **Missing permission**: name the exact scope or privilege to add, and which identity must carry it
- **Validation guard**: name the boundary, the field, and the validation rule

"Add error handling" or "improve resilience" fails. A specific mechanism at a named boundary passes.

---

## STEP 9 -- BATCH AND EDGE CASES

If this request type supports batch operations, pagination, or concurrent access:
- Name the platform limit (record count, payload size, rate ceiling) and which boundary enforces it
- Analyze N-1 (under limit), N (at limit), and N+1 (over limit) behavior
- State whether per-item processing overhead multiplies in batch mode and at which boundary

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## V-02: Two-Pass Top-Level Structure

**Axis**: Lifecycle emphasis -- the trace is structured as two explicitly labeled top-level passes: PASS 1 (primary traversal: failure modes, auth inline, latency) and PASS 2 (dedicated authorization audit); PASS 2 is a coequal structural element, not a phase subordinate to PASS 1; it runs after PASS 1 completes and must produce output regardless of PASS 1's auth findings

**Hypothesis**: In R1, V-04's PHASE 4 was the strongest C-04 enforcement mechanism (cited directly in the rubric as the source of C-11). V-02 R2 tests whether elevating the re-walk from a phase to a PASS -- architecturally coequal to the primary traversal -- produces stronger C-11 compliance. The separation also lets PASS 1's auth inline field focus on correctness during traversal without competing with re-walk concerns; PASS 2's exclusive focus may surface escalation paths that inline auth analysis misses. Risk: PASS 2 without a latency budget framing leaves C-10 (critical path) handled only by a PASS 1 ADDENDUM section, which is less structurally coercive than the budget accounting in V-01.

```
You are running /trace-request for: {{topic}}

Select your platform expert role from context:
- Dataverse platform expert (entity model, OData query pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing calculation, cart session, order lifecycle, payment
  gateway, tax service)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

State your role. This trace runs two passes. PASS 1 is the primary traversal.
PASS 2 is a dedicated authorization audit. Both are required. PASS 2 runs after PASS 1
completes -- not interleaved with it.

---

## ENTRY POINT

Before either pass, declare the full request entry point:

**Method / path / event**: [HTTP method + path, or event type + source]
**Payload**: [Required fields, data types, size constraints]
**Caller identity**: [Service principal, user identity type, anonymous -- be specific]
**Auth evidence**: [Bearer token, API key, managed identity, session cookie, none]

---

## BOUNDARY INVENTORY

Before PASS 1, list every boundary in traversal order. A boundary is crossed when:
a network call is made (HTTP, gRPC, SQL, message bus), identity context is evaluated,
or data is read from or written to a store.

Include: gateway, token validation, routing layer, each downstream service, each storage
operation (cache lookup counts), audit emission, response assembly.

Boundary inventory:
1. [Entry point -- as declared above]
2. [Second boundary]
3. [Third boundary]
...
[Continue until response is assembled and returned to caller]

[Complete this list before beginning PASS 1. Both passes will reference these boundary numbers.]

---

## PASS 1 -- PRIMARY TRAVERSAL

For each boundary in the inventory, fill all fields in traversal order:

**Boundary [N]: [name from inventory]**
Input crossing this boundary: [what is passed -- method, payload shape, token, message envelope]
Failure modes: [At least one concrete mechanism: HTTP status code, timeout threshold and
  behavior, throttle limit and breach behavior, auth rejection type (token expired / scope
  missing / role not assigned), payload validation rule, network failure class.
  "May fail" and "could error" without a named mechanism are not accepted.]
Auth inline: [Yes -- [exact permission, scope, or security role checked at this boundary] |
  No -- AUTH GAP: [specific reason authorization is absent or assumed here]]
Latency (p50 / p99): [ms estimates. "Fast" and "negligible" without numbers are not accepted.
  For sub-5ms: "< 5ms -- [reason]."]
Cache behavior: [cached / not cached -- impact on latency]

---

## PASS 1 ADDENDUM -- CRITICAL PATH

After completing all PASS 1 entries, identify the critical path.

The critical path is the specific sequence of boundaries whose cumulative p99 latency determines
worst-case end-to-end response time. Parallel paths and cached steps are excluded.

1. Sequential chain: [list boundary numbers/names in traversal order]
2. Parallel branches excluded: [which boundaries execute concurrently -- do not add to chain]
3. Cached steps contributing < 5ms on hit: [list]
4. Chain cumulative p50: [sum of sequential p50 values] ms
5. Chain cumulative p99: [sum of sequential p99 values] ms
6. Dominant boundary: [name -- its p99 contribution and % of total chain p99]

A critical path section that lists latency contributors without naming the sequential chain fails.

---

## PASS 2 -- AUTHORIZATION AUDIT

PASS 2 runs after PASS 1 is complete. Walk the full boundary inventory a second time.
This pass has a single focus: authorization correctness. Do not revisit failure modes or latency.

For each boundary from the inventory, answer three questions:

1. **Explicit or assumed?** Is the authorization check at this boundary explicitly performed here,
   or delegated to an upstream check? If delegated: name the upstream boundary that performs it,
   and confirm a caller cannot reach this boundary without that upstream check executing.

2. **Escalation path?** Could a caller with adjacent permissions -- a broader scope, a service
   identity borrowed from another service, or a role that includes this operation as a side-effect
   -- reach a higher-privilege resource through this boundary? Name the specific adjacent permission
   that would grant unintended access.

3. **Minimum enforced?** Is the scope or role evaluated at this boundary the minimum required for
   the operation? If a caller presents a more permissive token (e.g., admin scope when read scope
   suffices), is that accepted? If yes: is that the intended behavior?

**PASS 2 required output**: Name at least one gap or escalation path not raised in PASS 1's
Auth inline fields. Or state explicitly: "PASS 2 found no additional auth gaps --" followed by
specific clean confirmation for each of the three highest-risk boundaries in the inventory.

A PASS 2 that mirrors PASS 1's Auth inline column without raising new observations fails.

---

## ERROR PATH

After PASS 2, trace one complete error path from origination to caller response.
Select the highest-probability failure from PASS 1.

Originating boundary: [name and inventory number]
Failure mode: [mechanism from PASS 1]
At boundary [N+1]: [propagated unchanged / wrapped as {new type} / retried {N} times /
  swallowed -- caller receives no signal]
...
Caller receives: [status code + error body shape, or timeout, or silent empty response]

Show every boundary between origin and caller. Do not skip steps.

---

## ADVERSARIAL SCENARIO

Select one adversarial scenario targeting a gap identified in PASS 1 or PASS 2:
- A caller with valid credentials but insufficient scope for a specific sub-operation at a boundary
  where PASS 2 found assumed auth
- A token valid at the entry boundary but not re-validated at a downstream boundary PASS 2 flagged
- A malformed payload that passes entry-level schema validation but fails a domain constraint at
  a downstream boundary
- Concurrent callers mutating the same resource at the same boundary (narrow concurrency window)

Divergence boundary: [inventory number -- exact boundary where path splits from nominal]
Path after divergence: [boundary-by-boundary]
Outcome: [what the adversary achieves or receives -- name the concrete impact]

---

## REMEDIATION

For every failure mode from PASS 1 and every gap from PASS 2:

**Failure mode remediation**: specific mechanism at the named boundary (exponential backoff --
state algorithm, max retries, base delay; circuit breaker -- state threshold and probe interval;
payload validation guard -- state boundary and rule). "Add error handling" fails.

**Auth gap remediation**: exact scope or privilege to add, and the identity that must carry it.
"Improve authorization" fails.

---

## BATCH AND EDGE CASES

Platform limit, enforcement boundary, N-1/N/N+1 behavior, per-item overhead multiplication.
"Batch not applicable -- [specific reason]" if not applicable.
```

---

## V-03: Universal DISQUALIFIER Blocks

**Axis**: Output format -- every section opens with an explicit DISQUALIFIER block that names exact text patterns which auto-fail that criterion; the "may fail" prohibition from R1 V-02's column rules is elevated to a universal contract applied across all output sections, not just table cells; C-10 and C-11 each get their own DISQUALIFIER patterns

**Hypothesis**: Naming failure-mode text patterns upfront in negative-space form ("if you write any of these, you fail this criterion") is more effective than instructing the model what to produce. The instruction "name a concrete mechanism" competes with the model's prior training toward hedged language; the DISQUALIFIER "any response containing 'may fail' without a named mechanism fails this criterion" activates a constraint-satisfaction mode. Applied to C-10: the DISQUALIFIER pattern "lists latency sources without naming the sequential chain" prevents the R1 failure mode of listing individual contributors without identifying which sequence drives worst-case. Applied to C-11: "re-walk that mirrors primary traversal auth fields without raising new questions" prevents the re-walk from being a pro-forma repetition. Risk: disqualifier blocks add instruction surface without structural scaffolding (no gate, no table); a model may produce the disqualifier-compliant form with thin content.

```
You are running /trace-request for: {{topic}}

Select your platform expert role from context:
- Dataverse platform expert (entity model, OData pipeline, security roles, plugin execution, audit)
- Commerce platform expert (pricing, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls, flow runtime)

State your role: "I am the [role] for this trace."

---

## ENTRY POINT

**DISQUALIFIER**: Any entry point description matching these patterns fails C-01:
- "a POST request" or "a GET request" without the full path
- "a JSON body" or "a request payload" without named fields and types
- "an authenticated user" or "a service account" without the identity type and credential named

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

---

## BOUNDARY TRAVERSAL

**DISQUALIFIER for failure modes (C-03)**: Any failure mode field containing these patterns fails:
- "may fail"
- "could error" or "might error"
- "an exception might be thrown" or "an exception could occur"
- "errors may occur"
- "error handling required"
- "returns an error" without naming what error or what causes it

A failure mode must name a mechanism: HTTP 4xx/5xx status code (say which), timeout duration
and behavior on expiry, throttle rate limit and what the caller receives on breach, auth rejection
type (token expired / scope missing / role not assigned -- pick one), payload validation rule
that rejects the input, or a named network failure class (TLS failure, DNS timeout, etc.).

**DISQUALIFIER for authorization (C-04)**: Any auth field containing these patterns fails:
- "standard auth"
- "authenticated user" or "valid token" without the permission artifact named
- "authorization is handled upstream" without naming the upstream boundary
- "authorization is implicit" without explanation

For boundaries where auth is checked: name the exact artifact (security privilege, OAuth scope
name, Entra app permission, API key tier). For boundaries where auth is absent: write
"AUTH GAP -- [specific reason authorization is absent at this boundary]."

**DISQUALIFIER for latency (C-05)**: Any latency field containing these patterns fails:
- "fast" or "low latency" or "high latency" without a number
- "negligible" without a number and reason
- blank or omitted entirely

Required: p50 and p99 estimate in milliseconds or a range. For genuinely sub-5ms:
"< 5ms -- [specific reason why this step contributes near-zero latency]."

For each boundary in traversal order:

**Boundary: [name]**
Input: [what crosses this boundary]
Failure modes: [disqualifier conditions above apply]
Authorization: [disqualifier conditions above apply]
Latency (p50 / p99): [disqualifier conditions above apply]
Caching: [cached -- p50 draw / cache miss -- synchronous cost | not cached]

---

## CRITICAL PATH

**DISQUALIFIER (C-10)**: Any critical path section matching these patterns fails:
- Lists three or more latency sources without naming the sequential chain that drives worst-case
- States "the critical path goes through [service]" without listing the full chain
- Gives a single p99 figure without showing which boundaries are summed to produce it
- Omits whether parallel paths are excluded from the chain

Required: boundary names in sequential traversal order forming the critical path chain,
explicit identification of parallel branches excluded from the chain, cumulative p50 for
the chain, cumulative p99 for the chain, and the single dominant boundary.

Critical path chain: [boundary-1 -> boundary-2 -> ... -> boundary-N]
Excluded parallel branches: [list -- these execute concurrently and do not add to chain sum]
Excluded cached steps: [list -- contribute < 5ms on hit]
Chain cumulative p50: [ms]
Chain cumulative p99: [ms]
Dominant boundary: [name -- p99 contribution]

---

## AUTHORIZATION RE-WALK

**DISQUALIFIER (C-11)**: Any re-walk matching these patterns fails:
- Re-states auth fields from the boundary traversal without asking new questions about each boundary
- States "no additional auth gaps found" without per-boundary justification for high-risk boundaries
- Covers only the boundaries with AUTH GAP flags, ignoring boundaries where auth was marked present

Required: walk every boundary in the traversal list a second time, focused on privilege escalation
paths, scope gaps, and assumed-but-unverified auth. Must name at least one gap not surfaced in
the primary traversal -- or state "Re-walk found no additional gaps --" followed by specific
justification for the three highest-risk boundaries.

Re-walk the full boundary list. For each, assess:
1. Could a caller escalate privileges through this boundary's auth model?
2. Is auth assumed from upstream trust that may not have executed?
3. Is minimum-required scope enforced, or would over-permissioned tokens also be accepted?

---

## ERROR PATH

**DISQUALIFIER (C-06)**: Any error path section matching these patterns fails:
- "an error is returned to the caller" without showing the propagation chain
- "the error propagates through the system" without naming which boundaries it crosses
- Describes only the originating boundary and the final caller response, skipping intermediate
  boundaries

Required: origin boundary, behavior at each intermediate boundary (unchanged / wrapped / retried
/ swallowed), and exact caller response.

Trace one complete error path. Select the highest-probability failure from the boundary traversal.

Originating boundary: [name]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status code + error body, timeout, or silent empty response]

---

## ADVERSARIAL SCENARIO

Select the adversarial scenario most likely to expose a gap identified in the re-walk:
- Expired or forged token on a multi-hop path where auth is not re-validated at every boundary
- Malformed payload that bypasses entry validation but fails a downstream domain constraint
- Concurrent mutation of the same resource by two simultaneous callers
- Caller with broader scope than required accessing a sub-operation through an over-permissioned
  token at a boundary where minimum scope is not enforced

Adversarial condition: [specific input or state]
Divergence boundary: [exact boundary where path splits from nominal]
Path after divergence: [boundary-by-boundary]
Outcome: [what the adversary achieves or receives]

---

## REMEDIATION

**DISQUALIFIER (C-08)**: Any remediation matching these patterns fails:
- "add error handling"
- "improve resilience" or "add retry logic" without named values
- "fix the authorization gap" without naming the permission artifact to add
- "validate the input" without naming the boundary and validation rule

Required: specific mechanism at a named boundary. Accepted forms: exponential backoff (state
algorithm, max retries, base delay, cap), circuit breaker (state error rate threshold, window,
half-open behavior), permission scope addition (state exact scope name and identity that needs it),
payload validation guard (state boundary, field, and rule).

For every failure mode from the traversal and every gap from the re-walk, provide one concrete
remediation.

---

## BATCH AND EDGE CASES

Platform limit, enforcement boundary, N-1/N/N+1 behavior, per-item overhead multiplication.
"Batch not applicable -- [specific reason]" if not applicable.
```

---

## V-04: Two-Pass + Latency Budget + Threat Enumeration (Combination)

**Axes**: Two-pass top-level structure (C-11, from V-02) + latency budget framing (C-10, from V-01) + adversarial threat enumeration table (C-09 upgrade -- enumerate all applicable threat classes before selecting the highest-risk scenario rather than picking from a list)

**Hypothesis**: The two mechanisms that directly target the new rubric criteria (two-pass for C-11, latency budget for C-10) combined with an upgraded adversarial section that uses a threat enumeration table produce the highest aspirational criterion density. The threat table forces the model to evaluate all adversarial classes before selecting one, which should produce a more targeted scenario (one that targets a boundary actually flagged in PASS 2) rather than a generic "expired token" or "malformed payload" that is not specific to this request's structure. Risk: three combined mechanisms increase instruction surface; models may produce thin content per section to satisfy structural requirements without depth.

```
You are running /trace-request for: {{topic}}

Select your platform expert role:
- Dataverse platform expert (entity model, OData pipeline, security roles, plugin execution, audit)
- Commerce platform expert (pricing, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls, flow runtime)

State your role. This trace uses a declared latency budget and two passes.

---

## ENTRY POINT

**Method / path / event**: [HTTP method + path, or event type + source]
**Payload**: [Required fields, data types, size constraints]
**Caller identity**: [Service principal, user identity type, credential type]

---

## LATENCY BUDGET

Declare the end-to-end budget before beginning PASS 1.
Source priority:
1. Documented SLA (cite it)
2. Caller configured timeout (state the value)
3. UX threshold: 500ms (interactive) / 2000ms (synchronous background) / 10000ms (async)

**Budget: [N]ms** (source: [SLA / timeout / UX])

Budget accounting:
- Sequential boundaries: draws sum on the critical path
- Parallel branches: only the longest branch draws; concurrent branches share the slot
- Cached steps: draw < 5ms on hit; draw synchronous cost on miss

---

## BOUNDARY INVENTORY

List every boundary in traversal order before beginning PASS 1.

1. [Entry point]
2. [Second boundary]
3. ...

[PASS 1 and PASS 2 will reference these boundary numbers.]

---

## PASS 1 -- BOUNDARY TRAVERSAL

For each boundary in the inventory:

**Boundary [N]: [name]**
Draw type: [Sequential -- adds to critical path | Parallel with [boundary name(s)] -- slot shared]
Budget draw (p50 / p99): [ms / ms]
Failure modes: [Concrete mechanism. "May fail" without a named mechanism fails this field.]
Auth inline: [Yes -- [exact permission / scope / role] | No -- AUTH GAP: [reason]]
Cache behavior: [cached / not cached -- latency impact]

---

## PASS 1 ADDENDUM -- CRITICAL PATH ACCOUNTING

Review budget draws and draw types from PASS 1.

Sequential chain: [boundary names that are Sequential, in traversal order]
Parallel branches excluded from chain: [list -- concurrent, do not add to sum]
Cached steps (< 5ms on hit): [list]
Chain cumulative p50: [sum] ms -- headroom: [budget - p50] ms
Chain cumulative p99: [sum] ms -- headroom: [budget - p99] ms (negative = overrun)
Dominant boundary: [name -- p99 draw -- % of chain p99]

---

## PASS 2 -- AUTHORIZATION AUDIT

PASS 2 runs after PASS 1 completes. Walk the full boundary inventory a second time.
Exclusive focus: authorization correctness.

For each boundary, assess:
1. **Delegation**: Is the auth check explicit here, or assumed from upstream? If assumed: can
   a caller reach this boundary without the upstream check executing?
2. **Escalation**: Could a caller with adjacent permissions access a higher-privilege resource
   through this boundary? Name the specific permission set that would grant unintended access.
3. **Minimum scope**: Is minimum-required scope enforced? Would a broader token also pass?

**PASS 2 required output**: Name at least one gap or escalation path not raised in PASS 1's
Auth inline fields. Or: "PASS 2: no additional gaps --" with specific clean confirmation for
each of the three highest-risk boundaries.

A PASS 2 that repeats PASS 1's auth fields without new observations fails.

---

## THREAT ENUMERATION

Before selecting an adversarial scenario, enumerate which threat classes apply to this request:

| Threat class | Applies to this request? | Highest-risk boundary if yes |
|---|---|---|
| Token abuse (expired, forged, replayed credential) | Y / N | |
| Payload abuse (malformed, injection, over-size, schema-valid but domain-invalid) | Y / N | |
| Concurrency abuse (race condition, parallel mutation, stale read) | Y / N | |
| Scope creep (over-permissioned caller, minimum scope not enforced) | Y / N | |
| Trust abuse (forged service identity, misconfigured service-to-service trust) | Y / N | |

Select the Y row with the highest-risk boundary (prefer boundaries flagged in PASS 2).

---

## ADVERSARIAL SCENARIO

Selected threat: [class from table]
Adversarial condition: [specific input or state -- not a generic category, a specific instance]
Divergence boundary: [inventory number -- exact boundary where path separates from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Why this boundary: [one sentence explaining why this is the weakest point for this threat class
  based on PASS 1 and PASS 2 findings]

---

## ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from PASS 1.

Origin boundary: [name and inventory number]
Failure: [mechanism]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} / swallowed]
...
Caller receives: [status + body, timeout, or silent empty]

---

## REMEDIATION

For every failure mode from PASS 1 and every gap from PASS 2:

**Failure mode**: specific mechanism (retry -- algorithm and values; circuit breaker -- threshold
and probe interval; validation guard -- boundary and rule). Generic fails.

**Auth gap**: exact scope or privilege to add, and identity that must carry it. Generic fails.

---

## BATCH AND EDGE CASES

Platform limit, enforcement boundary, N-1/N/N+1 behavior, per-item overhead multiplication.
"Batch not applicable -- [specific reason]" if not applicable.
```

---

## V-05: Full Synthesis -- Boundary Gate + Table + Budget + Two-Pass + Disqualifiers + Threat Table

**Axes**: R1 V-05 (boundary inventory gate + per-boundary table + standalone adversarial section) + latency budget column (C-10, from V-01) + PASS 2 auth re-walk as a top-level section (C-11, from V-02) + DISQUALIFIER blocks per column (from V-03) + threat enumeration table before adversarial scenario (from V-04)

**Hypothesis**: Every criterion in the v2 rubric has at least one structural enforcement mechanism. C-01 (entry point declaration gate), C-02 (boundary inventory gate before table), C-03 (table column + DISQUALIFIER block), C-04 (table column + DISQUALIFIER block + PASS 2), C-05 (budget draw column -- latency is mandatory input, not optional annotation), C-06 (standalone error path section with chain requirement), C-07 (batch section), C-08 (remediation column + DISQUALIFIER block), C-09 (threat enumeration table forces all classes evaluated before selection), C-10 (budget accounting section -- critical path is the sequential chain sum, not a post-hoc identification), C-11 (PASS 2 as a top-level structural peer of PASS 1). The R1 V-05 boundary gate + table core provides the proven structural foundation; the R2 additions layer C-10/C-11/C-09 enforcement on top without replacing what worked.

```
You are running /trace-request for: {{topic}}

Select your platform expert role:
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

State your role before Step 1.

---

## STEP 1 -- ENTRY POINT

**DISQUALIFIER**: Entry points matching these patterns fail C-01:
"a POST request" (no path) / "a JSON body" (no field names) / "an authenticated user" (no credential type)

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

---

## STEP 2 -- LATENCY BUDGET

Declare the end-to-end latency budget before the boundary inventory:
1. Documented SLA (cite it), or
2. Caller configured timeout (state value), or
3. UX threshold: 500ms (interactive) / 2000ms (synchronous background) / 10000ms (async)

**Budget: [N]ms** (source: [SLA / timeout value / UX])

Accounting: sequential boundaries sum on the critical path. Parallel branches share a slot.
Cached steps draw < 5ms on hit; draw synchronous cost on miss.

---

## STEP 3 -- BOUNDARY INVENTORY (GATE)

List every boundary in traversal order. Do not fill Step 4's table until this inventory is complete.

A boundary: any transition where a network call is made, identity context is evaluated,
or data is read from or written to a store. Token validation, gateway routing, cache lookup,
and audit emission are boundaries.

1. [Entry point -- as declared in Step 1]
2. [Second boundary]
3. ...
[Continue until response is assembled and returned to caller]

[GATE: Every row in Step 4 must correspond to a boundary listed here, in the same order.
No boundary listed here may be absent from Step 4. No boundary may appear in Step 4 that
is not listed here.]

---

## STEP 4 -- PASS 1 TRAVERSAL TABLE

One row per boundary from Step 3. Every column is required. Column DISQUALIFIERS apply per cell.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | Budget Draw p50/p99 | Remediation |
|---|----------|-----------------|-------|---------------------------|---------------------|-------------|
| 1 | | | | | / | |
| 2 | | | | | / | |
| 3 | | | | | / | |

**Column DISQUALIFIERS:**

- **Failure Mode(s)**: FAILS if cell contains: "may fail," "could error," "might throw," "an
  exception could occur," "returns an error" without naming the error or cause. REQUIRED: HTTP
  status code, timeout threshold + behavior, throttle rate + breach behavior, auth rejection
  type (token expired / scope missing / role not assigned), payload validation rule, or
  network failure class.

- **Auth?**: Binary Y or N only.

- **Permission / Scope / Role**: FAILS for Y rows if cell contains: "standard auth," "valid
  token," "authenticated user," "authorization handled upstream" without naming the boundary.
  REQUIRED for Y rows: exact artifact (e.g., "Dataverse `prvReadAccount` security privilege,"
  "Commerce `orders.write` OAuth scope," "Automate `flows.run` Entra app permission").
  REQUIRED for N rows: "AUTH GAP -- [specific reason authorization is absent at this boundary]."

- **Budget Draw p50/p99**: FAILS if cell contains: "fast," "low," "negligible," or is blank.
  REQUIRED: ms value or range for p50 and p99. Sub-5ms: "< 5ms -- [reason]."
  Mark [Sequential] or [Parallel with boundary-N] per draw type.

- **Remediation**: FAILS if cell contains: "add error handling," "improve resilience," "handle
  the error," "add retry logic" without named values. REQUIRED: specific mechanism at this
  boundary (exponential backoff -- algorithm + max retries + base delay; circuit breaker --
  threshold + window + half-open; exact scope to add + identity; validation boundary + field + rule).

---

## STEP 5 -- CRITICAL PATH ACCOUNTING

Review the Budget Draw column and draw types from Step 4.

**DISQUALIFIER (C-10)**: Fails if: lists latency contributors without naming the chain / gives
a p99 without showing which boundaries sum to produce it / omits whether parallel paths are excluded.

Sequential chain: [boundary-1 -> boundary-2 -> ... -> boundary-N (Sequential draws only)]
Excluded parallel branches: [list -- execute concurrently, do not add to chain]
Excluded cached steps: [list -- < 5ms on hit]
Chain cumulative p50: [sum of Sequential p50 draws] ms -- headroom: [budget - p50] ms
Chain cumulative p99: [sum of Sequential p99 draws] ms -- headroom: [budget - p99] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

---

## STEP 6 -- PASS 2: AUTHORIZATION AUDIT

Walk the full boundary list from Step 3 a second time. Exclusive focus: authorization correctness.

**DISQUALIFIER (C-11)**: Fails if PASS 2 mirrors Step 4's Auth / Permission columns without
raising new questions. A PASS 2 is not a re-statement of inline auth fields.

For each boundary, assess:
1. **Delegation**: Is auth explicit here or assumed from an upstream check? If assumed: can a
   caller reach this boundary without the upstream check executing?
2. **Escalation**: Could adjacent permissions (broader scope, different role, borrowed identity)
   reach a higher-privilege resource through this boundary?
3. **Minimum enforcement**: Is the minimum required scope enforced? Would an over-permissioned
   token also be accepted?

**PASS 2 required output**: At least one gap or escalation path not raised in Step 4's auth
columns -- OR "PASS 2: no additional gaps --" with specific justification for the three
highest-risk boundaries confirming each is clean.

---

## STEP 7 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

**DISQUALIFIER (C-06)**: Fails if: states "error returned to caller" without propagation chain /
skips from origin to final response without showing intermediate boundaries.

Origin: [boundary name and Step 3 row number]
Failure: [mechanism from Step 4]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## STEP 8 -- THREAT ENUMERATION AND ADVERSARIAL SCENARIO

First, enumerate which threat classes apply to this request:

| Threat class | Applies? | Highest-risk boundary | PASS 2 flag? |
|---|---|---|---|
| Token abuse (expired, forged, replayed) | Y / N | | Y / N |
| Payload abuse (malformed, injection, domain-invalid) | Y / N | | Y / N |
| Concurrency abuse (race condition, parallel mutation) | Y / N | | Y / N |
| Scope creep (over-permissioned, minimum not enforced) | Y / N | | Y / N |
| Trust abuse (forged service identity, assumed delegation) | Y / N | | Y / N |

Select the Y row with the highest PASS 2 overlap (prefers a boundary flagged in Step 6).

Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Step 3 row number -- exact boundary where path splits from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [one sentence -- why this threat class at this boundary is the highest-risk
  based on Step 4 and Step 6 findings]

---

## STEP 9 -- BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Step 3 boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```
