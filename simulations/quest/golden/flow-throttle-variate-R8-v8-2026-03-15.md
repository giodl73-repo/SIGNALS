# flow-throttle Variate — Round 8 (v8 Rubric)
**Date:** 2026-03-15
**Rubric:** v8 (C-01 through C-27, N_essential=5, N_recommended=3, N_aspirational=19)
**Baseline ceiling:** R7 V-05 (110/110 under v7 rubric; confirmed passes C-01 through C-26)

---

## State Analysis: What R7 V-05 Has vs. What R8 Must Add

**R7 V-05 coverage under v8 (confirmed):**
- C-01 through C-22: all pass (verified through R7)
- C-23: passes — escape-route story names "STATUS tracks volume thresholds" as the inertia
  frame that routes shape analysis to Step 2G; structural rejection proof present
- C-24: passes — STEP 4 audit block uses two-line `- Verdict:` / `- If FAIL —` format;
  each FAIL finding names informal name + section/location + T-NN (three identifiers)
- C-25: passes — per-item `[Y — reminder present / N — missing]` verdicts issued for each
  step before aggregate failure list in C-19 compliance field
- C-26: passes — structural rejection proof contains the circular-dependency argument
  (Premise 1: load-shape classification requires Limit value in TABLE A; Premise 2: Step 2G
  depends on per-tier Load-shape verdicts; Consequence: deferring verdict to Step 2G creates
  a circular dependency — the comparison depends on the verdict, the verdict is deferred to
  the comparison)

**C-27 failure in R7 V-05:**

R7 V-05 uses the following format in STEP 4 for the C-24 schema requirement:

> **C-24 format:** Verdict and evidence on distinct labeled lines. Each finding uses the
> full identification schema: informal name used + section and location + T-NN. Example:
> `"T-02 referenced as 'the connector limit' at Step 2A Hop 2 — should have been T-02"`

This states the requirement positively — "name all three identifiers" — and supplies an
example. It does not include an explicit inline failure condition: "A finding that lists
only a T-NN without the informal name or location fails C-24." The definition specifies
what compliance looks like but not what non-compliance looks like. Under C-27, a schema
definition that relies on inference from the positive case alone (i.e., "comply by
including X; therefore non-compliance = absence of X") fails because the enforcement
boundary is implicit, not stated. The failure condition must be co-located with the
schema definition, not derivable from it.

R7 V-02 came closest: its named SCHEMA template included "A finding that lists only a
T-NN without the informal name or location fails C-24" as a standalone sentence at the
end of the schema definition block — co-located, explicit, and in failure-condition form.
V-02 implicitly satisfies C-27. R8 must make this property explicit and test its
presentation variants.

---

## Round 8 Variation Map

| Variation | Axes | C-27 | Predicted composite |
|-----------|------|------|---------------------|
| V-01 | Output format: positive-only schema, no failure condition (C-27 isolation FAIL) | FAIL | 109/110 |
| V-02 | Output format: SCHEMA template + explicit failure condition (C-27 isolation PASS) | PASS | 110/110 |
| V-03 | Phrasing register: WHY-first with embedded failure condition (single role) | PASS | 110/110 |
| V-04 | Role sequence + output format: single role + SCHEMA + failure condition | PASS | 110/110 |
| V-05 | All three axes: single role + WHY-first + failure condition extended to TABLE F column | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs V-02): Is C-27 the only difference between positive-only and SCHEMA-with-
failure-condition presentations? Hypothesis: the positive-only form fails C-27 cleanly;
all other criteria are unaffected because the three-identifier structure is still present.

Q2 (V-02 vs V-03): Does WHY-first framing for the failure condition satisfy C-27 as
reliably as declarative failure-condition form? Hypothesis: yes, provided the failure
condition is co-located and unambiguous — C-27 requires co-location and explicitness,
not a specific register.

Q3 (V-04): Does removing the dual-role opening affect C-27 compliance when the schema
format is explicit? Hypothesis: no — C-27 is a schema-definition property, not a role
property. V-04 should score 110 with single role + explicit failure condition.

