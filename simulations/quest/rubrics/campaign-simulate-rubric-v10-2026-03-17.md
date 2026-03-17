Three new aspirational criteria extracted from R10 and written to `simulations/quest/rubrics/campaign-simulate-rubric-v10-2026-03-17.md`:

---

**C-38 — Execution Order Gate Achieves Machine-Readable Three-Path Structural Verification**
*Category: format*

V-03 (R10) is the diagnostic control: correct trace-first order satisfies C-36's pass condition, but prose narrative does not produce a machine-readable completion record. C-38 requires all three structural paths that V-01/V-04/V-05 used: (1) Layer Completion Record table with Status column, (2) explicit gate signal statement naming all three Platform sub-skills, (3) Execution Log with Layer column. Each path is independently verifiable by column scan; prose is not. V-03 satisfies C-36, fails C-38. Relationship: **C-38 is the verifiability ceiling that C-36's correctness floor cannot enforce alone.**

---

**C-39 — Execution Order Gate Signal Certifies Both Execution Order and Dependency Map Completeness**
*Category: correctness / co-targeting condition: C-32 + C-36*

V-01 passed C-38 (three-path gate) but its gate signal certified execution order only. V-05's gate signal fired with dual-property certification: "all three Platform sub-skills complete AND DR-01 through DR-N are fully declared." This closes a race C-36 alone cannot detect — a trace sub-skill can complete in the right order while failing to emit all its DR-NN rules. The rule count must appear in the gate signal itself, not deferred to the Coverage Gate. Exempt when C-32 is not co-targeted.

---

**C-40 — Row Count Assertion Is Self-Referential When C-37 Is Targeted**
*Category: format / activation condition: C-37 targeted*

V-04 achieved C-37 (correct count, "7==7") without enumerating axes by name — the self-reference was implicit. V-05 listed all N targeted axes by name in the Row Count Assertion block, with the declaration-completeness-proof / C-37 axis itself appearing in that list. The completeness proof names itself as one of the items being proved complete. A "N==N" assertion without named axis enumeration satisfies C-37, fails C-40. Relationship: **C-37 is the count floor; C-40 is the self-reference ceiling.**

---

**Aspirational pool: 29 → 32. Max score: 100 unchanged.**
rose path cannot.
C-38 requires all three paths. A simulation satisfying C-36 via prose narrative alone satisfies
C-36 but fails C-38. V-03 is the controlled experiment that establishes the gap.

**C-39 -- Execution Order Gate Signal Certifies Both Execution Order and Dependency Map Completeness**
(requires C-32 + C-36 co-targeting; new dual-property certification)

V-05 coupled C-32 and C-36 in a single gate signal: the signal fired after step 3 naming all
three Platform sub-skills complete AND confirming "Dependency rules DR-01 through DR-[N] are
fully declared." V-01 also satisfied C-36 via gate table and C-38 via three-path structure, but
its gate signal certified only execution order — not dependency map completeness. The scorecard
called V-05's mechanism "dual-property certification coupling C-36 and C-32." The dual
certification closes a gap that single-property certification cannot detect: a trace sub-skill
may complete in the correct order but fail to declare all its dependency rules, leaving the map
incomplete even after the gate fires. A gate signal certifying only execution order satisfies
C-36 and C-38 but fails C-39. C-39 applies only when both C-32 and C-36 are co-targeted;
simulations targeting C-36 alone are exempt.

**C-40 -- Row Count Assertion Is Self-Referential When C-37 Is Targeted**
(requires C-37 targeting; completeness proof must count itself)

