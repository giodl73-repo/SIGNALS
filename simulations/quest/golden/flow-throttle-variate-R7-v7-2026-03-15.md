# flow-throttle Variate — Round 7 (v7 Rubric)
**Date:** 2026-03-15
**Rubric:** v7 (C-01 through C-26, 5 essential / 3 recommended / 18 aspirational, denominator 18)
**Baseline:** R7 V-05 (v6 rubric, 110/110) — emerges C-24, C-25, C-26 implicitly.

---

## Round 7 (v7) Purpose

R7 V-05 under v6 achieved 110/110 with emergent C-24/25/26 patterns. These patterns were
present in the output but not explicitly required by any v6 criterion. The v7 rubric
formalizes them:

- **C-24** — the two-line `- Verdict:` / `- If FAIL —` format with full identification
  schema (informal name used + section location + T-NN) was present in R7 V-05's
  INTEGRITY VERIFICATION block as a template, but not explicitly required by C-22.
- **C-25** — per-item `[Y — present / N — missing]` verdicts per step followed by an
  aggregate failure list was present in R7 V-05's C-19 compliance field, but not
  explicitly required by C-19.
- **C-26** — the circular-dependency structural proof in the deferral prohibition was
  present in R7 V-05 ("load-shape classification requires the registered Limit value...
  Step 2G depends on the per-tier verdict — deferring creates a circular dependency") but
  not required at that precision by C-23.

These variations explore whether these properties remain stable across presentation axes,
and test whether making them explicit structural requirements in the prompt produces more
reliable output than the example-based templates in R7 V-05.

**Variation axes:**
1. **Role sequence** (V-01) — single role vs. dual-role opening
2. **Output format** (V-02) — explicit named-template audit format vs. example-based
3. **Phrasing register** (V-03) — explanatory/WHY-first for enforcement blocks
4. **Role sequence + phrasing register** (V-04) — combined
5. **All three axes** (V-05) — maximum density targeting C-24 + C-25 + C-26 explicitly

**Predicted v7 scores:**

| Variation | Axes | C-24 | C-25 | C-26 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 | Single role | PASS | PASS | PASS | 18/18 | **110** |
| V-02 | Explicit audit template | PASS | PASS | PASS | 18/18 | **110** |
| V-03 | Explanatory register | PASS | PASS | PASS | 18/18 | **110** |
| V-04 | Single role + explanatory | PASS | PASS | PASS | 18/18 | **110** |
| V-05 | All three axes | PASS | PASS | PASS | 18/18 | **110** |

**Differentiation question:** If all five predict 110, what varies?

All five inherit C-24/25/26 from R7 V-05 baseline. The variation axes test presentation
risk profiles — which format is most reliable under output pressure:

- V-01 risk: single-role lacks UX priming; TABLE C may produce shallower tier UX entries
- V-02 risk: named-template audit is more rigid; may reduce natural output flow
- V-03 risk: explanatory register adds token cost to enforcement blocks; may compress tables
- V-04 risk: combined cost of V-01 savings + V-03 additions roughly neutral
- V-05 risk: maximum token cost; highest theoretical reliability if compression doesn't fire

**Round 7 (v7) questions:**

Q1: Does removing the dual-role pre-analysis (V-01) affect TABLE C UX catalog quality?
Hypothesis: single-role with INERTIA PROBLEM block maintains sufficient UX context for
TABLE C without the pre-analysis prose loading time.

Q2: Does the explicit named-template audit format (V-02) produce more reliable C-24
identification schema (informal name + location + T-NN) than the example-based template?
Hypothesis: explicit format instructions are more reliable than example-derived format
under token pressure — the example can be dropped while the explicit template cannot.

Q3: Does the explanatory register (V-03) produce more reliable C-26 proof execution?
Hypothesis: when the structural proof is presented as a logical chain (premise 1 +
premise 2 = contradiction) rather than as an embedded prohibition paragraph, the model
is less likely to compress the proof into a one-sentence summary.

---

## V-01 — Single Axis: Role Sequence (Single Role, No Pre-Analysis)

**Axis:** Remove the dual-role opening from R7 V-05. Replace ROLE 1 (flow author
pre-analysis) with a single-role instruction: "You are a Connectors / Power Automate
throughput domain expert." Retain the INERTIA PROBLEM preamble as the source of UX
context priming. All structural elements from R7 V-05 are preserved: STEP 1 (TIER
REGISTRY with TABLE A + Load-shape deferral prohibition with escape-route story and
circular-dependency proof), STEP 2 (analysis phases with distributed reminders), STEP 3
(test coverage gap analysis with STAGE 1 + TABLE E), STEP 4 (INTEGRITY VERIFICATION with
C-24 two-line format and C-25 per-item verdicts).

**Hypothesis:** The dual-role sequence in R7 V-05 loads UX vocabulary into working
context before TABLE C demands it. Removing the pre-analysis saves ~150 tokens but risks
shallower TABLE C entries (error codes, retry behavior specifics). If the INERTIA PROBLEM
block ("the missing Retry-After handler that turns a 30-second window into a 10-minute
retry storm") provides sufficient UX priming without the full pre-analysis, V-01 achieves
the same structural outcomes at lower token cost. Primary risk: TABLE C UX entries may
default to generic descriptions ("error 429") rather than specific retry behavior and
visibility-window details.

**v7 predicted scoring:** all 18 aspirational pass, including C-24 PASS (two-line format
present in STEP 4), C-25 PASS (per-item verdicts in C-19 check), C-26 PASS (structural
proof in deferral prohibition). Composite = 110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and
  never touches a real rate gate

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that
prose cannot represent with the same auditability. Fill every cell: an empty cell and a
cell where no throttle behavior applies look identical in a scan, and the distinction
matters. Produce sections in the order shown.

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x
or 5x nominal. The multi-volume STATUS columns exist because inertia lives at the volume
nobody tested — not the volume in the design document.)*

Complete Step 1 in full before opening any Step 2 section. Step 1 is the perspective-
separated enumeration phase: all tier discovery, numeric limits, and load-shape
classification happen here. Step 2 contains caller behavior and backpressure analysis only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** tiers discovered during Step 2
analysis are scope violations — evidence that the enumeration phase was incomplete, not
a routine fill-in opportunity. Return to TABLE A, register the tier with all columns
filled, then continue. This protocol is restated at each Step 2 section where mid-phase
discovery could occur.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
  The reason: synonyms make cross-section tracing unreliable — an auditor cannot verify
  a finding without resolving name equivalences.
- `Limit` — A number with a unit. The reason: a vague entry cannot anchor the numeric
  comparisons in LOAD SHAPE COMPARISON or determine STATUS transitions across bands.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — Lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer load-shape classification
  to the LOAD SHAPE COMPARISON section (Step 2G).

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold
  is crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears
  to be a pure volume-threshold analysis table — making load-shape classification (which
  compares arrival patterns, not volume levels) appear out of scope for the registry and
  naturally belonging in the section explicitly named "LOAD SHAPE COMPARISON." This frame
  routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating. Premise
  1: load-shape classification requires the registered `Limit` value present in TABLE A at
  registration time, because SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined by whether
  the Limit is expressed as a per-second window (burst and uniform saturate differently)
  or a per-minute bucket (total volume determines saturation). Premise 2: Step 2G (LOAD
  SHAPE COMPARISON) depends on per-tier Load-shape verdicts to identify which tiers change
  STATUS between uniform and burst — it cannot produce a meaningful numeric comparison
  without those verdicts already established. Consequence: deferring the verdict to Step
  2G creates a circular dependency. The comparison depends on the verdict; the verdict is
  deferred to the comparison. The escape route does not defer the work to a more
  appropriate location — it makes the work structurally impossible to complete correctly.

- `Failure visibility window` — How quickly saturation becomes observable (time + signal).
- `Recovery time` — How long until normal operation resumes after burst traffic subsides.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible in a development environment
where the connector layer is mocked.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers appearing
in backpressure analysis that are not in TABLE A are scope violations. Do not assign a
new T-NN here — return to TABLE A, register the tier with all required columns, then
continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

`Failure if Retry-After ignored` — name the escalation path precisely. Precision matters
because each failure mode has a different remediation.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has ever run at the volume where it fires.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers referenced
in burst path analysis that are not in TABLE A are scope violations. Return to TABLE A.

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence.

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear. One
sentence per tier with rationale. For the top-ranked tier, reference `Failure visibility
window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers introduced
during cascade trace that are not in TABLE A are scope violations. Return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, name
the failure mode precisely — the remediation for a retry storm (exponential backoff)
differs from the remediation for quota exhaustion (circuit breaker). If present, state
whether callers respect it correctly.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at
two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — State per-second arrival rate. State which tiers are HIT or SAT
  and why, referencing the Load-shape verdict and specific Limit value.
- **BURST arrival** — State the burst fraction and peak per-second rate. State which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs between patterns at identical total
count. Ground in a specific TABLE A Limit value and Load-shape verdict. If no tier changes
status, name the specific rate limit mechanism (per-minute bucket, per-second window,
sliding window, token bucket) as the structural reason.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Minimum two rows. One per gap from TABLE D, CASCADE, RETRY-AFTER, or LOAD SHAPE.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact config key, connector property, or API attribute.
Without a specific parameter, the row names a category and cannot be applied without
further research.

Calibration contrast:
> WRONG: "Add retry logic for throttle handling."
> PASS: "`connector.retryPolicy` on the SharePoint connector action — set
> `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
> `retryPolicy.maximumAttempts = 3`."

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer. The load test running at 10% of production concurrency. Their
architectural properties make specific throttle behaviors permanently unreachable.)*

