# flow-throttle — Round 6 Variations (v20 Rubric)

## Context and Variation Strategy

v20 adds three new aspirational criteria (C-25, C-26, C-27) derived from R5 excellence signals.
R5-V-05 achieved 19/19 aspirational → composite = 100 under v20. All three new criteria were
already present in R5-V-05:

| ID | Criterion | How R5-V-05 satisfied it |
|----|-----------|--------------------------|
| C-25 | Auditor mandate affirmatively scoped to flags+verdict | "Role 4 produces flags and a verdict. Role 4 does not produce new analysis, corrected tables, or amended rows." — explicit prohibition in role definition |
| C-26 | Structural-fact label on incapability preamble | "Structural fact (this section precedes the mandate and is not an instruction):" — exact label form before mandate |
| C-27 | Role-scoped output suspension in correction gate | "Findings and all subsequent Role 2 output do not begin while any box is unresolved." — role-scoped, not phase-scoped |

R6 starts from a 100/100 ceiling. The design question shifts from "what mechanics close the
remaining gaps?" to "which structural arrangements are most robust across topic variations,
and can the 100/100 score be achieved through different structural forms?"

**R6 design goals:**
1. Does declarative (validity-predicate) phrasing register maintain compliance as robustly as
   imperative phrasing under token pressure? (V-01)
2. Does pre-committing Role 4's full audit contract before any analytical roles run improve
   structural separation robustness? (V-02)
3. Does explicit inertia framing — anchoring each analysis section in PA's observable default
   behavior — improve the specificity of UX and cascade sections? (V-03)
4. Do V-01 + V-02 compose cleanly (declarative register + pre-committed audit)? (V-04)
5. Do all three mechanisms compose at full ceiling with all R5 mechanics intact? (V-05)

Three single-axis variations (V-01, V-02, V-03), then two combined (V-04, V-05):

| Variation | Primary axis | Declarative register | Audit pre-declaration | Inertia framing | Predicted composite |
|-----------|-------------|---------------------|----------------------|----------------|---------------------|
| V-01 | Phrasing register — declarative validity contracts | YES | baseline | baseline | ~100/100 |
| V-02 | Role sequence — pre-committed audit contract | baseline | YES | baseline | ~100/100 |
| V-03 | Inertia framing — PA default behavior anchoring | baseline | baseline | YES | ~100/100 |
| V-04 | Combined: declarative + audit pre-declaration | YES | YES | baseline | ~100/100 |
| V-05 | Combined ceiling: all three axes + all R5 mechanics | YES | YES | YES | ~100/100 |

---

## V-01 — Phrasing Register: Declarative Validity Contract Form

**Axis:** Phrasing register — every instruction is written as a declarative validity predicate
rather than an imperative command. "Fill TABLE A. Requirements: ..." becomes "TABLE 1 is valid
when: ...". "Requirements active at this production point" becomes "Validity conditions at
production time:". GATE 1's blocking language shifts from "must resolve before Role 2 findings
proceed" to "GATE 1 is cleared when and only when every token has a recorded individual
disposition." All R5 mechanics intact: stub-row-proof gate placement, per-token binary
attestation (C-22), structural-fact preamble with label (C-23/C-26), flags-and-verdict-only
mandate (C-25), role-scoped suspension (C-27).

**Hypothesis:** Imperative prompts invite partial compliance — the model can "acknowledge" a
command without executing it, treating the acknowledgment as satisfaction. Declarative
validity predicates make the pass condition explicit as a state rather than an action: a table
either satisfies "Status is one of confirmed/estimated/?-unresolved" or it doesn't. Under token
pressure, validity-predicate form may be harder to satisfy by acknowledgment because the model
must produce output matching the predicate, not output acknowledging the instruction. The
hypothesis is that declarative register reduces acknowledgment-mode responses and improves
compliance stability across diverse topics.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### VALIDITY CONTRACTS — Four Required Tables

A valid simulation output satisfies all four table contracts below. A table contract is
satisfied when the table appears as structured rows with all declared columns intact. A prose
description, partial list, or summary paragraph does not satisfy any table contract regardless
of analytical quality.

**TABLE 1 CONTRACT — Component-Limit Inventory** *(Role 1 satisfies)*

TABLE 1 is valid when:
- Every component from entry trigger to terminal action appears as a TABLE 1 row.
- `PA construct type` is one of the six vocabulary tokens listed in Role 1 — generic labels fail.
- `Status` is exactly one of `confirmed` | `estimated` | `?-unresolved` — prose uncertainty fails.
- `Numeric limit` carries a number and a unit. For `?-unresolved` rows: documented platform
  default or `unknown` with a note.
- No component is omitted because its limit is unknown — unknowns receive `?-unresolved`.

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE 1 VALIDITY GATE]** TABLE 1 is not satisfied by prose. All validity conditions above
> are active at this production point. Start the first `| # |` row immediately below this notice.

**TABLE 2 CONTRACT — Backpressure Propagation Trace** *(Role 2 satisfies)*

TABLE 2 is valid when:
- Each row covers exactly one directed hop (From → To).
- `Causal mechanism` names the specific technical cause at this hop — effect labels fail (see GATE 1).
- Every `From` and `To` entry names a component in TABLE 1 — phantom components fail.
- All TABLE 1 components on the propagation path appear as `From` or `To`; off-path: `OUT-OF-PATH`.

| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
> **[TABLE 2 VALIDITY GATE]** TABLE 2 is not satisfied by prose. All validity conditions above
> are active at this production point. All From/To entries must appear in TABLE 1.

