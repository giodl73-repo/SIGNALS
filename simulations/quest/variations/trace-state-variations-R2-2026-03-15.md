## trace-state Variations — Round 2 (V-01 through V-05)

---

### V-01 — Axis: Output Format
**Hypothesis**: Mandatory columnar table with criterion IDs baked into column headers forces C-01/C-02/C-03 coverage mechanically and earns C-11 (inline criterion anchoring) without extra prompting.

```
You are a state-transition analyst. Hand-compile the state machine for the
feature described below. Your output MUST use the exact table schema shown
here — no prose substitutions.

---

## TRACE TABLE (C-01: starting state · C-02a: pre · C-02b: post · C-03: invariants)

| Step | Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] | Ending State [C-01c] | Postconditions [C-02b] | Invariants Checked [C-03] |
|------|------------------------|-------------------|-----------------------|----------------------|------------------------|---------------------------|
| 1    | …                      | …                 | …                     | …                    | …                      | INV-1 ✓, INV-2 ✓         |
| 2    | …                      | …                 | …                     | …                    | …                      | INV-1 ✓, INV-2 ✓         |

(Add rows for every operation in scope.)

---

## INVARIANT REGISTER

Declare at least two domain-meaningful invariants before the trace. Each must
encode a real business rule, not a structural tautology.

| ID    | Invariant Statement [C-07] | Derived From Step [C-13] |
|-------|----------------------------|--------------------------|
| INV-1 | …                          | Step N observation       |
| INV-2 | …                          | Step N observation       |

---

## DEFECT REGISTER [C-04]

| Defect ID | Type | Triggering Operation | Reason |
|-----------|------|----------------------|--------|
| D-01      | …    | …                    | …      |

---

## NEGATIVE PATH TRACE [C-09]

One rejected operation, using the same four-column format: invalid starting
state → blocked operation → unchanged ending state → named error condition.

---

## RACE CONDITION ANALYSIS [C-08 / C-12]

Name one concurrent operation pair. Describe BOTH orderings explicitly:
- Ordering A→B: …
- Ordering B→A: …

State whether the outcomes are symmetric or asymmetric and why.

---

## REACHABILITY ANNOTATION [C-10]

List every transition NOT traced above. For each, give the rationale for
omission (out of scope, unreachable given preconditions, deferred, etc.).
Silent omissions do not qualify.

---

DOMAIN ROLE: You are a Finance state domain expert. States, operations, and
invariants must be recognizable in financial workflow contexts: approval
stages, ledger entries, authorization levels, audit checkpoints.

Feature to trace: {{feature_description}}
```

---

### V-02 — Axis: Role Sequence
**Hypothesis**: Leading with Finance (highest constraint density), then Customer Service, then Sales causes invariants to be derived from the strictest domain first — seeding C-03/C-07 depth before the looser Sales perspective loosens them.

```
You are running a three-role state transition audit. The roles execute in
sequence: Finance first, then Customer Service, then Sales. Each role
independently traces the same feature's state machine, then hands off a
"constraint memo" to the next role.

---

## ROLE 1 — FINANCE STATE DOMAIN EXPERT

Trace the full state machine from a financial controls perspective.

For each operation, supply all four elements:
  1. Starting state
  2. Operation (with preconditions)
  3. Ending state (with postconditions)
  4. Invariant check result

Declare at minimum two invariants that encode real financial rules
(authorization thresholds, balance constraints, audit trail completeness).
Derive each invariant explicitly from an observed trace row — state which
step made you recognize the rule.

Identify at least one defect: type, triggering operation, reason.

Close with a CONSTRAINT MEMO listing the three most critical invariants
and one race condition scenario Finance would flag.

---

## ROLE 2 — CUSTOMER SERVICE STATE DOMAIN EXPERT

Read the Finance constraint memo above. Now trace the same state machine
from a customer-facing service perspective.

  - Inherit the Finance invariants. Note any that do NOT apply in CS context
    (with rationale) and any new CS-domain invariants you add.
  - Trace happy path PLUS at least one rejected operation: show the invalid
    starting state, blocked operation, unchanged state, and named error.
  - Describe one concurrent operation pair (e.g., agent edit + customer
    cancel) with BOTH orderings. State whether outcomes are symmetric.

Close with a CONSTRAINT MEMO noting what Finance missed from the service
perspective and what CS adds to the invariant register.

---

## ROLE 3 — SALES STATE DOMAIN EXPERT

Read both prior constraint memos. Complete the audit from a sales workflow
perspective.

  - Add any Sales-domain states or operations not yet covered.
  - Validate or challenge each inherited invariant with a sales-context
    argument. Do not silently accept — state agreement or disagreement.
  - List every transition NOT traced by any role. For each omission, give
    the rationale. Silent gaps do not qualify.

---

## CONSOLIDATED OUTPUT

After all three roles complete, emit a single consolidated trace table:
  Step | Starting State | Operation | Pre | Ending State | Post | Invariants Checked

Then a consolidated defect register and a final race condition ruling.

Feature to trace: {{feature_description}}
```

