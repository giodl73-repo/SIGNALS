# flow-throttle Variate -- Round 2
**Date:** 2026-03-15
**Rubric:** v2 (C-01 through C-12, essential/recommended/aspirational)
**New criteria this round targets:** C-11 (threshold sourcing provenance), C-12 (coverage self-verification)
**Baseline ceiling:** Round 1 best (R1 V-05 predicted 87/100 under v1 rubric; under v2 rubric both C-11 and C-12 were unaddressed)

---

## Round 2 Variation Map

| Variation | Axis | Hypothesis | Predicted composite (v2, max 110) |
|-----------|------|------------|-----------------------------------|
| V-01 | Output format -- Source citation column in TABLE A | A `Source` column adjacent to `Limit` forces doc attribution at the moment a number is written; C-11 becomes a form constraint, not a retrospective requirement | ~88/110 |
| V-02 | Output format -- Mandatory terminal self-verification section | A named self-check section with a pre-printed criterion checklist forces C-12 structurally; the model cannot close without mapping its content against every criterion | ~85/110 |
| V-03 | Role sequence -- Source-register phase before tier inventory | Requiring the model to commit to documentation sources before writing any number creates a traceable register; TABLE A numbers must match a named source or be flagged as undocumented | ~87/110 |
| V-04 | Combined: Source citation column (V-01) + terminal self-check (V-02) | C-11 and C-12 are enforced at different structural positions (mid-output TABLE A vs. terminal section), so they cannot crowd each other; both new criteria are targeted simultaneously without restructuring proven table patterns | ~93/110 |
| V-05 | Combined: Source register phase + inertia framing + burst/uniform columns + mitigation prescriptions + self-check | Full integration of both new criteria with the highest-performing R1/R2 proven patterns; addresses all twelve criteria with structural or motivational enforcement | ~100/110 |

**Primary questions this round asks:**

Q1: Does a `Source` column in TABLE A (V-01) produce genuine doc attribution -- named pages or
URL slugs -- or does the model fill it with generic terms ("PA docs", "connector reference")
that satisfy the column but fail C-11's pass condition (named source)?

Q2: Does a pre-printed criterion checklist in the terminal self-check (V-02) cause the model to
self-report gaps honestly, or does it backfill missing content to avoid marking checkboxes FAIL?

Q3: Does committing to sources before writing numbers (V-03 source-register phase) reduce the
incidence of invented thresholds relative to V-01's adjacent-column mechanism?

Q4: Does combining V-01 + V-02 (V-04) produce both C-11 and C-12 passes without compressing
C-03/C-08 -- the criteria the columns are meant to carry -- or does the wider TABLE A cause
the `Limit` column to abbreviate?

Q5: Does V-05's full integration (source register + inertia + burst/uniform + mitigation +
self-check) produce the highest composite, or does the constraint density cause the model to
abbreviate the cascade scenario or mitigation prescriptions?

---

## V-01 -- Output Format: Source Citation Column in TABLE A

