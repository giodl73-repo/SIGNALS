# trace-state Variate — Round 2
**Date:** 2026-03-15
**Rubric:** v2 (C-01..C-11; golden: all essential pass AND composite >= 80)
**New criteria:** C-10 (gate enforcement — formal gates reference criteria by name/ID) and C-11 (inertia challenge pre-trace — adversarial generation precedes happy-path commitment)
**Scoring formula:** essential 60 + recommended 30 + aspirational 10 (4 criteria, 2.5 pts each)

---

## Round 2 Situation

R1 results under rubric v1 (C-01..C-09):
- V-05 scored 100 (inertia + table + boundary coverage)
- V-04 scored 97.5 (GATE pattern + boundary coverage; PHASE B prose blocks = C-08 partial)
- V-02/V-01/V-03 scored 90-95 (no C-09; V-03 also no C-08)

R1 under v2 scoring (retroactive):
- V-05: C-10 FAIL (no formal gates), C-11 PASS → 97.5
- V-04: C-08 PARTIAL, C-10 PASS, C-11 FAIL → ~96
- No R1 variation achieves all four aspirational

**R2 objective:** Structural guarantee for C-08 (transition table), C-09 (boundary coverage), C-10 (named gate enforcement), AND C-11 (inertia challenge precedes tracing).

---

## Round 2 Variation Map

| Var | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | Hypothesis |
|-----|------|------|------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | Inertia-as-spine | exp | exp | exp | exp | exp | exp | exp | exp | ? | ? | exp | When inertia assumptions become the organizing column in the transition table, C-11 is structural (inertia precedes any row fill) and C-08 is structural (the table IS the trace); C-09 uncertain without explicit boundary section |
| V-02 | Three-gate model (GATE C added) | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | ? | GATE C enumerates C-08, C-09, C-10, C-11 by criterion ID — a writer who reaches GATE C and cannot check C-08 must backtrack; C-11 uncertain because no inertia step is mandated |
| V-03 | Conversational voice + mandatory format | exp | exp | exp | exp | exp | exp | exp | exp | exp | ? | ? | Conversational reasoning sections produce richer preconditions than imperative prompts; mandatory table + explicit boundary section force C-08 and C-09; C-10 and C-11 uncertain without gate or inertia structure |
| V-04 | Four-phase synthesis (GATE + Inertia) | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | Combining V-04 and V-05 from R1: PHASE B locks inertia before PHASE C tracing (C-11 structural), four gates enforce all structural criteria (C-10 structural), mandatory transition table in PHASE C (C-08 structural), D3 boundary section (C-09 structural) |
| V-05 | Boundary-first + inertia + gate | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | Terminal states as Phase A anchors make C-09 the organizing principle; inertia challenge asks what process assumes about reaching terminals (C-11 structural); gate references C-09/C-11 by name (C-10 structural); transition table mandated (C-08 structural) |

---

## V-01 — Inertia as Structural Spine

**Axis:** Inertia framing intensity (single axis)
**Hypothesis:** In R1, V-05 used inertia as a pre-step that *fed* the transition table. V-01 makes inertia the spine: the transition table has an "Inertia Assumption" column, so every row is interrogated — "what process assumption is this operation testing?" Operations with no matching inertia assumption reveal the *implicit* assumptions the Domain Expert failed to name. The table structure (C-08) is guaranteed because it is the primary deliverable. C-11 is guaranteed because the inertia table is filled before any trace row can reference it. C-09 is uncertain — boundary coverage requires an explicit section this variation does not mandate.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace organized around process assumptions. Every operation is interrogated with the same question: *what current-process assumption is this operation testing, and does the platform enforce it?* The inertia assumption is the primary column; the transition mechanics are secondary.

---

### ROLES

**[D] Domain Expert**
Auto-selected from context: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Active / On Hold / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: PROCESS ASSUMPTION MAP, INVARIANT DECLARATION.

