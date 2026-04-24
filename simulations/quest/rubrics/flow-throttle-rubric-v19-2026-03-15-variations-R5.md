# flow-throttle — Round 5 Variations (v19 Rubric)

## Context and Variation Strategy

v19 adds three new aspirational criteria (C-22, C-23, C-24) derived from R4 excellence signals.
Each criterion codifies a mechanism that appeared in an R4 variation's passing behavior:

| ID | Signal Source | What the criterion requires | Why R4 output sometimes missed it |
|----|--------------|----------------------------|------------------------------------|
| C-22 | V-02 C-20 PASS (checkbox `- [ ]` per-token attestation) | Per-token binary attestation — each named token receives an individual `[CLEAR]` or `[FAIL: hop N — rewritten below]` disposition. A holistic "all tokens reviewed" verdict passes C-20 but fails C-22. | R4-V-02 introduced checkbox format but the model could resolve the entire category with a single pass statement rather than one `[CLEAR]` / `[FAIL]` per token — collective attestation mode remained open. |
| C-23 | V-03 C-21 focus (structural incapability preamble) | The consistency auditor opens with a structural fact statement establishing incapability — "Role 4 has no output in Tables 1–3, it cannot rationalize its own prior choices because it made none" — before the verification mandate. Role declared separate (C-21) but without the incapability preamble fails C-23. | R4-V-03 had an incapability declaration but it included the phrase "Self-certification is structurally impossible" as a framing device after the instruction — a model can still rationalize that its "instructed separation" is equivalent to a structural fact, leaving the rationalization path partially open. |
| C-24 | V-01 C-19 PARTIAL (TABLE C stub-row gap) | When a table schema includes pre-filled stub rows (e.g., `\| 1× \| \| \|`), the enforcement notice must be placed between the column header separator (`\|---\|---\|`) and the first stub row — not after them. Stub rows are scaffolding, not production output. Can pass C-19 on stub-free tables while failing C-24 on a stub-bearing table. | R4-V-01's TABLE C placed the `[TABLE C PRODUCTION GATE]` notice after the four `\| 1× \|` / `\| 3× \|` / `\| 5× \|` / `\| 10× \|` pre-filled rows with text "fill the four rows above." Under token pressure, TABLE C was the last heavy table; the gate arrived too late in the row-production sequence to prevent early row elision. |

**R5 design goals:**
1. C-24 isolation: does placing TABLE C's enforcement notice between `\|---\|` and the first pre-filled
   stub row — with the instruction reading "fill the four rows below" rather than "above" — produce
   more reliable stub-row completion than R4-V-01's post-stub placement? (V-01)
2. C-22 isolation: does requiring per-token `- [ ]` checkboxes each resolved individually to `[CLEAR]`
   or `[FAIL: hop N — rewritten below]` prevent the collective-attestation mode that R4-V-02 left
   open? (V-02)
3. C-23 isolation: does opening Role 4 with a declarative structural-fact statement in past-tense
   active voice — "Role 4 produced no rows. It made no choices." — foreclose the rationalization
   path more reliably than R4-V-03's framing-device incapability? (V-03)
4. C-22+C-24 stacking: do per-token attestation and stub-row gate placement compose cleanly without
   the TABLE C gate instructions conflicting with GATE 1 scan instructions? (V-04)
5. Full ceiling: do all three mechanisms (C-22+C-23+C-24) compose stably in a single Role-based
   prompt targeting all 24 criteria? (V-05)

Three single-axis variations (V-01, V-02, V-03), then two combined (V-04, V-05):

| Variation | Primary axis | C-22 | C-23 | C-24 | Predicted composite |
|-----------|-------------|------|------|------|---------------------|
| V-01 | Output format — stub-row-proof TABLE C and TABLE D gate placement | baseline | baseline | PASS | ~93/100 |
| V-02 | Lifecycle emphasis — per-token binary attestation checkbox scan | PASS | baseline | baseline | ~93/100 |
| V-03 | Role sequence — incapability preamble as structural-fact statement | baseline | PASS | baseline | ~93/100 |
| V-04 | Combined: per-token attestation + stub-row gate | PASS | baseline | PASS | ~96/100 |
| V-05 | Combined: per-token attestation + incapability preamble + stub-row gate | PASS | PASS | PASS | ~100/100 |

---

## V-01 — Output Format: Stub-Row-Proof Gate Placement

**Axis:** Output format — every table that includes pre-filled stub rows in its schema
declaration has its enforcement notice placed immediately between the column header separator
(`|---|---|`) and the first stub row. The notice fires before any scaffold row is produced, not
after. TABLE C (volume-multiplier matrix) and TABLE D (mitigation prescriptions) both carry
pre-filled stub rows in this variation; both receive between-separator-and-stub placement. TABLE A
and TABLE B have no stubs — they receive standard at-header placement. C-22 left at baseline
(named-token list, no per-token checkboxes). C-23 left at baseline (no Role 4 structural preamble).

