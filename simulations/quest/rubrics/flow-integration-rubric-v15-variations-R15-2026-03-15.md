# flow-integration — R15 Variations (v15 rubric, 247 pt ceiling)

New criterion: C-39 (C-37 consequence-form delivery-phase equivalence, 5 pts).
R14 V-01 confirmed consequence-form + delivery-phase marker + declarative unconditional
satisfies C-37. C-39 codifies this equivalence. Canonical ceiling: 212 pts.
Full non-standard ceiling: 247 pts.

**Canonical-terms ceiling:** 212 pts (C-27/C-30/C-31/C-34 require non-standard substitution;
these 20 pts are N/A when canonical terms are used). C-37, C-38, C-39 are achievable with
canonical terms; C-38 additionally requires C-35, which requires extension beyond four rows.

**R15 open questions under test:**
- Q1: Does C-37 require concern enumeration alongside the stakes anchor, or does a stakes
  anchor alone (no mention of authentication, rate limits, retry behavior, error propagation)
  satisfy C-37? Both confirmed C-37 PASS variations (V-01 R13, V-01 R14) included concern
  enumeration; stakes anchor alone not yet tested.
- Q1 form split: V-01 probes Q1 on consequence-form surface (new for R15); V-02 probes Q1
  on temporal form surface (companion — isolates whether concern enumeration requirement
  is form-independent).

**Axes selected:**
- Single-axis: C-37 stakes-only / consequence-form — WHY block has consequence-form anchor
  but no concern enumeration (V-01 / Q1 probe, consequence-form surface)
- Single-axis: C-37 stakes-only / temporal form — WHY block has temporal anchor but no
  concern enumeration (V-02 / Q1 probe, temporal surface)
- Single-axis: Phrasing register (conversational/imperative) — WHY block uses consequence-
  form + full concern enumeration in conversational register (V-03 / C-39 register neutrality)
- Combined: Inertia framing + stakes-only / consequence-form — WHY block foregrounds
  discovery-failure inertia, lands on consequence-form anchor, no verification-concern
  enumeration (V-04 / Q1 lower bound probe with richer framing context)
- Combined: C-35 + C-37 consequence-form concern-enumerated + C-38 + C-39 confirmation —
  five-row non-standard obligation table, consequence-form WHY anchor (V-05 / full 247 ceiling)

**Score predictions:**
- V-01: 212/212 if stakes anchor alone satisfies C-37 (Q1 permissive); 207/212 (-5 C-37)
        if concern enumeration is required alongside the stakes anchor
- V-02: 212/212 if stakes anchor alone satisfies C-37; 207/212 (-5 C-37) if required.
        Companion to V-01 — if both PASS, Q1 is permissive; if both FAIL, concern
        enumeration is required regardless of anchor form surface
- V-03: 212/212 — consequence-form + concern enumeration; confirms C-39 is register-neutral;
        conversational register is structurally neutral for all criteria
- V-04: 207/212 (-5 C-37) most likely — inertia framing names discovery-failure categories,
        not verification concerns; tests whether inertia context compensates for absent
        concern enumeration; 212/212 if any stakes anchor satisfies C-37 regardless of
        surrounding content
- V-05: 247/247 — full non-standard ceiling; C-39 confirmed at ceiling alongside C-35/C-38

---

## V-01 — C-37 Stakes-Only / Consequence-Form (Q1 Probe, Consequence-Form Surface)

**Axis**: C-37 content form — the WHY THIS TRACE DISCIPLINE EXISTS block includes the
consequence-form delivery-phase anchor ("become ship-blockers at integration review") but
carries NO concern enumeration: no mention of authentication, rate limits, retry behavior,
or error propagation. The purpose statement names the trace goal and lands immediately on
the consequence anchor. All other structural elements are unchanged from the canonical
baseline.

**Hypothesis**: C-37 is satisfied by the stakes anchor alone — the anchor converts the
framing from description to constraint regardless of whether specific verification concerns
are named alongside it. The operative C-37 element is the delivery-phase constraint boundary,
not the enumeration of what gets verified. Expected 212/212 if stakes anchor alone satisfies
C-37; 207/212 (-5 C-37) if concern enumeration is a required companion element.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes — undocumented
integration calls become ship-blockers at integration review and cannot be cleared without
a completed trace.

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

