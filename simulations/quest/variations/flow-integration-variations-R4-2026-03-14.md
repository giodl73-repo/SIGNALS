Written to `simulations/quest/variations/flow-integration-variations-R4-2026-03-14.md`.

---

## Round 4 Variations — flow-integration

**Situation:** v4 rubric adds C-16 (+expert persona before Stage 1) and C-17 (+in-block rate limit completeness), raising the ceiling from 123 to 137. V-01 R3 already had both patterns, so it should score 137/137 verbatim. V-05 R3 had no persona (C-16 FAIL). V-02 R3 used a registry cross-ref for rate limits (C-17 FAIL).

| V | Axis | Core Change from R3 | C-16 Form |
|---|------|---------------------|-----------|
| **V-01** | Role sequence: C-16 boundary | Minimal persona — domain + exactly 2 obligations; V-01 R3 blocks otherwise unchanged | 2 obligations (minimum) |
| **V-02** | Output format: Hybrid registry fixed | Section D restored to full in-block rate limit data; registry demoted to supplementary fan-out index; expert persona added | 4 obligations |
| **V-03** | Phrasing register: descriptive/guidance | "This section does not contain X, Y, Z, W" exclusion language instead of imperatives; tests C-13 pass with declarative register | 2 obligations |
| **V-04** | Combined: Lifecycle (Phase frame) + Role sequence | Phase 1-4 outer frame + CALL BLOCK inner units nested in Phase 2; tests R3 open Q3 definitively | 3 obligations |
| **V-05** | Combined: C-16 maximal + C-17 explicit anchor | V-05 R3 "You MUST NOT" language + richest possible persona (4 obligations + gap sensitivity) + explicit "three required separate fields" in Section D | Maximal (4 obligations + gap sensitivity) |

**Predicted scores:** V-01/V-02/V-03/V-05 → 137/137. V-04 → 137 if phase label is neutral, likely C-13/C-14 FAIL if phase framing triggers preamble interpretation.

**Key open questions being resolved:**
1. Is C-16 binary pass/fail at 2 obligations or does richness score within the pass band? (V-01 vs V-05 on C-16)
2. Does V-02's supplementary registry trigger C-11 "scanning elsewhere" even with Section D complete? (V-02 neutrality test)
3. Does Phase outer + call block inner satisfy C-13/C-14? (V-04 definitively answers R3 open Q3)
ests whether the call block architecture is the hard prerequisite or whether the "Phase" label triggers the preamble interpretation |
| **V-05** | Combined: Role sequence (C-16 maximal) + Output format (C-17 explicit) | V-05 R3 "You MUST NOT" structural language + richest possible expert persona (domain named richly, 4 discovery obligations, detailed gap sensitivity) + Section D with explicit C-17 anchor naming the three required fields | V-05 R3 scored 123/123 under v3 but had no persona (C-16 FAIL under v4). Adding the richest persona (C-16 maximal) + Section D language naming "limit value, burst risk, and throttle response are three required separate fields" (C-17 anchor) should produce ceiling with maximum semantic quality on both new criteria |

**Key R4 questions being tested:**
1. Whether the C-16 minimum-viable persona (two obligations) scores full credit vs a richer form
2. Whether V-02's hybrid registry reaches ceiling by adding full in-block Section D data while keeping the supplementary registry
3. Whether descriptive register satisfies C-13 ("This section does not contain X, Y, Z, W" = named exclusion)
4. Whether Phase outer frame + call block inner units satisfies C-13/C-14 (R3 open Q3)
5. Whether the richest possible C-16 persona + explicit C-17 Section D language produce maximum quality on both new criteria

---

## V-01: Role Sequence -- C-16 Minimal Compliant Expert Persona

**Axis:** Role sequence -- a minimal-viable expert persona is declared before Stage 1. It names the domain and exactly two discovery obligations, satisfying C-16 at the threshold without enrichment. The per-call block structure (V-01 R3) and full in-block rate limits (Section D) remain unchanged.

**Hypothesis:** The C-16 rubric pass condition is "names the domain and at least two discovery obligations." A persona that hits exactly two domain-specific obligations scores C-16 at full credit. If the rubric rewards richness beyond the pass threshold, V-01 R4 should score lower than V-05 R4 on C-16 semantics; if it is binary pass/fail, both score identically.

