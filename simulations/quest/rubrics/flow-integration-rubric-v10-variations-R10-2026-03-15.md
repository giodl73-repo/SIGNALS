# flow-integration — R10 Variations (v10 rubric, 202 pt ceiling)

New criteria: C-29 (C-26 explicit ARE directive requirement, 5 pts) + C-30 (C-27 single-block
comprehensive prohibition, 5 pts).
All R9 top variations scored 192/192. R10 target: 202/202.

R10 open questions under test:
- Q1: Does C-30 require the YOU MUST NOT block to enumerate each forbidden canonical token
  explicitly by name, or does a table-reference shorthand — "YOU MUST NOT use any of the
  canonical Obligation Term values listed in the table above" — satisfy C-27/C-30 via indirect
  reference? R8 V-05 used explicit named tokens (PASS); table-reference shorthand is untested.
- Q2: Does C-29 require the uppercase ARE keyword in an assertive declarative sentence, or does
  lowercase "are" embedded in a non-assertive construction satisfy the directive form? All
  confirmed PASS variations used uppercase ARE; lowercase minimum is untested.

Axes selected:
- Single-axis: C-30 block composition — table-reference shorthand (V-01 / Q1 probe)
- Single-axis: C-29 ARE form — lowercase non-assertive (V-02 / Q2 probe)
- Single-axis: Inertia framing — spec-as-incomplete status-quo block (V-03 / structural neutrality probe)
- Combined: C-29 lowercase + C-30 table-reference + non-standard terms (V-04 / Q1+Q2 joint probe)
- Combined: Section outer frame + confirming (V-05 / C-28 Section formula clean sweep)

Score predictions:
- V-01: 202/202 if table-reference satisfies C-27/C-30 (indirect enumeration sufficient);
        192/202 (−5 C-27, −5 C-30) if explicit token enumeration required
- V-02: 202/202 if lowercase non-assertive satisfies C-29; 197/202 (−5 C-29) if uppercase required
- V-03: 202/202 — inertia framing block is structurally neutral; adds no criterion exposure
- V-04: 202/202 if both Q1 and Q2 resolve positively;
        197/202 (−5 C-29) if only Q2 fails;
        192/202 (−5 C-27, −5 C-30) if only Q1 fails;
        187/202 (−5 C-27, −5 C-29, −5 C-30) if both fail
- V-05: 202/202 — known-good Section frame with explicit ARE and no non-standard terms;
        confirms C-28 Section formula and C-26/C-29 clean sweep after R9 V-04 contaminated this frame

---

## V-01 — C-30 Table-Reference Shorthand (Q1 Probe)

**Axis**: C-30 block composition — single YOU MUST NOT block that references the obligation
table by role without enumerating individual canonical token names.

**Hypothesis**: A single YOU MUST NOT block that reads "YOU MUST NOT use any of the
canonical Obligation Term values listed in the obligation table above as column headers or
obligation names in this trace" — placed as a unified block after the schema instruction,
comprehensive in scope, but delegating token enumeration to the obligation table — satisfies
C-27's "names the specific canonical tokens that are forbidden" via indirect reference. C-30's
single-block placement requirement is satisfied; C-27's token-naming requirement is delegated.
If the rubric interprets "names the specific canonical tokens" to require explicit inline
enumeration, this variation scores 192/202 (−5 C-27, −5 C-30). If indirect reference through
the table satisfies the naming requirement, this scores 202/202.

Non-standard obligation terms: footprint-call / implicit-pass / ghost-system / relay-chain
C-29 form: explicit uppercase ARE (confirmed pass — not the axis under test here)

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

YOU MUST NOT use any of the canonical Obligation Term values listed in the obligation table
above as column headers or obligation names in this trace.

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
| …       |               |           |                  |                  |                 |                |               |

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
| Authentication documented    | ☐    |
| Request/response documented  | ☐    |
| Rate limits documented       | ☐    |
| Retry/idempotency documented | ☐    |
| Error propagation documented | ☐    |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                              | Severity         | Rationale | Remediation |
|--------|---------|---------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / ghost-system / relay-chain    | HIGH / MED / LOW |           |             |
| …      |         |                                                                                       |                  |           |             |

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

## V-02 — C-29 Lowercase Non-Assertive ARE Form (Q2 Probe)

