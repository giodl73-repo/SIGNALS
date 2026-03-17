# flow-integration — R13 Variations (v13 rubric, 232 pt ceiling)

New criteria: C-35 (C-24 extended obligation set scalability, 5 pts) + C-36 (motivational
framing block, 5 pts).
R12 V-02 confirmed five-row obligation table passes C-24/C-35 (Q2 resolved: substituted-subset
enumeration scope). R12 V-03 confirmed WHY block structural neutrality (C-36 codified). R12
canonical ceiling: 212 pts. Full non-standard ceiling: 232 pts.

**Canonical-terms ceiling:** 212 pts (C-27/C-30/C-31/C-34 require non-standard substitution;
these 20 pts are N/A when canonical terms are used). C-35 and C-36 are both achievable with
canonical terms.

**R13 open questions under test:**
- Q1: Does C-36 require the framing block to reference specific failure modes, obligation
  categories, or integration risks — or does any prose block that names the purpose of the
  trace discipline satisfy C-36 regardless of content specificity? All confirmed PASS variations
  (R12 V-03) used detailed obligation-aware framing; a minimal single-sentence purpose statement
  has not been tested.
- Q2: When an extended obligation set (N > 4, C-35 in play) is paired with a motivational
  framing block (C-36), does C-36 require the framing block to acknowledge the extended
  obligation categories beyond the canonical four, or is obligation-count-agnostic framing
  sufficient to satisfy C-36 regardless of obligation set size?

**Axes selected:**
- Single-axis: C-36 minimal framing content — one-sentence purpose statement, no obligation
  references (V-01 / Q1 probe, lower bound)
- Single-axis: C-35 + C-36 count-agnostic framing — five-row obligation table, WHY block uses
  canonical four-obligation language only (V-02 / Q2 probe)
- Single-axis: Phrasing register — descriptive/declarative throughout (V-03 / structural
  neutrality probe)
- Combined: C-35 + C-36 extended-set-aware framing — five-row table, WHY block names all five
  categories including extended (V-04 / Q1+Q2 joint probe, upper bound)
- Combined: Inertia framing + phrasing register + minimal C-36 — status-quo competitor framing,
  descriptive register, one-sentence WHY block (V-05 / structural neutrality of combined axes)

**Score predictions:**
- V-01: 212/212 if any prose purpose statement satisfies C-36 (presence+position only);
        207/212 (-5 C-36) if obligation-aware content is required
- V-02: 232/232 if C-36 is obligation-count-agnostic (canonical four-obligation framing
        satisfies C-36 even with five-row table); 227/232 (-5 C-36) if extended categories
        must be named in the framing block; C-35 expected PASS regardless (five-row table
        pattern confirmed in R12)
- V-03: 212/212 — phrasing register is structurally neutral; all gates and directives remain
        explicit regardless of imperative vs declarative sentence form
- V-04: 232/232 — obligation-aware extended framing satisfies C-36 whether Q1 requires
        content specificity or not; both Q1 and Q2 resolved in favor; safe full-ceiling run
- V-05: 212/212 if minimal framing satisfies C-36 (same Q1 question as V-01 + register axis);
        207/212 (-5 C-36) if content-specific framing required; confirms inertia framing and
        register shift are each structurally neutral when combined

---

## V-01 — C-36 Minimal Framing Content (Q1 Probe)

**Axis**: C-36 content specificity — WHY THIS TRACE DISCIPLINE EXISTS block contains exactly
one sentence naming the purpose of the trace discipline; no obligation-category references, no
failure mode enumeration, no contrast framing against a status-quo competitor. All structural
elements from prior rounds are preserved unchanged.

**Hypothesis**: C-36 is a structural criterion about block presence and position (before the
expert persona declaration), not a semantic criterion about content specificity. Any prose block
that names the purpose of the trace discipline satisfies C-36 regardless of how minimal the
content is. If presence and position are sufficient, this scores 212/212 (canonical ceiling).
If C-36 requires obligation-aware framing (referencing forgotten calls, assumed-to-work,
unknown-system, or delegation-chain in the framing block), this scores 207/212 (-5 C-36;
C-16 still passes because the expert persona declaration is present and unaffected).

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and to verify that
each call's authentication, rate limits, retry behavior, and error propagation are fully
documented before the feature ships.

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

