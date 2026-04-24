---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 12
rubric_version: 12
---

# corps-committee -- Prompt Variations R12

## Variation Summary

| ID   | Axis                                                                         | Hypothesis |
|------|------------------------------------------------------------------------------|------------|
| V-01 | Role sequence — sequential tier gate (single axis)                          | Adding an explicit TIER-N-SEQUENCE-COMMIT after each tier's voices — before any next-tier voice can appear — makes challenger objections structurally prior to advocate responses. Without this gate, an LLM can interleave voices or allow advocates to "respond" before challengers have committed their full stance. The test: can a Tier 3 voice appear before TIER-1-SEQUENCE-COMMIT is printed? If yes, role ordering is implied, not enforced. A sequential commit gate makes tier completion a verifiable structural precondition for next-tier entry. |
| V-02 | Output format — table-driven participant voices (single axis)               | Replacing prose voice blocks with structured tables (Role \| Tier \| STANCE \| Primary concern \| INERTIA-FINDING cite) forces completeness: a missing INERTIA-FINDING citation is an empty cell, not a skipped sentence. The DECISIONS, TOKEN TRACE CONFIRMATION, and ACTION ITEMS sections also become tables. Hypothesis: table format reduces silent dropout (C-35, C-36) — a token with no table row is a count mismatch, visible before delivery. |
| V-03 | Lifecycle emphasis — explicit phase ENTER/EXIT contracts (single axis)      | Placing PHASE-N-ENTER: preconditions before each phase begins — and PHASE-N-EXIT: conditions before each COMMIT seal fires — makes manifest currency a structural gate rather than a fill rule. The C-34 RECOMMIT MANIFEST check becomes a PHASE-N-ENTER item: "if AMEND occurred, verify current-version RECOMMIT MANIFEST present before proceeding." Without explicit ENTER gates, phase re-entry after AMEND can bypass the manifest currency check. With them, the check is architecturally unavoidable. |
| V-04 | Combination: role sequence + output format (V-01 + V-02)                   | Pairing sequential tier gates with table-driven output creates complementary enforcement: tier gates prevent out-of-order voices; tables prevent silent field dropout within each voice. V-01 closes the inter-tier ordering gap; V-02 closes the intra-voice completeness gap. Together they address C-02 (role-consistent voice) and C-35/C-36 (token manifest and confirmation completeness) from orthogonal angles. |
| V-05 | Full integration: role sequence + output format + lifecycle gates (V-01–V-03) | All three structural axes applied: sequential tier gates close inter-tier ordering; table format closes intra-voice dropout; explicit phase ENTER/EXIT contracts close phase re-entry after AMEND. V-05 is the only variation where a DROPPED token, an out-of-tier voice, and a missing RECOMMIT MANIFEST each produce a structurally detectable mismatch before delivery — count gap, missing TIER-N-SEQUENCE-COMMIT, and PHASE-N-ENTER gate failure respectively. |

---

## V-01 -- Sequential Tier Gate

**Axis:** Role sequence — TIER-N-SEQUENCE-COMMIT gate
**Hypothesis:** An explicit TIER-N-SEQUENCE-COMMIT after all voices in a tier, blocking any
next-tier voice until the seal appears, makes challenger-first ordering a verifiable structural
constraint rather than a positional convention. This prevents voice interleaving and ensures
dissenting stances are committed before advocates can respond.

```
---
name: org-committee
description: Committee meeting simulation for ROB, shiproom, or architecture board.
allowed-tools: [Read, Write, Glob]
param_set: standard
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure

for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


## BEFORE YOU START

Type-specific primary obligations and fail conditions (C-13):

ROB: Produce a readiness verdict backed by named metric evidence.
  FAIL: "If there is no metric cited in the discussion, you have not done a ROB." — C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with a stated blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO decision line in the verdict, you have not done a shiproom." — C-01 miss

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: "If there are no named alternatives compared, you have not done an arch-board." — C-01 miss

COMMON ROLE FAIL: Any participant speaking from the wrong role orientation = C-02 miss.
  FAILS: PM raises deployment topology as primary concern — C-02
  FAILS: SRE leads product vision discussion — C-02

Read this block fully. Do not begin the skeleton until this block is complete.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins — verified for both structural presence and affirmation correctness.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
=== org:committee SIMULATION -- SKELETON (V-01: Sequential Tier Gate) ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would
            not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional.
 Continue INVESTIGATION-ATTEMPT-N / GATE-N until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Downstream CITE: and RESPONDS-TO: valid only against these four labels.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

### TIER SORT

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

### TOKEN TRACE CONFIRMATION

| Token              | Status              | Tier Sort usage or justification          |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (must equal PHASE-1-COMMIT sealed token count N=4).
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED
  DROPPED REPAIR RULE: any DROPPED token requires INVESTIGATION-ATTEMPT-N+1 before
    Phase 2 closes.

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, TOKEN TRACE
  CONFIRMATION complete, DROPPED count = ___.
  Sealed tokens: tier-assignments, confirmation-table [N=4 rows]
  Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- charter role maps to inertia perspective /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

[All Tier 1 voices must complete before any Tier 2 voice begins.]
[All Tier 2 voices must complete before any Tier 3 voice begins.]

### --- TIER 1: CHALLENGERS ---

### ___ -- Tier 1

STANCE: ___
___
[CITE: INERTIA-FINDING-* required for Tier 1]

[Repeat for each Tier 1 participant]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete. Stances committed:
  [list each Tier 1 role and their STANCE token].
  No Tier 2 voice may appear before this line.
  | ENFORCE: terminal position in Tier 1 block.

### --- TIER 2: CONDITIONALS ---

### ___ -- Tier 2

STANCE: ___
___
[specific approval condition required; "address concerns" fails -- C-07]

[Repeat for each Tier 2 participant]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete. Stances committed:
  [list each Tier 2 role and their STANCE token].
  No Tier 3 voice may appear before this line.
  | ENFORCE: terminal position in Tier 2 block.

### --- TIER 3: ADVOCATES ---

### ___ -- Tier 3

STANCE: ___
CITE: ___ -- ___
RESPONDS-TO: "___" -- ___
___

[Repeat for each Tier 3 participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant -- format: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-COMMIT: [locked] -- All voices complete in Tier 1 -> 2 -> 3 order with
  TIER-1-SEQUENCE-COMMIT and TIER-2-SEQUENCE-COMMIT both present.
  Sealed tokens: [list all role stances] [N=___]
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ -- ___ -- ___
[one row per item: Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role -- objection citing INERTIA-FINDING-* label -- resolution
 path -- named authority -- concrete trigger]

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written.
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type using recognized labels only.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified` -- C-01
  FAILS: `Committee Type -- product review` -- non-standard label; C-01
PRINT: PHASE-0-COMMIT with Sealed tokens field enumerating: Committee-Type,
  Agenda-Item, Charter-Source, Participant-roster.
  VALIDATE: all four tokens named explicitly -- C-35

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D per label spec:
  A -- specific workflow or tool in production this agenda item displaces
  B -- specific integration surface at risk; name systems, APIs, or contracts
  C -- team whose cognitive habit would break; name team and the habit
  D -- non-obvious switching cost the proposal author did not account for