---

## V-01 — Single Axis: Output Format (C-27 FAIL: positive-only schema, no failure condition)

**Axis:** STEP 4's C-24 format requirement states the three-identifier requirement
positively with an example, but does not include an explicit inline failure condition.
Role: single role (no dual-role pre-analysis). All other elements from R7 V-05 are
preserved intact: INERTIA PROBLEM preamble, REGISTRY GAP protocol with failure-mode
labels, escape-route story, structural rejection proof (P1/P2/Consequence), distributed
enforcement reminders, C-25 per-item verdicts in the C-19 compliance check, C-14 and
C-15 audit fields.

**Hypothesis:** V-01 is the clean C-27 isolation failure. The three-identifier
requirement is present; the finding-level failure condition is absent. The model receives
a correct-form requirement with a correct-form example. Under C-27, this is insufficient:
the definition specifies compliance but not non-compliance. A model following this
instruction knows what a correct finding looks like but has not been told when a finding
fails — making the enforcement boundary implicit. All other criteria should pass at the
same level as R7 V-05.

**v8 predicted scoring:** C-27 FAIL (schema definition has no failure condition). C-24
through C-26 pass. All other aspirationals pass. Composite = 109/110.

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

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time, because SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined
  by whether the Limit is expressed as a per-second window (burst and uniform saturate
  differently) or a per-minute bucket (total volume determines saturation). Premise 2:
  Step 2G (LOAD SHAPE COMPARISON) depends on per-tier Load-shape verdicts to identify
  which tiers change STATUS between uniform and burst — it cannot produce a meaningful
  numeric comparison without those verdicts already established. Consequence: deferring
  the verdict to Step 2G creates a circular dependency. The comparison depends on the
  verdict; the verdict is deferred to the comparison. The escape route does not defer the
  work to a more appropriate location — it makes the work structurally impossible to
  complete correctly.

- `Failure visibility window` — How quickly saturation becomes observable (time + signal).
- `Recovery time` — How long until normal operation resumes after burst traffic subsides.

*(Do not begin STEP 2 until TABLE A is complete with all columns filled.)*

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
- If FAIL — informal references found: [list each with full three-identifier schema]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full three-identifier schema]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full three-identifier schema]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full three-identifier schema]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full three-identifier schema]

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

## V-02 — Single Axis: Output Format (C-27 PASS: SCHEMA template with inline failure condition)

**Axis:** STEP 4's C-24 schema definition is replaced with an explicit named-template
that includes a co-located compliance failure condition — "A finding that lists only a
T-NN without the INFORMAL-NAME or SECTION:LOCATION fails C-24." The failure condition
is stated as a standalone sentence immediately after the slot definitions, co-located
with the schema and not deferred to the audit block or a preamble. Role: dual role
(ROLE 1 flow author pre-analysis + ROLE 2 domain expert). All other elements from R7
V-05 are preserved: INERTIA PROBLEM, REGISTRY GAP protocol with failure-mode labels,
escape-route story, structural rejection proof, distributed enforcement reminders, C-25
per-item verdicts.

**Hypothesis:** The named-template approach forces three-slot compliance: each slot is a
named requirement that must be filled rather than inferred from an example. The inline
failure condition satisfies C-27 by making the enforcement boundary explicit at the
definition site. A model that sees "A finding that lists only a T-NN without INFORMAL-NAME
or SECTION:LOCATION fails C-24" cannot claim compliance by omission — the failure
condition is named at the point the schema is defined. Primary risk: the template may
produce mechanical-sounding entries that satisfy C-24 structurally but lose analytical
depth. The dual-role opening primes TABLE C UX entries with retry behavior vocabulary,
mitigating depth loss in the error-code and failure-consequence columns.