Execute two stages in order. Stage 1 pre-loads artifact names that Stage 2's `Structural
reason` column requires — without Stage 1 complete, TABLE E entries default to category
labels.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2 opens.

Calibration contrast:
> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> PASS: "The integration test suite exercising connector calls via an HttpMessageHandler
> stub. Structural property: stub injects 429 responses; real rate gate is never invoked,
> so Retry-After timing is never produced and concurrent retry amplification is never
> observed."

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — GAP ENTRIES**

Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column calibration contrasts:
> `Throttle behavior` PASS: "Retry storm on T-02 connector limit when Retry-After header
> is absent; caller retries at full concurrency, exhausting tenant quota within 10 minutes."
>
> `Test approach` PASS: "Load test: 800 concurrent flow runs against a live connector in
> staging with tenant-level throttling enabled; assert 429 rate decrements to below 1%
> within 90 seconds."

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. Complete after Stage 2. Each downstream section receives an
individual verdict on a distinct verdict line, with evidence on a distinct evidence line.

**C-24 format requirement:** Each field entry must use two distinct labeled lines:
`- Verdict: [PASS / FAIL]` (the verdict, as a separate line)
`- If FAIL — [field label]: [list each finding]` (the evidence, as a separate line)
Each individual finding within a FAIL list must name all three identifiers: the informal
name used, the section and location, and the T-NN it should have been.
Example FAIL finding: `"T-02 referenced as 'the connector limit' at Step 2A Hop 2 — should have been T-02"`

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each as: "T-NN referenced as '[informal name]' at [step and location] — should have been [T-NN]"]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full identification schema]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full identification schema]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full identification schema]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full identification schema]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full identification schema]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each as: "[tier name] introduced at [step] — should have been registered in TABLE A as [T-NN]"]

**C-19 compliance — Failure 5 prevention (C-17, C-19) distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step before the
aggregate failure list. Format: `[step name]: [Y — reminder present / N — missing]`
followed by the aggregate on FAIL.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

**C-14 compliance — Perspective separation:**

- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

---

---

## V-02 — Single Axis: Output Format (Explicit Named-Template for C-24 Identification Schema)

**Axis:** Replace the example-based identification schema (`e.g., "T-02 referenced as
'the connector limit' at Hop 2"`) with an explicit named-template requirement in STEP 4.
The audit block header now states the required format as a named template with labeled
slots rather than an example: `SCHEMA: [INFORMAL-NAME] at [SECTION:LOCATION] identified
as [T-NN-FOUND]; correct identifier: [T-NN-CORRECT]`. All other structural elements
from R7 V-05 (including the dual-role opening) are preserved.