VALIDATE: each finding opens with full token label as first element.
  ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-workflow -- ...`
  FAILS: `(a) legacy-approval-workflow` -- C-27
  FAILS: `Finding A: ...` -- C-27

GATE-N retry rule: if INERTIA-FINDING-D is obvious, increment N and rewrite all four.
  Continue until GATE-N = YES.

WRITE: ## INERTIA RECORD with one-phrase anchors.
WRITE: INERTIA INVARIANT line with commit reference and modification prohibition.
  FAILS (a): commit reference present, prohibition absent -- C-35
  FAILS (b): neither element -- C-35
  FAILS (c): line absent -- C-35

PRINT: PHASE-1-COMMIT with Sealed tokens enumeration: INERTIA-FINDING-A,
  INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4].
  VALIDATE: token count explicitly stated; abbreviation or omission fails C-35.

---

**PHASE 2 fill rules:**

ASSIGN tiers by charter orientation:
  Tier 1 (CHALLENGERS): feasibility scrutiny, risk, disruption of existing systems
  Tier 2 (CONDITIONALS): conditional approval holders
  Tier 3 (ADVOCATES): aligned with proposal goals

SORT-CHECK:
PRINT: Test and Result. IF YES: name mis-sorted role, reprint corrected TIER SORT,
  loop until NO.
  FAILS: correct ordering without SORT-CHECK gate present -- C-25

TOKEN TRACE CONFIRMATION fill rules:
PRINT: table with four rows -- one per sealed token from PHASE-1-COMMIT.
ASSIGN status from vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED.
  CONSUMED: token cited in tier sort rationale or dissent assignment
  NOT-APPLICABLE: token is out of scope -- must cite Phase 0 charter constraint; vague
    justification ("not relevant") fails; cite the specific charter entry -- C-36
  DROPPED: token was not consumed and cannot be excluded by charter -- triggers REPAIR RULE
DROPPED REPAIR RULE: if any DROPPED status assigned, reopen Phase 1 for one more
  INVESTIGATION-ATTEMPT before Phase 2 can close.
PRINT: CONFIRMATION INVARIANT with Row count = 4.
  VALIDATE: row count matches PHASE-1-COMMIT N value.
  FAILS: fewer than 4 rows -- count mismatch; C-36 miss
  FAILS: "DROPOUT" or binary vocabulary -- three-way status required; C-36 miss

PRINT: PHASE-2-COMMIT with Sealed tokens field enumerating tier-assignments and
  confirmation-table token list. State DROPPED count explicitly (0 if clean).

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

INSPECT: tier sort for any Tier 1 or Tier 2 participant whose orientation maps to
  switching-cost investigation.
CONFIRM: YES if such participant exists; proceed to Phase 3.
CONFIRM: NO if none exists:
  INJECT: Inertia-Advocate as Tier 1 participant -- speaks first.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label in voice.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.

VALIDATE two independent FAILS axes:
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE -- C-46
  FAILS (incorrect affirmation): YES declared when no Tier 1/Tier 2 maps to inertia -- C-49

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE ENFORCEMENT (V-01 axis):
ENFORCE: ALL Tier 1 voices must complete and TIER-1-SEQUENCE-COMMIT must be printed
  before any Tier 2 voice begins.
ENFORCE: ALL Tier 2 voices must complete and TIER-2-SEQUENCE-COMMIT must be printed
  before any Tier 3 voice begins.
  FAILS: any Tier N+1 voice appearing before TIER-N-SEQUENCE-COMMIT -- C-02 ordering miss
  FAILS: TIER-N-SEQUENCE-COMMIT missing even if tier ordering appears correct -- gate absent;
    ordering is implied, not enforced; C-25 miss

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line.
  FAILS: stance embedded in prose -- C-02
  FAILS: qualified token like `STANCE: BLOCK (pending)` -- C-02

WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails -- C-07.
REQUIRE (Tier 3): CITE: [label -- content] and RESPONDS-TO: "[named concern]" before endorsement.

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST after all voices.
WRITE: STANCE INVARIANT with commit reference and modification prohibition.
PRINT: PHASE-3-COMMIT with Sealed tokens enumerating all role stances by name [N=K].
  VALIDATE: token count matches ## STANCE MANIFEST entry count.
  Bidirectionality clause: both coupling directions named (modifications to manifest require
  updating commit; modifications to commit require updating manifest).
  FAILS: one direction only -- C-45

---

**PHASE 4 fill rules:**

PRINT: TALLY counting tokens in ## STANCE MANIFEST only; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY:
  All APPROVE -> APPROVED
  Any CONDITION no BLOCK -> APPROVED WITH CONDITIONS
  Any BLOCK -> BLOCKED or DEFERRED
VALIDATE: counts match ## STANCE MANIFEST exactly.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role, not a team) and Trigger (named artifact + recipient
  + authority). Missing either fails C-23.
PRINT: action items as [Owner Role] -- [specific action] -- [deadline]; all three required.
WRITE: dissent per CONDITION/BLOCK stance citing INERTIA-FINDING-* label, resolution path,
  named authority.
ENFORCE: if no dissent -- `No dissent -- [reason]`.

---

**AMEND fill rules (C-30, C-33, C-34):**

If AMEND is invoked after simulation complete:

PRINT: AMEND ROUTING TABLE:
  | Amendment Type           | Invalidates           | Re-execution scope  |
  |--------------------------|----------------------|---------------------|
  | Add attendee             | Phase 0, Phase 3     | Phase 0 -> Phase 3+ |
  | Change scope             | Phase 0 -> Phase 5   | Full re-execution   |
  | Change committee type    | Phase 0 -> Phase 5   | Full re-execution   |
  | Inject role post-Phase 2 | Phase 3 -> Phase 5   | Phase 3 -> Phase 5  |

PRINT: AMEND-AFFECTED SITES before any re-execution:
  List each output element rendered stale: [element -- token -- reason stale]

RECOMMIT MANIFEST (C-34): After each invalidated phase re-executes, before the next phase
  resumes, emit:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta: tokens added: [list], tokens removed: [list], tokens modified: [list]
    Version: v[K+1] (supersedes v[K])
    Phase re-entry gate: manifest is current; downstream phases may resume.
  PHASE-REENTRY-COMMIT: [locked] -- PHASE-[N]-RECOMMIT MANIFEST v[K+1] present and current.
    Downstream phases do not gate on original v1 seals; gate on this manifest only.
    FAILS: phase resumes without emitting RECOMMIT MANIFEST -- C-34 miss
    FAILS: phase re-entry references original v1 PHASE-[N]-COMMIT as sufficient -- C-34 miss
```

---

## V-02 -- Table-Driven Output Format

**Axis:** Output format -- structured tables for participant voices
**Hypothesis:** Replacing prose voice blocks with structured tables forces completeness at the
field level: an empty INERTIA-FINDING citation cell is a visible gap, not a skipped sentence.
Combined with C-35 token enumeration in COMMIT seals and C-36 CONFIRMATION as a native table,
the entire skill output becomes machine-scannable and silent dropout produces a visible empty
cell or count mismatch rather than an absent sentence.

