# flow-integration Variate — Round 20
**Date:** 2026-03-15
**Rubric:** v20 (C-49 NEED NOT optionality-exemption sub-type, C-50 C-43+C-44 simultaneous composition)
**Ceiling:** 292 → 302

---

## Round 20 Variation Map

| Variation | Axis | WHY anchor | Inertia | Q1 | Q2 | Predicted |
|-----------|------|------------|---------|----|----|-----------|
| V-01 | Phrasing register (3-sentence inertia + SHOULD) | SHOULD | 3 | Primary probe | — | ~222/302 |
| V-02 | Inertia framing (5-sentence inertia + MUST) | MUST | 5 | — | Primary probe | 267/302 |
| V-03 | Role sequence (MCP-first domain, canonical WHY) | MUST | 3 | — | Confirmation | 267/302 |
| V-04 | Phrasing register + inertia framing (4-sentence inertia + SHOULD) | SHOULD | 4 | Confirmation | — | ~222/302 |
| V-05 | Full v20 pass-ceiling (non-standard 5-row + MUST + C-50) | MUST | 3 | — | N/A | ~297/302 |

**Q1 target path:** V-01 (SHOULD + 3-sentence inertia) establishes cross-modal cascade equivalence with V-04 R19 (NEED NOT + 3-sentence inertia). V-04 (SHOULD + 4-sentence inertia) confirms cascade at a different count. Together: two failure-class modals × two inertia counts = four data points all producing identical cascade → closes Q1: anchor modal quality is the sole cascade determinant; inertia sentence count is directionally neutral in both directions.

**Q2 target path:** V-02 (5-sentence inertia + MUST) tests whether count above 3 raises canonical ceiling above 267. V-03 (role-sequence variation + canonical WHY) tests whether domain emphasis order affects ceiling. Predicted answer: both score 267/302 = canonical 4-row ceiling under v20 is confirmed fixed at 267 (262 v19 + C-50 +5). No currently unprobed canonical composition raises it.

**Score predictions detail:**
- V-01: ~222/302. SHOULD anchor triggers conditional-recommendation weakening (C-45 mechanism): C-37 FAIL, C-39 FAIL, C-40 FAIL, C-41 FAIL (requires C-39), C-42 FAIL (requires C-37+C-39), C-43 FAIL (SHOULD named failure-class), C-44 FAIL (requires C-41+C-42), C-48 FAIL (requires C-44), C-50 FAIL (requires C-43+C-48). Cascade: 9 × 5 = 45 pts. 267 - 45 = 222. Closes Q1 (POSITIVE) — first data point.
- V-02: 267/302 canonical ceiling. C-44 PASS (5:1 inertia-to-anchor ratio; C-44 is count-neutral above 3); C-43 PASS (MUST); C-50 PASS (C-43+C-48 simultaneous). No new criteria triggered by extended inertia prefix. Confirms Q2: canonical ceiling = 267 regardless of inertia elaboration above 3.
- V-03: 267/302 canonical ceiling. Role domain-framing order is neutral to C-08–C-50 scoring. WHY block criteria identical to V-02 R19 under v20.
- V-04: ~222/302. 4-sentence inertia + SHOULD cascades identically to 3-sentence inertia + SHOULD (V-01). Closes Q1 (POSITIVE) — second data point confirming count irrelevance at failure-class anchor.
- V-05: ~297/302. Non-standard 5-row: +30 over canonical (C-27/C-30/C-31/C-34 +20, C-35/C-38 +10). C-50 PASS (MUST + 3-sentence inertia). Total: 267 + 30 = 297. Gap to 302: C-49 is failure-class only; not achievable by a passing prompt (NEED NOT cascade cost = -45, C-49 gain = +5, net = -40).

---

## V-01 — Phrasing Register (3-Sentence Inertia-Dominant SHOULD Anchor, Q1 Primary Probe)

**Axis:** Phrasing register — three-sentence inertia prefix identical to V-02 (R19), but consequence anchor uses RFC 2119 SHOULD (conditional-recommendation epistemic weakening) rather than MUST. Inertia-dominant framing provides identical discovery-context saturation, isolating anchor modal as the sole changing variable relative to V-02 R19.