**Hypothesis:** R4-V-01 proved that zero-gap at-header placement improves compliance on early
tables. Its gap was TABLE C, where `[TABLE C PRODUCTION GATE]` appeared after the four pre-filled
rows (`1×`, `3×`, `5×`, `10×`) with the phrasing "fill the four rows above." Under token pressure
on the last analytical table, the model reads the gate after the scaffolding is already in context
and treats the stub rows as completed output. Placing the gate before the first `| 1× |` stub row
— with the phrasing "fill the four rows immediately below this notice" — fires at the production
point for that table's rows, not retrospectively. TABLE D stub placement extends the same treatment
to the final table, closing the identical gap on the mitigation output.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

This simulation produces four required tables. All four must appear in the final output with
column structure intact. Under token pressure, abbreviate analytical commentary — do not
replace any table with prose.

---

### Phase 0 — TABLE A: Component-Limit Inventory

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE A PRODUCTION GATE]** You are now producing TABLE A rows. Start the first `| # |`
> data row immediately below this notice. Requirements active at this production point:
> - Every component from entry trigger to terminal action must appear as a TABLE A row.
>   Components with unknown limits use `?-unresolved` — they are not omitted.
> - `PA construct type` must use the taxonomy below — generic labels ("API limit",
>   "service rate limit") fail this column.
> - `Status` must be exactly one of: `confirmed` | `estimated` | `?-unresolved`
>   Prose uncertainty ("limit unclear", "may vary", "approximately X") fails this column.
> - `Numeric limit` must be a number with a unit. For `?-unresolved` rows, provide a
>   documented default or platform estimate, or write `unknown` with a note.
> - Structured table rows only — a prose paragraph listing components fails TABLE A entirely.

PA construct type vocabulary (use only these):
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE A is complete: declare the **FIRST BOTTLENECK** — the component whose limit is hit
first at the given request volume. Annotate that row `<-- FIRST BOTTLENECK`.

---

### Phase 1 — TABLE B: Backpressure Propagation Trace

| Hop | From component | To component | Causal mechanism | Effect observed |
|-----|---------------|-------------|-----------------|-----------------|
> **[TABLE B PRODUCTION GATE]** You are now producing TABLE B rows. Start the first `| Hop |`
> data row immediately below this notice. Requirements active at this production point:
> - `Causal mechanism` must name the specific technical cause at each hop. Acceptable forms:
>   "429 returned to action; no Retry-After handler present; immediate retry issued within
>   same throttle window; connector re-throttles before window resets" or "concurrency cap
>   reached; PA runtime queues new trigger invocations; trigger backlog accumulates."
>   Failing forms: "also throttled", "cascade occurs", "propagates to", "downstream effect",
>   "flow is affected", "rate limiting applies" — these name effects, not mechanisms.
> - Every From/To component must appear in TABLE A. No components absent from TABLE A may
>   be introduced in TABLE B (no phantom components).
> - All TABLE A components on the propagation path must appear as From or To. Off-path
>   components receive Effect = `OUT-OF-PATH`.
> - Minimum two directed hops from the FIRST BOTTLENECK.

---

**Correction Checkpoint:** Before Phase 2, scan every TABLE B `Causal mechanism` cell.
Any cell matching the failing-token patterns above requires rewriting: state (1) the signal
returned at From, (2) what the action or runtime does in response, and (3) why that response
causes the Effect at To. Rewrite deficient rows before proceeding.

---

### Phase 2 — Retry-After Handling Audit

For each TABLE B hop where a 429 or throttle signal is received, check whether the flow reads
and honors the `Retry-After` header or equivalent backoff signal. Produce:

`FINDING-RH-NN: [component name] — [specific gap description]`

for each missing handler. If no gaps exist, state explicitly: "No Retry-After handling gaps found."

---

### Phase 3 — Unprotected Burst Path

Identify at least one path where burst traffic bypasses throttle controls. Name:
- The specific PA construct (trigger type, action type, loop type).
- The structural absence (no concurrency cap configured, no retry policy, unbounded parallel branch).

A path throttled at a higher limit does not qualify — the control must be structurally absent.
If no unprotected path exists, state the conclusion and the evidence explicitly.

---

### Phase 4 — User Experience by Throttle Tier

For each distinct throttle tier reached in the TABLE B propagation trace, describe the
observable user-facing behavior: what the user sees (429 error message, queue delay, flow run
failure with error code, silent retry), how long they wait, and whether failure is visible or
silent. Cover at least two tiers if multiple tiers exist.

---

### Phase 5 — Cascading Throttle Failure Scenario

Construct a scenario where throttling at one TABLE B tier triggers a second throttle event at
a different tier. Name both TABLE B rows, the causal link between them, and the compounded
effect on throughput or error rate.

---

### Phase 6 — TABLE C: Volume-Multiplier Tier Matrix