**Hypothesis:** The R7 V-05 approach relies on the model inferring the required format
from the example `"T-02 referenced as 'the connector limit' at Hop 2"`. Under output
pressure, the model may drop the example and produce only `"T-02 informal reference"`.
An explicit named-template with labeled slots is harder to compress: each slot is a
named requirement rather than an instance of a pattern. Primary risk: the rigid template
may produce mechanical-sounding entries that technically satisfy C-24 but lose the
analytical context that makes the finding useful.

**v7 predicted scoring:** C-24 PASS (explicit template enforces three-part schema),
C-25 PASS (per-item verdicts retained from R7 V-05), C-26 PASS (structural proof
retained). All 18 aspirational pass. Composite = 110.

---

**ROLE 1 — FLOW AUTHOR PRE-ANALYSIS**

You are a flow author who has received a post-incident report showing throttle-related
failures in a production Power Automate environment. Before the technical analysis, write
a UX impact statement of 5-7 sentences covering: what error codes or signals appeared in
run history, what retry behavior was observed (immediate retries, exponential backoff, or
silent drops), how the business process was affected (partial completions, queued work,
user-facing errors), and what the first observable symptom was. Write as plain prose —
no tables, no section headers. This statement establishes the user-visible context that
TABLE C will later quantify per tier.

---

**ROLE 2 — DOMAIN EXPERT ANALYSIS**

You are a Connectors / Power Automate throughput domain expert. Using the UX context
established above, simulate throughput across the rate-limited system described in the
signal. Treat the stated request volume as 1x nominal; also analyze at 2x and 5x.

The tables below are the primary output. Fill every cell. Produce sections in the order
shown.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite that reports green because it mocks the connector layer

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x
or 5x nominal.)*

Complete Step 1 in full before opening any Step 2 section. Step 1 is the perspective-
separated enumeration phase. Step 2 contains caller behavior and backpressure analysis only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** tiers discovered during Step 2
are scope violations. Return to TABLE A, register the tier, then continue. Restated at
each vulnerable Step 2 section.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... verbatim in every downstream section.
- `Limit` — a number with a unit.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition:**
  Complete this column now. Do not defer to Step 2G.

  **Escape-route story (C-23):** The "STATUS tracks volume thresholds" frame makes the
  `Load-shape verdict` column appear to belong in LOAD SHAPE COMPARISON (Step 2G), not
  the registry. This frame is the inertia route.

  **Structural rejection proof (C-26):** Premise 1: Load-shape classification requires
  the registered `Limit` value (present in TABLE A) to determine per-second vs. per-minute
  enforcement. Premise 2: Step 2G depends on `Load-shape verdict` to identify which tiers
  change STATUS between uniform and burst. Consequence: deferring the verdict to Step 2G
  creates a circular dependency — the comparison depends on the verdict and the verdict
  is deferred to the comparison. Classify now.

- `Failure visibility window` — time before saturation becomes observable.
- `Recovery time` — time until normal operation resumes.

