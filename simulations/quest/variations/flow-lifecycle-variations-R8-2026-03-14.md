Now I have the full picture of all 22 criteria and how C-28/C-29/C-30 extend the dependency chain. Let me write the 5 complete variations.

---

## flow-lifecycle — Rubric v8 Variations (R8)

**Three single-axis variations, then two combinations.**

**R8 new criteria targeted:**
- **C-28** — per-block `Required format:` uses literal `B-01`/`B-02`, not generic `B-[ID]`
- **C-29** — explicit scaffold completeness gate: ALL B-NN blocks carry Evidence field
- **C-30** — consolidated dual-location requirements block (named header, both properties, both locations)

**Dependency chain for cascade test:** C-22→C-26→C-27→C-28 (depth-4); C-27→C-29; C-24+C-27→C-30

**Predicted scores (aspirational out of 22):**

| Variation | C-28 | C-29 | C-30 | Aspirational | Total |
|-----------|------|------|------|-------------|-------|
| V-01 | FAIL | PASS | PASS | 21/22 = 9.55 | 99.55 |
| V-02 | PASS | PASS | PASS | 22/22 = 10.00 | 100.00 |
| V-03 | PASS | FAIL | PASS | 21/22 = 9.55 | 99.55 |
| V-04 | FAIL\* | FAIL\* | FAIL\* | 18/22 = 8.18 | 98.18 |
| V-05 | PASS | PASS | PASS | 22/22 = 10.00 | 100.00 |

*V-04 cascade: C-27 FAIL → C-28, C-29, C-30 all FAIL via dependency; same cascade root as R7 V-04 extended one depth.*

---

## V-01 — Single Axis: C-28 Gap (Generic B-[ID] Placeholder in Per-Block Required Format)

**Axis:** Output format — per-block `Required format:` axis retains generic `B-[ID]` bracket placeholder instead of instantiating the owning B-ID.

**Hypothesis:** R7 V-05 carries forward into R8 with C-29 scaffold gate and C-30 consolidated block added, but the per-block `Required format:` axis still uses the generic `B-[ID]` placeholder. C-28 FAIL in isolation; all other criteria (including C-29 and C-30) pass. Score = 21/22 aspirational = 9.55.

---

```markdown
You are a business process simulation expert. Simulate a complete business document lifecycle.

**INPUTS**
- Topic: {{Topic}}
- Signal: {{Signal}}

---

## STEP 1 — ROLE REGISTRY GATE

Before tracing any state, declare the domain role registry for this process type.

**Required format:**
| Role ID | Role Name | Domain Authority |
|---------|-----------|-----------------|
| R-01 | [Domain role, no generic titles] | [Decision scope] |

**Gate checks — all three must clear before proceeding:**
1. No role is labeled generically (e.g., "Approver" or "Manager" without domain qualifier).
2. Role set matches the declared process type:
   - L2O → Sales Representative, Credit Analyst, Contract Manager, Revenue Controller
   - P2P → Procurement Specialist, Receiving Supervisor, AP Clerk, Finance Controller
   - Period Close → GL Accountant, Controller, External Auditor, CFO
   - Case → Support Engineer, Operations Lead, Legal Counsel, Escalation Manager
3. Every subsequent decision point and approval gate references a role by R-ID.

**STRUCTURAL CONSTRAINT: Do not trace any state until all three Role Registry Gate checks
clear.**

---

## STEP 2 — PHASE DECOMPOSITION

List the major phases of the process with scope boundaries.

| Phase # | Phase Name | Entry Event | Exit Event |
|---------|-----------|-------------|------------|
| P-1 | [Phase Name] | [What starts this phase] | [What ends it] |

---

## STEPS 3 THROUGH N — PHASE SIMULATION

Repeat the following block for each phase. Phases are labeled P-1, P-2, etc.

---

### Phase [N] — [Phase Name]

**SECTION A — EXCEPTION TRACES**

*STRUCTURAL CONSTRAINT: SECTION A must appear before SECTION B within every phase block.*

For each exception specific to this phase, produce a constructed-answer block:

**EX-[Phase#]A — [Exception Name]**
- Trigger: [specific condition in this phase that causes the exception]
- Trace: S-[ID] → S-[ID] → ... → TERMINAL
- Handling Role: R-[ID]
- Terminal: [terminal state name]
- Why Problematic: [process impact + frequency or likelihood note]

Minimum across all phases: 3 distinct exception flows. Each must be specific to the
simulated process — not generic boilerplate.

**SECTION B — STATE TABLE**

| State ID | State Name | Entry Condition | Exit(s) | Owner Role |
|----------|-----------|-----------------|---------|------------|
| S-01 | [Name] | [Named entry condition] | → S-02 [condition] | R-01 |

Rules:
- Every state has a named entry condition.
- Every exit references a destination state by S-ID, or is labeled TERMINAL with the
  terminal state name.
- No state is left without an exit.

**DECISION SUPPLEMENT** (one per branching state in SECTION B)

**DS-[S-ID] — [Decision Name]**
- Condition: [labeled branch condition]
- Owner: R-[ID]
- Branch A: [outcome A] → S-[ID] or TERMINAL
- Branch B: [outcome B] → S-[ID] or TERMINAL
- Fallback: [what happens if neither branch resolves within SLA]

---

## STEP [N+1] — PARALLEL PATH MODELING

Model at least one concurrent work stream with explicit fork and join.

**FORK at S-[ID] — [Fork Name]:**
- Path A: S-[ID] → S-[ID] → ... → S-[join-ID]
- Path B: S-[ID] → S-[ID] → ... → S-[join-ID]

**JOIN at S-[join-ID] — [Join Name]:**
- Join type: AND-join | OR-join
- Join condition: [what must be true at both/either branch for the join to proceed]
- If join fails: [what happens when the join condition is not met within SLA]

---

## STEP [N+2] — CROSS-PROCESS HANDOFF CONTRACT

Identify at least one handoff to or from an external process.

**Handoff Contract:**
- From state: S-[ID] ([State Name])
- To process: [External process name]
- Trigger: [event initiating the handoff]
- Expected return: [what comes back and in what form]
- Return SLA: [expected duration]
- Failure mode: [what happens if the external process does not return within SLA]

---

## STEP [N+3] — EDGE CASE ENUMERATION

List 3 or more edge cases distinct from the exception flows in SECTION A.

**EC-01 — [Edge Case Name]**
- Trigger: [specific condition that produces this case]
- Why Problematic: [system or process impact]
- Correct Response: [what the owning role and/or system should do]

(Repeat for EC-02, EC-03, ...)

---

## STEP [N+4] — BOTTLENECK AND GAP ANALYSIS

### BOTTLENECK ANALYSIS

**DUAL-LOCATION REQUIREMENTS:**
Both of the following properties must appear at BOTH the global preamble AND each B-NN
per-block hint:
1. Concrete named domain example (e.g., `S-05: Credit Hold Review -- AT-RISK,
   causal source: B-01`)
2. Labeled axes: `Required format:` and `Fail condition:` as explicitly named sub-fields

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.
A template where any B-NN block lacks the Evidence field entirely fails scaffold
completeness, and per-block dual-location criteria cannot be evaluated for that block.**

**Evidence field format contract (applies to all B-NN Evidence fields below):**
- Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
- Fail condition: An Evidence field containing only "see SLA ANALYSIS", state names
  without AT-RISK row-level specificity, or a general reference does not satisfy. Each
  entry must name a specific S-ID.
- Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`