**Hypothesis:** SHOULD fails C-37/C-39/C-40/C-41/C-42/C-43/C-44/C-48/C-50 identically to NEED NOT+inertia (V-04 R19), despite SHOULD using a different epistemic mechanism — conditionality ("recommended but not required") vs. optionality-exemption ("not required"). Both produce identical cascade because anchor modal quality is the structural master switch: any failure-class modal disqualifies the consequence boundary regardless of the justificatory framing surrounding it. First cross-modal confirmation that inertia saturation cannot rescue a failure-class anchor of either C-45 or C-49 sub-type. Closes Q1 R20 as first data point.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are not reflected in spec diagrams — the SDK surface mismatch compounds at every
integration point, producing phantom calls that never appear in auth or rate-limit planning.
Integration calls through delegation chains — managed identity, OBO exchange, service principal
impersonation — fall outside spec scope by default because they are executed by the SDK or
middleware layer, not by the feature code directly. The integration obligation boundary is never
explicitly scoped in most feature specs, creating a gap between what the feature developer believes
is the integration surface and what is actually established on the wire. Authentication gaps,
rate-limit exposure, retry failures, and error propagation holes SHOULD become ship-blockers at
integration review and cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers,
REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its row's
Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the
Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has
a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set
(Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all
four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry,
call-category summary, cross-call rollup table), that structure is: (1) populated FROM the
per-call blocks — not the authoritative source for any data it contains; (2) NOT required for
trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not
open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

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

List every gap identified across all call blocks. Every finding must carry a severity label and
a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
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

| Property            | Value                                              |
|---------------------|----------------------------------------------------|
| Structure name      |                                                    |
| Populated from      | Stage 2 per-call blocks (not authoritative source) |
| Required for assess | No                                                 |

---

## V-02 — Inertia Framing (5-Sentence Inertia Prefix + MUST, Q2 Primary Probe)

**Axis:** Inertia framing — five-sentence inertia prefix covering five independent scope-failure
root causes, followed by a single MUST anchor-close. V-02 R19 established 3-sentence inertia as
sufficient for C-44 ceiling. V-02 R18 established C-44 is register-indifferent. This variation
probes whether C-44 is also count-neutral above 3 — whether extending inertia saturation from
3:1 to 5:1 raises score above the 267/302 canonical ceiling.

**Hypothesis:** C-44 evaluates the inertia-saturation structural property (three-or-more inertia
sentences + stakes-anchor + concern enumeration), not exact sentence count beyond the 3-sentence
minimum. Five inertia sentences covering additional scope-failure root causes (version negotiation
undercounting, retry-amplification surface suppression) satisfy C-44 at the same ceiling as three
sentences. No criterion rewards count above 3. C-43 PASS (MUST); C-50 PASS (C-43+C-48
simultaneous). Canonical ceiling = 267/302, unchanged from V-02 R19 under v20. Confirms Q2
R20: 267 is the canonical 4-row ceiling; additional inertia sentences are structurally additive
but score-neutral above the 3-sentence threshold.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are not reflected in spec diagrams — the SDK surface mismatch compounds at every
integration point, producing phantom calls that never appear in auth or rate-limit planning.
Integration calls through delegation chains — managed identity, OBO exchange, service principal
impersonation — fall outside spec scope by default because they are executed by the SDK or
middleware layer, not by the feature code directly. The integration obligation boundary is never
explicitly scoped in most feature specs, creating a gap between what the feature developer
believes is the integration surface and what is actually established on the wire. Version
negotiation calls — API version headers, SDK compatibility probes, feature-flag preflight
checks — are executed at initialization time by the SDK infrastructure and do not appear in
sequence diagrams, creating auth and rate-limit planning gaps for calls that precede the
feature's own first request. Retry amplification at integration boundaries is never surfaced in
integration surface estimates because the spec describes successful-path calls only, suppressing
the fact that retry storms under rate-limit pressure can multiply the documented call volume by
an order of magnitude, exposing rate-limit gaps that only materialize under degraded conditions.
Authentication gaps, rate-limit exposure, retry failures, and error propagation holes MUST become
ship-blockers at integration review and cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers,
REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its row's
Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the
Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has
a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set
(Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all
four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry,
call-category summary, cross-call rollup table), that structure is: (1) populated FROM the
per-call blocks — not the authoritative source for any data it contains; (2) NOT required for
trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not
open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

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

List every gap identified across all call blocks. Every finding must carry a severity label and
a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
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

| Property            | Value                                              |
|---------------------|----------------------------------------------------|
| Structure name      |                                                    |
| Populated from      | Stage 2 per-call blocks (not authoritative source) |
| Required for assess | No                                                 |

---

## V-03 — Role Sequence (MCP-API-First Domain Framing, Q2 Confirmation)