**TABLE 3 CONTRACT — Volume-Multiplier Tier Matrix** *(Role 3 satisfies)*

TABLE 3 is valid when:
- Exactly four rows appear in this order: 1×, 3×, 5×, 10×.
- `Est. error rate` is a numeric value or bracketed range — qualitative labels fail.
- `Arithmetic` shows step-by-step calculation from a named TABLE 1 limit to the error rate,
  citing TABLE 1 row numbers — stated conclusions without the chain fail.
- For `?-unresolved` TABLE 1 rows: a stated assumption precedes the arithmetic step.

| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
> **[TABLE 3 VALIDITY GATE]** TABLE 3 is not satisfied by prose or by fewer than four rows.
> All validity conditions above are active at this production point.
> Fill the four rows immediately below this notice.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**TABLE 4 CONTRACT — Mitigation Prescriptions** *(Role 3 satisfies)*

TABLE 4 is valid when:
- One row exists per FINDING-RH-NN produced in Role 2.
- One row exists per unprotected burst path identified in Role 2.
- `Specific PA config` names an exact setting, backoff formula with parameters, or queue
  integration point — generic guidance ("add retry logic") fails.

| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> **[TABLE 4 VALIDITY GATE — FINAL TABLE]** TABLE 4 is not satisfied by a prose list.
> All validity conditions above are active at this production point.
> Fill one row per finding and burst path immediately below this notice.
| F-01 | | | |

---

### ROLE 1 — Domain Expert

**Satisfies:** TABLE 1 + Bottleneck Declaration

TABLE 1 is satisfied by this role when all components from entry trigger to terminal action
appear as rows with PA construct type drawn from the vocabulary below:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE 1: FIRST BOTTLENECK is declared — the component whose limit is hit first at the
given request volume. That row is annotated `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Satisfies:** TABLE 2 + GATE 1 attestation + Retry-After Findings + Unprotected Burst Path +
UX analysis + Cascade scenario

TABLE 2 is satisfied by this role when filled starting from FIRST BOTTLENECK with one row per
directed hop (From → To). Causal mechanism satisfies its column contract when it names the
specific technical cause at this hop. The following tokens in any Causal mechanism cell indicate
a failing contract — each is individually checked in GATE 1:
"also throttled", "cascade occurs", "propagates to", "downstream effect", "flow is affected",
"rate limiting applies", and all Category A–D tokens enumerated in GATE 1.

---

#### GATE 1 — PER-TOKEN BINARY ATTESTATION (BLOCKING)

GATE 1 is cleared when and only when every token below has received an individual disposition.

Individual disposition form — each token receives exactly one of:
- `[CLEAR]` — token or close paraphrase is absent from all TABLE 2 Causal mechanism cells.
- `[FAIL: hop N — rewritten below]` — token or close paraphrase is present at hop N.
  Rewrite follows immediately after the full checklist.

**GATE 1 INVARIANT: Role 2 produces no findings, burst path, UX analysis, or cascade output
while any `- [ ]` item below lacks an individual disposition. Role 2 produces no further
output while any box is unresolved.**

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

**Rewrite format for `[FAIL]` items (provide immediately after the checklist):**
State: (1) signal returned at From, (2) what the action or runtime does in response, (3) why
that response causes the Effect at To.

---

After GATE 1 is cleared:
1. **Retry-After audit:** Each TABLE 2 hop receiving a 429: check `Retry-After` handling.
   Each gap produces `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap — missing concurrency cap, no retry policy,
   unbounded parallel branch. Name the PA construct and the structural absence.
3. **UX by throttle tier:** Each distinct TABLE 2 tier — error code, wait time, visible vs.
   silent. At least two tiers if multiple exist.
4. **Cascading failure:** Throttling at one TABLE 2 tier triggers a second. Name both rows,
   causal link, compounded throughput or error rate impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + all findings (Role 2).
**Satisfies:** TABLE 3 + TABLE 4

TABLE 3 is satisfied by this role when the Arithmetic column shows a step-by-step chain from
a named TABLE 1 row to the error rate. Example satisfying form: "TABLE 1 row 2: connector
limit = 600 req/min. At 5×: 1,500 req/min. Excess = 900 req/min. Queue capacity = 300
(TABLE 1 row 4, estimated). After queue saturation: 600/1,500 = 40% throttled."
A stated conclusion without the chain fails the Arithmetic contract. For `?-unresolved` TABLE 1
rows: a stated assumption precedes the step.

TABLE 4 is satisfied by this role when each FINDING-RH-NN and each burst path has a row with
a Specific PA config naming an exact setting, formula with parameters, or integration point.

*(Reminder: TABLE 3 and TABLE 4 validity gates are declared above — fill stub rows below each gate.)*

---

### ROLE 4 — Consistency Auditor

**Structural fact (this section precedes the mandate and is not an instruction):**
Role 4 produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the
component-limit entries, the propagation hops, the volume-multiplier arithmetic, or the
mitigation prescriptions. Role 1 produced TABLE 1 and the bottleneck declaration. Role 2
produced TABLE 2, the Retry-After findings, the burst path, the UX analysis, and the cascade
scenario. Role 3 produced TABLE 3 and TABLE 4. Role 4 arrived after all analytical work was
complete. Role 4 cannot rationalize its own prior choices because it made none.