---

**STEP 2 — ANALYSIS PHASES**

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** new tiers here
are scope violations. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism`: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

*(Cross-reference the Role 1 pre-analysis to populate error codes and retry behavior.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** new tiers here
are scope violations. Return to TABLE A.

| Path-ID | Entry component | Gap reason (missing protection, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|----------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. One sentence per tier.
For the top-ranked tier, reference `Failure visibility window` and `Recovery time`.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** new tiers here
are scope violations. Return to TABLE A.

One concrete cascade from the 1x binding constraint. T-IDs throughout. Minimum three
tiers with explicit causal links.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: Retry-After present and surfaced? If absent, name the
failure mode precisely.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** new tiers here
are scope violations. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdicts, compare 1x nominal at two arrival
patterns. Identical total count; only distribution differs.

- **UNIFORM arrival** — State per-second rate. State tier statuses referencing Load-shape verdict.
- **BURST arrival** — State fraction and peak per-second rate. State tier statuses.

At least one numeric comparison where status differs. Ground in TABLE A Limit + Load-shape
verdict. If no tier changes status, name the rate limit mechanism.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact parameter. No category labels.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**STAGE 1** — Gate: two artifacts named.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2** — TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**

**C-24 IDENTIFICATION SCHEMA:** For every FAIL finding in this block, use the following
named template — fill every slot:

```
SCHEMA: [INFORMAL-NAME used] at [SECTION:LOCATION] — should have been [T-NN]
```

- `INFORMAL-NAME`: the component name, phrase, or synonym that appeared instead of the T-NN
- `SECTION:LOCATION`: the step name and specific sub-location (e.g., "Step 2A:Hop 2",
  "Step 2E:causal link 1")
- `T-NN`: the correct TABLE A identifier that should have been used

Every FAIL finding must use this three-slot schema. A finding that lists only a T-NN
without the informal name or location fails C-24.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using SCHEMA above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using SCHEMA above]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using SCHEMA above]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using SCHEMA above]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using SCHEMA above]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using SCHEMA above]

Unregistered tiers:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each using SCHEMA above with T-NN slot = "new tier — not in TABLE A"]

---

**C-19 compliance — distributed reminder audit:**

**C-25 format:** Issue an individual verdict per step inline, then aggregate any failures.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

**C-14 compliance:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe step and location]

---

---

## V-03 — Single Axis: Phrasing Register (Explanatory/WHY-First for Enforcement Blocks)

**Axis:** Replace imperative/prohibition-first enforcement language with an
explanatory/WHY-first register throughout. "Do not defer X to Y" becomes "X must happen
here because Y depends on it — deferring X to Y creates a dependency loop that prevents
Y from executing correctly." The structural proof (C-26) is presented as a labeled
logical argument (Premise 1, Premise 2, Consequence) rather than an embedded paragraph.
The audit block retains the R7 V-05 two-line format and per-item verdicts. The dual-role
opening is retained.

**Hypothesis:** The imperative register works through prohibition. The explanatory
register works through purpose — making the structural reason visible at the point of
use. For C-26 specifically, presenting the proof as a labeled argument (P1, P2, C) may
be more reliable than embedding it in a prohibition paragraph, because the model can
reconstruct the argument structure even if the surrounding text is compressed. If the
model understands WHY the circular dependency makes deferral self-defeating, it is less
likely to compress the proof into a one-sentence summary under output pressure. Primary
risk: explanatory text adds ~150 tokens to TABLE A column definitions.

**v7 predicted scoring:** all 18 aspirational pass including C-24 PASS, C-25 PASS,
C-26 PASS (structural proof now labeled as P1/P2/C making it harder to compress).
Composite = 110.

---

**ROLE 1 — FLOW AUTHOR PRE-ANALYSIS**

You are a flow author who has received a post-incident report showing throttle-related
failures in a production Power Automate environment. Before the technical analysis, write
a UX impact statement of 5-7 sentences covering: what error codes or signals appeared in
run history, what retry behavior was observed, how the business process was affected, and
what the first observable symptom was. Plain prose only. This loads the user-visible
context that TABLE C will quantify per tier.

---

**ROLE 2 — DOMAIN EXPERT ANALYSIS**

You are a Connectors / Power Automate throughput domain expert. Using the UX context
above, simulate throughput across the rate-limited system. Treat the stated request
volume as 1x nominal; also analyze at 2x and 5x. Produce sections in order. Fill every
cell.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. What inertia conceals:
- The burst path never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second window into a 10-minute retry storm
- The cascade that takes down three dependent flows from a single connector limit
- The tier nobody measured at 5x nominal
- The green test suite that mocks the connector layer

---

**STEP 1 — TIER REGISTRY**

Why Step 1 comes first: all tier discovery, numeric limits, and load-shape classification
must be complete before caller behavior analysis begins. When tier discovery and caller
analysis are interleaved (Step 1 and Step 2 mixed), two problems arise: (1) the registry
is incomplete when caller analysis begins, producing unresolvable forward references;
(2) caller observations create anchoring bias that changes which tiers are included in
the registry. The step boundary prevents both problems.

**REGISTRY GAP protocol — why returning is required:** When Step 2 analysis reveals a
tier that is not in TABLE A, the correct response is to return to Step 1 and complete the
registry before continuing. The reason: assigning a T-NN mid-analysis and proceeding
treats the gap as a fill-in step, but the gap is evidence that the enumeration phase was
incomplete — meaning other tiers may also be missing. Completing the registry before
continuing ensures completeness.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use these verbatim downstream. The reason: downstream
  synonyms prevent cross-section verification because an auditor cannot trace a finding
  without resolving name equivalences.
- `Limit` — a number with a unit. The reason: a vague entry prevents the LOAD SHAPE
  COMPARISON from grounding its numeric comparison and blocks STATUS determination.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands to show that
  the multi-volume analysis is producing new information.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential.

  **Why this column must be filled here (C-16, C-20, C-23, C-26):**

  The temptation is to defer load-shape classification to LOAD SHAPE COMPARISON (Step 2G).
  This temptation has a specific structural source: TABLE A STATUS columns use
  OK/HIT/SAT to track volume-threshold crossings, making TABLE A appear to be a
  volume-threshold analysis table. A volume-threshold table should not contain arrival-
  pattern analysis — that belongs in the section explicitly named for load-shape
  comparison. This is the "STATUS tracks volume thresholds" inertia frame.

  **The proof that deferral fails (C-26):**

  Premise 1 — Load-shape classification depends on the `Limit` value registered in this
  table. SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined by whether the Limit is
  expressed as a per-second window (burst and uniform traffic saturate differently because
  the burst arrives faster than the window allows) or a per-minute bucket (total volume
  determines saturation regardless of arrival timing). The `Limit` value that enables this
  determination is present in TABLE A now, at registration time.

  Premise 2 — LOAD SHAPE COMPARISON (Step 2G) depends on `Load-shape verdict` values
  to identify which tiers change STATUS between uniform and burst arrival. Without
  pre-established per-tier verdicts, Step 2G cannot determine which tiers need a numeric
  comparison — it would need to re-derive the classification, defeating the purpose of
  having a registry.

  Consequence — Deferring the verdict to Step 2G creates a circular dependency: Step 2G
  depends on the verdict, and the verdict is deferred until Step 2G runs. The inertia
  frame routes shape analysis to the wrong location. Classify the `Load-shape verdict`
  using the `Limit` value registered in this row, now.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible where the connector is mocked.)*

Why the reminder matters: tiers that appear in backpressure analysis but are not in
TABLE A indicate that the enumeration phase was incomplete. The correct response is to
return to TABLE A and complete the registry before continuing, not to assign a new T-NN
mid-analysis.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` — use a specific class: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade. The reason: a specific mechanism
explains the causal path; a generic term does not enable remediation.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

