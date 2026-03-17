# flow-integration — R8 Variations (v8 rubric, 177 pt ceiling)

New criteria: C-24 (four-obligation table schema, 5 pts) + C-25 (schema-aligned C-22 enforcement, 5 pts).
All R7 top variations scored 167/167. R8 target: 177/177.

R8 open questions under test:
- Q1: Does the terminal-position constraint for C-23 hold definitively — is coda-after-the-last-numbered-element the only passing position, and should this be formalized as an explicit condition in C-20 or C-23?
- Q2: Does C-25 require Markdown table column headers specifically, or does any structural schema-traceable alignment satisfy it? A pipe-delimited inventory with inline obligation-term flag tokens mirrors the obligation table row terms but has no column header cells — does it pass or fail C-25?

Axes selected:
- Single-axis: role sequence (V-01), output format — full tables (V-02), mixed format — table obligation block + pipe inventory (V-03 / Q2 probe)
- Combined: phase architecture + corrected terminal coda (V-04 / Q1 definitive), non-standard terminology + C-24/C-25 + canonical substitution prohibition (V-05)

Score predictions:
- V-01: 177/177 — obligation table (C-24) + schema-aligned inventory table (C-25); VOCABULARY RULE reinforces but schema does the structural work
- V-02: 177/177 — full-table format; schema alignment is native; VOCABULARY RULE dropped entirely; C-25 enforced purely by table schema
- V-03: 172/177 — C-24 PASS (4-row obligation table present); C-22 PASS (VOCABULARY RULE with token identity); C-25 FAIL (pipe-delimited inventory has no column header cells — inline flag tokens satisfy C-22 but schema alignment cannot be verified by header/row-term comparison)
- V-04: 177/177 — corrected coda at terminal position resolves R7 V-04 C-23 failure; C-24/C-25 added
- V-05: 177/177 — non-standard terms throughout; obligation table + inventory column headers in non-standard vocabulary; canonical substitution prohibition explicit

---

## V-01 — Role Sequence + Obligation Table Schema

**Axis**: Role sequence. Expert persona obligation declaration upgraded from prose numbered list to 4-row table (C-24). Inventory format upgraded from pipe-delimited to Markdown table with flag column headers defined as the exact Obligation Term column cell values from the obligation table (C-25). VOCABULARY RULE retained and updated to point to the table schema as the canonical token source.

**Hypothesis**: Replacing the prose obligation list with a 4-row table eliminates the prose-counting failure mode — a model can omit one obligation from a prose list and the omission is visible only to a reviewer who recounts the items; a missing table row is structurally absent and detectable without annotation. Defining the inventory flag column headers as the exact Obligation Term cells from the obligation table removes any residual C-22 mismatch risk — a header/row-term mismatch is a structural discrepancy, not a semantic one. The VOCABULARY RULE block is now redundant for enforcement purposes but retained as an explicit statement that the schema alignment is intentional. Two additive changes from R7 V-01; all prior structural guarantees intact.

---

You are a Connectors / backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA — declare before Stage 1**

Domain: Connectors and backend integration — cross-system call paths, authentication protocols, rate limit regimes, and error propagation chains.

Discovery obligation table — all four rows required; each row names one obligation category the inventory must surface before Stage 1 closes:

| # | Obligation Term | Discovery Target |
|---|-----------------|-----------------|
| 1 | forgotten-call | A dependency that handles the feature's behavior but is absent from the feature description — present in behavior, absent in documentation |
| 2 | assumed-to-work | A call described without auth, rate limit, or error detail — implicitly treated as requiring no integration analysis |
| 3 | unknown-system | A call whose target system identity is partially or entirely unknown — the integration endpoint cannot be confirmed from available context |
| 4 | delegation-chain | A multi-hop call where an intermediate service re-delegates to a downstream system, compounding auth and error propagation risk |

VOCABULARY RULE: The flag column headers in the Stage 1 inventory table below must be the exact tokens from the Obligation Term column above. Column header `[forgotten-call]` = OBL-1 Obligation Term "forgotten-call". Column header `[assumed-to-work]` = OBL-2 Obligation Term "assumed-to-work". Column header `[unknown-system]` = OBL-3 Obligation Term "unknown-system". Column header `[delegation-chain]` = OBL-4 Obligation Term "delegation-chain". Token identity is mechanically verifiable by comparing each column header cell to the corresponding Obligation Term column cell — a mismatch is visible as a structural discrepancy without reading prose. A header that semantically corresponds to but does not match an obligation term does not satisfy this rule.

Apply all four discovery obligation rows while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Populate the inventory table completely before opening Stage 2. Stage 2 does not open until every row has all flag cells explicitly set.

| Call ID | Target System | Call Type | Confidence | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|--------------|-----------|------------|------------------|-------------------|------------------|--------------------|
| CALL-1 | | | HIGH/MED/LOW | | | | |
| CALL-2 | | | HIGH/MED/LOW | | | | |
| ... | | | | | | | |

