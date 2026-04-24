Good — I have the full lineage. Now I'll write the 5 R7 variations incorporating C-26, C-27, C-28 as the new structural spine, with single-axis variation first.

---

# trace-state Variations — Round 7
**Rubric**: v7 (C-01 through C-28)
**New criteria to activate**: C-26 (anomaly-type-as-top-level-phase), C-27 (prejudice-dismissal naming), C-28 (dual-mode doc-vs-trace detection)

---

## V-01 — Single-axis: Role Sequence
**Axis**: Dedicated Acquittal Advocate sub-role within each C-26 anomaly phase
**Hypothesis**: Naming a specific sub-role for acquittal work separates the detection function from the dismissal justification function. When a phase closes with no finding, the Acquittal Advocate must produce the C-27 gap record before the exit gate opens — producing richer structural gap maps than a unified auditor who both detects and dismisses.
**Domain**: Customer Service

---

```markdown
# trace-state Skill — Customer Service Domain

## Behavioral Constraint (Read Before Starting)

**Score-Aloud Protocol**: When you identify a finding in any phase, say its evidence
strength (1/2/3) aloud before writing anything else. Say: "this is a [N] — [one sentence
why]." Then write it. If you notice you are filling in strength scores after finishing a
phase, stop. Go back to where the finding was first identified. Record the strength there.
A retroactive score fill does not pass.

Strength scale:
- 1 = Plausible but requires unusual conditions
- 2 = Reachable in normal Customer Service workflows
- 3 = Reachable under documented operating conditions with named field values

---

## Roles

Two roles operate throughout this trace. They do not take turns globally — they operate
within each phase.

**Role A — Transition Analyst**: Builds and reads the state machine. Constructs the trace
steps. Runs detection: for each anomaly type, examines the declaration tables and the trace
sequence for evidence.

**Role B — Acquittal Advocate**: Activates only when the Transition Analyst declares a
"no finding" verdict for an anomaly type. Before the phase exit gate opens, Role B must
produce a Gap Record: the specific trace step number, state condition, or field value that
would need to exist to produce the finding. "No evidence found" is not a Gap Record.

If Role B cannot produce a Gap Record, the phase does not close. The Transition Analyst
must extend the trace or revise the analysis until either a finding is produced or a genuine
gap is named.

---

## Phase 0 — Domain Setup and Invariant Gate

Select a Customer Service entity. Candidates: Support Ticket, Escalation Case, Return
Request, Service Level Agreement, Chat Session. Choose one and name it throughout.

### 0A — Numeric/Temporal Invariant Gate

Before building any declaration table, produce at least two invariants that include a
specific threshold, ratio, or duration constraint. Examples that pass:
- "Escalation required if unresolved after 48 hours"
- "SLA breach triggered when resolution time > contracted hours"
- "Ticket cannot be re-opened more than 30 days after close date"

Examples that do not pass:
- "Ticket must be valid before processing"
- "Data must be consistent"

Do not advance to Phase 1 until this gate is satisfied.

**Phase 0 Exit Gate** (check each before advancing):
- [ ] At least two invariants stated with specific numeric or duration thresholds
- [ ] Entity named and domain confirmed as Customer Service

---

## Phase 1 — State Machine Declaration

Produce three declaration tables. Assign IDs at declaration time. Every downstream
reference must use a declared ID.

### Table 1A — States

| S-ID | State Name | Entry Condition | Exit Conditions |
|------|------------|-----------------|-----------------|
| S-01 | ... | What must be true to be in this state (specific field values, not "data is valid") | Operations that move out |
| S-02 | ... | ... | ... |
| (minimum 5 states) | | | |

### Table 1B — Operations

| OP-ID | Operation Name | From State(s) | To State | Preconditions | Postconditions |
|-------|---------------|---------------|----------|---------------|----------------|
| OP-01 | ... | S-IDs | S-ID | Named field + value | Named field + value |
| (minimum 7 operations) | | | | | |

### Table 1C — Invariants

| INV-ID | Invariant Statement | Applies To States | Falsification Test |
|--------|--------------------|--------------------|-------------------|
| INV-01 | ... (from Phase 0) | S-IDs | The specific conditions that would violate this invariant |
| INV-02 | ... (from Phase 0) | S-IDs | ... |
| (minimum 3 invariants) | | | |

### 1D — ID Coverage Check

Before advancing, scan Tables 1A–1C. List every S-ID, OP-ID, and INV-ID declared. In
Phases 2 and 3, every reference to a state, operation, or invariant must use a declared ID.
Any reference to an undeclared ID is a finding for Phase 4E (Undeclared Reference).

**Phase 1 Exit Gate**:
- [ ] 5+ states with non-trivial Entry Condition column
- [ ] 7+ operations with state-specific preconditions and postconditions
- [ ] 3+ invariants, at least 2 with numeric/temporal thresholds from Phase 0
- [ ] ID registry complete

---

## Phase 2 — Trace Construction

Trace the entity lifecycle as numbered steps. Each step is a complete state snapshot.

### Required Trace Coverage

Include all three of the following:

1. **Happy path** — at least 5 steps showing the normal resolution workflow
2. **Negative path** — at least 1 step where an operation is attempted from a state that
   does not permit it. Name exactly which precondition fails and what the system does
   (rejects, errors, routes elsewhere). Vague outcomes do not pass.
3. **Concurrent scenario** — at least 1 step or step pair showing two operations that
   could interleave on the same entity. Name: which two operations, what state conflict
   results, and which should win (or how the conflict should be detected).

### Step Template

```
Step N — [OP-ID]: [Operation Name]
  Before: [S-ID] — [State Name] | [key field values that matter for this step]
  Preconditions: [name each precondition by field and value — "preconditions met" does not pass]
  After: [S-ID] — [State Name] | [key field values that changed]
  Postconditions: [name each guarantee by field and value]
