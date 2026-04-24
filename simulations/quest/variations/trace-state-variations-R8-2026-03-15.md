## trace-state — Round 8 Variations (rubric v22)

---

## V-01

**Variation axis:** Role sequence — Finance → CS → Sales (reversed from canonical Sales-first order)
**Hypothesis:** Finance's enumerable, ledger-grounded states force precise precondition habits before the model encounters the looser Sales stage states; invariant quality improves because the Finance pass establishes the "real business rule" bar before the other passes run.

---

You are a state-machine analyst. Hand-compile state transitions for a feature operation across three domain passes, in the order prescribed below. Complete each pass fully before beginning the next.

**Domain sequence: Finance → Customer Service → Sales.**
This order is required. Finance leads because its states are enumerable and its invariants are measurable, establishing the rigor baseline the other passes must match.

---

### FORMAT RULES

**Hard constraint — violation invalidates this artifact:** no prose substitutions. Every element must appear in the prescribed schema position. Tables and registers are mandatory throughout. "Prose if brief" is not a valid exception. [C-16, C-19]

**Minimum row count:** the State Transition Table in each pass must contain at least 5 rows. The artifact must contain at least 15 transition rows in total across all passes. [C-17]

---

### PASS 1 — Finance Domain

#### 1.1 State Transition Table [C-01] [C-02] [C-06]

*— Example row. Do not include this row in output. —* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] — write `none` if genuinely absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] — write `none` if genuinely absent [C-22] |
|---|---|---|---|---|
| Invoice:Draft | SubmitForApproval | Balance > 0; approver assigned | Invoice:PendingApproval | Approval request sent; audit trail entry created |

*— End example row. —*

Fill minimum 5 rows for this pass.

#### 1.2 Reachability Annotation [C-10]

Every transition omitted from the table above must appear here with a stated rationale. **Silent omissions invalidate this section.** [C-23]

| Omitted Transition | Rationale for Omission |
|---|---|
| … | … |

#### 1.3 Invariants — Finance Pass [C-03] [C-07] [C-13]

Declare at least two invariants. Each must encode a real Finance business rule — domain-specific, falsifiable, tied to observable business behavior.

**Disqualifying pattern — do not use:** `"ID is not null"`, `"record exists"`, `"amount field is populated"` — structural constraints, not domain invariants. [C-18]

**Qualifying pattern — use as positive model:** `"Invoice total must remain positive from creation through payment; negative totals are never valid in this state machine."` — domain-specific, falsifiable, grounded in Finance policy. [C-20]

For each invariant, record which rows it was derived from. [C-13]

| Invariant [C-03] | Derived From (row refs) [C-13] | Business Rule |
|---|---|---|
| … | Pass 1 R2, Pass 1 R4 | … |

---

### PASS 2 — Customer Service Domain

#### 2.1 State Transition Table [C-01] [C-02] [C-06]

*— Example row. Do not include this row in output. —* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] — write `none` if genuinely absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] — write `none` if genuinely absent [C-22] |
|---|---|---|---|---|
| Case:Open | EscalateToTier2 | Tier-1 resolution attempted; SLA threshold exceeded | Case:Escalated | Tier-2 agent notified; escalation timestamp recorded |

*— End example row. —*

Fill minimum 5 rows for this pass.

#### 2.2 Reachability Annotation [C-10]

**Silent omissions invalidate this section.** [C-23]

| Omitted Transition | Rationale for Omission |
|---|---|
| … | … |

#### 2.3 Invariants — CS Pass [C-03] [C-07] [C-13]

Same disqualifying and qualifying patterns as Pass 1 apply here. At least two invariants. [C-18] [C-20]

| Invariant [C-03] | Derived From (row refs) [C-13] | Business Rule |
|---|---|---|
| … | Pass 2 R1, Pass 2 R3 | … |

---

### PASS 3 — Sales Domain

#### 3.1 State Transition Table [C-01] [C-02] [C-06]

