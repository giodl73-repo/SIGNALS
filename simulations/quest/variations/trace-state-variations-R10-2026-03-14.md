## trace-state Skill Variations — Round 10

---

## V-01

**Axis**: Role sequence — upfront multi-phase Standards Registry locked before Phase 1 opens
**Hypothesis**: Publishing all five evidence standards before any detection runs makes every Gap Record auditable against an immutable pre-stated standard rather than a standard post-rationalized from findings; removes the loophole where Role B adjusts its bar to match what was found.

---

```markdown
You are conducting a trace-state analysis. Two roles operate throughout this session:

- **Role A (Analyst)** — builds all declaration tables, runs detection passes, records findings
- **Role B (Standard-Setter)** — locks evidence standards before detection; produces Gap Records

Topic: [TOPIC]
Domain: [Select one → Sales | Customer Service | Finance]

---

## PART 0 — STANDARDS REGISTRY (Role B, unconditional, produce first)

Before Phase 1 opens, Role B must publish and lock the evidence standard for every phase.
This registry is IMMUTABLE once Phase 1 begins. No standard may be revised after findings exist.

For each row, Role B states the minimum evidence required for a finding to count:
"A finding requires [specific artifact] demonstrating [specific condition] at strength ≥ [1/2/3]."

| Phase | Anomaly Type | Role B Evidence Standard (locked before Phase 1) |
|-------|-------------|--------------------------------------------------|
| P1 | Invalid State Transitions | |
| P2 | Missing Precondition Checks | |
| P3 | Invariant Violations | |
| P4 | Race Conditions | |
| P3E | Undeclared References | |

Evidence strength scale: 1 = indirect inference | 2 = direct declaration evidence | 3 = trace-confirmed

> **STANDARDS REGISTRY LOCKED.** Phases P1–P3E are now open to run sequentially.

---

## PART 1 — STATE MACHINE DECLARATION

### State Registry (S-IDs: S-01, S-02, …)
| S-ID | State Name | Entry Conditions | Terminal? |
|------|-----------|-----------------|-----------|

Minimum 5 states. Entry conditions must be state-specific (not "data is valid").

### Operation Registry (OP-IDs: OP-01, OP-02, …)
| OP-ID | Operation | From State | To State | Preconditions | Postconditions |
|-------|-----------|-----------|----------|---------------|----------------|

Minimum 6 operations. Each precondition and postcondition must name a specific state
or field value — no generic statements.

### Invariant Registry (INV-IDs: INV-01, INV-02, …)
| INV-ID | Invariant | Scope | Type | Falsifiable Threshold |
|--------|-----------|-------|------|----------------------|

Minimum 3 invariants. At least one must be numeric or temporal
(e.g., "discount ≤ 40%", "escalation within 24 h of creation").
The falsifiable threshold is the exact condition that, if violated, constitutes a finding.

---

## PART 2 — HAND-COMPILED TRACE (minimum 6 steps, numbered)

For every step:

**Step N — [OP-ID] [OperationName]**
- Before state: S-ID=[…], [key field]=[value], …
- Preconditions checked: [each precondition] → PASS / FAIL
- Operation applied: [exact field mutations]
- After state: S-ID=[…], [key field]=[value], …
- Postconditions verified: [each postcondition] → HOLD / VIOLATED
- Invariants: INV-01 → HOLD | INV-02 → HOLD | INV-03 → VIOLATED at [value]

Assign evidence strength at the moment of discovery — not retroactively.
Do not complete the trace and then assign strengths in batch.

---

## PART 3 — PRE-SWEEP HYPOTHESIS

Before any sweep runs, record predictions:

| Phase | Predicted Finding Count | Confidence (H / M / L) |
|-------|------------------------|------------------------|
| P1 – Invalid State Transitions | | |
| P2 – Missing Precondition Checks | | |
| P3 – Invariant Violations | | |
| P4 – Race Conditions | | |
| P3E – Undeclared References | | |

State which phase you expect to be most productive and why.

---

## ANOMALY SWEEP
### Phases run sequentially. Phase N+1 is LOCKED until Phase N emits COMPLETE.

---

### PHASE 1: INVALID STATE TRANSITIONS [STATUS: OPEN]

**Dual-mode detection** — run both passes independently:

**Pass 1 — Declaration-Only**: Examine the Operation Registry. For each OP, is the
From-State → To-State pair a declared valid transition in the State Registry?

**Pass 2 — Trace-Diff**: Examine each Step N. Does the actual Before-State → After-State
match the OP-Registry entry for that OP-ID? Is the declared From-State what the trace shows?

Sweep table:
| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

A "None" in either column requires an inline gap record in that cell:
"No [Pass 1 / Pass 2] evidence because [name the specific trace steps, state conditions,
or registry entries that would need to exist to produce a finding here]."

**Evidence Strength Exit Gate:**
☐ At least one finding at strength ≥ 2, OR Role B Gap Record explicitly states why
  no finding met the P1 standard declared in Part 0.

**Role B Gap Record** (unconditional — required even when findings exist):
Document: (a) which transitions were examined and cleared; (b) what evidence would
have satisfied the P1 standard locked in Part 0; (c) what this phase cannot determine.
The Gap Record is the exit gate unlock signal.

> **PHASE 1: COMPLETE** [Unlocks Phase 2]

---

### PHASE 2: MISSING PRECONDITION CHECKS [STATUS: LOCKED → OPEN on Phase 1 COMPLETE]

**Role B pre-detection evidence standard commitment for P2:**
(Reference the P2 row locked in Part 0. Restate it here as a single sentence.)

**Dual-mode detection:**

**Pass 1 — Declaration-Only**: Examine OP-Registry preconditions. Which OPs lack a precondition
entirely? Which have a precondition that is underspecified (no named state or field value)?

**Pass 2 — Trace-Diff**: Examine each Step N. Does the trace verify each declared precondition,
or does any step skip, abbreviate, or assume a precondition rather than explicitly checking it?

Sweep table:
| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

(Inline gap record for any "None" cell, as above)

**Evidence Strength Exit Gate:** ☐ (same criterion, referencing P2 standard)

**Role B Gap Record** (unconditional):

> **PHASE 2: COMPLETE** [Unlocks Phase 3]

---

### PHASE 3: INVARIANT VIOLATIONS [STATUS: LOCKED → OPEN on Phase 2 COMPLETE]

**Role B pre-detection evidence standard commitment for P3:**
(Reference Part 0 P3 row. Restate as single sentence.)

**Dual-mode detection:**

**Pass 1 — Declaration-Only**: Examine INV-Registry. Does each invariant have a falsifiable
threshold? Which operations in OP-Registry have no documented invariant check declared?

**Pass 2 — Trace-Diff**: Examine each Step N invariant row. Any VIOLATED verdict? Any invariant
from INV-Registry that applies to a step but is not checked there?

Sweep table:
| Finding-ID | INV-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|--------|-------------------------|-----|--------------------|-----|

(Inline gap record for any "None" cell)

**Evidence Strength Exit Gate:** ☐

**Role B Gap Record** (unconditional):

> **PHASE 3: COMPLETE** [Unlocks Phase 4]

---

### PHASE 4: RACE CONDITIONS [STATUS: LOCKED → OPEN on Phase 3 COMPLETE]

**Role B pre-detection evidence standard commitment for P4:**
(Reference Part 0 P4 row. Restate as single sentence.)

**Dual-mode detection:**

**Pass 1 — Declaration-Only**: Examine OP-Registry. Which OPs mutate shared state?
Which lack a concurrency precondition? Which have a check-then-act gap where the precondition
could be invalidated between its evaluation and the operation's execution?

**Pass 2 — Trace-Diff**: For each candidate OP pair identified in Pass 1, construct a minimal
two-thread interleaving. Does the interleaving produce a state inconsistency, a stale-read, or
a double-commit?

Sweep table:
| Finding-ID | OP-IDs | Declaration-Only Finding | Str | Trace-Diff (interleaving scenario) | Str |
|-----------|--------|-------------------------|-----|-------------------------------------|-----|

(Inline gap record for any "None" cell)

**Evidence Strength Exit Gate:** ☐

**Role B Gap Record** (unconditional):

> **PHASE 4: COMPLETE** [Unlocks Phase 3E]

---

### PHASE 3E: UNDECLARED REFERENCES [STATUS: LOCKED → OPEN on Phase 4 COMPLETE]

Phase 3E is a full sequential peer of Phases 1–4 — not a verification gate item.

**Role B pre-detection evidence standard commitment for P3E:**
(Reference Part 0 P3E row. Restate as single sentence.)

**Dual-mode detection:**

**Pass 1 — Declaration-Only**: Cross-reference all three registries against each other.
Scan: (a) operation names in OP-Registry for state names absent from S-Registry;
(b) invariant INV-IDs referenced in OP conditions but absent from INV-Registry;
(c) roles or field names appearing in conditions but never formally declared.

**Pass 2 — Trace-Diff**: Cross-reference trace steps against all three registries.
Scan: (a) state names in Before/After fields absent from S-Registry;
(b) OP-IDs in step headers absent from OP-Registry;
(c) INV-IDs in invariant rows absent from INV-Registry.

Sweep table:
| Finding-ID | Reference | Missing From | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-----------|-------------|-------------------------|-----|-------------------|-----|

(Inline gap record for any "None" cell)

**Evidence Strength Exit Gate:** ☐

**Role B Gap Record** (unconditional):

> **PHASE 3E: COMPLETE**

---

## PART 4 — RECONCILIATION TABLE

| Phase | Predicted | Actual | Outcome (C / FP / FN) | Surprising? | Explanation |
|-------|-----------|--------|----------------------|-------------|-------------|

Calibration score = Correct predictions / Total predictions.
If score < 0.5: perform structural diagnosis — which assumption about the domain model was wrong,
and what would a better hypothesis have required you to look for first?

---

## PART 5 — MASTER ANOMALY REGISTER

| Finding-ID | Type | OP-ID | S-ID | INV-ID | Evidence Str | Phase |
|-----------|------|-------|------|--------|-------------|-------|

A blank cell in any non-inapplicable column of a found-verdict row is a detectable
structural gap. "N/A" is acceptable only when the ID class genuinely does not apply
to the anomaly type (e.g., INV-ID on a race condition without a named invariant).
```

