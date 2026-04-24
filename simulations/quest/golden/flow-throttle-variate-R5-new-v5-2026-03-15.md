# flow-throttle Variate — Round 5 (New v5 Rubric)
**Date:** 2026-03-15
**Rubric:** v5 new (C-01 through C-14; N_essential=5, N_recommended=3, N_aspirational=6)
**Baseline:** Old R5 V-05 (carried from R4 V-05) re-scored under new v5 rubric

---

## Round 5 State Analysis: Old R5 V-05 Re-Scored Under New v5

**Confirmed carry-forward:**
- C-01 through C-08: Essential and recommended criteria pass reliably. Multi-volume TABLE A
  (1x/2x/5x) enforces C-01 and C-03. TABLE B with mechanism vocabulary enforces C-02. TABLE C
  per-tier enforces C-04. TABLE D with specific gap reason enforces C-05. RETRY-AFTER GAP
  ASSESSMENT for the first-hit tier enforces C-06. CASCADE SCENARIO with 3+ tiers enforces C-07.
  TIER RISK RANKING enforces C-08.
- C-09: Passes when TABLE F includes a `Setting or API parameter` column that explicitly rejects
  generic phrases. Present in old R5 V-03 through V-05.
- C-10: Passes when LOAD SHAPE COMPARISON includes UNIFORM vs. BURST at fixed 1x volume with
  numeric arrival rates and at least one TABLE A tier showing status change. Present in old R5
  V-02 through V-05.

**New v5 tighter formulations — re-scored under new v5:**

C-11 (worked throttle arithmetic): Old variations placed a THROTTLE ARITHMETIC EXAMPLE somewhere
in the prompt — sometimes before TABLE A, sometimes adjacent to it. The NEW v5 C-11 adds a
positional constraint: the arithmetic chain must PRECEDE the first trace table. An arithmetic
block that appears after TABLE A setup begins, or that is embedded inside a TABLE A row as a
`Binding at band` cell calculation, fails the anchor requirement even if the derivation is
correct. The "Complete before TABLE A" instruction must be explicit. PARTIAL PASS in old variations.

C-12 (explicit tier enumeration prefix): Old variations had an ordered tier list with 1-to-1
mapping language. The NEW v5 C-12 requires TWO elements that old prompts lacked: (1) "canonical
registry" language declaring TABLE A the authoritative source and that the prefix list is its
prerequisite, and (2) an explicit forward link stating "complete before TABLE A." An enumerated
list without the canonical-registry declaration allows TABLE A rows to silently extend the tier
set. Without the prerequisite forward link, the prefix can be written after TABLE A is partially
filled. PARTIAL PASS in old variations.

C-13 (mechanism-typed propagation hops): Old variations constrained TABLE B's `Mechanism`
column with one-word labels: queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. The new C-13 exposes the vocabulary-contract gap: when the column definition
accepts one-word forms and the criterion requires multi-clause event chains, a producer satisfies
the column without satisfying the criterion. "Queue-fill" passes the column check but does not
name the trigger event, the system response, or the propagation mechanism — it names the outcome
category. The column definition must itself require multi-clause forms so that one-word shortcuts
fail at the cell level, not just at the post-hoc audit level. PARTIAL PASS in old variations.

C-14 (Retry-After present vs. surfaced): Old R5 V-04 and V-05 had TABLE C with two columns
("Retry-After emitted? (Y/N)" and "Honored by caller? (Y/N)") and RETRY-AFTER GAP ASSESSMENT
named both dimensions. This matches the new C-14 requirement. PASS in old R5 V-04 and V-05.
FAIL in V-01, V-02, V-03 (single Retry-After present? column only).

**Re-scoring old R5 V-05 under new v5:**

| Criterion | Old v5 result | New v5 result | Reason |
|-----------|--------------|---------------|--------|
| C-01 through C-08 | PASS | PASS | Carry forward |
| C-09 | PASS | PASS | TABLE F with setting-level column |
| C-10 | PASS | PASS | LOAD SHAPE with numeric comparison |
| C-11 | PASS (old) | PARTIAL | Positional constraint not explicitly enforced |
| C-12 | PASS (old) | PARTIAL | Missing "canonical registry" + prerequisite forward link language |
| C-13 | PASS (old) | PARTIAL | One-word mechanism vocabulary; multi-clause contract absent |
| C-14 | PASS (old) | PASS | Split columns present in V-04, V-05 |

