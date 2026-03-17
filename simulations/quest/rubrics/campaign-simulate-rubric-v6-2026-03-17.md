The user is interrupting file writes — they want the rubric output directly as Markdown. Here it is:

---

**Three new aspirational criteria added (C-26 through C-28):**

| ID | Criterion | Upgrades | Source |
|----|-----------|----------|--------|
| C-26 | Remediation Quality Gate produces per-row Verb/Target/Location table | C-17 (blank-cell gate -> content-quality gate) | V-01/V-04/V-05 remediation extraction tables; extends C-14 prose-to-structure upgrade to remediation field |
| C-27 | Entity Coverage Matrix maps manifest entities to COVERED/CLEAN/SKIPPED | C-16 (sub-skill sentinel -> entity sentinel) | V-02/V-04/V-05 entity-level coverage tracking; SKIPPED entity treated same as missing sub-skill row |
| C-28 | Blast Radius Re-Assessment Gate propagates synthesis results via ELEVATED annotations | C-24 (pattern extraction -> feedback loop closed) | V-03/V-05 blast-radius re-assessment after cross-skill synthesis; ranked table updated before finalization |

**Three new structural pairs / extensions:**
- **C-17/C-26** -- blank cells gated vs. remediation content quality gated
- **C-16/C-27** -- sub-skill sentinel rows vs. entity-level sentinel coverage matrix
- **C-24/C-28** -- cross-skill patterns extracted vs. patterns propagated back into ranked table

**Feedback loop now closed:** C-24 extracts named patterns; C-28 requires those patterns alter the ranked findings table via ELEVATED annotations. The synthesis gate no longer dead-ends in a separate section.

Aspirational pool: 17 -> 20 criteria, still capped at 10 pts. Max score 100 unchanged. All five R6 variations score 100/100 on v5; V-04 and V-05 already satisfy C-26/C-27/C-28.

- **C-26** upgrades C-17 from a completeness gate (no blank cells) to a content-quality gate (no
  vague remediation). C-17 passes when all cells are filled; C-26 passes only when each
  remediation entry is decomposed into Verb/Target/Location/Conformance columns -- the same
  prose-to-structure upgrade C-14 made for System Boundary labels. A checklist checkbox like
  "add permission check" is structurally non-falsifiable; a Verb=add / Target=permission check /
  Location=CallHandler.process() row is verifiable by column scan.
- **C-27** upgrades C-16 from sub-skill granularity to entity granularity. C-16 passes when every
  sub-skill that executed has at least one row in the findings table (sentinel or real); C-27
  passes only when every entity in the Topic Entity Manifest appears in a named Entity Coverage
  Matrix with a COVERED/CLEAN/SKIPPED status. A SKIPPED entity is treated the same as a missing
  sub-skill row in C-16: it signals an execution gap, not a clean run. The matrix converts
  entity-level silence from an ambiguous absence into an explicit disqualifying marker.
- **C-28** upgrades C-24 from pattern extraction to feedback-loop closure. C-24 passes when the
  cross-skill synthesis gate produces at least one named cross-cutting pattern; C-28 passes only
  when those patterns are propagated back into the ranked findings table via ELEVATED annotations
  before the report is finalized. A synthesis gate that populates a P-ID table but leaves the
  ranked findings table unchanged after synthesis satisfies C-24 but not C-28.
- V-04 and V-05 from Round 6 satisfy all three new criteria. The rubric caught up to the Round 6
  gold standard.

---

## Essential Criteria (60 points)

### C-01 . All Five Sub-Skills Execute
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: The simulation must execute all five sub-skills: flow-lifecycle, flow-conversation,
  trace-state, trace-contract, and trace-permissions. Each must produce distinct findings, not
  be silently skipped or collapsed into one pass.
- **Pass condition**: Output contains a labeled section or findings block for each of the five
  sub-skills by name. Absence of any one sub-skill = fail.

---