```

**Phase 2 Exit Gate**:
- [ ] 7+ numbered steps with complete before/after snapshots
- [ ] At least one negative path step with named precondition failure
- [ ] At least one concurrent scenario with named state conflict

---

## Phase 3 — Pre-Sweep Hypothesis

Read Tables 1A–1C only. Do not read Phase 2 steps yet.

Predict which of the four anomaly types you expect to find. For each prediction, state
the structural reason (which declaration in 1A/1B/1C suggests vulnerability).

| Anomaly Type | Predicted? | Structural Reason (declarations only) | Confidence (H/M/L) |
|--------------|-----------|----------------------------------------|---------------------|
| Invalid transition | | | |
| Missing precondition check | | | |
| Invariant violation | | | |
| Race condition | | | |

Do not read Phase 2 until this table is complete.

**Phase 3 Exit Gate**:
- [ ] All four anomaly types have explicit Predicted? entries
- [ ] Structural Reason column references specific declaration IDs (S-ID/OP-ID/INV-ID)

---

## Phase 4 — Anomaly Sweep (Four Sequential Phases)

**Sequential Commitment Rule**: Complete Phase 4A entirely before beginning Phase 4B.
Complete 4B before 4C. Complete 4C before 4D. Complete 4D before 4E. The exit gate
of each phase must be satisfied before the next phase opens.

**For every phase**: The Transition Analyst runs detection. If the verdict is "no finding",
the Acquittal Advocate must produce a Gap Record before the phase exit gate is checked.

**Gap Record format**: "To find this anomaly, the trace would need to contain: [specific
step number, state condition (S-ID + field value), or operation sequence]. That condition
is absent because: [one sentence]."

A Gap Record that only says "no evidence was found" or "this anomaly does not apply" does
not pass.

### Dual-Mode Detection (applies to all phases)

Each phase runs two detection passes:

**Pass A (Declaration-Only)**: Read Tables 1A–1C. Does the declared behavior, taken alone,
contain any internal inconsistency or gap for this anomaly type? A state with no valid exit
operation is detectable from 1A alone. A precondition that references an undeclared state
is detectable from 1B alone.

**Pass B (Doc-vs-Trace Diff)**: Read Phase 2 steps. Does the trace demonstrate every
claim made in Tables 1A–1C? A postcondition declared in 1B that is never shown in any
Phase 2 step is a finding. An entry condition declared in 1A that no step verifies reaching
is a finding.

Both passes must complete before the phase exit gate is checked.

---

### Phase 4A — Invalid State Transition

**Transition Analyst (Pass A)**: Read Table 1B. Is any operation declared with an invalid
From State (a state that cannot reach this operation based on Table 1A Entry Conditions)?

**Transition Analyst (Pass B)**: Read Phase 2 steps. Is any step's Before S-ID invalid
for its OP-ID per Table 1B? Is any declared valid transition absent from the trace when
it should have been exercised?

Finding row format:
```
FINDING: [OP-ID] attempted from [S-ID] (Before state)
Pass: A (declaration-only) / B (doc-vs-trace)
Evidence: [what the table declares / what the step shows]
Expected: [what should happen per declaration]
Strength: [1/2/3] — assigned at point of discovery
```

**If no finding from either pass (Acquittal Advocate)**:
Produce a Gap Record for Pass A and a Gap Record for Pass B. Name what trace step or
declaration condition would need to exist to produce this finding in each pass.

**Phase 4A Exit Gate**:
- [ ] Pass A complete — verdict recorded
- [ ] Pass B complete — verdict recorded
- [ ] If any "no finding" verdict: Gap Record with specific missing condition produced
- [ ] Strength assigned at discovery, not retroactively

---

### Phase 4B — Missing Precondition Check

**Transition Analyst (Pass A)**: Read Table 1B. Is any operation's Precondition column
vague, absent, or referencing an undeclared ID?

**Transition Analyst (Pass B)**: Read Phase 2 steps. Is any step's precondition field
blank, "preconditions met", or naming a condition that contradicts Table 1B?

Finding row format: same as 4A, with OP-ID, S-ID, INV-ID columns.

**If no finding (Acquittal Advocate)**: Produce Gap Records for both passes.

**Phase 4B Exit Gate**:
- [ ] Pass A and Pass B verdicts recorded
- [ ] All "no finding" verdicts have Gap Records
- [ ] Strength at discovery

---

### Phase 4C — Invariant Violation

**Transition Analyst (Pass A)**: Read Table 1C. Is any INV-ID referencing an S-ID that
does not exist in Table 1A? Is any falsification test condition reachable without passing
through the invariant check?

**Transition Analyst (Pass B)**: Read Phase 2 steps. Does any step transition produce
a state that would violate an INV-ID from Table 1C? Does any step skip a state where an
invariant should have been checked?

Finding row format: includes INV-ID column.

**If no finding (Acquittal Advocate)**: Produce Gap Records for both passes. Name the
specific state (S-ID) or step where the invariant check is absent from the trace.

**Phase 4C Exit Gate**:
- [ ] Both passes complete with verdicts
- [ ] Gap Records produced for all "no finding" verdicts
- [ ] Strength at discovery

---

### Phase 4D — Race Condition

**Transition Analyst (Pass A)**: Read Tables 1A–1B. Are there two or more operations that
share a From State? Could they interleave on the same entity instance?

**Transition Analyst (Pass B)**: Read Phase 2. Does the concurrent scenario step (from
Phase 2 required coverage) produce the conflicting outcome declared in 1B, or does the
trace resolve the race without documenting the conflict?

Finding row format: includes both OP-IDs and the shared S-ID.

**If no finding (Acquittal Advocate)**: Produce Gap Records for both passes. For Pass B:
name the specific step pair that would need to be concurrent and the state conflict that
would need to be named.

**Phase 4D Exit Gate**:
- [ ] Both passes complete
- [ ] Gap Records for all "no finding" verdicts
- [ ] Strength at discovery

---

### Phase 4E — Undeclared ID Reference

Scan all Phase 2 steps, Phase 3, and Phase 4A–4D findings for any reference to an S-ID,
OP-ID, or INV-ID not present in the Phase 1 ID registry. Each undeclared reference is a
finding regardless of whether the referenced entity exists implicitly.

| Undeclared ID | Location | Production Consequence |
|---------------|----------|----------------------|
| ... | Step N or Phase 4X | What state corruption or untraced transition results |

**If no finding (Acquittal Advocate)**: Name the specific scan locations reviewed and
confirm the ID registry was complete at Phase 1 close.

**Phase 4E Exit Gate**:
- [ ] Full scan of all downstream references against Phase 1 registry completed
- [ ] Verdict recorded; undeclared references listed or absence confirmed with scan evidence

---

## Phase 5 — Anomaly Register

Consolidate all findings from Phases 4A–4E into a single register.

| A-ID | Type | OP-ID | S-ID | INV-ID | Pass (A/B) | What Breaks | Strength |
|------|------|-------|------|--------|------------|-------------|----------|
| A-01 | ... | ... | ... | ... | ... | ... | ... |

Rules:
- No blank cells in a "found" row. Use "N/A: [reason]" for ID columns that do not apply.
- Strength values must match the point-of-discovery scores from Phases 4A–4E. No revision.
- Quality gate: at least 2 findings. At least 1 with Strength ≥ 2.

---

## Phase 6 — Reconciliation

Compare Phase 3 predictions against Phase 5 register.

| Anomaly Type | Predicted? | Found? | C/FP/FN | Surprise Sentence |
|--------------|-----------|--------|---------|-------------------|
| Invalid transition | | | | One sentence: why this outcome matched or violated prediction |
| Missing precondition check | | | | |
| Invariant violation | | | | |
| Race condition | | | | |

Classification:
- **C** = Correct (predicted found → found, or predicted none → none)
- **FP** = False Positive (predicted found → not found)
- **FN** = False Negative (predicted none → found)

Calibration score: correct / total predictions. If score < 60%, write one sentence
diagnosing what structural feature of the declarations the hypothesis model missed.

**Phase 6 Exit Gate**:
- [ ] All four anomaly types classified C/FP/FN
- [ ] Calibration score computed
- [ ] If < 60%, structural diagnosis sentence written
```

---

## V-02 — Single-axis: Output Format
**Axis**: C-28's dual-mode structure as the top-level document skeleton — two major passes at document level, each generating its own anomaly table, with the four C-26 anomaly phases running inside each pass independently
**Hypothesis**: Making the dual-mode structure the primary document skeleton (not a mechanism within phases) forces genuinely independent detection runs because each major pass has its own anomaly tables, phase headers, and exit gates — the model cannot conflate declaration-only findings with doc-vs-trace findings.
**Domain**: Finance

---

```markdown
# trace-state Skill — Finance Domain

## Behavioral Constraint

**Score-Aloud Protocol**: Every finding receives a Strength score (1/2/3) at the moment
you first identify it. Say aloud: "Strength [N] — [one clause why]." Write that. Do not
fill Strength columns after completing a sweep section. If you catch yourself doing so,
stop. Return to the first identification point. Add the score there as a new row if needed.
Retroactive revision is prohibited.

Strength:
- 1 = Unusual conditions required
- 2 = Reachable in normal Finance approval workflows
- 3 = Demonstrated by named field values in the trace

---

## Pre-Declaration: Numeric/Temporal Invariant Gate

Select a Finance entity: Invoice, Purchase Order, Expense Claim, Budget Allocation, Payment
Run, Credit Memo. Name it throughout.

Before building any table, produce at least two invariants with specific thresholds:

| INV-ID | Invariant | Falsification Test (specific values that would violate it) |
|--------|-----------|-----------------------------------------------------------|
| INV-01 | | Example that passes: "Approval required when amount > $10,000" |
| INV-02 | | Example that passes: "Payment blocked if past-due balance > $0" |

Do not advance until both rows have non-blank Falsification Tests with specific amounts,
percentages, or date/duration constraints. Generic conditions do not pass.

---

## Section 1 — Declaration Tables

### 1A — States

| S-ID | State Name | Entry Condition | Valid Operations From This State |
|------|------------|-----------------|----------------------------------|
| S-01 | | Specific field values, not "document is valid" | OP-IDs |
| (minimum 5 states) | | | |

### 1B — Operations

| OP-ID | Operation | From State(s) | To State | Preconditions | Postconditions |
|-------|-----------|---------------|----------|---------------|----------------|
| OP-01 | | S-IDs | S-ID | Named field + value | Named field + value |
| (minimum 7 operations) | | | | | |

### 1C — Invariants

| INV-ID | Invariant Statement | Applies To | Falsification Test |
|--------|--------------------|-----------|--------------------|
| INV-01 | (from Pre-Declaration) | S-IDs | |
| INV-02 | (from Pre-Declaration) | S-IDs | |

### 1D — ID Registry

List all declared S-IDs, OP-IDs, INV-IDs. Any reference downstream to an undeclared ID
is a finding. Note any reference-before-declaration as a cross-reference failure.

---

## Section 2 — Trace

Build the entity lifecycle as numbered steps.

Required coverage:
- At least 7 numbered steps
- At least 1 negative path step (attempted operation from invalid state; name the
  precondition that fails and the rejection outcome)
- At least 1 concurrent scenario (two operations that could interleave; name the
  conflicting state outcome)

Step format:
```
Step N — [OP-ID]: [Operation Name]
  Before: [S-ID] — [State Name] | [relevant field values]
  Preconditions: [field and value — not "conditions met"]
  After: [S-ID] — [State Name] | [changed field values]
  Postconditions: [named guarantees]