## V-02 — C-37 Stakes-Only / Temporal Form (Q1 Probe, Temporal Surface)

**Axis**: C-37 content form — the WHY THIS TRACE DISCIPLINE EXISTS block includes the
temporal stakes anchor ("before the feature ships") but carries NO concern enumeration: no
mention of authentication, rate limits, retry behavior, or error propagation. The purpose
statement names the trace goal and lands immediately on the temporal anchor. All other
structural elements are unchanged from the canonical baseline.

**Hypothesis**: C-37 is satisfied by the temporal stakes anchor alone. If Q1 is permissive
regardless of anchor form, both V-01 (consequence-form) and V-02 (temporal form) should PASS.
If V-01 and V-02 both FAIL, concern enumeration is required alongside the anchor regardless of
which anchor form is used. If one passes and the other fails, the form surface is a variable —
but current rubric (C-37 updated, C-39 codified) makes both forms structurally equivalent,
so if one fails both should fail for the same reason. Expected 212/212 if stakes anchor alone
satisfies; 207/212 (-5 C-37) if concern enumeration is required.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and verify that
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

## V-03 — Phrasing Register: Conversational/Imperative (C-39 Register Neutrality Probe)

**Axis**: Phrasing register — the prompt body shifts to a direct second-person imperative
register throughout: gate commands are issued as imperatives ("Run this trace to..."),
stage instructions are addressed to "you," and section-exclusion parentheticals stay but
are compressed into the same imperative voice. The WHY block uses the consequence-form
anchor with full concern enumeration (C-39 confirmed form) to test whether C-37 and C-39
are satisfied by consequence-form in conversational register, not just formal declarative.
No schema elements, obligation terms, ARE directives, table structures, or checklist items
are removed — only the grammatical register of surrounding prose shifts.

**Hypothesis**: Phrasing register is structurally neutral for C-37 and C-39. The consequence-
form delivery-phase anchor satisfies C-37 regardless of whether the surrounding prose uses
formal declarative or conversational imperative constructions. C-10, C-12, C-15, C-20 each
require explicit completion conditions — none require the declarative mood. Expected 212/212,
confirming register is a free variation axis for C-39 as it was confirmed for C-37 in R14 V-03.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Run this trace to find every cross-system call this feature makes — document each call's
authentication, rate limits, retry behavior, and error propagation before it reaches
integration review; undocumented calls become ship-blockers at integration review and cannot
be cleared without a completed trace.

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

Build this inventory before you open Stage 2. Do not proceed past this table until it is
complete.

**INVENTORY GATE: Open Stage 2 only after every discovered call has a row with Call ID,
Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N;
blank is not acceptable).**

NEW-CALL RULE: If you discover a call during Stage 2 that is not already in this table,
add its row — with all four flag cells set — before opening its analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If you produce any cross-stage aggregation structure in this stage (fan-out
registry, call-category summary, cross-call rollup table), treat it as: (1) populated FROM
the per-call blocks — not the authoritative source for any data it contains; (2) NOT required
for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

