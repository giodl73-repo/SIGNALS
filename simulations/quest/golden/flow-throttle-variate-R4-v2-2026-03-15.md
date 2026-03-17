# flow-throttle Variate — Round 4 v2 (Rubric v4 Revised: C-16/C-17/C-18)
**Date:** 2026-03-15
**Rubric:** v4 revised (C-01 through C-18; N_essential=5, N_recommended=3, N_aspirational=10)
**New in this revision:** C-16 (mechanism class co-located in primary trace structure),
C-17 (cascade scenario follows complete mechanism trace), C-18 (anti-pattern contrast pairs)
**Baseline ceiling:** Prior rounds reliably pass C-01 through C-12; C-13 passes PARTIAL
(mechanism class in separate audit table passes vocabulary check but fails co-location);
C-14 passes when TABLE C has explicit "present" vs. "honored" split; C-15 passes when
TABLE C has a Work item fate column; C-16/C-17/C-18 first appearance here.

---

## Round 4 v2 State Analysis: What Prior Rounds Established vs. What This Round Must Add

**Prior rounds confirmed (carry forward):**
- C-01 through C-08: Essential and recommended criteria pass reliably across all prior
  variations when TABLE A has a Tier-ID system, TABLE B has minimum-two-hop enforcement,
  TABLE C has one row per tier, and TABLE D names at least one burst path.
- C-09 (mitigation prescriptions): TABLE F with a Setting-or-API-parameter column that
  explicitly rejects generic phrases passes reliably. Column enforcement is the structural
  surface: a cell requiring a specific key name cannot be satisfied by "add retry logic."
- C-10 (load shape sensitivity): LOAD SHAPE COMPARISON section with UNIFORM vs. BURST
  comparison at fixed 1x volume passes when numeric arrival rates are required and at least
  one TABLE A tier must show status change between patterns.
- C-11 (worked throttle arithmetic): Passes when a THROTTLE ARITHMETIC example appears
  before TABLE A, demonstrating a complete arithmetic chain: limit + volume + derived
  overage/headroom. Stating limits and volumes without the derived result is flagged as
  incomplete by the example.
- C-12 (explicit tier enumeration prefix): Passes when an ordered list of all tiers appears
  before TABLE A and TABLE A is declared as the canonical tier registry — downstream sections
  must reference only tiers in the list.
- C-13 (mechanism-typed propagation hops): PARTIAL pass. Prior variations constrained
  mechanism vocabulary (queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade as one-word labels; some added multi-clause forms). But mechanism class
  lived in a separate audit block below TABLE B, not in TABLE B itself. Vocabulary terms were
  present; structural co-location was absent.
- C-14 (Retry-After present vs. surfaced): Passes when TABLE C has two explicit columns —
  "Retry-After emitted? (Y/N)" for the API-level signal and "Honored by caller? (Y/N)" for
  whether the calling code reads and acts on it — and RETRY-AFTER GAP ASSESSMENT names both
  dimensions for the first-hit tier.
- C-15 (work item fate per tier): Passes when TABLE C has a "Work item fate" column with
  four constrained values — queued, dropped, returned-as-error, deferred — and the UX
  description names one of these for each tier.

**Three gaps Round 4 v2 must close:**

C-16 — Mechanism class co-located in primary trace structure: Prior rounds put mechanism
class in a separate audit block below TABLE B. Even with correct vocabulary terms, the
separation allowed synonym-rewordings to satisfy the constraint: "propagates," "cascades,"
"also throttled" could appear in the hop row while the audit block was completed separately.
Co-location makes vocabulary compliance visible at the moment of writing each hop row —
the cell cannot be satisfied by anything that isn't a multi-clause mechanism description.

C-17 — Cascade scenario follows complete mechanism trace: Prior rounds produced cascade
scenarios immediately after TABLE B without checking whether all Mechanism class cells were
populated with vocabulary terms. A cascade scenario can absorb mechanism gaps by implying
mechanisms through narrative: "T-02 saturates and T-03 is also affected" passes a casual
reading but conceals the absent mechanism class in TABLE B. An explicit gate — a structural
check that blocks advancing to CASCADE SCENARIO until every TABLE B row has a mechanism
class from the constrained vocabulary — removes this compensation pathway.

C-18 — Anti-pattern contrast pairs: Prior rounds did not name the failure modes they
avoided. An output can satisfy C-13, C-14, C-15 without ever naming "cascade labeling,"
"Retry-After conflation," or "symptom-only UX." C-18 requires both: the failure phrase AND
the compliant replacement in the same location. Pre-committing to the failure phrase as an
INERTIA CALLOUT before each relevant section forces the model to write the contrast rather
than simply achieve compliance silently.

