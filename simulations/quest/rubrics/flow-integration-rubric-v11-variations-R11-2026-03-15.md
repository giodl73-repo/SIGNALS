# flow-integration — R11 Variations (v11 rubric, 212 pt ceiling)

New criteria: C-31 (C-30 explicit inline token enumeration, 5 pts) + C-32 (C-29 uppercase ARE
assertive form, 5 pts).
All R10 top variations scored 202/202. R11 target: 212/212.

R11 open questions under test:
- Q1: Does C-32 require the multi-subject ARE form ("the flag column headers ARE the Obligation
  Term column values above"), or does a per-item IS form satisfy the directive? For example:
  "Each flag column header IS one of the Obligation Term values from the obligation table." All
  confirmed PASS variations used ARE in a multi-subject sentence; IS in a per-item assertive
  sentence has not been tested.
- Q2: Does C-31 require the YOU MUST NOT block to enumerate every substituted canonical token
  by name, or is partial inline enumeration (naming three of four non-standard terms, for
  example) sufficient? R8 V-05 used full enumeration (PASS); partial enumeration is untested.

Axes selected:
- Single-axis: C-32 assertive form — per-item IS form (V-01 / Q1 probe)
- Single-axis: C-31 enumeration completeness — partial inline enumeration 3-of-4 (V-02 / Q2 probe)
- Single-axis: Lifecycle emphasis — expanded stage rationale blocks (V-03 / structural neutrality probe)
- Combined: C-32 IS form + C-31 partial enumeration (V-04 / Q1+Q2 joint probe)
- Combined: Phrasing register shift + confirming clean sweep (V-05 / register neutrality confirming)

Score predictions:
- V-01: 212/212 if IS form satisfies C-32 (and C-29 interpreted as any uppercase assertive identity
        verb); 202/212 (−5 C-29, −5 C-32) if only multi-subject ARE satisfies
- V-02: 212/212 if partial enumeration (3-of-4) satisfies C-31;
        202/212 (−5 C-27, −5 C-31) if full enumeration required (C-27 also fails — prohibition
        surface is incomplete for the omitted token)
- V-03: 212/212 — lifecycle rationale additions are structurally neutral
- V-04: 212/212 if both Q1 and Q2 resolve positively;
        202/212 (−5 C-29, −5 C-32) if only Q1 fails;
        202/212 (−5 C-27, −5 C-31) if only Q2 fails;
        192/212 (−5 C-27, −5 C-29, −5 C-31, −5 C-32) if both fail
- V-05: 212/212 — register variation is structurally neutral; clean sweep confirmation after
        R10 V-03 established inertia framing neutrality

---

## V-01 — C-32 Per-Item IS Form (Q1 Probe)

**Axis**: C-32 assertive form variants — per-item IS assertive sentence instead of multi-subject
ARE assertive sentence in the schema alignment instruction.

**Hypothesis**: A schema instruction of the form "Each flag column header in the Stage 1 inventory
table IS one of the Obligation Term values from the obligation table above — use those exact tokens
as column headers" satisfies C-32 because IS in a per-item assertive sentence is an uppercase
assertive identity verb equivalent to ARE in a multi-subject sentence. If C-32 (and C-29) permit
any uppercase assertive identity verb, this scores 212/212. If C-32 requires specifically the
multi-subject ARE form, this scores 202/212 (−5 C-29, −5 C-32). C-26 is expected to survive in
either case — IS provides schema-only enforcement; only the specific verb form is under test.

Canonical obligation terms used (C-27 N/A — no non-standard substitution).
C-30/C-31 N/A — no YOU MUST NOT block required without non-standard terms.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

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

Each flag column header in the Stage 1 inventory table IS one of the Obligation Term values from
the obligation table above — use those exact tokens as column headers. A column header that does
not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing
this table to the Stage 1 inventory column headers without reading prose.

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

## V-02 — C-31 Partial Inline Enumeration (Q2 Probe)

**Axis**: C-31 enumeration completeness — a single YOU MUST NOT block that enumerates three of
four substituted canonical tokens inline, omitting the fourth.

**Hypothesis**: A YOU MUST NOT block that explicitly names three non-standard substitution terms
inline — "YOU MUST NOT use footprint-call, implicit-pass, or ghost-system as column headers or
obligation names in this trace" — satisfies C-31 despite omitting the fourth term (relay-chain).
If partial enumeration satisfies C-31, this scores 212/212. If C-31 requires all substituted
canonical tokens to be named explicitly, this scores 202/212 (−5 C-27, −5 C-31) because the
prohibition surface does not cover relay-chain and C-27's self-contained coverage requirement is
not met either.

Non-standard obligation terms: footprint-call / implicit-pass / ghost-system / relay-chain.
C-29 form: explicit uppercase ARE (confirmed pass — not the axis under test here).
YOU MUST NOT block: single block, names footprint-call + implicit-pass + ghost-system, omits relay-chain.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term | What to discover                                                                                                                              |
|-------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | footprint-call  | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry |
| OBL-2 | implicit-pass   | Calls the specification lists but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit entry       |
| OBL-3 | ghost-system    | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                           |
| OBL-4 | relay-chain     | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation            |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

YOU MUST NOT use footprint-call, implicit-pass, or ghost-system as column headers or obligation
names in this trace.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [footprint-call] | [implicit-pass] | [ghost-system] | [relay-chain] |
|---------|---------------|-----------|------------------|------------------|-----------------|----------------|---------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N           | Y / N          | Y / N         |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N           | Y / N          | Y / N         |
| ...     |               |           |                  |                  |                 |                |               |

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

| Gap ID | Call ID | Gap Type                                                                              | Severity         | Rationale | Remediation |
|--------|---------|---------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / ghost-system / relay-chain    | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                       |                  |           |             |

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

## V-03 — Lifecycle Emphasis Expansion (Structural Neutrality Probe)

**Axis**: Lifecycle emphasis — each stage opens with an explicit rationale paragraph explaining
what the stage is for, what it is not for, and why the gate or constraint exists. The structural
content is identical to the confirmed-pass R10 V-03 baseline; only the surrounding lifecycle
commentary is expanded.

**Hypothesis**: Adding explicit lifecycle rationale blocks before each stage gate — naming the
purpose of the stage, the failure mode it guards against, and the structural guarantee the gate
provides — is structurally neutral. These additions are prose-only; they add no schema
instructions, no obligation terms, and no format directives. Expected score: 212/212. Confirms
that lifecycle emphasis variation (how much space is devoted to explaining stage boundaries and
gate logic) does not create criterion exposure or satisfy any criterion it was not previously
satisfying.

Canonical obligation terms (C-27 N/A). Uppercase ARE (C-29/C-32 confirmed pass).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

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

Stage 1 exists because a trace that begins with per-call analysis is a product summary, not an
integration trace. The specification names the calls the author thought of; Stage 1 names the
calls the system will actually make. These are different lists. The inventory gate enforces the
separation: per-call analysis in Stage 2 cannot begin until the complete call surface is known.
A model that skips Stage 1 and opens call blocks directly is tracing what the spec says, not
what the system does.

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable). The gate is structural, not advisory — do
not open Stage 2 with an incomplete table.**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block. Late call discovery does
not invalidate the prior inventory; it extends it.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