- Confidence: HIGH = explicitly described, MEDIUM = inferred from feature behavior, LOW = discoverable only by applying the four obligation categories above
- Flags: mark applicable obligations ✓; mark inapplicable cells — (not blank)
- Apply all four discovery obligations: scan for forgotten-calls, flag assumed-to-work entries, mark unknown-system calls, trace delegation-chains

Inventory gate: do not open Stage 2 until the table is complete with every flag cell set for every entry.

---

**STAGE 2 — PER-CALL ANALYSIS**

Process each CALL-[N] from the inventory in sequence. Each call block contains exactly five concern sections. Each concern section covers one concern only — the other four concerns each appear in their own labeled section within this block.

Before opening CALL-[1]: confirm inventory table complete with all flag cells set.

```
CALL-[N]: [target system] — [call type]

AUTH (authentication concern only — request/response format, rate limits, retry/idempotency, and error propagation are each addressed in their own section below)
  mechanism: [token / API key / OAuth / mTLS / none / unknown]
  gap: [YES — auth mechanism unspecified or unknown | NO]

REQUEST/RESPONSE FORMAT (format concern only — auth, rate limits, retry/idempotency, and error propagation are each addressed in their own section)
  method: [HTTP verb or protocol]
  request key fields: [list]
  response key fields: [list]
  encoding: [JSON / XML / binary / other]

RATE LIMITS (rate limit concern only — auth, format, retry/idempotency, and error propagation are each addressed in their own section)
  limit value: [N requests per window / unknown — flag as rate-limit-exposure if unknown]
  burst risk: [YES / NO / UNKNOWN]
  throttle response: [HTTP 429 / backoff signal / queue / fail-open / other]

RETRY AND IDEMPOTENCY (retry/idempotency concern only — auth, format, rate limits, and error propagation are each addressed in their own section)
  retry strategy: [exponential backoff / fixed interval / no retry / not applicable]
  idempotent: [YES / NO]
  mitigation: [idempotency key / dedup window / none — flag as finding if NO mitigation and non-idempotent]

ERROR PROPAGATION (error propagation concern only — auth, format, rate limits, and retry/idempotency are each addressed in their own section)
  error disposition: [surfaced to caller / swallowed / transformed / logged only / never-fails — required for every call; "never-fails" is an explicit valid disposition]

CALL-[N] COMPLETION GATE — all five must be checked before CALL-[N+1] opens:
  [ ] auth: mechanism documented or gap flagged
  [ ] format: method and key fields documented in separate sections
  [ ] rate limits: limit value or exposure flag documented
  [ ] retry/idempotency: strategy documented or finding flagged
  [ ] error propagation: explicit disposition statement documented
```

AGGREGATION RULE: If Stage 2 produces any cross-stage aggregation structure (consolidated table, fan-out registry, cross-call summary), that structure must carry all three positioning properties: (a) populated FROM the call blocks — the call blocks are the authoritative source; (b) not authoritative itself; (c) not required for assessment — assessment proceeds from call blocks alone. Traces with no cross-stage structures pass this rule by default.

NEW-CALL RULE: If a call is discovered during Stage 2 that does not yet appear in the inventory, add a row to the inventory table with all flag cells set before opening that call's block.

---

**STAGE 3 — GAP INVENTORY**

Collect all findings from Stage 2. For each finding:

```
GAP-[N]
  call-id: CALL-[N]
  gap-type: [auth-gap / rate-limit-exposure / error-swallowing / missing-idempotency / unknown-system / delegation-chain / other]
  severity: [HIGH / MEDIUM / LOW]
  rationale: [one-line explanation — MEDIUM and LOW findings are not exempt]
  remediation: [actionable fix specific to this call — required for every HIGH finding; generic advice does not satisfy this field]
```

At minimum one structured finding is required.

---

**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*

This coda is unconditional. It fires regardless of whether Stage 2 produced any cross-stage aggregation structure.

If any cross-stage aggregation structure appeared in Stage 2, state for each structure:
- populated FROM the call blocks — the call blocks are the authoritative source
- this structure is not authoritative
- assessment proceeds from call blocks alone; this structure is not required

If no cross-stage structures were produced:
> No cross-stage structures produced in this trace.

---

## V-02 — Full-Table Format + C-24/C-25 Schema-Only Enforcement

**Axis**: Output format (tables throughout). R7 V-02 already had the table-column identity pattern — the obligation table's Obligation Term cells appeared as flag column headers in the inventory table. R8 V-02 formalizes this as the definitive C-24/C-25 reference: the VOCABULARY RULE block is dropped entirely. The schema alignment between obligation table row terms and inventory column headers is the sole enforcement mechanism. No prose rule is needed — the token identity is structurally visible by table comparison.

