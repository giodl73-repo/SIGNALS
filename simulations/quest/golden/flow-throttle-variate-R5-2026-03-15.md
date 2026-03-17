# flow-throttle Variate — Round 5 (rubric v5 — C-18 per-section audit, C-19 distributed enforcement, C-20 named deferral prohibition)
**Date:** 2026-03-15
**Rubric:** v5 (C-01 through C-20; 5 essential / 3 recommended / 12 aspirational)
**New in v5:** C-18 (per-section compliance verdict in audit block), C-19 (distributed scope-violation reminders at downstream steps), C-20 (explicit deferral prohibition naming the specific downstream section)
**Baseline ceiling:** R4 V-05 — all C-01 through C-17 reliable under three-failure inertia story + structured enforcement; C-18/C-19/C-20 first appearance here

---

## Round 5 State Analysis: What R4 Established vs. What R5 Must Add

**R4 confirmed (all carry forward under structural enforcement):**
- C-01 through C-14: Essential and recommended criteria pass reliably under ROLE 1/ROLE 2
  structure with registry gate, T-NN threading rule, bottleneck ordering, and three-failure
  inertia story.
- C-15 (end-of-analysis audit block): reliable when INTEGRITY VERIFICATION block names all 6
  downstream sections by canonical title and reports machine-checkable unregistered-tier count.
  R4 V-05 achieved this with section-by-section C-13 compliance entries using aggregate T-NN
  usage signals (Y / informal names: list) per section.
