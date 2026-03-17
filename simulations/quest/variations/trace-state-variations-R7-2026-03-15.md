## trace-state R7 — Five Variation Prompts (v21 rubric)

---

### V-01 — Output Format: Hard Schema with Embedded Criterion IDs
**Axis**: Output format
**Hypothesis**: Embedding criterion IDs directly into column headers (C-14) combined with a filled example row (C-15) pulls C-11 automatically and makes artifact compliance structurally unavoidable rather than instruction-dependent. Co-locating nil instructions at the column header level (C-22) and adding an artifact-invalidation clause (C-19) round out the schema-enforcement cluster.

---

You are a **Finance / Customer Service / Sales state domain expert** hand-compiling a state transition trace for the feature described in the input.

**Compliance rule**: Every structural field must be filled using the schema below. Substituting prose for a structural column **invalidates the artifact** — reviewers will reject it and request resubmission. If a field has no applicable value, write `none`; do not leave it blank or replace it with a sentence.

---

## Section A: State Transition Trace [C-01 · C-02 · C-03 · C-06 · C-17]

**Minimum 5 rows.** One row per operation. Filling any cell mechanically satisfies the labeled criterion.

| # [C-01] | Starting State [C-01a] | Operation [C-01b] | Ending State [C-01c] | Preconditions [C-02a — write `none` if genuinely absent] | Postconditions [C-02b — write `none` if genuinely absent] | Invariants Checked [C-03] |
|---|---|---|---|---|---|---|
| 1 | … | … | … | … | … | … |

**Example row** (do not include in output — shows correct cell content):

| 2 | PendingApproval | ApproveInvoice | Approved | Approver role assigned; invoice total > 0 | Status = Approved; notification sent to requester | Invoice amount must remain positive after creation; approver must hold Finance role |

---

## Section B: Declared Invariants [C-03 · C-07 · C-18 · C-20]

Declare at least **two domain-meaningful invariants** that hold after every relevant operation.

| Invariant ID | Statement | Domain | Checked After Operations |
|---|---|---|---|
| INV-01 | … | Finance / CS / Sales | Op 1, Op 3, … |

**Disqualifying patterns** (these entries invalidate the row): structural non-rules such as "ID is not null", "record exists", "timestamp is set". Naming a role category ("Finance-relevant") without a concrete statement also does not qualify.

**Qualifying example**: "Invoice amount must remain positive after creation" — this is valid because it encodes a lifecycle constraint on a domain entity, not a structural database property.

---

## Section C: Defect Log [C-04]

At least one entry. Use this structure; no prose substitutions:

| Defect # | Type | Triggering Operation | Reason |
|---|---|---|---|
| D-01 | [invalid state transition \| missing precondition check \| invariant violation \| race condition] | … | … |

---

## Section D: Race Condition Analysis [C-08 · C-12 · C-21]

Choose one operation pair that can execute concurrently.

**Instructions**: Describe both orderings in full and independently. Do not write "same as above" in the second ordering — each ordering must stand alone. The purpose of describing both is to surface asymmetric outcomes; referencing one ordering from the other defeats this. If both orderings genuinely produce identical outcomes, describe both fully and state explicitly what property guarantees symmetry.

**Ordering A → B**

| Field | Value |
|---|---|
| Actor A starting state | … |
| Actor B starting state | … |
| A executes | … |
| State after A | … |
| B executes | … |
| Final state | … |
| Conflict / resolution | … |

**Ordering B → A**

| Field | Value |
|---|---|
| Actor B starting state | … |
| Actor A starting state | … |
| B executes | … |
| State after B | … |
| A executes | … |
| Final state | … |
| Conflict / resolution | … |

Conflict type: [lost update \| dirty read \| phantom read \| deadlock \| none — state reason]

---

## Section E: Negative Path [C-09]

| Field | Value [write `none` if genuinely absent] |
|---|---|
| Invalid starting state | … |
| Blocked operation | … |
| State after rejection (must equal starting state) | … |
| Named error | … |

---

## Section F: Reachability Note [C-10]

List every transition you omitted and why. Silent omissions **invalidate this section**.

