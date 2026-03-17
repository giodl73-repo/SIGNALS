---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 26
---

# flow-lifecycle -- Rubric v26

Scoring rubric for the `flow-lifecycle` skill. Simulates a multi-step business document lifecycle (L2O, P2P, period close, case lifecycle): walks every state with entry conditions, transitions, decision points, parallel paths, exception flows, and terminal states. Surfaces bottlenecks, missing steps, and unhandled edge cases. Roles are domain-auto-selected from process context.

**v26 changes from v25 (v7 from v6)**: Added C-21 (Escape Valve Outcome Space Completeness) and C-22 (Escape Valve Completion Verification) from R6 excellence signals.

C-21 closes the gap between C-20 and the strongest V-02/V-04/V-05 implementations: C-20 requires both failure modes be named, but the four-row outcome table in V-02 also explicitly names both passing modes (PM-1: has evidence + typed reference = pass; PM-2: no evidence + SLA-ABSENT = pass). This creates a complete (evidence-state × author-action) decision space -- every cell of the matrix has a named outcome. C-20 prose implementations that name FM-A and FM-B but omit the passing modes leave authors to infer what success looks like; C-21 requires that inference to be eliminated.

C-22 captures the checklist self-audit pattern introduced by V-05: after completing all structured fields, the prompt includes an explicit author verification step -- a checklist item or declaration that confirms no FM-A or FM-B conditions apply to any instance of the dependency-bound field. C-20 and C-21 are instructional (here is what fails, here is the full outcome space); C-22 is operational (have you checked your entries?). The verification step converts passive instruction into active confirmation at fill time.

Aspirational pool: 12 criteria at 60 pts (v25) -> 14 criteria at 70 pts (v26). 5 pts/criterion rate preserved. Max composite: 150 -> 160.

---

## Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/14 * 70)
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

> Raise the bar once essential and recommended are stable. C-09 through C-13 added in v21; C-14 and C-15 added in v22; C-16 and C-17 added in v23; C-18 added in v24; C-19 and C-20 added in v25; C-21 and C-22 added in v26.

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

### C-16 -- Bottleneck-to-Breach Cross-Reference
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each bottleneck identified in C-04 includes an explicit cross-reference field linking it to the SLA analysis -- naming the specific phase exit gate, SLA envelope, or C-11 breach verdict where the bottleneck's timing consequence is documented. This replaces implicit inference with a traceable pointer from the bottleneck catalog to the breach evidence.
- **Pass condition**: All bottlenecks required by C-04 carry a breach-link field naming the specific phase, exit gate, or SLA threshold where the bottleneck's timing consequence is evidenced. Requires C-10 or C-11 to be satisfied (there must be SLA evidence to link to). A breach-link that states the bottleneck causes delays without naming the target phase or gate is a partial pass (0.5).

### C-17 -- Gap Risk Consequence Structuring
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each process gap identified in C-04 includes three structured fields: (a) the missing step -- what the lifecycle design omits, (b) the reason the step is required for correct execution (regulatory, handoff dependency, downstream state dependency), and (c) the risk consequence if the gap persists (SLA exposure, compliance failure, state inconsistency). This elevates gap identification from a label to an actionable risk entry.
- **Pass condition**: All gaps required by C-04 carry all three fields. The Risk if Absent field must name a specific consequence (e.g., "invoice may be posted against a closed period; triggers audit finding") -- "may cause issues" does not qualify. A three-field entry where the risk consequence is vague is a partial pass (0.5).

### C-18 -- SLA-Absent Escape Valve
- **Weight**: aspirational
- **Category**: depth
- **Text**: When a prompt field has a declared hard dependency on upstream SLA evidence (e.g., the C-16 breach-link field depends on C-10/C-11 being satisfied), the prompt provides an explicit escape valve: a named token or declared-absent state that authors use when the dependency evidence is not present. This creates a three-way outcome -- typed reference (full credit), declared-absent (earned-absence credit), or empty/general statement (fail) -- rather than a binary that penalizes legitimately SLA-free scenarios.
- **Pass condition**: At least one dependency-bound field in the prompt includes an explicit escape valve mechanism. The mechanism must: (a) provide a named token or equivalent (e.g., `SLA-ABSENT`, `N/A -- no SLA envelope defined`), (b) state the condition under which it applies (the dependency evidence is absent), and (c) explicitly distinguish the declared-absent outcome from the fail condition (empty cell or general statement). A prompt that enforces typed IDs on the dependency-bound field without providing any escape valve for the no-dependency case is a partial pass (0.5).

