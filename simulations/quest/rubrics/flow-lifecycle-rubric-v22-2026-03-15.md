---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 22
---

# flow-lifecycle -- Rubric v22

Scoring rubric for the `flow-lifecycle` skill. Simulates a multi-step business document lifecycle (L2O, P2P, period close, case lifecycle): walks every state with entry conditions, transitions, decision points, parallel paths, exception flows, and terminal states. Surfaces bottlenecks, missing steps, and unhandled edge cases. Roles are domain-auto-selected from process context.

**v22 changes from v21 (v3)**: Added C-14 (Edge Case SLA Risk Attribution) and C-15 (Exception Coverage Completeness Audit) as new aspirational criteria extracted from R2 excellence signals. Aspirational pool expands from 25 pts (5 criteria) to 35 pts (7 criteria); max composite rises from 115 to 125. Golden threshold unchanged.

---

## Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/7 * 35)
```

Where `_pass` counts full passes as 1.0 and partial passes as 0.5.

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria

> All must pass. Without these the output is not useful.

### C-01 -- State Transition Coverage
- **Weight**: essential
- **Category**: correctness
- **Text**: Every lifecycle step is traced with (a) the state name, (b) the condition required to enter it, and (c) the event or action that advances to the next state. No step is implied or described in prose without a named state.
- **Pass condition**: At least 6 distinct named states appear for the chosen lifecycle. Each state in the trace has an explicit entry trigger and an explicit exit trigger. No transition reads "then X happens" without naming the cause.

### C-02 -- Exception Flow Traces
- **Weight**: essential
- **Category**: coverage
- **Text**: The output does not stop at the happy path. At least one exception or failure branch per major lifecycle phase is traced -- with the trigger condition, the divergence point from the main sequence, and the outcome (recovery state or terminal failure).
- **Pass condition**: At least 3 exception flows are present. Each flow names: (1) the triggering condition, (2) the phase and step where it fires, (3) the recovery action or terminal failure state reached. A note that "errors can occur" is not an exception flow.

### C-03 -- Terminal State Completeness
- **Weight**: essential
- **Category**: correctness
- **Text**: All terminal states -- both success outcomes and failure/cancel endpoints -- are explicitly named and labeled. No branch in the trace leads to an unnamed dead end.
- **Pass condition**: At least 2 terminal states: one labeled success (e.g., "Invoice Paid," "Order Fulfilled") and one labeled failure or cancel (e.g., "Rejected -- No Resubmit," "Voided"). Every traced path reaches a named terminal.

### C-04 -- Bottleneck and Gap Identification
- **Weight**: essential
- **Category**: depth
- **Text**: The output explicitly identifies states or transitions where work stalls, approvals queue, or handoffs fail. Each bottleneck names the step, the cause (manual gate, role dependency, external system), and the process impact.
- **Pass condition**: At least 2 bottlenecks named with cause. At least 1 process gap identified -- a step that the described lifecycle omits but that real-world execution requires.

### C-05 -- Domain Role Assignment
- **Weight**: essential
- **Category**: correctness
- **Text**: Each major step or decision point is owned by a domain-specific role drawn from the lifecycle context. Generic placeholders ("User," "Admin," "System") do not qualify.
- **Pass condition**: At least 3 distinct named roles appear (e.g., Account Executive, AP Clerk, Controller, Support Agent). Each role assignment is tied to the step domain. No step at a decision gate is left unowned.

---

## Recommended Criteria

> Output is meaningfully better with these.

### C-06 -- Parallel Path Modeling
- **Weight**: recommended
- **Category**: depth
- **Text**: Concurrent activities within the lifecycle (e.g., credit check + inventory reservation in L2O; goods receipt + invoice matching in P2P) are shown as parallel lanes with an explicit join condition -- what must be true before the lifecycle resumes the main sequence.
- **Pass condition**: At least 1 parallel path identified with a named join condition. If the lifecycle type has no natural parallel (e.g., a simple case lifecycle), the output explicitly notes the absence and why.

### C-07 -- Decision Point Explicitness
- **Weight**: recommended
- **Category**: format
- **Text**: Every fork in the lifecycle (approval/rejection, threshold check, routing rule) is named as a decision point with: the question being decided, the role that decides, and the downstream path for each outcome.
- **Pass condition**: At least 3 named decision points. Each includes condition, owner role, and all outcome branches. A decision point described only as "approved or rejected" without stating who decides and what triggers each path is a partial fail.

### C-08 -- Edge Case Enumeration
- **Weight**: recommended
- **Category**: coverage
- **Text**: The output names edge cases the lifecycle design does not handle -- scenarios that are logically reachable but absent from the trace (e.g., partial shipment re-entry, duplicate submission collision, retroactive approval after payment).
- **Pass condition**: At least 2 edge cases distinct from the C-02 exception flows. Each includes: the scenario, why the current lifecycle has no step for it, and the risk or consequence.

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable. C-09 through C-13 added in v21; C-14 and C-15 added in v22.

### C-09 -- Cross-Lifecycle Dependencies
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one point where the simulated lifecycle interacts with a different business process is identified with direction: which lifecycle sends the artifact, which receives it, and at what state the handoff occurs (e.g., L2O generating a sales order that triggers P2P replenishment; period close blocking AR posting until all open L2O flows are resolved).
- **Pass condition**: 1 cross-lifecycle dependency named with direction, the partner lifecycle identified, and the coupling state or artifact specified.

### C-10 -- SLA and Timing Annotation
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least 3 states or transitions are annotated with a timing expectation (SLA target or typical duration) and a flag indicating whether the C-04 bottlenecks place that SLA at risk.
- **Pass condition**: 3 or more states carry a timing annotation (e.g., "target: 2 business days") and at least 1 is flagged as AT-RISK with a causal reference to a bottleneck from C-04.

### C-11 -- SLA Breach Detection
- **Weight**: aspirational
- **Category**: depth
- **Text**: For each phase, the output explicitly compares the scenario being traced against the stated SLA threshold and renders a verdict: breach (Y/N) plus a domain-specific cause when breach = Y. This goes beyond annotation (C-10) by requiring an active judgment for the specific scenario rather than a general timing label.
- **Pass condition**: Every phase that carries an SLA envelope (from C-10) includes an explicit breach flag (Y/N) with a breach cause field. At least 1 breach = Y verdict appears with a cause traceable to a specific bottleneck or exception in the trace. A threshold stated without a scenario verdict is a partial pass (0.5).

### C-12 -- Exception-to-SLA Impact Mapping
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each exception flow traced in C-02 includes an explicit SLA impact field: how the exception deviates from the phase timing envelope, whether it causes breach, and which downstream phases inherit the delay. This bridges the exception catalog to the timing analysis and makes exception severity legible without cross-referencing separately.
- **Pass condition**: At least 3 exception flows (all those required by C-02) carry an SLA impact field. The field must state the timing consequence (e.g., "adds 3+ days to PO approval phase; triggers breach threshold") not just note that an impact exists. A field present for some but not all exception entries is a partial pass (0.5).

### C-13 -- Bottleneck Trajectory Analysis
- **Weight**: aspirational
- **Category**: depth
- **Text**: When the lifecycle trace covers process variants (as-is vs. to-be, phased rollout, or pre/post system change), each C-04 bottleneck is tracked across the transition with a three-field entry: (a) how the bottleneck manifests in the current state, (b) its status in the target state (eliminated / shifted to a different step / residual), and (c) the net change assessment. Shifted bottlenecks must name the new location.
- **Pass condition**: At least 2 bottlenecks carry trajectory entries with all three fields. A lifecycle trace that covers only a single process state (no as-is/to-be distinction) earns this criterion by explicitly declaring that no variant comparison applies and naming the reason. A trajectory entry that classifies status without the net-change assessment is a partial pass (0.5).

### C-14 -- Edge Case SLA Risk Attribution
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each edge case identified in C-08 includes an explicit SLA risk field naming: (a) which phase SLA or timing envelope is at risk if the unhandled scenario fires, (b) the expected magnitude of impact, and (c) whether the risk is a breach-level consequence or a delay. This bridges edge case coverage to timing analysis without requiring a cross-reference lookup.
- **Pass condition**: All edge cases required by C-08 carry an SLA risk field. The field must state a specific timing consequence or name a SLA threshold at risk (e.g., "puts Day-3 PO approval SLA at risk; likely breach if concurrent with volume peak") -- "may affect timing" does not qualify. A field present for some but not all edge case entries is a partial pass (0.5).

### C-15 -- Exception Coverage Completeness Audit
- **Weight**: aspirational
- **Category**: coverage
- **Text**: After cataloging exception flows, the output includes an explicit coverage audit: a per-phase check identifying phases that lack exception handlers and naming the risk consequence of each gap. This goes beyond C-02 by surfacing the absence of coverage rather than only the presence of traced exceptions.
- **Pass condition**: A coverage audit section or column is present that accounts for every lifecycle phase. At least 1 unhandled phase gap is identified with a named risk consequence. A lifecycle where all phases have exception handlers earns this criterion by explicitly declaring full coverage. An audit that lists phases without naming risk consequences is a partial pass (0.5).

---

## Scoring Table

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | essential | correctness |
| C-02 | Exception Flow Traces | essential | coverage |
| C-03 | Terminal State Completeness | essential | correctness |
| C-04 | Bottleneck and Gap Identification | essential | depth |
| C-05 | Domain Role Assignment | essential | correctness |
| C-06 | Parallel Path Modeling | recommended | depth |
| C-07 | Decision Point Explicitness | recommended | format |
| C-08 | Edge Case Enumeration | recommended | coverage |
| C-09 | Cross-Lifecycle Dependencies | aspirational | depth |
| C-10 | SLA and Timing Annotation | aspirational | depth |
| C-11 | SLA Breach Detection | aspirational | depth |
| C-12 | Exception-to-SLA Impact Mapping | aspirational | depth |
| C-13 | Bottleneck Trajectory Analysis | aspirational | depth |
| C-14 | Edge Case SLA Risk Attribution | aspirational | depth |
| C-15 | Exception Coverage Completeness Audit | aspirational | coverage |

---

## Example Score Calculations

**All essential pass, all recommended pass, no aspirational**:
(5/5 * 60) + (3/3 * 30) + (0/7 * 35) = 60 + 30 + 0 = 90 -- golden

**All essential pass, 2/3 recommended, no aspirational**:
(5/5 * 60) + (2/3 * 30) + (0/7 * 35) = 60 + 20 + 0 = 80 -- golden (threshold met)

**4/5 essential pass, all recommended pass, all aspirational**:
(4/5 * 60) + (3/3 * 30) + (7/7 * 35) = 48 + 30 + 35 = 113 -- NOT golden (essential incomplete)

**All essential pass, 1/3 recommended, all aspirational**:
(5/5 * 60) + (1/3 * 30) + (7/7 * 35) = 60 + 10 + 35 = 105 -- golden

**R2 V-01 equivalent (all essential + recommended + aspirational pass)**:
(5/5 * 60) + (3/3 * 30) + (7/7 * 35) = 60 + 30 + 35 = 125 -- golden

**R2 V-02 equivalent (all essential + C-07 partial + all aspirational; C-14/C-15 not assessed)**:
(5/5 * 60) + (2.5/3 * 30) + (5/7 * 35) = 60 + 25 + 25 = 110 -- golden

**R2 V-03 equivalent (all essential + recommended + C-11 partial + C-09/C-10/C-12/C-13 pass; C-14/C-15 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (4.5/7 * 35) = 60 + 30 + 22.5 = 112.5 -- golden

---

## Evaluator Notes

- **C-01 strictness**: A step described in narrative prose without a named state does not count toward the 6-state minimum. State names must be unambiguous identifiers (e.g., "PO Pending Approval," not "the approval stage").
- **C-02 vs. C-08**: Exception flows (C-02) are reachable paths in the current lifecycle design. Edge cases (C-08) are gaps -- scenarios the design does not cover. Do not double-count.
- **C-05 generic roles**: "Finance team," "Operations," or "Management" are not specific enough. The role must be a named function (e.g., "Credit Analyst," "Warehouse Receiving Clerk," "Revenue Accountant").
- **C-06 absence credit**: If the lifecycle type genuinely has no parallel activities, an explicit declaration earns the recommended pass -- silence does not.
- **C-07 partial decision**: A decision point that names the condition but omits the owner role counts as a partial pass (0.5); all three elements (condition, role, outcomes) are required for full credit.
- **C-10 vs. C-11**: C-10 asks "is timing annotated?" -- labels applied to states. C-11 asks "is the scenario judged against those labels?" -- active verdict rendered. An output can pass C-10 and fail C-11 (annotation without comparison), but cannot pass C-11 without first satisfying C-10 intent.
- **C-12 scope**: SLA impact on an exception must be quantitative or directional (e.g., "adds N days," "triggers breach threshold") -- "may cause delays" does not satisfy the field.
- **C-13 single-state exemption**: A lifecycle traced without variant framing earns C-13 by declaring no variant applies and naming why. This prevents penalizing well-scoped outputs for a structural property of the prompt, not a quality failure.
- **C-14 scope**: SLA risk on an edge case must name a specific phase SLA or threshold at risk and give a directional consequence -- "may affect timing" does not qualify. Same strictness as C-10 and C-12.
- **C-15 full-coverage credit**: If every phase has an exception handler, the output earns C-15 by explicitly declaring full coverage. A coverage audit section that lists phases without naming gap consequences is a partial pass (0.5).
- **C-14 vs. C-08**: C-08 asks whether an edge case is identified and why it is unhandled. C-14 asks what the SLA cost is if it fires. An output can earn C-08 without C-14 (cases identified but no timing consequence), but C-14 presupposes C-08 is satisfied.
- **C-15 vs. C-02**: C-02 asks whether exception flows are traced. C-15 asks whether the catalog is complete -- are there phases with no exception handler at all? An output that traces three rich exception flows can still fail C-15 if uncovered phases are not audited.
