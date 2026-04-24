# flow-throttle — Round 4 Variations (v18 Rubric)

## Context and Variation Strategy

v18 adds three new aspirational criteria (C-19, C-20, C-21) derived from R3 excellence signals.
Each criterion codifies a mechanism that appeared in an R3 variation's passing behavior:

| ID | Signal Source | What the criterion requires | Why R3 output sometimes missed it |
|----|--------------|----------------------------|------------------------------------|
| C-19 | R3-V-01 C-15 PASS | ANTI-SUBSTITUTION placed *immediately after* each table's `|---|---| ` separator row — zero gap, production-point enforcement. Last-table vulnerability is the key failure mode. | R3-V-01 placed enforcement in a blockquote after the full schema declaration with a blank line gap; models under token pressure on TABLE D (the last table) reverted to the global header rather than the local notice. |
| C-20 | R3-V-02 C-18 PASS | Failing-token vocabulary enumerated as a scannable checklist — each token as a checkable item — making gate compliance binary and auditable. | R3-V-02 had a bulleted token list but no explicit checkbox-scan format; models could produce the gate in a "passes globally" mode without matching each token against each cell. |
| C-21 | R3-V-03 C-16 PASS | Consistency auditor's structural incapability is *declared* at role entry — "I produced no rows in these tables; self-certification is structurally impossible." Removes the rationalization path. | R3-V-03 prohibited corrections by mandate; models could rationalize that a Role 4 with no-correction mandate was equivalent to a structurally incapable auditor, satisfying C-21 by implication rather than declaration. |

**R4 design goals:**
1. C-19 isolation: does removing the blank line between each table's `|---|---| ` separator and the
   ANTI-SUBSTITUTION notice — making the notice the syntactically first element at the row-production
   point — produce more reliable last-table compliance than R3-V-01's adjacent-blockquote? (V-01)
2. C-20 isolation: does a checkbox scan format (`- [ ] "token"` → `[CLEAR]` or `[FAIL: hop N]`) per
   failing token produce more reliable gate compliance than a bulleted list with general correction
   instructions? (V-02)
3. C-21 isolation: does opening Role 4 with an explicit structural incapability declaration before
   the mandate suppress self-verification rationalization more reliably than a mandate-only Role 4? (V-03)
4. C-19+C-20 stacking: do at-header placement and checkbox-format gate reinforce each other without
   prompt bloat degrading essential-criteria compliance? (V-04)
5. Full ceiling: do all three mechanisms (C-19+C-20+C-21) compose stably in a single prompt? (V-05)

Three single-axis variations (V-01, V-02, V-03), then two combined (V-04, V-05):

| Variation | Primary axis | C-19 | C-20 | C-21 | Predicted composite |
|-----------|-------------|------|------|------|---------------------|
| V-01 | Output format — tight at-header enforcement on all 4 tables | PASS | PARTIAL | PARTIAL | ~88/100 |
| V-02 | Lifecycle emphasis — checkbox enumerated-token correction gate | PARTIAL | PASS | PARTIAL | ~88/100 |
| V-03 | Role sequence — structural incapability declaration at auditor entry | PARTIAL | PARTIAL | PASS | ~88/100 |
| V-04 | Combined: at-header placement + checkbox token gate | PASS | PASS | PARTIAL | ~93/100 |
| V-05 | Combined: at-header + checkbox gate + incapable auditor | PASS | PASS | PASS | 100/100 |

V-01 targets C-19 via output format — the enforcement notice fires at the exact production point for
every table including the last. V-02 targets C-20 via lifecycle — checkbox scan makes each token a
binary check rather than a general gate condition. V-03 targets C-21 via role sequence — the
structural incapability statement is the first thing Role 4 says. V-04 combines format + lifecycle
without role restructuring. V-05 adds role restructuring for the full ceiling.

---

## V-01 — Output Format: Tight At-header Anti-substitution Enforcement

**Axis:** Output format — each table's ANTI-SUBSTITUTION notice appears as the syntactically first
element after the `|---|---| ` separator row, with no blank line between them. The notice fires at
the exact moment the model begins producing data rows for that table. All four tables carry this
treatment identically. TABLE D is labeled "FINAL TABLE" in its gate to counter the last-table
vulnerability. No named-token correction gate (C-20 left at baseline). No structural auditor
separation (C-21 left at baseline).

**Hypothesis:** R3-V-01 placed ANTI-SUBSTITUTION in a blockquote after the full table schema block,
which the model reads as part of the schema preamble. Under token pressure on TABLE D (the 4th and
final table), the model may treat the global schema contract or the phase header as sufficient and
skip re-reading the local notice. The zero-gap placement between `|---|---| ` and the enforcement
blockquote makes the notice a structural part of the row-production sequence — the model cannot
advance past the separator without encountering it. V-02 tests whether a token-enumerated gate is a
sufficient alternative; V-01 tests pure placement discipline without gate augmentation.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

This simulation produces four required tables (TABLE A, TABLE B, TABLE C, TABLE D).
All four must appear in the final output with column structure intact.

---