| Multiplier | Est. req/min | First throttle tier hit | Behavior at this tier | Est. error rate | Arithmetic |
|-----------|-------------|------------------------|----------------------|----------------|------------|
> **[TABLE C PRODUCTION GATE]** You are now producing TABLE C rows. Fill the four rows
> immediately below this notice. Requirements active at this production point:
> - Exactly these four multiplier rows are required in order. Do not reorder or omit any.
> - `Est. error rate` must be a numeric value or bracketed range (e.g., "8–12%").
>   Qualitative labels ("high", "moderate") fail this column.
> - `Arithmetic` must show step-by-step calculation naming each TABLE A limit used, citing
>   the TABLE A row number. Example: "TABLE A row 2: connector limit = 600 req/min.
>   At 5×: inbound = 1,500 req/min. Excess = 900 req/min. TABLE A row 4 queue capacity =
>   300 (estimated). After queue saturation: 600/1,500 = 40% throttled."
>   A stated conclusion without the arithmetic chain fails this column.
> - For `?-unresolved` TABLE A rows: state the assumption explicitly and proceed.
> - A prose description of how behavior changes with load fails TABLE C entirely.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

---

### Phase 7 — TABLE D: Mitigation Prescriptions

| Finding ID | Root cause | Prescribed remediation | Specific PA config or pattern |
|-----------|-----------|----------------------|------------------------------|
> **[TABLE D PRODUCTION GATE — FINAL TABLE]** You are now producing TABLE D rows. Fill the
> rows immediately below this notice. Requirements active at this production point:
> - One row per FINDING-RH-NN from Phase 2. One row per unprotected burst path from Phase 3.
> - `Specific PA config` must name the exact setting, backoff formula with parameters, or
>   queue integration point. Examples: "Trigger concurrency: set to 1 in trigger settings
>   panel" or "Exponential backoff: base 10s, multiplier 2×, max 5 retries, jitter ±20%."
>   Generic guidance ("add retry logic", "implement throttle handling") fails this column.
> - A prose list of recommendations fails TABLE D entirely.
| F-01 | | | |

---

**Output Verification:** Before finalizing, confirm TABLE A, TABLE B, TABLE C, and TABLE D
are all present as structured tables with column structures intact. If any required table was
replaced with prose, rewrite it as a table.

---

## V-02 — Lifecycle Emphasis: Per-token Binary Attestation

**Axis:** Lifecycle emphasis — GATE 1 (the correction gate after TABLE B) is restructured as
a per-token binary attestation phase. Each failing token is a `- [ ]` checkbox item. Every
checkbox must be individually resolved to exactly one of: `[CLEAR]` (the token is absent from
all Causal mechanism cells) or `[FAIL: hop N — rewritten below]` (the token is present at hop
N; a rewrite follows immediately after the checklist). A holistic "all tokens reviewed" statement
does not pass GATE 1. Unresolved `- [ ]` items mean the gate has not passed. C-23 left at
baseline (no Role 4 incapability preamble). C-24 left at baseline (standard at-header placement
for all tables, no stub-row adjustment).

**Hypothesis:** R4-V-02 introduced checkboxes as a format but the model could satisfy the
gate by producing a collective attestation: "Reviewed all tokens — none found." The `[CLEAR]`
or `[FAIL]` resolution was possible to perform as a single batch rather than per-token. The
R5 variation requires that each of the 23 named tokens receives its own checkbox item resolved
independently. This makes the gate machine-auditable: an evaluator counts unresolved `- [ ]`
items. If any box lacks a disposition, GATE 1 has not passed and Phase 2 cannot begin.
The `[FAIL: hop N — rewritten below]` form additionally pins failure to a specific location,
enabling targeted rewrite rather than whole-section regeneration.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

This simulation produces four required tables. All four must appear in the final output with
column structures intact. Under token pressure, abbreviate analytical commentary — do not
replace any table with prose.

---

### OUTPUT SCHEMA — Four Required Tables

**TABLE A — Component-Limit Inventory**
| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> ANTI-SUBSTITUTION: Structured rows only. Prose listing fails.
> Status vocabulary — exactly: `confirmed` | `estimated` | `?-unresolved`

**TABLE B — Backpressure Propagation Trace**
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
> ANTI-SUBSTITUTION: Structured rows only. Prose narrative fails.
> COMPONENT CONSTRAINT: All From/To entries must appear in TABLE A.

**TABLE C — Volume-Multiplier Tier Matrix**
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
| 1× | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |
> ANTI-SUBSTITUTION: Exactly four rows (1×/3×/5×/10×) required. Prose fails.
> Arithmetic cites TABLE A row for each named limit. Error rate is numeric or bracketed.

**TABLE D — Mitigation Prescriptions**
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> ANTI-SUBSTITUTION: Structured rows only. Prose list fails.
> Specific PA config: exact setting, formula with parameters, or integration point.

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
Status: `confirmed`, `estimated`, or `?-unresolved` — no prose alternatives. Components with
unknown limits use `?-unresolved` — they are not omitted.

