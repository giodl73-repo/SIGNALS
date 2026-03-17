`flow-lifecycle-rubric-v12-2026-03-14.md` written.

---

**What changed from v11 → v12:**

2 new aspirational criteria extracted from R11 excellence signals. Formula bumped from `/31` to `/33`.

| ID | Criterion | Category | Root | Key dependency |
|----|-----------|----------|------|----------------|
| C-40 | Exception Block Role-Sequence Cross-Reference | depth | R11 V-04 (min); V-05 confirm | C-40→C-38+C-13 |
| C-41 | Phase Entry Contract Prior-Phase Sequential Linkage | format | R11 V-05 (min) | C-41→C-36 |

---

**C-40 design rationale.**
C-38 gave us Role→Phase traceability via the ROLE SEQUENCE SCHEDULE. C-40 opens the fourth orthogonal direction: Exception→Role. Each EX block carries a named R-ID sub-field (e.g. `Role Ref: R-02`) that string-matches the schedule entry for the enclosing phase. The Role Registry Gate additionally gates each declared R-ID on presence in at least one EX block, closing the chain bidirectionally (Role→Exception in the gate; Exception→Role in the block). The structural property is identical to the others — string comparison, no reader inference. "Dark" roles — registry-declared but with no observable exception-phase trace — become detectable as gate violations.

**C-41 design rationale.**
C-37 filled the exit gate's Phase→B-NN slot. C-41 fills the entry contract's Phase→Phase slot: a named `Prior phase:` sub-field in every PHASE ENTRY CONTRACT declares which phase this follows by literal identifier. PHASE 1 carries NONE/INIT. Together C-37+C-41 complete the gate-to-gate linkage: exit gate declares the blocking bottleneck forward; entry contract declares the predecessor phase backward. Out-of-order phase rendering is now detectable by identifier mismatch, independent of document position.

**Updated dependency chain:**
```
... (C-09 through C-39 unchanged from v11) ...
C-40->C-38+C-13; C-41->C-36
```

**Formula:** `aspirational_pass / 33 * 10` — golden threshold unchanged.
ut reading phase content. C-41 is to C-36 what C-37 is to C-36 on the exit side:
  a named sub-field that converts an implicit gate into a string-comparable traceability
  artifact.

**Full dependency chain (v12):**
- C-18->C-15; C-19->C-16; C-20->C-14+C-16; C-21->C-13+C-15+C-17
- C-22->C-19; C-23->C-20
- C-24->C-22; C-25->C-23; C-26->C-22
- C-27->C-26
- C-28->C-27; C-29->C-27; C-30->C-24+C-27
- C-31->C-29; C-32->C-30
- C-33->C-28+C-24
- C-34->C-04; C-35->C-34; C-36->C-04
- C-37->C-36+C-04; C-38->C-12; C-39->C-34+C-38
- **C-40->C-38+C-13; C-41->C-36**

---

# flow-lifecycle -- Rubric v12

**5 Essential (60 pts)**

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | State Transition Coverage -- every state has named entry condition + at least one labeled exit | correctness |
| C-02 | Exception Flow Identification -- 3+ process-specific exception flows to terminal | coverage |
| C-03 | Role Assignment Accuracy -- domain-specific roles at every decision point and gate | correctness |
| C-04 | Bottleneck and Gap Identification -- 2+ bottlenecks with cause + impact, 1+ gaps with rationale | depth |
| C-05 | Terminal State Completeness -- all success and failure/cancel terminals declared; every branch reaches one | correctness |

**3 Recommended (30 pts)**

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Parallel Path Modeling -- at least one fork/join with labeled join condition | depth |
| C-07 | Edge Case Enumeration -- 3+ edge cases distinct from C-02, each with trigger + why problematic + correct response | coverage |
| C-08 | Decision Point Explicitness -- every branch has labeled condition + owner role + fallback | format |

**33 Aspirational (10 pts)**

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | Cross-Process Interaction Modeling -- at least one inter-process handoff contract | depth |
| C-10 | SLA and Timing Analysis -- 3+ nodes annotated with SLA vs. typical, at-risk flags | depth |
| C-11 | Decision Supplement Block Structure -- per-decision structured block with Fallback field | format |
| C-12 | Role Registry Gate -- pre-declared domain registry with anti-generic validation before tracing | correctness |
| C-13 | Phase-Scoped Exception Traces -- each exception trace anchored to its originating phase | coverage |
| C-14 | SLA-to-Bottleneck Evidence Chain -- SLA at-risk entries cross-referenced to bottleneck IDs | depth |
| C-15 | Exception-First Structural Position -- exception sections structurally precede state tables per phase | format |
| C-16 | Bidirectional SLA-Bottleneck Cross-Reference -- B-NN entries cite affected SLA nodes; chain runs both directions | depth |
| C-17 | Constructed-Answer Format for Exception Sections -- exception and edge-case sections use labeled sub-field answers, not table cells | format |
| C-18 | Ordinal-Label Structural Enforcement -- SECTION A/B (or equivalent ordinal) labels encode exception-first ordering as a named constraint | format |
| C-19 | Backward-Chain Evidence Injection -- B-NN blocks contain a named Evidence field listing specific AT-RISK SLA rows that cite this B-ID | depth |
| C-20 | Chain Status Gate -- explicit CHAIN STATUS: CLOSED/OPEN declaration makes bidirectional verification a discrete output element | depth |
| C-21 | Unified Exception-Block Architecture -- SECTION A constructed-answer blocks per phase satisfy C-13, C-15, and C-17 through a single structural decision | format |
| C-22 | Evidence Field Format Contract -- the Evidence sub-field hint provides a concrete format example in `[State name -- S-ID]: AT-RISK, causal source: B-[ID]` form plus an explicit preamble fail condition for general references | depth |
| C-23 | Chain Status Section Isolation -- CHAIN STATUS is declared as the first element of a dedicated top-level section, not embedded in SLA ANALYSIS; anti-embedding instruction present | depth |
| C-24 | Evidence Field Format Dual Redundancy -- the concrete named domain example and fail condition appear in BOTH the global preamble AND each B-NN per-block hint | depth |
| C-25 | Anti-Embedding Dual Enforcement -- the anti-embedding instruction for CHAIN STATUS appears in BOTH the global preamble AND as the opening constraint of the dedicated CHAIN STATUS section | format |
| C-26 | Evidence Field Axis Separation -- the Evidence field instruction presents structure specification and contract specification as explicitly labeled, visually distinct components | format |
| C-27 | Evidence Field Axis Dual-Location Separation -- the `Required format:` and `Fail condition:` labeled axes appear in BOTH the global preamble AND each B-NN per-block hint | format |
| C-28 | Evidence Format Pattern B-ID Instantiation -- the `Required format:` axis in each B-NN per-block hint uses the specific B-ID for that block, not a generic `B-[ID]` placeholder | depth |
| C-29 | B-NN Scaffold Completeness Prerequisite Declaration -- the template contains an explicit instruction that ALL declared B-NN blocks carry the Evidence field before per-block dual-location criteria apply | correctness |
| C-30 | Dual-Location Requirements Consolidated Declaration -- a named block enumerates both dual-location properties (concrete example and labeled axes) at one declaration point, not scattered across individual B-NN hints | format |
| C-31 | Scaffold Gate Forward-Reference Structural Position -- the scaffold completeness gate appears before the first B-NN block in document order and uses forward-reference language ("declared below" or equivalent) making its scope positionally verifiable | format |
| C-32 | Dual-Location Consolidated Block Canonical Axis Citation -- the consolidated dual-location declaration names the `Required format:` and `Fail condition:` axes by their canonical labels, not by description or paraphrase | format |
| C-33 | Preamble Concrete Example B-ID Alignment -- the preamble concrete example (per C-24) names the same B-ID as the first declared B-NN block, aligning the preamble anchor with the per-block instantiation chain | depth |
| C-34 | Incumbent Baseline IM-ID Cross-Section Traceability -- INCUMBENT BASELINE table assigns IM-IDs to named failure modes; each B-NN Cause field cites at least one IM-ID by literal identifier, establishing the Baseline->B-NN traceability chain | depth |
| C-35 | Cost-of-No-Action Baseline Quantification -- the INCUMBENT BASELINE section declares at least one quantified metric (named measure with value or rate) before the first phase block in document order | depth |
| C-36 | Phase-Exit Gate Named Sub-Field Architecture -- each phase section contains both a PHASE ENTRY CONTRACT block and a PHASE EXIT GATE block with explicitly named structural sub-fields | format |
| C-37 | Phase Exit Gate B-ID Forward Reference -- the PHASE EXIT GATE block carries a `Blocked bottleneck:` sub-field citing the B-ID (or NONE) that can delay phase exit, creating a Phase->B-NN traceability direction verifiable by string comparison | depth |
| C-38 | Role Sequence Schedule Phase Ownership Declaration -- a named ROLE SEQUENCE SCHEDULE block declared after the Role Registry Gate and before PHASE 1 maps each R-ID to owned phases with activation triggers, handoff triggers, and parallel windows | format |
| C-39 | B-NN Cause Field Dual Citation -- each B-NN Cause field cites both an IM-ID from INCUMBENT BASELINE and a blocking R-ID from the ROLE SEQUENCE SCHEDULE, establishing the Role->B-NN traceability direction in addition to the Baseline->B-NN direction | depth |
| C-40 | Exception Block Role-Sequence Cross-Reference -- each EX block carries a named R-ID sub-field matching an entry in the ROLE SEQUENCE SCHEDULE; the registry gate validates that every declared R-ID appears in at least one EX block, creating the Role<->Exception traceability chain | depth |
| C-41 | Phase Entry Contract Prior-Phase Sequential Linkage -- each PHASE ENTRY CONTRACT block carries a named `Prior phase:` sub-field identifying the preceding phase by literal phase identifier, creating Phase->Phase sequential traceability verifiable by string comparison | format |