### C-02 . Findings Ranked by Blast Radius
- **Weight**: essential
- **Category**: format
- **Points**: 12
- **Text**: The final findings report must present findings in ranked order using blast radius as
  the sort key. Blast radius must be explicit -- not implied by placement -- and must distinguish
  at minimum high / medium / low (or equivalent severity tiers).
- **Pass condition**: A ranked findings list exists with an explicit blast-radius or severity
  column/label. Unranked flat lists = fail.

---

### C-03 . System Boundary and Severity per Finding
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: Every finding must identify (a) the system boundary where it was detected (e.g., state
  machine, contract surface, permission check, lifecycle phase) and (b) a severity rating. These
  must appear per finding, not as a summary average.
- **Pass condition**: Each finding entry includes both a boundary label and a severity. Findings
  missing either field = fail.

---

### C-04 . At Least One Spec Gap or Contract Violation Surfaced
- **Weight**: essential
- **Category**: coverage
- **Points**: 12
- **Text**: The primary use case of campaign-simulate is to find what breaks before writing code.
  The output must contain at least one concrete spec gap (underspecified behavior, missing
  precondition) or contract violation (expected vs. actual mismatch) with enough detail to act on.
- **Pass condition**: At least one finding is classified as a spec gap or contract violation with a
  description of what is missing or mismatched. A report with only all-clear findings = fail.

---

### C-05 . Single Synthesized Report (Not Five Separate Outputs)
- **Weight**: essential
- **Category**: format
- **Points**: 12
- **Text**: The output must be one unified simulation findings report, not five disconnected
  sub-skill outputs pasted together. Sub-skill results are inputs to synthesis; the artifact is
  the synthesized document.
- **Pass condition**: Output has a single report structure (header, findings table or list, summary
  section) that integrates all five sub-skills. Raw concatenation of five separate outputs with no
  integration = fail.

---

## Recommended Criteria (30 points)

### C-06 . Exception Paths and Edge Cases Identified
- **Weight**: recommended
- **Category**: depth
- **Points**: 10
- **Text**: The simulation should go beyond the happy path. flow-lifecycle and flow-conversation
  findings should include at least one exception flow, dead-end, loop risk, or edge case per
  sub-skill that ran.
- **Pass condition**: At least two exception paths or edge cases are named across the report
  (not just implied). A report covering only normal operation = does not pass.

---

### C-07 . Findings Cross-Reference Source Sub-Skill
- **Weight**: recommended
- **Category**: coverage
- **Points**: 10
- **Text**: Each finding should cite which sub-skill surfaced it (e.g., [trace-state],
  [flow-lifecycle]). This allows readers to trace a finding back to its simulation context and
  helps prioritize re-runs.
- **Pass condition**: >= 80% of findings carry a sub-skill citation. Findings without any
  attribution = does not pass.

---

### C-08 . State Machine Anomalies Explicitly Called Out
- **Weight**: recommended
- **Category**: depth
- **Points**: 10
- **Text**: The trace-state sub-skill should produce findings about state machine behavior --
  unreachable states, invalid transitions, or violated invariants -- not just a confirmation
  that the state machine was traversed.
- **Pass condition**: At least one state machine anomaly (unreachable state, invalid transition,
  invariant violation, or missing guard) is named in the trace-state findings. No anomalies
  found is acceptable only if the rationale is given.

---

## Aspirational Criteria (10 points, capped)

Each criterion contributes 1 pt. The aspirational section maximum is 10 pts. Passing any 10
of 20 criteria saturates the bucket. Max score = 100.

### C-09 . Test Scenario Baseline Derived from Findings
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The report derives a set of test scenarios (or scenario seeds) directly from its
  findings. Each high or medium blast-radius finding becomes a named test scenario with a brief
  description of what to exercise. This converts simulation output into implementation test
  scaffolding.
- **Pass condition**: The report includes a Test Scenario Baseline section with >= 3 named
  scenarios linked to specific findings.

---

