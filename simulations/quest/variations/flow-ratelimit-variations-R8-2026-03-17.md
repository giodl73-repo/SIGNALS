Now I have enough context. Writing the 5 variations:

---

## flow-ratelimit Skill — Round 8 Variations (v8 Rubric)

### Variation Axes and Hypotheses

| Variation | Axis | Primary Targets | Predicted Ceiling |
|---|---|---|---|
| V-01 | Role sequence — full gate chain closure | C-15, C-17, C-21, C-22, C-24 | All essential + C-06/07/08 + C-09/10/11/13/15/17/18/21/22/24 |
| V-02 | Output format — Format Contract with two-tier taxonomy | C-16, C-20, C-23, C-25 | All essential + C-06/07/08/09/10 + C-12/14/16/20/23/25 |
| V-03 | Lifecycle emphasis — bidirectional revision + four-field UX | C-18, C-19 | All essential + C-06/07/08 + C-15/17/18/19 |
| V-04 | Phrasing register — commitment-before-evidence, formal/imperative | C-13, C-15 | All essential + C-06/07/08 + C-13/15 + combined |
| V-05 | Inertia framing — INERTIA as structural competitor | C-11, C-12, C-14 | All essential + C-06/07/08/09 + C-11/12/14 + combined |

Single-axis: V-01, V-02, V-03. Combined-ceiling: V-04 (role sequence + commitment register), V-05 (inertia + format contract).

---

## V-01 — Role Sequence: Full Gate Chain Closure

**Axis:** Role sequence — 11 roles execute in strict order; every transition carries explicit gate language naming the prior role's specific deliverables; per-gate Verdict-currency checks embed REVISED markers at the boundary of each revising role; terminal Role 11 audits the complete document state retroactively.

