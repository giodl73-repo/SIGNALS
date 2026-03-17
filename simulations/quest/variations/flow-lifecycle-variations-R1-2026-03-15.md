## flow-lifecycle Variations — V-01 through V-05

---

### V-01 — Axis: Role Sequence (Roles First, Drive the Walk)
**Hypothesis**: Surfacing domain roles before the lifecycle forces expert-lens ownership at every gate; generic transitions get blocked by role-check pressure.

```markdown
You are simulating a business process lifecycle for: **{lifecycle}**

---

## Step 1 — Assign Domain Roles

Before touching any process step, select the expert panel for this lifecycle.
Auto-select 3–5 roles from the process context. Each role must be domain-qualified
(not "Approver" — use "Senior Credit Analyst", "Procurement Category Manager", etc.).

For each role, state:
- Role title (domain-qualified)
- Primary accountability in this lifecycle
- The decision gates they own

Do not proceed to Step 2 until every role is named and every gate has an owner.

---

## Step 2 — Walk the Lifecycle State by State

List every state the document or case passes through. For each state:
- State name (e.g., "Credit Hold", "PO Approved — Pending Goods Receipt")
- Entry trigger: what specific event or condition causes entry
- Exit trigger: what specific event or condition causes exit
- Owner role from your panel

Minimum 6 named states. No "then X happens" descriptions — each state boundary
must be explicit.

---

## Step 3 — Model Decision Points

For each decision gate in the lifecycle:
- Decision name
- Condition being evaluated (quantified or rule-based)
- Owner role (from your panel — no "system" ownership without a human sponsor)
- All outcome branches, each leading to a named next state

Minimum 3 decision points.

---

## Step 4 — Trace Exception Flows

Identify at least 3 exception scenarios. For each:
- Triggering condition (what breaks or deviates)
- Divergence point: which state/step the exception branches from
- Trace the exception path to its recovery state OR named failure terminal

---

## Step 5 — Identify Parallel Paths

Does this lifecycle have steps that run concurrently? If yes:
- Name each parallel path
- Name the join condition that synchronizes them back

If no parallel paths exist, state explicitly why and what enforces strict sequencing.

---

## Step 6 — Declare Terminal States

List every terminal state. At minimum:
- 1 success terminal (with the condition that closes it)
- 1 failure/cancellation terminal (with the condition and who authorizes it)

Verify: every traced path (happy + exception) reaches a named terminal.

---

## Step 7 — Find Bottlenecks and Gaps

**Bottlenecks (≥2):**
For each bottleneck: cause, which state it impacts, downstream consequence.

**Process gaps (≥1):**
A step that should exist but doesn't. Name it, state why it's missing, and what
can go wrong because of the omission.

---

## Step 8 — Surface Edge Cases

Identify 2+ edge cases not covered in your exception flows. For each:
- Scenario description
- Why the lifecycle design doesn't handle it
- Consequence if it occurs in production

---

## Step 9 — Cross-Lifecycle Handoffs

Name at least 1 handoff point where this lifecycle touches an adjacent lifecycle
(e.g., L2O handing to P2P, P2P handing to period close). For each:
- Direction (outbound / inbound)
- Partner lifecycle name
- Coupling state: what data or condition is handed across

---

## Output Format

Produce sections in the order above. Use headers and sub-bullets.
End with a one-paragraph **Lifecycle Health Summary** written by your panel's
most senior role, assessing the process's robustness and top risk.
```

---

### V-02 — Axis: Output Format (Table-First, Structured Columns)
**Hypothesis**: Forcing every claim into a table column eliminates prose drift; the rubric's ≥N conditions become countable cells, not buried paragraphs.

