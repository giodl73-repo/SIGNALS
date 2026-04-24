---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 28
---

# flow-lifecycle -- Rubric v28

Scoring rubric for the `flow-lifecycle` skill. Simulates a multi-step business document lifecycle (L2O, P2P, period close, case lifecycle): walks every state with entry conditions, transitions, decision points, parallel paths, exception flows, and terminal states. Surfaces bottlenecks, missing steps, and unhandled edge cases. Roles are domain-auto-selected from process context.

**v28 changes from v27 (v9 from v8)**: Added C-25 (Anchor Field-Level Citation Specificity), C-26 (As-Is Absent Escape Token), and C-27 (As-Is Source Column Dimensional Enforcement) from R8 excellence signals.

C-25 captures the field-level citation pattern from V-02: when the anchor block is cited in field instructions, the citation names specific fields within the anchor (e.g., "Known Bottlenecks" and "Manual Handoffs") rather than the block name alone. This elevates the no-reconstruct directive from a block-level reference to a field-level audit target. The V-02 differentiator note made the significance explicit: "field-name citation in Step 13 makes the no-reconstruct directive citable at the field level rather than block level." C-24 requires the anchor citation exist; C-25 requires the citation be specific enough to audit.

C-26 captures the absent-baseline escape token from V-03: an explicit named token (e.g., `New Process: [one sentence]`) for the case where no as-is baseline exists because the process is brand-new. This is the C-24 analog of C-18's SLA-ABSENT mechanism. Without this token, an author on a genuinely new process has no graceful path -- the single-state exemption (C-13/C-24) covers "no variant framing" but not "no historical baseline exists." These are structurally different scenarios. C-26 closes the gap by giving the no-baseline case its own declared-absent path that is distinct from reconstruction drift (C-24 fail) and from blank-cell failure.

C-27 captures the As-Is Source column pattern from V-05: a dedicated output column in Step 13's bottleneck trajectory table that records which anchor field each as-is entry was drawn from, covered by FIELD CONTENT RULES with positive (field name cited by name) and disqualifying categories (vague reference or blank). V-05's C-19 note identified this as closing "the last unguarded structured field." C-19 required dimensional enforcement across all structured fields; C-27 makes explicit that the As-Is Source field introduced by C-24/C-25 is subject to that same enforcement. The column converts the drawing instruction (C-25: "draw from Known Bottlenecks") into an auditable output record: reviewers can verify compliance from the document itself.

Aspirational pool: 16 criteria at 80 pts (v27) -> 19 criteria at 95 pts (v28). 5 pts/criterion rate preserved. Max composite: 170 -> 185.

---

## Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/19 * 95)
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

> Raise the bar once essential and recommended are stable. C-09 through C-13 added in v21; C-14 and C-15 added in v22; C-16 and C-17 added in v23; C-18 added in v24; C-19 and C-20 added in v25; C-21 and C-22 added in v26; C-23 and C-24 added in v27; C-25, C-26, and C-27 added in v28.

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

### C-23 -- Role Candidate Context Injection with Specificity Guard
- **Weight**: aspirational
- **Category**: depth
- **Text**: When a lifecycle trace requires domain-specific role assignment, the prompt injects a named context block of pre-qualified role candidates (e.g., a LIFECYCLE CONTEXT block listing domain-appropriate roles drawn from the lifecycle type) before the field-fill instructions. Step 1 becomes a "confirm-and-extend" gate: authors use the context block as a starting point but must actively select, confirm, and extend rather than copy-forward. The context injection is paired with an explicit guard clause stating that specificity enforcement applies with equal strictness to selections from the context list as to from-scratch assignments -- the context block reduces blank-page friction without weakening C-05's generic-label prohibition.
- **Pass condition**: A named context block providing domain-qualified role candidates appears before the role-assignment field instructions. The first step that uses those candidates includes an explicit guard clause -- either a warning that context list terms are starting candidates not final answers, or an instruction that authors must confirm domain fit even when selecting from the list. A context block present without a guard clause is a partial pass (0.5): the injection reduces friction but without the guard it enables label-copying that satisfies C-05 structurally while undermining it semantically.

