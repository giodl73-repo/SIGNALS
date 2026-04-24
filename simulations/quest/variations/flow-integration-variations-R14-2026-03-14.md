Written to `simulations/quest/rubrics/flow-integration-rubric-v14-variations-R14-2026-03-15.md`.

---

# flow-integration — R14 Variations (v14 rubric, 242 pt ceiling)

**New criteria under test:** C-37 (temporal stakes anchor, 5 pts) + C-38 (obligation-count-agnostic framing, 5 pts)

**R14 open questions:**
- **Q1** — Does C-37 require a delivery-phase temporal marker ("before the feature ships"), or does consequence-form ("undocumented calls become ship-blockers") satisfy C-37 equivalently?
- **Q2** — Does C-37 require concern enumeration alongside the stakes anchor, or does the stakes anchor alone (without listing auth/rate-limits/retry/error-propagation) satisfy C-37?

**Axes selected:**

| V | Axis | Type |
|---|------|------|
| V-01 | C-37 consequence-form (concern enumeration kept, temporal removed) | Single — Q1 probe |
| V-02 | C-37 stakes-alone (temporal kept, concern enumeration removed) | Single — Q2 probe |
| V-03 | Phrasing register: declarative (full C-37 temporal + concern form retained) | Single — C-37 register neutrality |
| V-04 | consequence-form + stakes-alone (both Q1+Q2 stripped; lower bound) | Combined |
| V-05 | C-35 extended set + C-37 consequence-form + C-38 count-agnostic (full 242-pt ceiling run) | Combined |

**Score predictions:**

| V | Predicted | Hinge |
|---|-----------|-------|
| V-01 | 212/212 if consequence-form satisfies C-37; 207/212 otherwise | Q1 |
| V-02 | 212/212 if stakes anchor alone satisfies C-37; 207/212 otherwise | Q2 |
| V-03 | 212/212 — register is structurally neutral; temporal anchor present in declarative form | — |
| V-04 | 207/212 most likely (-5 C-37) — neither temporal nor concern enumeration present | Q1+Q2 |
| V-05 | 242/242 if Q1 permissive + C-38 confirmed; 237/242 if temporal required | Q1 + C-35/C-38 |

---

## V-01 — C-37 Consequence-Form (Q1 Probe)

**Axis**: C-37 content form — concern enumeration kept, temporal marker replaced with consequence-form anchor.

**Hypothesis**: If consequence-form ("become ship-blockers at integration review") converts the framing from description to constraint as effectively as temporal form, C-37 PASS. Expected 212/212 if true; 207/212 if delivery-phase temporal marker is the required surface.

Canonical obligation terms. No YOU MUST NOT block needed.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and to verify
that each call's authentication, rate limits, retry behavior, and error propagation are fully
documented — undocumented integration calls become ship-blockers at integration review and
cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL | Obligation Term | What to discover |
|-----|----------------|-----------------|
| OBL-1 | forgotten-call | Calls absent from the spec: implicit token refreshes, health probes, SDK-internal calls, telemetry posts, connection pre-warm calls |
| OBL-2 | assumed-to-work | Calls present in the spec but underdocumented: missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment |
| OBL-3 | unknown-system | Calls whose target system identity, owner, or location cannot be confirmed from the available signal |
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

| Call ID | Target System | Call Type | Confidence | [forgotten-call] | [assumed-to-work] | [unknown-system] | [delegation-chain] |
|---------|---------------|-----------|------------|------------------|-------------------|------------------|--------------------|
| CALL-01 | | | HIGH/MED/LOW | Y/N | Y/N | Y/N | Y/N |
| CALL-02 | | | HIGH/MED/LOW | Y/N | Y/N | Y/N | Y/N |
| ... | | | | | | | |

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
| Idempotent | Y/N |
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
| Authentication documented | [] |
| Request/response documented | [] |
| Rate limits documented | [] |
| Retry/idempotency documented | [] |
| Error propagation documented | [] |

---

**STAGE 3 — GAP INVENTORY**

List every gap identified across all call blocks. Every finding must carry a severity label
and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings require a
call-specific remediation sketch; generic advice does not satisfy.