```

---

## Section 3 — Pre-Sweep Hypothesis

Read Sections 1A–1C only. Do not read Section 2.

For each anomaly type, predict: found or not found. State the specific declaration (by
ID) that suggests vulnerability. This is the prediction record; it does not change after
Section 4 begins.

| Anomaly Type | Predicted | Declaration Evidence (S-ID/OP-ID/INV-ID) | Confidence |
|--------------|-----------|------------------------------------------|-----------|
| Invalid transition | | | |
| Missing precondition check | | | |
| Invariant violation | | | |
| Race condition | | | |

---

## Section 4 — Sweep Pass A: Declaration-Only Analysis

**Instructions for Pass A**: Read Sections 1A–1C only. Do not read Section 2 during
this pass. Find anomalies that are detectable from the declared behavior alone —
internal inconsistencies in the declaration tables, missing entries, unreachable states,
contradictory preconditions.

Run all four anomaly-type phases in sequence. Complete each phase before starting the
next.

### Pass A — Phase 1: Invalid Transition (Declaration-Only)

Does Table 1B declare any operation with a From State that has no valid path to that
operation per Table 1A Entry Conditions? Is any declared transition logically unreachable?

Finding format:
```
FINDING A1-NN: Invalid transition detectable from declarations
OP-ID: [OP-ID] | S-ID: [S-ID]
Declaration Evidence: [what 1A or 1B says]
Strength: [1/2/3 — assigned now]
```

**No-Finding Rule**: If no declaration-level invalid transition is found, invoke the
Prejudice-Dismissal Protocol. State: "To find this anomaly in declarations alone, 1B would
need to declare [OP-ID] as executable from [S-ID], but 1A's Entry Condition for [S-ID]
would prohibit it. That contradiction is absent because [one sentence]." Bare "None" does
not pass.

Pass A Phase 1 Exit Gate:
- [ ] Full review of Table 1B From States against Table 1A Entry Conditions
- [ ] Finding recorded OR Prejudice-Dismissal Gap Record produced

---

### Pass A — Phase 2: Missing Precondition Check (Declaration-Only)

Does any row in Table 1B have a vague, absent, or undeclared-ID precondition? Is any
precondition referencing a state or invariant not in the Section 1D registry?

**No-Finding Rule**: Name the specific Table 1B row(s) reviewed and the precondition
wording that was inspected. Confirm each was state-specific. "Reviewed all rows and found
no gaps" does not pass — name what you looked at.

Pass A Phase 2 Exit Gate:
- [ ] All Table 1B precondition cells reviewed individually
- [ ] Finding OR gap record with named rows reviewed

---

### Pass A — Phase 3: Invariant Violation (Declaration-Only)

Does any INV-ID in Table 1C reference an S-ID not in Table 1A? Is any invariant's
Falsification Test reachable from the declared operations without a precondition check
that would block it?

**No-Finding Rule**: For each INV-ID, name the specific S-IDs it applies to and the
operations (OP-IDs) that could potentially violate it. Confirm each has a blocking
precondition in 1B or an entry condition in 1A. Name what is missing for a violation to
be reachable.

Pass A Phase 3 Exit Gate:
- [ ] All INV-IDs cross-checked against 1A and 1B
- [ ] Finding OR prejudice-dismissal gap record per invariant

---

### Pass A — Phase 4: Race Condition (Declaration-Only)

Are there two or more OP-IDs in Table 1B that share a From State? Could they operate
concurrently on the same entity without an exclusive lock declared in the preconditions?

**No-Finding Rule**: List the From States that have more than one operation and confirm
whether each pairing's preconditions include a mutual exclusion clause. Name what
precondition would need to be absent for a race to be reachable.

Pass A Phase 4 Exit Gate:
- [ ] All shared-From-State pairings reviewed
- [ ] Finding OR gap record naming what exclusion clause is present/absent

---

### Pass A — Phase 5: Undeclared Reference (Declaration-Only)

Cross-check: does any cell in Tables 1A–1C reference an ID not in the 1D registry? Any
forward-reference to an operation or state not yet declared at the point of reference?

Pass A Phase 5 Exit Gate:
- [ ] Full scan of 1A–1C cell values against 1D registry complete
- [ ] Verdict recorded

---

**Pass A Summary Table**

| Phase | Anomaly Type | Verdict | Finding IDs | Strength (if found) |
|-------|-------------|---------|-------------|---------------------|
| A1 | Invalid transition | | | |
| A2 | Missing precondition | | | |
| A3 | Invariant violation | | | |
| A4 | Race condition | | | |
| A5 | Undeclared reference | | | |

---

## Section 5 — Sweep Pass B: Doc-vs-Trace Diff Analysis

**Instructions for Pass B**: Now read Section 2. For each anomaly type, diff the declared
behavior (Sections 1A–1C) against the traced behavior (Section 2 steps). A claim in the
declaration that is not demonstrated in the trace is a finding. A step in the trace that
performs an undeclared operation is a finding.

This is an independent pass. Do not inherit Pass A verdicts as starting assumptions.
Each anomaly type begins with a fresh inquiry against the full trace.

Run all four anomaly-type phases in sequence. Complete each phase before the next.

### Pass B — Phase 1: Invalid Transition (Doc-vs-Trace Diff)

Does any Section 2 step show a Before S-ID that is not in Table 1B's From States for
that OP-ID? Does the trace demonstrate any transition that the declaration tables do not
permit? Does the trace omit any declared invalid-transition check that should have been
visible?

Finding format:
```
FINDING B1-NN: Transition present in trace but absent/prohibited in declarations
OP-ID: [OP-ID] | S-ID: [Before S-ID] | Step: [Step N]
Declaration says: [what Table 1B declares]
Trace shows: [what Step N does]
Strength: [1/2/3 — assigned now]
```

**No-Finding Rule**: For each Section 2 step, name the OP-ID and its Table 1B From States.
Confirm the trace Before S-ID is in the declared set. "Reviewed all steps" is not a gap
record — name the specific steps reviewed and what the 1B declaration says for each OP-ID.

Pass B Phase 1 Exit Gate:
- [ ] Every Section 2 step verified against Table 1B From States
- [ ] Finding OR step-by-step dismissal record produced

---

### Pass B — Phase 2: Missing Precondition Check (Doc-vs-Trace Diff)

Does any Section 2 step's Preconditions field fail to name the condition required by
Table 1B? Does the trace skip a precondition check on a step where one is declared?
Does any step claim a precondition is met without showing the field value?

**No-Finding Rule**: Name the Table 1B precondition for each Section 2 OP-ID and the
matching step's precondition field. Confirm equivalence by field and value. "Preconditions
match" without naming them does not pass.

Pass B Phase 2 Exit Gate:
- [ ] Table 1B preconditions cross-referenced against Section 2 step preconditions, per OP-ID
- [ ] Finding OR per-step comparison record

---

### Pass B — Phase 3: Invariant Violation (Doc-vs-Trace Diff)

Does any Section 2 step transition an entity to or through a state where an INV-ID from
Table 1C would be violated? Does the trace demonstrate the invariant check, or does it
skip the check silently? Are any invariant-relevant field transitions shown in steps?

**No-Finding Rule**: For each INV-ID, identify the Section 2 step(s) that enter or exit
the states it covers. Confirm the step shows the invariant is preserved. Name what the
step would need to show and what it actually shows.

Pass B Phase 3 Exit Gate:
- [ ] All INV-IDs mapped to their relevant Section 2 steps
- [ ] Finding OR per-invariant trace-confirmation record

---

### Pass B — Phase 4: Race Condition (Doc-vs-Trace Diff)

Does the concurrent scenario step(s) in Section 2 demonstrate the conflicting outcome
declared in Table 1B? Does the trace resolve the race via a named mechanism, or does it
assert conflict without showing resolution? Does the declared concurrent scenario match
what the trace actually shows?

**No-Finding Rule**: Reference the concurrent scenario step(s) from Section 2. Compare
the conflict named in those steps against the From States and preconditions in Table 1B.
Name what the trace would need to show (and what it actually shows) for the race to be
fully demonstrated.

Pass B Phase 4 Exit Gate:
- [ ] Concurrent scenario steps identified and mapped to 1B declarations
- [ ] Finding OR gap record naming the diff between declared and traced concurrent behavior

---

### Pass B — Phase 5: Undeclared Reference (Doc-vs-Trace Diff)

Do any Section 2 steps reference S-IDs, OP-IDs, or INV-IDs not in the Section 1D registry?
Does the trace introduce new states or operations not declared in Section 1?

Pass B Phase 5 Exit Gate:
- [ ] Full scan of Section 2 step IDs against Section 1D registry complete
- [ ] Verdict recorded

---

**Pass B Summary Table**

| Phase | Anomaly Type | Verdict | Finding IDs | Strength (if found) |
|-------|-------------|---------|-------------|---------------------|
| B1 | Invalid transition | | | |
| B2 | Missing precondition | | | |
| B3 | Invariant violation | | | |
| B4 | Race condition | | | |
| B5 | Undeclared reference | | | |

---

## Section 6 — Consolidated Anomaly Register

Merge all findings from Pass A and Pass B.

| A-ID | Pass | Type | OP-ID | S-ID | INV-ID | What Breaks | Strength |
|------|------|------|-------|------|--------|-------------|----------|
| A-01 | A/B | | | | | | |

Rules:
- No blank cells in a found-verdict row. Use "N/A: [reason]" for inapplicable ID columns.
- Strength must match point-of-discovery values. No revision.
- Quality gate: ≥ 2 total findings. ≥ 1 finding with Strength ≥ 2.

---

## Section 7 — Reconciliation

Compare Section 3 predictions against Section 6 register.

| Anomaly Type | Predicted | Found (Pass A/B) | C/FP/FN | Surprise Sentence |
|--------------|-----------|-----------------|---------|-------------------|
| Invalid transition | | | | |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |

- **C** = Correct | **FP** = Predicted found, not found | **FN** = Not predicted, found

Calibration score = correct / total predictions. If < 60%, one sentence: what structural
feature of the declarations the hypothesis model missed and why the dual-pass structure
surfaced it.
```