---

Identify at least 2 bottlenecks (states or transitions where delays accumulate):

**B-01 — [Bottleneck Name]**
- Cause: [why delays or errors accumulate at this point]
- Impact: [downstream effects on SLA, dependent states, or cross-process handoffs]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-01 in this format.

**B-02 — [Bottleneck Name]**
- Cause: [why delays or errors accumulate at this point]
- Impact: [downstream effects]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-02 in this format.

### GAP ANALYSIS (minimum 1 gap)

**MISSING: [Gap Name]**
- Where: between S-[ID] ([State Name]) and S-[ID] ([State Name])
- Rationale: [why this step belongs in real-world practice for this process type]

---

## STEP [N+5] — SLA AND TIMING ANALYSIS

*ANTI-EMBEDDING INSTRUCTION: Do not embed CHAIN STATUS in this section. CHAIN STATUS
must appear in its own dedicated section in STEP N+6.*

Annotate at least 3 states or transitions with SLA information:

| State/Transition | SLA Target | Typical Actual | Status | Bottleneck Cross-Ref |
|-----------------|-----------|----------------|--------|---------------------|
| S-05: [Name] | 24h | 48h | AT-RISK | B-01 |
| S-03: [Name] | 4h | 3h | OK | — |

Instructions:
- Every AT-RISK row must include a Bottleneck Cross-Ref naming the B-ID from STEP N+4.
- Every OK row sets Cross-Ref to —.

---

## STEP [N+6] — CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS in the SLA ANALYSIS section above.
Declare CHAIN STATUS as the first element of this dedicated section.*

**CHAIN STATUS: [CLOSED / OPEN]**

Forward chain (SLA → Bottleneck): Each AT-RISK row in STEP N+5 cites a B-ID.
Backward chain (Bottleneck → SLA): Each B-NN Evidence field in STEP N+4 lists only
SLA rows that cite that B-ID.

- CLOSED: all AT-RISK rows cite a B-ID; all B-NN Evidence lists match. State the count
  verified for each direction.
- OPEN: list each unresolved entry — direction (Forward/Backward), S-ID or B-ID, gap.

---

## TERMINAL STATE DECLARATION

| Terminal ID | Name | Type | Reached Via |
|------------|------|------|-------------|
| T-01 | [Name] | SUCCESS | S-[ID] |
| T-02 | [Name] | FAILURE | S-[ID] or exception trace |

Requirements:
- At least one SUCCESS terminal and at least one FAILURE or CANCEL terminal.
- Every branch in the state tables reaches a declared terminal. No branch ends mid-flow
  without a terminal label or explicit "continues via S-[ID]" pointer.

---

## OUTPUT FILE

Write the completed simulation to:

    simulations/flow/lifecycle/{{Topic}}-lifecycle-{{date}}.md
```

---

## V-02 — Single Axis: C-28 Fix (Instantiated B-ID in Per-Block Required Format)

**Axis:** Output format — per-block `Required format:` axis uses the specific B-ID for that block (`B-01` in B-01's hint, `B-02` in B-02's hint) instead of the generic `B-[ID]` placeholder.

**Hypothesis:** Minimal R8 increment from V-01. The only change is instantiating the B-ID in each per-block `Required format:` line. C-28 PASS. Score jumps to 22/22 = 10.00. This is the minimum change to reach 100.

---

```markdown
You are a business process simulation expert. Simulate a complete business document lifecycle.

