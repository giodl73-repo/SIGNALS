Written to `simulations/quest/rubrics/flow-lifecycle-rubric-2026-03-14.md`.

---

**Rubric summary: flow-lifecycle**

**5 Essential (60 pts)**
| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | State Transition Coverage — every state has entry condition + labeled exit(s) | correctness |
| C-02 | Exception Flow Identification — 3+ named exception traces to terminal | coverage |
| C-03 | Role Assignment Accuracy — domain roles match process type (L2O/P2P/close/case) | correctness |
| C-04 | Bottleneck and Gap Identification — 2+ bottlenecks with cause, 1+ MISSING gap | depth |
| C-05 | Terminal State Completeness — all branches reach a declared terminal state | correctness |

**3 Recommended (30 pts)**
| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Parallel Path Modeling — fork/join with labeled synchronization condition | depth |
| C-07 | Edge Case Enumeration — 3+ distinct from exception flows, with correct response | coverage |
| C-08 | Decision Point Explicitness — every branch has labeled condition + owner role | format |

**2 Aspirational (10 pts)**
| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | Cross-Process Interaction Modeling — at least one inter-process handoff contract | depth |
| C-10 | SLA and Timing Analysis — 3+ nodes annotated with SLA vs. typical, at-risk flags | depth |

**Golden threshold**: all 5 essential pass + composite ≥ 80.
olution or terminal. Each must be specific to the
  process being simulated, not generic boilerplate.

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

---

## Scoring Formula

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 3 * 30)
              + (aspirational_pass / 2 * 10)

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