```
---
name: org-committee
description: Committee meeting simulation for ROB, shiproom, or architecture board.
allowed-tools: [Read, Write, Glob]
param_set: standard
---
depth: standard
for: {value}


## BEFORE YOU START

Type-specific primary obligations and fail conditions (C-13):

ROB: Produce a readiness verdict backed by named metric evidence.
  FAIL: "If there is no metric in the output, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with a stated blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO decision line, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: "If there are no named alternatives compared, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: Participant speaking from wrong role orientation = C-02 miss.

Read this block. Do not begin the skeleton until complete.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-02: Table-Driven Output) ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |
[repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost not anticipated by the author?
  Answer: ___ [YES / NO]
  Basis: ___

## INERTIA RECORD

| Token              | One-phrase anchor                                      |
|--------------------|--------------------------------------------------------|
| INERTIA-FINDING-A  | ___                                                    |
| INERTIA-FINDING-B  | ___                                                    |
| INERTIA-FINDING-C  | ___                                                    |
| INERTIA-FINDING-D  | ___                                                    |

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-COMMIT: [locked] -- Investigation complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

### TIER SORT

| Role              | Tier  | Rationale (charter orientation -> tier assignment) |
|-------------------|-------|----------------------------------------------------|
| ___               | ___   | ___                                                |
[repeat per participant]

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]

### TOKEN TRACE CONFIRMATION

| Token              | Status              | Tier Sort usage or charter citation       |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (must equal PHASE-1-COMMIT N=4). DROPPED count: ___

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## PHASE 3 -- PARTICIPANT VOICES

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |
[Tier 1 rows]
| ___                 | 2    | ___       | Condition: ___ [specific deliverable]     | --                   |
[Tier 2 rows]
| ___                 | 3    | ___       | RESPONDS-TO: "___". ___                   | CITE: INERTIA-FINDING-___ |
[Tier 3 rows]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |
[repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-COMMIT: [locked] -- All voices in Tier 1 -> 2 -> 3 table order.
  Sealed tokens: [list all role stances by name] [N=___]
  Phase 4 TALLY derives from ## STANCE MANIFEST token count only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

### DECISIONS

| Field                       | Value                                              |
|-----------------------------|---------------------------------------------------|
| Verdict                     | ___                                               |
| Conditions for full approval| ___                                               |
| Re-entry owner              | ___                                               |
| Re-entry trigger            | ___                                               |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |
[one row per item]

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-COMMIT: [locked] -- All tables complete. Owner and Trigger present if not APPROVED.
  Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/`.
ENFORCE: fallback participants if no charter: PM, Architect, Inertia-Advocate.
PRINT: participant table with Role and Orientation columns; one row per participant.
PRINT: PHASE-0-COMMIT with Sealed tokens enumerating four items.
  VALIDATE: all four token names present -- C-35
  FAILS: Sealed tokens field absent -- C-35 miss

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D. Each opens with its full token label.
  FAILS: parenthesized letter like `(a)` -- C-27
  FAILS: abbreviated `Finding A:` -- C-27

GATE-N retry: if INERTIA-FINDING-D is obvious, rerun all four. Loop until GATE-N = YES.

WRITE: ## INERTIA RECORD as a table with Token and One-phrase anchor columns.
  FAILS: bare token with no anchor content -- C-35
  FAILS: placeholder text `[one-phrase anchor]` -- C-35

WRITE: INERTIA INVARIANT with commit reference and modification prohibition.
PRINT: PHASE-1-COMMIT with Sealed tokens: INERTIA-FINDING-A, B, C, D [N=4].
  VALIDATE: all four token names enumerated and count stated -- C-35
  FAILS: "Sealed tokens: findings A-D" -- abbreviated; full labels required -- C-35

---

**PHASE 2 fill rules:**

PRINT: TIER SORT as table with Role, Tier, Rationale columns.
  Tier 1: feasibility scrutiny, risk, disruption of existing systems
  Tier 2: conditional approval holders
  Tier 3: proposal advocates
SORT-CHECK: print Test and Result. IF YES: name mis-sorted role, reprint corrected table.
  FAILS: correct table without SORT-CHECK gate -- C-25

TOKEN TRACE CONFIRMATION fill rules:
PRINT: four-row table, one row per PHASE-1-COMMIT sealed token.
ASSIGN status: CONSUMED | NOT-APPLICABLE | DROPPED
  CONSUMED: token cited in tier sort rationale (Rationale column)
  NOT-APPLICABLE: cite specific Phase 0 charter constraint in usage column; vague entries fail -- C-36
  DROPPED: triggers REPAIR RULE -- reopen Phase 1 for INVESTIGATION-ATTEMPT-N+1 before
    Phase 2 closes
PRINT: CONFIRMATION INVARIANT with Row count = 4.
  VALIDATE: row count = N from PHASE-1-COMMIT -- C-36
  FAILS: fewer than 4 rows -- count mismatch; C-36 miss
  FAILS: binary CONFIRMED/DROPOUT vocabulary -- three-way status required; C-36 miss
PRINT: PHASE-2-COMMIT with DROPPED count stated.

---

**INERTIA CONTINUITY BRIDGE:**

INSPECT: Tier Sort table for inertia-oriented Tier 1/Tier 2 participant.
CONFIRM YES/NO. If NO: INJECT Inertia-Advocate -- Tier 1, speaks first, cites INERTIA-FINDING-*.
VALIDATE:
  FAILS (structural absence): Phase 3 begins without Bridge section -- C-46
  FAILS (incorrect affirmation): YES when no qualifying participant exists -- C-49

---

**PHASE 3 fill rules:**

PRINT: participant voice table with columns: Role, Tier, STANCE, Primary concern, INERTIA-FINDING cite.
  TABLE ORDER: all Tier 1 rows before any Tier 2 row; all Tier 2 rows before any Tier 3 row.
  FAILS: Tier N+1 row appearing before all Tier N rows complete -- C-02 ordering miss

VALIDATE STANCE cell: [BLOCK / CONDITION / APPROVE] -- no qualification.
  FAILS: "BLOCK (pending)" in cell -- C-02
  FAILS: stance inferred from Primary concern prose only -- C-02

Tier 1 rows: INERTIA-FINDING cite cell required; named label from ## INERTIA RECORD.
Tier 2 rows: Primary concern cell must name specific approval condition; not "address concerns" -- C-07.
Tier 3 rows: Primary concern cell opens with RESPONDS-TO: "[named concern]". INERTIA-FINDING cite
  cell must name a label and content. Endorsement follows.

VALIDATE: at least one CONDITION or BLOCK row in table; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST as table. WRITE: STANCE INVARIANT.
PRINT: PHASE-3-COMMIT with Sealed tokens enumerating all role stances [N=K].
  Bidirectionality clause required: modifications to manifest require updating commit;
  modifications to commit require updating manifest. FAILS: one direction only -- C-45

---

**PHASE 4 fill rules:**

TALLY: count STANCE-TOKEN column in ## STANCE MANIFEST only; do not re-parse prose.
OUTCOME: APPROVED / APPROVED WITH CONDITIONS / BLOCKED or DEFERRED per TALLY rules.

---

**PHASE 5 fill rules:**

DECISIONS table: Verdict, Conditions, Re-entry owner (named role, not team), Re-entry trigger
  (named artifact + recipient + authority). Owner and Trigger required if not APPROVED -- C-23.
ACTION ITEMS table: all three columns required (Owner Role, Specific action, Deadline).
  FAILS: missing Deadline cell -- C-04 miss
DISSENTING OPINIONS table: one row per CONDITION/BLOCK stance. Each row: objection + INERTIA-FINDING
  cite, resolution path, named authority, trigger.
  ENFORCE: if no dissent -- single row: [No dissent | [reason] | -- | -- | --]

---

**AMEND fill rules (C-30, C-33, C-34):**

AMEND ROUTING TABLE:
  | Amendment Type           | Invalidates           | Re-execution scope  |
  |--------------------------|----------------------|---------------------|
  | Add attendee             | Phase 0, Phase 3     | Phase 0 -> Phase 3+ |
  | Change scope             | Phase 0 -> Phase 5   | Full                |
  | Change committee type    | Phase 0 -> Phase 5   | Full                |

AMEND-AFFECTED SITES: list stale table cells before re-execution; format:
  [Phase -- table -- column -- token -- reason stale]

RECOMMIT MANIFEST (C-34): after re-execution of each invalidated phase, before next phase resumes:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta: cells added: [list], cells removed: [list], cells modified: [list]
    Version: v[K+1] supersedes v[K].
    Gate: downstream phases may resume only after this manifest is present.
  FAILS: phase resumes without RECOMMIT MANIFEST -- C-34 miss
  FAILS: downstream phase gates on v1 seal rather than current-version RECOMMIT MANIFEST -- C-34 miss