After TABLE A: declare FIRST BOTTLENECK, annotate that row `<-- FIRST BOTTLENECK`.

---

### Phase 1 — Backpressure Propagation Trace

Fill TABLE B starting from FIRST BOTTLENECK. One row per directed hop (From → To).
- Causal mechanism: specific technical cause at this hop.
  - Acceptable: "429 returned to action; no Retry-After handler present; immediate retry issued
    within same throttle window; connector re-throttles before window resets"
  - Acceptable: "concurrency cap reached; PA runtime queues trigger invocations; trigger backlog
    accumulates at runtime layer"
  - Failing tokens (see GATE 1 below): "also throttled", "cascade occurs", "propagates to",
    "downstream effect", "flow is affected", "rate limiting applies", and all listed equivalents.
- All TABLE A components on path appear as From or To. Off-path components: `OUT-OF-PATH`.
- Only TABLE A components appear in TABLE B.

---

### GATE 1 — PER-TOKEN BINARY ATTESTATION (BLOCKING)

Before Phase 2 begins, resolve each token below individually. For each token:
- Write `[CLEAR]` after the token text if the exact string (or close paraphrase) is absent
  from every Causal mechanism cell in TABLE B.
- Write `[FAIL: hop N — rewritten below]` if the token or a close paraphrase appears at hop N.
  Immediately after the full checklist, provide the rewrite for that hop.

**Every `- [ ]` must be resolved. Any unresolved box means GATE 1 has not passed and
Phase 2 does not begin.**

**Category A — Pure effect labels:**
- [ ] "also throttled"
- [ ] "also rate limited"
- [ ] "gets throttled"
- [ ] "is throttled"
- [ ] "rate limited"

**Category B — Causation assertions without mechanism:**
- [ ] "cascade occurs"
- [ ] "cascades to"
- [ ] "cascading throttle"
- [ ] "propagates to"
- [ ] "propagation"
- [ ] "throttle propagates"

**Category C — Vague effect descriptions:**
- [ ] "downstream effect"
- [ ] "downstream impact"
- [ ] "flow is affected"
- [ ] "becomes affected"
- [ ] "is impacted"
- [ ] "experiences throttling"

**Category D — Passive mechanism evasions:**
- [ ] "rate limiting applies"
- [ ] "throttling occurs"
- [ ] "throttling applies"
- [ ] "throttle applies"
- [ ] "is limited"
- [ ] "gets limited"
- [ ] "hits the limit"

**Rewrite format for any `[FAIL]` items (provide immediately after the full checklist):**
State: (1) what signal is returned at the From component, (2) what the action, runtime, or
connector does in response to that signal, and (3) why that response causes the Effect at To.

**GATE 1 PASS CONDITION:** All 23 tokens individually resolved. Any `- [ ]` without a
disposition = gate not passed.

---

### Phase 2 — Retry-After Handling Audit

For each TABLE B hop receiving a 429 or throttle signal, check whether the flow reads and
honors the `Retry-After` header. Produce `FINDING-RH-NN: [component] — [specific gap]`.
If no gaps exist, state "No Retry-After handling gaps found."

---

### Phase 3 — Unprotected Burst Path

At least one structural path where burst traffic bypasses throttle controls. Name the specific
PA construct and the structural absence. A path throttled at a higher limit does not qualify.
If no path exists, state the conclusion and evidence.

---

### Phase 4 — User Experience by Throttle Tier

For each distinct TABLE B throttle tier: describe observable user-facing behavior — error code,
wait time, visible vs. silent. At least two tiers if multiple exist.

---

### Phase 5 — Cascading Throttle Failure Scenario

A scenario where throttling at one TABLE B tier triggers a second throttle event at a different
tier. Name both TABLE B rows, the causal link, and the compounded throughput or error rate impact.

---

### Phase 6 — Tier Matrix and Mitigations

Fill TABLE C. Arithmetic column: step-by-step chain from named TABLE A limit to error rate,
citing TABLE A row numbers. For `?-unresolved` rows: state assumption, proceed.

Fill TABLE D. One row per FINDING-RH-NN from Phase 2. One row per burst path from Phase 3.
Specific PA config: exact setting, formula with parameters, or queue integration point.

---

## V-03 — Role Sequence: Structural Incapability Preamble as Declarative Fact

**Axis:** Role sequence — Role 4 (Consistency Auditor) opens with a structural fact statement
written in declarative active voice, establishing why it is incapable of self-certifying the
tables it is auditing. The statement names the specific tables and phases Role 4 had no output
in, and states explicitly that Role 4 cannot rationalize its own prior choices because it made
none. This structural-fact preamble precedes the verification mandate. C-22 left at baseline
(named-token correction gate in GATE 1, no per-token checkboxes). C-24 left at baseline
(standard at-header placement, no stub-row adjustment).

