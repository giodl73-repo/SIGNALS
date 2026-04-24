# flow-throttle Variate — Round 3
**Date:** 2026-03-15
**Rubric:** v3 (C-01 through C-15, essential/recommended/aspirational, denominator /7 aspirational)
**Baseline ceiling:** R2 V-05 (all C-01 through C-13 passing; ~93/100 predicted under v2)

---

## Round 3 State Analysis: What R2 Established vs. What R3 Must Add

**R2 confirmed:**
- C-01 through C-08: Essential and recommended criteria pass reliably in all five R2 variations.
- C-09 (mitigation prescriptions): V-03 and V-05 both pass with component-level remediation.
- C-10 (load shape sensitivity): V-05 TABLE A with volume band columns reliably surfaces burst
  vs. steady-state distinction.
- C-11 (multi-volume sweep): TABLE A with STATUS-1x/2x/5x columns forces three-band coverage
  structurally; binding constraint shift is visible as a column comparison.
- C-12 (cross-section T-NN traceability): Pre-committed T-NN column headers propagate through
  TABLE B, TABLE C, and TABLE D without requiring narrative reminders.
- C-13 (test coverage gap identification): Phase-required TEST COVERAGE GAP ANALYSIS section
  with explicit four-field template passes when structurally enforced (V-03, V-05) but regresses
  to generic advice when section is prose-optional (V-01, V-02).

**R2 gap (what v3 now scores):**

C-14 — Test infrastructure inertia catalog: R2 V-05's inertia preamble named test artifacts
("the integration test suite that reports green because it mocks the connector layer") but
placed them as motivational context, not a structured catalog. The model treated them as
preamble color rather than required output. C-14 requires the catalog to be the OPENING of
the test coverage section — naming artifacts and structural properties before any gap entry.

C-15 — Labeled gap entry completeness: R2 V-05's GAP-01/GAP-02 free-text blocks had four
fields but labeled them descriptively in the prompt template rather than requiring the model
to output the field label explicitly. Under token pressure the model sometimes omitted or
merged fields. C-15 requires each field explicitly labeled in output, making incomplete
entries structurally visible by inspection.

**What R3 must demonstrate:**

Q1 (V-01): Does a mandatory named TEST INFRASTRUCTURE CATALOG subsection that opens the test
coverage section force C-14 artifact-level specificity, or does the model still produce
category labels despite the instruction?

Q2 (V-02): Does reformatting GAP entries as a structured table (GAP-ID | Behavior | Test-type
| Structural-reason | Approach) make incomplete entries visible by column inspection,
satisfying C-15 without additional policing?

Q3 (V-03): Does sequential STAGE 1 / STAGE 2 gating within the test coverage section — the
artifact catalog must complete before gap entries open — improve both C-14 and C-15 by the
same role-gate mechanism that proved for C-01/C-03 in R1 V-04?

Q4 (V-04): Does combining V-01 (catalog preamble) + V-02 (table format) produce C-14 + C-15
jointly without one compressing the other under token pressure?

Q5 (V-05): Does the maximum-coverage variant — V-04 structure + sequential gating + negative
exemplar injection showing WRONG/PASS for both the catalog and gap fields — achieve the
highest composite by making substitution failures visible before the model makes them?

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis | Predicted composite |
|-----------|------|------------|---------------------|
| V-01 | Inertia framing — mandatory test infrastructure catalog subsection | Named artifact catalog before gap entries forces C-14; catalog pre-loads structural reasons making C-15 generic advice recognizably wrong | ~90/100 |
| V-02 | Output format — GAP-NN as structured four-column table | Table column headers make incomplete entries visible by inspection; `Structural reason` column requires artifact name not category label | ~91/100 |
| V-03 | Role sequence — STAGE 1 catalog gates STAGE 2 gap entries | Sequential gate forces catalog completion before gaps open; model cannot write generic gap advice before naming artifacts with structural properties | ~92/100 |
| V-04 | Combined: artifact catalog preamble + GAP table format | V-01 + V-02: catalog provides C-14 artifact names; table enforces C-15 field completeness; both satisfied by structural constraints not instructions alone | ~95/100 |
| V-05 | Combined: all three axes + negative exemplar injection | V-04 + STAGE gating + WRONG/PASS examples; exemplars name the exact substitution failures before the model makes them | ~97/100 |