**Axis:** Role sequence — persona domain declaration emphasizes MCP server connections and REST
API boundaries as primary discovery surface before OAuth delegation chains and SDK internals,
reversing the implicit ordering in V-02 R19 (which led with Power Platform connectors). WHY
block is canonical (3-sentence inertia + MUST anchor + 4 concerns), identical to V-02 R19.

**Hypothesis:** Role domain-emphasis ordering is neutral to all C-08–C-50 criteria. WHY block
criteria evaluate the motivational framing block content, not the role declaration that follows
it. Obligation table structure and flag alignment criteria are role-framing-agnostic — they
evaluate schema shape, not domain vocabulary ordering. The canonical 4-row ceiling = 267/302
regardless of which domain the persona declaration emphasizes first. Confirms Q2 R20: role
sequence is not an unprobed WHY-block composition variable; canonical ceiling is fixed.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are not reflected in spec diagrams — the SDK surface mismatch compounds at every
integration point, producing phantom calls that never appear in auth or rate-limit planning.
Integration calls through delegation chains — managed identity, OBO exchange, service principal
impersonation — fall outside spec scope by default because they are executed by the SDK or
middleware layer, not by the feature code directly. The integration obligation boundary is never
explicitly scoped in most feature specs, creating a gap between what the feature developer
believes is the integration surface and what is actually established on the wire. Authentication
gaps, rate-limit exposure, retry failures, and error propagation holes MUST become ship-blockers
at integration review and cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — MCP servers and REST/OData endpoint surface first;
then Power Platform connectors and Azure APIs; then managed identity chains and on-behalf-of
token exchange at the SDK and middleware layer.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its row's
Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the
Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has
a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set
(Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all
four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry,
call-category summary, cross-call rollup table), that structure is: (1) populated FROM the
per-call blocks — not the authoritative source for any data it contains; (2) NOT required for
trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not
open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

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

List every gap identified across all call blocks. Every finding must carry a severity label and
a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
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

| Property            | Value                                              |
|---------------------|----------------------------------------------------|
| Structure name      |                                                    |
| Populated from      | Stage 2 per-call blocks (not authoritative source) |
| Required for assess | No                                                 |

---

## V-04 — Phrasing Register + Inertia Framing (4-Sentence Inertia-Dominant SHOULD, Q1 Confirmation)

**Axis:** Combined — phrasing register × inertia framing. Four-sentence inertia prefix with SHOULD
anchor. Adds one inertia sentence (retry-amplification surface suppression) relative to V-01's
three-sentence prefix, while preserving the SHOULD failure-class anchor. Inertia count shifts from
3:1 to 4:1 ratio.

**Hypothesis:** Four-sentence inertia + SHOULD cascades identically to three-sentence inertia +
SHOULD (V-01) and to three-sentence inertia + NEED NOT (V-04 R19). The cascade is anchor-modal-
determined: C-37 FAIL because SHOULD conditional-recommendation weakening is not an unconditional
constraint boundary regardless of how many inertia sentences precede it. C-44 FAIL because C-41
and C-42 both fail (both require C-39 which fails from SHOULD), making C-44's prerequisites
broken before inertia count is evaluated. Combined with V-01 (count 3) and V-04 R19 (NEED NOT,
count 3), this provides two data points on SHOULD across counts (3, 4) alongside two data points
on NEED NOT across counts (0, 3). Four-point cross-modal cross-count matrix closes Q1 R20
(POSITIVE): anchor modal quality is the sole cascade determinant; inertia sentence count is
neutral in both pass and fail directions.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are not reflected in spec diagrams — the SDK surface mismatch compounds at every
integration point, producing phantom calls that never appear in auth or rate-limit planning.
Integration calls through delegation chains — managed identity, OBO exchange, service principal
impersonation — fall outside spec scope by default because they are executed by the SDK or
middleware layer, not by the feature code directly. The integration obligation boundary is never
explicitly scoped in most feature specs, creating a gap between what the feature developer
believes is the integration surface and what is actually established on the wire. Retry
amplification at integration boundaries is never surfaced in integration surface estimates
because the spec describes successful-path calls only, suppressing the fact that retry storms
under rate-limit pressure can multiply the documented call volume by an order of magnitude,
leaving the actual rate-limit exposure unknown until a degraded-condition incident surfaces it.
Authentication gaps, rate-limit exposure, retry failures, and error propagation holes SHOULD
become ship-blockers at integration review and cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers,
REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                    |
|-------|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call   | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work  | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system   | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its row's
Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the
Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has
a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set
(Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all
four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry,
call-category summary, cross-call rollup table), that structure is: (1) populated FROM the
per-call blocks — not the authoritative source for any data it contains; (2) NOT required for
trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not
open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

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