```
You are a Backend Integration Domain Expert. Your domain: connectors, APIs, and MCP
integrations between enterprise systems.

Your discovery obligations for this trace:
1. Forgotten-call inventory: token acquisition calls, health checks, and webhook receipts
   are systematically absent from first-pass inventories -- surface them.
2. Assumed-to-work gap entries: calls documented without verified auth or error handling
   are a gap category, not exclusions from the inventory.

Apply this expertise throughout. Do not skip fields because a system is familiar.

---

## STAGE 1 -- CALL INVENTORY

List every cross-system call this feature makes. Include reads, writes, webhooks, event
publishes, event subscribes, token acquisition calls, health checks, and MCP tool
invocations. Include calls assumed to work and calls to unknown systems.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM
Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]

**INVENTORY GATE:** Stage 2 does not begin until this table has a row for every
cross-system call the feature makes. No per-call analysis of any kind appears in Stage 1.

**LATE-CALL RULE:** If you identify a call during Stage 2 analysis that is not in this
table, you must STOP, add it here with the next available Call ID, and THEN write its
call block. You may not write a call block for a call that has no inventory entry.

---

## STAGE 2 -- PER-CALL ANALYSIS BLOCKS

Write one call block per Call ID from Stage 1, in inventory order. Complete all five
sections and the completion checklist before opening the next call block.

---

### CALL BLOCK: [Call ID] -- [System] ([Call Type])

#### Section A -- Authentication
**Concern: authentication only. Do not document request format, error handling, rate limits,
or retry logic here. If format or retry information surfaces here, note the section and
defer -- do not document it in Section A.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling (automatic refresh / manual rotation / unknown):
- Credential rotation policy (vault-managed / manual / unknown):
- Security note (delegation chain risk, missing application identity, elevation, or none):
- Gap flag (YES -- [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B -- Request and Response Format
**Concern: request and response format only. Do not document authentication, error handling,
rate limits, or retry logic here.**

- Method (HTTP verb or protocol operation):
- Key request headers (at minimum: Authorization type, Content-Type, correlation headers):
- Body key fields (list required fields; "no body" for side-effect-free reads):
- Expected response shape (status code(s) + key fields):
- Incomplete fields noted (YES -- list / NO):

All four fields are required as separate labeled lines.

#### Section C -- Error Fate
**Concern: error disposition only. Do not document authentication, request format, rate
limits, or retry logic here. If the call retries, write "retried -- see Section E".**

- Disposition (surfaced / transformed / swallowed / retried -- see Section E):
- Transformation detail (if applicable):
- Gap flag (YES -- [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

A call that "never fails" is not exempt. Document what would happen on a 500.

#### Section D -- Rate Limit Exposure
**Concern: rate limit exposure for this call's target system only. Do not document
authentication, request format, error handling, or retry logic here. Absence of a
documented limit is itself a gap -- document it here, do not omit it.**

- Documented rate limit (requests / time window):
- Burst risk (YES / NO / unknown):
- Throttle response (429 with Retry-After / silent drop / circuit breaker / unknown):
- Gap flag (YES -- [RATE-EXPOSURE / RATE-UNKNOWN] / NO):

#### Section E -- Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only. Do not document authentication,
request format, error handling, or rate limits here.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls (idempotency key header / deduplication / none):
- Gap flag (YES -- [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### CALL BLOCK COMPLETION CHECKLIST
**Do not open the next call block until all five boxes are checked.**

- [ ] Section A (Auth) -- all fields populated, gap flag set
- [ ] Section B (Format) -- all four fields documented as separate labeled lines
- [ ] Section C (Error fate) -- disposition stated, gap flag set
- [ ] Section D (Rate limit) -- limit or exposure gap documented, gap flag set
- [ ] Section E (Retry/Idempotency) -- strategy and idempotency documented, gap flag set

---

[Repeat the CALL BLOCK structure for each Call ID in Stage 1, in order.]

**The trace is not complete until every Call ID from Stage 1 has a call block with a
fully checked completion checklist.**

---

## STAGE 3 -- GAP INVENTORY

Collect every gap flag marked YES from every section of every Stage 2 call block.
Findings left inline in call blocks that do not appear in this table are incomplete.

| Finding ID | Call ID | Section | Gap Type | Description |
|------------|---------|---------|----------|-------------|

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

At minimum this stage must contain:
- At least one AUTH finding
- At least one RATE-EXPOSURE or RATE-UNKNOWN finding
- At least one RETRY-NONE or IDEMPOTENCY-MISSING finding

---

## STAGE 4 -- SEVERITY RANKING AND REMEDIATION

Rank every finding from Stage 3 by operational risk.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

Severity: HIGH (data loss / security breach) / MEDIUM (reliability / latency) /
LOW (observability / maintenance)

Rules:
- ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. No row is exempt.
- Every HIGH finding requires a concrete remediation specific to the call context.
  Acceptable forms: exact header name (e.g., Idempotency-Key: {uuid-v4}), exact backoff
  parameters (e.g., initial: 1s / factor: 2 / max: 32s / jitter: +/-25%), specific flow
  replacement (e.g., "replace shared key with managed identity using [scope]").
  Generic advice does not pass.
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, order by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-02: Output Format -- Hybrid Registry Fixed (C-17 PASS + Supplementary Fan-Out Registry)

**Axis:** Output format -- Section D is restored to full in-block rate limit data (limit value, burst risk, throttle response). The Rate Limit Registry in Stage 3 is demoted to a supplementary fan-out reference index populated from Section D entries, not the authoritative source. Expert persona added for C-16. Section E is back to Retry/Idempotency.

**Hypothesis:** V-02 R3 scored C-17 FAIL (Section E = registry cross-reference only; no limit value in call block) and C-11 PARTIAL (rate limit content outside call block). Moving rate limit data into Section D satisfies C-17; the supplementary registry preserves the fan-out consolidation benefit without moving any authoritative data outside the call block. C-11 is satisfied because "scanning elsewhere" for complete rate limit data is no longer required. With expert persona (C-16 PASS), this design should reach ceiling while preserving the registry readability benefit for high fan-out features.

```
You are a Backend Integration Domain Expert specializing in connectors, APIs, and MCP
integrations. Your job: trace every cross-system call a feature makes and surface
authentication gaps, rate limit exposure, error swallowing, and missing idempotency.