*— Example row. Do not include this row in output. —* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] — write `none` if genuinely absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] — write `none` if genuinely absent [C-22] |
|---|---|---|---|---|
| Opportunity:Qualified | SubmitProposal | Decision-maker identified; budget confirmed | Opportunity:ProposalSent | Proposal record attached; follow-up task created |

*— End example row. —*

Fill minimum 5 rows for this pass.

#### 3.2 Reachability Annotation [C-10]

**Silent omissions invalidate this section.** [C-23]

| Omitted Transition | Rationale for Omission |
|---|---|
| … | … |

#### 3.3 Invariants — Sales Pass [C-03] [C-07] [C-13]

| Invariant [C-03] | Derived From (row refs) [C-13] | Business Rule |
|---|---|---|
| … | Pass 3 R2, Pass 3 R5 | … |

---

### Consolidated Invariant Register [C-25]

After completing all three passes, aggregate every invariant here. At least one row must reference invariants across two different passes.

| Invariant | Domain | Derived From (row refs) [C-25] | Cross-Domain Conflict or Alignment |
|---|---|---|---|
| … | Finance | Pass 1 R2, Pass 2 R1 | … |

---

### Defect Log [C-04]

| Defect ID | Type | Triggering Operation | Reason |
|---|---|---|---|
| D-01 | missing precondition check | … | … |

At least one defect required. `Type` must be one of: `missing precondition check` / `invalid state transition` / `invariant violation` / `race condition`. [C-04]

---

### Negative Path Trace [C-09]

One rejected operation, all four elements required:

| Element | Value |
|---|---|
| Invalid Starting State | … |
| Blocked Operation | … |
| Unchanged Ending State | same as starting state |
| Named Error | … |

---

### Race Condition Analysis [C-08] [C-12] [C-21]

Identify one concurrent operation pair. Describe **both orderings fully and independently**. Do not write "same as above" — each ordering must be self-contained and complete. [C-21]

**Ordering A → B:**

| Step | Actor | Operation | State Before | State After | Note |
|---|---|---|---|---|---|
| 1 | A | … | … | … | … |
| 2 | B | … | … | … | … |

**Ordering B → A:**

| Step | Actor | Operation | State Before | State After | Note |
|---|---|---|---|---|---|
| 1 | B | … | … | … | … |
| 2 | A | … | … | … | … |

Conflict outcome or resolution: …

---

---

## V-02

**Variation axis:** Output format — numbered-step list with named registers (no tables in the transition body)
**Hypothesis:** Forcing numbered-step prose for each transition then requiring those steps to be indexed into a named register tests whether the structural requirements can be met without tables — and whether the register-first aggregation pattern produces stronger cross-pass derivation linkage than table-native formats.

---

You are a state-machine analyst. For each domain, trace state transitions as a numbered operation sequence. After all domain passes complete, aggregate findings into named registers.

**Hard constraints — violation invalidates this artifact:** [C-16] [C-19]
- Every operation must be written as a numbered step in the prescribed format.
- No summary prose may substitute for any required field.
- The Invariant Register and Defect Log are mandatory structures. Omitting either invalidates the artifact.
- Minimum 5 operations per domain pass (15 operations total). [C-17]

**Domain sequence: Sales → Customer Service → Finance.**

---

### PASS 1 — Sales

For each operation, write one numbered step in this format. *— This is the example step. Do not reproduce it in output. —* [C-24]

> **S1.** Starting state: `Opportunity:Qualified` | Operation: `SubmitProposal` [C-01b]
> Preconditions: Decision-maker identified; budget confirmed — write `none` if genuinely absent [C-02a] [C-22]
> Ending state: `Opportunity:ProposalSent` [C-01c]
> Postconditions: Proposal record attached; follow-up task created — write `none` if genuinely absent [C-02b] [C-22]
> Invariant check: [names of invariants checked here, or "see Invariant Register"] [C-03]

*— End example. Do not reproduce above. —*

Write steps S1 through S5 (minimum). Label each `S1`, `S2`, …

**Reachability:** After your steps, list every Sales transition you omitted, with rationale. **Silent omissions invalidate this section.** [C-10] [C-23]

---

### PASS 2 — Customer Service

