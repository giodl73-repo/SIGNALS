# flow-integration — R18 Variations (v18 rubric, 282 pt ceiling)

New criteria: C-45 (SHOULD conditional-recommendation failure mechanism, 5 pts),
C-46 (MAY discretionary-possibility failure mechanism + compound conditionality, 5 pts).
Ceiling: 272 → 282.

**Canonical-terms ceiling:** 232 pts (C-27/C-30/C-31/C-34 require non-standard substitution;
these 20 pts are N/A when canonical terms are used; C-38 additionally requires C-35 which
requires extension beyond four rows). C-43, C-44, C-45, and C-46 are each achievable with
canonical terms.

**Aspirational C-08–C-46 total: 192 pts** with canonical terms + all new criteria passing.

**Open questions for R18:**
- Q1 (R18): Does a MAY-only anchor (no conditional clause) confirm modal-only MAY failure
  independent of compound conditionality? V-02 (R17) used compound form (MAY + "if not
  documented"); a minimal MAY probe isolating modal-only failure would complete the
  single-mechanism boundary for the discretionary sub-type.
- Q2 (R18): Does V-03 (three-sentence inertia dominant) score C-44 at ceiling? Carried from
  R17 Q2 — V-03 (R17) scoring table was not completed.

**Axes selected:**
- Single-axis: Phrasing register — MAY-only anchor, no conditional clause (V-01 / Q1 R18
  modal-only failure boundary probe)
- Single-axis: Inertia framing — explicit three-sentence inertia dominant, declarative
  anchor-close with concern enumeration (V-02 / Q2 R18: clean C-44 ceiling confirmation)
- Single-axis: Output format — per-call analysis as prose labeled sections instead of tables
  (V-03 / format-neutrality probe: do structural criteria hold across table vs. prose
  per-call representation?)
- Combined: C-43 + C-44 — MUST modal + three-sentence inertia dominant (V-04 / interaction
  probe: does the strongest obligation form compose with inertia-dominant framing without
  criterion conflict?)
- Combined: Full 282-pt ceiling — five-row non-standard table + MUST anchor + inertia-
  dominant + YOU MUST NOT block (V-05 / first 282-pt ceiling attempt with v18 criteria active)

**Score predictions:**
- V-01: ~157/192 aspirational — C-37 FAIL (-5), C-39 FAIL (-5), C-40 FAIL (-5), C-41 PASS
  (no inertia framing present; neutrality rule not tested), C-42 FAIL (-5, no stakes anchor),
  C-43 FAIL (-5), C-44 FAIL (-5, C-42 prerequisite broken), C-45 N/A (SHOULD not used),
  C-46 PASS (+5, MAY mechanism 1 alone — discretionary-possibility without compound
  conditionality; closes Q1 R18 confirming modal-only boundary). Net: -30 from ceiling.
  Expected ~162/192 aspirational if C-46 PASS confirmed; ~157/192 if C-46 scored N/A for
  non-compound form.
- V-02: 192/192 aspirational ceiling (canonical terms) — C-44 PASS (three-sentence inertia
  prefix, 3:1 ratio, declarative anchor-close with concern enumeration simultaneously
  satisfying C-42); C-41 PASS (inertia framing doesn't disqualify); C-42 PASS; C-37/C-39/C-40
  PASS; C-43 conditional on declarative form vs. MUST/SHALL (see Q2 note). Closes Q2.
- V-03: Expected ceiling match — all structural criteria satisfied; C-03 PASS (method + key
  fields in labeled prose sections); C-11 PASS (single-concern prose sections with exclusion
  statements); C-13 PASS; C-17 PASS (separate labeled prose fields); C-14 PASS (completion
  checklist retained as table). Format-neutrality confirmed or refuted at per-call level.
- V-04: 192/192 aspirational ceiling — C-43 PASS (MUST modal, stronger-obligation); C-44
  PASS (three-sentence inertia dominant + MUST anchor-close); no interaction penalty expected
  (C-43 and C-44 address independent surfaces).
- V-05: 282/282 full ceiling — C-35 (five rows), C-38 (framing agnostic), C-43 (MUST),
  C-44 (inertia-dominant), C-27/C-30/C-31/C-34 (non-standard + YOU MUST NOT block), C-45/C-46
  N/A (MUST used, not SHOULD/MAY). First 282-pt ceiling attempt under v18.

---

## V-01 — MAY-Only Anchor Probe (Q1 R18: Modal-Only MAY Failure Boundary)

**Axis**: Phrasing register — the WHY block consequence anchor uses RFC 2119 MAY with no
conditional clause. MAY = "optional" — it introduces discretionary-possibility epistemic
weakening: the consequence is permitted but not required. V-02 (R17) used compound form
(MAY + "if not documented"); this variation isolates mechanism 1 (modal-only MAY) by removing
the conditional clause entirely, testing whether modal-only discretionary weakening alone
disqualifies the anchor independently of compound conditionality.

**Hypothesis**: MAY-only fails C-40 identically to compound MAY (V-02, R17) because the
discretionary-possibility weakening is carried by the modal alone, not by the conditional
clause — "MAY become ship-blockers" converts the unconditional constraint to a permission,
regardless of whether a conditional clause is attached. C-37 FAIL (discretionary possibility
is not an unconditional constraint boundary). C-39 FAIL (unconditional form requirement
violated by MAY modal). C-40 FAIL (unconditional constraint meaning not preserved). C-43 FAIL
(MAY is a named failure-class modal). C-42 FAIL (no stakes anchor; concern enumeration present
but insufficient). C-44 FAIL (C-42 prerequisite broken). C-46: PASS — this is the modal-only
sub-case of C-46's discretionary-possibility mechanism; compound conditionality not present,
but mechanism 1 (MAY modal) alone sufficient for disqualification. Expected: same cascade
outcome as V-02 (R17) despite absent mechanism 2. Closes Q1 (R18).

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and verify that
each call's authentication, rate limits, retry behavior, and error propagation are documented.
Undocumented integration calls MAY become ship-blockers at integration review and cannot be
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

| Property            | Value                                                                    |
|---------------------|--------------------------------------------------------------------------|
| Structure name      |                                                                          |
| Populated from      | Stage 2 per-call blocks (not authoritative source)                       |
| Required for assess | No                                                                       |

---

## V-02 — Three-Sentence Inertia Dominant, Declarative Anchor-Close (Q2 R18: C-44 Ceiling)

**Axis**: Inertia framing — the WHY block uses a three-sentence inertia prefix covering three
independent scope-failure root causes, followed by a single anchor-close sentence that
simultaneously supplies a consequence-form delivery-phase anchor and explicit concern
enumeration. This is the same structural pattern as V-03 (R17) whose scoring was not
completed, reproduced here as a clean ceiling probe.

**Hypothesis**: C-44 PASS — three-sentence inertia prefix (3:1 inertia-to-anchor ratio by
sentence count) followed by a C-42 anchor-close constitutes the inertia-dominant variant of
the highest-information WHY block. C-41 holds at three-sentence inertia saturation (inertia
quantity does not disqualify; only the stakes anchor presence or absence determines outcome).
C-37 PASS (declarative unconditional anchor-close, consequence-form, delivery-phase marker
"at integration review"). C-39 PASS. C-40 PASS (no modal weakening). C-42 PASS (stakes
anchor + concern enumeration both present in anchor-close). C-44 PASS (3:1 inertia ratio +
C-42 anchor-close simultaneously). Expected: 192/192 aspirational ceiling (canonical terms).
Closes Q2 (R18) by providing complete scoring evidence.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are invisible at the feature authorship level — but they carry authentication
and rate-limit exposure identical to any explicitly named call.

Delegation chains — managed identity, OBO token exchange, service principal impersonation —
traverse ownership and system boundaries that are never documented at the point of code
authorship, leaving the actual call graph unknown until the trace forces it to the surface.

The obligation boundary of the trace itself — what counts as a discovered call versus an
assumed-to-work entry — is almost never defined before a trace begins, so underdocumented
calls survive review by appearing in the spec without auth detail, retry strategy, or
rate-limit acknowledgment.

Authentication gaps, rate-limit exposure, retry failures, and error propagation holes become
ship-blockers at integration review and cannot be cleared without a completed trace.

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

| Property            | Value                                                                    |
|---------------------|--------------------------------------------------------------------------|
| Structure name      |                                                                          |
| Populated from      | Stage 2 per-call blocks (not authoritative source)                       |
| Required for assess | No                                                                       |

---

## V-03 — Prose Per-Call Analysis (Output Format: Table vs. Prose Sections)

**Axis**: Output format — Stage 2 per-call analysis sections are delivered as labeled prose
paragraphs with explicit concern exclusions rather than tables. The obligation table, inventory
table, completion gate checklist, and gap inventory table are retained as tables. Only the
per-call concern sections (N.1 through N.5) are converted to prose format with labeled fields.

**Hypothesis**: Format-neutral across all structural criteria. C-03 PASS — method and key
fields appear in separately labeled prose sections (distinct labeled position, not a merged
cell). C-11 PASS — each prose paragraph carries a single-concern label with explicit exclusion
statement. C-13 PASS — every section names its concern and excludes all other concerns in
opening prose. C-17 PASS — rate limit prose section contains explicitly labeled "Limit value:",
"Burst risk:", "Throttle response:" fields as inline labels. No structural criterion requires
the table form specifically. C-14 PASS — completion gate remains a checklist table, gating
explicitly. Expected: ceiling match with V-02 baseline; any criterion that fails relative to
table-format V-02 identifies a table-dependency in the rubric not previously named.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and verify that
each call's authentication, rate limits, retry behavior, and error propagation are documented.
Authentication gaps, rate-limit exposure, retry failures, and error propagation holes become
ship-blockers at integration review and cannot be cleared without a completed trace.

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

Mechanism: [authentication mechanism used — bearer token, managed identity, API key, etc.]
Credential source: [where the credential originates — Key Vault ref, app registration, etc.]
Token lifetime: [token expiry window and renewal policy]
Refresh behavior: [how token refresh is triggered — proactive, reactive, SDK-managed, etc.]
Auth gap: [any gap in auth documentation or coverage; "none identified" if fully covered]

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate
limits, retry/idempotency, and error propagation each have their own sections)*

Method: [HTTP verb or protocol method]
Endpoint: [URL pattern or connector action name]
Request key fields: [enumerate primary request parameters or body fields]
Response key fields: [enumerate primary response fields consumed downstream]
Encoding: [JSON / XML / OData / binary / etc.]

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format,
retry/idempotency, and error propagation each have their own sections)*