---

## V-02

**Axis**: Output format — schema-first declaration (all registries fully built and cross-referenced before any trace step runs)
**Hypothesis**: Forcing complete domain-model commitment before the trace begins prevents the analyst from adding or modifying declarations in response to what the trace reveals, producing a cleaner separation between what was declared and what was found.

---

```markdown
You are conducting a trace-state analysis. Your analysis has two committed phases:
the **Declaration Phase** (Parts 0–2) and the **Analysis Phase** (Parts 3–7).
The Declaration Phase must be fully complete before any trace step or sweep begins.

Topic: [TOPIC]
Domain: [Select one → Sales | Customer Service | Finance]

Roles:
- **Role A (Analyst)**: builds declaration tables; runs trace; runs detection passes
- **Role B (Standard-Setter)**: challenges declarations for completeness; commits evidence
  standards; produces Gap Records

---

## DECLARATION PHASE

### PART 0 — ENTITY AND LIFECYCLE SETUP

Choose a realistic entity with a multi-stage lifecycle. Examples by domain:
- Sales: SalesOpportunity, SalesContract, Quota
- CS: SupportTicket, EscalationCase, CustomerAccount
- Finance: Invoice, PurchaseOrder, ExpenseReport

State the entity name, describe the lifecycle in one sentence, and identify
the actor(s) who trigger state transitions.

---

### PART 1 — STATE REGISTRY

**Role A builds; Role B challenges each entry for missing entry conditions.**

| S-ID | State Name | Entry Conditions | Terminal? | Notes |
|------|-----------|-----------------|-----------|-------|

Rules:
- Minimum 5 states. S-IDs: S-01, S-02, …
- Entry conditions must be state-specific predicates, not generic phrases.
  Bad: "record is valid". Good: "amount > 0 AND approver is assigned".
- Terminal states may not be From-State in any OP-Registry row.
- Role B must challenge any entry condition that is ambiguous before Part 2 begins.

---

### PART 2 — OPERATION REGISTRY

**Role A builds; Role B challenges for missing or underspecified preconditions.**

| OP-ID | Operation | From State | To State | Preconditions | Postconditions | Roles Authorized |
|-------|-----------|-----------|----------|---------------|----------------|-----------------|

Rules:
- Minimum 6 operations. OP-IDs: OP-01, OP-02, …
- From-State and To-State must match S-IDs from Part 1. Any deviation is a P3E signal.
- Each precondition must name a specific field, value, or state condition.
- Postconditions must be verifiable from the after-state alone.
- Role B flags any OP with no precondition or a postcondition that restates
  the operation rather than the guaranteed outcome state.

**Transition Matrix** (cross-reference check — fill after OP-Registry is complete):
Rows = From-States, Columns = To-States. Cell value = OP-ID or "—" if no direct transition.

|  | S-01 | S-02 | S-03 | S-04 | S-05 |
|---|------|------|------|------|------|
| S-01 | — | | | | |
| S-02 | | — | | | |
…

Any cell with more than one OP-ID is a conflict candidate — note it before the trace begins.

---

### PART 3 — INVARIANT REGISTRY

**Role A declares; Role B challenges each invariant for falsifiability.**

| INV-ID | Invariant | Scope | Type | Falsifiable Threshold | Associated OPs |
|--------|-----------|-------|------|----------------------|---------------|

Rules:
- Minimum 3 invariants. INV-IDs: INV-01, INV-02, …
- Type: numeric | temporal | structural | relational
- At least 1 numeric or temporal invariant with an exact threshold.
  Bad: "price is reasonable". Good: "discount ≤ 40% of list price".
- Falsifiable Threshold: the exact value or condition whose violation constitutes a finding.
- Associated OPs: which OP-IDs must check this invariant (leave blank only if INV applies globally).
- Role B challenges any invariant that cannot be checked from a single state snapshot.

---

### PART 4 — DECLARATION CROSS-CHECK (Role B, unconditional)

Before the trace begins, Role B performs and signs off:

☐ Every From-State in OP-Registry appears in S-Registry
☐ Every To-State in OP-Registry appears in S-Registry
☐ Every INV-ID in Associated-OPs column matches an INV-Registry row
☐ At least one numeric or temporal invariant is present
☐ No operation has an empty precondition column
☐ No entry condition in S-Registry is a generic phrase

List any declaration gap found here. If none, state: "No declaration gaps found."
Explanation must name the specific registries and rows examined — not "looks complete."

> **DECLARATION PHASE COMPLETE.** Analysis Phase may now begin.

---

## ANALYSIS PHASE

### PART 5 — HAND-COMPILED TRACE (minimum 6 steps, numbered)

For every step:

**Step N — [OP-ID] [OperationName]**
- Before state: S-ID=[…], [key field]=[value], …
- Preconditions: [OP-Registry preconditions] → PASS / FAIL for each
- Operation applied: [exact field mutations]
- After state: S-ID=[…], [key field]=[value], …
- Postconditions: [each] → HOLD / VIOLATED
- Invariants: INV-01 → HOLD | INV-02 → HOLD | INV-03 → VIOLATED at [value]
- Evidence strength noted now: [1 / 2 / 3] — assigned at point of discovery

---

### PART 6 — PRE-SWEEP HYPOTHESIS

| Phase | Predicted Finding Count | Confidence |
|-------|------------------------|-----------|
| P1 – Invalid State Transitions | | |
| P2 – Missing Precondition Checks | | |
| P3 – Invariant Violations | | |
| P4 – Race Conditions | | |
| P3E – Undeclared References | | |

---

### PART 7 — ANOMALY SWEEP (sequential, each phase LOCKED until previous COMPLETE)

Each phase follows identical structure:

1. **Role B pre-detection commitment** (per phase, before detection runs):
   "For [phase type], I require [specific artifact] demonstrating [specific condition]
   at strength ≥ [1/2/3]. This standard is locked for this phase."

2. **Dual-mode sweep table**:
   | Finding-ID | ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
   A "None" cell requires inline gap text naming what would need to exist for a finding.

3. **Evidence Strength Exit Gate**: ☐ ≥1 finding at strength ≥ 2, OR Role B Gap Record
   explains why the standard could not be met.

4. **Role B Gap Record** (unconditional): Documents what was cleared, what was not found,
   and what this phase cannot determine. The Gap Record is the unlock signal.

5. **PHASE N: COMPLETE** declaration (required artifact to unlock next phase).

---

**PHASE 1: INVALID STATE TRANSITIONS** [OPEN]
Role B pre-detection commitment:

Pass 1 (Declaration-Only) — check Transition Matrix and OP-Registry for undeclared or
conflicting From→To pairs:

Pass 2 (Trace-Diff) — check each Step N Before-State → After-State against OP-Registry
From/To fields:

| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 1: COMPLETE**

---

**PHASE 2: MISSING PRECONDITION CHECKS** [LOCKED → OPEN]
Role B pre-detection commitment:

Pass 1 (Declaration-Only) — scan OP-Registry for empty or underspecified preconditions:
Pass 2 (Trace-Diff) — scan trace steps for skipped or abbreviated precondition checks:

| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 2: COMPLETE**

---

**PHASE 3: INVARIANT VIOLATIONS** [LOCKED → OPEN]
Role B pre-detection commitment:

Pass 1 (Declaration-Only) — scan INV-Registry for un-falsifiable thresholds; scan
OP-Registry for OPs with no associated invariant check:
Pass 2 (Trace-Diff) — scan trace step invariant rows for VIOLATED verdicts or
unchecked invariants at steps where they apply:

| Finding-ID | INV-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|--------|-------------------------|-----|--------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 3: COMPLETE**

---

**PHASE 4: RACE CONDITIONS** [LOCKED → OPEN]
Role B pre-detection commitment:

Pass 1 (Declaration-Only) — scan OP-Registry for OPs with shared-state mutations and
no concurrency precondition; identify check-then-act gaps:
Pass 2 (Trace-Diff) — construct minimal two-thread interleaving for each candidate pair;
show the interleaved step sequence and resulting state:

| Finding-ID | OP-IDs | Declaration-Only Finding | Str | Trace-Diff (interleaving) | Str |
|-----------|--------|-------------------------|-----|---------------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 4: COMPLETE**

---

**PHASE 3E: UNDECLARED REFERENCES** [LOCKED → OPEN] (fifth peer phase, not a gate item)
Role B pre-detection commitment:

Pass 1 (Declaration-Only) — cross-reference all three registries against each other
for internal undeclared references:
Pass 2 (Trace-Diff) — cross-reference trace text against all three registries for
references in steps that have no registry entry:

| Finding-ID | Reference | Missing From | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-----------|-------------|-------------------------|-----|-------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 3E: COMPLETE**

---

### PART 8 — RECONCILIATION

| Phase | Predicted | Actual | C / FP / FN | Surprising? | Explanation |
|-------|-----------|--------|-------------|-------------|-------------|

Calibration = Correct / Total. If < 0.5: diagnose which declaration assumption was wrong.

---

### PART 9 — MASTER ANOMALY REGISTER

| Finding-ID | Type | OP-ID | S-ID | INV-ID | Evidence Str | Phase |
|-----------|------|-------|------|--------|-------------|-------|
```

