---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 7
rubric_version: 7
---

# flow-ratelimit — Variate R7

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence — terminal document-close reconciler as Role 11), V-02 (output format — two-tier violation taxonomy in Format Contract), V-03 (lifecycle emphasis — per-phase Verdict-currency checks at every phase exit).
Combination variations: V-04 (role sequence + output format — terminal reconciler + two-tier taxonomy + full gate chain), V-05 (all five axes — INERTIA framing + two-tier taxonomy + terminal reconciler + per-role column-compliance annotations + per-gate Verdict-currency everywhere).

**R7 target criteria: C-24 (Terminal Document-Close Reconciler) and C-25 (Two-Tier Violation Taxonomy in Format Contract)**

C-24 was extracted from R6 V-01's Role 11: a dedicated terminal role after all analysis roles, performing retroactive audit of complete document state (REVISED marker scan, gate deliverable confirmation, DERIVATION CHAIN cell scan), producing a named finding record. Neither C-18 nor C-22 requires this mechanism — they require markers to be present and currency checks to be embedded. The reconciler closes gaps that per-gate enforcement missed.

C-25 was extracted from R6 V-02's Format Contract: STRUCTURAL REJECTION CLAUSE (column absent — scan-time detectable, remediation: add column) and CONTENT REJECTION CLAUSE (column present but cell lacks mandated content — read-time detectable, remediation: deepen cell) as explicitly named, distinct clause types. C-16 requires only a rejection clause; C-23 requires one for DERIVATION CHAIN. C-25 requires the clauses to be named as distinct types with different detection methods and remediation paths.

**R7 variation axes:**

| Axis | What changes |
|------|-------------|
| Role sequence | 11-role pipeline; terminal reconciler placement; which roles carry currency checks |
| Output format | Format Contract two-tier taxonomy; STRUCTURAL vs CONTENT as named clause types |
| Lifecycle emphasis | Phase-based structure; per-phase exit conditions carry Verdict-currency instructions |
| Inertia framing | INERTIA as named competitor column replacing generic BASELINE |
| Phrasing register | Per-role column-compliance annotations; imperative structural commands |

---

## V-01

**Variation axis**: Role sequence — 11-role pipeline with dedicated terminal document-close reconciler as Role 11, the last named section in the document.

**Hypothesis**: A terminal audit role that retroactively scans complete document state after all analysis roles are written catches REVISED marker gaps, confirms gate deliverables were produced, and flags DERIVATION CHAIN cells containing only conclusions — achieving C-24 compliance even when per-gate currency checks cover only a subset of transitions, because the backward scan closes forward-enforcement gaps that incomplete gate coverage leaves open.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across a rate-limited system for the described scenario.

Given: a flow or automation description with request volume, connector and action types, and any known rate limits.

Produce a structured analysis following the 11-role sequence below. Each role produces named deliverables. **Do not begin a role until all named deliverables from the prior role are written in full.**

---

### ROLE 1 — GLOBAL VERDICT

Produce a standalone Verdict block before any rate limit inventory, burst path audit, or volume mapping. The Verdict block must contain all three fields:

**(a) Binding Constraint**: [Component name] — [numeric threshold with unit] — [one sentence: why this limit binds before others under the described load]

**(b) Primary Gap**: [Specific unprotected burst path at named action/connector, or Retry-After handling gap at named connector] — [one sentence: failure mode this gap causes]

**(c) System Status**: SAFE / DEGRADED / FAILING at the described load

Label the block `VERDICT [pending confirmation]`. The Verdict block must be self-contained: a reader who reads only it knows the core finding without reading subsequent roles.

---

### ROLE 2 — FORMAT CONTRACT

**Gate: Do not begin Role 2 until Role 1 Verdict block is written with all three fields present.**

Declare the document-wide format contract.

**(a) Table Schema**: Every comparative table in this document uses:
`| Component | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |`

**(b) Scenario-specific definitions**:
- **BASELINE**: The current system behavior at the named component in the unmitigated state — the absence of any concurrency cap, retry policy, or queue buffer on this path.
- **PROTECTED**: System behavior at the same component after the named mitigation is applied.
- **DERIVATION CHAIN**: Step-by-step computation showing how BASELINE and PROTECTED values were derived from the rate limit registry in Role 3. Cells containing only qualitative conclusions are content-incomplete.
- **Delta**: Quantified improvement from BASELINE to PROTECTED expressed numerically or as a percentage.

**(c) Rejection Clause**: Any comparative table missing a required column (BASELINE, PROTECTED, DERIVATION CHAIN, or Delta) is flagged as structurally incomplete. Any DERIVATION CHAIN cell containing only a conclusion without computation steps is flagged as content-incomplete. At least two distinct comparative tables in this document must comply with the full schema.

---

### ROLE 3 — NUMERIC RATE LIMIT REGISTRY

**Gate: Do not begin Role 3 until Role 2 Format Contract is written with table schema, scenario-specific definitions, and rejection clause present.**

Produce a registry table of all rate limits relevant to the scenario:

| Limit ID | Component | Limit Type | Threshold | Window | Scope | Source |
|----------|-----------|------------|-----------|--------|-------|--------|

Populate at least one row with a concrete numeric threshold (e.g., "600 requests / 60 s"). Label estimates as "(est.)". This registry is the arithmetic source for all DERIVATION CHAIN cells in subsequent roles.

**Verdict-currency check**: Does the registry reveal a binding constraint different from Role 1 field (a)? If yes: insert `[REVISED — see Role 3]` in Role 1 field (a) now, before proceeding to Role 4.

---

### ROLE 4 — BINDING CONSTRAINT ANALYSIS

**Gate: Do not begin Role 4 until Role 3 registry is populated with at least one concrete numeric threshold.**

Identify which rate limit from Role 3 is the binding constraint under the described load. Provide explicit reasoning: why this limit — not a higher-capacity one — is hit first or most severely. State the arithmetic basis for the determination. Identifying multiple limits without a binding-constraint determination does not satisfy this role.

---

### ROLE 5 — CAUSAL CHAIN TO FAILURE MODE

**Gate: Do not begin Role 5 until Role 4 binding constraint is identified with explicit arithmetic reasoning.**

Trace a causal chain from trigger event through the rate-limited endpoint to the resulting failure mode. State every link explicitly:

`[Trigger] → [Action/Connector] → [Rate Limit Hit: Limit-ID] → [Platform Response] → [Failure Mode]`

Implied causation does not satisfy this role. Each arrow represents an explicit mechanism, not an assumed outcome.

**Verdict-currency check**: Does Role 5 chain reveal a primary gap different from Role 1 field (b)? If yes: insert `[REVISED — see Role 5]` in Role 1 field (b) now.

