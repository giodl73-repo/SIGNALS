v15 is written: 1,254 lines, 52 named criteria (C-01 through C-55 headings), with all additions confirmed.

**Summary of changes from v14 to v15:**

**Three new aspirational criteria (C-53 through C-55):**

- **C-53** — *Table Schema Is the Scan-Sufficiency Proof* (format, C-50 activation): The column schema of the compliance verification table must contain no narrative field — schema design excludes forbidden fields by construction rather than by declaration. Ceiling above C-50. Column-scan sufficiency tower: C-47 → C-50 → C-53.

- **C-54** — *Standalone Named Axiom Block Enables Zero-Lookup Compliance Proof* (correctness, C-51 activation): A standalone named axiom block (e.g., SEVERITY AXIOM) must appear before the ECM; the compliance checklist cites axiom text + one Status cell label only, with no cross-column lookup. Ceiling above C-51. Entity coverage gap tower: C-27 → C-48 → C-51 → C-54 (four levels).

- **C-55** — *Match? Column Materializes Column-Equality Constraint as Scan-Visible Verification Primitive* (correctness, C-52 activation): The self-match audit table must have a dedicated Match? column (YES/NO per row) materializing the F-ID equality check as a scan-visible result. Violations detectable by column scan without reading cell content. Ceiling above C-52. Type-verb binding tower: C-31 → C-47 → C-49 → C-52 → C-55 (five levels).

**Updated sections:** Aspirational pool 44 → 47, 3 new floor/ceiling pairs in the relationship map, 2 extended towers + 1 new tower, 3 new round-by-round entries (all R16, V-01/V-02/V-03 as first-to-satisfy), scoring updated to "C-26 through C-55", R16 Variation Outcomes section replaces R15 reference.
Verb Source F-NN | Match?), materializing the F-ID equality check as a dedicated column. A NO entry is visible by scan without reading any Verb Source cell content. C-52's ceiling is the declared self-matching F-ID invariant; C-55 requires the equality check to be materialized as a scan-visible column primitive. Type-verb binding tower now five levels deep: C-31 -> C-47 -> C-49 -> C-52 -> C-55.

**Aspirational pool: 44 -> 47. Max score: 100 unchanged.**
Finding
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

Each passing criterion adds equal fractional weight up to the 10-point cap.
Exempt criteria do not count in numerator or denominator.

---

## Aspirational Criteria -- Round 1 (C-09 through C-10)

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

## Aspirational Criteria -- Rounds 2-4 (C-11 through C-21)

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

## Aspirational Criteria -- Round 5 (C-22 through C-25)

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

## Aspirational Criteria -- Round 6 additions (C-26 through C-28)

### C-26 . Remediation Quality Gate: Verb/Target/Location Table
- **Weight**: aspirational
- **Category**: format
- **Text**: The Remediation Quality Gate must produce a per-row structured table decomposing each
  remediation entry into Verb / Target / Location / Conformance columns. A checklist checkbox
  is structurally non-falsifiable; a Verb=add / Target=permission check /
  Location=CallHandler.process() row is verifiable by column scan.
- **Pass condition**: Every remediation entry appears as a structured row with all four columns
  populated. Prose remediation entries or blank cells in any column = fail.

---

### C-27 . Entity Coverage Matrix: COVERED / CLEAN / SKIPPED
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every entity in the Topic Entity Manifest must appear in a named Entity Coverage Matrix
  with an explicit COVERED / CLEAN / SKIPPED status. A SKIPPED entity is treated as an execution
  gap, not a clean run -- same disqualifying weight as a missing sub-skill sentinel row in C-16.
- **Pass condition**: Entity Coverage Matrix present; every manifest entity has a status; SKIPPED
  entities logged as execution gaps. Entities absent from the matrix = fail.

---

### C-28 . Blast Radius Re-Assessment Gate: ELEVATED Annotations
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-skill synthesis patterns must be propagated back into the ranked findings table
  via ELEVATED annotations citing the named pattern ID before the report is finalized. A
  synthesis gate that populates a P-ID table but leaves the ranked findings table unchanged
  satisfies C-24 but not C-28.
- **Pass condition**: At least one finding carries an ELEVATED annotation with a P-ID citation;
  the ranked table reflects re-ordering based on synthesis results. Synthesis section isolated
  from ranked table = fail.

---

## Aspirational Criteria -- Round 7 additions (C-29 through C-31)

### C-29 . Propagation Coverage Gate: Dependency Rules Audited
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every dependency rule declared in the cross-skill dependency map must be explicitly
  accounted for in the execution record: either honored (re-examined, finding recorded, rule ID
  cited) or logged as an OPEN PROPAGATION GAP with the rule ID and reason for non-execution.
  A dependency map that silently drops rules after synthesis satisfies C-28 but fails C-29.
- **Pass condition**: All declared dependency rule IDs appear in either the finding record or an
  OPEN PROPAGATION GAP log. Rules present in the map but absent from both = fail.

---

### C-30 . Confidence-Stratified Action List: Two Named Tracks
- **Weight**: aspirational
- **Category**: format
- **Text**: The final action list must be split into two named tracks by blast-radius x confidence
  quadrant: (1) HIGH-confidence / HIGH-blast -> implement fix immediately; (2) LOW-confidence /
  HIGH-blast -> confirm spec interpretation first, then implement. A single merged action list
  ordered only by blast radius satisfies C-02 but fails C-30.
- **Pass condition**: Two named action tracks present with findings assigned by quadrant. Merged
  single-track list, or tracks defined without confidence as a dimension = fail.

---

### C-31 . Finding Type Constrains Remediation Verb Vocabulary
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Each finding must be typed at detection as GAP / CONTRADICTION / ASSUMPTION. The
  remediation Verb must be constrained by type: GAP -> "add" or "remove"; CONTRADICTION ->
  "resolve"; ASSUMPTION -> "confirm". An ASSUMPTION-typed finding with Verb="add" fails C-31
  even if the remediation row is otherwise structurally complete under C-26. The type-verb
  binding makes remediation self-auditing -- an out-of-vocabulary verb signals mis-typing or
  mis-planning.
- **Pass condition**: All findings carry a type declaration; all remediation Verbs match the
  allowed vocabulary for that type. Out-of-vocabulary Verbs = fail. Untyped findings = fail.

---

## Aspirational Criteria -- Round 8 additions (C-32 through C-35)

### C-32 . Dependency Rules Carry Stable DR-NN IDs Enabling End-to-End Traceability
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every dependency rule in the cross-skill dependency map must carry a stable DR-NN
  identifier (e.g., DR-01, DR-02) that is cited consistently in three places: (1) the map
  declaration, (2) the Coverage Gate row for that rule, and (3) the evidence field of any finding
  that instantiates the rule. A Coverage Gate that accounts for rules by prose description without
  citing DR-NN IDs satisfies C-29 but fails C-32. The DR-NN identifier converts the gate from a
  narrative audit into a set-membership check: {declared DR-NNs} must equal {gate rows union gap
  log entries}; no rule may appear in one context but not the other.
- **Pass condition**: Each dependency rule in the cross-skill map carries a DR-NN ID; Coverage Gate
  rows cite the originating DR-NN; findings that instantiate a dependency rule cite the DR-NN in
  their evidence field. Rules present in the map with no ID, or Coverage Gate rows with no DR-NN
  backlink = fail.

---