**Hypothesis:** R4-V-03 opened Role 4 with: "Role 4 produced no rows, no findings, and no
analysis... Self-certification of those tables is structurally impossible for Role 4." The
phrase "structurally impossible" is a framing device that could still allow rationalization —
a model running Role 4 can interpret "structurally impossible" as a strong instruction and then
still reason about what the tables "should" contain based on how other roles "would have"
produced them. The R5 preamble uses pure declarative fact: "Role 4 produced no rows in
TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the component limits, the
propagation hops, or the tier arithmetic. It cannot rationalize its own prior choices because
it made none." Past-tense active voice ("it did not produce") is structurally different from
"self-certification is impossible" — the former states a fact about what occurred; the latter
states a conclusion about capability. The fact form forecloses rationalization by establishing
the record, not by asserting a prohibition.

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
> ANTI-SUBSTITUTION: structured rows only. Prose listing fails.

**TABLE 2 — Backpressure Propagation Trace** *(Role 2 owns)*
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
> Causal mechanism: specific technical cause per hop. Effect-label text fails.
> ANTI-SUBSTITUTION: structured rows only. Prose narrative fails.
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
> ANTI-SUBSTITUTION: structured rows only. Prose list fails.

---

### ROLE 1 — Domain Expert

**Owns:** TABLE 1 + Bottleneck Declaration

Fill TABLE 1. PA construct type from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
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
**Owns:** TABLE 2 + Retry-After Findings + Unprotected Burst Path + UX analysis + Cascade scenario

Fill TABLE 2 starting from FIRST BOTTLENECK:
- One row per directed hop (From → To).
- Causal mechanism: specific technical cause. Failing text: "also throttled", "cascade occurs",
  "propagates to", "downstream effect", "flow is affected", "rate limiting applies."
- All TABLE 1 components on path: appear as From or To. Off-path: `OUT-OF-PATH`.
- Only TABLE 1 components appear in TABLE 2.

**GATE 1 — Mechanism Correction (BLOCKING):** Before producing findings, scan every TABLE 2
Causal mechanism cell. Any cell containing failing-token text must be rewritten with:
(1) signal returned at From, (2) action response to that signal, (3) why that response causes
the Effect at To. GATE 1 must pass before findings proceed.

After GATE 1 passes:
1. **Retry-After audit:** For each hop receiving a 429 signal, check `Retry-After` handling.
   Produce `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap — missing concurrency cap, no retry policy,
   unbounded parallel branch. Name PA construct and structural absence.
3. **UX by throttle tier:** Each distinct tier — error code, wait time, visible vs. silent.
   At least two tiers if multiple exist.
4. **Cascading failure:** Throttling at one TABLE 2 tier triggers a second. Name both rows,
   causal link, compounded impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** TABLE 3 + TABLE 4

Fill TABLE 3. Arithmetic: step-by-step chain naming each TABLE 1 row used:
> "TABLE 1 row 2: connector limit = 600 req/min. At 5×: inbound = 1,500 req/min.
>  Excess = 900 req/min. Queue capacity = 300 (TABLE 1 row 4, estimated).
>  After queue saturation: 600/1,500 = 40% error rate."

Do not leave Arithmetic empty or state conclusions without the chain. For `?-unresolved`
TABLE 1 rows: state the assumption and proceed.

Fill TABLE 4. One row per FINDING-RH-NN and one row per burst path. Specific PA config:
exact setting, formula with parameters, or queue integration point. Generic guidance fails.

---

### ROLE 4 — Consistency Auditor

**Structural fact (read before mandate):**
Role 4 produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the
component-limit entries, the propagation trace hops, the tier arithmetic, or the mitigation
prescriptions. Role 1 produced TABLE 1. Role 2 produced TABLE 2 and the findings. Role 3
produced TABLE 3 and TABLE 4. Role 4 entered this simulation after all analytical work was
complete. Role 4 cannot rationalize its own prior choices because it made none.

**Verification mandate:**
Cross-table referential consistency only. Role 4 produces flags and a verdict. Role 4 does
not produce new analysis, corrected tables, or amended rows. If a deficiency is discovered,
Role 4 flags it — the flag is the output. Correction is not.

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

## V-04 — Combined: Per-token Binary Attestation + Stub-Row-Proof Gate Placement

**Axis:** Combined (V-01 + V-02) — TABLE C and TABLE D carry enforcement notices placed
between the column header separator and the first pre-filled stub row (C-24), and GATE 1 uses
per-token `- [ ]` binary attestation requiring individual `[CLEAR]` / `[FAIL: hop N]`
disposition per token (C-22). No Role 4 structural separation (C-23 at baseline — standard
post-completion consistency check, not a structurally incapable auditor role).

**Hypothesis:** C-24 addresses the stub-row scaffolding gap in TABLE C and TABLE D — the gap
where pre-filled rows buffer the model from the production-point enforcement notice. C-22
addresses the collective-attestation loophole in GATE 1 — the gap where the model can declare
all tokens clear without individually checking each. These two mechanisms target orthogonal
failure modes: placement discipline prevents gate-arrival-too-late for stub-bearing tables;
per-token attestation prevents batch-pass mode in the correction gate. Combining them without
Role 4 isolation tests whether the two format mechanisms compose cleanly before adding the
role-separation overhead of V-05. If V-04 achieves similar composite to V-05, Role 4 isolation
may be redundant for this skill; if V-04 underperforms V-05, C-23 is load-bearing.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

This simulation produces four required tables (TABLE A, TABLE B, TABLE C, TABLE D).
All four must appear in the final output with column structure intact. Under token pressure,
abbreviate analytical commentary — do not replace any table with prose.

---

### Phase 0 — TABLE A: Component-Limit Inventory

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE A PRODUCTION GATE]** You are now producing TABLE A rows. Start the first `| # |`
> data row immediately below this notice. Requirements active at this production point:
> - Every component from entry trigger to terminal action must have a row.
>   Unknown limits: use `?-unresolved` status — do not omit.
> - `PA construct type` must use the PA taxonomy listed below.
> - `Status` must be exactly one of: `confirmed` | `estimated` | `?-unresolved`
> - `Numeric limit` is a number with a unit. For `?-unresolved`: provide platform default
>   or documented estimate, or write `unknown` with a note.
> - Structured rows only. A prose listing fails TABLE A.