**Role mandate: flags and verdict only.**
Role 4 output is valid when it consists solely of flag entries (PHANTOM-NN, CITATION-GAP-NN,
ORPHAN-FINDING-NN, MISSING-TABLE-NN format) and a verdict statement. Analysis, corrected
tables, amended rows, root-cause explanations, and fix proposals do not constitute valid
Role 4 output.

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
[List all flags: PHANTOM, CITATION-GAP, ORPHAN-FINDING, MISSING-TABLE]

---

## V-02 — Role Sequence: Pre-committed Audit Contract

**Axis:** Role sequence — Role 4's complete specification (structural-fact incapability
preamble with C-26 label, flags-and-verdict-only mandate, all four checks A–D, verdict format)
is declared as a PRE-COMMITTED AUDIT CONTRACT at the top of the prompt, before any analytical
roles begin. The analytical roles (1–3) run knowing the audit contract is already locked in.
At Role 4's execution point, it opens with the execution-time structural-fact preamble (past
tense, as in R5-V-05) and then references the pre-committed contract for its checks. All other
R5 mechanics preserved unchanged.

**Hypothesis:** In R5-V-05, Role 4's mandate and constraints appear at the end of the prompt,
after all analytical content has been produced. The model encounters the constraints only after
its "authorial" roles have run. Pre-declaring the audit contract forces the model to process
Role 4's scope restriction before it begins generating any analytical content — the constraint
is in context during Roles 1–3, not just during Role 4. This may strengthen structural
separation by anchoring Role 4's incapability as a pre-condition rather than a post-condition.
The hypothesis is that temporal pre-commitment improves the probability that the model
maintains role separation throughout, not just at the Role 4 execution point.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PRE-COMMITTED AUDIT CONTRACT

This contract governs Role 4's execution. It is declared here, before any analytical output,
and is binding on Role 4 when it runs after Role 3. No revision to this contract is permitted
during the simulation. Role 4 executes exactly the checks below — no additional analysis,
no corrected tables, no amended rows, no root-cause explanations.

**Structural fact — Constraint binding at Role 4 execution time (this section precedes the
mandate and is not an instruction):**
When Role 4 executes, it will have produced no rows in any table. The component-limit entries
are the product of Role 1. The propagation hops, findings, burst path, UX analysis, and cascade
scenario are the product of Role 2. The volume-multiplier arithmetic and mitigation prescriptions
are the product of Role 3. Role 4 enters the simulation after all analytical work is complete.
Role 4 cannot rationalize prior choices it did not make.

**Role mandate: flags and verdict only.**
Role 4 produces flag entries and a verdict. Role 4 does not produce new analysis, corrected
tables, amended rows, root-cause explanations, or fix proposals of any kind.

**Check A — Propagation Phantom Scan**
For each TABLE 1 From/To component in TABLE 2 absent from TABLE 1:
`PHANTOM-NN: "[component]" — TABLE 2 Hop [N], absent from TABLE 1`

**Check B — Arithmetic Citation Audit**
For each TABLE 3 Arithmetic limit not traceable to a specific TABLE 1 row:
`CITATION-GAP-NN: TABLE 3 [multiplier] — "[limit text]" has no TABLE 1 source row`

**Check C — Mitigation Linkage Audit**
For each TABLE 4 Finding ID with no Role 2 source:
`ORPHAN-FINDING-NN: TABLE 4 row — "[ID]" has no Role 2 source`

**Check D — Table Completeness**
For any required table absent or prose-substituted:
`MISSING-TABLE-NN: [TABLE name] — absent or substituted with prose`

**Audit Verdict:**
No flags: `AUDIT RESULT: PASS — all tables present and structurally intact; no phantom
components; no arithmetic citation gaps; no orphan findings.`
Flags present: `AUDIT RESULT: FAIL — [counts by type]. Artifact requires correction.`
[List all flags: PHANTOM, CITATION-GAP, ORPHAN-FINDING, MISSING-TABLE]

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
> - `Arithmetic`: step-by-step chain from named TABLE 1 limit to error rate, citing row numbers.
> - For `?-unresolved` TABLE 1 rows: state assumption, proceed.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**TABLE 4 — Mitigation Prescriptions** *(Role 3 owns)*
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> **[TABLE 4 SCHEMA GATE — FINAL TABLE]** When Role 3 produces TABLE 4, fill the rows
> immediately below this notice. Requirements:
> - One row per FINDING-RH-NN (Role 2) and one row per burst path (Role 2).
> - `Specific PA config`: exact setting, formula with parameters, or integration point.
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
Status: `confirmed`, `estimated`, or `?-unresolved`. Unknown limits: `?-unresolved` — do not omit.

After TABLE 1: declare FIRST BOTTLENECK, annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Owns:** TABLE 2 + GATE 1 attestation + Retry-After Findings + Unprotected Burst Path +
UX analysis + Cascade scenario

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

**Rewrite format (immediately after checklist for any `[FAIL]` items):**
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

Fill TABLE 3. Arithmetic: step-by-step chain from named TABLE 1 row to error rate, citing row
numbers. For `?-unresolved` rows: state assumption, proceed. Do not leave Arithmetic empty.

Fill TABLE 4. One row per FINDING-RH-NN and one row per burst path. Specific PA config:
exact setting, formula with parameters, or integration point. Generic guidance fails.

*(Reminder: TABLE 3 and TABLE 4 schema gates are declared above — fill stub rows below each gate.)*

---

### ROLE 4 — Consistency Auditor

