Good. I have full context on the rubric v5 (C-01 through C-22, three new: C-20 closure counters, C-21 prohibition contracts, C-22 all-slots mandate) and the evolution trajectory. Now generating the R8 variations.

---

# flow-trigger — Round 8 Variations

**Generated:** 2026-03-16
**Rubric:** v5 (C-01 through C-22, N_essential=5, N_recommended=3, N_aspirational=14)
**New aspirational criteria targeted this round:** C-20 (zero-tolerance closure counters), C-21 (named role prohibition contracts), C-22 (uniform all-slots-required mandate)

---

## Variation Axis Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence — Scope Arbiter leads; all structural artifacts declared before Enumeration Expert fires | Dedicating a first role to scope gate + exclusion log + prohibition contracts produces C-14/C-19/C-21 as named artifacts the Closure Auditor can count against, satisfying C-20 through structural sequencing rather than inline reminders |
| V-02 | Output format — Table-centric with global ALL-SLOTS-REQUIRED mandate declared before first entry | Declaring C-22's invariant once as a structural rule then using slot-per-column tables makes empty slots visually detectable, producing C-15/C-16/C-17 compliance as a formatting consequence rather than a per-entry discipline problem |
| V-03 | Lifecycle emphasis — Each phase carries a named PROHIBITION block as a required structural section | Making prohibition contracts a first-class required section per phase (C-21) closes scope by role-action definition, catching late-phase scope expansion that C-14's event gate alone cannot prevent |
| V-04 | Role sequence + Phrasing register — Inverted order (anomaly frame first) + formal SHALL/MUST throughout | Opening with explicit anomaly questions as OPEN investigations before enumeration forces denominator-first thinking (C-11) and makes each role's prohibition natural because the investigation contract already bounds what each role may add |
| V-05 | Output format + Lifecycle + Inertia framing — Status-quo contrast opens the prompt; CLOSURE CHECK block closes it | Naming the inertia baseline (ad-hoc audit: no gate, no denominator, no closure) makes the structural gain from each artifact concrete, increasing the probability the closure counters (C-20) are populated with substance rather than nominal compliance tokens |

---

## V-01

**Variation axis:** Role sequence — Scope Arbiter leads all phases
**Hypothesis:** When a dedicated Scope Arbiter role runs first and produces three locked structural artifacts (SCOPE GATE, EXCLUSION LOG, PROHIBITION CONTRACTS) before the Enumeration Expert may begin, each artifact exists as a named, citable object that the Closure Auditor can check by name. Closure counters (C-20) become auditable because the artifacts they count against are guaranteed to exist; prohibition contracts (C-21) emerge naturally because scope-by-role-action is the Arbiter's explicit mandate; the all-slots mandate (C-22) can be declared as a single Arbiter-issued structural rule that governs all subsequent roles.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to `Inactive` (1). Determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storm, missing trigger, circular trigger).

Execute the following four roles in strict sequence. A role SHALL NOT begin until the prior role's required outputs are produced and declared complete.

---

### ROLE 1 — SCOPE ARBITER

**The Scope Arbiter produces no analytical content about the trigger chain. The Arbiter builds the structural foundation all subsequent roles execute against.**

The Arbiter SHALL produce the following three locked artifacts before issuing the Arbiter Clearance (AC-1):

**Artifact A: SCOPE GATE**

Declare the formal event tuple that defines eligibility for candidate status. A trigger that does not satisfy this tuple is excluded before enumeration begins, not filtered during enumeration.

```
SCOPE GATE
Entity:        [entity type]
Operation:     [create | update | delete]
Triggering Field: [field name or event]
Value Transition: [from-value] -> [to-value]
Eligibility Rule: A trigger is a CANDIDATE if and only if it is registered to fire
                  on the above entity, operation, and field (or carries no field
                  filter but is registered to this entity/operation).
```

**Artifact B: EXCLUSION LOG**

Before declaring any candidate, sweep every automation layer and record its disposition. A layer with no registered triggers for this scope is EXCLUDED with a stated reason. A layer with at least one in-scope trigger is INCLUDED.

```
EXCLUSION LOG
| Layer                        | Disposition      | Reason if Excluded |
|------------------------------|------------------|--------------------|
| Dataverse sync plug-in steps |                  |                    |
| Dataverse async plug-in steps|                  |                    |
| Automated cloud flows        |                  |                    |
| Scheduled cloud flows        |                  |                    |
| Instant cloud flows          |                  |                    |
| Business rules               |                  |                    |
| Classic workflows            |                  |                    |
| [any additional layer]       |                  |                    |
```

Every included layer feeds the candidate denominator. Every excluded layer does not. If a layer's disposition is uncertain, mark UNCERTAIN with a stated reason; uncertain layers are included in the denominator with a `[?]` flag.

**Artifact C: PROHIBITION CONTRACTS**

Declare one prohibition contract per subsequent role. A prohibition contract names what that role is structurally barred from doing. Prohibitions are binding: a role that violates its contract incurs a `[PROHIBITION BREACH: Role N | action]` marker.

```
PROHIBITION CONTRACTS
Role 2 (Enumeration Expert) PROHIBITS:
  - Adding candidates not listed in the denominator declared by Role 1
  - Omitting the Condition (Skipped) slot on any firing entry
  - Entering Phase 3 (async enumeration) before Phase 2 (sync enumeration) is complete

Role 3 (Cascade Analyst) PROHIBITS:
  - Adding new trigger rows not originating from a side-effect field write in Role 2/3 output
  - Declaring a cascade chain closed without a [TERMINAL] marker on the final row
  - Skipping back-edge detection

Role 4 (Closure Auditor) PROHIBITS:
  - Reporting a CLOSED denominator before all three anomaly verdicts are issued
  - Omitting any named counter from the CLOSURE CHECK block
  - Allowing a counter value > 0 to be reported without a remediation reference
```

**ALL-SLOTS-REQUIRED MANDATE** (issued by the Scope Arbiter; governs all roles):

Every named slot in every entry template (FIRING ENTRY, NON-FIRING ENTRY, CASCADE ENTRY, ANOMALY VERDICT) is required. An empty named slot is a structural gap equivalent to a missing entry. "N/A" is not a valid slot value unless the slot definition explicitly permits it.

**Arbiter Clearance AC-1:** Issued when Artifact A, B, and C are complete and the ALL-SLOTS-REQUIRED MANDATE is declared. Role 2 SHALL NOT begin without AC-1.

---

### ROLE 2 — ENUMERATION EXPERT