**Golden threshold**: all 5 essential pass + composite >= 80.

---

## Essential Criteria (60 pts total)

### C-01 - State Transition Coverage
- **Weight**: essential
- **Category**: correctness
- **Text**: Every state in the lifecycle has an explicitly labeled entry condition and at
  least one labeled exit. No state is left dangling with an implicit or undeclared
  transition. The coverage spans the full process from initial trigger to terminal state.
- **Pass condition**: Each state has a named entry condition and one or more labeled exits.
  Exits must reference the destination state or be marked TERMINAL. Fail if any state
  lacks an entry condition or has an unlabeled exit.

### C-02 - Exception Flow Identification
- **Weight**: essential
- **Category**: coverage
- **Text**: The output identifies at least three distinct exception flows: named failure
  modes that deviate from the happy path. Each exception trace follows the path from
  trigger to resolution or terminal. Each must be specific to the process being
  simulated, not generic boilerplate.
- **Pass condition**: Three or more exception flows, each with: trigger condition, trace
  of states traversed, handling role, and resolution or terminal. Each must be specific
  to the process being simulated, not generic boilerplate.

### C-03 - Role Assignment Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Domain expert roles are auto-selected from the process context and assigned to
  specific decision points or approval gates. Role set matches the declared process type.
- **Pass condition**: Each approval gate or decision point is owned by a named role.
  Role set matches the process type: L2O -> Sales/Finance/Legal; P2P -> Procurement/Finance/
  Receiving; period close -> Finance/Controller/Auditor; case -> Support/Ops/Legal.
  Fail if roles are generic (Approver) with no domain specificity.

### C-04 - Bottleneck and Gap Identification
- **Weight**: essential
- **Category**: depth
- **Text**: The output explicitly calls out at least two bottlenecks (states or transitions
  where delays commonly accumulate) and at least one gap (a step missing from the flow that
  exists in real-world practice).
- **Pass condition**: Each bottleneck is labeled, its cause explained, and its downstream
  impact noted. Each gap is labeled MISSING: with a rationale for why it belongs. Fail if
  findings are stated without causal explanation.

### C-05 - Terminal State Completeness
- **Weight**: essential
- **Category**: correctness
- **Text**: All terminal states are identified -- both successful completion and
  failure/cancellation states. Every trace path reaches a terminal state; no path ends
  in a non-terminal state without a continuation or loop marker.
- **Pass condition**: At least two terminal states (one success, one failure/cancel). Every
  branch reaches a declared terminal state. Fail if any branch ends mid-flow without a
  terminal label or explicit continues-via pointer.

---

## Recommended Criteria (30 pts total)

### C-06 - Parallel Path Modeling
- **Weight**: recommended
- **Category**: depth
- **Text**: Where the real process has concurrent work streams (e.g., credit check parallel
  to inventory reservation in L2O; goods receipt concurrent with invoice processing in P2P),
  the output models these explicitly with join/synchronization points.
- **Pass condition**: At least one parallel path is present with both branches and a labeled
  synchronization point. Join condition must be specified (AND-join vs OR-join). Fail if
  parallelism is described only in prose without structural representation.

### C-07 - Edge Case Enumeration
- **Weight**: recommended
- **Category**: coverage
- **Text**: The output surfaces at least three edge cases that are never handled or handled
  inconsistently -- scenarios that exist in practice but fall outside the documented happy
  path and exception flows.
- **Pass condition**: Three distinct edge cases, each non-overlapping with C-02 exception
  flows. Each must include: triggering condition, why it is problematic, and what a correct
  response would look like. Fail if edge cases duplicate named exception flows.

### C-08 - Decision Point Explicitness
- **Weight**: recommended
- **Category**: format
- **Text**: Every decision point (branch) in the flow is accompanied by: the rule or
  condition being evaluated, the agent/role that evaluates it, and all possible outcomes.
  No implicit branching.
- **Pass condition**: Each decision point has a labeled condition, an owner role, and
  exhaustive outcome branches including a fallback branch if applicable. Fail if any branch
  originates from an unlabeled or condition-free node.

---

## Aspirational Criteria (10 pts total)

### C-09 - Cross-Process Interaction Modeling
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output identifies at least one point where the simulated lifecycle touches
  an adjacent process and traces the inter-process signal: what data crosses, who sends it,
  what the receiving process expects.
- **Pass condition**: At least one cross-process interaction is named, with sending state,
  receiving process, data payload, and expected acknowledgment described. Fail if adjacent
  processes are mentioned without any interface definition.

### C-10 - SLA and Timing Analysis
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output attaches realistic timing expectations or SLA targets to at least
  three transitions or states, and flags any transition whose typical duration exceeds its
  SLA target as a risk.
- **Pass condition**: Three or more states/transitions have timing annotations with
  explicit at-risk callouts where typical exceeds SLA. Fail if timing is absent entirely
  or applied to fewer than three nodes.

### C-11 - Decision Supplement Block Structure
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 1 signal: DECISION type column annotation and exits format are
  structurally insufficient for exhaustive outcome coverage. A dedicated per-decision
  supplement block with explicitly labeled fields -- Condition, Owner, Branch YES, Branch
  NO, Fallback -- is required to guarantee that no decision point omits a fallback path.
  Inline annotation leaves this gap open.
- **Pass condition**: Each decision point in the output has a dedicated structured block
  (not just a column annotation or inline note) with: Condition, Owner, at least two
  outcome branches, and an explicit Fallback field. Fail if decision coverage is provided
  only through type-column annotation without a supplement block per decision point.

### C-12 - Role Registry Gate
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Round 1 signal: A pre-declared role registry with explicit anti-generic
  validation, completed before any state is traced, prevents C-03 generic-name failure
  more reliably than role-list hints or column suggestions. The registry assigns R-IDs to
  domain-specific roles and is referenced at every decision point and approval gate.
- **Pass condition**: A role registry with at least one entry per process-type domain
  (R-NN IDs, role name, function, anti-generic check) is declared before the first state
  is traced. Every decision point and approval gate references an R-ID, not a free-text
  role name. Fail if role assignment is done inline without a pre-declared registry, or if
  any role name is generic (Approver, Owner, Actor) without domain qualification.

### C-13 - Phase-Scoped Exception Traces
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Round 1 signal: Exception traces anchored to the phase where the failure
  originates improve C-02 specificity by scoping failure-mode generation to phase context
  without additional instructions. A flat exception table produces generic cross-flow
  traces; per-phase exception sections produce phase-specific, operationally accurate
  failure modes.
- **Pass condition**: Each exception trace is labeled with the phase or state where it
  originates. Exception traces are grouped or annotated by phase, not presented as a flat
  undifferentiated list. Fail if exception flows are listed without phase or state
  anchoring, making it impossible to determine where in the lifecycle each failure occurs.

### C-14 - SLA-to-Bottleneck Evidence Chain
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 1 signal: SLA at-risk annotations gain diagnostic precision when
  cross-referenced to identified bottleneck IDs (B-NN). This creates a closed evidence
  chain: a timing risk is not a free-floating observation but is causally linked to a
  named bottleneck with an explained cause and downstream impact. Outputs without this
  cross-reference provide SLA risk flags that are disconnected from the bottleneck
  analysis.
