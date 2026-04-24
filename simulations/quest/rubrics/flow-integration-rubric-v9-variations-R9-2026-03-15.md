# flow-integration — R9 Variations (v9 rubric, 192 pt ceiling)

New criteria: C-26 (schema-only C-25 enforcement, 5 pts) + C-27 (dual-surface canonical-substitution prohibition, 5 pts) + C-28 (explicit terminal-position formula, 5 pts).
All R8 top variations scored 177/177. R9 target: 192/192.

R9 open questions under test:
- Q1: Does C-26 require the explicit "ARE" directive form ("the flag column headers ARE the Obligation Term column values above"), or does any unambiguous schema-aligned instruction satisfy it? R8 V-02 used the direct explicit ARE form. Minimum viable instruction is undefined.
- Q2: Does C-27 require all substituted canonical tokens named in a single YOU MUST NOT block, or does per-term prohibition (one YOU MUST NOT per canonical term, distributed across obligation table rows) achieve equivalent dual-surface coverage? R8 V-05 used a single comprehensive block. Per-term minimum is untested.

Axes selected:
- Single-axis: C-26 instruction minimum — cross-reference mapping table (V-01 / Q1 probe)
- Single-axis: C-27 prohibition scope — per-term distributed prohibition (V-02 / Q2 probe)
- Single-axis: outer frame vocabulary — numbered phases (V-03 / C-28 frame-agnosticism probe)
- Combined: C-26 cross-reference + C-27 per-term + non-standard terms (V-04 / Q1+Q2 joint probe)
- Combined: conversational register + role sequence split (V-05 / register-agnosticism probe)

Score predictions:
- V-01: 192/192 if cross-reference table satisfies C-26 minimum; 187/192 (−5 C-26) if explicit ARE is required
- V-02: 192/192 if per-term prohibition satisfies C-27; 187/192 (−5 C-27) if single comprehensive block is required
- V-03: 192/192 — phase-adapted C-28 formula is structurally identical; frame-agnosticism confirmed
- V-04: 192/192 if both cross-reference (C-26) and per-term (C-27) satisfy; 182/192 (−5/−5/−5) if one or both fail; ceiling under test
- V-05: 192/192 — conversational register changes no structural criterion; obligation table inside Stage 1 header still before inventory gate

---

## V-01 — Cross-Reference Schema Instruction (C-26 Instruction Minimum Probe)

**Axis**: C-26 instruction form — cross-reference mapping table instead of explicit ARE directive.

**Hypothesis**: A cross-reference table that maps each Obligation Term to its corresponding inventory column header name — with an explicit statement that each header must match its mapped term exactly and that mismatches are detectable by table comparison — satisfies C-26 without the explicit "ARE" formulation used in R8 V-02. Schema-aligned instruction is present (two-column mapping table with enforcement statement); the ARE keyword is omitted; the mechanism is identical. If C-26 requires the ARE keyword specifically, this variation scores 187/192 (−5 C-26). If any unambiguous schema-aligned instruction suffices, this scores 192/192.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation:

| OBL   | Obligation Term   | What to discover                                                                                                                    |
|-------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call    | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work   | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system    | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain  | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

COLUMN HEADER MAPPING — The Stage 1 inventory table includes one flag column per obligation category. Each inventory column header must match its corresponding Obligation Term in the mapping below exactly. A header that does not match its mapped term fails schema alignment; the mismatch is visible by comparing this table to the inventory column headers without reading prose.