**INPUTS**
- Topic: {{Topic}}
- Signal: {{Signal}}

---

## STEP 1 — ROLE REGISTRY GATE

Before tracing any state, declare the domain role registry for this process type.

**Required format:**
| Role ID | Role Name | Domain Authority |
|---------|-----------|-----------------|
| R-01 | [Domain role, no generic titles] | [Decision scope] |

**Gate checks — all three must clear before proceeding:**
1. No role is labeled generically (e.g., "Approver" or "Manager" without domain qualifier).
2. Role set matches the declared process type:
   - L2O → Sales Representative, Credit Analyst, Contract Manager, Revenue Controller
   - P2P → Procurement Specialist, Receiving Supervisor, AP Clerk, Finance Controller
   - Period Close → GL Accountant, Controller, External Auditor, CFO
   - Case → Support Engineer, Operations Lead, Legal Counsel, Escalation Manager
3. Every subsequent decision point and approval gate references a role by R-ID.

**STRUCTURAL CONSTRAINT: Do not trace any state until all three Role Registry Gate checks
clear.**

---

## STEP 2 — PHASE DECOMPOSITION

| Phase # | Phase Name | Entry Event | Exit Event |
|---------|-----------|-------------|------------|
| P-1 | [Phase Name] | [What starts this phase] | [What ends it] |

---

## STEPS 3 THROUGH N — PHASE SIMULATION

Repeat the following block for each phase.

---

### Phase [N] — [Phase Name]

**SECTION A — EXCEPTION TRACES**

*STRUCTURAL CONSTRAINT: SECTION A must appear before SECTION B within every phase block.*

