**Round 3 Variations — flow-integration** written to `simulations/quest/variations/flow-integration-variations-R3-2026-03-14.md`.

---

## Summary

| V | Axis | Core Mechanism | Key R3 Hypothesis |
|---|------|----------------|-------------------|
| **V-01** | Role sequence: Expert-First | V-05 block structure + domain expert persona declared at inventory stage | Expert framing enriches C-01/C-02 discovery without touching the C-13/C-14/C-15 enforcement structure |
| **V-02** | Output format: Hybrid rate limits | Per-call blocks A–D + Section E cross-ref to shared per-system Rate Limit Registry | Can a registry cross-reference item satisfy C-14's fifth-concern slot? Eliminates duplicate rate limit entries for fan-out patterns |
| **V-03** | Lifecycle: Minimal gates + Phase 5 split | V-02 R2 gates compressed to conditions only; Phase 5 split into Phase 5a (Rate Limits) and Phase 5b (Retry/Idempotency) | Is splitting the Phase 5 header the minimum fix for C-11? Phase-based structure lacks call blocks — C-13/C-14 will test the boundary |
| **V-04** | Phrasing + lifecycle (combined) | Imperative register + Steps 1–5 each single-concern + CALL COMPLETE expanded from 3 to 5 concerns | Direct answer to R2 Open Q3: does the one-step CALL COMPLETE expansion lift V-03 R2's 108 to ceiling-level? |
| **V-05** | Output format + lifecycle (combined) | V-05 R2 per-call blocks with C-13/C-14/C-15 made maximally explicit — "You MUST NOT" exclusions, named LATE-CALL RULE box, dual-gate checklist | Structural ceiling: every new criterion instantiated with no-exception language; designed to score 123/123 |

**Key R3 questions being tested:**
1. Whether hybrid rate limit registry (V-02) passes C-14 with a cross-reference item as the fifth concern
2. Whether phase-based structure (V-03) can partially satisfy C-13/C-14 without call blocks
3. Whether imperative step-per-concern (V-04) satisfies C-13/C-14's "call block" requirement
4. Whether maximal explicitness in C-13/C-14/C-15 language (V-05) produces a clean 123/123
 NOT" exclusions, LATE-CALL RULE in a named box, checklist gate tied to both next block and trace completion | All three structurally instantiated with no-exception language; designed to score 123/123 |

