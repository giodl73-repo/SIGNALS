---

# flow-integration — R10 Variations (v10 rubric, 202 pt ceiling)

---

## Context

**New criteria in v10:** C-29 (5 pts) + C-30 (5 pts). Both R9 top variations scored 192/192.
**R10 target:** 202/202.

**Open questions under test:**
- **Q1 (C-30):** Can the YOU MUST NOT block satisfy C-27's "names the specific canonical tokens" by referencing the obligation table by role — *"YOU MUST NOT use any of the canonical Obligation Term values listed in the obligation table above"* — without enumerating each forbidden token explicitly? PASS boundary: R8 V-05 (explicit named tokens). FAIL boundary: R9 V-02 (per-term inline distribution). Table-reference shorthand — single block in placement, no explicit enumeration — **untested.**
- **Q2 (C-29):** Does C-29 require uppercase ARE in an assertive sentence, or does lowercase "are" in a declarative construction satisfy the directive form? All confirmed PASSes used uppercase ARE. Lowercase minimum **untested.**

**Axes selected:**
- Single-axis: C-30 table-reference shorthand (V-01 / Q1 probe)
- Single-axis: C-29 lowercase non-assertive (V-02 / Q2 probe)
- Single-axis: Inertia framing block (V-03 / structural neutrality probe)
- Combined: C-29 lowercase + C-30 table-reference + non-standard terms (V-04 / Q1+Q2 joint)
- Combined: Section outer frame + all known-good patterns (V-05 / C-28 Section formula confirming)

**Score predictions:**

| Variation | Predicted | Contingency |
|-----------|-----------|-------------|
| V-01 | 202/202 or 192/202 | 202 if table-reference satisfies C-27/C-30; 192 (−5 C-27, −5 C-30) if explicit enumeration required |
| V-02 | 202/202 or 197/202 | 202 if lowercase satisfies C-29; 197 (−5 C-29) if uppercase required |
| V-03 | 202/202 | Confirming — inertia framing is structurally neutral |
| V-04 | 187–202/202 | 202 both pass; 197 Q2 only fail; 192 Q1 only fail; 187 both fail |
| V-05 | 202/202 | Confirming — Section frame with all known-good patterns; cleans R9 V-04 contamination |

---

## V-01 — C-30 Table-Reference Shorthand (Q1 Probe)

**Axis:** C-30 block composition — single YOU MUST NOT block referencing the obligation table by role without individual token enumeration.

**Hypothesis:** `YOU MUST NOT use any of the canonical Obligation Term values listed in the obligation table above as column headers or obligation names in this trace` — single block, placed after the schema instruction, comprehensive in scope — satisfies C-27/C-30 via indirect reference. If the rubric reads "names the specific canonical tokens" as requiring inline enumeration, scores 192/202 (−5 C-27, −5 C-30). If indirect reference through the table satisfies the naming requirement, scores 202/202.

Non-standard terms: **footprint-call / implicit-pass / ghost-system / relay-chain**
C-29: explicit uppercase ARE (confirmed pass — not the axis under test).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation:

| OBL | Obligation Term | What to discover |
|-----|-----------------|------------------|
| OBL-1 | footprint-call | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry |
| OBL-2 | implicit-pass | Calls the specification lists but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit entry |
| OBL-3 | ghost-system | Calls whose target system identity, owner, or location cannot be confirmed from the available signal |
| OBL-4 | relay-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the Stage 1 inventory column headers without reading prose.

YOU MUST NOT use any of the canonical Obligation Term values listed in the obligation table above as column headers or obligation names in this trace.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence | [footprint-call] | [implicit-pass] | [ghost-system] | [relay-chain] |
|---------|---------------|-----------|------------|------------------|-----------------|----------------|---------------|
| CALL-01 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| CALL-02 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| … | | | | | | | |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry, call-category summary, cross-call rollup table), that structure is: (1) populated FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT required for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field | Value |
|-------|-------|
| Mechanism | |
| Credential source | |
| Token lifetime | |
| Refresh behavior | |
| Auth gap | |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Method | |
| Endpoint | |
| Request key fields | |
| Response key fields | |
| Encoding | |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Limit value | |
| Burst risk | |
| Throttle response | |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Retry strategy | |
| Idempotent | Y / N |
| Mitigation if non-idempotent | |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

