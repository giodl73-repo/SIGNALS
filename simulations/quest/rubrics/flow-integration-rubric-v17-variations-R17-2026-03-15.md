# flow-integration — R17 Variations (v17 rubric, 272 pt ceiling)

New criteria: C-43 (RFC-modal MUST/SHALL unconditional obligation class, 5 pts),
C-44 (inertia-dominant saturation: three-sentence inertia prefix with C-42 anchor close, 5 pts).
Ceiling: 262 → 272.

**Canonical-terms ceiling:** 222 pts (C-27/C-30/C-31/C-34 require non-standard substitution;
these 20 pts are N/A when canonical terms are used; C-38 additionally requires C-35 which
requires extension beyond four rows). C-43 and C-44 are achievable with canonical terms.

**Aspirational C-08–C-44 total: 182 pts** with canonical terms + C-43 + C-44.

**Open questions for R17:**
- Q1 (R17): Do RFC-weakening modals (SHOULD/MAY) fail C-40 empirically? V-02 (R16) asserts
  yes on logical grounds (SHOULD = "recommended but not required" → conditional epistemic
  weakening → C-40 FAIL) but no probe has confirmed the failure boundary.
- Q2 (R17): Does V-03 (R16, three-sentence inertia dominant) score C-44 at ceiling? V-03
  scoring table was not completed in R16.

**Axes selected:**
- Single-axis: Phrasing register — SHOULD modal failure (V-01 / Q1 SHOULD failure boundary)
- Single-axis: Phrasing register — MAY modal failure (V-02 / Q1 MAY failure boundary;
  closes Q1 by confirming both named weakening modals independently)
- Single-axis: Inertia framing — explicit three-sentence inertia dominant, C-44 clean ceiling
  probe (V-03 / Q2: confirm C-44 at ceiling with explicit sentence-count labeling)
- Combined: C-43 + C-44 — MUST modal + three-sentence inertia dominant (V-04 / interaction
  probe: does the strongest obligation form compose with inertia-dominant framing without
  criterion conflict?)
- Combined: Full 272-pt ceiling — five-row non-standard table + C-43 MUST anchor + C-44
  inertia-dominant + all prior structural elements (V-05 / first 272-pt ceiling attempt)

**Score predictions:**
- V-01: ~177/182 aspirational (-5 C-40, -5 C-43 and partial: C-37 FAIL expected, loses
        further). More precisely: C-37 FAIL (-5), C-39 FAIL (-5), C-40 FAIL (-5), C-41 N/A
        (anchor absent), C-42 FAIL (-5), C-43 FAIL (-5). Expected ~157/182 aspirational —
        large loss because every criterion downstream of C-36 that requires the stakes anchor
        cascade-fails when the modal weakens the anchor.
- V-02: Same cascade pattern as V-01 with MAY modal. Expected ~157/182 aspirational. Confirms
        Q1 for MAY independently of SHOULD.
