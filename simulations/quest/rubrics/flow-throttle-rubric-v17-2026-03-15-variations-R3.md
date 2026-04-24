# flow-throttle — Round 3 Variations (v17 Rubric)

## Context and Variation Strategy

v17 adds four new aspirational criteria (C-15 through C-18) derived from R2 excellence signals.
The R2 signal sources and what each criterion targets:

| ID | Signal Source | What the criterion requires | Why R2 output elided it |
|----|--------------|----------------------------|------------------------|
| C-15 | V-01/V-05 schema contracts | All four tables present with column structure intact — no prose substitution of any table | Global schema declarations in a prompt header are overridden under token pressure; local enforcement at the point of each table was absent |
| C-16 | V-03/V-05 role ownership + consistency check | Propagation trace components trace to inventory; arithmetic citations trace to named inventory rows | Consistency check was present in R2-V-03/V-05 but as a "before submitting" prompt — models executed it after composition, when phantom introduction had already occurred |
| C-17 | V-01/V-02/V-03/V-05 vs V-04 | Status taxonomy column with typed tokens (`confirmed`, `estimated`, `?-unresolved`) per row — not prose | Status token vocabulary was described in prose in R2 instructions; models defaulted to inline prose notes when under token pressure |
| C-18 | V-02 GATE 1 retroactive correction | A named blocking gate that specifies the deficiency pattern and mandates rewriting before continuing | R2-V-02's GATE 1 was generic ("review every hop, any generic mechanism must be rewritten") — it did not name the specific deficiency pattern tokens that trigger the gate |

**R3 design goals:**
1. C-15 isolation: does moving the "no prose substitution" enforcement from a global header to
   an inline notice directly adjacent to each table schema produce more reliable C-15 compliance?
2. C-18 mechanism: does naming the specific deficiency pattern tokens (e.g., "also throttled",
   "cascade occurs") that trigger the retroactive correction gate — rather than describing the
   deficiency in general terms — produce a gate that fires when needed?
3. C-16 via dedicated role: does isolating cross-table consistency verification into a fourth
   "Consistency Auditor" role with no analytical mandate (verify only, no new content) prevent
   phantom component introduction more reliably than a post-composition check?
4. C-17 via formal acceptance criteria: does embedding per-deliverable acceptance criteria with
   explicit "prose uncertainty FAILS this criterion" statements produce typed status tokens more
   reliably than inline status vocabulary descriptions?
5. Combined ceiling: does combining all four R3 mechanisms (inline enforcement + named-deficiency
   gate + Consistency Auditor role + acceptance criteria) achieve stable 10/10 aspirational coverage?

Three single-axis variations (V-01, V-02, V-03), then two combined (V-04, V-05):

| Variation | Axis | C-15 | C-16 | C-17 | C-18 | Predicted composite |
|-----------|------|------|------|------|------|---------------------|
| V-01 | Output format — inline anti-substitution enforcement at each table | PASS | PASS | PASS | PARTIAL | ~90/100 |
| V-02 | Lifecycle emphasis — named-deficiency retroactive correction gate | PASS | PARTIAL | PASS | PASS | ~90/100 |
| V-03 | Role sequence — dedicated Consistency Auditor (Role 4) | PASS | PASS | PASS | PARTIAL | ~90/100 |
| V-04 | Phrasing register — deliverable + per-section acceptance criteria | PASS | PASS | PASS | PARTIAL | ~90/100 |
| V-05 | Combined: inline enforcement + named-deficiency gate + Auditor role | PASS | PASS | PASS | PASS | 100/100 |

V-01 targets C-15/C-17 via format (local enforcement), leaves C-18 as soft (no named-deficiency
gate; the Output Verification step is advisory). V-02 targets C-18 with a named-deficiency GATE 1
but cross-table consistency is only a post-composition check, not a dedicated verification pass.
V-03 isolates C-16 as a dedicated Role 4 mandate but the correction gate remains generic.
V-04 tests whether formal acceptance criteria per deliverable are sufficient for C-15/C-17 without
structural mandates at the prompt header. V-05 combines V-01/V-02/V-03 to target all four criteria.

---

## V-01 — Output Format: Inline Anti-Substitution Enforcement

**Axis:** Output format — each table schema declaration carries an inline ANTI-SUBSTITUTION
notice immediately below the column header row, at the exact point where a model under token
pressure might replace the table with a prose paragraph. Status vocabulary is declared as an
exhaustive three-token enumeration directly beneath the Status column definition.

**Hypothesis:** Global "output contract" schema declarations (R2-V-01) are read at prompt
intake but overridden at the moment of table construction under token pressure, because the
model does not re-reference the header. Inline notices placed directly at each table definition
fire at the moment the table is being produced, intercepting the substitution decision locally.
V-02 tests whether a named-deficiency correction gate achieves the same result via a different
mechanism; V-01 uses inline format enforcement instead.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### OUTPUT SCHEMA — Four Required Tables