| Obligation Term   | Inventory Column Header |
|-------------------|------------------------|
| forgotten-call    | forgotten-call         |
| assumed-to-work   | assumed-to-work        |
| unknown-system    | unknown-system         |
| delegation-chain  | delegation-chain       |

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N; blank is not acceptable).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| …       |               |           |                  |                  |                   |                  |                    |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure (fan-out registry, call-category summary, cross-call rollup table), that structure is: (1) populated FROM the per-call blocks — not the authoritative source for any data it contains; (2) NOT required for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field              | Value |
|--------------------|-------|
| Mechanism          |       |
| Credential source  |       |
| Token lifetime     |       |
| Refresh behavior   |       |
| Auth gap           |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field                | Value |
|----------------------|-------|
| Method               |       |
| Endpoint             |       |
| Request key fields   |       |
| Response key fields  |       |
| Encoding             |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field              | Value |
|--------------------|-------|
| Limit value        |       |
| Burst risk         |       |
| Throttle response  |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field                         | Value     |
|-------------------------------|-----------|
| Retry strategy                |           |
| Idempotent                    | Y / N     |
| Mitigation if non-idempotent  |           |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

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

List every gap identified across all call blocks. MEDIUM and LOW findings require a rationale entry. HIGH findings require a call-specific remediation sketch — generic advice does not satisfy.

| Gap ID | Call ID | Gap Type                                                                                        | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk        | HIGH / MED / LOW |           |             |
| …      |         |                                                                                                 |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures, write: "No cross-stage structures produced in this trace." It does not appear between any two numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property               | Value                                                   |
|------------------------|---------------------------------------------------------|
| Populated from         | Per-call blocks (Stage 2)                               |
| Authoritative source   | Per-call blocks — this structure is secondary           |
| Required for assessment| No                                                      |

---

## V-02 — Per-Term Distributed Prohibition (C-27 Prohibition Scope Probe)

**Axis**: C-27 prohibition scope — per-term YOU MUST NOT prohibition distributed inline across obligation table rows, not a single comprehensive block.

**Hypothesis**: One YOU MUST NOT prohibition per canonical term, placed in a dedicated column of the obligation table (one row per non-standard term, one canonical forbidden term per row), achieves equivalent dual-surface coverage to a single comprehensive block. Both surfaces remain present: schema alignment (C-25) detects substitution at the table surface by column header/row-term comparison; per-row prohibition blocks it at the prose and annotation surface by naming the specific forbidden canonical token in the same row as its non-standard replacement. If C-27 requires all canonical forbidden tokens in a single block, this variation scores 187/192 (−5 C-27). If per-term prohibition distributed across rows satisfies, this scores 192/192.

Non-standard obligation terms: shadow-call / taken-for-granted / fog-system / relay-chain.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation. Each row names the canonical term you MUST NOT substitute for the non-standard term in this trace:

| OBL   | Obligation Term      | What to discover                                                                                                                          | YOU MUST NOT substitute        |
|-------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| OBL-1 | shadow-call          | Calls that operate in the feature's behavior but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls | YOU MUST NOT use: forgotten-call  |
| OBL-2 | taken-for-granted    | Calls the specification lists but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit entry   | YOU MUST NOT use: assumed-to-work |
| OBL-3 | fog-system           | Calls whose target system identity, owner, or version cannot be confirmed from the available signal                                       | YOU MUST NOT use: unknown-system  |
| OBL-4 | relay-chain          | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or a proxy delegation hop  | YOU MUST NOT use: delegation-chain|

The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the inventory column headers without reading prose. The per-row YOU MUST NOT entries above prohibit substituting the named canonical token at the prose and annotation surface; both the table surface and the prose surface are covered.

Apply all four discovery obligations while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate this table before opening Stage 2.

**INVENTORY GATE: Stage 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N).**

NEW-CALL RULE: If Stage 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [shadow-call] | [taken-for-granted] | [fog-system] | [relay-chain] |
|---------|---------------|-----------|------------------|---------------|---------------------|--------------|---------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N         | Y / N               | Y / N        | Y / N         |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N         | Y / N               | Y / N        | Y / N         |
| …       |               |           |                  |               |                     |              |               |

---

**STAGE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this stage produces any cross-stage aggregation structure, that structure is: (1) populated FROM the per-call blocks — not the authoritative source; (2) NOT required for trace assessment. Traces with no cross-stage structures satisfy this rule by default.