List every gap identified across all call blocks. Every finding must carry a severity label and
a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
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

| Property            | Value                                              |
|---------------------|----------------------------------------------------|
| Structure name      |                                                    |
| Populated from      | Stage 2 per-call blocks (not authoritative source) |
| Required for assess | No                                                 |

---

## V-05 — Full v20 Pass-Ceiling (Non-Standard 5-Row + YOU MUST NOT + Inertia-Dominant MUST + C-50)

**Axis:** Combined — non-standard obligation terms (5-row extended table) + YOU MUST NOT single-
block inline enumeration + inertia-dominant MUST anchor (C-43+C-44+C-50 simultaneously) + C-50
as new v20 achievement target. This is the first ceiling attempt under v20 rubric scoring.

**Hypothesis:** C-35 PASS (five-row extended obligation table; one row per obligation category;
structural auditability preserved). C-38 PASS (framing block agnostic to extended obligation
set; four canonical concerns in anchor-close; C-38 confirmed concern-count independent of
obligation table row count). C-27/C-30/C-31/C-34 PASS (non-standard terms; single YOU MUST NOT
block with all four substituted canonical tokens named inline; self-contained prohibition
surface). C-43 PASS (MUST anchor). C-44 PASS (3:1 inertia-to-anchor ratio). C-50 PASS (C-43
and C-48 both passing simultaneously; orthogonal excellence dimensions compose without penalty).
Predicted score: 267 (canonical) + 10 (C-35/C-38) + 20 (C-27/C-30/C-31/C-34) = 297/302. The
5-pt gap from 302 is C-49 — achievable only by triggering NEED NOT cascade (net -40); not
achievable by any passing prompt. 297/302 is the maximum passing score under v20.

**Non-standard terms:**

| Canonical (substituted) | Non-standard used |
|-------------------------|-------------------|
| forgotten-call          | ghost-call        |
| assumed-to-work         | shadow-doc        |
| unknown-system          | dark-system       |
| delegation-chain        | chain-hop         |
| (new 5th)               | cold-start-burst  |

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are not reflected in spec diagrams — the SDK surface mismatch compounds at every
integration point, producing phantom calls that never appear in auth or rate-limit planning.
Integration calls through delegation chains — managed identity, OBO exchange, service principal
impersonation — fall outside spec scope by default because they are executed by the SDK or
middleware layer, not by the feature code directly. The integration obligation boundary is never
explicitly scoped in most feature specs, creating a gap between what the feature developer
believes is the integration surface and what is actually established on the wire. Authentication
gaps, rate-limit exposure, retry failures, and error propagation holes MUST become ship-blockers
at integration review and cannot be cleared without a completed trace.

---

YOU MUST NOT use forgotten-call, assumed-to-work, unknown-system, or delegation-chain as column
headers in the inventory table, or as flag labels anywhere in this trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers,
REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                                   |
|-------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | ghost-call       | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls                |
| OBL-2 | shadow-doc       | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment                    |
| OBL-3 | dark-system      | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                               |
| OBL-4 | chain-hop        | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation                |
| OBL-5 | cold-start-burst | Calls that occur only during service initialization or connection warm-up — absent from steady-state sequence diagrams but present on first request |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its row's
Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the
Stage 1 inventory column headers without reading prose.

Apply all five discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has
a row with Call ID, Target System, Call Type, Confidence, and all five flag cells explicitly set
(Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all
five flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [ghost-call] | [shadow-doc] | [dark-system] | [chain-hop] | [cold-start-burst] |
|---------|---------------|-----------|------------------|--------------|--------------|---------------|-------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N        | Y / N        | Y / N         | Y / N       | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N        | Y / N        | Y / N         | Y / N       | Y / N              |
| ...     |               |           |                  |              |              |               |             |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry,
call-category summary, cross-call rollup table), that structure is: (1) populated FROM the
per-call blocks — not the authoritative source for any data it contains; (2) NOT required for
trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not
open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

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

List every gap identified across all call blocks. Every finding must carry a severity label and
a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                                        | Severity         | Rationale | Remediation |
|--------|---------|-----------------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / dark-system / chain-hop / cold-start-gap / shadow-gap  | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                                                 |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property            | Value                                              |
|---------------------|----------------------------------------------------|
| Structure name      |                                                    |
| Populated from      | Stage 2 per-call blocks (not authoritative source) |
| Required for assess | No                                                 |