---

### V-03 — Axis: Lifecycle Emphasis
**Hypothesis**: Named phases with explicit completion gates and word-budget constraints prevent skipping postconditions and force C-09/C-10 coverage before the analyst can move on.

```
You are a state-transition analyst executing a five-phase protocol. You MUST
complete each phase fully before proceeding. Do not combine phases.

---

## PHASE 1 — STATE INVENTORY
(Complete this before writing any trace rows.)

List every distinct state the system can occupy. For each state:
  - State name
  - What business condition it represents
  - Which operations can originate from it
  - Which states it can transition to

Domain: Sales / Customer Service / Finance — pick the lens that fits the
feature and stay consistent.

Gate: You may not proceed to Phase 2 until every state has at least one
valid originating operation.

---

## PHASE 2 — FORWARD TRACE
(Complete all happy-path operations before adding defects.)

For each operation in the happy path, supply all four elements:
  Starting state → Operation → Ending state → Preconditions · Postconditions

Use a consistent numbered-step format throughout.

Derivation discipline: after each operation, ask whether the observed
transition reveals a new business invariant. If yes, add it to the
INVARIANT CANDIDATES list at the end of this phase. This list feeds Phase 3.

Gate: You may not proceed until every happy-path operation is traced and
the INVARIANT CANDIDATES list has at least two entries.

---

## PHASE 3 — INVARIANT DECLARATION
(Promote candidates from Phase 2 into binding invariants.)

For each candidate in the Phase 2 list:
  - State the invariant precisely
  - Reference the trace step that surfaced it (cross-reference by step number)
  - Classify: financial rule / service rule / sales rule
  - Confirm it encodes a real business constraint, not a structural tautology

Minimum two invariants. Both must be checked after every subsequent
operation in Phase 2 (annotate if you need to update Phase 2 rows).

Gate: You may not proceed until invariants are cross-referenced to trace rows.

---

## PHASE 4 — DEFECT AND NEGATIVE PATH ANALYSIS
(Do not invent defects; derive them from the Phase 2 trace.)

Part A — Defect Register
  For at least one defect: type · triggering operation · reason

Part B — Negative Path Trace
  One rejected operation, all four elements:
    Invalid starting state · Blocked operation · Unchanged state · Named error

Part C — Race Condition
  One concurrent pair. Describe BOTH orderings (A→B and B→A). State whether
  outcomes are symmetric or asymmetric and explain why they differ (or don't).

Gate: You may not proceed until all three parts are present.

---

## PHASE 5 — REACHABILITY AUDIT
(Enumerate what was NOT traced and why.)

List every transition from your Phase 1 state inventory that does not appear
in Phase 2. For each:
  - The omitted transition (from-state → operation → to-state)
  - Rationale: out of scope / unreachable / deferred / conditional on config

Silent omissions do not qualify. Every gap must be named.

---

Feature to trace: {{feature_description}}
```

---

### V-04 — Combined: Role Sequence (Sales-first) + Output Format (Narrative Prose)
**Hypothesis**: Sales-first narrative prose produces richer business-rule encoding (C-07) because storytelling naturally surfaces edge cases — but without table scaffolding, the analyst must discipline themselves on C-01/C-02 completeness, making format failures more diagnostic.

```
You are a Sales state domain expert narrating a state machine audit as a
structured case study. Write in narrative prose — no tables. Use numbered
paragraphs for each operation so reviewers can cite specific steps.

---

## OPENING: DOMAIN SETUP

Open with a one-paragraph description of the business object being traced
(deal, order, account, quota, contract — whichever fits the feature).
Name every state the object can occupy. Explain what each state means to
a salesperson, not to a developer.

---

## NARRATIVE TRACE

For each operation, write a numbered paragraph in this exact structure:

  [N]. **Operation Name** — Starting in *[state]*, the system performs
  *[operation]* when *[preconditions]*. The object moves to *[ending state]*.
  Afterwards, *[postconditions]*. Invariant check: *[INV-1: pass/fail,
  INV-2: pass/fail]*.

Every operation must have all elements above. Do not abbreviate or defer
any element. If a precondition is "none," write "none."

Before writing the first paragraph, declare your invariants:

  **Declared Invariants:**
  - INV-1: [statement] — first observed at Step [N] because [reason]
  - INV-2: [statement] — first observed at Step [N] because [reason]

Invariants must encode real sales rules (discount authority limits, stage
progression gates, contract value thresholds — not generic structural rules).
Cross-reference each invariant to the trace step where you first observed it.

---

## DEFECT NARRATIVE

Write one paragraph identifying a defect. State:
  - The defect type (missing precondition / invalid transition / invariant
    violation / race condition)
  - The specific operation that triggers it
  - The reason it constitutes a defect in sales domain terms

---

## REJECTED OPERATION

Write a paragraph tracing one rejected operation. Include all four elements:
  - The invalid starting state the operation was attempted from
  - The blocked operation
  - The unchanged ending state (the object did not move)
  - The named error or rejection reason

---

## CONCURRENT ACCESS STORY

Describe a scenario where two agents act on the same record simultaneously.
Tell the story twice — once with Agent A acting first, once with Agent B
acting first. Explain whether the outcome is the same in both orderings
or different, and why.

---

## GAPS AND OMISSIONS

End with a section naming every transition from your opening state inventory
that does not appear in the narrative. For each gap, state why it was
omitted. Unlabeled gaps fail this section.

---

## HANDOFF: CUSTOMER SERVICE PERSPECTIVE

Write a two-paragraph handoff note: what did the Sales trace assume or
leave unresolved that a Customer Service analyst would need to revisit?

---

Feature to trace: {{feature_description}}
```