---

## V-03

**Axis**: Phrasing register — formal technical imperative with SHALL / SHALL NOT / REQUIRED gate language throughout
**Hypothesis**: Modal verb obligations produce stronger gate compliance than descriptive framing; a model presented with "SHALL NOT advance" behaves differently than one presented with "next phase opens when."

---

```markdown
You SHALL conduct a trace-state analysis conforming to this protocol.
Departure from the protocol structure without explicit justification is a structural error.

Topic: [TOPIC]
Domain: SHALL be one of → Sales | Customer Service | Finance

Two roles SHALL operate throughout this protocol:
- **Role A (Analyst)**: SHALL build all declaration tables, run all detection passes,
  and record all findings.
- **Role B (Standard-Setter)**: SHALL commit evidence standards before each detection
  phase begins; SHALL produce a Gap Record for every phase regardless of finding count.

---

## SECTION 1 — DECLARATION TABLES

### 1.1 State Registry

Role A SHALL produce a State Registry containing a minimum of five states.
Each state SHALL be assigned a unique S-ID (S-01, S-02, …).
Each state SHALL include Entry Conditions expressed as specific state predicates.
Generic entry conditions (e.g., "data is valid") SHALL NOT be accepted.

| S-ID | State Name | Entry Conditions | Terminal? |
|------|-----------|-----------------|-----------|

### 1.2 Operation Registry

Role A SHALL produce an Operation Registry containing a minimum of six operations.
Each operation SHALL be assigned a unique OP-ID (OP-01, OP-02, …).
Every operation SHALL include at least one precondition and one postcondition.
Preconditions and postconditions SHALL reference specific fields or state IDs —
not narrative summaries.
From-State and To-State values SHALL reference S-IDs declared in Section 1.1.
Any reference to an undeclared S-ID SHALL be flagged before the trace begins.

| OP-ID | Operation | From State | To State | Preconditions | Postconditions |
|-------|-----------|-----------|----------|---------------|----------------|

### 1.3 Invariant Registry

Role A SHALL declare a minimum of three invariants.
At least one invariant SHALL be numeric or temporal with a specific threshold value.
Each invariant SHALL include a Falsifiable Threshold — the exact condition whose
violation constitutes a finding.
An invariant without a Falsifiable Threshold SHALL NOT be accepted.

| INV-ID | Invariant | Scope | Type | Falsifiable Threshold |
|--------|-----------|-------|------|----------------------|

---

## SECTION 2 — HAND-COMPILED TRACE

Role A SHALL trace a minimum of six operations in numbered step format.
For each step, Role A SHALL record before-state, precondition verification,
field mutations, after-state, postcondition verification, and invariant check results.
Evidence strength SHALL be assigned at the point of discovery — not retroactively.

**Step N — [OP-ID] [OperationName]**
- Before state: S-ID=[…], [key fields and values]
- Preconditions: [each precondition from OP-Registry] → PASS / FAIL
- Operation applied: [exact field mutations]
- After state: S-ID=[…], [key fields and values]
- Postconditions: [each postcondition] → HOLD / VIOLATED
- Invariants: INV-01 → HOLD | INV-02 → VIOLATED at [specific value]
- Evidence strength (assigned now): [1 / 2 / 3]

---

## SECTION 3 — PRE-SWEEP HYPOTHESIS

Role A SHALL record a prediction for each anomaly phase before the sweep begins.
The sweep SHALL NOT begin until predictions are recorded.

| Phase | Predicted Finding Count | Confidence (H / M / L) |
|-------|------------------------|------------------------|
| P1 | | |
| P2 | | |
| P3 | | |
| P4 | | |
| P3E | | |

---

## SECTION 4 — ANOMALY SWEEP

**Sequential commitment SHALL be enforced.** Phase N+1 SHALL remain LOCKED until
Phase N emits its COMPLETE declaration. Role A SHALL NOT begin Phase N+1 before
Phase N is fully complete.

Each phase SHALL conform to the following structure:

**Step A — Role B evidence standard commitment (SHALL precede all detection):**
Role B SHALL state: "For [phase type], a finding requires [specific artifact]
demonstrating [specific condition] at strength ≥ [1/2/3]."
This standard SHALL be locked for the duration of the phase.
Role B SHALL NOT adjust this standard after findings are known.

**Step B — Dual-mode detection sweep:**
Pass 1 (Declaration-Only): Role A SHALL examine declaration tables for anomalies
in the written specification, independent of the trace.
Pass 2 (Trace-Diff): Role A SHALL diff declared behavior against the actual trace
step sequence. A claim in the declaration not demonstrated in the trace IS a finding.

Sweep table format:
| Finding-ID | [ID type] | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
A "None" entry in any column SHALL be accompanied by an inline gap record naming
the specific steps, registry rows, or state conditions whose absence accounts for
the null result. "None" without explanation SHALL NOT be accepted.

**Step C — Evidence Strength Exit Gate:**
☐ At least one finding at strength ≥ 2 exists in this phase, OR Role B Gap Record
  explicitly states why no finding could satisfy the Phase N standard.
The gate SHALL be checked before Step D. The phase SHALL NOT be declared COMPLETE
while the gate is unchecked.

**Step D — Role B Gap Record (unconditional):**
Role B SHALL produce a Gap Record for every phase, including phases with findings.
The Gap Record SHALL document: (a) which entities were examined and cleared;
(b) what evidence would have been required under the pre-stated standard;
(c) what this phase cannot determine.
The Gap Record is the exit gate unlock signal.
Phase N SHALL NOT emit its COMPLETE declaration until the Gap Record exists.

**Step E — Phase completion declaration:**
> **PHASE N: COMPLETE** [Unlocks Phase N+1]

---

### PHASE 1: INVALID STATE TRANSITIONS [STATUS: OPEN]

Role B evidence standard commitment (SHALL be stated before either pass runs):

Pass 1 (Declaration-Only) — examine Transition Matrix / OP-Registry:
Pass 2 (Trace-Diff) — diff each Step N Before→After against OP-Registry From/To:

| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 1: COMPLETE**

---

### PHASE 2: MISSING PRECONDITION CHECKS [STATUS: LOCKED]
SHALL NOT begin until PHASE 1: COMPLETE is emitted.

Role B evidence standard commitment:

Pass 1 (Declaration-Only) — scan OP-Registry for absent or underspecified preconditions:
Pass 2 (Trace-Diff) — scan trace steps for skipped or implicit precondition checks:

| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 2: COMPLETE**

---

### PHASE 3: INVARIANT VIOLATIONS [STATUS: LOCKED]
SHALL NOT begin until PHASE 2: COMPLETE is emitted.

Role B evidence standard commitment:

Pass 1 (Declaration-Only) — scan INV-Registry for missing thresholds; scan OP-Registry
for operations with no declared invariant check:
Pass 2 (Trace-Diff) — scan trace step invariant rows for violations or unchecked INVs:

| Finding-ID | INV-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|--------|-------------------------|-----|--------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 3: COMPLETE**

---

### PHASE 4: RACE CONDITIONS [STATUS: LOCKED]
SHALL NOT begin until PHASE 3: COMPLETE is emitted.

Role B evidence standard commitment:

Pass 1 (Declaration-Only) — scan OP-Registry for shared-state mutations without
concurrency preconditions; identify check-then-act vulnerabilities:
Pass 2 (Trace-Diff) — construct two-thread interleaving for candidate OP pairs;
SHALL show the interleaved sequence and resulting state explicitly:

| Finding-ID | OP-IDs | Declaration-Only Finding | Str | Trace-Diff (interleaving scenario) | Str |
|-----------|--------|-------------------------|-----|-------------------------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 4: COMPLETE**

---

### PHASE 3E: UNDECLARED REFERENCES [STATUS: LOCKED]
SHALL NOT begin until PHASE 4: COMPLETE is emitted.
This phase IS a full sequential peer of Phases 1–4.
It SHALL NOT be treated as a verification gate item or a subsection of another phase.

Role B evidence standard commitment:

Pass 1 (Declaration-Only) — cross-reference registries against each other:
Pass 2 (Trace-Diff) — cross-reference trace text against all three registries:

| Finding-ID | Reference | Missing From | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-----------|-------------|-------------------------|-----|-------------------|-----|

Evidence Strength Exit Gate: ☐
Role B Gap Record:
> **PHASE 3E: COMPLETE**

---

## SECTION 5 — RECONCILIATION

Role A SHALL compare Part 3 predictions against actual findings.

| Phase | Predicted | Actual | C / FP / FN | Surprising? | Explanation |
|-------|-----------|--------|-------------|-------------|-------------|

Calibration score = Correct / Total.
If calibration < 0.5, Role A SHALL identify the domain assumption that produced
the miscalibration and state what a better hypothesis would have required.

---

## SECTION 6 — MASTER ANOMALY REGISTER

| Finding-ID | Type | OP-ID | S-ID | INV-ID | Evidence Str | Phase |
|-----------|------|-------|------|--------|-------------|-------|

A blank cell in a non-inapplicable column of a found-verdict row SHALL be treated
as a structural gap. "N/A" is acceptable only when the ID class genuinely does not
apply to the anomaly type; that judgment SHALL be stated explicitly.
```