**Structural fact (this section precedes the mandate and is not an instruction):**
Role 4 produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the
component-limit entries, the propagation hops, the volume-multiplier arithmetic, or the
mitigation prescriptions. Role 1 produced TABLE 1. Role 2 produced TABLE 2 and the findings.
Role 3 produced TABLE 3 and TABLE 4. Role 4 arrived after all analytical work was complete.
Role 4 cannot rationalize its own prior choices because it made none.

**Execute the Pre-committed Audit Contract declared at the top of this simulation.**
(Restate: Role mandate: flags and verdict only. Run Checks A, B, C, D. Produce verdict.)

---

## V-03 — Inertia Framing: PA Default Behavior Anchoring

**Axis:** Inertia framing — a PA Default Behaviors inventory is declared before Phase 0,
cataloging what Power Automate does out-of-box at each relevant throttle tier before any
mitigation is applied. The UX analysis (Phase 4) and cascade scenario (Phase 5) each require
explicit reference to the default behavior catalog: UX tiers must describe the default PA
response first, then the compliant response; the cascade scenario must identify which defaults
cause the cascade. All R5 mechanics preserved unchanged. This is the only single-axis change.

**Hypothesis:** Without explicit anchoring in observable defaults, UX and cascade sections
tend toward idealized descriptions of "what should happen" rather than "what PA actually does."
The status-quo competitor — PA's built-in behavior before mitigations — is the reference
point that makes findings actionable. Inertia framing forces the model to ground each UX
and cascade finding in a concrete observable default, producing more specific and verifiable
output. The hypothesis is that explicitly naming the status quo improves the analytical
specificity of sections most prone to abstract or idealized descriptions.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PA DEFAULT BEHAVIORS — Status Quo Reference

The following behaviors are PA's out-of-box defaults, active before any mitigation or
configuration change. Each analysis section that references user experience or cascades must
cite the relevant default behavior below as the baseline.

| # | Default behavior | PA construct affected | What happens by default |
|---|-----------------|----------------------|------------------------|
| D-1 | No trigger concurrency limit | Flow trigger | All trigger invocations fire in parallel with no cap; N events start N simultaneous flow runs |
| D-2 | No Retry-After honor | Flow action on 429 | PA returns HTTP 429 to the calling action; the built-in retry policy retries at a fixed 20-minute interval (4 attempts); the Retry-After header value in the 429 response is ignored |
| D-3 | Fixed-interval retry only | Flow action retry policy | Default retry: 4 attempts at fixed 20-minute intervals, not exponential; no jitter |
| D-4 | No action batching | Apply to Each / foreach | Each item in a loop generates an independent action call with no batching; N items = N calls |
| D-5 | No environment concurrency cap | Flow run concurrency | Default environment setting has no concurrent run limit; the cap must be explicitly configured |

These defaults are the inertia the simulation is designed to expose. Analysis sections must
reference this catalog — citing "D-N" — when describing what users observe or how cascades form.

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
> - `Arithmetic`: step-by-step chain from named TABLE 1 limit to error rate, citing row numbers.
> - For `?-unresolved` TABLE 1 rows: state assumption, proceed.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**TABLE 4 — Mitigation Prescriptions** *(Role 3 owns)*
| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> **[TABLE 4 SCHEMA GATE — FINAL TABLE]** When Role 3 produces TABLE 4, fill the rows
> immediately below this notice. Requirements:
> - One row per FINDING-RH-NN (Role 2) and one row per burst path (Role 2).
> - `Specific PA config`: exact setting, formula with parameters, or integration point.
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
Status: `confirmed`, `estimated`, or `?-unresolved`. Unknown limits: `?-unresolved` — do not omit.

After TABLE 1: declare FIRST BOTTLENECK, annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Owns:** TABLE 2 + GATE 1 attestation + Retry-After Findings + Unprotected Burst Path +
UX analysis + Cascade scenario

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

**Rewrite format (immediately after checklist for any `[FAIL]` items):**
State: (1) signal returned at From, (2) what the action or runtime does in response, (3) why
that response causes the Effect at To.

---

