# flow-integration — R14 Variations (v14 rubric, 242 pt ceiling)

New criteria: C-37 (temporal stakes anchor in motivational framing, 5 pts) + C-38 (C-36
obligation-count-agnostic content scope, 5 pts).
R13 V-01 confirmed temporal stakes anchor ("before the feature ships") satisfies C-37.
R13 V-02 confirmed canonical four-concern framing satisfies C-36 with five-row extended
obligation set (C-38 codified). Canonical ceiling: 212 pts. Full non-standard ceiling: 242 pts.

**Canonical-terms ceiling:** 212 pts (C-27/C-30/C-31/C-34 require non-standard substitution;
these 20 pts are N/A when canonical terms are used). C-37 and C-38 are both achievable with
canonical terms; C-38 additionally requires C-35, which requires non-standard terms or
canonical extension.

**R14 open questions under test:**
- Q1: Does C-37 require a delivery-phase temporal anchor ("before the feature ships"), or does
  a consequence-form anchor without an explicit temporal marker ("undocumented calls become
  ship-blockers") satisfy C-37 equivalently? V-01 tested temporal form; consequence-only form
  not yet tested.
- Q2: Does C-37 require concern enumeration alongside the stakes anchor, or does a
  stakes-anchored purpose statement without naming specific verification concerns (auth, rate
  limits, retry, error propagation) satisfy C-37? V-01 combined concern enumeration with the
  temporal anchor; stakes anchor alone not yet tested.

**Axes selected:**
- Single-axis: C-37 consequence-form — WHY block has concern enumeration but replaces
  temporal anchor with consequence-form anchor (V-01 / Q1 probe)
- Single-axis: C-37 stakes-alone — WHY block has temporal anchor but no concern enumeration
  (V-02 / Q2 probe)
- Single-axis: Phrasing register — declarative throughout; WHY block retains full C-37
  temporal + concern form (V-03 / C-37 register neutrality probe)
- Combined: consequence-form + stakes-alone — WHY block has neither temporal anchor nor
  concern enumeration; purpose + consequence reference only (V-04 / lower bound probe)
- Combined: C-35 + C-37 consequence-form + C-38 — five-row non-standard obligation table,
  WHY block uses consequence-form anchor + canonical four-concern framing (V-05 / full ceiling
  run with Q1 probe)

**Score predictions:**
- V-01: 212/212 if consequence-form satisfies C-37; 207/212 (-5 C-37) if temporal marker
        required
- V-02: 212/212 if stakes anchor alone satisfies C-37; 207/212 (-5 C-37) if concern
        enumeration is a C-37 requirement alongside the anchor
- V-03: 212/212 — declarative register is structurally neutral; C-37 temporal anchor present
        in declarative form; confirms C-37 is not register-sensitive
- V-04: 207/212 (-5 C-37) most likely — no temporal anchor and no concern enumeration; only
        a purpose + consequence reference; tests whether the lowest WHY content still reaches
        C-37; 212/212 if C-37 is satisfied by any consequence framing regardless of form
- V-05: 242/242 if consequence-form satisfies C-37 (Q1 permissive + C-38 confirmed from R13);
        237/242 (-5 C-37) if temporal marker required; C-35, C-36, C-38 expected PASS

---

## V-01 — C-37 Consequence-Form (Q1 Probe)

**Axis**: C-37 content form — the WHY THIS TRACE DISCIPLINE EXISTS block includes concern
enumeration (authentication, rate limits, retry behavior, error propagation) but replaces the
temporal stakes anchor ("before the feature ships") with a consequence-form anchor that names
the stakes without a delivery-phase temporal marker ("undocumented calls become ship-blockers
at integration review"). All other structural elements are unchanged from the R13 canonical
baseline.

**Hypothesis**: C-37 is satisfied by any temporal or delivery-phase consequence-boundary
statement. If the rubric's requirement is stakes presence — the framing converts from
description to constraint by naming what happens when documentation is absent — then
consequence-form ("become ship-blockers") achieves the same conversion as temporal form
("before the feature ships"). Expected 212/212 if consequence-form satisfies C-37; 207/212
(-5 C-37) if the delivery-phase temporal marker is the required surface form.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and to verify
that each call's authentication, rate limits, retry behavior, and error propagation are fully
documented — undocumented integration calls become ship-blockers at integration review and
cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out
registry, call-category summary, cross-call rollup table), that structure is: (1) populated
FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT
required for trace assessment. Traces with no cross-stage structures satisfy this rule by
default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do
not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate
limits, retry/idempotency, and error propagation each have their own sections below)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate
limits, retry/idempotency, and error propagation each have their own sections)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format,
retry/idempotency, and error propagation each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication,
format, rate limits, and error propagation each have their own sections)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format,
rate limits, and retry/idempotency each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                 | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                          |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property                | Value                                         |
|-------------------------|-----------------------------------------------|
| Populated from          | Per-call blocks (Stage 2)                     |
| Authoritative source    | Per-call blocks — this structure is secondary |
| Required for assessment | No                                            |