Write steps C1 through C5 (minimum) using the same format as Pass 1. Label each `C1`, `C2`, …

**Reachability:** List every CS transition omitted, with rationale. **Silent omissions invalidate this section.** [C-10] [C-23]

---

### PASS 3 — Finance

Write steps F1 through F5 (minimum) using the same format as Pass 1. Label each `F1`, `F2`, …

**Reachability:** List every Finance transition omitted, with rationale. **Silent omissions invalidate this section.** [C-10] [C-23]

---

### Invariant Register [C-03] [C-07] [C-13] [C-25]

Aggregate all invariants from all passes here. At least two invariants per domain. Each invariant must encode a real business rule — domain-specific and falsifiable.

**Disqualifying pattern — do not use:** `"ID is not null"`, `"status field is set"` — structural, not domain invariants. [C-18]
**Qualifying pattern — use as positive model:** `"An opportunity cannot move to Closed:Won without a signed contract reference."` — observable, domain-grounded, falsifiable. [C-20]

| Invariant ID | Invariant Statement [C-03] | Domain | Derived From (step refs) [C-13] [C-25] | Cross-Domain Note |
|---|---|---|---|---|
| INV-01 | … | Sales | S2, C1 | … |
| INV-02 | … | Finance | F1, F3 | … |

At least one row must reference steps from two different passes in the `Derived From` column. [C-25]

---

### Defect Log [C-04]

| Defect ID | Type | Triggering Step | Reason |
|---|---|---|---|
| D-01 | … | … | … |

At least one defect required. Type must be: `missing precondition check` / `invalid state transition` / `invariant violation` / `race condition`.

---

### Negative Path Trace [C-09]

One rejected operation:

- **Invalid starting state:** …
- **Blocked operation:** …
- **Unchanged ending state:** same as starting state
- **Named error:** …

---

### Race Condition Analysis [C-08] [C-12]

Identify one concurrent operation pair. Write both orderings as numbered step sequences. **Describe each ordering independently and completely. Do not write "same as above" or refer to the other ordering by reference.** [C-21]

**Ordering A → B:**

> A1. Actor A executes `[operation]` from state `[before]` → state `[after]`
> A2. Actor B executes `[operation]` from state `[before]` → state `[after]`
> Conflict / resolution: …

**Ordering B → A:**

> B1. Actor B executes `[operation]` from state `[before]` → state `[after]`
> B2. Actor A executes `[operation]` from state `[before]` → state `[after]`
> Conflict / resolution: …

---

---

## V-03

**Variation axis:** Phrasing register — direct second-person imperative throughout; no meta-commentary, no passive constructions
**Hypothesis:** Stripping all hedging and meta-framing reduces the model's tendency to substitute explanation for structure; imperative phrasing at each field label makes each step feel like a fill-in-the-blank task rather than a reasoning exercise, improving schema compliance.

---

You are compiling a state trace. Work through three domains: Sales, Customer Service, Finance. Each domain gets its own pass. Finish one pass completely before starting the next.

**These rules apply to every section. Breaking any of them invalidates the artifact.** [C-19]

- Write tables. No prose substitutions. [C-16]
- Write at least 5 rows per domain transition table. [C-17]
- Write `none` in any precondition or postcondition cell where the answer is genuinely absent. Do not leave cells blank. [C-22]

---

### Sales Pass

**Step 1 — Fill the transition table.**

For each row: write the starting state, the operation, the preconditions (or `none`), the ending state, the postconditions (or `none`). [C-01] [C-02]

*Below is an example row. Remove it from your output before submitting.* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] — `none` if absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] — `none` if absent [C-22] |
|---|---|---|---|---|
| Opportunity:Qualified | SubmitProposal | Decision-maker confirmed; budget locked | Opportunity:ProposalSent | Proposal attached; follow-up scheduled |

Write at least 5 rows, labeled R1–R5.

**Step 2 — List every transition you skipped.** [C-10]

For every Sales transition that belongs in this table but isn't there, name it and explain why you left it out. **Leaving a transition out without explanation invalidates this section.** [C-23]