## V-02 — C-35 + C-36 Count-Agnostic Framing (Q2 Probe)

**Axis**: C-35 extended obligation set paired with C-36 motivational framing that is
obligation-count-agnostic. The obligation table has five rows (three non-standard substitutions,
one canonical-kept, one new-without-canonical-equivalent), satisfying C-35. The WHY THIS TRACE
DISCIPLINE EXISTS block uses the canonical four-obligation framing language only — it mentions
forgotten calls, assumed-to-work entries, unknown-system placeholders, and delegation chain
risk, but does not acknowledge the extended cold-start category or the five-row extension.

**Hypothesis**: C-36 is satisfied by a WHY block that names the purpose of the trace discipline;
whether the framing block acknowledges the specific obligation categories currently in play
(including any extensions beyond four) is not a C-36 requirement. The framing block's
structural role is to anchor trace rationale above the persona boundary — it is not required
to enumerate or match the obligation set. If obligation-count-agnostic framing satisfies C-36,
this scores 232/232. If C-36 requires the framing block to acknowledge extended categories
when C-35 is in play, this scores 227/232 (-5 C-36).

Non-standard terms: trace-call (sub for forgotten-call) / silent-pass (sub for assumed-to-work)
/ unverified-system (sub for unknown-system) / delegation-chain (CANONICAL, kept) /
cold-start (NEW — calls where connection reuse or pre-warm state is unknown at trace time).
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."
YOU MUST NOT block: enumerates forgotten-call + assumed-to-work + unknown-system (three
substituted canonical tokens); omits delegation-chain (canonical, not substituted) and
cold-start (new, no canonical equivalent to prohibit).
WHY block content: canonical four-obligation framing only — no cold-start reference.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration failures cluster around calls the specification did not document: the implicit
token refresh that fires on credential expiry, the SDK-internal connection probe that bypasses
the rate-limit envelope, the managed identity chain that exchanges credentials three hops
from where the spec says it authenticates, the third-party service whose owner is unknown to
the feature team. A spec-walkthrough trace finds the calls someone already thought of. This
trace discipline exists to find the ones they did not — by requiring the tracer to actively
look for forgotten calls, document assumed-to-work entries, resolve unknown-system placeholders,
and trace delegation-chain risk before the inventory closes.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term    | What to discover                                                                                                                                              |
|-------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | trace-call         | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry posts |
| OBL-2 | silent-pass        | Calls the specification names but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment             |
| OBL-3 | unverified-system  | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                                          |
| OBL-4 | delegation-chain   | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation                           |
| OBL-5 | cold-start         | Calls where the connection reuse or pre-warm state is unknown at trace time — first-invocation behavior may differ materially from steady-state behavior      |

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

| Call ID | Target System | Call Type | Confidence       | [trace-call] | [silent-pass] | [unverified-system] | [delegation-chain] | [cold-start] |
|---------|---------------|-----------|------------------|--------------|---------------|---------------------|--------------------|--------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N        | Y / N         | Y / N               | Y / N              | Y / N        |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N        | Y / N         | Y / N               | Y / N              | Y / N        |
| ...     |               |           |                  |              |               |                     |                    |              |

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

| Gap ID | Call ID | Gap Type                                                                                                   | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unverified-system / delegation-chain / cold-start  | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                                            |                  |           |             |

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

## V-03 — Phrasing Register (Structural Neutrality Probe)

**Axis**: Phrasing register — all imperative instructions are rephrased as declarative/descriptive
constructions throughout the prompt body. "Populate this table before opening Stage 2" becomes
"The inventory table is fully populated before Stage 2 analysis begins." Gate commands become
completion conditions stated as declarations. Section exclusions are phrased as descriptions
rather than prohibitions. No schema elements, obligation terms, ARE directives, table structures,
or checklist items are removed or changed — only the grammatical register of the surrounding
prose.

**Hypothesis**: Phrasing register is structurally neutral. C-10 (inventory-first gate), C-12
(gate-enforced per-call completion), C-15 (late-call inventory discipline), and C-20
(unconditional cross-stage stage) each require explicit instructions — none require the
imperative mood. A gate stated as "Stage 2 analysis begins only after the inventory gate
clears" is as explicit as "Stage 2 does not open until the table is complete." Expected:
212/212 (canonical ceiling). Confirms register is a free variation axis.