**Hypothesis:** Full gate chain closure (zero ungated boundaries) produces qualitatively stronger structural enforcement than partial gate coverage because any single ungated transition permits selective skipping of intervening deliverables. Per-gate Verdict-currency checks prevent the stale-Verdict failure where REVISED markers are deferred to a closing reconciliation pass. The terminal reconciler adds a second, orthogonal enforcement mechanism — retroactive audit — that catches forward-enforcement gaps.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited integration system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/ratelimit/{{topic}}-ratelimit-{{date}}.md`

Execute the following 11 roles in strict order. Each role states an explicit GATE condition. Do not begin a role until every named deliverable from the prior role is present in the output. Roles that skip gate verification leave ungated boundaries that fail C-21.

---

### ROLE 0 — VERDICT BLOCK

Gate condition: none — this is the opening role.

Write the VERDICT block before any rate limit inventory, burst path table, or volume mapping. The block must be self-contained: a reader who reads only this block must know the core finding without proceeding to evidence.

State:
- **(a) Binding constraint:** component name and numeric threshold that saturates first at `{{topic}}` volume.
- **(b) Primary gap:** the specific unprotected burst path or Retry-After handling failure — name the action or connector.
- **(c) System status at stated load:** SAFE / DEGRADED / FAILING.

Label this section **VERDICT**. It must appear as a standalone named block — not embedded inside an analysis section.

**Gate to ROLE 1:** VERDICT section present as a named standalone block before all other content. All three fields populated with specific component names and numeric or status values. Field (a) includes a rate limit numeric threshold; field (b) names a specific action or connector; field (c) is one of the three status labels.

---

### ROLE 1 — FORMAT CONTRACT

Gate condition: Do not begin ROLE 1 until the VERDICT block is present as a standalone named section with all three fields populated.

Declare the document-wide format contract governing all comparative tables:

**Schema:** BASELINE | PROTECTED | DERIVATION CHAIN

Definitions (scenario-specific, not generic):
- **BASELINE:** The current unprotected system behavior at this volume tier or component, with no throttle protections beyond what is natively present in `{{topic}}`.
- **PROTECTED:** System behavior after the prescribed mitigation for this component or tier is applied.
- **DERIVATION CHAIN:** Step-by-step arithmetic for any quantified cell — at minimum: `requests_per_interval × load_multiplier = peak_load; peak_load − rate_limit = overflow; overflow × retry_factor = failed_requests; failed / peak = failure_pct`. Each step must be shown; a conclusion alone (e.g., "42% fail") without computation steps is a CONTENT violation.

Declare both rejection clause types as distinct named entries:

**STRUCTURAL REJECTION CLAUSE (scan-time):** A required column absent from a table's structure is a structural violation. Detection: scan the table header — no content reading required. Remediation: add the missing column before populating rows. Any table with a missing required column is flagged STRUCTURALLY INCOMPLETE.

**CONTENT REJECTION CLAUSE (read-time):** All required columns present, but a DERIVATION CHAIN cell containing only a conclusion without computation steps is a content violation. Detection: read the cell — judgment about content sufficiency required. Remediation: add the computation chain; the conclusion alone is not sufficient. Any such cell is flagged CONTENT INCOMPLETE.

**Gate to ROLE 2:** Format Contract section present. BASELINE, PROTECTED, and DERIVATION CHAIN declared with scenario-specific definitions. Both STRUCTURAL and CONTENT rejection clauses appear as distinct named entries, each stating its detection method and remediation. Verdict-currency check: if ROLE 1 analysis revises any VERDICT claim, insert "REVISED — see ROLE 1" inline in the VERDICT block before the gate condition is cleared.

---

### ROLE 2 — RATE LIMIT REGISTRY

Gate condition: Do not begin ROLE 2 until ROLE 1 is complete with both rejection clause types present as distinct named entries with detection methods and remediations.

Enumerate every rate limit relevant to `{{topic}}`. This table is non-comparative and exempt from the Format Contract three-column schema.

**TABLE 1 — Rate Limit Registry**

| Component / Connector | Limit Type | Threshold | Unit | Scope | Source |
|---|---|---|---|---|---|
| (exact PA / connector term) | requests / concurrency / burst / queue-depth | (N) | per-minute / per-connection / per-user / per-24h | per-user / per-connection / per-environment / per-tenant | documented / [EST] |

At least one row must cite a concrete numeric threshold without an [EST] label. Limit types must use exact Power Automate or connector documentation terms — generic "API limit" or "service throttle" does not pass.

**Gate to ROLE 3:** TABLE 1 present with at least two rows. At least one row has a numeric threshold without [EST]. All rows have Component, Limit Type, Threshold, Unit, Scope, and Source filled. Verdict-currency check: if ROLE 2 findings revise VERDICT(a), insert "REVISED — see ROLE 2" in the VERDICT block.

---

### ROLE 3 — BINDING CONSTRAINT DETERMINATION

Gate condition: Do not begin ROLE 3 until TABLE 1 is complete per ROLE 2 gate requirements. Confirm the ROLE 2 Verdict-currency check was performed before proceeding.

Identify the binding constraint — the rate limit reached first or most severely at the stated volume. Provide explicit reasoning: why this limit, not a higher-capacity one, is binding at this specific volume and scenario shape. Naming multiple limits without a binding-constraint determination does not satisfy this role.

End with a standalone labeled statement:

**BINDING CONSTRAINT:** [component] — [threshold with unit] — [one-sentence reason why this limit, not another, is the binding one at stated volume]

**Gate to ROLE 4:** BINDING CONSTRAINT labeled statement present. Reasoning precedes the statement and addresses why this specific limit, not alternatives, is binding. Statement names the exact component and numeric threshold from TABLE 1. Verdict-currency check: if ROLE 3 revises VERDICT(a), insert "REVISED — see ROLE 3" inline in the VERDICT block.

---

### ROLE 4 — CAUSAL CHAIN TO FAILURE MODE

Gate condition: Do not begin ROLE 4 until ROLE 3 is complete with the BINDING CONSTRAINT labeled statement present. Confirm the ROLE 3 Verdict-currency check was performed.

Trace the numbered causal chain from the trigger event to the terminal failure mode. Each link must be explicit — implied causation does not pass.

**Causal Chain:**
1. **Trigger:** [the event or action that initiates the request burst in `{{topic}}`]
2. **Action invoked:** [specific connector or action called]
3. **Rate limit encountered:** [component and threshold — use TABLE 1 row]
4. **Backpressure signal emitted:** [HTTP 429 with Retry-After / ActionThrottled event / queue overflow — name the specific signal]
5. **Failure mode:** [retry exhaustion after N attempts / silent drop / flow run failed with specific error — name specifically]

Minimum five links. Generic entries ("the system responds with an error") at any link do not pass — name the specific PA signal, event, or error.

**Gate to ROLE 5:** Numbered causal chain present with at least five links. All links name specific components, signals, or PA-native errors. Failure mode at link 5 is specific. Verdict-currency check: if ROLE 4 revises VERDICT(b) or (c), insert revision marker in VERDICT block before proceeding.

---

### ROLE 5 — BURST PATH AUDIT

Gate condition: Do not begin ROLE 5 until ROLE 4 (Causal Chain) is complete per gate requirements with all five links present.

Identify every unprotected burst path: a trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between the source and the rate-limited endpoint. A path that has throttle controls at a higher tier only does not qualify as unprotected.

**TABLE 2 — Burst Path Register**

| Burst Path | Rate Limit Hit | Protection Gap | Classification |
|---|---|---|---|
| [action or trigger name] | [component + threshold from TABLE 1] | no concurrency cap / no retry policy / no queue buffer — state which is absent | STRUCTURAL / INCIDENTAL |

**STRUCTURAL:** no throttle-control mechanism exists on this path.
**INCIDENTAL:** a mechanism exists but is misconfigured, bypassable, or absent only under specific conditions — state the specific condition.

**Gate to ROLE 6:** TABLE 2 present with at least one entry. Each entry has a Classification with justification. No entry is labeled STRUCTURAL if a mechanism exists (even if misconfigured). Verdict-currency check: if ROLE 5 revises VERDICT(b), insert "REVISED — see ROLE 5" in the VERDICT block.

---

### ROLE 6 — RETRY-AFTER GAP CHECK

Gate condition: Do not begin ROLE 6 until ROLE 5 (Burst Path Audit) is complete with TABLE 2 present per gate requirements.

Evaluate Retry-After header handling (or equivalent signals: `x-ms-ratelimit-remaining`, `Retry-After-Ms`) for each throttled connector or action in `{{topic}}`.

**TABLE 3 — Retry-After Gap Register**

| Connector / Action | Retry-After Emitted? | Retry-After Consumed by Flow? | Gap? | Failure Mode If Gap |
|---|---|---|---|---|
| [name] | yes / no | yes / no / N/A | yes / no | retry-storm / exhaustion after N retries / silent drop / fixed-delay misalignment |

All entries with Gap = yes must name the specific failure mode. If no gap exists for any connector, state explicitly why Retry-After handling is correctly implemented for each.

**Gate to ROLE 7:** TABLE 3 present. At least one row evaluated. All Gap = yes rows have a named failure mode from the allowed types. Verdict-currency check: if ROLE 6 revises VERDICT(b) or (c), insert revision marker in VERDICT block.

---

### ROLE 7 — CASCADING THROTTLE SCENARIO

Gate condition: Do not begin ROLE 7 until ROLE 6 (Retry-After Gap Check) is complete per gate requirements.

Identify or construct a cascade: throttling at Tier A causally triggers throttling at a distinct Tier B. Two independent limits both reached under load do not constitute a cascade — the Tier B throttle must be caused by the Tier A throttle, not merely co-occurring.

**Cascade Profile:**
- **Tier A:** [component] at [threshold] — triggered when: [specific trigger condition at stated volume]
- **Causal mechanism:** [explicit one-sentence statement of how the Tier A throttle generates additional load or constrains flow at Tier B — not implied, not paraphrased]
- **Tier B:** [component] at [threshold] — activated because: [direct causal link from Tier A mechanism]
- **Compounding effect:** [effect on total throughput or error rate when both tiers throttle simultaneously — numeric if possible, qualitative with direction if not]

**Gate to ROLE 8:** Cascade profile present with all four fields. Causal mechanism stated in one explicit sentence (not implied). Tier A and Tier B are distinct components. Verdict-currency check: if ROLE 7 revises VERDICT(c), insert revision marker in VERDICT block.

---

### ROLE 8 — VOLUME-TO-BEHAVIOR MAPPING

Gate condition: Do not begin ROLE 8 until ROLE 7 (Cascading Throttle Scenario) is complete per gate requirements.

Produce the volume-to-behavior mapping using the Format Contract schema (BASELINE | PROTECTED | DERIVATION CHAIN). This is a comparative table — the Format Contract rejection clauses apply.

**TABLE 4 — Volume-to-Behavior Map**

| Volume Tier | BASELINE | PROTECTED | DERIVATION CHAIN |
|---|---|---|---|
| 1× (baseline volume) | [current system behavior, no protections] | [system behavior with mitigations applied] | N/A or qualitative note |
| 2× volume | [escalated current behavior] | [protected behavior at 2×] | arithmetic if quantified |
| 5× volume | [specific failure mode at 5× — name PA errors] | [protected behavior at 5× — name PA feature state] | **REQUIRED: full arithmetic chain** |

For the 5× DERIVATION CHAIN cell: `requests × 5 = peak; peak − rate_limit = overflow; overflow × retry_factor = failed_requests; failed / peak = failure_pct`. A conclusion-only cell is a CONTENT REJECTION CLAUSE violation per the Format Contract declared in ROLE 1.

**Gate to ROLE 9:** TABLE 4 present using BASELINE | PROTECTED | DERIVATION CHAIN schema. Three volume tiers present (1×, 2×, 5×). 5× DERIVATION CHAIN cell contains step-by-step arithmetic. No CONTENT or STRUCTURAL violations in TABLE 4. Verdict-currency check: if ROLE 8 revises VERDICT(c), insert revision marker in VERDICT block.

---

### ROLE 9 — UX TIER ANALYSIS

Gate condition: Do not begin ROLE 9 until ROLE 8 (Volume-to-Behavior Mapping) is complete with TABLE 4 present per gate requirements.

Apply the four-field template to each distinct throttle tier reached in `{{topic}}`. Free prose without the template structure does not satisfy this role even if all four topics are mentioned in narrative form.

For each tier:

**Tier [N] — [Tier name / Component]:**
1. **Platform signal:** [specific error code or PA platform event — e.g., "HTTP 429 with `Retry-After: 60` header returned to HTTP connector", "ActionThrottled event visible in flow run history"]
2. **User-visible behavior:** [what the user observes or experiences — internal system behavior such as queue depth increase is not user experience]
3. **Visibility level:** user-visible and explicit (error surfaced to user) / silent or background (user is unaware the event occurred)
4. **Recovery path:** manual retry available to user / automatic exponential backoff (no user action required) / permanent failure — no recovery path available

Minimum: two tiers using the full four-field template with all fields labeled.

**Gate to ROLE 10:** UX analysis present with at least two tiers. Each tier uses the four-field template with all four fields labeled by number. No tier is described only in free prose without the template structure. Verdict-currency check: if ROLE 9 revises VERDICT(b) or (c), insert revision marker in VERDICT block.

---

### ROLE 10 — MITIGATION PRESCRIPTIONS

Gate condition: Do not begin ROLE 10 until ROLE 9 (UX Tier Analysis) is complete per gate requirements.

For each bottleneck, burst path, and Retry-After gap identified in Roles 5–7, prescribe a concrete remediation using the Format Contract schema.

**TABLE 5 — Mitigation Register**

| Bottleneck / Gap | BASELINE | PROTECTED | DERIVATION CHAIN |
|---|---|---|---|
| [component + gap type from TABLE 2 or TABLE 3] | [specific current before-state: what fails and how at this component] | [specific PA feature, action, or setting changed — exact name required] | [arithmetic for quantified impact; specific action/setting name for qualitative changes] |

Generic advice does not pass. Each PROTECTED cell must name the specific PA native construct (e.g., "enable concurrency control on the Apply to Each action, Degree of Parallelism = 5", "insert a Delay action after the SharePoint connector call, duration from `@outputs('HTTP_connector')?['headers']['Retry-After']`"). Each BASELINE cell must state the specific current failure condition from this scenario — a generic before-state that could apply to any flow does not pass.

**Gate to ROLE 11 (Reconciler):** TABLE 5 present using three-column schema. Each row names a specific PA feature/action/setting in PROTECTED. Each BASELINE cell references a specific current failure condition from this scenario. Verdict-currency check: if ROLE 10 revises any VERDICT claim, insert revision marker in VERDICT block before the gate to ROLE 11 is cleared.

---

### ROLE 11 — TERMINAL RECONCILER

Gate condition: Do not begin ROLE 11 until ROLE 10 (Mitigation Prescriptions) is complete per gate requirements. This is the last named section in the document — no analysis content follows it.

Perform three checks and produce a named finding record:

**(a) Verdict Revision Audit:** Scan the VERDICT block. For each claim in fields (a), (b), (c): determine if any role revised that claim during analysis. For every revised claim, confirm an inline "REVISED — see ROLE N" marker is present in the VERDICT block. List each revised claim without a marker as a violation.

**(b) Gate Deliverable Audit:** For each role transition from ROLE 0→1 through ROLE 10→11: confirm the named deliverables specified in the gate condition are present in the output. List any missing deliverable as a violation with the role boundary it belongs to (e.g., "ROLE 4→5: Numbered causal chain with five links absent — only three links present").

**(c) Derivation Chain Audit:** Scan TABLE 4 (Volume-to-Behavior Map) and TABLE 5 (Mitigation Register). Identify any DERIVATION CHAIN cell that contains only a conclusion without computation steps. List each as a violation with table name and row identifier.

Produce exactly one of:
- **RECONCILER FINDINGS: 0 VIOLATIONS** — document is structurally complete per all gate conditions and Format Contract requirements.
- **RECONCILER FINDINGS: N VIOLATIONS** — followed by an itemized list: `[boundary or table reference] | [violation type: missing deliverable / STRUCTURAL / CONTENT / missing REVISED marker] | [what is absent or incorrect]`

A ROLE 11 section that scans without producing a named finding record (either 0-violations confirmation or itemized list) does not satisfy this role.

---

---

## V-02 — Output Format: Format Contract with Two-Tier Violation Taxonomy

**Axis:** Output format — a Format Contract Preamble appears before any analysis section and declares BASELINE | PROTECTED | DERIVATION CHAIN as a mandatory document-wide schema; the preamble separates STRUCTURAL (scan-time, column absent) and CONTENT (read-time, cell insufficient) rejection clauses as distinct named entries, each with its own detection method and remediation path.

**Hypothesis:** Declaring the dual-column structure as a document-wide contract before sections removes per-section negotiation about whether the schema applies. Separating the two rejection clause types forces the distinction between detection method and remediation: a structural violation (missing column) is detectable without interpretation; a content violation (conclusion without derivation) requires reading the cell. Conflating them into one clause silently permits content violations under the structural remediation path ("add the column"), which doesn't address the cell's content.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited integration system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/ratelimit/{{topic}}-ratelimit-{{date}}.md`