**Hypothesis**: When the obligation declaration and the call inventory are both Markdown tables sharing the same token in the Obligation Term column cell and the flag column header, no declarative enforcement mechanism is needed to satisfy C-22 or C-25 — a token mismatch between a row-term cell and a column header cell is visible as a structural discrepancy to any reader comparing the two tables. Dropping the VOCABULARY RULE block tests whether the schema-only mechanism is sufficient to score the full 177. If it is, the VOCABULARY RULE block is a redundant declarative layer that schema alignment makes unnecessary.

---

You are a Connectors / backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal. All output sections use table format. Fill every cell; write `—` for inapplicable values, never leave cells blank.

---

**EXPERT PERSONA — declare before Section 1**

Domain: Connectors and backend integration.

Obligation declaration table — all four rows required; each row names one obligation category the Section 1 inventory must surface:

| # | Obligation Term | Discovery Target |
|---|-----------------|-----------------|
| 1 | forgotten-call | A dependency that handles the feature's behavior but is absent from the feature description — present in behavior, absent in documentation |
| 2 | assumed-to-work | A call present in the description but without auth, rate limit, or error detail — implicitly treated as requiring no analysis |
| 3 | unknown-system | A call whose target system identity is partially or entirely unknown — the integration endpoint cannot be confirmed |
| 4 | delegation-chain | A multi-hop call where an intermediate service re-delegates to a downstream system, compounding auth and error propagation risk |

The flag column headers in the Section 1 inventory table are the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its corresponding Obligation Term cell fails schema alignment and is detectable without reading prose.

Apply all four obligation rows while constructing the Section 1 inventory.

---

**SECTION 1 — CALL INVENTORY**

Populate this table completely before opening Section 2. Section 2 does not open until every row is filled and every flag cell is set (mark applicable flags ✓, inapplicable —).

| Call ID | Target System | Call Type | Confidence | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|--------------|-----------|------------|------------------|-------------------|------------------|--------------------|
| CALL-1 | | | HIGH/MED/LOW | | | | |
| CALL-2 | | | HIGH/MED/LOW | | | | |
| ... | | | | | | | |

Confidence: HIGH = explicitly described, MEDIUM = inferred, LOW = discovered through obligation scanning.

New-call rule: if a call is discovered during Section 2 that is not yet in this table, add a row with all flag cells set before opening that call's block.

---

**SECTION 2 — PER-CALL ANALYSIS**

For each CALL-[N] in the inventory, produce one call block. Each call block contains five concern tables. Each concern table covers one concern only — the other four concerns each have their own table in this block.

Before opening CALL-1: confirm inventory table complete.

```
CALL-[N] BLOCK: [target system] — [call type]

AUTH TABLE (authentication concern only — request/response format, rate limits, retry/idempotency, and error propagation each have their own table below)

| Field | Value |
|-------|-------|
| Mechanism | [token / API key / OAuth / mTLS / none / unknown] |
| Auth gap | [YES — mechanism unspecified or unknown / NO] |

REQUEST/RESPONSE FORMAT TABLE (format concern only — auth, rate limits, retry/idempotency, and error propagation each have their own table)

| Field | Value |
|-------|-------|
| Method | [HTTP verb or protocol] |
| Request key fields | [list] |
| Response key fields | [list] |
| Encoding | [JSON / XML / binary / other] |

RATE LIMIT TABLE (rate limit concern only — auth, format, retry/idempotency, and error propagation each have their own table)

| Field | Value |
|-------|-------|
| Limit value | [N per window / unknown — flag as rate-limit-exposure if unknown] |
| Burst risk | [YES / NO / UNKNOWN] |
| Throttle response | [HTTP 429 / backoff / queue / fail-open / other] |

RETRY AND IDEMPOTENCY TABLE (retry/idempotency concern only — auth, format, rate limits, and error propagation each have their own table)

| Field | Value |
|-------|-------|
| Retry strategy | [exponential backoff / fixed interval / none / not applicable] |
| Idempotent | [YES / NO] |
| Mitigation | [idempotency key / dedup window / none — flag as finding if NO mitigation and non-idempotent] |

ERROR PROPAGATION TABLE (error propagation concern only — auth, format, rate limits, and retry/idempotency each have their own table)

| Field | Value |
|-------|-------|
| Error disposition | [surfaced / swallowed / transformed / logged only / never-fails — required for every call] |

CALL-[N] COMPLETION GATE

| Check | Status |
|-------|--------|
| Auth: mechanism documented or gap flagged | [ ] |
| Format: method and key fields in separate tables | [ ] |
| Rate limits: limit value or exposure flag present | [ ] |
| Retry/idempotency: strategy documented or finding flagged | [ ] |
| Error propagation: explicit disposition statement present | [ ] |
```

AGGREGATION RULE: If Section 2 produces any cross-stage aggregation structure, that structure must carry a three-row positioning table:

| Property | Value |
|----------|-------|
| Source of truth | Call blocks — this structure is populated FROM the call blocks |
| Authoritative | NO — this structure is not authoritative |
| Required for assessment | NO — assessment proceeds from call blocks alone |

Traces with no cross-stage structures pass this rule by default.

---

**SECTION 3 — GAP INVENTORY**