**[T] Trace Developer**
Owns: TRANSITION TABLE, ASSUMPTION VERDICTS, RACE CONDITIONS, FINDINGS.

---

### STEP 1 — PROCESS ASSUMPTION MAP [D]

Declare the entity and state vocabulary, then inventory the assumptions the current manual process makes.

**Entity:** [name and entity type]
**Domain:** [Sales | Customer Service | Finance]

**State vocabulary** — domain terms only; no generic labels:

| State Name | Defining Field Values | Terminal? |
|-----------|---------------------|-----------|

**Operation registry:**

| Operation | Legal Source States | Target State |
|-----------|-------------------|-------------|

**Process assumption map** — what does the current process (spreadsheet, email, legacy system, verbal agreement, paper form) assume about operation order or preconditions that the platform may NOT enforce?

| # | Current Process Assumption | Platform Enforced? (Y/N) | If N: Expected Behavior Without Enforcement |
|---|--------------------------|--------------------------|---------------------------------------------|

*Discovery prompts by domain:*
- *Sales:* "Everyone knows you don't close a deal without a signed contract" — is that a state gate or a convention?
- *CS:* "Agents escalate before resolving priority cases" — platform-enforced or manager-enforced?
- *Finance:* "Finance approves before anyone posts" — is approval a state precondition or a manual step?

Minimum two assumptions. At least one must be marked Platform Enforced = N.

---

### STEP 2 — INVARIANT DECLARATION [D]

| ID | Name | Checkable Assertion | Authority Source |
|----|------|--------------------|-----------------|

Minimum two invariants. At least one must derive from a Platform Enforced = N assumption in STEP 1 (the assumption, when unenforced, is a potential invariant violation). Authority source: business rule name, SLA contract clause, accounting regulation, or policy.

---

### STEP 3 — TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | Inertia Assumption | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Column rules:**