---

### SECTION 0 — FORMAT CONTRACT (write this before any analysis begins)

Before producing any analysis content, declare the following document-wide format contract. This contract applies to every comparative table in the document. Non-comparative tables (rate limit registries, gap checklists) are exempt from the three-column schema but must still be clearly labeled.

**Schema:** All comparative tables use three mandatory columns:

| BASELINE | PROTECTED | DERIVATION CHAIN |
|---|---|---|

**Column definitions (specific to `{{topic}}` — not generic):**

- **BASELINE:** The current state of the system at this component or volume tier in `{{topic}}` with no throttle protections added beyond what is natively present. "Current state" means the observable runtime behavior, not the intended behavior.
- **PROTECTED:** The state of the system at this component or volume tier after the prescribed mitigation for this specific bottleneck is applied. The mitigation must be named in the cell — a general outcome without a named PA feature or action does not qualify as PROTECTED.
- **DERIVATION CHAIN:** For quantified cells — the step-by-step arithmetic showing how the BASELINE and PROTECTED values were derived: `requests_per_interval × load_multiplier = peak; peak − rate_limit = overflow; overflow × retry_factor = failed; failed / peak = failure_pct`. For qualitative rows — the specific action, setting, or configuration change that produces the PROTECTED state. A cell containing only a conclusion ("42% fail", "significantly reduced") without the chain or specific change is a CONTENT violation.

**Rejection clause declarations — two named, distinct types:**

**STRUCTURAL REJECTION CLAUSE**
- *Clause type:* STRUCTURAL
- *Violation:* A required column (BASELINE, PROTECTED, or DERIVATION CHAIN) is absent from the table's column structure.
- *Detection method:* Scan-time — inspect the table header. No content reading required. The violation is visible without reading any cell.
- *Remediation:* Add the missing column to the table structure before populating rows. A table with all cells filled but a missing column header does not satisfy the schema.
- *Flag:* Tables with a missing required column are marked `[STRUCTURALLY INCOMPLETE]` at scan time.

**CONTENT REJECTION CLAUSE**
- *Clause type:* CONTENT
- *Violation:* All required columns are present in the table header, but a DERIVATION CHAIN cell contains only a conclusion without the mandated computation steps or named configuration change.
- *Detection method:* Read-time — the cell content must be read and judged for sufficiency. Detection requires interpretation; a scan of headers is not sufficient to detect this violation.
- *Remediation:* Add the computation chain (each arithmetic step) or named PA change to the cell. The conclusion may remain but must not be the only content.
- *Flag:* Cells with conclusions only are marked `[CONTENT INCOMPLETE]` inline.

A Format Contract that names both clause types but provides the same detection method or remediation for both does not pass. A Format Contract with a single combined clause does not pass even if both violation types are mentioned within it.

At least three distinct comparative tables must appear in this document complying with the declared schema. A Format Contract satisfied by fewer than three compliant tables is incompletely enforced.

---

### SECTION 1 — VERDICT

Write this section immediately after the Format Contract, before any rate limit inventory or burst path audit.

State:
- **(a) Binding constraint:** component name and numeric threshold that will be hit first at `{{topic}}` volume
- **(b) Primary gap:** the unprotected burst path or Retry-After handling failure at a named action or connector
- **(c) System status at stated load:** SAFE / DEGRADED / FAILING

This block is self-contained. A reader who reads only the Verdict block must know the core finding. If any later section revises a claim here, insert "REVISED — see Section N" inline for that specific claim in this block.

---

### SECTION 2 — RATE LIMIT REGISTRY

This table is non-comparative and exempt from the Format Contract three-column schema.

**TABLE 1 — Rate Limit Registry**

| Component / Connector | Limit Type | Threshold | Unit | Scope | Source |
|---|---|---|---|---|---|