**Entry condition:** AC-1 received and Artifact A (SCOPE GATE), B (EXCLUSION LOG), C (PROHIBITION CONTRACTS) are present.

The Enumeration Expert SHALL enumerate all candidate triggers from the Role 1 denominator. Candidates that satisfy SCOPE GATE and have their conditions met at runtime are FIRING ENTRIES. Candidates in scope but with conditions not met are NON-FIRING ENTRIES.

**Execution Order Rules (EOR):**

Declare these before any trigger entry. Every firing entry carries an `EOR-NN` citation.

| EOR-ID | Rule |
|--------|------|
| EOR-01 | Synchronous plug-in steps fire before asynchronous plug-in steps |
| EOR-02 | Pre-operation sync steps fire before post-operation sync steps |
| EOR-03 | Within a tier, lower pipeline stage number fires first |
| EOR-04 | Automated cloud flows fire after the originating transaction commits |
| EOR-05 | Flows on the same trigger event are not guaranteed sequential; treat as concurrent unless connector documentation states otherwise |

**Phase 2a — Sync Tier Enumeration**

| # | Trigger Name | Flow Type | Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Registration Witness | EOR Citation | Anomaly Flag |
|---|-------------|-----------|------|--------------|-------------|--------------|-------------|-------------------|---------------------|---------------------|-------------|-------------|

Phase 2a exit condition: all sync-tier candidates have a resolved entry; all slots populated; no blank cells.

**Phase 2b — Async Tier Enumeration**

| # | Trigger Name | Flow Type | Tier | Latency Class | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Registration Witness | EOR Citation | Anomaly Flag |
|---|-------------|-----------|------|--------------|--------------|-------------|--------------|-------------|-------------------|---------------------|---------------------|-------------|-------------|

Phase 2b exit condition: all async-tier candidates have a resolved entry; latency class annotated; all slots populated.

**Negative vocabulary example (required):** At least one term deviating from approved platform vocabulary SHALL appear here with its correction. `[VOCAB FAIL: "workflow" -> automated cloud flow]`

**Denominator Reconciliation (pre-cascade):** firing_so_far + non-firing_so_far = N declared in Role 1. State count. If sum ≠ N, flag `[RECON FAIL: expected N, found M]`.

---

### ROLE 3 — CASCADE ANALYST

**Entry condition:** Role 2 complete; both Phase 2a and Phase 2b tables produced; denominator pre-reconciliation stated.

The Cascade Analyst SHALL trace every cascade chain originating from side-effect field writes in Role 2 output to its terminal. Each chain receives a Chain ID (CH-NN). The final row of each chain SHALL carry `[TERMINAL]`. Back-edge detection SHALL be applied to the adjacency structure.

**CASCADE DEPTH BUDGET:** Maximum chain depth = 5. Every cascade entry carries `[Depth: N/5]`. A chain exceeding depth 5 SHALL produce a `[DEPTH EXCEEDED: CH-NN]` entry and halt tracing for that chain.

| Chain ID | Depth | Step | Originating Trigger | Side-Effect Field | Field Write Value | Downstream Trigger | Downstream Tier | Chain-Status |
|----------|-------|------|--------------------|--------------------|-------------------|-------------------|-----------------|-------------|

**Back-edge detection result:** [adjacency list examined; cycles found / no cycles found with path listed]

Exit condition: all side-effect writes evaluated; all chains carry Chain-Status; back-edge detection reported.

---

### ROLE 4 — CLOSURE AUDITOR

**Entry condition:** Roles 1–3 complete; all tables produced; AC-1 on record.

**Anomaly Verdicts:**

Each verdict cites specific numbered rows from Phase 2a, 2b, and Cascade tables. A verdict without row citation is `[INSUFFICIENT: FM-12]`.

```
TRIGGER STORM
Evidence rows: [cite rows]
Verdict: CONFIRMED / NOT DETECTED
Remediation (if confirmed): [named step]

MISSING TRIGGER
Evidence rows: [cite rows]
Exclusion log reference: [Artifact B row]
Verdict: CONFIRMED / NOT DETECTED
Remediation (if confirmed): [named step]

CIRCULAR TRIGGER
Evidence rows: [cite rows]
Back-edge detection result: [from Role 3]
Verdict: CONFIRMED / NOT DETECTED
Remediation (if confirmed): [named step]
```

**CLOSURE CHECK**

```
CLOSURE CHECK
EOR citations missing:                    {count} [must be 0]
Firing entries missing Condition (Skipped): {count} [must be 0]
Entries missing Registration Witness:     {count} [must be 0]
Entries missing bilateral counterfactual: {count} [must be 0]
Cascade chains without [TERMINAL]:        {count} [must be 0]
Anomaly verdicts without row citation:    {count} [must be 0]
Exclusion log entries missing disposition:{count} [must be 0]
PROHIBITION BREACHES detected:            {count} [must be 0]
```

**Denominator Closure:**

`firing + non-firing + unresolved = N` → CLOSED / GAP DETECTED `[RECON MISS]`

Exit condition: CLOSURE CHECK block complete; all counters declared; denominator closure stated.

---

## V-02

**Variation axis:** Output format — Table-centric with global ALL-SLOTS-REQUIRED mandate
**Hypothesis:** Declaring the all-slots mandate once as a named global structural rule (C-22) and then rendering every entry type as a table where each column is a mandatory named slot makes empty slots visually detectable by column scan. Compliance with C-15 (bilateral counterfactual), C-16 (registration witness), and C-17 (EOR citation) becomes a formatting property rather than a per-entry discipline problem — a reviewer verifies slot presence by confirming no column is blank, not by re-reading each entry.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to `Inactive` (1). Determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storm, missing trigger, circular trigger).

---

### STRUCTURAL INVARIANT — ALL SLOTS REQUIRED

**This invariant governs every entry produced in this output:**

> All named slots in all entry types (FIRING ENTRY, NON-FIRING ENTRY, CASCADE ENTRY, ANOMALY VERDICT) are required. An empty named slot is a structural gap equivalent to a missing entry. "N/A" is not a valid value unless the slot definition explicitly permits it. This mandate applies uniformly across all entry types and all phases. An output that states per-entry obligations piecemeal across separate sections without this unifying rule is non-conforming with this invariant.

A slot left blank is tagged `[SLOT EMPTY: entry-name | slot-name]` by the reviewer. A prompt that produces a blank slot after declaring this invariant compounds the violation — the defect was pre-named.

---

### SCOPE GATE

Before any candidates are named, declare the formal event tuple:

```
SCOPE GATE
Entity:              account (Dynamics 365 Sales)
Operation:           Update
Triggering Field:    statecode
Value Transition:    Active (0) -> Inactive (1)
Eligibility Rule:    A trigger is a CANDIDATE if and only if its activation condition
                     is satisfied by this entity + operation + field + transition.
                     Triggers registered to other entities, other fields, or other
                     value transitions are OUT-OF-SCOPE and excluded before enumeration.
```

---

### EXCLUSION LOG

```
EXCLUSION LOG
| Layer                         | Disposition | Reason if Excluded |
|-------------------------------|-------------|-------------------|
| Dataverse sync plug-in steps  |             |                   |
| Dataverse async plug-in steps |             |                   |
| Automated cloud flows         |             |                   |
| Scheduled cloud flows         |             |                   |
| Instant cloud flows           |             |                   |
| Business rules                |             |                   |
| Classic workflows             |             |                   |
```

Total layers included: [N_layers]. Candidate triggers sourced from included layers only.

---

### EXECUTION ORDER RULE TABLE

| EOR-ID | Rule | Scope |
|--------|------|-------|
| EOR-01 | Sync plug-in steps fire before async plug-in steps | All tiers |
| EOR-02 | Pre-operation before post-operation within sync tier | Sync tier |
| EOR-03 | Lower stage number fires first within same tier | Sync tier |
| EOR-04 | Automated cloud flows fire after transaction commits | Async tier |
| EOR-05 | Concurrent async flows on same event: order not guaranteed | Async tier |

Every FIRING ENTRY carries an `EOR-NN` citation in its `Order Rule` slot. An entry without an EOR citation violates the ALL-SLOTS-REQUIRED invariant.

---

### CANDIDATE DENOMINATOR

List every trigger evaluated — firing and non-firing — before filtering:

| # | Candidate Trigger | Layer | Tier | Activation Condition | Disposition |
|---|------------------|-------|------|---------------------|-------------|

Total N = [integer declared here]. This N is the denominator for closure.

---

### SYNC TIER ENUMERATION

**Platform definition:** A synchronous trigger executes within the originating database transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `"workflow"` is not an approved term for an automated cloud flow. Correct: `automated cloud flow`.

**FIRING ENTRIES — Sync Tier:**

| # | Trigger Name | Flow Type | Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Registration Witness | Order Rule | Anomaly Flag |
|---|-------------|-----------|------|--------------|-------------|--------------|-------------|-------------------|---------------------|---------------------|-----------|-------------|

*All columns required per ALL-SLOTS-REQUIRED invariant. Empty cell = structural gap.*

**NON-FIRING ENTRIES — Sync Tier:**

| # | Trigger Name | Flow Type | Reason Not Firing | Condition That Would Cause Firing | Condition Present in This Scenario That Blocks It | Registration Witness |
|---|-------------|-----------|------------------|----------------------------------|--------------------------------------------------|---------------------|

*All columns required. Trigger present in denominator but absent from this table = omission.*

---

### ASYNC TIER ENUMERATION

**Platform definition:** An asynchronous trigger executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change event).

**FIRING ENTRIES — Async Tier:**

| # | Trigger Name | Flow Type | Tier | Latency Class | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Registration Witness | Order Rule | Anomaly Flag |
|---|-------------|-----------|------|--------------|--------------|-------------|--------------|-------------|-------------------|---------------------|---------------------|-----------|-------------|

**NON-FIRING ENTRIES — Async Tier:**

| # | Trigger Name | Flow Type | Reason Not Firing | Condition That Would Cause Firing | Blocking Condition | Registration Witness |
|---|-------------|-----------|------------------|----------------------------------|--------------------|---------------------|

---

### CASCADE TRACING

**CASCADE DEPTH BUDGET: MAX = 5. Every row carries `[Depth: N/5]`.**

| Chain ID | Depth | Step | Originating Trigger | Side-Effect Field | Downstream Trigger | Downstream Tier | Chain-Status |
|----------|-------|------|--------------------|--------------------|-------------------|-----------------|-------------|

Final row of each chain: `[TERMINAL]`. Chain exceeding budget: `[DEPTH EXCEEDED: CH-NN]`.

Back-edge detection: examine adjacency list [trigger → field → trigger] for cycles. Report: CYCLES FOUND [path] / NO CYCLES [adjacency list].

---

### ANOMALY VERDICTS

All three verdict blocks are required. A missing verdict block fails C-04. Each verdict cites rows from enumeration tables (e.g., "Sync rows 2, 4") and the exclusion log where applicable.

**TRIGGER STORM VERDICT**

| Slot | Value |
|------|-------|
| Evidence rows | |
| Storm condition assessed | Total firing count vs. capacity threshold |
| Verdict | CONFIRMED / NOT DETECTED |
| Remediation (if confirmed) | |

**MISSING TRIGGER VERDICT**

| Slot | Value |
|------|-------|
| Evidence rows | |
| Exclusion log reference | |
| Gap assessment | Expected behavior vs. observed firing surface |
| Verdict | CONFIRMED / NOT DETECTED |
| Remediation (if confirmed) | |

**CIRCULAR TRIGGER VERDICT**

| Slot | Value |
|------|-------|
| Evidence rows | |
| Back-edge detection result | |
| Cycle path (if confirmed) | |
| Verdict | CONFIRMED / NOT DETECTED |
| Remediation (if confirmed) | |

---

### TRIGGER MAP

| # | Trigger Name | Tier | Anomaly Flag | Spawns (Chain ID) |
|---|-------------|------|-------------|-------------------|

---

### CLOSURE CHECK

```
CLOSURE CHECK
EOR citations missing from firing entries:          {count} [must be 0]
Firing entries missing Condition (Skipped):         {count} [must be 0]
Entries missing Registration Witness:               {count} [must be 0]
Entries missing bilateral counterfactual:           {count} [must be 0]
Cascade chains without [TERMINAL] row:              {count} [must be 0]
Anomaly verdicts without row citation:              {count} [must be 0]
Empty cells in any required slot:                   {count} [must be 0]
```

**Denominator Closure:**
`firing_count + non_firing_count + unresolved_count = N`
Result: CLOSED / GAP DETECTED `[RECON MISS]`

---

## V-03

**Variation axis:** Lifecycle emphasis — Each phase carries a named PROHIBITION block as a required structural section
**Hypothesis:** When prohibition contracts are a mandatory named section within each phase body (not a preamble declaration), the phase cannot be declared complete unless its prohibitions are stated. This makes C-21 self-enforcing through exit-condition checking: a phase missing its PROHIBITION block fails its own exit condition before a reviewer even checks C-21. The lifecycle structure also creates natural entry/exit gate points that surface C-20's closure counters as the Phase 6 exit artifact.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to `Inactive` (1). Determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storm, missing trigger, circular trigger).