---

### V-05 — Combined: Lifecycle Emphasis + Phrasing Register (Conversational Derivation Coaching)
**Hypothesis**: Coaching language that explicitly asks the analyst "how did you arrive at this invariant?" activates C-13 (invariant derivation pipeline) more reliably than imperative instructions, because it frames derivation as a reasoning exercise rather than a format requirement.

```
Let's hand-compile a state machine together. I'll guide you through the
steps — think of this as a structured thinking exercise, not a form to fill.
At each step, I'll ask you a question. Answer it fully before moving on.

You're working as a domain expert in Sales, Customer Service, or Finance —
pick whichever fits best for the feature below, and stay in that role
throughout.

---

**Step 1 — What states can this thing be in?**

Before tracing any operations, list every state the business object can
occupy. Name them in domain terms your stakeholders would recognize, not
technical terms. For each state, briefly explain what it means in practice.

Take your time here. Incomplete state inventories cause problems later.

---

**Step 2 — Walk me through the happy path.**

For each operation that moves the object from one state to another, tell me:

  - Where it starts (starting state)
  - What happens (the operation)
  - What has to be true before it can happen (preconditions — if nothing,
    say so explicitly)
  - Where it ends up (ending state)
  - What's guaranteed to be true afterwards (postconditions)

Use a consistent format for every step — numbered steps work well.

As you trace each operation, pause and ask yourself: *does this transition
reveal a rule that must always hold?* If yes, note it as an invariant
candidate. We'll formalize them in the next step.

---

**Step 3 — What did you just learn about the invariants?**

Look back at your trace. Which steps made you realize there's a rule that
can never be violated? For each invariant you declare:

  - State the rule precisely in business terms
  - Tell me which step surfaced it — "I noticed this at Step N when..."
  - Explain why it's a real business constraint, not just a structural fact
    about the data model

You need at least two. Both will be checked against every operation in
your trace — go back and add the check results if you haven't already.

---

**Step 4 — What could go wrong?**

Three sub-questions:

*4a. Defect:* Is there an operation where the system might skip a
precondition check, allow an invalid transition, or violate an invariant?
Name it: what's the defect type, which operation triggers it, and why
is it a defect in your domain?

*4b. Rejected operation:* Trace one operation that should be blocked.
Walk through all four elements: the invalid state it was attempted from,
the blocked operation, the fact that the state did NOT change, and the
error or rejection reason the system should emit.

*4c. Concurrent access:* Name two operations that could race. Now tell
me what happens if A goes first, then B. Then tell me what happens if
B goes first, then A. Are the outcomes the same? If not, which ordering
is safe and which is dangerous?

---

**Step 5 — What did you not trace, and why?**

Look at the state inventory from Step 1. Which transitions from that
inventory don't appear anywhere in your trace? For each one, tell me why:
is it out of scope, unreachable given the preconditions, deferred to a
future phase, or conditional on configuration?

Don't leave any gaps unnamed. Unlabeled omissions fail this section.

---

Feature to trace: {{feature_description}}
```

---

## Variation Summary

| # | Axes | Hypothesis |
|---|------|------------|
| V-01 | Output format (columnar table + C-ID headers) | Table schema mechanically forces C-01–C-03 and earns C-11 via column labels |
| V-02 | Role sequence (Finance → CS → Sales with constraint memos) | Constraint-heaviest role first seeds invariant depth; memos propagate it |
| V-03 | Lifecycle emphasis (5 explicit phases with completion gates) | Phase gates prevent skipping; derivation discipline in Phase 2→3 earns C-13 |
| V-04 | Role sequence (Sales-first) + output format (narrative prose) | Storytelling surfaces C-07 richness; missing table scaffolding is diagnostic |
| V-05 | Lifecycle emphasis + phrasing register (conversational coaching) | "How did you arrive at this?" framing activates C-13 more than imperative instructions |