```markdown
You are simulating a business process lifecycle for: **{lifecycle}**

Produce all output in structured tables. Prose is permitted only in the final summary.

---

## Table 1 — Domain Role Panel

| Role Title (domain-qualified) | Lifecycle Accountability | Decision Gates Owned |
|-------------------------------|--------------------------|----------------------|
| ...                           | ...                      | ...                  |

Minimum 3 roles. No generic titles.

---

## Table 2 — State Inventory

| State Name | Entry Trigger | Exit Trigger | Owner Role | State Type |
|------------|---------------|--------------|------------|------------|
| ...        | ...           | ...          | ...        | (active / wait / terminal) |

Minimum 6 states. Mark terminal states in the State Type column.
Every terminal row must be classified: (success) or (failure/cancel).

---

## Table 3 — Decision Points

| Decision Name | Condition | Owner Role | Branch A → State | Branch B → State | Branch C (if any) |
|---------------|-----------|------------|------------------|------------------|-------------------|
| ...           | ...       | ...        | ...              | ...              | ...               |

Minimum 3 decision points. All branches must reference a state from Table 2.

---

## Table 4 — Exception Flows

| Exception ID | Triggering Condition | Divergence State | Exception Path | Terminal State |
|--------------|----------------------|------------------|----------------|----------------|
| EX-01        | ...                  | ...              | ...            | ...            |

Minimum 3 rows.

---

## Table 5 — Parallel Paths

| Path Name | Parallel Steps | Join Condition | Rejoins At State |
|-----------|---------------|----------------|-----------------|
| ...       | ...           | ...            | ...             |

If no parallel paths: insert one row with Path Name = "None" and a Rationale column
explaining what enforces strict sequencing.

---

## Table 6 — Bottlenecks

| Bottleneck ID | Affected State | Root Cause | Downstream Impact |
|---------------|---------------|------------|-------------------|
| BN-01         | ...           | ...        | ...               |

Minimum 2 rows.

---

## Table 7 — Process Gaps

| Gap ID | Missing Step Description | Why Absent | Consequence |
|--------|--------------------------|------------|-------------|
| GP-01  | ...                      | ...        | ...         |

Minimum 1 row.

---

## Table 8 — Edge Cases

| Edge Case ID | Scenario | Gap Reason | Consequence |
|--------------|----------|------------|-------------|
| EC-01        | ...      | ...        | ...         |

Minimum 2 rows. Must be distinct from Table 4 exception flows.

---

## Table 9 — Cross-Lifecycle Handoffs

| Direction | Partner Lifecycle | Coupling State / Data Transferred |
|-----------|------------------|-----------------------------------|
| ...       | ...              | ...                               |

Minimum 1 row.

---

## Table 10 — SLA and Timing Annotation

| State Name | Typical Duration | SLA Target | AT-RISK? | Causal Bottleneck (ref BN-ID) |
|------------|-----------------|------------|----------|-------------------------------|
| ...        | ...             | ...        | Yes/No   | ...                           |

Minimum 3 states annotated. At least 1 row marked AT-RISK.

---

## Lifecycle Health Summary

Two to three sentences of prose. Written from the perspective of the most senior
role in Table 1. States the top systemic risk and single most impactful fix.
```

---

### V-03 — Axis: Phrasing Register (Conversational, Imperative, Step-by-Step Commands)
**Hypothesis**: Imperative "do this now" framing reduces hedging; the model treats each step as an action to execute rather than a topic to discuss.

```markdown
You are about to simulate a business process lifecycle.

Your subject: **{lifecycle}**

Work through this exactly. Don't skip steps.

---

**First: pick your team.**

Who runs this process in real life? Choose 3 to 5 domain-qualified roles — the actual
job titles that own this work. For each person on your team, tell me what they're
responsible for and which decision gates they own. Don't call anyone "Approver" or
"Reviewer" — give me their real title.

---

**Now walk me through every state this process passes through.**

I need at least 6 named states. For each one, tell me:
- What triggers entry into this state (be specific — not "when approved", tell me
  what event fires)
- What triggers the exit (same rule — be specific)
- Who on your team owns this state

---

**Find every place where the process hits a fork.**

At each decision gate, tell me:
- What question is being asked
- Who makes the call
- Every possible outcome and where it leads next

Give me at least 3 decision points.

---

**Now break it.**

Walk me through at least 3 ways this process can go wrong. For each failure scenario:
- What sets it off
- Which step does it branch away from
- Where does it end up — recovery, rework, or hard failure

---

**Does anything run in parallel?**

If multiple things happen simultaneously, name those paths and tell me what brings
them back together. If everything is sequential, tell me why — what would break if
you tried to parallelize it.

---

**Where does it end?**

Give me every terminal state — at minimum one success close and one failure/cancel.
For each: what condition triggers it, and who signs off. Then verify: every path
you've traced (normal + exception) lands on a named terminal. If any path is
dangling, fix it now.

---

**What's slowing it down? What's missing entirely?**

Bottlenecks (at least 2): name the state, explain the cause, tell me the downstream
damage.

Process gaps (at least 1): what step should exist but doesn't? Why is it absent?
What goes wrong because of the omission?

---

**What does this process never handle?**

Find 2 or more edge cases that aren't in your failure scenarios above. For each:
describe the situation, explain why the process design has no answer for it, and
tell me what happens when it shows up in production.

---

**What does this process hand off to, and what feeds into it?**

Name at least one adjacent lifecycle this process connects to. Tell me the direction,
what's being handed, and what state both sides are in when the handoff happens.

---

**Finally — how healthy is this process?**

Your most senior team member writes a brief assessment: is this process production-
ready or fragile? What's the single biggest risk? What's the one fix that would
have the most leverage?
```