For each CALL-[N] in the Stage 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field              | Value |
|--------------------|-------|
| Mechanism          |       |
| Credential source  |       |
| Token lifetime     |       |
| Refresh behavior   |       |
| Auth gap           |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field                | Value |
|----------------------|-------|
| Method               |       |
| Endpoint             |       |
| Request key fields   |       |
| Response key fields  |       |
| Encoding             |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field              | Value |
|--------------------|-------|
| Limit value        |       |
| Burst risk         |       |
| Throttle response  |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field                         | Value |
|-------------------------------|-------|
| Retry strategy                |       |
| Idempotent                    | Y / N |
| Mitigation if non-idempotent  |       |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

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

| Gap ID | Call ID | Gap Type                                                                                              | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | shadow-call / taken-for-granted / fog-system / relay-chain / auth-gap / rate-limit-gap / retry-gap / error-swallow | HIGH / MED / LOW |           |             |
| …      |         |                                                                                                       |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures, write: "No cross-stage structures produced in this trace." It does not appear between any two numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property               | Value                                                 |
|------------------------|-------------------------------------------------------|
| Populated from         | Per-call blocks (Stage 2)                             |
| Authoritative source   | Per-call blocks — this structure is secondary         |
| Required for assessment| No                                                    |

---

## V-03 — Numbered Phase Outer Frame (C-28 Frame-Agnosticism Probe)

**Axis**: Outer frame vocabulary — numbered phases (Phase 1 / Phase 2 / Phase 3) instead of numbered stages.

**Hypothesis**: The C-23/C-28 terminal-position formula is fully outer-frame-agnostic. Substituting "phase" for "stage" in both the coda header annotation and the prose sentence produces an identical structural guarantee. Neither C-23 nor C-28 cares whether the numbered outer frame is labeled with phases, stages, or sections — the unnumbered coda appended after the last numbered element satisfies both criteria identically in any frame vocabulary. Expected score: 192/192.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation:

| OBL   | Obligation Term   | What to discover                                                                                                                    |
|-------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call    | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work   | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system    | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain  | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the Phase 1 inventory table ARE the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its row's Obligation Term fails schema alignment; the mismatch is visible by comparing this table to the Phase 1 inventory column headers without reading prose.

Apply all four discovery obligations while building the Phase 1 inventory.

---

**PHASE 1 — CALL INVENTORY**

Populate this table before opening Phase 2.

**INVENTORY GATE: Phase 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N).**

NEW-CALL RULE: If Phase 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| …       |               |           |                  |                  |                   |                  |                    |

---

**PHASE 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this phase produces any cross-phase aggregation structure, that structure is: (1) populated FROM the per-call blocks — not the authoritative source; (2) NOT required for trace assessment. Traces with no cross-phase structures satisfy this rule by default.

For each CALL-[N] in the Phase 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field              | Value |
|--------------------|-------|
| Mechanism          |       |
| Credential source  |       |
| Token lifetime     |       |
| Refresh behavior   |       |
| Auth gap           |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field                | Value |
|----------------------|-------|
| Method               |       |
| Endpoint             |       |
| Request key fields   |       |
| Response key fields  |       |
| Encoding             |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field              | Value |
|--------------------|-------|
| Limit value        |       |
| Burst risk         |       |
| Throttle response  |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field                         | Value |
|-------------------------------|-------|
| Retry strategy                |       |
| Idempotent                    | Y / N |
| Mitigation if non-idempotent  |       |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

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

**PHASE 3 — GAP INVENTORY**

| Gap ID | Call ID | Gap Type                                                                                        | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk        | HIGH / MED / LOW |           |             |
| …      |         |                                                                                                 |                  |           |             |

---

**CROSS-PHASE AGGREGATION STRUCTURES** *(no phase number — appended after Phase 3, the last numbered phase)*