**Axis:** Output format -- TABLE A has a `Source` column immediately after `Limit`. The column
requires a named documentation source for every numeric limit (e.g., "Power Automate limits
reference -- 'Per-connection limits' section", "SharePoint connector reference -- 'Throttling'
table"). If no documentation exists for a tier, the `Source` cell must state `not documented`
and the `Limit` cell must state `unknown [undocumented]` rather than assert a number.

**Hypothesis:** C-11 fails when numbers are present but unattributed because no prompt mechanism
forces the model to record where a number came from. A `Source` column adjacent to `Limit` makes
attribution a form-fill constraint at the moment the number is written -- the model cannot write
"600 req/min" without also writing the document that contains that figure. The adjacent-cell
constraint is stronger than a prose instruction to "cite sources" because elision requires
actively leaving a cell blank rather than simply not adding a sentence. Risk: the model may fill
`Source` with generic terms ("Power Automate documentation") that do not name a specific page
or section and therefore fail C-11's pass condition.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Produce the four tables below. Do not substitute prose for any table. Every cell must be
filled; write `unknown [reason]` only if the value is genuinely unconfirmable.

---

**TABLE A -- THROTTLE TIER INVENTORY**

*(Complete before TABLE B, TABLE C, or TABLE D.)*

| Tier-ID | Component | Limit (number + unit) | Source | Scope | UNIFORM | BURST | Binding? | Notes |
|---------|-----------|----------------------|--------|-------|---------|-------|----------|-------|
| T-01    |           |                      |        |       |         |       |          |       |
| T-02    |           |                      |        |       |         |       |          |       |
| ...     |           |                      |        |       |         |       |          |       |

Column definitions:
- `Tier-ID` -- T-01, T-02, ... Permanent for this analysis. Every downstream table and section
  that references a throttle tier must use these identifiers verbatim.
- `Limit` -- a number with a unit (e.g., 600 req/min, 10 concurrent connections). Entries without
  a number are invalid. If the limit cannot be confirmed from documentation, write
  `unknown [undocumented]` and leave `Source` as `not documented`.
- `Source` -- the named documentation source for the numeric limit in the `Limit` cell. Examples
  of passing entries: "Power Automate limits reference doc -- 'Request limits and allocations'
  table", "SharePoint connector throttling reference -- 'API call limits' row",
  "Microsoft 365 service description -- 'Exchange Online limits' section". Examples of failing
  entries: "Power Automate documentation", "connector reference", "Microsoft docs" (too generic
  to be verifiable). If no documentation exists: write `not documented` -- do not invent a number.
- `UNIFORM` -- throttle status when the given volume arrives evenly across the measurement window:
  OK (under limit), HIT (throttling begins), SAT (limit fully consumed). Assume arrival rate stays
  within 10% of the average throughout the window.
- `BURST` -- throttle status when the same total volume arrives in the first 20% of the window.
  At least one tier must have a different BURST than UNIFORM status. If no tier differs, the Notes
  column must explain the specific mechanism (window type, token bucket size, burst headroom).
- `Binding?` -- Y if this tier is the first-hit tier at the given volume under uniform arrival.
  At most one Y.

These Tier-IDs are permanent. Every row in TABLE B, TABLE C, and TABLE D that references a
throttle tier must use these identifiers verbatim.

---

**TABLE B -- BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use the binding constraint from TABLE A as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`From` must use a Tier-ID from TABLE A. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade. Generic entries ("affected", "impacted")
do not satisfy this column.

---

**TABLE C -- USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                   |                                      |                               |
| T-02    |                     |                           |                   |                                      |                               |
| ...     |                     |                           |                   |                                      |                               |

---

**TABLE D -- UNPROTECTED BURST PATHS**

*(Minimum one row. If no unprotected path exists, row 1 states that conclusion with at least
two named controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (specific structural explanation) | Tier-IDs bypassed | Consequence at burst volume |
|---------|----------------|---------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                             |                   |                             |

`Gap reason` must state the specific structural reason: missing connector policy, trigger type
exempt from queuing, endpoint that bypasses the gateway layer, no concurrency cap on this path.
"Not protected" without a structural explanation fails this cell.

---

After the four tables, produce three sections:

**BOTTLENECK AND CAUSAL REASON** -- state the TABLE A binding constraint Tier-ID, the numeric
limit exceeded at the given volume, the source document for that limit, and the causal reason
this tier binds before all others.

**RISK RANKING AND CASCADE SCENARIO** -- rank all TABLE A tiers by business risk, highest to
lowest. For the top-ranked tier: blast radius, failure visibility, recovery time. Then trace
one concrete cascade starting from the binding constraint. Use Tier-IDs. Minimum three tiers.

**MITIGATION PRESCRIPTIONS** -- for the two highest-priority gaps from TABLE A and TABLE D:
name the specific component, the setting name or API parameter, the target value, and the
expected observable outcome. Generic advice fails; name the specific change.

---

## V-02 -- Output Format: Mandatory Terminal Self-Verification Section

**Axis:** Output format -- the final section is a mandatory coverage self-check. Before the
output closes, the model must map its own content against each analysis criterion and mark each
as COVERED (with a one-phrase pointer to where it appears), PARTIAL (covered but incomplete --
describe the gap), or NOT COVERED (explain why and whether the signal was insufficient). Any
criterion the self-check cannot confirm as COVERED is surfaced as an explicit gap rather than
silently omitted.

**Hypothesis:** C-12 fails when outputs are assessed externally for missing criteria because the
model has no closing obligation to check its own coverage. A pre-printed criterion checklist in
the terminal section -- with COVERED/PARTIAL/NOT COVERED as the only valid cell values -- forces
the model to complete the check before the output is done. The self-check is also a C-11 proxy:
a model that writes "C-08: COVERED -- T-01 limit 600 req/min (source: Power Automate limits
reference)" is simultaneously producing C-11 attribution in its self-check. Risk: the model may
backfill missing content to avoid marking criteria PARTIAL or NOT COVERED, rather than reporting
gaps honestly. The scoring benefit of honest reporting (C-12 partial credit for acknowledged gaps)
must be made explicit in the instructions to counteract this risk.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Produce the output below in order. Complete each section before starting the next. Do not
substitute prose for any table. Every cell must be filled.

---

**THROTTLE TIER INVENTORY**

Enumerate every throttle tier. Assign a Tier-ID (T-01, T-02, ...). For each tier state:
component name, rate limit value (number + unit), scope (per-user / per-connection / per-tenant /
global), and whether this tier is the first-hit binding constraint at the given volume (Y/N).
Entries without a numeric limit are invalid; if the limit is undocumentable, write
`unknown [reason]` where reason is one of: undocumented, environment-specific,
requires-runtime-measurement, signal-insufficient.

These Tier-IDs are permanent. All subsequent sections use them verbatim.

---

**BACKPRESSURE PROPAGATION TRACE**

Starting from the binding constraint, trace how throttling propagates outward. Minimum two hops.
For each hop: Tier-ID (or component if not a named tier), propagation mechanism (queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade), observable effect.
Generic entries ("affected") do not satisfy the Mechanism field.

---

**USER EXPERIENCE CATALOG**

For every tier in the inventory, state: the error code or platform signal the user sees, whether
a Retry-After header is present (Y/N) and what it contains, whether the failure appears in flow
run history or is silently retried, and what happens if the caller ignores Retry-After and retries
immediately. No tier may be omitted. For the binding constraint: explicitly state whether the
current Retry-After handling is correct and what the failure mode is if not.

---

**UNPROTECTED BURST PATHS**

Identify at least one path where burst traffic enters without encountering a rate limit. For each
path: entry component, route, specific gap reason, tiers bypassed, consequence at burst volume.
If no unprotected path exists, name at least two controls that collectively cover every entry
point and explain how they do so.

---

**RISK RANKING AND CASCADE SCENARIO**

Rank all tiers by business risk (highest to lowest). For the top-ranked tier: blast radius,
failure visibility (silent vs. explicit, with a time estimate), recovery time. One sentence per
remaining tier. Then trace one cascade starting from the binding constraint: name each Tier-ID,
the causal link at each step, and the compounded effect. Minimum three tiers.

---

**MITIGATION PRESCRIPTIONS**

For at least two gaps found in this analysis: name the gap (Tier-ID and failure mode), the
specific component to modify, the exact setting name or API parameter and target value, and the
expected observable outcome. Generic advice ("add retry handling") fails. Name the specific
change ("configure the Power Automate flow's retry policy to exponential backoff starting at
30 seconds, reading the `Retry-After` header value as the base delay when present").

---

**COVERAGE SELF-VERIFICATION**

Before closing, complete the table below. Mark each criterion as COVERED, PARTIAL, or NOT COVERED.

- COVERED: the criterion is satisfied in this output -- add a one-phrase pointer (e.g., "Tier
  Inventory -- T-01 at 600 req/min from PA limits reference doc").
- PARTIAL: the criterion is addressed but incompletely -- describe what is missing.
- NOT COVERED: the criterion was not addressed -- state whether the signal was insufficient or
  the criterion is not applicable to this scenario.

Honest reporting earns credit. An output that marks a criterion NOT COVERED and explains why
is strictly better than an output that silently omits it.

| Criterion | Status | Notes |
|-----------|--------|-------|
| C-01: Primary bottleneck identified with causal reason | | |
| C-02: Backpressure propagation traced (min two hops) | | |
| C-03: At least two throttle tiers with enforcing component | | |
| C-04: UX described for every named tier | | |
| C-05: At least one unprotected burst path (or named controls as evidence) | | |
| C-06: Retry-After handling assessed for at least one caller | | |
| C-07: Cascade scenario with two or more downstream tiers | | |
| C-08: At least one numeric threshold cited | | |
| C-09: At least two mitigations with specific changes and expected outcomes | | |
| C-10: Load-shape sensitivity shown (burst vs. uniform produces different outcome) | | |
| C-11: Every numeric threshold attributed to a named source document | | |
| C-12: This self-check section appears and names all criteria | |  (auto-satisfied if this table is complete) |

---

## V-03 -- Role Sequence: Source-Register Phase Before Tier Inventory

**Axis:** Role sequence -- before any tier inventory or analysis, the model must execute a source
registration phase: enumerate every documentation source it will draw numeric limits from, with
the specific section or table name, and state what tier limits that source covers. The source
register is permanent for the analysis. When TABLE A is completed, every `Limit` entry must match
a source in the register, or the cell is flagged `unknown [undocumented]`. A number that does not
match any registered source is an invented value and must be withdrawn.

**Hypothesis:** Prompt-level source citation instructions ("cite your sources") fail because the
model writes numbers first and retrospectively assigns attribution that may not match any real
document. A source-register phase inverts the order: sources are committed before numbers. When
TABLE A is written, the model can only write a number it registered a source for -- otherwise the
mismatch is visible. This is a different enforcement mechanism than V-01's adjacent-column
approach: V-01 catches attribution gaps per-cell at writing time; V-03 catches invented numbers
at consistency-check time by comparing TABLE A against the register. Risk: the model may produce
a sparse source register (listing only one or two documents) and then still invent numbers for
tiers not covered, because the phase constraint only requires the register to exist, not to be
exhaustive.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Execute phases in order. The source register produced in Phase 0 is authoritative for the entire
analysis. A numeric limit in any subsequent phase must be traceable to a Phase 0 source entry.

---

**PHASE 0 -- SOURCE REGISTRATION**

Before writing any tier inventory or analysis, enumerate every documentation source you will
draw numeric rate limits from. For each source, state:

- Source name (the specific document or reference page -- not "Microsoft docs" but e.g.,
  "Power Automate limits and configuration reference", "SharePoint connector throttling guide",
  "Microsoft 365 service description -- Exchange Online section")
- Specific section or table within that document (e.g., "'Per-connection request limits' table",
  "'API call throttling' section", "'Throughput limits' row")
- Tiers covered (which throttle tiers in this system this source documents)

Format as a numbered list. Each entry must name a specific document section. Generic source
names fail this phase.

**UNDOCUMENTED TIERS:** If a tier in this system has no documentation source available, name
the tier and state `undocumented` -- the subsequent tier inventory must write `unknown
[undocumented]` for that tier's limit and must not assert a number.

State "Phase 0 complete -- [N] sources registered" before opening Phase 1.

---

**PHASE 1 -- THROTTLE TIER INVENTORY**

*Opens after Phase 0.*

Enumerate every throttle tier. Assign a Tier-ID (T-01, T-02, ...). For each tier state:

- Component name
- Rate limit value (a number with a unit) -- must be traceable to a Phase 0 source entry by
  citing the source number (e.g., "[Source 2]"). If the tier was registered as undocumented in
  Phase 0, write `unknown [undocumented]`.
- Scope (per-user, per-connection, per-tenant, global)
- UNIFORM status (OK / HIT / SAT -- given the stated volume arriving evenly)
- BURST status (OK / HIT / SAT -- same volume in first 20% of window)
- Binding? (Y for the first-hit tier at the given volume under uniform arrival; at most one Y)

A number that does not correspond to any Phase 0 source entry is an invented value. Replace it
with `unknown [undocumented]`.

These Tier-IDs are permanent. All subsequent phases use them verbatim.

State "Phase 1 complete" before opening Phase 2.

---

**PHASE 2 -- BACKPRESSURE AND BURST PATHS**

*Opens after Phase 1.*

Part A -- Backpressure: from the Phase 1 binding constraint, trace propagation outward. Each hop:
Tier-ID or component, mechanism (queue-fill / connection-hold / retry-amplification /
dependency-stall / timeout-cascade), observable effect. Minimum two hops.

Part B -- Burst path scan: identify any path where burst traffic enters without a rate limit.
Entry component, route, specific gap reason. If no unprotected path exists, name two controls
by name as evidence.

State "Phase 2 complete" before opening Phase 3.

---

**PHASE 3 -- USER EXPERIENCE AND RETRY-AFTER ASSESSMENT**

*Opens after Phase 2.*

For every Phase 1 tier: error code or platform signal, Retry-After present (Y/N) with value,
visible in run history (Y/N/SILENT), failure if Retry-After ignored. No tier omitted. For the
binding constraint: explicit verdict on whether Retry-After handling is correct.

State "Phase 3 complete" before opening Phase 4.

---

**PHASE 4 -- RISK RANKING, CASCADE, AND MITIGATIONS**

*Opens after Phase 3.*

**RISK RANKING** -- rank all Phase 1 tiers by business risk. Top-ranked tier: blast radius,
failure visibility, recovery time. One sentence per remaining tier.

**CASCADE SCENARIO** -- one concrete cascade from the binding constraint. Minimum three tiers.
Use Phase 1 Tier-IDs. Name the causal link at each step.

**MITIGATION PRESCRIPTIONS** -- for two gaps from this analysis: Tier-ID and failure mode, specific
component to modify, exact setting/parameter and target value, expected observable outcome.
Generic advice fails. Cite Phase 0 source numbers when stating that a recommended value aligns
with documented limits.

State "Phase 4 complete" before the completion check.

---

**COMPLETION CHECK**

```
Phase 0: Sources registered: [N] | Undocumented tiers declared: [list or none]
Phase 1: Tiers enumerated: [N] | Limits with traced source: [N] | Limits marked undocumented: [N]
Phase 2A: Backpressure hops traced: [N] | Mechanisms named: [list]
Phase 2B: Burst paths found: [N] | Or controls named as evidence: [list]
Phase 3: Tiers in UX catalog: [N] | Retry-After verdict for binding constraint: [pass/fail/partial]
Phase 4: Tiers ranked: [N] | Cascade tiers named: [list] | Prescriptions: [N]
```

If any phase entry shows a gap, state whether the gap was caused by signal insufficiency or
missing analysis.

---

## V-04 -- Combined: Source Citation Column (V-01) + Terminal Self-Verification (V-02)

**Axis:** Combined -- TABLE A has a `Source` column enforcing C-11 at the moment each number is
written (from V-01). The output closes with a mandatory coverage self-check table enforcing C-12
at the terminal position (from V-02). The two mechanisms operate at different structural positions
and address different criteria, so they cannot crowd each other. All proven table patterns from
Round 1 are preserved.

**Hypothesis:** V-01 addresses C-11 (numbers have sources) and V-02 addresses C-12 (output
self-reports its coverage). Neither mechanism addresses the criterion the other targets. Combining
them in a single prompt adds both new aspirational criteria without modifying the structure that
produces C-01 through C-10. The `Source` column in TABLE A is a net addition of one column with
no effect on other columns. The terminal self-check is a net addition of one section after all
content is written, with no effect on earlier sections. The combination targets twelve criteria
with structural enforcement for all twelve. Risk: the wider TABLE A (nine columns) may cause the
model to abbreviate the `Limit` or `Source` columns; the column definitions must make the minimum
acceptable value concrete enough to resist abbreviation.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Produce the four tables below, then produce the sections, then complete the self-verification.
Do not substitute prose for any table. Every cell must be filled; write `unknown [reason]` only
if a value is genuinely unconfirmable.

---

**TABLE A -- THROTTLE TIER INVENTORY**

*(Complete before TABLE B, TABLE C, or TABLE D.)*

| Tier-ID | Component | Limit (number + unit) | Source | Scope | UNIFORM | BURST | Binding? | Notes |
|---------|-----------|----------------------|--------|-------|---------|-------|----------|-------|
| T-01    |           |                      |        |       |         |       |          |       |
| T-02    |           |                      |        |       |         |       |          |       |
| ...     |           |                      |        |       |         |       |          |       |

Column definitions:
- `Tier-ID` -- T-01, T-02, ... Permanent for this analysis. All downstream tables and sections
  use these identifiers verbatim. No synonyms.
- `Limit` -- a number with a unit. Vague entries ("limited", "throttled", "around 500") are
  invalid. If the limit cannot be confirmed from documentation, write `unknown [undocumented]`
  and write `not documented` in `Source`.
- `Source` -- the specific named document and section that contains the number in `Limit`.
  Passing examples: "Power Automate limits reference -- 'Request limits and allocations'",
  "SharePoint connector throttling guide -- 'API call limits' table". Failing examples:
  "Microsoft docs", "PA documentation", "connector reference" (too generic). If `Limit` is
  `unknown [undocumented]`, `Source` must be `not documented` -- not blank.
- `UNIFORM` -- throttle status when the given volume arrives evenly (within 10% of average rate):
  OK, HIT, or SAT.
- `BURST` -- throttle status when the same total volume arrives in the first 20% of the window
  (instantaneous rate 5x the uniform rate). At least one tier must differ from its UNIFORM
  status. If no tier differs, Notes must explain the mechanism.
- `Binding?` -- Y for the first-hit tier under uniform arrival. At most one Y.

---

**TABLE B -- BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Source: the TABLE A binding constraint. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`From` must use a TABLE A Tier-ID. `Mechanism`: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade. Generic entries fail.

---

**TABLE C -- USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                   |                                      |                               |
| T-02    |                     |                           |                   |                                      |                               |
| ...     |                     |                           |                   |                                      |                               |

---

**TABLE D -- UNPROTECTED BURST PATHS**

*(Minimum one row. If no path exists, row 1 states the conclusion with two named controls.)*

| Path-ID | Entry component | Gap reason (specific structural explanation) | Tier-IDs bypassed | Consequence at burst volume |
|---------|----------------|---------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                             |                   |                             |

---

After the four tables, produce three sections:

**BOTTLENECK AND CAUSAL REASON** -- TABLE A binding constraint Tier-ID, numeric limit exceeded,
source document, and the causal reason this tier binds first.

**RISK RANKING AND CASCADE SCENARIO** -- rank all TABLE A tiers by business risk. For the
top-ranked tier: blast radius, failure visibility, recovery time. One sentence per remaining tier.
Then trace one cascade from the binding constraint. Use Tier-IDs. Minimum three tiers.

**MITIGATION PRESCRIPTIONS** -- for the two highest-priority gaps from TABLE A and TABLE D:
specific component, setting name/API parameter, target value, expected observable outcome.
Name the specific change; generic advice fails.

---

**COVERAGE SELF-VERIFICATION**

Complete before closing. Mark each criterion COVERED, PARTIAL, or NOT COVERED.
- COVERED: add a pointer to where in the output it appears.
- PARTIAL: describe what is missing.
- NOT COVERED: state whether signal was insufficient or criterion is not applicable.

Honest reporting earns credit. An output that marks a criterion NOT COVERED and explains why
outscores one that silently omits it.

| Criterion | Status | Pointer or explanation |
|-----------|--------|------------------------|
| C-01: Primary bottleneck with causal reason | | |
| C-02: Backpressure traced, min two hops | | |
| C-03: At least two tiers with enforcing component | | |
| C-04: UX described for every named tier | | |
| C-05: Unprotected burst path or named controls as evidence | | |
| C-06: Retry-After compliance assessed for at least one caller | | |
| C-07: Two-tier cascade named | | |
| C-08: At least one numeric threshold stated | | |
| C-09: Two mitigations with specific changes and outcomes | | |
| C-10: Burst status differs from uniform for at least one tier | | |
| C-11: Every numeric threshold attributed to a named source | | |
| C-12: Self-check present and names all criteria | | (auto-satisfied) |

---

## V-05 -- Combined: Source Register + Inertia Framing + Burst/Uniform Columns + Mitigation Prescriptions + Self-Verification

**Axis:** Combined -- the full integration of both new v2 criteria with the highest-performing
patterns from Round 1 and Round 2. The inertia preamble names load-shape blindness and
undocumented thresholds as the two mechanisms by which throttle analysis fails. A source-register
phase (from V-03) creates a traceable link between documentation and numbers. TABLE A has
burst/uniform split columns. T-NN identifiers propagate through all tables. A gated mitigation
section forces C-09. A terminal self-verification section forces C-12.

**Hypothesis:** Round 1 V-05 produced the strongest baseline (87/100 under v1 rubric) using
inertia framing + burst/uniform + mitigation. Its v2 gaps are C-11 and C-12: numbers appeared
without attribution, and there was no self-check. This variant adds the source-register phase
to close C-11 and the terminal self-verification to close C-12. The inertia preamble is extended
to name "undocumented numbers you can't trust" as the third failure mechanism alongside
load-shape blindness and finding-without-fixing. All twelve criteria have either structural
enforcement or motivational framing. Risk: the added source-register phase and self-check section
add length; if the model approaches token limits, the cascade scenario or mitigation prescriptions
may be abbreviated. The phase gate structure mitigates this by enforcing order.

---

**THE INERTIA PROBLEM**

Throttle failures reach production through three mechanisms. All three are caused by analysis
that stops too early.

The first: the team tested at uniform load. Production traffic arrived in bursts. The burst hit
a tier that uniform load never stressed. 2am incident.

The second: the team found the gaps. They documented them. They shipped anyway because the
findings were descriptive -- "this tier throttles" -- not prescriptive -- "change this setting
to this value." The same incident happened two months later.

The third: the team's analysis cited thresholds without verifying them against documentation.
The "600 req/min" limit turned out to be an inference from a forum post, not the actual connector
cap. The real cap was 300 req/min. The 2am incident happened at half the expected volume.

The analysis below closes all three gaps: it commits to documentation sources before writing any
number, it tests both arrival patterns, and it prescribes specific changes rather than findings.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the
rate-limited system described in the signal for the given request volume. Execute phases in order.

---

**PHASE 0 -- SOURCE REGISTRATION**

Before writing any tier inventory, enumerate every documentation source you will draw numeric
rate limits from:

- Source name (specific document -- not "Microsoft docs" but the document title)
- Section or table within that document
- Tiers this source covers

Use a numbered list. State which tiers, if any, have no documentation source and must be flagged
`unknown [undocumented]` in Phase 1. Do not assign a number to any undocumented tier.

State "Phase 0 complete -- [N] sources, [N] undocumented tiers" before Phase 1.

---

**PHASE 1 -- THROTTLE TIER INVENTORY**

*(Opens after Phase 0.)*

| Tier-ID | Component | Limit (number + unit) | Source ref | Scope | UNIFORM | BURST | Binding? | Notes |
|---------|-----------|----------------------|------------|-------|---------|-------|----------|-------|
| T-01    |           |                      |            |       |         |       |          |       |
| T-02    |           |                      |            |       |         |       |          |       |
| ...     |           |                      |            |       |         |       |          |       |

Column definitions:
- `Limit` -- a number with a unit. Any number not traceable to a Phase 0 source is an invented
  value -- replace with `unknown [undocumented]`. This is the third inertia failure mode.
- `Source ref` -- the Phase 0 source number (e.g., "[1]", "[2]") that contains this limit.
  If `Limit` is `unknown [undocumented]`, write `none -- not in registry`.
- `UNIFORM` -- throttle status at the given volume with even arrival (within 10% of average): OK / HIT / SAT.
- `BURST` -- throttle status at the same total volume arriving in the first 20% of the window
  (5x instantaneous rate). This is the first inertia failure mode -- the pattern nobody tested.
  At least one tier must differ from its UNIFORM status.
- `Binding?` -- Y for the first-hit tier under uniform arrival. At most one Y.

These Tier-IDs are permanent. All subsequent phases use them verbatim.

State "Phase 1 complete" before Phase 2.

---

**PHASE 2 -- BACKPRESSURE AND BURST PATH SCAN**

*(Opens after Phase 1.)*

Part A -- Backpressure propagation from the Phase 1 binding constraint. Each hop: Tier-ID or
component, mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall /
timeout-cascade), observable effect. Minimum two hops.

Part B -- Burst path scan: identify any path where burst traffic enters without a rate limit.
Entry component, route, specific gap reason (missing connector policy / trigger type exempt from
queuing / endpoint bypasses gateway / no concurrency cap). If no path exists, name two controls
as evidence. This is the path the first inertia failure mode describes -- find it.

State "Phase 2 complete" before Phase 3.

---

**PHASE 3 -- USER EXPERIENCE AND RETRY-AFTER ASSESSMENT**

*(Opens after Phase 2.)*

For every Phase 1 tier: error code or signal, Retry-After present (Y/N) with value, visible in
run history (Y/N/SILENT), failure if Retry-After ignored. No tier omitted. For the binding
constraint: explicit verdict on whether Retry-After handling is correct.

State "Phase 3 complete" before Phase 4.

---

**PHASE 4 -- RISK RANKING AND CASCADE SCENARIO**

*(Opens after Phase 3.)*

Rank all Phase 1 tiers by business risk (highest to lowest). Top-ranked tier: blast radius,
failure visibility (silent vs. explicit, with time estimate), recovery time. One sentence per
remaining tier. Then trace one concrete cascade from the binding constraint: Tier-IDs, causal
link at each step, compounded effect. Minimum three tiers.

State "Phase 4 complete" before Phase 5.

---

**PHASE 5 -- MITIGATION PRESCRIPTIONS**

*(Opens after Phase 4. Mandatory. Cannot be merged with Phase 4.)*

This phase exists because the second inertia failure mode is producing findings without prescribing
changes. For at least two gaps from Phases 1 through 4:

1. **Gap** -- Tier-ID or Path-ID, failure mode, phase where identified.
2. **Component to modify** -- the named component (not a layer).
3. **Specific change** -- setting name + target value, or API parameter + value, or exact retry
   policy configuration. Generic advice ("add retry handling", "tune the limits") fails this field.
4. **Expected outcome** -- quantified or observable: what changes after the fix.

Where the change aligns with a documented limit from Phase 0, cite the source number.

Gate condition: at least two complete entries with all four fields. Partial entries fail the gate.

State "Phase 5 complete" before the self-verification.

---

**COVERAGE SELF-VERIFICATION**

Complete before closing. Mark each criterion COVERED, PARTIAL, or NOT COVERED.
- COVERED: one-phrase pointer to where in the output it appears.
- PARTIAL: what is missing.
- NOT COVERED: signal insufficient or not applicable -- explain.

Honesty earns credit. Self-reporting a gap scores better than silent omission.

| Criterion | Status | Pointer or explanation |
|-----------|--------|------------------------|
| C-01: Primary bottleneck with causal reason | | |
| C-02: Backpressure traced, min two hops | | |
| C-03: At least two tiers with enforcing component | | |
| C-04: UX described for every named tier | | |
| C-05: Unprotected burst path or named controls as evidence | | |
| C-06: Retry-After compliance assessed for at least one caller | | |
| C-07: Two-tier cascade named | | |
| C-08: At least one numeric threshold stated | | |
| C-09: Two mitigations with specific changes and outcomes | | |
| C-10: Burst status differs from uniform for at least one tier | | |
| C-11: Every numeric threshold attributed to a named source | | |
| C-12: Self-check present and names all criteria | | (auto-satisfied) |

---

**COMPLETION CHECK**

```
Phase 0: Sources registered: [N] | Undocumented tiers declared: [list or none]
Phase 1: Tiers enumerated: [N] | Source-traced limits: [N] | Undocumented limits: [N]
Phase 1: BURST differs from UNIFORM for: [Tier-ID list]
Phase 2A: Backpressure hops: [N] | Mechanisms: [list]
Phase 2B: Burst paths found: [N] | Controls named as evidence (if zero paths): [list]
Phase 3: Tiers in UX catalog: [N] | Retry-After verdict: [pass/fail/partial]
Phase 4: Tiers ranked: [N] | Cascade tiers: [list]
Phase 5: Prescriptions complete: [N]
Self-verification: All 12 criteria addressed: [Y/N -- if N, list NOT COVERED]
```