**Round 4 v2 questions to answer:**

Q1 (V-01): Does adding `Mechanism class` as a column in TABLE B — with the multi-clause
vocabulary forms in the column definition — structurally enforce C-16 co-location and reduce
vocabulary drift compared to a separate audit block?

Q2 (V-02): Does an explicit MECHANISM GATE between TABLE B and CASCADE SCENARIO — a
pass/fail checklist requiring every TABLE B Mechanism class cell to contain a vocabulary
term — enforce C-17 phase dependency without becoming a token sink?

Q3 (V-03): Do INERTIA CALLOUTs placed immediately before TABLE B (C-13 anti-pattern),
RETRY-AFTER GAP ASSESSMENT (C-14 anti-pattern), and TABLE C's Work item fate column
definition (C-15 anti-pattern) produce C-18 contrast pairs in the output?

Q4 (V-04): Do all three (C-16 co-location + C-17 gate + C-18 CALLOUTs) compose without
mutual crowding — does co-location in TABLE B make the gate check redundant or complementary?

Q5 (V-05): Does the maximum-density variant — V-04 plus tier enumeration prefix (C-12) and
a worked arithmetic example (C-11) — maintain C-16/C-17/C-18 improvements without degrading
TABLE F (C-09) or LOAD SHAPE (C-10)?

---

## Round 4 v2 Variation Map

| Variation | Axis | New criteria targeted | Predicted composite |
|-----------|------|-----------------------|---------------------|
| V-01 | Single: C-16 mechanism class co-located in TABLE B | C-16 | ~87/100 |
| V-02 | Single: C-17 MECHANISM GATE between TABLE B and CASCADE SCENARIO | C-17 | ~85/100 |
| V-03 | Single: C-18 INERTIA CALLOUTs naming failure phrases before key sections | C-18 | ~84/100 |
| V-04 | Combined: C-16 + C-17 + C-18 | C-16 + C-17 + C-18 | ~100/100 |
| V-05 | Maximum density: V-04 + C-12 tier prefix + C-11 arithmetic example | all 10 aspirational | ~100/100 |

---

## V-01 — Single Axis: C-16 Mechanism Class Co-Located in TABLE B

**Axis:** The `Mechanism` column in TABLE B is replaced with `Mechanism class`. The column
definition requires a multi-clause description naming the trigger, the handler absence or
resource state, and the consequence within the window — not a one-word label. The column
appears in TABLE B's header row, directly adjacent to the hop fields. No separate mechanism
audit block appears anywhere in the output. The column definition contains a prohibitive note:
"Do not add a separate mechanism audit or review pass below this table. Every mechanism class
entry must appear in this column, in this table."