---

## V-04

**Axes**: Role sequence + phrasing register — named-character dialogue (Archivist / Auditor) with per-phase Auditor pre-commitment in conversational format
**Hypothesis**: Named characters with dialogue-turn structure reduce structural omission by making Role B's pre-detection commitment a required turn in an ongoing conversation rather than an optional annotation; the Auditor cannot stay silent at the start of a phase.

---

```markdown
You are running a trace-state analysis as a two-character dialogue session.

**The Archivist** builds all tables, runs detection passes, and records findings.
**The Auditor** challenges standards, commits to evidence thresholds, and produces Gap Records.

Both characters speak in this session. Every section header indicates whose turn it is.
A section cannot close until the named character has spoken.

Topic: [TOPIC]
Domain: [Select one → Sales | Customer Service | Finance]

---

## ACT 1 — DOMAIN SETUP

**Archivist:**
I'll model [entity] in the [domain] domain. Here's the lifecycle.

### State Table
| S-ID | State | Entry Conditions | Terminal? |
|------|-------|-----------------|-----------|
(Minimum 5 states. Entry conditions are state-specific predicates.)

### Operation Table
| OP-ID | Operation | From | To | Preconditions | Postconditions |
|-------|-----------|------|----|---------------|----------------|
(Minimum 6 operations. Preconditions name specific fields or state IDs.)

### Invariant Table
| INV-ID | Invariant | Scope | Type | Falsifiable Threshold |
|--------|-----------|-------|------|----------------------|
(Minimum 3. At least 1 numeric or temporal.)

**Auditor:**
Before we trace anything, let me check your declarations for structural gaps.

Archivist cross-check:
- Every From/To state in OP-Table appears in State Table? [YES / NO — list gaps]
- Every INV-ID referenced in conditions exists in INV-Table? [YES / NO]
- At least one invariant has a numeric or temporal falsifiable threshold? [YES / NO]
- Any operation lacks a precondition or has only a generic one? [YES / NO — list]

I'm satisfied / I flag [specific issues] before we proceed.

---

## ACT 2 — HAND-COMPILED TRACE

**Archivist:**
Here's the trace — [N] steps minimum.

**Step N — [OP-ID] [OperationName]**
- Before: S-ID=[…], [field]=[value]
- Preconditions checked: [each] → PASS / FAIL
- Operation applied: [field mutations]
- After: S-ID=[…], [field]=[value]
- Postconditions: [each] → HOLD / VIOLATED
- Invariants: INV-01=[HOLD], INV-02=[VIOLATED at value X]
- Strength I'm assigning now: [1 / 2 / 3]

(Note: Archivist assigns strength at the moment of discovery — before the Auditor sees it.)

---

## ACT 3 — PRE-SWEEP PREDICTIONS

**Archivist:**
Before the Auditor sets any standards, I'll predict what we'll find.

| Phase | My Predicted Count | Confidence |
|-------|-------------------|-----------|
| P1 – Invalid Transitions | | |
| P2 – Missing Preconditions | | |
| P3 – Invariant Violations | | |
| P4 – Race Conditions | | |
| P3E – Undeclared References | | |

I expect [phase] to be most productive because [reason].

---

## ACT 4 — SWEEP (five phases, sequential)

Each phase opens with the Auditor's standard commitment.
The Archivist cannot begin detection until the Auditor has spoken.
The Auditor's Gap Record is the signal that unlocks the next phase.

---

### PHASE 1 — INVALID STATE TRANSITIONS

**Auditor (speaking before any detection runs):**
For Phase 1, I require: [specific type of evidence] at strength ≥ [1/2/3].
If the Archivist produces a finding, I will check it against this standard.
If a detection pass returns nothing, I need to see what was examined and why that
passes — I won't accept a bare "None."

Standard locked. Archivist, run your passes.

**Archivist — Pass 1 (Declaration-Only):**
I'm checking the Operation Table for From→To pairs that aren't valid transitions in the State Table.

**Archivist — Pass 2 (Trace-Diff):**
Now I'm diffing each step's actual Before→After against what the OP-Table says should happen.

Findings table:
| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |

For any "None" cell: "No evidence here because [name the specific trace steps or registry rows
that were examined and cleared]."

**Evidence Strength Exit Gate:**
☐ At least one finding at strength ≥ 2 — or Auditor explains why the standard couldn't be met.

**Auditor:**
Here's what Phase 1 missed and why the Gap Record matters even with findings:
[Gap Record: what was examined and cleared, what would have been needed, what this phase can't say]

This Gap Record is my signal that Phase 2 can open.

> **PHASE 1: COMPLETE** — Phase 2 is now unlocked.

---

### PHASE 2 — MISSING PRECONDITION CHECKS

**Auditor (speaking before any detection runs):**
For Phase 2, I require: [standard]. Standard locked.

**Archivist — Pass 1 (Declaration-Only):**
Scanning OP-Table for missing or underspecified preconditions.

**Archivist — Pass 2 (Trace-Diff):**
Checking each trace step — does it verify every declared precondition, or skip any?

Findings table:
| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |

(Inline gap text for any "None" cell)

Evidence Strength Exit Gate: ☐

**Auditor:**
[Gap Record]

> **PHASE 2: COMPLETE**

---

### PHASE 3 — INVARIANT VIOLATIONS

**Auditor (speaking before any detection runs):**
For Phase 3, I require: [standard]. Standard locked.

**Archivist — Pass 1 (Declaration-Only):**
Scanning INV-Table for un-falsifiable thresholds; scanning OP-Table for ops with
no declared invariant check.

**Archivist — Pass 2 (Trace-Diff):**
Scanning each step's invariant row — VIOLATED verdicts? Invariants that apply but
weren't checked?

Findings table:
| Finding-ID | INV-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |

(Inline gap text for any "None" cell)

Evidence Strength Exit Gate: ☐

**Auditor:**
[Gap Record]

> **PHASE 3: COMPLETE**

---

### PHASE 4 — RACE CONDITIONS

**Auditor (speaking before any detection runs):**
For Phase 4, I require: [standard — typically a constructed interleaving scenario
showing a specific state inconsistency, strength ≥ 2]. Standard locked.

**Archivist — Pass 1 (Declaration-Only):**
Scanning OP-Table for shared-state mutations with no concurrency precondition;
identifying check-then-act patterns.

**Archivist — Pass 2 (Trace-Diff):**
Constructing two-thread interleavings for candidate OP pairs. Showing the sequence
and the resulting state explicitly.

Findings table:
| Finding-ID | OP-IDs | Declaration-Only Finding | Str | Trace-Diff (interleaving) | Str |

(Inline gap text for any "None" cell)

Evidence Strength Exit Gate: ☐

**Auditor:**
[Gap Record]

> **PHASE 4: COMPLETE**

---

### PHASE 3E — UNDECLARED REFERENCES

This is a full phase, not a checklist item. Same structure as Phases 1–4.

**Auditor (speaking before any detection runs):**
For Phase 3E, I require: [standard]. Standard locked.

**Archivist — Pass 1 (Declaration-Only):**
Cross-referencing all three tables against each other for internal undeclared references.

**Archivist — Pass 2 (Trace-Diff):**
Cross-referencing trace step text against all three tables for unregistered names.

Findings table:
| Finding-ID | Reference | Missing From | Declaration-Only Finding | Str | Trace-Diff Finding | Str |

(Inline gap text for any "None" cell)

Evidence Strength Exit Gate: ☐

**Auditor:**
[Gap Record]

> **PHASE 3E: COMPLETE**

---

## ACT 5 — RECONCILIATION

**Archivist:**
Here's how my predictions held up.

| Phase | I Predicted | Actual | C / FP / FN | Surprising? | What I got wrong |
|-------|------------|--------|-------------|-------------|-----------------|

Calibration = Correct / Total. If < 0.5, I'll say what assumption broke.

---

## ACT 6 — MASTER ANOMALY REGISTER

**Archivist:**
Full register of everything we found.

| Finding-ID | Type | OP-ID | S-ID | INV-ID | Strength | Phase |
|-----------|------|-------|------|--------|---------|-------|
```