---

## V-02 — C-37 Stakes-Alone (Q2 Probe)

**Axis**: C-37 concern enumeration — the WHY THIS TRACE DISCIPLINE EXISTS block includes the
temporal stakes anchor ("before the feature ships") but removes all concern enumeration (no
mention of authentication, rate limits, retry behavior, or error propagation). The framing
names trace purpose and delivery-phase stakes, but does not enumerate the specific verification
concerns that constitute documentation completeness. All other structural elements are
unchanged.

**Hypothesis**: C-37 is satisfied by the presence of a temporal or delivery-phase stakes anchor
regardless of whether the framing also enumerates specific concerns. The stakes anchor converts
description to constraint; concern enumeration is not a C-37 requirement — it is present in
the R13 V-01 pass boundary but was not tested in isolation. Expected 212/212 if stakes anchor
alone satisfies C-37; 207/212 (-5 C-37) if concern enumeration is a required companion element.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and to verify that
all documentation gaps are resolved before the feature ships.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out
registry, call-category summary, cross-call rollup table), that structure is: (1) populated
FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT
required for trace assessment. Traces with no cross-stage structures satisfy this rule by
default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do
not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate
limits, retry/idempotency, and error propagation each have their own sections below)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate
limits, retry/idempotency, and error propagation each have their own sections)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format,
retry/idempotency, and error propagation each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication,
format, rate limits, and error propagation each have their own sections)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format,
rate limits, and retry/idempotency each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                 | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                          |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property                | Value                                         |
|-------------------------|-----------------------------------------------|
| Populated from          | Per-call blocks (Stage 2)                     |
| Authoritative source    | Per-call blocks — this structure is secondary |
| Required for assessment | No                                            |

---

## V-03 — Phrasing Register: Declarative (C-37 Register Neutrality Probe)

**Axis**: Phrasing register — all imperative instructions are rephrased as declarative or
descriptive constructions throughout the prompt body. The WHY block retains the full C-37
temporal + concern form ("before the feature ships" + concern enumeration) to confirm that
C-37's temporal anchor is not register-sensitive. Gate commands become completion conditions
stated as declarations. Section exclusions are described rather than prohibited. No schema
elements, obligation terms, ARE directives, table structures, or checklist items are removed
or changed — only the grammatical register of the surrounding prose.

**Hypothesis**: Phrasing register is structurally neutral for C-37. The temporal stakes anchor
satisfies C-37 whether phrased as an imperative ("verify...before the feature ships") or a
declarative ("documentation gaps are identified before the feature ships"). C-10, C-12, C-15,
and C-20 each require explicit completion conditions — none require the imperative mood.
Expected 212/212, confirming register is a free variation axis for C-37.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes. Each call's
authentication, rate limits, retry behavior, and error propagation are documented before the
feature ships — documentation gaps identified at that boundary are integration-review blockers,
not post-ship discoveries.