**Hypothesis:** The structural problem with a separate audit block is that the model writes
the hop row first (with a vague Mechanism cell) and then writes the audit block, where
vocabulary terms appear — the two actions are separated by token distance. Co-location forces
the vocabulary decision at the moment of writing the hop row: the cell is adjacent to From,
To component, and Observable effect, which supply the context needed to select the vocabulary
form. The prohibitive note blocks the audit-block compensation pathway. Primary risk: the
model writes a compliant-looking multi-clause entry that doesn't actually name a constrained
mechanism (e.g., "request volume exceeds capacity; system experiences slowdown; performance
degrades") — formally multi-clause but vocabulary-free.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

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
- `Limit` — a number with a unit. Vague entries such as "limited" or "throttled" invalidate
  the row.
- `STATUS Nx` — OK (limit not reached), HIT (throttling begins), SAT (fully saturated,
  requests failing). The binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable after the limit
  is exceeded (time + observable signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism class | Observable effect |
|-----|---------------|--------------|-----------------|-------------------|
| 1   |               |              |                 |                   |
| 2   |               |              |                 |                   |
| ... |               |              |                 |                   |

Column definitions:
- `From` — a Tier-ID from TABLE A. No other form.
- `Mechanism class` — a multi-clause description naming: (1) the signal or resource state at
  the source tier, (2) the handler absence or queue/concurrency behavior that transmits the
  pressure, and (3) the consequence at the destination component within the throttle window.
  Acceptable forms: "429 returned; no Retry-After handler; immediate retry issued within same
  throttle window" / "concurrency cap reached; runtime queues trigger invocations; backlog
  accumulates at PA runtime layer" / "queue fills; overflow requests dropped; upstream sees
  503 and retries compound inbound load." One-word labels (queue-fill, cascade-occurs,
  propagates) do not satisfy this column even if the correct tiers are named.
  **Do not add a separate mechanism audit section or review pass below this table. Every
  mechanism class entry must appear in this column, in this table.**
- `Observable effect` — what becomes visible at the destination component as pressure arrives.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After emitted? (Y/N) | Honored by caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Work item fate | Failure if Retry-After ignored |
|---------|---------------------|--------------------------|--------------------------|--------------------------------------|----------------|-------------------------------|
| T-01    |                     |                          |                          |                                      |                |                               |
| T-02    |                     |                          |                          |                                      |                |                               |
| ...     |                     |                          |                          |                                      |                |                               |

Column definitions:
- `Retry-After emitted?` — whether the throttle tier includes a Retry-After header or
  equivalent signal in the 429/503 response at the API level. Y/N only.
- `Honored by caller?` — whether the calling code reads the Retry-After signal and respects
  the wait interval before retrying. Y/N only. A tier where Retry-After is emitted but not
  honored has Y in the first column and N in the second.
- `Work item fate` — what happens to in-flight work items when this tier throttles. One of:
  queued (held for retry), dropped (lost, no retry), returned-as-error (caller handles),
  deferred (moved to a later window). No other values.

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with rationale.
For the top-ranked tier, reference the `Failure visibility window` and `Recovery time` values
from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from TABLE A
throughout. State each causal link explicitly. Minimum three tiers causally linked. Generic
cascade claims ("also affected," "cascade occurs") do not satisfy this section — name the
mechanism at each causal link.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier, address both dimensions:
1. **API-level signal** — does the throttle tier emit a Retry-After header or equivalent
   (from the `Retry-After emitted?` column in TABLE C)? If yes, state the signal format.
2. **Caller-level handling** — does the calling code in the flow read and honor the
   Retry-After signal (from the `Honored by caller?` column in TABLE C)? If the signal is
   emitted but not honored, name the failure mode precisely: retry storm, quota exhaustion
   within the throttle window, silent degradation.

Both dimensions must appear. An assessment that addresses only one dimension does not satisfy
this section.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after RETRY-AFTER GAP ASSESSMENT. One row per identified gap. Minimum two rows.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `Source` — Tier-ID from TABLE A or Path-ID from TABLE D where the gap was identified.
- `Gap type` — one of: unprotected-burst-path, missing-retry-after, cascade-risk,
  quota-exhaustion.
- `Component` — the specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key, connector property, or API
  attribute name. Generic entries such as "add retry logic," "improve error handling," or
  "configure throttling" do not satisfy this column. A cell without a specific parameter
  name is incomplete.
- `Change` — the specific value to set or pattern to apply.
- `Expected outcome` — the concrete behavioral change at the Source tier.

---

**LOAD SHAPE COMPARISON**

Using TABLE A rate limit values, compare 1x nominal volume under two arrival patterns.
Total request count is the same in both patterns — only the arrival distribution differs.

- **UNIFORM arrival** — requests distributed evenly across the measurement window. Express
  as: total volume distributed over [window], yielding [N] req/sec or req/min average. State
  which TABLE A tiers are HIT or SAT at this arrival rate and why.
- **BURST arrival** — same total requests concentrated in a fraction of the window (state
  the fraction). Express as: total volume arriving in first [fraction] of window, yielding
  [N] req/sec peak. State which TABLE A tiers are HIT or SAT and why.

Required: at least one numeric comparison showing a TABLE A tier that is OK under UNIFORM
but HIT or SAT under BURST at identical total request count. If no tier changes status,
state why — citing the specific rate limit type (per-minute vs. per-second, token bucket vs.
sliding window) as the reason.

---

## V-02 — Single Axis: C-17 Mechanism Gate

**Axis:** A MECHANISM GATE section is inserted between TABLE B and CASCADE SCENARIO. The
gate contains a structured checklist: for each TABLE B row, the Mechanism class cell must
contain one of the constrained vocabulary forms — a multi-clause description naming the
signal, the handler/queue behavior, and the consequence. If any row has a blank Mechanism
class or a one-word label (queue-fill, propagates, cascades, also affected), the gate
instructs: "Correct that row before advancing. Write the compliant Mechanism class for
hop [N], then continue to CASCADE SCENARIO." The gate is self-evaluating: the model is
the evaluator, the pass condition is stated explicitly.

**Hypothesis:** The cascade scenario is a dependent artifact. Its quality depends on the
mechanism trace being complete. A cascade scenario that appears alongside an incomplete
TABLE B absorbs mechanism gaps — narrative fills in what the table omits. The gate forces
the mechanism decision to be made and recorded in TABLE B before the cascade can begin.
The gate is self-evaluating rather than requiring a reviewer because the pass condition is
mechanically verifiable: does the cell contain a multi-clause description or not? Primary
risk: the model passes its own gate by writing a formally multi-clause entry that doesn't
select from the vocabulary (e.g., "HTTP error returned; system processes it; delay occurs").

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

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
dependency-stall, timeout-cascade. Do not write phrases that name no mechanism: "propagates,"
"also throttled," "cascade occurs" without a mechanism term fail this column.

---

**MECHANISM GATE**

*(Complete before advancing to CASCADE SCENARIO.)*

Evaluate each TABLE B row. For each hop, the Mechanism cell must contain one of these
constrained forms — a multi-clause description naming (1) the signal or resource state at
the source, (2) the handler absence or queue behavior, and (3) the consequence at the
destination within the throttle window:

- Form A: "[HTTP signal, e.g., 429 returned]; [handler absence, e.g., no Retry-After
  handler]; [consequence, e.g., immediate retry issued within same throttle window]"
