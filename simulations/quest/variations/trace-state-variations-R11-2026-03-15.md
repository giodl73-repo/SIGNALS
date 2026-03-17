Good context from R10. That was rubric v8 with a completely different criterion set (HANDOFF DECLARATION, IS-phrasing, CONSTRAINT MATRIX). R11 is on rubric v9 (v25 trace-state) — 31 criteria including the new C-30 (criterion-instruction fusion) and C-31 (sub-criterion element decomposition). The R10 role-protocol apparatus doesn't map to v9 at all, so R11 starts fresh.

---

# trace-state Variate — Round 11
**Date:** 2026-03-15
**Rubric:** v9 / trace-state v25 (C-01..C-31; golden: all 5 essential pass AND composite ≥ 80)
**Basis:** R10 operated on rubric v8. R11 is the first generation on rubric v9, which adds C-30 (criterion-instruction fusion in field labels) and C-31 (sub-criterion element decomposition). Both new criteria require structural embedding of compliance instructions directly into field labels — a pattern that v8 CONSTRAINT MATRIX variants partially approached but never made the scoring object. R11 objective: explore the structural space of v9, establish coverage of C-30 and C-31, and identify which variation axes best support the new criteria alongside the existing 29.

---

## R11 Variation Map

| Var | Axis | Primary Aspirationals Targeted | Hypothesis |
|-----|------|-------------------------------|------------|
| V-01 | Role sequence: Finance → CS → Sales | C-13, C-25, C-26, C-22, C-27 | Finance-first seeding produces richer cross-domain invariant synthesis; derivation linkage emerges more naturally when the richest state machine domain runs first |
| V-02 | Output format: numbered steps with sub-element labels | C-31, C-11, C-15, C-24, C-22 | Step-block format enables sub-criterion decomposition (C-31) and inline criterion anchoring (C-11) without requiring columnar schema; example step demonstrates `…` placeholder syntax (C-15) |
| V-03 | Lifecycle emphasis: race section 2× structural weight | C-12, C-21, C-28, C-23, C-29 | Dedicating a four-sub-section race schema to concurrent analysis forces symmetric interleaving (C-12), named operations (C-28), anti-lazy-copy declaration (C-21), and active mutation verification (C-29) |
| V-04 | Phrasing register (conversational) + Inertia framing | C-18, C-20, C-27, C-16, C-19 | Accessible "what your state docs miss" framing gives natural anchoring for invariant quality requirements (C-18/C-20/C-27) and consequence declarations (C-19) without the formalism needed to achieve C-30/C-31 |
| V-05 | Schema-first + criterion-instruction fusion | C-30, C-31, C-14, C-11, C-19 | Embedding criterion IDs alongside behavioral directives in every field label (C-30) and decomposing multi-element criteria into labeled sub-elements (C-31) makes compliance structurally unavoidable (C-14); first live test of C-30/C-31 coexistence |

---

## V-01 — Role Sequence: Finance → CS → Sales

**Axis:** Role sequence (single-axis)
**Hypothesis:** Starting with Finance (deepest invariant space — invoice lifecycle, credit memos, payment states) seeds higher-quality invariant candidates that CS and Sales passes can validate and extend. Cross-domain derivation linkage (C-13) and invariant aggregation (C-25) are more natural when the domain with the richest state machine runs first.

---

You are a state domain expert. Hand-compile state transitions across three business domains in this order: **Finance → Customer Service → Sales**.

Each domain pass is independent. Do not blend domain vocabulary across passes.

---

### Output Format

For each domain pass, produce a **State Transition Table**:

| Step | Starting State | Operation | Preconditions | Ending State | Postconditions | Invariants Checked |
|------|---------------|-----------|---------------|-------------|----------------|-------------------|

**Rules applying to every table:**
- Every row must complete all seven columns. Write `none` if Preconditions or Postconditions are genuinely absent — never leave these blank.
- Starting State must differ from Ending State in at least one property per row.
- Invariants Checked must list at least the invariants active for that operation — not a column you may leave empty.
- Minimum **5 rows per domain pass**. Minimum **15 rows total** across all three passes.
- No prose substitutions. A row replaced with a narrative paragraph invalidates the artifact.
- Uniform table format throughout all three domain passes.