### C-19 -- Per-Field Dimensional Enforcement
- **Weight**: aspirational
- **Category**: depth
- **Text**: When a structured output requires named fields that must be populated with specific categories of content, each field carries explicit dimensional bounds: (a) the category of answer that satisfies the field (e.g., "must cite a regulatory rule, handoff precondition, or system dependency") and (b) at least one disqualifying category or disqualifying example (e.g., "best practice does not qualify"). This closes the partial-pass trap where a field is structurally present but content requirements are unspecified -- a vague answer looks structurally correct but carries no informational value.
- **Pass condition**: For each structured field in a required multi-field output (e.g., C-17's Missing Step / Why Required / Risk if Absent), the prompt provides explicit dimensional guidance for field content. At least one field carries a negative example or disqualifying category. A structured output schema where fields are named without content rules is a partial pass (0.5). A schema where some fields have dimensional guidance and others do not is also a partial pass (0.5).

### C-20 -- Escape Valve Dual-Failure Path Declaration
- **Weight**: aspirational
- **Category**: depth
- **Text**: When an escape valve mechanism is present (C-18), the prompt explicitly names both failure modes for the dependency-bound field: (a) the over-specific failure -- the author has dependency evidence and still uses general language instead of a typed reference, and (b) the under-specific failure -- the author lacks dependency evidence but leaves the field blank or empty instead of using the declared-absent token. This paired articulation makes the three-way outcome (typed reference / declared-absent / fail) unambiguous: each fail path is identified by its specific cause rather than merged into a single "empty or general" bucket.
- **Pass condition**: The escape valve section or instruction explicitly names both failure modes in a co-located or paired statement. A prompt that names only one failure mode -- either "has evidence but uses general language" or "no evidence but leaves blank" but not both -- is a partial pass (0.5). A prompt that merges both failure modes into a single "empty or general statement fails" rule without distinguishing SLA-evidence presence is a partial pass (0.5). A prompt that omits failure-mode articulation entirely should be assessed under C-18 (c) rather than C-20.

### C-21 -- Escape Valve Outcome Space Completeness
- **Weight**: aspirational
- **Category**: depth
- **Text**: When both failure modes are declared (C-20), the declaration is elevated to a complete outcome matrix that covers all four (evidence-state x author-action) combinations: FM-A (has evidence, general language -- fail), FM-B (no evidence, blank -- fail), PM-1 (has evidence, typed reference -- pass), PM-2 (no evidence, declared-absent token -- pass). Explicitly naming the two passing modes alongside the two failure modes eliminates the need for inference: authors see the full decision space, not just the edges where they can go wrong. A prose paired statement that names FM-A and FM-B but leaves PM-1 and PM-2 implicit satisfies C-20 but falls short of C-21.
- **Pass condition**: The escape valve declaration includes all four outcomes (FM-A, FM-B, PM-1, PM-2), each with its evidence-state condition, the author action it describes, and the verdict (pass/fail). A table format with co-located rows is the canonical implementation; prose that covers all four outcomes explicitly in a single passage also qualifies. An implementation that names both failure modes (satisfying C-20) but omits one or both passing modes is a partial pass (0.5). An implementation that names FM-A, FM-B, and one passing mode is also a partial pass (0.5).

### C-22 -- Escape Valve Completion Verification
- **Weight**: aspirational
- **Category**: depth
- **Text**: After all dependency-bound fields are completed, the prompt includes an explicit author self-verification step -- a checklist item or confirmation declaration that prompts the author to confirm no FM-A or FM-B conditions apply to any instance of the dependency-bound field in their output. This converts the instructional role of C-20 and C-21 (informing the author what fails) into an operational role (requiring the author to certify their entries are clean). The verification step names the specific failure modes and applies them as a post-fill audit rather than only a pre-fill guide.
- **Pass condition**: At least one checklist item, self-audit row, or declaration statement is present that explicitly asks the author to confirm absence of FM-A and FM-B conditions across all filled instances of the dependency-bound field. The item must name the failure modes (not just reference "errors") and must be positioned after the field-fill instructions rather than only within them. A verification step that checks for only one failure mode is a partial pass (0.5). A verification step that is embedded within the field instructions rather than positioned as a post-fill check is also a partial pass (0.5).

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
| C-16 | Bottleneck-to-Breach Cross-Reference | aspirational | depth |
| C-17 | Gap Risk Consequence Structuring | aspirational | depth |
| C-18 | SLA-Absent Escape Valve | aspirational | depth |
| C-19 | Per-Field Dimensional Enforcement | aspirational | depth |
| C-20 | Escape Valve Dual-Failure Path Declaration | aspirational | depth |
| C-21 | Escape Valve Outcome Space Completeness | aspirational | depth |
| C-22 | Escape Valve Completion Verification | aspirational | depth |

---

## Example Score Calculations

**All essential pass, all recommended pass, no aspirational**:
(5/5 * 60) + (3/3 * 30) + (0/14 * 70) = 60 + 30 + 0 = 90 -- golden

**All essential pass, 2/3 recommended, no aspirational**:
(5/5 * 60) + (2/3 * 30) + (0/14 * 70) = 60 + 20 + 0 = 80 -- golden (threshold met)

**4/5 essential pass, all recommended pass, all aspirational**:
(4/5 * 60) + (3/3 * 30) + (14/14 * 70) = 48 + 30 + 70 = 148 -- NOT golden (essential incomplete)

**All essential pass, 1/3 recommended, all aspirational**:
(5/5 * 60) + (1/3 * 30) + (14/14 * 70) = 60 + 10 + 70 = 140 -- golden

**All essential + all recommended + all aspirational**:
(5/5 * 60) + (3/3 * 30) + (14/14 * 70) = 60 + 30 + 70 = 160 -- golden (max)

**R6 V-01/V-03/V-04/V-05 (all criteria pass)**:
(5/5 * 60) + (3/3 * 30) + (14/14 * 70) = 60 + 30 + 70 = 160 -- golden (MAX)

**R6 V-02 (C-19 partial, C-20/C-21/C-22 pass)**:
(5/5 * 60) + (3/3 * 30) + (13.5/14 * 70) = 60 + 30 + 67.5 = 157.5 -- golden

**R5 V-05 equivalent under v26 (C-21, C-22 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (12/14 * 70) = 60 + 30 + 60 = 150 -- golden

**R5 V-01/V-02/V-03/V-04 equivalent under v26 (C-17 partial, C-19 partial, C-20 partial, C-21/C-22 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (10.5/14 * 70) = 60 + 30 + 52.5 = 142.5 -- golden

**R4 equivalent under v26 (C-17 partial, C-18 pass, C-19 partial, C-20 partial, C-21/C-22 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (10.5/14 * 70) = 60 + 30 + 52.5 = 142.5 -- golden

**R3 equivalent under v26 (8.5/10 aspirational C-09-C-17, C-18 through C-22 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (8.5/14 * 70) = 60 + 30 + 42.5 = 132.5 -- golden

**R2 V-02 equivalent (C-07 partial, C-09-C-15 pass, C-16 through C-22 not assessed)**:
(5/5 * 60) + (2.5/3 * 30) + (7/14 * 70) = 60 + 25 + 35 = 120 -- golden

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
- **C-16 vs. C-04 and C-11**: C-04 requires bottleneck identification with cause. C-11 requires per-phase breach verdicts. C-16 requires explicit pointers from each bottleneck to the breach evidence -- the connective tissue between the two catalogs. An output can pass C-04 and C-11 without C-16 if the bottleneck-to-breach relationship is left to implicit inference. C-16 cannot be satisfied if C-10 or C-11 is absent (no SLA evidence to link to).
- **C-17 vs. C-04**: C-04 requires that at least 1 gap be identified with a named cause and impact. C-17 requires that every gap carry three structured fields: Missing Step, Why Required, and Risk if Absent. An output satisfies C-04 with a named gap but fails C-17 if the why and risk fields are absent. The Risk if Absent field follows the same specificity rule as C-12 and C-14 -- a named consequence, not a vague gesture.
- **C-18 vs. C-16**: C-16 requires that bottleneck entries carry typed breach references. C-18 requires that the prompt provide a graceful path for the case where no SLA evidence exists -- the three-way outcome mechanism. A prompt that passes C-16 because SLA evidence happens to be present does not automatically satisfy C-18 unless it also handles the no-SLA case with a named escape token. Conversely, providing an escape valve (C-18) without enforcing typed IDs on entries that do have SLA evidence does not earn C-16.
- **C-18 scope**: The escape valve pattern applies wherever a criterion carries a declared hard dependency (e.g., C-16 depends on C-10/C-11). A prompt that omits both the typed-ID enforcement and the escape valve fails C-16; if it has typed-ID enforcement but no escape valve, it is a C-18 partial pass. The escape valve does not weaken the fail condition for empty or general-statement entries -- it only carves out a named declared-absent state.
- **C-19 vs. C-17**: C-17 requires the three-field structure. C-19 requires that each field within that structure carry explicit dimensional bounds and a disqualifying category. An output can satisfy C-17 (three fields structurally present) and partially fail C-19 if some fields have dimensional guidance (e.g., Risk if Absent enforces specificity) but others do not (e.g., Why Required has no guidance on what category of reason qualifies). This is the root cause of C-17 partial fails across R5 V-01-V-04: the Cause field existed without dimensional guidance.
- **C-19 scope**: Dimensional enforcement applies to any structured field, not only those in C-17. If other multi-field outputs (e.g., C-13's three-field bottleneck trajectory, C-11's breach verdict) have fields without content rules, they are also subject to C-19 assessment. Evaluate C-19 across all structured fields in the output.
- **C-20 vs. C-18**: C-18 requires an escape valve with a named token, a condition for use, and a distinction from the fail condition. C-20 requires that the distinction (C-18 condition c) name BOTH failure modes explicitly: the over-specific failure (has evidence, uses general language) and the under-specific failure (no evidence, leaves blank). A prompt that passes C-18 by naming the fail condition as "empty or general statement" without bifurcating by SLA-evidence presence satisfies C-18 but earns only a C-20 partial pass. C-20 cannot be assessed if C-18 is not satisfied.
- **C-20 paired statement**: The two failure modes do not need to appear in a single sentence, but they should be co-located (same step instruction or same outcome table) so authors encounter both paths in a single reading. Modes split across steps or sections reduce clarity and warrant a partial pass assessment.
- **C-21 vs. C-20**: C-20 requires both failure modes be named. C-21 requires the full four-cell outcome matrix: failure modes AND passing modes. The passing modes (PM-1: has evidence + typed reference = pass; PM-2: no evidence + declared-absent = pass) are as important as the failure modes for authors who want to confirm their correct entries, not just avoid their incorrect ones. An implementation that satisfies C-20 by naming FM-A and FM-B in prose satisfies C-20 but earns only a C-21 partial pass unless PM-1 and PM-2 are also explicitly named. C-21 cannot be assessed if C-20 is not satisfied.
- **C-21 format flexibility**: A four-row table is the canonical form, but any structure that co-locates all four (evidence-state, action, verdict) tuples qualifies. The key requirement is that every cell of the (evidence x action) matrix has a named outcome -- no cell should require inference.
- **C-22 vs. C-20 and C-21**: C-20 and C-21 are instructional: they tell the author what the outcomes are. C-22 is operational: it requires the author to apply those outcomes to their own entries as a post-fill verification. C-22 cannot be assessed if C-20 is not satisfied; it presupposes the failure modes are named (so the author knows what to check). A checklist item that asks "did you fill in all Breach Link cells?" without referencing FM-A or FM-B does not satisfy C-22 -- the verification must name the specific failure modes being checked.
- **C-22 positioning**: The verification step earns full credit only if it is positioned after the field-fill instructions -- as a post-fill audit, not as a warning embedded within the instructions. A verification warning inside the field instructions is informational; the same check positioned as a closing confirmation step is operational.