Limit value: [requests per second / per minute / per day; or "not published" if unknown]
Burst risk: [scenarios under which this call could contribute to a limit breach]
Throttle response: [what the system returns on 429 or equivalent; back-off behavior]

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication,
format, rate limits, and error propagation each have their own sections)*

Retry strategy: [max attempts, back-off policy, which error classes trigger retry]
Idempotent: [Yes / No — and one-line rationale]
Mitigation if non-idempotent: [deduplication key, conditional write, or "none — gap"]

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format,
rate limits, and retry/idempotency each have their own sections)*

Error disposition: [how this call's errors are handled — surfaced, swallowed, retried, logged]
Propagation path: [how the error reaches the caller; intermediate transforms or wrappers]
Swallowing risk: [whether any code path discards the error without surfacing it upstream]

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

| Property            | Value                                                                    |
|---------------------|--------------------------------------------------------------------------|
| Structure name      |                                                                          |
| Populated from      | Stage 2 per-call blocks (not authoritative source)                       |
| Required for assess | No                                                                       |

---

## V-04 — MUST Modal + Three-Sentence Inertia Dominant (C-43 + C-44 Interaction)

**Axis**: Combined — inertia framing (three-sentence prefix, 3:1 ratio) + phrasing register
(RFC 2119 MUST in the anchor-close sentence). V-02 uses declarative indicative in the
anchor-close; V-04 substitutes MUST to simultaneously probe C-43 (stronger-obligation modal
class) and C-44 (inertia-dominant saturation). Tests whether C-43 and C-44 compose without
interaction penalty.

**Hypothesis**: C-43 PASS (MUST introduces stronger-obligation force, not epistemic weakening;
passes C-40 unconditionally). C-44 PASS (three-sentence inertia prefix + MUST anchor-close
with concern enumeration satisfies the inertia-dominant variant of the C-42 highest-information
form). No interaction penalty expected — C-43 evaluates modal register and C-44 evaluates
inertia sentence count; they address independent properties of the WHY block. Expected:
192/192 aspirational ceiling (canonical terms, same as V-02 baseline with C-43 explicitly
confirmed by MUST modal).

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are invisible at the feature authorship level — but they carry authentication
and rate-limit exposure identical to any explicitly named call.

Delegation chains — managed identity, OBO token exchange, service principal impersonation —
traverse ownership and system boundaries that are never documented at the point of code
authorship, leaving the actual call graph unknown until the trace forces it to the surface.

The obligation boundary of the trace itself — what counts as a discovered call versus an
assumed-to-work entry — is almost never defined before a trace begins, so underdocumented
calls survive review by appearing in the spec without auth detail, retry strategy, or
rate-limit acknowledgment.

Authentication gaps, rate-limit exposure, retry failures, and error propagation holes MUST
become ship-blockers at integration review — none can be cleared without a completed trace.

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

| Property            | Value                                                                    |
|---------------------|--------------------------------------------------------------------------|
| Structure name      |                                                                          |
| Populated from      | Stage 2 per-call blocks (not authoritative source)                       |
| Required for assess | No                                                                       |

---

## V-05 — Full 282-pt Ceiling: Five-Row Non-Standard + MUST + Inertia-Dominant

**Axis**: Combined — five-row extended non-standard obligation table (C-35 + C-38) + YOU
MUST NOT prohibition block (C-27 + C-30 + C-31 + C-34) + RFC 2119 MUST anchor (C-43) +
three-sentence inertia dominant (C-44). First attempt at the 282-pt ceiling with v18 criteria
active. C-45 and C-46 are N/A (MUST used, not SHOULD or MAY).

**Hypothesis**: All 39 aspirational criteria satisfied simultaneously. C-35 PASS (five-row
table, one row per obligation category). C-38 PASS (WHY block framing is obligation-count-
agnostic — concern enumeration names the four canonical concerns, not the extended five).
C-27 PASS (dual-surface: schema alignment detects term substitution by column comparison;
YOU MUST NOT block names all four substituted canonical tokens explicitly). C-30 PASS (all
substituted tokens in a single YOU MUST NOT block). C-31 PASS (inline enumeration, not
table-reference shorthand). C-34 PASS (all four substituted tokens enumerated — OBL-5
has no canonical equivalent, so it is outside C-34 scope). C-43 PASS (MUST anchor). C-44
PASS (three-sentence inertia dominant + MUST anchor-close with concern enumeration). Expected:
282/282.

Non-standard substitution map:
- OBL-1: "missing-call" (replaces canonical "forgotten-call")
- OBL-2: "underdocumented-call" (replaces canonical "assumed-to-work")
- OBL-3: "opaque-system" (replaces canonical "unknown-system")
- OBL-4: "identity-proxy-chain" (replaces canonical "delegation-chain")
- OBL-5: "cold-start-call" (new category; no canonical equivalent — outside C-34 scope)

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are invisible at the feature authorship level — but they carry authentication
and rate-limit exposure identical to any explicitly named call.

Delegation chains — managed identity, OBO token exchange, service principal impersonation —
traverse ownership and system boundaries that are never documented at the point of code
authorship, leaving the actual call graph unknown until the trace forces it to the surface.

The obligation boundary of the trace itself — what counts as a discovered call versus an
assumed-to-work entry — is almost never defined before a trace begins, so underdocumented
calls survive review by appearing in the spec without auth detail, retry strategy, or
rate-limit acknowledgment.

Authentication gaps, rate-limit exposure, retry failures, and error propagation holes MUST
become ship-blockers at integration review — none can be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term      | What to discover                                                                                                                    |
|-------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | missing-call         | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | underdocumented-call | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | opaque-system        | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | identity-proxy-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |
| OBL-5 | cold-start-call      | Calls that fire only during service initialization, connection establishment, or first-request warm-up and are absent during steady state |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers. A column header that does not match its
row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table
to the Stage 1 inventory column headers without reading prose.

YOU MUST NOT use the canonical Obligation Term values forgotten-call, assumed-to-work,
unknown-system, or delegation-chain anywhere in this trace — not in column headers, flag
labels, prose annotations, finding references, or the gap inventory. The non-standard terms
above are the complete vocabulary contract for this trace.

Apply all five discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call
has a row with Call ID, Target System, Call Type, Confidence, and all five flag cells
explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with
all five flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [missing-call] | [underdocumented-call] | [opaque-system] | [identity-proxy-chain] | [cold-start-call] |
|---------|---------------|-----------|------------------|----------------|------------------------|-----------------|------------------------|-------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N          | Y / N                  | Y / N           | Y / N                  | Y / N             |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N          | Y / N                  | Y / N           | Y / N                  | Y / N             |
| ...     |               |           |                  |                |                        |                 |                        |                   |

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
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / opaque-system / identity-proxy-chain / cold-start-gap | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                                       |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property            | Value                                                                    |
|---------------------|--------------------------------------------------------------------------|
| Structure name      |                                                                          |
| Populated from      | Stage 2 per-call blocks (not authoritative source)                       |
| Required for assess | No                                                                       |

---

## Scoring Summary

| V   | Axis                                           | Open Q      | Key Criteria Under Test              | Predicted Score |
|-----|------------------------------------------------|-------------|--------------------------------------|-----------------|
| V-01 | Phrasing register — MAY-only anchor           | Q1 (R18)    | C-37 FAIL, C-40 FAIL, C-43 FAIL, C-46 PASS | ~162/192 asp. |
| V-02 | Inertia framing — 3-sentence prefix           | Q2 (R18)    | C-44 PASS, C-41 PASS, C-42 PASS          | 192/192 asp.   |
| V-03 | Output format — prose per-call sections       | —           | C-03, C-11, C-13, C-17 format-neutrality | ~192/192 asp.  |
| V-04 | Combined: C-43 (MUST) + C-44 (inertia-dom.)   | —           | C-43 PASS, C-44 PASS, no interaction     | 192/192 asp.   |
| V-05 | Combined: full 282 ceiling                    | —           | C-35, C-38, C-43, C-44, C-27/C-30/C-31/C-34 | 282/282   |

**Q1 (R18) resolution test (V-01):** If C-46 PASS and cascade confirmed, modal-only MAY
failure boundary established independent of compound conditionality. C-46's compound-
conditionality finding (V-02, R17) is a special case; the modal mechanism alone is sufficient
and primary.

**Q2 (R18) resolution test (V-02):** If C-44 PASS at 192/192, inertia-sentence-count
neutrality is confirmed at three sentences; the 3:1 inertia-to-anchor ratio with C-42
anchor-close is the ceiling form for C-44.