This coda fires unconditionally. If Phase 2 produced no cross-phase aggregation structures, write: "No cross-phase structures produced in this trace." It does not appear between any two numbered phases; it does not displace or renumber any existing element.

For any cross-phase structure produced in Phase 2:

| Property               | Value                                                 |
|------------------------|-------------------------------------------------------|
| Populated from         | Per-call blocks (Phase 2)                             |
| Authoritative source   | Per-call blocks — this structure is secondary         |
| Required for assessment| No                                                    |

---

## V-04 — C-26 Cross-Reference + C-27 Per-Term, Non-Standard Terms (Q1+Q2 Joint Probe)

**Axes combined**: C-26 instruction form (cross-reference table, not explicit ARE) + C-27 prohibition scope (per-term distributed prohibition, not single block) + non-standard obligation terms + section outer frame.

**Hypothesis**: Both open questions can be settled jointly. Non-standard terms (anchor-call, rubber-stamped, ghost-system, proxy-chain) enable C-27 probing. C-26 is probed via cross-reference table without ARE. C-27 is probed via per-term prohibition distributed in the obligation table rows. If both open questions resolve positively, this variation scores 192/192. If C-26 requires ARE, −5. If C-27 requires a single block, −5. Worst case: 182/192.

Non-standard obligation terms: anchor-call / rubber-stamped / ghost-system / proxy-chain.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row count; a missing row is a missing obligation. Each row names the canonical term you MUST NOT substitute:

| OBL   | Obligation Term  | What to discover                                                                                                                              | YOU MUST NOT substitute         |
|-------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| OBL-1 | anchor-call      | Calls explicitly named in the specification as entry points — these are the known surface; all other obligation rows find what these miss      | YOU MUST NOT use: forgotten-call    |
| OBL-2 | rubber-stamped   | Calls present in the specification but treated as documentation-free — missing retry strategy, auth detail, failure modes, or rate-limit entry  | YOU MUST NOT use: assumed-to-work   |
| OBL-3 | ghost-system     | Calls whose target system identity, owner, or version cannot be confirmed from the available signal                                           | YOU MUST NOT use: unknown-system    |
| OBL-4 | proxy-chain      | Calls made on behalf of the user through OBO exchange, managed identity, service principal impersonation, or any proxy delegation hop         | YOU MUST NOT use: delegation-chain  |

COLUMN HEADER MAPPING — The Section 1 inventory table includes one flag column per obligation category. Each column header must match its corresponding Obligation Term in the mapping below exactly. A header that does not match its mapped term fails schema alignment; the mismatch is visible by comparing this table to the inventory column headers without reading prose.

| Obligation Term  | Inventory Column Header |
|------------------|------------------------|
| anchor-call      | anchor-call            |
| rubber-stamped   | rubber-stamped         |
| ghost-system     | ghost-system           |
| proxy-chain      | proxy-chain            |

The per-row YOU MUST NOT entries above prohibit substituting the named canonical token at the prose and annotation surface; the column header mapping above prohibits substitution at the table schema surface. Both surfaces are covered.

Apply all four discovery obligations while building the Section 1 inventory.

---

**SECTION 1 — CALL INVENTORY**

Populate this table before opening Section 2.

**INVENTORY GATE: Section 2 does not open until the table is complete — every discovered call has a row with Call ID, Target System, Call Type, Confidence, and all four flag cells explicitly set (Y or N).**

NEW-CALL RULE: If Section 2 analysis reveals a call not already in this table, add a row with all four flag cells set before opening that call's analysis block.

| Call ID | Target System | Call Type | Confidence       | [anchor-call] | [rubber-stamped] | [ghost-system] | [proxy-chain] |
|---------|---------------|-----------|------------------|---------------|------------------|----------------|---------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N         | Y / N            | Y / N          | Y / N         |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N         | Y / N            | Y / N          | Y / N         |
| …       |               |           |                  |               |                  |                |               |

---

**SECTION 2 — PER-CALL ANALYSIS**