**EX-[Phase#]A — [Exception Name]**
- Trigger: [specific condition in this phase]
- Trace: S-[ID] → S-[ID] → ... → TERMINAL
- Handling Role: R-[ID]
- Terminal: [terminal state name]
- Why Problematic: [process impact + frequency note]

Minimum across all phases: 3 distinct exception flows, each process-specific.

**SECTION B — STATE TABLE**

| State ID | State Name | Entry Condition | Exit(s) | Owner Role |
|----------|-----------|-----------------|---------|------------|
| S-01 | [Name] | [Named entry condition] | → S-02 [condition] | R-01 |

Rules: every state has a named entry condition; every exit names a destination by S-ID or
TERMINAL; no dangling states.

**DECISION SUPPLEMENT** (one per branching state)

**DS-[S-ID] — [Decision Name]**
- Condition: [labeled branch condition]
- Owner: R-[ID]
- Branch A: [outcome A] → S-[ID] or TERMINAL
- Branch B: [outcome B] → S-[ID] or TERMINAL
- Fallback: [what happens if neither branch resolves within SLA]

---

## STEP [N+1] — PARALLEL PATH MODELING

**FORK at S-[ID] — [Fork Name]:**
- Path A: S-[ID] → ... → S-[join-ID]
- Path B: S-[ID] → ... → S-[join-ID]

**JOIN at S-[join-ID] — [Join Name]:**
- Join type: AND-join | OR-join
- Join condition: [what must be true for the join to proceed]
- If join fails: [what happens when join condition is not met within SLA]

---

## STEP [N+2] — CROSS-PROCESS HANDOFF CONTRACT

**Handoff Contract:**
- From state: S-[ID] ([State Name])
- To process: [External process name]
- Trigger: [event initiating the handoff]
- Expected return: [what comes back and in what form]
- Return SLA: [expected duration]
- Failure mode: [what happens if the external process does not return within SLA]

---

## STEP [N+3] — EDGE CASE ENUMERATION

**EC-01 — [Edge Case Name]**
- Trigger: [specific condition]
- Why Problematic: [system or process impact]
- Correct Response: [what should happen]

(Repeat for EC-02, EC-03, ...)

---

## STEP [N+4] — BOTTLENECK AND GAP ANALYSIS

### BOTTLENECK ANALYSIS

**DUAL-LOCATION REQUIREMENTS:**
Both of the following properties must appear at BOTH the global preamble AND each B-NN
per-block hint:
1. Concrete named domain example (e.g., `S-05: Credit Hold Review -- AT-RISK,
   causal source: B-01`)
2. Labeled axes: `Required format:` and `Fail condition:` as explicitly named sub-fields

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.
A template where any B-NN block lacks the Evidence field entirely fails scaffold
completeness, and per-block dual-location criteria cannot be evaluated for that block.**

**Evidence field format contract (applies to all B-NN Evidence fields below):**
- Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
- Fail condition: An Evidence field containing only "see SLA ANALYSIS", state names
  without AT-RISK row-level specificity, or a general reference does not satisfy. Each
  entry must name a specific S-ID.
- Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`

---

Identify at least 2 bottlenecks:

**B-01 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-01 in this format.

**B-02 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-02 in this format.

### GAP ANALYSIS (minimum 1 gap)

**MISSING: [Gap Name]**
- Where: between S-[ID] ([State Name]) and S-[ID] ([State Name])
- Rationale: [why this step belongs in real-world practice]

---

## STEP [N+5] — SLA AND TIMING ANALYSIS

*ANTI-EMBEDDING INSTRUCTION: Do not embed CHAIN STATUS in this section. CHAIN STATUS
must appear in its own dedicated section in STEP N+6.*

| State/Transition | SLA Target | Typical Actual | Status | Bottleneck Cross-Ref |
|-----------------|-----------|----------------|--------|---------------------|
| S-05: [Name] | 24h | 48h | AT-RISK | B-01 |
| S-03: [Name] | 4h | 3h | OK | — |

Every AT-RISK row must cite a B-ID. Every OK row sets Cross-Ref to —.

---

## STEP [N+6] — CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS in the SLA ANALYSIS section above.
Declare CHAIN STATUS as the first element of this dedicated section.*

**CHAIN STATUS: [CLOSED / OPEN]**

Forward chain (SLA → Bottleneck): each AT-RISK row cites a B-ID.
Backward chain (Bottleneck → SLA): each B-NN Evidence field lists only SLA rows that
cite that B-ID.

- CLOSED: all AT-RISK rows cite a B-ID; all B-NN Evidence lists match. State counts.
- OPEN: list each unresolved entry — direction, S-ID or B-ID, gap.

---

## TERMINAL STATE DECLARATION

| Terminal ID | Name | Type | Reached Via |
|------------|------|------|-------------|
| T-01 | [Name] | SUCCESS | S-[ID] |
| T-02 | [Name] | FAILURE | S-[ID] or exception |

At least one SUCCESS and one FAILURE/CANCEL terminal. Every branch reaches a declared
terminal.

---

## OUTPUT FILE

    simulations/flow/lifecycle/{{Topic}}-lifecycle-{{date}}.md
```

---

## V-03 — Single Axis: C-29 Gap (No Scaffold Completeness Prerequisite Declaration)

**Axis:** Lifecycle emphasis — the scaffold completeness gate is absent; per-block blocks carry all dual-location requirements but no explicit pre-declaration that ALL B-NN blocks must carry the Evidence field.

**Hypothesis:** C-28 PASS (instantiated B-IDs), C-30 PASS (consolidated block present), C-29 FAIL only (no explicit scaffold completeness instruction before the B-NN blocks). Score = 21/22 = 9.55. Demonstrates that C-29 is an independent structural gate — the dual-location content and instantiated IDs are not sufficient to imply scaffold completeness was required.

---

```markdown
You are a business process simulation expert. Simulate a complete business document lifecycle.

**INPUTS**
- Topic: {{Topic}}
- Signal: {{Signal}}

---

## STEP 1 — ROLE REGISTRY GATE

Before tracing any state, declare the domain role registry for this process type.

**Required format:**
| Role ID | Role Name | Domain Authority |
|---------|-----------|-----------------|
| R-01 | [Domain role, no generic titles] | [Decision scope] |

**Gate checks — all three must clear before proceeding:**
1. No role is labeled generically (e.g., "Approver" or "Manager" without domain qualifier).
2. Role set matches the declared process type:
   - L2O → Sales Representative, Credit Analyst, Contract Manager, Revenue Controller
   - P2P → Procurement Specialist, Receiving Supervisor, AP Clerk, Finance Controller
   - Period Close → GL Accountant, Controller, External Auditor, CFO
   - Case → Support Engineer, Operations Lead, Legal Counsel, Escalation Manager
3. Every subsequent decision point and approval gate references a role by R-ID.

**STRUCTURAL CONSTRAINT: Do not trace any state until all three Role Registry Gate checks
clear.**

---

## STEP 2 — PHASE DECOMPOSITION

| Phase # | Phase Name | Entry Event | Exit Event |
|---------|-----------|-------------|------------|
| P-1 | [Phase Name] | [What starts this phase] | [What ends it] |

---

## STEPS 3 THROUGH N — PHASE SIMULATION

Repeat the following block for each phase.

---

### Phase [N] — [Phase Name]

**SECTION A — EXCEPTION TRACES**

*STRUCTURAL CONSTRAINT: SECTION A must appear before SECTION B within every phase block.*

**EX-[Phase#]A — [Exception Name]**
- Trigger: [specific condition in this phase]
- Trace: S-[ID] → S-[ID] → ... → TERMINAL
- Handling Role: R-[ID]
- Terminal: [terminal state name]
- Why Problematic: [process impact + frequency note]

Minimum across all phases: 3 distinct exception flows, each process-specific.

**SECTION B — STATE TABLE**

| State ID | State Name | Entry Condition | Exit(s) | Owner Role |
|----------|-----------|-----------------|---------|------------|
| S-01 | [Name] | [Named entry condition] | → S-02 [condition] | R-01 |

Every state has a named entry condition; every exit names a destination by S-ID or
TERMINAL; no dangling states.

**DECISION SUPPLEMENT** (one per branching state)

**DS-[S-ID] — [Decision Name]**
- Condition: [labeled branch condition]
- Owner: R-[ID]
- Branch A: [outcome A] → S-[ID] or TERMINAL
- Branch B: [outcome B] → S-[ID] or TERMINAL
- Fallback: [what happens if neither branch resolves within SLA]

---

## STEP [N+1] — PARALLEL PATH MODELING

**FORK at S-[ID] — [Fork Name]:**
- Path A: S-[ID] → ... → S-[join-ID]
- Path B: S-[ID] → ... → S-[join-ID]

**JOIN at S-[join-ID] — [Join Name]:**
- Join type: AND-join | OR-join
- Join condition: [what must be true for the join to proceed]
- If join fails: [what happens when join condition is not met within SLA]

---

## STEP [N+2] — CROSS-PROCESS HANDOFF CONTRACT

**Handoff Contract:**
- From state: S-[ID] ([State Name])
- To process: [External process name]
- Trigger: [event initiating the handoff]
- Expected return: [what comes back]
- Return SLA: [expected duration]
- Failure mode: [what happens if the external process does not return within SLA]

---

## STEP [N+3] — EDGE CASE ENUMERATION

**EC-01 — [Edge Case Name]**
- Trigger: [specific condition]
- Why Problematic: [system or process impact]
- Correct Response: [what should happen]

(Repeat for EC-02, EC-03, ...)

---

## STEP [N+4] — BOTTLENECK AND GAP ANALYSIS

### BOTTLENECK ANALYSIS

**DUAL-LOCATION REQUIREMENTS:**
Both of the following properties must appear at BOTH the global preamble AND each B-NN
per-block hint:
1. Concrete named domain example (e.g., `S-05: Credit Hold Review -- AT-RISK,
   causal source: B-01`)
2. Labeled axes: `Required format:` and `Fail condition:` as explicitly named sub-fields

**Evidence field format contract (applies to all B-NN Evidence fields below):**
- Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
- Fail condition: An Evidence field containing only "see SLA ANALYSIS", state names
  without AT-RISK row-level specificity, or a general reference does not satisfy. Each
  entry must name a specific S-ID.
- Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`

---

Identify at least 2 bottlenecks:

**B-01 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-01 in this format.

**B-02 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-02 in this format.

### GAP ANALYSIS (minimum 1 gap)

**MISSING: [Gap Name]**
- Where: between S-[ID] ([State Name]) and S-[ID] ([State Name])
- Rationale: [why this step belongs in real-world practice]

---

## STEP [N+5] — SLA AND TIMING ANALYSIS

*ANTI-EMBEDDING INSTRUCTION: Do not embed CHAIN STATUS in this section. CHAIN STATUS
must appear in its own dedicated section in STEP N+6.*

| State/Transition | SLA Target | Typical Actual | Status | Bottleneck Cross-Ref |
|-----------------|-----------|----------------|--------|---------------------|
| S-05: [Name] | 24h | 48h | AT-RISK | B-01 |
| S-03: [Name] | 4h | 3h | OK | — |

Every AT-RISK row must cite a B-ID. Every OK row sets Cross-Ref to —.

---

## STEP [N+6] — CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS in the SLA ANALYSIS section above.
Declare CHAIN STATUS as the first element of this dedicated section.*

**CHAIN STATUS: [CLOSED / OPEN]**

Forward chain (SLA → Bottleneck): each AT-RISK row cites a B-ID.
Backward chain (Bottleneck → SLA): each B-NN Evidence field lists only SLA rows that
cite that B-ID.

- CLOSED: state counts for both directions.
- OPEN: list each unresolved entry — direction, S-ID or B-ID, gap.

---

## TERMINAL STATE DECLARATION

| Terminal ID | Name | Type | Reached Via |
|------------|------|------|-------------|
| T-01 | [Name] | SUCCESS | S-[ID] |
| T-02 | [Name] | FAILURE | S-[ID] or exception |

At least one SUCCESS and one FAILURE/CANCEL terminal. Every branch reaches a declared
terminal.

---

## OUTPUT FILE

    simulations/flow/lifecycle/{{Topic}}-lifecycle-{{date}}.md
```

**C-29 evaluation note:** The DUAL-LOCATION REQUIREMENTS block is present (C-30 PASS); instantiated B-IDs present (C-28 PASS); but no explicit instruction states that ALL B-NN blocks must carry the Evidence field before per-block criteria apply. C-29 FAIL — scaffold completeness is only implied by per-block inspection, not declared as a named prerequisite gate.

---

## V-04 — Combination: C-27 Degradation → C-28 / C-29 / C-30 Cascade FAIL

**Axes combined:** Output format (per-block axes degraded to back-reference) + dependency cascade (C-27 FAIL triggers 3-criterion failure)

**Hypothesis:** Removing per-block labeled axis restatement (C-27 FAIL) causes the full R8 cascade: C-28 FAIL (C-28→C-27), C-29 FAIL (C-29→C-27), C-30 FAIL (C-30→C-27). This extends the R7 cascade by one depth level — C-22 preamble-only now cascades to 5 failures (C-22, C-24, C-26, C-27, C-28, C-29, C-30 if C-22 root fails; here we degrade at C-27 directly). Score = 18/22 = 8.18.

---

```markdown
You are a business process simulation expert. Simulate a complete business document lifecycle.

**INPUTS**
- Topic: {{Topic}}
- Signal: {{Signal}}

---

## STEP 1 — ROLE REGISTRY GATE

Before tracing any state, declare the domain role registry for this process type.

**Required format:**
| Role ID | Role Name | Domain Authority |
|---------|-----------|-----------------|
| R-01 | [Domain role, no generic titles] | [Decision scope] |

**Gate checks — all three must clear before proceeding:**
1. No role is labeled generically (e.g., "Approver" or "Manager" without domain qualifier).
2. Role set matches the declared process type:
   - L2O → Sales Representative, Credit Analyst, Contract Manager, Revenue Controller
   - P2P → Procurement Specialist, Receiving Supervisor, AP Clerk, Finance Controller
   - Period Close → GL Accountant, Controller, External Auditor, CFO
   - Case → Support Engineer, Operations Lead, Legal Counsel, Escalation Manager
3. Every subsequent decision point and approval gate references a role by R-ID.

**STRUCTURAL CONSTRAINT: Do not trace any state until all three Role Registry Gate checks
clear.**

---

## STEP 2 — PHASE DECOMPOSITION

| Phase # | Phase Name | Entry Event | Exit Event |
|---------|-----------|-------------|------------|
| P-1 | [Phase Name] | [What starts this phase] | [What ends it] |

---

## STEPS 3 THROUGH N — PHASE SIMULATION

Repeat for each phase.

---

### Phase [N] — [Phase Name]

**SECTION A — EXCEPTION TRACES**

*STRUCTURAL CONSTRAINT: SECTION A must appear before SECTION B within every phase block.*

**EX-[Phase#]A — [Exception Name]**
- Trigger: [specific condition in this phase]
- Trace: S-[ID] → S-[ID] → ... → TERMINAL
- Handling Role: R-[ID]
- Terminal: [terminal state name]
- Why Problematic: [process impact + frequency note]

Minimum: 3 distinct exception flows, process-specific.

**SECTION B — STATE TABLE**

| State ID | State Name | Entry Condition | Exit(s) | Owner Role |
|----------|-----------|-----------------|---------|------------|
| S-01 | [Name] | [Named entry condition] | → S-02 [condition] | R-01 |

**DECISION SUPPLEMENT** (one per branching state)

**DS-[S-ID] — [Decision Name]**
- Condition: [labeled branch condition]
- Owner: R-[ID]
- Branch A: [outcome A] → S-[ID] or TERMINAL
- Branch B: [outcome B] → S-[ID] or TERMINAL
- Fallback: [what happens if neither branch resolves within SLA]

---

## STEP [N+1] — PARALLEL PATH MODELING

**FORK at S-[ID]:**
- Path A: S-[ID] → ... → S-[join-ID]
- Path B: S-[ID] → ... → S-[join-ID]

**JOIN at S-[join-ID]:**
- Join type: AND-join | OR-join
- Join condition: [what must be true]
- If join fails: [consequence]

---

## STEP [N+2] — CROSS-PROCESS HANDOFF CONTRACT

**Handoff Contract:**
- From state: S-[ID] ([State Name])
- To process: [External process]
- Trigger: [event]
- Expected return: [artifact]
- Return SLA: [duration]
- Failure mode: [consequence]

---

## STEP [N+3] — EDGE CASE ENUMERATION

**EC-01 — [Edge Case Name]**
- Trigger: [specific condition]
- Why Problematic: [impact]
- Correct Response: [action]

(Repeat for EC-02, EC-03, ...)

---

## STEP [N+4] — BOTTLENECK AND GAP ANALYSIS

### BOTTLENECK ANALYSIS

**Evidence field format contract (applies to all B-NN Evidence fields below):**
- Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
- Fail condition: An Evidence field containing only "see SLA ANALYSIS" or state names
  without AT-RISK row-level specificity does not satisfy. Each entry must name a specific
  S-ID.
- Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`

---

Identify at least 2 bottlenecks:

**B-01 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Using the format above, list each AT-RISK SLA row from STEP N+5 that cites B-01.

**B-02 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Using the format above, list each AT-RISK SLA row from STEP N+5 that cites B-02.

### GAP ANALYSIS (minimum 1 gap)

**MISSING: [Gap Name]**
- Where: between S-[ID] and S-[ID]
- Rationale: [why this step belongs in real-world practice]

---

## STEP [N+5] — SLA AND TIMING ANALYSIS

*ANTI-EMBEDDING INSTRUCTION: Do not embed CHAIN STATUS in this section. CHAIN STATUS
must appear in its own dedicated section in STEP N+6.*

| State/Transition | SLA Target | Typical Actual | Status | Bottleneck Cross-Ref |
|-----------------|-----------|----------------|--------|---------------------|
| S-05: [Name] | 24h | 48h | AT-RISK | B-01 |
| S-03: [Name] | 4h | 3h | OK | — |

---

## STEP [N+6] — CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS in the SLA ANALYSIS section above.
Declare CHAIN STATUS as the first element of this dedicated section.*

**CHAIN STATUS: [CLOSED / OPEN]**

Forward chain (SLA → Bottleneck): each AT-RISK row cites a B-ID.
Backward chain (Bottleneck → SLA): each B-NN Evidence field lists only SLA rows that
cite that B-ID.

---

## TERMINAL STATE DECLARATION

| Terminal ID | Name | Type | Reached Via |
|------------|------|------|-------------|
| T-01 | [Name] | SUCCESS | S-[ID] |
| T-02 | [Name] | FAILURE | S-[ID] |

---

## OUTPUT FILE

    simulations/flow/lifecycle/{{Topic}}-lifecycle-{{date}}.md
```

**V-04 cascade analysis:**
- C-27 FAIL: per-block hints say "using the format above" — `Required format:` / `Fail condition:` labeled axes not restated at per-block location.
- C-28 FAIL: C-28→C-27; C-27 failure makes C-28 unevaluable — per-block `Required format:` not present at per-block scope at all.
- C-29 FAIL: C-29→C-27; no per-block Evidence field structure to attach scaffold completeness to; no explicit ALL-B-NN gate present either.
- C-30 FAIL: C-30→C-27; C-27 failing means dual-location labeled axes are absent; C-30 cannot declare both locality properties satisfied.
- All other criteria: PASS.

**Cascade depth from C-27:** 4 FAIL criteria total (C-27, C-28, C-29, C-30). R7 V-04 (degraded at C-26) cascaded to 4 failures; R8 V-04 (degraded at C-27, one level deeper) also cascades to 4 failures, but the cascade is now reachable from a shallower degradation point. The full C-22-root cascade in R8 reaches depth-7 (C-22→C-26→C-27→C-28, C-22→C-24→C-30, C-27→C-29→C-30) — 7 distinct criteria from a single preamble-bracket-only failure.

---

## V-05 — Combination: Full R8 Synthesis (C-28 + C-29 + C-30 All Pass)

**Axes combined:** Instantiated B-IDs (C-28) + explicit scaffold completeness gate (C-29) + consolidated dual-location requirements block (C-30).

**Hypothesis:** All 22 aspirational criteria pass. C-30 is the net-new structural addition over V-02: a named DUAL-LOCATION REQUIREMENTS block with a unifying header makes the complete locality contract discoverable at one location without cross-referencing individual B-NN hints. C-29 scaffold gate is explicit and precedes all B-NN blocks. C-28 B-IDs are instantiated per-block. Score = 22/22 = 10.00.

---

```markdown
You are a business process simulation expert. Simulate a complete business document lifecycle.

**INPUTS**
- Topic: {{Topic}}
- Signal: {{Signal}}

---

## STEP 1 — ROLE REGISTRY GATE

Before tracing any state, declare the domain role registry for this process type.

**Required format:**
| Role ID | Role Name | Domain Authority |
|---------|-----------|-----------------|
| R-01 | [Domain role, no generic titles] | [Decision scope] |

**Gate checks — all three must clear before proceeding:**
1. No role is labeled generically (e.g., "Approver" or "Manager" without domain qualifier).
2. Role set matches the declared process type:
   - L2O → Sales Representative, Credit Analyst, Contract Manager, Revenue Controller
   - P2P → Procurement Specialist, Receiving Supervisor, AP Clerk, Finance Controller
   - Period Close → GL Accountant, Controller, External Auditor, CFO
   - Case → Support Engineer, Operations Lead, Legal Counsel, Escalation Manager
3. Every subsequent decision point and approval gate references a role by R-ID.

**STRUCTURAL CONSTRAINT: Do not trace any state until all three Role Registry Gate checks
clear.**

---

## STEP 2 — PHASE DECOMPOSITION

| Phase # | Phase Name | Entry Event | Exit Event |
|---------|-----------|-------------|------------|
| P-1 | [Phase Name] | [What starts this phase] | [What ends it] |

---

## STEPS 3 THROUGH N — PHASE SIMULATION

Repeat for each phase.

---

### Phase [N] — [Phase Name]

**SECTION A — EXCEPTION TRACES**

*STRUCTURAL CONSTRAINT: SECTION A must appear before SECTION B within every phase block.*

**EX-[Phase#]A — [Exception Name]**
- Trigger: [specific condition in this phase]
- Trace: S-[ID] → S-[ID] → ... → TERMINAL
- Handling Role: R-[ID]
- Terminal: [terminal state name]
- Why Problematic: [process impact + frequency note]

Minimum: 3 distinct exception flows, process-specific.

**SECTION B — STATE TABLE**

| State ID | State Name | Entry Condition | Exit(s) | Owner Role |
|----------|-----------|-----------------|---------|------------|
| S-01 | [Name] | [Named entry condition] | → S-02 [condition] | R-01 |

Every state has a named entry condition; every exit names a destination by S-ID or
TERMINAL; no dangling states.

**DECISION SUPPLEMENT** (one per branching state)

**DS-[S-ID] — [Decision Name]**
- Condition: [labeled branch condition]
- Owner: R-[ID]
- Branch A: [outcome A] → S-[ID] or TERMINAL
- Branch B: [outcome B] → S-[ID] or TERMINAL
- Fallback: [what happens if neither branch resolves within SLA]

---

## STEP [N+1] — PARALLEL PATH MODELING

**FORK at S-[ID] — [Fork Name]:**
- Path A: S-[ID] → ... → S-[join-ID]
- Path B: S-[ID] → ... → S-[join-ID]

**JOIN at S-[join-ID] — [Join Name]:**
- Join type: AND-join | OR-join
- Join condition: [what must be true for the join to proceed]
- If join fails: [consequence]

---

## STEP [N+2] — CROSS-PROCESS HANDOFF CONTRACT

**Handoff Contract:**
- From state: S-[ID] ([State Name])
- To process: [External process name]
- Trigger: [event initiating handoff]
- Expected return: [artifact and form]
- Return SLA: [duration]
- Failure mode: [consequence if not returned within SLA]

---

## STEP [N+3] — EDGE CASE ENUMERATION

**EC-01 — [Edge Case Name]**
- Trigger: [specific condition]
- Why Problematic: [system or process impact]
- Correct Response: [action]

(Repeat for EC-02, EC-03, ...)

---

## STEP [N+4] — BOTTLENECK AND GAP ANALYSIS

### BOTTLENECK ANALYSIS

**LOCALITY CONTRACT:**
The following dual-location requirements apply to all Evidence fields in this section.
Both properties must appear at BOTH the global preamble (below) AND each B-NN per-block
hint:
1. Concrete named domain example: a filled-in S-ID example such as
   `S-05: Credit Hold Review -- AT-RISK, causal source: B-01` must appear at both
   locations — not a bracket template.
2. Labeled axes: `Required format:` and `Fail condition:` as explicitly named sub-fields
   must appear at both locations — not a back-reference such as "using the format above."

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.
A template where any B-NN block lacks the Evidence field entirely fails scaffold
completeness, and per-block dual-location criteria cannot be evaluated for that block.**

**Evidence field format contract (applies to all B-NN Evidence fields below):**
- Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
- Fail condition: An Evidence field containing only "see SLA ANALYSIS", state names
  without AT-RISK row-level specificity, or a general reference does not satisfy. Each
  entry must name a specific S-ID.
- Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`

---

Identify at least 2 bottlenecks:

**B-01 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-01 in this format.

**B-02 — [Bottleneck Name]**
- Cause: [why delays accumulate here]
- Impact: [downstream effects]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: An Evidence field containing only "see SLA ANALYSIS" or general
    references does not satisfy. Each entry must name a specific S-ID.
  - Example: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01`
  - List each AT-RISK SLA row from STEP N+5 that cites B-02 in this format.

### GAP ANALYSIS (minimum 1 gap)

**MISSING: [Gap Name]**
- Where: between S-[ID] ([State Name]) and S-[ID] ([State Name])
- Rationale: [why this step belongs in real-world practice]

---

## STEP [N+5] — SLA AND TIMING ANALYSIS

*ANTI-EMBEDDING INSTRUCTION: Do not embed CHAIN STATUS in this section. CHAIN STATUS
must appear in its own dedicated section in STEP N+6.*

Annotate at least 3 states or transitions:

| State/Transition | SLA Target | Typical Actual | Status | Bottleneck Cross-Ref |
|-----------------|-----------|----------------|--------|---------------------|
| S-05: [Name] | 24h | 48h | AT-RISK | B-01 |
| S-03: [Name] | 4h | 3h | OK | — |

Every AT-RISK row must cite a B-ID. Every OK row sets Cross-Ref to —.

---

## STEP [N+6] — CHAIN STATUS

*STRUCTURAL CONSTRAINT: Do not embed CHAIN STATUS in the SLA ANALYSIS section above.
Declare CHAIN STATUS as the first element of this dedicated section.*

**CHAIN STATUS: [CLOSED / OPEN]**

Forward chain (SLA → Bottleneck): each AT-RISK row in STEP N+5 cites a B-ID.
Backward chain (Bottleneck → SLA): each B-NN Evidence field in STEP N+4 lists only
SLA rows that cite that B-ID.

- CLOSED: state counts verified for both directions.
- OPEN: list each unresolved entry — direction, S-ID or B-ID, gap.

---

## TERMINAL STATE DECLARATION

| Terminal ID | Name | Type | Reached Via |
|------------|------|------|-------------|
| T-01 | [Name] | SUCCESS | S-[ID] |
| T-02 | [Name] | FAILURE | S-[ID] or exception |

At least one SUCCESS and one FAILURE/CANCEL terminal. Every branch reaches a declared
terminal.

---

## OUTPUT FILE

    simulations/flow/lifecycle/{{Topic}}-lifecycle-{{date}}.md
```

---

## Summary

| Variation | Axis | C-28 | C-29 | C-30 | Aspirational | Total |
|-----------|------|------|------|------|-------------|-------|
| V-01 | C-28 gap: generic `B-[ID]` in per-block Required format | FAIL | PASS | PASS | 21/22 = 9.55 | **99.55** |
| V-02 | C-28 fix: instantiated `B-01`/`B-02` in per-block Required format | PASS | PASS | PASS | 22/22 = 10.00 | **100.00** |
| V-03 | C-29 gap: no scaffold completeness prerequisite declaration | PASS | FAIL | PASS | 21/22 = 9.55 | **99.55** |
| V-04 | C-27 cascade: per-block axes degraded to back-reference → C-28/C-29/C-30 cascade | FAIL\* | FAIL\* | FAIL\* | 18/22 = 8.18 | **98.18** |
| V-05 | Full R8 synthesis: C-28 + C-29 + LOCALITY CONTRACT block (C-30) | PASS | PASS | PASS | 22/22 = 10.00 | **100.00** |

**Predicted rank:** V-02 = V-05 (100) > V-01 = V-03 (99.55) > V-04 (98.18)

---

**Key structural difference between V-02 and V-05:**

V-02 achieves 100 without C-30. V-05 adds the LOCALITY CONTRACT named block — a consolidated declaration that makes the complete dual-location contract discoverable at one location. Both score identically; the test is whether C-30 is structurally recognizable as an independent criterion, not whether it affects the score. If the rubric later adds a C-31 requiring per-block LOCALITY CONTRACT restatement, V-05 survives; V-02 does not.

**New R8 cascade note:**

V-04 degrades at C-27 (one level shallower than degrading at C-22). Four criteria fail from C-27 degradation: C-27, C-28, C-29, C-30. This is structurally identical in cascade breadth to R7 V-04's 4-failure cascade (C-22, C-24, C-26, C-27), but is now reachable from a more narrowly degraded prompt — only the per-block labeled axes are removed. The full C-22-root cascade in R8 reaches 7 criteria: C-22→{C-24, C-26}→{C-27}→{C-28, C-29}→{C-30 via C-24+C-27}. The chain is now wide as well as deep.