**Old R5 V-05 under new v5:** 4/6 aspirational.
`composite = 60 + 30 + (4/6 × 10) = 96.67 → 96`

**Round 5 purpose:** Close C-11 positional, C-12 canonical-registry, C-13 vocabulary-contract
coherence. Single-axis variations isolate each. V-04 combines the three. V-05 adds C-14
reinforcement at maximum inertia-framing density.

**Variation map:**

| Variation | Axis | Criteria targeted | Predicted composite |
|-----------|------|------------------|---------------------|
| V-01 | Lifecycle emphasis: arithmetic anchor as prerequisite lifecycle gate before TABLE A | C-11 | ~98 |
| V-02 | Output format: canonical registry declaration with explicit forward link before TABLE A | C-12 | ~98 |
| V-03 | Phrasing register: multi-clause vocabulary contract in TABLE B column definition | C-13 | ~98 |
| V-04 | Combined: lifecycle + format + phrasing register | C-11 + C-12 + C-13 | ~100 |
| V-05 | Maximum density: V-04 + inertia framing for C-14 present/surfaced distinction | all 6 aspirational | ~100 |

---

## V-01 — Single Axis: C-11 Arithmetic Anchor as Lifecycle Gate

**Axis:** Lifecycle emphasis — the arithmetic derivation is placed as an explicit lifecycle
prerequisite step before TABLE A, with a "complete before TABLE A" gate instruction and a
model calculation format. No canonical registry language (C-12 not targeted). No multi-clause
mechanism vocabulary (C-13 not targeted). Single Retry-After column (C-14 not targeted).

**Hypothesis:** C-11 requires a complete arithmetic chain — limit / distribution factor =
per-unit capacity; demand per unit; derived overage or headroom as percentage or absolute number
— AND it requires this chain to precede the first trace table. Embedding arithmetic inside a
TABLE A cell (e.g., in the `Binding at band` column) or placing an arithmetic example after
TABLE A setup has begun fails the positional constraint even if the derivation is correct. The
lifecycle gate — "complete before TABLE A" as a named phase-opening instruction — is the
structural surface that enforces position. The model cannot begin TABLE A until the anchor
section is marked complete. Primary risk: the model fills the anchor with limit and volume but
stops before the derived overage/headroom, satisfying the format but failing the derivation
requirement.

**New v5 scoring:** passes C-09, C-10, C-11, C-14 (inherited from baseline) = 4/6 aspirational.
Does not pass C-12 or C-13. `composite = 60 + 30 + (4/6 × 10) = 96.67 → 96`

Wait — C-14 is present in baseline V-05 but this is a single-axis variation so it may not
have the split columns. Conservatively: C-09 + C-10 + C-11 = 3/6 aspirational if C-14 absent.
`composite = 60 + 30 + (3/6 × 10) = 95` Single-axis baseline; combined will close the gap.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the sections below in order. Do not substitute prose for
any table. Every cell must be filled.

---

**THROTTLE ARITHMETIC ANCHOR**

*(Complete this section before beginning TABLE A. Do not proceed to TABLE A until the
arithmetic chain is fully derived.)*

State the complete arithmetic chain for the primary throttle constraint:

Format:
- System limit: [number + unit, e.g. 600 req/min]
- Distribution factor: [flows, connections, or tenants sharing the limit, with count]
- Per-unit capacity: [system limit / distribution factor = result with unit]
- Demand per unit at 1x nominal: [request rate per unit at the stated volume]
- Derived overage or headroom: [difference as absolute number AND percentage]

Example: "System limit: 600 req/min connector limit. Distribution factor: 12 concurrent flows.
Per-unit capacity: 600 / 12 = 50 req/min per flow. Demand per unit at 1x: 75 req/min per flow.
Derived overage: 75 - 50 = 25 req/min per flow over limit — 50% over capacity at 1x nominal."

Stating limit and demand volume without the derived overage or headroom percentage fails this
anchor. The arithmetic chain must be derivable from the numbers stated here before TABLE A rows
are populated.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete after THROTTLE ARITHMETIC ANCHOR. Use T-NN identifiers in all downstream sections.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent identifier. Every downstream section uses these
  verbatim; no synonyms, no component-name substitutions.