AGGREGATION RULE: If this section produces any cross-section aggregation structure, that structure is: (1) populated FROM the per-call blocks — not the authoritative source; (2) NOT required for trace assessment. Traces with no cross-section structures satisfy this rule by default.

For each CALL-[N] in the Section 1 inventory table, in order, produce the following block. Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*

| Field              | Value |
|--------------------|-------|
| Mechanism          |       |
| Credential source  |       |
| Token lifetime     |       |
| Refresh behavior   |       |
| Auth gap           |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(this section: format only — authentication, rate limits, retry/idempotency, and error propagation each have their own sections)*

| Field                | Value |
|----------------------|-------|
| Method               |       |
| Endpoint             |       |
| Request key fields   |       |
| Response key fields  |       |
| Encoding             |       |

**[N.3] RATE LIMITS** *(this section: rate limits only — authentication, format, retry/idempotency, and error propagation each have their own sections)*

| Field              | Value |
|--------------------|-------|
| Limit value        |       |
| Burst risk         |       |
| Throttle response  |       |

**[N.4] RETRY AND IDEMPOTENCY** *(this section: retry and idempotency only — authentication, format, rate limits, and error propagation each have their own sections)*

| Field                         | Value |
|-------------------------------|-------|
| Retry strategy                |       |
| Idempotent                    | Y / N |
| Mitigation if non-idempotent  |       |

**[N.5] ERROR PROPAGATION** *(this section: error propagation only — authentication, format, rate limits, and retry/idempotency each have their own sections)*

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

| Gap ID | Call ID | Gap Type                                                                                              | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | anchor-call / rubber-stamped / ghost-system / proxy-chain / auth-gap / rate-limit-gap / retry-gap / error-swallow | HIGH / MED / LOW |           |             |
| …      |         |                                                                                                       |                  |           |             |

---

**CROSS-SECTION AGGREGATION STRUCTURES** *(no section number — appended after Section 3, the last numbered section)*

This coda fires unconditionally. If Section 2 produced no cross-section aggregation structures, write: "No cross-section structures produced in this trace." It does not appear between any two numbered sections; it does not displace or renumber any existing element.

For any cross-section structure produced in Section 2:

| Property               | Value                                                   |
|------------------------|---------------------------------------------------------|
| Populated from         | Per-call blocks (Section 2)                             |
| Authoritative source   | Per-call blocks — this structure is secondary           |
| Required for assessment| No                                                      |

---

## V-05 — Conversational Register + Obligation Table Inside Stage 1 (Role Sequence Split)

**Axes combined**: Phrasing register (conversational imperative second-person) + role sequence (expert persona brief at top; obligation table co-located with Stage 1 inventory header, before the gate).

**Hypothesis**: (1) Conversational register — second-person imperative throughout, informal headers, natural-language gate statements — changes no structural criterion; all 28 criteria are satisfied by structure, not by formal header vocabulary. (2) Role sequence split — placing the obligation table inside the Stage 1 header (directly above the inventory table, before the gate statement) while keeping the expert persona brief at the document top still satisfies C-16 ("before the inventory gate") and C-24 ("appears before the inventory gate"). The obligation table is part of Stage 1 setup, not a pre-Stage-1 block, but it precedes the gate — that meets both criteria. Expected score: 192/192.

---

You are a connectors and backend integration domain expert. Your job is to trace every cross-system call this feature makes — the ones named in the spec and the ones that operate behind it.

Before you begin, establish your expert frame: you're looking for calls across four obligation lenses — calls absent from the spec, calls treated as documentation-free, calls to systems of unconfirmed identity, and calls that flow through delegation chains on behalf of the user. These four lenses are what separate a surface read from a complete trace.

---

**STAGE 1 — CALL INVENTORY**

Your first task is to build the complete call inventory. Start here and do not move to Stage 2 until it's done.

Set up your obligation tracking by declaring your four discovery obligations. One row per obligation — if a row is missing, the obligation is missing:

| OBL   | Obligation Term   | What to discover                                                                                                                    |
|-------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| OBL-1 | forgotten-call    | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work   | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment     |
| OBL-3 | unknown-system    | Calls whose target system identity, owner, or location cannot be confirmed from the available signal                                |
| OBL-4 | delegation-chain  | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |

The flag column headers in the inventory table below ARE the Obligation Term column values above — use those exact tokens as column headers. A column header that doesn't match its row's Obligation Term fails schema alignment; you can catch this by comparing the two tables directly without reading any surrounding prose.

Now build the inventory. Apply all four obligation lenses as you work through the feature signal. Every call you find goes in this table before Stage 2 opens:

| Call ID | Target System | Call Type | Confidence       | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------------|------------------|-------------------|------------------|--------------------|
| CALL-01 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| CALL-02 |               |           | HIGH / MED / LOW | Y / N            | Y / N             | Y / N            | Y / N              |
| …       |               |           |                  |                  |                   |                  |                    |

You may not open Stage 2 until every row has all four flag cells explicitly set to Y or N. A blank flag cell means the inventory isn't done.

One more rule before you continue: if Stage 2 turns up a call that isn't in this table yet, add it here with all four flags set before you open its analysis block.

---

**STAGE 2 — PER-CALL ANALYSIS**

Work through every call in the Stage 1 inventory, in order. For each call, cover all five concerns — auth, format, rate limits, retry/idempotency, and error propagation. Each concern gets its own labeled section; don't mix them.

One global note about aggregation structures: if you happen to produce any cross-stage summary table or fan-out registry during this stage, treat it as a secondary view only — it's populated from the per-call blocks and isn't required for the assessment. If you produce none, that's fine too.

For each CALL-[N], produce the following block. Don't move to CALL-[N+1] until the completion gate at the bottom is fully checked.

---

### CALL-[N]: [Target System] — [Call Type]

**[N.1] AUTHENTICATION** *(authentication only — the other four concerns each have their own section below)*

| Field              | Value |
|--------------------|-------|
| Mechanism          |       |
| Credential source  |       |
| Token lifetime     |       |
| Refresh behavior   |       |
| Auth gap           |       |

**[N.2] REQUEST AND RESPONSE FORMAT** *(format only — authentication, rate limits, retry/idempotency, and error propagation each have their own section)*

| Field                | Value |
|----------------------|-------|
| Method               |       |
| Endpoint             |       |
| Request key fields   |       |
| Response key fields  |       |
| Encoding             |       |

**[N.3] RATE LIMITS** *(rate limits only — authentication, format, retry/idempotency, and error propagation each have their own section)*

| Field              | Value |
|--------------------|-------|
| Limit value        |       |
| Burst risk         |       |
| Throttle response  |       |

**[N.4] RETRY AND IDEMPOTENCY** *(retry and idempotency only — authentication, format, rate limits, and error propagation each have their own section)*

| Field                         | Value |
|-------------------------------|-------|
| Retry strategy                |       |
| Idempotent                    | Y / N |
| Mitigation if non-idempotent  |       |

**[N.5] ERROR PROPAGATION** *(error propagation only — authentication, format, rate limits, and retry/idempotency each have their own section)*

| Field             | Value |
|-------------------|-------|
| Error disposition |       |
| Propagation path  |       |
| Swallowing risk   |       |

**Before moving to CALL-[N+1], confirm all five concerns are covered:**

| Concern                      | Done |
|------------------------------|------|
| Authentication documented    | ☐    |
| Request/response documented  | ☐    |
| Rate limits documented       | ☐    |
| Retry/idempotency documented | ☐    |
| Error propagation documented | ☐    |

---

**STAGE 3 — GAP INVENTORY**

Pull together every gap you found across all call blocks. Medium and low severity findings need a rationale — don't leave those cells blank. High findings need a specific-to-this-call fix — generic advice doesn't count.