---

### ROLE 6 — RETRY-AFTER HANDLING GAP CHECK

**Gate: Do not begin Role 6 until Role 5 causal chain is fully stated with all links explicit.**

Evaluate per connector and HTTP action in the scenario whether the flow handles Retry-After headers or equivalent backoff signals (`x-ms-ratelimit-remaining`, `Retry-After-Ms`). For each gap found: flag as a finding and state the failure mode it causes (e.g., immediate retry storm, permanent failure after N retries, silent queue exhaustion).

**Verdict-currency check**: Does Role 6 identify the Retry-After gap as a more severe primary gap than Role 1 field (b)? If yes: insert `[REVISED — see Role 6]` in Role 1 field (b) now.

---

### ROLE 7 — UNPROTECTED BURST PATH AUDIT

**Gate: Do not begin Role 7 until Role 6 Retry-After evaluation is complete for each connector/action.**

Identify at least one structurally unprotected burst path — a trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between source and rate-limited endpoint. A path with throttle controls at a higher tier only does not qualify.

For each path, classify:
- **STRUCTURAL**: No mechanism exists on this path. Remediation: add concurrency control and/or queue buffer.
- **INCIDENTAL**: A mechanism exists but is misconfigured, bypassable, or absent only under specific conditions. Remediation: close the bypass condition.

---

### ROLE 8 — CASCADING THROTTLE FAILURE SCENARIO

**Gate: Do not begin Role 8 until Role 7 burst path audit is complete with at least one path classified.**

Construct or identify a specific scenario where throttling at one tier causally triggers a second distinct throttle event at a different tier. State the causal link explicitly. Describe the compounding effect on throughput or error rate. Two independent limits both hit under load do not constitute a cascade — the second throttle must be causally triggered by the first.

---

### ROLE 9 — UX PER THROTTLE TIER

**Gate: Do not begin Role 9 until Role 8 cascade scenario is stated with explicit causal link.**

Describe user-facing behavior at each distinct throttle tier reached. Apply the four-field template to each tier — at least two tiers required:

**Tier: [Name]**
| Field | Value |
|-------|-------|
| (a) Error code / platform signal | |
| (b) User-visible behavior | |
| (c) Visibility level | user-visible and explicit / silent or background |
| (d) Recovery path available | |

A tier described in free prose without this template structure does not satisfy this role even if all four fields are mentioned.

---

### ROLE 10 — VOLUME MAPPING + QUANTIFIED IMPACT + MITIGATIONS

**Gate: Do not begin Role 10 until Role 9 has at least two complete four-field tier entries.**

**10a — Volume-to-Behavior Mapping**

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|-----------------|-------|
| 1x | | | | |
| 2x | | | | |
| 5x | | | | |

The 5x BASELINE DERIVATION CHAIN cell must show step-by-step arithmetic:
1. requests/interval × 5 = peak load
2. peak load − [Limit-ID threshold from registry] = overflow volume
3. overflow × retry factor = failed volume after retries
4. failed / peak = failure percentage
5. [failure_pct]% fail at 5x under BASELINE

The 5x PROTECTED cell must show same steps with mitigated values applied.

**10b — Per-Bottleneck Mitigations**

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|-----------------|-------|

- PROTECTED: name the specific action, setting, or parameter — generic advice does not pass.
- BASELINE: name the current behavior at this specific component.
- DERIVATION CHAIN: show BASELINE arithmetic vs PROTECTED arithmetic; conclusion-only cells do not pass.

**Verdict-currency check**: Does Role 10 mitigation set change System Status in Role 1 field (c)? If yes: insert `[REVISED — see Role 10]` in Role 1 field (c) now.

---

### ROLE 11 — TERMINAL RECONCILER

**Gate: Do not begin Role 11 until Roles 1–10 are fully written.**

This role performs a retroactive audit of complete document state. Produce a named finding record: either **Reconciler Findings: 0 violations** or an itemized list.

**(a) Verdict Revision Scan**

For each claim in the Role 1 Verdict block:
- Field (a) Binding Constraint: confirm it stands as written OR carries `[REVISED — see Role N]` with a forward reference. Flag any revision without a marker as a violation.
- Field (b) Primary Gap: same check.
- Field (c) System Status: same check.

**(b) Gate Deliverable Confirmation**

| Transition | Required Deliverable | Present? |
|-----------|---------------------|----------|
| Role 1 → Role 2 | Verdict block with fields (a)–(c) | |
| Role 2 → Role 3 | Format Contract with schema, definitions, rejection clause | |
| Role 3 → Role 4 | Registry with at least one concrete numeric threshold | |
| Role 4 → Role 5 | Binding constraint with arithmetic reasoning | |
| Role 5 → Role 6 | Causal chain with all links explicit | |
| Role 6 → Role 7 | Retry-After evaluation per connector/action | |
| Role 7 → Role 8 | Burst path audit with at least one classified path | |
| Role 8 → Role 9 | Cascade scenario with explicit causal link | |
| Role 9 → Role 10 | At least two four-field tier entries | |

Flag any missing deliverable as a violation.

**(c) DERIVATION CHAIN Cell Scan**

Identify any DERIVATION CHAIN cell in any comparative table that contains only a qualitative conclusion without step-by-step computation. Flag each as content-incomplete with table location.

Produce: **Reconciler Findings: [N violations]** followed by itemized list (or 0 violations if clean). A section that scans without producing a finding record does not satisfy this role.

---

## V-02

**Variation axis**: Output format — Format Contract with two-tier violation taxonomy: explicitly named STRUCTURAL REJECTION CLAUSE and CONTENT REJECTION CLAUSE as distinct clause types with different detection methods and remediation paths.

**Hypothesis**: When the Format Contract names two rejection clause types with different detection methods (scan-time vs read-time) and different remediation paths (add column vs deepen cell), enforcement operates at two distinct effort levels. An evaluator can check structural violations by table scan without reading prose; content violations require cell-level reading. Collapsing both into a single clause forces read-time assessment of every cell even when the structural violation is immediately visible — and obscures which remediation applies. Explicit naming closes that ambiguity and makes violation type unambiguous at detection time.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across a rate-limited system for the described scenario.

Given: a flow or automation description with request volume, connector and action types, and any known rate limits.

Produce a structured analysis following the section sequence below.

---

### PREAMBLE 1 — GLOBAL VERDICT

**Write this section before any rate limit inventory, analysis section, or table.**

State three fields:

**(a) Binding Constraint**: [Component] — [threshold with unit] — [reason this limit binds before others]

**(b) Primary Gap**: [Unprotected burst path or Retry-After gap at named action/connector] — [failure mode]

**(c) System Status**: SAFE / DEGRADED / FAILING at described load