Canonical obligation terms. No YOU MUST NOT block needed.
WHY block: obligation-aware purpose statement (references all four obligation categories).
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Every cross-system integration has calls the specification does not document: the implicit
token refresh that fires on credential expiry, the SDK health probe that never appears in the
design, the service whose identity the feature team cannot confirm, the managed identity chain
that exchanges credentials outside the feature's trust boundary. These forgotten calls,
assumed-to-work entries, unknown-system placeholders, and delegation-chain exposures are the
ones that cause production incidents. This trace discipline exists to discover them before
the feature ships — by applying four discovery obligations to the call inventory before any
per-call analysis begins.

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

All four discovery obligations are applied while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

The inventory table is fully populated before Stage 2 analysis begins.

**INVENTORY GATE: Stage 2 analysis begins only when every discovered call has a row with
Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N;
blank is not acceptable).**

NEW-CALL RULE: Any call discovered during Stage 2 analysis that is not already in the
inventory receives a row — with all four flag cells set — before its analysis block opens.

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

## V-04 — Combined: C-35 + C-36 Extended-Set-Aware Framing (Q1+Q2 Joint Probe)

**Axis**: Five-row obligation table (C-35 in play, same non-standard terms as V-02) paired
with a WHY THIS TRACE DISCIPLINE EXISTS block that explicitly names all five obligation
categories — including the extended cold-start category — in its framing. This is the
upper-bound probe: if C-36 requires obligation-aware content (Q1) or extended-set acknowledgment
(Q2), this variation satisfies both. If C-36 requires neither, this variation still satisfies
the criterion by virtue of having a WHY block at all.

**Hypothesis**: Regardless of how Q1 and Q2 resolve — whether C-36 requires obligation-aware
content, extended-set acknowledgment, or neither — this variation satisfies C-36. It is the
safe full-ceiling probe for C-35 + C-36 combined. Expected: 232/232.

Non-standard terms: trace-call / silent-pass / unverified-system / delegation-chain (canonical,
kept) / cold-start (new, no canonical equivalent).
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."
YOU MUST NOT block: enumerates forgotten-call + assumed-to-work + unknown-system (three
substituted canonical tokens).
WHY block content: obligation-aware AND extended-set-aware — names all five obligation
categories including cold-start.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration failures cluster around calls that were never in scope for documentation. The
feature specification names what the author intended; it does not name the implicit calls that
execute underneath. This trace discipline exists to force explicit discovery across five
obligation categories before any call analysis begins:

- **trace-call** — calls that execute but do not appear in the specification; the token
  refresh, the SDK health probe, the telemetry post that fires on every invocation
- **silent-pass** — calls the specification names but documents as if they cannot fail;
  authentication details, retry strategies, and rate-limit acknowledgments left blank
- **unverified-system** — calls whose target system identity, owner, or location cannot be
  confirmed from the available signal at trace time
- **delegation-chain** — calls made on behalf of the user through managed identity, OBO token
  exchange, service principal impersonation, or proxy delegation
- **cold-start** — calls where connection reuse or pre-warm state is unknown; first-invocation
  behavior may differ materially from steady-state behavior

A trace that documents only the calls the specification named has not completed this discipline.
The inventory gate does not clear until all five obligation categories have been applied.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term    | What to discover                                                                                                                                              |
|-------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | trace-call         | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry posts |
| OBL-2 | silent-pass        | Calls the specification names but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment             |
| OBL-3 | unverified-system  | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                                          |
| OBL-4 | delegation-chain   | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation                           |
| OBL-5 | cold-start         | Calls where the connection reuse or pre-warm state is unknown at trace time — first-invocation behavior may differ materially from steady-state behavior      |

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

| Call ID | Target System | Call Type | Confidence       | [trace-call] | [silent-pass] | [unverified-system] | [delegation-chain] | [cold-start] |
|---------|---------------|-----------|------------------|--------------|---------------|---------------------|--------------------|--------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N        | Y / N         | Y / N               | Y / N              | Y / N        |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N        | Y / N         | Y / N               | Y / N              | Y / N        |
| ...     |               |           |                  |              |               |                     |                    |              |

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