---

## V-05

**Axes**: Output format + lifecycle emphasis — mandatory triple-output template per phase with visual block enforcement; schema-first declaration
**Hypothesis**: Making the symmetric output contract physically visible as a three-block template (PRE-COMMITMENT / SWEEP TABLE / GAP RECORD) per phase produces higher compliance with C-33, C-35, C-37 than prose-embedded requirements; a missing block is structurally obvious rather than quietly absent.

---

```markdown
You are conducting a trace-state analysis.

Two roles operate throughout:
- **Role A (Analyst)**: builds all tables, runs trace, runs detection passes, records findings
- **Role B (Standard-Setter)**: commits evidence standards before detection; produces gap records

Topic: [TOPIC]
Domain: [Select one → Sales | Customer Service | Finance]

**Every phase in this analysis produces exactly three outputs, in this order:**

```
┌─────────────────────────────────────────────┐
│ [PHASE N] — PRE-COMMITMENT (Role B)          │
│ Role B states the evidence standard before   │
│ either detection pass begins. Locked.        │
├─────────────────────────────────────────────┤
│ [PHASE N] — SWEEP TABLE (Role A)             │
│ Dual-mode findings table with inline gap     │
│ records for any "None" cell.                 │
├─────────────────────────────────────────────┤
│ [PHASE N] — GAP RECORD (Role B)              │
│ Unconditional. Produced regardless of        │
│ finding count. This block is the unlock      │
│ signal for the next phase.                   │
└─────────────────────────────────────────────┘
```

A phase with any block missing is structurally incomplete. The next phase does not open.

---

## SCHEMA DECLARATION (complete before trace begins)

### State Registry (S-IDs: S-01, S-02, …)
| S-ID | State | Entry Conditions | Terminal? |
|------|-------|-----------------|-----------|

Minimum 5 states. Entry conditions are specific predicates, not generic phrases.

### Operation Registry (OP-IDs: OP-01, OP-02, …)
| OP-ID | Operation | From State | To State | Preconditions | Postconditions |
|-------|-----------|-----------|----------|---------------|----------------|

Minimum 6 operations. All From/To values must be S-IDs from State Registry.

### Invariant Registry (INV-IDs: INV-01, INV-02, …)
| INV-ID | Invariant | Scope | Type | Falsifiable Threshold |
|--------|-----------|-------|------|----------------------|

Minimum 3. At least 1 numeric or temporal with exact threshold.

### Schema Cross-Check (before trace)
Verify: every From/To in OP-Registry appears in State Registry.
Verify: every INV-ID referenced in OP conditions appears in INV-Registry.
List any gap found. If none: "Schema complete — no undeclared references at declaration time."

> **SCHEMA LOCKED. Trace may now begin.**

---

## HAND-COMPILED TRACE (minimum 6 steps)

**Step N — [OP-ID] [OperationName]**
- Before: S-ID=[…], [fields and values]
- Preconditions: [each] → PASS / FAIL
- Applied: [field mutations]
- After: S-ID=[…], [fields and values]
- Postconditions: [each] → HOLD / VIOLATED
- Invariants: INV-01=[HOLD], INV-02=[VIOLATED at value X]
- Strength assigned now: [1 / 2 / 3]

---

## PRE-SWEEP HYPOTHESIS

| Phase | Predicted Count | Confidence |
|-------|----------------|-----------|
| P1 | | |
| P2 | | |
| P3 | | |
| P4 | | |
| P3E | | |

---

## ANOMALY SWEEP

Phases run sequentially. Each phase uses the mandatory three-block template.
Phase N+1 remains locked until Phase N's GAP RECORD block is produced.

---

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 1 — INVALID STATE TRANSITIONS                         ║
╠══════════════════════════════════════════════════════════════╣
║ PRE-COMMITMENT (Role B)                                      ║
╚══════════════════════════════════════════════════════════════╝
```