| Gap ID | Call ID | Gap Type                                                                                        | Severity         | Rationale | Remediation |
|--------|---------|-------------------------------------------------------------------------------------------------|------------------|-----------|-------------|
| GAP-01 |         | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk        | HIGH / MED / LOW |           |             |
| …      |         |                                                                                                 |                  |           |             |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This section runs unconditionally. If Stage 2 produced no cross-stage aggregation structures, write: "No cross-stage structures produced in this trace." It does not appear between any two numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure that appeared in Stage 2:

| Property               | Value                                                 |
|------------------------|-------------------------------------------------------|
| Populated from         | Per-call blocks (Stage 2)                             |
| Authoritative source   | Per-call blocks — this structure is secondary         |
| Required for assessment| No                                                    |

---

## Variation Summary

| Variation | Axis / Axes | Open Question | Non-Standard Terms | C-26 Form | C-27 Form | Outer Frame | Predicted Score |
|-----------|-------------|---------------|--------------------|-----------|-----------|-------------|-----------------|
| V-01 | C-26 instruction minimum | Q1 | No | Cross-reference mapping table (no ARE) | N/A (canonical) | Numbered stages | 192/192 if cross-reference satisfies; 187/192 (−C-26) if ARE required |
| V-02 | C-27 prohibition scope | Q2 | Yes (shadow-call / taken-for-granted / fog-system / relay-chain) | Explicit ARE | Per-term inline in obligation table rows | Numbered stages | 192/192 if per-term satisfies; 187/192 (−C-27) if single block required |
| V-03 | Outer frame vocabulary | C-28 frame-agnosticism | No | Explicit ARE | N/A (canonical) | Numbered phases | 192/192 |
| V-04 | C-26 cross-reference + C-27 per-term | Q1 + Q2 joint | Yes (anchor-call / rubber-stamped / ghost-system / proxy-chain) | Cross-reference mapping table (no ARE) | Per-term inline in obligation table rows | Numbered sections | 192/192 if both open questions resolve; 182/192 worst case |
| V-05 | Conversational register + role sequence split | Register/sequence agnosticism | No | Explicit ARE (in conversational phrasing) | N/A (canonical) | Numbered stages | 192/192 |

### Structural Differentiators

**C-26 minimum (Q1):**
- V-01 and V-04 use a cross-reference mapping table: `| Obligation Term | Inventory Column Header |` with identical term/header pairs and an explicit statement that headers must match their mapped term. No "ARE" keyword. This is the R9 Q1 probe.
- V-02, V-03, V-05 use the explicit ARE form from R8 V-02: "The flag column headers ARE the Obligation Term column values above."

**C-27 scope (Q2):**
- V-02 and V-04 place one YOU MUST NOT prohibition per canonical term inline in the obligation table (one column: `YOU MUST NOT substitute`). Each row names one forbidden canonical token specific to its non-standard replacement. This is the R9 Q2 probe.
- V-05 does not probe C-27 (canonical terms used; C-27 passes trivially).

**C-28 frame adaptation:**
- V-01, V-02, V-04, V-05: stage frame → `*(no stage number — appended after Stage 3, the last numbered stage)*` + "does not appear between any two numbered stages"
- V-03: phase frame → `*(no phase number — appended after Phase 3, the last numbered phase)*` + "does not appear between any two numbered phases"
- V-04: section frame → `*(no section number — appended after Section 3, the last numbered section)*` + "does not appear between any two numbered sections"

**Role sequence (V-05):**
- Standard: Expert Persona Declaration (top-level block) → Obligation Table (within persona block) → Stage 1 inventory → Gate
- V-05: Expert persona brief sentence (top) → Stage 1 opens → Obligation table (first item inside Stage 1, before inventory table) → Inventory table → Gate
- The obligation table is inside Stage 1 but precedes the gate statement — satisfies C-16 (before gate) and C-24 (before gate)