This simulation produces exactly four structured tables. All four must appear in the final
output with their declared column structures intact. If token pressure requires cutting
content, cut analytical commentary — never replace a table with a prose equivalent.

---

### Phase 1 — TABLE A: Component-Limit Inventory

**TABLE A — Component-Limit Inventory**
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

> **ANTI-SUBSTITUTION:** This table must appear as structured rows. A prose paragraph
> listing components does not satisfy TABLE A. If the full table does not fit, produce
> the rows that do fit and mark remaining entries `TRUNCATED — [component name]`.
>
> **STATUS VOCABULARY — exactly three tokens, no others permitted:**
> - `confirmed` — value from Power Platform documentation
> - `estimated` — platform default applied in absence of documented value
> - `?-unresolved` — no documented value and no applicable platform default
>
> Inline prose ("limit unclear", "approximately X", "may vary by tenant") does not
> substitute for a status token. Every TABLE A row carries exactly one of the three
> tokens above.

Fill TABLE A before any propagation or UX analysis begins. PA construct type must come
from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

Generic labels ("API limit", "service rate limit") are not valid PA construct types.
Every component reachable from entry trigger to terminal action must have a TABLE A row.
`?-unresolved` rows are required for components with unknown limits — do not omit them.

After TABLE A: declare the FIRST BOTTLENECK by annotating that row `<-- FIRST BOTTLENECK`.

---

### Phase 2 — TABLE B: Backpressure Propagation Trace

**TABLE B — Backpressure Propagation Trace**
| Hop | From component | To component | Causal mechanism | Effect observed |
|-----|---------------|-------------|-----------------|-----------------|

> **ANTI-SUBSTITUTION:** This table must appear as structured rows. A narrative paragraph
> describing how throttling propagates does not satisfy TABLE B.
>
> **CAUSAL MECHANISM REQUIREMENT:** Each Causal mechanism cell must name the specific
> technical cause at that hop. Acceptable forms:
> - "429 returned to action; no Retry-After handler; immediate retry issued within same
>   throttle window; connector re-throttles before window resets"
> - "concurrency cap reached; runtime queues new trigger invocations; trigger backlog
>   accumulates at PA runtime layer"
>
> Unacceptable: "also throttled", "cascade occurs", "propagates to", "flow is affected."
>
> **COMPONENT CONSTRAINT:** Every From and To component must appear in TABLE A. A
> component not in TABLE A may not be introduced in TABLE B.

Fill TABLE B starting from the FIRST BOTTLENECK. One row per directed hop (From → To).
All TABLE A components on the propagation path must appear as From or To. Components not
on the path: add a row with Effect = `OUT-OF-PATH`. Continue tracing until no further
downstream component is affected.

---

### Phase 3 — Unprotected Burst Paths

Identify at least one structural path where burst traffic bypasses throttle controls:
a trigger that fires parallel flow runs without a concurrency cap, a loop without a
concurrency constraint, or an action sequence without a retry policy. Name the specific
PA construct (trigger type, action type, loop type) and the structural absence.

This is a structurally absent control — a path throttled at a higher limit does not qualify.

---

### Phase 4 — Retry-After Handling Audit

For each TABLE B hop where a 429 or throttle signal is received, check whether the flow
reads and honors the `Retry-After` header or equivalent backoff signal. Produce:
`FINDING-RH-NN: [component name] — [specific gap description]`

for each missing handler. If no gaps exist, explicitly state "No Retry-After handling gaps found."

---

### Phase 5 — User Experience by Throttle Tier

For each distinct throttle tier reached in TABLE B, describe the observable user-facing
behavior: what the user sees (429 message? queue delay? silent failure?), how long they
wait, and whether failure is visible or silent. Cover at least two tiers if multiple exist.

---

### Phase 6 — Cascading Throttle Failure Scenario

Construct or identify a scenario where throttling at one TABLE B tier triggers a second
throttle event at a different tier. Name both TABLE B rows, the causal link, and the
compounded effect on throughput or error rate.

---

### Phase 7 — TABLE C: Volume-Multiplier Tier Matrix

**TABLE C — Volume-Multiplier Tier Matrix**
| Multiplier | Est. req/min | First throttle tier hit | Behavior at this tier | Est. error rate | Arithmetic |
|-----------|-------------|------------------------|----------------------|----------------|------------|
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