PA construct type vocabulary:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE A: declare FIRST BOTTLENECK, annotate that row `<-- FIRST BOTTLENECK`.

---

### Phase 1 — TABLE B: Backpressure Propagation Trace

| Hop | From component | To component | Causal mechanism | Effect observed |
|-----|---------------|-------------|-----------------|-----------------|
> **[TABLE B PRODUCTION GATE]** You are now producing TABLE B rows. Start the first `| Hop |`
> data row immediately below this notice. Requirements active at this production point:
> - `Causal mechanism` must name the specific technical cause at each hop.
>   Acceptable: "429 returned; no Retry-After handler; immediate retry in same window;
>   connector re-throttles before window resets" or "concurrency cap reached; runtime queues
>   trigger invocations; backlog accumulates."
>   Failing tokens (each individually checked in GATE 1): "also throttled", "cascade occurs",
>   "propagates to", "downstream effect", "flow is affected", "rate limiting applies",
>   and all Category A–D tokens enumerated in GATE 1.
> - All From/To entries must appear in TABLE A. No phantom components.
> - All TABLE A path components appear as From or To. Off-path: `OUT-OF-PATH`.
> - Minimum two directed hops from FIRST BOTTLENECK.

---

### GATE 1 — PER-TOKEN BINARY ATTESTATION (BLOCKING)

Before Phase 2: individually resolve each token below. For each token write exactly one of:
- `[CLEAR]` — token or close paraphrase is absent from all TABLE B Causal mechanism cells.
- `[FAIL: hop N — rewritten below]` — token or close paraphrase is present at hop N.
  Provide the rewrite immediately after the full checklist.

**Every `- [ ]` must be individually resolved. Any unresolved `- [ ]` = GATE 1 not passed.
Phase 2 does not begin while any box remains unresolved.**

**Category A — Pure effect labels:**
- [ ] "also throttled"
- [ ] "also rate limited"
- [ ] "gets throttled"
- [ ] "is throttled"
- [ ] "rate limited"

**Category B — Causation assertions without mechanism:**
- [ ] "cascade occurs"
- [ ] "cascades to"
- [ ] "cascading throttle"
- [ ] "propagates to"
- [ ] "propagation"
- [ ] "throttle propagates"

**Category C — Vague effect descriptions:**
- [ ] "downstream effect"
- [ ] "downstream impact"
- [ ] "flow is affected"
- [ ] "becomes affected"
- [ ] "is impacted"
- [ ] "experiences throttling"

**Category D — Passive mechanism evasions:**
- [ ] "rate limiting applies"
- [ ] "throttling occurs"
- [ ] "throttling applies"
- [ ] "throttle applies"
- [ ] "is limited"
- [ ] "gets limited"
- [ ] "hits the limit"

**Rewrite format (provide immediately after the checklist for any `[FAIL]` items):**
State: (1) the signal returned at From, (2) what the action or runtime does in response,
(3) why that response causes the Effect at To. Replace the failing cell text.

---

### Phase 2 — Retry-After Handling Audit

For each TABLE B hop receiving a 429 or throttle signal, check `Retry-After` handling.
Produce `FINDING-RH-NN: [component] — [specific gap]`. If none: "No Retry-After handling gaps."

---

### Phase 3 — Unprotected Burst Path

At least one structural path where burst traffic bypasses throttle controls. Name the PA
construct and structural absence. A path throttled at a higher limit does not qualify.
If none, state conclusion and evidence.

---

### Phase 4 — User Experience by Throttle Tier

Each distinct TABLE B throttle tier: error code, wait time, visible vs. silent. At least two
tiers if multiple exist.