- Form B: "[resource cap type, e.g., concurrency cap reached]; [queue behavior, e.g.,
  runtime queues trigger invocations]; [accumulation, e.g., backlog accumulates at PA
  runtime layer]"
- Form C: "[buffer state, e.g., queue fills]; [overflow outcome, e.g., overflow requests
  dropped]; [upstream effect, e.g., upstream sees 503 and retries compound inbound load]"

For each hop, verify:
- [ ] Hop 1 Mechanism — does it match one of the constrained forms above? If no: write the
  compliant form for Hop 1 now, then continue.
- [ ] Hop 2 Mechanism — does it match? If no: correct before continuing.
- [ ] (Repeat for each additional hop)

**Do not advance to CASCADE SCENARIO until all hop rows pass this gate.** An incomplete
TABLE B with a cascade scenario present fails C-17 even if the cascade is well-formed.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After emitted? (Y/N) | Honored by caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Work item fate | Failure if Retry-After ignored |
|---------|---------------------|--------------------------|--------------------------|--------------------------------------|----------------|-------------------------------|
| T-01    |                     |                          |                          |                                      |                |                               |
| T-02    |                     |                          |                          |                                      |                |                               |
| ...     |                     |                          |                          |                                      |                |                               |

Column definitions:
- `Retry-After emitted?` — API-level: does the throttle response include a Retry-After signal?
- `Honored by caller?` — caller-level: does the flow's calling code read and wait before retry?
- `Work item fate` — queued, dropped, returned-as-error, or deferred. No other values.

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row.)*

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk. One sentence per tier with rationale. For the top tier,
reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

*(Complete only after all TABLE B hops pass the MECHANISM GATE above.)*

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers. Generic cascade claims do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier, address both:
1. **API-level signal** — does the tier emit Retry-After? State the signal format.
2. **Caller-level handling** — does the calling code honor it? If emitted but not honored,
   name the failure mode: retry storm, quota exhaustion, silent degradation.

---

**TABLE F — MITIGATION REGISTRY**