**Axis**: C-29 ARE form — lowercase "are" embedded in a declarative sentence rather than
uppercase ARE in an assertive sentence.

**Hypothesis**: A schema instruction of the form "The flag column headers in the Stage 1
inventory table are the Obligation Term column values above — use those exact tokens as column
headers" — declarative, structurally equivalent, but using lowercase "are" rather than
uppercase ARE — satisfies C-29. The identity relationship is stated; token identity is
enforced; the only variation is capitalisation and grammatical assertiveness. If C-29 requires
the uppercase ARE keyword in an assertive form, this variation scores 197/202 (−5 C-29). If
lowercase in a declarative construction satisfies the directive form, this scores 202/202.

Canonical obligation terms (C-27 N/A — criterion does not trigger without non-standard
substitution).

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

The flag column headers in the Stage 1 inventory table are the Obligation Term column values
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
| …       |               |           |                  |                  |                   |                  |                    |

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
| Authentication documented    | ☐    |
| Request/response documented  | ☐    |
| Rate limits documented       | ☐    |
| Retry/idempotency documented | ☐    |
| Error propagation documented | ☐    |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                 | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW |           |             |
| …      |         |                                                                                          |                  |           |             |

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

## V-03 — Inertia Framing Block (Structural Neutrality Probe)

**Axis**: Inertia framing — a named DISCOVERY IMPERATIVE block immediately before the
inventory gate that explicitly names the specification as an incomplete artifact and the
status-quo assumption as the failure mode the persona is hired to overcome.

**Hypothesis**: Adding a prominent inertia framing block between the expert persona
declaration and the inventory gate — which names the spec as the starting point rather than
the truth, calls out "spec trust" as the primary risk, and positions the expert persona as the
counter-force to undiscovered integration surface — is structurally neutral. It adds no
content that conflicts with any criterion, modifies no schema instruction, and does not alter
gate sequencing. Expected score: 202/202. Confirms that lifecycle emphasis variation (how
prominently the status-quo assumption is surfaced) does not create criterion exposure.

Canonical obligation terms (C-27 N/A). Uppercase ARE (C-29 confirmed pass).

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

---

**DISCOVERY IMPERATIVE**

The feature specification is the starting point — not the integration truth. Specifications
describe intended behavior from a product perspective; they systematically under-represent
the integration surface because authors do not think in terms of wire calls. Every real
deployment has calls the specification never mentions: token refresh cycles, health probes
before the first payload call, SDK-internal retries, telemetry endpoints, connection
pre-warming, and delegation hops invisible at the product layer.

Your obligation as the connectors and backend integration expert is to surface what the
specification assumed away:

- **Spec trust** is the primary failure mode. A model that traces only the calls named in
  the specification is producing a product summary, not an integration trace.
- **Assumed confidence** is the secondary failure mode. A call listed in the specification
  without auth detail, retry strategy, or rate-limit acknowledgment is underdocumented
  regardless of how familiar it looks.
- **System opacity** is the third failure mode. Any call whose target system identity,
  owner, or version cannot be confirmed from the signal should be flagged, not silently
  resolved.
- **Delegation invisibility** is the fourth failure mode. Calls that execute on behalf of
  the user through managed identity or proxy chains are structurally absent from
  product-level specifications and structurally present in real deployments.

Apply all four discovery obligations to every call before accepting the inventory as
complete.

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
| …       |               |           |                  |                  |                   |                  |                    |

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
| Authentication documented    | ☐    |
| Request/response documented  | ☐    |
| Rate limits documented       | ☐    |
| Retry/idempotency documented | ☐    |
| Error propagation documented | ☐    |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                 | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW |           |             |
| …      |         |                                                                                          |                  |           |             |

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

## V-04 — C-29 Lowercase + C-30 Table-Reference Shorthand (Q1+Q2 Joint Probe)

**Axes combined**: C-29 ARE form (lowercase non-assertive) + C-30 block composition
(table-reference shorthand) + non-standard obligation terms.

**Hypothesis**: Both open questions tested simultaneously with non-standard terms to ensure
C-27/C-30 triggers. Lowercase "are" is used in the schema instruction (Q2 probe); the YOU
MUST NOT block references the obligation table by role rather than naming tokens individually
(Q1 probe). If both questions resolve positively, this scores 202/202. If only C-29 (Q2)
fails: 197/202. If only C-27/C-30 (Q1) fails: 192/202 (both criteria fail together because
C-30 requires C-27 and C-27 fails if the naming requirement is not met). If both fail:
187/202.