At least one row must cite a concrete numeric threshold (not labeled [EST]). Use exact Power Automate and connector documentation terminology for Limit Type.

---

### SECTION 3 — BINDING CONSTRAINT AND CAUSAL CHAIN

**3.A — Binding Constraint**

Identify the rate limit hit first or most severely at `{{topic}}` volume. State explicit reasoning. End with:

**BINDING CONSTRAINT:** [component] — [threshold with unit] — [reason why this limit, not a higher-capacity alternative, is binding at stated volume]

**3.B — Causal Chain to Failure Mode**

Trace the numbered causal chain:

1. Trigger: [event initiating the request burst]
2. Action invoked: [specific connector or action]
3. Rate limit encountered: [TABLE 1 row reference]
4. Backpressure signal: [HTTP 429 / ActionThrottled / queue overflow — name specifically]
5. Failure mode: [retry exhaustion / silent drop / flow run failure — name specifically]

Implied causation at any link does not pass.

---

### SECTION 4 — BURST PATH AUDIT

This table is non-comparative and exempt from the Format Contract schema.

**TABLE 2 — Burst Path Register**

| Burst Path | Rate Limit Hit | Protection Gap | Classification |
|---|---|---|---|
| [action or trigger] | [TABLE 1 reference] | no concurrency cap / no retry policy / no queue buffer | STRUCTURAL / INCIDENTAL |

STRUCTURAL: no mechanism exists on this path.
INCIDENTAL: mechanism exists but is misconfigured or bypassable — state the condition.

---

### SECTION 5 — RETRY-AFTER GAP CHECK

This table is non-comparative and exempt from the Format Contract schema.

**TABLE 3 — Retry-After Gap Register**

| Connector / Action | Retry-After Emitted? | Retry-After Consumed? | Gap? | Failure Mode If Gap |
|---|---|---|---|---|

All Gap = yes rows must name the failure mode. If no gap exists, state why Retry-After is correctly handled for each connector.

---

### SECTION 6 — CASCADING THROTTLE SCENARIO

Identify or construct a cascade where Tier A throttling causally triggers Tier B throttling. Two independent limits co-occurring do not constitute a cascade.

State: Tier A component and threshold → explicit causal mechanism → Tier B component and threshold → compounding effect on throughput or error rate.

---

### SECTION 7 — VOLUME-TO-BEHAVIOR MAPPING

**This table is comparative. The Format Contract schema (BASELINE | PROTECTED | DERIVATION CHAIN) applies. Both rejection clause types are in effect.**

**TABLE 4 — Volume-to-Behavior Map**

| Volume Tier | BASELINE | PROTECTED | DERIVATION CHAIN |
|---|---|---|---|
| 1× (baseline) | [current behavior] | [behavior with mitigations] | N/A or qualitative |
| 2× volume | [escalated current behavior] | [protected behavior] | arithmetic if quantified |
| 5× volume | [specific PA failure mode] | [named PA feature + state] | **Full arithmetic chain required** |

For the 5× DERIVATION CHAIN cell, show every step: `requests × 5 = peak; peak − rate_limit = overflow; overflow × retry_factor = failed; failed / peak = failure_pct`. A cell with the conclusion only is flagged `[CONTENT INCOMPLETE]` per the CONTENT REJECTION CLAUSE.

Both BASELINE and PROTECTED columns in the 5× row must use the same numeric basis derived from TABLE 1 thresholds — not qualitative-only descriptions at the tier where arithmetic is possible.

---

### SECTION 8 — UX PER THROTTLE TIER

For each throttle tier, apply the four-field template:

1. **Platform signal:** [specific error code or PA platform event]
2. **User-visible behavior:** [what the user observes — not internal system state]
3. **Visibility level:** user-visible and explicit / silent or background
4. **Recovery path:** manual retry / automatic backoff / permanent failure — no recovery

Minimum two tiers with the full four-field template applied.

---

### SECTION 9 — MITIGATION PRESCRIPTIONS

**This table is comparative. The Format Contract schema (BASELINE | PROTECTED | DERIVATION CHAIN) applies.**

**TABLE 5 — Mitigation Register**

| Bottleneck / Gap | BASELINE | PROTECTED | DERIVATION CHAIN |
|---|---|---|---|
| [component + gap from TABLE 2 or TABLE 3] | [specific current failure mode at this component] | [exact PA feature, action, or setting — no generic advice] | [arithmetic for quantified; named setting/value for qualitative] |

Generic advice ("add retry logic", "reduce load") does not pass. PROTECTED must name the PA-native construct and the specific configuration (e.g., "concurrency control on Apply to Each action, Degree of Parallelism = 5").

---

### SECTION 10 — FORMAT CONTRACT COMPLIANCE CHECK

Before finalizing output: verify that at least three comparative tables (Sections 7, 9, and one other) use the BASELINE | PROTECTED | DERIVATION CHAIN schema. Identify any table that:

- Is missing a required column → flag as `[STRUCTURALLY INCOMPLETE]` per the STRUCTURAL REJECTION CLAUSE
- Has a DERIVATION CHAIN cell with only a conclusion → flag as `[CONTENT INCOMPLETE]` per the CONTENT REJECTION CLAUSE

Produce: **FORMAT CONTRACT STATUS: COMPLIANT** or **FORMAT CONTRACT STATUS: N VIOLATIONS** with an itemized list of each violation citing clause type (STRUCTURAL / CONTENT), table reference, and what is absent or insufficient.

---

---

## V-03 — Lifecycle Emphasis: Bidirectional Verdict Revision + Four-Field UX Template

**Axis:** Lifecycle emphasis — phases are explicitly bounded with lifecycle semantics (pre-conditions, execution window, post-conditions); each phase carries a revision propagation rule: if Phase N revises a claim from a prior phase, the prior phase is updated with an inline REVISED marker and a forward reference; the UX tier phase receives the heaviest content allocation and enforces a four-field template per tier.

**Hypothesis:** Making the Verdict block self-annotating (REVISED markers pointing forward) means a reader consulting only the Verdict section immediately knows whether it was revised and which phase to consult — without reading every evidence phase. Heavy lifecycle description at phase boundaries forces the analyst to commit to the phase's scope before executing it, preventing scope creep between phases and making boundary violations visible. The four-field UX template at Phase 4 enforces all four UX dimensions per tier — eliminating the single-tier or prose-only pattern that C-03 permits but C-19 rejects.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited integration system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/ratelimit/{{topic}}-ratelimit-{{date}}.md`

**Revision Protocol — read before executing any phase:**
> When any phase produces findings that revise a claim made in a prior phase, the prior phase's section must be updated with an inline revision marker: `[REVISED — see Phase N]` appended to the revised claim, where N is the revising phase number. The revision marker must appear in the prior phase's section itself — not only in the revising phase's section. A reader who reads only Phase 0 must be able to tell from the VERDICT block whether any of its claims were revised and which phase to consult. A Verdict block that was revised but not updated with markers does not satisfy this protocol.

---

### PHASE 0 — VERDICT BLOCK

*Pre-condition:* This phase executes first, before any rate limit enumeration or analysis.
*Execution window:* Write the three verdict claims based on initial assessment — commit to positions before evidence.
*Post-condition:* VERDICT block is a named standalone section before all other phases. If any later phase revises a claim, this section is updated with an inline revision marker per the Revision Protocol.

State:
- **(a) Binding constraint:** component name and numeric threshold expected to saturate first at `{{topic}}` volume
- **(b) Primary gap:** the unprotected burst path or Retry-After handling failure at a named action or connector
- **(c) System status at stated load:** SAFE / DEGRADED / FAILING