### C-33 . Structural Axis Declaration and Compliance Checklist Self-Extend per Targeted Quality Axis
- **Weight**: aspirational
- **Category**: format
- **Text**: Each quality axis targeted by the simulation run (propagation coverage for C-29,
  confidence stratification for C-30, type-verb binding for C-31, etc.) must manifest as (a) a
  new named row in the Structural Axis Declaration with >=3 declared sub-observables, and (b) a
  corresponding verification row in the Compliance Checklist with >=3 sub-claims. A simulation
  that targets C-30 (confidence stratification) but runs a fixed-depth axis template without
  adding a confidence row satisfies C-22 but fails C-33. Axes not targeted by the simulation
  are exempt -- the self-extension requirement is per targeted axis only.
- **Pass condition**: Structural Axis Declaration contains one row per targeted quality axis, each
  with >=3 sub-observables; Compliance Checklist contains one verification row per axis row, each
  with >=3 sub-claims. Inherited fixed-depth template with no extension for targeted axes = fail.

---

### C-34 . Empty-State Templates Guard Structured Output Sections Against Silent Omission
- **Weight**: aspirational
- **Category**: format
- **Text**: Every structured output section that uses a schema and could legitimately contain no
  content -- action tracks (C-30), Coverage Gate (C-29), T-1 ANNEX (C-23), Entity Coverage Matrix
  (C-27) -- must provide a named empty-state template. The empty-state template shows the section's
  column headers and schema with no data rows, explicitly confirming that the section was executed
  and found nothing rather than silently skipped. A section that is simply absent when empty fails
  C-34; a section that shows its empty-state template passes.
- **Pass condition**: Each structured output section either contains content or displays a named
  empty-state template. Sections absent without either form = fail.

---

### C-35 . Confidence Rationale Field Makes Confidence Assignments Auditable
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every finding that carries a Confidence field (required by C-30 for HIGH-blast
  findings) must also carry a Conf rationale sub-field explaining the basis for the HIGH or LOW
  judgment. A finding that states "Confidence: HIGH" without a rationale satisfies C-30's label
  requirement but fails C-35. The rationale field converts a declaration into a falsifiable claim:
  "HIGH -- spec section 4.2 explicitly defines the permission boundary" can be verified; "HIGH"
  alone cannot. Findings below the HIGH-blast threshold that do not participate in C-30's
  stratification are exempt from the rationale requirement.
- **Pass condition**: Every finding assigned to a C-30 action track carries both a Confidence label
  (HIGH/LOW) and a non-empty Conf rationale. Confidence label without rationale = fail.
  Findings outside C-30 stratification are exempt.

---

## Aspirational Criteria -- Round 9 additions (C-36 through C-37)

### C-36 . Trace-First Sub-Skill Execution Order Pre-Loads Dependency Map Before Flow Evaluation
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The three trace sub-skills (trace-state, trace-contract, trace-permissions) must all
  complete before either flow sub-skill (flow-lifecycle, flow-conversation) begins. The cross-skill
  dependency map (C-29, C-32) is populated during trace execution: trace-state declares lifecycle
  transition rules, trace-contract declares boundary contract rules, trace-permissions declares
  permission enforcement rules. A flow finding that references a permission contract or lifecycle
  rule must be evaluated against a complete map; if the relevant trace sub-skill has not yet run,
  the DR-NN entry for that rule does not yet exist and the evaluation is performed against an
  incomplete map. Trace-first ordering eliminates this risk: by the time flow-lifecycle or
  flow-conversation executes, all platform-layer dependency rules are declared, numbered, and
  available for coverage gate lookup. A simulation that executes flow-lifecycle or flow-conversation
  before all three trace sub-skills complete satisfies C-01 but fails C-36. The constraint is not
  about thoroughness -- it is about evaluation correctness.
- **Pass condition**: Execution record shows trace-state, trace-contract, and trace-permissions
  completing before flow-lifecycle and flow-conversation begin. Any flow sub-skill that precedes
  any incomplete trace sub-skill = fail.

---

### C-37 . Structural Axis Declaration Achieves 1:1 Axis-to-Criterion Correspondence
- **Weight**: aspirational
- **Category**: format
- **Text**: The total number of rows in the Structural Axis Declaration must equal the total number
  of quality criteria targeted by the simulation run. C-33 requires each targeted axis to add a
  row (the floor); C-37 requires no targeted criterion to be absent from the declaration (the
  ceiling). A simulation targeting nine quality criteria must declare exactly nine axis rows. This
  1:1 invariant converts the Structural Axis Declaration from a depth-showing artifact into a
  completeness proof: a reviewer counts rows, counts targeted criteria, and verifies they match.
  If they do not match, at least one targeted criterion lacks a structural commitment and the
  report cannot be trusted to have honored it. A declaration with N-1 rows for an N-criterion
  run satisfies C-33 (it self-extended for each present axis) but fails C-37 (one targeted axis
  is structurally invisible). Untargeted criteria are exempt -- the count applies only to criteria
  the simulation explicitly targets.
- **Pass condition**: Row count in the Structural Axis Declaration equals the count of targeted
  quality criteria for the simulation run. Each targeted criterion maps to exactly one declared
  axis row; no targeted criterion is absent; no row represents an untargeted criterion. Count
  mismatch in either direction = fail.

---

## Aspirational Criteria -- Round 10 additions (C-38 through C-40)

### C-38 . Execution Order Gate Achieves Machine-Readable Three-Path Structural Verification
- **Weight**: aspirational
- **Category**: format
- **Text**: The execution order constraint (C-36) must be independently verifiable through three
  structural mechanisms, not prose narrative alone. The three required paths are: (1) a Layer
  Completion Record table with a Status column that transitions to COMPLETE as each trace
  sub-skill finishes, showing all three Platform sub-skills at COMPLETE before any Domain
  sub-skill begins; (2) an explicit gate signal statement placed between the last Platform step
  and the first Domain step, naming all three Platform sub-skills by name and declaring the
  gate open; (3) an Execution Log with a Layer column classifying each step as Platform or
  Domain, enabling verification by row-layer inspection independent of the gate signal. V-03
  (R10) established that correct execution order satisfies C-36 but not C-38: the Layer Sequence
  Rule paragraph named both layers and stated the ordering constraint, but produced no machine-
  readable completion record. A reviewer verifying C-38 must be able to confirm the execution
  order through each of the three paths independently; a prose description of the constraint
  does not enable this. C-38 is the verifiability ceiling that C-36's correctness floor cannot
  enforce alone.
- **Pass condition**: Execution Order Gate section contains all three structural mechanisms: a
  Layer Completion Record table with a Status column showing Platform sub-skills completing
  before Domain sub-skills begin; an explicit gate signal statement naming all three Platform
  sub-skills by name; and an Execution Log with a Layer column. Prose description of ordering
  constraint without a structured gate table = fail. Any of the three structural paths absent
  = fail.

---

### C-39 . Execution Order Gate Signal Certifies Both Execution Order and Dependency Map Completeness
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When both C-32 (DR-NN IDs) and C-36 (trace-first execution order) are co-targeted,
  the gate signal that fires at the Platform-to-Domain transition must certify two properties
  simultaneously: (1) all three trace sub-skills have completed, and (2) the dependency map
  contains a complete set of declared DR-NN rules, confirmed by explicit range or count in the
  gate signal itself (e.g., "Dependency rules DR-01 through DR-N are fully declared"). A gate
  signal that certifies execution order alone satisfies C-36 and C-38 but fails C-39. The dual
  certification closes a race that single-property certification cannot detect: a trace sub-skill
  may complete in the correct execution order while failing to declare all its dependency rules,
  leaving the dependency map incomplete even though the execution order gate has fired. The rule
  count or range must appear in the gate signal itself -- not deferred to a separate Coverage Gate
  section. V-01 (R10) achieved C-38 via three-path gate table but its gate signal certified
  execution order only, not dependency map completeness; V-05 (R10) coupled both properties in a
  single gate signal, satisfying C-39. C-39 applies only when both C-32 and C-36 are co-targeted;
  simulations targeting C-36 without C-32 are exempt.