---

### V-04 — Combined Axis: Lifecycle Emphasis (Phase-Heavy Boundaries) + Inertia Framing (Status-Quo Competitor Prominent)
**Hypothesis**: Naming the incumbent manual/legacy process at each phase keeps the model grounded in realistic friction rather than idealized flows; phase-boundary explicitness prevents state conflation.

```markdown
You are simulating the lifecycle of: **{lifecycle}**

This process exists in real organizations. In most of them today, it is executed
manually — through email threads, spreadsheets, shared drives, and tribal knowledge.
Before you model the ideal lifecycle, keep that incumbent in mind at each phase.
The gaps and bottlenecks you find must be real, not theoretical.

---

## Phase Boundaries First

Before walking any steps, declare the top-level phases of this lifecycle. Each phase
is a named chunk of the process with a clear entry condition and a clear exit condition.
A phase boundary is a real handoff — ownership transfers, a document changes form,
or a system records a state change.

List 3–5 phases. For each:
- Phase name
- Entry condition (what event or artifact triggers this phase to start)
- Exit condition (what event or artifact marks this phase complete)
- Primary owner role (domain-qualified — not generic)

---

## Phase Deep-Dives

For each phase from above, walk the internal states:

**[Phase Name]**

Steps and states within this phase (minimum 2 per phase):
- State name → entry trigger → exit trigger → owner

Decision points inside this phase:
- Decision name → condition → owner → all outcome branches

How does the manual/legacy version of this phase work? What are people doing
in Excel or email that a well-designed process would automate or enforce?

Exception flows inside this phase:
- What can go wrong here specifically?
- Does the exception recover within the phase or escalate out?

---

## Cross-Phase Transitions

For each phase boundary you declared:
- What artifact or event crosses the boundary?
- What state does the receiving phase start in?
- What data must be present for the transition to be valid?
- What happens when that data is missing or wrong? (This is a gap if there is
  no defined answer.)

---

## Parallel Paths

Does this lifecycle have phases or steps that run concurrently?
- If yes: name the paths, their join condition, and the state they converge to.
- If no: state what enforces strict sequencing and whether that constraint is
  necessary or inherited from the manual process.

---

## Terminal States

List every terminal state across all phases:
- At minimum: 1 success terminal, 1 failure terminal, 1 cancellation terminal
- For each: triggering condition, authorizing role, what data is archived

---

## Bottleneck Analysis

Identify at least 2 bottlenecks. For each:
- Which phase and state it occurs in
- Root cause (be specific — is it a waiting step? an approval queue? a data
  dependency on a slow upstream system?)
- Downstream impact on the rest of the lifecycle

**Inertia note**: For each bottleneck, assess whether it exists because the process
was designed this way intentionally, or because it was inherited from the manual
process and never redesigned.

---

## Process Gaps

Identify at least 1 step that should exist but doesn't:
- What is the missing step?
- At which phase boundary or internal transition is it absent?
- What happens in production when the omission is encountered?

---

## Edge Cases

Identify 2+ edge cases not covered in your exception flows:
- Scenario description
- Why this lifecycle has no defined path for it
- Consequence

---

## Cross-Lifecycle Handoffs

Name at least 1 adjacent lifecycle that this process connects to. For each handoff:
- Direction (outbound from this lifecycle / inbound)
- Partner lifecycle name
- Coupling state: what document, event, or data crosses the boundary

---

## SLA and Timing

For at least 3 states or phases, annotate:
- Typical duration in the manual process
- Target duration in a well-designed version
- Whether this state is AT-RISK of SLA breach

Mark at least 1 state AT-RISK and reference the bottleneck that causes it.

---

## Lifecycle Health Summary

Produce a brief assessment from the perspective of the most senior domain role:
1. What is the most fragile handoff in this lifecycle?
2. Where does the legacy/manual inheritance cause the most damage?
3. What single redesign would have the highest leverage?
```

---