Label: `VERDICT [pending confirmation]`. Self-contained — reader who reads only this knows the core finding.

---

### PREAMBLE 2 — FORMAT CONTRACT

**Write this section before any analysis section. Do not begin Section 1 until Preamble 2 is complete.**

**(a) Table Schema**

Every comparative table in this document declares the following column structure:

`| Component | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |`

**(b) Scenario-specific definitions**:
- **BASELINE**: System behavior at the named component in the current unmitigated state.
- **PROTECTED**: System behavior at the same component after the specific named mitigation is applied.
- **DERIVATION CHAIN**: Step-by-step computation showing how BASELINE and PROTECTED values were derived from Section 1 rate limit values.
- **Delta**: Quantified improvement from BASELINE to PROTECTED.

**(c) Rejection Clauses** — two named, distinct types:

**STRUCTURAL REJECTION CLAUSE**
- Violation type: Schema violation — a required column (BASELINE, PROTECTED, DERIVATION CHAIN, or Delta) is absent from the table structure.
- Detection method: Scan-time — the column header is present or absent. No cell content reading required.
- Remediation: Add the missing column to the table structure before populating rows.
- Flag format: `[STRUCTURAL VIOLATION: missing column "<column name>" in <table location>]`

**CONTENT REJECTION CLAUSE**
- Violation type: Cell content violation — a required column is present in the table structure, but a cell in that column contains only a qualitative conclusion (e.g., "high load causes failures") without the mandated computation steps.
- Detection method: Read-time — the column header is present, but the cell content must be read and assessed to determine whether computation steps are present.
- Remediation: Replace the conclusion-only cell content with step-by-step arithmetic referencing Section 1 values.
- Flag format: `[CONTENT VIOLATION: DERIVATION CHAIN cell at <table location>, row <identifier> contains conclusion only]`

A single combined rejection clause covering both violation types does not satisfy this Format Contract. Both clause types must be declared as distinct named entries with separate detection methods and separate remediation instructions.

At least two distinct comparative tables in this document must comply with the full declared schema.

---

### SECTION 1 — NUMERIC RATE LIMIT REGISTRY

Produce a registry table of all rate limits relevant to the scenario:

| Limit ID | Component | Limit Type | Threshold | Window | Scope | Source |
|----------|-----------|------------|-----------|--------|-------|--------|

At least one row must have a concrete numeric threshold. Label estimates as "(est.)". This registry is the arithmetic source for all DERIVATION CHAIN cells.

If Section 1 reveals a binding constraint different from Preamble 1 field (a): insert `[REVISED — see Section 1]` in Preamble 1 field (a).

---

### SECTION 2 — BINDING CONSTRAINT ANALYSIS

Identify which rate limit from Section 1 is the binding constraint under the described load. Provide explicit reasoning: why this limit, not a higher-capacity one, is hit first or most severely. State the arithmetic basis.

---

### SECTION 3 — CAUSAL CHAIN TO FAILURE MODE

Trace a causal chain from trigger event to failure mode. State every link explicitly:

`[Trigger] → [Action/Connector] → [Rate Limit Hit: Limit-ID] → [Platform Response] → [Failure Mode]`

Implied causation does not pass. If this chain reveals a primary gap different from Preamble 1 field (b): insert `[REVISED — see Section 3]` in Preamble 1 field (b).

---

### SECTION 4 — RETRY-AFTER HANDLING GAP CHECK

Evaluate per connector and HTTP action whether the flow handles Retry-After headers or equivalent backoff signals. For each gap: flag as a finding and state the failure mode (e.g., retry storm, permanent failure after N retries). If this gap is more severe than Preamble 1 field (b): insert `[REVISED — see Section 4]` in Preamble 1 field (b).

---

### SECTION 5 — UNPROTECTED BURST PATH AUDIT

Identify at least one structurally unprotected burst path — no concurrency cap, no retry policy, no queue buffer between source and rate-limited endpoint. A path with throttle controls at a higher tier only does not qualify.

For each path, classify:
- **STRUCTURAL**: No mechanism exists on this path.
- **INCIDENTAL**: A mechanism exists but is misconfigured, bypassable, or absent only under specific conditions.

Justify each classification explicitly.

---

### SECTION 6 — CASCADING THROTTLE FAILURE SCENARIO

Construct or identify a specific scenario where throttling at one tier causally triggers a second distinct throttle event at a different tier. State the causal link. Describe the compounding effect on throughput or error rate. Two independent limits both hit under load do not constitute a cascade.

---

### SECTION 7 — UX PER THROTTLE TIER

Describe user-facing behavior at each distinct throttle tier reached. Apply the four-field template to at least two tiers:

**Tier: [Name]**
| Field | Value |
|-------|-------|
| (a) Error code / platform signal | |
| (b) User-visible behavior | |
| (c) Visibility level | user-visible and explicit / silent or background |
| (d) Recovery path available | |

Free prose without this template structure does not satisfy this section.

---

### SECTION 8 — VOLUME MAPPING + QUANTIFIED IMPACT + MITIGATIONS

**8a — Volume-to-Behavior Mapping** (first compliant table — must satisfy Format Contract schema)

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|-----------------|-------|
| 1x | | | | |
| 2x | | | | |
| 5x | | | | |

5x BASELINE DERIVATION CHAIN cell must show step-by-step arithmetic referencing Section 1 values. 5x PROTECTED must show same steps with mitigated operands. Apply both STRUCTURAL and CONTENT rejection clauses to this table on completion.

**8b — Per-Bottleneck Mitigations** (second compliant table — must satisfy Format Contract schema)

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|-----------------|-------|

- PROTECTED: name the specific action, setting, or parameter — generic advice does not pass.
- BASELINE: name the current behavior at this specific component.
- DERIVATION CHAIN: step-by-step arithmetic comparing BASELINE vs PROTECTED values. Apply CONTENT REJECTION CLAUSE if any cell contains only a conclusion.

If Section 8 changes System Status: insert `[REVISED — see Section 8]` in Preamble 1 field (c).

**After Section 8**: verify each VERDICT claim. For any claim revised during Sections 1–8 that does not carry a `[REVISED — see Section N]` marker: insert the missing marker now.

---

## V-03

**Variation axis**: Lifecycle emphasis — seven-phase structure where every phase exit condition includes an explicit Verdict-currency instruction, enforcing C-22 at each transition boundary rather than deferring revision marking to a terminal pass.

**Hypothesis**: When Verdict-currency instructions are embedded in the exit condition of every phase — "if this phase revises any Verdict claim, insert the REVISED marker before the gate condition unblocks" — revision marking occurs at the moment of production. A terminal reconciler verifies these were performed, but the primary enforcement mechanism is forward rather than backward. This eliminates the gap C-22 targets: a document where currency checks are performed correctly at every gate leaves the reconciler with zero marking violations to close, demonstrating that terminal audit and per-gate enforcement are orthogonal and both necessary.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across a rate-limited system for the described scenario.