### C-10 . Finding IDs Assigned (F-NN Pattern)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Findings use the F-NN identifier pattern (F-01, F-02, ...) to enable cross-referencing
  in downstream artifacts (spec amendments, test plans, topic-echo). IDs make findings traceable
  through the full finding lifecycle (finding -> DCR/amendment -> spec update -> scenario update).
- **Pass condition**: All findings in the report carry an F-NN ID. Findings without IDs = does not
  pass this criterion.

---

### C-11 . At Least One CRITICAL or HIGH Finding per Trace Sub-Skill
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each of the three trace sub-skills (trace-state, trace-contract, trace-permissions)
  contributes at least one CRITICAL or HIGH severity finding to the report. When all three trace
  budgets are met, >= 3 HIGH/CRITICAL findings exist in the corpus upstream of the test scenario
  baseline -- C-09 passes by construction without requiring an explicit scenario count floor.
  Guarantee the inputs; the output floor follows.
- **Pass condition**: trace-state, trace-contract, and trace-permissions each have at least one
  finding rated CRITICAL or HIGH attributed to them. Missing severity budget on any one trace
  sub-skill = does not pass.

---

### C-12 . Findings Presented in Structured Table (No Blank Cells)
- **Weight**: aspirational
- **Category**: format
- **Text**: All findings appear in a structured table with explicit columns for at minimum:
  Finding ID, Sub-skill, System Boundary, Severity, Description. No cell in any finding row is
  blank. The table format makes C-03 and C-07 failures structurally visible -- a missing boundary
  label or sub-skill citation cannot be buried in prose.
- **Pass condition**: A findings table exists with all required columns populated for every row.
  Prose-only findings lists or a table with blank cells = does not pass.

---

### C-13 . Flow Findings Explicitly Reference Trace Context
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one flow sub-skill finding (flow-lifecycle or flow-conversation) explicitly
  references or builds on a specific trace finding -- e.g., a lifecycle finding cites a state
  invariant violation from trace-state, or a conversation finding references a contract mismatch
  from trace-contract. This cross-reference is the measurable output signature of trace-first
  execution ordering: trace context fed into flow simulations rather than five sub-skills running
  in isolation.
- **Pass condition**: At least one flow finding explicitly names a trace finding by ID or by
  content description. Flow findings that are fully isolated from trace context = does not pass.

---

### C-14 . System Boundary Vocabulary Pre-Assigned per Sub-Skill
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The five system boundary labels must be statically mapped to their owning sub-skills
  and used verbatim in the findings table. Boundary labeling that requires the model to infer
  context from prose is subject to hallucination; pre-assigned labels make C-03 compliance a
  mechanical transcription rather than a judgment call. The fixed map is: trace-state = state
  machine, trace-contract = contract surface, trace-permissions = permission check,
  flow-lifecycle = lifecycle phase, flow-conversation = conversation state.
- **Pass condition**: All System Boundary values in the findings table match the pre-defined
  label for the attributed sub-skill. A boundary value not drawn from the five-label vocabulary,
  or attributed to the wrong sub-skill, = does not pass.

---

### C-15 . Universal Sentinel Rule Across All Columns
- **Weight**: aspirational
- **Category**: format
- **Text**: The no-blank-cell contract from C-12 must extend to every column without exception,
  including optional and conditional fields. When a field does not apply to a given row, the cell
  must contain N/A -- [reason] rather than be left empty. This generalizes C-12 required-column
  enforcement into a complete no-blank contract: there is no column exempt from the rule.
- **Pass condition**: No cell in any finding row is blank. Optional fields contain either a value
  or a filled N/A -- [reason] sentinel. A blank cell in any column, including optional ones,
  = does not pass.

---

### C-16 . No-Findings Sentinel Rows for Clean Sub-Skills
- **Weight**: aspirational
- **Category**: format
- **Text**: When a sub-skill execution produces no findings, the findings table must still contain
  a fully-populated row for that sub-skill. The sentinel row uses Summary = No findings detected
  and fills all other columns per the universal sentinel rule (C-15). An absent row for a clean
  sub-skill is indistinguishable from an execution gap -- silence cannot be used as evidence of a
  clean run.