---

A cross-system integration trace is produced for the feature described in the signal by a
connectors and backend integration domain expert.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

All four discovery obligations are applied while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

The inventory table is fully populated before Stage 2 analysis begins.

**INVENTORY GATE: Stage 2 analysis begins only when every discovered call has a row with
Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N;
blank is not acceptable).**

NEW-CALL RULE: Any call discovered during Stage 2 analysis that is not already in this table
receives a row — with all four flag cells set — before its analysis block opens.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: Any cross-stage aggregation structure produced in this stage (fan-out
registry, call-category summary, cross-call rollup table) is: (1) populated FROM the per-call
blocks — not the authoritative source for any data it contains; (2) not required for trace
assessment. Traces with no cross-stage structures satisfy this rule by default.

Each CALL-[N] in the Stage 1 inventory table is analyzed in order. CALL-[N+1] opens only
after the CALL-[N] COMPLETION GATE confirms all five concerns are documented.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(authentication only — the other four concerns each occupy a
dedicated section in this call block)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(format only — the other four concerns each occupy a
dedicated section in this call block)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(rate limits only — the other four concerns each occupy a dedicated
section in this call block)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(retry and idempotency only — the other four concerns each
occupy a dedicated section in this call block)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(error propagation only — the other four concerns each occupy a
dedicated section in this call block)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**CALL-[N] COMPLETION GATE** — CALL-[N+1] opens only after all five rows are confirmed:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

Every gap identified across all call blocks is listed here. Each finding carries a severity
label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings carry
a call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                 | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                          |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda is present regardless of Stage 2 output. When Stage 2 produces no cross-stage
aggregation structures, the entry reads: "No cross-stage structures produced in this trace."
It occupies no position between numbered stages; no existing element is displaced or
renumbered.

For any cross-stage structure produced in Stage 2:

| Property                | Value                                         |
|-------------------------|-----------------------------------------------|
| Populated from          | Per-call blocks (Stage 2)                     |
| Authoritative source    | Per-call blocks — this structure is secondary |
| Required for assessment | No                                            |

---

## V-04 — Combined: Consequence-Form + Stakes-Alone (Lower Bound Probe)

**Axis**: Both Q1 and Q2 simultaneously stripped — the WHY block has no temporal marker AND
no concern enumeration. The block contains only purpose + consequence reference: integration
traces exist to surface cross-system calls that can block a release. This is the minimal WHY
content that could conceivably satisfy C-37 — it names the trace purpose and implies stakes
(ship-blocking) but specifies neither the temporal phase nor the specific concerns at risk.
All other structural elements are unchanged from the R13 canonical baseline.

**Hypothesis**: This variation isolates the lower bound of C-37 content. If C-37 requires
either a temporal marker or concern enumeration (or both), this variation fails C-37 and scores
207/212. If C-37 is satisfied by any consequence reference — even implicit ship-blocking
language without temporal form or concern enumeration — this variation scores 212/212. The
most likely outcome is 207/212, as neither the temporal anchor nor concern enumeration is
present to convert the framing from description to constraint. The adjudication result
resolves whether C-37 is a presence-of-stakes criterion or a form-of-stakes criterion.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface the cross-system calls that can block a release — the
ones not in the specification, the ones assumed to work, the ones with unknown owners, and
the ones delegating credentials through chains the feature team has not mapped.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out
registry, call-category summary, cross-call rollup table), that structure is: (1) populated
FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT
required for trace assessment. Traces with no cross-stage structures satisfy this rule by
default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do
not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate
limits, retry/idempotency, and error propagation each have their own sections below)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate
limits, retry/idempotency, and error propagation each have their own sections)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format,
retry/idempotency, and error propagation each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication,
format, rate limits, and error propagation each have their own sections)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format,
rate limits, and retry/idempotency each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                 | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                          |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property                | Value                                         |
|-------------------------|-----------------------------------------------|
| Populated from          | Per-call blocks (Stage 2)                     |
| Authoritative source    | Per-call blocks — this structure is secondary |
| Required for assessment | No                                            |

