# flow-integration — R12 Variations (v12 rubric, 222 pt ceiling)

New criteria: C-33 (C-32 multi-subject collective ARE form, 5 pts) + C-34 (C-31 complete inline
enumeration full coverage, 5 pts).
All R11 top variations scored 202/212 (IS form and partial enumeration each failed as predicted).
R11 V-03 (canonical, lifecycle expansion) and V-05 (canonical, register shift) confirmed 212/212.
R12 target: 222/222.

**Canonical-terms ceiling:** 202 pts (C-27/C-30/C-31/C-34 require non-standard substitution; these
20 pts are N/A when canonical terms are used). C-33 is achievable with canonical terms — it tests
the ARE subject form, not whether substitution is in play.

**R12 open questions under test:**
- Q1: Does C-33 require the exact subject phrase "the flag column headers" in the ARE directive, or
  does any valid multi-subject ARE construction satisfy it? For example: "Flag column headers ARE
  the Obligation Term column values above" (no definite article, no "in the Stage 1 inventory
  table" qualifier). All confirmed PASS variations used "The flag column headers in the Stage 1
  inventory table ARE the Obligation Term column values above"; alternate multi-subject phrasings
  have not been tested.
- Q2: When the obligation table has five or more rows with a mix of non-standard and canonical
  terms, does C-34 require the YOU MUST NOT block to enumerate all substituted canonical tokens
  (the per-substitution reading), or all terms in the full extended set regardless of
  canonical/non-standard status (the per-table-row reading)? All prior tested cases had exactly
  four rows with all four terms substituted; a mixed five-row case has not been tested.

**Axes selected:**
- Single-axis: C-33 subject form — alternate ARE subject without definite article (V-01 / Q1 probe)
- Single-axis: C-34 extended obligation set — 5-row mixed table, substituted-subset enumeration
  (V-02 / Q2 probe)
- Single-axis: Inertia framing — status-quo competitor named prominently before the persona
  (V-03 / structural neutrality probe)
- Combined: C-33 alternate subject + C-34 extended set (V-04 / Q1+Q2 joint probe)
- Combined: Role sequence (inline persona within Stage 1) + phrasing register (V-05 / confirming
  clean sweep)

**Score predictions:**
- V-01: 202/202 (canonical ceiling) if any multi-subject ARE satisfies C-33; 197/202 (−5 C-33,
        C-32 still passes — uppercase ARE assertive sentence present) if exact subject phrase
        "the flag column headers" is required
- V-02: 222/222 if C-34 applies per-substituted-token only (substituted-subset enumeration
        sufficient); 212/222 (−5 C-34) if C-34 requires enumeration of all rows in the extended
        set; 207/222 (−5 C-27, −5 C-34) if C-27 also fails when the block omits a non-standard
        term (cold-start) that has no canonical equivalent but appears in the obligation table
- V-03: 202/202 — inertia framing additions are prose-only and structurally neutral
- V-04: 222/222 if both Q1 and Q2 resolve positively; 217/222 (−5 C-33) if Q1 fails, Q2 passes;
        212/222 (−5 C-34) or 207/222 (−5 C-27, −5 C-34) if Q1 passes, Q2 fails; lower if both fail
- V-05: 202/202 — inline persona positioning satisfies C-16/C-19/C-24 pre-gate requirement; role
        sequence and register are structurally neutral

---

## V-01 — C-33 Alternate ARE Subject Form (Q1 Probe)

**Axis**: C-33 subject form — replaces "The flag column headers in the Stage 1 inventory table
ARE the Obligation Term column values above" with "Flag column headers ARE the Obligation Term
column values above" (drops the definite article "the" as subject determiner and drops the
"in the Stage 1 inventory table" positional qualifier; the ARE keyword and assertive collective
sentence form are preserved).

**Hypothesis**: C-33 requires the multi-subject collective ARE form — all flag column headers
subject to one identity constraint in a single assertion — not a specific lexical subject phrase.
"Flag column headers ARE the Obligation Term column values above" satisfies C-33 because it uses
ARE in a multi-subject assertive sentence; the subject "Flag column headers" is plural and
collective; the definite article and positional qualifier are incidental, not structural. If any
multi-subject ARE construction satisfies C-33, this scores 202/202 (canonical ceiling). If C-33
requires the exact phrase "the flag column headers," this scores 197/202 (−5 C-33; C-32 still
passes because uppercase ARE in an assertive declarative sentence is present regardless of subject
phrasing).

Canonical obligation terms (C-27 N/A). No YOU MUST NOT block needed.
ARE form under test: "Flag column headers ARE the Obligation Term column values above."

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

Flag column headers ARE the Obligation Term column values above — use those exact tokens as column
headers. A column header that does not match its row's Obligation Term fails schema alignment; the
mismatch is visible by comparing this table to the Stage 1 inventory column headers without
reading prose.

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