*(Cross-reference the Role 1 pre-analysis for error codes and retry behavior per tier.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

`Failure if Retry-After ignored` — name the escalation path precisely. The reason:
different failure modes have different remediations — "retry storm" leads to exponential
backoff; "quota exhaustion" leads to circuit breaker.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has run at the volume where it fires.)*

Why the reminder matters: tiers referenced in burst path analysis but not in TABLE A
indicate incomplete enumeration. Return to TABLE A.

| Path-ID | Entry component | Gap reason (missing protection, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|----------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear —
an absent tier has unknown risk. One sentence per tier with rationale. For the top-ranked
tier, reference `Failure visibility window` and `Recovery time` from TABLE A to quantify
the exposure and recovery cost.

---

**Step 2E — CASCADE SCENARIO**

Why the reminder matters: tiers introduced during cascade trace that are not in TABLE A
indicate incomplete enumeration. Return to TABLE A.

One concrete cascade from the 1x binding constraint. Use T-IDs throughout. State each
causal link explicitly. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced to the caller?
If absent, name the failure mode precisely — the remediation depends on the failure mode.
If present, state whether callers honor it correctly and what evidence exists.

---

**Step 2G — LOAD SHAPE COMPARISON**

Why the reminder matters: tiers introduced during load shape analysis that are not in
TABLE A indicate incomplete enumeration. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdicts, compare 1x nominal at two arrival
patterns. Identical total count; only arrival distribution differs. The reason for the
comparison: per-minute limits and per-second limits respond differently to burst arrivals
— a system safe at uniform arrival may saturate under burst at the same total volume.

- **UNIFORM arrival** — State per-second arrival rate. State tier statuses with Load-shape
  verdict reference.
- **BURST arrival** — State burst fraction and peak per-second rate. State tier statuses.

At least one numeric comparison where status differs. Ground in TABLE A Limit + Load-shape
verdict. If no tier changes status, name the rate limit mechanism as structural reason —
this absence is itself a finding.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Why specific parameters matter: a mitigation row that names a category of action ("add
retry logic") cannot be applied without further research. A row that names the exact
parameter (`connector.retryPolicy`, `retryPolicy.type = ExponentialBackoff`) can be
applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Why Stage 1 comes before Stage 2: Stage 1 establishes the artifact names and structural
properties that Stage 2's `Structural reason` column requires. Without Stage 1 complete,
TABLE E entries default to category labels rather than artifact-grounded explanations,
which cannot be verified.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY** (Gate: two artifacts named)

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — GAP ENTRIES**

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

---

**STEP 4 — INTEGRITY VERIFICATION**

Why this block exists: the per-section compliance audit ensures that the structural
properties (tier-ID threading, perspective separation, scope-violation reminders) that
the analysis depends on were actually maintained throughout. A prose summary cannot
verify these properties — only an enumerated per-section check can.

**C-24 format:** Verdict and evidence on distinct labeled lines. Each finding uses the
full identification schema: informal name used + section and location + T-NN. Example:
`"T-02 referenced as 'the connector limit' at Step 2A Hop 2 — should have been T-02"`

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with informal name + location + T-NN]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with informal name + location + T-NN]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with informal name + location + T-NN]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with informal name + location + T-NN]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with informal name + location + T-NN]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with informal name + location + T-NN]

