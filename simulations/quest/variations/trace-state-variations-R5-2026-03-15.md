## trace-state Variations — Round 5 (v20 rubric)

---

## V-01 — Output Format: Schema-Level Enforcement

**Axis:** Output format
**Hypothesis:** Embedding criterion IDs directly into column header labels (C-14) transforms the schema into a self-enforcing artifact. Adding a filled example row with placeholder anchors (C-15), an explicit numeric floor (C-17), a named anti-example for triviality (C-18), and an invalidation clause (C-19) clusters five aspirational criteria into the format itself — earned structurally, not by instruction compliance.

---

You are a state machine analyst for a [Sales / Customer Service / Finance] feature. Hand-compile a state transition trace for the feature under review.

**Hard rules — violation of any rule below invalidates this artifact:**
1. No prose substitutions for table columns. Every cell must be filled with structured content.
2. The state transition table must contain at least 5 data rows (not counting the example row EX).
3. Every Preconditions cell must be filled. Write `none` only if the operation genuinely has no preconditions.
4. **Disqualifying invariant pattern — your artifact is invalid if you submit this:** `ID is not null`. Structural database constraints are not domain invariants. Name a rule a domain expert would audit manually.

---

### Section 1 — State Transition Table

| Row [C-01] | Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] | State Changes | Postconditions [C-02b] | Ending State [C-01c] | I-1 ✓/✗ [C-03] | I-2 ✓/✗ [C-03] | Defect? [C-04] |
|------------|------------------------|-------------------|-----------------------|---------------|------------------------|----------------------|----------------|----------------|----------------|
| EX | Opportunity: Qualified | Advance to Proposal | Needs assessment complete; decision-maker identified | stage: Qualified → Proposal; forecast_category updated | Proposal doc exists; stage = Proposal | Opportunity: Proposal | ✓ amount > 0 | ✓ stage ∈ valid set | — |
| 1 | … | … | … | … | … | … | … | … | … |
| 2 | … | … | … | … | … | … | … | … | … |
| 3 | … | … | … | … | … | … | … | … | … |
| 4 | … | … | … | … | … | … | … | … | … |
| 5 | … | … | … | … | … | … | … | … | … |

Add more rows as needed. Minimum 5 data rows required.

---

### Section 2 — Declared Invariants [C-03, C-07]

Declare at least 2 invariants. Each must encode a real domain business rule. Cross-reference each invariant back to the row(s) in the trace where it is checked [C-13].

| ID | Invariant Statement [C-07] | Operations That Could Violate It | Source row(s) in trace [C-13] |
|----|---------------------------|----------------------------------|-------------------------------|
| I-1 | … | … | Row … |
| I-2 | … | … | Row … |

---

### Section 3 — Defect Catalog [C-04]

At least one defect required.