| Gap ID | Call ID | Gap Type                                                                                                   | Severity         | Rationale | Remediation |
|--------|---------|------------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unverified-system / delegation-chain / cold-start  | HIGH / MED / LOW |           |             |
| ...    |         |                                                                                                            |                  |           |             |

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

## V-05 — Combined: Inertia Framing + Phrasing Register + Minimal C-36

**Axis**: Three combined axes, all hypothesized structurally neutral.
(1) Inertia framing — the WHY block names the default spec-walkthrough pattern as the
approach this discipline displaces, and states why that displacement is necessary. The WHY
block content is obligation-aware but structured around the contrast with the status-quo
approach rather than a direct enumeration of obligation categories.
(2) Phrasing register — declarative/descriptive throughout, mirroring V-03's approach.
(3) Minimal C-36 framing — the WHY block is present and anchored before the expert persona
but is structured as contrast prose rather than an explicit purpose statement.

**Hypothesis**: All three axes are structurally neutral. The inertia framing pattern was
confirmed neutral in R12 V-03 (inertia framing, canonical terms, no WHY block — scored
202/202 at v12 ceiling). The phrasing register axis was confirmed neutral in V-03 above. The
minimal C-36 question mirrors V-01. If V-01 resolves that minimal/contrast framing satisfies
C-36, this scores 212/212. If C-36 requires a direct purpose statement (not contrast framing),
this scores 207/212 (-5 C-36). Combined probe confirms the three axes compose independently.

Canonical obligation terms. No YOU MUST NOT block needed.
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above."

---

**WHY THIS TRACE DISCIPLINE EXISTS**

The default approach to integration traces takes the spec's call list, attaches auth and format
documentation to each named call, and stops. It produces a record of what was planned — not
what will execute. The calls that cause production incidents are not in that record: the
implicit token refresh that fires on credential expiry, the SDK-internal probe that bypasses
the rate-limit envelope, the third-party service whose identity the feature team cannot confirm,
the managed identity chain that exchanges tokens three hops from where the spec says the
feature authenticates. A spec-walkthrough trace finds the calls someone already thought of.
This trace finds the ones they did not.

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

All four discovery obligations are applied while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

The inventory table is fully populated before Stage 2 analysis begins.

**INVENTORY GATE: Stage 2 analysis begins only when every discovered call has a row with
Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N;
blank is not acceptable).**

NEW-CALL RULE: Any call discovered during Stage 2 analysis that is not already in the
inventory receives a row — with all four flag cells set — before its analysis block opens.

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

## Variation Summary

| Variation | Axis | WHY Block Content | Obligation Set | Terms | C-36 Predicts | Ceiling |
|-----------|------|-------------------|----------------|-------|---------------|---------|
| V-01 | C-36 minimal framing (Q1 probe) | One sentence, no obligation refs | 4-row canonical | Canonical | PASS if presence+position; FAIL if content-specific required | 212 |
| V-02 | C-35 + C-36 count-agnostic framing (Q2 probe) | Four-obligation language, no cold-start mention | 5-row extended | Non-standard | PASS if count-agnostic; FAIL if extended categories must be named | 232 |
| V-03 | Phrasing register — declarative/descriptive | Obligation-aware purpose statement | 4-row canonical | Canonical | PASS (register neutral) | 212 |
| V-04 | C-35 + C-36 extended-set-aware (Q1+Q2 upper bound) | Names all five categories including cold-start | 5-row extended | Non-standard | PASS regardless of Q1/Q2 resolution | 232 |
| V-05 | Inertia framing + register + minimal C-36 (neutrality) | Contrast framing (inertia), declarative register | 4-row canonical | Canonical | PASS if minimal/contrast framing satisfies; FAIL if direct purpose required | 212 |

**Q1 diagnostic**: V-01 PASS → minimal framing satisfies C-36; V-01 FAIL → V-03's
obligation-aware framing is the lower bound for content.

**Q2 diagnostic**: V-02 PASS → count-agnostic framing satisfies C-36 with extended sets;
V-02 FAIL → V-04 establishes the safe pattern (extended-set-aware framing required).

**Interaction check**: V-05 tests whether the inertia-framing + register combination from
R12 composes cleanly with the minimal C-36 content boundary established by V-01.