These are pre-commitments, not conclusions. State them as analytical positions. Evidence phases that confirm them validate the pre-commitment; evidence phases that revise them update this block per the Revision Protocol.

---

### PHASE 1 — RATE LIMIT INVENTORY

*Pre-condition:* PHASE 0 (VERDICT BLOCK) is complete as a standalone named section.
*Execution window:* Enumerate all rate limits relevant to `{{topic}}`. This phase does not determine binding order — that is Phase 2. Scope is inventory only.
*Post-condition:* TABLE 1 is complete with at least one numeric threshold. If Phase 1 findings revise VERDICT(a) — i.e., if the enumeration reveals a component not considered in the Phase 0 pre-commitment — update the VERDICT block with `[REVISED — see PHASE 1]` on field (a) before proceeding.

**TABLE 1 — Rate Limit Registry**

| Component / Connector | Limit Type | Threshold | Unit | Scope | Source |
|---|---|---|---|---|---|

At least one row has a concrete numeric threshold. Limit types use exact PA / connector documentation terms.

---

### PHASE 2 — BINDING CONSTRAINT AND CAUSAL CHAIN

*Pre-condition:* TABLE 1 (Phase 1) is complete with at least one numeric threshold.
*Execution window:* Determine binding order from TABLE 1 data. Trace the causal chain to failure. These are the two analytical outputs of this phase — neither is optional.
*Post-condition:* BINDING CONSTRAINT statement present. Numbered causal chain with at least five links present. If Phase 2 analysis revises VERDICT(a), update the VERDICT block with `[REVISED — see PHASE 2]` on field (a). If Phase 2 revises VERDICT(b) or (c), update the corresponding field.

**2.A — Binding Constraint**

Identify the rate limit hit first or most severely at `{{topic}}` volume. State explicit reasoning — why this limit, not a higher-capacity alternative, is binding. End with:

**BINDING CONSTRAINT:** [component] — [threshold] — [reason why binding at stated volume]

**2.B — Causal Chain to Failure Mode**

Trace the numbered chain:
1. Trigger event
2. Action or connector invoked
3. Rate limit from TABLE 1 encountered
4. Backpressure signal emitted (name specifically: HTTP 429 with Retry-After / ActionThrottled / queue overflow)
5. Failure mode (name specifically: retry exhaustion / silent drop / flow run failed)

Implied causation does not pass. Each link must name the specific component, signal, or PA error.

---

### PHASE 3 — EXPOSURE ANALYSIS

*Pre-condition:* BINDING CONSTRAINT statement (Phase 2.A) and Causal Chain (Phase 2.B) are both complete.
*Execution window:* Three parallel exposure analyses: burst paths, Retry-After gaps, cascade risk. No binding order within this phase — all three are required.
*Post-condition:* TABLE 2 (burst paths), TABLE 3 (Retry-After gaps), and cascade profile all present. If Phase 3 findings revise any VERDICT claim, update the VERDICT block per the Revision Protocol before proceeding to Phase 4.

**3.A — Burst Path Audit**

**TABLE 2 — Burst Path Register**

| Burst Path | Rate Limit Hit | Protection Gap | Classification |
|---|---|---|---|
| [action or trigger] | [TABLE 1 reference] | no concurrency cap / no retry policy / no queue buffer | STRUCTURAL / INCIDENTAL |

**3.B — Retry-After Gap Check**

**TABLE 3 — Retry-After Gap Register**

| Connector / Action | Retry-After Emitted? | Consumed? | Gap? | Failure Mode |
|---|---|---|---|---|

**3.C — Cascade Risk Profile**

Identify or construct a cascade: Tier A throttling causally triggers Tier B. State Tier A component + threshold, causal mechanism (one explicit sentence), Tier B component + threshold, compounding effect.

---

### PHASE 4 — UX PER THROTTLE TIER

*Pre-condition:* Phase 3 (Exposure Analysis) is complete — TABLE 2, TABLE 3, and cascade profile all present.
*Execution window:* This is the heaviest phase by content allocation. Each distinct throttle tier encountered in `{{topic}}` receives a full four-field template block. Free prose is not permitted as a substitute for the template, even if it covers all four topics.
*Post-condition:* At least two tiers described with the complete four-field template. Every field is labeled by number. If Phase 4 analysis revises VERDICT(b) or (c), update the VERDICT block per the Revision Protocol.

For each distinct throttle tier:

**Tier [N] — [Component Name] — [Throttle Type]:**

1. **Platform signal:** [Exact error code or PA platform event surfaced at this tier — e.g., "HTTP 429 response with `Retry-After: 60` header returned by the SharePoint connector", "ActionThrottled event logged in Power Automate run history for the HTTP action"]
2. **User-visible behavior:** [What the user observes or experiences — not what the system does internally. "Queue depth increased" is not user experience. "User sees the flow run in 'Running' state for 10 additional minutes before completing" is user experience.]
3. **Visibility level:** Choose one:
   - *user-visible and explicit* — an error or warning is surfaced to the user in the flow run result or a notification
   - *silent or background* — the event occurs internally; the user has no direct indication it happened
4. **Recovery path:** Choose one:
   - *Manual retry available* — the user can re-run or re-trigger the flow after the throttle window expires
   - *Automatic exponential backoff* — the flow retries autonomously without user action; the user waits
   - *Permanent failure — no recovery* — the flow run fails and the request is not automatically retried; user must intervene

A tier described in prose paragraphs without all four fields labeled by number does not satisfy the template requirement even if all four topics are present in the prose.

Apply this template to every distinct throttle tier in `{{topic}}`. A minimum of two tiers is required.

---

### PHASE 5 — VOLUME-TO-BEHAVIOR MAPPING AND QUANTIFIED IMPACT

*Pre-condition:* Phase 4 (UX Per Throttle Tier) is complete with at least two tiers using the full four-field template.
*Execution window:* Volume-to-behavior table using two states (BASELINE and PROTECTED) across volume tiers; quantified impact arithmetic for the 5× tier.
*Post-condition:* TABLE 4 present with three volume tiers (1×, 2×, 5×). 5× row has step-by-step arithmetic. If Phase 5 revises any VERDICT claim, update the VERDICT block per the Revision Protocol.

**TABLE 4 — Volume-to-Behavior Map (BASELINE | PROTECTED)**

| Volume Tier | BASELINE | PROTECTED |
|---|---|---|
| 1× (baseline) | [current behavior] | [behavior with mitigations] |
| 2× | [escalated current] | [protected behavior] |
| 5× | [failure mode — name PA error + numeric impact] | [protected behavior — name PA feature + impact] |

For the 5× row, include a **DERIVATION NOTE** below the table showing step-by-step arithmetic:
`requests × 5 = peak; peak − rate_limit = overflow; overflow × retry_factor = failed; failed / peak = failure_pct` — using values from TABLE 1 as the numeric basis.

---

### PHASE 6 — MITIGATION PRESCRIPTIONS

*Pre-condition:* Phase 5 (Volume-to-Behavior Mapping) is complete with TABLE 4 and the 5× DERIVATION NOTE present.
*Execution window:* One mitigation per identified bottleneck or burst path from Phases 2–3. Each mitigation states the explicit before-state (BASELINE in this scenario) and after-state (PROTECTED with this mitigation applied). Generic mitigations that could apply to any flow are not permitted.
*Post-condition:* TABLE 5 present with at least two mitigations, each naming a specific PA feature/action/setting and referencing the specific BASELINE condition being displaced. If Phase 6 revises any VERDICT claim, update the VERDICT block per the Revision Protocol.

**TABLE 5 — Mitigation Register**