Stage 2 exists because cross-system integration fails at the call level, not the feature level.
Authentication gaps are per-call. Rate limit exposure is per-call. Retry and idempotency risk is
per-call. Error propagation paths diverge per-call. The concern-isolation architecture of this
stage — each section handles exactly one concern and explicitly excludes all others — exists
because a merged section allows a model to satisfy authentication documentation by mentioning
auth inside a format block or rate limit in an error block. The five-section structure with
per-section exclusion declarations prevents this; each concern has exactly one place where it
must be found, and its absence in that place is structurally visible.

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

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked. The
gate is sequential and structural: a call block that is 80% complete is an incomplete call
block. Each concern must be documented before the next call opens, not retroactively after
all calls are processed.

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

Stage 3 exists because a trace that does not name gaps is a description, not an analysis.
Every entry in Stage 1 is a candidate for a gap entry in Stage 3; the absence of a gap
finding for a call is itself an implicit finding that all concerns are fully resolved. MEDIUM
and LOW severity findings carry rationale because severity without rationale is an
assertion, not a judgment. HIGH findings carry a remediation sketch because a gap without a
direction of resolution is an open risk, not a closed one.

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

## V-04 — Combined: C-32 IS Form + C-31 Partial Enumeration (Q1+Q2 Joint Probe)

**Axis**: Combined — per-item IS assertive form (C-32 Q1 probe) plus partial inline enumeration
of 3-of-4 non-standard tokens (C-31 Q2 probe).