> **ANTI-SUBSTITUTION:** This table must appear as structured rows with exactly four
> multiplier rows (1×, 3×, 5×, 10×). A prose description of how behavior changes
> with load does not satisfy TABLE C.
>
> **ERROR RATE:** Must be a numeric value or bracketed range (e.g., "8–12%"). Qualitative
> labels ("high", "low", "significant") do not qualify.
>
> **ARITHMETIC:** Must show the step-by-step calculation, naming each TABLE A limit used:
> "TABLE A row 2: connector limit = 600 req/min. At 5×: inbound = 1500 req/min.
>  Excess = 900 req/min. Queue capacity = 300 (TABLE A row 4, estimated).
>  After queue saturates: 600/1500 = 40% error rate."
> Each named limit must trace to a specific TABLE A row. Stated conclusions without the
> step-by-step chain do not satisfy the Arithmetic column.

For `?-unresolved` TABLE A rows used in arithmetic: state the assumption and proceed.

---

### Phase 8 — TABLE D: Mitigation Prescriptions

**TABLE D — Mitigation Prescriptions**
| Finding ID | Root cause | Prescribed remediation | Specific PA config or pattern |
|-----------|-----------|----------------------|------------------------------|

> **ANTI-SUBSTITUTION:** This table must appear as structured rows. A prose list of
> recommendations does not satisfy TABLE D.
>
> **SPECIFIC CONFIG:** The Specific PA config column must name the exact setting, formula
> with parameters, or queue integration point. Generic guidance ("add retry logic",
> "implement throttle handling") does not qualify.

One row per FINDING-RH-NN from Phase 4 and one row per unprotected burst path from Phase 3.

---

### Output Verification

Before finalizing: confirm all four required tables (TABLE A, TABLE B, TABLE C, TABLE D)
are present with their column structures intact. If any table was replaced with a prose
section, rewrite that section as a structured table before submitting.

---

## V-02 — Lifecycle Emphasis: Named-Deficiency Retroactive Correction Gate

**Axis:** Lifecycle emphasis — after Phase 2 (propagation trace), a GATE fires that
names the specific deficiency pattern tokens that trigger it and mandates rewriting the
affected rows before Phase 3 begins. The gate is retroactive (fires after the table is
produced), blocking (Phase 3 cannot start until the gate passes), and deficiency-named
(specifies exactly which text patterns constitute a failing mechanism).

**Hypothesis:** R2-V-02's GATE 1 instructed "review every hop; rewrite any hop with a
generic mechanism." The generic framing allows models to judge their own mechanisms as
acceptable. A named-deficiency gate that lists specific failing token patterns
("also throttled", "cascade occurs", "propagates to", "downstream effect", "affected")
removes the model's ability to self-certify a generic mechanism as passing — the gate
fires when the named pattern is present, regardless of surrounding prose quality. V-01
tests inline anti-substitution enforcement; V-02 tests named-deficiency correction gate
as the independent mechanism for C-18.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PHASE 0 — Component-Limit Inventory (BLOCKING GATE)

**Phase 1 is blocked until Phase 0 is complete.**

List every component in the `{{topic}}` request path. For each component:

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

PA construct type from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

Status vocabulary — three tokens only:
- `confirmed` — from Power Platform documentation
- `estimated` — platform default applied
- `?-unresolved` — no documented value and no applicable default

Prose uncertainty descriptions ("limit unclear", "approximately X", "may vary") do not
satisfy the Status field. Each row carries exactly one of the three tokens above.

**GATE 0:** Every component from entry trigger to terminal action must have a row.
A `?-unresolved` row satisfies GATE 0. A missing row does not. Phase 1 does not
begin until GATE 0 is satisfied.

After Phase 0: declare the FIRST BOTTLENECK (the component whose limit is hit first
at baseline request volume) and annotate that row `<-- FIRST BOTTLENECK`.

---

### PHASE 1 — Backpressure Propagation Trace

Trace how throttling at the FIRST BOTTLENECK propagates through the system.

| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|

Rules:
- One row per directed hop (From → To).
- Causal mechanism names the specific technical cause at this hop.
  Acceptable: "429 returned to action; no Retry-After handler present; immediate
  retry issued within same throttle window; connector re-throttles" or "concurrency
  cap reached; runtime queues trigger invocations; backlog accumulates at PA runtime."
- All Phase 0 components on the propagation path appear as From or To.
- Phase 0 components not on the path: row with Effect = `OUT-OF-PATH`.
- No component may appear in this table that is not in Phase 0.

---

**GATE 1 — RETROACTIVE CORRECTION: Inspect every Phase 1 row now.**

Before proceeding to Phase 2, scan every Causal mechanism cell for the following
deficiency patterns:

**Failing tokens** (any of these constitute a deficient mechanism):
- "also throttled"
- "cascade occurs" / "cascades to"
- "propagates to" / "propagation"
- "downstream effect" / "downstream impact"
- "flow is affected" / "becomes affected"
- "rate limiting applies"
- any phrase that names an effect at the destination without explaining the technical
  cause at the source