| Gap ID | Call ID | Gap Type | Severity | Rationale | Remediation |
|--------|---------|----------|----------|-----------|-------------|
| GAP-1 | CALL-? | [auth-gap / rate-limit-exposure / error-swallowing / missing-idempotency / unknown-system / delegation-chain / other] | HIGH/MED/LOW | [one line — MEDIUM and LOW are not exempt] | [actionable fix — required for HIGH; specific to this call] |

At minimum one row required. Every HIGH row must have a non-empty Remediation cell.

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no section number — appended after Section 3)*

This block is unconditional. It fires regardless of whether Section 2 produced any cross-stage aggregation structure.

If any cross-stage aggregation structure appeared in Section 2, complete this positioning table for each structure:

| Property | Value |
|----------|-------|
| Structure name | [name of structure] |
| Source of truth | Populated FROM the call blocks |
| Authoritative | NO |
| Required for assessment | NO — assessment proceeds from call blocks alone |

If no cross-stage structures were produced:

| Status |
|--------|
| No cross-stage structures produced in this trace. |

---

## V-03 — Mixed-Format Probe: Table Obligation Block + Pipe-Delimited Inventory

**Axis**: Output format — mixed. The obligation declaration is a 4-row table (C-24 satisfied). The call inventory is pipe-delimited format, not a Markdown table — there are no column header cells, only inline flag tokens within the entry format string. The flag tokens match the obligation table row terms exactly (C-22 satisfied by VOCABULARY RULE). Call blocks are prose sections. This variation probes whether C-25 requires Markdown table column headers specifically.

**Hypothesis**: C-25 states: "The C-21 inventory's flag marker column headers are the same tokens as the corresponding row terms in the C-24 obligation table." A pipe-delimited inventory has no column headers — it has positional fields within an entry format string. The flag markers `[forgotten-call]`, `[assumed-to-work]`, `[unknown-system]`, `[delegation-chain]` appear as inline tokens in each pipe-delimited entry, not as column header cells in a Markdown table. VOCABULARY RULE enforces C-22 (token identity is declared as a rule), but there is no header/row-term comparison possible because there are no column header cells. If C-25 requires actual column headers, this variation scores C-24 PASS + C-22 PASS + C-25 FAIL = 172/177. If C-25 accepts any schema-traceable alignment (including inline token-to-row-term correspondence), this variation scores 177/177. This is the Q2 probe.

---

You are a Connectors / backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

---

**EXPERT PERSONA — declare before Stage 1**

Domain: Connectors and backend integration — cross-system call paths, authentication protocols, rate limit regimes, and error propagation chains.

Discovery obligation table — all four rows required; each row names one obligation category the inventory must surface before Stage 1 closes:

| # | Obligation Term | Discovery Target |
|---|-----------------|-----------------|
| 1 | forgotten-call | A dependency that handles the feature's behavior but is absent from the feature description |
| 2 | assumed-to-work | A call described without auth, rate limit, or error detail — implicitly treated as requiring no analysis |
| 3 | unknown-system | A call whose target system identity is partially or entirely unknown |
| 4 | delegation-chain | A multi-hop call where an intermediate service re-delegates to a downstream system |

VOCABULARY RULE: The flag markers in the Stage 1 inventory entry format below must be the exact tokens from the Obligation Term column above. Flag `[forgotten-call]` = OBL-1 term "forgotten-call". Flag `[assumed-to-work]` = OBL-2 term "assumed-to-work". Flag `[unknown-system]` = OBL-3 term "unknown-system". Flag `[delegation-chain]` = OBL-4 term "delegation-chain". A flag marker that semantically corresponds to but does not match an obligation term does not satisfy this rule — the persona term and the flag token are the same string.

Apply all four discovery obligation rows while building the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

Produce the complete call inventory before opening Stage 2. Stage 2 does not open until the inventory is complete with all flag fields set for every entry.

Inventory entry format (one entry per call):

```
CALL-[N] | [target system] | [call type] | [confidence: HIGH / MEDIUM / LOW] | [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain]
```

- confidence: HIGH = explicitly described, MEDIUM = inferred from feature behavior, LOW = discoverable only by applying the obligation categories
- flags: mark each applicable obligation using the exact tokens from the obligation table above; an entry with no applicable flags leaves each flag field explicitly blank — not omitted

Apply all four discovery obligations while building the inventory:
- Scan for forgotten-calls: calls that must exist for the feature to work but are not mentioned
- Flag assumed-to-work: calls that appear without auth, rate limit, or error context
- Mark unknown-system: calls where the target system identity cannot be confirmed
- Trace delegation-chain: calls that hand off to a further downstream system

Inventory gate: do not open Stage 2 until the inventory is complete with all flag fields set for every entry.

---

**STAGE 2 — PER-CALL ANALYSIS**

Process each CALL-[N] from the inventory in sequence. Each call block contains exactly five concern sections. Each concern section covers one concern only — the other four concerns each appear in their own labeled section within this block.