---

## V-05 — Combined: C-35 + C-37 Consequence-Form + C-38 (Full Ceiling Run / Q1 Probe)

**Axis**: Extended obligation set (C-35 in play: five rows, three non-standard substitutions,
one canonical kept, one new-without-canonical-equivalent) paired with a consequence-form
C-37 anchor (no temporal marker) and canonical four-concern framing in the WHY block (C-38
count-agnostic framing confirmed in R13 V-02). This is the full-ceiling probe: tests whether
C-37 consequence-form achieves 242 pts alongside C-35 + C-38 in a non-standard configuration.

**Hypothesis**: C-35 PASS expected (five-row extended table pattern confirmed in R13 V-02).
C-38 PASS expected (canonical four-concern framing satisfies C-36 regardless of extended
obligation set — confirmed R13 V-02). C-37 is the open question: if consequence-form satisfies
Q1, this variation scores 242/242. If temporal marker is required for C-37, scores 237/242
(-5 C-37). C-36 PASS expected regardless (any purpose statement satisfies C-36 — confirmed
R13 V-01 adjudication). C-27/C-30/C-31/C-34 in play for the three substituted canonical
tokens.

Non-standard terms: expose-call (sub for forgotten-call) / silent-entry (sub for
assumed-to-work) / shadow-system (sub for unknown-system) / delegation-chain (CANONICAL,
kept) / burst-start (NEW — first-request behavior when connection reuse or pre-warm state is
unknown; no canonical equivalent).
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."
YOU MUST NOT block: enumerates forgotten-call + assumed-to-work + unknown-system (three
substituted canonical tokens); omits delegation-chain (canonical, not substituted) and
burst-start (new, no canonical equivalent to prohibit).
WHY block: consequence-form anchor + canonical four-concern framing — no temporal marker,
no burst-start mention.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and to verify
that each call's authentication, rate limits, retry behavior, and error propagation are fully
documented — calls without documentation become ship-blockers at integration review and
cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term | What to discover                                                                                                                                              |
|-------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | expose-call     | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry posts |
| OBL-2 | silent-entry    | Calls the specification names but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment             |
| OBL-3 | shadow-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                                          |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation                          |
| OBL-5 | burst-start     | Calls where connection reuse or pre-warm state is unknown at trace time — first-invocation behavior may differ materially from steady-state behavior          |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

YOU MUST NOT use forgotten-call, assumed-to-work, or unknown-system as column headers or
obligation names in this trace.

Apply all five discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all five flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all five flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [expose-call] | [silent-entry] | [shadow-system] | [delegation-chain] | [burst-start] |
|---------|---------------|-----------|------------------|---------------|----------------|-----------------|--------------------|---------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N         | Y / N          | Y / N           | Y / N              | Y / N         |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N         | Y / N          | Y / N           | Y / N              | Y / N         |
| ...     |               |           |                  |               |                |                 |                    |               |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out
registry, call-category summary, cross-call rollup table), that structure is: (1) populated
FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT
required for trace assessment. Traces with no cross-stage structures satisfy this rule by
default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do
not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate
limits, retry/idempotency, and error propagation each have their own sections below)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate
limits, retry/idempotency, and error propagation each have their own sections)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format,
retry/idempotency, and error propagation each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication,
format, rate limits, and error propagation each have their own sections)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format,
rate limits, and retry/idempotency each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                              | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / shadow-system / delegation-chain / burst-start | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                                       |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property                | Value                                         |
|-------------------------|-----------------------------------------------|
| Populated from          | Per-call blocks (Stage 2)                     |
| Authoritative source    | Per-call blocks — this structure is secondary |
| Required for assessment | No                                            |