Unregistered tiers:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: tier name + section of introduction]

**C-19 compliance — distributed reminder audit:**

Why per-item verdicts (C-25): a single aggregate verdict ("all reminders present") cannot
identify which specific step was missing. Per-item verdicts enable targeted correction.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

**C-14 compliance:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe step and location]

---

---

## V-04 — Combined: Role Sequence + Phrasing Register (Single Role + Explanatory)

**Axis:** Combine V-01 (single role, no pre-analysis) with V-03 (explanatory/WHY-first
register for enforcement blocks). The INERTIA PROBLEM block provides UX context priming
in place of the pre-analysis. All enforcement blocks use the explanatory register.
The structural proof (C-26) is labeled as P1/P2/Consequence. The audit block uses the
R7 V-05 two-line format and C-25 per-item verdicts.

**Hypothesis:** V-01 saves ~150 tokens by removing the pre-analysis. V-03 adds ~150
tokens through explanatory context on enforcement blocks. Combined, they are roughly
token-neutral while providing both (1) clear structural purpose explanations for each
enforcement block and (2) a labeled proof structure for C-26 that is hard to compress.
The trade-off: the pre-analysis loads UX vocabulary for TABLE C, but the INERTIA PROBLEM
block covers the same domain territory at lower cost. Primary risk: TABLE C UX entries
may be shallower than V-03 without the pre-analysis loading retry behavior vocabulary.

**v7 predicted scoring:** all 18 aspirational pass. Composite = 110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. What inertia conceals:
- The burst path never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler turning a 30-second window into a 10-minute retry storm
- The cascade taking down three dependent flows from a single connector limit
- The tier nobody measured at 5x nominal
- The green test suite that mocks the connector layer and never hits a real rate gate

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system. Treat the stated request volume as 1x nominal; also analyze at
2x and 5x. Fill every cell. Produce sections in order.

---

**STEP 1 — TIER REGISTRY**

Why Step 1 must be complete before Step 2: all tier discovery, numeric limits, and
load-shape classification happen here. Step 2 analysis depends on a complete registry —
an incomplete registry causes Step 2 to reference undefined tiers, making findings
unverifiable. When a tier is discovered during Step 2, the correct response is to return
to Step 1 and complete the registry, then continue Step 2 from the point of discovery.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use verbatim downstream. Synonyms prevent verification.
- `Limit` — a number with a unit. Vague entries block numeric comparison and STATUS
  determination.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — lowest band where this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential.

  **Why this column must be filled here (C-16, C-20, C-23, C-26):**

  The temptation to defer: TABLE A STATUS columns track volume-threshold crossings, so
  TABLE A appears to be a volume-threshold table. Load-shape classification (arrival
  pattern analysis) appears to belong in "LOAD SHAPE COMPARISON" — the section named for
  it. This is the inertia frame that routes classification to Step 2G.

  **Proof that deferral is self-defeating:**

  P1 — Load-shape classification requires the `Limit` value in this table. SHAPE-NEUTRAL
  vs. SHAPE-SENSITIVE is determined by whether the Limit uses a per-second window (where
  arrival timing matters) or a per-minute bucket (where only total volume matters). The
  `Limit` needed to make this determination is registered here, now.

  P2 — Step 2G (LOAD SHAPE COMPARISON) depends on `Load-shape verdict` values to
  identify which tiers change STATUS between uniform and burst. It cannot execute its
  numeric comparison without those verdicts pre-established.

  C — Deferring `Load-shape verdict` to Step 2G creates a circular dependency: Step 2G
  needs the verdict; the verdict is deferred to Step 2G. The inertia frame sends the work
  to a location that cannot complete it. Fill this column now.

- `Failure visibility window` — time before saturation becomes observable.
- `Recovery time` — time until normal operation resumes.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

