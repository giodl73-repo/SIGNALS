# flow-throttle Variate — Round 4 (rubric v4 — C-15 audit block, C-16 registry load-shape, C-17 violation posture)
**Date:** 2026-03-15
**Rubric:** v4 (C-01 through C-17; 5 essential / 3 recommended / 9 aspirational)
**New in v4:** C-15 (named end-of-analysis audit block), C-16 (per-tier load-shape classification in registry at registration time), C-17 (REGISTRY GAP as scope violation, not fill-in step)
**Baseline ceiling:** R3 V-05 — all C-01 through C-14 reliable under structural enforcement (role-sequence + registry gate + inertia framing); C-15/C-16/C-17 first appearance here

---

## Round 4 State Analysis: What R3 Established vs. What R4 Must Add

**R3 confirmed (all carry forward under structural enforcement):**
- C-01 (bottleneck localization): reliable when binding constraint requires T-NN + numeric limit +
  causal reason; regresses to vague claims under prose-only instructions.
- C-02 (backpressure 2+ hops): reliable when minimum-hop count is explicit in table schema.
- C-03 (rate-limit tier enumeration, numeric): reliable under Tier Registry table with a Limit column
  that prohibits vague labels by definition.
- C-04 (UX per tier): reliable when UX catalog table requires one row per T-NN — fails when UX is
  an unanchored prose paragraph.
- C-05 (unprotected burst path): reliable under a dedicated table with Gap-reason column requiring
  structural explanation.
- C-06 (retry-after handling): reliable when the binding-tier row requires explicit Retry-After
  presence verdict plus consequence.
- C-07 (cascade 3+ tiers): reliable when minimum-tier count and explicit causal links are required.
- C-08 (quantified thresholds): reliable when the bottleneck section requires a number with unit.
- C-09 (mitigations with tradeoffs): reliable under structured gap entries with Component, Change,
  Expected outcome, and Tradeoff fields — fails when mitigations are an unanchored paragraph.
- C-10 (load-shape sensitivity, numeric): passes when arrival-shape sensitivity is required per T-NN
  in ROLE 1 (SHAPE-NEUTRAL/SHAPE-SENSITIVE with numeric rate differential). Falls back to prose
  label when the registry has no shape-verdict column.
- C-11 (tier-complete severity ranking): reliable when ranking section requires every T-NN with
  explicit coverage check.
- C-12 (cross-section tier integrity verification): passes with explicit count checks in the
  COMPLETION VERIFICATION block (registry count vs. catalog row count vs. ranking count).
- C-13 (tier-ID threading): reliable under role-sequence structure with T-NN-only reference rule
  enforced by the PHASE BOUNDARY RULES; regresses under conversational register.
- C-14 (perspective-separated analysis): reliable when ROLE 1 is a named phase with a "ROLE 1
  complete" gate declaration that precedes ROLE 2 opening.

**R3 gaps (what Round 4 must close):**

C-15 — End-of-analysis audit block: R3 COMPLETION VERIFICATION blocks count rows and report a
C-14/C-13 check, but do not enumerate each downstream section by name. R3 V-05 lists "Step 2B
catalog count" and "Step 2D ranking count" but omits "Step 2A — Backpressure Propagation Trace",
"Step 2C — Unprotected Burst Path Analysis", "Step 2E — Cascade Scenario", and
"Step 2F — Retry-After Gap Assessment" from the audit table. A section not named in the audit
block cannot be verified for C-13 compliance by inspection. C-15 requires a self-contained block
that enumerates every downstream section by canonical name and reports a machine-checkable
unregistered-tier count.

C-16 — Per-tier load-shape classification in registry: R3 ROLE 1 Step 1B asks for arrival-shape
sensitivity per T-NN as a prose bullet after the registry table. This is a deferred analysis: the
shape verdict appears outside the registry row. C-16 requires the load-shape verdict
(SHAPE-NEUTRAL/SHAPE-SENSITIVE) to be a column in the Tier Registry table itself, populated at
registration time, with the numeric rate differential and mechanism explanation in the same cell.
A shape column in a downstream table or a prose note following the registry fails C-16.

C-17 — REGISTRY GAP as scope violation: R3 V-01 says "flag it as a REGISTRY GAP before
continuing" — the analysis pauses but a T-NN is assigned and proceeds. R3 V-02 says "assign the
next available T-NN before filling the row" — a fill-in step with no halt. Neither frames
mid-analysis tier discovery as evidence that enumeration was incomplete. C-17 requires that the
analysis treat a mid-phase component without a T-NN as a structural failure: a named SCOPE
VIOLATION that halts analysis and requires restarting ROLE 1 before ROLE 2 can continue.
Instructions that permit T-NN assignment during ROLE 2 fail C-17 regardless of whether they flag
the event.

**Three questions this round answers:**

Q1 (V-01): Does adding a Load-shape column to the Tier Registry table — with the SHAPE-NEUTRAL /
SHAPE-SENSITIVE verdict and numeric rate differential required at registration time — produce C-16
compliance structurally, or does the model defer the shape analysis to the bottleneck section and
leave the column blank?

Q2 (V-02): Does upgrading the COMPLETION VERIFICATION block to enumerate every downstream section
by canonical name — with a T-NN compliance check per section and a machine-checkable unregistered-
tier count at the end — produce C-15 compliance, or does the model collapse the enumeration to a
summary statement even when section names are listed as required fields?

Q3 (V-03): Does replacing "flag REGISTRY GAP before continuing" with an explicit SCOPE VIOLATION
directive that prohibits T-NN assignment and requires a ROLE 1 restart produce C-17 compliance, or
does the model revert to the fill-in pattern under completion pressure?

---

## Round 4 Variation Map

| Variation | Axis | New criteria targeted | Predicted composite |
|-----------|------|-----------------------|---------------------|
| V-01 | Single: C-16 Load-shape column in registry at registration time | C-16 | ~95/110 |
| V-02 | Single: C-15 Named audit block enumerating all downstream sections by name | C-15 | ~93/110 |
| V-03 | Single: C-17 REGISTRY GAP as SCOPE VIOLATION with restart directive, not fill-in | C-17 | ~94/110 |
| V-04 | Combined: C-15 + C-16 + C-17 on V-03 role-sequence baseline | C-15 + C-16 + C-17 | ~108/110 |
| V-05 | Maximum density: V-04 + three-failure inertia story (tier drift, shape blindness, mid-trace discovery) + explicit section-enumeration in audit block with machine-checkable counts | C-15 + C-16 + C-17 | ~110/110 |

---

## V-01 — Single Axis: C-16 Per-Tier Load-Shape Classification in Registry