Work through each CALL-[N] in the Stage 1 inventory table in order. Do not open CALL-[N+1]
until you have fully checked the CALL-[N] COMPLETION GATE.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(authentication only — document format, rate limits,
retry/idempotency, and error propagation in their own sections below)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(format only — authentication, rate limits,
retry/idempotency, and error propagation each have their own sections)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(rate limits only — authentication, format, retry/idempotency,
and error propagation each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(retry and idempotency only — authentication, format,
rate limits, and error propagation each have their own sections)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(error propagation only — authentication, format, rate limits,
and retry/idempotency each have their own sections)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**CALL-[N] COMPLETION GATE** — Check all five before opening CALL-[N+1]:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

List every gap you found across all call blocks. Every finding carries a severity label and
a one-line rationale — MEDIUM and LOW findings are not exempt. Write a call-specific
remediation sketch for every HIGH finding; generic advice does not satisfy.

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

## V-04 — Combined: Inertia Framing + Stakes-Only / Consequence-Form (Q1 Lower Bound Probe)

**Axes**: (1) Inertia framing — the WHY block leads with a description of what goes wrong
when the trace is skipped (discovery-failure inertia: calls assumed to work, SDK calls never
traced, delegation chains unmapped) before landing on the consequence anchor; (2) Stakes-only
— no verification-concern enumeration (no mention of authentication, rate limits, retry
behavior, or error propagation as a named verification list). The inertia passage names
discovery-failure categories, not concern categories — testing whether inertia context that
foregrounds the WHY-traces-miss-calls dimension (without naming what each call must be checked
against) achieves C-37 alongside the consequence-form anchor.

**Hypothesis**: 207/212 (-5 C-37) most likely. The inertia framing names discovery risk
(obligation-scope framing) rather than verification-concern risk (auth/rate-limit/retry/error
framing). If C-37 requires naming specific verification concerns, this WHY block fails C-37
for the same reason as V-01. If any consequence-form stakes anchor satisfies C-37 regardless
of surrounding content, 212/212. V-04 is the most inertia-rich stakes-only form — if this
fails C-37 despite rich inertia context, the concern-enumeration requirement is confirmed
robustly.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Features arrive at integration review with more undocumented cross-system calls than their
specifications name — calls assumed to work without verification, implicit SDK calls that
nobody traced, delegation chains that never appeared in any design document, connection
behaviors that were copy-pasted from a previous feature and never re-examined. Teams discover
these gaps at the worst possible time: under deadline pressure, after the review gate is
already blocking. This trace exists to surface all of them before that moment: undocumented
integration calls become ship-blockers at integration review and cannot be cleared without a
completed trace.

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

## V-05 — Combined: C-35 + C-37 Consequence-Form + C-38 + C-39 Confirmation (Full 247 Ceiling)

**Axes**: Extended obligation set (C-35: five rows, three non-standard substitutions, one
canonical kept, one new-without-canonical-equivalent) paired with the consequence-form C-37
anchor with full concern enumeration (C-39 confirmed form from R14 V-01). This is the full
247-ceiling confirmation run: tests whether C-39 contributes its 5 pts at ceiling alongside
C-35 and C-38 in a non-standard configuration where all four non-standard sub-criteria
(C-27/C-30/C-31/C-34) are also in play.

**Hypothesis**: C-39 PASS — consequence-form + delivery-phase marker + concern enumeration +
declarative unconditional form is the confirmed C-37 pass boundary from R14 V-01. C-35 PASS
expected (five-row extended table pattern confirmed R13 V-02). C-38 PASS expected (canonical
four-concern framing satisfies C-36 regardless of extended obligation set — confirmed R13
V-02). C-27/C-30/C-31/C-34 PASS expected with YOU MUST NOT block naming all three substituted
canonical tokens. Expected 247/247 — first full ceiling confirmation for the v15 rubric.

Non-standard terms: expose-call (sub for forgotten-call) / silent-entry (sub for
assumed-to-work) / shadow-system (sub for unknown-system) / delegation-chain (CANONICAL,
kept) / burst-start (NEW — first-request behavior when connection reuse or pre-warm state is
unknown; no canonical equivalent).
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."
YOU MUST NOT block: enumerates forgotten-call + assumed-to-work + unknown-system (three
substituted canonical tokens; delegation-chain is canonical and kept; burst-start is new with
no canonical equivalent to prohibit).
WHY block: consequence-form anchor + canonical four-concern framing (authentication, rate
limits, retry behavior, error propagation) — no temporal marker; no burst-start mention.

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

| OBL   | Obligation Term  | What to discover                                                                                                                                              |
|-------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | expose-call      | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry posts |
| OBL-2 | silent-entry     | Calls the specification names but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment             |
| OBL-3 | shadow-system    | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                                          |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation                           |
| OBL-5 | burst-start      | Calls where connection reuse or pre-warm state is unknown at trace time — first-invocation behavior may differ materially from steady-state behavior          |

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