Your discovery obligations:
1. Forgotten-call categories: token acquisition calls, health checks, and webhook receipts
   are the calls most often absent from first-pass inventories -- include them.
2. Assumed-to-work entries: undocumented auth or unverified error handling is a gap entry,
   not a reason to skip the call.
3. Delegation chain risk: service-to-service calls that inherit credentials from a user
   context are a scope elevation and token expiry gap -- flag them in Section A.
4. Unknown systems: calls to systems you cannot identify are UNKNOWN-SYSTEM rows in the
   inventory, not omissions.

Apply this lens from inventory through severity ranking.

---

## STAGE 1 -- CALL INVENTORY

List every cross-system call this feature makes. Include reads, writes, webhooks, event
publishes, event subscribes, token acquisition calls, health checks, and MCP tool
invocations. Include calls assumed to work and calls to unknown systems.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM
Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]

**INVENTORY GATE:** Stage 2 does not begin until this table has a row for every
cross-system call the feature makes. No per-call analysis of any kind appears in Stage 1.

**LATE-CALL RULE:** If you identify a call during Stage 2 or Stage 3 that is not in this
table, you must STOP, add it here with the next available Call ID, and THEN continue.
You may not write a call block for a call that has no inventory entry.

---

## STAGE 2 -- PER-CALL ANALYSIS BLOCKS

Write one call block per Call ID from Stage 1. Complete all five sections and the
checklist before opening the next block. All rate limit data belongs in Section D of
each call block -- do not defer it to the Stage 3 registry.

---

### CALL BLOCK: [Call ID] -- [System] ([Call Type])