---

### Phase 5 — Cascading Throttle Failure Scenario

Throttling at one TABLE B tier triggers a second. Name both rows, causal link, compounded impact.

---

### Phase 6 — TABLE C: Volume-Multiplier Tier Matrix

| Multiplier | Est. req/min | First throttle tier hit | Behavior at this tier | Est. error rate | Arithmetic |
|-----------|-------------|------------------------|----------------------|----------------|------------|
> **[TABLE C PRODUCTION GATE]** You are now producing TABLE C rows. Fill the four rows
> immediately below this notice. Requirements active at this production point:
> - Exactly four rows required in this order: 1×, 3×, 5×, 10×. Do not reorder or omit.
> - `Est. error rate`: numeric value or bracketed range. Qualitative labels fail.
> - `Arithmetic`: step-by-step calculation citing TABLE A row number for each limit.
>   Example: "TABLE A row 3: connector = 600 req/min. At 5×: 1,500 req/min. Excess =
>   900. Queue cap = 300 (TABLE A row 5, estimated). Throttled fraction = 900/1,500 = 60%."
>   Stated conclusions without the chain fail.
> - Structured rows only. A prose description of load scaling fails TABLE C.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

---

### Phase 7 — TABLE D: Mitigation Prescriptions

| Finding ID | Root cause | Prescribed remediation | Specific PA config or pattern |
|-----------|-----------|----------------------|------------------------------|
> **[TABLE D PRODUCTION GATE — FINAL TABLE]** You are now producing TABLE D rows. Fill
> the rows immediately below this notice. Requirements active at this production point:
> - One row per FINDING-RH-NN from Phase 2. One row per burst path from Phase 3.
> - `Specific PA config`: exact setting, backoff formula with parameters, or queue
>   integration point. Generic guidance ("add retry logic") fails.
> - Structured rows only. A prose recommendation list fails TABLE D.
| F-01 | | | |

---

**Cross-table Consistency Check:** Before finalizing, verify:
1. Every From/To in TABLE B names a TABLE A component — flag any absent as PHANTOM-NN.
2. Every TABLE C arithmetic chain cites a TABLE A row number — flag any uncited limits as
   CITATION-GAP-NN.
3. Every TABLE D Finding ID maps to a Phase 2 FINDING-RH-NN or Phase 3 burst path —
   flag any unmapped row as ORPHAN-FINDING-NN.
4. All four tables present as structured tables with columns intact — flag any missing or
   prose-substituted table as MISSING-TABLE-NN.

---

## V-05 — Combined: Per-token Binary Attestation + Incapability Preamble + Stub-Row-Proof Gate

**Axis:** Combined (V-01 + V-02 + V-03) — all three R5 mechanisms active in a single
Role-based prompt. TABLE C and TABLE D carry enforcement notices placed between the column
header separator and the first stub row (C-24). GATE 1 uses per-token `- [ ]` binary
attestation with individual dispositions (C-22). Role 4 (Consistency Auditor) opens with a
declarative structural-fact preamble establishing incapability before the verification mandate
(C-23). This is the full R5 ceiling variation targeting all 24 criteria.

**Hypothesis:** Each R5 mechanism targets a distinct failure mode. C-24 closes the stub-row
buffering gap for TABLE C and TABLE D — the last analytical tables produced under maximum
token pressure. C-22 closes the collective-attestation loophole in GATE 1 — forcing the model
to check each of the 23 failing tokens individually and locate failure at a specific hop. C-23
closes the rationalization path in Role 4 — the fact statement establishes what did not happen
(Role 4 produced no rows) before stating what must happen (Role 4 checks cross-table
consistency). All three mechanisms are structurally complementary: C-24 fires at table
production time, C-22 fires at gate time, C-23 fires at auditor-role entry. No mechanism
redundantly covers another's failure mode.

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
> ANTI-SUBSTITUTION: structured rows only. Prose listing fails.

**TABLE 2 — Backpressure Propagation Trace** *(Role 2 owns)*
| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
> Causal mechanism: specific technical cause per hop. Effect-label text fails.
> ANTI-SUBSTITUTION: structured rows only. Prose narrative fails.
> COMPONENT CONSTRAINT: All From/To entries must appear in TABLE 1.

**TABLE 3 — Volume-Multiplier Tier Matrix** *(Role 3 owns)*
| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
> **[TABLE 3 SCHEMA GATE]** When Role 3 produces TABLE 3, fill the four rows immediately
> below this notice. Requirements at TABLE 3 production point:
> - Exactly four rows in this order: 1×, 3×, 5×, 10×.
> - `Est. error rate`: numeric or bracketed range. Qualitative labels fail.
> - `Arithmetic`: step-by-step chain from named TABLE 1 limit to error rate, citing TABLE 1
>   row numbers. Conclusions without the chain fail.
> - For `?-unresolved` TABLE 1 rows: state assumption, proceed.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**TABLE 4 — Mitigation Prescriptions** *(Role 3 owns)*
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> **[TABLE 4 SCHEMA GATE — FINAL TABLE]** When Role 3 produces TABLE 4, fill the rows
> immediately below this notice. Requirements at TABLE 4 production point:
> - One row per FINDING-RH-NN (Role 2) and one row per burst path (Role 2).
> - `Specific PA config`: exact setting, formula with parameters, or integration point.
>   Generic guidance ("add retry logic") fails.
> - Structured rows only. A prose list fails TABLE 4.
| F-01 | | | |