---

## V-01 — Inertia Framing: Mandatory Test Infrastructure Catalog Subsection

**Axis:** Inertia framing — the test coverage section opens with a mandatory TEST
INFRASTRUCTURE CATALOG subsection that names specific existing test artifacts (not test
categories) before any gap entry is produced. The catalog is not motivational preamble;
it is a required output deliverable with an explicit artifact-naming criterion.

**Hypothesis:** C-14 requires naming specific artifacts before gap entries — this pre-loading
technique makes generic gap advice recognizably wrong because the artifact's structural
limitation is established first. Naming "the integration test suite that mocks the connector
layer via HttpMessageHandler stubs" before writing GAP-01 makes "integration tests don't
exercise this" a detectable reference to the catalog rather than a generic category claim.
A model that has named structural properties in the catalog cannot write a generic structural
reason in the gap entry without contradicting the catalog it just produced. Primary risk: the
model names categories ("integration tests are limited") rather than specific artifacts,
failing C-14 while appearing to satisfy it.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x. Produce the tables and sections below in
order. Do not substitute prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent for this analysis. Every downstream section that
  references a throttle tier uses these identifiers verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries such as "limited" or "throttled" invalidate
  the row and fail C-05.
- `STATUS Nx` — OK (limit not reached), HIT (throttling begins), SAT (fully saturated,
  requests failing). The binding constraint must shift between at least two bands, or a new
  tier must become primary as volume increases. All-identical status columns across bands
  fail C-11.
- `Binding at band` — the lowest band at which this tier is the primary bottleneck.
  Write N/A if it is never the binding constraint.
