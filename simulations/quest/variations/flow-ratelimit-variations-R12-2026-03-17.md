# flow-ratelimit — Quest Variate R12 (V-01 through V-05)

---

## V-01 — Role Sequence Axis
**Hypothesis:** A complete numbered role sequence where every transition is gated by named prior-section deliverables, a dedicated pre-reconciler role sweeps deferred revision markers before the terminal reconciler, and the terminal reconciler separately names all four audit checks produces higher enforcement coverage than any partial implementation.

---

```markdown
# flow-ratelimit — Rate Limit Throughput Analysis

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the topic. For the given request volume,
trace where bottlenecks occur, which rate limits are hit first, how backpressure
propagates, and what the user experience is at each throttle tier.

Execute the following 11 roles in strict sequence.
**Do not begin Role N until all named deliverables from Role N-1 are written.**

---

## ROLE 0 — VERDICT BLOCK

**Gate in:** None — this role opens the document.
**Gate out:** Do not begin Role 1 until this block contains all four claims:
(a) binding constraint — component name + numeric threshold + interval + scope
(b) primary gap — unprotected burst path at a named action OR Retry-After not
    handled at a named connector
(c) system status at the stated load: SAFE / DEGRADED / FAILING
(d) UX completeness commitment — total tier count + confirmation that all tiers
    will use the Schema B four-field template

Produce a standalone VERDICT block. A reader who reads only this block must
know the core finding without proceeding to the evidence.

```
VERDICT
(a) Binding constraint: [component name] — [N req / M seconds / scope]
(b) Primary gap: [description — must name action or connector]
(c) System status at [stated load]: SAFE / DEGRADED / FAILING
(d) UX completeness: [N] throttle tiers — all tiers use Schema B four-field template
```

When any evidence role revises a Verdict claim, insert an inline revision marker
in this block: `REVISED — see Role N`. A Verdict block revised by evidence but
not updated with markers fails the terminal reconciler.

---

## ROLE 1 — FORMAT CONTRACT

**Gate in:** VERDICT block with all four claims (a)–(d) present.
**Gate out:** Do not begin Role 2 until both schemas are declared and all four
rejection clauses are named with detection methods and remediations.

Declare the document-wide format contract. Every comparative table and UX tier
block in this document is governed by this contract.

### Schema A — Comparative Table

Every comparative table must include these three columns:
- **BASELINE**: current system behavior at this volume — unprotected state
- **PROTECTED**: system behavior with the specific mitigations named in this
  analysis applied — cells must reference the specific component and setting changed
- **DERIVATION CHAIN**: computation steps linking registry values to the stated
  outcome — not a conclusion alone

### Schema B — UX Tier Template

Every throttle tier block must contain all four labeled fields:

```
ERROR SIGNAL:        [HTTP status code or platform event]
USER-VISIBLE BEHAVIOR: [what the user observes or experiences]
VISIBILITY LEVEL:    EXPLICIT (user sees error) | SILENT (background, user unaware)
RECOVERY PATH:       [manual retry / auto backoff with Retry-After / queued with
                      delay notification / permanent failure — no recovery]