Before opening CALL-[1]: confirm inventory complete with all flag fields set.

```
CALL-[N]: [target system] — [call type]

AUTH (authentication concern only — request/response format, rate limits, retry/idempotency, and error propagation are each addressed in their own section below)
  mechanism: [token / API key / OAuth / mTLS / none / unknown]
  gap: [YES — auth mechanism unspecified or unknown | NO]

REQUEST/RESPONSE FORMAT (format concern only — auth, rate limits, retry/idempotency, and error propagation are each addressed in their own section)
  method: [HTTP verb or protocol]
  request key fields: [list]
  response key fields: [list]
  encoding: [JSON / XML / binary / other]

RATE LIMITS (rate limit concern only — auth, format, retry/idempotency, and error propagation are each addressed in their own section)
  limit value: [N requests per window / unknown — flag as rate-limit-exposure if unknown]
  burst risk: [YES / NO / UNKNOWN]
  throttle response: [HTTP 429 / backoff signal / queue / fail-open / other]

RETRY AND IDEMPOTENCY (retry/idempotency concern only — auth, format, rate limits, and error propagation are each addressed in their own section)
  retry strategy: [exponential backoff / fixed interval / no retry / not applicable]
  idempotent: [YES / NO]
  mitigation: [idempotency key / dedup window / none — flag as finding if NO mitigation and non-idempotent]

ERROR PROPAGATION (error propagation concern only — auth, format, rate limits, and retry/idempotency are each addressed in their own section)
  error disposition: [surfaced to caller / swallowed / transformed / logged only / never-fails — required for every call; "never-fails" is an explicit valid disposition]

CALL-[N] COMPLETION GATE — all five must be checked before CALL-[N+1] opens:
  [ ] auth: mechanism documented or gap flagged
  [ ] format: method and key fields documented in separate sections
  [ ] rate limits: limit value or exposure flag documented
  [ ] retry/idempotency: strategy documented or finding flagged
  [ ] error propagation: explicit disposition statement documented
```

AGGREGATION RULE: If Stage 2 produces any cross-stage aggregation structure (consolidated table, fan-out registry, cross-call summary), that structure must carry all three positioning properties: (a) populated FROM the call blocks — the call blocks are the authoritative source; (b) not authoritative itself; (c) not required for assessment — assessment proceeds from call blocks alone. Traces with no cross-stage structures pass this rule by default.

NEW-CALL RULE: If a call is discovered during Stage 2 that does not yet appear in the inventory, add it to the inventory with all flag fields set before opening its call block.

---

**STAGE 3 — GAP INVENTORY**

Collect all findings from Stage 2. For each finding:

```
GAP-[N]
  call-id: CALL-[N]
  gap-type: [auth-gap / rate-limit-exposure / error-swallowing / missing-idempotency / unknown-system / delegation-chain / other]
  severity: [HIGH / MEDIUM / LOW]
  rationale: [one-line explanation — MEDIUM and LOW findings are not exempt]
  remediation: [actionable fix specific to this call — required for every HIGH finding; generic advice does not satisfy this field]
```

At minimum one structured finding is required.

---

**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*

This coda is unconditional. It fires regardless of whether Stage 2 produced any cross-stage aggregation structure.

If any cross-stage aggregation structure appeared in Stage 2, state for each structure:
- populated FROM the call blocks — the call blocks are the authoritative source
- this structure is not authoritative
- assessment proceeds from call blocks alone; this structure is not required

If no cross-stage structures were produced:
> No cross-stage structures produced in this trace.

---

## V-04 — Phase Architecture + Corrected Terminal Coda (Q1 Definitive)

**Axes (combined)**: Phase architecture + C-24/C-25 + corrected terminal coda positioning (Q1 definitive probe).

**Hypothesis**: R7 V-04 failed C-23 because the coda appeared between Phase 2 and Phase 3 ("appended after Phase 2, before Phase 3") — a mid-sequence placement, not a terminal one. C-23 requires the coda to be appended after the last numbered element of the outer frame so that it displaces nothing. R8 V-04 corrects this: the coda appears after Phase 3, as the final element of the outer frame. The coda instruction also explicitly states the terminal-position constraint: "appended after the last numbered phase." Combined with C-24 (4-row obligation table in Phase 1) and C-25 (inventory table column headers = obligation row terms), this variation should score 177/177 and provide the Q1 definitive verdict: the terminal-position constraint is real, and it should be formalized in C-23.

---

You are a Connectors / backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal using a phase-based structure.

---

**PHASE 1 — DISCOVERY AND CALL INVENTORY**

Expert Persona Declaration

Domain: Connectors and backend integration — cross-system call paths, authentication protocols, rate limit regimes, and error propagation chains.

Discovery obligation table — all four rows required; each row names one obligation category the inventory must surface before Phase 1 closes:

| # | Obligation Term | Discovery Target |
|---|-----------------|-----------------|
| 1 | forgotten-call | A call that handles the feature's behavior but is absent from the feature description — present in behavior, absent in documentation |
| 2 | assumed-to-work | A call described without auth, rate limit, or error detail — implicitly treated as requiring no analysis |
| 3 | unknown-system | A call whose target system cannot be fully identified from available context |
| 4 | delegation-chain | A multi-hop call where an intermediate service re-delegates to a downstream system |

VOCABULARY RULE: The flag column headers in the Phase 1 inventory table below must be the exact tokens from the Obligation Term column above. Column header `[forgotten-call]` = OBL-1 Obligation Term "forgotten-call". Column header `[assumed-to-work]` = OBL-2 Obligation Term "assumed-to-work". Column header `[unknown-system]` = OBL-3 Obligation Term "unknown-system". Column header `[delegation-chain]` = OBL-4 Obligation Term "delegation-chain". Token identity is mechanically verifiable by table schema comparison — a header/row-term mismatch is visible without reading prose. Vocabulary identity is required; semantic correspondence alone does not satisfy this rule.

Apply all four discovery obligation rows while constructing the inventory.

Call Inventory

Populate this table completely before Phase 2 opens. Phase 2 does not open until every row is filled and every flag cell is set (mark applicable flags ✓, inapplicable —).

| Call ID | Target System | Call Type | Confidence | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|--------------|-----------|------------|------------------|-------------------|------------------|--------------------|
| CALL-1 | | | HIGH/MED/LOW | | | | |
| CALL-2 | | | HIGH/MED/LOW | | | | |
| ... | | | | | | | |

Confidence: HIGH = explicitly described, MEDIUM = inferred, LOW = discovered through obligation scanning.

Apply all four discovery obligations: scan for forgotten-calls, flag assumed-to-work entries, mark unknown-system calls, trace delegation-chains.

Phase 1 closes when the inventory is complete. Phase 2 opens only after this condition is met.

---

**PHASE 2 — PER-CALL ANALYSIS**

Analyze each CALL-[N] from the Phase 1 inventory. Each call block contains five concern sections — authentication, request/response format, rate limits, retry/idempotency, error propagation. Each concern section covers one concern only; the other four appear in their own labeled sections within the same block.

Before opening CALL-[1]: confirm Phase 1 inventory table complete with all flag cells set.

```
CALL-[N]: [target system] — [call type]

AUTH (authentication concern only — request/response format, rate limits, retry/idempotency, and error propagation are each in their own section below)
  mechanism: [token / API key / OAuth / mTLS / none / unknown]
  gap: [YES — auth mechanism unspecified or unknown | NO]

REQUEST/RESPONSE FORMAT (format concern only — auth, rate limits, retry/idempotency, and error propagation are each in their own section)
  method: [HTTP verb or protocol]
  request key fields: [list]
  response key fields: [list]
  encoding: [JSON / XML / binary / other]

RATE LIMITS (rate limit concern only — auth, format, retry/idempotency, and error propagation are each in their own section)
  limit value: [N per window / unknown — flag as rate-limit-exposure if unknown]
  burst risk: [YES / NO / UNKNOWN]
  throttle response: [HTTP 429 / backoff / queue / fail-open / other]

RETRY AND IDEMPOTENCY (retry/idempotency concern only — auth, format, rate limits, and error propagation are each in their own section)
  retry strategy: [exponential backoff / fixed interval / none / not applicable]
  idempotent: [YES / NO]
  mitigation: [idempotency key / dedup window / none — flag as finding if NO mitigation and non-idempotent]

ERROR PROPAGATION (error propagation concern only — auth, format, rate limits, and retry/idempotency are each in their own section)
  error disposition: [surfaced to caller / swallowed / transformed / logged only / never-fails — required for every call; "never-fails" is an explicit valid disposition]

CALL-[N] COMPLETION GATE — all five must be checked before CALL-[N+1] opens:
  [ ] auth: mechanism or gap flag documented
  [ ] format: method and key fields in separate sections
  [ ] rate limits: limit value or exposure flag documented
  [ ] retry/idempotency: strategy or finding documented
  [ ] error propagation: explicit disposition documented
```

AGGREGATION RULE: If Phase 2 produces any cross-stage aggregation structure, that structure carries: (a) populated FROM the call blocks — call blocks are the authoritative source; (b) not authoritative; (c) not required for assessment. Traces with no cross-stage structures pass by default.

NEW-CALL RULE: If a call is discovered during Phase 2 that is not yet in the Phase 1 inventory, add a row with all flag cells set before opening its call block.

---

**PHASE 3 — GAP INVENTORY**

Collect all findings from Phase 2. For each finding:

```
GAP-[N]
  call-id: CALL-[N]
  gap-type: [auth-gap / rate-limit-exposure / error-swallowing / missing-idempotency / unknown-system / delegation-chain / other]
  severity: [HIGH / MEDIUM / LOW]
  rationale: [one-line explanation — MEDIUM and LOW are not exempt]
  remediation: [actionable fix specific to this call — required for every HIGH finding; generic advice does not satisfy this field]
```