**v8 predicted scoring:** C-27 PASS (failure condition co-located with schema definition).
All other aspirationals pass. Composite = 110/110.

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
are scope violations. Return to TABLE A, register the tier with all columns filled, then
continue. Restated at each vulnerable Step 2 section.

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

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now. Do not defer load-shape classification to Step 2G.

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold
  is crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears
  to be a pure volume-threshold analysis table — making load-shape classification appear
  out of scope for the registry and naturally belonging in LOAD SHAPE COMPARISON. This
  frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** Premise 1: load-shape classification requires
  the registered `Limit` value in TABLE A at registration time — SHAPE-NEUTRAL vs.
  SHAPE-SENSITIVE is determined by whether the Limit is a per-second window (burst and
  uniform saturate differently) or a per-minute bucket (total volume determines
  saturation). Premise 2: Step 2G depends on per-tier Load-shape verdicts to identify
  which tiers change STATUS between uniform and burst. Consequence: deferring the verdict
  to Step 2G creates a circular dependency — the comparison depends on the verdict, the
  verdict is deferred to the comparison.

- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

*(Do not begin STEP 2 until TABLE A is complete.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(Cross-reference the Role 1 pre-analysis for retry behavior and error signal context.)*

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

For the 1x binding constraint tier: Retry-After present and surfaced? If absent, name
the failure mode precisely.

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

**C-24 IDENTIFICATION SCHEMA:** For every FAIL finding in this block, fill all three slots
of the following named template:

```
SCHEMA: [INFORMAL-NAME used] at [SECTION:LOCATION] — should have been [T-NN]
```

- `INFORMAL-NAME` — the component name, phrase, or synonym that appeared instead of the T-NN
- `SECTION:LOCATION` — the step name and specific sub-location (e.g., "Step 2A:Hop 2",
  "Step 2E:causal link 1", "Step 2D:tier 3 ranking entry")
- `T-NN` — the correct TABLE A identifier that should have been used

Compliance failure condition (C-27): A finding that lists only a T-NN without the
INFORMAL-NAME or SECTION:LOCATION fails C-24. All three slots are required; no slot
may be omitted or merged.

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
- If FAIL — unregistered tiers: [list each using SCHEMA with T-NN slot = "unregistered — not in TABLE A"]

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

## V-03 — Single Axis: Phrasing Register (C-27 PASS: WHY-first failure condition, single role)

**Axis:** STEP 4's C-24 schema definition uses a WHY-first explanatory register to
embed the failure condition — the enforcement boundary is stated as the logical consequence
of the purpose statement, not as a prohibition appended to the requirement. Role: single
role (no dual-role pre-analysis). All other elements from R7 V-05 are preserved.

**Hypothesis:** WHY-first framing satisfies C-27 provided the failure condition is
co-located and unambiguous. The register differs from V-02 (declarative failure condition)
but the logical content is the same: a finding that omits INFORMAL-NAME or SECTION:LOCATION
fails C-24. C-27 does not specify a register — it requires that the failure condition be
"explicit" and "co-located." If WHY-first framing makes the failure condition equally
explicit through the consequence chain ("the audit block cannot do its job — therefore
the finding fails C-24"), C-27 is satisfied. Primary risk: the WHY-first form is more
verbose; under output pressure, a model may compress the consequence into the premise
and drop the failure condition. Testing whether WHY-first survives token pressure is the
purpose of this variation.

**v8 predicted scoring:** C-27 PASS (failure condition is present and co-located, in WHY-
first form). All other aspirationals pass. Composite = 110/110.

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

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Fill every cell. Produce sections in the order shown.

---

**STEP 1 — TIER REGISTRY**

Why Step 1 is complete before Step 2: all tier discovery, numeric limits, and load-shape
classification must be established before caller behavior analysis begins. When tier
discovery and caller analysis are interleaved, the registry is incomplete when caller
analysis begins — producing unresolvable forward references and anchoring bias in which
tiers get included. The step boundary prevents both problems.

**REGISTRY GAP protocol — why returning is required (Failure 5 prevention, C-17):** When
Step 2 analysis reveals a tier not in TABLE A, the correct response is to return to Step 1
and complete the registry. The reason: assigning a T-NN mid-analysis treats the gap as a
fill-in step, but a gap during Step 2 is evidence that the enumeration phase was incomplete
— meaning other tiers may also be missing. Restated at each Step 2 section where mid-phase
discovery could occur.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use these verbatim downstream. The reason: downstream synonyms
  prevent cross-section verification because an auditor cannot trace a finding without
  resolving name equivalences.
- `Limit` — a number with a unit. The reason: a vague entry prevents the LOAD SHAPE
  COMPARISON from grounding its numeric comparison and blocks STATUS determination.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Why this column must be filled here — Failure 2 + Failure 6 prevention (C-16, C-20,
  C-23, C-26):**

  The temptation is to defer load-shape classification to LOAD SHAPE COMPARISON (Step 2G).
  This temptation has a specific structural source: TABLE A STATUS columns track volume-
  threshold crossings using OK/HIT/SAT, making TABLE A appear to be a volume-threshold
  analysis table. A volume-threshold table should not contain arrival-pattern analysis —
  that appears to belong in LOAD SHAPE COMPARISON. This is the "STATUS tracks volume
  thresholds" inertia frame (C-23).

  **The proof that deferral fails (C-26):**

  Premise 1 — Load-shape classification requires the `Limit` value registered in this table.
  SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined by whether the Limit is a per-second window
  (burst and uniform saturate differently) or a per-minute bucket (total volume determines
  saturation). The `Limit` value needed for this determination is present in TABLE A now.

  Premise 2 — LOAD SHAPE COMPARISON (Step 2G) depends on per-tier `Load-shape verdicts` to
  identify which tiers change STATUS between uniform and burst. Without pre-established verdicts,
  Step 2G cannot determine which tiers require a numeric comparison.

  Consequence — Deferring the verdict to Step 2G creates a circular dependency: Step 2G
  depends on the verdict, and the verdict is deferred to Step 2G. Classify the `Load-shape
  verdict` using the `Limit` value in this row, now.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes.

*(Do not begin STEP 2 until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible where the connector is mocked.)*

Why the reminder matters (Failure 5 prevention, C-17, C-19): a tier appearing in
backpressure analysis that is not in TABLE A is evidence that the enumeration phase was
incomplete. The correct response is to return to TABLE A and complete the registry before
continuing — not to assign a new T-NN mid-analysis.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` — specific class: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

`Failure if Retry-After ignored` — name the escalation path precisely. Different failure
modes have different remediations; a generic label cannot be actioned.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has run at the volume where it fires.)*

Why the reminder matters (Failure 5 prevention, C-17, C-19): tiers referenced in burst
path analysis but not in TABLE A indicate incomplete enumeration. Return to TABLE A.

| Path-ID | Entry component | Gap reason (missing protection, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|----------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear —
an absent tier has unknown risk. One sentence per tier with rationale. For the top-ranked
tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

Why the reminder matters (Failure 5 prevention, C-17, C-19): tiers introduced during
cascade trace that are not in TABLE A indicate incomplete enumeration. Return to TABLE A.

One concrete cascade from the 1x binding constraint. Use T-IDs throughout. State each
causal link explicitly. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, name
the failure mode precisely — different failure modes require different remediations.

---

**Step 2G — LOAD SHAPE COMPARISON**

Why the reminder matters (Failure 5 prevention, C-17, C-19): tiers introduced during
load shape analysis that are not in TABLE A indicate incomplete enumeration. Return to
TABLE A.

Using TABLE A's Limit values and Load-shape verdicts, compare 1x nominal at two arrival
patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — State per-second arrival rate. State tier statuses referencing
  Load-shape verdict.
- **BURST arrival** — State the burst fraction and peak per-second rate. State tier statuses.

At least one numeric comparison where status differs. Ground in TABLE A Limit + Load-shape
verdict. If no tier changes status, name the specific rate limit mechanism as structural
reason — this absence is itself a finding.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Why specific parameters matter: a mitigation row that names a category of action cannot be
applied without further research. A row that names the exact parameter can be applied
immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Why Stage 1 comes before Stage 2: Stage 1 establishes the artifact names and structural
properties that Stage 2's `Structural reason` column requires. Without Stage 1, TABLE E
entries default to category labels rather than artifact-grounded explanations.

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

Why this block exists (Failure 4 prevention, C-15, C-18, C-22, C-24, C-25): the per-
section compliance audit ensures that the structural properties the analysis depends on —
tier-ID threading, perspective separation, scope-violation reminders — were actually
maintained throughout. Prose closure cannot verify these properties; only an enumerated
per-section check can.

**C-24 IDENTIFICATION SCHEMA:** The purpose of the three-part identification schema is to
front-load the discovery work. An audit finding that names only a T-NN requires a reviewer
to locate the section and identify the informal name used — that is the discovery work
this block exists to do; a finding that stops at the T-NN leaves the work undone.

Required format for every FAIL finding:

```
SCHEMA: [INFORMAL-NAME used] at [SECTION:LOCATION] — should have been [T-NN]
```

- `INFORMAL-NAME` — the phrase that appeared instead of the T-NN
- `SECTION:LOCATION` — step name and sub-location (e.g., "Step 2A:Hop 2")
- `T-NN` — the correct TABLE A identifier

Enforcement boundary (C-27): A finding that names only a T-NN — even the correct one —
fails C-24, because INFORMAL-NAME and SECTION:LOCATION are absent and the discovery work
is not done. The schema is not satisfied by the T-NN alone.

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
- If FAIL — unregistered tiers: [list each using SCHEMA with T-NN slot = "unregistered"]

---

**C-19 compliance — distributed reminder audit:**

Why per-item verdicts (C-25): a single aggregate verdict cannot identify which specific
step was missing; per-item verdicts enable targeted correction.

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

## V-04 — Combined: Role Sequence + Output Format (single role + SCHEMA + failure condition)

**Axes:** (1) Role sequence: single role only, no dual-role pre-analysis. (2) Output
format: SCHEMA named template with inline failure condition (V-02's C-27 treatment).
All enforcement blocks use the same imperative register as V-01. Tests whether the
role sequence axis interacts with C-27 compliance when the schema format is explicit.

**Hypothesis:** C-27 is a schema-definition property, not a role property. The single-
role opening saves ~150 tokens over the dual-role opening, but the C-24 schema definition
in STEP 4 is unchanged from V-02. If C-27 compliance depends solely on the schema
definition (and not on role setup or UX vocabulary loading), V-04 should score 110/110
with single role. The test determines whether the dual-role opening in V-02 is load-
bearing for C-27 or incidental. Primary risk: same as V-01 — TABLE C UX entries may be
shallower without the pre-analysis loading retry behavior vocabulary.

**v8 predicted scoring:** C-27 PASS (failure condition co-located with schema definition).
All other aspirationals pass. Composite = 110/110.

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
  day one
- The integration test suite that reports green because it mocks the connector layer and
  never touches a real rate gate

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

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
or 5x nominal.)*

Complete Step 1 in full before opening any Step 2 section. Step 1 is the perspective-
separated enumeration phase: all tier discovery, numeric limits, and load-shape
classification happen here. Step 2 contains caller behavior and backpressure analysis only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** tiers discovered during Step 2
analysis are scope violations — evidence that the enumeration phase was incomplete. Return
to TABLE A, register the tier with all columns filled, then continue. Restated at each
Step 2 section where mid-phase discovery could occur.

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

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer load-shape classification
  to the LOAD SHAPE COMPARISON section (Step 2G).

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track volume-threshold crossings. Because
  STATUS is a volume-threshold metric, TABLE A appears to be a pure volume-threshold analysis
  table — making load-shape classification appear out of scope for the registry and naturally
  belonging in LOAD SHAPE COMPARISON. This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** Premise 1: load-shape classification requires
  the registered `Limit` value in TABLE A at registration time — SHAPE-NEUTRAL vs.
  SHAPE-SENSITIVE is determined by whether the Limit is a per-second window or a per-minute
  bucket. Premise 2: Step 2G depends on per-tier Load-shape verdicts to identify which
  tiers change STATUS between uniform and burst. Consequence: deferring the verdict to
  Step 2G creates a circular dependency — the comparison depends on the verdict, the verdict
  is deferred to the comparison.

- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

*(Do not begin STEP 2 until TABLE A is complete.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers appearing
in backpressure analysis that are not in TABLE A are scope violations. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism`: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers referenced
in burst path analysis that are not in TABLE A are scope violations. Return to TABLE A.

| Path-ID | Entry component | Gap reason (missing protection, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|----------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear. One
sentence per tier with rationale. For the top-ranked tier, reference `Failure visibility
window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers introduced
during cascade trace that are not in TABLE A are scope violations. Return to TABLE A.

One concrete cascade from the 1x binding constraint. T-IDs throughout. Minimum three
tiers with explicit causal links.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: Retry-After present and surfaced? If absent, name
the failure mode precisely.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

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

**STAGE 1** — Gate: two artifacts named before Stage 2 opens.

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

**C-24 IDENTIFICATION SCHEMA:** For every FAIL finding in this block, fill all three slots
of the following named template:

```
SCHEMA: [INFORMAL-NAME used] at [SECTION:LOCATION] — should have been [T-NN]
```

- `INFORMAL-NAME` — the component name, phrase, or synonym that appeared instead of the T-NN
- `SECTION:LOCATION` — step name and specific sub-location (e.g., "Step 2A:Hop 2",
  "Step 2E:causal link 2", "Step 2D:tier 1 entry")
- `T-NN` — the correct TABLE A identifier that should have been used

Compliance failure condition (C-27): A finding that lists only a T-NN without the
INFORMAL-NAME or SECTION:LOCATION fails C-24. All three slots are required; no slot
may be omitted or merged.

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
- If FAIL — unregistered tiers: [list each using SCHEMA with T-NN = "unregistered — not in TABLE A"]

---

**C-19 compliance — distributed reminder audit:**

**C-25 format:** Individual inline verdict per step, then aggregate on FAIL.

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

## V-05 — All Three Axes: Single role + WHY-first + failure condition at schema AND TABLE F column

**Axes:** (1) Role sequence: single role, no pre-analysis. (2) Phrasing register:
WHY-first throughout enforcement blocks, including the REGISTRY GAP protocol and
distributed reminders. (3) Output format: C-27 applied at two definition sites — the
C-24 identification schema in STEP 4 (primary C-27 target), AND the TABLE F `Setting or
API parameter` column definition in Step 2H (extending C-27 to a second format
requirement). All other elements from R7 V-05 are preserved.

**Hypothesis:** V-05 tests maximum C-27 density. By extending the failure-condition
pattern to TABLE F's column definition, V-05 explores whether C-27's principle generalizes
across definition sites within a single prompt, or whether it is strictly limited to the
C-24 identification schema. If the TABLE F extension produces a cleaner `Setting or API
parameter` column in practice (fewer category labels, more specific parameters), it
demonstrates that co-located failure conditions improve precision beyond the C-24 audit
context. Primary risk: WHY-first throughout adds ~200 tokens over V-01's imperative form;
combined with single role (no pre-analysis savings), total token count may approach V-05's
output ceiling.

**v8 predicted scoring:** C-27 PASS (two co-located failure conditions: one at SCHEMA
definition, one at TABLE F column definition). All other aspirationals pass.
Composite = 110/110.

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
  day one
- The integration test suite that reports green because it mocks the connector layer and
  never touches a real rate gate

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Fill every cell. Produce sections in the order shown.

---

**STEP 1 — TIER REGISTRY**

Why Step 1 must be complete before Step 2: all tier discovery, numeric limits, and
load-shape classification happen here. When tier discovery and caller analysis are
interleaved, two structural failures occur — the registry is incomplete when caller
analysis begins (producing unresolvable forward references), and caller observations
create anchoring bias in which tiers get included. Step 1 completion prevents both.

**REGISTRY GAP protocol — why returning is required (Failure 5 prevention, C-17):** When
Step 2 reveals a tier not in TABLE A, the correct response is to return to Step 1 and
complete the registry before continuing. The reason: a gap during Step 2 is evidence that
the enumeration phase was incomplete — other tiers may also be missing. Treating the gap
as a fill-in step and assigning a T-NN mid-analysis masks this incompleteness. This
protocol is restated at each Step 2 section where mid-phase discovery is structurally
possible.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use verbatim downstream. The reason: downstream synonyms
  prevent cross-section verification because an auditor cannot trace a finding without
  resolving name equivalences.
- `Limit` — a number with a unit. The reason: a vague entry prevents the LOAD SHAPE
  COMPARISON from grounding its numeric comparison and blocks STATUS determination across
  volume bands.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands to demonstrate
  that the multi-volume analysis produces new information.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Why this column must be filled here — Failure 2 + Failure 6 prevention (C-16, C-20,
  C-23, C-26):**

  The temptation is to defer load-shape classification to LOAD SHAPE COMPARISON (Step 2G).
  This temptation has a specific structural source — the "STATUS tracks volume thresholds"
  inertia frame (C-23): TABLE A STATUS columns track volume-threshold crossings using
  OK/HIT/SAT. Because STATUS is a volume-threshold metric, TABLE A appears to be a
  volume-threshold table — making arrival-pattern analysis appear out of scope and
  naturally belonging in the section explicitly named for load-shape comparison.

  **The proof that deferral fails (C-26):**

  Premise 1 — Load-shape classification requires the `Limit` value registered in this
  table. SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined by whether the Limit is a
  per-second window (burst and uniform saturate differently because the burst exceeds the
  per-second capacity) or a per-minute bucket (total volume determines saturation
  regardless of arrival timing). The `Limit` value enabling this determination is present
  in TABLE A at registration time.

  Premise 2 — LOAD SHAPE COMPARISON (Step 2G) depends on `Load-shape verdict` values
  to identify which tiers change STATUS between uniform and burst. Without pre-established
  per-tier verdicts, Step 2G cannot determine which tiers require a numeric comparison.

  Consequence — Deferring the verdict to Step 2G creates a circular dependency: Step 2G
  depends on the verdict; the verdict is deferred to Step 2G. The inertia frame routes
  shape analysis to a location where the analysis cannot be completed. Classify the
  `Load-shape verdict` using the `Limit` value in this row, now.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes.

*(Do not begin STEP 2 until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible where the connector layer is
mocked.)*

Why the reminder matters (Failure 5 prevention, C-17, C-19): a tier appearing in
backpressure analysis that is not in TABLE A is evidence that the enumeration phase was
incomplete. Returning to TABLE A and completing the registry before continuing ensures
that the incompleteness is surfaced — assigning a T-NN mid-analysis conceals it.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` — specific class: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade. The reason: a specific mechanism
names the causal path; a generic term cannot anchor a remediation.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted — an omitted tier's UX
consequence is unknown, which is different from "no UX consequence."

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

`Failure if Retry-After ignored` — name the escalation path precisely. The reason:
different failure modes require different remediations — a retry storm leads to exponential
backoff; quota exhaustion leads to a circuit breaker; a generic label enables neither.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has run at the volume where it fires.)*

Why the reminder matters (Failure 5 prevention, C-17, C-19): tiers referenced in burst
path analysis but not in TABLE A indicate incomplete enumeration. Returning to TABLE A
ensures completeness; assigning a new T-NN here masks the gap.

| Path-ID | Entry component | Gap reason (missing protection, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|----------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear — an
absent tier has unknown risk, which is not the same as low risk. One sentence per tier
with rationale. For the top-ranked tier, reference `Failure visibility window` and
`Recovery time` from TABLE A to quantify the exposure and recovery cost.

---

**Step 2E — CASCADE SCENARIO**

Why the reminder matters (Failure 5 prevention, C-17, C-19): tiers introduced during
cascade trace that are not in TABLE A indicate incomplete enumeration. Return to TABLE A
before continuing — new tiers discovered here mean the registry was not complete.

One concrete cascade from the 1x binding constraint. Use T-IDs throughout. State each
causal link explicitly. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced to the caller?
If absent, name the failure mode precisely — the remediation depends on the failure mode
and generic descriptions cannot be applied.

---

**Step 2G — LOAD SHAPE COMPARISON**

Why the reminder matters (Failure 5 prevention, C-17, C-19): tiers introduced during
load shape analysis that are not in TABLE A indicate incomplete enumeration. Return to
TABLE A before continuing.

Using TABLE A's Limit values and Load-shape verdicts, compare 1x nominal at two arrival
patterns. Identical total count; only arrival distribution differs. The reason for the
comparison: per-minute limits and per-second limits respond differently to burst arrivals
— a system safe at uniform arrival may saturate under burst at the same total volume.

- **UNIFORM arrival** — State per-second arrival rate. State tier statuses referencing
  Load-shape verdict and Limit.
- **BURST arrival** — State burst fraction and peak per-second rate. State tier statuses.

At least one numeric comparison where status differs. Ground in TABLE A Limit + Load-shape
verdict. If no tier changes status, name the specific rate limit mechanism — this absence
is itself a finding that validates the Load-shape verdicts.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Why specific parameters matter: a mitigation row that names a category of action ("add
retry logic") requires further research before it can be applied. A row that names the
exact configuration key (`connector.retryPolicy`) or API attribute can be applied
immediately. The difference is operational — one produces a task, the other produces
a change.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name. Compliance failure condition (C-27 extension): A row that names a category
of action rather than a specific parameter identifier fails this column's precision
requirement. "Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Why Stage 1 comes before Stage 2: Stage 1 establishes the artifact names and structural
properties that Stage 2's `Structural reason` column requires. Without Stage 1, TABLE E
entries default to category labels ("integration tests don't cover throttle behavior")
rather than artifact-grounded structural explanations that can be verified and actioned.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY** (Gate: two artifacts named before Stage 2)

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

Why this block exists (Failure 4 prevention, C-15, C-18, C-22, C-24, C-25): the
per-section compliance audit ensures that the structural properties the analysis depends
on — tier-ID threading, perspective separation, scope-violation reminders — were actually
maintained throughout. A prose summary cannot verify these properties; only an enumerated
per-section check that produces individual verdicts can detect which specific section
failed and where.

**C-24 IDENTIFICATION SCHEMA:** The purpose of the three-part identification schema is to
front-load the discovery work at the finding level. An audit finding that names only a
T-NN shifts the discovery burden to the reviewer — they must locate the section and
identify the informal name used. The schema makes that work visible at the point of the
finding, where it can be immediately actioned.

Required format for every FAIL finding:

```
SCHEMA: [INFORMAL-NAME used] at [SECTION:LOCATION] — should have been [T-NN]
```

- `INFORMAL-NAME` — the component name, phrase, or synonym that appeared instead of the T-NN
- `SECTION:LOCATION` — step name and specific sub-location (e.g., "Step 2A:Hop 2",
  "Step 2E:causal link 1", "Step 2D:tier 2 ranking sentence")
- `T-NN` — the correct TABLE A identifier that should have been used

Compliance failure condition (C-27): A finding that names only a T-NN — even the correct
one — fails C-24, because INFORMAL-NAME and SECTION:LOCATION are absent and the discovery
work is not done. The schema is not satisfied by the T-NN alone; no slot may be omitted
or merged.

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
- If FAIL — unregistered tiers: [list each using SCHEMA with T-NN slot = "unregistered"]

---

**C-19 compliance — distributed reminder audit:**

Why per-item verdicts matter (C-25): a single aggregate verdict ("all reminders present")
cannot identify which specific step was missing. Individual inline verdicts enable targeted
correction — if Step 2E shows N, the gap is at the cascade section, not elsewhere.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

**C-14 compliance:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe step and location where tier discovery and caller
  behavior appeared in the same phase]