- **Pass condition**: The findings table contains at least one row attributed to every sub-skill
  that executed. A sub-skill with zero findings must appear as a sentinel row, not be absent from
  the table. Missing sub-skill row = does not pass, regardless of whether the execution log
  mentions a clean result.

---

### C-17 . Pre-Output Blank-Cell Verification Gate
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output must include a named final verification step confirming that no blank cells
  exist in the findings table before the report is written. This step must be labeled or documented
  as a gate, not implied by the absence of blank cells. The gate converts the no-blank contract
  from a style instruction into an explicit checklist item whose outcome is visible in the artifact.
- **Pass condition**: Output contains a named verification gate (e.g., a labeled section, a
  checklist item marked PASSED, or an inline assertion) that confirms table completeness before
  the report is finalized. Reports with no verification gate = does not pass.

---

### C-18 . Unified Schema Closes C-03, C-07, C-10, and C-13 Simultaneously
- **Weight**: aspirational
- **Category**: format
- **Text**: The findings table schema must include at minimum these columns: F-ID (satisfies C-10),
  Sub-Skill (satisfies C-07), System Boundary (satisfies C-03), Severity (satisfies C-03), Blast
  Radius (satisfies C-02 sorting), Trace Link (satisfies C-13), and Description. A single table
  with this schema makes it possible to verify C-03, C-07, C-10, and C-13 by inspection of one
  artifact. Multi-schema designs -- separate tables per sub-skill, or per-phase schemas that omit
  required columns -- fail this criterion even if the data is correct across all tables.
- **Pass condition**: A single findings table exists whose column set includes F-ID, Sub-Skill,
  System Boundary, Severity, Blast Radius, Trace Link, and Description. A multi-table design that
  requires aggregation to verify any of C-03, C-07, C-10, or C-13 = does not pass.

---

### C-19 . Finding Type Drawn from Closed Vocabulary
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The Finding Type field carries the same hallucination risk as System Boundary (C-14):
  free-form type labels allow invented or misattributed categories that silently fail C-04. A
  pre-defined Type Vocabulary Map closes the field to a fixed set (e.g., spec-gap,
  contract-violation, missing-guard, unreachable-state, caller-callee-mismatch,
  undefined-behavior, invariant-violation, permission-gap) and makes type assignment a copy
  operation. The vocabulary map should appear as a named artifact in the output -- either a
  standalone section or as additional columns in the Type Vocabulary Map table alongside the
  System Boundary map from C-14.
- **Pass condition**: All Type values in the findings table are drawn from a named, pre-defined
  vocabulary. Type values not present in the vocabulary, or a findings table with no accompanying
  vocabulary artifact, = does not pass.

---

### C-20 . Blast Radius Rationale for Top-Tier Findings
- **Weight**: aspirational
- **Category**: depth
- **Text**: Findings rated CRITICAL or system-wide must include an explicit rationale sentence
  explaining why the blast radius reaches that tier -- e.g., system-wide because the missing
  permission check applies to all callers regardless of role. Without a rationale, the tier
  assignment is an assertion; with one, it is a verifiable claim that reviewers can challenge or
  confirm. C-02 requires blast-radius labels; C-20 requires audit sentences for the highest-tier
  assignments.
- **Pass condition**: Each finding rated CRITICAL or classified as system-wide blast radius
  includes at least one sentence explaining the basis for that tier assignment. Top-tier findings
  with no rationale = does not pass.

---

### C-21 . Exception Path Coverage Tracked in Named Column
- **Weight**: aspirational
- **Category**: depth
- **Text**: C-06 requires at least two named exception paths across the report. C-21 requires that
  exception path coverage be tracked in a named structural column in the findings table or entity
  manifest -- e.g., an Exception Path column that is populated per finding row. A structural
  column makes coverage verifiable by inspection: counting non-null Exception Path cells is
  sufficient evidence. Prose mention of exception paths satisfies C-06 but not C-21.