---

## V-03 — Single-axis: Lifecycle Emphasis
**Axis**: C-27 prejudice-dismissal structured as a named exit gate step within each C-26 anomaly phase — the phase checklist contains a mandatory "Gap Record" step that fires at the moment of acquittal, not as a preamble rule
**Hypothesis**: The model encounters the prejudice-dismissal instruction at the exact moment it writes a "no finding" verdict. Placing C-27 as the next checklist item after a "no finding" entry — rather than as a rule in the preamble that may have been read 2000 tokens ago — produces fuller gap maps through temporal proximity.
**Domain**: Sales

---

```markdown
# trace-state Skill — Sales Domain

## Behavioral Constraint (Non-Negotiable)

**Score-Aloud Protocol**: When you identify a finding, state its Strength (1/2/3)
immediately. Write: "Strength [N]: [one clause]." Then enter it in the finding table.
If you realize you have not scored a finding yet, stop. Return to it. Score it. Then
continue. Do not batch-score after completing a phase.

Strength:
- 1 = Requires unusual workflow conditions
- 2 = Reachable in normal Sales processing
- 3 = Directly demonstrated by named field values in the trace

---

## Phase 0 — Entity and Invariant Gate

Select a Sales entity: Deal, Opportunity, Quote, Sales Order, Commission Record, Discount
Approval. Name it.

Before building any table, produce at least two invariants with specific thresholds or
temporal constraints:

| INV-ID | Invariant | Falsification Test |
|--------|-----------|-------------------|
| INV-01 | | Must name a dollar amount, percentage, date, or approval tier |
| INV-02 | | Must name a dollar amount, percentage, date, or approval tier |

If either Falsification Test is generic ("data must be valid", "approval must occur"),
revise before proceeding.

**Phase 0 Exit Gate**:
- [ ] Entity named
- [ ] ≥ 2 INV-IDs with specific numeric or temporal falsification tests

---

## Phase 1 — Declaration Tables

### Table 1A — States
| S-ID | State Name | Entry Condition | Exit Operations |
|------|------------|-----------------|-----------------|
| S-01 | | (specific field values) | |
| (≥ 5 states) | | | |

### Table 1B — Operations
| OP-ID | Operation | From State(s) | To State | Preconditions | Postconditions |
|-------|-----------|---------------|----------|---------------|----------------|
| OP-01 | | | | (field + value) | (field + value) |
| (≥ 7 operations) | | | | | |

### Table 1C — Invariants
| INV-ID | Statement | Applies To | Falsification Test |
|--------|-----------|-----------|-------------------|
| INV-01 | (from Phase 0) | S-IDs | |
| INV-02 | (from Phase 0) | S-IDs | |

### 1D — ID Registry
List all S-IDs, OP-IDs, INV-IDs declared above. Any downstream reference to an ID not
on this list is a finding for Phase 5E.

**Phase 1 Exit Gate**:
- [ ] ≥ 5 states with non-generic Entry Conditions
- [ ] ≥ 7 operations with named preconditions (field + value)
- [ ] ≥ 3 invariants including those from Phase 0
- [ ] ID registry complete

---

## Phase 2 — Trace Construction

Build the lifecycle as numbered steps.

Required coverage:
1. **Normal workflow** — ≥ 5 steps showing the primary sales path
2. **Rejected transition** — ≥ 1 step where an operation is attempted and rejected.
   Name: which precondition fails, by field and value. Name: what the system does.
3. **Concurrent scenario** — ≥ 1 step pair. Name: the two OP-IDs that could interleave,
   the resulting state conflict (by S-ID), and which operation should win.

```
Step N — [OP-ID]: [Operation Name]
  Before: [S-ID] — [State Name] | [field: value, field: value]
  Preconditions: [field: value — not "conditions satisfied"]
  After: [S-ID] — [State Name] | [changed fields: new values]
  Postconditions: [named guarantees]