| Omitted Transition | Reason |
|---|---|
| … | … |

---

## Input

{{FEATURE_DESCRIPTION}}

---
---

### V-02 — Role Sequence: Finance → CS → Sales
**Axis**: Role sequence (Finance leads)
**Hypothesis**: Leading with Finance primes high-invariant-density thinking — Finance states carry strong monetary lifecycle constraints — before reaching the looser Sales domain. This increases the probability of domain-meaningful invariants (C-07) and cross-domain invariant candidates (C-13) appearing naturally in the trace rather than being forced in post-hoc.

---

You are hand-compiling a state transition analysis in three sequential domain passes. Each pass contributes its perspective to the same underlying feature. Finance runs first because its invariants tend to be the strongest anchors for the full trace.

---

## Pass 1: Finance Lens

You are a Finance domain expert. Finance states involve monetary amounts, approval workflows, payment lifecycle, and audit trail requirements.

### State Transition Table — Finance Operations

Minimum 3 Finance operations. For each row:

| # | Starting State | Operation | Ending State | Preconditions [write `none` if genuinely absent] | Postconditions [write `none` if genuinely absent] | Invariant Candidates |
|---|---|---|---|---|---|---|

**On invariants**: Record the business rule pattern you observe, even tentatively. Do not write structural properties ("ID is not null", "record exists"). A valid qualifying example: "Invoice amount must remain positive after creation" — this encodes a Finance lifecycle constraint, not a database property.

After the table: declare your **two strongest Finance invariants** and the row(s) each was derived from.

---

## Pass 2: Customer Service Lens

You are a Customer Service domain expert. CS states involve ticket status, escalation tiers, SLA windows, and resolution stages.

### State Transition Table — CS Operations

Same format as Pass 1. Minimum 3 CS operations.

After the table: identify any invariant that **crosses Finance and CS domains** — for example, a customer should not be billed while a billing dispute ticket is open. If no cross-domain invariant applies to this feature, write `none — no cross-domain invariant applies` (do not leave blank).

---

## Pass 3: Sales Lens

You are a Sales domain expert. Sales states involve opportunity stages, contract status, quota attribution, and close conditions.

### State Transition Table — Sales Operations

Same format as Pass 1. Minimum 3 Sales operations.

After the table: flag any Sales state that should prevent a Finance operation from proceeding (or vice versa). If none apply, write `none`.

---

## Consolidated Invariant Register

Across all three passes, declare the final invariant set:

| Invariant ID | Statement | Derived From (row refs) | Domain | Business Rule Encoded |
|---|---|---|---|---|
| INV-01 | … | Pass 1 R2, Pass 2 R1 | Finance/CS | … |

Minimum 2. Each must trace back to at least one row from the passes above.

---

## Defect Log

At least one defect found during any pass:

| Defect # | Type | Triggering Operation | Reason |
|---|---|---|---|
| D-01 | [invalid state transition \| missing precondition check \| invariant violation \| race condition] | … | … |

---

## Race Condition Analysis

Choose one concurrent operation pair from any domain.

Describe both orderings **in full and independently** — write out each completely. Do not write "same as above" or refer the second ordering to the first. Each must stand alone because the purpose is to surface asymmetric outcomes.

**Ordering A → B**: [complete walk-through, all fields]

**Ordering B → A**: [complete walk-through, written independently, not by reference to the above]

Conflict type (if any): [lost update \| dirty read \| phantom read \| deadlock \| none — reason]

---

## Negative Path

One rejected operation from any domain:

| Field | Value [write `none` if genuinely absent] |
|---|---|
| Invalid state | … |
| Blocked operation | … |
| State after rejection (unchanged) | … |
| Named error | … |

---

## Input

{{FEATURE_DESCRIPTION}}

---
---

### V-03 — Lifecycle Emphasis: Invariant Derivation Pipeline as Organizing Spine
**Axis**: Lifecycle emphasis (derivation pipeline foregrounded, C-13 as structural backbone)
**Hypothesis**: Making the derivation pipeline the explicit two-stage structure of the prompt — forward trace first, invariant extraction second with mandatory row citations — produces traceable cross-references (C-13) at higher rates than prompts where invariants are declared independently alongside the trace.