```

---

## V-03 -- Explicit Phase Entry/Exit Contracts

**Axis:** Lifecycle emphasis -- PHASE-N-ENTER / PHASE-N-EXIT conditions
**Hypothesis:** Placing explicit ENTER preconditions before each phase's content block -- and
explicit EXIT conditions before each COMMIT seal -- makes manifest currency (C-34) a structural
gate. After AMEND, the PHASE-N-ENTER check for the re-entered phase explicitly verifies that a
current-version RECOMMIT MANIFEST is present. Without this check, a phase can resume based on
the original v1 COMMIT seal, silently skipping the version currency requirement.

```
---
name: org-committee
description: Committee meeting simulation for ROB, shiproom, or architecture board.
allowed-tools: [Read, Write, Glob]
param_set: standard
---
depth: standard
for: {value}


## BEFORE YOU START

Type-specific primary obligations and fail conditions (C-13):

ROB: Produce a readiness verdict backed by named metric evidence.
  FAIL: "If there is no metric, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with stated blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO decision line, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: "If there are no named alternatives, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: wrong-role voice = C-02 miss.

Read this block fully before beginning.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant. INERTIA CONTINUITY BRIDGE injects one if
no charter inertia owner exists.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-03: Phase Entry/Exit Contracts) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___

PHASE-0-EXIT:
  [ ] Committee Type declared using recognized label
  [ ] Agenda Item stated
  [ ] Charter Source named (or fallback declared)
  [ ] Participant roster complete
  All checks: ___ [PASS / FAIL -- identify failing item]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

PHASE-1-ENTER:
  Precondition: PHASE-0-COMMIT present and EXIT checks all PASS.
  If AMEND has occurred invalidating Phase 1: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt -- emit PHASE-1-RECOMMIT MANIFEST before proceeding.
  Entering Phase 1.

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have
            anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-EXIT:
  [ ] INERTIA-FINDING-A through D each open with full token label
  [ ] ## INERTIA RECORD populated with content anchors (no placeholders)
  [ ] INERTIA INVARIANT line present with commit reference and modification prohibition
  [ ] Sealed tokens enumeration prepared: INERTIA-FINDING-A, B, C, D [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS, N=4 sealed tokens available.
  If AMEND has occurred invalidating Phase 2: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt -- emit PHASE-2-RECOMMIT MANIFEST before proceeding.
  Entering Phase 2.

### TIER SORT

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]

### TOKEN TRACE CONFIRMATION

| Token              | Status              | Usage citation or charter justification   |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4). DROPPED count: ___

PHASE-2-EXIT:
  [ ] TIER SORT assignments declared
  [ ] SORT-CHECK printed with explicit Result
  [ ] TOKEN TRACE CONFIRMATION table has 4 rows (= N=4)
  [ ] All status cells use CONSUMED / NOT-APPLICABLE / DROPPED vocabulary
  [ ] DROPPED count stated (0 if clean); DROPPED REPAIR RULE invoked if count > 0
  [ ] Sealed tokens prepared for PHASE-2-COMMIT
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete,
  DROPPED count = ___.
  Sealed tokens: tier-assignments, confirmation-table [N=4 rows]
  Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## PHASE 3 -- PARTICIPANT VOICES

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present, EXIT checks PASS, INERTIA CONTINUITY BRIDGE declared.
  If AMEND has occurred invalidating Phase 3: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt -- emit PHASE-3-RECOMMIT MANIFEST before proceeding.
  Entering Phase 3.

[Tier 1 -> Tier 2 -> Tier 3 order]

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___        [Tier 3]
RESPONDS-TO: "___" -- ___  [Tier 3]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-EXIT:
  [ ] All participants have a voice block in Tier 1 -> 2 -> 3 order
  [ ] Each voice block has STANCE: as standalone labeled line
  [ ] Tier 1 voices each cite INERTIA-FINDING-* label
  [ ] Tier 2 voices each name a specific condition
  [ ] Tier 3 voices each have CITE: and RESPONDS-TO: before endorsement
  [ ] At least one CONDITION or BLOCK in ## STANCE MANIFEST
  [ ] Sealed tokens enumeration prepared: [all role stances] [N=K]
  All checks: ___ [PASS / FAIL]

PHASE-3-COMMIT: [locked] -- All voices complete, Tier 1 -> 2 -> 3 order.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to STANCE MANIFEST require updating this commit; modifications to
  this commit require updating STANCE MANIFEST.
  Phase 4 TALLY derives from ## STANCE MANIFEST token count only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

PHASE-4-ENTER:
  Precondition: PHASE-3-COMMIT present, EXIT checks PASS.
  If AMEND has occurred invalidating Phase 4: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt.
  Entering Phase 4.

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

PHASE-5-ENTER:
  Precondition: PHASE-4-COMMIT present.
  If AMEND has occurred invalidating Phase 5: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt.
  Entering Phase 5.

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ -- ___ -- ___

### DISSENTING OPINIONS

___

PHASE-5-EXIT:
  [ ] Verdict matches OUTCOME from Phase 4 exactly
  [ ] Conditions stated as specific deliverables (not "address feedback")
  [ ] Owner and Trigger present if verdict not APPROVED
  [ ] Every action item has Owner Role, specific action, and deadline
  [ ] Every CONDITION/BLOCK role has a dissent entry citing INERTIA-FINDING-* label
  All checks: ___ [PASS / FAIL]

PHASE-5-COMMIT: [locked] -- EXIT checks PASS. DECISIONS, ACTION ITEMS, and DISSENTING
  OPINIONS written. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**General phase entry/exit fill rule (C-15 axis):**

EVERY phase begins by printing its PHASE-N-ENTER block:
  1. State precondition (which prior COMMIT must be present).
  2. If AMEND has occurred and this phase was invalidated: check whether current-version
     RECOMMIT MANIFEST is present. If not -- HALT; emit RECOMMIT MANIFEST before proceeding.
  3. Print "Entering Phase N."
EVERY phase ends by printing its PHASE-N-EXIT block:
  1. Print each checkbox item.
  2. State All checks: PASS or identify the failing item.
  3. Emit PHASE-N-COMMIT only after All checks: PASS.
  FAILS: PHASE-N-COMMIT fires without PHASE-N-EXIT block present -- C-15 miss
  FAILS: PHASE-N-EXIT checks not evaluated (printed but not filled) -- C-15 miss

**PHASE 0 fill rules:** [identical to V-01 base; ENTER is no-op first phase]

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D, full token labels.
GATE-N retry until YES.
WRITE: ## INERTIA RECORD, one-phrase anchors.
WRITE: INERTIA INVARIANT.
FILL: PHASE-1-EXIT checklist -- confirm each item before printing PHASE-1-COMMIT.
PRINT: PHASE-1-COMMIT with Sealed tokens: A, B, C, D [N=4] -- C-35.

**PHASE 2 fill rules:**

PHASE-2-ENTER: check PHASE-1-COMMIT present. If AMEND invalidated Phase 2:
  state "PHASE-2-RECOMMIT MANIFEST v[K+1] present? YES" only after emitting it.
  FAILS: proceeding past PHASE-2-ENTER without current-version RECOMMIT MANIFEST
  when Phase 2 was invalidated by AMEND -- C-34 miss

WRITE: TIER SORT, SORT-CHECK.
WRITE: TOKEN TRACE CONFIRMATION table, four rows.
  CONSUMED / NOT-APPLICABLE / DROPPED -- three-way required -- C-36.
  NOT-APPLICABLE requires specific Phase 0 charter citation.
  DROPPED triggers REPAIR RULE -- reopen Phase 1.
FILL: PHASE-2-EXIT checklist.
PRINT: PHASE-2-COMMIT.

**INERTIA CONTINUITY BRIDGE:** [same as V-01]

**PHASE 3 fill rules:**