- C-16 (per-tier load-shape classification in registry): reliable when the Load-shape verdict
  column is in the Tier Registry table at Step 1A, classified at registration time, with
  numeric rates and mechanism in the same cell. Prohibitive language ("do not defer to a
  downstream section") present in V-04/V-05.
- C-17 (REGISTRY GAP as scope violation): reliable when the PHASE BOUNDARY RULES replace
  "flag and continue" with an explicit SCOPE VIOLATION directive that names the failure pattern
  (Failure 3), prohibits T-NN assignment, and requires ROLE 1 restart. Declared at phase
  boundary in V-03/V-04/V-05.

**R4 gaps (what Round 5 must close):**

C-18 — Per-section compliance verdict in audit block: R4 V-05 INTEGRITY VERIFICATION reports
per-section T-NN usage signals as [Y / informal names: list] — presence/absence signals, not
compliance verdicts. A section showing "[Y]" reports that T-NN identifiers appear, not that
all tier references are T-NN-anchored and counts match. C-18 requires each section entry to
emit a binary compliance status (PASS or FAIL) with a machine-checkable reason when FAIL. The
difference: R4 shows "Step 2B: row count: [N — matches / MISMATCH]" — this is a count
comparison; C-18 requires "Step 2B — User Experience Catalog: [N] rows, all T-NN anchored,
count = registry count — PASS" or "Step 2B: [N] rows, T-03 row missing — FAIL." Every section
needs its own verdict. Audit blocks that enumerate sections and report a single total count
fail C-18 even if all sections are named.

C-19 — Distributed scope-violation reminders at downstream steps: R4 V-05 declares the SCOPE
VIOLATION prohibition at the PHASE BOUNDARY RULES block — before ROLE 1 even opens. This is
a phase-level declaration: the model reads it once, acknowledges it, and proceeds. By the time
the model reaches Step 2A, 2C, or 2E — the steps where new components most naturally appear —
the prohibition was declared 300+ tokens earlier. C-19 requires the prohibition to be restated
at the opening of each vulnerable step (2A, 2C, 2E) as a standing enforcement reminder. A
single phase-boundary declaration without per-step repetition fails C-19 regardless of whether
the violation directive is clear.

C-20 — Explicit deferral prohibition naming the downstream section: R4 V-05 Load-shape verdict
column definition says "do not defer this verdict to a downstream section or to a prose note
following the registry." The word "downstream section" is a category. Step 1B — Bottleneck
Ordering follows the registry table in ROLE 1; a model under completion pressure may consider
Step 1B exempt from the "downstream section" prohibition. C-20 requires the prohibition to name
Step 1B — Bottleneck Ordering (the natural ROLE 1 deferral target) AND at least one ROLE 2
section (e.g., Step 2E — Cascade Scenario) where shape analysis informally migrates. A
prohibition that says "do not defer to a downstream section" without naming the step satisfies
the anti-deferral spirit but leaves the specific escape route open.

**Three questions this round answers:**

Q1 (V-01): Does upgrading the INTEGRITY VERIFICATION block to report a per-section binary
compliance verdict (PASS/FAIL with reason) for each of the 6 downstream sections produce
C-18 compliance, or does the model collapse the verdicts to a single summary even when the
per-section format is required?

Q2 (V-02): Does adding a standing REGISTRY GAP ENFORCEMENT reminder at the opening of each
vulnerable downstream step (2A, 2C, 2E) — in addition to the phase-boundary declaration —
produce C-19 compliance, or does the model treat the per-step reminder as redundant and omit
it under token-budget pressure?

Q3 (V-03): Does replacing the generic "do not defer to a downstream section" prohibition with
a named prohibition that identifies Step 1B — Bottleneck Ordering and Step 2E — Cascade
Scenario as the specific deferral targets produce C-20 compliance, or does the model still
defer to one of the named sections because the column schema makes the shape verdict optional?

---

## Round 5 Variation Map

| Variation | Axis | New criteria targeted | Predicted composite |
|-----------|------|-----------------------|---------------------|
| V-01 | Single: C-18 — per-section PASS/FAIL compliance verdict in audit block | C-18 | ~110/110 |
| V-02 | Single: C-19 — distributed REGISTRY GAP enforcement reminders at Steps 2A, 2C, 2E | C-19 | ~110/110 |
| V-03 | Single: C-20 — named deferral prohibition in Load-shape column (Step 1B + Step 2E) | C-20 | ~110/110 |
| V-04 | Combined: C-18 + C-19 + C-20 on R4 V-05 baseline | C-18 + C-19 + C-20 | ~110/110 |
| V-05 | Maximum density: V-04 + three new named failure stories (Failures 4–6) + reinforced enforcement | C-18 + C-19 + C-20 | ~110/110 |

---

## V-01 — Single Axis: C-18 Per-Section Compliance Verdict in Audit Block

**Axis:** Lifecycle emphasis — the INTEGRITY VERIFICATION block at analysis close is upgraded
so that each of the 6 downstream sections receives its own binary compliance verdict (PASS or
FAIL) with a machine-checkable reason when FAIL. The block is structured as a section-by-
section verdict table, not a summary of counts. No other structural changes from R4 V-05.

**Hypothesis:** R4 V-05 INTEGRITY VERIFICATION reports [Y / informal names: list] per section
for C-13 T-NN threading — a presence/absence signal, not a verdict. C-18 requires that each
section entry emit a binary PASS/FAIL with an explicit reason field. The upgrade from signal to
verdict is the structural surface that enforces per-section accountability: the model must
evaluate each section independently and produce a compliance determination, not just report that
T-NN identifiers appear. Risk: the model produces PASS for every section without evidence,
turning the verdict format into a checkbox; the per-section reason-when-FAIL instruction is
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
registered, so no mitigation existed.

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
block assigns a PASS or FAIL verdict to each downstream section individually — Failure 1 is
verifiable at close, section by section.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences. If you find yourself writing what a flow author sees
  when a tier fires, stop — flag SCOPE DEFERRAL [ROLE 2] and continue after the boundary.
- During ROLE 2: you may NOT introduce a new tier. You may NOT assign a T-NN to any component
  not registered in ROLE 1. If any component appears in ROLE 2 without a T-NN from the ROLE 1
  registry, this is a SCOPE VIOLATION — Failure 3 is occurring:

  **"SCOPE VIOLATION (Failure 3 — mid-trace discovery) — [component name] has no registry
  entry. ROLE 1 was incomplete. Halt ROLE 2 at this point. Restart ROLE 1 with [component
  name] included, re-complete ROLE 1 (including its Load-shape verdict), then resume ROLE 2
  from the beginning of this section."**

  Do not assign a T-NN and continue. The SCOPE VIOLATION requires ROLE 1 restart.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier discovery, registry assignment, limits, scope, window type, burst headroom,
load-shape classification, bottleneck ordering.*
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
  is declared complete.
  - SHAPE-NEUTRAL: throttle status identical under uniform arrival and burst arrival at the
    same total volume. State the specific mechanism: window design, token-bucket headroom,
    concurrent-cap that does not distinguish arrival distribution.
  - SHAPE-SENSITIVE: throttle status differs at the same total volume depending on arrival
    pattern. State: (1) the numeric instantaneous rate under burst that triggers throttling;
    (2) the numeric average rate under uniform arrival that does not trigger it; (3) the window
    mechanism that punishes instantaneous rate regardless of total volume.
  - A shape label without numeric rates satisfies the column header visually but fails
    substantive review — both numeric values required for SHAPE-SENSITIVE tiers.

State: **"Tier Registry complete — N tiers registered (T-01 through T-NN). Registry is closed.
Load-shape verdicts recorded for all N tiers. Any component found in ROLE 2 without a T-NN
from this registry is a SCOPE VIOLATION (Failure 3)."**

### Step 1B — Bottleneck Ordering

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason (lower absolute cap,
   narrower scope, no burst headroom, shortest window). State all that apply.

2. **Hit order:** every T-NN in the order they fire at the given volume.
   `T-NN (limit: X unit) — fires at Y req/min` or `T-NN — not reached at this volume`.
   Every T-NN from Step 1A must appear.

State "ROLE 1 complete" before opening ROLE 2. The registry is locked.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX per tier, burst paths, cascade, severity ranking, retry
handling, mitigations. Does not cover: new tier introduction. Registry is closed.*

Open ROLE 2 with: **"Registry verification: N tiers from ROLE 1 (T-01 through T-NN). Registry
is closed. Failure 1 prevention: every tier reference in ROLE 2 uses T-NN identifiers. Failure
3 prevention: any unregistered component triggers SCOPE VIOLATION — halt and restart ROLE 1."**

### Step 2A — Backpressure Propagation Trace

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — ROLE 1 registry identifier only. Unregistered source: SCOPE VIOLATION
  (Failure 3) — halt, signal the violation, restart ROLE 1.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade. Generic entries fail this column.
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

| Path-ID | Entry component | Gap reason (structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|--------------------------------------|----------------|-----------------------------|
| P-01    |                |                                      |                |                             |

- `T-NNs bypassed` — ROLE 1 identifiers only. Unregistered entry component: SCOPE VIOLATION.
- `Gap reason` must be structural: missing connector policy, trigger type exempt from queuing,
  endpoint that bypasses the gateway layer, no concurrency cap on this path.
- If no unprotected path: conclusion + two T-NN controls covering every entry point.

### Step 2D — Severity Ranking

Rank all ROLE 1 T-NN entries by business risk, highest to lowest. Every T-NN must appear.
Format: `T-NN — [rationale sentence]`. Top-ranked tier: blast radius, failure visibility
(silent vs. explicit), recovery time. Coverage check: T-NN count = registry count.

### Step 2E — Cascade Scenario

Trace one concrete cascade starting from the ROLE 1 binding constraint. Use T-NN identifiers
throughout — informal names without T-NN anchors are untracked references (Failure 1).
Format: `T-NN (binding, limit: X) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
State the compounded throughput/error-rate effect. Minimum three T-NNs with explicit causal
links. Generic claims ("could cascade") fail.

### Step 2F — Retry-After Gap Assessment

For the ROLE 1 binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely (retry storm, missing exponential backoff, silent quota
exhaustion, immediate re-queue within same throttle window). If present, state whether callers
respect it correctly.

### Step 2G — Mitigation Prescriptions

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component]
- Change: [setting name + value, API parameter + value, or retry policy with concrete
  parameters; generic advice fails]
- Expected outcome: [quantified or observable behavioral change]
- Tradeoff: [specific cost — latency, throughput ceiling, operational complexity]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

This block is mandatory. Report a PASS or FAIL verdict for each of the six downstream sections
individually. PASS requires: (a) all tier references in the section use T-NN identifiers from
the ROLE 1 registry, and (b) where a count comparison applies, counts match. FAIL requires:
the specific T-NN mismatch, informal reference, or count discrepancy that caused the failure.
A prose summary of overall coverage without per-section verdicts fails this block.

```
ROLE 1 registry count (locked):   [N tiers — T-01 through T-NN]

Per-section compliance verdicts (C-18):
  Step 2A — Backpressure Propagation Trace:
    T-NN compliance: all From cells contain T-NN identifiers —  [PASS / FAIL: list informal refs]
    Unregistered sources:                                        [0 / list components]
    Section verdict:                                             [PASS / FAIL]

  Step 2B — User Experience Catalog:
    T-NN compliance: all rows T-NN anchored —                    [PASS / FAIL: list rows without T-NN]
    Row count vs. registry count:                                [N rows = N / MISMATCH: list missing tiers]
    Section verdict:                                             [PASS / FAIL]

  Step 2C — Unprotected Burst Path Analysis:
    T-NN compliance: T-NNs bypassed column uses registry IDs —   [PASS / FAIL: list informal refs]
    Unregistered entry components:                               [0 / list]
    Section verdict:                                             [PASS / FAIL]

  Step 2D — Severity Ranking:
    T-NN compliance: all entries T-NN anchored —                 [PASS / FAIL: list informal refs]
    Entry count vs. registry count:                              [N = N / MISMATCH: list missing tiers]
    Section verdict:                                             [PASS / FAIL]

  Step 2E — Cascade Scenario:
    T-NN compliance: all tier references T-NN anchored —         [PASS / FAIL: list informal refs]
    Unregistered cascade members:                                [0 / list]
    Section verdict:                                             [PASS / FAIL]

  Step 2F — Retry-After Gap Assessment:
    T-NN compliance: binding constraint cited by T-NN —          [PASS / FAIL: name used instead]
    Section verdict:                                             [PASS / FAIL]

Failure 2 audit (C-16):
  Load-shape verdict in registry at registration:                [Y / tiers with deferred verdicts: list]
  Shape-sensitive tiers numeric rates recorded:                  [Y / tiers missing numeric rates: list]

Failure 3 audit (C-17):
  SCOPE VIOLATIONS triggered in ROLE 2:                          [count or "none"]
  All violations treated as restarts (not fill-ins):             [Y / fill-in steps taken: list]
  Unregistered tiers introduced after registry closed:           [0] (or list by name)

C-14: ROLE 1 declared complete before ROLE 2 opened:             [Y]
C-15: All six downstream sections named in this block:           [Y]
C-18: Per-section verdict emitted for all 6 sections:            [Y]
Overall:                                                         [PASS if all 6 verdicts PASS / FAIL: list]
```

---

## V-02 — Single Axis: C-19 Distributed Scope-Violation Reminders at Downstream Steps

**Axis:** Role sequence — the REGISTRY GAP / SCOPE VIOLATION enforcement (C-17) is restated
as a standing reminder at the opening of each downstream step where mid-phase tier discovery
is structurally likely (Steps 2A, 2C, 2E). The reminder is a brief enforcement block at the
top of each vulnerable section. No changes to the audit block (C-18 not targeted). No changes
to the Load-shape column definition (C-20 not targeted).

**Hypothesis:** R4 V-05 declares the SCOPE VIOLATION prohibition at the PHASE BOUNDARY RULES
block before ROLE 1 begins. By the time the model reaches Step 2A, the rule was established
300+ tokens earlier; the immediate context is the section template, not the boundary rules.
Adding a standing enforcement reminder at the opening of each vulnerable step reactivates the
prohibition at the precise moment of exposure: Step 2A when filling the `From (T-NN)` column,
Step 2C when identifying entry components, Step 2E when extending the cascade chain. Risk: the
model copies the reminder verbatim and then immediately violates it under completion pressure.
Mitigation: each reminder includes the specific violation signal to emit.

---

**THE THREE ANALYSIS FAILURES THAT MAKE THROTTLE DOCUMENTATION UNAUDITABLE**

Most throttle analyses fail in the same three ways after the analysis is written.

**Failure 1: Tier drift.** Five tiers enumerated. Cascade references three by component label.
UX catalog references two by error code. No common identifier. Two tiers have no UX entry;
the gap is invisible.

**Failure 2: Shape blindness.** Shape verdict written as prose after the registry table, then
skipped under time pressure. Registry row blank. Burst event at 4x rate six months later.

**Failure 3: Mid-trace discovery.** New component in backpressure trace. T-NN assigned in
parentheses. Never added to registry. Limit was an estimate. Analysis appeared complete.

The analysis below prevents all three failures. The registry gate closes before ROLE 2. The
SCOPE VIOLATION prohibition is active at every step where a new component can appear — it is
restated at each vulnerable step, not declared once and assumed to hold. The audit block
verifies section coverage at close.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences.
- During ROLE 2: you may NOT introduce a new tier. You may NOT assign a T-NN to any component
  not registered in ROLE 1. If any component appears in ROLE 2 without a T-NN from the ROLE 1
  registry, this is a SCOPE VIOLATION:

  **"SCOPE VIOLATION (Failure 3 — mid-trace discovery) — [component name] has no registry
  entry. ROLE 1 was incomplete. Halt ROLE 2 at this point. Restart ROLE 1 with [component
  name] included, re-complete ROLE 1 (including its Load-shape verdict), then resume ROLE 2
  from the beginning of this section."**

  Do not assign a T-NN and continue. This prohibition applies at every ROLE 2 section. It is
  restated at each section where tier discovery risk is highest. The phase-level declaration
  here and the per-step reminders are not substitutes — both apply simultaneously.

---

**ROLE 1 — TIER ANALYST**

### Step 1A — Tier Registry

Enumerate every throttle tier. Assign permanent T-NN identifiers. Populate all columns before
advancing to the next tier.

| T-NN | Component | Limit (number + unit) | Scope | Window type | Load-shape verdict |
|------|-----------|----------------------|-------|-------------|-------------------|
| T-01 |           |                      |       |             |                   |
| T-02 |           |                      |       |             |                   |
| ...  |           |                      |       |             |                   |

Column definitions:
- `T-NN` — permanent. Every ROLE 2 reference verbatim.
- `Limit` — number with unit. `unknown [reason]` for unconfirmable values.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (refill rate in cell), concurrent-cap.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE at registration time. Do not defer
  to a downstream section. State mechanism and numeric rates for SHAPE-SENSITIVE tiers.

State: **"Tier Registry complete — N tiers registered (T-01 through T-NN). Registry is closed.
Any component in ROLE 2 without a T-NN is a SCOPE VIOLATION (Failure 3)."**

### Step 1B — Bottleneck Ordering

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason.
2. **Hit order:** every T-NN in firing order at the given volume.

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX per tier, burst paths, cascade, severity ranking, retry
handling, mitigations. Does not cover: new tier introduction. Registry is closed.*

Open ROLE 2 with: **"Registry verification: N tiers from ROLE 1 (T-01 through T-NN). Registry
is closed. Failure 1 prevention: T-NN identifiers throughout. Failure 3 prevention: SCOPE
VIOLATION on any unregistered component — halt and restart ROLE 1."**

### Step 2A — Backpressure Propagation Trace

> **REGISTRY GAP ENFORCEMENT (C-17 — Step 2A):** Before filling any row in this section,
> confirm that every component you are about to name as a `From` source already has a T-NN
> in the ROLE 1 registry. If a source component lacks a T-NN, do not proceed with the row.
> Emit:
> **"SCOPE VIOLATION at Step 2A — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2A."**
> This reminder applies at this step. The phase-boundary declaration applies at all steps.

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — ROLE 1 registry identifier only.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade.
- Minimum two hops.

### Step 2B — User Experience Catalog

One row per ROLE 1 T-NN. No tier may be omitted.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: row count = ROLE 1 registry count. State explicitly.

### Step 2C — Unprotected Burst Path Analysis

> **REGISTRY GAP ENFORCEMENT (C-17 — Step 2C):** Before identifying any entry component in
> this section, confirm it has a T-NN in the ROLE 1 registry. Burst path analysis commonly
> surfaces gateway layers and trigger types that were not enumerated in ROLE 1. If an entry
> component lacks a T-NN, do not fill the row. Emit:
> **"SCOPE VIOLATION at Step 2C — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2C."**
> This reminder applies at this step. The phase-boundary declaration applies at all steps.

| Path-ID | Entry component | Gap reason (structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|--------------------------------------|----------------|-----------------------------|
| P-01    |                |                                      |                |                             |

- `T-NNs bypassed` — ROLE 1 identifiers only.
- `Gap reason` must be structural. No path: conclusion + two T-NN controls.

### Step 2D — Severity Ranking

Every ROLE 1 T-NN by business risk. `T-NN — [rationale]`. Top tier: blast radius, failure
visibility, recovery time. Coverage check: count = registry count.

### Step 2E — Cascade Scenario

> **REGISTRY GAP ENFORCEMENT (C-17 — Step 2E):** Before extending the cascade chain to any
> component, confirm it has a T-NN in the ROLE 1 registry. Cascade analysis commonly surfaces
> dependency tiers that were not enumerated. If a cascade member lacks a T-NN, do not write
> the causal link. Emit:
> **"SCOPE VIOLATION at Step 2E — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2E."**
> This reminder applies at this step. The phase-boundary declaration applies at all steps.

Concrete cascade from ROLE 1 binding constraint. T-NN identifiers throughout.
`T-NN (binding) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
Compounded effect. Minimum three T-NNs.

### Step 2F — Retry-After Gap Assessment

Binding constraint tier: Retry-After present? If absent, precise failure mode. If present,
caller compliance status.

### Step 2G — Mitigation Prescriptions

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component to modify: [specific named component]
- Change: [setting name + value; generic advice fails]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component to modify: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

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
C-19: REGISTRY GAP reminders present at Steps 2A, 2C, 2E:                   [Y — all three present]
```

---

## V-03 — Single Axis: C-20 Named Deferral Prohibition in Load-Shape Column

**Axis:** Phrasing register — the Load-shape verdict column definition in the Tier Registry
table is upgraded from a generic anti-deferral statement ("do not defer to a downstream
section") to a prohibition that names two specific deferral targets: Step 1B — Bottleneck
Ordering (the natural ROLE 1 deferral destination) and Step 2E — Cascade Scenario (the ROLE 2
section where shape analysis informally migrates). No changes to the audit block. No distributed
enforcement reminders.

**Hypothesis:** R4 V-05 says "do not defer this verdict to a downstream section or to a prose
note following the registry." Step 1B is in ROLE 1 and follows the registry table; a model may
consider Step 1B exempt from the "downstream section" prohibition. Adding "including Step 1B
— Bottleneck Ordering" closes the ROLE 1 escape route. Adding "Step 2E — Cascade Scenario"
closes the most common ROLE 2 deferral target: shape effects are most visible in cascade
behavior, making Step 2E an attractive deferral destination without an explicit prohibition.
Risk: the model acknowledges the named prohibition but writes a placeholder in the registry row
and performs the substantive analysis at Step 1B or Step 2E anyway, splitting the record.

---

**THE THREE ANALYSIS FAILURES THAT MAKE THROTTLE DOCUMENTATION UNAUDITABLE**

Most throttle analyses fail in the same three ways after the analysis is written.

**Failure 1: Tier drift.** Five tiers enumerated. Cascade references three by label. UX catalog
references two by error code. No common identifier. Two tiers have no UX entry; invisible.

**Failure 2: Shape blindness.** Shape verdict written in a prose paragraph after the registry,
then skipped. Registry row blank. Burst event at 4x rate six months later. Verdict existed only
in a note that no reviewer connected to the tier's registry entry.

**Failure 3: Mid-trace discovery.** New component in backpressure trace. T-NN in parentheses.
Never in registry. Limit was an estimate. Appeared complete.

The analysis below prevents all three failures. Shape verdict is a registry column, not a note —
Failure 2 cannot occur if the registry is complete. Registry closes before ROLE 2 — Failure 3
is a structural halt. Audit block names every section — Failure 1 is verifiable.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences.
- During ROLE 2: you may NOT introduce a new tier. If any component appears without a ROLE 1
  T-NN, this is a SCOPE VIOLATION:

  **"SCOPE VIOLATION (Failure 3) — [component name] has no registry entry. Halt. Restart
  ROLE 1 with [component name] included, then resume ROLE 2 from the beginning of this
  section."**

---

**ROLE 1 — TIER ANALYST**

### Step 1A — Tier Registry

Enumerate every throttle tier. Assign permanent T-NN identifiers. Populate all columns before
advancing to the next tier.

| T-NN | Component | Limit (number + unit) | Scope | Window type | Load-shape verdict |
|------|-----------|----------------------|-------|-------------|-------------------|
| T-01 |           |                      |       |             |                   |
| T-02 |           |                      |       |             |                   |
| ...  |           |                      |       |             |                   |

Column definitions:
- `T-NN` — permanent identifier. Every ROLE 2 reference verbatim.
- `Limit` — number with unit. `unknown [reason]` for unconfirmable values.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (refill rate in cell), concurrent-cap.
- `Load-shape verdict` — classify each tier SHAPE-NEUTRAL or SHAPE-SENSITIVE at registration
  time. **Do not defer load-shape classification to Step 1B — Bottleneck Ordering and do not
  defer it to Step 2E — Cascade Scenario.** Step 1B is the step immediately following this
  registry in ROLE 1 — deferring there means the registry row is empty and the verdict is not
  a registered attribute. Step 2E is the step where shape effects manifest most visibly in
  cascade behavior — deferring there moves the verdict outside the registry entirely, into a
  downstream analysis section where it cannot be audited as a tier property. Both steps are
  named and prohibited. Any other downstream section is also prohibited. The registry row is
  the authoritative load-shape record; if the shape verdict is elsewhere, the registry is
  incomplete at closure.
  - SHAPE-NEUTRAL: throttle status identical under uniform arrival and burst arrival at the
    same total volume. State the specific mechanism: window design, token-bucket headroom,
    concurrent-cap that does not distinguish arrival distribution.
  - SHAPE-SENSITIVE: throttle status differs at the same total volume. State: (1) numeric
    instantaneous rate under burst that triggers throttling; (2) numeric average rate under
    uniform arrival that does not; (3) the window mechanism. Both numeric values required —
    a shape label without them satisfies the column header but fails review.

State: **"Tier Registry complete — N tiers registered (T-01 through T-NN). Registry closed.
Load-shape verdicts recorded for all N tiers at registration time. No shape analysis deferred
to Step 1B or Step 2E."**

### Step 1B — Bottleneck Ordering

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason.
2. **Hit order:** every T-NN in firing order at the given volume.

*Load-shape verdicts are closed in Step 1A. Do not add or revise shape verdicts here.*

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation, UX per tier, burst paths, cascade, severity ranking, retry
handling, mitigations. Does not cover: new tier introduction or load-shape analysis (closed
in Step 1A).*

Open ROLE 2 with: **"Registry verification: N tiers from ROLE 1 (T-01 through T-NN). Registry
closed. Load-shape verdicts finalized at Step 1A — not modified in ROLE 2. Failure 3
prevention: SCOPE VIOLATION on any unregistered component."**

### Step 2A — Backpressure Propagation Trace

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — ROLE 1 registry identifier only. Unregistered: SCOPE VIOLATION.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade.
- Minimum two hops.

### Step 2B — User Experience Catalog

One row per ROLE 1 T-NN. No tier may be omitted.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: row count = registry count.

### Step 2C — Unprotected Burst Path Analysis

| Path-ID | Entry component | Gap reason (structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|--------------------------------------|----------------|-----------------------------|
| P-01    |                |                                      |                |                             |

`T-NNs bypassed` — ROLE 1 identifiers only. Unregistered entry component: SCOPE VIOLATION.

### Step 2D — Severity Ranking

Every ROLE 1 T-NN by business risk. `T-NN — [rationale]`. Top tier: blast radius, failure
visibility, recovery time. Coverage check: count = registry count.

### Step 2E — Cascade Scenario

*Note: load-shape analysis was completed in Step 1A. This section traces cascade mechanics
only. If a Step 1A SHAPE-SENSITIVE verdict is relevant to a causal link, reference the T-NN
and the Step 1A verdict — do not introduce new shape analysis here.*

Concrete cascade from ROLE 1 binding constraint. T-NN identifiers throughout.
`T-NN (binding) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
Compounded effect. Minimum three T-NNs.

### Step 2F — Retry-After Gap Assessment

Binding constraint tier: Retry-After present? If absent, precise failure mode. If present,
caller compliance status.

### Step 2G — Mitigation Prescriptions

**GAP-01:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component to modify: [specific named component]
- Change: [setting name + value; generic advice fails]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

**GAP-02:**
- Gap: [T-NN or Path-ID, failure mode, step]
- Component to modify: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

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
  Unregistered tiers introduced after registry closed:                      [0] (or list)

C-20 audit:
  Shape analysis deferred to Step 1B — Bottleneck Ordering:                 [none / FAIL: list tiers]
  Shape analysis deferred to Step 2E — Cascade Scenario:                    [none / FAIL: list tiers]

C-14: ROLE 1 declared complete before ROLE 2 opened:                        [Y]
C-15: All six downstream sections named in this block:                      [Y]
C-20: No load-shape analysis deferred to named targets:                     [Y / FAIL: list tiers]
```

---

## V-04 — Combined: C-18 + C-19 + C-20 on R4 V-05 Baseline

**Axis:** Combined — all three new v5 criteria applied simultaneously on the R4 V-05 structural
baseline (three-failure inertia story, Load-shape column in registry, SCOPE VIOLATION restart
directive, named section audit block). Applies:
- C-18: per-section PASS/FAIL verdict in INTEGRITY VERIFICATION (from V-01)
- C-19: distributed REGISTRY GAP enforcement reminders at Steps 2A, 2C, 2E (from V-02)
- C-20: named deferral prohibition in Load-shape column (Step 1B and Step 2E) (from V-03)

**Hypothesis:** All three criteria are structurally independent — no interaction effects that
would cause one enforcement to weaken another. V-01/V-02/V-03 each established single-axis
mechanisms. V-04 tests whether combination produces token-budget pressure that drops any one
mechanism. Primary risk: per-step reminders at 2A, 2C, 2E add ~150 tokens to ROLE 2, and the
per-section verdict table adds ~200 tokens to the audit block — combined addition may cause the
model to abbreviate Step 2G or truncate the cascade. Mitigation: both per-step reminders and
per-section audit format are required fields (FAIL for omission in the final checklist).

---

**THE THREE ANALYSIS FAILURES THAT MAKE THROTTLE DOCUMENTATION UNAUDITABLE**

Most throttle analyses fail in the same three ways after the analysis is written.

**Failure 1: Tier drift.** Five tiers enumerated. Cascade references three by component label.
UX catalog references two by error code. No common identifier. Reviewer cannot verify coverage.

**Failure 2: Shape blindness.** Shape verdict written as prose after the registry, then skipped.
Registry row blank. Burst event at 4x rate six months later.

**Failure 3: Mid-trace discovery.** New component in backpressure trace. T-NN in parentheses.
Never in registry. Limit estimated. Analysis appeared complete.

The analysis below prevents all three failures. Shape verdict is a registry column, not a note
— Failure 2 cannot occur. Registry closes before ROLE 2 — Failure 3 is a structural halt.
Per-section PASS/FAIL verdicts at close — Failure 1 is section-by-section verifiable.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences. If you find yourself writing what a flow author sees
  when a tier fires, stop — flag SCOPE DEFERRAL [ROLE 2].
- During ROLE 2: you may NOT introduce a new tier. You may NOT assign a T-NN to any component
  not registered in ROLE 1. If any component appears in ROLE 2 without a ROLE 1 T-NN, this is
  a SCOPE VIOLATION:

  **"SCOPE VIOLATION (Failure 3 — mid-trace discovery) — [component name] has no registry
  entry. ROLE 1 was incomplete. Halt ROLE 2 at this point. Restart ROLE 1 with [component
  name] included, re-complete ROLE 1 (including its Load-shape verdict), then resume ROLE 2
  from the beginning of this section."**

  Do not assign a T-NN and continue. This prohibition applies at every ROLE 2 section and is
  restated at Steps 2A, 2C, and 2E. The phase-level declaration and the per-step reminders
  both apply simultaneously.

---

**ROLE 1 — TIER ANALYST**

### Step 1A — Tier Registry

Enumerate every throttle tier. Assign permanent T-NN identifiers. Populate all columns before
advancing to the next tier.

| T-NN | Component | Limit (number + unit) | Scope | Window type | Load-shape verdict |
|------|-----------|----------------------|-------|-------------|-------------------|
| T-01 |           |                      |       |             |                   |
| T-02 |           |                      |       |             |                   |
| ...  |           |                      |       |             |                   |

Column definitions:
- `T-NN` — permanent. Every ROLE 2 reference verbatim.
- `Limit` — number with unit. `unknown [reason]` for unconfirmable values.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (refill rate in cell), concurrent-cap.
- `Load-shape verdict` — classify each tier SHAPE-NEUTRAL or SHAPE-SENSITIVE at registration
  time. **Do not defer load-shape classification to Step 1B — Bottleneck Ordering and do not
  defer it to Step 2E — Cascade Scenario.** Step 1B immediately follows this registry in
  ROLE 1 and is the natural ROLE 1 deferral target; Step 2E is the ROLE 2 section where shape
  effects manifest in cascade behavior and is the natural ROLE 2 deferral target. Both are
  named and prohibited. The registry row is the authoritative load-shape record.
  - SHAPE-NEUTRAL: throttle status identical under uniform and burst at the same total volume.
    State the specific mechanism.
  - SHAPE-SENSITIVE: throttle status differs at the same total volume. State: (1) numeric burst
    rate that triggers throttling; (2) numeric uniform rate that does not; (3) window mechanism.
    Both numeric values required.

State: **"Tier Registry complete — N tiers registered (T-01 through T-NN). Registry closed.
Load-shape verdicts recorded for all N tiers. No shape analysis deferred to Step 1B or Step
2E. Any ROLE 2 component without a T-NN is a SCOPE VIOLATION (Failure 3)."**

### Step 1B — Bottleneck Ordering

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason.
2. **Hit order:** every T-NN in firing order.

*Load-shape verdicts are closed in Step 1A. Do not add or revise shape verdicts here.*

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

Open ROLE 2 with: **"Registry verification: N tiers from ROLE 1 (T-01 through T-NN). Registry
closed. Load-shape verdicts finalized at Step 1A. Failure 1 prevention: T-NN throughout.
Failure 3 prevention: SCOPE VIOLATION on any unregistered component — halt and restart ROLE 1."**

### Step 2A — Backpressure Propagation Trace

> **REGISTRY GAP ENFORCEMENT (C-17 — Step 2A):** Before filling any row, confirm every source
> component has a T-NN in the ROLE 1 registry. If a `From (T-NN)` source lacks a T-NN, emit:
> **"SCOPE VIOLATION at Step 2A — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2A."**

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

`Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
timeout-cascade. Minimum two hops.

### Step 2B — User Experience Catalog

One row per ROLE 1 T-NN. No tier may be omitted.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: row count = registry count. State explicitly.

### Step 2C — Unprotected Burst Path Analysis

> **REGISTRY GAP ENFORCEMENT (C-17 — Step 2C):** Before naming any entry component, confirm
> it has a T-NN in the ROLE 1 registry. If an entry component lacks a T-NN, emit:
> **"SCOPE VIOLATION at Step 2C — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2C."**

| Path-ID | Entry component | Gap reason (structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|--------------------------------------|----------------|-----------------------------|
| P-01    |                |                                      |                |                             |

`T-NNs bypassed` — ROLE 1 identifiers only. No path: conclusion + two T-NN controls.

### Step 2D — Severity Ranking

Every ROLE 1 T-NN by business risk. `T-NN — [rationale]`. Top tier: blast radius, failure
visibility, recovery time. Coverage check: count = registry count.

### Step 2E — Cascade Scenario

> **REGISTRY GAP ENFORCEMENT (C-17 — Step 2E):** Before extending the cascade chain to any
> component, confirm it has a T-NN in the ROLE 1 registry. If a cascade member lacks a T-NN,
> emit:
> **"SCOPE VIOLATION at Step 2E — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2E."**
> *Note: load-shape analysis is closed in Step 1A. Reference Step 1A verdicts by T-NN if
> relevant to causal links — do not introduce new shape analysis here.*

Concrete cascade from ROLE 1 binding constraint. T-NN throughout.
`T-NN (binding) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
Compounded effect. Minimum three T-NNs.

### Step 2F — Retry-After Gap Assessment

Binding constraint tier: Retry-After present? Precise failure mode if absent. Caller compliance
if present.

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

Report a PASS or FAIL verdict for each of the six downstream sections individually. PASS
requires: all tier references use T-NN identifiers, and counts match where applicable. FAIL
requires the specific mismatch. Prose summary without per-section verdicts fails this block.

```
ROLE 1 registry count (locked):   [N tiers — T-01 through T-NN]

Per-section compliance verdicts (C-18):
  Step 2A — Backpressure Propagation Trace:
    T-NN compliance:           [PASS / FAIL: list informal refs]
    Unregistered sources:      [0 / list]
    Section verdict:           [PASS / FAIL]

  Step 2B — User Experience Catalog:
    T-NN compliance:           [PASS / FAIL: list rows without T-NN]
    Row count = registry:      [Y / MISMATCH: list missing tiers]
    Section verdict:           [PASS / FAIL]

  Step 2C — Unprotected Burst Path Analysis:
    T-NN compliance:           [PASS / FAIL: list informal refs]
    Unregistered entries:      [0 / list]
    Section verdict:           [PASS / FAIL]

  Step 2D — Severity Ranking:
    T-NN compliance:           [PASS / FAIL: list informal refs]
    Entry count = registry:    [Y / MISMATCH: list missing tiers]
    Section verdict:           [PASS / FAIL]

  Step 2E — Cascade Scenario:
    T-NN compliance:           [PASS / FAIL: list informal refs]
    Unregistered members:      [0 / list]
    Section verdict:           [PASS / FAIL]

  Step 2F — Retry-After Gap Assessment:
    T-NN compliance:           [PASS / FAIL: name used instead]
    Section verdict:           [PASS / FAIL]

Failure 2 audit (C-16 + C-20):
  Load-shape verdict in registry at registration:      [Y / tiers deferred: list]
  Shape-sensitive numeric rates recorded:              [Y / tiers missing: list]
  Shape deferred to Step 1B:                           [none / FAIL: list tiers]
  Shape deferred to Step 2E:                           [none / FAIL: list tiers]

Failure 3 audit (C-17 + C-19):
  SCOPE VIOLATIONS triggered:                          [count or "none"]
  All violations treated as restarts:                  [Y / fill-ins: list]
  REGISTRY GAP reminders at 2A, 2C, 2E:                [Y — all three]
  Unregistered tiers after registry closed:            [0] (or list)

C-14: ROLE 1 complete before ROLE 2:                   [Y]
C-15: All 6 sections named:                            [Y]
C-18: Per-section verdict for all 6:                   [Y / FAIL: list missing]
C-19: Reminders at 2A, 2C, 2E:                         [Y]
C-20: No shape deferred to named targets:              [Y / FAIL: list tiers]
Overall:                                               [PASS / FAIL: list failing sections]
```

---

## V-05 — Maximum Density: V-04 + Three New Named Failure Stories (Failures 4–6)

**Axis:** Inertia framing — V-04's full three-axis structure (C-18 + C-19 + C-20) is extended
with three additional named failure stories that motivate the three new v5 enforcement
mechanisms. Failure 4 (INCOMPLETE AUDIT) motivates C-18. Failure 5 (SINGLE-POINT PROHIBITION)
motivates C-19. Failure 6 (DEFERRED SHAPE TARGET) motivates C-20. Each story names the specific
incident pattern, the missed gap, and the enforcement mechanism that prevents recurrence.

**Hypothesis:** The three-failure story in R4 V-05 was the highest-scoring structural mechanism
across all rounds — it made the analysis feel urgent and committed the model to finding specific
named failures. Extending to six failures with three named incidents provides the same committed-
search effect for C-18/C-19/C-20 that the original three provided for C-15/C-16/C-17. Risk:
six failure stories plus V-04's full structure is a longer prompt, and the model may truncate
Step 2G or abbreviate the cascade to compensate. Mitigation: the new stories are written
compactly, one paragraph each, naming the failure and enforcement without repeating structural
rules already stated elsewhere.

---

**THE SIX ANALYSIS FAILURES THAT MAKE THROTTLE DOCUMENTATION UNAUDITABLE**

Most throttle analyses fail in one or more of six ways — not because they found the wrong gaps,
but because the analysis cannot be audited for completeness after the fact.

**Failure 1: Tier drift.** Five tiers enumerated. Cascade references three by component label.
UX catalog references two by error code. Severity ranking uses informal names. No common
identifier threads the sections. Reviewer cannot verify UX coverage. Two tiers have no entry;
the gap is invisible.
*Prevention: T-NN identifiers assigned in Step 1A, required verbatim in all ROLE 2 sections.*

**Failure 2: Shape blindness.** Shape verdict written as a prose paragraph after the registry,
then skipped under time pressure. Registry row blank. Burst traffic event at 4x the uniform-
arrival rate six months later — the shape sensitivity was never a registry attribute, so no
mitigation existed.
*Prevention: Load-shape verdict column in Step 1A, populated at registration time.*

**Failure 3: Mid-trace discovery.** New component found during backpressure trace. T-NN
assigned in parentheses and analysis continued. Never in registry. Limit was an estimate.
UX catalog and ranking both missing it. Analysis appeared complete.
*Prevention: SCOPE VIOLATION directive — mid-ROLE 2 discovery halts and restarts ROLE 1.*

**Failure 4: Incomplete audit.** The post-incident review found an audit block that named all
six downstream sections and reported "4 informal tier references across the analysis." The
reviewer could not determine which section had the informal references — the audit block
reported a total. Two sections had mismatches; four had none. The sections with mismatches
were never fixed because the audit block provided no actionable location. The PASS/FAIL
status was unanswerable at the section level.
*Prevention: per-section PASS/FAIL verdict in INTEGRITY VERIFICATION — each section has its
own compliance determination with a specific reason when FAIL, not a shared total.*

**Failure 5: Single-point prohibition.** The REGISTRY GAP prohibition was declared at the
phase boundary before ROLE 1. By Step 2C — Unprotected Burst Path Analysis, the declaration
was 400+ tokens earlier. A new entry component appeared. The model's immediate context was
the Step 2C table template, not the boundary rules. It reverted to the fill-in pattern:
assigned T-NN in the row, noted "late registration" in the Gap reason, and continued. The
single-point declaration did not hold under completion pressure at a vulnerable step.
*Prevention: REGISTRY GAP ENFORCEMENT reminders at Step 2A, Step 2C, and Step 2E — the
prohibition is reactivated at each vulnerable execution point.*

**Failure 6: Deferred shape target.** The Load-shape column said "do not defer to a downstream
section." The analyst interpreted "downstream section" as referring to ROLE 2. Step 1B is in
ROLE 1 and immediately follows the registry table; the analyst wrote shape analysis there,
reasoning that Step 1B is not a "downstream section" in the ROLE 2 sense. The registry row
had "see bottleneck ordering" in the Load-shape column. When a reviewer checked the registry,
the shape verdict was absent from the tier row — it was in Step 1B, which the prohibition did
not name.
*Prevention: Load-shape column names Step 1B — Bottleneck Ordering and Step 2E — Cascade
Scenario as the two specifically prohibited deferral targets.*

The analysis below prevents all six failures. Shape verdict is a registry column, Step 1B and
Step 2E are named prohibited deferral targets — Failures 2 and 6 cannot occur if the registry
is complete. Registry closes before ROLE 2, SCOPE VIOLATION is enforced at every vulnerable
step — Failures 3 and 5 are structural halts. Per-section PASS/FAIL verdicts at close with
actionable locations — Failures 1 and 4 are section-by-section verifiable.

---

You are a Connectors / Power Automate throughput domain expert with two distinct analytic
perspectives. Execute them in strict sequence. ROLE 1 completes entirely before ROLE 2 opens.

**PHASE BOUNDARY RULES — read before beginning:**

- During ROLE 1: describe tier properties only (limits, scope, window type, burst headroom,
  load-shape verdict). You may NOT describe caller behavior, retry responses, error codes seen
  by users, or backpressure consequences. If you find yourself writing what a flow author sees
  when a tier fires, stop — flag SCOPE DEFERRAL [ROLE 2] and continue after the boundary.
  This prevents Failure 1: caller analysis mixed into ROLE 1 produces interleaved sections.
- During ROLE 2: you may NOT introduce a new tier. You may NOT assign a T-NN to any component
  not registered in ROLE 1. If any component appears in ROLE 2 without a T-NN from the ROLE 1
  registry, this is a SCOPE VIOLATION — Failure 3 and Failure 5 are occurring:

  **"SCOPE VIOLATION (Failure 3 + Failure 5 — mid-trace discovery) — [component name] has no
  registry entry. ROLE 1 was incomplete. Halt ROLE 2 at this point. Restart ROLE 1 with
  [component name] included, re-complete ROLE 1 (including its Load-shape verdict), then
  resume ROLE 2 from the beginning of this section."**

  Do not assign a T-NN and continue. The fill-in pattern is exactly Failure 3. This
  prohibition applies at every ROLE 2 section. It is restated at Steps 2A, 2C, and 2E
  where the fill-in pattern most commonly occurs (Failure 5 prevention). The phase-level
  declaration and the per-step reminders both apply simultaneously.

---

**ROLE 1 — TIER ANALYST**

*Covers: tier discovery, registry assignment, limits, scope, window type, burst headroom,
load-shape classification (Failure 2 + Failure 6 prevention), bottleneck ordering.*
*Does not cover: caller behavior, retry handling, UX consequences, backpressure propagation.*

### Step 1A — Tier Registry

Enumerate every throttle tier in the system. This is the enumeration commitment — every tier
must appear before ROLE 2 opens. Assign permanent T-NN identifiers. Populate all columns
before advancing to the next tier.

| T-NN | Component | Limit (number + unit) | Scope | Window type | Load-shape verdict |
|------|-----------|----------------------|-------|-------------|-------------------|
| T-01 |           |                      |       |             |                   |
| T-02 |           |                      |       |             |                   |
| ...  |           |                      |       |             |                   |

Column definitions:
- `T-NN` — T-01, T-02, ... Permanent. Every ROLE 2 reference verbatim. Informal-name-only
  references are the tier-drift pattern (Failure 1) — untracked.
- `Limit` — number with unit. Vague labels invalid. `unknown [reason]` for unconfirmable
  values: undocumented, environment-specific, requires-runtime-measurement,
  signal-insufficient. Unknown-limit tiers still receive a T-NN.
- `Scope` — per-user, per-connection, per-tenant, global.
- `Window type` — sliding, fixed-minute, token-bucket (refill rate in cell), concurrent-cap.
- `Load-shape verdict` — Failure 2 + Failure 6 prevention. Classify each tier SHAPE-NEUTRAL
  or SHAPE-SENSITIVE at registration time. **Do not defer load-shape classification to
  Step 1B — Bottleneck Ordering and do not defer it to Step 2E — Cascade Scenario.** Step 1B
  is the natural ROLE 1 deferral target (immediately following, still in ROLE 1 — Failure 6
  pattern). Step 2E is the natural ROLE 2 deferral target (shape effects manifest most visibly
  in cascade behavior — also Failure 6 pattern). Writing "see Step 1B" or "see cascade" in
  this column means the registry is incomplete at closure. Both steps are named and prohibited.
  - SHAPE-NEUTRAL: throttle status identical under uniform arrival (within 10% average rate
    throughout the window) and burst arrival (same total volume in first 20% of window, 5x
    average instantaneous rate). State the specific mechanism: window design, token-bucket
    headroom, concurrent-cap indifferent to arrival distribution.
    Example: "token-bucket, 60-req headroom, 10 req/sec refill; burst depletes headroom in
    6s but 600 req/min total cap not exceeded; identical status under both patterns."
  - SHAPE-SENSITIVE: throttle status differs at the same total volume depending on arrival
    pattern. State: (1) numeric instantaneous rate under burst that triggers throttling; (2)
    numeric average rate under uniform arrival that does not; (3) window mechanism — the
    specific property that punishes instantaneous rate regardless of total volume.
    Example: "fixed 10-sec sub-window; burst: 150 req/10s exceeds sub-window cap; uniform:
    30 req/10s does not; mechanism: sub-window is a hard instantaneous-rate cap."
  - A shape label without both numeric values satisfies the column header visually but fails
    substantive review.

State: **"Tier Registry complete — N tiers registered (T-01 through T-NN). Registry is closed.
Load-shape verdicts recorded for all N tiers at registration time. No shape analysis deferred
to Step 1B or Step 2E (Failure 6 prevention). Any component in ROLE 2 without a T-NN is a
SCOPE VIOLATION (Failure 3 + Failure 5 prevention). Registry count is locked."**

### Step 1B — Bottleneck Ordering

1. **Binding constraint:** T-NN, numeric limit exceeded, causal reason (lower absolute cap,
   narrower scope, no burst headroom, shortest window, least token-bucket headroom).

2. **Hit order:** every T-NN in the order they fire at the given volume.
   `T-NN (limit: X unit) — fires at Y req/min` or `T-NN — not reached at this volume`.
   Every T-NN from Step 1A must appear.

*Load-shape verdicts are closed in Step 1A (Failure 6 prevention). Do not add or revise shape
verdicts here. If a shape verdict is absent from a Step 1A row, the registry is incomplete —
correct it in Step 1A, not here.*

State "ROLE 1 complete" before opening ROLE 2.

---

**ROLE 2 — CALLER PERSPECTIVE**

*Covers: backpressure propagation (Failure 1 + Failure 4 prevention: T-NN throughout,
per-section verdicts at close), UX per tier, burst paths, cascade, severity ranking, retry
handling, mitigations.*
*Does not cover: new tier introduction (Failure 3 + Failure 5 prevention), load-shape analysis
(Failure 6 prevention — closed in Step 1A).*

Open ROLE 2 with: **"Registry verification: N tiers from ROLE 1 (T-01 through T-NN). Registry
closed. Load-shape verdicts finalized at Step 1A (Failure 6 prevention). Failure 1+4
prevention: every tier reference uses T-NN identifiers. Failure 3+5 prevention: SCOPE
VIOLATION on any unregistered component — halt and restart ROLE 1."**

### Step 2A — Backpressure Propagation Trace

> **REGISTRY GAP ENFORCEMENT (C-17 + Failure 5 prevention — Step 2A):** Before filling any
> row, confirm every source component has a T-NN in the ROLE 1 registry. Backpressure tracing
> is where new sources most naturally appear. If a `From (T-NN)` source lacks a T-NN, emit:
> **"SCOPE VIOLATION at Step 2A — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2A."**
> This reminder is here because Failure 5 fires at this step. Phase-boundary declaration also
> applies.

| Hop | From (T-NN) | To component | Mechanism | Observable effect |
|-----|-------------|--------------|-----------|-------------------|
| 1   |             |              |           |                   |
| 2   |             |              |           |                   |
| ... |             |              |           |                   |

- `From (T-NN)` — ROLE 1 registry identifier only. Unregistered: SCOPE VIOLATION, halt,
  restart ROLE 1.
- `Mechanism` — queue-fill, connection-hold, retry-amplification, dependency-stall,
  timeout-cascade. Generic entries fail.
- Minimum two hops.

### Step 2B — User Experience Catalog

*(Failure 4 prevention: this section's per-section verdict in INTEGRITY VERIFICATION requires
all rows T-NN anchored and count = registry. FAIL if any row missing or informal.)*

One row per ROLE 1 T-NN. No tier may be omitted.

| T-NN | Error code or signal | Retry-After present? (Y/N) | Retry-After value | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|------|---------------------|---------------------------|-------------------|--------------------------------------|-------------------------------|
| T-01 |                     |                           |                   |                                      |                               |
| T-02 |                     |                           |                   |                                      |                               |
| ...  |                     |                           |                   |                                      |                               |

Coverage check: row count = registry count. State explicitly.

### Step 2C — Unprotected Burst Path Analysis

> **REGISTRY GAP ENFORCEMENT (C-17 + Failure 5 prevention — Step 2C):** Before naming any
> entry component, confirm it has a T-NN in the ROLE 1 registry. Burst path analysis surfaces
> gateway layers and trigger types not enumerated in ROLE 1. If an entry component lacks a
> T-NN, emit:
> **"SCOPE VIOLATION at Step 2C — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2C."**
> This reminder is here because Failure 5 fires at this step.

| Path-ID | Entry component | Gap reason (structural explanation) | T-NNs bypassed | Consequence at burst volume |
|---------|----------------|--------------------------------------|----------------|-----------------------------|
| P-01    |                |                                      |                |                             |

- `T-NNs bypassed` — ROLE 1 identifiers only.
- `Gap reason` must be structural: missing connector policy, trigger type exempt from queuing,
  endpoint bypassing the gateway layer, no concurrency cap on this path.
- If no unprotected path: conclusion + two T-NN controls covering every entry point.

### Step 2D — Severity Ranking

*(Failure 4 prevention: per-section verdict requires all entries T-NN anchored and count =
registry.)*

Every ROLE 1 T-NN by business risk. `T-NN — [rationale sentence]`. Top-ranked tier: blast
radius, failure visibility (silent vs. explicit), recovery time. Coverage check: count =
registry count.

### Step 2E — Cascade Scenario

> **REGISTRY GAP ENFORCEMENT (C-17 + Failure 5 prevention — Step 2E):** Before extending the
> cascade chain to any component, confirm it has a T-NN in the ROLE 1 registry. Cascade
> analysis surfaces dependencies not enumerated as throttle tiers. If a cascade member lacks a
> T-NN, emit:
> **"SCOPE VIOLATION at Step 2E — [component name] has no ROLE 1 registry entry. Halt.
> Restart ROLE 1 before continuing Step 2E."**
> *Note: load-shape analysis is closed in Step 1A (Failure 6 prevention). Reference Step 1A
> verdicts by T-NN if relevant to a causal link — do not introduce new shape analysis here.*

Concrete cascade from ROLE 1 binding constraint. T-NN identifiers throughout — informal names
are the tier-drift pattern (Failure 1).
Format: `T-NN (binding, limit: X) → T-NN (causal mechanism) → T-NN (causal mechanism)`.
Compounded throughput/error-rate effect. Minimum three T-NNs with explicit causal links at each
step. Generic claims ("could cascade") fail.

### Step 2F — Retry-After Gap Assessment

For the ROLE 1 binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely (retry storm, missing exponential backoff, silent quota
exhaustion, immediate re-queue within same throttle window). If present, state whether callers
respect it correctly and what evidence exists.

### Step 2G — Mitigation Prescriptions

**GAP-01:** First-priority gap
- Gap: [T-NN or Path-ID, failure mode, which step surfaced it]
- Component to modify: [specific named component — not a layer]
- Change: [setting name + value, API parameter, or retry policy with concrete parameters;
  e.g., "configure Power Automate trigger concurrency to maxConcurrentRuns: 10 to cap parallel
  execution that exhausts T-02's concurrent-connection limit"; generic advice fails]
- Expected outcome: [quantified or observable behavioral change after fix]
- Tradeoff: [specific cost — latency, throughput ceiling, operational complexity]

**GAP-02:** Second-priority gap
- Gap: [T-NN or Path-ID, failure mode, step]
- Component to modify: [specific named component]
- Change: [setting name + value]
- Expected outcome: [quantified or observable]
- Tradeoff: [specific cost]

---

**INTEGRITY VERIFICATION**

This block is mandatory (Failure 4 prevention). Report a PASS or FAIL verdict for each of the
six downstream sections individually — not a total count. PASS requires: (a) all tier references
use T-NN identifiers from the ROLE 1 registry, and (b) where counts apply, counts match. FAIL
requires: the specific mismatch with the section location. Abbreviation, section omission, or a
single aggregate count in place of per-section verdicts fails this block.

```
ROLE 1 registry count (locked):   [N tiers — T-01 through T-NN]

Per-section compliance verdicts — Failure 4 prevention (C-18):
  Step 2A — Backpressure Propagation Trace:
    T-NN compliance: all From cells contain T-NN identifiers —   [PASS / FAIL: list informal refs]
    Unregistered sources:                                         [0 / list with missing T-NN]
    Section verdict:                                              [PASS / FAIL]

  Step 2B — User Experience Catalog:
    T-NN compliance: all rows T-NN anchored —                     [PASS / FAIL: list rows without T-NN]
    Row count vs. registry count:                                 [N rows = N / MISMATCH: list missing]
    Section verdict:                                              [PASS / FAIL]

  Step 2C — Unprotected Burst Path Analysis:
    T-NN compliance: T-NNs bypassed column uses registry IDs —    [PASS / FAIL: list informal refs]
    Unregistered entry components:                                [0 / list with missing T-NN]
    Section verdict:                                              [PASS / FAIL]

  Step 2D — Severity Ranking:
    T-NN compliance: all entries T-NN anchored —                  [PASS / FAIL: list informal refs]
    Entry count vs. registry count:                               [N = N / MISMATCH: list missing]
    Section verdict:                                              [PASS / FAIL]

  Step 2E — Cascade Scenario:
    T-NN compliance: all tier references T-NN anchored —          [PASS / FAIL: list informal refs]
    Unregistered cascade members:                                 [0 / list with missing T-NN]
    Shape analysis deferred from Step 1A:                         [none / FAIL: list tiers]
    Section verdict:                                              [PASS / FAIL]

  Step 2F — Retry-After Gap Assessment:
    T-NN compliance: binding constraint cited by T-NN —           [PASS / FAIL: name used instead]
    Section verdict:                                              [PASS / FAIL]

Failure 2 audit (C-16):
  Load-shape verdict in registry at registration:                 [Y / tiers with deferred verdicts: list]
  Shape-sensitive tiers numeric rates recorded:                   [Y / tiers missing numeric rates: list]

Failure 6 audit (C-20):
  Shape analysis deferred to Step 1B — Bottleneck Ordering:       [none / FAIL: list tiers]
  Shape analysis deferred to Step 2E — Cascade Scenario:          [none / FAIL: list tiers]

Failure 3 + Failure 5 audit (C-17 + C-19):
  SCOPE VIOLATIONS triggered in ROLE 2:                           [count or "none"]
  All violations treated as restarts (not fill-ins):              [Y / fill-in steps taken: list]
  REGISTRY GAP reminders present at 2A, 2C, 2E:                   [Y — all three / list missing steps]
  Unregistered tiers introduced after registry closed:            [0] (or list by name)

C-14: ROLE 1 declared complete before ROLE 2 opened:              [Y]
C-15: All 6 downstream sections named in this block:              [Y]
C-18: Per-section PASS/FAIL verdict for all 6 sections:           [Y / FAIL: list sections missing verdict]
C-19: Reminders present at Steps 2A, 2C, 2E:                      [Y]
C-20: No shape deferred to Step 1B or Step 2E:                    [Y / FAIL: list tiers and targets]
Overall:                                                          [PASS if all 6 verdicts PASS / FAIL: list]
```