| Field | Value |
|-------|-------|
| Error disposition | |
| Propagation path | |
| Swallowing risk | |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern | Done |
|---------|------|
| Authentication documented | ☐ |
| Request/response documented | ☐ |
| Rate limits documented | ☐ |
| Retry/idempotency documented | ☐ |
| Error propagation documented | ☐ |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type | Severity | Rationale | Remediation |
|--------|---------|----------|----------|-----------|-------------|
| GAP-01 | | auth-gap / rate-limit-gap / retry-gap / error-swallow / ghost-system / relay-chain | HIGH / MED / LOW | | |
| … | | | | | |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures, write: "No cross-stage structures produced in this trace." It does not appear between any two numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property | Value |
|----------|-------|
| Populated from | Per-call blocks (Stage 2) |
| Authoritative source | Per-call blocks — this structure is secondary |
| Required for assessment | No |

---

## V-02 — C-29 Lowercase Non-Assertive ARE Form (Q2 Probe)

**Axis:** C-29 ARE form — lowercase "are" in a declarative sentence rather than uppercase ARE in an assertive sentence.

**Hypothesis:** `The flag column headers in the Stage 1 inventory table are the Obligation Term column values above — use those exact tokens as column headers` — declarative, structurally equivalent, lowercase "are" — satisfies C-29. If C-29 requires the uppercase ARE keyword in an assertive form, scores 197/202 (−5 C-29). If lowercase in a declarative construction satisfies the directive form, scores 202/202.

Canonical terms (C-27 N/A — criterion does not trigger without non-standard substitution).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation:

| OBL | Obligation Term | What to discover |
|-----|-----------------|------------------|
| OBL-1 | forgotten-call | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment |
| OBL-3 | unknown-system | Calls whose target system identity, owner, or location cannot be confirmed from the available signal |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table are the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the Stage 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------|------------------|-------------------|------------------|--------------------|
| CALL-01 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| CALL-02 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| … | | | | | | | |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry, call-category summary, cross-call rollup table), that structure is: (1) populated FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT required for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field | Value |
|-------|-------|
| Mechanism | |
| Credential source | |
| Token lifetime | |
| Refresh behavior | |
| Auth gap | |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Method | |
| Endpoint | |
| Request key fields | |
| Response key fields | |
| Encoding | |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Limit value | |
| Burst risk | |
| Throttle response | |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Retry strategy | |
| Idempotent | Y / N |
| Mitigation if non-idempotent | |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

| Field | Value |
|-------|-------|
| Error disposition | |
| Propagation path | |
| Swallowing risk | |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern | Done |
|---------|------|
| Authentication documented | ☐ |
| Request/response documented | ☐ |
| Rate limits documented | ☐ |
| Retry/idempotency documented | ☐ |
| Error propagation documented | ☐ |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type | Severity | Rationale | Remediation |
|--------|---------|----------|----------|-----------|-------------|
| GAP-01 | | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW | | |
| … | | | | | |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures, write: "No cross-stage structures produced in this trace." It does not appear between any two numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property | Value |
|----------|-------|
| Populated from | Per-call blocks (Stage 2) |
| Authoritative source | Per-call blocks — this structure is secondary |
| Required for assessment | No |

---

## V-03 — Inertia Framing Block (Structural Neutrality Probe)

**Axis:** Lifecycle emphasis / inertia framing — a named DISCOVERY IMPERATIVE block placed between the expert persona declaration and the inventory gate that explicitly names the specification as an incomplete artifact and spec-trust as the primary failure mode.

**Hypothesis:** Adding a prominent inertia framing block does not touch any schema instruction, gate sequence, or structural criterion. Confirms that lifecycle emphasis variation (how prominently the status-quo assumption is surfaced) is structurally neutral. Expected score: 202/202.

Canonical terms (C-27 N/A). Uppercase ARE (C-29 confirmed pass).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation:

| OBL | Obligation Term | What to discover |
|-----|-----------------|------------------|
| OBL-1 | forgotten-call | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment |
| OBL-3 | unknown-system | Calls whose target system identity, owner, or location cannot be confirmed from the available signal |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the Stage 1 inventory column headers without reading prose.

---

**DISCOVERY IMPERATIVE**

The feature specification is the starting point — not the integration truth. Specifications describe intended behavior from a product perspective; they systematically under-represent the integration surface because authors do not think in terms of wire calls. Every real deployment has calls the specification never mentions: token refresh cycles, health probes before the first payload call, SDK-internal retries, telemetry endpoints, connection pre-warming, and delegation hops invisible at the product layer.

Your obligation as the connectors and backend integration expert is to surface what the specification assumed away:

- **Spec trust** is the primary failure mode. A model that traces only the calls named in the specification is producing a product summary, not an integration trace.
- **Assumed confidence** is the secondary failure mode. A call listed in the specification without auth detail, retry strategy, or rate-limit acknowledgment is underdocumented regardless of how familiar it looks.
- **System opacity** is the third failure mode. Any call whose target system identity, owner, or version cannot be confirmed from the signal should be flagged, not silently resolved.
- **Delegation invisibility** is the fourth failure mode. Calls that execute on behalf of the user through managed identity or proxy chains are structurally absent from product-level specifications and structurally present in real deployments.