After each transition table, declare the invariants for that domain in a subsection:

#### Invariants Declared — [Domain]

List at least 2 invariants. Requirements:
- Must encode real business rules specific to the domain. "Invoice amount must remain positive after creation" qualifies.
- Disqualifying patterns — these do not count: `"ID is not null"`, `"record exists"`, `"amount field is populated"`, `"status field is set"`. An invariant matching any of these patterns will not be scored.
- For each invariant, record which Step row(s) in the transition table above caused you to identify it — e.g., "Derived From: Step 3". This derivation note is required; invariants without derivation references are not linked to the trace.

---

### Domain Pass 1 — Finance

States to trace: Invoice lifecycle (Draft → Submitted → Approved → Paid → Void), credit memo states (Open → Applied → Void), payment states (Pending → Cleared → Returned).

Compile a representative Finance scenario — at least 5 operations in the invoice or payment lifecycle.

---

### Domain Pass 2 — Customer Service

States to trace: Ticket lifecycle (Open → Assigned → In Progress → Resolved → Closed → Reopened), escalation states, SLA status.

Compile a representative CS scenario — at least 5 operations.

---

### Domain Pass 3 — Sales

States to trace: Opportunity lifecycle (Prospect → Qualified → Proposal → Negotiation → Closed-Won / Closed-Lost), contract states, account states.

Compile a representative Sales scenario — at least 5 operations.

---

### Defect Register

Minimum 1 entry. For each defect:
- Defect type
- Triggering operation
- Reason

Silent omissions from this section invalidate the section.

---

### Invariant Register

Aggregate all invariants from all three passes into a single register. For each entry:

| Invariant Statement | Domain | Derived From |
|--------------------|---------|-----------------------------|
| [invariant] | Finance / CS / Sales | [pass name + step number, e.g., "Finance Step 3"] |

The Derived From column must be populated for every entry. An invariant listed without a derivation reference is not cross-domain traceable and does not contribute to synthesis.

---

### Negative Path Trace

For at least one domain, trace one rejected operation:
- Invalid starting state
- Blocked operation
- Unchanged ending state
- Named error

Write `none` for Preconditions in the negative path row if there are no applicable preconditions. After the trace, actively confirm no state mutation occurred — this is not satisfied by recording the unchanged state; it requires an explicit verification statement.

---

### Race Condition Analysis

Name the two concurrent operations: **Op A: ___ / Op B: ___**

Describe both orderings:

**Ordering 1 (A executes first, then B):** [full interleaving — describe state at each transition step]
Conflict or resolution: ___

**Ordering 2 (B executes first, then A):** [full interleaving — describe independently; do not write "same as above" or reference Ordering 1]
Conflict or resolution: ___

---

**Output sequence:** Finance table + invariants → CS table + invariants → Sales table + invariants → Defect Register → Invariant Register → Negative Path Trace → Race Condition Analysis.

---
---

## V-02 — Output Format: Numbered Steps with Sub-Element Labels

**Axis:** Output format (single-axis)
**Hypothesis:** Replacing table rows with labeled step blocks enables C-31 (sub-criterion element decomposition) and C-11 (inline criterion anchoring) without requiring columnar schema. Each step becomes a self-contained auditable unit with individually labeled sub-elements. An example step using `…` placeholder syntax demonstrates the format before generation begins (C-15) and is guarded against literal copy (C-24).

---

You are a state domain expert. Hand-compile state transitions for three business domains — **Sales, Customer Service, Finance** — using numbered step blocks. Each step is a fully labeled, self-contained unit.

---

### Step Format

Each numbered step uses this exact structure:

**Step N — [Operation Name]**
- Starting State `[C-01a]`: ___
- Operation Applied `[C-01b]`: ___
- Preconditions `[C-02a — write "none" if genuinely absent]`: ___
- State Changes `[C-01c]`: ___
- Ending State `[C-01d]`: ___
- Postconditions `[C-02b — write "none" if genuinely absent]`: ___
- Invariants Checked `[C-03 — minimum 2 per pass; never omit]`: ___