PHASE-3-ENTER: check PHASE-2-COMMIT present and INERTIA CONTINUITY BRIDGE declared.
  If AMEND invalidated Phase 3: current-version RECOMMIT MANIFEST required -- C-34.

WRITE: voices in Tier 1 -> 2 -> 3 order.
  Tier 1: CITE INERTIA-FINDING-* label.
  Tier 2: specific condition.
  Tier 3: CITE: + RESPONDS-TO: before endorsement.
WRITE: ## STANCE MANIFEST, STANCE INVARIANT.
FILL: PHASE-3-EXIT checklist.
PRINT: PHASE-3-COMMIT with Sealed tokens [N=K]; bidirectionality clause.
  FAILS: one coupling direction -- C-45.

**PHASE 4 fill rules:** [same; ENTER checks PHASE-3-COMMIT]

**PHASE 5 fill rules:**

PHASE-5-ENTER: check PHASE-4-COMMIT.
WRITE: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS.
FILL: PHASE-5-EXIT checklist. All checks PASS required.
PRINT: PHASE-5-COMMIT.

---

**AMEND fill rules (C-30, C-33, C-34):**

On AMEND invocation:
PRINT: AMEND ROUTING TABLE (same as V-01).
PRINT: AMEND-AFFECTED SITES (elements stale by amendment).

RECOMMIT MANIFEST protocol (C-34):
After each invalidated phase re-executes:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta: tokens added/removed/modified vs prior version.
    Version: v[K+1] supersedes v[K].
  PHASE-REENTRY-COMMIT: manifest present and current.

VALIDATE: next phase's PHASE-[N+1]-ENTER block checks for current-version manifest explicitly.
  "If AMEND has occurred invalidating this phase: RECOMMIT MANIFEST v___ present? YES"
  The ENTER check is the enforcement surface for C-34: it cannot be satisfied by a v1 seal.
  FAILS: ENTER block says "PHASE-[N]-COMMIT present" without version currency check after AMEND -- C-34 miss
```

---

## V-04 -- Sequential Tier Gate + Table-Driven Output

**Axis combination:** Role sequence (V-01) + Output format (V-02)
**Hypothesis:** Tier gates prevent inter-tier voice ordering violations; table format prevents
intra-voice field dropout. V-01 closes the ordering gap: challengers cannot be preempted.
V-02 closes the completeness gap: empty cells are visible misses. Together they address
C-02 (role ordering), C-04 (action items with owners), C-35 (token manifest), and C-36
(CONFIRMATION count integrity) from orthogonal enforcement surfaces.

```
---
name: org-committee
description: Committee meeting simulation for ROB, shiproom, or architecture board.
allowed-tools: [Read, Write, Glob]
param_set: standard
---
depth: standard
for: {value}


## BEFORE YOU START

Type-specific primary obligations and fail conditions (C-13):

ROB: Produce a readiness verdict backed by named metric evidence.
  FAIL: "If there is no metric, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with stated blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO decision line, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: "If there are no named alternatives, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: wrong-role voice = C-02 miss. FILLS: criterion ID -- C-14.

Read this block. Do not begin skeleton until complete.

---

You are running `org:committee`. Execute: (1) print skeleton, (2) fill it.
INERTIA CONTINUITY BRIDGE injects Inertia-Advocate if no charter inertia owner exists.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-04: Tier Gate + Table Format) ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          | Assigned Tier |
|-------------------|------------------------------|---------------|
| ___               | ___                          | ___           |

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost not anticipated by the author?
  Answer: ___ [YES / NO]
  Basis: ___

## INERTIA RECORD

| Token              | One-phrase anchor                                      |
|--------------------|--------------------------------------------------------|
| INERTIA-FINDING-A  | ___                                                    |
| INERTIA-FINDING-B  | ___                                                    |
| INERTIA-FINDING-C  | ___                                                    |
| INERTIA-FINDING-D  | ___                                                    |

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-COMMIT: [locked] -- Investigation complete, GATE YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

### TIER SORT

| Role              | Tier  | Charter rationale -> tier assignment       |
|-------------------|-------|--------------------------------------------|
| ___               | ___   | ___                                        |

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]

### TOKEN TRACE CONFIRMATION

| Token              | Status              | Usage citation or charter justification   |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4). DROPPED count: ___

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete,
  DROPPED count = ___.
  Sealed tokens: tier-assignments, confirmation-table [N=4 rows]
  Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## PHASE 3 -- PARTICIPANT VOICES

[Tier 1 voices complete before any Tier 2 voice. Tier 2 voices complete before any Tier 3 voice.]

### --- TIER 1: CHALLENGERS ---

| Role                | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|-----------|-------------------------------------------|----------------------|
| ___                 | ___       | ___                                       | INERTIA-FINDING-___  |
[one row per Tier 1 participant]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete. Stances:
  [list Tier 1 roles and STANCE tokens].
  No Tier 2 voice may appear before this line.
  | ENFORCE: terminal position in Tier 1 block.

### --- TIER 2: CONDITIONALS ---

| Role                | STANCE    | Specific approval condition               | -- |
|---------------------|-----------|-------------------------------------------|----|
| ___                 | ___       | ___                                       | -- |
[one row per Tier 2 participant]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete. Stances:
  [list Tier 2 roles and STANCE tokens].
  No Tier 3 voice may appear before this line.
  | ENFORCE: terminal position in Tier 2 block.

### --- TIER 3: ADVOCATES ---

| Role                | STANCE    | RESPONDS-TO + endorsement                 | CITE: INERTIA-FINDING |
|---------------------|-----------|-------------------------------------------|-----------------------|
| ___                 | ___       | RESPONDS-TO: "___". ___                   | INERTIA-FINDING-___   |
[one row per Tier 3 participant]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stances may not be revised without
  reopening Phase 3.

PHASE-3-COMMIT: [locked] -- All voices in Tier 1 -> 2 -> 3 table order.
  TIER-1-SEQUENCE-COMMIT and TIER-2-SEQUENCE-COMMIT both present.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to STANCE MANIFEST require updating this commit; modifications to
  this commit require updating STANCE MANIFEST.
  Phase 4 TALLY derives from ## STANCE MANIFEST token count only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

### DECISIONS