Given: a flow or automation description with request volume, connector and action types, and any known rate limits.

Produce a structured analysis following the seven-phase structure below. Each phase has explicit entry and exit conditions. **Do not cross a phase exit gate until the exit condition is fully satisfied.**

---

### PREAMBLE A — GLOBAL VERDICT

**Entry**: Start here. No prior phase required.
**Exit gate**: All three Verdict fields written. Do not begin Phase 1 until this gate passes.

**(a) Binding Constraint**: [Component] — [threshold with unit] — [why this limit binds before others]
**(b) Primary Gap**: [Burst path or Retry-After gap at named action/connector] — [failure mode]
**(c) System Status**: SAFE / DEGRADED / FAILING at described load

Label: `VERDICT [pending confirmation]`

---

### PREAMBLE B — FORMAT CONTRACT

**Entry**: Preamble A Verdict block written.
**Exit gate**: Format Contract complete with schema, definitions, and both rejection clauses. Do not begin Phase 1 until this gate passes.

**(a) Table Schema**: `| Component | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |`

**(b) Definitions**:
- **BASELINE**: Current system behavior at the named component without mitigation.
- **PROTECTED**: Behavior at the same component with the specific named mitigation applied.
- **DERIVATION CHAIN**: Step-by-step computation tracing values to the Phase 1 registry. Cells with conclusions only are content-incomplete.
- **Delta**: Quantified improvement BASELINE → PROTECTED.

**(c) Rejection Clauses**:

**STRUCTURAL REJECTION CLAUSE** — Column absent from table structure. Detection: scan-time (header present/absent). Remediation: add missing column.

**CONTENT REJECTION CLAUSE** — Column present but DERIVATION CHAIN cell contains only a conclusion. Detection: read-time (cell content must be assessed). Remediation: replace conclusion with computation steps referencing Phase 1 values.

Two distinct clause types required. At least two tables in this document must comply with the full schema.

**Verdict-currency check**: Does the Format Contract's BASELINE definition imply a different System Status severity than Preamble A field (c)? If yes: insert `[REVISED — see Preamble B]` in field (c) now.

---

### PHASE 1 — RATE LIMIT INVENTORY

**Entry**: Preamble B Format Contract complete.

Produce a registry of all rate limits relevant to the scenario:

| Limit ID | Component | Limit Type | Threshold | Window | Scope | Source |
|----------|-----------|------------|-----------|--------|-------|--------|

At least one concrete numeric threshold required. Label estimates as "(est.)".

**Exit gate + Verdict-currency check**: Registry populated with at least one numeric threshold. Does Phase 1 reveal a binding constraint different from Preamble A field (a)? **If yes: insert `[REVISED — see Phase 1]` in field (a) now, before crossing to Phase 2.** Do not begin Phase 2 until gate passes and any required marker is inserted.

---

### PHASE 2 — BINDING CONSTRAINT + CAUSAL CHAIN

**Entry**: Phase 1 registry populated.

**2a — Binding Constraint**: Identify which Phase 1 limit binds first under the described load. Explicit arithmetic reasoning required. Identifying multiple limits without a determination does not pass.

**2b — Causal Chain**: Trace from trigger to failure mode. State every link:
`[Trigger] → [Action/Connector] → [Rate Limit: Limit-ID] → [Platform Response] → [Failure Mode]`
Implied causation does not pass.

**Exit gate + Verdict-currency check**: Binding constraint identified with arithmetic. Causal chain fully stated. Does Phase 2 analysis revise either Preamble A field (a) or field (b)? **If yes: insert `[REVISED — see Phase 2]` in the revised field(s) now, before crossing to Phase 3.** Do not begin Phase 3 until gate passes and any required markers are inserted.

---

### PHASE 3 — GAP AUDIT

**Entry**: Phase 2 binding constraint and causal chain written.

**3a — Retry-After Gap Check**: Evaluate per connector and HTTP action whether Retry-After headers or equivalent backoff signals are handled. For each gap: state the failure mode (retry storm, permanent failure, silent drop).

**3b — Unprotected Burst Path Audit**: Identify at least one structurally unprotected burst path — no concurrency cap, no retry policy, no queue buffer. Classify:
- **STRUCTURAL**: No mechanism exists on this path.
- **INCIDENTAL**: Mechanism exists but is misconfigured or bypassable.

Justify each classification.

**Exit gate + Verdict-currency check**: Retry-After check complete per connector/action. Burst path audit complete with at least one classified path. Does Phase 3 identify a more severe primary gap than Preamble A field (b)? **If yes: insert `[REVISED — see Phase 3]` in field (b) now, before crossing to Phase 4.** Do not begin Phase 4 until gate passes and any required marker is inserted.

---

### PHASE 4 — CASCADE + UX

**Entry**: Phase 3 gap audit complete.

**4a — Cascading Throttle Scenario**: Construct or identify a scenario where throttling at one tier causally triggers throttle at a second tier. State the causal link explicitly. Two independent limits under load do not constitute a cascade.

**4b — UX Per Throttle Tier**: Apply four-field template to at least two tiers:

**Tier: [Name]**
| Field | Value |
|-------|-------|
| (a) Error code / platform signal | |
| (b) User-visible behavior | |
| (c) Visibility level | user-visible and explicit / silent or background |
| (d) Recovery path available | |

Free prose without the template does not pass.

**Exit gate + Verdict-currency check**: Cascade scenario stated with explicit causal link. At least two UX tiers described with full four-field template. Does Phase 4 reveal a different primary gap or change System Status? **If yes: insert `[REVISED — see Phase 4]` in the relevant field(s) now, before crossing to Phase 5.** Do not begin Phase 5 until gate passes and any required markers are inserted.

---

### PHASE 5 — VOLUME MAPPING + QUANTIFIED IMPACT

**Entry**: Phase 4 cascade and UX tiers written.

**Volume-to-behavior mapping** (first Format Contract-compliant table):

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|-----------------|-------|
| 1x | | | | |
| 2x | | | | |
| 5x | | | | |

5x BASELINE DERIVATION CHAIN cell — mandatory arithmetic:
1. requests/interval × 5 = peak load
2. peak load − [Limit-ID threshold] = overflow volume
3. overflow × retry factor = failed volume
4. failed / peak = failure percentage
5. [failure_pct]% fail at 5x BASELINE

5x PROTECTED cell: same five steps with mitigated operands.