- **Inertia Assumption:** Reference the row number from STEP 1 (e.g., "IA-2"). If this operation does not correspond to any declared assumption, write "[Implicit]" — implicit assumptions are findings candidates because they were never named.
- **From State / To State:** Domain vocabulary from STEP 1 only. Never blank.
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == Active`, `owner != null`, `SLA timer is paused`).
- **Postconditions:** Minimum one assertion distinct from the To State name. Assert a property of the ending state, not just its label.
- **INV-01 / INV-02:** `HOLDS` or `VIOLATED — [reason]`. Never blank.
- **Side Effects:** Triggered plugins, business rules, related record changes, notifications, async jobs.

---

### STEP 4 — ASSUMPTION VERDICTS [T]

For every STEP 1 row, record the verdict based on what the trace revealed:

| # | Assumption | Verdict | Evidence (table row or finding) |
|---|------------|---------|--------------------------------|

Verdicts: **ENFORCED** (platform blocked the violation), **UNENFORCED** (platform allows — finding required), or **PARTIAL** (some paths enforce, others do not — describe).

**Every UNENFORCED verdict generates an invalid transition:**

| Attempted Operation | From State | Blocking Condition (if any) | Inertia Row | Risk if Bypassed |
|--------------------|------------|---------------------------|-------------|-----------------|

If Blocking Condition is empty, the platform allows the operation — this is a finding, not just an invalid transition.

---

### STEP 5 — RACE CONDITIONS [T]

Identify concurrent access risks or explicitly clear them.

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If no concurrent access is possible: "No concurrent access — [reason]."

---

### STEP 6 — FINDINGS [D + T]

Priority order. Reference table row and inertia assumption number.

- **P[N]:** [title] — [description, row reference, inertia assumption reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: State Vocabulary, Operation Registry, Process Assumption Map, Invariant Registry, Transition Table, Assumption Verdicts, Invalid Transitions, Race Conditions, Findings.

---

## V-02 — Three-Gate Model (GATE C Added)

**Axis:** Gate granularity (single axis)
**Hypothesis:** R1 V-04 had GATE A (pre-trace declaration) and GATE B (post-trace completeness). Both referenced specific fields to check, which is why V-04 passed C-10 under v2. The gap: no gate after adversarial review. GATE C explicitly enumerates C-08, C-09, C-10, and C-11 by criterion ID — a writer who reaches GATE C cannot confirm C-11 without having done a pre-trace adversarial step, and cannot confirm C-08 without having filled the transition table. The gate creates backpressure: failing any gate item requires return to the relevant phase, not a note to self. C-11 is uncertain because this variation does not mandate a specific inertia challenge — GATE C asks whether one was done, but does not force it structurally before tracing.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace using a three-gate model. Each gate is a named checkpoint that references specific criteria. A gate that cannot be confirmed is a blocker — return to the relevant phase, correct, and re-confirm before advancing. Gates do not bend.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead/Opportunity/Proposal/Closed), CS expert (New/Active/On Hold/Pending/Resolved/Closed), Finance expert (Draft/Submitted/Approved/Posted/Paid/Voided).
Owns: PHASE A.

**[T] Trace Developer**
Owns: PHASE B, PHASE C.

---

### PHASE A — DECLARATION [D]

#### A1 — Entity and State Vocabulary

| State Name | Field Values | Entry Conditions | Terminal? |
|-----------|-------------|-----------------|-----------|

Domain vocabulary only.

#### A2 — Operation Registry

| Operation | Legal Source States | Target State | Triggering Actor |
|-----------|-------------------|-------------|-----------------|

#### A3 — Invariant Registry

| ID | Invariant Name | Checkable Assertion | Authority Source |
|----|---------------|--------------------|--------------------|

Minimum two invariants. Authority source: business rule, SLA clause, regulation, or policy.

---

### GATE A — DECLARATION GATE

Confirm each item before starting PHASE B. Unconfirmed = blocked.

- [ ] **[C-04]** All state names use domain vocabulary — no "State A", "initial", "final", or numbered generics
- [ ] **[C-01]** Every operation in A2 has enumerated legal source states and a single target state
- [ ] **[C-03]** At least two invariants in A3 with checkable assertions and authority sources
- [ ] Entity and domain are explicitly declared

**Any item unconfirmed → return to PHASE A.**

---

### PHASE B — PER-OPERATION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Per-operation format:

```
OPERATION [N]: [name from A2]
  Starting state:   [from A1 vocabulary] — [key field values]
  Preconditions:    [minimum two testable assertions]
  Processing:       [plugins, business rules, calculations, messages that execute]
  Ending state:     [from A1 vocabulary] — [updated field values]
  Postconditions:   [minimum one assertion distinct from the state name]
  Side effects:     [related records, notifications, async jobs]
  Invariant check:
    - [INV-ID] [name]: HOLDS | VIOLATED — [reason]
    (check every invariant from A3 per operation)