Non-standard obligation terms: shadow-wire / assumed-clear / void-target / transfer-chain

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term | What to discover                                                                                                                                        |
|-------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | shadow-wire     | Calls that execute as part of the feature's integration surface but are not referenced anywhere in the specification — implicit exchanges, SDK internals, telemetry |
| OBL-2 | assumed-clear   | Calls the specification names but leaves without documentation — missing auth mechanism, retry strategy, failure disposition, or rate-limit entry        |
| OBL-3 | void-target     | Calls whose target system identity, owner, API version, or location cannot be confirmed from the available signal                                        |
| OBL-4 | transfer-chain  | Calls made on behalf of the user through managed identity, OBO exchange, service principal impersonation, or any proxy delegation hop                   |

The flag column headers in the Stage 1 inventory table are the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

YOU MUST NOT use any of the canonical Obligation Term values listed in the obligation table
above as column headers or obligation names in this trace.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [shadow-wire] | [assumed-clear] | [void-target] | [transfer-chain] |
|---------|---------------|-----------|------------------|---------------|-----------------|---------------|------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N         | Y / N           | Y / N         | Y / N            |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N         | Y / N           | Y / N         | Y / N            |
| …       |               |           |                  |               |                 |               |                  |

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
| Authentication documented    | ☐    |
| Request/response documented  | ☐    |
| Rate limits documented       | ☐    |
| Retry/idempotency documented | ☐    |
| Error propagation documented | ☐    |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                              | Severity         | Rationale | Remediation |
|--------|---------|---------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / void-target / transfer-chain  | HIGH / MED / LOW |           |             |
| …      |         |                                                                                       |                  |           |             |

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

## V-05 — Section Outer Frame (C-28 Section Formula Confirming)

**Axis**: Outer frame vocabulary — numbered sections (Section 1 / Section 2 / Section 3)
instead of numbered stages, with C-28 formula adapted to section vocabulary.

**Hypothesis**: R9 V-04 used a Section frame but failed C-26/C-27 due to the open-question
exposures under test in that round. The Section frame itself was never confirmed clean.
This variation uses the Section frame with all known-good R10 patterns (explicit uppercase
ARE, canonical terms so C-27 N/A), confirming that the C-28 formula is Section-frame-safe
and that no Section-specific structural hazard exists. Expected score: 202/202.

Canonical obligation terms (C-27 N/A). Uppercase ARE (C-29 confirmed pass).

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

The flag column headers in the Section 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Section 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Section 1 inventory.

---

**SECTION 1 — CALL INVENTORY**

Populate this table before opening Section 2.

**INVENTORY GATE: Section 2 does not open until the table is complete — every discovered
call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Section 2 analysis reveals a call not already in this table, add a row
with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| …       |               |           |                  |                  |                   |                  |                    |

---

**SECTION 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this section produces any cross-section aggregation structure (fan-out
registry, call-category summary, cross-call rollup table), that structure is: (1) populated
FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT
required for trace assessment. Traces with no cross-section structures satisfy this rule by
default.

For each CALL-[N] in the Section 1 inventory table, in order, produce the following block. Do
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
| Authentication documented    | ☐    |
| Request/response documented  | ☐    |
| Rate limits documented       | ☐    |
| Retry/idempotency documented | ☐    |
| Error propagation documented | ☐    |

---

**SECTION 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                 | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW |           |             |
| …      |         |                                                                                          |                  |           |             |

---

**CROSS-SECTION AGGREGATION STRUCTURES** *(no section number — appended after Section 3, the last numbered section)*

This coda fires unconditionally. If Section 2 produced no cross-section aggregation
structures, write: "No cross-section structures produced in this trace." It does not appear
between any two numbered sections; it does not displace or renumber any existing element.

For any cross-section structure produced in Section 2:

| Property                | Value                                         |
|-------------------------|-----------------------------------------------|
| Populated from          | Per-call blocks (Section 2)                   |
| Authoritative source    | Per-call blocks — this structure is secondary |
| Required for assessment | No                                            |
