Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v5-2026-03-14.md`.

---

**2 new criteria extracted from R4 excellence patterns:**

**C-22 — Evidence Field Format Contract** (depth)
The C-18-to-C-15 analog for C-19. V-01/V-03 fail C-19 because the Evidence hint is vague (`[AT-RISK entries that list "causal source: B-01"...]`) — no format example, no explicit fail condition. V-02/V-04/V-05 pass because they provide a concrete `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"` example plus a preamble fail condition for general references. C-22 requires both. Every C-22 pass implies C-19 pass; C-22 cannot pass if C-19 fails.

**C-23 — Chain Status Section Isolation** (depth)
V-01/V-02/V-04 fail C-20 because CHAIN STATUS is the last line of the `Bidirectional evidence check:` sub-block inside SLA ANALYSIS — still requires navigation. V-03/V-05 pass because they use a dedicated `## CHAIN STATUS` top-level section with `CHAIN STATUS: [CLOSED / OPEN]` as the first element plus an explicit anti-embedding preamble ("Do not embed chain status inside the SLA ANALYSIS section"). Section isolation is to C-20 what ordinal labels are to C-15. Every C-23 pass implies C-20 pass; C-23 cannot pass if C-20 fails.

**Formula**: `/13` → `/15`; aspirational total remains 10 pts.

**Full dependency chain (v5):**
- C-18 → C-15; C-19 → C-16; C-20 → C-14+C-16; C-21 → C-13+C-15+C-17
- **C-22 → C-19**; **C-23 → C-20**
) makes non-compliant
Evidence entries structurally visible. Every C-22 pass implies C-19 pass; V-01 and V-03 in R4
pass C-16 but fail C-19 because the Evidence hint provides no format contract.

**Key distinction between C-20 and C-23**: C-20 requires an explicit CHAIN STATUS declaration
with CLOSED/OPEN status (a content requirement); C-23 requires that declaration to appear as
the first element of a dedicated top-level section, separated from SLA ANALYSIS, with an
anti-embedding instruction. A CHAIN STATUS line embedded inside `Bidirectional evidence check:`
within SLA ANALYSIS satisfies neither: it is not a discrete output element a reader can locate
independently. V-01, V-02, and V-04 in R4 all fail C-20 because their chain status is embedded;
V-03 and V-05 pass both C-20 and C-23 because they isolate the gate into a dedicated
`## CHAIN STATUS` section.

---

## Quick Reference

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

**15 Aspirational (10 pts)**

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

---

## Scoring Formula

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 15 * 10)

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