> **Example step — do not reproduce in output:**
> **Step 1 — Submit Invoice for Approval**
> - Starting State `[C-01a]`: Invoice in Draft status, amount $500, all required fields complete
> - Operation Applied `[C-01b]`: Finance rep submits invoice to approval queue
> - Preconditions `[C-02a]`: Amount > 0; all required fields populated; invoice not previously submitted
> - State Changes `[C-01c]`: status Draft → Submitted; submitted_at timestamp set; approval_queue entry created
> - Ending State `[C-01d]`: Invoice in Submitted status, awaiting approval
> - Postconditions `[C-02b]`: approval_queue contains this invoice; submitted_at ≤ current timestamp
> - Invariants Checked `[C-03]`: (1) Invoice amount remains positive after state change; (2) submitted_at cannot precede created_at

Rules:
- Minimum 5 steps per domain pass. Minimum 15 steps total.
- All sub-elements must be filled in every step — `none` for Preconditions or Postconditions if genuinely absent.
- No prose substitutions. A step block replaced with narrative invalidates the artifact.
- Uniform step format throughout all three passes.

---

### Domain Pass 1 — Sales

States: Prospect, Qualified, Proposal, Negotiation, Closed-Won, Closed-Lost.

Produce at least 5 numbered steps for a representative Sales opportunity lifecycle.

**Invariants Declared — Sales**
At least 2 invariants. Must encode real Sales business rules — "Deal value must remain positive at Closed-Won" qualifies; "ID is not null" does not.
- Acceptable example: "Opportunity close date cannot be earlier than creation date"
- Disqualifying patterns: `"ID is not null"`, `"record exists"`, `"amount field is populated"`
- For each invariant: cite the step number(s) that revealed it.

---

### Domain Pass 2 — Customer Service

States: Open, Assigned, In Progress, Resolved, Closed, Reopened.

Produce at least 5 numbered steps. Invariants section: same requirements as Pass 1.

---

### Domain Pass 3 — Finance

States: Draft, Submitted, Approved, Paid, Void (invoice). Open, Applied, Void (credit memo).

Produce at least 5 numbered steps. Invariants section: same requirements as Pass 1.

---

### Defect Entry `[C-04]`

Minimum 1 entry. Use this sub-element structure:

- Defect type `[C-04a]`: ___
- Triggering operation `[C-04b]`: ___
- Reason `[C-04c]`: ___

---

### Negative Path Trace `[C-09]`

For one domain, one rejected operation. Sub-element structure:

- Invalid Starting State `[C-09a]`: ___
- Blocked Operation `[C-09b]`: ___
- Unchanged Ending State `[C-09c]`: ___
- Named Error `[C-09d]`: ___

After filling the above, explicitly confirm: no state mutation occurred as a result of this rejection.

Silent omissions from this section invalidate the section.

---

### Race Condition Analysis

Name the concurrent operations: **Op A: ___ / Op B: ___**

**Ordering 1 (A first, then B):** [describe full interleaving as numbered sub-steps]
Conflict or resolution: ___

**Ordering 2 (B first, then A):** [describe independently — do not write "same as above" or cross-reference Ordering 1]
Conflict or resolution: ___

---
---

## V-03 — Lifecycle Emphasis: Race Condition Section 2× Structural Weight

**Axis:** Lifecycle emphasis (single-axis)
**Hypothesis:** Giving the race condition section a four-sub-section schema — identification, Ordering 1, Ordering 2, asymmetry analysis — forces symmetric interleaving (C-12), explicitly named concurrent operations (C-28), the anti-lazy-copy declaration within the section (C-21), and section-level invalidation consequence (C-23). Active mutation verification in the negative path section (C-29) completes the coverage.

---

You are a state domain expert. Hand-compile state transitions for three business domains — **Sales, Customer Service, Finance** — with expanded treatment of concurrent operation analysis.

---

### State Transition Tables

Produce one table per domain pass. Minimum 5 rows per pass, 15 rows total.

| Step | Starting State | Operation | Preconditions | Ending State | Postconditions | Invariants Checked |
|------|---------------|-----------|---------------|-------------|----------------|-------------------|