- **Pass condition**: The findings table or entity manifest contains a named Exception Path column
  (or structural equivalent) populated for each finding row. Exception paths mentioned only in
  prose, or implied by finding descriptions, = does not pass.

---

### C-22 . Severity Budget Gate Enforces Trace-Before-Flow Ordering
- **Weight**: aspirational
- **Category**: behavior
- **Text**: C-11 requires that the CRITICAL/HIGH finding budget is met across all three trace
  sub-skills. C-22 requires that a named severity budget gate mechanism actively enforces this
  before any flow sub-skill executes. The gate must block flow execution if the trace budget is
  not met and either halt the campaign or require an exhaustion rationale explaining why the
  budget could not be satisfied. This converts the trace-before-flow dependency from a convention
  to an enforced structural constraint. A campaign where flow and trace run in parallel or in
  arbitrary order, even if the budget happens to be met, fails this criterion.
- **Pass condition**: Output contains a named severity budget gate that explicitly checks trace
  sub-skill CRITICAL/HIGH counts before flow sub-skills begin. Flow execution that proceeds
  without this gate, or a budget shortfall with no exhaustion rationale, = does not pass.

---

### C-23 . Blast Rationale Appears as Named Table Column
- **Weight**: aspirational
- **Category**: format
- **Text**: C-20 requires that blast radius rationale sentences exist for top-tier findings.
  C-23 requires those rationale sentences appear in a dedicated named column in the ranked
  findings table -- e.g., a Blast Rationale column alongside the Blast Radius column. A
  structural column makes rationale coverage verifiable by table scan: a blank Blast Rationale
  cell for a system-wide finding is immediately visible without reading prose. Rationale buried
  in the Description column or in a separate section satisfies C-20 but not C-23.
- **Pass condition**: The ranked findings table contains a named Blast Rationale column (or
  structural equivalent) populated for every CRITICAL or system-wide finding row. Rationale
  present only in prose or only in the Description cell = does not pass.

---

### C-24 . Mandatory Cross-Skill Synthesis Gate Extracts Named Patterns
- **Weight**: aspirational
- **Category**: depth
- **Text**: C-05 requires a single synthesized report rather than five concatenated outputs.
  C-24 requires that synthesis include a named cross-skill synthesis gate step that explicitly
  identifies patterns appearing in two or more sub-skills -- e.g., a missing permission check
  surfaced by both trace-permissions and flow-lifecycle, or a state invariant that appears in
  both trace-state and trace-contract findings. The gate must be labeled in the output and must
  produce at least one named cross-cutting pattern before the report is finalized. C-17 gates on
  blank cells; C-24 gates on pattern extraction. A report that integrates findings into one table
  without running this named gate step satisfies C-05 but not C-24.
- **Pass condition**: Output contains a named cross-skill synthesis gate step with at least one
  documented cross-cutting pattern citing two or more source sub-skills by name. A unified table
  with no named synthesis gate, or a gate that produces no patterns, = does not pass.

---

### C-25 . Severity Drawn from Closed Four-Value Vocabulary
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Severity values must be drawn from a fixed four-value set -- CRITICAL, HIGH, MEDIUM,
  LOW -- and enforced by a verification gate before the report is finalized. This closes the
  Severity field against invented tiers (e.g., ELEVATED, MODERATE, MINOR) that make cross-run
  comparisons unreliable. C-25 completes the closed-vocabulary triple: C-14 closes System
  Boundary to 5 labels, C-19 closes Finding Type to a named vocabulary, and C-25 closes Severity
  to {CRITICAL, HIGH, MEDIUM, LOW}. Together the three fields -- the two most hallucination-prone
  and the severity tier -- become mechanical transcription rather than model judgment.