| Bottleneck / Gap | BASELINE (before) | PROTECTED (after) | Specific PA Change |
|---|---|---|---|
| [TABLE 2 or TABLE 3 reference] | [current failure condition — specific to this scenario] | [outcome with mitigation applied] | [exact PA feature, action name, setting, and value] |

Generic entries in "Specific PA Change" (e.g., "add retry logic", "batch the requests") do not pass — name the PA-native construct and configuration.

---

### PHASE 7 — REVISION AUDIT

*Pre-condition:* All prior phases (0–6) are complete.
*Execution window:* Scan each prior phase for findings that revised a VERDICT claim. Confirm every such revision has an inline marker in the VERDICT block. This phase produces a revision audit record — it does not add new analysis.
*Post-condition:* Revision audit record present.

For each VERDICT field (a), (b), (c):
- Was the claim from Phase 0 revised by any later phase?
- If yes: is a `[REVISED — see Phase N]` marker present in the VERDICT block for that claim?
- If a marker is missing: flag as REVISION PROTOCOL VIOLATION — field (X) revised by Phase N, marker absent.

Produce: **REVISION AUDIT: COMPLETE — 0 PROTOCOL VIOLATIONS** or **REVISION AUDIT: N VIOLATIONS** followed by an itemized list.

---

---

## V-04 — Phrasing Register: Commitment-Before-Evidence, Formal/Imperative

**Axis:** Phrasing register — all instructions are imperative and state requirements without hedging; the VERDICT block appears literally first in the document as a standalone commitment before any rate limit enumeration, burst path inventory, or volume mapping section; evidence sections that confirm the verdict are labeled confirmations, sections that revise it are labeled revisions with an immediate marker in the Verdict block.

**Hypothesis:** Commitment-before-evidence structure with formal/imperative phrasing forces an analytical position rather than narration toward a conclusion. An analyst asked to state the binding constraint before they have enumerated rate limits must commit to a hypothesis from domain knowledge — which produces a cleaner, more falsifiable claim that the evidence phases either confirm or explicitly revise. Imperative register removes wording that permits optional execution of required deliverables.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited integration system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/ratelimit/{{topic}}-ratelimit-{{date}}.md`

**Mandatory execution rule:** The VERDICT section must appear as the first named section in the document — before any rate limit inventory, cascade analysis, burst path audit, or volume table. State the binding constraint before you enumerate the rate limits that prove it. This forces a commitment; the evidence sections that follow either confirm the commitment or revise it. An analyst who defers the VERDICT until after the evidence is not making a commitment — they are narrating to a conclusion. Do not narrate to a conclusion.

**Per-section revision rule:** When a section produces a finding that revises a VERDICT claim, you must: (1) insert "REVISED — see [Section Name]" inline in the VERDICT section on the revised claim, then (2) continue to the next section. Do not defer revision marking to a closing section.

**Gate rule:** Each section below lists the prior sections whose content must be present before the current section executes. State the gate explicitly. Do not proceed without the named prior deliverable.

---

### VERDICT — BINDING CONSTRAINT, PRIMARY GAP, AND SYSTEM STATUS

*(No prior section required — this is the first section.)*

State three analytical commitments before any evidence:

**(a) Binding constraint:** Name the component and numeric threshold that will saturate first at `{{topic}}` volume. State why this limit, not a higher-capacity alternative, is the binding one — one sentence of reasoning from domain knowledge, before enumeration confirms it.

**(b) Primary gap:** Name the unprotected burst path or Retry-After handling failure and the specific action or connector where it occurs. Commit to the most critical gap — not a list of possibilities.

**(c) System status at stated load:** SAFE / DEGRADED / FAILING. Commit to one status label.

These are pre-commitments, not conclusions. If any subsequent section revises them, this block is updated per the per-section revision rule.

---

### SECTION A — RATE LIMIT REGISTRY

*Gate: VERDICT section present with all three fields (a)(b)(c) populated.*

Enumerate every rate limit relevant to `{{topic}}`.

**TABLE 1 — Rate Limit Registry**

| Component / Connector | Limit Type | Threshold | Unit | Scope | Source |
|---|---|---|---|---|---|

Use exact Power Automate and connector documentation terms for Limit Type. At least one row must state a concrete numeric threshold without an estimate label. Generic terms ("API limit", "service throttle") do not pass.

After completing TABLE 1: if the enumeration reveals a rate limit more constraining than VERDICT(a), update VERDICT(a) with "REVISED — see Section A" and state the corrected binding constraint.

---

### SECTION B — BINDING CONSTRAINT CONFIRMATION

*Gate: TABLE 1 (Section A) present with at least one numeric threshold.*

Using TABLE 1 data, confirm or revise the binding constraint committed in VERDICT(a).

Provide explicit reasoning: at `{{topic}}` volume, which TABLE 1 entry saturates first? Show the comparison: `volume × request_multiplier = generated_requests; compare against rate_limit_threshold`.

**Binding constraint confirmation:** [component] — [threshold] — [arithmetic showing saturation order]

If this analysis revises VERDICT(a): insert "REVISED — see Section B" in the VERDICT block. State the corrected binding constraint in the VERDICT block. Then continue to Section C.

If this confirms VERDICT(a): state "VERDICT(a) confirmed by Section B."

---

### SECTION C — CAUSAL CHAIN TO FAILURE MODE

*Gate: Section B (Binding Constraint Confirmation) present with confirmation or revision statement.*

Trace the numbered causal chain from trigger to failure. Each link must state the specific component, signal, or PA error — implied causation at any link is a structural deficiency.

1. Trigger: [specific event or action in `{{topic}}`]
2. Action invoked: [specific connector or action name]
3. Rate limit hit: [TABLE 1 row — component and threshold]
4. Backpressure signal: [HTTP 429 with Retry-After / ActionThrottled / queue overflow — state the exact PA signal name]
5. Failure mode: [retry exhaustion after N attempts / silent drop / ActionThrottled error — name the PA error]

If the causal chain reveals a failure mode inconsistent with VERDICT(c): insert "REVISED — see Section C" in the VERDICT block and update field (c).

---

### SECTION D — BURST PATH AUDIT

*Gate: Section C (Causal Chain) present with at least five numbered links.*

Identify every structurally unprotected burst path in `{{topic}}`: a trigger or action generating concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between source and the rate-limited endpoint.

**TABLE 2 — Burst Path Register**

| Burst Path | Rate Limit Hit | Protection Gap | Classification |
|---|---|---|---|
| [action or trigger] | [TABLE 1 reference] | no concurrency cap / no retry policy / no queue buffer | STRUCTURAL / INCIDENTAL |

**STRUCTURAL:** No throttle-control mechanism exists on this path.
**INCIDENTAL:** A mechanism exists but is misconfigured, bypassable, or absent under specific conditions — name the condition.

Classify every burst path. A path labeled STRUCTURAL when a mechanism exists (even if insufficient) is a misclassification.

If Section D findings revise VERDICT(b): insert "REVISED — see Section D" in the VERDICT block and update field (b).

---

### SECTION E — RETRY-AFTER GAP CHECK

*Gate: TABLE 2 (Section D) present with at least one entry.*

Determine whether `{{topic}}`'s flow or connectors handle Retry-After signals from throttled endpoints (Retry-After header, `x-ms-ratelimit-remaining`, `Retry-After-Ms`).

**TABLE 3 — Retry-After Gap Register**

| Connector / Action | Retry-After Emitted? | Consumed by Flow? | Gap? | Failure Mode |
|---|---|---|---|---|
| [name] | yes / no | yes / no / N/A | yes / no | retry-storm / exhaustion / silent drop / fixed-delay misalignment |

All Gap = yes rows must name the failure mode. Do not mark a row Gap = no without stating what mechanism correctly handles the Retry-After signal.

If Section E findings revise VERDICT(b): update VERDICT block per per-section revision rule.

---

### SECTION F — CASCADING THROTTLE SCENARIO

*Gate: TABLE 3 (Section E) present with at least one row evaluated.*

Construct or identify a cascade: throttling at one tier causally triggers throttling at a distinct second tier.

State:
- **Tier A:** [component and threshold] — triggered by [specific condition at `{{topic}}` volume]
- **Causal link:** [one explicit sentence — how does Tier A throttling generate the load or constraint that activates Tier B]
- **Tier B:** [component and threshold] — activated because [direct causal consequence of Tier A state]
- **Compounding effect:** [quantified impact on throughput or error rate when both tiers are throttling simultaneously]

Two independent limits both hit under load do not constitute a cascade. State the mechanism explicitly — do not imply it.

---

### SECTION G — VOLUME-TO-BEHAVIOR MAPPING

*Gate: Section F (Cascading Throttle Scenario) present with Tier A, Tier B, causal link, and compounding effect all stated.*

Map volume tiers to throttle behavior. Use columns: VOLUME TIER | BASELINE | PROTECTED.

For the 5× tier: show step-by-step arithmetic in a DERIVATION NOTE below the table: `requests × 5 = peak; peak − rate_limit = overflow; overflow × retry_factor = failed; failed / peak = failure_pct` — using TABLE 1 values as the numeric basis.

**TABLE 4 — Volume-to-Behavior Map**

| Volume Tier | BASELINE | PROTECTED |
|---|---|---|
| 1× baseline | [current behavior] | [with mitigations] |
| 2× | [escalated current behavior] | [protected behavior] |
| 5× | [specific PA failure mode + numeric] | [named PA protection + numeric] |

**5× DERIVATION NOTE:** [step-by-step arithmetic here]

---

### SECTION H — UX PER THROTTLE TIER

*Gate: TABLE 4 (Section G) present with three volume tiers including 5× DERIVATION NOTE.*

Apply the four-field template to each distinct throttle tier. Free prose without the template does not pass.

**Tier [N] — [Component]:**
1. **Platform signal:** [specific PA error code or event name]
2. **User-visible behavior:** [what the user observes — not internal system state]
3. **Visibility level:** user-visible and explicit / silent or background
4. **Recovery path:** manual retry / automatic backoff / permanent failure — no recovery

Minimum: two tiers with the full four-field template applied.

---

### SECTION I — MITIGATION PRESCRIPTIONS

*Gate: Section H (UX Per Throttle Tier) present with at least two tiers using the four-field template.*

For each burst path (TABLE 2) and Retry-After gap (TABLE 3), prescribe a concrete remediation. State the specific before-state (BASELINE — the current failure condition in `{{topic}}`) and after-state (PROTECTED — the PA-native feature and configuration applied). Generic advice does not pass.

**TABLE 5 — Mitigation Register**

| Bottleneck / Gap | BASELINE | PROTECTED | PA Feature + Configuration |
|---|---|---|---|
| [TABLE 2 or TABLE 3 reference] | [current failure condition, specific to this scenario] | [outcome with mitigation] | [exact PA construct name + setting + value] |

Each PROTECTED cell must name the PA-native construct. Each BASELINE cell must reference a specific failure condition from `{{topic}}` — not a description applicable to any system.

---

### SECTION J — VERDICT CONFIRMATION

*Gate: All sections A–I complete.*

Review the VERDICT block. For each claim (a), (b), (c):
- Was the pre-commitment from the VERDICT section confirmed or revised by any section?
- Is a REVISED marker present in the VERDICT block for every revised claim?
- Is the revised claim's wording in the VERDICT block accurate (reflecting the latest finding, not the original pre-commitment)?

Produce: **VERDICT STATUS: CONFIRMED** (all three claims confirmed by evidence) or **VERDICT STATUS: REVISED** (one or more claims revised — list each with the section that revised it and whether the REVISED marker was correctly inserted).

A VERDICT block that was revised but not updated with markers, or where the claim's wording was not corrected after revision, is a protocol violation.

---

---

## V-05 — Inertia Framing: INERTIA as Structural Competitor + Baseline-Delta Mitigations

**Axis:** Inertia framing — the current unprotected system state is named INERTIA and appears as a structural competitor in every comparative table; the INERTIA state is the baseline against which all mitigations are measured; each mitigation must displace the named INERTIA condition — a mitigation that cannot state what INERTIA condition it displaces is rejected; burst path classification distinguishes structural INERTIA (no mechanism exists) from incidental INERTIA (mechanism exists but inactive or misconfigured).

**Hypothesis:** Naming the status quo as a competitor forces mitigations to prove they move the needle from the specific INERTIA condition — generic advice ("add retry logic") is structurally rejected because it cannot name the INERTIA state it displaces. The dual-column structure (INERTIA vs. PROTECTED) at every volume tier surfaces the concrete cost of inaction, which is often omitted in analyses that present mitigations without a counterfactual. Burst gap classification as structural vs. incidental INERTIA makes the remediation path explicit: structural INERTIA requires adding a mechanism; incidental INERTIA requires activating or correcting one.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited integration system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/ratelimit/{{topic}}-ratelimit-{{date}}.md`