| Gap ID | Call ID | Gap Type | Severity | Rationale | Remediation |
|--------|---------|----------|----------|-----------|-------------|
| GAP-01 | | auth-gap / rate-limit-gap / retry-gap / error-swallow / unknown-system / delegation-risk | HIGH/MED/LOW | | |

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda fires unconditionally. If Stage 2 produced no cross-stage aggregation structures,
write: "No cross-stage structures produced in this trace." It does not appear between any two
numbered stages; it does not displace or renumber any existing element.

For any cross-stage structure produced in Stage 2:

| Property | Value |
|----------|-------|
| Populated from | Per-call blocks (Stage 2) |
| Authoritative source | Per-call blocks — this structure is secondary |
| Required for assessment | No |

---

## V-02 — C-37 Stakes-Alone (Q2 Probe)

**Axis**: C-37 concern enumeration removed — temporal anchor kept, no listing of specific concerns.

**Hypothesis**: Stakes anchor alone ("before the feature ships") converts description to constraint without concern enumeration. Expected 212/212 if stakes anchor alone satisfies C-37; 207/212 if concern enumeration is a required companion.

*(All structural elements identical to V-01 except the WHY block below.)*

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and to verify that
all documentation gaps are resolved before the feature ships.

---

*(remainder of prompt body: expert persona declaration through coda — identical to V-01)*

---

## V-03 — Phrasing Register: Declarative (C-37 Register Neutrality Probe)

**Axis**: All imperative instructions rephrased as declarative/descriptive constructions. WHY block retains full C-37 form — temporal anchor + concern enumeration — in declarative voice.

**Hypothesis**: C-37 is not register-sensitive. A declarative temporal anchor ("documentation gaps are identified before the feature ships") satisfies C-37 equally to the imperative form. Expected 212/212; confirms register is a free variation axis for C-37 as it was for C-01–C-36.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes. Each call's
authentication, rate limits, retry behavior, and error propagation are documented before the
feature ships — documentation gaps identified at that boundary are integration-review blockers,
not post-ship discoveries.

---

A cross-system integration trace is produced for the feature described in the signal by a
connectors and backend integration domain expert.

---

**EXPERT PERSONA DECLARATION**

*(obligation table: canonical four rows, identical to V-01)*

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

NEW-CALL RULE: Any call discovered during Stage 2 analysis that is not already in this table
receives a row — with all four flag cells set — before its analysis block opens.

*(inventory table: identical to V-01)*

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

**[N.1] AUTHENTICATION** *(authentication only — the other four concerns each occupy a dedicated section in this call block)*

*(tables identical to V-01)*

**CALL-[N] COMPLETION GATE** — CALL-[N+1] opens only after all five rows are confirmed:

*(checklist identical to V-01)*

---

**STAGE 3 — GAP INVENTORY**

Every gap identified across all call blocks is listed here. Each finding carries a severity
label and a one-line rationale — MEDIUM and LOW findings are not exempt. HIGH findings carry
a call-specific remediation sketch; generic advice does not satisfy.

*(gap table identical to V-01)*

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

This coda is present regardless of Stage 2 output. When Stage 2 produces no cross-stage
aggregation structures, the entry reads: "No cross-stage structures produced in this trace."
It occupies no position between numbered stages; no existing element is displaced or renumbered.

*(secondary-positioning table identical to V-01)*

---

## V-04 — Combined: Consequence-Form + Stakes-Alone (Lower Bound Probe)

**Axis**: Both Q1 and Q2 stripped — no temporal marker, no concern enumeration. WHY block contains only purpose + ship-blocking consequence reference.

**Hypothesis**: 207/212 most likely (-5 C-37). Neither the temporal anchor nor concern enumeration is present to convert the framing from description to delivery-phase constraint. Adjudication resolves whether C-37 is a *stakes-presence* criterion (any consequence reference passes) or a *stakes-form* criterion (temporal or concern enumeration required). If the former, 212/212.

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface the cross-system calls that can block a release — the
ones not in the specification, the ones assumed to work, the ones with unknown owners, and
the ones delegating credentials through chains the feature team has not mapped.