- **Pass condition**: All Severity values in the findings table are drawn from the set
  {CRITICAL, HIGH, MEDIUM, LOW}. A verification gate explicitly confirms all severity values are
  from this set before output is written. Severity values outside the vocabulary, or no
  enforcement gate, = does not pass.

---

### C-26 . Remediation Quality Gate Produces Structured Extraction Table
- **Weight**: aspirational
- **Category**: behavior
- **Text**: C-17 gates on blank cells; C-26 gates on remediation content quality. A remediation
  checklist with checkbox entries (e.g., "add permission check") is structurally non-falsifiable:
  there is no way to verify by column scan whether the remediation is complete or precisely
  scoped. C-26 requires that each remediation entry be decomposed into a per-row extraction table
  with at minimum: Verb (the required action), Target (the artifact to modify), Location (the
  exact site in the artifact), and Conformance (MET/NOT MET). This is the same upgrade C-14 made
  to System Boundary labels: from prose-inferred assignment to column-scan-verifiable structure.
  A findings table that includes remediation text in a Description cell, or a prose remediation
  section, satisfies the implied remediation requirement but not C-26.
- **Pass condition**: The output contains a remediation extraction table (or equivalent per-row
  structure) with Verb, Target, Location, and Conformance columns populated for every remediation
  entry. Remediation present only as checklist checkboxes or prose = does not pass.

---

### C-27 . Entity Coverage Matrix Maps Manifest Entities to Coverage Status
- **Weight**: aspirational
- **Category**: coverage
- **Text**: C-16 requires a sentinel row for every sub-skill that executed. C-27 extends this
  sentinel discipline to entity granularity. After sub-skill execution, a named Entity Coverage
  Matrix must map every entity in the Topic Entity Manifest to one of three states: COVERED
  (entity appeared in at least one finding), CLEAN (entity executed without findings, documented
  as clean), or SKIPPED (entity was not reached during simulation). A SKIPPED entity is as
  unacceptable as a missing sub-skill row in C-16: it signals an execution gap, not a clean run.
  A report that mentions all five sub-skills but does not account for each manifest entity is
  incomplete in the same structural sense as a report that omits a sub-skill row. The matrix must
  be a named structural artifact, not implied by the absence of entity-specific findings.
- **Pass condition**: The output contains a named Entity Coverage Matrix with one row per Topic
  Entity Manifest entity, each populated with COVERED, CLEAN, or SKIPPED status. A report with
  no entity coverage matrix, or with SKIPPED entity rows carrying no exhaustion rationale,
  = does not pass.

---

### C-28 . Blast Radius Re-Assessment Gate Propagates Synthesis Results
- **Weight**: aspirational
- **Category**: depth
- **Text**: C-24 requires a cross-skill synthesis gate that extracts named cross-cutting patterns.
  C-28 requires that those patterns be propagated back into the ranked findings table via ELEVATED
  annotations before the report is finalized -- e.g., a finding whose blast radius was assessed as
  component-wide during sub-skill execution receives an ELEVATED annotation if the C-24 synthesis
  gate identifies it as part of a system-wide combined pattern. This closes the feedback loop that
  C-24 leaves open: synthesis extraction results must alter the primary ranked artifact, not merely
  appear in a separate synthesis section. A report where the C-24 synthesis gate populates a
  pattern table but the ranked findings table is unchanged after synthesis = does not pass.
- **Pass condition**: The output contains a named blast radius re-assessment gate (or equivalent
  named step) that applies ELEVATED annotations -- or equivalent upward revisions -- to ranked
  findings whose blast radius changed due to cross-skill pattern extraction from C-24. A ranked
  findings table finalized before C-24 synthesis runs, or unchanged after synthesis, = does not
  pass.

---

## Scoring Summary Table

