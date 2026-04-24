v13 written to `simulations/quest/rubrics/campaign-simulate-rubric-v13-2026-03-17.md`.

---

**Three new criteria extracted from R14:**

**C-47 — Findings Table Carries Verb Column at Detection Time for Cross-Artifact Type-Verb Binding Verification** *(correctness, C-31 activation)*
V-02 added a Verb column to the Findings Table at detection time, creating a second independently-falsifiable location for the Type-Verb binding check. C-31's ceiling is single-artifact (RQG Verb only); C-47 requires the Verb at detection so cross-artifact consistency is verifiable by column scan without narrative reasoning. Type-verb binding tower now three levels deep: C-31 → C-47 → C-49.

**C-48 — Entity Coverage Matrix SKIPPED Entries Distinguish Commitment-Present from None-Declared** *(correctness, C-27 activation)*
V-03 added an Examining Sub-Skill column to the TEM before execution, converting it from a passive manifest into a pre-execution commitment register. This creates a two-tier SKIPPED signal: promise-breach gap (commitment declared, not executed) vs. planning gap (no commitment ever declared). C-27's ceiling treats all SKIPPED entries identically; C-48 requires tier labels. Entity coverage gap tower now two levels deep: C-27 → C-48.

**C-49 — RQG Verb Source Column Creates Three-Point Cross-Artifact Type-Verb-Source Chain** *(correctness, C-47 activation)*
V-04 added a Verb Source column to the RQG naming the originating Findings Table row, extending C-47's two-point consistency check into a three-point bidirectional chain: Findings Table Verb → RQG Verb → Verb Source back-cite. A discrepancy is structurally detectable from either endpoint. C-47's ceiling is cross-consistency (unidirectional); C-49 requires the structural citation. Type-verb binding tower: C-31 → C-47 → C-49.

**Aspirational pool: 38 → 41. Max score: 100 unchanged.**
per-row structured table decomposing each
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
| C-27 | C-48 | Binary gap floor vs commitment-aware two-tier ceiling (promise-breach vs planning-gap distinction) |
| C-47 | C-49 | Cross-consistency floor vs cited-provenance ceiling (Verb Source cross-cite creates bidirectional chain) |

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

**Type-verb binding tower (C-31 -> C-47 -> C-49):** C-31 is the single-artifact type-verb
floor (RQG Verb must match the allowed vocabulary for the finding's Type); C-47 is the dual-
artifact detection ceiling (Verb also appears in the Findings Table at detection time, enabling
cross-artifact Type-Verb consistency verification from either artifact independently); C-49 is
the cited-provenance ceiling (RQG Verb Source column names the originating Findings Table entry,
creating a three-point bidirectional chain where a discrepancy is structurally detectable from
either endpoint without manual cross-comparison).

**Entity coverage gap tower (C-27 -> C-48):** C-27 is the binary gap floor (ECM must log all
SKIPPED entities as execution gaps); C-48 is the commitment-aware ceiling (SKIPPED entries
must carry a tier label distinguishing promise-breach gaps, where an Examining Sub-Skill was
declared in the TEM but not executed, from planning gaps, where no examining commitment was
ever declared).

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

---

## Scoring

**Essential criteria (C-01 through C-25)**: 60 points total. Each essential criterion carries
equal weight within its group. Failure of any essential criterion disqualifies the simulation
from aspirational scoring.

**Aspirational criteria (C-26 through C-49)**: 41 criteria in pool, capped at 10 points total
regardless of how many aspirational criteria pass. Each aspirational criterion passed adds equal
fractional weight up to the cap. Exempt criteria do not count toward numerator or denominator.

**Maximum score: 100 points.**

---

## R14 Variation Outcomes (reference)

*Scores computed under v13 rubric (41-criterion aspirational pool).*

- **V-01 (~99.0):** 12-axis SAD base. C-43 PASS (DR-NN Contributed column; union-of-rows equality
  check; zero-contribution template); C-44 PASS (opening sentence embeds count + self-reference);
  C-45 PASS (dedicated execution-log attribution axis, 3 sub-observables); C-46 PASS (P2
  sub-entries cross-cite Execution Log row by name). C-30 FAIL; C-35 EXEMPT (C-30 absent).
  C-47/C-48/C-49 FAIL (no Findings Table Verb column, no two-tier SKIPPED, no Verb Source).
  36 passing / 40 eligible = 90.0%. Score: 90 + 9.0 = **99.0**.

- **V-02 (~99.25):** Same 12-axis base + Verb column added to Findings Table at detection time.
  All V-01 criteria PASS. C-47 PASS (Findings Table Verb column enables cross-artifact C-31
  verification). C-30 FAIL; C-35 EXEMPT. C-48 FAIL (no two-tier SKIPPED); C-49 FAIL (no Verb
  Source column in RQG). 37 passing / 40 eligible = 92.5%. Score: 90 + 9.25 = **99.25**.

- **V-03 (~99.25):** Same 12-axis base + Examining Sub-Skill column in TEM (entity-coverage
  commitment axis). All V-01 criteria PASS. C-48 PASS (two-tier SKIPPED signal: commitment-
  present vs none-declared). C-30 FAIL; C-35 EXEMPT. C-47 FAIL (no Findings Table Verb column);
  C-49 FAIL (no Verb Source column). 37 passing / 40 eligible = 92.5%. Score: 90 + 9.25 = **99.25**.

- **V-04 (~99.5):** V-01 + V-02 combined; six-column RQG (Verb / Target / Location / Conformance /
  Blast Status / Verb Source). All V-01 criteria PASS. C-47 PASS (Findings Table Verb column from
  V-02); C-49 PASS (Verb Source column in RQG creates three-point bidirectional chain). C-30 FAIL;
  C-35 EXEMPT. C-48 FAIL (no Examining Sub-Skill in TEM). 38 passing / 40 eligible = 95.0%.
  Score: 90 + 9.5 = **99.5**.

- **V-05 (100.0):** Full integration -- 18-axis SAD, R13 V-05 base extended with all three new
  mechanisms. All C-26 through C-46 PASS (C-35 PASS; C-30 PASS via confidence-stratified action
  list preserved from R13 base). C-47 PASS (Findings Table Verb column); C-48 PASS (two-tier
  SKIPPED signal); C-49 PASS (Verb Source column closes bidirectional chain). 41 passing / 41
  eligible = 100%. Score: 90 + 10 = **100**.

**R14 ranking**: V-05 > V-04 > V-02 = V-03 > V-01

**Confirmed next extraction targets**: C-30 fails for V-01 through V-04 in R14. Confidence-
stratified action list with two named tracks remains the primary mechanism separating V-05 from
the field. C-35 co-activates with C-30 and is exempt for all variations that fail C-30.

---

*Rubric version: v13. Aspirational pool: 41 criteria (C-26 through C-49). Max score: 100. Date: 2026-03-17.*
