# flow-throttle Variate — Round 3 (rubric v3 — C-13 tier-ID threading, C-14 perspective separation)
**Date:** 2026-03-15
**Rubric:** v3 (C-01 through C-14; 5 essential / 3 recommended / 6 aspirational)
**New in v3:** C-13 (tier-ID threading across all downstream sections), C-14 (perspective-separated analysis — analyst completes before caller begins)
**Baseline ceiling:** R2 V-05 — all C-01 through C-11 reliable under structural enforcement; C-12 passes with T-NN tables; C-13/C-14 are new and untested

---

## Round 3 State Analysis: What R2 Established vs. What R3 Must Add

**R2 confirmed (under structural enforcement):**
- C-01 (bottleneck localization): reliable when bottleneck is a named section with causal reason.
- C-02 (backpressure 2+ hops): reliable when minimum-hop count is explicit; silently regresses
  to one hop under prose-only instructions.
- C-03 (rate-limit tier enumeration, numeric): reliable under table-column enforcement; vague
  labels survive prose-only instructions without a column definition prohibiting them.
- C-04 (UX per tier): reliable when each tier has a required row; fails when UX is an
  unanchored prose paragraph.
- C-05 (unprotected burst path): reliable under a dedicated section with gap-reason requirement.
- C-06 (retry-after handling): reliable when the first-hit tier has an explicit row with
  consequence stated.
- C-07 (cascade 3+ tiers): reliable when minimum tier count and causal-link requirement are
  explicit.
- C-08 (quantified thresholds): reliable when the primary bottleneck section requires a number.
- C-09 (mitigations with tradeoffs): passes under structural enforcement (named setting required,
  generic advice explicitly rejected); fails in prose-optional sections.
- C-10 (load-shape sensitivity, numeric comparison): passes with burst/uniform split columns
  in TABLE A; fails without an embedded arrival-pattern comparison mechanism.
- C-11 (tier-complete severity ranking): passes when the ranking section requires all T-NN
  entries to appear; fails when ranking is prose without a per-tier anchor.
- C-12 (cross-section tier integrity verification): passes with explicit count-checks across
  sections referencing the registry.

**R2 gap (what v3 now scores):**