## V-02 — C-34 Extended Obligation Set, Substituted-Subset Enumeration (Q2 Probe)

**Axis**: C-34 enumeration completeness with a five-row obligation table — three non-standard
substitutions (OBL-1/2/3 replacing canonical terms), one canonical row kept (OBL-4), and one
new non-standard term with no canonical equivalent (OBL-5). The YOU MUST NOT block enumerates
only the three canonical tokens that were substituted (forgotten-call, assumed-to-work,
unknown-system) — it does not include delegation-chain (canonical, kept) or cold-start (new
term, no canonical equivalent to prohibit).

**Hypothesis**: C-34 applies per substituted canonical token — "each substituted canonical
token" in C-31 means every token where a canonical term was replaced by a non-standard
substitute. A row kept canonical (OBL-4: delegation-chain) was never substituted; its canonical
term is the correct term and must not appear in a YOU MUST NOT block. A new term with no
canonical equivalent (OBL-5: cold-start) has no canonical token to prohibit. The YOU MUST NOT
block is self-contained for the three substituted tokens: a reviewer reading only the block knows
exactly which canonical terms are forbidden, without cross-referencing the table. If the
per-substitution reading is correct, this scores 222/222. If C-34 requires the block to enumerate
all non-standard terms in the full extended set (including cold-start, which has no canonical
equivalent to prohibit), this scores 212/222 (−5 C-34). If C-27 also fails because the
prohibition surface is judged incomplete when a non-standard table term (cold-start) appears
nowhere in the YOU MUST NOT block, this scores 207/222 (−5 C-27, −5 C-34).

Non-standard terms: trace-call (sub for forgotten-call) / silent-pass (sub for assumed-to-work)
/ unverified-system (sub for unknown-system) / delegation-chain (CANONICAL, kept) /
cold-start (NEW — calls whose pre-warm or connection-reuse state is unknown at trace time;
no canonical equivalent in the standard four).
ARE form: "The flag column headers in the Stage 1 inventory table ARE the Obligation Term
column values above" (confirmed multi-subject form; not the axis under test).
YOU MUST NOT block: single block, enumerates forgotten-call + assumed-to-work + unknown-system
(three substituted canonical tokens); omits delegation-chain (canonical, not substituted) and
cold-start (new, no canonical equivalent).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term    | What to discover                                                                                                                              |
|-------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | trace-call         | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry posts |
| OBL-2 | silent-pass        | Calls the specification names but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment               |
| OBL-3 | unverified-system  | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                          |
| OBL-4 | delegation-chain   | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation            |
| OBL-5 | cold-start         | Calls where the connection reuse or pre-warm state is unknown at trace time — first-invocation behavior may differ materially from steady-state behavior |

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

| Gap ID | Call ID | Gap Type                                                                                              | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unverified-system / delegation-chain / cold-start | HIGH / MED / LOW |           |             |
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

---

## V-03 — Inertia Framing Prominence (Structural Neutrality Probe)

**Axis**: Inertia framing — an explicit status-quo displacement block is prepended before the
expert persona declaration, naming the default trace pattern (spec-walkthrough: take the call
list from the spec, document each call, produce a summary) as the approach this skill displaces
and explaining why the displacement is necessary. No schema instructions, obligation terms,
ARE directives, or format rules are changed; all additions are explanatory prose.

**Hypothesis**: Inertia framing additions are structurally neutral. No criterion rewards or
penalizes the presence of contrast prose that names and critiques the default approach. All
criteria target structural presence — a section exists, a table row is present, a directive
uses uppercase ARE, a gate is explicit — none of which are affected by surrounding prose that
frames the approach against a status-quo competitor. Expected: 202/202 (canonical ceiling).
Confirms inertia framing is a free variation axis and rules out contrast prose as a criterion
confound in either direction.

Canonical obligation terms (C-27 N/A). Confirmed ARE multi-subject form.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

The default integration trace takes the spec's call list, adds auth and format documentation
to each named call, and produces a summary. It finds the calls someone already thought of. It
documents the calls the author remembered to write down. It produces a surface-level record
of what was intended — not what will actually execute.

This trace exists because the default produces a false floor. The calls that cause production
incidents are not in the spec: the implicit token refresh that fires on credential expiry, the
SDK-internal connection health probe that bypasses the rate-limit envelope, the managed identity
chain that exchanges credentials three hops from where the spec says it authenticates, the
service whose identity has changed since the original design. None of these appear in a
spec-walkthrough trace. All of them appear in this one — if the discovery obligations are
applied before the inventory is closed.

The staged gate architecture below enforces the discipline that separates this trace from the
default: discovery before documentation; inventory before analysis; explicit completion
conditions before any stage advances. The persona declaration is not a preamble — it is the
discovery contract that governs what the Stage 1 inventory must contain.

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

## V-04 — Combined: C-33 Alternate ARE Subject + C-34 Extended Obligation Set (Q1+Q2 Joint Probe)