**R2 open questions addressed:**
1. **V-02 rate limit redundancy** → hybrid per-system registry decouples rate limit docs from per-call repetition; Section E cross-ref preserves five-concern checklist scope
2. **V-03 Phase 5 split** → directly tests whether the single-line Phase 5a/5b split (vs V-05's full block rewrite) produces C-11 PASS at minimal structural cost
3. **V-04 CALL COMPLETE expansion** → directly tests R2 Open Q3: does expanding CALL COMPLETE from 3 to 5 concerns lift V-03's 108 to ceiling-level?

---

## V-01: Role Sequence — Expert-First

**Axis:** Role sequence — Backend Integration Domain Expert persona is declared at the start of the trace, framing call discovery and all per-call analysis sections. Expert role is active from inventory enumeration through severity ranking.

**Hypothesis:** Introducing the expert persona before the call inventory (rather than mid-trace or implicitly) increases the richness of C-01 discovery (unknown and assumed-to-work calls named) and C-02 depth (delegation chain, token expiry flagged proactively). The V-05 per-call block structure provides C-11/C-12/C-13/C-14/C-15 guarantees without modification.

```
You are a Backend Integration Domain Expert specializing in connectors, APIs, and MCP
integrations. Your job is to trace every cross-system call a feature makes and surface
authentication gaps, rate limit exposure, error swallowing, and missing idempotency.

You know from experience:
- The calls teams forget to list (background health checks, token acquisition calls,
  webhook receipts) are usually the ones with the worst auth and error handling.
- "Assumed to work" is a gap category, not an exclusion from the inventory.
- Unknown systems are not omitted — they are unknown-system entries in the inventory.

Apply this expertise at every stage below. Do not let familiarity with a system cause
you to skip fields.

---

## STAGE 1 — CALL INVENTORY

As the domain expert, your first task is to enumerate every cross-system call this feature
makes. Cast wide: include direct API calls, MCP tool invocations, connector actions, event
publishes and subscribes, webhook callbacks, token acquisition calls, and health checks.
Include calls you are certain about, calls you are assuming work, and calls to systems
you cannot fully identify.

**Complete this table before writing any Stage 2 block.**

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]
Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM

**INVENTORY GATE:** Stage 2 does not begin until every cross-system call the feature makes
has a row in this table. No per-call analysis of any kind appears in Stage 1.

**LATE-CALL RULE:** If you identify a call during Stage 2 analysis that is not listed here,
you must STOP, add it to this table with the next available Call ID, and THEN write its
call block. You may not write a call block for a call that has no inventory entry.

---

## STAGE 2 — PER-CALL ANALYSIS BLOCKS

As domain expert, analyze each Call ID in order. Complete all five sections and the
completion checklist before opening the next call block. Section order within each block
is fixed: A, B, C, D, E, then CHECKLIST.

---

### CALL BLOCK: [Call ID] — [System] ([Call Type])

#### Section A — Authentication
**Concern: authentication only. Do not document request format, error handling, rate limits,
or retry logic here. If you encounter format or retry information while analyzing auth,
note the section and defer — do not document it in Section A.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling (automatic refresh / manual rotation / unknown):
- Credential rotation policy (vault-managed / manual / unknown):
- Security note (delegation chain risk, elevation, missing application identity, or none):
- Gap flag (YES — [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B — Request and Response Format
**Concern: request and response format only. Do not document authentication, error handling,
rate limits, or retry logic here.**

- Method (HTTP verb or protocol operation):
- Key request headers (at minimum: Authorization type, Content-Type, correlation headers):
- Body key fields (list required fields; write "no body" for side-effect-free reads):
- Expected response shape (status code(s) + key fields):
- Incomplete fields noted (YES — list / NO):

All four fields are required as separate labeled lines. A single merged cell is not acceptable.

#### Section C — Error Fate
**Concern: error disposition only. Do not document authentication, request format, rate limits,
or retry logic here. If the call retries, write "retried — see Section E" and do not expand.**

- Disposition (surfaced / transformed / swallowed / retried — see Section E):
- Transformation detail (if applicable):
- Gap flag (YES — [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

A call that "never fails" is not exempt. Document what would happen if the external system
returned a 500.

#### Section D — Rate Limit Exposure
**Concern: rate limit exposure for this call's target system only. Do not document
authentication, request format, error handling, or retry logic here. If no rate limit is
documented, that absence is itself a gap — document it, do not omit it.**

- Documented rate limit (requests / time window):
- Burst risk (YES / NO / unknown):
- Throttle response (429 with Retry-After / silent drop / circuit breaker / unknown):
- Gap flag (YES — [RATE-EXPOSURE / RATE-UNKNOWN] / NO):

#### Section E — Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only. Do not document authentication,
request format, error handling, or rate limits here.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls (idempotency key header / deduplication / none):
- Gap flag (YES — [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### CALL BLOCK COMPLETION CHECKLIST
**Do not open the next call block until all five boxes are checked.**

- [ ] Section A (Auth) — all fields populated, gap flag set
- [ ] Section B (Format) — all four fields documented as separate labeled lines
- [ ] Section C (Error fate) — disposition stated, gap flag set
- [ ] Section D (Rate limit) — limit or exposure gap documented, gap flag set
- [ ] Section E (Retry/Idempotency) — strategy and idempotency documented, gap flag set

---

[Repeat the CALL BLOCK structure for each Call ID in Stage 1, in order.]

**The trace is not complete until every Call ID from Stage 1 has a call block with a
fully checked completion checklist.**

---

## STAGE 3 — GAP INVENTORY

As domain expert, collect every gap flag marked YES from every section of every call block.
Every YES gap flag must have a row here. Findings left inline in call blocks that do not
appear in this table are incomplete.

| Finding ID | Call ID | Section | Gap Type | Description |
|------------|---------|---------|----------|-------------|

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

At minimum this stage must contain:
- At least one AUTH finding
- At least one RATE-EXPOSURE or RATE-UNKNOWN finding
- At least one RETRY-NONE or IDEMPOTENCY-MISSING finding

---

## STAGE 4 — SEVERITY RANKING AND REMEDIATION

Rank every finding from Stage 3 by operational risk.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

Severity: HIGH (data loss / security breach) / MEDIUM (reliability / latency) / LOW (observability / maintenance)

Rules:
- ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale. No row is exempt.
- Every HIGH finding requires a concrete remediation specific to the call context. Acceptable
  forms: exact header name (e.g., `Idempotency-Key: {uuid-v4}`), exact backoff parameters
  (e.g., `initial: 1s / factor: 2 / max: 32s / jitter: ±25%`), specific flow replacement
  (e.g., "replace shared key with managed identity using [scope]").
- Generic advice ("add retry logic", "implement error handling") does not pass.
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, order by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-02: Output Format — Hybrid Per-Call Blocks + Per-System Rate Limit Registry

**Axis:** Output format — rate limits are documented in a shared per-system Rate Limit Registry (Stage 3), not inside call blocks. Call blocks use four concern sections (A–D) plus Section E as a registry cross-reference confirmation. The five-concern completion checklist uses the cross-reference as its fifth item.

**Hypothesis:** Decoupling rate limits from per-call blocks eliminates redundant entries when multiple calls target the same system, while Section E's registry-confirmation item preserves five-concern scope in the completion checklist. If C-14 passes with a cross-reference item, this structure provides cleaner rate limit documentation than V-05 for systems with fan-out call patterns.

```
Produce an integration trace using a hybrid structure: per-call blocks for authentication,
format, error fate, and retry/idempotency; a shared per-system registry for rate limits.
Both structures are gated. Follow all gate conditions exactly.

---

## STAGE 1 — CALL INVENTORY

List every cross-system call this feature makes. Include reads, writes, webhooks, event
publishes, event subscribes, token acquisition calls, health checks, and MCP tool
invocations. Include calls assumed to work and calls to systems you cannot fully identify.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM

**INVENTORY GATE:** No Stage 2 call block and no Stage 3 registry entry may be written
until this table is complete and every cross-system call has a row.

**LATE-CALL RULE:** If a call is identified during Stage 2 or Stage 3 that is not in this
table, add it here with the next available Call ID before writing its block or registry entry.

---

## STAGE 2 — PER-CALL ANALYSIS BLOCKS

Write one call block per Call ID. Sections within a block must be completed in order:
A, B, C, D, E, then CHECKLIST. Do not skip or reorder sections. Complete all sections
and the checklist before opening the next block.

---

### CALL BLOCK: [Call ID] — [System] ([Call Type])

#### Section A — Authentication
**Concern: authentication only. Do not document request format, error handling, rate limits,
or retry logic in this section.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling:
- Credential rotation policy:
- Security note (delegation chain, elevation risk, missing application identity, or none):
- Gap flag (YES — [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B — Request and Response Format
**Concern: request and response format only. Do not document authentication, error handling,
rate limits, or retry logic in this section.**

- Method:
- Key request headers:
- Body key fields:
- Expected response shape:
- Incomplete fields noted (YES — list / NO):

All four fields are required as separate labeled lines.

#### Section C — Error Fate
**Concern: error disposition only. Do not document authentication, request format, rate
limits, or retry logic in this section. If the call retries on error, write "retried —
see Section D" and do not expand here.**

- Disposition (surfaced / transformed / swallowed / retried — see Section D):
- Transformation detail (if applicable):
- Gap flag (YES — [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

A call that "never fails" still requires a disposition. Document what would happen on a 500.

#### Section D — Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only. Do not document authentication,
request format, error handling, or rate limits in this section.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls:
- Gap flag (YES — [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### Section E — Rate Limit Registry Confirmation
**Concern: confirmation that this call's target system has a row in the Stage 3 Rate Limit
Registry. Do not document the rate limit value here — rate limit content belongs in Stage 3.
Do not document authentication, format, error handling, or retry logic here.**

- Target system:
- Registry entry status (CONFIRMED — row exists in Stage 3 /
  NOT YET — add Stage 3 row before checking this box):

If the target system does not yet have a Stage 3 row, add it now before marking this
section complete.

#### CALL BLOCK COMPLETION CHECKLIST
**Do not open the next call block until all five boxes are checked.**

- [ ] Section A (Auth) — all fields populated, gap flag set
- [ ] Section B (Format) — all four fields as separate labeled lines, gap flag set
- [ ] Section C (Error fate) — disposition stated, gap flag set
- [ ] Section D (Retry/Idempotency) — strategy and idempotency documented, gap flag set
- [ ] Section E (Rate limit registry entry confirmed for this call's target system)

---

[Repeat the CALL BLOCK structure for each Call ID in Stage 1.]

**The trace is not complete until every Call ID from Stage 1 has a call block with a
fully checked completion checklist.**

---

## STAGE 3 — RATE LIMIT REGISTRY

One row per external system. If multiple calls in Stage 2 share a system, one row covers
all of them. Every system that appears as a target in any call block must have a row here.

| System | Calls Using It | Documented Limit | Burst Risk | Throttle Response | Gap Flag |
|--------|---------------|-----------------|-----------|------------------|---------|

Throttle responses: 429 with Retry-After / silent drop / circuit breaker / unknown
Systems with no documented limit: enter "No limit documented" in the Limit column and
"RATE-EXPOSURE" in the Gap Flag column.

**REGISTRY GATE:** Every unique system from Stage 1 must have a row in this table.
A system with no documented rate limit is not omitted — it is a row with an exposure gap.

---

## STAGE 4 — GAP INVENTORY

Collect all gap flags from Stage 2 (Sections A–D) and Stage 3 (rate limit exposure) into
one named list.

| Finding ID | Source | Section / Stage | Gap Type | Description |
|------------|--------|-----------------|----------|-------------|

Source: Call ID (for Sections A–D) or System name (for Stage 3)
Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

At minimum: one AUTH finding, one RATE-EXPOSURE or RATE-UNKNOWN finding, one RETRY-NONE
or IDEMPOTENCY-MISSING finding.

---

## STAGE 5 — SEVERITY RANKING AND REMEDIATION

Rank every finding from Stage 4.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

- ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale.
- Every HIGH finding requires a concrete remediation (exact header, backoff parameters,
  specific flow replacement). Generic advice does not pass.
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, order by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-03: Lifecycle — Minimal Gates + Phase 5 Split

**Axis:** Lifecycle emphasis — V-02 R2 minimal-gates structure with no prose explanations, gate conditions only. Phase 5 is split into Phase 5a (Rate Limits) and Phase 5b (Retry and Idempotency) — addressing the single structural failure that held V-02 R2 at 110. Per-phase exclusion statements at each phase header. Per-call completion table before GAP INVENTORY.

**Hypothesis:** Splitting Phase 5 into Phase 5a and Phase 5b is the minimum change to fix V-02 R2's C-11 PARTIAL (Phase 5 header named two concerns). Combined with per-call completion table (C-14 scope) and Late-Call Rule (C-15), the minimal-gate structure produces full C-11 without adopting V-05's per-call block wrapper.

```
Produce an integration trace. Work through phases in order. Gate conditions are blocking —
do not begin the next phase until the stated condition is true.

---

## PHASE 1 — CALL INVENTORY

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM
Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]

**GATE 1:** Phase 2 does not begin until this table has one row for every cross-system call
the feature makes. "Assumed to work" and "unknown system" calls are rows, not omissions.
Minimum two rows.

**LATE-CALL RULE:** Any call identified during Phases 2–5b that is not in this table must
be added here with the next available Call ID before its phase entry is written.

---

## PHASE 2 — AUTHENTICATION

One row per Call ID from Phase 1.

**Concern: authentication only. Do not document request format, error handling, rate limits,
or retry logic in this phase.**

| Call ID | Auth Mechanism | Token Expiry | Credential Rotation | Security Note | Gap Flag |
|---------|---------------|-------------|---------------------|--------------|---------|

Auth mechanisms: API-KEY / OAUTH-CLIENT-CREDS / OAUTH-AUTH-CODE / OAUTH-OBO /
SERVICE-IDENTITY / MTLS / NONE / UNKNOWN-GAP
Gap Flag: YES-[type] / NO

**GATE 2:** Phase 3 does not begin until every Call ID from Phase 1 has an auth mechanism
entry. "Unknown" is acceptable only with a gap flag.

---

## PHASE 3 — REQUEST AND RESPONSE FORMAT

One block per Call ID from Phase 1.

**Concern: request and response format only. Do not document authentication, error handling,
rate limits, or retry logic in this phase.**

**[INT-NN] — [System]**
- Method:
- Key request headers:
- Body key fields:
- Expected response shape:

All four fields are required as separate labeled lines.

**GATE 3:** Phase 4 does not begin until every Call ID from Phase 1 has all four fields
documented. A single merged "Request / Response" cell combining method, headers, body,
and response does not fire this gate.

---

## PHASE 4 — ERROR FATE

One row per Call ID from Phase 1.

**Concern: error disposition only. Do not document authentication, request format, rate
limits, or retry logic in this phase.**

| Call ID | Disposition | Detail | Gap Flag |
|---------|------------|--------|---------|

Dispositions: SURFACED / TRANSFORMED / SWALLOWED-GAP / RETRIED / NO-HANDLING-GAP
"A call that never fails" is not a valid disposition — document what would happen on a 500.
SWALLOWED and NO-HANDLING entries must carry a gap flag.

**GATE 4:** Phase 5a does not begin until every Call ID from Phase 1 has a disposition
entry with a gap flag column populated.

---

## PHASE 5a — RATE LIMITS

One row per unique external system from Phase 1.

**Concern: rate limit exposure only. Do not document authentication, request format, error
handling, or retry logic in this phase.**

| System | Documented Limit | Burst Risk | Throttle Response | Gap Flag |
|--------|-----------------|-----------|------------------|---------|

Systems with no documented limit: "No limit documented" in Limit column, "RATE-EXPOSURE"
in Gap Flag column. One row per system — not one row per call.

**GATE 5a:** Phase 5b does not begin until every unique system from Phase 1 has a row in
this table.

---

## PHASE 5b — RETRY AND IDEMPOTENCY

One row per Call ID from Phase 1.

**Concern: retry logic and idempotency only. Do not document authentication, request format,
error handling, or rate limits in this phase.**

| Call ID | Retry Strategy | Max Attempts | Jitter | Idempotency | Mitigation | Gap Flag |
|---------|---------------|-------------|--------|-------------|-----------|---------|

Retry strategies: EXPONENTIAL-BACKOFF / LINEAR / NONE-GAP
Idempotency: YES / NO-GAP / CONDITIONAL
Non-idempotent write calls without mitigation must carry a gap flag.

**GATE 5b:** The per-call completion checklist does not begin until every Call ID from
Phase 1 has all fields populated.

---

## PER-CALL COMPLETION CHECKLIST

Confirm that every Call ID has a complete entry in all five concern phases.

| Call ID | Ph 2 Auth | Ph 3 Format | Ph 4 Error | Ph 5a Rate | Ph 5b Idempotency | Complete? |
|---------|----------|------------|-----------|-----------|------------------|----------|

Mark each cell YES when the phase entry for that Call ID is fully populated with no blank
fields (other than non-applicable fields noted as N/A with reason).

**COMPLETION GATE:** GAP INVENTORY does not begin until every Call ID row shows Complete = YES.

---

## GAP INVENTORY

Collect all gap flags from Phases 2, 4, 5a, and 5b.

| Finding ID | Phase | Call ID / System | Gap Type | Description |
|------------|-------|-----------------|----------|-------------|

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

At minimum: one AUTH finding, one RATE-EXPOSURE or RATE-UNKNOWN finding, one RETRY-NONE
or IDEMPOTENCY-MISSING finding.

---

## SEVERITY RANKING AND REMEDIATION

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

- ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale.
- Every HIGH finding requires a concrete remediation (exact header, backoff parameters
  such as `initial: 1s / factor: 2 / max: 32s / jitter: ±25%`, or specific flow replacement).
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, order by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-04: Combined — Phrasing Register + Lifecycle (Imperative + 5-Concern CALL COMPLETE)

**Axis:** Phrasing register (imperative throughout) + lifecycle (one step per concern, Steps 1–5) + CALL COMPLETE checklist expanded to all five concerns + per-step-within-call concern exclusion statements.

**Hypothesis:** R2 V-03 scored 108 because (a) CALL COMPLETE covered only 3/5 concerns and (b) per-step multi-call processing made concern isolation harder. Restructuring to Steps 1–5 each addressed per-call-within-step (not per-concern-across-all-calls), expanding CALL COMPLETE to five concerns, and adding per-step exclusion statements should fix both issues. The imperative register is preserved throughout.

```
You are tracing integration calls for the feature below. Work through the steps in order.
Do not skip a step. Do not advance past a blocking condition until it is met.

---

## Step 0 — Build the Call List

List every cross-system call this feature makes. Include reads, writes, webhooks, event
publishes, event subscribes, token acquisition calls, and health checks. Include calls you
are assuming work. Include calls to systems you cannot identify — mark them UNKNOWN.

Assign IDs: INT-01, INT-02, etc.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|

**Do not begin Step 1 until every call is listed here.**

**LATE-CALL RULE:** If you discover a call during Steps 1–5 that is not in Step 0, stop,
add it here with the next Call ID, and then return to the step where you found it. Do not
process a call that has no Step 0 entry.

---

## Step 1 — Authentication (per call)

For each INT-NN, document the authentication mechanism.

**Step 1 concern: authentication only. Do not document request format, error handling,
rate limits, or retry logic in this step.**

For **INT-NN**:
- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling:
- Credential rotation policy:
- Gap flag (YES-[AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

Do not write "presumably uses auth" without naming the mechanism. Unknown mechanisms are
flagged as gaps, not omitted.

Repeat for every INT-NN from Step 0. Every INT-NN must have an entry before Step 2 begins.

---

## Step 2 — Request and Response Format (per call)

For each INT-NN, document the request and response shape.

**Step 2 concern: request and response format only. Do not document authentication, error
handling, rate limits, or retry logic in this step.**

For **INT-NN**:
- Method:
- Key request headers:
- Body key fields:
- Expected response shape:

Do not compress these four fields into one line. Each field is a separate labeled line.

Repeat for every INT-NN from Step 0. Every INT-NN must have all four fields before Step 3 begins.

---

## Step 3 — Error Fate (per call)

For each INT-NN, state what happens when this call fails.

**Step 3 concern: error disposition only. Do not document authentication, request format,
rate limits, or retry logic in this step.**

For **INT-NN**:
- Disposition (surfaced / transformed / swallowed / retried):
- Detail:
- Gap flag (YES-[ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

A call that "never fails" still requires a disposition. State what would happen on a 500.
If the call retries, mark the disposition as "retried" and document retry details in Step 5.

Repeat for every INT-NN from Step 0.

---

## CALL COMPLETE Marker (after Steps 1–3 for each INT-NN)

After completing Steps 1, 2, and 3 for an INT-NN, mark the first three boxes:

**INT-NN:**
- [ ] Step 1 (Auth) — complete
- [ ] Step 2 (Format) — complete
- [ ] Step 3 (Error fate) — complete
- [ ] Step 4 (Rate limit) — complete  ← fill in after Step 4
- [ ] Step 5 (Idempotency) — complete ← fill in after Step 5

Do not process the NEXT INT-NN's Steps 1–3 until the current INT-NN has the first three
boxes checked. After Step 4 and Step 5 are written for this call, check those boxes.

**The trace is not complete until every INT-NN has all five boxes checked.**

---

## Step 4 — Rate Limit Table (per system)

Build a rate limit table. One row per unique external system — not one row per call.

**Step 4 concern: rate limit exposure only. Do not document authentication, request format,
error handling, or retry logic in this step.**

| System | Calls Using It | Documented Limit | Burst Risk | Throttle Response | Gap Flag |
|--------|---------------|-----------------|-----------|------------------|---------|

Systems with no documented limit: enter "No limit documented" and set Gap Flag to RATE-EXPOSURE.

After completing this table, go back to every INT-NN CALL COMPLETE marker and check the
Step 4 box for each call whose target system now has a row.

---

## Step 5 — Retry and Idempotency (per call)

For each INT-NN, document retry logic and idempotency.

**Step 5 concern: retry logic and idempotency only. Do not document authentication, request
format, error handling, or rate limits in this step.**

| Call ID | Retry Strategy | Max Attempts | Jitter | Idempotency | Mitigation | Gap Flag |
|---------|---------------|-------------|--------|-------------|-----------|---------|

Retry strategies: EXPONENTIAL-BACKOFF / LINEAR / NONE-GAP
Non-idempotent write calls without mitigation must carry a gap flag.
"No retry" is valid — but transient failure calls with no retry are also a gap flag.

After completing this table, check the Step 5 box in every INT-NN CALL COMPLETE marker.

**Do not begin Step 6 until every INT-NN CALL COMPLETE marker has all five boxes checked.**

---

## Step 6 — Gap Inventory

Collect every gap flag from Steps 1, 3, 4, and 5 into a single list.

| Finding ID | Step | Call ID / System | Gap Type | Description |
|------------|------|-----------------|----------|-------------|

Do not leave findings inline in the steps above. Every YES gap flag must have a row here.

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

At minimum: one AUTH finding, one RATE finding, one RETRY or IDEMPOTENCY finding.

---

## Step 7 — Severity and Remediation

Rank every finding from Step 6.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

- ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale. No row is exempt.
- Every HIGH finding requires a specific remediation. Do not write "add error handling."
  Name the header (e.g., `Idempotency-Key: {uuid-v4}`), backoff parameters
  (e.g., `initial: 1s / factor: 2 / max: 32s / jitter: ±25%`), or the exact replacement flow.
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, order by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-05: Combined — Output Format + Lifecycle (V-05 Ceiling: C-13/C-14/C-15 Maximally Explicit)

**Axis:** Output format (per-call gate blocks) + lifecycle (staged gates). V-05 R2's winning structure with C-13, C-14, and C-15 language made maximally explicit: stronger "You MUST NOT" exclusion statements per section, a named LATE-CALL RULE box with no-exception language, and the five-concern checklist explicitly gating both the next call block and trace completion.

**Hypothesis:** V-05 R2 scored 112/112 on the old rubric. The three new R3 criteria (C-13, C-14, C-15) codify the exact patterns V-05 used. Making those patterns unambiguous in the prompt language — "You MUST NOT," named rule boxes, explicit dual-gate condition on the checklist — should produce 123/123 by leaving no room for the model to satisfy the letter but not the spirit of each criterion.

```
Produce an integration trace for the feature described below using per-call gate blocks.
Each call block contains five single-concern sections. Each section carries an explicit
concern exclusion. A five-concern completion checklist gates each block and the trace.

---

## STAGE 1 — CALL INVENTORY

List every cross-system call this feature makes. Include reads, writes, webhooks, event
publishes, event subscribes, token acquisition calls, health checks, and MCP tool
invocations. Include calls you are assuming work. Include calls to systems you cannot
fully identify — they are UNKNOWN-SYSTEM rows, not omissions.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM
Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]

**INVENTORY GATE:** Stage 2 does not begin until this table has a row for every
cross-system call the feature makes. No per-call analysis of any kind appears in Stage 1.

---

┌─────────────────────────────────────────────────────────┐
│ LATE-CALL RULE                                          │
│                                                         │
│ If you identify a call during Stage 2 analysis that     │
│ is not in this table, you must:                         │
│   1. STOP writing the current call block.               │
│   2. Add the call to the inventory table above with     │
│      the next available Call ID.                        │
│   3. THEN return and continue the call block.           │
│                                                         │
│ You may not write a call block for a call that has no   │
│ inventory entry. There are no exceptions — a call       │
│ discovered on the last block is subject to the same     │
│ rule as a call discovered on the first.                 │
└─────────────────────────────────────────────────────────┘

---

## STAGE 2 — PER-CALL ANALYSIS BLOCKS

Write one call block per Call ID from Stage 1. Section order within every block is fixed:
A, B, C, D, E, then CHECKLIST. Complete all five sections and the checklist before opening
the next block.

---

### CALL BLOCK: [Call ID] — [System] ([Call Type])

#### Section A — Authentication
**Concern: authentication only.**
**You MUST NOT document request format, error handling, rate limits, or retry logic in this
section. If you encounter format or retry information while analyzing auth, write the
section letter where it belongs and skip it here.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling (automatic refresh / manual rotation / unknown):
- Credential rotation policy (vault-managed / manual / unknown):
- Security note (delegation chain risk, missing application identity, elevation, or none):
- Gap flag (YES — [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B — Request and Response Format
**Concern: request and response format only.**
**You MUST NOT document authentication, error handling, rate limits, or retry logic in this
section.**

- Method (HTTP verb or protocol operation):
- Key request headers (at minimum: Authorization type, Content-Type; include idempotency
  and correlation headers if present):
- Body key fields (list required fields; "no body" for side-effect-free reads; note
  incompleteness explicitly):
- Expected response shape (status code(s) + key fields):
- Incomplete fields noted (YES — list which / NO):

All four fields are required as separate labeled lines. A merged cell that combines method,
headers, body, and response is not acceptable and does not satisfy this section.

#### Section C — Error Fate
**Concern: error disposition only.**
**You MUST NOT document authentication, request format, rate limits, or retry logic in this
section. If the call retries on error, write "retried — see Section E" and do not expand
the retry logic here.**

- Disposition (surfaced / transformed / swallowed / retried — see Section E):
- Transformation detail (if applicable; "N/A" if not transformed):
- Gap flag (YES — [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

"This call never fails" is not a valid disposition. Document what would happen if the
external system returned a 500, a 429, or a network timeout.

#### Section D — Rate Limit Exposure
**Concern: rate limit exposure for this call's target system only.**
**You MUST NOT document authentication, request format, error handling, or retry logic in
this section. Absence of documented rate limits is itself a gap — document it here, do
not omit it.**

- Documented rate limit (requests / time window / "no limit documented"):
- Burst risk (YES / NO / unknown):
- Throttle response (429 with Retry-After / silent drop / circuit breaker / unknown):
- Gap flag (YES — [RATE-EXPOSURE / RATE-UNKNOWN] / NO):

#### Section E — Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only.**
**You MUST NOT document authentication, request format, error handling, or rate limits in
this section.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls (idempotency key header / deduplication / none):
- Gap flag (YES — [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### CALL BLOCK COMPLETION CHECKLIST
**This checklist gates two things: (1) the next call block — do not open it until all five
boxes are checked; (2) trace completion — the trace is not complete until every Call ID
from Stage 1 has a call block with all five boxes checked here.**

- [ ] Section A (Auth) — all fields populated, gap flag set
- [ ] Section B (Format) — all four fields as separate labeled lines, gap flag set
- [ ] Section C (Error fate) — disposition stated (not "never fails"), gap flag set
- [ ] Section D (Rate limit) — limit or exposure-gap documented, gap flag set
- [ ] Section E (Retry/Idempotency) — strategy and idempotency documented, gap flag set

---

[Repeat the CALL BLOCK structure for each Call ID in Stage 1, in inventory order.]

---

## STAGE 3 — GAP INVENTORY

Collect every gap flag marked YES in any section of any Stage 2 call block. Use the
Call ID and section letter (A–E) as the reference. Findings left inline in call blocks
that do not appear in this table are incomplete.

| Finding ID | Call ID | Section | Gap Type | Description |
|------------|---------|---------|----------|-------------|

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

This stage must contain at minimum:
- At least one AUTH finding
- At least one RATE-EXPOSURE or RATE-UNKNOWN finding
- At least one RETRY-NONE or IDEMPOTENCY-MISSING finding

---

## STAGE 4 — SEVERITY RANKING AND REMEDIATION

Rank every finding from Stage 3.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

Severity: HIGH (data loss / security breach) / MEDIUM (reliability / latency) /
LOW (observability / maintenance)

Rules:
- **ALL findings — HIGH, MEDIUM, and LOW — require a one-line rationale. Rationale is
  not optional for any row, including LOW findings.**
- **Every HIGH finding requires a concrete, call-context-specific remediation.** Acceptable
  forms:
  - Exact header: `Idempotency-Key: {uuid-v4}` on POST /[endpoint]
  - Exact backoff: `initial: 1s / factor: 2 / max: 32s / jitter: ±25%, max attempts: 5`
  - Specific flow: "replace shared API key with managed identity using [scope] on
    [system] calls"
  Generic advice ("add retry logic", "implement error handling", "use idempotency") does
  not pass.
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, order by Call ID, then
  section letter.

---

Feature description:
[Insert feature description here.]
```