**INERTIA framing rule:** Throughout this document, the current unprotected state of `{{topic}}` is referred to as the **INERTIA state** — the outcome if no throttle protections are added or corrected beyond what is natively present. Every comparative table shows INERTIA and PROTECTED as columns. Every mitigation identifies the INERTIA condition it replaces. A mitigation that cannot name the specific INERTIA condition in `{{topic}}` that it displaces is rejected as generic advice.

**Burst gap framing rule:** Every unprotected burst path is classified as:
- **STRUCTURAL INERTIA:** No throttle-control mechanism exists on this path in `{{topic}}` — adding it requires creating a new PA construct.
- **INCIDENTAL INERTIA:** A mechanism exists in `{{topic}}` but is misconfigured, inactive, or absent only under specific conditions — correcting it requires activating or reconfiguring an existing PA construct.

The classification determines the remediation type. A STRUCTURAL INERTIA gap requires a different remediation than an INCIDENTAL INERTIA gap.

---

### SECTION 1 — VERDICT

State:
- **(a) Binding constraint:** component name and numeric threshold expected to saturate first at `{{topic}}` volume — and what the INERTIA system experiences when it does
- **(b) Primary gap:** the most critical INERTIA state — structural or incidental — at a named action or connector
- **(c) INERTIA system status at stated load:** SAFE / DEGRADED / FAILING

If any subsequent section revises a claim here, insert "REVISED — see Section N" inline on the revised claim.

---

### SECTION 2 — RATE LIMIT REGISTRY

**TABLE 1 — Rate Limit Registry**

| Component / Connector | Limit Type | Threshold | Unit | Scope | INERTIA Exposure |
|---|---|---|---|---|---|
| [exact PA / connector term] | [type] | [N] | [unit] | [scope] | [what happens in INERTIA state when this limit is hit — specific to `{{topic}}`] |

At least one row has a concrete numeric threshold. The INERTIA Exposure column must describe what the INERTIA state experiences — not what a protected system would do. "Flow run fails with ActionThrottled" is an INERTIA exposure; "would be mitigated by retry logic" is not.

---

### SECTION 3 — BINDING CONSTRAINT AND CAUSAL CHAIN

**3.A — Binding Constraint**

From TABLE 1, identify the rate limit the INERTIA system hits first at `{{topic}}` volume. Show the saturation arithmetic: `volume × request_multiplier = generated_requests; compare against threshold`.