*(Minimum two rows. One per identified gap.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` requires a specific named parameter. Generic entries fail.

---

**LOAD SHAPE COMPARISON**

Compare 1x nominal volume under UNIFORM and BURST arrival (same total, different shape).
State numeric arrival rates for each. Show at least one TABLE A tier whose status changes
between patterns. If no tier changes, state why citing the rate limit type.

---

## V-03 — Single Axis: C-18 Anti-Pattern INERTIA CALLOUTs

**Axis:** Three INERTIA CALLOUTs are injected immediately before the sections that produce
the outputs C-13, C-14, and C-15 evaluate. Each CALLOUT names the specific failure phrase,
states why it fails, and provides the compliant replacement in adjacent contrast form. The
CALLOUTs appear as labeled blocks before TABLE B (C-13 anti-pattern: cascade labeling),
before RETRY-AFTER GAP ASSESSMENT (C-14 anti-pattern: Retry-After conflation), and in
TABLE C's Work item fate column definition (C-15 anti-pattern: symptom-only UX). The rest
of the structure is the R4 v1 baseline: TABLE A through TABLE F plus LOAD SHAPE COMPARISON.

**Hypothesis:** An output can satisfy C-13, C-14, C-15 without ever naming the failure it
avoided. C-18's pass condition requires both the failure phrase and the compliant form in
the same location. Pre-committing to the failure phrase as an INERTIA CALLOUT forces the
contrast: the model has already named the failure, so the compliant section immediately
below constitutes the replacement. The form is: "[failure phrase] fails because [reason];
compliant form: [vocabulary term with context]." Primary risk: the CALLOUT naming the failure
phrase is present but the section that follows does not contrast with it — it achieves
compliance without referencing the named failure.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

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
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

> **INERTIA CALLOUT — Mechanism class (C-13 anti-pattern: cascade labeling)**
> "Cascade occurs" fails because it names no mechanism — it is a label for the outcome, not
> a description of what transmitted the pressure from one tier to the next. Similarly,
> "propagates," "also throttled," and "T-03 is affected" fail because they name the result
> without identifying the handler absence, queue behavior, or resource state that caused it.
> Compliant form: "429 returned; no Retry-After handler; immediate retry issued within same
> throttle window" — this names the signal (429), the absence (no handler), and the
> consequence (immediate retry in window). Use this form in TABLE B's Mechanism column.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must be a multi-clause description as shown in the INERTIA CALLOUT above:
signal or resource state + handler absence or queue behavior + consequence within window.
One-word labels fail even if the correct tiers are named.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After emitted? (Y/N) | Honored by caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Work item fate | Failure if Retry-After ignored |
|---------|---------------------|--------------------------|--------------------------|--------------------------------------|----------------|-------------------------------|
| T-01    |                     |                          |                          |                                      |                |                               |
| T-02    |                     |                          |                          |                                      |                |                               |
| ...     |                     |                          |                          |                                      |                |                               |

Column definitions:
- `Retry-After emitted?` — API-level signal presence. Y/N.
- `Honored by caller?` — caller reads and waits before retry. Y/N.
- `Work item fate` — **INERTIA CALLOUT (C-15 anti-pattern: symptom-only UX):** "User sees
  an error message" fails because it names the user-visible symptom but omits what happened
  to the work item. Compliant form: one of — queued (held for retry), dropped (lost),
  returned-as-error (caller handles), deferred (moved to later window). The symptom may
  appear in `Error code or signal`; the fate must appear here.

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row.)*

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk. One sentence per tier with rationale. For the top tier,
reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers. Generic cascade claims do not satisfy this section.

---

> **INERTIA CALLOUT — Retry-After layer split (C-14 anti-pattern: Retry-After conflation)**
> "Retry-After is absent" fails when the API emits it but the caller ignores it — in that case
> the signal is present at the API level but not surfaced to the calling code. "Retry-After is
> present" fails when it is emitted but the flow does not read or honor it. Compliant form:
> name both dimensions separately: (1) whether the throttle tier emits a Retry-After signal
> in the 429/503 response, AND (2) whether the calling code reads and acts on it. These are
> independent facts and must appear as distinct statements.

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier, address both dimensions as distinguished above:
1. **API-level** — does the tier emit a Retry-After signal? State the format if yes.
2. **Caller-level** — does the calling code honor it? If emitted but not honored, name the
   failure mode: retry storm, quota exhaustion within the throttle window, silent degradation.

---

**TABLE F — MITIGATION REGISTRY**

*(Minimum two rows. One per identified gap.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` requires a specific named parameter. Generic entries fail.

---

**LOAD SHAPE COMPARISON**

Compare 1x nominal volume under UNIFORM and BURST arrival (same total, different shape).
State numeric arrival rates for each. Show at least one TABLE A tier whose status changes
between patterns. If no tier changes, state why citing the rate limit type.

---

## V-04 — Combined: C-16 + C-17 + C-18

**Axis:** All three new criteria combined in a single prompt. C-16: `Mechanism class` column
co-located in TABLE B with constrained multi-clause vocabulary and explicit prohibition
against separate audit blocks. C-17: MECHANISM GATE between TABLE B and CASCADE SCENARIO
using the same vocabulary forms as TABLE B's column definition, creating a cross-check that
TABLE B's column definitions and the gate enforce the same constraint from two angles.
C-18: INERTIA CALLOUTs for all three key distinctions — cascade labeling (before TABLE B),
Retry-After conflation (before RETRY-AFTER GAP ASSESSMENT), symptom-only UX (in TABLE C
Work item fate column definition). The CALLOUT before TABLE B reinforces the Mechanism class
column definition immediately above it; the gate reinforces it again before CASCADE SCENARIO.

**Hypothesis:** C-16 and C-17 are complementary, not redundant. C-16 enforces co-location
at the row level (the cell is filled correctly when the hop is written). C-17 enforces
completeness at the section level (no row is blank when the cascade begins). They address
different failure modes: the model that writes a partially-compliant Mechanism class in a
separate block fails C-16 but not necessarily C-17; the model that writes correct cells but
leaves one hop blank fails C-17 but not C-16. C-18's CALLOUTs front-load all three named
failure phrases, ensuring they appear in the output before their respective sections — the
compliant sections that follow constitute the explicit replacement. Combined predicted
composite: 100/100. Primary risk: token pressure from three CALLOUT blocks compresses
TABLE F or LOAD SHAPE COMPARISON in models with tight token budgets.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent. Every downstream section uses these verbatim,
  no synonyms.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

> **INERTIA CALLOUT — Mechanism class (C-13 anti-pattern: cascade labeling)**
> "Cascade occurs" fails: it labels the outcome without naming what transmitted the pressure.
> "Also throttled," "propagates," "T-03 is affected" fail for the same reason. These are
> results, not mechanisms. Compliant form: "429 returned; no Retry-After handler; immediate
> retry issued within same throttle window" — three clauses: signal, absence, consequence.
> The Mechanism class column in TABLE B requires this form. The same form is checked in the
> MECHANISM GATE before CASCADE SCENARIO.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism class | Observable effect |
|-----|---------------|--------------|-----------------|-------------------|
| 1   |               |              |                 |                   |
| 2   |               |              |                 |                   |
| ... |               |              |                 |                   |

Column definitions:
- `From` — a Tier-ID from TABLE A. No other form.
- `Mechanism class` — a multi-clause description: (1) signal or resource state at source,
  (2) handler absence or queue/concurrency behavior, (3) consequence at destination within
  throttle window. Acceptable forms:
  - "429 returned; no Retry-After handler; immediate retry issued within same throttle window"
  - "concurrency cap reached; runtime queues trigger invocations; backlog accumulates at PA
    runtime layer"
  - "queue fills; overflow requests dropped; upstream sees 503 and retries compound inbound
    load"
  One-word labels (queue-fill, propagates, cascade-occurs) do not satisfy this column.
  **Do not add a separate mechanism audit section below this table. All mechanism class
  entries appear in this column only.**
- `Observable effect` — what becomes visible at the destination as pressure arrives.

---

**MECHANISM GATE**

*(Complete before advancing to CASCADE SCENARIO.)*

Before writing CASCADE SCENARIO, verify every TABLE B row:
- Each Mechanism class cell contains a three-clause form: (1) signal or resource state,
  (2) handler/queue behavior, (3) downstream consequence within throttle window.
- No cell contains only a one-word label or a phrase that names no mechanism.

For each hop:
- [ ] Hop 1 — Mechanism class satisfies three-clause form? If no: correct before continuing.
- [ ] Hop 2 — Mechanism class satisfies three-clause form? If no: correct before continuing.
- [ ] (Repeat for each additional hop)

CASCADE SCENARIO is not written until all rows pass. If any row is corrected here, the
correction applies to TABLE B as well.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After emitted? (Y/N) | Honored by caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Work item fate | Failure if Retry-After ignored |
|---------|---------------------|--------------------------|--------------------------|--------------------------------------|----------------|-------------------------------|
| T-01    |                     |                          |                          |                                      |                |                               |
| T-02    |                     |                          |                          |                                      |                |                               |
| ...     |                     |                          |                          |                                      |                |                               |

Column definitions:
- `Retry-After emitted?` — API-level: does the throttle response include a Retry-After signal?
- `Honored by caller?` — caller-level: does the flow read and wait before retrying?
- `Work item fate` — **(C-15 anti-pattern: symptom-only UX)** "User sees error message"
  names the symptom but omits the fate. Compliant: one of queued / dropped /
  returned-as-error / deferred. Name the fate here; the symptom lives in `Error code or
  signal`.

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row.)*

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk. One sentence per tier with rationale. For the top tier,
reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