```

**Phase 2 Exit Gate**:
- [ ] ≥ 7 steps with complete before/after snapshots
- [ ] ≥ 1 rejected-transition step with named precondition failure
- [ ] ≥ 1 concurrent scenario with named state conflict

---

## Phase 3 — Pre-Sweep Hypothesis

Read Tables 1A–1C only. Do not read Phase 2.

| Anomaly Type | Predicted | Declaration Evidence (by ID) | Confidence |
|--------------|-----------|------------------------------|-----------|
| Invalid transition | | | |
| Missing precondition check | | | |
| Invariant violation | | | |
| Race condition | | | |

**Phase 3 Exit Gate**:
- [ ] All four rows complete with declaration-based reasoning
- [ ] No references to Phase 2 content

---

## Phase 4 — Anomaly Sweep

**Sequential Rule**: Complete Phase 4A entirely before starting 4B. 4B before 4C. 4C
before 4D. 4D before 4E. Each phase has its own exit gate checklist. The exit gate
must be checked before the next phase begins.

**Dual-Mode Rule (applies to all phases)**: Each phase runs two detection passes:
- **Pass A**: Read Tables 1A–1C only. Find anomalies detectable from declarations alone.
- **Pass B**: Read Phase 2 steps. Diff declared behavior against traced behavior. A
  documented claim not demonstrated in a Phase 2 step is a finding.

**Acquittal Gate Rule**: If either pass produces a "no finding" verdict, the phase exit
gate includes a mandatory Gap Record step. The phase cannot close until the Gap Record
is produced. Instructions for each Gap Record are embedded in the phase's exit gate.

---

### Phase 4A — Invalid State Transition

**Pass A**: Read Table 1B. Is any From State listed for an operation unreachable per
Table 1A Entry Conditions? Does any declared operation create an impossible state jump?

**Pass B**: Read Phase 2 steps. Does any step's Before S-ID contradict the allowed From
States for its OP-ID in Table 1B? Is any declared valid transition claimed in 1B but
never exercised in the trace?

Finding row:
```
FINDING [A-ID]: [description]
Pass: [A or B] | OP-ID: [OP-ID] | S-ID: [S-ID]
Evidence: [what the declaration says / what the step shows]
Strength: [1/2/3 — assigned now]
```

**Phase 4A Exit Gate**:

- [ ] Pass A verdict: Found / No Finding
- [ ] Pass B verdict: Found / No Finding
- [ ] If Pass A = No Finding → Gap Record A:
  "The trace or declarations would need to contain: [specific OP-ID + S-ID combination
  from Table 1B whose From State would be invalid per Table 1A]. That combination is absent
  because: [one sentence naming the entry condition that blocks it]."
- [ ] If Pass B = No Finding → Gap Record B:
  "Step [N] would need to show [OP-ID] executing from [S-ID] where Table 1B does not
  permit it. That step is absent because: [one sentence]."
- [ ] Strength recorded at discovery for all findings

---

### Phase 4B — Missing Precondition Check

**Pass A**: Read Table 1B. Is any Preconditions cell blank, vague ("data valid"), or
referencing an undeclared ID? Does any precondition fail to name a specific field and value?

**Pass B**: Read Phase 2 steps. Does any step's Preconditions line omit a condition
required by Table 1B? Does any step assert a precondition is met without naming the
field value that satisfies it?

Finding row: same format, include OP-ID.

**Phase 4B Exit Gate**:

- [ ] Pass A verdict: Found / No Finding
- [ ] Pass B verdict: Found / No Finding
- [ ] If Pass A = No Finding → Gap Record A:
  "Table 1B row [OP-ID] would need a Preconditions cell that either names no field-level
  condition or references an undeclared state. Instead it contains: [what it actually says].
  To surface this anomaly, the declaration would need to say: [what a missing precondition
  check would look like in 1B]."
- [ ] If Pass B = No Finding → Gap Record B:
  "Step [N] for [OP-ID] would need to show the precondition field as blank or naming only
  a generic condition. It currently says: [what it says]. The specific field-value match
  that would expose the gap is: [what would be missing]."
- [ ] Strength at discovery

---

### Phase 4C — Invariant Violation

**Pass A**: Read Tables 1A and 1C. Does any INV-ID reference an S-ID not in 1A? Is any
Falsification Test condition reachable via operations in 1B without a precondition or
entry condition that would block it?

**Pass B**: Read Phase 2. Does any step enter or exit a state covered by an INV-ID in
1C without demonstrating the invariant check? Does any After-state field value in a step
violate a 1C invariant?

Finding row: include INV-ID.

**Phase 4C Exit Gate**:

- [ ] Pass A verdict: Found / No Finding
- [ ] Pass B verdict: Found / No Finding
- [ ] If Pass A = No Finding → Gap Record A:
  "To find an invariant violation in declarations, INV-[ID]'s Falsification Test would need
  to be reachable from a declared operation without a blocking precondition. The path
  [OP-ID → S-ID] is blocked by: [named precondition or entry condition]. That block is
  present, which is why no violation is detectable from declarations alone."
- [ ] If Pass B = No Finding → Gap Record B:
  "Step [N] enters state [S-ID] where INV-[ID] applies. The invariant would be violated if
  [named field] were [value threshold]. Step [N]'s After field shows [actual value], which
  does not violate the threshold. To find this anomaly, the step would need to show
  [field: violating value]."
- [ ] Strength at discovery

---

### Phase 4D — Race Condition

**Pass A**: Read Table 1B. Are there two or more OP-IDs with an overlapping From State?
Do their preconditions include a mutual exclusion clause? Could both execute concurrently
without one blocking the other?

**Pass B**: Read Phase 2. Does the concurrent scenario step pair demonstrate a state
conflict? Does the trace name which operation wins and how the conflict is detected, or
does it only set up the scenario without showing the resolution?

Finding row: include both OP-IDs and shared S-ID.

**Phase 4D Exit Gate**:

- [ ] Pass A verdict: Found / No Finding
- [ ] Pass B verdict: Found / No Finding
- [ ] If Pass A = No Finding → Gap Record A:
  "For a declaration-level race, two OP-IDs sharing a From State would need no mutual
  exclusion clause in their 1B preconditions. The operations sharing [S-ID] are [OP-IDs].
  Their preconditions include: [what the exclusion clause says, or confirm it is absent].
  The gap is: [what would need to be missing for the race to be detectable from 1B alone]."
- [ ] If Pass B = No Finding → Gap Record B:
  "The concurrent scenario in Step [N]/[N+1] would need to show the conflicting outcome —
  both operations reaching the same entity in [S-ID] without one blocking the other.
  The steps show: [what they actually show]. The specific missing element is: [what would
  need to be in the step to confirm the race]."
- [ ] Strength at discovery

---

### Phase 4E — Undeclared ID Reference

Scan all Phase 2 steps and Phase 4A–4D finding rows for S-IDs, OP-IDs, or INV-IDs not
present in the Phase 1D registry.

| Undeclared ID | Location | Production Consequence |
|---------------|----------|----------------------|
| | | |

**If no finding** → Gap Record: "Reviewed [step numbers] and [phase references]. All IDs
appearing in those locations were found in the Phase 1D registry: [list checked IDs]."

**Phase 4E Exit Gate**:
- [ ] Full scan completed
- [ ] Verdict recorded with scan evidence

---

## Phase 5 — Anomaly Register

| A-ID | Pass | Type | OP-ID | S-ID | INV-ID | What Breaks | Severity | Strength |
|------|------|------|-------|------|--------|-------------|---------|---------|
| | | | | | | | | |

- No blank cells in found rows. "N/A: [reason]" required.
- Strength matches point-of-discovery scores. No revision.
- Quality gate: ≥ 2 findings total. ≥ 1 with Strength ≥ 2.

---

## Phase 6 — Reconciliation

| Anomaly Type | Predicted | Found | C/FP/FN | Surprise |
|--------------|-----------|-------|---------|---------|
| Invalid transition | | | | Why matched/violated prediction (one sentence) |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |

Calibration = correct / total. If < 60%, diagnose what the hypothesis model missed.
```

---

## V-04 — Combination: Role Sequence + Phrasing Register
**Axes**: Workshop-voice register (R5 V-03 pattern, scored 99) combined with character-owned C-26 anomaly phases — each phase is owned by a named domain expert who narrates their reasoning aloud, with C-27 prejudice-dismissal and C-28 dual-mode detection woven into each character's investigative voice
**Hypothesis**: The workshop register lowers structural rigidity enough for genuine reasoning. Character-owned phases prime domain vocabulary at the phase level (not just globally). The combination produces richer, more domain-grounded findings because the character voice activates at the exact moment the model is detecting anomalies for that type — not just during declaration setup.
**Domain**: Customer Service

---

```markdown
# trace-state Skill — Customer Service Domain

## The Rules (Read First — These Are Not Optional)

Rule 1 — Score Aloud: Every time you identify a finding, pause. Say: "Strength [1/2/3]:
[one clause." Then record it. If you finish a phase and notice Strength cells are blank,
stop. Go back to where you found it. Record the strength there. You may add a new row.
You may not revise a previously-written score.

Rule 2 — No Bare Acquittals: If you end a phase with "nothing found," you owe the reader
a Gap Record — the specific trace step number, state field value, or declaration entry
that would need to exist to produce the finding. "No evidence" is not a Gap Record.

Rule 3 — Two Independent Passes: Each anomaly phase runs a declaration-only pass first,
then a doc-vs-trace diff pass second. Do not read the trace during the declaration pass.
Do not revise declaration-pass findings based on trace-pass findings.

---

## Workshop Setup

Pick a Customer Service entity. Use one of these: Support Ticket, Escalation Case,
Return Request, SLA Contract, Chat Session. Name it and stick with it.

Before building any tables, write down two invariants that a domain expert would actually
check on day one:

```
Invariant 1: _________________________________
Falsification test (specific numbers): _______
Example: "Escalation fires if unresolved after 48 hours."
Not: "Tickets must be resolved promptly."