- **Pass condition**: Gate signal statement names all three Platform sub-skills as complete AND
  includes an explicit rule count or range confirming the dependency map is fully declared
  (e.g., "DR-01 through DR-N are fully declared"). Gate signal certifying execution order without
  a rule-count confirmation = fail. C-39 exempt if C-32 is not co-targeted.

---

### C-40 . Row Count Assertion Is Self-Referential When C-37 Is Targeted
- **Weight**: aspirational
- **Category**: format
- **Activation condition**: C-37 targeted
- **Text**: When C-37 is targeted, the Row Count Assertion block must enumerate the targeted axes
  by name, and the declaration-completeness-proof axis row (the C-37 axis) must appear by name
  in that enumerated list. This makes the Row Count Assertion self-referential: the completeness
  proof explicitly counts itself as one of the N items it is proving complete. A Row Count
  Assertion that states "N rows, N targeted axes, N==N" without enumerating the axes by name
  satisfies C-37 (the count is correct) but fails C-40 (the self-reference cannot be verified
  by name inspection). The requirement is that the C-37 axis row appear explicitly in the named
  axis list, not merely be present in the declaration and implicitly counted. V-04 (R10) achieved
  C-37 by construction -- the Row Count Assertion stated the correct count -- but did not
  enumerate the axes, so the self-reference was implicit. V-05 (R10) explicitly listed all N
  targeted axes in the assertion block with the C-37 declaration-completeness-proof axis named
  among them, making the proof apply recursively to itself. C-40 is the self-reference ceiling
  that C-37's count floor cannot enforce alone. C-40 applies only when C-37 is targeted.
- **Pass condition**: Row Count Assertion block enumerates the targeted axes by name; the
  declaration-completeness-proof / C-37 axis appears by name in the enumerated list. Row Count
  Assertion with correct count but no named axis enumeration = fail. C-37 axis absent from the
  named list = fail. C-40 exempt if C-37 is not targeted.

---

## Aspirational Criteria -- Round 11 additions (C-41 through C-43)

### C-41 . Gate Signal P1/P2 Decomposition Provides Per-Sub-Skill DR-NN Attribution
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-39 targeted (i.e., C-32 + C-36 co-targeted)
- **Text**: C-39 requires the gate signal to certify both execution order (P1 property) and
  dependency map completeness (P2 property) in a single firing. C-41 extends C-39 by requiring
  the gate signal to be structurally decomposed into two explicit, labeled parts -- P1 and P2 --
  where P2 provides per-sub-skill DR-NN attribution rather than an aggregate rule count alone.
  The P2 attribution takes the form: N1 rules from trace-state + N2 rules from trace-contract +
  N3 rules from trace-permissions = N_total, with the addition sum explicitly confirmed. A gate
  signal that states the aggregate total ("N dependency rules fully declared") satisfies C-39 but
  fails C-41 because a reviewer cannot detect a mismatch between per-sub-skill scope and claimed
  rule counts without the breakdown. The P1/P2 decomposition converts the gate signal from an
  aggregate assertion into a scope-attribution trace: each trace sub-skill's contribution is
  individually verifiable, and a discrepancy between expected scope and declared count is
  detectable by arithmetic. V-02 (R11) is the first variation to achieve C-41: P1 certified
  execution order by naming all three Platform sub-skills, and P2 certified dependency map
  completeness with explicit per-sub-skill attribution (N1 + N2 + N3 = N_total addition
  confirmation). A C-39-passing gate signal that certifies aggregate rule count without
  per-sub-skill breakdown satisfies C-39, fails C-41. C-41 is the per-sub-skill attribution
  ceiling that C-39's aggregate-count floor cannot enforce alone.
- **Pass condition**: Gate signal contains a labeled P1 statement certifying execution order
  (naming all three Platform sub-skills as complete) and a labeled P2 statement certifying
  dependency map completeness with per-sub-skill rule count breakdown (N1 + N2 + N3 = N_total,
  with the sum explicitly confirmed). P2 statement without per-sub-skill breakdown = fail.
  Unlabeled gate signal that mixes both properties in a single sentence = fail. C-41 exempt if
  C-39 is not targeted.

---

### C-42 . Row Count Assertion Self-Reference Appears as Opening Sentence for Zero-Scan Verification
- **Weight**: aspirational
- **Category**: format
- **Activation condition**: C-40 targeted (i.e., C-37 targeted)
- **Text**: C-40 requires the Row Count Assertion to enumerate targeted axes by name with the
  C-37 axis appearing in that list, enabling the self-reference to be confirmed by list scan.
  C-42 extends C-40 by requiring the self-referential property to be stated in the opening
  sentence of the Row Count Assertion block, enabling verification without scanning the axis
  list at all. A Row Count Assertion that satisfies C-40 by naming the C-37 axis somewhere in
  an enumerated list requires a reviewer to read the entire list to confirm the self-reference
  is present. A Row Count Assertion satisfying C-42 declares the self-referential property
  explicitly in its first sentence -- e.g., "This Row Count Assertion is itself C-37's
  completeness proof and appears as the final axis listed below" -- so the C-40 property is
  verifiable from the opening sentence alone without list scan. V-03 (R11) achieved C-42: the
  opening sentence stated the self-referential property in full, making C-40 verifiable at
  first-sentence scope. V-05 (R10), which first satisfied C-40, listed the C-37 axis among the
  enumerated axes but placed the self-reference within the list rather than as an opening-sentence
  preamble; it satisfies C-40, fails C-42. C-42 is the zero-scan ceiling that C-40's
  named-enumeration floor cannot enforce alone.
- **Pass condition**: The Row Count Assertion block begins with an opening sentence that
  explicitly declares the self-referential property: the assertion is itself C-37's completeness
  proof and will appear as a named item in the axis list that follows. C-40-passing assertion
  that places the C-37 axis within the enumerated list without an opening-sentence preamble
  declaration = fail. C-42 exempt if C-40 is not targeted.

---

### C-43 . Execution Log DR-NN Contributed Column Enables Step-Level Rule Attribution
- **Weight**: aspirational
- **Category**: format
- **Activation condition**: C-38 targeted
- **Text**: C-38 requires three structural paths for execution order verification: Layer
  Completion Record table, gate signal naming all three Platform sub-skills, and Execution Log
  with Layer column. C-43 extends C-38 by adding a fourth structural path: a DR-NN Contributed
  column in the Execution Log that records, per execution step, the specific DR-NN rule(s) that
  step contributed to the dependency map, or an explicit zero-contribution template for steps
  that declare no rules. This fourth path creates a step-to-rule attribution map that is
  independently verifiable from the Execution Log alone: a reviewer can scan the DR-NN
  Contributed column, reconstruct the full set of declared rules from step-level contributions,
  and confirm that the union of all Contributed entries matches the declared dependency map.
  The DR-NN Contributed column also provides the structural foundation for C-41's per-sub-skill
  attribution: the P2 gate signal's per-sub-skill rule counts can be verified against the
  Contributed column without consulting the dependency map separately. V-01 (R11) added the
  DR-NN Contributed column as an additive mechanism beyond C-38's three required paths -- the
  first variation to achieve C-43. A simulation satisfying C-38 with all three structural paths
  but no DR-NN Contributed column in the Execution Log satisfies C-38, fails C-43. C-43 is the
  step-level attribution ceiling that C-38's layer-classification floor cannot enforce alone.