Apply all four discovery obligations to every call before accepting the inventory as complete.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------|------------------|-------------------|------------------|--------------------|
| CALL-01 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| CALL-02 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| … | | | | | | | |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry, call-category summary, cross-call rollup table), that structure is: (1) populated FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT required for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field | Value |
|-------|-------|
| Mechanism | |
| Credential source | |
| Token lifetime | |
| Refresh behavior | |
| Auth gap | |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Method | |
| Endpoint | |
| Request key fields | |
| Response key fields | |
| Encoding | |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Limit value | |
| Burst risk | |
| Throttle response | |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Retry strategy | |
| Idempotent | Y / N |
| Mitigation if non-idempotent | |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

| Field | Value |
|-------|-------|
| Error disposition | |
| Propagation path | |
| Swallowing risk | |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern | Done |
|---------|------|
| Authentication documented | ☐ |
| Request/response documented | ☐ |
| Rate limits documented | ☐ |
| Retry/idempotency documented | ☐ |
| Error propagation documented | ☐ |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type | Severity | Rationale | Remediation |
|--------|---------|----------|----------|-----------|-------------|
| GAP-01 | | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW | | |
| … | | | | | |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures, write: "No cross-stage structures produced in this trace." It does not appear between any two numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property | Value |
|----------|-------|
| Populated from | Per-call blocks (Stage 2) |
| Authoritative source | Per-call blocks — this structure is secondary |
| Required for assessment | No |

---

## V-04 — C-29 Lowercase + C-30 Table-Reference (Q1+Q2 Joint Probe)

**Axes combined:** C-29 lowercase non-assertive + C-30 table-reference shorthand + non-standard obligation terms.

**Hypothesis:** Both open questions tested simultaneously. Lowercase "are" (Q2) + YOU MUST NOT block referencing the table by role without explicit token enumeration (Q1). Score outcomes: 202 both pass; 197 (−5 C-29) Q2 only fails; 192 (−5 C-27, −5 C-30) Q1 only fails (C-30 requires C-27, both fail together when naming requirement is not met); 187 (−5 C-27, −5 C-29, −5 C-30) both fail.

Non-standard terms: **shadow-wire / assumed-clear / void-target / transfer-chain**

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation:

| OBL | Obligation Term | What to discover |
|-----|-----------------|------------------|
| OBL-1 | shadow-wire | Calls that execute as part of the feature's integration surface but are not referenced anywhere in the specification — implicit exchanges, SDK internals, telemetry |
| OBL-2 | assumed-clear | Calls the specification names but leaves without documentation — missing auth mechanism, retry strategy, failure disposition, or rate-limit entry |
| OBL-3 | void-target | Calls whose target system identity, owner, API version, or location cannot be confirmed from the available signal |
| OBL-4 | transfer-chain | Calls made on behalf of the user through managed identity, OBO exchange, service principal impersonation, or any proxy delegation hop |

The flag column headers in the Stage 1 inventory table are the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the Stage 1 inventory column headers without reading prose.

YOU MUST NOT use any of the canonical Obligation Term values listed in the obligation table above as column headers or obligation names in this trace.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence | [shadow-wire] | [assumed-clear] | [void-target] | [transfer-chain] |
|---------|---------------|-----------|------------|---------------|-----------------|---------------|------------------|
| CALL-01 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| CALL-02 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| … | | | | | | | |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry, call-category summary, cross-call rollup table), that structure is: (1) populated FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT required for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field | Value |
|-------|-------|
| Mechanism | |
| Credential source | |
| Token lifetime | |
| Refresh behavior | |
| Auth gap | |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Method | |
| Endpoint | |
| Request key fields | |
| Response key fields | |
| Encoding | |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Limit value | |
| Burst risk | |
| Throttle response | |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Retry strategy | |
| Idempotent | Y / N |
| Mitigation if non-idempotent | |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

| Field | Value |
|-------|-------|
| Error disposition | |
| Propagation path | |
| Swallowing risk | |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern | Done |
|---------|------|
| Authentication documented | ☐ |
| Request/response documented | ☐ |
| Rate limits documented | ☐ |
| Retry/idempotency documented | ☐ |
| Error propagation documented | ☐ |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type | Severity | Rationale | Remediation |
|--------|---------|----------|----------|-----------|-------------|
| GAP-01 | | auth-gap / rate-limit-gap / retry-gap / error-swallow / void-target / transfer-chain | HIGH / MED / LOW | | |
| … | | | | | |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures, write: "No cross-stage structures produced in this trace." It does not appear between any two numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property | Value |
|----------|-------|
| Populated from | Per-call blocks (Stage 2) |
| Authoritative source | Per-call blocks — this structure is secondary |
| Required for assessment | No |

