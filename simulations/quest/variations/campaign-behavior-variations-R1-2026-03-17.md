---

## campaign-behavior — Quest Variations R1

5 variations written to `simulations/quest/variations/campaign-behavior-variations-R1-2026-03-17.md`.

### Axis map

| Variation | Single/Combo | Axis | Hypothesis |
|-----------|-------------|------|------------|
| **V-01** | single | Role sequence: trace-first | Establishing structural contracts before behavioral simulation surfaces deeper violations |
| **V-02** | single | Output format: table-dominant | Tabular output forces machine-checkable attribution and blast radius ranking |
| **V-03** | single | Phrasing register: imperative | Command-style phrasing reduces hedging, produces more concrete findings |
| **V-04** | combo | V-01 + V-02 (trace-first + table) | Structural sequencing + table format maximizes finding depth and verifiability |
| **V-05** | combo | Explicit phase gates + imperative + blast radius defined upfront | Precise blast radius anchor + per-phase ENTER/EXIT gates prevents skipping and sharpens ranking |

### What distinguishes each

- **V-01**: Flow-lifecycle and flow-conversation run *after* all trace sub-skills — contracts are pinned before behavior is simulated, so lifecycle gaps get checked against a defined boundary baseline.
- **V-02**: Every sub-skill produces a table; consolidated output is a ranked table. Attribution is structural, not incidental.
- **V-03**: No descriptive scaffolding. Pure imperative. "Flag. Label. Fix." — LLM has no narrative to hide behind.
- **V-04**: V-03's imperative energy applied to V-01+V-02's structure. Most constrained variation — tests whether over-constraining the format kills finding quality.
- **V-05**: Blast radius definition is explicit and placed *before* any sub-skill runs, so the model has the ranking criterion in context while generating findings. Phase gates (ENTER/EXIT CRITERIA) prevent incomplete execution.

**Next step:** Run these against a test topic with `/quest:score` to rank against the rubric.
n as: [component-A → component-B] expected
   {X} got {Y}.

2. trace-permissions — Walk through every RBAC path relevant to {{topic}}.
   For each role, list what actions are permitted, what is denied, and flag any
   privilege escalation path (a lower-privilege role reaching a higher-privilege
   outcome through indirect means).

3. trace-state — Hand-compile the state machine. For each state: list the valid
   preconditions, the transition trigger, and the expected postcondition. Flag any
   state that has no defined exit path (dead state) or a transition with no precondition
   guard (unguarded transition).

4. flow-lifecycle — Simulate the full business document lifecycle for {{topic}}.
   Walk each phase in sequence: creation, in-progress transitions, terminal states,
   and exception paths. Note any phase with an undefined entry condition or missing
   exception handler.

5. flow-conversation — Walk the multi-turn agent conversation graph for {{topic}}.
   Identify dead ends (a topic path with no exit), infinite loops (a path that revisits
   the same state without progress), and missing handoff definitions.

**After all five sub-skills complete:**

Synthesize findings into a single consolidated report. Do not concatenate five separate
outputs. Cross-reference findings that appear in multiple sub-skills — these are systemic
issues with higher blast radius than isolated findings.

**Findings report structure:**
- Executive summary (2-3 sentences: what did the campaign find overall?)
- Ranked findings list (blast radius order, highest first)
  - Each finding: [sub-skill source] | finding description | blast radius rationale |
    remediation direction
- Spec gaps: conditions the simulation exposed that the spec does not address
  (or "none found")
- Contract violations: component boundary mismatches (or "none found")
- Implementation readiness verdict: go / conditional-go / no-go with one-sentence
  rationale citing the highest-blast-radius finding or its absence

Blast radius = how broadly a failure propagates. A finding that corrupts shared state
has higher blast radius than one that breaks a single isolated path.
```

---

## V-02 — Single axis: Output format (table-dominant)

**Hypothesis:** Requiring tabular output for both per-sub-skill findings and the
ranked consolidation forces source attribution and blast radius ranking to be
machine-checkable rather than buried in prose.

```
You are running the campaign-behavior simulation for: {{topic}}

Run all five sub-skills in sequence. Produce structured table output at each stage.
Do not skip any sub-skill. Mark "none" explicitly if a sub-skill produces no findings.

**Execution order:**
1. flow-lifecycle
2. flow-conversation
3. trace-state
4. trace-contract
5. trace-permissions

**Per-sub-skill output format** (repeat for each of the five):

### [Sub-skill name] findings

| ID | Finding | Blast radius | Severity | Spec gap? | Contract violation? |
|----|---------|--------------|----------|-----------|---------------------|
| FL-01 | ... | wide/narrow/isolated | high/med/low | yes/no | yes/no |

If no findings: one row with "no findings detected" in the Finding column.

---

**After all five sub-skills, produce the consolidated report:**

### Campaign Summary

| Metric | Value |
|--------|-------|
| Sub-skills run | 5 of 5 |
| Total findings | N |
| Spec gaps | N |
| Contract violations | N |
| Cross-skill findings | N |
| Readiness verdict | go / conditional-go / no-go |

### Ranked Findings (by blast radius, highest first)