Rules:
- Every column filled in every row. Preconditions and Postconditions: write `none` if genuinely absent.
- Starting State ≠ Ending State in at least one property per row.
- Invariants Checked: at least 2 domain-meaningful invariants declared and checked per pass.
- Invariants must encode real business rules — "Invoice amount must remain positive after creation" qualifies; "ID is not null" does not.
- No prose substitutions. Uniform table format throughout.

After each table, list the declared invariants for that domain with a derivation note (cite the Step row that generated each invariant).

---

### Defect Register

Minimum 1 entry. Columns: Defect type | Triggering operation | Reason.

---

### Negative Path Trace

For at least one domain, trace one rejected operation:
- Invalid starting state
- Blocked operation
- Unchanged ending state
- Named error

Actively confirm no mutation occurred — this requires an explicit verification statement, not merely recording the pre-operation state.

---

### Race Condition Analysis

This section uses four sub-sections. Complete all four.

#### RC-1: Concurrent Operation Identification

Name the two concurrent operations under analysis:
- **Op A:** ___ (domain, operation name, starting state)
- **Op B:** ___ (domain, operation name, starting state)

A race condition section that does not explicitly name both operations in this sub-section does not satisfy the concurrent-operation identification requirement. Silent omissions from this sub-section invalidate this section.

#### RC-2: Ordering 1 — A executes first, then B

Describe the full state interleaving for this ordering:
- State before A executes: ___
- State after A executes (before B begins): ___
- State after B executes: ___
- Conflict or resolution for this ordering: ___

#### RC-3: Ordering 2 — B executes first, then A

Describe the full state interleaving for this ordering **independently**. Do not write "same as above." Do not reference RC-2. Each ordering must be fully and independently described — a cross-reference to the other ordering does not satisfy this sub-section.

- State before B executes: ___
- State after B executes (before A begins): ___
- State after A executes: ___
- Conflict or resolution for this ordering: ___

#### RC-4: Asymmetry Analysis

Compare RC-2 and RC-3:
- Are the conflict outcomes the same or different for both orderings?
- If different: describe the asymmetric behavior and its business impact.
- If the same: explain why the conflict is ordering-invariant.

---

**Output sequence:** Sales table + invariants → CS table + invariants → Finance table + invariants → Defect Register → Negative Path Trace → Race Condition Analysis (RC-1 through RC-4).

---
---

## V-04 — Phrasing Register: Conversational + Inertia Framing

**Axis:** Phrasing register (conversational) + Inertia framing (combined)
**Hypothesis:** Framing the prompt around "what your current state documentation misses" produces more practitioner-grounded artifacts. The conversational register makes invariant quality requirements (C-18/C-20/C-27) feel like substantive guidance rather than compliance rules. Consequence declarations (C-19/C-16) sit more naturally in conversational framing than in schema-first formats.

---

Most state documentation describes states. It rarely traces what happens when you move between them — what has to be true before an operation fires, what changes, and what has to remain true once it completes. When two operations run at the same time, that documentation offers almost nothing. When an operation is called on an invalid state, most specs are silent about what the system should do and whether anything changed.

This exercise closes that gap. You're going to trace the actual transitions — step by step, operation by operation — for three business domains: Sales, Customer Service, and Finance. If any part of this output is replaced with prose paragraphs instead of structured trace data, the artifact is invalid and cannot be used for feature decision-making.

---

**For each domain, produce a transition table.**

Walk through at least 5 operations. For each one, fill every column. If preconditions or postconditions are genuinely absent, write `none` — a blank cell is not the same as no precondition:

| Step | Starting State | Operation | Preconditions | Ending State | Postconditions | Invariants Checked |

At least 5 rows per domain, 15 rows total. Same table format throughout — no mixing styles between domains.

**On invariants:** These are the business rules that can never be broken regardless of what operation runs. You need at least 2 per domain. Here's the bar: "Invoice amount must remain positive after creation" qualifies. That's a rule the business would call a violation if broken.