**Gate condition:** If any Causal mechanism cell contains a failing token or any text
matching the pattern above, rewrite that row's Causal mechanism cell with the specific
technical cause before continuing. Name: what signal is returned at the From component,
what the action or runtime does in response, and why that response causes the Effect at
the To component.

**GATE 1 is a blocking condition.** Phase 2 does not begin until every Causal mechanism
cell passes the failing-token scan. A table with all mechanisms passing may proceed.

After GATE 1 passes: verify that every Phase 1 From and To component appears in Phase 0.
For any component in Phase 1 that is absent from Phase 0, add a `PHANTOM-FLAG` note
before proceeding.

---

### PHASE 2 — User Experience at Each Throttle Tier

For each distinct throttle tier reached in Phase 1, describe the observable user-facing
behavior: what the user sees (429 response? queue delay? flow run failure with error code?),
how long they wait, and whether failure is visible or silent. Cover at least two tiers if
multiple tiers exist.

---

### PHASE 3 — Unprotected Burst Paths

Identify at least one path where burst traffic bypasses throttle controls. Name:
- The specific PA construct (trigger type, action type, loop type)
- The structural absence (no concurrency cap, no retry policy, unbounded parallelism)

A path throttled at a higher limit does not qualify. The absence of control must be named.

---

### PHASE 4 — Retry-After Handling Audit

For each Phase 1 hop where a 429 or throttle signal is received, check whether the flow
reads and honors the `Retry-After` header. Produce:
`FINDING-RH-NN: [component name] — [specific gap]`
for each missing handler.

---

### PHASE 5 — Cascading Throttle Failure Scenario

Construct a scenario where throttling at one Phase 1 tier triggers a second throttle event
at a different tier. Name both Phase 1 rows, the causal link, and the compounded impact
on throughput or error rate.

---

### PHASE 6 — Quantified Impact with Step-by-step Arithmetic

For a 10× volume spike, write the arithmetic step by step, naming each Phase 0 limit:
1. Baseline throughput (requests/min at normal load)
2. 10× inbound volume
3. The limiting component and numeric threshold from Phase 0 (cite the row)
4. Excess volume above the limit
5. Queue absorption — state the assumption if the queue capacity is from a `?-unresolved` row
6. Error rate as a percentage

Each limit used must trace back to a named Phase 0 row. Stated conclusions without the
step-by-step chain do not satisfy this phase.

---

### PHASE 7 — Volume-Multiplier Tier Matrix

| Load | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|------|-------------|----------------|----------|----------------|------------|
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

Rows 1×/3×/5×/10× are required. Error rate must be numeric or a bracketed range.
Arithmetic cites Phase 0 row numbers and shows the step-by-step chain from named limit
to stated error rate.

---

### PHASE 8 — Mitigation Prescriptions

| Finding ID | Root cause | Prescribed remediation | Specific PA config or pattern |
|-----------|-----------|----------------------|------------------------------|

One row per FINDING-RH-NN (Phase 4) and one row per unprotected burst path (Phase 3).
Specific PA config names the exact setting, backoff formula with parameters, or queue
integration point. Generic guidance does not qualify.

---

## V-03 — Role Sequence: Dedicated Consistency Auditor (Role 4)

**Axis:** Role sequence — a fourth role (Consistency Auditor) is added after the three
analytical roles. Role 4 has no analytical mandate: it produces no new findings, no
new tables, and no new recommendations. Its sole mandate is cross-table referential
verification — phantom component scan, arithmetic citation audit, and mitigation linkage
check. The audit produces a structured verdict (PASS or FAIL with itemized flags).

**Hypothesis:** R2-V-05 included a "Consistency Verification" section at the end of
Role 3, which ran after Role 3 had already composed all tables. A role that runs after
composition and cannot produce new analysis is structurally forced to find and flag
inconsistencies (its only output is flags), whereas a section at the end of an analytical
role can satisfy the prompt by finding no inconsistencies — including when inconsistencies
exist. Role 4's structural separation also prevents the Consistency Auditor from
"correcting" the tables in place (which would defeat the verification purpose). V-03
changes only role sequence; the analytical role content is held constant relative to V-05's
R2 structure.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables — they appear in full.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PRE-COMMITTED TABLE SCHEMAS

**TABLE 1 — Component-Limit Inventory** *(Role 1 owns)*
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

Status tokens: `confirmed` | `estimated` | `?-unresolved` — no prose substitutions.

**TABLE 2 — Backpressure Propagation Trace** *(Role 2 owns)*
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|

**TABLE 3 — Volume-Multiplier Tier Matrix** *(Role 3 owns)*
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**TABLE 4 — Mitigation Prescriptions** *(Role 3 owns)*
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|

---

### ROLE 1 — Domain Expert

**Owns:** TABLE 1 + Bottleneck Declaration

Fill TABLE 1. PA construct type from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