### Phase 0 — TABLE A: Component-Limit Inventory

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE A PRODUCTION GATE]** You are now producing TABLE A rows. Start the first `| # |`
> data row immediately below this notice. Requirements active at this production point:
> - Produce structured table rows — a prose paragraph listing components fails TABLE A.
> - PA construct type must come from the taxonomy below — generic labels ("API limit",
>   "service rate limit") fail.
> - Status token: exactly one of `confirmed` / `estimated` / `?-unresolved` per row.
>   Prose uncertainty ("limit unclear", "approximately X", "may vary") fails this column.
> - Every component from entry trigger to terminal action must have a row. Unknown limits
>   receive `?-unresolved` — they are not omitted.
> - TABLE A has no rows only if no components exist, which cannot be the case.

PA construct type vocabulary (use only these):
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE A: declare the FIRST BOTTLENECK — the component whose limit is hit first at
baseline request volume. Annotate that row `<-- FIRST BOTTLENECK`.

---

### Phase 1 — TABLE B: Backpressure Propagation Trace

| Hop | From component | To component | Causal mechanism | Effect observed |
|-----|---------------|-------------|-----------------|-----------------|
> **[TABLE B PRODUCTION GATE]** You are now producing TABLE B rows. Start the first `| Hop |`
> data row immediately below this notice. Requirements active at this production point:
> - Produce structured table rows — a prose narrative of how throttling propagates fails TABLE B.
> - Causal mechanism column: name the specific technical cause at this hop. Acceptable:
>   "429 returned to action; no Retry-After handler present; immediate retry issued within
>   same throttle window; connector re-throttles before window resets" or "concurrency cap
>   reached; PA runtime queues new trigger invocations; trigger backlog accumulates."
>   Failing forms: "also throttled", "cascade occurs", "propagates to", "downstream effect",
>   "flow is affected", "rate limiting applies" — these name an effect, not a mechanism.
> - Every From and To component must appear in TABLE A. A component absent from TABLE A
>   may not be introduced in TABLE B (no phantom components).
> - All TABLE A components on the propagation path appear as From or To. Off-path
>   components receive Effect = `OUT-OF-PATH`.

Start from the FIRST BOTTLENECK. Trace until no further downstream component is affected.

---

**Correction Checkpoint:** Before Phase 2, review TABLE B. Any Causal mechanism cell that
describes an effect without naming a specific technical cause requires rewriting. Rewrite
deficient rows before continuing. State: what signal is returned at From, what the action
or runtime does in response, and why that response causes the Effect at To.

---

### Phase 2 — Retry-After Handling Audit

For each TABLE B hop where a 429 or throttle signal is received, check whether the flow
reads and honors the `Retry-After` header or equivalent backoff signal. Produce:
`FINDING-RH-NN: [component name] — [specific gap description]`
for each missing handler. If no gaps exist, explicitly state "No Retry-After handling gaps found."

---

### Phase 3 — Unprotected Burst Path

Identify at least one path where burst traffic bypasses throttle controls. Name:
- The specific PA construct (trigger type, action type, loop type).
- The structural absence (no concurrency cap configured, no retry policy, unbounded parallelism).

A path throttled at a higher limit does not qualify. The control must be structurally absent.

---

### Phase 4 — User Experience by Throttle Tier

For each distinct throttle tier reached in TABLE B, describe the observable user-facing
behavior: what the user sees (429 error message? queue delay? flow run failure with error
code? silent retry?), how long they wait, and whether failure is visible or silent.
Cover at least two tiers if multiple exist.

---

### Phase 5 — Cascading Throttle Failure Scenario

Construct a scenario where throttling at one TABLE B tier triggers a second throttle event
at a different tier. Name both TABLE B rows, the causal link between them, and the
compounded effect on throughput or error rate.

---

### Phase 6 — TABLE C: Volume-Multiplier Tier Matrix