Invariant 2: _________________________________
Falsification test (specific numbers): _______
```

If either test is vague, revise it now. You cannot start the declaration tables with
generic invariants.

---

## Step 1 — Build the State Machine

Go ahead and build the three declaration tables. Be specific on entry conditions — a CS
domain expert should be able to read "Entry Condition: assigned to a Tier-2 agent AND
customer reply received within SLA window" and recognize the real state.

**State table** (≥ 5 states):
| S-ID | State Name | Entry Condition | Exit Operations (OP-IDs) |
|------|------------|-----------------|--------------------------|
| S-01 | | | |

**Operations table** (≥ 7 operations):
| OP-ID | Operation | From States | To State | Preconditions | Postconditions |
|-------|-----------|-------------|----------|---------------|----------------|
| OP-01 | | | | | |

**Invariants table** (≥ 3, including the two from setup):
| INV-ID | Statement | Applies To | Falsification Test |
|--------|-----------|-----------|-------------------|
| INV-01 | | S-IDs | |

**ID List**: Before going further, list every S-ID, OP-ID, INV-ID declared above. Keep
this list. If a later step references an ID not on the list, that's a finding.

Step 1 checkpoint — check these before moving on:
- [ ] ≥ 5 states with real entry conditions (not "ticket exists")
- [ ] ≥ 7 operations with named preconditions (field and value)
- [ ] ≥ 2 invariants with specific thresholds
- [ ] ID list complete

---

## Step 2 — Run the Trace

Write the lifecycle as numbered steps. Three things you must include:

1. **The normal path**: at least 5 steps showing a ticket moving from open to resolved
2. **A rejection**: one step where an operation fails. Name the precondition that blocks
   it and what the system does. "Rejected due to invalid state" is not enough — name the
   field.
3. **A collision**: one step or step pair showing two operations that could run at the
   same time on the same ticket. Name which two, what state conflict results, and who wins.

Use this format:
```
Step N — [OP-ID]: [Operation Name]
  Before: [S-ID] — [State Name] | [field: value, field: value]
  Preconditions: [field: value — saying "conditions met" doesn't count]
  After: [S-ID] — [State Name] | [what changed]
  Postconditions: [what is now guaranteed]
```

Step 2 checkpoint:
- [ ] ≥ 7 steps with full before/after snapshots
- [ ] ≥ 1 rejection step with named precondition failure
- [ ] ≥ 1 collision step with named conflict

---

## Step 3 — Predict Before You Look

Read your Step 1 tables only. Don't look at Step 2 yet.

For each of the four anomaly types, write down whether you think you'll find one and why.
Cite the declaration by ID. This is your prediction record; it doesn't change.

| Type | Think you'll find it? | Why (which declaration ID suggests it) | Confidence |
|------|-----------------------|-----------------------------------------|-----------|
| Invalid transition | | | |
| Missing precondition | | | |
| Invariant violation | | | |
| Race condition | | | |

Done? Now you can look at Step 2.

---

## Step 4 — Investigation Phases

Four phases. Finish one completely before starting the next. Each phase is owned by a
named character — a CS domain expert who walks through the evidence aloud.

### Phase 4A — Invalid State Transition
**Expert**: Alex, Senior CS Operations Analyst (10 years routing Support Tickets)

Alex runs two passes:

**Alex's Declaration Pass**: Alex reads Table 1B and Table 1A. "I'm checking whether any
operation in my declaration claims to start from a state that, according to my Entry
Conditions, shouldn't be reachable." Alex writes findings in this format:
```
Alex finds: [OP-ID] declared executable from [S-ID], but 1A Entry Condition for [S-ID]
says [condition]. This operation can't start there.
Strength [1/2/3]: [Alex says aloud why]
```

**Alex's Doc-vs-Trace Pass**: Alex now reads Step 2. "I'm checking whether any step in
the trace shows a Before state that contradicts Table 1B's From States. I'm also checking
whether any declared valid transition in 1B is completely absent from the trace — that
absence is itself a signal."

If Alex finds something: record it with Strength at discovery.

**If Alex finds nothing**:
Alex must say: "If I were going to find an invalid transition, I'd need to see [specific
OP-ID] executing from [specific S-ID] that contradicts 1B. That scenario is absent
because [one sentence — what entry condition or precondition blocks it]. And in the trace,
the step I'd need to see is Step [N] with Before=[S-ID], which would make it a 1B
violation. That step doesn't exist because [one sentence]."

Phase 4A checkpoint:
- [ ] Alex ran the declaration pass
- [ ] Alex ran the doc-vs-trace pass
- [ ] Findings recorded with Strength, OR Gap Records produced for both passes

---

### Phase 4B — Missing Precondition Check
**Expert**: Brianna, CS Quality Assurance Lead (specializes in precondition audits)

**Brianna's Declaration Pass**: "I'm reading Table 1B looking for any Preconditions cell
that's vague, blank, or referencing something I haven't declared. A cell that says 'valid
state' or 'system ready' fails my audit." Brianna names each OP-ID she inspects.

**Brianna's Doc-vs-Trace Pass**: "Now I'm reading Step 2. I'm checking whether each step's
Preconditions line actually names the field and value that Table 1B requires. If a step
says 'preconditions met' without naming them, that's a missing check."

**If Brianna finds nothing**:
Brianna says: "For a declaration-level finding, I'd need Table 1B row [OP-ID] to have
a vague or blank precondition. That row currently says [what it says]. In the trace, I'd
need Step [N] for [OP-ID] to show a blank or generic precondition field. It currently
shows [what it shows]. The specific missing element would be [what would be absent]."

Phase 4B checkpoint:
- [ ] Brianna reviewed all Table 1B preconditions by name
- [ ] Brianna cross-checked Step 2 precondition fields against 1B
- [ ] Findings with Strength, OR Gap Records for both passes

---

### Phase 4C — Invariant Violation
**Expert**: Carmen, CS Compliance Officer (owns SLA and escalation policy enforcement)

**Carmen's Declaration Pass**: "I'm reading Table 1C and checking: does any INV-ID cover
a state that doesn't exist in 1A? Is any Falsification Test reachable via 1B operations
without a precondition that would block it?" Carmen names each INV-ID she checks.

**Carmen's Doc-vs-Trace Pass**: "Now I'm reading Step 2. I'm checking: when a step enters
or exits a state covered by one of my invariants, does the step show the invariant is
preserved? Does any After-state field value violate a threshold in 1C?"

**If Carmen finds nothing**:
Carmen says: "For a declaration finding, INV-[ID] would need a Falsification Test condition
reachable from 1B without a blocking precondition. The path is blocked by [named condition].
In the trace, the violation I'd need to see is Step [N] showing [field: violating value],
but it shows [field: actual value]. That's why I'm acquitting on this charge."

Phase 4C checkpoint:
- [ ] Carmen reviewed all INV-IDs against 1A states
- [ ] Carmen checked all invariant-relevant Step 2 transitions
- [ ] Findings with Strength, OR Gap Records

---

### Phase 4D — Race Condition
**Expert**: Devon, CS Platform Engineer (specializes in concurrent ticket processing)

**Devon's Declaration Pass**: "I'm checking Table 1B for operations sharing a From State
with no mutual exclusion clause in their preconditions. Two operations that can both start
from [S-ID] without one blocking the other is a race candidate."

**Devon's Doc-vs-Trace Pass**: "Now I'm reading the concurrent scenario in Step 2. Does
the trace actually show the conflict I'd expect? Does it name which operation wins and
how? Or does it only set up the scenario without showing the conflict resolution?"

**If Devon finds nothing**:
Devon says: "For a declaration-level race, I'd need two OP-IDs sharing a From State with
no mutual exclusion. The operations sharing [S-ID] are [OP-IDs]; their preconditions
[include/exclude] an exclusion clause. In the trace, the concurrent scenario in Step [N/N+1]
shows [what it shows]. To find a race here, the step would need to show [the missing
conflict element]."

Phase 4D checkpoint:
- [ ] Devon checked all shared-From-State pairings in 1B
- [ ] Devon reviewed the concurrent scenario steps in Step 2
- [ ] Findings with Strength, OR Gap Records

---

### Phase 4E — Undeclared ID Reference

No character needed for this one — it's a mechanical scan.

Go through every Step 2 step and every Phase 4A–4D finding. Check every S-ID, OP-ID,
and INV-ID against the Step 1 ID list. Flag any ID not on the list.

| Undeclared ID | Where It Appears | What Would Break |
|---------------|-----------------|-----------------|
| | | |

If no undeclared references: "Scanned Steps [N-N] and Phases 4A-4D. All IDs found in
Step 1 registry: [list the IDs checked]."

---

## Step 5 — Register

Consolidate all findings.

| A-ID | Phase | Pass | Type | OP-ID | S-ID | INV-ID | What Breaks | Strength |
|------|-------|------|------|-------|------|--------|-------------|----------|
| | | | | | | | | |

Quality gate: ≥ 2 findings. ≥ 1 at Strength ≥ 2. If you're below this, go back and check
your Gap Records — you may have acquitted where there was actually a finding.

---

## Step 6 — Reconciliation

Compare your Step 3 predictions to your Step 5 register.

| Type | Predicted | Found | C/FP/FN | Why It Surprised You (or didn't) |
|------|-----------|-------|---------|----------------------------------|
| Invalid transition | | | | |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |

Score = correct / 4. If < 60%: one sentence on what the declaration tables hid.
```

---

## V-05 — Combination: Output Format + Lifecycle Emphasis
**Axes**: Each C-26 anomaly phase contains its own inner dual-mode structure (inner Pass A: declaration-only; inner Pass B: doc-vs-trace diff) with independent exit gate checkboxes per inner pass. C-27 prejudice-dismissal fires separately for each inner pass. The four phases are top-level sequentially committed sections.
**Hypothesis**: Nesting C-28 inside each C-26 phase produces higher detection density than a global two-pass structure because the model applies the doc-vs-trace lens specifically tuned to each anomaly type. C-27 acquittal gaps accumulate independently per anomaly type per pass — four phases × two passes × potential gap record = eight structural gap slots, each evaluated at the moment of its specific acquittal rather than globally at sweep end.
**Domain**: Finance

---

```markdown
# trace-state Skill — Finance Domain

## Non-Negotiable Constraint

**Score at point of discovery**: When you identify a finding during any pass of any
phase, assign its Strength (1/2/3) immediately. Say: "Strength [N] — [clause]." Write it.
If you catch yourself assigning Strength to a finding you recorded earlier without a score,
stop. Return to that finding. Record Strength there. Then continue.

Retroactive Strength revision is prohibited. Adding a new evidence row is permitted.

Strength:
- 1 = Requires unusual or edge-case conditions
- 2 = Reachable in routine Finance workflows
- 3 = Demonstrated directly by named field values in the trace

---

## Phase 0 — Foundation

### Entity Selection
Choose a Finance entity: Invoice, Purchase Order, Expense Claim, Payment Voucher, Budget
Line, Credit Memo. Name it.

### Invariant Gate
Produce two invariants with specific numeric or temporal thresholds before building any
declaration table. These invariants must pass the falsification test — a domain expert
must be able to say "this would be violated if [field X] equaled [specific value]."

| INV-ID | Invariant Statement | Falsification Test (specific threshold) |
|--------|--------------------|-----------------------------------------|
| INV-01 | | Example: "Approval required when invoice amount > $10,000" |
| INV-02 | | Example: "Payment blocked if outstanding balance overdue > 30 days" |

Do not proceed to Phase 1 until both rows have a falsification test with a named amount,
percentage, date, or duration.

**Phase 0 Exit Gate**:
- [ ] Entity named
- [ ] INV-01 and INV-02 have specific falsification tests

---

## Phase 1 — Declaration Tables

### Table 1A — States
| S-ID | State Name | Entry Condition | Valid Exit Operations |
|------|------------|-----------------|----------------------|
| S-01 | | (specific field values, not "document is ready") | OP-IDs |
| (minimum 5 states) | | | |

### Table 1B — Operations
| OP-ID | Operation | From State(s) | To State | Preconditions | Postconditions |
|-------|-----------|---------------|----------|---------------|----------------|
| OP-01 | | S-IDs | S-ID | (field: value) | (field: value) |
| (minimum 7 operations) | | | | | |

### Table 1C — Invariants
| INV-ID | Statement | Applies To States | Falsification Test |
|--------|-----------|------------------|--------------------|
| INV-01 | (from Phase 0) | S-IDs | |
| INV-02 | (from Phase 0) | S-IDs | |
| (additional invariants as needed) | | | |

### 1D — ID Registry
List all declared S-IDs, OP-IDs, INV-IDs. This registry is the reference point for Phase
4E undeclared-reference detection. Any downstream ID not on this list is a finding.

**Phase 1 Exit Gate**:
- [ ] ≥ 5 states with non-generic Entry Conditions
- [ ] ≥ 7 operations with field-level preconditions and postconditions
- [ ] ≥ 3 invariants (including Phase 0 invariants)
- [ ] ID registry complete

---

## Phase 2 — Trace Construction

Build the lifecycle as numbered steps.

Required coverage:
1. **Normal path** — ≥ 5 steps showing the primary Finance workflow
2. **Rejected transition** — ≥ 1 step where an operation is blocked. Name the failing
   precondition by field and value. Name the rejection outcome.
3. **Concurrent scenario** — ≥ 1 step pair. Name: two OP-IDs that could interleave on
   the same entity, the resulting state conflict (by S-ID), and which operation wins.

```
Step N — [OP-ID]: [Operation Name]
  Before: [S-ID] — [State Name] | [field: value, field: value]
  Preconditions: [field: value — "preconditions met" does not count]
  After: [S-ID] — [State Name] | [changed fields: new values]
  Postconditions: [named guarantees by field]
```

**Phase 2 Exit Gate**:
- [ ] ≥ 7 steps with complete before/after field snapshots
- [ ] ≥ 1 rejected-transition step with named precondition failure
- [ ] ≥ 1 concurrent scenario with named state conflict

---

## Phase 3 — Pre-Sweep Hypothesis

Read Tables 1A–1C only. Do not read Phase 2.

For each anomaly type: predict found or not found. State the declaration evidence by ID.

| Anomaly Type | Predicted | Declaration Evidence (ID) | Confidence |
|--------------|-----------|--------------------------|-----------|
| Invalid transition | | | |
| Missing precondition check | | | |
| Invariant violation | | | |
| Race condition | | | |

**Phase 3 Exit Gate**:
- [ ] All four rows complete with ID-based reasoning
- [ ] Phase 2 was not read during this phase

---

## Phase 4 — Anomaly Phases (Sequential, Each with Inner Dual-Mode Structure)

**Sequential Commitment**: Phases 4A → 4B → 4C → 4D → 4E in order. A phase's exit gate
must be fully checked before the next phase begins.

**Inner Structure for Each Phase (4A–4D)**:

Each anomaly phase contains two inner passes:

> **Inner Pass i — Declaration Analysis**: Read Tables 1A–1C only. Find this anomaly type
> from the declared behavior alone. Does the declared state machine, without consulting the
> trace, contain the conditions for this anomaly?

> **Inner Pass ii — Doc-vs-Trace Diff**: Read Phase 2. Diff declared behavior against
> traced behavior. A claim in declarations not demonstrated in any Phase 2 step is a
> finding. A step in Phase 2 that contradicts declarations is a finding.

Both inner passes run independently. A finding in Pass i does not exempt Pass ii from
running (different detection paths may surface different findings). A "no finding" verdict
in Pass i does not carry over to Pass ii.

**Inner Acquittal Rule**: If an inner pass produces "no finding", produce a Gap Record for
that pass before the phase exit gate is checked. The Gap Record names the specific
declaration entry, step number, or field value that would need to exist to produce the
finding in that pass. "Nothing found" is not a Gap Record.

---

### Phase 4A — Invalid State Transition

**Inner Pass i (Declaration-Only)**:
Read Table 1B From States and Table 1A Entry Conditions. Does any operation declare a
From State that has no valid path to it per Table 1A? Is any state-to-state transition
internally contradictory in the declaration?

Finding row format:
```
FINDING i-4A-NN:
  OP-ID: [OP-ID] | From State: [S-ID]
  Declaration says: [what 1B declares as valid From State]
  Entry Condition conflict: [what 1A says about that state's reachability]
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass i):
"For an invalid transition to appear in declarations alone, Table 1B would need [OP-ID]
listed with From State [S-ID], but Table 1A Entry Condition for [S-ID] would need to
contradict it. The [OP-ID]/[S-ID] combination that comes closest is [describe]. It is
not a finding because [one sentence naming the condition that makes the From State valid]."

**Inner Pass ii (Doc-vs-Trace Diff)**:
Read Phase 2 steps. For each step, check: is the Before S-ID in the From States declared
for that OP-ID in Table 1B? Also check: is any declared valid transition in 1B absent
from the trace when it should have been exercised? Absence of a documented claim is a
finding.

Finding row format:
```
FINDING ii-4A-NN:
  Step: [Step N] | OP-ID: [OP-ID] | Before S-ID: [S-ID]
  Table 1B declares: [what From States are permitted]
  Trace shows: [what Step N shows as Before state]
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass ii):
"For a doc-vs-trace transition finding, Step [N] would need to show [OP-ID] executing from
[S-ID] that is not in Table 1B's From States. Step [N] shows Before=[current S-ID], which
is [in/not in] the declared set. Additionally, Table 1B declares [OP-ID] as valid from
[S-ID] — that transition would need to be exercised. Step [step that would exercise it]
is [present/absent] in the trace."

**Phase 4A Exit Gate**:
- [ ] Pass i complete — verdict recorded
- [ ] Pass ii complete — verdict recorded
- [ ] Gap Record for Pass i if no finding (names specific ID combination)
- [ ] Gap Record for Pass ii if no finding (names specific step + 1B comparison)
- [ ] Strength at discovery for all findings

---

### Phase 4B — Missing Precondition Check

**Inner Pass i (Declaration-Only)**:
Read Table 1B. Is any Preconditions cell blank, vague ("data valid", "system ready"), or
referencing an ID not in the Phase 1D registry? Name each OP-ID inspected.

Finding format:
```
FINDING i-4B-NN:
  OP-ID: [OP-ID]
  Precondition cell says: [what it says]
  Issue: blank / vague / undeclared ID reference
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass i):
"Reviewed Table 1B rows: [OP-IDs reviewed]. Each Preconditions cell names at least one
specific field and value. The row that comes closest to a gap is [OP-ID], which says
[what it says]. It passes because [one sentence naming what makes it specific enough]."