---

### ROLE 1 — Domain Expert

**Owns:** TABLE 1 + Bottleneck Declaration

Fill TABLE 1. PA construct type from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

Every component from entry trigger to terminal action: add a TABLE 1 row. Generic labels fail.
Status: `confirmed`, `estimated`, or `?-unresolved` — no prose alternatives. Unknown limits:
`?-unresolved` — do not omit.

After TABLE 1: declare FIRST BOTTLENECK, annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Owns:** TABLE 2 + Retry-After Findings + Unprotected Burst Path + UX analysis + Cascade

Fill TABLE 2 starting from FIRST BOTTLENECK:
- One row per directed hop (From → To).
- Causal mechanism: specific technical cause. Failing tokens listed in GATE 1.
- All TABLE 1 components on path: From or To. Off-path: `OUT-OF-PATH`.
- Only TABLE 1 components appear in TABLE 2.

---

#### GATE 1 — PER-TOKEN BINARY ATTESTATION (BLOCKING)

Before producing findings, resolve each token individually. For each token write exactly one of:
- `[CLEAR]` — token absent from all TABLE 2 Causal mechanism cells.
- `[FAIL: hop N — rewritten below]` — token present at hop N. Rewrite follows after checklist.

**Every `- [ ]` must be individually resolved. Unresolved items = GATE 1 not passed.
Findings and all subsequent Role 2 output do not begin while any box is unresolved.**

**Category A — Pure effect labels:**
- [ ] "also throttled"
- [ ] "also rate limited"
- [ ] "gets throttled"
- [ ] "is throttled"
- [ ] "rate limited"

**Category B — Causation assertions without mechanism:**
- [ ] "cascade occurs"
- [ ] "cascades to"
- [ ] "cascading throttle"
- [ ] "propagates to"
- [ ] "propagation"
- [ ] "throttle propagates"

**Category C — Vague effect descriptions:**
- [ ] "downstream effect"
- [ ] "downstream impact"
- [ ] "flow is affected"
- [ ] "becomes affected"
- [ ] "is impacted"
- [ ] "experiences throttling"

**Category D — Passive mechanism evasions:**
- [ ] "rate limiting applies"
- [ ] "throttling occurs"
- [ ] "throttling applies"
- [ ] "throttle applies"
- [ ] "is limited"
- [ ] "gets limited"
- [ ] "hits the limit"

**Rewrite format (immediately after the checklist for any `[FAIL]` items):**
State: (1) signal returned at From, (2) what the action or runtime does in response, (3) why
that response causes the Effect at To.

---

After GATE 1 passes:
1. **Retry-After audit:** Each TABLE 2 hop receiving a 429: check `Retry-After` handling.
   Produce `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap — missing concurrency cap, no retry policy,
   unbounded parallel branch. Name PA construct and structural absence.
3. **UX by throttle tier:** Each distinct tier — error code, wait time, visible vs. silent.
   At least two tiers if multiple exist.
4. **Cascading failure:** Throttling at one TABLE 2 tier triggers a second. Name both rows,
   causal link, compounded impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** TABLE 3 + TABLE 4

Fill TABLE 3. Arithmetic: step-by-step chain from named TABLE 1 row to error rate.
For `?-unresolved` rows: state assumption, proceed. Do not leave Arithmetic empty.

Fill TABLE 4. One row per FINDING-RH-NN and one row per burst path. Specific PA config:
exact setting, formula with parameters, or integration point. Generic guidance fails.

*(Reminder: TABLE 3 and TABLE 4 schema gates are declared above — fill stub rows below each gate.)*

---

### ROLE 4 — Consistency Auditor

**Structural fact (this section precedes the mandate and is not an instruction):**
Role 4 produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the
component-limit entries, the backpressure propagation hops, the volume-multiplier arithmetic,
or the mitigation prescriptions. Role 1 produced TABLE 1 and the bottleneck declaration.
Role 2 produced TABLE 2, the Retry-After findings, the burst path, the UX analysis, and the
cascade scenario. Role 3 produced TABLE 3 and TABLE 4. Role 4 arrived after all analytical
work was complete. Role 4 cannot rationalize its own prior choices because it made none.

**Verification mandate:**
Cross-table referential consistency only. Role 4 produces flags and a verdict. Role 4 does
not produce new analysis, corrected tables, or amended rows. If a deficiency is discovered,
Role 4 flags it — the flag is the output. Correction is not.

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