### V-05 — Combined Axis: Role Sequence (Sequential Handoffs as Primary Structure) + Output Format (Prose Narrative with Embedded Callouts)
**Hypothesis**: Structuring the lifecycle as a relay race — each role explicitly receives and passes ownership — makes missing handoffs and ambiguous transitions viscerally obvious; prose narrative forces the model to reason continuously rather than fill table cells.

```markdown
You are simulating a business process lifecycle for: **{lifecycle}**

Structure your simulation as a **relay narrative** — the lifecycle is a relay race
where ownership passes from role to role. Your job is to tell the story of one
complete lifecycle execution, narrating each handoff and every decision along the way.

---

## Cast of Characters

Open with your role panel. Select 3–5 domain-qualified roles from the process context.
For each, write one sentence: who they are, what they own, and what they're watching for.

Example format:
> **Maria Chen, Senior Credit Analyst (Finance)** — owns credit assessment and the
> hold/release decision gate. Watching for: incomplete financial data, credit limit
> exceptions, disputed invoice chains.

Do not proceed until every decision gate has a named owner.

---

## The Normal-Path Narrative

Tell the story of a lifecycle that goes right. Walk every state in sequence.
For each state transition, write:
- A sentence describing what event or action triggers the state change
- Who is handing off to whom (or if the same role continues)
- What the receiving role checks before accepting the work

**Callout rule**: Wherever a decision gate occurs, break into a structured callout:

> **DECISION [name]**
> Owner: [role]
> Condition: [what is being evaluated]
> If yes: [outcome and next state]
> If no: [outcome and next state]
> If missing data: [what happens — this is not optional]

Minimum 6 named states. Minimum 3 decision callouts.

---

## The Parallel Plot

If two or more roles work simultaneously at any point, write a parallel narrative
section. Label each parallel thread and narrate them side by side. At the
convergence point, write:

> **JOIN [join point name]**
> Thread A delivers: [what]
> Thread B delivers: [what]
> Merge condition: [what must be true before continuing]

If no parallel paths exist, write one paragraph explaining why sequencing is strict
and whether that constraint is necessary or accidental.

---

## Three Things Go Wrong

Write three exception scenarios, each as a short narrative:
- Set the scene: which state, what condition triggers the exception
- Walk the exception path to its end
- End each scenario with a named terminal state: recovery, rework, or hard failure

These must be distinct paths, not variations of the same failure.

---

## The Edge Cases Nobody Planned For

Write 2+ short paragraphs, each describing an edge case the process design ignores.
For each:
- Describe the situation concretely (a real-world scenario, not abstract)
- Explain what the process currently does — which is usually nothing, or the wrong thing
- State the consequence

---

## Handoffs to Adjacent Lifecycles

Write a brief section narrating where this lifecycle ends and another begins.
Name the partner lifecycle, describe what is handed across, and state what coupling
exists — what does the receiving lifecycle depend on from this one?

At least 1 outbound or inbound handoff.

---

## Where It Slows Down

Write a bottleneck section in prose. For each bottleneck (minimum 2):
- Name the state or transition
- Explain the cause in one sentence
- Explain the downstream consequence in one sentence

Then add a gap paragraph: what step is absent from this process that should be there?
Name the gap, explain the omission, and describe what breaks when it's encountered.

---

## Timing Risks

In a short table, annotate at least 3 states with timing:

| State | Typical Duration | SLA Target | AT-RISK? | Bottleneck Reference |
|-------|-----------------|------------|----------|----------------------|
| ...   | ...             | ...        | ...      | ...                  |

At least 1 row must be AT-RISK with a specific bottleneck reference.

---

## Closing Assessment

The most senior role on your panel writes a one-paragraph assessment of this
lifecycle's health. They have just watched the full relay. What did they see?
What is the single most dangerous gap? What would they fix first?
```

---

## Variation Axis Summary

| ID | Axis | Hypothesis | Distinguishing Feature |
|----|------|------------|----------------------|
| V-01 | Role sequence | Role-first pressure blocks generic transitions | Roles assigned before any lifecycle step |
| V-02 | Output format | Table columns make rubric criteria directly countable | All output in structured tables |
| V-03 | Phrasing register | Imperative register reduces hedging prose | Conversational commands ("do this now") |
| V-04 | Lifecycle emphasis + inertia framing | Legacy process anchor surfaces real friction | Phase-boundary-first + manual incumbent named per phase |
| V-05 | Role sequence + output format | Relay narrative structure makes missing handoffs visceral | Prose relay race with embedded callout blocks |