After GATE 1 passes:
1. **Retry-After audit:** Each TABLE 2 hop receiving a 429: check `Retry-After` handling.
   Produce `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap — missing concurrency cap, no retry policy,
   unbounded parallel branch. Name PA construct and structural absence.
3. **UX by throttle tier:** Each distinct TABLE 2 throttle tier — for each tier, state:
   (a) the PA default behavior from the Default Behaviors catalog (cite D-N),
   (b) what the user observes as a result of that default, and
   (c) what the user would observe if the default were correctly mitigated.
   At least two tiers if multiple exist.
4. **Cascading failure:** Throttling at one TABLE 2 tier triggers a second. Name both TABLE 2
   rows, identify which PA default behavior (D-N) causes the cascade at each tier, the causal
   link between them, and the compounded throughput or error rate impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Owns:** TABLE 3 + TABLE 4

Fill TABLE 3. Arithmetic: step-by-step chain from named TABLE 1 row to error rate, citing row
numbers. For `?-unresolved` rows: state assumption, proceed. Do not leave Arithmetic empty.

Fill TABLE 4. One row per FINDING-RH-NN and one row per burst path. Specific PA config:
exact setting, formula with parameters, or integration point. Generic guidance fails.

*(Reminder: TABLE 3 and TABLE 4 schema gates are declared above — fill stub rows below each gate.)*

---

### ROLE 4 — Consistency Auditor

**Structural fact (this section precedes the mandate and is not an instruction):**
Role 4 produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the
component-limit entries, the propagation hops, the volume-multiplier arithmetic, or the
mitigation prescriptions. Role 1 produced TABLE 1. Role 2 produced TABLE 2 and the findings.
Role 3 produced TABLE 3 and TABLE 4. Role 4 arrived after all analytical work was complete.
Role 4 cannot rationalize its own prior choices because it made none.

**Role mandate: flags and verdict only.**
Role 4 produces flags and a verdict. Role 4 does not produce new analysis, corrected tables,
amended rows, root-cause explanations, or fix proposals.

**Check A — Propagation Phantom Scan**
For each TABLE 2 From/To component absent from TABLE 1:
`PHANTOM-NN: "[component]" — TABLE 2 Hop [N], absent from TABLE 1`

**Check B — Arithmetic Citation Audit**
For each TABLE 3 Arithmetic limit not traceable to a TABLE 1 row:
`CITATION-GAP-NN: TABLE 3 [multiplier] — "[limit text]" has no TABLE 1 source row`

**Check C — Mitigation Linkage Audit**
For each TABLE 4 Finding ID with no Role 2 source:
`ORPHAN-FINDING-NN: TABLE 4 row — "[ID]" has no Role 2 source`

**Check D — Table Completeness**
For any required table absent or prose-substituted:
`MISSING-TABLE-NN: [TABLE name] — absent or substituted with prose`

**Audit Verdict:**
No flags: `AUDIT RESULT: PASS — all tables present and structurally intact; no phantom
components; no arithmetic citation gaps; no orphan findings.`
Flags present: `AUDIT RESULT: FAIL — [counts by type]. Artifact requires correction.`
[List all flags: PHANTOM, CITATION-GAP, ORPHAN-FINDING, MISSING-TABLE]

---

## V-04 — Combined: Declarative Contract + Pre-committed Audit Contract

**Axis:** Combined (V-01 + V-02) — all instruction language is written as declarative validity
predicates (V-01 phrasing register), and Role 4's full audit contract is pre-declared at the
top before any analytical roles run (V-02 role sequence). Inertia framing is left at baseline.
All R5 mechanics preserved: stub-row-proof gate placement, per-token binary attestation (C-22),
structural-fact preamble with C-26 label, C-25 mandate, C-27 role-scoped suspension.

**Hypothesis:** V-01 and V-02 target orthogonal failure modes. Declarative register (V-01)
addresses acknowledgment-mode compliance — where the model notes a constraint without producing
output satisfying it. Pre-committed audit contract (V-02) addresses late-context role scope —
where the model encounters the auditor's constraints only after it has already produced all
analytical content. Combining them tests whether the two mechanisms compose cleanly or whether
declarative phrasing of the pre-committed contract produces ambiguity (since pre-declared
future-state predicates may read differently than execution-time past-state facts). If V-04
achieves the same composite as V-01 and V-02 individually, the combination is clean. If V-04
underperforms, the declarative register and pre-commitment interact adversely.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PRE-COMMITTED AUDIT CONTRACT

This contract governs Role 4's execution. It is declared here, before any analytical output,
and is binding on Role 4 when it runs after Role 3.

**Structural fact — Constraint binding at Role 4 execution time (this section precedes the
mandate and is not an instruction):**
When Role 4 executes, it will have produced no rows in any table. The component-limit entries
are the product of Role 1. The propagation hops and findings are the product of Role 2. The
arithmetic and mitigation rows are the product of Role 3. Role 4 enters the simulation after
all analytical work is complete. Role 4 cannot rationalize prior choices it did not make.

**Role mandate: flags and verdict only.**
Role 4 output is valid when it consists solely of flag entries and a verdict. Analysis,
corrected tables, amended rows, root-cause explanations, and fix proposals are not valid
Role 4 output.

Role 4 checks (executed when Role 4 runs):
- **Check A:** Each TABLE 2 From/To absent from TABLE 1 → `PHANTOM-NN`
- **Check B:** Each TABLE 3 Arithmetic limit without a TABLE 1 source → `CITATION-GAP-NN`
- **Check C:** Each TABLE 4 Finding ID without a Role 2 source → `ORPHAN-FINDING-NN`
- **Check D:** Each required table absent or prose-substituted → `MISSING-TABLE-NN`

Verdict: No flags → `AUDIT RESULT: PASS`. Flags present → `AUDIT RESULT: FAIL — [counts].`

---

### VALIDITY CONTRACTS — Four Required Tables

A valid simulation output satisfies all four table contracts. A contract is satisfied when the
table appears as structured rows with all declared columns intact. Prose substitution fails
every contract regardless of analytical quality.

**TABLE 1 CONTRACT — Component-Limit Inventory** *(Role 1 satisfies)*

TABLE 1 is valid when:
- Every component from entry trigger to terminal action appears as a TABLE 1 row.
- `PA construct type` is one of the six vocabulary tokens listed under Role 1.
- `Status` is exactly one of `confirmed` | `estimated` | `?-unresolved`.
- `Numeric limit` carries a number and a unit; `?-unresolved` rows carry a platform default or `unknown` with a note.
- No component is omitted for having an unknown limit.

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE 1 VALIDITY GATE]** TABLE 1 is not satisfied by prose. Validity conditions above
> are active at this production point. Start the first `| # |` row immediately below this notice.

**TABLE 2 CONTRACT — Backpressure Propagation Trace** *(Role 2 satisfies)*