| Field                        | Value                                              |
|------------------------------|---------------------------------------------------|
| Verdict                      | ___                                               |
| Conditions for full approval | ___                                               |
| Re-entry owner               | ___                                               |
| Re-entry trigger             | ___                                               |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-COMMIT: [locked] -- All tables complete. Owner and Trigger present if not APPROVED.
  Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/`. Fallback: PM, Architect, Inertia-Advocate.
PRINT: participant table with Role, Orientation, Tier columns.
PRINT: PHASE-0-COMMIT with Sealed tokens enumerating four items -- C-35.

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D with full token labels.
GATE-N retry until YES.
WRITE: ## INERTIA RECORD as table (Token | One-phrase anchor).
  FAILS: bare token without anchor -- C-35
WRITE: INERTIA INVARIANT.
PRINT: PHASE-1-COMMIT with Sealed tokens: A, B, C, D [N=4] -- C-35.
  FAILS: abbreviated "findings A-D" -- full labels required -- C-35 partial

---

**PHASE 2 fill rules:**

PRINT: TIER SORT table (Role | Tier | Charter rationale).
SORT-CHECK: print Test and Result. IF YES: reprint corrected table; loop until NO.
  FAILS: correct table without SORT-CHECK gate -- C-25

TOKEN TRACE CONFIRMATION:
PRINT: four-row table, one row per sealed token.
STATUS: CONSUMED | NOT-APPLICABLE | DROPPED -- three-way required -- C-36.
  NOT-APPLICABLE: cite specific Phase 0 charter constraint -- C-36.
  DROPPED: REPAIR RULE -- reopen Phase 1.
CONFIRMATION INVARIANT: row count = 4 = N=4 from PHASE-1-COMMIT.
  FAILS: fewer than 4 rows -- count mismatch -- C-36 miss
  FAILS: binary vocab -- C-36 miss

PRINT: PHASE-2-COMMIT with tier-assignments and confirmation-table in Sealed tokens.

---

**INERTIA CONTINUITY BRIDGE:** [same as V-01/V-03]

---

**PHASE 3 fill rules -- V-04 combined axis:**

TIER 1 table fill:
  One row per Tier 1 participant. STANCE cell: BLOCK / CONDITION / APPROVE (no qualification).
  INERTIA-FINDING cite cell: named label from ## INERTIA RECORD; empty cell fails -- C-27 miss.
  If Inertia-Advocate INJECTED: first row in Tier 1 table.
PRINT: TIER-1-SEQUENCE-COMMIT with list of Tier 1 stances.
  FAILS: any Tier 2 row appearing before TIER-1-SEQUENCE-COMMIT line -- C-02 miss

TIER 2 table fill:
  One row per Tier 2 participant. Specific approval condition in cell; "address concerns" fails -- C-07.
PRINT: TIER-2-SEQUENCE-COMMIT with list of Tier 2 stances.
  FAILS: any Tier 3 row appearing before TIER-2-SEQUENCE-COMMIT line -- C-02 miss

TIER 3 table fill:
  RESPONDS-TO: "[named concern]" must open Primary concern cell.
  CITE: label + content in INERTIA-FINDING cite cell.
  FAILS: empty CITE cell -- C-35/C-27 miss

VALIDATE: at least one CONDITION or BLOCK row across all tier tables; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST table. WRITE: STANCE INVARIANT.
PRINT: PHASE-3-COMMIT with Sealed tokens [N=K], bidirectionality clause.
  TIER-1-SEQUENCE-COMMIT and TIER-2-SEQUENCE-COMMIT both verified present.
  FAILS: one coupling direction only -- C-45

---

**PHASE 4 fill rules:** TALLY from STANCE MANIFEST table token column only.

---

**PHASE 5 fill rules:**

DECISIONS table: all four fields required. Owner = named role (not team). Trigger = artifact + recipient + authority.
  FAILS: missing Owner or Trigger row when verdict not APPROVED -- C-23
ACTION ITEMS table: all three columns per row.
  FAILS: missing Deadline cell -- C-04 miss
DISSENTING OPINIONS table: one row per CONDITION/BLOCK stance.
  INERTIA-FINDING cite required in objection cell.
  ENFORCE: if no dissent -- single row with [No dissent | [reason] | -- | -- | --]

---

**AMEND fill rules (C-30, C-33, C-34):**

AMEND ROUTING TABLE: [same as V-01]
AMEND-AFFECTED SITES: list stale table cells and rows before re-execution.
  Format: [Phase -- section -- table column -- token -- reason stale]

RECOMMIT MANIFEST (C-34): after each invalidated phase re-executes, before next phase:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta (table-level): rows added, rows removed, cells modified vs v[K].
    Version: v[K+1] supersedes v[K].
    Gate: downstream phases may resume.
  FAILS: phase resumes without RECOMMIT MANIFEST -- C-34 miss
  FAILS: downstream gates on v1 PHASE-[N]-COMMIT rather than current RECOMMIT MANIFEST -- C-34 miss
```

---

## V-05 -- Full Integration: Sequential Gate + Table Format + Phase Contracts

**Axis combination:** Role sequence (V-01) + Output format (V-02) + Lifecycle emphasis (V-03)
**Hypothesis:** All three structural axes together close every detectable gap in the R12 rubric:
TIER-N-SEQUENCE-COMMIT gates prevent inter-tier ordering violations (C-02); table format
produces visible count mismatches for silent dropout (C-35, C-36); PHASE-N-ENTER/EXIT
contracts make manifest currency an unavoidable structural gate after AMEND (C-34, C-15).
V-05 is the only variation where a DROPPED token, a tier ordering violation, and a missing
RECOMMIT MANIFEST each produce a structurally detectable mismatch before delivery.