---

*(remainder of prompt body: identical to V-01)*

---

## V-05 — Combined: C-35 + C-37 Consequence-Form + C-38 (Full Ceiling Run / Q1 Probe)

**Axis**: Five-row non-standard obligation table (C-35) + consequence-form C-37 + canonical four-concern WHY framing (C-38 confirmed count-agnostic from R13 V-02). Tests whether Q1-permissive C-37 composes cleanly with C-35 + C-38 at full 242-pt ceiling.

**Hypothesis**: C-35 PASS, C-36 PASS, C-38 PASS all expected from R13 confirmation. C-37 is the open question. If consequence-form satisfies: 242/242. If temporal marker required: 237/242 (-5 C-37). C-27/C-30/C-31/C-34 in play for the three substituted canonical tokens.

Non-standard terms: `expose-call` (sub for forgotten-call) / `silent-entry` (sub for assumed-to-work) / `shadow-system` (sub for unknown-system) / `delegation-chain` (canonical, kept) / `burst-start` (new — first-request behavior when pre-warm state unknown; no canonical equivalent).

---

**WHY THIS TRACE DISCIPLINE EXISTS**

Integration traces exist to surface every cross-system call a feature makes and to verify
that each call's authentication, rate limits, retry behavior, and error propagation are fully
documented — calls without documentation become ship-blockers at integration review and
cannot be cleared without a completed trace.

---

You are a connectors and backend integration domain expert. Produce a cross-system integration
trace for the feature described in the signal.

---

**EXPERT PERSONA DECLARATION**

Domain: Connectors and backend integration — Power Platform connectors, Azure APIs, MCP
servers, REST and OData endpoints, managed identity chains, on-behalf-of token exchange.

Discovery obligation table — one row per obligation; structural completeness is verified by row
count; a missing row is a missing obligation:

| OBL | Obligation Term | What to discover |
|-----|----------------|-----------------|
| OBL-1 | expose-call | Calls that execute as part of the feature but are absent from the specification — implicit token refreshes, health probes, SDK-internal calls, telemetry posts |
| OBL-2 | silent-entry | Calls the specification names but treats as documentation-free — missing auth detail, retry strategy, failure modes, or rate-limit acknowledgment |
| OBL-3 | shadow-system | Calls whose target system identity, owner, or location cannot be confirmed from the available signal |
| OBL-4 | delegation-chain | Calls made on behalf of the user through managed identity, OBO token exchange, service principal impersonation, or proxy delegation |
| OBL-5 | burst-start | Calls where connection reuse or pre-warm state is unknown at trace time — first-invocation behavior may differ materially from steady-state behavior |

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

| Call ID | Target System | Call Type | Confidence | [expose-call] | [silent-entry] | [shadow-system] | [delegation-chain] | [burst-start] |
|---------|---------------|-----------|------------|---------------|----------------|-----------------|--------------------|---------------|
| CALL-01 | | | HIGH/MED/LOW | Y/N | Y/N | Y/N | Y/N | Y/N |
| CALL-02 | | | HIGH/MED/LOW | Y/N | Y/N | Y/N | Y/N | Y/N |

---

**STAGE 2 — PER-CALL ANALYSIS**

*(AGGREGATION RULE, per-call block structure, COMPLETION GATE: identical to V-01)*

---

**STAGE 3 — GAP INVENTORY**

*(identical to V-01 except Gap Type enum includes shadow-system / delegation-chain / burst-start)*

---

**CROSS-STAGE AGGREGATION STRUCTURES** *(no stage number — appended after Stage 3, the last numbered stage)*

*(coda structure identical to V-01)*

---

**What R14 resolves:**

| Criterion | Q | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|---|------|------|------|------|------|
| C-37 temporal vs. consequence form | Q1 | **probe** | control | control | probe | **probe** |
| C-37 stakes-alone vs. concern-enumerated | Q2 | control | **probe** | control | probe | control |
| C-37 register sensitivity | — | — | — | **probe** | — | — |
| C-35 + C-37 + C-38 composition | — | — | — | — | — | **probe** |