---

You are a **Sales / Customer Service / Finance state domain expert** hand-compiling a state transition analysis using a two-stage pipeline: observe first, derive second.

The insight behind the pipeline: invariants discovered by watching transitions happen are more grounded than invariants declared from memory. Stage 1 produces the observations. Stage 2 mines them for business rules.

**Hard constraint**: No prose substitutions for structural fields. If a field has no applicable value, write `none`. Replacing a column with a sentence **invalidates the artifact**.

---

## Stage 1: Forward Trace

Build the state transition table. **Minimum 5 rows.**

| Row | Starting State | Operation | Ending State | Preconditions [write `none` if genuinely absent] | Postconditions [write `none` if genuinely absent] | Observed Pattern (invariant candidate) |
|---|---|---|---|---|---|---|
| R1 | … | … | … | … | … | … |
| R2 | … | … | … | … | … | … |

**Observed Pattern column**: Note any business rule pattern visible in this transition — even tentative. For example: "amount decreases only on payment operations", "approval requires role check". Write `none observed` only when no pattern is detectable.

Use states and operations recognizable in your domain:
- **Finance**: invoice lifecycle, payment status, approval stages, audit states
- **Customer Service**: ticket tiers, escalation states, SLA windows, resolution stages
- **Sales**: opportunity stages, contract status, close conditions, quota states

---

## Stage 2: Invariant Derivation

For each invariant you declare, cite the Stage 1 row(s) that generated it. Derivation must be traceable — if you cannot cite a row, the invariant does not qualify.

| Invariant ID | Statement | Derived From (row refs) | Domain | Business Rule Encoded |
|---|---|---|---|---|
| INV-01 | … | R1, R3 | Finance | Invoice amount must remain positive after creation |

**Minimum 2 invariants.** Each must:
- Cite at least one Stage 1 row
- Encode a domain business rule

**Disqualifying patterns**: "ID is not null", "record exists", "timestamp is set" — structural properties, not business rules. These entries invalidate the row.

**Qualifying example**: "Invoice amount must remain positive after creation." Valid because it encodes a Finance lifecycle constraint on a domain entity.

After the table: cross-reference these invariants back into Stage 1 by adding their IDs to the Observed Pattern cells of the rows that generated them (annotate inline).

---

## Stage 3: Defect Log

At least one defect discovered by examining transitions and derived invariants:

| Defect # | Type | Triggering Operation | Violates | Reason |
|---|---|---|---|---|
| D-01 | [invalid state transition \| missing precondition check \| invariant violation \| race condition] | … | INV-01 / precondition in R2 / … | … |

---

## Stage 4: Race Condition Analysis

Choose one operation pair that can execute concurrently.

Describe **both orderings in full** — write each independently. Do not write "same as above" or reference the first ordering from the second. The point of describing both is to detect asymmetric outcomes; that detection fails if one ordering defers to the other.

**Ordering A → B**:
- A's starting state:
- B's starting state:
- A executes — state changes:
- B executes — state changes:
- Final state and conflict or resolution:

**Ordering B → A**:
- B's starting state:
- A's starting state:
- B executes — state changes:
- A executes — state changes:
- Final state and conflict or resolution:

Conflict type: [lost update \| dirty read \| phantom read \| deadlock \| none — explain]

---

## Stage 5: Negative Path

| Field | Value [write `none` if genuinely absent] |
|---|---|
| Invalid state | … |
| Blocked operation | … |
| State after rejection (must equal starting state) | … |
| Named error | … |

---

## Stage 6: Reachability Note

Transitions omitted from Stage 1 and why:

| Omitted Transition | Reason |
|---|---|
| … | … |

Silent omissions invalidate this section.

---

## Input

{{FEATURE_DESCRIPTION}}

---
---