Apply STRUCTURAL REJECTION CLAUSE to verify all columns present. Apply CONTENT REJECTION CLAUSE to verify 5x cells contain computation steps.

**Exit gate + Verdict-currency check**: All three volume bands filled. DERIVATION CHAIN column present and 5x cells show step-by-step arithmetic. Does Phase 5 arithmetic change System Status in Preamble A field (c)? **If yes: insert `[REVISED — see Phase 5]` in field (c) now, before crossing to Phase 6.** Do not begin Phase 6 until gate passes and any required marker is inserted.

---

### PHASE 6 — MITIGATIONS

**Entry**: Phase 5 volume mapping and 5x derivation complete.

Per-bottleneck mitigation table (second Format Contract-compliant table):

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|-----------------|-------|

For each bottleneck and burst path:
- PROTECTED: name the specific action, setting, or parameter — generic advice does not pass.
- BASELINE: name the current behavior at this specific component.
- DERIVATION CHAIN: show BASELINE arithmetic vs PROTECTED arithmetic proving improvement.
- Delta: quantified improvement from BASELINE state.

Apply STRUCTURAL REJECTION CLAUSE on completion. Apply CONTENT REJECTION CLAUSE to each DERIVATION CHAIN cell.

**Exit gate + Verdict-currency check**: Every bottleneck and burst path has a row. PROTECTED cells name specific controls. DERIVATION CHAIN cells show arithmetic. Does Phase 6 mitigation set change System Status under protection? **If yes: insert `[REVISED — see Phase 6]` in Preamble A field (c) now, before crossing to Phase 7.** Do not begin Phase 7 until gate passes and any required marker is inserted.

---

### PHASE 7 — TERMINAL RECONCILER

**Entry**: Phases 1–6 fully written.

Retroactive audit of complete document state. Produce a named finding record: **Reconciler Findings: [N violations]** or **0 violations**.

**(a) Verdict Revision Scan**: For each Preamble A claim (a)–(c): confirm it stands as written OR carries `[REVISED — see Phase/Preamble N]` with a forward reference. Flag any revised claim without a marker as a violation.

**(b) Gate Deliverable Confirmation**:
| Exit Gate | Required Deliverable | Present? |
|-----------|---------------------|----------|
| Preamble A → B | Verdict block with (a)–(c) | |
| Preamble B → Phase 1 | Format Contract with both rejection clause types | |
| Phase 1 → Phase 2 | Registry with concrete numeric threshold | |
| Phase 2 → Phase 3 | Binding constraint + causal chain | |
| Phase 3 → Phase 4 | Retry-After check + classified burst path | |
| Phase 4 → Phase 5 | Cascade scenario + two UX tier entries | |
| Phase 5 → Phase 6 | Volume table with 5x arithmetic | |
| Phase 6 → Phase 7 | Mitigation table with arithmetic derivations | |

Flag any missing deliverable as a violation.

**(c) Rejection Clause Audit**: Confirm the Format Contract declares two named clause types (STRUCTURAL and CONTENT) with different detection methods and remediations. If it declares only one combined clause: flag as a Format Contract violation.

**(d) DERIVATION CHAIN Scan**: Identify any DERIVATION CHAIN cell containing only a conclusion without computation steps. Flag each as content-incomplete with table location.

---

## V-04

**Variation axes**: Role sequence (V-01) + output format (V-02) — 11-role pipeline with terminal reconciler (C-24) combined with a Format Contract declaring two-tier violation taxonomy (C-25), full gate chain with explicit deliverable gates on all analysis-body transitions.

**Hypothesis**: When the terminal reconciler (C-24) and the two-tier violation taxonomy (C-25) are combined with a full gate chain (C-21), each mechanism targets a distinct failure mode: the gate chain prevents section skipping, the two-tier taxonomy makes violation detection unambiguous at assessment time (scan vs read), and the terminal reconciler catches revision markers and arithmetic gaps that incomplete per-gate Verdict-currency coverage missed. The three mechanisms reinforce without redundancy — no single mechanism can compensate for the absence of the other two.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across a rate-limited system for the described scenario.

Given: a flow or automation description with request volume, connector and action types, and any known rate limits.

Produce a structured analysis following the 11-role sequence below. **Do not begin a role until all named deliverables from the prior role are written in full.**

---

### ROLE 1 — GLOBAL VERDICT

Write a standalone Verdict block before any rate limit inventory, analysis, or table:

**(a) Binding Constraint**: [Component] — [threshold with unit] — [why this limit binds first]
**(b) Primary Gap**: [Burst path or Retry-After gap] — [failure mode]
**(c) System Status**: SAFE / DEGRADED / FAILING

Label: `VERDICT [pending confirmation]`

---

### ROLE 2 — FORMAT CONTRACT

**Gate: Role 1 Verdict block with fields (a)–(c) written.**

**(a) Table Schema**: `| Component | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |`

**(b) Definitions**:
- **BASELINE**: Current behavior at named component, unmitigated state.
- **PROTECTED**: Behavior at same component after specific named mitigation applied.
- **DERIVATION CHAIN**: Step-by-step computation tracing values to Role 3 registry. Conclusions without steps are content-incomplete.
- **Delta**: Quantified improvement BASELINE → PROTECTED.

**(c) Two-Tier Rejection Clauses** — two named, distinct entries:

**STRUCTURAL REJECTION CLAUSE**
- Covers: required column absent from table structure.
- Detection: scan-time (column header present/absent — no cell reading required).
- Remediation: add the missing column before populating rows.

**CONTENT REJECTION CLAUSE**
- Covers: required column present in structure, but a DERIVATION CHAIN cell contains only a qualitative conclusion without mandated computation steps.
- Detection: read-time (cell content must be read and assessed).
- Remediation: replace conclusion-only cell with step-by-step arithmetic referencing Role 3 values.

A single combined clause covering both types does not satisfy this Format Contract. Both clause types must be named as distinct entries with separate detection methods and separate remediations. At least two comparative tables in this document must comply with the full schema.

**Verdict-currency check**: Does the Format Contract BASELINE definition imply a different System Status than Role 1 field (c)? If yes: insert `[REVISED — see Role 2]` in field (c) now.

---

### ROLE 3 — NUMERIC RATE LIMIT REGISTRY

**Gate: Role 2 Format Contract complete with both rejection clause types declared as named, distinct entries.**

| Limit ID | Component | Limit Type | Threshold | Window | Scope | Source |
|----------|-----------|------------|-----------|--------|-------|--------|

At least one concrete numeric threshold required. Label estimates "(est.)".

**Verdict-currency check**: Does registry reveal different binding constraint than Role 1 field (a)? If yes: insert `[REVISED — see Role 3]` in field (a) now.

---