**Hypothesis**: Both open questions resolve positively: (1) the IS form in a per-item assertive
sentence satisfies C-32 and C-29; (2) partial inline enumeration of three of four non-standard
tokens satisfies C-31. If both pass: 212/212. If only the IS form fails: 202/212 (−5 C-29,
−5 C-32). If only partial enumeration fails: 202/212 (−5 C-27, −5 C-31). If both fail:
192/212 (−5 C-27, −5 C-29, −5 C-31, −5 C-32).

Non-standard obligation terms: footprint-call / implicit-pass / ghost-system / relay-chain.
Schema instruction: IS per-item form (Q1 axis).
YOU MUST NOT block: single block, inline enumeration of footprint-call + implicit-pass +
ghost-system (omits relay-chain) (Q2 axis).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term | What to discover                                                                                                                              |
|-------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | footprint-call  | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry |
| OBL-2 | implicit-pass   | Calls the specification lists but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit entry       |
| OBL-3 | ghost-system    | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                           |
| OBL-4 | relay-chain     | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation            |

Each flag column header in the Stage 1 inventory table IS one of the Obligation Term values from
the obligation table above — use those exact tokens as column headers. A column header that does
not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing
this table to the Stage 1 inventory column headers without reading prose.

YOU MUST NOT use footprint-call, implicit-pass, or ghost-system as column headers or obligation
names in this trace.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [footprint-call] | [implicit-pass] | [ghost-system] | [relay-chain] |
|---------|---------------|-----------|------------------|------------------|-----------------|----------------|---------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N           | Y / N          | Y / N         |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N           | Y / N          | Y / N         |
| ...     |               |           |                  |                  |                 |                |               |

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

| Gap ID | Call ID | Gap Type                                                                              | Severity         | Rationale | Remediation |
|--------|---------|---------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / ghost-system / relay-chain    | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                       |                  |           |             |

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

## V-05 — Phrasing Register Shift (Confirming, Clean Sweep)

**Axis**: Phrasing register — imperative/action-oriented register throughout, replacing
descriptive preamble language with direct directives. "Discovery obligation table" becomes
"Your four discovery commitments." "Populate this table before opening Stage 2" becomes
"Build this inventory now." Stage headers use action verbs. The structural architecture is
identical to the confirmed-pass R10 V-03 baseline; only the register changes.

**Hypothesis**: Register variation — shifting from descriptive-formal to imperative-directive
tone in stage preambles, gate instructions, and persona framing — is structurally neutral. No
criterion is phrasing-sensitive at the schema or schema-instruction level; all criteria target
structural presence (section exists, table row present, instruction uses uppercase ARE, etc.).
Expected score: 212/212. Confirms that phrasing register is a free variation axis and rules
out tone-driven criterion exposure as a confound in future variations.

Canonical obligation terms (C-27 N/A). Uppercase ARE (C-29/C-32 confirmed pass).
No non-standard substitution (C-31 N/A).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**YOUR ROLE**

You are the connectors and backend integration expert on this trace. Your job is to find the
calls the specification did not name, challenge every assumption of smooth operation, surface
every system whose identity cannot be confirmed, and map every delegation chain that moves
credentials through the stack. Do not summarize the specification. Trace the integration.

**YOUR FOUR DISCOVERY COMMITMENTS**

Make these four commitments before building the call inventory. Each commitment IS a row in
the table below — a missing row is a broken commitment:

| OBL   | Obligation Term  | What you commit to find                                                                                                             |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

Apply all four discovery commitments while building Stage 1.

---

**STAGE 1 — BUILD THE CALL INVENTORY**

Build this inventory now. Do not open Stage 2 until every discovered call has a row.

**INVENTORY GATE: Open Stage 2 only when every call has a row with Call ID, Target System,
Call Type, Confidence, and all four flag cells explicitly set (Y or N — blank fails the
gate).**

NEW-CALL RULE: When Stage 2 surfaces a call not yet in this table, add the row with all four
flags set before opening that call's block. Stop. Add the row. Then continue.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — TRACE EVERY CALL**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out
registry, call-category summary, cross-call rollup table), that structure is: (1) populated
FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT
required for trace assessment. Traces with no cross-stage structures satisfy this rule by
default.

Work through each CALL-[N] from Stage 1 in order. Do not open CALL-[N+1] until the
CALL-[N] COMPLETION GATE is fully checked.

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

**CALL-[N] COMPLETION GATE** — Check all five before opening CALL-[N+1]:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — NAME EVERY GAP**

Name every gap found across all call blocks. Every finding carries a severity label and a
one-line rationale — MEDIUM and LOW are not exempt from rationale. HIGH findings require a
call-specific remediation sketch; point to the fix, not the category.

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