| Omitted Transition | Why You Skipped It |
|---|---|

**Step 3 — Write your invariants.** [C-03] [C-07]

Name at least two invariants. Make them real Sales business rules — something a Sales manager would recognize as policy.

Do not write things like `"ID is not null"` or `"record exists"`. Those are structural facts, not business rules. [C-18]

A good invariant looks like this: `"A closed-lost opportunity cannot be re-opened without a manager override."` — specific, tied to observed Sales behavior, falsifiable. [C-20]

For each invariant, name which rows caused you to declare it. [C-13]

| Invariant [C-03] | Came From (row refs) [C-13] | Business Rule It Encodes [C-07] |
|---|---|---|
| … | Sales R2, Sales R4 | … |

---

### Customer Service Pass

**Step 1 — Fill the transition table.** [C-01] [C-02]

Same format as Sales. Write at least 5 rows, labeled R1–R5.

*Below is an example row. Remove it from your output.* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] — `none` if absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] — `none` if absent [C-22] |
|---|---|---|---|---|
| Case:Open | EscalateToTier2 | Tier-1 tried; SLA threshold crossed | Case:Escalated | Tier-2 notified; priority updated |

**Step 2 — List every transition you skipped.** [C-10]
**Leaving a transition out without explanation invalidates this section.** [C-23]

| Omitted Transition | Why You Skipped It |
|---|---|

**Step 3 — Write your invariants.** [C-03] [C-07] [C-13] [C-18] [C-20]

Same rules as Sales pass. At least two invariants.

| Invariant [C-03] | Came From (row refs) [C-13] | Business Rule It Encodes [C-07] |
|---|---|---|

---

### Finance Pass

**Step 1 — Fill the transition table.** [C-01] [C-02]

Same format. Write at least 5 rows, labeled R1–R5.

*Below is an example row. Remove it from your output.* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] — `none` if absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] — `none` if absent [C-22] |
|---|---|---|---|---|
| Invoice:Draft | SubmitForApproval | Balance > 0; approver assigned | Invoice:PendingApproval | Approval queued; audit entry written |

**Step 2 — List every transition you skipped.** [C-10]
**Leaving a transition out without explanation invalidates this section.** [C-23]

| Omitted Transition | Why You Skipped It |
|---|---|

**Step 3 — Write your invariants.** [C-03] [C-07] [C-13] [C-18] [C-20]

| Invariant [C-03] | Came From (row refs) [C-13] | Business Rule It Encodes [C-07] |
|---|---|---|

---

### Invariant Register — All Domains [C-25]

Now bring all invariants together in one place. At least one entry must reference rows from two different passes. [C-25]

| Invariant | Domain | Came From (row refs) [C-13] [C-25] | Conflict With Other Domains? |
|---|---|---|---|
| … | Sales | Sales R2, CS R1 | … |

---

### Defects [C-04]

Write at least one defect you found.

| ID | Type | Where | Why It's a Defect |
|---|---|---|---|
| D-01 | missing precondition check | … | … |

Type: `missing precondition check` / `invalid state transition` / `invariant violation` / `race condition`.

---

### Negative Path [C-09]

Pick one operation that should be rejected. Write all four:

| | |
|---|---|
| State it starts from | … |
| Operation attempted | … |
| State it ends in | same as starting state — no change |
| Error raised | … |

---

### Race Conditions [C-08] [C-12]

Pick one concurrent pair. Write each ordering as its own complete sequence. **Do not write "same as above" or "mirrors the above."** Write each one from scratch. [C-21]

**If A goes first:**

| # | Who | Does | Before | After |
|---|---|---|---|---|
| 1 | A | … | … | … |
| 2 | B | … | … | … |

Outcome: …

**If B goes first:**

| # | Who | Does | Before | After |
|---|---|---|---|---|
| 1 | B | … | … | … |
| 2 | A | … | … | … |

Outcome: …

---

---

## V-04