**Axis:** Output format — the Tier Registry table gains a Load-shape verdict column, populated at
registration time. Each tier is classified SHAPE-NEUTRAL or SHAPE-SENSITIVE within the registry
row, with the numeric rate differential and mechanism explanation in the same cell. Arrival-shape
analysis that appears only in a downstream prose section or in the bottleneck analysis step fails
C-16: the shape verdict must be a first-class registry attribute. The column definition explicitly
prohibits deferral.

**Hypothesis:** C-10 passes when arrival-shape sensitivity appears in the bottleneck ordering step
(ROLE 1 Step 1B), but that step follows the registry table — the shape verdict is not embedded in
the tier row, making it easy to omit for some tiers while covering others. A Load-shape column in
the registry table forces the verdict at the moment of tier registration: the model must decide
SHAPE-NEUTRAL or SHAPE-SENSITIVE for each tier before advancing to the next row, because the column
is adjacent to the Limit and Window-type columns that supply the context for the decision. The
prohibitive note ("do not defer load-shape analysis to a downstream section; every row requires a
Load-shape verdict at registration") blocks the deferred-analysis compensation pathway. Risk: the
model writes a compliant-looking shape label without the numeric rate differential, satisfying the
column header visually but not substantively.

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
- The tier whose load-shape sensitivity was never measured: same total request count, different
  arrival pattern — and the tier that passes under uniform load fails under burst, because the
  window mechanism punishes instantaneous rate regardless of total volume; the integration test
  at nominal rate never sees it

The analysis below finds these before production does.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences. If you find yourself writing what a flow author sees
  when a tier fires, stop — that belongs in ROLE 2.
- During ROLE 2: describe how callers react to throttle signals, what users observe, how
  failures propagate, and how to fix gaps. You may NOT introduce a new tier that was not
  registered in ROLE 1. If a component appears in a backpressure trace or cascade scenario
  that has no T-NN identifier from ROLE 1, flag it as a REGISTRY GAP before continuing.
  Every tier reference in ROLE 2 must use the T-NN identifier assigned in ROLE 1 — informal
  name references without a T-NN anchor are untracked.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier registry, numeric limits, scope, window type, burst headroom, load-shape
classification, bottleneck ordering. Does not cover: caller behavior, retry handling, UX
consequences, backpressure propagation.*

### Step 1A — Tier Registry

Enumerate every throttle tier in the system described in the signal. Assign a permanent
Tier-ID (T-01, T-02, ...) to each tier. Populate all columns before advancing to the next tier.

| T-NN | Component | Limit (number + unit) | Scope | Window type | Load-shape verdict |
|------|-----------|----------------------|-------|-------------|-------------------|
| T-01 |           |                      |       |             |                   |
| T-02 |           |                      |       |             |                   |
| ...  |           |                      |       |             |                   |

Column definitions:
- `T-NN` — T-01, T-02, ... These identifiers are permanent. Every downstream ROLE 2 section
  that references a throttle tier must use these identifiers verbatim. Informal name references
  without a T-NN anchor are untracked and fail C-13.
- `Limit` — a number with a unit (e.g., 600 req/min, 10 concurrent connections, 100k tokens
  per 10 min). A vague label ("limited", "throttled") is not a limit. If the value cannot be
  confirmed, write `unknown [reason]` where reason is one of: undocumented,
  environment-specific, requires-runtime-measurement, signal-insufficient. Do not omit tiers —
  tiers with unknown limits still receive a T-NN.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (include refill rate in this cell),
  or concurrent-cap.
- `Load-shape verdict` — classify each tier as SHAPE-NEUTRAL or SHAPE-SENSITIVE at
  registration time. Do not defer this verdict to the bottleneck ordering step or to a
  downstream section. Every row requires a verdict before the registry is declared complete.
  - SHAPE-NEUTRAL: the tier's throttle status is identical whether the given request volume
    arrives uniformly (within 10% of average rate throughout the window) or bursts into the
    first 20% of the window. State the specific mechanism that makes it neutral — e.g.,
    "token-bucket: 10 req/sec refill rate; burst depletes headroom but total window count
    stays below 600 req/min cap regardless of arrival distribution."
  - SHAPE-SENSITIVE: the tier's throttle status differs between uniform and burst arrival at
    the same total volume. State: (1) the numeric rate at which the tier fires under burst
    arrival but NOT under uniform arrival at the same total volume (e.g., "burst: 150 req/10s
    exceeds the per-10s cap; uniform: 30 req/10s does not"), and (2) the window mechanism that
    creates the sensitivity (e.g., "fixed-minute window measures instantaneous rate within
    sub-windows; burst concentrates volume into the first sub-window").
  - Leaving this column blank or writing "see bottleneck section" is invalid. The registry row
    is the authoritative load-shape record for each tier.

State "Tier Registry complete — N tiers registered (T-01 through T-NN)." before Step 1B.
**Lock the registry count.** ROLE 2 will verify that every downstream section accounts for
all N tiers.

### Step 1B — Bottleneck Ordering

Using the Step 1A registry and the given request volume, determine:

1. **Binding constraint:** which T-NN is the first to throttle at the given volume under
   uniform arrival. State the T-NN, the numeric limit exceeded, and the causal reason this
   tier binds before all others (lower absolute cap, narrower scope, no burst headroom,
   shortest window, least token-bucket headroom).

2. **Hit order:** list all registry tiers in the order they fire at the given volume under
   uniform arrival. Format: `T-NN (limit: X unit) — fires at Y req/min` or
   `T-NN — not reached at this volume`. Every T-NN from Step 1A must appear in this list.

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX consequences per tier, retry handling, burst paths,
cascade scenario, severity ranking, mitigation prescriptions. Does not cover: new tier
introduction. Every tier reference uses ROLE 1 T-NN identifiers.*

Open ROLE 2 with a registry verification: state the ROLE 1 registry count (N tiers). Every
table and section below that catalogs per-tier data must account for all N tiers.

### Step 2A — Backpressure Propagation Trace

Starting from the ROLE 1 binding constraint, trace how throttling propagates outward.

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — must use a T-NN from the ROLE 1 registry. If a source component has no
  T-NN, flag REGISTRY GAP before filling the row.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade. Generic entries ("degraded", "affected") fail this column.
- Minimum two hops.

### Step 2B — User Experience Catalog

One row per T-NN from the ROLE 1 registry. No tier may be omitted.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: state the row count. Must match ROLE 1 registry count.

### Step 2C — Unprotected Burst Path Analysis

| Path-ID | Entry component | Gap reason (structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|--------------------------------------|----------------|-----------------------------|
| P-01    |                |                                      |                |                             |

- `T-NNs bypassed` — ROLE 1 identifiers only.
- `Gap reason` must be structural: missing connector policy, trigger type exempt from queuing,
  endpoint that bypasses the gateway layer, no concurrency cap on this path.
- If no unprotected path exists: state the conclusion and cite at least two T-NN controls that
  collectively cover every entry point.

### Step 2D — Severity Ranking

Rank all ROLE 1 T-NN entries by business risk, highest to lowest. Every T-NN must appear.
Format: `T-NN — [rationale sentence]`.
For the top-ranked tier: additionally state blast radius, failure visibility (silent vs.
explicit), recovery time.
Coverage check: T-NN count must match ROLE 1 registry count. State explicitly.

### Step 2E — Cascade Scenario

Trace one concrete cascade starting from the ROLE 1 binding constraint. Use T-NN identifiers
throughout — informal names without T-NN anchors are untracked references.
Format: `T-NN (binding, limit: X) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
State the compounded throughput/error-rate effect across all tiers. Minimum three T-NNs with
explicit causal links at each step. Generic claims ("could cascade") fail.

### Step 2F — Retry-After Gap Assessment

For the ROLE 1 binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely (retry storm, missing exponential backoff, silent quota
exhaustion, immediate re-queue within same throttle window). If present, state whether callers
respect it correctly.

### Step 2G — Mitigation Prescriptions

For at least two gaps identified in Steps 2A–2F:

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component — not a layer]
- Change: [setting name + value, API parameter + value, or retry policy with concrete
  parameters; e.g., "set connector.retryPolicy.mode to Exponential with base delay 30s,
  maxAttempts 3, jitter 0.2; read Retry-After header value and use as base delay when present"]
- Expected outcome: [quantified or observable behavioral change]
- Tradeoff: [specific cost — latency, throughput ceiling, operational complexity]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**COMPLETION VERIFICATION**

```
ROLE 1 registry count:                                [N tiers]
Step 2B catalog count:                                [N rows — must match]
Step 2D ranking count:                                [N entries — must match]
ROLE 1 complete before ROLE 2 opened:                 [ ]
ROLE 2 complete:                                      [ ]
C-16: Load-shape verdict in registry at reg time:     [Y / or list tiers with deferred verdicts]
C-14 check — new tiers in ROLE 2:                     [0 unregistered tiers, or REGISTRY GAP entries]
C-13 check — T-NN used in 2A, 2B, 2C, 2D, 2E:        [ ]
```

---

## V-02 — Single Axis: C-15 Named Audit Block with Section Enumeration

**Axis:** Lifecycle emphasis — the analysis closes with a dedicated, named INTEGRITY VERIFICATION
block that enumerates every downstream section by its canonical name and verifies C-13 compliance
section by section. The block additionally reports a machine-checkable count of unregistered tiers
introduced after the registry closed. The block is not a prose summary: it is a structured
checklist where each downstream section appears as a named line item with an explicit coverage
status. A prose closure statement that describes coverage without naming individual sections fails
this block.

**Hypothesis:** R3 COMPLETION VERIFICATION blocks count rows (Step 2B, Step 2D) but leave several
downstream sections unaudited: Step 2A (backpressure trace), Step 2C (burst paths), Step 2E
(cascade), Step 2F (retry-after) are not named in the R3 block. A section absent from the audit
block cannot be verified for C-13 compliance after the fact. The named audit block forces section-
level enumeration: the model must write each section's canonical name and check it explicitly. The
unregistered-tier count at the block's close is machine-checkable: it is a number, not an
assertion. Risk: the model generates the named block but uses non-canonical labels (e.g.,
"section 2" instead of "Step 2A — Backpressure Propagation Trace"), producing a structural block
that cannot be cross-referenced against the analysis sections.

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
- The post-incident audit that cannot verify completeness: the review finds that three sections
  referenced tiers by informal name, the coverage check was a single count comparison, and no
  record exists of which sections were audited — because the audit block named no sections

The analysis below closes with an INTEGRITY VERIFICATION block that names every downstream
section explicitly and makes the unregistered-tier count machine-checkable.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  arrival-shape sensitivity). You may NOT describe caller behavior, retry responses, error
  codes seen by users, or backpressure consequences.
- During ROLE 2: describe caller reactions, user observations, failure propagation, and
  remediation. You may NOT introduce a new tier that was not registered in ROLE 1. If a
  component appears without a T-NN from ROLE 1, flag it as a REGISTRY GAP before continuing.
  Every tier reference uses ROLE 1 T-NN identifiers — informal names without T-NN anchors
  are untracked.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier registry, numeric limits, scope, window type, bottleneck ordering, arrival-shape
sensitivity. Does not cover: caller behavior or UX.*

### Step 1A — Tier Registry

Enumerate every throttle tier. Assign permanent T-NN identifiers (T-01, T-02, ...).

| T-NN | Component | Limit (number + unit) | Scope | Window type | Burst headroom |
|------|-----------|----------------------|-------|-------------|----------------|
| T-01 |           |                      |       |             |                |
| T-02 |           |                      |       |             |                |
| ...  |           |                      |       |             |                |

Column definitions:
- `T-NN` — permanent for this analysis. Every downstream ROLE 2 section uses this identifier
  verbatim. Informal-name-only references are untracked.
- `Limit` — number with unit. Vague labels invalid. `unknown [reason]` for unconfirmable
  values where reason is: undocumented, environment-specific, requires-runtime-measurement,
  signal-insufficient.
- `Window type` — sliding, fixed-minute, token-bucket (refill rate in cell), concurrent-cap.
- `Burst headroom` — Y [amount] or N.

State "Tier Registry complete — N tiers registered (T-01 through T-NN)." before Step 1B.
**Lock the registry count.**

### Step 1B — Bottleneck Ordering and Arrival-Shape Sensitivity

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason (lower cap, narrower
   scope, no burst headroom, shortest window).

2. **Hit order:** every T-NN in order of firing at the given volume.
   `T-NN (limit: X unit) — fires at Y` or `T-NN — not reached at this volume`. All T-NNs
   must appear.

3. **Arrival-shape sensitivity:** for each T-NN: SHAPE-NEUTRAL (state mechanism — window type,
   token-bucket headroom) or SHAPE-SENSITIVE (state numeric rate at which tier fires under
   burst but not under uniform arrival at the same total volume, plus window mechanism).

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX per tier, burst paths, cascade, severity ranking, retry
handling, mitigations. Does not cover: new tier introduction.*

Open ROLE 2 with: "Registry verification: N tiers from ROLE 1 (T-01 through T-NN). All
downstream sections account for this count."

### Step 2A — Backpressure Propagation Trace

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

`From (T-NN)` — ROLE 1 registry identifier. If source component has no T-NN: flag REGISTRY
GAP before filling the row. `Mechanism` — queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade. Minimum two hops.

### Step 2B — User Experience Catalog

One row per ROLE 1 T-NN. No tier may be omitted.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: state the row count. Must match ROLE 1 registry count.

### Step 2C — Unprotected Burst Path Analysis

| Path-ID | Entry component | Gap reason (structural) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|-------------------------|----------------|-----------------------------|
| P-01    |                |                         |                |                             |

`T-NNs bypassed` — ROLE 1 identifiers. Gap reason must be structural.
If no path: conclusion + two T-NN controls covering every entry point.

### Step 2D — Severity Ranking

Every ROLE 1 T-NN ranked by business risk. `T-NN — [rationale]`. Top-ranked T-NN: blast
radius, failure visibility, recovery time. Coverage check: count = ROLE 1 registry count.

### Step 2E — Cascade Scenario

Concrete cascade from ROLE 1 binding constraint. T-NN identifiers throughout.
`T-NN (binding) → T-NN (causal mechanism) → T-NN (causal mechanism)`. Compounded effect.
Minimum three T-NNs. Generic cascade claims fail.

### Step 2F — Retry-After Gap Assessment

For the binding constraint tier: Retry-After handling present? If absent, name the precise
failure mode. If present, state whether callers respect it.

### Step 2G — Mitigation Prescriptions

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component: [specific named component]
- Change: [setting name + value; generic advice fails]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

This block is mandatory. It must name every downstream section by its canonical section title
and report a machine-checkable unregistered-tier count. A prose summary that describes coverage
without naming sections fails this block.

```
ROLE 1 registry count (locked):                                    [N tiers]

Section-by-section C-13 compliance check:
  Step 2A — Backpressure Propagation Trace:      T-NN IDs used:   [Y / informal names found: list]
  Step 2B — User Experience Catalog:             row count:        [N — matches registry / MISMATCH]
  Step 2C — Unprotected Burst Path Analysis:     T-NN IDs used:   [Y / informal names found: list]
  Step 2D — Severity Ranking:                    T-NN count:       [N — matches registry / MISMATCH]
  Step 2E — Cascade Scenario:                    T-NN IDs used:   [Y / informal names found: list]
  Step 2F — Retry-After Gap Assessment:          binding T-NN ref: [T-NN / informal name]

C-14: ROLE 1 declared complete before ROLE 2 opened:               [Y]
C-15: All downstream sections named in this block:                  [Y]
Unregistered tiers introduced after registry closed:                [0] (or list by name)
```

---

## V-03 — Single Axis: C-17 REGISTRY GAP as Restart Directive

**Axis:** Phrasing register — the REGISTRY GAP handling instruction changes from a pause-and-
fill-in step to a prohibitive restart directive. Any component discovered in ROLE 2 without a
T-NN from the ROLE 1 registry triggers a named SCOPE VIOLATION signal that halts the analysis.
The model may not assign a T-NN during ROLE 2 analysis. The instruction explicitly frames mid-
analysis tier discovery as evidence that ROLE 1 was incomplete, requiring ROLE 1 to be restarted
before ROLE 2 can proceed. The distinction from R3 V-01: R3 V-01 says "flag it as a REGISTRY
GAP before continuing" (the analysis continues after flagging); V-03 here says "halt — ROLE 1
was incomplete — restart before continuing" (analysis stops).

**Hypothesis:** R3 V-01 achieves C-14 PASS because tier discovery in ROLE 2 is flagged before
the analysis proceeds, but C-17 requires a stronger posture: the event is a scope violation that
invalidates the current analysis state, not a recoverable condition. "Flag and continue" permits
the model to accommodate mid-trace discoveries without signaling structural failure; "halt and
restart" treats each discovery as evidence of an incomplete enumeration phase. The prohibitive
language ("You may NOT assign a T-NN during ROLE 2") removes the accommodation pathway entirely.
Risk: under completion pressure, the model may reinterpret "restart ROLE 1" as a directive to
add a parenthetical note rather than an actual structural halt.

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
- The tier that first appeared in the backpressure trace, was assigned a T-NN mid-analysis as
  a fill-in step, and was never formally confirmed for its limit, scope, or window type —
  the analyst continued without correcting the registry, and the limit estimate became the
  documented limit that no one verified

The analysis below treats mid-phase tier discovery as a structural failure, not an extension.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  arrival-shape sensitivity). You may NOT describe caller behavior, retry responses, error
  codes seen by users, or backpressure consequences. If you find yourself writing what a flow
  author sees when a tier fires, stop — that belongs in ROLE 2.
- During ROLE 2: you may NOT introduce a new tier. You may NOT assign a T-NN to any component
  not registered in ROLE 1. If any component appears in ROLE 2 without a T-NN from the ROLE 1
  registry, this is a SCOPE VIOLATION:

  **"SCOPE VIOLATION — [component name] has no registry entry. The ROLE 1 tier enumeration
  was incomplete. Halt ROLE 2 analysis at this point. Restart ROLE 1 with this component
  included, re-complete ROLE 1, then resume ROLE 2 from the beginning of the section where
  the violation occurred."**

  Do not assign a T-NN and continue. Do not add a parenthetical limit estimate and proceed.
  Do not note the gap and move forward. The SCOPE VIOLATION requires ROLE 1 to be restarted
  and re-completed before ROLE 2 may proceed — it is a structural correction, not a fill-in
  step.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier discovery, registry assignment, limits, scope, window type, burst headroom,
bottleneck ordering, arrival-shape sensitivity. Does not cover: caller behavior or UX.*

### Step 1A — Tier Registry

Enumerate every throttle tier in the system described in the signal. This is the enumeration
commitment: every tier that exists in this system must appear in this registry before ROLE 2
opens. Assign permanent T-NN identifiers (T-01, T-02, ...).

| T-NN | Component | Limit (number + unit) | Scope | Window type | Burst headroom |
|------|-----------|----------------------|-------|-------------|----------------|
| T-01 |           |                      |       |             |                |
| T-02 |           |                      |       |             |                |
| ...  |           |                      |       |             |                |

Column definitions:
- `T-NN` — T-01, T-02, ... Permanent. Every ROLE 2 reference to a throttle tier uses this
  identifier verbatim. Informal-name-only references are untracked.
- `Limit` — number with unit. Vague labels invalid. `unknown [reason]` where reason is:
  undocumented, environment-specific, requires-runtime-measurement, signal-insufficient.
  Do not omit tiers — unknown-limit tiers receive a T-NN.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (with refill rate), concurrent-cap.
- `Burst headroom` — Y [amount] or N.

State "Tier Registry complete — N tiers registered (T-01 through T-NN). Registry is now closed.
Any component found in ROLE 2 without a T-NN from this registry is a SCOPE VIOLATION."
**Lock the registry count.**

### Step 1B — Bottleneck Ordering and Arrival-Shape Sensitivity

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason (lower cap, narrower
   scope, no burst headroom, shortest window).

2. **Hit order:** every T-NN in the order they fire at the given volume. Format:
   `T-NN (limit: X unit) — fires at Y` or `T-NN — not reached at this volume`. All T-NNs
   must appear.

3. **Arrival-shape sensitivity:** for each T-NN: SHAPE-NEUTRAL (mechanism — window type,
   token-bucket headroom) or SHAPE-SENSITIVE (numeric rate under burst arrival that triggers
   vs. numeric rate under uniform arrival that misses; window mechanism that creates the
   sensitivity).

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX per tier, burst paths, cascade, severity ranking, retry
handling, mitigations. Does not cover: new tier introduction. The registry is closed.*

Open ROLE 2 with: "Registry verification: N tiers from ROLE 1 (T-01 through T-NN). The
registry is closed. Any component in ROLE 2 without a ROLE 1 T-NN is a SCOPE VIOLATION —
halt and restart ROLE 1."

### Step 2A — Backpressure Propagation Trace

Starting from the ROLE 1 binding constraint, trace how throttling propagates outward.

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — ROLE 1 registry identifier only. If the source component has no T-NN:
  SCOPE VIOLATION — halt at this row. Do not fill From. Signal the violation as specified
  in the PHASE BOUNDARY RULES. Restart ROLE 1 before continuing.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade. Generic entries fail.
- Minimum two hops.

### Step 2B — User Experience Catalog

One row per ROLE 1 T-NN. No tier may be omitted. No informal-name-only rows.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: row count = ROLE 1 registry count. State explicitly.

### Step 2C — Unprotected Burst Path Analysis

| Path-ID | Entry component | Gap reason (structural) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|-------------------------|----------------|-----------------------------|
| P-01    |                |                         |                |                             |

`T-NNs bypassed` — ROLE 1 identifiers. If a bypassed-tier component has no T-NN:
SCOPE VIOLATION — halt and restart ROLE 1.
If no path: conclusion + two T-NN controls covering every entry point.

### Step 2D — Severity Ranking

Every ROLE 1 T-NN ranked by business risk. Every T-NN must appear.
`T-NN — [rationale]`. Top-ranked T-NN: blast radius, failure visibility, recovery time.
Coverage check: count = ROLE 1 registry count.

### Step 2E — Cascade Scenario

Concrete cascade from ROLE 1 binding constraint. T-NN identifiers throughout. If any
component appears in the cascade without a ROLE 1 T-NN: SCOPE VIOLATION — halt and restart
ROLE 1. Minimum three T-NNs with explicit causal links. Compounded effect.
`T-NN (binding) → T-NN (causal mechanism) → T-NN (causal mechanism)`.

### Step 2F — Retry-After Gap Assessment

For the binding constraint tier: Retry-After handling present? If absent, name the precise
failure mode. If present, state whether callers respect it.

### Step 2G — Mitigation Prescriptions

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component: [specific named component]
- Change: [setting name + value; generic advice fails]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**COMPLETION VERIFICATION**

```
ROLE 1 registry count (closed):                              [N tiers]
Step 2B catalog count:                                       [N rows — must match]
Step 2D ranking count:                                       [N entries — must match]
ROLE 1 complete before ROLE 2 opened:                        [Y]
SCOPE VIOLATIONS triggered in ROLE 2:                        [count or "none"]
C-17: All REGISTRY GAPSs treated as violations (not fill-ins): [Y / or list fill-in steps taken]
C-14: ROLE 1 complete before ROLE 2 opened:                  [Y]
C-13: T-NN used in 2A, 2B, 2C, 2D, 2E:                      [ ]
```

---

## V-04 — Combined: C-15 + C-16 + C-17 on Role-Sequence Baseline

**Axis:** Combined — all three new v4 criteria applied simultaneously to the R3 V-05 role-
sequence baseline. The Tier Registry gains a Load-shape verdict column (C-16) populated at
registration time. The ROLE 2 SCOPE VIOLATION directive halts analysis on any unregistered
component and requires a ROLE 1 restart (C-17). The analysis closes with a named INTEGRITY
VERIFICATION block that enumerates every downstream section by canonical name and reports a
machine-checkable unregistered-tier count (C-15). The three mechanisms are orthogonal: the
Load-shape column fires at registration, the SCOPE VIOLATION fires at any mid-phase tier
discovery, and the audit block fires at analysis close — they do not interfere.

**Hypothesis:** C-15 and C-16 compose with no structural tension: C-16 adds one column to
the registry table; C-15 adds one block at the end of the analysis. C-17 potentially interacts
with C-14: both concern phase-boundary enforcement, but C-17 is the enforcement posture (what
happens when the boundary is violated) while C-14 is the structural separation (the boundary
exists). The V-04 combination tests whether C-17's restart directive consumes token budget
that would otherwise go to C-15 audit block completeness — if the model generates the SCOPE
VIOLATION signal but then truncates the INTEGRITY VERIFICATION block, C-15 fails while C-17
passes. The combined prediction is ~108/110: one point reserved for the possibility that the
audit block is populated but some section names are abbreviated rather than canonical.

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
- The tier whose load-shape sensitivity was never classified at registration: the analyst deferred
  it to a later section, the later section was skipped under time pressure, and the burst-only
  failure mode remained undiscovered until the spike traffic event
- The mid-trace tier discovery that was silently incorporated as a fill-in step, giving the
  analysis the appearance of completeness while leaving the newly registered tier's limit as an
  estimate with no formal confirmation

The analysis below prevents all five failures. Load-shape verdicts are registered at tier
registration time. Mid-phase tier discoveries are SCOPE VIOLATIONS requiring ROLE 1 restart.
The audit block names every downstream section and reports a machine-checkable count.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences. If you find yourself writing what a flow author sees
  when a tier fires, stop — flag SCOPE DEFERRAL and continue after the role boundary.
- During ROLE 2: you may NOT introduce a new tier. You may NOT assign a T-NN to any component
  not registered in ROLE 1. If any component appears in ROLE 2 without a T-NN from the ROLE 1
  registry, this is a SCOPE VIOLATION:

  **"SCOPE VIOLATION — [component name] has no registry entry. ROLE 1 tier enumeration was
  incomplete. Halt ROLE 2 at this point. Restart ROLE 1 with [component name] included,
  re-complete ROLE 1, then resume ROLE 2 from the beginning of this section."**

  Do not assign a T-NN and continue. Do not add a parenthetical limit estimate. The SCOPE
  VIOLATION requires ROLE 1 restart — not a fill-in step.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier discovery, registry assignment, limits, scope, window type, burst headroom,
load-shape classification, bottleneck ordering, arrival-shape sensitivity. Does not cover:
caller behavior, retry handling, UX consequences, backpressure propagation.*

### Step 1A — Tier Registry

Enumerate every throttle tier. Assign permanent T-NN identifiers (T-01, T-02, ...). Populate
all columns for each tier before advancing to the next row.

| T-NN | Component | Limit (number + unit) | Scope | Window type | Load-shape verdict |
|------|-----------|----------------------|-------|-------------|-------------------|
| T-01 |           |                      |       |             |                   |
| T-02 |           |                      |       |             |                   |
| ...  |           |                      |       |             |                   |

Column definitions:
- `T-NN` — T-01, T-02, ... Permanent. Every ROLE 2 section references tiers by this identifier
  verbatim. Informal-name-only references are untracked.
- `Limit` — number with unit. Vague labels invalid. `unknown [reason]` where reason is:
  undocumented, environment-specific, requires-runtime-measurement, signal-insufficient.
  Unknown-limit tiers still receive a T-NN.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (refill rate in cell), concurrent-cap.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, decided at registration time.
  Do not defer this verdict. Every row requires a verdict before the registry closes.
  - SHAPE-NEUTRAL: throttle status identical under uniform arrival (within 10% of average
    rate) and burst arrival (same total volume in first 20% of window). State the mechanism:
    window design, token-bucket headroom, concurrent-cap insensitivity to distribution.
    Example: "token-bucket with 60-req headroom; burst depletes headroom but 600 req/min
    window cap is not exceeded; status: OK under both patterns."
  - SHAPE-SENSITIVE: throttle status differs between uniform and burst at the same total
    volume. State: (1) the numeric instantaneous rate under burst that triggers throttling;
    (2) the numeric average rate under uniform arrival that does not; (3) the window mechanism
    that creates the differential. Example: "fixed 10-sec sub-window; burst: 150 req/10s
    exceeds sub-window cap; uniform: 30 req/10s does not; mechanism: sub-window measures
    instantaneous rate, not rolling total."

State "Tier Registry complete — N tiers registered (T-01 through T-NN). Registry is closed.
ROLE 2 may not introduce new tiers — any unregistered component is a SCOPE VIOLATION."
**Lock the registry count.**

### Step 1B — Bottleneck Ordering

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason (lower cap, narrower
   scope, no burst headroom, shortest window, least token-bucket headroom).

2. **Hit order:** every T-NN in order of firing at the given volume.
   `T-NN (limit: X unit) — fires at Y` or `T-NN — not reached at this volume`. All T-NNs
   must appear.

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX per tier, burst paths, cascade, severity ranking, retry
handling, mitigations. Does not cover: new tier introduction. Registry is closed.*

Open ROLE 2 with: "Registry verification: N tiers from ROLE 1 (T-01 through T-NN). Registry
closed. Any unregistered component encountered in ROLE 2 is a SCOPE VIOLATION — halt and
restart ROLE 1."

### Step 2A — Backpressure Propagation Trace

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — ROLE 1 identifier only. Unregistered source: SCOPE VIOLATION — halt.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade. Generic entries fail.
- Minimum two hops.

### Step 2B — User Experience Catalog

One row per ROLE 1 T-NN. No tier may be omitted. No informal-name-only rows.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: row count = ROLE 1 registry count. State explicitly.

### Step 2C — Unprotected Burst Path Analysis

| Path-ID | Entry component | Gap reason (structural) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|-------------------------|----------------|-----------------------------|
| P-01    |                |                         |                |                             |

`T-NNs bypassed` — ROLE 1 identifiers. Unregistered bypassed component: SCOPE VIOLATION.
If no path: conclusion + two T-NN controls covering every entry point.

### Step 2D — Severity Ranking

Every ROLE 1 T-NN ranked by business risk. Every T-NN must appear.
`T-NN — [rationale]`. Top-ranked T-NN: blast radius, failure visibility, recovery time.
Coverage check: count = ROLE 1 registry count.

### Step 2E — Cascade Scenario

Concrete cascade from ROLE 1 binding constraint. T-NN identifiers throughout. Unregistered
component in cascade: SCOPE VIOLATION — halt and restart ROLE 1.
`T-NN (binding) → T-NN (causal mechanism) → T-NN (causal mechanism)`. Compounded effect.
Minimum three T-NNs with explicit causal links.

### Step 2F — Retry-After Gap Assessment

For the binding constraint tier: Retry-After handling present? If absent, name the precise
failure mode. If present, state whether callers respect it.

### Step 2G — Mitigation Prescriptions

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component: [specific named component]
- Change: [setting name + value; generic advice fails]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

This block is mandatory. It must name every downstream section by canonical title and report
a machine-checkable unregistered-tier count. A prose summary that describes coverage without
naming sections fails this block.

```
ROLE 1 registry count (locked):                                          [N tiers]

Section-by-section C-13 compliance:
  Step 2A — Backpressure Propagation Trace:       T-NN IDs used:        [Y / informal names: list]
  Step 2B — User Experience Catalog:              row count:             [N — matches / MISMATCH]
  Step 2C — Unprotected Burst Path Analysis:      T-NN IDs used:        [Y / informal names: list]
  Step 2D — Severity Ranking:                     T-NN count:           [N — matches / MISMATCH]
  Step 2E — Cascade Scenario:                     T-NN IDs used:        [Y / informal names: list]
  Step 2F — Retry-After Gap Assessment:           binding T-NN by ID:   [Y / informal name]

C-14: ROLE 1 complete before ROLE 2 opened:                              [Y]
C-15: All downstream sections named above:                               [Y]
C-16: Load-shape verdict in registry column at registration:             [Y / tiers with deferred verdicts: list]
C-17: SCOPE VIOLATIONS treated as restarts (not fill-ins):               [Y / fill-in steps taken: list]
Unregistered tiers introduced after registry closed:                     [0] (or list by name)
```

---

## V-05 — Maximum Density: V-04 + Three-Failure Inertia Story + Extended Enforcement

**Axis:** Combined — V-04's full structure (C-16 shape column + C-17 restart directive + C-15
named audit block) extended with an inertia story that names three specific failure patterns —
TIER DRIFT, SHAPE BLINDNESS, and MID-TRACE DISCOVERY — as the production incidents that motivated
the three new v4 criteria. The inertia story names the incident before the structural mechanism
that prevents it, so the model understands the causal chain between failure mode and enforcement.
The INTEGRITY VERIFICATION block is extended: each section line includes a compliance indicator
for the relevant criterion (C-13 for section-level T-NN threading; C-16 for shape verdict at
registration; C-17 for violation posture). The combination tests whether the narrative motivation
and the structural enforcement reinforce each other or create token-budget competition.

**Hypothesis:** R3 V-05 achieved the highest R3 composite because the inertia story made the
analysis feel urgent — the model was searching for the specific failure patterns the story named
("tier drift", "mixed-perspective sections"). V-05 here extends that mechanism to the three v4
failure patterns. TIER DRIFT is the C-13/C-14 failure (already established in R3). SHAPE
BLINDNESS is the C-16 failure: the analyst acknowledged load-shape sensitivity in prose but never
embedded it in the registry, so downstream sections could not reference a shape verdict they never
had. MID-TRACE DISCOVERY is the C-17 failure: the analyst accommodated a late-discovered tier with
a fill-in T-NN, the tier's limit was estimated rather than confirmed, and the estimate became
documentation. Naming all three in the inertia story commits the model to finding them; the
structural mechanisms in the prompt prevent them. Risk: three named failures plus V-04's full
structure may create token-budget pressure on the audit block — if the model generates an
abbreviated INTEGRITY VERIFICATION that names only some sections, C-15 fails. The explicit
constraint "name all six downstream sections; abbreviation or omission fails this block" is
the compensating mechanism.

---

**THE THREE ANALYSIS FAILURES THAT MAKE THROTTLE DOCUMENTATION UNAUDITABLE**

Most throttle analyses fail in the same three ways after the analysis is written — not because
they found the wrong gaps, but because the analysis itself cannot be audited for completeness.

**Failure 1: Tier drift.** The team enumerated five tiers. In the cascade scenario, three are
referenced by component label ("the SharePoint connector", "the API Management gateway"). In
the UX catalog, two are referenced by error code name ("the 429 from the connector layer"). The
risk ranking names them differently again. There is no common identifier threading the sections.
When a reviewer tries to verify that the UX catalog covers all five tiers, they cannot —
the names are inconsistent and there is no registry to audit against. Two tiers have no UX
entry; the gap is invisible.

**Failure 2: Shape blindness.** The analyst noted that one tier had burst-sensitive behavior in
a paragraph after the registry table. The note was prose: "this tier may behave differently under
burst arrival." The downstream load-shape section was skipped under time pressure. The registry
row had no shape verdict. Six months later, a burst traffic event triggered that tier at 4x the
rate the uniform-arrival analysis showed — the tier's burst behavior had never been formally
registered, so no mitigation existed. The shape verdict existed in a prose note that no
subsequent reviewer connected to the tier's registry entry.

**Failure 3: Mid-trace discovery.** The analyst was tracing backpressure from the binding
constraint. A new component appeared — its rate limit had not been enumerated. The analyst
added "T-06: estimated 100 req/min" in parentheses inside the backpressure trace and continued.
T-06 was never added to the registry table. Its limit was an estimate. The UX catalog did not
include it. The severity ranking did not include it. The fill-in step created the appearance of
a complete analysis while leaving an unconfirmed tier undocumented.

The analysis below prevents all three failures. The Tier Registry includes a Load-shape verdict
column populated at registration — Failure 2 is impossible if the registry is complete. The
registry is closed before ROLE 2 opens and any mid-trace discovery is a SCOPE VIOLATION
requiring ROLE 1 restart — Failure 3 is a structural halt, not an accommodation. The audit
block names every downstream section by canonical title and reports a machine-checkable
unregistered-tier count — Failure 1 is verifiable at close.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences. If you find yourself writing what a flow author sees
  when a tier fires, stop — flag SCOPE DEFERRAL [ROLE 2] and continue after the boundary.
  This prevents Failure 1 (tier drift): caller analysis mixed into ROLE 1 produces interleaved
  sections that cannot be audited for perspective separation.
- During ROLE 2: you may NOT introduce a new tier. You may NOT assign a T-NN to any component
  not registered in ROLE 1. If any component appears in ROLE 2 without a T-NN from the ROLE 1
  registry, this is a SCOPE VIOLATION — Failure 3 is occurring:

  **"SCOPE VIOLATION (Failure 3 — mid-trace discovery) — [component name] has no registry
  entry. ROLE 1 was incomplete. Halt ROLE 2 at this point. Restart ROLE 1 with [component
  name] included, re-complete ROLE 1 (including its Load-shape verdict), then resume ROLE 2
  from the beginning of this section."**

  Do not assign a T-NN and continue. Do not add a parenthetical limit estimate. The SCOPE
  VIOLATION requires ROLE 1 restart — a fill-in step is exactly Failure 3.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier discovery, registry assignment, limits, scope, window type, burst headroom,
load-shape classification (Failure 2 prevention), bottleneck ordering.*
*Does not cover: caller behavior, retry handling, UX consequences, backpressure propagation.*

### Step 1A — Tier Registry

Enumerate every throttle tier in the system. This is the enumeration commitment — every tier
that exists in this system must appear in this registry before ROLE 2 opens. Assign permanent
T-NN identifiers (T-01, T-02, ...). Populate all columns before advancing to the next tier.

| T-NN | Component | Limit (number + unit) | Scope | Window type | Load-shape verdict |
|------|-----------|----------------------|-------|-------------|-------------------|
| T-01 |           |                      |       |             |                   |
| T-02 |           |                      |       |             |                   |
| ...  |           |                      |       |             |                   |

Column definitions:
- `T-NN` — T-01, T-02, ... Permanent. Every ROLE 2 reference uses this identifier verbatim.
  Informal-name-only references are the tier-drift pattern (Failure 1) — they are untracked.
- `Limit` — number with unit. Vague labels invalid. `unknown [reason]` where reason is:
  undocumented, environment-specific, requires-runtime-measurement, signal-insufficient.
  Unknown-limit tiers still receive a T-NN — omitting them is a registry gap.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (include refill rate in this cell),
  concurrent-cap.
- `Load-shape verdict` — Failure 2 prevention. Classify each tier SHAPE-NEUTRAL or
  SHAPE-SENSITIVE at registration time. Do not defer this verdict to a downstream section
  or to a prose note following the registry. Every row requires a verdict before the registry
  is declared complete. Deferring the shape verdict is the mechanism by which Failure 2 occurs.
  - SHAPE-NEUTRAL: throttle status identical under uniform arrival (within 10% of average
    rate throughout the measurement window) and burst arrival (same total volume concentrated
    in the first 20% of the window, producing 5x the average instantaneous rate). State the
    specific mechanism: window design that rolls over sub-window peaks, token-bucket headroom
    that absorbs bursts, concurrent-cap that does not distinguish arrival distribution.
    Example: "token-bucket, 60-req headroom, 10 req/sec refill; burst depletes headroom in
    6 sec but 600 req/min total cap is not exceeded; identical status under both patterns."
  - SHAPE-SENSITIVE: throttle status differs at the same total volume depending on arrival
    pattern. State: (1) the numeric instantaneous rate under burst that triggers throttling;
    (2) the numeric average rate under uniform arrival that does not trigger it; (3) the window
    mechanism — the specific property of the window design that punishes instantaneous rate
    regardless of total volume. Example: "fixed 10-sec sub-window; burst: 150 req/10s exceeds
    150 req/10s sub-window cap; uniform: 30 req/10s does not; mechanism: sub-window is a
    hard instantaneous-rate cap, not a rolling average."
  - A shape label without numeric rates (e.g., "SHAPE-SENSITIVE: burst causes issues")
    satisfies the column header visually but not substantively — both numeric values are
    required.

State: **"Tier Registry complete — N tiers registered (T-01 through T-NN). Registry is closed.
Load-shape verdicts recorded for all N tiers. Any component found in ROLE 2 without a T-NN
from this registry is a SCOPE VIOLATION (Failure 3). The registry count is locked."**

### Step 1B — Bottleneck Ordering

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason (lower absolute cap,
   narrower scope, no burst headroom, shortest window, least token-bucket headroom). State all
   that apply.

2. **Hit order:** every T-NN in the order they fire at the given volume.
   `T-NN (limit: X unit) — fires at Y req/min` or `T-NN — not reached at this volume`.
   Every T-NN from Step 1A must appear.

State "ROLE 1 complete" before opening ROLE 2. The registry is locked; the bottleneck is
identified; ROLE 2 may now begin caller analysis on the closed registry.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation (Failure 1 prevention: T-NN throughout), UX per tier,
burst paths, cascade, severity ranking, retry handling, mitigations.*
*Does not cover: new tier introduction. Registry is closed. Failure 3 prevention is active.*

Open ROLE 2 with: **"Registry verification: N tiers from ROLE 1 (T-01 through T-NN). Registry
is closed. Load-shape verdicts recorded for all N tiers. Any unregistered component is a SCOPE
VIOLATION (Failure 3) — halt and restart ROLE 1. Failure 1 prevention: every tier reference
in ROLE 2 uses T-NN identifiers, not informal component names."**

### Step 2A — Backpressure Propagation Trace

*(Failure 1 check: every `From` cell must contain a T-NN. Informal names without T-NN anchors
are untracked — they are how Failure 1 manifests in this section.)*

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — ROLE 1 registry identifier only. Unregistered source: SCOPE VIOLATION
  (Failure 3) — halt at this row, signal the violation, restart ROLE 1.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade. Generic entries ("degraded", "impacted") fail this column.
- Minimum two hops.

### Step 2B — User Experience Catalog

*(Failure 1 check: one row per T-NN. The row count verifiable against the registry is how
Failure 1 is detected — a missing row means a tier with no UX entry.)*

One row per ROLE 1 T-NN. No tier may be omitted. No informal-name-only rows.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: row count = ROLE 1 registry count. State explicitly.

### Step 2C — Unprotected Burst Path Analysis

*(Failure 3 check: any path component that has no T-NN is a SCOPE VIOLATION.)*

| Path-ID | Entry component | Gap reason (structural) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|-------------------------|----------------|-----------------------------|
| P-01    |                |                         |                |                             |

`T-NNs bypassed` — ROLE 1 identifiers. Unregistered component: SCOPE VIOLATION — halt and
restart ROLE 1. `Gap reason` must be structural (not generic). If no path: conclusion + two
T-NN controls covering every entry point.

### Step 2D — Severity Ranking

*(Failure 1 check: every T-NN must appear. Missing tiers indicate drift — they appeared in
earlier sections under informal names that could not be tracked to the registry.)*

Every ROLE 1 T-NN ranked by business risk. Every T-NN must appear. `T-NN — [rationale]`.
Top-ranked T-NN: blast radius, failure visibility, recovery time. Coverage check: count =
ROLE 1 registry count. State explicitly.

### Step 2E — Cascade Scenario

*(Failure 1 and Failure 3 check: this section has historically been where tier drift and
mid-trace discovery both manifest — narrative prose makes both failures easy to miss.)*

Concrete cascade from ROLE 1 binding constraint. T-NN identifiers throughout — no informal
names. Unregistered component: SCOPE VIOLATION — halt and restart ROLE 1.
`T-NN (binding, limit: X) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
State the compounded throughput/error-rate effect across all T-NN entries. Minimum three
T-NNs with explicit causal links.

### Step 2F — Retry-After Gap Assessment

For the ROLE 1 binding constraint tier (reference by T-NN): is Retry-After handling present
in the caller? If absent, name the precise failure mode (retry storm, missing exponential
backoff, silent quota exhaustion, immediate re-queue within same throttle window). If present,
state whether the caller respects it.

### Step 2G — Mitigation Prescriptions

*(These prescriptions close the gaps that Failures 1, 2, and 3 leave open in production.)*

**GAP-01:** Highest-priority gap from any Step 2A–2F finding
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component — not a layer]
- Change: [setting name + value, API parameter + value, or retry policy with concrete
  parameters; generic advice fails; e.g., "configure the Power Automate concurrency control
  on the trigger to maxConcurrentRuns: 10 to cap the per-flow parallel execution that
  exhausts T-02's concurrent-connection limit"]
- Expected outcome: [quantified or observable behavioral change after fix]
- Tradeoff: [specific cost — latency increase, throughput ceiling reduction, added dependency]

**GAP-02:** Second-priority gap
- Gap: [T-NN or Path-ID, failure mode, step]
- Component to modify: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

This block is mandatory. Name all six downstream sections by canonical title. Abbreviation or
omission of any section fails this block. Report a machine-checkable unregistered-tier count.

```
ROLE 1 registry count (locked):                                             [N tiers]

Section-by-section C-13 compliance (Failure 1 audit):
  Step 2A — Backpressure Propagation Trace:       T-NN IDs used:           [Y / informal names: list]
  Step 2B — User Experience Catalog:              row count:                [N — matches / MISMATCH]
  Step 2C — Unprotected Burst Path Analysis:      T-NN IDs used:           [Y / informal names: list]
  Step 2D — Severity Ranking:                     T-NN count:              [N — matches / MISMATCH]
  Step 2E — Cascade Scenario:                     T-NN IDs used:           [Y / informal names: list]
  Step 2F — Retry-After Gap Assessment:           binding T-NN by ID:      [Y / informal name]

Failure 2 audit (C-16):
  Load-shape verdict in registry at registration:                           [Y / tiers with deferred verdicts: list]
  Shape-sensitive tiers numeric rates recorded:                             [Y / tiers missing numeric rates: list]

Failure 3 audit (C-17):
  SCOPE VIOLATIONS triggered in ROLE 2:                                     [count or "none"]
  All violations treated as restarts (not fill-ins):                        [Y / fill-in steps taken: list]
  Unregistered tiers introduced after registry closed:                      [0] (or list by name)

C-14: ROLE 1 declared complete before ROLE 2 opened:                        [Y]
C-15: All six downstream sections named in this block:                      [Y]
```