TABLE 2 is valid when:
- Each row covers one directed hop (From → To).
- `Causal mechanism` names the specific technical cause — effect labels (see GATE 1) fail.
- Every From/To entry names a TABLE 1 component — phantom components fail.
- All TABLE 1 path components appear as From or To; off-path components: `OUT-OF-PATH`.

| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
> **[TABLE 2 VALIDITY GATE]** TABLE 2 is not satisfied by prose. Validity conditions above
> are active at this production point. All From/To entries must appear in TABLE 1.

**TABLE 3 CONTRACT — Volume-Multiplier Tier Matrix** *(Role 3 satisfies)*

TABLE 3 is valid when:
- Exactly four rows appear: 1×, 3×, 5×, 10×.
- `Est. error rate` is a numeric value or bracketed range.
- `Arithmetic` shows step-by-step calculation from a named TABLE 1 row to error rate, citing
  TABLE 1 row numbers — conclusions without the chain fail.
- `?-unresolved` TABLE 1 rows: a stated assumption precedes the arithmetic step.

| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
> **[TABLE 3 VALIDITY GATE]** TABLE 3 is not satisfied by prose or fewer than four rows.
> Validity conditions above are active at this production point.
> Fill the four rows immediately below this notice.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**TABLE 4 CONTRACT — Mitigation Prescriptions** *(Role 3 satisfies)*

TABLE 4 is valid when:
- One row per FINDING-RH-NN from Role 2; one row per burst path from Role 2.
- `Specific PA config` names an exact setting, formula with parameters, or integration point.

| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> **[TABLE 4 VALIDITY GATE — FINAL TABLE]** TABLE 4 is not satisfied by a prose list.
> Validity conditions above are active at this production point.
> Fill one row per finding and burst path immediately below this notice.
| F-01 | | | |

---

### ROLE 1 — Domain Expert

**Satisfies:** TABLE 1 + Bottleneck Declaration

Fill TABLE 1 per the TABLE 1 CONTRACT. PA construct type from the Power Platform taxonomy:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE 1: declare FIRST BOTTLENECK, annotate that row `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Satisfies:** TABLE 2 + GATE 1 attestation + Retry-After Findings + Unprotected Burst Path +
UX analysis + Cascade scenario

TABLE 2 is satisfied by this role starting from FIRST BOTTLENECK with one row per directed hop.
A Causal mechanism cell satisfies its contract when it names the specific technical cause.
The following tokens in any Causal mechanism cell indicate a failing contract:
"also throttled", "cascade occurs", "propagates to", "downstream effect", "flow is affected",
"rate limiting applies", and all Category A–D tokens in GATE 1.

---

#### GATE 1 — PER-TOKEN BINARY ATTESTATION (BLOCKING)

GATE 1 is cleared when and only when every token below has received an individual disposition.

Individual disposition form:
- `[CLEAR]` — token absent from all TABLE 2 Causal mechanism cells.
- `[FAIL: hop N — rewritten below]` — token present at hop N; rewrite follows after checklist.

**GATE 1 INVARIANT: Role 2 produces no findings, burst path, UX analysis, or cascade output
while any `- [ ]` item below lacks an individual disposition. Role 2 produces no further
output while any box is unresolved.**

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

**Rewrite format for `[FAIL]` items (immediately after checklist):**
State: (1) signal returned at From, (2) action or runtime response, (3) why that response
causes the Effect at To.

---

After GATE 1 is cleared:
1. **Retry-After audit:** `FINDING-RH-NN: [component] — [specific gap]` per 429 hop.
2. **Unprotected burst path:** One structural gap — name PA construct and structural absence.
3. **UX by throttle tier:** Each distinct tier — error code, wait time, visible vs. silent.
   At least two tiers if multiple exist.
4. **Cascading failure:** One tier triggers a second. Name both rows, causal link, compounded impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Satisfies:** TABLE 3 + TABLE 4

TABLE 3 is satisfied when Arithmetic shows step-by-step chain from a named TABLE 1 row to
error rate with TABLE 1 row numbers cited. Conclusions without the chain fail.

TABLE 4 is satisfied when Specific PA config names exact settings or formulas. Generic fails.

*(Reminder: TABLE 3 and TABLE 4 validity gates are declared above — fill stub rows below each gate.)*

---

### ROLE 4 — Consistency Auditor

**Structural fact (this section precedes the mandate and is not an instruction):**
Role 4 produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the
component-limit entries, the propagation hops, the arithmetic, or the mitigations. Role 1
produced TABLE 1. Role 2 produced TABLE 2 and the findings. Role 3 produced TABLE 3 and
TABLE 4. Role 4 arrived after all analytical work was complete. Role 4 cannot rationalize its
own prior choices because it made none.

**Execute the Pre-committed Audit Contract declared at the top of this simulation.**
(Role mandate: flags and verdict only. Run Checks A, B, C, D. Produce verdict.)

---

## V-05 — Combined Ceiling: All Three Axes + All R5 Mechanics

**Axis:** Combined (V-01 + V-02 + V-03) — declarative validity-contract phrasing register,
pre-committed audit contract before analytical roles, and explicit PA default behavior
anchoring for UX and cascade sections. All R5 mechanics intact: stub-row-proof gate placement
between schema separator and first stub row (C-24), per-token binary attestation with
individual `[CLEAR]`/`[FAIL]` dispositions (C-22), structural-fact preamble with explicit
C-26 label (C-23/C-26), flags-and-verdict-only role mandate (C-25), role-scoped output
suspension in GATE 1 (C-27).

**Hypothesis:** The three R6 mechanisms target orthogonal properties. Declarative register
(V-01) addresses acknowledgment-mode compliance at production time. Pre-committed audit
contract (V-02) addresses late-context role scope — auditor constraints now appear before
any analytical content is produced. Inertia framing (V-03) addresses analytical abstraction
in UX and cascade sections by forcing reference to named PA defaults. None of the three
mechanisms overlaps with an R5 mechanism or with each other. V-05 tests whether all six
mechanisms (three R5, three R6) compose stably in a single prompt and whether the combination
produces the most robust 100/100 output across diverse topic inputs.

---

You are running a four-role Power Automate throttle simulation for `{{topic}}`.
Roles execute in sequence. Each role receives prior roles' structured output verbatim.
No role abbreviates or paraphrases a prior role's tables.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`
**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