```
---
name: org-committee
description: Committee meeting simulation for ROB, shiproom, or architecture board.
allowed-tools: [Read, Write, Glob]
param_set: standard
---
depth: standard
for: {value}


## BEFORE YOU START

Type-specific primary obligations and fail conditions (C-13):

ROB: Produce a readiness verdict backed by named metric evidence.
  FAIL: "If there is no metric, you have not done a ROB." -- C-01 miss
  Fill-rule annotation: missing metric would fail C-01.

SHIPROOM: Produce a binary GO / NO-GO decision with stated blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO decision line, you have not done a shiproom." -- C-01 miss
  Fill-rule annotation: missing decision line would fail C-01.

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: "If there are no named alternatives compared, you have not done an arch-board." -- C-01 miss
  Fill-rule annotation: missing trade-off comparison would fail C-01.

COMMON FAIL: wrong-role voice = C-02 miss. [C-14: fails C-02]
  FAILS example: PM raises deployment topology as primary -- C-02
  FAILS example: SRE leads product vision -- C-02

Read this block fully. Do not begin the skeleton until this block is complete.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant. INERTIA CONTINUITY BRIDGE injects one
if no charter inertia owner exists in the tier sort. Injection is the default assumption;
the skill must actively confirm a qualifying participant exists to declare YES.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-05: Full Integration) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: First phase -- no preconditions.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          | Assigned Tier |
|-------------------|------------------------------|---------------|
| ___               | ___                          | ___           |

PHASE-0-EXIT:
  [ ] Committee Type: recognized label (ROB / shiproom / arch-board)
  [ ] Agenda Item: stated
  [ ] Charter Source: named or fallback declared
  [ ] Participant table: all roles with orientations
  All checks: ___ [PASS / FAIL]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

PHASE-1-ENTER:
  Precondition: PHASE-0-COMMIT present, EXIT checks PASS.
  AMEND reentry check: if Phase 1 was invalidated by AMEND, PHASE-1-RECOMMIT MANIFEST
    v[K+1] must be present before proceeding. [Present? YES / NO -- halt if NO]
  Entering Phase 1.

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would
            not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE NO -> INVESTIGATION-ATTEMPT-N+1 within Phase 1; repeat until YES.]

## INERTIA RECORD

| Token              | One-phrase anchor                                      |
|--------------------|--------------------------------------------------------|
| INERTIA-FINDING-A  | ___                                                    |
| INERTIA-FINDING-B  | ___                                                    |
| INERTIA-FINDING-C  | ___                                                    |
| INERTIA-FINDING-D  | ___                                                    |

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-EXIT:
  [ ] INERTIA-FINDING-A through D each open with full token label
  [ ] INERTIA RECORD table populated (no bare labels, no placeholders)
  [ ] INERTIA INVARIANT: commit reference AND modification prohibition present
  [ ] Sealed tokens list prepared: A, B, C, D [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Modifications to INERTIA RECORD require updating this commit; modifications to this commit
  require updating INERTIA RECORD.
  Downstream CITE: and RESPONDS-TO: valid only against these four labels.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS, N=4 sealed tokens available.
  AMEND reentry check: if Phase 2 invalidated by AMEND, PHASE-2-RECOMMIT MANIFEST v[K+1]
    must be present. [Present? YES / NO -- halt if NO]
  Entering Phase 2.

### TIER SORT

| Role              | Tier  | Charter rationale -> tier assignment       |
|-------------------|-------|--------------------------------------------|
| ___               | ___   | ___                                        |

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  [YES -> name mis-sorted role, reprint corrected TIER SORT, reprint SORT-CHECK; loop until NO]

### TOKEN TRACE CONFIRMATION

| Token              | Status              | Usage citation or charter justification   |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (must equal PHASE-1-COMMIT N=4). DROPPED count: ___

PHASE-2-EXIT:
  [ ] TIER SORT table complete with Role, Tier, Rationale columns
  [ ] SORT-CHECK printed and Result = NO
  [ ] TOKEN TRACE CONFIRMATION: exactly 4 rows (= N from PHASE-1-COMMIT)
  [ ] All status cells: CONSUMED / NOT-APPLICABLE / DROPPED only
  [ ] NOT-APPLICABLE cells each cite a specific Phase 0 charter constraint
  [ ] DROPPED count stated; REPAIR RULE invoked if count > 0
  [ ] Sealed tokens prepared: tier-assignments + confirmation-table [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete,
  DROPPED count = ___.
  Sealed tokens: tier-assignments, confirmation-table [N=4 rows]
  Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- charter Tier 1/Tier 2 role maps to inertia analysis /
                                  NO -- Inertia-Advocate INJECTED -- Tier 1, speaks first]
  [NO -> Inertia-Advocate Tier 1, CITE obligation: at least one INERTIA-FINDING-* in Phase 3 voice]

---

## PHASE 3 -- PARTICIPANT VOICES

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present, EXIT checks PASS, INERTIA CONTINUITY BRIDGE declared.
  AMEND reentry check: if Phase 3 invalidated by AMEND, PHASE-3-RECOMMIT MANIFEST v[K+1]
    must be present. [Present? YES / NO -- halt if NO]
  Entering Phase 3.

[Sequential gate: Tier 1 complete before Tier 2. Tier 2 complete before Tier 3.]

### --- TIER 1: CHALLENGERS ---

| Role                | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|-----------|-------------------------------------------|----------------------|
| ___                 | ___       | ___                                       | INERTIA-FINDING-___  |
[one row per Tier 1 participant; Inertia-Advocate first if INJECTED]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 rows complete.
  Stances: [list Tier 1 roles and STANCE tokens].
  No Tier 2 row may appear before this line.
  | ENFORCE: terminal position in Tier 1 block.

### --- TIER 2: CONDITIONALS ---

| Role                | STANCE    | Specific approval condition               | -- |
|---------------------|-----------|-------------------------------------------|----|
| ___                 | ___       | ___                                       | -- |

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 rows complete.
  Stances: [list Tier 2 roles and STANCE tokens].
  No Tier 3 row may appear before this line.
  | ENFORCE: terminal position in Tier 2 block.

### --- TIER 3: ADVOCATES ---

| Role                | STANCE    | RESPONDS-TO + endorsement                 | CITE: INERTIA-FINDING |
|---------------------|-----------|-------------------------------------------|-----------------------|
| ___                 | ___       | RESPONDS-TO: "___". ___                   | INERTIA-FINDING-___   |

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-EXIT:
  [ ] All Tier 1 rows complete; TIER-1-SEQUENCE-COMMIT present before any Tier 2 row
  [ ] All Tier 2 rows complete; TIER-2-SEQUENCE-COMMIT present before any Tier 3 row
  [ ] Each Tier 1 row: INERTIA-FINDING cite cell non-empty
  [ ] Each Tier 2 row: condition cell is specific (not "address concerns")
  [ ] Each Tier 3 row: RESPONDS-TO: and CITE: both present
  [ ] At least one CONDITION or BLOCK in STANCE MANIFEST
  [ ] Sealed tokens enumeration prepared: [all role stances by name] [N=K]
  All checks: ___ [PASS / FAIL]

PHASE-3-COMMIT: [locked] -- All voices complete, Tier 1 -> 2 -> 3 table order confirmed.
  TIER-1-SEQUENCE-COMMIT and TIER-2-SEQUENCE-COMMIT both present.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to STANCE MANIFEST require updating this commit; modifications to
  this commit require updating STANCE MANIFEST.
  Phase 4 TALLY derives from ## STANCE MANIFEST STANCE-TOKEN column only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

PHASE-4-ENTER:
  Precondition: PHASE-3-COMMIT present, EXIT checks PASS.
  AMEND reentry check: if Phase 4 invalidated by AMEND, PHASE-4-RECOMMIT MANIFEST v[K+1]
    must be present. [Present? YES / NO -- halt if NO]
  Entering Phase 4.

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

PHASE-5-ENTER:
  Precondition: PHASE-4-COMMIT present.
  AMEND reentry check: if Phase 5 invalidated by AMEND, PHASE-5-RECOMMIT MANIFEST v[K+1]
    must be present. [Present? YES / NO -- halt if NO]
  Entering Phase 5.

### DECISIONS

| Field                        | Value                                              |
|------------------------------|---------------------------------------------------|
| Verdict                      | ___                                               |
| Conditions for full approval | ___                                               |
| Re-entry owner               | ___                                               |
| Re-entry trigger             | ___                                               |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-EXIT:
  [ ] Verdict matches OUTCOME exactly
  [ ] Conditions for full approval: specific deliverables (not "address feedback")
  [ ] Owner and Trigger present if verdict not APPROVED
  [ ] Every ACTION ITEMS row has three cells (Owner, action, deadline)
  [ ] Every CONDITION/BLOCK role has a DISSENTING OPINIONS row with INERTIA-FINDING cite
  All checks: ___ [PASS / FAIL]

PHASE-5-COMMIT: [locked] -- EXIT checks PASS. All tables complete. Phase 5 closed.
  Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**General fill protocol (V-05 integrated):**

For every phase:
1. Print PHASE-N-ENTER block. State precondition. Check AMEND reentry condition.
2. Execute phase content per phase-specific fill rules below.
3. Print PHASE-N-EXIT checklist. Evaluate each checkbox. Confirm All checks: PASS.
4. Print PHASE-N-COMMIT only after EXIT PASS confirmed.
   FAILS: COMMIT fires without EXIT block evaluated -- C-15 miss [C-14: would fail C-15]

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/`. Fallback if none: PM, Architect, Inertia-Advocate.
PRINT: participant table (Role | Orientation | Assigned Tier) -- three columns, all populated.
EVALUATE: PHASE-0-EXIT checklist. All four items must PASS.
PRINT: PHASE-0-COMMIT with Sealed tokens: four items named explicitly.
  FAILS: "Sealed tokens: committee metadata" -- abbreviated; all four names required -- C-35 [C-14]

---

**PHASE 1 fill rules:**

AMEND REENTRY: if Phase 1 invalidated by AMEND, emit PHASE-1-RECOMMIT MANIFEST v[K+1]
  before any Phase 1 content. Delta: findings added/removed/modified vs v[K].
  Gate: confirm "Present? YES" in PHASE-1-ENTER. FAILS if gate omitted -- C-34 miss [C-14]

WRITE: INERTIA-FINDING-A through D. Full token label opens each line.
  FAILS: `(a)`, `Finding A:`, or any abbreviated label -- C-27 [C-14]
GATE-N: if FINDING-D is obvious, run INVESTIGATION-ATTEMPT-N+1. Loop until YES.
WRITE: ## INERTIA RECORD table. Non-empty anchor required per row.
  FAILS: bare label, placeholder cell -- C-35 [C-14]
WRITE: INERTIA INVARIANT line. Both elements required: commit reference + modification prohibition.
  FAILS (a): commit reference only, prohibition absent -- C-35 [C-14]
  FAILS (b): neither element in present line -- C-35 [C-14]
  FAILS (c): line absent -- C-35 [C-14]
EVALUATE: PHASE-1-EXIT checklist.
PRINT: PHASE-1-COMMIT. Sealed tokens: INERTIA-FINDING-A, B, C, D [N=4].
  Bidirectionality clause required.
  FAILS: one coupling direction only -- C-45 [C-14]
  FAILS: sealed token count absent -- C-35 [C-14]

---