#### Section A -- Authentication
**Concern: authentication only. Do not document request format, error handling, rate limits,
or retry logic in this section.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling (automatic refresh / manual rotation / unknown):
- Credential rotation policy (vault-managed / manual / unknown):
- Security note (delegation chain risk, missing application identity, elevation, or none):
- Gap flag (YES -- [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B -- Request and Response Format
**Concern: request and response format only. Do not document authentication, error handling,
rate limits, or retry logic in this section.**

- Method (HTTP verb or protocol operation):
- Key request headers (at minimum: Authorization type, Content-Type, correlation headers):
- Body key fields (list required fields; "no body" for side-effect-free reads):
- Expected response shape (status code(s) + key fields):
- Incomplete fields noted (YES -- list / NO):

All four fields are required as separate labeled lines.

#### Section C -- Error Fate
**Concern: error disposition only. Do not document authentication, request format, rate
limits, or retry logic in this section. If the call retries on error, write
"retried -- see Section E" and do not expand retry logic here.**

- Disposition (surfaced / transformed / swallowed / retried -- see Section E):
- Transformation detail (if applicable):
- Gap flag (YES -- [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

"Never fails" is not a valid disposition. Document what would happen on a 500.

#### Section D -- Rate Limit Exposure
**Concern: rate limit exposure for this call's target system only. Do not document
authentication, request format, error handling, or retry logic in this section.
Document the actual rate limit data here, inside this block. Do not defer to Stage 3.
The Stage 3 registry is a supplementary fan-out index populated from this section --
it is not the authoritative source. Absence of a documented limit is itself a gap --
document it here, do not omit it.**

- Documented rate limit (requests / time window / "no limit documented"):
- Burst risk (YES / NO / unknown):
- Throttle response (429 with Retry-After / silent drop / circuit breaker / unknown):
- Gap flag (YES -- [RATE-EXPOSURE / RATE-UNKNOWN] / NO):

#### Section E -- Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only. Do not document authentication,
request format, error handling, or rate limits in this section.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls (idempotency key header / deduplication / none):
- Gap flag (YES -- [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### CALL BLOCK COMPLETION CHECKLIST
**Do not open the next call block until all five boxes are checked.**

- [ ] Section A (Auth) -- all fields populated, gap flag set
- [ ] Section B (Format) -- all four fields as separate labeled lines
- [ ] Section C (Error fate) -- disposition stated, gap flag set
- [ ] Section D (Rate limit) -- limit value, burst risk, throttle response documented
      in-block; gap flag set
- [ ] Section E (Retry/Idempotency) -- strategy and idempotency documented, gap flag set

---

[Repeat for each Call ID in Stage 1, in inventory order.]

**The trace is not complete until every Call ID from Stage 1 has a fully checked
completion checklist.**

---

## STAGE 3 -- RATE LIMIT REGISTRY (SUPPLEMENTARY)

One row per unique external system. This table is a convenience index for fan-out
reference -- the authoritative rate limit data is in Section D of each call block above.
Populate from Section D entries. Do not introduce rate limit data here that does not
already appear in a Section D.

| System | Calls Using It | Limit (from Section D) | Burst Risk | Throttle Response | Gap Flag |
|--------|---------------|----------------------|-----------|------------------|----------|

---

## STAGE 4 -- GAP INVENTORY

Collect every YES gap flag from Sections A-E of every Stage 2 call block into one named
list. Findings left inline in call blocks that do not appear here are incomplete.

| Finding ID | Call ID | Section | Gap Type | Description |
|------------|---------|---------|----------|-------------|

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

At minimum: one AUTH finding, one RATE-EXPOSURE or RATE-UNKNOWN finding, one RETRY-NONE
or IDEMPOTENCY-MISSING finding.

---

## STAGE 5 -- SEVERITY RANKING AND REMEDIATION

Rank every finding from Stage 4.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

Severity: HIGH (data loss / security breach) / MEDIUM (reliability / latency) /
LOW (observability / maintenance)

- ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. No row is exempt.
- HIGH findings require concrete, call-specific remediation: exact header name, exact
  backoff parameters, or specific flow replacement. Generic advice does not pass.
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-03: Phrasing Register -- Descriptive / Guidance Style

**Axis:** Phrasing register -- all instructions use declarative/guidance language ("A complete Stage 1 table has a row for every call..." / "This section does not contain X, Y, Z, W") rather than imperatives ("Do not begin until..." / "Do not document X here"). Same structural guarantees: expert persona (C-16), per-call blocks, five-concern sections, in-block concern exclusions (C-13), five-item completion checklist (C-14), late-call rule (C-15), full in-block rate limits (C-17).

**Hypothesis:** Per R3 finding, "You MUST NOT" vs "Do not" is aesthetic -- both satisfy C-13. Extending this principle: declarative exclusion statements within each section ("This section does not contain authentication, request format, rate limits, or retry logic") should satisfy C-13's "named exclusion of all other concerns" pass condition at the same score.

```
An integration trace maps every cross-system call a feature makes. A complete trace
covers authentication, request shape, error fate, rate limits, and idempotency for
each call, then collects gaps and ranks them by operational risk.

---

## Expert Framing

Before the inventory begins, adopt the perspective of a backend integration domain expert
specializing in connectors, APIs, and MCP integrations.

This expert's discovery lens carries two specific obligations:
- Forgotten call categories: token acquisition calls, health checks, and webhook receipts
  are the calls most often left off first-pass inventories. The expert expects them and
  looks for them.
- Assumed-to-work gap entries: "uses the standard connector" is not auth documentation
  -- it is a gap entry. Undocumented auth and unverified error handling belong in the
  inventory as gap-flagged rows, not as omissions.

Hold this lens from inventory through severity ranking.

---

## Stage 1 -- Call Inventory

A complete Stage 1 table has a row for every cross-system call the feature makes: reads,
writes, webhooks, event publishes, event subscribes, token acquisition calls, health
checks, and MCP tool invocations. Calls assumed to work are rows. Calls to unknown
systems are UNKNOWN-SYSTEM rows.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM
Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]

**Stage 2 begins when this table has a row for every cross-system call the feature makes.
No per-call analysis of any kind appears in Stage 1.**

**When a call is identified during Stage 2 that is not in this table, the right procedure
is to stop, add the call here with the next available Call ID, and then continue the call
block. A call block cannot be written for a call without an inventory row.**

---

## Stage 2 -- Per-Call Analysis Blocks

A well-formed Stage 2 contains one call block per Call ID. Each call block has five
sections in order -- A, B, C, D, E -- followed by a completion checklist. A section
covers exactly one integration concern and carries a statement of what it does not
contain. The checklist closes each block before the next one opens.

---

### Call Block: [Call ID] -- [System] ([Call Type])

#### Section A -- Authentication
**Concern: authentication only.
This section does not contain request format, error handling, rate limit data, or retry
logic. If format or retry information surfaces here, note the correct section and skip it.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling (automatic refresh / manual rotation / unknown):
- Credential rotation policy (vault-managed / manual / unknown):
- Security note (delegation chain risk, missing application identity, elevation, or none):
- Gap flag (YES -- [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B -- Request and Response Format
**Concern: request and response format only.
This section does not contain authentication, error handling, rate limit data, or retry
logic.**

- Method (HTTP verb or protocol operation):
- Key request headers (at minimum: Authorization type, Content-Type, correlation headers):
- Body key fields (list required fields; "no body" for side-effect-free reads):
- Expected response shape (status code(s) + key fields):
- Incomplete fields noted (YES -- list which / NO):

A well-formed Section B has four separate labeled lines. A single merged field combining
method, headers, body, and response is not a complete Section B.

#### Section C -- Error Fate
**Concern: error disposition only.
This section does not contain authentication, request format, rate limit data, or retry
logic. When the call retries on error, "retried -- see Section E" is the complete
disposition entry; retry details belong in Section E.**

- Disposition (surfaced / transformed / swallowed / retried -- see Section E):
- Transformation detail (if applicable):
- Gap flag (YES -- [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

A call that "never fails" still requires a disposition. The right question is what would
happen if the external system returned a 500 or a network timeout.

#### Section D -- Rate Limit Exposure
**Concern: rate limit exposure for this call's target system only.
This section does not contain authentication, request format, error handling, or retry
logic. The actual rate limit data -- limit value, burst risk, and throttle response --
is documented here, in this block. When the documented limit is unknown or undocumented,
that absence is a gap belonging in this section, not an omission.**

- Documented rate limit (requests / time window):
- Burst risk (YES / NO / unknown):
- Throttle response (429 with Retry-After / silent drop / circuit breaker / unknown):
- Gap flag (YES -- [RATE-EXPOSURE / RATE-UNKNOWN] / NO):

#### Section E -- Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only.
This section does not contain authentication, request format, error handling, or rate
limit data.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls (idempotency key header / deduplication / none):
- Gap flag (YES -- [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### Call Block Completion Checklist
**When all five boxes are checked, the next call block may open.
Stage 2 is not complete until every Call ID from Stage 1 has a fully checked checklist.**

- [ ] Section A (Auth) -- all fields populated, gap flag set
- [ ] Section B (Format) -- four fields as separate labeled lines, gap flag set
- [ ] Section C (Error fate) -- disposition stated (not "never fails"), gap flag set
- [ ] Section D (Rate limit) -- limit or exposure gap documented in-block, gap flag set
- [ ] Section E (Retry/Idempotency) -- strategy and idempotency documented, gap flag set

---

[Repeat the call block structure for each Call ID in Stage 1, in inventory order.]

---

## Stage 3 -- Gap Inventory

A complete Stage 3 collects every YES gap flag from Sections A-E of every Stage 2 call
block into one named table. Findings left inline in call blocks that do not appear here
are not complete.

| Finding ID | Call ID | Section | Gap Type | Description |
|------------|---------|---------|----------|-------------|

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

A complete Stage 3 contains at least one AUTH finding, one RATE-EXPOSURE or RATE-UNKNOWN
finding, and one RETRY-NONE or IDEMPOTENCY-MISSING finding.

---

## Stage 4 -- Severity Ranking and Remediation

Each finding from Stage 3 carries a severity label, a rationale, and -- for HIGH findings
-- a concrete remediation specific to the call context.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

Severity: HIGH (data loss / security breach) / MEDIUM (reliability / latency) /
LOW (observability / maintenance)

Every finding -- HIGH, MEDIUM, and LOW -- requires a one-line rationale. No finding is
exempt, including LOW.

A HIGH remediation names the exact header, the exact backoff parameters, or the specific
flow replacement. "Add retry logic" is not a remediation.

Order: HIGH first, then MEDIUM, then LOW. Within each tier, by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-04: Combined -- Lifecycle (Phase Frame + Call Block Inner Units) + Role Sequence (3 Obligations)

**Axis:** Lifecycle emphasis (Phase 1-4 outer frame with phase-level gates) + Role sequence (expert persona with three discovery obligations). Phase 2 contains per-call CALL BLOCK sub-structures -- each call block carries per-section concern exclusions and a five-item completion checklist.

**Hypothesis:** R3 open Q3: phase-based V-03 and step-based V-04 both failed C-13/C-14 because concern exclusion statements were at the phase/step header (a preamble for all calls) and no call block structural unit existed. This variation keeps the Phase outer frame but nests per-call CALL BLOCKs inside Phase 2. C-13 exclusion statements appear within each section inside each call block (not at the phase header level). C-14 checklist appears inside each call block and gates the next block (not the next phase). If the per-call block architecture is the hard prerequisite -- not the "Phase" label -- this design should score C-13 and C-14 at full credit.

```
You are a Backend Integration Domain Expert specializing in connectors, APIs, and MCP
integrations. Your job: trace every cross-system call a feature makes, then surface
authentication gaps, rate limit exposure, error swallowing, and missing idempotency.

Your discovery obligations:
1. Forgotten calls: token acquisition calls, health checks, and webhook receipts are
   systematically absent from first-pass inventories -- surface them.
2. Assumed-to-work gap entries: calls documented without verified auth or error handling
   are gap entries, not exclusions.
3. Delegation chains: service-to-service calls that inherit user credentials are a scope
   elevation and token expiry risk -- flag them in Section A.

Work through each phase in order. Phase gates are blocking.

---

## PHASE 1 -- CALL INVENTORY

List every cross-system call this feature makes: reads, writes, webhooks, event publishes,
event subscribes, token acquisition calls, health checks, and MCP tool invocations.
Include calls assumed to work and calls to unknown systems.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM
Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]

**PHASE 1 GATE:** Phase 2 does not begin until every cross-system call has a row in
this table. No per-call analysis of any kind appears in Phase 1.

**LATE-CALL RULE:** Any call identified during Phase 2 that is not in this table must be
added here with the next available Call ID before its call block is opened. A call block
may not be written for a call without a Phase 1 entry.

---

## PHASE 2 -- PER-CALL ANALYSIS

Process each Call ID from Phase 1 inside a dedicated call block. Open one call block at
a time. Complete all five sections and the completion checklist before opening the next
call block.

---

### CALL BLOCK: [Call ID] -- [System] ([Call Type])

#### Section A -- Authentication
**Concern: authentication only. Do not document request format, error handling, rate
limits, or retry logic in this section.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling (automatic refresh / manual rotation / unknown):
- Credential rotation policy (vault-managed / manual / unknown):
- Security note (delegation chain risk, missing application identity, elevation, or none):
- Gap flag (YES -- [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B -- Request and Response Format
**Concern: request and response format only. Do not document authentication, error
handling, rate limits, or retry logic in this section.**

- Method (HTTP verb or protocol operation):
- Key request headers (at minimum: Authorization type, Content-Type, correlation headers):
- Body key fields (list required fields; "no body" for side-effect-free reads):
- Expected response shape (status code(s) + key fields):
- Incomplete fields noted (YES -- list / NO):

All four fields are required as separate labeled lines.

#### Section C -- Error Fate
**Concern: error disposition only. Do not document authentication, request format, rate
limits, or retry logic in this section. If the call retries on error, write
"retried -- see Section E" and do not expand retry logic here.**

- Disposition (surfaced / transformed / swallowed / retried -- see Section E):
- Transformation detail (if applicable):
- Gap flag (YES -- [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

"Never fails" is not a valid disposition. Document what would happen on a 500.

#### Section D -- Rate Limit Exposure
**Concern: rate limit exposure for this call's target system only. Do not document
authentication, request format, error handling, or retry logic in this section.
Absence of a documented limit is itself a gap -- document it here, do not omit it.**

- Documented rate limit (requests / time window / "no limit documented"):
- Burst risk (YES / NO / unknown):
- Throttle response (429 with Retry-After / silent drop / circuit breaker / unknown):
- Gap flag (YES -- [RATE-EXPOSURE / RATE-UNKNOWN] / NO):

#### Section E -- Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only. Do not document authentication,
request format, error handling, or rate limits in this section.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls (idempotency key header / deduplication / none):
- Gap flag (YES -- [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### CALL BLOCK COMPLETION CHECKLIST
**Do not open the next call block until all five boxes are checked.**

- [ ] Section A (Auth) -- all fields populated, gap flag set
- [ ] Section B (Format) -- four separate labeled lines, gap flag set
- [ ] Section C (Error fate) -- disposition stated, gap flag set
- [ ] Section D (Rate limit) -- limit or exposure gap documented in-block, gap flag set
- [ ] Section E (Retry/Idempotency) -- strategy and idempotency documented, gap flag set

---

[Repeat for each Call ID from Phase 1, one call block at a time.]

**Phase 2 is not complete until every Call ID from Phase 1 has a call block with a
fully checked completion checklist.**

---

## PHASE 3 -- GAP INVENTORY

Collect every YES gap flag from Sections A-E of every Phase 2 call block into one named
table. Findings left inline in call blocks that do not appear here are incomplete.

| Finding ID | Call ID | Section | Gap Type | Description |
|------------|---------|---------|----------|-------------|

Gap types: AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION / RATE-EXPOSURE / RATE-UNKNOWN /
ERROR-SWALLOW / ERROR-UNTRANSFORMED / RETRY-NONE / IDEMPOTENCY-MISSING / FORMAT-INCOMPLETE / OTHER

At minimum: one AUTH finding, one RATE-EXPOSURE or RATE-UNKNOWN finding, one RETRY-NONE
or IDEMPOTENCY-MISSING finding.

---

## PHASE 4 -- SEVERITY RANKING AND REMEDIATION

Rank every finding from Phase 3 by operational risk.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

Severity: HIGH (data loss / security breach) / MEDIUM (reliability / latency) /
LOW (observability / maintenance)

- ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. No row is exempt.
- HIGH findings require concrete, call-specific remediation: exact header name, exact
  backoff parameters, or specific flow replacement. Generic advice does not pass.
- Order: HIGH first, then MEDIUM, then LOW. Within each tier, by Call ID.

---

Feature description:
[Insert feature description here.]
```

---

## V-05: Combined -- Expert Persona Maximal (C-16 Richest) + Structural Ceiling (C-17 Explicit)

**Axis:** Role sequence (richest possible C-16 persona: domain named richly, four discovery obligations, detailed gap sensitivity) + Output format (V-05 R3 "You MUST NOT" structural language, plus explicit C-17 anchor in Section D naming the three required fields and prohibiting cross-reference substitution).

**Hypothesis:** V-05 R3 scored 123/123 under v3 but had no expert persona (C-16 FAIL under v4). Adding the richest possible expert persona satisfies C-16 at maximum semantic quality. Section D in V-05 R3 already had full rate limit data, but adding an explicit anchor statement naming the three required fields ("limit value, burst risk, and throttle response are three required separate labeled fields -- a registry reference in place of these fields is not acceptable") ensures C-17 with no ambiguity. Combined: ceiling with highest possible semantic quality on both new criteria.

```
You are a Backend Integration Domain Expert specializing in enterprise connector and API
integration patterns: OAuth delegation chains, MCP tool invocations, Power Automate
connector actions, REST and GraphQL APIs, event bus subscriptions, and cross-tenant
API access.

Your job: trace every cross-system call a feature makes and surface the integration
failure modes that cause production incidents.

Your discovery obligations:
1. Forgotten call categories: token acquisition calls, health probe endpoints, and
   webhook receipt handlers are the calls teams most systematically omit. You know to
   look for them before closing the inventory.
2. Assumed-to-work gap entries: "uses the platform connector" or "standard auth" without
   named mechanism and token lifetime is an AUTH-MISSING entry in the inventory, not a
   basis for skipping the call.
3. Delegation chains: service-to-service calls that acquire tokens in the context of a
   calling user (OBO flows, impersonation) carry scope elevation and token expiry risk.
   They get their own delegation chain note in Section A.
4. Unknown systems: external dependencies you cannot fully identify are UNKNOWN-SYSTEM
   rows. Identification gaps are documented, not used as grounds for omission.

Your gap sensitivity: authentication gaps that surface as 401 storms, rate limit exposure
that shows up as 429 cascades, error swallowing that produces silent data loss,
idempotency gaps that create duplicate writes under retry.

Apply this full lens from inventory enumeration through severity ranking.

---

## STAGE 1 -- CALL INVENTORY

List every cross-system call this feature makes. Include reads, writes, webhooks, event
publishes, event subscribes, token acquisition calls, health checks, and MCP tool
invocations. Include calls assumed to work. Include calls to systems you cannot fully
identify -- they are UNKNOWN-SYSTEM rows, not omissions.

| Call ID | System | Protocol | Call Type | Status |
|---------|--------|----------|-----------|--------|
| INT-01  |        |          |           |        |

Status: KNOWN / ASSUMED / UNKNOWN-SYSTEM
Call types: read / write / webhook / event-publish / event-subscribe / token-acquire /
health-check / stream / other:[specify]

**INVENTORY GATE:** Stage 2 does not begin until this table has a row for every
cross-system call the feature makes. No per-call analysis of any kind appears in Stage 1.

---

+----------------------------------------------------------+
| LATE-CALL RULE                                           |
|                                                          |
| If you identify a call during Stage 2 analysis that      |
| is not in this table, you must:                          |
|   1. STOP writing the current call block.                |
|   2. Add the call to the inventory table above with      |
|      the next available Call ID.                         |
|   3. THEN return and continue the call block.            |
|                                                          |
| You may not write a call block for a call that has no    |
| inventory entry. There are no exceptions -- a call       |
| discovered on the last block is subject to the same      |
| rule as a call discovered on the first.                  |
+----------------------------------------------------------+

---

## STAGE 2 -- PER-CALL ANALYSIS BLOCKS

Write one call block per Call ID from Stage 1, in inventory order. Complete all five
sections and the completion checklist before opening the next block.

---

### CALL BLOCK: [Call ID] -- [System] ([Call Type])

#### Section A -- Authentication
**Concern: authentication only.**
**You MUST NOT document request format, error handling, rate limits, or retry logic in
this section. If you encounter format or retry information while analyzing auth, write
the section letter where it belongs and skip it here.**

- Auth mechanism (API key / OAuth token / service identity / mTLS / none):
- Token expiry handling (automatic refresh / manual rotation / unknown):
- Credential rotation policy (vault-managed / manual / unknown):
- Security note (delegation chain risk, missing application identity, elevation, or none):
- Gap flag (YES -- [AUTH-MISSING / AUTH-EXPIRY / AUTH-DELEGATION] / NO):

#### Section B -- Request and Response Format
**Concern: request and response format only.**
**You MUST NOT document authentication, error handling, rate limits, or retry logic in
this section.**

- Method (HTTP verb or protocol operation):
- Key request headers (at minimum: Authorization type, Content-Type; include idempotency
  and correlation headers if present):
- Body key fields (list required fields; "no body" for side-effect-free reads; note
  incompleteness explicitly):
- Expected response shape (status code(s) + key fields):
- Incomplete fields noted (YES -- list which / NO):

All four fields are required as separate labeled lines. A merged cell that combines
method, headers, body, and response is not acceptable and does not satisfy this section.

#### Section C -- Error Fate
**Concern: error disposition only.**
**You MUST NOT document authentication, request format, rate limits, or retry logic in
this section. If the call retries on error, write "retried -- see Section E" and do not
expand the retry logic here.**

- Disposition (surfaced / transformed / swallowed / retried -- see Section E):
- Transformation detail (if applicable; "N/A" if not transformed):
- Gap flag (YES -- [ERROR-SWALLOW / ERROR-UNTRANSFORMED] / NO):

"This call never fails" is not a valid disposition. Document what would happen if the
external system returned a 500, a 429, or a network timeout.

#### Section D -- Rate Limit Exposure
**Concern: rate limit exposure for this call's target system only.**
**You MUST NOT document authentication, request format, error handling, or retry logic
in this section.**
**The three required fields for this section are: (1) documented rate limit value,
(2) burst risk, and (3) throttle response. These are three separate labeled fields.
A cross-reference to an external registry is not a substitute for these fields.
If the rate limit is unknown or undocumented, document that absence as a gap here --
do not defer it to a registry or omit it.**

- Documented rate limit (requests / time window / "no limit documented"):
- Burst risk (YES / NO / unknown):
- Throttle response (429 with Retry-After / silent drop / circuit breaker / unknown):
- Gap flag (YES -- [RATE-EXPOSURE / RATE-UNKNOWN] / NO):

#### Section E -- Retry Logic and Idempotency
**Concern: retry logic and idempotency for this call only.**
**You MUST NOT document authentication, request format, error handling, or rate limits
in this section.**

- Retry strategy (exponential backoff / linear / none):
- Parameters (initial delay / backoff factor / max delay / jitter):
- Max attempts:
- Idempotency guarantee (YES / NO / conditional):
- Mitigation for non-idempotent calls (idempotency key header / deduplication / none):
- Gap flag (YES -- [RETRY-NONE / IDEMPOTENCY-MISSING] / NO):

#### CALL BLOCK COMPLETION CHECKLIST
**This checklist gates two things: (1) the next call block -- do not open it until all
five boxes are checked; (2) trace completion -- the trace is not complete until every
Call ID from Stage 1 has a call block with all five boxes checked here.**

- [ ] Section A (Auth) -- all fields populated, gap flag set
- [ ] Section B (Format) -- all four fields as separate labeled lines, gap flag set
- [ ] Section C (Error fate) -- disposition stated (not "never fails"), gap flag set
- [ ] Section D (Rate limit) -- limit value, burst risk, and throttle response each
      documented as separate labeled fields in-block; gap flag set
- [ ] Section E (Retry/Idempotency) -- strategy and idempotency documented, gap flag set

---

[Repeat the CALL BLOCK structure for each Call ID in Stage 1, in inventory order.]

---

## STAGE 3 -- GAP INVENTORY

Collect every gap flag marked YES in any section of any Stage 2 call block. Use the
Call ID and section letter (A-E) as the reference. Findings left inline in call blocks
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

## STAGE 4 -- SEVERITY RANKING AND REMEDIATION

Rank every finding from Stage 3.

| Finding ID | Severity | Rationale | Remediation (HIGH only) |
|------------|----------|-----------|------------------------|

Severity: HIGH (data loss / security breach) / MEDIUM (reliability / latency) /
LOW (observability / maintenance)

Rules:
- ALL findings -- HIGH, MEDIUM, and LOW -- require a one-line rationale. Rationale is
  not optional for any row, including LOW findings.
- Every HIGH finding requires a concrete, call-context-specific remediation. Acceptable
  forms:
  - Exact header: Idempotency-Key: {uuid-v4} on POST /[endpoint]
  - Exact backoff: initial: 1s / factor: 2 / max: 32s / jitter: +/-25%, max attempts: 5
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

---

## Predicted Scoring Under v4 Rubric (137 pt ceiling)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS (?) | PASS |
| C-14 | PASS | PASS | PASS | PASS (?) | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS (2 obligations) | PASS (4 obligations) | PASS (2 obligations) | PASS (3 obligations) | PASS (maximal) |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| **Predicted** | **137** | **137** | **137** | **137 (?)** | **137** |

**C-13/C-14 uncertainty on V-04:** The call blocks in Phase 2 contain per-section concern
exclusions (satisfying C-13's "within the section itself, not only in a preamble") and
per-block five-concern checklists gating the next call block (satisfying C-14). The open
question is whether the rubric treats "PHASE 2 -- PER-CALL ANALYSIS" as a phase-level
preamble for all call blocks within it, triggering the R3 failure mode. If the grading
treats call blocks as the structural unit regardless of outer frame, V-04 scores ceiling.
If the Phase label itself triggers the preamble interpretation, V-04 fails C-13/C-14.

**C-16 differentiation:** V-01 and V-03 use the minimum-viable form (two obligations).
V-04 uses three. V-02 and V-05 use four with detailed gap sensitivity. If C-16 is
binary pass/fail at the two-obligation threshold, all five score equally. If the rubric
grades richness within the pass band, V-02 and V-05 should score higher on C-16 semantics.

**V-02 supplementary registry:** The registry is labeled supplementary and explicitly
prohibited from being the authoritative source. Section D carries all three required
fields. The test is whether Stage 3 registry presence is neutral (no scoring effect) or
actively positive (bonus semantic organization for fan-out features).

---

## Open Questions for R5

1. **V-04 C-13/C-14 result:** Does Phase outer + call block inner score ceiling? Definitive
   answer to R3 open Q3. If yes, phase architecture is fully rehabilitated at the call
   block level. If no, "Phase" label is sufficient to trigger preamble interpretation.

2. **C-16 grading depth:** Do V-01/V-03 (two obligations) and V-05 (four obligations plus
   gap sensitivity) score the same on C-16, or does the rubric differentiate within the
   pass band? This determines whether minimum-viable personas can hold ceiling or whether
   enriched personas add structural value.

3. **V-02 supplementary registry neutrality:** Is Stage 3 supplementary registry scored
   neutrally (neither penalized nor rewarded)? If neutral, V-02 holds ceiling. If the
   registry's mere presence triggers a C-11 scan-elsewhere reading even though Section D
   has complete data, V-02 loses 2 points again.