Why the reminder: tiers appearing here that are not in TABLE A indicate incomplete
enumeration. The correct response is to return to Step 1, not to assign a new T-NN.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` — specific class: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

Why the reminder: tiers here not in TABLE A indicate incomplete enumeration. Return to
Step 1.

| Path-ID | Entry component | Gap reason (missing protection, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|----------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. One sentence per tier. For
the top-ranked tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

Why the reminder: new tiers in cascade trace indicate incomplete enumeration. Return to
Step 1.

One concrete cascade from 1x binding constraint. T-IDs throughout. Minimum three tiers
with explicit causal links.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: Retry-After present and surfaced? Name the failure
mode precisely if absent.

---

**Step 2G — LOAD SHAPE COMPARISON**

Why the reminder: new tiers here indicate incomplete enumeration. Return to Step 1.

Using TABLE A's Limit values and Load-shape verdicts, compare 1x nominal at two arrival
patterns. Identical total count; only distribution differs.

- **UNIFORM arrival** — state per-second rate and tier statuses.
- **BURST arrival** — state burst fraction, peak per-second rate, and tier statuses.

At least one numeric comparison where status differs. If no tier changes status, name the
rate limit mechanism.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Why specific parameters: a category-level action cannot be applied without research. An
exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Why Stage 1 precedes Stage 2: Stage 2's `Structural reason` column requires artifact
names and architectural properties. Stage 1 establishes these before Stage 2 opens.

**STAGE 1** (Gate: two artifacts named)

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — TABLE E**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

---

**STEP 4 — INTEGRITY VERIFICATION**

Why this block exists: structural properties (tier threading, perspective separation,
reminder placement) cannot be verified by a prose summary — only by an enumerated
per-section check. This block provides that check.

**C-24 format:** Two distinct labeled lines per field entry — verdict line and evidence
line. Each FAIL finding names all three identifiers: informal name used, section and
location, T-NN.

**C-13 compliance:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each: "informal name" at section:location — should have been T-NN]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Unregistered tiers:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: tier name + section]

**C-19 compliance — Why per-item (C-25):** an aggregate verdict cannot identify which
specific step was missing. Per-item verdicts enable targeted correction.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

**C-14 compliance:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe step and location]

---

---

## V-05 — Maximum Density: All Three Axes (Single Role + Explicit Template + Explanatory)

**Axis:** Combine all three R7 v7 axes: V-01 (single role, no pre-analysis) + V-02
(explicit named-template for C-24 identification schema) + V-03 (explanatory/WHY-first
register). The structural proof (C-26) appears as a labeled P1/P2/C argument. The audit
block uses the explicit C-24 template from V-02. The C-19 compliance field uses per-item
verdicts (C-25) as in R7 V-05. The INERTIA PROBLEM block replaces the pre-analysis.

**Hypothesis:** The three axes target different reliability risks for C-24, C-25, C-26
simultaneously:
- **V-01 (single role)** reduces token cost, freeing output budget for full audit block
  completion
- **V-02 (explicit template)** makes the C-24 identification schema a named structural
  requirement rather than an example to be inferred
- **V-03 (explanatory register)** makes the C-26 structural proof a labeled P1/P2/C
  argument that is hard to compress to a one-sentence summary

Combined, V-05 should produce the most reliable C-24/25/26 output of any variation.
Primary risk: the explicit template (V-02) combined with the explanatory register (V-03)
may produce verbose enforcement blocks that compress downstream table cells.

**v7 predicted scoring:** C-24 PASS (explicit template + example in STEP 4), C-25 PASS
(per-item inline verdicts in C-19 check), C-26 PASS (labeled P1/P2/C proof). All 18
aspirational pass. Composite = 110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite that reports green because it mocks the connector layer

The analysis below finds these before production does. Three volume bands — 1x, 2x, 5x —
because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that
prose cannot represent with the same auditability. Fill every cell. Produce sections in
the order shown.

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x
or 5x nominal. The multi-volume STATUS columns exist because inertia lives at the volume
nobody tested.)*

Why Step 1 must be complete before Step 2: tier discovery, numeric limits, and load-shape
classification all happen here. Step 2 depends on a closed registry. A tier discovered
during Step 2 indicates incomplete enumeration — the correct response is to return to
Step 1 and close the registry, then continue, not to assign a T-NN mid-analysis.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream section. Synonyms prevent
  cross-section verification.
- `Limit` — a number with a unit. A vague entry prevents numeric comparison and STATUS
  determination.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Why this column must be filled here — deferral prohibition with escape-route and proof
  (C-16, C-20, C-23, C-26):**

  **The inertia frame (C-23):** TABLE A STATUS columns track volume-threshold crossings
  (OK/HIT/SAT). Because STATUS is a volume-threshold metric, TABLE A appears to be a
  pure volume-threshold analysis table. Load-shape classification (arrival pattern
  analysis) appears to belong in "LOAD SHAPE COMPARISON" — the section explicitly named
  for it. This "STATUS tracks volume thresholds" frame is the escape route that routes
  `Load-shape verdict` classification to Step 2G.

  **The structural proof (C-26):**

  P1 — Load-shape classification requires the `Limit` value registered in this row.
  SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined by whether the Limit is expressed as
  a per-second window (burst arrival saturates the window faster than uniform arrival at
  the same total volume) or a per-minute bucket (total volume determines saturation
  regardless of arrival timing). The `Limit` that enables this determination is present
  in TABLE A now.

  P2 — Step 2G (LOAD SHAPE COMPARISON) depends on `Load-shape verdict` values to
  identify which tiers change STATUS between uniform and burst arrival and to ground its
  numeric comparison. Without those per-tier verdicts pre-established, Step 2G cannot
  determine which tiers require numeric comparison.

  C — Deferring `Load-shape verdict` to Step 2G creates a circular dependency: Step 2G
  needs the verdict; the verdict is deferred to Step 2G. The inertia frame routes the work
  to a section that cannot complete it. Fill this column using the `Limit` value in this
  row, now.

- `Failure visibility window` — time before saturation becomes observable (time + signal).
- `Recovery time` — time until normal operation resumes after burst traffic subsides.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler turning a 30-second window
into a 10-minute retry storm — invisible where the connector is mocked.)*

Why the reminder: tiers appearing in backpressure analysis that are not in TABLE A
indicate incomplete enumeration. Return to Step 1, register the tier, then continue.
Do not assign a new T-NN here.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` — specific class: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade. The reason: a specific mechanism
identifies the causal path; a generic verb does not.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