- **Pass condition**: At least two SLA at-risk entries reference a bottleneck ID (B-NN)
  from the C-04 bottleneck analysis. The cross-reference must be explicit (e.g., "see
  B-02" or a cross-ref column). Fail if SLA at-risk flags are present but no bottleneck
  cross-reference exists, leaving timing risk causally unlinked.

### C-15 - Exception-First Structural Position
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 2 signal: C-13 column annotation (Phase/State Origin column or labeled
  sub-field) is the weakest structural form of phase-scoped exception tracing. V-01 R2
  note identifies it as lowest structural reliability -- a blank column is visible but
  the model generates exception content after seeing the state table, not before. V-03
  achieves C-13 by placing a dedicated exception section structurally before the state
  table in each phase section, forcing the model to enumerate phase-specific failure modes
  from phase context alone before any state-level detail is available. This structural
  ordering improves exception specificity by construction, without instruction overhead.
- **Pass condition**: In each phase section (or equivalent structural unit), the exception
  traces for that phase appear as a dedicated section before the state transition table.
  The exception section must be a first-class output element (not a column, not a
  sub-field, not an inline annotation) and must precede the state detail for that phase.
  Fail if exceptions are listed in a flat post-hoc table, as column annotations, or in
  sub-fields appended after state tables.

### C-16 - Bidirectional SLA-Bottleneck Cross-Reference
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 2 signal: All R2 variations achieve C-14 one-directionally only: SLA
  at-risk entries cite the causing bottleneck (SLA->B). No variation closes the chain in
  the reverse direction. A bidirectional chain requires that each B-NN bottleneck entry
  also identifies the SLA node(s) it affects, enabling navigation from cause to timing
  impact as well as from timing impact to cause. Without the reverse linkage, the
  bottleneck analysis and the SLA analysis remain two separate lookup tables rather than a
  single coherent evidence structure.
- **Pass condition**: Each identified bottleneck (B-NN) in the C-04 bottleneck analysis
  includes an explicit reference to the SLA node(s) it affects (by state name, SLA row
  ID, or explicit annotation). Combined with C-14 (SLA->B), this closes the chain
  bidirectionally. Fail if the bottleneck section contains no SLA impact references, even
  if the SLA section contains bottleneck cross-references.

### C-17 - Constructed-Answer Format for Exception Sections
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 2 signal: V-02 wildcard observation: question/constructed-answer format
  is the only R2 variation predicted to improve C-02 and C-07 content quality through
  answer synthesis rather than cell-fill. When exception flows and edge cases are
  presented as labeled answer blocks with required sub-fields (Trigger:, Trace:,
  Handling role:, Terminal:, Why problematic:, Correct response:), the model constructs a
  complete answer per item rather than populating a table cell. Cell-fill format allows
  sparse entries that pass column-count checks; constructed-answer format makes incomplete
  entries structurally visible as unanswered sub-fields. This is a format-level pattern
  that raises specificity and completeness independently of structural ordering or phase
  scoping.
- **Pass condition**: Exception flows (C-02) and edge cases (C-07) are each presented as
  per-item answer blocks with explicitly labeled sub-fields. Each sub-field must be
  answered with process-specific content; a blank or "N/A" sub-field is a visible failure.
  Fail if exceptions or edge cases are presented as table rows where sparse cell content
  can satisfy column-count requirements without substantive answers.

### C-18 - Ordinal-Label Structural Enforcement
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 3 signal: V-03 in R3 passes C-15 at the borderline level -- named
  section headers ("Exception Traces for This Phase") precede state tables by construction,
  satisfying the C-15 pass condition. But unnamed headers do not encode ordinal priority as
  a structural constraint: a model can insert content between sections without violating any
  labeled sequence, and two sections with content-based names carry no positional guarantee
  beyond the instruction. SECTION A/B labels (or equivalent ordinal designations) convert
  exception-first ordering from a prose instruction into a named label sequence that cannot
  be reversed without violating a labeled header constraint. A model that writes
  "SECTION B -- STATES" before "SECTION A -- EXCEPTIONS" has violated a named structural
  rule, not merely a style preference. This is the difference between V-03 borderline C-15
  compliance and V-02/V-04 full C-15 compliance.
- **Pass condition**: Each phase section uses explicit ordinal labels (SECTION A/SECTION B,
  or equivalent numbered or lettered designations such as 1./2. or A./B.) to mark exception
  content and state content as an ordered sequence. The exception label must carry a lower
  ordinal than the state label within the same phase block. The ordinal must be part of the
  section header itself, not a prose instruction preceding an unnamed section. Fail if
  section headers are named by content alone (e.g., "Exception Traces", "States") without
  an ordinal marker that encodes positional priority as a labeled constraint. Every C-18
  pass implies C-15 pass; the reverse is not true.

### C-19 - Backward-Chain Evidence Injection
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 3 signal: C-16 requires each B-NN entry to reference the SLA node(s)
  it affects, establishing the backward direction of the chain as a structural element.
  The Evidence field pattern advances this: the backward lookup result is embedded as a
  named structural sub-field in the B-NN answer block -- listing the specific AT-RISK SLA
  rows that cite this B-ID by identifier, making the lookup result part of the block
  rather than a reader-performed check. Without Evidence injection a reader must navigate
  from the B-NN entry to the SLA table and manually verify which AT-RISK rows cite that
  B-ID; with Evidence injection the confirmation is a declared sub-field in the block,
  making incomplete backward references visible as blank sub-fields.
- **Pass condition**: Each B-NN answer block contains a named Evidence field (or equivalent
  sub-field such as "AT-RISK Rows Citing This B-ID:") that lists the specific AT-RISK SLA
  row identifiers or state names that cite this B-ID. The field must be populated with
  specific identifiers; a general reference to "see SLA ANALYSIS" without row-level
  specificity does not satisfy. Fail if the backward reference is present as a general
  column annotation or summary statement rather than an injected per-block sub-field with
  specific AT-RISK row citations. C-19 cannot pass if C-16 fails.

### C-20 - Chain Status Gate
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 3 signal: The bidirectional chain (C-14 forward + C-16 backward) can be
  structurally present in both directions and still require reader-performed navigation to
  confirm closure. A CHAIN STATUS: CLOSED/OPEN gate (or equivalent declaration block)
  converts bidirectional verification into a discrete output element: the output itself
  declares whether the chain is closed rather than leaving verification to the reader.
  CLOSED means every AT-RISK SLA row cites a B-ID (forward complete) and every B-ID's SLA
  impact annotation appears in the SLA table as AT-RISK (backward complete). OPEN means
  one or both directions are incomplete, with the specific gap named. A CLOSED gate that
  is incorrect fails; an OPEN gate that accurately names a real gap passes. The gate makes
  verification failures visible as declared output rather than silent omissions.
- **Pass condition**: A CHAIN STATUS element is declared in the output as an explicit gate
  with CLOSED or OPEN status. A CLOSED status must confirm that both forward (SLA->B) and
  backward (B->SLA) directions are complete, citing the counts or IDs verified. An OPEN
  status must name the specific direction(s) incomplete and the unresolved gap. Fail if
  bidirectional verification is present only as a prose instruction, reader checklist, or
  annotation without a declared status output. C-20 cannot pass if both C-14 and C-16
  fail.

### C-21 - Unified Exception-Block Architecture
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 3 signal: When per-phase exception sections use constructed-answer blocks
  (C-17) within ordinal-labeled phase sections (C-18) that precede state tables (C-15),
  all three structural criteria are satisfied by a single architectural decision rather
  than by three independently specified mechanisms. The convergence matters because it
  reduces the number of independent correct decisions required: a template with SECTION A
  constructed-answer exception blocks per phase satisfies phase-scoped generation before
  state detail (C-13), exception-first ordering (C-15), and synthesis-format completeness
  per exception (C-17) through one structural unit. Outputs that achieve this convergence
  are more robust than outputs that satisfy C-13, C-15, and C-17 through three separate
  structural mechanisms, because the convergence eliminates the possibility of the
  mechanisms conflicting or degrading independently.
- **Pass condition**: The exception sections for each phase use constructed-answer blocks
  (per C-17 pass condition) within an ordinal-labeled section (per C-18 pass condition)
  that structurally precedes the state table (per C-15 pass condition). All three
  constituent criteria (C-13, C-15, C-17) must independently pass. The convergence is the
  architectural coherence: a single SECTION A answer-block structure per phase satisfies
  all three without requiring separate structural mechanisms for each. Fail if any
  constituent criterion (C-13, C-15, C-17) fails, or if the three criteria are satisfied
  through three structurally independent mechanisms rather than a unified per-phase
  exception-block section.

### C-22 - Evidence Field Format Contract
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 4 signal: V-01 and V-03 fail C-19 despite having an Evidence sub-field
  in each B-NN block because the field hint uses a vague description
  (`[AT-RISK entries that list "causal source: B-01" in SLA ANALYSIS]`) without a concrete
  format example and without a preamble fail condition for general references. V-02, V-04,
  and V-05 pass C-19 because their Evidence field hint provides (a) a concrete example in
  the form `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"` and (b) a preamble
  fail condition explicitly stating that a field containing only "see SLA ANALYSIS" or
  state names without AT-RISK row-level specificity does not satisfy. V-05 additionally
  specifies a required format pattern `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
  that removes any remaining ambiguity about what constitutes a compliant entry. The format
  contract converts the Evidence field from a structural placeholder into a format-anchored
  sub-field that makes incomplete entries visibly non-compliant without requiring a reader
  to compare the B-NN block against the SLA table. This is the C-19 analog of C-18's
  relationship to C-15: C-18 adds ordinal enforcement to C-15's position requirement; C-22
  adds format contract to C-19's specificity requirement. Every C-22 pass implies C-19
  pass; the reverse is not true.
- **Pass condition**: Each B-NN answer block's Evidence field hint (or the preamble
  directly preceding the bottleneck section) provides (a) a concrete format example using
  actual S-ID syntax, e.g. `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"` or
  the pattern `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`, and (b) an explicit
  fail condition stating that general references such as "see SLA ANALYSIS" or state names
  without AT-RISK row-level S-ID specificity do not satisfy. The format contract must
  appear in the block hint or a preamble immediately preceding the bottleneck blocks --
  not in a distant general instruction section. Fail if the Evidence field hint uses only
  a general description of what to look for without a format-anchored example and explicit
  fail condition. C-22 cannot pass if C-19 fails. Every C-22 pass implies C-19 pass.

### C-23 - Chain Status Section Isolation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 4 signal: V-01, V-02, and V-04 fail C-20 despite containing a CHAIN
  STATUS declaration because it appears as a line within the `Bidirectional evidence
  check:` sub-block embedded inside the SLA ANALYSIS section. A declaration embedded in a
  larger section is not a discrete output element: a reader must navigate into SLA
  ANALYSIS, locate the bidirectional check sub-block, and find the status line -- the same
  navigation task C-20 was intended to eliminate. V-03 and V-05 pass C-20 by using a
  dedicated `## CHAIN STATUS` top-level section after SLA ANALYSIS, with
  `CHAIN STATUS: [CLOSED / OPEN]` as the first output element of that section, followed by
  Forward and Backward direction enumeration. Both V-03 and V-05 include a preamble
  instruction: "Do not embed chain status as a line inside the SLA ANALYSIS section."
  Section isolation converts the chain status from an annotation inside a check block into
  a first-class output artifact locatable without section navigation. Every C-23 pass
  implies C-20 pass.
- **Pass condition**: CHAIN STATUS is declared as the first output element of a dedicated
  top-level section (`##` heading or equivalent structural separator that is not a
  sub-section of SLA ANALYSIS or any other section). The dedicated section must appear
  after SLA ANALYSIS in document order and must include Forward and Backward direction
  enumeration as subsequent elements. An explicit anti-embedding instruction ("Do not embed
  chain status inside the SLA ANALYSIS section" or equivalent prohibition) must appear in
  the preamble or section instruction immediately preceding or within the dedicated CHAIN
  STATUS section. Fail if CHAIN STATUS appears only as an embedded line or annotation
  within another section. C-23 cannot pass if C-20 fails. Every C-23 pass implies C-20
  pass.

### C-24 - Evidence Field Format Dual Redundancy
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 5 signal: R5 V-02 and V-03 pass C-22 with the concrete named domain
  example in the global preamble only; per-block hints carry minimal references. V-05
  repeats the concrete example in BOTH the preamble AND each individual B-NN per-block
  hint. Dual-location placement is to C-22 what C-22 is to C-19: a structural escalation
  that makes the format contract discoverable regardless of reader entry point. A
  preamble-only contract requires the reader to have encountered the preamble before any
  block; if the preamble is skipped, the per-block hint provides no filled-in anchor.
  Dual-location placement combines both guarantees: the preamble provides
  discovery-independent anchoring; the per-block repeat makes each B-NN block
  self-contained and resistant to format drift. C-24 requires both locations to carry
  concrete filled-in examples. Every C-24 pass implies C-22 pass; C-24 cannot pass if
  C-22 fails.
- **Pass condition**: (a) The global preamble or the preamble immediately preceding the
  bottleneck section contains a concrete named domain example with filled-in S-ID syntax
  (e.g., `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`) and an explicit
  fail condition for general references, AND (b) each individual B-NN block's Evidence
  field hint also contains a concrete format example (not a bracket template with
  unfilled placeholders). Both (a) and (b) must be satisfied independently. Fail if the
  concrete example appears only in the preamble without per-block repetition, if per-block
  hints use an unfilled bracket template without a filled-in domain example, or if either
  location omits the fail condition. C-24 cannot pass if C-22 fails. Every C-24 pass
  implies C-22 pass.

### C-25 - Anti-Embedding Dual Enforcement
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 5 signal: R5 establishes that section-proximate anti-embedding is fully
  equivalent to global-preamble anti-embedding for C-23 pass -- neither location is
  privileged. V-05 places the prohibition in both locations: the global preamble states
  the constraint before any section, and the CHAIN STATUS section instruction opens with
  the same prohibition immediately before the gate is generated. The two placements are
  complementary: a model that generates SLA ANALYSIS without retaining the preamble
  instruction will encounter the prohibition when generating the CHAIN STATUS section.
  This is the C-23 analog of C-24's dual-location Evidence field contract. Every C-25
  pass implies C-23 pass; C-25 cannot pass if C-23 fails.
- **Pass condition**: The anti-embedding instruction appears in BOTH (a) the global
  preamble or the instruction block preceding the SLA ANALYSIS section, AND (b) as the
  first or second content element of the dedicated CHAIN STATUS section instruction. Both
  locations must carry an explicit prohibition; a general style suggestion does not
  satisfy either location. Fail if the instruction appears in only one location. C-25
  cannot pass if C-23 fails. Every C-25 pass implies C-23 pass.

### C-26 - Evidence Field Axis Separation
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 5 signal: C-19 (structure) and C-22 (contract) are independent axes of
  the Evidence field requirement. When both axes are bundled into a single prose hint, a
  model may satisfy one while missing the other, and a reviewer cannot independently check
  each axis. C-26 requires the Evidence field instruction to present both axes as
  explicitly labeled, visually distinct components. The V-05 pattern achieves this with
  three labeled sub-fields per B-NN block: field intent, a `Required format:` labeled line
  with the structural pattern, and a `Fail condition:` labeled line with the explicit
  prohibition. C-26 cannot pass if C-22 fails.
- **Pass condition**: The Evidence field instruction (in the preamble and/or each B-NN
  per-block hint) contains both of the following as explicitly labeled and visually
  distinct elements: (a) a structural format specification stated as a labeled line or
  sub-field (e.g., `Required format: [State name -- S-ID]: AT-RISK, causal source:
  B-[ID]`), and (b) a contract specification -- a concrete filled-in domain example plus
  an explicit fail condition stated as a labeled line or sub-field. Both (a) and (b) must
  be identifiable as independent labeled elements; a single sentence that contains both a
  format pattern and a fail condition does not satisfy. Fail if the Evidence field hint
  bundles structure and contract into a single unlabeled prose description. C-26 cannot
  pass if C-22 fails.

### C-27 - Evidence Field Axis Dual-Location Separation
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 6 signal: R6 V-03 demonstrates that preamble-only labeled axis
  separation passes C-26 -- per-block hints carry only a minimal back-reference ("using
  the format above") without restating the labeled axes. R6 V-02 achieves C-26 with
  labeled axes in BOTH the preamble AND each B-NN per-block hint. C-27 encodes this
  dual-location requirement: the relationship mirrors the chain for concrete domain
  examples (C-22 escalates to C-24; C-26 escalates to C-27). A per-block back-reference
  without restated labeled axes is not self-contained for axis verification. C-27 cannot
  pass if C-26 fails. Every C-27 pass implies C-26 pass.
- **Pass condition**: (a) The global preamble or preamble immediately preceding the
  bottleneck section contains the Evidence field instruction with explicitly labeled
  `Required format:` and `Fail condition:` sub-fields (per C-26 pass condition at the
  preamble location), AND (b) each individual B-NN per-block hint ALSO contains the same
  explicitly labeled sub-fields -- not a back-reference or pointer to the preamble.
  Per-block presence of "using the format above" or equivalent without restated labeled
  axes fails (b). Both (a) and (b) must be satisfied independently. C-27 cannot pass if
  C-26 fails. Every C-27 pass implies C-26 pass.

### C-28 - Evidence Format Pattern B-ID Instantiation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 7 signal: V-02 achieves C-27 with per-block `Required format: [State
  name -- S-ID]: AT-RISK, causal source: B-[ID]` -- the structural format axis retains a
  generic `B-[ID]` bracket placeholder in every B-NN block. C-28 requires the
  `Required format:` labeled axis in each B-NN per-block hint to be instantiated with the
  specific B-ID for that block: B-01's hint states `causal source: B-01`, B-02's hint
  states `causal source: B-02`. An instantiated format pattern makes cross-block Evidence
  non-compliance directly detectable by string comparison without placeholder resolution.
  C-28 is to C-27 what C-27 is to C-26: a per-block specificity escalation on the same
  structural axis. Every C-28 pass implies C-27 pass; C-28 cannot pass if C-27 fails.
- **Pass condition**: Each B-NN per-block `Required format:` axis uses the specific B-ID
  for that block spelled out as a literal identifier (e.g., B-01 block states
  `Required format: [State name -- S-ID]: AT-RISK, causal source: B-01`; B-02 states
  `causal source: B-02`). A `Required format:` line using `B-[ID]`, `B-[N]`, `B-NN`, or
  any bracket placeholder fails, even if the prose line identifies the owning B-ID. Check
  each B-NN block independently. Fail if any B-NN per-block hint uses a generic
  placeholder in the `Required format:` axis. C-28 cannot pass if C-27 fails. Every C-28
  pass implies C-27 pass.

### C-29 - B-NN Scaffold Completeness Prerequisite Declaration
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Round 7 signal: R6 B-02 lacked the Evidence field entirely, making per-block
  dual-location criteria structurally unevaluable for B-02's scope -- the criterion could
  not be tested, not merely failed. C-29 converts the implicit prerequisite into a named
  structural gate: the template must contain an explicit instruction that ALL declared
  B-NN blocks carry the Evidence field. A template with N declared B-NN blocks but only
  k < N carrying the Evidence field fails C-29 even if the k carrying blocks fully satisfy
  C-27. C-29->C-27.
- **Pass condition**: The template contains an explicit instruction -- in the preamble, in
  the bottleneck section header, or as a named structural gate before the first B-NN block
  -- stating that ALL B-NN blocks in the template must carry the Evidence field. The
  instruction must be explicit (naming scaffold completeness or equivalent) rather than
  implied by the "each B-NN" quantifier language in C-27's per-block hint. A template
  where any B-NN block lacks the Evidence field entirely fails C-29 regardless of whether
  the present blocks satisfy C-27. Fail if the completeness requirement is only derivable
  from per-block inspection without a named prerequisite gate or instruction. C-29 cannot
  pass if C-27 fails.

### C-30 - Dual-Location Requirements Consolidated Declaration
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 7 signal: two symmetric escalation pairs (C-22/C-24 and C-26/C-27) have
  accumulated through R4-R7, each encoding a base criterion (preamble sufficient) and its
  dual-location escalation. The locality invariant has stabilized: at high rubric maturity,
  the discriminating aspirational gap is consistently a locality failure, not a content
  failure. C-30 encodes the locality invariant as a named structural property: the template
  contains a consolidated dual-location requirements block listing BOTH locality properties
  together in one declaration. A consolidated declaration makes the full locality contract
  discoverable at one point without requiring per-criterion cross-reference. C-30 cannot
  pass if C-24 or C-27 fails. Every C-30 pass implies C-24 and C-27 both pass.
- **Pass condition**: The template contains a named consolidated declaration -- a labeled
  block, a named section, or an enumerated list with an explicit header such as
  "DUAL-LOCATION REQUIREMENTS:" or "LOCALITY CONTRACT:" or equivalent -- that explicitly
  lists BOTH dual-location properties: (a) the concrete named domain example (per C-24)
  must appear at both preamble and per-block location, and (b) the `Required format:` and
  `Fail condition:` labeled axes (per C-27) must appear at both preamble and per-block
  location. Fail if dual-location requirements are discoverable only by reading individual
  criterion hints without a consolidated declaration. C-30 cannot pass if C-24 or C-27
  fails. Every C-30 pass implies C-24 and C-27 both pass.

### C-31 - Scaffold Gate Forward-Reference Structural Position
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 8 signal: V-02 passes C-29 with "SCAFFOLD REQUIREMENT: ALL B-NN blocks
  declared below must carry an Evidence field". The phrase "declared below" is
  forward-reference language scoping the gate's ALL quantifier to B-NN blocks following
  the gate in document order. C-29 requires the gate to exist; C-31 requires it to appear
  before the first B-NN block in document order AND to use forward-reference language that
  makes its positional scope explicit. A gate positioned after the B-NN blocks it claims
  to govern is a retroactive declaration, not a prerequisite gate. C-31 cannot pass if
  C-29 fails. Every C-31 pass implies C-29 pass.
- **Pass condition**: (a) The scaffold completeness gate appears before the first B-NN
  block header in document order -- a reader encountering the gate has not yet seen any
  B-NN block, AND (b) the gate uses forward-reference language ("declared below", "that
  follow", "listed below", or equivalent) that explicitly establishes its scope as applying
  to B-NN blocks following it. Both (a) and (b) must hold independently. A gate using only
  "all B-NN blocks" without positional scope language fails (b). C-31 cannot pass if C-29
  fails. Every C-31 pass implies C-29 pass.

### C-32 - Dual-Location Consolidated Block Canonical Axis Citation
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 8 signal: V-02 passes C-30 with a consolidated block explicitly naming
  "(2) labeled axes (`Required format:`/`Fail condition:`) at both locations". C-30
  requires the consolidated block to enumerate both dual-location properties; C-32 requires
  the enumeration to name the `Required format:` and `Fail condition:` axes by their
  canonical labels as used elsewhere in the template. This makes the consolidated block a
  navigable cross-reference: a reviewer can match a label in the consolidated declaration
  directly to a label in the per-block hint without label translation. C-32 cannot pass if
  C-30 fails. Every C-32 pass implies C-30 pass.
- **Pass condition**: The consolidated dual-location declaration names the `Required
  format:` and `Fail condition:` axes using those exact labels (or the canonical label pair
  as established in C-26's per-block hint structure throughout the template). The labels
  must appear as recognizable strings in the consolidated block, not as paraphrases,
  descriptions, or equivalent-meaning alternatives. A consolidated block that says
  "concrete example at both locations" and "labeled axes at both locations" satisfies C-30
  but not C-32 unless it identifies the axes by name. Fail if the consolidated block
  describes the axis properties without citing canonical label strings. C-32 cannot pass
  if C-30 fails. Every C-32 pass implies C-30 pass.

### C-33 - Preamble Concrete Example B-ID Alignment
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 8 signal: V-02 passes both C-24 (preamble concrete example uses B-01)
  and C-28 (per-block `Required format:` instantiated with block-specific B-ID). When
  both hold, the preamble anchor and the first per-block instantiation are consistent by
  string comparison. C-33 requires this alignment explicitly: the preamble concrete
  example (C-24) must name the same B-ID as the first declared B-NN block. A preamble
  example using a generic placeholder or a non-first-block B-ID introduces a
  preamble-level inconsistency that C-28 closes at per-block scope but leaves open at
  the preamble boundary. C-33 is to C-24 what C-28 is to C-27. C-33 cannot pass if C-24
  or C-28 fails. Every C-33 pass implies C-24 and C-28 both pass.
- **Pass condition**: The preamble concrete example required by C-24 uses the same literal
  B-ID as the first declared B-NN block in the template (typically B-01). The preamble
  example B-ID must be a literal identifier (B-01, B-02, etc.), not a bracket placeholder.
  Fail if the preamble concrete example uses a generic B-ID placeholder, a B-ID that does
  not match the first declared bottleneck block, or omits the B-ID from the causal source
  field entirely. C-33 cannot pass if C-24 or C-28 fails. Every C-33 pass implies C-24
  and C-28 both pass.

### C-34 - Incumbent Baseline IM-ID Cross-Section Traceability
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 9 signal: V-01 establishes an INCUMBENT BASELINE section containing a
  table that assigns IM-IDs (e.g., IM-01, IM-02) to named failure modes observed in the
  current-state process before any phase is traced. Each B-NN bottleneck block's Cause
  field cites one or more of these IM-IDs, creating a cross-section traceability chain in
  the Baseline->B-NN direction. C-34 is orthogonal to the SLA<->B-NN bidirectional chain
  (C-14/C-16): it covers the Baseline->B-NN direction, enabling a reviewer to
  string-compare an IM-ID from the baseline table to the Cause field of the B-NN block
  that it motivates. C-34 cannot pass if C-04 fails.
- **Pass condition**: An INCUMBENT BASELINE section (or equivalent pre-phase artifact,
  appearing before the first phase block in document order) declares at least two named
  failure modes with IM-ID identifiers (IM-01, IM-02, etc.). Each B-NN bottleneck block's
  Cause field cites at least one IM-ID from the baseline table by literal identifier (e.g.,
  "driven by IM-02" or "root cause: IM-01"). The citation must be a literal IM-ID
  identifier, not a paraphrase without the ID. Fail if bottleneck Cause fields name root
  causes without citing a baseline IM-ID, or if the INCUMBENT BASELINE section assigns no
  IM-IDs. C-34 cannot pass if C-04 fails.

### C-35 - Cost-of-No-Action Baseline Quantification
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 9 signal: V-01 declares a quantified accumulating metric in the
  INCUMBENT BASELINE section before the first phase is traced -- a named measure with a
  declared current-state value or rate (e.g., "Average delay per rejection: 3.2 days",
  "Rejection rate: 18%"). This cost-of-no-action anchor grounds the bottleneck analysis in
  observable behavior. C-35 requires the quantification to appear before the first phase
  block in document order: a metric declared after phase tracing has begun is a
  retrospective annotation, not a baseline constraint. C-35 cannot pass if C-34 fails.
  Every C-35 pass implies C-34 pass.
- **Pass condition**: The INCUMBENT BASELINE section (per C-34 pass condition) contains at
  least one quantified metric -- a named measure with a declared current-state value or
  percentage -- appearing before the first phase block in document order. The metric must
  be specific: a named measure plus a numeric value or rate. A narrative description of
  process pain without a quantified measure does not satisfy. Fail if the baseline section
  names failure modes and IM-IDs but carries no quantified metric, or if a quantified
  metric appears only after the first phase block. C-35 cannot pass if C-34 fails. Every
  C-35 pass implies C-34 pass.

### C-36 - Phase-Exit Gate Named Sub-Field Architecture
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 9 signal: V-02 establishes PHASE ENTRY CONTRACT and PHASE EXIT GATE
  blocks as named structural elements within each phase section, carrying explicitly named
  sub-fields. These named sub-fields establish phase-entry and phase-exit as structural
  artifacts distinct from state-transition rows: a reviewer can locate the entry constraint
  and exit verification for any phase as first-class output elements without parsing state
  tables. C-36 requires both entry and exit gate blocks to be present per phase with
  explicitly named sub-fields; an explicit bottleneck ID citation in the gate is not
  required for C-36 (that is C-37). C-36 cannot pass if C-04 fails.
- **Pass condition**: Each phase section contains both a PHASE ENTRY CONTRACT block and a
  PHASE EXIT GATE block (or equivalent named structural elements). The PHASE ENTRY
  CONTRACT must carry at minimum: Entry Condition and one blocking or pre-condition
  sub-field. The PHASE EXIT GATE must carry at minimum: Exit Condition, Required outputs,
  and one blocking or verification sub-field. All sub-fields must be named (labeled)
  structural elements -- not prose paragraphs or inline annotations. A template that
  carries gate blocks for some phases but omits them for others fails C-36. C-36 cannot
  pass if C-04 fails.

### C-37 - Phase Exit Gate B-ID Forward Reference
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 10 signal: V-02 adds a `Blocked bottleneck: B-NN or NONE` sub-field to
  the PHASE EXIT GATE block established by C-36. This sub-field names the B-ID (or NONE
  if no bottleneck blocks the exit) that can delay phase completion. The B-ID is a forward
  reference: assigned before the Bottleneck Analysis section is generated, and later
  verified against the bottleneck block identifier in that section. C-36 established the
  structural slot; C-37 requires that slot to carry a B-ID linkage, creating the
  Phase->B-NN traceability direction. This direction is orthogonal to both the SLA<->B-NN
  chain (C-14/C-16) and the Baseline->B-NN chain (C-34): the three chains form a
  multi-directional network in which every B-NN block is reachable from three independent
  source artifacts (SLA AT-RISK row, INCUMBENT BASELINE IM-ID, and PHASE EXIT GATE). The
  detectability property is string comparison: "B-02" in the exit gate and "B-02" in the
  Bottleneck Analysis block are consistent by inspection without reader inference.
- **Pass condition**: Each PHASE EXIT GATE block (per C-36 pass condition) contains a
  `Blocked bottleneck:` sub-field (or equivalent named sub-field) that carries either a
  literal B-ID (e.g., `Blocked bottleneck: B-02`) or an explicit NONE declaration. The
  sub-field must be a named structural element within the exit gate block, not a prose
  annotation appended to the gate's Blocking condition field. The cited B-ID must match a
  declared B-NN block identifier in the Bottleneck Analysis section. A gate that carries
  a `Blocking condition:` prose description without a separate `Blocked bottleneck:` B-ID
  sub-field satisfies C-36 but fails C-37. Check every phase's exit gate independently;
  omission in any phase fails C-37 overall. C-37 cannot pass if C-36 fails or C-04 fails.
  Every C-37 pass implies C-36 pass.

### C-38 - Role Sequence Schedule Phase Ownership Declaration
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 10 signal: V-01 introduces a ROLE SEQUENCE SCHEDULE block declared after
  the Role Registry Gate (C-12) and before PHASE 1. The schedule maps each R-ID to the
  phases they own, with at minimum: the primary activation trigger, the handoff trigger,
  and any parallel windows. This creates Role->Phase traceability as a pre-phase structural
  artifact: the schedule enables a reviewer to string-compare an R-ID from the schedule
  directly to an R-ID in the phase's entry contract pre-condition check or exit
  verification field, without navigating the full role registry. C-38 cannot pass if C-12
  fails.
- **Pass condition**: A named ROLE SEQUENCE SCHEDULE block appears in the output after
  the Role Registry Gate (C-12 output) and before the first PHASE block in document order.
  The schedule must map at least two R-IDs from the role registry to their owned phases,
  with explicitly named sub-fields for: (a) the phase(s) owned, (b) the activation
  trigger, and (c) the handoff trigger. Parallel windows are required if the process has
  declared concurrent paths (C-06 pass condition met). All R-IDs cited in the schedule
  must match literal identifiers in the Role Registry Gate output. Fail if the schedule
  is absent, uses free-text role names without R-ID identifiers, or cites R-IDs not in
  the registry. A role list embedded in a phase description does not satisfy the pre-phase
  schedule position requirement. C-38 cannot pass if C-12 fails.

### C-39 - B-NN Cause Field Dual Citation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 10 signal: V-01 (confirmed V-04/V-05) extends the B-NN Cause field
  beyond the single IM-ID citation required by C-34 to include a second citation: the
  blocking R-ID from the ROLE SEQUENCE SCHEDULE. The dual citation creates a three-way
  intersection: IM-01 in INCUMBENT BASELINE, R-02 in ROLE SEQUENCE SCHEDULE, and both
  identifiers in the B-NN Cause field. All three string comparisons are independently
  verifiable. C-39 is the convergence criterion for C-34 and C-38: the Cause field closes
  both directions explicitly. Without C-39, the bottleneck block's Cause field leaves the
  role-ownership attribution as reader inference. C-39 cannot pass if C-34 fails or C-38
  fails. Every C-39 pass implies C-34 and C-38 both pass.
- **Pass condition**: Each B-NN bottleneck block's Cause field contains both (a) a literal
  IM-ID from the INCUMBENT BASELINE table (per C-34 pass condition) and (b) a literal
  R-ID from the ROLE SEQUENCE SCHEDULE naming the role whose ownership pattern or handoff
  gap creates or amplifies the bottleneck (e.g., "Cause: Manual re-keying under R-02
  ownership, root cause IM-01"). Both identifiers must be literal strings matching their
  respective source artifacts. The R-ID citation must cite an R-ID that appears in the
  ROLE SEQUENCE SCHEDULE (C-38), not merely in the role registry. Fail if any B-NN Cause
  field cites only an IM-ID without an R-ID, or cites an R-ID absent from the ROLE
  SEQUENCE SCHEDULE. C-39 cannot pass if C-34 fails or C-38 fails. Every C-39 pass
  implies C-34 and C-38 both pass.

### C-40 - Exception Block Role-Sequence Cross-Reference
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 11 signal: V-04 extends the EX block sub-field set to include a named
  R-ID citation (in the Bottleneck Ref sub-field or a dedicated Role Ref sub-field)
  identifying the R-ID from the ROLE SEQUENCE SCHEDULE whose phase-ownership window
  encompasses the exception's triggering phase. This creates the Exception->Role
  traceability direction: an EX block in PHASE 2 citing R-02 allows a reviewer to
  string-compare that R-ID directly to R-02's entry in the ROLE SEQUENCE SCHEDULE without
  navigating the full role registry. Additionally, V-04 gates the Role Registry Gate
  validation on EX block presence: each declared R-ID must appear in at least one EX
  block's role-citation sub-field, closing the chain bidirectionally (Role->Exception in
  the gate, Exception->Role in the EX block). V-05 confirms the pattern composes with the
  Prior-Phase sub-field (C-41) without degradation.

  C-40 is the fourth orthogonal traceability direction alongside SLA<->B-NN (C-14/C-16),
  Baseline->B-NN (C-34), and Phase->B-NN (C-37). The structural property is string
  comparison: R-02 in the EX block and R-02 in the ROLE SEQUENCE SCHEDULE for the same
  phase are consistent by inspection without registry lookup. The registry gate closure
  (Role->Exception) ensures that no declared R-ID is a "dark" role with registry presence
  but no traceable exception activity, making the schedule and registry jointly auditable
  against exception outputs. C-40 cannot pass if C-38 fails (the ROLE SEQUENCE SCHEDULE
  is the source artifact for R-ID declarations) or C-13 fails (exception traces must be
  phase-scoped for the phase-ownership match to be verifiable).
- **Pass condition**: (a) Each EX block carries a named sub-field -- labeled "Role Ref:",
  "Owning R-ID:", "Responsible Role:", or equivalent -- citing a literal R-ID from the
  ROLE SEQUENCE SCHEDULE whose phase-ownership mapping covers the phase containing this
  exception trace. The R-ID must be a literal identifier (e.g., R-02) matching a ROLE
  SEQUENCE SCHEDULE entry; a free-text role name without an R-ID identifier fails; a cited
  R-ID absent from the ROLE SEQUENCE SCHEDULE fails; a cited R-ID whose schedule phase
  mapping does not include the EX block's originating phase fails. AND (b) the Role
  Registry Gate section (C-12 output) or the ROLE SEQUENCE SCHEDULE block (C-38 output)
  includes an explicit gate validation confirming that each declared R-ID appears in at
  least one EX block's role-citation sub-field -- the gate must be a named structural
  element (labeled check, validation instruction, or equivalent), not an implicit
  assumption. Both (a) and (b) must be independently satisfied. Fail if any EX block
  lacks an R-ID citation sub-field, if a cited R-ID does not appear in the ROLE SEQUENCE
  SCHEDULE, or if the registry gate validation is absent. C-40 cannot pass if C-38 fails
  or C-13 fails.

### C-41 - Phase Entry Contract Prior-Phase Sequential Linkage
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 11 signal: V-05 extends the PHASE ENTRY CONTRACT block established by
  C-36 with a named `Prior phase:` sub-field identifying the preceding phase by its
  literal phase identifier (e.g., "Prior phase: PHASE 1"). The first phase carries an
  explicit sentinel value (NONE, INIT, or equivalent) indicating no prior phase. This
  creates Phase->Phase sequential traceability as a named structural property: the phase
  sequence is not derived from document order alone but declared as an entry condition,
  making out-of-order phase rendering detectable as an identifier mismatch.

  C-37 fills the exit gate's B-ID slot (Phase->B-NN forward reference on the exit side);
  C-41 fills the entry contract's phase-sequencing slot (Phase->Phase backward reference
  on the entry side). Together they form complete gate-to-gate phase linkage: the exit
  gate declares which bottleneck may block the phase (forward), and the entry contract
  declares which phase this follows (backward). The structural property is string
  comparison: the `Prior phase:` identifier in PHASE 2's entry contract must match the
  identifier used to label PHASE 1's block in document order. The sentinel requirement for
  PHASE 1 ensures that the chain's start is declared explicitly rather than implied by
  document-initial position. C-41 cannot pass if C-36 fails.
- **Pass condition**: Each PHASE ENTRY CONTRACT block (per C-36 pass condition) contains
  a named `Prior phase:` sub-field (or equivalent: "Preceding phase:", "Previous phase:",
  or a canonically labeled sub-field with the same semantics) carrying a literal phase
  identifier. For all phases after the first: the identifier must match the label of the
  immediately preceding phase block in document order (e.g., if PHASE 1 is labeled
  "PHASE 1 -- Initiation", the Prior phase: field in PHASE 2's entry contract must cite
  "PHASE 1" or "PHASE 1 -- Initiation" as a recognizable string match). For the first
  phase: the sub-field must carry an explicit sentinel value (NONE, INIT, START, or
  equivalent) rather than a phase identifier or blank. The sub-field must be a named
  labeled element within the entry contract block -- not a prose annotation appended to
  the Entry Condition field. Fail if any PHASE ENTRY CONTRACT lacks the Prior phase:
  sub-field, if a non-first phase carries a sentinel instead of a phase identifier, if the
  identifier does not string-match the preceding phase label, or if the first phase carries
  a non-sentinel value. C-41 cannot pass if C-36 fails.

---

## Scoring Formula

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 33 * 10)

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band   | Score                   | Meaning                                    |
|--------|-------------------------|--------------------------------------------|
| Gold   | >= 80 + all essential   | Output is production-ready signal artifact |
| Silver | >= 65 + all essential   | Useful with minor gaps                     |
| Bronze | >= 50 + all essential   | Usable but incomplete                      |
| Fail   | any essential fails     | Not useful regardless of score             |

---

## Evaluation Notes

- Grade each criterion pass/fail -- no partial credit per criterion.
- For C-01 and C-05 use the state diagram or trace table as the evidence base.
- For C-02 and C-07 verify that exception flows and edge cases are non-overlapping and
  process-specific before counting toward their respective totals.
- For C-03 verify the role set matches the declared process type.
- For C-06 the parallel path may be represented as a fork/join diagram, a two-column
  table, or explicit prose with a labeled synchronization point -- any structural form
  counts.
- For C-08 a pass requires a fallback branch; type-column annotation alone does not satisfy
  the exhaustive outcome requirement (see C-11 for the stronger structural form).
- For C-11 a dedicated block per decision point is required; column annotation is not
  sufficient even if it includes a Fallback column.
- For C-12 the registry must precede the first state trace; a role list embedded in a
  process profile section does not satisfy the gate requirement.
- For C-13 count only traces that are explicitly labeled with their originating phase or
  state; flat lists without phase anchoring do not qualify even if the trace text mentions
  a phase incidentally.
- For C-14 the cross-reference must be explicit: the SLA at-risk entry names the B-NN, or
  a cross-ref column carries the ID. Prose mention without ID linkage does not satisfy.
- For C-15 position is the evidence: the exception section must appear in the output before
  the state table for the same phase. A column in the state table does not satisfy even if
  the column is labeled Phase/State Origin.
- For C-16 check the bottleneck section (C-04 output), not the SLA section. The B-NN
  entry itself must name an SLA node. A bidirectional pass requires C-14 to also pass;
  C-16 cannot pass if C-14 fails.
- For C-17 inspect each exception flow and edge case item individually. A table row with
  sparse cells fails even if all column headers are present. Pass requires every sub-field
  per item to contain process-specific content.
- For C-18 the ordinal marker must be in the section header itself (e.g., "SECTION A --
  EXCEPTIONS", "1. Exception Traces"); a prose instruction preceding an unnamed section
  does not satisfy. V-03-style unnamed headers ("Exception Traces for This Phase") fail
  C-18 even when they pass C-15.
- For C-19 inspect each B-NN answer block individually. A sub-field that names specific
  AT-RISK row IDs passes; a field that says only "see SLA ANALYSIS" or names SLA states in
  general without AT-RISK row specificity fails. C-19 cannot pass if C-16 fails.
- For C-20 the CHAIN STATUS declaration must be an explicit output element -- a labeled
  block or gate, not a prose sentence embedded in a section. CLOSED status requires
  enumeration confirming both directions. An OPEN status that accurately describes the gap
  also passes. C-20 cannot pass if both C-14 and C-16 fail.
- For C-21 all three constituent criteria (C-13, C-15, C-17) must independently pass
  first. Then confirm that a single per-phase SECTION A constructed-answer block is the
  mechanism satisfying all three. If C-13 passes via a Phase column and C-17 passes via
  answer blocks in a separate flat section and C-15 passes via section ordering, C-21
  fails -- the mechanisms are not unified.
- For C-22 locate the Evidence field hint in the B-NN block template or in the preamble
  immediately preceding the bottleneck section. The hint must contain (a) a concrete
  example with S-ID syntax and (b) an explicit fail condition naming general references as
  non-compliant. C-22 cannot pass if C-19 fails.
- For C-23 verify that the CHAIN STATUS section has its own `##`-level heading (or
  equivalent) that is not nested under SLA ANALYSIS or any other section. The
  `CHAIN STATUS: [CLOSED / OPEN]` line must be the first content line of that section. The
  preamble or section instruction must explicitly prohibit embedding. C-23 cannot pass if
  C-20 fails.
- For C-24 check both locations independently. The preamble must carry a filled-in domain
  example (not a bracket template); each B-NN per-block hint must also carry a concrete
  example (not a general description or bracket template with unfilled placeholders).
  C-24 cannot pass if C-22 fails.
- For C-25 check both locations independently. Look for the anti-embedding prohibition in
  the global preamble (before the SLA ANALYSIS section) AND inside the CHAIN STATUS
  section instruction itself (as a first or second element). A prohibition in only one
  location satisfies C-23 but not C-25. C-25 cannot pass if C-23 fails.
- For C-26 locate the Evidence field instruction and verify that it contains two
  independently labeled elements: (a) a structural format specification under a label such
  as "Required format:" and (b) a contract specification under a label such as "Fail
  condition:". A single prose sentence that combines a format pattern and a fail condition
  fails C-26. C-26 cannot pass if C-22 fails.
- For C-27 check both locations independently. The preamble must carry `Required format:`
  and `Fail condition:` as explicitly labeled, visually distinct sub-fields. Each B-NN
  per-block hint must ALSO carry these same labeled sub-fields; "using the format above"
  or any equivalent back-reference without restated labeled axes fails (b). C-27 cannot
  pass if C-26 fails.
- For C-28 locate the `Required format:` axis in each B-NN per-block hint. The B-ID must
  be a literal identifier in the format pattern itself -- not a bracket placeholder. Check
  each B-NN block independently. C-28 cannot pass if C-27 fails.
- For C-29 look for an explicit instruction about scaffold completeness at or before the
  first B-NN block. The instruction must explicitly state that ALL B-NN blocks carry the
  Evidence field. If any B-NN block lacks the Evidence field entirely, C-29 fails. C-29
  cannot pass if C-27 fails.
- For C-30 locate a consolidated dual-location declaration block with a named header or
  label. The block must enumerate BOTH locality properties together. Adjacent paragraphs
  without a unifying header do not satisfy. C-30 cannot pass if C-24 or C-27 fails.
- For C-31 verify TWO independent conditions: (a) the scaffold gate appears before the
  first B-NN block header in the document; (b) the gate text uses forward-reference
  language. A gate using "ALL B-NN blocks in this section" without positional scope fails
  (b). C-31 cannot pass if C-29 fails.
- For C-32 locate the consolidated dual-location declaration (C-30 pass condition). Check
  whether the axis names cited match the canonical labels as they appear in the per-block
  hints: look for the exact strings `Required format:` and `Fail condition:`. Paraphrases
  fail even if the reader can infer the referent. C-32 cannot pass if C-30 fails.
- For C-33 locate the preamble concrete example (C-24 evidence) and read its
  `causal source:` field. Check that the B-ID named is a literal identifier AND that it
  matches the first declared B-NN block's identifier. C-33 cannot pass if C-24 or C-28
  fails.
- For C-34 locate the INCUMBENT BASELINE section and verify it appears before the first
  phase block in document order. Confirm it contains at least two IM-ID entries. Then
  inspect each B-NN block's Cause field for a literal IM-ID citation. A Cause field that
  describes the root cause in prose without citing the IM-ID by identifier fails C-34.
  C-34 cannot pass if C-04 fails.
- For C-35 locate the quantified metric in the INCUMBENT BASELINE section (per C-34).
  Verify it contains a named measure plus a numeric value or percentage before the first
  phase block. A narrative description without a specific number fails. C-35 cannot pass
  if C-34 fails.
- For C-36 locate each phase section and verify the presence of BOTH a PHASE ENTRY
  CONTRACT block AND a PHASE EXIT GATE block. Check that each block contains explicitly
  named sub-fields. A template with gates in one phase but not another fails C-36. C-36
  cannot pass if C-04 fails.
- For C-37 locate each PHASE EXIT GATE block (C-36 pass condition already required) and
  check for a `Blocked bottleneck:` sub-field distinct from the `Blocking condition:` prose
  field. The sub-field must carry a literal B-ID or the token NONE. Verify that any cited
  B-ID matches a declared B-NN block identifier. Check every phase's exit gate
  independently. C-37 cannot pass if C-36 fails or C-04 fails.
- For C-38 verify TWO independent conditions: (a) a named ROLE SEQUENCE SCHEDULE block
  appears after the Role Registry Gate output and before the first PHASE block; (b) the
  schedule contains explicitly named sub-fields for phase ownership, activation trigger,
  and handoff trigger for at least two R-IDs from the registry. R-IDs must match literal
  identifiers in the Role Registry Gate. C-38 cannot pass if C-12 fails.
- For C-39 inspect each B-NN block's Cause field individually. The field must contain BOTH
  a literal IM-ID AND a literal R-ID from the ROLE SEQUENCE SCHEDULE (not merely the role
  registry). A Cause field with only an IM-ID fails C-39 even if C-34 passes. A Cause
  field citing an R-ID absent from the schedule fails C-39. Check each B-NN block
  independently. C-39 cannot pass if C-34 fails or C-38 fails.
- For C-40 verify TWO independent conditions: (a) inspect each EX block individually for
  a named R-ID citation sub-field ("Role Ref:", "Owning R-ID:", "Responsible Role:", or
  equivalent). The sub-field must carry a literal R-ID that appears in the ROLE SEQUENCE
  SCHEDULE's phase-ownership mapping for the phase containing the EX block. A free-text
  role name without an R-ID identifier fails; a cited R-ID absent from the ROLE SEQUENCE
  SCHEDULE fails; a cited R-ID whose schedule phase mapping does not include the EX
  block's originating phase fails. (b) Locate a named gate validation in the Role Registry
  Gate or ROLE SEQUENCE SCHEDULE confirming that each declared R-ID appears in at least
  one EX block's role-citation sub-field. An implicit assumption that R-IDs will appear
  in EX blocks does not satisfy; the gate must be a named structural element. Check all
  EX blocks independently; omission in any EX block fails (a). If any R-ID lacks a
  corresponding EX block citation in the gate validation, (b) fails. C-40 cannot pass if
  C-38 fails or C-13 fails.
- For C-41 locate each PHASE ENTRY CONTRACT block (C-36 pass condition already required)
  and check for a `Prior phase:` sub-field (or equivalent labeled sub-field). For the
  first phase: the sub-field must carry a sentinel value (NONE, INIT, START, or
  equivalent) -- a blank or omitted sub-field fails; a phase identifier also fails (the
  chain has no prior phase). For all subsequent phases: the sub-field must carry a literal
  string that string-matches the label of the immediately preceding phase block in document
  order. A `Prior phase:` value expressed as a prose description instead of the label
  identifier fails. Check every phase's entry contract independently; omission in any
  phase fails C-41 overall. C-41 cannot pass if C-36 fails.