---

## V-05 — Section Outer Frame (C-28 Section Formula Confirming)

**Axis:** Outer frame vocabulary — numbered sections (Section 1 / Section 2 / Section 3) with C-28 formula adapted to section vocabulary.

**Hypothesis:** R9 V-04 used a Section frame but failed C-26/C-27 — the frame itself was never confirmed clean. This variation uses the Section frame with all known-good patterns (uppercase ARE, canonical terms, C-27 N/A), confirming the C-28 Section formula and removing the contamination from R9 V-04. Expected score: 202/202.

Canonical terms (C-27 N/A). Uppercase ARE (C-29 confirmed pass).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation:

| OBL | Obligation Term | What to discover |
|-----|-----------------|------------------|
| OBL-1 | forgotten-call | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment |
| OBL-3 | unknown-system | Calls whose target system identity, owner, or location cannot be confirmed from the available signal |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Section 1 inventory table ARE the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the Section 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Section 1 inventory.

---

**SECTION 1 — CALL INVENTORY**

Populate this table before opening Section 2.

**INVENTORY GATE: Section 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Section 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------|------------------|-------------------|------------------|--------------------|
| CALL-01 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| CALL-02 | | | HIGH / MED / LOW | Y / N | Y / N | Y / N | Y / N |
| … | | | | | | | |

---

**SECTION 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this section produces any cross-section aggregation structure (fan-out registry, call-category summary, cross-call rollup table), that structure is: (1) populated FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT required for trace assessment. Traces with no cross-section structures satisfy this rule by default.

For each CALL-[N] in the Section 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field | Value |
|-------|-------|
| Mechanism | |
| Credential source | |
| Token lifetime | |
| Refresh behavior | |
| Auth gap | |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Method | |
| Endpoint | |
| Request key fields | |
| Response key fields | |
| Encoding | |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Limit value | |
| Burst risk | |
| Throttle response | |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field | Value |
|-------|-------|
| Retry strategy | |
| Idempotent | Y / N |
| Mitigation if non-idempotent | |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

| Field | Value |
|-------|-------|
| Error disposition | |
| Propagation path | |
| Swallowing risk | |

**CALL-[N] COMPLETION GATE** — Do not open CALL-[N+1] until all five rows are checked:

| Concern | Done |
|---------|------|
| Authentication documented | ☐ |
| Request/response documented | ☐ |
| Rate limits documented | ☐ |
| Retry/idempotency documented | ☐ |
| Error propagation documented | ☐ |

---

**SECTION 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type | Severity | Rationale | Remediation |
|--------|---------|----------|----------|-----------|-------------|
| GAP-01 | | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH / MED / LOW | | |
| … | | | | | |

---

**CROSS-SECTION AGGREGATION STRUCTURES** *(no section number — appended after Section 3, the last numbered section)*

This coda fires unconditionally. If Section 2 produced no cross-section aggregation structures, write: "No cross-section structures produced in this trace." It does not appear between any two numbered sections; it does not displace or renumber any existing element.

For any cross-section structure produced in Section 2:

| Property | Value |
|----------|-------|
| Populated from | Per-call blocks (Section 2) |
| Authoritative source | Per-call blocks — this structure is secondary |
| Required for assessment | No |

---

Written to `simulations/quest/rubrics/flow-integration-rubric-v10-variations-R10-2026-03-15.md`.

**Coverage table:**

| V | Single/Combined | C-29 form | C-30 form | Terms | Frame | Criterion exposure |
|---|----------------|-----------|-----------|-------|-------|-------------------|
| V-01 | Single (C-30) | uppercase ARE | table-reference shorthand | non-standard | Stages | C-27, C-30 |
| V-02 | Single (C-29) | lowercase declarative | N/A (canonical) | canonical | Stages | C-29 |
| V-03 | Single (inertia) | uppercase ARE | N/A (canonical) | canonical | Stages | none (structural neutrality) |
| V-04 | Combined (Q1+Q2) | lowercase declarative | table-reference shorthand | non-standard | Stages | C-27, C-29, C-30 |
| V-05 | Combined (Section confirm) | uppercase ARE | N/A (canonical) | canonical | Sections | none (C-28 Section formula) |

**What R10 settles vs. what it leaves open:**

- V-01 settles Q1 (C-30 indirect enumeration) in isolation
- V-02 settles Q2 (C-29 lowercase) in isolation
- V-03 establishes inertia framing as structural dead-weight (no criterion effect)
- V-04 provides a joint read on Q1+Q2 and cross-validates both single-axis verdicts
- V-05 cleanly confirms the Section frame after R9 V-04 contaminated it with two open-question failures simultaneously