| Multiplier | Est. req/min | First throttle tier hit | Behavior at this tier | Est. error rate | Arithmetic |
|-----------|-------------|------------------------|----------------------|----------------|------------|
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |
> **[TABLE C PRODUCTION GATE]** You are now producing TABLE C rows. Fill the four rows
> above (1×, 3×, 5×, 10×). Requirements active at this production point:
> - Exactly these four multiplier rows are required. Free-form tier labels or omitted rows fail.
> - Est. error rate: numeric value or bracketed range (e.g., "8–12%"). Qualitative labels
>   ("high", "moderate") fail this column.
> - Arithmetic: step-by-step calculation naming each TABLE A limit used. Cite the TABLE A row
>   for every limit (e.g., "TABLE A row 2: connector limit = 600 req/min. At 5×: inbound =
>   1500 req/min. Excess = 900 req/min. TABLE A row 4 queue capacity = 300 (estimated).
>   After saturation: 600/1500 = 40% error rate."). Stated conclusions without the chain fail.
> - For `?-unresolved` TABLE A rows: state the assumption and proceed.
> - A prose description of how behavior changes with load fails TABLE C entirely.

Note: TABLE C rows are above this gate notice. Fill the table rows above, then continue.

---

### Phase 7 — TABLE D: Mitigation Prescriptions

| Finding ID | Root cause | Prescribed remediation | Specific PA config or pattern |
|-----------|-----------|----------------------|------------------------------|
> **[TABLE D PRODUCTION GATE — FINAL TABLE]** This is the fourth and last required table.
> The same enforcement applies here as for TABLE A, TABLE B, and TABLE C. Produce
> structured table rows below. Requirements active at this production point:
> - One row per FINDING-RH-NN from Phase 2 and one row per unprotected burst path from Phase 3.
> - Specific PA config: name the exact setting, backoff formula with parameters, or queue
>   integration point (e.g., "Trigger concurrency: set to 1 in trigger settings panel" or
>   "Exponential backoff: base 10s, multiplier 2×, max 5 retries, jitter ±20%").
>   Generic guidance ("add retry logic", "implement throttle handling") fails this column.
> - A prose list of recommendations fails TABLE D entirely.

---

**Output Verification:** Before finalizing, confirm TABLE A, TABLE B, TABLE C, and TABLE D
are all present as structured tables with column structures intact. If any table was replaced
with prose, rewrite it as a table before submitting.

---

## V-02 — Lifecycle Emphasis: Checkbox Enumerated-token Correction Gate

**Axis:** Lifecycle emphasis — after TABLE B is produced, GATE 1 runs as a checkbox scan
protocol. Each known failing token is a checkable item. The model must mark each token
`[CLEAR]` (not present in any Causal mechanism cell) or `[FAIL: hop N — rewritten below]`
(present; rewrite provided). A GATE 1 with any unresolved `[ ]` boxes or any `[FAIL]` box
without a rewrite is an incomplete gate — the gate has not passed and Phase 2 does not begin.
Standard (adjacent blockquote) ANTI-SUBSTITUTION is used for tables. No structural auditor
separation (C-21 at baseline).

**Hypothesis:** R3-V-02 presented failing tokens as a bulleted list with a general correction
mandate ("if any token is present, rewrite the row"). The model could satisfy this gate by
running a holistic review and concluding "no failing tokens found" without checking each token
individually. A checkbox format forces a per-token attestation: the model must state its
finding for each specific token string. This makes the gate machine-auditable — an evaluator
can count unresolved boxes. V-01 tests whether placement discipline achieves C-19; V-02 tests
whether per-token checkbox discipline achieves C-20. Combined in V-04.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### OUTPUT SCHEMA — Four Required Tables

All four tables below must appear in the final output with column structures intact.
Under token pressure, abbreviate analytical commentary — do not replace a table with prose.

**TABLE A — Component-Limit Inventory**
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

> ANTI-SUBSTITUTION: Structured rows required. Prose listing fails.
> Status vocabulary — exactly three tokens: `confirmed` | `estimated` | `?-unresolved`
> Inline prose ("limit unclear", "may vary", "approximately X") fails the Status column.

**TABLE B — Backpressure Propagation Trace**
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|

> ANTI-SUBSTITUTION: Structured rows required. Prose narrative fails.
> Causal mechanism: specific technical cause per hop. Effect-label text fails (see GATE 1).
> COMPONENT CONSTRAINT: All From/To entries must appear in TABLE A.

**TABLE C — Volume-Multiplier Tier Matrix**
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

> ANTI-SUBSTITUTION: Exactly four rows (1×/3×/5×/10×) required. Prose fails.
> Arithmetic cites TABLE A row numbers. Error rate is numeric or bracketed range.

**TABLE D — Mitigation Prescriptions**
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|

> ANTI-SUBSTITUTION: Structured rows required. Prose list fails.
> Specific PA config: exact setting, formula with parameters, or queue integration point.

---

### Phase 0 — Component-Limit Inventory

Fill TABLE A. PA construct type from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

Every component from entry trigger to terminal action: add a TABLE A row. Generic labels fail.
Status: `confirmed`, `estimated`, or `?-unresolved` — no prose alternatives. Do not omit
components with unknown limits; use `?-unresolved`.

After TABLE A: declare FIRST BOTTLENECK, annotate that row `<-- FIRST BOTTLENECK`.

---

### Phase 1 — Backpressure Propagation Trace

Fill TABLE B starting from the FIRST BOTTLENECK. One row per directed hop (From → To).
All TABLE A components on the propagation path appear as From or To. Off-path components:
row with Effect = `OUT-OF-PATH`. Only TABLE A components appear in TABLE B.

Causal mechanism must name the specific technical cause at this hop:
- Acceptable: "429 returned to action; no Retry-After handler; immediate retry within throttle
  window; connector re-throttles before window resets"
- Acceptable: "concurrency cap reached; PA runtime queues trigger invocations; trigger backlog
  accumulates at PA runtime layer"

---

### GATE 1 — ENUMERATED TOKEN SCAN (BLOCKING)

Before Phase 2: run the token scan below. For each token, mark `[CLEAR]` (not present in
any Causal mechanism cell) or `[FAIL: hop N — rewritten below]` (present; provide rewrite
immediately after the checklist). Phase 2 does not begin until every box is resolved and
every `[FAIL]` has a rewrite.

**TOKEN SCAN — Causal mechanism cells:**

Category A — Pure effect labels (no mechanism stated):
- [ ] "also throttled"
- [ ] "also rate limited"
- [ ] "gets throttled"
- [ ] "is throttled"
- [ ] "rate limited"

Category B — Causation assertions without mechanism:
- [ ] "cascade occurs"
- [ ] "cascades to"
- [ ] "cascading throttle"
- [ ] "propagates to"
- [ ] "propagation"
- [ ] "throttle propagates"

Category C — Vague effect descriptions:
- [ ] "downstream effect"
- [ ] "downstream impact"
- [ ] "flow is affected"
- [ ] "becomes affected"
- [ ] "is impacted"
- [ ] "experiences throttling"

Category D — Passive mechanism evasions:
- [ ] "rate limiting applies"
- [ ] "throttling occurs"
- [ ] "throttling applies"
- [ ] "throttle applies"

**Rewrite format for any [FAIL] items:**
State: (1) what signal is returned at the From component, (2) what the action, runtime, or
connector does in response to that signal, and (3) why that response causes the Effect at
the To component. Replace the failing cell with this three-part statement.

**GATE 1 PASS CONDITION:** All boxes resolved to `[CLEAR]` or `[FAIL + rewrite provided]`.
An incomplete scan (remaining `[ ]` boxes) means GATE 1 has not passed.

---

### Phase 2 — Retry-After Handling Audit

For each TABLE B hop receiving a 429 or throttle signal, check whether the flow reads and
honors the `Retry-After` header. Produce `FINDING-RH-NN: [component] — [specific gap]`.
If no gaps exist, state "No Retry-After handling gaps found."

---

### Phase 3 — Unprotected Burst Path

At least one structural path where burst traffic bypasses throttle controls. Name:
- The specific PA construct (trigger type, action type, loop type).
- The structural absence (no concurrency cap, no retry policy, unbounded parallel branch).

A path throttled at a higher limit does not qualify.

---

### Phase 4 — User Experience by Throttle Tier

For each distinct throttle tier in TABLE B: describe observable user-facing behavior —
error message, wait time, visible vs. silent failure. At least two tiers if multiple exist.

---

### Phase 5 — Cascading Throttle Failure Scenario

A scenario where throttling at one TABLE B tier triggers a second throttle event at a
different tier. Name both TABLE B rows, the causal link, and the compounded impact.

---

### Phase 6 — Tier Matrix and Mitigations

Fill TABLE C. Arithmetic column: step-by-step chain from named TABLE A limit to error rate,
citing TABLE A row numbers. For `?-unresolved` rows: state assumption, proceed.

Fill TABLE D. One row per FINDING-RH-NN (Phase 2) and one row per burst path (Phase 3).
Specific PA config: exact setting, formula with parameters, or queue integration point.

---

## V-03 — Role Sequence: Structural Incapability Declaration for Auditor

**Axis:** Role sequence — Role 4 (Consistency Auditor) opens with an explicit structural
incapability declaration: "I produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4.
I am structurally incapable of self-certifying these tables." This declaration precedes
Role 4's mandate. Role 4 cannot correct or amend prior tables — any correction attempt is
treated as a mandate violation. Standard ANTI-SUBSTITUTION placement (adjacent blockquote).
Standard correction gate with named tokens (not checkbox format, C-20 at baseline).

**Hypothesis:** R3-V-03 prohibited Role 4 from producing new analysis and from corrections,
relying on the prohibition to establish structural separation. A model running GATE 1 and
knowing it will run Role 4 can rationalize: "Role 4's no-correction mandate means it is
structurally separated." The explicit incapability declaration removes this rationalization
by stating the structural fact before the mandate: Role 4 cannot self-certify because it
has no stake in the tables, not merely because it is instructed not to. This framing shift
targets C-21 without changing the analytical content of Roles 1–3. V-01 and V-02 test
other mechanisms; V-03 tests the C-21 rationalization-suppression effect in isolation.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PRE-COMMITTED TABLE SCHEMAS

All four tables must appear in the final output with declared column structures intact.

**TABLE 1 — Component-Limit Inventory** *(Role 1 owns)*
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|

> Status tokens: `confirmed` | `estimated` | `?-unresolved` — no prose substitutions.
> ANTI-SUBSTITUTION: structured rows required. Prose listing fails.

**TABLE 2 — Backpressure Propagation Trace** *(Role 2 owns)*
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|

> Causal mechanism: specific technical cause per hop. Effect-label text fails.
> ANTI-SUBSTITUTION: structured rows required. Prose narrative fails.
> COMPONENT CONSTRAINT: All From/To entries must appear in TABLE 1.

**TABLE 3 — Volume-Multiplier Tier Matrix** *(Role 3 owns)*
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

> Arithmetic cites TABLE 1 row for each named limit. Error rate: numeric or bracketed.
> ANTI-SUBSTITUTION: exactly four rows required. Prose fails.

**TABLE 4 — Mitigation Prescriptions** *(Role 3 owns)*
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|

> Specific PA config: exact setting, formula with parameters, or integration point.
> ANTI-SUBSTITUTION: structured rows required. Prose list fails.

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

Every component from entry trigger to terminal action: add a TABLE 1 row. Generic labels fail.
Status: `confirmed`, `estimated`, or `?-unresolved` — no prose alternatives. Components with
unknown limits use `?-unresolved` — they are not omitted.

After TABLE 1: declare FIRST BOTTLENECK and annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Owns:** TABLE 2 + Retry-After Findings + Unprotected Burst Path + UX analysis + Cascading scenario

Fill TABLE 2 starting from FIRST BOTTLENECK:
- One row per directed hop (From → To).
- Causal mechanism: specific technical cause. Acceptable: "429 returned; no Retry-After handler;
  immediate retry within throttle window" or "concurrency cap reached; runtime queues trigger
  invocations; backlog accumulates." Failing: "also throttled", "cascade occurs", "propagates to",
  "downstream effect", "flow is affected", "rate limiting applies."
- All TABLE 1 components on the path appear as From or To. Off-path: `OUT-OF-PATH`.
- Only TABLE 1 components may appear in TABLE 2.

**GATE 1 — Retroactive Correction:** Before producing findings, scan TABLE 2 every Causal
mechanism cell for the failing-token patterns above. Any cell containing a failing token must
be rewritten with: (1) signal returned at From, (2) action response to that signal, (3) why
that response causes the Effect at To. GATE 1 is blocking — findings do not proceed until
every mechanism passes the failing-token scan.

After GATE 1 passes:
1. **Retry-After audit:** For each TABLE 2 hop receiving a 429 signal, check `Retry-After`
   handling. Produce `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap — missing concurrency cap, no retry policy,
   unbounded parallel branch. Name the PA construct and the structural absence.
3. **UX by throttle tier:** For each distinct TABLE 2 tier, describe observable user behavior
   (error message, wait time, visible vs. silent). At least two tiers if multiple exist.
4. **Cascading failure:** A scenario where throttling at one TABLE 2 tier triggers a second.
   Name both rows, causal link, compounded impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** TABLE 3 + TABLE 4

Fill TABLE 3. Arithmetic column shows step-by-step chain from named TABLE 1 limit to error rate:
> "TABLE 1 row 2: connector limit = 600 req/min. At 5×: inbound = 1500 req/min.
>  Excess = 900 req/min. Queue capacity = 300 (TABLE 1 row 4, estimated).
>  After saturation: 600/1500 = 40% error rate."

Each named limit must cite a specific TABLE 1 row. For `?-unresolved` TABLE 1 rows: state
assumption and proceed. Do not leave Arithmetic cells empty or conclude without the chain.

Fill TABLE 4. One row per FINDING-RH-NN and one row per burst path. Specific PA config:
exact setting, formula with parameters, or queue integration point. Generic guidance fails.

---

### ROLE 4 — Consistency Auditor

**STRUCTURAL DECLARATION (read before mandate):**
Role 4 produced no rows, no findings, and no analysis in TABLE 1, TABLE 2, TABLE 3, or
TABLE 4. Role 4 entered this simulation after Roles 1, 2, and 3 completed their work.
Self-certification of those tables is structurally impossible for Role 4 — Role 4 cannot
verify its own work because Role 4 produced none of the work being verified.

This is a structural fact, not an instruction. Role 4's incapability to self-certify is not
derived from a prohibition on corrections — it is derived from the absence of any Role 4
contribution to the tables being audited.

**Mandate:** Cross-table referential verification only. Role 4 produces flags and a verdict.
Role 4 does not produce new analysis, new findings, corrected tables, or amended rows.
If a deficiency is discovered, Role 4 flags it — the flag is the output. Correction is not.

**Check A — Propagation Phantom Scan**
List every From/To entry in TABLE 2. Cross-reference against TABLE 1. For each TABLE 2
component absent from TABLE 1:
`PHANTOM-NN: "[component]" — TABLE 2 Hop [N], absent from TABLE 1`

**Check B — Arithmetic Citation Audit**
For each TABLE 3 Arithmetic cell, identify every named numeric limit. For each limit not
traceable to a specific TABLE 1 row:
`CITATION-GAP-NN: TABLE 3 [multiplier] — "[limit text]" has no TABLE 1 source row`

**Check C — Mitigation Linkage Audit**
For each TABLE 4 Finding ID, verify it maps to a Role 2 FINDING-RH-NN or named burst path.
For each unmapped TABLE 4 row:
`ORPHAN-FINDING-NN: TABLE 4 row — "[ID]" has no Role 2 source`

**Check D — Table Completeness**
Verify all four required tables are present as structured tables with all columns intact.
For any required table replaced with prose or omitted:
`MISSING-TABLE-NN: [TABLE name] — absent or substituted with prose`

**Audit Verdict:**
No flags: `AUDIT RESULT: PASS — all tables present and structurally intact; no phantom
components; no arithmetic citation gaps; no orphan findings.`

Flags present: `AUDIT RESULT: FAIL — [counts by type]. Artifact requires correction.`
[List all flags in order: PHANTOM, CITATION-GAP, ORPHAN-FINDING, MISSING-TABLE]

---

## V-04 — Combined: At-header Placement + Checkbox Enumerated-token Gate

**Axis:** Combined (V-01 + V-02) — at-header ANTI-SUBSTITUTION placement for all four tables
and checkbox enumerated-token correction gate after TABLE B. No structural auditor separation
(C-21 at baseline — standard post-composition consistency check, not Role 4).

**Hypothesis:** C-19 (at-header placement) prevents the last-table substitution failure by
making the enforcement notice the syntactically first element at each table's row-production
point. C-20 (checkbox gate) prevents mechanism-label pass-through by requiring per-token
attestation at GATE 1. These two mechanisms target different failure modes and should be
complementary: placement discipline prevents table substitution; checkbox discipline prevents
causal mechanism evasion. V-04 tests whether they compose without prompt-length degradation
of essential criteria. V-05 adds the structural auditor for the full ceiling.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

This simulation produces four required tables (TABLE A, TABLE B, TABLE C, TABLE D).
All four must appear in the final output. Under token pressure, abbreviate analysis — never
replace a table with prose.

---

### Phase 0 — TABLE A: Component-Limit Inventory

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE A — AT-HEADER GATE]** Produce TABLE A data rows starting from the next line.
> Prose listing of components fails TABLE A. Each row must include:
> - PA construct type from the taxonomy below (generic labels fail).
> - Status token: `confirmed`, `estimated`, or `?-unresolved` — no inline prose.
> - Every component from entry trigger to terminal action. Unknown limits → `?-unresolved`,
>   not omitted.

PA construct type vocabulary:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE A: declare FIRST BOTTLENECK. Annotate that row `<-- FIRST BOTTLENECK`.

---

### Phase 1 — TABLE B: Backpressure Propagation Trace

| Hop | From component | To component | Causal mechanism | Effect observed |
|-----|---------------|-------------|-----------------|-----------------|
> **[TABLE B — AT-HEADER GATE]** Produce TABLE B data rows starting from the next line.
> Prose narrative of propagation fails TABLE B. Each row must include:
> - Causal mechanism: specific technical cause at this hop (see acceptable forms below).
> - From and To components that appear in TABLE A (no phantom components).
> - Off-path TABLE A components: row with Effect = `OUT-OF-PATH`.

Acceptable causal mechanism forms:
- "429 returned to action; no Retry-After handler; immediate retry within throttle window;
  connector re-throttles before window resets"
- "concurrency cap reached; PA runtime queues new trigger invocations; trigger backlog
  accumulates at PA runtime layer"

---

### GATE 1 — CHECKBOX TOKEN SCAN (BLOCKING)

Before Phase 2, run this scan against every Causal mechanism cell in TABLE B.
Mark each token `[CLEAR]` (not present) or `[FAIL: hop N — rewritten below]`.
Phase 2 does not begin until all boxes are resolved and all `[FAIL]` items have rewrites.

**Effect-label tokens (fail if present in any mechanism cell):**
- [ ] "also throttled"
- [ ] "also rate limited"
- [ ] "gets throttled"
- [ ] "is throttled"
- [ ] "rate limited"

**Causation-assertion tokens (fail if present):**
- [ ] "cascade occurs"
- [ ] "cascades to"
- [ ] "propagates to"
- [ ] "propagation"
- [ ] "throttle propagates"

**Vague-effect tokens (fail if present):**
- [ ] "downstream effect"
- [ ] "downstream impact"
- [ ] "flow is affected"
- [ ] "becomes affected"
- [ ] "is impacted"
- [ ] "experiences throttling"

**Passive-evasion tokens (fail if present):**
- [ ] "rate limiting applies"
- [ ] "throttling occurs"
- [ ] "throttling applies"
- [ ] "throttle applies"

**Rewrite format for `[FAIL]` items:** state (1) signal returned at From, (2) what the
action/runtime does in response, (3) why that causes the Effect at To.

**GATE 1 PASS CONDITION:** All boxes `[CLEAR]` or `[FAIL + rewrite]`. Unresolved `[ ]`
means the gate has not passed and Phase 2 may not begin.

---

### Phase 2 — Retry-After Handling Audit

For each TABLE B hop receiving a 429 or throttle signal, check `Retry-After` handling.
`FINDING-RH-NN: [component] — [specific gap]` for each missing handler.
If no gaps: "No Retry-After handling gaps found."

---

### Phase 3 — Unprotected Burst Path

At least one structural path bypassing throttle controls. Name the PA construct and the
structural absence. A path throttled at a higher limit does not qualify.

---

### Phase 4 — User Experience by Throttle Tier

For each distinct TABLE B tier: observable user behavior — error message, wait time,
visible vs. silent failure. At least two tiers if multiple exist.

---

### Phase 5 — Cascading Throttle Failure Scenario

Throttling at one TABLE B tier triggers a second throttle event at a different tier.
Name both TABLE B rows, the causal link, and the compounded impact.

---

### Phase 6 — TABLE C: Volume-Multiplier Tier Matrix

| Multiplier | Est. req/min | First throttle tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|------------------------|---------|----------------|------------|
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |
> **[TABLE C — AT-HEADER GATE]** Produce TABLE C data rows filling the four rows above.
> Prose description of load behavior fails TABLE C. Each row must include:
> - Est. error rate: numeric or bracketed range (e.g., "8–12%"). Qualitative labels fail.
> - Arithmetic: step-by-step chain naming each TABLE A limit with row citation (e.g.,
>   "TABLE A row 2: limit = 600 req/min. At 5×: inbound = 1500. Excess = 900.
>   TABLE A row 4 queue = 300 (estimated). Saturation: 600/1500 = 40% error rate.").
> - `?-unresolved` TABLE A rows used in arithmetic: state the assumption explicitly.

Note: the four multiplier rows appear above this gate. Fill those rows.

---

### Phase 7 — TABLE D: Mitigation Prescriptions

| Finding ID | Root cause | Prescribed remediation | Specific PA config or pattern |
|-----------|-----------|----------------------|------------------------------|
> **[TABLE D — AT-HEADER GATE — FINAL TABLE]** Produce TABLE D data rows starting from
> the next line. Prose list of recommendations fails TABLE D. Each row must include:
> - One row per FINDING-RH-NN (Phase 2) and one row per burst path (Phase 3).
> - Specific PA config: exact setting, backoff formula with parameters, or queue
>   integration point. Generic guidance ("add retry logic") fails this column.

---

**Post-simulation consistency check:** Verify all TABLE B From/To components appear in
TABLE A. Verify all TABLE C arithmetic named limits trace to TABLE A rows. Flag any
discrepancies as `INCONSISTENCY-NN: [description]` before finalizing.

---

## V-05 — Combined: At-header Enforcement + Checkbox Gate + Structurally Incapable Auditor

**Axis:** Combined — V-01 (at-header ANTI-SUBSTITUTION for all four tables), V-02 (checkbox
enumerated-token correction gate at GATE 1), and V-03 (structurally incapable auditor with
explicit incapability declaration) integrated into a four-role prompt.

**Hypothesis:** C-19 requires local enforcement at the exact production point of each table —
achieved by at-header placement (no blank line between separator and gate notice). C-20 requires
the correction gate to enumerate specific failing token strings as checkable items — achieved by
checkbox scan protocol that must be explicitly resolved before advancement. C-21 requires the
consistency auditor to be structurally incapable of self-certifying — achieved by an opening
declaration at Role 4 entry that states the structural fact before the mandate. Each mechanism
addresses a distinct failure mode: last-table substitution, mechanism-label evasion, and
self-verification rationalization. V-04 confirms C-19+C-20 stack without prompt bloat. V-05
adds C-21 and tests the full ceiling of aspirational compliance under a single execution.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PRE-COMMITTED TABLE SCHEMAS

Four tables required in the final output. Under token pressure, abbreviate analysis — do not
substitute a prose section for any table.

*(Schemas are declared here for reference. At-header production gates are embedded at the
production point of each table within their owning role.)*

TABLE 1: Component | PA construct type | Numeric limit | Unit | Status (`confirmed`/`estimated`/`?-unresolved`)
TABLE 2: Hop | From | To | Causal mechanism | Effect
TABLE 3: Multiplier (1×/3×/5×/10×) | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic
TABLE 4: Finding ID | Root cause | Prescribed remediation | Specific PA config

---

### ROLE 1 — Domain Expert

**Owns:** TABLE 1 + Bottleneck Declaration

**TABLE 1 — Component-Limit Inventory**
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE 1 — AT-HEADER GATE]** Produce TABLE 1 data rows starting from the next line.
> Requirements active at this production point:
> - PA construct type from the taxonomy below. Generic labels fail.
> - Status token: `confirmed` / `estimated` / `?-unresolved` — one per row, no prose.
> - Every component from entry trigger to terminal action has a row.
>   Unknown limits → `?-unresolved`, not omitted.
> - Prose listing of components fails TABLE 1.

PA construct type vocabulary:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE 1: declare FIRST BOTTLENECK. Annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Owns:** TABLE 2 + Retry-After Findings + Unprotected Burst Path + UX analysis + Cascading scenario

**TABLE 2 — Backpressure Propagation Trace**
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
> **[TABLE 2 — AT-HEADER GATE]** Produce TABLE 2 data rows starting from the next line.
> Requirements active at this production point:
> - Causal mechanism: specific technical cause at this hop (see acceptable forms below).
> - From/To: TABLE 1 components only. No phantom components.
> - Off-path TABLE 1 components: Effect = `OUT-OF-PATH`.
> - Prose narrative of propagation fails TABLE 2.

Acceptable causal mechanism forms:
- "429 returned to action; no Retry-After handler present; immediate retry within throttle
  window; connector re-throttles before window resets"
- "concurrency cap reached; PA runtime queues new trigger invocations; trigger backlog
  accumulates at PA runtime layer"

---

**GATE 1 — CHECKBOX TOKEN SCAN (BLOCKING)**

Before producing findings: run this scan against every TABLE 2 Causal mechanism cell.
Mark each `[CLEAR]` or `[FAIL: hop N — rewritten below]`. Findings do not proceed until
all boxes are resolved and all `[FAIL]` items have explicit rewrites immediately after
this checklist.

Effect-label tokens:
- [ ] "also throttled"
- [ ] "also rate limited"
- [ ] "gets throttled"
- [ ] "is throttled"
- [ ] "rate limited"

Causation-assertion tokens:
- [ ] "cascade occurs"
- [ ] "cascades to"
- [ ] "propagates to"
- [ ] "propagation"
- [ ] "throttle propagates"

Vague-effect tokens:
- [ ] "downstream effect"
- [ ] "downstream impact"
- [ ] "flow is affected"
- [ ] "becomes affected"
- [ ] "is impacted"
- [ ] "experiences throttling"

Passive-evasion tokens:
- [ ] "rate limiting applies"
- [ ] "throttling occurs"
- [ ] "throttling applies"
- [ ] "throttle applies"

**Rewrite format:** (1) signal returned at From, (2) action/runtime response to that signal,
(3) why that response causes the Effect at To.

**GATE 1 PASS CONDITION:** All boxes `[CLEAR]` or `[FAIL + rewrite provided]`.
Any `[ ]` box means GATE 1 has not passed.

---

After GATE 1 passes, produce:

1. **Retry-After audit:** For each TABLE 2 hop receiving a 429 signal, check `Retry-After`
   handling. Produce `FINDING-RH-NN: [component] — [specific gap]`.

2. **Unprotected burst path:** One structural gap — missing concurrency cap, no retry policy,
   unbounded parallel branch. Name the PA construct and the structural absence.

3. **User experience by throttle tier:** For each distinct TABLE 2 tier, describe observable
   user behavior — error message, wait time, visible vs. silent failure. At least two tiers
   if multiple exist.

4. **Cascading failure scenario:** Throttling at one TABLE 2 tier triggers a second throttle
   event at a different tier. Name both TABLE 2 rows, the causal link, and the compounded
   impact on throughput or error rate.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** TABLE 3 + TABLE 4

**TABLE 3 — Volume-Multiplier Tier Matrix**
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |
> **[TABLE 3 — AT-HEADER GATE]** Fill the four multiplier rows above with data.
> Requirements active at this production point:
> - Exactly four rows (1×/3×/5×/10×). Free-form labels or fewer rows fail.
> - Est. error rate: numeric or bracketed range (e.g., "8–12%"). Qualitative labels fail.
> - Arithmetic: step-by-step chain naming each TABLE 1 row and limit used. Example:
>   "TABLE 1 row 2: connector limit = 600 req/min. At 5×: inbound = 1500 req/min.
>    Excess = 900 req/min. TABLE 1 row 4 queue capacity = 300 (estimated).
>    After saturation: 600/1500 = 40% error rate."
> - `?-unresolved` TABLE 1 rows used in arithmetic: state assumption explicitly.
> - Prose description of load behavior fails TABLE 3.

**TABLE 4 — Mitigation Prescriptions**
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> **[TABLE 4 — AT-HEADER GATE — FINAL TABLE]** This is the fourth and last required table.
> Produce TABLE 4 data rows starting from the next line. Requirements active here:
> - One row per FINDING-RH-NN (Role 2) and one row per burst path (Role 2).
> - Specific PA config: exact setting, formula with parameters, or queue integration point
>   (e.g., "Trigger concurrency: set to 1 in trigger settings panel" or "Exponential
>   backoff: base 10s, multiplier 2×, max 5 retries, jitter ±20%").
> - Generic guidance ("add retry logic", "implement throttle handling") fails this column.
> - Prose list of recommendations fails TABLE 4.

---

### ROLE 4 — Consistency Auditor

**STRUCTURAL DECLARATION (precedes mandate — read first):**

Role 4 produced no rows, no findings, and no analytical content in TABLE 1, TABLE 2,
TABLE 3, or TABLE 4. Role 4 entered this simulation after Roles 1, 2, and 3 completed
their analytical work. Role 4 has no stake in any of the tables being audited.

Self-certification of TABLE 1, TABLE 2, TABLE 3, or TABLE 4 is structurally impossible
for Role 4. This is not derived from an instruction prohibiting self-certification — it
is derived from the structural fact that Role 4 produced nothing in those tables. An
auditor cannot self-certify what it did not create.

**Mandate:** Cross-table referential verification. Role 4 produces flags and a verdict.
Role 4 does not produce new analysis, new findings, corrected data rows, or amended tables.
If Role 4 discovers a deficiency, the output is a flag — not a correction.

---

**Check A — Propagation Phantom Scan**

List every component appearing as From or To in TABLE 2. For each, verify it appears in
TABLE 1. For each TABLE 2 component absent from TABLE 1:
`PHANTOM-NN: "[component]" — TABLE 2 Hop [N], no TABLE 1 row`

**Check B — Arithmetic Citation Audit**

For each TABLE 3 Arithmetic cell, list every named numeric limit. For each limit, verify it
traces to a specific TABLE 1 row by row number or component name. For each that cannot be
traced:
`CITATION-GAP-NN: TABLE 3 [multiplier] row — "[limit text]" has no TABLE 1 source row`

**Check C — Mitigation Linkage Audit**

For each TABLE 4 Finding ID, verify it corresponds to a Role 2 FINDING-RH-NN or a named
unprotected burst path. For each TABLE 4 row without a traceable source:
`ORPHAN-FINDING-NN: TABLE 4 row — "[ID]" has no Role 2 source`

**Check D — Table Completeness**

Verify all four required tables (TABLE 1, TABLE 2, TABLE 3, TABLE 4) are present as
structured tables with all declared columns intact. For any required table absent or
replaced with prose:
`MISSING-TABLE-NN: [TABLE name] — absent or substituted with prose`

---

**Audit Verdict:**

No flags:
`AUDIT RESULT: PASS — all four tables present and structurally intact; no phantom
components; no arithmetic citation gaps; no orphan findings. Artifact is consistent.`

Flags present:
`AUDIT RESULT: FAIL — [N phantom], [N citation gap], [N orphan finding], [N missing table].
Artifact requires correction before finalization.`
[Flag list in order: PHANTOM, CITATION-GAP, ORPHAN-FINDING, MISSING-TABLE]