```

### Four Rejection Clauses

**SCHEMA A — STRUCTURAL REJECTION CLAUSE**
- Clause type: STRUCTURAL
- Detection: SCAN-TIME — are BASELINE, PROTECTED, and DERIVATION CHAIN each present
  as column headers?
- Violation: any required column header absent from table structure
- Remediation: add the missing column header; populate all cells before proceeding

**SCHEMA A — CONTENT REJECTION CLAUSE**
- Clause type: CONTENT
- Detection: READ-TIME — does the DERIVATION CHAIN cell contain computation steps
  or only a conclusion?
- Violation: a DERIVATION CHAIN cell contains only a numerical conclusion without
  intermediate computation steps
- Remediation: expand the cell to show the chain referencing specific registry values

**SCHEMA B — STRUCTURAL REJECTION CLAUSE**
- Clause type: STRUCTURAL
- Detection: SCAN-TIME — count field labels present in the tier block
- Violation: one or more of the four field labels absent from a tier block
- Remediation: add the missing label(s) and populate the field

**SCHEMA B — CONTENT REJECTION CLAUSE**
- Clause type: CONTENT
- Detection: READ-TIME — is each field cell substantive and specific to this tier,
  or generic and applicable to any throttle scenario?
- Violation: a field cell contains boilerplate or non-specific text
- Remediation: replace with tier-specific content referencing the component name,
  observed platform event, or specific behavior at this tier

---

## ROLE 2 — RATE LIMIT REGISTRY

**Gate in:** Format Contract with both schemas and all four rejection clauses declared.
**Gate out:** Do not begin Role 3 until the registry contains at least one rate
limit with: component name, numeric threshold, interval, scope (connector-level /
action-level / platform-level / environment-level), and explicit differentiation from
adjacent tiers it could be confused with.

Enumerate the rate limits in scope as a named registry.

| COMPONENT | THRESHOLD | INTERVAL | SCOPE | TIER TYPE |
|-----------|-----------|----------|-------|-----------|
| [name] | [N req] | [per M sec] | [level] | connector-level / platform-level |

Explicitly separate connector-level limits (enforced by the external service or
connector SDK) from platform-level limits (enforced by Power Automate run concurrency
or action throughput). Treating them as a single undifferentiated category fails
the essential correctness check.

**Verdict currency check:** If the registry reveals the binding constraint in
VERDICT (a) requires revision, insert `REVISED — see Role 2` in VERDICT (a) now.

---

## ROLE 3 — BURST PATH AUDIT

**Gate in:** Rate Limit Registry with at least one fully enumerated limit
(name + threshold + interval + scope + differentiation).
**Gate out:** Do not begin Role 4 until the audit includes at least one
structurally unprotected burst path with all four fields, and explicit
structural-vs-incidental classification for each gap.

Audit all trigger and action paths that generate concurrent requests.

| PATH | CONCURRENCY CAP | RETRY POLICY | QUEUE BUFFER | GAP TYPE |
|------|-----------------|--------------|--------------|----------|
| [name] | None / [limit] | None / [policy] | None / [buffer] | STRUCTURAL / INCIDENTAL |

- **STRUCTURAL**: no mechanism exists on this path
- **INCIDENTAL**: mechanism exists but is misconfigured, bypassable, or absent only
  under specific conditions — state the condition

A path that has throttle controls at a higher tier does not qualify as unprotected
at this path level.

**Verdict currency check:** If burst path count or primary gap identification requires
revising VERDICT (b) or VERDICT (d), insert REVISED marker(s) now.

---

## ROLE 4 — CASCADING FAILURE SCENARIO

**Gate in:** Burst path audit table with at least one classified gap.
**Gate out:** Do not begin Role 5 until the scenario names a specific two-tier
cascade: throttle event at Tier 1 → causal mechanism → throttle event at Tier 2,
with compounding effect stated.

| STAGE | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------|----------|-----------|------------------|
| Tier 1 throttle | [behavior at first limit] | [protected behavior] | [math: volume → limit exceeded → event] |
| Causal mechanism | [how Tier 1 reaches Tier 2] | [protected path] | [retry volume or queue depth generated] |
| Tier 2 throttle | [compounding effect] | [protected behavior] | [math: retry storm → second threshold] |

Two limits independently reached under load do not constitute a cascade. The
second throttle must be causally triggered by the first.

**Verdict currency check:** Insert any required REVISED markers now.

---

## ROLE 5 — RETRY-AFTER GAP ANALYSIS

**Gate in:** Cascading failure scenario with two-tier causal chain documented.
**Gate out:** Do not begin Role 6 until every rate-limited endpoint in the
registry has been evaluated for Retry-After handling, with a failure mode named
for each gap.

| ENDPOINT | RETRY-AFTER HANDLED? | FAILURE MODE IF MISSING |
|----------|---------------------|------------------------|
| [component] | YES / NO | [immediate retry storm / perm failure / silent discard] |

Evaluate Retry-After (or equivalents: `x-ms-ratelimit-remaining`, `Retry-After-Ms`).
Missing handling is a named finding with stated failure mode.

**Verdict currency check:** Insert any required REVISED markers now.

---

## ROLE 6 — UX PER THROTTLE TIER

**Gate in:** Retry-After gap analysis with named findings for each missing handler.
**Gate out — six-item gate, all must be satisfied before Role 7 begins:**
(a) ERROR SIGNAL present and substantively populated for every tier described
(b) USER-VISIBLE BEHAVIOR present and substantively populated for every tier described
(c) VISIBILITY LEVEL present and substantively populated for every tier described
(d) RECOVERY PATH present and substantively populated for every tier described
(e) Tier count verified against Role 3 burst path audit — NOT against VERDICT (d)
(f) Structure compliance confirmed: each tier uses Schema B template, not free prose

Apply the Schema B four-field template to every throttle tier. At minimum two tiers.

```
TIER [N] — [component name + platform event]
ERROR SIGNAL:          [specific HTTP code / platform event for this tier]
USER-VISIBLE BEHAVIOR: [specific to this tier's error mode and platform]
VISIBILITY LEVEL:      EXPLICIT / SILENT
RECOVERY PATH:         [specific to this tier's recovery options]
```

**Verdict currency check:** If tier count differs from VERDICT (d), insert
`REVISED — see Role 6` in VERDICT (d) now.

---

## ROLE 7 — MITIGATION PRESCRIPTIONS

**Gate in:** UX tier section with six-item gate satisfied.
**Gate out:** Do not begin Role 8 until every bottleneck and Retry-After gap has a
prescription naming the specific action, setting, or pattern — with both before-state
and after-state stated for each.

| BOTTLENECK | BASELINE | PROTECTED | DERIVATION CHAIN |
|------------|----------|-----------|------------------|
| [component + limit] | [specific before-state — this scenario] | [specific after-state — named setting or pattern] | [why this mitigation changes the state — formula or logic] |

Generic advice ("add retry logic") fails. Name the specific action, setting, or
pattern. The baseline must be specific to this scenario's components.

**Verdict currency check:** Insert any required REVISED markers now.

---

## ROLE 8 — QUANTIFIED IMPACT AT LOAD SPIKE

**Gate in:** Mitigation prescriptions table with BASELINE, PROTECTED, and DERIVATION
CHAIN populated for all bottlenecks.
**Gate out:** Do not begin Role 9 until the impact table contains at least one load
spike cell with step-by-step arithmetic referencing registry values from Role 2.

| VOLUME TIER | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------------|----------|-----------|------------------|
| [Nx load] | [failure rate / queue depth] | [protected metrics] | Step 1: [req/interval] × [N] = [peak] Step 2: [peak] − [limit] = [overflow] Step 3: [overflow] × [retry factor] = [failed] Step 4: [failed] ÷ [peak] = [failure %] |

A DERIVATION CHAIN cell with only "X% fail" without computation steps is a
Schema A CONTENT VIOLATION.

**Verdict currency check:** Insert any required REVISED markers now.

---

## ROLE 9 — PRE-RECONCILER VERDICT CURRENCY SWEEP

**Gate in:** Quantified impact table with at least one fully derived load spike cell.
**Gate out:** Do not begin Role 10 until the sweep has checked all prior roles and
produced a named finding record.

Retroactively sweep all prior sections (Roles 2–8) for REVISED markers that should
have been inserted at gate boundaries but were deferred.

For each prior role:
- Was a revision triggered by that role's findings?
- Is the corresponding REVISED marker present in the Verdict block?
- If not: insert the marker now, annotated as: `REVISED (deferred from Role N) — see Role N`

This sweep separates correction from verification. The terminal reconciler confirms
that markers are correctly placed — it does not discover and insert them. A document
that defers all insertions to Role 10 has no independent verification that Role 10
itself executed correctly.

**Pre-Reconciler Sweep Output:**
```
Deferred markers inserted: [0 / itemized list of Role N → Verdict claim]
All Verdict claims now current: [YES / list any remaining gaps]
```

---

## ROLE 10 — TERMINAL RECONCILER (FOUR-CHECK AUDIT)

**Gate in:** Pre-reconciler sweep output with named finding record produced.
**Gate out:** None — this is the final section.

Perform four separately enumerated audit checks. Each produces a named finding record.

**(a) VERDICT MARKER AUDIT**
Scan the Verdict block. For each claim (a)–(d): was this claim revised by any
analysis role? If yes, is an inline REVISED marker with forward reference to the
revising role present?
`Verdict marker audit: [0 violations / itemized list]`

**(b) GATE DELIVERABLE AUDIT**
For each role transition (Roles 1–9), enumerate the named prior-section deliverables
and confirm each is present in the document.
`Gate deliverable audit: [0 violations / itemized list]`

**(c) SCHEMA A CONTENT AUDIT (DERIVATION CHAIN)**
Scan every DERIVATION CHAIN cell in all Schema A tables (Roles 3, 4, 7, 8). Flag
any cell containing only a conclusion without computation steps as a Schema A
CONTENT VIOLATION.
`Schema A content audit: [0 violations / itemized list]`

**(d) SCHEMA B STRUCTURAL SCAN**
Scan every UX tier block in Role 6. Confirm each contains all four field labels:
ERROR SIGNAL, USER-VISIBLE BEHAVIOR, VISIBILITY LEVEL, RECOVERY PATH. Flag any
tier block missing one or more labels as a Schema B STRUCTURAL VIOLATION.
`Schema B structural scan: [0 violations / itemized list]`

**Reconciler Summary:**
```
(a) Verdict marker audit:   [result]
(b) Gate deliverable audit: [result]
(c) Schema A content audit: [result]
(d) Schema B structural:    [result]
Overall: CLEAN / [N violations — see items above]
```
```

---

## V-02 — Output Format Axis
**Hypothesis:** Declaring Schema A and Schema B as co-equal named structural contracts — each with its own STRUCTURAL and CONTENT rejection clause (four clauses total), with DERIVATION CHAIN as a mandatory schema column — produces scan-time detectability of violations that prose-level enforcement clauses cannot achieve.

---

```markdown
# flow-ratelimit — Rate Limit Throughput Analysis

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system in the topic. Trace bottlenecks, identify which limits
are hit first, describe backpressure propagation, and characterize the user experience
at each throttle tier.

This document is structured in three layers: (1) FORMAT CONTRACT — declared before
any analysis, governs all tables and tier blocks; (2) VERDICT BLOCK — analytical
commitment before evidence; (3) ANALYSIS SECTIONS — evidence that confirms or
revises the Verdict.

---

## FORMAT CONTRACT

Declare this contract before any analysis section. Every comparative table and UX
tier block in this document is governed by the schemas and rejection clauses below.

---

### Schema A — Comparative Table Schema

**Mandatory columns for every comparative table:**

```
| BASELINE | PROTECTED | DERIVATION CHAIN |
```

Column definitions for this document:
- **BASELINE** — the current system behavior at the stated volume, with no
  concurrency controls, no Retry-After parsing, and no queue buffers beyond what
  the scenario's existing configuration already provides
- **PROTECTED** — system behavior after the specific mitigations named in this
  analysis are applied; each cell must reference the specific Power Automate action
  name, connector setting, or configuration value changed
- **DERIVATION CHAIN** — the computation steps that connect the rate limit values
  in the registry to the conclusion stated in BASELINE or PROTECTED; a DERIVATION
  CHAIN cell must show the full chain: requests × multiplier = peak, peak − limit
  = overflow, overflow × retry factor = failed requests; a bare conclusion such as
  "42% fail" is a Schema A CONTENT VIOLATION

---

### Schema B — UX Tier Template Schema

**Mandatory structure for every throttle tier block:**

```
ERROR SIGNAL:          [HTTP status code / platform event — e.g., "HTTP 429
                        Retry-After: 60", "ActionThrottled in run history"]
USER-VISIBLE BEHAVIOR: [specific behavior the user observes at this tier]
VISIBILITY LEVEL:      EXPLICIT (error surfaced to user) |
                       SILENT (background retry or discard — user unaware)
RECOVERY PATH:         [manual retry / auto exponential backoff / flow queued
                        with notification delay / permanent failure — no recovery]
```

Each field must contain substantive, tier-specific content. Generic text that could
apply to any throttle scenario is a Schema B CONTENT VIOLATION.

---

### Four Rejection Clauses (Two-Tier Taxonomy)

**STRUCTURAL violations** are detected at SCAN TIME — observable by examining
table column headers or tier block field labels without reading cell content.
Remediation: add the missing structural element before proceeding.

**CONTENT violations** are detected at READ TIME — require reading cell content
to assess whether the required information is present. Remediation: deepen the
cell to meet the content requirement.

---

**CLAUSE 1 — SCHEMA A STRUCTURAL REJECTION**
- Type: STRUCTURAL | Detection: SCAN-TIME
- Trigger: any of the three column headers (BASELINE, PROTECTED, DERIVATION CHAIN)
  is absent from a comparative table
- Flag: `[TABLE NAME] — Schema A STRUCTURAL VIOLATION: missing column [X]`
- Remediation: add the missing column header; populate all rows

**CLAUSE 2 — SCHEMA A CONTENT REJECTION**
- Type: CONTENT | Detection: READ-TIME
- Trigger: a DERIVATION CHAIN cell contains only a numerical conclusion without the
  intermediate computation steps linking registry values to the stated outcome
- Flag: `[TABLE NAME] Row [N] — Schema A CONTENT VIOLATION: DERIVATION CHAIN
  contains conclusion only`
- Remediation: expand cell to show full computation chain; reference specific numeric
  values from the Rate Limit Registry

**CLAUSE 3 — SCHEMA B STRUCTURAL REJECTION**
- Type: STRUCTURAL | Detection: SCAN-TIME
- Trigger: one or more of the four field labels (ERROR SIGNAL, USER-VISIBLE BEHAVIOR,
  VISIBILITY LEVEL, RECOVERY PATH) is absent from a tier block
- Flag: `Tier [N] — Schema B STRUCTURAL VIOLATION: missing field label [X]`
- Remediation: add the missing field label(s); populate the field

**CLAUSE 4 — SCHEMA B CONTENT REJECTION**
- Type: CONTENT | Detection: READ-TIME
- Trigger: a tier field cell contains generic, boilerplate, or non-specific content
  not tied to the component, platform event, or specific behavior at this tier
- Flag: `Tier [N] Field [X] — Schema B CONTENT VIOLATION: generic content`
- Remediation: replace with tier-specific analytical content naming the component,
  event, or specific platform behavior

---

## SECTION 1 — VERDICT BLOCK

State the document's binding findings before any rate limit inventory, burst path
table, or volume mapping. This block is self-contained.

```
VERDICT
(a) Binding constraint: [component name] — [N req / M sec / scope: connector-level
    or platform-level]
(b) Primary gap: [unprotected burst path at named action] OR [Retry-After not
    handled at named connector]
(c) System status at [stated load]: SAFE / DEGRADED / FAILING
(d) UX completeness: [N] throttle tiers committed — all will use Schema B template
```

When any section revises a Verdict claim, insert an inline marker here:
`REVISED — see Section N`. This block is updated as revisions occur — it always
reflects the current analytical position.

**Revision rule for Claim (d):** A tier discovered mid-analysis that modifies the
tier count or reveals incomplete Schema B coverage requires a REVISED marker on
Claim (d) inserted at the boundary of the section where the new tier was found —
not deferred to the terminal reconciler.

---

## SECTION 2 — RATE LIMIT REGISTRY

Enumerate rate limits as a named registry. Connector-level limits (enforced by the
external service or connector SDK) and platform-level limits (enforced by Power
Automate) must appear as explicitly differentiated entries.

| COMPONENT | THRESHOLD | INTERVAL | SCOPE | TIER TYPE |
|-----------|-----------|----------|-------|-----------|
| [name] | [N req] | [M sec] | [level] | connector-level / platform-level |

At least one limit must be cited with a concrete numeric threshold, not described
only in abstract terms. Estimates are acceptable if labeled.

**Verdict currency:** Does the registry change what VERDICT (a) names as the binding
constraint? If yes, insert `REVISED — see Section 2` in VERDICT (a) now.

---

## SECTION 3 — BURST PATH AUDIT

Audit paths that generate concurrent requests. Produce a Schema A table.
Check: CLAUSE 1 (column headers present?) before producing the table.

| PATH | BASELINE | PROTECTED | DERIVATION CHAIN |
|------|----------|-----------|------------------|
| [action/trigger name] | [current: no cap, fanout volume at baseline] | [protected: named concurrency cap, queue buffer] | [concurrent runs × ops/run = peak req/interval vs. threshold] |

For each unprotected path, classify the gap:
- **STRUCTURAL** — no mechanism exists on this path
- **INCIDENTAL** — mechanism exists but is misconfigured or absent only under a
  specific stated condition

**Verdict currency:** Revise VERDICT (b) or (d) if warranted. Insert markers now.

---

## SECTION 4 — CASCADING FAILURE SCENARIO

Construct a specific two-tier cascade where throttling at Tier 1 causally triggers
throttling at Tier 2. Produce a Schema A table.

| STAGE | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------|----------|-----------|------------------|
| Tier 1 throttle | [first limit hit, at what volume] | [protected behavior] | [req/interval → threshold → event] |
| Causal mechanism | [how Tier 1 reaches Tier 2] | [protected path] | [retry volume or latency → Tier 2 load] |
| Tier 2 throttle | [compounding effect on throughput or error rate] | [protected behavior] | [second threshold → compounded failure rate] |

Two limits independently reached under load do not constitute a cascade. The second
throttle must be causally triggered by the first.

**Verdict currency:** Insert REVISED markers for any affected Verdict claims now.

---

## SECTION 5 — RETRY-AFTER GAP ANALYSIS

Evaluate Retry-After handling at every rate-limited endpoint in the registry.

| ENDPOINT | RETRY-AFTER SIGNAL | HANDLED? | FAILURE MODE |
|----------|-------------------|----------|--------------|
| [component] | Retry-After / x-ms-ratelimit-remaining / Retry-After-Ms | YES / NO | [retry storm / perm failure / silent discard] |

Every missing handler is a named finding. State the failure mode it causes.

**Verdict currency:** Insert REVISED markers now if warranted.

---

## SECTION 6 — UX PER THROTTLE TIER

Apply Schema B to every throttle tier. Check: CLAUSE 3 (field labels present?) before
producing each tier block.

**Six-item gate — all six must be satisfied before Section 7:**
(a) ERROR SIGNAL: present and substantive for every tier
(b) USER-VISIBLE BEHAVIOR: present and substantive for every tier
(c) VISIBILITY LEVEL: present and substantive for every tier
(d) RECOVERY PATH: present and substantive for every tier
(e) Tier count verified against Section 3 burst path audit (not VERDICT (d))
(f) Structure confirmed: Schema B template used, not free prose

After completing all tiers, explicitly verify the six-item gate. If any item fails,
resolve the violation before proceeding. Apply CLAUSE 3 (structural) and CLAUSE 4
(content) checks to each tier block after writing it.

**Verdict currency:** If tier count differs from VERDICT (d), insert
`REVISED — see Section 6` in VERDICT (d) now.

---

## SECTION 7 — MITIGATION PRESCRIPTIONS

For each bottleneck from Section 3 and each Retry-After gap from Section 5, produce
a Schema A prescription row. Check: CLAUSE 1 before producing the table.

| BOTTLENECK | BASELINE | PROTECTED | DERIVATION CHAIN |
|------------|----------|-----------|------------------|
| [component + limit] | [specific before-state — this bottleneck] | [after-state — named action name, setting value, pattern] | [why this changes the state — specific formula or logic] |

Generic advice fails. Name the specific action, setting, or pattern. CLAUSE 2 check:
ensure DERIVATION CHAIN cells show the reasoning chain, not just the outcome.

**Verdict currency:** Insert REVISED markers now.

---

## SECTION 8 — QUANTIFIED IMPACT AT LOAD SPIKE

Quantify degradation at a specific load multiplier. Produce a Schema A table.
DERIVATION CHAIN must show the full arithmetic chain — CLAUSE 2 applies.

| VOLUME TIER | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------------|----------|-----------|------------------|
| [Nx load] | [failure rate + queue depth] | [protected outcome] | Step 1: [req/interval] × [N] = [peak] / Step 2: [peak] − [limit] = [overflow] / Step 3: [overflow] × [retry factor] = [failed] / Step 4: [failed] ÷ [peak] = [failure %] |

A CLAUSE 2 CONTENT VIOLATION in this table must be flagged and resolved before
proceeding.

**Verdict currency:** Insert REVISED markers now.

---

## SECTION 9 — PRE-RECONCILER VERDICT CURRENCY SWEEP

Sweep all prior sections (2–8). For each: was a revision triggered? Is the REVISED
marker present in the Verdict block? If not, insert the marker now and annotate:
`REVISED (deferred from Section N) — see Section N`.

This sweep converts the terminal reconciler's check (a) from a correction-and-
verification operation into a pure verification operation.

```
Pre-Reconciler Output:
  Deferred markers inserted: [0 / list: Section N → Verdict claim]
  All Verdict claims current: YES / [list gaps]
```

---

## SECTION 10 — TERMINAL RECONCILER

Four separately enumerated checks. Each produces a named finding record.

**(a) VERDICT MARKER AUDIT**
For each Verdict claim (a)–(d): revised during analysis? Inline REVISED marker with
forward reference present?
`(a) Verdict marker audit: [0 violations / list]`

**(b) GATE DELIVERABLE AUDIT**
For each section transition: named prior-section deliverables present?
`(b) Gate deliverable audit: [0 violations / list]`

**(c) SCHEMA A CONTENT AUDIT**
Scan every DERIVATION CHAIN cell in Sections 3, 4, 7, 8. Flag CLAUSE 2 violations
(conclusion-only cells).
`(c) Schema A content audit: [0 violations / list]`

**(d) SCHEMA B STRUCTURAL SCAN**
Scan every tier block in Section 6. Flag CLAUSE 3 violations (missing field labels).
`(d) Schema B structural scan: [0 violations / list]`

```
Reconciler Summary:
  (a) Verdict markers:   [result]
  (b) Gate deliverables: [result]
  (c) Schema A content:  [result]
  (d) Schema B structure:[result]
  Overall: CLEAN / [N violations]
```
```

---

## V-03 — Lifecycle Emphasis Axis
**Hypothesis:** Structuring the document as an explicit phase lifecycle — where every phase boundary carries a Verdict-currency instruction, C-28 UX completeness is a named Verdict Claim (d) with an explicit revision rule, and Phase N-1 is a named pre-reconciler sweep — makes the revision propagation chain the visible backbone of the analysis rather than a background constraint.

---

```markdown
# flow-ratelimit — Rate Limit Throughput Analysis

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system in the topic. Trace bottlenecks, identify which rate
limits are hit first, describe backpressure propagation, and characterize user
experience per throttle tier.

This document follows a phase lifecycle. Each phase boundary triggers an explicit
Verdict-currency check. Phases do not begin until all prior-phase deliverables are
written. A pre-reconciler phase sweeps deferred revision markers before the terminal
reconciler audit.

---

## PHASE 0 — VERDICT COMMITMENT

**Phase lifecycle rule:** This block opens the document and anchors all subsequent
analysis. When any later phase revises a claim, the Verdict block is updated at the
boundary of the revising phase — not deferred to Phase 10.

Produce the Verdict block now, committing to analytical positions that will be
confirmed or revised by evidence:

```
VERDICT
(a) Binding constraint: [component name] — [numeric threshold / interval / scope]
(b) Primary gap: [unprotected burst path at named action] OR
                 [Retry-After not handled at named connector]
(c) System status at [stated load]: SAFE / DEGRADED / FAILING
(d) UX completeness: [N] throttle tiers — all tiers will use Schema B four-field
    template (ERROR SIGNAL / USER-VISIBLE BEHAVIOR / VISIBILITY LEVEL / RECOVERY PATH)
```

**Claim (d) revision rule:** If a tier is discovered mid-analysis that changes the
tier count, or if Phase 6 reveals that the four-field template cannot be fully
applied to a stated tier, a REVISED marker must be inserted on Claim (d) at the
Phase 6 boundary — not at the terminal reconciler. A Verdict that is stale at any
phase boundary is a violation.

**Inline revision protocol:** When Phase N revises Claim X, insert:
`REVISED — see Phase N` adjacent to the claim in this block.

---

## PHASE 1 — FORMAT CONTRACT

**Phase lifecycle rule:** Declare before any analysis. Governs all comparative
tables (Schema A) and UX tier blocks (Schema B) in this document.

### Schema A — Comparative Table

Mandatory columns: **BASELINE** | **PROTECTED** | **DERIVATION CHAIN**

- **BASELINE**: current system behavior — unprotected state specific to this scenario
- **PROTECTED**: behavior with specific named mitigations applied
- **DERIVATION CHAIN**: computation steps linking rate limit registry values to the
  stated outcome; must show the chain — not a conclusion alone

**Schema A STRUCTURAL clause** (scan-time): a table missing any of the three column
headers is flagged STRUCTURAL — add the missing column before proceeding.

**Schema A CONTENT clause** (read-time): a DERIVATION CHAIN cell containing only a
conclusion is flagged CONTENT — show the computation chain referencing specific
registry values.

### Schema B — UX Tier Template

Mandatory fields per tier:

```
ERROR SIGNAL:          [platform signal — specific HTTP code or run-history event]
USER-VISIBLE BEHAVIOR: [what the user observes at this throttle tier]
VISIBILITY LEVEL:      EXPLICIT | SILENT
RECOVERY PATH:         [user's available action at this tier]
```

**Schema B STRUCTURAL clause** (scan-time): a tier block missing a field label is
flagged STRUCTURAL — add the label before proceeding.

**Schema B CONTENT clause** (read-time): a field cell with generic, non-tier-specific
content is flagged CONTENT — replace with substantive content specific to this tier.

**Phase 1 → Phase 2 gate:** Format Contract with both schemas and all four rejection
clauses declared. Do not begin Phase 2 until this phase is complete.

---

## PHASE 2 — RATE LIMIT REGISTRY

**Phase lifecycle rule:** Enumerate the limits that bound all subsequent analysis.
This is the numeric basis for every DERIVATION CHAIN cell.

| COMPONENT | THRESHOLD | INTERVAL | SCOPE | TIER TYPE |
|-----------|-----------|----------|-------|-----------|
| [name] | [N req] | [M sec] | [level] | connector-level / platform-level |

Connector-level limits (enforced by external service or connector SDK) and platform-
level limits (enforced by Power Automate) must appear as explicitly differentiated
entries. Treating them as a single tier fails the essential correctness check.

**Phase 2 → Phase 3 Verdict currency check:** Does the registry revise the binding
constraint named in VERDICT (a)? If yes: insert `REVISED — see Phase 2` in VERDICT
(a) now — before Phase 3 begins.

**Phase 2 → Phase 3 gate:** At least one rate limit present with component name,
numeric threshold, interval, scope, and tier-type differentiation.

---

## PHASE 3 — BURST PATH AUDIT

**Phase lifecycle rule:** Audit unprotected paths before constructing cascades or
UX tiers. Tier count for Phase 6 is verified here, not in the Verdict block.

Produce a Schema A burst path table:

| PATH | BASELINE | PROTECTED | DERIVATION CHAIN |
|------|----------|-----------|------------------|
| [action/trigger] | [current fanout — no cap, direct to rate-limited endpoint] | [named concurrency cap + queue buffer] | [concurrent branches × ops/branch = req/interval vs. [threshold]] |

For each unprotected path, classify the gap type:
- **STRUCTURAL**: no mechanism exists on this path
- **INCIDENTAL**: mechanism exists but is misconfigured or absent under a specific
  stated condition — name the condition

A path that has throttle controls at a higher tier does not qualify as unprotected
at this path level.

**Phase 3 → Phase 4 Verdict currency check:** Does the burst path audit revise
VERDICT (b) (primary gap) or VERDICT (d) (tier count)? If yes: insert REVISED
marker(s) in the Verdict block now — before Phase 4 begins.

**Phase 3 → Phase 4 gate:** Audit table present with at least one classified gap.
VERDICT (b) and (d) current as of this phase.

---

## PHASE 4 — CASCADING FAILURE SCENARIO

**Phase lifecycle rule:** Construct the two-tier causal chain that the burst path
audit makes possible. The cascade must use components from the Phase 2 registry.

Produce a Schema A cascade table:

| STAGE | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------|----------|-----------|------------------|
| Tier 1 throttle | [first limit hit] | [protected behavior] | [volume → threshold → event] |
| Causal mechanism | [how Tier 1 reaches Tier 2] | [protected path] | [retry volume or latency spike → Tier 2 load] |
| Tier 2 throttle | [compounding effect on throughput or error rate] | [protected behavior] | [retry storm → second threshold → compound failure] |

Two limits independently reached under load are not a cascade. The second throttle
must be causally triggered by the first.

**Phase 4 → Phase 5 Verdict currency check:** Any Verdict claims affected? Insert
markers now.

**Phase 4 → Phase 5 gate:** Cascade table with two-tier causal chain, using Phase 2
registry components.

---

## PHASE 5 — RETRY-AFTER GAP ANALYSIS

**Phase lifecycle rule:** Evaluate Retry-After handling at each rate-limited endpoint.
Missing handling is a named finding before Phase 6's UX tiers can characterize the
recovery path accurately.

| ENDPOINT | SIGNAL TYPE | HANDLED? | FAILURE MODE |
|----------|-------------|----------|--------------|
| [component] | Retry-After / x-ms-ratelimit-remaining / Retry-After-Ms | YES / NO | [retry storm / perm failure / silent discard] |

Missing handling must be flagged as a named finding with the failure mode it causes.

**Phase 5 → Phase 6 Verdict currency check:** Any Verdict claims affected? Insert
markers now.

**Phase 5 → Phase 6 gate:** Each rate-limited endpoint in the Phase 2 registry
evaluated; named findings present for each missing Retry-After handler.

---

## PHASE 6 — UX PER THROTTLE TIER

**Phase lifecycle rule:** Apply Schema B to every throttle tier. The tier count
established here is the authoritative count — Phase 6 verifies against the Phase 3
burst path audit, not against VERDICT (d).

Apply the Schema B four-field template to every tier. At minimum two tiers.

```
TIER [N] — [component name / platform event]
ERROR SIGNAL:          [specific code or event for this tier]
USER-VISIBLE BEHAVIOR: [specific behavior at this tier]
VISIBILITY LEVEL:      EXPLICIT / SILENT
RECOVERY PATH:         [specific recovery action for this tier]
```

**Six-item gate — all must be satisfied before Phase 7:**
(a) ERROR SIGNAL substantively populated for every tier
(b) USER-VISIBLE BEHAVIOR substantively populated for every tier
(c) VISIBILITY LEVEL substantively populated for every tier
(d) RECOVERY PATH substantively populated for every tier
(e) Tier count verified against Phase 3 burst path audit (not VERDICT (d))
(f) Structure compliance: Schema B template used, not free prose

After verifying the six-item gate:
- Apply Schema B STRUCTURAL clause scan (all four field labels present in each tier?)
- Apply Schema B CONTENT clause check (substantive content in each field?)

**Phase 6 → Phase 7 Verdict currency check:**
- If tier count here differs from VERDICT (d): insert `REVISED — see Phase 6` in
  VERDICT (d) now — this is the boundary where Claim (d) revision must occur
- Any other claims affected? Insert markers now
- Do not begin Phase 7 until VERDICT (d) is current

**Phase 6 → Phase 7 gate:** Six-item gate satisfied. VERDICT (d) updated if needed.

---

## PHASE 7 — MITIGATION PRESCRIPTIONS

**Phase lifecycle rule:** Prescriptions reference the before-state (Phase 3 baseline)
and after-state (specific named setting or pattern) for each bottleneck.

Produce a Schema A prescription table:

| BOTTLENECK | BASELINE | PROTECTED | DERIVATION CHAIN |
|------------|----------|-----------|------------------|
| [component + limit] | [specific before-state — this bottleneck at this load] | [after-state — named Power Automate action, setting, or pattern] | [why the mitigation changes the state — formula, configuration value, logic] |

Generic prescriptions fail. Name the specific action, setting, or pattern. Baseline
must be specific to this scenario.

**Phase 7 → Phase 8 Verdict currency check:** Any Verdict claims affected? Insert
markers now.

**Phase 7 → Phase 8 gate:** All bottlenecks from Phase 3 and all gaps from Phase 5
have prescriptions with BASELINE, PROTECTED, and DERIVATION CHAIN populated.

---

## PHASE 8 — QUANTIFIED IMPACT AT LOAD SPIKE

**Phase lifecycle rule:** Arithmetic derives conclusions from the Phase 2 registry —
conclusions not traceable to registry values are CONTENT violations.

Produce a Schema A impact table at a specific load multiplier:

| VOLUME TIER | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------------|----------|-----------|------------------|
| [Nx load] | [failure rate / queue depth at baseline] | [protected metrics] | Step 1: [req/interval] × [N] = [peak] / Step 2: [peak] − [limit] = [overflow] / Step 3: [overflow] × [retry factor] = [failed] / Step 4: [failed] ÷ [peak] = [%] |

A DERIVATION CHAIN cell with only a conclusion is a Schema A CONTENT violation.
The computation chain is mandatory.

**Phase 8 → Phase 9 Verdict currency check:** Any Verdict claims affected? Insert
markers now.

**Phase 8 → Phase 9 gate:** Impact table with at least one fully derived load spike
cell. VERDICT current.

---

## PHASE 9 — PRE-RECONCILER VERDICT CURRENCY SWEEP

**Phase lifecycle rule:** This phase separates deferred-marker correction from
terminal-reconciler verification. The terminal reconciler performs pure verification;
this phase performs any remaining corrections.

Sweep Phases 2–8. For each phase:
- Did this phase's findings trigger a Verdict revision?
- Is the REVISED marker present in the Verdict block?
- If not: insert the marker now, annotated as `REVISED (deferred from Phase N) — see Phase N`

This sweep exists because gate-boundary currency checks (Phases 2–8) are forward
enforcement — they can be missed. The pre-reconciler converts those misses from
undetected gaps into corrected-and-documented deferred insertions. The terminal
reconciler then verifies that this sweep executed correctly, not that insertions
still need to happen.

```
Pre-Reconciler Sweep Output:
  Deferred markers inserted: [0 / list: Phase N → Verdict Claim X]
  All Verdict claims current: YES / [list any remaining gaps]
```

**Phase 9 → Phase 10 gate:** Sweep output with named finding record produced. No
uncorrected deferred markers remain.

---

## PHASE 10 — TERMINAL RECONCILER (FOUR-CHECK AUDIT)

**Phase lifecycle rule:** Terminal — no phase follows. Performs pure verification
over the full document.

**(a) VERDICT MARKER AUDIT**
For each Verdict claim (a)–(d): revised during any phase? Is an inline REVISED marker
with forward phase reference present?
`(a) Verdict marker audit: [0 violations / list]`

**(b) GATE DELIVERABLE AUDIT**
For each phase transition (Phases 1–9): named prior-phase deliverables confirmed
present?
`(b) Gate deliverable audit: [0 violations / list]`

**(c) SCHEMA A CONTENT AUDIT (DERIVATION CHAIN)**
Scan every DERIVATION CHAIN cell in Phases 3, 4, 7, 8. Any cell with only a
conclusion (no computation chain) is a Schema A CONTENT violation.
`(c) Schema A content audit: [0 violations / list]`

**(d) SCHEMA B STRUCTURAL SCAN**
Scan every tier block in Phase 6. Any block missing one or more of the four field
labels is a Schema B STRUCTURAL violation.
`(d) Schema B structural scan: [0 violations / list]`

```
Reconciler Summary:
  (a) Verdict markers:   [result]
  (b) Gate deliverables: [result]
  (c) Schema A content:  [result]
  (d) Schema B structure:[result]
  Overall: CLEAN / [N violations]
```
```

---

## V-04 — Phrasing Register Axis
**Hypothesis:** Formal technical imperative voice — where each section opens with a binding assertion (the conclusion to be supported) before producing the evidence, and generic instructions are replaced with precise analytical imperatives — produces stronger commitment-before-evidence discipline than sections that describe what to do.

---

```markdown
# flow-ratelimit — Rate Limit Throughput Analysis

You are a Connectors / Power Automate throughput domain expert.

**Task:** For the rate-limited system described in the topic, at the stated request
volume: (1) identify the binding rate limit constraint, (2) locate unprotected burst
paths and Retry-After gaps, (3) trace cascade failure chains, (4) characterize user
experience per throttle tier, (5) prescribe concrete mitigations with arithmetic
derivations.

Produce the document in the order specified. Each section opens with a binding
assertion before the evidence. If evidence contradicts the assertion, revise the
assertion inline and insert a cross-reference.

---

## SECTION A — VERDICT

**Position:** First section, before any rate limit inventory or burst path analysis.

State the binding findings. These are commitments, not summaries of what follows.

```
VERDICT
(a) Binding constraint: [component name] — [N req per M sec, scope: connector-level
    or platform-level] — this limit is hit first at the stated volume
(b) Primary gap: [structurally unprotected burst path at ACTION NAME] OR
                 [Retry-After not handled at CONNECTOR NAME]
(c) System status at [stated load]: SAFE / DEGRADED / FAILING
(d) UX completeness: [N] throttle tiers will be documented; all use Schema B
    four-field template
```

This block is self-contained. A reader who reads only Sections A does not need
to read Sections B–J to know the core finding.

**Revision protocol:** When Section N produces evidence that contradicts a claim,
insert `REVISED — see Section N` next to the claim — do not append a correction
at the end of the document. The Verdict block must always reflect the current
analytical position.

---

## SECTION B — FORMAT CONTRACT

**Position:** Before the first analysis section.

Declare the structural rules that all tables and tier blocks in this document obey.

**Table schema (Schema A):** Every comparative table must include three columns:

```
| BASELINE | PROTECTED | DERIVATION CHAIN |
```

- **BASELINE**: what the system does now, at the stated volume, unprotected
- **PROTECTED**: what the system does after the specific mitigations applied in
  Section H — cells must name the Power Automate action, setting value, or
  connector configuration changed
- **DERIVATION CHAIN**: arithmetic steps connecting Phase C registry values to the
  conclusion — format: [req/interval] × [multiplier] = [peak]; [peak] − [limit] =
  [overflow]; [overflow] × [retry factor] = [failed]; [failed] ÷ [peak] = [%fail]

**Tier block schema (Schema B):** Every throttle tier uses this structure:

```
ERROR SIGNAL:          [HTTP status code / platform run-history event]
USER-VISIBLE BEHAVIOR: [what the user sees or experiences at this tier]
VISIBILITY LEVEL:      EXPLICIT | SILENT
RECOVERY PATH:         [action available to the user at this tier]
```

**Rejection clauses:**

STRUCTURAL (scan-time): A table missing a column header, or a tier block missing
a field label, is a structural violation. Flag and resolve before continuing.

CONTENT (read-time): A DERIVATION CHAIN cell with only a conclusion, or a tier
field with non-specific generic content, is a content violation. Expand the cell
with the required specificity before continuing.

Two clause types, four application surfaces: Schema A STRUCTURAL, Schema A CONTENT,
Schema B STRUCTURAL, Schema B CONTENT.

---

## SECTION C — RATE LIMIT REGISTRY

**Assertion:** The binding constraint in VERDICT (a) is the rate limit component
named there. This section confirms or revises that assertion.

Enumerate rate limits as a registry. State component name, numeric threshold,
interval, and scope for each entry.

| COMPONENT | THRESHOLD | INTERVAL | SCOPE | TIER TYPE |
|-----------|-----------|----------|-------|-----------|
| [name] | [N req] | [M sec] | [level] | connector-level / platform-level |

Connector-level (external service / connector SDK) and platform-level (Power Automate
run concurrency, action throughput) must appear as separate rows.

**If the registry contradicts VERDICT (a):** revise VERDICT (a) now — insert
`REVISED — see Section C` and update the component name and threshold.

**Gate to Section D:** Registry contains at least one entry with all five fields:
name, threshold, interval, scope, tier-type differentiation. VERDICT (a) is current.

---

## SECTION D — BURST PATH AUDIT

**Assertion:** The primary gap in VERDICT (b) is the burst path named there.
This section confirms or revises that assertion, and establishes the authoritative
tier count for VERDICT (d).

Produce a Schema A burst path table. Verify STRUCTURAL clause (column headers
present) before writing the table.

| PATH | BASELINE | PROTECTED | DERIVATION CHAIN |
|------|----------|-----------|------------------|
| [action/trigger] | [current: no concurrency cap, fanout to endpoint] | [named concurrency cap value + queue buffer setting] | [concurrent branches × ops = req/interval vs. threshold from Section C] |

Classify each unprotected path:
- **STRUCTURAL** — no mechanism exists on this path
- **INCIDENTAL** — mechanism exists but misconfigured or conditionally absent
  (state the condition)

**If the audit contradicts VERDICT (b):** insert `REVISED — see Section D` now.
**If the tier count contradicts VERDICT (d):** insert `REVISED — see Section D` now.

**Gate to Section E:** Table present with at least one classified gap. VERDICT (b)
and (d) current.

---

## SECTION E — CASCADING FAILURE SCENARIO

**Assertion:** Throttle at Tier 1 (named component from Section C) causally triggers
throttle at Tier 2 (second named component from Section C). This section constructs
the causal chain.

Produce a Schema A cascade table:

| STAGE | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------|----------|-----------|------------------|
| Tier 1 throttle | [first component: limit hit, consequence] | [protected] | [volume → threshold → action event] |
| Causal mechanism | [backpressure path from Tier 1 to Tier 2] | [protected] | [retry volume or latency → second endpoint load] |
| Tier 2 throttle | [compounding effect: combined throughput or error rate] | [protected] | [retry storm volume → second threshold → compound %] |

Requirement: the second throttle is causally triggered by the first. Two limits
independently reached under load do not qualify as a cascade.

**Gate to Section F:** Two-tier causal chain documented. Any Verdict revisions
inserted now.

---

## SECTION F — RETRY-AFTER GAP ANALYSIS

**Assertion:** The Retry-After handling gap identified in VERDICT (b) is at the
connector named there. This section audits all rate-limited endpoints and confirms
or revises the assertion.

| ENDPOINT | SIGNAL | HANDLED? | FAILURE MODE IF MISSING |
|----------|--------|----------|------------------------|
| [component] | Retry-After / x-ms-ratelimit-remaining / Retry-After-Ms | YES / NO | [retry storm / perm failure / silent discard] |

Each missing handler is a named finding. State the failure mode it causes.

**Gate to Section G:** All Section C registry endpoints evaluated. Any Verdict
revisions inserted now.

---

## SECTION G — UX PER THROTTLE TIER

**Assertion:** The system produces exactly [N] distinct throttle tiers with
observable user-facing behavior, as committed in VERDICT (d). This section applies
Schema B to each tier and verifies the assertion.

Apply Schema B four-field template to each throttle tier. Minimum two tiers.
Verify Schema B STRUCTURAL clause (field labels present) before writing each block.

```
TIER [N] — [component name + triggering event]
ERROR SIGNAL:          [specific HTTP code or Power Automate run-history event]
USER-VISIBLE BEHAVIOR: [specific behavior the user observes at this tier]
VISIBILITY LEVEL:      EXPLICIT (user sees error) | SILENT (background — user unaware)
RECOVERY PATH:         [specific action available to the user at this tier]
```

**Six-item gate — all six must be satisfied before Section H:**
(a) ERROR SIGNAL: substantive and tier-specific for every tier
(b) USER-VISIBLE BEHAVIOR: substantive and tier-specific for every tier
(c) VISIBILITY LEVEL: classified for every tier
(d) RECOVERY PATH: substantive and tier-specific for every tier
(e) Tier count verified against Section D burst path audit — not VERDICT (d)
(f) Structure: Schema B template used for every tier, not free prose

**If tier count discovered here differs from VERDICT (d):** insert
`REVISED — see Section G` in VERDICT (d) now.

**Gate to Section H:** Six-item gate satisfied. VERDICT (d) current.

---

## SECTION H — MITIGATION PRESCRIPTIONS

**Assertion:** Each bottleneck from Section D and each Retry-After gap from Section F
has a specific, implementable remediation that moves the system from the baseline
state to the protected state.

Produce a Schema A prescription table:

| BOTTLENECK | BASELINE | PROTECTED | DERIVATION CHAIN |
|------------|----------|-----------|------------------|
| [component + limit] | [specific baseline behavior — this bottleneck at this load] | [specific after-state — named action name, setting, value] | [why this mitigation moves the state — formula or logic chain] |

Generic advice ("add retry logic", "implement throttling") fails. Name the specific
Power Automate action, the specific configuration property, and the specific value.
The baseline must describe the condition in this scenario, not any generic system.

**Gate to Section I:** All bottlenecks and gaps have prescriptions with all three
columns substantively populated. Any Verdict revisions inserted now.

---

## SECTION I — QUANTIFIED IMPACT AT LOAD SPIKE

**Assertion:** At [N]x normal volume, the baseline system reaches [X]% request
failure. The protected system reaches [Y]% failure. This section derives both
figures from the Section C registry values.

Produce a Schema A impact table:

| VOLUME TIER | BASELINE | PROTECTED | DERIVATION CHAIN |
|-------------|----------|-----------|------------------|
| Nx load | [failure rate + queue depth — baseline] | [failure rate + queue depth — protected] | Step 1: [req/interval] × [N] = [peak] / Step 2: [peak] − [limit] = [overflow] / Step 3: [overflow] × [retry factor] = [failed] / Step 4: [failed] ÷ [peak] = [%fail] |

A DERIVATION CHAIN cell with only a conclusion is a Schema A CONTENT violation.
Conclusions are not acceptable — the arithmetic chain is mandatory.

**Gate to Section J:** At least one load spike cell with full arithmetic derivation.
Any Verdict revisions inserted now.

---

## SECTION J1 — PRE-RECONCILER VERDICT CURRENCY SWEEP

Sweep Sections C–I. For each section: revision triggered? REVISED marker present
in Verdict block? If not: insert `REVISED (deferred from Section N) — see Section N`.

```
Pre-Reconciler Output:
  Deferred markers inserted: [0 / list]
  All Verdict claims current: YES / [gaps]
```

**Gate to Section J2:** Sweep output with named finding record. No uncorrected
deferred markers.

---

## SECTION J2 — TERMINAL RECONCILER

Four-check audit. Each check produces a named finding record.

**(a) VERDICT MARKER AUDIT:** For each Verdict claim (a)–(d): revised? Inline
REVISED marker with section reference present?
`(a) Verdict marker audit: [0 violations / list]`

**(b) GATE DELIVERABLE AUDIT:** For each section transition: named deliverables
confirmed present?
`(b) Gate deliverable audit: [0 violations / list]`

**(c) SCHEMA A CONTENT AUDIT:** Every DERIVATION CHAIN cell in Sections D, E, H, I
scanned. Conclusion-only cells flagged as Schema A CONTENT violations.
`(c) Schema A content audit: [0 violations / list]`

**(d) SCHEMA B STRUCTURAL SCAN:** Every tier block in Section G scanned. Blocks
missing field labels flagged as Schema B STRUCTURAL violations.
`(d) Schema B structural scan: [0 violations / list]`

```
Reconciler Summary:
  (a) Verdict markers:   [result]
  (b) Gate deliverables: [result]
  (c) Schema A content:  [result]
  (d) Schema B structure:[result]
  Overall: CLEAN / [N violations]
```
```

---

## V-05 — Inertia Framing Axis
**Hypothesis:** Treating the unprotected current state ("inertia") as an explicitly named first-class analytical state throughout — with INERTIA as the left-most column in every table, burst gap classification as structural-vs-incidental rather than binary present/absent, and mitigations framed as quantified departures from inertia — produces sharper mitigation specificity than baseline-neutral framing.

---

```markdown
# flow-ratelimit — Rate Limit Throughput Analysis

You are a Connectors / Power Automate throughput domain expert.

**Analytical frame:** The current system without protections is the "inertia state."
All analysis compares the inertia state against the protected state. Mitigations are
movements away from inertia — each mitigation must name what the inertia condition
is and how the mitigation changes it. A mitigation that does not reference the
specific inertia condition it corrects is analytically incomplete.

Produce the document in section order. Do not begin Section N until all named
deliverables from Section N-1 are written.

---

## SECTION 1 — VERDICT

**Position:** Before any rate limit inventory, burst path table, or volume mapping.

Commit to the binding findings. State the inertia-state failure before evidence.

```
VERDICT
(a) Binding constraint: [component name] — [N req / M sec / scope] — this is the
    rate limit hit first as inertia-state volume reaches [stated load]
(b) Primary gap (inertia): [structurally unprotected burst path at ACTION NAME] OR
                           [Retry-After not handled at CONNECTOR NAME — inertia
                           behavior: immediate retry storm / perm failure]
(c) Inertia system status at [stated load]: SAFE / DEGRADED / FAILING
(d) UX completeness: [N] throttle tiers — all tiers will use Schema B four-field
    template; tier count authoritative source is the burst path audit (Section 3)
```

When any section revises a Verdict claim, insert `REVISED — see Section N` next
to the affected claim at the boundary of the revising section.

**Claim (d) revision rule:** A tier discovered in Section 5 that changes the tier
count requires `REVISED — see Section 5` in VERDICT (d) at the Section 5 boundary.
Deferral to the terminal reconciler is not permitted.

---

## SECTION 2 — FORMAT CONTRACT

**Inertia-state column contract:** Every comparative table in this document declares
the inertia state as its reference point.

### Schema A — Comparative Table

Mandatory columns:

```
| INERTIA | PROTECTED | IMPROVEMENT OVER INERTIA |
```

Column definitions for this scenario:
- **INERTIA**: current system behavior at the stated volume — no concurrency controls,
  no Retry-After parsing, no queue buffers beyond what exists today; describe the
  specific inertia condition for each component
- **PROTECTED**: system behavior with the specific mitigations from Section 7 applied;
  must name the Power Automate action, connector setting, or configuration value changed
- **IMPROVEMENT OVER INERTIA**: the delta — what changes when the mitigation is applied
  and by how much; for quantified rows: show the computation chain
  ([inertia peak] − [protected threshold] = [improvement]) using registry values;
  for structural rows: state the mechanism change (from uncapped to capped at N)

### Schema B — UX Tier Template

Mandatory fields per tier:

```
ERROR SIGNAL:          [HTTP code or Power Automate run-history event]
USER-VISIBLE BEHAVIOR: [behavior the user observes at this tier in inertia state]
VISIBILITY LEVEL:      EXPLICIT | SILENT
RECOVERY PATH:         [action available — or state "none — permanent failure"]
```

### Four Rejection Clauses (Two-Tier Taxonomy)

**SCHEMA A — STRUCTURAL** (scan-time): INERTIA, PROTECTED, or IMPROVEMENT OVER
INERTIA column header absent from a table. Flag: `[TABLE] Schema A STRUCTURAL
VIOLATION`. Remediation: add missing column header before continuing.

**SCHEMA A — CONTENT** (read-time): IMPROVEMENT OVER INERTIA cell contains only
a conclusion without the arithmetic steps linking registry values to the delta.
Flag: `[TABLE] Row [N] Schema A CONTENT VIOLATION`. Remediation: expand cell
with computation chain referencing specific registry values.

**SCHEMA B — STRUCTURAL** (scan-time): one or more of the four field labels absent
from a tier block. Flag: `Tier [N] Schema B STRUCTURAL VIOLATION`. Remediation:
add missing field label(s) before continuing.

**SCHEMA B — CONTENT** (read-time): a tier field cell contains generic content not
specific to this tier's component, event, or inertia behavior. Flag: `Tier [N]
Field [X] Schema B CONTENT VIOLATION`. Remediation: replace with tier-specific
inertia-state content.

---

## SECTION 3 — RATE LIMIT REGISTRY

Enumerate the rate limits that define the inertia-state ceiling at each component.

| COMPONENT | THRESHOLD | INTERVAL | SCOPE | TIER TYPE |
|-----------|-----------|----------|-------|-----------|
| [name] | [N req] | [M sec] | [level] | connector-level / platform-level |

At least one entry must include a concrete numeric threshold. Connector-level and
platform-level entries must appear as explicitly differentiated rows.

**Verdict currency:** Does the registry revise the binding constraint in VERDICT (a)?
Insert `REVISED — see Section 3` in VERDICT (a) now if yes.

**Gate to Section 4:** Registry with at least one fully specified entry and explicit
tier-type differentiation. VERDICT (a) current.

---

## SECTION 4 — BURST PATH AUDIT (INERTIA STATE)

Produce a Schema A inertia-state burst path table. Schema A STRUCTURAL clause check:
verify INERTIA, PROTECTED, and IMPROVEMENT OVER INERTIA column headers before writing.

| PATH | INERTIA | PROTECTED | IMPROVEMENT OVER INERTIA |
|------|---------|-----------|--------------------------|
| [action/trigger] | [inertia: no cap, fanout volume = N concurrent × M ops = X req/interval] | [protected: concurrency cap at Y — named setting] | [structural: from uncapped to capped at Y; eliminates Z% of inertia overflow] |

For each unprotected path, classify the inertia gap:
- **STRUCTURAL INERTIA GAP**: no protective mechanism exists on this path in any
  configuration — the system is architecturally exposed in its inertia state
- **INCIDENTAL INERTIA GAP**: a protective mechanism exists but is inactive,
  misconfigured, or absent only under a specific stated condition — name the condition
  and the triggering scenario

This classification distinguishes paths that require adding a mechanism (structural)
from paths that require correcting an existing mechanism (incidental).

**Verdict currency:** Does the burst path count or primary gap classification revise
VERDICT (b) or VERDICT (d)? Insert REVISED marker(s) now.

**Gate to Section 5:** Table with at least one classified inertia gap. VERDICT (b)
and (d) current.

---

## SECTION 5 — CASCADING FAILURE SCENARIO

Construct the specific scenario where inertia-state behavior at Tier 1 causally
triggers a throttle event at Tier 2. Produce a Schema A cascade table.

| STAGE | INERTIA | PROTECTED | IMPROVEMENT OVER INERTIA |
|-------|---------|-----------|--------------------------|
| Tier 1 throttle | [inertia: component, limit hit, volume] | [protected: behavior with cap or backoff] | [event eliminated at Tier 1: retry volume reduction] |
| Causal mechanism | [inertia: retry storm volume or latency spike reaching Tier 2] | [protected: mechanism that prevents Tier 2 load] | [retry volume delta: inertia retry volume − protected retry volume] |
| Tier 2 throttle | [inertia: compounding failure rate at Tier 2] | [protected: Tier 2 outcome] | [compound failure rate reduction from inertia] |

Two limits independently reached under load are not a cascade. The second throttle
must be causally driven by the inertia behavior at Tier 1.

**Verdict currency:** Insert any required REVISED markers now.

**Gate to Section 6:** Two-tier causal cascade with INERTIA, PROTECTED, and
IMPROVEMENT populated. VERDICT current.

---

## SECTION 6 — RETRY-AFTER GAP ANALYSIS

Evaluate Retry-After handling at each rate-limited endpoint in the Section 3 registry.
In the inertia state, missing Retry-After handling produces a specific failure mode
that compounds with the cascade identified in Section 5.

| ENDPOINT | INERTIA RETRY BEHAVIOR | PROTECTED RETRY BEHAVIOR | IMPROVEMENT OVER INERTIA |
|----------|----------------------|------------------------|--------------------------|
| [component] | [inertia: Retry-After not parsed — immediate retry / after N tries: fail] | [protected: exponential backoff with Retry-After header parsing] | [retry volume reduction at this endpoint; failure mode eliminated] |

**Verdict currency:** Insert any required REVISED markers now.

**Gate to Section 7:** All Section 3 registry endpoints evaluated with inertia-state
failure modes named. VERDICT current.

---

## SECTION 7 — UX PER THROTTLE TIER (INERTIA-STATE CHARACTERIZATION)

Apply Schema B to each throttle tier as experienced in the inertia state. The tier
count here is verified against Section 4 — not against VERDICT (d).

```
TIER [N] — [component name + throttle event in inertia state]
ERROR SIGNAL:          [HTTP code or run-history event as the user encounters it]
USER-VISIBLE BEHAVIOR: [specific inertia-state behavior — what the user sees or
                        experiences at this tier, given no retry handling]
VISIBILITY LEVEL:      EXPLICIT | SILENT
RECOVERY PATH:         [available action — or "none — permanent failure in inertia
                        state; protected state provides [named recovery]"]
```

**Six-item gate — all must be satisfied before Section 8:**
(a) ERROR SIGNAL substantive and inertia-specific for every tier
(b) USER-VISIBLE BEHAVIOR substantive and inertia-specific for every tier
(c) VISIBILITY LEVEL classified for every tier
(d) RECOVERY PATH substantive; includes inertia-state limitation and protected-state
    improvement for every tier
(e) Tier count verified against Section 4 burst path audit — not VERDICT (d)
(f) Structure: Schema B template used for every tier, not free prose

After completing all tiers: apply Schema B STRUCTURAL clause (field labels present?)
and Schema B CONTENT clause (substantive, tier-specific content?).

**Verdict currency:** If tier count here differs from VERDICT (d), insert
`REVISED — see Section 7` in VERDICT (d) now.

**Gate to Section 8:** Six-item gate satisfied. VERDICT (d) current.

---

## SECTION 8 — MITIGATION PRESCRIPTIONS (DEPARTURE FROM INERTIA)

For each inertia gap from Section 4 and each Retry-After gap from Section 6,
produce a Schema A prescription showing the specific departure from inertia.

| INERTIA GAP | INERTIA | PROTECTED | IMPROVEMENT OVER INERTIA |
|-------------|---------|-----------|--------------------------|
| [component + inertia condition] | [specific inertia behavior at this component at this load] | [specific after-state: named Power Automate action + setting + value] | [delta: mechanism change (structural) or value correction (incidental) + why it removes the inertia condition] |

Generic prescriptions fail. Each prescription must:
- Name the specific inertia condition it targets (not applicable to any generic system)
- Name the specific Power Automate action, connector setting, or configuration value
- State the IMPROVEMENT OVER INERTIA with enough specificity that a reader knows
  why this mitigation moves from the named inertia state to the protected state

**Verdict currency:** Insert any required REVISED markers now.

**Gate to Section 9:** All inertia gaps and Retry-After gaps have prescriptions with
all three Schema A columns substantively populated.

---

## SECTION 9 — QUANTIFIED IMPACT: INERTIA VS. PROTECTED AT LOAD SPIKE

Quantify the inertia-state failure rate and the protected-state failure rate at a
specific load multiplier. All arithmetic derives from the Section 3 registry values.

| VOLUME TIER | INERTIA | PROTECTED | IMPROVEMENT OVER INERTIA |
|-------------|---------|-----------|--------------------------|
| [Nx load] | [inertia: failure % + queue depth] | [protected: failure % + queue depth] | Step 1: [req/interval] × [N] = [inertia peak] / Step 2: [inertia peak] − [limit] = [overflow] / Step 3: [overflow] × [retry factor] = [inertia failed] / Step 4: [inertia failed] ÷ [inertia peak] = [inertia %] / Protected delta: [protected peak − limit = protected overflow] → [protected failure %] / Improvement: [inertia %] − [protected %] = [improvement %] |

Schema A CONTENT clause: IMPROVEMENT OVER INERTIA cells must show the arithmetic
chain. A cell with only "improvement: 38%" is a CONTENT violation.

**Verdict currency:** Insert any required REVISED markers now.

**Gate to Section 10:** At least one load spike cell with full arithmetic derivation
for both inertia and protected states.

---

## SECTION 10 — PRE-RECONCILER INERTIA SWEEP

Sweep Sections 3–9. For each section: was a Verdict revision triggered by that
section's findings? Is the REVISED marker present in the Verdict block? If not,
insert `REVISED (deferred from Section N) — see Section N` now.

This sweep performs corrections. The terminal reconciler performs verification.

```
Pre-Reconciler Output:
  Deferred markers inserted: [0 / list: Section N → Verdict claim]
  All Verdict claims current: YES / [gaps]
```

**Gate to Section 11:** Named finding record produced. No uncorrected deferred
markers remain.

---

## SECTION 11 — TERMINAL RECONCILER

Four-check audit. Each check is a separately enumerated named audit.

**(a) VERDICT MARKER AUDIT:** Each Verdict claim (a)–(d) scanned. Revised claims
without REVISED markers with forward section references flagged.
`(a) Verdict marker audit: [0 violations / list]`

**(b) GATE DELIVERABLE AUDIT:** Each section transition (2–10) scanned. Named
prior-section deliverables confirmed present.
`(b) Gate deliverable audit: [0 violations / list]`

**(c) SCHEMA A CONTENT AUDIT (IMPROVEMENT OVER INERTIA):** Every IMPROVEMENT OVER
INERTIA cell in Sections 4, 5, 8, 9 scanned. Cells with only conclusions (no
computation chain) flagged as Schema A CONTENT violations.
`(c) Schema A content audit: [0 violations / list]`

**(d) SCHEMA B STRUCTURAL SCAN:** Every tier block in Section 7 scanned. Blocks
missing any of the four field labels flagged as Schema B STRUCTURAL violations.
`(d) Schema B structural scan: [0 violations / list]`

```
Reconciler Summary:
  (a) Verdict markers:   [result]
  (b) Gate deliverables: [result]
  (c) Schema A content:  [result]
  (d) Schema B structure:[result]
  Overall: CLEAN / [N violations]
```
```

---

## Variation Summary

| Variation | Primary Axis | Key Structural Differentiator | C-32 Implementation | C-33 Implementation |
|-----------|-------------|-------------------------------|---------------------|---------------------|
| **V-01** | Role sequence | Complete 10-role gate chain with explicit named deliverables at every boundary | Role 9: dedicated "Pre-Reconciler Verdict Currency Sweep" with deferred-vs-gate-inserted annotation | Role 10: four separately enumerated checks (a)–(d) each with named finding record |
| **V-02** | Output format | Four-clause Format Contract (Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT) with two-tier violation taxonomy as backbone | Section 9: "Pre-Reconciler Verdict Currency Sweep" converting reconciler check (a) from correction to verification | Section 10: four-check audit with separate finding record per check |
| **V-03** | Lifecycle emphasis | Phase lifecycle where every phase boundary carries an explicit Verdict-currency instruction; Claim (d) has a named revision rule banning deferral | Phase 9: "Pre-Reconciler Verdict Currency Sweep" as a named phase — correction before verification | Phase 10: four-check terminal reconciler with separate finding records |
| **V-04** | Phrasing register | Formal technical imperative — each section opens with a binding assertion (commitment) before evidence; evidence confirms or revises the assertion inline | Section J1: "Pre-Reconciler Verdict Currency Sweep" separating deferred-marker correction from terminal verification | Section J2: four-check audit; checks (c) and (d) separately named and separately finding-recorded |
| **V-05** | Inertia framing | INERTIA / PROTECTED / IMPROVEMENT OVER INERTIA columns throughout; structural-vs-incidental gap classification; mitigations as quantified departures from named inertia conditions | Section 10: "Pre-Reconciler Inertia Sweep" — same function, inertia-frame terminology | Section 11: four-check terminal reconciler with separate named audits for (c) IMPROVEMENT OVER INERTIA cells and (d) Schema B fields |