Execute the following six phases. Each phase contains four required sections: ENTRY CONDITION, PROHIBITIONS, JOB, and EXIT CONDITION. A phase that omits any of these four sections is structurally incomplete and its outputs are not valid inputs to the next phase.

---

### Phase 1 — Scope Declaration and Denominator

**ENTRY CONDITION:** Phase 1 begins unconditionally. No prior phase output is required.

**PROHIBITIONS:**
- Phase 1 PROHIBITS enumerating trigger inputs, outputs, or side effects. Scope declaration only.
- Phase 1 PROHIBITS issuing any anomaly verdict or assessment.
- Phase 1 PROHIBITS entering Phase 2 before N is declared and the SCOPE GATE is written.

**JOB:**

Declare the SCOPE GATE:

```
SCOPE GATE
Entity: account (Dynamics 365 Sales)
Operation: Update
Triggering Field: statecode
Value Transition: Active (0) -> Inactive (1)
Eligibility: Triggers registered for this entity + operation + field transition are CANDIDATES.
             All other triggers are OUT-OF-SCOPE and must not appear in enumeration phases.
```

Declare the EXCLUSION LOG — sweep all automation layers:

```
EXCLUSION LOG
| Layer                         | Disposition (INCLUDED / EXCLUDED) | Reason if Excluded |
|-------------------------------|----------------------------------|-------------------|
| Dataverse sync plug-in steps  |                                  |                   |
| Dataverse async plug-in steps |                                  |                   |
| Automated cloud flows         |                                  |                   |
| Scheduled cloud flows         |                                  |                   |
| Instant cloud flows           |                                  |                   |
| Business rules                |                                  |                   |
| Classic workflows             |                                  |                   |
```

Declare ALL-SLOTS-REQUIRED MANDATE: All named slots in all entry templates are required. Empty named slot = structural gap.

Declare the CANDIDATE DENOMINATOR: List every candidate trigger (firing and non-firing). Total N = [integer].

Open three anomaly investigation slots: Storm: OPEN | Missing: OPEN | Circular: OPEN

**EXIT CONDITION:** Phase 1 is complete when: SCOPE GATE declared, EXCLUSION LOG complete with disposition per layer, CANDIDATE DENOMINATOR declared with total N, all three anomaly slots OPEN.

---

### Phase 2 — Sync Tier Enumeration

**ENTRY CONDITION:** Phase 1 complete; SCOPE GATE, EXCLUSION LOG, and denominator N present.

**PROHIBITIONS:**
- Phase 2 PROHIBITS adding candidates not declared in Phase 1's denominator.
- Phase 2 PROHIBITS enumerating asynchronous triggers (those belong to Phase 3).
- Phase 2 PROHIBITS advancing to Phase 3 before all sync-tier denominator entries are resolved.
- Phase 2 PROHIBITS leaving any slot blank in a FIRING ENTRY or NON-FIRING ENTRY.

**JOB:**

Declare the EXECUTION ORDER RULE (EOR) table:

| EOR-ID | Ordering Principle |
|--------|-------------------|
| EOR-01 | Sync plug-in steps before async plug-in steps |
| EOR-02 | Pre-operation before post-operation within sync tier |
| EOR-03 | Lower stage number fires first within same tier |

Every firing entry carries an `EOR-NN` citation.

**FIRING ENTRY template (all slots required):**
```
Trigger Name:
Flow Type:
Execution Tier:      sync
Trigger Event:
Input Fields:
Output Action:
Side Effects:
Condition (Taken):   [what must be true for this trigger to fire -- met in this scenario]
Condition (Skipped): [what would cause this trigger NOT to fire -- not present here]
Registration Witness:
EOR Citation:
Anomaly Flag:
```

**NON-FIRING ENTRY template (all slots required):**
```
Trigger Name:
Flow Type:
Reason Not Firing:
Condition (Taken):   [what would cause this trigger to fire -- not present in this scenario]
Condition (Skipped): [what IS true that blocks this trigger]
Registration Witness:
```

Negative vocabulary example (required inline): `[VOCAB FAIL: "workflow" -> automated cloud flow]`

**EXIT CONDITION:** Phase 2 is complete when: all sync-tier denominator entries resolved; no slot blank; EOR citations present on all firing entries; PROHIBITIONS not violated.

---

### Phase 3 — Async Tier Enumeration

**ENTRY CONDITION:** Phase 2 complete; sync trigger table produced with all slots populated.