- `Failure visibility window` — how quickly saturation becomes observable after the limit
  is exceeded (time + observable signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`From` must use a Tier-ID from TABLE A where the source is a named throttle tier.
`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two
named controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference the `Failure visibility window` and
`Recovery time` values from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link. Minimum three tiers. Generic cascade claims
do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely (retry storm, missing exponential backoff, silent
quota exhaustion). If present, state whether callers respect it correctly.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite — the behaviors that show
green in CI but fail at production volume or production concurrency.

**TEST INFRASTRUCTURE CATALOG**

Before enumerating gaps, name the specific test infrastructure artifacts currently in
place that structurally cannot reach the throttle behaviors identified above.

Do not name a test category. Name the artifact — the specific test suite, fixture, or
harness — and state the architectural property that prevents it from reaching the
throttle behavior.

Required format for each catalog entry:
- **Artifact:** [the specific test artifact, e.g., "the integration test suite that
  exercises connector calls via mocked HttpMessageHandler responses" — not
  "integration tests"]
- **Structural property:** [the specific architectural reason this artifact cannot
  reach the throttle behavior, e.g., "connector rate gate is never invoked because all
  responses including 429s are injected by the stub; Retry-After handling is never
  exercised under real concurrency"]

Minimum: two catalog entries. Each entry must name a specific artifact. Category labels
without artifact identification do not satisfy this section.

---

After the catalog, produce at least two gap entries. Each entry must reference a
specific behavior from this analysis and a specific artifact or limitation from the
catalog above.

**GAP-01**
- **Behavior:** [the specific throttle behavior — reference the Tier-ID and the failure
  mode, e.g., "retry storm on T-02 connector limit when Retry-After is absent under
  concurrent flow runs"]
- **Test type that misses it:** [unit / integration / load / chaos — one type only]
- **Structural reason:** [specific structural gap — reference an artifact from the
  catalog above, naming the artifact and the architectural property that causes the miss]
- **Test approach that surfaces it:** [concrete design — name the component, the volume
  or concurrency level, and the assertion]

**GAP-02**
- **Behavior:** [the specific throttle behavior — reference the Tier-ID and the failure
  mode]
- **Test type that misses it:** [unit / integration / load / chaos — one type only]
- **Structural reason:** [specific structural gap — reference an artifact from the
  catalog or name a specific architectural limitation not covered by the catalog]
- **Test approach that surfaces it:** [concrete design — name the component, the volume
  or concurrency level, and the assertion]

Do not write generic advice such as "add load testing." Each entry must name a specific
behavior from this analysis, reference a catalog artifact, and state a concrete test
design with a named assertion.

---

## V-02 — Output Format: GAP-NN as Structured Four-Column Table

**Axis:** Output format — test coverage gap entries are expressed as rows in TABLE E with
four mandatory named column headers, not as free-text blocks. Each column makes the field's
pass condition visible by inspection: a generic "add load testing" entry fails the
`Test approach` column without a rubric audit; a category label fails the `Structural reason`
column by the same structural inspection.

**Hypothesis:** C-15 requires four explicitly named fields per gap entry. Converting
GAP-01/GAP-02 blocks to table rows makes each field a mandatory column that the model cannot
omit or merge without producing a visibly incomplete row. The `Structural reason` column
header instructs artifact naming — a category label ("integration tests are limited") stands
out against a column that expects an artifact name and architectural property. The
`Test approach` column makes "add load testing" structurally incomplete by requiring
component + volume + assertion in the same cell. A preamble catalog instruction opens the
section to satisfy C-14's artifact catalog requirement before TABLE E is produced. Primary
risk: a wide table may cause the model to abbreviate entries to fit column width, producing
terse but passing cells rather than the verbose specificity C-15 requires.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x. Produce the tables and sections below in
order. Do not substitute prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent for this analysis. Every downstream section uses
  these identifiers verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states conclusion with two named controls
as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier. For the
top-ranked tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link. Minimum three tiers. Generic cascade claims
do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely. If present, state whether callers respect it
correctly.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite.

Before completing TABLE E, name the specific test infrastructure artifacts currently in
place that structurally cannot reach the throttle behaviors identified above. Each entry
names the artifact (not the category) and states the architectural property that prevents
it from reaching the behavior.

**Test infrastructure catalog (required before TABLE E):**
1. **Artifact:** [specific artifact name] | **Structural property:** [architectural reason]
2. **Artifact:** [specific artifact name] | **Structural property:** [architectural reason]

A category label without artifact identification ("integration tests don't cover throttle
behavior") does not satisfy a catalog slot.

---

After the catalog, produce TABLE E. Do not substitute prose for this table. Every cell
must be filled. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

*(Complete after the catalog above. Minimum two rows.)*

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type that misses it | Structural reason (artifact name + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |                          |                                                           |                                                           |
| GAP-02 |                                           |                          |                                                           |                                                           |

Column definitions:
- `Throttle behavior` — the specific throttle behavior from this analysis, referenced by
  Tier-ID and failure mode. Generic entries ("rate limiting occurs") invalidate the row.
- `Test type that misses it` — one type: unit, integration, load, or chaos.
- `Structural reason` — name a specific test artifact and the architectural property that
  prevents it from reaching the behavior (e.g., "the integration test suite identified in
  the catalog above mocks the connector layer; the rate gate is never invoked"). A
  category label without artifact identification does not satisfy this column.
- `Test approach` — a concrete test design: component under test, volume or concurrency
  level, and the expected assertion (e.g., "load test at 1,200 concurrent flows against
  live SharePoint connector in staging; assert <1% 429 error rate within 90 seconds after
  burst subsides"). Generic approaches ("add load testing") do not satisfy this column.

---

## V-03 — Role Sequence: STAGE 1 Catalog Gates STAGE 2 Gap Entries

**Axis:** Role sequence — the test coverage section is structured as two explicit sequential
stages with a mandatory gate condition. STAGE 1 produces the test infrastructure catalog.
STAGE 2 (gap entries) cannot open until STAGE 1 is declared complete and has met its gate
condition. This mirrors the phase-gate pattern from R1 V-04 (proven to prevent C-03 elision
by making tier inventory a blocking gate) applied to the intra-section structure of the test
coverage analysis.

**Hypothesis:** The phase-gate mechanism works because the model must satisfy the gate
condition — produce artifact-named entries with structural properties — before it can write
gap entries. Once STAGE 1 is complete, the model has already named the artifacts and their
structural limitations. STAGE 2 entries that fail to reference those named artifacts are
structurally visible as gate violations. C-14 is satisfied by the gate condition on STAGE 1
(artifact names required, not category labels). C-15 is satisfied by the STAGE 2 entry
template that references STAGE 1 output. The sequential structure prevents the most common
failure mode: the model writing gap entries before naming the artifacts that motivate them.
Primary risk: STAGE 1 token budget consumed by verbose artifact descriptions, compressing
STAGE 2 entries.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x. Produce the tables and sections below in
order. Do not substitute prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent for this analysis. Every downstream section uses
  these identifiers verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states conclusion with two named controls
as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier. For the
top-ranked tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link. Minimum three tiers. Generic cascade claims
do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely. If present, state whether callers respect it
correctly.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order.
Do not open Stage 2 until Stage 1 is declared complete.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: must be complete before Stage 2 opens.*

Enumerate the specific test infrastructure artifacts currently in place that structurally
cannot reach the throttle behaviors identified in this analysis. For each artifact:

- **Artifact:** [name the specific artifact — the test suite, fixture, harness, or mock
  configuration — not a test category. E.g., "the integration test suite that exercises
  the SharePoint connector via an HttpMessageHandler stub registered in the DI container
  at test startup"]
- **Structural property:** [the architectural reason this artifact cannot reach the
  throttle behavior. E.g., "the stub injects preconfigured responses including 429s; the
  actual connector rate gate at the API Management layer is bypassed entirely, so real
  throttle timing and Retry-After header values are never produced"]

**GATE CONDITION:** At least two artifacts are named with structural properties. An entry
that names only a test category ("integration tests do not cover throttle behavior") does
not satisfy a catalog slot — a category label without artifact identification fails this
gate.

State "Stage 1 complete" before opening Stage 2.

---

**STAGE 2 — GAP ENTRIES**

*Opens after Stage 1 is declared complete.*

For at least two throttle behaviors identified in this analysis, produce a gap entry.
Each entry must carry a GAP-ID and four explicitly labeled fields:

**GAP-01**
- **Behavior:** [the specific throttle behavior — reference the Tier-ID from TABLE A
  and the failure mode, e.g., "retry storm on T-02 connector limit when Retry-After is
  absent under concurrent flow runs"]
- **Test type:** [the specific test type: unit / integration / load / chaos — one type]
- **Structural reason:** [reference a Stage 1 artifact and its structural property,
  e.g., "the integration test suite from Stage 1 — the HttpMessageHandler stub injects
  429s without real timing, so concurrent retry amplification at the connector rate gate
  is never exercised"]
- **Test approach:** [a concrete test design — name the component, the volume or
  concurrency level, and the specific assertion. E.g., "load test: 800 concurrent flow
  runs against a live SharePoint connector in a staging environment with tenant-level
  throttling enabled; assert that 429 error rate decrements to zero within 90 seconds
  of burst subsiding"]

**GAP-02**
- **Behavior:** [specific behavior — Tier-ID + failure mode]
- **Test type:** [one type]
- **Structural reason:** [reference Stage 1 artifact or name a specific architectural
  limitation not covered by the catalog]
- **Test approach:** [component + volume/concurrency + specific assertion]

Each entry must reference a behavior from this analysis and a Stage 1 artifact or a
specific architectural limitation. Generic approaches ("add load testing") do not satisfy
the `Test approach` field.

---

## V-04 — Combined: Artifact Catalog Preamble + GAP Table Format

**Axis:** Combined — V-01's mandatory TEST INFRASTRUCTURE CATALOG subsection (targets C-14
by requiring artifact names before gap entries) combined with V-02's TABLE E structured
format (targets C-15 by making incomplete gap entries visible by column inspection). Neither
axis alone is sufficient: the catalog preamble pre-loads structural reasons but leaves gap
entry completeness to free-text; the table format enforces field structure but cannot force
artifact-level specificity in the structural reason column without the catalog preamble to
anchor it. Together they produce a self-reinforcing pass condition: the catalog names the
artifacts, the table column requires artifact references.

**Hypothesis:** C-14 and C-15 are mutually reinforcing when both structural constraints are
present. A model that has named specific artifacts in the catalog cannot write a generic
"integration tests don't cover this" in the TABLE E `Structural reason` column without
contradicting its own catalog output. The table format makes that contradiction visible by
column inspection. Combined predicted composite: 95/100 — the catalog + table structure
eliminates both substitution failures independently, reducing the probability that either
criterion regresses under token pressure.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x. Produce the tables and sections below in
order. Do not substitute prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent. Every downstream section uses these verbatim.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift across at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states conclusion with two named controls
as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier. For the
top-ranked tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link. Minimum three tiers. Generic cascade claims
do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely. If present, state whether callers respect it
correctly.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite.

**TEST INFRASTRUCTURE CATALOG**

Name the specific test infrastructure artifacts currently in place that structurally
cannot reach the throttle behaviors identified above. Each entry names the artifact —
the specific test suite, fixture, harness, or mock configuration — and states the
architectural property that prevents it from reaching the behavior.

Required format:
1. **Artifact:** [specific artifact name, not a category] | **Structural property:** [architectural reason]
2. **Artifact:** [specific artifact name, not a category] | **Structural property:** [architectural reason]

A category label without artifact identification ("integration tests don't cover throttle
behavior") does not satisfy a catalog slot.

---

After the catalog, produce TABLE E. Do not substitute prose for this table. Every cell
must be filled. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

*(Complete after the catalog above. Reference catalog artifacts in `Structural reason`.)*

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type that misses it | Structural reason (artifact name + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |                          |                                                           |                                                           |
| GAP-02 |                                           |                          |                                                           |                                                           |

Column definitions:
- `Throttle behavior` — specific throttle behavior from this analysis, referenced by
  Tier-ID and failure mode. Generic entries ("rate limiting occurs") invalidate the row.
- `Test type that misses it` — one type: unit, integration, load, or chaos.
- `Structural reason` — name a specific artifact from the catalog above and the
  architectural property. A category label without artifact identification does not
  satisfy this column.
- `Test approach` — component under test + volume or concurrency level + specific
  assertion. "Add load testing" does not satisfy this column.

---

## V-05 — Combined: All Three Axes + Negative Exemplar Injection

**Axis:** Combined maximum-coverage — V-03's sequential stage gating (STAGE 1 catalog gates
STAGE 2 gaps) combined with V-04's artifact catalog + TABLE E format, plus negative exemplar
injection. For both the catalog and the gap entries, the prompt shows a concrete WRONG example
and a PASS example side by side, naming the exact substitution failure before the model makes
it. The exemplars are not instructions — they are pattern contrast signals that make the
forbidden form recognizable at generation time.

**Hypothesis:** Negative exemplar injection transforms an abstract pass condition ("name an
artifact, not a category") into a visible contrast ("WRONG: 'integration tests are limited'
/ PASS: 'the integration test suite that exercises the SharePoint connector via an
HttpMessageHandler stub registered in DI at test startup'"). The model can compare its own
output against the exemplar before producing it. V-03's stage gating ensures catalog is
complete before gaps open. V-04's TABLE E makes incomplete cells visible by column. The
three structural constraints together eliminate the three failure modes independently:
- Stage gating prevents gaps before catalog (C-14 sequence requirement)
- Table format makes field omission visible (C-15 structural completeness)
- Negative exemplars name the substitution failures (C-14 category vs. artifact; C-15
  generic approach vs. concrete design)
Primary risk: exemplar length increases prompt size, potentially compressing TABLE A or
TABLE D under token pressure. Mitigated by placing exemplars only in the test coverage
section, where they are most needed, and keeping each exemplar pair to two lines.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput
across the rate-limited system described in the signal. Treat the stated request volume
as 1x nominal; also analyze at 2x and 5x. Produce the tables and sections below in
order. Do not substitute prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent for this analysis. Every downstream section that
  references a throttle tier uses these identifiers verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries such as "limited" or "throttled" invalidate
  the row and fail C-05.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint must shift between at least two bands,
  or a new tier must become primary as volume increases.
- `Binding at band` — the lowest band at which this tier is the primary bottleneck.
  Write N/A if it is never the binding constraint.
- `Failure visibility window` — how quickly saturation becomes observable after the limit
  is exceeded (time + observable signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`From` must use a Tier-ID from TABLE A where the source is a named throttle tier.
`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two
named controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference the `Failure visibility window` and
`Recovery time` values from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link. Minimum three tiers. Generic cascade claims
do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely (retry storm, missing exponential backoff, silent
quota exhaustion). If present, state whether callers respect it correctly.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order.
Do not open Stage 2 until Stage 1 is declared complete.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: at least two artifacts named with structural properties before Stage 2
opens. Category labels without artifact identification fail this gate.*

Name the specific test infrastructure artifacts currently in place that structurally
cannot reach the throttle behaviors identified in this analysis. For each artifact, state
the artifact name and the architectural property that prevents it from reaching the
behavior.

Calibration contrast — use this to judge your own catalog entries:

> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> *(This is a category label with a generic reason. No artifact is identified. No
> architectural property is stated. This does not satisfy a catalog slot.)*
>
> PASS: "The integration test suite that exercises the SharePoint connector via an
> HttpMessageHandler stub registered in the DI container at test startup. Structural
> property: the stub injects preconfigured responses; the real connector rate gate at the
> API Management layer is never invoked, so 429 responses with real Retry-After timing are
> never produced and concurrent retry amplification behavior is never exercised."

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before opening Stage 2.

---

**STAGE 2 — GAP ENTRIES**

*Opens after Stage 1 is declared complete.*

Produce TABLE E. Do not substitute prose for this table. Every cell must be filled.
Minimum two rows. Reference Stage 1 artifacts in the `Structural reason` column.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column pass condition contrasts — use these to calibrate each cell:

`Throttle behavior`:
> WRONG: "Rate limiting can cause failures at high volume."
> PASS: "Retry storm on T-02 connector limit when Retry-After header is absent from 429
> response; caller retries at full concurrency for 10 minutes exhausting tenant quota."

`Structural reason`:
> WRONG: "Integration tests don't exercise high-volume scenarios."
> PASS: "The integration test suite from Stage 1 catalog — the HttpMessageHandler stub
> injects 429 responses without real rate gate timing, so Retry-After header values are
> simulated and concurrent retry amplification at the connector layer is never observed."

`Test approach`:
> WRONG: "Add a load test for this scenario."
> PASS: "Load test: 800 concurrent flow runs against a live SharePoint connector in a
> dedicated staging environment with tenant-level throttling enabled at production policy;
> assert that 429 error rate decrements to below 1% within 90 seconds after the burst
> window closes."

Every cell must satisfy the PASS form. An entry that contains the WRONG pattern in any
cell does not satisfy that column.