```

**Transition table** — fill in parallel with per-operation blocks:

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

---

### GATE B — TRACE COMPLETENESS GATE

Confirm each item before starting PHASE C. Unconfirmed = blocked.

- [ ] **[C-01]** Every operation has a named starting state AND named ending state
- [ ] **[C-02]** Every operation has at least two preconditions as testable assertions
- [ ] **[C-03]** Every invariant from A3 is checked (HOLDS or VIOLATED) for every operation
- [ ] **[C-06]** Every operation has at least one postcondition distinct from the ending state name
- [ ] **[C-08]** Transition table is present and complete — every operation appears as a table row; no operation exists only in prose

**Any item unconfirmed → return to PHASE B.**

---

### PHASE C — ADVERSARIAL REVIEW [T]

#### C1 — Invalid Transitions

| Attempted Operation | From State | Blocking Condition | Precondition or INV Reference | Risk if Bypassed |
|--------------------|------------|-------------------|-----------------------------|-----------------|

Minimum one row.

#### C2 — Race Conditions

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If cleared: "No concurrent access — [reason]."

#### C3 — Boundary Coverage

- **Initial state:** [name; confirm it appears in A1 with Terminal = No]
- **Terminal states:** [list all; confirm each is marked Terminal = Yes in A1]
- **Re-entry blocked:** Trace one attempt to execute an operation from a terminal state. Show the blocking condition (which precondition or invariant prevents it).

---

### GATE C — COVERAGE AND ASPIRATIONAL GATE

Confirm each item before writing FINDINGS. Unconfirmed = blocked.

- [ ] **[C-05]** At least one row in C1 with a named blocking condition
- [ ] **[C-07]** C2 addressed — at least one race row OR explicit clearance with reason
- [ ] **[C-09]** C3 complete — initial state labeled, at least one terminal state, re-entry blocked
- [ ] **[C-08]** Transition table from GATE B confirmed complete (all rows present)
- [ ] **[C-10]** All three gates (A, B, C) are present in this trace output and each references at least one criterion by ID or name
- [ ] **[C-11]** Was a pre-trace adversarial step (inertia challenge, process assumption mapping, or equivalent) performed BEFORE filling the PHASE B table? If yes: confirm at least one invalid transition in C1 is derived from it. If no: note whether one would have helped surface additional findings.

**Any item unconfirmed → correct the relevant phase.**

---

### FINDINGS

Priority order. Reference PHASE and gate.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: PHASE A (A1, A2, A3), PHASE B per-operation trace + transition table, PHASE C (C1 invalid transitions, C2 race conditions, C3 boundary coverage), FINDINGS.

---

## V-03 — Conversational Voice + Mandatory Format

**Axis:** Phrasing register (single axis)
**Hypothesis:** R1 V-03 was the richest in reasoning depth but scored 90 — the lowest of the five. Both failures were format failures (C-08, C-09), not reasoning failures. This variation keeps the conversational first-person reasoning voice that produced the richest precondition documentation in R1, but adds two structural mandates: (a) after each conversational reasoning section, a table row must be filled; (b) a dedicated boundary coverage section is required. The conversational voice is the *how you think*; the tables are *what you produce*. C-10 and C-11 remain uncertain — no gates, no inertia mandate.

---

You are running a **trace-state** signal for: {{topic}}

Walk through this state machine as an expert explaining it to a developer who is new to this domain. Think out loud — reason about preconditions, postconditions, and invariants as you narrate. Every time you finish reasoning about an operation, record it in the table. The conversation is how you think; the tables are what you build.

Pick the role that fits {{topic}}:

- **Sales Expert** — you live in the Lead → Opportunity → Proposal → Close lifecycle; you know every qualification gate and every reason a deal stalls
- **Customer Service Expert** — you know the Case lifecycle and SLA timers cold; you have felt the pain of a Resolved case that re-opens after the timer stops
- **Finance Expert** — you understand every Journal → Posting → Payment state transition; you know why the Voided state exists and what it prevents

---

### Part 1 — Tell me about this state machine

Before tracing any operations, explain the entity:

**1a.** What are we tracing? Name the entity, its entity type, and its purpose in this domain.

**1b.** What states can it be in? Think through the full lifecycle — from the moment it is created to the moment it is done (or the moment it fails). Use real domain names. Fill this table as you explain:

| State Name | Defining Field Values | Terminal? |
|-----------|---------------------|-----------|

**1c.** What operations can change its state? Tell me the legal transitions.

| Operation | Legal Source States | Target State | Triggering Actor |
|-----------|-------------------|-------------|-----------------|

**1d.** What must always be true? Think about what would indicate a bug or data corruption if violated. Name at least two invariants as conditions you could check in a test. Tell me *why* each one matters in your domain — what bad outcome it prevents.

| ID | Name | Checkable Assertion | Why This Matters |
|----|------|--------------------|-----------------|

---

### Part 2 — Walk me through a concrete sequence

Pick a realistic scenario — real field values, a real user type, a timestamp that makes sense in your domain.

**Scenario:** [describe the entity instance, who's involved, what state we start from, what the goal is]

For each operation, reason out loud first, then fill the row:

*Think out loud:* "Before I can [operation], I check that... What actually happens when this fires is... After this, the record should show..."

*Then record it:*

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Row rules:**
- **Preconditions:** Minimum two testable assertions per row. Not just "record exists" — be specific: `status == Active`, `SLA timer is running`, `approver role is assigned`.
- **Postconditions:** At least one assertion that is NOT just the To State name. What property of the ending state must hold? `Audit entry created`, `SLA timer paused`, `total_amount recalculated`.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`. Never blank. Checking invariants per row is not optional.