For every component from entry trigger to terminal action: add a row. Generic labels fail.

Status: `confirmed` (documented value), `estimated` (platform default), or `?-unresolved`
(no default available). Prose uncertainty descriptions fail. Components may not be omitted.

After TABLE 1: declare FIRST BOTTLENECK and annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Owns:** TABLE 2 + Retry-After Findings + Unprotected Burst Path

Fill TABLE 2 starting from the FIRST BOTTLENECK:
- One row per directed hop (From → To).
- Causal mechanism names the specific technical cause at this hop. Acceptable:
  "429 returned; no Retry-After handler; immediate retry within throttle window" or
  "concurrency cap reached; runtime queues trigger invocations; backlog accumulates."
  Generic text ("also throttled", "cascade occurs", "propagates") fails.
- Every TABLE 1 component on the propagation path appears as From or To.
- TABLE 1 components not on the path: row with Effect = `OUT-OF-PATH`.
- Only TABLE 1 components may appear in TABLE 2.

After TABLE 2:
1. **Retry-After audit:** For each hop receiving a 429 signal, check whether the flow
   honors `Retry-After`. Produce `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap (missing concurrency cap, no retry
   policy, unbounded parallel branch). Name the PA construct and structural absence.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** UX analysis + Cascading scenario + TABLE 3 + TABLE 4

**UX by Throttle Tier**
For each distinct tier in TABLE 2: describe what the user observes — error message,
wait time, silent vs. visible failure. Cover at least two tiers if multiple exist.

**Cascading Failure Scenario**
Using TABLE 2 hops: construct a scenario where throttling at one tier triggers a second
throttle event at a different tier. Name both TABLE 2 rows, the causal link, and the
compounded impact on throughput or error rate.

**TABLE 3 — Tier Matrix**
Fill TABLE 3. Arithmetic column shows step-by-step calculation naming each TABLE 1 limit:
> "TABLE 1 row 2: connector limit = 600 req/min. At 5×: inbound = 1500 req/min.
>  Excess = 900 req/min. Queue capacity = 300 (TABLE 1 row 4, estimated).
>  After queue saturates: 600/1500 = 40% error rate."

For `?-unresolved` TABLE 1 rows: state the assumption, proceed with arithmetic.

**TABLE 4 — Mitigations**
One row per FINDING-RH-NN and one row per unprotected burst path. Specific PA config
column names the exact setting, formula with parameters, or queue integration point.

---

### ROLE 4 — Consistency Auditor

**Receives:** TABLE 1, TABLE 2, TABLE 3, TABLE 4 from Roles 1–3.
**Mandate:** Cross-table referential verification only. Role 4 produces no new analysis,
no new findings, and no corrections to prior tables. Role 4 produces only flags and a
verdict.

**Check A — Propagation Phantom Scan**
List every component appearing as From or To in TABLE 2. Cross-reference each against
TABLE 1. For every TABLE 2 component not in TABLE 1, produce:
`PHANTOM-NN: "[component]" appears in TABLE 2 (Hop N) but has no row in TABLE 1`

**Check B — Arithmetic Citation Audit**
For each TABLE 3 Arithmetic cell, identify every named numeric limit. For each named
limit, verify it traces to a specific TABLE 1 row (by row number, component name, or
both). For each limit that cannot be traced:
`CITATION-GAP-NN: TABLE 3 [multiplier] row — "[limit text]" has no TABLE 1 source row`

**Check C — Mitigation Linkage Audit**
For each TABLE 4 Finding ID, verify it corresponds to a Role 2 FINDING-RH-NN or a
named unprotected burst path. For each TABLE 4 row without a traceable source:
`ORPHAN-FINDING-NN: TABLE 4 row — "[finding ID]" has no Role 2 source`

**Audit Verdict:**
If no flags: `AUDIT RESULT: PASS — no phantom components, no arithmetic citation gaps,
no orphan findings. Artifact is consistent.`

If flags exist: `AUDIT RESULT: FAIL — [N phantom flags], [N citation gaps], [N orphan
findings]. Artifact requires correction before finalization. Flag list follows.`
[List all flags in order: PHANTOM, CITATION-GAP, ORPHAN-FINDING]

---

## V-04 — Phrasing Register: Deliverable + Per-Section Acceptance Criteria

**Axis:** Phrasing register — formal "deliverable specification" register where each
section is titled as a deliverable with explicit acceptance criteria at the end of the
section. The criteria specify both what passes and what fails, creating local enforcement
at the point of each deliverable without relying on global header declarations or role
ownership contracts.

**Hypothesis:** A per-section acceptance criteria list that explicitly names the failure
mode ("A prose paragraph substituting for this table FAILS criterion 5") creates stronger
compliance pressure at the moment of generation than a global "output contract" header,
because the failure condition appears immediately adjacent to the work being produced.
This is a phrasing register test (formal/contractual) rather than a structural test —
the analytical content and lifecycle sequence are held constant. V-01 tests inline
anti-substitution at the table schema level; V-04 tests acceptance criteria at the section
level (which also covers non-table content like status tokens and mechanism specificity).

---

You are a Connectors / Power Automate throughput domain expert.
Produce a throttle simulation for `{{topic}}` using the deliverable specification below.
Each deliverable ends with acceptance criteria — these specify pass and fail conditions.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### DELIVERABLE 1 — Component-Limit Inventory

Produce a structured inventory of every component in the `{{topic}}` request path, with
PA construct type, numeric rate limit, and status designation.

**Format:**
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

PA construct type vocabulary (use exactly these terms — generic labels fail criterion 3):
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After the inventory: declare the FIRST BOTTLENECK and annotate that row
`<-- FIRST BOTTLENECK`.

**Acceptance criteria:**
1. Every component from entry trigger to terminal action has a table row.
2. Components with unknown limits carry a `?-unresolved` status token — they are not
   omitted because their limit is unknown.
3. PA construct type is drawn from the vocabulary above. Generic labels ("API limit",
   "service rate limit") FAIL criterion 3.
4. Status field carries exactly one of: `confirmed`, `estimated`, `?-unresolved`.
   Prose uncertainty descriptions ("limit unclear", "approximately X", "may vary by
   tenant") FAIL criterion 4 — they are not status tokens.
5. The inventory is present as a structured table with all columns intact. A prose
   paragraph listing components FAILS criterion 5.

---

### DELIVERABLE 2 — Backpressure Propagation Trace

Starting from the FIRST BOTTLENECK, trace how throttling propagates hop by hop through
the system.

**Format:**
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|

**Acceptance criteria:**
1. One row per directed hop (From → To).
2. Causal mechanism column names the specific technical cause at this hop. Acceptable
   forms: "429 returned to action; no Retry-After handler; immediate retry issued within
   same throttle window" or "concurrency cap reached; runtime queues trigger invocations;
   backlog accumulates at PA runtime layer." Failing forms: "also throttled", "cascade
   occurs", "propagates to", "downstream effect", "flow is affected" — any of these FAIL
   criterion 2.
3. Every component in From or To appears in the Deliverable 1 inventory. A component not
   in the inventory FAILS criterion 3 (phantom component).
4. All inventory components on the propagation path appear as From or To. Off-path
   components carry Effect = `OUT-OF-PATH`.
5. The trace is present as a structured table with all columns intact. A prose narrative
   of how throttling propagates FAILS criterion 5.

---

### DELIVERABLE 3 — Retry-After Handling Audit

For each Deliverable 2 hop receiving a 429 or throttle signal, check whether the flow
reads and honors the `Retry-After` header.

Produce `FINDING-RH-NN: [component name] — [specific gap]` for each missing handler.

**Acceptance criteria:**
1. Every Deliverable 2 hop receiving a 429 signal is explicitly checked.
2. Missing handlers are named as sequentially numbered findings (FINDING-RH-01,
   FINDING-RH-02, ...).
3. If no gaps exist, the audit explicitly states "No Retry-After handling gaps found."
   Omitting the audit section FAILS criterion 3.

---

### DELIVERABLE 4 — Unprotected Burst Path

Identify at least one structural path where burst traffic bypasses throttle controls.

**Acceptance criteria:**
1. The specific PA construct is named (trigger type, action type, loop type).
2. The structural absence is named (no concurrency cap configured, no retry policy,
   unbounded parallel branch).
3. The path is structurally unprotected — a path throttled at a higher limit FAILS
   criterion 3. The absence of control must be stated, not implied.

---

### DELIVERABLE 5 — User Experience by Throttle Tier

For each distinct throttle tier reached in the propagation trace, describe the observable
user-facing behavior.

**Acceptance criteria:**
1. At least two tiers described if multiple tiers exist in the propagation trace.
2. Each tier description states: what the user sees (error message? queue delay? silent
   failure?), how long they wait, and whether failure is visible or silent.
3. "The user experiences degraded performance" without specifics FAILS criterion 2.

---

### DELIVERABLE 6 — Cascading Throttle Failure Scenario

Construct a scenario where throttling at one tier triggers throttling at a different,
second tier.

**Acceptance criteria:**
1. Both tiers named and correspond to rows in the propagation trace.
2. The causal link from tier 1 to tier 2 is explained, not asserted.
3. The compounded effect on throughput or error rate is stated with specifics.

---

### DELIVERABLE 7 — Volume-Multiplier Tier Matrix

Produce a matrix mapping fixed load multipliers to throttle behavior and estimated
error rates, with step-by-step arithmetic in each row.

**Format:**
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**Acceptance criteria:**
1. Exactly four rows: 1×, 3×, 5×, 10×. Free-form tier labels or fewer than four rows
   FAIL criterion 1.
2. Est. error rate is a numeric value or bracketed range (e.g., "8–12%"). Qualitative
   labels ("high", "low", "significant") FAIL criterion 2.
3. Arithmetic column shows step-by-step calculation naming each inventory limit:
   each named limit traces to a specific Deliverable 1 row. Stated conclusions without
   the calculation chain FAIL criterion 3.
4. For `?-unresolved` rows used in arithmetic: the assumption is stated explicitly.
5. The tier matrix is present as a structured table. A prose description of how behavior
   changes with load FAILS criterion 5.

---

### DELIVERABLE 8 — Mitigation Prescriptions

For each finding and unprotected burst path, a specific, actionable remediation naming
the exact PA config or pattern.

**Format:**
| Finding ID | Root cause | Prescribed remediation | Specific PA config or pattern |
|-----------|-----------|----------------------|------------------------------|

**Acceptance criteria:**
1. One row per FINDING-RH-NN from Deliverable 3.
2. One row per unprotected burst path from Deliverable 4.
3. Specific PA config names the exact setting (e.g., "Trigger concurrency: set to 1 in
   trigger settings panel"), backoff formula with parameters (e.g., "Exponential backoff:
   base 10s, multiplier 2×, max 5 retries, jitter ±20%"), or queue integration point
   (e.g., "Route to Service Bus queue; consuming flow concurrency set to 10"). Generic
   guidance ("add retry logic", "implement throttle handling") FAILS criterion 3.
4. The mitigation table is present as a structured table. A prose list of recommendations
   FAILS criterion 4.

---

## V-05 — Combined: Inline Enforcement + Named-Deficiency Gate + Auditor Role

**Axis:** Combined — V-01 (inline anti-substitution enforcement at each table schema),
V-02 (named-deficiency retroactive correction gate after Phase 1 with specific failing
token list), and V-03 (dedicated Consistency Auditor role) integrated into a single prompt.
Status token vocabulary is declared as an exhaustive enumeration both at the table schema
(V-01 mechanism) and in the Phase 0 gate (V-02 mechanism), targeting C-17 through two
co-present enforcement points.

**Hypothesis:** C-15 requires local enforcement that fires at the moment of table
construction (V-01 mechanism). C-18 requires a named-deficiency gate that fires after
the mechanism column is produced but before the model advances (V-02 mechanism). C-16
requires a structural role that cannot self-approve (V-03 mechanism). C-17 requires the
status token vocabulary to appear as an exhaustive enumeration in close proximity to the
status column. No single axis achieves all four; the combined variation tests whether
the four mechanisms are compatible under a single prompt — whether the prompt becomes too
long to execute reliably, or whether each mechanism reinforces the others.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PRE-COMMITTED TABLE SCHEMAS

All four tables below must appear in the final output with column structure intact.
Produce structured table rows — do not substitute a prose section for any table.
If token budget is constrained, abbreviate analytical commentary first.

**TABLE 1 — Component-Limit Inventory** *(Role 1 owns)*
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

> Status vocabulary — exactly three tokens, no prose substitutions permitted:
> `confirmed` | `estimated` | `?-unresolved`
> Inline prose ("limit unclear", "may vary", "approximately") does not satisfy Status.
> ANTI-SUBSTITUTION: This table must appear as structured rows. Prose lists fail.

**TABLE 2 — Backpressure Propagation Trace** *(Role 2 owns)*
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|

> Causal mechanism must name the specific technical cause per hop.
> ANTI-SUBSTITUTION: This table must appear as structured rows. Prose narratives fail.
> COMPONENT CONSTRAINT: All From/To entries must appear in TABLE 1.

**TABLE 3 — Volume-Multiplier Tier Matrix** *(Role 3 owns)*
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

> Arithmetic = step-by-step calculation naming TABLE 1 row for each limit used.
> ANTI-SUBSTITUTION: Exactly four rows required. Prose descriptions fail.

**TABLE 4 — Mitigation Prescriptions** *(Role 3 owns)*
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|

> ANTI-SUBSTITUTION: This table must appear as structured rows. Prose lists fail.

---

### ROLE 1 — Domain Expert

**Owns:** TABLE 1 + Bottleneck Declaration

Fill TABLE 1. PA construct type from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

Every component from entry trigger to terminal action: add a TABLE 1 row. Generic labels
fail. Status: use `confirmed`, `estimated`, or `?-unresolved` — no prose alternatives.
Do not omit components with unknown limits; use `?-unresolved` instead.

After TABLE 1: declare FIRST BOTTLENECK and annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Owns:** TABLE 2 + Retry-After Findings + Unprotected Burst Path

Fill TABLE 2 starting from the FIRST BOTTLENECK:
- One row per directed hop (From → To).
- Causal mechanism names the specific technical cause. Acceptable:
  "429 returned; no Retry-After handler; immediate retry within throttle window" or
  "concurrency cap reached; runtime queues trigger invocations; backlog accumulates."
  Failing: "also throttled", "cascade occurs", "propagates to", "downstream effect."
- Every TABLE 1 component on the path appears as From or To.
- Off-path TABLE 1 components: row with Effect = `OUT-OF-PATH`.
- Only TABLE 1 components may appear in TABLE 2.

---

**GATE 1 — RETROACTIVE CORRECTION: Before producing findings, scan TABLE 2 now.**

Scan every Causal mechanism cell for the following failing token patterns:

**Failing tokens** (presence of any of these requires rewriting the row):
- "also throttled" / "also rate limited"
- "cascade occurs" / "cascades to" / "cascades"
- "propagates to" / "propagation" / "propagates"
- "downstream effect" / "downstream impact" / "downstream"
- "flow is affected" / "becomes affected" / "gets throttled"
- "rate limiting applies" / "throttling occurs"
- any phrase that names an effect at the To component without stating the technical
  cause at the From component

**Correction mandate:** For each Causal mechanism cell containing a failing token,
rewrite the cell. State: (1) what signal is returned at the From component, (2) what
the action, runtime, or connector does in response to that signal, and (3) why that
response causes the Effect at the To component.

**GATE 1 is a blocking condition.** Findings do not proceed until every Causal
mechanism cell passes the failing-token scan.

---

After GATE 1 passes, produce:
1. **Retry-After audit:** For each TABLE 2 hop receiving a 429 signal, check whether
   the flow honors `Retry-After`. Produce `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap (missing concurrency cap, no retry
   policy, unbounded parallel branch). Name the PA construct and structural absence.