**Inner Pass ii (Doc-vs-Trace Diff)**:
For each Phase 2 step, check: does the Preconditions line name the field and value
required by Table 1B for that OP-ID? Does the step demonstrate the precondition is met,
or assert it without naming field values?

Finding format:
```
FINDING ii-4B-NN:
  Step: [Step N] | OP-ID: [OP-ID]
  Table 1B requires precondition: [field: value]
  Step shows: [what the Preconditions line actually says]
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass ii):
"Checked Steps [N-N] for [OP-IDs]. Table 1B precondition for [OP-ID] is [condition].
Step [N] shows [matching field: value]. The step that would expose a gap would show
[what a missing precondition check looks like in the step format]. No step shows that."

**Phase 4B Exit Gate**:
- [ ] Pass i complete — all 1B rows inspected by name
- [ ] Pass ii complete — all step preconditions cross-checked against 1B
- [ ] Gap Records for no-finding passes
- [ ] Strength at discovery

---

### Phase 4C — Invariant Violation

**Inner Pass i (Declaration-Only)**:
Read Table 1C. Does any INV-ID reference an S-ID not in Table 1A? Is any Falsification
Test condition reachable via Table 1B operations without a blocking precondition or
entry condition?

Finding format:
```
FINDING i-4C-NN:
  INV-ID: [INV-ID]
  Applies to: [S-IDs]
  Issue: [undeclared S-ID reference / reachable falsification path]
  Path: [OP-ID sequence that reaches the violation without a block]
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass i):
"For INV-[ID]: Falsification Test condition is [threshold]. The path to violate it would
need [OP-ID] to transition from [S-ID] to [S-ID] without a precondition blocking it.
Table 1B shows [OP-ID]'s preconditions include [blocking condition]. That block is
present, which is why no declaration-level violation is detectable."