---

### Part 3 — Push on it

**3a. Invalid transitions:** What would someone try from the current state that would fail? Walk me through why — which precondition blocks it, which invariant it would violate. Give at least one example. Then record it:

| Attempted Operation | From State | Blocking Condition | INV or Precondition Reference | Risk if Bypassed |
|--------------------|------------|-------------------|-----------------------------|-----------------|

**3b. Race conditions:** If a user and an automated process both tried to touch this record at the same time, what's the unsafe interleaving? Walk me through the scenario. If it can't happen, tell me why.

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If cleared: "No concurrent access — [reason]."

**3c. Boundary states:** Walk me through the edges of this entity's life.

- **Brand new:** What does a freshly created [entity] look like? What is its initial state? What field values define it at creation?
- **Done:** What does "done" look like? Name all the terminal states — states from which no further operations are legal. For each: what does it mean in the domain?
- **Trying to exit done:** Pick a terminal state. Walk me through what happens if someone tries to run an operation on it. Which precondition or invariant blocks it? Fill this:

| Attempted Operation | Terminal State | Blocking Condition |
|--------------------|---------------|-----------------|

---

### Part 4 — What did we learn?

Summarize what the trace surfaced — surprises, invariant violations, invalid transitions you wouldn't have thought of without the walk-through, race conditions the platform needs to handle. Priority order.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: State vocabulary table, operation registry, invariant table, transition table, invalid transitions table, race conditions, boundary coverage (initial state, terminal states, re-entry attempt), findings.

---

## V-04 — Four-Phase Synthesis (GATE + Inertia)

**Axis:** Combined — role sequence + GATE enforcement + inertia challenge + mandatory table
**Hypothesis:** R1 V-04 achieved 97.5 by structural gate enforcement but missed C-08 (PHASE B used prose operation blocks, not a columnar table) and missed C-11 (no inertia step). R1 V-05 achieved 100 by inertia + table + boundary coverage, but missed C-10 (no formal gates). V-04 (R2) combines both: four phases (Declaration → Inertia → Trace → Adversarial), four gates, mandatory transition table in PHASE C, and an inertia challenge as PHASE B that precedes tracing. PHASE C fixes the R1 V-04 C-08 gap by requiring a columnar table as the PHASE C output (not prose blocks with an optional table). GATE D references C-10 and C-11 explicitly, creating the complete coverage.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace in four phases. Each phase is owned by a specific role. A GATE checkpoint must pass before advancing to the next phase. Gates reference specific criteria; they cannot be skipped or loosely confirmed.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead/Opportunity/Proposal/Closed-Won/Closed-Lost), CS expert (New/Active/On Hold/Pending/Resolved/Closed), Finance expert (Draft/Submitted/Approved/Posted/Paid/Voided).
Owns: PHASE A (declaration), PHASE B (inertia challenge).

**[T] Trace Developer**
Owns: PHASE C (transition trace), PHASE D (adversarial review).

---

### PHASE A — STATE MACHINE DECLARATION [D]

#### A1 — Entity and State Vocabulary