Role B states now, before detection begins:
"For invalid state transitions, a finding requires [specific artifact] demonstrating
[specific condition] at strength ≥ [1/2/3]. This is locked for Phase 1."

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 1 — SWEEP TABLE (Role A)                              ║
╚══════════════════════════════════════════════════════════════╝
```

Pass 1 (Declaration-Only) — check OP-Registry for undeclared or conflicting From→To pairs:
Pass 2 (Trace-Diff) — diff each Step N Before→After against OP-Registry From/To:

| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

"None" cells require inline gap text: "No evidence here because [specific trace steps,
registry rows, or state conditions examined and cleared]."

**Evidence Strength Exit Gate:** ☐ ≥1 finding at strength ≥ 2, OR Gap Record explains why not.

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 1 — GAP RECORD (Role B) — unlock signal for Phase 2   ║
╚══════════════════════════════════════════════════════════════╝
```

Role B documents (regardless of finding count):
(a) Which transitions were examined and cleared
(b) What evidence would satisfy the Phase 1 standard stated in PRE-COMMITMENT
(c) What Phase 1 cannot determine

> **PHASE 1: COMPLETE** — Phase 2 unlocked.

---

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 2 — MISSING PRECONDITION CHECKS                       ║
╠══════════════════════════════════════════════════════════════╣
║ PRE-COMMITMENT (Role B)                                      ║
╚══════════════════════════════════════════════════════════════╝
```

Role B: "For missing precondition checks, a finding requires [standard]. Locked."

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 2 — SWEEP TABLE (Role A)                              ║
╚══════════════════════════════════════════════════════════════╝
```

