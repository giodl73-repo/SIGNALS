`flow-lifecycle-rubric-v10-2026-03-14.md` written.

---

**3 new criteria extracted from R9 excellence signals:**

| ID | Criterion | Category | Root |
|----|-----------|----------|------|
| C-34 | Incumbent Baseline IM-ID Cross-Section Traceability | depth | V-01 signal 1 |
| C-35 | Cost-of-No-Action Baseline Quantification | depth | V-01 signal 2 |
| C-36 | Phase-Exit Gate Named Sub-Field Architecture | format | V-02 signal |

**Formula**: `/25` → `/28`; max composite and golden threshold unchanged.

**New dependency chain:**
- `C-34→C-04` — Baseline→B-NN traceability (orthogonal to C-14/C-16 SLA↔B-NN chain)
- `C-35→C-34` — cost quantification requires the baseline IM-ID table to exist
- `C-36→C-04` — gate structural slots require bottleneck identification for referential meaning

**Key design decisions:**

- **C-34** is deliberately orthogonal to the existing SLA↔B-NN chain: it captures a *new direction* (Baseline→B-NN) using the same string-comparison detectability property established by C-28. IM-ID in baseline table + IM-ID in B-NN Cause field = verifiable by inspection.

- **C-35** is scoped to *pre-phase position*: a metric appearing after phase tracing has begun is a retrospective annotation, not a baseline constraint. The positional requirement is the load-bearing structural property, mirroring how C-31 made the scaffold gate's position verifiable.