*(Complete only after the MECHANISM GATE above is fully satisfied.)*

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers. Generic cascade claims ("also affected," "cascade
occurs" without mechanism) do not satisfy this section.

---

> **INERTIA CALLOUT — Retry-After layer split (C-14 anti-pattern: Retry-After conflation)**
> "Retry-After is absent" fails when the API emits it but the caller doesn't honor it.
> "Retry-After is present" fails when it's emitted but not honored by the flow. Compliant
> form: state both independently — (1) does the throttle tier emit the signal? (2) does
> the calling code honor it? These are independent facts. Both must appear for the first-hit
> tier.

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier:
1. **API-level signal** — does the tier emit Retry-After? State signal format if yes.
2. **Caller-level handling** — does the calling code honor it? If emitted but not honored,
   name the failure mode: retry storm, quota exhaustion within window, silent degradation.

Both dimensions must appear as distinct statements.

---

**TABLE F — MITIGATION REGISTRY**

*(Minimum two rows. One per identified gap.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `Source` — Tier-ID or Path-ID where the gap was identified.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component where the change is applied.
- `Setting or API parameter` — exact key, property, or attribute name. Generic entries fail.
- `Change` — specific value to set or pattern to apply.
- `Expected outcome` — concrete behavioral change at the Source tier.

---

**LOAD SHAPE COMPARISON**

Compare 1x nominal volume under UNIFORM and BURST arrival (same total, different shape).
State numeric arrival rates for each. Show at least one TABLE A tier whose status changes
between patterns. If no tier changes, state why citing the rate limit type.

---

## V-05 — Maximum Density: V-04 + C-12 Tier Prefix + C-11 Arithmetic Example

**Axis:** V-04 (C-16 + C-17 + C-18) plus two additional aspirational elements: C-12 (explicit
tier enumeration prefix as an ordered list before TABLE A, with TABLE A declared as the
canonical registry — no tier can appear in analysis unless it appears in the prefix list) and
C-11 (a worked throttle arithmetic example immediately before TABLE A, demonstrating the
complete chain: limit + volume + derived overage/headroom as a percentage or absolute number,
with an explicit statement that stating limit and volume without the derived result fails).
Stage structure: (1) tier prefix list, (2) arithmetic example, (3) TABLE A through TABLE F,
(4) LOAD SHAPE COMPARISON.

**Hypothesis:** C-12's tier prefix forces the model to enumerate all tiers before writing
TABLE A — this pre-commitment reduces the likelihood that tiers added mid-analysis (during
TABLE B or cascade scenario) appear in downstream sections without appearing in TABLE A. The
prefix list creates a set-membership constraint: if a component appears in TABLE B's To
component column but is not in the prefix list, the constraint is violated. C-11's arithmetic
example serves as a worked example placed before the task — the model sees the complete chain
(limit / volume = per-unit; demand — per-unit = overage) before filling TABLE A cells, which
primes the `Binding at band` and STATUS columns to carry numeric context. Combined with C-16,
C-17, C-18, this is the maximum-density variation. Primary risk: tier prefix + arithmetic
example + three CALLOUT blocks total approximately 40% more instruction tokens than V-01, which
may compress TABLE F and LOAD SHAPE COMPARISON under tight token budgets.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

---

**TIER ENUMERATION PREFIX**

*(Complete before TABLE A. List every throttle tier present in this system.)*

Enumerate all rate-limiting tiers below. These are the only tiers that may appear in any
downstream table or section. If a component is discovered later in the analysis that was not
listed here, add it to this list before using it downstream — do not introduce unnamed tiers
directly into TABLE B, the cascade scenario, or TABLE F.

1. [Tier name and brief scope — e.g., "SharePoint connector: per-connection request limit"]
2. [Tier name and brief scope]
3. [Add rows as needed]

TABLE A below is the canonical tier registry. Every tier in this list must appear in TABLE A.
Every tier in TABLE A must have appeared in this list first.

---

**THROTTLE ARITHMETIC EXAMPLE**

*(Read before filling TABLE A. This example shows the required arithmetic chain.)*

Example: A flow calls SharePoint at 600 requests per minute across 12 concurrent runs.
SharePoint connector limit: 600 req/min per connection. Demand per flow: 600 / 12 = 50 req/min.
But the signal states actual demand is 75 req/min per flow at peak. Overage: 75 - 50 = 25
req/min per flow, or 50% above the per-connection limit.

This chain is required: **limit + volume + derived overage or headroom as percentage or
absolute number**. Stating "600 req/min limit, flow demands 750 req/min" without deriving
"25% over" or "150 req/min excess" fails C-11. Apply this chain in the `Binding at band`
column and in any arithmetic cited in TIER RISK RANKING or CASCADE SCENARIO.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete after TIER ENUMERATION PREFIX. One row per tier in the prefix list.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent. Assign IDs in the order listed in the tier prefix.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. Include the
  arithmetic chain from the example: limit + volume + derived overage/headroom. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

> **INERTIA CALLOUT — Mechanism class (C-13 anti-pattern: cascade labeling)**
> "Cascade occurs" fails: it names the outcome without the mechanism. "Propagates," "also
> throttled," "T-03 is affected" fail for the same reason — results without mechanisms.
> Compliant form: "429 returned; no Retry-After handler; immediate retry issued within same
> throttle window." Three clauses: signal, absence, consequence. This form is required in
> TABLE B's Mechanism class column and is checked in the MECHANISM GATE.

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism class | Observable effect |
|-----|---------------|--------------|-----------------|-------------------|
| 1   |               |              |                 |                   |
| 2   |               |              |                 |                   |
| ... |               |              |                 |                   |

Column definitions:
- `From` — a Tier-ID from TABLE A. Must match the tier prefix list.
- `To component` — if this component is a throttle tier, it must appear in the tier prefix
  list. If it is not a throttle tier, name it explicitly as a non-throttled downstream component.
- `Mechanism class` — three-clause form required: (1) signal or resource state at source,
  (2) handler absence or queue/concurrency behavior, (3) consequence at destination within
  throttle window. Acceptable forms:
  - "429 returned; no Retry-After handler; immediate retry issued within same throttle window"
  - "concurrency cap reached; runtime queues trigger invocations; backlog accumulates at PA
    runtime layer"
  - "queue fills; overflow requests dropped; upstream sees 503 and retries compound inbound
    load"
  One-word labels and outcome-only phrases fail. **No separate mechanism audit section.**
- `Observable effect` — what becomes visible at the destination as pressure arrives.

---

**MECHANISM GATE**

*(Complete before advancing to CASCADE SCENARIO.)*

Before CASCADE SCENARIO, verify all TABLE B rows:
- [ ] Every Mechanism class cell contains a three-clause form per the column definition.
- [ ] No cell is blank or contains only a one-word label.
- [ ] Every Hop's `From` is a Tier-ID that appears in TABLE A and the tier prefix list.

Correct any failing row before continuing. If a correction reveals a tier not in the prefix
list, add it there and to TABLE A before proceeding.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After emitted? (Y/N) | Honored by caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Work item fate | Failure if Retry-After ignored |
|---------|---------------------|--------------------------|--------------------------|--------------------------------------|----------------|-------------------------------|
| T-01    |                     |                          |                          |                                      |                |                               |
| T-02    |                     |                          |                          |                                      |                |                               |
| ...     |                     |                          |                          |                                      |                |                               |

Column definitions:
- `Retry-After emitted?` — API-level signal. Y/N.
- `Honored by caller?` — caller reads and waits. Y/N. Independent from the above.
- `Work item fate` — **(C-15 anti-pattern: symptom-only UX)** "User sees error" names the
  symptom, not the fate. Compliant: queued / dropped / returned-as-error / deferred.

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. Tier-IDs must match the prefix list.)*

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk. One sentence per tier with rationale, including the
arithmetic overage where available. For the top tier, reference `Failure visibility window`
and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

*(Complete only after the MECHANISM GATE above is fully satisfied.)*

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers. Include the arithmetic chain for the binding
tier from TABLE A's `Binding at band` column. Generic cascade claims do not satisfy this
section.

---

> **INERTIA CALLOUT — Retry-After layer split (C-14 anti-pattern: Retry-After conflation)**
> "Retry-After absent" fails when the API emits it but the caller ignores it. "Retry-After
> present" fails when emitted but not honored. These are distinct facts. Compliant form:
> (1) state whether the tier emits the signal; (2) state whether the calling code honors it.
> Both must appear as separate statements for the first-hit tier.

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier:
1. **API-level signal** — emit? State format if yes.
2. **Caller-level handling** — honor? If emitted but not honored: retry storm, quota
   exhaustion within window, or silent degradation.

Both dimensions must appear as distinct statements.

---

**TABLE F — MITIGATION REGISTRY**

*(Minimum two rows. One per identified gap.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `Source` — Tier-ID or Path-ID. Must match prefix list.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component.
- `Setting or API parameter` — exact key or attribute. Generic entries fail.
- `Change` — specific value or pattern.
- `Expected outcome` — concrete behavioral change at the Source tier, including arithmetic
  where applicable (e.g., "retry amplification capped at 3 attempts; 50% overage at T-01
  eliminated within throttle window").

---

**LOAD SHAPE COMPARISON**

Compare 1x nominal volume under UNIFORM and BURST arrival (same total, different shape).
State numeric arrival rates for each. Show at least one TABLE A tier whose status changes
between patterns. If no tier changes, state why citing the rate limit type. Use Tier-IDs
from TABLE A throughout.