C-13 — Tier-ID threading: R2 T-NN table schemas ensured numeric limits (C-03) and drove C-12
(count checks), but did not require downstream sections to reference tiers by T-NN identifier.
Prose sections (CASCADE SCENARIO, RISK RANKING) named tiers by component label ("SharePoint
connector", "API Management gateway") without T-NN anchors. C-13 requires that all four
downstream sections — UX catalog, backpressure trace, cascade, severity ranking — use the
registry identifiers. Tiers appearing only by informal name are untracked references that break
audit continuity.

C-14 — Perspective-separated analysis: R2 V-03 (conversational register) and R2 V-01
(role-sequenced table schemas) interleaved tier enumeration with caller analysis. In V-03,
tiers were discovered and their caller behavior described in the same paragraph. In R2 V-01's
table-per-section design, the UX TABLE appeared immediately after the tier row, co-locating
limit enumeration with error-code description. C-14 requires that the tier enumeration section
is structurally complete — all tiers registered, all limits assigned — before any caller
behavior section opens. Sections where the model discovers a new tier while tracing backpressure
(and records its limit mid-trace) fail C-14 regardless of whether the tier is eventually covered.

**Three questions this round asks:**

Q1 (V-01, V-05): Does strict role separation — enforced by a PHASE BOUNDARY rule that prohibits
new tier introduction in Phase 2 — produce C-14 compliance structurally, or does the model
"discover" tiers in Phase 2 and silently add them to the Phase 1 registry retrospectively?

Q2 (V-02, V-05): Does a formal registry gate table — with a "Registry Complete" declaration
required before any downstream table opens — produce C-13 compliance because downstream tables
structurally require T-NN values, not just informal name references?

Q3 (V-04): When structural scaffolding is removed (conversational register, no table schemas,
no T-NN instruction), do C-13 and C-14 fail predictably, confirming that both criteria require
structural enforcement to pass?

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis | Predicted composite |
|-----------|------|------------|---------------------|
| V-01 | Role sequence — Tier Analyst role completes entirely before Caller Perspective role opens; prohibition rules prevent new tier introduction in Phase 2 | Perspective separation is C-14's mechanism. Phase 2's T-NN-only reference rule enforces C-13. Risk: model retrospectively edits Phase 1 if a Phase 2 trace reveals an uncovered tier | ~95/110 |
| V-02 | Output format — tier registry is a formally gated table with a "Registry Complete" declaration; all downstream tables require a T-NN column drawn verbatim from the registry | Registry-as-gate makes C-13 structurally enforced (downstream tables cannot fill their T-NN column without registry values). C-14 is implicit because the registry phase must close before analysis tables open. Risk: prose sections (cascade, ranking) may still use informal names if only tables are schema-enforced | ~92/110 |
| V-03 | Lifecycle emphasis — each section carries explicit SCOPE COVERS / SCOPE EXCLUDES declarations; Phase 1 EXCLUDES caller behavior; Phase 2+ EXCLUDES new tier discovery | Prohibition rules in section headers separate perspectives (C-14) and enforce ID consistency (C-13) without requiring role personas. Tests whether scope headers alone are sufficient without full role-sequence structure | ~88/110 |
| V-04 | Phrasing register — conversational/imperative; no table schemas, no T-NN instruction, no formal phase names | Expected to produce C-01 through C-12 but fail C-13 and C-14. Establishes the degradation baseline when structural scaffolding is removed | ~72/110 |
| V-05 | Combined: registry gate (V-02) + role separation (V-01) + extended inertia framing naming tier-drift and mixed-perspective sections as the two production failure patterns | Inertia frame motivates C-13 and C-14 by naming the incidents they prevent; registry gate enforces C-13 structurally; role separation enforces C-14 structurally. Full 14-criterion coverage with both structural and motivational mechanisms | ~107/110 |

---

## V-01 — Role Sequence: Strict Analyst-First Perspective Separation

**Axis:** Role sequence — the analysis divides into two named roles with explicit phase
boundaries and prohibition rules. ROLE 1 (Tier Analyst) covers all tier-side analysis: registry
construction, numeric limits, scope, bottleneck ordering, arrival-shape sensitivity. ROLE 2
(Caller Perspective) covers all caller-side analysis: backpressure propagation, UX consequences,
retry handling, cascade scenarios, mitigations. A prohibition rule at the Phase 1 / Phase 2
boundary enforces that: (1) no caller behavior is stated in Phase 1; (2) no new tiers are
introduced in Phase 2. All Phase 2 references to throttle tiers must use the T-NN identifiers
assigned in Phase 1.

**Hypothesis:** C-14 fails when tier discovery and caller analysis are interleaved — the model
encounters a new component while tracing backpressure, assigns it a limit mid-trace, and the
tier never appears in a formal registry. Strict role separation makes the failure mode
structural: if Phase 2 contains a tier with no T-NN identifier, the prohibition rule flags it.
C-13 is enforced by the same prohibition — informal name references in Phase 2 are disallowed,
making T-NN threading the only compliant reference style. Risk: the model may use Phase 2
observations to "discover" tiers that should have been in Phase 1, then retroactively edit
Phase 1. The Phase 1 registry count lock (stated before Phase 2 opens) prevents this.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: you may describe tier properties (limits, scope, window type, hit order).
  You may NOT describe caller behavior, retry responses, error codes seen by users, or
  backpressure consequences. If you find yourself writing what a flow author sees when a tier
  fires, stop — that belongs in ROLE 2.
- During ROLE 2: you may describe how callers react to throttle signals, what users observe,
  how failures propagate, and how to fix gaps. You may NOT introduce a new tier that was not
  registered in ROLE 1. If a component appears in a backpressure trace or cascade scenario
  that has no T-NN identifier from ROLE 1, flag it as a REGISTRY GAP before continuing.
  Every tier reference in ROLE 2 must use the T-NN identifier assigned in ROLE 1 — informal
  name references without a T-NN anchor are untracked.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier registry, numeric limits, scope, bottleneck ordering, arrival-shape sensitivity.*
*Does not cover: caller behavior, retry handling, UX consequences, backpressure propagation.*

### Step 1A — Tier Registry

Enumerate every throttle tier in the system described in the signal. Assign a permanent
Tier-ID (T-01, T-02, ...) to each tier. For each tier record:

- **Tier-ID** — T-01, T-02, ... These identifiers are permanent. Every downstream ROLE 2
  section that references a throttle tier must use these identifiers verbatim.
- **Component** — the specific named component enforcing this limit.
- **Limit** — a number with a unit (e.g., 600 req/min, 10 concurrent connections, 100k tokens
  per 10 min). A vague label ("limited", "throttled") is not a limit. If the value cannot be
  confirmed, write `unknown [reason]` where reason is one of: undocumented,
  environment-specific, requires-runtime-measurement, signal-insufficient. Do not omit any
  tier — tiers with unknown limits still receive a T-NN identifier.
- **Scope** — per-user, per-connection, per-tenant, global.
- **Window type** — sliding, fixed-minute, token-bucket (with refill rate), or concurrent-cap.

State "Tier Registry complete — N tiers registered" before continuing to Step 1B.
**Lock the registry count.** ROLE 2 will verify that every section accounts for all N tiers.

### Step 1B — Bottleneck Ordering and Arrival-Shape Sensitivity

Using the Step 1A registry and the given request volume, determine:

1. **Binding constraint:** which T-NN is the first to throttle at the given volume under
   uniform arrival? State the T-NN, the numeric limit exceeded, and the causal reason this
   tier binds before all others (lower absolute cap, narrower scope, no burst headroom,
   shortest window).

2. **Hit order:** list all registry tiers in the order they fire at the given volume under
   uniform arrival. Format: `T-NN (limit: X unit) — fires at Y req/min; T-NN — not reached
   at this volume`. Every T-NN from Step 1A must appear in this list.

3. **Arrival-shape sensitivity:** for each T-NN, does arrival pattern (uniform vs. burst)
   change its throttle status at the given volume?
   - Uniform: requests arrive within 10% of average rate throughout the measurement window.
   - Burst: same total volume arrives in the first 20% of the window (5x instantaneous rate).
   - For each T-NN: mark SHAPE-NEUTRAL (status identical under both patterns — state the
     mechanism: window type, token-bucket headroom) or SHAPE-SENSITIVE (status differs —
     state the exact rate differential and the mechanism that causes it).

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX consequences, retry handling, burst paths, cascade,*
*severity ranking, mitigations.*
*Does not cover: new tier introduction. Check each tier reference against the ROLE 1 registry.*

**Open with a registry verification:** state the ROLE 1 registry count (N tiers). Every
table and section below that catalogs per-tier data must account for all N tiers.

### Step 2A — Backpressure Propagation Trace

Starting from the ROLE 1 binding constraint, trace how throttling propagates outward.

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From` must use a T-NN from the ROLE 1 registry. If a source component has no T-NN,
  flag REGISTRY GAP before filling the row.
- `Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
  dependency-stall, timeout-cascade. Generic entries ("degraded", "affected", "impacted")
  are not mechanisms and fail this column.
- Minimum two hops.

### Step 2B — User Experience Catalog

One row per T-NN from the ROLE 1 registry. No tier may be omitted.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|------------------------|-------------------------------|
| T-01 |                     |                           |                   |                        |                               |
| T-02 |                     |                           |                   |                        |                               |
| ...  |                     |                           |                   |                        |                               |

If a tier produces no user-visible signal, state that explicitly in the "Error code or signal"
column — do not omit the row.

**Coverage check:** state the row count. Must match ROLE 1 registry count.

### Step 2C — Unprotected Burst Path Analysis

Identify any path where burst traffic enters the system without encountering a rate limit.

| Path-ID | Entry component | Gap reason (specific structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|----------------------------------------------|----------------|-----------------------------|
| P-01    |                |                                              |                |                             |

- `T-NNs bypassed` must use Tier-IDs from the ROLE 1 registry.
- `Gap reason` must be structural: missing connector policy, trigger type exempt from queuing,
  endpoint that bypasses the gateway layer, no concurrency cap on this path.

If no unprotected path exists: state the conclusion and cite at least two T-NN controls that
collectively cover every entry point. Use T-NN identifiers for the controls.

### Step 2D — Severity Ranking and Cascade Scenario

**Severity ranking:** rank all ROLE 1 registry tiers by business risk, highest to lowest.
Every T-NN must appear in the ranking. For each entry: `T-NN: [rationale sentence]`.
For the top-ranked tier, additionally state: blast radius, failure visibility (silent vs.
explicit), recovery time.

**Coverage check:** count the T-NN entries in the ranking. Must match ROLE 1 registry count.

**Cascade scenario:** trace one concrete scenario starting from the ROLE 1 binding constraint.
Use T-NN identifiers throughout.
- `T-NN` (binding): what it throttles, numeric limit, when it fires
- Causal link to `T-NN`: the mechanism by which binding-tier throttling causes this failure
- Causal link to `T-NN`: the mechanism by which the second failure causes a third
- Compounded throughput/error-rate effect across all three T-NN entries

Minimum three T-NN entries in the cascade. Generic claims ("could cascade") do not satisfy
this section.

### Step 2E — Mitigation Prescriptions

For at least two gaps identified in ROLE 2, prescribe a specific change. Generic advice fails
this section — name the setting, the parameter, the value.

**GAP-01:**
- Gap: [T-NN or Path-ID from above, failure mode, which step surfaced it]
- Component to modify: [specific named component — not a layer, the specific element]
- Change: [setting name + value, or API parameter + value, or retry policy with concrete
  parameters; e.g., "Configure the PA flow retry policy to exponential backoff starting at
  30 seconds with a 0.2 jitter coefficient, reading the Retry-After header value and using
  it as the base delay when present"]
- Expected outcome: [quantified or observable change after the fix is applied]
- Tradeoff: [what this setting costs — increased latency, reduced throughput ceiling, added
  operational complexity]

**GAP-02:**
- Gap: [T-NN or Path-ID from above, failure mode, which step surfaced it]
- Component to modify: [specific named component]
- Change: [setting name + value or implementation pattern]
- Expected outcome: [quantified or observable change]
- Tradeoff: [specific cost]

---

**COMPLETION VERIFICATION**

```
ROLE 1 registry count:          [N tiers]
Step 2B catalog count:          [N rows — must match]
Step 2D ranking count:          [N entries — must match]
ROLE 1 complete:                [ ]
ROLE 2 complete:                [ ]
C-14 check — new tiers in ROLE 2: [0 unregistered tiers, or flag REGISTRY GAP entries]
C-13 check — T-NN used in 2A, 2B, 2C, 2D: [ ]
```

---

## V-02 — Output Format: Registry Table as Structural Gate

**Axis:** Output format — the Tier Registry is a named, formally gated table. A "Registry
Complete" declaration must appear after the table before any downstream analysis table opens.
All downstream tables (backpressure trace, UX catalog, burst paths, severity ranking) have
a T-NN column as their first column, with values drawn verbatim from the registry. The T-NN
column in downstream tables cannot be filled with informal names — the column header enforces
registry-consistent identifiers structurally.

**Hypothesis:** When the registry is a schema-enforced gate rather than a prose instruction,
C-13 becomes a column compliance problem rather than a memory problem. The model fills the
T-NN column from the registry naturally — it has no other value to put there. C-14 is
implicit: the registry table must be declared complete before the first analysis table opens,
so tier discovery cannot happen inside an analysis table. Risk: prose sections (cascade
scenario, load-shape analysis) that do not have a T-NN column may still reference tiers by
informal name; explicit T-NN instruction for prose sections is the compensating mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Produce the registry and the five analysis sections below in order. The registry must be
declared complete before any analysis section opens. Do not substitute prose for any table.
Every cell must be filled; write `unknown [reason]` only if the value is genuinely
undocumentable, where reason is one of: undocumented, environment-specific,
requires-runtime-measurement, signal-insufficient.

---

**TIER REGISTRY**

*(Complete this table first. Declare it complete before opening any analysis section.)*

| T-NN | Component | Limit (number + unit) | Scope | Window type | Burst headroom |
|------|-----------|----------------------|-------|-------------|----------------|
| T-01 |           |                      |       |             |                |
| T-02 |           |                      |       |             |                |
| ...  |           |                      |       |             |                |

Column definitions:
- `T-NN` — T-01, T-02, ... Permanent identifiers for this analysis. Every cell in every
  downstream table that references a throttle tier must use these identifiers verbatim.
  Informal name references without a T-NN anchor are untracked and fail C-13.
- `Limit` — a number with a unit. "Limited" or "throttled" without a number is invalid.
- `Window type` — sliding, fixed-minute, token-bucket (with refill rate), concurrent-cap.
- `Burst headroom` — whether the window absorbs short bursts above average rate (Y [amount]
  or N).

When every tier has a T-NN and a limit (or `unknown [reason]`), state:
**"Registry complete — N tiers. T-01 through T-NN assigned."**
Do not open any analysis section before this declaration.

---

**ANALYSIS SECTION 1 — THROTTLE INVENTORY WITH ARRIVAL PATTERN**

*(Opens after registry is declared complete.)*

| T-NN | Binding? | Limit hit at volume? | STATUS-UNIFORM | STATUS-BURST | Hit order |
|------|----------|---------------------|----------------|--------------|-----------|
| T-01 |          |                     |                |              |           |
| T-02 |          |                     |                |              |           |
| ...  |          |                     |                |              |           |

Column definitions:
- `T-NN` — drawn verbatim from the Tier Registry. No additions. No informal names.
- `Binding?` — Y for the single first-hit tier under uniform arrival. At most one Y.
- `STATUS-UNIFORM` — OK / HIT / SAT when requests arrive within 10% of average rate.
- `STATUS-BURST` — OK / HIT / SAT when same total volume arrives in first 20% of window
  (5x instantaneous rate). At least one T-NN must show a STATUS-BURST different from
  STATUS-UNIFORM. If all statuses match, the `Burst headroom` column in the Registry must
  explain the specific mechanism making this system arrival-shape neutral.
- `Hit order` — the sequence in which this tier fires at the given volume (1 = first, 2 =
  second, "not reached" if volume does not hit this tier).

After the table, in one paragraph: state the binding T-NN, the numeric limit exceeded, and the
causal reason this tier is first (lower cap, narrower scope, shortest window, no burst
headroom).

---

**ANALYSIS SECTION 2 — BACKPRESSURE PROPAGATION TRACE**

*(Source: the binding T-NN from Section 1. Minimum two hops.)*

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — must be a T-NN from the Tier Registry. If a source component has no T-NN,
  it is a registry gap — flag it and assign the next available T-NN before filling the row.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade. Generic entries fail this column.

---

**ANALYSIS SECTION 3 — USER EXPERIENCE CATALOG**

*(One row per T-NN in the Tier Registry. No tier may be omitted.)*

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: state the row count. Must match the Tier Registry count.

---

**ANALYSIS SECTION 4 — SEVERITY RANKING AND CASCADE SCENARIO**

**Severity ranking** — rank all T-NN entries from the Tier Registry by business risk.
Every T-NN must appear in the ranking. Format: `T-NN — [rationale sentence]`.
For the top-ranked T-NN: additionally state blast radius, failure visibility, recovery time.
Coverage check: count T-NN entries in the ranking against the Tier Registry count.

**Cascade scenario** — trace one concrete cascade starting from the Section 1 binding T-NN.
Use T-NN identifiers throughout — informal names without T-NN anchors are untracked references.
- T-NN (binding): limit, when it fires
- → T-NN: causal mechanism
- → T-NN: causal mechanism
- Compounded effect: throughput/error-rate impact across all three T-NN entries
Minimum three T-NN entries.

**Load-shape note** — for each SHAPE-SENSITIVE T-NN from Section 1: state the numeric rate
under burst arrival that the uniform test never reached, the window mechanism that creates the
sensitivity, and what the user observes during the burst that does not appear under uniform load.

---

**ANALYSIS SECTION 5 — BURST PATHS AND MITIGATION PRESCRIPTIONS**

**Unprotected burst paths:**

| Path-ID | Entry component | Gap reason | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|------------|----------------|-----------------------------|
| P-01    |                |            |                |                             |

`T-NNs bypassed` must use Tier Registry identifiers. If no path exists: state the conclusion
and cite at least two T-NN controls as evidence.

**Mitigation prescriptions** — for the two highest-priority gaps from Sections 2 through 5:

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, which section surfaced it]
- Component: [specific named component]
- Change: [setting name + value, or API parameter + configuration — not generic advice]
- Outcome: [quantified or observable]
- Tradeoff: [specific cost of this change]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, which section surfaced it]
- Component: [specific named component]
- Change: [setting name + value or implementation pattern]
- Outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

```
Tier Registry count:              [N]
Section 1 row count:              [N — must match]
Section 3 row count:              [N — must match]
Section 4 ranking count:          [N — must match]
C-13: T-NN used in S2, S3, S4:   [ ] (all four downstream sections)
C-14: Tier Registry declared complete before Section 1 opened: [ ]
Registry gaps flagged in S2 (if any): [count or "none"]
```

---

## V-03 — Lifecycle Emphasis: Scope Boundary Declarations

**Axis:** Lifecycle emphasis — each phase carries explicit SCOPE COVERS and SCOPE EXCLUDES
declarations at the section header level. Phase 1 explicitly excludes caller behavior, retry
consequences, and user-visible error signals. Phases 2 through 5 explicitly exclude new tier
introduction — any tier that appears without a T-NN identifier from Phase 1 is a registry gap
and must be flagged before the section continues.

**Hypothesis:** When scope boundaries are declared in section headers rather than embedded in
preamble instructions, the model cannot "forget" them as it moves through the analysis —
every section opens with a reminder of what it covers and what it does not. This achieves
C-14 (tier enumeration complete before caller analysis opens) and C-13 (all tier references
downstream use Phase 1 T-NN identifiers) without requiring full role-persona separation.
C-14 is tested more precisely than in V-01: the scope exclusion for Phase 1 prevents caller
behavior even if the model would naturally include it as "helpful context." Risk: the model
may treat SCOPE EXCLUDES as advisory rather than mandatory — the "flag as SCOPE VIOLATION and
stop" instruction at each exclusion boundary is the enforcement mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Execute the phases below in order. Each phase opens with a SCOPE declaration. If you find
yourself writing content that belongs in a different phase's scope, stop — flag it as a
SCOPE DEFERRAL, note which phase it belongs to, and continue. Do not merge phases.

---

**PHASE 1 — TIER ENUMERATION AND LIMIT REGISTRY**

> SCOPE COVERS: tier discovery, component names, numeric rate limits, scope definitions,
> window types, burst headroom, arrival-shape analysis, bottleneck ordering.
>
> SCOPE EXCLUDES: caller behavior, retry responses, error codes seen by users, backpressure
> consequences, cascade effects, and remediation. If any of these appear in Phase 1 output,
> flag as SCOPE DEFERRAL [Phase X] and continue.

Enumerate every throttle tier. Assign T-NN identifiers (T-01, T-02, ...).

**Tier Registry table:**

| T-NN | Component | Limit (number + unit) | Scope | Window type | Burst headroom |
|------|-----------|----------------------|-------|-------------|----------------|
| T-01 |           |                      |       |             |                |
| T-02 |           |                      |       |             |                |
| ...  |           |                      |       |             |                |

Limits must be numeric. Vague labels ("limited", "throttled") fail. Use `unknown [reason]`
for unconfirmable values. Do not omit tiers — unknown-limit tiers receive a T-NN identifier.

After the table:
- State registry count: "Phase 1 registry: N tiers (T-01 through T-NN)."
- Identify the binding constraint: T-NN, numeric limit exceeded, causal reason this tier
  binds first (lower cap, narrower scope, no burst headroom, shortest window).
- Hit order: every T-NN from the registry listed in the sequence they fire at the given
  volume. Tiers not reached at this volume listed last with "not reached."
- Arrival-shape sensitivity: for each T-NN, mark SHAPE-NEUTRAL (explain mechanism) or
  SHAPE-SENSITIVE (state numeric rate differential and window mechanism).

Declare "Phase 1 complete" before opening Phase 2.

---

**PHASE 2 — BACKPRESSURE PROPAGATION**

> SCOPE COVERS: how throttling at the Phase 1 binding constraint propagates to downstream and
> upstream components; propagation mechanisms; observable effects at each hop.
>
> SCOPE EXCLUDES: new tier introduction. Every tier referenced here must have a T-NN from
> Phase 1. If a component appears here without a T-NN, flag as REGISTRY GAP, assign the next
> available T-NN, and note that Phase 1 should have included it. Do not continue the trace
> without resolving the registry gap.

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

`From (T-NN)` — Phase 1 identifier only. `Mechanism` — queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade. No generic entries.
Minimum two hops.

Declare "Phase 2 complete" before opening Phase 3.

---

**PHASE 3 — USER EXPERIENCE CATALOG**

> SCOPE COVERS: what flow authors and end users observe when each throttle tier fires; error
> codes; Retry-After header presence and handling; run history visibility.
>
> SCOPE EXCLUDES: new tier introduction (same rule as Phase 2). All rows reference Phase 1
> T-NN identifiers. No informal-name-only entries.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

One row per Phase 1 registry tier. No tier may be omitted.
Coverage check: state row count — must match Phase 1 registry count.

Declare "Phase 3 complete" before opening Phase 4.

---

**PHASE 4 — SEVERITY RANKING, CASCADE, AND LOAD-SHAPE ANALYSIS**

> SCOPE COVERS: business-risk ranking across all registered tiers; a concrete cascade scenario;
> load-shape comparison for arrival-sensitive tiers.
>
> SCOPE EXCLUDES: new tier introduction. T-NN identifiers required throughout. If a new
> component appears in the cascade scenario without a T-NN, flag REGISTRY GAP before
> proceeding.

**Severity ranking** — rank all Phase 1 T-NN entries by business risk. Every T-NN must appear.
`T-NN — [rationale sentence]`. For the top-ranked T-NN: blast radius, failure visibility,
recovery time. Coverage check: count must match Phase 1 registry count.

**Cascade scenario** — trace one concrete cascade from the Phase 1 binding constraint. Use
T-NN identifiers at each step — not informal component names.
- T-NN (binding): limit, when it fires
- → T-NN: causal mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade)
- → T-NN: causal mechanism
- Compounded throughput/error-rate effect across all three T-NN entries
Minimum three T-NN entries. Generic cascade claims fail.