V-04 achieved 1:1 axis-to-criterion correspondence by construction: both the execution-order
axis row (for C-36) and the declaration-completeness-proof axis row (for C-37) were present, and
the Row Count Assertion stated "7 rows, 7 targeted axes, 7==7." V-05 went further: the
declaration-completeness-proof / C-37 axis row was explicitly listed by name among the N targeted
axes in the Row Count Assertion itself, making the completeness proof self-referential — the
declaration declares that it is contract-complete, and the proof names itself as one of the items
being proved complete. V-04 satisfies C-37 (the count is correct) but not C-40 (the Row Count
Assertion does not enumerate the axes by name; the self-reference is implicit). C-40 requires:
(1) the Row Count Assertion enumerates the targeted axes by name in the assertion block, and
(2) the declaration-completeness-proof / C-37 axis appears in that named list. A Row Count
Assertion that states "N rows, N criteria, N==N" without naming the axes fails C-40 because the
self-reference cannot be verified by name inspection. C-40 applies only when C-37 is targeted.

---

Aspirational pool grows 29 -> 32. The `*(C-04 through C-25 -- unchanged from v6)*` placeholder
preserved.

**Cross-round criterion relationships:**

- **C-36 / C-38** -- C-36 is the correctness floor (execution order must be trace-first); C-38
  is the verifiability ceiling (gate must be machine-readable via three independent structural
  paths). V-03 satisfies C-36 without C-38; V-01/V-04/V-05 satisfy both.

- **C-36 + C-32 / C-39** -- C-36 certifies execution order; C-32 certifies DR-NN traceability;
  C-39 requires the gate signal to certify both properties simultaneously. C-39 activates only
  when both C-32 and C-36 are targeted. V-05 is the first variation to satisfy C-39.

- **C-37 / C-40** -- C-37 is the completeness floor (N rows for N criteria); C-40 is the
  self-reference ceiling (the Row Count Assertion explicitly names the C-37 axis among the axes
  it counts). V-04 satisfies C-37 without C-40; V-05 satisfies both.

- **C-33 -> C-37 -> C-40** -- C-33 is the per-axis floor (each targeted axis adds a row); C-37
  is the count ceiling (total rows equals total targeted criteria); C-40 is the self-reference
  requirement (the completeness-proof row must name itself among the counted items). The three
  criteria form a tower: C-33 passes when the declaration self-extends; C-37 passes only when
  the count matches exactly; C-40 passes only when the assertion names itself as one of the
  counted items.

**R10 variation outcomes:**

- V-01 (~92): C-36 PASS via three-path gate table (satisfies C-38); C-37 implicit PASS (fails
  C-40 -- no named axis list); C-39 not targeted (gate signal certifies execution order only).
- V-02 (~90): C-37 PASS via explicit Row Count Assertion (fails C-40 -- no named axis list);
  C-36 FAIL (flow-first order); C-38 and C-39 also fail by C-36 failure. Demonstrates that
  formal assertions do not substitute for correct mechanics.
- V-03 (~91): C-36 PASS via prose (fails C-38 -- no gate table; no three-path structure); C-37
  implicit PASS (fails C-40 -- no named axis list). The controlled experiment establishing the
  prose/gate-table gap for C-36.
- V-04 (~93): First to satisfy both C-36 (gate table) and C-38 (three-path structure) and C-37
  (explicit Row Count Assertion) simultaneously. Fails C-39 (gate signal is single-property
  only) and C-40 (Row Count Assertion does not enumerate axes by name).
- V-05 (~97): Satisfies C-38 (three-path gate table), C-39 (dual-property gate signal coupling
  C-36 + C-32), and C-40 (self-referential Row Count Assertion naming C-37 axis). First
  variation to satisfy all three R10 criteria.

**Aspirational pool: 29 -> 32 criteria, capped at 10 pts. Max score 100 unchanged.**

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

*(C-04 through C-25 -- unchanged from v6)*

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

## Scoring

**Essential criteria (C-01 through C-25)**: 60 points total. Each essential criterion carries
equal weight within its group. Failure of any essential criterion disqualifies the simulation
from aspirational scoring.

**Aspirational criteria (C-26 through C-40)**: 32 criteria in pool, capped at 10 points total
regardless of how many aspirational criteria pass. Each aspirational criterion passed adds equal
fractional weight up to the cap.

**Maximum score: 100 points.**

---

*Rubric version: v10. Aspirational pool: 32 criteria. Max score: 100. Date: 2026-03-17.*