**PHASE 2 fill rules:**

AMEND REENTRY: if Phase 2 invalidated, check current RECOMMIT MANIFEST in PHASE-2-ENTER.
  FAILS: ENTER block says "PHASE-1-COMMIT present" without version currency check -- C-34 miss [C-14]

PRINT: TIER SORT table. All three columns (Role, Tier, Rationale) per row.
  Tier 1 (CHALLENGERS): feasibility scrutiny, risk, disruption of existing systems.
  Tier 2 (CONDITIONALS): conditional approval holders.
  Tier 3 (ADVOCATES): proposal advocates.
SORT-CHECK: print Test and Result. IF YES: name mis-sorted role, reprint table, loop.
  FAILS: correct table without SORT-CHECK gate -- C-25 [C-14]

TOKEN TRACE CONFIRMATION:
PRINT: four-row table, one row per PHASE-1-COMMIT sealed token (N=4).
ASSIGN STATUS from three-way vocabulary only: CONSUMED | NOT-APPLICABLE | DROPPED.
  CONSUMED: token is cited in Rationale column of TIER SORT table.
  NOT-APPLICABLE: cite specific Phase 0 charter constraint in usage cell.
    FAILS: vague justification "not relevant" -- specific charter citation required -- C-36 [C-14]
  DROPPED: triggers DROPPED REPAIR RULE -- reopen Phase 1 for INVESTIGATION-ATTEMPT-N+1.
    Phase 2 cannot close until DROPPED count = 0.
CONFIRMATION INVARIANT: Row count = 4. Must equal N from PHASE-1-COMMIT.
  FAILS: fewer than 4 rows -- count mismatch -- C-36 [C-14]
  FAILS: binary CONFIRMED/DROPOUT vocabulary -- C-36 [C-14]
  FAILS: row count stated but not equal to N -- C-36 [C-14]
EVALUATE: PHASE-2-EXIT checklist. DROPPED count = 0 required before PASS.
PRINT: PHASE-2-COMMIT.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Tier Sort table. Does any Tier 1 or Tier 2 row have a Rationale mapping to
  switching-cost investigation, status-quo defense, or cost-of-change analysis?
CONFIRM: YES if such row exists; proceed.
CONFIRM: NO if none exists:
  INJECT Inertia-Advocate: Tier 1, first row in Tier 1 table.
  CITE obligation: INERTIA-FINDING-* label in Phase 3 Tier 1 row.
  ENFORCE: Inertia-Advocate present in STANCE MANIFEST.

VALIDATE two FAILS axes:
  FAILS (structural absence): Phase 3 entered without Bridge section -- C-46 [C-14]
  FAILS (incorrect affirmation): YES declared when no qualifying Tier 1/Tier 2 row exists --
    C-49 [C-14]; injection silently absent; inertia perspective lost

---

**PHASE 3 fill rules:**

AMEND REENTRY: check current RECOMMIT MANIFEST in PHASE-3-ENTER before any Tier row.

TIER 1 table:
  One row per Tier 1 participant. Inertia-Advocate first if INJECTED.
  STANCE cell: BLOCK / CONDITION / APPROVE. No qualifications.
    FAILS: "BLOCK (pending)" -- C-02 [C-14]
    FAILS: stance inferred from prose only -- C-02 [C-14]
  INERTIA-FINDING cite cell: named label from ## INERTIA RECORD. Empty cell fails.
    FAILS: empty cell -- C-27 miss [C-14]
PRINT: TIER-1-SEQUENCE-COMMIT with stances listed.
  FAILS: any Tier 2 row appearing before this line -- C-02 [C-14]

TIER 2 table:
  Specific approval condition per row. "Address concerns" fails.
    FAILS: vague condition -- C-07 [C-14]
PRINT: TIER-2-SEQUENCE-COMMIT with stances listed.
  FAILS: any Tier 3 row appearing before this line -- C-02 [C-14]

TIER 3 table:
  RESPONDS-TO: "[named concern]" must open Primary concern cell.
    FAILS: missing RESPONDS-TO -- C-02 [C-14]
  INERTIA-FINDING cite cell: named label + content. Empty cell fails.

VALIDATE: at least one CONDITION or BLOCK row across all tier tables. All-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST (Role | STANCE-TOKEN).
WRITE: STANCE INVARIANT. Both elements required.
EVALUATE: PHASE-3-EXIT checklist.
PRINT: PHASE-3-COMMIT with Sealed tokens [N=K], bidirectionality clause.
  TIER-1-SEQUENCE-COMMIT and TIER-2-SEQUENCE-COMMIT both verified present in EXIT check.
  FAILS: one coupling direction only -- C-45 [C-14]
  FAILS: STANCE INVARIANT missing prohibition -- C-35 [C-14]

---

**PHASE 4 fill rules:**

AMEND REENTRY: check PHASE-4-ENTER.
TALLY: count STANCE-TOKEN column in ## STANCE MANIFEST only.
  FAILS: re-parsing Phase 3 table prose to derive TALLY -- C-36 miss
OUTCOME: APPROVED / APPROVED WITH CONDITIONS / BLOCKED or DEFERRED.
PRINT: PHASE-4-COMMIT.

---

**PHASE 5 fill rules:**

AMEND REENTRY: check PHASE-5-ENTER.
DECISIONS table: all four rows required.
  Owner = named role (not a team or group).
  Trigger = named artifact + recipient + authority.
  FAILS: missing Owner or Trigger when verdict not APPROVED -- C-23 [C-14]
ACTION ITEMS table: all three cells per row.
  FAILS: missing Deadline -- C-04 [C-14]
DISSENTING OPINIONS table: one row per CONDITION/BLOCK stance.
  INERTIA-FINDING cite required in objection cell.
  ENFORCE: if no dissent -- single row: No dissent | [reason] | -- | -- | --
  FAILS: no dissent row for a CONDITION stance -- C-05 [C-14]
EVALUATE: PHASE-5-EXIT checklist. All checks PASS required before COMMIT.
PRINT: PHASE-5-COMMIT.

---

**AMEND fill rules (C-30, C-33, C-34):**

On AMEND invocation:

PRINT: AMEND ROUTING TABLE:
  | Amendment Type           | Invalidates                    | Re-execution scope      |
  |--------------------------|-------------------------------|-------------------------|
  | Add attendee             | Phase 0, Phase 3              | Phase 0 -> Phase 3+     |
  | Change scope             | Phase 0 -> Phase 5            | Full                    |
  | Change committee type    | Phase 0 -> Phase 5            | Full                    |
  | Inject role post-Phase 2 | Phase 3 -> Phase 5            | Phase 3 -> Phase 5      |
  | Amendment type not listed | -- UNHANDLED CASE            | Report; do not infer    |

PRINT: AMEND-AFFECTED SITES before any re-execution:
  | Phase | Section | Table column | Token | Reason stale |
  Per invalidated element; not per phase block.

RECOMMIT MANIFEST (C-34): after each invalidated phase re-executes, emit before next phase:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta: rows/cells added: [list], removed: [list], modified: [list (old -> new)] vs v[K].
    Version: v[K+1] supersedes v[K].
    Phase re-entry gate: this manifest is current; downstream phases may resume.
  PHASE-REENTRY-COMMIT: [locked] -- RECOMMIT MANIFEST v[K+1] present. Gate satisfied.
    Downstream phases gate on this commit, not on original PHASE-[N]-COMMIT v1.

VALIDATE:
  FAILS: invalidated phase resumes without emitting RECOMMIT MANIFEST -- C-34 miss [C-14]
  FAILS: next phase's ENTER block checks original v1 COMMIT without version qualifier -- C-34 miss [C-14]
  FAILS: RECOMMIT MANIFEST present but delta annotations absent -- C-34 partial [C-14]
```