| State Name | Field Values | Entry Conditions | Terminal? |
|-----------|-------------|-----------------|-----------|

Domain vocabulary only.

#### A2 — Operation Registry

| Operation | Legal Source States | Target State | Triggering Actor |
|-----------|-------------------|-------------|-----------------|

#### A3 — Invariant Registry

| ID | Invariant Name | Checkable Assertion | Authority Source |
|----|---------------|--------------------|--------------------|

Minimum two invariants. Authority source: business rule name, SLA contract clause, accounting regulation, or policy.

---

### GATE A

- [ ] **[C-04]** All state names use domain vocabulary — no "State A", "initial", "final"
- [ ] **[C-01]** Every operation in A2 has enumerated legal source states and a single target state
- [ ] **[C-03]** At least two invariants in A3 with checkable assertions and authority sources
- [ ] Entity and domain explicitly declared

**Unconfirmed → return to PHASE A.**

---

### PHASE B — INERTIA CHALLENGE [D]

Before the Developer traces any operation, challenge the process assumptions for {{topic}}.

**Core question:** What does the current manual process (spreadsheet, email, legacy system, verbal convention, paper form) assume about operation order or preconditions that the platform does NOT enforce?

| # | Current Process Assumption | Platform Enforced? (Y/N) | If N: Expected Enforcement Gap |
|---|--------------------------|--------------------------|-------------------------------|

*Discovery prompts by domain:*
- *Sales:* "Opportunity can only be Closed Won if a signed contract exists — is that a state gate?"
- *CS:* "Cases require customer confirmation before Resolved — platform-enforced or verbal?"
- *Finance:* "Invoices require manager approval before Posting — state precondition or manual step?"

Minimum two assumptions. Every row with Platform Enforced = N is a candidate invalid transition for PHASE D.

---

### GATE B

- [ ] At least two process assumptions documented
- [ ] Every assumption has a Platform Enforced verdict (Y/N)
- [ ] At least one assumption marked N (if genuinely none: document why — fully automated pipelines with zero manual handoffs are rare and the explanation is itself a finding)
- [ ] All N rows have an Expected Enforcement Gap named

**Unconfirmed → return to PHASE B.**

---

### PHASE C — TRANSITION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

**Transition table** — primary deliverable for PHASE C. All operations are rows; no operation exists only in prose.

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Column rules:**
- **From State / To State:** Vocabulary from A1 only. Never generic.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank. Add INV-03, INV-04 columns if A3 has more invariants.
- **Side Effects:** Triggered plugins, business rules, related record changes, notifications, async jobs.

For operations with significant branching logic, add a sub-block beneath the row:

```
OPERATION [N] detail:
  Processing:   [plugins, business rules, calculations that execute]
  Branching:    [conditions that alter the Processing path]
```

---

### GATE C

- [ ] **[C-01]** Every row has a named From State and named To State from A1
- [ ] **[C-02]** Every row has at least two preconditions as testable assertions
- [ ] **[C-03]** Every invariant from A3 is checked (HOLDS or VIOLATED) in every row
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] **[C-08]** Transition table is present and complete — all operations are rows; no operation exists only in prose

**Unconfirmed → return to PHASE C.**

---

### PHASE D — ADVERSARIAL REVIEW [T]

#### D1 — Invalid Transitions

Start with PHASE B rows where Platform Enforced = N. For each: does the platform actually block it, or does it allow the transition?

| Attempted Operation | From State | Blocking Condition | PHASE B Row | Risk if Bypassed |
|--------------------|------------|-------------------|-----------|-----------------|

Every PHASE B N-row must appear in D1. Add any additional invalid transitions not from PHASE B.

Minimum: one row total.

#### D2 — Race Conditions

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

#### D3 — Boundary Coverage

- **Initial state:** [name; confirm in A1, Terminal = No]
- **Terminal states:** [list all; confirm each is marked Terminal = Yes in A1]
- **Re-entry blocked:** Trace one attempt to execute an operation from a terminal state. Show the blocking condition.