**Variation axes (combo):** Role sequence (CS → Finance → Sales) + lifecycle emphasis (explicit forbidden-transition phase after each pass, mandatory before moving to next domain)
**Hypothesis:** Inserting a required "forbidden transitions" phase at the end of each domain pass — listing operations that must never occur in this domain regardless of state — surfaces a category of defect (illegal state transition) that only appears when the analyst is forced to think about the negative space of the state machine before moving on. Combined with CS-first ordering, which introduces ambiguous states (escalation, hold, re-open) early, this forces explicit precondition reasoning before the more rigorous Finance domain validates the model.

---

You are a state-machine analyst. Trace state transitions domain-by-domain. Between passes, complete a mandatory **Forbidden Transitions** audit before advancing to the next domain. Skipping the audit between passes invalidates the artifact. [C-19]

**Domain sequence: Customer Service → Finance → Sales.**

**Hard constraints (any violation invalidates the artifact):** [C-16] [C-19]
- Tables are required. No prose substitutions.
- Write `none` in any Preconditions or Postconditions cell where genuinely absent. Do not leave cells blank. [C-22]
- Each transition table must contain at least 5 rows. [C-17]
- Reachability sections must list every omitted transition with a rationale. Silent omissions invalidate the reachability section. [C-10] [C-23]

---

### PASS 1 — Customer Service

#### Transition Table [C-01] [C-02] [C-06]

*— Example row. Do not include this row in your output. —* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] `none` if absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] `none` if absent [C-22] |
|---|---|---|---|---|
| Case:Open | EscalateToTier2 | Tier-1 resolution attempted; SLA crossed | Case:Escalated | Tier-2 notified; case priority set to High |

*— End example. —*

Minimum 5 rows. Label them CS-R1 through CS-R5+.

#### Reachability [C-10]

List every CS transition omitted from the table above. **Silent omissions invalidate this section.** [C-23]

| Omitted Transition | Rationale |
|---|---|

#### Forbidden Transitions — CS Phase [C-04]

List at least two CS state transitions that must never occur regardless of inputs. For each, name the invariant or business rule that prohibits it.

| Forbidden Transition (From → To) | Prohibiting Rule | Defect Type If Attempted |
|---|---|---|
| Case:Resolved → Case:Escalated | Cannot escalate after resolution; resolution is terminal | invalid state transition |

These entries feed the Defect Log. [C-04]

#### Invariants — CS Pass [C-03] [C-07] [C-13]

**Disqualifying pattern:** `"ID is not null"`, `"status is set"` — not domain invariants. [C-18]
**Qualifying pattern:** `"A resolved case may not re-enter any active state without explicit customer re-open request."` [C-20]

| Invariant [C-03] | Derived From (row refs) [C-13] | Business Rule |
|---|---|---|
| … | CS-R1, CS-R3 | … |

---

### PASS 2 — Finance

#### Transition Table [C-01] [C-02] [C-06]

*— Example row. Do not include this row in your output. —* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] `none` if absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] `none` if absent [C-22] |
|---|---|---|---|---|
| Invoice:Approved | IssuePayment | Bank account verified; payment amount ≤ approved amount | Invoice:Paid | Payment record created; ledger entry posted |

*— End example. —*

Minimum 5 rows. Label them FI-R1 through FI-R5+.

#### Reachability [C-10]

**Silent omissions invalidate this section.** [C-23]

| Omitted Transition | Rationale |
|---|---|

#### Forbidden Transitions — Finance Phase [C-04]

| Forbidden Transition | Prohibiting Rule | Defect Type If Attempted |
|---|---|---|
| Invoice:Paid → Invoice:Draft | Payments are final; retroactive voiding requires a separate credit memo | invalid state transition |

#### Invariants — Finance Pass [C-03] [C-07] [C-13]

Same disqualifying and qualifying standards apply. [C-18] [C-20]

| Invariant [C-03] | Derived From (row refs) [C-13] | Business Rule |
|---|---|---|
| … | FI-R2, FI-R4 | … |

---

### PASS 3 — Sales

#### Transition Table [C-01] [C-02] [C-06]

*— Example row. Do not include this row in your output. —* [C-24]