| Rank | ID | Sub-skill | Finding | Blast radius | Severity | Remediation |
|------|----|-----------|---------|--------------|----------|-------------|
| 1 | ... | ... | ... | wide | high | ... |
| 2 | ... | ... | ... | ... | ... | ... |

**Blast radius definition:** How broadly a failure propagates. A finding that corrupts
shared state or breaks a contract consumed by multiple callers ranks higher than a
finding contained to a single code path.

### Spec Gaps

List every spec gap found, or write: "No spec gaps detected."
A spec gap is a condition, state transition, or contract term exposed by simulation
that the spec does not address.

### Contract Violations

List every contract violation found, or write: "No contract violations detected."
A contract violation is a mismatch between what one component promises and what
another component expects.

### Cross-skill Findings

List any finding flagged by two or more sub-skills, or write: "No cross-skill patterns."
These are systemic issues — label them explicitly.

### Implementation Readiness Verdict

**Verdict:** [go / conditional-go / no-go]
**Rationale:** [one sentence citing the highest-blast-radius finding or its absence]
```

---

## V-03 — Single axis: Phrasing register (imperative/direct)

**Hypothesis:** Imperative, command-style phrasing with no descriptive scaffolding
reduces LLM hedging and produces more concrete, specific findings rather than
general observations about what might happen.

```
Run campaign-behavior for: {{topic}}

Five sub-skills. Run them in order. Find real problems. Report what you find.

---

STEP 1 — flow-lifecycle

Simulate the complete lifecycle of {{topic}}.
Walk: creation → active states → terminal states → exception paths.
For each phase transition: state the entry condition and exit condition.
Flag: any transition with no defined trigger, any exception with no handler,
any terminal state that is reachable without passing through required intermediate states.

---

STEP 2 — flow-conversation

Walk the full conversation graph for {{topic}}.
For each node in the graph: list outbound paths.
Flag: dead ends (no exit), loops (same node visited twice without progress),
missing handoffs (agent passes control but destination is not defined).

---

STEP 3 — trace-state

Hand-compile the state machine for {{topic}}.
For each state: list preconditions, trigger, postcondition, invariants.
Flag: unguarded transitions (trigger with no precondition check),
dead states (valid entry, no valid exit), invariant violations
(postcondition contradicts a system-wide invariant).

---

STEP 4 — trace-contract

At every component boundary relevant to {{topic}}:
State what the producer promises. State what the consumer expects.
Flag any mismatch: type, cardinality, nullability, timing, ordering.
Label each mismatch with the components involved.

---

STEP 5 — trace-permissions

Walk every RBAC role that touches {{topic}}.
For each role: list what it can do, what it cannot do.
Flag: privilege escalation paths (indirect route to a permission the role does not hold),
missing deny rules (a sensitive action with no explicit deny for low-privilege roles),
over-broad grants (a permission scope wider than the role requires).

---

SYNTHESIZE

One report. Not five.

Rank every finding by blast radius. Blast radius = how many components or users break
if this finding is a real defect. Wide blast radius first.

For each finding:
- Source sub-skill
- What breaks
- Why the blast radius is wide or narrow
- What to fix

Then:
- Spec gaps section: what the simulation exposed that the spec does not cover.
  Write "none" if clean.
- Contract violations section: mismatches between component promises.
  Write "none" if clean.
- Verdict: go / conditional-go / no-go. One sentence. Name the finding that drove it
  or name its absence.
```

---

## V-04 — Combination: Role sequence (trace-first) + Output format (table-dominant)

**Hypothesis:** Combining structural-first sequencing with mandatory tabular output
maximizes both finding depth (contracts established before behavior simulated) and
output verifiability (table format enforces attribution and ranking).

```
You are running the campaign-behavior simulation for: {{topic}}

Run five sub-skills in the sequence below. This order is intentional: structural
contracts are verified before behavioral flows are walked, so lifecycle and conversation
simulations have a defined contract baseline to check against.

**Execution sequence:**
1. trace-contract
2. trace-permissions
3. trace-state
4. flow-lifecycle
5. flow-conversation

Use structured table output throughout. All five sub-skills must appear.
Mark "none" explicitly when a sub-skill finds no issues.

---

### 1. trace-contract

Compare expected vs actual at every component boundary for {{topic}}.

| ID | Producer | Consumer | Expected | Actual | Mismatch type | Severity |
|----|----------|----------|----------|--------|---------------|----------|

If clean: one row "no contract violations detected".

---

### 2. trace-permissions

Walk every RBAC role for {{topic}}.

| ID | Role | Permitted actions | Denied actions | Escalation path? | Flag |
|----|------|-------------------|----------------|------------------|------|

If clean: one row "no permission issues detected".

---

### 3. trace-state

Hand-compile the state machine for {{topic}}.

| State | Preconditions | Trigger | Postcondition | Flag |
|-------|---------------|---------|---------------|------|

Flags: UNGUARDED (no precondition), DEAD (no exit), INVARIANT-VIOLATION.
If clean: one row "no state issues detected".

---

### 4. flow-lifecycle

Simulate the full business lifecycle for {{topic}}.