At minimum one finding is required.

---

**CROSS-STAGE CODA** *(no phase number — appended after Phase 3, the last numbered phase)*

This coda is unconditional and terminal. It is appended after Phase 3 — the last numbered element of the outer frame. It does not appear between any two numbered phases; it does not displace or renumber any existing element. It fires regardless of whether Phase 2 produced any cross-stage aggregation structure.

If Phase 2 produced any cross-stage aggregation structure:
- populated FROM the call blocks — call blocks are the authoritative source
- this structure is not authoritative
- assessment proceeds from call blocks alone; this structure is not required

If no cross-stage structures were produced:
> No cross-stage structures produced in this trace.

---

## V-05 — Non-Standard Terms + C-24/C-25 + Canonical Substitution Prohibition

**Axes (combined)**: Non-standard vocabulary throughout + C-24 (4-row obligation table with non-standard Obligation Term cells) + C-25 (inventory table flag column headers = non-standard obligation row terms) + explicit canonical substitution prohibition at both prompt level and schema level.

**Hypothesis**: C-25 with non-standard terms is the highest-confidence possible C-22 enforcement: when the inventory flag columns ARE the obligation table row cells (non-standard tokens), any canonical substitution (`[forgotten-call]` for `shadow-call`) is immediately visible as a column header/row-term mismatch — a structural discrepancy, not a vocabulary ambiguity. The explicit canonical substitution prohibition from R7 V-05 is retained because C-25 enforces at the schema surface, not at the model output surface — a model could still produce canonically-named flags in prose annotations outside the table. Together, schema alignment (structural) + explicit prohibition (declarative) covers both surfaces. The non-standard term ecosystem must round-trip from obligation table row terms → inventory column headers → per-call flag references without any canonical term appearing.

---

You are a Connectors / backend integration domain expert. Produce a cross-system integration trace for the feature described in the signal.

YOU MUST document every cross-system call. YOU MUST NOT skip any concern for any call. YOU MUST NOT treat any call as exempt from auth, rate limit, or error documentation.

---

**EXPERT PERSONA — declare before Stage 1**

Domain: Connectors and backend integration.

Discovery obligation table — all four rows required; each row names one obligation category the inventory must surface before Stage 1 closes:

| # | Obligation Term | Discovery Target |
|---|-----------------|-----------------|
| 1 | shadow-call | A dependency that handles the feature's behavior but is nowhere in the feature description — discoverable only by inference from what the feature must do |
| 2 | taken-for-granted | A call present in the description but documented without auth, rate limit, or error context — assumed to work without scrutiny |
| 3 | fog-system | A call whose target system identity is partially or entirely unknown — the integration endpoint is unclear |
| 4 | relay-chain | A multi-hop call where an intermediate service re-delegates to a downstream system, compounding auth and error propagation risk |

VOCABULARY RULE: The flag column headers in the Stage 1 inventory table below must be the exact tokens from the Obligation Term column above. Column header `[shadow-call]` = OBL-1 Obligation Term "shadow-call". Column header `[taken-for-granted]` = OBL-2 Obligation Term "taken-for-granted". Column header `[fog-system]` = OBL-3 Obligation Term "fog-system". Column header `[relay-chain]` = OBL-4 Obligation Term "relay-chain". Token identity is mechanically verifiable by table schema comparison — a column header that does not match its corresponding Obligation Term cell fails schema alignment. YOU MUST NOT substitute a canonical term (e.g., `[forgotten-call]`, `[unknown-system]`) for any of the non-standard Obligation Terms above — canonical substitution breaks vocabulary identity within this trace, and a reviewer comparing the obligation table to the inventory table will see the mismatch as a structural discrepancy.

Apply all four discovery obligation rows while constructing the Stage 1 inventory.

---

**STAGE 1 — CALL INVENTORY**

YOU MUST complete the inventory table before opening Stage 2. Stage 2 does not open until every row has all flag cells explicitly set.

| Call ID | Target System | Call Type | Confidence | [shadow-call] | [taken-for-granted] | [fog-system] | [relay-chain] |
|---------|--------------|-----------|------------|---------------|---------------------|--------------|---------------|
| CALL-1 | | | HIGH/MED/LOW | | | | |
| CALL-2 | | | HIGH/MED/LOW | | | | |
| ... | | | | | | | |

- Confidence: HIGH = explicitly described, MEDIUM = inferred from feature behavior, LOW = discovered through obligation scanning
- Flags: mark each applicable obligation using the exact tokens from the obligation table; mark inapplicable cells explicitly — (not omitted)

Stage 1 gate: YOU MUST NOT open Stage 2 until every call appears in the inventory table with all four flag cells explicitly set.

---

**STAGE 2 — PER-CALL ANALYSIS**

For each CALL-[N], produce one call block. Each block covers five concerns. Each concern occupies its own labeled section — the other four concerns are addressed in their own labeled sections in this block.

Before CALL-[1]: YOU MUST confirm inventory table complete.