| ID   | Criterion                                              | Weight       | Category    | Points |
|------|--------------------------------------------------------|--------------|-------------|--------|
| C-01 | All five sub-skills execute                            | essential    | correctness | 12     |
| C-02 | Findings ranked by blast radius                        | essential    | format      | 12     |
| C-03 | System boundary + severity per finding                 | essential    | correctness | 12     |
| C-04 | At least one spec gap or contract violation            | essential    | coverage    | 12     |
| C-05 | Single synthesized report                              | essential    | format      | 12     |
| C-06 | Exception paths and edge cases                         | recommended  | depth       | 10     |
| C-07 | Findings cross-reference source sub-skill              | recommended  | coverage    | 10     |
| C-08 | State machine anomalies called out                     | recommended  | depth       | 10     |
| C-09 | Test scenario baseline derived from findings           | aspirational | behavior    | 1      |
| C-10 | Finding IDs assigned (F-NN pattern)                    | aspirational | behavior    | 1      |
| C-11 | CRITICAL/HIGH budget met per trace sub-skill           | aspirational | depth       | 1      |
| C-12 | Structured findings table, no blank cells              | aspirational | format      | 1      |
| C-13 | Flow findings reference trace context                  | aspirational | depth       | 1      |
| C-14 | System boundary vocabulary pre-assigned                | aspirational | correctness | 1      |
| C-15 | Universal sentinel rule across all columns             | aspirational | format      | 1      |
| C-16 | No-findings sentinel rows for clean sub-skills         | aspirational | format      | 1      |
| C-17 | Pre-output blank-cell verification gate                | aspirational | behavior    | 1      |
| C-18 | Unified schema closes C-03/C-07/C-10/C-13             | aspirational | format      | 1      |
| C-19 | Finding Type drawn from closed vocabulary              | aspirational | correctness | 1      |
| C-20 | Blast radius rationale for top-tier findings           | aspirational | depth       | 1      |
| C-21 | Exception path coverage tracked in named column        | aspirational | depth       | 1      |
| C-22 | Severity budget gate enforces trace-before-flow        | aspirational | behavior    | 1      |
| C-23 | Blast Rationale appears as named table column          | aspirational | format      | 1      |
| C-24 | Cross-skill synthesis gate extracts named patterns     | aspirational | depth       | 1      |
| C-25 | Severity drawn from closed four-value vocabulary       | aspirational | correctness | 1      |
| C-26 | Remediation quality gate produces extraction table     | aspirational | behavior    | 1      |
| C-27 | Entity coverage matrix maps manifest entities          | aspirational | coverage    | 1      |
| C-28 | Blast radius re-assessment gate propagates synthesis   | aspirational | depth       | 1      |

**Essential subtotal**: 60 pts (5 criteria x 12)  
**Recommended subtotal**: 30 pts (3 criteria x 10)  
**Aspirational subtotal**: 10 pts max (20 criteria x 1 pt each, capped at 10)  
**Max score**: 100  
**Golden threshold**: all of C-01--C-05 pass AND composite >= 80

---

## Usage Notes

- Run this rubric against outputs from /quest-variate to compare prompt variations.
- A run that passes C-01--C-05 but scores 60--79 is useful but shallow -- C-06 through
  C-08 are the depth signal.
- C-09 through C-28 are structural markers worth 1 pt each, capped at 10 pts total.
  Passing all 20 earns 10 pts (same as passing any 10). The cap means the last 10 passed
  represent excellence beyond the rubric ceiling, not extra score.
- C-11/C-22 are the trace-before-flow pair: C-11 requires the CRITICAL/HIGH budget is
  met; C-22 requires a named gate mechanism enforces this before flow executes. C-11
  passes when the output is correct; C-22 passes when the process is correct.
- C-20/C-23 are the blast-rationale pair: C-20 requires rationale sentences exist for
  top-tier findings; C-23 requires those sentences occupy a named table column. Same
  prose-to-structure upgrade relation as C-06/C-21.