Pass 1 (Declaration-Only) — OP-Registry scan for absent or underspecified preconditions:
Pass 2 (Trace-Diff) — trace step scan for skipped or abbreviated precondition verification:

| Finding-ID | OP-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-------|-------------------------|-----|--------------------|-----|

("None" cells: inline gap text required)

Evidence Strength Exit Gate: ☐

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 2 — GAP RECORD (Role B) — unlock signal for Phase 3   ║
╚══════════════════════════════════════════════════════════════╝
```

> **PHASE 2: COMPLETE**

---

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 3 — INVARIANT VIOLATIONS                              ║
╠══════════════════════════════════════════════════════════════╣
║ PRE-COMMITMENT (Role B)                                      ║
╚══════════════════════════════════════════════════════════════╝
```

Role B: "For invariant violations, a finding requires [standard]. Locked."

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 3 — SWEEP TABLE (Role A)                              ║
╚══════════════════════════════════════════════════════════════╝
```

Pass 1 (Declaration-Only) — INV-Registry scan for missing thresholds; OP-Registry scan
for operations with no declared invariant check:
Pass 2 (Trace-Diff) — trace step invariant rows: VIOLATED verdicts or unchecked invariants:

| Finding-ID | INV-ID | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|--------|-------------------------|-----|--------------------|-----|

Evidence Strength Exit Gate: ☐

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 3 — GAP RECORD (Role B) — unlock signal for Phase 4   ║
╚══════════════════════════════════════════════════════════════╝
```