These patterns do not count — if your invariants match any of them, go deeper:
- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`
- `"status field is set"`

And here's a positive example so the bar is concrete: "Opportunity close date cannot precede the date the opportunity was created" — that's a real business constraint that an invoice total being positive mirrors.

For each invariant you declare, note which step row in the transition table caused you to identify it. That derivation link is what makes the invariant register useful.

---

**What breaks it?**

After your traces, cover two failure modes.

**Defects:** At least one operation that hits a defect. What type of defect is it? What operation triggered it? Why did it happen?

**Rejected operation:** Pick one operation that should fail. Show the invalid starting state, the operation that was attempted, that the state is unchanged after the rejection, and the error that fires. Then actively confirm that no mutation occurred — don't just record the before-state; explicitly state that you verified no change happened. An output that shows the unchanged state without a verification statement doesn't satisfy this requirement.

---

**What happens when two operations collide?**

Pick two operations that could plausibly run concurrently. Name both of them — Op A is ___, Op B is ___. Unnamed concurrent operations don't qualify.

Then trace both orderings — A first then B, and B first then A. Write both out in full. Do not reference one from the other. "Same as above" is not an answer here, because the outcomes are often not the same, and that asymmetry is exactly what this analysis is designed to surface.

Name the conflict or resolution in each ordering.

---

**Output order:**
1. Sales transition table + invariants (with derivation notes)
2. CS transition table + invariants (with derivation notes)
3. Finance transition table + invariants (with derivation notes)
4. Defect register
5. Rejected operation trace (with explicit mutation verification)
6. Race condition analysis (both orderings, fully independent descriptions)

---
---

## V-05 — Schema-First + Criterion-Instruction Fusion

**Axis:** Output format (schema-first) + criterion-instruction fusion (combined)
**Hypothesis:** Embedding criterion IDs alongside behavioral directives in field labels (C-30) and decomposing multi-element criteria into individually labeled sub-elements (C-31) makes compliance structurally unavoidable (C-14) — filling a cell satisfies the criterion without consulting the rubric. First live test of C-30 + C-31 coexistence alongside C-11 (IDs present), C-14 (schema-level enforcement), and C-19 (artifact invalidation clause).

---

You are a state domain expert. The schema below is the contract for this artifact. Field labels carry criterion IDs and behavioral directives — these are compliance requirements embedded at the point of use. Fill every field exactly as its label specifies.

---

### Section 1: State Transition Table `[C-01: starting state, operation, ending state in every row — never omit]` `[C-06: uniform format throughout all three passes]`

Produce one table per domain pass (Sales → Customer Service → Finance). Minimum 5 rows per pass, 15 rows total across all three passes `[C-17: minimum 5 rows per pass]` `[C-26: minimum 15 rows total — cross-pass floor]`.

| Step `[C-01a]` | Starting State `[C-01b: must differ from Ending State in ≥1 property]` | Operation `[C-01c]` | Preconditions `[C-02a: write "none" if genuinely absent — never blank]` | Ending State `[C-01d]` | Postconditions `[C-02b: write "none" if genuinely absent — never blank]` | Invariants Checked `[C-03: minimum 2 per pass — never skip]` |

> **Example row — do not reproduce in output:**
> | 1 | Invoice in Draft, amount $500… | Submit for Approval | Amount > 0…; required fields complete… | Invoice in Submitted… | approval_queue contains this invoice… | (1) Amount remains positive after…; (2) submitted_at ≤ current timestamp… |

No prose substitutions anywhere in this table. A cell filled with narrative instead of structured data invalidates the artifact `[C-16: no prose substitutions]` `[C-19: violation invalidates the artifact]`.

---

### Section 2: Invariants Declared `[C-03: minimum 2 per pass — never skip]` `[C-07: real business rules only]`

After each transition table, produce an invariant list. For each entry:

| Invariant Statement `[C-07: encode real domain business rules]` | Domain Pass | Derived From `[C-13: cite step row — e.g., "Step 3"]` |

**Qualifying example** (this is the bar): "Invoice amount must remain positive after creation" `[C-20]`

**Exclusion list** — these patterns do not qualify `[C-18]` `[C-27: enumerated exclusion set]`:
- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`
- `"status field is set"`

A Derived From cell left blank disqualifies the invariant from cross-domain synthesis.

---

### Section 3: Defect Register `[C-04: minimum 1 entry — silent omissions invalidate this section]`

| Defect type `[C-04a]` | Triggering operation `[C-04b]` | Reason `[C-04c]` |

Silent omissions from this section invalidate this section `[C-23: section-level invalidation]`.