| Phase | Entry condition | Exit condition | Exception handler | Flag |
|-------|----------------|----------------|-------------------|------|

Flags: NO-ENTRY, NO-EXIT, NO-HANDLER.
If clean: one row "no lifecycle issues detected".

---

### 5. flow-conversation

Walk the agent conversation graph for {{topic}}.

| Node | Outbound paths | Dead end? | Loop? | Missing handoff? | Flag |
|------|---------------|-----------|-------|------------------|------|

If clean: one row "no conversation issues detected".

---

### Campaign Summary

| Metric | Value |
|--------|-------|
| Sub-skills run | 5 of 5 |
| Total findings | N |
| Spec gaps | N |
| Contract violations | N |
| Cross-skill findings | N |

### Ranked Findings (blast radius order)

Blast radius = how broadly a failure propagates across components and users.
Wide blast radius = failure corrupts shared state or breaks a contract consumed by
multiple callers. Narrow blast radius = failure contained to one code path.

| Rank | ID | Sub-skill | Finding | Blast radius | Severity | Remediation |
|------|----|-----------|---------|--------------|----------|-------------|

### Spec Gaps

Conditions the simulation exposed that the spec does not address.
Write "none detected" if clean.

### Contract Violations

Mismatches between component promises. Write "none detected" if clean.

### Cross-skill Findings

Findings that appeared in two or more sub-skills. Label as SYSTEMIC.
Write "none" if no overlap.

### Implementation Readiness Verdict

**Verdict:** go / conditional-go / no-go
**Rationale:** [one sentence — cite the highest-blast-radius finding or state none found]
```

---

## V-05 — Combination: Explicit phase gates + Imperative register + Blast radius defined upfront

**Hypothesis:** Defining blast radius precisely before any sub-skill runs, combined
with explicit ENTER/EXIT gates per phase and imperative commands, produces findings
that are both more specific (clear definition to anchor against) and more complete
(gates prevent skipping work mid-campaign).

```
Run campaign-behavior for: {{topic}}

BLAST RADIUS DEFINITION — read before running any sub-skill:
Blast radius measures propagation scope. A finding has WIDE blast radius if a defect
in it would corrupt shared state, break a contract consumed by N>1 callers, or cause
cascading failure across unrelated user paths. It has NARROW blast radius if the defect
is contained to one code path and has no external dependencies. Rank ALL findings
by this definition. Do not substitute severity, priority, or frequency.

---

PHASE 1 — ENTER: flow-lifecycle

Walk the full business document lifecycle for {{topic}} from creation to all terminal
states. Include every exception path.

For each phase transition state: entry condition, exit condition, exception handler.
Flag: missing entry conditions, missing exit conditions, missing exception handlers,
unreachable terminal states.

EXIT CRITERIA: Every phase transition accounted for. Every exception path either
handled or flagged. Record findings or write "no findings — phase 1 clean".

---

PHASE 2 — ENTER: flow-conversation

Walk the multi-turn agent conversation graph for {{topic}}.
Map every topic node and its outbound edges.
Flag: dead ends (node with no valid outbound path), loops (revisiting a node without
forward progress), missing handoff definitions (agent passes control to undefined
destination).

EXIT CRITERIA: Full graph traversal complete. All dead ends and loops identified
or graph declared clean. Record findings or write "no findings — phase 2 clean".

---

PHASE 3 — ENTER: trace-state

Hand-compile the state machine. For each state: preconditions, transition trigger,
postcondition, system invariants that must hold.
Flag: unguarded transitions, dead states, invariant violations.

EXIT CRITERIA: Every reachable state traced. No state skipped. Record findings
or write "no findings — phase 3 clean".

---

PHASE 4 — ENTER: trace-contract

At every component boundary: state what the producer promises, what the consumer
expects. Compare. Flag every mismatch by type (schema, nullability, ordering,
cardinality, timing).

EXIT CRITERIA: Every boundary crossed. No assumed compatibility. Record findings
or write "no findings — phase 4 clean".

---

PHASE 5 — ENTER: trace-permissions

Walk every RBAC role that touches {{topic}}. For each role: permitted actions,
denied actions. Look for: privilege escalation paths, over-broad grants,
missing deny rules on sensitive operations.

EXIT CRITERIA: Every role walked. No role skipped. Record findings
or write "no findings — phase 5 clean".

---

CONSOLIDATE — do not skip this step

Write ONE report. Not five. Synthesize across all phases.

Rank every finding by blast radius (wide first). Use the definition above.
For each finding:
  - [phase/sub-skill source]
  - What the finding is
  - Blast radius: wide / medium / narrow — and why
  - Severity at the epicenter: high / med / low
  - What must change to resolve it (one clear direction)

Identify any finding that appeared in two or more phases. Call it SYSTEMIC.
Systemic findings rank higher than isolated findings of equivalent blast radius.

SPEC GAPS: List every condition the simulation exposed that the spec does not address.
Write "none detected" if the spec covered every case.

CONTRACT VIOLATIONS: List every producer/consumer mismatch. Write "none detected" if clean.

VERDICT: go / conditional-go / no-go
One sentence rationale. Name the finding that drove it, or state that no blocking
findings were detected.
```