- V-03: 182/182 aspirational ceiling — C-44 PASS (three-sentence inertia prefix + C-42
        anchor-close, 3:1 ratio); C-41 PASS (inertia framing doesn't disqualify anchor);
        C-42 PASS (anchor + concern enumeration present); C-37/C-39/C-40 PASS (consequence-
        form + delivery-phase + declarative unconditional). Completes Q2.
- V-04: 182/182 aspirational ceiling — C-43 PASS (MUST modal, stronger-obligation); C-44
        PASS (three-sentence inertia dominant + MUST anchor-close); no interaction penalty
        expected between C-43 and C-44 because they address independent surfaces (modal
        register and inertia quantity).
- V-05: 272/272 full ceiling — C-35 (five-row), C-38 (framing agnostic to extended set),
        C-43 (MUST anchor), C-44 (inertia-dominant), C-27/C-30/C-31/C-34 (non-standard +
        YOU MUST NOT block). First 272-pt ceiling attempt.

---

## V-01 — SHOULD Modal Failure Probe (Q1: RFC-Weakening Modal Failure Boundary)

**Axis**: Phrasing register — the WHY block consequence anchor uses the RFC 2119 weakening
modal SHOULD in place of indicative form. SHOULD = "recommended but not required" — it
introduces conditional epistemic weakening: the consequence is recommended, not required.
All other structural elements are identical to V-01 (R16): canonical obligation terms,
four-row table, ARE form, all gates and stages intact. Only the WHY block anchor shifts.

**Hypothesis**: SHOULD fails C-40 because it converts unconditional constraint meaning into
conditional meaning — a recommended consequence is not a named constraint boundary. C-37 FAIL
(no unconditional stakes anchor). C-39 FAIL (consequence-form requires unconditional framing).
C-40 FAIL (modal weakening present). C-41 indeterminate (no anchor to evaluate). C-42 FAIL
(no stakes anchor; concern enumeration alone does not satisfy). C-43 FAIL (SHOULD is the
named failure class in C-43). Expected cascade: each criterion dependent on the stakes anchor
fails together. Score prediction: ~157/182 aspirational (loses C-37, C-39, C-40, C-42, C-43,
each -5 = -25; C-41 still passes as no-anchor default remains undecided — if C-41 requires
anchor to be evaluable, add another -5; C-44 FAIL by C-42 prerequisite chain).

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and verify that
each call's authentication, rate limits, retry behavior, and error propagation are documented.
Undocumented integration calls SHOULD become ship-blockers at integration review and cannot be
cleared without a completed trace.

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

## V-02 — MAY Modal Failure Probe (Q1: MAY Failure Boundary, Independent Confirmation)

**Axis**: Phrasing register — the WHY block consequence anchor uses the RFC 2119 weakening
modal MAY in place of indicative form. MAY = "optional" — it introduces discretionary
epistemic weakening: the consequence is possible/permitted, not obligatory. This is distinct
from V-01 (SHOULD = recommended, conditional) in failure mechanism: SHOULD weakens by making
the consequence recommended-not-required; MAY weakens by making it optional. Both are named
failure-class modals in C-43. All structural elements other than the WHY block are identical
to V-01 (canonical terms, four-row table, ARE form, all gates).

**Hypothesis**: MAY fails C-40 by a different mechanism than SHOULD but with the same
structural outcome: unconditional constraint meaning is converted to discretionary meaning.
C-37 FAIL (discretionary "may" is not a constraint boundary). C-39 FAIL. C-40 FAIL.
C-42 FAIL. C-43 FAIL (MAY is named failure class). Expected ~157/182 aspirational — same
cascade as V-01. Confirms Q1 for MAY independently. Together V-01 + V-02 close Q1 by
confirming both named weakening modals fail the failure boundary empirically.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes. Authentication,
rate limits, retry behavior, and error propagation gaps MAY become ship-blockers at integration
review if not documented in a completed trace.

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

## V-03 — C-44 Clean Ceiling Probe (Q2: Three-Sentence Inertia Dominant, Explicit Sentence Labeling)

**Axis**: Inertia framing — the WHY block is constructed as an explicit three-sentence inertia
prefix followed by a single anchor-close sentence, with each sentence's structural role
labeled in a scoring comment. This is the C-44 canonical form by definition: three independent
scope-failure root causes — (1) implicit SDK call undercounting, (2) delegation chain
documentation failure, (3) obligation-scope never explicitly defined — followed by one sentence
that supplies both the concern enumeration and the consequence-form delivery-phase anchor.
The three-sentence structure matches R16 V-03's WHY block; the explicit sentence labels ensure
the scoring table is unambiguous and closes Q2. All other structural elements are canonical:
four-row obligation table, ARE form, all gates intact.

**Hypothesis**: 182/182 aspirational ceiling. C-44 PASS — three independent root-cause inertia
sentences + single C-42 anchor-close → inertia-sentence-count neutrality confirmed at the
named 3:1 ratio; C-41 PASS (inertia framing context + consequence anchor present); C-42 PASS
(anchor + concern enumeration in closing sentence); C-37 PASS (consequence-form + delivery-
phase + declarative unconditional); C-39 PASS; C-40 PASS (declarative register). Q2 resolved
PASS. No novel interaction — C-44 is a saturation-level property of C-41 and does not
conflict with C-42.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Feature integration scopes consistently undercount cross-system calls because spec documents
capture the API calls a developer consciously wrote while implicit SDK operations — token
refreshes, health probes, pre-warm connections — are invisible to the spec author and go
undocumented through every review.
Managed identity and on-behalf-of delegation chains are documented at their entry point only;
the downstream calls the platform makes on the user's behalf go unrecorded because design
documents describe the happy-path intent, not the runtime token exchange sequence that
executes beneath it.
Prior integration reviews repeatedly failed to catch calls in both categories not because
teams were careless but because the obligation scope — what the tracing engineer is actually
responsible for discovering — was never written down; engineers traced what they recognized,
not what they were obligated to find.
This trace defines that scope: document each call's authentication, rate limits, retry
behavior, and error propagation — undocumented integration calls become ship-blockers at
integration review and cannot be cleared without a completed trace.

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

## V-04 — C-43 + C-44 Interaction: MUST Modal + Three-Sentence Inertia Dominant

**Axis**: Combined — phrasing register (MUST modal, C-43) AND inertia framing (three-sentence
inertia dominant, C-44). The WHY block opens with the same three inertia sentences as V-03 —
covering the three independent scope-failure root causes (implicit SDK undercounting, delegation
chain gap, undefined obligation scope) — and closes with a MUST-modal anchor sentence that
supplies both consequence-form delivery-phase anchor and concern enumeration. This is the
first probe of C-43 and C-44 in combination: does the MUST modal's "stronger-obligation"
property interact with the inertia-dominant saturation in any way that degrades either
criterion? The null hypothesis is no interaction — they address independent surfaces.

**Hypothesis**: 182/182 aspirational ceiling. C-43 PASS — MUST is absolute-requirement
modal, unconditional, no epistemic weakening. C-44 PASS — three-sentence inertia prefix +
single MUST anchor-close; the anchor-close sentence also supplies concern enumeration
(→ C-42 simultaneously). No interaction penalty between C-43 and C-44: C-43 evaluates the
modal strength of the anchor sentence; C-44 evaluates the inertia-to-anchor sentence count
ratio; these are orthogonal properties. C-41 PASS (inertia + anchor present). The key
question is whether C-44's pass condition specifies "declarative indicative" or any
unconditional anchor — C-44's criterion says "consequence-form delivery-phase anchor" without
restricting register, so MUST satisfies the anchor requirement the same way it satisfies C-40.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Feature integration scopes consistently undercount cross-system calls because spec documents
capture the API calls a developer consciously wrote while implicit SDK operations — token
refreshes, health probes, pre-warm connections — are invisible to the spec author and go
undocumented through every review.
Managed identity and on-behalf-of delegation chains are documented at their entry point only;
the downstream calls the platform makes on the user's behalf go unrecorded because design
documents describe the happy-path intent, not the runtime token exchange sequence that
executes beneath it.
Prior integration reviews repeatedly failed to catch calls in both categories not because
teams were careless but because the obligation scope — what the tracing engineer is actually
responsible for discovering — was never written down; engineers traced what they recognized,
not what they were obligated to find.
This trace defines that scope: authentication, rate limits, retry behavior, and error
propagation MUST each be documented per call — undocumented integration calls MUST become
ship-blockers at integration review and MUST NOT be cleared without a completed trace.

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

## V-05 — Full 272-pt Ceiling: Five-Row Non-Standard Table + C-43 MUST + C-44 Inertia-Dominant

**Axis**: Combined — all of V-04 (C-43 MUST anchor + C-44 three-sentence inertia dominant)
PLUS five-row non-standard obligation table (C-35 extended set, C-38 obligation-count-agnostic
framing) PLUS YOU MUST NOT block for all four substituted canonical tokens (C-27/C-30/C-31/C-34).
This is the first attempt at the 272-pt ceiling. The five non-standard obligation terms are:

  spec-invisible     (substitutes: forgotten-call)
  underspecified     (substitutes: assumed-to-work)
  unresolvable       (substitutes: unknown-system)
  proxy-relay        (substitutes: delegation-chain)
  cold-start-init    (new category — no canonical equivalent; outside C-34 scope)

Four canonical tokens substituted: forgotten-call, assumed-to-work, unknown-system,
delegation-chain. One new row with no canonical equivalent. YOU MUST NOT block enumerates
all four substituted tokens explicitly by name.

WHY block: same three-sentence inertia prefix as V-03/V-04 + MUST anchor with five-concern
enumeration (adds cold-start initialization to the four canonical concerns). C-38 is in play —
the WHY block names the four canonical concerns in framing context; the anchor-close covers
all five concerns to match the extended obligation set.

**Hypothesis**: 272/272 full ceiling.
- C-35 PASS: five-row table, one row per obligation, structural auditability preserved.
- C-38 PASS: framing block does not enumerate extended obligation categories; canonical four-
  concern framing satisfies C-38 regardless of five-row extension.
- C-43 PASS: MUST modal in anchor-close → absolute-requirement, no epistemic weakening.
- C-44 PASS: three-sentence inertia prefix + MUST anchor-close (3:1 ratio); anchor-close
  contains five-concern enumeration → C-42 simultaneously; C-41 confirms inertia neutrality.
- C-27 PASS: dual-surface — schema alignment via ARE (detects header mismatch) + YOU MUST NOT
  block naming all four substituted canonical tokens.
- C-30 PASS: all four tokens in single YOU MUST NOT block.
- C-31 PASS: each substituted canonical token enumerated explicitly by name inside the block.
- C-34 PASS: all four substituted tokens named; cold-start-init has no canonical equivalent
  so it is outside C-34 scope.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Feature integration scopes consistently undercount cross-system calls because spec documents
capture the API calls a developer consciously wrote while implicit SDK operations — token
refreshes, health probes, pre-warm connections — are invisible to the spec author and go
undocumented through every review.
Managed identity and on-behalf-of delegation chains are documented at their entry point only;
the downstream calls the platform makes on the user's behalf go unrecorded because design
documents describe the happy-path intent, not the runtime token exchange sequence that
executes beneath it.
Prior integration reviews repeatedly failed to catch calls in both categories not because
teams were careless but because the obligation scope — what the tracing engineer is actually
responsible for discovering — was never written down; engineers traced what they recognized,
not what they were obligated to find.
Authentication, rate limits, retry behavior, error propagation, and cold-start initialization
MUST each be documented per call — undocumented integration calls MUST become ship-blockers
at integration review and MUST NOT be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term   | What to discover                                                                                                                              |
|-------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | spec-invisible    | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls           |
| OBL-2 | underspecified    | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment               |
| OBL-3 | unresolvable      | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                          |
| OBL-4 | proxy-relay       | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation           |
| OBL-5 | cold-start-init   | Calls that occur only during connector cold-start or session initialization: capability probes, schema handshakes, protocol version negotiation |

YOU MUST NOT use the following canonical Obligation Term tokens in flag column headers,
obligation table row terms, or any annotation within this trace:
forgotten-call, assumed-to-work, unknown-system, delegation-chain.
Use the non-standard terms above (spec-invisible, underspecified, unresolvable, proxy-relay)
in their place. cold-start-init has no canonical equivalent and is not subject to this
prohibition.

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

Apply all five discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all five flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all five flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [spec-invisible] | [underspecified] | [unresolvable] | [proxy-relay] | [cold-start-init] |
|---------|---------------|-----------|------------------|------------------|------------------|----------------|---------------|-------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N            | Y / N          | Y / N         | Y / N             |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N            | Y / N          | Y / N         | Y / N             |
| ...     |               |           |                  |                  |                  |                |               |                   |

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

| Gap ID | Call ID | Gap Type                                                                                      | Severity         | Rationale | Remediation |
|--------|---------|-----------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unresolvable / proxy-relay / cold-start | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                               |                  |           |             |

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

## Scoring Summary

| Variation | Axis | Hypothesis | Key criteria at stake |
|-----------|------|------------|-----------------------|
| V-01 | SHOULD modal in WHY | ~157/182 aspirational — cascade fail C-37/C-39/C-40/C-42/C-43 | Q1 SHOULD failure |
| V-02 | MAY modal in WHY | ~157/182 aspirational — cascade fail C-37/C-39/C-40/C-42/C-43 | Q1 MAY failure |
| V-03 | Three-sentence inertia, explicit labels | 182/182 aspirational ceiling | Q2 C-44 PASS |
| V-04 | MUST modal + three-sentence inertia | 182/182 aspirational ceiling | C-43 + C-44 no interaction |
| V-05 | Five-row non-standard + MUST + inertia | 272/272 full ceiling | First 272-pt attempt |

**Open questions for R18:**
- Q1 (R17): Resolved by V-01 (SHOULD) and V-02 (MAY) — expected FAIL confirmed.
- Q2 (R17): Resolved by V-03 — C-44 PASS at ceiling confirmed.
- Q1 (R18): Does V-04 confirm C-43 + C-44 compose without interaction penalty at 182-pt
  aspirational ceiling? (expected yes — orthogonal surfaces)
- Q2 (R18): Does V-05 achieve 272/272 full ceiling? First empirical test of the combined
  form including non-standard five-row table + C-43 MUST + C-44 inertia-dominant.