| Starting State [C-01a] | Operation [C-01b] | Preconditions [C-02a] `none` if absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] `none` if absent [C-22] |
|---|---|---|---|---|
| Opportunity:Qualified | SubmitProposal | Decision-maker identified; budget confirmed | Opportunity:ProposalSent | Proposal attached; next-step task created |

*— End example. —*

Minimum 5 rows. Label them SA-R1 through SA-R5+.

#### Reachability [C-10]

**Silent omissions invalidate this section.** [C-23]

| Omitted Transition | Rationale |
|---|---|

#### Forbidden Transitions — Sales Phase [C-04]

| Forbidden Transition | Prohibiting Rule | Defect Type If Attempted |
|---|---|---|
| Opportunity:Closed:Won → Opportunity:Qualified | A won opportunity cannot regress to qualification; requires new opportunity record | invalid state transition |

#### Invariants — Sales Pass [C-03] [C-07] [C-13]

| Invariant [C-03] | Derived From (row refs) [C-13] | Business Rule |
|---|---|---|
| … | SA-R1, SA-R3 | … |

---

### Consolidated Invariant Register [C-25]

Aggregate all invariants from all three passes. At least one entry must carry derivation references spanning two different passes.

| Invariant | Domain | Derived From (row refs) [C-13] [C-25] | Cross-Domain Alignment or Conflict |
|---|---|---|---|
| … | CS + Finance | CS-R2, FI-R1 | … |

---

### Defect Log [C-04]

Incorporate defects surfaced from Forbidden Transitions audits and from trace analysis.

| Defect ID | Type | Source (row or forbidden transition ref) | Reason |
|---|---|---|---|
| D-01 | invalid state transition | CS Forbidden-T1 | … |

---

### Negative Path Trace [C-09]

| Element | Value |
|---|---|
| Invalid Starting State | … |
| Blocked Operation | … |
| Unchanged Ending State | same as starting state |
| Named Error | … |

---

### Race Condition Analysis [C-08] [C-12] [C-21]

Pick one concurrent operation pair. Write both orderings as independent, complete descriptions. **Do not write "same as above" or describe one ordering by reference to the other. Each ordering must stand alone.** [C-21]

**Ordering A → B:**

| Step | Actor | Operation | State Before | State After |
|---|---|---|---|---|
| 1 | A | … | … | … |
| 2 | B | … | … | … |

Conflict or resolution: …

**Ordering B → A:**

| Step | Actor | Operation | State Before | State After |
|---|---|---|---|---|
| 1 | B | … | … | … |
| 2 | A | … | … | … |

Conflict or resolution: …

---

---

## V-05

**Variation axes (combo):** Schema-level write-time enforcement (C-14) + quantified floors embedded in column headers
**Hypothesis:** If every column header carries a criterion ID *and* a measurability instruction (e.g., "min 5 rows declared here"), the model cannot fill the schema without satisfying the criterion — compliance becomes structurally unavoidable at write time rather than instruction-dependent. This is the maximum C-14 exploitation posture: the schema itself is the rubric.

---

You are a state-machine analyst. Your output is a set of structured registers. The schema below is the complete and mandatory output format. Fill every cell; write `none` for genuinely absent optional values. No prose substitutions anywhere in the output. [C-16]

**Artifact invalidation rule:** any section that is omitted, left as prose, or filled with fewer rows than its declared minimum invalidates the artifact. [C-19]

---

### REGISTER A — State Transitions [C-01] [C-02] [C-06] [C-14]
**Minimum 5 rows per domain; minimum 15 rows total. Row count is auditable here — do not reduce below floor. [C-17]**

*— Example row. Do not include in output. —* [C-24]

| Row [C-06] | Domain [C-05] | Starting State [C-01a] | Operation [C-01b] — no prose fallback [C-16] | Preconditions [C-02a] — write `none` if genuinely absent [C-22] | Ending State [C-01c] | Postconditions [C-02b] — write `none` if genuinely absent [C-22] | Invariants Checked [C-03] — list IDs from Register C |
|---|---|---|---|---|---|---|---|
| SA-R1 | Sales | Opportunity:Qualified | SubmitProposal | Decision-maker confirmed; budget locked | Opportunity:ProposalSent | Proposal attached; follow-up scheduled | INV-01, INV-03 |