**Load-shape analysis** — for each SHAPE-SENSITIVE T-NN from Phase 1:
- Numeric rate under burst arrival vs. numeric rate under uniform arrival at the same volume
- Window mechanism that creates the sensitivity
- Observable user consequence under burst that does not appear under uniform load

Declare "Phase 4 complete" before opening Phase 5.

---

**PHASE 5 — BURST PATHS AND MITIGATIONS**

> SCOPE COVERS: identifying entry points where burst traffic bypasses throttle controls;
> prescribing specific changes for the two highest-priority gaps found across all phases.
>
> SCOPE EXCLUDES: new tier introduction.

**Unprotected burst paths:**

| Path-ID | Entry component | Gap reason (structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|--------------------------------------|----------------|-----------------------------|
| P-01    |                |                                      |                |                             |

`T-NNs bypassed` — Phase 1 identifiers. If no path: state conclusion and name two T-NN
controls covering every entry point.

**Mitigation prescriptions** — two entries, each with all four fields:

**GAP-01:** Gap: [T-NN or P-NN, failure mode, phase] | Component: [specific] | Change:
[setting + value or retry policy with concrete parameters] | Outcome: [quantified or observable]
| Tradeoff: [specific cost]

**GAP-02:** Gap: [T-NN or P-NN, failure mode, phase] | Component: [specific] | Change:
[setting + value] | Outcome: [quantified or observable] | Tradeoff: [specific cost]

Declare "Phase 5 complete."

---

**COMPLETION SUMMARY**

```
Phase 1 registry count:         [N]
Phase 3 catalog count:          [N rows — must match]
Phase 4 ranking count:          [N entries — must match]
Registry gaps flagged:          [count or "none"]
Scope deferrals flagged:        [count or "none"]
C-13: T-NN used in Ph2, Ph3, Ph4: [ ]
C-14: Phase 1 declared complete before Phase 2 opened: [ ]
```

---

## V-04 — Phrasing Register: Conversational/Imperative (Baseline)

**Axis:** Phrasing register — direct imperative language with no formal phase names, no table
schemas, no T-NN instruction, no persona framing. Instructions tell the model what to analyze
and what to produce, but provide no structural scaffolding for perspective separation or
identifier threading. Tests whether C-13 and C-14 survive when the scaffolding is removed.

**Hypothesis:** C-13 and C-14 both require structural enforcement to pass reliably. Without a
registry-gate (V-02) or scope-prohibition rule (V-01, V-03), the model defaults to a
conversational discovery mode: tiers appear when they become relevant to a point being made,
not in a formal registration step, and each section uses whatever name is natural at that
moment. The expected outcome is that C-01 through C-12 pass (the analysis covers the right
topics) while C-13 fails (informal names in at least one downstream section) and C-14 fails
(a tier is discovered or described while tracing backpressure, interleaving perspectives).
This variation establishes the failure baseline for the two new v3 criteria.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Start by listing all the rate limits in the system. For each one, give a specific number and
unit — not just "throttled" but the actual value (e.g., 600 req/min, 10 concurrent
connections). If you don't know the exact value, say so and explain why.

Identify which limit fires first at the given request volume. Why does it fire before the
others — is it a lower cap, narrower scope, no burst headroom? Show the hit order: which
limit fires first, second, and so on.

Now trace what happens after the first limit fires. How does that throttle reach other
components? Walk through at least two steps, and for each step name the specific mechanism
(not just "it affects downstream" but the actual propagation type: queue fills up, connection
holds, retries amplify, dependency stalls, or timeout cascades).

For each rate limit in your list, describe what a Power Automate flow author actually sees
when that limit is hit: the error code, whether a Retry-After header appears and what it
says, whether the failure shows up in run history or is silently handled. Be specific per
limit — don't collapse them into a general paragraph.

For the first limit that fires: does the caller handle Retry-After correctly? If Retry-After
is absent, what failure mode results? If it is present, does the caller code respect it?

Find any path where burst traffic can enter the system without hitting a rate limit. Describe
the entry point, the route, and why no throttle applies on that path. If no such path exists,
name the controls that cover every entry point.

Does the same total request volume produce different throttle behavior depending on whether
requests arrive evenly or in a burst in the first 20% of the window? Show the comparison
numerically for at least one limit.

Rank the rate limits by business risk. For the most dangerous one: who and what is affected,
how visible is the failure, and how long does recovery take?

Trace one scenario where the first-hit limit triggers a failure at a second limit, which
triggers a failure at a third. Name the limits and the causal link at each step. Show the
combined effect.

For the two most important gaps you found: prescribe a specific change. Name the component,
the setting, the value, and what changes after the fix is applied. Don't give general advice —
name the exact configuration change.

---

## V-05 — Combined: Registry Gate + Role Separation + Extended Inertia Framing

**Axis:** Combined — the registry-as-structural-gate (V-02) and strict role separation (V-01)
are combined with an extended inertia framing that explicitly names tier-drift and
mixed-perspective sections as the two production failure patterns that motivated C-13 and
C-14. The inertia story in R2 V-05 named burst-shape blindness and missing prescriptions as
the failure mechanisms. V-05 here extends that story to name the two analysis quality failures
that make throttle documentation unauditable after the fact: (1) tier identifiers that drift
across sections, making coverage gaps invisible; and (2) new tiers discovered mid-caller-trace
whose limits were never formally established.

**Hypothesis:** R2 V-05 achieved the highest R2 composite because the inertia story made the
analysis feel urgent rather than mechanical — the model was searching for the specific gaps the
story named. This variation extends that mechanism to C-13 and C-14 by naming tier-drift and
perspective-mixing as the failure modes the analysis exists to prevent. Registry gate enforces
C-13 structurally. Role separation enforces C-14 structurally. The inertia frame ensures the
model understands why both structures exist rather than treating them as formatting constraints.
Full 14-criterion coverage with both structural and motivational mechanisms. Risk: the inertia
preamble may consume context that would otherwise go to detailed tier analysis; the preamble is
explicitly bounded at two failure patterns to limit this.

---

**THE TWO ANALYSIS QUALITY FAILURES THAT MAKE THROTTLE DOCUMENTATION UNAUDITABLE**

Most throttle analyses fail in the same two ways after the analysis is written — not because
they found the wrong gaps, but because the analysis itself cannot be audited for completeness.

**Failure 1: Tier drift.** The team enumerated five tiers in the initial inventory. In the
cascade scenario, three of them are referenced by component label ("the SharePoint connector",
"the API Management gateway"). In the UX catalog, two are referenced by error code name ("the
429 from the connector layer"). The risk ranking names them differently again. There is no
common identifier threading the sections together. When a reviewer tries to verify that the
UX catalog covers all five tiers, they cannot — the tier names are inconsistent and there is
no registry to audit against. Two tiers have no UX entry; the gap is invisible.

**Failure 2: Mixed-perspective sections.** The analyst began tracing backpressure from the
binding constraint. Midway through the trace, a new component appeared — its limit was not in
the original inventory. The analyst noted the limit in parentheses inside the backpressure
trace, then continued. The tier was never formally registered. Its limit was estimated, not
confirmed. The UX catalog did not include it. The risk ranking did not include it. The coverage
gap appeared after the incident that surfaced it.

The analysis below prevents both failures. The Tier Registry is committed before any caller
analysis begins. Every downstream section references tiers by their registry identifiers.
Tiers discovered after the registry closes are flagged as registry gaps — not silently
incorporated.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Execute the two roles below in strict sequence. ROLE 1 (Tier Analyst) closes the registry
before ROLE 2 (Caller Perspective) opens. ROLE 2 references tiers exclusively by their
ROLE 1 T-NN identifiers.

**PHASE BOUNDARY RULES:**
- ROLE 1: tier properties only. No caller behavior, no error codes, no retry responses.
  If you find yourself describing what a user sees when a tier fires, stop — flag SCOPE
  DEFERRAL and continue after the role boundary.
- ROLE 2: caller analysis only. No new tier introduction. Any component that appears in
  ROLE 2 without a T-NN from ROLE 1 is flagged REGISTRY GAP — assign the next T-NN,
  note the gap, and return to ROLE 2. Every tier reference uses T-NN identifiers.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier discovery, registry assignment, limits, scope, window types, bottleneck*
*ordering, arrival-shape sensitivity. Does not cover: caller behavior or UX.*

### Registry Construction

Enumerate every throttle tier in the system. Assign T-NN identifiers (T-01, T-02, ...).

**TIER REGISTRY:**

| T-NN | Component | Limit (number + unit) | Scope | Window type | Burst headroom |
|------|-----------|----------------------|-------|-------------|----------------|
| T-01 |           |                      |       |             |                |
| T-02 |           |                      |       |             |                |
| ...  |           |                      |       |             |                |

Column rules (these enforce Failure 1 prevention):
- `T-NN` — permanent for this analysis. Every downstream ROLE 2 table and section that
  references a throttle tier must use this identifier verbatim. Informal-name-only references
  are the tier-drift pattern the inertia story names.
- `Limit` — a number with a unit. Vague entries are invalid. `unknown [reason]` for
  unconfirmable values where reason is: undocumented / environment-specific /
  requires-runtime-measurement / signal-insufficient.
- `Burst headroom` — Y [amount] if the window design absorbs short spikes above average
  rate; N if the limit applies to instantaneous rate.

State **"Registry closed — N tiers (T-01 through T-NN). No additions after this point."**

This is the anti-Failure-2 gate. Tiers found after this point are REGISTRY GAPSs, not
silent additions.

### Bottleneck Analysis

Using the closed registry and the given request volume:

1. **Binding constraint:** T-NN of the first-hit tier under uniform arrival; numeric limit
   exceeded; causal reason this tier binds first (lower cap, narrower scope, shortest window,
   no burst headroom).

2. **Hit order:** every T-NN from the registry in the order they fire at the given volume.
   Format: `T-NN: fires at [N unit] / [binding/second/not-reached-at-this-volume]`.

3. **Arrival-shape sensitivity:** for each T-NN, mark SHAPE-NEUTRAL (mechanism: [specific
   window/bucket property]) or SHAPE-SENSITIVE (uniform rate [N unit] does not trigger;
   burst rate [N unit] does trigger; mechanism: [specific window property]).

Declare "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX per tier, burst path analysis, cascade scenario,*
*severity ranking, load-shape consequences, mitigation prescriptions.*
*Does not cover: new tier introduction (flag REGISTRY GAP if a new component appears).*

Open ROLE 2 with: "Registry verification: N tiers from ROLE 1 (T-01 through T-NN).
All downstream sections account for this count."

### Step 2A — Backpressure Propagation Trace

*(Failure 2 prevention: all components traced here must have T-NN identifiers. New components
 flagged as REGISTRY GAP and resolved before continuing.)*

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

`From (T-NN)` — ROLE 1 registry identifier. `Mechanism` — queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade. No generic entries. Minimum two hops.

### Step 2B — User Experience Catalog

*(Failure 1 prevention: one row per T-NN. The row count must match the ROLE 1 registry count.
 This is the audit that tier-drift makes impossible — ensure it passes here.)*

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

`T-NNs bypassed` — ROLE 1 identifiers. Gap reason must be structural, not generic.
If no path: conclusion + two T-NN controls as evidence.

### Step 2D — Severity Ranking and Cascade Scenario

**Severity ranking:** every T-NN from the ROLE 1 registry, ranked by business risk.
`T-NN — [rationale]`. Top-ranked T-NN: blast radius, failure visibility, recovery time.
Coverage check: T-NN count = ROLE 1 registry count. State explicitly.

**Cascade scenario:** concrete cascade from the ROLE 1 binding constraint. T-NN identifiers
throughout (Failure 1 prevention — this is where tier-drift most commonly occurs in cascade
prose). Use: `T-NN (binding) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
Compounded effect. Minimum three T-NNs. Generic cascade claims fail.

**Load-shape analysis:** for each SHAPE-SENSITIVE T-NN from ROLE 1:
- Numeric rate under burst vs. uniform arrival (same total volume)
- Window mechanism that creates the sensitivity
- Observable consequence under burst that uniform arrival never produces
- Whether a standard integration test at this volume would have caught this sensitivity

### Step 2E — Mitigation Prescriptions

*(These are the changes that prevent the two inertia failures from recurring: both Failure 1
 and Failure 2 produce documentation that looks complete but contains invisible gaps. These
 prescriptions are the interventions that close the gaps before the next incident.)*

**GAP-01:** Highest-priority gap from any Step 2A–2D finding
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component]
- Change: [setting name + value, or API parameter + concrete parameters; generic advice fails]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost of this change]

**GAP-02:** Second-priority gap
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component]
- Change: [setting name + value or implementation pattern]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**COMPLETION VERIFICATION**

```
ROLE 1 registry count (closed):  [N tiers]
Step 2B catalog count:           [N rows — must match]
Step 2D ranking count:           [N entries — must match]
REGISTRY GAPs flagged in ROLE 2: [count or "none"]
SCOPE DEFERRALS flagged:         [count or "none"]
C-13: T-NN used in 2A, 2B, 2C, 2D: [ ]
C-14: ROLE 1 declared complete before ROLE 2 opened: [ ]
Failure 1 check (tier drift): zero informal-name-only tier references in ROLE 2: [ ]
Failure 2 check (mixed perspective): zero unregistered tiers introduced in ROLE 2: [ ]
```