- C-05/C-24 are the synthesis pair: C-05 requires one integrated report rather than five
  separate outputs; C-24 requires a named cross-skill synthesis gate step that extracts
  cross-cutting patterns. C-05 passes when the artifact is integrated; C-24 passes when
  the extraction process is explicit and documented.
- C-24/C-28 are the synthesis feedback-loop pair: C-24 extracts named cross-cutting
  patterns into a gate output; C-28 requires those patterns propagate back into the ranked
  findings table via ELEVATED annotations before finalization. C-24 passes when patterns
  are extracted; C-28 passes when those extractions alter the primary artifact.
- C-14/C-19/C-25 are the closed-vocabulary triple: C-14 closes System Boundary to 5
  labels, C-19 closes Finding Type to a named vocabulary, C-25 closes Severity to
  {CRITICAL, HIGH, MEDIUM, LOW} enforced by gate. Together they eliminate model judgment
  from the three fields most susceptible to hallucination drift across runs.
- C-16/C-27 are the sentinel coverage pair: C-16 requires a sentinel row for every
  sub-skill that executed (sub-skill granularity); C-27 requires a named Entity Coverage
  Matrix mapping every Topic Entity Manifest entity to COVERED/CLEAN/SKIPPED (entity
  granularity). A SKIPPED entity in C-27 is treated the same as a missing sub-skill row
  in C-16: both signal execution gaps.
- C-17/C-26 are the gate-quality pair: C-17 gates on cell completeness (no blanks);
  C-26 gates on remediation content quality (no vague entries). C-17 passes when all
  cells are filled; C-26 passes when each remediation is decomposed into Verb/Target/
  Location/Conformance columns -- the same prose-to-structure upgrade C-14 made to System
  Boundary labels.
- C-11 is the upstream guarantee: when all three trace sub-skills each contribute a
  CRITICAL/HIGH finding, C-09 closes by construction.
- C-12/C-15 are the no-blank-cell contract at two levels: required columns (C-12) and
  every column without exception (C-15). C-15 fails if any optional column is blank.
- C-16 is the silent-skip detector at sub-skill level; C-27 is the silent-skip detector
  at entity level. Silence cannot be used as evidence of a clean execution at either
  granularity.
- C-17 is the blank-cell process gate; C-24 is the synthesis process gate; C-26 is the
  remediation-quality gate; together they make completeness (no blanks), depth (cross-
  cutting patterns), and actionability (structured remediations) into explicit named steps
  whose outcomes appear in the artifact.
- C-18 is the schema integrity test: one table whose column set alone satisfies four other
  criteria. Multi-table designs fail C-18 regardless of per-table data correctness.
- C-13/C-21 make the two key simulation disciplines (trace-informed flow, exception-path
  completeness) verifiable by column scan rather than prose reading.
- Common failure modes: silent sub-skill skipping (C-01), five separate outputs with no
  synthesis (C-05), findings without severity labels (C-03), boundary labels inferred
  from prose (C-14), finding types not drawn from vocabulary (C-19), severity values
  outside four-value set (C-25), clean sub-skills absent from table (C-16), top-tier
  blast radius with no rationale (C-20/C-23), flow running before trace budget gate
  clears (C-22), no cross-skill patterns extracted from synthesis gate (C-24), synthesis
  patterns not propagated back into ranked table (C-28), remediation entries as vague
  checkboxes instead of Verb/Target/Location rows (C-26), manifest entities with no
  COVERED/CLEAN/SKIPPED accounting (C-27).
- v2 change: aspirational criteria expanded from 2 to 5; per-criterion points reduced
  from 5 to 2.
- v3 change: aspirational criteria expanded from 5 to 10; per-criterion points reduced
  from 2 to 1. Max score unchanged at 100.
- v4 change: aspirational criteria expanded from 10 to 13; section capped at 10 pts.
  Max score unchanged at 100.
- v5 change: aspirational criteria expanded from 13 to 17. Max score unchanged at 100.
- v6 change: aspirational criteria expanded from 17 to 20. Max score unchanged at 100.