**PROHIBITIONS:**
- Phase 3 PROHIBITS adding new candidates beyond Phase 1 denominator.
- Phase 3 PROHIBITS tracing cascade chains (Phase 4's mandate).
- Phase 3 PROHIBITS advancing to Phase 4 before all async-tier denominator entries are resolved.

**JOB:**

EOR additions for async tier:

| EOR-ID | Ordering Principle |
|--------|-------------------|
| EOR-04 | Automated cloud flows fire after originating transaction commits |
| EOR-05 | Concurrent async flows on same event: order not guaranteed |

Enumerate all async-tier denominator entries using the same FIRING ENTRY / NON-FIRING ENTRY templates. Add `Latency Class` slot to every async FIRING ENTRY (near-real-time / standard / batch).

**EXIT CONDITION:** Phase 3 is complete when: all async-tier denominator entries resolved; latency class annotated; all slots populated; PROHIBITIONS not violated.

---

### Phase 4 — Cascade Tracing

**ENTRY CONDITION:** Phases 2 and 3 complete; both sync and async trigger tables produced.

**PROHIBITIONS:**
- Phase 4 PROHIBITS adding new trigger rows that do not originate from a side-effect field write declared in Phase 2 or 3.
- Phase 4 PROHIBITS declaring a chain closed without a `[TERMINAL]` marker on the final row.
- Phase 4 PROHIBITS advancing to Phase 5 before back-edge detection is applied.

**JOB:**

**CASCADE DEPTH BUDGET: MAX = 5.**

| Chain ID | Depth | Step | Originating Trigger | Side-Effect Field | Downstream Trigger | Chain-Status |
|----------|-------|------|--------------------|--------------------|-------------------|-------------|

Every cascade entry carries `[Depth: N/5]`. Chain exceeding budget: `[DEPTH EXCEEDED: CH-NN]`.

Back-edge detection: construct adjacency list [trigger → field mutated → trigger]. Apply back-edge detection. Report: CYCLES / NO CYCLES with adjacency structure shown.

**EXIT CONDITION:** Phase 4 is complete when: all side-effect writes evaluated; all chains carry Chain-Status; `[TERMINAL]` on final row of each chain; back-edge detection result reported.

---

### Phase 5 — Anomaly Assessment

**ENTRY CONDITION:** Phase 4 complete; all cascade chains carry Chain-Status; back-edge detection result present.

**PROHIBITIONS:**
- Phase 5 PROHIBITS issuing any verdict without citing specific numbered rows from Phase 2, 3, or 4.
- Phase 5 PROHIBITS using bare assertion language ("no storms found") as a complete verdict — evidence must be cited.
- Phase 5 PROHIBITS closing an anomaly investigation slot without a CONFIRMED or NOT DETECTED verdict.
- Phase 5 PROHIBITS advancing to Phase 6 before all three investigation slots are closed.

**JOB:**

For each anomaly class, close the investigation slot opened in Phase 1:

**TRIGGER STORM — Investigation closure:**
Evidence rows: | Storm threshold: | Verdict: CONFIRMED / NOT DETECTED | Remediation:

**MISSING TRIGGER — Investigation closure:**
Evidence rows: | Exclusion log reference: | Gap assessment: | Verdict: CONFIRMED / NOT DETECTED | Remediation:

**CIRCULAR TRIGGER — Investigation closure:**
Evidence rows: | Back-edge result: | Cycle path (if confirmed): | Verdict: CONFIRMED / NOT DETECTED | Remediation:

**EXIT CONDITION:** Phase 5 is complete when: all three investigation slots closed with CONFIRMED or NOT DETECTED; every verdict cites evidence rows; confirmed anomalies have remediation; PROHIBITIONS not violated.

---

### Phase 6 — Trigger Map and Closure

**ENTRY CONDITION:** Phase 5 complete; all three anomaly verdicts issued; all investigation slots closed.

**PROHIBITIONS:**
- Phase 6 PROHIBITS reporting CLOSED denominator before CLOSURE CHECK counters are populated.
- Phase 6 PROHIBITS leaving any CLOSURE CHECK counter blank.
- Phase 6 PROHIBITS reporting a counter value > 0 without identifying which entries are non-conformant.

**JOB:**

**Trigger Map:**

| # | Trigger Name | Tier | Anomaly Flag | Spawns (Chain ID) |
|---|-------------|------|-------------|-------------------|

**CLOSURE CHECK:**

```
CLOSURE CHECK
EOR citations missing from firing entries:           {count} [must be 0]
Firing entries missing Condition (Skipped):          {count} [must be 0]
Non-firing entries missing bilateral counterfactual: {count} [must be 0]
Entries missing Registration Witness:                {count} [must be 0]
Cascade chains without [TERMINAL]:                   {count} [must be 0]
Anomaly verdicts without row citation:               {count} [must be 0]
Anomaly verdicts missing Exclusion log reference:    {count} [must be 0]
PROHIBITION BREACHES in any phase:                   {count} [must be 0]
```

**Denominator Closure:** `firing + non-firing + unresolved = N` → CLOSED / GAP DETECTED

**EXIT CONDITION:** Phase 6 is complete when: trigger map covers all candidates; CLOSURE CHECK block complete; all counters declared; denominator closure stated; no counter > 0 without identification.

---

## V-04

**Variation axis:** Role sequence inverted (anomaly frame first) + formal phrasing register (SHALL/MUST throughout)
**Hypothesis:** Opening with an explicit anomaly investigation contract — three OPEN investigation questions declared before any enumeration begins — forces denominator-first thinking because the analyst must name what they are counting toward before counting. Combined with formal SHALL/MUST language in every obligation position, this framing makes prohibition contracts (C-21) emerge naturally: each role must declare what it is structurally barred from adding because the investigation contract already defines the boundary.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to `Inactive` (1). Your output SHALL determine exactly which automations fire, in what order, with what inputs and outputs, and SHALL identify all trigger pathologies (storm, missing trigger, circular trigger).

The following protocol SHALL be executed in strict sequence. No phase SHALL begin before the prior phase's required deliverables are issued. All gate statements in all phases SHALL use formal obligation language (SHALL/MUST) in the obligation position. A phase gate statement using descriptive language ("this phase is complete when") rather than formal obligation language ("this phase SHALL be declared complete when") is non-conforming.

---

### PROTOCOL PREAMBLE

**Platform Vocabulary Contract**

All trigger types, execution tiers, and flow categories SHALL use the platform's approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| Dataverse plug-in | plugin, CRM plugin |
| sync plug-in step | synchronous plugin |
| async plug-in step | asynchronous plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |

A term deviating from this contract SHALL be tagged: `[VOCAB FAIL: "actual" -> correction]`

**ALL-SLOTS-REQUIRED MANDATE:** All named slots in all entry templates are required. An empty named slot is a structural gap. This mandate applies uniformly across all entry types without exception.

---

### Phase 1 — Anomaly Investigation Contract

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE is declared.

**Job:** Phase 1 SHALL open three anomaly investigations before any trigger candidate is named. Opening an investigation commits the output to closing it with evidence — not with assertion. An investigation closed without evidence citation is a protocol violation.

**Prohibition:** Phase 1 SHALL NOT name any trigger candidate. Phase 1 SHALL NOT enumerate any trigger property. Phase 1 SHALL NOT assess any anomaly verdict. Phase 1 is structural framing only.

**ANOMALY INVESTIGATIONS — Status: OPEN**

| Class | Investigation Question | Evidence Required to Close | Status |
|-------|----------------------|---------------------------|--------|
| Trigger Storm | Does the `statecode` change from Active to Inactive cause more triggers to fire than the environment can absorb without throttling, sequencing failure, or platform limit breach? | Firing trigger count; platform concurrency limits; throttle window assessment | OPEN |
| Missing Trigger | Is there an expected automation for this account suspension transition — such as downstream record deactivation, notification dispatch, or audit logging — that does not appear in the firing surface? | Denominator candidate list; gap between expected behavior and observed trigger surface | OPEN |
| Circular Trigger | Does any trigger's side-effect output create a field write that causes the same trigger or an upstream trigger to fire again, creating a loop? | Adjacency list; back-edge detection result | OPEN |

**Exit condition:** Phase 1 SHALL be declared complete when all three investigations are OPEN and their evidence requirements are stated.

---

### Phase 2 — Scope Gate and Candidate Denominator

**Entry condition:** Phase 2 SHALL begin when Phase 1 is complete and all three investigation slots are OPEN.

**Job:** Phase 2 SHALL declare the formal scope gate and enumerate all candidates without condition filtering.

**Prohibition:** Phase 2 SHALL NOT evaluate whether any candidate fires. Phase 2 SHALL NOT issue any anomaly assessment. Phase 2 SHALL NOT produce trigger input/output entries. Phase 2 SHALL NOT advance to Phase 3 before N is declared.

**SCOPE GATE:**
```
Entity: account (Dynamics 365 Sales)
Operation: Update
Triggering Field: statecode
Value Transition: Active (0) -> Inactive (1)
Eligibility: A trigger SHALL be a candidate if and only if its activation
             condition is satisfiable by this entity + operation + field transition.
```

**EXCLUSION LOG** — sweep all automation layers before declaring candidates:

```
| Layer                         | Disposition | Reason if Excluded |
|-------------------------------|-------------|-------------------|
| Dataverse sync plug-in steps  |             |                   |
| Dataverse async plug-in steps |             |                   |
| Automated cloud flows         |             |                   |
| Scheduled cloud flows         |             |                   |
| Business rules                |             |                   |
| Classic workflows             |             |                   |
```

**Candidate Denominator:**

| # | Candidate Trigger | Layer | Tier | Activation Condition |
|---|-----------------|-------|------|---------------------|

Total N = [integer]. This N SHALL be the denominator for all closure operations.

**Exit condition:** Phase 2 SHALL be declared complete when the SCOPE GATE is declared, the EXCLUSION LOG is complete, and N is declared.

---

### Phase 3 — Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 is complete and N is declared.

**Job:** Phase 3 SHALL enumerate all N candidates. Every candidate SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. Sync-tier entries SHALL precede async-tier entries.

**Prohibition:** Phase 3 SHALL NOT add candidates beyond Phase 2's denominator. Phase 3 SHALL NOT trace cascade chains — that is Phase 4's mandate. Phase 3 SHALL NOT advance to Phase 4 before all N entries are resolved.

**Execution Order Rules:**

| EOR-ID | Rule |
|--------|------|
| EOR-01 | Sync plug-in steps SHALL fire before async plug-in steps |
| EOR-02 | Pre-operation sync steps SHALL fire before post-operation sync steps |
| EOR-03 | Lower stage number SHALL fire first within same tier |
| EOR-04 | Automated cloud flows SHALL fire after the originating transaction commits |
| EOR-05 | Concurrent async flows on the same event SHALL be treated as unordered unless documentation states otherwise |

**FIRING ENTRY** (all slots required per ALL-SLOTS-REQUIRED MANDATE):

```
Trigger Name:
Flow Type:
Execution Tier:       [sync | async | scheduled]
Latency Class:        [sync-transactional | near-real-time | standard | batch] (async entries only)
Trigger Event:
Input Fields:
Output Action:
Side Effects:
Condition (Taken):    [condition met in this scenario that causes firing]
Condition (Skipped):  [condition absent in this scenario that would prevent firing]
Registration Witness:
EOR Citation:         [EOR-NN]
Anomaly Flag:         [none | storm-candidate | missing-candidate | circular-candidate]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:
Condition (Taken):    [condition that WOULD cause this trigger to fire -- not present here]
Condition (Skipped):  [condition present in this scenario that blocks firing]
Registration Witness:
```

Negative vocabulary example (SHALL appear inline): `[VOCAB FAIL: "workflow" -> automated cloud flow]`

**Exit condition:** Phase 3 SHALL be declared complete when all N candidates are resolved; all slots populated; EOR citations present on all firing entries; sync entries precede async entries.

---

### Phase 4 — Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phase 3 is complete and all N entries are resolved.

**Job:** Phase 4 SHALL trace every cascade chain from side-effect field writes to terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL carry `[TERMINAL]`. Back-edge detection SHALL be applied to the adjacency structure.

**Prohibition:** Phase 4 SHALL NOT add trigger rows not derived from a side-effect write in Phase 3. Phase 4 SHALL NOT issue anomaly verdicts. Phase 4 SHALL NOT declare a chain closed without `[TERMINAL]`.

**CASCADE DEPTH BUDGET: MAX = 5. Every cascade entry SHALL carry `[Depth: N/5]`.**

| Chain ID | Depth | Step | Originating Trigger | Side-Effect Field | Downstream Trigger | Tier | Chain-Status |
|----------|-------|------|--------------------|--------------------|-------------------|------|-------------|

Back-edge detection: construct adjacency list [trigger → field → trigger]. Apply back-edge test. Report: CYCLES / NO CYCLES.

**Exit condition:** Phase 4 SHALL be declared complete when all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection is reported.

---

### Phase 5 — Anomaly Verdict and Investigation Closure

**Entry condition:** Phase 5 SHALL begin when Phase 4 is complete and back-edge detection is reported.

**Job:** Phase 5 SHALL close all three investigations opened in Phase 1 by issuing evidence-anchored verdicts. Each verdict SHALL cite specific numbered rows from Phase 3 and Phase 4.

**Prohibition:** Phase 5 SHALL NOT issue a verdict without citing row evidence. Phase 5 SHALL NOT use bare assertion language as a complete verdict. Phase 5 SHALL NOT leave any investigation slot in OPEN status. Phase 5 SHALL NOT advance to Phase 6 before all three slots are CLOSED.

**TRIGGER STORM — Investigation closure:**
Evidence rows: | Count assessed: | Verdict: CONFIRMED / NOT DETECTED | Investigation: CLOSED | Remediation (if confirmed):

**MISSING TRIGGER — Investigation closure:**
Evidence rows: | Exclusion log reference: | Gap assessment: | Verdict: CONFIRMED / NOT DETECTED | Investigation: CLOSED | Remediation (if confirmed):

**CIRCULAR TRIGGER — Investigation closure:**
Evidence rows: | Back-edge result: | Cycle path (if confirmed): | Verdict: CONFIRMED / NOT DETECTED | Investigation: CLOSED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when all three investigations are CLOSED and every verdict cites evidence rows.

---

### Phase 6 — Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 is complete and all three investigations are CLOSED.

**Job:** Phase 6 SHALL produce the trigger map and issue the CLOSURE CHECK block. The CLOSURE CHECK SHALL precede the denominator closure statement.

**Prohibition:** Phase 6 SHALL NOT report denominator CLOSED before the CLOSURE CHECK block is complete. Phase 6 SHALL NOT leave any CLOSURE CHECK counter blank. Phase 6 SHALL NOT report a counter > 0 without identifying the non-conformant entries.

**Trigger Map:**

| # | Trigger Name | Tier | Anomaly Flag | Spawns |
|---|-------------|------|-------------|--------|

**CLOSURE CHECK:**

```
CLOSURE CHECK
EOR citations missing:                               {count} [must be 0]
Firing entries missing Condition (Skipped):          {count} [must be 0]
Non-firing entries missing bilateral counterfactual: {count} [must be 0]
Entries missing Registration Witness:                {count} [must be 0]
Cascade chains missing [TERMINAL]:                   {count} [must be 0]
Cascade entries missing Depth counter:               {count} [must be 0]
Anomaly verdicts missing row citation:               {count} [must be 0]
Investigations closed without evidence:              {count} [must be 0]
Prohibition breaches (any phase):                    {count} [must be 0]
```

**Denominator Closure:** `firing + non-firing + unresolved = N` → CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map is produced; CLOSURE CHECK is complete; all counters declared; denominator closure stated.

---

## V-05

**Variation axis:** Output format + Lifecycle emphasis + Inertia framing — status-quo contrast opens the prompt; CLOSURE CHECK block closes it
**Hypothesis:** Naming the inertia baseline explicitly (what a Power Automate admin would typically do when asked "what fires when this account is deactivated?") creates a concrete contrast that makes each structural artifact's purpose evident. An analyst who sees that the informal approach produces no scope gate, no denominator, no closure, and no prohibition contracts is more likely to populate each artifact with substance rather than compliance tokens — because the contrast names what happens without each artifact. The CLOSURE CHECK block at the end then audits whether the substance was actually present.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to `Inactive` (1). Determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storm, missing trigger, circular trigger).

---

### WHY A TYPICAL AUDIT IS NOT SUFFICIENT

A typical Power Automate admin responding to "what fires when we deactivate an account?" produces something like this:

> "We have a flow that sends a notification when an account is deactivated. There's probably a plug-in that updates related contacts. I'm not sure about the ordering. I don't think there are any loops."

This informal audit has five structural gaps that this simulation is designed to close:

| Gap | What the Informal Audit Misses | What This Simulation Produces |
|-----|-------------------------------|-------------------------------|
| No scope gate | No formal definition of what counts as in-scope; analyst relies on memory | Named SCOPE GATE with entity + operation + field + value transition |
| No denominator | Analyst lists what they remember; non-firing candidates are invisible | CANDIDATE DENOMINATOR: named list of every evaluated trigger |
| No exclusion accounting | Layers not checked are not reported; gaps are silent | EXCLUSION LOG: disposition for every automation layer |
| No closure | Audit ends when the analyst stops thinking; completeness is unverifiable | CLOSURE CHECK: zero-tolerance counters per per-entry obligation |
| No prohibition contracts | Each analyst phase can silently expand scope or add candidates | PROHIBITION blocks: named barred actions per phase |

This simulation is complete when the informal audit's five gaps are closed by artifact.

---

### ALL-SLOTS-REQUIRED MANDATE

All named slots in all entry types (FIRING ENTRY, NON-FIRING ENTRY, CASCADE ENTRY, ANOMALY VERDICT) are required. An empty named slot is a structural gap. This mandate collapses individual per-entry obligations (counterfactual required, witness required, EOR citation required) into one auditable rule: slot presence is the compliance test.

---

### Phase 1 — Scope and Denominator

**Entry condition:** Unconditional.

**PROHIBITIONS:**
- Phase 1 PROHIBITS enumerating trigger inputs, outputs, or execution order.
- Phase 1 PROHIBITS issuing any anomaly assessment.

**Job:**

**SCOPE GATE:**
```
Entity:           account (Dynamics 365 Sales)
Operation:        Update
Field:            statecode
Value Transition: Active (0) -> Inactive (1)
Eligibility:      Triggers registered for this entity + operation + field transition
                  are CANDIDATES. All others are OUT-OF-SCOPE.
```

**EXCLUSION LOG:**

| Layer | Disposition | Reason if Excluded |
|-------|-------------|-------------------|
| Dataverse sync plug-in steps | | |
| Dataverse async plug-in steps | | |
| Automated cloud flows | | |
| Scheduled cloud flows | | |
| Instant cloud flows | | |
| Business rules | | |
| Classic workflows | | |

*This is the artifact the informal audit omits. An excluded layer that is later found to contain a relevant trigger is a MISSING TRIGGER candidate.*

**CANDIDATE DENOMINATOR:**

| # | Candidate | Layer | Tier | Activation Condition |
|---|-----------|-------|------|---------------------|

Total N = [integer]. *The informal audit omits this. N makes completeness auditable.*

Open anomaly investigations: Storm: OPEN | Missing: OPEN | Circular: OPEN

**Exit condition:** SCOPE GATE, EXCLUSION LOG, CANDIDATE DENOMINATOR complete; N declared; investigations OPEN.

---

### Phase 2 — Sync Trigger Enumeration

**Entry condition:** Phase 1 complete; N declared.

**PROHIBITIONS:**
- Phase 2 PROHIBITS adding candidates beyond Phase 1's denominator.
- Phase 2 PROHIBITS enumerating async triggers.
- Phase 2 PROHIBITS advancing to Phase 3 with any sync-tier candidate unresolved.

**Job:**

**Execution Order Rules:**

| EOR-ID | Rule |
|--------|------|
| EOR-01 | Sync plug-in steps before async plug-in steps |
| EOR-02 | Pre-operation before post-operation (sync tier) |
| EOR-03 | Lower stage number first within same tier |

Negative vocabulary example (required): `[VOCAB FAIL: "workflow" -> automated cloud flow]`

**FIRING ENTRY** (all slots required — ALL-SLOTS-REQUIRED MANDATE applies):
```
Trigger Name:
Flow Type:
Execution Tier:      sync
Trigger Event:
Input Fields:
Output Action:
Side Effects:
Condition (Taken):   [what must be true for firing -- present in this scenario]
Condition (Skipped): [what would prevent firing -- absent in this scenario]
Registration Witness:
EOR Citation:        [EOR-NN]
Anomaly Flag:
```

**NON-FIRING ENTRY** (all slots required):
```
Trigger Name:
Flow Type:
Reason Not Firing:
Condition (Taken):   [what WOULD cause firing -- not present here]
Condition (Skipped): [what IS present that blocks firing]
Registration Witness:
```

*The informal audit produces no NON-FIRING ENTRIES. This is why denominator closure fails.*

**Exit condition:** All sync-tier candidates resolved; all slots populated; EOR citations on all firing entries.

---

### Phase 3 — Async Trigger Enumeration

**Entry condition:** Phase 2 complete; sync trigger table produced.

**PROHIBITIONS:**
- Phase 3 PROHIBITS adding candidates beyond Phase 1's denominator.
- Phase 3 PROHIBITS tracing cascade chains.

**Job:**

Additional EOR for async tier:

| EOR-ID | Rule |
|--------|------|
| EOR-04 | Automated cloud flows fire after originating transaction commits |
| EOR-05 | Concurrent async flows on same event: order not guaranteed |

Enumerate all async-tier denominator entries using FIRING ENTRY / NON-FIRING ENTRY templates. Add `Latency Class` to async FIRING ENTRY (near-real-time / standard / batch).

**Exit condition:** All async-tier candidates resolved; latency class annotated; all slots populated.

---

### Phase 4 — Cascade Tracing

**Entry condition:** Phases 2 and 3 complete; both tables produced.

**PROHIBITIONS:**
- Phase 4 PROHIBITS adding trigger rows not derived from a side-effect field write in Phase 2/3.
- Phase 4 PROHIBITS declaring a chain closed without `[TERMINAL]` on the final row.

**Job:**

**CASCADE DEPTH BUDGET: MAX = 5. Every entry carries `[Depth: N/5]`.**

| Chain ID | Depth | Step | Originating Trigger | Side-Effect Field | Downstream Trigger | Chain-Status |
|----------|-------|------|--------------------|--------------------|-------------------|-------------|

Back-edge detection: [adjacency list] → CYCLES / NO CYCLES

*The informal audit has no cascade tracing. A circular trigger that the informal audit misses appears here as a back-edge.*

**Exit condition:** All side-effect writes evaluated; all chains carry Chain-Status; back-edge detection reported.

---

### Phase 5 — Anomaly Assessment

**Entry condition:** Phase 4 complete; all chains carry Chain-Status.

**PROHIBITIONS:**
- Phase 5 PROHIBITS issuing a verdict without citing Phase 2/3/4 row evidence.
- Phase 5 PROHIBITS leaving any investigation slot OPEN.

**Job:**

**TRIGGER STORM:**
Evidence rows: | Verdict: CONFIRMED / NOT DETECTED | Investigation: CLOSED | Remediation:

**MISSING TRIGGER:**
Evidence rows: | Exclusion log reference: | Verdict: CONFIRMED / NOT DETECTED | Investigation: CLOSED | Remediation:
*The exclusion log reference is mandatory. A missing trigger that was caught by the exclusion log must be cited here. The informal audit has no exclusion log to cite.*

**CIRCULAR TRIGGER:**
Evidence rows: | Back-edge result: | Verdict: CONFIRMED / NOT DETECTED | Investigation: CLOSED | Remediation:

**Exit condition:** All three investigations CLOSED; all verdicts cite row evidence.

---

### Phase 6 — Trigger Map and Closure

**Entry condition:** Phase 5 complete; all investigations CLOSED.

**PROHIBITIONS:**
- Phase 6 PROHIBITS reporting CLOSED denominator before CLOSURE CHECK is complete.
- Phase 6 PROHIBITS leaving any counter blank.
- Phase 6 PROHIBITS reporting a counter > 0 without identifying non-conformant entries.

**Job:**

**Trigger Map:**

| # | Trigger Name | Tier | Latency | Anomaly Flag | Spawns (Chain ID) |
|---|-------------|------|---------|-------------|-------------------|

**CLOSURE CHECK** — *This is the artifact the informal audit omits entirely. It audits the five gaps named in the opening contrast.*

```
CLOSURE CHECK
-- Gap 1: Denominator --
Denominator declared before enumeration:             [YES / NO — must be YES]
Candidates unaccounted for (firing+non-firing ≠ N):  {count} [must be 0]

-- Gap 2: Scope gate --
SCOPE GATE present and specific:                     [YES / NO — must be YES]
Out-of-scope candidates included in enumeration:     {count} [must be 0]

-- Gap 3: Exclusion log --
Exclusion log covers all automation layers:          [YES / NO — must be YES]
Anomaly verdicts missing exclusion log reference:    {count} [must be 0]

-- Gap 4: Per-entry obligations --
EOR citations missing from firing entries:           {count} [must be 0]
Firing entries missing Condition (Skipped):          {count} [must be 0]
Non-firing entries missing bilateral counterfactual: {count} [must be 0]
Entries missing Registration Witness:                {count} [must be 0]
Cascade chains without [TERMINAL]:                   {count} [must be 0]

-- Gap 5: Prohibition contracts --
Prohibition breaches detected (any phase):           {count} [must be 0]
```

**Denominator Closure:** `firing + non-firing + unresolved = N` → CLOSED / GAP DETECTED

**Exit condition:** Trigger map produced; CLOSURE CHECK complete; all counters declared; denominator closure stated. When CLOSURE CHECK shows all gaps at zero, the five informal-audit gaps named in the opening are closed.

---

## Variation Comparison

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Role sequence | Scope Arbiter leads; Closure Auditor closes | Single-role sequential | Single-role sequential | Anomaly frame inverted to front | Single-role sequential |
| Output format | Mixed tables + structured entries | Pure table-centric; column = slot | Structured block per phase | Named entry templates | Phase blocks + inertia contrast table |
| Lifecycle emphasis | Role boundaries = phase gates | Light (table structure enforces compliance) | Heavy (four-section per phase) | Medium (entry/exit conditions per phase) | Medium (prohibition blocks prominent) |
| Phrasing register | Formal in gate positions; mandatory for inter-role gates | Neutral/structural | Formal (SHALL/MUST in all gate positions) | Strictly formal (SHALL/MUST everywhere; descriptive gates tagged) | Conversational framing for inertia contrast; formal for obligations |
| Inertia framing | None | None | None | None | Explicit opening contrast: informal audit vs. simulation |
| C-20 mechanism | Closure Auditor role owns the CLOSURE CHECK | CLOSURE CHECK table at end | Phase 6 CLOSURE CHECK as exit artifact | CLOSURE CHECK in Phase 6 | CLOSURE CHECK structured around the five informal-audit gaps |
| C-21 mechanism | Prohibition Contracts as named Arbiter artifact | Not emphasized | PROHIBITION block required per phase section | Prohibition clauses per phase | PROHIBITION blocks per phase |
| C-22 mechanism | Arbiter issues ALL-SLOTS-REQUIRED MANDATE globally | Declared as named structural invariant before first entry | Implied by slot templates; not declared as single rule | Declared in PROTOCOL PREAMBLE | Declared as named mandate; CLOSURE CHECK gap 4 tests it |
