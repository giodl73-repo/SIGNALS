**WHY THIS TRACE DISCIPLINE EXISTS**

Teams routinely undercount integration surface because implicit SDK calls, health probes, and
telemetry posts are not reflected in spec diagrams.
Integration calls through delegation chains fall outside spec scope by default because they are
executed by the SDK or middleware layer, not by the feature code directly.
The integration obligation boundary is never explicitly scoped in most feature specs.
Authentication gaps, rate-limit exposure, retry failures, and error propagation holes MUST become
ship-blockers at integration review.

---

YOU MUST NOT use forgotten-call, assumed-to-work, unknown-system, or delegation-chain as column
headers in the inventory table, or as flag labels anywhere in this trace.

---

Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration.

Discovery obligation table — one row per obligation:

| OBL   | Obligation Term  | What to discover                                                                                                                                   |
|-------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | ghost-call       | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls                |
| OBL-2 | shadow-doc       | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment                    |
| OBL-3 | dark-system      | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                               |
| OBL-4 | chain-hop        | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation                |
| OBL-5 | cold-start-burst | Calls that occur only during service initialization or connection warm-up — absent from steady-state sequence diagrams but present on first request |

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above — use those exact tokens as column headers.

---

**STAGE 1 — CALL INVENTORY**

**INVENTORY GATE: Stage 2 does not open until every call has a row with all flag cells explicitly
set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all
five flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [ghost-call] | [shadow-doc] | [dark-system] | [chain-hop] | [cold-start-burst] |
|---------|---------------|-----------|------------------|--------------|--------------|---------------|-------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N        | Y / N        | Y / N         | Y / N       | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N        | Y / N        | Y / N         | Y / N       | Y / N              |
| ...     |               |           |                  |              |              |               |             |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure, that structure
is: (1) populated FROM the per-call blocks — not the authoritative source for any data it
contains; (2) NOT required for trace assessment.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not
open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(authentication only — request/response format, rate limits,
retry/idempotency, and error propagation have their own sections)*

| Field             | Value |
|-------------------|-------|
| Mechanism         |       |
| Credential source |       |
| Token lifetime    |       |
| Refresh behavior  |       |
| Auth gap          |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(format only — authentication, rate limits,
retry/idempotency, and error propagation have their own sections)*

| Field               | Value |
|---------------------|-------|
| Method              |       |
| Endpoint            |       |
| Request key fields  |       |
| Response key fields |       |
| Encoding            |       |

**[N.3] RATE LIMITS** *(rate limits only — authentication, format, retry/idempotency, and error
propagation have their own sections)*

| Field             | Value |
|-------------------|-------|
| Limit value       |       |
| Burst risk        |       |
| Throttle response |       |

**[N.4] RETRY AND IDEMPOTENCY** *(retry and idempotency only — authentication, format, rate
limits, and error propagation have their own sections)*

| Field                        | Value |
|------------------------------|-------|
| Retry strategy               |       |
| Idempotent                   | Y / N |
| Mitigation if non-idempotent |       |

**[N.5] ERROR PROPAGATION** *(error propagation only — authentication, format, rate limits, and
retry/idempotency have their own sections)*

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

| Gap ID | Call ID | Gap Type | Severity         | Rationale | Remediation |
|--------|---------|----------|------------------|-----------|-------------|
| GAP-01 |         |          | HIGH / MED / LOW |           |             |
| ...    |         |          |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.