### V-04 — Phrasing Register: Conversational Expert Voice + Inertia Framing
**Axis**: Phrasing register (first-person expert, conversational) + inertia framing (existing system as baseline with known gaps)
**Hypothesis**: Grounding the trace in "what the current system gets wrong" (inertia framing) gives the LLM a concrete anchor for generating defects and preconditions, while conversational register reduces over-formalization and produces more realistic state descriptions. This combination targets C-04, C-05, and C-07 together without requiring schema-heavy format machinery.

---

You've been brought in as a domain expert — Finance, Customer Service, or Sales, whichever fits the feature best — to review a new capability before it gets approved.

The reason your review matters: the existing system handling this workflow has known edge cases. The new feature has to cover them explicitly. That means you need to trace the state transitions with enough precision that reviewers can see every place where the new feature either fixes a gap or introduces a new one.

Here's what you'll produce.

---

## 1. State Transition Trace

Walk through the feature's operations in order. For each one, give:

**Starting state → Operation → Ending state**

Plus, for each operation:
- **Preconditions** — what has to be true before this can run. If there are none, write `none` (not a blank, not a sentence that says "no preconditions apply").
- **Postconditions** — what is guaranteed true afterward. If there are none, write `none`.
- **Invariants** — business rules that hold after this operation runs.

On invariants: these are the interesting ones. "Invoice amount must remain positive after creation" — that's a good invariant, because it says something real about what the Finance domain allows. "ID is not null" — that's not useful, it's structural. Write the ones that would actually catch a bug.

Trace at least **5 operations**. A trace with fewer is not detailed enough for approval.

Use a consistent format throughout — table, numbered steps, or structured prose — but don't mix them.

---

## 2. What the current system gets wrong

You found at least one defect while tracing. Tell reviewers:
- What kind of defect is it? (invalid state transition / missing precondition check / invariant violation / race condition)
- Which operation triggered it?
- Why is it a defect — which rule does it violate, and what goes wrong?

If you found more than one, list them all.

---

## 3. Race condition walk-through

The existing system almost certainly has at least one place where two operations can happen concurrently and produce different outcomes depending on which runs first.

Pick one such pair. Walk through both orderings — and write each one out completely. Don't say "same as above" for the second ordering; the whole point is to find out whether the outcomes actually differ. If they don't, say why they're symmetric and what property guarantees that.

**A executes before B:**
[Walk through the full sequence — starting states, what each operation does, final state, and any conflict that emerges.]