- `Limit` — a number with a unit. Vague entries (e.g., "limited," "throttled") invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier becomes the primary bottleneck. N/A if never.
- `Failure visibility window` — elapsed time before saturation becomes observable to the operator.
- `Recovery time` — elapsed time until normal operation resumes after the throttle clears.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must name a specific class: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade. Generic verbs ("propagates," "cascades," "also throttled")
do not satisfy this column even if the correct tiers are named.

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

*(At least one row. If no unprotected path exists, row 1 states the conclusion with at least
two named controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (missing protection or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|--------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                              |                   |                             |

---

**TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale tied to failure impact and recovery cost. For the top-ranked tier, explicitly
reference its `Failure visibility window` and `Recovery time` values from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting from the 1x binding constraint tier. Use Tier-IDs
throughout. State each causal link explicitly. Minimum three tiers. Generic claims
("could cascade," "would affect downstream") do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: state whether Retry-After handling is present in the
calling code. If absent, name the precise failure mode. If present, state whether callers
honor it correctly and what evidence exists for each conclusion.

---

**LOAD SHAPE COMPARISON**

Using TABLE A rate limit values, compare 1x nominal volume under two arrival patterns.
Total request count is identical in both patterns; only arrival distribution differs.

- **UNIFORM arrival** — requests distributed evenly across the measurement window. State
  as: [volume] over [window] = [N req/sec or req/min]. Name which TABLE A tiers are HIT or
  SAT and why.
- **BURST arrival** — same total requests concentrated in a fraction of the window (state
  the fraction). State as: [volume] in first [fraction] = [N req/sec peak]. Name which
  TABLE A tiers are HIT or SAT and why.

Required: at least one numeric comparison showing a TABLE A tier that is OK under UNIFORM
but HIT or SAT under BURST at the identical total count. Ground the comparison in a specific
TABLE A limit value (e.g., "T-02's 20 req/sec limit is not exceeded at 10 req/sec uniform
but is exceeded at 60 req/sec burst, even though both deliver 600 req/min total").

If no tier changes status between patterns, state why — citing the specific rate limit
mechanism (per-minute bucket, per-second window, sliding window, token bucket) as the
structural reason arrival shape does not affect behavior at the stated volume.

---

**TABLE F — MITIGATION PRESCRIPTIONS**

*(At least two rows. One row per identified gap: unprotected burst path, missing or
unhandled Retry-After, cascade risk source.)*

| Gap-ID | Throttle behavior (Tier-ID + failure mode) | Setting or API parameter | Recommended value or pattern | Expected outcome |
|--------|-------------------------------------------|--------------------------|------------------------------|-----------------|
| M-01   |                                           |                          |                              |                 |
| M-02   |                                           |                          |                              |                 |

Column definitions:
- `Throttle behavior` — Tier-ID from TABLE A + specific failure mode. Generic entries fail.
- `Setting or API parameter` — the exact setting name, API parameter, or configuration key
  that addresses this gap. "Add retry logic" does not satisfy this column. "Set
  `x-ms-ratelimit-remaining-subscription-reads` threshold in connector policy" satisfies it.
- `Recommended value or pattern` — numeric value, pattern name, or specific implementation
  instruction. "Adjust as needed" does not satisfy this column.
- `Expected outcome` — measurable change in throttle behavior when the prescription is applied.

---

## V-02 — Single Axis: C-12 Canonical Registry + Prerequisite Forward Link

**Axis:** Output format — a TIER REGISTRY block appears before TABLE A, explicitly declares
itself the canonical tier registry, and states as a prerequisite that it must be complete
before TABLE A begins. No arithmetic anchor before TABLE A (C-11 not targeted). No multi-clause
mechanism vocabulary (C-13 not targeted). Single Retry-After column (C-14 not targeted).

**Hypothesis:** C-12 requires two specific elements that an ordinary tier list lacks:
(1) "canonical registry" language declaring the list authoritative — without this, TABLE A can
silently introduce new tiers and downstream sections reference them without violating the rubric;
(2) an explicit prerequisite forward link — without this, the prefix can be written after TABLE A
population begins (backfilling), which satisfies the format but defeats the pre-commitment
purpose. The output-format axis is the correct lever: making the registry a named structural
output (with declared authority over TABLE A) enforces both elements at the prompt level. Primary
risk: the model produces the tier list but writes "TABLE A is below" rather than "canonical
registry" language, and the prerequisite instruction is acknowledged but not treated as a hard
gate.

**New v5 scoring:** passes C-09, C-10, C-12 = 3/6 aspirational.
`composite = 60 + 30 + (3/6 × 10) = 95`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the sections below in order. Do not substitute prose for
any table. Every cell must be filled.

---

**TIER REGISTRY — CANONICAL SOURCE OF TRUTH**

*(This is the canonical tier registry. Complete before proceeding to TABLE A.)*

Enumerate every throttle tier in the system. This list is the authoritative source — no tier
may appear in TABLE A, TABLE B, TABLE C, TABLE D, the cascade scenario, or any other downstream
section unless it is declared here first. Any tier referenced downstream but absent from this
registry is a structural violation.

| Registry-ID | Component | Limit type (rate, concurrency, quota) |
|-------------|-----------|--------------------------------------|
| T-01        |           |                                      |
| T-02        |           |                                      |
| ...         |           |                                      |

*Prerequisite: This registry must be complete and every tier identified before TABLE A begins.
TABLE A populates numeric limits and volume-band status for the tiers declared here — it does
not introduce new tiers.*

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete after TIER REGISTRY. Use only Tier-IDs declared in the registry above.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — must match a Registry-ID from TIER REGISTRY above. No new identifiers introduced here.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — elapsed time before saturation becomes observable.
- `Recovery time` — elapsed time until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must name a specific class: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade. Generic verbs do not satisfy this column.

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

*(At least one row. If no unprotected path exists, row 1 states the conclusion with at least
two named controls as evidence.)*

| Path-ID | Entry component | Gap reason (missing protection or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|--------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                              |                   |                             |

---

**TIER RISK RANKING**

Rank all TIER REGISTRY tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference `Failure visibility window` and `Recovery time`
from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting from the 1x binding constraint. Use Tier-IDs from TIER
REGISTRY throughout. State each causal link. Minimum three tiers. Generic cascade claims do
not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: state whether Retry-After handling is present in the
calling code. If absent, name the precise failure mode. If present, state whether callers
honor it correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A rate limit values, compare 1x nominal volume under two arrival patterns.
Total request count is identical; only arrival distribution differs.

- **UNIFORM arrival** — requests distributed evenly. State as: [volume] over [window] =
  [N req/sec or req/min]. Name TABLE A tiers that are HIT or SAT and why.
- **BURST arrival** — same total requests concentrated in a fraction of the window (state
  the fraction). Name TABLE A tiers that are HIT or SAT and why.

Required: at least one numeric comparison showing a TABLE A tier OK under UNIFORM but HIT
or SAT under BURST at identical total count.

If no tier changes status between patterns, state why — citing the specific rate limit
mechanism as the structural reason.

---

**TABLE F — MITIGATION PRESCRIPTIONS**

*(At least two rows.)*

| Gap-ID | Throttle behavior (Tier-ID + failure mode) | Setting or API parameter | Recommended value or pattern | Expected outcome |
|--------|-------------------------------------------|--------------------------|------------------------------|-----------------|
| M-01   |                                           |                          |                              |                 |
| M-02   |                                           |                          |                              |                 |

Column definitions:
- `Setting or API parameter` — the exact setting name or API parameter. "Add retry logic"
  does not satisfy this column.
- `Recommended value or pattern` — numeric value or specific implementation instruction.
- `Expected outcome` — measurable change when the prescription is applied.

---

## V-03 — Single Axis: C-13 Vocabulary Contract Coherence in TABLE B

**Axis:** Phrasing register — TABLE B's `Mechanism class` column definition moves from
one-word technical shorthand (queue-fill, connection-hold) to multi-clause event-chain forms
(trigger event; system response; propagation effect). The column definition itself becomes the
vocabulary contract: a cell that does not contain all three clause-elements fails the column,
not a separate post-hoc audit. No arithmetic anchor (C-11 not targeted). No canonical registry
(C-12 not targeted). Single Retry-After column (C-14 not targeted).

**Hypothesis:** C-13 fails in old variations because the TABLE B column definition accepts
one-word labels. A one-word label names the outcome category ("queue-fill") but omits the
trigger event that caused it and the propagation mechanism that follows from it — the two
elements that make mechanism tracing useful for diagnosis. When the column definition specifies
one-word forms, the model produces one-word forms. When the column definition specifies
multi-clause event chains in the exact pass-condition form ("429 returned; no Retry-After
handler; immediate retry issued within same throttle window"), the phrasing register of the
instruction shapes the phrasing register of the output. A vocabulary gate checklist separate
from the column achieves weaker coherence — the model can pass the checklist by reformulating
after the fact. Primary risk: multi-clause form instruction increases TABLE B token cost and
the model compresses the cascade scenario to compensate.

**New v5 scoring:** passes C-09, C-10, C-13 = 3/6 aspirational.
`composite = 60 + 30 + (3/6 × 10) = 95`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the sections below in order. Do not substitute prose for
any table. Every cell must be filled.

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
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Failure visibility window` — elapsed time before saturation becomes observable.
- `Recovery time` — elapsed time until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism class | Observable effect |
|-----|---------------|--------------|-----------------|-------------------|
| 1   |               |              |                 |                   |
| 2   |               |              |                 |                   |
| ... |               |              |                 |                   |

`Mechanism class` — each cell must contain a complete three-clause event chain:
[trigger event]; [system response]; [downstream propagation]. Acceptable forms:

- "429 returned; no Retry-After handler; immediate retry issued within same throttle window"
- "concurrency cap reached; runtime queues trigger invocations; backlog accumulates at PA
  runtime layer"
- "queue fills; overflow requests dropped; upstream sees 503 and retries compound inbound load"
- "connection limit reached; new requests queued at gateway; queue depth grows until timeout
  fires"
- "tenant quota exhausted; all flows sharing quota receive 429; backoff timers unsynchronized
  across flows producing compounding re-entry"

One-word labels (queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade) do not satisfy this column even if the correct mechanism category is named.
The full three-clause chain is required. Phrases like "it propagates," "also throttled," or
"cascade occurs" fail even if the correct tier is named.

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

*(At least one row. If no unprotected path exists, state conclusion with at least two named
controls as evidence.)*

| Path-ID | Entry component | Gap reason (missing protection or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|--------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                  |                   |                             |

---

**TIER RISK RANKING**

Rank all TABLE A tiers by business risk. One sentence per tier. For the top-ranked tier,
reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting from the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link explicitly. Minimum three tiers.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: state whether Retry-After handling is present. If absent,
name the precise failure mode. If present, state whether callers honor it correctly.

---

**LOAD SHAPE COMPARISON**

Compare 1x nominal volume under UNIFORM vs. BURST arrival. Total request count identical;
only arrival distribution differs. Required: at least one numeric comparison showing a TABLE A
tier OK under UNIFORM but HIT or SAT under BURST. If no tier changes status, state the
structural reason (specific rate limit mechanism).

---

**TABLE F — MITIGATION PRESCRIPTIONS**

*(At least two rows.)*

| Gap-ID | Throttle behavior (Tier-ID + failure mode) | Setting or API parameter | Recommended value or pattern | Expected outcome |
|--------|-------------------------------------------|--------------------------|------------------------------|-----------------|
| M-01   |                                           |                          |                              |                 |
| M-02   |                                           |                          |                              |                 |

`Setting or API parameter` — exact setting name or API parameter. "Add retry logic" fails.
`Recommended value or pattern` — specific value or implementation instruction.
`Expected outcome` — measurable change when applied.

---

## V-04 — Combined: C-11 + C-12 + C-13

**Axis:** Combined lifecycle + output format + phrasing register. Arithmetic anchor as
lifecycle gate (C-11), canonical registry as prerequisite output block (C-12), multi-clause
vocabulary contract in TABLE B column definition (C-13). Does NOT reinforce C-14 — TABLE C
retains a single Retry-After column.

**Hypothesis:** The three criteria are structurally orthogonal: arithmetic anchor occupies
a pre-TABLE A gate slot, canonical registry occupies a pre-TABLE A declaration slot, and
multi-clause vocabulary lives in the TABLE B column definition. None crowds the other. The
arithmetic anchor and tier registry both precede TABLE A but serve different purposes: the
anchor derives the binding overage before the tier inventory begins; the registry declares
the authoritative tier set before inventory populates it. Risk: the two pre-TABLE A blocks
(anchor + registry) increase prompt length before any analysis begins, and the model skips
or compresses one under token pressure. Mitigation: both blocks are marked as explicit
prerequisites with gate language ("do not proceed to TABLE A until complete").

**New v5 scoring:** passes C-09, C-10, C-11, C-12, C-13 = 5/6 aspirational.
`composite = 60 + 30 + (5/6 × 10) = 98.33 → 98`
C-14 is the sole remaining gap; V-05 closes it.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the sections below in order. Do not substitute prose for
any table. Every cell must be filled.

---

**THROTTLE ARITHMETIC ANCHOR**

*(Complete before any other section. Do not proceed to TIER REGISTRY or TABLE A until
the arithmetic chain is fully derived.)*

State the primary throttle constraint arithmetic:

- System limit: [number + unit]
- Distribution factor: [flows, connections, or tenants sharing the limit, with count]
- Per-unit capacity: [system limit / distribution factor = result with unit]
- Demand per unit at 1x nominal: [request rate per unit]
- Derived overage or headroom: [absolute number AND percentage]

Example: "600 req/min connector limit / 12 flows = 50 req/min per flow. Demand: 75 req/min
per flow. Overage: 25 req/min per flow — 50% over capacity at 1x nominal."

Stating limit and volume without the derived overage/headroom percentage fails this anchor.

---

**TIER REGISTRY — CANONICAL SOURCE OF TRUTH**

*(Complete after THROTTLE ARITHMETIC ANCHOR and before TABLE A.)*

This is the canonical tier registry. Every throttle tier must be declared here before any
analysis section references it. No tier may appear in TABLE A, TABLE B, TABLE C, TABLE D,
the cascade scenario, the risk ranking, or any downstream section unless it is listed here.
Any tier introduced in a downstream section that is absent from this registry is a structural
violation.

| Registry-ID | Component | Limit type (rate, concurrency, or quota) |
|-------------|-----------|------------------------------------------|
| T-01        |           |                                          |
| T-02        |           |                                          |
| ...         |           |                                          |

*Prerequisite: This registry must be complete before TABLE A begins. TABLE A adds numeric
limits and volume-band status to the tiers declared here. It does not introduce new tiers.*

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete after TIER REGISTRY. Use only Tier-IDs declared in the registry.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — must match a Registry-ID above. No new identifiers here.
- `Limit` — number with unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Failure visibility window` — elapsed time before saturation becomes observable.
- `Recovery time` — elapsed time until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism class | Observable effect |
|-----|---------------|--------------|-----------------|-------------------|
| 1   |               |              |                 |                   |
| 2   |               |              |                 |                   |
| ... |               |              |                 |                   |

`Mechanism class` — each cell must contain a three-clause event chain:
[trigger event]; [system response]; [downstream propagation]. Acceptable forms:

- "429 returned; no Retry-After handler; immediate retry issued within same throttle window"
- "concurrency cap reached; runtime queues trigger invocations; backlog accumulates at PA
  runtime layer"
- "queue fills; overflow requests dropped; upstream sees 503 and retries compound inbound load"
- "connection limit reached; new requests queued at gateway; queue depth grows until timeout
  fires"
- "tenant quota exhausted; all flows sharing quota receive 429; backoff timers unsynchronized
  across flows"

One-word labels do not satisfy this column. Phrases like "it propagates" or "cascade occurs"
fail even if correct tiers are named.

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

*(At least one row.)*

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**TIER RISK RANKING**

Rank all TIER REGISTRY tiers by business risk. One sentence per tier. For the top-ranked
tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting from the 1x binding constraint. Use Tier-IDs from TIER
REGISTRY throughout. Minimum three tiers. State each causal link.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: state whether Retry-After handling is present. If absent,
name the failure mode precisely. If present, state whether callers honor it correctly.

---

**LOAD SHAPE COMPARISON**

Compare 1x nominal volume under UNIFORM vs. BURST arrival (same total count, different
distribution). Required: at least one numeric comparison showing a TABLE A tier OK under
UNIFORM but HIT or SAT under BURST. If no tier changes status, state the structural reason.

---

**TABLE F — MITIGATION PRESCRIPTIONS**

*(At least two rows.)*

| Gap-ID | Throttle behavior (Tier-ID + failure mode) | Setting or API parameter | Recommended value or pattern | Expected outcome |
|--------|-------------------------------------------|--------------------------|------------------------------|-----------------|
| M-01   |                                           |                          |                              |                 |
| M-02   |                                           |                          |                              |                 |

`Setting or API parameter` — exact setting name. Generic phrases fail.
`Recommended value or pattern` — specific value or instruction.
`Expected outcome` — measurable change when applied.

---

## V-05 — Maximum Density: C-11 + C-12 + C-13 + C-14 Reinforced via Inertia Framing

**Axis:** V-04 plus inertia framing for C-14. The preamble explicitly names "Retry-After
conflation" — treating API-level signal emission and calling-code handling as the same
property — as the specific inertia pattern C-14 addresses. TABLE C gets two independent
Retry-After columns (emitted by API vs. honored by calling code). RETRY-AFTER GAP ASSESSMENT
explicitly addresses both dimensions for the first-hit tier.

**Hypothesis:** C-14's pass condition requires both the "present" (API emits the header) and
"surfaced" (calling code reads and waits) dimensions to appear for at least the first-hit tier.
The most common failure mode is conflation: the analysis notes "Retry-After present" or "Retry-
After absent" as if these describe the same property, when they describe two independent
implementation points. Inertia framing primes against conflation before the output begins: if
the preamble names conflation as an inertia pattern ("the Retry-After header that the API emits
but the calling flow ignores — treating 'the API signals it' and 'the code honors it' as the
same thing"), the model has a named failure mode to avoid, not just an implicit standard to
meet. TABLE C's two-column structure then enforces the distinction at every row; RETRY-AFTER
GAP ASSESSMENT closes by explicitly assigning pass/fail to each dimension independently.

**New v5 scoring:** passes all 6 aspirational: C-09, C-10, C-11, C-12, C-13, C-14.
`composite = 60 + 30 + (6/6 × 10) = 100`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The Retry-After header that the API emits but the calling flow ignores — treating "the API
  signals the retry window" and "the code waits the specified interval" as the same property,
  when one is an API contract and the other is an implementation choice in the flow runtime
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the sections below in order. Do not substitute prose for
any table. Every cell must be filled.

---

**THROTTLE ARITHMETIC ANCHOR**

*(Complete before TIER REGISTRY and TABLE A. Do not proceed until derivation is complete.)*

State the primary throttle constraint arithmetic:

- System limit: [number + unit]
- Distribution factor: [flows, connections, or tenants sharing the limit, with count]
- Per-unit capacity: [system limit / distribution factor = result with unit]
- Demand per unit at 1x nominal: [request rate per unit at stated volume]
- Derived overage or headroom: [absolute number AND percentage]

Example: "600 req/min connector limit / 12 flows = 50 req/min per flow. Demand: 75 req/min
per flow. Overage: 25 req/min per flow — 50% over capacity at 1x nominal."

Stating limit and volume without the derived overage or headroom percentage fails this anchor.

---

**TIER REGISTRY — CANONICAL SOURCE OF TRUTH**

*(Complete after THROTTLE ARITHMETIC ANCHOR. Complete before TABLE A.)*

This is the canonical tier registry. Every throttle tier must be declared here before any
downstream section references it. No tier may appear in TABLE A, TABLE B, TABLE C, TABLE D,
the cascade scenario, or any other section unless listed here first. Any tier introduced
downstream but absent from this registry is a structural violation.

| Registry-ID | Component | Limit type (rate, concurrency, or quota) |
|-------------|-----------|------------------------------------------|
| T-01        |           |                                          |
| T-02        |           |                                          |
| ...         |           |                                          |

*Prerequisite: This registry must be complete before TABLE A begins. TABLE A adds numeric
limits and volume-band status. It does not introduce new tiers.*

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete after TIER REGISTRY. Use only Tier-IDs declared in the registry.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — must match a Registry-ID above.
- `Limit` — number with unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Failure visibility window` — elapsed time before saturation becomes observable.
- `Recovery time` — elapsed time until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism class | Observable effect |
|-----|---------------|--------------|-----------------|-------------------|
| 1   |               |              |                 |                   |
| 2   |               |              |                 |                   |
| ... |               |              |                 |                   |

`Mechanism class` — each cell must contain a three-clause event chain:
[trigger event]; [system response]; [downstream propagation]. Acceptable forms:

- "429 returned; no Retry-After handler; immediate retry issued within same throttle window"
- "concurrency cap reached; runtime queues trigger invocations; backlog accumulates at PA
  runtime layer"
- "queue fills; overflow requests dropped; upstream sees 503 and retries compound inbound load"
- "connection limit reached; new requests queued at gateway; queue depth grows until timeout
  fires"
- "tenant quota exhausted; all flows sharing quota receive 429; backoff timers unsynchronized
  across flows"

One-word labels (queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade) do not satisfy this column. Phrases like "it propagates" or "cascade occurs"
fail even if correct tiers are named.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

Two independent Retry-After columns appear below. These are different implementation properties
and must be assessed independently:
- `Retry-After emitted by API?` — does the throttled API or service layer emit a Retry-After
  header in its 429 response? This is an API contract property.
- `Retry-After honored by calling code?` — does the flow, connector, or calling runtime read
  the Retry-After value and wait the specified interval before retrying? This is an
  implementation property of the caller. A tier may be Y/Y (API emits; code waits), Y/N
  (API emits; code ignores and retries immediately), or N/N (API does not emit; no interval
  to honor). Treating these two columns as the same property is the inertia pattern named
  above.

| Tier-ID | Error code or signal | Retry-After emitted by API? (Y/N) | Retry-After honored by calling code? (Y/N) | User-visible consequence |
|---------|---------------------|----------------------------------|--------------------------------------------|--------------------------|
| T-01    |                     |                                  |                                            |                          |
| T-02    |                     |                                  |                                            |                          |
| ...     |                     |                                  |                                            |                          |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row.)*

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**TIER RISK RANKING**

Rank all TIER REGISTRY tiers by business risk. One sentence per tier. For the top-ranked
tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting from the 1x binding constraint. Use Tier-IDs from TIER
REGISTRY throughout. Minimum three tiers. State each causal link.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier, assess both dimensions independently:

**PRESENT (API layer):** Does the throttled endpoint emit a Retry-After header in its 429
response? State the header value if known, or "not emitted" if the tier sends 429 without
the header. Reference the TABLE C `Retry-After emitted by API?` column.

**SURFACED (calling code):** Does the calling flow, connector runtime, or HTTP handler read
the Retry-After value and wait the specified interval before retrying? State specifically
whether the PA runtime or custom connector honors this header, or whether it fires its own
retry policy on a separate schedule. Reference the TABLE C `Retry-After honored by calling
code?` column.

Name the failure consequence for each Y/N combination observed. A "Y/N" result (API emits;
code ignores) produces a retry storm at the flow's own retry frequency — not at the interval
the throttled system permits. This is the inertia pattern the two columns exist to surface.

---

**LOAD SHAPE COMPARISON**

Compare 1x nominal volume under UNIFORM vs. BURST arrival (same total count, different
distribution). Required: at least one numeric comparison showing a TABLE A tier OK under
UNIFORM but HIT or SAT under BURST. Ground in a specific TABLE A rate limit value. If no
tier changes status between patterns, state the structural reason (specific rate limit
mechanism: per-minute bucket, per-second window, sliding window, token bucket).

---

**TABLE F — MITIGATION PRESCRIPTIONS**

*(At least two rows. One per identified gap.)*

| Gap-ID | Throttle behavior (Tier-ID + failure mode) | Setting or API parameter | Recommended value or pattern | Expected outcome |
|--------|-------------------------------------------|--------------------------|------------------------------|-----------------|
| M-01   |                                           |                          |                              |                 |
| M-02   |                                           |                          |                              |                 |

Column definitions:
- `Throttle behavior` — Tier-ID + specific failure mode. Generic entries fail the row.
- `Setting or API parameter` — exact setting name, connector policy key, or API parameter.
  "Add retry logic" does not satisfy this column.
- `Recommended value or pattern` — specific numeric value, pattern name, or implementation
  instruction. "Adjust as needed" does not satisfy this column.
- `Expected outcome` — measurable change in throttle behavior when the prescription is applied.