**Axis**: Combined — alternate ARE subject form without definite article (Q1 axis from V-01)
plus five-row extended obligation set with substituted-subset YOU MUST NOT enumeration (Q2 axis
from V-02).

**Hypothesis**: Both open questions resolve positively — "Flag column headers ARE the Obligation
Term column values above" satisfies C-33, and the substituted-subset YOU MUST NOT block
satisfies C-34 in the mixed five-row case. If both pass: 222/222. If only Q1 fails (alternate
ARE subject does not satisfy C-33): 217/222 (−5 C-33; C-32 still passes). If only Q2 fails
(substituted-subset insufficient): 217/222 (−5 C-34) or 212/222 (−5 C-27, −5 C-34) depending
on whether C-27 is also judged incomplete. If both fail: 212/222 (−5 C-33, −5 C-34) minimum,
lower if Q2 cascades to C-27.

Non-standard terms: trace-call / silent-pass / unverified-system / delegation-chain (canonical,
kept) / cold-start (new, no canonical equivalent).
ARE form under test: "Flag column headers ARE the Obligation Term column values above" (no
definite article, no "in the Stage 1 inventory table" qualifier).
YOU MUST NOT block: single block, enumerates forgotten-call + assumed-to-work + unknown-system
only (3 substituted canonical tokens; omits delegation-chain and cold-start).

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL   | Obligation Term    | What to discover                                                                                                                              |
|-------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | trace-call         | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry posts |
| OBL-2 | silent-pass        | Calls the specification names but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment               |
| OBL-3 | unverified-system  | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                          |
| OBL-4 | delegation-chain   | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation            |
| OBL-5 | cold-start         | Calls where the connection reuse or pre-warm state is unknown at trace time — first-invocation behavior may differ materially from steady-state behavior |

Flag column headers ARE the Obligation Term column values above — use those exact tokens as
column headers. A column header that does not match its row's Obligation Term fails schema
alignment; the mismatch is visible by comparing this table to the Stage 1 inventory column
headers without reading prose.

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

| Gap ID | Call ID | Gap Type                                                                                              | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unverified-system / delegation-chain / cold-start | HIGH / MED / LOW |           |             |
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

---

## V-05 — Combined: Role Sequence + Phrasing Register (Confirming Clean Sweep)

**Axis**: Combined — expert persona declaration is positioned inline within Stage 1 (after the
Stage 1 header, before the inventory gate instruction) rather than as a standalone pre-Stage-1
section; formal/technical phrasing register is used throughout (section headers use noun phrases
rather than imperative verbs; gate instructions use declarative rather than imperative form).

**Hypothesis**: (1) Inline persona positioning satisfies C-16 because C-16 requires the persona
to appear "before the inventory gate" — positioning within Stage 1 but prior to the gate
instruction satisfies this regardless of whether the persona has its own standalone section
header. C-19 and C-24 carry the same "before the inventory gate" requirement; inline positioning
satisfies both. (2) Formal/technical register variation is structurally neutral — no criterion is
phrasing-sensitive; all criteria target structural presence. Expected: 202/202 (canonical ceiling).
Confirms both role sequence (inline vs. standalone persona placement) and phrasing register as
free variation axes, and rules out section-header presence as a C-16/C-19/C-24 requirement.

Canonical obligation terms (C-27 N/A). Confirmed ARE multi-subject form
("The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values
above").

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**STAGE 1 — CALL INVENTORY**

**Expert Persona and Discovery Obligations**

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

All four discovery obligations are applied while building the inventory below.

**Inventory Gate**

The inventory table is populated before Stage 2 is opened. Every discovered call has a row
with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set
(Y or N; blank is not acceptable). Stage 2 does not open until this condition is met.

**Late-Call Rule**

When Stage 2 analysis reveals a call not present in the table below, a row with all four flag
cells set is added before that call's analysis block is opened.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| ...     |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

**Aggregation Rule**

Any cross-stage aggregation structure produced in this stage (fan-out registry, call-category
summary, cross-call rollup table) is: (1) populated FROM the per-call blocks — not the
authoritative source for any data it contains; (2) NOT required for trace assessment. Traces
with no cross-stage structures satisfy this rule by default.

Each CALL-[N] from the Stage 1 inventory is processed in order. CALL-[N+1] does not open
until the CALL-[N] COMPLETION GATE is fully checked.

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

**CALL-[N] COMPLETION GATE** — CALL-[N+1] does not open until all five rows are confirmed:

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | []   |
| Request/response documented  | []   |
| Rate limits documented       | []   |
| Retry/idempotency documented | []   |
| Error propagation documented | []   |

---

**STAGE 3 — GAP INVENTORY**

Every gap identified across all call blocks is listed below. Every finding carries a severity
label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings carry
a call-specific remediation sketch; generic advice does not satisfy.

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