- **Pass condition**: Execution Log contains a DR-NN Contributed column; each trace sub-skill
  execution step lists the specific DR-NN rule(s) contributed (or a named zero-contribution
  template if the step contributes no rules); the union of all DR-NN Contributed entries across
  the Execution Log equals the full set of declared DR-NNs in the dependency map. Execution Log
  without DR-NN Contributed column = fail. Step rows with no Contributed entry and no
  zero-contribution template = fail. C-43 exempt if C-38 is not targeted.

---

## Aspirational Criteria -- Round 12 additions (C-44 through C-46)

### C-44 . Row Count Assertion Opening Sentence Embeds Both C-37 Count Invariant and C-42 Self-Reference Simultaneously
- **Weight**: aspirational
- **Category**: format
- **Activation condition**: C-42 targeted (i.e., C-40 + C-37 targeted)
- **Text**: C-42 requires the self-referential property to appear in the opening sentence of the
  Row Count Assertion block, enabling C-40 verification without list scan. C-44 extends C-42 by
  requiring that same opening sentence to simultaneously declare the C-37 count invariant inline
  -- in the form "this assertion is itself the Nth and final of the N targeted axes declared
  below" -- so that both the self-reference (C-42) and the count proof (C-37) are verifiable
  from a single sentence without reading further. A Row Count Assertion satisfying C-42 places
  the self-referential declaration in its opening sentence but may confirm the count invariant
  (N rows == N targeted criteria) separately in a subsequent line, requiring a reader to continue
  past the opening sentence to verify C-37. A Row Count Assertion satisfying C-44 embeds the
  count directly in the opening sentence: one sentence simultaneously confirms self-reference and
  count invariant, and both properties are verifiable at zero-scan scope with no additional
  reading. V-03 (R11) achieved C-42 at 6-axis scope but confirmed the count separately; V-05
  (R12) scaled to 12 axes and embedded the count inline ("itself the 12th and final of the 12
  targeted axes declared below"), satisfying C-44 for the first time. C-44 is the dual-property
  zero-scan ceiling that C-42's single-property zero-scan floor cannot enforce alone.
- **Pass condition**: The Row Count Assertion block's opening sentence declares both (a) the
  self-referential property (this assertion is itself C-37's completeness proof) and (b) the
  count invariant (the Nth and final of N targeted axes) in the same sentence. Opening sentence
  that declares self-reference without embedding the count inline = fail. C-37 count invariant
  confirmed only in a subsequent sentence = fail. C-44 exempt if C-42 is not targeted.

---

### C-45 . Mechanism Criterion Promoted to First-Class SAD Axis for Declaration-Level Verification
- **Weight**: aspirational
- **Category**: format
- **Activation condition**: C-43 targeted (i.e., C-38 targeted)
- **Text**: C-43 requires the Execution Log to carry a DR-NN Contributed column (the fourth
  structural path beyond C-38's three required paths). In simulations targeting C-33's
  self-extension requirement, this fourth structural path is typically declared as an extension
  within the C-38 execution-order axis row -- a mechanism enrichment inside an existing axis
  rather than an independent declaration. C-45 requires that the C-43 mechanism be promoted to
  a dedicated, named axis row in the Structural Axis Declaration with >=3 independently-verifiable
  sub-observables. The promotion creates a declaration that can be verified from the SAD section
  alone, without reading the Execution Order Gate section: a reviewer confirms C-43 compliance
  by checking the dedicated axis row's sub-observables against the Execution Log's DR-NN
  Contributed column, independent of whether the gate section was read. The two checks -- SAD
  axis row (C-45) and Execution Log column presence (C-43) -- become independently falsifiable:
  a simulation could satisfy C-43 (column present) while failing C-45 (no dedicated SAD row),
  and vice versa. A simulation that satisfies C-43 by recording the DR-NN Contributed column
  but embeds the declaration inside C-38's axis row satisfies C-43, fails C-45. V-05 (R12) is
  the first variation to achieve C-45: the 12th SAD axis row was named "Execution-log attribution
  axis" with three independently-verifiable sub-observables covering the Contributed column,
  union-of-rows equality, and compliance checklist sub-claims. C-45 is the SAD-level declaration
  ceiling that C-43's column-presence floor cannot enforce alone.
- **Pass condition**: Structural Axis Declaration contains a dedicated named row for the Execution
  Log attribution mechanism (C-43) with >=3 sub-observables, each independently verifiable from
  the Execution Log's DR-NN Contributed column. C-43 declared as extension or sub-item within
  C-38's axis row = fail. Dedicated SAD row with fewer than 3 sub-observables = fail. C-45 exempt
  if C-43 is not targeted.

---

### C-46 . P2 Sub-Entries Cross-Cite Execution Log Row by Name for Bidirectional Closed Verification
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-41 targeted (i.e., C-39 + C-32 + C-36 co-targeted)
- **Text**: C-41 requires the P2 gate signal component to break down rule counts by sub-skill
  scope with arithmetic confirmation (N1 + N2 + N3 = N_total). The P2 attribution is
  unidirectional: the gate signal asserts a count; a reviewer verifies it by scanning the
  dependency map or Execution Log separately, with no declared structural link between the two.
  C-46 extends C-41 by requiring each P2 sub-entry to cross-cite the specific Execution Log row
  by name that contributed those rules -- e.g., "N1 rules from trace-state [Execution Log: row
  1 -- trace-state, DR-NN Contributed: DR-01, DR-02]". The citation creates a bidirectional
  verification loop: read P2 sub-entry -> locate named Execution Log row -> confirm DR-NN
  Contributed column entries sum to the declared count. The same discrepancy is detectable in
  the reverse direction: scan Execution Log DR-NN Contributed column -> confirm P2 sub-entry
  cites this row and matches the count. Without the Execution Log cross-cite, the P2 arithmetic
  and the Execution Log remain independent artifacts; a count discrepancy between them is only
  detectable by a reviewer who chooses to compare both. The bidirectional citation converts the
  two artifacts into a closed integrity contract where any discrepancy is structurally visible
  from either endpoint. V-05 (R12) is the first variation to achieve C-46: P2 sub-entries cited
  the Execution Log row by name AND the Execution Log's DR-NN Contributed column carried entries
  traceable back to the P2 counts. C-46 is the bidirectional verification ceiling that C-41's
  arithmetic-attribution floor cannot enforce alone.
- **Pass condition**: Each P2 sub-entry names the specific Execution Log row it corresponds to
  by row identifier or sub-skill name; the cited row's DR-NN Contributed column entries are
  consistent with the P2-declared count; the union of all P2 cross-citations covers the full
  set of Execution Log trace-step rows. P2 sub-entries with correct arithmetic attribution but
  no Execution Log row cross-cite = fail. Named Execution Log row whose Contributed entries
  contradict the P2 count = fail. C-46 exempt if C-41 is not targeted.

---

## Aspirational Criteria -- Round 13 additions (C-47 through C-49)

### C-47 . Findings Table Carries Verb Column at Detection Time for Cross-Artifact Type-Verb Binding Verification
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-31 targeted
- **Text**: C-31 requires the remediation Verb in the RQG to match the allowed vocabulary for the
  finding's Type (GAP / CONTRADICTION / ASSUMPTION). The constraint is single-artifact: the Verb
  appears once, in the RQG, and is checked against the Type declared in the same row. C-47
  extends C-31 by requiring the Verb to also appear in the Findings Table at detection time --
  the point where the finding is first recorded and typed -- creating a second independently-
  verifiable location for the Type-Verb binding. The two appearances are independently falsifiable:
  a discrepancy between the Findings Table Verb and the RQG Verb is structurally visible by
  cross-artifact column scan without narrative reasoning. A simulation satisfying C-31 via RQG
  Verb alone satisfies C-31 but fails C-47: the Verb exists only in the remediation artifact;
  the detection artifact carries no Verb; no cross-artifact check is possible. V-02 (R14) is the
  first variation to achieve C-47: the Findings Table carried a Verb column populated at detection
  time, enabling C-31 verification from both the detection and remediation artifacts independently.
  C-47 is the dual-artifact detection ceiling that C-31's single-artifact floor cannot enforce alone.
- **Pass condition**: Findings Table contains a Verb column populated at detection time alongside
  the finding's Type; each finding's Findings Table Verb is consistent with its RQG Verb; the
  Type-Verb vocabulary constraint (C-31) is verifiable from the Findings Table alone without
  consulting the RQG. Findings Table without Verb column = fail. Cross-artifact Verb mismatch
  between Findings Table and RQG = fail. C-47 exempt if C-31 is not targeted.

---

### C-48 . Entity Coverage Matrix SKIPPED Entries Distinguish Commitment-Present from None-Declared
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-27 targeted
- **Text**: C-27 requires every entity in the Topic Entity Manifest to appear in the Entity
  Coverage Matrix with an explicit COVERED / CLEAN / SKIPPED status, treating SKIPPED as an
  execution gap. All SKIPPED entries carry the same weight: a gap is a gap. C-48 extends C-27
  by requiring SKIPPED entries to carry a tier label distinguishing two structurally different
  gap types: (1) commitment-present -- an Examining Sub-Skill was declared for this entity in
  the TEM before execution but was not executed at runtime, signaling a promise-breach gap; (2)
  none-declared -- no Examining Sub-Skill was ever committed for this entity in the TEM,
  signaling a planning gap. The two-tier signal requires that the Examining Sub-Skill commitment
  be recorded in the TEM before execution begins, converting the TEM from a passive manifest
  into a pre-execution commitment register. A flat SKIPPED log without tier distinction satisfies
  C-27 but fails C-48: a reviewer cannot determine whether a skipped entity was ever targeted for
  examination, only that it was skipped. The tier label converts the binary gap flag into an
  auditable signal that distinguishes missed commitments from absent planning. V-03 (R14) is the
  first variation to achieve C-48: an Examining Sub-Skill column was added to the TEM before
  execution, and the ECM's SKIPPED entries carried tier labels reflecting whether a commitment had
  been declared. C-48 is the commitment-aware gap ceiling that C-27's binary-gap floor cannot
  enforce alone.
- **Pass condition**: ECM SKIPPED entries carry a tier label distinguishing commitment-present
  (Examining Sub-Skill declared in TEM but not executed) from none-declared (no Examining
  Sub-Skill committed in TEM); the TEM contains an Examining Sub-Skill column populated before
  execution begins. Flat SKIPPED log without tier distinction = fail. ECM SKIPPED entries with
  no tier label = fail. C-48 exempt if C-27 is not targeted.

---

### C-49 . RQG Verb Source Column Creates Three-Point Cross-Artifact Type-Verb-Source Chain
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-47 targeted (i.e., C-31 targeted + Findings Table Verb column present)
- **Text**: C-47 requires the Verb to appear in both the Findings Table (at detection) and the
  RQG (at remediation), enabling cross-artifact consistency verification. The two-point chain is
  a consistency check: Findings Table Verb must equal RQG Verb. C-49 extends C-47 by requiring
  the RQG to carry a Verb Source column that explicitly names the Findings Table row from which
  the RQG Verb was derived, creating a three-point chain: Findings Table Verb (detection) ->
  RQG Verb (remediation) -> Verb Source column (explicit back-cite to detection entry). The
  Verb Source cross-cite creates a bidirectional closed integrity contract: a reviewer can
  traverse the chain from either endpoint -- Findings Table -> Verb Source cite -> confirm RQG
  Verb matches (forward); RQG Verb -> Verb Source backlink -> confirm Findings Table entry
  (reverse) -- and a discrepancy is structurally detectable from either direction without
  narrative reasoning. A simulation satisfying C-47 (both Verb columns consistent, no Verb
  Source column) satisfies C-47 but fails C-49: the consistency is present but the structural
  citation is absent; a reviewer must choose to compare both artifacts rather than following
  a declared link. V-04 (R14) is the first variation to achieve C-49: the RQG carried a six-
  column schema (Verb / Target / Location / Conformance / Blast Status / Verb Source) where
  the Verb Source column named the originating Findings Table entry, creating the full three-
  point bidirectional chain. C-49 is the cited-provenance ceiling that C-47's cross-consistency
  floor cannot enforce alone.
- **Pass condition**: RQG contains a Verb Source column that names the specific Findings Table
  row each RQG Verb was derived from; the cited Findings Table entry's Verb is consistent with
  the RQG Verb; the chain is verifiable in both directions from either endpoint. RQG without
  Verb Source column = fail. Verb Source column present but citing a Findings Table entry whose
  Verb differs from the RQG Verb = fail. C-49 exempt if C-47 is not targeted.

---

## Aspirational Criteria -- Round 15 additions (C-50 through C-52)

### C-50 . C-47 Compliance Declared as Column-Scan Sufficiency via Verbatim Field-Exclusion Proof
- **Weight**: aspirational
- **Category**: format
- **Activation condition**: C-47 targeted (i.e., C-31 targeted + Findings Table Verb column present)
- **Text**: C-47 requires the Verb to appear in both the Findings Table and the RQG, enabling
  cross-artifact Type-Verb consistency verification. C-47's ceiling is cross-consistency: both
  columns present and consistent. C-50 extends C-47 by requiring that the cross-verification be
  proven column-scan-sufficient by a verbatim field-exclusion declaration. Three structural
  elements are required: (1) a named "COLUMN-SCAN SURFACE (C-47)" annotation in the Findings
  Table Verb field schema that names exactly which columns are included in the scan (FT Verb,
  RQG Verb) and which narrative fields are explicitly excluded; (2) a checklist enumeration that
  lists all (F-ID, Verb) pairs from both the Findings Table and the RQG without referencing any
  narrative field; (3) a verbatim sufficiency declaration stating that C-47 was verified without
  reading Summary, Impact, Remediation, or any other narrative field. The verbatim declaration
  is itself the falsifiable assertion: any finding whose C-47 compliance actually required
  narrative reading contradicts sub-claim 3 at first instance. A simulation satisfying C-47
  (Verb columns present and consistent) but without a verbatim sufficiency declaration satisfies
  C-47, fails C-50. The declared sufficiency converts the column-scan claim from an implicit
  property of the artifact into an explicit, auditable commitment. V-01 (R15) is the first
  variation to achieve C-50. C-50 is the declared-sufficiency ceiling that C-47's
  cross-consistency floor cannot enforce alone.
- **Pass condition**: Findings Table Verb field schema carries a "COLUMN-SCAN SURFACE (C-47)"
  annotation naming included and excluded fields; compliance checklist enumerates all (F-ID,
  Verb) pairs without referencing narrative fields; checklist contains a verbatim sufficiency
  declaration confirming C-47 was verified without reading any narrative field. Missing schema
  annotation = fail. Verbatim sufficiency declaration absent = fail. Enumeration that references
  any narrative field = fail. C-50 exempt if C-47 is not targeted.

---

### C-51 . ECM SKIPPED Tier Label Is Status-Cell-Local, Enabling Single-Column Tier Verification
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-48 targeted (i.e., C-27 targeted + two-tier SKIPPED labels present)
- **Text**: C-48 requires SKIPPED entries in the Entity Coverage Matrix to carry a tier label
  distinguishing commitment-present (T1, promise-breach gap) from none-declared (T2, planning
  gap), with the tier derivable by comparing the ECM Status column to the Examining Sub-Skill
  column in the TEM. C-48's ceiling is commitment-aware tier distinction; C-51 extends C-48 by
  requiring the tier to be determinable from the Status cell value alone without cross-referencing
  the Examining Sub-Skill column. The tier is embedded directly in the Status cell:
  "SKIPPED-T1 (commitment-present)" or "SKIPPED-T2 (none-declared)". A tier derivation rule
  written above the ECM table makes the encoding explicit and auditable. This status-cell
  locality property means a reviewer scanning only the Status column can distinguish promise-
  breach gaps from planning gaps: no secondary column lookup is required. C-48 can be satisfied
  by a SKIPPED label with tier information only derivable by cross-referencing the Examining
  Sub-Skill column; C-51 requires the tier to be structurally encoded in the Status cell value
  itself. A bare "SKIPPED" label in the Status cell with tier derivable only from the Examining
  Sub-Skill column satisfies C-48, fails C-51. V-02 (R15) is the first variation to achieve
  C-51: Status cells carried "SKIPPED-T1 (commitment-present)" or "SKIPPED-T2 (none-declared)"
  with an explicit derivation rule above the ECM, making tier verification column-local.
  C-51 is the status-local tier ceiling that C-48's two-tier-label floor cannot enforce alone.
- **Pass condition**: ECM Status cell values for skipped entities carry explicit tier-embedded
  labels ("SKIPPED-T1 (commitment-present)" or "SKIPPED-T2 (none-declared)"); a tier derivation
  rule appears above the ECM table making the encoding auditable; tier determination requires
  only scanning the Status column with no cross-reference to the Examining Sub-Skill column.
  SKIPPED entries with tier information derivable only by comparing two columns = fail. Status
  cells labeled "SKIPPED" without embedded tier suffix = fail. C-51 exempt if C-48 is not
  targeted.

---

### C-52 . RQG Verb Source Carries DETECTION/CORRECTED Classification with Self-Matching F-ID for Structurally Self-Verifying Chain
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-49 targeted (i.e., C-47 targeted + RQG Verb Source column present)
- **Text**: C-49 requires the RQG Verb Source column to name the originating Findings Table row,
  creating a three-point bidirectional chain. The citation is a provenance claim; its accuracy
  is verifiable but not self-evident from the cell value alone. C-52 extends C-49 by requiring
  the Verb Source column to carry two additional structural properties: (1) a
  DETECTION/CORRECTED classification prefix making the type of binding event explicit at a glance
  -- "DETECTION: FT[F-NN].Verb=[Verb]" for clean cases where the RQG Verb matches the FT Verb
  at detection, or "CORRECTED: FT[F-NN].Verb=[old]->[new]; bind failure declared" for cases
  where a correction was needed; (2) a self-matching F-ID constraint requiring the F-NN cited in
  the Verb Source to equal the RQG row's own F-ID. The self-match converts the back-cite from a
  narrative claim into a structural invariant: F-ID(RQG row) == F-NN(Verb Source) is a
  column-value equality check verifiable by inspection without tracing to the Findings Table.
  CORRECTED entries explicitly declare a bind failure, making all detection-vs-remediation Verb
  divergences structurally flagged rather than silently inconsistent. A Verb Source column
  satisfying C-49 (originating FT row named) but without DETECTION/CORRECTED classification and
  without the self-matching F-ID constraint satisfies C-49, fails C-52. V-03 (R15) is the first
  variation to achieve C-52. C-52 is the classified-self-verifying-citation ceiling that
  C-49's cited-provenance floor cannot enforce alone.
- **Pass condition**: Each RQG Verb Source cell carries a DETECTION or CORRECTED prefix; the
  F-NN cited in the Verb Source matches the RQG row's own F-ID (self-matching constraint);
  CORRECTED entries include both the old and new Verb values and an explicit bind-failure
  declaration. Verb Source cells without DETECTION/CORRECTED prefix = fail. F-NN in Verb
  Source that does not match the RQG row's F-ID = fail. CORRECTED entry without explicit
  bind-failure declaration = fail. C-52 exempt if C-49 is not targeted.

---

## Aspirational Criteria -- Round 16 additions (C-53 through C-55)

### C-53 . Table Schema Is the Scan-Sufficiency Proof: Column Set Excludes Forbidden Fields by Construction
- **Weight**: aspirational
- **Category**: format
- **Activation condition**: C-50 targeted (i.e., C-47 targeted + verbatim sufficiency declaration present)
- **Text**: C-50 requires a verbatim sufficiency declaration asserting that C-47 cross-verification
  required no narrative field reading. The declaration is a human assertion -- falsifiable but not
  self-enforcing. C-53 extends C-50 by requiring the scan-sufficiency property to be established
  by the column schema of the compliance verification table itself, not merely declared by a
  sentence. A K-column table whose schema contains only structural columns (e.g., F-ID | FT Verb
  | RQG Verb) and no narrative column cannot silently include narrative context: the schema design
  excludes narrative reading by construction. An author attempting to add a Summary or Impact
  column would violate the schema before any compliance claim is made. The verbatim declaration
  in C-50 asserts that narrative was not read; the column schema in C-53 makes narrative reading
  structurally impossible by schema omission. A simulation satisfying C-50 (verbatim declaration
  present) but whose verification table schema includes any narrative column satisfies C-50, fails
  C-53. A simulation satisfying C-50 but whose verification table has no declared schema -- where
  scan-sufficiency relies entirely on the declaration sentence -- satisfies C-50, fails C-53.
  V-01 (R16) is the first variation to achieve C-53: the COLUMN-SCAN SURFACE table's 3-column
  schema (F-ID | FT Verb | RQG Verb) contains no narrative column, making the scan-sufficiency
  claim provable from the schema by inspection. C-53 is the schema-enforced ceiling that C-50's
  declaration-based floor cannot enforce alone.
- **Pass condition**: The compliance verification table for C-47/C-50 carries an explicit column
  schema declaration that contains no narrative field (no Summary, Impact, Remediation, or
  equivalent); the schema design itself is the scan-sufficiency proof; the verbatim declaration
  in C-50 is verifiable by schema inspection rather than trust alone. Verification table with no
  declared schema = fail. Schema that includes any narrative column = fail. C-53 exempt if C-50
  is not targeted.

---

### C-54 . Standalone Named Axiom Block Enables Zero-Lookup Compliance Proof from Axiom Text + Cell Value
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-51 targeted (i.e., C-48 targeted + Status-cell-local tier labels present)
- **Text**: C-51 requires the ECM tier label to be determinable from the Status cell value alone,
  eliminating the cross-reference to the Examining Sub-Skill column. The tier is embedded in the
  Status cell string itself. The derivation mechanism in C-51 can be any rule or convention
  visible in the document -- the requirement is structural locality of the tier label, not the
  derivation source. C-54 extends C-51 by requiring the tier ordering to be derivable from a
  standalone named axiom block that appears immediately before the ECM table. The axiom block
  pre-states the ordering claim as a named proposition -- e.g., "SEVERITY AXIOM: T1 severity >
  T2 severity. T1 = promise-breach. T2 = planning gap." The compliance checklist sub-claim for
  the SKIPPED-tier axis then cites axiom text + one ECM Status cell label only, with no
  cross-column lookup, no Examining Sub-Skill column, no finding content. The axiom-first
  structure decouples the derivation from all table structure: a reviewer can derive the tier
  ordering from the axiom text alone, verify that the Status cell label matches the axiom-defined
  tier, and confirm compliance without reading any other column or row. A simulation satisfying
  C-51 (Status-cell-local tier, no cross-reference) but without a standalone named axiom block
  satisfies C-51, fails C-54: the tier is locally derivable but the derivation source is embedded
  in the Status cell label itself rather than declared as a named standalone proposition. V-02
  (R16) is the first variation to achieve C-54: a SEVERITY AXIOM block was written as a
  standalone named block before the ECM; the Tier severity axiom SAD axis confirmed axiom-block
  presence as a declared sub-observable; the compliance checklist sub-claim 3 cited axiom text +
  Status cell label with the required declaration "gap ordering derived from SEVERITY AXIOM; no
  sub-skill column or finding content consulted." C-54 is the axiom-first zero-lookup ceiling
  that C-51's status-local tier floor cannot enforce alone.
- **Pass condition**: A standalone named axiom block appears immediately before the ECM table
  pre-stating the tier ordering as a named proposition; the compliance checklist sub-claim for
  the SKIPPED-tier axis cites axiom text + one Status cell label only with no cross-column
  lookup; a Tier severity axiom SAD axis is declared with the axiom-block presence as a
  verifiable sub-observable; the checklist contains the required declaration "gap ordering
  derived from SEVERITY AXIOM; no sub-skill column or finding content consulted." Status-cell-
  local tier present but no standalone named axiom block = fail. Axiom block present but not
  cited by the compliance checklist sub-claim = fail. Checklist sub-claim that references the
  Examining Sub-Skill column in addition to axiom text = fail. C-54 exempt if C-51 is not
  targeted.

---

### C-55 . Match? Column Materializes Column-Equality Constraint as Scan-Visible Verification Primitive
- **Weight**: aspirational
- **Category**: correctness
- **Activation condition**: C-52 targeted (i.e., C-49 targeted + DETECTION/CORRECTED prefix + self-matching F-ID present)
- **Text**: C-52 requires the RQG Verb Source to carry a self-matching F-ID constraint: the F-NN
  cited in the Verb Source must equal the RQG row's own F-ID, converting the back-cite from a
  narrative claim into a structural invariant. The self-match invariant is declared but not
  materialized as a visible artifact -- a reviewer must compare two column values (F-ID column
  vs. the F-NN embedded in Verb Source cell content) to verify equality. This requires reading
  cell content. C-55 extends C-52 by requiring the self-matching equality check to be
  materialized as a dedicated Match? column in the self-match audit table. The Match? column
  contains the result of the equality comparison (YES / NO) for each row; a NO entry is visible
  by column scan without reading any Verb Source cell content. The audit table with a Match?
  column converts the structural invariant from a hidden column-comparison into an explicit
  scan-visible check: mismatch rows are detectable at a glance without reading cell content. The
  three-column audit table (RQG Row F-ID | Verb Source F-NN | Match?) is itself the verification
  primitive: column A == column B is the equality check; the Match? column materializes the
  result; a scan of the Match? column for any NO entry is the complete correctness check. A
  simulation satisfying C-52 (DETECTION/CORRECTED prefix + self-matching F-ID asserted) but
  without a Match? column in the audit table satisfies C-52, fails C-55: the self-match invariant
  is declared but not materialized as a scan primitive -- a reviewer must still read Verb Source
  cell content to verify equality. V-03 (R16) is the first variation to achieve C-55: the
  Self-match audit table's 3-column schema (RQG Row F-ID | Verb Source F-NN | Match?)
  materialized the column-equality check as a dedicated column; a NO entry in the Match? column
  is scan-visible without reading Verb Source cell content. C-55 is the materialized-equality
  ceiling that C-52's declared-invariant floor cannot enforce alone.
- **Pass condition**: The RQG Verb Source self-match audit table contains a dedicated Match?
  column populated for every row with YES (F-ID matches) or NO (mismatch); the Match? column
  materializes the equality check such that violations are detectable by column scan without
  reading Verb Source cell content; a Self-match audit table SAD axis declares the Match? column
  presence as a verifiable sub-observable with >=3 independently-verifiable sub-claims. Audit
  table without Match? column = fail. Match? column present but not populated for all rows = fail.
  Self-match audit table SAD axis absent or without Match? column as a named sub-observable =
  fail. C-55 exempt if C-52 is not targeted.

---

## Criterion Relationship Map

### Floor/ceiling pairs

| Floor | Ceiling | Gap the ceiling closes |
|-------|---------|----------------------|
| C-36 | C-38 | Correctness (trace-first order) vs verifiability (three machine-readable paths) |
| C-38 | C-43 | Layer classification vs step-level DR-NN attribution (fourth structural path) |
| C-43 | C-45 | Column-presence floor vs SAD-level declaration ceiling (dedicated axis row with >=3 sub-observables) |
| C-36 + C-32 | C-39 | Co-targeting vs dual-property gate signal (single firing, both properties certified) |
| C-39 | C-41 | Aggregate rule count vs per-sub-skill attribution with labeled P1/P2 decomposition |
| C-41 | C-46 | Arithmetic attribution floor vs bidirectional cross-cite ceiling (closed verification loop) |
| C-37 | C-40 | Count floor (N rows for N criteria) vs self-reference ceiling (C-37 axis named in list) |
| C-40 | C-42 | Named-enumeration floor vs zero-scan ceiling (self-reference in opening sentence) |
| C-42 | C-44 | Single-property zero-scan floor vs dual-property zero-scan ceiling (count invariant inline) |
| C-33 | C-37 | Per-axis row floor vs count ceiling (total rows equals total targeted criteria) |
| C-31 | C-47 | Single-artifact type-verb floor vs dual-artifact cross-verification ceiling (Findings Table Verb at detection) |
| C-47 | C-50 | Cross-consistency floor vs declared-sufficiency ceiling (verbatim field-exclusion proof) |
| C-50 | C-53 | Declaration-based floor vs schema-enforced ceiling (column schema excludes forbidden fields by construction) |
| C-27 | C-48 | Binary gap floor vs commitment-aware two-tier ceiling (promise-breach vs planning-gap distinction) |
| C-48 | C-51 | Two-tier-label floor vs status-local tier ceiling (tier embedded in Status cell, no cross-reference needed) |
| C-51 | C-54 | Status-local tier floor vs axiom-first zero-lookup ceiling (standalone named axiom block enables proof from axiom text + cell value) |
| C-47 | C-49 | Cross-consistency floor vs cited-provenance ceiling (Verb Source cross-cite creates bidirectional chain) |
| C-49 | C-52 | Cited-provenance floor vs classified-self-verifying-citation ceiling (DETECTION/CORRECTED + self-matching F-ID) |
| C-52 | C-55 | Declared-invariant floor vs materialized-equality ceiling (Match? column makes violations scan-visible without reading cell content) |

### Criterion towers

**Execution order tower (C-36 -> C-38 -> C-43 -> C-45):** C-36 is the correctness floor
(execution order must be trace-first); C-38 is the verifiability ceiling (gate must be
machine-readable via three independent structural paths); C-43 is the attribution ceiling
(Execution Log must carry a DR-NN Contributed column enabling step-level rule reconstruction
independent of the gate signal and dependency map); C-45 is the SAD-declaration ceiling
(the C-43 mechanism must be promoted to a dedicated first-class SAD axis row with >=3
independently-verifiable sub-observables, enabling SAD-level verification without reading the
Execution Order Gate section at all).

**Dependency gate signal tower (C-39 -> C-41 -> C-46):** C-39 is the dual-property floor
(gate signal must certify both execution order and aggregate dependency map completeness in one
firing); C-41 is the per-sub-skill attribution ceiling (P2 must break down rule counts by
sub-skill scope with arithmetic confirmation, enabling scope-mismatch detection); C-46 is the
bidirectional closed-verification ceiling (each P2 sub-entry must cross-cite the specific
Execution Log row by name, converting arithmetic attribution into a closed integrity contract
where a discrepancy is structurally detectable from either endpoint). C-43's Contributed column
provides the underlying step-level data that C-41's P2 arithmetic is verified against; C-46
makes that link structural and bidirectional.

**Row count assertion tower (C-33 -> C-37 -> C-40 -> C-42 -> C-44):** C-33 is the per-axis
row floor (each targeted axis adds a declaration row); C-37 is the count ceiling (total rows
equals total targeted criteria); C-40 is the self-reference ceiling (Row Count Assertion
enumerates axes by name, C-37 axis appears in list); C-42 is the zero-scan ceiling
(self-referential property declared in opening sentence, verifiable without scanning the
enumerated list); C-44 is the dual-property zero-scan ceiling (opening sentence simultaneously
embeds self-reference and count invariant, making both C-37 and C-42 verifiable from a single
sentence with no further reading).

**Type-verb binding tower (C-31 -> C-47 -> C-49 -> C-52 -> C-55):** C-31 is the
single-artifact type-verb floor (RQG Verb must match the allowed vocabulary for the finding's
Type); C-47 is the dual-artifact detection ceiling (Verb also appears in the Findings Table at
detection time, enabling cross-artifact Type-Verb consistency verification from either artifact
independently); C-49 is the cited-provenance ceiling (RQG Verb Source column names the
originating Findings Table entry, creating a three-point bidirectional chain where a discrepancy
is structurally detectable from either endpoint without manual cross-comparison); C-52 is the
classified-self-verifying-citation ceiling (Verb Source carries DETECTION/CORRECTED
classification plus a self-matching F-ID constraint, converting the back-cite into a structural
invariant verifiable by column-value equality without tracing to the Findings Table); C-55 is
the materialized-equality ceiling (a dedicated Match? column in the self-match audit table
materializes the F-ID equality check as a scan-visible result column, making violations
detectable by column scan without reading Verb Source cell content).

**Column-scan sufficiency tower (C-47 -> C-50 -> C-53):** C-47 is the dual-artifact
cross-consistency floor (Verb present in both FT and RQG); C-50 is the declared-sufficiency
ceiling (a verbatim field-exclusion proof declares that C-47 compliance required no narrative
reading, making the column-scan claim itself the falsifiable assertion); C-53 is the
schema-enforced ceiling (the column schema of the compliance verification table contains no
narrative field, making narrative reading structurally impossible by construction rather than
merely asserted absent by declaration).

**Entity coverage gap tower (C-27 -> C-48 -> C-51 -> C-54):** C-27 is the binary gap floor
(ECM must log all SKIPPED entities as execution gaps); C-48 is the commitment-aware ceiling
(SKIPPED entries must carry a tier label distinguishing promise-breach gaps, where an Examining
Sub-Skill was declared in the TEM but not executed, from planning gaps, where no examining
commitment was ever declared); C-51 is the status-local tier ceiling (tier label embedded
directly in the Status cell value, enabling tier verification by single-column scan without
cross-referencing the Examining Sub-Skill column); C-54 is the axiom-first zero-lookup ceiling
(tier ordering derivable from a standalone named axiom block + single ECM Status cell label
alone, with no cross-column lookup -- the axiom block pre-states the ordering claim as a named
proposition decoupled from all table structure).

### Round-by-round first-to-satisfy

| Criterion | First variation to satisfy | Round |
|-----------|--------------------------|-------|
| C-38 | V-01 | R10 |
| C-39 | V-05 | R10 |
| C-40 | V-05 | R10 |
| C-41 | V-02 | R11 |
| C-42 | V-03 | R11 |
| C-43 | V-01 | R11 |
| C-44 | V-05 | R12 |
| C-45 | V-05 | R12 |
| C-46 | V-05 | R12 |
| C-47 | V-02 | R14 |
| C-48 | V-03 | R14 |
| C-49 | V-04 | R14 |
| C-50 | V-01 | R15 |
| C-51 | V-02 | R15 |
| C-52 | V-03 | R15 |
| C-53 | V-01 | R16 |
| C-54 | V-02 | R16 |
| C-55 | V-03 | R16 |

---

## Scoring

**Essential criteria (C-01 through C-05)**: 60 points total. Each essential criterion carries
equal weight within its group. Failure of any essential criterion disqualifies the simulation
from aspirational scoring.

**Aspirational criteria (C-26 through C-55)**: 47 criteria in pool, capped at 10 points total
regardless of how many aspirational criteria pass. Each aspirational criterion passed adds equal
fractional weight up to the cap. Exempt criteria do not count toward numerator or denominator.

**Maximum score: 100 points.**

---

## R16 Variation Outcomes (reference)

*Scores computed under v15 rubric (47-criterion aspirational pool).*
*All five R16 variations are supersets of R15 V-05 (the first variation to pass all 44 v14
criteria). All five inherit 44/44 v14 PASS. The v15 question is which of C-53, C-54, C-55
each variation satisfies.*

- **V-01 (~99.6):** Table-Schema-as-Proof Axis. C-53 PASS (Column-scan enumeration table's
  3-column schema (F-ID | FT Verb | RQG Verb) contains no narrative column; schema design IS the
  scan-sufficiency proof by construction). C-54 FAIL (no standalone SEVERITY AXIOM block before
  ECM). C-55 FAIL (no Match? column in Self-match audit table). 45 passing / 47 eligible = 95.74%.
  Score: 90 + 9.57 = **~99.6**.

- **V-02 (~99.6):** Axiom-First Derivation Axis. C-54 PASS (SEVERITY AXIOM block written as
  standalone named block immediately before ECM; Tier severity axiom SAD axis declared; checklist
  sub-claim cites axiom text + Status cell label only; required declaration "gap ordering derived
  from SEVERITY AXIOM; no sub-skill column or finding content consulted"). C-53 FAIL (no declared
  column schema for Column-scan enumeration table). C-55 FAIL (no Match? column).
  45 passing / 47 eligible = 95.74%.
  Score: 90 + 9.57 = **~99.6**.

- **V-03 (~99.6):** Match? Column Materialization Axis. C-55 PASS (Self-match audit table carries
  3-column schema (RQG Row F-ID | Verb Source F-NN | Match?); Match? column populated YES/NO per
  row; violations scan-visible without reading Verb Source cell content; SAD axis declares Match?
  column as verifiable sub-observable with >=3 sub-claims). C-53 FAIL (no declared column schema
  for Column-scan enumeration table). C-54 FAIL (no standalone SEVERITY AXIOM block).
  45 passing / 47 eligible = 95.74%.
  Score: 90 + 9.57 = **~99.6**.

- **V-04 (~99.8):** Two-surface integration (C-53 + C-55). C-53 PASS (Column-scan enumeration
  table schema declared; no narrative columns). C-55 PASS (Match? column present and populated).
  C-54 FAIL (no standalone SEVERITY AXIOM block). 46 passing / 47 eligible = 97.87%.
  Score: 90 + 9.79 = **~99.8**.

- **V-05 (100.0):** All three R16 ceiling mechanisms on disjoint surfaces. C-53 PASS (Column-scan
  enumeration table schema on checklist axis 21 -- no narrative column). C-54 PASS (SEVERITY AXIOM
  block on ECM axis 22 -- standalone named block, axiom-text + cell-value proof). C-55 PASS
  (Self-match audit table Match? column on Verb-source axis 23 -- scan-visible equality check).
  All three surfaces independently falsifiable with no cross-surface interference.
  47 passing / 47 eligible = 100%.
  Score: 90 + 10.0 = **100.0**.

**R16 ceiling targets**: C-53 (schema-enforced scan-sufficiency) + C-54 (axiom-first zero-lookup
proof) + C-55 (materialized-equality scan primitive) form three independent towers on disjoint
document surfaces. A full-integration variation satisfying all three alongside the 44 v14 base
criteria achieves 47/47 = 100.0.

---