---

### Section 4: Negative Path Trace `[C-09: minimum 1 entry — silent omissions invalidate this section]`

| Invalid Starting State `[C-09a]` | Blocked Operation `[C-09b]` | Unchanged Ending State `[C-09c]` | Named Error `[C-09d]` | Mutation Verification `[C-29: actively confirm no state changed — recording unchanged state without verification does not qualify]` |

Silent omissions from this section invalidate this section `[C-23]`.

---

### Section 5: Race Condition Analysis `[C-08: minimum 1 interleaving — never skip]`

**Named concurrent operations** `[C-28: both operations must be named — an unnamed operation disqualifies this section]`:
- Op A: ___
- Op B: ___

**Ordering 1 (A executes first, then B)** `[C-12a: describe full interleaving independently]`:

| Phase `[C-12a-i]` | State `[C-12a-ii]` | Notes `[C-12a-iii]` |

Conflict or resolution for this ordering: ___

**Ordering 2 (B executes first, then A)** `[C-12b: describe independently — do not write "same as above"; do not reference Ordering 1]` `[C-21: anti-cross-reference — each ordering must be fully self-contained]`:

| Phase `[C-12b-i]` | State `[C-12b-ii]` | Notes `[C-12b-iii]` |

Conflict or resolution for this ordering: ___

---

### Section 6: Invariant Register `[C-25: aggregate all invariants from all passes with cross-pass derivation linkage]`

| Invariant Statement | Domain | Derived From `[C-13: cite pass name and step row — e.g., "Finance Step 2"]` |

The Derived From column is required for every entry. Invariants without derivation linkage are not aggregate-traceable.

---

### Domain Passes

Run in this order: **Sales → Customer Service → Finance**

**Sales:** Opportunity lifecycle (Prospect, Qualified, Proposal, Negotiation, Closed-Won, Closed-Lost); contract states; account states.

**Customer Service:** Ticket lifecycle (Open, Assigned, In Progress, Resolved, Closed, Reopened); escalation states; SLA status.

**Finance:** Invoice lifecycle (Draft, Submitted, Approved, Paid, Void); credit memo states (Open, Applied, Void); payment states (Pending, Cleared, Returned).

Complete every schema section for each domain pass before advancing to the next. Fill the schema — do not substitute narrative for any section.

---

## Criterion Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Essential | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-02** Essential | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-03** Essential | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-04** Essential | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-05** Essential | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-06** Recommended | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-07** Recommended | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-08** Recommended | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-09 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-11 | — | ✓ | — | — | ✓ |
| C-12 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-13 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-14 | — | — | — | — | ✓ |
| C-15 | — | ✓ | — | — | ✓ |
| C-16 | — | — | ✓ | ✓ | ✓ |
| C-17 | ✓ | ✓ | ✓ | — | ✓ |
| C-18 | — | ✓ | — | ✓ | ✓ |
| C-19 | — | — | — | ✓ | ✓ |
| C-20 | ✓ | ✓ | — | ✓ | ✓ |
| C-21 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-22 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-23 | ✓ | ✓ | ✓ | — | ✓ |
| C-24 | — | ✓ | — | — | ✓ |
| C-25 | ✓ | — | — | — | ✓ |
| C-26 | ✓ | ✓ | ✓ | — | ✓ |
| C-27 | ✓ | ✓ | — | ✓ | ✓ |
| C-28 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-29 | ✓ | ✓ | ✓ | ✓ | ✓ |
| **C-30** New | — | — | — | — | ✓ |
| **C-31** New | — | ✓ | — | — | ✓ |

**Notes:**
- V-05 is the only variation targeting C-30 and C-31 simultaneously. R12 can test whether they can be separated.
- V-01 is the only variation targeting C-25 (Invariant Register with cross-pass derivation); the Finance-first ordering provides the strongest basis for cross-domain synthesis.
- V-03's RC-4 asymmetry sub-section is the structural innovation for this round; no prior trace-state variation has included an explicit asymmetry comparison step after symmetric interleaving.
- V-04 is the diagnostic variation — if it scores lower on C-14/C-30/C-31 and higher on C-18/C-19/C-20, that confirms these criterion families require different structural approaches.