**B executes before A:**
[Walk through the full sequence independently — don't reference the walk-through above. Write it from scratch. If the outcomes are different from the A→B case, say so explicitly.]

---

## 4. The rejected case

Trace one operation that should be rejected:
- What state was the system in when the operation was attempted?
- What was attempted?
- What's the state after the rejection? It should be unchanged — confirm this explicitly.
- What error does the system return?

---

## 5. What you didn't trace and why

Any state transitions you chose not to include: list them with a reason. "Out of scope for this feature" is a valid reason — but name it explicitly rather than leaving a silent gap. A trace with unexplained omissions fails review.

---

## The feature to trace

{{FEATURE_DESCRIPTION}}

---
---

### V-05 — Combination: Race Section Expansion + Nil-Value Enforcement + Artifact Invalidation
**Axis**: Output format (artifact invalidation clause, C-19) + lifecycle emphasis (race section fully structured for C-12 and C-21) + nil-value co-location at field level (C-22)
**Hypothesis**: Dedicating a structured, two-table race condition section with an explicit anti-lazy-copy instruction baked into the section header (C-21) produces symmetric interleaving (C-12) at higher rates than a prose-level instruction to "describe both orderings." Pairing this with field-level nil instructions (C-22) and artifact-invalidation language (C-19) captures the three newest criteria together in a single variation.

---

You are a **Customer Service / Sales / Finance state domain expert** hand-compiling a state transition trace for the feature described in the input.

**Compliance rule**: This trace uses a structural schema. Any section that replaces a schema field with prose **invalidates the artifact** — it will be returned without review and must be resubmitted. Fill every field. If a field has no applicable value, write `none` — never leave it blank and never substitute an explanatory sentence.

---

## Section 1: State Transition Trace

**Minimum 5 rows.** One row per operation.

| # | Starting State | Operation | Ending State | Preconditions [write `none` if genuinely absent] | Postconditions [write `none` if genuinely absent] | Invariants Checked |
|---|---|---|---|---|---|---|
| 1 | … | … | … | … | … | … |
| 2 | … | … | … | … | … | … |

**Example row** (exclude from output — shows correct syntax per column):

| 3 | PendingApproval | ApproveInvoice | Approved | Approver role assigned; invoice total > 0 | Status = Approved; notification dispatched | Invoice amount must remain positive after creation; approver must hold Finance role |

---

## Section 2: Declared Invariants

| Invariant ID | Statement | Domain | Checked After Operations |
|---|---|---|---|
| INV-01 | … | Finance / CS / Sales | Op 1, Op 3, … |

**Minimum 2.** Each must encode a real business rule.

Do not declare structural properties — "ID is not null", "record exists", "timestamp is set" — these entries **invalidate the row**.

A qualifying invariant names a domain lifecycle constraint. Example: "Invoice amount must remain positive after creation." This is valid because it encodes a Finance constraint on a domain entity's value across operations, not a database integrity property.

---

## Section 3: Defect Log

| Defect # | Type | Triggering Operation | Reason |
|---|---|---|---|
| D-01 | [invalid state transition \| missing precondition check \| invariant violation \| race condition] | … | … |

Minimum 1 entry. No prose substitutions — violation **invalidates this section**.

---

## Section 4: Race Condition Analysis

Choose one operation pair that can execute concurrently.

**Section rule**: Describe both orderings in full using the tables below. Do not write "same as above" in the second table or reference the first table from the second. Each ordering must be independently complete. The purpose of this section is to detect asymmetric outcomes — that detection fails if one ordering defers to the other. Even if both orderings produce identical outcomes, write both in full and state what property guarantees their symmetry.

**Ordering A → B**

| Field | Value [write `none` if genuinely absent] |
|---|---|
| Actor A — starting state | … |
| Actor B — starting state | … |
| A executes | … |
| State after A completes | … |
| B executes (against post-A state) | … |
| Final state | … |
| Conflict detected / resolution applied | … |

**Ordering B → A**

| Field | Value [write `none` if genuinely absent] |
|---|---|
| Actor B — starting state | … |
| Actor A — starting state | … |
| B executes | … |
| State after B completes | … |
| A executes (against post-B state) | … |
| Final state | … |
| Conflict detected / resolution applied | … |

Conflict type (if any): [lost update \| dirty read \| phantom read \| deadlock \| none — state reason]

Outcome comparison: [symmetric \| asymmetric — describe the difference]

---

## Section 5: Negative Path

| Field | Value [write `none` if genuinely absent] |
|---|---|
| Invalid starting state | … |
| Blocked operation | … |
| State after rejection (must equal starting state — confirm) | … |
| Named error | … |

---

## Section 6: Reachability Note

| Omitted Transition | Reason |
|---|---|
| … | … |

Silent omissions **invalidate this section**. If no transitions were omitted, write one row: `none omitted | full coverage achieved`.

---

## Input

{{FEATURE_DESCRIPTION}}

---

### Variation Summary

| Variation | Primary Axis | Target Criteria | Key Hypothesis |
|---|---|---|---|
| V-01 | Output format — hard schema, embedded IDs | C-11, C-14, C-15, C-19, C-22 | Criterion IDs in column headers make compliance structurally unavoidable |
| V-02 | Role sequence — Finance → CS → Sales | C-07, C-13, C-20 | Finance-first primes invariant quality; cross-domain pass surfaces C-13 |
| V-03 | Lifecycle emphasis — derivation pipeline | C-13, C-18, C-20, C-22 | Two-stage structure with mandatory row citations locks in derivation traceability |
| V-04 | Phrasing register — conversational + inertia | C-04, C-05, C-07 | Existing-system framing produces grounded, realistic defects and states |
| V-05 | Combination — race expansion + nil co-location | C-12, C-19, C-21, C-22 | Structured per-ordering tables with anti-lazy-copy baked into section header captures C-12 + C-21 together |
