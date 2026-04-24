Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v3-2026-03-14.md`.

---

**Changes in v3**

**3 new aspirational criteria** extracted from Round 2 excellence signals:

| ID | Criterion | Signal source |
|----|-----------|---------------|
| C-15 | Exception-First Structural Position | V-01 R2 note: column annotation is "lowest structural reliability" — V-03 places exception section structurally before state table in each phase, forcing phase-scoped generation by construction |
| C-16 | Bidirectional SLA-Bottleneck Cross-Reference | V-01/V-02/V-03 all one-directional only (SLA->B); B-NN entries must also cite the SLA node(s) they affect to close the chain in both directions |
| C-17 | Constructed-Answer Format for Exception Sections | V-02 wildcard: question/constructed-answer is the only R2 variation predicted to improve C-02/C-07 content quality via synthesis over cell-fill |

**Scoring formula updated**: aspirational denominator `/6` → `/9`; aspirational total remains 10 pts.

**Key distinction between C-13 and C-15**: C-13 requires phase *labeling* (column, sub-field, or grouping); C-15 requires phase *ordering* — exceptions must precede their phase's state table as a first-class output element. Every C-15 pass implies C-13 pass; the reverse is not true.

**C-16 dependency**: the evaluation note specifies C-16 cannot pass if C-14 fails — the bidirectional chain requires the forward direction (SLA->B) to already exist.
+ at least one labeled exit | correctness |
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

**9 Aspirational (10 pts)**

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

---

## Scoring Formula

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 9 * 10)

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