`Failure if Retry-After ignored` — name the escalation path precisely. Different failure
modes have different remediations.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has run at the volume where it fires.)*

Why the reminder: tiers here not in TABLE A indicate incomplete enumeration. Return to
Step 1.

At least one row. If no unprotected path exists, row 1 states the conclusion with two
named controls as evidence.

| Path-ID | Entry component | Gap reason (missing protection, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|----------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear. One
sentence per tier. For the top-ranked tier, reference `Failure visibility window` and
`Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

Why the reminder: new tiers in cascade trace indicate incomplete enumeration. Return to
Step 1.

One concrete cascade from the 1x binding constraint. T-IDs throughout. Minimum three
tiers with explicit causal links, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: Retry-After present and surfaced? If absent, name
the failure mode precisely — the remediation depends on the failure mode.

---

**Step 2G — LOAD SHAPE COMPARISON**

Why the reminder: new tiers here indicate incomplete enumeration. Return to Step 1.

Using TABLE A's Limit values and Load-shape verdicts, compare 1x nominal at two arrival
patterns. Identical total count; only distribution differs.

- **UNIFORM arrival** — state per-second rate and tier statuses referencing Load-shape
  verdict and Limit value.
- **BURST arrival** — state burst fraction, peak per-second rate, and tier statuses.

At least one numeric comparison where status differs at identical total count. Ground in
TABLE A Limit + Load-shape verdict. If no tier changes status, name the rate limit
mechanism — this null finding requires the mechanism explanation to be distinguishable
from an incomplete analysis.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Why exact parameters: a category-level action cannot be applied without research. An
exact parameter (`connector.retryPolicy` with sub-keys and values) can be applied
immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer; the load test running at 10% of production concurrency.)*

Why Stage 1 precedes Stage 2: Stage 2's `Structural reason` column requires artifact names
and architectural properties. Stage 1 establishes these before Stage 2 opens — without
Stage 1 complete, TABLE E entries default to category labels that cannot be verified.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY** (Gate: two artifacts)

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — GAP ENTRIES**

Produce TABLE E. Fill every cell. Minimum two rows. Reference Stage 1 artifacts in
`Structural reason`.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column calibration:
> `Throttle behavior` PASS: "Retry storm on T-02 connector limit when Retry-After header
> is absent; caller retries at full concurrency, exhausting tenant quota within 10 minutes."
>
> `Test approach` PASS: "Load test: 800 concurrent flow runs against a live connector in
> staging with tenant-level throttling enabled; assert 429 rate decrements to below 1%
> within 90 seconds after burst window closes."

---

**STEP 4 — INTEGRITY VERIFICATION**

Why this block exists: structural properties cannot be verified by prose summary — only
by enumerated per-section check. This block makes the verification explicit and
traceable.

**C-24 IDENTIFICATION SCHEMA (explicit named template):**

Every FAIL finding in this block must use the following three-slot schema:

```
[INFORMAL-NAME] at [SECTION:LOCATION] — should have been [T-NN]
```

Slots:
- `[INFORMAL-NAME]`: the exact phrase used instead of the T-NN (e.g., "the connector limit",
  "SharePoint tier", "primary bottleneck")
- `[SECTION:LOCATION]`: the step name and sub-location (e.g., "Step 2A:Hop 2",
  "Step 2E:causal link between tier 1 and tier 2")
- `[T-NN]`: the correct TABLE A identifier that should have appeared

A finding that omits any slot fails C-24.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using three-slot schema above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using three-slot schema above]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using three-slot schema above]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using three-slot schema above]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using three-slot schema above]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using three-slot schema above]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers: [list each: tier name at section:location — not in TABLE A]

---

**C-19 compliance — distributed reminder audit:**

Why per-item verdicts matter (C-25): a single aggregate PASS/FAIL cannot identify which
specific step was missing a reminder. Per-item verdicts enable targeted correction. Issue
an individual verdict for each step inline, then aggregate any failures.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

---

**C-14 compliance — Perspective separation:**

- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe the step and the specific location where tier
  discovery and caller behavior analysis were mixed]