*— End example row. —*

Fill rows labeled `SA-R1…`, `CS-R1…`, `FI-R1…` for Sales, Customer Service, Finance respectively. Minimum 5 per domain.

---

### REGISTER B — Reachability [C-10] [C-23] [C-14]
**Every transition omitted from Register A must appear here. Silent omissions invalidate this register. [C-23]**

| Domain [C-05] | Omitted Transition [C-10] — write `none omitted` only if state space is fully covered [C-22] | Rationale for Omission [C-10] — "not relevant" does not qualify |
|---|---|---|
| … | … | … |

---

### REGISTER C — Invariant Register [C-03] [C-07] [C-13] [C-25] [C-14]
**Minimum 2 invariants per domain; minimum 6 rows total. At least 1 row must carry derivation references from 2 different domains. [C-25]**

**Disqualifying pattern — reject these from Register C:** `"ID is not null"`, `"status field populated"`, `"record exists"` — structural, not domain invariants. Any row matching this pattern disqualifies the artifact. [C-18]

**Qualifying pattern — use as positive model for all invariants:** `"Invoice total must remain positive from creation through payment; no operation may produce a non-positive invoice in a valid state machine trace."` [C-20]

*— Example row. Do not include in output. —* [C-24]

| Invariant ID [C-03] | Invariant Statement [C-07] — must be domain-specific and falsifiable [C-18] [C-20] | Domain [C-05] | Derived From (row refs) [C-13] — include at least `Register A row ID` | Cross-Domain Ref [C-25] — `none` if single-domain [C-22] |
|---|---|---|---|---|
| INV-01 | Invoice total must remain positive from creation through payment | Finance | FI-R1, FI-R3 | CS-R2 |

*— End example row. —*

Fill minimum 6 rows.

---

### REGISTER D — Defects [C-04] [C-14]
**Minimum 1 row. Type must be an exact value from the allowed set — no freeform text in the Type column. [C-16]**

*— Example row. Do not include in output. —* [C-24]

| Defect ID [C-04] | Type [C-04] — allowed: `missing precondition check` / `invalid state transition` / `invariant violation` / `race condition` | Triggering Operation (Register A row ref) [C-04] | Reason [C-04] |
|---|---|---|---|
| D-01 | missing precondition check | SA-R3 | No check that opportunity stage is ≥ Qualified before SubmitProposal is accepted |

*— End example row. —*

---

### REGISTER E — Negative Path [C-09] [C-14]
**Exactly 1 row required. All four columns must be filled. [C-09]**

| Invalid Starting State [C-09a] | Blocked Operation [C-09b] | Unchanged Ending State [C-09c] — must equal Invalid Starting State | Named Error [C-09d] |
|---|---|---|---|
| … | … | same as starting state | … |

---

### REGISTER F — Race Conditions [C-08] [C-12] [C-21] [C-14]
**Minimum 1 concurrent pair, both orderings fully described. [C-12]**

**Anti-lazy-copy rule for this register:** describe each ordering independently and completely. Do not write "same as above", "mirrors A→B", or any reference to the other ordering. Each ordering row sequence must be self-contained. Violation of this rule invalidates Register F. [C-21] [C-23]

*— Example row (Ordering A→B). Do not include in output. —* [C-24]

| Ordering [C-12] | Step | Actor | Operation | State Before | State After | Conflict Note |
|---|---|---|---|---|---|---|
| A→B | 1 | A | ApproveInvoice | Invoice:PendingApproval | Invoice:Approved | — |
| A→B | 2 | B | VoidInvoice | Invoice:Approved | Invoice:Voided | Conflict: A approved then B voided — payment record left orphaned |

*— End example. —*

Write both orderings (`A→B` and `B→A`) as independent row sequences. Minimum 2 steps per ordering. Name the conflict or resolution at the end of each ordering's rows.

---

*All six registers are mandatory. Any omitted register invalidates the artifact.* [C-19]

---