3. **User experience by tier:** For each distinct throttle tier in TABLE 2, describe
   the observable user-facing behavior (error message, wait time, silent vs. visible
   failure). Cover at least two tiers if multiple exist.
4. **Cascading failure scenario:** A scenario where throttling at one TABLE 2 tier
   triggers a second throttle event at a different tier. Name both rows, the causal
   link, and the compounded impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** TABLE 3 + TABLE 4

**TABLE 3 — Tier Matrix**
Fill TABLE 3. The Arithmetic column shows the step-by-step chain from named TABLE 1
limit to stated error rate:
> "TABLE 1 row 2: connector limit = 600 req/min. At 3×: inbound = 900 req/min.
>  Excess = 300 req/min. Queue capacity = 300 (TABLE 1 row 4, estimated).
>  After queue saturates: 300/900 = 33% error rate."

Each named limit must reference a specific TABLE 1 row. For `?-unresolved` rows:
state the assumption and proceed. Do not leave Arithmetic cells empty.

**TABLE 4 — Mitigations**
One row per FINDING-RH-NN and one row per unprotected burst path. Specific PA config
column names the exact setting, formula with parameters, or queue integration point.

---

### ROLE 4 — Consistency Auditor

**Receives:** TABLE 1, TABLE 2, TABLE 3, TABLE 4 from Roles 1–3.
**Mandate:** Cross-table verification only. No new analysis. No corrections to prior
tables. Produces flags and a verdict only.