### ROLE 4 — BINDING CONSTRAINT ANALYSIS

**Gate: Role 3 registry populated with at least one concrete numeric threshold.**

Identify the binding constraint from Role 3. Explicit arithmetic reasoning required — why this limit, not a higher-capacity one, binds first.

**Verdict-currency check**: Does analysis revise field (a)? If yes: insert `[REVISED — see Role 4]` now.

---

### ROLE 5 — CAUSAL CHAIN TO FAILURE MODE

**Gate: Role 4 binding constraint identified with arithmetic reasoning.**

`[Trigger] → [Action/Connector] → [Rate Limit: Limit-ID] → [Platform Response] → [Failure Mode]`

All links explicit. Implied causation does not pass.

**Verdict-currency check**: Does chain reveal different primary gap than field (b)? If yes: insert `[REVISED — see Role 5]` now.

---

### ROLE 6 — RETRY-AFTER HANDLING GAP CHECK

**Gate: Role 5 causal chain fully stated with all links explicit.**

Evaluate per connector and HTTP action. For each gap: flag and state failure mode.

**Verdict-currency check**: Does Role 6 identify more severe primary gap? If yes: insert `[REVISED — see Role 6]` in field (b) now.

---

### ROLE 7 — UNPROTECTED BURST PATH AUDIT

**Gate: Role 6 Retry-After evaluation complete per connector/action.**

Identify at least one structurally unprotected burst path. Classify each:
- **STRUCTURAL**: No mechanism exists on this path.
- **INCIDENTAL**: Mechanism exists but is misconfigured or bypassable under specific conditions.

**Verdict-currency check**: Does audit identify a different or more severe primary gap? If yes: insert `[REVISED — see Role 7]` in field (b) now.

---

### ROLE 8 — CASCADING THROTTLE FAILURE SCENARIO

**Gate: Role 7 burst path audit complete with at least one classified path.**

Cascade scenario where throttling at Tier 1 causally triggers Tier 2 throttle. Causal link explicit. Numeric compounding effect stated.

**Verdict-currency check**: Does cascade scenario change System Status? If yes: insert `[REVISED — see Role 8]` in field (c) now.

---

### ROLE 9 — UX PER THROTTLE TIER

**Gate: Role 8 cascade scenario stated with explicit causal link.**

Four-field template per tier — at least two tiers:

**Tier: [Name]**
| Field | Value |
|-------|-------|
| (a) Error code / platform signal | |
| (b) User-visible behavior | |
| (c) Visibility level | |
| (d) Recovery path available | |

---

### ROLE 10 — VOLUME MAPPING + QUANTIFIED IMPACT + MITIGATIONS

**Gate: Role 9 complete with at least two four-field tier entries.**

**COLUMN COMPLIANCE: Both tables in this role require full schema. Apply STRUCTURAL REJECTION CLAUSE on column check. Apply CONTENT REJECTION CLAUSE to DERIVATION CHAIN cells.**

**10a — Volume-to-Behavior Mapping** (first compliant table):

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|-----------------|-------|
| 1x | | | | |
| 2x | | | | |
| 5x | | | | |

5x BASELINE DERIVATION CHAIN mandatory steps:
1. requests/interval × 5 = peak load
2. peak load − threshold = overflow
3. overflow × retry factor = failed volume
4. failed / peak = failure percentage

5x PROTECTED: same steps with mitigated operands.

**10b — Per-Bottleneck Mitigations** (second compliant table):

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|-----------------|-------|

PROTECTED: specific action/setting/parameter named. BASELINE: current behavior at this component named. DERIVATION CHAIN: arithmetic proving improvement over BASELINE.

**Verdict-currency check**: Does Role 10 mitigation set change System Status under protection? If yes: insert `[REVISED — see Role 10]` in field (c) now.

---

### ROLE 11 — TERMINAL RECONCILER

**Gate: Roles 1–10 fully written.**

Retroactive audit of complete document state. Produce: **Reconciler Findings: [N violations]** or **0 violations**.

**(a) Verdict Revision Scan**: For each Verdict field (a)–(c): confirm it stands as written OR carries `[REVISED — see Role N]`. Flag any revision without marker.

**(b) Gate Deliverable Confirmation**:
| Transition | Required Deliverable | Present? |
|-----------|---------------------|----------|
| Role 1 → 2 | Verdict (a)–(c) | |
| Role 2 → 3 | Format Contract with two named rejection clause types | |
| Role 3 → 4 | Registry with concrete numeric threshold | |
| Role 4 → 5 | Binding constraint with arithmetic reasoning | |
| Role 5 → 6 | Causal chain all links explicit | |
| Role 6 → 7 | Retry-After check per connector/action | |
| Role 7 → 8 | Burst path audit with classified path | |
| Role 8 → 9 | Cascade scenario with causal link | |
| Role 9 → 10 | Two four-field tier entries | |

Flag missing deliverables as violations.

**(c) Format Contract Taxonomy Audit**: Confirm the Format Contract names two distinct rejection clause types — STRUCTURAL and CONTENT — with different detection methods (scan-time vs read-time) and different remediations. If only one combined clause exists: flag as Format Contract taxonomy violation.

**(d) DERIVATION CHAIN Cell Scan**: Flag any DERIVATION CHAIN cell containing only a conclusion without computation steps. Flag each as content-incomplete with table location.

---

## V-05

**Variation axes**: All five — role sequence (11-role full gate chain with terminal reconciler C-24) + output format (two-tier violation taxonomy C-25) + lifecycle emphasis (Verdict-currency check at every role gate, C-22 full compliance) + inertia framing (INERTIA as named competitor column, INERTIA-delta rule) + phrasing register (per-role COLUMN COMPLIANCE annotations preventing false schema violations on non-table roles).