**INERTIA BINDING CONSTRAINT:** [component] — [threshold] — [arithmetic showing saturation order at stated volume]

**3.B — Causal Chain (INERTIA System)**

Trace the numbered causal chain in the INERTIA state — what happens in `{{topic}}` with no additional protections:

1. Trigger: [event]
2. Action invoked: [connector or action]
3. Rate limit hit: [TABLE 1 row]
4. Backpressure signal: [specific PA signal]
5. INERTIA failure mode: [specific PA error or failure behavior]

This is the INERTIA causal chain. It describes what happens now — not what happens after mitigations are applied.

---

### SECTION 4 — BURST PATH AUDIT (INERTIA CLASSIFICATION)

Identify every burst path in `{{topic}}` where the INERTIA state has no effective throttle protection. For each:

**TABLE 2 — Burst Path Register**

| Burst Path | Rate Limit Hit | INERTIA Protection Gap | INERTIA Classification | Remediation Type |
|---|---|---|---|---|
| [action or trigger] | [TABLE 1 ref] | [no concurrency cap / no retry / no queue buffer — what is absent] | STRUCTURAL INERTIA / INCIDENTAL INERTIA | Add mechanism (structural) / Correct mechanism (incidental) |

**STRUCTURAL INERTIA:** No PA throttle-control mechanism exists on this path — the INERTIA system has no construct that could limit concurrent requests or enforce backoff here. Remediation type: add a new PA construct.

**INCIDENTAL INERTIA:** A PA mechanism exists on this path but is inactive, misconfigured, or bypassed under conditions present in `{{topic}}`. Remediation type: correct or activate the existing construct. Name the specific condition that makes it inactive.

Do not classify a path as STRUCTURAL INERTIA if any mechanism exists, even if insufficient.

---

### SECTION 5 — RETRY-AFTER GAP CHECK

**TABLE 3 — Retry-After Gap Register**

| Connector / Action | Retry-After Emitted? | INERTIA Consumption? | INERTIA Gap? | INERTIA Failure Mode |
|---|---|---|---|---|
| [name] | yes / no | INERTIA state: yes / no | yes / no | retry-storm / exhaustion after N retries / silent drop / fixed-delay misalignment |

The INERTIA Consumption and INERTIA Failure Mode columns describe the current state in `{{topic}}` — not what a protected system would do. A row where INERTIA Gap = no must state why the INERTIA system correctly handles the signal.

---

### SECTION 6 — CASCADING THROTTLE SCENARIO (INERTIA SYSTEM)

In the INERTIA state of `{{topic}}`, identify or construct a cascade: Tier A throttling causally triggers Tier B.

State:
- **Tier A:** [component + threshold in INERTIA state] — triggered by [condition]
- **Causal mechanism:** [explicit one-sentence statement]
- **Tier B:** [component + threshold] — activated because [direct causal consequence]
- **INERTIA compounding effect:** [impact on throughput or error rate in the INERTIA system when both tiers throttle]

The cascade describes what happens in `{{topic}}` today — without interventions.

---

### SECTION 7 — VOLUME-TO-BEHAVIOR MAPPING (INERTIA vs. PROTECTED)

Map behavior across volume tiers in both INERTIA and PROTECTED states. Every tier shows the cost of remaining in INERTIA.

**TABLE 4 — Volume-to-Behavior Map**

| Volume Tier | INERTIA | PROTECTED | INERTIA Cost |
|---|---|---|---|
| 1× baseline | [INERTIA behavior] | [PROTECTED behavior] | [what INERTIA loses vs PROTECTED at this tier] |
| 2× | [escalated INERTIA] | [PROTECTED behavior] | [INERTIA cost at 2×] |
| 5× | [INERTIA failure mode + arithmetic] | [PROTECTED behavior + arithmetic] | [INERTIA cost at 5×] |

For the 5× row: show step-by-step arithmetic in **both** INERTIA and PROTECTED cells:
- INERTIA 5×: `requests × 5 = peak; peak − rate_limit = overflow; overflow × retry_factor = failed; failed / peak = failure_pct`
- PROTECTED 5×: `peak − [mitigated effective limit] = reduced_overflow; reduced_overflow × [mitigated retry factor] = failed; failed / peak = protected_failure_pct`

Use TABLE 1 numeric values as the arithmetic basis. A conclusion-only cell for the 5× row does not pass.

---

### SECTION 8 — UX PER THROTTLE TIER

Apply the four-field template to each distinct throttle tier in `{{topic}}`. For each tier, note whether the experience differs between INERTIA and PROTECTED states.

**Tier [N] — [Component] — INERTIA vs. PROTECTED:**

1. **Platform signal:** [specific error code or PA event in INERTIA state] / [in PROTECTED state: same signal or different?]
2. **User-visible behavior:** [INERTIA: what user observes] / [PROTECTED: what user observes — does the UX improve?]
3. **Visibility level:** [INERTIA: user-visible and explicit / silent or background] / [PROTECTED: same or changed?]
4. **Recovery path:** [INERTIA: manual retry / automatic backoff / permanent failure] / [PROTECTED: does the recovery path change?]

Minimum: two tiers with the full four-field template applied to both INERTIA and PROTECTED states.

---

### SECTION 9 — MITIGATION PRESCRIPTIONS (INERTIA-DELTA)

For each INERTIA burst gap (TABLE 2) and Retry-After gap (TABLE 3), prescribe a concrete remediation that displaces the named INERTIA condition.

**TABLE 5 — Mitigation Register**

| INERTIA Condition | INERTIA State | PROTECTED State | PA Construct + Configuration | INERTIA Delta |
|---|---|---|---|---|
| [TABLE 2 or TABLE 3 reference] | [specific current failure — what INERTIA does at this bottleneck in `{{topic}}`] | [behavior after mitigation — what changes] | [exact PA feature, action, setting, and value — no generic advice] | [delta: what moves from INERTIA to PROTECTED — quantified if possible] |

**INERTIA Delta column requirement:** Each row must state what specifically changes — a numeric improvement, a failure mode eliminated, or a recovery path gained. "Improved resilience" without a named change does not satisfy the INERTIA Delta. A mitigation whose PROTECTED state is not distinguishable from the INERTIA state in this scenario is a non-mitigation.

**Generic advice rejection:** Each PA Construct + Configuration cell must name the specific PA construct (exact name from Power Automate documentation) and the specific configuration value (e.g., "Apply to Each concurrency control, Degree of Parallelism = 5", not "add concurrency control"). A cell without an exact PA construct name and configuration value is flagged as generic advice and does not pass.

For each STRUCTURAL INERTIA gap: the mitigation adds a new PA construct — name the construct and where in the flow it is added.

For each INCIDENTAL INERTIA gap: the mitigation corrects or activates an existing construct — name the construct, the current (INERTIA) misconfiguration, and the corrected value.

---

### SECTION 10 — INERTIA COST SUMMARY

Produce a final summary of the cost of remaining in the INERTIA state across all identified gaps:

**TABLE 6 — INERTIA Cost Summary**

| Gap | INERTIA Failure Mode | PROTECTED Outcome | INERTIA Delta | Priority |
|---|---|---|---|---|
| [from TABLE 2 or TABLE 3] | [specific failure in INERTIA state] | [specific outcome in PROTECTED state] | [quantified or named delta] | HIGH / MEDIUM / LOW |

Priority is determined by: (1) severity of INERTIA failure mode, (2) frequency of trigger condition in `{{topic}}`, (3) user-visibility of the failure. State the basis for the priority assignment in one sentence.

This section answers: "What happens if the team does nothing?" for every gap identified. A gap without a named INERTIA failure mode does not have a cost — reconsider whether it is a real gap.

---