### C-24 -- As-Is Baseline Single-Source Declaration
- **Weight**: aspirational
- **Category**: depth
- **Text**: When the lifecycle trace involves variant comparison (as-is vs. to-be, or pre/post system change), the current-state baseline is declared once in a named anchor block (e.g., AS-IS ANCHOR) before any field-fill instructions that require as-is data. Every step that needs the as-is baseline references the anchor explicitly and includes a "do not reconstruct here" directive or equivalent. This single-source pattern prevents reconstruction drift -- the subtle divergence that occurs when each step independently reconstructs its own version of the current-state baseline, producing a document where the as-is picture shifts between sections without an authoritative source.
- **Pass condition**: When variant framing is in scope, a named as-is anchor block appears before the field-fill instructions. At least one step that requires as-is data (e.g., the as-is column in C-13's bottleneck trajectory table) explicitly cites the anchor as its source and includes a prohibition against inline reconstruction. A prompt that requires as-is data in multiple steps without a single declared source is a partial pass (0.5). A lifecycle trace with no variant framing earns this criterion by explicitly declaring that no as-is/to-be distinction applies and stating why -- the same single-state exemption logic as C-13.

### C-25 -- Anchor Field-Level Citation Specificity
- **Weight**: aspirational
- **Category**: depth
- **Text**: When an anchor block citation is present (C-24), the citation in field instructions names the specific fields within the anchor that the step must draw from -- not just the block name. A Step 13 instruction that reads "draw from the Known Bottlenecks and Manual Handoffs fields of the anchor" satisfies this criterion; one that reads "draw from the AS-IS ANCHOR" does not. This field-level specificity elevates the no-reconstruct directive from a block-level reference to a field-level audit target: a reviewer can verify that the as-is column content came specifically from the named anchor fields, not merely that the anchor was referenced in general. Any associated checklist or verification item must carry the same field-name precision.
- **Pass condition**: At least one step that references an anchor block names the specific anchor fields to draw from (not just the block name). The field names must appear in both the drawing instruction and in any associated checklist or verification item. A citation that names the anchor block without naming specific fields is a partial pass (0.5). C-25 cannot be assessed if C-24 is not satisfied.

### C-26 -- As-Is Absent Escape Token
- **Weight**: aspirational
- **Category**: depth
- **Text**: When the as-is baseline single-source pattern (C-24) is in scope, the prompt provides an explicit escape token for the case where no as-is baseline exists at all -- a brand-new process with no historical state to document. The token (e.g., `New Process: [one sentence explaining why no as-is baseline applies]`) creates a declared-absent path that is structurally distinct from: the single-state exemption (C-13/C-24: no variant framing in the trace at all), the SLA-ABSENT escape (C-18: no SLA evidence exists), and the reconstruction-drift fail condition (C-24: inline reconstruction present). Without this token, an author encountering a genuinely new process has no graceful path: leaving the as-is column blank is an ambiguous fail, and writing inline content violates the no-reconstruct directive (reconstruction drift). The token closes this gap by giving the no-historical-baseline case its own named declared-absent state, analogous to C-18's role in the SLA dimension.
- **Pass condition**: A named escape token or declared-absent mechanism is provided for the no-as-is-baseline case. The mechanism must: (a) provide a named token or equivalent form (e.g., `New Process: [one sentence]`), (b) state the condition under which it applies (no historical baseline exists for this process), and (c) explicitly distinguish the declared-absent outcome from reconstruction drift. A prompt that relies solely on the single-state exemption (C-13/C-24) for no-as-is scenarios is a partial pass (0.5): the single-state exemption covers "no variant framing in the trace" but not "variant framing present, historical baseline genuinely absent." C-26 cannot be assessed if C-24 is not satisfied.

### C-27 -- As-Is Source Column Dimensional Enforcement
- **Weight**: aspirational
- **Category**: depth
- **Text**: When an anchor block citation is present (C-24) and field-level citation specificity is enforced (C-25), the Step 13 output table includes an As-Is Source column that records the specific anchor field each as-is entry was drawn from. This column is covered by FIELD CONTENT RULES with explicit dimensional bounds: a positive category (must name a specific anchor field by name, e.g., "Known Bottlenecks" or "Manual Handoffs") and a disqualifying category (e.g., "From current state," "see above," or blank). The column converts the drawing instruction (C-25: "draw from Known Bottlenecks") into an auditable output record: reviewers can verify compliance from the document itself without consulting the instruction. This closes the last unguarded structured field in the Step 13 bottleneck trajectory table and extends C-19's dimensional enforcement to the anchor-citation field introduced by C-24/C-25.
- **Pass condition**: The bottleneck trajectory output table includes an As-Is Source column or equivalent field. The column carries FIELD CONTENT RULES with at least one positive example (names a specific anchor field by name) and at least one disqualifying example (vague reference such as "from current state" or blank). A table that includes the column without FIELD CONTENT RULES is a partial pass (0.5). A table where the As-Is Source column appears in the schema but is not covered by dimensional enforcement in the FIELD CONTENT RULES section is also a partial pass (0.5). C-27 cannot be assessed if C-24 and C-25 are not both satisfied.

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
| C-23 | Role Candidate Context Injection with Specificity Guard | aspirational | depth |
| C-24 | As-Is Baseline Single-Source Declaration | aspirational | depth |
| C-25 | Anchor Field-Level Citation Specificity | aspirational | depth |
| C-26 | As-Is Absent Escape Token | aspirational | depth |
| C-27 | As-Is Source Column Dimensional Enforcement | aspirational | depth |

---

## Example Score Calculations

**All essential pass, all recommended pass, no aspirational**:
(5/5 * 60) + (3/3 * 30) + (0/19 * 95) = 60 + 30 + 0 = 90 -- golden

**All essential pass, 2/3 recommended, no aspirational**:
(5/5 * 60) + (2/3 * 30) + (0/19 * 95) = 60 + 20 + 0 = 80 -- golden (threshold met)

**4/5 essential pass, all recommended pass, all aspirational**:
(4/5 * 60) + (3/3 * 30) + (19/19 * 95) = 48 + 30 + 95 = 173 -- NOT golden (essential incomplete)

**All essential pass, 1/3 recommended, all aspirational**:
(5/5 * 60) + (1/3 * 30) + (19/19 * 95) = 60 + 10 + 95 = 165 -- golden

**All essential + all recommended + all aspirational**:
(5/5 * 60) + (3/3 * 30) + (19/19 * 95) = 60 + 30 + 95 = 185 -- golden (max)

**R8 V-01/V-02/V-03/V-04 under v28 (C-25/C-26/C-27 not assessed; prior 24 all pass)**:
(5/5 * 60) + (3/3 * 30) + (16/19 * 95) = 60 + 30 + 80 = 170 -- golden

**R8 V-02 under v28 (C-25 pass: field-name citation; C-26 not assessed: no New Process escape confirmed; C-27 pass: As-Is Source + FIELD CONTENT RULES)**:
(5/5 * 60) + (3/3 * 30) + (18/19 * 95) = 60 + 30 + 90 = 180 -- golden

**R8 V-03 under v28 (C-25 partial: block-level citation present, field-name citation in conversational form; C-26 pass: New Process escape token; C-27 not assessed: no As-Is Source column confirmed)**:
(5/5 * 60) + (3/3 * 30) + (17.5/19 * 95) = 60 + 30 + 87.5 = 177.5 -- golden

**R8 V-05 under v28 (C-25 pass: field-name citation; C-26 partial: not confirmed in scorecard; C-27 pass: As-Is Source + FIELD CONTENT RULES)**:
(5/5 * 60) + (3/3 * 30) + (18.5/19 * 95) = 60 + 30 + 92.5 = 182.5 -- golden

**R7 V-01/V-02/V-03 equivalent under v28 (C-23/C-24 pass; C-25/C-26/C-27 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (16/19 * 95) = 60 + 30 + 80 = 170 -- golden

**R6 V-01/V-03/V-04/V-05 equivalent under v28 (C-23/C-24/C-25/C-26/C-27 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (14/19 * 95) = 60 + 30 + 70 = 160 -- golden

**R5 V-05 equivalent under v28 (C-21/C-22/C-23/C-24/C-25/C-26/C-27 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (12/19 * 95) = 60 + 30 + 60 = 150 -- golden

**R3 equivalent under v28 (8.5/10 aspirational C-09-C-17; C-18 through C-27 not assessed)**:
(5/5 * 60) + (3/3 * 30) + (8.5/19 * 95) = 60 + 30 + 42.5 = 132.5 -- golden

**R2 V-02 equivalent (C-07 partial, C-09-C-15 pass; C-16 through C-27 not assessed)**:
(5/5 * 60) + (2.5/3 * 30) + (7/19 * 95) = 60 + 25 + 35 = 120 -- golden

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
- **C-22 extensibility**: The post-fill checklist may include additional verification items beyond FM-A/FM-B (e.g., confirming as-is data was drawn from a named anchor field per C-25, or confirming As-Is Source column entries per C-27). Additional items do not change the C-22 assessment -- the criterion requires FM-A and FM-B verification; supplementary items are evidence of excellence, not a separate requirement.
- **C-23 vs. C-05**: C-05 requires domain-specific role assignment. C-23 requires that the mechanism for achieving C-05 include a context injection block paired with a specificity guard. A prompt can satisfy C-05 (correct roles assigned) without C-23 (no context block, no guard). C-23 cannot be assessed if C-05 is not satisfied. The guard clause is the critical differentiator: a context block without a guard is a friction reducer but not an excellence pattern.
- **C-23 guard clause forms**: The guard may appear as a warning ("selecting a term from this list does not discharge the specificity requirement"), an instruction ("confirm each selection fits the specific process domain before using it"), or a step framing ("confirm and extend -- do not copy forward without validation"). All qualify as long as they explicitly state that context list selections face the same specificity bar as from-scratch assignments.
- **C-24 vs. C-13**: C-13 requires bottleneck trajectory analysis across as-is and to-be variants. C-24 requires that the as-is baseline used in that analysis be declared once in a named anchor block before field instructions. A prompt can satisfy C-13 (trajectory entries present with all three fields) without C-24 (no anchor; each step reconstructs its own as-is). C-24 cannot be assessed if variant framing is absent; the single-state exemption (declare no variant applies) applies to C-24 on the same terms as C-13.
- **C-24 reconstruction drift**: The failure mode C-24 prevents is subtle -- a document where Step 5's as-is description and Step 13's as-is column describe the same process differently because each step independently recalled or summarized the baseline. The anchor block creates a canonical reference; the "do not reconstruct here" directive makes the dependency explicit. Absence of the directive (anchor present but steps silently use it) is a partial pass (0.5).
- **C-25 vs. C-24**: C-24 requires the anchor citation be present and include a no-reconstruct directive. C-25 requires the citation name specific fields within the anchor, not just the block name. An instruction that reads "draw from the AS-IS ANCHOR" satisfies C-24 but not C-25. An instruction that reads "draw from the Known Bottlenecks and Manual Handoffs fields of the anchor" satisfies both. The field-level specificity is what makes the reference independently auditable -- a reviewer can check that the content came from the named field, not merely that the anchor was mentioned. C-25 cannot be assessed if C-24 is not satisfied.
- **C-25 checklist consistency**: The field-name precision required by C-25 must carry through to all associated verification artifacts. A drawing instruction that names specific fields but a checklist that says only "As-Is drawn from anchor" (without naming the fields) is a partial pass (0.5) -- the precision is present in one location but not enforced end-to-end.
- **C-26 vs. C-13/C-24 single-state exemption**: The single-state exemption covers the case where no variant framing exists in the trace -- there is only one process state to document. C-26 covers a structurally different case: variant framing exists (as-is and to-be are both in scope) but the specific process being traced is brand-new and has no historical baseline to document. A single-state exemption declaration satisfies C-13 and C-24 but does not satisfy C-26. The scenarios are orthogonal: a trace can have variant framing but no history (needs C-26), or no variant framing at all (needs the single-state exemption), or variant framing with history (needs the anchor per C-24).
- **C-26 vs. C-18**: C-18 requires an escape token for the no-SLA-evidence case. C-26 requires an escape token for the no-as-is-baseline case. These are parallel mechanisms applied to different dependency dimensions. A prompt that has C-18's SLA-ABSENT token addresses the SLA dependency; C-26 addresses the as-is-baseline dependency. The two tokens serve different failure modes and must be separately provided. A prompt that has one but not the other earns credit for the one it has.
- **C-27 vs. C-19**: C-19 requires dimensional enforcement for all structured fields. C-27 requires specifically that the As-Is Source field introduced by C-24/C-25 carry dimensional enforcement within FIELD CONTENT RULES. An output can satisfy C-19 by enforcing dimensions on all fields that predate C-24/C-25; if As-Is Source is a new field added by the v28 pattern, C-19 assessment of earlier rounds would not retroactively require it. C-27 makes the requirement explicit and scoped: the anchor-citation field must have its own FIELD CONTENT RULES entry covering positive and disqualifying categories.
- **C-27 vs. C-24 and C-25**: C-24 requires the anchor and no-reconstruct directive. C-25 requires the drawing instruction names specific fields. C-27 requires the output table includes an As-Is Source column covered by FIELD CONTENT RULES. These form a three-step chain: declare the anchor (C-24), name specific fields in the instruction (C-25), record which field was used in the output (C-27). C-27 converts the instruction-time precision of C-25 into an output-time audit trail. C-27 cannot be assessed if C-24 and C-25 are not both satisfied.
- **C-27 closing claim**: The description states C-27 closes "the last unguarded structured field" in the Step 13 table. This claim is valid as of v28 given the known field set. If future rounds introduce additional structured fields in Step 13, C-19 assessment should evaluate whether those fields carry dimensional enforcement; C-27 does not need to be amended for fields outside the As-Is Source column.