**Check A — Propagation Phantom Scan**
List all TABLE 2 From and To entries. Cross-reference against TABLE 1. For each TABLE 2
component absent from TABLE 1:
`PHANTOM-NN: "[component]" — TABLE 2 Hop [N], absent from TABLE 1`

**Check B — Arithmetic Citation Audit**
For each TABLE 3 Arithmetic cell, identify every named numeric limit. For each limit
not traceable to a specific TABLE 1 row:
`CITATION-GAP-NN: TABLE 3 [multiplier] — "[limit]" has no TABLE 1 source`

**Check C — Mitigation Linkage Audit**
For each TABLE 4 Finding ID, verify it maps to a Role 2 FINDING-RH-NN or named
unprotected burst path. For each unmapped TABLE 4 row:
`ORPHAN-FINDING-NN: TABLE 4 row — "[ID]" has no Role 2 source`

**Check D — Table Completeness**
Confirm all four required tables (TABLE 1, TABLE 2, TABLE 3, TABLE 4) are present as
structured tables with all declared columns intact. For any required table replaced
with prose or omitted:
`MISSING-TABLE-NN: [TABLE name] — absent or substituted with prose`

**Audit Verdict:**
No flags: `AUDIT RESULT: PASS — all tables present and structurally intact; no phantom
components; no arithmetic citation gaps; no orphan findings.`

Flags present: `AUDIT RESULT: FAIL — [counts by type]. Artifact requires correction.`
[List all flags.]