---

### GATE D (Final)

- [ ] **[C-05]** At least one D1 row with a named blocking condition
- [ ] **[C-07]** D2 addressed — at least one row OR explicit clearance with reason
- [ ] **[C-09]** D3 complete — initial state, all terminal states, re-entry blocked
- [ ] **[C-10]** All four gates (A, B, C, D) are present in this output and each references at least one criterion by ID or name
- [ ] **[C-11]** PHASE B inertia challenge precedes PHASE C trace; at least one D1 row is derived from a PHASE B N-row (confirm by referencing the PHASE B row number in the D1 table)

**Any item unconfirmed → correct the relevant phase.**

---

### FINDINGS

Priority order. Reference phase, gate, and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: PHASE A (A1 vocabulary, A2 operation registry, A3 invariant registry), PHASE B inertia table, PHASE C transition table, PHASE D (D1 invalid transitions, D2 race conditions, D3 boundary coverage), FINDINGS.

---

## V-05 — Boundary-First + Inertia + Gate

**Axis:** Combined — lifecycle emphasis (terminal-first) + inertia framing + gate enforcement
**Hypothesis:** V-04 reaches terminal states by tracing forward. V-05 declares them first, which changes the reasoning order: instead of discovering terminal states at the end of a trace, the writer must define "done" before tracing anything. Terminal-first reasoning makes C-09 the organizing principle of PHASE A (not an afterthought in adversarial review). The inertia challenge in PHASE B asks specifically about the assumptions the process makes about *reaching* terminal states — which surfaces a different category of invalid transition than inertia framing applied generically. A pre-trace gate (GATE A) locks terminal state declaration; a post-trace gate (GATE C) references C-09, C-10, C-11 explicitly. The forward trace (PHASE C) and adversarial review (PHASE D) complete the coverage.

---

You are running a **trace-state** signal for: {{topic}}

Begin at the end. Before tracing how this entity moves through its states, define what "done" looks like. Terminal states anchor the trace; the trace is the story of how the entity gets there. Once you know where you are going, you can ask the harder question: what does the current process assume about how it gets there — and what happens when those assumptions are wrong?

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales / Customer Service / Finance.
Owns: PHASE A (terminal-first declaration), PHASE B (inertia challenge toward terminals).

**[T] Trace Developer**
Owns: PHASE C (forward trace), PHASE D (adversarial review).

---

### PHASE A — TERMINAL-FIRST DECLARATION [D]

#### A1 — Define the Endpoints First

Start with the terminal states. What does "done" mean for this entity in your domain?

| Terminal State | Defining Field Values | What Ended Here | Can It Be Undone? |
|---------------|----------------------|-----------------|--------------------|

**Minimum one terminal state.** If the entity has no terminal state (e.g., it cycles), explain why — this is itself a finding (fully cyclical entities have different invariant risks than terminal-state entities).

#### A2 — Define the Origin

What does this entity look like the moment it is created? What is its initial state?

| Initial State | Defining Field Values | Created By | Created When |
|--------------|----------------------|-----------|-------------|

#### A3 — Full State Vocabulary

Enumerate all states between origin (A2) and terminus (A1).

| State Name | Field Values | Entry Conditions | Terminal? |
|-----------|-------------|-----------------|-----------|

Include all states from A1 and A2. Domain vocabulary only.

#### A4 — Operation Registry

| Operation | Legal Source States | Target State | Triggering Actor |
|-----------|-------------------|-------------|-----------------|

#### A5 — Invariant Registry

| ID | Invariant Name | Checkable Assertion | Authority Source |
|----|---------------|--------------------|--------------------|

Minimum two invariants. At least one must be a terminal-state invariant — a condition that must hold specifically when the entity reaches or exists in a terminal state (e.g., "a Closed Won Opportunity always has owner_id and total_amount > 0").