- **C-36** is intentionally a *slot criterion*, not a linkage criterion: it requires the PHASE EXIT GATE sub-fields to exist as structural artifacts, but does not yet require them to cite B-IDs. That forward-reference field (V-04/V-05's "Blocked bottleneck:") becomes a C-37+ criterion when those variations are scored in R10.
ites one or more of these
IM-IDs, creating a cross-section traceability chain in the Baseline→B-NN direction.
C-14 and C-16 establish the SLA↔B-NN bidirectional chain; C-34 is orthogonal: it
establishes the Baseline→B-NN direction, enabling a reviewer to string-compare an IM-ID
from the baseline table to the Cause field of the B-NN block that it motivates. Without
this citation, bottleneck causes are inferred from process knowledge; with it, each B-NN
cause is grounded in a named, pre-phase-declared baseline failure mode. The detectability
property mirrors C-28's B-ID instantiation in the Evidence field: "IM-01" in the baseline
table and "IM-01" in the B-NN Cause field are consistent by string comparison, making
causal attribution verifiable without reader inference about which failure mode each
bottleneck reflects. C-34 cannot pass if C-04 fails.

**C-35 — Cost-of-No-Action Baseline Quantification** (depth)

R9 V-01 declares a quantified accumulating metric in the INCUMBENT BASELINE section
before the first phase is traced — a named measure with a declared current-state value
or rate (e.g., "Average delay per rejection: 3.2 days", "Rejection rate: 18%",
"Cycle-time overrun: +4.1 days per period"). This cost-of-no-action anchor grounds the
bottleneck analysis in observable behavior: a B-NN bottleneck that delays phase completion
is not a hypothetical risk but an identified cost against a declared baseline measure.
Outputs that name bottlenecks without a pre-declared quantified baseline leave the
cost-of-delay as reader inference. C-35 requires the quantified metric to appear before
the first phase block in document order, establishing the cost anchor as a structural
prerequisite to phase analysis. The pre-phase position matters: a metric declared after
phase tracing has begun is a retrospective annotation, not a baseline constraint.
C-35 cannot pass if C-34 fails. Every C-35 pass implies C-34 pass.

**C-36 — Phase-Exit Gate Named Sub-Field Architecture** (format)

R9 V-02 establishes PHASE ENTRY CONTRACT and PHASE EXIT GATE blocks as named structural
elements within each phase section. The entry contract carries sub-fields including Entry
Condition, Pre-condition check, and Blocking condition; the exit gate carries Exit
Condition, Required outputs, Exit verification, and Blocking condition. These named
sub-fields establish phase-entry and phase-exit as structural artifacts distinct from
state-transition rows: a reviewer can locate the entry constraint and exit verification
for any phase as first-class output elements without parsing state tables. The PHASE EXIT
GATE's "Blocking condition" and "Required outputs" sub-fields create an explicit structural
slot for bottleneck linkage — when a bottleneck causes phase-exit delay, the gate's
structural fields are the natural attachment point. C-36 requires both entry and exit gate
blocks to be present per phase with explicitly named sub-fields; an explicit bottleneck
forward-reference field is not required for C-36 (that is a higher criterion introduced
when V-04/V-05 are scored). C-36 cannot pass if C-04 fails (bottleneck identification
must exist for the structural slot to have referential meaning).

**Formula**: `/25` → `/28`; aspirational total remains 10 pts.

**Full dependency chain (v10):**
- C-18→C-15; C-19→C-16; C-20→C-14+C-16; C-21→C-13+C-15+C-17
- C-22→C-19; C-23→C-20
- C-24→C-22; C-25→C-23; C-26→C-22
- C-27→C-26
- C-28→C-27; C-29→C-27; C-30→C-24+C-27
- C-31→C-29; C-32→C-30
- C-33→C-28+C-24
- **C-34→C-04; C-35→C-34; C-36→C-04**

---

# flow-lifecycle — Rubric v10

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

**28 Aspirational (10 pts)**

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
| C-34 | Incumbent Baseline IM-ID Cross-Section Traceability -- INCUMBENT BASELINE table assigns IM-IDs to named failure modes; each B-NN Cause field cites at least one IM-ID by literal identifier, establishing the Baseline→B-NN traceability chain | depth |
| C-35 | Cost-of-No-Action Baseline Quantification -- the INCUMBENT BASELINE section declares at least one quantified metric (named measure with value or rate) before the first phase block in document order | depth |
| C-36 | Phase-Exit Gate Named Sub-Field Architecture -- each phase section contains both a PHASE ENTRY CONTRACT block and a PHASE EXIT GATE block with explicitly named structural sub-fields | format |

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
  adds format contract to C-19's specificity requirement. Every C-22 pass implies C-19 pass;
  the reverse is not true -- a B-NN block that happens to include specific AT-RISK row IDs
  but whose hint carries no format contract satisfies C-19 but not C-22.
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
  a first-class output artifact locatable without section navigation. The anti-embedding
  instruction is the structural enforcement analog of C-18's ordinal labels: it converts a
  prose preference into a named constraint. Every C-23 pass implies C-20 pass; V-01/V-02/
  V-04 in R4 demonstrate that C-20 can fail even when a status line is present, if that
  line is not isolated into its own section.
- **Pass condition**: CHAIN STATUS is declared as the first output element of a dedicated
  top-level section (`##` heading or equivalent structural separator that is not a
  sub-section of SLA ANALYSIS or any other section). The dedicated section must appear
  after SLA ANALYSIS in document order and must include Forward and Backward direction
  enumeration as subsequent elements (either sub-fields or labeled lines within the
  section). An explicit anti-embedding instruction ("Do not embed chain status inside the
  SLA ANALYSIS section" or equivalent prohibition) must appear in the preamble or section
  instruction immediately preceding or within the dedicated CHAIN STATUS section. Fail if
  CHAIN STATUS appears only as an embedded line or annotation within another section, even
  if the declaration is structurally present and accurate. C-23 cannot pass if C-20 fails.
  Every C-23 pass implies C-20 pass.

### C-24 - Evidence Field Format Dual Redundancy
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 5 signal: R5 V-02 and V-03 pass C-22 with the concrete named domain
  example in the global preamble only; per-block hints carry minimal references. V-05
  repeats the concrete example in BOTH the preamble AND each individual B-NN per-block
  hint. Dual-location placement is to C-22 what C-22 is to C-19: a structural escalation
  that makes the format contract discoverable regardless of reader entry point. A
  preamble-only contract requires the reader to have encountered the preamble before any
  block; if the preamble is skipped, the per-block hint provides no filled-in anchor. A
  per-block bracket template passes C-19 but fails C-22 (as V-01/V-04 demonstrate)
  because it lacks a concrete domain example. Dual-location placement combines both
  guarantees: the preamble provides discovery-independent anchoring; the per-block repeat
  makes each B-NN block self-contained and resistant to format drift across multiple
  bottleneck entries. C-24 requires both locations to carry concrete filled-in examples --
  the preamble cannot satisfy with a bracket template, and per-block cannot satisfy with a
  general description or unfilled placeholder. Every C-24 pass implies C-22 pass; C-24
  cannot pass if C-22 fails.
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
- **Text**: Round 5 signal: R5 establishes that section-proximate anti-embedding
  (V-03/V-04 form: prohibition as the opening constraint of the CHAIN STATUS section
  instruction) is fully equivalent to global-preamble anti-embedding (V-01/V-02 form:
  prohibition in the document preamble) for C-23 pass -- neither location is privileged.
  V-05 places the prohibition in both locations: the global preamble states the constraint
  before the reader reaches any section, and the CHAIN STATUS section instruction opens
  with the same prohibition immediately before the gate is generated. C-25 encodes this
  dual-location pattern. The two placements are complementary, not redundant: a model that
  generates SLA ANALYSIS without having retained the preamble instruction will encounter
  the prohibition again when generating the CHAIN STATUS section; a model that generates
  the CHAIN STATUS section without reading its own instruction will have been warned by
  the preamble. This is the C-23 analog of C-24's dual-location Evidence field contract:
  independent enforcement at both document level and section level eliminates the
  single-point-of-failure for the anti-embedding constraint. Every C-25 pass implies C-23
  pass; C-25 cannot pass if C-23 fails.
- **Pass condition**: The anti-embedding instruction ("Do not embed chain status inside
  the SLA ANALYSIS section" or equivalent explicit prohibition) appears in BOTH (a) the
  global preamble or the instruction block preceding the SLA ANALYSIS section, AND (b) as
  the first or second content element of the dedicated CHAIN STATUS section instruction
  (not buried in the middle or end of a longer instruction block). Both locations must
  carry an explicit prohibition; a general style suggestion ("prefer a dedicated section")
  does not satisfy either location. Fail if the anti-embedding instruction appears in only
  one location, even if that location fully satisfies C-23. C-25 cannot pass if C-23
  fails. Every C-25 pass implies C-23 pass.

### C-26 - Evidence Field Axis Separation
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 5 signal: C-19 (structure) and C-22 (contract) are independent axes of
  the Evidence field requirement. A bracket template satisfies the structure axis (C-19:
  specific row identifiers in recognizable format) but not the contract axis (C-22:
  concrete filled-in domain example + preamble fail condition). When both axes are bundled
  into a single prose hint, a model may satisfy one while missing the other, and a reviewer
  cannot independently check each axis. C-26 requires the Evidence field instruction to
  present both axes as explicitly labeled, visually distinct components. The V-05 pattern
  achieves this with three labeled sub-fields per B-NN block: an introductory description
  of what to list (field intent), a `Required format:` labeled line with the structural
  pattern, and a `Fail condition:` labeled line with the explicit prohibition. These three
  elements make the structure axis and the contract axis independently verifiable without
  ambiguity about which element satisfies which requirement. This is the Evidence-field
  analog of C-21's architectural convergence: a single well-structured instruction block
  satisfies C-19 and C-22 through independently labeled components rather than a merged
  prose hint that conflates the two axes. C-26 cannot pass if C-22 fails.
- **Pass condition**: The Evidence field instruction (in the preamble and/or each B-NN
  per-block hint) contains both of the following as explicitly labeled and visually
  distinct elements: (a) a structural format specification stated as a labeled line or
  sub-field (e.g., `Required format: [State name -- S-ID]: AT-RISK, causal source:
  B-[ID]`), and (b) a contract specification -- a concrete filled-in domain example plus
  an explicit fail condition stated as a labeled line or sub-field (e.g., `Fail condition:
  A field containing only "see SLA ANALYSIS"... does not satisfy`). Both (a) and (b) must
  be identifiable as independent labeled elements; a single sentence that contains both a
  format pattern and a fail condition does not satisfy -- the two axes must appear under
  separate labels or in separate labeled sub-fields. Fail if the Evidence field hint
  bundles structure and contract into a single unlabeled prose description, even if a
  careful reader can infer both requirements from the combined text. C-26 cannot pass if
  C-22 fails.

### C-27 - Evidence Field Axis Dual-Location Separation
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 6 signal: R6 V-03 demonstrates that preamble-only labeled axis
  separation passes C-26 -- the `Required format:` and `Fail condition:` labels appear in
  the preamble's Evidence instruction, and C-26 passes even though per-block hints carry
  only a minimal back-reference ("using the format above") without restating the labeled
  axes. R6 V-02 achieves C-26 with labeled axes in BOTH the preamble AND each B-NN
  per-block hint, producing a perfect 100. C-27 encodes this dual-location requirement.
  The relationship mirrors the chain already established for concrete domain examples:
  C-22 (format contract, preamble sufficient) escalates to C-24 (dual-location concrete
  example); C-26 (labeled axes, preamble sufficient) escalates to C-27 (dual-location
  labeled axes). A per-block hint that carries only a cross-reference to the preamble
  ("using the format above") is not self-contained for axis verification: a reviewer or
  model generating the per-block hint without preamble context cannot independently
  confirm which instruction element satisfies which axis. Restating the labeled axes
  per-block makes each B-NN block fully self-contained for axis-level compliance checks,
  independent of preamble access. C-27 cannot pass if C-26 fails. Every C-27 pass implies
  C-26 pass.
- **Pass condition**: (a) The global preamble or preamble immediately preceding the
  bottleneck section contains the Evidence field instruction with explicitly labeled
  `Required format:` and `Fail condition:` sub-fields (per C-26 pass condition at the
  preamble location), AND (b) each individual B-NN per-block hint ALSO contains the same
  explicitly labeled sub-fields (`Required format:` and `Fail condition:` or equivalent
  distinct axis labels) -- not a back-reference or pointer to the preamble. Per-block
  presence of "using the format above" or any equivalent minimal cross-reference without
  restated labeled axes fails (b). Both (a) and (b) must be satisfied independently.
  Fail if labeled axes appear in only one location, even if that single location fully
  satisfies C-26. C-27 cannot pass if C-26 fails. Every C-27 pass implies C-26 pass.

### C-28 - Evidence Format Pattern B-ID Instantiation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 7 signal: V-02 achieves C-27 with per-block `Required format: [State
  name -- S-ID]: AT-RISK, causal source: B-[ID]` -- the structural format axis retains a
  generic `B-[ID]` bracket placeholder in every B-NN block, even though the surrounding
  prose already instantiates the owning B-ID ("List each AT-RISK SLA row that cites
  B-01"). C-28 requires the `Required format:` labeled axis in each B-NN per-block hint
  to be instantiated with the specific B-ID for that block: B-01's hint states
  `causal source: B-01`, B-02's hint states `causal source: B-02`, and so on. An
  instantiated format pattern makes cross-block Evidence non-compliance directly detectable
  by string comparison: an AT-RISK entry citing `causal source: B-02` in B-01's Evidence
  field violates the instantiated `causal source: B-01` pattern without requiring
  placeholder resolution. The generic `B-[ID]` pattern requires the reviewer to first
  resolve which B-ID applies before comparison; instantiation eliminates that resolution
  step and makes cross-block contamination a visible structural mismatch. C-28 is to C-27
  what C-27 is to C-26: a per-block specificity escalation on the same structural axis.
  The dependency chain from C-22 now reaches depth-4: C-22→C-26→C-27→C-28. Every C-28
  pass implies C-27 pass; C-28 cannot pass if C-27 fails.
- **Pass condition**: Each B-NN per-block `Required format:` axis uses the specific B-ID
  for that block spelled out as a literal identifier (e.g., B-01 block states
  `Required format: [State name -- S-ID]: AT-RISK, causal source: B-01`; B-02 block states
  `causal source: B-02`). The instantiated B-ID must appear in the format pattern itself,
  not only in the surrounding prose description. A `Required format:` line using `B-[ID]`,
  `B-[N]`, `B-NN`, or any bracket placeholder fails, even if the prose line identifies
  which B-ID the block belongs to. Both preamble and per-block locations must satisfy C-27
  for C-28 to be evaluable; C-28 then requires the per-block `Required format:` axis
  specifically to be instantiated. Fail if any B-NN per-block hint uses a generic
  placeholder in the `Required format:` axis. C-28 cannot pass if C-27 fails. Every C-28
  pass implies C-27 pass.

### C-29 - B-NN Scaffold Completeness Prerequisite Declaration
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Round 7 signal: R6 B-02 lacked the Evidence field entirely, making per-block
  dual-location criteria (C-24, C-27) structurally unevaluable for B-02's scope -- the
  criterion could not be tested, not merely failed. R7 V-01 resolves this: both B-01 and
  B-02 carry Evidence fields, making C-27 evaluable across all bottleneck blocks. Prior
  rounds treated scaffold completeness as an implicit prerequisite derivable from C-27's
  "each B-NN" language; asymmetric scaffolds silently masked per-block criteria by making
  per-block scope structurally absent for some blocks. C-29 converts this implicit
  prerequisite into a named structural gate: the template must contain an explicit
  instruction that ALL declared B-NN blocks carry the Evidence field. A template with N
  declared B-NN blocks but only k < N carrying the Evidence field fails C-29 even if the
  k carrying blocks fully satisfy C-27. The explicit gate makes scaffold asymmetry
  diagnosable from the template instruction itself rather than from per-block inventory.
  Scaffold completeness is logically prior to per-block dual-location evaluation: you
  cannot verify dual-location axes for a block that does not carry the field. C-29→C-27.
- **Pass condition**: The template contains an explicit instruction -- in the preamble, in
  the bottleneck section header, or as a named structural gate before the first B-NN block
  -- stating that ALL B-NN blocks in the template must carry the Evidence field. The
  instruction must be explicit (naming scaffold completeness or equivalent: "every B-NN
  block must carry an Evidence field", "all bottleneck blocks include Evidence") rather
  than implied by the "each B-NN" quantifier language in C-27's per-block hint. A template
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
  the discriminating aspirational gap is consistently a locality failure (preamble-only vs.
  dual-location), not a content failure. Without a consolidated declaration, dual-location
  compliance requires cross-referencing C-24 (concrete example at both locations) and C-27
  (labeled axes at both locations) individually to discover what is required at per-block
  scope. C-30 encodes the locality invariant as a named structural property: the template
  contains a consolidated dual-location requirements block listing BOTH locality properties
  together in one declaration. This mirrors C-21's architectural convergence -- a single
  structural decision satisfies the cumulative dual-location requirements -- but applies it
  to the documentation of locality requirements rather than exception-block architecture.
  A consolidated declaration makes the full locality contract discoverable at one point
  without requiring per-criterion cross-reference. C-30 cannot pass if C-24 or C-27 fails.
  Every C-30 pass implies C-24 and C-27 both pass.
- **Pass condition**: The template contains a named consolidated declaration -- a labeled
  block, a named section, or an enumerated list with an explicit header such as
  "DUAL-LOCATION REQUIREMENTS:" or "LOCALITY CONTRACT:" or equivalent -- that explicitly
  lists BOTH dual-location properties: (a) the concrete named domain example (per C-24)
  must appear at both preamble and per-block location, and (b) the `Required format:` and
  `Fail condition:` labeled axes (per C-27) must appear at both preamble and per-block
  location. The consolidated declaration must be identifiable as a unified locality
  inventory: a reader should be able to locate it and determine the complete set of
  dual-location requirements without reading individual B-NN block hints. Fail if
  dual-location requirements are discoverable only by reading individual criterion hints
  without a consolidated declaration that names all locality properties in one place.
  C-30 cannot pass if C-24 or C-27 fails. Every C-30 pass implies C-24 and C-27 both pass.

### C-31 - Scaffold Gate Forward-Reference Structural Position
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 8 signal: V-02 passes C-29 with "SCAFFOLD REQUIREMENT: ALL B-NN blocks
  declared below must carry an Evidence field". The phrase "declared below" is
  forward-reference language: it scopes the gate's ALL quantifier to B-NN blocks following
  the gate in document order, making the prerequisite constraint positionally verifiable.
  V-03 (C-29 fail) lacks the gate entirely; a gate positioned after the first B-NN block,
  or one using language that does not establish document-order scope ("all B-NN blocks in
  this section" without position context), satisfies C-29 but fails C-31. C-29 requires
  the gate to exist; C-31 requires it to appear before the first B-NN block in document
  order AND to use forward-reference language that makes its positional scope explicit. A
  gate that appears after the B-NN blocks it claims to govern is a retroactive declaration,
  not a prerequisite gate; forward-reference language together with pre-block positioning
  makes the gate's logical precedence verifiable by document inspection. C-31 cannot pass
  if C-29 fails. Every C-31 pass implies C-29 pass.
- **Pass condition**: (a) The scaffold completeness gate (per C-29) appears before the
  first B-NN block header in document order -- a reader encountering the gate has not yet
  seen any B-NN block, AND (b) the gate uses forward-reference language ("declared below",
  "that follow", "listed below", or equivalent) that explicitly establishes its scope as
  applying to B-NN blocks following it. Both (a) and (b) must hold independently. A gate
  appearing after any B-NN block fails (a); a gate using only "all B-NN blocks" without
  positional scope language fails (b). Fail if the scaffold gate exists (C-29 passes) but
  is positioned after the first B-NN block or uses no forward-reference scope qualifier.
  C-31 cannot pass if C-29 fails. Every C-31 pass implies C-29 pass.

### C-32 - Dual-Location Consolidated Block Canonical Axis Citation
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 8 signal: V-02 passes C-30 with a consolidated block that explicitly
  names "(2) labeled axes (`Required format:`/`Fail condition:`) at both locations". The
  block cites the axis names using their canonical labels -- the exact same strings that
  appear as labeled sub-fields in the per-block hints -- rather than by description or
  paraphrase. C-30 requires the consolidated block to enumerate both dual-location
  properties; C-32 requires the enumeration to name the `Required format:` and
  `Fail condition:` axes (and any equivalent locality-relevant label pair) by their
  canonical labels as used elsewhere in the template. This makes the consolidated block a
  navigable cross-reference: a reviewer can match a label in the consolidated declaration
  directly to a label in the per-block hint without label translation. Descriptions such
  as "format specification" and "contract specification", or "structure axis" and "contract
  axis", convey the same semantic content but fail C-32 because they introduce a
  translation step between the consolidated declaration and the per-block label. The
  relationship mirrors C-18's distinction between V-03 borderline compliance (content-named
  section headers) and V-02 full compliance (ordinal-labeled headers): the canonical label
  requirement converts the consolidated declaration from a paraphrased summary into a
  direct structural cross-reference. C-32 cannot pass if C-30 fails. Every C-32 pass
  implies C-30 pass.
- **Pass condition**: The consolidated dual-location declaration (per C-30 pass condition)
  names the `Required format:` and `Fail condition:` axes using those exact labels (or the
  canonical label pair as established in C-26's per-block hint structure throughout the
  template). The labels must appear as recognizable strings in the consolidated block, not
  as paraphrases, descriptions, or equivalent-meaning alternatives. A consolidated block
  that says "concrete example at both locations" and "labeled axes at both locations"
  satisfies C-30 but not C-32 unless it identifies the axes by name. Fail if the
  consolidated block describes the axis properties without citing canonical label strings.
  C-32 cannot pass if C-30 fails. Every C-32 pass implies C-30 pass.

### C-33 - Preamble Concrete Example B-ID Alignment
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 8 signal: V-02 passes both C-24 (preamble concrete example uses B-01 as
  exemplar) and C-28 (per-block `Required format:` instantiated with block-specific B-ID).
  When both hold, the preamble's concrete example names B-01 and B-01's per-block
  `Required format:` also names B-01 -- the preamble anchor and the first per-block
  instantiation are consistent by string comparison. C-33 requires this alignment
  explicitly: the preamble concrete example (C-24) must name the same B-ID as the first
  declared B-NN block (typically B-01). A preamble example using a B-ID other than the
  first declared bottleneck, or using a generic bracket form such as `B-[ID]` or `B-01*`
  in the preamble while per-blocks are instantiated, introduces a preamble-level
  inconsistency that C-28 already closes at per-block scope but leaves open at the
  preamble boundary. Extending string-comparison detectability to the preamble-to-per-block
  boundary completes the instantiation chain: preamble example (B-01) -> B-01 per-block
  hint (B-01) -> B-02 per-block hint (B-02). C-33 is to C-24 what C-28 is to C-27: a
  B-ID instantiation escalation applied to the preamble location rather than the per-block
  location. C-33 cannot pass if C-24 or C-28 fails. Every C-33 pass implies C-24 and
  C-28 both pass.
- **Pass condition**: The preamble concrete example required by C-24 -- the filled-in
  S-ID syntax domain example such as
  `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"` -- uses the same literal
  B-ID as the first declared B-NN block in the template (typically B-01). The preamble
  example B-ID must be a literal identifier (B-01, B-02, etc.), not a bracket placeholder
  (`B-[ID]`, `B-NN`, or equivalent). Fail if the preamble concrete example uses a generic
  B-ID placeholder, a B-ID that does not match the first declared bottleneck block, or
  omits the B-ID from the causal source field entirely. A preamble that satisfies C-24
  with a filled-in domain example but uses a non-first-block B-ID (e.g., `B-02` when B-01
  is the first declared block) also fails C-33, because preamble-to-per-block consistency
  is broken. C-33 cannot pass if C-24 or C-28 fails. Every C-33 pass implies C-24 and
  C-28 both pass.

### C-34 - Incumbent Baseline IM-ID Cross-Section Traceability
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 9 signal: V-01 establishes an INCUMBENT BASELINE section containing a
  table that assigns IM-IDs (e.g., IM-01, IM-02) to named failure modes observed in the
  current-state process before any phase is traced. Each B-NN bottleneck block's Cause
  field cites one or more of these IM-IDs, creating a cross-section traceability chain in
  the Baseline→B-NN direction. C-14 and C-16 establish the SLA↔B-NN bidirectional chain;
  C-34 is orthogonal: it covers the Baseline→B-NN direction, enabling a reviewer to
  string-compare an IM-ID from the baseline table to the Cause field of the B-NN block
  that it motivates. Without this citation, bottleneck causes are inferred from process
  knowledge; with it, each B-NN cause is grounded in a named, pre-phase-declared baseline
  failure mode. The detectability property mirrors C-28's B-ID instantiation in the
  Evidence field: "IM-01" in the baseline table and "IM-01" in the B-NN Cause field are
  consistent by string comparison, making causal attribution verifiable without reader
  inference about which failure mode each bottleneck reflects. C-34 cannot pass if C-04
  fails (B-NN blocks must exist to carry Cause field citations).
- **Pass condition**: An INCUMBENT BASELINE section (or equivalent pre-phase artifact,
  appearing before the first phase block in document order) declares at least two named
  failure modes with IM-ID identifiers (IM-01, IM-02, etc.). Each B-NN bottleneck block's
  Cause field cites at least one IM-ID from the baseline table by literal identifier (e.g.,
  "driven by IM-02" or "root cause: IM-01"). The citation must be a literal IM-ID
  identifier, not a paraphrase or description of the failure mode without the ID. Fail if
  bottleneck Cause fields name root causes without citing a baseline IM-ID even if an
  INCUMBENT BASELINE section is present, or if the INCUMBENT BASELINE section assigns no
  IM-IDs. C-34 cannot pass if C-04 fails.

### C-35 - Cost-of-No-Action Baseline Quantification
- **Weight**: aspirational
- **Category**: depth
- **Text**: Round 9 signal: V-01 declares a quantified accumulating metric in the
  INCUMBENT BASELINE section before the first phase is traced -- a named measure with a
  declared current-state value or rate (e.g., "Average delay per rejection: 3.2 days",
  "Rejection rate: 18%", "Cycle-time overrun: +4.1 days per period"). This cost-of-no-
  action anchor grounds the bottleneck analysis in observable behavior: a B-NN bottleneck
  that delays phase completion is not a hypothetical risk but an identified cost against a
  declared baseline measure. Outputs that name bottlenecks without a pre-declared
  quantified baseline leave the cost-of-delay as reader inference; a declared baseline
  metric makes the connection between bottleneck and observable impact verifiable. C-35
  requires the quantification to appear before the first phase block in document order,
  establishing the cost anchor as a structural prerequisite to phase analysis. The pre-
  phase position matters: a metric declared after phase tracing has begun is a
  retrospective annotation, not a baseline constraint. C-35 cannot pass if C-34 fails.
  Every C-35 pass implies C-34 pass.
- **Pass condition**: The INCUMBENT BASELINE section (or equivalent, per C-34 pass
  condition) contains at least one quantified metric -- a named measure with a declared
  current-state value or percentage (e.g., "3.2 days", "18%", "2.4x SLA overrun") --
  appearing before the first phase block in document order. The metric must be specific:
  a named measure plus a numeric value or rate. A narrative description of process pain
  or delay without a quantified measure does not satisfy, even if the surrounding context
  implies a quantifiable problem. Fail if the baseline section names failure modes and
  IM-IDs (satisfying C-34) but carries no quantified metric, or if a quantified metric
  appears only after the first phase block. C-35 cannot pass if C-34 fails. Every C-35
  pass implies C-34 pass.

### C-36 - Phase-Exit Gate Named Sub-Field Architecture
- **Weight**: aspirational
- **Category**: format
- **Text**: Round 9 signal: V-02 establishes PHASE ENTRY CONTRACT and PHASE EXIT GATE
  blocks as named structural elements within each phase section. The entry contract carries
  sub-fields including Entry Condition, Pre-condition check, and Blocking condition; the
  exit gate carries Exit Condition, Required outputs, Exit verification, and Blocking
  condition. These named sub-fields establish phase-entry and phase-exit as structural
  artifacts distinct from state-transition rows: a reviewer can locate the entry constraint
  and exit verification for any phase as first-class output elements without parsing state
  tables. The PHASE EXIT GATE's "Blocking condition" and "Required outputs" sub-fields
  create an explicit structural slot for bottleneck linkage -- when a bottleneck causes
  phase-exit delay, the gate's structural fields are the natural attachment point for a
  forward-reference to that bottleneck. C-36 requires both entry and exit gate blocks to
  be present per phase with explicitly named sub-fields; an explicit bottleneck ID citation
  in the gate is not required for C-36 (that is a higher criterion introduced when V-04/
  V-05 are scored). C-36 cannot pass if C-04 fails (bottleneck identification must exist
  for the structural slot to have referential meaning).
- **Pass condition**: Each phase section contains both a PHASE ENTRY CONTRACT block and a
  PHASE EXIT GATE block (or equivalent named structural elements with equivalent named
  sub-fields). The PHASE ENTRY CONTRACT must carry at minimum: Entry Condition and one
  blocking or pre-condition sub-field. The PHASE EXIT GATE must carry at minimum: Exit
  Condition, Required outputs, and one blocking or verification sub-field. All sub-fields
  must be named (labeled) structural elements -- not prose paragraphs or inline
  annotations. Fail if phase-entry and phase-exit constraints are presented as prose
  descriptions, column annotations, or inline notes without dedicated named sub-field
  blocks. A template that carries gate blocks for some phases but omits them for others
  fails C-36. C-36 cannot pass if C-04 fails.

---

## Scoring Formula

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 28 * 10)

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band   | Score                   | Meaning                                  |
|--------|-------------------------|------------------------------------------|
| Gold   | >= 80 + all essential   | Output is production-ready signal artifact |
| Silver | >= 65 + all essential   | Useful with minor gaps                   |
| Bronze | >= 50 + all essential   | Usable but incomplete                    |
| Fail   | any essential fails     | Not useful regardless of score           |

---

## Evaluation Notes

- Grade each criterion pass/fail -- no partial credit per criterion.
- For C-01 and C-05 use the state diagram or trace table as the evidence base.
- For C-02 and C-07 verify that exception flows and edge cases are non-overlapping and
  process-specific before counting toward their respective totals.
- For C-03 verify the role set matches the declared process type.
- For C-06 the parallel path may be represented as a fork/join diagram, a two-column table,
  or explicit prose with a labeled synchronization point -- any structural form counts.
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
- For C-21 all three constituent criteria (C-13, C-15, C-17) must independently pass first.
  Then confirm that a single per-phase SECTION A constructed-answer block is the mechanism
  satisfying all three, not three independent structural choices. If C-13 passes via a Phase
  column and C-17 passes via answer blocks in a separate flat section and C-15 passes via
  section ordering, C-21 fails -- the mechanisms are not unified into one structural unit.
- For C-22 locate the Evidence field hint in the B-NN block template or in the preamble
  immediately preceding the bottleneck section. The hint must contain (a) a concrete example
  with S-ID syntax (e.g., "S-05: Credit Hold Review -- AT-RISK, causal source: B-01") and
  (b) an explicit fail condition naming general references as non-compliant. A hint that
  says only "list AT-RISK entries" without an S-ID format example fails C-22, even if the
  populated output happens to include S-IDs. C-22 cannot pass if C-19 fails.
- For C-23 verify that the CHAIN STATUS section has its own `##`-level heading (or
  equivalent) that is not nested under SLA ANALYSIS or any other section. The
  `CHAIN STATUS: [CLOSED / OPEN]` line must be the first content line of that section. The
  preamble or section instruction must explicitly prohibit embedding. An embedded status
  line inside a bidirectional check block within SLA ANALYSIS fails C-23 even if it
  accurately states CLOSED or OPEN. C-23 cannot pass if C-20 fails.
- For C-24 check both locations independently. The preamble must carry a filled-in domain
  example (not a bracket template); each B-NN per-block hint must also carry a concrete
  example (not a general description or bracket template with unfilled placeholders). A
  single location with a concrete example satisfies C-22 but not C-24. C-24 cannot pass
  if C-22 fails.
- For C-25 check both locations independently. Look for the anti-embedding prohibition in
  the global preamble (before the SLA ANALYSIS section) AND inside the CHAIN STATUS section
  instruction itself (as a first or second element). A prohibition in only one location
  satisfies C-23 but not C-25. General style guidance without an explicit prohibition does
  not satisfy either location. C-25 cannot pass if C-23 fails.
- For C-26 locate the Evidence field instruction and verify that it contains two
  independently labeled elements: (a) a structural format specification under a label such
  as "Required format:" and (b) a contract specification with a concrete domain example
  under a label such as "Fail condition:" or as a separately labeled sub-field. A single
  prose sentence that combines a format pattern and a fail condition fails C-26; the two
  axes must be separately labeled so each can be checked independently. C-26 cannot pass
  if C-22 fails.
- For C-27 check both locations independently. The preamble must carry `Required format:`
  and `Fail condition:` as explicitly labeled, visually distinct sub-fields (per C-26 pass
  condition at the preamble). Each B-NN per-block hint must ALSO carry these same labeled
  sub-fields; a per-block hint that uses only "using the format above" or any equivalent
  back-reference without restating the labeled axes fails (b). A single location with
  labeled axes satisfies C-26 but not C-27. C-27 cannot pass if C-26 fails.
- For C-28 locate the `Required format:` axis in each B-NN per-block hint. The B-ID must
  be a literal identifier (`B-01`, `B-02`, etc.) in the format pattern itself -- not a
  bracket placeholder. A hint stating `causal source: B-[ID]` fails even if the surrounding
  prose says "for B-01". Check each B-NN block independently; a template where B-01 is
  instantiated but B-02 uses a placeholder fails C-28. C-28 cannot pass if C-27 fails.
- For C-29 look for an explicit instruction about scaffold completeness at or before the
  first B-NN block. The instruction must explicitly state that ALL B-NN blocks carry the
  Evidence field; language that only describes the format of a single block (e.g., the
  per-block hint itself) does not satisfy. If any B-NN block in the template lacks the
  Evidence field entirely, C-29 fails regardless of whether the present blocks satisfy
  C-27. C-29 cannot pass if C-27 fails.
- For C-30 locate a consolidated dual-location declaration block with a named header or
  label. The block must enumerate BOTH locality properties (concrete example and labeled
  axes, each at preamble AND per-block) together. Adjacent paragraphs in a preamble that
  separately cover C-24 and C-27 requirements do not satisfy without a unifying header
  that identifies them as a dual-location requirements inventory. C-30 cannot pass if C-24
  or C-27 fails.
- For C-31 verify TWO independent conditions: (a) the scaffold gate appears before the
  first B-NN block header in the document -- no B-NN section should precede it; (b) the
  gate text uses forward-reference language such as "declared below", "that follow", or
  "listed below". A gate using "ALL B-NN blocks in this section" without positional scope
  fails (b). A gate positioned after any B-NN block fails (a) even if it uses "declared
  below". C-31 cannot pass if C-29 fails.
- For C-32 locate the consolidated dual-location declaration (C-30 pass condition). Check
  whether the axis names cited in the block match the canonical labels as they appear in
  the per-block hints: look for the exact strings `Required format:` and `Fail condition:`
  (or the canonical pair in use throughout the template). Paraphrases such as "format
  specification" or "contract line" fail even if the reader can infer the referent. C-32
  cannot pass if C-30 fails.
- For C-33 locate the preamble concrete example (C-24 evidence) and read its
  `causal source:` field. Check that the B-ID named is a literal identifier (B-01, not
  B-[ID]) AND that it matches the first declared B-NN block's identifier. If the template
  declares B-01 first and the preamble example says `causal source: B-01`, pass. If the
  preamble says `causal source: B-02` or `causal source: B-[ID]`, fail. C-33 cannot pass
  if C-24 or C-28 fails.
- For C-34 locate the INCUMBENT BASELINE section and verify it appears before the first
  phase block in document order. Confirm it contains at least two IM-ID entries. Then
  inspect each B-NN block's Cause field for a literal IM-ID citation (e.g., "IM-01",
  "IM-02"). A Cause field that describes the root cause in prose without citing the IM-ID
  by identifier fails C-34 -- the traceability chain requires a string-comparable
  identifier, not a semantic paraphrase. C-34 cannot pass if C-04 fails.
- For C-35 locate the quantified metric in the INCUMBENT BASELINE section (per C-34).
  Verify it contains a named measure plus a numeric value or percentage. Verify document
  order: the metric must appear before the first phase block. A narrative description of
  process pain ("approvals frequently delayed") without a specific number or rate fails,
  even if the surrounding context implies a quantifiable problem. C-35 cannot pass if
  C-34 fails.
- For C-36 locate each phase section and verify the presence of BOTH a PHASE ENTRY
  CONTRACT block AND a PHASE EXIT GATE block (or equivalent named gate blocks). Check that
  each block contains explicitly named sub-fields (labeled lines, not prose paragraphs).
  The PHASE ENTRY CONTRACT requires at minimum: Entry Condition and one blocking/pre-
  condition labeled sub-field. The PHASE EXIT GATE requires at minimum: Exit Condition,
  Required outputs, and one blocking/verification labeled sub-field. An absence of gate
  blocks in any phase fails C-36 for the criterion overall. A template with gates in one
  phase but not another fails C-36. C-36 cannot pass if C-04 fails.