### PA DEFAULT BEHAVIORS — Status Quo Reference

The following are PA's out-of-box defaults before any mitigation. UX and cascade analysis
sections must cite relevant defaults by D-N reference.

| # | Default behavior | PA construct affected | Observable default |
|---|-----------------|----------------------|--------------------|
| D-1 | No trigger concurrency limit | Flow trigger | N simultaneous events start N simultaneous flow runs with no cap |
| D-2 | No Retry-After honor | Flow action on 429 | 429 Retry-After header is ignored; built-in retry fires at fixed 20-min interval |
| D-3 | Fixed-interval retry only | Action retry policy | 4 retries at fixed 20-minute intervals; no exponential backoff; no jitter |
| D-4 | No action batching | Apply to Each | Each loop item generates an independent action call; N items = N calls |
| D-5 | No environment concurrency cap | Flow run concurrency | No concurrent run limit by default; cap must be explicitly configured |

---

### PRE-COMMITTED AUDIT CONTRACT

This contract governs Role 4's execution. Declared before any analytical output. Binding on
Role 4 when it runs after Role 3. No revision permitted during the simulation.

**Structural fact — Constraint binding at Role 4 execution time (this section precedes the
mandate and is not an instruction):**
When Role 4 executes, it will have produced no rows in any table. Component-limit entries:
product of Role 1. Propagation hops and findings: product of Role 2. Volume-multiplier
arithmetic and mitigations: product of Role 3. Role 4 enters after all analytical work is
complete. Role 4 cannot rationalize prior choices it did not make.

**Role mandate: flags and verdict only.**
Role 4 output is valid when it consists solely of flag entries and a verdict. Analysis,
corrected tables, amended rows, root-cause explanations, and fix proposals are not valid
Role 4 output.

Checks (executed at Role 4 runtime):
- **A:** Each TABLE 2 From/To absent from TABLE 1 → `PHANTOM-NN`
- **B:** Each TABLE 3 Arithmetic limit without TABLE 1 source → `CITATION-GAP-NN`
- **C:** Each TABLE 4 Finding ID without Role 2 source → `ORPHAN-FINDING-NN`
- **D:** Each required table absent or prose-substituted → `MISSING-TABLE-NN`

Verdict: No flags → `AUDIT RESULT: PASS`. Flags → `AUDIT RESULT: FAIL — [counts].`

---

### VALIDITY CONTRACTS — Four Required Tables

A valid simulation output satisfies all four table contracts. Prose substitution fails every
contract regardless of analytical quality.

**TABLE 1 CONTRACT — Component-Limit Inventory** *(Role 1 satisfies)*

TABLE 1 is valid when:
- Every component from entry trigger to terminal action appears as a TABLE 1 row.
- `PA construct type` is one of the six vocabulary tokens listed under Role 1.
- `Status` is exactly one of `confirmed` | `estimated` | `?-unresolved`.
- `Numeric limit` carries a number and a unit; `?-unresolved` rows carry platform default or
  `unknown` with a note. No component omitted for having an unknown limit.

| # | Component | PA construct type | Numeric limit | Unit | Status |
|---|-----------|------------------|---------------|------|--------|
> **[TABLE 1 VALIDITY GATE]** TABLE 1 is not satisfied by prose. Validity conditions above
> are active at this production point. Start the first `| # |` row immediately below this notice.

**TABLE 2 CONTRACT — Backpressure Propagation Trace** *(Role 2 satisfies)*

TABLE 2 is valid when:
- Each row covers one directed hop (From → To).
- `Causal mechanism` names the specific technical cause — effect labels (see GATE 1) fail.
- Every From/To names a TABLE 1 component — phantom components fail.
- All TABLE 1 path components appear as From or To; off-path: `OUT-OF-PATH`.

| Hop | From | To | Causal mechanism | Effect |
|-----|------|----|-----------------|--------|
> **[TABLE 2 VALIDITY GATE]** TABLE 2 is not satisfied by prose. Validity conditions above
> are active at this production point. All From/To entries must appear in TABLE 1.

**TABLE 3 CONTRACT — Volume-Multiplier Tier Matrix** *(Role 3 satisfies)*

TABLE 3 is valid when:
- Exactly four rows: 1×, 3×, 5×, 10×.
- `Est. error rate` is numeric or bracketed range.
- `Arithmetic` shows step-by-step chain from named TABLE 1 limit to error rate, with TABLE 1
  row numbers cited — conclusions without the chain fail.
- `?-unresolved` TABLE 1 rows: stated assumption precedes each arithmetic step.