**Inner Pass ii (Doc-vs-Trace Diff)**:
For each INV-ID, identify the Phase 2 steps that enter or exit states it covers. Does
any step's After-state field values violate the invariant's threshold? Does any step skip
a state where the invariant should have been checked?

Finding format:
```
FINDING ii-4C-NN:
  Step: [Step N] | INV-ID: [INV-ID]
  State entered: [S-ID] | Field in question: [field: after-value]
  INV-[ID] requires: [threshold or condition]
  Violation: [how the after-value breaches the requirement]
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass ii):
"INV-[ID] applies to states [S-IDs]. Steps that enter these states: [Step N, N+1].
Step [N] After-state shows [field: value]. INV-[ID] Falsification Test threshold is
[threshold]. The value [does/does not] breach the threshold. To find a violation, the
step would need to show [field: violating value]. It shows [actual value] instead."

**Phase 4C Exit Gate**:
- [ ] Pass i complete — all INV-IDs checked against 1A and 1B
- [ ] Pass ii complete — invariant-relevant steps identified and checked
- [ ] Gap Records for no-finding passes
- [ ] Strength at discovery

---

### Phase 4D — Race Condition

**Inner Pass i (Declaration-Only)**:
Read Table 1B. Identify all shared-From-State pairings: OP-IDs with overlapping From
States. For each pairing, check whether preconditions include a mutual exclusion clause.

Finding format:
```
FINDING i-4D-NN:
  OP-IDs: [OP-ID1] and [OP-ID2] | Shared From State: [S-ID]
  OP-ID1 preconditions: [what they say about exclusion]
  OP-ID2 preconditions: [what they say about exclusion]
  Gap: no mutual exclusion clause — both can execute concurrently
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass i):
"Shared-From-State pairings in Table 1B: [list]. For pair [OP-ID1 + OP-ID2] sharing [S-ID]:
OP-ID1 preconditions include [exclusion clause]. OP-ID2 preconditions include [exclusion
clause]. These clauses would need to be absent for a declaration-level race. They are
present, which is why no race is detectable from 1B alone."

**Inner Pass ii (Doc-vs-Trace Diff)**:
Read the concurrent scenario step(s) from Phase 2. Does the trace demonstrate the
conflicting state outcome? Does the step name the winner and detection mechanism, or only
set up the race without resolving it? Does the concurrent scenario align with the
shared-From-State pairings identified in Pass i?

Finding format:
```
FINDING ii-4D-NN:
  Steps: [Step N] and [Step N+1]
  Table 1B declares: [what the From States and preconditions say about these OP-IDs]
  Trace shows: [what the concurrent scenario steps actually demonstrate]
  Gap: [what the trace claims vs. what the declaration requires — or the missing resolution]
  Strength: [1/2/3 — now]
```

Gap Record (if no finding in Pass ii):
"Concurrent scenario steps: Step [N] and [N+1]. They show [OP-IDs] potentially
interleaving on [S-ID]. Table 1B From States for these OP-IDs: [confirmed]. The trace
step shows conflict [named/not named] and resolution [named/not named]. To find a
doc-vs-trace race finding, the trace would need to show the conflict but not name
the resolution, or show a resolution method not covered by 1B preconditions. The current
steps show [what they show], which [does/does not] expose a gap."

**Phase 4D Exit Gate**:
- [ ] Pass i complete — all shared-From-State pairings checked for exclusion clauses
- [ ] Pass ii complete — concurrent scenario steps mapped against 1B declarations
- [ ] Gap Records for no-finding passes
- [ ] Strength at discovery

---

### Phase 4E — Undeclared ID Reference

Scan all Phase 2 steps and all Phase 4A–4D findings (all passes) for IDs not in the
Phase 1D registry.

| Undeclared ID | Location | Pass | Production Consequence |
|---------------|----------|------|----------------------|
| | | | |

No finding: "Scanned Phase 2 Steps [list] and Phase 4A–4D Passes i and ii. IDs appearing
in these locations: [list]. All confirmed in Phase 1D registry."

**Phase 4E Exit Gate**:
- [ ] Full scan of Phase 2 and all Phase 4 passes against 1D registry
- [ ] Verdict with scan evidence

---

## Phase 5 — Anomaly Register

| A-ID | Phase | Pass | Type | OP-ID | S-ID | INV-ID | What Breaks | Strength |
|------|-------|------|------|-------|------|--------|-------------|----------|
| | | i or ii | | | | | | |

Rules:
- No blank cells in found rows. "N/A: [reason]" for non-applicable ID columns.
- Strength values must match point-of-discovery scores. No revision.
- Quality gate: ≥ 2 findings total. ≥ 1 with Strength ≥ 2.
  If below this gate: review Gap Records — a well-specified Gap Record sometimes reveals
  that the acquittal was premature. Return to that phase if so.

---

## Phase 6 — Reconciliation

Compare Phase 3 predictions against Phase 5 register.

| Anomaly Type | Predicted | Found (Pass i/ii/both) | C/FP/FN | Surprise |
|--------------|-----------|------------------------|---------|---------|
| Invalid transition | | | | One sentence why outcome matched or violated prediction |
| Missing precondition | | | | |
| Invariant violation | | | | |
| Race condition | | | | |

- **C** = Correct | **FP** = Predicted found, not found | **FN** = Not predicted, found

Calibration = correct / 4. If < 60%: one sentence diagnosing what structural feature the
hypothesis model missed and whether the dual-pass structure revealed it.

Note whether the finding surfaced in Pass i (declaration-only) or Pass ii (doc-vs-trace)
— this indicates whether the gap lived in the declared model or in the implementation trace.
```

---

## Variation Summary

| Variation | Axis | Domain | C-26 Mechanism | C-27 Mechanism | C-28 Mechanism | Hypothesis to Test |
|-----------|------|--------|----------------|----------------|----------------|-------------------|
| V-01 | Role Sequence | CS | 4 sequential anomaly phases | Dedicated Acquittal Advocate sub-role fires on "no finding" verdict | Per-phase dual pass (A: declarations, B: doc-vs-trace) | Separation of detection and dismissal roles produces richer gap maps |
| V-02 | Output Format | Finance | Four anomaly phases inside each of two major document sections | Per-phase no-finding rule within each major section | Major document sections ARE the two passes (Pass A = entire Section 4, Pass B = entire Section 5) | Document-level pass separation forces genuinely independent detection; model cannot conflate |
| V-03 | Lifecycle Emphasis | Sales | 4 sequential anomaly phases, each with dual-pass | Prejudice-dismissal embedded as a named checklist item in the phase exit gate (fires at acquittal moment) | Per-phase dual pass with independent exit gate checkboxes per pass | Temporal proximity of C-27 instruction to the acquittal moment produces fuller gap maps than preamble placement |
| V-04 | Role + Register | CS | 4 phases, each owned by a named domain expert character | Character must voice prejudice-dismissal before their phase closes | Character runs inner declaration pass then doc-vs-trace pass, narrates both | Workshop register + character ownership primes domain vocabulary at anomaly-detection time |
| V-05 | Format + Lifecycle | Finance | 4 sequential anomaly phases as primary structure | C-27 fires independently per inner pass (i and ii) within each phase — 8 potential gap slots | Each C-26 phase contains its own inner Pass i (declaration-only) + Pass ii (doc-vs-trace diff) | Per-phase nested dual-mode produces highest detection density; C-27 accumulates independently per anomaly type per pass |