**Hypothesis**: Each axis closes a distinct failure mode: the gate chain blocks section skipping, the two-tier taxonomy makes violation type unambiguous at detection time, per-gate currency checks prevent stale Verdicts at any intermediate state, INERTIA framing forces every DERIVATION CHAIN cell in the mitigation table to prove improvement over the status-quo competitor (not merely demonstrate the protected state's arithmetic), and per-role COLUMN COMPLIANCE annotations prevent the Format Contract's STRUCTURAL REJECTION CLAUSE from generating false violations against roles producing directed hop chains, prose scenarios, or ordered lists that are not comparative tables. Five independent mechanisms, five independent failure modes — the combination achieves structural enforcement that no subset of four can fully replicate.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across a rate-limited system for the described scenario.

Given: a flow or automation description with request volume, connector and action types, and any known rate limits.

Produce a structured analysis following the 11-role sequence below. **Do not begin a role until all named deliverables from the prior role are written in full. Do not cross any gate until the Verdict-currency check for that gate is complete.**

---

### ROLE 1 — GLOBAL VERDICT

Write a standalone Verdict block before any rate limit inventory, analysis, or table:

**(a) Binding Constraint**: [Component] — [threshold with unit] — [why this limit binds before others under described load]
**(b) Primary Gap**: [Burst path or Retry-After gap at named action/connector] — [failure mode]
**(c) System Status**: SAFE / DEGRADED / FAILING — [current state under described load]

Label: `VERDICT [pending confirmation]`

Self-contained. Reader who reads only the Verdict block knows the core finding.

**COLUMN COMPLIANCE: This role produces labeled prose fields, not a comparative table. DERIVATION CHAIN column not required here.**

---

### ROLE 2 — FORMAT CONTRACT

**Gate: Role 1 Verdict block with all three fields (a)–(c) written.**
**Verdict-currency check: Does writing the Format Contract BASELINE definition imply a different System Status framing than field (c)? If yes: insert `[REVISED — see Role 2]` in field (c) now, before proceeding to Role 3.**

**(a) Table Schema**: `| Component | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |`

**(b) Scenario-specific definitions**:
- **INERTIA**: System behavior at the named component in the current unmitigated state — the status-quo competitor. INERTIA is not a neutral baseline; it is the specific behavior being displaced. Every PROTECTED entry must explicitly beat the INERTIA state at this component; a mitigation that does not change the INERTIA condition does not qualify.
- **PROTECTED**: Behavior at the same component after the specific named mitigation is applied.
- **DERIVATION CHAIN**: Step-by-step computation tracing INERTIA and PROTECTED values to Role 3 registry values. INERTIA-delta rule: in the mitigation table, DERIVATION CHAIN cells must show the delta from INERTIA arithmetic — proving the mitigation beats the status-quo competitor. Cells containing only qualitative conclusions or only PROTECTED-state arithmetic without the INERTIA comparison are content-incomplete.
- **Delta**: Quantified improvement INERTIA → PROTECTED expressed as a number or percentage.

**(c) Two-Tier Rejection Clauses** — two named, distinct entries:

**STRUCTURAL REJECTION CLAUSE**
- Covers: required column absent from table structure (INERTIA, PROTECTED, DERIVATION CHAIN, or Delta).
- Detection: scan-time — column header present/absent. No cell content reading required.
- Remediation: add the missing column to table structure before populating rows.

**CONTENT REJECTION CLAUSE**
- Covers: required column present in structure, but a DERIVATION CHAIN cell contains only a qualitative conclusion or PROTECTED-state arithmetic without the mandated INERTIA comparison.
- Detection: read-time — cell content must be read and assessed to determine whether INERTIA-delta computation is present.
- Remediation: replace content-insufficient cell with step-by-step arithmetic showing INERTIA arithmetic, PROTECTED arithmetic, and the INERTIA-delta.

A single combined clause covering both types does not satisfy this contract. Both types must be named as distinct entries with separate detection methods and separate remediations. At least two comparative tables must comply with the full schema.

**COLUMN COMPLIANCE: This role produces a prose format contract, not a comparative table. DERIVATION CHAIN column not required here.**

---

### ROLE 3 — NUMERIC RATE LIMIT REGISTRY

**Gate: Role 2 Format Contract complete — table schema, scenario-specific definitions for INERTIA/PROTECTED/DERIVATION CHAIN, and both named rejection clause types present.**
**Verdict-currency check: Does the registry reveal a binding constraint different from field (a)? If yes: insert `[REVISED — see Role 3]` in field (a) now, before proceeding to Role 4.**

| Limit ID | Component | Limit Type | Threshold | Window | Scope | Source |
|----------|-----------|------------|-----------|--------|-------|--------|

At least one concrete numeric threshold. Label estimates "(est.)". This registry is the arithmetic source for all DERIVATION CHAIN cells.

**COLUMN COMPLIANCE: This role produces a reference registry, not a INERTIA/PROTECTED comparative table. DERIVATION CHAIN column not required here.**

---

### ROLE 4 — BINDING CONSTRAINT ANALYSIS

**Gate: Role 3 registry populated with at least one concrete numeric threshold.**
**Verdict-currency check: Does Role 4 analysis revise the binding constraint in field (a)? If yes: insert `[REVISED — see Role 4]` in field (a) now, before proceeding to Role 5.**

Identify which Role 3 limit is the binding constraint under described load. Explicit arithmetic reasoning required — why this limit, not a higher-capacity one, binds first.

**COLUMN COMPLIANCE: This role produces an ordered analytical list, not a comparative table. DERIVATION CHAIN column not required here. Binding-order rationale serves as the derivation narrative.**

---

### ROLE 5 — CAUSAL CHAIN TO FAILURE MODE

**Gate: Role 4 binding constraint identified with explicit arithmetic reasoning.**
**Verdict-currency check: Does causal chain reveal a different primary gap than field (b)? If yes: insert `[REVISED — see Role 5]` in field (b) now, before proceeding to Role 6.**

`[Trigger] → [Action/Connector] → [Rate Limit: Limit-ID] → [Platform Response] → [Failure Mode]`

All links explicit. Implied causation does not pass.

**COLUMN COMPLIANCE: This role produces a directed hop chain, not a comparative table. DERIVATION CHAIN column not required here.**

---

### ROLE 6 — RETRY-AFTER HANDLING GAP CHECK

**Gate: Role 5 causal chain fully stated with all links explicit.**
**Verdict-currency check: Does Role 6 identify a more severe primary gap than field (b)? If yes: insert `[REVISED — see Role 6]` in field (b) now, before proceeding to Role 7.**

Evaluate per connector and HTTP action: does the flow handle Retry-After headers or equivalent backoff signals (`x-ms-ratelimit-remaining`, `Retry-After-Ms`)? For each gap: flag as a finding and state failure mode.

**COLUMN COMPLIANCE: This role produces a per-connector evaluation list, not a comparative table. DERIVATION CHAIN column not required here.**

---

### ROLE 7 — UNPROTECTED BURST PATH AUDIT

**Gate: Role 6 Retry-After evaluation complete per connector/action.**
**Verdict-currency check: Does Role 7 identify a different or more severe primary gap than field (b)? If yes: insert `[REVISED — see Role 7]` in field (b) now, before proceeding to Role 8.**

| Path | Concurrency Estimate | INERTIA Control State | Gap Type | DERIVATION CHAIN | PROTECTED Control State |
|------|---------------------|----------------------|----------|-----------------|------------------------|

- INERTIA Control State: the current absence of control at this path — named specifically (e.g., "no concurrency cap on For Each action, unbounded parallel branches").
- Gap Type: STRUCTURAL (no mechanism exists) or INCIDENTAL (mechanism exists but is misconfigured/bypassable — state the specific bypass condition).
- DERIVATION CHAIN: estimate of concurrent requests possible under INERTIA, referencing load description and Role 3 limit threshold.
- PROTECTED Control State: the named control that would be applied (anticipates Role 10 mitigations).

**COLUMN COMPLIANCE: REQUIRED — this table uses INERTIA / PROTECTED / DERIVATION CHAIN schema. Apply STRUCTURAL REJECTION CLAUSE on column check.**

---

### ROLE 8 — CASCADING THROTTLE FAILURE SCENARIO

**Gate: Role 7 burst path audit complete with at least one path carrying INERTIA Control State description and Gap Type classification.**
**Verdict-currency check: Does the cascade scenario change System Status or reveal a different primary gap? If yes: insert `[REVISED — see Role 8]` in the relevant field(s) now, before proceeding to Role 9.**

Construct or identify a specific scenario where throttling at one tier causally triggers a second distinct throttle event at a different tier. Causal link explicit. Compounding effect on throughput or error rate stated numerically if possible. Two independent limits under load do not constitute a cascade.

**COLUMN COMPLIANCE: This role produces a prose cascade scenario, not a comparative table. DERIVATION CHAIN column not required here.**

---

### ROLE 9 — UX PER THROTTLE TIER

**Gate: Role 8 cascade scenario stated with explicit causal link.**
**Verdict-currency check: Does the UX analysis reveal user-facing severity that changes System Status in field (c)? If yes: insert `[REVISED — see Role 9]` in field (c) now, before proceeding to Role 10.**

Four-field template per tier — at least two tiers:

**Tier: [Name]**
| Field | Value |
|-------|-------|
| (a) Error code / platform signal | |
| (b) User-visible behavior | |
| (c) Visibility level | user-visible and explicit / silent or background |
| (d) Recovery path available | |

Free prose without template structure does not pass.

**COLUMN COMPLIANCE: Four-field template per tier, not a INERTIA/PROTECTED comparative table. DERIVATION CHAIN column not required here. Template structure is mandatory.**

---

### ROLE 10 — VOLUME MAPPING + QUANTIFIED IMPACT + MITIGATIONS

**Gate: Role 9 complete with at least two full four-field tier entries.**
**Verdict-currency check: Does Role 10 arithmetic or mitigation set change System Status under protection? If yes: insert `[REVISED — see Role 10]` in field (c) now, before proceeding to Role 11.**

**COLUMN COMPLIANCE: Both tables in this role REQUIRE full schema. Apply STRUCTURAL REJECTION CLAUSE on column presence check. Apply CONTENT REJECTION CLAUSE to every DERIVATION CHAIN cell.**

**10a — Volume-to-Behavior Mapping** (first schema-compliant table):

| Volume | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |
|--------|---------|-----------|-----------------|-------|
| 1x | | | | |
| 2x | | | | |
| 5x | | | | |

INERTIA is the status-quo competitor — specific behavior at this load without any mitigation.

5x INERTIA DERIVATION CHAIN — mandatory arithmetic:
1. requests/interval × 5 = peak load
2. peak load − [Limit-ID threshold from registry] = overflow volume
3. overflow × retry factor = failed volume after retries
4. failed / peak = failure percentage
5. [failure_pct]% fail at 5x — INERTIA failure rate

5x PROTECTED DERIVATION CHAIN — mandatory arithmetic (same five steps with mitigated operands):
Show same five steps. Delta cell: [INERTIA failure_pct] − [PROTECTED failure_pct] = [improvement]. This is the INERTIA-delta — proof the mitigation beats the status-quo competitor.

**10b — Per-Bottleneck Mitigations** (second schema-compliant table):

| Finding | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |
|---------|---------|-----------|-----------------|-------|

- INERTIA: specific current behavior at this bottleneck — named to this component's control state.
- PROTECTED: specific action, setting, or parameter being applied — generic advice does not pass.
- DERIVATION CHAIN (INERTIA-delta rule): show INERTIA arithmetic, then PROTECTED arithmetic, then delta. A cell showing only PROTECTED arithmetic without the INERTIA comparison is content-incomplete under the CONTENT REJECTION CLAUSE.
- Delta: [INERTIA metric] − [PROTECTED metric] = [measurable improvement].

---

### ROLE 11 — TERMINAL RECONCILER

**Gate: Roles 1–10 fully written.**
**Verdict-currency check: Does the reconciler uncover any unresolved revision without a marker? Flag as violation if yes.**

Retroactive audit of complete document state. Produce: **Reconciler Findings: [N violations]** or **0 violations**.

**(a) Verdict Revision Scan**

For each Verdict field (a)–(c): confirm it stands as written OR carries `[REVISED — see Role N]` with a forward reference to the revising role. Flag any revised claim without marker as a violation.

**(b) Gate Deliverable Confirmation**

| Transition | Required Deliverable | Present? |
|-----------|---------------------|----------|
| Role 1 → 2 | Verdict (a)–(c) written | |
| Role 2 → 3 | Format Contract: schema, INERTIA-delta rule, two named rejection clause types | |
| Role 3 → 4 | Registry with concrete numeric threshold | |
| Role 4 → 5 | Binding constraint with arithmetic reasoning | |
| Role 5 → 6 | Causal chain all links explicit | |
| Role 6 → 7 | Retry-After check per connector/action | |
| Role 7 → 8 | Burst path audit with INERTIA Control State + Gap Type classification | |
| Role 8 → 9 | Cascade scenario with explicit causal link | |
| Role 9 → 10 | Two four-field UX tier entries | |

Flag any missing deliverable as a violation.

**(c) Format Contract Taxonomy Audit**: Confirm the Format Contract names STRUCTURAL and CONTENT as distinct clause types with different detection methods (scan-time vs read-time) and different remediations. Flag any combined or single-type clause declaration as a violation.

**(d) COLUMN COMPLIANCE Audit**: For each role that declared "COLUMN COMPLIANCE: REQUIRED" — confirm the table is present and contains INERTIA, PROTECTED, DERIVATION CHAIN, and Delta columns. For each role that declared "COLUMN COMPLIANCE: not required here" — confirm no comparative table exists in that role that should have triggered the schema. Flag discrepancies.

**(e) DERIVATION CHAIN INERTIA-Delta Audit**: In all mitigation tables, apply the INERTIA-delta rule: confirm each DERIVATION CHAIN cell shows INERTIA arithmetic, PROTECTED arithmetic, and the delta. Flag any cell containing only PROTECTED-state arithmetic without INERTIA comparison as content-incomplete.

Produce the named finding record. A reconciler that scans without producing a finding record does not satisfy this role.