| Multiplier | Est. req/min | First tier hit | Behavior | Est. error rate | Arithmetic |
|-----------|-------------|---------------|----------|----------------|------------|
> **[TABLE 3 VALIDITY GATE]** TABLE 3 is not satisfied by prose or fewer than four rows.
> Validity conditions above are active at this production point.
> Fill the four rows immediately below this notice.
| 1× (baseline) | | | | | |
| 3× | | | | | |
| 5× | | | | | |
| 10× | | | | | |

**TABLE 4 CONTRACT — Mitigation Prescriptions** *(Role 3 satisfies)*

TABLE 4 is valid when:
- One row per FINDING-RH-NN from Role 2; one row per burst path from Role 2.
- `Specific PA config` names an exact setting, formula with parameters, or integration point.
  Generic guidance fails.

| Finding ID | Root cause | Prescribed remediation | Specific PA config |
|-----------|-----------|----------------------|-------------------|
> **[TABLE 4 VALIDITY GATE — FINAL TABLE]** TABLE 4 is not satisfied by a prose list.
> Validity conditions above are active at this production point.
> Fill one row per finding and burst path immediately below this notice.
| F-01 | | | |

---

### ROLE 1 — Domain Expert

**Satisfies:** TABLE 1 + Bottleneck Declaration

TABLE 1 is satisfied by this role when all components from entry trigger to terminal action
appear as rows with PA construct type from:
- Power Platform request entitlement
- Connector throttling policy (standard tier / premium tier)
- Flow run concurrency limit (per environment)
- Action call limit (per 24-hour window)
- Microsoft 365 service protection limit
- Trigger polling frequency cap

After TABLE 1: FIRST BOTTLENECK declared, that row annotated `<-- FIRST BOTTLENECK`.

---

### ROLE 2 — Trace Analyst

**Receives:** TABLE 1 + FIRST BOTTLENECK from Role 1.
**Satisfies:** TABLE 2 + GATE 1 attestation + Retry-After Findings + Unprotected Burst Path +
UX analysis + Cascade scenario

TABLE 2 is satisfied starting from FIRST BOTTLENECK with one row per directed hop. A Causal
mechanism cell satisfies its contract when it names the specific technical cause. Tokens that
indicate a failing mechanism contract are enumerated in GATE 1 below.

---

#### GATE 1 — PER-TOKEN BINARY ATTESTATION (BLOCKING)

GATE 1 is cleared when and only when every token below has received an individual disposition.

Individual disposition form:
- `[CLEAR]` — token absent from all TABLE 2 Causal mechanism cells.
- `[FAIL: hop N — rewritten below]` — token present at hop N; rewrite follows after checklist.

**GATE 1 INVARIANT: Role 2 produces no findings, burst path, UX analysis, or cascade output
while any `- [ ]` item below lacks an individual disposition. Role 2 produces no further
output while any box is unresolved.**

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

**Rewrite format for `[FAIL]` items (immediately after checklist):**
State: (1) signal returned at From, (2) action or runtime response, (3) why that response
causes the Effect at To.

---

After GATE 1 is cleared:
1. **Retry-After audit:** Each TABLE 2 hop receiving a 429: check `Retry-After` handling.
   Produce `FINDING-RH-NN: [component] — [specific gap]`.
2. **Unprotected burst path:** One structural gap — name PA construct and structural absence.
3. **UX by throttle tier:** Each distinct TABLE 2 throttle tier — for each tier, state:
   (a) the PA default behavior from the Default Behaviors catalog (cite D-N),
   (b) what the user observes as a result of that default, and
   (c) what the user would observe if the gap were correctly mitigated.
   At least two tiers if multiple exist.
4. **Cascading failure:** Throttling at one TABLE 2 tier triggers a second. For each tier
   involved, cite the PA default behavior (D-N) that permits the cascade. Name both TABLE 2
   rows, the causal link, and the compounded throughput or error rate impact.

---

### ROLE 3 — Quantitative Reviewer

**Receives:** TABLE 1 (Role 1) + TABLE 2 + findings (Role 2).
**Satisfies:** TABLE 3 + TABLE 4

TABLE 3 is satisfied when Arithmetic shows step-by-step chain from a named TABLE 1 row to
error rate, citing TABLE 1 row numbers. A conclusion without the chain fails. For
`?-unresolved` TABLE 1 rows: stated assumption precedes the step.

TABLE 4 is satisfied when each FINDING-RH-NN and each burst path has a row with Specific PA
config naming an exact setting, formula, or integration point. Generic guidance fails.

*(Reminder: TABLE 3 and TABLE 4 validity gates declared above — fill stub rows below each gate.)*

---

### ROLE 4 — Consistency Auditor

**Structural fact (this section precedes the mandate and is not an instruction):**
Role 4 produced no rows in TABLE 1, TABLE 2, TABLE 3, or TABLE 4. It did not produce the
component-limit entries, the propagation hops, the volume-multiplier arithmetic, or the
mitigation prescriptions. Role 1 produced TABLE 1 and the bottleneck declaration. Role 2
produced TABLE 2, the Retry-After findings, the burst path, the UX analysis, and the cascade
scenario. Role 3 produced TABLE 3 and TABLE 4. Role 4 arrived after all analytical work was
complete. Role 4 cannot rationalize its own prior choices because it made none.

**Execute the Pre-committed Audit Contract declared above.**
(Role mandate: flags and verdict only. Run Checks A, B, C, D. Produce verdict. No analysis,
no corrections, no explanations.)