---

### GATE A

- [ ] **[C-09]** At least one terminal state declared in A1 with field values; OR a reasoned explanation of why none exists
- [ ] **[C-09]** Initial state declared in A2
- [ ] **[C-04]** All state names in A3 use domain vocabulary (no generics)
- [ ] **[C-03]** At least two invariants in A5 with checkable assertions; at least one is a terminal-state invariant

**Unconfirmed → return to PHASE A.**

---

### PHASE B — INERTIA CHALLENGE (TOWARD TERMINALS) [D]

With terminal states declared, challenge what the current process assumes about reaching them.

**Core question:** What does the current manual process assume is required before this entity reaches [terminal state] that the platform does NOT enforce as a state gate?

| # | Terminal State Targeted | Current Process Assumption | Platform Enforced? (Y/N) | Expected Gap if Unenforced |
|---|------------------------|--------------------------|--------------------------|--------------------------|

*Domain examples:*
- *Sales → Closed Won:* "Opportunity can only be won if legal has reviewed the contract" — platform gate or manager approval?
- *CS → Closed:* "Cases require customer satisfaction confirmed before Closed" — enforced state precondition or verbal process?
- *Finance → Voided:* "Only the CFO can void a posted invoice" — role-based state gate or permission convention?

At least one assumption per terminal state. Every N row is a candidate finding in PHASE D.

---

### GATE B

- [ ] At least one assumption per terminal state documented (or a documented reason why no assumptions apply)
- [ ] Every assumption has a Platform Enforced verdict (Y/N)
- [ ] All N rows have an Expected Gap named

**Unconfirmed → return to PHASE B.**

---

### PHASE C — FORWARD TRACE [T]

Trace operations forward from the initial state (A2) toward the terminal states (A1). Cover the primary path and at least one variant path.

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Column rules:**
- **From State / To State:** Vocabulary from A3 only.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank.
- At least one row must have a terminal state as its To State.

---

### GATE C

- [ ] **[C-01]** Every row has a named From State and To State from A3
- [ ] **[C-02]** Every row has at least two preconditions as testable assertions
- [ ] **[C-06]** Every row has at least one postcondition distinct from the state name
- [ ] **[C-03]** Every invariant from A5 checked (HOLDS or VIOLATED) per row
- [ ] **[C-08]** Transition table is complete — all operations are rows; no operation exists only in prose
- [ ] **[C-09]** At least one row reaches a terminal state from A1
- [ ] **[C-10]** GATE A, GATE B, and GATE C are all present in this output and each references at least one criterion by ID
- [ ] **[C-11]** PHASE B inertia challenge was completed before this PHASE C table was filled (inertia precedes tracing)

**Unconfirmed → return to PHASE C or relevant prior phase.**

---

### PHASE D — ADVERSARIAL REVIEW [T]

#### D1 — Invalid Transitions (from Inertia)

For each PHASE B N-row: does the platform actually block the transition toward the terminal state, or allow it?

| Attempted Operation | From State | Blocking Condition | PHASE B Row | Risk if Bypassed |
|--------------------|------------|-------------------|-----------|-----------------|

Add any additional invalid transitions not from PHASE B. Minimum: one row total.

#### D2 — Re-Entry Attempts (Terminal State Violations)

For each terminal state in A1, trace an attempt to execute an operation from it. Show the blocking condition.

| Attempted Operation | Terminal State | Blocking Condition |
|--------------------|---------------|-----------------|

#### D3 — Race Conditions

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If cleared: "No concurrent access — [reason]."

---

### FINDINGS

Priority order. Reference phase, gate, and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: PHASE A (A1 terminal states, A2 initial state, A3 full vocabulary, A4 operation registry, A5 invariant registry), PHASE B inertia table, PHASE C transition table, PHASE D (D1 invalid transitions, D2 re-entry attempts, D3 race conditions), FINDINGS.