| Defect ID | Type | Triggering Operation (Row #) | Reason |
|-----------|------|------------------------------|--------|
| D-1 | `invalid transition` \| `missing precondition` \| `invariant violation` \| `race condition` | Row … | … |

---

### Section 4 — Negative Path Trace [C-09]

| Element | Value |
|---------|-------|
| Invalid starting state | … |
| Blocked operation | … |
| Unchanged ending state | … |
| Named error / exception | … |

---

### Section 5 — Race Condition Analysis [C-08, C-12]

Concurrent pair: **Op-A = [name]**, **Op-B = [name]**

**A → B ordering:**
- State after A executes: …
- State after B executes (seeing A's result): …
- Conflict outcome: …

**B → A ordering:**
- State after B executes: …
- State after A executes (seeing B's result): …
- Conflict outcome: [describe this ordering independently — "same as above" or "symmetric" disqualifies]

---

### Section 6 — Omitted Transitions [C-10]

| Omitted Transition (From → To) | Rationale for Omission |
|-------------------------------|------------------------|
| … | … |

Silent omissions do not qualify for reachability credit.

---

Domain: [Sales / Customer Service / Finance] — pick the domain most relevant to the feature. All states, operations, and invariants must be grounded in that domain's real business logic.

---

## V-02 — Role Sequence: Finance First

**Axis:** Role sequence
**Hypothesis:** Leading with Finance forces richer quantified invariants. Financial workflows have natural numeric floors — minimum amounts, balance constraints, period-close rules, approval thresholds — that encode real business logic by nature. A Finance-first trace earns C-07 non-trivial invariants structurally rather than by effort, and the quantified framing carries into CS and Sales layers when the feature spans domains.

---

You are a Finance state domain expert performing a hand-compilation of state transitions for the feature under review.

Finance workflows center on: approval chains, amount thresholds, balance constraints, period-close rules, and audit trails. Every state has a monetary or approval-status dimension. Ground your trace in these realities first.

If the feature also touches **Customer Service**: add a CS layer after the Finance trace, focusing on case status, SLA triggers, and escalation gates.

If the feature also touches **Sales**: add a Sales layer after CS, focusing on pipeline stage, quota impact, and commit status.

---

### Step 1 — Declare invariants before you write a single trace row

Name at least 2 invariants. These must encode real Finance business rules — not structural constraints.

**Qualifying examples:**
- "Invoice amount must remain positive at all stages after creation"
- "An expense report in Approved state cannot re-enter Draft without an audit record"
- "Period-close locks all write operations for the closed fiscal period"

**Disqualifying examples — do not submit these:**
- "ID is not null" — database constraint, not a domain invariant
- "Record exists in table" — structural, not behavioral

Declared invariants:
- **I-1:** …
- **I-2:** …
- *(add more as needed)*

---

### Step 2 — Trace at least 5 operations

For each operation:

**Operation N: [Operation Name]**
- Starting state: …
- Preconditions: … *(write `none` only if genuinely absent)*
- State changes: … *(which fields, values, status flags change)*
- Postconditions: … *(what is guaranteed true after the operation)*
- Ending state: …
- Invariants checked: I-1 [holds / violated], I-2 [holds / violated]
- Defect (if any): … *(type + reason, or `none`)*

Use this format consistently for every operation. Minimum 5 operations.

---

### Step 3 — Defect catalog

Summarize every defect found. At least one required.

**D-N — [Type]: [Title]**
- Type: `invalid transition` | `missing precondition` | `invariant violation` | `race condition`
- Triggering operation: …
- Reason: …

---

### Step 4 — Negative path trace

Pick one operation that should be rejected because the starting state is wrong:
- Invalid starting state for this operation: …
- Blocked operation: …
- Unchanged ending state (the operation has no effect): …
- Named error or exception raised: …

---

### Step 5 — Race condition: both orderings

Identify one pair of concurrent operations. Describe each ordering **independently**.

**Op-A = [name], Op-B = [name]**

*Order 1 — A executes first, then B:*
- State after A: …
- State after B (seeing A's result): …
- Conflict? [yes / no] — reason: …

*Order 2 — B executes first, then A:*
- State after B: …
- State after A (seeing B's result): …
- Conflict? [yes / no] — reason: …

Do not write "same as above" or "symmetric" for Order 2. Describe it explicitly.

---

### Step 6 — Invariant derivation cross-reference

For each invariant, note which trace operation revealed or confirmed it:
- **I-1** derived from: Operation [N] — [brief note on how that operation exposed the invariant]
- **I-2** derived from: Operation [N] — [brief note]

---

### Step 7 — Omitted transitions

List every state transition you chose not to trace, with rationale. Silent omissions disqualify the reachability claim.

- [Transition]: [Rationale]

---

## V-03 — Phrasing Register: Conversational Imperative

**Axis:** Phrasing register
**Hypothesis:** Short, direct imperative commands with explicit "do not do X" rules reduce the model's tendency to produce hedging prose ("this could involve…"). When the instructions sound like a checklist an expert gives to a junior analyst, structural compliance increases because each instruction maps to exactly one action — there is no interpretive slack that allows prose substitution.

---

You are going to hand-compile a state machine trace. No summaries. No narrative paragraphs. Structured output only.

Pick one domain: Sales, Customer Service, or Finance. Stay in that domain for the entire trace.

---

**First: declare your invariants.**

Before you trace anything, write down at least 2 invariants. They must encode real business logic — the kind of rule a domain expert would audit manually.

Do NOT write: `ID is not null`. That is a database constraint, not a business invariant. It fails. Write something that would matter to a Sales VP, a CS team lead, or a Finance controller.

---

**Now trace at least 5 operations.**

For each one, give me all seven of these — in order, every time:

1. **Starting state**
2. **Preconditions** — what must be true for this operation to be valid. Write `none` only if there genuinely are none.
3. **State changes** — which fields, values, or status flags change
4. **Postconditions** — what is guaranteed to be true after the operation completes
5. **Ending state**
6. **Invariants checked** — check each invariant you declared; say whether it holds or was violated
7. **Defect** — if something's wrong, name the type and reason. If nothing's wrong, write `none`.

Minimum 5 operations. Use a consistent format for every operation.

---

**Flag at least one defect.**

Pick the most interesting one you found. Give it:
- A type: `invalid transition`, `missing precondition`, `invariant violation`, or `race condition`
- The operation that triggers it
- Why it is a defect — one or two sentences

---

**Run a negative path.**

Find one operation that gets rejected because the starting state is wrong. Show all four:
- The invalid starting state
- The blocked operation
- The unchanged ending state after rejection
- The error or exception that fires

---

**Run a race condition — both orderings.**

Pick two operations that can run concurrently. Show me what happens in each ordering:
- What happens if A runs before B
- What happens if B runs before A

Do not write "symmetric." Write it out for both. They might not produce the same result.

---

**List what you skipped.**

Name every transition you did not trace. Give a reason for each one. Saying nothing is not acceptable — silent omissions disqualify you.

---

**Format rules:**
- Table or numbered steps — pick one and stick to it for the whole trace
- No prose paragraphs in place of structured fields
- No blank cells — write `none` if a field is genuinely empty
- No skipping the invariant check for any row

---

## V-04 — Combination: Output Format + Lifecycle Emphasis

**Axis:** Output format (schema enforcement) × Lifecycle emphasis (explicit phase gates with completion checks)
**Hypothesis:** Phase-gating prevents the most common failure mode: the model interleaves phases (declares invariants while tracing, buries defects in narrative, skips negative paths as "optional"). Requiring a completion check before advancing each phase forces full coverage of C-01 through C-05 before reaching C-08/C-09. Schema enforcement within each phase closes the prose-substitution escape hatch. The combination should maximize essential pass rate and aspirational cluster coverage simultaneously.

---

You are a state machine analyst for a [Sales / Customer Service / Finance] feature. Produce a hand-compiled state transition trace in five phases. **Complete each phase fully before advancing to the next. Do not mix phases.**

**Hard constraint — violation invalidates the artifact:** No prose substitutions for any structured section. Fill every field. Write `none` only when genuinely applicable.

---

### PHASE 1 — Invariant Declaration
*Complete this phase before writing any trace rows.*

Declare at least 2 invariants. Each must encode a real domain business rule that a domain expert would audit manually.

**Disqualifying pattern — your artifact is invalid if you submit this:** Structural constraints such as `ID is not null` or `record exists` are not domain invariants. Name the business rule, not the database constraint.

| ID | Invariant Statement [C-07] | Operations That Could Violate It | Source row in trace [C-13] |
|----|---------------------------|----------------------------------|---------------------------|
| I-1 | … | … | Row # — fill after Phase 2 |
| I-2 | … | … | Row # — fill after Phase 2 |

After completing Phase 2, return here and fill in the `Source row in trace` column.

**Phase 1 completion check:** ≥2 invariants declared, none are structural DB constraints ✓/✗

---

### PHASE 2 — State Transition Trace
*Minimum 5 data rows. Fill every cell.*

| Row [C-01] | Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] | State Changes | Postconditions [C-02b] | Ending State [C-01c] | I-1 ✓/✗ [C-03] | I-2 ✓/✗ [C-03] | Defect? [C-04] |
|------------|------------------------|-------------------|-----------------------|---------------|------------------------|----------------------|----------------|----------------|----------------|
| EX | Case: Unassigned | Assign to agent | Agent available; case severity ≤ agent tier | assigned_to = agent_id; status → In Progress | Agent notified; SLA clock started | Case: In Progress | ✓ SLA clock running | ✓ assigned_to not null | — |
| 1 | … | … | … | … | … | … | … | … | … |
| 2 | … | … | … | … | … | … | … | … | … |
| 3 | … | … | … | … | … | … | … | … | … |
| 4 | … | … | … | … | … | … | … | … | … |
| 5 | … | … | … | … | … | … | … | … | … |

After completing this table, return to Phase 1 and fill in the `Source row in trace` column for each invariant.

**Phase 2 completion check:** ≥5 data rows, every cell filled, I-1/I-2 columns checked per row ✓/✗

---

### PHASE 3 — Defect Catalog + Negative Path
*At least one defect required. Negative path is a separate structured entry.*

**Defects from trace:**

| Defect ID | Type | Triggering Operation (Row #) | Reason |
|-----------|------|------------------------------|--------|
| D-1 | `invalid transition` \| `missing precondition` \| `invariant violation` \| `race condition` | Row … | … |

**Negative path trace:**

| Element | Value |
|---------|-------|
| Invalid starting state | … |
| Blocked operation | … |
| Unchanged ending state | … |
| Named error / exception | … |

**Phase 3 completion check:** ≥1 defect in catalog, negative path has all 4 elements ✓/✗

---

### PHASE 4 — Race Condition Analysis
*Both orderings required. Describe the second ordering independently — do not write "symmetric."*

Concurrent pair: **Op-A = [name]**, **Op-B = [name]**

**Ordering A → B:**
- State before A: …
- State after A executes: …
- State after B executes (seeing A's result): …
- Conflict outcome: [conflict / safe merge / last-write-wins / lock required / …]

**Ordering B → A:**
- State before B: …
- State after B executes: …
- State after A executes (seeing B's result): …
- Conflict outcome: [describe independently — "same as above" disqualifies this phase]

**Phase 4 completion check:** Both orderings filled explicitly, no shortcut reference between them ✓/✗

---

### PHASE 5 — Omitted Transitions
*Silent omissions disqualify reachability credit.*

| Omitted Transition (From → To) | Rationale for Omission |
|-------------------------------|------------------------|
| … | … |
| … | … |

**Phase 5 completion check:** Every untraced transition listed with rationale ✓/✗

---

Domain: [Sales / Customer Service / Finance] — select the one best matching the feature under review.

---

## V-05 — Combination: Role Sequence (CS First) + Inertia Framing

**Axis:** Role sequence (Customer Service leads) × Inertia framing (explicit contrast with the naive "list states" approach that fails)
**Hypothesis:** CS-first framing naturally surfaces re-open, re-assign, and SLA-triggered escalation edges — transitions that naive traces consistently miss because they appear after "resolution." Inertia framing (showing what a naive trace produces and naming its failure modes) prevents the "just list states" failure mode before it occurs, because the model has already been shown what that looks like and told why it fails. Together they should produce the highest defect count and non-trivial invariant quality.

---

You are a Customer Service state domain expert. Before you produce anything, read this section.

---

### What a naive trace looks like — and why it fails

A naive trace names states and operations without analyzing transitions:

> "A support case can be Open, In Progress, Resolved, or Closed. Agents move cases between these states based on activity."

This is useless for defect detection. It misses:
- What makes a transition **valid** — the preconditions that must hold
- What the system **guarantees** after a transition — the postconditions
- Which business rules **must hold at every step** — the domain invariants
- What happens when **two agents act simultaneously** — race conditions
- What happens when someone **attempts an invalid transition** — the negative path

A hand-compiled trace answers all of these. That is what you are producing.

---

### Your domain: Customer Service (primary)

If the feature spans Sales, add a Sales layer after the CS trace (pipeline stage, quota impact, commit status).
If the feature spans Finance, add a Finance layer after CS (billing status, payment state, period-close locks).

CS state patterns to draw from:
- **Case lifecycle:** Unassigned → Assigned → In Progress → Pending Customer → Resolved → Closed → Reopened
- **Escalation triggers:** SLA breach, severity upgrade, manager reassignment
- **Re-open rules:** who can reopen, from which terminal states, under what conditions
- **Concurrent access:** two agents acting on the same case at the same time

---

### Step 1 — Declare invariants before you trace

Name at least 2 CS-domain invariants. These encode real rules a CS team lead would enforce.

**Disqualified — do not submit:** `Case ID is not null`. This is a database constraint, not a domain invariant. It earns zero credit and downgrades the artifact.

Qualifying examples:
- "A case in Closed state cannot receive agent replies without first transitioning to Reopened"
- "SLA clock stops when case enters Pending Customer and restarts on customer reply"
- "Escalated cases require manager-level assignment before Resolved transition is permitted"

Your invariants:
- **I-1:** …
- **I-2:** …

---

### Step 2 — Trace at least 5 operations

For each operation:

**Operation N: [Name]**
- Starting state:
- Preconditions: *(required; write `none` only if there are genuinely none)*
- State changes: *(which fields, flags, timestamps change)*
- Postconditions: *(what is guaranteed true after this operation completes)*
- Ending state:
- Invariants checked: I-1 [holds / violated], I-2 [holds / violated]
- Defect: *(type + reason, or `none`)*

Maintain this exact format for every operation. Minimum 5 operations.

---

### Step 3 — Defect catalog

List every defect surfaced in the trace. Minimum 1 required.

**D-N — [Type]: [Title]**
- Type: `invalid transition` | `missing precondition` | `invariant violation` | `race condition`
- Triggering operation: …
- Reason: …

---

### Step 4 — Negative path trace

Show one operation that gets blocked because the starting state is wrong:
- Invalid starting state: …
- Blocked operation: …
- Unchanged ending state (rejection leaves state intact): …
- Named error or exception: …

---

### Step 5 — Race condition: both orderings, described independently

CS example to consider: Agent A and Agent B both attempt to assign the same Unassigned case at the same moment.

Identify your concurrent pair. Describe **both orderings independently**.

**Op-A = [name], Op-B = [name]**

*A runs first, then B:*
- State after A: …
- State after B (seeing A's committed state): …
- Conflict or resolution: …

*B runs first, then A:*
- State after B: …
- State after A (seeing B's committed state): …
- Conflict or resolution: [write this out — do not refer back to the first ordering; "same as above" disqualifies this section]

---

### Step 6 — Invariant derivation cross-reference

For each invariant, identify which operation in the trace revealed or stress-tested it:
- **I-1** surfaced at: Operation [N] — [why that operation made this invariant visible]
- **I-2** surfaced at: Operation [N] — [why]

---

### Step 7 — Omitted transitions

Name every transition you did not trace. State why each was omitted. Silent omissions disqualify the reachability claim.

---

### Format rule

Do not substitute narrative paragraphs for structured fields. Every field is a field. If you are about to write a paragraph where a label belongs, stop and use the label.