```
CALL-[N]: [target system] — [call type]

- AUTH (authentication only — request/response format, rate limits, retry/idempotency, and error propagation are each in their own section below)
  - mechanism: [token / API key / OAuth / mTLS / none / unknown]
  - gap: [YES — auth mechanism unknown | NO]

- REQUEST/RESPONSE FORMAT (format only — auth, rate limits, retry/idempotency, and error propagation are each in their own section)
  - method: [HTTP verb or protocol]
  - request key fields: [list]
  - response key fields: [list]
  - encoding: [JSON / XML / binary / other]

- RATE LIMITS (rate limits only — auth, format, retry/idempotency, and error propagation are each in their own section)
  - limit value: [N per window / unknown — flag as rate-limit-exposure if unknown]
  - burst risk: [YES / NO / UNKNOWN]
  - throttle response: [HTTP 429 / backoff / queue / fail-open / other]

- RETRY AND IDEMPOTENCY (retry/idempotency only — auth, format, rate limits, and error propagation are each in their own section)
  - retry strategy: [exponential backoff / fixed interval / none / not applicable]
  - idempotent: [YES / NO]
  - mitigation: [idempotency key / dedup window / none — flag as finding if NO mitigation and non-idempotent]

- ERROR PROPAGATION (error propagation only — auth, format, rate limits, and retry/idempotency are each in their own section)
  - error disposition: [surfaced / swallowed / transformed / logged only / never-fails — required for every call; "never-fails" is an explicit valid disposition]

CALL-[N] GATE — YOU MUST check all five before CALL-[N+1]:
  [ ] auth: mechanism or gap flag documented
  [ ] format: method and key fields in separate sections
  [ ] rate limits: limit value or exposure flag documented
  [ ] retry/idempotency: strategy or finding documented
  [ ] error propagation: explicit disposition documented
```

AGGREGATION RULE: If Stage 2 produces any cross-stage aggregation structure, YOU MUST state on that structure: (a) populated FROM the call blocks — call blocks are the authoritative source; (b) this structure is not authoritative; (c) assessment proceeds from call blocks alone — this structure is not required. Traces with no cross-stage structures pass this rule by default.

NEW-CALL RULE: YOU MUST NOT open a call block for any call not already in the Stage 1 inventory table. If you discover a new call during Stage 2, add a row to the inventory table with all flags set before opening its block.

---

**STAGE 3 — GAP INVENTORY**

Collect all findings from Stage 2. For each finding:

```
- GAP-[N]
  - call-id: CALL-[N]
  - gap-type: [auth-gap / rate-limit-exposure / error-swallowing / missing-idempotency / fog-system / relay-chain / other]
  - severity: [HIGH / MEDIUM / LOW]
  - rationale: [one line — MEDIUM and LOW are not exempt]
  - remediation: [actionable fix specific to this call — required for every HIGH finding; YOU MUST NOT use generic advice]
```

At minimum one finding required.

---

**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*

YOU MUST include this coda unconditionally. It is appended after Stage 3 — the last numbered stage — and fires regardless of whether Stage 2 produced any cross-stage aggregation structure.

If any cross-stage aggregation structure appeared in Stage 2:
  YOU MUST state for each structure:
  - populated FROM the call blocks — call blocks are the authoritative source
  - this structure is not authoritative
  - assessment proceeds from call blocks alone; this structure is not required

If no cross-stage structures were produced:
> No cross-stage structures produced in this trace.

---

## Variation Summary

| ID | Axis | C-24 Mechanism | C-25 Mechanism | Open Question Probed | Prediction |
|----|------|----------------|----------------|----------------------|------------|
| V-01 | Role sequence | 4-row obligation table before Stage 1 | Inventory table column headers = obligation row terms; VOCABULARY RULE reinforces | — | 177/177 |
| V-02 | Output format (full tables) | 4-row obligation table before Section 1 | Schema-only enforcement — VOCABULARY RULE dropped; column headers are obligation row terms by instruction | — | 177/177 |
| V-03 | Mixed format (table obligation + pipe inventory) | 4-row obligation table present | NO column headers in pipe-delimited inventory — VOCABULARY RULE satisfies C-22 but schema alignment is unverifiable by header comparison | Q2: does C-25 require column header cells? | 172/177 (C-25 FAIL predicted) |
| V-04 | Phase architecture + terminal coda corrected | 4-row obligation table in Phase 1 | Inventory table column headers = obligation row terms | Q1: terminal-position constraint definitive verdict | 177/177 |
| V-05 | Non-standard terms + C-24/C-25 + canonical prohibition | 4-row obligation table with non-standard terms | Inventory column headers = non-standard obligation row terms; canonical substitution prohibited | — | 177/177 |

**R8 scoring predictions:**
- V-01, V-02, V-04, V-05: 177/177
- V-03: 172/177 IF C-25 requires column header cells (Q2 probe predicts FAIL); 177/177 IF any schema-traceable token alignment passes C-25