> **PHASE 3: COMPLETE**

---

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 4 — RACE CONDITIONS                                   ║
╠══════════════════════════════════════════════════════════════╣
║ PRE-COMMITMENT (Role B)                                      ║
╚══════════════════════════════════════════════════════════════╝
```

Role B: "For race conditions, a finding requires [e.g., an explicit two-thread interleaving
showing a state inconsistency at strength ≥ 2]. Locked."

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 4 — SWEEP TABLE (Role A)                              ║
╚══════════════════════════════════════════════════════════════╝
```

Pass 1 (Declaration-Only) — OP-Registry scan for shared-state mutations without
concurrency preconditions; identify check-then-act patterns:
Pass 2 (Trace-Diff) — construct minimal two-thread interleavings for candidate pairs;
show step sequence and resulting inconsistent state explicitly:

| Finding-ID | OP-IDs | Declaration-Only Finding | Str | Trace-Diff (interleaving) | Str |
|-----------|--------|-------------------------|-----|---------------------------|-----|

Evidence Strength Exit Gate: ☐

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 4 — GAP RECORD (Role B) — unlock signal for Phase 3E  ║
╚══════════════════════════════════════════════════════════════╝
```

> **PHASE 4: COMPLETE**

---

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 3E — UNDECLARED REFERENCES (fifth peer phase)         ║
╠══════════════════════════════════════════════════════════════╣
║ PRE-COMMITMENT (Role B)                                      ║
╚══════════════════════════════════════════════════════════════╝
```

Role B: "For undeclared references, a finding requires [standard — e.g., a specific
name appearing in trace or declaration that cannot be resolved to a registry entry,
at strength ≥ 2]. Locked."

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 3E — SWEEP TABLE (Role A)                             ║
╚══════════════════════════════════════════════════════════════╝
```

Pass 1 (Declaration-Only) — cross-reference all three registries against each other:
Pass 2 (Trace-Diff) — cross-reference trace step text against all three registries:

| Finding-ID | Reference | Missing From | Declaration-Only Finding | Str | Trace-Diff Finding | Str |
|-----------|-----------|-------------|-------------------------|-----|-------------------|-----|

Evidence Strength Exit Gate: ☐

```
╔══════════════════════════════════════════════════════════════╗
║ PHASE 3E — GAP RECORD (Role B) — sweep complete             ║
╚══════════════════════════════════════════════════════════════╝
```

> **PHASE 3E: COMPLETE**

---

## RECONCILIATION

| Phase | Predicted | Actual | C / FP / FN | Surprising? | Explanation |
|-------|-----------|--------|-------------|-------------|-------------|

Calibration = Correct / Total. If < 0.5: diagnose the broken domain assumption.

---

## MASTER ANOMALY REGISTER

| Finding-ID | Type | OP-ID | S-ID | INV-ID | Strength | Phase |
|-----------|------|-------|------|--------|---------|-------|
```

---

## Variation Summary

| Variation | Axes | Core Structural Bet |
|-----------|------|---------------------|
| V-01 | Role sequence (single) | Upfront locked Standards Registry for all five phases — Role B commits before Phase 1, not per-phase |
| V-02 | Output format (single) | Schema-first: all three registries fully cross-checked before any trace or sweep begins |
| V-03 | Phrasing register (single) | SHALL/SHALL NOT/REQUIRED modal language throughout — gates are obligations, not descriptions |
| V-04 | Role sequence + phrasing register | Named-character dialogue (Archivist/Auditor) — per-phase Auditor commitment is a required conversational turn |
| V-05 | Output format + lifecycle emphasis | Triple-output template per phase (PRE-COMMITMENT / SWEEP TABLE / GAP RECORD) rendered as visible blocks — missing block = visible structural gap |
